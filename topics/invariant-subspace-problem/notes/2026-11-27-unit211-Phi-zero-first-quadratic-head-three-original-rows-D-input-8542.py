#!/usr/bin/env python3
"""NEW Phi=0 three-generator chart and actual D original-ideal return.
Use the original scalar means and original N1, with f=-Pc/Pf, z=Qt.
On the chart of the first true quadratic head, solve exactly for
T^2,T*z,z^2.  The leftover original N1 row and the two actual
multiplication-ambiguity rows form a fixed 3-by-3 original-ideal DAG.
Clear only the FINAL common denominator of the true D target.
All temporary rational-field pivots are multiplied back.  The first
quadratic-head-zero curve is retained; no global head unit claim.
No old six-row cofactor or failed geometric inverse is replayed.
120 seconds / 1 GiB. Self-contained, no helpers or JSON dependencies.
"""
import json,time,hashlib,base64,zlib,signal,resource
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
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
ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
    -4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
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
quads=[extract_quad(p) for p in [Rbar,W4,Obar,N1]]
head=[r[3:] for r in quads[:3]]
lower=[r[:3] for r in quads[:3]]
def determinant(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def adjugate(a):
 out=[[R() for _ in range(3)] for _ in range(3)]
 for i in range(3):
  for j in range(3):
   rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
   v=a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]
   out[i][j]=v if (i+j)%2==0 else -v
 return out
def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(3)),R()) for j in range(3)] for i in range(3)]
def rm(r,b):
 return [sum((r[k]*b[k][j] for k in range(3)),R()) for j in range(3)]
head_det=determinant(head);assert head_det
head_adj=adjugate(head)
assert all(v==(head_det if i==j else 0) for i,row in enumerate(mm(head,head_adj)) for j,v in enumerate(row))
rules=[[-sum((head_adj[i][k]*lower[k][j] for k in range(3)),R())/head_det
        for j in range(3)] for i in range(3)]
assert all(sum((head[i][k]*rules[k][j] for k in range(3)),R())+lower[i][j]==0
           for i in range(3) for j in range(3))
say("new_exact_three_generator_original_mean_chart",
    quadraticHeadNumerator=info(head_det.n),quadraticHeadDenominator=info(head_det.d),
    variables=["T","z"],generators=["1","T","z"],
    allNineOriginalRuleCoefficientIdentitiesReturned=True,
    onlyOnFirstHeadNonzeroChart=True,firstHeadZeroCurveRetained=True)
MT=[[R(0),R(1),R(0)],rules[0],rules[1]]
MZ=[[R(0),R(0),R(1)],rules[1],rules[2]]
commA=mm(MT,MZ);commB=mm(MZ,MT)
comm=[[a-b for a,b in zip(ar,br)] for ar,br in zip(commA,commB)]
assert all(c==0 for c in comm[0])
# This is the fixed reduction of the fourth original polynomial.
leftover=[quads[3][j]+sum((quads[3][3+k]*rules[k][j] for k in range(3)),R())
          for j in range(3)]
rows=[leftover,comm[1],comm[2]]
# The commutator rows are genuine original-ideal rows: apply the
# displayed three original quadratic identities in the two orders
# to T^2*z and T*z^2.  No commutation in the free rank-three module
# is assumed; these very differences remain imposed as extra rows.
Drow=[R(ell*A2)-rules[0][0],-rules[0][1],-rules[0][2]]
assert all(param(rr.n) and param(rr.d) for row in rows+[Drow] for rr in row)
say("new_fixed_original_N1_and_true_multiplication_ambiguity_DAG",
    rows=["original_N1","T_square_z_two_orders","T_z_square_two_orders"],
    actualExtraRowNumerators=[[info(rr.n) for rr in row] for row in rows],
    target="D=ell*A2-T^2",
    originalCoefficientDAGNotOnlyPointwiseNecessary=True,
    noUnprovedAssociativityUsed=True)
det0=determinant(rows)
if not det0:
 say("new_D_target_return_unresolved",
     reason="the fixed three genuine original rows are not generically independent",
     wholePhiFaceExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
adj0=adjugate(rows)
assert all(v==(det0 if i==j else 0) for i,row in enumerate(mm(rows,adj0)) for j,v in enumerate(row))
alpha=[rr/det0 for rr in rm(Drow,adj0)]
assert all(a==b for a,b in zip(rm(alpha,rows),Drow))
den=oneP
for rr in alpha:
 gg=den.gcd(rr.d);den=(den/gg)*rr.d
coeff=[]
for rr in alpha:
 q=den/rr.d;assert q*rr.d==den;coeff.append(rr.n*q)
assert all(sum((R(coeff[i])*rows[i][j] for i in range(3)),R())==R(den)*Drow[j]
           for j in range(3))
say("new_complete_same_original_D_target_common_denominator",
    commonDenominator=info(den),
    threeClearedOriginalRowMultipliers=[info(p) for p in coeff],
    allThreeFullOriginalCoefficientProductsReturned=True,
    temporaryCofactorHeadsNotDeclaredUnits=True)
atoms=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
       ("ell",ell.n),("u-ell",m.n),("M",M.n),("P02",P02.n),
       ("T0",T0.n),("J-Q",(J-Q).n),("u+Q-1",(u+Q-1).n),
       ("lambda",lam.n),("first_quadratic_head_chart_only",head_det.n)]
core=den;stripped=[]
for name,pp in atoms:
 while True:
  gg=core.gcd(pp)
  if gg.total_degree()==0:break
  qq=core/gg;assert qq*gg==core
  core=qq;stripped.append([name,info(gg)])
lc=core.coefficient(0);core=core/lc
assert param(core)
payload=json.dumps({"variables":["u","Q","lambda"],
                    "terms":[[list(map(int,e[:3])),str(c)]
                             for e,c in sorted(core.to_dict().items())]},
                   separators=(",",":")).encode()
packed=zlib.compress(payload,9);back=json.loads(zlib.decompress(packed))
assert ctx.from_dict({tuple(e)+(0,0):fmpq(c) for e,c in back["terms"]})==core
say("complete_new_first_quadratic_head_chart_actual_D_necessary_polynomial",
    core=info(core),strippedOnlyActualOriginalUnitsOrNamedHeadChart=stripped,
    encoding="base64+zlib+json",payloadSha256=hashlib.sha256(payload).hexdigest(),
    uncompressedBytes=len(payload),data=base64.b64encode(packed).decode(),
    fullPayloadDecodeAndRebuildReturned=True,
    actualIdentity="delta*D = polynomial combination of three actual original-ideal rows",
    firstHeadZeroCurveRetained=True,wholePhiFaceExcluded=False,
    entireHeadChartExcluded=core.total_degree()==0,
    noGeometricDOrSnZInverse=True,noNormInverse=True,
    noOldSixRowCofactorRecomputed=True,ordinaryISPClaim=False)
