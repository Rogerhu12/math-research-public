"""H96 successor. Admit the exact failed parent and continue its joint height integral."""
import argparse
import ast
import hashlib
import json
import os
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
SCRIPTS = TOPIC+"/scripts/"
NOTES = TOPIC+"/notes/"
PARENT_RUN = "46123190757"
PARENT_EVENT = "0ed00cf191cf6ce8366db09769f6ad377ab66257"
PARENT_CHECKOUT = "e4509035f86170656711b06fa126c7dd0715b67a"
ORIGINAL_MANIFEST = NOTES+"2026-11-28-finite-trial-height-complete-inputs.json"
ORIGINAL_BASE = NOTES+"finite_trial_height_ci"
ORIGINAL_RUN = ORIGINAL_BASE+"/run-"+PARENT_RUN+"-1"
ORIGINAL_SOURCE_SHA = "91b7929a910e04f8eb1f20bc581c694325b242aab0a4c1791afbf05ec1dae34b"
ORIGINAL_WORKER_SHA = "1f98010b06299e843bea939f4a14974aec50b0e0db970edae5b6b836a8e1e8fd"
MATH_SHA = "c45a551210cf2ba4c49047b1a063f1f8fb1d30531168add2a47001f044d1f5f7"
PREFIX_SHA = "d9598396f28c8c00e54a2abe1ee37e1a038bacb17e1e54c062be1369c83b3e66"
PARENT_FILES = {
    "H96_original_manifest":(ORIGINAL_MANIFEST,"60f1e7ca8d83f986d7020e786a0f1ed7dd1958634039c5bdb7c5952a28ea1483"),
    "H96_parent_actual":(ORIGINAL_RUN+"/actual-finite-trial-height.json","0f4b60c25adfaa626aa4569c5a5b8db5cc6a6cbb93ffc871e0264255f874b08c"),
    "H96_parent_execution":(ORIGINAL_RUN+"/execution.json","c079f8091a3811d42a5be7971c0390390ed0af57b3afc3767e9b009d7fabcac3"),
    "H96_parent_consumed":(ORIGINAL_BASE+"/consumed-target.json","15fbc017b39743c559aa9586605cbffea1e6b5bcd894fb491fb574613dfd16ae")}
REVIEW = (NOTES+"2026-11-28-read-public-model-ultra-rules.json","32fa03fbdb357d7d5a98b7115a24acc10f218705a1ecdef2e756ff73284098ce")
MANIFEST = NOTES+"2026-11-28-finite-trial-height-after-728-inputs.json"
STAGE = "complete_original_finite_trial_height_rows_after_paid728"
PREFIX_KIND = "R149_H96_whole_signed96_continuation_after_46123190757_v1"
KIND, MANIFEST_KIND, EXECUTION_KIND = ("R149_"+STAGE+s for s in ("_v1","_inputs_v1","_execution_v1"))
PROBLEM = "R149_H96_after_46123190757_1_all96_728_to_2847"
CARRIERS = ("necessary_original_trial_receipts","necessary_original_NP_receipts","necessary_relative_carrier_receipt")
RECEIPT = {"kind":PREFIX_KIND, "parent_run_id":PARENT_RUN,"parent_run_attempt":"1",
           "parent_actual_sha256":PARENT_FILES["H96_parent_actual"][1],
           "parent_execution_sha256":PARENT_FILES["H96_parent_execution"][1],
           "parent_consumed_sha256":PARENT_FILES["H96_parent_consumed"][1],
           "parent_signed_prefix_sha256":PREFIX_SHA,"already_paid_relative_cells":728,
           "assigned_relative_cells":[728,2847],"complete_joint_trial_columns":96,
           "old_signed_integrals_and_adjoint_error_carried":True}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False, allow_nan=False)+"\n").encode()


def check_parent(raws):
    records = {}
    for role,(path,digest) in PARENT_FILES.items():
        raw = raws[path]
        require(sha(raw) == digest, "complete immutable H96 parent input: "+role)
        records[role] = json.loads(raw)
    old, parent, execution, marker = [records[role] for role in PARENT_FILES]
    ident = parent["identity"]
    require(ident["source_sha256"] == ORIGINAL_SOURCE_SHA and
            ident["manifest_sha256"] == execution["manifest_sha256"] == marker["manifest_sha256"] == PARENT_FILES["H96_original_manifest"][1]
            and ident["run_id"] == execution["run_id"] == marker["run_id"] == PARENT_RUN
            and ident["run_attempt"] == execution["run_attempt"] == marker["run_attempt"] == "1"
            and ident["event_commit"] == execution["event_commit"] == PARENT_EVENT
            and ident["actual_checkout_commit"] == execution["actual_scientific_checkout"] == PARENT_CHECKOUT
            and marker["output_directory"] == ORIGINAL_RUN and execution["problem_id"] == marker["problem_id"] == old["problem_id"]
            and execution["current_input_receipts"] == old["files"] and
            execution["scientific_files"] == [{"path":PARENT_FILES["H96_parent_actual"][0],"bytes":13221,
                                                "sha256":PARENT_FILES["H96_parent_actual"][1]}],
            "real original manifest, entire scientific inventory, exclusive marker and failed execution")
    require(parent["complete"] is parent["proved"] is execution["complete"] is False
            and parent["actual_returncode"] is parent["current_target"] is parent["candidate_record"] is parent["result"] is None
            and parent["completed_targets"] == [] and parent["new_records"] == {} and parent["saved_record_count"] == 0
            and execution["actual_child_returncode"] == -9 and execution["child_timeout"] is False
            and execution["scientific_children"] == 1 and execution["completed_new_scalar_targets"] == 0
            and execution["failure"]["message"] == "README changed: preserve prefix and apply the printed change before further science",
            "the original child was actually interrupted on the rule change before any final target")
    prefix = parent["height_integral_prefix"]
    require(sha(canonical(prefix)) == PREFIX_SHA and prefix["complete_relative_cells"] == prefix["complete_intersections"] == 728
            and len(prefix["all96_signed_polynomial_integrals"]) == 96 and all(parent[k] is not None for k in CARRIERS),
            "one whole signed paid 96-column prefix and all original carrier identities")
    old_rules = json.loads(raws[old["roles"]["reviewed_rules"]])
    require(sha(raws[REVIEW[0]]) == REVIEW[1], "whole actually reviewed rule16 contract")
    latest = json.loads(raws[REVIEW[0]])
    require(latest["supersedes_review"]["sha256"] == sha(raws[old["roles"]["reviewed_rules"]])
            and latest["large_data_policy"] == old_rules["large_data_policy"]
            and latest["previously_read_readme_sha256"] == old_rules["readme_sha256"]
            and latest["readme_sha256"] == execution["readme_checks"][-1]["readme_sha256"]
            and latest["new_unread_rules_must_still_be_reported_and_applied"] is True
            and (latest["model"], latest["reasoning_effort"]) == ("gpt-6.2-astra","ultra"),
            "both whole old and newly applied README reviews and all preserved policy terms")
    return old, parent


def read_source(path, expected, name):
    raw = Path(path).read_bytes()
    require(sha(raw) == expected, "whole immutable executable: "+name)
    env = {"__name__":name, "__file__":str(path)}
    from types import ModuleType
    module = ModuleType(name)
    module.__dict__.update(env)
    exec(compile(raw, str(path), "exec"), module.__dict__)
    return module


def build_main(raw):
    require(sha(raw) == ORIGINAL_SOURCE_SHA, "entire original scientific owner")
    old = ast.parse(raw)
    fn, = [node for node in old.body if isinstance(node,ast.FunctionDef) and node.name=="main"]
    # Each replacement has exactly one structural owner and changes exactly the scoped statement.
    mappings = [
        ('admitted = admit(manifest, raws, paths)', 'admitted, parent = admit_resume(manifest, raws, paths)'),
        ('require(sorted(state) == SCI_FIELDS, "whole H96 result envelope")',
         'state["resume"] = RECEIPT.copy()\nstate["height_integral_prefix"] = parent["height_integral_prefix"]\nrequire(sorted(state) == SCI_FIELDS, "whole H96 resume result envelope")'),
        ('result = math.compute(bundle, publish, save_prefix, progress)',
         'require(all(state[key] == parent[key] for key in CARRIERS), "all four whole TC, four whole NP, and complete RHI endpoint, chain and polynomial-cache receipts equal the parent")\nbundle["original_prefix"] = parent["height_integral_prefix"]\nresult = resume_math.compute(math, bundle, publish, save_prefix, progress)')]
    targets = {ast.dump(ast.parse(before).body[0]): (i,ast.parse(after).body) for i,(before,after) in enumerate(mappings)}
    counts = [0]*len(mappings)
    class Adapter(ast.NodeTransformer):
        def generic_visit(self,node):
            if isinstance(node,ast.stmt):
                match = targets.get(ast.dump(node))
                if match is not None:
                    i,replacement = match
                    counts[i] += 1
                    return replacement
            return super().generic_visit(node)
    fn = Adapter().visit(fn)
    require(counts == [1]*len(mappings), "exact scientific owner AST adaptation counts")
    return ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[]))


def main():
    sys.dont_write_bytecode = True
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--input-map",type=Path,required=True)
    args,_ = parser.parse_known_args()
    mapping = json.loads(args.input_map.read_bytes())
    original = read_source(mapping["H96_original_science"], ORIGINAL_SOURCE_SHA, "_old_H96_owner")
    math = read_source(mapping["resume_math"], MATH_SHA, "_resume_H96_math")
    def admit_resume(manifest, raws, paths):
        old,parent = check_parent(raws)
        require(manifest["resume"] == RECEIPT and manifest["problem_id"] == PROBLEM
                and manifest["historical_inputs"] == old["historical_inputs"]
                and all(any(new["path"] == item["path"] and new["sha256"] == item["sha256"] and new["bytes"] == item["bytes"]
                            and new["git_blob_sha"] == item["git_blob_sha"] for new in manifest["files"]) for item in old["files"])
                and os.environ["GITHUB_RUN_ID"] != PARENT_RUN, "new successor identity; entire old closure retained")
        return original.admit(old, raws, paths), parent
    namespace = {**vars(original),"__file__":__file__,"MANIFEST_KIND":MANIFEST_KIND,"KIND":KIND,
                 "STAGE":STAGE,"SCI_FIELDS":sorted(original.SCI_FIELDS+["resume"]),"RECEIPT":RECEIPT,
                 "CARRIERS":CARRIERS,"resume_math":math,"admit_resume":admit_resume}
    exec(compile(build_main(Path(original.__file__).read_bytes()), "<H96 continuation owner>", "exec"), namespace)
    return namespace["main"]()


if __name__ == "__main__":
    raise SystemExit(main())
