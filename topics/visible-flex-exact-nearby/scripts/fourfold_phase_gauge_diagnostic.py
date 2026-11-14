#!/usr/bin/env python3
"""Project actual phase Schur directions onto radial reparameterization.

For each x, xi=<V,Fx>/<Fx,Fx> is the best angular L2 radial coefficient.
Its derivative is evaluated from Vx and Fxx, not from sampled differences.
Also fits a constant Euclidean dilation after radial projection, since the
current numerical equations leave the output mean metric free. Neither a
reparameterization nor a dilation is automatically a homogeneous variation
when a target metric is held fixed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import trapezoid

from fourfold_phase_compare import load
from fourfold_phase_newton import primitive_quarter


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint', type=Path)
    ap.add_argument('directions', type=Path)
    ap.add_argument('--angles', type=int, default=256)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    solver, vector, metadata = load(args.checkpoint)
    with np.load(args.directions, allow_pickle=False) as f:
        if not np.array_equal(f['candidate_vector'], vector):
            raise ValueError('directions and candidate are not the same saved graph')
        basis = f['directions']
        schur_report = json.loads(str(f['metadata']))
    eig, rotation = np.linalg.eigh(np.asarray(schur_report['schur_matrix']))
    names = [f'mean_{j}' for j in range(len(basis))]+['schur_soft', 'schur_middle', 'schur_hard']
    combinations = np.r_[np.eye(len(basis)), rotation.T]
    directions = combinations@basis
    x = np.unique(np.r_[np.linspace(0., .35, 351), np.linspace(.35, 1., 131),
                         np.linspace(1., solver.length, 101)])
    q = args.angles
    sine = np.sin(np.arange(1, solver.modes+1)[:, None]*2*np.pi*np.arange(q)/q)
    reference = {key: np.zeros(len(x)) for key in ('E', 'Ep', 'a', 'ap', 'xiF', 'xiFp')}
    f_perp = np.zeros((len(x), q, 3))
    data = [{key: np.zeros(len(x)) for key in
             ('xi', 'xip', 'dE', 'da', 'meanV2', 'maxV', 'maxNormal', 'lambda_numerator')}
            for _ in names]
    perpendicular = np.zeros((len(names), len(x), q, 3))
    for start in range(0, len(x), 32):
        xx = x[start:start+32]
        sl = slice(start, start+len(xx))
        jets, exact, phase, fields = solver.geometry(vector, xx, angles=q)
        f, fx, ft, fxx, _, _ = jets
        normal = np.cross(ft, fx)
        normal /= np.linalg.norm(normal, axis=2)[:, :, None]
        E = np.mean(np.sum(fx*fx, axis=2), axis=1)
        Ep = 2*np.mean(np.sum(fx*fxx, axis=2), axis=1)
        numeratorF = np.mean(np.sum(f*fx, axis=2), axis=1)
        numeratorFp = E+np.mean(np.sum(f*fxx, axis=2), axis=1)
        xiF, xiFp = numeratorF/E, (numeratorFp*E-numeratorF*Ep)/(E*E)
        fp = f-xiF[:, None, None]*fx
        f_perp[sl] = fp
        mean, mean_x = (solver.mean(xx, solver.unpack(vector)[1], j) for j in (0, 1))
        for key, value in dict(E=E, Ep=Ep, a=mean[:, 0], ap=mean_x[:, 0],
                               xiF=xiF, xiFp=xiFp).items():
            reference[key][sl] = value
        primitive, primitive_x = (primitive_quarter(fields[key]) for key in ('T', 'Tx'))
        for j, direction in enumerate(directions):
            dp = solver.phases(direction, xx, derivatives=1)
            db, dg = dp[0, :, :, 0]@sine, dp[0, :, :, 1]@sine
            dbx, dgx = dp[1, :, :, 0]@sine, dp[1, :, :, 1]@sine
            dt = fields['Tb']*db[:, :, None]+fields['Tg']*dg[:, :, None]
            dtx = (fields['Tb']*dbx[:, :, None]+fields['Tg']*dgx[:, :, None]
                   +fields['Tbx']*db[:, :, None]+fields['Tgx']*dg[:, :, None])
            dprimitive, dprimitive_x = primitive_quarter(dt), primitive_quarter(dtx)
            da_coeff = solver.unpack(direction)[1]
            dm, dmx = (sum((c*sp(xx, nu=nu) for c, sp in zip(da_coeff, solver.mean_splines)),
                           np.zeros((len(xx), 3))) for nu in (0, 1))
            v = dm[:, 0, None, None]*primitive+mean[:, 0, None, None]*dprimitive
            v[..., 2] += dm[:, 2, None]
            vx = (dmx[:, 0, None, None]*primitive+dm[:, 0, None, None]*primitive_x
                  +mean_x[:, 0, None, None]*dprimitive+mean[:, 0, None, None]*dprimitive_x)
            vx[..., 2] += dmx[:, 2, None]
            numerator = np.mean(np.sum(v*fx, axis=2), axis=1)
            numerator_x = np.mean(np.sum(vx*fx+v*fxx, axis=2), axis=1)
            xi, xip = numerator/E, (numerator_x*E-numerator*Ep)/(E*E)
            vp = v-xi[:, None, None]*fx
            perpendicular[j, sl] = vp
            values = dict(xi=xi, xip=xip, dE=2*np.mean(np.sum(fx*vx, axis=2), axis=1),
                          da=dm[:, 0], meanV2=np.mean(np.sum(v*v, axis=2), axis=1),
                          maxV=np.linalg.norm(v, axis=2).max(axis=1),
                          maxNormal=abs(np.sum(v*normal, axis=2)).max(axis=1),
                          lambda_numerator=np.mean(np.sum(vp*fp, axis=2), axis=1))
            for key, value in values.items():
                data[j][key][sl] = value
    report = dict(kind='floating_radial_gauge_and_scale_projection_not_a_kernel_proof',
                  checkpoint=str(args.checkpoint), directions=str(args.directions),
                  radial_samples=len(x), quarter_period_angles=q,
                  norms='coordinate dx times angular mean; pointwise Euclidean vector norms',
                  schur_eigenvalues=eig.tolist(), results=[])
    for j, name in enumerate(names):
        row = dict(name=name, mean_combination=combinations[j].tolist(), domains={})
        for label, endpoint in (('inner_core', .25), ('core', .35), ('body', 1.), ('full_body', solver.length)):
            mask = x <= endpoint+1e-12
            xx = x[mask]
            item = data[j]
            E, Ep, a, ap = (reference[key][mask] for key in ('E', 'Ep', 'a', 'ap'))
            xi, xip, dE, da = (item[key][mask] for key in ('xi', 'xip', 'dE', 'da'))
            vp = perpendicular[j, mask]
            fp = f_perp[mask]
            denominator = float(trapezoid(item['meanV2'][mask], xx))
            radial_error = float(trapezoid(np.mean(np.sum(vp*vp, axis=2), axis=1), xx))
            scale_denominator = float(trapezoid(np.mean(np.sum(fp*fp, axis=2), axis=1), xx))
            scale = float(trapezoid(item['lambda_numerator'][mask], xx))/scale_denominator
            scale_perp = vp-scale*fp
            scale_error = float(trapezoid(np.mean(np.sum(scale_perp*scale_perp, axis=2), axis=1), xx))
            corrected_xi = xi-scale*reference['xiF'][mask]
            corrected_xip = xip-scale*reference['xiFp'][mask]
            row['domains'][label] = dict(
                endpoint=endpoint, variation_L2=float(np.sqrt(denominator)),
                maximum_V=float(item['maxV'][mask].max()),
                maximum_normal_component=float(item['maxNormal'][mask].max()),
                radial_projection_relative_L2=float(np.sqrt(radial_error/denominator)),
                radial_projection_maximum_remainder=float(np.linalg.norm(vp, axis=2).max()),
                maximum_abs_xi=float(abs(xi).max()),
                maximum_relative_delta_E=float(abs(dE/E).max()),
                maximum_relative_delta_a=float(abs(da/a).max()),
                maximum_relative_delta_E_minus_radial_Lie=float(abs((dE-xi*Ep-2*E*xip)/E).max()),
                maximum_relative_delta_a_minus_radial_Lie=float(abs((da-xi*ap)/a).max()),
                fitted_constant_scale=scale,
                scale_plus_radial_relative_L2=float(np.sqrt(scale_error/denominator)),
                scale_plus_radial_maximum_remainder=float(np.linalg.norm(scale_perp, axis=2).max()),
                maximum_relative_delta_E_minus_scale_and_Lie=float(abs(
                    (dE-2*scale*E-corrected_xi*Ep-2*E*corrected_xip)/E).max()),
                maximum_relative_delta_a_minus_scale_and_Lie=float(abs(
                    (da-scale*a-corrected_xi*ap)/a).max()))
        report['results'].append(row)
    report['identities'] = [
        'For V=xi Fx: delta a=xi a_prime; delta E=xi E_prime+2 E xi_prime',
        'For V=lambda F+xi Fx: add lambda a and 2 lambda E to those metric variations',
        'The numerical objective retains only nonmean metric equations; both transformations can change its mean output',
        'A fixed-target homogeneous variation must also satisfy delta a=0 and delta E=0; a small Schur eigenvalue alone does not imply this']
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
