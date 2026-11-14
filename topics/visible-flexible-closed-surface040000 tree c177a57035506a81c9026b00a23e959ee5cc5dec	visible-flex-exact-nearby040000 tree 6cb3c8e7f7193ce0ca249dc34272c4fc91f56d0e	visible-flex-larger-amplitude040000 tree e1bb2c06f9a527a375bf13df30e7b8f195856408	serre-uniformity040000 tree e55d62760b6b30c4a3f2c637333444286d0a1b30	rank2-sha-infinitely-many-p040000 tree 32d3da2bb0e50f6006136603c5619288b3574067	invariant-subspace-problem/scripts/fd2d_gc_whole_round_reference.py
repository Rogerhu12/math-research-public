"""Fixed whole round reference and unprojected three-field increments.

The mathematical reference is R136 for the immutable base delta=0 metric.
Radius evaluation reuses the frozen Candidate reader.  The final brake is
evaluated from its distance-to-cut phase, with the exact flat endpoint
handled explicitly.  All returned numbers are binary64 evaluations, not
interval enclosures.  No nonlinear problem or solver is constructed here.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fd2d_frozen_ellipse_candidate import Candidate, phase


REFERENCE_CANDIDATE_SHA = '7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1'
REFERENCE_READER_SHA = '393848295e1d8e321c057286d722f47a6c51665aa1a35f4b3bbed3a63ddeac30'
ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CANDIDATE = ROOT/'notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _phase_second(piece, t):
    """Physical phi_ss on one declared piece, including one-sided ends."""
    kind, length = piece['kind'], piece['L']
    delta = piece['p1']-piece['p0']
    if kind == 'phase_bridge':
        q0, q1 = length*piece['ps0'], length*piece['ps1']
        c2, c3 = 3*delta-2*q0-q1, -2*delta+q0+q1
        return (2*c2+6*c3*t)/length**2
    if kind == 'turn':
        ramp_t = np.clip(np.minimum(t, 1-t)/.08, 0., 1.)
        sign = np.where(t < .08, 1., np.where(t > .92, -1., 0.))
        return delta*sign*(6*ramp_t-6*ramp_t*ramp_t)/(.92*.08*length**2)
    if kind == 'brake':
        return np.full_like(t, 2*delta/length**2)
    return np.zeros_like(t)


class FrozenRoundPrefixReference:
    """S0(s) with no target parameters, in component order (n,m,l).

    jet(s, side='right') returns arrays with the shape of s (a scalar is
    treated as a one-point array), followed by a length-three component
    axis for values/ds/dxi/dxi2/ds_dxi.  At an interior piece boundary, side
    selects the one-sided l_s.  At the final cut only the prefix left jet
    is supplied.  The flat annulus has the same zero VALUES there, but its
    l_s is zero; continuity of this II derivative is not asserted.
    """
    def __init__(self, candidate=DEFAULT_CANDIDATE):
        self.source = Path(candidate)
        reader = Path(__import__('fd2d_frozen_ellipse_candidate').__file__)
        if digest(self.source) != REFERENCE_CANDIDATE_SHA:
            raise ValueError('This fixed reference binds the closed 7c3 candidate')
        if digest(reader) != REFERENCE_READER_SHA:
            raise ValueError('The frozen radius reader source changed')
        self.base = Candidate(json.loads(self.source.read_text()))
        self.a0, self.end = self.base.a0, self.base.end
        self.breaks = self.base.breaks.copy()
        self.cut_radius = float(self.base.bundle['cut']['r'])
        last = self.base.segments[-1]
        if (last['kind'] != 'phase_bridge'
                or last.get('exact_endpoint_phase') != '-pi/2'
                or last['ps0'] != 0 or last['ps1'] != 0
                or self.base.bundle['cut']['a_prime'] != -1
                or self.base.bundle['cut']['a_second'] != 0):
            raise ValueError('The accurate zero-slope flat cut is required')

    def definition(self):
        return dict(
            schema='fd2d-fixed-whole-round-prefix-reference-v1',
            candidate_sha256=REFERENCE_CANDIDATE_SHA,
            radius_reader_sha256=REFERENCE_READER_SHA,
            source_sha256=digest(__file__), component_order=['n', 'm', 'l'],
            exact_definition='R136 shared-jet/rational-data profile with accurate pi endpoint; n0=cos(phi)/a,m0=0,l0=-phi_s',
            physical_metric='fixed base delta=0; reference has no target-parameter input',
            radius_numeric_evaluation='frozen Candidate quadrature, with the defining cut radius returned at s=end',
            terminal_phase_evaluation='epsilon=(pi/2+p0)*(3*(r/L)^2-2*(r/L)^3); b=sin(epsilon), l=epsilon_r',
            physical_end_binary64=self.end,
            derivative_convention='interior joins use requested side; final cut ds is the prefix LEFT jet only',
            angular_jets='all zero as complete functions, in every fixed angular atlas',
            target_parameter_jets='all zero; target delta forcing is kept separately',
            interval_certificate=False, no_surface_regularities_beyond_R136_C2=True)

    def jet(self, s, *, side='right'):
        if side not in ('left', 'right'):
            raise ValueError('Choose an explicit left or right piece trace')
        s = np.atleast_1d(np.asarray(s, dtype=float))
        if not np.all(np.isfinite(s)) or np.any(s < 0) or np.any(s > self.end):
            raise ValueError('Outside the closed physical prefix interval')
        ids = np.clip(np.searchsorted(self.breaks, s, side=side)-1,
                      0, len(self.base.segments)-1)
        a, ap, app, phi, ps, pss, b = [np.empty_like(s) for _ in range(7)]
        for j in np.unique(ids):
            mask = ids == j
            piece = self.base.segments[int(j)]
            points = s[mask]
            t = np.clip((points-piece['s0'])/piece['L'], 0., 1.)
            t = np.where(points == piece['s0'], 0., t)
            t = np.where(points == piece['s1'], 1., t)
            aa, vv, acc = self.base._jet(piece, t)
            if piece['kind'] == 'hermite':
                bb = np.sqrt((1-vv)*(1+vv))
                if np.any(bb <= 0):
                    raise FloatingPointError('The feedback reference lost its proved positive b')
                cc = np.asarray(piece['coefficients'], dtype=float)
                jerk = np.polynomial.polynomial.polyval(t, np.polynomial.polynomial.polyder(cc, 3))/piece['L']**3
                pp, pp_s = np.arcsin(vv), acc/bb
                pp_ss = jerk/bb+vv*acc*acc/bb**3
            elif piece.get('exact_endpoint_phase') == '-pi/2':
                # Use the exact limiting formula, not sqrt(1-a_s^2) or
                # cos(-pi/2 + tiny epsilon) at the flat end.
                length = piece['L']
                r = np.clip(piece['s1']-points, 0., length)
                r = np.where(points == piece['s0'], length, r)
                tau = r/length
                D = math.pi/2+piece['p0']
                eps = D*tau*tau*(3-2*tau)
                eps_r = 6*D*tau*(1-tau)/length
                eps_rr = 6*D*(1-2*tau)/length**2
                bb, vv = np.sin(eps), -np.cos(eps)
                pp, pp_s, pp_ss = -math.pi/2+eps, -eps_r, eps_rr
                acc = -bb*eps_r
                at_cut = points == self.end
                aa = np.where(at_cut, self.cut_radius, aa)
                bb = np.where(at_cut, 0., bb)
                vv = np.where(at_cut, -1., vv)
                acc = np.where(at_cut, 0., acc)
                pp_s = np.where(at_cut, 0., pp_s)
            else:
                pp, pp_s = phase(piece, t)
                pp_ss = _phase_second(piece, t)
                at0, at1 = t == 0., t == 1.
                pp = np.where(at0, piece['p0'], np.where(at1, piece['p1'], pp))
                if piece['kind'] == 'phase_bridge':
                    pp_s = np.where(at0, piece['ps0'], np.where(at1, piece['ps1'], pp_s))
                elif piece['kind'] in ('turn', 'coast', 'coast_to'):
                    pp_s = np.where(at0 | at1, 0., pp_s)
                bb, vv = np.cos(pp), np.sin(pp)
                acc = bb*pp_s
            for target, value in zip((a, ap, app, phi, ps, pss, b),
                                     (aa, vv, acc, pp, pp_s, pp_ss, bb)):
                target[mask] = value
        c, K = ap/a, -app/a
        n, l = b/a, -ps
        # This is the differentiated formula for b/a; retain this
        # independent evaluation so a local check can observe roundoff
        # against c*(l-n), not conceal it by assignment.
        n_s = -ap*ps/a-b*ap/(a*a)
        zero = np.zeros_like(s)
        values = np.stack((n, zero, l), axis=-1)
        ds = np.stack((n_s, zero, -pss), axis=-1)
        angular_zero = np.zeros_like(values)
        return dict(values=values, ds=ds, dxi=angular_zero.copy(),
                    dxi2=angular_zero.copy(), ds_dxi=angular_zero.copy(),
                    s=s.copy(), a=a, a_s=ap, a_ss=app, c0=c, K0=K,
                    phase=phi, phase_s=ps, phase_ss=pss, b=b,
                    piece_index=ids, cut_mask=s == self.end,
                    side=side, final_ds_is_prefix_left_trace=True)


def _increment_arrays(increment, increment_s, increment_xi):
    arrays = tuple(np.asarray(v, dtype=float) for v in
                   (increment, increment_s, increment_xi))
    if arrays[0].shape[-1:] != (3,) or any(v.shape != arrays[0].shape for v in arrays):
        raise ValueError('Complete increments and their jets must share shape (...,3)')
    return arrays


def round_increment_residual(reference, increment, increment_s, increment_xi,
                             *, a, c, K, U_s=0., U_xi=1.):
    """Full actual G/Cn/Cm, with known round GC contribution cancelled.

    All inputs are COMPLETE angular functions at common physical points.
    `increment` includes any tail lifting and nonlinear field composition;
    this helper performs neither projection nor a hidden representation
    change. The fixed reference broadcasts over leading angular axes.
    """
    Y, Ys, Yx = _increment_arrays(increment, increment_s, increment_xi)
    a, c, K, U_s, U_xi = map(np.asarray, (a, c, K, U_s, U_xi))
    if np.any(a <= 0) or np.any(U_xi <= 0):
        raise ValueError('The target metric and fixed chart must be positive')
    S0 = np.broadcast_to(reference['values'], Y.shape)
    n0, l0 = S0[..., 0], S0[..., 2]
    eta, mu, lam = (Y[..., j] for j in range(3))
    adv, inv = U_s/U_xi, 1/(a*U_xi)
    Cn = (Ys[..., 0]-adv*Yx[..., 0]-inv*Yx[..., 1]
          -c*(lam-eta)+(reference['c0']-c)*(l0-n0))
    Cm = Ys[..., 1]-adv*Yx[..., 1]-inv*Yx[..., 2]+2*c*mu
    G = l0*eta+n0*lam+eta*lam-mu*mu+reference['K0']-K
    return dict(fields=S0+Y, codazzi=np.stack((Cn, Cm), axis=-1),
                gauss=G, inv=inv, adv=adv)


def round_increment_jvp(reference, increment, increment_s, increment_xi,
                        direction, direction_s, direction_xi, *,
                        a, c, K, a_direction, c_direction, K_direction,
                        U_s=0., U_xi=1.):
    """Exact directional formula for the same complete-function operator.

    Target profile changes and the tail/current-radius/field-composition
    chain all belong in the supplied directions; none are inferred or
    silently discarded. Reference and fixed chart have zero variation.
    """
    Y, Ys, Yx = _increment_arrays(increment, increment_s, increment_xi)
    DY, DYs, DYx = _increment_arrays(direction, direction_s, direction_xi)
    if DY.shape != Y.shape:
        raise ValueError('Directions must match complete function values')
    out = round_increment_residual(reference, Y, Ys, Yx,
        a=a, c=c, K=K, U_s=U_s, U_xi=U_xi)
    a, c, da, dc, dK = map(np.asarray,
                           (a, c, a_direction, c_direction, K_direction))
    S0 = np.broadcast_to(reference['values'], Y.shape)
    n0, l0 = S0[..., 0], S0[..., 2]
    eta, mu, lam = (Y[..., j] for j in range(3))
    inv, adv = out['inv'], out['adv']
    dinv = -inv*da/a
    DCn = (DYs[..., 0]-adv*DYx[..., 0]-inv*DYx[..., 1]
           -c*(DY[..., 2]-DY[..., 0])-dinv*Yx[..., 1]
           -dc*(lam-eta+l0-n0))
    DCm = (DYs[..., 1]-adv*DYx[..., 1]-inv*DYx[..., 2]
           +2*c*DY[..., 1]-dinv*Yx[..., 2]+2*dc*mu)
    fields = out['fields']
    DG = (fields[..., 2]*DY[..., 0]+fields[..., 0]*DY[..., 2]
          -2*mu*DY[..., 1]-dK)
    return dict(fields=DY.copy(), codazzi=np.stack((DCn, DCm), axis=-1), gauss=DG)


def fixed_scale_gap(actual_gap, target_gap, *, scale):
    """One unchanged equation at zero target, normalized by fixed scale."""
    scale = float(scale)
    if not math.isfinite(scale) or scale <= 0:
        raise ValueError('Use one fixed strictly positive gap scale')
    return dict(value=(np.asarray(actual_gap)-np.asarray(target_gap))/scale,
                actual_gap_derivative=1/scale, target_gap_derivative=-1/scale,
                scale=scale)
