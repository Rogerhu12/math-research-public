"""Actual complete native three-curl change on both U patches for the R760 zero-control branches."""
import numpy as np

import r763_material_twist as twist

model = twist.material


def material_rule(build, phase, order):
    small = phase <= .08
    name, lo, hi = twist.PANELS[0 if small else 1]
    ell, weights = model.moments.rules(np.array([lo, hi]), order)
    # Integrate in physical ell,sigma on both R750 U patches. The polar r
    # instrument is used solely to read actual source quantities and columns.
    u, wu = model.moments.rules(np.array([.01, .99]), order)
    lu, perimeter = build.ring.LU, build.ring.length
    s = np.r_[(2.+lu*u)/perimeter, (4.+lu+lu*u)/perimeter]
    sigma_weights = lu*np.tile(wu, 2)
    length, labels = np.broadcast_arrays(ell[:, None], s[None, :])
    length, labels = length.ravel(), labels.ravel()
    r = build.radius_at(length)
    frame, info = model.axial_jet(build, phase, length, labels, build.r760_small)
    theta, theta_l, original, psi_l, psi_s, T, N, k, ks, theta_s = info
    if np.any(abs(psi_s)+abs(theta_s)>1.e-11):
        raise ArithmeticError('R763 true U test landed outside the uniform R760 foot data')
    _, dist, *_ = build.profile.read(r)
    h = 1.+k*dist
    hp = k*np.sin(original)
    t = np.sin(theta)
    c = np.cos(theta)
    target_t = (k+psi_s)*t
    old = np.column_stack((hp-target_t, h*c*psi_l+theta_s, -h*t*psi_l))
    scalar = twist.initial_twist(phase,3,1.)
    b, br, _ = twist.radial_and_angular(build,3,r,labels)
    er = model.space.ell_data(r)[1]
    a, al = b@scalar, (br@scalar)/er
    w = (weights[:, None]*sigma_weights).ravel()
    return dict(phase=phase,order=order,ell=length,normalized_angles=labels,physical_weights=w,
                h=h,h_ell=hp,theta=theta,theta_ell=theta_l,psi_ell=psi_l,
                k=k,native_curl_in_T_M_L=old,unit_control=a,unit_control_ell=al,
                real_intervals=[lo,hi,.01,.99],name=name)


def measured_change(rows, factor):
    h, hp = rows['h'], rows['h_ell']
    theta, theta_l, twist_l = rows['theta'], rows['theta_ell'], rows['psi_ell']
    t, c = np.sin(theta), np.cos(theta)
    a, al = factor*rows['unit_control'], factor*rows['unit_control_ell']
    sa, ca = np.sin(a), np.cos(a)
    cm = -2.*np.sin(.5*a)**2
    old = rows['native_curl_in_T_M_L']
    delta = np.column_stack((hp*cm-h*sa*(al+c*twist_l),
                             hp*sa+h*(ca*al+cm*c*twist_l),
                             h*(theta_l*sa-twist_l*t*cm)))
    after = old+delta
    weights = rows['physical_weights']
    first = np.column_stack((-h*rows['unit_control']*c*twist_l,
                             hp*rows['unit_control']+h*rows['unit_control_ell'],
                             h*theta_l*rows['unit_control']))
    energy = float(weights@np.einsum('ij,ij->i',old,old))
    diff = float(weights@np.einsum('ij,ij->i',2.*old+delta,delta))
    derivative = float(2.*weights@np.einsum('ij,ij->i',old,first))
    if rows['phase'] and not derivative < 0.:
        raise ArithmeticError('actual material U data contradict the strict three-curl descent')
    return dict(factor=float(factor),source_energy=energy,change=diff,after_energy=energy+diff,
                zero_directional_derivative=derivative,
                three_axis_in_T_M_L=np.max(np.abs(after),axis=0),
                native_peak=float(np.linalg.norm(after,axis=1).max()),
                unchanged_exterior=True)


def guarded_factor(build, phase, paid):
    if not phase:return dict(factor=0.,profile_orders=[],phase=0.)
    profiles=[]
    for order in (24,40):
        key=[phase,order]
        profiles.append(paid.get('r763_actual_U_quadrature',key,
                                  lambda order=order:material_rule(build,phase,order)))
    best=None;tested=[]
    for i in range(23):
        factor=2.**(-i);scores=[]
        for order,row in zip((24,40),profiles,strict=True):
            scores.append(paid.get('r763_full_U_nonlinear_trial',[phase,order,factor],
                                   lambda row=row:measured_change(row,factor)))
        c=[s['change'] for s in scores]
        if abs(c[0]-c[1])>4.e-10*max(1.,abs(c[1])):
            raise ArithmeticError('independent R763 material integral orders disagree')
        tested.append(dict(factor=factor,changes=c))
        if max(c)<0. and (best is None or max(c)<best[0]):
            best=(max(c),factor)
        if best is not None and factor<best[1]/8.:
            break
    if best is None:
        raise ArithmeticError('no finite R763 strict three-component energy descent at either order')
    return dict(factor=best[1],change=best[0],phase=phase,profile_orders=[24,40],trials=tested)
