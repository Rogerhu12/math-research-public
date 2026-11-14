#!/usr/bin/env python3
"""Run the original bounded small QP from an immutable saved Schur packet."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import json
from pathlib import Path
import traceback
import numpy as np
from fd2d_gc_staged_search_context import NumericalContext,array_identity
from fd2d_gc_normal_tile_io import partition_context,merged_normal_binding
from fd2d_gc_normal_checkpoint import load_normal_checkpoint
from fd2d_gc_packet_checkpoint import load_actual_packet
from fd2d_gc_saved_schur_search import bounded_direction_from_schur,normal_direction_quadratic
from fd2d_gc_schur_stage_io import factor_binding
from fd2d_gc_stage_io import atomic_json
from fd2d_gc_archive_arrays import identity,save_npz


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--factor-id',required=True)
    ap.add_argument('--direction-id',required=True)
    ap.add_argument('--central-floor',type=float)
    args=ap.parse_args()
    if any(Path(name).name!=name for name in (args.factor_id,args.direction_id)):
        raise ValueError('Use plain immutable factor and direction ids')
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=False,central_floor=args.central_floor)
    ctx.report.update(stage='original_bounded_QP_from_saved_same_normal_Schur',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root,plan,common,baseline=partition_context(ctx)
        normal_manifest=root/'normal-partitioned'/'manifest.json'
        saved_path=root/'reduced-factors'/args.factor_id/'summary.json'
        saved=json.loads(saved_path.read_text());here=Path(__file__).resolve().parent
        solver_name=Path(saved['solver_source']['path']).name
        producer_name=Path(saved['producer_source']['path']).name
        expected=factor_binding(ctx,normal_manifest,saved['damping'],here/solver_name,here/producer_name)
        if saved['binding']!=expected:raise ValueError('Saved factor does not bind the exact requested field, normal or source')
        manifest=saved['packet_manifest'];actual=identity(manifest['path'])
        if (actual['sha256'],actual['bytes'])!=(manifest['sha256'],manifest['bytes']):
            raise ValueError('Saved factor packet manifest changed')
        packet=load_actual_packet(manifest['path'],expected_binding=expected)
        normal=load_normal_checkpoint(ctx.problem,normal_manifest,expected_binding=merged_normal_binding(common,plan))
        destination=root/'directions'/args.direction_id
        destination.mkdir(parents=True,exist_ok=True)
        summary_path=destination/'summary.json'
        if summary_path.exists():raise FileExistsError('Keep every actually computed QP direction immutable')
        ctx.event('saved_Schur_QP_start',factor_id=args.factor_id,central_floor=ctx.args.central_floor,
            damping=saved['damping'],parameters=ctx.problem.parameter_count)
        def qp_progress(iteration,parameter_step):
            if iteration!=1 and iteration%10: return
            target=destination/'qp-iterate-latest.npz';temporary=target.with_suffix('.npz.writing')
            with temporary.open('wb') as stream:
                np.savez(stream,scaled_parameter_step=parameter_step,iteration=np.array(iteration),
                    factor_summary_sha256=np.array(identity(saved_path)['sha256']),
                    central_floor=np.array(ctx.args.central_floor))
            os.replace(temporary,target)
            ctx.save_report(latest_incomplete_QP_iterate=identity(target),QP_iteration=iteration)
            ctx.event('QP_iterate_observed',iteration=iteration,
                parameter_QP_value=float(.5*parameter_step@packet['schur']@parameter_step+packet['gradient']@parameter_step),
                actual_physical_trial=False)
        direction,information,reduced=bounded_direction_from_schur(ctx.problem,ctx.vector,normal,packet,
            central_floor=ctx.args.central_floor,central_cap=ctx.args.central_cap,
            profile_box=ctx.args.profile_box,preserve_gap=True,iteration_callback=qp_progress)
        original=direction.copy();direction=ctx.project(ctx.vector+direction)-ctx.vector
        information['before_projection_prediction']=normal_direction_quadratic(normal,original)
        information.update(normal_direction_quadratic(normal,direction))
        slope=information['actual_merit_slope']
        entity=save_npz(destination/'direction.npz',direction=direction,base_vector=ctx.vector.copy(),
            base_vector_definition=np.array(json.dumps(array_identity(ctx.vector),sort_keys=True)),
            damping=np.array(saved['damping']),central_floor=np.array(ctx.args.central_floor),
            merit_slope=np.array(slope),**reduced)
        summary=dict(schema='fd2d-actual-direction-from-durable-normal-v1',binding=ctx.binding,
            normal_manifest=identity(normal_manifest),saved_Schur_summary=identity(saved_path),direction=entity,
            base_vector=array_identity(ctx.vector),direction_array=array_identity(direction),
            direction_id=args.direction_id,damping=saved['damping'],
            search=dict(central_floor=ctx.args.central_floor,central_cap=ctx.args.central_cap,
                profile_box=ctx.args.profile_box,preserve_gap=True),
            actual_merit_slope=slope,direction_projection_maximum_change=float(np.max(abs(direction-original))),
            usable_descent=bool(np.isfinite(slope) and slope<0),information=information,
            actual_F_or_J_recomputed=False,actual_line_search_executed=False,stage_source=identity(__file__))
        atomic_json(summary_path,summary)
        ctx.save_report(completed=True,direction_summary=identity(summary_path),direction=entity,
            direction_information=information,actual_merit_slope=slope,actual_F_or_J_recomputed=False)
        ctx.event('bounded_QP_direction_durably_closed',direction_id=args.direction_id,
            linear_residual_norm=information['linear_residual_norm'],merit_directional_derivative=slope,
            optimizer_success=information['optimizer_success'],summary=str(summary_path))
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
