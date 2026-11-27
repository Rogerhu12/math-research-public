"""Metadata-only first four-target WMR/WRC entry after the real RHI completion."""
from __future__ import annotations
import ast,hashlib,json
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT_NAME="make_world_mean_height_manifest.py"
PARENT_SHA="167734f686aa950ea4ac6f00a8aeea74a8ca23526a3c444460f56a9ea62f6778"
RENAMES={
 "R147_complete_physical_mean_height_nu_kernel_20261127":
    "R147_complete_reference_world_mean_height_nu_20261127",
 "name: R147 complete physical mean-height parameter kernel":
    "name: R147 complete reference-world mean-height parameter column",
 "  group: visible-exact-world-mean-height-20261127":
    "  group: visible-exact-complete-reference-world-height-20261127",
 "  first-complete-physical-mean-height:":
    "  first-complete-reference-world-height:",
 "      - name: Restore fixed whole carriers and pair the full physical height kernel":
    "      - name: Restore fixed whole carriers and pair complete reference-world height",
 TOPIC+"/notes/world_mean_height_ci/consumed-target.json":
    TOPIC+"/notes/complete_reference_world_height_ci/consumed-target.json",
 TOPIC+"/notes/world_mean_height_ci":
    TOPIC+"/notes/complete_reference_world_height_ci",
}


def _namespace():
    path=Path(__file__).resolve().with_name(PARENT_NAME)
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=PARENT_SHA:
        raise ValueError("whole frozen metadata-only WMR generator")
    tree=ast.parse(raw.decode())
    counts={name:0 for name in RENAMES};record_counts=0;guards=0
    class Extension(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in RENAMES:
                counts[node.value]+=1
                return ast.copy_location(ast.Constant(RENAMES[node.value]),node)
            return node
        def visit_Dict(self,node):
            nonlocal record_counts
            for index,key in enumerate(node.keys):
                if isinstance(key,ast.Constant) and key.value=="complete_record_counts":
                    if ast.dump(node.values[index])!=ast.dump(ast.parse("[3]",mode="eval").body):
                        raise ValueError("original whole three-target metadata count")
                    node.values[index]=ast.parse("[4]",mode="eval").body;record_counts+=1
            return self.generic_visit(node)
    tree=Extension().visit(tree);body=[]
    for node in tree.body:
        if (isinstance(node,ast.If)
            and ast.dump(node.test)==ast.dump(ast.parse('__name__=="__main__"',mode="eval").body)):
            guards+=1
        else:
            body.append(node)
    tree.body=body
    if record_counts!=1 or guards!=1 or any(value!=1 for value in counts.values()):
        raise ValueError("only complete entry names and one target count change")
    ast.fix_missing_locations(tree)
    ns={"__name__":"_WRC_frozen_metadata_generator","__file__":__file__}
    exec(compile(tree,"<WRC inherited first-entry generator>","exec"),ns)
    ns.update({
        "OWNER":TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_owner.py",
        "WORKER":TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_public_worker.py",
        "MANIFEST":TOPIC+"/notes/2026-11-27-complete-reference-world-height-inputs.json",
        "WORKFLOW":".github/workflows/visible-exact-complete-reference-world-height.yml",
    })
    return ns


_INNER=_namespace()
_ORIGINAL_BUILD=_INNER["build"]


def build(root,rhi_actual,rhi_execution,rhi_manifest):
    raw,unused_yaml=_ORIGINAL_BUILD(root,rhi_actual,rhi_execution,rhi_manifest)
    manifest=json.loads(raw)
    manifest["scope"].update({
        "all_four_new_targets_share_one_necessary_carrier_restoration":True,
        "original_three_WMR_targets_never_previously_executed":True,
        "complete_reference_world_mean_height_includes_dotJ_f0":True,
        "reference_anchor_is_the_original_fixed_raw_anchor_at_b":True,
        "complete_known_reference_waist_position_error_paid":True,
        "actual_frame_and_position_anchor_differences_independent":True,
        "full_reference_value_does_not_close_actual_world_Schur":True,
    })
    raw=(json.dumps(manifest,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode()
    if len(raw)>=100000:
        raise ValueError("whole small immutable new first manifest")
    return raw,_INNER["workflow"](manifest["files"],hashlib.sha256(raw).hexdigest())


_INNER["build"]=build
globals().update({key:value for key,value in _INNER.items() if not key.startswith("__")})


if __name__=="__main__":
    main()
