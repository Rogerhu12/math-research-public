"""Exact polynomial certificate for the fixed physical S3 phase block."""
import hashlib
import json
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parent
source = root / '2026-11-14-odd-five-bit-phase-limit-diagnostic-789f.json'
record = json.loads(source.read_text())
x, u, v = sp.symbols('x u v')
trace = sp.sympify(record['trace'], locals={'x': x})
sums = [sp.Integer(2), u]
for k in range(2, 7):
    sums.append(sp.expand(u * sums[-1] - sums[-2]))
p = sum(c * sums[k] for k, c in [(6, 27), (5, 473), (4, 2766),
                                (3, 9133), (2, 20997), (1, 34762)]) + 43684
d = 3 * (u + 3) * (u + 4)**2 * (3*u + 4)**3
assert sp.cancel(trace - (2*p/d).subs(u, x + 1/x)) == 0
denominator = sp.Poly(sp.expand(d.subs(u, v+2)), v)
margin = sp.Poly(sp.expand((d-2*p).subs(u, v+2)), v)
three_quarters = sp.Poly(4*margin.as_expr()-denominator.as_expr(), v)
assert all(c > 0 for c in three_quarters.all_coeffs())
result = {
    'status': 'exact-positive-coefficient-certificate',
    'scope': 'Complete two-dimensional S3-invariant lower primitive block for old weights (r,r^-1,1,1,1); not other S3 types or arbitrary weights.',
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'substitution': 'x=r^2>0, v=x+x^-1-2>=0',
    'denominator_factorization': '3*(v+5)*(v+6)^2*(3*v+10)^3',
    'denominator_ascending': list(map(int, reversed(denominator.all_coeffs()))),
    'one_minus_trace_numerator_ascending': list(map(int, reversed(margin.all_coeffs()))),
    'four_times_three_quarters_margin_numerator_ascending': list(map(int, reversed(three_quarters.all_coeffs()))),
    'exact_original_trace_identity_verified': True,
    'strict_trace_upper_bound': '3/4',
    'physical_positive_operator_upper_bound': 'K < (3/4) I on the stated two-dimensional physical block',
    'finite_weak_bit_corollary': 'For each fixed r>0, all sufficiently small a>0 give phase <=7/8 on the entire three-dimensional S3-invariant primitive source of (r,r^-1,1,1,1,a); threshold may depend on r.',
    'general_phase_bound_proved': False
}
(root / '2026-11-14-odd-five-bit-s3-phase-trace-budget-789f.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
