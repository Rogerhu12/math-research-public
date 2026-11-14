"""Fixed-metric warm restart on the saved adaptive radial mesh.

This only constructs an initial guess. Mode padding and gauge rescaling
preserve the old represented nonmean Fourier profile before the explicit
inlet correction; the mean height is recomputed by the solver.
The nonlinear BVP and actual-DN acceptance tests remain unchanged.
"""
from pathlib import Path
import hashlib
import math
import numpy as np
from scipy.interpolate import PPoly


def restart(obj, checkpoint, chart, merge_tolerance=2e-13):
    from curve_stable_prefix_bvp import load_checkpoint
    rec = load_checkpoint(checkpoint)
    if not obj.fixed:
        raise ValueError('Saved-mesh restart requires a fixed physical metric')
    checks = [('angular_chart', rec.get('angular_chart') == 'frozen-spline-adaptive-v1'),
              ('chart', rec['chart'] == chart),
              ('frozen_profile', rec['frozen_profile'] == obj.cfg),
              ('physical_tail_parameters', rec['physical_tail_parameters'] == obj.port['parameters']),
              ('physical_tail_cut', rec['physical_tail_cut'] == obj.port['cut']),
              ('warp_reference_q', rec['warp_reference_q'] == obj.warp_q)]
    for name, passed in checks:
        if not passed:
            raise ValueError('Changed fixed-metric restart input: '+name)
    oldM = rec['config']['modes']
    if obj.M < oldM:
        raise ValueError('Saved-mesh mode padding cannot reduce Fourier order')
    q0 = rec['gauge_amplitude']
    p = np.zeros(obj.M)
    p[0] = math.log(rec['actual_primary_amplitude']/obj.seed_support_amplitude)
    for j in range(1, min(oldM, obj.M)):
        p[j] = rec['parameters'][j]*rec['central_correction_scales'][j-1]/obj.pscale[j-1]
    f = obj.flow(p[0])
    if abs(f.end-rec['meridian_length']) > 3e-13:
        raise ValueError('Physical meridian endpoint changed')
    oldmesh = np.asarray(rec['mesh'], float)
    xold = obj.inverse_chart(oldmesh, p[0])
    anchors = []
    for x in np.sort(np.r_[0., obj.chart_breaks, 1.]):
        if not 0 <= x <= 1:
            continue
        if not anchors or x-anchors[-1] > merge_tolerance:
            anchors.append(float(x))
    extra = []
    for x in np.sort(xold):
        if x < -merge_tolerance or x > 1+merge_tolerance:
            raise ValueError('Saved mesh leaves the numerical meridian domain')
        if any(abs(x-b) <= merge_tolerance for b in anchors):
            continue
        if extra and x-extra[-1] <= merge_tolerance:
            continue
        extra.append(float(x))
    x = np.sort(np.r_[anchors, extra])
    if float(np.min(np.diff(x))) <= merge_tolerance:
        raise ValueError('Near-coincident saved restart nodes')
    s, _ = obj.chart(x, p[0])
    pp = PPoly.construct_fast(np.asarray(rec['pp_coefficients']), oldmesh,
                             extrapolate=True, axis=1)
    old = pp(s)
    y = np.zeros((obj.n, len(x)))
    ratio = q0/obj.q
    y[0] = ratio*old[0]
    y[1:oldM+1] = ratio*old[1:oldM+1]
    y[obj.M+1:obj.M+oldM+1] = ratio*old[oldM+1:2*oldM+1]
    y[2*obj.M+1:2*obj.M+oldM+1] = ratio*old[2*oldM+1:3*oldM+1]
    correction = obj.initial(p)-y[:, 0]
    cutoff = (f.Tu if f.direction == 'outward' else f.Td)/2
    if not cutoff > 0:
        raise ValueError('Invalid inlet correction interval')
    y += correction[:, None]*np.maximum(0, 1-s/cutoff)[None, :]**3
    info = dict(method='saved-adaptive-mesh-and-exact-signed-mode-padding',
                source=str(checkpoint), source_sha256=hashlib.sha256(Path(checkpoint).read_bytes()).hexdigest(),
                helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                fixed_inputs_checked=[name for name, passed in checks],
                old_modes=oldM, new_modes=obj.M, old_nodes=len(oldmesh), new_nodes=len(x),
                numerical_merge_tolerance=merge_tolerance, minimum_numerical_span=float(np.diff(x).min()),
                physical_gauge_ratio=ratio,
                inlet_correction_coefficient_l1=float(np.abs(correction).sum()),
                inlet_correction_physical_l1=float(abs(obj.q)*np.abs(correction).sum()),
                scope=__doc__)
    return x, y, p, info
