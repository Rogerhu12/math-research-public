#!/usr/bin/env python3
"""R289 exact whole-core slab and ball maps; physical metric/curvature optimization on their complete Cartesian images."""
import importlib.util,os
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.linalg import solve
p=Path(__file__).with_name('2ecf-r262-m2-low-cap-stadium-active.py');s=importlib.util.spec_from_file_location('true_r289_obj',p);v=importlib.util.module_from_spec(s);s.loader.exec_module(v);m=v.m;dot=v.dot;OldFit=m.Fit

def cap(r,threshold,width):
    t=np.maximum(r-threshold,0);q=t/width;A=1+q**4;g=np.where(r>threshold,threshold+t*A**(-.25),r);g1=A**(-1.25);g2=-5*q**3/width*A**(-2.25);g3=(-15*q**2*A**(-2.25)+45*q**6*A**(-3.25))/width**2;return g,g1,g2,g3

def slab(J):
    new=J.copy();p,ps,pu,pss,psu,puu=J[...,1].swapaxes(0,1);f,d1,d2,d3=cap(abs(p),.78,.114);d2*=np.sign(p)
    new[:,0,:,1]=np.sign(p)*f;new[:,1,:,1]=d1*ps;new[:,2,:,1]=d1*pu
    new[:,3,:,1]=d1*pss+d2*ps*ps;new[:,4,:,1]=d1*psu+d2*ps*pu;new[:,5,:,1]=d1*puu+d2*pu*pu
    return new,(d1,d2,d3)
def ball(J):
    P,Ps,Pu,Pss,Psu,Puu=J.swapaxes(0,1);r=np.linalg.norm(P,axis=-1);active=r>1.596
    if not np.any(active):return J
    q=r[active];p=P[active];t,t1,t2,_=cap(q,1.596,.003);A=t/q;A1=(t1-A)/q;A2=(t2-2*A1)/q
    out=J.copy();out0=out.swapaxes(0,1);out0[0][active]=A[:,None]*p;D=[dot(p,Ps[active])/q,dot(p,Pu[active])/q]
    for k,b in enumerate((Ps,Pu)):out0[k+1][active]=A[:,None]*b[active]+(A1*D[k])[:,None]*p
    for j,(i,k,second) in enumerate(((0,0,Pss),(0,1,Psu),(1,1,Puu))):
        x,y=(Ps,Pu)[i][active],(Ps,Pu)[k][active];z=second[active];dd=(dot(x,y)+dot(p,z)-D[i]*D[k])/q
        out0[j+3][active]=A[:,None]*z+(A1*D[k])[:,None]*x+(A1*D[i])[:,None]*y+(A1*dd+A2*D[i]*D[k])[:,None]*p
    return out
class Fit(OldFit):
    def field(self,x):return ball(slab(super().field(x))[0])

def step(g,x,mu,guide,reg,power):
    # This physical proposal uses all slab derivatives. The ball is also applied to every true trial.
    raw=OldFit.field(g,x);J,(s1,s2,s3)=slab(raw);Cmax=float(np.linalg.norm(J[:,0],axis=-1).max())
    if Cmax>1.596:raise ValueError('Active ball Hessian at a training state requires its full directional proposal')
    V,U=J[:,1],J[:,2];R=g.bb;E,F,G=dot(V,V)-1,dot(V,U)/R,dot(U,U)/R**2-1;er=abs(E+G)/2+np.hypot((E-G)/2,F);K,dK=v.curve(J);kp=np.maximum(abs(K)-guide,0);n=x.size;H=np.zeros((n,n));rhs=np.zeros(n);ks=max(.1,float(kp.max()));peak=max(er.max(),1e-12)
    for i in range(len(g.z)):
        ids=np.nonzero(abs(g.B[0][i])+abs(g.B[1][i])+abs(g.B[2][i])>1e-15)[0]
        if not len(ids):continue
        ix=(ids[:,None]*g.na+np.arange(g.na)).ravel();rho=R[i];ys,yu,yss,ysu,yuu=raw[i,1:,:,1];d1,d2,d3=s1[i],s2[i],s3[i];N=len(g.t);q,ds,dd=[b[i,ids] for b in g.B]
        def pull(c):
            # c is an array of six true jet covectors; pull it through the physical coordinate map.
            y=c[:,:,1];p0,cs,cu,ss,su,uu=y.copy();y[0]=d1*p0+d2*(cs*ys+cu*yu+ss*yss+su*ysu+uu*yuu)+d3*(ss*ys**2+su*ys*yu+uu*yu**2);y[1]=d1*cs+d2*(2*ss*ys+su*yu);y[2]=d1*cu+d2*(su*ys+2*uu*yu);y[3:]*=d1
            return sum(rad[None,:,None]*np.einsum('uc,uac->ua',vv,g.ang[j])[:,None,:] for vv,rad,j in zip(c,(q,ds,q,dd,ds,q),(0,0,1,0,1,2)))
        empty=lambda:np.zeros((6,N,3));c=empty();c[1]=2*V[i];je=pull(c);c=empty();c[1]=np.sqrt(2)*U[i]/rho[:,None];c[2]=np.sqrt(2)*V[i]/rho[:,None];jf=pull(c);c=empty();c[2]=2*U[i]/rho[:,None]**2;jg=pull(c)
        w=np.sqrt(.03+(er[i]/peak)**power);jj=(np.stack([je,jf,jg],axis=1)*w[:,None,None,None]).reshape(3*N,-1);rr=(np.stack([E[i],np.sqrt(2)*F[i],G[i]],axis=1)*w[:,None]).ravel();hh=jj.T@jj;vv=jj.T@rr
        active=kp[i]>0
        if np.any(active):
            c=empty();c[1:]=np.stack([z[i] for z in dK]);row=pull(c)[active];w=mu*np.sqrt(.1+(kp[i,active]/ks)**power);jj=(w[:,None,None]*row).reshape(len(w),-1);rr=w*np.sign(K[i,active])*kp[i,active];hh+=jj.T@jj;vv+=jj.T@rr
        H[np.ix_(ix,ix)]+=hh;rhs[ix]+=vv
    sc=np.maximum(np.sqrt(np.diag(H)),1e-13);return (solve(H/sc[:,None]/sc[None,:]+reg*np.eye(n),-rhs/sc,assume_a='pos')/sc).reshape(x.shape)
if __name__=='__main__':
    m.Fit=Fit;v.step=step;v.__file__=__file__;v.main()
