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
from fd2d_gc_dyadic_grouped_search_context import NumericalContext,array_identity
from fd2d_gc_dyadic_stage_io import selected_normal,load_selected_normal,parent_factor_binding
load_normal_checkpoint=load_selected_normal
from fd2d_gc_packet_checkpoint import load_actual_packet
from fd2d_gc_dyadic_saved_schur_search import bounded_direction_from_schur,normal_direction_quadratic
from fd2d_gc_schur_stage_io import factor_binding
from fd2d_gc_stage_io import atomic_json
from fd2d_gc_archive_arrays import identity,save_npz


def tail_activity(problem, vector, tolerance=1e-10):
    """Finite search-box diagnostics; never a geometry certificate."""
    _, parameters = problem.unpack(vector)
    tail = np.asarray(parameters[problem.tail_parameter_slice], float)
    return dict(count=int(tail.size), tolerance=float(tolerance),
        minimum=float(tail.min()), maximum=float(tail.max()),
        lower_active_count=int(np.count_nonzero(np.abs(tail) <= tolerance)),
        upper_active_count=int(np.count_nonzero(np.abs(tail-1.2) <= tolerance)),
        below_lower_count=int(np.count_nonzero(tail < -tolerance)),
        above_upper_count=int(np.count_nonzero(tail > 1.2+tolerance)))


def unconstrained_prediction(problem, vector, normal, packet):
    """One same-Schur linear-model diagnostic, with all p constraints omitted.

    Exact structural field eliminations remain. The diagnostic is not a
    feasible trial, a new physical state, or a finite-space lower bound.
    """
    schur=np.asarray(packet['schur']); gradient=np.asarray(packet['gradient'])
    zp=np.linalg.solve(schur,-gradient)
    zf=-packet['solved'][:,0]-packet['solved'][:,1:]@zp
    direction=normal.mapping.expand(packet['field_scale']*zf,
                                   packet['parameter_scale']*zp)
    info=normal_direction_quadratic(normal,direction)
    info.update(parameter_constraints_omitted=True,
        omitted_constraints=['central bounds','tail coefficient box',
                             'profile box and radius rows','linear gap equality'],
        exact_structural_field_eliminations_preserved=True,
        same_damping=float(packet['damping']), same_schur_shift=float(packet['schur_shift']),
        small_schur_equation_maximum=float(np.max(np.abs(schur@zp+gradient))),
        proposed_tail=tail_activity(problem,vector+direction),
        actual_F_or_J_recomputed=False,actual_line_search_executed=False,
        finite_space_lower_bound_claimed=False,usable_physical_direction_claimed=False)
    return info


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
    ctx.report.update(stage='explicit_R170_tail_domain_QP_from_unchanged_same_function_Schur',stage_source=identity(__file__))
    ctx.save_report()
    try:
        root=Path(ctx.request['cache_dir'])
        normal_manifest,normal_binding,normal_origin=selected_normal(ctx)
        ctx.report['normal_origin']=normal_origin
        saved_path=root/'reduced-factors'/args.factor_id/'summary.json'
        saved=json.loads(saved_path.read_text());here=Path(__file__).resolve().parent
        solver_name=Path(saved['solver_source']['path']).name
        producer_name=Path(saved['producer_source']['path']).name
        expected=parent_factor_binding(ctx,normal_manifest,saved['damping'],here/solver_name,here/producer_name)
        if saved['binding']!=expected:raise ValueError('Saved factor does not bind the exact requested field, normal or source')
        manifest=saved['packet_manifest'];actual=identity(manifest['path'])
        if (actual['sha256'],actual['bytes'])!=(manifest['sha256'],manifest['bytes']):
            raise ValueError('Saved factor packet manifest changed')
        packet=load_actual_packet(manifest['path'],expected_binding=expected)
        normal=load_normal_checkpoint(ctx.problem,normal_manifest,expected_binding=normal_binding)
        baseline=json.loads((root/'baseline-summary.json').read_text())
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
        information['global_tail_box_for_comparison_only']=dict(current=tail_activity(ctx.problem,ctx.vector),
            proposed_before_projection=tail_activity(ctx.problem,ctx.vector+original),
            proposed_after_projection=tail_activity(ctx.problem,ctx.vector+direction))
        information['same_Schur_unconstrained_linear_diagnostic']=unconstrained_prediction(
            ctx.problem,ctx.vector,normal,packet)
        information['actual_baseline_curvature_merit']=dict(
            node=baseline['diagnostics']['curvature_merit'],
            interior=baseline['diagnostics']['interior_actual_constraints'],
            complete_objective_norm=baseline['objective_norm'],
            source='Previously saved complete actual same-state value packet; no new F/J')
        cn=float(baseline['diagnostics']['curvature_merit']['residual_l2'])
        ci=float(baseline['diagnostics']['interior_actual_constraints']['curvature_residual_l2'])
        information['actual_baseline_curvature_merit'].update(
            complete_weighted_curvature_l2=float(np.hypot(cn,ci)),
            complete_weighted_curvature_square_fraction=float((cn*cn+ci*ci)/baseline['objective_norm']**2),
            no_constraint_importance_or_infeasibility_inferred=True)
        information['actual_tail_projection']=ctx.last_projection_information
        information['tail_search_domain_definition']=ctx.problem.tail_search_domain_definition
        _,proposed_parameters=ctx.problem.unpack(ctx.vector+direction)
        information['exact_proposed_dyadic_certificate']=ctx.problem.tail_control_box.certificate(proposed_parameters[ctx.problem.tail_parameter_slice])
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
                profile_box=ctx.args.profile_box,preserve_gap=True,tail_search_domain=ctx.problem.tail_search_domain_definition),
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
