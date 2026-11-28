"""Current physical four-end map on R654's released material pieces.

Use the original fixed normalized grid: t=(L*x-S)/D is a Jet at each
original quadrature/observation point. All moving-time and nonlocal costs
then pass through the same physical shape and the same prefix integrals.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
import time

import numpy as np

import r632_true_hermite_kinetic_chart as original
from r654_released_rest_physical_base import PhysicalBase, derivative

LD, Jet, paid = original.LD, original.Jet, original.paid


class FourEndPending(RuntimeError):
    def __init__(self,record):
        super().__init__("The current four-end or sufficient physical qualification is unfinished")
        self.record=record


def number(value):
    value=F(value)
    return LD(str(value.numerator))/LD(str(value.denominator))


def polynomial_jet(coefficients,t):
    val=np.polynomial.polynomial.polyval(t.value,coefficients[0])
    first=np.polynomial.polynomial.polyval(t.value,coefficients[1])
    return Jet(val,first*t.derivative)


def coefficients(p):
    arrays=[]
    for _ in range(4):
        arrays.append(np.asarray([number(x) for x in p],dtype=LD))
        p=derivative(p)
    return arrays


class ReleasedChart:
    def __init__(self,parameters_exact,epsilon,grid,clock):
        original.reduced.require_public_science()
        self.base=PhysicalBase(parameters_exact,epsilon)
        self.grid,self.clock=grid,clock
        self.polys=[(coefficients(p.h),coefficients(p.k)) for p in self.base.pieces]
        self.counts=Counter()
        self.progress={}
        self.knots=np.linspace(0.,1.,65)
        x=np.asarray(grid.x,dtype=LD)[:,None]
        h_index=np.arange(129,dtype=LD)
        k_index=np.arange(127,dtype=LD)
        pi=np.arccos(LD(-1))
        hf=pi*h_index
        kf=pi*(k_index+LD(".5"))
        hc,hs=np.cos(x*hf),np.sin(x*hf)
        ks,kc=np.sin(x*kf),np.cos(x*kf)
        hs[(grid.x==0)|(grid.x==1)]=0
        ks[grid.x==0]=0
        kc[grid.x==1]=0
        self.h_basis=[v/(1+h_index*h_index) for v in (hc,-hs*hf,-hc*hf**2)]
        self.k_basis=[v/(1+(2*k_index+1)**2) for v in (ks,kc*kf,-ks*kf**2)]

    def joint(self,q,tau,mode="full",fixed_center=None):
        """mode full: q and four times; controls: four current times; fixed: no chain."""
        self.clock.check("before_R654_current_four_end_map")
        started=time.monotonic()
        self.counts[mode+"_attempts"]+=1
        self.progress["current_map"]={"mode":mode,"shape":list(map(float,q)),"durations":list(map(float,tau))}
        try:
            return self._joint(q,tau,mode,fixed_center)
        finally:
            self.counts[mode+"_seconds_including_partial"]+=time.monotonic()-started

    def _joint(self,q,tau,mode,fixed_center):
        q,tau=np.asarray(q,float),np.asarray(tau,float)
        if (q.shape!=(256,) or tau.shape!=(4,) or not np.all(np.isfinite(q))
                or not np.all(np.isfinite(tau)) or np.any(tau<=0)):
            raise ValueError("Finite shapes and four strictly positive actual times are required")
        qualification=self.base.physical_enclosure(q,tau)
        self.progress["current_map"]["continuous_physical_qualification"]=qualification
        if not qualification["sufficient_bounds_closed"]:
            raise FourEndPending(self.progress)
        dimension={"full":260,"controls":4,"fixed":0}[mode]
        if fixed_center is not None and mode!="fixed":
            raise ValueError("Fixed-center fine needs the frozen physical curve")
        def constant(value):
            return Jet(value,np.zeros(dimension))
        durations=[]
        for p in self.base.pieces:
            if p.control is None:
                value=constant(number(p.duration))
            else:
                value=constant(tau[p.control])
                if mode!="fixed":
                    value.derivative[dimension-4+p.control]=1
            durations.append(value)
        starts=[constant(0)]
        for duration in durations:
            starts.append(starts[-1]+duration)
        length=starts[-1]
        cuts=np.asarray([v.value for v in starts[1:]],dtype=LD)
        h_fields=[arr @ q[:129].astype(LD) for arr in self.h_basis]
        k_fields=[arr @ q[129:].astype(LD) for arr in self.k_basis]
        raw=[]
        for i,x_value in enumerate(self.grid.x):
            x=LD(x_value)
            index=min(int(np.searchsorted(cuts,length.value*x,side="right")),len(durations)-1)
            D=durations[index]
            if x==0 or x==1:
                t=constant(x)
            else:
                t=(length*x-starts[index])/D
            h_coeff,k_coeff=self.polys[index]
            fields=[]
            for coeff,basis,values,offset,width in ((h_coeff,self.h_basis,h_fields,0,129),
                    (k_coeff,self.k_basis,k_fields,129,127)):
                for j in range(3):
                    perturb=constant(values[j][i])
                    if mode=="full":
                        perturb.derivative[offset:offset+width]=basis[j][i]
                    base=polynomial_jet(coeff[j:j+2],t)
                    fields.append(base/D**j+perturb/length**j)
            raw.append(fields)
        eta=self.grid.integrate([[length*r[4]/(2*r[0])] for r in raw])
        geometry=[[r[0],r[3],e[0],r[1],r[4]] for r,e in zip(raw,eta)]
        acceleration=[[r[2],r[5]] for r in raw]
        physical=original.physical_attainers(geometry,self.grid.x,length.value)
        physical["released_shape_continuous_original_field_enclosure"]=qualification
        physical["all_represented_shape_fields_in_original_box"]=True
        # These shapes are polynomial-plus-trigonometric. Keep the original
        # actual fields and give their own continuous certificate an explicit name.
        if not physical["all_sampled_original_physical_fields_in_box"]:
            raise FloatingPointError("A reconstructed physical sample leaves an original box")
        center=geometry[0]
        beta=acceleration[0][0]-center[0]*center[4]**2/4
        physical.update(physical_center_v=float(center[4].value),physical_center_beta=float(beta.value))
        if center[4].value>=0 or beta.value>=0:
            raise FloatingPointError("The selected nonzero negative R620 center branch is unavailable")
        primitive=self.grid.integrate([[length*v for v in paid.density(g)] for g in geometry])
        total=primitive[-1]
        if fixed_center is None:
            history=[[v-total[j] if j in original.original.ODD else v for j,v in enumerate(row)]
                     for row in primitive]
        else:
            history=[[v+constant(LD(fixed_center[j])) for j,v in enumerate(row)] for row in primitive]
        p,t,s,r=(history[-1][j] for j in (1,3,6,4))
        E=[8*t+2*p,p,4*s,8*r]
        H=center[0]
        observed=[total[1]/length,(8*total[3]+2*total[1])/length,
                  8*H**2*total[4]/length,4*H**2*total[6]/length]
        curve={"geometry":geometry,"acceleration":acceleration,"history":history,
            "total_integral":total,"length":length,"grid":self.grid,"knots":self.knots,
            "end":observed,"reduced_end":[p,t,s,r],"shape_parameters":q.copy(),
            "parameters":q.copy(),"four_rest_controls_binary64":tau.copy(),
            "physical_attainers":physical,"fixed_physical_centers":fixed_center is not None}
        self.counts[mode+"_completed"]+=1
        self.clock.check("after_R654_current_true_density_integrals")
        return curve,E

    def solve_controls(self,q,tau,*,target_tolerance=1.e-12,iterations=18,backtracks=16):
        """Solve all four actual current moments; never use the old stationary V."""
        tau=np.asarray(tau,float).copy()
        report=self.progress["control_solve"]={"shape":list(map(float,q)),"initial_times":tau.tolist(),
            "events":[],"state":"pending"}
        current=None
        for iteration in range(iterations+1):
            if current is None:
                current=self.joint(q,tau,"controls")
            _,rows=current
            value,jac=paid.values_and_jacobian(rows)
            error=float(np.max(np.abs(value)))
            report.update(current_times=tau.tolist(),current_rows=np.asarray(value,float).tolist(),
                          current_control_jacobian=np.asarray(jac,float).tolist(),iteration=iteration)
            if error<=target_tolerance:
                curve,full_rows=self.joint(q,tau,"full")
                end_value,J=paid.values_and_jacobian(full_rows)
                if np.max(np.abs(end_value))>target_tolerance:
                    raise FourEndPending(self.progress)
                J=np.asarray(J,float)
                # This is the full current four-by-four partial derivative,
                # including moving times, eta prefixes, velocities and length.
                try:
                    Dtaudq=np.linalg.solve(J[:,256:],-J[:,:256])
                except np.linalg.LinAlgError as error:
                    report.update(state="current_four_control_matrix_unresolved",exception=str(error))
                    raise FourEndPending(self.progress) from error
                if not np.all(np.isfinite(Dtaudq)):
                    raise FourEndPending(self.progress)
                def collapse(v):
                    return Jet(v.value,v.derivative[:256]+v.derivative[256:] @ Dtaudq)
                for field in ("geometry","acceleration","history"):
                    curve[field]=[[collapse(v) for v in row] for row in curve[field]]
                for field in ("total_integral","end","reduced_end"):
                    curve[field]=[collapse(v) for v in curve[field]]
                curve["length"]=collapse(curve["length"])
                curve["implicit_four_time_derivatives"]=Dtaudq
                report.update(state="actual_finite_grid_four_current_ends_closed",
                    full_current_control_jacobian=J[:,256:].tolist(),independent_shape_columns=256,
                    continuous_original_root_not_inferred_from_finite_quadrature=True)
                return curve,report
            if iteration==iterations:
                break
            J=np.asarray(jac,float)
            residual=np.asarray(value,float)
            try:
                direction=np.linalg.solve(J,-residual)
            except np.linalg.LinAlgError as error:
                report.update(state="current_four_control_matrix_unresolved",exception=str(error))
                raise FourEndPending(self.progress) from error
            old=float(residual @ residual/2)
            accepted=False
            for trial in range(backtracks):
                candidate=tau+(2.**-trial)*direction
                event={"iteration":iteration,"backtrack":trial,"candidate":candidate.tolist(),"accepted":False}
                report["events"].append(event)
                if not np.all(np.isfinite(candidate)) or np.any(candidate<=0):
                    event["reason"]="actual_nonpositive_or_nonfinite_duration"
                    continue
                try:
                    candidate_curve,candidate_rows=self.joint(q,candidate,"controls")
                except FourEndPending:
                    event.update(reason="unclosed_physical_candidate_preserved",
                                 physical_record=dict(self.progress["current_map"]))
                    continue
                except FloatingPointError as error:
                    event.update(reason="actual_original_domain",exception=str(error))
                    continue
                rv,_=paid.values_and_jacobian(candidate_rows)
                new=float(rv@rv/2)
                actual_slope=float(residual @ (J @ (candidate-tau)))
                event.update(cost=new,actual_delta_slope=actual_slope)
                if actual_slope<0 and new<old and new<=old+1.e-4*actual_slope:
                    tau,current,accepted=candidate,(candidate_curve,candidate_rows),True
                    event["accepted"]=True
                    break
            if not accepted:
                break
        raise FourEndPending(self.progress)


def original_absolute_gates(report,args):
    """Same original absolute tolerances, using the appropriate shape certificate."""
    geometry = report["physical_attainers"]
    return bool(report["actual_original_ruling_max"]<=args.ruling_tol
        and report["all_ten_true_terminal_max"]<=args.end_tol
        and report["original_feedback_formula_defect_max"]<=args.ode_tol
        and report["original_Hermite_Simpson_ODE_defect_max"]<=args.ode_tol
        and geometry["all_sampled_original_physical_fields_in_box"]
        and geometry["released_shape_continuous_original_field_enclosure"]["sufficient_bounds_closed"])
