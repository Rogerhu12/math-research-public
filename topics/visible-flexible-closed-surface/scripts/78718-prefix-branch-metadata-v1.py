#!/usr/bin/env python3
"""Read-only saved metadata comparison, not a branch uniqueness theorem."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def ident(path):
    p=Path(path).resolve();raw=p.read_bytes()
    return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--checkpoint',type=Path,action='append',required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('Refuse existing report')
    records=[];values=[]
    for path in a.checkpoint:
        r=json.loads(gzip.decompress(path.read_bytes()))
        coeff=[float(r['actual_primary_amplitude'])]+[
            float(x)*float(y) for x,y in zip(r['parameters'][1:],r['central_correction_scales'])]
        if len(coeff)!=r['config']['modes']:raise ValueError('Unexpected support coefficient dimensions')
        values.append((r,coeff))
        records.append({'checkpoint':ident(path),'modes':r['config']['modes'],
            'source_angular':r['config']['angular'],'nodes':r['nodes'],
            'solver_success_saved':r['solver_success'],
            'gauge_amplitude':r['gauge_amplitude'],'actual_support_amplitude':r['actual_primary_amplitude'],
            'support_higher_absolute_sum':sum(abs(x) for x in coeff[1:]),
            'support_higher_absolute_max':max(map(abs,coeff[1:]),default=0.),
            'highest_support_mode':len(coeff),'highest_support_coefficient':coeff[-1],
            'last_three_support_absolute_max':max(map(abs,coeff[-3:])),
            'sampled_metric_saved':r['summary']['metric_l1'],
            'sampled_flow_defect_saved':r['summary']['flow_defect'],
            'sampled_inlet_saved':r['summary']['inlet'],
            'physical_collocation_rms_saved':r['max_rms_collocation_residual']})
    pairs=[]
    fixed=('frozen_profile','chart','warp_reference_q','physical_port_sha256',
           'physical_tail_parameters','physical_tail_cut','gauge_amplitude')
    for k in range(1,len(values)):
        prev,pc=values[k-1];r,rc=values[k];n=min(len(pc),len(rc))
        equal={key:prev[key]==r[key] for key in fixed}
        if not all(equal.values()):raise ValueError('Different frozen material/gauge metadata')
        pairs.append({'left_index':k-1,'right_index':k,'fixed_fields_equal':equal,
            'support_amplitude_difference':rc[0]-pc[0],
            'common_support_coefficient_difference_max':max(abs(rc[j]-pc[j]) for j in range(n)),
            'common_support_coefficient_difference_l1':sum(abs(rc[j]-pc[j]) for j in range(n)),
            'common_higher_support_difference_max':max((abs(rc[j]-pc[j]) for j in range(1,n)),default=0.),
            'new_support_modes':len(rc)-n,
            'new_support_modes_absolute_max':max((abs(x) for x in rc[n:]),default=0.),
            'branch_switch_proved':False,'same_mathematical_branch_proved':False})
    out={'schema':'78718-prefix-saved-branch-metadata-v1','script':ident(__file__),
        'checkpoints':records,'adjacent_comparisons':pairs,
        'solver_calls':0,'RHS_calls':0,'ODE_calls':0,
        'scope':'Saved numerical diagnostics and exact JSON metadata identities only; no new solution or uniqueness/branch certificate.'}
    for row in records:
        if ident(row['checkpoint']['path'])!=row['checkpoint']:raise ValueError('Input changed')
    a.out.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'output':ident(a.out),'modes':[x['modes']for x in records],
        'q':[x['actual_support_amplitude']for x in records],
        'sampled_metric_saved':[x['sampled_metric_saved']for x in records],
        'highest_support_coefficient':[x['highest_support_coefficient']for x in records],
        'all_fixed_fields_equal':True,'solver_calls':0,'RHS_calls':0},sort_keys=True))


if __name__=='__main__':main()
