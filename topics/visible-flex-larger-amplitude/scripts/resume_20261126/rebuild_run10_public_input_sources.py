#!/usr/bin/env python3
"""Replay both complete run10 input sources without importing scientific modules.

Only full source bytes, replacement counts, AST and compile objects are
processed. The actual public inputs and generated arrays are never opened.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-larger-amplitude"
SOURCE_DIRECTORY = "scripts/resume_20261126"
COMPLETE_DERIVATIONS = json.loads(r'''[
  {
    "name": "actual_public_run10_reference_input_binding.py",
    "parent_name": "actual_public_reference_input_binding.py",
    "parent_sha256": "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a",
    "parent_bytes": 44907,
    "bytes": 44908,
    "sha256": "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209",
    "complete_edits": [
      {
        "role": "binding_current_labels",
        "old": "run09",
        "new": "run10",
        "count": 8
      },
      {
        "role": "binding_actual_run",
        "old": "45943410994",
        "new": "45972294636",
        "count": 7
      },
      {
        "role": "binding_actual_step",
        "old": "independent-axisymmetric-R690-reference-prepare-v2-first-20261127-09",
        "new": "independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10",
        "count": 1
      },
      {
        "role": "binding_complete_public_record",
        "old": "5e3732096b95ccc65f7fc70cc2b4e5ba4ffc67023c444ce4f93762c7d765a1be",
        "new": "b23954c94ac4f69969dae9768d9ebdc1b77f5a65b82377b48d1cd63c84330583",
        "count": 1
      },
      {
        "role": "binding_actual_model",
        "old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75",
        "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5",
        "count": 1
      },
      {
        "role": "binding_actual_profile",
        "old": "5de7dcbb0fd1daacad7c20b276120dfc52b9d1f2eb67890300c9afc56242b3ed",
        "new": "c46f875f96a41a09ccad4bcfb75ed6efd33e239b28dbcdb538ce9d2daa47bc65",
        "count": 1
      },
      {
        "role": "binding_complete_six_actual_files",
        "old": "ACTUAL_CURRENT_FILES = {\n    \"current_warm_bundle\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.npz\",\n        \"sha256\": \"3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c\",\n        \"bytes\": 8767118\n    },\n    \"current_node_report\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.json\",\n        \"sha256\": \"918ccdf1a132ca4ba50e0fa97cbb53f7aeabac8f63dc24e7eada64a18fb80269\",\n        \"bytes\": 554141\n    },\n    \"current_scalar_input\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz\",\n        \"sha256\": \"83e65252955298326934ee371ace2391ea9161b69a9289ce4a3c5bd74c67c986\",\n        \"bytes\": 14227850\n    },\n    \"current_carrier\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/observations.npz\",\n        \"sha256\": \"792a132357861684ae01b15b2276c0259583ef27c44387288f424e08d6b488bb\",\n        \"bytes\": 227205\n    },\n    \"current_preparation_report\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/report.json\",\n        \"sha256\": \"4cc93d406cc1882771d2ebabb34856e7ed195fb6cdb6b361e1b213e504193ad2\",\n        \"bytes\": 29802\n    },\n    \"current_reference_bundle\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/reference.npz\",\n        \"sha256\": \"2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2\",\n        \"bytes\": 866176\n    }\n}",
        "new": "ACTUAL_CURRENT_FILES = {\n    \"current_warm_bundle\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.npz\",\n        \"sha256\": \"3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c\",\n        \"bytes\": 8767118\n    },\n    \"current_node_report\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/fullclosed-hold-warm.json\",\n        \"sha256\": \"1fed8f9b49202ae67c2d317c3a30d855d7a5d9f486fe034591a23fada2b08268\",\n        \"bytes\": 554141\n    },\n    \"current_scalar_input\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/fullclosed_solver/data/pulse-a5-complete-base.json.gz\",\n        \"sha256\": \"aa7af21dc95861841c2d6cbbe4d5034cce671e796fe8a4346aeb8aa887d8b2c4\",\n        \"bytes\": 14227847\n    },\n    \"current_carrier\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/observations.npz\",\n        \"sha256\": \"71f0048e2c6c973625fd110c6980c24242d2cf67b7dd7da5dd9e889fde26a22d\",\n        \"bytes\": 227202\n    },\n    \"current_preparation_report\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/report.json\",\n        \"sha256\": \"35fdae489de9a7ee205b4f03f805b30107cec382abbdd242ece43f87d857d286\",\n        \"bytes\": 29809\n    },\n    \"current_reference_bundle\": {\n        \"path\": \"/home/runner/work/_temp/visible-larger-research-45972294636-1/research/axisymmetric-R690-reference-v2-first/reference.npz\",\n        \"sha256\": \"512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b\",\n        \"bytes\": 866207\n    }\n}\n",
        "count": 1
      }
    ]
  },
  {
    "name": "freeze_run10_public_reference_and_restore_run05_carrier.py",
    "parent_name": "freeze_run09_public_reference_and_restore_run05_carrier.py",
    "parent_sha256": "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18",
    "parent_bytes": 47041,
    "bytes": 47047,
    "sha256": "fcd20177bed258bc463f5ca6431c29c18c3b381b75146e1da7bbc8bc4e7a475a",
    "complete_edits": [
      {
        "role": "producer_current_labels",
        "old": "run09",
        "new": "run10",
        "count": 9
      },
      {
        "role": "producer_actual_step",
        "old": "independent-axisymmetric-R690-reference-prepare-v2-first-20261127-09",
        "new": "independent-axisymmetric-R690-reference-prepare-v2-first-20261127-10",
        "count": 1
      },
      {
        "role": "producer_complete_immediate_parent",
        "old": "105289ba7c454f671c8eae086b31a4ea01b06978101503cd0ef283320fc85361",
        "new": "9e3d0590c6d37eb07da094128df9e3b82fc03a7e9cf784cea1831b4ab0d39a18",
        "count": 1
      },
      {
        "role": "producer_complete_binding_source_pin",
        "old": "306b5f86e0d287ea0c6cf9abb0f326f0eec869640b52daa59cf76db1492e382a",
        "new": "9f69b860d4bf2e25e707d08c7c85ca01c17ebf468398ea007ad7448df9951209",
        "count": 1
      },
      {
        "role": "producer_complete_binding_source_name",
        "old": "actual_public_reference_input_binding.py",
        "new": "actual_public_run10_reference_input_binding.py",
        "count": 1
      },
      {
        "role": "producer_actual_reference",
        "old": "2ab8593585286a6c4eab78d107f83a02d8332e7ae1747253534264506b3da7f2",
        "new": "512f13149c54b0cce9ca7b1d27fd4139493a480efcc824fe2e083d192d3a222b",
        "count": 1
      },
      {
        "role": "producer_actual_model",
        "old": "d4494b14955535635b8b72b1ed3278fa8f60186d4ef7df5687ca3de5566c2f75",
        "new": "081bdf939b7bdc6d5dfb54bce955fdfbcda90a8cef3668388a8874272e594af5",
        "count": 1
      }
    ]
  }
]''')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def reject_duplicate_literal_keys(tree):
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        seen = set()
        for key in node.keys:
            if key is None:
                continue
            try:
                value = ast.literal_eval(key)
                hash(value)
            except (ValueError, TypeError, SyntaxError):
                continue
            if value in seen:
                raise ValueError("Duplicate literal dictionary key")
            seen.add(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    repo, outdir = args.repo.resolve(), args.outdir.resolve()
    if outdir.exists() or outdir == repo or repo in outdir.parents:
        raise ValueError("Use an independent fresh scratch source staging directory")
    directory = repo / TOPIC / SOURCE_DIRECTORY
    result = []
    staged = {}
    for specification in COMPLETE_DERIVATIONS:
        parent_path = directory / specification["parent_name"]
        original = parent_path.read_bytes()
        if (len(original) != specification["parent_bytes"]
                or digest(original) != specification["parent_sha256"]):
            raise ValueError("The complete parent source changed")
        value = original.decode("utf-8")
        for change in specification["complete_edits"]:
            if value.count(change["old"]) != change["count"]:
                raise ValueError("A complete source replacement count changed: " + change["role"])
            value = value.replace(change["old"], change["new"])
        body = value.encode("utf-8")
        if len(body) != specification["bytes"] or digest(body) != specification["sha256"]:
            raise ValueError("The independently rebuilt full source differs")
        supplied = (directory / specification["name"]).read_bytes()
        if supplied != body:
            raise ValueError("The delivered whole source differs from full independent replay")
        inverse = value
        for change in reversed(specification["complete_edits"]):
            if inverse.count(change["new"]) != change["count"]:
                raise ValueError("The complete inverse source replacement is ambiguous")
            inverse = inverse.replace(change["new"], change["old"])
        if inverse.encode("utf-8") != original:
            raise ValueError("The original entire source was not recovered")
        tree = ast.parse(value, filename=specification["name"])
        compile(tree, specification["name"], "exec")
        reject_duplicate_literal_keys(tree)
        if any(line.rstrip() != line for line in value.splitlines()):
            raise ValueError("Unexpected source trailing whitespace")
        staged[specification["name"]] = body
        result.append(dict(name=specification["name"], bytes=len(body),
            sha256=digest(body), parent_name=specification["parent_name"],
            parent_sha256=digest(original), complete_replacement_count=len(specification["complete_edits"]),
            whole_forward_source_replay=True, whole_inverse_parent_recovery=True,
            full_AST_and_compile_without_import=True))
    outdir.mkdir(parents=True)
    for name, body in staged.items():
        (outdir / name).write_bytes(body)
    report = dict(schema="complete-run10-public-input-source-replay-v1",
        source_sha256=digest(Path(__file__).read_bytes()), complete_sources=result,
        source_count=len(result), complete_source_identity_passed=True,
        complete_AST_and_compile_without_import=True,
        scientific_import_or_evaluation=False,
        actual_public_input_files_or_arrays_read=False,
        scientific_field_or_root_calls=0)
    target = outdir / "report.json"
    target.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print(json.dumps(dict(report=str(target), source_count=len(result),
        source_only=True, scientific_execution=False), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
