#!/usr/bin/env python3
"""True affine parameter two-jets of the moving-turn principal field.

The coordinate tau is fixed and x=t(delta)*sin(tau). The exact mathematical
family is the explicitly symmetric affine R33 family, not a rounded graph.
The floating implementation below has no finite-difference derivative in its
field source. Finite FFT, trig, root-centre and quadrature errors remain unpaid.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import re
import time

import numpy as np
from numpy.polynomial.legendre import leggauss

from fourfold_mixed_jet_algebra import Jet
from fourfold_phase_symmetric_geometry import load_exact_object, SymmetricAffineGeometry


class AngularParameterJet(Jet):
    # First variable is ordinary cylindrical theta, second is the actual
    # affine parameter. The third theta order is needed before forming Ftt.
    nx = 3
    np = 2


def mapped(jet, function):
    out = jet.__class__()
    for i in range(jet.nx+1):
        for j in range(jet.np+1):
            out[i, j] = function(jet[i, j])
    return out


def floating_sincos(value):
    return np.sin(value), np.cos(value)


def tangent(beta, gamma):
    sb, cb = beta.sincos(floating_sincos)
    sg, cg = gamma.sincos(floating_sincos)
    T = (-cg*sb, cg*cb, sg)
    Tb = (-cg*cb, -cg*sb, beta.constant(0.))
    Tg = (sg*sb, -sg*cb, cg)
    return T, Tb, Tg


def dot(a, b):
    return sum((u*v for u, v in zip(a, b)), a[0].constant(0.))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


class ActualAffineSecondField:
    def __init__(self, geometry, root, root_quadrature=5):
        self.geometry, self.root = geometry, float(root)
        self.root_quadrature = int(root_quadrature)
        self._target_cache = {}
        C, _, _ = self.target_jets(self.root)
        cx, cp = C[1, 0], C[0, 1]
        self.root_p = float(-cp/cx)
        self.root_pp = float(-(2*C[0, 2]+2*C[1, 1]*self.root_p
                              +2*C[2, 0]*self.root_p**2)/cx)

    def target_jets(self, x):
        """Normalized x<=3,p<=2 jets of K; x<=2,p<=2 of C.

        These are actual mixed derivatives of the finite-DFT evaluation of
        the infinite primitive; the truncation/rounding cost is not certified.
        """
        key = float(x)
        if key in self._target_cache:
            return self._target_cache[key]
        g = self.geometry
        data = g.profile_jets([x], order=5)
        beta, gamma, radius, slope = Jet(), Jet(), Jet(), Jet()
        for i in range(6):
            for j, suffix in enumerate(("", "_parameter")):
                phase = data["phase"+suffix][i, 0]/math.factorial(i)
                beta[i, j], gamma[i, j] = phase[:, 0]@g.sine, phase[:, 1]@g.sine
                radius[i, j] = data["mean"+suffix][i, 0, 0]/math.factorial(i)
                if i < 5:
                    slope[i, j] = data["mean"+suffix][i+1, 0, 2]/math.factorial(i)
        T, _, _ = tangent(beta, gamma)
        primitive = Jet()
        for i in range(6):
            for j in range(3):
                samples = np.stack([np.broadcast_to(component[i, j], (g.nodes,))
                                    for component in T], axis=-1)
                primitive[i, j] = g.primitive_coefficients(samples)
        fx = (radius*primitive).derivative()
        for i in range(5):
            for j in range(3):
                fx[i, j] = np.array(fx[i, j], copy=True)
                fx[i, j][0, 2] += slope[i, j]
        # Parseval with both positive and negative complex Fourier modes.
        squared = fx*mapped(fx, np.conjugate)
        E = mapped(squared, lambda z: float(np.real(np.sum(z))))
        C = radius.derivative()*E.derivative()-2*radius.derivative().derivative()*E
        K = C/(2*radius*E*E)
        answer = (C, K, (float(radius[0, 0]), float(E[0, 0])))
        if len(self._target_cache) >= 32:
            self._target_cache.pop(next(iter(self._target_cache)))
        self._target_cache[key] = answer
        return answer

    def q_derivatives(self, tau):
        """Q,Qp,Qpp at fixed tau, deflated at both moving endpoints.

        Exact symmetry permits s=abs(sin(tau)). The near-root formula uses
        Kx along [ts,t], so no division of a vanishing parameter numerator
        by cos(tau)**2 occurs. Returned derivatives are unnormalized.
        """
        s = abs(float(np.sin(tau)))
        t, tp, tpp = self.root, self.root_p, self.root_pp
        if s < .999:
            _, K, _ = self.target_jets(t*s)
            k0 = K[0, 0]
            k1 = K[0, 1]+tp*s*K[1, 0]
            k2 = (2*K[0, 2]+2*tp*s*K[1, 1]
                  +2*(tp*s)**2*K[2, 0]+tpp*s*K[1, 0])
            return -np.array([k0, k1, k2])/(1-s*s)
        points, weights = leggauss(self.root_quadrature)
        I = np.zeros(3)
        for u, weight in zip((points+1)/2, weights/2):
            xi = 1-u*(1-s)
            _, K, _ = self.target_jets(t*xi)
            I += weight*np.array([
                K[1, 0],
                K[1, 1]+2*tp*xi*K[2, 0],
                2*K[1, 2]+4*tp*xi*K[2, 1]
                +6*(tp*xi)**2*K[3, 0]+2*tpp*xi*K[2, 0]])
        return np.array([t*I[0], tp*I[0]+t*I[1],
                         tpp*I[0]+2*tp*I[1]+t*I[2]])/(1+s)

    def _path_profiles(self, tau):
        s = float(np.sin(tau))
        data = self.geometry.profile_jets([self.root*s], order=3)
        xp, xpp = self.root_p*s, self.root_pp*s
        result = {}
        for name in ("phase", "mean"):
            value, first = data[name][:, 0], data[name+"_parameter"][:, 0]
            # Shape: original radial order (0,1), normalized p order (0,1,2).
            result[name] = np.stack([
                np.stack((value[r], first[r]+xp*value[r+1],
                          xp*first[r+1]+.5*xp*xp*value[r+2]+.5*xpp*value[r+1]))
                for r in (0, 1)])
        return result

    def _angular_tangent(self, path, theta):
        g = self.geometry
        theta = np.atleast_1d(theta)
        modes = 4*np.arange(1, g.modes+1)
        argument = theta[:, None]*modes
        sin, cos = np.sin(argument), np.cos(argument)
        waves = (sin, cos*modes, -sin*modes**2/2, -cos*modes**3/6)
        fields = []
        for r in (0, 1):
            parts = []
            for component in (0, 1):
                value = AngularParameterJet()
                for i in range(4):
                    for j in range(3):
                        value[i, j] = waves[i]@path["phase"][r, j, :, component]
                parts.append(value)
            fields.append(parts)
        T, Tb, Tg = tangent(*fields[0])
        Tx = tuple(tb*fields[1][0]+tg*fields[1][1] for tb, tg in zip(Tb, Tg))
        a, ax, slope = (AngularParameterJet() for _ in range(3))
        for j in range(3):
            a[0, j], ax[0, j], slope[0, j] = (path["mean"][0, j, 0],
                path["mean"][1, j, 0], path["mean"][1, j, 2])
        ft = tuple(a*v for v in T)
        B = tuple(ax*v+a*vx for v, vx in zip(T, Tx))
        Dt = (T[0].derivative()-T[1], T[1].derivative()+T[0], T[2].derivative())
        ftt = tuple(a*v for v in Dt)
        return ft, B, ftt, slope

    def principal_path_jets(self, tau, theta):
        """b=-m/n and w=G/n, normalized theta<=2 and path-p<=2."""
        g = self.geometry
        theta = np.atleast_1d(np.asarray(theta, dtype=float))
        path = self._path_profiles(tau)
        _, Bq, _, slope = self._angular_tangent(path, g.angles)
        coefficients = []
        for j in range(3):
            samples = np.stack([component[0, j] for component in Bq], axis=-1)
            values = g.primitive_coefficients(samples)
            values[0, 2] += slope[0, j]
            coefficients.append(values)
        wave = np.exp(1j*theta[:, None]*g.frequency)
        fx = tuple(AngularParameterJet() for _ in range(3))
        for i in range(4):
            factor = (1j*g.frequency)**i/math.factorial(i)
            for j in range(3):
                evaluated = np.real(np.einsum("nq,q,qc->nc", wave, factor, coefficients[j]))
                for c in range(3):
                    fx[c][i, j] = evaluated[:, c]
        ft, B, ftt, _ = self._angular_tangent(path, theta)
        C = cross(ft, fx)
        m, n, G = dot(C, B), dot(C, ftt), dot(C, C)
        if np.any(n[0, 0] >= 0) or np.any(G[0, 0] <= 0):
            raise ValueError("actual real chart failed")
        return -m/n, G/n

    def evaluate(self, tau, theta, sign):
        b, w = self.principal_path_jets(tau, theta)
        q = self.q_derivatives(tau)
        if q[0] <= 0:
            raise ValueError("root-deflated Q positivity failed")
        root, sqrtq = AngularParameterJet(), AngularParameterJet()
        root[0, 0], root[0, 1], root[0, 2] = self.root, self.root_p, self.root_pp/2
        qroot = np.sqrt(q[0])
        sqrtq[0, 0], sqrtq[0, 1], sqrtq[0, 2] = (qroot, q[1]/(2*qroot),
            q[2]/(4*qroot)-q[1]*q[1]/(8*qroot**3))
        cosine = float(np.cos(tau))
        f = cosine*root*b+sign*cosine*cosine*root*w*sqrtq
        return dict(f=f[0, 0], f_theta=f[1, 0], f_parameter=f[0, 1],
                    f_theta_theta=2*f[2, 0], f_theta_parameter=f[1, 1],
                    f_parameter_parameter=2*f[0, 2], Q=q)

    def rhs(self, tau, state, sign):
        """Rows Y, log J, Yp, Ypp, optionally (log J)p.

        Pass the final rows of branch one as the initial rows of branch two
        to obtain the complete return and its actual parameter two-jet.
        """
        y, logj, z, w = state[:4]
        f = self.evaluate(tau, y, sign)
        rows = [f["f"], f["f_theta"],
                f["f_theta"]*z+f["f_parameter"],
                f["f_theta"]*w+f["f_theta_theta"]*z*z
                +2*f["f_theta_parameter"]*z+f["f_parameter_parameter"]]
        if len(state) == 5:
            rows.append(f["f_theta_theta"]*z+f["f_theta_parameter"])
        elif len(state) != 4:
            raise ValueError("expected four or five state rows")
        return np.stack(rows)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object",type=Path,required=True)
    parser.add_argument("--root-certificate",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--parameter-step",type=float,default=1e-4)
    parser.add_argument("--root-quadrature",type=int,default=5)
    args = parser.parse_args()
    geometry, definition = load_exact_object(args.object)
    root = json.loads(args.root_certificate.read_text())
    if (not root["proved"] or root["delta_binary64_hex"] != definition["delta_hex"]
        or root["origin_inputs_sha256"] != definition["origin_inputs"]["sha256"]
        or root["frozen_direction_sha256"] != definition["direction"]["sha256"]):
        raise ValueError("root certificate is for another object")
    started = time.monotonic()
    evaluator = ActualAffineSecondField(geometry, root["root_center"], args.root_quadrature)
    knot_regularity = []
    for name in geometry.frozen:
        if not re.fullmatch(r"phase_knots|base_knots|shift_knots|mean\d+_knots|height\d+_slope_knots",name):
            continue
        values, counts = np.unique(geometry.frozen[name], return_counts=True)
        degree = 5 if name == "phase_knots" else int(geometry.frozen[name[:-6]+"_degree"])
        core = np.abs(values) <= .24
        multiplicity = int(np.max(counts[core])) if np.any(core) else 0
        reflected = np.unique(np.abs(values))
        collar = (reflected >= .238152859375)&(reflected <= .23864114062500003)
        if degree-multiplicity < 4 or np.any(collar):
            raise ValueError("this diagnostic's C4 core / analytic root collar input gate failed")
        knot_regularity.append(dict(field=name,degree=degree,
            maximum_core_multiplicity=multiplicity,knots_in_common_root_collar=int(np.sum(collar))))
    angles = np.array([.037, .259, .623, 1.13])
    taus = np.array([-np.pi/2, -1.53, -.71, 0., .71, 1.53, np.pi/2])
    fields = [evaluator.evaluate(t, angles, -1.) for t in taus]
    fixed_x_comparison = []
    for tau in (-.71, 0., .71):
        s, cosine = np.sin(tau), np.cos(tau)
        x = evaluator.root*s
        radial = geometry.radial_target_metric([x], with_variations=True)
        raw = geometry.principal_quantities(np.full_like(angles, x), angles, columns=True)
        _, fx, ft, fxx, fxt, ftt, _, fxxt, fxtt, _ = geometry.paired_jets(x, angles)
        C = np.cross(ft, fx)
        Cx = np.cross(fxt, fx)+np.cross(ft, fxx)
        inner = lambda u,v: np.sum(u*v,axis=-1)
        m, n, G = (raw[k] for k in ("m", "n", "G"))
        mx, nx, Gx = inner(Cx,fxt)+inner(C,fxxt), inner(Cx,ftt)+inner(C,fxtt), 2*inner(C,Cx)
        mp, np_, Gp = (raw[k] for k in ("m_parameter", "n_parameter", "G_parameter"))
        b, w = -m/n, G/n
        bx, wx = -mx/n+m*nx/n**2, Gx/n-G*nx/n**2
        bp, wp = -mp/n+m*np_/n**2, Gp/n-G*np_/n**2
        xp = evaluator.root_p*s
        sqk = np.sqrt(float(radial["minus_K"][0]))
        sqkp = (float(radial["minus_K_columns"][0,0])
                +xp*float(radial["minus_K_x"][0]))/(2*sqk)
        field = evaluator.evaluate(tau, angles, -1.)
        direct = evaluator.root*cosine*(b-w*sqk)
        first = (evaluator.root_p*cosine*(b-w*sqk)
                 +evaluator.root*cosine*(bp+xp*bx-(wp+xp*wx)*sqk-w*sqkp))
        fixed_x_comparison.append(dict(tau=tau,
            field_difference=float(np.max(abs(direct-field["f"]))),
            first_parameter_difference=float(np.max(abs(first-field["f_parameter"])))))
    # Meaningful independent comparisons: actual finite parameter shifts with
    # separately solved roots, plus the pre-existing fixed-x first-column.
    shifts = []
    for sign in (-1, 1):
        changed = SymmetricAffineGeometry(geometry.frozen, geometry.direction,
                    geometry.delta+sign*args.parameter_step, geometry.nodes)
        point = root["root_center"]
        probe = ActualAffineSecondField(changed, point, args.root_quadrature)
        for _ in range(4):
            C, _, _ = probe.target_jets(point)
            point -= float(C[0, 0]/C[1, 0])
        probe = ActualAffineSecondField(changed, point, args.root_quadrature)
        shifts.append([probe.evaluate(t, angles, -1.) for t in taus])
    first, second, mixed = [], [], []
    for base, minus, plus in zip(fields, *shifts):
        step = args.parameter_step
        first.append(float(np.max(abs((plus["f"]-minus["f"])/(2*step)-base["f_parameter"]))))
        second.append(float(np.max(abs((plus["f"]-2*base["f"]+minus["f"])/(step*step)-base["f_parameter_parameter"]))))
        mixed.append(float(np.max(abs((plus["f_theta"]-minus["f_theta"])/(2*step)-base["f_theta_parameter"]))))
    report = dict(kind="floating_actual_affine_fixed_tau_second_source_diagnostic",
        source_sha256=digest(Path(__file__)), object_sha256=digest(args.object),
        root_certificate_sha256=digest(args.root_certificate),
        exact_delta_fraction=str(Fraction.from_float(geometry.delta)),
        root=evaluator.root, root_parameter=evaluator.root_p,
        root_parameter_parameter=evaluator.root_pp,
        exact_binary_knot_regularity_checks=knot_regularity,
        root_quadrature=args.root_quadrature, angles=angles.tolist(), taus=taus.tolist(),
        fields=[{key:np.asarray(value).tolist() for key,value in row.items()} for row in fields],
        comparison_with_preexisting_fixed_x_analytic_column=fixed_x_comparison,
        finite_difference_step=args.parameter_step,
        finite_difference_max_discrepancy=dict(first_parameter=max(first),
            second_parameter=max(second), theta_parameter=max(mixed)),
        per_tau_discrepancy=dict(first_parameter=first,second_parameter=second,theta_parameter=mixed),
        elapsed_seconds=time.monotonic()-started,
        limitations=["analytic source derivatives, but floating evaluation only",
            "finite FFT primitive, root centre, quadrature and rounding remain unpaid",
            "finite differences validate samples only; they do not define the derivative",
            "no continuous parameter Taylor or true return bound is established"])
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("root_parameter","root_parameter_parameter", "finite_difference_max_discrepancy","elapsed_seconds")}),flush=True)


if __name__ == "__main__":
    main()
