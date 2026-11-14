"""R129: division-free three-field Gauss--Codazzi residual consumer.

All shape fields are orthonormal l,m,n.  A zero n is allowed, including an open
flat arc.  The only positive denominators are the material radius a and the
specified coordinate Jacobians J=S_x, omega=U_xi.  There is no l_s or K_s input.

Functions evaluate actual supplied jets, not a solver RHS substituted for the
derivative of its interpolant.  NumPy broadcasting is used without reshaping.
This module is a floating consumer; continuous interval bounds remain separate.
"""
from __future__ import annotations

import numpy as np


def _positive(value, name):
    value = np.asarray(value, dtype=float)
    if np.any(~np.isfinite(value)) or np.any(value <= 0):
        raise ValueError(f"{name} must be finite and positive")
    return value


def physical_residuals(*, a, a_s, a_ss, l, m, n, l_u, m_u, m_s, n_s):
    """Complete residuals in the fixed material (s,u) coordinates."""
    a = _positive(a, "a")
    c, K = np.asarray(a_s)/a, -np.asarray(a_ss)/a
    l, m, n = np.asarray(l), np.asarray(m), np.asarray(n)
    G = l*n-m*m-K
    Rm = np.asarray(m_s)-np.asarray(l_u)/a+2*c*m
    Rn = np.asarray(n_s)-np.asarray(m_u)/a-c*(l-n)
    G, Rm, Rn, aa = np.broadcast_arrays(G, Rm, Rn, a)
    h = np.stack((-aa*Rn, aa*Rm, -aa*G), axis=-1)
    return dict(G=G, Rm=Rm, Rn=Rn, connection_vector=h,
                connection_operator_norm=np.linalg.norm(h, axis=-1))


def physical_jvp(*, a, a_s, a_ss, l, m, n, l_u, m_u, m_s, n_s,
                 dl, dm, dn, dl_u, dm_u, dm_s, dn_s,
                 da=0., da_s=0., da_ss=0.):
    """Directional derivative, optionally including a genuine metric change.

    The supplied derivative jets are derivatives of physical jets.  For a
    varying computation chart, use native_jvp to include that chain rule.
    """
    a = _positive(a, "a")
    l, m, n = np.asarray(l), np.asarray(m), np.asarray(n)
    c = np.asarray(a_s)/a
    dc = np.asarray(da_s)/a-np.asarray(a_s)*np.asarray(da)/a**2
    dK = -np.asarray(da_ss)/a+np.asarray(a_ss)*np.asarray(da)/a**2
    dG = n*np.asarray(dl)+l*np.asarray(dn)-2*m*np.asarray(dm)-dK
    dRm = (np.asarray(dm_s)-np.asarray(dl_u)/a
           +np.asarray(l_u)*np.asarray(da)/a**2+2*dc*m+2*c*np.asarray(dm))
    dRn = (np.asarray(dn_s)-np.asarray(dm_u)/a
           +np.asarray(m_u)*np.asarray(da)/a**2-dc*(l-n)-c*(np.asarray(dl)-np.asarray(dn)))
    base = physical_residuals(a=a,a_s=a_s,a_ss=a_ss,l=l,m=m,n=n,
                             l_u=l_u,m_u=m_u,m_s=m_s,n_s=n_s)
    v = np.stack(np.broadcast_arrays(-dRn,dRm,-dG),axis=-1)
    z = np.stack((-base['Rn'],base['Rm'],-base['G']),axis=-1)
    dh = np.asarray(a)[...,None]*v+np.asarray(da)[...,None]*z
    return dict(G=dG,Rm=dRm,Rn=dRn,connection_vector=dh)


def native_physical_jets(*, J, U_x, U_xi, l_xi, m_xi, n_xi, m_x, n_x):
    """s=S(x), u=U(x,xi); every radial derivative holds physical u fixed."""
    J, omega = _positive(J,"J=S_x"), _positive(U_xi,"U_xi")
    drift = np.asarray(U_x)/omega
    return dict(l_u=np.asarray(l_xi)/omega,m_u=np.asarray(m_xi)/omega,
                n_u=np.asarray(n_xi)/omega,
                m_s=(np.asarray(m_x)-drift*np.asarray(m_xi))/J,
                n_s=(np.asarray(n_x)-drift*np.asarray(n_xi))/J)


def native_residuals(*, a, a_s, a_ss, l, m, n,
                     J, U_x, U_xi, l_xi, m_xi, n_xi, m_x, n_x):
    jets = native_physical_jets(J=J,U_x=U_x,U_xi=U_xi,l_xi=l_xi,
                               m_xi=m_xi,n_xi=n_xi,m_x=m_x,n_x=n_x)
    out = physical_residuals(a=a,a_s=a_s,a_ss=a_ss,l=l,m=m,n=n,
                            **{k:jets[k] for k in ('l_u','m_u','m_s','n_s')})
    out['physical_jets'] = jets
    return out


def native_jvp(*, a, a_s, a_ss, l, m, n,
               J, U_x, U_xi, l_xi, m_xi, n_xi, m_x, n_x,
               dl, dm, dn, dl_xi, dm_xi, dn_xi, dm_x, dn_x,
               da=0., da_s=0., da_ss=0., dJ=0., dU_x=0., dU_xi=0.):
    J, omega = _positive(J,"J=S_x"), _positive(U_xi,"U_xi")
    drift = np.asarray(U_x)/omega
    ddrift = (np.asarray(dU_x)-drift*np.asarray(dU_xi))/omega
    p = native_physical_jets(J=J,U_x=U_x,U_xi=omega,l_xi=l_xi,m_xi=m_xi,
                            n_xi=n_xi,m_x=m_x,n_x=n_x)
    dlu=(np.asarray(dl_xi)-p['l_u']*np.asarray(dU_xi))/omega
    dmu=(np.asarray(dm_xi)-p['m_u']*np.asarray(dU_xi))/omega
    dms=(np.asarray(dm_x)-drift*np.asarray(dm_xi)-ddrift*np.asarray(m_xi)
         -p['m_s']*np.asarray(dJ))/J
    dns=(np.asarray(dn_x)-drift*np.asarray(dn_xi)-ddrift*np.asarray(n_xi)
         -p['n_s']*np.asarray(dJ))/J
    return physical_jvp(a=a,a_s=a_s,a_ss=a_ss,l=l,m=m,n=n,
                        **{k:p[k] for k in ('l_u','m_u','m_s','n_s')},
                        dl=dl,dm=dm,dn=dn,dl_u=dlu,dm_u=dmu,dm_s=dms,dn_s=dns,
                        da=da,da_s=da_s,da_ss=da_ss)


def native_angular_residuals(*, a, a_s, l, m, n, J, U_x, U_xi, U_x_xi, U_xixi,
                             l_xi, m_xi, n_xi, l_xixi, m_xixi, n_xixi,
                             m_x_xi, n_x_xi):
    """Physical u derivatives of all three residuals, without K_s or l_s."""
    a,J,omega=_positive(a,'a'),_positive(J,'J=S_x'),_positive(U_xi,'U_xi')
    c=np.asarray(a_s)/a;v=np.asarray(U_x)/omega
    v_xi=(np.asarray(U_x_xi)-v*np.asarray(U_xixi))/omega
    lu,mu,nu=np.asarray(l_xi)/omega,np.asarray(m_xi)/omega,np.asarray(n_xi)/omega
    luu=(np.asarray(l_xixi)-lu*np.asarray(U_xixi))/omega**2
    muu=(np.asarray(m_xixi)-mu*np.asarray(U_xixi))/omega**2
    msu=(np.asarray(m_x_xi)-v_xi*np.asarray(m_xi)-v*np.asarray(m_xixi))/(J*omega)
    nsu=(np.asarray(n_x_xi)-v_xi*np.asarray(n_xi)-v*np.asarray(n_xixi))/(J*omega)
    Gu=lu*np.asarray(n)+np.asarray(l)*nu-2*np.asarray(m)*mu
    Rmu=msu-luu/a+2*c*mu
    Rnu=nsu-muu/a-c*(lu-nu)
    h=np.stack(np.broadcast_arrays(-a*Rnu,a*Rmu,-a*Gu),axis=-1)
    return dict(G_u=Gu,Rm_u=Rmu,Rn_u=Rnu,connection_u_vector=h,
                connection_u_operator_norm=np.linalg.norm(h,axis=-1))


def _laurent(cosine, sine, order):
    out=np.zeros(2*order+1,dtype=complex)
    if cosine is not None:
        a=np.asarray(cosine,dtype=float);out[order]=a[0]
        for k in range(1,len(a)):out[order-k]=out[order+k]=a[k]/2
    if sine is not None:
        for k,v in enumerate(np.asarray(sine,dtype=float),1):
            out[order+k]=-0.5j*v;out[order-k]=0.5j*v
    return out


def gauss_fourier(l_cos,m_sin,n_cos,K):
    """All real cos(2*j*xi) coefficients of ln-m^2-K, without aliasing.

    Cosine arrays include their mean, the sine array starts at j=1.  No high
    product mode is dropped: an order-M input returns through order 2M.
    """
    order=max(len(l_cos)-1,len(n_cos)-1,len(m_sin))
    L=_laurent(l_cos,None,order);N=_laurent(n_cos,None,order);M=_laurent(None,m_sin,order)
    q=np.convolve(L,N)-np.convolve(M,M);center=2*order
    q[center]-=K
    out=2*q[center:].real;out[0]/=2
    return out


def gauss_fourier_jvp(l_cos,m_sin,n_cos,dl_cos,dm_sin,dn_cos,dK=0.):
    order=max(len(l_cos)-1,len(n_cos)-1,len(m_sin),len(dl_cos)-1,len(dn_cos)-1,len(dm_sin))
    L=_laurent(l_cos,None,order);N=_laurent(n_cos,None,order);M=_laurent(None,m_sin,order)
    dL=_laurent(dl_cos,None,order);dN=_laurent(dn_cos,None,order);dM=_laurent(None,dm_sin,order)
    q=np.convolve(dL,N)+np.convolve(L,dN)-2*np.convolve(M,dM);center=2*order
    q[center]-=dK
    out=2*q[center:].real;out[0]/=2
    return out


def compatible_cartesian_twojet(*, frame, a, a_s, l, m, n):
    """Jets of an actual compatible isometry; valid at n=0 as well.

    For a residual-bearing prefix, use its ACTUAL R124 jets instead.  Its
    auxiliary frame and input shape do not by themselves satisfy this premise.
    """
    a=_positive(a,'a');F=np.asarray(frame);e1,e2,N=F[...,0],F[...,1],F[...,2]
    def mul(s,v):return np.asarray(s)[...,None]*v
    return dict(X_s=e1,X_u=mul(a,e2),X_ss=mul(l,N),
                X_su=mul(a_s,e2)+mul(a*np.asarray(m),N),
                X_uu=mul(-a*np.asarray(a_s),e1)+mul(a*a*np.asarray(n),N))
