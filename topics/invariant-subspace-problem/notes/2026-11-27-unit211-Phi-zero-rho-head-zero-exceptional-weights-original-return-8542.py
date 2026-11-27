#!/usr/bin/env python3
"""NEW Phi=0 rho-quadratic head-zero EXCEPTIONAL constant weights.
Choose b=1,c=1/2,ell=3/2; the other exceptional ordered weights are
covered by the original B/C exchange.  The actual rho is free.
Then u=(3+rho)/2,Q=1-rho^2 and Phi is identically zero.
The original monic T-six moment relation is independent of rho.
All eight original values and ONE complete six-row unit Cramer return.
No finite-algebra norm inverse; no complete large QQ resultant.
120 seconds / 1 GiB.  No assertion on the other head-zero branch.
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


# The only additional input is a true six-row unit return on this new face.
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
original_names=["E1","EB_even","EB_odd","N1",
                "NB_even","NB_odd","PB_even","PB_odd"]
source_elements={name:alg.from_mpoly(polys[name]) for name in original_names}
source_rows=[];source_tags=[]
powers=[K6(1)]
for jj in range(1,6):powers.append(powers[-1]*T)
for jj in range(6):
 for name in original_names:
  row,dd=clear_six_vector(source_elements[name]*powers[jj])
  source_rows.append(row)
  source_tags.append(dict(original=name,Tpower=jj,paidScalarDenominator=profile(dd)))
say("new_head_zero_exceptional_complete_original_six_column_candidates",
    originalCount=8,candidateCount=len(source_rows),columns=6,
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
 say("new_head_zero_exceptional_no_six_rows_selected",
     selectionOnly=True,maximumObservedModRank=maximum_rank,
     noQQRankOrExclusionClaim=True)
 sys.exit(0)
mat=[source_rows[ix] for ix in selected]
target_element=D*P
target,target_den=clear_six_vector(target_element)
assert target_element==D*Sn*Z
say("new_head_zero_exceptional_exact_Cramer_start",
    selectedIndices=selected,selectedOriginalTags=[source_tags[ix] for ix in selected],
    selectionOnlyModularPoint=selection,
    target="paidScalarDenominator * D * Sn * Z",
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
  say("new_head_zero_exceptional_QQ_Bareiss_stage",matrix=label,pivotIndex=k,
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
 say("new_head_zero_exceptional_one_actual_target_cofactor",row=i,cofactor=profile(cc),
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
say("complete_new_head_zero_exceptional_same_point_original_unit_Cramer_return",
    originalSelectedRows=[source_tags[ix] for ix in selected],
    originalDeterminant=profile(det),commonFullTargetCancellation=profile(common),
    actualNecessaryCore=profile(delta_core),paidFactorsRemoved=removed,
    corePolynomial=str(delta_core) if len(delta_core.to_dict())<=1200 else None,
    exactBareissDivisionProducts=bareiss_divisions,
    allSixOriginalCoordinateIdentitiesMultipliedBack=True,
    allUnpaidTemporaryPivotZeroFibersRetainedByClearedIdentity=True,
    targetUnit="paidScalarDenominator * D * Sn * Z",
    wholeExceptionalConstantWeightBranchesExcluded=(delta_core.total_degree()==0),
    mainHeadZeroRhoMinusDOutsideScope=True,
    entirePhiFaceClaim=False,ordinaryISPClaim=False)
