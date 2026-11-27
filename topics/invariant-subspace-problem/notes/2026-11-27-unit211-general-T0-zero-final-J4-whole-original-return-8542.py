#!/usr/bin/env python3
"""New whole T0 final J4 fiber: exact original QQ Gram/Macaulay and physical-D module return.
Parent original source SHA256 d843f639c07b2b24be559f76f0d6aafd24593b6ece4587ac872242d9112d9709.
No W assumption. Every finite inverse is actual Bezout; all nonunits retained.
120 seconds / 1 GiB. This new source has not yet executed.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_poly,fmpq
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3));start=time.perf_counter()
P=lambda a=():fmpq_poly([fmpq(c) for c in a])
def co(p):return [str(c) for c in p.coeffs()]
def exact(a,b):q,r=divmod(a,b);assert not r and q*b==a;return q
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
class Nonunit(Exception):
 def __init__(self,g):self.g=g/g[g.degree()];super().__init__('actual QQ nonunit retained')
class PhysicalZero(Exception):
 def __init__(self,label):self.label=label;super().__init__(label)
def fiber(F,label):
 F=F/F[F.degree()];inverse_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.q=v.q;return
   if not isinstance(v,fmpq_poly):v=P([v])
   q,r=divmod(v,F);assert q*F+r==v;self.q=r
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
   g,s,t=self.q.xgcd(F);assert s*self.q+t*F==g
   if g.degree()!=0:raise Nonunit(g)
   out=K(s/g[0]);assert self*out==1;inverse_count+=1;return out
  def __truediv__(self,v):return self*K(v).inv()
  def __rtruediv__(self,v):return K(v)/self
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   return K(self.q**n)
  def json(self):return co(self.q)
 A=K
 def unit(label,v):
  if not v:raise PhysicalZero(label)
  iv=v.inv();assert v*iv==1
 k=K(P([0,1]))
 for nm,v in [('parameter k',k),('parameter k2-5',k*k-5),('parameter 2k-5',2*k-5)]:unit(nm,v)
 u=(k*k-4*k+5)/(k*k-5);Q=16*k*(5-2*k)**2/(5*(k*k-5)**2)
 ell=-5*(k*k-4*k+5)/(4*k*(5-2*k));d=1-Q
 for nm,v in [('u',u),('u-1',u-1),('Q',Q),('1-Q',d),('whole equal-weight boundary',Q+2*u-2),('whole Qboundary T0-zero',Q+u-1)]:unit(nm,v)
 assert ell==2*u*(1-u)/Q
 bc=(ell*ell-(u-ell)**2/d)/4
 V2=2*u-ell*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
 J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);M=ell*V2-u*u
 for nm,v in [('original P02',P02),('original bc',bc)]:unit(nm,v)
 assert T0==0 and P02==u*(4*u-4*u*u-Q) and M==u*u*(2*ell-1) and M==4*bc*d
 assert 16*u**4-32*u**3-16*u*Q+32*u-5*Q*Q+16*Q-16==0
 assert k==5*Q/(4*(u-1)**2) and (u-1)*(k*k-5)==10-4*k
 class Mpoly:
  def __init__(self,v=0):
   if isinstance(v,Mpoly):self.terms=v.terms.copy();return
   c=A(v);self.terms={(0,0,0,0):c} if c else {}
  @staticmethod
  def variable(j):
   p=Mpoly();m=[0,0,0,0];m[j]=1;p.terms[tuple(m)]=A(1);return p
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
     m=tuple(ma[j]+mb[j] for j in range(4));z=p.terms.get(m,A())+ca*cb
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
 N1=N4(va(gram[0],gram[1]))-N4(gram[0])-N4(gram[1])-E(lam.scale(A(fmpq(4,3))))*Pj
 A2=2*lam**2-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
 NS=b*N4(gram[2])+c*N4(gram[3])-E((lam*(Mpoly(ell)+2*T+A2)).scale(2*P02))
 PS=b*P2(gram[2])+c*P2(gram[3])-E((Mpoly(ell)+3*T+3*A2+B3).scale(P02))
 E1,EB,EC=mean(1),mean(2),mean(3)
 assert not E1.b and EB.conj()==EC and not N1.b and not NS.b and not PS.b
 original=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a];names=['E1','EBe','EBo','N1','NS','PS']
 
 Dphysical=A2.scale(ell)-T*T
 zeta=Mpoly.variable(3);v1=(T-zeta.scale(ell)).scale(1/u);v0=v1+zeta
 hh=E(1+v0,v1);kk=hh.conj()
 HA=(zeta*zeta).scale(ell*M)-(T*zeta).scale(2*M)+(T*T).scale(V2)-A2.scale(u*u)
 zv=(hh-1)*(kk-1);assert not zv.b
 HB=(B3-2*v0*A2+zv.a*T).scale(u*u)
 assert b*(hh-1)+c*(kk-1)==E(T)
 assert b*hh*hh+c*kk*kk==E(Mpoly(ell)+2*T+A2+HA.scale(1/(u*u)))
 assert b*hh**3+c*kk**3==E(Mpoly(ell)+3*T+3*A2+B3+((3+2*v0)*HA-HB).scale(1/(u*u)))
 weightedNB=b*(N4(gram[2])-E(lam.scale(2*P02))*hh*hh)+c*(N4(gram[3])-E(lam.scale(2*P02))*kk*kk)
 weightedPB=b*(P2(gram[2])-E(Mpoly(P02))*hh**3)+c*(P2(gram[3])-E(Mpoly(P02))*kk**3)
 assert weightedNB==NS-E((lam*HA).scale(2*P02/(u*u)))
 assert weightedPB==PS-E(((3+2*v0)*HA-HB).scale(P02/(u*u)))
 assert E(Dphysical+HA.scale(ell/(u*u)))==E(Mpoly(bc))*(hh-kk)**2
 for pp in original+[Dphysical]:assert all(m[3]==0 for m in pp.terms)
 say(stage='new_T0_J4_whole_finite_original_Gram',label=label,QQBaseDegree=F.degree(),allOriginalE0N0P1MeanAndNPIdentitiesVerified=True,allOriginalWeightedNPThroughHAHBVerified=True,originalPhysicalDIdentityVerified=True,finiteInverseProducts=inverse_count,claimExcluded=False)
 mons=sorted([(i,j,k,0) for i in range(5) for j in range(5-i) for k in range(5-i-j)],key=lambda m:(sum(m),m[1],m[0],m[2]),reverse=True)
 assert len(mons)==35
 def scalev(row,c0):return [v*c0 for v in row]
 def subv(a0,b0):return [v-b0[j] for j,v in enumerate(a0)]
 generated=[];labels=[];basis=[];tags=[];pivs=[]
 def add35(row,label0):
  idx=len(generated);generated.append(row[:]);labels.append(label0);tag={idx:K(1)}
  for b0,pv,tg in zip(basis,pivs,tags):
   c0=row[pv]
   if not c0:continue
   row=subv(row,scalev(b0,c0))
   for j,v in tg.items():tag[j]=tag.get(j,K())-c0*v
  if not any(row):return
  pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv();row=scalev(row,iv);tag={j:v*iv for j,v in tag.items() if v}
  for j in range(35):assert sum((v*generated[i][j] for i,v in tag.items()),K())==row[j]
  basis.append(row);pivs.append(pv);tags.append(tag)
 for ni,pp in enumerate(original):
  for mon in sorted((m for m in mons if sum(m)<=(2 if ni<4 else 1)),key=lambda m:(sum(m),m[1],m[0],m[2])):
   po=pp*Mpoly.from_terms([(mon,K(1))]);assert po.degree()<=4
   add35([po.terms.get(m,K()) for m in mons],[names[ni],mon])
 assert len(generated)==48
 def red35(row):
  cf=[]
  for b0,pv in zip(basis,pivs):
   v=row[pv];cf.append(v);row=subv(row,scalev(b0,v))
  return row,cf
 for power,pp in [(0,Mpoly(1)),(1,Dphysical),(2,Dphysical*Dphysical)]:
  target=[pp.terms.get(m,K()) for m in mons];rem,cf=red35(target)
  if any(rem):continue
  actual={}
  for z,c0 in enumerate(cf):
   for j,v in tags[z].items():actual[j]=actual.get(j,K())+c0*v
  actual={j:v for j,v in actual.items() if v}
  for j in range(35):assert sum((v*generated[i][j] for i,v in actual.items()),K())==target[j]
  cert=dict(modulus=co(F),labels=labels,originalCombination={str(j):v.json() for j,v in actual.items()},target=[v.json() for v in target],Dpower=power)
  cb=json.dumps(cert,separators=(',',':')).encode()
  return dict(label=label,QQBaseDegree=F.degree(),method='whole finite QQ original 48x35 Macaulay',originalRows=len(generated),columns=35,rank=len(basis),DpowerReturned=power,allOriginal35ColumnProductsVerified=True,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),actualInverseProducts=inverse_count,excluded=True)
 say(stage='new_T0_J4_original_Macaulay_partial',label=label,rank=len(basis),originalRows=len(generated),targetsOneDAndDSquaredNotReturned=True,claimExcluded=False)

 # New same-point six-generator return only if degree-four Macaulay did not close.
 def det(mat):
  if not mat:return K(1)
  if len(mat)==1:return mat[0][0]
  return sum(((-1)**j*mat[0][j]*det([[v for z,v in enumerate(row) if z!=j] for row in mat[1:]]) for j in range(len(mat))),K())
 def verify(pp,tg):assert sum((tg[i]*original[i] for i in range(6)),Mpoly())==pp
 quad=[(2,0,0,0),(1,1,0,0),(1,0,1,0),(0,0,2,0)]
 free=[(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,2,0,0),(0,1,1,0)]
 cube=[(0,3,0,0),(0,2,1,0)]
 head=[[pp.terms.get(m,K()) for m in quad] for pp in original[:4]];de=det(head)
 if not de:return dict(label=label,QQBaseDegree=F.degree(),excluded=False,stage='entire original quadratic head zero; retained',MacaulayRank=len(basis))
 iv=[]
 for j in range(4):iv.append([((-1)**(i+j))*det([[head[a0][b0] for b0 in range(4) if b0!=j] for a0 in range(4) if a0!=i])/de for i in range(4)])
 for i in range(4):
  for j in range(4):assert sum((iv[i][z]*head[z][j] for z in range(4)),K())==int(i==j)
 qr=[];qt=[]
 for i in range(4):
  pp=sum((original[j].scale(iv[i][j]) for j in range(4)),Mpoly());tg=[Mpoly(iv[i][j]) if j<4 else Mpoly() for j in range(6)]
  verify(pp,tg)
  for j,m in enumerate(quad):assert pp.terms.get(m,K())==int(i==j)
  qr.append(pp);qt.append(tg)
 def key(m):return(sum(m),m[0],m[2],m[1])
 def lead(pp):m=max(pp.terms,key=key);return m,pp.terms[m]
 def shift(pp,mm,cf):return Mpoly.from_terms((tuple(m[j]+mm[j] for j in range(4)),v*cf) for m,v in pp.terms.items())
 def redpoly(inp):
  pp=inp;rem=Mpoly();tg=[Mpoly() for _ in range(6)]
  while pp:
   lm,lc=lead(pp);ix=next((i for i,r in enumerate(qr) if all(lead(r)[0][j]<=lm[j] for j in range(4))),None)
   if ix is None:
    term=Mpoly.from_terms([(lm,lc)]);rem+=term;pp-=term;continue
   qm,qc=lead(qr[ix]);mm=tuple(lm[j]-qm[j] for j in range(4));cf=lc/qc
   pp-=shift(qr[ix],mm,cf);tg=[tg[j]-shift(qt[ix][j],mm,cf) for j in range(6)]
  verify(rem-inp,tg);return rem,tg
 xx,yy,tt=[Mpoly.variable(j) for j in range(3)]
 ov=[];ot=[]
 for i,j,aa,bb in [(0,1,yy,xx),(0,2,tt,xx),(1,2,tt,yy),(2,3,tt,xx)]:
  inp=aa*qr[i]-bb*qr[j];tg=[aa*qt[i][z]-bb*qt[j][z] for z in range(6)]
  verify(inp,tg);rem,tr=redpoly(inp);tg=[tg[z]+tr[z] for z in range(6)];verify(rem,tg)
  assert all(m in free+cube for m in rem.terms);ov.append(rem);ot.append(tg)
 aa,bb=[ov[1].terms.get(m,K()) for m in cube];cc,dd=[ov[2].terms.get(m,K()) for m in cube];de=aa*dd-bb*cc
 if not de:return dict(label=label,QQBaseDegree=F.degree(),excluded=False,stage='entire original cubic head zero; retained',MacaulayRank=len(basis))
 for ca,cb in [(dd/de,-bb/de),(-cc/de,aa/de)]:
  pp=ov[1].scale(ca)+ov[2].scale(cb);tg=[ot[1][z].scale(ca)+ot[2][z].scale(cb) for z in range(6)]
  verify(pp,tg);qr.append(pp);qt.append(tg)
 for i in range(2):
  for j,m in enumerate(cube):assert qr[4+i].terms.get(m,K())==int(i==j)
 vars0=[xx,yy,tt];bpol=[Mpoly.from_terms([(m,K(1))]) for m in free]
 mats=[];errors=[]
 for ax in range(3):
  mat=[];err=[]
  for po in bpol:
   rem,tr=redpoly(vars0[ax]*po);assert all(m in free for m in rem.terms)
   mat.append([rem.terms.get(m,K()) for m in free]);err.append([-v for v in tr])
  mats.append(mat);errors.append(err)
 def rowpoly(row):return sum((bpol[j].scale(row[j]) for j in range(6)),Mpoly())
 def rp(row,mat):return [sum((row[z]*mat[z][j] for z in range(6)),K()) for j in range(6)]
 def mp(A0,B0):return [rp(row,B0) for row in A0]
 gen=[];glab=[];gsrc=[];bas=[];btag=[];bsrc=[];pv0=[]
 def add6(row,source,label0):
  verify(rowpoly(row),source);idx=len(gen);gen.append(row[:]);gsrc.append(source);glab.append(label0);tag={idx:K(1)}
  for b0,pv,tg in zip(bas,pv0,btag):
   cf=row[pv]
   if not cf:continue
   row=subv(row,scalev(b0,cf))
   for j,v in tg.items():tag[j]=tag.get(j,K())-cf*v
  if not any(row):return
  pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv();row=scalev(row,iv);tag={j:v*iv for j,v in tag.items() if v}
  for j in range(6):assert sum((v*gen[i][j] for i,v in tag.items()),K())==row[j]
  src=[sum((gsrc[i][j].scale(v) for i,v in tag.items()),Mpoly()) for j in range(6)]
  verify(rowpoly(row),src);bas.append(row);btag.append(tag);bsrc.append(src);pv0.append(pv)
 for i in [0,3]:
  rem,tr=redpoly(ov[i]);src=[ot[i][z]+tr[z] for z in range(6)]
  add6([rem.terms.get(m,K()) for m in free],src,['remaining_original_overlap',i])
 for i,po in enumerate(original):
  rem,tr=redpoly(po);src=[tr[z]+Mpoly(int(i==z)) for z in range(6)]
  add6([rem.terms.get(m,K()) for m in free],src,['full_original_polynomial',names[i]])
 for ai in range(3):
  for aj in range(ai+1,3):
   ij=mp(mats[ai],mats[aj]);ji=mp(mats[aj],mats[ai])
   for a0 in range(6):
    row=subv(ij[a0],ji[a0])
    src=[vars0[ai]*errors[aj][a0][z]-vars0[aj]*errors[ai][a0][z]+sum((errors[ai][j][z].scale(mats[aj][a0][j])-errors[aj][j][z].scale(mats[ai][a0][j]) for j in range(6)),Mpoly()) for z in range(6)]
    add6(row,src,['full_original_commutator',ai,aj,a0])
 cursor=0
 while cursor<len(bas):
  for ax in range(3):
   row=rp(bas[cursor],mats[ax]);src=[vars0[ax]*bsrc[cursor][z]-sum((errors[ax][j][z].scale(bas[cursor][j]) for j in range(6)),Mpoly()) for z in range(6)]
   add6(row,src,['full_original_true_point_product',cursor,ax])
  cursor+=1
  assert len(bas)<=6
 def red6(row):
  cf=[]
  for b0,pv in zip(bas,pv0):
   v=row[pv];cf.append(v);row=subv(row,scalev(b0,v))
  return row,cf
 for row in bas:
  for ax in range(3):
   prod=rp(row,mats[ax]);rem,cf=red6(prod);assert not any(rem)
   for j in range(6):assert sum((cf[z]*bas[z][j] for z in range(len(bas))),K())==prod[j]
 I=[[K(int(i==j)) for j in range(6)] for i in range(6)];powers=[[I,mat] for mat in mats]
 for ax in range(3):powers[ax].append(mp(mats[ax],mats[ax]))
 Dm=[[K() for _ in range(6)] for _ in range(6)]
 for mon,cf in Dphysical.terms.items():
  assert mon[3]==0 and sum(mon)<=2;mat=I
  for ax,po in enumerate(mon[:3]):mat=mp(mat,powers[ax][po])
  Dm=[[Dm[i][j]+cf*mat[i][j] for j in range(6)] for i in range(6)]
 target=I[0][:];dp=None;combo=None
 for power in range(7):
  rem,cf=red6(target)
  if not any(rem):
   for j in range(6):assert sum((cf[z]*bas[z][j] for z in range(len(bas))),K())==target[j]
   dp=power;combo=cf;break
  target=rp(target,Dm)
 cert=dict(modulus=co(F),labels=glab,basis=[[v.json() for v in row] for row in bas],tags=[{str(i):v.json() for i,v in tag.items()} for tag in btag],pivots=pv0,Dpower=dp,Dtarget=[v.json() for v in target] if dp is not None else None,Dcombination=[v.json() for v in combo] if combo is not None else None)
 cb=json.dumps(cert,separators=(',',':')).encode()
 return dict(label=label,QQBaseDegree=F.degree(),method='whole finite QQ original six-generator physical-D module',MacaulayRank=len(basis),rank=len(bas),generatedRows=len(gen),allSixOriginalRuleAnd18MultiplicationTracesVerified=True,allOriginalCommutatorAndClosureTracesVerified=True,allOriginalSixColumnProductsVerified=True,DpowerReturned=dp,certificateBytes=len(cb),certificateSHA256=hashlib.sha256(cb).hexdigest(),actualInverseProducts=inverse_count,excluded=dp is not None)
J4=P([-6875,5000,-1100,80,3]);results=[];splits=[]
def process(F,label):
 t0=time.perf_counter()
 try:
  rec=fiber(F,label);rec['wallSeconds']=time.perf_counter()-t0;results.append(rec);say(stage='new_T0_final_J4_whole_QQ_original_return',**rec)
 except Nonunit as ex:
  g=ex.g
  if g.degree()>=F.degree():
   rec=dict(label=label,QQBaseDegree=F.degree(),excluded=False,actualNonunitWholeFactorRetained=True);results.append(rec);say(stage='new_T0_final_J4_whole_nonunit_retained',**rec);return
  other=exact(F,g);assert g.degree()>0 and other.degree()>0 and g*other==F
  splits.append(dict(label=label,factor=co(g),complement=co(other),allFactorsRetained=True))
  say(stage='new_T0_final_J4_exact_nonunit_split',**splits[-1]);process(g,label+'/a');process(other,label+'/b')
 except PhysicalZero as ex:
  rec=dict(label=label,QQBaseDegree=F.degree(),excluded=True,alreadyPaidOriginalUnitZero=ex.label,wallSeconds=time.perf_counter()-t0);results.append(rec);say(stage='new_T0_final_J4_original_unit_zero',**rec)
process(J4,'whole_J4')
signal.alarm(0)
say(stage='new_T0_final_J4_complete_original_QQ_atlas',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),parentOriginalSourceSHA256='d843f639c07b2b24be559f76f0d6aafd24593b6ece4587ac872242d9112d9709',modulus=co(J4),allOriginalSpectrumBranchesRetained=True,allFiniteNonunitSplitsRetained=True,completeOriginalReturns=results,actualNonunitSplits=splits,wholeJ4Excluded=all(r['excluded'] for r in results),wholeT0PlaneClaimed=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
