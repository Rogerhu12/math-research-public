#!/usr/bin/env python3
"""Reproduce every complete N-only source using only stdlib source/AST operations."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile

INPUTS = {'angular_observation_refinement.py': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3',
 'angular_transfer_additions.py': '5c83a16ef02f5381c17492fab47caa82cda355eec2e3b2cd1d2e1375a00234cf',
 'derive_angular_refinement_core.py': '6367b481877cfe41da0902bcc372de702274be4944838ef4121836d82a253b8e',
 'derive_angular_refinement_entry.py': 'ac1680f453c65240ee72073f9e49c1b667425cae58c58b4f165c254c27a56130',
 'derive_angular_refinement_memory.py': 'd196edae52e1aabae67cccfb88bb97190b18c1d8a5db8df0a7943b1ba169571f',
 'derive_angular_refinement_transfer.py': '78fe9e4e936006b623fe1b32a50f0f11d3a044e911b66fd2184a810b66c89c33'}
EXPECTED = {'angular_observation_refinement.py': '8506eb861bb8650ddfd0c5db5c268e8bb0a71b38e48ebb551767b45d2d339ab3',
 'angular_refined_material_envelope_memory.py': '5a011f9264db492f79f154719128387bfc7571a03f7b7a2b0e54880c01225685',
 'angular_refined_normal_frame_c1_reuse.py': 'e2ca9fee30128c9cd15d05fd636b3129df1de10522cb3b9bf03f1129d5c85a48',
 'angular_refined_reference_centred_calibration.py': '08fc5a1732740a597d2a47b47a91afe2bd5e0bc0541f6ab9fb0ae6297f9e1001',
 'angular_refined_smooth_triangle_literal_zero_moment_input.py': 'a4a53ff3ff92bb4fdbf8db2da048c717437d945423932e2b3d69cfc1cc06035d',
 'angular_refinement_history_transfer.py': '44feb567a2462522ca762c8bfd0af3404a358f1b0a623efd43981ebba498ac8b',
 'fullclosed_angular_refined_material_envelope_so3_qp.py': '75910e4b693c02979d1920ed0db43f78f9b7f106314263e6e1aef4ec9d217df6',
 'launch_angular_refined_material_envelope_so3_actions.py': '6c2c10bad7020dd664b6bf872dfc9994ad0dae227fc191bdd75abdcabeaf969b',
 'read_angular_refined_material_envelope_so3_report.py': 'afa9ee09917ef9e2825acfb1ceb504fb9ee83ced95b34a0c36760b3c51fcd11a',
 'so3_angular_refined_material_envelope_geometry.py': 'f5911b057295ffdb78baa2af1d71f971b6dfa3bc49cd04d49a7a08981a020bb5',
 'so3_angular_refined_reference_centred_normal_lift_operator.py': '765b8b8d3b2b142e1c1e7d2c6735eee6bdd79e8601449f05148f0ee1d6c27e1b',
 'so3_angular_refined_smooth_triangle_meridian_operator.py': '1ba446d9283891cfbb8d3af319a27804b4889f4b7f5f2891dea0b101aa042529'}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path):
    name='_source_construction_'+path.stem
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-directory',type=Path,required=True)
    p.add_argument('--output-directory',type=Path,required=True)
    p.add_argument('--verify-existing',action='store_true')
    args=p.parse_args()
    source=args.source_directory.resolve()
    for name,digest in INPUTS.items():
        if sha(source/name)!=digest:
            raise ValueError('The complete source-construction input changed: '+name)
    observer=(source/'angular_observation_refinement.py').read_text()
    additions=(source/'angular_transfer_additions.py').read_text()
    core=module(source/'derive_angular_refinement_core.py')
    memory=module(source/'derive_angular_refinement_memory.py')
    transfer=module(source/'derive_angular_refinement_transfer.py')
    entry=module(source/'derive_angular_refinement_entry.py')
    original_transfer=source/'transfer_material_envelope_memory_to_adjacent_frames.py'
    if sha(original_transfer)!=transfer.PARENT_SHA:
        raise ValueError('The complete published original parent-transfer body changed')
    result=core.derive(source,observer)
    result['angular_observation_refinement.py']=observer
    result['angular_refined_material_envelope_memory.py']=memory.derive(
        (source/'complete_material_envelope_memory.py').read_text(),observer)
    result['angular_refinement_history_transfer.py']=transfer.derive(original_transfer.read_text(),additions)
    with tempfile.TemporaryDirectory(prefix='N-refinement-source-only-') as temp:
        intermediate=Path(temp)
        for name,text in result.items():
            (intermediate/name).write_text(text)
        result.update(entry.derive(source,intermediate,observer))
    if set(result)!=set(EXPECTED):
        raise ValueError('The complete output source family differs')
    report={}
    args.output_directory.mkdir(parents=True,exist_ok=True)
    for name,text in result.items():
        data=text.encode()
        digest=hashlib.sha256(data).hexdigest()
        ast.parse(text);compile(text,name,'exec')
        if digest!=EXPECTED[name] or len(data)>=100000:
            raise ValueError('The full derived output differs: '+name)
        output=args.output_directory/name
        if args.verify_existing:
            if not output.is_file() or output.read_bytes()!=data:
                raise ValueError('Actual complete existing output differs: '+name)
        else:
            output.write_bytes(data)
        report[name]=dict(bytes=len(data),sha256=digest)
    print(json.dumps(dict(complete=True,science_imported_or_executed=False,
        full_outputs=report),sort_keys=True))


if __name__=='__main__':
    main()
