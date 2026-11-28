"""R784. First nonzero spatial Taylor coefficient past the flat developed cap.

On an R786 flat delayed collar this evaluates the ninth-degree physical
correction to the exact R784 Gauss-Codazzi solution. Its six returned slots are
the actual derivatives of the cut polynomial, not derivatives claimed for an
uncomputed solution. The width and true angular/phase supports follow R784.
"""
import numpy as np
import r785_two_cap_separable_world_shear as shear
from r742_tilted_disk_two_jets import J, gather, trig, unary

HALF_BAND = 5.e-8


def smooth(x):
    r = np.clip(x.v, 0., 1.)
    return unary(x, r**3*(10.+r*(-15.+6.*r)), 30.*r**2*(1.-r)**2,
                 60.*r*(1.-r)*(1.-2.*r))


def add_ninth_jet(field, chart, u, b, phase, order):
    if not chart.startswith("end") or phase <= np.pi/4:
        return field
    raw_u, raw_b = np.broadcast_arrays(np.asarray(u,float), np.asarray(b,float))
    theta = raw_u.ravel()/shear.R
    orient = np.floor(theta/(np.pi/2)+.5).astype(int)
    angle = theta - orient*(np.pi/2)
    depth = shear.L - raw_b.ravel()
    use = (depth>0.) & (depth<2*HALF_BAND) & (abs(angle)>.46) & (abs(angle)<.69)
    if not np.any(use):
        return field
    v = J(depth[use],a=-1.)
    phi = J(angle[use],s=1./shear.R)
    absolute = unary(phi, np.abs(phi.v), np.sign(phi.v), np.zeros_like(phi.v))
    time_gate = smooth(J(np.array([(phase-np.pi/4)/(np.pi/12)]))).v[0]
    weight = (time_gate*smooth((absolute-.46)/.02)*smooth((.69-absolute)/.02)
              *smooth((2*HALF_BAND-v)/HALF_BAND))
    ca, sa = trig(phi)
    a0 = shear.R - shear.end_limits(order)[1]
    quadrant = orient[use] % 4
    amplitudes = np.asarray(shear.MILD_ANGLES)[np.array([0,2,1,3])[quadrant]]
    k = amplitudes*np.sin(phase)**2/.0752
    beta = (ca*a0 - a0/np.sqrt(2.) - .08*.06/2)*k
    cb,sb = trig(beta)
    alpha4 = 2.5/(shear.base.RH*shear.SM**3)
    v2=v*v;v4=v2*v2;v8=v4*v4
    lead = weight*(v8*v)*(alpha4**2/(18.*a0))/(J(k)*sa*sa)
    tx = np.array([1.,0.,-1.,0.])[quadrant]
    tz = np.array([0.,1.,0.,-1.])[quadrant]
    delta = gather([-lead*sb*tx,lead*cb,-lead*sb*tz],int(np.sum(use)))
    result=np.array(field,copy=True).reshape(-1,6,3)
    result[use]+=delta
    return result.reshape(field.shape)
