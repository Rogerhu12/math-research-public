"""First fixed-affine base Newton trajectory, using the complete original WSS transport."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_fixed_negative_Newton_public_worker.py"
OLD=TOPIC+"/scripts/fourfold_codazzi_whole_selected_signed_source_public_worker.py"
OLD_SHA="a7cefd09f678228db19141f111a0277484323677f27fd64f09e8a7e146caa767"
FM="e99e081cd404c36e9f754c0839e9f8f7d95502fffa2db02bff093fe90a0599a8"
AFFINE={"original_affine_origin_inputs":"0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b",
        "original_affine_direction":"8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab"}


def stage_affine(shared,inputs,files,manifest,state):
    raw=(inputs/files["FM_manifest"]["path"]).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=FM:
        raise ValueError("entire original fixed-affine object definition")
    fixed=json.loads(raw)
    originals=[s for s in fixed["historical_inputs"] if s["role"] in AFFINE]
    if len(originals)!=2 or originals!=manifest["original_affine_historical_inputs"]:
        raise ValueError("both whole original native affine arrays")
    for s in originals:
        if s["sha256"]!=AFFINE[s["role"]] or s["commit"]!="3731c70d223185aaafa76815924609747d175cf9":
            raise ValueError("original whole historical scientific identity")
        shared["fetch_commit"](s["commit"])
        b,blob=shared["checked_bytes"](s,s["commit"],False)
        if blob!=s["git_blob_sha"]:
            raise ValueError("whole native original Git blob mismatch")
        path=inputs/s["path"]
        if path.exists():
            if path.read_bytes()!=b:
                raise ValueError("two original inputs conflict")
        else:
            shared["atomic"](path,b)
    state["whole_original_affine_geometry"]=originals


def adapter(raw):
    if hashlib.sha256(raw).hexdigest()!=OLD_SHA:
        raise ValueError("original WSS public first-entry transport")
    main,=[n for n in ast.parse(raw).body if isinstance(n,ast.FunctionDef) and n.name=="main"]
    names={
        "R149_whole_selected_body_signed_source_inputs_v1":"R149_fixed_affine_base_Newton_trajectory_inputs_v1",
        "R149_whole_selected_body_signed_source_execution_v1":"R149_fixed_affine_base_Newton_trajectory_execution_v1",
        "consumed_whole_selected_signed_body_source_v1":"consumed_fixed_affine_base_Newton_trajectory_v1",
        "new_complete_signed_cells":"complete_cells",
        "whole-selected-signed-source.json":"fixed-negative-Newton-trajectory.json",
        "/whole-selected-signed-source.json":"/fixed-negative-Newton-trajectory.json",
        "# Actual whole selected signed source carrier\n\n":"# Actual fixed-affine negative Newton trajectory\n\n",
        "Every original scalar/cubic seam, the repaired base, full direction, both signed forcing columns, the same selected intrinsic perturbation, and the original physical mean remain. The signed source polarization uses all 577 physical rows with ordinary radial measure. The full boundary-value solution requires its independent root, physical outer and height data.\n":
            "The complete original affine geometry, the physical base forcing, all original cubic joins and the uncertain root enter the flat residual integrals and the selected-operator transfer. The even mean remains an independent coordinate.\n",
        "RECOVERABLE WHOLE WSS OUTCOME BEFORE GIT ":"RECOVERABLE WHOLE ASQ27 FIXED NEGATIVE NEWTON BEFORE GIT ",
        "visible-exact: reserve whole selected signed source carrier":"visible-exact: reserve fixed affine negative Newton trajectory",
        "visible-exact: preserve complete selected signed source prefix":"visible-exact: preserve complete fixed affine Newton suffix",
        "visible-exact: preserve complete selected signed forcing results":"visible-exact: preserve fixed affine negative Newton trajectory",
        "the new whole source carrier or polarization did not finish; its whole prefix is retained":
            "the complete fixed affine base trajectory retains its actual accepted negative suffix"}
    seen=dict.fromkeys(names,0)
    for n in ast.walk(main):
        if isinstance(n,ast.Constant) and n.value in names:
            seen[n.value]+=1
            n.value=names[n.value]
    if not all(seen.values()):
        raise ValueError("whole original operational AST string contract")
    current,=[n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=="current"]
    if not isinstance(current.body[-1],ast.Assign):
        raise ValueError("complete original input ledger before affine restoration")
    current.body.extend(ast.parse("stage_affine(shared,inputs,files,manifest,state)").body)
    return ast.fix_missing_locations(ast.Module(body=[main],type_ignores=[]))


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",type=Path,required=True)
    args,unused=parser.parse_known_args()
    old_path=args.repo/OLD
    tree=adapter(old_path.read_bytes())
    s=importlib.util.spec_from_file_location("_ASQ27_whole_WSS_original_transport",old_path)
    old=importlib.util.module_from_spec(s)
    sys.modules[s.name]=old
    s.loader.exec_module(old)
    scope=dict(old.__dict__,__file__=__file__,SOURCE=SOURCE,stage_affine=stage_affine)
    exec(compile(tree,str(old_path)+"#ASQ27","exec"),scope)
    return scope["main"]()


if __name__=="__main__":
    main()
