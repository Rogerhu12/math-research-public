"""Exact finite-field input and rational bad-height calculation for R134."""
import json
from fractions import Fraction as Q
from pathlib import Path

p=41; ns=-7%p; zero=(0,0); one=(1,0)
def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def neg(x):return ((-x[0])%p,(-x[1])%p)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return ((x[0]*y[0]+ns*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def sc(a,x):return (a*x[0]%p,a*x[1]%p)
def pw(x,n):
 z=one
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n//=2
 return z
def inv(x):
 assert x!=zero
 return pw(x,p*p-2)
def div(x,y):return mul(x,inv(y))
def jinv(A,B):return div(sc(1728*4,pw(A,3)),add(sc(4,pw(A,3)),sc(27,pw(B,2))))
field=[(a,b) for a in range(p) for b in range(p)]
assert pow(ns,(p-1)//2,p)==p-1
labels=[0,3,28,32];weights=[3,1,1,1]
H=[[0]*4 for _ in range(4)];data=[]
for col,j in enumerate(labels):
 if j==0:A,B=zero,one
 elif j==28:A,B=(6,0),(16,0)
 else:
  k=j*pow((1728-j)%p,-1,p)%p;A,B=(3*k%p,0),(2*k%p,0)
 assert jinv(A,B)==(j,0)
 poly=[1]
 for _ in range((p-1)//2):
  out=[0]*(len(poly)+3)
  for n,c in enumerate(poly):
   for k,d in [(0,B[0]),(1,A[0]),(3,1)]:out[n+k]=(out[n+k]+c*d)%p
  poly=out
 assert poly[p-1]==0
 roots=[x for x in field if add(add(pw(x,3),mul(A,x)),B)==zero]
 assert len(roots)==3
 branches=[]
 for x in roots:
  A2=add(sc(-4,A),sc(-15,pw(x,2)))
  B2=add(sc(-22,pw(x,3)),sc(-8,mul(A,x)))
  jj=jinv(A2,B2);assert jj[1]==0 and jj[0] in labels
  H[labels.index(jj[0])][col]+=1
  row={'kernel_x':x,'quotient_A':A2,'quotient_B':B2,'quotient_j':jj[0]}
  if jj[0]==j:
   cs=[c for c in field if mul(pw(c,4),A)==A2 and mul(pw(c,6),B)==B2]
   assert len(cs)==2
   c=next(c for c in cs if add(c,pw(c,p))==one)
   assert mul(c,pw(c,p))==(2,0)
   assert add(sub(pw(c,2),c),(2,0))==zero
   q=sc(pow(17,-1,p),c);assert pw(q,42)==one
   z=pw(q,2);assert pw(z,21)==one and z!=one
   order=next(n for n in range(1,22) if pw(z,n)==one)
   # Character exponents of H^1(D_j): odd k mod42 other than21.
   exponents=[k for k in range(1,42,2) if k!=21]
   assert len(exponents)==20
   counts=[sum(k%order==a for k in exponents) for a in range(order)]
   assert all(counts[a]==counts[0]+1 for a in range(1,order))
   # counts[0] + (counts[0]+1) * sum_{a=1}^{order-1} zeta^a = -1.
   row.update(differential=c,normalized_q=q,zeta=z,zeta_order=order,character_trace=-1)
  branches.append(row)
 data.append({'j':j,'A':A,'B':B,'hasse_coefficient':0,'branches':branches})
assert [sum(H[i][j] for i in range(4)) for j in range(4)]==[3]*4
assert all(weights[i]*H[i][j]==weights[j]*H[j][i] for i in range(4) for j in range(4))
assert [H[j][j] for j in range(4)]==[0,0,2,0]
mass=sum(Q(1,a) for a in weights);qv=[Q(1,a)/mass for a in weights]
assert all(sum(H[i][j]*qv[j] for j in range(4))==3*qv[i] for i in range(4))
lengths=[Q(a,420) for a in weights];h1dims=[6,20,20,20]
tauT=[0,0,-2,0]
tauF=[27*x+4*y for x,y in zip(tauT,h1dims)]
graph=[lengths[j]/2*(27*H[j][j]+4-85*qv[j]) for j in range(4)]
Xi=[weights[j]*tauF[j]+840*graph[j] for j in range(4)]
bad=[-Q(40,42)*(v-Xi[0]) for v in Xi]
assert bad==[0]*4
cert={'p':p,'field_relation':'s^2=-7','labels':labels,'weights':weights,'curves':data,'T2_path_matrix':H,'q':[str(x) for x in qv],'halfedge_lengths':[str(x) for x in lengths],'tau_T2':tauT,'tau_F':tauF,'Q_F':[str(x) for x in graph],'Xi_F':[str(x) for x in Xi],'b_F':[str(x) for x in bad],'F':'27*T2+4','scope':'finite field and rational arithmetic inputs; actual geometric identification is proved in R134'}
out=Path(__file__).resolve().parent/'data'/'p41_bad_t2_certificate.json';out.parent.mkdir(exist_ok=True);out.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:cert[k] for k in ['T2_path_matrix','tau_F','Q_F','Xi_F','b_F']}))
