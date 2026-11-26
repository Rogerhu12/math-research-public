#!/usr/bin/env python3
"""R150 S0/Lt0: complete original Qa projection factor A24(e,k)=0 return.
Every polynomial comes from the original Frobenius Gram or an exact paid
coordinate transformation. Dixon rows are explicit combinations of the three original means.
A full rational one-variable cover and degree-preserving Sylvester reduction exclude the whole curve.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
start=time.perf_counter()
def say(x):x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('l','u','Q','lam','f','t','eta0','z0'),'lex');lp,up,Qp,Lp,fp,tp,eta0p,z0p=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
l,u,Q,lam,f,t=map(R,ctx.gens()[:6]);eta0=R(eta0p);z0=R(z0p);Delta=1-Q
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
W1=E(T0/2+2*u*f);W2=E(u*T0+lam*P02+(V2+2*u*u)*f-bc*Q*t)
X=ivbp*(q*W1-W2);Y=ivcq*(W2-p*W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b


# Full original base-column identities, using the dual product throughout.
v0c=va(rows[0],vs(-tau(rows[0]),one))
assert tau(vm(vm(v0c,v0c),v0c))==E(P02)
assert N4(rows[0])==E(2*lam*P02)
def P2of(vv):
 centered=va(vv,vs(-tau(vv),one))
 return tau(vm(vm(centered,centered),centered))
H0=lam-fmpq(1,2);Dphys=(2*lam-3)**2-4*z0;norm_eta=eta0*eta0-(1-Q)*Dphys
hraw=E(H0,eta0/(2*(1-Q)));kraw=hraw.conj()
h2=E(H0*H0+Dphys/4,H0*eta0/(1-Q))
h3=E(H0**3+3*H0*Dphys/4,eta0*(3*H0*H0+Dphys/4)/(2*(1-Q)))
assert hraw*hraw-h2==E(norm_eta/(4*(1-Q)))
assert hraw**3-h3==E(3*H0*norm_eta/(4*(1-Q)),eta0*norm_eta/(8*(1-Q)**2))
PBvalue=P2of(rows[2]);PCvalue=P2of(rows[3]);NBvalue=N4(rows[2]);NCvalue=N4(rows[3])
NBraw=NBvalue-E(2*lam*P02)*h2
NCraw=NCvalue-E(2*lam*P02)*h2.conj()
PBraw=PBvalue-E(P02)*h3
PCraw=PCvalue-E(P02)*h3.conj()
assert NBraw.conj()==NCraw and PBraw.conj()==PCraw
assert (NBvalue-E(2*lam*P02)*hraw*hraw)-NBraw==-E(2*lam*P02)*E(norm_eta/(4*(1-Q)))
assert (PBvalue-E(P02)*hraw**3)-PBraw==-E(P02)*E(3*H0*norm_eta/(4*(1-Q)),eta0*norm_eta/(8*(1-Q)**2))
say({'stage':'original_highest_normal_same_root_norm_identity_verified','identity':'original PB/NB minus returned PB/NB is an explicit multiple of eta^2-(1-Q)Delta','sameConjugationVerified':True,'noDivisionByH':True,'claimExcluded':False})
raw=[('E1',E1.a),('EBeven',EB.a),('EBodd',EB.b),('N1elim',NH.a),('NB_even',NBraw.a),('NB_odd',NBraw.b),('PB_even',PBraw.a),('PB_odd',PBraw.b)]
original_data=[]
for label,val in raw:
 den=val.d;paid=[]
 for nm,atom in [('pq',Qp),('distinct_p_q',1-Qp),('bc',2*lp*up-up*up-lp*lp*Qp)]:
  count=0
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   q0=den/gg;assert q0*gg==den;den=q0;count+=1
  if count:paid.append((nm,count))
 assert den.total_degree()==0
 original_data.append((label,val.n.to_dict()))
 say({'stage':'original_universal_necessary_polynomial','label':label,'numSha256':hashlib.sha256(str(sorted(val.n.to_dict().items())).encode()).hexdigest(),'paidDenominatorAtoms':paid,'dualProductChecked':True})
# e=u-1, k=Q/e; these symbols have no relation to the U-value named k.
ctx=fmpq_mpoly_ctx.get(('e','k','lam','f','v','eta','invUnit'),'lex')
e,k,la,fp,v,eta,invUnit=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
j=k+2-2*e;x=k+4;qq=e*k;Dq=qq-1
D3=4*e**3-3*e**2*k-4*e**2+e*k*k+4*e*k+4*e-k-4
assert 2*j*k*(e+1)-(e+1)**2*k*k-j*j*qq==-k*D3
# Thus bc=D3/(4*k*(e*k-1)), and the reversible t change is v=4*k*bc*t.
# z is recovered from the original P1 and second U moment; its only
# denominator here is Zden=2*j^2, paid by original P02 on Lt0.
s_pre=2*la-3;A_pre=2*la*la-2*la+1
Tnum_pre=x*x-2*j*j-2*la*j*x-4*x*fp
Znum_pre=s_pre*Tnum_pre-2*j*k*A_pre;Zden_pre=2*j*j
polys=[];names=[]
smallunits=[('e',e),('k',k),('distinct_p_q',Dq),('ell',j),('bc',D3),('T0',x)]
for label,terms in original_data:
 ml=max(int(m[0]) for m in terms);mz=max(int(m[7]) for m in terms);praw=zz
 for m,aa in terms.items():
  il,iu,iq,ia,iff,it,ie,iz=map(int,m)
  praw+=aa*j**il*k**(ml-il)*(e+1)**iu*qq**iq*la**ia*fp**iff*v**it*eta**ie*Znum_pre**iz*Zden_pre**(mz-iz)
 pp=praw;removed=[];removed_product=oo
 for nm,atom in smallunits:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   rr=pp/gg;assert rr*gg==pp;pp=rr;removed_product*=gg;count+=1
  if count:removed.append((nm,count))
 assert pp*removed_product==praw
 small=zz;left=zz
 if label in ['E1','EBeven','EBodd','N1elim']:
  for n in range(3):
   cc=ctx.from_dict({tuple(int(m[i]) if i!=4 else 0 for i in range(7)):aa for m,aa in pp.to_dict().items() if int(m[4])==n})
   paidscale=Dq**(2-n)*D3**n;reduced=cc/paidscale
   assert reduced*paidscale==cc
   small+=reduced*v**n;left+=cc*Dq**n*D3**(2-n)*v**n
  assert left==Dq*Dq*D3*D3*small
  assert all(int(m[2])+int(m[3])+int(m[4])<=2 for m in small.to_dict())
 else:
  td=max(int(m[4]) for m in pp.to_dict())
  for n in range(td+1):
   cc=ctx.from_dict({tuple(int(m[i]) if i!=4 else 0 for i in range(7)):aa for m,aa in pp.to_dict().items() if int(m[4])==n})
   small+=cc*Dq**n*D3**(td-n)*v**n
  rawsmall=small;paidprod=oo
  for nm,atom in smallunits:
   count=0
   while small:
    gg=small.gcd(atom)
    if gg.total_degree()==0:break
    red=small/gg;assert red*gg==small;small=red;paidprod*=gg;count+=1
   if count:removed.append(('rescaled_'+nm,count))
  assert small*paidprod==rawsmall
 polys.append(small);names.append(label)
 say({'stage':'original_low_necessary_polynomial','label':label,'degrees':list(map(int,small.degrees())),'terms':len(small.to_dict()),'sha256':hashlib.sha256(str(sorted(small.to_dict().items())).encode()).hexdigest(),'removedOnlyPaidFactors':removed,'exactCoordinateMultiplicationVerified':True})
def coeff(p,na,nf,nv):
 return ctx.from_dict({(int(m[0]),int(m[1]),0,0,0,0,0):aa for m,aa in p.to_dict().items() if int(m[2])==na and int(m[3])==nf and int(m[4])==nv})
assert coeff(polys[0],0,0,2)==j/8
assert coeff(polys[3],0,0,2)==j/4
Cmat=[[coeff(p,2,0,0),coeff(p,1,1,0),coeff(p,0,2,0)] for p in polys]
a0,b0,c0=Cmat[:3]
detC=a0[0]*(b0[1]*c0[2]-b0[2]*c0[1])-a0[1]*(b0[0]*c0[2]-b0[2]*c0[0])+a0[2]*(b0[0]*c0[1]-b0[1]*c0[0])
expected=-512*e*(e+1)*(4*e-k-4)*k*k*(-j)**3*D3**3
assert detC==expected
adj=[]
for i in range(3):
 rr=[]
 for q in range(3):
  sub=[[Cmat[row][col] for col in range(3) if col!=i] for row in range(3) if row!=q]
  rr.append((-1)**(i+q)*(sub[0][0]*sub[1][1]-sub[0][1]*sub[1][0]))
 adj.append(rr)
for i in range(3):
 for q in range(3):
  assert sum((Cmat[i][ii]*adj[ii][q] for ii in range(3)),zz)==(detC if i==q else zz)
weights=[-sum((Cmat[3][i]*adj[i][q] for i in range(3)),zz) for q in range(3)]+[detC]
Lraw=sum((ww*pp for ww,pp in zip(weights,polys)),zz);Lsmall=Lraw;Lpaid=oo;Lhistory=[]
for nm,atom in smallunits:
 count=0
 while Lsmall:
  gg=Lsmall.gcd(atom)
  if gg.total_degree()==0:break
  rr=Lsmall/gg;assert rr*gg==Lsmall;Lsmall=rr;Lpaid*=gg;count+=1
 if count:Lhistory.append((nm,count))
assert Lsmall*Lpaid==sum((ww*pp for ww,pp in zip(weights,polys)),zz)
assert all(int(m[2])+int(m[3])<=1 for m in Lsmall.to_dict())
say({'stage':'entire_original_matrix_multiplication_verified','matrixDeterminant':'-512 e(e+1)(4e-k-4) k^2 (-j)^3 D3^3','unpaidDeterminantFactors':[],'halfWeightPaidBy':'R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-half-base-weight-exclusion.md','adjugateIdentities':9,'normalizedDerivedRowTerms':len(Lsmall.to_dict()),'normalizedDerivedRowPaidDivisions':Lhistory,'claimExcluded':False})

import functools,itertools
bctx=fmpq_mpoly_ctx.get(('e','k'),'lex');be,bk=bctx.gens();bz=bctx.constant(0);bo=bctx.constant(1)
def bp(x):return x if hasattr(x,'to_dict') else bctx.constant(x)
class BR:
 def __init__(self,n=0,d=None):
  if isinstance(n,BR):self.n=n.n;self.d=n.d;return
  n=bp(n);d=bo if d is None else bp(d);assert d
  if not n:self.n=bz;self.d=bo;return
  gg=n.gcd(d);n=n/gg;d=d/gg;lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=BR(o)
  if not self:return o
  if not o:return self
  gg=self.d.gcd(o.d);a=self.d/gg;b=o.d/gg
  return BR(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return BR(-self.n,self.d)
 def __sub__(self,o):return self+-BR(o)
 def __rsub__(self,o):return BR(o)+-self
 def __mul__(self,o):
  o=BR(o)
  if not self or not o:return BR()
  gg=self.n.gcd(o.d);hh=o.n.gcd(self.d)
  return BR((self.n/gg)*(o.n/hh),(self.d/hh)*(o.d/gg))
 __rmul__=__mul__
 def __truediv__(self,o):o=BR(o);assert o;return self*BR(o.d,o.n)
 def __eq__(self,o):o=BR(o);return self.n*o.d==o.n*self.d

def split(p):
 dd={}
 for mm,aa in p.to_dict().items():
  assert mm[6]==0
  mon=tuple(map(int,mm[2:6]));coef=bctx.from_dict({tuple(map(int,mm[:2])):aa});dd[mon]=dd.get(mon,BR())+BR(coef)
 return {m:a for m,a in dd.items() if a}
def addp(a,b):
 out=dict(a)
 for m,vv in b.items():out[m]=out.get(m,BR())+vv
 return {m:v for m,v in out.items() if v}
def scalep(a,s):return {m:s*v for m,v in a.items() if s*v}
def shiftp(a,mon):return {tuple(x+y for x,y in zip(m,mon)):v for m,v in a.items()}
SP=[split(p) for p in polys]
quadmons=[(2,0,0,0),(1,1,0,0),(0,2,0,0)]
rest=[{m:v for m,v in p.items() if m not in quadmons} for p in SP[:3]]
detc=split(detC)[(0,0,0,0)]
adjB=[[split(a)[(0,0,0,0)] if a else BR() for a in row] for row in adj]
rules=[]
for i in range(3):
 pp={}
 for q in range(3):pp=addp(pp,scalep(rest[q],-adjB[i][q]/detc))
 assert all(m[0]+m[1]<=1 for m in pp)
 rules.append(pp)

def mulp(a,b):
 out={}
 for m,aa in a.items():
  for n,bb in b.items():
   key=tuple(x+y for x,y in zip(m,n));out[key]=out.get(key,BR())+aa*bb
 return {m:aa for m,aa in out.items() if aa}
def subp(a,b):return addp(a,scalep(b,BR(-1)))
zero_mon=(0,0,0,0)
@functools.lru_cache(None)
def nfmon(mon):
 a,b,c,d=mon
 if a+b<=1:return {mon:BR(1)},[{},{},{}]
 if a>=2:i=0;shift=(a-2,b,c,d)
 elif a and b:i=1;shift=(a-1,b-1,c,d)
 else:i=2;shift=(a,b-2,c,d)
 out={};trace=[{shift:adjB[i][q]/detc} for q in range(3)]
 for m,vv in rules[i].items():
  normal,qt=nfmon(tuple(x+y for x,y in zip(m,shift)))
  out=addp(out,scalep(normal,vv))
  for q in range(3):trace[q]=addp(trace[q],scalep(qt[q],vv))
 return out,trace
def nf(p):
 out={};trace=[{},{},{}]
 for m,vv in p.items():
  normal,qt=nfmon(m);out=addp(out,scalep(normal,vv))
  for q in range(3):trace[q]=addp(trace[q],scalep(qt[q],vv))
 check=subp(p,out)
 for q in range(3):check=subp(check,mulp(trace[q],SP[q]))
 assert not check
 return out,trace
for pp in SP[:3]:assert not nf(pp)[0]
# Exact low equations of the SAME S0 value parameter and original N(V).
s=2*la-3;AA=2*la*la-2*la+1;CC=-4*la*la+5*la-2;RR=3-4*la
Tnum=x*x-2*j*j-2*la*j*x-4*x*fp;Tden=2*j*k
Znum=s*Tnum-2*j*k*AA;Zden=2*j*j
Dnum=s*s*Zden-4*Znum
Bnum=Tnum-j*j*s;Unum=e*k+2*e-2
Mmoment=Znum*Tnum-CC*Zden*Tden
Malign=Unum*Dnum-2*j*eta*Bnum
Mnorm=eta*eta*Zden-(1-e*k)*Dnum
Enum=2*j*j+Tnum;Wnum=(la-1)*Tden-Tnum
Lnum=j+k*(e+1);Ynum=j*Lnum*s-Tnum-j*j*eta
Mnormal=2*k*k*x*(RR*Zden-Znum)*fp-2*e*k*Enum*Znum-x*Wnum*Ynum
# Multiply every rational-coordinate identity back before using it.
lv=R(j,k);uv=R(e+1);Qv=R(e*k);Tv=R(Tnum,Tden);Zv=R(Znum,Zden);Dv=R(Dnum,Zden);wv=R(la-1)-Tv
assert lv*Zv==R(s)*Tv-R(AA)
assert Zv*Tv-R(CC)==R(Mmoment,Zden*Tden)
assert Dv==R(s*s)-4*Zv
Bval=2*Tv-lv*R(s)
assert (uv-lv)*Dv-R(eta)*Bval==R(Malign,k*Zden)
assert R(eta*eta)-(1-Qv)*Dv==R(Mnorm,Zden)
T0v=-R(e*x)
assert (2*uv-lv*Qv-2*uv*uv)==T0v
assert 4*R(e)*T0v*R(fp)==-T0v*T0v+2*lv*Qv*Qv*(lv+Tv)-2*R(la)*lv*Qv*T0v
normal_expr=2*(R(RR)-Zv)*R(fp)-4*lv*(lv+Tv)*Qv*Zv/R(x)-wv*((lv+uv)*R(s)-2*Tv-lv*R(eta))
assert normal_expr==R(Mnormal,Zden*k*k*x)
# Verify the original K-to-N(V) relation before taking any quotient.
oldctx=fmpq_mpoly_ctx.get(('L','Z','TH','F'),'lex');ll,zz0,tt0,ff0=oldctx.gens()
ss=2*ll-3;ac=2*ll*ll-2*ll+1;cc=-4*ll*ll+5*ll-2;dd=ss*cc-ac*zz0;de=ss*ss-4*zz0;bb=2*cc*zz0-dd*ss
uu=dd+tt0*bb;vv=uu-zz0*zz0;qu=1-tt0*tt0*de;ee=dd+cc*zz0;tn=-4*vv-zz0*zz0*qu;ww=(ll-1)*zz0-cc;yy=2*(dd*ss-cc*zz0)+tt0*(bb*ss-dd*de)
fn=-tn*tn+2*dd*ee*qu*qu-2*ll*dd*qu*tn
korig=zz0**3*(3-4*ll-zz0)*fn+8*dd*ee*qu*vv*vv-2*vv*tn*ww*yy
nlin=2*zz0**3*(3-4*ll-zz0)*tn*ff0+4*dd*ee*qu*vv-tn*ww*yy
assert 2*vv*nlin-korig==zz0**3*(3-4*ll-zz0)*(4*vv*tn*ff0-fn)
say({'stage':'same_parameter_original_moment_alignment_norm_P1_Nvalue_identities_verified','divisionAtoms':['e','k','j','k+4'],'originalKIdentity':True,'noNormEmbeddingMismatch':True,'claimExcluded':False})

# SAME eta alignment/norm: no division by the possibly zero Bnum.
Qalign=Unum*Unum*Dnum-2*(1-e*k)*Bnum*Bnum
assert Dnum*Qalign==Malign*(Unum*Dnum+2*j*eta*Bnum)+2*Bnum*Bnum*Mnorm
CC=-4*la*la+5*la-2;Mmoment=Znum_pre*Tnum_pre-CC*Zden_pre*(2*j*k)
inputs=[('N1elim',SP[3]),('NB_even',SP[4]),('PB_even',SP[6]),('U_moment',split(Mmoment))]
CP1=addp(shiftp(rules[0],(0,1,0,0)),scalep(shiftp(rules[1],(1,0,0,0)),BR(-1)))
CP2=addp(shiftp(rules[1],(0,1,0,0)),scalep(shiftp(rules[2],(1,0,0,0)),BR(-1)))
for cp,i,jj in [(CP1,0,1),(CP2,1,2)]:
 trace=[addp({(1,0,0,0):adjB[jj][q]/detc},{(0,1,0,0):-adjB[i][q]/detc}) for q in range(3)]
 check=dict(cp)
 for q in range(3):check=subp(check,mulp(trace[q],SP[q]))
 assert not check
inputs += [('original_mean_S1',CP1),('original_mean_S2',CP2)]
# Every coefficient denominator is verified to contain only det(C) factors.
bdet=detc.n
coefficient_inverse_checks=0
def check_paid_den(den):
 global coefficient_inverse_checks
 dd=den
 while dd.total_degree()>0:
  gg=dd.gcd(bdet);assert gg.total_degree()>0
  rr=dd/gg;assert rr*gg==dd;dd=rr
 assert dd
 coefficient_inverse_checks+=1
rows=[];row_names=[]
# The entire k=4e line was independently excluded by two original
# resultants and QQ[e] Bezout, including every v leading-zero fiber.
pure_paid=smallunits+[('u',e+1),('closed_half_weight',4*e-k-4),('closed_base_zero',e-1),('closed_consistency_line',4*e-k)]
for label,pp in inputs:
 out,trace=nf(pp)
 assert all(m[0]+m[1]<=1 and m[3]==0 for m in out)
 for vv in out.values():check_paid_den(vv.d)
 for tr in trace:
  for vv in tr.values():check_paid_den(vv.d)
 den=bo
 for vv in out.values():den=den*vv.d/den.gcd(vv.d)
 check_paid_den(den)
 poly=zz
 for mon,vv in out.items():
  cf=vv.n*(den/vv.d)
  for (ie,ik),aa in cf.to_dict().items():poly+=aa*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
 paidprod=oo;history=[]
 for nm,atom in pure_paid:
  count=0
  while poly:
   gg=poly.gcd(atom)
   if gg.total_degree()==0:break
   rr=poly/gg;assert rr*gg==poly;poly=rr;paidprod*=gg;count+=1
  if count:history.append((nm,count))
 assert not subp(scalep(split(poly),split(paidprod)[zero_mon]),scalep(out,BR(den)))
 rows.append(poly);row_names.append(label)
 say({'stage':'original_normal_form_and_trace_multiplied_back','name':label,'degrees':list(map(int,poly.degrees())),'terms':len(poly.to_dict()),'paidRemovals':history,'allCoefficientDenominatorsVerified':True,'sha256':hashlib.sha256(str(sorted(poly.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
# All rows are linear in lambda,f with constant coordinate exactly 1.
# Thus each minor is an explicit polynomial combination of three original rows.
coeffrows=[]
for pp in rows:
 rr=[]
 for na,nf0 in [(1,0),(0,1),(0,0)]:
  rr.append(ctx.from_dict({tuple(int(m[i]) if i not in [2,3] else 0 for i in range(7)):aa for m,aa in pp.to_dict().items() if int(m[2])==na and int(m[3])==nf0}))
 assert pp==rr[0]*la+rr[1]*fp+rr[2];coeffrows.append(rr)
minor_paid=pure_paid+[('closed_zero_singleton_pairing',v)]
minors=[];minor_names=[]
for inds in itertools.combinations(range(6),3):
 aa,bb,cc=[coeffrows[i] for i in inds]
 minor=aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])-aa[1]*(bb[0]*cc[2]-bb[2]*cc[0])+aa[2]*(bb[0]*cc[1]-bb[1]*cc[0])
 assert minor==(bb[0]*cc[1]-bb[1]*cc[0])*rows[inds[0]]-(aa[0]*cc[1]-aa[1]*cc[0])*rows[inds[1]]+(aa[0]*bb[1]-aa[1]*bb[0])*rows[inds[2]]
 if not minor:continue
 rawminor=minor;paidprod=oo;history=[]
 for nm,atom in minor_paid:
  count=0
  while minor:
   gg=minor.gcd(atom)
   if gg.total_degree()==0:break
   rr=minor/gg;assert rr*gg==minor;minor=rr;paidprod*=gg;count+=1
  if count:history.append((nm,count))
 assert minor*paidprod==rawminor
 assert all(int(m[2])==int(m[3])==int(m[5])==int(m[6])==0 for m in minor.to_dict())
 minors.append(minor);minor_names.append(inds)
 say({'stage':'original_three_parameter_minor','rows':inds,'degrees':list(map(int,minor.degrees())),'terms':len(minor.to_dict()),'originalRowCombinationMultipliedBack':True,'paidRemovals':history,'sha256':hashlib.sha256(str(sorted(minor.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
assert len(minors)==20

# The full original mean Dixon identity is generated by divided differences.
# It is a polynomial original-ideal combination, not merely a norm condition.
import signal
from flint import fmpq_poly
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
q0=polys[:3]
qalpha=[ctx.from_dict({(int(m[0]),int(m[1]),0,int(m[3]),int(m[4]),int(m[2]),0):aa for m,aa in q.to_dict().items()}) for q in q0]
qalphabeta=[ctx.from_dict({(int(m[0]),int(m[1]),0,0,int(m[4]),int(m[2]),int(m[3])):aa for m,aa in q.to_dict().items()}) for q in q0]
dx=[];dy=[]
for i in range(3):
 fx=(qalpha[i]-q0[i])/(eta-la);fy=(qalphabeta[i]-qalpha[i])/(invUnit-fp)
 assert fx*(eta-la)==qalpha[i]-q0[i]
 assert fy*(invUnit-fp)==qalphabeta[i]-qalpha[i]
 dx.append(fx);dy.append(fy)
dixon_cof=[dx[1]*dy[2]-dx[2]*dy[1],dx[2]*dy[0]-dx[0]*dy[2],dx[0]*dy[1]-dx[1]*dy[0]]
dixon=sum((q*c for q,c in zip(q0,dixon_cof)),zz)
num=q0[0]*(qalpha[1]*qalphabeta[2]-qalpha[2]*qalphabeta[1])-q0[1]*(qalpha[0]*qalphabeta[2]-qalpha[2]*qalphabeta[0])+q0[2]*(qalpha[0]*qalphabeta[1]-qalpha[1]*qalphabeta[0])
assert dixon*(la-eta)*(fp-invUnit)==num
mons=sorted(set((int(m[5]),int(m[6])) for m in dixon.to_dict()))
assert mons==[(0,0),(0,1),(1,0),(1,1),(2,0)]
def abcoef(p,ia,ib):
 return ctx.from_dict({(int(m[0]),int(m[1]),int(m[2]),int(m[3]),int(m[4]),0,0):aa for m,aa in p.to_dict().items() if int(m[5])==ia and int(m[6])==ib})
drows=[];dab=[]
for ia,ib in mons:
 dp=abcoef(dixon,ia,ib)
 assert dp==sum((q*abcoef(c,ia,ib) for q,c in zip(q0,dixon_cof)),zz)
 out,trace=nf(split(dp))
 for aa in out.values():check_paid_den(aa.d)
 for tr0 in trace:
  for aa in tr0.values():check_paid_den(aa.d)
 if not out:
  say({'stage':'original_Dixon_coefficient_reduced','alphaBetaMonomial':[ia,ib],'zero':True,'originalMeanCombinationVerified':True});continue
 assert all(mon[0]+mon[1]<=1 and mon[3]==0 for mon in out)
 den=bo
 for aa in out.values():den=den*aa.d/den.gcd(aa.d)
 check_paid_den(den);row=zz
 for mon,aa in out.items():
  for (ie,ik),cc in (aa.n*(den/aa.d)).to_dict().items():row+=cc*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
 rawrow=row;paid=oo
 for nm,at in pure_paid:
  while row:
   gg=row.gcd(at)
   if gg.total_degree()==0:break
   rr=row/gg;assert rr*gg==row;row=rr;paid*=gg
 assert row*paid==rawrow
 assert not subp(scalep(split(row),split(paid)[zero_mon]),scalep(out,BR(den)))
 drows.append(row);dab.append([ia,ib])
 say({'stage':'original_Dixon_coefficient_reduced','alphaBetaMonomial':[ia,ib],'degrees':list(map(int,row.degrees())),'terms':len(row.to_dict()),'originalMeanCombinationVerified':True,'normalFormTraceMultipliedBack':True,'sha256':hashlib.sha256(str(sorted(row.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
assert len(drows)==3
DC=[]
for pp in drows:
 cc=[]
 for ia,ib in [(1,0),(0,1),(0,0)]:cc.append(ctx.from_dict({(int(m[0]),int(m[1]),0,0,int(m[4]),0,0):aa for m,aa in pp.to_dict().items() if int(m[2])==ia and int(m[3])==ib}))
 assert pp==cc[0]*la+cc[1]*fp+cc[2];DC.append(cc)
aa,bb,cc=DC
Dmean=aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])-aa[1]*(bb[0]*cc[2]-bb[2]*cc[0])+aa[2]*(bb[0]*cc[1]-bb[1]*cc[0])
assert Dmean==(bb[0]*cc[1]-bb[1]*cc[0])*drows[0]-(aa[0]*cc[1]-aa[1]*cc[0])*drows[1]+(aa[0]*bb[1]-aa[1]*bb[0])*drows[2]
rawD=Dmean;paid=oo
for nm,at in minor_paid:
 while Dmean:
  gg=Dmean.gcd(at)
  if gg.total_degree()==0:break
  rr=Dmean/gg;assert rr*gg==Dmean;Dmean=rr;paid*=gg
assert Dmean*paid==rawD
pctx=fmpq_mpoly_ctx.get(('e','k','v'),'lex');pe,pk,pv=pctx.gens();pz=pctx.constant(0);po=pctx.constant(1)
def lower(p):
 assert all(int(m[2])==int(m[3])==int(m[5])==int(m[6])==0 for m in p.to_dict())
 return pctx.from_dict({(int(m[0]),int(m[1]),int(m[4])):aa for m,aa in p.to_dict().items()})
PD=lower(Dmean);P=lower(minors[minor_names.index((0,4,5))]);P35=lower(minors[minor_names.index((0,3,5))]);P34=lower(minors[minor_names.index((0,3,4))])
assert list(map(int,PD.degrees()))==[25,20,8]
assert list(map(int,P.degrees()))==[19,16,6]
say({'stage':'original_Dixon_scalar_identity_complete','degrees':list(map(int,PD.degrees())),'terms':len(PD.to_dict()),'polynomialSha256':hashlib.sha256(str(sorted(PD.to_dict().items())).encode()).hexdigest(),'allOriginalRowCombinationsVerified':True,'claimExcluded':False})

# New original same-eta quadratic, returned through the three original means.
qa_out,qa_trace=nf(split(Qalign))
for aa in qa_out.values():check_paid_den(aa.d)
for tr0 in qa_trace:
 for aa in tr0.values():check_paid_den(aa.d)
den=bo
for aa in qa_out.values():den=den*aa.d/den.gcd(aa.d)
check_paid_den(den);qarow=zz
for mon,aa in qa_out.items():
 for (ie,ik),cc in (aa.n*(den/aa.d)).to_dict().items():qarow+=cc*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
rawqa=qarow;paidqa=oo
for nm,at in pure_paid:
 while qarow:
  gg=qarow.gcd(at)
  if gg.total_degree()==0:break
  rr=qarow/gg;assert rr*gg==qarow;qarow=rr;paidqa*=gg
assert qarow*paidqa==rawqa
assert not subp(scalep(split(qarow),split(paidqa)[zero_mon]),scalep(qa_out,BR(den)))
assert len(qarow.to_dict())==451 and list(map(int,qarow.degrees()))==[12,10,1,1,2,0,0]
say({'stage':'same_eta_quadratic_original_return','terms':451,'degrees':list(map(int,qarow.degrees())),'sameEtaOriginalIdentityMultipliedBack':True,'meanTraceMultipliedBack':True,'noDivisionByBnum':True,'sha256':hashlib.sha256(str(sorted(qarow.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
qa_coeff=[]
for ia,ib in [(1,0),(0,1),(0,0)]:qa_coeff.append(ctx.from_dict({(int(m[0]),int(m[1]),0,0,int(m[4]),0,0):aa for m,aa in qarow.to_dict().items() if int(m[2])==ia and int(m[3])==ib}))
assert qarow==qa_coeff[0]*la+qa_coeff[1]*fp+qa_coeff[2]
new_minors=[]
for other in [4,5]:
 rowvecs=[rows[0],rows[other],qarow];aa,bb,cc=[coeffrows[0],coeffrows[other],qa_coeff]
 mm=aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])-aa[1]*(bb[0]*cc[2]-bb[2]*cc[0])+aa[2]*(bb[0]*cc[1]-bb[1]*cc[0])
 assert mm==(bb[0]*cc[1]-bb[1]*cc[0])*rowvecs[0]-(aa[0]*cc[1]-aa[1]*cc[0])*rowvecs[1]+(aa[0]*bb[1]-aa[1]*bb[0])*rowvecs[2]
 originalmm=mm;removed=oo;history=[]
 for nm,at in minor_paid:
  count=0
  while mm:
   gg=mm.gcd(at)
   if gg.total_degree()==0:break
   rr=mm/gg;assert rr*gg==mm;mm=rr;removed*=gg;count+=1
  if count:history.append([nm,count])
 assert mm*removed==originalmm;new_minors.append(lower(mm))
 say({'stage':'new_original_same_eta_minor','oldOriginalRows':[0,other],'thirdRow':'Qa','degrees':list(map(int,new_minors[-1].degrees())),'terms':len(mm.to_dict()),'paidRemovals':history,'originalCombinationMultipliedBack':True,'sha256':hashlib.sha256(str(sorted(new_minors[-1].to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
Q5,Q4=new_minors
assert list(map(int,Q5.degrees()))==[22,19,5] and len(Q5.to_dict())==1085
assert list(map(int,Q4.degrees()))==[21,16,4] and len(Q4.to_dict())==764
L4=pctx.from_dict({(int(m[0]),int(m[1]),0):aa for m,aa in Q4.to_dict().items() if int(m[2])==4})
B118=L4/L4.coefficient(0)
assert list(map(int,B118.degrees()))==[11,8,0] and len(B118.to_dict())==83
assert B118*L4.coefficient(0)==L4
lcK=pctx.from_dict({(int(m[0]),0,0):aa for m,aa in B118.to_dict().items() if int(m[1])==8})
assert lcK==-pe*pe*(37*pe**3+54*pe*pe-32*pe+4)/512
say({'stage':'complete_new_quartic_leading_coefficient','degree':4,'leadingFactorDegrees':[11,8],'leadingFactorTerms':83,'leadingFactorSha256':hashlib.sha256(str(sorted(B118.to_dict().items())).encode()).hexdigest(),'leadingScalar':str(L4.coefficient(0)),'allKLeadingZeroFibersRetained':True,'claimExcluded':False})
param_paid=[(nm,lower(at)) for nm,at in pure_paid]+[('closed_zero_singleton_pairing',pv),('closed_quadratic_invariant_curve',2*pe*pe-pe*pk+2)]
def strip_param(raw):
 rr=raw;paid=po;history=[]
 for nm,at in param_paid:
  count=0
  while rr:
   gg=rr.gcd(at)
   if gg.total_degree()==0:break
   red=rr/gg;assert red*gg==rr;rr=red;paid*=gg;count+=1
  if count:history.append([nm,count])
 assert rr*paid==raw
 return rr,history
def digest_poly(p):return hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()
# FULL resultants, followed by FULL factorizations and exact reconstruction.
# We do not replace a multivariate common-zero set by a multivariate gcd.
projection_factors=[]
for label,aa,bb,expected in [('original_Dixon',P,PD,[[33,21,0],[38,32,0]]),('same_eta_Q5_Q4',Q5,Q4,[[24,20,0],[83,64,0]])]:
 raw=aa.resultant(bb,'v');assert raw
 rr,history=strip_param(raw)
 scalar,factors=rr.factor();multiply=pctx.constant(scalar)
 for fac,mult in factors:multiply*=fac**mult
 assert multiply==rr
 assert sorted([list(map(int,fac.degrees())) for fac,mult in factors])==expected
 projection_factors.append([fac for fac,mult in factors])
 say({'stage':'complete_original_parameter_projection_factorization','input':label,'fullResultantDegrees':list(map(int,raw.degrees())),'paidRemovals':history,'remainingDegrees':list(map(int,rr.degrees())),'sha256':digest_poly(rr),'allFactors':[{'degrees':list(map(int,fac.degrees())),'multiplicity':int(mult),'terms':len(fac.to_dict()),'sha256':digest_poly(fac)} for fac,mult in factors],'wholeFactorizationMultipliedBack':True,'claimExcluded':False})

# Scope: the ENTIRE A_(24,20)=0 component of the new Qa projection.
# The other Qa factor C_(83,64) is not excluded by this source.
A24=next(fac for fac in projection_factors[1] if list(map(int,fac.degrees()))==[24,20,0])
assert len(A24.to_dict())==309
ue=fmpq_poly([0,1])
paid_e=[('original_e',ue),('zero_base_weight',ue-1),('original_u',ue+1),('complete_ehalf_fiber',ue-fmpq(1,2)),('complete_77e16_fiber',ue-fmpq(16,77))]
def as_e_polynomial(pp):
 assert all(int(m[1])==int(m[2])==0 for m in pp.to_dict())
 coeff=[fmpq(0)]*(int(pp.degrees()[0])+1)
 for m,aa in pp.to_dict().items():coeff[int(m[0])]=aa
 return fmpq_poly(coeff)
cover=fmpq_poly([1])
for fac in sorted(projection_factors[0],key=lambda p:int(p.degrees()[1])):
 full=A24.resultant(fac,'k');assert full
 rp=as_e_polynomial(full);remainder=rp;unit_product=fmpq_poly([1]);history=[]
 for name,unit in paid_e:
  count=0
  while True:
   qq,rr=divmod(remainder,unit)
   if rr:break
   assert qq*unit==remainder;remainder=qq;unit_product*=unit;count+=1
  if count:history.append([name,count])
 assert remainder*unit_product==rp
 cover*=remainder
 say({'stage':'entire_A24_original_QQ_parameter_cover','otherCurveDegrees':list(map(int,fac.degrees())),'fullDegree':rp.degree(),'paidParameterDivisions':history,'remainingDegree':remainder.degree(),'fullQQDivisionsMultipliedBack':True,'fullResultantSha256':digest_poly(full),'remainingSha256':hashlib.sha256(str(remainder).encode()).hexdigest(),'claimExcluded':False})
assert cover.degree()==799
# Generate an additional FULL original v projection over QQ before reducing.
raw35=P.resultant(P35,'v');assert raw35
proj35,history=strip_param(raw35)
assert list(map(int,proj35.degrees()))==[132,109,0]
say({'stage':'additional_full_original_QQ_projection','input':'P045/P035','rawDegrees':list(map(int,raw35.degrees())),'afterPaidDegrees':list(map(int,proj35.degrees())),'paidRemovals':history,'sha256':digest_poly(proj35),'allOriginalLeadingZeroFibersRetained':True,'claimExcluded':False})
# Let S(e)=Res_k(A24,proj35) in QQ[e], with the FULL k degrees 20 and109.
# Its complete reduction can be evaluated without forming large QQ coefficients.
# We verify all rational denominators and BOTH eliminated-variable degrees.
from flint import nmod_poly,nmod_mpoly_ctx
prime=1031;modctx=nmod_mpoly_ctx.get(('e','k'),ordering='lex',modulus=prime)
def reduce_coefficient(aa):
 den=int(aa.denominator)%prime;assert den
 return (int(aa.numerator)%prime)*pow(den,-1,prime)%prime

def full_bivariate_reduction(pp):
 assert all(int(m[2])==0 for m in pp.to_dict())
 out=modctx.from_dict({(int(m[0]),int(m[1])):reduce_coefficient(aa) for m,aa in pp.to_dict().items()})
 assert int(out.degrees()[1])==int(pp.degrees()[1])
 return out
Amod=full_bivariate_reduction(A24);Bmod=full_bivariate_reduction(proj35)
assert [int(Amod.degrees()[1]),int(Bmod.degrees()[1])]==[20,109]
Smod=Amod.resultant(Bmod,'k');assert Smod
coeff=[0]*(int(Smod.degrees()[0])+1)
for m,aa in Smod.to_dict().items():assert int(m[1])==0;coeff[int(m[0])]=int(aa)
Sbar=nmod_poly(coeff,prime)
Cbar=nmod_poly([reduce_coefficient(aa) for aa in cover],prime)
assert Cbar.degree()==cover.degree()==799
one,bb,cc=Cbar.xgcd(Sbar)
assert one==bb*Cbar+cc*Sbar and one==1
# QQ conclusion uses only a one-variable Gauss lemma:
# cover has integral coefficients at1031 and its full leading coefficient
# is a local unit. A positive-degree QQ divisor common to cover and S is
# monic/integral at1031, hence remains a nonconstant common divisor mod1031.
# The exact product-one identity above rules that out. This is NOT an inference
# from an arbitrary multivariate modular unit ideal.
say({'stage':'entire_A24_one_variable_characteristic_zero_obstruction','QQCandidateDegree':cover.degree(),'sameModularCandidateDegree':Cbar.degree(),'SylvesterKDegreesQQ':[int(A24.degrees()[1]),int(proj35.degrees()[1])],'sameSylvesterKDegreesMod':[int(Amod.degrees()[1]),int(Bmod.degrees()[1])],'fullResultantReductionDegree':Sbar.degree(),'prime':prime,'bezoutCoefficientDegrees':[bb.degree(),cc.degree()],'actualModularBezoutProductOne':True,'allInputDenominatorsPrimeToPrime':True,'completeSylvesterSpecializationVerified':True,'coverSha256':hashlib.sha256(str(cover).encode()).hexdigest(),'SylvesterReductionSha256':hashlib.sha256(str(Sbar).encode()).hexdigest(),'bezoutSha256':hashlib.sha256((str(bb)+'|'+str(cc)).encode()).hexdigest(),'claimExcluded':True})
signal.alarm(0)
say({'stage':'complete','scope':'entire A24(e,k)=0 curve of the original same-eta Q5/Q4 projection on S0 Lt0','remainingQaCurve':'C83(e,k)=0','wholeS0Lt0ExclusionClaim':False,'ordinaryISPClaim':False,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'claimExcluded':True})
