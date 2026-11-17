#!/usr/bin/env python3
"""Sample raw mean/primary-projected supported controls at fixed old coefficients.

Unlike the earlier canonical path, the high support moments are not kept
equal to the old coefficients at positive lambda. At lambda=1 the full free
control span is unchanged for a given cutoff. No BVP, continuous certificate,
or nonexistence claim is made by this quadrature/angle-grid diagnostic.
"""
import argparse
import hashlib
import json
from pathlib import Path
from curvature_minimum_controls import features,primary_target,np

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--widths',nargs='+',type=float,default=[.04,.08,.12,.16,.20,.24,.30,.40,.50,.60,.70,.80])
    p.add_argument('--samples',type=int,default=32768)
    p.add_argument('--quad-order',type=int,default=256)
    a=p.parse_args();r=json.loads(a.record.read_text())
    n,M,q=r['base_mode'],r['modes'],r['q'];half=r['halfwidth'];c=np.array(r['physical_corrections'])
    T=2*np.pi/n;phi=T*np.arange(a.samples)/a.samples;x=phi-T/2
    target,beta=primary_target(phi,n,half,r['flatten_transition'],a.quad_order)
    gx,gw=np.polynomial.legendre.leggauss(a.quad_order)
    rows=[]
    for width in a.widths:
        if not 0<half<half+width<T/2:raise ValueError('Invalid cutoff width')
        xs=[];ws=[]
        for lo,hi in [(half,half+width),(half+width,T/2)]:
            xs.append((lo+hi)/2+(hi-lo)*gx/2);ws.append((hi-lo)*gw/T)
        xx=np.concatenate(xs);ww=np.concatenate(ws);B=features(xx,n,M,half,width,0)[0]
        low=np.c_[np.ones_like(xx),-np.cos(n*xx)]
        G=low.T@(ww[:,None]*B)
        C=np.linalg.solve(G[:,:2],G[:,2:])
        h=np.r_[-C@c,c]
        B,_,B2=features(x,n,M,half,width)
        b=B@h;rho_control=(B+B2)@h;rho=1+q*target+rho_control
        row=dict(control_transition=width,low_gram_condition=float(np.linalg.cond(G[:,:2])),
            quadrature_mean_primary_residual_linf=float(max(abs(G@h))),
            sampled_complete_support_linf=float(max(abs(b))),
            sampled_complete_rho_control_linf=float(max(abs(rho_control))),
            sampled_complete_rho_control_min=float(min(rho_control)),
            sampled_complete_rho_control_max=float(max(rho_control)),
            sampled_full_rho_lambda_one_min=float(min(rho)),
            sampled_zero_on_open_protected_arc=float(max(abs(b[abs(x)<half]))))
        rows.append(row);print(json.dumps(row),flush=True)
    result=dict(scope=__doc__,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
        source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in
            [Path(__file__),Path(__file__).with_name('curvature_minimum_controls.py')]},
        input_sha256=hashlib.sha256(a.record.read_bytes()).hexdigest(),
        physical_input=dict(base_mode=n,modes=M,q=q,halfwidth=half,flatten_transition=r['flatten_transition'],
            flatten_beta=beta,physical_corrections=c.tolist()),rows=rows)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
