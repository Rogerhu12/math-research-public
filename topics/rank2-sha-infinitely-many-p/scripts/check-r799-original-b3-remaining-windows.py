#!/usr/bin/env python3
"""R799: the three remaining original b=3 small-characteristic systems.
Public Actions only. Reuses the exact R788 rational-series producer.
No generated result file is written.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import importlib.util
import json

helper = Path(__file__).with_name("check-r788-original-b3-contact-all-primes.py")
expected = "f729371aa6867a84e1a4de18abdcd6d2451987e7174809a0a19269631c68da0e"
digest = hashlib.sha256(helper.read_bytes()).hexdigest()
if digest != expected:
    raise RuntimeError("R788 producer changed; re-read its diff before running")
spec = importlib.util.spec_from_file_location("r788_original", helper)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

cases = [(293,23),(311,24),(317,25)]
cap = 25
tp = m.theta_powers(cap-1)
cols, labels, v0 = [], [], []
for n in range(1,4):
    base = m.mul(m.power([7,4,16],n,cap),m.power([-1,1],n,cap),cap)
    base = m.mul(base,m.power([1,8],n,cap),cap)
    base = m.pad(m.mul(base,tp[n],cap),cap)
    for j in range(n+1):
        cols.append(m.pad(([Q(0)]*j+base)[:cap],cap))
        labels.append((n,j))
        v0.append(int(base[0]) if j == 0 else 0)
rows = [[col[i] for col in cols] for i in range(cap)]
assert len(labels) == 9
rational_digest = hashlib.sha256(json.dumps(
    [[[v.numerator,v.denominator] for v in row] for row in rows],
    separators=(",",":")).encode()).hexdigest()

reports = []
for p,h in cases:
    assert p in m.primes_to(p)
    field = m.field_rows(rows[:h],p)
    rhs = [-1]+[0]*(h-1)
    actual = m.solve_affine(field,rhs,p,labels,v0)
    encoded = json.dumps({"matrix":field,"rhs":[v%p for v in rhs]},
                         separators=(",",":")).encode()
    reports.append({"p":p,"h":h,"columns":len(labels),
                    "input_sha256":hashlib.sha256(encoded).hexdigest(),
                    **actual})

result = {
    "format":"R799 original kappa-nine cubic contact systems",
    "source_helper_sha256":digest,
    "rational_matrix_sha256":rational_digest,
    "rational_rows":cap,
    "labels":labels,
    "reports":reports,
    "all_inconsistent":all(not r["consistent"] for r in reports),
    "scope":"Only the original full nine-column class F=1+sum_(n=1)^3 [h7(t)(t-1)Y]^n p_n(t), deg p_n<=n, evaluated at rho=d*Theta^17. R799 supplies all-prime geometry and r/k reduction; this script does not claim them.",
    "outputs_persisted":False
}
print(json.dumps(result,separators=(",",":")))
