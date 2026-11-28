"""PWA96 reuses the unchanged complete-small-scalar publication engine.

Only task names and the complete seven-target validator/report change.
No native restoration, arithmetic retry, capacity relaxation or skipped pull
is introduced. Every actual failed prefix remains a public whole object.
"""
from __future__ import annotations
import argparse, ast, hashlib
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT=TOPIC+"/scripts/fourfold_codazzi_physical_chain_public_worker.py"
PARENT_SHA="2b8cb4bedce8ce40d0d184ac03abf3aabd2d223aa7520c1984c046c977222cf0"
REPLACEMENTS={
    "actual-physical-stage.json":"actual-pwa-height-phase.json",
    "actual_positive_physical_scalar_stage_execution_v1":"R149_complete_PWA_height_phase_saved_execution_v1",
    "actual-positive-physical-stage-":"actual-pwa-height-phase-",
    "consumed_actual_positive_physical_scalar_stage_v1":"consumed_R149_complete_PWA_height_phase_saved_v1",
    "whole_actual_predecessors_reserved_for_one_new_scalar_stage":"whole_H96_P96_APHI_reserved_for_one_PWA_scalar_combination",
    "visible-exact: reserve actual positive physical ":"visible-exact: reserve complete PWA height phase ",
    "visible-exact: preserve actual positive physical ":"visible-exact: preserve complete PWA height phase "}
VALIDATOR='''
def validate_output(raw):
    import importlib.util
    definition=importlib.util.spec_from_file_location("_PWA96_complete_output_metadata",snapshots["science"])
    owner=importlib.util.module_from_spec(definition);definition.loader.exec_module(owner)
    return owner.validate_output(raw,manifest,args.manifest_sha,by_role["science"]["sha256"],run,attempt)
'''
REPORT='''
def final_files():
    body=encode(state)
    require(len(body)<=op["maximum_execution_bytes"],"complete PWA96 execution budget")
    report=("# Actual PWA height and common-ratio phase rows\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "Only the complete actual H96/P96/APHI small publications are consumed. "
        "The unchanged canonical height row and complete G/H vectors give the PWA cap-height row; "
        "the same unnormalized strict particular supplies one common phase/height ratio. "
        "All96 exact dyadic centres, both joint row radii, and complete original negative/world "
        "receivers are retained. No old carrier, height/phase integral or scientific target runs. "
        "True PDE correction, cap input admissibility, independent world/mean/raw phase ports "
        "and the remaining full Schur problem remain separate.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw=(Path(root)/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PARENT_SHA,"whole original small-scalar public engine")
    tree=ast.parse(raw.decode(),filename=PARENT)
    strings=dict.fromkeys(REPLACEMENTS,0)
    functions={"validate_output":VALIDATOR,"final_files":REPORT};counts=dict.fromkeys(functions,0)
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value]+=1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            if node.name in functions:
                counts[node.name]+=1
                return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
    tree=Adapter().visit(tree)
    require(all(x==1 for group in (strings,counts) for x in group.values()),
            "only declared exact task names, complete validator and report change")
    tree.body[0].value=ast.Constant(__doc__);ast.fix_missing_locations(tree)
    return tree


def main():
    parser=argparse.ArgumentParser(add_help=False);parser.add_argument("--repo",required=True)
    args,_=parser.parse_known_args()
    namespace={"__name__":"_PWA96_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()),"<PWA96 complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__=="__main__":
    main()
