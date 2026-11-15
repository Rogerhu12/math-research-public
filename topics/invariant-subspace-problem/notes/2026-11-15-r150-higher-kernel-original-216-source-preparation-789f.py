#!/usr/bin/env python3
"""Original 1632-curve split and high216 source preparation; exact Q + field profile.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
This stage computes no high-kernel Smith value and uses no lost temporary inputs.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[key]="1"
PIN={
 "primitive_equations":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "paid_full_receipt":(72072,"d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e"),
 "paid_full_summary":(35730,"2782f380fe5731fd4766fb05fa94a6fa38c36d2d5e491bd63dd1149adc3a9388"),
 "generic_rank_proof":(9957,"b803d92f159bf26bc9b4a80bbaf5a150ff8f17e81e201b0a99e845b7777038e4")}
RAW_PRIMITIVE="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
class BudgetExpired(Exception):pass
def need(ok,message):
 if not ok:raise ValueError(message)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   h.update(b);n+=len(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 b=pathlib.Path(p).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b"\x1f\x8b" else b)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".partial")
 if p.suffix==".gz":
  with gzip.open(q,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:q.write_bytes(canonical(x)+b"\n")
 os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in PIN:ap.add_argument("--"+key.replace("_","-"),required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=60)
 ap.add_argument("--memory-mib",type=int,default=512)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 10<=a.seconds<=300 and 512<=a.memory_mib<=2048,"explicit finite original source budget")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024*1024,)*2)
 started=time.monotonic();stopped=[False];out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rp=out/"higher-kernel-original-216-source-receipt.json";files=[]
 rec={"format":"isp-original-higher-kernel-216-source-preparation-v1","status":"running","phase":"inputs",
  "allHigherKernelMapsComputed":False,"characteristicZeroHighSmithComputed":False,
  "characteristicZeroFullSmithComputed":False,"selectedLeadingCoefficientUnitProved":False,
  "oldFullSchurLayersRecomputed":False,"oldOutsideSmithRecomputed":False,"largeDataUploadedOrCommitted":False,
  "parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib},"events":[]}
 def stop(sig,frame):stopped[0]=True
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 def check():
  if stopped[0] or time.monotonic()-started>=a.seconds-3:raise BudgetExpired("shared original source preparation budget")
 def keep(p):
  v={"file":p.name,**identity(p),"temporaryOnly":True}
  files[:]=[q for q in files if q["file"]!=v["file"]];files.append(v)
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-started
  rec["parameters"]["temporaryFiles"]=files;save(rp,rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":rec["mathematicalElapsedSeconds"]}),flush=True);check()
 rc=1
 try:
  data={}
  for key,(n,h) in PIN.items():
   b=getattr(a,key).read_bytes();need(digest(b)=={"bytes":n,"sha256":h},"complete pinned input: "+key);data[key]=b
  raw=gzip.decompress(data["primitive_equations"])
  need(hashlib.sha256(raw).hexdigest()==RAW_PRIMITIVE,"complete exact original primitive equations")
  primitive=json.loads(raw);eq=primitive["equations"]
  need(primitive["format"]=="r150-original-primitive-integer-equations-v1" and len(eq)==17
       and all(len(row)==77 for row in eq),"original17 by77 polynomial schema")
  need(len(primitive["contents"])==17 and all(int(x)%31 for x in [primitive["denominator"]]+primitive["contents"]),
       "all fixed original coefficients are31-integral with unit scales")
  F=[[[0]*77 for _ in range(17)] for __ in range(11)]
  for e,row in enumerate(eq):
   for j,poly in enumerate(row):
    v=list(map(int,poly));need(v,"nonempty original coefficient polynomial")
    if e>=11 and j<11:
     need(not any(v),"all original Gamma linear terms zero");continue
    degree=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(v[degree+1:]),"exact original natural parameter degree")
    for k in range(degree+1):F[k][e][j]=v[degree-k] if degree-k<len(v) else 0
  tok=iter(data["native_model"].decode().split())
  need(next(tok)=="R150_NATIVE_NF_V1","same original native model")
  def take(n):return [next(tok) for _ in range(n)]
  count=0
  for e in range(11):
   q=list(map(int,take(66)))
   need(all(q[j]==int(eq[e][j+11][0])%31 for j in range(66)),"all original quadratic coefficients");count+=66
   for j in range(11):
    v=list(map(int,take(11)));p=list(map(int,eq[e][j]))
    need(all(v[d]==(p[d] if d<len(p) else 0)%31 for d in range(11)),"all original linear parameter coefficients");count+=11
  need(int(next(tok))==3333,"all3333 paid prebasis source records")
  pre=[list(map(int,take(4))) for _ in range(3333)]
  for e in range(11,17):
   for j in range(66):
    v=list(map(int,take(6)));p=list(map(int,eq[e][j+11]))
    need(all(v[d]==(p[d] if d<len(p) else 0)%31 for d in range(6)),"all six original Gamma parameter families");count+=6
  ns,nt=map(int,take(2));need((ns,nt)==(2195,9),"complete original remaining-source dictionary")
  take(ns*3);need(list(map(int,take(nt)))==list(range(2,11)) and next(tok,None) is None and count==4433,
    "complete original native tail and4433 coefficients")
  varkeys=[8**i for i in range(11)]
  multuples=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  multipliers=[sum(varkeys[i] for i in q) for q in multuples];mi={x:i for i,x in enumerate(multipliers)}
  outputs=[sum(varkeys[i] for i in q) for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  oi={x:i for i,x in enumerate(outputs)}
  terms=varkeys+[varkeys[i]+varkeys[j] for i in range(11) for j in range(i,11)]
  need(len(multipliers)==364 and len(oi)==4367,"complete original source/output monomials")
  preP=[];preR=[]
  for e,m,p,r in pre:
   need(1<=r<=6188 and (r-1)%17==e and multipliers[(r-1)//17]==m and p in oi,"same original prebasis coordinates")
   preP.append(r);preR.append(oi[p])
  need(len(set(preP))==len(set(preR))==3333,"distinct full prebasis original witnesses")
  paid=json.loads(data["paid_full_receipt"]);ps=paid["summary"]
  need(paid["status"]=="completed" and (ps["field"],ps["components"],ps["sources"],ps["constantRank"],ps["kernelRows"])
       ==(31,1034,2855,1007,1848),"paid original full1007 profile")
  full=json.loads(data["paid_full_summary"]);fr=full["result"];fp=fr["parameters"]
  need(full["exitCode"]==0 and fr["fullConstantRankModulo31"]==4340 and fr["fullGenericRankModulo31"]==4354
       and fr["all3333OriginalPrebasisTriangularUnitProductsVerified"] and fr["all1007OriginalFullPivotProductsVerified"]
       and fr["all4340OriginalUnitJetCancellationsVerified"] and fr["all4433OriginalParameterCoefficientsVerified"],
       "actual same original full4340 unit certificate")
  inputs=fp["inputIdentity"]["inputs"]
  for current,old in (("native_model","native_model"),("paid_full_receipt","paid_full_receipt"),("primitive_equations","primitive_equations"),
                      ("generic_rank_proof","generic_rank_proof")):
   need(inputs[old]==digest(data[current]),"same original unit input: "+current)
  preRset=set(preR);prePset=set(preP)
  components=[i for i in range(4367) if i not in preRset]
  remaining=[i for i in range(1,6189) if i not in prePset]
  rows=ps["constantPivots"];need(len(rows)==1007,"all1007 actual constant pivot records")
  P=list(preP);R=list(preR)
  for c,ordinal,rawrow,scale in rows:
   need(1<=c<=1034 and 1<=ordinal<=2855 and remaining[ordinal-1]==rawrow and 0<scale<31,
        "same complete original full constant pivot coordinate")
   P.append(rawrow);R.append(components[c-1])
  P=sorted(P);R=sorted(R);H=sorted(set(range(1,6189))-set(P))
  need(len(P)==len(set(P))==len(R)==len(set(R))==4340 and len(H)==1848,"same original full unit/complement extents")
  dictionaries={"unitOriginalSourceRowsOneBased":P,"unitOriginalOutputIndicesZeroBased":R,"tailOriginalSourceRowsOneBased":H}
  for key,value in dictionaries.items():
   need(hashlib.sha256(canonical(value)).hexdigest()==fp["nativeDictionarySHA256"][key],"complete paid original dictionary SHA: "+key)
  material={"version":"same-original-high216-curve-split-v1","source":identity(__file__),
   "inputs":{k:digest(v) for k,v in data.items()},"paidFullBinding":fp["binding"],
   "originalDictionarySHA256":fp["nativeDictionarySHA256"],
   "familyOrder":"i<j lex; factor1,m0,...,m10; +Fj*ei-Fi*ej",
   "naturalParameter":"u=1/s; linear N reversed to10; quadratic Gamma reversed to5",
   "exactPolynomialCurveShape":[6188,1632],"tailShape":[1848,1632],"highComplement":216}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"sourceRows":6188,"outputRows":4367,
     "oldConstantUnitRank":4340,"tailSourceRows":1848,"standardCurveColumns":1632})
  rec["all4433OriginalParameterCoefficientsVerified"]=True
  rec["samePaidOriginal4340SourceAndOutputDictionariesVerified"]=True
  manifestpath=out/"complete-stage-manifest.json"
  manifest=read(manifestpath) if manifestpath.exists() else {"binding":binding,"stages":{}}
  need(manifest["binding"]==binding,"same portable completed-stage binding")
  def committed(p):
   if p.name not in manifest["stages"]:return False
   need(p.exists() and identity(p)==manifest["stages"][p.name],"complete saved stage bytes/SHA")
   return True
  def commit(p):
   manifest["stages"][p.name]=identity(p);save(manifestpath,manifest);keep(manifestpath)
  curvepath=out/"complete-original-koszul-tail-polynomial-coordinates.json.gz"
  beat("original-exact-1632-curve-coordinates")
  if committed(curvepath):
   cur=read(curvepath);need(cur["binding"]==binding and cur["tailOriginalSourceRowsOneBased"]==H,
      "same completed original curve binding")
   records=cur["coordinates"];families=cur["families"];counts=cur["nonzerosByDegree"]
   rec["events"].append({"reusedCompleteExactCurveCoordinates":True})
  else:
   hi={r-1:i for i,r in enumerate(H)}
   records=[];families=[];counts=[0]*11;symbolic=0
   for i in range(17):
    for j in range(i+1,17):
     for factor in [0]+varkeys:
      col=len(families);families.append([i,j,factor])
      for source,pol,sign in ((i,j,1),(j,i,-1)):
       for t,key in enumerate(terms):
        mul=key+factor;need(mul in mi,"every natural Koszul coefficient remains in original multiplier degree<=3")
        rr=17*mi[mul]+source
        need((rr%17, multipliers[rr//17])==(source,mul),"every original source coefficient dictionary identity")
        coeff=[[k,str(sign*F[k][pol][t])] for k in range(11) if F[k][pol][t]]
        symbolic+=len(coeff)
        if coeff and rr in hi:
         records.append([hi[rr],col,coeff])
         for k,v in coeff:counts[k]+=1
      check()
   need(len(families)==1632,"all136 pairs times12 original factors")
   cur={"binding":binding,"tailOriginalSourceRowsOneBased":H,"families":families,"coordinates":records,
     "nonzerosByDegree":counts,"allOriginalSourceCoefficientRecordsVerified":True,
     "verifiedOriginalCoefficientRecordCount":symbolic,
     "syzygyProof":"each whole original column is factor*(F_j e_i-F_i e_j); exact original commuting polynomial identity",
     "naturalParameterDegree":10}
   save(curvepath,cur);commit(curvepath)
  keep(curvepath)
  need(cur["allOriginalSourceCoefficientRecordsVerified"] and len(families)==1632
       and len(H)==1848 and len(counts)==11,"complete original family stage")
  # A fresh exact multiplication of each constant base-pair uses the original
  # polynomial dictionaries.  The eleven shifted versions follow from their
  # individually verified source coordinates and multiplication by m_i.
  constantTerms=[[(terms[t],F[0][e][t]) for t in range(77) if F[0][e][t]] for e in range(17)]
  constantProducts=0
  for i in range(17):
   for j in range(i+1,17):
    check();v={}
    for a0,co in constantTerms[j]:
     for b0,dd in constantTerms[i]:
      key=a0+b0;need(key in oi,"original constant Koszul output degree1..5")
      v[key]=v.get(key,0)+co*dd;constantProducts+=1
    for a0,co in constantTerms[i]:
     for b0,dd in constantTerms[j]:
      key=a0+b0;v[key]=v.get(key,0)-co*dd;constantProducts+=1
    need(not any(v.values()),"all136 exact original constant Koszul pair products")
  rec["all136OriginalConstantKoszulPairsExactIntegerZero"]=True
  rec["all1632NaturalSyzygiesProvedByVerifiedOriginalAntisymmetry"]=True
  rec["parameters"]["actualConstantIntegerScalarProducts"]=constantProducts
  q0=[{} for _ in H];seen=set()
  for rr,col,coeff in records:
   need(0<=rr<1848 and 0<=col<1632 and (rr,col) not in seen,"unique complete original tail coordinate")
   seen.add((rr,col));last=-1
   for k,v in coeff:
    need(last<k<=10 and int(v)!=0,"all exact nonzero curve coefficients in increasing natural degree")
    last=k
    if k==0 and int(v)%31:q0[rr][col]=int(v)%31
  profilepath=out/"complete-original-high216-source-profile.json"
  rec["parameters"]["nonzeroTailCoefficientsByDegree"]=counts
  beat("actual-original1632-unit-row-profile")
  from flint import nmod_mat
  import flint
  rec["pythonFlintVersion"]=flint.__version__
  qhash=hashlib.sha256(canonical(q0)).hexdigest()
  if committed(profilepath):
   cp=read(profilepath)
   need(cp["binding"]==binding and cp["tailConstantFieldSHA256"]==qhash
       and cp["actualConstantRank"]==1632 and cp["actualUnitDeterminantModulo31"]%31,
       "complete same original source unit profile")
   rec["events"].append({"reusedCompleteOriginal1632SourceProfile":True})
  else:
   Q=nmod_mat(1848,1632,[row.get(j,0) for row in q0 for j in range(1632)],31)
   T,rank=Q.transpose().rref();rank=int(rank)
   need(rank==1632,"actual original Koszul-tail constant rank1632")
   pivot=[next(j for j in range(1848) if T[i,j]) for i in range(rank)]
   need(pivot==sorted(set(pivot)),"complete field unit row profile")
   U=nmod_mat(1632,1632,[q0[i].get(j,0) for i in pivot for j in range(1632)],31)
   unitdet=int(U.det());need(unitdet!=0,"actual original1632 determinant is a31 unit")
   pivset=set(pivot);e=[i for i in range(1848) if i not in pivset]
   need(len(e)==216,"exact216 original complementary coordinate columns")
   rrefsha=hashlib.sha256(bytes(int(v) for v in T.entries())).hexdigest()
   cp={"binding":binding,"tailConstantFieldSHA256":qhash,"actualConstantRank":1632,
      "actualUnitDeterminantModulo31":unitdet,"unitTailRowPositionsZeroBased":pivot,
      "highComplementTailPositionsZeroBased":e,"highComplementOriginalSourceRowsOneBased":[H[i] for i in e],
      "completeReducedTransposeSHA256":rrefsha,"allOriginalCurveCoordinatesSHA256":identity(curvepath),
      "unitOriginalSourceRowsOneBased":P,"unitOriginalOutputIndicesZeroBased":R,"tailOriginalSourceRowsOneBased":H,
      "localUnitProof":"[Phi_H,E216] determinant has original constant1632 minor a31 unit",
      "characteristicZeroSourceDirectSumProved":True,"coefficientRing":"Z_(31)[[u]]"}
   save(profilepath,cp);commit(profilepath)
   del T,U,Q
  keep(profilepath)
  pivot=cp["unitTailRowPositionsZeroBased"];e=cp["highComplementTailPositionsZeroBased"]
  need(len(pivot)==1632 and len(e)==216 and sorted(pivot+e)==list(range(1848))
       and cp["highComplementOriginalSourceRowsOneBased"]==[H[i] for i in e],"all complete source direct-sum coordinates")
  rec.update(status="completed",outcome="complete-original-high216-source-direct-sum",
   actualKoszulTailConstantRank=1632,actualConstantUnitDeterminantModulo31=cp["actualUnitDeterminantModulo31"],
   highComplementSourceColumns=216,genericHighSchurRankProved=14,highFormalKernelRankProved=202,
   characteristicZeroSourceDirectSumProved=True,sourceDirectSumOverZ31PowerSeriesProved=True,
   all1632ExactOriginalCurveCoordinatesRetained=True,highSchurActuallyComputed=False,
   original4340UnitNumericsRecomputed=False)
  rec["parameters"].update({
   "highComplementTailPositionsZeroBased":e,"highComplementOriginalSourceRowsOneBased":[H[i] for i in e],
   "actual1632UnitTailRowPositionsSHA256":hashlib.sha256(canonical(pivot)).hexdigest(),
   "actualFieldReducedTransposeSHA256":cp["completeReducedTransposeSHA256"],
   "fullSchurConsumer":"S has27 by1848; select these216 columns without inverting Phi_H",
   "exactSourceBackSubstitution":"j(h)=(-U^-1 V h,h); completeK=Phi plus j(E216*ker(S E216))",
   "nextRequiredOriginalObjects":["true full Schur S","regular202-column kernel of S E216",
      "regular202-column original left kernel of O","complete original source back-substitution"],
   "noFieldHighLengthUsedAsCharacteristicZeroConclusion":True})
  rc=0
 except BudgetExpired as ex:
  rec.update(status="budget-exhausted",outcome="checkpointed-original-high216-source-preparation",error=str(ex));rc=75
 except Exception as ex:
  rec.update(status="failed",error=str(ex),exceptionType=type(ex).__name__)
  lp=out/"exception.log";lp.write_text(traceback.format_exc());keep(lp);rc=1
 finally:checkpoint()
 need(rp.stat().st_size<100000,"only small original execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True);return rc
if __name__=="__main__":sys.exit(main())
