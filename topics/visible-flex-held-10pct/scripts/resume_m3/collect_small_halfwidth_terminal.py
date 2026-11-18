#!/usr/bin/env python3
"""Collect the existing a=.01 endpoint terminal; no solver is imported."""
import argparse
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def load(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();run=args.run.resolve()
    launch=load(run/'continuation-command.json')
    wrapper=load(run/'seed-round-record.json')
    summary=load(run/'seed-summary.json')
    cp_path=run/'seed.json.gz';cp=load(cp_path)
    resource=load(run/'resource.json');worker=load(run/'seed_tail_worker_exit.json')
    if (resource['status']!='observed_terminal' or resource['child_returncode']!=0 or
        launch['returncode']!=0 or worker['events'][-1]['returncode']!=0):
        raise ValueError('An observed complete terminal with original worker exit is required')
    if (cp['solver_success'] or summary['solver_success'] or
        cp['message']!='The maximum number of mesh nodes is exceeded.' or
        summary['tail_calls']!=4 or len(list(run.glob('seed_tail_[0-9]*.json.gz')))!=4):
        raise ValueError('The recorded endpoint stopping classification differs')
    settings=cp['core_round_settings']
    if settings['halfwidth']!=.01 or settings['homotopy']!=1. or settings['transition']!=.32 or settings['control_transition']!=.4:
        raise ValueError('This collector is only the declared small-halfwidth new design')
    if cp['summary']!=summary['summary'] or cp['tail_seam']!=summary['tail_seam']:
        raise ValueError('The checkpoint does not contain the same complete saved audits')
    for mapping in [launch['inputs'],launch['input_coefficient_chunks'],wrapper['source_hashes']]:
        for path,digest in mapping.items():
            if sha(path)!=digest:raise ValueError('Recorded source or input changed: '+path)
    chunks=[];next_state=0
    for item in cp['pp_coefficient_chunks']:
        path=run/item['file']
        if item['state_first']!=next_state or sha(path)!=item['sha256']:
            raise ValueError('Physical polynomial chunk coverage/identity changed')
        array=np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
        if array.dtype!=np.dtype('float64') or not np.isfinite(array).all():
            raise ValueError('The physical quintic coefficients must be finite float64')
        chunks.append(dict(path=str(path),sha256=sha(path),shape=list(array.shape),
            state_first=item['state_first'],state_last_exclusive=item['state_last_exclusive']))
        next_state=item['state_last_exclusive']
    M=cp['config']['modes']
    if M!=16 or next_state!=3*M+1:raise ValueError('Complete M16 physical state coverage required')
    records=[];heights=[]
    for index in range(1,5):
        path=run/f'seed_tail_{index:04d}.json.gz';record=load(path);response=record['response']
        tolerance=record['config']['solveTolerance']
        if tolerance!=2e-9 or response.get('converged') is not True or not math.isfinite(response['residual']) or not response['residual']<tolerance:
            raise ValueError('An actual tail call did not pass the original stopping gate')
        jac=response.get('heightJetJacobian') or []
        if not all(math.isfinite(x) for x in jac) or (record['request']['jacobian'] and len(jac)!=(3*M+2)*M):
            raise ValueError('A requested finite full Jacobian is missing')
        if record['request']['audit'] and response.get('audit') is None:
            raise ValueError('A requested full finite audit is missing')
        heights.append(np.asarray(record['request']['height'],dtype='float64'))
        records.append(dict(call=index,path=str(path),sha256=sha(path),
            original_gate=tolerance,residual=response['residual'],
            requested_jacobian=record['request']['jacobian'],requested_audit=record['request']['audit'],
            finite_jacobian_entries=len(jac),full_finite_audit_returned=response.get('audit') is not None,
            height_binary64_sha256=hashlib.sha256(heights[-1].tobytes()).hexdigest(),
            first_height=float(heights[-1][0]),last_iteration=response['history'][-1]))
    if heights[0].tobytes()!=heights[1].tobytes() or heights[0].tobytes()==heights[2].tobytes():
        raise ValueError('Expected identical initial H pair and a distinct final candidate H')
    final_height_difference=heights[3]-heights[2]
    metric=summary['summary'];seam=summary['tail_seam'];core=metric['core']
    result=dict(status='Complete failed a=.01 lambda-one prefix; all four finite tail calls passed their original stopping gate',
        scope='Only existing source/output/physical-polynomial identities are read. No BVP, tail solve, or full audit is rerun.',
        observed_execution=dict(session=19739,observer=resource,launcher_returncode=launch['returncode'],
            worker_exit=worker,prefix_coupler_seconds=summary['seconds'],wrapper_seconds=wrapper['seconds'],
            interpretation='Exit 0 reports normal program completion, not mathematical acceptance.'),
        command=launch['command'],source_sha256=wrapper['source_hashes'],
        input_sha256=launch['inputs'],input_coefficient_chunks=launch['input_coefficient_chunks'],
        collector_sha256=sha(__file__),
        terminal_files={str(run/name):sha(run/name) for name in ['continuation-command.json',
            'seed-summary.json','seed-round-record.json','seed-c2-restart-record.json','resource.json',
            'process.log','seed_tail_worker_exit.json','seed_tail_worker_stderr.log','worker-trace.jsonl']},
        failed_physical_checkpoint=dict(path=str(cp_path),sha256=sha(cp_path),chunks=chunks,
            role='Complete saved physical quintic plus final numerical audits of a failed inner iterate; not an accepted prefix or an original raw-cubic dump.'),
        original_inner={key:cp[key] for key in ['solver_success','message','nodes',
            'max_rms_collocation_residual','newton_domain_audit','actual_outer_checks']},
        q_gauge=cp['gauge_amplitude'],actual_q=cp['actual_primary_amplitude'],
        profile=cp['frozen_profile'],core_settings=settings,
        parameters=cp['parameters'],central_correction_scales=cp['central_correction_scales'],
        physical_controls=(np.asarray(cp['parameters'][1:])*np.asarray(cp['central_correction_scales'])).tolist(),
        saved_complete_finite_prefix_audit={key:metric[key] for key in ['metric_l1','flow_defect','darboux_l1',
            'root_min','chart_rho_min','physical_bc_max','samples_s','samples_psi','scope']},
        final_core_scalars={key:core[key] for key in ['rho_lower_conservative','rho_triangle_lower',
            'rho_min_sample','rho_max_sample','positivity_grid_per_sector','rho_derivative_bound',
            'rho_second_derivative_bound','plateau_radius_at_one','plateau_material_length']},
        tail_calls=records,new_candidate_height_queried=True,
        final_audit_height_identity=dict(calls=[3,4],
            binary64_identical=heights[2].tobytes()==heights[3].tobytes(),
            changed_component_indices=np.flatnonzero(final_height_difference).tolist(),
            maximum_absolute_difference=float(np.max(abs(final_height_difference))),
            scope='The terminal and seam audit use their own actual saved H requests. '
                'They are compared literally; nearby floating values are not declared identical.'),
        saved_complete_finite_seam={key:seam[key] for key in ['tail_converged','tail_shooting_residual',
            'mean_first_mismatch','mean_second_mismatch','nonmean_first_mismatch','nonmean_second_mismatch',
            'cut_metric_fft_l1','cut_metric_c1_fft_l1','angular_samples','scope']},
        limits='The positive numerical core guard and accepted actual tails did not make the prefix acceptable. '
            'The complete finite metric is far above 1e-6, the inner solver failed, and the a=.01 arc has '
            'no inherited a=.21 holding witness. This failed state is not an accepted continuation anchor; '
            'the unclassified domain rejection counter cannot be assigned to one cause without trial evidence.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),nodes=cp['nodes'],
        rms=cp['max_rms_collocation_residual'],metric=metric['metric_l1'],tail_calls=len(records))),flush=True)


if __name__=='__main__':main()
