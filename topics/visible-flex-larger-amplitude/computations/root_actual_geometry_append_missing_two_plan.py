#!/usr/bin/env python3
"""Append only four real missing-control fields to the frozen q122 M28 plan.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The baseline and twelve completed fields retain their exact original command,
source and metadata identities. The new lambda/vd directions consume the real
supplemental columns and explicitly corrected provider anchor. This is a
finite design plan at the old M28 baseline, not a fine32 response or new BVP.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PLAN_SHA='240b5d5bd2bd51019296bab9c8eaa28d30de04e195cc2273a38c2d8c61cefab3'
SIX_SHA='2e848e2b59507a4bec44546a4916fb54e461b59713c0b37a968313669dc97f30'
EIGHT_SHA='5c83df392bb2e9ed75b767e0ed90fc85bfb83ae545945acb4177d200891937c0'
ANCHOR_SHA='583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('plan','inventory','response','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh appended plan required')
    plan,inventory,eight=map(read,(a.plan,a.inventory,a.response))
    if sha(a.plan)!=PLAN_SHA or sha(a.response)!=EIGHT_SHA:
        raise ValueError('Require the immutable completed-six plan and actually assembled eight response')
    if (not inventory['all_gates'] or inventory['total_fields']!=13 or
            inventory['input_sha256'].get(str(a.plan))!=PLAN_SHA):
        raise ValueError('The actual complete thirteen-field inventory is required')
    if (not eight['finished'] or eight['new_solution'] or eight['modes']!=28 or
            not eight['partial_recovery'] or
            not eight['all_eight_external_full_and_half_gates_observed'] or
            eight['all_eight_combined_half_vectors_available'] or
            eight['complete_eight_combined_half_gate_claimed'] or
            not eight['prior_six_combined_rows_and_arrays_reused_unchanged'] or
            eight['original_six_external_fields_recomputed'] or
            eight['corrected_anchor_sha256']!=ANCHOR_SHA):
        raise ValueError('The genuine partial-recovery limitations and new two columns must remain explicit')
    first=plan['candidates'][1]['command']
    six_path=Path(first[first.index('--response-data')+1]);six=read(six_path)
    if sha(six_path)!=SIX_SHA or eight['baseline']!=six['baseline']:
        raise ValueError('The same actual baseline and original six response are required')
    if eight['prescribed_low_core_responses']!=six['prescribed_low_core_responses']:
        raise ValueError('An old prescribed response was changed')
    oldrows=six['additional_core_held_directions'];newrows=eight['additional_core_held_directions']
    if newrows[:len(oldrows)]!=oldrows or len(newrows)!=len(oldrows)+2:
        raise ValueError('An old neutral row changed or a missing response is absent')
    rows={r['external_field']:r for r in newrows}
    if set(rows)-{r['external_field'] for r in oldrows}!={'initial_speed_frontload','vd'}:
        raise ValueError('Only the two actual supplemental controls may be appended')
    for original,observed in zip(plan['candidates'],inventory['fields']):
        if original['name']!=observed['name']:
            raise ValueError('The completed original field order changed')
        for k in ('report','resource','field'):
            if sha(original[k])!=observed[k+'_sha256']:
                raise ValueError('An original completed field metadata changed')
    for path,h in plan['source_and_input_sha256'].items():
        if sha(path)!=h:raise ValueError('An original source/input changed: '+path)
    wrapper=HERE/'root_actual_geometry_field_anchor.py'
    from strong_frontload_anchor_loader_adapter import build
    ns,provenance=build('geometry',wrapper)
    unused,unused_main,prepared=ns['prepare_entry']()
    if prepared['frontload_anchor_adapter']['current_anchor_hook_sha256']!=ANCHOR_SHA:
        raise ValueError('The actual geometry loader did not install the corrected anchor')
    original=plan['candidates'][0]['command'];base=original[original.index('--')+1:]
    if base[1]!=plan['geometry_wrapper']:raise ValueError('Original geometry command differs')
    base=base[:base.index('--out-prefix')];base[1]=str(wrapper)
    result=copy.deepcopy(plan);result['scope']=__doc__
    result['assembled_response_file']=str(a.response)
    result['assembled_response_sha256']=EIGHT_SHA
    result['original_plan']=str(a.plan);result['original_plan_sha256']=PLAN_SHA
    result['original_complete_field_inventory']=str(a.inventory)
    result['original_complete_field_inventory_sha256']=sha(a.inventory)
    result['original_thirteen_candidates_retained_verbatim']=True
    result['original_baseline_or_twelve_fields_recomputed']=False
    result['actual_corrected_anchor_preparation']=prepared
    result['field_specific_executed_wrappers']={r['name']:plan['geometry_wrapper'] for r in plan['candidates']}
    result['partial_control_response_scope']={
        'original_six':plan['partial_control_response_scope'],
        'actual_eight_response_sha256':EIGHT_SHA,
        'all_eight_external_full_half_gates_observed':True,
        'all_eight_combined_half_vectors_observed':False,
        'original_six_combined_rows_retained_verbatim':True,
        'new_two_combination_scope':[r for r in newrows[len(oldrows):]],
        'local_M28_unsolved_warm_design_only':True,
        'new_M32_actual_J_claimed':False,
    }
    added=[]
    for name,step in [('initial_speed_frontload',.01),('vd',.002)]:
        result['directions'].append(dict(name=name,step=step))
        for sign in [1,-1]:
            case_name=name+('-plus' if sign>0 else '-minus');h=sign*step
            prefix=a.out.parent/('geometry-'+case_name+'-anchor-r1')
            command=base+['--response-data',str(a.response),
                '--neutral-control-step',name+'='+repr(h),
                '--out-prefix',str(prefix),'--inspect-warm-output',str(prefix)+'-screen.json',
                '--geometry-array',str(prefix)+'-field.json']
            profile=dict(eight['baseline']['profile'])
            for key,value in rows[name]['physical_profile_derivative'].items():
                delta=h*value
                if key=='initial_speed_frontload' and key not in profile:
                    if delta!=0.:profile[key]=delta
                else:profile[key]+=delta
            resource=str(prefix)+'-resource.json'
            owned=[sys.executable,str(HERE/'strong_foreground_resource_run.py'),
                '--out',resource,'--heartbeat',str(prefix)+'-heartbeat.json',
                '--ownership',str(prefix)+'-ownership.json','--task-prefix',
                'q122-actual-missing-control-'+case_name,'--',*command]
            row=dict(name=case_name,direction=name,step=h,command=owned,
                expected_core=plan['baseline_core'],expected_profile=profile,
                report=str(prefix)+'-screen.json',field=str(prefix)+'-field.json',
                resource=resource,log=str(prefix)+'-log.txt',complete_mean_angular=1360,
                actual_new_corrected_anchor_source_sha256=sha(wrapper),
                baseline_is_M28_not_fine_M32=True)
            for key in ('report','field','resource','log'):
                if Path(row[key]).exists():raise FileExistsError('Do not rerun a completed or started new field: '+row[key])
            added.append(row);result['field_specific_executed_wrappers'][case_name]=str(wrapper)
    result['candidates'].extend(added)
    result['new_fields_only']=[r['name'] for r in added]
    result['source_and_input_sha256'].update({str(p):sha(p) for p in
        [Path(__file__),a.plan,a.inventory,a.response,wrapper,
         HERE/'strong_frontload_anchor_loader_adapter.py',HERE/'strong_monotone_initial_speed_anchor.py',
         HERE/'strong_foreground_resource_run.py']})
    result['source_and_input_sha256'].update(prepared['source_inputs'])
    result['limitations']+=['Only four supplemental finite geometry fields are to be evaluated; the original thirteen are reused.',
        'The new external columns have measured full/half data, but the original six combined-half vectors remain unavailable.',
        'The original M28 baseline is not silently relabelled as the accepted fine M32 field.']
    if result['candidates'][:13]!=plan['candidates'] or len(result['candidates'])!=17:
        raise ArithmeticError('The original complete fields or intended count changed')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(plan=str(a.out),sha256=sha(a.out),retained_original_fields=13,new_fields=4,
        names=result['new_fields_only'],new_geometry_or_ODE_Node_calls=0)),flush=True)

if __name__=='__main__':main()
