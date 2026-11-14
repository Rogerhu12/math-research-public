#!/usr/bin/env python3
"""Actual full-DN attempt with explicit nonaxisymmetric-prefix controls.

The original equations, complete modes, tail client, Newton, line search,
RMS and BC tolerances are retained.  Only the separately serialized scalar
design supports change.  The domain preflight includes the two actual
Lobatto RMS queries, and the unchanged QR factor exposes its small matrix,
near-null vectors and linear residual locations before any acceptance.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key] = "1"

import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.linalg import solve_triangular

import geometry_20261114_full_dn_solve as original
from geometry_20261114_prefix_controls_profile import (
    PrefixControlsProfile, SCHEMA, SCHEME, scalar_spec)


HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def argument(name):
    if name not in sys.argv:
        return None
    return Path(sys.argv[sys.argv.index(name)+1])


def finite(value):
    value = np.asarray(value)
    return float(np.max(abs(value))) if value.size and np.all(np.isfinite(value)) else None


def point_domain(flow,s,y):
    """Read the original real point-domain expression, without taking sqrt(beta2)."""
    _,d,dd = flow.q.jet(np.asarray(y[:flow.n],float))
    lam2 = np.sum(d*d,axis=1)
    tangent = d/np.sqrt(lam2)[:,None]
    normal = dd-np.sum(dd*tangent,axis=1)[:,None]*tangent
    curvature = np.sqrt(np.sum(normal*normal,axis=1))/lam2
    a,ap,app = flow.scalar_jets(np.array([s]),np.asarray(y[flow.parameter_slice])[:,None])[0]
    margin = 1-(ap/(a*curvature))**2
    at = int(np.argmin(margin))
    return dict(s=float(s),a=float(a),ap=float(ap),app=float(app),
                minimum_beta_squared=float(margin[at]),phi=float(2*np.pi*at/flow.q.N),
                curve_curvature_at_minimum=float(curvature[at]),
                scalar_parameters=np.asarray(y[flow.parameter_slice]).tolist())


def rms_domain(x,values,rhs,flow):
    """The exact two off-midpoint fractions used by SciPy's RMS estimator."""
    h = np.diff(x)
    fractions = (.5-.5*np.sqrt(3/7),.5+.5*np.sqrt(3/7))
    curve = CubicHermiteSpline(x,values,rhs,axis=0)
    bad_points,rows = [],[]
    for fraction in fractions:
        points = x[:-1]+fraction*h
        yy = curve(points)
        result = flow(points,yy.T)
        bad = np.flatnonzero(~np.all(np.isfinite(result),axis=0))
        bad_points.extend(points[bad].tolist())
        samples = []
        for j in bad[:24]:
            samples.append(dict(interval=int(j),left=float(x[j]),right=float(x[j+1]),
                                **point_domain(flow,points[j],yy[j])))
        rows.append(dict(fraction=float(fraction),points=len(points),invalid_count=len(bad),
                         first_invalid_points=samples))
    return np.asarray(bad_points),rows


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run this actual numerical attempt only in the public repository's Actions")
    output = argument("--out")
    if output is None:
        raise ValueError("The original full-DN CLI requires --out")
    output.mkdir(parents=True,exist_ok=True)
    own_hash = sha(__file__)
    source_hashes = {name:sha(HERE/name) for name in (
        "geometry_20261114_full_dn_solve.py","geometry_20261114_prefix_controls_profile.py",
        "geometry_20261114_full_scalar_profile.py","geometry_20261114_separated_qr_bvp.py",
        "geometry_20261114_full_dn_augmented.py","geometry_20261114_full_dn_boundary.py")}
    warm_path = argument("--warm")
    warm = original.read(warm_path) if warm_path else None
    analytic_new_points_allowed = True
    if warm is not None:
        values = np.asarray(warm.get("augmented_states",warm["states"]),float)
        params = values[:,-3:]
        analytic_new_points_allowed = bool(np.all(params == 0))
        spec = warm.get("complete_scalar_profile",warm.get("fixed_scalar_profile",{}).get("geometry",{}))
        if np.any(params != 0) and (spec.get("schema") != SCHEMA or
                spec.get("control_scheme") != SCHEME or
                spec.get("profile_source_sha256") != source_hashes["geometry_20261114_prefix_controls_profile.py"]):
            raise ValueError("Nonzero warm controls cannot be reinterpreted under a different serialized control scheme")
    intent = dict(scope=__doc__,source_sha256=own_hash,original_sources_sha256=source_hashes,
        control_schema=SCHEMA,control_scheme=SCHEME,
        warm_sha256=sha(warm_path) if warm_path else None,
        original_saved_warm_nodes_retained_exactly=True,
        new_nodes_may_sample_original_analytic_zero_control_seed=analytic_new_points_allowed,
        unchanged_acceptance=dict(collocation_RMS=1e-6,boundary_residual=1e-11,
                                  complete_original_Newton_and_line_search=True),
        new_acceptance_claim=False)
    original.write(output/"prefix-controls-intent.json",intent)
    original_write = original.write
    def write(path,data):
        if isinstance(data,dict) and Path(path).name in ("driver-status.json","prepared.json.gz","actual.json.gz"):
            data["prefix_controls_design_adapter"] = intent
        original_write(path,data)
    original.write = write
    original.CompleteProfile = PrefixControlsProfile
    original.scalar_spec = scalar_spec
    original.__doc__ = __doc__
    original.__file__ = __file__
    base_guess = original.prepared_guess
    analytic = None
    def prepared_guess(*args,**kwargs):
        nonlocal analytic
        result = base_guess(*args,**kwargs)
        analytic = result[1]
        return result
    original.prepared_guess = prepared_guess
    base_preflight = original.preflight
    domain_history = []
    def preflight(mesh,initial_at,flow,max_nodes):
        saved_x = np.asarray(warm["mesh"],float) if warm is not None else np.asarray(mesh,float)
        if warm is not None:
            yy = np.asarray(warm.get("augmented_states",warm["states"]),float)
            ff = np.asarray(warm.get("augmented_rhs",warm["rhs"]),float)
            bad,rows = rms_domain(saved_x,yy,ff,flow)
            domain_history.append(dict(stage="original_saved_warm_before_new_controls",nodes=len(saved_x),
                                       invalid_RMS_points=len(bad),checks=rows))
            original_write(output/"RMS-domain-preflight.json",dict(history=domain_history))
        def safe_new_points(points):
            points = np.asarray(points,float)
            values = initial_at(points)
            if analytic_new_points_allowed:
                at = np.searchsorted(saved_x,points)
                saved = (at < len(saved_x)) & (saved_x[np.minimum(at,len(saved_x)-1)] == points)
                if np.any(~saved):
                    values[~saved] = analytic(points[~saved])
            return values
        all_additions = []
        for iteration in range(16):
            mesh,values,rhs,residual,additions = base_preflight(mesh,safe_new_points,flow,max_nodes)
            all_additions.extend(additions)
            bad,rows = rms_domain(mesh,values,rhs,flow)
            item = dict(iteration=iteration,nodes=len(mesh),invalid_RMS_points=len(bad),checks=rows)
            domain_history.append(item)
            original_write(output/"RMS-domain-preflight.json",dict(
                scope="Actual original RHS at every collocation and Lobatto RMS query; no relaxed domain or acceptance gate.",
                history=domain_history,saved_nodes_retained_exactly=True,
                only_inserted_zero_control_points_use_original_analytic_seed=analytic_new_points_allowed,
                extra_nodes=all_additions))
            print(json.dumps(dict(event="full_DN_RMS_domain_preflight",iteration=iteration,
                nodes=len(mesh),invalid_RMS_points=len(bad))),flush=True)
            if not len(bad):
                return mesh,values,rhs,residual,all_additions
            revised = original.original_solver.merge_mesh(mesh,bad)
            if len(revised) == len(mesh) or len(revised) > max_nodes:
                raise FloatingPointError("The actual RMS quadrature domain needs more than the declared node budget; original positions are recorded")
            all_additions.extend(float(s) for s in revised if s not in set(mesh))
            mesh = revised
        raise FloatingPointError("The complete actual RMS-query domain did not resolve")
    original.preflight = preflight
    base_factor = original.original_qr.DiskQRFactor
    factor_count = 0
    class DiagnosticFactor(base_factor):
        def finish(self):
            nonlocal factor_count
            factor_count += 1
            self.diagnostic_index = factor_count
            small = self.right@self.U[-1]
            U,singular,Vh = np.linalg.svd(small,full_matrices=False)
            packet = output/f"reduced-{factor_count:03d}.npz"
            np.savez_compressed(packet,small=small,singular_values=singular,U=U,Vh=Vh,
                                nullspace_left=self.U[0],nullspace_right=self.U[-1],
                                boundary_right=self.right)
            modes = []
            for j in range(1,min(7,self.k+1)):
                coordinate = Vh[-j].copy()
                endpoint = self.U[-1]@coordinate
                initial = None
                maximum = finite(endpoint)
                pdrift = cdrift = 0.
                try:
                    for i in range(self.m-2,-1,-1):
                        coordinate = solve_triangular(self.transport[i],coordinate,check_finite=False)
                        value = self.U[i]@coordinate
                        if not np.all(np.isfinite(value)):
                            raise FloatingPointError("Nonfinite homogeneous backward transport")
                        maximum = max(maximum,finite(value))
                        pdrift = max(pdrift,float(np.max(abs(value[-3:]-endpoint[-3:]))))
                        cdrift = max(cdrift,float(np.max(abs(value[290:386]-endpoint[290:386]))))
                        if i == 0:
                            initial = value
                    transport_error = None
                except (ValueError,FloatingPointError,np.linalg.LinAlgError) as error:
                    transport_error = repr(error)
                modes.append(dict(singular_value=float(singular[-j]),
                    endpoint_physical_norm=float(np.linalg.norm(endpoint[:290])),
                    endpoint_core_norm=float(np.linalg.norm(endpoint[290:386])),
                    endpoint_scalar_parameters=endpoint[-3:].tolist(),endpoint_z0=float(endpoint[193]),
                    inlet_scalar_parameters=None if initial is None else initial[-3:].tolist(),
                    homogeneous_state_max=maximum,constant_parameter_transport_drift=pdrift,
                    constant_core_transport_drift=cdrift,transport_error=transport_error))
            self.diagnostic = dict(factor=factor_count,n=self.n,nodes=self.m,free_dimensions=self.k,
                reduced_condition=float(singular[0]/singular[-1]) if singular[-1] else None,
                singular_values=singular.tolist(),
                numerical_ranks={str(tol):int(np.sum(singular > tol*singular[0])) for tol in (1e-8,1e-10,1e-12,1e-14,1e-16)},
                smallest_six_directions=modes,packet=dict(file=str(packet),sha256=sha(packet)),
                original_factor_and_solve_unchanged=True,mathematical_rank_certified=False,
                control_scheme=SCHEME)
            original_write(output/f"reduced-{factor_count:03d}.json",self.diagnostic)
            return super().finish()

        def solve(self,rhs):
            answer = super().solve(rhs)
            if self.solve_count == 1:
                values = answer.reshape(self.m,self.n)
                rhs = np.asarray(rhs)
                col = rhs[:(self.m-1)*self.n].reshape(self.m-1,self.n)
                worst = dict(absolute=0.)
                maxima = dict(physical=0.,constant_core=0.,constant_parameters=0.,left_boundary=0.,right_boundary=0.)
                for i in range(self.m-1):
                    with np.load(self.directory/f"{i:05d}.npz") as block:
                        error = block["L"]@values[i]+block["R"]@values[i+1]-col[i]
                    row = int(np.argmax(abs(error)))
                    if abs(error[row]) > worst["absolute"]:
                        worst = dict(absolute=float(abs(error[row])),interval=i,state_row=row)
                    maxima["physical"] = max(maxima["physical"],float(np.max(abs(error[:290]))))
                    maxima["constant_core"] = max(maxima["constant_core"],float(np.max(abs(error[290:386]))))
                    maxima["constant_parameters"] = max(maxima["constant_parameters"],float(np.max(abs(error[-3:]))))
                offset = (self.m-1)*self.n
                left = self.left@values[0]-rhs[offset:offset+self.nl]
                right = self.right@values[-1]-rhs[offset+self.nl:]
                maxima["left_boundary"],maxima["right_boundary"] = finite(left),finite(right)
                self.diagnostic["first_original_linear_solve"] = dict(
                    residual_max_by_block=maxima,worst_collocation_row=worst,rhs_max=finite(rhs),
                    solution_max=finite(answer),scalar_parameter_step_at_inlet=values[0,-3:].tolist(),
                    scalar_parameter_step_at_cut=values[-1,-3:].tolist())
                original_write(output/f"reduced-{self.diagnostic_index:03d}.json",self.diagnostic)
            return answer
    original.original_qr.DiskQRFactor = DiagnosticFactor
    return original.main()


if __name__ == "__main__":
    raise SystemExit(main())
