#!/usr/bin/env python3
"""R613 complete derivative of the same actual position-defect field.

This helper has no seed, ODE, optimization, I/O or independent probe. A new
declared Actions scope supplies one already evaluated actual height and its
complete two-jet derivatives. Finite quadrature/primitive errors are not
silently certified as continuous identities.
"""
from collections import defaultdict
import numpy as np

COUNTS=defaultdict(int)


def primitive(values,matrix):
    """Apply exactly the supplied original angular primitive, axis1.

Two-dimensional values have shape (r,theta); derivative blocks have shape
(r,theta,direction). No FFT replacement or independent angular grid is used.
"""
    if values.ndim==2:
        return values@matrix.T
    if values.ndim!=3:
        raise ValueError("position primitive expects two or three axes")
    nr,nt,nc=values.shape
    packed=values.transpose(0,2,1).reshape(nr*nc,nt)
    return (packed@matrix.T).reshape(nr,nc,nt).transpose(0,2,1)


def prepare(state,data):
    """One same-field cache; no geometry or height evaluation is called."""
    g=state["g"]
    b,N,u,E=[g[k] for k in ("b","N","u","E")]
    P=data["primitive"]
    G=state["At"]/state["M"]
    weight=N/u**3
    mean_weight=np.mean(weight,axis=1,keepdims=True)
    mu=np.mean(weight*G,axis=1,keepdims=True)/mean_weight
    T=g["Yt"]/b[:,:,None]
    JT=np.stack([-T[:,:,1],T[:,:,0]],axis=2)
    pir=primitive(g["R"],P)
    COUNTS["same_field_cache_builds"]+=1
    COUNTS["same_field_radial_angular_points"]+=int(b.size)
    return {"primitive":P,"b":b,"N":N,"u":u,"E":E,
            "G":G,"weight":weight,"mean_weight":mean_weight,"mu":mu,
            "T":T,"JT":JT,"pir":pir,"Wstar":g["Wstar"],
            "S":g["Wstar"]/np.sqrt(E)[:,:,None]}


def derivative(cache,dN,du,dE,db,dG):
    """Complete R613 derivative, returning shape (r,theta,component,direction).

Inputs are derivatives of the *same* current N,u,E,b,G, all shaped
(r,theta,direction), with broadcasting allowed for angular-constant dE.
In particular, dG must include the implicit turning derivative and the
actual dependent core chain. The off-solution weight and phase terms below
are retained.
"""
    N,u,E,b=[cache[k][:,:,None] for k in ("N","u","E","b")]
    G,mu,weight=[cache[k][:,:,None] for k in ("G","mu","weight")]
    dw=dN/u**3-3*N*du/u**4
    da=dN/u-N*du/u**2
    dmu=np.mean(dw*(G-mu)+weight*dG,axis=1,keepdims=True)
    dmu/=cache["mean_weight"][:,:,None]
    dR=dw*(G-mu)+weight*(dG-dmu)
    dpsi=primitive(da,cache["primitive"])
    dpir=primitive(dR,cache["primitive"])
    pir=cache["pir"][:,:,None]
    common=db*pir+b*dpir
    phase=b*pir*dpsi
    answer=[]
    for component in range(2):
        dW=primitive(common*cache["JT"][:,:,component,None]
                     -phase*cache["T"][:,:,component,None],cache["primitive"])
        dS=dW/np.sqrt(E)-cache["Wstar"][:,:,component,None]*dE/(2*E**1.5)
        answer.append(dS)
    result=np.stack(answer,axis=2)
    if not np.all(np.isfinite(result)):
        raise ArithmeticError("nonfinite complete actual-position derivative")
    COUNTS["analytic_direction_blocks"]+=1
    COUNTS["analytic_direction_columns"]+=int(result.shape[-1])
    COUNTS["analytic_direction_radial_angular_points"]+=int(result.shape[0]*result.shape[1]*result.shape[-1])
    return result


def projection(theta,odd_modes):
    odd_modes=np.asarray(odd_modes,dtype=int)
    if (odd_modes.ndim!=1 or len(odd_modes)==0 or np.any(odd_modes<=0)
        or np.any(odd_modes%2!=1) or np.any(np.diff(odd_modes)<=0)
        or 2*int(odd_modes[-1])>=len(theta)):
        raise ValueError("declared actual-position modes must be distinct positive odd modes below Nyquist")
    angles=odd_modes[:,None]*np.asarray(theta)[None,:]
    # sqrt(2)*mean is the cosine/sine coefficient divided by sqrt(2),
    # hence the complete Fourier l2 objective has exactly Parseval units.
    unit=np.sqrt(2.)/len(theta)
    return unit*np.cos(angles),unit*np.sin(angles)


def residual(cache,matrices,radial_units,amplitude):
    co,si=matrices
    S=cache["S"]
    values=np.stack([S[:,:,0]@co.T,S[:,:,1]@si.T],axis=1)
    return (values*np.asarray(radial_units)[:,None,None]/amplitude).ravel()


def projected_derivative(dS,matrices,radial_units,amplitude):
    co,si=matrices
    x=np.einsum("rtp,jt->rjp",dS[:,:,0,:],co,optimize=True)
    y=np.einsum("rtp,jt->rjp",dS[:,:,1,:],si,optimize=True)
    values=np.stack([x,y],axis=1)
    return (values*np.asarray(radial_units)[:,None,None,None]/amplitude).reshape(-1,dS.shape[-1])
