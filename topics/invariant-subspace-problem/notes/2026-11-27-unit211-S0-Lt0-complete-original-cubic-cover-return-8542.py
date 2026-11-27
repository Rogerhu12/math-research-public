#!/usr/bin/env python3
"""R150 S0/Lt0: complete original general-branch return through a 615-degree cover.
Rebuilds original five quadrics, three original cubic replacements and all
cofactor identities, regenerates the full original P045/P035 projection, forms
the exact QQ F41/U38 resultant, and excludes every entire QQ factor with actual
full-degree univariate modular Bezout certificates at a verified leading unit.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(360)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
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

# The original first nineteen rows do not use or swap in the final Qa*1 row.
# Consequently the same first nineteen pivots transform each new last row.
assert all(swap!=19 for pivot,lower_col,swap in steps)
bx=bk+4
atoms=[('e',be),('k',bk),('j',bj),('x',bx),('D3',bD3),('ek-1',be*bk-1),('u',be+1),('e-1',be-1),('half',4*be-bk-4),('k4e',4*be-bk),('ehalf',2*be-1),('U',be*bk+2*be-2),('Omega',2*be*be-be*bk+2),('77e16',77*be-16)]
expected={
 'U_moment':([38,31],737,'b76f8e51881fd426200f19bc07cd3d0c0c24873016435d9782b46e56be8664a5'),
 'NB_even':([42,34],908,'b200b0d88c5c45de4d077f68b213a271950fe982b9f4a860c74824409e79ddab'),
 'PB_even':([47,37],1076,'e5fe302767735755c866d2851c1b56d83babcbaa6b23c636c161ed29c1fbe4fc')}
new_curves=[]
for label,p in [('U_moment',Mmoment),('NB_even',polys[4]),('PB_even',polys[6])]:
 assert all(int(m[5])==int(m[6])==0 for m in p.to_dict())
 assert max(sum(map(int,m[2:5])) for m in p.to_dict())<=3
 row=[bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in p.to_dict().items() if tuple(map(int,m[2:5]))==mon}) for mon in mons]
 recon=zz
 for mon,coef in zip(mons,row):
  for (ie,ik),cc in coef.to_dict().items():recon+=cc*e**int(ie)*k**int(ik)*la**mon[0]*fp**mon[1]*v**mon[2]
 assert recon==p
 Brow=[list(rr) for rr in M];Brow[-1]=row
 transformed=list(row);prev=bo;newsteps=[]
 for z,(pivot,lower_col,swap) in enumerate(steps):
  assert pivot==A[z][z]
  low=transformed[z]
  newcol=list(lower_col);newcol[-1]=low
  newsteps.append((pivot,newcol,swap))
  for q in range(z+1,20):
   numerator=transformed[q]*pivot-low*A[z][q]
   red=numerator/prev;assert red*prev==numerator;transformed[q]=red
  transformed[z]=bz;prev=pivot
 Dnew=transformed[-1];assert Dnew
 newcofactor=[bz]*20;newcofactor[-1]=newsteps[-1][0]
 for z in range(18,-1,-1):
  pivot,lower_col,swap=newsteps[z]
  numerator=-sum((newcofactor[i]*lower_col[i-z-1] for i in range(z+1,20)),bz)
  val=numerator/pivot;assert val*pivot==numerator;newcofactor[z]=val
  if swap!=z:newcofactor[z],newcofactor[swap]=newcofactor[swap],newcofactor[z]
 for q in range(20):
  actual=sum((newcofactor[i]*Brow[i][q] for i in range(20)),bz)
  assert actual==(Dnew if q==19 else bz)
 say({'stage':'entire_original_cube_replacement_cofactor_return','name':label,'replacedRowIndex':19,'replacedOldRow':'Qa*1','newOriginalRowMultipliedBack':True,'matrixSize':[20,20],'actualCofactorIdentities':20,'identity':'newcofactor * original_replaced_M = (0,...,0,Dnew)','cofactorSha256':hashlib.sha256('|'.join(digest(pp) for pp in newcofactor).encode()).hexdigest(),'noPointwisePivotDivision':True,'allLeadingZeroFibersRetained':True,'claimExcluded':False})
 stripped=Dnew;paid=bo;hist=[]
 for name,at in atoms:
  ct=0
  while True:
   gg=stripped.gcd(at)
   if gg.total_degree()==0:break
   red=stripped/gg;assert red*gg==stripped;stripped=red;paid*=gg;ct+=1
  if ct:hist.append([name,ct])
 assert stripped*paid==Dnew
 scalar,factors=stripped.factor();assert len(factors)==1 and int(factors[0][1])==1
 curve=factors[0][0];assert scalar*curve==stripped and scalar*paid*curve==Dnew
 degrees,terms,sha=expected[label]
 assert list(map(int,curve.degrees()))==degrees and len(curve.to_dict())==terms and digest(curve)==sha
 new_curves.append((label,curve))
 say({'stage':'complete_new_original_cube_curve_factorization','name':label,'fullDegrees':list(map(int,Dnew.degrees())),'fullTerms':len(Dnew.to_dict()),'fullSha256':digest(Dnew),'paidDivisions':hist,'nonzeroScalar':str(scalar),'remainingDegrees':degrees,'remainingTerms':terms,'remainingSha256':sha,'fullFactorizationMultipliedBack':True,'otherUnpaidFactors':[],'newNecessaryParameterEquation':label+'(e,k)=0','allLeadingZeroFibersRetained':True,'claimExcluded':False})

# Original G132 projection, with all same-point row traces regenerated.
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

assert digest(proj)=='eda457be0935386401451ddf8b2d09410dc6ea5a6d263c9a3e415de36eec1f96'
G132=bctx.from_dict({(int(m[0]),int(m[1])):aa for m,aa in proj.to_dict().items()})
assert all(int(m[2])==0 for m in proj.to_dict())
from flint import fmpq_poly,nmod_poly,nmod_mpoly_ctx
curve_by_name=dict(new_curves);U38=curve_by_name['U_moment'];N42=curve_by_name['NB_even']
# All finite k-leading degeneracies remain in the COMPLETE QQ resultant.
say({'stage':'begin_complete_original_QQ_parameter_cover','inputs':['F41_33','U38_31'],'fullKDegrees':[33,31],'allLeadingZeroFibersRetained':True,'claimExcluded':False})
QQR=F41.resultant(U38,'k');assert QQR
cs=[fmpq(0)]*(int(QQR.degrees()[0])+1)
for mm,aa in QQR.to_dict().items():assert int(mm[1])==0;cs[int(mm[0])]=aa
R615=fmpq_poly(cs);C615=R615;ue=fmpq_poly([0,1]);paid_poly=fmpq_poly([1]);hist=[]
paid_e=[('original_e',ue),('closed_zero_base_weight',ue-1),('original_u',ue+1),('closed_entire_ehalf',ue-fmpq(1,2)),('closed_entire_77e16',ue-fmpq(16,77))]
for name,at in paid_e:
 n=0
 while True:
  qq,rr=divmod(C615,at)
  if rr:break
  assert qq*at==C615;C615=qq;paid_poly*=at;n+=1
 if n:hist.append([name,n])
assert C615*paid_poly==R615
assert R615.degree()==1502 and C615.degree()==615
assert hist==[['original_e',98],['closed_zero_base_weight',44],['original_u',555],['closed_entire_ehalf',190]]
assert hashlib.sha256(str(R615).encode()).hexdigest()=='d379086ccd80f7a1e41d390b5745ea0249ee0df7af8dce28e8107e417fe9bd6b'
assert hashlib.sha256(str(C615).encode()).hexdigest()=='4a3942a867bc1745d8e3094bce8fe5acf696b6eb94338f80eca26d7ca66adef7'
say({'stage':'complete_original_QQ_parameter_cover','fullDegree':1502,'paidDivisions':hist,'remainingQQDegree':615,'fullSha256':hashlib.sha256(str(R615).encode()).hexdigest(),'remainingSha256':hashlib.sha256(str(C615).encode()).hexdigest(),'allQQDivisionsMultipliedBack':True,'allOriginalKLeadingZeroFibersRetained':True,'claimExcluded':False})
scalar,factors=C615.factor();ff=fmpq_poly([scalar]);ordered=sorted(factors,key=lambda pp:pp[0].degree())
assert [(p.degree(),int(n)) for p,n in ordered]==[(2,1),(296,1),(317,1)]
for pp,n in factors:ff*=pp**n
assert ff==C615
C2,C296,C317=[pp for pp,n in ordered];assert C2==fmpq_poly([1,0,1])
expected_factors={2:'ba96a490d05076d882fafacd51dbf0cfdf8468fe9886273e2ff353bd0331658d',296:'199b93f663d60c8990cf1cbc4477bf397b4716f38c01001f7da4cca4416cf91f',317:'f08a5fba7e9204886fb70147d627287673020a4683fa016a13c4d1099bb30dfc'}
for pp,n in ordered:assert hashlib.sha256(str(pp).encode()).hexdigest()==expected_factors[pp.degree()]
say({'stage':'entire_QQ_parameter_cover_factorization','factorDegrees':[2,296,317],'multiplicities':[1,1,1],'factorSha256':[expected_factors[p.degree()] for p,n in ordered],'allFactorsAndQQScalarMultipliedBack':True,'noIrreducibilityAssumptionNeededForNextBezout':True,'claimExcluded':False})
prime=1009;modctx=nmod_mpoly_ctx.get(('e','k'),ordering='lex',modulus=prime)
def red_coeff(aa):
 denominator=int(aa.denominator)%prime;assert denominator
 return int(aa.numerator)%prime*pow(denominator,-1,prime)%prime
def mod_input(pp,expected_k_degree):
 out=modctx.from_dict({tuple(map(int,m)):red_coeff(aa) for m,aa in pp.to_dict().items()})
 assert int(pp.degrees()[1])==int(out.degrees()[1])==expected_k_degree
 return out
Fm=mod_input(F41,33);Nm=mod_input(N42,34);Gm=mod_input(G132,109)
def full_resultant_mod(pp,name,second_k_degree):
 out=Fm.resultant(pp,'k');assert out
 cc=[0]*(int(out.degrees()[0])+1)
 for m,aa in out.to_dict().items():assert int(m[1])==0;cc[int(m[0])]=int(aa)
 out=nmod_poly(cc,prime)
 say({'stage':'full_original_univariate_Sylvester_modular_return','name':name,'prime':prime,'originalFullKDegrees':[33,second_k_degree],'modularFullKDegrees':[33,int(pp.degrees()[1])],'fullResultantModDegree':out.degree(),'resultantModSha256':hashlib.sha256(str(out).encode()).hexdigest(),'actualQQResultantDefinedByTheseFullInputs':True,'claimExcluded':False})
 return out
SN=full_resultant_mod(Nm,'Res_k(F41,N42)',34)
SG=full_resultant_mod(Gm,'Res_k(F41,G132)',109)
for candidate,support,name in [(C2,SN,'quadratic_with_original_N_even'),(C296,SG,'degree296_with_original_G132'),(C317,SN,'degree317_with_original_N_even')]:
 lc=candidate.leading_coefficient();assert red_coeff(lc)
 monic=candidate/lc;assert monic*lc==candidate
 for aa in monic:red_coeff(aa)
 cb=nmod_poly([red_coeff(aa) for aa in candidate],prime)
 assert cb.degree()==candidate.degree()
 unit,ss,tt=cb.xgcd(support)
 assert unit==ss*cb+tt*support and unit==1
 say({'stage':'entire_original_QQ_factor_modular_Bezout','case':name,'prime':prime,'actualQQCandidateDegree':candidate.degree(),'modularCandidateDegree':cb.degree(),'QQMonicNormalizationIsPrimeIntegral':True,'actualQQLeadingCoefficientIsPrimeUnit':True,'fullResultantModDegree':support.degree(),'coefficientDegrees':[ss.degree(),tt.degree()],'coefficientSha256':hashlib.sha256((str(ss)+'|'+str(tt)).encode()).hexdigest(),'candidateSha256':hashlib.sha256(str(candidate).encode()).hexdigest(),'actualBezoutMultipliedBack':True,'GaussLemmaAppliesToActualQQUnivariateCover':True,'arbitraryMultivariateModularUnitUsed':False,'allComplexEmbeddingsRetained':True,'wholeCandidateExcluded':True,'claimExcluded':True})
signal.alarm(0)
say({'stage':'complete','scope':'every remaining original S0 Lt0 point after the previously paid physical and boundary factors','completeQQCoverDegree':615,'entireCandidateDegreesExcluded':[2,296,317],'allOriginalSamePointInputTracesVerified':True,'allLeadingZeroFibersRetained':True,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'wholeRemainingS0Lt0Excluded':True,'ordinaryISPClaim':False,'claimExcluded':True})
