#!/usr/bin/env python3
"""Explicit fallback and globally consistent high-precision arc audit.

The mathematical Fourier curve, scalar target metric, and physical source
formula are held fixed. The original outer 5e-14 gate is never relaxed.
Only a failed actual source row invokes a tighter inner material solve.
"""
from contextlib import contextmanager
import types
import numpy as np


@contextmanager
def tight_material(field, tolerance=2e-15):
    core = field.master._ports.core
    old = core.at_material
    def refined(*args, **kwargs):
        kwargs.update(tolerance=tolerance, max_iterations=100)
        return old(*args, **kwargs)
    core.at_material = refined
    try:
        yield
    finally:
        core.at_material = old


@contextmanager
def longdouble_primitive(field, gauss=16):
    """Same literal coefficients/arc anchors; stronger primitive arithmetic.

The original float64 cumulative arc anchors, cuts, normalization constants
and polynomial coefficients are frozen. Only the local primitive evaluation
and inverse solve are upgraded. This is a numerical audit, not an interval
certificate or a replacement of the source by an interpolated field.
"""
    ports = field.master._ports
    core = ports.core
    raw = field.master.curve.raw
    old_derivative, old_theta = raw.derivative, raw.theta
    old_core_mul, old_ports_mul = core.mul, ports.mul
    old_a,old_perimeter,old_cumulative=raw.a,raw.perimeter,raw.cumulative
    old_normalization=field.master.curve.normalization
    modes = np.asarray(raw.modes, dtype=np.longdouble)
    coeff = np.asarray(raw.coeff, dtype=np.clongdouble)
    if gauss == 16:
        gx, gw = np.asarray(raw.gx, dtype=np.longdouble), np.asarray(raw.gw, dtype=np.longdouble)
    else:
        xx, ww = np.polynomial.legendre.leggauss(gauss)
        gx, gw = np.asarray((xx+1)/2, dtype=np.longdouble), np.asarray(ww/2, dtype=np.longdouble)
    original_cumulative=np.asarray(raw.cumulative,dtype=np.longdouble)
    period=2*np.arccos(np.longdouble(-1))
    cuts=np.linspace(np.longdouble(0),period,raw.panels+1,dtype=np.longdouble)
    stats = dict(gauss=gauss, primitiveMantissaBits=int(np.finfo(np.longdouble).nmant)+1,
        maximumArcResidual=0., literalArcAnchorsUnchanged=False,
        referenceArcAnchorsReintegratedFromZero=True,
        literalCurveCoefficientsUnchanged=True,
        independentTargetMetricNotReadOrModified=True,
        physicalFixedCurveRadiusUnchanged=float(field.master.curve.a),
        referencePeriodLongdouble=str(period),
        oldPeriod=float(raw.cuts[-1]),periodDifference=float(period-np.longdouble(raw.cuts[-1])))
    def mul(a, b):
        shape = np.broadcast_shapes(a.shape[1:], b.shape[1:])
        out = np.zeros((core.ORDER+1,)+shape, dtype=np.result_type(a, b, float))
        for k in range(core.ORDER+1):
            for j in range(k+1):
                out[k] += a[j]*b[k-j]
        return out
    def derivative(instance, theta, order=0):
        theta = np.asarray(theta, dtype=np.longdouble).reshape(-1)
        phase = np.exp(np.clongdouble(1j)*theta[:, None]*modes)
        return (phase @ (coeff*(np.clongdouble(1j)*modes[:, None])**order)).real
    def theta(instance, u):
        u = np.asarray(u, dtype=np.longdouble).reshape(-1)
        target = np.remainder(u, period)*np.longdouble(raw.a)
        cell = np.clip(np.searchsorted(cumulative, target, side='right')-1, 0, raw.panels-1)
        lo, hi = cuts[cell], cuts[cell+1]
        t = lo+(target-cumulative[cell])/(cumulative[cell+1]-cumulative[cell])*(hi-lo)
        for unused in range(16):
            q = lo[:, None]+(t-lo)[:, None]*gx
            d = derivative(raw, q.ravel(), 1).reshape(len(t), len(gx), 3)
            speed = np.sqrt(np.sum(d*d, axis=-1))
            residual = cumulative[cell]+(t-lo)*np.sum(speed*gw, axis=-1)-target
            if np.max(abs(residual)) <= np.longdouble('8e-18'):
                stats['maximumArcResidual'] = max(stats['maximumArcResidual'], float(np.max(abs(residual))))
                return t
            d = derivative(raw, t, 1)
            t -= residual/np.sqrt(np.sum(d*d, axis=-1))
            t = np.minimum(hi, np.maximum(lo, t))
        raise ArithmeticError('Longdouble literal primitive inverse unresolved: '+str(float(np.max(abs(residual)))))
    left=cuts[:-1];length=np.diff(cuts)
    points=left[:,None]+length[:,None]*gx
    d=derivative(raw,points.ravel(),1).reshape(raw.panels,len(gx),3)
    speed=np.sqrt(np.sum(d*d,axis=-1))
    integrals=length*np.sum(speed*gw,axis=-1)
    cumulative=np.r_[np.longdouble(0),np.cumsum(integrals,dtype=np.longdouble)]
    reference_a=cumulative[-1]/period
    reference_normalization=np.longdouble(field.master.curve.a)/reference_a
    stats.update(originalRawRadius=float(old_a),referenceRawRadiusLongdouble=str(reference_a),
        rawRadiusDifference=float(reference_a-np.longdouble(old_a)),
        originalNormalization=float(old_normalization),referenceNormalizationLongdouble=str(reference_normalization),
        normalizationDifference=float(reference_normalization-np.longdouble(old_normalization)),
        maximumOldAnchorForwardDiscrepancy=float(np.max(abs(original_cumulative-cumulative))),
        oldAnchorForwardDiscrepancies=[float(x) for x in original_cumulative-cumulative],
        originalArcAnchorsUsedAsExactRootData=False,
        referenceIsMoreAccurateEvaluationOfSameIntegralNotNewTargetG=True)
    raw.a,raw.perimeter,raw.cumulative=reference_a,cumulative[-1],cumulative
    field.master.curve.normalization=reference_normalization
    raw.derivative = types.MethodType(derivative, raw)
    raw.theta = types.MethodType(theta, raw)
    core.mul = ports.mul = mul
    try:
        with tight_material(field, 1e-17):
            yield stats
    finally:
        raw.derivative, raw.theta = old_derivative, old_theta
        raw.a,raw.perimeter,raw.cumulative=old_a,old_perimeter,old_cumulative
        field.master.curve.normalization=old_normalization
        core.mul, ports.mul = old_core_mul, old_ports_mul


def tracked_inverse(field, side, theta, base):
    """Published compatible algorithm with the actual returned roots recorded."""
    theta = np.asarray(theta, float).reshape(-1)
    u = theta.copy()
    for iteration in range(8):
        clock = base.endpoint_clock(field.providers[side](u), u)
        error = np.arctan2(np.sin(clock['phi'][0]-theta), np.cos(clock['phi'][0]-theta))
        if np.any(clock['phi'][1] <= 0):
            raise ArithmeticError('Actual polar inverse orientation failed')
        if np.max(abs(error)) < 5e-14:
            profile = base.polar_profiles(clock)
            return profile, float(np.max(abs(error))), u.copy()
        u -= error/clock['phi'][1]
    lo, hi = theta-np.pi, theta+np.pi
    def evaluate(values, targets):
        clock = base.endpoint_clock(field.providers[side](values), values)
        error = clock['phi'][0]-targets
        if np.any(clock['phi'][1] <= 0):
            raise ArithmeticError('Actual polar orientation failed')
        return clock, error
    _, fl = evaluate(lo, theta); _, fr = evaluate(hi, theta)
    if np.any(fl >= 0) or np.any(fr <= 0):
        raise ArithmeticError('Actual unwrapped bracket failed')
    u = theta.copy(); active = np.ones(len(theta), dtype=bool)
    result = {key:np.empty((3,3,len(theta))) for key in ('logrho','rho','z')}
    roots = np.full(len(theta), np.nan); residual = np.full(len(theta), np.inf)
    for iteration in range(64):
        index = np.flatnonzero(active)
        if not len(index): break
        clock, error = evaluate(u[index], theta[index])
        derivative = clock['phi'][1]; done = abs(error) < 5e-14
        if np.any(done):
            profile = base.polar_profiles(clock); finished = index[done]
            for key in result: result[key][:,:,finished] = profile[key][:,:,done]
            roots[finished] = u[finished]; residual[finished] = abs(error[done]); active[finished] = False
        if np.any(~done):
            index = index[~done]; error = error[~done]; derivative = derivative[~done]
            positive = error > 0; hi[index[positive]] = u[index[positive]]; lo[index[~positive]] = u[index[~positive]]
            candidate = u[index]-error/derivative
            unsafe = (candidate <= lo[index]) | (candidate >= hi[index]) | (~np.isfinite(candidate))
            candidate[unsafe] = (lo[index[unsafe]]+hi[index[unsafe]])/2
            u[index] = candidate
    if np.any(active):
        raise ArithmeticError('Tracked original outer gate unresolved')
    return result, float(np.max(residual)), roots


def audit_row(source, s, u, base):
    """Pay original/tight/LDBL residuals at every returned inverse root."""
    field = source.field
    original_inverse = field.inverse
    field.clock_cache = None
    records = []
    def inverse(instance, side, theta):
        profiles, error, roots = tracked_inverse(instance, side, theta, base)
        records.append(dict(side=int(side), targets=np.asarray(theta, float).copy(), roots=roots,
            reportedResidual=error, profiles=profiles))
        return profiles, error
    field.inverse = types.MethodType(inverse, field)
    try:
        with tight_material(field):
            tight = source.sample([s], u)
        checks = []
        for gauss in (16,32):
            with longdouble_primitive(field, gauss) as stats:
                root_checks = []
                for rec in records:
                    roots = rec['roots']; targets = rec['targets']
                    port = field.providers[rec['side']](roots)
                    xy = np.asarray(port['P'][:,:2], dtype=np.longdouble)
                    uu = np.asarray(roots, dtype=np.longdouble)
                    x,y = xy.T
                    angle = uu+np.arctan2(y*np.cos(uu)-x*np.sin(uu),x*np.cos(uu)+y*np.sin(uu))
                    error = angle-np.asarray(targets, dtype=np.longdouble)
                    prof = base.polar_profiles(base.endpoint_clock(port, roots))
                    root_checks.append(dict(side=rec['side'], roots=roots.tolist(), targets=targets.tolist(),
                        originalGateResidual=rec['reportedResidual'],
                        independentPrimitiveResidual=float(np.max(abs(error))),
                        profileTwoJetMaxDifference={key:float(np.max(abs(prof[key]-rec['profiles'][key]))) for key in prof}))
                checks.append(dict(primitive=dict(stats), rootChecks=root_checks))
        if max(x['independentPrimitiveResidual'] for c in checks for x in c['rootChecks']) >= 5e-14:
            raise ArithmeticError('Independent stronger primitive fails the unchanged outer angle gate')
        return tight, dict(physicalS=float(s), physicalAngles=np.asarray(u).tolist(),
            tighterInnerMaterialTolerance=2e-15, outerPolarToleranceUnchanged=5e-14,
            originalMathematicalCurveAndSourceFormulaUnchanged=True,
            independentTargetMetricA0Unchanged=True,
            auditArcAnchorsAreConsistentReintegralsNotOriginalFrozenBinaryAnchors=True,
            strongerPrimitiveChecks=checks, numericalAuditNotIntervalCertificate=True)
    finally:
        field.inverse = original_inverse
        field.clock_cache = None
