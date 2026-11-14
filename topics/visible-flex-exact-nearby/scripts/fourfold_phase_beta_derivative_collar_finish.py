#!/usr/bin/env python3
"""Finish a saved true derivative collar coefficient checkpoint on a new domain.

The retained coefficients are accepted only from the unchanged full source,
with every exact family identity and dependency checked. Their computation
is independent of the subsequently selected radial/angle Cauchy radii.
No failed domain enclosure is reused.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_derivative_collar import ParameterDerivativeCollar
from fourfold_phase_beta_parameter_derivative import sha,record_budget
from fourfold_phase_beta_parameter_germ import provenance


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--center-object",type=Path,required=True)
    ap.add_argument("--coefficient-checkpoint",type=Path,required=True)
    ap.add_argument("--radial-radius",default=".0005")
    ap.add_argument("--sigma",default=".0125")
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();started=time.monotonic()
    checkpoint=json.loads(args.coefficient_checkpoint.read_text())
    here=Path(__file__).parent
    kernel=here/"fourfold_phase_beta_derivative_collar.py"
    core=here/"fourfold_phase_beta_parameter_derivative.py"
    if (checkpoint.get("kind")!="uniform_true_fixed_r_parameter_derivative_collar"
            or checkpoint["source_sha256"]!=sha(kernel)
            or checkpoint["derivative_core_sha256"]!=sha(core)
            or checkpoint["center_object_sha256"]!=sha(args.center_object)
            or not checkpoint["coefficient_diagnostics"]["independent_H0_identity_checked"]):
        raise ValueError("saved derivative coefficients do not identify the unchanged kernel and graph")
    for name,digest in checkpoint["dependency_sha256"].items():
        if sha(here/name)!=digest:raise ValueError("changed coefficient dependency: "+name)
    ctx.prec,ctx.cap=checkpoint["bits"],checkpoint["series_precision"]
    target=ParameterDerivativeCollar(args.center_object,Fraction(checkpoint["exact_parameter_half_width"]),
        checkpoint["quarter_nodes"],checkpoint["angles"],arb(".003"),arb(".0025"),arb(".32"))
    identity=provenance(target,args.center_object)
    for key in ("origin_inputs_sha256","direction_sha256","exact_center_parameter",
                "exact_parameter_half_width","exact_parameter_interval"):
        if identity[key]!=checkpoint[key]:raise ValueError("parameter identity differs: "+key)
    root,cut=stored_ball(checkpoint["root"]),Fraction(checkpoint["fixed_cut"])
    cell=tuple(map(Fraction,checkpoint["exact_common_span"]))
    if not exact_arb(cell[0])<exact_arb(cut)<root.lower() or not root.upper()<exact_arb(cell[1]):
        raise ValueError("complete physical collar crosses its common span")
    target.set_cell(*cell)
    scale=exact_arb(Fraction(1,4096));R=arb(args.radial_radius);sigma=arb(args.sigma)
    eta=root-exact_arb(cut)
    if not 0<eta<R:raise ValueError("chosen Cauchy disk does not cover every physical collar")
    coefficients=[stored_ball(x) for x in checkpoint["coefficients"]]
    degree=checkpoint["degree"]
    if len(coefficients)!=degree+1:raise ValueError("wrong retained coefficient count")
    polynomial=sum((coefficients[j]*eta**(arb(j)-arb(5)/2)/(arb(j)-arb(5)/2)
                    for j in range(degree+1)),arb(0))
    budgets=target.parameter_input_budget(root,arb(".003"),arb(".32"),arb(".0025"))
    data=target.parameter_target(root,scale,budgets)
    report=dict(checkpoint)
    report.update(complete=False,source_sha256=sha(__file__),
        coefficient_kernel_sha256=sha(kernel),coefficient_checkpoint_path=str(args.coefficient_checkpoint),
        coefficient_checkpoint_sha256=sha(args.coefficient_checkpoint),
        radial_radius=args.radial_radius,sigma=args.sigma,eta=ball_record(eta),
        polynomial_finite_part=ball_record(polynomial),
        base_input_budget=record_budget(budgets[0]),derivative_input_budget=record_budget(budgets[1]))
    def save():
        report["wall_seconds"]=time.monotonic()-started
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(json.dumps(report,indent=2)+"\n")
    save()
    print(json.dumps(dict(stage="new derivative domain",radial_radius=args.radial_radius,
                          sigma=args.sigma,polynomial=polynomial.str(28))),flush=True)
    bound,domain=target.density_domain(root,scale,R,sigma,budgets,data)
    radial=bound*eta**(arb(degree)-arb(3)/2)/(
        (arb(degree)-arb(3)/2)*R**(degree+1)*(1-eta/R))
    angle_mean=2*bound*(-sigma*target.angles).exp()/(1-(-sigma*target.angles).exp())
    angular=2*angle_mean*eta**(-arb(5)/2)/(1-eta/R)
    result=polynomial+arb(0,(radial+angular).upper())
    report.update(complete=True,domain=domain,radial_tail_error=ball_record(radial.upper()),
        angular_error=ball_record(angular.upper()),derivative_collar_integral=ball_record(result))
    save()
    print(json.dumps(dict(complete=True,derivative_collar=result.str(30),
        radial_tail=radial.str(22),angular_tail=angular.str(22),wall_seconds=report["wall_seconds"])),flush=True)


if __name__=="__main__":main()

