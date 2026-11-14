# R165 finite objective entry; never consumes a v25 old-goal packet.
#!/usr/bin/env python3
"""Evaluate one real Armijo trial from immutable baseline/direction files."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import json
from pathlib import Path
import traceback
import numpy as np
from fd2d_gc_dyadic_grouped_search_context import NumericalContext,array_identity
from fd2d_gc_stage_io import atomic_json,load_baseline
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_packet_checkpoint import save_actual_packet
from fd2d_gc_search_domain_roundoff import checked_search_domain
from fd2d_gc_bump_residual_locations import residual_locations
from fd2d_gc_checkpointed_grouped_values import checkpointed_grouped_objective


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--direction-id',required=True)
    ap.add_argument('--backtracking-index',type=int,required=True)
    args=ap.parse_args()
    if Path(args.direction_id).name!=args.direction_id or not 0<=args.backtracking_index<22:
        raise ValueError('Use a plain direction id and the original backtracking range')
    request=json.loads(args.request.read_text());root=Path(request['cache_dir'])
    direction_path=root/'directions'/args.direction_id/'summary.json'
    direction_record=json.loads(direction_path.read_text())
    ctx=NumericalContext(args.request,args.out_prefix,install_caches=True,
        central_floor=direction_record['search']['central_floor'])
    ctx.report.update(stage='R170_actual_checkpointed_Armijo_trial',stage_source=identity(__file__),value_engine_source=identity(Path(__file__).resolve().parent/'fd2d_gc_checkpointed_grouped_values.py'))
    ctx.save_report()
    try:
        packet=load_baseline(ctx)
        if direction_record['binding']!=ctx.binding:
            raise ValueError('Direction and actual finite baseline identities differ')
        entity=direction_record['direction']
        actual=identity(entity['path'])
        if actual['sha256']!=entity['sha256'] or actual['bytes']!=entity['bytes']:
            raise ValueError('Saved actual direction changed')
        arrays=load_npz(entity['path'])
        if array_identity(arrays['base_vector'])!=array_identity(ctx.vector):
            raise ValueError('Saved direction starts at a different vector')
        if array_identity(arrays['direction'])!=direction_record['direction_array']:
            raise ValueError('Direction array checksum differs')
        alpha=2.**(-args.backtracking_index)
        slope=float(direction_record['actual_merit_slope'])
        cost=.5*float(packet['residual']@packet['residual'])
        threshold=cost+1e-4*alpha*slope
        trial=ctx.project(ctx.vector+alpha*arrays['direction'])
        result=dict(schema='fd2d-independent-actual-Armijo-trial-v1',binding=ctx.binding,
            direction_summary=identity(direction_path),direction_id=args.direction_id,
            backtracking_index=args.backtracking_index,alpha=alpha,
            actual_trial_vector=array_identity(trial),baseline_cost=cost,
            merit_directional_derivative=slope,armijo_threshold=threshold,
            accepted=False,actual_full_residual_evaluated=False,
            stage_source=identity(__file__),strong_target_complete=False,tail_search_domain=ctx.problem.tail_search_domain_definition,actual_projection=ctx.last_projection_information)
        destination=root/'trials'/args.direction_id/('back-%02d.json'%args.backtracking_index)
        if destination.exists():
            raise FileExistsError('An immutable trial already exists; consume its recorded outcome')
        if not np.isfinite(slope) or slope>=0:
            result['rejection']='Saved direction is not a finite descent direction'
        else:
            permitted,domain=checked_search_domain(ctx.problem,trial,ctx.args.central_cap,ctx.args.central_floor)
            result['domain']=domain;result['domain_diagnostics']=ctx.domain_diagnostics(trial)
            if not permitted:
                result['rejection']='Original actual search-domain comparison rejected the trial'
            else:
                try:
                    residual,data=checkpointed_grouped_objective(ctx,trial,root/'trial-value-cache'/args.direction_id/('back-%02d'%args.backtracking_index))
                except (FloatingPointError,ValueError,OverflowError) as exc:
                    result['rejection']='Actual field/residual evaluation rejected the trial'
                    result['evaluation_exception']=dict(type=type(exc).__name__,message=str(exc))
                else:
                    value=.5*float(residual@residual)
                    result.update(actual_full_residual_evaluated=True,actual_cost=value,
                        objective_norm=float(np.linalg.norm(residual)),
                        actual_residual=array_identity(residual),diagnostics=ctx.diag(trial,data),
                        locations=residual_locations(ctx.problem,trial,data,
                            data['codazzi_complement_result'],ctx.args.curvature_cap))
                    if np.isfinite(value) and value<threshold:
                        result['accepted']=True
                        accepted_state=ctx.checkpoint(trial,'-accepted.npz')
                        result['accepted_state']=accepted_state
                        # Save the actual accepted entity and report BEFORE
                        # optional transport of its full diagnostic packet.
                        ctx.save_report(accepted_steps=1,latest_checkpoint=accepted_state,
                            latest=result['diagnostics'],actual_cost=value,
                            alpha=alpha,armijo_threshold=threshold)
                        ctx.event('actual_accepted_state_saved',checkpoint=accepted_state,
                            alpha=alpha,objective_norm=result['objective_norm'])
                        accepted_binding=dict(schema='fd2d-actual-accepted-value-packet-binding-v1',
                            original_context=ctx.binding,actual_vector=array_identity(trial),
                            accepted_state_sha256=accepted_state['sha256'],
                            actual_direction_summary_sha256=identity(direction_path)['sha256'],
                            alpha=alpha)
                        manifest=save_actual_packet(dict(vector=trial.copy(),residual=residual,data=data),
                            root/'accepted-values',binding=accepted_binding)
                        result['accepted_value_packet']=identity(manifest)
                        result['accepted_value_binding']=accepted_binding
                        _,parameters=ctx.problem.unpack(trial)
                        ctx.problem.profile.set_parameters(parameters[ctx.problem.profile_parameter_slice])
                        metric=ctx.stem.with_name(ctx.stem.name+'-physical-metric.json')
                        atomic_json(metric,ctx.problem.profile.definition())
                        result['physical_metric']=identity(metric)
                        atomic_json(root/'accepted-result.json',result)
                    else:
                        result['rejection']='Complete actual Armijo inequality failed'
        atomic_json(destination,result)
        ctx.save_report(completed=True,accepted_steps=int(result['accepted']),
            trial_result=identity(destination),trial_outcome=result)
        ctx.event('actual_trial_durably_closed',direction_id=args.direction_id,
            backtracking_index=args.backtracking_index,alpha=alpha,
            accepted=result['accepted'],actual_full_residual_evaluated=result['actual_full_residual_evaluated'],
            actual_cost=result.get('actual_cost'),baseline_cost=cost,
            armijo_threshold=threshold,result=str(destination))
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        ctx.event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
