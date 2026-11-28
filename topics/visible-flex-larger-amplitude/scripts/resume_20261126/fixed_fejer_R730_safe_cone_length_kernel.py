#!/usr/bin/env python3
"""Complete R730 single-wide-pulse length root and inverse-arclength kernel.

Exact law: six-control Bezier B=(b,z), G=((1-xi*psi)b,z),
psi=(1-(2*t-1)^12)^7, L(xi)=S, F(s)=G(t(s)), l(t(s))=s.
The explicit construction is eta=1/32, xi_max=3/4. Both whole-angle
length inequalities are proved in R730 for the complete fixed input.

This file implements working quadrature, roots and all two-angle chains.
Those working errors are not certified. All numerical calls require public
Actions. No old chord/Slerp mean, profile root or normal root is inherited.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np

SCHEMA = "complete-R730-safe-cone-length-and-inverse-arclength-working-kernel-v1"
DEFINITION_SCHEMA = "R730-global-single-pulse-contracted-Bezier-physical-definition-v1"
HANDLE_LENGTH = "1/32"
MAXIMUM_CONTRACTION = "3/4"
PULSE_FLATNESS = 6


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("R730 scientific evaluation requires public repository Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def array_record(value):
    a=np.ascontiguousarray(value);h=hashlib.sha256(str(a.dtype).encode())
    h.update(json.dumps(list(a.shape)).encode());h.update(a.tobytes())
    return dict(shape=list(a.shape),dtype=str(a.dtype),sha256=h.hexdigest())


def positive_integer(value,name):
    if isinstance(value,(bool,np.bool_)) or int(value)!=value or int(value)<1:
        raise ValueError(name+" must be an explicit positive integer")
    return int(value)


@dataclass(frozen=True)
class LengthParameters:
    handle_length: str = HANDLE_LENGTH
    maximum_contraction: str = MAXIMUM_CONTRACTION
    pulse_flatness: int = PULSE_FLATNESS
    radial_quadrature_order: int = 8
    profile_quadrature_order: int = 16
    mean_maxiter: int = 128
    mean_tolerance: float = 2.e-12
    scalar_iterations: int = 64
    mean_backtracks: int = 24
    mean_armijo: float = 1.e-4

    def definitions(self):
        if (self.handle_length!=HANDLE_LENGTH
                or self.maximum_contraction!=MAXIMUM_CONTRACTION
                or type(self.pulse_flatness) is not int
                or self.pulse_flatness!=PULSE_FLATNESS):
            raise ValueError("This source fixes eta=1/32, xi_max=3/4 and one wide pulse k=6")
        ints={name:positive_integer(getattr(self,name),name) for name in (
            "radial_quadrature_order","profile_quadrature_order","mean_maxiter",
            "scalar_iterations","mean_backtracks")}
        if min(ints["radial_quadrature_order"],ints["profile_quadrature_order"])<4:
            raise ValueError("Use complete positive quadrature orders at least four")
        tolerance,armijo=float(self.mean_tolerance),float(self.mean_armijo)
        if not math.isfinite(tolerance) or tolerance<=0:
            raise ValueError("Use the complete positive physical root tolerance")
        if not math.isfinite(armijo) or not 0<armijo<1:
            raise ValueError("Use the complete Armijo coefficient in (0,1)")
        return F(HANDLE_LENGTH),F(MAXIMUM_CONTRACTION),ints,tolerance,armijo


class LengthReferenceFailure(RuntimeError):
    def __init__(self,message,record):
        super().__init__(message);self.record=record


def physical_definition(parameters):
    """Whole exact mathematical recipe; no field/root/quadrature evaluation."""
    if type(parameters) is not LengthParameters:
        raise ValueError("Use this exact complete LengthParameters source")
    eta,maximum,ints,tolerance,armijo=parameters.definitions()
    return dict(schema=DEFINITION_SCHEMA,proof_result="R730",
        exact_handle_length=str(eta),exact_maximum_contraction=str(maximum),
        pulse_flatness=PULSE_FLATNESS,pulse="(1-(2*t-1)^12)^7",
        pulse_is_one_global_polynomial=True,polynomial_degree=84,
        internal_formula_cuts=[],endpoint_vanishing_derivatives=list(range(7)),
        controls=["Gamma","Gamma+eta*ez",
            "Gamma+2*eta*ez+(5/4)*kappa0*eta^2*er(Theta)",
            "(R+2*eta)*er(Theta)+H0*ez","(R+eta)*er(Theta)+H0*ez","R*er(Theta)+H0*ez"],
        baseline="sum_{j=0}^5 binom(5,j)t^j(1-t)^(5-j)P_j",
        z_depends_on_phi=False,
        contracted_curve="G_xi=((1-xi*psi)*baseline_xy,baseline_z)",
        accurate_length_equation="integral_0^1 |d_t G_xi| dt = S",
        accurate_root_range="0 < xi(phi) < 3/4",
        accurate_inverse_equation="integral_0^t |d_u G_xi(phi)| du = s",
        accurate_field="F(s,phi)=G_xi(phi)(t(s,phi),phi)",
        accurate_unit_reference="T0=F_s",
        complete_domain="all s in [0,S] and every original fixed-chart angle",
        original_fixed_scalar_chart_and_target_unchanged=True,
        old_support_complement_boundary_width_and_profile_delta_used=False,
        old_R709_R722_R726_R727_mean_or_branch_certificate_inherited=False,
        working_full_cell_rule="all original normalized material mesh cells; full positive Gauss",
        working_order=max(ints["radial_quadrature_order"],ints["profile_quadrature_order"]),
        declared_original_orders={n:ints[n] for n in (
            "radial_quadrature_order","profile_quadrature_order")},
        working_inverse_rule=(
            "full positive prefix table and same positive Gauss rule on each required "
            "partial cell; target (s/S)*actual_total_length"),
        working_angle_chain=(
            "two implicit length-root jets and two inverse-arclength jets of the "
            "accurate expressions, evaluated with complete working quadratures"),
        complete_root_budgets={n:ints[n] for n in (
            "mean_maxiter","scalar_iterations","mean_backtracks")},
        root_tolerance_hex=tolerance.hex(),armijo_hex=armijo.hex(),
        working_partial_integral_monotonicity_or_exact_discrete_derivatives_claimed=False,
        quadrature_root_inverse_trigonometry_and_rounding_errors_enclosed=False,
        original_outer_whole_cell_integration_and_normal32_are_separate=True)


def _finite(name,*values):
    if any(not np.isfinite(v).all() for v in values):
        raise LengthReferenceFailure("Nonfinite complete R730 "+name,
            dict(schema=SCHEMA,complete=False,phase=name,
                 reason="A required complete working array is nonfinite"))


def baseline_jets(controls,t):
    """All t derivatives 0..3 and phi derivatives 0..2 of six complete controls."""
    controls,t=np.asarray(controls,dtype=float),np.asarray(t,dtype=float)
    if (controls.shape!=(3,6,3) or t.ndim!=1 or not len(t)
            or not np.isfinite(controls).all() or not np.isfinite(t).all()
            or np.any(t<0.) or np.any(t>1.)):
        raise ValueError("Use all six controls, both angular jets and complete t rows")
    out=np.empty((4,3,len(t),3),dtype=float)
    for r in range(4):
        d=np.diff(controls,n=r,axis=1)*(math.factorial(5)//math.factorial(5-r))
        degree=5-r
        basis=np.column_stack([math.comb(degree,j)*t**j*(1.-t)**(degree-j)
                               for j in range(degree+1)])
        for q in range(3):out[r,q]=basis@d[q]
    _finite("baseline_jets",out)
    return out


def pulse_jets(t):
    """Complete fixed polynomial and its first three t derivatives."""
    t=np.asarray(t,dtype=float)
    if t.ndim!=1 or not len(t) or not np.isfinite(t).all() or np.any(t<0.) or np.any(t>1.):
        raise ValueError("Use every requested normalized coordinate in [0,1]")
    x=2.*t-1.
    A=1.-x**12;A1=-12.*x**11;A2=-132.*x**10;A3=-1320.*x**9
    out=np.stack((A**7,14.*A**6*A1,
        4.*(42.*A**5*A1*A1+7.*A**6*A2),
        8.*(210.*A**4*A1**3+126.*A**5*A1*A2+7.*A**6*A3)))
    _finite("pulse_jets",out)
    return out


def geometry_jets(controls,t,xi,xi_phi,xi_phiphi):
    """G_{t^r phi^j}; r=0..3,j=0..2, including all xi angular chain terms."""
    roots=np.asarray((xi,xi_phi,xi_phiphi),dtype=float)
    _finite("root_angle_jets",roots)
    B=baseline_jets(controls,t);p=pulse_jets(t)
    multiplier=-p[:,None,:]*roots[None,:,None];multiplier[0,0]+=1.
    out=np.zeros_like(B)
    for r in range(4):
        for q in range(3):
            for j in range(r+1):
                for h in range(q+1):
                    out[r,q,:,:2]+=(math.comb(r,j)*math.comb(q,h)
                        *multiplier[j,h,:,None]*B[r-j,q-h,:,:2])
            out[r,q,:,2]=B[r,q,:,2]
    _finite("complete_geometry_jets",out)
    return out


def length_samples(controls,t,xi):
    """L,L_xi,L_xixi,L_phi,L_xiphi,L_phiphi integrands at fixed xi."""
    B=baseline_jets(controls,t);p=pulse_jets(t)
    V=B[1].copy();X=np.zeros_like(V)
    for q in range(3):
        X[q,:,:2]=-(p[0,:,None]*B[1,q,:,:2]+p[1,:,None]*B[0,q,:,:2])
        V[q]+=xi*X[q]
    v=np.linalg.norm(V[0],axis=-1)
    if not np.isfinite(v).all() or np.any(v<=0):
        raise LengthReferenceFailure("A complete length speed is not positive",
            dict(schema=SCHEMA,complete=False,phase="length_speed"))
    n=V[0]/v[:,None]
    lx=np.sum(n*X[0],axis=-1);lp=np.sum(n*V[1],axis=-1)
    lxx=(np.sum(X[0]*X[0],axis=-1)-lx*lx)/v
    lxp=(np.sum(X[0]*V[1],axis=-1)-lx*lp)/v+np.sum(n*X[1],axis=-1)
    lpp=(np.sum(V[1]*V[1],axis=-1)-lp*lp)/v+np.sum(n*V[2],axis=-1)
    out=np.column_stack((v,lx,lxx,lp,lxp,lpp))
    _finite("complete_length_samples",out)
    return out


def total_density_jets(controls,t,root):
    G=geometry_jets(controls,t,root["xi"],root["xi_phi"],root["xi_phiphi"])
    V,Vp,Vpp=G[1]
    v=np.linalg.norm(V,axis=-1)
    if np.any(v<=0.) or not np.isfinite(v).all():
        raise LengthReferenceFailure("A complete actual R730 speed is not positive",
            dict(schema=SCHEMA,complete=False,phase="actual_speed"))
    n=V/v[:,None];vp=np.sum(n*Vp,axis=-1)
    vpp=np.sum(n*Vpp,axis=-1)+(np.sum(Vp*Vp,axis=-1)-vp*vp)/v
    out=np.column_stack((v,vp,vpp));_finite("total_density_jets",out)
    return out


class CompleteLengthRule:
    """All cells, positive full quadrature, one immutable root state per angle."""

    def __init__(self,normalized_nodes,physical_S,parameters):
        require_actions()
        if type(parameters) is not LengthParameters:
            raise ValueError("Use this complete length-parameter type")
        eta,maximum,ints,tolerance,armijo=parameters.definitions()
        nodes=np.asarray(normalized_nodes,dtype=float);S=float(physical_S)
        if (nodes.ndim!=1 or len(nodes)<2 or nodes[0]!=0. or nodes[-1]!=1.
                or not np.isfinite(nodes).all() or np.any(np.diff(nodes)<=0.)
                or not math.isfinite(S) or S<=0.):
            raise ValueError("Keep the full increasing original normalized mesh and physical S")
        self.nodes=np.array(nodes,copy=True);self.nodes.setflags(write=False)
        self.S,self.parameters,self.maximum=S,parameters,float(maximum)
        self.ints,self.tolerance,self.armijo=ints,tolerance,armijo
        self.order=max(ints["radial_quadrature_order"],ints["profile_quadrature_order"])
        x,w=np.polynomial.legendre.leggauss(self.order)
        self.u,self.w=(x+1.)/2.,w/2.
        if not np.isfinite(self.w).all() or np.any(self.w<=0.):
            raise ArithmeticError("Every complete R730 Gauss weight must remain positive")
        width=np.diff(nodes);self.cell_widths=width
        self.points=(nodes[:-1,None]+width[:,None]*self.u[None]).reshape(-1)
        self.weights=(width[:,None]*self.w[None]).reshape(-1)
        for a in (self.u,self.w,self.points,self.weights,self.cell_widths):a.setflags(write=False)
        self.counts=dict(length_residual_integrals=0,length_jet_integrals=0,
            length_root_iterations=0,length_backtracks=0,inverse_batches=0,
            inverse_iterations=0,partial_integrals=0,completed_angle_states=0)
        self.maximum_working_length_residual=0.
        self.maximum_working_inverse_residual=0.

    def integral(self,controls,xi,jets=False):
        self.counts["length_jet_integrals" if jets else "length_residual_integrals"]+=1
        values=length_samples(controls,self.points,xi)
        out=np.sum(self.weights[:,None]*values,axis=0)
        _finite("length_integral",out)
        return out if jets else float(out[0])

    def solve(self,controls,*,angle_hex):
        require_actions()
        controls=np.array(controls,dtype=float,copy=True)
        f0=self.integral(controls,0.)-self.S
        f1=self.integral(controls,self.maximum)-self.S
        if not f0<0.<f1:
            raise LengthReferenceFailure("The complete working length rule lacks its positive bracket",
                dict(schema=SCHEMA,complete=False,phase="length_bracket",angle_hex=angle_hex,
                    left_residual=f0,right_residual=f1,left_xi_hex=0.0.hex(),
                    right_xi_hex=self.maximum.hex(),full_rule=self.metadata(),
                    continuous_existence_or_failure_claimed=False))
        lo,hi=0.,self.maximum;xi=self.maximum*(-f0)/(f1-f0)
        if not lo<xi<hi:xi=(lo+hi)/2.
        history=[];converged=False
        for iteration in range(self.ints["mean_maxiter"]):
            self.counts["length_root_iterations"]+=1
            values=self.integral(controls,xi,jets=True);residual=float(values[0]-self.S)
            history.append(dict(iteration=iteration,xi_hex=xi.hex(),
                residual=residual,length_xi=float(values[1])))
            if abs(residual)<=self.tolerance and values[1]>0.:
                converged=True;break
            if residual<0.:lo=xi
            else:hi=xi
            direction=-residual/float(values[1]) if values[1]>0. else float("nan")
            candidate=xi+direction;accepted=False
            if math.isfinite(candidate) and lo<candidate<hi:
                for backtrack in range(self.ints["mean_backtracks"]):
                    self.counts["length_backtracks"]+=1
                    alpha=2.**(-backtrack);trial=xi+alpha*direction
                    if not lo<trial<hi:continue
                    trial_residual=self.integral(controls,trial)-self.S
                    if abs(trial_residual)<=(1.-self.armijo*alpha)*abs(residual):
                        candidate=trial;accepted=True;break
            if not accepted:candidate=(lo+hi)/2.
            if candidate==xi:
                raise LengthReferenceFailure("The complete scalar length iteration stagnated",
                    dict(schema=SCHEMA,complete=False,phase="length_stagnation",
                        angle_hex=angle_hex,complete_history=history,
                        lo_hex=lo.hex(),hi_hex=hi.hex(),continuous_root_claimed=False))
            xi=float(candidate)
        if not converged:
            raise LengthReferenceFailure("The full scalar length-root budget was exhausted",
                dict(schema=SCHEMA,complete=False,phase="length_budget",angle_hex=angle_hex,
                    complete_history=history,lo_hex=lo.hex(),hi_hex=hi.hex(),
                    continuous_root_claimed=False))
        lx=float(values[1]);xp=-float(values[3])/lx
        xpp=-float(values[5]+2.*values[4]*xp+values[2]*xp*xp)/lx
        _finite("two_root_angle_jets",np.array((xi,xp,xpp,lx)))
        root=dict(xi=float(xi),xi_phi=xp,xi_phiphi=xpp,
            physical_S_hex=self.S.hex(),working_total_length=float(values[0]),
            complete_fixed_xi_length_jets=[float(v) for v in values],
            full_root_history=history,working_left_residual=f0,working_right_residual=f1,
            working_current_bracket=[lo,hi],literal_angle_hex=angle_hex,
            accurate_R730_root_and_inverse_bound_certified=False)
        density=total_density_jets(controls,self.points,root)
        pieces=np.sum(density.reshape(len(self.nodes)-1,self.order,3)
            *self.weights.reshape(len(self.nodes)-1,self.order,1),axis=1)
        prefix=np.vstack((np.zeros((1,3)),np.cumsum(pieces,axis=0)))
        if np.any(np.diff(prefix[:,0])<=0.) or not np.isfinite(prefix).all():
            raise LengthReferenceFailure("Complete prefix lengths are not strictly increasing",
                dict(schema=SCHEMA,complete=False,phase="prefix_lengths",angle_hex=angle_hex))
        root["actual_total_length_and_two_angle_jets"]=[float(v) for v in prefix[-1]]
        root["full_prefix_record"]=array_record(prefix)
        root["full_density_record"]=array_record(density)
        root["root_identity_sha256"]=canonical(root)
        controls.setflags(write=False);prefix.setflags(write=False)
        self.maximum_working_length_residual=max(self.maximum_working_length_residual,abs(residual))
        self.counts["completed_angle_states"]+=1
        return dict(root=root,controls=controls,prefix=prefix)

    def partial(self,state,t):
        t=np.asarray(t,dtype=float)
        if (t.ndim!=1 or not len(t) or not np.isfinite(t).all()
                or np.any(t<0.) or np.any(t>1.)):
            raise ValueError("Keep complete finite inverse-coordinate queries")
        cell=np.minimum(len(self.nodes)-2,np.maximum(0,np.searchsorted(self.nodes,t,side="right")-1))
        left=self.nodes[cell];width=t-left
        points=(left[:,None]+width[:,None]*self.u[None]).reshape(-1)
        density=total_density_jets(state["controls"],points,state["root"])
        out=state["prefix"][cell]+width[:,None]*np.sum(
            density.reshape(len(t),self.order,3)*self.w[None,:,None],axis=1)
        out[t==0.]=0.;out[t==1.]=state["prefix"][-1]
        self.counts["partial_integrals"]+=len(t);_finite("partial_length_jets",out)
        return out

    def evaluate_tangents(self,state,physical_s):
        require_actions()
        s=np.asarray(physical_s,dtype=float)
        if (s.ndim!=1 or not len(s) or not np.isfinite(s).all()
                or np.any(s<0.) or np.any(s>self.S)):
            raise ValueError("Retain every original physical material row in [0,S]")
        self.counts["inverse_batches"]+=1
        total=state["prefix"][-1];alpha=s/self.S;target=alpha*total[0]
        edge0=s==0.;edge1=s==self.S
        cell=np.minimum(len(self.nodes)-2,np.maximum(0,
            np.searchsorted(state["prefix"][:,0],target,side="right")-1))
        lo=self.nodes[cell].copy();hi=self.nodes[cell+1].copy()
        fraction=(target-state["prefix"][cell,0])/(state["prefix"][cell+1,0]-state["prefix"][cell,0])
        t=lo+(hi-lo)*fraction;t[edge0]=0.;t[edge1]=1.
        complete=edge0|edge1;residual=np.zeros_like(t)
        for iteration in range(self.ints["scalar_iterations"]):
            indices=np.flatnonzero(~complete)
            if not len(indices):break
            self.counts["inverse_iterations"]+=1
            at=self.partial(state,t[indices]);f=at[:,0]-target[indices]
            residual[indices]=f;done=np.abs(f)<=self.tolerance
            complete[indices[done]]=True
            active=indices[~done]
            if not len(active):continue
            fa=f[~done];lower=fa<0.
            lo[active[lower]]=t[active[lower]];hi[active[~lower]]=t[active[~lower]]
            G=geometry_jets(state["controls"],t[active],state["root"]["xi"],
                state["root"]["xi_phi"],state["root"]["xi_phiphi"])
            v=np.linalg.norm(G[1,0],axis=-1)
            if np.any(v<=0.) or not np.isfinite(v).all():
                raise LengthReferenceFailure("A required inverse speed is not positive",
                    dict(schema=SCHEMA,complete=False,phase="inverse_speed",
                        literal_angle_hex=state["root"]["literal_angle_hex"]))
            new=t[active]-fa/v
            good=np.isfinite(new)&(new>lo[active])&(new<hi[active])
            new=np.where(good,new,(lo[active]+hi[active])/2.)
            if np.any(new==t[active]):
                raise LengthReferenceFailure("A complete inverse query stagnated",
                    dict(schema=SCHEMA,complete=False,phase="inverse_stagnation",
                        literal_angle_hex=state["root"]["literal_angle_hex"],
                        remaining_rows=active.tolist(),remaining_residuals=fa.tolist()))
            t[active]=new
        if not np.all(complete):
            raise LengthReferenceFailure("The full inverse-arclength budget was exhausted",
                dict(schema=SCHEMA,complete=False,phase="inverse_budget",
                    literal_angle_hex=state["root"]["literal_angle_hex"],
                    remaining_rows=np.flatnonzero(~complete).tolist(),
                    remaining_residuals=residual[~complete].tolist(),accurate_inverse_certified=False))
        ell=self.partial(state,t)
        G=geometry_jets(state["controls"],t,state["root"]["xi"],
            state["root"]["xi_phi"],state["root"]["xi_phiphi"])
        V=G[1,0];v=np.linalg.norm(V,axis=-1)
        if np.any(v<=0.) or not np.isfinite(v).all():
            raise LengthReferenceFailure("A final inverse speed is not positive",
                dict(schema=SCHEMA,complete=False,phase="inverse_final_speed"))
        T=V/v[:,None];vt=np.sum(T*G[2,0],axis=-1);vp=np.sum(T*G[1,1],axis=-1)
        tp=(alpha*total[1]-ell[:,1])/v
        tpp=(alpha*total[2]-ell[:,2]-2.*vp*tp-vt*tp*tp)/v
        W1=G[1,1]+G[2,0]*tp[:,None]
        W2=G[1,2]+2.*G[2,1]*tp[:,None]+G[3,0]*(tp*tp)[:,None]+G[2,0]*tpp[:,None]
        v1=np.sum(T*W1,axis=-1)
        v2=np.sum(T*W2,axis=-1)+(np.sum(W1*W1,axis=-1)-v1*v1)/v
        Tp=(W1-T*v1[:,None])/v[:,None]
        Tpp=(W2/v[:,None]-2.*W1*(v1/v**2)[:,None]
            -T*(v2/v)[:,None]+2.*T*(v1*v1/v**2)[:,None])
        unit_t=(G[2,0]-T*vt[:,None])/v[:,None]
        Ts=unit_t*(total[0]/(self.S*v))[:,None]
        result=dict(T0=T,T0_s=Ts,T0_phi=Tp,T0_phiphi=Tpp,
            actual_inverse_t=t,actual_inverse_phi=tp,actual_inverse_phiphi=tpp,
            actual_inverse_residual=ell[:,0]-target,
            working_total_length_normalization=float(total[0]/self.S))
        for name,value in result.items():
            if isinstance(value,np.ndarray):
                _finite("complete_"+name,value);value.setflags(write=False)
        self.maximum_working_inverse_residual=max(self.maximum_working_inverse_residual,
            float(np.max(np.abs(result["actual_inverse_residual"]))))
        return result

    def metadata(self):
        return dict(schema=SCHEMA,source_sha256=sha(__file__),
            physical_definition=physical_definition(self.parameters),
            full_node_count=len(self.nodes),full_cell_count=len(self.nodes)-1,
            quadrature_order=self.order,full_quadrature_point_count=len(self.points),
            all_original_cells_retained=True,normalized_node_record=array_record(self.nodes),
            physical_S_carrier_hex=self.S.hex(),positive_weight_record=array_record(self.weights),
            counts=dict(self.counts),maximum_working_length_residual=self.maximum_working_length_residual,
            maximum_working_inverse_residual=self.maximum_working_inverse_residual,
            continuous_root_and_inverse_errors_enclosed=False,
            complete_normal_or_geometry_certificate_inherited=False)
