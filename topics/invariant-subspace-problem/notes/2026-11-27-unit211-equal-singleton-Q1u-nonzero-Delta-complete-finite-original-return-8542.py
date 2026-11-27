#!/usr/bin/env python3
"""New complete original finite return on h=k,Q=1-u,Delta!=0.
Use every root of the three already proved QQ lambda factors of degrees
2,6,24. Reconstruct only the frozen raw original eight-row input prefix,
never its old factorization or four large projection gates.
Specialize whole K[u], return denominators to actual original units,
strip only such units, and perform complete original row Bezout.
180 seconds / 4 GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
QZ=QQ();QO=QQ([1])
class ConstantSplit(Exception):
 def __init__(self,g,h):self.g=g;self.h=h
case_results=[];split_records=[];inverse_count=0;division_count=0
deadline=start+180
dep=Path(__file__).with_name("2026-11-27-unit211-equal-singleton-Q1u-nonzero-Delta-original-two-parameter-return-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="7eaa1987e85a9e1f9ac6752f496dc0ee9a9b31fcaf4c8c99f0d9d376423d095b"
marker=b"\nactual=["
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={"__file__":str(dep),"__name__":"__new_finite_original_Q1u_input__"}
prefixlog=io.StringIO()
with contextlib.redirect_stdout(prefixlog):
 exec(compile(prefix,str(dep),"exec"),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
actual=[("E1",ns["E1"].a),("EBe",ns["EB"].a),("EBo",ns["EB"].b),
        ("N1",ns["n1"].a),("NBe",ns["NB"].a),("NBo",ns["NB"].b),
        ("PBe",ns["PB"].a),("PBo",ns["PB"].b)]
for name,rr in actual:ns["audit_den"](rr.d)
original_units=ns["paid_atoms"]
say("new_Q1u_nonzero_Delta_original_finite_input",
    originalInputSourceSHA256=hashlib.sha256(raw).hexdigest(),
    onlyRawConstructionPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
    noOldOriginalFactorizationOrProjectionGateReplayed=True,
    allEightOriginalRowsReconstructed=True,
    allOriginalAffineMomentsE0N0P1NVAndBothSingletonTargetsReturned=True,
    completeLambdaFactorDegrees=[2,6,24],claimExcluded=False)

def process_case(phi,label):
 global inverse_count,division_count
 phi=phi/phi[phi.degree()]
 class C:
  def __init__(self,v=0):
   if isinstance(v,C):self.p=v.p;return
   if isinstance(v,fmpq_poly):pp=v
   elif isinstance(v,(list,tuple)):pp=QQ(v)
   else:pp=QQ([v])
   qq,rr=divmod(pp,phi);assert qq*phi+rr==pp
   self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return C(-self.p)
  def __add__(self,v):return C(self.p+C(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-C(v)
  def __rsub__(self,v):return C(v)+-self
  def __mul__(self,v):return C(self.p*C(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==C(v).p
  def inv(self):
   global inverse_count
   assert self
   gg,ss,tt=self.p.xgcd(phi)
   assert ss*self.p+tt*phi==gg
   if gg.degree()>0:
    qq,rr=divmod(phi,gg);assert not rr and qq*gg==phi
    assert 0<gg.degree()<phi.degree()
    raise ConstantSplit(gg,qq)
   out=C(ss/gg[0]);assert self*out==C(1);inverse_count+=1
   return out
  def __truediv__(self,v):return self*C(v).inv()
  def __rtruediv__(self,v):return C(v)*self.inv()
  def __pow__(self,n):
   assert isinstance(n,int) and n>=0
   out=C(1)
   for i in range(n):out=out*self
   return out
  def data(self):return [str(v) for v in self.p.coeffs()]
 z=C();one=C(1)
 def trim(pp):
  while pp and not pp[-1]:pp.pop()
  return pp
 def add(aa,bb):
  cc=[z]*max(len(aa),len(bb))
  for j,v in enumerate(aa):cc[j]=cc[j]+v
  for j,v in enumerate(bb):cc[j]=cc[j]+v
  return trim(cc)
 def neg(aa):return [-v for v in aa]
 def sub(aa,bb):return add(aa,neg(bb))
 def mul(aa,bb):
  if not aa or not bb:return []
  cc=[z]*(len(aa)+len(bb)-1)
  for i,v in enumerate(aa):
   for j,w in enumerate(bb):cc[i+j]=cc[i+j]+v*w
  return trim(cc)
 def scale(aa,v):return trim([cc*v for cc in aa])
 def divrem(aa,bb):
  global division_count
  assert bb
  rr=aa[:];qq=[z]*max(0,len(aa)-len(bb)+1);iv=bb[-1].inv()
  while rr and len(rr)>=len(bb):
   shift=len(rr)-len(bb);cf=rr[-1]*iv
   qq[shift]=qq[shift]+cf
   for j,v in enumerate(bb):rr[j+shift]=rr[j+shift]-cf*v
   rr=trim(rr)
  qq=trim(qq);assert add(mul(qq,bb),rr)==aa;division_count+=1
  return qq,rr
 def xgcd(aa,bb):
  r0,r1=aa[:],bb[:];s0,s1=[one],[];t0,t1=[],[one]
  while r1:
   q0,r2=divrem(r0,r1)
   r0,r1=r1,r2;s0,s1=s1,sub(s0,mul(q0,s1));t0,t1=t1,sub(t0,mul(q0,t1))
   assert add(mul(s0,aa),mul(t0,bb))==r0
   assert add(mul(s1,aa),mul(t1,bb))==r1
  if not r0:return [],[],[]
  iv=r0[-1].inv();gg,ss,tt=scale(r0,iv),scale(s0,iv),scale(t0,iv)
  assert add(mul(ss,aa),mul(tt,bb))==gg
  return gg,ss,tt
 def from_mpoly(pp):
  if not pp:return []
  out=[z]*(int(pp.degrees()[1])+1)
  byq={}
  for ex,cc in pp.to_dict().items():
   il,iq=map(int,ex)
   if iq not in byq:byq[iq]=[fmpq(0)]*(int(pp.degrees()[0])+1)
   byq[iq][il]=fmpq(cc)
  for iq,cc in byq.items():out[iq]=C(QQ(cc))
  return trim(out)
 def pdata(pp):return [cc.data() for cc in pp]
 def small_profile(pp):
  blob=json.dumps(pdata(pp),separators=(",",":")).encode()
  r=dict(uDegree=len(pp)-1,bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
  if len(blob)<=8192:r["coefficients_u_then_lambda"]=pdata(pp)
  return r

 try:
  units=[]
  for name,ap in original_units:
   pp=from_mpoly(ap)
   if not pp:
    out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=True,
             excludedByEntireOriginalUnitZero=name,
             lambdaFactor=[str(cc) for cc in phi.coeffs()],
             allLambdaEmbeddingsRetained=True)
    case_results.append(out);say("new_Q1u_nonzero_Delta_whole_original_unit_zero",**out)
    return
   units.append((name,pp))
  def strip(pp):
   original=pp[:];product=[one];records=[]
   for name,ap in units:
    count=0
    while pp:
     gg,ss,tt=xgcd(pp,ap)
     assert add(mul(ss,pp),mul(tt,ap))==gg
     if len(gg)<=1:break
     nn,rr=divrem(pp,gg);assert not rr
     pp=nn;product=mul(product,gg);count+=1
    if count:records.append(dict(originalUnit=name,gcdLoops=count))
   assert mul(pp,product)==original
   return pp,records
  cores=[];rows=[]
  for name,rr in actual:
   den=from_mpoly(rr.d)
   assert den,("entire_original_denominator_zero",name)
   left,removed_den=strip(den)
   assert len(left)==1,("unpaid_specialized_original_denominator",name,pdata(left))
   original_num=from_mpoly(rr.n)
   pp,removed=strip(original_num)
   cores.append((name,pp))
   rows.append(dict(name=name,originalUDegree=len(original_num)-1,
                    primitive=small_profile(pp),
                    onlyPaidNumeratorRemovals=removed,
                    wholeOriginalDenominatorReturned=True))
  say("new_Q1u_nonzero_Delta_complete_original_finite_rows",
      case=label,lambdaDegree=int(phi.degree()),rows=rows,
      allLambdaRootsAndAllUSpecializationsRetained=True,
      constantFieldInversesActuallyReturned=True,claimExcluded=False)
  gg=[];tags=[];done=[]
  for name,pp in cores:
   newg,ss,tt=xgcd(gg,pp)
   tags=[mul(ss,tag) for tag in tags]+[tt]
   done.append((name,pp));gg=newg
   check=[]
   for tag,(_,ip) in zip(tags,done):check=add(check,mul(tag,ip))
   assert check==gg
   say("new_Q1u_nonzero_Delta_original_finite_Bezout",
       case=label,newOriginalRow=name,uDegree=len(gg)-1,
       allOriginalCoefficientProductsReturned=True)
   if len(gg)==1:break
  cert=dict(lambdaFactor=[str(cc) for cc in phi.coeffs()],
            originalRows=[dict(name=nn,coefficients=pdata(pp)) for nn,pp in done],
            tags=[pdata(tt) for tt in tags],finalUPolynomial=pdata(gg))
  bb=json.dumps(cert,separators=(",",":")).encode()
  out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=len(gg)==1,
           originalRowsUsed=[nn for nn,pp in done],finalUPolynomial=pdata(gg),
           allLambdaEmbeddingsRetained=True,allOriginalUnitFibersAccounted=True,
           certificateBytes=len(bb),certificateSHA256=hashlib.sha256(bb).hexdigest(),
           fullCertificate=cert if len(bb)<=16000 else None)
  case_results.append(out);say("new_Q1u_nonzero_Delta_complete_original_finite_return",**out)
 except ConstantSplit as ex:
  assert ex.g*ex.h==phi
  rec=dict(case=label,left=[str(cc) for cc in ex.g.coeffs()],
           right=[str(cc) for cc in ex.h.coeffs()],bothBranchesRetained=True)
  split_records.append(rec);say("new_Q1u_nonzero_Delta_constant_nonunit_split",**rec)
  process_case(ex.g,label+"/left");process_case(ex.h,label+"/right")

factors=[
 [1,-2,3],
 [2,-12,39,-76,96,-72,24],
 [-18,399,-4412,32152,-171905,710808,-2332482,6112826,-12570078,18848763,
 -14402138,-21172682,111728893,-266613390,460231700,-629475832,702614944,
 -645322096,486216224,-296971456,143911680,-53435136,14348800,-2500608,215040]
]
for coefficients in factors:
 pp=QQ(coefficients)
 assert pp.gcd(pp.derivative()).degree()==0
 process_case(pp,"complete_lambda_degree_"+str(pp.degree()))
signal.alarm(0)
say("new_Q1u_nonzero_Delta_entire_original_finite_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalDomain="h=k!=1,Q=1-u,Delta!=0",
    allOriginalReturns=case_results,constantSplits=split_records,
    allThreeCompleteLambdaFactorsProcessed=True,
    entireOriginalFaceExcluded=bool(case_results) and all(x["excluded"] for x in case_results),
    actualConstantInverseCount=inverse_count,actualPolynomialDivisionCount=division_count,
    complementaryDeltaZeroFaceStillRequiresFullGramReturn=True,
    ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
