#!/usr/bin/env python3
"""Exact local algebra certificate for R96; Python standard library only.

The proof of the Galois/inertia implications is in R96.  This program verifies
the polynomial identities, the Eisenstein transformations and every leading
residue used there.  It does not replace an infinite statement by a numerical
search through elliptic curves.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

class Poly:
    """Sparse Q[a,b,c], sufficient for the identities below."""
    def __init__(self,terms=None):
        if isinstance(terms,Poly):
            self.terms=dict(terms.terms)
        elif isinstance(terms,dict):
            self.terms={m:Fraction(v) for m,v in terms.items() if v}
        else:
            value=Fraction(0 if terms is None else terms)
            self.terms={(0,0,0):value} if value else {}
    @classmethod
    def variable(cls,index):
        m=[0,0,0]; m[index]=1
        return cls({tuple(m):1})
    def __add__(self,other):
        other=Poly(other); result=dict(self.terms)
        for m,c in other.terms.items():
            result[m]=result.get(m,0)+c
        return Poly(result)
    __radd__=__add__
    def __neg__(self):
        return Poly({m:-c for m,c in self.terms.items()})
    def __sub__(self,other): return self+(-Poly(other))
    def __rsub__(self,other): return Poly(other)-self
    def __mul__(self,other):
        other=Poly(other); result={}
        for m,c in self.terms.items():
            for n,d in other.terms.items():
                k=tuple(x+y for x,y in zip(m,n))
                result[k]=result.get(k,0)+c*d
        return Poly(result)
    __rmul__=__mul__
    def __pow__(self,exponent):
        assert isinstance(exponent,int) and exponent>=0
        answer,base=Poly(1),self
        while exponent:
            if exponent&1: answer*=base
            base*=base; exponent//=2
        return answer
    def __truediv__(self,scalar):
        scalar=Fraction(scalar); assert scalar
        return Poly({m:c/scalar for m,c in self.terms.items()})
    def __eq__(self,other): return self.terms==Poly(other).terms
    def value(self,*values):
        assert len(values)==3
        return sum(c*values[0]**m[0]*values[1]**m[1]*values[2]**m[2]
                   for m,c in self.terms.items())
    def mod3(self):
        result={}
        for m,c in self.terms.items():
            assert c.denominator%3
            v=c.numerator*pow(c.denominator,-1,3)%3
            if v: result[m]=v
        return result

def disc(a,b,c):
    """Discriminant of X^3 + a X^2 + b X + c."""
    return a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c

def squared_coefficients(a,b,c):
    """Polynomial of y^2/3, given y^3+a y^2+b y+c=0."""
    return ((2*b-a*a)*Fraction(1,3),(b*b-2*a*c)*Fraction(1,9),
            -c*c*Fraction(1,27))

def multiply_mod_f(left,right,a,b,c):
    coefficients=[Poly(0) for _ in range(5)]
    for i,x in enumerate(left):
        for j,y in enumerate(right):
            coefficients[i+j]+=x*y
    for i in (4,3):
        x=coefficients[i]
        coefficients[i-1]-=a*x
        coefficients[i-2]-=b*x
        coefficients[i-3]-=c*x
    return coefficients[:3]

def vp(integer,prime=3):
    integer=Fraction(integer); assert integer
    numerator,denominator=abs(integer.numerator),integer.denominator
    answer=0
    while numerator%prime==0: numerator//=prime; answer+=1
    while denominator%prime==0: denominator//=prime; answer-=1
    return answer

def eisenstein3(coefficients):
    assert all(Fraction(x).denominator==1 for x in coefficients)
    return all(int(x)%3==0 for x in coefficients) and int(coefficients[-1])%9!=0

def leading_mod3(integer,exponent):
    scaled=Fraction(integer)/3**exponent
    assert scaled.denominator%3
    return scaled.numerator*pow(scaled.denominator,-1,3)%3

def build_certificate():
    a,b,c=(Poly.variable(i) for i in range(3))
    qa,qb,qc=squared_coefficients(a,b,c)
    assert disc(qa,qb,qc)*3**6==disc(a,b,c)*(c-a*b)**2
    beta=[Poly(0),Poly(0),Poly(Fraction(1,3))]
    beta2=multiply_mod_f(beta,beta,a,b,c)
    beta3=multiply_mod_f(beta2,beta,a,b,c)
    residual=[beta3[i]+qa*beta2[i]+qb*beta[i]+(qc if i==0 else 0)
              for i in range(3)]
    assert all(x==0 for x in residual)
    r,d,C=a,b,c
    a0=-r*r+3*d
    B=C+2*r**3-9*d*r
    assert 4*a0**3+B*B==27*d*d*(4*d-r*r)+C*(4*r**3-18*d*r+C)
    u=c
    f_special=(3*r,9*d,9*u)
    beta_special=squared_coefficients(*f_special)
    expected_special=(3*(2*d-r*r),3*(3*d*d-2*r*u),-3*u*u)
    assert beta_special==expected_special
    special_leading=disc(*f_special)/3**5
    assert special_leading.mod3()==(-r**3*u).mod3()
    assert (disc(*beta_special)/3**3).mod3()==(-r**3*u**3).mod3()
    assert disc(0,3*a,3*b)==-3**3*(4*a**3+9*b*b)
    assert disc(0,9*a,b)==-3**3*(108*a**3+b*b)
    assert disc(0,9*a,3*b)==-3**5*(12*a**3+b*b)
    assert disc(0,27*a,9*b)==-3**7*(36*a**3+b*b)
    beta_seven=squared_coefficients(Poly(0),27*a,9*b)
    assert beta_seven==(18*a,81*a*a,-3*b*b)
    assert disc(*beta_seven)==-3**5*b*b*(36*a**3+b*b)
    checks=0
    special_residues=[]
    for rr in (-1,1):
        for dd in range(3):
            for uu in (1,2):
                ff=tuple(x.value(rr,dd,uu) for x in f_special)
                gg=tuple(x.value(rr,dd,uu) for x in beta_special)
                assert eisenstein3(gg)
                assert vp(disc(*ff))==5 and vp(disc(*gg))==3
                assert vp(disc(*ff)/disc(*gg))==2
                delta_unit=leading_mod3(16*disc(*ff),5)
                assert (delta_unit==2)==(rr*uu%3==1)
                if delta_unit==2:
                    A=3*(-rr*rr+3*dd)
                    j=Fraction((-48*A)**3,16*disc(*ff))
                    assert vp(j)==1 and leading_mod3(j,1)==2
                special_residues.append({"r":rr,"d_mod3":dd,"c0_mod3":uu,
                    "square_class_is_minus3":delta_unit==2})
                checks+=1
    for aa in range(3):
        for bb in (1,2):
            ff=(0,9*aa,3*bb)
            assert eisenstein3(ff) and vp(disc(*ff))==5
            assert leading_mod3(16*disc(*ff),5)==2
            gg=(18*aa,81*aa*aa,-3*bb*bb)
            assert eisenstein3(gg) and vp(disc(*gg))==5
            assert vp(disc(0,27*aa,9*bb))==7
            assert leading_mod3(16*disc(0,27*aa,9*bb),7)==2
            if aa:
                j5=Fraction((-48*9*aa)**3,16*disc(*ff))
                j7=Fraction((-48*27*aa)**3,16*disc(0,27*aa,9*bb))
                assert vp(j5)==4 and vp(j7)==5
            checks+=1
    for aa in (1,2):
        for bb in range(3):
            first=disc(0,3*aa,3*bb)
            assert vp(first)==3
            assert (leading_mod3(16*first,3)==2)==(aa==1)
            if aa==1:
                j=Fraction((-48*3*aa)**3,16*first)
                assert vp(j)==3 and leading_mod3(j,3)==1
            checks+=1
    for aa in range(3):
        for bb in (1,2):
            second=disc(0,9*aa,bb)
            assert vp(second)==3 and leading_mod3(16*second,3)==2
            checks+=1
    for bb in (1,2):
        forbidden=disc(0,3,bb)
        assert vp(forbidden)==3 and leading_mod3(16*forbidden,3)==1
        checks+=1
    sample_f=(0,-3,11); sample_translated=(3,0,9)
    sample_beta=tuple(int(x) for x in squared_coefficients(*map(Fraction,sample_translated)))
    assert sample_beta==(-3,-6,-3)
    assert disc(*sample_f)==disc(*sample_translated)==-3159
    assert disc(*sample_beta)==-351
    assert disc(*sample_f)==9*disc(*sample_beta) and eisenstein3(sample_beta)
    def canonical(vector):
        vector=tuple(x%3 for x in vector)
        for exponent in vector:
            if exponent:
                multiplier=1 if exponent==1 else 2
                return tuple(multiplier*x%3 for x in vector)
        raise AssertionError("nontrivial p exponent was lost")
    c2_fields=sorted({canonical((a2,ap)) for a2 in (1,2) for ap in (1,2)})
    c6_fields=sorted({canonical((a2,a3,ap)) for a2 in (1,2) for a3 in (0,2) for ap in (1,2)})
    c9_fields=sorted({canonical((a3,ap)) for a3 in (1,2) for ap in (1,2)})
    assert c2_fields==[(1,1),(1,2)]
    assert c6_fields==[(1,a3,ap) for a3 in range(3) for ap in (1,2)]
    assert c9_fields==[(1,1),(1,2)]
    return {
        "result":"R96",
        "status":"exact identities and complete leading-residue certificate",
        "symbolic_checks":[
            "squared-root polynomial vanishes modulo the original cubic",
            "disc(beta)=disc(f)*(c-a*b)^2/3^6",
            "special translation identity for 4*a0^3+B^2",
            "special branch has polynomial index valuation one",
            "all normalized Eisenstein-family discriminants",
        ],
        "leading_residue_cases":checks,
        "special_branch_residues":special_residues,
        "normalized_local_branches":[
            {"v3_A":"1","v3_B":">=1","v3_Delta":3,
             "v3_disc_cubic_field":3,"v3_c":1,
             "extra_unit_condition":"A/3 = 1 mod 3"},
            {"v3_A":">=2","v3_B":"0","v3_Delta":3,
             "v3_disc_cubic_field":3,"v3_c":1,
             "extra_unit_condition":"automatic"},
            {"v3_A":"1","v3_B":"0","v3_Delta":5,
             "v3_disc_cubic_field":3,"v3_c":1,
             "extra_unit_condition":"r*c0 = 1 mod 3"},
            {"v3_A":">=2","v3_B":"1","v3_Delta":5,
             "v3_disc_cubic_field":5,"v3_c":2,
             "extra_unit_condition":"automatic"},
            {"v3_A":">=3","v3_B":"2","v3_Delta":7,
             "v3_disc_cubic_field":5,"v3_c":2,
             "extra_unit_condition":"automatic"},
        ],
        "local_counterexample_to_c6_implies_3_divides_vDelta":{
            "A":-3,"B":11,"original_cubic_discriminant":-3159,
            "E_discriminant":-50544,
            "integral_generator_polynomial":[1,-3,-6,-3],
            "integral_generator_polynomial_discriminant":-351,
            "local_index":3,
            "warning":"local example, not a global integral-j exceptional curve",
        },
        "quotient_field_normal_forms":{
            "c2_coordinates_2_p":c2_fields,
            "c6_coordinates_2_3_p":c6_fields,
            "c9_coordinates_3_p":c9_fields,
        },
    }

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true",
                        help="write the deterministic JSON certificate")
    args=parser.parse_args()
    certificate=build_certificate()
    payload=(json.dumps(certificate,indent=2,sort_keys=True,ensure_ascii=False)+"\n").encode()
    output=Path(__file__).resolve().parent/"data"/"ring_class_three_discriminant_support.json"
    if args.write:
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_bytes(payload)
    else:
        assert output.read_bytes()==payload,"stored certificate differs"
    print("R96 exact local algebra: PASS")
    print("SHA256",hashlib.sha256(payload).hexdigest())

if __name__=="__main__":
    main()
