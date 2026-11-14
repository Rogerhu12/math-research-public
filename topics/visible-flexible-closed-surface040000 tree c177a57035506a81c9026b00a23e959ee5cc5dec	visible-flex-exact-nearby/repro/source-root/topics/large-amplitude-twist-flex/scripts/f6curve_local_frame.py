"""Equivalent cylindrical-frame evaluation of the spatial Frenet ODE.
Astra curve_transition, AI-assisted 2026-11-08. This is a floating-point
evaluation change, not a changed geometric equation. It removes the pure
background before Fourier projection and uses extended precision only where
the physical perturbation is tiny. Cartesian output/audit is unchanged.
"""
import types
import numpy as np
from scipy.interpolate import PPoly

def local_basis(obj,N):
    theta=2*np.pi*np.arange(N)/N;B=np.zeros((obj.n,N,3));D=B.copy();DD=B.copy();B[0,:,0]=1.;D[0,:,1]=1.;DD[0,:,0]=-1.
    for j,m in enumerate(obj.even):
        co=np.cos(m*theta);si=np.sin(m*theta);r=1+j;t=obj.M+1+j;z=obj.iz+j
        B[r,:,0]=co;D[r,:,0]=-m*si;D[r,:,1]=co;DD[r,:,0]=-(m*m+1)*co;DD[r,:,1]=-2*m*si
        B[t,:,1]=si;D[t,:,0]=-si;D[t,:,1]=m*co;DD[t,:,0]=-2*m*co;DD[t,:,1]=-(m*m+1)*si
        B[z,:,2]=co;D[z,:,2]=-m*si;DD[z,:,2]=-m*m*co
    return B,D,DD

def project_local(F,B):
    mean=np.mean(F,axis=1);osc=F-mean[:,None,:]
    ans=np.einsum('npc,kpc->kn',osc,B,optimize=True)/np.sum(B*B,axis=(1,2))[:,None]
    ans[0]=mean[:,0];return ans

def frame_groups(obj,s,y):
    # Variation is assessed before adding the O(1) background radius.
    amp=obj.q*np.max(abs(y),axis=0);weak=amp<1e-6
    for flag in (False,True):
        indices=np.flatnonzero(weak==flag)
        for first in range(0,len(indices),192):
            ix=indices[first:first+192];dtype=np.clongdouble if np.iscomplexobj(y) else np.longdouble
            yy=y[:,ix].astype(dtype) if flag else y[:,ix]
            C=obj.base(s[ix]).astype(yy.dtype)+obj.q*yy
            yield ix,obj.frame(s[ix],C,obj.LB1,obj.LB2)

def local_fun(self,s,y,p):
    self.calls+=1;s=np.asarray(s);out=np.empty(y.shape,dtype=y.dtype)
    for ix,fr in frame_groups(self,s,y):
        V=fr['V'].copy();V[:,:,0]-=fr['ap'][:,None]
        out[:,ix]=np.asarray(project_local(V,self.LB)/self.q,dtype=y.dtype)
    return out

def local_fun_jac(self,s,y,p):
    s=np.asarray(s);out=np.empty((self.n,self.n,len(s)))
    # The Jacobian itself is not a tiny difference from a background; use
    # ordinary precision with bounded batches and the same local equations.
    for first in range(0,len(s),128):
        sl=slice(first,first+128);C=self.base(s[sl])+self.q*y[:,sl];fr=self.frame(s[sl],C,self.LB1,self.LB2)
        for j in range(self.n):
            dv=self.frame_jvp(fr,self.LB1[j][None,:,:],self.LB2[j][None,:,:]);out[:,j,sl]=project_local(dv,self.LB)
    return out,np.zeros((self.n,self.M,len(s)))

def local_c2_interpolant(self,sol):
    s=sol.x;y=sol.y;dy=local_fun(self,s,y,sol.p);ddy=np.empty_like(y)
    for ix,fr in frame_groups(self,s,y):
        Cp=self.base(s[ix],1).astype(fr['V'].dtype)+self.q*dy[:,ix]
        dV=self.frame_jvp(fr,self.values(Cp,self.LB1),self.values(Cp,self.LB2))
        ae=-fr['app'][:,None]/(fr['a'][:,None]*fr['kap'])+fr['ap'][:,None]**2/(fr['a'][:,None]**2*fr['kap']);be=-fr['alpha']*ae/fr['beta'];dV+=ae[:,:,None]*fr['N']+be[:,:,None]*fr['Bin'];dV[:,:,0]-=fr['app'][:,None]
        ddy[:,ix]=np.asarray(project_local(dV,self.LB)/self.q,float)
    Y=y.astype(np.longdouble).T;D=dy.astype(np.longdouble).T;Q=ddy.astype(np.longdouble).T;h=np.diff(s).astype(np.longdouble)[:,None]
    e0=Y[1:]-Y[:-1]-h*D[:-1]-h*h*Q[:-1]/2;e1=D[1:]-D[:-1]-h*Q[:-1];e2=Q[1:]-Q[:-1]
    u=10*e0-4*h*e1+h*h*e2/2;v=-15*e0+7*h*e1-h*h*e2;w=6*e0-3*h*e1+h*h*e2/2
    c=np.stack((w/h**5,v/h**4,u/h**3,Q[:-1]/2,D[:-1],Y[:-1])).astype(float)
    return PPoly.construct_fast(c,s,extrapolate=True,axis=1)

def install_local_frame(obj):
    obj.LB,obj.LB1,obj.LB2=local_basis(obj,obj.nt)
    obj.fun=types.MethodType(local_fun,obj);obj.fun_jac=types.MethodType(local_fun_jac,obj);obj.c2_interpolant=types.MethodType(local_c2_interpolant,obj)
    obj.local_frame=True;return obj

if __name__=='__main__':
    import json
    from pathlib import Path
    from f6curve_outward_bvp import OutwardPrefix
    o=OutwardPrefix(6,.0075,angular=384,compute_stable=False);s=np.array([.002,.016,.35,.5,1.1,1.218]);rng=np.random.default_rng(20261108)
    y=rng.normal(size=(o.n,len(s)))*1e-7;y[o.iz]=.001;y[1]=-.0006;y[o.M+1]=.0001
    old=o.fun(s,y,np.zeros(o.M));Jold=o.fun_jac(s,y,np.zeros(o.M))[0];install_local_frame(o);new=o.fun(s,y,np.zeros(o.M));Jnew=o.fun_jac(s,y,np.zeros(o.M))[0]
    direction=rng.normal(size=y.shape);actual=o.fun(s,y.astype(complex)+1e-25j*direction,np.zeros(o.M)).imag/1e-25;pred=np.einsum('ijk,jk->ik',Jnew,direction)
    zero=o.fun(s,np.zeros_like(y),np.zeros(o.M));row=dict(scope=__doc__,flow_difference=float(abs(new-old).max()),jacobian_difference=float(abs(Jnew-Jold).max()),complex_step_error=float(abs(actual-pred).max()),complex_step_relative=float(abs(actual-pred).max()/max(1,abs(actual).max())),pure_background_nonmean=float(abs(zero[1:]).max()),pure_background_mean=float(abs(zero[0]).max()))
    path=Path(__file__).parent.parent/'notes/f6curve_local_frame_check.json';path.write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row,indent=2))
