"""Exact QQ certificate for the two residue identities in restored R564.

This does not sample primes or torsion points.  It verifies identities in
QQ[r]/(r^3-4), with denominator invertibility certified in the same field.
"""
from pathlib import Path
from hashlib import sha256
import json
import sympy as s

r = s.symbols("r")
modulus = r**3 - 4
x = (r + 2) / (r - 1)
X = x**3
Dprime = 3 * X**2 - 456 * X + 48
rows = []
for name, coefficient, expected in [
    ("minus", 34, -r / 72),
    ("plus", -20, -r**2 / 144),
]:
    # beta * residue, using y/beta=-3/(r-1)^2 and the exact dx/(2y).
    actual = s.cancel(-(r - 1)**2 * (X**2 + coefficient * X - 8) / (18 * Dprime))
    numerator, denominator = s.fraction(actual)
    den_mod = s.rem(denominator, modulus)
    inverse = s.invert(den_mod, modulus)
    reduced = s.rem(s.rem(numerator, modulus) * inverse, modulus)
    difference = s.cancel(reduced - expected)
    assert difference == 0
    rows.append({
        "kernel": name,
        "reduced_beta_residue": str(reduced),
        "expected": str(expected),
        "difference": str(difference),
        "denominator_remainder": str(den_mod),
        "denominator_inverse": str(inverse),
        "inverse_check": str(s.rem(den_mod * inverse - 1, modulus)),
    })
result = {
    "status": "exact-algebraic-identities",
    "field": "QQ[r]/(r^3-4)",
    "sampling": False,
    "rows": rows,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(out), "sha256": sha256(out.read_bytes()).hexdigest(), "status": result["status"]}))
