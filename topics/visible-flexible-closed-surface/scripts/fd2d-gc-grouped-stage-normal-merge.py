# R165 finite objective entry; never consumes a v25 old-goal packet.
#!/usr/bin/env python3
"""Restore normal tiles in plan order, releasing each generator reference before loading the next."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from pathlib import Path
import traceback
from fd2d_gc_grouped_search_context import NumericalContext
from fd2d_gc_grouped_normal_tile_io import partition_context,tile_binding,merged_normal_binding
from fd2d_gc_grouped_coast_partitioned_normal import merge_normal_tiles
from fd2d_gc_stage_io import load_baseline,atomic_json
from fd2d_gc_normal_checkpoint import save_normal_checkpoint,load_normal_checkpoint
from fd2d_gc_archive_arrays import identity


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False)
    ctx.report.update(stage='restore_and_sum_complete_actual_normal_partition',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        binding=merged_normal_binding(common,plan)
        directory=root/'normal-partitioned';manifest=directory/'manifest.json'
        recovered=manifest.exists();tile_records=[]
        if recovered:
            normal=load_normal_checkpoint(ctx.problem,manifest,expected_binding=binding)
            info=normal.info
        else:
            def tiles():
                for descriptor in plan['tiles']:
                    part=root/'normal-tiles'/descriptor['id']/'manifest.json'
                    normal=load_normal_checkpoint(ctx.problem,part,
                        expected_binding=tile_binding(common,descriptor))
                    tile_records.append(dict(id=descriptor['id'],ordinal=descriptor['ordinal'],
                        manifest=identity(part),rows=normal.rows,residual_squared=normal.residual_squared))
                    yield descriptor,normal
                    del normal
                    ctx.event('normal_tile_merged',tile_id=descriptor['id'],ordinal=descriptor['ordinal'])
            normal,info=merge_normal_tiles(ctx.problem,tiles(),plan)
        packet=load_baseline(ctx)
        squared=float(packet['residual']@packet['residual'])
        difference=abs(normal.residual_squared-squared)
        if difference>2e-10*max(1.,squared):
            raise ArithmeticError('Complete partition does not reproduce the actual original objective')
        info.update(actual_complete_value_objective_squared=squared,
            merged_normal_residual_squared=normal.residual_squared,
            actual_objective_squared_difference=difference)
        normal.info=info
        if not recovered:manifest=save_normal_checkpoint(normal,directory,binding=binding)
        summary=dict(schema='fd2d-complete-durable-partitioned-normal-v1',
            binding=binding,normal_manifest=identity(manifest),normal_information=info,
            complete_plan=plan,tile_records=tile_records,rows=normal.rows,
            residual_squared=normal.residual_squared,actual_value_objective_squared=squared,
            objective_squared_difference=difference,recovered_complete_normal=recovered,
            F_or_J_recomputed_during_merge=False,only_one_tile_plus_total_retained=True)
        out=root/'normal-partitioned-summary.json'
        if not out.exists():atomic_json(out,summary)
        ctx.save_report(completed=True,normal_manifest=identity(manifest),
            complete_normal_summary=identity(out),normal_information=info,
            recovered_complete_normal=recovered)
        ctx.event('partitioned_normal_durably_closed',manifest=str(manifest),
            tiles=len(plan['tiles']),rows=normal.rows,objective_squared_difference=difference,
            recovered_complete_normal=recovered)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
