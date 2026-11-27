#!/usr/bin/env python3
"""Stage the three whole continuous-geometry sources using only stdlib parsing.

No source is imported and no scientific arithmetic, field, root or interval
fixture is executed. The supplied complete files are authoritative; the
output is an independent whole-byte replay and complete static source check.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC="topics/visible-flex-larger-amplitude"
DIRECTORY="scripts/resume_20261126"
SOURCES=[
    [
        "run09_complete_physical_leaf_binding.py",
        "b71e2e87a910e9461f53a72977263dab0966e55ca1b5800927416343f6d7fb06",
        44591
    ],
    [
        "run09_continuous_gram_curvature_support.py",
        "91843225f698e7f6de945acc353f7a3733ac70719d93995099c2ac3e6186b40a",
        44853
    ],
    [
        "run09_complete_geometry_support_beta_bridge.py",
        "f14acf7bd84559b17de4359dc138ccd30b2b59ec26ec292336fd6b4686d99640",
        20741
    ]
]


def sha(value):
    return hashlib.sha256(value).hexdigest()

def literal(tree,name):
    values = [node.value for node in tree.body if isinstance(node,ast.Assign)
        and any(isinstance(t,ast.Name) and t.id==name for t in node.targets)]
    if len(values) != 1:
        raise ValueError("Keep the single complete literal source contract: "+name)
    return ast.literal_eval(values[0])

def duplicates(tree):
    for node in ast.walk(tree):
        if isinstance(node,ast.Dict):
            seen = set()
            for key in node.keys:
                if key is None:
                    continue
                try:
                    value = ast.literal_eval(key)
                    hash(value)
                except (ValueError,TypeError,SyntaxError):
                    continue
                if value in seen:
                    raise ValueError("Duplicate literal dictionary key")
                seen.add(value)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-dir",type=Path,required=True)
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--repo",type=Path)
    args=p.parse_args()
    source,out=args.source_dir.resolve(),args.outdir.resolve()
    if source==out or source in out.parents or out in source.parents:
        raise ValueError("Stage complete sources into an independent scratch directory")
    raw,trees,records={},{},[]
    for name,digest,size in SOURCES:
        value=(source/name).read_bytes()
        if len(value)!=size or sha(value)!=digest or size>=100000:
            raise ValueError("A complete supplied source differs: "+name)
        text=value.decode("utf-8")
        tree=ast.parse(text,filename=name)
        compile(tree,name,"exec")
        duplicates(tree)
        if any(line.rstrip()!=line for line in text.splitlines()):
            raise ValueError("Unexpected source trailing whitespace")
        raw[name],trees[name]=value,tree
        records.append(dict(name=name,bytes=size,sha256=digest))
    by_name={name:digest for name,digest,_ in SOURCES}
    leaf=trees["run09_complete_physical_leaf_binding.py"]
    main_tree=trees["run09_continuous_gram_curvature_support.py"]
    bridge=trees["run09_complete_geometry_support_beta_bridge.py"]
    for tree,key in ((main_tree,"LEAF_READER"),(bridge,"GEOMETRY_SOURCE")):
        name,digest=literal(tree,key)
        if by_name.get(name)!=digest:
            raise ValueError("A whole new source pin changed")
    beta=literal(main_tree,"BETA_SOURCE")
    if (literal(bridge,"BETA_SOURCE")!=beta
            or beta[1]!="e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991"):
        raise ValueError("Do not replace the complete original eight-role beta consumer")
    if literal(leaf,"NORMAL_FEE_SOURCE")[1]!="f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1":
        raise ValueError("The accurate full-stage source changed")
    external=[]
    if args.repo is not None:
        root=args.repo.resolve()/TOPIC/DIRECTORY
        pins=literal(leaf,"ACTUAL_INPUT_SOURCE_PINS")
        if len(pins)!=9:
            raise ValueError("Retain the complete accurate input's original nine source roles")
        needed=list(pins.items())
        needed+=[("normal_fee",literal(leaf,"NORMAL_FEE_SOURCE")),
            ("arithmetic",literal(leaf,"ROTATION_SOURCE")),("beta",beta),
            ("actual_input",("run09_normal_packet_accurate_field_input.py",
                "f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82")),
            ("accurate_radial",("run09_accurate_reference_control_radial_boxes.py",
                "0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b"))]
        for role,(name,digest) in needed:
            path=root/name
            value=path.read_bytes()
            if sha(value)!=digest:
                raise ValueError("A complete original source differs: "+role)
            external.append(dict(role=role,path=str(path),bytes=len(value),sha256=digest))
        driver=ast.parse((root/pins["driver"][0]).read_text())
        scientific=literal(driver,"SOURCE_PINS")
        if len(scientific)!=58:
            raise ValueError("Retain the entire original fifty-eight-role scientific registry")
        for role,(name,digest) in scientific.items():
            path=args.repo.resolve()/TOPIC/name
            value=path.read_bytes()
            if sha(value)!=digest:
                raise ValueError("An original complete scientific source differs: "+role)
            external.append(dict(scientific_role=role,path=str(path),bytes=len(value),sha256=digest))
    out.mkdir(parents=True,exist_ok=True)
    for name,value in raw.items():
        path=out/name
        if path.exists() and path.read_bytes()!=value:
            raise ValueError("An independently staged complete source has different bytes")
        if not path.exists():
            path.write_bytes(value)
    result=dict(schema="complete-run09-continuous-geometry-whole-source-stage-v1",
        complete_sources=records,complete_external_sources=external,
        complete_original_scientific_roles_verified=58 if args.repo is not None else None,
        full_source_AST_and_compile_without_import=True,
        scientific_fixture_or_field_or_interval_evaluation=False,
        complete_authoritative_sources_replayed_without_truncation=True)
    path=out/"whole-source-stage.json"
    path.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps(dict(complete_source_count=len(records),source_only=True,
        scientific_evaluation=False,report=str(path)),sort_keys=True))


if __name__=="__main__":
    main()
