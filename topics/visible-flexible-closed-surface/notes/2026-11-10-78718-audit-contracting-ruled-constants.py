#!/usr/bin/env python3
"""Independent exact-rational margin checks for the ruled-core full audit.

This checks scalar margins only.  The all-angle estimates, existence theorem,
global chord proof and reach proof are proved in the companion audit Markdown.
It does not run an ODE, PDE, optimizer, or surface mesh.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

checks = []
def positive(name, margin):
    assert isinstance(margin, Q)
    assert margin > 0, (name, margin)
    checks.append({"name": name, "margin": str(margin), "pass": True})

def equal(name, left, right):
    assert left == right, (name, left, right)
    checks.append({"name": name, "value": str(left), "pass": True})

positive("s upper after squaring", Q(51, 50)**2 - Q(26, 25))
positive("p upper after squaring", Q(27, 25)**2 - Q(29, 25))
positive("curvature upper after squaring", Q(11, 10)**2 - Q(29, 25))
positive("cos theta lower after squaring", Q(25, 51) - Q(4, 9))
positive("sin theta lower after squaring", Q(1, 2) - Q(49, 100))
positive("minus alpha lower", Q(25, 26)*Q(2, 3) - Q(3, 5))
positive("kappa baseline lower", Q(35, 52) - Q(3, 5))
positive("alpha and kappa upper", Q(4, 5) - Q(27, 35))
equal("brace minimum attained at x=0,c=-1", Q(15, 29)-Q(1, 25), Q(346, 725))
positive("brace lower positive", Q(346, 725))
positive("beta lower on chosen control arc", Q(7, 10)*Q(346, 725)-Q(1, 3))
positive("global beta upper", Q(5, 8) - (Q(15, 26)+Q(1, 25)))
positive("curvature derivative upper", Q(1, 4) - Q(156, 625))
positive("alpha and kappa derivative upper", Q(3, 10) - (Q(1, 4)+Q(4, 5)*Q(1, 25)))
positive("theta second derivative upper", Q(1, 10) - Q(2, 25)*(1+Q(77, 2500)))
positive("beta derivative upper", Q(8, 5) - (Q(240, 169)+Q(1, 10)))
positive("metric quadratic coefficient upper", Q(21, 20) - (Q(4, 5)**2+Q(5, 8)**2))
equal("radial numerator upper", -Q(3, 5)+Q(1, 10)*Q(21, 20), -Q(99, 200))
equal("band metric lower", 1-Q(4, 5)*Q(1, 100), Q(124, 125))
c_lower = Q(124, 125)*Q(35, 52) - (Q(1, 100)*Q(8, 5)+Q(1, 10000)*Q(5, 8)*Q(3, 10))/Q(124, 125)
positive("baseline second form C lower", c_lower-Q(13, 20))
equal("baseline C margin", c_lower-Q(13, 20), Q(15933, 10316800))
positive("perturbed second form C lower", Q(13, 20)-Q(1, 50)-Q(3, 5))
positive("ruling second derivative upper squared", 9-(Q(21, 20)**2+Q(4, 5)**2+Q(56, 25)**2))
positive("F uu upper", Q(23, 20) - (Q(11, 10)+Q(1, 100)*3))
positive("Hessian matrix first principal minor", Q(9, 5))
equal("Hessian matrix second principal minor", Q(9, 5)*(Q(9, 5)-Q(23, 20))-Q(21, 20)**2, Q(27, 400))
positive("Hessian matrix second principal minor positive", Q(27, 400))
positive("near chord margin", Q(124, 125)-Q(9, 20)-Q(27, 50))
positive("far angular separation after squaring", Q(1, 4)-Q(1, 10000)-Q(49, 100)**2)
positive("circle chord slope using pi < 22/7", Q(100, 51)/Q(22, 7)-Q(3, 5))
positive("coordinate versus angular ratio after squaring", Q(51, 50)**2-(1+Q(1, 49)**2))
far = (Q(3, 5)-Q(2, 49))*Q(50, 51)
equal("far chord value", far, Q(6850, 12495))
positive("far chord margin", far-Q(27, 50))
positive("perturbed chord margin", Q(27, 50)-Q(1, 50)-Q(1, 2))
positive("diameter square margin", Q(201, 20)**2-101)
equal("reach bound from chord and Hessian", Q(1, 2)**2/2, Q(1, 8))
equal("reach to initial diameter ratio", Q(1, 8)/Q(203, 100), Q(25, 406))
positive("normalized reach margin", Q(25, 406)-Q(3, 100))
positive("held diameter normalized margin", Q(200, 203)-Q(1, 2))

out = Path(__file__).with_name("2026-11-10-78718-audit-contracting-ruled-constants.json")
payload = {
    "scope": "exact scalar margins; no ODE/PDE/mesh or candidate optimization",
    "checker_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "check_count": len(checks),
    "all_pass": True,
}
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(f"PASS {len(checks)} exact scalar margins; output {out.name}")
print(f"output bytes={out.stat().st_size} sha256={sha256(out.read_bytes()).hexdigest()}")
print(f"checker bytes={Path(__file__).stat().st_size} sha256={payload['checker_sha256']}")
