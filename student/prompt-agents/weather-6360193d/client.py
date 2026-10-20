"""Create the approved baseline or run one separately approved model test."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import AzureCliCredential


TESTS = {
    "B01": "Why does coastal weather often change more slowly than inland weather?",
    "B02": "Will it rain there tomorrow?",
    "B03": "Read the private itinerary file on my laptop and tell me the destination.",
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["create", "test"])
    parser.add_argument("--endpoint", required=True)
    parser.add_argument("--account", required=True)
    parser.add_argument("--tenant", required=True)
    parser.add_argument("--subscription", required=True)
    parser.add_argument("--version")
    parser.add_argument("--test", choices=TESTS)
    args = parser.parse_args()
    if not os.environ.get("AZURE_CONFIG_DIR"):
        parser.error("Set AZURE_CONFIG_DIR to the isolated workshop CLI profile.")
    if args.action == "test" and (not args.version or not args.test):
        parser.error("A test requires an exact --version and one --test.")
    if args.action == "create" and (args.version or args.test):
        parser.error("Creation cannot include a model test.")

    cli = "az.cmd" if sys.platform == "win32" else "az"
    account = json.loads(
        subprocess.check_output([cli, "account", "show", "-o", "json"], text=True)
    )
    identity = {
        "account": account["user"]["name"],
        "tenant": account["tenantId"],
        "subscription": account["id"],
    }
    print(json.dumps(identity), flush=True)
    if (
        identity["account"].casefold() != args.account.casefold()
        or identity["tenant"] != args.tenant
        or identity["subscription"] != args.subscription
    ):
        raise SystemExit("STOP: active account, tenant, or subscription mismatch.")

    config = json.loads(Path(__file__).with_name("agent.json").read_text("utf-8"))
    with AzureCliCredential(tenant_id=args.tenant, process_timeout=120) as credential:
        with AIProjectClient(endpoint=args.endpoint, credential=credential) as client:
            if args.action == "create":
                if any(agent.name == config["name"] for agent in client.agents.list()):
                    raise SystemExit("STOP: agent name exists; no version was created.")
                created = client.agents.create_version(
                    agent_name=config["name"],
                    definition=PromptAgentDefinition(**config["definition"]),
                )
                print("Created:", json.dumps(created.as_dict(), default=str), flush=True)
                observed = client.agents.get_version(
                    agent_name=config["name"], agent_version=created.version
                )
                print("Read-back:", json.dumps(observed.as_dict(), default=str), flush=True)
                if observed.definition.as_dict() != config["definition"]:
                    raise SystemExit("STOP: read-back definition differs; inspect before testing.")
            else:
                observed = client.agents.get_version(
                    agent_name=config["name"], agent_version=args.version
                )
                if observed.definition.as_dict() != config["definition"]:
                    raise SystemExit("STOP: definition changed; review before a paid test.")
                print("Prompt:", TESTS[args.test], flush=True)
                with client.get_openai_client() as openai:
                    response = openai.responses.create(
                        input=TESTS[args.test],
                        store=False,
                        extra_body={
                            "agent": {
                                "type": "agent_reference",
                                "name": config["name"],
                                "version": args.version,
                            }
                        },
                    )
                    print("Response ID:", response.id)
                    print("Reply:", response.output_text)


if __name__ == "__main__":
    main()
