"""WRC public worker: four first targets on the unchanged WMR engine.

No prior WMR execution exists.  The fourth signed target is the complete
fixed-reference physical height, sharing the first three targets' inputs.
Whole genuine failure prefixes, README pulls and publication are inherited.
"""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT=TOPIC+"/scripts/fourfold_codazzi_world_mean_height_public_worker.py"
PARENT_SHA="b7f4349942ee383077c6e4bdac82d90607fd6ac7d0d017584583738bdc5da26b"
NAMES={
 "R147_complete_physical_mean_height_nu_kernel_inputs_v1":"R147_complete_reference_world_mean_height_nu_inputs_v1",
 "complete_physical_mean_height_nu_kernel":"complete_reference_world_mean_height_nu",
 "actual-world-mean-height.json":"actual-complete-reference-world-height.json",
 "actual-world-mean-height-":"actual-complete-reference-world-height-",
 "R147_complete_physical_mean_height_nu_kernel_execution_v1":"R147_complete_reference_world_mean_height_nu_execution_v1",
 "consumed_R147_complete_physical_mean_height_nu_kernel_v1":"consumed_R147_complete_reference_world_mean_height_nu_v1",
 "one complete physical mean-height kernel manifest":"one complete reference-world mean-height manifest",
 "visible-exact: reserve complete physical mean height ":"visible-exact: reserve full reference mean height ",
 "visible-exact: preserve complete physical mean height ":"visible-exact: preserve full reference mean height ",
}
EXTRA_VALIDATION='''
    if details is not None:
        full=details["complete_reference_world_height"]
        require(full["maximum_contraction_degree"]==2080
            and full["complete_exact_quadrature_grid"]==8192
            and isinstance(full["whole_raw_position_mean_ball"],str)
            and isinstance(full["new_complete_weighted_position_L2_upper"],str)
            and set(full["complete_error_terms"])=={"EW","UW","ET","Gstar","full_reference_radius"}
            and all(isinstance(value,str) for value in full["complete_error_terms"].values())
            and full["reference_covector_error"]=="108627/1000000000"
            and full["reference_waist_vertical_position_upper"]=="232743/1000000000"
            and full["full_physical_coordinate_term"]=="Pi[dotJ*f0_reference]"
            and full["coordinate_term_bounded_without_being_deleted"] is True
            and isinstance(full["actual_anchor_frame_error_coefficient"],str)
            and isinstance(full["actual_anchor_position_error_coefficient"],str)
            and full["actual_anchor_changes_and_variation_ports_independent"] is True,
            "whole new reference-height contraction, errors and actual independent ports")
    if doc["complete"]:
        require(result["complete_reference_world_height_computed"] is True
            and result["complete_reference_height_coordinate_term_paid"] is True
            and type(result["actual_reference_full_height_excludes_zero"]) is bool
            and result["reference_waist_vertical_position_upper"]=="232743/1000000000",
            "four genuinely complete new targets, including the full reference coordinate term")
'''
REPORT='''
def final_files():
    body=encode(state)
    require(len(body)<=op["maximum_execution_bytes"],"whole reference-height execution")
    report=("# Actual complete reference-world mean-height parameter column\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "One necessary complete NP/RHI carrier restoration feeds the8192-point grid. "
        "The first three WMR targets and the new fourth complete reference-height target "
        "are evaluated once. Both means, the full physical-coordinate term dotJ*f0, "
        "all angular products and original determinant-1 world orientation are retained. "
        "The specified raw b-anchor reference is kept distinct from actual frame/position "
        "anchor differences and independent varying rigid ports. No old geometry, RHI, "
        "NP or phase target is repeated. Every genuine failure and its entire accepted "
        "target prefix is preserved; no actual full world-height Schur is asserted.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def _replace_expressions(tree,replacements):
    parsed={ast.dump(ast.parse(old,mode="eval").body):(old,new) for old,new in replacements.items()}
    counts={old:0 for old in replacements}
    class Exact(ast.NodeTransformer):
        def generic_visit(self,node):
            key=ast.dump(node)
            if key in parsed:
                old,new=parsed[key];counts[old]+=1
                return ast.copy_location(ast.parse(new,mode="eval").body,node)
            return super().generic_visit(node)
    tree=Exact().visit(tree)
    require(all(value==1 for value in counts.values()),"each exact WMR schema expression changes once")
    ast.fix_missing_locations(tree)
    return tree


def build_adapter(root):
    raw=(root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PARENT_SHA,"whole frozen WMR public worker")
    spec=importlib.util.spec_from_file_location("_WRC_frozen_public_engine",root/PARENT)
    parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    require(set(parent.REPLACEMENTS.values())==set(NAMES),"all nine exact WMR entry names")
    parent.REPLACEMENTS={key:NAMES[value] for key,value in parent.REPLACEMENTS.items()}
    validator=_replace_expressions(ast.parse(parent.VALIDATOR),{
        "0<=count<=3":"0<=count<=4",
        "index in (0,2)":"index in (0,2,3)",
        "[3,1,1][index]":"[3,1,1,1][index]",
        "count==3":"count==4",
        'result["complete_new_record_count"]==3':'result["complete_new_record_count"]==4',
    })
    function=validator.body[0]
    require(isinstance(function,ast.FunctionDef) and function.name=="validate_output"
        and isinstance(function.body[-1],ast.Return),"whole original WMR validator")
    extra=ast.parse("def extension():\n"+EXTRA_VALIDATION).body[0].body
    function.body[-1:-1]=extra
    ast.fix_missing_locations(validator)
    parent.VALIDATOR=ast.unparse(validator)
    parent.REPORT=REPORT
    tree=parent.build_adapter(root)
    tree=_replace_expressions(tree,{
        'manifest["complete_record_counts"] == [3]':'manifest["complete_record_counts"] == [4]'})
    tree.body[0].value=ast.Constant(__doc__);ast.fix_missing_locations(tree)
    return tree


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",required=True)
    args,unused=parser.parse_known_args()
    namespace={"__name__":"_WRC_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()),"<WRC complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__=="__main__":
    main()
