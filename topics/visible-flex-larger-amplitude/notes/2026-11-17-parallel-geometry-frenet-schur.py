#!/usr/bin/env python3
"""Read-only full finite Frenet Jacobian/left real-Schur diagnostics.

This changes neither the accepted field nor its boundary condition.  A
selected instantaneous invariant subspace is not a nonlinear tail DN map.
Raw reports and matrices belong outside the repository.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.linalg import eigvals, schur, solve, solve_sylvester, subspace_angles
from scipy.linalg.lapack import dtrsen

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile
from parallel_20261117_inward_profile import InwardProfile
from parallel_20261117_continue import physical, projector


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def profile_from(data):
    geometry = data['fixed_scalar_profile']['geometry']
    origin = data['analytic_extension_origin']
    p = data.get('inward_scalar_profile')
    if p:
        return InwardProfile(geometry, origin, p['cut'], p['curvature'],
                             p['ramp_in'], p['ramp_out'])
    return Profile(geometry, origin)


def modal_energy(rows, modes):
    energy = [float(np.sum(rows[:, [0, 2*modes+1]]**2))]
    for j in range(1, modes+1):
        energy.append(float(np.sum(rows[:, [j, modes+j, 2*modes+1+j]]**2)))
    total = sum(energy)
    return dict(total=total, modes_0_to_3_fraction=sum(energy[:4])/total,
                modes_0_to_10_fraction=sum(energy[:11])/total,
                mean_mode=sum(j*x for j, x in enumerate(energy))/total,
                energy=energy)


def selected_left(A, predicate, modes, principal):
    T, Q, dim = schur(A.T, output='real', sort=lambda re, im: predicate(re))
    n = len(A)
    if dim == 0 or dim == n:
        return dict(dimension=int(dim)), None
    select = np.r_[np.ones(dim, dtype=np.int32), np.zeros(n-dim, dtype=np.int32)]
    Ts, Qs, wr, wi, count, reciprocal_mean_condition, sep, info = dtrsen(
        select, T, Q, job='B', wantq=1,
        lwork=max(1, 2*dim*(n-dim)), liwork=max(1, dim*(n-dim)))
    if info != 0 or count != dim:
        raise RuntimeError(f'dtrsen failed: info={info}, count={count}, expected={dim}')
    L = Qs[:, :dim].T
    restricted = Ts[:dim, :dim].T
    residual = L @ A - restricted @ L
    normA = np.linalg.norm(A, 2)
    X = solve_sylvester(Ts[:dim, :dim], -Ts[dim:, dim:], -Ts[:dim, dim:])
    sylv = Ts[:dim, :dim] @ X - X @ Ts[dim:, dim:] + Ts[:dim, dim:]
    info = dict(dimension=int(dim), orthogonality_error_2=float(np.linalg.norm(L@L.T-np.eye(dim), 2)),
                row_condition_2=float(np.linalg.cond(L)),
                invariance_residual_2=float(np.linalg.norm(residual, 2)),
                invariance_relative_A_2=float(np.linalg.norm(residual, 2)/normA),
                schur_reconstruction_relative_fro=float(np.linalg.norm(A.T-Qs@Ts@Qs.T)/np.linalg.norm(A)),
                selected_real_min=float(wr[:dim].min()), selected_real_max=float(wr[:dim].max()),
                selected_imaginary_abs_max=float(np.max(abs(wi[:dim]))),
                complement_real_min=float(wr[dim:].min()), complement_real_max=float(wr[dim:].max()),
                lapack_reciprocal_mean_eigenvalue_condition=float(reciprocal_mean_condition),
                lapack_invariant_subspace_sep_estimate=float(sep), sep_over_A_norm_2=float(sep/normA),
                oblique_spectral_projector_norm_2=float(np.sqrt(1+np.linalg.norm(X, 2)**2)),
                sylvester_relative_residual=float(np.linalg.norm(sylv)/(np.linalg.norm(Ts)*np.linalg.norm(X)+np.linalg.norm(Ts[:dim,dim:]))),
                modal_energy=modal_energy(L, modes))
    if principal is not None:
        angles = subspace_angles(L.T, principal.T)
        info['principal_rowspace_angle_degrees'] = dict(
            maximum=float(np.degrees(angles.max())), minimum=float(np.degrees(angles.min())),
            root_mean_square=float(np.degrees(np.sqrt(np.mean(angles**2)))))
    return info, L


def moving_frame_map(q, z, derivative=True):
    d, V, n = z['d'], z['V'], z['normal']
    length = np.linalg.norm(d, axis=1)
    ephi = d/length[:, None]
    es = np.cross(ephi, n)
    axes = (es, ephi, n)
    T = np.empty((q.n, q.n))
    Ts = np.empty_like(T) if derivative else None
    if derivative:
        ep_s = (z['dV']-ephi*np.sum(ephi*z['dV'], axis=1)[:, None])/length[:, None]
        cross_s = np.cross(z['Acc'], d)+np.cross(V, z['dV'])
        ns = (cross_s-n*np.sum(n*cross_s, axis=1)[:, None])/z['area'][:, None]
        es_s = np.cross(ep_s, n)+np.cross(ephi, ns)
        axes_s = (es_s, ep_s, ns)
    for j in range(q.n):
        basis = np.zeros(q.n); basis[j] = 1
        U, _, _ = q.jet(basis)
        T[:, j] = q.project(np.column_stack([np.sum(U*v, axis=1) for v in axes]))
        if derivative:
            Ts[:, j] = q.project(np.column_stack([np.sum(U*v, axis=1) for v in axes_s]))
    return T, Ts


def moving_diagnose(q, y, profile, s, A, geom, principal, fixed_modes):
    T, Ts = moving_frame_map(q, geom)
    B = solve(T.T, (T@A+Ts).T).T
    principal_frame = solve(T.T, principal.T).T
    ev = eigvals(B); ev = ev[np.argsort(ev.real)]
    d = q.M-fixed_modes
    lo, hi = float(ev.real[-d-1]), float(ev.real[-d])
    threshold = (lo+hi)/2
    scale = np.linalg.norm(B, 2)
    out = dict(definition='T=P_M(deltaF.es,deltaF.ephi,deltaF.n); B=(T A+T_s)T^-1',
               T_condition_2=float(np.linalg.cond(T)), T_norm_2=float(np.linalg.norm(T,2)),
               Ts_norm_2=float(np.linalg.norm(Ts,2)), B_norm_2=float(scale),
               B_numeric_abscissa=float(np.linalg.eigvalsh((B+B.T)/2)[-1]),
               transformation_relative_residual=float(np.linalg.norm(B@T-T@A-Ts)/(np.linalg.norm(T@A)+np.linalg.norm(Ts))),
               positive_counts={str(t):int(np.sum(ev.real>t)) for t in (1e-6,.01,.1,1.,2.,5.,10.)},
               negative_counts={str(t):int(np.sum(ev.real < -t)) for t in (1e-6,.01,.1,1.,2.,5.,10.)},
               eigenvalues_real_imag=[[float(x.real),float(x.imag)] for x in ev],
               max_absolute_imaginary=float(np.max(abs(ev.imag))),
               selection_real_gap=dict(lower=lo,upper=hi,gap=hi-lo,threshold=threshold))
    checks=[]
    for h in (1e-6, 5e-7):
        yp, ypp = geom['yp'], geom['ypp']
        pm=[]
        for sign in (-1,1):
            nearby=physical(q,y+sign*h*yp+.5*h*h*ypp,profile,s+sign*h)
            pm.append(moving_frame_map(q, nearby, derivative=False)[0])
        derivative=(pm[1]-pm[0])/(2*h)
        checks.append(dict(step=h,relative_fro=float(np.linalg.norm(derivative-Ts)/np.linalg.norm(Ts)),
                           absolute_max=float(np.max(abs(derivative-Ts)))))
    out['Ts_centered_jet_checks']=checks
    if hi-lo>1e-8:
        chosen,L=selected_left(B,lambda re:re>threshold,q.M,principal_frame)
        original=L@T
        restricted=L@B@L.T
        covariant=original@A+L@Ts-restricted@original
        angles=subspace_angles(original.T,principal.T)
        chosen.update(original_rows_condition_2=float(np.linalg.cond(original)),
                      original_covariant_relative_residual=float(np.linalg.norm(covariant,2)/(np.linalg.norm(original,2)*np.linalg.norm(A,2)+np.linalg.norm(L@Ts,2))),
                      original_principal_rowspace_angle_degrees=dict(maximum=float(np.degrees(angles.max())),
                      root_mean_square=float(np.degrees(np.sqrt(np.mean(angles**2))))))
        out['fastest_target_dimension']=chosen
    mlo,mhi=float(ev.real[-q.M-1]),float(ev.real[-q.M])
    out['fastest_M_gap']=dict(lower=mlo,upper=mhi,gap=mhi-mlo)
    if mhi-mlo>1e-8:
        out['fastest_M_dimension'],_=selected_left(B,lambda re:re>(mlo+mhi)/2,q.M,None)
    return out


def diagnose(path, fixed_modes):
    raw = Path(path).read_bytes()
    data = json.loads(gzip.decompress(raw))
    if not data.get('success'):
        raise ValueError('Input is not an accepted field')
    q = Frenet(data['M'], data['N'])
    s = float(data['mesh'][-1]); y = np.asarray(data['states'][-1])
    profile = profile_from(data); a, ap, app = profile(s)
    A = q.jacobian(y, ap/a)
    rng = np.random.default_rng(20261117)
    checks = []
    for j in range(5):
        v = rng.normal(size=q.n); v /= np.linalg.norm(v)
        Av = A@v; direct = q.jvp(y, ap/a, v)
        complex_step = q.rhs(y+1j*1e-24*v, ap/a).imag/1e-24
        checks.append(dict(direction=j,
                           jvp_relative=float(np.linalg.norm(Av-direct)/np.linalg.norm(direct)),
                           complex_step_relative=float(np.linalg.norm(Av-complex_step)/np.linalg.norm(complex_step))))
    ev = eigvals(A)
    order = np.argsort(ev.real)
    ev = ev[order]
    principal, geom = projector(q, y, profile, s, fixed_modes)
    target_dim = q.M-fixed_modes
    lo = float(ev.real[-target_dim-1]); hi = float(ev.real[-target_dim])
    threshold = (lo+hi)/2
    record = dict(input_path=str(path), input_sha256=hashlib.sha256(raw).hexdigest(),
                  M=q.M, N=q.N, dimension=q.n, endpoint=s, scalar_a=float(a), scalar_ap=float(ap),
                  scalar_app=float(app), scalar_k=float(ap/a), inward_scalar_profile=data.get('inward_scalar_profile'),
                  matrix_norm_2=float(np.linalg.norm(A,2)), matrix_norm_fro=float(np.linalg.norm(A)),
                  matrix_max_abs=float(np.max(abs(A))),
                  matrix_numeric_abscissa=float(np.linalg.eigvalsh((A+A.T)/2)[-1]),
                  zero_height_column_norm=float(np.linalg.norm(A[:,2*q.M+1])),
                  derivative_checks=checks,
                  positive_counts={str(t): int(np.sum(ev.real>t)) for t in (0.,1e-10,1e-8,1e-6,1e-4,.01,.1,1.)},
                  negative_counts={str(t): int(np.sum(ev.real < -t)) for t in (0.,1e-10,1e-8,1e-6,1e-4,.01,.1,1.)},
                  max_absolute_imaginary=float(np.max(abs(ev.imag))),
                  eigenvalues_real_imag=[[float(x.real),float(x.imag)] for x in ev],
                  principal_row_condition_2=float(np.linalg.cond(principal)),
                  target_dimension=target_dim, selection_real_gap=dict(lower=lo,upper=hi,gap=hi-lo,threshold=threshold))
    positive, _ = selected_left(A, lambda re: re>1e-6, q.M, principal)
    record['positive_above_1e_minus_6'] = positive
    if hi-lo > 1e-8:
        selected, L = selected_left(A, lambda re: re>threshold, q.M, principal)
        record['fastest_target_dimension'] = selected
        slow, _ = selected_left(A, lambda re: 1e-6<re<threshold, q.M, None)
        record['omitted_slow_positive'] = slow
        if selected['dimension'] != target_dim:
            record['target_selection_warning'] = 'Threshold did not give target dimension; a real Schur pair cannot be split.'
    else:
        record['target_selection_warning'] = 'No distinct growth-rate threshold at requested dimension.'
    record['moving_frame']=moving_diagnose(q,y,profile,s,A,geom,principal,fixed_modes)
    return record


def main(args):
    result = dict(scope=__doc__, source_sha256=sha(__file__), numpy_version=np.__version__, scipy_version=scipy.__version__,
                  dependencies={str(p.relative_to(SCRIPTS.parent)):sha(p) for p in [
                      SCRIPTS/'parallel_20261117_frenet_symbol.py', SCRIPTS/'parallel_20261117_profile.py',
                      SCRIPTS/'parallel_20261117_inward_profile.py', SCRIPTS/'parallel_20261117_continue.py']},
                  inputs=[])
    for path in args.inputs:
        z = diagnose(path, args.fixed_modes); result['inputs'].append(z)
        short={k:v for k,v in z.items() if k not in ('eigenvalues_real_imag','inward_scalar_profile','moving_frame')}
        for name in ('positive_above_1e_minus_6','fastest_target_dimension','omitted_slow_positive'):
            if name in short and 'modal_energy' in short[name]:
                short[name]=dict(short[name]); short[name]['modal_energy']={k:v for k,v in short[name]['modal_energy'].items() if k!='energy'}
        print(json.dumps(short),flush=True)
        frame=z['moving_frame']
        print(json.dumps(dict(endpoint=z['endpoint'],moving_frame={k:v for k,v in frame.items()
            if k not in ('eigenvalues_real_imag','fastest_target_dimension','fastest_M_dimension')},
            moving_target={k:v for k,v in frame.get('fastest_target_dimension',{}).items() if k!='modal_energy'},
            moving_M={k:v for k,v in frame.get('fastest_M_dimension',{}).items() if k!='modal_energy'})),flush=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs',type=Path,nargs='+',required=True)
    p.add_argument('--fixed-modes',type=int,default=3)
    p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
