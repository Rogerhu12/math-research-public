#!/usr/bin/env python3
"""Read the actual q060 saved-inner terminal; do not repeat a solve/audit."""
import argparse
import gzip
import io
import json
import math
from pathlib import Path

import numpy as np

from recovering_tail_client_v2 import exact_equal, read_gzip, sha, physical_solver_config, payload_sha


def ref(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def flatten(value):
    if not isinstance(value,list):return [value]
    return [v for child in value for v in flatten(child)]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory',type=Path,required=True)
    parser.add_argument('--session',type=int,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); directory=args.directory.resolve()
    if args.out.exists():
        raise FileExistsError('Preserve the completed original record')
    entry_path=directory/'seed-resume-entry.json'
    entry=json.loads(entry_path.read_text())
    for path,digest in entry['source_sha256'].items():
        assert sha(path)==digest,path
    for key in ('entry_plan','raw_inner','dn_anchor','accepted_initializer'):
        assert sha(entry['provenance'][key]['path'])==entry['provenance'][key]['sha256']
    assert entry['maximum_total_outer_indices']==list(range(8)) and entry['warmup_scales']==[]
    cp_path=directory/'seed.json.gz'; cp=read_gzip(cp_path)
    summary_path=directory/'seed-summary.json'; summary=json.loads(summary_path.read_text())
    terminal_path=directory/'seed-resume-terminal.json'; terminal=json.loads(terminal_path.read_text())
    observation_path=directory/'observation.json'; observation=json.loads(observation_path.read_text())
    assert observation['status']=='observed_terminal' and observation['child_returncode']==0
    assert terminal['original_main_returned'] is True and terminal['original_solver_success'] is True
    assert terminal['original_error'] is None and terminal['original_summary']==ref(summary_path)
    assert cp['solver_success'] is True and cp['config']['actual_nonlinear_tail'] is True
    assert cp['config']['fixed_metric'] is False
    assert all(exact_equal(value,cp[key]) for key,value in summary.items() if key!='seconds')
    assert summary['seconds']>=cp['seconds']  # original serialization adds elapsed time
    assert cp['config']['modes']==8 and cp['config']['base_mode']==3
    assert cp['config']['core_kind']=='adaptive_warped_support'
    assert cp['gauge_amplitude']==cp['actual_primary_amplitude']==.06
    assert cp['max_rms_collocation_residual']<=cp['config']['tol']
    checks=cp['actual_outer_checks']
    assert [row['outer'] for row in checks]==[0,1]
    assert checks[0]['actual_boundary_residual']>cp['config']['bc_tol']
    assert checks[-1]['inner_success'] is True
    assert checks[-1]['actual_boundary_residual']<=cp['config']['bc_tol']
    assert cp['summary']['physical_bc_max']<=cp['config']['physical_bc_tol']
    diag=cp['saved_inner_resume_diagnostics']
    assert diag['final_solution_is_restored_raw_inner'] is False
    assert diag['message_provenance']=='new_actual_solve_bvp'
    assert diag['rms_provenance']=='new_actual_solve_bvp_vector'
    assert diag['original_interval_rms_reconstructed'] is False
    assert diag['input_resume_provenance']['remaining_original_outer_indices']==list(range(1,8))
    assert cp['tail_calls']==3
    raw0=read_gzip(entry['provenance']['raw_inner']['path'])
    raw1_path=directory/'seed-inner-0001-debug.json.gz'
    anchor1_path=directory/'seed-inner-0001-dn-anchor.json'
    raw1=read_gzip(raw1_path); anchor1=json.loads(anchor1_path.read_text())
    assert raw1['outer']==anchor1['outer']==1 and raw1['projected_solver_success'] is True
    assert raw1['actual_tail_accepted'] is False and anchor1['actual_tail_accepted'] is False
    assert anchor1['raw_inner']==ref(raw1_path)
    assert exact_equal(anchor1['candidate_cut_height'],raw1['candidate_cut_height'])
    assert exact_equal(cp['parameters'],raw1['parameters'])
    assert exact_equal(cp['frozen_profile'],raw1['candidate_frozen_profile'])
    chunks=[]
    for part in cp['pp_coefficient_chunks']:
        path=directory/part['file']; assert sha(path)==part['sha256']
        assert path.stat().st_size==part['bytes']
        values=np.load(io.BytesIO(gzip.decompress(path.read_bytes())),allow_pickle=False)
        assert np.all(np.isfinite(values))
        chunks.append(dict(**ref(path),shape=list(values.shape),dtype=str(values.dtype),
            state_first=part['state_first'],state_last_exclusive=part['state_last_exclusive']))
    coefficients=np.asarray(cp['parameters'][1:])*np.asarray(cp['central_correction_scales'])
    assert exact_equal([cp['actual_primary_amplitude'],*coefficients.tolist()],cp['summary']['core']['coefficients'])
    tail_records=[]; natives=[]
    for call in (1,2,3):
        path=directory/f'seed_tail_{call:04d}.json.gz'
        native=read_gzip(path); response=native['response']; natives.append(native)
        assert response.get('converged') is True and response['residual']<2e-9
        J=flatten(response['heightJetJacobian'])
        assert len(J)==208 and all(math.isfinite(value) for value in J)
        assert exact_equal(physical_solver_config(native['config']),physical_solver_config(cp['tail_config']))
        if natives:assert native['source_sha256']==natives[0]['source_sha256']
        assert exact_equal(response['checkpoint']['cutHeight'],native['request']['height'])
        tail_records.append(dict(call=call,file=ref(path),request=native['request'],
            residual=response['residual'],jacobian_entries=len(J),jacobian_all_finite=True,
            audit_present=response.get('audit') is not None,
            audit=response.get('audit'),iterations=len(response['history']),
            first_iteration=response['history'][0],last_iteration=response['history'][-1]))
    assert [row['audit_present'] for row in tail_records]==[True,False,True]
    initializer=read_gzip(entry['provenance']['accepted_initializer']['path'])
    assert exact_equal(natives[0]['request']['height'],raw0['candidate_cut_height'])
    assert exact_equal(natives[0]['response']['checkpoint']['states'],initializer['response']['checkpoint']['states'])
    affine=anchor1['affine_actual_tail']
    assert affine['sha256']==sha(directory/'seed_tail_0001.json.gz')
    assert affine['response_sha256']==payload_sha(natives[0]['response'])
    assert affine['configuration_sha256']==payload_sha(natives[0]['config'])
    assert exact_equal(affine['request'],natives[0]['request'])
    assert exact_equal(natives[1]['request']['height'],raw1['candidate_cut_height'])
    assert exact_equal(natives[2]['request']['height'],cp['tail_seam']['tail_jets']['height'])
    assert cp['tail_seam']['tail_converged'] is True
    assert cp['tail_seam']['tail_shooting_residual']==natives[2]['response']['residual']
    height_changes=[]
    for j,(before,after) in enumerate(zip(natives[1]['request']['height'],natives[2]['request']['height'],strict=True)):
        if not exact_equal(before,after):
            height_changes.append(dict(index=j,before=before,after=after,
                difference=after-before,difference_over_ulp_of_before=(after-before)/math.ulp(before)))
    seam={key:value for key,value in cp['tail_seam'].items() if key!='tail_jets'}
    seam['tail_mean_and_geometry']={key:value for key,value in cp['tail_seam']['tail_jets'].items()
                                   if not isinstance(value,list)}
    finite_summary={key:value for key,value in cp['summary'].items() if key!='core'}
    result=dict(scope='Genuine original-solver terminal of the saved-inner continuation. All entries are read from stored outputs; no BVP, flow, complete metric or seam computation is repeated. Finite sampled prefix and tail audits do not certify a complete closed surface or a continuous metric bound.',
        collector=ref(__file__),collector_helpers={name:sha(Path(__file__).with_name(name)) for name in
            ('recovering_tail_client_v2.py',)},
        actual_entry=ref(entry_path),launch_plan=ref(directory/'launch-plan.json'),
        owned_manifest=entry['source_manifest'],resume_provenance=entry['provenance'],
        session=args.session,command=entry['command'],original_main_arguments=entry['original_main_arguments'],
        checkpoint=ref(cp_path),coefficient_chunks=chunks,summary=ref(summary_path),
        runner_terminal=ref(terminal_path),observer=ref(observation_path),
        log=ref(directory/'solver.log'),resume_events=ref(directory/'seed-resume-events.jsonl'),
        recovery_events=ref(directory/'seed_tail-recovery-events.jsonl'),
        source_sha256=entry['source_sha256'],
        solver_success=True,original_solver_config=cp['config'],
        physical_profile=cp['frozen_profile'],meridian_length_binary64=cp['meridian_length'],
        q_gauge=cp['gauge_amplitude'],q_actual=cp['actual_primary_amplitude'],
        full_parameters=cp['parameters'],full_correction_scales=cp['central_correction_scales'],
        full_support_coefficients=cp['summary']['core']['coefficients'],
        physical_port_sha256=cp['physical_port_sha256'],
        frozen_candidate_metric_identity=dict(
            scope='The complete physical design returned by this unfixed design solve; freeze all these inputs for any subsequent fixed-g refinement. This record is not itself a continuous integral/atlas error certificate.',
            core_kind=cp['config']['core_kind'],base_mode=3,
            core_q=cp['actual_primary_amplitude'],full_support_coefficients=cp['summary']['core']['coefficients'],
            profile=cp['frozen_profile'],warp_reference_q=cp['warp_reference_q'],
            chart_kind=cp['angular_chart'],chart_payload_sha256=payload_sha(cp['chart']),
            original_chart_file=raw1['inputs']['chart'],
            physical_port_sha256=cp['physical_port_sha256'],physical_tail_parameters=cp['physical_tail_parameters'],
            physical_tail_cut=cp['physical_tail_cut'],meridian_length_binary64=cp['meridian_length']),
        nodes=cp['nodes'],message=cp['message'],max_rms=cp['max_rms_collocation_residual'],
        current_process_newton_domain_audit=cp['newton_domain_audit'],
        actual_outer_checks=checks,original_total_outer_indices=list(range(8)),
        original_inner0_recomputed=False,new_inner_indices=[1],
        saved_inner_resume_diagnostics=diag,tail_records=tail_records,
        saved_outer1=dict(raw_inner=ref(raw1_path),dn_anchor=ref(anchor1_path),
            nodes=len(raw1['raw_inner_solution']['mesh']),
            state_variables=len(raw1['raw_inner_solution']['values']),
            recorded_projected_max_rms=raw1['max_rms_collocation_residual'],
            affine_request=affine['request'],affine_response_canonical_payload_sha256=affine['response_sha256'],
            affine_configuration_canonical_payload_sha256=affine['configuration_sha256']),
        final_export_request_scope='Original C2/export post-processing forms the final physical H again; three components differ from the raw-inner H by one binary64 ULP. The original worker genuinely accepts this final full request with Jacobian and audit; an earlier response is not substituted.',
        final_export_height_changes=height_changes,
        finite_prefix_summary=finite_summary,finite_tail_seam=seam,
        observation=observation,
        serialization_seconds=dict(checkpoint=cp['seconds'],summary=summary['seconds'],runner=terminal['seconds']),
        resource_scope='Sampled namespace RSS and RUSAGE_CHILDREN high-water observations have different scope; neither is a measured whole-host memory peak.',
        design_not_fixed_g_convergence=True,core_is_local_circle=False,
        continuous_metric_bound=False,closed_surface_certificate=False,held_10pct_claimed=False,
        data_policy='Only source/input/output identities, original physical parameter vectors and compact scalar results are published. Polynomial/state/Jacobian arrays remain scratch-only.')
    assert len(height_changes)==3 and all(abs(row['difference_over_ulp_of_before'])==1 for row in height_changes)
    text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    assert len(text.encode())<100000
    args.out.write_text(text)
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out),solver_success=True,
                         metric=cp['summary']['metric_l1'],tail_residual=cp['tail_seam']['tail_shooting_residual'])))


if __name__=='__main__':
    main()
