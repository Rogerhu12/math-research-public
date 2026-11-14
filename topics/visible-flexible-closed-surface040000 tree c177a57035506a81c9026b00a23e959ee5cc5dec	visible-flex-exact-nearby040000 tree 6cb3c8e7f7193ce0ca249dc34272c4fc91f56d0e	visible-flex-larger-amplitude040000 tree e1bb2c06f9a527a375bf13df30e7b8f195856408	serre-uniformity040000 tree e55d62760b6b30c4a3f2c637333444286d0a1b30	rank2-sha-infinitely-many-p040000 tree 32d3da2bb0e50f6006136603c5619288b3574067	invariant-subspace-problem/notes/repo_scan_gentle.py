#!/usr/bin/env python3
"""Small reproducible m=2 cycle/bridge geometry screen (NOT a nonlinear solution).

Reuses the repository's gentle_inner_cycle_scan.screen and its physical
linear ODE.  A changed cut radius is an explicitly provisional linear port:
it does not supply a new compact tail, circular collar, closed surface, or
fixed-metric convergence.  Principal curvatures here belong to the actual
first-order parametric surface, not merely its rotational background.
"""
from __future__ import annotations
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"
import argparse
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.integrate import cumulative_trapezoid


def finite_value(value):
    if isinstance(value, dict):
        return {k: finite_value(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [finite_value(v) for v in value]
    if isinstance(value, np.generic):
        value = value.item()
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def save_report(path, report):
    """Keep raw numerical detail compressed and human scalar summary small."""
    path = Path(path)
    if path.suffix != '.gz':
        raise ValueError('Raw scan output must end in .json.gz')
    with gzip.open(path,'wt',compresslevel=9) as handle:
        json.dump(finite_value(report),handle,indent=2,allow_nan=False)
        handle.write('\n')
    candidates = []
    for index,row in enumerate(report['rows']):
        best = row.get('largest_low_curvature_amplitude')
        if best is None:
            continue
        keys = ['amplitude','PV_over_radius','PV_over_cylinder_diagonal',
                'first_order_radius_max','first_order_halfheight',
                'first_order_cylinder_diagonal','first_order_height_over_radius',
                'sampled_kappa_times_cylinder_diagonal','sampled_relative_root',
                'core_sampled_minimum_denominator','first_order_metric_component_max',
                'terminal_linear_height']
        candidates.append(dict(index=index+1,config=row['config'],h0=row['h0'],
            meridian_length_before_tail=row['meridian_length_before_tail'],
            **{k:best[k] for k in keys}))
    candidates.sort(key=lambda row:row['PV_over_radius'],reverse=True)
    summary = dict(scope='Sampled first-order annulus screen ONLY; no nonlinear solution or closed surface.',
        raw=path.name,stage=report['stage'],configurations=len(report['rows']),
        construction_errors=sum('error' in row for row in report['rows']),
        with_kappaD_under33=len(candidates),elapsed_seconds=report.get('elapsed_seconds'),
        top_low_curvature_candidates=candidates[:6])
    summary_path = path.with_name(path.name.removesuffix('.json.gz')+'_summary.json')
    summary_path.write_text(json.dumps(finite_value(summary),indent=2,allow_nan=False)+'\n')


def scaled_port(source, radius, slope=None, dimensionless_D=None):
    """Uniformly scale the linear port only, optionally change its slope.

    The attached tail's curvature would INCREASE when radius decreases;
    this routine does not claim the old tail is eligible.  Replacing slope
    or D is an explicitly synthetic boundary condition for annulus search.
    """
    old = source["cut"]
    scale = radius / old["radius"]
    w = old["backgroundSlope"] if slope is None else slope
    cut = dict(radius=radius, backgroundSlope=w,
               backgroundSecond=-7*w/radius,
               E=1+w*w, Ep=-14*w*w/radius)
    slopes = [x/scale for x in source["linearSlope"]]
    if dimensionless_D is not None:
        slopes[0] = dimensionless_D/radius
    return dict(cut=cut, linearSlope=slopes)


def port_from_core_halfwidth(port, cfg, halfwidth):
    """Compute a provisional Robin line from an explicitly chosen core h.

    This is a finite-annulus design variable, NOT known compact-tail data.
    It separates restrictions intrinsic to the cycle from restrictions
    imported by the old particular tail.  Higher-mode lines stay provisional.
    """
    from scipy.integrate import solve_ivp
    from f6curve_outward_bvp import OutwardPrefix
    from f6curve_inward_bvp import InwardPrefix
    from f6curve_bidirectional_bridge import DirectionalBridge
    if cfg.get('direction','outward') == 'inward':
        pref = InwardPrefix(1,.01,cfg['delta']/(1-cfg['delta']),cfg['vu'],cfg['vd'],
                           cfg['ramp'],cfg['cycles'],128,2,compute_stable=False)
    else:
        pref = OutwardPrefix(1,.01,cfg['delta'],cfg['vu'],cfg['vd'],
                            cfg['ramp'],cfg['cycles'],128,2,compute_stable=False)
    bridge = DirectionalBridge(port['cut'])
    end = pref.end+bridge.L
    def rhs(s,y):
        if s <= pref.end:
            a,v,_ = pref.profile(np.array([s]))
        else:
            a,v,_ = bridge.profile(np.array([s-pref.end]))
        a = float(a[0]); v = float(v[0]); b = math.sqrt(1-v*v)
        return np.array([-3*v*y[0]-4*b*y[1],3*v*v*y[0]/b+4*v*y[1]])/a
    sol = solve_ivp(rhs,[0,end],[-4*halfwidth,1.],method='DOP853',
                    rtol=3e-12,atol=3e-14,max_step=min(pref.period,bridge.L)/100)
    if not sol.success:
        raise ValueError(sol.message)
    f,g = sol.y[:,-1]
    if abs(g)<1e-14:
        raise ValueError('Selected Robin chart is singular at zero endpoint height')
    r = port['cut']['radius']; w = port['cut']['backgroundSlope']
    D = (4+3*f/(bridge.sigma*w*g))/r
    result = dict(cut=port['cut'].copy(),linearSlope=list(port['linearSlope']))
    result['linearSlope'][0] = float(D)
    return result,dict(requested_core_halfwidth=halfwidth,
                      derived_dimensionless_D=float(r*D),
                      forward_endpoint_gain=float(g),
                      scope='Synthetic fundamental Robin line; no compatible compact tail supplied.')


def linear_jets(obj, x):
    """Analytic first and second s derivatives of the physical linear mode."""
    a, v, acc = obj.profile(x)
    b = np.sqrt(1-v*v)
    m = obj.base_mode
    k = m*m-1
    P = np.zeros((len(x), 2, 2))
    P[:, 0, 0] = -k*v
    P[:, 0, 1] = -m*m*b
    P[:, 1, 0] = k*v*v/b
    P[:, 1, 1] = m*m*v
    A = P/a[:, None, None]
    Pv = np.zeros_like(P)
    Pv[:, 0, 0] = -k
    Pv[:, 0, 1] = m*m*v/b
    Pv[:, 1, 0] = k*(2*v/b+v**3/b**3)
    Pv[:, 1, 1] = m*m
    Ap = Pv*acc[:, None, None]/a[:, None, None]-A*(v/a)[:, None, None]
    fg = obj.linear[0].sol(x).T
    dfg = np.einsum("nij,nj->ni", A, fg)
    ddfg = np.einsum("nij,nj->ni", Ap, fg)+np.einsum("nij,nj->ni", A, dfg)
    ys = []
    for u in (fg, dfg, ddfg):
        y = np.zeros((obj.n, len(x)))
        y[1] = u[:, 0]
        y[obj.M+1] = -u[:, 0]/m
        y[obj.iz] = u[:, 1]
        ys.append(y)
    return (a, v, acc, b), ys


def prepare(obj, radial=49, angular=128):
    x = np.unique(np.concatenate([
        np.linspace(lo, hi, radial)
        for lo, hi in zip(obj.breaks[:-1], obj.breaks[1:])]))
    profile, ys = linear_jets(obj, x)
    Bs = obj.basis(angular)
    return x, profile, ys, Bs


def evaluate(obj, data, q):
    from construct_general_reflected_core import curve_geometry
    x, (a, v, acc, b), ys, (B, B1, B2) = data
    C = [obj.base(x, j)+q*ys[j] for j in range(3)]
    positions = obj.values(C[0], B)
    zbase = obj.h0+cumulative_trapezoid(b, x, initial=0.)
    positions[:, :, 2] += zbase[:, None]
    Fs = obj.values(C[1], B)
    Fs[:, :, 2] += b[:, None]
    Fss = obj.values(C[2], B)
    Fss[:, :, 2] += (-v*acc/b)[:, None]
    Ft = obj.values(C[0], B1)
    Ftt = obj.values(C[0], B2)
    Fst = obj.values(C[1], B1)
    E = np.sum(Fs*Fs, axis=2)
    F = np.sum(Fs*Ft, axis=2)
    G = np.sum(Ft*Ft, axis=2)
    detI = E*G-F*F
    normal = np.cross(Fs, Ft)
    normal /= np.linalg.norm(normal, axis=2)[:, :, None]
    II = [np.sum(V*normal, axis=2) for V in (Fss, Fst, Ftt)]
    L, M, N = II
    tr = (L*G-2*M*F+N*E)/detI
    detII = (L*N-M*M)/detI
    discriminant = np.maximum(0., tr*tr-4*detII)
    kap = .5*(np.abs(tr)+np.sqrt(discriminant))
    where = np.unravel_index(int(np.argmax(kap)), kap.shape)
    rho = np.linalg.norm(positions[:, :, :2], axis=2)
    radius = float(np.max(rho))
    halfheight = float(np.max(np.abs(positions[:, :, 2])))
    # The rectifying core is exact, but its joining to the first-order
    # prefix is generally only O(q^2).  Report its own regularity separately.
    oldq = obj.q
    obj.q = q
    try:
        par = obj.parameters(np.zeros(obj.M))
    finally:
        obj.q = oldq
    theta = 2*np.pi*np.arange(1024)/1024
    core = curve_geometry(theta, par['R'], par['radial'], par['height'])
    den = 1-obj.h0*np.abs(core['wt'])
    min_den = float(np.min(den))
    core_kappa = float(np.max(core['kappa']*(1+core['w']**2)/den)) if min_den > 0 else math.inf
    for sign in (-1, 1):
        port = core['gamma']+sign*obj.h0*core['D']
        radius = max(radius, float(np.max(np.linalg.norm(port[:, :2], axis=1))))
        halfheight = max(halfheight, float(np.max(np.abs(port[:, 2]))))
    cylinder_diagonal = 2*math.hypot(radius, halfheight)
    surface_kappa = float(np.max(kap))
    fr = obj.frame(x, C[0], B1, B2)
    relroot = fr['margin']/(1-v*v)[:, None]
    errors = np.stack((E-1, F/a[:, None], G/a[:, None]**2-1), axis=2)
    result = dict(
        amplitude=q, central_PV=2*q,
        first_order_radius_max=radius,
        first_order_halfheight=halfheight,
        first_order_height_over_radius=halfheight/radius,
        first_order_cylinder_diagonal=cylinder_diagonal,
        PV_over_radius=2*q/radius,
        PV_over_cylinder_diagonal=2*q/cylinder_diagonal,
        first_order_kappa=surface_kappa,
        first_order_kappa_location_s=float(x[where[0]]),
        first_order_kappa_location_theta=float(2*np.pi*where[1]/len(B[0])),
        core_sampled_minimum_denominator=min_den,
        core_sampled_kappa=core_kappa,
        sampled_kappa_times_cylinder_diagonal=max(surface_kappa, core_kappa)*cylinder_diagonal,
        sampled_kappa_times_twice_radius=max(surface_kappa, core_kappa)*2*radius,
        sampled_root=float(np.min(fr['margin'])),
        sampled_relative_root=float(np.min(relroot)),
        first_order_metric_component_max=float(np.max(np.abs(errors))),
        first_order_minimum_detI=float(np.min(detI)),
        terminal_linear_height=q*obj.linear[0].gain,
        terminal_linear_gain=obj.linear[0].gain,
        radial_samples=len(x), angular_samples=len(B[0]),
        complete_nonlinear_solution=False,
    )
    return result


def default_configs(stage):
    if stage == 'initial':
        # Deliberately small factorial, not the old 384-case scan.
        return [dict(delta=d, vu=u, vd=v, ramp=e, cycles=n,
                     cut_radius=r, cut_slope=.05)
                for d, u, v, e, n, r in [
                    (.8,.85,.98,.05,5,.98),
                    (.3,.5,.7,.3,1,.6), (.3,.6,.8,.3,1,.6),
                    (.4,.65,.85,.3,1,.6), (.4,.7,.9,.3,1,.6),
                    (.5,.75,.9,.3,1,.6), (.6,.8,.95,.3,1,.6),
                    (.4,.6,.8,.4,1,.7), (.5,.7,.9,.4,1,.7),
                    (.6,.8,.95,.4,1,.7), (.8,.85,.98,.3,1,.7),
                    (.3,.5,.7,.3,2,.6), (.4,.65,.85,.3,2,.6),
                    (.5,.75,.9,.3,2,.6), (.6,.8,.95,.3,2,.6),
                    (.4,.65,.85,.2,1,.5), (.5,.75,.9,.2,1,.5),
                    (.4,.65,.85,.3,1,.8), (.5,.75,.9,.3,1,.8),
                    (.4,.7,.85,.45,1,.6), (.6,.85,.95,.45,1,.6),
                    (.8,.92,.98,.4,1,.6), (.6,.9,.95,.4,1,.5),
                    (.4,.85,.9,.4,1,.5),
                ]]
    raise ValueError('Provide --configs for an adaptive follow-up')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--configs', type=Path)
    parser.add_argument('--stage', default='initial')
    parser.add_argument('--radial', type=int, default=33)
    parser.add_argument('--angular', type=int, default=128)
    args = parser.parse_args()
    scriptdir = args.source_root/'topics/large-amplitude-twist-flex/scripts'
    sys.path.insert(0, str(scriptdir))
    from f6curve_outward_bridge_linear import OutwardBridgeLinear, read_port
    from f6root_gentle_inner_cycle_scan import screen
    from repo_scan_inward_model import InwardCycleBridge
    srcpath = args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json'
    source = read_port(srcpath)
    configs = json.loads(args.configs.read_text()) if args.configs else default_configs(args.stage)
    names = ['f6root_gentle_inner_cycle_scan.py','f6curve_outward_bridge_linear.py',
             'f6curve_outward_bvp.py','f6curve_bidirectional_bridge.py',
             'f6curve_inward_bvp.py','curve_stable_prefix_bvp.py',
             'construct_general_reflected_core.py']
    hashes = {name: hashlib.sha256((scriptdir/name).read_bytes()).hexdigest() for name in names}
    hashes[str(srcpath.name)] = hashlib.sha256(srcpath.read_bytes()).hexdigest()
    hashes[Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    helper = Path(__file__).with_name('repo_scan_inward_model.py')
    hashes[helper.name] = hashlib.sha256(helper.read_bytes()).hexdigest()
    report = dict(scope=__doc__, source_root=str(args.source_root), source_hashes=hashes,
                  stage=args.stage, rows=[], limitations=[
                    'No exact nonlinear band, C2 seam, compact collar, or closed family is supplied.',
                    'All curvature, root, and diameter data are sampled, not interval enclosures.',
                    'Cylinder diagonal is an estimate for this candidate only, not a proved closed-surface D.',
                    'Changing a port changes the provisional geometry; no fixed-geometry convergence is claimed.',
                    'Current old compact tails have high curvature and are not made eligible by port rescaling.'
                  ])
    start = time.time()
    for i, cfg in enumerate(configs):
        row = dict(config=cfg)
        try:
            port = scaled_port(source, cfg['cut_radius'], cfg.get('cut_slope'), cfg.get('dimensionless_D'))
            if 'core_halfwidth' in cfg:
                port, row['synthetic_port_design'] = port_from_core_halfwidth(port,cfg,cfg['core_halfwidth'])
            row['port'] = port
            direction = cfg.get('direction','outward')
            if direction == 'outward':
                row['original_screen_at_q001'] = screen(
                    port, cfg['delta'], cfg['vu'], cfg['vd'], cfg['ramp'], cfg['cycles'],
                    .01, cfg['delta']+1-cfg['cut_radius'], base_mode=2,
                    tail_height=0, tail_length=0, cuff_radius=cfg['cut_radius'])
                cls = OutwardBridgeLinear
            elif direction == 'inward':
                row['screen_adaptation'] = 'Inward-first counterpart; same physical linear ODE, own explicit breakpoints.'
                cls = InwardCycleBridge
            else:
                raise ValueError('Unknown direction: '+direction)
            obj = cls(port, modes=1, amplitude=.01,
                delta=cfg['delta'], vu=cfg['vu'], vd=cfg['vd'], eps=cfg['ramp'],
                cycles=cfg['cycles'], angular=args.angular, base_mode=2)
            data = prepare(obj, args.radial, args.angular)
            row.update(h0=obj.h0, prefix_length=obj.prefix_end,
                       bridge_length=obj.bridge.L,
                       meridian_length_before_tail=2*(obj.h0+obj.end),
                       background_halfheight=float(obj.h0+np.trapezoid(data[1][3], data[0])),
                       terminal_linear_gain=obj.linear[0].gain)
            evaluations = []
            low = 0.
            high = None
            for q in cfg.get('amplitudes', [.01,.025,.05,.075,.1,.125,.15,.2,.25,.3]):
                try:
                    ev = evaluate(obj, data, q)
                    evaluations.append(ev)
                    if ev['sampled_relative_root'] < .15 or ev['core_sampled_minimum_denominator'] < .15:
                        high = q
                        break
                    low = q
                except Exception as exc:
                    high = q
                    row['first_amplitude_failure'] = dict(amplitude=q, error=repr(exc))
                    break
            if high is not None and high-low>.002:
                for j in range(8):
                    q = (low+high)/2
                    try:
                        ev = evaluate(obj, data, q)
                        evaluations.append(ev)
                        if ev['sampled_relative_root'] < .15 or ev['core_sampled_minimum_denominator'] < .15:
                            high = q
                        else:
                            low = q
                    except Exception:
                        high = q
            row['evaluations'] = evaluations
            good = [ev for ev in evaluations if ev['sampled_relative_root'] >= .15
                    and ev['core_sampled_minimum_denominator'] >= .15]
            if good:
                row['largest_sampled_admissible_amplitude'] = max(good,key=lambda ev:ev['amplitude'])
                gentle = [ev for ev in good if ev['sampled_kappa_times_cylinder_diagonal']<33.]
                row['largest_low_curvature_amplitude'] = max(gentle,key=lambda ev:ev['PV_over_radius']) if gentle else None
        except Exception as exc:
            row['error'] = repr(exc)
        report['rows'].append(finite_value(row))
        report['elapsed_seconds'] = time.time()-start
        save_report(args.out,report)
        best = row.get('largest_low_curvature_amplitude') or row.get('largest_sampled_admissible_amplitude',{})
        print(json.dumps(finite_value(dict(index=i+1,total=len(configs),config=cfg,
            q=best.get('amplitude'),PV_over_radius=best.get('PV_over_radius'),
            kappaD=best.get('sampled_kappa_times_cylinder_diagonal'),
            H_over_radius=best.get('first_order_height_over_radius'),
            end_height=best.get('terminal_linear_height'),error=row.get('error'),
            seconds=round(report['elapsed_seconds'],2)))),flush=True)


if __name__ == '__main__':
    main()
