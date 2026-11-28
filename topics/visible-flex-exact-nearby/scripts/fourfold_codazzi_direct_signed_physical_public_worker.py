"""First signed physical reception using the complete WSS execution transport and original DCP inputs."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

TOPIC="topics/visible-flex-exact-nearby"
SOURCE=TOPIC+"/scripts/fourfold_codazzi_direct_signed_physical_public_worker.py"
OLD=TOPIC+"/scripts/fourfold_codazzi_whole_selected_signed_source_public_worker.py"
OLD_SHA="a7cefd09f678228db19141f111a0277484323677f27fd64f09e8a7e146caa767"
DCP_MANIFEST="d85c0d55f82e50d9f061756a4d132db6780992654f3c01fbf5ae9a03657c44df"


def stage_dcp(shared,inputs,files,head,state):
    """Stage the unchanged current 269 and the historical 53 at their genuine source revisions."""
    spec=files["DCP_manifest"]
    raw=(inputs/spec["path"]).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=DCP_MANIFEST or spec["sha256"]!=DCP_MANIFEST:
        raise ValueError("whole original DCP manifest")
    m=json.loads(raw)
    if len(m["files"])!=269 or len(m["historical_inputs"])!=53:
        raise ValueError("complete 322 original inputs")
    def put(s,revision,small):
        payload,unused=shared["checked_bytes"](s,revision,small)
        path=inputs/s["path"]
        if path.exists():
            if path.read_bytes()!=payload:
                raise ValueError("entire shared scientific input conflict: "+s["path"])
        else:
            shared["atomic"](path,payload)
    for s in m["files"]:
        put(s,head,True)
    for s in m["historical_inputs"]:
        if not s["restore_only"] or s["encoding"]!="gzip-json":
            raise ValueError("genuine original historical carrier only")
        shared["fetch_commit"](s["commit"])
        put(s,s["commit"],False)
    state["whole_DCP_original_closure"]={"manifest":DCP_MANIFEST,"current":269,"historical":53,
        "complete_ordered_descriptors_sha256":hashlib.sha256(shared["encode"](m["files"]+m["historical_inputs"])).hexdigest()}


def adapter(raw):
    if hashlib.sha256(raw).hexdigest()!=OLD_SHA:
        raise ValueError("the entire already audited unchanged original public transport")
    start=ast.parse(raw)
    functions=[n for n in start.body if isinstance(n,ast.FunctionDef) and n.name=="main"]
    if len(functions)!=1:
        raise ValueError("one original operational main")
    main=functions[0]
    renames={
       "R149_whole_selected_body_signed_source_inputs_v1":"R149_three_direct_signed_physical_Theta_and_recovered_columns_inputs_v1",
       "R149_whole_selected_body_signed_source_execution_v1":"R149_three_direct_signed_physical_Theta_and_recovered_columns_execution_v1",
       "consumed_whole_selected_signed_body_source_v1":"consumed_three_direct_signed_physical_Theta_v1",
       "new_complete_signed_cells":"saved_record_count",
       "whole-selected-signed-source.json":"direct-signed-physical-columns.json",
       "/whole-selected-signed-source.json":"/direct-signed-physical-columns.json",
       "# Actual whole selected signed source carrier\n\n":"# Actual three signed physical columns and recovered coordinates\n\n",
       "Every original scalar/cubic seam, the repaired base, full direction, both signed forcing columns, the same selected intrinsic perturbation, and the original physical mean remain. The signed source polarization uses all 577 physical rows with ordinary radial measure. The full boundary-value solution requires its independent root, physical outer and height data.\n":
         "The whole signed Newton and parameter waists and the independent strict parameter column retain their true source and target phases, original means, and joint infinite-target errors. The finite-coordinate residual uses the same signed full density inverse.\n",
       "RECOVERABLE WHOLE WSS OUTCOME BEFORE GIT ":"RECOVERABLE WHOLE ASQ25 PHYSICAL COLUMN OUTCOME BEFORE GIT ",
       "visible-exact: reserve whole selected signed source carrier":"visible-exact: reserve three signed physical coordinate receptions",
       "visible-exact: preserve complete selected signed source prefix":"visible-exact: preserve signed physical coordinate prefix",
       "visible-exact: preserve complete selected signed forcing results":"visible-exact: preserve three signed physical coordinate receptions",
       "the new whole source carrier or polarization did not finish; its whole prefix is retained":
          "the three signed physical columns retain their completed target prefix"}
    seen=dict.fromkeys(renames,0)
    for node in ast.walk(main):
        if isinstance(node,ast.Constant) and isinstance(node.value,str) and node.value in renames:
            seen[node.value]+=1
            node.value=renames[node.value]
    if not all(seen.values()):
        raise ValueError("every original scoped identity must match")
    currents=[n for n in main.body if isinstance(n,ast.FunctionDef) and n.name=="current"]
    if len(currents)!=1 or not isinstance(currents[0].body[-1],ast.Assign):
        raise ValueError("one unchanged complete input current after each pull")
    currents[0].body.extend(ast.parse("stage_dcp(shared,inputs,files,head,state)").body)
    tree=ast.Module(body=[main],type_ignores=[])
    return ast.fix_missing_locations(tree)


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",type=Path,required=True)
    args,unused=parser.parse_known_args()
    path=args.repo/OLD
    tree=adapter(path.read_bytes())
    spec=importlib.util.spec_from_file_location("_ASQ25_whole_unmodified_WSS_publication",path)
    old=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=old
    spec.loader.exec_module(old)
    scope=dict(old.__dict__,__file__=__file__,SOURCE=SOURCE,stage_dcp=stage_dcp)
    exec(compile(tree,str(path)+"#ASQ25", "exec"),scope)
    return scope["main"]()


if __name__=="__main__":
    main()
