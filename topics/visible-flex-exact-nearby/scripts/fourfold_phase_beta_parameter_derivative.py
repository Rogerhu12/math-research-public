#!/usr/bin/env python3
"""True first parameter derivatives of the exact infinite affine phase graph.

The scalar direction is formed before multiplying the original basis powers.
All nonlinear trigonometric, primitive, E and curvature derivatives are then
taken analytically. Infinite Fourier errors for the differentiated primitive
are paid separately, before using any coefficient of E_delta or K_delta.
This module does not yet assert a whole beta-prime integral bound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, acb_series, ctx
from fourfold_phase_beta_interval import (
    series_constant, series_array, series_real, array_derivative,
    series_derivative, vector_dot, polynomial_disk_bound,
    primitive_fourier_budget, add_real_cauchy_error, ball_record,
)
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget, provenance


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class ParameterDerivativeTarget(ParameterGermBulkTarget):
    """The same exact real family, together with its true physical-r derivative."""

    def parameter_input_budget(self, center, radial_radius, sigma, E_radius):
        base = self.analytic_input_budget(center, radial_radius, sigma, E_radius)
        old_cap, ctx.cap = ctx.cap, max(ctx.cap, 21)
        try:
            beta_d, gamma_d, radius_d, height_d = self.direction_scalars(acb(center), 1)
        finally:
            ctx.cap = old_cap
        Bd = sum((polynomial_disk_bound(beta_d[j], radial_radius)*(sigma*(j+1)).cosh()
                  for j in range(self.modes)), arb(0)).upper()
        Gd = sum((polynomial_disk_bound(gamma_d[j], radial_radius)*(sigma*(j+1)).cosh()
                  for j in range(self.modes)), arb(0)).upper()
        Ad = polynomial_disk_bound(radius_d, radial_radius)
        Zd = polynomial_disk_bound(height_d, radial_radius)
        # |a_delta T+a T_delta| <= (Ad+A(Bd+Gd))*exp(B+G).
        effective = (Ad+base["radius_bound"]*(Bd+Gd)).upper()
        errors, finite = primitive_fourier_budget(
            self.nodes, sigma, arb(0), radial_radius, effective, Zd, base["tangent_bound"])
        gap = radial_radius-E_radius
        e, ed = base["field_errors"][0]/gap, errors[0]/gap
        M, Md = base["finite_field_bounds"][0]/gap, finite[0]/gap
        # E_delta=2 <F_r . F_{r,delta}>; three components and both errors.
        Ed_error = (6*(M*ed+Md*e+e*ed)).upper()
        change = {
            "radial_radius": radial_radius, "E_radius": E_radius,
            "sigma_normalized_x": sigma, "beta_direction_bound": Bd,
            "gamma_direction_bound": Gd, "true_radius_direction_bound": Ad,
            "height_bound": Zd, "radius_bound": effective,
            "tangent_bound": base["tangent_bound"],
            "field_errors": errors, "finite_field_bounds": finite,
            "E_error": Ed_error,
            "E_full_bound": (6*(M+e)*(Md+ed)).upper(),
        }
        return base, change

    def _primitive_operator(self, tangent):
        """Exactly the same linear Fourier primitive and parity as BallTarget."""
        coefficient = self.fourier.fft(tangent)/self.nodes
        primitive = series_array((self.nodes, 3))
        for k, n in enumerate(self.frequency):
            primitive[k, 0] = (acb(0,n)*coefficient[k,0]+coefficient[k,1])/(1-n*n)
            primitive[k, 1] = (-coefficient[k,0]+acb(0,n)*coefficient[k,1])/(1-n*n)
            if n:
                primitive[k, 2] = coefficient[k,2]/acb(0,n)
        for j in range(3):
            primitive[self.nodes//2,j] = series_constant(0)
        primitive[0,1], primitive[0,2] = series_constant(0), series_constant(0)
        for k in range(1,self.nodes//2):
            for j, parity in enumerate((1,-1,1)):
                value = (primitive[k,j]+parity*primitive[-k,j])/2
                primitive[k,j], primitive[-k,j] = value, parity*value
        return primitive

    def primitive_parameter(self, center, direction):
        beta, gamma, radius, height = self.scalars(center,direction)
        bd, gd, ad, zd = self.direction_scalars(center,direction)
        tangent, change = series_array((self.nodes,3)), series_array((self.nodes,3))
        for k in range(self.nodes):
            b = sum((beta[j]*self.sines[j,k] for j in range(self.modes)),series_constant(0))
            g = sum((gamma[j]*self.sines[j,k] for j in range(self.modes)),series_constant(0))
            b1 = sum((bd[j]*self.sines[j,k] for j in range(self.modes)),series_constant(0))
            g1 = sum((gd[j]*self.sines[j,k] for j in range(self.modes)),series_constant(0))
            sb,cb,sg,cg = b.sin(),b.cos(),g.sin(),g.cos()
            tangent[k] = [-cg*sb,cg*cb,sg]
            change[k] = [sg*g1*sb-cg*cb*b1,
                         -sg*g1*cb-cg*sb*b1,cg*g1]
        primitive, derivative = self._primitive_operator(tangent), self._primitive_operator(change)
        output, output_d = series_array(primitive.shape), series_array(primitive.shape)
        for key in np.ndindex(primitive.shape):
            output[key] = radius*primitive[key]
            output_d[key] = ad*primitive[key]+radius*derivative[key]
        output[0,2] += height
        output_d[0,2] += zd
        return output, output_d, radius, ad

    def parameter_target(self, center, scale, budgets):
        if acb(center).imag != 0:
            raise ValueError("real physical center required by the real-coefficient E projection")
        base, change = budgets
        F,Fd,a,ad = self.primitive_parameter(center,-scale)
        X,Xd = array_derivative(F,-scale),array_derivative(Fd,-scale)
        Ef = sum((vector_dot(X[k],X[(-k)%self.nodes]) for k in range(self.nodes)),series_constant(0))
        Edf = 2*sum((vector_dot(X[k],Xd[(-k)%self.nodes]) for k in range(self.nodes)),series_constant(0))
        E = add_real_cauchy_error(series_real(Ef),base["E_error"],scale,base["E_radius"])
        Ed = add_real_cauchy_error(series_real(Edf),change["E_error"],scale,change["E_radius"])
        ar,arr = series_derivative(a,-scale),series_derivative(a,-scale,2)
        adr,adrr = series_derivative(ad,-scale),series_derivative(ad,-scale,2)
        Er,Edr = series_derivative(E,-scale),series_derivative(Ed,-scale)
        C = ar*Er-2*arr*E
        Cd = adr*Er+ar*Edr-2*adrr*E-2*arr*Ed
        K = C/(2*a*E**2)
        Kd = Cd/(2*a*E**2)-K*(ad/a+2*Ed/E)
        return dict(F=F,Fd=Fd,a=a,ad=ad,E=E,Ed=Ed,C=C,Cd=Cd,K=K,Kd=Kd,
                    Efinite=Ef,Edfinite=Edf)


def record_budget(data):
    return {key:([ball_record(x) for x in value] if isinstance(value,list) else ball_record(value))
            for key,value in data.items()}


def run_root(args):
    started=time.monotonic()
    ctx.prec,ctx.cap=args.bits,args.precision
    box=json.loads(args.root_box_report.read_text())
    germ_source=Path(__file__).with_name("fourfold_phase_beta_parameter_germ.py")
    if (box.get("kind")!="uniform_affine_germ_Arb_root" or not box.get("proved")
            or box["source_sha256"]!=sha(germ_source)
            or box["center_object_sha256"]!=sha(args.center_object)):
        raise ValueError("root box does not identify the same exact family and germ source")
    for name,digest in box["dependency_sha256"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("root-box dependency changed: "+name)
    target=ParameterDerivativeTarget(args.center_object,Fraction(box["exact_parameter_half_width"]),
        args.quarter_nodes,args.quarter_nodes,arb(".003"),arb(".0025"),arb(".32"))
    identity=provenance(target,args.center_object)
    for key in ("origin_inputs_sha256","direction_sha256","exact_center_parameter",
                "exact_parameter_half_width","exact_parameter_interval"):
        if identity[key]!=box[key]:
            raise ValueError("parameter identity mismatch: "+key)
    root=stored_ball(box["root"])
    knots={Fraction.from_float(float(v)) for key,values in target.frozen.items()
           if key.endswith("_knots") for v in values}
    knots|={-x for x in knots}
    cells=[(a,b) for a,b in zip(sorted(knots),sorted(knots)[1:])
           if exact_arb(a)<root.lower() and root.upper()<exact_arb(b)]
    if len(cells)!=1:
        raise ValueError("uniform positive root is not inside one exact common scalar span")
    target.set_cell(*cells[0])
    R0,RE,sigma,scale=arb(".003"),arb(".0025"),arb(".32"),exact_arb(Fraction(1,4096))
    budget=target.analytic_input_budget(root,R0,sigma,RE)
    root,trace=target.refine_certified_root(root,scale,budget,3)
    budgets=target.parameter_input_budget(root,R0,sigma,RE)
    fields=target.parameter_target(root,scale,budgets)
    Cr=(-fields["C"][1]/scale).real
    if not Cr>0:
        raise ValueError("positive root transversality was not retained")
    Cd=fields["Cd"][0].real
    tp=-Cd/Cr
    Kr=(-fields["K"][1]/scale).real
    Kd=fields["Kd"][0].real
    alternative=-Kd/Kr
    if not tp.overlaps(alternative):
        raise ValueError("the two exact implicit-root derivative formulas disagree")
    tp=tp.intersection(alternative)
    identity["source_sha256"]=sha(__file__)
    report=dict(kind="uniform_true_affine_parameter_root_first_derivative",proved=True,
        **identity,germ_source_sha256=sha(germ_source),
        root_box_report_sha256=sha(args.root_box_report),root=ball_record(root),
        root_newton_trace=trace,exact_common_span=list(map(str,cells[0])),
        bits=args.bits,quarter_nodes=args.quarter_nodes,series_precision=args.precision,
        root_parameter_derivative=ball_record(tp),C_parameter=ball_record(Cd),
        C_radial=ball_record(Cr),K_parameter=ball_record(Kd),K_radial=ball_record(Kr),
        E_parameter_at_root=ball_record(fields["Ed"][0].real),
        E_radial_parameter_at_root=ball_record((-fields["Ed"][1]/scale).real),
        base_infinite_budget=record_budget(budgets[0]),
        derivative_infinite_budget=record_budget(budgets[1]),
        justification="exact scalar affine first jets; analytic nonlinear derivative; independent infinite primitive and E_delta tails; true-root implicit differentiation",
        limitations=["first root derivative only; no beta-prime integral certificate yet",
                     "this explicit parameter interval is not asserted to be the final KAM interval"],
        wall_seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({key:report[key] for key in
        ("proved","root_parameter_derivative","C_parameter","C_radial","wall_seconds")},indent=2),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-object",type=Path,required=True)
    parser.add_argument("--root-box-report",type=Path,required=True)
    parser.add_argument("--quarter-nodes",type=int,default=512)
    parser.add_argument("--bits",type=int,default=160)
    parser.add_argument("--precision",type=int,default=12)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if args.precision<6:
        raise ValueError("at least six retained radial coefficients required")
    run_root(args)


if __name__=="__main__":
    main()

