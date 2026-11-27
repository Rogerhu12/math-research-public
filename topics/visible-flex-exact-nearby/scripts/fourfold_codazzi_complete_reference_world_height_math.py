"""WRC adds one complete reference-height target to the first WMR pass.

The original three targets have never run.  This adapter shares their
one necessary RHI restoration and8192-point directed grid, then appends
the genuinely new full reference-world mean-height contraction.
"""
from __future__ import annotations
import ast,hashlib
from pathlib import Path

PARENT_NAME="fourfold_codazzi_world_mean_height_math.py"
PARENT_ROLE="WMR_math"
PARENT_SHA="38e83cec3f0117664025c32ee67d41e161576dabb1514c37b78cde5fc2776f48"
NEW_TARGET="complete_original_reference_world_mean_height_nu_full"

ASSEMBLY='''
    weighted_position=J0*y
    C2=norm2_upper(c,weighted_position)
    raw_position=as_arb(c,mean(c,sum(
        (A[:,i,0]*weighted_position[:,i] for i in range(3)),c.Box(0.))))
    EW=(c.arb(27)/8*EY+EJ*Y2).upper()
    UW=(C2+EW).upper()
    ET=(EW+EA*C2).upper()
    Gstar=(G2+EG).upper()
    full_reference_radius=(ET+c.arb(108627)/1000000000*UW
        +c.arb(232743)/1000000000*Gstar).upper()
    full_reference=raw_position+c.arb(0,full_reference_radius)
    actual_frame_coefficient=(UW+c.arb(171)/250*Gstar).upper()
    require(all(value.is_finite() and value>=0 for value in
        (C2,EW,UW,ET,Gstar,full_reference_radius,actual_frame_coefficient)),
        "all complete new reference-height error terms")
    details["complete_reference_world_height"]={
        "maximum_contraction_degree":2080,"complete_exact_quadrature_grid":8192,
        "whole_raw_position_mean_ball":str(raw_position),
        "new_complete_weighted_position_L2_upper":str(C2),
        "complete_error_terms":{key:str(value) for key,value in
            zip(("EW","UW","ET","Gstar","full_reference_radius"),
                (EW,UW,ET,Gstar,full_reference_radius))},
        "reference_covector_error":"108627/1000000000",
        "reference_waist_vertical_position_upper":"232743/1000000000",
        "full_physical_coordinate_term":"Pi[dotJ*f0_reference]",
        "coordinate_term_bounded_without_being_deleted":True,
        "actual_anchor_frame_error_coefficient":str(actual_frame_coefficient),
        "actual_anchor_position_error_coefficient":str(Gstar),
        "actual_anchor_changes_and_variation_ports_independent":True}
'''
PUBLISH='''
    saved_full_reference=publish(TARGETS[3],[full_reference],"signed_enclosure")[0]
'''


def _parent_source():
    here=Path(__file__).resolve().parent
    candidates=(here/PARENT_NAME,here/("input_"+PARENT_ROLE+".py"))
    for path in candidates:
        if path.is_file():
            raw=path.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=PARENT_SHA:
                raise ValueError("whole frozen WMR math parent differs")
            return raw
    raise ValueError("complete declared WMR math parent is absent")


def _build():
    tree=ast.parse(_parent_source().decode())
    counts={"targets":0,"details":0,"publish":0,"result":0}
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="TARGETS" for t in node.targets):
            if not isinstance(node.value,ast.List) or len(node.value.elts)!=3:
                raise ValueError("exact three unrun WMR target definitions")
            node.value.elts.append(ast.Constant(NEW_TARGET));counts["targets"]+=1
        if isinstance(node,ast.FunctionDef) and node.name=="compute":
            body=[]
            for statement in node.body:
                if (isinstance(statement,ast.Expr) and isinstance(statement.value,ast.Call)
                    and isinstance(statement.value.func,ast.Name)
                    and statement.value.func.id=="save_details"):
                    body.extend(ast.parse("def extension():\n"+ASSEMBLY).body[0].body)
                    counts["details"]+=1
                if isinstance(statement,ast.Return):
                    body.extend(ast.parse("def extension():\n"+PUBLISH).body[0].body)
                    counts["publish"]+=1
                    if not isinstance(statement.value,ast.Dict):
                        raise ValueError("whole original WMR result mapping")
                    extras={
                        "complete_reference_world_height_computed":ast.Constant(True),
                        "complete_reference_height_coordinate_term_paid":ast.Constant(True),
                        "actual_reference_full_height_excludes_zero":ast.UnaryOp(
                            ast.Not(),ast.Call(ast.Attribute(ast.Name("saved_full_reference",ast.Load()),
                                "contains",ast.Load()),[ast.Constant(0)],[])),
                        "reference_waist_vertical_position_upper":ast.Constant("232743/1000000000"),
                    }
                    for key,value in extras.items():
                        statement.value.keys.append(ast.Constant(key));statement.value.values.append(value)
                    counts["result"]+=1
                body.append(statement)
            node.body=body
    if any(value!=1 for value in counts.values()):
        raise ValueError("one shared-grid extension and one new fourth target")
    ast.fix_missing_locations(tree)
    return tree


exec(compile(_build(),"<WRC first shared-grid full reference height>","exec"),globals())
