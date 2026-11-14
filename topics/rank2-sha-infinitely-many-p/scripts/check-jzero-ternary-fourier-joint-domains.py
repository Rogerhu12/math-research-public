#!/usr/bin/env python3
"""Exact fixed Q(sqrt(-3)) identities supporting the uniform proof R340."""
from pathlib import Path
import json
import sympy as s
d=s.symbols('d'); mod=d*d+3
w=(-1+d)/2
wb=(-1-d)/2
x1,x2,x3=s.symbols('x1 x2 x3')
def red(e):
    num,den=s.fraction(s.together(s.expand(e)))
    a=s.rem(num,mod,d); b=s.rem(den,mod,d)
    return s.expand(s.rem(a*s.invert(b,mod,d),mod,d))
checks=[]
def zero(name,e):
    assert red(e)==0,(name,red(e))
    checks.append(name)
F=s.Matrix([[1,1,1],[1,w,wb],[1,wb,w]])/d
P=s.Matrix([[1,0,0],[0,0,1],[0,1,0]])
zero('ternary determinant one',F.det()-1)
for i in range(3):
 for j in range(3):zero(f'Fourier square entry {i},{j}',(F*F+P)[i,j])
r=F*s.Matrix([x1,x2,x3])
zero('quadratic difference weight is preserved',(r[1]-r[2])**2-(x2-x3)**2)
zero('cubic collision is actual Vandermonde',r[1]**3-r[2]**3-(x1-x2)*(x2-x3)*(x3-x1))
zero('auxiliary product is exact quadratic norm',r[1]*r[2]+(x1*x1+x2*x2+x3*x3-x1*x2-x1*x3-x2*x3)/3)
u,v,z=s.symbols('u v z')
zero('complete cubic leading term',(u+v+z)*(u+w*v+wb*z)*(u+wb*v+w*z)-(u**3+v**3+z**3-3*u*v*z))
zero('scaled BBB coefficient',-3/d**3-1/d)
# All A and C factors have type 0 mod 3, whereas B has type 1.
# List every possible term and every actual monomial in the quadratic weight.
survivors=[]
for term,typ in [('ACC',(0,0,0)),('CAC',(0,0,0)),('CCA',(0,0,0)),('AAA',(0,0,0)),('BBB',(1,1,1))]:
 for name,der in [('cross',(0,1,1)),('square2',(0,2,0)),('square3',(0,0,2))]:
  if (typ[1]-der[1])%3==0 and (typ[2]-der[2])%3==0:survivors.append((term,name))
assert survivors==[('BBB','cross')]
checks.append('full auxiliary type projection leaves exactly BBB cross')
c=s.Matrix([1,2,d])
target=[s.Matrix([-2*w,-w,-d*wb]),s.Matrix([d*wb,1,2*w]),s.Matrix([-w,0,d-2])]
for k in range(3):
 val=F*s.diag(w**k,1,1)*c
 for i in range(3):zero(f'original three-factor output k{k} i{i}',val[i]-target[k][i])
zero('exact original phase normalization',d*(-w+wb)/3-1)
for m in [1,2,3]:
 leaf=s.symbols('Z');pairs=s.symbols('X0:'+str(2*m));cur=leaf
 for h in range(m,0,-1):cur=(cur+pairs[2*(h-1)]+pairs[2*(h-1)+1])/d
 expected=leaf/d**m+sum((pairs[2*(h-1)]+pairs[2*(h-1)+1])/d**h for h in range(1,m+1))
 zero(f'actual nested root coordinate m{m}',cur-expected)
result={'status':'PASS','number_of_exact_checks':len(checks),'checks':checks,
'joint_identity':'P0_aux2 P0_aux3 F_*(Q nu^3)=delta^-1 nu tensor rho tensor rho',
'Q':'-(X2-X3)^2/(2 Omega^2)','rho':'x nu / Omega',
'auxiliary_core':'t_p [kappa]_*rho','depth_factor':'t_p^(a+b)',
'collision':'R2^3-R3^3=(X1-X2)(X2-X3)(X3-X1)',
'chain_identity':'P_aux T_m*(delta^m Q_m nu^(2m+1))=nu tensor rho^(2m)',
'limitation':'Actual auxiliary domains are not identified with R339 independent leaf-depth domains.'}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'output':str(out)},ensure_ascii=False))
