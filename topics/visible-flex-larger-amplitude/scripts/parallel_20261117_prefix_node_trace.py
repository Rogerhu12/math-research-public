#!/usr/bin/env python3
"""Read an existing node of one accepted C2 prefix, without a new BVP claim.

The 0/1/2 jets are precisely those used by prefix_readout.py's common-jet
quintic.  Selecting a shorter prefix changes the proposed tail design, not
the accepted parent field or its scalar metric on the retained interval.
Raw state and trace arrays are written only to the caller's external path.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def read_node(path, requested_s, angles=2048):
    raw=Path(path).read_bytes();d=json.loads(gzip.decompress(raw))
    if not d.get('success'):raise ValueError('An accepted parent is required')
    x=np.asarray(d['mesh']);i=int(np.argmin(abs(x-requested_s)));s=float(x[i])
    M=d['M'];q=Frenet(M,angles);old=Frenet(M,d['N'])
    y=np.asarray(d['states'][i]);ys=np.asarray(d['rhs'][i])
    base=d.get('fixed_scalar_profile',d.get('inherited_profile'))
    origin=float(d.get('analytic_extension_origin',d.get('extension_scalar',{}).get('start',x[-1])))
    r,ap,app=Profile(base['geometry'],origin)(s)
    if not 0<ap<1:raise ValueError('This chart requires 0<a_prime<1')
    k=ap/r;yss=old.jvp(y,k,ys,dk=app/r-k*k)
    yr=ys/ap;yrr=(yss-ys*app/ap)/(ap*ap)
    w=np.sqrt(1-ap*ap)/ap;wr=-app/(ap**3*np.sqrt(1-ap*ap))
    freq=q.freq[1:];core=np.asarray(d['core']['coefficients'])
    rc=(1-freq*freq)*core
    cs=np.cos(q.angle[:,None]*freq);sn=np.sin(q.angle[:,None]*freq)
    rho=1+cs@rc;rho_phi=-sn@(freq*rc)
    F,dF,ddF=q.jet(y);Fr,_,_=q.jet(yr)
    P=dF[:,2]/(r*rho*w);K=Fr[:,2]/w-1
    T=ddF[:,2]/(r*w*rho*rho)-dF[:,2]*rho_phi/(r*w*rho**3)
    z=w*w;E=1+z;S=1-z*P*P
    A=2*K+K*K+E*P*P;D=1-z*A;L=1+K+E*T
    if np.any(D<=0) or np.any(S<=0):raise ValueError('Sampled projection branch is not positive')
    root=np.sqrt(D);B=A/(root*(1+root))+(1+K)*T/(S*root)
    scan=dict(node_index=i,s=s,r=float(r),a_prime=float(ap),a_second=float(app),
              w=float(w),w_r=float(wr),height_mean=float(y[2*M+1]),
              height_spread=float(np.ptp(F[:,2])),P_max=float(np.max(abs(P))),
              K_max=float(np.max(abs(K))),minimum_D=float(D.min()),
              minimum_S=float(S.min()),minimum_L=float(L.min()),
              sampled_weighted_mean=float(np.mean(rho*B)))
    report=dict(scope=__doc__,parent_input_sha256=hashlib.sha256(raw).hexdigest(),
                requested_s=requested_s,M=M,N=angles,**scan,rho_mean=1.,
                rho_cos_coefficients=rc.tolist(),
                Ptilde_sin_coefficients=(-freq*y[2*M+2:]/(r*w)).tolist(),
                K_cos_coefficients=(yr[2*M+2:]/w).tolist(),K_mean=float(yr[2*M+1]/w-1),
                height_cos_coefficients=y[2*M+2:].tolist(),
                height_r_mean=float(yr[2*M+1]),height_rr_mean=float(yrr[2*M+1]),
                height_r_cos_coefficients=yr[2*M+2:].tolist(),
                height_rr_cos_coefficients=yrr[2*M+2:].tolist(),
                frenet_state=y.tolist(),frenet_r_state=yr.tolist(),frenet_rr_state=yrr.tolist(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return report,scan


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--s',type=float,required=True)
    p.add_argument('--angles',type=int,default=2048);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();report,scan=read_node(args.input,args.s,args.angles)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(**scan,output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest(),
                          source_sha256=report['source_sha256'])))
