#!/usr/bin/env python3
"""Compact two completed shifted-root arms against the frozen MP90 reference."""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import mpmath as mp
from record_fixed_actual import load, scalar_tree, sha
from record_tail_initialization import numeric_identity

mp.mp.dps = 140


def identity(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def packed(values):
    return struct.pack('<'+'d'*len(values),*values)


def text(value):
    return mp.nstr(value,32)


def verify_reference(ref):
    if sha(ref['path'])!=ref['sha256']:raise ValueError('A bound file changed: '+ref['path'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('plan','arm-a','arm-b','resource-a','resource-b','log-a','log-b','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('A completed record already exists')
    plan=load(a.plan)
    for key in ('source','base','bridge','capsule','baseline','mp90_reference'):verify_reference(plan[key])
    cs=load(plan['capsule']['path']);capsule=load(cs['coefficients']['path'])
    reference=load(cs['reference']['path']);ms=load(plan['mp90_reference']['path']);precise=load(ms['raw']['path'])
    for ref in (cs['coefficients'],cs['reference'],cs['fixture'],cs['input'],ms['raw']):verify_reference(ref)
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path)!=digest:raise ValueError('An original bound source changed: '+path)
    arms={}
    for label,summary_path,resource_path,log_path,expected_arm in (
        ('A',a.arm_a,a.resource_a,a.log_a,'root-only'),
        ('B',a.arm_b,a.resource_b,a.log_b,'root-and-linear-split')):
        summary,resource=load(summary_path),load(resource_path)
        if resource['status']!='observed_terminal' or resource['child_returncode']!=0:
            raise ValueError('Actual successful terminal required')
        planned=next(item for item in plan['planned_runs']if item['arm']==expected_arm)
        if resource['command']!=planned['child_command']:raise ValueError('Executed command differs from frozen plan')
        if (summary['arm']!=expected_arm or summary['source_sha256']!=plan['source']['sha256'] or
            summary['base_source_sha256']!=plan['base']['sha256'] or summary['bridge_sha256']!=plan['bridge']['sha256']):
            raise ValueError('The mathematical source identity changed')
        for name,key in (('capsule_summary','capsule'),('float_baseline','baseline'),('mp90_summary','mp90_reference')):
            if summary[name]!=plan[key]:raise ValueError('The prior verified reference changed')
        if numeric_identity(summary['root_rules'])!=numeric_identity(capsule['root_rules']):
            raise ValueError('A root rule changed')
        for field in ('full_flow_jacobian_computed','complete_tail_solver_invoked','physical_checkpoint_written','production_source_changed'):
            if summary[field]:raise ValueError('This is only the three-stage arithmetic scope')
        verify_reference(summary['raw']);raw=load(summary['raw']['path'])
        scalar_rows={}
        for fixture,old,high,row,scalar in zip(capsule['fixtures'],reference['rows'],precise['rows'],raw['rows'],summary['named_results'],strict=True):
            if not fixture['stage']==old['stage']==high['stage']==row['stage']==scalar['stage']:
                raise ValueError('Prescribed stage differs')
            initial=next(e for e in row['events']if e['event']=='shifted_root_start')
            if packed(initial['state'])!=packed(fixture['initial42']):raise ValueError('Complete initial42 differs')
            if len(row['state'])!=42 or hashlib.sha256(packed(row['state'])).hexdigest()!=scalar['output42_sha256']:
                raise ValueError('Complete output42 identity differs')
            expected=[mp.mpf(v)for v in high['state']]
            current=[mp.mpf(float(v))for v in row['state']]
            original=[mp.mpf(float(v))for v in old['state']]
            errors=[v-expected[j]for j,v in enumerate(current)]
            old_errors=[v-expected[j]for j,v in enumerate(original)]
            scale=mp.mpf(float(fixture['normalizationScale']));ratio=mp.mpf(float(fixture['portRatio']))
            norms=[abs(errors[j]if j<20 else errors[j]/ratio)/scale for j in range(40)]
            old_norms=[abs(old_errors[j]if j<20 else old_errors[j]/ratio)/scale for j in range(40)]
            checks={
                'maximum_all42_error_to_mp90':text(max(map(abs,errors))),
                'maximum_original_all42_error_to_mp90':text(max(map(abs,old_errors))),
                'maximum_mean2_error_to_mp90':text(max(map(abs,errors[40:]))),
                'maximum_normalized_physical_error_to_mp90':text(max(norms)),
                'maximum_original_normalized_physical_error_to_mp90':text(max(old_norms))}
            for key,value in checks.items():
                if scalar[key]!=value:raise ValueError('Stored MP-reference scalar differs: '+key)
            physical=[v if j<20 else v/fixture['portRatio']for j,v in enumerate(row['state'][:40])]
            residual=[v-fixture['targetNode40'][j]for j,v in enumerate(physical)]
            if packed(residual)!=packed(row['residual']):raise ValueError('Stored physical target residual differs')
            if max(map(abs,residual))/fixture['normalizationScale']!=scalar['fixed_target_normalized_residual']:
                raise ValueError('Stored target norm differs')
            if len(row['root_outcomes'])!=64:raise ValueError('All original RK fields must complete')
            if max(r['err']/r['scale']for r in row['root_outcomes'])!=scalar['max_stable_root_relative_residual']:
                raise ValueError('Stable root report differs')
            if max(r['formedMomentErr']/r['scale']for r in row['root_outcomes'])!=scalar['max_formed_moment_root_relative_residual']:
                raise ValueError('Formed-moment root report differs')
            scalar_rows[str(fixture['stage'])]=dict(**scalar,
                error_to_original_error_ratio=text(max(norms)/max(old_norms)),
                original_initial42_sha256=hashlib.sha256(packed(fixture['initial42'])).hexdigest(),
                complete_two_means_compared=True)
        arms[label]=dict(summary=identity(summary_path),raw=summary['raw'],
            observer=scalar_tree(resource),observer_identity=identity(resource_path),log=identity(log_path),
            actual_command=resource['command'],named_results=scalar_rows)
    rules=dict(capsule['root_rules']);halves=rules.pop('halving_factors')
    rules.update(halving_count=len(halves),halving_factors_float64_sha256=hashlib.sha256(packed(halves)).hexdigest())
    output=dict(
        confidence='Finite arithmetic evidence only.',
        scope='Two separately observed arithmetic arms at the original three fixed stages. A shifts only the root variable/residual; B additionally separates literal-coefficient linear/nonlinear RHS terms. Neither is a production or original-DN acceptance.',
        collector=identity(__file__),collector_helpers={name:sha(Path(__file__).with_name(name))for name in
            ('record_fixed_actual.py','record_tail_initialization.py')},
        frozen_plan=identity(a.plan),frozen_source=plan['source'],base=plan['base'],bridge=plan['bridge'],
        original_capsule=plan['capsule'],exact_float_baseline=plan['baseline'],mp90_reference=plan['mp90_reference'],
        original_source_sha256=cs['source_sha256'],additional_original_root_sources=cs['additional_original_root_sources'],
        unchanged_root_rule_constants=rules,
        stopping_scope='Threshold constants/rules are unchanged. The stable residual ell+quad differs from formed moments-target in binary64; both reports are retained. This is not original floating stopping-path identity.',
        arms=arms,
        conclusion='A lowers the maximum MP-reference flow error in the two high-mode stages and leaves the stage175 dominant error unchanged. B is less accurate than A in both high-mode stages. B stage175 has a much smaller fixed-target residual while its dominant MP-reference error is unchanged; fixed-target residual is not an arithmetic accuracy criterion.',
        full_flow_jacobian_computed=False,complete_tail_solver_invoked=False,production_installed=False,
        rigorous_error_bound=False,continuous_ODE_solved=False,
        data_policy='Only sources, commands, original identities and scalar all42/mean comparisons are published. Full fields/root traces stay scratch-only.')
    encoded=json.dumps(output,ensure_ascii=False,indent=2)+'\n'
    if len(encoded.encode())>=100000:raise ValueError('Compact record exceeds100KB')
    a.out.write_text(encoded);print(json.dumps(dict(bytes=a.out.stat().st_size,sha256=sha(a.out))))


if __name__=='__main__':main()
