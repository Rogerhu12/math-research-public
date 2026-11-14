#!/usr/bin/env python3
"""One small native sign/branch probe of the actual closed20 terminal field.

No BVP, whole objective, Jacobian, inverse angle, reset or body is run.
Raw axis sums are also recorded as exact dyadic rationals, independently
of the floating Fourier sum. A report is a finite diagnostic unless an
explicit separate continuous inequality is supplied.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import resource,time
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_positive_trace_native_field_v2 import (
    PositiveTraceNativeField,terminal_window_jets,positive_trace_native_jets)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('input','candidate','reference-inlet','reference-cache','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    begun=time.perf_counter();saved=load_npz(a.input)
    x,y=saved['mesh'],saved['corrections'];Kmode=int(saved['modes']);e=Kmode+1;d=2*Kmode+1
    trace=json.loads(str(saved['positive_trace_definition']))
    start,stop,cut=[trace[k] for k in ('start','ramp_stop','cut')]
    js=int(np.searchsorted(x,start));je=int(np.searchsorted(x,stop))
    cells=list(range(max(js-2,0),min(je+1,len(x)-1)))
    s=np.unique(np.concatenate([x[j]+(x[j+1]-x[j])*np.array([0.,.25,.5,.75,1.]) for j in cells]))
    theta=2*np.pi*np.arange(128)/128
    ss,tt=np.meshgrid(s,theta,indexing='ij')
    reader=PositiveTraceNativeField(a.input,a.candidate,reference_inlet=a.reference_inlet,
        reference_cache=a.reference_cache)
    bg=reader.evaluate_coast_angular_native(ss,tt)
    w,ws=terminal_window_jets(ss,start,stop)
    q=positive_trace_native_jets(bg,w,ws,exact_tail_mask=ss==cut,include_radial=False)
    if np.max(abs(q['u']-tt))>1e-14 or np.any(q['U_x']!=0):
        raise ArithmeticError('This probe was requested only in the exact U=xi late chart')
    n,m,l=[q[k] for k in ('n','m','l')]
    K=-q['a_ss']/q['a'];G=n*l-m*m-K
    t=(n+l)/2;rad=np.hypot((n-l)/2,m);lm,lp=t-rad,t+rad
    def argmin(values):
        i,j=np.unravel_index(np.argmin(values),values.shape)
        return dict(s=float(s[i]),xi=float(theta[j]),n=float(n[i,j]),m=float(m[i,j]),l=float(l[i,j]),
            K=float(K[i,j]),G=float(G[i,j]),lambda_min=float(lm[i,j]),lambda_max=float(lp[i,j]),
            trace_weight=float(w[i,j]))
    rows=[]
    for i,v in enumerate(s):
        rows.append(dict(s=float(v),K=float(K[i,0]),weight=float(w[i,0]),
            n_min=float(n[i].min()),l_min=float(l[i].min()),
            lambda_min=float(lm[i].min()),lambda_max_min=float(lp[i].min()),
            G_min=float(G[i].min()),G_max=float(G[i].max()),
            negative_n_count=int(np.count_nonzero(n[i]<0)),negative_l_count=int(np.count_nonzero(l[i]<0)),
            negative_definite_count=int(np.count_nonzero(lp[i]<0))))
    exact=[]
    for j in range(max(js-2,0),min(je+2,len(x))):
        axis={}
        for label,sign in (('u0',np.ones(e,dtype=int)),('u_pi_over2',(-1)**np.arange(e))):
            nr=sum((F.from_float(float(v))*int(sg) for v,sg in zip(y[j,:e],sign)),F(0))
            lr=sum((F.from_float(float(v))*int(sg) for v,sg in zip(y[j,d:],sign)),F(0))
            axis[label]=dict(raw_n_exact=str(nr),raw_l_exact=str(lr),raw_n_float=float(nr),raw_l_float=float(lr),
                raw_m_exact='0',tail_n_m_l_exact='0 at u=0; also at pi/2 when actual a>=cut_radius')
        exact.append(dict(node=j,s=float(x[j]),axis=axis))
    protected=(s>=start)&(s<=stop)
    posK=K>0;negative=(lp<0)&posK
    report=dict(schema='fd2d-actual20-terminal-native-branch-probe-v1',source=identity(__file__),
        input=identity(a.input),candidate=identity(a.candidate),
        original_native_source=identity(Path(__file__).with_name('fd2d_gc_positive_trace_native_field_v2.py')),
        trace_window=dict(start=float(start),ramp_stop=float(stop),cut=float(cut)),
        old_cells=cells,angular_count=len(theta),point_count=int(ss.size),
        fixed_angle_chart_U_equals_xi=True,no_angle_inverse=True,radial_rows=rows,
        exact_raw_axis_rows=exact,
        minimum_n_point=argmin(n),minimum_l_point=argmin(l),minimum_eigenvalue_point=argmin(lm),
        minimum_max_eigenvalue_point=argmin(lp),
        sampled_positive_K_negative_definite_points=int(np.count_nonzero(negative)),
        protected_sample=dict(K_min=float(K[protected].min()),n_min=float(n[protected].min()),
            l_min=float(l[protected].min()),lambda_min=float(lm[protected].min()),
            lambda_max_min=float(lp[protected].min()),
            negative_definite_count=int(np.count_nonzero(negative[protected])),
            negative_n_count=int(np.count_nonzero(n[protected]<0)),
            negative_l_count=int(np.count_nonzero(l[protected]<0)),
            G_min=float(G[protected].min()),G_max=float(G[protected].max())),
        no_BVP=True,no_whole_F=True,no_Jacobian=True,no_body=True,no_field_change=True,
        continuous_branch_claim_from_samples=False,
        seconds=time.perf_counter()-begun,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('point_count','sampled_positive_K_negative_definite_points',
        'protected_sample','minimum_l_point','minimum_max_eigenvalue_point','seconds','peak_rss_kib')}))


if __name__=='__main__':main()
