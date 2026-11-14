#!/usr/bin/env python3
"""Refine only unpaid radial atoms of the same actual periodic-cylinder mean.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Successful prior atoms are retained. An unpaid atom is bisected at exact
rational physical coordinates; each actual quintic is restricted again by
exact Bernstein arithmetic. All background, state-repair, full-angle,
holomorphic-branch and complete original mean rules stay unchanged.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

HERE=Path(__file__).resolve().parent
ORIGINAL_SHA='013a0355bbd7a85d4fe64cabda6faa3140929caf85335986a44f083fe29be336'
BOUNDARY_SHA='3d0c0eee684d17f74e6dddf3a84d0d130ae644d4f416d51ecb16c0cb455b273d'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(x):return F(int(x[0]))*F(2)**int(x[1])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('background','state-repair','radial','table','background-source','domain','primary','prior','prior-resource','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--max-depth',type=int,default=4)
    p.add_argument('--angular',type=int,default=1024)
    p.add_argument('--angular-max',type=int,default=4096)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh actual radial-refined strip output required')
    original=HERE/'strong_newg_complex_angular_mean_strip.py'
    boundary=HERE/'strong_newg_complex_angular_mean_boundary_refine.py'
    if sha(original)!=ORIGINAL_SHA or sha(boundary)!=BOUNDARY_SHA:
        raise ValueError('Original complex-strip or boundary source changed')
    prior,formal=map(read,(a.prior,a.prior_resource))
    if (prior['source_sha256']!=BOUNDARY_SHA or not prior['complete_domain_cover'] or
        formal['exitcode']!=0 or not formal['wait4_observed'] or
        prior['schema']!='actual-q106-complete-periodic-boundary-mean-strip-v1' or
        not 1<=a.max_depth<=8):
        raise ValueError('The completed same-field boundary run and explicit refinement limit are required')
    source=original.read_text()
    old='hypercos=np.array([1.,R.ai(cp)[1]]);hypersin=np.array([-R.ai(sp)[1],R.ai(sp)[1]])'
    new='hypercos=R.ai(cp);hypersin=R.ai(sp)'
    stop='    records=[];failed=[];cover=F(0);height_error=F(0);maxerrs=[F(0),F(0)];quality={}\n'
    if source.count(old)!=1 or source.count(stop)!=1:raise ValueError('Frozen exact context moved')
    changed=source.replace(old,new,1).replace(stop,'    return locals()\n'+stop,1)
    if changed.replace('    return locals()\n'+stop,stop,1).replace(new,old,1)!=source:
        raise ValueError('Unlisted exact-context change')
    ns={'__file__':str(original),'__name__':'actual_boundary_radial_context'}
    exec(compile(changed,'<actual-boundary-radial-context>','exec'),ns)
    argv=sys.argv;sys.argv=[argv[0]]
    for key in ('background','state_repair','radial','table','background_source','domain','primary','out'):
        sys.argv+=['--'+key.replace('_','-'),str(getattr(a,key))]
    sys.argv+=['--angular',str(a.angular),'--angular-max',str(a.angular_max)]
    try:ctx=ns['main']()
    finally:sys.argv=argv
    for key,h in ctx['inputs'].items():
        if prior['input_sha256'].get(key)!=h:raise ValueError('The actual same-field input changed: '+key)
    domain=ctx['domain'];parents=domain['rows']
    if len(parents)!=len(prior['rows']) or len(parents)!=3326:
        raise ValueError('Full original 3326-parent cover required')
    result=[];tree=[];retained=0;computed=0

    def evaluate(parent_number,row,path,depth):
        nonlocal computed
        left,right=map(F,row['s_interval'])
        Y,Ys=ctx['states_on'](row['original_interval'],left,right)
        attempts=[];ok=False;data={};width=F(1,32)
        widths=[F(1,32)] if depth<a.max_depth else [F(1,32),F(3,128),F(1,64)]
        for width in widths:
            N=a.angular
            while True:
                ok,data=ctx['enclose'](row,Y,Ys,width,N)
                attempts.append(dict(strip_width=str(width),boundary_angular_boxes=N,positive=ok,
                    **{k:v for k,v in data.items() if k.startswith('real_part_')}))
                if ok or N>=a.angular_max:break
                N*=2
            if ok:break
        computed+=1
        node=dict(parent_atom=parent_number,subdivision_path=path,depth=depth,
            s_interval=row['s_interval'],positive_complex_domain=ok,attempts=attempts)
        tree.append(node)
        print(json.dumps(dict(event='actual_radial_strip_refinement_node',parent_atom=parent_number,
            path=path,positive=ok,width=str(width),depth=depth)),flush=True)
        if not ok and depth<a.max_depth:
            middle=(left+right)/2
            for child,ab in enumerate(((left,middle),(middle,right))):
                smaller=dict(row,s_interval=[str(v) for v in ab])
                evaluate(parent_number,smaller,path+str(child),depth+1)
            return
        item=dict(parent_atom=parent_number,subdivision_path=path,original_interval=row['original_interval'],
            background_piece=row['background_piece'],s_interval=row['s_interval'],
            whole_physical_interval_and_complex_angular_strip=True,whole_repair_homotopy=True,
            actual_original_quintics_restricted_exactly=True,positive_complex_domain=ok,
            strip_width=str(width),angular_boxes=N,attempts=attempts,**data,
            evaluated_upper_boundary_with_exact_fixed_imaginary_coordinate=True,
            lower_boundary_by_real_coefficient_conjugation=True,
            whole_strip_by_periodic_harmonic_minimum_and_maximum_principles=True,
            retained_prior_successful_atom=False)
        result.append(item)

    for number,(row,oldrow) in enumerate(zip(parents,prior['rows'])):
        if oldrow['atom']!=number or oldrow['s_interval']!=row['s_interval'] or oldrow['original_interval']!=row['original_interval']:
            raise ArithmeticError('Same original radial atom identity required')
        if oldrow['positive_complex_domain']:
            result.append(dict(oldrow,parent_atom=number,subdivision_path='',retained_prior_successful_atom=True));retained+=1
        else:
            left,right=map(F,row['s_interval']);middle=(left+right)/2
            for child,ab in enumerate(((left,middle),(middle,right))):
                evaluate(number,dict(row,s_interval=[str(v) for v in ab]),str(child),1)
    cursor=F(0);height=F(0);maximum=[F(0),F(0)];failed=[];counts={}
    parent_cover={i:[] for i in range(len(parents))}
    for number,item in enumerate(result):
        item['atom']=number
        left,right=map(F,item['s_interval']);parent=parents[item['parent_atom']]
        pl,pr=map(F,parent['s_interval'])
        if left!=cursor or not pl<=left<right<=pr:
            raise ArithmeticError('The exact refined cover changed the real physical domain')
        parent_cover[item['parent_atom']].append([left,right]);cursor=right
        if item['positive_complex_domain']:
            errors=list(map(dy,item['complete_periodic_mean_Hs_Hss_alias_upper']))
            height+=(right-left)*errors[0];maximum=[max(x,y) for x,y in zip(maximum,errors)]
            counts[item['strip_width']]=counts.get(item['strip_width'],0)+1
        else:failed.append(number)
    for i,intervals in parent_cover.items():
        pl,pr=map(F,parents[i]['s_interval'])
        if not intervals or intervals[0][0]!=pl or intervals[-1][1]!=pr or any(x[1]!=y[0] for x,y in zip(intervals,intervals[1:])):
            raise ArithmeticError('An original whole radial atom was not completely covered')
    complete=cursor==ctx['L'];passed=complete and not failed
    out=dict(schema='actual-q106-complete-radial-refined-complex-mean-strip-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        original_rectangle_source_sha256=ORIGINAL_SHA,boundary_source_sha256=BOUNDARY_SHA,
        exact_reversible_boundary_context_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        input_sha256={**ctx['inputs'],str(a.prior):sha(a.prior),str(a.prior_resource):sha(a.prior_resource)},
        primary_sha256=prior['primary_sha256'],background_comparison_definition_sha256=prior['background_comparison_definition_sha256'],
        state_comparison_definition_sha256=prior['state_comparison_definition_sha256'],
        complete_domain_cover=complete,all_complex_domain_gates=passed,original_parents=3326,
        complete_atoms=len(result),failed_atoms=failed,retained_prior_successful_atoms=retained,
        actually_evaluated_refinement_nodes=computed,exact_refinement_tree=tree,rows=result,
        exact_mean_angular=1360,complex_strip_width_counts=counts,
        complete_mean_alias_H_Hs_Hss_upper=[ns['upper'](ns['aq'](z)) for z in (height,*maximum)] if passed else None,
        full_mean_alias_H_Hs_Hss_display=[float(z) for z in (height,*maximum)] if passed else None,
        fixed_chart_transport=prior['fixed_chart_transport'],harmonic_argument=prior['harmonic_argument'],
        exact_uniform_mean_rule=prior['exact_uniform_mean_rule'],H_alias_scope=prior['H_alias_scope'],
        original_IEEE_libm_and_node_evaluation_or_coordinate_alignment_paid=False,radial_Gauss6_error_paid=False,
        prior_negative_rows_preserved_by_original_inputs=True,
        original_g_PDE_reach_or_closed_surface_certified=False,new_ODE_Node_Newton_or_spatial_sampling_calls=0,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:
            g.write((json.dumps(out,separators=(',',':'))+'\n').encode())
    print(json.dumps(dict(event='actual_radial_refined_complex_mean_finished',all_complex_domain_gates=passed,
        atoms=len(result),failed=len(failed),retained=retained,computed=computed,
        H_Hs_Hss=out['full_mean_alias_H_Hs_Hss_display'],path=str(a.out),sha256=sha(a.out))),flush=True)

if __name__=='__main__':main()
