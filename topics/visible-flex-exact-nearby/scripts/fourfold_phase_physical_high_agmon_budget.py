#!/usr/bin/env python3
"""Actual restricted-cap Agmon action and remote-source/contact budgets."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(x):
    x=F(x)
    return arb(x.numerator)/x.denominator
def binary(x):return exact(F.from_float(x))
def low(r):return arb(r["lower"]).lower()
def high(r):return arb(r["upper"]).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--collar",type=Path,default=Path("notes/2026-11-12-positive-family-root-collar.json"))
    ap.add_argument("--boundary",type=Path,default=Path("notes/2026-11-12-actual-physical-high-boundary-budget.json"))
    ap.add_argument("--out",type=Path,required=True)
    args=ap.parse_args();ctx.prec=256
    c=json.loads(args.collar.read_text());d=json.loads(args.boundary.read_text())
    if not c.get("complete") or c["failed_cells"] or c["pending"] or not d.get("proved"):
        raise ValueError("required actual collar/high boundary certificate is incomplete")
    for key in ("origin_inputs_sha256","direction_sha256"):
        if c[key]!=d[key]:raise ValueError("actual family identities differ")
    ca,cb=map(F,c["exact_parameter_interval"]);da,db=map(F,d["exact_parameter_interval"])
    if not ca<=da<=db<=cb:raise ValueError("high boundary family not in actual collar family")
    rows=sorted(c["cells"],key=lambda r:F(r["radial_interval"][0]))
    if c["exact_radial_cover"] is not True:
        raise ValueError("old actual radial cover was not verified")
    start=F(c["root_interval"][0]);end=F(c["physical_regular_cut"]);cursor=start
    for row in rows:
        a,b=map(F,row["radial_interval"])
        if a!=cursor or not b>a:raise ValueError("real physical collar cover has gap/overlap")
        cursor=b
    if cursor!=end or len(rows)!=d["actual_collar_cells"]:
        raise ValueError("real collar coverage identity mismatch")
    kap=low(c["operator_constants"]["K_over_distance_lower"])
    length=low(c["operator_constants"]["length_lower"])
    # A fixed rational length avoids defining the weight by a numerical
    # endpoint.  The true same-family collar is strictly longer.
    ell=exact(F(29,2500))
    if not 0<ell<length:raise ValueError("fixed actual weight support exceeds collar")
    ratios=[]
    for index,row in enumerate(rows):
        g=row["real_geometry"]
        amin,amax=g["alpha"];emin,emax=g["eta"]
        if not 0<amin<=amax or not 0<emin<=emax:
            raise ValueError("real positive coefficient bounds unresolved")
        value=kap*binary(emin)/(2*binary(amax))
        ratios.append({"row_index":index,"radial_interval":row["radial_interval"],
                       "action_slope_square_lower":ball_record(value.lower())})
    sigma2=min(low(r["action_slope_square_lower"]) for r in ratios).lower()
    if not sigma2>0:raise ValueError("actual positive action unresolved")
    # Select a rational rounded-down slope.  This is a definition of psi,
    # not an approximate equality between uncertain interval quantities.
    scale=10**9
    numerator=int(float((sigma2.sqrt()*scale).lower().floor()))
    sigma=arb(numerator)/scale
    if not 0<sigma*sigma<sigma2:raise ValueError("rational action slope not strictly justified")
    output=[]
    for row in d["cutoff_table"]:
        N=row["N"];lam=arb(row["first_retained_physical_frequency"])
        if row["first_retained_physical_frequency"]!=4*(N+1):
            raise ValueError("physical fourfold frequency mismatch")
        C=high(row["compressed_L2_Poisson_and_source_contact"])
        E=high(row["true_projected_boundary_lift_energy"])
        values=[]
        for support in [F(1,2048),F(1,1024),F(1,512),F(1,256),F(1,128),F(29,2500)]:
            x=exact(support)
            action=arb(2)/3*sigma*lam*min(x,ell)**(arb(3)/2)
            factor=min(arb(1),(arb(2).sqrt()*(-action).exp()).upper())
            energy_factor=min(arb(1),((1+arb(2).sqrt())*(-action).exp()).upper())
            values.append({"exact_source_support_lower":str(support),
             "action":ball_record(action),"improvement_factor":ball_record(factor),
             "remote_L2_source_to_high_root_contact":ball_record((C*factor).upper()),
             "remote_energy_source_to_high_root_contact":ball_record(
                 (E.sqrt()*energy_factor).upper())})
        action_end=arb(2)/3*sigma*lam*ell**(arb(3)/2)
        regular=min((7*E).sqrt().upper(),
                    ((14*E).sqrt()*(-action_end).exp()).upper())
        output.append({"N":N,"first_retained_physical_frequency":4*(N+1),
          "original_source_contact_upper":ball_record(C),"source_support_table":values,
          "full_regular_action":ball_record(action_end),
          "regular_high_Robin_source_to_root_contact":ball_record(regular)})
    report={"kind":"actual_full_positive_restricted_high_cap_Agmon_remote_contact",
      "proved":True,"source_sha256":sha(__file__),
      "input_sha256":{str(args.collar):sha(args.collar),str(args.boundary):sha(args.boundary)},
      "exact_parameter_interval":d["exact_parameter_interval"],
      "origin_inputs_sha256":d["origin_inputs_sha256"],"direction_sha256":d["direction_sha256"],
      "actual_collar_cells":len(rows),"fixed_weight_support_length":"29/2500",
      "true_local_length_lower":ball_record(length),"global_K_over_root_distance_lower":ball_record(kap),
      "actual_action_slope_square_lower":ball_record(sigma2),
      "exact_selected_action_slope":f"{numerator}/{scale}",
      "per_cell_action_square_lower":ratios,"cutoff_table":output,
      "weight_formula":"psi_N(s)=(2/3)*sigma*4*(N+1)*min(s,29/2500)^(3/2)",
      "scope":["The weight is radial, equals zero at the true root, and is constant at the true regular Robin end.",
       "The exact weighted energy identity includes the complete same-object Robin form.",
       "All results concern the physical Fourier-restricted high body, not the uncompressed full cap.",
       "The original root mean, regular xi/lambda slots, and low-body/low-root coupling remain in the complete Schur system.",
       "Canonical high inputs are not identified with physical high inputs.",
       "No actual Airy source support or reflected-wave cutoff is inferred merely from this remote-source bound."]}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"proved":True,"actual_cells":len(rows),"sigma":str(sigma),
      "report_sha256":sha(args.out)},indent=2))


if __name__=="__main__":
    main()
