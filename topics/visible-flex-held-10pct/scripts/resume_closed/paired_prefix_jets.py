"""Vectorized paired-coordinate evaluation of the frozen finite Cartesian map.

This evaluator supplies sampled physical-material two-jets for comparisons.
It does not replace the outward continuous geometry certificates.
"""
import numpy as np

def paired_cartesian(prefix,s,psi):
    s=np.asarray(s,float);psi=np.asarray(psi,float)
    if s.ndim!=1 or psi.ndim!=2 or psi.shape[0]!=len(s):raise ValueError('Expected s[S],psi[S,N]')
    coeff=[prefix.rep(s,j).T for j in range(3)]
    ep=np.exp(1j*psi[:,:,None]*prefix.pm)
    phase=psi[:,:,None]*prefix.hm
    basis=[]
    for order in range(3):
        xy=ep*(1j*prefix.pm)**order
        hz=(np.cos(phase)if order==0 else(-np.sin(phase)if order==1 else-np.cos(phase)))*prefix.hm**order
        basis.append((xy,hz))
    pairs=[(0,0),(1,0),(2,0),(0,1),(0,2),(1,1)];jets=[]
    for radial,angular in pairs:
        c=coeff[radial];xy=np.einsum('sk,snk->sn',c[:,:prefix.P],basis[angular][0],optimize=True)
        z=np.einsum('sk,snk->sn',c[:,prefix.P:],basis[angular][1],optimize=True)
        jets.append(np.stack([xy.real,xy.imag,z],axis=-1))
    use=s<=prefix.center_width
    if np.any(use):
        d=prefix.center_delta(psi[use].ravel());w=[prefix.center_weights(s[use],j)for j in range(3)]
        for out,(radial,angular)in zip(jets,pairs):
            dd=d[angular].reshape(3,int(use.sum()),psi.shape[1],3)
            out[use]+=np.einsum('sj,jsuk->suk',w[radial],dd,optimize=True)
    if prefix.end_lift is not None:
        lift=prefix.end_lift;use=s>=lift.end-lift.width
        if np.any(use):
            d=lift.delta(psi[use].ravel());w=[lift.weights(s[use],j)for j in range(3)]
            for out,(radial,angular)in zip(jets,pairs):
                dd=d[angular].reshape(3,int(use.sum()),psi.shape[1],3)
                out[use]+=np.einsum('sj,jsuk->suk',w[radial],dd,optimize=True)
    return jets

def physical_jets(prefix,angle_chart,s,theta):
    s=np.asarray(s,float);theta=np.asarray(theta,float)
    psi=angle_chart.inverse(s[:,None],theta[None,:])
    X,Xs,Xss,Xp,Xpp,Xsp=paired_cartesian(prefix,s,psi)
    _,rho,rhop,ts,tss,rhos=angle_chart.angular(s[:,None],psi)
    v=ts/rho;vp=(rhos*rho-ts*rhop)/rho**2;vs=(tss*rho-ts*rhos)/rho**2
    Fs=Xs-v[:,:,None]*Xp;Ft=Xp/rho[:,:,None]
    Fss=Xss-2*v[:,:,None]*Xsp+(v*v)[:,:,None]*Xpp+(v*vp-vs)[:,:,None]*Xp
    Ftt=Xpp/rho[:,:,None]**2-Xp*(rhop/rho**3)[:,:,None]
    Fst=(Xsp-vp[:,:,None]*Xp-v[:,:,None]*Xpp)/rho[:,:,None]
    return [X,Fs,Fss,Ft,Ftt,Fst]
