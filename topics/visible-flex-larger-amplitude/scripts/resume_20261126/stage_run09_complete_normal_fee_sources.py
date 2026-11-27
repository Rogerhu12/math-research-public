#!/usr/bin/env python3
"""Stage and parse the four entire accurate-normal-fee sources, without importing them.

These are original complete source units, not truncated patches. This stdlib
utility replays the delivered whole-byte source set into an independent scratch
directory and checks its complete local source-pin closure. It performs no
mathematical or numerical evaluation and is not a scientific admission gate.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

SOURCES = [
    ["accurate_normal_rotation_and_stage_boxes.py","29eed317796b18c5f7430535ee2f45ee7ce9cb6546bbbd44d0bc97b9839e3f6b",27453],
    ["run09_normal_packet_accurate_field_input.py","f0808c8563679a85969aaf56a3d4fa87de99b58635e5ad72853bc54f30c42f82",26431],
    ["run09_accurate_reference_control_radial_boxes.py","0587d88cd46ea8379b7e250872ed1b34deb0452ab7d61ae230c284bac126d42b",45392],
    ["run09_complete_normal_root_and_sixjet_fees.py","f5ecc7fb67d4c34d5c52cba16ba0cee94b8fb5872f14c67123a190b32c6450c1",40268],
]
EXTERNAL_INPUT_PINS = {
    "driver": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
    "reader": "aee22caf8dc3e544cd0d7a5e80e6475608dc397a4c2aa1095c0adb72238f0b32",
    "normal": "3d8d3ed8f2a21db5731fec87115546502a49b701f7344328e8e36396cba52dbc",
    "packets": "094ca6a87213a8677b46aa9b0ad4c5a4b12f8c4c80437d7b640c47f7793b40f0",
    "reference_fees": "7666e726f424e2d95c53b4d57e28a195923cb344a5fd34487fee9d00950677b1",
    "mean_integrals": "17427d11f8a0b0685260e90a20947306d0c474c11be97b30662978a2223af820",
}
TOPIC = "topics/visible-flex-larger-amplitude"
DIRECTORY = "scripts/resume_20261126"


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
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-dir",type=Path,required=True)
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--repo",type=Path,
        help="Optionally verify all actually present external full sources and the original 58-role registry")
    args = p.parse_args()
    source,outdir = args.source_dir.resolve(),args.outdir.resolve()
    if source==outdir or source in outdir.parents or outdir in source.parents:
        raise ValueError("Stage into a separate scratch tree without overwriting the source tree")
    records,trees,raw = [],{},{}
    for name,digest,size in SOURCES:
        data = (source/name).read_bytes()
        if len(data)!=size or sha(data)!=digest or size>=100000:
            raise ValueError("Whole source identity differs: "+name)
        text = data.decode("utf-8")
        tree = ast.parse(text,filename=name)
        compile(tree,name,"exec")
        duplicates(tree)
        if any(line.rstrip()!=line for line in text.splitlines()):
            raise ValueError("Unexpected source whitespace change: "+name)
        trees[name],raw[name] = tree,data
        records.append(dict(name=name,bytes=size,sha256=digest))
    named = {name:digest for name,digest,_ in SOURCES}
    upper = literal(trees["run09_complete_normal_root_and_sixjet_fees.py"],"PINS")
    if set(upper) != {"actual_input","accurate_rotation","accurate_radial"}:
        raise ValueError("Keep all three complete lower source roles")
    for role,(name,digest) in upper.items():
        if named.get(name)!=digest:
            raise ValueError("The complete producer has a different lower source: "+role)
    radial = trees["run09_accurate_reference_control_radial_boxes.py"]
    for key,digest in {
            "INPUT_SHA":named["run09_normal_packet_accurate_field_input.py"],
            "ROTATION_SHA":named["accurate_normal_rotation_and_stage_boxes.py"],
            "MEAN_SHA":EXTERNAL_INPUT_PINS["mean_integrals"],
            "SEED_MATH_SHA":EXTERNAL_INPUT_PINS["reference_fees"]}.items():
        if literal(radial,key)!=digest:
            raise ValueError("The accurate radial source contract differs: "+key)
    inputs = literal(trees["run09_normal_packet_accurate_field_input.py"],"PINS")
    for role,digest in EXTERNAL_INPUT_PINS.items():
        if inputs[role][1]!=digest:
            raise ValueError("The complete actual input source contract differs: "+role)
    external = []
    if args.repo is not None:
        repo = args.repo.resolve()
        scripts = repo/TOPIC/DIRECTORY
        for role,(name,digest) in inputs.items():
            data = (scripts/name).read_bytes()
            if sha(data)!=digest:
                raise ValueError("An actual complete external input source differs: "+role)
            external.append(dict(role=role,path=str(scripts/name),bytes=len(data),sha256=digest))
        driver_tree = ast.parse((scripts/inputs["driver"][0]).read_text())
        roles = literal(driver_tree,"SOURCE_PINS")
        if len(roles)!=58:
            raise ValueError("Keep the actual entire scientific source registry")
        for role,(relative,digest) in roles.items():
            path = repo/TOPIC/relative
            data = path.read_bytes()
            if sha(data)!=digest:
                raise ValueError("An original full scientific role differs: "+role)
            external.append(dict(scientific_role=role,path=str(path),bytes=len(data),sha256=digest))
    outdir.mkdir(parents=True,exist_ok=True)
    for name,data in raw.items():
        path = outdir/name
        if path.exists() and path.read_bytes()!=data:
            raise ValueError("An existing staged whole source has different bytes")
        if not path.exists():
            path.write_bytes(data)
    result = dict(schema="complete-run09-normal-fee-whole-source-stage-v1",
        complete_sources=records,external_source_records=external,
        complete_original_scientific_roles_verified=58 if args.repo is not None else None,
        full_AST_and_compile_without_import=True,scientific_evaluation=False,
        source_files_truncated_or_reconstructed_from_numeric_output=False,
        supplied_complete_source_set_is_authoritative=True)
    path = outdir/"whole-source-stage.json"
    path.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps(dict(source_count=len(records),source_only=True,
        scientific_evaluation=False,report=str(path)),sort_keys=True))


if __name__ == "__main__":
    main()
