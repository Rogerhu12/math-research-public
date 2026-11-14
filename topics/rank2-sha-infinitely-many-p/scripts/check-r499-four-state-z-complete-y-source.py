#!/usr/bin/env python3
"""R499: the new four-state z source, from the complete norm-weighted quarter fibers.

The entire rational fiber numerator is the R465 calculation, retained below.
Its last trace is now weighted by epsilon=(-i)^Norm(4t), with the actual
b=-1 to b=1 CM-period anchor fixing both primitive-quarter classes.
"""
from pathlib import Path
import json, runpy, time
import sympy as sy
from sympy.polys.domains import QQ
from sympy.polys.rings import ring
BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))

def exact_quarter_norm_difference():
    start = time.monotonic()
    field = QQ.algebraic_field(sy.sqrt(3), sy.sqrt(-3))
    ring_x, x = ring("x", field)
    zero, one = ring_x.zero, ring_x.one
    delta = field.from_sympy(sy.sqrt(-3))
    omega = (delta-1)/2
    e = field.from_sympy(-1-sy.sqrt(3))
    h = -field.one
    ebar = 2*h-e
    f2 = e**3+1
    em, en, hm = omega*ebar, omega**2*ebar, omega*h
    k = -3*delta/f2                 # y(m t)=k*y(t), m=2+3 omega
    X, Y = x**3, x**3+1
    R2 = X**2+20*X-8
    ell = 8*Y**2
    xnum = 2*Y*x*(X-8)             # x(2z)=xnum/ell
    tau2 = f2*Y

    def add(a, b):
        return a[0]+b[0], a[1]+b[1]

    def scale(a, c):
        return a[0]*c, a[1]*c

    def mul(a, b):
        return (a[0]*b[0]+a[1]*b[1]*tau2,
                a[0]*b[1]+a[1]*b[0])

    def power(a, n):
        out = one, zero
        while n:
            if n & 1:
                out = mul(out, a)
            a = mul(a, a)
            n //= 2
        return out

    def constant(a):
        return a, zero

    # All factors below are homogeneous numerators after P=[2]z.
    # tau=f*y(z), f*y(2z)=R2*tau/ell.
    u = (f2*ell+3*e*e*(xnum-e*ell)/2, R2)
    nt = (e*xnum*xnum+e*e*xnum*ell+2*ell*ell, -2*R2*ell)
    de, dm = xnum-e*ell, xnum-em*ell
    yt = add((zero, -R2*de**3),
             mul((-f2*ell, R2),
                 add(constant(xnum*de**2), scale(nt, -ell))))
    middle = add(power(nt, 3), constant(-8*de**6))
    p2 = add(add(scale(power(nt, 6), field(7)),
                 scale(power(nt, 3), -4*de**6)), constant(16*de**12))
    um = (k*k*f2*ell+3*em*em*(xnum-em*ell)/2, k*R2)
    nm = (em*xnum*xnum+em*em*xnum*ell+2*ell*ell, -2*k*R2*ell)
    difference = add(constant(en*dm**2), scale(nm, -field.one))
    numerator = power(u, 14)
    for factor in (um, difference, power(nt, 2), yt, middle, p2):
        numerator = mul(numerator, factor)

    c8 = (e-h)/(12*h*h*f2)         # R419 canonical sign, not h-e
    coeff = 3*2**32*c8**7*(7*e**6-4*e**3+16)**2/(k*f2**8)
    root_numerator = x*x-2*hm*x-2*hm*hm
    # Sum over the two signs of f first.
    complete_numerator = numerator[0]*Y**15*R2*root_numerator*coeff*2
    complete_denominator = ell**8*(xnum-h*ell)**7*(xnum-hm*ell)*dm**2*de**25
    quotient, remainder = complete_numerator.div(complete_denominator)
    assert not remainder
    assert quotient.degree() == 67
    four_coeffs = []
    twelve_coeffs = []
    for j in range(69):
        c = field.to_sympy(quotient.get((j,), field.zero))
        # Keep delta fixed. Norm1 has e=-1-sqrt(3), epsilon=-i;
        # Norm3 has e=-1+sqrt(3), epsilon=+i. The CM period anchor is proved in R499.
        conjugate = c.xreplace({sy.sqrt(3): -sy.sqrt(3), sy.I: -sy.I})
        c = sy.expand(-sy.I*(c-conjugate))
        four_coeffs.append(c)
        # sigma^136*x^j has weight 2(j+1) for the mu_3 rotation.
        twelve_coeffs.append(sy.expand(3*c) if j % 3 == 2 else sy.Integer(0))
    print("Complete canonical norm-weighted quarter division, remainder zero;",
          round(time.monotonic()-start, 2), "s", flush=True)
    return four_coeffs, twelve_coeffs


def main():
    four,weighted=exact_quarter_norm_difference()
    values=[sy.expand(-weighted[j]/336) for j in range(2,69,3)]
    Q,Mat=H["Q"],H["Mat"]
    def vector(v):
        return (Mat([[Q(str(sy.simplify(sy.re(c))))] for c in v]),
                Mat([[Q(str(sy.simplify(sy.im(c)/sy.sqrt(3))))] for c in v]))
    def decode(v):
        return tuple(Mat([[Q(x)for x in row]for row in v[k]])for k in("real","delta"))
    M=decode(json.loads((BASE/"notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())["matrix"])
    z=vector(values);I=H["identity"](23)
    assert H["km"](H["kp"](M,9,I),z)==z
    assert H["get_entry"](z,22)==H["fq"](0)
    cur=z;vs=[]
    for j in range(18):vs.append(cur);cur=H["km"](M,cur)
    w=H["fq"](Q(-1,2),Q(1,2));w2=H["fm"](w,w)
    parts={str(e):H["serialize_matrix"](H["eig_project"](M,e,z)) for e in [H["fq"](1),w,w2]}
    # Compare the whole canonical CM19 trace, not a selected eigencoefficient.
    km,ka,ks,kp=(H[k] for k in ("km","ka","ks","kp"))
    fq,fp,entry,serial=(H[k] for k in ("fq","fp","get_entry","serialize_matrix"))
    cm19=json.loads((BASE/"notes/2026-11-14-theta-degree136-cm19-exact.json").read_text())
    N=decode(cm19["matrix"])
    D=ks(km(N,kp(M,16,I)),fp(w,-1))
    assert D==decode(cm19["D33"])
    assert km(D,D)==I and km(M,D)==km(D,M)
    old=json.loads((BASE/"scripts/check-r465-common-six-sigma-true-core-marginal.json").read_text())
    xi,S2=decode(old["Xi_double"]),decode(old["S_double"])
    v=ka(xi,ks(S2,fq(Q(1,4),Q(1,4))))
    assert z==km(D,v)
    assert v==km(D,z)
    positive9=ks(ka(I,kp(M,9,I)),fq(Q(1,2)))
    dminus=ks(ka(I,ks(D,fq(-1))),fq(Q(1,2)))
    dplus=ks(ka(I,D),fq(Q(1,2)))
    assert km(positive9,z)==z and km(positive9,v)==v
    plus,minus=ka(v,z),ka(v,ks(z,fq(-1)))
    def orbit(source,n=9):
        answer=[]
        for j in range(n):
            answer.append(source);source=km(M,source)
        return answer
    dimensions={
        "positive_N7_ninth":H["rank"](positive9),
        "positive_D_plus":H["rank"](km(positive9,dplus)),
        "positive_D_minus":H["rank"](km(positive9,dminus)),
        "v_orbit":H["rank"](H["cols"](orbit(v))),
        "z_orbit":H["rank"](H["cols"](orbit(z))),
        "v_plus_z_orbit":H["rank"](H["cols"](orbit(plus))),
        "v_minus_z_orbit":H["rank"](H["cols"](orbit(minus))),
        "joint_v_z_orbits":H["rank"](H["cols"](orbit(v)+orbit(z))),
    }
    assert list(dimensions.values())==[17,9,8,9,9,9,8,17]
    bridge=json.loads((BASE/"scripts/check-r476-full-xi-wstar-bridge.json").read_text())
    href=decode(bridge["reference_mass_one"])
    coeff=km(decode(bridge["coefficient_dual"]),km(dminus,z))
    expected=[fq(Q(1,2016),Q(1,2016))]
    expected += [H["fn"](tuple(Q(x) for x in c)) for c in bridge["bridge_polynomial_coefficients"]]
    assert all(entry(coeff,j)==c for j,c in enumerate(expected))
    assert km(decode(bridge["eight_source_basis"]),coeff)==km(dminus,z)
    one=H["eig_project"](M,fq(1),I)
    assert km(km(dminus,one),z)==ks(href,expected[0])
    new=decode(json.loads((BASE/"scripts/check-r470-original-negative-source-new-line.json").read_text())["Snew"])
    new_projection=km(km(dminus,H["eig_project"](M,w2,I)),z)
    assert new_projection==ks(new,fq(Q(-52,3)))
    rational_rank_table=[]
    for name,e in [("1",fq(1)),("omega",w),("omega_squared",w2)]:
        E=km(positive9,H["eig_project"](M,e,I))
        rational_rank_table.append({"eigenvalue":name,"total":H["rank"](E),
            "D_plus":H["rank"](km(E,dplus)),"D_minus":H["rank"](km(E,dminus))})
    out={"field":"Q(delta), delta^2=-3; b=1; canonical period Omega=i*Omega_for_b_minus_1",
         "normalization":"z=q-h/2; zY(2z)=-sum_primitive epsilon(t)*raw_six_sigma/336",
         "basis":"sigma136*x2*X^j, j=0,...,22",
         "norm1_quarter_x":"-1-sqrt(3)","norm3_quarter_x":"-1+sqrt(3)",
         "z_double":H["serialize_matrix"](z),
         "whole_N7_9_eigenvalue":1,"cyclic_dimension":H["rank"](H["cols"](vs)),
         "rational_CM7_eigenparts":parts,
         "D33":serial(D),"full_identity":"z_Y = D33 v_Y in all 23 coordinates",
         "v_double":serial(v),"v_plus_z":serial(plus),"v_minus_z":serial(minus),
         "cyclic_dimensions":dimensions,"positive_rational_eigen_rank_table":rational_rank_table,
         "D_minus_z_eight_coefficients_b1":[[str(x) for x in c] for c in expected],
         "reference_coefficient_general_b":"(1+delta)/(2016*b)",
         "new_projection_coefficient":"-52/3","new_projection":serial(new_projection),
         "norm_weighted_four_point_raw_x":H["serialize_matrix"](vector(four)),
         "all_fiber_remainders_zero":True}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
    print("New z entire Y source computed; CM7 cyclic dimension",out["cyclic_dimension"],flush=True)
if __name__=="__main__":main()
