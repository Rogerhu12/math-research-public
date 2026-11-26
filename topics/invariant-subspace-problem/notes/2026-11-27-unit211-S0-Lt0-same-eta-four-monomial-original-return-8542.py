#!/usr/bin/env python3
"""R150 S0/Lt0: same-eta six original relations and four-monomial generation.
Every polynomial comes from the original Frobenius Gram or an exact paid
coordinate transformation. Every change has both original and rule combination traces.
The four monomials span; freeness, a unit ideal, and exclusion are not claimed.
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

import signal
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
# Six specified ORIGINAL equations, not a claim about the entire critical ideal.
O=SP[:3]+[split(Malign),split(Mnormal),split(Mnorm)]
Onames=['E1','EB_even','EB_odd','same_eta_alignment','original_Nvalue','same_eta_norm']
partials=[];partial_traces=[]
for p in [Malign,Mnormal,Mnorm]:
 out,trace=nf(split(p));partials.append(out);partial_traces.append(trace)
eta_mons=[(1,0,0,1),(0,1,0,1)];etamat=[[p.get(m,BR()) for m in eta_mons] for p in partials[:2]]
deteta=etamat[0][0]*etamat[1][1]-etamat[0][1]*etamat[1][0]
assert deteta==split(32*x*x*j**4*(1-e))[zero_mon]
eta_inverse=[[etamat[1][1]/deteta,-etamat[0][1]/deteta],[-etamat[1][0]/deteta,etamat[0][0]/deteta]]
for a in range(2):
 for b in range(2):assert sum((etamat[a][q]*eta_inverse[q][b] for q in range(2)),BR())==BR(int(a==b))
eta_rest=[{m:aa for m,aa in pp.items() if m not in eta_mons} for pp in partials[:2]]
eta_rules=[]
for i in range(2):eta_rules.append(scalep(addp(scalep(eta_rest[0],eta_inverse[i][0]),scalep(eta_rest[1],eta_inverse[i][1])),BR(-1)))
norm_lead=partials[2][(0,0,0,2)];assert norm_lead==split(2*j*j)[zero_mon]
norm_rule=scalep({m:aa for m,aa in partials[2].items() if m!=(0,0,0,2)},BR(-1)/norm_lead)
all_rules=rules+eta_rules+[norm_rule];all_mons=quadmons+eta_mons+[(0,0,0,2)]
# Exact rows expressing each rewrite relation in the six original equations.
rule_traces=[]
for i in range(3):rule_traces.append([{zero_mon:adjB[i][q]/detc} for q in range(3)]+[{},{},{}])
for i in range(2):
 tr=[{} for q in range(6)]
 for q in range(2):
  weight=eta_inverse[i][q];tr[3+q]={zero_mon:weight}
  for a in range(3):tr[a]=subp(tr[a],scalep(partial_traces[q][a],weight))
 rule_traces.append(tr)
tr=[{} for q in range(6)];tr[5]={zero_mon:BR(1)/norm_lead}
for a in range(3):tr[a]=scalep(partial_traces[2][a],BR(-1)/norm_lead)
rule_traces.append(tr)
Rels=[subp({m:BR(1)},rhs) for m,rhs in zip(all_mons,all_rules)]
full_paid=detc.n*(bk+4)*(be-1)
new_denominator_checks=0
def check_full_paid_den(dd):
 global new_denominator_checks
 p=dd
 while p.total_degree()>0:
  gg=p.gcd(full_paid);assert gg.total_degree()>0
  qq=p/gg;assert qq*gg==p;p=qq
 assert p;new_denominator_checks+=1
for i,(rel,tr) in enumerate(zip(Rels,rule_traces)):
 check=dict(rel)
 for q in range(6):check=subp(check,mulp(tr[q],O[q]))
 assert not check
 assert all(m[0]+m[1]+m[3]<=1 for m in all_rules[i])
 for aa in all_rules[i].values():check_full_paid_den(aa.d)
 for tt in tr:
  for aa in tt.values():check_full_paid_den(aa.d)
 say({'stage':'six_original_rewrite_relation_multiplied_back','monomial':all_mons[i],'vDegree':max(m[2] for m in all_rules[i]),'basisCoefficientCount':len(all_rules[i]),'originalRelationCombinationVerified':True,'claimExcluded':False})
say({'stage':'same_eta_paid_two_by_two_matrix_verified','determinant':'32*(k+4)^2*j^4*(1-e)','inverseMatrixIdentities':4,'etaSquaredLeadingCoefficient':'2*j^2','newPaidFactorsBeyondOriginalC':['k+4','e-1'],'basisClaim':'four formal spanning monomials; quotient independence not asserted','claimExcluded':False})
@functools.lru_cache(None)
def nf4mon(mon):
 a,b,c,d=mon
 if a+b+d<=1:return {mon:BR(1)},[{} for q in range(6)]
 index=next(i for i,mq in enumerate(all_mons) if all(mm>=nn for mm,nn in zip(mon,mq)))
 shift=tuple(mm-nn for mm,nn in zip(mon,all_mons[index]));out={};tr=[{} for q in range(6)];tr[index]={shift:BR(1)}
 for m,aa in all_rules[index].items():
  normal,tail=nf4mon(tuple(mm+nn for mm,nn in zip(m,shift)))
  out=addp(out,scalep(normal,aa))
  for q in range(6):tr[q]=addp(tr[q],scalep(tail[q],aa))
 return out,tr
def nf4(p):
 out={};tr=[{} for q in range(6)]
 for m,aa in p.items():
  normal,tail=nf4mon(m);out=addp(out,scalep(normal,aa))
  for q in range(6):tr[q]=addp(tr[q],scalep(tail[q],aa))
 check=subp(p,out)
 for q in range(6):check=subp(check,mulp(tr[q],Rels[q]))
 assert not check
 original_tr=[{} for q in range(6)]
 for q in range(6):
  for a in range(6):original_tr[a]=addp(original_tr[a],mulp(tr[q],rule_traces[q][a]))
 check=subp(p,out)
 for a in range(6):check=subp(check,mulp(original_tr[a],O[a]))
 assert not check
 for tt in tr+original_tr:
  for aa in tt.values():check_full_paid_den(aa.d)
 for aa in out.values():check_full_paid_den(aa.d)
 return out,tr,original_tr
# This is the converse inclusion: each of the six specified original equations
# is a verified combination of the six new rewriting relations.
for name,oo0 in zip(Onames,O):
 returned,tr,otr=nf4(oo0);assert not returned
 say({'stage':'reverse_original_ideal_inclusion_verified','originalEquation':name,'zeroRemainder':True,'ruleCombinationVerified':True,'claimExcluded':False})
paid_rows=smallunits+[('u',e+1),('closed_half_weight',4*e-k-4),('closed_base_zero',e-1)]
returned_rows=[];returned_names=[]
def row_from_normal(name,out):
 if not out:
  say({'stage':'original_four_monomial_return','name':name,'zero':True,'claimExcluded':False});return
 den=bo
 for aa in out.values():check_full_paid_den(aa.d);den=den*aa.d/den.gcd(aa.d)
 check_full_paid_den(den);p=zz
 for m,aa in out.items():
  for (ie,ik),cc in (aa.n*(den/aa.d)).to_dict().items():p+=cc*e**int(ie)*k**int(ik)*la**m[0]*fp**m[1]*v**m[2]*eta**m[3]
 raw=p;paid=oo;hist=[]
 for nm,atom in paid_rows:
  count=0
  while p:
   gg=p.gcd(atom)
   if gg.total_degree()==0:break
   rr=p/gg;assert rr*gg==p;p=rr;paid*=gg;count+=1
  if count:hist.append((nm,count))
 assert p*paid==raw
 assert not subp(scalep(split(p),split(paid)[zero_mon]),scalep(out,BR(den)))
 assert all(int(m[2])+int(m[3])+int(m[5])<=1 for m in p.to_dict())
 returned_rows.append(p);returned_names.append(name)
 say({'stage':'original_four_monomial_return','name':name,'degrees':list(map(int,p.degrees())),'terms':len(p.to_dict()),'normalizationMultipliedBack':True,'paidRemovals':hist,'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
for name,p in [('N1',polys[3]),('U_moment',Mmoment),('NB_even',polys[4]),('NB_odd',polys[5]),('PB_even',polys[6]),('PB_odd',polys[7])]:
 out,tr,otr=nf4(split(p));row_from_normal(name,out)
# All pairwise overlap checks of the six quadratic leading monomials.
# Coprime pairs have an exact product identity. The nine cubic overlaps
# retain a normal-form row, with its original source combination multiplied back.
overlap_count=0;coprime_count=0
for i,j0 in itertools.combinations(range(6),2):
 mi,mj=all_mons[i],all_mons[j0];lcm=tuple(max(a,b) for a,b in zip(mi,mj));si=tuple(a-b for a,b in zip(lcm,mi));sj=tuple(a-b for a,b in zip(lcm,mj))
 S=subp(shiftp(all_rules[i],si),shiftp(all_rules[j0],sj))
 src=subp(shiftp(Rels[j0],sj),shiftp(Rels[i],si));assert not subp(S,src)
 if all(min(a,b)==0 for a,b in zip(mi,mj)):
  identity=subp(mulp(all_rules[i],Rels[j0]),mulp(all_rules[j0],Rels[i]));assert not subp(S,identity);coprime_count+=1
  say({'stage':'coprime_overlap_product_identity_verified','rulePair':[i,j0],'claimExcluded':False});continue
 overlap_count+=1;assert sum(lcm)==3
 original_S=[subp(shiftp(rule_traces[j0][q],sj),shiftp(rule_traces[i][q],si)) for q in range(6)]
 check=dict(S)
 for q in range(6):check=subp(check,mulp(original_S[q],O[q]))
 assert not check
 out,tr,original_reduction=nf4(S)
 original_out=[subp(a,b) for a,b in zip(original_S,original_reduction)]
 check=dict(out)
 for q in range(6):
  check=subp(check,mulp(original_out[q],O[q]))
  for aa in original_out[q].values():check_full_paid_den(aa.d)
 assert not check
 row_from_normal('overlap_'+str(i)+'_'+str(j0),out)
assert overlap_count==9 and coprime_count==6
# One particularly small same-eta consequence, with no division by Bnum.
Qalign=Unum*Unum*Dnum-2*(1-e*k)*Bnum*Bnum
assert Dnum*Qalign==Malign*(Unum*Dnum+2*j*eta*Bnum)+2*Bnum*Bnum*Mnorm
# Dnum=Delta*2j^2 is paid by the complete h=k exclusion and original ell unit.
out,tr,otr=nf4(split(Qalign));row_from_normal('same_eta_alignment_norm_quadratic',out)
signal.alarm(0)
say({'stage':'complete_original_four_monomial_generation_and_consistency','sixSpecifiedOriginalGeneratorsLocalizedEquivalent':True,'wholeCriticalIdealEquivalenceClaim':False,'formalSpanningMonomials':['1','lambda','f','eta'],'quotientFreenessClaim':False,'cubicOverlapCount':overlap_count,'coprimeProductIdentityCount':coprime_count,'verifiedPaidCoefficientDenominators':new_denominator_checks,'returnedNecessaryRows':len(returned_rows),'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'claimExcluded':False,'ordinaryISPClaim':False})
