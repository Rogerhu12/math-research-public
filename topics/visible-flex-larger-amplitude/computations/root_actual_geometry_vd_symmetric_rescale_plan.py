#!/usr/bin/env python3
"""Use a measured valid symmetric vd step without changing any geometry gate.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The old +.002 failure and its exact chart diagnosis are retained. Actual
zero-ODE probes must show both +.001 and -.001 pass the unchanged chart gate.
All original thirteen fields and both completed lambda fields are reused.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('plan','out'):p.add_argument('--'+key,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh symmetric-step plan required')
    plan=read(a.plan)
    if sha(a.plan)!='e223a02f55b1ba337646bf53d67fd5041137d6a17d4c739e2c8556ff3afd4fc6':
        raise ValueError('The original real assembled-eight plan changed')
    parent=a.plan.resolve().parent;rows={r['name']:r for r in plan['candidates']}
    failure=read(rows['vd-plus']['report']);failure_owned=read(rows['vd-plus']['resource'])
    if (failure_owned['exitcode']!=1 or failure['finite_domain_passed'] or
        failure['inspection_error']!="ValueError('The physical chart lost orientation')" or
        failure['worker_start_attempts']!=0):
        raise ValueError('The actual original +.002 orientation rejection is required')
    observations=[]
    for name in ('plus002','plus001','minus001'):
        prefix=parent/('chart-vd-'+name+'-probe-r1')
        chart_path=Path(str(prefix)+'-chart.json');resource_path=Path(str(prefix)+'-resource.json')
        chart,owned=map(read,(chart_path,resource_path))
        if (owned['exitcode']!=0 or not owned['wait4_observed'] or chart['geometry_field_computed'] or
                not chart['raw_strict_increase'] or not chart['all_exact_binary_polynomial_piece_derivatives_positive']):
            raise ValueError('An actual same-chart diagnostic is incomplete')
        if name=='plus002':
            bad=chart['grid_nonpositive_spacings']
            if chart['original_geometry_gate_passed'] or len(bad)!=1 or bad[0]['displayed_ds']!=0 or not bad[0]['same_piece_strict_positive_exact_ds']:
                raise ValueError('The original isolated displayed-grid tie was not reproduced')
        elif not chart['original_geometry_gate_passed']:
            raise ValueError('Both exact same smaller symmetric steps must pass the original gate')
        observations.append(dict(label=name,chart=str(chart_path),chart_sha256=sha(chart_path),resource=str(resource_path),resource_sha256=sha(resource_path)))
    for name in ('initial_speed_frontload-plus','initial_speed_frontload-minus'):
        row=rows[name];report,owned=map(read,(row['report'],row['resource']))
        if owned['exitcode']!=0 or not report['finite_domain_passed'] or not report['geometry_fields']['all_raw_nodes_and_modes_retained']:
            raise ValueError('Both completed lambda fields must be preserved')
    response=read(plan['assembled_response_file'])
    vd=next(r for r in response['additional_core_held_directions'] if r['external_field']=='vd')
    result=copy.deepcopy(plan);result['scope']=__doc__
    result['rescaled_from_plan']=str(a.plan);result['rescaled_from_plan_sha256']=sha(a.plan)
    for direction in result['directions']:
        if direction['name']=='vd':
            if direction['step']!=.002:raise ValueError('Original vd scale differs')
            direction['step']=.001
    for row in result['candidates']:
        if row['direction']!='vd':continue
        old=rows[row['name']];sign=1 if old['step']>0 else -1;step=sign*.001
        oldprefix=old['command'][old['command'].index('--out-prefix')+1]
        prefix=parent/('geometry-'+row['name']+'-anchor-half-r1')
        row['command']=[s.replace(oldprefix,str(prefix)) for s in old['command']]
        row['command'][row['command'].index('--neutral-control-step')+1]='vd='+repr(step)
        row['command'][row['command'].index('--task-prefix')+1]='q122-actual-missing-control-'+row['name']+'-half'
        for key in ('report','field','resource','log'):row[key]=old[key].replace(oldprefix,str(prefix))
        row['step']=step;profile=dict(response['baseline']['profile'])
        for key,value in vd['physical_profile_derivative'].items():profile[key]+=step*value
        row['expected_profile']=profile
        row['same_original_orientation_gate_prechecked']=True
        if list(prefix.parent.glob(prefix.name+'*')):raise FileExistsError('Fresh actual vd field output required')
    if result['candidates'][:15]!=plan['candidates'][:15]:
        raise ArithmeticError('A completed old or lambda field was changed')
    result['new_fields_only']=['vd-plus','vd-minus']
    result['unchanged_completed_fields_retained']=15
    result['explicit_symmetric_vd_rescale']=dict(original_step=.002,new_step=.001,
        reason='Actual +.002 common-grid binary64 displayed coordinate tie; exact binary chart piece has strictly positive derivative.',
        original_gate_retained=True,failed_report=rows['vd-plus']['report'],failed_report_sha256=sha(rows['vd-plus']['report']),
        failed_resource=rows['vd-plus']['resource'],failed_resource_sha256=sha(rows['vd-plus']['resource']),
        actual_zero_ODE_chart_probes=observations,finite_geometry_not_inferred_from_chart_probes=True)
    result['source_and_input_sha256'].update({str(Path(__file__)):sha(__file__),str(a.plan):sha(a.plan)})
    for row in observations:
        result['source_and_input_sha256'].update({row['chart']:row['chart_sha256'],row['resource']:row['resource_sha256']})
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(plan=str(a.out),sha256=sha(a.out),old_fields_retained=15,new_fields=2,symmetric_vd_step=.001,new_geometry_calls=0)),flush=True)

if __name__=='__main__':main()
