"""Exact flat-tail family with a step and C4 Chebyshev bubble parameters.

coefficients = [A,b_0,...,b_(K-1)] and
alpha(y) = sign(y) [A*S9(q) + sum b_j*1024*q^5*(1-q)^5*T_j(2q-1)],
q=(abs(y)-flat_radius)/(cut_radius-flat_radius).
S9 is clipped, and all bubbles are zero outside (0,1).

The metric identity is exact for all coefficients.  Positive horizontal
projection and the geometric budgets are separate conditions, never imposed
by deleting a coefficient or by replacing the mathematical field.
"""

from __future__ import annotations
from functools import lru_cache
import numpy as np


@lru_cache(maxsize=8)
def _gauss(order):
    nodes, weights = np.polynomial.legendre.leggauss(int(order))
    nodes.flags.writeable = False
    weights.flags.writeable = False
    return nodes, weights


def angle_basis(q, bubble_count):
    """Return value, d/dq and d²/dq² of [S9,B0,...].

    Last axis is the parameter axis.  The recursion differentiates T_j(2q-1)
    in q, including both factors of 2; no sampled derivative is used.
    """
    q = np.asarray(q,dtype=float)
    z = np.clip(q,0.,1.)
    active = (q>0.) & (q<1.)
    count = int(bubble_count)+1
    value = np.zeros(q.shape+(count,))
    first = np.zeros_like(value)
    second = np.zeros_like(value)
    value[...,0] = z**5*(126+z*(-420+z*(540+z*(-315+70*z))))
    first[...,0] = np.where(active,630*z**4*(1-z)**4,0.)
    second[...,0] = np.where(active,2520*z**3*(1-z)**3*(1-2*z),0.)
    if bubble_count == 0:
        return value,first,second
    x = 2*z-1
    T = np.empty(q.shape+(bubble_count,))
    Tq = np.zeros_like(T)
    Tqq = np.zeros_like(T)
    T[...,0] = 1.
    if bubble_count > 1:
        T[...,1] = x
        Tq[...,1] = 2.
    for j in range(2,bubble_count):
        T[...,j] = 2*x*T[...,j-1]-T[...,j-2]
        Tq[...,j] = 4*T[...,j-1]+2*x*Tq[...,j-1]-Tq[...,j-2]
        Tqq[...,j] = 8*Tq[...,j-1]+2*x*Tqq[...,j-1]-Tqq[...,j-2]
    p = np.where(active,1024*z**5*(1-z)**5,0.)
    pq = np.where(active,5120*z**4*(1-z)**4*(1-2*z),0.)
    pqq = np.where(active,5120*(4*z**3*(1-z)**3*(1-2*z)**2-2*z**4*(1-z)**4),0.)
    value[...,1:] = p[...,None]*T
    first[...,1:] = pq[...,None]*T+p[...,None]*Tq
    second[...,1:] = pqq[...,None]*T+2*pq[...,None]*Tq+p[...,None]*Tqq
    return value,first,second


def _rotate(value,phase,parameter_axis=False):
    result=np.array(value,copy=True)
    c,s=np.cos(phase),np.sin(phase)
    if parameter_axis:
        result[...,0,:]=c*value[...,0,:]-s*value[...,1,:]
        result[...,1,:]=s*value[...,0,:]+c*value[...,1,:]
    else:
        result[...,0]=c*value[...,0]-s*value[...,1]
        result[...,1]=s*value[...,0]+c*value[...,1]
    return result


class FlatDevelopableFamily:
    def __init__(self,coefficients,cut_radius=.8,flat_radius=.34,
                 cuff_radius=.32,plane_height=1.25,quadrature_order=None,
                 quadrature_chunk=32):
        self.coefficients=np.array(coefficients,dtype=float,copy=True)
        if self.coefficients.ndim!=1 or len(self.coefficients)<1 or not np.all(np.isfinite(self.coefficients)):
            raise ValueError('coefficients must be a nonempty finite vector [A,b0,...]')
        self.coefficients.flags.writeable=False
        self.cut_radius=float(cut_radius)
        self.flat_radius=float(flat_radius)
        self.cuff_radius=float(cuff_radius)
        self.plane_height=float(plane_height)
        if not 0<self.cuff_radius<self.flat_radius<self.cut_radius:
            raise ValueError('require 0 < cuff_radius < flat_radius < cut_radius')
        self.width=self.cut_radius-self.flat_radius
        self.parameter_count=len(self.coefficients)
        self.bubble_count=self.parameter_count-1
        self.quadrature_order=int(quadrature_order if quadrature_order is not None else max(96,self.bubble_count+32))
        self.quadrature_chunk=max(1,int(quadrature_chunk))

    def sufficient_bounds(self):
        """Analytic, deliberately separate sufficient geometric conditions.

        |B_j|<=1, |B_j'|<=81920/19683+2j².
        |B_j'/S9'|<=512/63+(256/315)j² in (0,1).
        These are not tests which alter the field or stop an evaluation.
        """
        A=self.coefficients[0]
        b=np.abs(self.coefficients[1:])
        j=np.arange(self.bubble_count,dtype=float)
        angle=float(abs(A)+b.sum())
        curvature=float((abs(A)*(315/128)+np.dot(b,81920/19683+2*j*j))/self.width)
        convexity_slack=float(A-np.dot(b,512/63+(256/315)*j*j))
        convex=convexity_slack>=0
        actual_angle_bound=float(A) if convex else angle
        return dict(absolute_angle_upper=actual_angle_bound,
                    crude_absolute_angle_upper=angle,
                    absolute_curvature_upper=curvature,
                    curvature_nonnegative_sufficient=convex,
                    curvature_nonnegative_sufficient_slack=convexity_slack,
                    positive_projection_sufficient=actual_angle_bound<np.pi/2,
                    projection_lower=(float(np.cos(actual_angle_bound)) if actual_angle_bound<np.pi else None),
                    scope='analytic sufficient bounds; no condition is enforced by modifying coefficients; support/held budgets require their own actual assumptions')

    def angle_jets(self,y):
        y=np.asarray(y,dtype=float)
        sign=np.sign(y)
        q=(np.abs(y)-self.flat_radius)/self.width
        val,d1,d2=angle_basis(q,self.bubble_count)
        aJ=sign[...,None]*val
        kJ=d1/self.width
        kyJ=sign[...,None]*d2/self.width**2
        alpha=aJ@self.coefficients
        kappa=kJ@self.coefficients
        kappa_y=kyJ@self.coefficients
        return dict(alpha=alpha,kappa=kappa,kappa_y=kappa_y,
                    alpha_jacobian=aJ,kappa_jacobian=kJ,kappa_y_jacobian=kyJ,
                    cos_alpha=np.cos(alpha),sin_alpha=np.sin(alpha))

    def curve(self,y,*,integrate=True):
        """Angle/curvature jets and optional GL curve positions and all JVPs.

        Returned Jacobians have parameter as their last dimension.  GL work is
        chunked, has no point memoization, and holds no full-grid spectral cache.
        The exact mathematical curve uses the integrals, not a fixed GL rule.
        """
        y=np.asarray(y,dtype=float)
        result=self.angle_jets(y)
        if not integrate:
            return result
        shape=y.shape
        flat=y.reshape(-1)
        X=flat.copy()
        Z=np.zeros_like(flat)
        XJ=np.zeros((flat.size,self.parameter_count))
        ZJ=np.zeros_like(XJ)
        nodes,weights=_gauss(self.quadrature_order)
        A=self.coefficients[0]
        for start in range(0,flat.size,self.quadrature_chunk):
            end=min(flat.size,start+self.quadrature_chunk)
            yf=flat[start:end]
            sign=np.sign(yf)
            v=np.maximum(np.abs(yf)-self.flat_radius,0)/self.width
            vmax=np.minimum(v,1.)
            points=vmax[:,None]*(nodes+1)/2
            basis,_,_=angle_basis(points,self.bubble_count)
            angle=basis@self.coefficients
            sn,cs=np.sin(angle),np.cos(angle)
            scale=self.width*vmax/2
            X[start:end]+=sign*scale*np.sum(-2*np.sin(angle/2)**2*weights,axis=1)
            Z[start:end]=scale*np.sum(sn*weights,axis=1)
            XJ[start:end]=-sign[:,None]*scale[:,None]*np.einsum('no,nop,o->np',sn,basis,weights,optimize=True)
            ZJ[start:end]=scale[:,None]*np.einsum('no,nop,o->np',cs,basis,weights,optimize=True)
            beyond=self.width*np.maximum(v-1,0)
            X[start:end]+=sign*beyond*(np.cos(A)-1)
            Z[start:end]+=beyond*np.sin(A)
            XJ[start:end,0]-=sign*beyond*np.sin(A)
            ZJ[start:end,0]+=beyond*np.cos(A)
        result.update(X=X.reshape(shape),Z=Z.reshape(shape),
                      X_jacobian=XJ.reshape(shape+(self.parameter_count,)),
                      Z_jacobian=ZJ.reshape(shape+(self.parameter_count,)))
        return result

    def evaluate(self,r,u,*,phase=0.,position_jets=True):
        r,u=np.broadcast_arrays(np.asarray(r,float),np.asarray(u,float))
        sn,cs=np.sin(u-phase),np.cos(u-phase)
        q=self.curve(r*sn,integrate=position_jets)
        k,kJ,ky,kyJ=q['kappa'],q['kappa_jacobian'],q['kappa_y'],q['kappa_y_jacobian']
        aJ=q['alpha_jacobian']
        l,m,n=k*sn**2,-k*sn*cs,k*cs**2
        lJ,mJ,nJ=kJ*sn[...,None]**2,-kJ*(sn*cs)[...,None],kJ*cs[...,None]**2
        # Fixed physical r,u derivatives, useful for exact cut liftings.
        ku=ky*r*cs
        kuJ=kyJ*(r*cs)[...,None]
        lu=ku*sn**2+2*k*sn*cs
        mu=-ku*sn*cs-k*(cs**2-sn**2)
        nu=ku*cs**2-2*k*sn*cs
        luJ=kuJ*sn[...,None]**2+2*kJ*(sn*cs)[...,None]
        muJ=-kuJ*(sn*cs)[...,None]-kJ*(cs**2-sn**2)[...,None]
        nuJ=kuJ*cs[...,None]**2-2*kJ*(sn*cs)[...,None]
        result=dict(alpha=q['alpha'],kappa=k,kappa_y=ky,
                    alpha_jacobian=aJ,kappa_jacobian=kJ,kappa_y_jacobian=kyJ,
                    l=l,m=m,n=n,l_jacobian=lJ,m_jacobian=mJ,n_jacobian=nJ,
                    l_u=lu,m_u=mu,n_u=nu,
                    l_u_jacobian=luJ,m_u_jacobian=muJ,n_u_jacobian=nuJ,
                    l_s=-ky*sn**3,m_s=ky*sn**2*cs,n_s=-ky*sn*cs**2,
                    l_s_jacobian=-kyJ*sn[...,None]**3,
                    m_s_jacobian=kyJ*(sn**2*cs)[...,None],
                    n_s_jacobian=-kyJ*(sn*cs**2)[...,None],
                    r=r,u=u,phase=phase)
        if not position_jets:
            return result
        zeros=np.zeros_like(r)
        ex=np.stack((np.ones_like(r),zeros,zeros),axis=-1)
        T=np.stack((zeros,q['cos_alpha'],-q['sin_alpha']),axis=-1)
        N=np.stack((zeros,-q['sin_alpha'],-q['cos_alpha']),axis=-1)
        TJ=N[..., :,None]*aJ[...,None,:]
        NJ=-T[..., :,None]*aJ[...,None,:]
        Ty=k[...,None]*N
        TyJ=N[..., :,None]*kJ[...,None,:]+k[...,None,None]*NJ
        X=np.stack((r*cs,q['X'],self.plane_height-q['Z']),axis=-1)
        XJ=np.stack((np.zeros_like(q['X_jacobian']),q['X_jacobian'],-q['Z_jacobian']),axis=-2)
        Xr=cs[...,None]*ex+sn[...,None]*T
        Xu=r[...,None]*(-sn[...,None]*ex+cs[...,None]*T)
        Xrr=sn[...,None]**2*Ty
        Xru=-sn[...,None]*ex+cs[...,None]*T+(r*sn*cs)[...,None]*Ty
        Xuu=(-r*cs)[...,None]*ex+(-r*sn)[...,None]*T+(r*r*cs*cs)[...,None]*Ty
        XrJ=sn[...,None,None]*TJ
        XuJ=(r*cs)[...,None,None]*TJ
        XrrJ=sn[...,None,None]**2*TyJ
        XruJ=cs[...,None,None]*TJ+(r*sn*cs)[...,None,None]*TyJ
        XuuJ=(-r*sn)[...,None,None]*TJ+(r*r*cs*cs)[...,None,None]*TyJ
        vec=dict(X=X,X_r=Xr,X_u=Xu,X_rr=Xrr,X_ru=Xru,X_uu=Xuu,
                 X_s=-Xr,X_ss=Xrr,X_su=-Xru,e1=-Xr,e2=Xu/r[...,None],N=N)
        jac=dict(X=XJ,X_r=XrJ,X_u=XuJ,X_rr=XrrJ,X_ru=XruJ,X_uu=XuuJ,
                 X_s=-XrJ,X_ss=XrrJ,X_su=-XruJ,e1=-XrJ,e2=XuJ/r[...,None,None],N=NJ)
        vec={key:_rotate(value,phase) for key,value in vec.items()}
        jac={key:_rotate(value,phase,True) for key,value in jac.items()}
        result.update(vec)
        result.update({key+'_jacobian':value for key,value in jac.items()})
        result['outward_normal']=-vec['N']
        result['outward_normal_jacobian']=-jac['N']
        result['H']=q['Z']
        result['H_jacobian']=q['Z_jacobian']
        result['gc_values']=np.concatenate((n[...,None],m[...,None],vec['X'],vec['e1'],vec['e2'],vec['N']),axis=-1)
        result['gc_values_jacobian']=np.concatenate((nJ[...,None,:],mJ[...,None,:],jac['X'],jac['e1'],jac['e2'],jac['N']),axis=-2)
        sa,ca=q['sin_alpha'],q['cos_alpha']
        h=dict(H=q['Z'],Hr=sn*sa,Hu=r*cs*sa,
               Hrr=sn**2*k*ca,Hru=cs*sa+r*sn*cs*k*ca,
               Huu=-r*sn*sa+r*r*cs*cs*k*ca)
        dsa=ca[...,None]*aJ
        dkc=kJ*ca[...,None]-k[...,None]*sa[...,None]*aJ
        hj=dict(H=q['Z_jacobian'],Hr=sn[...,None]*dsa,Hu=(r*cs)[...,None]*dsa,
                Hrr=sn[...,None]**2*dkc,
                Hru=cs[...,None]*dsa+(r*sn*cs)[...,None]*dkc,
                Huu=(-r*sn)[...,None]*dsa+(r*r*cs*cs)[...,None]*dkc)
        result['height_jet']=h
        result['height_jet_jacobian']=hj
        return result

    def cut_port(self,u,*,phase=0.,position_jets=True):
        return self.evaluate(self.cut_radius,u,phase=phase,position_jets=position_jets)

    def jvp(self,r,u,direction,*,phase=0.,position_jets=True):
        direction=np.asarray(direction,dtype=float)
        if direction.shape!=self.coefficients.shape:
            raise ValueError('direction must have the same shape as coefficients')
        out=self.evaluate(r,u,phase=phase,position_jets=position_jets)
        result={key[:-9]:value@direction for key,value in out.items() if key.endswith('_jacobian') and isinstance(value,np.ndarray)}
        if position_jets:
            result['height_jet']={key:value@direction for key,value in out['height_jet_jacobian'].items()}
        return result
