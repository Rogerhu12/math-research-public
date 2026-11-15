#!/usr/bin/env python3
"""Exact characteristic-zero original full13 kernel and the SAME deleted13 output.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only small source/parameters/run/hash receipts are permanent; arrays are job-local.
"""
import argparse,gzip,hashlib,importlib.util,itertools,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for key in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[key]="1"
PIN={
 "primitive_equations":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "physical_generator":(15328,"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186"),
 "paid_full_summary":(35730,"2782f380fe5731fd4766fb05fa94a6fa38c36d2d5e491bd63dd1149adc3a9388"),
 "paid_projection_summary":(20819,"28b2605d03746fb5d1a4398c36d22650239d7989f5b68463ed9d6c9f99c5f830"),
 "generic_rank_proof":(9957,"b803d92f159bf26bc9b4a80bbaf5a150ff8f17e81e201b0a99e845b7777038e4")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
from flint import fmpq,fmpq_mat,fmpq_poly
ZERO=fmpq_poly([]);ONE=fmpq_poly([1]);QZERO=fmpq(0)
class BudgetExpired(Exception):pass
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".partial")
 if p.suffix==".gz":
  with gzip.open(q,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:q.write_bytes(canonical(x)+b"\n")
 os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def read(p):
 b=pathlib.Path(p).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b"\x1f\x8b" else b)
def exact_div(a,b):
 need(bool(b),"nonzero exact polynomial divisor")
 q,r=divmod(a,b);need(not r,"complete exact polynomial division")
 return q
def pack_poly(p):
 return {"numerator":[str(x) for x in p.numer().coeffs()],"denominator":str(p.denom())}
def unpack_poly(p):return fmpq_poly([int(x) for x in p["numerator"]],int(p["denominator"]))
def poly_order(p):
 return next((i for i,x in enumerate(p.coeffs()) if x),None)
class RF:
 __slots__=("n","d")
 def __init__(self,n=0,d=1):
  if isinstance(n,RF):
   need(d==1,"RF copy denominator");self.n=n.n;self.d=n.d;return
  n=n if isinstance(n,fmpq_poly) else fmpq_poly([fmpq(n)])
  d=d if isinstance(d,fmpq_poly) else fmpq_poly([fmpq(d)])
  need(bool(d),"nonzero rational-function denominator")
  if not n:self.n=ZERO;self.d=ONE;return
  g=n.gcd(d);n=exact_div(n,g);d=exact_div(d,g)
  lc=d.leading_coefficient();self.n=n*(1/lc);self.d=d*(1/lc)
 def __bool__(self):return bool(self.n)
 def __neg__(self):return RF(-self.n,self.d)
 def __add__(self,other):
  other=RF(other)
  if not self:return other
  if not other:return self
  g=self.d.gcd(other.d);a=exact_div(self.d,g);b=exact_div(other.d,g)
  return RF(self.n*b+other.n*a,a*other.d)
 __radd__=__add__
 def __sub__(self,other):return self+-RF(other)
 def __rsub__(self,other):return RF(other)+-self
 def __mul__(self,other):
  other=RF(other)
  if not self or not other:return RF()
  a=self.n.gcd(other.d);b=other.n.gcd(self.d)
  return RF(exact_div(self.n,a)*exact_div(other.n,b),exact_div(self.d,b)*exact_div(other.d,a))
 __rmul__=__mul__
 def __truediv__(self,other):
  other=RF(other);need(bool(other),"nonzero rational-function divisor")
  return self*RF(other.d,other.n)
 def __rtruediv__(self,other):return RF(other)/self
 def __eq__(self,other):
  other=RF(other);return self.n*other.d==other.n*self.d
 def pack(self):return {"n":pack_poly(self.n),"d":pack_poly(self.d)}
 def order(self):
  if not self:return None
  return poly_order(self.n)-poly_order(self.d)
 def regular(self):return not self or bool(self.d[0])
def unpack_rf(x):return RF(unpack_poly(x["n"]),unpack_poly(x["d"]))
def zero_matrix(n,m):return [[RF() for _ in range(m)] for __ in range(n)]
def matmul(A,B,check):
 n=len(A);k=len(B);m=len(B[0]);need(len(A[0])==k,"complete rational matrix product shape")
 C=zero_matrix(n,m)
 for i in range(n):
  check()
  for j in range(k):
   if A[i][j]:
    for q in range(m):
     if B[j][q]:C[i][q]=C[i][q]+A[i][j]*B[j][q]
 return C
def rf_inverse(A,check):
 n=len(A);M=[[RF(x) for x in row]+[RF(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
 for k in range(n):
  check();pivot=next((i for i in range(k,n) if M[i][k]),None)
  need(pivot is not None,"actual rational normalization block is nonsingular")
  M[k],M[pivot]=M[pivot],M[k];v=M[k][k]
  M[k]=[x/v for x in M[k]]
  for i in range(n):
   if i!=k and M[i][k]:
    q=M[i][k];M[i]=[M[i][j]-q*M[k][j] for j in range(2*n)]
 need(all(M[i][j]==int(i==j) for i in range(n) for j in range(n)),"actual normalization inverse identity")
 return [row[n:] for row in M]
def polynomial_row_profile(H,check):
 """Fraction-free elimination on ORIGINAL H; no evaluation or prime assumption."""
 M=[[x for x in row] for row in H];labels=list(range(len(H)));previous=ONE
 for k in range(9):
  check();poss=[i for i in range(k,len(H)) if M[i][k]]
  need(poss,"actual generic normal linear rank9")
  pivot=min(poss,key=lambda i:(M[i][k].degree(),i))
  M[k],M[pivot]=M[pivot],M[k];labels[k],labels[pivot]=labels[pivot],labels[k]
  v=M[k][k]
  for i in range(k+1,len(H)):
   c=M[i][k]
   for j in range(k+1,9):M[i][j]=exact_div(v*M[i][j]-c*M[k][j],previous)
   M[i][k]=ZERO
  previous=v
 return labels[:9]
def polynomial_inverse(A,check):
 """Bareiss-Montante complete9 inverse; every division exact in Q[u]."""
 n=len(A);M=[[x for x in row]+[ONE if i==j else ZERO for j in range(n)] for i,row in enumerate(A)]
 previous=ONE;sign=1
 for k in range(n):
  check();pivot=next((i for i in range(k,n) if M[i][k]),None)
  need(pivot is not None,"actual polynomial H9 is nonsingular")
  if pivot!=k:M[k],M[pivot]=M[pivot],M[k];sign=-sign
  v=M[k][k];new=[row[:] for row in M]
  for i in range(n):
   if i==k:continue
   c=M[i][k]
   for j in range(2*n):
    if j!=k:new[i][j]=exact_div(v*M[i][j]-c*M[k][j],previous)
   new[i][k]=ZERO
  M=new;previous=v
 D=M[0][0]
 need(D and all(M[i][j]==(D if i==j else ZERO) for i in range(n) for j in range(n)),
      "complete fraction-free diagonal identity")
 inv=[[RF(M[i][n+j],D) for j in range(n)] for i in range(n)]
 product=matmul([[RF(x) for x in row] for row in A],inv,check)
 need(all(product[i][j]==int(i==j) for i in range(n) for j in range(n)),"all81 original polynomial H inverse products")
 return inv,D*sign
def common_columns(M):
 columns=[]
 for j in range(len(M[0])):
  D=ONE
  for row in M:
   d=row[j].d;D=exact_div(D,D.gcd(d))*d
  N=[row[j].n*exact_div(D,row[j].d) for row in M]
  columns.append((D,N))
 return columns
def pack_columns(cols):
 return [{"denominator":pack_poly(D),"numerators":[pack_poly(x) for x in N]} for D,N in cols]
def unpack_columns(cols):
 return [(unpack_poly(x["denominator"]),[unpack_poly(p) for p in x["numerators"]]) for x in cols]
def vp_integer(x):
 x=abs(int(x))
 if x==0:return None
 r=0
 while x%31==0:x//=31;r+=1
 return r
def vp_rational(x):
 if not x:return None
 return vp_integer(x.numer())-vp_integer(x.denom())
def reduce_q31(x):
 need(int(x.denom())%31!=0,"actual rational coefficient denominator is31 unit")
 return int(x.numer())%31*pow(int(x.denom())%31,-1,31)%31
def series31_if_unit(f,count):
 if not f:return [0]*count
 if not f.regular():return None
 scale=f.d[0];nn=[x/scale for x in f.n.coeffs()];dd=[x/scale for x in f.d.coeffs()]
 if any(vp_rational(x) is not None and vp_rational(x)<0 for x in nn+dd):return None
 n=[reduce_q31(x) for x in nn];d=[reduce_q31(x) for x in dd];out=[]
 need(d[0]==1,"actual denominator normalized at zero")
 for k in range(count):
  q=n[k] if k<len(n) else 0
  for j in range(1,min(k,len(d)-1)+1):q-=d[j]*out[k-j]
  out.append(q%31)
 return out
def main(argv=None):
 ap=argparse.ArgumentParser()
 for name in PIN:ap.add_argument("--"+name.replace("_","-"),required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 10<=a.seconds<=600 and 512<=a.memory_mib<=2048,"finite exact Q13 budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024*1024,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);start=time.monotonic();stopping=[False];files={}
 rp=out/"original-characteristic-zero-free13-projection-receipt.json"
 rec={"format":"isp-original-characteristic-zero-free13-projection-v1","status":"running","phase":"inputs",
  "arithmetic":"exact Q[u] and Q(u), python-flint","characteristicZeroFullSmithComputed":False,
  "selectedLeadingCoefficientUnitProved":False,"newLargeGaussianEliminations":0,
  "largeDataUploadedOrCommitted":False,"parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib},"events":[]}
 def signal_stop(signum,frame):stopping[0]=True
 signal.signal(signal.SIGTERM,signal_stop);signal.signal(signal.SIGINT,signal_stop)
 def check():
  if stopping[0] or time.monotonic()-start>=a.seconds-3:raise BudgetExpired("shared exact Q13 deadline")
 def keep(p):files[p.name]={"file":p.name,**identity(p),"temporaryOnly":True}
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=list(files.values());save(rp,rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":rec["mathematicalElapsedSeconds"]}),flush=True)
 rc=1
 try:
  blobs={}
  for name,pin in PIN.items():
   b=getattr(a,name).read_bytes();need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+name);blobs[name]=b
  full=json.loads(blobs["paid_full_summary"]);projection=json.loads(blobs["paid_projection_summary"])
  fr=full["result"];gr=projection["result"];gp=gr["parameters"]
  need(full["exitCode"]==0 and fr["fullGenericRankModulo31"]==4354 and fr["full13FormalKernelMapperConstructed"]
       and fr["all4433OriginalParameterCoefficientsVerified"],"paid original generic rank and full13 dictionary")
  need(projection["exitCode"]==0 and gr["completeOutputProjectionSmithComputed"]
       and gr["sameThirteenOriginalDeletedOutputsVerified"] and gr["outputProjectionTorsionLengthModulo31"]==2,
       "paid original selected output dictionary, not a Q order assumption")
  free27=fr["parameters"]["nativeSummary"]["freeOriginalOutputIndicesZeroBased"]
  fc=gp["formalFreeHeadCoordinates"];F=[free27[i] for i in fc];Ic=gp["deletedOriginalOutputIndicesZeroBased"]
  need(F==[3001,3002,4002,4003,4288,4289,4353,4354,4355,4363,4364,4365,4366]
       and Ic==[3001,3002,4002,4003,4288,4289,4354,4355,4362,4363,4364,4365,4366],
       "same actual original free13 and deleted13")
  material={"version":"original-natural-Q13-physical-polynomial-v1","source":identity(__file__),
    "inputs":{k:digest(v) for k,v in blobs.items()},"originalFree13":F,"originalDeleted13":Ic,
    "naturalChart":"u=1/s; N=Q+u^10 L(1/u)m; Gamma=u^5 Gamma(1/u,m)",
    "originalMomentTransport":"old_m_i=sum_j binom(10-i,j) u^(10-i-j) z_j",
    "sameOriginalFieldProjectionBinding":gp["binding"],"arithmetic":"Q[u]/Q(u)"}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"sameOriginalFree13":F,
    "sameOriginalDeleted13":Ic,"fieldOrder2UsedAsCharacteristicZeroBound":False,
    "paidCharacteristicZeroOutputProjectionUpperBound":25})
  manifest=out/"stage-manifest.json";cache=read(manifest) if manifest.exists() else {"binding":binding,"stages":{}}
  need(cache["binding"]==binding,"same exact source/input stage binding")
  def stage(name,builder):
   path=out/(name+".json.gz")
   if name in cache["stages"]:
    info=cache["stages"][name]
    need(identity(path)=={"bytes":info["bytes"],"sha256":info["sha256"]},"complete saved exact stage")
    v=read(path);need(v["binding"]==binding,"same exact stage material")
    keep(path);rec["events"].append({"reusedCompleteStage":name});return v["payload"]
   value=builder();save(path,{"binding":binding,"payload":value});keep(path)
   cache["stages"][name]=identity(path);save(manifest,cache);keep(manifest)
   return value
  primitive_raw=gzip.decompress(blobs["primitive_equations"])
  need(hashlib.sha256(primitive_raw).hexdigest()==PRIMITIVE_RAW_SHA,"complete original primitive integer equations")
  primitive=json.loads(primitive_raw);eq=primitive["equations"]
  need(primitive["format"]=="r150-original-primitive-integer-equations-v1" and len(eq)==17
       and all(len(row)==77 for row in eq),"all original17 by77 coefficient polynomials")
  need(all(int(x)%31 for x in [primitive["denominator"]]+primitive["contents"]),"original fixed row scales are31 units")
  spec=importlib.util.spec_from_file_location("q13_physical_original",a.physical_generator);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  import flint
  rec["pythonFlintVersion"]=flint.__version__
  terms=[(i,) for i in range(11)]+[(i,j) for i in range(11) for j in range(i,11)]
  term_index={x:i for i,x in enumerate(terms)}
  allmons=[q for degree in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),degree)]
  sources=[q for degree in range(4) for q in itertools.combinations_with_replacement(range(11),degree)]
  cols=[q for q in allmons if sum(j>=2 for j in q)<=1]
  need(len(allmons)==4367 and len(sources)*17==6188 and len(cols)==155,"same complete original truncated dictionaries")
  ci={q:i for i,q in enumerate(cols)};oi={q:i for i,q in enumerate(allmons)}
  variables=[8**i for i in range(11)]
  need([sum(variables[i] for i in allmons[r]) for r in Ic]==gp["deletedOriginalOutputMonomialKeys"],
       "same original monomial keys for every deleted output")
  def original_stage():
   beat("full-natural-physical-coefficient-verification")
   K=m.fmpq_mat([[m.ORIGINAL_K[5-i][5-j] for j in range(6)] for i in range(6)])
   J2=m.polynomial_power_kernel(K,2);J3=m.polynomial_power_kernel(K,3);J3inv=J3.inv()
   need(J3inv*J3==m.fmpq_mat([[int(i==j) for j in range(16)] for i in range(16)]),"complete original J3 inverse")
   p=[[K[i,k] for i in range(6)] for k in range(6)]
   maps=[]
   for k in range(6):
    B=m.fmpq_mat([[p[k][i-j] if 0<=i-j<6 else QZERO for j in range(11)] for i in range(16)])
    maps.append(J3inv*B*J2)
   def lp(t,v):
    return m.fmpq_mat([[sum((t[i+j+k]*v[k] for k in range(6)),QZERO) for j in range(6)] for i in range(6)])
   def polar(N):
    Z=K*N*K;return [sum((Z[i,j] for i in range(6) for j in range(6) if i+j==d),QZERO) for d in range(11)]
   def evaluate(v):
    M=m.hankel(v);KM=K*M;Q=M*K*M;KMK=KM*K;tau=m.trace(KM*KM)
    tensors=[m.values(L*m.column(v)) for L in maps];ans=[]
    for k in range(11):
     N=4*Q if k==0 else m.fmpq_mat(6,6)
     for r in range(max(0,k-5),min(5,k)+1):N+=6*lp(tensors[r],p[k-r])
     gamma=[QZERO]*6
     if k<=5:
      pp=m.values(Q*m.column(p[k]))
      gamma=[2*tau*int(i==k)+8*pp[i]-
       12*sum((tensors[k][i+j+l]*KMK[j,l] for j in range(6) for l in range(6)),QZERO) for i in range(6)]
     ans.append(polar(N)+gamma)
    return ans
   linear=[];diagonal=[];values=[]
   for j in range(11):
    check();v=[QZERO]*11;v[j]=fmpq(1);plus=evaluate(v);minus=evaluate([-x for x in v]);values.append(plus)
    linear.append([[(plus[k][e]-minus[k][e])/2 for e in range(17)] for k in range(11)])
    diagonal.append([[(plus[k][e]+minus[k][e])/2 for e in range(17)] for k in range(11)])
   phys=[[ZERO for _ in range(77)] for __ in range(17)]
   for j in range(11):
    for e in range(17):phys[e][j]=fmpq_poly([linear[j][k][e] for k in range(11)])
   for a0,b0 in terms[11:]:
    check()
    if a0==b0:v=diagonal[a0]
    else:
     w=[QZERO]*11;w[a0]=1;w[b0]=1;both=evaluate(w)
     v=[[both[k][e]-values[a0][k][e]-values[b0][k][e] for e in range(17)] for k in range(11)]
    ix=term_index[(a0,b0)]
    for e in range(17):phys[e][ix]=fmpq_poly([v[k][e] for k in range(11)])
   reversedF=[[ZERO for _ in range(77)] for __ in range(17)];checks=0
   for e in range(17):
    ee=10-e if e<11 else 27-e
    for j,t in enumerate(terms):
     v=list(map(int,eq[e][j]));need(v,"nonempty primitive coefficient polynomial")
     degree=10 if e<11 and j<11 else 0 if e<11 else 5
     if e>=11 and j<11:need(not any(v),"Gamma has no linear coefficients")
     need(not any(v[degree+1:]),"natural parameter degree is exact")
     q=fmpq_poly([(v[degree-k] if degree-k<len(v) else 0) for k in range(degree+1)])
     nt=tuple(sorted(10-x for x in t));reversedF[ee][term_index[nt]]=q
     if e<11:checks+=11 if j<11 else 1
     elif j>=11:checks+=6
   scales=[]
   for e in range(17):
    check();pair=next(((j,k) for j in range(77) for k in range(11) if phys[e][j][k]),None)
    need(pair is not None,"nonzero whole physical equation")
    j,k=pair;scale=reversedF[e][j][k]/phys[e][j][k]
    need(scale and int(scale.numer())%31 and int(scale.denom())%31,"actual original physical equation scale is a31 unit")
    need(all(reversedF[e][j]==phys[e][j]*scale for j in range(77)),
         "every coefficient of each of17 whole natural physical polynomials")
    scales.append(str(scale))
   need(checks==4433,"complete original natural parameter coefficient count")
   Fco=[[ZERO for _ in range(77)] for __ in range(17)]
   def add(e,target,poly,coef,power):
    if poly and coef:Fco[e][term_index[tuple(sorted(target))]]+=poly.left_shift(power)*coef
   for e in range(17):
    check()
    for j,t in enumerate(terms):
     q=reversedF[e][j]
     if not q:continue
     if len(t)==1:
      i=t[0]
      for a0 in range(i+1):add(e,(a0,),q,math.comb(i,a0),i-a0)
     else:
      i,l=t
      for a0 in range(i+1):
       for b0 in range(l+1):add(e,(a0,b0),q,math.comb(i,a0)*math.comb(l,b0),i+l-a0-b0)
   for e in range(17):
    need(not Fco[e][term_index[(0,)]] and not Fco[e][term_index[(1,)]]
      and not Fco[e][term_index[(0,0)]] and not Fco[e][term_index[(0,1)]],
      "all original pure terms except d squared are identically zero")
    if e>=11:need(not Fco[e][term_index[(1,1)]],"all six Gamma pure polynomials vanish")
   return {"Fco":[[pack_poly(q) for q in row] for row in Fco],"rowScales":scales,
    "all4433CoefficientIdentities":True,"all17WholeNaturalEquations":True,
    "reversedK":[[str(K[i,j]) for j in range(6)] for i in range(6)],
    "physicalHashes":{"J2":m.matrix_hash(J2),"J3":m.matrix_hash(J3),
       "maps":[m.matrix_hash(L) for L in maps]},"sourceDegree":3,"outputDegree":5}
  physical=stage("complete-natural-physical-and-comoving-polynomials",original_stage)
  Fco=[[unpack_poly(q) for q in row] for row in physical["Fco"]]
  rec["all4433OriginalParameterCoefficientsVerified"]=True
  rec["all17WholeNaturalPhysicalPolynomialsMatched"]=True
  rec["sameOriginalNaturalUAndReversedPhysicalKernelVerified"]=True
  rec["parameters"]["actual17ConstantRowScales"]=physical["rowScales"]
  rec["parameters"]["physicalHashes"]=physical["physicalHashes"]
  def raw_kernel_stage():
   beat("exact-original-nine-by-nine-rational-kernels")
   H=[[Fco[e][term_index[(j,)]] for j in range(2,11)] for e in range(17)]
   C=[[Fco[e][term_index[(0,j)]] for j in range(2,11)] for e in range(17)]
   D=[[Fco[e][term_index[(1,j)]] for j in range(2,11)] for e in range(17)]
   q=[Fco[e][term_index[(1,1)]] for e in range(17)]
   selected=polynomial_row_profile(H,check);U=[[H[e][j] for j in range(9)] for e in selected]
   inv,det=polynomial_inverse(U,check)
   def solve(rhs):
    return [sum((inv[i][j]*rhs[selected[j]] for j in range(9)),RF()) for i in range(9)]
   r=solve([-RF(v) for v in q])
   cr=[sum((RF(C[e][j])*r[j] for j in range(9)),RF()) for e in range(17)]
   dr=[sum((RF(D[e][j])*r[j] for j in range(9)),RF()) for e in range(17)]
   rc=solve([-x for x in cr]);rd=solve([-x for x in dr])
   for e in range(17):
    need(sum((RF(H[e][j])*r[j] for j in range(9)),RF())+RF(q[e])==0,"all17 original r forcing products")
    need(sum((RF(H[e][j])*rc[j] for j in range(9)),RF())+cr[e]==0,"all17 original rc forcing products")
    need(sum((RF(H[e][j])*rd[j] for j in range(9)),RF())+dr[e]==0,"all17 original rd forcing products")
   Uco=zero_matrix(155,13)
   pure=[(0,)*d for d in range(1,6)]+[(0,)*a0+(1,) for a0 in range(5)]
   for j,t in enumerate(pure):Uco[ci[t]][j]=RF(1)
   Uco[ci[(1,1)]][10]=RF(1);Uco[ci[(0,1,1)]][11]=RF(1);Uco[ci[(1,1,1)]][12]=RF(1)
   for j in range(2,11):
    Uco[ci[(j,)]][10]=r[j-2];Uco[ci[(j,)]][11]=rc[j-2];Uco[ci[(j,)]][12]=rd[j-2]
    Uco[ci[(0,j)]][11]=r[j-2];Uco[ci[(1,j)]][12]=r[j-2]
   return {"HSelectedOriginalEquationRows":selected,"Hdet":pack_poly(det),
     "r":[x.pack() for x in r],"rc":[x.pack() for x in rc],"rd":[x.pack() for x in rd],
     "rawCoMovingKernel":[[x.pack() for x in row] for row in Uco]}
  raw=stage("complete-original-nine-block-and-thirteen-generic-kernels",raw_kernel_stage)
  Uco=[[unpack_rf(x) for x in row] for row in raw["rawCoMovingKernel"]]
  rec["actualOriginalNineByNineRationalProductsVerified"]=True
  rec["parameters"]["actualHSelectedEquationRows"]=raw["HSelectedOriginalEquationRows"]
  rec["parameters"]["actualHDeterminant"]=raw["Hdet"]
  def transport_terms(mon):
   ds=[10-i for i in mon];total=sum(ds);n=len(mon);result={}
   # All pure c,d terms.  Each fixed target has one exact u exponent.
   elementary=[1]+[0]*n
   for d in ds:
    for b in range(n,0,-1):elementary[b]+=d*elementary[b-1]
   for b,c in enumerate(elementary):
    target=(0,)*(n-b)+(1,)*b
    if c and target in ci:result[target]=(c,total-b)
   # Raw and normalized kernels have no one-normal support above degree2.
   if n<=2:
    for k,d in enumerate(ds):
     others=ds[:k]+ds[k+1:]
     for j in range(2,d+1):
      for b in range(n):
       c=math.comb(d,j)*(1 if b==0 else others[0])
       target=tuple(sorted((0,)*(n-1-b)+(1,)*b+(j,)))
       if c and target in ci:
        old=result.get(target,(0,total-j-b));need(old[1]==total-j-b,"same exact transport degree")
        result[target]=(old[0]+c,total-j-b)
   return result
  def evaluate_original_rows(U,indices):
   answer=[]
   for index in indices:
    check();v=[RF() for _ in range(13)]
    for target,(coef,power) in transport_terms(allmons[index]).items():
     row=U[ci[target]];p=ONE.left_shift(power)*coef
     for j in range(13):
      if row[j]:v[j]=v[j]+row[j]*RF(p)
    answer.append(v)
   return answer
  def normalize_stage():
   beat("same-original-free13-normalization-and-regularity")
   for i,t in enumerate(cols):
    if len(t)>=3 and any(j>=2 for j in t):need(not any(Uco[i]),"all one-normal support above degree2 is zero")
   T=evaluate_original_rows(Uco,F);inverse=rf_inverse(T,check)
   Vco=matmul(Uco,inverse,check)
   Fcheck=evaluate_original_rows(Vco,F)
   need(all(Fcheck[i][j]==int(i==j) for i in range(13) for j in range(13)),
        "all169 exact original free13 normalization products")
   bad=[{"row":i,"monomial":list(cols[i]),"column":j,"order":Vco[i][j].order()}
     for i in range(155) for j in range(13) if not Vco[i][j].regular()]
   columns=common_columns(Vco)
   return {"normalizer":[[x.pack() for x in row] for row in inverse],
     "all155NormalizedCoefficientsRegular":not bad,"poleCoordinates":bad,
     "normalizedCoMovingColumns":pack_columns(columns)}
  normalized=stage("complete-original-free13-normalized-kernel",normalize_stage)
  columns=unpack_columns(normalized["normalizedCoMovingColumns"])
  rec["samePaidOriginalFree13IdentityVerified"]=True
  rec["parameters"]["nonregularCoordinates"]=normalized["poleCoordinates"]
  if not normalized["all155NormalizedCoefficientsRegular"]:
   rec.update(status="completed-prefix",outcome="fixed-original-free-chart-not-regular",
      all155NormalizedCoefficientsRegular=False,primitiveFormalKernelProved=False,
      completeCharacteristicZeroOutputProjectionComputed=False)
   rc=75
  else:
   need(all(D[0] for D,N in columns),"complete common denominators are u units")
   beat("complete6188-original-source-products-and4367-coordinate-transport")
   def final_stage():
    # Every original source is covered in the co-moving polynomial unit basis.
    products=0
    for no,mul in enumerate(sources):
     check()
     for e in range(17):
      values=[ZERO for _ in range(13)]
      for j,t in enumerate(terms):
       p=Fco[e][j]
       if not p:continue
       target=tuple(sorted(mul+t));r=ci.get(target)
       if r is not None:
        for c,(den,N) in enumerate(columns):
         if N[r]:values[c]+=p*N[r]
      need(not any(values),"all6188 complete original source equations after exact coordinate unit")
      products+=13
    need(products==80444,"complete original6188 by13 product count")
    old_columns=[(den,[]) for den,N in columns]
    for i,mon in enumerate(allmons):
     check();transport=transport_terms(mon)
     for c,(den,N) in enumerate(columns):
      value=ZERO
      for target,(coef,power) in transport.items():
       if N[ci[target]]:value+=N[ci[target]].left_shift(power)*coef
      old_columns[c][1].append(value)
    for i,raw in enumerate(F):
     for c,(den,N) in enumerate(old_columns):
      need(N[raw]==(den if i==c else ZERO),"all original4367 transported free13 identities")
    G=[[RF(old_columns[c][1][raw],old_columns[c][0]) for c in range(13)] for raw in Ic]
    common=set(F)&set(Ic);extra=list(set(Ic)-set(F));missing=list(set(F)-set(Ic))
    need(len(common)==12 and extra==[4362] and missing==[4353],"same original m6-for-m9squared projection")
    for i,raw in enumerate(Ic):
     if raw in common:
      need(all(G[i][c]==int(F[c]==raw) for c in range(13)),"all twelve same original common unit rows")
    rr=Ic.index(4362);cc=F.index(4353);minor=fmpq_mat([[fmpq(1 if Ic[i]==F[j] else 0)
      for j in range(13) if j!=cc] for i in range(13) if i!=rr])
    sign=minor.det()*(-1 if (rr+cc)%2 else 1);need(sign in (1,-1),"actual exact projection cofactor sign")
    scalar=G[rr][cc];det=scalar*RF(sign)
    need(det and det.regular(),"nonzero regular projection of complete original formal kernel")
    order=det.order();need(0<=order<=25,"paid joint selected-output bound68 minus fullQ lower43")
    kernel31units=all(series31_if_unit(RF(N[r],D),1) is not None for D,N in columns for r in range(155))
    # A regular determinant alone does not prove flat specialization of the
    # primitive kernel.  Compare only after EVERY normalized kernel entry has
    # a coefficientwise31-integral representation with unit constant divisor.
    comparison=series31_if_unit(det,11) if kernel31units else None
    if kernel31units:
     need(comparison is not None,"integral primitive kernel gives integral projection determinant")
     need(comparison==gp["determinantCoefficientsModulo31"],"actual full-kernel reduction matches all11 paid field coefficients")
    return {"all80444ProductsZero":True,"originalProductCoordinates":products,
      "all4367OriginalCoordinatesTransported":True,"completeOriginalKernelColumns":pack_columns(old_columns),
      "projection":[[x.pack() for x in row] for row in G],"projectionCofactorSign":str(sign),
      "projectionScalar":scalar.pack(),"projectionDeterminant":det.pack(),"projectionOrder":order,
      "coefficientwise31UnitRepresentationVerified":kernel31units,
      "paidFieldDeterminantComparisonPerformed":comparison is not None,"determinantFieldSeries":comparison}
   final=stage("complete-original-thirteen-kernel-and-deleted-output-projection",final_stage)
   rec.update(status="completed",outcome="complete-characteristic-zero-original-output-projection",
    all155NormalizedCoefficientsRegular=True,all80444CoMovingOriginalSourceProductsZero=True,
    all4367OriginalOutputCoordinatesTransported=True,sourceAndOutputChangesArePolynomialUnits=True,
    primitiveFormalKernelProved=True,primitiveFormalKernelRank=13,
    completeCharacteristicZeroOutputProjectionComputed=True,
    characteristicZeroOutputProjectionLength=final["projectionOrder"],
    characteristicZeroOutputProjectionPositiveExponents=[] if final["projectionOrder"]==0 else [final["projectionOrder"]],
    characteristicZeroOutputProjectionUnitFactors=13 if final["projectionOrder"]==0 else 12,
    allCommonTwelveOriginalRowsUnitIdentity=True,
    directUntransformed6188PolynomialMultiplicationPerformed=False)
   rec["parameters"].update({"projectionScalar":final["projectionScalar"],"projectionDeterminant":final["projectionDeterminant"],
    "projectionCofactorSign":final["projectionCofactorSign"],"allOriginalProductCoordinates":final["originalProductCoordinates"],
    "coefficientwise31UnitRepresentationVerified":final["coefficientwise31UnitRepresentationVerified"],
    "paidFieldDeterminantComparisonPerformed":final["paidFieldDeterminantComparisonPerformed"],
    "actualDeterminantFieldSeries":final["determinantFieldSeries"],
    "primitiveProof":"K original free13 block=I; all155 coordinates u-regular; any formal kernel coefficient vector is its same free13 coordinates",
    "completeGenericRankJustification":"original13 exact kernels plus paid same original nonzero4354 minor",
    "sameOriginalCoordinateTransport":"reverse original moment indices, then ordinary binomial translation; full degree<=3 source and degree1..5 output maps are polynomial units"})
   rc=0
 except BudgetExpired as e:
  rec.update(status="budget-exhausted",outcome="checkpointed-exact-Q13",error=str(e));rc=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  p=out/"exception.log";p.write_text(traceback.format_exc());keep(p);rc=1
 finally:checkpoint()
 need(rp.stat().st_size<100000,"only small exact execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
