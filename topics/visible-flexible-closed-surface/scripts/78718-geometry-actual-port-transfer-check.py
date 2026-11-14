#!/usr/bin/env python3
"""Author exact checks for actual position/Sturm/Robin port conversion.
This checks symbolic identities and source file identities only: no data arrays,
no PDE, no candidate solve, and no original tail DN call.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sympy as s

TOPIC = Path(__file__).resolve().parent.parent
PROOF = TOPIC / "notes/2026-11-10-78718-geometry-actual-port-transfer-v1.md"
PROOF_SHA = "4922ab60da4f8f361e21c01df13ec5e0ece4846b5f94c825ca370cb300b89f69"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if sha(PROOF) != PROOF_SHA:
        raise ValueError("Frozen proof identity mismatch")
    a, c, v, n, f, h, lam = s.symbols("a c v n f h lam")
    nn = n**2 - 1
    fs = -(nn*c*f + n**2*v*h) / a
    hs = (nn*c**2*f/v + n**2*c*h) / a
    rot = s.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])

    def du(vec):
        return s.I*n*vec + rot*vec

    disp = s.Matrix([f, s.I*f/n, h])
    disp_s = s.Matrix([fs, s.I*fs/n, hs])
    d = s.Matrix([c, 0, v])
    tangent = s.Matrix([0, 1, 0])
    normal = s.Matrix([-v, 0, c])
    dotn = -(disp_s.dot(normal))*d - (du(disp).dot(normal)/a)*tangent
    dc = du(du(disp)).dot(normal) + s.Matrix([-a, 0, 0]).dot(dotn)
    dm = du(disp_s).dot(normal) + s.Matrix([0, c, 0]).dot(dotn)
    checks = {}

    def zero(name, expr, constraint=True):
        num, den = s.together(expr).as_numer_denom()
        if constraint:
            num = s.rem(s.expand(num), v**2+c**2-1, v)
        value = s.cancel(num/den)
        if value != 0:
            raise AssertionError((name, str(value)))
        checks[name] = True

    zero("metric_ss", c*fs+v*hs)
    zero("metric_su", a*fs+nn*c*f+n**2*v*h)
    zero("delta_C_with_normal_variation", dc-nn*f/v)
    zero("delta_M_with_normal_variation", dm+s.I*nn/(n*v)*(fs-c*f/a))
    x = s.I*n*nn*(h+c*f/v)
    y = -nn*f/a
    zero("sturm_x", a*dm-x)
    zero("sturm_y", -dc*v/a-y)
    zero("inverse_f", -a*y/nn-f)
    zero("inverse_h", x/(s.I*n*nn)+a*c*y/(nn*v)-h)
    mat = s.Matrix([[s.I*n*nn*c/v, s.I*n*nn], [-nn/a, 0]])
    zero("map_determinant", mat.det()-s.I*n*nn**2/a)
    b = n**2*c/a-lam
    k = n*c*(c-a*lam)/v
    zero("forced_Robin_row", b*x+s.I*k*y-s.I*n*nn*(hs-lam*h))

    sig, w, dn = s.symbols("sig w dn")
    fterm = sig*w*(a*dn-n**2)/nn*h

    def sigma_zero(name, expr):
        num, den = s.together(expr).as_numer_denom()
        num = s.rem(s.expand(num), sig**2-1, sig)
        if s.cancel(num/den) != 0:
            raise AssertionError(name)
        checks[name] = True

    sigma_zero("ideal_cut_x", s.I*n*nn*(h+sig/w*fterm)-s.I*n*(a*dn-1)*h)
    sigma_zero("ideal_cut_y", -nn*fterm/a+sig*w*(a*dn-n**2)*h/a)

    names = [
        "notes/fixed_metric_mode3_flow.py",
        "notes/fixed_metric_mode3_core.py",
        "scripts/950f-prefix-warped-bvp.py",
        "scripts/950f-prefix-adaptive-chart-bvp-v2.py",
        "scripts/db6f-prefix-coupled.py",
        "scripts/db6f-audit-metric-supplier.py",
        "repro/source-root/topics/large-amplitude-twist-flex/scripts/f6curve_bidirectional_bridge.py",
    ]
    sources = []
    for name in names:
        path = TOPIC/name
        if not path.is_file():
            raise FileNotFoundError(name)
        sources.append({"path":name, "bytes":path.stat().st_size, "sha256":sha(path)})
    report = {
        "scope": __doc__.strip(),
        "proof": str(PROOF.relative_to(TOPIC)),
        "proof_sha256": PROOF_SHA,
        "checker_sha256": sha(Path(__file__).resolve()),
        "symbolic_checks": checks,
        "symbolic_count": len(checks),
        "sources": sources,
        "pde_runs": 0,
        "candidate_arrays_read": 0,
        "tail_calls": 0,
        "passed": True,
    }
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({
        "passed":True, "symbolic_count":len(checks), "sources_bound":len(sources),
        "pde_runs":0, "tail_calls":0, "report_bytes":args.out.stat().st_size,
        "report_sha256":sha(args.out),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

