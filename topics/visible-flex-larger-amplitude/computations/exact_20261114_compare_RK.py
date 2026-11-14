#!/usr/bin/env python3
"""Compare completed same-g/full-H tail solves at two RK step counts.

This records actual cut DN jets, its requested Jacobian, complete canonical
states and finite audits. A separately accepted prefix is not inferred.
"""
import argparse
import json
from pathlib import Path
import struct
import numpy as np
from exact_20261114_compare_depth import read,sha,compare


def main():
    source_hash=sha(__file__)
    helper_hash=sha(Path(__file__).with_name('exact_20261114_compare_depth.py'))
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('topic','new-dir','out'):p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args();notes=a.topic/'notes';stem='2026-11-13-strong-q126-m32-tail2-actual-r1'
    old_path=notes/(stem+'-tail-response_0003.json.gz');old_ready_path=notes/(stem+'-accepted-ready-extracted.json')
    packet=read(old_path);old=packet['response'];new=read(a.new_dir/'response.json.gz')
    config=read(a.new_dir/'config.json');run=read(a.new_dir/'result.json');ready=read(a.new_dir/'ready.json.gz')
    if not run.get('success')or run.get('actual_exit_code')!=0 or not old['converged']or not new['converged']:
        raise ValueError('Both solves must have actually converged and exited')
    if new['checkpoint']['cutHeight']!=packet['request']['height']or not new['residual']<config['solveTolerance']:
        raise ValueError('Complete H or tolerance differs')
    ignored={'steps','auditSteps','initialCheckpoint','traceFile','iterationCheckpointFile','trialDiagnosticFile'}
    project=lambda q:{k:v for k,v in q.items()if k not in ignored}
    if project(config)!=project(packet['config'])or project(new['checkpoint']['parameters'])!=project(old['checkpoint']['parameters']):
        raise ValueError('A setting other than RK steps and I/O differs')
    former=read(old_ready_path)['storedMetricAdapter'];current=ready['storedMetricAdapter']
    keys=['sourceRevision','frozenWarpAlpha','cellCount','profileFingerprintBefore','profileFingerprintAfter']
    if any(former[k]!=current[k]for k in keys)or project(former['physicalParameters'])!=project(current['physicalParameters']):
        raise ValueError('Stored source geometry differs')
    geometry=['radius','backgroundSlope','backgroundSecond','E','Ep']
    if any(struct.pack('<d',old['jets'][k])!=struct.pack('<d',new['jets'][k])for k in geometry):
        raise ValueError('Cut geometry differs')
    M=config['modes'];oldJ=np.asarray(old['heightJetJacobian']).reshape(3*M+2,M);newJ=np.asarray(new['heightJetJacobian']).reshape(3*M+2,M)
    blocks={'slope':slice(0,M),'second':slice(M,2*M),'meanSlopeCorrection':slice(2*M,2*M+1),
            'meanSecondCorrection':slice(2*M+1,2*M+2),'height':slice(2*M+2,3*M+2)}
    jac={name:compare(oldJ[sl],newJ[sl])for name,sl in blocks.items()}
    for row in jac.values():row['relative_to_old_block_linf']=row['max_absolute_difference']/max(row['old_max_absolute'],np.finfo(float).tiny)
    old_states=np.asarray(old['checkpoint']['states']);new_states=np.asarray(new['checkpoint']['states'])
    states=compare(old_states,new_states)
    scale=np.maximum(np.max(abs(old_states),axis=1),np.finfo(float).tiny)
    states['maximum_row_relative_difference']=float(np.max(np.max(abs(new_states-old_states),axis=1)/scale))
    jets={key:compare(old['jets'][key],new['jets'][key])for key in ('height','slope','second')}
    means={key:compare([old['jets'][key]],[new['jets'][key]])for key in ('meanSlope','meanSecond','meanSlopeCorrection','meanSecondCorrection')}
    files=[old_path,old_ready_path,a.new_dir/'response.json.gz',a.new_dir/'result.json',a.new_dir/'config.json',a.new_dir/'ready.json.gz']
    result=dict(schema='actual-same-H-RK-refinement-comparison-v1',finished=True,
        source_sha256_at_start=source_hash,comparison_helper_sha256_at_start=helper_hash,
        input_sha256={str(q):sha(q)for q in files},old_steps=packet['config']['steps'],new_steps=config['steps'],
        physical_depth=config['depth'],shooting_nodes=len(old_states),modes=M,quadrature=config['quadrature'],
        complete_H_exactly_equal=True,all_parameters_except_RK_and_IO_equal=True,
        same_stored_metric_factory_fields={k:current[k]for k in keys},exact_cut_geometry={k:old['jets'][k]for k in geometry},
        residuals=[old['residual'],new['residual']],original_tolerance=config['solveTolerance'],
        histories=[old['history'],new['history']],audits=[old['audit'],new['audit']],
        physical_cut_jets=jets,physical_cut_mean_jets=means,DN_Jacobian_blocks=jac,
        Jacobian_rows=['slope[M]','second[M]','meanSlopeCorrection','meanSecondCorrection','height[M]'],
        Jacobian_columns='Complete physical cut height coefficients H[0:M]',
        Jacobian_methods=[old.get('heightJetJacobianMethod'),new.get('heightJetJacobianMethod')],
        complete_canonical_states=states,accepted_prefix_resolved=False,
        limitations=['Two finite RK solves do not certify an infinite nonlinear solution or an interval error bound.',
            'Original symmetric-difference second/mean-second/height DN rows remain numerical; actual analytic slope and mean-slope rows are retained.',
            'The original prefix is not re-solved or accepted using the refined DN operator.'])
    with a.out.open('x')as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
    print(json.dumps(dict(output=str(a.out),steps=[result['old_steps'],result['new_steps']],
        residuals=result['residuals'],slope_difference=jets['slope']['max_absolute_difference'],
        second_difference=jets['second']['max_absolute_difference'],state_difference=states['max_absolute_difference'])),flush=True)


if __name__=='__main__':main()
