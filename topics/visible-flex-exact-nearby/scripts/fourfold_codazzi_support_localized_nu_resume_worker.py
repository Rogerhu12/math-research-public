"""Continue the four SL targets after the observed zero-target stdlib collision.

The scientific owner and all four formulas are unchanged.  The original
small-worker adapter is reused; only private snapshot basenames acquire
an input_ prefix so that the role math cannot shadow Python's math module.
The old failed execution and consumed marker remain permanent records.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
ADAPTER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py"
ADAPTER_SHA = "65daf6f2fa7a5e3a09bb331e0087d4ffe563e5740fb972e46e61fb7d14187fa0"
FAILED = TOPIC+"/notes/support_localized_nu_ci/run-45887481333-1/execution.json"
FAILED_SHA = "01563ee206b7da9b04a4073865f68fa461deacc774a9c0d3f03f4459898a2113"
OLD_MANIFEST = TOPIC+"/notes/2026-11-27-support-localized-nu-inputs.json"
OLD_MANIFEST_SHA = "34d7e0a3458bac8ddde6e7dde2721b054e9ebd0dc8b9e5953d07f4a63628e7a1"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def admitted_failure(root):
    raw = (root/FAILED).read_bytes()
    original = (root/OLD_MANIFEST).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == FAILED_SHA
            and hashlib.sha256(original).hexdigest() == OLD_MANIFEST_SHA,
            "whole original zero-target failure and original mathematical manifest")
    old, manifest = json.loads(raw), json.loads(original)
    require(old["run_id"] == "45887481333" and old["run_attempt"] == "1"
            and old["manifest_sha256"] == OLD_MANIFEST_SHA
            and old["kind"] == "R147_support_localized_selected_negative_nu_execution_v1"
            and old["complete"] is False and old["actual_child_returncode"] == 1
            and old["child_timeout"] is False and old["scientific_children"] == 1
            and old["completed_new_scalar_targets"] == 0 and old["scientific_files"] == []
            and old["original_scientific_complete"] is old["original_scientific_failure"] is None
            and old["old_completed_targets_recomputed"] == old["old_numerical_producers_called"] == 0
            and old["current_input_receipts"] == manifest["files"]
            and old["complete_child_stdout"]["bytes"] == 844
            and old["complete_child_stdout"]["sha256"]
                == "acc0a26ac552337ded574444afc77d73a4994cc7fcf7aeb36e66f459a0543f78",
            "the observed import/admission failure completed none of the four mathematical targets")
    return old, manifest


def build_adapter(root):
    raw = (root/ADAPTER).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == ADAPTER_SHA,
            "the unchanged complete first public adapter")
    spec = importlib.util.spec_from_file_location("_SL_original_adapter", root/ADAPTER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tree = module.build_adapter(root)
    replacements = 0

    class PrivateNames(ast.NodeTransformer):
        def visit_Assign(self, node):
            nonlocal replacements
            if (len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
                    and node.targets[0].id == "destination"
                    and isinstance(node.value, ast.BinOp)
                    and isinstance(node.value.op, ast.Div)
                    and isinstance(node.value.left, ast.Name)
                    and node.value.left.id == "source_dir"):
                expected = ast.parse('source_dir / (spec["role"] + Path(spec["path"]).suffix)', mode="eval").body
                require(ast.dump(node.value) == ast.dump(expected), "the exact original snapshot naming expression")
                node.value = ast.parse('source_dir / ("input_" + spec["role"] + Path(spec["path"]).suffix)', mode="eval").body
                replacements += 1
            return self.generic_visit(node)

    tree = PrivateNames().visit(tree)
    require(replacements == 1, "only the one private basename expression changes")
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo", required=True)
    args, _ = parser.parse_known_args()
    root = Path(args.repo).resolve()
    admitted_failure(root)
    namespace = {"__name__": "_SL_resume_public_worker", "__file__": __file__}
    exec(compile(build_adapter(root), str(Path(__file__).resolve()), "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
