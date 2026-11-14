#!/usr/bin/env python3
"""R129: all rational points on the fixed nine-Cartan twist, via p=5.

All group operations take place in O_L/5^N using Jacobian projective
coordinates. Only units are inverted. The sole precision loss is division
by 5 in the final logarithm. Standard library and R127 helpers only.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import verify_r127_cubic_cover_rank as K

A=K.add(K.add(K.mul(K.ROOTS[0],K.ROOTS[1]),K.mul(K.ROOTS[0],K.ROOTS[2])),
        K.mul(K.ROOTS[1],K.ROOTS[2]))
B=K.neg(K.mul(K.mul(K.ROOTS[0],K.ROOTS[1]),K.ROOTS[2]))
assert A==(-7779,-120,1668)
assert B==(156958,-49320,-10092)


def finite_field_data():
    assert all((r**3-3*r-4)%5 for r in range(5))
    elts=list(product(range(5),repeat=3))
    mul=lambda a,b:tuple(v%5 for v in K.mul(a,b))
    squares={a:0 for a in elts}
    for a in elts:squares[mul(a,a)]+=1
    card=1
    for x in elts:
        f=(1,0,0)
        for e in K.ROOTS:f=mul(f,tuple((a-b)%5 for a,b in zip(x,e)))
        card+=squares[f]
    assert card==140
    Scoeff=[19,-72,84,-10,-36,12,7]
    Cpoints=[(x,y) for x in range(5) for y in range(5)
             if (y*y-sum(c*x**i for i,c in enumerate(Scoeff)))%5==0]
    assert Cpoints==[(0,2),(0,3),(1,2),(1,3),(4,2),(4,3)]
    assert pow(7%5,2,5)==4
    return dict(inert_prime=5,residue_field_size=125,E_cardinality=card,
                C_affine_points_mod5=[list(v) for v in Cpoints],
                C_points_at_infinity_mod5=0)


class Ring:
    def __init__(self,n):
        self.n=n
        self.modulus=5**n
        self.projective_steps=0
        self.unit_inversions=0
    def red(self,a):return tuple(v%self.modulus for v in a)
    def add(self,a,b):return self.red(K.add(a,b))
    def sub(self,a,b):return self.red(K.sub(a,b))
    def mul(self,a,b):return self.red(K.mul(a,b))
    def scale(self,a,c):return self.red(K.scale(a,c))
    def power(self,a,c):
        r=(1,0,0)
        for _ in range(c):r=self.mul(r,a)
        return r
    def inverse(self,a):
        x,y,z=a
        M=[[x,4*z,4*y],[y,x+3*z,3*y+4*z],[z,y,x+3*z]]
        adj=(M[1][1]*M[2][2]-M[1][2]*M[2][1],
             M[1][2]*M[2][0]-M[1][0]*M[2][2],
             M[1][0]*M[2][1]-M[1][1]*M[2][0])
        norm=K.norm(a)
        assert norm%5
        self.unit_inversions+=1
        result=self.scale(adj,pow(norm,-1,self.modulus))
        assert self.mul(a,result)==(1,0,0)
        return result
    def constant(self,a):
        a=tuple(F(v) for v in a)
        assert all(v.denominator%5 for v in a)
        return tuple(v.numerator*pow(v.denominator,-1,self.modulus)%self.modulus for v in a)
    def check_projective(self,P):
        X,Y,Z=P
        # This excludes any base locus or unremoved common nonunit factor
        # in the addition formulas, rather than guessing a lost precision.
        assert any(v%5 for c in P for v in c)
        rhs=self.add(self.add(self.power(X,3),self.mul(A,self.mul(X,self.power(Z,4)))),
                     self.mul(B,self.power(Z,6)))
        assert self.power(Y,2)==rhs
        self.projective_steps+=1
        return P
    def double(self,P):
        X,Y,Z=P
        yy=self.mul(Y,Y)
        yyyy=self.mul(yy,yy)
        S=self.scale(self.mul(X,yy),4)
        M=self.add(self.scale(self.mul(X,X),3),self.mul(A,self.power(Z,4)))
        XX=self.sub(self.mul(M,M),self.scale(S,2))
        YY=self.sub(self.mul(M,self.sub(S,XX)),self.scale(yyyy,8))
        ZZ=self.scale(self.mul(Y,Z),2)
        return self.check_projective((XX,YY,ZZ))
    def add_points(self,P,Q):
        if P is None:return Q
        if Q is None:return P
        X,Y,Z=P
        U,V,W=Q
        U1=self.mul(X,self.power(W,2))
        U2=self.mul(U,self.power(Z,2))
        S1=self.mul(Y,self.power(W,3))
        S2=self.mul(V,self.power(Z,3))
        H=self.sub(U2,U1)
        R=self.sub(S2,S1)
        HH=self.mul(H,H)
        HHH=self.mul(H,HH)
        XX=self.sub(self.sub(self.mul(R,R),HHH),self.scale(self.mul(U1,HH),2))
        YY=self.sub(self.mul(R,self.sub(self.mul(U1,HH),XX)),self.mul(S1,HHH))
        ZZ=self.mul(self.mul(H,Z),W)
        return self.check_projective((XX,YY,ZZ))
    def times(self,P,m):
        self.check_projective(P)
        out=None
        while m:
            if m&1:out=self.add_points(out,P)
            m//=2
            if m:P=self.double(P)
        return out
    def logarithm_mod125(self,P):
        X,Y,Z=self.times(P,140)
        assert K.norm(Y)%5
        t=self.scale(self.mul(self.mul(X,Z),self.inverse(Y)),-1)
        assert all(v%5==0 for v in t)
        assert any(v%25 for v in t)
        # t=-x/y=-XZ/Y.  log_formal(t)-t has valuation >=4.
        # Dividing by 140 loses exactly one digit, leaving log modulo125.
        tdiv5=tuple((v//5)%125 for v in t)
        ans=tuple(v*pow(28,-1,125)%125 for v in tdiv5)
        return ans,dict(t_valuation=1,t_div_5_mod125=list(tdiv5),
                        logarithm_mod125=list(ans))


def calculate(n):
    assert n>=4
    R=Ring(n)
    PP=(R.constant((19,-108,F(181,4))),
        R.constant((F(2907,2),F(14625,8),-1134)),(1,0,0))
    L,p_data=R.logarithm_mod125(PP)
    assert L==(20,22,24)
    f=[K.mul(K.EPS,c) for c in K.BCOEFF]
    H=K.psub(K.pscale(K.pmul(f,K.deriv(K.deriv(f))),4),
              K.pscale(K.pmul(K.deriv(f),K.deriv(f)),3))
    G=K.psub(K.pmul(K.deriv(f),H),K.pmul(f,K.deriv(H)))
    y=(0,2,2)
    assert all(v%5==0 for v in K.sub(K.mul(y,y),f[0]))
    # Hensel/Newton: the initial root is modulo5, and 2y is a unit.
    for _ in range(n.bit_length()+1):
        y=R.scale(R.add(y,R.mul(f[0],R.inverse(y))),pow(2,-1,R.modulus))
    assert R.sub(R.mul(y,y),f[0])==(0,0,0)
    X=R.scale(R.mul(H[0],R.inverse(f[0])),-pow(12,-1,R.modulus))
    Y=R.scale(R.mul(G[0],R.inverse(R.power(y,3))),pow(24,-1,R.modulus))
    log0,q0_data=R.logarithm_mod125((X,Y,(1,0,0)))
    assert tuple(v%125 for v in y)==(105,57,102)
    assert log0==(55,16,27)
    def ann(v,mod=125):
        return[(L[1]*v[0]-L[0]*v[1])%mod,
               (L[1]*v[2]-L[2]*v[1])%mod]
    a0=ann(log0)
    d0=ann(R.inverse(y))
    assert a0==[15,85] and d0==[4,75]
    assert a0[1]%25==10 and d0[1]%5==0
    derivatives={}
    for x,b in [(1,(1,2,1)),(-1,(1,4,1))]:
        yy=R.red(K.mul(K.EPS,b))
        derivatives[str(x)]=ann(R.inverse(yy),5)
    assert derivatives=={'1':[2,2],'-1':[3,1]}
    return dict(curve_a4=list(A),curve_a6=list(B),P_log=p_data,
                x0_square_root_mod125=[v%125 for v in y],x0_log=q0_data,
                annihilator_pivot=1,x0_annihilators_mod125=a0,
                x0_annihilator_derivatives_mod125=d0,
                known_disc_derivatives_mod5=derivatives,
                projective_steps_checked=R.projective_steps,
                all_projective_steps_primitive_mod5=True,
                x0_obstruction_mod25=10,
                rational_points=[[-1,-12],[-1,12],[1,-2],[1,2]])


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    finite=finite_field_data()
    a,b=calculate(4),calculate(8)
    assert a==b
    payload=dict(finite_field=finite,five_adic=a,working_precision=4,
                 independent_working_precision=8,
                 precision_loss_from_division_by_140=1,
                 formal_log_remainder_before_division_valuation_at_least=4,
                 logic=['all six C(F5) residue discs, including both signs',
                        'the global rank-one logarithm line, no subgroup-index assumption',
                        'x=0 disc excluded modulo25; x=1,-1 discs have a unique zero'],
                 scope='complete rational-point classification of the fixed genus-two twist')
    encoded=json.dumps(payload,indent=2,sort_keys=True)+'\n'
    path=Path(__file__).with_name('r129_nine_twist_rational_points_certificate.json')
    if args.check:
        assert path.read_text()==encoded
        print('R129 PASS: all six residue discs; exactly four rational points')
    else:
        path.write_text(encoded)
        print(path.name)
    print('certificate sha256',hashlib.sha256(encoded.encode()).hexdigest())

if __name__=='__main__':main()
