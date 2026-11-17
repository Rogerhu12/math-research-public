"""Experimental Gauss--Codazzi evolution of a constant-speed elliptical equator.

No cap or global existence assertion is made. s is meridian arclength and
u has period 2*pi. Cauchy integration is stable only in negative-curvature
regions; mixed/positive curvature segments are diagnostic at best.
"""
import argparse
import json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipe, ellipeinc
from scipy.optimize import brentq


def initial(A, B, n):
    m = 1-(B/A)**2
    E = ellipe(m)
    a0 = 2*A*E/np.pi
    u = 2*np.pi*np.arange(n)/n
    alpha = np.array([brentq(lambda x: A*(ellipeinc(x-np.pi/2,m)+E)-a0*y,
                             0,2*np.pi,xtol=2e-14) for y in u])
    h = np.sqrt(A*A*np.sin(alpha)**2+B*B*np.cos(alpha)**2)
    X = np.stack([A*np.cos(alpha),B*np.sin(alpha),np.zeros(n)])
    e1 = np.tile([0.,0.,1.],(n,1)).T
    e2 = np.stack([-A*np.sin(alpha)/h,B*np.cos(alpha)/h,np.zeros(n)])
    N = a0*a0*A*B/h**3
    state = np.concatenate([np.zeros(n),N,X.ravel(),e1.ravel(),e2.ravel()])
    return a0,state


def evolve(A=1.,B=.7,n=96,c=4.,smax=.5,atol=1e-9,rtol=1e-9,mode='constant',k=0.,p=1.,ramp=.03,output=None):
    a0,y0=initial(A,B,n)
    freq=np.fft.fftfreq(n,1./n)
    def diff(x):
        return np.fft.ifft(1j*freq*np.fft.fft(x)).real
    def profile(s):
        if mode=='constant':
            return a0+.5*c*s*s,c*s,c
        if mode=='cosine':
            if abs(k)<1e-12:
                return a0+.5*c*s*s,c*s,c
            return a0+c*(1-np.cos(k*s))/(k*k),c*np.sin(k*s)/k,c*np.cos(k*s)
        if mode=='ramped_cosine':
            if s<=ramp:
                theta=np.pi*s/ramp
                return (a0+c*(s*s/4+ramp*ramp/(2*np.pi*np.pi)*(np.cos(theta)-1)),
                        c*(s/2-ramp/(2*np.pi)*np.sin(theta)),
                        c*(1-np.cos(theta))/2)
            t=s-ramp
            p0=c*ramp/2
            a1=a0+c*ramp*ramp*(1/4-1/(np.pi*np.pi))
            return a1+p0*t+c*(1-np.cos(k*t))/(k*k),p0+c*np.sin(k*t)/k,c*np.cos(k*t)
        if mode=='power':
            # acceleration c*(1-s/smax)^p, positive through endpoint
            t=1-s/smax
            acc=c*t**p
            vel=c*smax/(p+1)*(1-t**(p+1))
            pos=a0+c*smax/(p+1)*(s-smax/(p+2)*(1-t**(p+2)))
            return pos,vel,acc
        raise ValueError(mode)
    def fun(s,y):
        a,ap,app=profile(s)
        M=y[:n];N=y[n:2*n]
        L=(M*M-a*app)/N
        e1=y[5*n:8*n].reshape(3,n)
        e2=y[8*n:11*n].reshape(3,n)
        normal=np.cross(e1.T,e2.T).T
        dM=diff(L)-ap/a*M
        dN=diff(M)+ap/a*N+a*ap*L
        return np.concatenate([dM,dN,e1.ravel(),(normal*L).ravel(),(normal*M/a).ravel()])
    def event(s,y):
        return np.min(y[n:2*n])-.002
    event.terminal=True
    event.direction=-1
    sol=solve_ivp(fun,[0,smax],y0,method='DOP853',rtol=rtol,atol=atol,
                  dense_output=True,events=event,max_step=min(.01,smax/100))
    rows=[]
    for s in np.linspace(0,sol.t[-1],21):
        y=sol.sol(s);a,ap,app=profile(s)
        M=y[:n];N=y[n:2*n];L=(M*M-a*app)/N
        X=y[2*n:5*n].reshape(3,n)
        e1=y[5*n:8*n].reshape(3,n);e2=y[8*n:11*n].reshape(3,n)
        normal=np.cross(e1.T,e2.T).T
        Xu=np.stack([diff(x) for x in X])
        Xuu=np.stack([diff(x) for x in Xu])
        Nr=np.sum(Xuu*normal,axis=0)
        curv=np.linalg.eigvalsh(np.stack([np.stack([L,M/a],axis=-1),
                                         np.stack([M/a,N/a**2],axis=-1)],axis=-2))
        radial=np.sqrt(X[0]**2+X[1]**2)
        theta=np.unwrap(np.arctan2(X[1],X[0]))
        rows.append(dict(s=float(s),a=float(a),ap=float(ap),app=float(app),
                         N_min=float(N.min()),N_max=float(N.max()),
                         N_relstd=float(N.std()/N.mean()),M_max=float(np.max(np.abs(M))),
                         radius_min=float(radial.min()),radius_max=float(radial.max()),
                         height_min=float(X[2].min()),height_max=float(X[2].max()),
                         kappa_max=float(np.max(np.abs(curv))),
                         coordinate_error=float(np.max(np.linalg.norm(Xu-a*e2,axis=0))),
                         N_error=float(np.max(np.abs(N-Nr))),
                         frame_error=float(max(np.max(abs(np.sum(e1*e1,axis=0)-1)),
                                               np.max(abs(np.sum(e2*e2,axis=0)-1)),
                                               np.max(abs(np.sum(e1*e2,axis=0)))))))
    result=dict(params=dict(A=A,B=B,n=n,c=c,smax=smax,mode=mode,k=k,p=p,ramp=ramp,rtol=rtol,atol=atol),
                a0=a0,success=sol.success,message=sol.message,nfev=sol.nfev,
                endpoint=sol.t[-1],rows=rows)
    if output:
        with open(output,'w') as f:json.dump(result,f,indent=2)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=96)
    parser.add_argument('--c',type=float,default=4.)
    parser.add_argument('--smax',type=float,default=.5)
    parser.add_argument('--mode',choices=['constant','cosine','power','ramped_cosine'],default='constant')
    parser.add_argument('--k',type=float,default=0.)
    parser.add_argument('--p',type=float,default=1.)
    parser.add_argument('--ramp',type=float,default=.03)
    parser.add_argument('--output')
    args=parser.parse_args()
    r=evolve(**vars(args))
    print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
    print('s radius_min radius_max height_max kappa_max N_min N_relstd coorderr')
    for x in r['rows']:
        print(' '.join(f'{x[k]:.8g}' for k in ['s','radius_min','radius_max','height_max','kappa_max','N_min','N_relstd','coordinate_error']))
