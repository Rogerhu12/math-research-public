#!/usr/bin/env python3
"""Full-state physical-quintic prefix in the common material angle.

This reader consumes an actually accepted full-DN output.  Its state already
contains the entire height, including z0.  No old small-field height primitive
or gauge factor is added.  It exposes the six Cartesian jets used by the
closed-map consumer, and all nine radial/angular derivatives needed for a
continuous angular cut correction.  Numerical evaluation belongs in the
public repository's Actions; construction is not a new BVP acceptance.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace

import numpy as np

import geometry_20261114_material_quintic_readout as physical
from geometry_20261114_prefix_controls_profile import reconstruct_profile, SCHEMA as PREFIX_CONTROL_SCHEMA
from root_20261114_scaled_core import r225_coefficients


HERE = Path(__file__).resolve().parent


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def actions_only():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Evaluate this numerical adapter in the public repository's Actions")


class PhysicalQuintic:
    """The existing saved-y/saved-RHS/finite-ODE-second physical C2 field."""
    def __init__(self, x, y, dy, ddy):
        self.x = np.asarray(x, float)
        self.nodal = tuple(np.asarray(v, float) for v in (y, dy, ddy))
        if not np.all(np.diff(self.x) > 0):
            raise ValueError("Physical knots must increase strictly")
        h = np.diff(self.x.astype(np.longdouble))
        y, dy, ddy = (v.astype(np.longdouble) for v in self.nodal)
        c0, c1, c2 = y[:-1], h[:, None]*dy[:-1], h[:, None]**2*ddy[:-1]/2
        A = y[1:]-c0-c1-c2
        B = h[:, None]*dy[1:]-c1-2*c2
        C = h[:, None]**2*ddy[1:]-2*c2
        self.coefficients = np.stack([c0, c1, c2, 10*A-4*B+C/2,
                                      -15*A+7*B-C, 6*A-3*B+C/2], axis=1)
        self.h = h
        # PPoly-compatible physical descending powers; state layout is full,
        # not the historical 3M+1 perturbation layout.
        self.c = np.transpose(self.coefficients[:, ::-1]/h[:, None, None]**
                              np.arange(5, -1, -1)[None, :, None], (1, 0, 2))

    def __call__(self, s, derivative=0):
        if derivative not in (0, 1, 2):
            raise ValueError("Only the saved physical zero/first/second jets are exposed")
        s = np.atleast_1d(np.asarray(s, float))
        if s.ndim != 1 or np.any(s < self.x[0]) or np.any(s > self.x[-1]):
            raise ValueError("Prefix requests must stay inside the saved interval")
        j = np.clip(np.searchsorted(self.x, s, side="right")-1, 0, len(self.x)-2)
        u = (s.astype(np.longdouble)-self.x[j].astype(np.longdouble))/self.h[j]
        result = np.zeros((len(s), self.nodal[0].shape[1]), np.longdouble)
        for k in range(derivative, 6):
            factor = 1
            for q in range(derivative):
                factor *= k-q
            result += (factor*u**(k-derivative)/self.h[j]**derivative)[:, None]*self.coefficients[j, k]
        # Exact saved-node requests retain their original binary64 jets.
        # This also keeps an exactly zero terminal nonmean height exactly zero.
        at = np.searchsorted(self.x, s)
        equal = (at < len(self.x)) & (self.x[np.minimum(at, len(self.x)-1)] == s)
        result[equal] = self.nodal[derivative][at[equal]]
        return np.asarray(result.T, float)


class LargeCoreSavedPrefix:
    """SavedPrefix-compatible six jets, with an explicit complete-state layout."""
    def __init__(self, checkpoint):
        actions_only()
        self.path = Path(checkpoint)
        self.rec = read(self.path)
        d = self.rec
        if (d.get("success") is not True or d.get("status") != 0 or
                not d.get("actual_tail") or d.get("collocation_rms_max", np.inf) > 1e-6 or
                d.get("boundary_residual_max", np.inf) > 1e-11 or
                d.get("physical_frozen_control_RMS_max", np.inf) > 1e-6):
            raise ValueError("An actually accepted full-DN physical field is required")
        self.M, self.N, self.mode = int(d["M"]), int(d["N"]), 2
        self.n = 3*self.M+2
        self.core = np.asarray(d["core"]["coefficients"], float)
        self.frequencies = 2*np.arange(1, self.M+1)
        self.density = (1-self.frequencies**2)*self.core
        reference = [Q(6,5)*v for v in r225_coefficients()]
        exact_core = [Q(float(v)) for v in self.core]
        rho_reference_lower = 1+sum((1-4*m*m)*v for m,v in enumerate(reference,1))
        rho_difference = sum((4*m*m-1)*abs(v-(reference[m-1] if m <= len(reference) else 0))
                             for m,v in enumerate(exact_core,1))
        self.rho_lower_exact = rho_reference_lower-rho_difference
        if self.M < len(reference) or self.rho_lower_exact <= 0:
            raise ValueError("The R237 complete-core bound does not certify this global material inverse; a stronger density certificate is required")
        self.profile_model = reconstruct_profile(d["fixed_scalar_profile"]["geometry"])
        if d["fixed_scalar_profile"]["geometry"].get("schema") not in (
                "complete-controlled-scalar-profile-v1",PREFIX_CONTROL_SCHEMA):
            raise ValueError("The complete frozen scalar profile, including every solved control, is required")
        x, Y, DY = (np.asarray(d[k], float) for k in ("mesh", "states", "rhs"))
        if Y.shape != (len(x), self.n) or DY.shape != Y.shape or self.core.shape != (self.M,):
            raise ValueError("The saved state is not the complete r0..rM,t1..tM,z0..zM layout")
        if not np.all(np.isfinite(Y)) or not np.all(np.isfinite(DY)):
            raise ValueError("Nonfinite saved physical field")
        law = d["original_metric_identity"]["law"]
        q = physical.base.native.outward.FullCoreProbe(self.core, self.M, self.N,
                        law["velocity"], law["length"], law["k0"])
        q.profile = self.profile_model.profile
        physical.base.fixed.fft.enable_fft(q)
        DDY, gap = [], 0.
        for s, y, yp in zip(x, Y, DY):
            fr = q.frame(float(s), y)
            local = q.project(fr["V"])
            gap = max(gap, float(np.max(abs(local-yp))))
            state = q.project(q.frame(float(s), y.astype(complex)+1j*1e-25*yp,
                                      strict=False)["V"]).imag/1e-25
            da = -fr["app"]/(fr["a"]*fr["kap"])+fr["ap"]**2/(fr["a"]**2*fr["kap"])
            db = -fr["al"]*da/fr["be"]
            DDY.append(state+q.project(da[:, None]*fr["N"]+db[:, None]*fr["B"]))
        self.quintic = PhysicalQuintic(x, Y, DY, np.asarray(DDY))
        self.sol = SimpleNamespace(x=x, y=Y.T, p=np.empty(0), sol=self.quintic)
        self.flow = SimpleNamespace(end=float(x[-1]), breaks=np.asarray(self.profile_model.knots, float),
                                    profile=self.profile, bridge=SimpleNamespace(sigma=-1.))
        self.kind = "complete-full-state-material-quintic"
        self.rotation_to_native = np.eye(2)
        self.translation_from_native = np.zeros(2)
        self.registration = None
        self.definition = dict(
            input_sha256=sha(self.path), source_sha256=sha(__file__),
            original_material_quintic_source_sha256=sha(HERE/"geometry_20261114_material_quintic_readout.py"),
            scalar_profile_source_sha256=sha(HERE/"geometry_20261114_full_scalar_profile.py"),
            prefix_controls_profile_source_sha256=sha(HERE/"geometry_20261114_prefix_controls_profile.py"),
            state_layout="r[0:M+1],t[1:M+1],z[0:M+1]; all physical, n=3M+2",
            includes_entire_z0=True, old_mean_added=False,
            polynomial="Unique physical quintic through saved y, saved RHS, original finite-ODE second jet",
            node_saved_vs_local_RHS_max=gap,
            global_rho_lower_exact=str(self.rho_lower_exact),
            material_circle_diffeomorphism_proof="R237 complete-core rational triangle bound relative to the independently recomputed R236 core",
            frozen_scalar_parameters=d["fixed_scalar_profile"]["geometry"]["frozen_design_parameters"],
            canonical_material_metric="ds^2+a(s; frozen_parameters)^2 dtheta^2",
            exact_isometry_certified=False)

    def profile(self, s):
        s = np.asarray(s, float)
        if s.ndim == 0:
            return self.profile_model.profile(float(s))
        values = np.array([self.profile_model.profile(float(v)) for v in s.ravel()])
        return tuple(values[:, j].reshape(s.shape) for j in range(3))

    def inverse(self, s, target):
        target = np.asarray(target, float)
        theta, back = np.unique(target, return_inverse=True)
        turns = np.floor(theta/(2*np.pi))
        t = theta-turns*(2*np.pi)
        phi, lo, hi = t.copy(), np.zeros_like(t), np.full_like(t, 2*np.pi)
        for iteration in range(100):
            arg = self.frequencies[:, None]*phi
            value = phi+(self.density/self.frequencies)@np.sin(arg)
            rho = 1+self.density@np.cos(arg)
            error = value-t
            active = abs(error) > 2e-14
            if not np.any(active):
                break
            lo = np.where(active & (error < 0), phi, lo)
            hi = np.where(active & (error > 0), phi, hi)
            trial = phi-error/rho
            bad = (trial <= lo) | (trial >= hi) | (~np.isfinite(trial)) | (rho <= 0)
            phi = np.where(active, np.where(bad, (lo+hi)/2, trial), phi)
        else:
            raise ValueError("Complete material inverse did not converge")
        if np.any(rho <= 0):
            raise ValueError("Material density is not positive at a requested angle")
        phi += turns*(2*np.pi)
        return phi[back].reshape(target.shape), float(np.max(abs(error), initial=0)), iteration+1

    def angle(self, s, phi):
        phi = np.asarray(phi, float)
        unique, back = np.unique(phi, return_inverse=True)
        arg = self.frequencies[:, None]*unique
        rho = 1+self.density@np.cos(arg)
        rhop = -(self.frequencies*self.density)@np.sin(arg)
        theta = unique+(self.density/self.frequencies)@np.sin(arg)
        values = {k:v[back].reshape(phi.shape) for k,v in dict(theta=theta, rho=rho, rhop=rhop).items()}
        for key in ("theta_s", "theta_ss", "rho_s", "rhop_s"):
            values[key] = np.zeros_like(phi)
        return values

    def mean_jets(self, s):
        """Actual material means; informational, never added to the field."""
        weights = np.r_[1., self.density/2]
        return tuple(self.quintic(s, order)[2*self.M+1:].T@weights for order in range(3))

    def height_jets(self, s, angular=None, order=None):
        return self.mean_jets(s)

    def _world(self, values, phi):
        phi = np.asarray(phi, float)
        if phi.ndim == 1:
            phi = np.broadcast_to(phi, (len(values), len(phi)))
        freq = 2*np.arange(self.M+1)
        arg = phi[:, None, :]*freq[None, :, None]
        C, S = np.cos(arg), np.sin(arg)
        C1, S1 = -freq[None, :, None]*S, freq[None, :, None]*C
        C2, S2 = -freq[None, :, None]**2*C, -freq[None, :, None]**2*S
        r, t, z = values[:, :self.M+1], values[:, self.M+1:2*self.M+1], values[:, 2*self.M+1:]
        product = lambda a,b:np.einsum("sm,smq->sq", a, b)
        R, T, Z = product(r,C), product(t,S[:,1:]), product(z,C)
        Rp, Tp, Zp = product(r,C1), product(t,S1[:,1:]), product(z,C1)
        Rpp, Tpp, Zpp = product(r,C2), product(t,S2[:,1:]), product(z,C2)
        rotating = [np.stack(v, axis=-1) for v in ((R,T,Z), (Rp-T,Tp+R,Zp),
                         (Rpp-2*Tp-R,Tpp+2*Rp-T,Zpp))]
        co, si = np.cos(phi), np.sin(phi)
        result = []
        for v in rotating:
            world = np.stack((co*v[...,0]-si*v[...,1], si*v[...,0]+co*v[...,1], v[...,2]), axis=-1)
            result.append(world)
        return result

    def nine_jets(self, s, theta, *, material=True, normalized=True):
        """F_{s^i theta^j}, i,j=0,1,2, without truncating the inverse angle."""
        s = np.atleast_1d(np.asarray(s, float))
        theta = np.asarray(theta, float)
        if theta.ndim == 1:
            theta = np.broadcast_to(theta, (len(s), len(theta)))
        if theta.shape[0] != len(s):
            raise ValueError("One angular row per radial request is required")
        if material:
            phi, residual, iterations = self.inverse(s, theta)
            angular = self.angle(s, phi)
            rho, rhop = angular["rho"][...,None], angular["rhop"][...,None]
        else:
            phi, residual, iterations = theta, 0., 0
        out = {}
        for i in range(3):
            values = self._world(self.quintic(s,i).T, phi)
            if material:
                values = [values[0], values[1]/rho,
                          values[2]/rho**2-values[1]*rhop/rho**3]
            for j,value in enumerate(values):
                if normalized:
                    value = value.copy()
                    xy = value[...,:2]
                    if i == 0 and j == 0:
                        xy = xy-self.translation_from_native
                    value[...,:2] = xy@self.rotation_to_native
                out[(i,j)] = value
        return out, residual, iterations

    def jets(self, s, phi, height=None):
        full, _, _ = self.nine_jets(s, phi, material=False)
        return six_jets(full)

    def material_jets(self, s, theta, height=None):
        full, error, iterations = self.nine_jets(s,theta)
        return six_jets(full), error, iterations

    def set_native_registration(self, prefix_points, native_points):
        """One proper SE(2), used on the whole prefix and every derivative."""
        if self.registration is not None:
            raise ValueError("The single global registration has already been frozen")
        p, n = np.asarray(prefix_points,float), np.asarray(native_points,float)
        pc, nc = p.mean(axis=0), n.mean(axis=0)
        U, singular, Vt = np.linalg.svd((p-pc).T@(n-nc))
        fix = np.eye(2)
        fix[-1,-1] = np.linalg.det(U@Vt)
        rotation = U@fix@Vt
        angle = float(np.arctan2(rotation[1,0],rotation[0,0]))
        co, si = np.cos(angle), np.sin(angle)
        rotation = np.array([[co,-si],[si,co]])
        # p_native = (p_prefix - c) R, i.e. p_prefix = p_native R^T+c.
        translation = pc-nc@rotation.T
        self.rotation_to_native = rotation
        self.translation_from_native = translation
        self.registration = dict(prefix_to_native_row_rotation=rotation.tolist(),
            prefix_translation_to_subtract=translation.tolist(), singular_values=singular.tolist(),
            determinant=float(np.linalg.det(rotation)), angular_samples=len(p),
            rotation_angle=angle, exact_rotation_definition="cos/sin of the recorded binary64 angle; the printed matrix is its floating evaluation",
            position_max_after=float(np.max(np.linalg.norm((p-translation)@rotation-n,axis=1))),
            definition="One least-squares proper SE(2) fitted to the complete cut samples and applied to the entire prefix; no per-angle or radial registration.")
        return self.registration


def six_jets(full):
    return {key:full[index] for key,index in dict(pos=(0,0),s1=(1,0),s2=(2,0),
                                                p1=(0,1),p2=(0,2),sp=(1,1)).items()}


def complete_material_means(saved, s, angular=None, batch=None):
    return saved.mean_jets(s), dict(definition="Direct full-state material mean z0 + sum(z_m*(1-4m^2)*c_m)/2; no old mean primitive and no double addition.",
        complete_modes=saved.M, old_mean_added=False, formula_exact_for_finite_phi_state=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    saved = LargeCoreSavedPrefix(args.checkpoint)
    result = dict(schema="large-core-complete-saved-prefix-v1", **saved.definition,
                  M=saved.M, N=saved.N, n=saved.n, end=saved.flow.end,
                  nodes=len(saved.sol.x), physical_cut_scalar_jet=list(saved.profile(saved.flow.end)),
                  cut_material_mean_012=[float(x[0]) for x in saved.mean_jets([saved.flow.end])],
                  nonlinear_solution_created=False, closed_surface=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
