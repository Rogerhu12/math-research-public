"""Seed the three-field BVP with a genuine GC prefix plus a blended tail.

The blended tail is deliberately only an optimization initializer, not an
isometric cap. Its residual is reported before and after optimization.
"""
import argparse,json
import numpy as np
from scipy.integrate import solve_ivp,cumulative_trapezoid,simpson
from scipy.optimize import brentq
from gc_bvp import Problem,smooth5
from gc_prefix_explore import initial


def hermite6(y,dy,ddy,y1=0.,dy1=0.,ddy1=0.):
    c=np.zeros(6);c[:3]=[y,dy,ddy/2]
    A=np.array([[1,1,1],[3,4,5],[6,12,20]],float)
    b=np.array([y1-c[:3].sum(),dy1-c[1]-2*c[2],ddy1-2*c[2]])
    c[3:]=np.linalg.solve(A,b)
    return c


def seed(pr,length=1.8,prefix=.28,c=4.,k=10.,ramp=.03):
    nu=pr.nu;a0,y0=initial(pr.A,pr.B,nu);freq=np.fft.fftfreq(nu,1/nu)
    def du(a):return np.fft.ifft(1j*freq*np.fft.fft(a,axis=-1),axis=-1).real
    def profile(s):
        if s<=ramp:
            x=np.pi*s/ramp
            return (a0+c*(s*s/4+ramp*ramp/(2*np.pi*np.pi)*(np.cos(x)-1)),
                    c*(s/2-ramp/(2*np.pi)*np.sin(x)),c*(1-np.cos(x))/2,
                    c*np.pi/(2*ramp)*np.sin(x))
        t=s-ramp
        p0=c*ramp/2;a1=a0+c*ramp*ramp*(1/4-1/np.pi**2)
        return a1+p0*t+c*(1-np.cos(k*t))/k**2,p0+c*np.sin(k*t)/k,c*np.cos(k*t),-c*k*np.sin(k*t)
    def rhs(s,y):
        a,ap,app,_=profile(s);M=y[:nu];N=y[nu:]
        L=(M*M-a*app)/N
        return np.r_[du(L)-ap/a*M,du(M)+ap/a*N+a*ap*L]
    sol=solve_ivp(rhs,[0,prefix],y0[:2*nu],method='DOP853',rtol=2e-11,atol=2e-12,max_step=.002,dense_output=True)
    v=sol.sol(prefix);dv=rhs(prefix,v);M0,N0=v[:nu],v[nu:];Ms0,Ns0=dv[:nu],dv[nu:]
    a,ap,app,appp=profile(prefix);w=np.sqrt(1-ap*ap)
    L0=(M0*M0-a*app)/N0
    Ls0=(2*M0*Ms0-ap*app-a*appp)/N0-L0*Ns0/N0
    theta0=-np.arcsin(ap);thetaS=-app/w;thetaSS=-appp/w-ap*app*app/w**3
    tail=length-prefix
    ctheta=hermite6(theta0,thetaS*tail,0.,np.pi/2,0,0)
    tf=np.linspace(0,1,4001);bump=64*tf**3*(1-tf)**3
    base=np.polynomial.polynomial.polyval(tf,ctheta)
    def eq(amp):return tail*simpson(np.sin(base+amp*bump),x=tf)-(a-pr.rc)
    grid=np.linspace(-3,3,121);roots=[]
    for x,y in zip(grid[:-1],grid[1:]):
        if eq(x)*eq(y)<0:roots.append(brentq(eq,x,y))
    if not roots:raise RuntimeError('No tail angle correction closes radius at requested length')
    def root_cost(amp):
        th=base+amp*bump
        return 10*max(th.max()-np.pi/2,0)+10*max(-th.min()-.6,0)+.1*abs(amp)
    amp=min(roots,key=root_cost);theta=base+amp*bump
    ztail=tail*cumulative_trapezoid(np.cos(theta),tf,initial=0)
    atail=a-tail*cumulative_trapezoid(np.sin(theta),tf,initial=0)
    thetad=np.gradient(theta,tf,edge_order=2)/tail
    # Nonradial differences retain the prefix value and derivative, and
    # vanish with two derivatives at the prospective planar end.
    delta0=[L0+app/w,M0,N0-a*w]
    delta1=[Ls0-Ls0.mean(),Ms0,Ns0-(ap*w-a*ap*app/w)]
    basis0=np.polynomial.polynomial.polyval(tf,hermite6(1.,0.,0.))
    basis1=np.polynomial.polynomial.polyval(tf,hermite6(0.,1.,0.))
    x=np.linspace(0,1,max(801,30*pr.nc));s=length*x
    aval=np.zeros(len(x));Lv=np.zeros((len(x),nu));Mv=Lv.copy();Nv=Lv.copy()
    for j,ss in enumerate(s):
        if ss<=prefix:
            aa,pp,dd,_=profile(ss);y=sol.sol(ss)
            mm,nn=y[:nu],y[nu:]
            aval[j]=aa;Lv[j]=(mm*mm-aa*dd)/nn;Mv[j]=mm;Nv[j]=nn
        else:
            t=(ss-prefix)/tail
            aa=np.interp(t,tf,atail);th=np.interp(t,tf,theta);thd=np.interp(t,tf,thetad)
            h0=np.interp(t,tf,basis0);h1=np.interp(t,tf,basis1)
            vals=[thd+delta0[0]*h0+tail*delta1[0]*h1,
                  delta0[1]*h0+tail*delta1[1]*h1,
                  aa*np.cos(th)+delta0[2]*h0+tail*delta1[2]*h1]
            aval[j]=aa;Lv[j],Mv[j],Nv[j]=vals
    B=pr.sp(x);p=np.zeros(pr.nvar);p[-1]=length
    def angular_projection(vals,trig):
        coeff=vals@trig*2/nu
        if trig.shape[1] and np.all(trig[:,0]==1):coeff[:,0]/=2
        return coeff
    lcoef=angular_projection(Lv,pr.C);mcoef=angular_projection(Mv,pr.Si)
    nv=Nv-(1-smooth5(x))[:,None]*pr.Ninitial
    ncoef=angular_projection(nv,pr.C)
    p[pr.sl[0]]=np.linalg.lstsq(B@pr.ZL,lcoef,rcond=None)[0].ravel()
    p[pr.sl[1]]=np.linalg.lstsq(B@pr.ZMN,mcoef,rcond=None)[0].ravel()
    p[pr.sl[2]]=np.linalg.lstsq(B@pr.ZMN,ncoef,rcond=None)[0].ravel()
    apart=B@(pr.apart+length*pr.apartS)
    p[pr.sl[3]]=np.linalg.lstsq(B@pr.Za,aval-apart,rcond=None)[0]
    info=dict(prefix=prefix,tail_angle_correction=amp,theta_min=float(theta.min()),theta_max=float(theta.max()),
              tail_height=float(ztail[-1]),seed_radius_end=float(atail[-1]),prefix_N_min=float(N0.min()))
    return p,info


if __name__=='__main__':
    ag=argparse.ArgumentParser();ag.add_argument('--B',type=float,default=.9)
    ag.add_argument('--nc',type=int,default=24);ag.add_argument('--K',type=int,default=4)
    ag.add_argument('--length',type=float,default=1.8);ag.add_argument('--prefix',type=float,default=.28)
    ag.add_argument('--max-nfev',type=int,default=400);ag.add_argument('--output',default='gc_bvp_prefixseed.json')
    args=ag.parse_args();pr=Problem(B=args.B,nc=args.nc,K=args.K,length_max=args.length)
    p,info=seed(pr,length=args.length,prefix=args.prefix)
    print(json.dumps(dict(stage='initial',**info,**pr.evaluate(p)[2])),flush=True)
    p,stats=pr.solve(p,max_nfev=args.max_nfev)
    pr.save(args.output,p,stats)
    print(json.dumps(dict(stage='final',**stats)),flush=True)
