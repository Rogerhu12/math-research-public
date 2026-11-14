"""R153 local positive-n Gauss substitution and complete first variation.

Only active w>0 entries are divided. Outside the chosen coast the old
independent three-field representation, including n=0, is untouched.
"""
from __future__ import annotations
import numpy as np


def positive_gauss_l_delta(values,angular,K,weight,*,minimum_active_n=.05):
    values=np.asarray(values,float);angular=np.asarray(angular,float)
    if values.shape!=angular.shape or values.shape[-1]!=3:raise ValueError('Expected matching (...,n/m/l) arrays')
    n,m,l=(values[...,j] for j in range(3));nx,mx,lx=(angular[...,j] for j in range(3))
    w=np.broadcast_to(np.asarray(weight,float),n.shape);K=np.broadcast_to(np.asarray(K,float),n.shape)
    if np.any(w<0) or np.any(w>1) or minimum_active_n<0:raise ValueError('Use a fixed [0,1] window and nonnegative finite search margin')
    active=w>0
    if np.any(n[active]<=minimum_active_n):raise FloatingPointError('Chosen active coast positive-n search domain failed')
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(angular)):raise FloatingPointError('Nonfinite actual raw fields')
    delta=np.zeros_like(n);dx=np.zeros_like(n);actual_l=l.copy();actual_l_xi=lx.copy()
    gn=np.zeros_like(n);gm=np.zeros_like(n);gk=np.zeros_like(n);hn=np.zeros_like(n);hm=np.zeros_like(n);hk=np.zeros_like(n)
    if np.any(active):
        ni,mi,nxi,mxi,wi,ki=(q[active] for q in (n,m,nx,mx,w,K))
        A=(ki+mi*mi)/ni;B=(2*mi*mxi-A*nxi)/ni
        delta[active]=wi*(A-l[active]);dx[active]=wi*(B-lx[active])
        actual_l[active]=(1-wi)*l[active]+wi*A;actual_l_xi[active]=(1-wi)*lx[active]+wi*B
        gn[active]=-wi*A/ni;gm[active]=2*wi*mi/ni;gk[active]=wi/ni
        hn[active]=wi*(-B/ni+A*nxi/ni**2)
        hm[active]=wi*(2*mxi/ni-2*mi*nxi/ni**2);hk[active]=-wi*nxi/ni**2
    return dict(delta=delta,delta_xi=dx,actual_l=actual_l,actual_l_xi=actual_l_xi,gn=gn,gm=gm,gl=-w,gK=gk,
        hn=hn,hm=hm,hK=hk,weight=w,active=active,
        sampled_minimum_active_n=float(np.min(n[active])) if np.any(active) else None)


def gauss_delta_direction(delta,value_direction,angular_direction,K_direction):
    """All columns at once; value/xi (...,3,P), K (...,P)."""
    dv,dx=np.asarray(value_direction,float),np.asarray(angular_direction,float)
    dk=np.asarray(K_direction,float)
    if dv.shape!=dx.shape or dv.shape[-2]!=3:raise ValueError('Expected (...,3,parameters) jets')
    v=(delta['gn'][...,None]*dv[...,0,:]+delta['gm'][...,None]*dv[...,1,:]
       +delta['gl'][...,None]*dv[...,2,:]+delta['gK'][...,None]*dk)
    xi=(delta['hn'][...,None]*dv[...,0,:]+delta['hm'][...,None]*dv[...,1,:]
        +delta['hK'][...,None]*dk+delta['gn'][...,None]*dx[...,0,:]
        +delta['gm'][...,None]*dx[...,1,:]+delta['gl'][...,None]*dx[...,2,:])
    return v,xi


def gauss_delta_state_columns(problem,delta,node):
    """Actual local Fourier-node columns before any radial P1 map."""
    j=int(node)
    value=np.concatenate((delta['gn'][:,j,None]*problem.E,
        delta['gm'][:,j,None]*problem.O,delta['gl'][:,j,None]*problem.E),axis=1)
    angular=np.concatenate((delta['hn'][:,j,None]*problem.E+delta['gn'][:,j,None]*problem.Ex,
        delta['hm'][:,j,None]*problem.O+delta['gm'][:,j,None]*problem.Ox,
        delta['gl'][:,j,None]*problem.Ex),axis=1)
    return value,angular
