#!/usr/bin/env python3
"""Floating evaluator for the explicit symmetric, exact-affine infinite R33 graph.

The mathematical object is S0+delta*V BEFORE rounding controls. Pure radial
primitives are evaluated by a quarter DFT approximation, while every angular
jet uses the exact unit-tangent formula. Infinite-tail and floating arithmetic
errors are not certified here. The target metric changes synchronously with
delta. No old approximate-mirror checkpoint is silently substituted.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_geometry import (
    PhaseGeometry, tangent_radial_jets, tangent_variation_jets,
)


def _derivatives(spline, x, order):
    return np.stack([spline(x, nu=j) if j <= spline.k else
                     np.zeros_like(spline(x)) for j in range(order + 1)])


def _jet_product(left, right):
    return np.stack([sum(math.comb(j, k) * left[k] * right[j-k]
                         for k in range(j + 1)) for j in range(len(left))])


class SymmetricAffineGeometry(PhaseGeometry):
    def __init__(self, frozen, direction, delta, quarter_nodes=256):
        self.frozen, self.direction = frozen, direction
        self.delta = float(delta)
        self.nodes = int(quarter_nodes)
        self.modes = frozen["phase_coefficients"].shape[1]
        if self.nodes % 4 or self.nodes < 4*self.modes + 8:
            raise ValueError("quarter nodes must be divisible by four and >=4M+8")
        self.solver = SimpleNamespace(modes=self.modes, mean_count=1)
        self.raw_phase = BSpline(frozen["phase_knots"], frozen["phase_coefficients"], 5)
        self.raw_variation = BSpline(frozen["phase_knots"], direction["phase_direction_coefficients"], 5)
        self.base = BSpline(frozen["base_knots"], frozen["base_radius_coefficients"], int(frozen["base_degree"]))
        self.shift = BSpline(frozen["shift_knots"], frozen["shift_coefficients"], int(frozen["shift_degree"]))
        self.means = [BSpline(frozen[f"mean{j}_knots"], frozen[f"mean{j}_radius_coefficients"],
                              int(frozen[f"mean{j}_degree"])) for j in range(len(frozen["alpha"]))]
        self.slopes = [BSpline(frozen[f"height{j}_slope_knots"], frozen[f"height{j}_slope_coefficients"],
                               int(frozen[f"height{j}_slope_degree"])) for j in range(len(self.means)+1)]
        # These are floating evaluations of the exact integral of each frozen
        # slope, rather than the old independently rounded height primitive.
        self.height_integrals = [sp.antiderivative() for sp in self.slopes]
        self.height_origins = [sp(0.) for sp in self.height_integrals]
        self.alpha0 = frozen["alpha"].copy()
        self.alpha_direction = direction["alpha_direction"].copy()
        self.alpha = self.alpha0 + self.delta*self.alpha_direction
        self.frequency = 4*np.fft.fftfreq(self.nodes, 1/self.nodes)
        self.angles = np.arange(self.nodes)*(np.pi/2)/self.nodes
        self.sine = np.sin(4*np.arange(1, self.modes+1)[:, None]*self.angles)
        self._cache = {}

    def _one_side(self, x, order):
        base = _derivatives(self.base, x, order)
        raw0 = _derivatives(self.raw_phase, x, order)
        rawp = _derivatives(self.raw_variation, x, order)
        raw = raw0 + self.delta*rawp
        phase, dphase = [], []
        for component, power in enumerate((3, 2)):
            weight = np.zeros_like(base)
            weight[0] = 1.
            for _ in range(power):
                weight = _jet_product(weight, base)
            phase.append(_jet_product(raw[..., component], weight[..., None]))
            dphase.append(_jet_product(rawp[..., component], weight[..., None]))
        phase, dphase = np.stack(phase, axis=-1), np.stack(dphase, axis=-1)
        radius = base + _derivatives(self.shift, x, order)
        dradius = np.zeros_like(radius)
        for a, da, sp in zip(self.alpha, self.alpha_direction, self.means):
            jet = _derivatives(sp, x, order)
            radius += a*jet
            dradius += da*jet
        height_jets = []
        for slope, primitive, origin in zip(self.slopes, self.height_integrals, self.height_origins):
            rows = [primitive(x)-origin]
            rows += [slope(x, nu=j-1) if j-1 <= slope.k else np.zeros_like(x)
                     for j in range(1, order+1)]
            height_jets.append(np.stack(rows))
        height = height_jets[0].copy()
        dheight = np.zeros_like(height)
        for a, da, jet in zip(self.alpha, self.alpha_direction, height_jets[1:]):
            height += a*jet
            dheight += da*jet
        mean, dmean = np.zeros((order+1, len(x), 3)), np.zeros((order+1, len(x), 3))
        mean[..., 0], mean[..., 2] = radius, height
        dmean[..., 0], dmean[..., 2] = dradius, dheight
        return phase, mean, dphase, dmean

    def profile_jets(self, x, order=3):
        x = np.atleast_1d(np.asarray(x, dtype=float))
        plus, minus = self._one_side(x, order), self._one_side(-x, order)
        signs = (-1.)**np.arange(order+1)
        phase_parity = signs[:, None, None, None]*np.array([1., -1.])[None, None, None, :]
        mean_parity = signs[:, None, None]*np.array([1., 1., -1.])[None, None, :]
        return dict(
            phase=(plus[0]+minus[0]*phase_parity)*.5,
            mean=(plus[1]+minus[1]*mean_parity)*.5,
            phase_parameter=(plus[2]+minus[2]*phase_parity)*.5,
            mean_parameter=(plus[3]+minus[3]*mean_parity)*.5,
        )

    def radial_coefficients(self, x):
        x = np.atleast_1d(x)
        key = x.tobytes()
        if key in self._cache:
            return self._cache[key]
        data = self.profile_jets(x)
        tangent, aux = tangent_radial_jets(data["phase"], self.sine)
        primitive = self.primitive_coefficients(tangent)
        mean = data["mean"]
        radial = []
        for j in range(4):
            coefficient = sum(math.comb(j, k)*mean[k, :, 0, None, None]*primitive[j-k]
                              for k in range(j+1))
            coefficient[:, 0, 2] += mean[j, :, 2]
            radial.append(coefficient)
        answer = dict(**data, radial=radial, primitive=primitive, auxiliary=aux)
        if len(self._cache) >= 3:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key] = answer
        return answer

    def variation_radial_coefficients(self, x):
        data = self.radial_coefficients(x)
        if "variation_radial" in data:
            return data["variation_radial"]
        dprimitive = self.primitive_coefficients(tangent_variation_jets(
            data["auxiliary"], data["phase_parameter"][:3], self.sine))
        mean, dmean = data["mean"], data["mean_parameter"]
        primitive, radial = data["primitive"], []
        for j in range(3):
            coefficient = sum(math.comb(j, k)*(
                dmean[k, :, 0, None, None]*primitive[j-k]
                +mean[k, :, 0, None, None]*dprimitive[j-k]) for k in range(j+1))
            coefficient[:, 0, 2] += dmean[j, :, 2]
            radial.append(coefficient)
        answer = [dict(radial=radial, mean=dmean[:3])]
        data["variation_radial"] = answer
        return answer

    def _angular_fields(self, data, inverse, theta):
        modes = 4*np.arange(1, self.modes+1)
        phase = data["phase"][:, inverse]
        dphase = data["phase_parameter"][:, inverse]
        sine, cosine = np.sin(theta[:, None]*modes), np.cos(theta[:, None]*modes)
        fields = np.einsum("rxmc,xm->rxc", phase, sine)
        dfields = np.einsum("rxmc,xm->rxc", dphase, sine)
        angular = np.einsum("rxmc,xm->rxc", phase, cosine*modes)
        dangular = np.einsum("rxmc,xm->rxc", dphase, cosine*modes)
        second = np.einsum("xmc,xm->xc", phase[0], -sine*modes**2)
        b, g = fields[0].T
        bx, gx = fields[1].T
        bxx, gxx = fields[2].T
        bt, gt = angular[0].T
        bxt, gxt = angular[1].T
        btt, gtt = second.T
        db, dg = dfields[0].T
        dbx, dgx = dfields[1].T
        dbt, dgt = dangular[0].T
        sb, cb, sg, cg = np.sin(b), np.cos(b), np.sin(g), np.cos(g)
        zero = np.zeros_like(b)
        eh = np.stack((-sb, cb, zero), axis=-1)
        ep = np.stack((-cb, -sb, zero), axis=-1)
        ez = np.stack((zero, zero, np.ones_like(b)), axis=-1)
        T = cg[:, None]*eh+sg[:, None]*ez
        eg = -sg[:, None]*eh+cg[:, None]*ez
        Q = 1+bt
        mul = lambda a, v: a[:, None]*v
        Tx = mul(cg*bx, ep)+mul(gx, eg)
        Txx = (mul(cg*bxx-2*sg*bx*gx, ep)-mul(cg*bx*bx, eh)
               +mul(gxx, eg)-mul(gx*gx, T))
        Dt = mul(cg*Q, ep)+mul(gt, eg)
        Dtx = (mul(cg*bxt-sg*(gx*Q+gt*bx), ep)-mul(cg*Q*bx, eh)
               +mul(gxt, eg)-mul(gt*gx, T))
        Dtt = (mul(cg*btt-2*sg*gt*Q, ep)-mul(cg*Q*Q, eh)
               +mul(gtt, eg)-mul(gt*gt, T))
        dT = mul(cg*db, ep)+mul(dg, eg)
        dTx = (mul(cg*dbx-sg*(dg*bx+gx*db), ep)-mul(cg*bx*db, eh)
                +mul(dgx, eg)-mul(gx*dg, T))
        dDt = (mul(cg*dbt-sg*(dg*Q+gt*db), ep)-mul(cg*Q*db, eh)
                +mul(dgt, eg)-mul(gt*dg, T))
        return T, Tx, Txx, Dt, Dtx, Dtt, dT, dTx, dDt

    def paired_jets(self, x, theta):
        x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
        shape, x, theta = x.shape, x.ravel(), theta.ravel()
        unique, inverse = np.unique(x, return_inverse=True)
        data = self.radial_coefficients(unique)
        pure = [self.evaluate_coefficients(field, inverse, theta) for field in data["radial"]]
        T, Tx, Txx, Dt, Dtx, Dtt, *_ = self._angular_fields(data, inverse, theta)
        a, ax, axx, _ = data["mean"][:, inverse, 0, None]
        fields = (pure[0], pure[1], a*T, pure[2], ax*T+a*Tx, a*Dt,
                  pure[3], axx*T+2*ax*Tx+a*Txx, ax*Dt+a*Dtx, a*Dtt)
        return tuple(value.reshape(shape+(3,)) for value in fields)

    def variation_jets(self, x, theta):
        x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
        shape, x, theta = x.shape, x.ravel(), theta.ravel()
        unique, inverse = np.unique(x, return_inverse=True)
        data = self.radial_coefficients(unique)
        variation = self.variation_radial_coefficients(unique)[0]
        pure = [self.evaluate_coefficients(field, inverse, theta) for field in variation["radial"]]
        T, Tx, _, Dt, _, _, dT, dTx, dDt = self._angular_fields(data, inverse, theta)
        a, ax = data["mean"][:2, inverse, 0, None]
        da, dax = data["mean_parameter"][:2, inverse, 0, None]
        fields = (pure[0], pure[1], da*T+a*dT, pure[2],
                  dax*T+ax*dT+da*Tx+a*dTx, da*Dt+a*dDt)
        return [tuple(value.reshape(shape+(3,)) for value in fields)]

    def principal_quantities(self, x, theta, columns=False):
        x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
        shape, x, theta = x.shape, x.ravel(), theta.ravel()
        unique, inverse = np.unique(x, return_inverse=True)
        data = self.radial_coefficients(unique)
        fx = self.evaluate_coefficients(data["radial"][1], inverse, theta)
        T, Tx, _, Dt, Dtx, Dtt, dT, dTx, dDt = self._angular_fields(data, inverse, theta)
        a, ax = data["mean"][:2, inverse, 0, None]
        ft, fxt, ftt, fxtt, fttt = a*T, ax*T+a*Tx, a*Dt, ax*Dt+a*Dtx, a*Dtt
        cross = np.cross(ft, fx)
        ctheta = np.cross(ftt, fx)+np.cross(ft, fxt)
        dot = lambda a, b: np.sum(a*b, axis=-1)
        result = dict(m=dot(cross, fxt), n=dot(cross, ftt), G=dot(cross, cross),
                      m_theta=dot(ctheta, fxt)+dot(cross, fxtt),
                      n_theta=dot(ctheta, ftt)+dot(cross, fttt),
                      G_theta=2*dot(cross, ctheta))
        if columns:
            variation = self.variation_radial_coefficients(unique)[0]
            vx = self.evaluate_coefficients(variation["radial"][1], inverse, theta)
            da, dax = data["mean_parameter"][:2, inverse, 0, None]
            vt, vxt, vtt = da*T+a*dT, dax*T+ax*dT+da*Tx+a*dTx, da*Dt+a*dDt
            dcross = np.cross(vt, fx)+np.cross(ft, vx)
            result.update(m_parameter=dot(dcross, fxt)+dot(cross, vxt),
                          n_parameter=dot(dcross, ftt)+dot(cross, vtt),
                          G_parameter=2*dot(cross, dcross))
        return {key:value.reshape(shape) for key,value in result.items()}


def load_exact_object(path, quarter_nodes=256):
    path = Path(path)
    definition = json.loads(path.read_text())
    topic = next((parent for parent in path.parents if (parent/"scripts").is_dir()), None)
    if topic is None:
        raise ValueError("object JSON must be inside the topic or use a topic directory")
    arrays = []
    for key in ("origin_inputs", "direction"):
        entry = definition[key]
        source = Path(entry["path"])
        if not source.is_absolute():
            source = topic/source
        if hashlib.sha256(source.read_bytes()).hexdigest() != entry["sha256"]:
            raise ValueError("frozen input SHA mismatch: "+key)
        with np.load(source, allow_pickle=False) as data:
            arrays.append({name:data[name].copy() for name in data.files})
    delta = float.fromhex(definition["delta_hex"])
    exact = definition["delta_fraction"]
    if Fraction.from_float(delta) != Fraction(int(exact["numerator"]), int(exact["denominator"])):
        raise ValueError("delta is not the recorded exact binary64 fraction")
    if delta != float(definition["delta"]):
        raise ValueError("inconsistent delta fields")
    metadata = json.loads(str(arrays[1]["metadata"]))
    if metadata["origin_inputs_sha256"] != definition["origin_inputs"]["sha256"]:
        raise ValueError("direction belongs to another origin")
    return SymmetricAffineGeometry(*arrays, delta, quarter_nodes), definition
