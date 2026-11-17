#!/usr/bin/env python3
"""Compare original and complete-reference/C2-window m3 endpoint initializers.

Read-only finite diagnostics.  No BVP or new nonlinear tail solve is run.
The old accepted coefficient field is multiplied by its recorded gauge q;
the new field uses the different new gauge.  geo already contains the exact
core lift once.  Dynamical mean height remains outside the nonmean Z basis.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import json
from pathlib import Path
import sys
import numpy as np
from scipy.interpolate import PPoly
from scipy.integrate import _bvp
from m3_raw_diagnostic_model import RawDiagnosticEnvironment, sha
from couple_m3_smallcut_secant import accepted_anchor


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--projection-angular', type=int, default=4096)
    a = p.parse_args()
    run = a.run.resolve()
    launch = json.loads((run/'continuation-command.json').read_text())
    command = launch['command']
    def argument(key):
        return command[command.index('--'+key)+1]
    source, bridge = Path(argument('source-topic')), Path(argument('short-bridge'))
    restart = Path(argument('restart'))
    old = json.loads(gzip.decompress(restart.read_bytes()))
    accepted_anchor(old, restart)
    profile = json.loads(Path(argument('profile')).read_text())
    chart = json.loads(Path(argument('chart')).read_text())
    port_path = Path(argument('linear-port'))
    port = json.loads(port_path.read_text()); port['_sha256'] = sha(port_path)
    settings = json.loads((run/'seed-round-record.json').read_text())['settings']
    N = int(argument('angular')); M = int(argument('modes'))
    q_new = float(argument('amplitude'))
    if (M != old['config']['modes'] or chart != old['chart'] or
            profile != old['frozen_profile']):
        raise ValueError('This comparison requires the actual same-mode, same-profile entrance')
    env = RawDiagnosticEnvironment(source, bridge, chart, old['core_round_settings'])
    oldobj = env.make(old['core_round_settings'], old['frozen_profile'], port,
        old['gauge_amplitude'], M, N, True, old['warp_reference_q'])
    oldobj.pscale = np.asarray(old['central_correction_scales']).copy()
    oldpar = np.asarray(old['parameters']).copy()
    if not old['config']['fixed_metric']:
        oldpar[0] = 0.
    oldobj.initial(oldpar); oldf = oldobj.flow(oldpar[0]); oldcore = oldobj._core
    if oldobj.support_amplitude != old['actual_primary_amplitude']:
        raise ValueError('The original actual amplitude was not preserved')
    from curve_stable_prefix_bvp import load_checkpoint
    decoded = load_checkpoint(restart)
    oldpp = PPoly.construct_fast(np.asarray(decoded['pp_coefficients']),
        np.asarray(decoded['mesh']), extrapolate=False, axis=1)
    obj = env.make(settings, profile, port, q_new, M, N, False,
                   float(argument('warp-reference')))
    obj.restart_remesh = int(argument('nodes'))
    obj.bcweights = np.full(M, float(argument('physical-bc-tol'))/float(argument('bc-tol')))
    t, original, par = obj.restart(restart)
    initial = obj.initial(par); f = obj.flow(par[0]); newcore = obj._core
    s, _ = obj.chart(t, par[0])
    if f.end != oldf.end or f.warp_e != oldf.warp_e:
        raise ValueError('A genuine material-angle pullback is required for changed charts')
    tail_path = run/'seed_tail_0002.json.gz'
    tail = json.loads(gzip.decompress(tail_path.read_bytes()))
    if not tail['response']['converged']:
        raise ValueError('The original inner affine DN has no accepted actual anchor')
    H0 = np.asarray(tail['request']['height'])
    obj.tail = env.coupler.AffineTailForInnerBVP(H0, tail['response'], M)
    B = f.basis(a.projection_angular)[0]
    oldB = oldf.basis(a.projection_angular)[0]
    finite_only = oldpp(s) * oldobj.q / obj.q
    projected = np.empty_like(original)
    projection_error = 0.; chart_error = 0.
    for first in range(0, len(s), 16):
        sl = slice(first, first+16)
        oldgeo, newgeo = oldf.geo(s[sl], a.projection_angular), f.geo(s[sl], a.projection_angular)
        chart_error = max(chart_error, float(abs(oldgeo['theta']-newgeo['theta']).max()))
        previous = oldgeo['pos'] + oldobj.q * oldf.values(oldpp(s[sl]), oldB)
        projected[:, sl] = f.project(previous-newgeo['pos'], B)/obj.q
        projection_error = max(projection_error, float(abs(
            newgeo['pos']+obj.q*f.values(projected[:,sl],B)-previous).max()))
    if chart_error != 0.:
        raise ValueError('The two angular charts are not bitwise identical in the finite check')
    cutoff = (f.Tu if f.direction=='outward' else f.Td)/2
    cubic = np.maximum(0., 1-s/cutoff)**3
    u = np.clip((s-.5*f.prefix_end)/(.4*f.prefix_end), 0., 1.)
    smooth = f.profile(s)[0]*(1-u**3*(10-15*u+6*u*u))
    make = lambda base, weight: base + (initial-base[:,0])[:,None]*weight[None,:]
    variants = dict(original_material_restart=original,
        complete_reference_cubic=make(projected, cubic),
        finite_only_shared_C2_window=make(finite_only, smooth),
        complete_reference_shared_C2_window=make(projected, smooth))
    inlet_geo_old, inlet_geo_new = oldf.geo(np.array([0.]), a.projection_angular), f.geo(np.array([0.]), a.projection_angular)
    base_inlet = [oldpp(0., j)*oldobj.q/obj.q for j in range(3)]
    projected_inlet = [base_inlet[j] + f.project(
        inlet_geo_old[key]-inlet_geo_new[key], B)[:,0]/obj.q
        for j,key in enumerate(('pos','s1','s2'))]
    target1 = f.fun(np.array([0.]), initial[:,None], par)[:,0]
    fr,_,dW = f.velocity_s(np.array([0.]),initial[:,None],target1[:,None])
    target2 = f.project(dW-fr['geo']['s2'], f.B)[:,0]/obj.q
    target = [initial, target1, target2]
    rows = {}
    for name, y in variants.items():
        is_projected = name.startswith('complete_reference')
        base = projected_inlet if is_projected else base_inlet
        repair = initial-base[0]
        weight_jets = [1.,0.,0.] if 'C2_window' in name else [1.,-3/cutoff,6/cutoff**2]
        inlet = [float(abs(base[j]+repair*weight_jets[j]-target[j]).max()) for j in range(3)]
        row = dict(inlet_coefficient_jet_errors=inlet,
            inlet_value_error=float(abs(y[:,0]-initial).max()),
            boundary_residual=float(abs(obj.bc(y[:,0],y[:,-1],par)).max()),
            terminal_height_change=float(abs(obj.bridge.sigma*obj.q*y[obj.iz:,-1]-H0).max()))
        try:
            h = np.diff(t)
            col, middle, rhs, rhs_middle = _bvp.collocation_fun(obj.fun,y,par,t,h)
            spline = _bvp.create_spline(y,rhs,t,h)
            rms = _bvp.estimate_rms_residuals(obj.fun,spline,t,h,par,1.5*col/h,rhs_middle)
            minimum = 1.
            for x0,z in ((t,y),((t[:-1]+t[1:])/2,middle)):
                physical,_ = obj.chart(x0,par[0])
                for first in range(0,len(x0),32):
                    sl = slice(first,first+32)
                    minimum = min(minimum,float(np.min(f.frame(physical[sl],obj.q*z[:,sl])['margin'].real)))
            row.update(original_domain_passed=True,original_collocation_rms=float(rms.max()),
                collocation_residual_max=float(abs(col).max()),sampled_min_frenet_margin=minimum)
        except FloatingPointError as error:
            row.update(original_domain_passed=False,original_domain_error=str(error))
        rows[name] = row
        print(json.dumps(dict(variant=name,**row)),flush=True)
    if oldf.exact_lift_core is not oldcore or f.exact_lift_core is not newcore:
        raise ValueError('An original immutable core reference was replaced')
    result = dict(scope=__doc__,command=sys.argv,run=str(run),input_checkpoint=str(restart),
        input_sha256=sha(restart),input_chunks=[dict(path=str(restart.parent/f),sha256=sha(restart.parent/f))
            for f in sorted(z.name for z in restart.parent.glob(restart.stem.split('.')[0]+'_coeff_*.npy.gz'))],
        affine_tail_anchor=dict(path=str(tail_path),sha256=sha(tail_path),
            role='The accepted actual DN/Jacobian used by the original failed inner problem; no new tail calls'),
        original_gauge_q=oldobj.q,original_actual_q=oldobj.support_amplitude,new_gauge_q=obj.q,
        new_actual_q=obj.support_amplitude,physical_parameters=par.tolist(),
        source_sha256={**env.sources,str(Path(__file__).resolve()):sha(__file__)},
        old_settings=old['core_round_settings'],new_settings=settings,nodes=len(t),
        original_seed_tail_height_difference=float(abs(obj.bridge.sigma*obj.q*original[obj.iz:,-1]-H0).max()),
        finite_angular_chart_difference=chart_error,
        complete_reference_projection_error_before_repair=projection_error,
        projection_versus_finite_only_coeff_max=float(abs(projected-finite_only).max()),
        projection_versus_finite_only_C2_seed_max=float(abs(
            variants['complete_reference_shared_C2_window']-variants['finite_only_shared_C2_window']).max()),
        full_map_scope='geo includes the unprojected integral H exactly once. The dynamic mean height '
            'is not injected into a coefficient basis that has no mean-Z slot; it remains an original '
            'Frenet integration audit. The finite comparison of the complete reference concerns '
            'the represented position plus exact core lift.',
        inlet_jet_scope='Analytic same-chart initializer formula at s=0, including recorded old '
            'quintic coefficient derivatives and the stated repair derivatives. No radial finite differences.',
        variants=rows,
        interpretation='These are finite initial-guess diagnostics for the same declared new endpoint '
            'equations. They are not solved states, continuous domain certificates, or proof that '
            'initialization alone caused the failed solve. No core source or acceptance gate changed.')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
