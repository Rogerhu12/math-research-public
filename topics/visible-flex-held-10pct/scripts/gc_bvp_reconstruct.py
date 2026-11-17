"""Check the actual embedding compatibility of a GC BVP checkpoint."""
import argparse,json
import numpy as np
from scipy.integrate import solve_ivp
from gc_bvp import Problem
from gc_prefix_explore import initial


def reconstruct(filename,nu=128,ns=81):
    d=json.load(open(filename));pr=Problem(**d['params']);p=np.array(d['coefficients'])
    S=p[-1]
    Lc=pr.ZL@p[pr.sl[0]].reshape(pr.nL,pr.K+1)
    Mc=pr.ZMN@p[pr.sl[1]].reshape(pr.nMN,pr.K)
    ac=pr.apart+S*pr.apartS+pr.Za@p[pr.sl[3]]
    u=2*np.pi*np.arange(nu)/nu;ks=2*np.arange(pr.K+1)
    C=np.cos(u[:,None]*ks);Si=np.sin(u[:,None]*ks[1:])
    a0,y=initial(pr.A,pr.B,nu)
    yi=y[2*nu:]
    def fun(s,v):
        B=pr.sp(s/S)
        a=B@ac;L=(B@Lc)@C.T;M=(B@Mc)@Si.T
        e1=v[3*nu:6*nu].reshape(3,nu);e2=v[6*nu:].reshape(3,nu)
        normal=np.cross(e1.T,e2.T).T
        return np.r_[e1.ravel(),(normal*L).ravel(),(normal*M/a).ravel()]
    sol=solve_ivp(fun,[0,S],yi,rtol=2e-11,atol=2e-12,method='DOP853',max_step=S/250,dense_output=True)
    freq=np.fft.fftfreq(nu,1/nu)
    def du(x):return np.fft.ifft(1j*freq*np.fft.fft(x,axis=-1),axis=-1).real
    rows=[]
    for s in np.linspace(0,S,ns):
        v=sol.sol(s);F=v[:3*nu].reshape(3,nu)
        e1=v[3*nu:6*nu].reshape(3,nu);e2=v[6*nu:].reshape(3,nu)
        a=pr.sp(s/S)@ac;Fu=du(F)
        E=np.sum(e1*e1,axis=0);G=np.sum(Fu*Fu,axis=0)/a**2
        cross=np.sum(Fu*e1,axis=0)/a
        metric=max(abs(E-1).max(),abs(G-1).max(),abs(cross).max())
        r=np.linalg.norm(F[:2],axis=0)
        rows.append(dict(s=float(s),a=float(a),metric_error=float(metric),
                         coordinate_error=float(np.linalg.norm(Fu-a*e2,axis=0).max()),
                         radial_min=float(r.min()),radial_max=float(r.max()),
                         z_min=float(F[2].min()),z_max=float(F[2].max())))
    F=sol.sol(S)[:3*nu].reshape(3,nu);r=np.linalg.norm(F[:2],axis=0)
    endpoint_circle_error=np.max(np.sqrt((r-pr.rc)**2+(F[2]-F[2].mean())**2))
    return dict(checkpoint=filename,nu=nu,ns=ns,length=float(S),
                max_height=max(x['z_max'] for x in rows),
                metric_error=max(x['metric_error'] for x in rows),
                coordinate_error=max(x['coordinate_error'] for x in rows),
                endpoint_circle_error=float(endpoint_circle_error),
                endpoint=rows[-1],rows=rows)


if __name__=='__main__':
    pa=argparse.ArgumentParser();pa.add_argument('input');pa.add_argument('--output');args=pa.parse_args()
    ans=reconstruct(args.input)
    if args.output:json.dump(ans,open(args.output,'w'),indent=2)
    print(json.dumps({k:v for k,v in ans.items() if k!='rows'},indent=2))
