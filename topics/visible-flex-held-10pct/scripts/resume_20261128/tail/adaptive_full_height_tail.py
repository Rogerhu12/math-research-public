#!/usr/bin/env python3
"""Try the complete original H from a true all-node tangent predictor.

Every prediction is explicitly unaccepted. Each actual request runs the
unchanged original native/chord worker, full shooting unknowns, root/domain
guards, residual tolerance, and audit. The f=1 request additionally pays the
original complete heightJetJacobian. A mathematical failed request bisects
the amplitude interval; an engineering failure remains an explicit failure.
No accepted precursor request is recomputed.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import json
import math
from pathlib import Path
import subprocess
import sys
import traceback

import numpy as np

from tail_full_state_tangent_predictor import predict, module, ref, sha, load, read_packet


RUNTIME_KEYS = ('chordMaxCorrections','traceFile','initialCheckpoint')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('repo','work','resume-summary','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--workers',type=int,choices=(1,2,3,4),default=2)
    a=p.parse_args()
    repo,work,resume,out=map(lambda x:x.resolve(),(a.repo,a.work,a.resume_summary,a.outdir))
    if repo==work or repo in work.parents or work not in out.parents or work not in resume.parents:
        raise ValueError('All generated fields and true predecessor data stay outside Git')
    out.mkdir(parents=True,exist_ok=False)
    scripts=repo/'topics/visible-flex-held-10pct/scripts'
    public=scripts/'resume_20261126'
    native=scripts/'resume_n4_tail/native_extended'
    helper=module('_adaptive_complete_tail_helpers',public/'continue_original_actual_dn_chord.py')
    gate=module('_adaptive_complete_original_source',public/'material_design_secant_predictor.py')
    state=dict(scope=__doc__,status='checking_true_source_and_resume',stages=[],
        result=dict(accepted=False,original_full_height_returned=False,
                    prefix_coupling_accepted=False,fixed_metric_refinement=False,complete_surface=False))
    tail=None
    def save():
        helper.write(out/'summary.json',state)
    save()
    try:
        old=load(resume)
        for key in ('source_run','raw','physical','baseline_config'):
            if ref(old['input'][key]['path']) != old['input'][key]:
                raise ValueError('True predecessor identity changed: '+key)
        source_run=Path(old['input']['source_run']['path'])
        record,raw=gate.accepted_original(source_run,repo)
        del raw
        M=int(record['modes'])
        baseline_path=Path(old['input']['baseline_config']['path'])
        baseline=load(baseline_path)
        if baseline['modes']!=M or baseline['spacing']!=3 or baseline['quadrature']<=12*M:
            raise ValueError('Retain the complete original finite dimension/quadrature')
        if any(k in baseline for k in RUNTIME_KEYS):
            raise ValueError('Use the clean source-bound physical baseline')
        H=np.asarray(record['raw_return']['candidate_H'],float)
        if H.shape!=(M,) or not np.all(np.isfinite(H)):
            raise ValueError('The actual source omitted its complete H')
        last=[r for r in old.get('stages',[]) if r.get('original_finite_response_passed') is True][-1]
        if int(last['modes'])!=M or int(last['quadrature'])!=int(baseline['quadrature']):
            raise ValueError('Tangent continuation starts only at the accepted complete source dimension')
        base=float(last['factor'])
        if not 0<base<1:
            raise ValueError('Use a genuine intermediate amplitude of the full dimension')
        packet_path=Path(last['packet']['path'])
        manifest_path=Path(last['native_manifest']['path'])
        if ref(packet_path)!=last['packet'] or ref(manifest_path)!=last['native_manifest']:
            raise ValueError('Accepted predecessor packet or native binding changed')
        packet=read_packet(packet_path)
        if packet['request']!=dict(height=(H*base**np.arange(1,M+1)).tolist(),jacobian=False,audit=True):
            raise ValueError('The predecessor is not this actual complete H at its declared amplitude')
        manifest=load(manifest_path)
        helper.verify_references(manifest)
        executable=Path(old['input']['native_executable']['path'])
        if ref(executable)!=old['input']['native_executable']:
            raise ValueError('Original native executable changed')
        if (manifest['native_files']['executable']!=ref(executable)
                or manifest['native_files']['cpp']!=ref(native/'frozen_flow_production.cpp')
                or manifest['native_files']['header']!=ref(native/'frozen_flow.h')):
            raise ValueError('Use the unchanged original native kernel')
        chord=work/'chord-source'
        if Path(manifest['original_source_topic']).resolve()!=chord:
            raise ValueError('Wrong original shared/chord source')
        native_runs=packet_path.parent/'native-runs'
        height_path=out/'height-reference.json'
        helper.write(height_path,dict(scope='Complete actual source H, unchanged; target factor one uses an exact copy',
            candidate_H=H.tolist(),source_run=ref(source_run),raw=old['input']['raw'],
            physical=old['input']['physical']))
        state.update(input=copy.deepcopy(old['input']),resumed_from=dict(summary=ref(resume),
            accepted_packet=ref(packet_path),modes=M,factor=base,accepted_response_recomputed=False),
            source_hashes={str(x.resolve()):sha(x) for x in (
                Path(__file__),Path(__file__).with_name('tail_full_state_tangent_predictor.py'),
                Path(__file__).with_name('export_tail_tangent_scales.mjs'),
                public/'continue_original_actual_dn_chord.py',native/'prepare_recovered_native.py')})
        state['input'].update(height_reference=ref(height_path),height_reference_key='candidate_H',
                              native_workers=a.workers)
        state['stages'].append(dict(last,inherited_from_summary=ref(resume)))
        save()
        env=dict(os.environ,PYTHONUNBUFFERED='1',VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
            VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_PRELOAD','LD_LIBRARY_PATH'):
            env.pop(key,None)
        target_factor,attempt=1.,0
        while base<1:
            attempt+=1
            directory=out/f'attempt-{attempt:03d}'
            directory.mkdir()
            desired=H.copy() if target_factor==1 else H*target_factor**np.arange(1,M+1)
            state.update(status='forming_unaccepted_all_node_tangent_predictor',
                current_attempt=dict(index=attempt,base_factor=base,target_factor=target_factor,
                                     source_accepted_packet=ref(packet_path)))
            save()
            prediction=predict(repo,packet_path,native_runs,desired,directory/'predictor')
            native_source=directory/'native-source'
            next_native_runs=directory/'native-runs'
            prepare=[sys.executable,str(native/'prepare_recovered_native.py'),
                '--source-topic',str(chord),'--dest',str(native_source),
                '--native-cli',str(executable),'--modes',str(M),'--spacing','3',
                '--quadrature',str(baseline['quadrature']),'--steps',str(baseline['steps']),
                '--workers',str(a.workers)]
            with (directory/'prepare.log').open('x') as stream:
                subprocess.run(prepare,cwd=repo,env=env,stdout=stream,stderr=subprocess.STDOUT,check=True)
            next_manifest=native_source/'native-manifest.json'
            installed=load(next_manifest)
            helper.verify_references(installed)
            runtime=copy.deepcopy(baseline)
            runtime.update(chordMaxCorrections=3,traceFile=str(directory/'worker-trace.jsonl'),
                           initialCheckpoint=prediction['predictor']['path'])
            config_path=directory/'tail-settings.json'
            helper.write(config_path,runtime)
            stage_env=dict(env,VISIBLE_FLEX_NATIVE_MANIFEST=str(next_manifest),
                VISIBLE_FLEX_NATIVE_MANIFEST_SHA256=sha(next_manifest),
                VISIBLE_FLEX_NATIVE_RUN_DIR=str(next_native_runs))
            os.environ.update(stage_env)
            client=helper.module('_adaptive_original_client_'+str(attempt),
                                 native_source/'scripts/950f-tail-client-v3.py')
            tail=client.WeightedTailPort(config_path,native_source/'repro/source-root',
                                         directory/'tail',node_heap=2048)
            final=target_factor==1
            request=dict(height=desired.tolist(),jacobian=final,audit=True)
            state['status']='original_full_height_request_running' if final else 'original_bisection_request_running'
            state['current_attempt'].update(predictor_summary=ref(directory/'predictor/summary.json'),
                requested_jacobian=final,requested_audit=True,native_manifest=ref(next_manifest),
                worker_trace=str(directory/'worker-trace.jsonl'))
            save()
            actual=directory/'tail_0001.json.gz'
            failure=None
            try:
                tail.solve(desired,jacobian=final,audit=True)
            except FloatingPointError as error:
                failure=str(error)
            finally:
                tail.close()
                tail=None
            actual_packet=read_packet(actual)
            response=actual_packet['response']
            if actual_packet['request']!=request or actual_packet['config']!=runtime:
                raise ValueError('Saved actual request/config differs')
            for name,expected in actual_packet['source_sha256'].items():
                if sha(native_source/'scripts'/name)!=expected:
                    raise ValueError('Actual worker source changed: '+name)
            row=dict(modes=M,quadrature=baseline['quadrature'],factor=target_factor,
                original_full_height=final,requested_jacobian=final,requested_audit=True,
                packet=ref(actual),native_manifest=ref(next_manifest),
                predictor_summary=ref(directory/'predictor/summary.json'),
                predictor_was_unaccepted=True,converged=response.get('converged'),
                failed=bool(response.get('failed')),residual=helper.diagnostic_json(response.get('residual')))
            if response.get('audit') is not None:
                row['audit']=helper.diagnostic_json(response['audit'])
            if response.get('history'):
                row['last_original_iteration']=helper.diagnostic_json(response['history'][-1])
            if response.get('lastIteration'):
                row['failed_last_original_iteration']=helper.diagnostic_json(response['lastIteration'])
            if failure:
                row['failure_message']=failure[:2400]
            accepted=(response.get('converged') is True and not response.get('failed')
                and math.isfinite(response.get('residual',math.nan))
                and response['residual']<=runtime['solveTolerance']
                and isinstance(response.get('audit'),dict)
                and response['checkpoint']['cutHeight']==desired.tolist())
            if accepted and final:
                J=response.get('heightJetJacobian')
                accepted=(isinstance(J,list) and len(J)==(3*M+2)*M and all(math.isfinite(v) for v in J))
                row.update(full_height_jacobian_count=len(J) if isinstance(J,list) else None,
                           full_height_jacobian_finite=accepted)
            row['original_finite_response_passed']=bool(accepted)
            state['stages'].append(row)
            save()
            print(json.dumps(row),flush=True)
            if accepted:
                base=target_factor
                packet_path,native_runs=actual,next_native_runs
                if final:
                    state['status']='original_complete_height_tail_returned'
                    state['result'].update(accepted=True,original_full_height_returned=True,
                        full_height_record=str(actual),full_height_record_sha256=sha(actual),
                        height_reference=str(height_path),height_reference_sha256=sha(height_path),
                        height_reference_key='candidate_H',source_homotopy=record['core_settings']['homotopy'],
                        lambda_one_reached=record['core_settings']['homotopy']==1)
                    save()
                    return 0
                target_factor=1.
            else:
                if failure is None:
                    raise ValueError('The real response did not supply the required original acceptance data')
                text=str(response.get('failed',''))
                if any(word in text for word in ('EEXIST','engineering','protocol','ENOENT','SIG','stopped')):
                    raise RuntimeError('Engineering failure is not used for amplitude bisection: '+text)
                middle=(base+target_factor)/2
                if not base<middle<target_factor:
                    raise RuntimeError('Amplitude bisection exhausted distinct floating inputs; retain the last genuine acceptance')
                target_factor=middle
                state['status']='original_failed_trial_retained_bisecting'
                save()
    except Exception as error:
        (out/'exception.txt').write_text(traceback.format_exc())
        state.update(status='adaptive_original_tail_entry_failed',error=repr(error),
                     exception_record=ref(out/'exception.txt'))
        save()
        raise
    finally:
        if tail is not None:
            tail.close()


if __name__=='__main__':
    sys.exit(main())
