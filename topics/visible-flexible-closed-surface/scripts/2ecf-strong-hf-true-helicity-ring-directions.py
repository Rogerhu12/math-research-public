"""All-point shear and four full within-ring directional spreads on a physical Gram tensor."""
import numpy as np


def profiles(metric,scale):
    E=1+metric[...,0]
    F=metric[...,1]/np.sqrt(2.)
    G=1+metric[...,2]
    shear=F/np.sqrt(E*G)
    weights=np.array(((1.,0.,0.),(0.,0.,1.),(.5,1.,.5),(.5,-1.,.5)))
    values=weights[:,0,None,None]*E+weights[:,1,None,None]*F+weights[:,2,None,None]*G
    if min(E.min(),G.min(),values.min())<=0:raise ArithmeticError("Actual positive tangent norm required")
    logs=np.log(values)/(2*scale)
    lower,upper=logs.min(axis=2),logs.max(axis=2)
    return E,G,shear,weights,values,logs,lower,upper


def maximum(profile,shear_scale):
    _,_,rho,_,_,_,lo,hi=profile
    return max(float(np.max(abs(rho))/shear_scale),float(np.max(hi-lo)))


def exponentials(profile,w,beta,shift,scale,shear_scale):
    E,G,rho,basis,D,log,lo,hi=profile
    plus=w*np.exp(beta*(rho/shear_scale-shift))
    minus=w*np.exp(beta*(-rho/shear_scale-shift))
    bar=(plus-minus)/shear_scale
    g=np.stack((-bar*rho/(2*E),bar/np.sqrt(E*G),-bar*rho/(2*G)),axis=-1)
    mass=float(np.sum(plus+minus))
    # This equals the full N x N ordered-angle exponential at each radius,
    # with per-pair ds/N^2. Differentiation acts on both actual angle factors.
    for v,d,l,h,L in zip(basis,D,lo,hi,log):
        A=np.exp(beta*(L-h[:,None]))
        B=np.exp(beta*(l[:,None]-L))
        su=A.sum(axis=1);sd=B.sum(axis=1)
        j=w[:,0]/d.shape[1]*np.exp(beta*(h-l-shift))
        mass+=float(np.sum(j*su*sd))
        coeff=j[:,None]*(A*sd[:,None]-B*su[:,None])/(2*scale*d)
        g+=coeff[...,None]*v
    return mass,g
