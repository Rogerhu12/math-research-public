#!/usr/bin/env python3
"""Check R137 Cartesian two-jets against exact cone and bent-plane surfaces."""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from fd2d_k0_ruling_coast import propagate,at_material


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def cylinder_inlet(u,a=1.1,curvature=.4):
    u=np.asarray(u);c,s=np.cos(u),np.sin(u);q=curvature*a*s
    ex=np.zeros(u.shape+(3,));ex[...,0]=1
    T=np.stack((np.zeros_like(u),np.cos(q),np.sin(q)),axis=-1)
    N=np.stack((np.zeros_like(u),-np.sin(q),np.cos(q)),axis=-1)
    C=lambda t:t[...,None]
    e1=C(c)*ex+C(s)*T;e2=-C(s)*ex+C(c)*T
    e1u=-C(s)*ex+C(c)*T+C(curvature*a*s*c)*N
    e2u=-C(c)*ex-C(s)*T+C(curvature*a*c*c)*N
    e1uu=-C(c)*ex-C(s+curvature**2*a*a*s*c*c)*T+C(curvature*a*(2*c*c-s*s))*N
    e2uu=C(s)*ex-C(c+curvature**2*a*a*c**3)*T-C(3*curvature*a*s*c)*N
    return dict(u=u,X=np.stack((a*c,np.sin(q)/curvature,(1-np.cos(q))/curvature),axis=-1),
        X_u=a*e2,X_uu=a*e2u,e1=e1,e1_u=e1u,e1_uu=e1uu,
        e2=e2,e2_u=e2u,e2_uu=e2uu,N=N,N_u=-C(curvature*a*c)*T,
        n=curvature*c*c,m=curvature*s*c,n_u=-2*curvature*s*c,
        m_u=curvature*(c*c-s*s),n_uu=-2*curvature*(c*c-s*s),m_uu=-4*curvature*s*c)


def cylinder_jet(r,u,curvature=.4):
    c,s=np.cos(u),np.sin(u);q=curvature*r*s;z=np.zeros_like(u)
    e1=np.stack((c,np.cos(q)*s,np.sin(q)*s),axis=-1)
    e2=np.stack((-s,np.cos(q)*c,np.sin(q)*c),axis=-1)
    N=np.stack((z,-np.sin(q),np.cos(q)),axis=-1);C=lambda t:t[...,None]
    return dict(X=np.stack((r*c,np.sin(q)/curvature,(1-np.cos(q))/curvature),axis=-1),
        X_s=e1,X_u=r*e2,X_ss=C(curvature*s*s)*N,
        X_su=e2+C(r*curvature*s*c)*N,X_uu=-r*e1+C(r*r*curvature*c*c)*N)


def cone_inlet(u,a=1.1,v=.3,z0=.2):
    u=np.asarray(u);c,s=np.cos(u),np.sin(u);b=np.sqrt(1-v*v);zero=np.zeros_like(u)
    er=np.stack((c,s,zero),axis=-1);et=np.stack((-s,c,zero),axis=-1)
    e1=v*er;e1[...,2]=b;N=-b*er;N[...,2]=v
    X=a*er;X[...,2]=z0
    return dict(u=u,X=X,X_u=a*et,X_uu=-a*er,e1=e1,e1_u=v*et,e1_uu=-v*er,
        e2=et,e2_u=-er,e2_uu=-et,N=N,N_u=-b*et,n=np.full_like(u,b/a),m=zero,
        n_u=zero,m_u=zero,n_uu=zero,m_uu=zero)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();rows=[]
    for sigma in (0.,.1,.4):
        phi=np.linspace(-.7,.7,501);out=propagate(1.1,1.,sigma,cylinder_inlet(phi))
        exact=cylinder_jet(1.1+sigma,out['material_u'])
        errors={k:float(np.max(abs(out[k]-exact[k]))) for k in exact}
        rows.append(dict(case='exact generalized cylinder, nonzero ruling ratio',sigma=sigma,
            errors=errors,metric=float(out['metric'].max()),curvature_error=float(np.max(abs(out['actual_curvature']-.4))),
            D_error=float(np.max(abs(out['D']-1.1)))))
        phi=np.linspace(0,2*np.pi,513)[:-1];out=propagate(1.1,.3,sigma,cone_inlet(phi))
        r=1.1+.3*sigma;c,s=np.cos(phi),np.sin(phi);b=np.sqrt(1-.3**2)
        expected=np.stack((r*c,r*s,np.full_like(phi,.2+b*sigma)),axis=-1)
        rows.append(dict(case='exact round cone, zero ruling ratio',sigma=sigma,
            position_error=float(np.max(abs(out['X']-expected))),metric=float(out['metric'].max()),
            curvature_error=float(np.max(abs(out['actual_curvature']-b/r)))))
    target=np.linspace(-.4,.4,129);out=at_material(1.1,1.,.4,target,cylinder_inlet)
    exact=cylinder_jet(1.5,target)
    inverse_errors={k:float(np.max(abs(out[k]-exact[k]))) for k in exact}
    worst=max([v for r in rows for k,v in r.items() if k.endswith('error') or k=='metric']+
        [v for r in rows for v in r.get('errors',{}).values()]+list(inverse_errors.values()))
    report=dict(schema='fd2d-k0-ruling-actual-twojet-check-v1',source_sha256=digest(__file__),
        provider_sha256=digest(Path(__file__).with_name('fd2d_k0_ruling_coast.py')),rows=rows,
        material_inverse_errors=inverse_errors,worst_error=worst,passed=worst<2e-10,
        seconds=time.monotonic()-start,scope='Finite implementation checks of exact known surfaces, not the research core certificate.')
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),worst=worst,passed=report['passed'],seconds=report['seconds'])))
    if not report['passed']:raise SystemExit(1)


if __name__=='__main__':main()
