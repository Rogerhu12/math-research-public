"""First new signed negative-waist job using the whole already verified WSS public input transport."""
import argparse
import ast
import hashlib
import importlib.util
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_negative_defect_signed_waist_public_worker.py"
ORIGINAL=TOPIC+"/scripts/fourfold_codazzi_whole_selected_signed_source_public_worker.py"
ORIGINAL_SHA="a7cefd09f678228db19141f111a0277484323677f27fd64f09e8a7e146caa767"

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",type=Path,required=True)
    args,unused=parser.parse_known_args()
    p=args.repo/ORIGINAL
    raw=p.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=ORIGINAL_SHA:
        raise ValueError("entire original operational worker")
    spec=importlib.util.spec_from_file_location("_ASQ23_original_WSS_transport",p)
    old=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=old
    spec.loader.exec_module(old)
    tree=ast.parse(raw)
    functions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=="main"]
    old.require(len(functions)==1,"one immutable original public main")
    node=functions[0]
    # Preserve all executable decisions including reservation, Github identity,
    # CPU/restoration, re-pulls and capacity. Change only new target identities
    # in string constants and its human-readable report.
    renames={
        "R149_whole_selected_body_signed_source_inputs_v1":"R149_negative_solutions_signed_joint_waists_inputs_v1",
        "R149_whole_selected_body_signed_source_execution_v1":"R149_negative_solutions_signed_joint_waists_execution_v1",
        "consumed_whole_selected_signed_body_source_v1":"consumed_two_negative_signed_waists_v1",
        "new_complete_signed_cells":"new_complete_negative_trial_cells",
        "whole-selected-signed-source.json":"negative-signed-waists.json",
        "/whole-selected-signed-source.json":"/negative-signed-waists.json",
        "# Actual whole selected signed source carrier\n\n":"# Actual signed negative Newton and parameter waist responses\n\n",
        "Every original scalar/cubic seam, the repaired base, full direction, both signed forcing columns, the same selected intrinsic perturbation, and the original physical mean remain. The signed source polarization uses all 577 physical rows with ordinary radial measure. The full boundary-value solution requires its independent root, physical outer and height data.\n":
            "Both forced negative solutions use the full selected field, zero root data, every signed cubic interface, and the separate physical mean. The strict and root-window residuals each retain their full two-column Gram.\n",
        "RECOVERABLE WHOLE WSS OUTCOME BEFORE GIT ":"RECOVERABLE WHOLE ASQ23 SIGNED NEGATIVE WAISTS BEFORE GIT ",
        "visible-exact: reserve whole selected signed source carrier":"visible-exact: reserve both signed negative waist responses",
        "visible-exact: preserve complete selected signed source prefix":"visible-exact: preserve complete signed backward waist suffix",
        "visible-exact: preserve complete selected signed forcing results":"visible-exact: preserve both signed negative waist responses",
        "the new whole source carrier or polarization did not finish; its whole prefix is retained":"the two signed negative waist targets retain their latest complete backward suffix"}
    seen={k:0 for k in renames}
    for n in ast.walk(node):
        if isinstance(n,ast.Constant) and isinstance(n.value,str) and n.value in renames:
            seen[n.value]+=1
            n.value=renames[n.value]
    old.require(all(v>0 for v in seen.values()),"every scoped target-string replacement present in verified original AST")
    scope=dict(old.__dict__,SOURCE=SOURCE,__file__=__file__)
    exec(compile(ast.Module(body=[node],type_ignores=[]),str(p)+"#ASQ23","exec"),scope)
    return scope["main"]()

if __name__=="__main__":
    main()
