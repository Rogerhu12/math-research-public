#!/usr/bin/env python3
"""The two actual delta words of the four-sigma degree102 source.
Exact rational function operations only; no new CM spectrum or p scan.
"""
import hashlib
import json
import os
import time
from fractions import Fraction as F
from math import comb
from pathlib import Path

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

def clean(a):
    return {int(k):F(v) for k,v in a.items() if v}

def pseq(a):
    return clean(dict(enumerate(a)))

ZERO = {}
ONE = {0:F(1)}
H = {1:F(1)}
KREL = {2:F(-2),3:F(1)}  # t=x*kappa; t^3=h^2(h-2)

def add(a,b):
    r=dict(a)
    for k,v in b.items():
        r[k]=r.get(k,F(0))+v
    return clean(r)

def scale(a,c):
    return clean({k:v*F(c) for k,v in a.items()})

def mul(a,b):
    r={}
    for i,x in a.items():
        for j,y in b.items():
            r[i+j]=r.get(i+j,F(0))+x*y
    return clean(r)

def power(a,n):
    assert n>=0
    r=ONE
    while n:
        if n&1:
            r=mul(r,a)
        n//=2
        if n:
            a=mul(a,a)
    return r

def shift(a,n):
    return {k+n:v for k,v in a.items()}

def kmake(a=None,b=None,c=None):
    return (a or {}, b or {}, c or {})

KZERO=kmake()
KONE=kmake(ONE)

def kadd(a,b):
    return tuple(add(a[i],b[i]) for i in range(3))

def kscale(a,c):
    return tuple(scale(x,c) for x in a)

def kmul(a,b):
    r=[{}, {}, {}]
    for i in range(3):
        for j in range(3):
            w=mul(a[i],b[j])
            k=i+j
            if k>=3:
                k-=3
                w=mul(w,KREL)
            r[k]=add(r[k],w)
    return tuple(r)

def kpower(a,n):
    assert n>=0
    r=KONE
    while n:
        if n&1:
            r=kmul(r,a)
        n//=2
        if n:
            a=kmul(a,a)
    return r

def kpole_value(a):
    return [None if not c else [min(c),max(c)] for c in a]

def polynomial_list(a, length=None):
    assert not a or min(a)>=0
    n=(max(a)+1 if a else 0) if length is None else length
    assert not a or max(a)<n
    return [str(a.get(k,F(0))) for k in range(n)]

def laurent_list(a):
    return [[k,str(v)] for k,v in sorted(a.items())]

def digest(a):
    data=json.dumps(a,sort_keys=True,separators=(",",":")).encode()
    return hashlib.sha256(data).hexdigest()

def subst_y_squared_minus_one(a):
    # a is a polynomial in v=y^2; return a(X+1).
    r={}
    for j,c in a.items():
        r=add(r,scale(power({0:F(1),1:F(1)},j),c))
    return r

def reflect_y(a):
    return {j:(-1)**j*c for j,c in a.items()}

def halfperiod_over_sqrt3(p):
    # Exact R1021/R967 q_e^2=e^2(x-e)/sqrt3, e^3=-1.
    # Source convention: -sigma^34*x*y*p(X).
    # This is (sum_e T_e)/sqrt3 on the complete five-dimensional type5 space.
    assert not p or (min(p)>=0 and max(p)<=4)
    r={}
    for j,c in p.items():
        a,b=1+3*j,14-3*j
        for u in range(a+1):
            for v in range(b+1):
                ke=1+u+v
                if ke%3:
                    continue
                ex=15-u-v
                assert ex>=1 and (ex-1)%3==0
                index=(ex-1)//3
                term=-c*((-1)**j)*comb(a,u)*(2**u)*comb(b,v)*((-1)**v)
                term*=F(3*((-1)**(ke//3)),3**8)
                r[index]=r.get(index,F(0))+term
    return clean(r)

def span_two(p,v0,v1):
    # Both prescribed vectors have coefficient X^4=1.
    c4=p.get(4,F(0)); c3=p.get(3,F(0))
    a=F(11*c3+109*c4,252)
    b=c4-a
    residue=add(p,scale(add(scale(v0,a),scale(v1,b)),-1))
    return a,b,residue

def run(request=None):
    started=time.monotonic()
    request=request or {}
    U=kmake(pseq([-4,18,-9]),pseq([12,-9]),{-1:F(6),0:F(-9)})
    Ui=kmake({0:F(-1,4)},{0:F(3,8)},{-1:F(-3,8)})
    assert kmul(U,Ui)==KONE
    assert kmul(Ui,U)==KONE

    # R1038 actual complete factored source:
    # F0/(273 delta)=sigma^102*x*R16(X).
    factors=[
        pseq([4,1]),
        pseq([16,-4,7]),
        pseq([64,48,-96,1]),
        pseq([256,1024,1536,52,13]),
        pseq([4096,-49152,-189696,-123136,-5808,564,1]),
    ]
    R16=ONE
    for fac in factors:
        R16=mul(R16,fac)
    R16=scale(R16,F(1,91))
    assert max(R16)==16 and R16[16]==1

    # Keep all seventeen coefficients, all three Kummer words, both directions.
    powers={0:KONE}
    for j in range(1,6):
        powers[j]=kmul(powers[j-1],U)
    for j in range(1,12):
        powers[-j]=kmul(powers[-j+1],Ui)
    f=KZERO
    for j,c in R16.items():
        f=kadd(f,kscale(powers[j-11],-c/F(3**17)))
    A0,A1,A2=f
    assert A0=={}  # the previously proved entire delta trace, independently returned
    assert A1 and A2
    assert min(A1)>=0 and max(A1)<=10
    assert min(A2)>=-1 and max(A2)<=9

    # Two complete Miller-standardized functions.
    # h1=(1-y)^-11; h2=x^2/(1+y)^12.
    # Multiply by h_i and translate by R1=S, R2=-S.
    # Q1=x*B1(y), Q2=x*B2(y).
    yp={0:F(1),1:F(1)}
    ym={0:F(-1),1:F(1)}
    B1={}
    for e,c in A1.items():
        B1=add(B1,scale(power(yp,10-e),-2*c*(F(4)**(e-11))))
    B2={}
    for e,c in A2.items():
        term=mul(power(ym,9-e),power(yp,e+1))
        B2=add(B2,scale(term,c*(F(2)**e)/F(2**20)))
    assert max(B1)<=10 and max(B2)<=10
    assert B2==reflect_y(B1)
    # Independently proved in the source note from U^-11 and R16'(-4).
    assert sum(B1.values(), F(0)) == -F(1,1092)
    assert sum(((-1)**j)*c for j,c in B1.items()) == -F(1,1092)

    # Exact inverse of the complete first Miller return:
    # A1(h)=-2*h^10*B1(4/h-1).
    inverse={}
    four_over_h_minus_one={-1:F(4),0:F(-1)}
    for j,c in B1.items():
        inverse=add(inverse,scale(shift(power(four_over_h_minus_one,j),10),-2*c))
    assert inverse==A1

    # Second return is verified as an independent polynomial identity:
    # B2 from A2 above, and evenness of the actual original F0:
    # A2(h)=-A1(2-h)/h.
    two_minus_h={0:F(2),1:F(-1)}
    expected_A2={}
    for j,c in A1.items():
        expected_A2=add(expected_A2,scale(shift(power(two_minus_h,j),-1),-c))
    assert A2==expected_A2

    # Reconstruct the original full F0 from both returned words, not a few jets.
    restored=kmake({},inverse,expected_A2)
    assert restored==f
    full_numerator=kpower(U,11)
    full_numerator=kmul(full_numerator,kscale(restored,-F(3**17)))
    expected=KZERO
    for j,c in R16.items():
        expected=kadd(expected,kscale(kpower(U,j),c))
    assert full_numerator==expected

    even_in_y2={j//2:c for j,c in B1.items() if j%2==0}
    odd_over_y={((j-1)//2):c for j,c in B1.items() if j%2}
    even_X=subst_y_squared_minus_one(even_in_y2)
    odd_X=scale(subst_y_squared_minus_one(odd_over_y),-1)
    # Actual odd source is -sigma^34*x*y*odd_X.
    assert max(even_X,default=-1)<=5 and max(odd_X,default=-1)<=4

    vminus=pseq([64,-104,-156,13,1])
    vomega=pseq([F(128,11),F(368,11),F(120,11),F(-109,11),1])
    Hminus=halfperiod_over_sqrt3(vminus)
    Homega=halfperiod_over_sqrt3(vomega)
    sign=None
    for e in [1,-1]:
        if Hminus==scale(vminus,e) and Homega==scale(vomega,e):
            sign=e
    assert sign is not None
    Hcols=[halfperiod_over_sqrt3({j:F(1)}) for j in range(5)]
    for j in range(5):
        assert halfperiod_over_sqrt3(Hcols[j])=={j:F(1)}
    Hp=halfperiod_over_sqrt3(odd_X)
    good=scale(add(odd_X,scale(Hp,sign)),F(1,2))
    other=add(odd_X,scale(good,-1))
    a,b,rem=span_two(good,vminus,vomega)
    assert not rem
    assert add(good,other)==odd_X
    assert halfperiod_over_sqrt3(good)==scale(good,sign)
    assert halfperiod_over_sqrt3(other)==scale(other,-sign)

    # Read the actual covariant derivative of the original S34 as a full polynomial.
    S=pseq([F(-128,7),F(-80,7),F(-12,7),F(-53,7),1])
    derivative={j:-(4+6*j)*c for j,c in S.items()}
    Hder=halfperiod_over_sqrt3(derivative)
    derivative_good=scale(add(derivative,scale(Hder,sign)),F(1,2))
    derivative_other=add(derivative,scale(derivative_good,-1))
    da,db,drem=span_two(derivative_good,vminus,vomega)
    assert not drem
    proportional=None
    derivative_remainder={}
    if derivative_other:
        index=next(iter(derivative_other))
        ratio=other.get(index,F(0))/derivative_other[index]
        residue=add(other,scale(derivative_other,-ratio))
        derivative_remainder=residue
        if not residue:
            proportional=ratio

    canonical_factorized_source=polynomial_list(R16,17)
    result={
        "status":"PASS",
        "mathematical_source":"R1038 (complete four-sigma quotient, with original delta phases)",
        "normalizations":{
            "F0":"sigma(7z)*sigma(pi z)*sigma(barpi z)*sigma(3delta z)",
            "f":"F0/(273delta*sigma(delta z)^34)",
            "kappa":"-(y_up+delta)/(delta*x_up); kappa^3=1-y_target",
            "deck":"u_delta=(0,-1), kappa(P+u_delta)=omega*kappa(P)",
            "t":"x_target*kappa; t^3=h^2(h-2)",
            "Ri":["S=(0,1)","-S=(0,-1)"],
            "Miller":["h1=(1-y)^-11","h2=x^2/(1+y)^12"],
            "standardization":"Qi=(fi*hi) composed with t_Ri",
            "word_sources":["sigma^34*x*B(y)","sigma^34*x*B(-y)"],
            "full_degree126_factor_retained":"sigma(2Q)^2/(-3276delta), Q=delta P",
        },
        "R16_full_ascending":canonical_factorized_source,
        "R16_sha256":digest(canonical_factorized_source),
        "three_Kummer_coefficients":[laurent_list(a) for a in f],
        "Kummer_coefficient_pole_windows":kpole_value(f),
        "B_full_y_ascending":polynomial_list(B1,11),
        "B_sha256":digest(polynomial_list(B1,11)),
        "complete_word_reflection_and_reconstruction":True,
        "even_type2_polynomial_X_ascending":polynomial_list(even_X,6),
        "odd_type5_polynomial_in_negative_xy_basis":polynomial_list(odd_X,5),
        "full_type5_halfperiod_matrix_columns":[polynomial_list(c,5) for c in Hcols],
        "known_R735_two_line_halfperiod_sign":sign,
        "actual_two_rank_one_component":{
            "D_minus_coefficient":str(a),
            "D_omega_coefficient":str(b),
            "whole_vector":polynomial_list(good,5),
            "nonzero":bool(good),
        },
        "complete_other_type5_component":{
            "whole_vector":polynomial_list(other,5),
            "nonzero":bool(other),
        },
        "actual_covariant_original_S34_derivative":{
            "whole_vector":polynomial_list(derivative,5),
            "two_line_coefficients":[str(da),str(db)],
            "complete_other_vector":polynomial_list(derivative_other,5),
            "new_other_proportional_to_this":None if proportional is None else str(proportional),
            "full_proportionality_remainder":polynomial_list(derivative_remainder,5),
        },
        "no_new_central_zero_assigned_to_words_or_projections":True,
        "no_unit_cut_or_Miller_factor_removed":True,
        "mathematical_computation_scope":"one fixed rational three-word return and complete five-dimensional dyadic action",
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "generated_files_written":False,
        "elapsed_seconds":time.monotonic()-started,
    }
    data=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    assert len(data)<60000
    return result

if __name__=="__main__":
    print(json.dumps(run(),sort_keys=True,separators=(",",":")))
