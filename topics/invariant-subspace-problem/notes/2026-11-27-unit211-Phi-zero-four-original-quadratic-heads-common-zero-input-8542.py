#!/usr/bin/env python3
"""NEW full common-zero return for four original Phi=0 quadratic heads.
Reads the already-completed exact four-head JSON, not old original rows.
Fixed QQ[u] Sylvester determinants eliminate Q without dropping any
leading-zero fiber.  The exact common u polynomial is then factored
over QQ; in every irreducible u quotient, the full four original heads
are returned by polynomial gcd with Bezout products, and ONLY actual
original weight-unit factors are removed.  No modular emptiness claim,
no lambda assumption, no original cofactor replay.
120 seconds / 1 GiB. One SHA-pinned JSON dependency beside this source.
"""
import json,re,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
name="2026-11-27-unit211-Phi-zero-monic-twelve-original-four-rows-and-heads-exact-input-8542.json"
raw=Path(__file__).with_name(name).read_bytes()
assert hashlib.sha256(raw).hexdigest()=="e1263fa8c00162a0e9144163c7417d7f603206c235079cda7df92919264b7404"
data=json.loads(raw)
records=data["quadratic_head_minors"]
assert len(records)==4
ctx4=fmpq_mpoly_ctx.get(("u","Q","lam","T"),"lex")
ctx=fmpq_mpoly_ctx.get(("u","Q"),"lex")
u,Q=ctx.gens()
expected=[
"fd3c82df65ec85ccdd5d40ef1f93a115b5f34a0637073a1fbf3c83a0b6e0aa0d",
"4406b4db3ef1c44adf686960f9caafddf42a64afc6fe27fe73cd47ebc9c02e0e",
"db5b53eaf874f9d3b6924edafe79aa6e19080855dfd34a49da9cb8ee0cba9aa6",
"e69b7a64074b7596e43ca5a97060c5032ef63b4ca9870cc63900444d0d50309d"]
def parse_exact_polynomial(s):
 out={}
 for token in re.findall(r"[+-]?[^+-]+",s.replace(" ","")):
  sign=-1 if token.startswith("-") else 1
  if token[0] in "+-":token=token[1:]
  coeff=fmpq(sign);ex=[0,0,0,0]
  for part in token.split("*"):
   mm=re.fullmatch(r"(u|Q)(?:\^([0-9]+))?",part)
   if mm:ex[0 if mm[1]=="u" else 1]+=int(mm[2] or "1")
   else:
    assert re.fullmatch(r"[0-9]+(?:/[0-9]+)?",part),part
    coeff*=fmpq(part)
  ee=tuple(ex);out[ee]=out.get(ee,fmpq(0))+coeff
 return ctx4.from_dict(out)
heads=[]
for k,rec in enumerate(records):
 p4=parse_exact_polynomial(rec["residualPolynomial"])
 digest=hashlib.sha256(str(sorted(p4.to_dict().items())).encode()).hexdigest()
 assert digest==expected[k]==rec["residualAfterPaidUnitFactors"]["sha256"]
 assert all(e[2:]==(0,0) for e in p4.to_dict())
 p=ctx.from_dict({e[:2]:c for e,c in p4.to_dict().items()})
 heads.append(p)
say("new_exact_four_original_weight_heads_loaded",
 sourceJSON=name,sourceJSONSha256=hashlib.sha256(raw).hexdigest(),
 originalHeadHashes=expected,
 degrees=[list(map(int,p.degrees())) for p in heads],
 noOriginalRowsOrCofactorsRecomputed=True)
zero=fmpq_poly([]);one=fmpq_poly([1]);uu=fmpq_poly([0,1])
checks={"QQBareissExactDivisions":0,"QQGcdBezoutProducts":0,
        "fieldInverseQQBezoutProducts":0,"fieldPolynomialDivisionProducts":0,
        "fieldPolynomialGcdBezoutProducts":0,"unitFactorDivisionProducts":0}
def qcoefficients(p):
 n=int(p.degrees()[1]);out=[zero for _ in range(n+1)]
 for (a,b),c in p.to_dict().items():
  cc=[fmpq(0)]*(int(a)+1);cc[int(a)]=c
  out[int(b)]=out[int(b)]+fmpq_poly(cc)
 return out
hc=[qcoefficients(p) for p in heads]
assert [len(p)-1 for p in hc]==[4,6,7,5]
def exact_det(M):
 n=len(M);A=[list(row) for row in M];prev=one;sgn=1
 for k in range(n-1):
  if not A[k][k]:
   pivot=next((i for i in range(k+1,n) if A[i][k]),None)
   if pivot is None:return zero
   A[k],A[pivot]=A[pivot],A[k];sgn=-sgn
  piv=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    num=piv*A[i][j]-A[i][k]*A[k][j]
    q,r=divmod(num,prev)
    assert not r and q*prev==num
    checks["QQBareissExactDivisions"]+=1
    A[i][j]=q
   A[i][k]=zero
  prev=piv
 return A[-1][-1]*sgn
def fixed_resultant(a,b):
 m,n=len(a)-1,len(b)-1;size=m+n
 M=[[zero for _ in range(size)] for _ in range(size)]
 for i in range(n):
  for j in range(m+1):M[i][i+j]=a[j]
 for i in range(m):
  for j in range(n+1):M[n+i][i+j]=b[j]
 return exact_det(M)
def qpinfo(p,full=False):
 d=dict(degree=int(p.degree()),
        sha256=hashlib.sha256(str(p).encode()).hexdigest())
 if full:d["coefficientsAscending"]=[str(p[i]) for i in range(p.degree()+1)]
 return d
cover=zero;results=[];cover_tags=[]
# First the three fixed projections anchored on the smallest-degree head.
# If all three happen to vanish identically, the remaining pairs are also
# processed; this is a finite complete list, not a random source search.
pairs=[(0,1),(0,2),(0,3)]
for i,j in pairs:
 r=fixed_resultant(hc[i],hc[j])
 results.append((i,j,r))
 say("new_fixed_original_head_Sylvester_Q_projection",
     rows=[i,j],fixedQDegrees=[len(hc[i])-1,len(hc[j])-1],
     matrixSize=len(hc[i])+len(hc[j])-2,projection=qpinfo(r),
     everyExactDivisionMultipliedBack=True,allQLeadingZeroFibersRetained=True)
 if r:
  if not cover:cover=r*(1/r[r.degree()]);cover_tags=[one/r[r.degree()]]
  else:
   g,a,b=cover.xgcd(r)
   assert a*cover+b*r==g
   checks["QQGcdBezoutProducts"]+=1
   cover=g
if not cover:
 for i,j in [(1,2),(1,3),(2,3)]:
  r=fixed_resultant(hc[i],hc[j]);results.append((i,j,r))
  say("additional_fixed_original_head_Sylvester_Q_projection",
      rows=[i,j],fixedQDegrees=[len(hc[i])-1,len(hc[j])-1],
      matrixSize=len(hc[i])+len(hc[j])-2,projection=qpinfo(r),
      everyExactDivisionMultipliedBack=True,allQLeadingZeroFibersRetained=True)
  if r:
   if not cover:cover=r*(1/r[r.degree()])
   else:
    g,a,b=cover.xgcd(r);assert a*cover+b*r==g
    checks["QQGcdBezoutProducts"]+=1;cover=g
if not cover:
 say("common_head_zero_cover_unresolved",
     reason="all six fixed QQ projections vanish identically",
     commonHeadZeroFullyExcluded=False,ordinaryISPClaim=False,checks=checks)
 raise SystemExit(0)
cover=cover*(1/cover[cover.degree()])
for _,_,r in results:
 q,s=divmod(r,cover);assert not s and q*cover==r
scalar,factors=cover.factor()
product=fmpq_poly([scalar])
for phi,e in factors:product*=phi**e
assert product==cover
say("new_exact_common_u_cover",
 cover=qpinfo(cover,True),
 irreducibleFactors=[dict(polynomial=str(p),multiplicity=int(e),
                         coefficientsAscending=[str(p[i]) for i in range(p.degree()+1)])
                     for p,e in factors],
 completeQQFactorProductReturned=True)
elln=Q-2*(u-1)*(u-2)
mn=u*Q-elln
Mnum=elln*(2*u-elln)-u*u*Q
unit_inputs=[
 ("Q",Q),("1-Q",1-Q),("ell numerator",elln),
 ("u-ell numerator",mn),("M numerator",Mnum),
 ("-T0",Q+4*(u-1)),("u+Q-1",u+Q-1)]
survivors=[];fibers=[]
for phi,multiplicity in factors:
 phi=phi*(1/phi[phi.degree()])
 if not ((uu*(uu-one))%phi):
  fibers.append(dict(phi=str(phi),excluded=True,
                     reason="actual original u*(u-1) unit is identically zero"))
  say("exact_u_fiber_is_original_unit_zero",**fibers[-1]);continue
 def k(a):
  return (a if isinstance(a,fmpq_poly) else fmpq_poly([a]))%phi
 kz=k(0);ko=k(1)
 def ki(a):
  a=k(a);assert a
  gg,ss,tt=a.xgcd(phi)
  assert ss*a+tt*phi==gg and gg.degree()==0
  ans=(ss*(1/gg[0]))%phi
  assert k(a*ans)==ko
  checks["fieldInverseQQBezoutProducts"]+=1
  return ans
 def trim(a):
  a=[k(x) for x in a]
  while a and not a[-1]:a.pop()
  return a
 def add(a,b):
  c=[kz]*max(len(a),len(b))
  for i in range(len(a)):c[i]=c[i]+a[i]
  for i in range(len(b)):c[i]=c[i]+b[i]
  return trim(c)
 def neg(a):return [-x for x in a]
 def sub(a,b):return add(a,neg(b))
 def mul(a,b):
  if not a or not b:return []
  c=[kz]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):c[i+j]=c[i+j]+x*y
  return trim(c)
 def scale(a,c):return trim([x*c for x in a])
 def divrem(a,b):
  a=trim(a);b=trim(b);assert b
  original=a
  q=[kz]*max(0,len(a)-len(b)+1)
  inv=ki(b[-1])
  while a and len(a)>=len(b):
   shift=len(a)-len(b);coef=k(a[-1]*inv);q[shift]=coef
   for j in range(len(b)):a[shift+j]=k(a[shift+j]-coef*b[j])
   a=trim(a)
  q=trim(q)
  assert add(mul(q,b),a)==original
  checks["fieldPolynomialDivisionProducts"]+=1
  return q,a
 def xgcd(a,b):
  a=trim(a);b=trim(b);aa,bb=a,b
  r0,r1=a,b;s0,s1=[ko],[];t0,t1=[],[ko]
  while r1:
   q,r=divrem(r0,r1)
   r0,r1=r1,r;s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
  if r0:
   cc=ki(r0[-1]);r0=scale(r0,cc);s0=scale(s0,cc);t0=scale(t0,cc)
  assert add(mul(s0,aa),mul(t0,bb))==r0
  checks["fieldPolynomialGcdBezoutProducts"]+=1
  return r0,s0,t0
 pp=[trim(c) for c in hc]
 common=pp[0];tags=[[ko],[],[],[]]
 for i in range(1,4):
  common,aa,bb=xgcd(common,pp[i])
  tags=[mul(aa,x) for x in tags]
  tags[i]=add(tags[i],bb)
 total=[]
 for tag,hp in zip(tags,pp):total=add(total,mul(tag,hp))
 assert total==common
 units=[(name,trim(qcoefficients(p))) for name,p in unit_inputs]
 if any(not up for _,up in units):
  bad=[name for name,up in units if not up]
  fiber=dict(phi=str(phi),excluded=True,reason="actual original unit identically zero",
             identicallyZeroUnits=bad)
  fibers.append(fiber);say("exact_u_fiber_is_original_unit_zero",**fiber);continue
 assert common,("all four heads vanish identically on a u line",str(phi))
 cur=common;removals=[]
 for label,up in units:
  while len(cur)>1:
   gg,ss,tt=xgcd(cur,up)
   if len(gg)<=1:break
   qq,rr=divrem(cur,gg);assert not rr and mul(qq,gg)==cur
   checks["unitFactorDivisionProducts"]+=1
   cur=qq;removals.append(dict(unit=label,removedQDegree=len(gg)-1))
 residual=[qpinfo(c,True) for c in cur]
 fiber=dict(phi=str(phi),phiCoefficientsAscending=[str(phi[j]) for j in range(phi.degree()+1)],
            irreducibleUDegree=int(phi.degree()),originalFourSpecializedQDegrees=[len(x)-1 for x in pp],
            actualFourHeadGcdQDegree=len(common)-1,
            fullFourHeadBezoutTagDegrees=[len(x)-1 for x in tags],
            removedOnlyOriginalWeightUnitFactors=removals,
            residualQDegree=len(cur)-1,residualCoefficients=residual,
            excluded=len(cur)==1)
 fibers.append(fiber)
 if len(cur)>1:survivors.append(fiber)
 say("new_exact_irreducible_u_fiber_four_head_original_unit_return",**fiber)
say("complete_original_four_head_common_zero_QQ_return",
     fixedProjectionCount=len(results),commonUCoverDegree=int(cover.degree()),
     fiberCount=len(fibers),survivingFibers=survivors,
     commonHeadZeroFullyExcluded=not survivors,
     globalThreeGeneratorHeadChartCover=not survivors,
     allOriginalLeadingZeroFibersRetained=True,
     noLambdaOrValueNoncollisionConditionIntroduced=True,
     noOldOriginalCofactorRecomputed=True,
     noModularEmptinessInference=True,checks=checks,ordinaryISPClaim=False)
