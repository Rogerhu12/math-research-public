"""Full-column relative Gram and shell differential with explicit material Rayleigh cuts."""
from __future__ import annotations
import math

import numpy as np
from scipy.linalg import qr, svd
from scipy.optimize import minimize

from r675_bowed_endpoint_pose_response_20261128 import dot
from r685_hard_moment_physical_pose_20261128 import RadialQR, as_grid, metric_defect, operators, reordered
from r691_same_metric_bowed_pose_continuation_20261128 import Problem, physical_state, positive, tensors, weights_grid


def gram_inverse(raw,r):
    D,Y=raw[1],raw[2]/r[:,None,None]
    a=dot(D,D);f=dot(D,Y);b=dot(Y,Y);m=f/a
    return np.sqrt(a),m,np.sqrt(b-m*f)


def whitened(vals,co):
    sa,m,sh=co
    x,y,z=vals
    return np.stack((x/sa**2,(y-m*x)/(sa*sh),(z-2*m*y+m*m*x)/sh**2))


def local_rows(sp,x,g,q,guards,opt,indices,jacobian):
    raw=physical_state(sp,x,g,q);co=gram_inverse(g['raw'],g['r'])
    metric=whitened(metric_defect(raw,g['raw'],g['r']),co)
    w,ww=weights_grid(g);vals,der=tensors(raw,g['r'],opt['T'])
    out=[(metric*ww).ravel()]
    if jacobian:
        ids,A,B=operators(sp,g,raw,indices)
        Ap=whitened(A,[v[...,None] for v in co]);n=len(ids)
        jac=[(Ap*ww[...,None]).reshape(-1,n)]
    for val,guard,(dc,db) in zip(vals,guards,der,strict=True):
        res,factor=positive(guard-val,opt['smooth_width'])
        mask=factor>0
        if mask.any():
            out.append((w*opt['cone_weight']*res)[mask])
            if jacobian:
                dval=sum(a[mask,None]*A[k][mask]+b[mask,None]*B[k][mask] for k,(a,b) in enumerate(zip(dc,db)))
                jac.append(-(w*factor*opt['cone_weight'])[mask,None]*dval)
    vec=np.concatenate(out)
    if not jacobian:
        return float(vec@vec)
    return ids,np.column_stack((np.vstack(jac),vec)),np.column_stack(((B*ww[...,None]).reshape(-1,n),np.zeros(B.shape[0]*B.shape[1]*B.shape[2])))


class RelativeProblem(Problem):
    def matrices(self,x,check=False):
        sp=self.sp;left=RadialQR(sp.size,self.count);right=RadialQR(sp.size,self.count)
        if check:
            y=np.cos(.417*np.arange(1,sp.size+1));y/=np.linalg.norm(y)
            d=y[np.argsort(reordered(sp))]
            first=0.;fd=np.zeros(2);steps=(1.2e-9,3.e-10)
        for g,guards,active,stop in self.data:
            ids,A,B=local_rows(sp,x,g,self.q,guards,self.opts,active,True)
            if check:
                first+=2*A[:,-1]@(A[:,:-1]@y[ids])
                for j,h in enumerate(steps):
                    a=local_rows(sp,x+h*d,g,self.q,guards,self.opts,active,False)
                    b=local_rows(sp,x-h*d,g,self.q,guards,self.opts,active,False)
                    fd[j]+=(a-b)/(2*h)
            ids=np.r_[ids,sp.size];left.add(ids,A,stop);right.add(ids,B,stop)
        if left.carry.size or right.carry.size:raise ArithmeticError('Nonempty radial factor carry.')
        self.count['new_complete_relative_matrices']+=1;self.count['all_bulk_columns']+=sp.size
        checks=(abs(fd-first)/max(abs(first),1e-14)).tolist() if check else []
        return left.square,right.square,checks

    def merit(self,x):
        return sum(local_rows(self.sp,x,g,self.q,guards,self.opts,active,False)
                   for g,guards,active,_ in self.data)


def rays(sp,x,g,q,options,one=False):
    """Source-unit covectors are fixed from actual current/trial extrema, on the closed reflection half."""
    raw=physical_state(sp,x,g,q);r=g['r'];phi=g['phi']
    sa,m,sh=gram_inverse(g['raw'],r)
    a,b,c=whitened(metric_defect(raw,g['raw'],r),(sa,m,sh))
    arr=np.empty(a.shape+(2,2));arr[...,0,0]=a;arr[...,0,1]=b;arr[...,1,0]=b;arr[...,1,1]=c
    val,V=np.linalg.eigh(arr)
    ii=np.flatnonzero(phi<=math.pi+1e-14)
    mag=abs(val[:,ii]);rank=np.argsort(-mag.ravel())
    best=mag.ravel()[rank[0]];seen=set();out=[]
    for flat in rank:
        i,j,k=np.unravel_index(flat,mag.shape);j=ii[j]
        if abs(val[i,j,k])<options['peak_floor']*best:break
        key=(int(np.searchsorted(sp.edges,r[i],side='right')),int(phi[j]/math.pi*options['angular_sectors']),int(k))
        if key in seen:continue
        seen.add(key)
        u,v=V[i,j,:,k];d=u/sa[i,j]-m[i,j]*v/sh[i,j];h=v/sh[i,j]
        out.append((float(r[i]),float(phi[j]),float(d),float(h),float(np.sign(val[i,j,k]) or 1.)))
        if one or len(out)>=options['maximum_initial_rays']:break
    return out


def ray_rows(sp,x,q,witnesses):
    """Return signed actual values and complete parameter rows, in radial-major order."""
    result=np.zeros((len(witnesses),sp.size));values=[]
    for i,(r,f,v,w,sgn) in enumerate(witnesses):
        g=as_grid(sp,np.array([r]),np.array([f]),np.ones(1))
        raw=physical_state(sp,x,g,q);active=np.flatnonzero(g['b'][0][0]!=0)
        # A basis may vanish at a knot while its first or second jet is supported.
        active=np.union1d(active,np.flatnonzero((g['b'][1][0]!=0)|(g['b'][2][0]!=0)))
        ids,A,_=operators(sp,g,raw,active)
        weights=sgn*np.array([v*v,2*v*w,w*w])
        result[i,ids]=weights@A[:,0,0]
        defect=np.asarray(metric_defect(raw,g['raw'],g['r']))[:,0,0]
        values.append(float(weights@defect))
    return np.asarray(values),result


class CompletePencil:
    """The scaled full SVD supplies a positive primal metric and a small convex dual."""
    def __init__(self,A,B,mu,ridge):
        F=np.asfortranarray(np.vstack((A[:,:-1],mu*B[:,:-1])))
        rhs=np.r_[A[:,-1],mu*B[:,-1]]
        self.scale=np.linalg.norm(F,axis=0);self.scale[self.scale==0]=1.;F/=self.scale
        Q,R=qr(F,mode='economic',overwrite_a=True,check_finite=False)
        force=Q.T@rhs;del Q,F
        U,self.s,self.V=svd(R,full_matrices=False,check_finite=False)
        self.ridge=ridge*max(1.,float(self.s[0]))
        self.den=np.hypot(self.s,self.ridge)
        self.y0=-(self.s/self.den)*(U.T@force)

    def direction(self,C,h):
        M=((C/self.scale)@self.V.T)/self.den
        lens=np.linalg.norm(M,axis=1)
        if np.any((lens==0)&(h<0)):return None,dict(reason='nonpositive immovable active bound')
        keep=lens>0;M=M[keep]/lens[keep,None];h=h[keep]/lens[keep]
        delta=M@self.y0-h
        if len(delta) and delta.max()>0:
            unit=max(np.max(abs(delta)),1e-30);f=delta/unit;gram=M@M.T
            def fun(z):
                w=gram@z
                return .5*z@w-f@z,w-f
            sol=minimize(fun,np.zeros(len(f)),jac=True,method='L-BFGS-B',bounds=[(0.,None)]*len(f),
                         options=dict(ftol=1e-15,gtol=2e-10,maxiter=1000,maxls=70))
            y=self.y0-unit*(M.T@sol.x)
            remaining=float(max(0.,np.max(M@y-h))/unit)
            info=dict(dual_iterations=int(sol.nit),dual_converged=bool(sol.success),scaled_cut_excess=remaining)
        else:y=self.y0;info=dict(dual_iterations=0,dual_converged=True,scaled_cut_excess=0.)
        return (self.V.T@(y/self.den))/self.scale,info


def true_l2_row(sp,x,g,q):
    """Exact adjoint of the reported unwhitened quadrature L2, without a truncated basis."""
    r=g['r'][:,None,None];raw=physical_state(sp,x,g,q);D,Y=raw[1],raw[2]/r
    e,f,b=metric_defect(raw,g['raw'],g['r'])
    ww=g['weights'][:,None]/len(g['phi'])
    value=np.sqrt(np.sum(ww*(e*e+2*f*f+b*b)))
    if value==0:return 0.,np.zeros(sp.size)
    fac=(2*ww/value)[...,None]
    dr=fac*(e[...,None]*D+f[...,None]*Y)
    dp=fac*(f[...,None]*D+b[...,None]*Y)/r
    result=np.empty(sp.size)
    for i,(coord,k) in enumerate(sp.blocks):
        s,s1,_=sp.angular(coord,k,g['phi'])
        result[i*sp.nb:(i+1)*sp.nb]=g['b'][1].T@(dr[...,coord]@s)+g['b'][0].T@(dp[...,coord]@s1)
    for j,coord in enumerate((0,2)):result[-2+j]=sp.scale*g['chi'][1]@dr[...,coord].sum(axis=1)
    return float(value),result[reordered(sp)]
