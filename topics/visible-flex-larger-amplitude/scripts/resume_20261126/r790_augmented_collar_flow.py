"""R790 transport of the R761 physical six-jets and two pairs of inverse labels.

This module evaluates original integral fields on a public scientific runner.
Every requested angle is an integration endpoint. The independent material
two-jets are recovered by the same implicit two-by-two systems as in R761.
"""
import json
import os
import time
from pathlib import Path

import numpy as np
from scipy.integrate import DOP853, solve_ivp

import r761_paired_tube_safe_nonflat_caps as tube
from r742_tilted_disk_two_jets import J, cap_s7


RESIDUAL = 3.e-10
REGULAR = 1.e-11
RTOL = 2.e-9
ATOL = 2.e-11


class PhysicalDOP853(DOP853):
    """Keep the original physical-component error estimate at its original norm."""
    def _estimate_error_norm(self, K, h, scale):
        width = len(scale) // 16
        physical = 12 * width
        original = super()._estimate_error_norm(K[:, :physical], h, scale[:physical])
        auxiliary = super()._estimate_error_norm(K[:, physical:], h, scale[physical:])
        return max(original, auxiliary)


def from_words(words):
    return J(*words[:6]), J(*words[6:12])


def map_data(fn, s, w, x, z):
    f, h = fn(J(s, s=1.), J(w, a=1.))
    error = max(float(np.max(abs(f.v - x.v))), float(np.max(abs(h.v - z.v))))
    det = f.s * h.a - f.a * h.s
    return f, h, error, float(np.min(abs(det)))


def inverse_jets(x, z, s, w, f, h):
    si, wi = tube.solve2(f, h, x.s, z.s)
    sj, wj = tube.solve2(f, h, x.a, z.a)

    def second(first, other, xx, zz):
        a, b = first
        c, d = other
        u = f.ss*a*c + f.sa*(a*d+b*c) + f.aa*b*d
        v = h.ss*a*c + h.sa*(a*d+b*c) + h.aa*b*d
        return tube.solve2(f, h, xx-u, zz-v)

    ss, ws = second((si, wi), (si, wi), x.ss, z.ss)
    sm, wm = second((si, wi), (sj, wj), x.sa, z.sa)
    sa, wa = second((sj, wj), (sj, wj), x.aa, z.aa)
    return J(s, si, sj, ss, sm, sa), J(w, wi, wj, ws, wm, wa)


def checked_chart(fn, x, z, s, w, seed_s, seed_w, statistics):
    try:
        f, h, err, det = map_data(fn, s, w, x, z)
        if not (np.isfinite(err) and np.isfinite(det)) or err > RESIDUAL or det < REGULAR:
            raise ArithmeticError("inverse-coordinate predictor needs the original Newton solve")
        ds, dw = tube.solve2(f, h, f.v-x.v, h.v-z.v)
        if max(np.max(abs(ds)), np.max(abs(dw))) >= 8.e-14:
            s, w = s-ds, w-dw
            f, h, err, det = map_data(fn, s, w, x, z)
            statistics["predictor_polishes"] += 1
            if not (np.isfinite(err) and np.isfinite(det)) or err > RESIDUAL or det < REGULAR:
                raise ArithmeticError("polished inverse needs the original Newton solve")
    except (ArithmeticError, FloatingPointError, ValueError):
        statistics["original_newton_fallbacks"] += 1
        a, b = tube.inverse(fn, x, z, seed_s, seed_w)
        s, w = a.v, b.v
        f, h, err, det = map_data(fn, s, w, x, z)
        if not (np.isfinite(err) and np.isfinite(det)) or err > RESIDUAL or det < REGULAR:
            raise ArithmeticError("original collar residual or nonregular coordinate map")
    statistics["maximum_returned_inverse_residual"] = max(
        statistics["maximum_returned_inverse_residual"], err)
    prev = statistics["minimum_returned_abs_determinant"]
    statistics["minimum_returned_abs_determinant"] = det if prev is None else min(det, prev)
    return *inverse_jets(x, z, s, w, f, h), f, h


def save_progress(file, values):
    tmp = file.with_suffix(".tmp")
    tmp.write_text(json.dumps(values, separators=(",", ":"), allow_nan=False), encoding="utf-8")
    os.replace(tmp, file)


def run_chunk(words, angles, nr, order, payload_path, progress_dir):
    """Return all originally requested angle states of the original active material rows."""
    tube.g.disk._public()
    begin = time.monotonic()
    stat = dict(rhs_calls=0, original_newton_fallbacks=0, predictor_polishes=0,
                original_flow_fallback_angles=0, original_flow_fallback_reason=None,
                maximum_returned_inverse_residual=0., minimum_returned_abs_determinant=None,
                angle_intervals=0, chunk_points=words.shape[1], active_points=0)
    progress_file = Path(progress_dir) / ("worker-%d.json" % os.getpid())
    stamp = [-100.]
    def report(t, done, force=False):
        now = time.monotonic()
        if force or now-stamp[0] >= 40:
            stamp[0] = now
            save_progress(progress_file, dict(stat, pid=os.getpid(),
                chunk=Path(payload_path).stem, working_angle=float(t),
                returned_angles=done, requested_angles=len(angles), elapsed_seconds=now-begin))

    xfull, zfull = from_words(words)
    dist, guess = tube.nearest(xfull, zfull, 0., nr, order)
    ids = np.flatnonzero(dist < tube.FLOW_BAND+.00050)
    def normal0(s, w):
        return tube.normal(s, w, 0., nr, order)
    if len(ids):
        first, depth = tube.inverse(normal0, tube.cut(xfull, ids), tube.cut(zfull, ids),
                                    guess[ids], guess[ids]*0.)
        live = depth.v < tube.FLOW_BAND
        ids = ids[live]
    stat["active_points"] = len(ids)
    report(0., 0, True)
    if not len(ids):
        return ids, stat

    s0, w0 = first.v[live], depth.v[live]
    full = tube.packed((tube.cut(xfull, ids), tube.cut(zfull, ids)))
    state = np.vstack((full, s0, w0, s0, w0)).ravel()
    count = full.shape[1]
    result = np.lib.format.open_memmap(payload_path, mode="w+", dtype="<f8",
        shape=(len(angles), 12, count))
    done = 0

    def evaluate(theta, current, with_labels=False):
        lanes = current.reshape(16, count)
        x, z = from_words(lanes)
        def mapped(s, w):
            return tube.planar(*normal0(s, w), theta, nr, order)
        def normal(s, w):
            return tube.normal(s, w, theta, nr, order)
        a, w, bf, bh = checked_chart(mapped, x, z, lanes[12], lanes[13], s0, w0, stat)
        c, d, cf, ch = checked_chart(normal, x, z, lanes[14], lanes[15], a.v, w.v, stat)
        if with_labels:
            return np.vstack((lanes[:12], a.v, w.v, c.v, d.v)).ravel()
        vb = tube.planar(*normal0(a, w), theta, nr, order, velocity=True)
        vc = tube.normal(c, d, theta, nr, order, velocity=True)
        weight = 1-cap_s7((w-tube.FLOW_BAND*.35)/(tube.FLOW_BAND*.65))
        vel = [v+weight*(r-v) for v, r in zip(vb, vc)]
        bs, bw = tube.solve2(bf, bh, vel[0].v-vb[0].v, vel[1].v-vb[1].v)
        cs, cw = tube.solve2(cf, ch, vel[0].v-vc[0].v, vel[1].v-vc[1].v)
        stat["rhs_calls"] += 1
        report(theta, done)
        return np.vstack((tube.packed(vel), bs, bw, cs, cw)).ravel()

    left = 0.
    for i, angle in enumerate(angles):
        right = float(angle)
        if stat["original_flow_fallback_reason"] is None:
            try:
                sol = solve_ivp(evaluate, (left, right), state, method=PhysicalDOP853,
                                rtol=RTOL, atol=ATOL, t_eval=[right])
                if not sol.success:
                    raise ArithmeticError(sol.message)
                state = evaluate(right, sol.y[:, -1], with_labels=True)
                result[i] = state.reshape(16, count)[:12]
                stat["angle_intervals"] += 1
            except (ArithmeticError, FloatingPointError) as exc:
                stat["original_flow_fallback_reason"] = type(exc).__name__+": "+str(exc)
        if stat["original_flow_fallback_reason"] is not None:
            # Re-enter the complete original R761 routine on its same full 32-row block.
            # It performs both Newton inversions, integration and its original checks.
            report(right, done, True)
            original = tube.move(xfull, zfull, right, nr, order)
            result[i] = tube.packed(original)[:, ids]
            stat["original_flow_fallback_angles"] += 1
        done += 1
        left = right
        report(right, done)
    result.flush()
    del result
    report(left, done, True)
    return ids, stat
