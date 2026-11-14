#!/usr/bin/env python3
"""R347: an exact original three-auxiliary mixed moment; no prime scan."""
from fractions import Fraction as Q
from math import factorial, comb
from pathlib import Path
import json

checks=[]
def ck(name,value):
    assert value,name
    checks.append(name)
def q(x=0,y=0):return(Q(x),Q(y))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def sc(x,c):return(x[0]*c,x[1]*c)
def conj(x):return(x[0]-x[1],-x[1])
def pw(x,n):
    z=q(1)
    for _ in range(n):z=mul(z,x)
    return z
def sm(xs):
    z=q()
    for x in xs:z=add(z,x)
    return z
def dot(x,y):return sm(mul(a,b) for a,b in zip(x,y))
def st(x):return [str(x[0]),str(x[1])]
om=q(0,1);om2=q(-1,-1);delta=q(1,2);dinv=sc(delta,Q(-1,3))
c=[q(1),q(2),delta,sc(delta,2),q(3,1),q(2,-1)]
r=[q(1),om2,q(1),q(),q(),q()]
s=[q(1),q(),q(),sc(om2,-1),sc(om,-1),q()]
t=[q(1),q(),q(),om,q(),sc(om2,-1)]
for name,v in [('r',r),('s',s),('t',t)]:
    ck('original relation '+name,dot(c,v)==q())
    ck('original auxiliary quasi-period cancellation '+name,dot(list(map(conj,c)),list(map(conj,v)))==q())
ck('original theta degree is thirty-four',dot(c,list(map(conj,c)))==q(34))
ck('delta normalization in total degree eighteen',pw(dinv,18)==q(Q(-1,3**9)))
W1=-Q(1,7);W2=W1*W1/13
F1=-W1/30;F2=-W2/132
c1=F1;c2=F2+F1*F1/2
ck('exact original sigma seventh coefficient',c1==Q(1,210))
ck('exact original sigma thirteenth coefficient',c2==-Q(1,1801800))
mult=Q(factorial(13),factorial(4)**2*factorial(5))
ck('complete thirteenth multinomial',mult==90090)
phase=mul(om,add(om2,sc(om,-1)))
ck('complete single-thirteenth phase',phase==q(2,1))
a13=sc(phase,mult*c2)
term=sm(sc(mul(pw(sc(om,-1),5-j),pw(om2,2+j)),comb(3,j)*comb(7,5-j)) for j in range(4))
ck('complete two-seventh binomial sum',term==sc(delta,105))
a77=sc(mul(om,term),35*c1*c1)
ck('single-thirteenth contribution',a13==sc(q(2,1),-Q(1,20)))
ck('two-seventh contribution',a77==sc(q(2,1),-Q(1,12)))
coef=mul(add(a13,a77),pw(dinv,18))
ck('true auxiliary coefficient with every delta factor',coef==sc(q(2,1),Q(2,295245)))
moment=sc(coef,-Q(factorial(6)**3,84))
ck('true mixed measure moment including original source scale',moment==sc(q(2,1),-Q(51200,1701)))
ck('norm of remaining CM phase',mul(q(2,1),conj(q(2,1)))==q(3))
ck('all rational denominator primes are fixed small primes',1701==3**5*7 and 51200==2**11*5**2)
ck('all six possible even original CM theta monomials',[k for k in range(18) if (34-2*k)%6==0]==[2,5,8,11,14,17])
for name,v1,v2 in [('r,s',r,s),('r,t',r,t),('s,t',s,t)]:
    ck('pair '+name+' leaves an original zero-mass factor',any(x==q() and y==q() for x,y in zip(v1,v2)))
out={'status':'PASS','check_count':len(checks),'checks':checks,
     'sigma13_coefficient_at_b1':str(c2),
     'joint_coefficient_divided_by_b_squared':st(coef),
     'original_moment_divided_by_b_squared_and_Omega18':st(moment),
     'basis_exponents':[2,5,8,11,14,17],
     'scope':'Exact original joint moment and full theta-space bound; no central derivative nonvanishing or prime scan.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(str(len(checks))+' exact checks: PASS')
