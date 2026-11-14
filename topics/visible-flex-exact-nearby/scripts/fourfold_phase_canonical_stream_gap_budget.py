#!/usr/bin/env python3
"""R108: exact arithmetic from five complete, hash-bound actual reports.

This source was reconstructed after executor loss. It does not reuse a lost
JSON or claim that the unexecuted wide-collar pilot ran. All new reported
numbers are calculated by this native entry point. The full residual R1 is
an explicitly unpaid input, not a numeric output of this program.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
from fractions import Fraction as F
from pathlib import Path

INPUTS = [
    ("frame", "notes/2026-11-12-ci-actual-root-Cauchy-frame-Fourier-summary.json",
     "8c13c40e1ea65eb05a97eaeb79cba1ab49f8ebe734ad598d0b382a0afe6890bf"),
    ("v0", "notes/2026-11-12-ci-canonical-v0-scaled-Wiener-summary.json",
     "66112956b245389aa38c3d07244685ad31c29f7aae0575b8986bf80b54459ce8"),
    ("v1", "notes/2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json",
     "c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b"),
    ("contact", "notes/2026-11-12-ci-direct-canonical-source-summary.json",
     "826bda30e5d42bf47efc4fb5daa3bf6da1361bb2f4ee737486f89be9c597ca09"),
    ("root", "notes/2026-11-12-actual-common-root-high-remainder.json",
     "e727251cd6c187ded5782aff3a03401301d21b83fd03d419f31f716862be6253"),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def interval(x):
    """Exact rational enclosure of the saved directed decimal or Arb text."""
    if isinstance(x, dict):
        if "ball" in x:
            return interval(x["ball"])
        if "numerator" in x:
            q = F(int(x["numerator"]), int(x["denominator"]))
            return q, q
        raise ValueError("unsupported saved number")
    if isinstance(x, float):
        raise ValueError("binary floating point must not enter exact budget")
    s = str(x).strip()
    if not s.startswith("["):
        q = F(s)
        return q, q
    m = re.fullmatch(r"\[\s*(\S+)\s+\+/-\s+(\S+)\s*\]", s)
    if not m:
        raise ValueError("unsupported Arb text: " + s)
    c, r = F(m.group(1)), F(m.group(2))
    if r < 0:
        raise ValueError("negative radius")
    return c-r, c+r


def upper(x):
    return interval(x)[1]


def lower(x):
    return interval(x)[0]


def ceil_decimal(x, digits=18):
    if x < 0:
        raise ValueError("positive bound expected")
    scale = 10**digits
    q = (x.numerator*scale+x.denominator-1)//x.denominator
    s = str(q).zfill(digits+1)
    return s[:-digits]+"."+s[-digits:]


def sqrt_upper(x, digits=24):
    if x < 0:
        raise ValueError("negative square")
    scale = 10**digits
    q = math.isqrt(x.numerator*scale*scale//x.denominator)
    if q*q*x.denominator < x.numerator*scale*scale:
        q += 1
    return F(q, scale)


def record(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal_upper": ceil_decimal(x)}


def budget(inputs):
    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise ValueError(name)

    frame, v0, v1, cap, root = (inputs[k] for k in
                              ("frame", "v0", "v1", "contact", "root"))
    check("all_original_reports_proved", all(v["proved"] for v in inputs.values()))
    identity = frame["identity"]
    for key in ("exact_parameter_interval", "exact_center_parameter",
                "exact_parameter_half_width", "origin_inputs_sha256", "direction_sha256"):
        check("same_actual_identity_"+key,
              all(x["identity"][key] == identity[key] for x in (v0, v1, root)))
    check("same_eta_1e-9", identity["exact_parameter_half_width"] == "1/1000000000")
    check("R96_all_178_cells", cap["actual_cells"] == 178)

    def wfield(name, order):
        x = frame["fields"][name]["Wiener"][str(order)]
        # The original norm already includes its prescribed complete fees;
        # adding error once more is a deliberate safe overestimate.
        return upper(x["norm"])+upper(x["error"])

    t0, I0, I1 = F("1.477443"), F(".831"), F("1.489006")
    mu0, mu1, Y = F("24.940215"), F("31.245346"), F(".055953")
    check("true_root_height_sup", wfield("t0", 0) < t0)
    check("true_inverse_height_sup", upper(frame["fields"]["inverse_t0"]["complex_modulus"]) < I0)
    check("true_inverse_height_physical_first_derivative", wfield("inverse_t0", 1) < I1)
    check("true_root_momentum_shear_sup", wfield("root_momentum_shear", 0) < mu0)
    check("true_root_momentum_shear_physical_derivative", wfield("root_momentum_shear", 1) < mu1)
    C = cap["constants"]
    check("true_root_angle_derivative_lower", Y < lower(C["root_angle_derivative_lower"]["lower"]))
    eps, G, H, tmin = F(".000001552858"), F("33.417980"), F(49,102400), F("1.1568")
    check("true_principal_normalized_error", upper(C["epsilon"]["upper"]) < eps)
    check("true_covariant_log_height_derivative", upper(C["G0"]["upper"]) < G)
    check("true_height_positive_lower", tmin < lower(C["actual_height_lower"]["lower"]))
    check("same_paid_canonical_height", lower(C["canonical_flat_height"]) <= H <= upper(C["canonical_flat_height"]))
    check("height_drift_denominator_positive", G*H < 1)
    Tmax = t0/(1-G*H)
    inv_factor = Tmax*Tmax/(1-eps)
    L = F("2.257")
    check("actual_full_inverse_density_not_height_only", inv_factor < L)

    B0, B1, V0, V1 = F(692327), F(143113), F(5176), F(1186)
    for name, data, order, val in (("b_M0", v1, 0, B0), ("b_M1", v1, 1, B1),
                                    ("v0_M0", v0, 0, V0), ("v0_M1", v0, 1, V1)):
        row = next(x for x in data["budgets"] if x["high_cutoff"]==256
                   and x["weight_order"]==0 and x["moment"]==order)
        check("complete_actual_"+name, upper(row["true_scaled_Wiener_upper"]) < val)
    qlo, qhi = F(243,25), F(10)
    check("complete_actual_q_lower", qlo < lower(v0["true_frequency"]["lower"]))
    check("complete_actual_q_upper", upper(v0["true_frequency"]["upper"]) < qhi)

    L1, H2 = I1/Y, I0*mu0
    L2 = (I0*mu1+mu0*I1)/Y
    Db, Dv = 4*qhi*B1, 4*qhi*V1
    cm = sqrt_upper(L*H)
    c1 = sqrt_upper(L/tmin**2*(H**5/20+H**2/(2*(4*qlo)**2)))
    Ereg = upper(C["regular_mean_extension_energy"]["upper"])
    contacts = {x["canonical_output_cutoff_N"]: x for x in cap["high_root_contact_table"]}
    rows = []
    for r in root["budgets"]:
        K = r["canonical_high_cutoff"]
        lam = F(r["strict_Lambda_lower"])
        cube = F(r["strict_cuberoot_Lambda_lower"])
        check("strict_frequency_lower_K"+str(K), lam < 4*qlo*(K+1))
        check("strict_cube_lower_K"+str(K), cube**3 < lam)
        mean = F(39,100)*L1/cube**2 + F(54,100)*L2/(lam*cube)
        mean += F(39,100)*(Db*I0+B0*L1+Dv*H2+V0*L2)/(lam**2*cube**2)
        E = upper(contacts[K]["root_extension_energy"]["upper"])
        cr, cj = sqrt_upper(E), sqrt_upper(E+Ereg)
        rows.append({"canonical_high_input_cutoff": K,
            "all_output_modes_and_mean_retained": True,
            "Lambda_strict_lower": str(lam), "cube_Lambda_strict_lower": str(cube),
            "full_mean_functional_upper": record(mean),
            "complete_gap_mean_fee": record(cm*mean),
            "root_contact_mean_fee": record(cr*cm*mean),
            "root_contact_R1_coefficient": record(cr*c1),
            "root_and_regular_contact_mean_fee": record(cj*cm*mean),
            "root_and_regular_contact_R1_coefficient": record(cj*c1),
            "root_contact": record(cr), "root_and_regular_contact": record(cj)})

    return {"kind": "R108_complete_canonical_compact_stream_actual_budget",
        "proved_actual_coefficient_and_mean_budget": True,
        "proved_new_full_cap_gap": False, "actual_identity": identity,
        "angular_normalization": "unaveraged integral; e_phi=(2*pi/q)^(-1/2); physical e_theta=(2*pi)^(-1/2)",
        "paid_canonical_height": str(H), "true_root_height_upper": record(t0),
        "complete_principal_relative_error_upper": record(eps),
        "complete_height_log_derivative_upper": record(G),
        "complete_height_upper": record(Tmax),
        "inverse_density_factor_including_normalized_matrix": record(inv_factor),
        "clean_inverse_density_factor": record(L),
        "gap_mean_coefficient": record(cm), "gap_R1_coefficient": record(c1),
        "coefficient_bounds": {k: record(v) for k,v in dict(I0=I0,I1=I1,mu0=mu0,mu1=mu1,
             Yprime_lower=Y,L1=L1,H2=H2,L2=L2,B0=B0,B1=B1,V0=V0,V1=V1,Db=Db,Dv=Dv).items()},
        "tables": rows, "checks": checks,
        "unpaid_input": "R1 = sup_y || P_can(chi U_completed)(y)/y || from all continuous angles/radii, all cutoff, full E and height terms",
        "scope": ["Full physical cap with unchanged Robin form; compact primal and solenoidal dual vanish before outer port.",
                  "Canonical input high projection never replaces physical projection or removes low output rows.",
                  "No new wide-collar geometry was sampled; actual range is only the already proved R96 collar.",
                  "A fixed y^2 completion alone does not authorize high-input strong gain; R108 supplies right-input Airy localization."]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    inputs, records = {}, []
    for key, rel, expected in INPUTS:
        p = args.topic/rel
        if sha(p) != expected:
            raise ValueError("actual input SHA mismatch: "+str(p))
        inputs[key] = json.loads(p.read_text())
        records.append({"key":key,"path":rel,"sha256":expected})
    report = budget(inputs)
    report["input_reports"] = records
    report["source_sha256"] = sha(__file__)
    report["execution"] = {"full_native_entry_executed": True,
        "arithmetic": "Python exact Fraction, integer isqrt, directed rational decimals; no binary floating point",
        "reconstructed_after_executor_loss": True, "lost_old_report_reused": False}
    out = args.output or args.topic/"notes/2026-11-12-R108-canonical-stream-gap-budget.json"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"checks":len(report["checks"]),"all_passed":all(x["passed"] for x in report["checks"]),
        "inverse_factor":report["inverse_density_factor_including_normalized_matrix"]["decimal_upper"],
        "gap_mean":report["gap_mean_coefficient"]["decimal_upper"],
        "gap_R1":report["gap_R1_coefficient"]["decimal_upper"],
        "source_sha256":sha(__file__),"report_sha256":sha(out),"full_gap_paid":False}))


if __name__ == "__main__":
    main()
