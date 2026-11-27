#!/usr/bin/env python3
"""New entire W u=1/2 original finite weight return. All leading factors are checked; no old gate rerun."""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_poly,fmpq
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
zero=P();one=P([1]);w=P([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 return q
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  if not isinstance(n,fmpq_poly):n=P([n])
  if d is None:d=one
  elif not isinstance(d,fmpq_poly):d=P([d])
  assert d
  if not n:self.n=zero;self.d=one;return
  g=n.gcd(d);n=exact(n,g);d=exact(d,g);lc=d[d.degree()];self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v);g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R(exact(self.n,g)*exact(v.n,h),exact(self.d,h)*exact(v.d,g))
 __rmul__=__mul__
 def __truediv__(self,v):v=R(v);assert v;return self*R(v.d,v.n)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n)) if n<0 else R(self.n**n,self.d**n)
 def __eq__(self,v):v=R(v);return self.n*v.d==v.n*self.d
 def json(self):return dict(n=[str(c) for c in self.n.coeffs()],d=[str(c) for c in self.d.coeffs()])

A=R
k=R(w);e=R(-1)/2;u=e+1;Q=e*k;V=u*k+2
ell=u*((k+2)**2-2*e*k)/(k*V);d=1-Q
bc=(ell*ell-(u-ell)**2/d)/4
V2=2*u-ell*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);M=ell*V2-u*u
assert ell==(k+1)/k and bc==(2*k+3)/(8*k) and P02==(k+2)/2 and Phi==-1
assert M==4*bc*d and Phi*(J-2*u*Q)-Pf==0
H=4*e*k-k*k-4*k-8
J19=16*e**4*k**3+e**3*(-8*k**4-16*k**3-96*k*k)+e*e*(-k**5-8*k**4+24*k**3+64*k*k+192*k)+e*(-2*k**5-14*k**4-12*k**3-128)-k**5-10*k**4-40*k**3-104*k*k-160*k-128
C9=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
assert J19==-(k+2)**2*(k+4)**3/4 and C9==(k+1)*(k+2)*(k+4)**2/2 and H==-(k+2)*(k+4)
class Mpoly:
 def __init__(self,v=0):
  if isinstance(v,Mpoly):self.terms=v.terms.copy();return
  c=A(v);self.terms={(0,0,0):c} if c else {}
 @staticmethod
 def variable(j):
  p=Mpoly();m=[0,0,0];m[j]=1;p.terms[tuple(m)]=A(1);return p
 @staticmethod
 def from_terms(ts):
  p=Mpoly();p.terms={m:c for m,c in ts if c};return p
 def __bool__(self):return bool(self.terms)
 def __add__(self,v):
  v=Mpoly(v);p=Mpoly(self)
  for m,c in v.terms.items():
   z=p.terms.get(m,A())+c
   if z:p.terms[m]=z
   elif m in p.terms:del p.terms[m]
  return p
 __radd__=__add__
 def __neg__(self):return Mpoly.from_terms((m,-c) for m,c in self.terms.items())
 def __sub__(self,v):return self+-Mpoly(v)
 def __rsub__(self,v):return Mpoly(v)+-self
 def __mul__(self,v):
  v=Mpoly(v);p=Mpoly()
  for ma,ca in self.terms.items():
   for mb,cb in v.terms.items():
    m=tuple(ma[j]+mb[j] for j in range(3));z=p.terms.get(m,A())+ca*cb
    if z:p.terms[m]=z
    elif m in p.terms:del p.terms[m]
  return p
 __rmul__=__mul__
 def scale(self,c):
  c=A(c);return Mpoly.from_terms((m,v*c) for m,v in self.terms.items())
 def __pow__(self,n):
  p=Mpoly(1)
  for i in range(n):p=p*self
  return p
 def __eq__(self,v):return not(self-Mpoly(v))
 def degree(self):return max((sum(m) for m in self.terms),default=-1)
 def json(self):return [[list(m),c.json()] for m,c in sorted(self.terms.items())]
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=Mpoly(a);self.b=Mpoly(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):v=E(v);return E(self.a*v.a+(self.b*v.b).scale(d),self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for i in range(n):out=out*self
  return out
 def conj(self):return E(self.a,-self.b)
 def __eq__(self,v):v=E(v);return self.a==v.a and self.b==v.b
b=E(Mpoly(ell/2),Mpoly((u-ell)/(2*d)));c=b.conj();p=E(1,1);q=p.conj();a=1-ell
assert b*c==E(Mpoly(bc)) and b*p+c*q==E(Mpoly(u))
x,y,t=[Mpoly.variable(j) for j in range(3)];X=E(x,y);Y=X.conj()
f=(x.scale(u)+y.scale(u-ell*Q)-Mpoly(T0/2)).scale(1/(2*u))
W2=x.scale(V2)+y.scale(2*u-u*Q-ell*Q)
lam=(W2-Mpoly(u*T0)-f.scale(V2+2*u*u)+t.scale(bc*Q)).scale(1/P02)
T=((lam.scale(P02)-Mpoly((1-u)*T0)).scale(T0)-f.scale(Pf)-t.scale(Phi*bc*Q)).scale(1/(Q*P02))-Mpoly(ell)
rg=X-p*E(Mpoly(a))-c*E(t);sg=Y-q*E(Mpoly(a))-b*E(t)
ag=E(f.scale(2))-2*b*X-2*c*Y+E(t.scale(2*bc))
zz=E();oo=E(1);gram=[[zz,zz,p,q],[zz,ag,rg,sg],[p,rg,zz,E(t)],[q,sg,E(t),zz]];unitvec=[oo,zz,oo,oo]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(v,z):return [v*a for a in z]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return E(Mpoly(a))*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in gram]
dv=DK(unitvec);F2=tau(dv);Kd=DK(dv)
assert F2==E(f.scale(2))
def mean(j):
 first=2*tau(vm(gram[0],gram[1])) if j==1 else tau(vm(gram[j],gram[j]))
 return first-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
assert not mean(0)
def N4(v):return 2*tau(vm(dv,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(dv,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
def P2(v):
 cv=va(v,vs(-tau(v),unitvec));return tau(vm(vm(cv,cv),cv))
vc=va(gram[0],vs(-tau(gram[0]),unitvec));zc=va(gram[1],vs(-tau(gram[1]),unitvec));Pj=3*tau(vm(vm(vc,vc),zc))
assert N4(gram[0])==E(lam.scale(2*P02)) and Pj==E((lam-1-T).scale(3*P02)) and P2(gram[0])==E(Mpoly(P02))
N1=N4(va(gram[0],gram[1]))-N4(gram[0])-N4(gram[1])-E(lam.scale(A(R(4)/3)))*Pj
A2=2*lam**2-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
NS=b*N4(gram[2])+c*N4(gram[3])-E((lam*(Mpoly(ell)+2*T+A2)).scale(2*P02))
PS=b*P2(gram[2])+c*P2(gram[3])-E((Mpoly(ell)+3*T+3*A2+B3).scale(P02))
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC and not N1.b and not NS.b and not PS.b
original=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a];names=['E1','EBe','EBo','N1','NS','PS']

Dphysical=A2.scale(ell)-T*T
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
def pco(pp):return [str(c) for c in pp.coeffs()]
atoms=[w,w+1,w+2,w+4,2*w+3]
def strip(pp):
 original=pp;paid=one
 for at in atoms:
  while pp:
   gg=pp.gcd(at)
   if gg.degree()<=0:break
   pp=exact(pp,gg);paid*=gg
 assert pp*paid==original
 return pp,paid
def checkden(c):assert strip(c.d)[0].degree()==0
def verify(pp,tag):assert sum((tag[i]*original[i] for i in range(6)),Mpoly())==pp
def det(mat):
 if not mat:return R(1)
 if len(mat)==1:return mat[0][0]
 return sum(((-1)**j*mat[0][j]*det([[v for z,v in enumerate(row) if z!=j] for row in mat[1:]]) for j in range(len(mat))),R())
quadmons=[(2,0,0),(1,1,0),(1,0,1),(0,0,2)]
free=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
cube=[(0,3,0),(0,2,1)]
head=[[pp.terms.get(m,R()) for m in quadmons] for pp in original[:4]]
d2=det(head);assert d2 and strip(d2.n)[0].degree()==0 and strip(d2.d)[0].degree()==0
inv=[]
for j in range(4):
 inv.append([((-1)**(i+j))*det([[head[a][b] for b in range(4) if b!=j] for a in range(4) if a!=i])/d2 for i in range(4)])
for i in range(4):
 for j in range(4):assert sum((inv[i][a]*head[a][j] for a in range(4)),R())==int(i==j)
q=[];tags=[]
for i in range(4):
 pp=sum((original[j].scale(inv[i][j]) for j in range(4)),Mpoly())
 tg=[Mpoly(inv[i][j]) if j<4 else Mpoly() for j in range(6)]
 verify(pp,tg)
 for j,m in enumerate(quadmons):assert pp.terms.get(m,R())==int(i==j)
 q.append(pp);tags.append(tg)
def key(m):return(sum(m),m[0],m[2],m[1])
def lead(pp):m=max(pp.terms,key=key);return m,pp.terms[m]
def shift(pp,mm,cf):return Mpoly.from_terms((tuple(m[i]+mm[i] for i in range(3)),v*cf) for m,v in pp.terms.items())
def reduce(inp):
 pp=inp;rem=Mpoly();tag=[Mpoly() for _ in range(6)]
 while pp:
  lm,lc=lead(pp);ix=next((i for i,r in enumerate(q) if all(lead(r)[0][j]<=lm[j] for j in range(3))),None)
  if ix is None:
   term=Mpoly.from_terms([(lm,lc)]);rem+=term;pp-=term;continue
  qm,qc=lead(q[ix]);mm=tuple(lm[j]-qm[j] for j in range(3));cf=lc/qc
  pp-=shift(q[ix],mm,cf);tag=[tag[j]-shift(tags[ix][j],mm,cf) for j in range(6)]
 verify(rem-inp,tag)
 return rem,tag
xx,yy,tt=[Mpoly.variable(i) for i in range(3)]
spec=[(0,1,yy,xx),(0,2,tt,xx),(1,2,tt,yy),(2,3,tt,xx)]
ov=[];ot=[]
for i,j,aa,bb in spec:
 pp=aa*q[i]-bb*q[j];tg=[aa*tags[i][z]-bb*tags[j][z] for z in range(6)];verify(pp,tg)
 rem,tr=reduce(pp);tg=[tg[z]+tr[z] for z in range(6)];verify(rem,tg)
 assert all(m in free+cube for m in rem.terms);ov.append(rem);ot.append(tg)
aa,bb=[ov[0].terms.get(m,R()) for m in cube];cc,dd=[ov[2].terms.get(m,R()) for m in cube]
d3=aa*dd-bb*cc;assert d3 and strip(d3.n)[0].degree()==0 and strip(d3.d)[0].degree()==0
for a0,b0 in [(dd/d3,-bb/d3),(-cc/d3,aa/d3)]:
 pp=ov[0].scale(a0)+ov[2].scale(b0);tg=[ot[0][z].scale(a0)+ot[2][z].scale(b0) for z in range(6)]
 verify(pp,tg);q.append(pp);tags.append(tg)
for j in range(2):
 for h,m in enumerate(cube):assert q[j+4].terms.get(m,R())==int(j==h)
for pp,tg in zip(q,tags):
 for cf in pp.terms.values():checkden(cf)
 for tp in tg:
  for cf in tp.terms.values():checkden(cf)
basis=[Mpoly.from_terms([(m,R(1))]) for m in free];variables=[xx,yy,tt];mats=[]
for ax in range(3):
 mat=[]
 for i in range(6):
  rem,tr=reduce(variables[ax]*basis[i]);assert all(m in free for m in rem.terms)
  mat.append([rem.terms.get(m,R()) for m in free])
  for cf in rem.terms.values():checkden(cf)
  for tp in tr:
   for cf in tp.terms.values():checkden(cf)
 mats.append(mat)
def rp(a,B):return [sum((a[z]*B[z][j] for z in range(6)),R()) for j in range(6)]
def mp(A0,B0):return [rp(a,B0) for a in A0]
rows=[];labels=[]
for i in [1,3]:
 rem,tr=reduce(ov[i]);assert all(m in free for m in rem.terms);row=[rem.terms.get(m,R()) for m in free]
 if any(row):rows.append(row);labels.append(['unused_original_overlap',i])
for i in [4,5]:
 rem,tr=reduce(original[i]);assert all(m in free for m in rem.terms);row=[rem.terms.get(m,R()) for m in free]
 if any(row):rows.append(row);labels.append(['full_original_NP',names[i]])
for a0 in range(3):
 for b0 in range(a0+1,3):
  ab=mp(mats[a0],mats[b0]);ba=mp(mats[b0],mats[a0])
  for j in range(6):
   row=[ab[j][h]-ba[j][h] for h in range(6)]
   if any(row):rows.append(row);labels.append(['same_point_commutator',a0,b0,j])
base_count=len(rows)
for i in range(min(base_count,4)):
 for ax in range(3):
  row=rp(rows[i],mats[ax])
  if any(row):rows.append(row);labels.append(['true_point_product',i,ax])
integral=[]
for row in rows:
 den=one
 for c0 in row:checkden(c0);den*=exact(c0.d,den.gcd(c0.d))
 rr=[c0.n*exact(den,c0.d) for c0 in row];common=zero
 for v in rr:common=common.gcd(v)
 _,paid=strip(common);clean=[exact(v,paid) for v in rr]
 for v,c0 in zip(clean,row):assert v*paid*c0.d==c0.n*den
 integral.append(clean)
say(stage='new_entire_u_half_original_global_six_module',allOriginalE0N0P1AndGramProductsVerified=True,allOriginalSixRuleTracesAnd18MultiplicationsVerified=True,allQuadraticAndCubicLeadingFactorsPaid=True,allOriginalDenominatorsPaid=True,basis=free,necessaryRows=len(rows),polynomialRowDegrees=[max(v.degree() for v in row) for row in integral],allRowScalingProductsVerified=True,claimLineExcluded=False)

def detP(mat):
 n=len(mat)
 if n==0:return one
 aa=[row[:] for row in mat];prev=one;sgn=1
 for co in range(n-1):
  if not aa[co][co]:
   sw=next((i for i in range(co+1,n) if aa[i][co]),None)
   if sw is None:return zero
   aa[co],aa[sw]=aa[sw],aa[co];sgn=-sgn
  pivot=aa[co][co]
  for i in range(co+1,n):
   for j in range(co+1,n):aa[i][j]=exact(aa[i][j]*pivot-aa[i][co]*aa[co][j],prev)
   aa[i][co]=zero
  prev=pivot
 return sgn*aa[-1][-1]
order=[1,2,3,4,5,0];orig=[[row[j] for j in order] for row in integral]
aa=[r[:] for r in orig];sel=list(range(len(aa)));pos=0;prev=one;pivs=[]
for co in range(5):
 opts=[i for i in range(pos,len(aa)) if aa[i][co]]
 if not opts:continue
 sw=min(opts,key=lambda i:aa[i][co].degree());aa[pos],aa[sw]=aa[sw],aa[pos];sel[pos],sel[sw]=sel[sw],sel[pos]
 pivot=aa[pos][co]
 for i in range(pos+1,len(aa)):
  for j in range(co+1,6):aa[i][j]=exact(aa[i][j]*pivot-aa[i][co]*aa[pos][j],prev)
  aa[i][co]=zero
 prev=pivot;pivs.append(co);pos+=1
 say(stage='new_u_half_original_polynomial_elimination',nonconstantRankSoFar=pos,pivotColumn=co,pivotDegree=pivot.degree(),allExactDivisionsMultipliedBack=True,claimLineExcluded=False)
for row in aa[pos:]:assert all(not v for v in row[:5])
candidates=sorted((i for i in range(pos,len(aa)) if aa[i][5]),key=lambda i:aa[i][5].degree())
cover=zero;bez=[];rawrem=[];profiles=[]
for ix in candidates[:6]:
 indices=sel[:pos]+[sel[ix]];mat=[orig[i] for i in indices]
 cof=[((-1)**(j+pos))*detP([[row[c] for c in pivs] for z,row in enumerate(mat) if z!=j]) for j in range(len(indices))]
 for co in range(5):assert sum((c*row[co] for c,row in zip(cof,mat)),zero)==0
 delta=sum((c*row[5] for c,row in zip(cof,mat)),zero);assert delta
 rem,paid=strip(delta);rawrem.append(rem)
 gg,ss,tt=cover.xgcd(rem);assert ss*cover+tt*rem==gg
 bez=[ss*v for v in bez]+[tt];cover=gg
 assert sum((a0*b0 for a0,b0 in zip(bez,rawrem)),zero)==cover
 cert=dict(selectedRows=indices,cofactors=[pco(c) for c in cof],delta=pco(delta),paidRemoved=pco(paid))
 cb=json.dumps(cert,separators=(',',':')).encode()
 rec=dict(selectedRows=indices,rawCofactorDegree=delta.degree(),unpaidDegree=rem.degree(),runningCoverDegree=cover.degree(),allSixOriginalColumnsMultipliedBack=True,allPaidRemovalProductsVerified=True,allUnivariateBezoutProductsVerified=True,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest())
 profiles.append(rec);say(stage='new_u_half_original_constant_cofactor',**rec,claimLineExcluded=cover.degree()==0)
 if cover.degree()==0:break
class Nonunit(Exception):
 def __init__(self,g):self.factor=g/g[g.degree()];super().__init__('finite original QQ nonunit retained')
def finite(F):
 F=F/F[F.degree()];inverse_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.q=v.q;return
   if not isinstance(v,fmpq_poly):v=P([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v;self.q=rr
  def __bool__(self):return bool(self.q)
  def __add__(self,v):return K(self.q+K(v).q)
  __radd__=__add__
  def __neg__(self):return K(-self.q)
  def __sub__(self,v):return self+-K(v)
  def __rsub__(self,v):return K(v)+-self
  def __mul__(self,v):return K(self.q*K(v).q)
  __rmul__=__mul__
  def __eq__(self,v):return self.q==K(v).q
  def inv(self):
   nonlocal inverse_count
   gg,ss,tt=self.q.xgcd(F);assert ss*self.q+tt*F==gg
   if gg.degree()!=0:raise Nonunit(gg)
   out=K(ss/gg[0]);assert self*out==1;inverse_count+=1;return out
  def json(self):return pco(self.q)
 def cf(v):return K(v.n)*K(v.d).inv()
 kmats=[[[cf(c0) for c0 in row] for row in mat] for mat in mats]
 I=[[K(int(i==j)) for j in range(6)] for i in range(6)]
 def rp0(a0,B0):return [sum((a0[z]*B0[z][j] for z in range(6)),K()) for j in range(6)]
 def mp0(A0,B0):return [rp0(row,B0) for row in A0]
 def scalev(row,c0):return [v*c0 for v in row]
 def subv(a0,b0):return [v-b0[j] for j,v in enumerate(a0)]
 powers=[[I,mat] for mat in kmats]
 for ax in range(3):
  for po in range(2,4):powers[ax].append(mp0(powers[ax][-1],kmats[ax]))
 def em(pp):
  out=[[K() for _ in range(6)] for _ in range(6)]
  for mon,c0 in pp.terms.items():
   mat=I
   for ax,po in enumerate(mon):mat=mp0(mat,powers[ax][po])
   c1=cf(c0)
   out=[[out[i][j]+mat[i][j]*c1 for j in range(6)] for i in range(6)]
  return out
 gen=[];glabels=[];basis0=[];tags0=[];piv0=[]
 def add(row,label):
  idx=len(gen);gen.append(row[:]);glabels.append(label);tag={idx:K(1)}
  for b0,pv,tg in zip(basis0,piv0,tags0):
   cc=row[pv]
   if not cc:continue
   row=subv(row,scalev(b0,cc))
   for j,v in tg.items():tag[j]=tag.get(j,K())-cc*v
  if not any(row):return
  pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv();row=scalev(row,iv);tag={j:v*iv for j,v in tag.items() if v}
  for j in range(6):assert sum((v*gen[i][j] for i,v in tag.items()),K())==row[j]
  basis0.append(row);piv0.append(pv);tags0.append(tag)
 for i,row in enumerate(integral):add([K(v) for v in row],['fixed_original_row',i])
 initial=len(basis0)
 for name,pp in zip(names,original):add(em(pp)[0],['full_original_polynomial',name])
 cursor=0
 while cursor<len(basis0):
  for ax in range(3):add(rp0(basis0[cursor],kmats[ax]),['true_point_multiplication',cursor,ax])
  cursor+=1
  assert len(basis0)<=6
 def red(row):
  co=[]
  for b0,pv in zip(basis0,piv0):
   v=row[pv];co.append(v);row=subv(row,scalev(b0,v))
  return row,co
 for row in basis0:
  for ax in range(3):
   prod=rp0(row,kmats[ax]);rem,co=red(prod);assert not any(rem)
   for j in range(6):assert sum((co[z]*basis0[z][j] for z in range(len(basis0))),K())==prod[j]
 dm=em(Dphysical);dr=I[0][:];dp=None;dc=None
 for power in range(7):
  rem,co=red(dr)
  if not any(rem):
   for j in range(6):assert sum((co[z]*basis0[z][j] for z in range(len(basis0))),K())==dr[j]
   dp=power;dc=co;break
  dr=rp0(dr,dm)
 cert=dict(modulus=pco(F),labels=glabels,basis=[[v.json() for v in row] for row in basis0],tags=[{str(j):v.json() for j,v in tg.items()} for tg in tags0],pivots=piv0,Dpower=dp,Drow=[v.json() for v in dr] if dp is not None else None,Dcombination=[v.json() for v in dc] if dc is not None else None)
 cb=json.dumps(cert,separators=(',',':')).encode()
 return dict(modulus=pco(F),QQBaseDegree=F.degree(),initialRank=initial,finalRank=len(basis0),generatedRows=len(gen),allSixOriginalColumnProductsVerified=True,allTruePointClosureProductsVerified=True,actualInverseProducts=inverse_count,DpowerReturned=dp,physicalDIsOriginalUnit='D+ell*HA/u^2=bc*(hU-kU)^2',certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),excluded=dp is not None)
returns=[];factorrecords=[]
def return_factor(F,path):
 t0=time.perf_counter()
 if F.degree()>32:
  rec=dict(path=path,modulus=pco(F),QQBaseDegree=F.degree(),excluded=False,notAttempted='new exact finite return limited to base degree <=32; whole factor retained')
  returns.append(rec);say(stage='new_u_half_large_finite_factor_retained',**rec);return
 try:
  rr=finite(F);rr['path']=path;rr['wallSeconds']=time.perf_counter()-t0;returns.append(rr);say(stage='new_u_half_whole_QQ_original_D_return',**rr)
 except Nonunit as ex:
  gg=ex.factor;other=exact(F,gg);assert gg.degree()>0 and other.degree()>0 and gg*other==F
  say(stage='new_u_half_actual_finite_nonunit_split',path=path,factor=pco(gg),complement=pco(other),allFactorsRetained=True)
  return_factor(gg,path+'/a');return_factor(other,path+'/b')
if cover and cover.degree()>0:
 content,fac=cover.factor();back=P([content])
 for i,(ff,mult) in enumerate(fac):
  back*=ff**mult;factorrecords.append(dict(coefficients=pco(ff),degree=ff.degree(),multiplicity=int(mult)))
 assert back==cover
 say(stage='new_u_half_complete_original_univariate_cover',degree=cover.degree(),factors=factorrecords,wholeQQFactorProductVerified=True)
 for i,(ff,mult) in enumerate(fac):return_factor(ff,'F'+str(i))
closed=bool(cover) and (cover.degree()==0 or bool(returns) and all(r['excluded'] for r in returns))
result=dict(stage='new_entire_W_u_half_original_finite_return_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),lineDefinition=dict(u='1/2',e='-1/2',Q='-k/2',ell='(k+1)/k'),allOriginalGramAndSixRulesAnd18MultiplicationsVerified=True,allLeadingAndDenominatorFactorsPaid=True,physicalUnits=['k','k+1','k+2','k+4','2k+3'],fixedOriginalNecessaryRows=len(integral),nonconstantRank=pos,originalCofactorProfiles=profiles,commonCover=pco(cover),completeQQFactors=factorrecords,finiteOriginalReturns=returns,wholeLineExcluded=closed,wholeWExcluded=False,wallSeconds=time.perf_counter()-start,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0);print(json.dumps(result,separators=(',',':')),flush=True)
