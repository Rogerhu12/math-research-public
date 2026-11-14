#!/usr/bin/env python3
"""R321 exact original U-frame primitives and their six paid CM sources.

No prime scan or repetition of R324's five-block computation.
"""
from pathlib import Path
import json
import sympy as s

X, b, T, x, q = s.symbols("X b T x q")
R = s.Rational
checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


P = {
    1: X**4-R(53,7)*b*X**3-R(12,7)*b**2*X**2-R(80,7)*b**3*X-R(128,7)*b**4,
    3: X**5-208*b*X**4+400*b**2*X**3+8128*b**3*X**2+12032*b**4*X-2048*b**5,
    5: X**5+272*b*X**4-272*b**2*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5,
}
B = {
    1: -R(3,448)*X**2/b-X/28+b/14,
    3: -X**2/4+28*b*X+8*b**2,
    5: -X**2/4-38*b*X-4*b**2,
}
a = {1: -R(3,448)/b, 3: R(3,4), 5: R(3,4)}
c = {1: -R(3,112), 3: -9*b, 5: 9*b}
PU = X*(X-8*b)**4
PV = X*(X-8*b)**3


def reduction(poly):
    return s.expand(6*X*(X+b)*(X-8*b)*s.diff(poly,X)
                    -(13*X**2+8*b*X-32*b**2)*poly)


cols = [reduction(X**j) for j in range(3)] + [X*(X-8*b)**3, X*(X-8*b)**2]
M = s.Matrix([[s.expand(col).coeff(X,k) for col in cols] for k in range(5)])
check("actual five-dimensional reduction determinant",
      s.factor(M.det()) == -2**14*3**6*b**6)
check("actual U is the original three-source combination",
      s.expand((-336*b*P[1]+5*P[3]+4*P[5])/9-PU) == 0)
for i in (1,3,5):
    check("original polynomial shares the actual six-torsion factor " + str(i),
          s.rem(P[i],X-8*b,X) == 0)
    check("complete U primitive, holomorphic and logarithmic terms " + str(i),
          s.cancel(P[i]-(X-8*b)*reduction(B[i])-a[i]*PU-c[i]*PV) == 0)
    check("original first derivative and mass compensation " + str(i),
          s.simplify(-s.expand(B[i]).coeff(X,2)+a[i]-(0 if i == 1 else 1)) == 0)

RX = -(X-8*b)**2*(X**2+20*b*X-8*b**2)/(560*b)
LF = lambda poly: s.expand(6*X*(X+b)*s.diff(poly,X)-(25*X+28*b)*poly)
LU = lambda poly: s.cancel(LF(poly)-192*b*(X+b)*poly/(X-8*b))
BU = P[1]/5+P[3]/(1680*b)+P[5]/(840*b)
BF = P[1]+P[3]/(336*b)-P[5]/(840*b)
check("same pure companion returns through F", s.cancel(LF(RX)-BF) == 0)
check("same pure companion returns through U", s.cancel(LU(RX)-BU) == 0)
check("the two complete returns isolate H5", s.cancel(BF-5*BU+P[5]/(140*b)) == 0)
check("same companion is the sum of the two U primitives",
      s.expand((X-8*b)**2*(B[3]+B[5])-280*b*RX) == 0)
check("original U combination has zero rational primitive",
      s.expand(-336*b*B[1]+5*B[3]+4*B[5]) == 0)
check("original U combination has zero logarithmic residue",
      s.expand(-336*b*c[1]+5*c[3]+4*c[5]) == 0)
check("original U combination has exactly mass one",
      s.simplify((-336*b*a[1]+5*a[3]+4*a[5])/9) == 1)

# A genuine Miller function at P=(2q,3), q^3=1.  The logarithmic derivative
# below is obtained after using y^2=x^3+1, not by choosing an approximate point.
m = 2*q**2
raw = (6*m*x**3-18*x**2-12*m)/(x**3+1-(m*x-1)**2)+6/x
expected = 12*q**2+36/(x-2*q)
numerator = s.fraction(s.cancel(raw-expected))[0]
check("all three exact Miller logarithmic derivatives",
      s.rem(s.Poly(numerator,q),s.Poly(q**3-1,q)).as_expr() == 0)
check("tangent third intersection is minus twice the original point",
      s.rem(s.Poly((m*m-4*q),q),s.Poly(q**3-1,q)).as_expr() == 0)
w = s.symbols("omega")
resolvent = sum(w**j/(x-2*w**j) for j in range(3))-12/(x**3-8)
numerator = s.fraction(s.together(resolvent))[0]
check("original six-torsion logarithmic resolvent",
      s.rem(s.Poly(numerator,w),s.Poly(w*w+w+1,w)).as_expr() == 0)
check("actual linear normalization of the logarithmic primitive", R(3*12,432) == R(1,12))

# The complete odd six sources of R311, in the same normalization Y_j'=1.
plus = [-R(1024,17)*(5*T*T-T-8),-R(256,17)*(53*T*T-133*T-180),
        -R(256,17)*(66*T*T-105*T-58),-R(16,17)*(605*T*T+338*T-1019),
        -R(4,17)*(308*T*T-184*T-537),-1]
minus = [-512*T*(T-2),-256*(8*T*T-7*T-11),-32*(69*T*T-3*T-253),
         -16*(20*T*T+68*T-165),2*(176*T*T-208*T-227),-1]
dplus = {1:-(5*T*T-T-31)/12096,3:-(T*T-5*T+1)/36,5:-(2*T-3)/12}
dminus = {1:(T+1)**2/6048,3:(T+1)**2/18,5:-(T+1)**2/18}
traces = [3,0,6,3,18]


def tr(poly):
    return sum(s.expand(poly).coeff(T,j)*traces[j] for j in range(5))


for i in (1,3,5):
    original = s.expand(X*(X-8)**2*B[i].subs(b,1))
    actual = sum((tr(dplus[i]*plus[j])+tr(dminus[i]*minus[j]))*X**j for j in range(6))
    check("complete original six-source decomposition " + str(i), s.expand(original-actual) == 0)
    check("complete six-source first mass " + str(i),
          s.simplify(tr(dplus[i])+tr(dminus[i])+B[i].subs(b,1).coeff(X,2)) == 0)
    check("no missing plus CM embedding " + str(i), s.gcd(s.Poly(dplus[i],T),s.Poly(T**3-3*T-1,T)).degree() == 0)
    check("no missing minus CM embedding " + str(i), s.gcd(s.Poly(dminus[i],T),s.Poly(T**3-3*T-1,T)).degree() == 0)
check("pure companion cancels exactly the other three CM sources", s.expand(dminus[3]+dminus[5]) == 0)
check("pure companion retains exactly the original plus trace",
      s.expand(dplus[3]+dplus[5]+(T*T+T-8)/36) == 0)

# The new four-factor row is a homogeneous linear weight on the same kernel.
x1,x2,x3,x4 = s.symbols("x1 x2 x3 x4")
weightF = -16*x1+2*x2+2*x3+4*x4
weightU = -2*x2-2*x3+4*x4
check("second four-factor row retains the entire original derivative",
      s.expand((x1+2*x2+2*x3+4*x4)-(x1+4*x2+4*x3)-weightU) == 0)
check("both complete four-factor rows have zero theta translation anomaly",
      all(2*f.coeff(x1)+4*f.coeff(x2)+4*f.coeff(x3)+4*f.coeff(x4) == 0 for f in (weightF,weightU)))
check("H5 four-factor first mass", s.expand(weightF-5*weightU).coeff(x4) == -16)

data = {
    "status":"PASS", "checks":checks,
    "actual_quotient_space":"span(1,1/X,1/(X-8b),1/(X-8b)^2,1/(X-8b)^3)",
    "integral_reduction_determinant":"-2^14*3^6*b^6",
    "primitive_shape":"D_i=sigma^34*x^3*y*(X-8b)^2*B_i(X)",
    "primitive_polynomials":{str(i):str(B[i]) for i in (1,3,5)},
    "holomorphic_constants":{str(i):str(a[i]) for i in (1,3,5)},
    "logarithmic_constants":{str(i):str(c[i]) for i in (1,3,5)},
    "normalized_six_torsion_primitive":"L6=sum_j omega^j*log(f_j)/(432*theta^7)-z/(12b); L6'=1/(X-8b), L6(0)=0",
    "Miller_divisor":"div(f_j)=6(P_j)-6(-P_j); f_j(O)=1",
    "Miller_log_derivative":"12*theta*omega^(2j)+36*theta^3/(x-2*theta^2*omega^j)",
    "six_source_coefficients_at_b1":{str(i):{"plus":str(dplus[i]),"minus":str(dminus[i])} for i in (1,3,5)},
    "six_source_b_scaling":{"1":"divide both coefficients by b","3":"unchanged","5":"unchanged"},
    "second_original_four_factor_weight":"4*x4-2*x2-2*x3",
    "second_original_source":"H1/5+H3/(1680b)+H5/(840b)",
    "same_companion_relation":"D3+D5=280b*C_X; -336b*D1+5D3+4D5=0",
    "inert_reference":"R324 supplies the complete original integrality and first forced row; it is not re-tested here.",
    "central_scope":"All exact, logarithmic, Gaussian, tame-one and additive carry terms are retained."
}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(f"PASS: {len(checks)} exact checks; {out.name}")
