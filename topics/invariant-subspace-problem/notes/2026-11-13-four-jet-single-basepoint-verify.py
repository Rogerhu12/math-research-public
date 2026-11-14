#!/usr/bin/env python3
"""Exact coefficient certificate for the original four-jet single-basepoint theorem.
Requires SymPy; no numerical roots or floating-point tests are used.
"""
import json
import sympy as S
s,t,z,x,y=S.symbols('s t z x y')
K=S.Matrix([[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
 [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]])
v=lambda a:S.Matrix([a**i for i in range(6)])
k=S.expand((v(s).T*K*v(z))[0])
q=lambda a,b:a**3*b+a*b**3-3*a*a*b*b+a**3+b**3-3*a*a*b-3*a*b*b-5*a*a-5*b*b+22*a*b
assert S.expand(k+(s-z)**2*q(s,z))==0

def bezout(f,g,n):
    fc=[S.Poly(f,z).nth(i) for i in range(n+1)]
    gc=[S.Poly(g,z).nth(i) for i in range(n+1)]
    B=S.zeros(n)
    for i in range(1,n+1):
        for j in range(i):
            c=fc[i]*gc[j]-fc[j]*gc[i]
            for a in range(i-j):B[i-1-a,j+a]+=c
    return B.applyfunc(S.expand)

# Two distinct finite poles: divide the forced two roots under q(s,t)=0.
As,rem=S.div(S.expand(q(s,z)-q(s,t)),z-t,z);assert rem==0
At,rem=S.div(S.expand(q(t,z)-q(t,s)),z-s,z);assert rem==0
B=bezout((z-s)*As,(z-t)*At,3)
C={
 (2,2):5*(y+x),
 (1,2):-3*y*x+4*y-3*x*x-4*x-32,
 (1,1):40*y*y-7*y*x*x+40*y*x-154*y-7*x**3+33*x*x+10*x+160,
 (0,1):-5*y*y*x+20*y*y+y*x**3-9*y*x*x+46*y*x-130*y+x**4-8*x**3+37*x*x-110*x,
 (0,2):-5*y*y+y*x*x-9*y*x+26*y+x**3-3*x*x+22*x,
}
for (i,j),c in C.items():
    assert S.expand(B[i,j]-(s-t)*c.subs({x:s+t,y:s*t}))==0
q0=x**3+(y-5)*x*x-6*y*x+32*y-5*y*y
assert S.expand(q0.subs({x:s+t,y:s*t})-q(s,t))==0
P1=4*y*x**4+32*y*x**3-87*y*x*x+1476*y*x-21088*y+4*x**5+16*x**4-279*x**3+3260*x*x-2720*x+5120
P2=4*y*x**4-3*y*x**3-537*y*x*x+5716*y*x+512*y+4*x**5-19*x**4-1089*x**3+2060*x*x-3520*x
m1=C[1,1]*C[2,2]-C[1,2]**2
m2=C[0,1]*C[2,2]-C[0,2]*C[1,2]
assert S.expand(-5*m1-P1+2*q0*(2*x*x-92*x-100*y-247))==0
assert S.expand(-5*m2-P2+2*q0*(22*x*x+20*x*y-12*x-60*y+73))==0
R1=-300*x**8-7920*x**7-45491*x**6+184528*x**5+1096256*x**4-15232*x**3+20633600*x*x-129294336*x+166199296
R2=-25*x**7-590*x**6-2356*x**5+22625*x**4+79688*x**3-400112*x*x+579456*x-32768
A1=S.Poly(P1,y).nth(1);B1=S.Poly(P1,y).nth(0)
A2=S.Poly(P2,y).nth(1);B2=S.Poly(P2,y).nth(0)
assert S.expand(-5*B1**2-(x*x-6*x+32)*A1*B1+(x**3-5*x*x)*A1**2-20*R1)==0
assert S.expand(A1*B2-A2*B1-80*R2)==0

# A double finite pole: first and last principal 2-minors of the original Bezout matrix.
BT=bezout(k,S.diff(k,s),5)
T0=-s**10*(25*s**6+240*s**5-452*s**4-1272*s**3-6428*s*s+45232*s-61680)
T1=(s+2)*(19*s**5+76*s**4-162*s**3-188*s*s+800*s-512)
assert S.expand(BT.extract([0,1],[0,1]).det()-T0)==0
assert S.expand(BT.extract([3,4],[3,4]).det()-T1)==0

def witness(a,b,var,u,v):
    ua=sum(c*var**i for i,c in enumerate(u));vb=sum(c*var**i for i,c in enumerate(v))
    aa=S.Poly(a,var);bb=S.Poly(b,var)
    assert aa.degree()==S.Poly(a,var,modulus=103).degree()
    assert bb.degree()==S.Poly(b,var,modulus=103).degree()
    assert S.Poly(S.expand(ua*a+vb*b-1),var,modulus=103).is_zero
    return {'degrees':[aa.degree(),bb.degree()],
            'a_mod103':[int(aa.nth(i))%103 for i in range(aa.degree()+1)],
            'b_mod103':[int(bb.nth(i))%103 for i in range(bb.degree()+1)],
            'bezout_u_mod103':u,'bezout_v_mod103':v}
secant=witness(R1,R2,x,[24,78,69,15,79,11,65],[4,34,47,22,27,17,53,44])
tangent=witness(T0,T1,s,[66,5,86,41,42,1],[86,27,82,3,57,79,0,29,25,27,34,80,78,61,60,23])

# Infinity: k_inf=-a^4(a+b), first jet is 5a^3(a^2+ab+b^2).
assert (K*S.Matrix([0,0,0,0,0,1]))==S.Matrix([-1,-1,0,0,0,0])
assert (K*S.Matrix([0,0,0,0,1,0]))==S.Matrix([5,5,5,0,0,0])
assert S.Poly(k,z).nth(5)==-s-1
assert S.Poly(k,z).nth(4)==5*(s*s+s+1)
assert (s*s+s+1).subs(s,-1)==1
print(json.dumps({'all_pass':True,'exact_original_matrix_and_minor_identities':True,
 'secant_resultant_contents':[20,80],'prime':103,'secant':secant,'tangent':tangent,
 'infinity_secant_excluded':True,'infinity_tangent_gcd_degree':3},indent=2))
