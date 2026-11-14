#!/usr/bin/env python3
"""R471: exact original connection and complete six-sigma norm-two factor."""
from pathlib import Path
import json
from flint import fmpq as Q, fmpq_poly as P

base = Path(__file__).resolve().parents[1]
X = P([0, 1])
p13 = P([0,Q(10880,14847),Q(-13504,14847),Q(6269,9898),
         Q(-6523,59388),Q(-37,33936)])
p15 = P([0,Q(923,1470),Q(107,5880),Q(11399,15680),
         Q(-15919,94080),Q(-37,53760)])
D2 = X**2+20*X-8
CX = -X*(X-8)**2*D2/560
assert 101*p13-64*p15 == 37*CX
S = P([Q(-128,7),Q(-80,7),Q(-12,7),Q(-53,7),1])
H3 = P([-2048,12032,8128,400,-208,1])
H5 = P([1024,-6784,-14912,-272,272,1])
HX = (5*H3-2*H5)/3
numerator = 6*X*(X+1)*CX.derivative()-(31*X+34)*CX
GX, rem = divmod(numerator, X)
assert rem == 0 and GX == S+HX/560

# Exact division recurrence: r_n=(-1)^(n-1)*psi_n in the fixed sigma sign.
psi5 = 32*(X+1)**2*D2-27*X*(X+4)**3
theta4 = 16*(X+1)*D2**2-3*(X+4)*psi5
six_sigma = 8*(X+1)*D2*(27*X*(X+4)**3*(psi5-4*D2**2)-psi5**2)
assert theta4.degree() == 5 and theta4[5] == 1
assert six_sigma.degree() == 11 and six_sigma[11] == 16
old = json.loads((base/"scripts/check-r466-fixed-two-division-source.json").read_text())
w13, w15 = [P([Q(x) for x in row]) for row in old["source_polynomials"]]
assert 101*w13-64*w15 == Q(-111,280)*six_sigma*theta4**2
assert (101*w13-64*w15)[21] == Q(-222,35)
assert Q(101)*Q(-81328,6363)-Q(64)*Q(-20527,2520) == Q(-3848,5)
data = {
    "normalization": "b=1; all displayed polynomials homogenize exactly in X,b",
    "CX_polynomial_in_sigma34_y_frame": [str(CX[i]) for i in range(6)],
    "GX_polynomial_in_sigma34_x2_frame": [str(GX[i]) for i in range(6)],
    "HX_polynomial_in_sigma34_x2_frame": [str(HX[i]) for i in range(6)],
    "theta4_in_sigma32_x_frame": [str(theta4[i]) for i in range(6)],
    "six_sigma_in_sigma72_frame": [str(six_sigma[i]) for i in range(12)],
    "Wstar_z6": "-222/35",
    "new_arithmetic_projection_z6": "-3848/5",
    "all_polynomial_identities_exact": True,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(data, indent=2)+"\n")
print("Original connection, division recurrence, and complete six-sigma factor passed.")
