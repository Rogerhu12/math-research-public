#!/usr/bin/env python3
"""Reuse one immutable context for up to four independently durable tiles."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import gc
from pathlib import Path
import traceback
from fd2d_gc_staged_search_context import NumericalContext
from fd2d_gc_normal_tile_io import partition_context,tile_binding
from fd2d_gc_partitioned_normal import assemble_normal_tile
from fd2d_gc_normal_checkpoint import save_normal_checkpoint,load_normal_checkpoint
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--tile-id',action='append',required=True)
    args=ap.parse_args()
    if not 1<=len(args.tile_id)<=4 or len(set(args.tile_id))!=len(args.tile_id):
        raise ValueError('Use one to four distinct explicit tiles')
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=True)
    ctx.report.update(stage='small_sequential_batch_of_independently_durable_normal_tiles',
        stage_source=identity(__file__),completed_tile_records=[],requested_tile_ids=args.tile_id,
        immutable_context_reused=True,normal_target_or_partition_changed=False)
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        selected=[d for d in plan['tiles'] if d['id'] in args.tile_id]
        if [d['id'] for d in selected]!=args.tile_id:
            raise ValueError('Requested tiles must be present in declared ordinal order')
        for descriptor in selected:
            if ctx.args.owner_stop_file.exists():
                ctx.save_report(owner_stop_observed=True,normal_batch_returncode=130)
                return 130
            tile_id=descriptor['id'];binding=tile_binding(common,descriptor)
            directory=root/'normal-tiles'/tile_id;manifest=directory/'manifest.json'
            recovered=manifest.exists()
            ctx.save_report(current_tile_id=tile_id)
            if recovered:
                normal=load_normal_checkpoint(ctx.problem,manifest,expected_binding=binding)
            else:
                def progress(kind,index,rows):
                    ctx.event('normal_tile_progress',tile_id=tile_id,phase=kind,index=index,rows=rows)
                normal,info=assemble_normal_tile(ctx.problem,ctx.vector,descriptor,
                    curvature_cap=ctx.args.curvature_cap,curvature_weight=ctx.args.curvature_weight,
                    high_gauss_weight=ctx.args.high_gauss_weight,high_codazzi_weight=ctx.args.high_codazzi_weight,
                    interior_gauss_weight=ctx.args.interior_gauss_weight,block_cells=ctx.args.block_cells,
                    cell_consumer=gauss_cell_positive_trace_frozen_operator_compatible,
                    progress=progress,binding=common)
                manifest=save_normal_checkpoint(normal,directory,binding=binding)
            record=dict(tile_descriptor=descriptor,tile_manifest=identity(manifest),
                rows=normal.rows,tile_residual_squared=normal.residual_squared,
                recovered_complete_tile=recovered)
            ctx.report['completed_tile_records'].append(record)
            ctx.save_report()
            ctx.event('normal_tile_durably_closed',tile_id=tile_id,ordinal=descriptor['ordinal'],
                rows=normal.rows,residual_squared=normal.residual_squared,manifest=str(manifest),
                recovered_complete_tile=recovered)
            del normal
            if not recovered:del info
            gc.collect()
        ctx.save_report(completed=True,normal_batch_returncode=0,current_tile_id=None)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
