"""Metadata-only explicit SL continuation after run45887481333 saved zero targets."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
WORKER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_resume_worker.py"
GENERATOR = TOPIC+"/scripts/make_support_localized_nu_resume_manifest.py"
ORIGINAL_GENERATOR = TOPIC+"/scripts/make_support_localized_nu_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-support-localized-nu-after-45887481333-inputs.json"
WORKFLOW = ".github/workflows/visible-exact-support-localized-nu-after-45887481333.yml"


def load(root, path, name):
    spec = importlib.util.spec_from_file_location(name, root/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    sys.dont_write_bytecode = True
    worker = load(root, WORKER, "_SL_resume_metadata")
    _, old = worker.admitted_failure(root)
    owner = load(root, TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_owner.py", "_SL_original_owner")
    original_generator = load(root, ORIGINAL_GENERATOR, "_SL_original_generator")
    contents, specs = owner.gather(root)
    owner.admit(contents, specs)
    owner.require(old["files"] == [specs[k] for k in sorted(specs)],
                  "all original mathematical inputs and source bytes remain unchanged")
    compile(worker.build_adapter(root), WORKER, "exec")
    for role, old_role in (("failed_worker", "worker"), ("failed_generator", "generator")):
        specs[role] = dict(specs[old_role], role=role)
    for role, path in (("worker", WORKER), ("generator", GENERATOR),
                       ("failed_execution", worker.FAILED), ("failed_manifest", worker.OLD_MANIFEST)):
        raw = (root/path).read_bytes()
        owner.require(0 < len(raw) < 100000, "complete small continuation input")
        raw.decode()
        specs[role] = owner.descriptor(role, path, raw)
    review = owner.parse(contents["reviewed_rules"])
    for path, digest in review["readme_sha256"].items():
        owner.require(owner.sha((root/path).read_bytes()) == digest, "same already read current README")
    owner.require(len(specs) == 23 and len({x["path"] for x in specs.values()}) == 23
                  and not any(x in sys.modules for x in ("flint", "numpy", "scipy")),
                  "23 complete inputs; no local scientific evaluation")
    manifest = dict(old)
    manifest.update(problem_id="R147_support_localized_negative_nu_after_45887481333",
                    files=[specs[k] for k in sorted(specs)], expected_current_input_count=23,
                    continuation={"run": "45887481333/1", "complete_old_scientific_targets": [],
                                  "missing_targets": list(owner.TARGETS), "failed_execution_sha256": worker.FAILED_SHA,
                                  "scientific_owner_and_math_unchanged": True,
                                  "only_private_snapshot_names_changed": True})
    manifest["operation"] = dict(old["operation"], consumed_marker=
        TOPIC+"/notes/support_localized_nu_ci/consumed-after-45887481333.json")
    raw = owner.canonical(manifest)
    workflow = original_generator.WORKFLOW_TEMPLATE
    for before, after in ((original_generator.WORKFLOW, WORKFLOW),
                          (original_generator.MANIFEST, MANIFEST),
                          (original_generator.WORKER, WORKER),
                          ("visible-flex-exact-support-localized-nu-20261127",
                           "visible-flex-exact-support-localized-nu-after-45887481333")):
        workflow = workflow.replace(before, after)
    insertion = ("            /"+worker.ADAPTER+"\n"
                 "            /"+worker.FAILED+"\n"
                 "            /"+worker.OLD_MANIFEST+"\n")
    workflow = workflow.replace("            /"+WORKER+"\n", "            /"+WORKER+"\n"+insertion)
    workflow = workflow.replace("@MANIFEST_SHA@", owner.sha(raw))
    for path, payload in ((MANIFEST, raw), (WORKFLOW, workflow.encode())):
        destination = root/path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(payload)
    print(json.dumps({"manifest": MANIFEST, "manifest_sha256": owner.sha(raw),
                      "workflow": WORKFLOW, "scientific_targets_evaluated_locally": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
