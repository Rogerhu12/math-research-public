"""One first WMR pass with the additional complete WRC reference-height row.

The frozen owner supplies whole input admission, carrier restoration,
signed publication and failure retention.  Only the immutable entry
identity, four-target schema and explicitly pinned parent sources differ.
"""
from __future__ import annotations
import ast,hashlib
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT_NAME="fourfold_codazzi_world_mean_height_owner.py"
PARENT_ROLE="WMR_owner"
PARENT_SHA="e7ee9d7f15b8b6f311f82def25e4485941db87f29ff7e1c7a5336510ed692fd2"
NEW_TARGET="complete_original_reference_world_mean_height_nu_full"
PARENT_INPUTS=[
    ("WMR_owner",TOPIC+"/scripts/"+PARENT_NAME,PARENT_SHA),
    ("WMR_math",TOPIC+"/scripts/fourfold_codazzi_world_mean_height_math.py",
        "38e83cec3f0117664025c32ee67d41e161576dabb1514c37b78cde5fc2776f48"),
    ("WMR_worker",TOPIC+"/scripts/fourfold_codazzi_world_mean_height_public_worker.py",
        "b7f4349942ee383077c6e4bdac82d90607fd6ac7d0d017584583738bdc5da26b"),
    ("WMR_generator",TOPIC+"/scripts/make_world_mean_height_manifest.py",
        "167734f686aa950ea4ac6f00a8aeea74a8ca23526a3c444460f56a9ea62f6778"),
    ("WMR_proof",TOPIC+"/results/R147-supplement-original-world-anchor-and-physical-mean-height-reduction.md",
        "1ed80e3dc5e04ab4dd4e89c76712ff69be4f2f956983d7bed516ec6fc3b8eee0"),
    ("WRC_saved_bounds",TOPIC+"/scripts/fourfold_codazzi_reference_world_height_saved_bounds.py",
        "cc1cd029923c87da80038660707818d5bfdb4b09b1911f438f692d2e37538259"),
    ("ARHI_proof",TOPIC+"/results/R147-supplement-actual-complete-relative-parameter-frame-and-position.md",
        "29035a269dde760b128efd74516ea923d337e6ab4675d9e20ba31201ab496716"),
]


def _parent_source():
    here=Path(__file__).resolve().parent
    for path in (here/PARENT_NAME,here/("input_"+PARENT_ROLE+".py")):
        if path.is_file():
            raw=path.read_bytes()
            if hashlib.sha256(raw).hexdigest()!=PARENT_SHA:
                raise ValueError("whole unchanged WMR owner parent")
            return raw
    raise ValueError("complete WMR owner input is absent")


def _namespace():
    tree=ast.parse(_parent_source().decode())
    changed=0;guards=0
    class ResultCount(ast.NodeTransformer):
        def visit_keyword(self,node):
            nonlocal changed
            if node.arg=="complete_new_record_count":
                if not isinstance(node.value,ast.Constant) or node.value.value!=3:
                    raise ValueError("exact original three-target owner result")
                node.value=ast.Constant(4);changed+=1
            return self.generic_visit(node)
    tree=ResultCount().visit(tree)
    body=[]
    for node in tree.body:
        if (isinstance(node,ast.If)
            and ast.dump(node.test)==ast.dump(ast.parse('__name__=="__main__"',mode="eval").body)):
            guards+=1
        else:
            body.append(node)
    tree.body=body
    if changed!=1 or guards!=1:
        raise ValueError("only the one result count and original entry guard change")
    ast.fix_missing_locations(tree)
    ns={"__name__":"_WRC_whole_frozen_owner","__file__":__file__}
    exec(compile(tree,"<WRC inherited whole owner>","exec"),ns)
    ns.update({
        "SOURCE":TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_owner.py",
        "MATH":TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_math.py",
        "WORKER":TOPIC+"/scripts/fourfold_codazzi_complete_reference_world_height_public_worker.py",
        "GENERATOR":TOPIC+"/scripts/make_complete_reference_world_height_manifest.py",
        "PROOF":TOPIC+"/results/R147-supplement-complete-reference-world-height-and-original-negative-receiver.md",
        "KIND":"R147_complete_reference_world_mean_height_nu_v1",
        "MANIFEST_KIND":"R147_complete_reference_world_mean_height_nu_inputs_v1",
        "STAGE":"complete_reference_world_mean_height_nu",
        "TARGETS":ns["TARGETS"]+[NEW_TARGET],"COUNTS":[3,1,1,1],
        "SIGNED_INDICES":(0,2,3),
    })
    ns["PARAMETERS"]=dict(ns["PARAMETERS"],new_complete_targets=4,
        complete_reference_position_contraction_degree=2080,
        reference_waist_vertical_position_upper="232743/1000000000",
        complete_reference_coordinate_variation_term="dotJ*f0_reference",
        complete_reference_anchor_fixed_at="9/50",
        actual_frame_position_anchor_differences_independent=True,
        original_three_WMR_targets_never_previously_executed=True)
    return ns


_INNER=_namespace()
_ORIGINAL_GATHER=_INNER["gather"]


def gather(root,rhi_actual,rhi_execution,rhi_manifest=_INNER["RHI_MANIFEST"]):
    declared=_ORIGINAL_GATHER(root,rhi_actual,rhi_execution,rhi_manifest)
    current={item["path"]:dict(item) for item in declared["files"]}
    roles=dict(declared["roles"]);root=Path(root)
    for role,path,digest in PARENT_INPUTS:
        raw=(root/path).read_bytes();raw.decode()
        if not 0<len(raw)<100000 or hashlib.sha256(raw).hexdigest()!=digest:
            raise ValueError("whole explicitly frozen WRC input: "+role)
        if path.endswith(".py"):
            ast.parse(raw.decode(),filename=path)
        spec={"role":role,"path":path,"bytes":len(raw),"sha256":digest,
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if path in current and any(current[path][key]!=spec[key] for key in
            ("path","bytes","sha256","git_blob_sha")):
            raise ValueError("same input alias must retain the whole object")
        current.setdefault(path,spec);roles[role]=path
    files=sorted(current.values(),key=lambda item:item["role"])
    all_specs=files+declared["historical_inputs"]
    if len({item["role"] for item in all_specs})!=len(all_specs):
        raise ValueError("every whole parent and new source has a distinct receipt")
    return dict(declared,files=files,roles=roles)


_INNER["gather"]=gather
globals().update({key:value for key,value in _INNER.items() if not key.startswith("__")})


if __name__=="__main__":
    raise SystemExit(main())
