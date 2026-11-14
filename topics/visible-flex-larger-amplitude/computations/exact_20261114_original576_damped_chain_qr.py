#!/usr/bin/env python3
"""R273 on the original saved576 system, plus actual57 on the same matrix.

Reuse only the frozen dynamic square-root class. Do not invoke its fixed
1372 main or exact context. Both full exact readbacks below target the same
actual28 original576 J/r/scales/cut/far. The actual57 reference is its real
saved577 restriction, never a new initial state or an acceptance claim.
All scientific execution is confined to this public repository Actions.
"""
from __future__ import annotations

import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
import hashlib
import importlib
import json
import math
import multiprocessing
import os
from pathlib import Path
import resource
import struct
import time
import traceback
import gzip

import numpy as np
import scipy


HERE = Path(__file__).resolve().parent
SYSTEM_NAME = 'exact_20261114_original576_damped_system.py'
SYSTEM_SHA = 'c78dfc6a5ef64a9de8bbbc857a927c6cd1078bbfb2281be62be4eb942014b207'
QR_NAME = 'exact_20261114_native_damped_chain_qr.py'
QR_SHA = '9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33'
KERNEL_NAME = 'exact_20261114_native_allrows_dyadic_residual.py'
KERNEL_SHA = '0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f'
SCHEMA = 'complete-native-original576-damped-square-root-direction-v1'
MODEL_SCOPE = 'R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates'
REFERENCE57_RESULT_SHA = 'c6feb54847e96778b076076ba17b4ccd666c2548c72f8c36414b2897d176cdc1'
REFERENCE57_DELTA_SHA = '5b6e7bb4205ce79c6d0f20b63e491def9747e95a3272e8add1712595ea1c4a85'
REFERENCE57_CHECKPOINT_SHA = '691d2b98bbd767c7c524bc9e7d6dd287067a0e9283939401d8b80bf028d72d84'
REFERENCE57_BINDING_SHA = '32cb5a0b92ab4ce642b65c0b75ba010ff26dcab5cbf77b1b847b5b469ea5279f'
REFERENCE57_MANIFEST_SHA = '8a77b6b6365562ae3d41b3ff4832576f0bd880f41f2b5ed0a8fdefa86a650401'
REFERENCE57_MATRIX_SHA = '76f30d775c0255dd127b08fa279e59fcaaa4a79a50b72bc7adc8231e436f6999'
_KERNEL = None


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('Original576 R273 work belongs only to this public repository Actions')


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def load_pinned(name, digest):
    path = HERE/name
    if file_sha(path) != digest:
        raise ValueError('Frozen source changed: '+name)
    module = importlib.import_module(path.stem)
    if Path(module.__file__).resolve() != path:
        raise ValueError('Unexpected frozen import: '+name)
    return module


def kernel():
    global _KERNEL
    if _KERNEL is None:
        _KERNEL = load_pinned(KERNEL_NAME,KERNEL_SHA)
    return _KERNEL


def exact_stage_job(task):
    return kernel().stage_job(task)


def checked_file(B, directory, descriptor):
    path = B.safe_file(directory,descriptor['file'])
    B.same(path.stat().st_size,descriptor['bytes'],'selected actual57 file size')
    B.same(file_sha(path),descriptor['sha256'],'selected actual57 file SHA')
    return path


def reference57(B, directory, expected_result_sha, system, output):
    """Read precisely five saved files, with no factor/1373-state recompute."""
    directory = Path(directory).resolve()
    B.same(expected_result_sha,REFERENCE57_RESULT_SHA,'completed actual57 result pin')
    path = B.safe_file(directory,'result.json.gz')
    B.same(file_sha(path),REFERENCE57_RESULT_SHA,'actual57 complete result bytes')
    r = B.read(path)
    B.same(r['schema'],'complete-native-direct-LD-J1372-damped-square-root-direction-v1',
           'actual57 producer schema')
    B.same(r['source_sha256'],QR_SHA,'actual57 original producer source')
    B.same(r['new_matrix_identity_sha256'],REFERENCE57_MATRIX_SHA,'actual57 original1372 target identity')
    B.same(r['diagnostic_completed'],True,'actual57 complete diagnostic')
    B.same(r['linear_direction_computed'],True,'actual57 actual saved direction')
    B.same(r['native_accepted'],False,'actual57 direction result is not native acceptance')
    B.same(r['eta_binary64']['float64le_hex'],'000000000000f03f','actual57 explicit eta1 bits')
    frozen = {'input_binding':REFERENCE57_BINDING_SHA,'array_manifest':REFERENCE57_MANIFEST_SHA,
        'restricted_direction_checkpoint':REFERENCE57_CHECKPOINT_SHA,
        'restricted_old_node_delta':REFERENCE57_DELTA_SHA}
    paths = {}
    for key,digest in frozen.items():
        desc = r[key]
        B.same(desc['sha256'],digest,'actual57 selected descriptor '+key)
        paths[key] = checked_file(B,directory,desc)
    binding = B.read(paths['input_binding'])
    B.same(binding['new_matrix_identity_sha256'],REFERENCE57_MATRIX_SHA,'actual57 complete input binding')
    B.same(binding['original1372_input_binding']['original_capture_binding'],system.original.binding,
           'actual57 and current direction use exactly the same original actual28 capture')
    manifest = B.read(paths['array_manifest'])
    B.same(manifest['schema'],'complete-native-damped-chain-direction-arrays-v1','actual57 full descriptor schema')
    B.same(manifest['source_sha256'],QR_SHA,'actual57 descriptor producer')
    B.same(manifest['new_matrix_identity_sha256'],REFERENCE57_MATRIX_SHA,'actual57 descriptor target')
    matches = [d for d in manifest['arrays'] if d['name'] == r['restricted_old_node_delta']['name']]
    B.same(matches,[r['restricted_old_node_delta']],'actual57 selected array alias is complete descriptor')
    desc = r['restricted_old_node_delta']
    B.same((desc['shape'],desc['dtype'],desc['order']),([577,224],'<f8','C'),'actual57 complete original-node direction')
    raw = paths['restricted_old_node_delta'].read_bytes()
    B.same(len(raw),577*224*8,'every actual57 original-node direction word')
    delta = np.frombuffer(raw,dtype='<f8').reshape(577,224)
    if not np.isfinite(delta).all():
        raise ValueError('The actual57 reference direction contains a nonfinite word')
    cp = B.read(paths['restricted_direction_checkpoint'])
    B.same(cp['schema'],'complete-original-node-restriction-of-damped-chain-direction-v1',
           'actual57 restriction checkpoint schema')
    B.same(cp['source_sha256'],QR_SHA,'actual57 checkpoint source')
    B.same(cp['input_binding'],binding,'actual57 full checkpoint binding')
    B.same((cp['M'],cp['K'],cp['depth'],cp['original_depth'],cp['step_depth']),
           (112,224,576,576,1372),'actual57 source/reference depths remain distinct')
    B.same(cp['old_to_new'],binding['old_to_new'],'actual57 original restriction map')
    B.same(cp['restricted_to_original_nodes'],True,'actual57 raw is already the saved restriction')
    B.same(cp['delta_float64le_sha256'],REFERENCE57_DELTA_SHA,'actual57 checkpoint all direction bytes')
    B.same(cp['eta_binary64'],r['eta_binary64'],'actual57 checkpoint eta')
    B.same(cp['model_scope'],MODEL_SCOPE,'actual57 checkpoint model scope')
    B.same(len(cp['rows']),577,'all actual57 checkpoint rows')
    recovered = np.empty((577,224),dtype='<f8')
    for n,item in enumerate(cp['rows']):
        B.same(item['node'],n,'actual57 checkpoint row order')
        B.same(len(item['state']),224,'all actual57 checkpoint state columns')
        recovered[n] = np.asarray(item['state'],dtype='<f8')
        columns = item['negative_zero_columns']
        B.same(columns,sorted(set(columns)),'actual57 explicit zero-sign column list')
        for j in columns:
            if type(j) is not int or not 0 <= j < 224 or recovered[n,j] != 0:
                raise ValueError('Only actual zero signs can be restored in the reference checkpoint')
            recovered[n,j] = -0.0
    B.same(B.float_bytes(recovered),raw,'all actual57 checkpoint/raw words including signed zero')
    exported = output.save('reference57-original-node-delta',delta,
        'Unchanged saved actual57 original577-node restriction; read back here on the original576 matrix')
    B.same(exported['sha256'],REFERENCE57_DELTA_SHA,'actual57 reference export byte identity')
    receipt = dict(schema='actual57-original-node-direction-reference-binding-v1',
        result=dict(file='result.json.gz',bytes=path.stat().st_size,sha256=REFERENCE57_RESULT_SHA),
        selected_files={key:r[key] for key in frozen},
        source_schema=r['schema'],source_sha256=QR_SHA,source_matrix_identity_sha256=REFERENCE57_MATRIX_SHA,
        source_complete1373_delta_sha256=r['step_delta']['sha256'],
        actual_restricted577_delta_sha256=REFERENCE57_DELTA_SHA,source_eta_binary64=r['eta_binary64'],
        current_original576_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
        same_original_actual28_capture_binding=True,source_reference_direction_bytes_unchanged=True,
        current_exact_readback_is_on_the_original576_target_not_the_source1372_target=True,
        source_full1373_direction_not_reloaded=True,source_factors_not_reloaded=True,
        this_does_not_reaudit_the_original1373_to577_restriction_operation=True,
        reference_is_not_a_new_candidate_or_new_native_state=True,exported_reference_array=exported)
    return delta,receipt


def full_exact_comparison(S, system, directions, provenance, output, workers, producer_sha):
    """Two complete exact readbacks share original J decoding, not results."""
    require_actions()
    B=system.B;E=kernel();C=S.Original576ExactContext(system,E)
    M,K,D=system.M,system.K,system.depth
    labels=tuple(directions)
    B.same(labels,('current_damped','reference57'),'two explicit independent readback directions')
    inputs={name:system.raw(name) for name in ('stage-residuals','cut-residual','end-residual',
                                              'original-scales','original-far-graph')}
    raw={name:B.float_bytes(value) for name,value in directions.items()}
    digests={name:hashlib.sha256(value).hexdigest() for name,value in raw.items()}
    decoded={name:E.decoded_array(value,(D+1)*K,'complete original576 '+name) for name,value in raw.items()}
    residuals=E.decoded_array(inputs['stage-residuals'],D*K,'all original576 stage residuals')
    cut=E.decoded_array(inputs['cut-residual'],M,'all original576 cut residuals')
    far=E.decoded_array(inputs['end-residual'],M,'all original576 far residuals')
    graph=E.decoded_array(inputs['original-far-graph'],M,'complete original576 far graph')
    sigma_words=[item[0] for item in struct.iter_unpack('<Q',inputs['original-scales'])]
    state={name:dict(rows=0,products=0,worst=None,maxima=[]) for name in labels}
    base_worst=None
    files={name:output.directory/('large-arrays/'+name+'-original576-all-exact-rows.jsonl.gz') for name in labels}
    handles={};ledgers={};pool=None;stages=0
    started=time.monotonic()

    def consume(kind,node,data,jhash=None):
        nonlocal base_worst
        count=K if kind=='stage' else M
        value,row=data['base_maximum']
        base=C.max_record(kind,node,row,value,sigma_words[node])
        if E.better(base,base_worst):
            base_worst=base
        for label in labels:
            result=data['directions'][label]
            B.same(len(result['rows']),count,'all exact rows in original576 block')
            record=C.max_record(kind,node,result['maximum_row'],result['maximum_integer'],sigma_words[node])
            entry=state[label]
            if E.better(record,entry['worst']):
                entry['worst']=record
            public=E.public_record(record)
            entry['maxima'].append(public)
            ledgers[label].write(E.json_bytes(dict(kind=kind,node=node,
                first_global_equation_row=C.row_order(kind,node,0),
                all_exact_unscaled_rows=result['rows'],original_J_stage_sha256=jhash,
                exact_original_sigma_maximum=public,direction_label=label,
                direction_float64le_sha256=digests[label],
                new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'])))
            entry['rows']+=count
            entry['products']+=result['original_product_positions']

    def tasks():
        for n,J in system.stage_bytes():
            yield dict(stage=n,J=J,residuals=residuals[n*K:(n+1)*K],directions={name:(
                decoded[name][n*K:(n+1)*K],decoded[name][(n+1)*K:(n+2)*K]) for name in labels})

    def take(result):
        nonlocal stages
        B.same(result['stage'],stages,'complete original576 exact stage order')
        consume('stage',stages,result,result['J_stage_raw_sha256'])
        stages+=1
        if stages%32==0 or stages==D:
            print(json.dumps(dict(event='original576_exact_two_directions',completed_stages=stages,
                expected_stages=D,labels=list(labels),elapsed_seconds=time.monotonic()-started)),flush=True)

    try:
        for name,path in files.items():
            handles[name]=path.open('xb')
            ledgers[name]=gzip.GzipFile(fileobj=handles[name],mode='wb',mtime=0)
        consume('cut',0,E.boundary_job('cut',cut,{name:decoded[name][:K] for name in labels},graph))
        if workers==1:
            for task in tasks():
                take(E.stage_job(task))
        else:
            pool=ProcessPoolExecutor(max_workers=workers,mp_context=multiprocessing.get_context('spawn'))
            queue=deque();source=iter(tasks())
            for _ in range(2*workers):
                task=next(source,None)
                if task is None:break
                queue.append(pool.submit(exact_stage_job,task))
            while queue:
                take(queue.popleft().result())
                task=next(source,None)
                if task is not None:queue.append(pool.submit(exact_stage_job,task))
            pool.shutdown(wait=True);pool=None
        consume('far',D,E.boundary_job('far',far,{name:decoded[name][D*K:(D+1)*K] for name in labels},graph))
        B.same(stages,D,'every original576 stage in both exact readbacks')
        for name in labels:
            B.same(state[name]['rows'],(D+1)*K,'complete original576 exact row count')
            B.same(state[name]['products'],D*K*K+M,'complete original576 product positions')
    finally:
        if pool is not None:pool.shutdown(wait=True,cancel_futures=True)
        for ledger in ledgers.values():ledger.close()
        for handle in handles.values():handle.close()
    result={}
    for name in labels:
        entry=state[name];path=files[name]
        descriptor=dict(name=name+'-original576-all-exact-rows',file=path.relative_to(output.directory).as_posix(),
            dtype='exact-dyadic-jsonl-gzip',shape=[entry['rows']],bytes=path.stat().st_size,sha256=file_sha(path),
            role='Every original576 unscaled cut/stage/far residual, then exact division by original sigma; no eta rows')
        output.entries.append(descriptor)
        maximum=E.public_record(entry['worst'])
        witness=B.write(output.directory/(name+'-original576-worst-witness.json'),dict(
            source_sha256=producer_sha,kernel_sha256=KERNEL_SHA,
            new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],direction_label=name,
            direction_float64le_sha256=digests[name],exact_original_sigma_maximum=maximum,
            operands=C.worst_witness(entry['worst'],raw[name],inputs),
            saved_finite_arrays_only=True,exact_nonlinear_derivative_not_claimed=True))
        detail=dict(schema='original576-complete-exact-direction-readback-v1',
            source_sha256=producer_sha,system_source_sha256=SYSTEM_SHA,kernel_sha256=KERNEL_SHA,
            matrix_scope=S.MATRIX_SCOPE,new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            direction_label=name,direction_float64le_sha256=digests[name],direction_provenance=provenance[name],
            exact_rows=entry['rows'],completed_stages=stages,original_product_positions=entry['products'],
            exact_global_original_sigma_norm=maximum,exact_stored_base_sigma_norm=E.public_record(base_worst),
            typed_block_maxima=entry['maxima'],all_exact_residual_rows=descriptor,worst_witness=witness,
            eta_not_in_original_equations=True,readback_uses_unscaled_J_and_r_before_exact_sigma_division=True,
            no_float_refinement_RHS_formed=True,used_as_new_nonlinear_acceptance_gate=False,
            native_accepted=False,elapsed_seconds_for_shared_two_direction_pass=time.monotonic()-started)
        full=B.write(output.directory/(name+'-original576-exact-readback.json.gz'),detail,compressed=True)
        result[name]=dict(full_report=full,direction_label=name,direction_float64le_sha256=digests[name],
            exact_global_original_sigma_norm=maximum,exact_stored_base_sigma_norm=detail['exact_stored_base_sigma_norm'],
            exact_rows=entry['rows'],completed_stages=stages,original_product_positions=entry['products'],
            all_exact_residual_rows=descriptor,worst_witness=witness,
            used_as_new_nonlinear_acceptance_gate=False,no_float_refinement_RHS_formed=True)
    return result


def checkpoint(B, output, system, delta, eta, producer_sha):
    rows=[dict(node=n,state=row.tolist(),
        negative_zero_columns=np.flatnonzero((row==0)&np.signbit(row)).tolist()) for n,row in enumerate(delta)]
    return B.write(output.directory/'native-direction-checkpoint.json.gz',dict(
        schema='complete-native-original576-damped-direction-v1',source_sha256=producer_sha,
        system_source_sha256=SYSTEM_SHA,factor_engine_source_sha256=QR_SHA,
        input_binding=system.binding,M=system.M,K=system.K,depth=system.depth,
        original_depth=system.depth,old_to_new=system.old_to_new,
        eta_binary64=B.scalar(eta),model_scope=MODEL_SCOPE,
        delta_float64le_sha256=hashlib.sha256(B.float_bytes(delta)).hexdigest(),rows=rows,
        original576_full_direction=True,not_a_restriction_of_a1372_direction=True,
        complete_damped_direction_not_an_exact_Newton_claim=True,
        original_cut_and_far_direction_components_not_projected_or_zeroed=True,
        original_nonlinear_readback_required=True,no_nonlinear_trial=True,
        native_accepted=False,task_completed=False),compressed=True)


def small_summary(report, full_result):
    keys=('source_sha256','system_source_sha256','factor_engine_source_sha256','kernel_source_sha256',
        'eta_cli_text','eta_binary64','diagnostic_completed','linear_direction_computed',
        'new_matrix_identity_sha256','input_binding','reference57_binding','factor_report','factor_summary',
        'factor_index','formed_stage_inventory','formed_model_diagnostic','native_delta',
        'native_direction_checkpoint','original_exact_readback','reference57_original576_exact_readback',
        'array_manifest','actual_error','elapsed_seconds','maximum_RSS_kib')
    result={key:report[key] for key in keys if key in report}
    result.update(schema='native-original576-damped-chain-small-summary-v1',full_result=full_result,
        native_accepted=False,task_completed=False,
        same_original576_target_for_both_exact_directions=True,
        no_linear_norm_threshold_is_a_native_trial_gate=True,
        L2_model_descent_does_not_imply_original_infinity_descent=True)
    if len((json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n').encode())>=95000:
        result={key:report[key] for key in ('diagnostic_completed','linear_direction_computed',
            'new_matrix_identity_sha256','actual_error','elapsed_seconds') if key in report}
        result.update(schema='native-original576-damped-chain-small-summary-v1',full_result=full_result,
            compact_transport_fallback=True,native_accepted=False,task_completed=False)
    return result


def main():
    require_actions()
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--capture-directory',type=Path,required=True)
    p.add_argument('--reference57-directory',type=Path,required=True)
    p.add_argument('--reference57-result-sha256',required=True)
    p.add_argument('--eta',required=True)
    p.add_argument('--factor-budget-seconds',type=float,default=None)
    p.add_argument('--max-factor-bytes',type=int,default=2*1024**3)
    p.add_argument('--exact-workers',type=int,default=2)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    eta=float(a.eta)
    if not math.isfinite(eta) or eta<=0:
        raise ValueError('Eta is an explicit positive finite model parameter, not a native tolerance')
    if a.factor_budget_seconds is not None and (not math.isfinite(a.factor_budget_seconds) or a.factor_budget_seconds<=0):
        raise ValueError('An optional factor budget must be finite and positive')
    if a.max_factor_bytes<=0 or not 1<=a.exact_workers<=4:
        raise ValueError('Keep a positive complete-factor storage budget and one to four exact workers')
    out=a.out.resolve()
    if os.path.lexists(a.out) or any(out.is_relative_to(x.resolve()) for x in
            (a.capture_directory,a.reference57_directory)):
        raise ValueError('Use one new independent output directory')
    out.mkdir(parents=True)
    started=time.monotonic();producer_sha=file_sha(__file__)
    S=load_pinned(SYSTEM_NAME,SYSTEM_SHA);Q=load_pinned(QR_NAME,QR_SHA);B=S.load_binding()
    output=B.OutputArrays(out);factor=None
    report=dict(schema=SCHEMA,source_sha256=producer_sha,system_source_sha256=SYSTEM_SHA,
        factor_engine_source_sha256=QR_SHA,kernel_source_sha256=KERNEL_SHA,
        eta_cli_text=a.eta,eta_binary64=B.scalar(eta),model_scope=MODEL_SCOPE,
        original_native_calls=0,new_RHS_calls=0,new_J_calls=0,new_ODE_steps=0,nonlinear_trials=0,
        diagnostic_completed=False,linear_direction_computed=False,native_accepted=False,task_completed=False,
        target_is_complete_original576_saved_matrix=True,
        original_cut_H_far_and_sigma_not_changed=True,
        no_normal_matrix_Riccati_inverse_rank_truncation_or_extra_ridge=True,
        damping_is_not_a_new_final_equation_or_acceptance_tolerance=True,
        exact_linear_defect_not_used_as_new_native_trial_gate=True,
        reference57_source1372_defect_not_claimed_to_apply_to_original576=True,
        factor_budget_seconds=a.factor_budget_seconds,maximum_factor_bytes=a.max_factor_bytes,
        exact_workers=a.exact_workers,NumPy=np.__version__,SciPy=scipy.__version__,
        BLAS_threads={key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')})
    try:
        system=S.Original576System(a.capture_directory,B)
        report['new_matrix_identity_sha256']=system.binding['new_matrix_identity_sha256']
        report['input_binding']=B.write(out/'input-binding.json.gz',system.binding,compressed=True)
        report['original_arrays']=system.export_inputs(output)
        reference,reference_binding=reference57(B,a.reference57_directory,a.reference57_result_sha256,system,output)
        report['reference57_binding']=B.write(out/'reference57-binding.json',reference_binding)
        deadline=None if a.factor_budget_seconds is None else time.monotonic()+a.factor_budget_seconds
        factor=Q.NativeDampedChainQR(system,eta,a.eta,output,deadline,a.max_factor_bytes)
        factor.factorize()
        report['factor_index']=B.write(out/'factor-index.json.gz',dict(
            source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
            new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            factors=factor.factors,complete=True),compressed=True)
        report['formed_stage_inventory']=B.write(out/'formed-stage-inventory.json.gz',dict(
            source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
            new_matrix_identity_sha256=system.binding['new_matrix_identity_sha256'],
            formed_model_identity_sha256=factor.report['formed_model_identity_sha256'],
            stages=factor.formed_stage_rows),compressed=True)
        z,delta=factor.solve()
        report['linear_direction_computed']=True
        report['native_delta']=factor.report['solve']['delta']
        report['native_direction_checkpoint']=checkpoint(B,output,system,delta,eta,producer_sha)
        comparisons=full_exact_comparison(S,system,dict(current_damped=delta,reference57=reference),
            dict(current_damped=dict(source_sha256=producer_sha,eta_binary64=B.scalar(eta),
                 direction_array=report['native_delta']),reference57=reference_binding),output,a.exact_workers,producer_sha)
        report['original_exact_readback']=comparisons['current_damped']
        report['reference57_original576_exact_readback']=comparisons['reference57']
        report['formed_model_diagnostic']=factor.model_readback(z)
        report['diagnostic_completed']=True
    except Exception as error:
        report['actual_error']=repr(error)
        report['actual_traceback']=traceback.format_exc()
    finally:
        if factor is not None:
            factor.report.update(qr_calls=factor.qr_calls,formation_calls=factor.formation_calls,
                formation_underflow_to_binary64_zero=factor.formation_underflow,
                elapsed_seconds=time.monotonic()-factor.started,
                maximum_RSS_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            report['factor_summary']={key:factor.report[key] for key in (
                'complete','rows','columns','augmented_rows','stage_count','node_count','block_width',
                'node_penalty_blocks','qr_calls','formation_calls','formation_underflow_to_binary64_zero',
                'pure_constant_rows','actual_factor_and_constant_bytes','formed_model_identity_sha256',
                'pure_constant_energy_longdouble','minimum_absolute_triangular_diagonal',
                'expected_factor_and_constant_bytes','maximum_declared_factor_bytes','working_precision',
                'elapsed_seconds','maximum_RSS_kib') if key in factor.report}
            report['factor_report']=B.write(out/'factor-report.json.gz',factor.report,compressed=True)
            if 'factor_index' not in report:
                report['factor_index']=B.write(out/'partial-factor-index.json.gz',dict(
                    source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
                    complete=False,factors=factor.factors,partial_factors_not_a_complete_direction=True),compressed=True)
            if 'formed_stage_inventory' not in report:
                report['formed_stage_inventory']=B.write(out/'partial-formed-stage-inventory.json.gz',dict(
                    source_sha256=producer_sha,factor_engine_source_sha256=QR_SHA,
                    complete=False,stages=factor.formed_stage_rows),compressed=True)
        report['array_manifest']=B.write(out/'output-array-manifest.json.gz',dict(
            schema='complete-native-original576-damped-direction-arrays-v1',source_sha256=producer_sha,
            factor_engine_source_sha256=QR_SHA,new_matrix_identity_sha256=report.get('new_matrix_identity_sha256'),
            arrays=output.entries,all_arrays_artifact_only=True,native_accepted=False),compressed=True)
        report['elapsed_seconds']=time.monotonic()-started
        report['maximum_RSS_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        full=B.write(out/'result.json.gz',report,compressed=True)
        B.write(out/'summary.json',small_summary(report,full))
    print(json.dumps(dict(event='original576_damped_chain_finished',diagnostic_completed=report['diagnostic_completed'],
        linear_direction_computed=report['linear_direction_computed'],native_accepted=False)),flush=True)
    return 0 if report['diagnostic_completed'] else 2


if __name__=='__main__':
    raise SystemExit(main())
