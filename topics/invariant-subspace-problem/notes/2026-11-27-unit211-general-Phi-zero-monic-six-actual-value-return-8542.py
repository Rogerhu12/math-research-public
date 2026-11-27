#!/usr/bin/env python3
"""R150 Phi=0: same-source original values with immediate monic T^6 reduction.
This is a new actual-value input, not a replay of the 5842-term old cofactor.
No finite-algebra norm is inverted.  Original moments, P1 and N(V) recover
zeta,f,t and then the original full Gram matrix on paid physical units.
All operations use exact rational coefficients; 120 seconds / 1 GiB.
"""
import os,sys,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
helper_path=Path(os.environ.get("ISP_MONIC_SIX_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-monic-six-explicit-geometric-localization-helper-8542.py"))))
helper_text=helper_path.read_text()
assert hashlib.sha256(helper_text.encode()).hexdigest()=="5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6"
exec(compile(helper_text,str(helper_path),"exec"),globals())
atoms_path=Path(os.environ.get("ISP_MONIC_SIX_ATOMS_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-monic-six-separate-geometric-exponents-helper-8542.py"))))
atoms_text=atoms_path.read_text()
assert hashlib.sha256(atoms_text.encode()).hexdigest()=="8fef06d13684d0a6ab9a463c38287cabc2793c9f92cd43dd43544a7c8f7d3408"
exec(compile(atoms_text,str(atoms_path),"exec"),globals())
ctx=fmpq_mpoly_ctx.get(('u','Q','lam','T'),'lex')
up,Qp,Lp,Tp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
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
 def __pow__(self,n):
  return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o)
  if self.n==o.n and self.d==o.d:return True
  return self.n*o.d==o.n*self.d
u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
M=ell*V2-u*u;bc=M/(4*delta)
assert Phi==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
Dr=ell*A2-Tr*Tr
snr=ell*B3-A2*Tr;znr=Tr*B3-A2*A2
Kr=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
Zr=u*snr-2*Tr*Dr;Snr=snr+(3-2*lam)*Dr
F6r=M*Kr*Kr-4*m*m*Dr**3
G=lam*P02-(1-u)*T0;wr=lam-1-Tr
Pcr=Q*P02*(ell+Tr)-G*T0
NF4r=4*m*((3-4*lam)*Q*Dr*Dr-J*znr*Dr)+2*Snr*(-2*u*Q*Kr+J*Zr)
NC4r=(4*m*G*znr*Dr-2*G*Snr*Zr-Q*T0*Snr*Kr
      +4*m*Q*wr*u*(3-2*lam)*Dr*Dr
      +2*m*Q*wr*u*snr*Dr-2*Q*wr*(u-ell*Q)*Kr*Dr)
# These are exact polynomial identities before taking the moment quotient.
assert Kr+2*Tr*Dr==ell*snr
assert ell*Zr==2*m*Tr*Dr+u*Kr
assert m*snr-Zr+Kr==0
raw_values=dict(D=Dr,sn=snr,zn=znr,K=Kr,Z=Zr,Sn=Snr,Pc=Pcr,
                NF4=NF4r,NC4=NC4r)
def profile(p):
 return dict(degrees=list(map(int,p.degrees())),terms=len(p.to_dict()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
say("original_Phi0_exact_weight_and_compact_numerator_input",
    variables=["u","Q","lambda","T"],PhiExactlyZero=True,
    originalMomentRelation=profile(F6r.n),
    originalNumerators={k:profile(v.n) for k,v in raw_values.items()},
    originalUnits=["u","u-1","Q","1-Q","ell","ell-u","M","P02",
                   "T0","J-Q","u+Q-1","lambda","D","S","zeta"],
    ordinaryISPClaim=False)
unit_atoms=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
            ("ell",ell.n),("ell-u",m.n),("M",M.n),("P02",P02.n),
            ("T0",T0.n),("J-Q",(J-Q).n),("u+Q-1",(u+Q-1).n),
            ("lambda",lam.n)]
paid_cache=set();coefficient_cache=set()
def strip_paid(pp):
 if not pp:raise AssertionError("zero cannot be a paid weight unit")
 key=str(pp)
 if key in paid_cache:return
 p=pp
 for name,atom in unit_atoms:
  while p:
   g=p.gcd(atom)
   if g.total_degree()==0:break
   q=p/g;assert q*g==p;p=q
 assert p.total_degree()==0,("unpaid weight factor",str(p),str(pp))
 paid_cache.add(key)
def noT(pp):return all(int(e[3])==0 for e in pp.to_dict())
def coefficient_audit(rr):
 rr=R(rr);assert noT(rr.n) and noT(rr.d)
 key=str(rr.d)
 if key not in coefficient_cache:
  strip_paid(rr.d);coefficient_cache.add(key)
def parameter_unit_audit(name,rr):
 assert name.startswith("paid_weight:") or name=="F6_leading"
 rr=R(rr);assert noT(rr.n) and noT(rr.d)
 strip_paid(rr.n);strip_paid(rr.d)
cooperate_parameter_ring(R)
alg=make_six_from_mpoly(R,ctx,F6r.n,3,coefficient_audit,
                       parameter_unit_audit,"F6_leading")
K6=alg.K6;T=alg.T
# The true monic leading coefficient is the old F6 leading times its
# already-paid scalar denominator; verify it in the original coefficient ring.
assert alg.original_leading_coefficient==4*ell*ell*delta*R(F6r.d)
def kin(rr):
 rr=R(rr);assert noT(rr.d)
 inv=alg.inverse_parameter("paid_weight:input_denominator",R(rr.d))
 return alg.from_mpoly(rr.n)*inv
kv={k:kin(v) for k,v in raw_values.items()}
D,sn,zn,K,Z,Sn,Pc,NF4,NC4=(kv[k] for k in
                            ("D","sn","zn","K","Z","Sn","Pc","NF4","NC4"))
assert D==K6(ell*A2)-T*T
assert alg.from_mpoly(F6r.n)==0
P=Sn*Z
loc=make_atom_localization(alg,[
 ("D",D,"Original physical D=bc(h-k)^2 is nonzero"),
 ("P",P,"Original general LS has S*zeta nonzero; P=2*(u-ell)*D^2*S*zeta")
])
F=loc.Fraction
def pinv(name,rr):return loc.inverse_parameter("paid_weight:"+name,rr)
invD=loc.inverse_atom("D");invP=loc.inverse_atom("P")
fnum=-Pc*alg.inverse_parameter("paid_weight:Pf",Pf)
f=F(fnum)
tnum=-(NF4*fnum+NC4)*alg.inverse_parameter("paid_weight:2bcQ",2*bc*Q)
t=F(tnum)*invP
zeta=F(Z)*invD*pinv("2m",2*m)
v0=F(sn)*invD/2
v1=-F(K)*invD*pinv("2m",2*m)
S=F(Sn)*invD
zbar=F(zn)*invD
ww=F(K6(lam-1)-T)
assert F(Pf)*f+F(Pc)==0
assert F(NF4)*f+2*F(P)*F(bc*Q)*t+F(NC4)==0
assert F(ell)*zeta==F(T)+F(u)*(zeta-v0)
assert v1==v0-zeta
HA=ell*M*zeta*zeta-2*F(T)*M*zeta+F(V2)*F(T*T)-u*u*A2
HB=u*u*(F(B3)-2*v0*A2+(v0*v0-F(delta)*v1*v1)*F(T))
assert HA==0 and HB==0
assert v0*v0-F(delta)*v1*v1==zbar
say("six_dimensional_original_moment_and_same_source_line_return",
    allMomentIdentities=True,originalP1=True,originalNVLine=True,
    geometricFactors=list(loc.factors),noNormInverse=True,
    statistics=dict(alg.statistics))

class E:
 _isp_quotient_level=3
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=F(a);self.b=F(b)
 def __bool__(self):return not(self.a==0 and self.b==0)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+F(delta)*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert isinstance(o,int) and o!=0
  return E(self.a/o,self.b/o)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  while n:
   if n&1:out=out*self
   n>>=1
   if n:self=self*self
  return out
 def __eq__(self,o):
  o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(ell/2,m/(2*delta));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj()
ivdiff=E(0,-1/(2*delta))
ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
W1=E(T0/2)+2*E(u)*E(f)
W2=E(u*T0+lam*P02)+E(V2+2*u*u)*E(f)-E(bc*Q)*E(t)
X=ivbp*(q*W1-W2);Y=ivcq*(W2-p*W1)
rg=X-a*p-c*E(t);sg=Y-a*q-b*E(t)
AA=2*E(f)-2*b*X-2*c*Y+2*E(bc)*E(t)
rows=[[E(),E(),p,q],[E(),AA,rg,sg],
      [p,rg,E(),E(t)],[q,sg,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);rawF2=tau(d)
assert rawF2==E(2*f)
F2=E(2*f)
Kd=DK(d)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert mean(0)==0
E1,EB,EC=mean(1),mean(2),mean(3)
assert E1.b==0 and EB.conj()==EC
hh=E(1+v0,v1);kk=hh.conj();VV=[E(1),E(ww),hh,kk]
assert b*(hh-1)+c*(kk-1)==E(T)
assert tau(VV)==E(lam)
assert q*(hh-1)-p*(kk-1)==E(0,-2*zeta)
assert tau(vm(VV,VV))==E(2*lam*lam)
assert tau(vm(VV,vm(VV,VV)))==E(4*lam**3)
assert E(D)==E(bc)*(hh-kk)**2

def N4(v,known_tau=None):
 tv=tau(v)
 if known_tau is not None:
  assert tv==known_tau;tv=known_tau
 return (2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))
         -4*tv*tau(vm(d,v))+2*F2*tv**2+tau(vm(v,DK(v))))
def P2(v):
 vc=va(v,vs(-tau(v),one))
 return tau(vm(vm(vc,vc),vc))
v,zz=rows[0],rows[1]
vc=va(v,vs(-tau(v),one));zc=va(zz,vs(-tau(zz),one))
Pj=3*tau(vm(vm(vc,vc),zc))
# Exact polarization of the original N4 quadratic form in its vector argument.
Nv=(4*tau(vm(d,vm(v,zz)))-2*F2*tau(vm(v,zz))
    -4*(tau(v)*tau(vm(d,zz))+tau(zz)*tau(vm(d,v)))
    +4*F2*tau(v)*tau(zz)+tau(vm(v,DK(zz)))+tau(vm(zz,DK(v))))
NH=Nv-(4*E(lam)/3)*Pj
assert NH.b==0
assert Pj==3*E(ww*P02)
assert N4(rows[0])==E(2*lam*P02)
assert P2(rows[0])==E(P02)

def export_polynomial(name,frac):
 frac=F(frac)
 coeffs=frac.numerator.coefficients
 den=oneP
 for rr in coeffs:
  coefficient_audit(rr)
  g=den.gcd(rr.d);den=(den/g)*rr.d
 out=zeroP
 for j,rr in enumerate(coeffs):
  quot=den/rr.d;assert quot*rr.d==den
  out+=rr.n*quot*Tp**j
 # Denominator is nonzero on the original weight domain.
 strip_paid(den)
 # Strip only paid weight factors, never an unproved T-leading coefficient.
 reduced=out;removed=[]
 if reduced:
  for uname,atom in unit_atoms:
   power=0
   while True:
    gg=reduced.gcd(atom)
    if gg.total_degree()==0:break
    qq=reduced/gg;assert qq*gg==reduced;reduced=qq;power+=1
   if power:removed.append([uname,power])
  leading=reduced.coefficient(0)
  if leading:reduced=reduced/leading
 say("same_point_original_necessary_polynomial",name=name,
     poleOrders=list(frac.pole_orders),geometricAtoms=["D","Sn*Z"],
     before=profile(out),after=profile(reduced),paidRemoved=removed,
     denominator=profile(den),TLeadingNotInverted=True)
 return reduced
polys={}
for name,ff in [("E1",E1.a),("EB_even",EB.a),("EB_odd",EB.b),("N1",NH.a)]:
 polys[name]=export_polynomial(name,ff)
say("original_means_and_N1_complete",sameOriginalGram=True,
    statistics=dict(alg.statistics),claimExcluded=False)

# The published full original atlas identity is
# Q*N(V)/2 = NF*f + NT*t + NC - Q*f*HA/u^2.
# NF4=4*m*D^2*NF, NC4=4*m*D^2*NC,
# and 4*m*D^2*NT=2*bc*Q*Sn*Z.
# The exact HA=0 and the full second line were verified above in this
# same quotient and source.  Thus this proves original N(V)=0 without
# replaying the already-paid full generic atlas expansion.
say("full_original_NV_by_paid_atlas_and_actual_same_source_lines",
    publishedAtlasSource="2026-11-27-unit211-generic-LS-Delta-zero-global-monic-value-quadratic-original-return-8542.py",
    exactOriginalIdentity="Q*NV/2=NF*f+NT*t+NC-Q*f*HA/u^2",
    currentHAMomentZero=True,currentOriginalSecondLineZero=True,
    sameOriginalGram=True,fullOriginalNVZero=True,
    extraGenericAtlasExpansion=False,statistics=dict(alg.statistics))

NB=N4(rows[2])-2*E(lam*P02)*hh**2
PB=P2(rows[2])-E(P02)*hh**3
NC=N4(rows[3])-2*E(lam*P02)*kk**2
PC=P2(rows[3])-E(P02)*kk**3
assert NB.conj()==NC and PB.conj()==PC
for name,ff in [("NB_even",NB.a),("NB_odd",NB.b),
                ("PB_even",PB.a),("PB_odd",PB.b)]:
 polys[name]=export_polynomial(name,ff)
say("complete_Phi0_full_original_value_input",
    sameSourceRecovery=["original moment line","original P1","original N(V)",
                        "original E0 and N0"],
    allOriginalMeanN1AndIndividualNP=True,
    originalRows=list(polys),statistics=dict(alg.statistics),
    claimExcluded=False,ordinaryISPClaim=False,
    newUnpaidInversions=[],algebraicNormInversions=0)
