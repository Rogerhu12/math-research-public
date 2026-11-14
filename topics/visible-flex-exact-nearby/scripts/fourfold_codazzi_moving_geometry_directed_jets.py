#!/usr/bin/env python3
"""Complete directed radial jets of the actual model moving connection.

Every Fourier product is evaluated on an alias-free grid and the primitive
retains all index-64 coefficients. Returned connection jets retain index 96.
The point grid is the exact phi_k=pi*k/(2*N), not binary64 approximations to pi.
"""
from __future__ import annotations
import math
from fractions import Fraction
import numpy as np
from flint import arb
from fourfold_phase_beta_bulk_box import (
    Box,CBox,DirectedFFT,arb_box,reduce_box,stack,square_box)
from fourfold_phase_beta_bulk_interval import exact_arb

ORDER=4

def add(a,b):
    return [a[j]+b[j] for j in range(ORDER)]

def scale(a,b):
    return [x*b for x in a]

def product(a,b):
    return [sum((a[k]*b[j-k] for k in range(j+1)),Box(0.))
            for j in range(ORDER)]

def inverse(a):
    result=[a[0].reciprocal()]
    for j in range(1,ORDER):
        result.append(-result[0]*sum(
            (a[k]*result[j-k] for k in range(1,j+1)),Box(0.)))
    return result

def quotient(a,b):
    return product(a,inverse(b))

def target_jet(values,name):
    return [arb_box(values[name+(str(j) if j else '')])/math.factorial(j)
            for j in range(ORDER)]

def checked_real(values):
    if np.any(values.imag.lo>0) or np.any(values.imag.hi<0):
        raise ValueError("a complete real Fourier field lost its imaginary zero")
    return [values.real[:,j] for j in range(ORDER)]

def model_jets(saved,piece,left,right,coefficients,alpha,fft,N=512):
    """Normalized radial jets, valid on the entire supplied closed interval."""
    M=(saved["piece_coefficients"].shape[2]-1)//2
    if N<=6*M or N&(N-1):raise ValueError("the complete connection support aliases")
    nodes=saved["radial_nodes"]
    l=Fraction.from_float(float(nodes[piece]))
    r=Fraction.from_float(float(nodes[piece+1]))
    if not l<=left<=right<=r:raise ValueError("no actual PPoly extrapolation")
    dx=arb_box(exact_arb(left-l).union(exact_arb(right-l)))
    c=[Box(x) for x in saved["piece_coefficients"][:,piece,:]]
    y=[((c[0]*dx+c[1])*dx+c[2])*dx+c[3],
       (3*c[0]*dx+2*c[1])*dx+c[2],
       3*c[0]*dx+c[1],c[0]]
    a0=arb_box(coefficients["a"])
    beta=target_jet(coefficients,"beta")
    gamma=target_jet(coefficients,"gamma")
    K=target_jet(coefficients,"K")
    s=target_jet(coefficients,"s")
    a=[a0,a0*beta[0],
       a0*(beta[1]+beta[0]*beta[0])/2,
       a0*(2*beta[2]+3*beta[0]*beta[1]+beta[0]*beta[0]*beta[0])/6]
    al=arb_box(exact_arb(alpha))
    rows=stack(y,1)
    uc=CBox(Box(np.zeros((N,ORDER))))
    vc=CBox(Box(np.zeros((N,ORDER))))
    ids=np.arange(1,M+1)
    uc[ids]=CBox(0.,-al*rows[:M]/2)
    uc[-ids]=CBox(0.,al*rows[:M]/2)
    vc[ids]=CBox(al*rows[M+1:]/2)
    vc[-ids]=CBox(al*rows[M+1:]/2)
    mean=[s[j]+al*y[j][M] for j in range(ORDER)]
    if np.any(mean[0].hi>=0):raise ValueError("complete true mean gap unresolved")
    vc[0]=CBox(stack(mean))
    u=checked_real(fft.fft(uc,inverse=True)*N)
    v=checked_real(fft.fft(vc,inverse=True)*N)
    S=add(product(u,u),product(K,product(v,v)))
    sc=fft.fft(CBox(stack(S,1)))/N
    # The exact S has degree at most 2M. This is an identity of the full
    # candidate polynomial, not a truncation of an unknown Fourier field.
    freq=np.r_[np.arange(N//2),np.arange(-N//2,0)]
    factors=np.zeros(N)
    nonzero=(freq!=0)&(abs(freq)<=2*M)
    factors[nonzero]=1/(4*freq[nonzero])
    exact_factors=Box(np.zeros(N))
    for k in np.nonzero(nonzero)[0]:
        z=arb_box(arb(1)/(4*int(freq[k])))
        exact_factors.lo[k],exact_factors.hi[k]=z.lo,z.hi
    primitive=checked_real(fft.fft(
        sc*CBox(0.,-exact_factors.reshape(N,1)),inverse=True)*N)
    primitive_v=checked_real(fft.fft(
        vc*CBox(0.,-exact_factors.reshape(N,1)),inverse=True)*N)
    d=scale(product(beta,primitive),-1)
    vm=quotient(v,mean);um=quotient(u,mean)
    tau=add(product(d,vm),scale(product(gamma,u),-1))
    result=dict(
        p=product(quotient(beta,gamma),tau),
        q=product(a,add(product(product(gamma,K),v),product(d,um))),
        t=product(a,quotient(d,mean)),
        fx=product(a,gamma),fy=product(a,tau),
        A=product(quotient(beta,gamma),vm),
        B=product(a,um),C=quotient(a,mean),
        angular_speed=product(a,vm),
        u=u,v=v,mean=mean,inverse_lift_shift=quotient(primitive_v,mean))
    for values in result.values():
        for value in values:
            if not (np.all(np.isfinite(value.lo)) and np.all(np.isfinite(value.hi))):
                raise ValueError("a complete model jet is nonfinite")
    return result

def whole_circle_norms(values,fft,N=512,maximum_support=96):
    """All true angular modes, derivative orders zero through three."""
    arrays=[]
    for x in values:
        arrays.append(Box(np.broadcast_to(x.lo,(N,)),np.broadcast_to(x.hi,(N,))))
    coefficients=fft.fft(CBox(stack(arrays,1)))/N
    freq=np.r_[np.arange(N//2),np.arange(-N//2,0)]
    keep=abs(freq)<=maximum_support
    magnitude=coefficients.magnitude_upper()[keep]
    sums=reduce_box(Box(magnitude),0)
    return [(arb(float(sums.hi[j]))*math.factorial(j)).upper()
            for j in range(ORDER)]

def coefficient_norms(fields,fft,N=512):
    """True radial operator norms at every exact angle in the declared grid.

    The grid integration theorem needs no Fourier/Wiener norm. In the
    skew 3 by 3 connection, the operator norm is exactly sqrt(p²+q²+t²).
    Taking this pointwise bound avoids turning interval radii into 193
    artificial Fourier coefficient errors. Continuous-angle geometry is
    expressly outside this consumer's permission.
    """
    def norms(names):
        result=[]
        for j in range(ORDER):
            arrays=[Box(np.broadcast_to(fields[n][j].lo,(N,)),
                        np.broadcast_to(fields[n][j].hi,(N,))) for n in names]
            result.append((maximum_euclidean(stack(arrays,1))*math.factorial(j)).upper())
        return result
    return norms(('p','q','t')),norms(('fx','fy'))

def right_connection(Q,fields,order):
    """Q stores its three world-vector columns X,Y,N."""
    p,q,t=(fields[name][order]*math.factorial(order) for name in ('p','q','t'))
    p,q,t=(x.reshape(-1,1) if x.lo.ndim else x for x in (p,q,t))
    X,Y,N=Q[:,:3],Q[:,3:6],Q[:,6:9]
    out=[p*Y+q*N,-p*X+t*N,-q*X-t*Y]
    return Box(np.concatenate([x.lo for x in out],1),
               np.concatenate([x.hi for x in out],1))

def position_connection(Q,fields,order):
    fx,fy=(fields[name][order]*math.factorial(order) for name in ('fx','fy'))
    fx,fy=(x.reshape(-1,1) if x.lo.ndim else x for x in (fx,fy))
    return fx*Q[:,:3]+fy*Q[:,3:6]

def maximum_euclidean(value):
    squared=reduce_box(square_box(value),1)
    return arb(float(np.max(squared.hi))).sqrt().upper()

def local_taylor_budget(before,after,h,fields,anorm,fnorm):
    """Third Taylor polynomial and the complete fourth-derivative remainder."""
    Q=Box(before[:,3:12]);F=Box(before[:,:3])
    if not maximum_euclidean(Q)<2:
        raise ValueError("the actual numerical frame norm exceeds its paid factor")
    Q1=right_connection(Q,fields,0)
    Q2=right_connection(Q1,fields,0)+right_connection(Q,fields,1)
    Q3=(right_connection(Q2,fields,0)+2*right_connection(Q1,fields,1)
        +right_connection(Q,fields,2))
    F1=position_connection(Q,fields,0)
    F2=position_connection(Q1,fields,0)+position_connection(Q,fields,1)
    F3=(position_connection(Q2,fields,0)+2*position_connection(Q1,fields,1)
        +position_connection(Q,fields,2))
    hb=arb_box(exact_arb(h))
    tq=Q+hb*Q1+(hb*hb/2)*Q2+(hb*hb*hb/6)*Q3
    tf=F+hb*F1+(hb*hb/2)*F2+(hb*hb*hb/6)*F3
    defect_q=maximum_euclidean(Box(after[:,3:12])-tq)
    defect_f=maximum_euclidean(Box(after[:,:3])-tf)
    A0,A1,A2,A3=anorm;f0,f1,f2,f3=fnorm
    B2=A0**2+A1
    B3=A0**3+3*A0*A1+A2
    B4=A0**4+6*A0**2*A1+3*A1**2+4*A0*A2+A3
    F4=B3*f0+3*B2*f1+3*A0*f2+f3
    width=abs(exact_arb(h))
    dq=(defect_q+2*width**4*B4/24).upper()
    df=(defect_f+2*width**4*F4/24).upper()
    return dict(local_frame_error=dq,local_position_error=df,
                complete_model_speed=fnorm[0],complete_connection_norm=anorm[0],
                fourth_frame_majorant=(2*B4).upper(),
                fourth_position_majorant=(2*F4).upper(),
                evaluated_third_Taylor_frame_defect=defect_q,
                evaluated_third_Taylor_position_defect=defect_f)
