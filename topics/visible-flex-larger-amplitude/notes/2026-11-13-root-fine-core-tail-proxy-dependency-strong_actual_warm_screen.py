"""Unsolved full-field actual-control warm diagnostics, without a tail solve.

The prefix domain and original residual quadrature are evaluated in full.
For the boundary only, the caller supplies the accepted actual tail tangent;
the warm is never accepted as a new nonlinear-tail solution.  Geometry is an
explicit C2 physical-s cubic through every warm node, retaining all modes
and the full production height mean.  It is a design screen, not the final
physical quintic or a continuous curvature/reach certificate.
"""
from __future__ import annotations
import gc
import hashlib
import inspect
import textwrap
import types
from types import SimpleNamespace
import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import CubicSpline
from strong_tangent_warm_bvp import principal


def geometry(obj, t, y, p, angular=384):
    obj.select(p)
    f = obj.flow()
    s_nodes, _ = obj.chart(t, 0.)
    poly = CubicSpline(s_nodes, y, axis=1)
    sol = SimpleNamespace(x=s_nodes, y=y, p=p, sol=poly)
    s = np.unique(np.r_[np.linspace(0., f.end, 241), f.breaks, f.end])
    prefix = f._alternative_neck
    boost_end = max(seg['s1'] for seg in prefix.segments if seg['kind'] == 'boost')
    for seg in prefix.segments:
        if seg['kind'] == 'boost' or (seg['s0'] >= boost_end-1e-12 and seg['s0'] < prefix.loop_begin):
            s = np.unique(np.r_[s, np.linspace(seg['s0'], seg['s1'], 33)])
    original = textwrap.dedent(inspect.getsource(f.height_integral.__func__))
    if original.count('128') != 3:
        raise ValueError('The original mean-height independent batch sites changed')
    transformed = original.replace('128', '8')
    scope = {'np': np}
    exec(compile(transformed, '<bounded-warm-height-integral>', 'exec'), scope)
    H = types.MethodType(scope['height_integral'], f)(sol, s, angular, 6)
    B, B1, B2 = f.basis(angular)
    maximum, D, zmax = 0., 0., 0.
    margin, area_min, metric_max = 1., np.inf, 0.
    witness = None
    for first in range(0, len(s), 8):
        sl = slice(first, first+8)
        ss = s[sl]
        Y, Yp, Ypp = poly(ss), poly(ss, 1), poly(ss, 2)
        frame, Fsp, dW = f.velocity_s(ss, Y, Yp, B1, B2)
        g = frame['geo']
        Fs = g['s1']+obj.q*f.values(Yp, B)
        Fs[:, :, 2] += np.mean(frame['V'][:, :, 2], axis=1)[:, None]
        Fss = g['s2']+obj.q*f.values(Ypp, B)
        Fss[:, :, 2] += np.mean(dW[:, :, 2], axis=1)[:, None]
        kap, area = principal(Fs, frame['d'], Fss, Fsp, frame['dd'])
        points = g['pos']+obj.q*f.values(Y, B)
        points[:, :, 2] += H[sl, None]
        physical_s = Fs-g['v'][:, :, None]*frame['d']
        physical_theta = frame['d']/g['rho'][:, :, None]
        a = f.profile(ss)[0][:, None]
        metric = [np.sum(physical_s**2, axis=2)-1,
            np.sum(physical_s*physical_theta, axis=2)/a,
            np.sum(physical_theta**2, axis=2)/a**2-1]
        metric_max = max(metric_max, *[float(np.sum(abs(np.fft.fft(v, axis=1)/angular), axis=1).max()) for v in metric])
        ij = np.unravel_index(int(np.argmax(kap)), kap.shape)
        if kap[ij] > maximum:
            maximum = float(kap[ij])
            witness = dict(s=float(ss[ij[0]]), psi=float(ij[1]*2*np.pi/angular),
                material_theta=float(g['theta'][ij]), point=points[ij].tolist())
        D = max(D, 2*float(np.linalg.norm(points, axis=2).max()))
        zmax = max(zmax, float(abs(points[:, :, 2]).max()))
        margin = min(margin, float(frame['margin'].min()))
        area_min = min(area_min, float(area.min()))
    obj.initial(p)
    core = obj._core.summary()
    return dict(scope=__doc__, radial_samples=len(s), angular=angular, independent_batch=8,
        diameter_sample=D, kappa_sample=maximum, kappa_times_D_sample=maximum*D,
        reciprocal_kappa_D_sample=1/(maximum*D), height_max_sample=zmax,
        twice_height_max_sample=2*zmax, physical_metric_l1_sample=metric_max,
        frenet_margin_min_sample=margin, tangent_area_min_sample=area_min,
        curvature_witness=witness, actual_core=core,
        core_phase_gap_lower_over_D_sample=core['phase_pi_over_base_mode_support_gap_lower']/D,
        mean_height_integral=dict(angular=angular, quadrature_order=6,
            original_sha256=hashlib.sha256(original.encode()).hexdigest(),
            transformed_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
            original_integration_order_preserved=True))


def inspect_warm(obj, x, y, p, baseline_H, angular=384):
    h = np.diff(x)
    cr, ym, ff, fm = _bvp.collocation_fun(obj.fun, y, p, x, h)
    br = obj.bc(y[:, 0], y[:, -1], p)
    spline = _bvp.create_spline(y, ff, x, h)
    rms = _bvp.estimate_rms_residuals(obj.fun, spline, x, h, p, 1.5*cr/h, fm)
    result = dict(finite_domain_passed=True, full_collocation=dict(
        scaled_max=float(np.max(abs(cr)/(h[None, :]*(1+abs(fm))))),
        rms_max=float(np.max(rms)), boundary_max=float(np.max(abs(br))),
        inlet_max=float(np.max(abs(br[:obj.n]))),
        affine_actual_tail_boundary_max=float(np.max(abs(br[obj.n:obj.n+obj.M]))),
        prescribed_actual_core_constraint_max=float(np.max(abs(br[-3:]))),
        radial_sites_evaluated=len(x)+3*(len(x)-1),
        boundary_scope='Only the complete accepted actual nonlinear tail tangent; new-H true nonlinear tail is not evaluated.'),
        complete_warm_H=obj.tail_height(y[:, -1]).tolist(),
        complete_H_change_max=float(np.max(abs(obj.tail_height(y[:, -1])-baseline_H))))
    del cr, ym, ff, fm, br, spline, rms
    gc.collect()
    result['warm_physical_cubic_geometry'] = geometry(obj, x, y, p, angular=angular)
    return result
