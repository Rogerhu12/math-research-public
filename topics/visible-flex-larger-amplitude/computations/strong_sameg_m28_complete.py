#!/usr/bin/env python3
"""Complete the original same-g M28 provenance after staged postprocessing.

The original spectral plan, real M24 fixed view, full exact M24-to-M28 warm
embedding, accepted M28 raw and complete staged acceptance must all bind.
Only after the original physical postprocessor and its full RMS/BC/audit
gates finish is the standard same_g_spectral_refinement record attached.
This does not rerun Newton, modify the metric/chart, or replace an audit with
a metadata flag. --attach-completed-only is for an already completed physical
packet and repeats all the identity/acceptance checks before metadata writes.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key,None)
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
import strong_sameg_m28_postprocess as post
from root_actual_staged_tail import raw_arrays,read_json,sha,equation_config

SELF_SHA=sha(__file__)
POST_SHA='80044bf34cb90b104149e4c212647f322dce1d59dac6fe1ba7723d8ba60b5277'
PLAN_SHA='625be5f52341af64198d70722ae7c7c3922e3bef678effedc425560021e582e0'
WARM_CHECK_SHA='0021c30166d833f94a437656c3ca884549a1957b4133abd7b88dd8b34f1281d2'
ACCEPTED_SHA='4ce9b8927b864fd5627b64949d786aff0f4a409d1d6f19a3329ff26363bad1b3'
PENDING_SHA='2defe8acda9dadd4c85fa05c9c01f6528622b491c898712386fa89976a4b3163'


def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False)


def argument(argv,name):
    if argv.count(name)!=1:raise ValueError('Exactly one '+name+' is required')
    return Path(argv[argv.index(name)+1])


def local_binding(parent,item):
    path=parent/Path(item['file']).name
    if sha(path)!=item['sha256']:raise ValueError('A recorded original file differs: '+str(path))
    return path


def same_array(a,b):
    return a.shape==b.shape and a.dtype==b.dtype and a.tobytes()==b.tobytes()


def verify_original_chain(argv):
    plan_file=argument(argv,'--original-spectral-plan')
    accepted_file=argument(argv,'--accepted-raw')
    pending_file=argument(argv,'--raw-collocation-restart')
    fixed_file=argument(argv,'--fixed-reference')
    config_file=argument(argv,'--tail-config')
    if (sha(post.__file__)!=POST_SHA or sha(plan_file)!=PLAN_SHA or
            sha(accepted_file)!=ACCEPTED_SHA or sha(pending_file)!=PENDING_SHA):
        raise ValueError('This completion is only for the original stored recovery6 M28 solve')
    plan=read_json(plan_file)
    if not plan_file.name.endswith('-spectral-plan.json'):
        raise ValueError('Original spectral plan basename differs')
    warm_check_file=plan_file.with_name(plan_file.name[:-len('-spectral-plan.json')]+'-spectral-warm-verified.json')
    if sha(warm_check_file)!=WARM_CHECK_SHA:
        raise ValueError('The original live spectral embedding verification differs')
    warm_check=read_json(warm_check_file)
    if sha(fixed_file)!=plan['fixed_reference']['sha256'] or sha(config_file)!=plan['new_config']['sha256']:
        raise ValueError('Original exact fixed reference or M28 tail configuration differs')
    fixed=read_json(fixed_file);config=read_json(config_file)
    coarse_file=local_binding(plan_file.parent,plan['fixed_raw'])
    report_file=local_binding(plan_file.parent,plan['fixed_view_report'])
    baseline_file=local_binding(plan_file.parent,plan['baseline_config'])
    report=read_json(report_file);baseline=read_json(baseline_file)
    if (report['output']['sha256']!=sha(fixed_file) or report['raw_output']['sha256']!=sha(coarse_file) or
            report.get('original_parameter_count')!=27 or report.get('fixed_parameter_count')!=24 or
            report.get('counters')!={'raw_restorations':1,'residual_checks':1,'tail_start_attempts':0} or
            report.get('nonlinear_solve_run') is not False or report.get('tail_worker_started') is not False):
        raise ValueError('The actual original 27-to-24 fixed-view report does not bind')
    for key in ('complete_H_bitwise_equal','raw_x_y_cubic_unchanged','physical_quintics_unchanged',
                'all_core_coefficients_unchanged','gauge_unchanged',
                'original_numerical_reference_unchanged','eight_physical_data_unchanged'):
        if report.get(key) is not True:raise ValueError('Original fixed-view gate was not paid: '+key)
    changed=[k for k in sorted(set(config)|set(baseline))
             if canonical(config.get(k))!=canonical(baseline.get(k))]
    if set(changed)-set(post.spectral.IO_KEYS)!={'modes'} or baseline['modes']!=24 or config['modes']!=28:
        raise ValueError('Original old/new tail changed more than the spectrum and I/O')
    accepted,A=raw_arrays(accepted_file);pending,B=raw_arrays(pending_file)
    if (not accepted['solver_success'] or accepted['status']!=0 or
            accepted['physical_surface'] is not False or pending['solver_success'] or
            not pending['provenance'].get('affine_inner_success') or
            not pending['provenance'].get('actual_nonlinear_coupling_pending')):
        raise ValueError('Original accepted/pending raw status differs')
    if canonical(accepted['identity'])!=canonical(pending['identity']):
        raise ValueError('The accepted and pending complete identities differ')
    if not all(same_array(A[key],B[key]) for key in ('x','y','p','cubic','rms')):
        raise ValueError('The complete original accepted/pending state is not identical')
    coarse,C=raw_arrays(coarse_file)
    warm_file=local_binding(plan_file.parent,warm_check['warm_checkpoint'])
    warm,W=raw_arrays(warm_file)
    identity=accepted['identity']
    if (not coarse['solver_success'] or not coarse['identity']['fixed'] or
            coarse['identity']['modes']!=24 or coarse['identity']['angular']!=768 or
            warm['solver_success'] or warm['physical_surface'] is not False or
            not warm['provenance'].get('spectral_warm_only') or
            warm['provenance'].get('source_plan_sha256')!=PLAN_SHA or
            warm['provenance'].get('source_fixed_raw_sha256')!=sha(coarse_file) or
            canonical(warm['identity'])!=canonical(warm_check['live_identity']) or
            canonical(warm['identity'])!=canonical(identity)):
        raise ValueError('Original complete live spectral warm identity differs')
    if (identity['modes']!=28 or identity['angular']!=1024 or not identity['fixed'] or
            identity['tol']!=1e-7 or
            identity['coupling_context']['tail_config_sha256']!=sha(config_file)):
        raise ValueError('Original M28/N1024/tol7 actual problem differs')
    for key in ('gauge','profile','physical_tail_parameters','physical_tail_cut',
                'reference_coefficients','reference_frequencies','parameter_layout','tol','bc_tol',
                'numerical_reference_knots'):
        if canonical(coarse['identity'][key])!=canonical(identity[key]):
            raise ValueError('Old/new physical/reference datum differs: '+key)
    mapping=np.r_[np.arange(25),29+np.arange(24),57+np.arange(24)]
    new_rows=np.array(sorted(set(range(85))-set(mapping.tolist())),dtype=int)
    if (mapping.tolist()!=plan['state_channel_embedding'] or new_rows.tolist()!=plan['new_zero_state_rows'] or
            not same_array(W['x'],C['x']) or not same_array(W['rms'],C['rms']) or
            not same_array(W['y'][mapping],C['y']) or
            not same_array(W['cubic'][:,:,mapping],C['cubic']) or
            not same_array(W['p'][:24],C['p']) or
            not np.all(W['y'][new_rows]==0) or not np.all(W['cubic'][:,:,new_rows]==0) or
            not np.all(W['p'][24:]==0)):
        raise ValueError('The original full exact 24-to-28 spectral embedding does not reproduce')
    for key in ('original_grid_retained_bitwise','physical_grid_retained_bitwise',
                'actual_basis_zero_first_second_rows_bitwise_equal','original_core_preserved_bitwise'):
        if warm_check.get(key) is not True:
            raise ValueError('Original actual live embedding gate differs: '+key)
    if warm_check['pinned_basis_source_sha256']!='e621ee2e9e8a706332b3839122a8ec57e1c5c2cfe82a48a759dcdad0548c54b2':
        raise ValueError('The original live basis identity differs')
    original_H=-float(identity['gauge'])*W['y'][57:,-1]
    if original_H.tobytes()!=np.asarray(warm_check['exact_complete_warm_H'],dtype=np.float64).tobytes():
        raise ValueError('The original complete M28 warm H changed')
    if (not np.all(np.diff(A['x'])>0) or A['x'][0]!=0 or A['x'][-1]!=1 or len(C['x'])!=2181):
        raise ValueError('The complete original t interval/grid is not retained')
    indices=np.searchsorted(A['x'],C['x'])
    if np.any(indices>=len(A['x'])) or not same_array(A['x'][indices],C['x']):
        raise ValueError('An original2181 raw t node is missing from the accepted M28 state')
    if (canonical(plan['profile'])!=canonical(fixed['frozen_profile']) or
            canonical(plan['profile'])!=canonical(identity['profile']) or
            plan['physical_length']!=fixed['meridian_length'] or
            plan['gauge']!=identity['gauge'] or
            canonical(plan['original_numerical_reference'])!=canonical(identity['numerical_reference_knots'])):
        raise ValueError('The original frozen metric/length/chart plan differs')
    record=dict(scope=__doc__,entry_sha256=SELF_SHA,postprocessor_sha256=POST_SHA,
        original_plan=dict(file=str(plan_file),sha256=PLAN_SHA),
        original_warm_verification=dict(file=str(warm_check_file),sha256=WARM_CHECK_SHA),
        fixed_reference=dict(file=str(fixed_file),sha256=sha(fixed_file)),
        original_fixed_raw=dict(file=str(coarse_file),sha256=sha(coarse_file)),
        actual_fixed_view_report=dict(file=str(report_file),sha256=sha(report_file)),
        original_warm_raw=dict(file=str(warm_file),sha256=sha(warm_file)),
        accepted_raw=dict(file=str(accepted_file),sha256=ACCEPTED_SHA),
        pending_raw=dict(file=str(pending_file),sha256=PENDING_SHA),
        original_M24_to_M28_complete_embedding_replayed_bitwise=True,
        new_channels_originally_exact_zero=True,old_t_nodes=2181,new_t_nodes=len(A['x']),
        all_original_t_nodes_retained_bitwise=True,original_t_interval=[0.,1.],
        all_five_accepted_pending_arrays_bitwise_equal=True,
        original_complete_warm_H_bitwise_equal=True,
        physical_metric_profile_gauge_length_and_both_charts_unchanged=True,
        tail_configuration_changes=changed,only_new_tail_spectrum_and_IO=True,
        prefix_Newton_calls=0,Node_workers=0,
        old_warm_RMS_not_used_as_new_RMS=True,
        final_physical_acceptance_not_yet_inferred=True)
    del A,B,C,W
    gc.collect()
    return record,plan,fixed,identity


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--attach-completed-only',action='store_true')
    options,remaining=parser.parse_known_args()
    out=argument(remaining,'--out-prefix')
    record,plan,fixed,identity=verify_original_chain(remaining)
    out.parent.mkdir(parents=True,exist_ok=True)
    post.spectral.atomic_new_or_same(out.with_name(out.name+'-original-spectral-chain.json'),record)
    oldargv=sys.argv
    if not options.attach_completed_only:
        try:
            sys.argv=[oldargv[0],*remaining]
            post.main()
        finally:
            sys.argv=oldargv
    primary=out.with_suffix('.json.gz');summary=out.with_name(out.name+'-summary.json')
    data=[read_json(primary),read_json(summary)]
    packet=argument(remaining,'--tail-packet');packet_sha=sha(packet)
    for value in data:
        if (not value.get('solver_success') or value.get('audit_pending',True) or
                not value['config'].get('fixed_metric') or not value['config'].get('actual_nonlinear_tail') or
                value['modes']!=28):
            raise ValueError('The original complete physical postprocessing did not finish')
        bounded=value.get('same_g_M28_bounded_postprocess',{})
        staged=value.get('staged_actual_recovery',{})
        verify=staged.get('verification',{})
        if (bounded.get('entry_sha256')!=POST_SHA or bounded.get('entry_error') is not None or
                bounded.get('live_raw_restores',0)<2 or not bounded.get('complete_H_bitwise_equal') or
                bounded.get('source_packet_sha')!=packet_sha or
                bounded.get('small_actual_C2_comparison',{}).get('complete_physical_quintic_coefficients_bitwise_equal') is not True or
                bounded.get('small_complete_mean_comparison',{}).get('complete_mean_values_bitwise_equal') is not True or
                not staged.get('prefix_accepted') or not verify.get('passed_original_acceptance') or
                staged.get('tail_packet_sha256')!=packet_sha or
                staged.get('numerical_BVP_repeated') is not False):
            raise ValueError('The actual bounded/RMS/inlet/trueBC/mean acceptance chain is incomplete')
        for key in ('frozen_profile','physical_tail_parameters','physical_tail_cut','gauge_amplitude',
                    'meridian_length','angular_chart','chart_reference_coefficients','chart_reference_frequencies'):
            if canonical(value[key])!=canonical(fixed[key]):
                raise ValueError('The completed physical packet changed a fixed datum: '+key)
        for key in ('reference_t','physical_s'):
            if canonical(value['numerical_meridian_chart'][key])!=canonical(fixed['numerical_meridian_chart'][key]):
                raise ValueError('The completed physical packet changed its recorded chart: '+key)
        if equation_config(value['actual_tail']['config'])!=equation_config(read_json(argument(remaining,'--tail-config'))):
            raise ValueError('The completed physical packet changed the full tail problem')
    final_raw_path=local_binding(primary.parent,data[0]['raw_collocation_checkpoint'])
    final_raw,F=raw_arrays(final_raw_path)
    accepted,A=raw_arrays(argument(remaining,'--accepted-raw'))
    if (not final_raw['solver_success'] or canonical(final_raw['identity'])!=canonical(identity) or
            not all(same_array(F[key],A[key]) for key in ('x','y','p','cubic')) or
            float(np.max(F['rms']))>identity['tol']):
        raise ValueError('The completed raw state changed original fields or failed new original RMS')
    for item in data[0]['pp_coefficient_chunks']:
        file=local_binding(primary.parent,item)
        if file.stat().st_size!=item['bytes']:
            raise ValueError('A completed physical coefficient file is incomplete')
    status=dict(entry_sha256=SELF_SHA,execution_mode='staged completion of the original same-g M28 raw',
        original_spectral_entry_sha256=plan['entry_sha256'],plan_file=record['original_plan']['file'],
        plan_sha256=PLAN_SHA,warm_record_file=record['original_warm_verification']['file'],
        warm_record_sha256=WARM_CHECK_SHA,original_spectral_chain=record,
        solver_success=True,audit_pending=False,
        max_rms_collocation_residual=float(np.max(F['rms'])),
        actual_tail_residual=data[0]['actual_tail']['residual'],
        original_math_and_acceptance_preserved=True,MJS_sources_unchanged=True,
        original_g_and_charts_unchanged=True,
        prefix_Newton_calls_in_this_completion=0,Node_workers_in_this_completion=0,
        final_tail_packet_sha256=packet_sha,
        reused_already_audited_packet=True,
        full_tail_audit_recomputed_in_this_metadata_stage=False,
        original_warm_RMS_was_not_new_M_acceptance=True,
        original_successful_M28_Newton_not_repeated=True)
    existing_terminal=out.with_name(out.name+'-sameg-staged-complete.json')
    if existing_terminal.exists():
        done=read_json(existing_terminal)
        if (done.get('entry_sha256')!=SELF_SHA or not done.get('completion_passed') or
                done.get('outputs')!={str(primary):sha(primary),str(summary):sha(summary)} or
                any(canonical(v.get('same_g_spectral_refinement'))!=canonical(status) for v in data)):
            raise ValueError('An existing completion terminal does not bind these exact outputs')
        print(json.dumps(dict(event='same_g_M28_staged_completion_already_verified',
            primary=str(primary),primary_sha256=sha(primary),new_physical_work=False)),flush=True)
        return
    before={str(primary):sha(primary),str(summary):sha(summary)}
    for path,value in zip((primary,summary),data):
        old=value.get('same_g_spectral_refinement')
        if old is not None and canonical(old)!=canonical(status):
            raise ValueError('A different same-g completion record is already present')
        value['same_g_spectral_refinement']=status
        content=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
        if path.suffix=='.gz':content=gzip.compress(content,mtime=0)
        if len(content)>=5_000_000:raise ValueError('Completed metadata exceeds the per-file limit')
        tmp=path.with_name(path.name+'.sameg-completion.tmp-'+str(os.getpid()))
        with tmp.open('xb') as stream:
            stream.write(content);stream.flush();os.fsync(stream.fileno())
        tmp.replace(path)
    terminal=dict(scope=__doc__,entry_sha256=SELF_SHA,completion_passed=True,
        attach_completed_only=bool(options.attach_completed_only),
        original_spectral_chain_sha256=sha(out.with_name(out.name+'-original-spectral-chain.json')),
        completed_raw=dict(file=str(final_raw_path),sha256=sha(final_raw_path)),
        outputs={str(primary):sha(primary),str(summary):sha(summary)},
        output_hashes_before_provenance_attachment=before,
        mathematical_data_modified=False,original_successful_Newton_repeated=False,
        true_full_tail_audit_reused_by_exact_complete_H=True)
    post.spectral.atomic_new_or_same(out.with_name(out.name+'-sameg-staged-complete.json'),terminal)
    print(json.dumps(dict(event='same_g_M28_staged_completion_passed',
        solver_success=True,audit_pending=False,prefix_Newton_calls=0,Node_workers=0,
        primary=str(primary),primary_sha256=sha(primary))),flush=True)


if __name__=='__main__':main()
