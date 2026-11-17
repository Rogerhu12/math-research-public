#!/usr/bin/env python3
"""Read-only short full-Frenet IVP versus the saved Taylor2 terminal target.

No boundary condition is changed and no IVP value is called a solved BVP.
Integration tolerance agreement is numerical evidence, not an enclosure.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigvals,solve

SOURCE=Path(__file__).with_name('2026-11-17-parallel-geometry-frenet-schur.py')
spec=importlib.util.spec_from_file_location('schur_probe_helper',SOURCE)
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
from parallel_20261117_continue import lift_states,physical,projector


def gram(q,y,velocity,a,core):
    F,d,_=q.jet(y);V,_,_=q.jet(velocity)
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core)
    E=np.sum(V*V,axis=1)-1
    G=np.sum(d*d,axis=1)/(a*rho)**2-1
    C=np.sum(V*d,axis=1)/(a*rho)
    error=(abs(E+G)+np.sqrt((E-G)**2+4*C*C))/2
    j=int(np.argmax(error))
    return dict(relative_operator=float(error[j]),angle=float(q.angle[j]),
                rr=float(E[j]),mixed=float(C[j]),angular=float(G[j]))


def main(args):
    raw=args.reference.read_bytes();ref=json.loads(gzip.decompress(raw))
    metric=json.loads(gzip.decompress(args.metric.read_bytes()))
    if not ref.get('success') or not metric.get('inward_scalar_profile'):
        raise ValueError('Need an accepted reference and explicit inward scalar')
    q=h.Frenet(args.modes or ref['M'],ref['N'])
    reader=h.Frenet(q.M,args.read_angles)
    profile=h.profile_from(metric);s=float(ref['mesh'][-1]);end=args.end
    y=lift_states(ref['states'][-1],ref['M'],q.M)
    z=physical(q,y,profile,s);dt=end-s
    pred=y+dt*z['yp']+.5*dt*dt*z['ypp']
    pred_v=z['yp']+dt*z['ypp']
    principal,_=projector(q,y,profile,s,3)
    T,Ts=h.moving_frame_map(q,z);B=solve(T.T,(T@z['J']+Ts).T).T
    re=np.sort(eigvals(B).real);count=q.M-3
    lo,hi=float(re[-count-1]),float(re[-count])
    if hi-lo<=1e-8:raise ValueError('No real-part threshold at required dimension')
    info,LB=h.selected_left(B,lambda value:value>(lo+hi)/2,q.M,None)
    if info['dimension']!=count:raise ValueError('Selected dimension differs')
    L=LB@T
    core=np.pad(np.asarray(ref['core']['coefficients']),(0,q.M-ref['M']))
    a,ap,_=profile(end);k=ap/a
    out=dict(scope=__doc__,source_sha256=h.sha(__file__),helper_sha256=h.sha(SOURCE),
        reference_sha256=hashlib.sha256(raw).hexdigest(),metric_sha256=h.sha(args.metric),
        M=q.M,N=q.N,read_angles=reader.N,start=s,end=end,
        reference_RHS_gram=gram(reader,y,z['yp'],z['a'],core),
        Taylor2_parametric_gram=gram(reader,pred,pred_v,a,core),
        Taylor2_endpoint_RHS_gram=gram(reader,pred,q.rhs(pred,k),a,core),runs=[])
    values=[]
    for rtol,atol in [(1e-10,1e-13),(1e-12,1e-15)]:
        def rhs(t,state):
            aa,aa1,_=profile(float(t));return q.rhs(state,aa1/aa)
        try:
            sol=solve_ivp(rhs,(s,end),y,method='DOP853',rtol=rtol,atol=atol)
            last=sol.y[:,-1]
            row=dict(rtol=rtol,atol=atol,success=bool(sol.success),message=sol.message,
                nfev=sol.nfev,nodes=len(sol.t),last_time=float(sol.t[-1]))
            if sol.success:
                delta=last-pred;values.append(last)
                row.update(Taylor2_difference_max=float(np.max(abs(delta))),
                    Taylor2_difference_norm_2=float(np.linalg.norm(delta)),
                    Schur_target_difference_max=float(np.max(abs(L@delta))),
                    principal_target_difference_max=float(np.max(abs(principal@delta))),
                    endpoint_RHS_gram=gram(reader,last,q.rhs(last,k),a,core))
        except FloatingPointError as error:
            row=dict(rtol=rtol,atol=atol,success=False,domain_error=str(error))
        out['runs'].append(row)
        print(json.dumps(row),flush=True)
    if len(values)==2:
        delta=values[1]-values[0]
        out['two_tolerance_difference']=dict(coeff_max=float(np.max(abs(delta))),
            Schur_target_max=float(np.max(abs(L@delta))))
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--metric',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--end',type=float,default=.997)
    p.add_argument('--modes',type=int)
    p.add_argument('--read-angles',type=int,default=8192)
    main(p.parse_args())
