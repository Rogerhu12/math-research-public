#!/usr/bin/env python3
"""Fixed exact angular certificate for R263; no target-prime sampling."""
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "check-e136-theta-section.json").read_text())[
    "projective_coordinate_checks"
]
t = s.symbols("t")
a, b, h = [
    s.Poly(sum(s.Rational(c) * t**j for j, c in enumerate(data[key])), t)
    for key in ("primitive_a", "primitive_b", "primitive_h")
]
A, B, H = 5*a, 5*b, 55*h
assert all(c.q == 1 for P in (A, B, H) for c in P.all_coeffs())
f = (A*A+B*B).primitive()[1].set_domain(s.QQ)
g = (H*H-121*B*B).primitive()[1].set_domain(s.QQ)
U, V, one = s.gcdex(f, g)
assert one == s.Poly(1, t, domain=s.QQ)
den = s.ilcm(*[c.q for P in (U, V) for c in P.all_coeffs()])
Ui, Vi = (U*den).set_domain(s.ZZ), (V*den).set_domain(s.ZZ)
assert Ui*f+Vi*g == s.Poly(den, t, domain=s.QQ)
gaussian_gcd = s.gcd(
    s.Poly(b.as_expr()+s.I*a.as_expr(), t, extension=s.I),
    s.Poly(h.as_expr()-s.I*a.as_expr(), t, extension=s.I),
)
assert gaussian_gcd.degree() == 0
def asc(P):
    return [str(P.nth(j)) for j in range(P.degree()+1)]
payload = {
    "claim": "The original projective curve misses [1:-i:i] and its conjugate",
    "input_sha256": hashlib.sha256(
        (ROOT / "check-e136-theta-section.json").read_bytes()).hexdigest(),
    "primitive_degrees": [a.degree(), b.degree(), h.degree()],
    "f_definition": "primitive_part((5a)^2+(5b)^2)",
    "g_definition": "primitive_part((55h)^2-121*(5b)^2)",
    "f": asc(f), "g": asc(g),
    "bezout_U": asc(Ui), "bezout_V": asc(Vi),
    "bezout_integer": str(den),
    "gaussian_gcd_degree": gaussian_gcd.degree(),
    "infinity_image": "[0:0:1]",
    "status": "PASS",
}
output = ROOT / "check-three-source-ordinary-cartier-defect.json"
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({
    "status": "PASS",
    "degrees": [f.degree(), g.degree(), Ui.degree(), Vi.degree()],
    "bezout_integer_digits": len(str(den)),
    "json_bytes": output.stat().st_size,
}))

