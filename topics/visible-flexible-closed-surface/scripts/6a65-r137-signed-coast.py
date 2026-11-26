#!/usr/bin/env python3
"""Signed-domain R137 consumer, preserving the original positive-only source.

The connected ruling root is used on every signed sigma for which r>0,
radicand>0 and D>0.  The physical increasing-s inlet direction d and slope
v are unchanged when sigma is negative.  Numeric checks are not a whole-
circle certificate.  See the original R137 note for the local negative
extension; this module makes the explicit domain and full jets consumable.
"""
from __future__ import annotations
import numpy as np


def col(x):
    return np.asarray(x)[..., None]


def ruling_coordinates(a, v, sigma, k, k_u, k_uu):
    a, v = float(a), float(v)
    sigma = np.asarray(sigma, dtype=float)
    if a <= 0 or v <= 0:
        raise ValueError('Signed consumer keeps a>0 and positive physical slope v')
    k, kt, ktt = np.broadcast_arrays(k, k_u, k_uu)
    r0 = a/v
    r = r0+sigma
    delta = sigma*(2*r0+sigma)
    radicand = r0*r0+(1+k*k)*delta
    if np.any(r <= 0) or np.any(radicand <= 0):
        raise ValueError('Signed ruling root leaves r>0, radicand>0 domain')
    A = np.sqrt(radicand)
    w = delta/(r0+A)
    c = r0+w
    if np.any(c <= 0):
        raise ArithmeticError('Connected root must have r0+w>0')
    ws = r/A
    wt = -k*kt*w*w/A
    wss = (1-(1+k*k)*ws*ws)/A
    wst = -ws*(2*k*kt*w+(1+k*k)*wt)/A
    wtt = -((1+k*k)*wt*wt+4*k*kt*w*wt+(kt*kt+k*ktt)*w*w)/A
    b = k*w
    cs, ct, bs, bt = ws, wt, k*ws, kt*w+k*wt
    css, cst, ctt = wss, wst, wtt
    bss = k*wss
    bst = kt*ws+k*wst
    btt = ktt*w+2*kt*wt+k*wtt
    beta = np.arctan2(b, c)
    betas = (c*bs-b*cs)/(r*r)
    betat = (c*bt-b*ct)/(r*r)
    betass = (c*bss-b*css)/(r*r)-2*betas/r
    betast = (ct*bs+c*bst-bt*cs-b*cst)/(r*r)
    betatt = (c*btt-b*ctt)/(r*r)
    Us, Ut = -betas/v, 1-betat/v
    Uss, Ust, Utt = -betass/v, -betast/v, -betatt/v
    D = a+w*(v*(1+k*k)-kt)
    if np.any(D <= 0) or np.any(Ut <= 0):
        raise ValueError('Signed ruling focus or material degeneracy reached')
    ts, tu = -Us/Ut, 1/Ut
    tss = -(Uss+2*Ust*ts+Utt*ts*ts)/Ut
    tsu = -(Ust+Utt*ts)*tu/Ut
    tuu = -Utt*tu*tu/Ut
    return dict(
        w=w, A=A, D=D, radicand=radicand, new_radius=a+v*sigma,
        material_shift=-beta/v, U_s=Us, U_t=Ut,
        U_ss=Uss, U_st=Ust, U_tt=Utt,
        inlet_t_s=ts, inlet_t_u=tu, inlet_t_ss=tss,
        inlet_t_su=tsu, inlet_t_uu=tuu,
        ruling_w_s=ws+wt*ts, ruling_w_u=wt*tu,
        ruling_w_ss=wss+2*wst*ts+wtt*ts*ts+wt*tss,
        ruling_w_su=(wst+wtt*ts)*tu+wt*tsu,
        ruling_w_uu=wtt*tu*tu+wt*tuu,
        raw_w_s=ws, raw_w_t=wt,
        connected_root_identity_error=A-r0-(1+k*k)*w,
        material_derivative_identity_error=Ut-D/(v*A))


def propagate(a, v, sigma, inlet):
    n, m = np.asarray(inlet['n']), np.asarray(inlet['m'])
    if np.any(n <= 0):
        raise ValueError('This signed chart requires positive inlet n')
    nu, mu, nuu, muu = (np.asarray(inlet[q]) for q in ('n_u','m_u','n_uu','m_uu'))
    k = m/n
    ku = mu/n-m*nu/(n*n)
    kuu = muu/n-m*nuu/(n*n)-2*mu*nu/(n*n)+2*m*nu*nu/(n*n*n)
    c = ruling_coordinates(a, v, sigma, k, ku, kuu)
    X, Xu, Xuu, e1, e1u, e1uu, e2, e2u, e2uu = (
        np.asarray(inlet[q]) for q in
        ('X','X_u','X_uu','e1','e1_u','e1_uu','e2','e2_u','e2_uu'))
    G = e1-col(k)*e2
    Gu = e1u-col(ku)*e2-col(k)*e2u
    Guu = e1uu-col(kuu)*e2-2*col(ku)*e2u-col(k)*e2uu
    w = c['w']
    Xnew = X+col(w)*G
    Ft, Ftt = Xu+col(w)*Gu, Xuu+col(w)*Guu
    ws, wu, wss, wsu, wuu = (c[q] for q in
        ('ruling_w_s','ruling_w_u','ruling_w_ss','ruling_w_su','ruling_w_uu'))
    ts, tu, tss, tsu, tuu = (c[q] for q in
        ('inlet_t_s','inlet_t_u','inlet_t_ss','inlet_t_su','inlet_t_uu'))
    Xs = col(ws)*G+col(ts)*Ft
    Xn_u = col(wu)*G+col(tu)*Ft
    Xss = 2*col(ws*ts)*Gu+col(ts*ts)*Ftt+col(wss)*G+col(tss)*Ft
    Xsu = col(ws*tu+wu*ts)*Gu+col(ts*tu)*Ftt+col(wsu)*G+col(tsu)*Ft
    Xn_uu = 2*col(wu*tu)*Gu+col(tu*tu)*Ftt+col(wuu)*G+col(tuu)*Ft
    normal = np.cross(Xs, Xn_u)
    area = np.linalg.norm(normal, axis=-1)
    if np.any(area <= 0):
        raise ValueError('Own Cartesian signed map is not immersed')
    normal /= col(area)
    E = np.sum(Xs*Xs, axis=-1)
    F = np.sum(Xs*Xn_u, axis=-1)
    Gm = np.sum(Xn_u*Xn_u, axis=-1)
    L = np.sum(normal*Xss, axis=-1)
    M = np.sum(normal*Xsu, axis=-1)
    Nc = np.sum(normal*Xn_uu, axis=-1)
    det = E*Gm-F*F
    trace = (Gm*L-2*F*M+E*Nc)/det
    gauss = (L*Nc-M*M)/det
    radius = c['new_radius']
    de, df, dg = E-1, F/radius, Gm/(radius*radius)-1
    metric = abs(de+dg)/2+np.sqrt(((de-dg)/2)**2+df*df)
    return dict(c, material_u=np.asarray(inlet['u'])+c['material_shift'],
        X=Xnew, X_s=Xs, X_u=Xn_u, X_ss=Xss, X_su=Xsu, X_uu=Xn_uu,
        N=normal, e1=Xs, e2=Xn_u/radius,
        E=E, F=F, G=Gm, l=L, m=M/radius, n=Nc/(radius*radius),
        metric=metric,
        actual_curvature=abs(trace)/2+np.sqrt(np.maximum(0,trace*trace/4-gauss)),
        actual_K=gauss, ideal_nonzero_curvature=a*n*(1+k*k)/c['D'],
        ideal_n=a*n*(v*c['A'])**2/(c['D']*radius*radius),
        ideal_ratio=(a/v)*k/c['A'],
        inlet_ratio=k, inlet_ratio_u=ku, inlet_ratio_uu=kuu,
        normal_is_own_cross_product=True, continuous_certificate=False)


def at_material(a, v, sigma, material_u, inlet_provider,
                *, tolerance=2e-13, max_iterations=60):
    target = np.asarray(material_u, dtype=float)
    if sigma == 0:
        return propagate(a, v, 0., inlet_provider(target))
    width = np.pi/(2*v)+1e-8
    lo, hi, t = target-width, target+width, target.copy()
    for unused in range(max_iterations):
        data = inlet_provider(t)
        n, m = data['n'], data['m']
        k = m/n
        ku = data['m_u']/n-m*data['n_u']/(n*n)
        c = ruling_coordinates(a, v, sigma, k, ku, np.zeros_like(k))
        residual = t+c['material_shift']-target
        done = abs(residual) <= tolerance
        if np.all(done):
            return propagate(a, v, sigma, data)
        lo = np.where(residual < 0, t, lo)
        hi = np.where(residual > 0, t, hi)
        trial = t-residual/c['U_t']
        trial = np.where((trial <= lo)|(trial >= hi), (lo+hi)/2, trial)
        t = np.where(done, t, trial)
    raise RuntimeError('Signed material inverse exceeded its iteration bound')


def transported_inlet(a, v, sigma, inlet):
    """Complete new inlet through angular order two, on the exact coast.

    The original n,m need three material derivatives. This consumes the
    exact R137 transport identities; it is not valid for an approximate
    independent frame. The position and its displayed two-jets remain those
    of propagate's actual Cartesian formula.
    """
    out=propagate(a,v,sigma,inlet)
    n,m,nu,mu,nuu,muu,nuuu,muuu=(np.asarray(inlet[q]) for q in
        ('n','m','n_u','m_u','n_uu','m_uu','n_uuu','m_uuu'))
    k=out['inlet_ratio'];kt=out['inlet_ratio_u'];ktt=out['inlet_ratio_uu']
    kttt=(muuu-3*nu*ktt-3*nuu*kt-nuuu*k)/n
    w,A,D=out['w'],out['A'],out['D'];wt=out['raw_w_t']
    wtt=-((1+k*k)*wt*wt+4*k*kt*w*wt+(kt*kt+k*ktt)*w*w)/A
    At=2*k*kt*w+(1+k*k)*wt
    Att=2*(kt*kt+k*ktt)*w+4*k*kt*wt+(1+k*k)*wtt
    B=v*(1+k*k)-kt;Bt=2*v*k*kt-ktt;Btt=2*v*(kt*kt+k*ktt)-kttt
    Dt=wt*B+w*Bt;Dtt=wtt*B+2*wt*Bt+w*Btt
    radius=out['new_radius'];nn=out['ideal_n'];kk=out['ideal_ratio']
    h=nu/n+2*At/A-Dt/D
    ht=nuu/n-(nu/n)**2+2*(Att/A-(At/A)**2)-(Dtt/D-(Dt/D)**2)
    nnt=nn*h;nntt=nn*(h*h+ht)
    kkt=(a/v)*(kt/A-k*At/(A*A))
    kktt=(a/v)*(ktt/A-2*kt*At/(A*A)-k*Att/(A*A)+2*k*At*At/(A*A*A))
    mm=kk*nn;mmt=kkt*nn+kk*nnt;mmtt=kktt*nn+2*kkt*nnt+kk*nntt
    tu,tuu=out['inlet_t_u'],out['inlet_t_uu']
    nnu=nnt*tu;mmu=mmt*tu
    nnuu=nntt*tu*tu+nnt*tuu;mmuu=mmtt*tu*tu+mmt*tuu
    d,T,N=out['X_s'],out['X_u']/radius,out['N']
    du=v*T+radius*col(mm)*N;Tu=-v*d+radius*col(nn)*N
    Nu=-radius*(col(mm)*d+col(nn)*T)
    duu=v*Tu+radius*col(mmu)*N+radius*col(mm)*Nu
    Tuu=-v*du+radius*col(nnu)*N+radius*col(nn)*Nu
    return dict(u=out['material_u'],X=out['X'],X_u=out['X_u'],X_uu=out['X_uu'],
                e1=d,e1_u=du,e1_uu=duu,e2=T,e2_u=Tu,e2_uu=Tuu,N=N,N_u=Nu,
                n=nn,m=mm,n_u=nnu,m_u=mmu,n_uu=nnuu,m_uu=mmuu,
                actual_packet=out,exact_coast_transport_identities_used=True)


def at_material_inlet(a,v,sigma,material_u,inlet_provider,**kwargs):
    """Material inverse and transported full inlet, with no angular fitting."""
    packet=at_material(a,v,sigma,material_u,inlet_provider,**kwargs)
    # material_u = inlet_t + material_shift is evaluated on the same lift.
    t=packet['material_u']-packet['material_shift']
    return transported_inlet(a,v,sigma,inlet_provider(t))
