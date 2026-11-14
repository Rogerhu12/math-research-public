#!/usr/bin/env python3
"""Compute just one declared normal row group and save it atomically."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
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
    ap.add_argument('--tile-id',required=True)
    args=ap.parse_args()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=True)
    ctx.report.update(stage='one_immutable_actual_normal_tile',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        candidates=[d for d in plan['tiles'] if d['id']==args.tile_id]
        if len(candidates)!=1:raise ValueError('Requested tile is absent or duplicated in the exact plan')
        descriptor=candidates[0];binding=tile_binding(common,descriptor)
        directory=root/'normal-tiles'/args.tile_id;manifest=directory/'manifest.json'
        recovered=manifest.exists()
        if recovered:
            normal=load_normal_checkpoint(ctx.problem,manifest,expected_binding=binding)
            info=normal.info
        else:
            def progress(kind,index,rows):
                ctx.event('normal_tile_progress',tile_id=args.tile_id,phase=kind,index=index,rows=rows)
            normal,info=assemble_normal_tile(ctx.problem,ctx.vector,descriptor,
                curvature_cap=ctx.args.curvature_cap,curvature_weight=ctx.args.curvature_weight,
                high_gauss_weight=ctx.args.high_gauss_weight,high_codazzi_weight=ctx.args.high_codazzi_weight,
                interior_gauss_weight=ctx.args.interior_gauss_weight,block_cells=ctx.args.block_cells,
                cell_consumer=gauss_cell_positive_trace_frozen_operator_compatible,
                progress=progress,binding=common)
            manifest=save_normal_checkpoint(normal,directory,binding=binding)
        ctx.save_report(completed=True,tile_descriptor=descriptor,
            tile_manifest=identity(manifest),tile_information=info,
            recovered_complete_tile=recovered,rows=normal.rows,
            tile_residual_squared=normal.residual_squared)
        ctx.event('normal_tile_durably_closed',tile_id=args.tile_id,ordinal=descriptor['ordinal'],
            rows=normal.rows,residual_squared=normal.residual_squared,manifest=str(manifest),
            recovered_complete_tile=recovered)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
