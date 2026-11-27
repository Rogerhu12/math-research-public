#!/usr/bin/env python3
"""Reproduce the complete independent run10 closed/phase/grip source.

The entire original producer is read and SHA-bound before these complete
literal source changes. Full inverse restoration must recover it exactly.
This program only writes/parses/compiles source; it imports no scientific code
and evaluates no field, interval, root, integral or mathematical example.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC="topics/visible-flex-larger-amplitude"
PARENT_NAME="run09_complete_closed_phase_grip_evidence.py"
PARENT_SHA="7de5742e80c32721a6bc93c9451e1182ba08608f9a86387736ed30abb4ea9f1c"
PARENT_BYTES=69336
TARGET_NAME="run10_complete_closed_phase_grip_evidence.py"
TARGET_SHA="f7a10d7d6050cd57b5aea72d374c33662bf0c88e4175b6f7b738d6331d0976be"
TARGET_BYTES=70086
PATCHES=[
  {
    "kind": "replace-all-exact",
    "old": "run09",
    "new": "run10",
    "count": 7
  },
  {
    "kind": "replace-all-exact",
    "old": "f14acf7bd84559b17de4359dc138ccd30b2b59ec26ec292336fd6b4686d99640",
    "new": "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9",
    "count": 1
  },
  {
    "kind": "replace-all-exact",
    "old": "91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a",
    "new": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7",
    "count": 1
  },
  {
    "kind": "replace-once-exact",
    "old": "PROOFS = {\n",
    "new": "PROOFS = {\n    \"run10_current_source_adapter\": (\n        TOPIC+\"/notes/2026-11-27-run10-closed-phase-grip-source-adapter.md\",\n        \"b378593327e31a91385d4f5397c8fbb9294147febb843060941bfbaba92584e7\"),\n",
    "count": 1
  },
  {
    "kind": "replace-once-exact",
    "old": "        complete_old_field_and_target_unchanged=True,\n",
    "new": "        complete_old_field_and_target_unchanged=True,\n        original_field_in_this_statement_is_the_actual_run10_field=True,\n        cross_run09_target_point_or_certificate_inherited=False,\n        same_mathematical_g_as_run09_claimed=False,\n        complete_current_source_adapter_proof_sha256=\"b378593327e31a91385d4f5397c8fbb9294147febb843060941bfbaba92584e7\",\n",
    "count": 1
  },
  {
    "kind": "replace-once-exact",
    "old": "\"R661_components_only\",\"R715\",\"original_problem\")]\n",
    "new": "\"R661_components_only\",\"R715\",\"original_problem\",\"run10_current_source_adapter\")]\n",
    "count": 1
  },
  {
    "kind": "replace-once-exact",
    "old": "(\"source_specific_ports\",\"R248\",\"R650\",\"R661_components_only\",\"R716\")},\n",
    "new": "(\"source_specific_ports\",\"R248\",\"R650\",\"R661_components_only\",\"R716\",\"run10_current_source_adapter\")},\n",
    "count": 1
  },
  {
    "kind": "replace-once-exact",
    "old": "        if gripping[\"delta_hold_standard_sufficient\"] is not True:\n            remaining.append(\"The complete-image witness has not paid delta_hold >= 0.05D\")\n",
    "new": "        if gripping[\"delta_hold_standard_sufficient\"] is not True:\n            remaining.append(\"The complete-image witness has not paid delta_hold >= 0.05D\")\n        if gripping[\"delta_hold_stronger_target_sufficient\"] is not True:\n            remaining.append(\"The complete-image witness has not paid the stronger delta_hold >= 0.2D target\")\n",
    "count": 1
  }
]
DIRECT_DEPENDENCIES={
  "run10_complete_normal_root_and_sixjet_fees.py": "0d6e4c109f75e621ebceb7c660b3f4d5a798c34b15b6d90e4004ef9d97c5ac83",
  "accurate_normal_rotation_and_stage_boxes.py": "29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b",
  "read_run10_detached_closure_so3_report.py": "2efa4b1d7df920fb616b51988bc29730aa18b29ba57dc0a943d36cdcf87b3e8e",
  "fullclosed_run10_detached_closure_so3_qp.py": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
  "immutable_closure_values_normal_root_packets.py": "31f66203897cde00ca537f500209296ce2e42605f06a3cbbb1221e502e298805",
  "so3_reference_centred_closure_values_normal_lift_operator.py": "6d2b8e59bea94226ced74cd2bdab1ffa537e4afb1cd4594b2ed83e28832029f4",
  "so3_supported_smooth_triangle_meridian_operator.py": "6a80361a7f2fe376682fd63d39215630f5b31d4bc26493552b458691404db865",
  "so3_axisymmetric_reference.py": "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3",
  "so3_axisymmetric_continuous_integrand.py": "a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6",
  "run10_reference_seed_angular_profile_error_bounds.py": "91fd1fb0148c7dde3260bdcfed61b057033d308517960bdb86454cc1e96ab3a1",
  "run10_reference_accurate_mean_residuals.py": "19fd82f3d746cce4b7de474f42aeb4192e4e1cec8e38c375148bcd4a9ab51a38",
  "run10_normal_packet_accurate_field_input.py": "852bc97e2990051c776dfbbb5d17de265fd3321758fcfa201fe3d6d2b3adbda8",
  "run10_accurate_reference_control_radial_boxes.py": "fdddefd60f89c7d3cea4a59f8a3d1e1bd70764d53095907fbbc09f49f6fb0f3c",
  "run10_continuous_gram_curvature_support.py": "e3178af9e5f2313fd3d1e4f649424a0ee9cdaa205964d4b470582572f5be5ed7",
  "run10_complete_geometry_support_beta_bridge.py": "96d3467b15130c08948f52f701a80aeaf7a86337ebf3b9f1535b301e5677b8c9",
  "run10_complete_physical_leaf_binding.py": "cf571370b53288048db55dbcc0156a36de481a3fd91c9b3e0b85398905af39a5",
  "same_field_positive_support_parameter.py": "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991"
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def verify_source(text,name):
    tree=ast.parse(text,filename=name)
    compile(tree,name,"exec")
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            keys=[]
            for item in node.keys:
                if isinstance(item,ast.Constant) and isinstance(item.value,(str,int,float,bool,type(None))):
                    if item.value in keys:
                        raise ValueError("Duplicate literal dictionary key")
                    keys.append(item.value)
        if isinstance(node,ast.Call):
            keys=[item.arg for item in node.keywords if item.arg is not None]
            if len(keys)!=len(set(keys)):
                raise ValueError("Duplicate explicit keyword")
    if any(line.rstrip()!=line for line in text.splitlines()):
        raise ValueError("Trailing source whitespace")
    return tree


def proof_paths(tree):
    assignment=next(node for node in tree.body if isinstance(node,ast.Assign)
        and any(isinstance(v,ast.Name) and v.id=="PROOFS" for v in node.targets))
    result={}
    for key,value in zip(assignment.value.keys,assignment.value.values):
        role=ast.literal_eval(key)
        path_node,digest_node=value.elts
        if isinstance(path_node,ast.Constant):
            path=ast.literal_eval(path_node)
        elif (isinstance(path_node,ast.BinOp) and isinstance(path_node.op,ast.Add)
                and isinstance(path_node.left,ast.Name) and path_node.left.id=="TOPIC"):
            path=TOPIC+ast.literal_eval(path_node.right)
        else:
            raise ValueError("Unrecognized complete proof path expression")
        result[role]=(path,ast.literal_eval(digest_node))
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--verify-existing",action="store_true")
    a=p.parse_args()
    repo=a.repo.resolve()
    parent_path=repo/TOPIC/"scripts/resume_20261126"/PARENT_NAME
    raw=parent_path.read_bytes()
    if len(raw)!=PARENT_BYTES or digest(raw)!=PARENT_SHA:
        raise ValueError("The entire original closed-family producer changed")
    parent=raw.decode("utf-8")
    current=parent
    for patch in PATCHES:
        if (patch["kind"] not in ("replace-all-exact","replace-once-exact")
                or current.count(patch["old"])!=patch["count"]
                or patch["kind"]=="replace-once-exact" and patch["count"]!=1):
            raise ValueError("A complete explicit source change no longer applies")
        current=current.replace(patch["old"],patch["new"])
    reverse=current
    for patch in reversed(PATCHES):
        if reverse.count(patch["new"])!=patch["count"]:
            raise ValueError("The current source is not uniquely reversible")
        reverse=reverse.replace(patch["new"],patch["old"])
    if reverse!=parent:
        raise ValueError("The explicit source adapter changed an undeclared byte")
    result=current.encode("utf-8")
    if digest(result)!=TARGET_SHA or len(result)!=TARGET_BYTES:
        raise ValueError("The complete new source differs from the locked body")
    tree=verify_source(current,TARGET_NAME)
    for name,expected in DIRECT_DEPENDENCIES.items():
        path=repo/TOPIC/"scripts/resume_20261126"/name
        if digest(path.read_bytes())!=expected:
            raise ValueError("A complete run10 dependency changed: "+name)
    proofs=proof_paths(tree)
    for role,(path,expected) in proofs.items():
        if digest((repo/path).read_bytes())!=expected:
            raise ValueError("A complete formal/current-source proof changed: "+role)
    outdir=a.outdir.resolve()
    target=outdir/TARGET_NAME
    if a.verify_existing:
        if not target.is_file() or target.read_bytes()!=result:
            raise ValueError("The existing complete output differs")
    else:
        outdir.mkdir(parents=True,exist_ok=True)
        if target.exists():
            if target.read_bytes()!=result:
                raise ValueError("Refuse to overwrite a different complete source")
        else:
            with target.open("xb") as handle:
                handle.write(result)
    if target.stat().st_size!=TARGET_BYTES or digest(target.read_bytes())!=TARGET_SHA:
        raise ValueError("The entire output source changed")
    print(json.dumps(dict(schema="complete-run10-closed-phase-grip-source-reproducer-v1",
        parent=dict(path=str(parent_path),sha256=PARENT_SHA,bytes=PARENT_BYTES),
        result=dict(path=str(target),sha256=TARGET_SHA,bytes=TARGET_BYTES),
        complete_forward_inverse_text_reproduction=True,
        full_runtime_AST_and_compile_only=True,
        directly_bound_source_count=len(DIRECT_DEPENDENCIES),
        complete_proof_source_count=len(proofs),
        mathematical_or_scientific_module_import_or_execution=False),
        sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
