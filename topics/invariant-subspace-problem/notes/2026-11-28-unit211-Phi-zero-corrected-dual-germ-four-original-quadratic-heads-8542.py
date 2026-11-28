#!/usr/bin/env python3
"""NEW corrected dual-germ Phi=0 four original quadratic heads.

This is a genuinely different original system: the old E1 used d1^2
where the dual algebra requires 2*d0*d1.  The corrected Rbar is taken
from the complete seven-variable exact certificate SHA256
a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae.
W4, Obar and polarized N1 have their independent true-vm identities.

Only Phi=0, Q*(1-Q)*Pf != 0 and the displayed E0/N0/P1 substitution
are assumed.  No old H1 head, H42, 2*ell-3, m, or u+Q-1 unit is used.
All four maximal quadratic-head minors are new mathematical inputs.
Every denominator and factorization is multiplied back.
No old Gaussian, determinant, projection, or cache is replayed.
120 seconds / 1 GiB; self-contained; only small diagnostic output.
"""
import json,time,hashlib,signal,resource,itertools
from flint import fmpq,fmpq_mpoly_ctx
began=time.perf_counter()
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw,sort_keys=True),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','lam','T','z'),'lex')
up,Qp,Lp,Tp,zp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
z=R(zp)
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
M=ell*V2-u*u;bc=M/(4*delta)
A2=2*lam*lam-2*lam+1
G=lam*P02+(u-1)*T0
Pc=Q*P02*(ell+Tr)-G*T0
ff=-Pc/Pf
assert T0+4*u-4+Q==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
assert Pf*ff+Pc==0
aa=1-ell
vn=J*ff-G+bc*z
wstar=T0+4*u*ff
nn=Q*wstar-2*vn
ww=lam-1-Tr
# Corrected TRUE germ mean, established in the new seven-variable
# integer identity certificate a7f1db43..., not the withdrawn compact R2.
ii=(4*Q*(ff-u)*(vn-Q*ff)+bc*z*z
    +z*(4*bc*u*Q-ell*vn))
Rbar=ii+(m/(2*delta))*z*nn
W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
    +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
    +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
s0=2*ell*vn-(m/delta)*nn
d0=-2*m*vn+ell*nn
Obar=(32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
      +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
      +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z
      -16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn)
al=ell*(1-u)-m
ber=ell*delta-m*(1-u)
av=(2*u-1)*ell+3*m
bur=(2*u-1)*m+3*ell*delta
Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
       +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
       +16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
       -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff
       +16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*z*vn
       -2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aa*Q)
       -8*u*bc*bc*delta*z*z)
N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww

def param(p):return all(e[3]==0 and e[4]==0 for e in p.to_dict())
def info(p):
 return dict(degrees=list(map(int,p.degrees()))[:3],
             terms=len(p.to_dict()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
def extract_quad(p):
 p=R(p);assert param(p.d)
 cc=[zeroP for _ in range(6)]
 slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
 for e,c in p.n.to_dict().items():
  assert (int(e[3]),int(e[4])) in slots
  j=slots[(int(e[3]),int(e[4]))]
  ee=tuple(e[:3])+(0,0);cc[j]=cc[j]+ctx.from_dict({ee:c})
 ans=[R(p0,p.d) for p0 in cc]
 rebuild=ans[0]+ans[1]*Tr+ans[2]*z+ans[3]*Tr*Tr+ans[4]*Tr*z+ans[5]*z*z
 assert rebuild==p
 return ans

def det3(a):
 return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
returned_divisions=0
def divide_exact(a,b):
 global returned_divisions
 q,r=divmod(a,b);assert not r and q*b==a
 returned_divisions+=1
 return q
def assert_base_denominator(p):
 # Phi identities give Pf=4*(u-1)^2*(Q+4*u-4).
 support=Qp*(1-Qp)*(up-1)*(Qp+4*up-4)
 rem=p
 while int(rem.total_degree())>0:
  g=rem.gcd(support)
  assert int(g.total_degree())>0,("unpaid denominator",str(rem))
  rem=divide_exact(rem,g)
 assert rem
def compact_poly(p):
 value=info(p)
 if len(p.to_dict())<=220:value["polynomial"]=str(p)
 return value
def factor_checked(p):
 if not p:return {"zero":True}
 const,factors=p.factor()
 product=poly(const)
 out=[]
 for fac,power in factors:
  product*=fac**int(power)
  row={"power":int(power),**compact_poly(fac)}
  out.append(row)
 assert product==p
 return {"constant":str(const),"factors":out,"fullProductReturned":True}
quads=[extract_quad(p) for p in (Rbar,W4,Obar,N1)]
assert len(quads)==4
for row in quads:
 for c0 in row:assert_base_denominator(c0.d)
heads=[row[3:] for row in quads]
assert all(int(c0.n.degrees()[2])<=0 and int(c0.d.degrees()[2])<=0
           for row in heads for c0 in row)
say("corrected_original_four_quadratics_defined",
    originalRows=["corrected_true_germ_Rbar","original_weighted_mean_W4",
                  "original_mean_difference_Obar","original_polarized_N1"],
    originalParameterAssumptions=["Phi=0","Q!=0","1-Q!=0","Pf!=0"],
    oldHeadOrWeightExclusionUsed=False,
    all24OriginalQuadraticCoefficientsReturned=True,
    allHeadsIndependentOfLambda=True,
    correctedOriginalR2CertificateSHA256=
      "a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae")
nonzero=[]
for selected in itertools.combinations(range(4),3):
 h=det3([heads[i] for i in selected])
 assert_base_denominator(h.d)
 if h:nonzero.append(h.n)
 say("new_corrected_original_maximal_quadratic_head",
     selectedOriginalRows=list(selected),
     numerator=compact_poly(h.n),denominator=compact_poly(h.d),
     numeratorFactorization=factor_checked(h.n),
     denominatorFactorization=factor_checked(h.d),
     noHeadFactorDeleted=True,noHeadZeroFiberExcluded=True)
if nonzero:
 common=nonzero[0]
 for p0 in nonzero[1:]:common=common.gcd(p0)
 for p0 in nonzero:divide_exact(p0,common)
 say("new_corrected_head_common_polynomial_content",
     commonNumerator=factor_checked(common),
     allFourZeroSetNotIdentifiedByGCDAlone=True,
     genericRank=3,numberOfNonzeroMaximalMinors=len(nonzero),
     exactDivisionsReturned=returned_divisions,
     originalPhiExcluded=False,ordinaryISPClaim=False)
else:
 say("new_corrected_head_rank_at_most_two",
     allFourMaximalMinorsExactlyZero=True,
     exactDivisionsReturned=returned_divisions,
     noOldThreeGeneratorModelReused=True,
     originalPhiExcluded=False,ordinaryISPClaim=False)
