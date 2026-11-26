#!/usr/bin/env python3
"""R603: exact prepared center jet/speed and the original R598 mass equations.

Science is executed only by the named public Actions runner. The paid guide
parameters enter the exact h_ss(0)=H, k_s(0)=2 family, not an old fit replay.
The old finite physical chart is applied independently to every column.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np
from scipy.integrate import simpson, solve_ivp
from scipy.optimize import brentq, least_squares
from scipy.spatial.distance import pdist

import r598_wide_mother_prepared_mass_bvp_agent as base

previous, paid = base.previous, base.paid
LD, ODD, emit = base.LD, base.ODD, base.emit


class ColumnCoordinates(previous.CenterCoordinates):
    """Only a batch adapter; every physical inverse is the original one."""

    def encode(self, geometry):
        values = np.asarray(geometry)
        if values.ndim == 1:
            return paid.FiniteCoordinates.encode(self, values)
        if values.ndim != 2 or values.shape[0] != 5:
            raise ValueError("physical geometry must be one vector or 5-by-N columns")
        return np.column_stack([
            paid.FiniteCoordinates.encode(self, values[:, index])
            for index in range(values.shape[1])
        ])


class ColumnMassRHS(base.MassRHS):
    def __init__(self, coefficients, potential, coordinate_guard):
        super().__init__(coefficients, potential, coordinate_guard)
        self.coordinates = ColumnCoordinates(self.nuhat_scale)

    def set_gauge_unit(self, unit):
        # Same fixed unit, physical chart, AD, guards and ten true parameters.
        super().set_gauge_unit(unit)
        self.coordinates = ColumnCoordinates(self.nuhat_scale)


class CenterJetGuide(base.PreparedGuide):
    """Nine parameters impose h_ss(0)=h(0) and k_s(0)=vstar, vstar=+/-2.

    Parameters: H, alpha_1,alpha_2,alpha_3,b_1,...,b_4,L.
    alpha_0, alpha_4 and b_5(c) are exact dependent coefficients. The same
    monotone scalar c pays integral h*k=0; it is not a pointwise control.
    """
    def __init__(self, root_order, center_speed):
        super().__init__(root_order)
        if center_speed not in (-2.,2.):
            raise ValueError("the R603 center speed must be +2 or -2")
        self.center_speed = float(center_speed)

    def expand(self, parameters, c):
        if len(parameters) != 9:
            raise ValueError("the vtwo center-jet guide has nine parameters")
        h0, aa1, aa2, aa3 = parameters[:4]
        length = parameters[-1]
        shifted = h0-1.9
        if not (-1 < shifted < 1):
            raise ValueError("the new center must lie in the open tanh height range")
        total = np.arctanh(shifted)
        weighted = -h0*length*length/(np.pi*np.pi*(1-shifted*shifted))
        aa4 = (weighted-aa1-4*aa2-9*aa3)/16
        aa0 = total-aa1-aa2-aa3-aa4
        target = 2*length*self.center_speed/(1.95*np.pi)
        bb5 = (target-c-np.dot(np.array([3.,5.,7.,9.]),parameters[4:8]))/11
        return np.r_[aa0,aa1,aa2,aa3,aa4,parameters[4:8],bb5,length]

    def fields(self, parameters, x, c):
        return base.PreparedGuide.fields(self.expand(parameters,c),x,c)

    def center_coefficient(self, parameters):
        self.root_solves += 1

        def residual(c):
            self.root_integrand_calls += 1
            h,k,*_ = self.fields(parameters,self.root_x,c)
            return np.dot(self.root_w,h*k)

        # dK/dc=sin(theta)-sin(11 theta)/11>0 at every positive Gauss node.
        target = 2*parameters[-1]*self.center_speed/(1.95*np.pi)
        radius = 2+2*np.sum(np.abs(parameters[4:8]))+abs(target)
        while residual(-radius)*residual(radius) > 0:
            radius *= 2
            if radius > 1024:
                raise FloatingPointError("vtwo_monotone_root_outside_declared_bracket_scope")
        return brentq(residual,-radius,radius,xtol=2.e-13,rtol=8.e-15,maxiter=100)


def new_guide_from_paid_parameters(args, model):
    """Fit the R603 exact-jet/speed family from the actual paid 11-vector."""
    started = time.time()
    parent = np.asarray(args.parent_guide,dtype=float)
    if parent.shape != (11,) or not np.all(np.isfinite(parent)):
        raise ValueError("one finite paid eleven-parameter guide is required")
    # This numerical conversion occurs here in Actions, never in local review.
    initial = np.r_[1.9+np.tanh(np.sum(parent[:5])),
                    parent[1:4],parent[5:9],parent[10]]
    lower = np.r_[.95,np.full(7,-2.5),2.05]
    upper = np.r_[2.85,np.full(7,2.5),7.5]
    if not (np.all(initial > lower) and np.all(initial < upper)):
        raise ValueError("mapped paid input is outside the declared new finite scope")
    x = np.linspace(0.,1.,args.guide_nodes)
    kept = np.array([0,1,3,4,5,6,7])
    scale = np.array([2.,1.,8.,8.,4.,4.,8.])
    best = {"parameters":initial.copy(),"score":float("inf")}
    feasible = {"parameters":None,"score":float("inf")}
    calls = 0
    first_c = None

    def residual(parameters):
        nonlocal calls,first_c
        calls += 1
        geometry,_,_,current_c = model.geometry(parameters,x)
        if calls == 1:
            first_c = float(current_c)
        ac = model.prepared(geometry)
        endpoint = ac+parameters[-1]*simpson(previous.matrix_rates(geometry),x=x,axis=1)
        core = endpoint[kept]/parameters[-1]*scale
        overflow = np.array([np.max(np.abs(geometry[2]))-.94,
                             np.max(np.abs(geometry[3]))-5.7,
                             np.max(np.abs(geometry[4]))-5.7])
        value = np.r_[core,25*np.maximum(overflow,0.)]
        score = np.linalg.norm(value)
        if score < best["score"]:
            best.update(parameters=parameters.copy(),score=float(score))
        if np.all(overflow < 0) and np.linalg.norm(core) < feasible["score"]:
            feasible.update(parameters=parameters.copy(),score=float(np.linalg.norm(core)))
        return value

    first = residual(initial)
    emit("R603_VTWO_NEW_GUIDE_INPUT",{
        "paid_parent_parameters":parent.tolist(),
        "mapped_new_nine_parameters":initial.tolist(),
        "mapped_actual_eleven_coefficients":model.expand(initial,first_c).tolist(),
        "initial_dependent_c":first_c,"center_speed_target":model.center_speed,
        "first_new_residual":first.tolist(),
        "old_eleven_or_unrun_ten_parameter_fit_replayed":False,
        "exact_center_definition":"h_ss(0)=h(0), k_s(0)=vstar, k_ss(0)=0",
        "full_M_and_positive_square_unchanged":True})
    result = least_squares(residual,initial,bounds=(lower,upper),method="trf",
                           jac="3-point",x_scale="jac",max_nfev=args.guide_max_nfev,
                           ftol=1.e-12,xtol=1.e-12,gtol=1.e-12)
    chosen = feasible["parameters"] if feasible["parameters"] is not None else best["parameters"]
    last = residual(chosen)
    fine_x = np.linspace(0.,1.,args.history_nodes)
    geometry,a,b,c = model.geometry(chosen,fine_x)
    ac = model.prepared(geometry)
    endpoint = ac+chosen[-1]*simpson(previous.matrix_rates(geometry),x=fine_x,axis=1)
    record = {
        "new_nine_parameters":chosen.tolist(),
        "actual_eleven_coefficients":model.expand(chosen,c).tolist(),
        "dependent_c":float(c),"prepared_center_Aodd":ac[ODD].tolist(),
        "eight_true_numerical_endpoint_moments":endpoint.tolist(),
        "initial_residual":first.tolist(),"chosen_residual":last.tolist(),
        "actual_residual_calls":calls,"nfev":int(result.nfev),
        "status":int(result.status),"message":str(result.message),
        "success":bool(result.success),
        "feasible_sampled_guide_found":feasible["parameters"] is not None,
        "elapsed_seconds":time.time()-started,
        "geometry_ranges":{name:[float(row.min()),float(row.max())]
                          for name,row in zip(("h","k","eta","gamma","upsilon"),geometry)},
        "numerical_center_jet_readout":{
            "h0":float(geometry[0,0]),"h_ss0":float(a[0]),"k_ss0":float(b[0]),
            "h_ss0_minus_h0":float(a[0]-geometry[0,0]),
            "k_s0":float(geometry[4,0]),"k_s0_minus_target":float(geometry[4,0]-model.center_speed)},
        "center_speed_target":model.center_speed,
        "monotone_root_quadrature_order":args.guide_root_order,
        "monotone_root_solves":model.root_solves,
        "monotone_root_integrand_calls":model.root_integrand_calls,
        "sampled_eta_is_not_a_continuous_box_certificate":True,
        "exact_moment_or_ruling_root_claim":False,
        "entire_energy_or_highest_potential_deleted":False,
        "R603_limit_is_not_finite_epsilon_nonexistence":True}
    emit("R603_VTWO_NEW_GUIDE",record)
    return model,chosen,c,record


def retain_complete_mass_input(rhs,x,y,p,unit,seed):
    """Print the completed physical seed before the first mass evaluation."""
    data = {
        "schema":"r603-vtwo-center-complete-mass-input-v1",
        "clock_nodes":x.tolist(),"state_rows":y.tolist(),"parameters":p.tolist(),
        "acceleration_unit":base.ACCELERATION_UNIT,
        "fixed_differential_row_units":[1.]*19,"fixed_ruling_unit":float(unit),
        "fixed_center_null_parameter_unit":float(rhs.nuhat_scale),
        "fixed_state_guard_units":rhs.state_guard_units.tolist(),
        "fixed_parameter_guard_units":rhs.parameter_guard_units.tolist(),
        "exact_old_encoder_applied_columnwise":True,
        "physical_chart_or_mass_equation_changed":False,
        "complete_initial_input_only_not_accepted_root":True,
        "seed_record":seed}
    canonical = json.dumps(data,sort_keys=True,separators=(",",":"),allow_nan=False)
    emit("R603_VTWO_COMPLETE_MASS_INPUT",{
        "state_sha256":hashlib.sha256(canonical.encode()).hexdigest(),
        "complete_state":data})


def final_mass_geometry_budget(rhs,system,current):
    """Original geometry of this actual final interpolant, not an exact root.

    The shape entries use derivatives of its h,k rather than unsatisfied
    velocity-state values. This makes the geometric readout unambiguous even
    when the mass solver stops with a nonzero physical kinematic defect.
    """
    started = time.time()
    interpolant = system.physical_spline(current)
    _,_,_,length_jet = rhs.coordinates.center(
        [paid.constant(v,0) for v in current["p"]])
    length = float(length_jet.value)
    geometry_calls = 0

    def geometry_at(x):
        nonlocal geometry_calls
        geometry_calls += 1
        encoded = interpolant(np.array([x]))[:,0]
        geometry,chart = rhs.coordinates.physical([paid.constant(v,0) for v in encoded])
        return (np.asarray([v.value for v in geometry],dtype=float),
                np.asarray([v.value for v in chart],dtype=float))

    def ode(x,state):
        geometry,_ = geometry_at(x)
        h,k = geometry[:2]
        frame = state[:9].reshape(3,3)
        omega = np.array([[0.,-k,0.],[k,0.,1.],[0.,-1.,0.]])
        return length*np.r_[(frame@omega).ravel(),h*h*frame[:,0]]

    solution = solve_ivp(ode,(0.,1.),np.r_[np.eye(3).ravel(),np.zeros(3)],
                         method="DOP853",rtol=2.e-10,atol=2.e-12,dense_output=True)
    if not solution.success:
        return {"frame_success":False,"message":str(solution.message),
                "frame_nfev":int(solution.nfev),"geometry_calls":geometry_calls,
                "elapsed_seconds":time.time()-started,"exact_geometry_claim":False}
    x = np.linspace(0.,1.,513)
    samples = [geometry_at(t) for t in x]
    geometry = np.asarray([pair[0] for pair in samples]).T
    chart = np.asarray([pair[1] for pair in samples]).T
    derivatives = chart*interpolant(x,1)[:5]/length
    h,k,eta,gamma_state,upsilon_state = geometry
    gamma,upsilon = derivatives[:2]
    posed = solution.sol(x)
    frames,alpha = posed[:9].T.reshape(-1,3,3),posed[9:].T
    normal = frames[:,:,1]
    edges,curvatures = [],[]
    for yy in (4.,6.):
        for sign in (1,-1):
            u = h/(yy+sign*eta)
            if sign == 1:
                edges.append(alpha+u[:,None]*normal)
            else:
                edges.append(np.array([-1.,-1.,1.])*(alpha-u[:,None]*normal))
            kk,gg,vv = sign*k,sign*gamma,upsilon
            aa = h*h-kk*u
            den = np.sqrt(aa*aa+u*u)
            s11 = u*(2*h*gg-vv*u)/den**3
            s12 = -h*h/den**2
            curvatures.append((np.abs(s11)+np.sqrt(s11*s11+4*s12*s12))/2)
    diameter = float(np.max(pdist(np.concatenate(edges))))
    curvature = float(np.max(curvatures))
    return {"frame_success":True,"frame_nfev":int(solution.nfev),
            "geometry_calls":geometry_calls,"elapsed_seconds":time.time()-started,
            "sampled_edge_diameter":diameter,"sampled_principal_curvature_max":curvature,
            "sampled_focal_cap":1/curvature,
            "sampled_focal_cap_over_edge_diameter":1/(curvature*diameter),
            "two_pose_readouts":[float(normal[-1,2]**2-.5),
                float(alpha[-1,0]*normal[-1,1]-alpha[-1,1]*normal[-1,0])],
            "sampled_true_hk_derivative_vs_velocity_state_max":float(np.max(np.abs(
                derivatives[:2]-np.array([gamma_state,upsilon_state])))),
            "shape_entries_use_actual_interpolant_derivatives":True,
            "readout_scope":"this actual final interpolant only, even if equations remain open",
            "continuous_reach_embedding_finite_flex_or_root_claim":False}


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Science only in the declared public Actions repository")
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent-guide",type=json.loads,required=True)
    parser.add_argument("--center-speed",type=float,choices=(-2.,2.),default=2.)
    parser.add_argument("--order",type=int,default=192)
    parser.add_argument("--gap-order",type=int,default=8)
    parser.add_argument("--guide-root-order",type=int,default=96)
    parser.add_argument("--guide-nodes",type=int,default=257)
    parser.add_argument("--guide-max-nfev",type=int,default=400)
    parser.add_argument("--history-nodes",type=int,default=513)
    parser.add_argument("--intervals",type=int,default=32)
    parser.add_argument("--newton-iterations",type=int,default=50)
    parser.add_argument("--trial-limit",type=int,default=12)
    parser.add_argument("--linear-iterations",type=int,default=1600)
    parser.add_argument("--trust-radius",type=float,default=.25)
    parser.add_argument("--maximum-trust",type=float,default=4.)
    parser.add_argument("--damping",type=float,default=1.e-4)
    parser.add_argument("--acceptance-ratio",type=float,default=1.e-4)
    parser.add_argument("--coordinate-guard",type=float,default=1.e6)
    parser.add_argument("--flow-tol",type=float,default=1.e-7)
    parser.add_argument("--ruling-tol",type=float,default=1.e-7)
    parser.add_argument("--bc-tol",type=float,default=1.e-10)
    args = parser.parse_args()
    started = time.time()
    coefficients = model = rhs = None
    status = "not_initialized"
    try:
        # Necessary same-mother table recreation: its numbers were not stored.
        # There is no old identity, derivative, quadrature or optimizer gate.
        labels,rows = previous.rebuild_known_rows()
        grid = base.WideReferenceGrid(args.order,args.gap_order,5.)
        coefficients = base.CountedCoefficients(labels,rows,grid)
        potential = previous.FactoredPotential(grid)
        emit("R603_VTWO_FIXED_MOTHER",{
            "graph":grid.graph_info,"coefficients":coefficients.stats,
            "positive_Gram":potential.stats,
            "same_R598_physical_mother":True,
            "necessary_table_recreation_counted":True,
            "old_numeric_table_not_stored_or_reloaded":True,
            "old_identity_derivative_or_quadrature_gate_repeated":False,
            "full_square_coefficient":1})
        model = CenterJetGuide(args.guide_root_order,args.center_speed)
        model,guide,c,guide_record = new_guide_from_paid_parameters(args,model)
        emit("R603_VTWO_NEW_GEOMETRY_BUDGET",
             base.guide_geometry_budget(model,guide,c,grid))
        rhs = ColumnMassRHS(coefficients,potential,args.coordinate_guard)
        x,y,p,unit,seed = base.make_seed(rhs,model,guide,c,args)
        retain_complete_mass_input(rhs,x,y,p,unit,seed)
        system,current,summary,report = base.solve_mass(rhs,x,y,p,unit,args)
        if summary["status"] == "actual_discrete_mass_equations_converged":
            refined = np.linspace(0.,1.,4*args.intervals+1)
            physical = system.physical_spline(current)(refined)
            accelerations = np.vstack([
                np.interp(refined,system.x,row) for row in current["y"][19:]])
            system,current,summary,report = base.solve_mass(
                rhs,refined,np.vstack([physical,accelerations]),current["p"],unit,args,1)
        status = summary["status"]
        try:
            budget = final_mass_geometry_budget(rhs,system,current)
            json.dumps(budget,allow_nan=False)
            emit("R603_VTWO_FINAL_MASS_GEOMETRY_BUDGET",budget)
        except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
            emit("R603_VTWO_FINAL_GEOMETRY_FAILURE",{
                "type":type(exc).__name__,"message":str(exc),
                "last_complete_mass_state_retained":True})
    except (FloatingPointError,ValueError,OverflowError,RuntimeError) as exc:
        status = "new_vtwo_guide_or_mass_attempt_failed"
        emit("R603_VTWO_FAILURE",{"type":type(exc).__name__,"message":str(exc),
             "physical_square_not_removed":True,"exact_root_claim":False})
    emit("R603_VTWO_DONE",{
        "elapsed_seconds":time.time()-started,"last_status":status,
        "coefficient_value_evaluations_all_scopes":None if coefficients is None else coefficients.value_calls,
        "coefficient_jet_evaluations_all_scopes":None if coefficients is None else coefficients.jet_calls,
        "guide_geometry_calls":None if model is None else model.geometry_calls,
        "guide_scalar_root_solves":None if model is None else model.root_solves,
        "guide_scalar_integrand_calls":None if model is None else model.root_integrand_calls,
        "mass_RHS_calls":None if rhs is None else rhs.calls,
        "mass_RHS_points":None if rhs is None else rhs.points,
        "mass_Jacobian_calls":None if rhs is None else rhs.jacobian_calls,
        "mass_direct_state_evaluations":None if rhs is None else rhs.direct_state_evaluations,
        "mass_derivative_state_evaluations":None if rhs is None else rhs.derivative_state_evaluations,
        "README_completion_claim":False,"full_period_or_reach_claim":False})


if __name__ == "__main__":
    main()

