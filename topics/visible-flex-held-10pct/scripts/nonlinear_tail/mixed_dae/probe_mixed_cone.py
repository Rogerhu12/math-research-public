"""Independent cone regression for the experimental mu-free mixed BVP.

The cone may already have sign-changing A. It is seeded independently at its
own amplitude. No continuation through a Gram singularity is claimed.
"""
from __future__ import annotations
import argparse, hashlib, json, sys, time
from pathlib import Path
import numpy as np
from mu_free_fields import MuFreeFields
from mixed_bvp import MixedBVP


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cone_reference(fields, row, phase):
    d, M = fields.d, fields.modes
    base = np.asarray(row['H'][:M])/(np.sqrt(2)*row['radius']*row['w'])
    if fields.full:
        freq = fields.freq[:M]
        v = np.r_[base*np.cos(freq*phase), base*np.sin(freq*phase)]
    else:
        if phase != 0:
            raise ValueError('A nonzero material phase requires full cos/sin')
        v = base
    Y = np.zeros(fields.width)
    Y[:d] = v
    Y[2*d] = row['meanSlope']/row['w']-1
    Y[2*d+1:] = -(fields.freq**2-1)*v
    scalar_history = []
    for _ in range(16):
        e = fields.evaluate(Y, row['radius'], row['w'], 1., 0., True)
        residual = float(e['moments'][0, 0])
        derivative = float(e['gram'][0, 0, 0])
        scalar_history.append(dict(residual=residual, derivative=derivative))
        if abs(residual) <= 2e-15*max(e['max_quad'], 1e-15):
            break
        if abs(derivative) < 1e-13:
            raise ArithmeticError('Independent scalar mean root is ill conditioned')
        Y[2*d] -= residual/derivative
    e = fields.evaluate(Y, row['radius'], row['w'], 1., 0., True)
    Y[d:2*d] = e['moments'][0, 1:]
    e = fields.evaluate(Y, row['radius'], row['w'], 1., 0., True)
    if np.max(e['root_relative']) > 8e-14:
        raise ArithmeticError('Independent reference mean root was not accepted')
    return Y, scalar_history


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--amplitudes', default='.002,.0088')
    p.add_argument('--modes', default='8,16')
    p.add_argument('--intervals', type=int, default=4)
    p.add_argument('--angular', type=int, default=512)
    p.add_argument('--phase', type=float, default=.17)
    p.add_argument('--cosine-only', action='store_true')
    p.add_argument('--perturbation', type=float, default=1e-5)
    p.add_argument('--span', type=float, default=.02)
    p.add_argument('--max-iterations', type=int, default=16)
    a = p.parse_args()
    if a.cosine_only:
        a.phase = 0.
    inputs = json.loads(a.inputs.read_text())
    document = dict(scope=__doc__, command=sys.argv, inputs_sha256=digest(a.inputs),
                    sources={Path(path).name:digest(path) for path in
                             [__file__, Path(__file__).with_name('mu_free_fields.py'),
                              Path(__file__).with_name('mixed_bvp.py')]},
                    parameters=vars(a).copy(), results=[])
    document['parameters']['inputs'] = str(a.inputs)
    document['parameters']['out'] = str(a.out)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(210223)
    for amp in map(float, a.amplitudes.split(',')):
        row = next(row for row in inputs['rows'] if abs(row['amplitude']-amp) < 1e-14)
        for M in map(int, a.modes.split(',')):
            started = time.monotonic()
            result = dict(amplitude=amp, modes=M, full_cosine_sine=not a.cosine_only,
                          phase=a.phase, intervals=a.intervals, radial_span=a.span,
                          angular=a.angular, perturbation=a.perturbation)
            try:
                f = MuFreeFields(M, 2, a.angular, not a.cosine_only, .01)
                ref, scalar = cone_reference(f, row, a.phase)
                x = np.linspace(0, 1, 2*a.intervals+1)
                def profile(x):
                    return dict(r=row['radius']+a.span*x, w=row['w'], rx=a.span, ell=0.)
                bvp = MixedBVP(f, x, profile, ref[:f.d], ref[f.d:2*f.d])
                Y = np.tile(ref, (len(x), 1))
                initial = Y+a.perturbation*rng.normal(size=Y.shape)*np.maximum(abs(Y), 1e-3)
                check = bvp.evaluate(initial, True)
                direction = rng.normal(size=initial.shape)
                direction /= np.linalg.norm(direction)
                analytic = check['jacobian']@direction.ravel()
                fd = []
                for h in (1e-5, 1e-6, 1e-7):
                    plus = bvp.evaluate(initial+h*direction)['residual']
                    minus = bvp.evaluate(initial-h*direction)['residual']
                    delta = (plus-minus)/(2*h)-analytic
                    fd.append(dict(step=h, absolute=float(np.max(abs(delta))),
                                   relative=float(np.max(abs(delta)))/max(1e-30, float(np.max(abs(analytic))))))
                print(json.dumps(dict(event='mixed_start', **result)), flush=True)
                sol = bvp.solve(initial, max_iterations=a.max_iterations,
                                callback=lambda item:print(json.dumps(dict(event='iteration', **item)), flush=True))
                final = sol['final']
                ref_e = bvp.evaluate(Y, True)
                gram = final['fields']['gram']
                eig = np.linalg.eigvalsh(gram)
                mean_delta = sol['Y'][:, 2*f.d]-(row['meanSlope']/row['w']-1)
                result.update(success=sol['success'], stop_reason=sol['stop_reason'],
                    root_relative=final['root_relative'], ode_residual=final['ode_residual'],
                    boundary_residual=final['boundary_residual'], minD=final['fields']['minD'],
                    minS=final['fields']['minS'], minA=final['fields']['minA'],
                    maxA=final['fields']['maxA'], negative_gram_eigenvalues=int(np.sum(eig[0]<0)),
                    minimum_abs_gram_eigenvalue=float(np.min(abs(eig))),
                    gram_spectral_condition=float(np.max(abs(eig))/np.min(abs(eig))),
                    reference_state_linf_error=float(np.max(abs(sol['Y']-Y))),
                    reference_mean_slope_linf_error=float(np.max(abs(mean_delta))*row['w']),
                    reference_full_residual=float(np.max(abs(ref_e['residual']))),
                    scalar_reference_root_history=scalar, global_jacobian_directional_check=fd,
                    history=sol['history'], elapsed_seconds=time.monotonic()-started)
                checkpoint = a.out.with_name(a.out.stem+f'-a{amp:g}-m{M}.npz')
                np.savez_compressed(checkpoint, x=x, Y=sol['Y'], reference=Y)
                result['checkpoint'] = dict(path=str(checkpoint), sha256=digest(checkpoint))
            except Exception as error:
                result.update(success=False, error=repr(error), elapsed_seconds=time.monotonic()-started)
            document['results'].append(result)
            a.out.write_text(json.dumps(document, indent=2)+'\n')
            print(json.dumps(dict(event='mixed_completed', **result)), flush=True)


if __name__ == '__main__':
    main()
