"""Exact identities and atomic metadata for independent finite-search stages."""
import json
import os
from pathlib import Path
from fd2d_gc_archive_arrays import identity
from fd2d_gc_packet_checkpoint import load_actual_packet
from fd2d_gc_staged_search_context import array_identity


def atomic_json(path, value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_suffix(path.suffix+'.writing')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    os.replace(temporary,path)


def load_baseline(context):
    root=Path(context.request['cache_dir'])
    packet=load_actual_packet(root/'baseline-values'/'manifest.json',expected_binding=context.binding)
    if array_identity(packet['vector'])!=array_identity(context.vector):
        raise ValueError('The durable baseline is for a different actual vector')
    return packet


def normal_binding(context, packet):
    here=Path(__file__).resolve().parent
    return dict(schema='fd2d-durable-normal-binding-v1',
        field_and_finite_objective=context.binding,
        actual_value_residual=array_identity(packet['residual']),
        assembly_entry_sha256=identity(here/'fd2d-gc-stage-normal.py')['sha256'],
        stage_io_source_sha256=identity(__file__)['sha256'],
        damping_and_search_floor_not_part_of_normal_identity=True)
