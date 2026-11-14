#!/usr/bin/env python3
"""Use the complete ordered normal tile sum for a bounded Schur direction."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import json
from pathlib import Path
import traceback
import numpy as np
from fd2d_gc_staged_search_context import NumericalContext,array_identity
from fd2d_gc_stage_io import atomic_json
from fd2d_gc_normal_tile_io import partition_context,merged_normal_binding
from fd2d_gc_normal_checkpoint import load_normal_checkpoint
from fd2d_gc_local_normal_system import bounded_normal_direction
from fd2d_gc_archive_arrays import identity,save_npz


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--direction-id',required=True)
    ap.add_argument('--damping',type=float,required=True)
    ap.add_argument('--central-floor',type=float)
    args=ap.parse_args()
    if Path(args.direction_id).name!=args.direction_id:
        raise ValueError('direction-id must be a plain basename')
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False,central_floor=args.central_floor)
    ctx.report.update(stage='actual_bounded_direction_from_saved_ordered_normal_tile_sum',stage_source=identity(__file__),
        actual_damping=args.damping,actual_central_floor=ctx.args.central_floor)
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        manifest=root/'normal-partitioned'/'manifest.json'
        normal=load_normal_checkpoint(ctx.problem,manifest,expected_binding=merged_normal_binding(common,plan))
        destination=root/'directions'/args.direction_id
        destination.mkdir(parents=True,exist_ok=True)
        summary_path=destination/'summary.json'
        if summary_path.exists():
            raise FileExistsError('Keep each actually computed direction immutable; choose a fresh id')
        direction,info,reduced=bounded_normal_direction(ctx.problem,ctx.vector,normal,
            damping=args.damping,central_floor=ctx.args.central_floor,
            central_cap=ctx.args.central_cap,profile_box=ctx.args.profile_box,
            preserve_gap=True,return_reduced=True)
        original=direction.copy()
        direction=ctx.project(ctx.vector+direction)-ctx.vector
        slope=float(normal.gf@direction[normal.mapping.free]+normal.gp@direction[normal.mapping.total:])
        arrays=dict(direction=direction,base_vector=ctx.vector.copy(),
            base_vector_definition=np.array(json.dumps(array_identity(ctx.vector),sort_keys=True)),
            damping=np.array(args.damping),central_floor=np.array(ctx.args.central_floor),
            merit_slope=np.array(slope),**reduced)
        entity=save_npz(destination/'direction.npz',**arrays)
        summary=dict(schema='fd2d-actual-direction-from-durable-normal-v1',
            binding=ctx.binding,normal_manifest=identity(manifest),direction=entity,
            base_vector=array_identity(ctx.vector),direction_array=array_identity(direction),
            direction_id=args.direction_id,damping=args.damping,
            search=dict(central_floor=ctx.args.central_floor,central_cap=ctx.args.central_cap,
                profile_box=ctx.args.profile_box,preserve_gap=True),
            actual_merit_slope=slope,direction_projection_maximum_change=float(np.max(abs(direction-original))),
            usable_descent=bool(np.isfinite(slope) and slope<0),information=info,
            actual_F_or_J_recomputed=False,actual_line_search_executed=False,
            stage_source=identity(__file__))
        atomic_json(summary_path,summary)
        ctx.save_report(completed=True,direction_summary=identity(summary_path),
            direction=entity,direction_information=info,actual_merit_slope=slope,
            actual_F_or_J_recomputed=False)
        ctx.event('direction_durably_closed',direction_id=args.direction_id,
            damping=args.damping,merit_directional_derivative=slope,
            linear_residual_norm=info['linear_residual_norm'],
            optimizer_success=info['optimizer_success'],summary=str(summary_path))
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
