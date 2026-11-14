#!/usr/bin/env python3
"""Exact algebra and certified complex intervals for R253; no target-p scan."""
import json
from pathlib import Path
import sympy as s
from flint import acb, acb_poly, arb, ctx

x, t = s.symbols("x t")
I = s.I
Kraw = s.Poly(
    (4-I)*x**8 + (-12+20*I)*x**6 + (28+10*I)*x**4
    + (-20-12*I)*x**2-I, x, domain=s.QQ_I
)
K = Kraw.monic()
f = s.Poly(
    t**8+(8-4*I)*t**7+(-4+8*I)*t**6+(-8-12*I)*t**5
    +(-10-48*I)*t**4+(-8-12*I)*t**3+(-4+8*I)*t**2
    +(8-4*I)*t+1, t, domain=s.QQ_I
)
checks = {}

def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)

transform = s.Poly(
    s.expand(sum(c*(1+t)**j*(1-t)**(8-j)
                 for (j,), c in Kraw.terms())/(16*I)),
    t, domain=s.QQ_I
)
check("relative_unit_polynomial", transform == f)
check("monic_and_constant_one", f.LC() == 1 and f.TC() == 1)
absolute = s.Poly(
    s.expand(f.as_expr()*s.conjugate(f.as_expr()).subs(s.conjugate(t),t)),
    t, domain=s.ZZ
)
check("absolute_monic_integral_unit", absolute.LC() == 1 and absolute.TC() == 1)

f5 = s.Poly(f.as_expr().subs(I,3), t, modulus=5)
target5 = s.Poly(t**8+t**7+t**5+t**4+t**3+t+1,t,modulus=5)
check("reduction_at_5_i3", f5 == target5)

def modpow(base, exponent, modulus):
    answer = s.Poly(1,t,modulus=5)
    while exponent:
        if exponent & 1:
            answer=(answer*base).rem(modulus)
        base=(base*base).rem(modulus)
        exponent >>= 1
    return answer

frob4=modpow(s.Poly(t,t,modulus=5),5**4,f5)
frob8=modpow(s.Poly(t,t,modulus=5),5**8,f5)
diff=frob4-s.Poly(t,t,modulus=5)
aa,bb,gg=s.gcdex(f5,diff)
check("rabin_frobenius_degree8", frob8 == s.Poly(t,t,modulus=5))
check("rabin_no_degree_dividing4", gg == s.Poly(1,t,modulus=5))
check("rabin_bezout", aa*f5+bb*diff == gg)

U=x*x
num=s.Poly(x*(U**4+12*U**3+30*U**2-36*U+9),x,domain=s.QQ_I)
den=s.Poly((3*U**2-6*U-1)**2,x,domain=s.QQ_I)
g=(num*s.invert(den,K)).rem(K)
g_claim=s.Poly(
    (-2+I/2)*x**7+(6-10*I)*x**5+(-14-5*I)*x**3
    +(10+13*I/2)*x,x,domain=s.QQ_I
)
check("actual_triplication_reduction",g == g_claim)
check("triplication_preserves_kernel", K.compose(g).rem(K).is_zero)
v=s.Poly(x,x,domain=s.QQ_I)
orbit=[]
for j in range(8):
    orbit.append(v)
    v=v.compose(g).rem(K)
check("g_fourth_is_minus_x", orbit[4] == -orbit[0])
check("g_eighth_is_x", v == orbit[0])
check("eight_distinct_orbit_functions",
      len({str(z.as_expr()) for z in orbit}) == 8)

ctx.prec=256
poly=acb_poly([
    -acb(0,1),0,acb(-20,-12),0,acb(28,10),0,
    acb(-12,20),0,acb(4,-1)
])
roots=poly.roots(tol=arb(2)**-180,maxprec=1024)
check("all_eight_roots_isolated",len(roots)==8)
selected=[
    z for z in roots
    if z.real > arb(-22533)/10000 and z.real < arb(-22532)/10000
    and z.imag > arb(11246)/10000 and z.imag < arb(11247)/10000
]
check("unique_root_in_rational_box",len(selected)==1)
z=selected[0]
root_box=str(z)
logs=[]
units=[]
for j in range(4):
    rr=(z-1)/(z+1)
    units.append(str(rr))
    logs.append(abs(rr).log())
    Z=z*z
    z=z*(Z**4+12*Z**3+30*Z**2-36*Z+9)/(3*Z**2-6*Z-1)**2

bounds=[(7149,7151),(6330,6332),(-22928,-22927),(-1882,-1880)]
for j,(lo,hi) in enumerate(bounds):
    check("log_interval_"+str(j),
          logs[j]>arb(lo)/10000 and logs[j]<arb(hi)/10000)
margin=abs(logs[2])-abs(logs[0])-abs(logs[1])-abs(logs[3])
check("strict_dominance_exceeds_three_quarters",margin>arb(3)/4)
check("rational_interval_dominance",
      s.Rational(22927-7151-6332-1882,10000)>s.Rational(3,4))

for k in [1,3,5,7]:
    check("octic_i_character_minus_one_"+str(k),(12*k)%8 == 4)
check("norm5_residue_pi",pow(3,15,17)==6)
check("norm5_residue_barpi",pow(3,6,17)==15)

output={
    "status":"PASS",
    "kind":"Exact rational algebra plus certified Arb root isolation; no target-prime scan",
    "checks":checks,
    "relative_unit_polynomial":str(f.as_expr()),
    "absolute_unit_polynomial":str(absolute.as_expr()),
    "mod5_polynomial":str(f5.as_expr()),
    "mod5_frobenius_four":str(frob4.as_expr()),
    "mod5_frobenius_eight":str(frob8.as_expr()),
    "mod5_bezout_a":str(aa.as_expr()),
    "mod5_bezout_b":str(bb.as_expr()),
    "triplication_polynomial":str(g.as_expr()),
    "precision_bits":ctx.prec,
    "isolated_x":root_box,
    "four_units":units,
    "four_log_absolute_values":[str(z) for z in logs],
    "rational_log_intervals_numerators":bounds,
    "rational_log_intervals_denominator":10000,
    "dominance_margin":str(margin),
    "strict_rational_lower_bound":str(s.Rational(3781,5000)),
    "permuted_diagonal_columns":[2,1,0,3],
    "octic_character_exponents":[1,3,5,7]
}
destination=Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n")
print("PASS:",len(checks),"exact/interval checks;",destination.name)
