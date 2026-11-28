#!/usr/bin/env python3
"""True-cuff full finite phase-zero core, exact slab/ball/witness-hole transforms, analytic physical first/second jets and full principal-curvature pullback."""
import argparse,importlib.util,sys
from pathlib import Path
from math import comb
import numpy as np
p=Path(__file__).with_name('2ecf-r289-slab-ball-full-chain.py');s=importlib.util.spec_from_file_location('r289_main_delta',p);k=importlib.util.module_from_spec(s);s.loader.exec_module(k);m,v=k.m,k.v;dot=k.dot

def upper(r):
    return k.cap(r,1635/1024,2/1024)
def lower(r):
    width=.01;h=.65;t=np.maximum((h+width-r)/width,0.);P=1+t+t*t+t**3;D=1+2*t+3*t*t;D2=2+6*t;active=r<h+width
    return (np.where(active,h+width/P,r),D/P**2,np.where(active,(2*D**2/P**3-D2/P**2)/width,0),np.where(active,(6*D**3/P**4-6*D*D2/P**3+6/P**2)/width**2,0))
def evaluate(J,yc,upper_map=False):
    center=np.array([0.,yc,0.]);P,Ps,Pu,Pss,Psu,Puu=J.swapaxes(0,1);p=P-center;r=np.linalg.norm(p,axis=-1);active=r>1635/1024 if upper_map else r<.66
    if not np.any(active):return J
    q=r[active];p=p[active];t,t1,t2,_=(upper if upper_map else lower)(q);A=t/q;A1=(t1-A)/q;A2=(t2-2*A1)/q;out=J.copy();o=out.swapaxes(0,1);o[0][active]=center+A[:,None]*p;D=[dot(p,Ps[active])/q,dot(p,Pu[active])/q]
    for j,b in enumerate((Ps,Pu)):o[j+1][active]=A[:,None]*b[active]+(A1*D[j])[:,None]*p
    for j,(a,b,sec) in enumerate(((0,0,Pss),(0,1,Psu),(1,1,Puu))):
        x,y=(Ps,Pu)[a][active],(Ps,Pu)[b][active];z=sec[active];dd=(dot(x,y)+dot(p,z)-D[a]*D[b])/q
        o[j+3][active]=A[:,None]*z+(A1*D[b])[:,None]*x+(A1*D[a])[:,None]*y+(A1*dd+A2*D[a]*D[b])[:,None]*p
    return out

def radial_pull(c,j,yc,upper_map=False):
    shifted=j.copy();shifted[0,:,1]-=yc;p,ps,pu,pss,psu,puu=shifted;r=np.linalg.norm(p,axis=-1);hit=r>1635/1024 if upper_map else r<.66
    if not np.any(hit):return c
    x=p[hit];r=r[hit];f,g,gg,ggg=(upper if upper_map else lower)(r);a=f/r;ap=(g-a)/r;app=(gg-2*ap)/r;appp=(ggg-3*app)/r;h=ap/r;h2=(app-h)/r**2;h3=(appp-3*app/r+3*ap/r**2)/r**3;mul=lambda v,z:v[:,None]*z
    def M(q):return mul(a,q)+mul(h*dot(x,q),x)
    def T(q,z):
        xq=dot(x,q);xz=dot(x,z);return mul(h,mul(dot(q,z),x)+mul(xq,z)+mul(xz,q))+mul(h2*xq*xz,x)
    def W(q,z,w):
        xq,xz,xw=dot(x,q),dot(x,z),dot(x,w);qz,qw,zw=dot(q,z),dot(q,w),dot(z,w)
        return mul(h,mul(qz,w)+mul(qw,z)+mul(zw,q))+mul(h2,mul(xz*xw,q)+mul(xq*xw,z)+mul(xq*xz,w)+mul(qz*xw+qw*xz+zw*xq,x))+mul(h3*xq*xz*xw,x)
    q,qs,qu,qss,qsu,quu=c[:,hit].copy();ps,pu,pss,psu,puu=[t[hit] for t in (ps,pu,pss,psu,puu)];c[0,hit]=M(q)+T(qs,ps)+T(qu,pu)+T(qss,pss)+T(qsu,psu)+T(quu,puu)+W(qss,ps,ps)+W(qsu,ps,pu)+W(quu,pu,pu);c[1,hit]=M(qs)+2*T(qss,ps)+T(qsu,pu);c[2,hit]=M(qu)+T(qsu,ps)+2*T(quu,pu)
    for i,q in enumerate((qss,qsu,quu),3):c[i,hit]=M(q)
    return c

def install(A):
    def allmaps(J):return evaluate(evaluate(evaluate(J,0,True),A),-A)
    def allpull(c,row):
        j=row[None];first=evaluate(j,0,True);second=evaluate(first,A);c=radial_pull(c,second[0],-A);c=radial_pull(c,first[0],A);return radial_pull(c,row,0,True)
    def slab(J):
        new=J.copy();p,ps,pu,pss,psu,puu=J[...,1].swapaxes(0,1);g,a,b,c=k.cap(abs(p),399/512,117/1024);b*=np.sign(p);new[:,0,:,1]=np.sign(p)*g;new[:,1,:,1]=a*ps;new[:,2,:,1]=a*pu;new[:,3,:,1]=a*pss+b*ps*ps;new[:,4,:,1]=a*psu+b*ps*pu;new[:,5,:,1]=a*puu+b*pu*pu;return new,(a,b,c)
    k.ball=allmaps;k.radius_pull=allpull;k.slab=slab;m.Fit=k.Fit;v.step=k.step;v.__file__=__file__
if __name__=='__main__':
    p=argparse.ArgumentParser(add_help=False)
    for key in ('meridian','buffer','tail-table'):p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--index',type=int,default=0);p.add_argument('--epsilon',type=float,required=True);p.add_argument('--stadium-p',type=int,default=32);p.add_argument('--stadium-mix',type=float,required=True);args,_=p.parse_known_args();src=m.Source(args);pw=args.stadium_p;c=np.array([2*(-1)**j*comb(2*pw,pw-j)/comb(2*pw,pw)/(1-4*j*j) for j in range(1,pw+1)]);A=src.R+args.epsilon*((1-args.stadium_mix)+args.stadium_mix*c.sum()/c[::2].sum());install(A);v.main()
