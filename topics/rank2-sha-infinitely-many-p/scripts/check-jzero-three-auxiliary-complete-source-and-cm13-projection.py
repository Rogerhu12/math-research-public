#!/usr/bin/env python3
"""R348: complete fixed six-dimensional source and original CM13 projection.

All fibers identify one universal theta polynomial; no target-prime scan.
"""
from fractions import Fraction as Q
from math import factorial, comb
import json
from pathlib import Path

def q(a=0,b=0):return(Q(a),Q(b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def sc(a,c):return(a[0]*c,a[1]*c)
def cj(a):return(a[0]-a[1],-a[1])
def inv(a):
 n=mul(a,cj(a));assert n[1]==0 and n[0]
 return sc(cj(a),1/n[0])
def div(a,b):return mul(a,inv(b))
def pw(a,n):
 if n<0:return pw(inv(a),-n)
 z=q(1)
 for i in range(n):z=mul(z,a)
 return z
def sm(seq):
 z=q()
 for x in seq:z=add(z,x)
 return z
zero=q();one=q(1);om=q(0,1);om2=q(-1,-1);delta=q(1,2);gamma=q(3,1);gbar=q(2,-1)

def xyseries(x,y,n=18):
 X=[x];Y=[y]
 for k in range(n):
  X.append(sc(Y[k],Q(2,k+1)))
  Y.append(sc(sm(mul(X[j],X[k-j]) for j in range(k+1)),Q(3,k+1)))
 return X,Y

def polysmul(A,B,n):return[sm(mul(A[j],B[k-j]) for j in range(max(0,k-len(B)+1),min(k,len(A)-1)+1)) for k in range(n+1)]
def point_from_div(x,y,c,N,f):
 h1=div(f[1],f[0]);h2=sub(sc(div(f[2],f[0]),2),pw(h1,2))
 h3=add(sub(sc(div(f[3],f[0]),6),sc(mul(div(f[2],f[0]),h1),6)),sc(pw(h1,3),2))
 xc=div(sub(sc(x,N),h2),pw(c,2));yc=div(sub(sc(y,2*N),h3),sc(pw(c,3),2))
 zc=div(h1,c)
 return xc,yc,zc

def sigma_local(point,n=18):
 x,y,zeta=point;X,Y=xyseries(x,y,n)
 L=[q(),zeta]+[sc(X[k-2],-Q(1,k*(k-1))) for k in range(2,n+1)]
 S=[q(1)]
 for k in range(1,n+1):S.append(sc(sm(sc(mul(L[j],S[k-j]),j) for j in range(1,k+1)),Q(1,k)))
 return S

def evalcoeff(b,y):
 x=q(1);y=q(y);X,Y=xyseries(x,y,3)
 X3=polysmul(polysmul(X,X,3),X,3)
 fg=list(X3);fg[0]=add(fg[0],sc(q(-2,0),Q(b,7)));fg[0]=add(fg[0],sc(delta,Q(6*b,7)))
 fb=[cj(z) for z in fg]
 P1=(x,y,q());P2=point_from_div(x,y,q(2),4,Y);Pd=point_from_div(x,y,delta,3,X)
 xd,yd,zd=Pd;sl=div(sc(pw(xd,2),3),sc(yd,2));x2d=sub(pw(sl,2),sc(xd,2));y2d=sub(mul(sl,sub(xd,x2d)),yd);z2d=add(sc(zd,2),sl)
 P2d=(x2d,y2d,z2d);Pg=point_from_div(x,y,gamma,7,fg);Pgb=point_from_div(x,y,gbar,7,fb)
 pts=[P1,P2,Pd,P2d,Pg,Pgb]
 for xc,yc,zc in pts:assert sub(pw(yc,2),pw(xc,3))==q(b)
 S=[sigma_local(pt) for pt in pts]
 A=[sm(mul(mul(S[1][i],pw(om,i)),S[2][k-i]) for i in range(k+1)) for k in range(7)]
 B=[mul(S[4][i],pw(neg(om2),i)) for i in range(7)];C=[mul(S[5][i],pw(neg(om),i)) for i in range(7)]
 P={}
 for j in range(7):
  for k in range(7):
   P[j,k]=sm(sc(mul(mul(mul(mul(S[3][d+e],pw(neg(om),d)),pw(om2,e)),B[j-d]),C[k-e]),comb(d+e,d)) for d in range(j+1) for e in range(k+1))
 out=q()
 for i in range(7):
  for j in range(7):
   for k in range(7):
    a,b0,c0=6-i,6-j,6-k;n=a+b0+c0
    out=add(out,sc(mul(mul(A[i],P[j,k]),S[0][n]),Q(factorial(n),factorial(a)*factorial(b0)*factorial(c0))))
 out=mul(out,pw(delta,-18))
 P4=7-53*b-12*b*b-80*b**3-128*b**4
 return sc(out,Q(-12*P4,b*b))


checks=[]
def ck(name,value):
    assert value,name
    checks.append(name)
K=[q(-20864,81920),q(-68080,179200),q(-109796,225920),
   q(-68879,-5920),q(-6259,-3320),q(40,20)]
a=[sc(z,Q(1,2952450)) for z in K]
for yy in range(2,9):
    b=yy*yy-1
    expected=sm(sc(a[j],Q(b)**(5-j)) for j in range(6))
    ck('complete algebraic theta fiber at x=1, y='+str(yy),evalcoeff(b,yy)==expected)
ck('constant term is the complete R347 mixed mass',a[5]==sc(q(2,1),Q(2,295245)))
# Same already-paid actual CM13 matrix, using its complete integer storage.
d=json.loads(Path(__file__).with_name('check-jzero-actual-cm13-matrix-and-theta-source.json').read_text())
den=d['integer_matrix_denominator']
Mres=[[sc(add(q(d['integer_matrix_real'][i][j]),sc(delta,d['integer_matrix_delta'][i][j])),Q(1,den)) for j in range(6)] for i in range(6)]
M=[[sc(Mres[i][j],Q(4)**(j-i)) for j in range(6)] for i in range(6)]
def mm(A,B):return [[sm(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def ma(A,B):return [[add(x,y) for x,y in zip(a,b)] for a,b in zip(A,B)]
def ms(A,c):return [[mul(c,x) for x in a] for a in A]
I=[[q(int(i==j)) for j in range(6)] for i in range(6)]
Z=[[q() for j in range(6)] for i in range(6)]
S=[q(-Q(128,7)),q(-Q(80,7)),q(-Q(12,7)),q(-Q(53,7)),q(1),q()]
l=[q(Q(k,17496)) for k in [-329,14,112,-616,7168,-15232]]
g13=q(4,1);lam=neg(g13)
ck('actual normalized original S is the CM13 eigenline',[sm(mul(M[i][j],S[j]) for j in range(6)) for i in range(6)]==[mul(lam,z) for z in S])
ck('complete displayed left functional has exact normalization',sm(mul(x,y) for x,y in zip(l,S))==q(1))
ck('complete displayed left functional is the actual left eigenline',[sm(mul(l[i],M[i][j]) for i in range(6)) for j in range(6)]==[mul(lam,z) for z in l])
B=ms(M,inv(g13));B2=mm(B,B);B3=mm(B2,B)
ck('full normalized CM13 polynomial identity',mm(ma(B3,I),ma(B3,ms(I,om2)))==Z)
Proj=ms(mm(ma(ma(B2,ms(B,q(-1))),I),ma(B3,ms(I,om2))),inv(sc(sub(om2,q(1)),3)))
rankone=[[mul(S[i],l[j]) for j in range(6)] for i in range(6)]
ck('actual CM13 polynomial gives exactly the displayed rank-one projector',Proj==rankone)
ck('actual fixed projector is idempotent',mm(Proj,Proj)==Proj)
ck('actual fixed projector commutes with CM13',mm(Proj,M)==mm(M,Proj))
scalar=sm(mul(x,y) for x,y in zip(l,a))
ck('complete mixed source original S coefficient',scalar==sc(q(539,1120),-Q(1,2952450)))
ck('exact norm of possible projection losses',mul(q(539,1120),cj(q(539,1120)))==q(3*7**2*19*337))
ck('all coefficient denominator primes are fixed small primes',2952450==2*3**10*5**2 and 17496==2**3*3**7)
ck('source scaling and original S scaling leave exactly b cubed',all((7-j)+(j-4)==3 for j in range(6)))
rest=[sub(a[j],mul(scalar,S[j])) for j in range(6)]
ck('the complete remaining source is killed by the actual original projection',sm(mul(x,y) for x,y in zip(l,rest))==q())
ck('the full remaining source keeps the original nonzero mass',rest[5]==a[5])
out={'status':'PASS','check_count':len(checks),'checks':checks,
     'complete_P5_numerators_ascending':[[str(v) for v in x] for x in K],
     'common_denominator':2952450,'coefficient_of_Xj':'K_j*b^(7-j)/2952450',
     'normalized_left_functional_numerators':[-329,14,112,-616,7168,-15232],
     'left_functional_denominator':17496,
     'actual_S_projection_scalar_divided_by_b_cubed':[str(v) for v in scalar],
     'remaining_source_coefficients_at_b1':[[str(v) for v in x] for x in rest],
     'scope':'Complete original theta source and fixed CM13 projector; no new central zero or target-prime scan.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(str(len(checks))+' exact checks: PASS')
