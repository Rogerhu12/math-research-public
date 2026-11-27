#!/usr/bin/env python3
"""R150 S0/Lt0: original two-parameter minors with global monic-e return and a QQ unit gate.
Regenerates every original trace and all H64/H16 boundaries, pays the actual
H9 common cofactor including its entire quadratic field, and retains every
Cramer leading-zero case. Build-only mode makes no general Lt0 exclusion claim.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(300)
resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
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


# Original same-eta quadratic, without dividing by B or a norm embedding.
Qa=Unum*Unum*Dnum-2*(1-e*k)*Bnum*Bnum
assert Dnum*Qa==Malign*(Unum*Dnum+2*j*eta*Bnum)+2*Bnum*Bnum*Mnorm
base=[*polys[:4],Qa]
mons=sorted([(a,b,c) for a in range(4) for b in range(4-a) for c in range(4-a-b)],key=lambda m:(sum(m),m),reverse=True)
assert len(mons)==20 and mons[-1]==(0,0,0)
original_rows=[]
for g in base:
 assert max(sum(map(int,m[2:5])) for m in g.to_dict())<=2
 for at in [la,fp,v,oo]:original_rows.append(g*at)
M=[]
for rowpoly in original_rows:
 rr=[]
 for mon in mons:
  rr.append(bctx.from_dict({(int(m[0]),int(m[1])):a for m,a in rowpoly.to_dict().items() if tuple(map(int,m[2:5]))==mon}))
 assert all(int(m[5])==int(m[6])==0 for m in rowpoly.to_dict())
 # Reconstruct each original row from its coefficient matrix, term for term.
 reconstructed=zz
 for mon,coef in zip(mons,rr):
  for (ie,ik),cc in coef.to_dict().items():reconstructed+=cc*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
 assert reconstructed==rowpoly
 M.append(rr)
def digest(p):return hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()
say({'stage':'entire_twenty_original_multiplication_rows_verified','variablesInMonomials':['lam','f','v'],'monomials':[list(m) for m in mons],'matrixSize':[20,20],'originalQuadratics':['E1','EB_even','EB_odd','N1elim','Qa'],'rowMultipliers':['lambda','f','v','1'],'matrixEntrySha256':hashlib.sha256('|'.join(digest(p) for row in M for p in row).encode()).hexdigest(),'allRowsMultipliedBack':True,'noRowContentDivided':True,'claimExcluded':False})
A=[list(row) for row in M];prev=bo;steps=[];row_sign=1
for z in range(19):
 swap=z
 if not A[z][z]:
  swap=next(i for i in range(z+1,20) if A[i][z])
  A[z],A[swap]=A[swap],A[z];row_sign=-row_sign
 pivot=A[z][z];assert pivot
 lower_col=[A[i][z] for i in range(z+1,20)]
 steps.append((pivot,lower_col,swap))
 for i in range(z+1,20):
  for q in range(z+1,20):
   numerator=A[i][q]*pivot-A[i][z]*A[z][q]
   red=numerator/prev;assert red*prev==numerator;A[i][q]=red
  A[i][z]=bz
 prev=pivot
 say({'stage':'twenty_matrix_fraction_free_step','index':z,'rowSwap':swap,'pivotDegrees':list(map(int,pivot.degrees())),'pivotTerms':len(pivot.to_dict()),'allDivisionsMultipliedBack':True,'noPointwisePivotInverted':True,'claimExcluded':False})
D=A[-1][-1];assert D
# Recover ONLY the cofactor row needed for the constant coordinate.  This is a
# reverse pass through the original row operations, not the failed expansion
# of a full ten-by-ten adjugate. Every reverse quotient is a polynomial.
cofactor=[bz for _ in range(20)];cofactor[-1]=steps[-1][0]
for z in range(18,-1,-1):
 pivot,lower_col,swap=steps[z]
 numerator=-sum((cofactor[i]*lower_col[i-z-1] for i in range(z+1,20)),bz)
 out=numerator/pivot;assert out*pivot==numerator;cofactor[z]=out
 if swap!=z:cofactor[z],cofactor[swap]=cofactor[swap],cofactor[z]
for q in range(20):
 multiplied=sum((cofactor[i]*M[i][q] for i in range(20)),bz)
 assert multiplied==(D if q==19 else bz)
# The constant monomial is exactly 1, so this actual row identity expresses D
# as a polynomial combination of the twenty original quadratic multiples.
say({'stage':'original_constant_coordinate_cofactor_row_multiplied_back','identities':20,'identity':'cofactor * original_M = (0,...,0,D)','constantCoordinateExactlyOne':True,'cofactorCoefficientDegrees':[list(map(int,p.degrees())) for p in cofactor],'cofactorSha256':hashlib.sha256('|'.join(digest(p) for p in cofactor).encode()).hexdigest(),'ordinaryOriginalIdealCombination':True,'claimExcluded':False})
constant,factors=D.factor();full=bctx.constant(constant)
for pp,multiplicity in factors:full*=pp**multiplicity
assert full==D
F41=next(pp for pp,multiplicity in factors if list(map(int,pp.degrees()))==[41,33])
assert digest(F41)=='ca1b9ef43348fdfa70bf1303051d4a5d9315a64a18c7b9b0f98c4ed1e2482144'
assert len(F41.to_dict())==846
be,bk=bctx.gens();bj=bk+2-2*be
bD3=4*be**3-3*be**2*bk-4*be**2+be*bk*bk+4*be*bk+4*be-bk-4
paid_product=be**4*bk**10*bj**6*(4*be-bk-4)**2*(4*be-bk)*bD3**10
ratio=D/(paid_product*F41);assert ratio and ratio.total_degree()==0
assert D==ratio*paid_product*F41
say({'stage':'complete_original_five_quadrics_parameter_factorization','fullDegrees':list(map(int,D.degrees())),'fullTerms':len(D.to_dict()),'fullSha256':digest(D),'scalar':str(ratio),'fullFactorization':'scalar*e^4*k^10*j^6*(4e-k-4)^2*(4e-k)*D3^10*F41_33','allFactorsMultipliedBack':True,'discardedUnpaidFactors':[],'remainingDegrees':[41,33],'remainingTerms':846,'remainingSha256':digest(F41),'newNecessaryEquation':'F41_33(e,k)=0','allOriginalLeadingZeroFibersRetained':True,'claimExcluded':False})

# The coefficient determinant of lambda*v and f*v in the SAME original
# N1 and Qa mean remainders. Every coefficient denominator is already paid.
qouts=[]
for pp in [polys[3],Qa]:
 out,traces=nf(split(pp));qouts.append(out)
headmons=[(1,0,1,0),(0,1,1,0),(0,0,2,0)]
heads=[[out.get(m,BR()) for m in headmons] for out in qouts]
head_raw=heads[0][0]*heads[1][1]-heads[0][1]*heads[1][0]
head_paid_atoms=[e,k,j,x,Dq,D3,e+1,e-1,4*e-k-4,4*e-k]
bhead_paid=[bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in at.to_dict().items()}) for at in head_paid_atoms]
def paid_den(den):
 dd=den
 for at in bhead_paid:
  while dd.total_degree()>0:
   gg=dd.gcd(at)
   if gg.total_degree()==0:break
   rr=dd/gg;assert rr*gg==dd;dd=rr
 assert dd and dd.total_degree()==0
for out in qouts:
 for aa in out.values():paid_den(aa.d)
paid_den(head_raw.d)
H64=head_raw.n;head_paid=bo
for at in bhead_paid:
 while H64:
  gg=H64.gcd(at)
  if gg.total_degree()==0:break
  rr=H64/gg;assert rr*gg==H64;H64=rr;head_paid*=gg
assert H64*head_paid==head_raw.n
assert list(map(int,H64.degrees()))==[6,4] and len(H64.to_dict())==24
assert digest(H64)=='c2ab52cf20759d7bfb7e1d4bdb27ad62fc9d64b4534952b1046a4e6ef61c7159'
say({'stage':'original_quadratic_head_determinant','monomials':['lambda*v','f*v'],'rows':['original_N1_mean_remainder','original_Qa_mean_remainder'],'degrees':[6,4],'terms':24,'polynomial':str(H64),'sha256':digest(H64),'rawNumeratorEqualsPaidProductTimesH':True,'allCoefficientDenominatorsPaid':True,'claimExcluded':False})
# Full QQ resultant, including all k-leading-zero fibers of either polynomial.
from flint import fmpq_poly,nmod_poly,nmod_mpoly_ctx
full_cover=H64.resultant(F41,'k');assert full_cover
coeff=[fmpq(0)]*(int(full_cover.degrees()[0])+1)
for mm,aa in full_cover.to_dict().items():assert int(mm[1])==0;coeff[int(mm[0])]=aa
Rcover=fmpq_poly(coeff);cover=Rcover;ue=fmpq_poly([0,1]);paid_e=[('original_e',ue),('zero_base_weight',ue-1),('original_u',ue+1),('entire_ehalf',ue-fmpq(1,2)),('entire_77e16',ue-fmpq(16,77))]
paid_cover=fmpq_poly([1]);hist=[]
for name,at in paid_e:
 n=0
 while True:
  qq,rr=divmod(cover,at)
  if rr:break
  assert qq*at==cover;cover=qq;paid_cover*=at;n+=1
 if n:hist.append([name,n])
assert cover*paid_cover==Rcover
assert Rcover.degree()==230 and cover.degree()==89
say({'stage':'whole_quadratic_head_QQ_parameter_cover','fullDegree':230,'remainingDegree':89,'paidDivisions':hist,'allQQDivisionsMultipliedBack':True,'fullSha256':hashlib.sha256(str(Rcover).encode()).hexdigest(),'remainingSha256':hashlib.sha256(str(cover).encode()).hexdigest(),'allOriginalKLeadingZeroFibersRetained':True,'claimExcluded':False})
# Additional original P045/P035 projection, rebuilt only from N1, the U moment
# and two exact overlaps of the three original means. No old coefficient data.
CP1=addp(shiftp(rules[0],(0,1,0,0)),scalep(shiftp(rules[1],(1,0,0,0)),BR(-1)))
CP2=addp(shiftp(rules[1],(0,1,0,0)),scalep(shiftp(rules[2],(1,0,0,0)),BR(-1)))
for cp,i,jj in [(CP1,0,1),(CP2,1,2)]:
 tr=[addp({(1,0,0,0):adjB[jj][q]/detc},{(0,1,0,0):-adjB[i][q]/detc}) for q in range(3)]
 ck=dict(cp)
 for q in range(3):ck=subp(ck,mulp(tr[q],SP[q]))
 assert not ck
pure_paid=smallunits+[('u',e+1),('closed_half_weight',4*e-k-4),('closed_base_zero',e-1),('closed_consistency_line',4*e-k)]
minor_paid=pure_paid+[('closed_zero_singleton_pairing',v)]
rrows=[];rrcoefs=[]
for name,pp in [('N1',SP[3]),('U_moment',split(Mmoment)),('mean_S1',CP1),('mean_S2',CP2)]:
 out,tr=nf(pp)
 for aa in out.values():paid_den(aa.d)
 for tr0 in tr:
  for aa in tr0.values():paid_den(aa.d)
 den=bo
 for aa in out.values():den=den*aa.d/den.gcd(aa.d)
 paid_den(den);rpoly=zz
 for mon,aa in out.items():
  for (ie,ik),cc in (aa.n*(den/aa.d)).to_dict().items():rpoly+=cc*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
 rawrow=rpoly;paid=oo
 for nm,at in pure_paid:
  while rpoly:
   gg=rpoly.gcd(at)
   if gg.total_degree()==0:break
   rr=rpoly/gg;assert rr*gg==rpoly;rpoly=rr;paid*=gg
 assert rpoly*paid==rawrow
 assert not subp(scalep(split(rpoly),split(paid)[(0,0,0,0)]),scalep(out,BR(den)))
 coef=[]
 for ia,ib in [(1,0),(0,1),(0,0)]:coef.append(ctx.from_dict({(int(m[0]),int(m[1]),0,0,int(m[4]),0,0):cc for m,cc in rpoly.to_dict().items() if int(m[2])==ia and int(m[3])==ib}))
 assert rpoly==coef[0]*la+coef[1]*fp+coef[2]
 rrows.append(rpoly);rrcoefs.append(coef)
 say({'stage':'original_low_row_for_boundary_return','name':name,'degrees':list(map(int,rpoly.degrees())),'terms':len(rpoly.to_dict()),'originalTraceAndPaidNormalizationMultipliedBack':True,'claimExcluded':False})
pctx=fmpq_mpoly_ctx.get(('e','k','v'),'lex');pe,pk,pv=pctx.gens();pz=pctx.constant(0);po=pctx.constant(1)
def lower(p):
 assert all(int(m[2])==int(m[3])==int(m[5])==int(m[6])==0 for m in p.to_dict())
 return pctx.from_dict({(int(m[0]),int(m[1]),int(m[4])):aa for m,aa in p.to_dict().items()})
selected=[]
for label,inds in [('P045',(0,2,3)),('P035',(0,1,3))]:
 aa,bb,cc=[rrcoefs[i] for i in inds]
 p=aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])-aa[1]*(bb[0]*cc[2]-bb[2]*cc[0])+aa[2]*(bb[0]*cc[1]-bb[1]*cc[0])
 assert p==(bb[0]*cc[1]-bb[1]*cc[0])*rrows[inds[0]]-(aa[0]*cc[1]-aa[1]*cc[0])*rrows[inds[1]]+(aa[0]*bb[1]-aa[1]*bb[0])*rrows[inds[2]]
 rawp=p;paid=oo
 for nm,at in minor_paid:
  while p:
   gg=p.gcd(at)
   if gg.total_degree()==0:break
   rr=p/gg;assert rr*gg==p;p=rr;paid*=gg
 assert p*paid==rawp;selected.append(lower(p))
 say({'stage':'original_boundary_return_minor','name':label,'degrees':list(map(int,selected[-1].degrees())),'terms':len(p.to_dict()),'originalCombinationMultipliedBack':True,'sha256':digest(selected[-1]),'claimExcluded':False})
P045,P035=selected
raw_projection=P045.resultant(P035,'v');assert raw_projection
proj=raw_projection;paid_projection=po;hist=[]
param_paid=[(nm,lower(at)) for nm,at in pure_paid]+[('closed_v_zero',pv),('closed_Omega',2*pe*pe-pe*pk+2)]
for nm,at in param_paid:
 n=0
 while proj:
  gg=proj.gcd(at)
  if gg.total_degree()==0:break
  rr=proj/gg;assert rr*gg==proj;proj=rr;paid_projection*=gg;n+=1
 if n:hist.append([nm,n])
assert proj*paid_projection==raw_projection
assert list(map(int,proj.degrees()))==[132,109,0]
say({'stage':'full_additional_original_QQ_projection','input':'P045/P035','rawDegrees':list(map(int,raw_projection.degrees())),'afterPaidDegrees':[132,109,0],'paidRemovals':hist,'allDivisionsMultipliedBack':True,'sha256':digest(proj),'allVLeadingZeroFibersRetained':True,'claimExcluded':False})
# Let S(e)=Res_k(H64,proj) with the full k degrees 4 and 109.  This evaluates
# its complete reduction, never a changed-degree or dehomogenized resultant.
prime=1031;modctx=nmod_mpoly_ctx.get(('e','k'),ordering='lex',modulus=prime)
def red_coeff(aa):
 denominator=int(aa.denominator)%prime;assert denominator
 return int(aa.numerator)%prime*pow(denominator,-1,prime)%prime
Hm=modctx.from_dict({tuple(map(int,m)):red_coeff(aa) for m,aa in H64.to_dict().items()})
Pm=modctx.from_dict({(int(m[0]),int(m[1])):red_coeff(aa) for m,aa in proj.to_dict().items()})
assert int(Hm.degrees()[1])==int(H64.degrees()[1])==4
assert int(Pm.degrees()[1])==int(proj.degrees()[1])==109
Sm=Hm.resultant(Pm,'k');assert Sm
coeff=[0]*(int(Sm.degrees()[0])+1)
for m,aa in Sm.to_dict().items():assert int(m[1])==0;coeff[int(m[0])]=int(aa)
Sbar=nmod_poly(coeff,prime);Cbar=nmod_poly([red_coeff(aa) for aa in cover],prime)
assert Cbar.degree()==cover.degree()==89
unit,ss,tt=Cbar.xgcd(Sbar);assert unit==ss*Cbar+tt*Sbar and unit==1
say({'stage':'whole_quadratic_head_original_modular_Bezout','prime':1031,'actualQQCoverDegree':89,'modularCoverDegree':Cbar.degree(),'fullKDegreesQQ':[4,109],'fullKDegreesMod':[int(Hm.degrees()[1]),int(Pm.degrees()[1])],'fullResultantModDegree':Sbar.degree(),'coefficientDegrees':[ss.degree(),tt.degree()],'coefficientSha256':hashlib.sha256((str(ss)+'|'+str(tt)).encode()).hexdigest(),'resultantModSha256':hashlib.sha256(str(Sbar).encode()).hexdigest(),'actualBezoutMultipliedBack':True,'gaussLemmaLeadingUnitProvidedByActualQQCover':True,'arbitraryMultivariateModularUnitUsed':False,'claimExcluded':True})

# Five original quadratic heads, including the now paid H64 determinant.
Qa=Unum*Unum*Dnum-2*(1-e*k)*Bnum*Bnum
S5=[split(g) for g in [*polys[:4],Qa]]
leadmons=[(2,0,0,0),(1,1,0,0),(0,2,0,0),(1,0,1,0),(0,1,1,0)]
CM=[[p.get(m,BR()) for m in leadmons] for p in S5]
AB=[list(row)+[BR(1 if i==q else 0) for q in range(5)] for i,row in enumerate(CM)]
for z in range(5):
 if not AB[z][z]:
  j0=next(i for i in range(z+1,5) if AB[i][z]);AB[z],AB[j0]=AB[j0],AB[z]
 at=AB[z][z];AB[z]=[a/at for a in AB[z]]
 for i in range(5):
  if i==z:continue
  at=AB[i][z]
  if at:AB[i]=[a-at*b for a,b in zip(AB[i],AB[z])]
INV=[row[5:] for row in AB]
for i in range(5):
 for q in range(5):assert sum((INV[i][j0]*CM[j0][q] for j0 in range(5)),BR())==BR(1 if i==q else 0)
# H64 is the identical complete-boundary polynomial already generated above.
bpaid=[bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in at.to_dict().items()}) for at in [e,k,j,x,Dq,D3,e+1,e-1,4*e-k-4,4*e-k]]+[H64]
den_checks=0
def check_den(d):
 global den_checks
 p=d
 for a in bpaid:
  while p.total_degree()>0:
   gg=p.gcd(a)
   if gg.total_degree()==0:break
   rr=p/gg;assert rr*gg==p;p=rr
 assert p and p.total_degree()==0;den_checks+=1
for row in INV:
 for a in row:check_den(a.d)
rest=[{m:a for m,a in p.items() if m not in leadmons} for p in S5]
RULES=[]
for i in range(5):
 r={}
 for q in range(5):r=addp(r,scalep(rest[q],-INV[i][q]))
 assert all(sum(m[:3])<=1 or m==(0,0,2,0) for m in r)
 check=subp({leadmons[i]:BR(1)},r)
 for q in range(5):check=subp(check,scalep(S5[q],INV[i][q]))
 assert not check
 for a in r.values():check_den(a.d)
 RULES.append(r)
 say({'stage':'five_original_quadratic_rules','head':leadmons[i],'rightMonomials':[list(m) for m in r],'coefficientNumeratorDegrees':[list(map(int,a.n.degrees())) for a in r.values()],'rawOriginalCombinationVerified':True,'claimExcluded':False})
@functools.lru_cache(None)
def fnfmon(m):
 possible=next((i for i,h in enumerate(leadmons) if all(x>=y for x,y in zip(m,h))),None)
 if possible is None:return {m:BR(1)},[{} for _ in range(5)]
 ii=possible;shift=tuple(x-y for x,y in zip(m,leadmons[ii]));out={};tr=[{shift:INV[ii][q]} for q in range(5)]
 for n,a in RULES[ii].items():
  rest,qt=fnfmon(tuple(x+y for x,y in zip(n,shift)))
  out=addp(out,scalep(rest,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(qt[q],a))
 return out,tr

def fnf(p):
 out={};tr=[{} for _ in range(5)]
 for m,a in p.items():
  rr,tt=fnfmon(m);out=addp(out,scalep(rr,a))
  for q in range(5):tr[q]=addp(tr[q],scalep(tt[q],a))
 check=subp(p,out)
 for q in range(5):check=subp(check,mulp(tr[q],S5[q]))
 assert not check
 for a in out.values():check_den(a.d)
 for t in tr:
  for a in t.values():check_den(a.d)
 return out,tr

# The lambda*v, f*v overlap has no v^3; its v^2 coefficient is the already
# completely returned H16,13 parameter boundary.
p=subp(shiftp(RULES[3],(0,1,0,0)),shiftp(RULES[4],(1,0,0,0)))
input_trace=[addp(scalep(shiftp({(0,0,0,0):INV[3][q]},(0,1,0,0)),BR(-1)),shiftp({(0,0,0,0):INV[4][q]},(1,0,0,0))) for q in range(5)]
check=dict(p)
for q in range(5):check=subp(check,mulp(input_trace[q],S5[q]))
assert not check
out,tr=fnf(p)
assert (0,0,3,0) not in out
trace_out=[subp(input_trace[q],tr[q]) for q in range(5)]
check=dict(out)
for q in range(5):check=subp(check,mulp(trace_out[q],S5[q]))
assert not check
alpha=out[(0,0,2,0)];c0,fac=alpha.n.factor();assert len(fac)==1 and int(fac[0][1])==1;H16=fac[0][0];assert c0*H16==alpha.n
assert hashlib.sha256(str(sorted(H16.to_dict().items())).encode()).hexdigest()=='a17adccb80b9ec09219643cbee3c47a64f1ed3c27716623da8adfe559fc8b93e'

# Return the ENTIRE new v^2 leading coefficient boundary before dividing by it.
H16full=H16.resultant(F41,'k');assert H16full
hcoef=[fmpq(0)]*(int(H16full.degrees()[0])+1)
for m,aa in H16full.to_dict().items():assert int(m[1])==0;hcoef[int(m[0])]=aa
H16R=fmpq_poly(hcoef);H16C=H16R;hpaid=fmpq_poly([1]);hhist=[]
for name,at in paid_e:
 count=0
 while True:
  quotient,remainder=divmod(H16C,at)
  if remainder:break
  assert quotient*at==H16C;H16C=quotient;hpaid*=at;count+=1
 if count:hhist.append([name,count])
assert H16C*hpaid==H16R
assert H16R.degree()==665 and H16C.degree()==305
say({'stage':'whole_v2_leading_QQ_parameter_cover','leadingFactorDegrees':[16,13],'leadingFactorTerms':156,'leadingFactorSha256':digest(H16),'fullQQCoverDegree':665,'remainingQQDegree':305,'paidDivisions':hhist,'allQQDivisionsMultipliedBack':True,'fullSha256':hashlib.sha256(str(H16R).encode()).hexdigest(),'remainingSha256':hashlib.sha256(str(H16C).encode()).hexdigest(),'noKLeadingCoefficientInverted':True,'claimExcluded':False})
H16m=modctx.from_dict({tuple(map(int,m)):red_coeff(aa) for m,aa in H16.to_dict().items()})
assert int(H16m.degrees()[1])==int(H16.degrees()[1])==13
assert int(Pm.degrees()[1])==int(proj.degrees()[1])==109
H16S=H16m.resultant(Pm,'k');assert H16S
hcoef=[0]*(int(H16S.degrees()[0])+1)
for m,aa in H16S.to_dict().items():assert int(m[1])==0;hcoef[int(m[0])]=int(aa)
H16Sbar=nmod_poly(hcoef,prime);H16Cbar=nmod_poly([red_coeff(aa) for aa in H16C],prime)
assert H16Cbar.degree()==H16C.degree()==305
hg,hs,ht=H16Cbar.xgcd(H16Sbar)
assert hg==hs*H16Cbar+ht*H16Sbar and hg==1
say({'stage':'whole_v2_leading_original_modular_Bezout','prime':1031,'actualQQCandidateDegree':305,'modCandidateDegree':H16Cbar.degree(),'fullKDegreesQQ':[13,109],'fullKDegreesMod':[int(H16m.degrees()[1]),int(Pm.degrees()[1])],'fullResultantModDegree':H16Sbar.degree(),'coefficientDegrees':[hs.degree(),ht.degree()],'coefficientSha256':hashlib.sha256((str(hs)+'|'+str(ht)).encode()).hexdigest(),'resultantSha256':hashlib.sha256(str(H16Sbar).encode()).hexdigest(),'actualBezoutMultipliedBack':True,'sameGaussLemmaLeadingUnitAsH64':True,'wholeH16BoundaryExcluded':True,'claimExcluded':True})

bpaid.append(H16)
rule6=scalep({m:a for m,a in out.items() if m!=(0,0,2,0)},-BR(1)/alpha)
trace6=[scalep(t,BR(1)/alpha) for t in trace_out]
L6=leadmons+[(0,0,2,0)];R6=[];T6=[];v2coeff=[]
for i in range(5):
 c=RULES[i].get((0,0,2,0),BR());v2coeff.append(c)
 new=addp({m:a for m,a in RULES[i].items() if m!=(0,0,2,0)},scalep(rule6,c));R6.append(new)
 T6.append([addp({(0,0,0,0):INV[i][q]},scalep(trace6[q],c)) for q in range(5)])
R6.append(rule6);T6.append(trace6)
for i in range(6):
 assert all(sum(m)<=1 for m in R6[i])
 chk=subp({L6[i]:BR(1)},R6[i])
 for q in range(5):chk=subp(chk,mulp(T6[i][q],S5[q]))
 assert not chk
 for a in R6[i].values():check_den(a.d)
 for trr in T6[i]:
  for a in trr.values():check_den(a.d)
# Reverse ideal identities: the original five polynomials are combinations of
# these six monic relations, so this is the same localized selected ideal.
Rel6=[subp({m:BR(1)},rhs) for m,rhs in zip(L6,R6)]
for q in range(5):
 ck=dict(S5[q])
 for i in range(5):ck=subp(ck,scalep(subp(Rel6[i],scalep(Rel6[5],v2coeff[i])),CM[q][i]))
 assert not ck
say({'stage':'six_quadratic_original_rewrites_complete','spanningMonomials':['1','lambda','f','v'],'selectedOriginalIdealEqualityVerifiedBothDirections':True,'sameParameterBase':'QQ(e,k)','newDenominators':['H64','H16'],'claimFreeBasis':False,'claimExcluded':False})
@functools.lru_cache(None)
def n6mon(m):
 ii=next((i for i,h in enumerate(L6) if all(x>=y for x,y in zip(m,h))),None)
 if ii is None:return {m:BR(1)},[{} for _ in range(6)]
 sh=tuple(x-y for x,y in zip(m,L6[ii]));o={};tr=[{sh:BR(1)} if z==ii else {} for z in range(6)]
 for n,a in R6[ii].items():
  rr,qt=n6mon(tuple(x+y for x,y in zip(n,sh)));o=addp(o,scalep(rr,a))
  for q in range(6):tr[q]=addp(tr[q],scalep(qt[q],a))
 return o,tr

def n6(p):
 out={};tr=[{} for _ in range(6)]
 for m,a in p.items():
  rr,qt=n6mon(m);out=addp(out,scalep(rr,a))
  for q in range(6):tr[q]=addp(tr[q],scalep(qt[q],a))
 ck=subp(p,out)
 for q in range(6):ck=subp(ck,mulp(tr[q],Rel6[q]))
 assert not ck
 assert all(sum(m)<=1 for m in out)
 for a in out.values():check_den(a.d)
 for trr in tr:
  for a in trr.values():check_den(a.d)
 return out,tr
for p in S5:assert not n6(p)[0]
returned=[]
def ser(a):return {'n':[[list(map(int,m)),str(v)] for m,v in a.n.to_dict().items()],'d':[[list(map(int,m)),str(v)] for m,v in a.d.to_dict().items()]}
def rowlog(label,out):
 den=bo
 for a in out.values():den=den*a.d/den.gcd(a.d)
 check_den(den);cf=[out.get(m,BR()).n*(den/out[m].d) if m in out else bz for m in [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,0)]]
 rawcf=list(cf);paid=bo
 for at in bpaid:
  while True:
   gg=at
   for cc in cf:gg=gg.gcd(cc)
   if gg.total_degree()==0:break
   cf=[cc/gg for cc in cf];paid*=gg
 for aa,bb in zip(rawcf,cf):assert aa==paid*bb
 say({'stage':'four_basis_original_row','name':label,'degrees':[max(int(a.degrees()[i]) for a in cf if a) for i in [0,1]],'terms':sum(len(a.to_dict()) for a in cf),'sha256':hashlib.sha256('|'.join(str(sorted(a.to_dict().items())) for a in cf).encode()).hexdigest(),'twoLayerOriginalTraceAndPaidDivisionsVerified':True,'claimExcluded':False})
 returned.append({'name':label,'coefficients':[[[list(map(int,m)),str(a)] for m,a in p.to_dict().items()] for p in cf]})
for i,j0 in itertools.combinations(range(6),2):
 lcm=tuple(max(x,y) for x,y in zip(L6[i],L6[j0]))
 if sum(lcm)>3:continue
 p=subp(shiftp(R6[i],tuple(x-y for x,y in zip(lcm,L6[i]))),shiftp(R6[j0],tuple(x-y for x,y in zip(lcm,L6[j0]))))
 shj=tuple(x-y for x,y in zip(lcm,L6[j0]));shi=tuple(x-y for x,y in zip(lcm,L6[i]))
 origtrace=[addp({shj:BR(1)} if q==j0 else {},{shi:BR(-1)} if q==i else {}) for q in range(6)]
 ck=dict(p)
 for q in range(6):ck=subp(ck,mulp(origtrace[q],Rel6[q]))
 assert not ck
 out,tr=n6(p);rowlog('cubic_overlap_'+str(i)+'_'+str(j0),out)
# Same eta in ALL remaining original N/P equations.
nd=2*j*Bnum;nn=Unum*Dnum
assert Malign==nn-nd*eta
assert Zden*nn*nn-(1-e*k)*Dnum*nd*nd==Zden*Dnum*Qa
elist=[]
for label,p in [('Nvalue',Mnormal),('NB_odd',polys[5]),('PB_odd',polys[7])]:
 p0=ctx.from_dict({tuple(map(int,m)):a for m,a in p.to_dict().items() if int(m[5])==0})
 p1=ctx.from_dict({(int(m[0]),int(m[1]),int(m[2]),int(m[3]),int(m[4]),0,0):a for m,a in p.to_dict().items() if int(m[5])==1})
 assert p==p0+p1*eta
 rr=nd*p0+nn*p1;assert rr==nd*p+p1*Malign;elist.append((label,rr))
extra=[('U_moment',Mmoment),elist[0],('NB_even',polys[4]),elist[1],('PB_even',polys[6]),elist[2]]
for label,p in extra:
 out,tr=n6(split(p));rowlog(label,out)


# The common cofactor factor is the SECOND original quadratic-head minor,
# columns lambda*v,v^2; normalize its full scalar-times-single-factor identity.
hraw=heads[0][0]*heads[1][2]-heads[0][2]*heads[1][0]
paid_den(hraw.d);hn=hraw.n;hproduct=bo
for at in bhead_paid:
 while hn:
  gg=hn.gcd(at)
  if gg.total_degree()==0:break
  quotient=hn/gg;assert quotient*gg==hn;hn=quotient;hproduct*=gg
assert hn*hproduct==hraw.n
hscalar,hfactors=hn.factor();assert len(hfactors)==1 and int(hfactors[0][1])==1
H9=hfactors[0][0];assert hscalar*H9==hn
assert list(map(int,H9.degrees()))==[9,7] and len(H9.to_dict())==54
assert digest(H9)=='6fe1d2d2f22082738cada074f04da6afbf0f578a4a254948064103bf1a0092d1'
H9full=H9.resultant(F41,'k');assert H9full
coeff=[fmpq(0)]*(int(H9full.degrees()[0])+1)
for m,aa in H9full.to_dict().items():assert int(m[1])==0;coeff[int(m[0])]=aa
H9R=fmpq_poly(coeff);H9C=H9R;H9paid=fmpq_poly([1]);hist=[]
for name,at in paid_e:
 n=0
 while True:
  qq,rr=divmod(H9C,at)
  if rr:break
  assert qq*at==H9C;H9C=qq;H9paid*=at;n+=1
 if n:hist.append([name,n])
assert H9C*H9paid==H9R and H9R.degree()==386 and H9C.degree()==176
phi=fmpq_poly([1,0,1]);H9other,rem=divmod(H9C,phi);assert not rem and H9other*phi==H9C and H9other.degree()==174
H9m=modctx.from_dict({tuple(map(int,m)):red_coeff(aa) for m,aa in H9.to_dict().items()})
assert int(H9m.degrees()[1])==int(H9.degrees()[1])==7 and int(Pm.degrees()[1])==109
H9S=H9m.resultant(Pm,'k');assert H9S
coeff=[0]*(int(H9S.degrees()[0])+1)
for m,aa in H9S.to_dict().items():assert int(m[1])==0;coeff[int(m[0])]=int(aa)
H9Sbar=nmod_poly(coeff,prime);H9Cbar=nmod_poly([red_coeff(aa) for aa in H9other],prime)
assert H9Cbar.degree()==H9other.degree()==174
hg,hs,ht=H9Cbar.xgcd(H9Sbar);assert hg==hs*H9Cbar+ht*H9Sbar and hg==1
say({'stage':'whole_common_cofactor_QQ_cover_and_modular_return','leadingFactorDegrees':[9,7],'leadingFactorTerms':54,'leadingFactorSha256':digest(H9),'fullQQCoverDegree':386,'paidDivisions':hist,'remainingQQDegreeBeforeQuadratic':176,'exactQuadraticFactor':'e^2+1','otherQQDegree':174,'fullQQSha256':hashlib.sha256(str(H9R).encode()).hexdigest(),'otherQQSha256':hashlib.sha256(str(H9other).encode()).hexdigest(),'prime':1031,'preservedFullKDegrees':[7,109],'fullResultantModDegree':H9Sbar.degree(),'modCandidateDegree':H9Cbar.degree(),'actualBezoutMultipliedBack':True,'coefficientDegrees':[hs.degree(),ht.degree()],'coefficientSha256':hashlib.sha256((str(hs)+'|'+str(ht)).encode()).hexdigest(),'allKLeadingZeroFibersRetained':True,'claimExcluded':False})

class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1;return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0;self.bezout=0;self.divisions=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def trim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def addpoly(pp,qq,zero):
 out=[zero]*max(len(pp),len(qq))
 for j,v in enumerate(pp):out[j]=out[j]+v
 for j,v in enumerate(qq):out[j]=out[j]+v
 return trim(out)
def mulpoly(pp,qq,zero):
 if not pp or not qq:return []
 out=[zero]*(len(pp)+len(qq)-1)
 for i,v in enumerate(pp):
  for j,w in enumerate(qq):out[i+j]=out[i+j]+v*w
 return trim(out)
def dividep(pp,qq):
 pp=trim(pp);qq=trim(qq);assert qq
 field=qq[0].field;original=list(pp);inv=qq[-1].inv()
 out=[field.zero]*max(0,len(pp)-len(qq)+1)
 while pp and len(pp)>=len(qq):
  shift=len(pp)-len(qq);a=pp[-1]*inv;out[shift]=out[shift]+a
  for j,v in enumerate(qq):pp[shift+j]=pp[shift+j]-a*v
  pp=trim(pp)
 out=trim(out)
 assert original==addpoly(mulpoly(out,qq,field.zero),pp,field.zero)
 field.divisions+=1
 return out,pp
def gcdp(pp,qq):
 pp=trim(pp);qq=trim(qq)
 if not pp and not qq:return []
 field=(pp or qq)[0].field;zero=field.zero;one=field.one
 originalp=list(pp);originalq=list(qq)
 s0=[one];s1=[];t0=[];t1=[one]
 while qq:
  quotient,remainder=dividep(pp,qq);pp,qq=qq,remainder
  s0,s1=s1,addpoly(s0,[-v for v in mulpoly(quotient,s1,zero)],zero)
  t0,t1=t1,addpoly(t0,[-v for v in mulpoly(quotient,t1,zero)],zero)
 if pp:
  inv=pp[-1].inv();pp=[inv*v for v in pp];s0=[inv*v for v in s0];t0=[inv*v for v in t0]
 assert pp==addpoly(mulpoly(s0,originalp,zero),mulpoly(t0,originalq,zero),zero)
 field.bezout+=1
 return pp

tr=trim
def quo(pp,qq):
 out,remainder=dividep(pp,qq);assert not remainder;return out
def spec(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 out=[]
 for j0 in range(max(int(m[1]) for m in terms)+1):
  dd={int(m[0]):v for m,v in terms.items() if int(m[1])==j0}
  cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,v in dd.items():cs[i]=v
  out.append(field(fmpq_poly(cs)))
 return tr(out)
def fpower(self,n):
 assert n>=0
 out=self.field.one;v=self
 while n:
  if n&1:out=out*v
  v=v*v;n//=2
 return out
FE.__pow__=fpower
FE.__rsub__=lambda self,o:FE(self.field,o)+-self
FE.__truediv__=lambda self,o:self*FE(self.field,o).inv()
FE.__rtruediv__=lambda self,o:FE(self.field,o)*self.inv()


# Whole quadratic field: no selected complex embedding or numerical root.
hfield=Field(phi);hk=gcdp(spec(H9,hfield),spec(F41,hfield))
assert len(hk)==2 and hk[0]==0 and hk[1]==1
say({'stage':'complete_common_cofactor_quadratic_field_return','fieldPolynomial':'e^2+1','fieldDimension':2,'originalInputs':['H9','F41'],'gcdInK':'k','inversesMultipliedBack':hfield.inverses,'divisionsMultipliedBack':hfield.divisions,'bezoutMultipliedBack':hfield.bezout,'paidContradiction':'original k=Q/e is nonzero','bothEmbeddingsRetained':True,'wholeH9BoundaryExcluded':True,'claimExcluded':True})
# The 15 rows below act on the ACTUAL nonzero column (lambda,f,v,1).
# Neither four-generator freeness nor entrywise-zero multiplication is assumed.
def from_serialized(data):return bctx.from_dict({tuple(m):fmpq(a) for m,a in data})
parameter_rows=[[from_serialized(p) for p in rec['coefficients']] for rec in returned]
parameter_names=[rec['name'] for rec in returned]
assert len(parameter_rows)==15
chosen=(2,6,8)
assert [parameter_names[i] for i in chosen]==['cubic_overlap_1_2','cubic_overlap_3_4','cubic_overlap_4_5']
base_rows=[parameter_rows[i] for i in chosen];A3=[row[:3] for row in base_rows]
def det3(M):
 a,b,c=M;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
adj3=[]
for jj in range(3):
 row=[]
 for ii in range(3):
  sub=[[A3[r][c] for c in range(3) if c!=jj] for r in range(3) if r!=ii]
  row.append((-1)**(ii+jj)*(sub[0][0]*sub[1][1]-sub[0][1]*sub[1][0]))
 adj3.append(row)
delta=det3(A3);assert delta
Craw=[-sum((adj3[jj][ii]*base_rows[ii][3] for ii in range(3)),bz) for jj in range(3)]+[delta]
for jj in range(3):
 for q in range(4):
  assert sum((adj3[jj][ii]*base_rows[ii][q] for ii in range(3)),bz)==(delta if q==jj else -Craw[jj] if q==3 else bz)
be,bk=bctx.gens();bj=bk+2-2*be;bx=bk+4
bD3=4*be**3-3*be*be*bk-4*be*be+be*bk*bk+4*be*bk+4*be-bk-4
bB44=-be*be*bk**4+(-16*be**3-19*be*be+be)*bk**3+(16*be**4-40*be**3-8*be*be+36*be)*bk*bk+(16*be**4-48*be**3+64*be*be+80*be-16)*bk-64
parameter_units=[('e',be),('k',bk),('ell*k',bj),('T0',bx),('distinct_p_q',be*bk-1),('bc',bD3),('u',be+1),('closed_zero_base',be-1),('closed_half_weight',4*be-bk-4),('closed_consistency_line',4*be-bk),('closed_ehalf',2*be-1),('closed_equal_singleton_weights',be*bk+2*be-2),('closed_77e16',77*be-16),('closed_Omega',2*be*be-be*bk+2),('closed_H64',H64),('closed_H16',H16),('closed_H9',H9),('closed_original_v_leading_B44',bB44)]
common=bz
for pp in Craw:common=common.gcd(pp)
cofactor_paid=bo;cofactor_history=[]
for name,at in parameter_units:
 count=0
 while common:
  gg=common.gcd(at)
  if gg.total_degree()==0:break
  rr=common/gg;assert rr*gg==common;common=rr;cofactor_paid*=gg;count+=1
 if count:cofactor_history.append([name,count])
Cnorm=[pp/cofactor_paid for pp in Craw]
for aa,bb in zip(Craw,Cnorm):assert aa==bb*cofactor_paid
assert common.total_degree()==0
say({'stage':'original_three_row_cofactor_matrix_return','rowIndices':list(chosen),'rowNames':[parameter_names[i] for i in chosen],'actualCramerCoefficientIdentities':12,'paidCommonFactors':cofactor_history,'normalizedCofactorDegrees':[list(map(int,p.degrees())) for p in Cnorm],'normalizedCofactorTerms':[len(p.to_dict()) for p in Cnorm],'noUnpaidCommonFactorRemains':True,'deltaNotInverted':True,'allDeltaZeroFibersRetained':True,'claimExcluded':False})
# F41 is globally monic in e up to a nonzero rational constant.  This is
# stronger than an unproved generic leading coefficient: no parameter fiber
# is discarded by these exact e remainders.
import math
F_e_leading=bctx.from_dict({(0,int(m[1])):aa for m,aa in F41.to_dict().items() if int(m[0])==41})
assert F_e_leading==4503599627370496
Fmonic=F41/4503599627370496
assert Fmonic*4503599627370496==F41
say({'stage':'global_monic_e_parameter_curve','degreeE':41,'leadingCoefficientQQ':'2^52','parameterLeadingZeroBoundary':None,'noAdditionalLocalization':True,'claimExcluded':False})
def primitive_integer(p):
 denominator=1
 for aa in p.to_dict().values():denominator=math.lcm(denominator,int(aa.denominator))
 nums={m:int(aa.numerator)*(denominator//int(aa.denominator)) for m,aa in p.to_dict().items()}
 content=0
 for aa in nums.values():content=math.gcd(content,aa)
 assert content
 q=bctx.from_dict({m:fmpq(aa//content) for m,aa in nums.items()})
 if q.coefficient(0)<0:q=-q;content=-content
 assert p==fmpq(content,denominator)*q
 return q
generators=[];generator_names=[];seen=set()
def add_generator(name,p):
 assert p
 if name!='five_original_quadratics_F41':
  quotient,remainder=divmod(p,Fmonic)
  assert p==quotient*Fmonic+remainder
  assert not remainder or int(remainder.degrees()[0])<41
  say({'stage':'original_monic_e_remainder','name':name,'originalDegrees':list(map(int,p.degrees())),'remainderDegrees':list(map(int,remainder.degrees())) if remainder else None,'remainderTerms':len(remainder.to_dict()),'exactOriginalCombinationMultipliedBack':True,'newParameterDenominators':[],'claimExcluded':False})
  if not remainder:return
  p=remainder
 q=primitive_integer(p);dg=digest(q)
 if dg in seen:
  say({'stage':'duplicate_original_parameter_generator','name':name,'normalizedSha256':dg,'claimExcluded':False});return
 seen.add(dg);generators.append(q);generator_names.append(name)
 say({'stage':'two_parameter_original_generator','name':name,'degrees':list(map(int,q.degrees())),'terms':len(q.to_dict()),'sha256':dg,'primitiveIntegerNormalizationMultipliedBack':True,'claimExcluded':False})
add_generator('five_original_quadratics_F41',F41)
extraG=bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in proj.to_dict().items()})
assert all(int(m[2])==0 for m in proj.to_dict())
add_generator('full_original_P045_P035_projection',extraG)
nonzero_minors=0
for idx,row in enumerate(parameter_rows):
 Q=sum((aa*bb for aa,bb in zip(row,Cnorm)),bz)
 assert Q*cofactor_paid==sum((aa*bb for aa,bb in zip(row,Craw)),bz)
 # This is the original coefficient identity for the four-by-four determinant:
 # delta*row - sum(row[j]*adj3[j,i]*base_i) has only the constant column left.
 for col in range(4):
  rr=delta*row[col]-sum((row[jj]*adj3[jj][ii]*base_rows[ii][col] for jj in range(3) for ii in range(3)),bz)
  assert rr==(Q*cofactor_paid if col==3 else bz)
 if idx in chosen:assert not Q
 if not Q:continue
 rawQ=Q;paid=bo;history=[]
 for name,at in parameter_units:
  count=0
  while Q:
   gg=Q.gcd(at)
   if gg.total_degree()==0:break
   rr=Q/gg;assert rr*gg==Q;Q=rr;paid*=gg;count+=1
  if count:history.append([name,count])
 assert Q*paid==rawQ;nonzero_minors+=1
 say({'stage':'original_four_column_parameter_minor','returnedRow':parameter_names[idx],'degrees':list(map(int,Q.degrees())),'terms':len(Q.to_dict()),'paidRemovals':history,'originalFourCoefficientCombinationMultipliedBack':True,'noDeltaDivision':True,'sha256':digest(Q),'claimExcluded':False})
 add_generator(parameter_names[idx],Q)
assert nonzero_minors==11
# The higher degree original G input also constrains every rank-drop point of
# the selected three rows. No unproved Cramer delta or its numerator is saturated.
Stext='*'.join('('+str(p)+')' for name,p in parameter_units)
smoke_script='ring smokeRing=0,(s),dp;\nideal smoke=s,s-1;matrix smc;ideal smg=liftstd(smoke,smc,"std");matrix smp=matrix(smoke)*smc;\nif(size(smg)==1 && smg[1]==1 && nrows(smp)==1 && ncols(smp)==1 && smp[1,1]==1){print("ISP_LT0_TWO_PARAMETER_STD_SMOKE_VERIFIED");}else{print("ISP_LT0_TWO_PARAMETER_STD_SMOKE_FAILED");}quit;\n'
script='ring isp=0,(invUnit,k,e),dp;\noption(redSB);\npoly S='+Stext+';\n'
script+='ideal I='+',\n'.join(str(p) for p in generators)+',invUnit*S-1;\n'
script+='print("ISP_LT0_BEGIN_TWO_PARAMETER_ORIGINAL_QQ_LIFT");matrix cert;ideal GB=liftstd(I,cert,"slimgb");print("ISP_LT0_TWO_PARAMETER_ORIGINAL_LIFT_RETURNED");matrix product=matrix(I)*cert;\n'
script+='if(size(GB)==1 && GB[1]==1 && nrows(product)==1 && ncols(product)==1 && product[1,1]==1){print("ISP_LT0_TWO_PARAMETER_ORIGINAL_QQ_UNIT_VERIFIED");int q;for(q=1;q<=nrows(cert);q++){print(q);print(deg(cert[q,1]));print(size(cert[q,1]));}}else{print("ISP_LT0_TWO_PARAMETER_ORIGINAL_NO_UNIT_IDENTITY");print(size(GB));print(dim(GB));}quit;\n'
say({'stage':'two_parameter_original_QQ_input_built','geometricVariables':['e','k'],'auxiliaryVariables':['invUnit'],'variables':3,'nonSaturationGenerators':len(generators),'generatorNames':generator_names,'originalNonzeroFourColumnMinors':11,'wholeCommonH9BoundaryPaid':True,'fullOriginalGInputRetained':True,'deltaZeroFibersRetained':True,'exactMonicEQuotientDegree':41,'remainingGeneratorEDegreeBound':40,'originalParameterIdealEqualAfterMonicEAndConstantNormalization':True,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scriptBytes':len(script.encode()),'scriptSha256':hashlib.sha256(script.encode()).hexdigest(),'smokeScriptSha256':hashlib.sha256(smoke_script.encode()).hexdigest(),'saturationAtoms':[name for name,p in parameter_units],'independentSmokeAlgorithm':'std','fullAlgorithm':'slimgb','claimExcluded':False})
signal.alarm(0)
if '--build-only' in sys.argv:
 say({'stage':'build_only_complete','wholeH9BoundaryAndAllOriginalTracesVerified':True,'claimExcluded':False});raise SystemExit(0)
singular=shutil.which('Singular');assert singular is not None
version=subprocess.run([singular,'--version'],capture_output=True,text=True,timeout=15)
say({'stage':'singular_version','returncode':version.returncode,'version':(version.stdout+version.stderr).splitlines()[0]})
limit=int(os.environ.get('ISP_ALG_SECONDS','1200'))
def limits():resource.setrlimit(resource.RLIMIT_AS,(8*1024**3,8*1024**3))
def process_output(stdout,stderr):return ''.join(part.decode(errors='replace') if isinstance(part,bytes) else (part or '') for part in [stdout,stderr])
def diagnostics(out):return [line for line in out.splitlines() if line.lstrip().startswith('?')]
with tempfile.TemporaryDirectory(prefix='isp-Lt0-two-parameter-original-') as td:
 smoke_path=Path(td)/'smoke.sing';smoke_path.write_text(smoke_script)
 try:sm=subprocess.run([singular,'-q',str(smoke_path)],capture_output=True,text=True,timeout=45,preexec_fn=limits)
 except subprocess.TimeoutExpired as ex:
  out=process_output(ex.stdout,ex.stderr);say({'stage':'independent_std_smoke_timeout','timeoutSeconds':45,'stdoutSha256':hashlib.sha256(out.encode()).hexdigest(),'stdoutBytes':len(out.encode()),'text':out[:30000],'fullInputWritten':False,'fullAlgorithmStarted':False,'claimExcluded':False});raise
 out=sm.stdout+sm.stderr;err=diagnostics(out);passed=sm.returncode==0 and 'ISP_LT0_TWO_PARAMETER_STD_SMOKE_VERIFIED' in set(sm.stdout.splitlines()) and not err
 say({'stage':'independent_std_smoke_return','returncode':sm.returncode,'smokeVerified':passed,'singularDiagnosticLines':len(err),'stdoutSha256':hashlib.sha256(out.encode()).hexdigest(),'stdoutBytes':len(out.encode()),'text':out[:30000],'fullInputWritten':False,'fullAlgorithmStarted':False,'claimExcluded':False})
 assert passed,'separate std smoke failed: full slimgb input is not written or started'
 path=Path(td)/'input.sing';path.write_text(script)
 say({'stage':'full_slimgb_start_after_verified_independent_smoke','fullScriptSha256':hashlib.sha256(path.read_bytes()).hexdigest(),'smokeVerified':True,'timeoutSeconds':limit,'addressSpaceBytes':8*1024**3,'claimExcluded':False})
 try:
  rr=subprocess.run([singular,'-q',str(path)],capture_output=True,text=True,timeout=limit,preexec_fn=limits)
  out=rr.stdout+rr.stderr;err=diagnostics(out);passed=rr.returncode==0 and 'ISP_LT0_TWO_PARAMETER_ORIGINAL_QQ_UNIT_VERIFIED' in set(rr.stdout.splitlines()) and not err
  say({'stage':'actual_two_parameter_original_QQ_return','returncode':rr.returncode,'actualUnitVerified':passed,'singularDiagnosticLines':len(err),'stdoutSha256':hashlib.sha256(out.encode()).hexdigest(),'stdoutBytes':len(out.encode()),'text':out[:30000],'claimExcluded':passed})
  assert passed,'original two-parameter system has not produced a unit certificate'
 except subprocess.TimeoutExpired as ex:
  out=process_output(ex.stdout,ex.stderr);say({'stage':'actual_two_parameter_original_QQ_timeout','timeoutSeconds':limit,'stdoutSha256':hashlib.sha256(out.encode()).hexdigest(),'stdoutBytes':len(out.encode()),'text':out[:30000],'claimExcluded':False});raise
say({'stage':'complete','identity':'matrix(original two-parameter necessary ideal)*certificate=[1]','scope':'remaining original S0 Lt0 after every paid boundary','ordinaryISPClaim':False,'claimExcluded':True})
