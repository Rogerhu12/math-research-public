#!/usr/bin/env python3
"""Actual endpoint-jet C2 completion to a flat circular cuff.

The exact construction uses the actual boundary functions and matches their
radial 0/1/2 jets.  This program evaluates it on exported angular samples and
uses literal angular derivatives, never a Darboux prediction.  It defines a
new fixed reference metric only beyond the given finite tail endpoint.
"""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


P = (np.array([1., 0., 0., -10., 15., -6.]),
     np.array([0., 1., 0., -6., 8., -3.]),
     np.array([0., 0., .5, -1.5, 1.5, -.5]))


def derivative(values, order=1):
    n = len(values)
    factor = (1j*np.fft.fftfreq(n, d=1/n))**order
    if order % 2:
        factor[n//2] = 0.
    return np.fft.ifft(np.fft.fft(values, axis=0)*factor.reshape((n,)+(1,)*(values.ndim-1)), axis=0).real


def fourier_interval(values):
    coefficient = np.fft.rfft(values)/len(values)
    radius = 2*np.sum(abs(coefficient[1:-1]))+abs(coefficient[-1])
    return float(coefficient[0].real-radius), float(coefficient[0].real+radius)


def height_jets(u, *, width, w0, w1, mean_height, hb, hrb, hrrb, lift=0.):
    """Evaluate the same height formula at arbitrary supplied angle values.

    hb/hrb/hrrb can be exact finite-mode evaluations at Theta(phi); no angular
    grid interpolation is required.  mean_height is any one fixed reference
    height at the inner boundary, and lift is selected once for the new g.
    """
    u = np.atleast_1d(np.asarray(u, dtype=float))
    hb, hrb, hrrb = (np.atleast_1d(np.asarray(a)) for a in (hb, hrb, hrrb))
    coefficient = np.array([w0, width*w1, -3*w0-2*width*w1+lift,
                            2*w0+width*w1-2*lift, lift])
    w = np.polynomial.polynomial.polyval(u, coefficient)
    wr = np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(coefficient))/width
    mean = mean_height+width*np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyint(coefficient))
    h = np.broadcast_to(mean[:, None], (len(u), len(hb))).copy()
    hr = np.broadcast_to(w[:, None], h.shape).copy()
    hrr = np.broadcast_to(wr[:, None], h.shape).copy()
    for j, delta in enumerate((hb-mean_height, hrb-w0, hrrb-w1)):
        h += (np.polynomial.polynomial.polyval(u, P[j])*width**j)[:, None]*delta
        hr += (np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(P[j]))*width**(j-1))[:, None]*delta
        hrr += (np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(P[j], 2))*width**(j-2))[:, None]*delta
    return dict(h=h, hr=hr, hrr=hrr, w=w, wr=wr, mean_height=mean)


def jets(u, endpoint, lift):
    radius = float(endpoint['r']); width = float(endpoint['width'])
    theta, rho, rho_phi = (endpoint[key] for key in ('Theta', 'rho', 'rho_phi'))
    w0, w1, h0 = (float(endpoint[key]) for key in ('w', 'wr', 'mean_height'))
    er = np.column_stack((np.cos(theta), np.sin(theta), np.zeros(len(theta))))
    et = np.column_stack((-np.sin(theta), np.cos(theta), np.zeros(len(theta))))
    b0 = radius*er; b0[:, 2] = h0
    b1 = er.copy(); b1[:, 2] = w0
    b2 = np.zeros_like(er); b2[:, 2] = w1
    delta = [endpoint[key]-base for key, base in zip(('F', 'Fr', 'Frr'), (b0, b1, b2))]
    delta_phi = [endpoint['Fphi']-radius*rho[:, None]*et,
                 endpoint['Frphi']-rho[:, None]*et,
                 derivative(delta[2])]
    angular_second_base = rho_phi[:, None]*et-rho[:, None]**2*er
    delta_phiphi = [endpoint['Fphiphi']-radius*angular_second_base,
                    derivative(delta[1], 2), derivative(delta[2], 2)]
    w_coefficient = np.array([w0, width*w1, -3*w0-2*width*w1+lift,
                              2*w0+width*w1-2*lift, lift])
    w = np.polynomial.polynomial.polyval(u, w_coefficient)
    wr = np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(w_coefficient))/width
    h = h0+width*np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyint(w_coefficient))
    r = radius+width*u
    F = r[:, None, None]*er[None, :, :]; F[:, :, 2] = h[:, None]
    Fr = np.broadcast_to(er, F.shape).copy(); Fr[:, :, 2] = w[:, None]
    Frr = np.zeros_like(F); Frr[:, :, 2] = wr[:, None]
    Fphi = r[:, None, None]*rho[None, :, None]*et[None, :, :]
    Fphiphi = r[:, None, None]*angular_second_base[None, :, :]
    Frphi = np.broadcast_to(rho[:, None]*et, F.shape).copy()
    for j in range(3):
        p = np.polynomial.polynomial.polyval(u, P[j])*width**j
        pr = np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(P[j]))*width**(j-1)
        prr = np.polynomial.polynomial.polyval(u, np.polynomial.polynomial.polyder(P[j], 2))*width**(j-2)
        F += p[:, None, None]*delta[j][None, :, :]
        Fr += pr[:, None, None]*delta[j][None, :, :]
        Frr += prr[:, None, None]*delta[j][None, :, :]
        Fphi += p[:, None, None]*delta_phi[j][None, :, :]
        Fphiphi += p[:, None, None]*delta_phiphi[j][None, :, :]
        Frphi += pr[:, None, None]*delta_phi[j][None, :, :]
    return dict(F=F, Fr=Fr, Frr=Frr, Fphi=Fphi, Fphiphi=Fphiphi, Frphi=Frphi,
                w=w, wr=wr, r=r, h=h, delta=delta, w_coefficients=w_coefficient)


def geometry(jet, rho):
    F, Fr, Frr, Fphi, Fphiphi, Frphi = (jet[key] for key in ('F', 'Fr', 'Frr', 'Fphi', 'Fphiphi', 'Frphi'))
    E = np.sum(Fr*Fr, axis=2); B = np.sum(Fr*Fphi, axis=2); G = np.sum(Fphi*Fphi, axis=2)
    E0, G0 = 1+jet['w'][:, None]**2, (jet['r'][:, None]*rho)**2
    e, f, g = E/E0-1, B/np.sqrt(E0*G0), G/G0-1
    op = (abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    cross = np.cross(Fr, Fphi); det = np.sum(cross*cross, axis=2)
    n = cross/np.sqrt(det)[:, :, None]
    ee, ff, gg = (np.sum(a*n, axis=2) for a in (Frr, Frphi, Fphiphi))
    trace = (ee*G+gg*E-2*ff*B)/det; gauss = (ee*gg-ff*ff)/det
    curvature = (abs(trace)+np.sqrt(np.maximum(0., trace*trace-4*gauss)))/2
    xy = F[:, :, :2]; radius = np.linalg.norm(xy, axis=2)
    polar = (xy[:, :, 0]*Fphi[:, :, 1]-xy[:, :, 1]*Fphi[:, :, 0])/radius**2
    jac = Fr[:, :, 0]*Fphi[:, :, 1]-Fr[:, :, 1]*Fphi[:, :, 0]
    return dict(op=op, e=e, f=f, g=g, curvature=curvature, determinant=det,
                polar_derivative=polar, planar_jacobian=jac)


def run(args):
    raw = args.jets.read_bytes()
    with np.load(args.jets, allow_pickle=False) as archive:
        endpoint = {key: archive[key] for key in archive.files}
    width = args.cuff_radius-float(endpoint['r'])
    if width <= 0:
        raise ValueError('The flat cuff must have larger reference radius')
    endpoint['width'] = width
    w0, w1, h0 = (float(endpoint[key]) for key in ('w', 'wr', 'mean_height'))
    d0 = endpoint['F'][:, 2]-h0
    d1 = endpoint['Fr'][:, 2]-w0
    d2 = endpoint['Frr'][:, 2]-w1
    height_lift_threshold = 30*d0/width+12*d1+1.5*width*d2-3*w0-width*w1
    threshold_interval = fourier_interval(height_lift_threshold)
    if args.lift == 'auto':
        lift = max(0., threshold_interval[1])+1e-12
    else:
        lift = float(args.lift)
    if lift < 0:
        raise ValueError('The optional reference-height lift must be nonnegative')
    u = np.linspace(0., 1., args.radial_points)
    maximum = {key: 0. for key in ('gram_operator', 'rr', 'rphi', 'phiphi', 'principal_curvature', 'origin_norm')}
    minimum = {key: float('inf') for key in ('gram_determinant', 'height_radial_derivative', 'polar_angle_derivative', 'planar_jacobian')}
    zmin = float('inf'); zmax = -float('inf'); witness_distance = float('inf')
    worst = {}; worst_curvature = {}; first = None; last = None
    for start in range(0, len(u), 32):
        us = u[start:start+32]; q = jets(us, endpoint, lift); g = geometry(q, endpoint['rho'])
        if first is None:
            first = {key: q[key][0].copy() for key in ('F', 'Fr', 'Frr')}
        last = {key: q[key][-1].copy() for key in ('F', 'Fr', 'Frr')}
        if g['op'].max() > maximum['gram_operator']:
            i, j = np.unravel_index(np.argmax(g['op']), g['op'].shape)
            worst = dict(u=float(us[i]), r=float(q['r'][i]), phi=float(endpoint['phi'][j]),
                         rr=float(g['e'][i,j]), rphi=float(g['f'][i,j]), phiphi=float(g['g'][i,j]))
            maximum['gram_operator'] = float(g['op'][i,j])
        if g['curvature'].max() > maximum['principal_curvature']:
            i, j = np.unravel_index(np.argmax(g['curvature']), g['curvature'].shape)
            worst_curvature = dict(u=float(us[i]), r=float(q['r'][i]), phi=float(endpoint['phi'][j]))
            maximum['principal_curvature'] = float(g['curvature'][i,j])
        for key, source in [('rr','e'),('rphi','f'),('phiphi','g')]:
            maximum[key] = max(maximum[key],float(np.max(abs(g[source]))))
        maximum['origin_norm'] = max(maximum['origin_norm'],float(np.linalg.norm(q['F'],axis=2).max()))
        for key, value in [('gram_determinant',g['determinant']),('height_radial_derivative',q['Fr'][:,:,2]),
                           ('polar_angle_derivative',g['polar_derivative']),('planar_jacobian',g['planar_jacobian'])]:
            minimum[key] = min(minimum[key],float(value.min()))
        zmin = min(zmin,float(q['F'][:,:,2].min()));zmax=max(zmax,float(q['F'][:,:,2].max()))
        if args.witness_major is not None:
            witness_distance=min(witness_distance,float(np.linalg.norm(q['F']-np.array([0.,args.witness_major,0.]),axis=2).min()))
    end = jets(np.array([1.]),endpoint,lift)
    theta = endpoint['Theta']
    target0 = np.column_stack((args.cuff_radius*np.cos(theta),args.cuff_radius*np.sin(theta),np.full(len(theta),end['h'][0])))
    target1 = np.column_stack((np.cos(theta),np.sin(theta),np.zeros(len(theta))))
    result = dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        end_jets_sha256=hashlib.sha256(raw).hexdigest(),
        endpoint_identity=json.loads(str(endpoint['identity_json'])),
        r_inner=float(endpoint['r']),cuff_radius=args.cuff_radius,width=width,
        angle_points=len(theta),radial_points=args.radial_points,height_lift=lift,
        height_lift_threshold_sampled_max=float(height_lift_threshold.max()),
        height_lift_threshold_fourier_upper=threshold_interval[1],
        height_a0_fourier_lower=fourier_interval(endpoint['Fr'][:,2])[0],
        height_a1_fourier_lower=fourier_interval(2*endpoint['Fr'][:,2]+width*endpoint['Frr'][:,2])[0],
        reference_w_coefficients=end['w_coefficients'].tolist(),
        cuff_height=float(end['h'][0]),height_range=[zmin,zmax],maxima=maximum,minima=minimum,
        minimum_witness_distance=None if args.witness_major is None else witness_distance,
        worst_metric=worst,worst_curvature=worst_curvature,
        inner_jet_join_errors={key:float(np.max(np.linalg.norm(first[key]-endpoint[key],axis=1))) for key in first},
        outer_flat_jet_errors={key:float(np.max(np.linalg.norm(last[key]-target,axis=1))) for key,target in
                              [('F',target0),('Fr',target1),('Frr',np.zeros_like(target1))]},
        initial_correction_jet_norms=[float(np.linalg.norm(a,axis=1).max()) for a in end['delta']],
        status='Concrete C2 formula using exact boundary functions; sampled metric/curvature/position evidence, not a continuous or closed-surface certificate',
        reference_metric='Original finite metric retained inside; beyond r_inner use (1+w_new(r)^2)dr^2+r^2*rho(phi)^2*dphi^2, w_new polynomial shown')
    text = json.dumps(result,indent=2)+'\n'
    if args.out:args.out.write_text(text)
    print(text,end='')


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--jets',type=Path,required=True)
    p.add_argument('--cuff-radius',type=float,required=True)
    p.add_argument('--lift',default='auto')
    p.add_argument('--radial-points',type=int,default=257)
    p.add_argument('--witness-major',type=float)
    p.add_argument('--out',type=Path)
    run(p.parse_args())
