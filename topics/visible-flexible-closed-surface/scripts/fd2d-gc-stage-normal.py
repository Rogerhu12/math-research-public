#!/usr/bin/env python3
"""Assemble the unchanged finite normal system, save every block, then exit."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import json
from pathlib import Path
import traceback
import numpy as np
from fd2d_gc_staged_search_context import NumericalContext
from fd2d_gc_stage_io import atomic_json,load_baseline,normal_binding
from fd2d_gc_normal_checkpoint import save_normal_checkpoint,load_normal_checkpoint
from fd2d_gc_positive_trace_interior_stream_normal_consumer import stream_positive_trace_interior_normal
from fd2d_gc_gauss_cell_frozen_operator_compatible import gauss_cell_positive_trace_frozen_operator_compatible
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=True)
    ctx.report.update(stage='complete_actual_normal_before_QP',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root=Path(ctx.request['cache_dir'])
        packet=load_baseline(ctx);binding=normal_binding(ctx,packet)
        manifest=root/'normal'/'manifest.json';recovered=manifest.exists()
        if recovered:
            normal=load_normal_checkpoint(ctx.problem,manifest,expected_binding=binding)
            info=normal.info
        else:
            def progress(kind,index,rows):
                if kind!='node' or index%16==0:
                    ctx.event('normal_assembly',phase=kind,index=index,rows=rows)
            normal,info=stream_positive_trace_interior_normal(ctx.problem,ctx.vector,
                cells=ctx.args.interior_cells,interior_gauss_weight=ctx.args.interior_gauss_weight,
                curvature_cap=ctx.args.curvature_cap,curvature_weight=ctx.args.curvature_weight,
                high_gauss_weight=ctx.args.high_gauss_weight,high_codazzi_weight=ctx.args.high_codazzi_weight,
                block_cells=ctx.args.block_cells,progress=progress,
                cell_consumer=gauss_cell_positive_trace_frozen_operator_compatible)
        squared=float(packet['residual']@packet['residual'])
        difference=abs(normal.residual_squared-squared)
        if difference>2e-10*max(1.,squared):
            raise ArithmeticError('Normal rows do not reproduce the durable actual value objective')
        info.update(direct_full_objective_squared=squared,
            streamed_full_objective_squared=normal.residual_squared,
            objective_squared_difference=difference)
        normal.info=info
        # This durable boundary is deliberately before hff(), splu(), QP,
        # or even an attempted search direction.
        if not recovered:manifest=save_normal_checkpoint(normal,root/'normal',binding=binding)
        summary=dict(schema='fd2d-durable-complete-normal-stage-v1',binding=binding,
            normal_manifest=identity(manifest),normal_info=info,
            rows=normal.rows,blocks=normal.blocks,row_groups=normal.row_groups,
            storage_bytes=normal.storage_bytes(),residual_squared=normal.residual_squared,
            direct_objective_squared=squared,objective_squared_difference=difference,
            recovered_complete_normal=recovered,QP_or_line_search_executed=False,
            strong_target_complete=False)
        destination=root/'normal-summary.json'
        if not destination.exists():atomic_json(destination,summary)
        ctx.save_report(completed=True,normal_stage_summary=identity(destination),
            normal_manifest=identity(manifest),normal_info=info,
            recovered_complete_normal=recovered)
        ctx.event('normal_durably_closed',manifest=str(manifest),rows=normal.rows,
            objective_squared_difference=difference,storage_bytes=normal.storage_bytes(),
            recovered_complete_normal=recovered)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
