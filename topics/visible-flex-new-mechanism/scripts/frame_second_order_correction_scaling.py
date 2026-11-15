#!/usr/bin/env python3
"""Reversible scaling for the existing second-order-correction *linear* program.

SOC here means second-order correction, not a second-order cone. The helper
consumes arrays only; it never loads or evaluates a research surface. The old
physical correction, auxiliary upper bound, objective, original-unit residual
gate, and subsequent true two-grid gates remain the caller's responsibility.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import linprog

POLICY = "reversible-second-order-correction-LP-scaling-v1"


@dataclass(frozen=True)
class ScaledCorrectionLP:
    original_A: np.ndarray
    original_b: np.ndarray
    original_lower: np.ndarray
    original_upper: np.ndarray
    radius: float
    row_divisors: np.ndarray
    row_binary_exponents: np.ndarray
    A: np.ndarray
    b: np.ndarray
    lower: np.ndarray
    upper: np.ndarray
    objective: np.ndarray

    @property
    def physical_dimension(self):
        return self.A.shape[1] // 2

    def to_original(self, scaled_solution):
        z = np.asarray(scaled_solution, dtype=float)
        if z.shape != self.objective.shape or not np.all(np.isfinite(z)):
            raise ValueError("matching finite complete scaled primal required")
        x = self.radius * z
        if not np.all(np.isfinite(x)):
            raise FloatingPointError("nonfinite reconstructed original primal")
        return x

    def to_scaled(self, original_solution):
        x = np.asarray(original_solution, dtype=float)
        if x.shape != self.objective.shape or not np.all(np.isfinite(x)):
            raise ValueError("matching finite complete original primal required")
        z = x / self.radius
        if not np.all(np.isfinite(z)):
            raise FloatingPointError("nonfinite mapped scaled primal")
        return z

    def original_residuals(self, scaled_solution):
        """No scaled residual is substituted for these original-unit values."""
        z = np.asarray(scaled_solution, dtype=float)
        x = self.to_original(z)
        row_residual = self.original_A @ x - self.original_b
        bound_violation = max(0., float(np.max(self.original_lower - x)),
            float(np.max(x - self.original_upper)))
        n = self.physical_dimension
        return {
            "maximum_original_linear_row_violation":max(0., float(np.max(row_residual))),
            "maximum_original_linear_bound_violation":bound_violation,
            "maximum_scaled_linear_row_violation":max(0., float(np.max(self.A @ z-self.b))),
            "maximum_scaled_linear_bound_violation":max(0., float(np.max(self.lower-z)),
                float(np.max(z-self.upper))),
            "original_absolute_auxiliary_objective":float(np.sum(x[n:])),
            "scaled_objective":float(np.sum(z[n:])),
            "original_objective_from_scaled_factor":self.radius*float(np.sum(z[n:])),
            "reported_residuals_are_not_a_geometry_acceptance":True,
        }

    def original_dual_diagnostics(self, result, groups=None):
        """Map this same solver's marginal convention back to original units.

        This is a floating diagnostic, not a validated optimality certificate.
        Missing marginals/primal are reported as unavailable, not filled by 0.
        """
        if result.x is None:
            return {"available":False,"reason":"solver returned no primal"}
        try:
            primal=np.asarray(result.x,dtype=float)
        except (TypeError,ValueError):
            return {"available":False,"reason":"solver primal is not a finite numeric vector"}
        if primal.shape!=self.objective.shape or not np.all(np.isfinite(primal)):
            return {"available":False,"reason":"solver primal has wrong shape or nonfinite entries"}
        try:
            mu_s=np.asarray(result.ineqlin.marginals,dtype=float)
            lower_mu=np.asarray(result.lower.marginals,dtype=float)
            upper_mu=np.asarray(result.upper.marginals,dtype=float)
        except (AttributeError,TypeError,ValueError):
            return {"available":False,"reason":"solver marginals unavailable"}
        if (mu_s.shape!=self.b.shape or lower_mu.shape!=self.objective.shape
                or upper_mu.shape!=self.objective.shape
                or not all(np.all(np.isfinite(x)) for x in (mu_s,lower_mu,upper_mu))):
            return {"available":False,"reason":"matching finite solver marginals unavailable"}
        # SciPy minimization marginals: inequality <=0, lower >=0, upper <=0.
        mu=self.radius*mu_s/self.row_divisors
        x=self.to_original(primal)
        stationarity=self.objective-self.original_A.T@mu-lower_mu-upper_mu
        primal=float(self.objective@x)
        dual=float(self.original_b@mu+self.original_lower@lower_mu+self.original_upper@upper_mu)
        complementary=np.r_[mu*(self.original_b-self.original_A@x),
            lower_mu*(x-self.original_lower),upper_mu*(self.original_upper-x)]
        out={"available":True,"original_primal_objective":primal,
            "original_dual_objective_evaluated":dual,"original_primal_minus_dual":primal-dual,
            "maximum_original_stationarity_residual":float(np.max(abs(stationarity))),
            "maximum_original_complementarity_product":float(np.max(abs(complementary))),
            "dual_sign_violation":max(0.,float(np.max(mu)),float(np.max(-lower_mu)),float(np.max(upper_mu))),
            "marginal_conversion":"mu_original=r_c*mu_scaled/row_divisor; bound marginals unchanged",
            "floating_diagnostics_not_a_validated_optimality_or_geometry_certificate":True}
        if groups is not None:
            gs=np.asarray(groups,int)
            if gs.shape!=self.b.shape:raise ValueError("one group label for every affine LP row required")
            out["original_unit_inequality_group_summaries"]=[]
            for group in np.unique(gs):
                take=gs==group; contribution=self.original_A[take].T@(-mu[take])
                out["original_unit_inequality_group_summaries"].append({
                    "group":int(group),"rows":int(np.sum(take)),
                    "nonnegative_multiplier_sum":float(np.sum(-mu[take])),
                    "maximum_multiplier_magnitude":float(np.max(abs(mu[take]))),
                    "stationarity_contribution_infinity_norm":float(np.max(abs(contribution))),
                    "nonunique_decomposition_not_an_irreplaceable_physical_bottleneck":True})
        return out

    def definition(self):
        ex = self.row_binary_exponents
        return {
            "schema":POLICY,
            "problem_is_a_linear_program_not_a_second_order_cone_program":True,
            "old_variables":"v=D^-1 w and h_aux, both bounded in magnitude by r_c",
            "new_variables":"v=r_c z and h_aux=r_c t",
            "original_auxiliary_upper_bound_r_c_is_required":True,
            "positive_radius_evaluated":self.radius,
            "new_objective":"sum(t); original objective equals r_c * sum(t)",
            "each_scalar_affine_inequality_divided_by_positive_power_of_two":True,
            "row_divisor_rule":"2^clip(frexp(max(max_j(abs(r_c*A_ij)),abs(b_i))).exponent,-1022,1023); zero row uses 1",
            "row_count":int(self.A.shape[0]),
            "physical_dimension":self.physical_dimension,
            "row_binary_exponent_min":int(np.min(ex)),
            "row_binary_exponent_max":int(np.max(ex)),
            "zero_row_count":int(np.sum(np.all(self.original_A==0,axis=1)&(self.original_b==0))),
            "row_divisor_minimum":float(np.min(self.row_divisors)),
            "row_divisor_maximum":float(np.max(self.row_divisors)),
            "all_bounds_and_rows_map_bijectively_in_exact_arithmetic":True,
            "same_primal_optima_after_positive_objective_rescaling":True,
            "floating_solver_path_need_not_match_unscaled_solver":True,
            "original_unit_postsolve_residual_gate_must_be_retained":True,
            "same_true_geometry_gates_and_shared_time_budget_must_be_retained":True,
            "no_claim_that_scaling_repairs_infeasibility_or_proves_the_timeout_cause":True,
        }


def scale_correction_lp(A, b, lower, upper, radius):
    """Scale an already assembled old SOC LP; do not change any target or row.

    lower/upper cover the full 2n vector (v,h_aux). The existing bounds
    h_aux in [0,radius] are checked, so the entire extended feasible set is
    mapped, not just its projection to the physical correction.
    """
    A, b, lo, hi = [np.asarray(x, dtype=float) for x in (A,b,lower,upper)]
    radius = float(radius)
    if (A.ndim != 2 or A.shape[0] < 1 or A.shape[1] < 2 or A.shape[1] % 2
            or b.shape != (A.shape[0],) or lo.shape != (A.shape[1],) or hi.shape != lo.shape
            or not np.isfinite(radius) or radius <= 0
            or not all(np.all(np.isfinite(x)) for x in (A,b,lo,hi))
            or np.any(lo>hi)):
        raise ValueError("finite nonempty bounded 2n-variable SOC LP and positive radius required")
    n = A.shape[1]//2
    if (not np.array_equal(lo[n:],np.zeros(n))
            or not np.array_equal(hi[n:],np.full(n,radius))
            or np.any(lo[:n] < -radius) or np.any(hi[:n] > radius)):
        raise ValueError("the existing physical correction box and auxiliary [0,r_c] bounds are required")
    As = A*radius
    if not np.all(np.isfinite(As)):
        raise FloatingPointError("nonfinite SOC column scaling")
    magnitude = np.maximum(np.max(np.abs(As),axis=1),np.abs(b))
    _, exponent = np.frexp(magnitude)
    exponent = np.clip(exponent,-1022,1023).astype(np.int64)
    exponent[magnitude==0.] = 0
    divisor = np.ldexp(np.ones(len(b)),exponent)
    scaled_A, scaled_b = As/divisor[:,None], b/divisor
    scaled_lo, scaled_hi = lo/radius, hi/radius
    if not all(np.all(np.isfinite(x)) for x in (divisor,scaled_A,scaled_b,scaled_lo,scaled_hi)):
        raise FloatingPointError("nonfinite scaled SOC LP")
    # The caller may keep its original arrays; this helper never mutates them.
    result = ScaledCorrectionLP(A.copy(),b.copy(),lo.copy(),hi.copy(),radius,
        divisor,exponent,scaled_A,scaled_b,scaled_lo,scaled_hi,
        np.r_[np.zeros(n),np.ones(n)])
    for value in (result.original_A,result.original_b,result.original_lower,result.original_upper,
            result.row_divisors,result.row_binary_exponents,result.A,result.b,
            result.lower,result.upper,result.objective):
        value.flags.writeable=False
    return result


def developer_check():
    """Only small artificial affine arrays; no research loader or geometry."""
    radius=1/64000
    n=3
    rows=[];rhs=[]
    row=np.zeros(2*n);row[0]=-1.;rows.append(row);rhs.append(-.2*radius)
    row=np.zeros(2*n);row[1]=1.;rows.append(row);rhs.append(-.3*radius)
    row=np.zeros(2*n);row[0]=row[1]=1.;rows.append(row);rhs.append(.1*radius)
    for j in range(n):
        row=np.zeros(2*n);row[j]=1.;row[n+j]=-1.;rows.append(row);rhs.append(0.)
        row=np.zeros(2*n);row[j]=-1.;row[n+j]=-1.;rows.append(row);rhs.append(0.)
    rows.append(np.zeros(2*n));rhs.append(0.)
    A=np.array(rows);b=np.array(rhs)
    lo=np.r_[np.full(n,-radius),np.zeros(n)];hi=np.full(2*n,radius)
    copies=[x.copy() for x in (A,b,lo,hi)]
    scaled=scale_correction_lp(A,b,lo,hi,radius)
    points=np.array([[.2,-.3,0.,.2,.3,0.],
        [-.8,.1,.4,.8,.4,.7],[.9,.9,-.2,1.,1.,.5],[0.,0.,0.,0.,0.,0.]])
    mapping_error=max(float(np.max(np.abs(scaled.A@z-scaled.b-
        (A@scaled.to_original(z)-b)/scaled.row_divisors))) for z in points)
    back_error=max(float(np.max(np.abs(scaled.to_scaled(scaled.to_original(z))-z))) for z in points)
    options={"primal_feasibility_tolerance":1e-9,"dual_feasibility_tolerance":1e-9,"time_limit":3.}
    original=linprog(np.r_[np.zeros(n),np.ones(n)],A_ub=A,b_ub=b,
        bounds=list(zip(lo,hi)),method="highs",options=options)
    solved=linprog(scaled.objective,A_ub=scaled.A,b_ub=scaled.b,
        bounds=list(zip(scaled.lower,scaled.upper)),method="highs",options=options)
    if not original.success or not solved.success:
        raise AssertionError("artificial small LPs must return their known optima")
    reconstructed=scaled.to_original(solved.x)
    expected=radius*np.array([.2,-.3,0.,.2,.3,0.])
    row_factors=np.exp2(np.arange(len(b))*8-40)
    heterogeneous=scale_correction_lp(A*row_factors[:,None],b*row_factors,lo,hi,radius)
    other=linprog(heterogeneous.objective,A_ub=heterogeneous.A,b_ub=heterogeneous.b,
        bounds=list(zip(heterogeneous.lower,heterogeneous.upper)),method="highs",options=options)
    if not other.success:raise AssertionError("rescaled artificial affine rows retain the known optimum")
    residuals=scaled.original_residuals(solved.x)
    dual=scaled.original_dual_diagnostics(solved,np.arange(len(b))%3)

    # A small *scaled* residual need not meet the existing original-unit gate.
    huge=np.array([[2.**40,0.]])
    huge_lp=scale_correction_lp(huge,np.zeros(1),np.array([-radius,0.]),
        np.array([radius,radius]),radius)
    misleading=huge_lp.original_residuals(np.array([1e-10,1e-10]))
    rejects={}
    for label,callback in {
        "zero-radius":lambda:scale_correction_lp(A,b,lo,hi,0.),
        "negative-radius":lambda:scale_correction_lp(A,b,lo,hi,-radius),
        "wrong-auxiliary-upper-bound":lambda:scale_correction_lp(A,b,lo,np.r_[hi[:n],hi[n:]*2],radius),
        "nonfinite":lambda:scale_correction_lp(A*np.inf,b,lo,hi,radius),
    }.items():
        try:
            with np.errstate(invalid="ignore"):callback()
        except (ValueError,FloatingPointError):rejects[label]=True
        else:rejects[label]=False
    from types import SimpleNamespace
    unavailable_dual={name:scaled.original_dual_diagnostics(SimpleNamespace(x=value))
        for name,value in [('missing',None),('nan',np.full(2*n,np.nan)),
            ('infinite',np.full(2*n,np.inf)),('wrong-shape',np.zeros(2*n+1))]}
    checks={
        "inputs_not_mutated":all(np.array_equal(x,y) for x,y in zip((A,b,lo,hi),copies)),
        "positive_power_of_two_row_divisors":bool(np.all(scaled.row_divisors>0)
            and np.array_equal(np.ldexp(np.ones(len(b)),scaled.row_binary_exponents),scaled.row_divisors)),
        "full_variable_and_all_affine_row_mapping":mapping_error<2e-15 and back_error<2e-15,
        "known_original_and_scaled_optimum":float(np.max(abs(original.x-expected)))<1e-12
            and float(np.max(abs(reconstructed-expected)))<1e-12,
        "positive_objective_scale":abs(original.fun-radius*solved.fun)<1e-12,
        "heterogeneous_row_units_do_not_change_artificial_primal":
            float(np.max(abs(heterogeneous.to_original(other.x)-expected)))<1e-12,
        "original_unit_postsolve_residuals_preserved":
            residuals["maximum_original_linear_row_violation"]<1e-12,
        "same_solver_dual_maps_to_original_units":dual["available"]
            and abs(dual["original_primal_minus_dual"])<1e-12
            and dual["maximum_original_stationarity_residual"]<1e-12
            and dual["maximum_original_complementarity_product"]<1e-12
            and dual["dual_sign_violation"]<1e-12,
        "tiny_scaled_residual_not_misreported_as_original_gate_pass":
            misleading["maximum_scaled_linear_row_violation"]<1e-9
            and misleading["maximum_original_linear_row_violation"]>1e-7,
        "invalid_scalings_rejected":all(rejects.values()),
        "missing_nonfinite_and_wrong_shape_primal_only_disable_dual_diagnostics":
            all(d.get('available') is False for d in unavailable_dual.values()),
        "artificial_only_no_research_state_loaded_or_evaluated":True,
    }
    result={"schema":POLICY+"-artificial-check","passed":all(checks.values()),
        "checks":checks,"rejections":rejects,
        "maximum_affine_row_mapping_difference":mapping_error,
        "maximum_variable_roundtrip_difference":back_error,
        "known_original_optimum":float(original.fun),
        "known_scaled_optimum":float(solved.fun),
        "original_residuals_at_scaled_optimum":residuals,
        "original_dual_diagnostics_at_scaled_optimum":dual,
        "unavailable_primal_dual_diagnostics":unavailable_dual,
        "deliberately_misleading_scaled_residual":misleading,
        "new_LP_representation_only_not_a_geometry_or_performance_certificate":True,
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "definition":scaled.definition()}
    if not result["passed"]:raise AssertionError(json.dumps(result,indent=2))
    return result


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only",action="store_true",required=True)
    parser.add_argument("--out",type=Path)
    args=parser.parse_args(argv)
    result=developer_check()
    raw=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(raw,encoding="utf-8")
    print(raw,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())

