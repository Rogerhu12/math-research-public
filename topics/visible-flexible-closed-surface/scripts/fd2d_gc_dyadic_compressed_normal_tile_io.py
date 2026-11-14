# New lossless compressed tile transport; numerical fields and row partition unchanged.
"""Bindings for an exact row partition of the unchanged finite objective."""
import json
from pathlib import Path
from fd2d_gc_archive_arrays import identity
from fd2d_gc_dyadic_grouped_search_context import array_identity
from fd2d_gc_stage_io import atomic_json
from fd2d_gc_grouped_coast_partitioned_normal import make_normal_partition


def partition_context(context):
    root=Path(context.request['cache_dir'])
    summary=json.loads((root/'baseline-summary.json').read_text())
    if summary['binding']!=context.binding or summary['vector']!=array_identity(context.vector):
        raise ValueError('The actual baseline and requested context differ')
    described=summary['value_packet_manifest'];actual=identity(described['path'])
    if (actual['sha256'],actual['bytes'])!=(described['sha256'],described['bytes']):
        raise ValueError('The actual baseline packet manifest changed')
    plan=make_normal_partition(context.problem,node_block=16,cell_block=4,
        interior_cells=context.args.interior_cells,interior_block=1)
    destination=root/'normal-partition-plan.json'
    if destination.exists():
        if json.loads(destination.read_text())!=plan:
            raise ValueError('Do not silently replace an actual row partition')
    else:atomic_json(destination,plan)
    here=Path(__file__).resolve().parent
    sources=('fd2d_gc_grouped_coast_partitioned_normal.py','fd2d_gc_grouped_coast_stream_normal.py',
             'fd2d-gc-dyadic-compressed-stage-normal-tile-batch.py','fd2d-gc-compressed-piecewise-normal-reduce.py',
             'fd2d_gc_dyadic_compressed_normal_tile_io.py','fd2d_gc_normal_checkpoint.py','fd2d_gc_compressed_normal_tile.py','fd2d_gc_normal_capsule.py')
    common=dict(schema='fd2d-R170-R165-compressed-partitioned-normal-common-binding-v1',
        field_and_finite_objective=context.binding,
        actual_value_residual=summary['residual'],
        plan_sha256=plan['plan_sha256'],
        partition_sources={name:identity(here/name)['sha256'] for name in sources},
        partition_changes_only_floating_sum_grouping=True)
    return root,plan,common,summary


def tile_binding(common,descriptor):
    return dict(schema='fd2d-durable-normal-tile-binding-v1',common=common,descriptor=descriptor)


def merged_normal_binding(common,plan):
    return dict(schema='fd2d-durable-merged-normal-binding-v1',common=common,
        plan_sha256=plan['plan_sha256'],ordered_tile_ids=[d['id'] for d in plan['tiles']])
