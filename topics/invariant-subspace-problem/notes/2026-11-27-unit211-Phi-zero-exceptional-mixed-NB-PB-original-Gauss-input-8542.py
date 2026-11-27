#!/usr/bin/env python3
"""NEW exceptional Phi=0 source: mixed individual NB/PB original rows.
The old PB six-row matrix and old NB six-row matrix are not replayed.
Use E1,EBe,EBo,N1,NBe,PBe and actual T multiples, target (D Sn Z)^6.
The already-paid monic original R has exact QQ lambda degree 2033
and 1009-unit leading coefficient (cf39 infinity certificate).
Only a NEW fixed original resultant and its full modular Bezout with
that saved R are computed.  Every new core is saved recoverably.
120 seconds / 1 GiB.  Unknown zero fibers are retained.
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
ctx=fmpq_mpoly_ctx.get(('rho','lam','T'),'lex')
dp,Lp,Tp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
gap,lam,Tr=map(R,(dp,Lp,Tp))
u=(3+gap)/2;Q=1-gap*gap
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
M=ell*V2-u*u;bc=M/(4*delta)
assert Phi==0
assert ell==R(3)/2
assert u==ell+gap/2 and ell-1-2*(R(1)/2)**2==0
assert T0==(gap-3)*(gap+1) and J-Q==-(gap+1)**2
assert M==2*gap*gap and bc==R(1)/2
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
Dr=ell*A2-Tr*Tr
snr=ell*B3-A2*Tr;znr=Tr*B3-A2*A2
Kr=ell*ell*B3-3*ell*Tr*A2+2*Tr**3
Zr=u*snr-2*Tr*Dr;Snr=snr+(3-2*lam)*Dr
F6r=M*Kr*Kr-4*m*m*Dr**3
assert F6r==gap*gap*(2*Kr*Kr-Dr**3)
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
             totalDegree=int(p.total_degree()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
say("original_Phi0_exact_weight_and_compact_numerator_input",
    variables=["rho","lambda","T"],PhiExactlyZero=True,
    actualBranch="b=1,c=1/2,ell=3/2,u=(3+rho)/2,Q=1-rho^2",
    exactRhoQuadraticHeadAndLinearCoefficientZero=True,
    otherExceptionalOrderedWeightCoveredByOriginalBCExchange=True,
    momentRelationAfterPaidRhoSquaredRemoval="2*K^2-D^3",
    noClaimOnMainHeadZeroBranch=True,
    originalMomentRelation=profile(F6r.n),
    originalNumerators={k:profile(v.n) for k,v in raw_values.items()},
    originalUnits=["u","u-1","Q","1-Q","ell","ell-u","M","P02",
                   "T0","J-Q","u+Q-1","lambda","D","S","zeta"],
    ordinaryISPClaim=False)
unit_atoms=[("rho",gap.n),("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
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
def noT(pp):return all(int(e[2])==0 for e in pp.to_dict())
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
alg=make_six_from_mpoly(R,ctx,F6r.n,2,coefficient_audit,
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
say("complete_new_Phi0_rho_head_zero_exceptional_main_branch_original_values",
    sameSourceRecovery=["original moment line","original P1","original N(V)",
                        "original E0 and N0"],
    allOriginalMeanN1AndIndividualNP=True,
    originalRows=list(polys),statistics=dict(alg.statistics),
    claimExcluded=False,ordinaryISPClaim=False,
    newUnpaidInversions=[],algebraicNormInversions=0)


# New input: the actual mean/N1 ideal under all six T powers, target unit power six.
# Sampling below chooses rows only.  The mathematical conclusion is the
# subsequent complete QQ determinant / cofactor identity in the original
# six-column quotient; no sampled rank is itself used as a proof.
def clear_six_vector(kk):
 cc=list(K6(kk).coefficients);dd=oneP
 for rr in cc:
  coefficient_audit(rr)
  gg=dd.gcd(rr.d);dd=(dd/gg)*rr.d
 strip_paid(dd)
 vals=[]
 for rr in cc:
  qq=dd/rr.d;assert qq*rr.d==dd;vals.append(rr.n*qq)
 assert all(noT(vv) for vv in vals)
 assert all(R(vv)==rr*R(dd) for vv,rr in zip(vals,cc))
 return vals,dd
original_names=["E1","EB_even","EB_odd","N1","NB_even","PB_even"]
source_elements={name:alg.from_mpoly(polys[name]) for name in original_names}
source_rows=[];source_tags=[]
powers=[K6(1)]
for jj in range(1,6):powers.append(powers[-1]*T)
for jj in range(6):
 for name in original_names:
  row,dd=clear_six_vector(source_elements[name]*powers[jj])
  source_rows.append(row)
  source_tags.append(dict(original=name,Tpower=jj,paidScalarDenominator=profile(dd)))
say("new_exceptional_original_NB_PB_mixed_complement_complete_original_six_column_candidates",
    originalCount=6,candidateCount=len(source_rows),columns=6,
    allSameTAndOriginalRows=True,
    originalRowMultiplicationAndPaidClearingReturned=True,
    candidateShape=[len(source_rows),6],claimExcluded=False)
prime=1009
def scalar_mod(x):
 x=fmpq(x);den=int(x.denominator)%prime;assert den
 return int(x.numerator)%prime*pow(den,-1,prime)%prime
def eval_mod(pp,dv,lv):
 ans=0
 for ex,cc in pp.to_dict().items():
  assert int(ex[2])==0
  ans=(ans+scalar_mod(cc)*pow(dv,int(ex[0]),prime)*pow(lv,int(ex[1]),prime))%prime
 return ans
selected=None;selection=None;maximum_rank=0
for trialprime in (1009,1013,1019):
 prime=trialprime
 if any(int(fmpq(cc).denominator)%prime==0
        for row in source_rows for pp in row for cc in pp.to_dict().values()):
  continue
 for dv,lv in [(2,3),(3,2),(5,7),(7,11)]:
  basis=[];choice=[]
  for ix,row in enumerate(source_rows):
   vv=[eval_mod(pp,dv,lv) for pp in row]
   for piv,old in basis:
    coef=vv[piv]
    if coef:vv=[(a-coef*b)%prime for a,b in zip(vv,old)]
   lead=next((j for j,a in enumerate(vv) if a),None)
   if lead is None:continue
   inv=pow(vv[lead],-1,prime);vv=[a*inv%prime for a in vv]
   basis.append((lead,vv));choice.append(ix)
   if len(choice)==6:break
  maximum_rank=max(maximum_rank,len(choice))
  if len(choice)==6:
   selected=choice;selection=[prime,dv,lv];break
 if selected is not None:break
if selected is None:
 say("new_exceptional_original_NB_PB_mixed_complement_no_six_rows_selected",
     selectionOnly=True,maximumObservedModRank=maximum_rank,
     noQQRankOrExclusionClaim=True)
 sys.exit(0)
mat=[source_rows[ix] for ix in selected]
target_element=(D*P)**6
target,target_den=clear_six_vector(target_element)
assert target_element==(D*Sn*Z)**6
say("new_exceptional_original_NB_PB_mixed_complement_exact_Cramer_start",
    selectedIndices=selected,selectedOriginalTags=[source_tags[ix] for ix in selected],
    selectionOnlyModularPoint=selection,
    target="paidScalarDenominator * (D * Sn * Z)^6",
    targetScalarDenominator=profile(target_den),
    actualTargetIsPaidUnit=True,
    sixBySixQQMatrixOnly=True,noLargeResultant=True)
bareiss_divisions=0
def bareiss_det(mm,label):
 global bareiss_divisions
 a=[row[:] for row in mm];nn=len(a);previous=oneP;sgn=1
 for k in range(nn-1):
  pivot=next((i for i in range(k,nn) if a[i][k]),None)
  if pivot is None:return zeroP
  if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sgn=-sgn
  pp=a[k][k]
  for i in range(k+1,nn):
   for j in range(k+1,nn):
    numerator=pp*a[i][j]-a[i][k]*a[k][j]
    qq=numerator/previous
    assert qq*previous==numerator
    a[i][j]=qq;bareiss_divisions+=1
   a[i][k]=zeroP
  previous=pp
  say("new_exceptional_original_NB_PB_mixed_complement_QQ_Bareiss_stage",matrix=label,pivotIndex=k,
      maximumTerms=max((len(a[i][j].to_dict())
                        for i in range(k+1,nn) for j in range(k+1,nn)),default=0),
      exactDivisionProducts=bareiss_divisions,claimExcluded=False)
 return sgn*a[-1][-1]
det=bareiss_det(mat,"original_selected_rows");assert det
cofactors=[]
for i in range(6):
 replaced=[row[:] for row in mat];replaced[i]=target
 cc=bareiss_det(replaced,"target_replaces_row_"+str(i))
 cofactors.append(cc)
 say("new_exceptional_original_NB_PB_mixed_complement_one_actual_target_cofactor",row=i,cofactor=profile(cc),
     exactDivisionProducts=bareiss_divisions,claimExcluded=False)
for j in range(6):
 assert sum((cc*row[j] for cc,row in zip(cofactors,mat)),zeroP)==det*target[j]
common=det
for cc in cofactors:common=common.gcd(cc)
delta_core=det/common;assert delta_core*common==det
tags=[cc/common for cc in cofactors]
assert all(tt*common==cc for tt,cc in zip(tags,cofactors))
for j in range(6):
 assert sum((cc*row[j] for cc,row in zip(tags,mat)),zeroP)==delta_core*target[j]
removed=[]
for uname,atom in unit_atoms:
 count=0
 while delta_core:
  gg=delta_core.gcd(atom)
  if gg.total_degree()==0:break
  quot=delta_core/gg;assert quot*gg==delta_core;delta_core=quot;count+=1
 if count:removed.append([uname,count])
if delta_core:
 scalar=delta_core.coefficient(0);old=delta_core;delta_core=delta_core/scalar
 assert delta_core*scalar==old
say("complete_new_exceptional_original_NB_PB_mixed_complement_same_point_original_unit_Cramer_return",
    originalSelectedRows=[source_tags[ix] for ix in selected],
    originalDeterminant=profile(det),commonFullTargetCancellation=profile(common),
    actualNecessaryCore=profile(delta_core),paidFactorsRemoved=removed,
    corePolynomialOmittedHereAndSavedExactlyBelow=True,
    exactBareissDivisionProducts=bareiss_divisions,
    allSixOriginalCoordinateIdentitiesMultipliedBack=True,
    allUnpaidTemporaryPivotZeroFibersRetainedByClearedIdentity=True,
    targetUnit="paidScalarDenominator * (D * Sn * Z)^6",
    wholeExceptionalConstantWeightBranchesExcludedByMixedSource=(delta_core.total_degree()==0),
    mainHeadZeroRhoMinusDOutsideScope=True,
    entirePhiFaceClaim=False,ordinaryISPClaim=False)



import zlib,base64
from math import gcd,lcm
from flint import nmod_poly,nmod_mpoly_ctx
fctx=fmpq_mpoly_ctx.get(("rho","lam"),"lex")
assert all(int(ex[2])==0 for ex in delta_core.to_dict())
newcore=fctx.from_dict({(int(ex[0]),int(ex[1])):cc
                       for ex,cc in delta_core.to_dict().items()})
assert ctx.from_dict({(int(ex[0]),int(ex[1]),0):cc
                      for ex,cc in newcore.to_dict().items()})==delta_core
def saved_exact(pp,label):
 data={"variables":["rho","lam"],"terms":[[int(ex[0]),int(ex[1]),str(cc)]
         for ex,cc in sorted(pp.to_dict().items())]}
 payload=json.dumps(data,separators=(",",":")).encode()
 compressed=zlib.compress(payload,9)
 decoded=json.loads(zlib.decompress(compressed))
 assert fctx.from_dict({(i,j):fmpq(cc) for i,j,cc in decoded["terms"]})==pp
 say("new_exact_recoverable_polynomial",label=label,profile=profile(pp),
     encoding="base64+zlib+json",uncompressedBytes=len(payload),
     compressedBytes=len(compressed),payloadSha256=hashlib.sha256(payload).hexdigest(),
     data=base64.b64encode(compressed).decode(),
     completeReconstructionMultipliedBack=True)
saved_exact(newcore,"new_mixed_NB_PB_unit_six_core")
known_payload=zlib.decompress(base64.b64decode(
"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"
))
assert hashlib.sha256(known_payload).hexdigest()=="7c4ecb78633f9539f26e6e989bb883ea78b1ae4919399a7d6358725b0ef5bae8"
known_data=json.loads(known_payload);assert known_data["variables"]==["rho","lam"]
F26=fctx.from_dict({(int(i),int(j)):fmpq(cc) for i,j,cc in known_data["terms"]})
assert profile(F26)["sha256"]=="9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7"
assert list(map(int,F26.degrees()))==[26,26] and len(F26.to_dict())==729
gg=F26.gcd(newcore)
say("new_full_QQ_original_mixed_complement_gcd",
    oldExactF26=profile(F26),newPBUnitCore=profile(newcore),fullQQGcd=profile(gg),
    actualQQGcdConstant=(gg.total_degree()==0),
    finiteOrderedWeightPointUpperBound=(int(F26.total_degree()*newcore.total_degree())
                                      if gg.total_degree()==0 else None),
    atMostSixOriginalTValuesPerWeightPoint=True,
    bothOrderedWeightsNotMergedIntoOneCount=True,
    oldSevenDeterminantsNotReplayed=True)
if gg.total_degree()>0:
 saved_exact(gg,"actual_QQ_common_factor_F26_new_mixed")
 say("new_mixed_complement_no_projection_claim",
     exactGcdNotConstant=True,entirePhiFaceClaim=False,ordinaryISPClaim=False)
 sys.exit(0)
def primitive_integer(pp):
 den=1
 for cc in pp.to_dict().values():den=lcm(den,int(fmpq(cc).denominator))
 vals={ex:fmpq(cc)*den for ex,cc in pp.to_dict().items()}
 content=0
 for cc in vals.values():
  assert cc.denominator==1
  content=gcd(content,abs(int(cc.numerator)))
 assert content
 out=fctx.from_dict({tuple(map(int,ex)):fmpq(int(cc.numerator)//content)
                     for ex,cc in vals.items()})
 scalar=fmpq(den,content)
 if out.coefficient(0)<0:out=-out;scalar=-scalar
 assert out==scalar*pp
 assert all(fmpq(cc).denominator==1 for cc in out.to_dict().values())
 return out,scalar
Fint,Fscale=primitive_integer(F26);Gint,Gscale=primitive_integer(newcore)
def minimum_assignment(cost):
    """Hungarian minimization, returning a matching and feasible integral dual."""
    n = len(cost)
    assert n and all(len(row) == n for row in cost)
    inf = 10**15
    u, v, matching, way = ([0] * (n + 1) for _ in range(4))
    for row in range(1, n + 1):
        matching[0] = row
        col = 0
        reduced_min = [inf] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[col] = True
            active_row = matching[col]
            delta, next_col = inf, 0
            for j in range(1, n + 1):
                if not used[j]:
                    reduced = cost[active_row - 1][j - 1] - u[active_row] - v[j]
                    if reduced < reduced_min[j]:
                        reduced_min[j], way[j] = reduced, col
                    if reduced_min[j] < delta:
                        delta, next_col = reduced_min[j], j
            assert next_col and delta < inf
            for j in range(n + 1):
                if used[j]:
                    u[matching[j]] += delta
                    v[j] -= delta
                else:
                    reduced_min[j] -= delta
            col = next_col
            if matching[col] == 0:
                break
        while True:
            next_col = way[col]
            matching[col] = matching[next_col]
            col = next_col
            if col == 0:
                break
    permutation = [None] * n
    for j in range(1, n + 1):
        permutation[matching[j] - 1] = j - 1
    assert sorted(permutation) == list(range(n))
    assert all(cost[i][j] >= u[i + 1] + v[j + 1]
               for i in range(n) for j in range(n))
    objective = sum(cost[i][j] for i, j in enumerate(permutation))
    assert objective == sum(u[1:]) + sum(v[1:])
    assert all(cost[i][j] == u[i + 1] + v[j + 1]
               for i, j in enumerate(permutation))
    return objective, permutation, u[1:], v[1:]

m,n=int(Fint.degrees()[0]),int(Gint.degrees()[0])
def lambda_degrees_by_rho(pp,degree):
 out=[None]*(degree+1)
 for ex,cc in pp.to_dict().items():
  i,j=int(ex[0]),int(ex[1])
  out[i]=j if out[i] is None else max(out[i],j)
 return out
fd,gd=lambda_degrees_by_rho(Fint,m),lambda_degrees_by_rho(Gint,n)
rowdegrees=[[None]*s+fd+[None]*(n-1-s) for s in range(n)]
rowdegrees+=[[None]*s+gd+[None]*(m-1-s) for s in range(m)]
N=m+n
assert len(rowdegrees)==N and all(len(rr)==N for rr in rowdegrees)
costs=[[10**9 if d is None else -d for d in row] for row in rowdegrees]
objective,matching,dualrows,dualcolumns=minimum_assignment(costs)
assert all(rowdegrees[i][j] is not None for i,j in enumerate(matching))
upper=-objective
assert all(rowdegrees[i][j] is None or
           rowdegrees[i][j]<=-dualrows[i]-dualcolumns[j]
           for i in range(N) for j in range(N))
say("new_fixed_original_rho_resultant_QQ_degree_upper",
    firstOriginalNecessaryPolynomial=profile(Fint),second=profile(Gint),
    fixedRhoDegrees=[m,n],fixedSylvesterOrder=N,lambdaDegreeUpperBound=upper,
    completeMatching=matching,
    upperDualRows=[-a for a in dualrows],upperDualColumns=[-a for a in dualcolumns],
    primitiveIntegerScales=[str(Fscale),str(Gscale)],
    noCompleteQQResultantExpanded=True)
prime=1009
mc=nmod_mpoly_ctx.get(("rho","lam"),prime,"lex")
def mp(pp):return mc.from_dict({tuple(map(int,ex)):int(fmpq(cc).numerator)%prime
                               for ex,cc in pp.to_dict().items()})
fm,gm=mp(Fint),mp(Gint)
assert int(fm.degrees()[0])==m and int(gm.degrees()[0])==n
res=fm.resultant(gm,"rho")
assert res
coef=[0]*(int(res.degrees()[1])+1)
for ex,cc in res.to_dict().items():
 assert int(ex[0])==0;coef[int(ex[1])]=int(cc)
Rbar=nmod_poly(coef,prime)
assert Rbar.degree()<=upper
blob=json.dumps(coef,separators=(",",":")).encode()
packed=zlib.compress(blob,9)
say("new_actual_fixed_original_mixed_rho_resultant_mod",
    prime=prime,fullDegree=int(Rbar.degree()),QQDegreeUpperBound=upper,
    degreeGap=upper-int(Rbar.degree()),
    QQLambdaDegreeAndLeadingUnitPaid=(Rbar.degree()==upper),
    fullModSha256=hashlib.sha256(str(Rbar).encode()).hexdigest(),
    fullCoefficientsEncoding="base64+zlib+json-ascending",
    fullCoefficientsPayloadSha256=hashlib.sha256(blob).hexdigest(),
    fullCoefficientsData=base64.b64encode(packed).decode(),
    allRhoLeadingZeroFibersPreservedByFixedOriginalSylvester=True,
    noModularEmptySetLiftClaim=True,
    entireExceptionalBranchExcluded=False,ordinaryISPClaim=False)

# NEW Gauss return against the already-paid original monic 2033 cover.
# The saved coefficients are from 642bad.  The exact degree/LC statement
# is cf39a424's new original infinity proof, not an assumption from mod data.
base_bytes=zlib.decompress(base64.b64decode("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"))
assert hashlib.sha256(base_bytes).hexdigest()=="e2cc0cd7d4542509e406c2324516f2f7c8d96e9d250f50b8d82c75f2447d6b10"
base_coeff=json.loads(base_bytes)
base_R=nmod_poly(base_coeff,1009)
assert base_R.degree()==2033
assert hashlib.sha256(str(base_R).encode()).hexdigest()=="f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85"
gg,aa,bb=base_R.xgcd(Rbar)
assert aa*base_R+bb*Rbar==gg
assert gg and int(gg[gg.degree()])==1
say("new_mixed_original_projection_true_2033_Gauss_return",
 originalBaseFixedDegrees=[26,31],baseOriginalSylvesterDimension=57,
 exactBaseQQDegreePreviouslyPaid=2033,
 baseLeading1009UnitPreviouslyPaidBy="cf39a424 original infinity kernel certificate",
 newFixedRhoDegrees=[m,n],newOriginalSylvesterDimension=m+n,
 actualModBaseDegree=int(base_R.degree()),actualModNewDegree=int(Rbar.degree()),
 actualFullBezoutProductReturned=True,
 bezoutCoefficientDegrees=[int(aa.degree()),int(bb.degree())],
 actualCommonModDegree=int(gg.degree()),actualCommonModPolynomial=str(gg),
 trueQQDistinctOrderedBasePointUpperBound=int(gg.degree()),
 sameActualOriginalRhoAndAllHeadZeroFibers=True,
 QQIndividualFactorsNotInferredFromModFactorization=True,
 wholeExceptionalOrderedWeightBranchExcluded=(gg.degree()==0),
 bothOrderedWeightsExcludedByBCExchange=(gg.degree()==0),
 mainHeadZeroRhoMinusDOutsideScope=True,ordinaryISPClaim=False)
data=json.dumps([int(gg[j]) for j in range(gg.degree()+1)],separators=(",",":")).encode()
say("new_saved_actual_mixed_Gauss_common_mod_input",
 coefficientsAscending=[int(gg[j]) for j in range(gg.degree()+1)],
 payloadSha256=hashlib.sha256(data).hexdigest(),
 exactQQFactorsNOTPaid=(gg.degree()>0))
content,factors=gg.factor()
prod=nmod_poly([int(content)],1009)
out=[]
for fac,mult in factors:
 prod*=fac**mult
 out.append(dict(degree=int(fac.degree()),multiplicity=int(mult),
  coefficientsAscending=[int(fac[j]) for j in range(fac.degree()+1)]))
assert prod==gg
say("new_actual_mixed_projection_common_mod_factorization",
 content=int(content),factors=out,completeProductReturned=True,
 noCharacteristicZeroFactorLiftClaim=True,
 nextMustUseGenuineOriginalQQFibersOrDivisibility=True)
