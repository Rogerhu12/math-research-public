#!/usr/bin/env python3
"""Exact rational comparisons of completed small records and the SM estimates.

No native, coefficient field, ODE, quadrature or old scientific target is
evaluated. All arithmetic is on published decimal endpoints and constants.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]
CP = TOPIC / "notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json"
LC = TOPIC / "notes/localized_full_state_compact_sources_ci/run-45797426031-1/localized-full-state-and-compact-sources.json"
VM = TOPIC / "notes/signed_metric_mean_moments_ci/run-45888851105-1/signed-metric-mean-moments.json"


def ball(value):
    scale = Q(10)**int(value["decimal_exponent"])
    m, r = int(value["midpoint_integer"]), int(value["radius_integer"])
    return (m-r)*scale, (m+r)*scale


def read(path, expected):
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == expected
    doc = json.loads(raw)
    assert doc["complete"] is True and doc.get("failure") is None
    return doc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vm", type=Path, default=VM)
    args = parser.parse_args()
    cp = read(CP, "0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641")
    lc = read(LC, "60ac20418b405281a3150216e45f7bffd0e73b7625ccc8c383cf4204968b5748")
    vm = read(args.vm, "d50260a3bd8e6b224b4cf82751e1d14d87f557b9a469cbad5c119e171b7ef960")
    checks = []

    def check(name, condition):
        assert condition, name
        checks.append(name)

    c, l, v = cp["complete_new_scalars"], lc["complete_new_scalars"], vm["complete_new_scalars"]
    check("raw mean lower", ball(c["mean_abs_lower"])[0] > Q("1.068"))
    check("raw mean upper", ball(c["mean_abs_upper"])[1] < 6)
    check("raw variance", ball(c["variance_upper"])[1] < Q(".474"))
    check("H compact endpoint", ball(c["H_at_compact_right"])[1] < Q("1.003"))
    check("positive moment lower", ball(c["abar"])[0] > Q(".00452"))
    check("positive moment upper", ball(c["abar"])[1] < Q(".00462"))
    check("second positive moment", 0 < ball(c["bbar"])[0]
          and ball(c["bbar"])[1] < Q(".00172"))
    check("raw density norm", ball(l["density_A0_upper"])[1] < Q("1.923"))
    check("raw nonmean norm", ball(l["cosine_nonmean_A0_upper"])[1] < Q(".986"))
    check("normalized variance", Q(".474")/Q("1.068")**2 < Q(".416"))
    check("complete new metric run", vm["gates"]["kappa_nu_interval_excludes_zero"] is True
          and vm["completed_original_rows"] == 7721
          and vm["completed_original_mean_joins"] == 6143
          and vm["completed_compact_rows"] == 1156
          and vm["completed_signed_subcells"] == 1157
          and vm["completed_compact_candidate_joins"] == 864)
    table = {
        "I_U": ("0.0000049198", "0.0000049918"),
        "E0": ("-.001682146", "-.001571667"),
        "E1": ("-.000638393", "-.000579550"),
        "E2": ("-.000358865", "-.000318775"),
        "A3": (".001394994", ".001425940"),
        "M0": ("-.000745924", "-.000589680"),
        "M1": ("-.001134012", "-.001041629"),
        "M2": ("-.001107165", "-.001036129"),
        "normalized_metric_waist_polynomial": ("-.000745924", "-.000589680"),
        "kappa_nu": ("-.0003986", "-.0003151"),
        "density_control_metric_derivative": (".1277", ".1649"),
    }
    for name, (lo, hi) in table.items():
        a, b = ball(v[name])
        check("actual signed " + name, Q(lo) < a <= b < Q(hi))

    d, rho, r = Q("1e-10"), Q("8e-13"), Q("2e-8")
    H, q, aa, bb = Q("1.003"), Q(".416"), Q(".00462"), Q(".00172")
    check("old LC algebraic range", r < Q(lc["exact_parameters"]["rho"])
          and Q("2.57e-7") < Q(lc["exact_parameters"]["b"]))
    J = 1+(1+r)**2*q
    check("density second moment", J < Q("1.417"))
    Fxi_lo = (1-r)*((1-d)*Q(".00452") - 4*d*q/(1-d))
    Fxi_hi = (1+r)*(aa+4*d*q)/(1-d)
    check("uniform xi derivative lower", Fxi_lo > Q(".0045"))
    check("uniform xi derivative upper", Fxi_hi < Q(".004621"))
    Fnu_abs = Q(".003")+(1+rho)**2*((aa/2+2*d*q)/(1-d)+2*q)
    check("coarse metric waist derivative", Fnu_abs < Q(".838"))
    check("coarse root endpoint signs", Q(".0045")*(r-rho) > Q(".838")*d)
    eps = H*(3*Q("1.417")*d+aa*(r+rho)+bb*(r*r+rho*rho))
    check("coarse complete Y change", eps < Q("5.2e-10"))
    check("uniform positive Y", 1/Q("6.001")**2-Q("5.2e-10") > 1/Q("6.01")**2)
    check("coarse mean change", Q("6.01")**3*Q("5.2e-10")/2 < Q("5.65e-8"))
    check("coarse raw mean radius", Q("2e-7")+Q("5.65e-8") < Q("2.57e-7"))
    check("complete density floor", Q(".09")/6-r*Q(".986")/Q("1.068") > Q(".01499"))

    p_lo, p_hi = ball(v["normalized_metric_waist_polynomial"])
    m1 = max(map(abs, ball(v["M1"])))
    m2 = max(map(abs, ball(v["M2"])))
    drift = 4*Q("1.417")*d/(1-d) + 2*(r+rho)*m1 + (r*r+rho*rho)*m2
    check("actual signed derivative on whole rectangle",
          p_lo-drift > Q("-.000746") and p_hi+drift < Q("-.0005896"))
    check("actual compensating slope lower", Q(".0005896")/Fxi_hi > Q(".1275"))
    check("actual compensating slope upper", Q(".000746")/Fxi_lo < Q(".166"))
    rs = Q("1.75e-11")
    check("actual selected metric root radius", rho+Q(".166")*d < rs)
    eps_s = H*(3*Q("1.417")*d+aa*(rs+rho)+bb*(rs*rs+rho*rho))
    check("sharp complete Y change", eps_s < Q("4.265e-10"))
    check("sharp mean change", Q("6.01")**3*Q("4.265e-10")/2 < Q("4.63e-8"))
    bs = Q("2.464e-7")
    check("sharp raw mean radius", Q("2e-7")+Q("4.63e-8") < bs)
    c0 = Q("1.923")*bs+Q(".986")*rs
    c1 = Q("5.438")*(bs/Q("1.068")*(1+rs)+rs)
    check("sharp same circle state", c0 < Q("4.739e-7"))
    check("sharp same circle derivative", c1 < Q("1.255e-6"))
    check("same selected metric state bridge",
          c0+Q("3.861e-18")+19*d < Q("4.760e-7"))
    check("same selected metric derivative bridge",
          c1+Q("1.970e-17")+83*d < Q("1.264e-6"))
    print(json.dumps(dict(complete=True, exact_rational_comparisons=len(checks),
                          all_passed=True, scientific_native_or_quadrature_calls=0),
                     sort_keys=True))


if __name__ == "__main__":
    main()
