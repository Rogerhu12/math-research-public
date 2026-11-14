#!/usr/bin/env python3
"""Refine failed or narrow actual angular strips on the periodic boundary.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The old complete rectangle run is retained. Only its unpaid or narrower
atoms are reevaluated. W,D,rho are entire periodic functions before angular
division. A uniform positive real part on Im(psi)=delta and its conjugate
boundary gives the same lower bound on the compact periodic cylinder by
the harmonic minimum principle. The resulting holomorphic Vz and Vsz have
their absolute maxima on those same boundaries. No radial/physical domain,
square-root branch, angular mean rule or accepted candidate is changed.
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
ORIGINAL=HERE/'strong_newg_complex_angular_mean_strip.py'
ORIGINAL_SHA='013a0355bbd7a85d4fe64cabda6faa3140929caf85335986a44f083fe29be336'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(x):return F(int(x[0]))*F(2)**int(x[1])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('background','state-repair','radial','table','background-source','domain','primary','prior','prior-resource','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--strip-widths',nargs='+',default=['1/32','3/128','1/64'])
    p.add_argument('--angular',type=int,default=1024)
    p.add_argument('--angular-max',type=int,default=4096)
    p.add_argument('--reuse-width',default='1/32')
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh actual boundary-strip output required')
    if sha(ORIGINAL)!=ORIGINAL_SHA:raise ValueError('Original actual complex-strip source changed')
    prior=read(a.prior);formal=read(a.prior_resource)
    if (prior['source_sha256']!=ORIGINAL_SHA or not prior['complete_domain_cover'] or
        formal['exitcode']!=0 or not formal['wait4_observed'] or
        prior['schema']!='actual-q106-complete-complex-angular-mean-strip-v1'):
        raise ValueError('The completed original rectangle run, including any failure, is required')
    source=ORIGINAL.read_text()
    old='hypercos=np.array([1.,R.ai(cp)[1]]);hypersin=np.array([-R.ai(sp)[1],R.ai(sp)[1]])'
    new='hypercos=R.ai(cp);hypersin=R.ai(sp)'
    stop='    records=[];failed=[];cover=F(0);height_error=F(0);maxerrs=[F(0),F(0)];quality={}\n'
    if source.count(old)!=1 or source.count(stop)!=1:raise ValueError('Frozen boundary/context construction moved')
    transformed=source.replace(old,new,1).replace(stop,'    return locals()\n'+stop,1)
    if transformed.replace('    return locals()\n'+stop,stop,1).replace(new,old,1)!=source:
        raise ValueError('The two explicit construction changes are not exactly reversible')
    ns={'__file__':str(ORIGINAL),'__name__':'actual_complex_boundary_context'}
    exec(compile(transformed,'<actual-positive-periodic-boundary-context>','exec'),ns)
    argv=sys.argv;sys.argv=[argv[0]]
    for key in ('background','state_repair','radial','table','background_source','domain','primary','out'):
        sys.argv+=['--'+key.replace('_','-'),str(getattr(a,key))]
    sys.argv+=['--strip-widths',*a.strip_widths,'--angular',str(a.angular),'--angular-max',str(a.angular_max)]
    try:ctx=ns['main']()
    finally:sys.argv=argv
    if prior['input_sha256']!=ctx['inputs']:raise ValueError('The same complete field and all actual domains are required')
    domain=ctx['domain'];rows=domain['rows'];widths=list(map(F,a.strip_widths));reuse=F(a.reuse_width)
    if len(prior['rows'])!=len(rows) or len(rows)!=3326:raise ValueError('Complete actual 3326-atom cover required')
    result=[];failed=[];height=F(0);maximum=[F(0),F(0)];counts={};retained=0;computed=0;cursor=F(0)
    for number,(row,oldrow) in enumerate(zip(rows,prior['rows'])):
        left,right=map(F,row['s_interval'])
        if left!=cursor or oldrow['atom']!=number or oldrow['s_interval']!=row['s_interval'] or oldrow['original_interval']!=row['original_interval']:
            raise ArithmeticError('The complete radial/source atom identity changed')
        if oldrow['positive_complex_domain'] and F(oldrow['strip_width'])>=reuse:
            item=dict(oldrow,retained_original_complete_rectangle_row=True);retained+=1
        else:
            Y,Ys=ctx['states_on'](row['original_interval'],left,right);attempts=[];ok=False
            for width in widths:
                N=a.angular
                while True:
                    ok,data=ctx['enclose'](row,Y,Ys,width,N)
                    attempts.append(dict(strip_width=str(width),boundary_angular_boxes=N,positive=ok,
                                         **{k:v for k,v in data.items() if k.startswith('real_part_')}))
                    if ok or N>=a.angular_max:break
                    N*=2
                if ok:break
            item=dict(atom=number,original_interval=row['original_interval'],background_piece=row['background_piece'],s_interval=row['s_interval'],
                whole_physical_interval_and_complex_angular_strip=True,whole_repair_homotopy=True,
                actual_original_quintics_restricted_exactly=True,positive_complex_domain=ok,
                strip_width=str(width),angular_boxes=N,attempts=attempts,**data,
                evaluated_upper_boundary_with_exact_fixed_imaginary_coordinate=True,
                lower_boundary_by_real_coefficient_conjugation=True,
                whole_strip_by_periodic_harmonic_minimum_and_maximum_principles=True,
                retained_original_complete_rectangle_row=False)
            computed+=1
        result.append(item);cursor=right
        if item['positive_complex_domain']:
            e=list(map(dy,item['complete_periodic_mean_Hs_Hss_alias_upper']))
            height+=(right-left)*e[0];maximum=[max(x,y) for x,y in zip(maximum,e)]
            counts[item['strip_width']]=counts.get(item['strip_width'],0)+1
        else:failed.append(number)
        if len(result)%128==0:
            print(json.dumps(dict(event='actual_complex_boundary_refinement_progress',atoms=len(result),retained=retained,
                actual_new_boundary_atoms=computed,failed=len(failed),width_counts=counts)),flush=True)
    complete=cursor==ctx['L'] and len(result)==len(rows);passed=complete and not failed
    upper,aq=ns['upper'],ns['aq']
    out=dict(schema='actual-q106-complete-periodic-boundary-mean-strip-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        original_rectangle_source_sha256=ORIGINAL_SHA,exact_reversible_boundary_context_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        input_sha256={**ctx['inputs'],str(a.prior):sha(a.prior),str(a.prior_resource):sha(a.prior_resource)},
        primary_sha256=prior['primary_sha256'],background_comparison_definition_sha256=prior['background_comparison_definition_sha256'],
        state_comparison_definition_sha256=prior['state_comparison_definition_sha256'],
        complete_domain_cover=complete,all_complex_domain_gates=passed,complete_atoms=len(result),failed_atoms=failed,
        retained_original_complete_rectangle_atoms=retained,actually_recomputed_boundary_atoms=computed,
        rows=result,exact_mean_angular=1360,complex_strip_width_counts=counts,
        complete_mean_alias_H_Hs_Hss_upper=[upper(aq(z)) for z in (height,*maximum)] if passed else None,
        full_mean_alias_H_Hs_Hss_display=[float(z) for z in (height,*maximum)] if passed else None,
        fixed_chart_transport='theta_s=b_s Q and nu=b_s Q/(1+b Q_psi); Q is the original finite periodic sine polynomial, without atan branches.',
        harmonic_argument='For every fixed real s and repair parameter: W,D,rho are entire 2*pi-periodic with real coefficients. Uniform positive real parts on the upper horizontal boundary transfer by conjugation and the harmonic minimum principle to the compact periodic cylinder. The resulting holomorphic scalar Vz,Vsz have their modulus maxima on its horizontal boundary. No vertical-edge fee.',
        exact_uniform_mean_rule='2*M/(exp(1360*delta)-1), for normalized dpsi/(2*pi) averages',
        H_alias_scope='Same single zero anchor and exact positive radial primitive of angular alias; not the radial Gauss6 error.',
        original_IEEE_libm_and_node_evaluation_or_coordinate_alignment_paid=False,radial_Gauss6_error_paid=False,
        old_rectangle_failure_rows_preserved_by_original_input=True,
        original_g_PDE_reach_or_closed_surface_certified=False,new_ODE_Node_Newton_or_spatial_sampling_calls=0,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:g.write((json.dumps(out,separators=(',',':'))+'\n').encode())
    print(json.dumps(dict(event='actual_complex_boundary_mean_finished',all_complex_domain_gates=passed,
        atoms=len(result),failed=len(failed),retained=retained,computed=computed,
        H_Hs_Hss=out['full_mean_alias_H_Hs_Hss_display'],path=str(a.out),sha256=sha(a.out))),flush=True)

if __name__=='__main__':main()
