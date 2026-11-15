#!/usr/bin/env python3
"""Bridge the completed4318 unit to14 paid Q columns plus4 missing heads.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Reuse the actual field-rank4 prefix. Do not assert31 saturation of HF/T.
The paid old36 residual Qrank14 supplies a complete14-column spanning set.
"""
import argparse,gzip,hashlib,io,json,math,os,pathlib,resource,signal,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
class BudgetExpired(Exception):pass
STOP=False
def stop(signum,frame):
 global STOP
 STOP=True
def need(v,s):
 if not v:raise ValueError(s)
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,v):
 p=pathlib.Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp")
 if p.suffix==".gz":
  with q.open("wb") as raw:
   with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=1) as gz:
    with io.TextIOWrapper(gz,encoding="utf-8",newline="\n") as f:json.dump(v,f,sort_keys=True,separators=(",",":"))
 else:
  b=json.dumps(v,sort_keys=True,separators=(",",":")).encode();need(len(b)<100000,"small permanent metadata only");q.write_bytes(b)
 os.replace(q,p);return {"file":p.name,**identity(p),"temporaryOnly":True}
PREFIX=(3375,"23035e646b1d3598fae8c42e2c34195f910962213a846289fca656ad9f1b7742")
PREFIX_BINDING="8a66f5f182b224bcdf158b3cbd739f23692f333c9c338e7056ca8c5162018ebf"
PREPARER_SHA="6bfab671f390be5f40c30e3d2260bb873ac7c8a37302d2a4902228e6521089b7"
OLD="c40049455e9f310607586b55cc271ca00636dc954f0de63693d0da886a6d067e"
N4="672a21c0de59ec537f5d19333524f92ceb71ad3621eec643b9c11cf3f3fce2d3"
PINS={
 "prefix":PREFIX,
 "old_unit":(9008513,"c53406d65cfd66f2f3b6f1c946bd7495e44c7041538c4f3c85518eb7be7d5dfe"),
 "old_full":(12690,"b186ecd4ef8a8ca910392a8900c838da1e9e166a0b4738b40748677fd7e14a70"),
 "normal4_full":(27679,"4158cc3b978edeafd9c993e7f1c054d9acc419eb9a5d3f34cf8e9f2cff965c22"),
 "normal4_rref":(25174,"7e060678aa752228f8515e105726ad5335aaf403bb8965b19f6be796b25d1956")}
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ("constant-preparation-out","second-out","normal-four-out","out"):ap.add_argument("--"+k,required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=120 and 0<a.memory_mib<=4096,"explicit bounded bridge")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 st=time.monotonic();deadline=st+a.seconds-min(3,a.seconds/10);out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-missing-third-eighteen-unit-preparation-v1","status":"running","phase":"actual-prefix",
  "outputs":[],"parameters":{},"events":[],"largeDataUploadedOrCommitted":False,
  "oldConstantUnitProofRecomputed":False,"old14RationalResidualProfileRecomputed":False,
  "newLargeGaussianPerformed":False,"newRationalRightHandSidesSolved":0,
  "newOriginalThirdCoChainsConstructed":False,"oldHFandT31SaturationAsserted":False}
 cp=out/"missing-third-constant-unit-eighteen-preparation-receipt.json";code=1
 def check():
  if STOP or time.monotonic()>=deadline:raise BudgetExpired("complete18 bridge boundary")
 def ck():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-st;save(cp,rec)
 try:
  ps={"prefix":a.constant_preparation_out/"missing-third-constant-unit-preparation-receipt.json",
   "old_unit":a.second_out/"prepared"/"second-left-m0-unit-input.json.gz",
   "old_full":a.second_out/"full-products"/"second-left-full-products-receipt.json",
   "normal4_full":a.normal_four_out/"full-products"/"normal-four-full-products-receipt.json",
   "normal4_rref":a.normal_four_out/"full-products"/"complete-normal-four-extended-small-residual-rref.json.gz"}
  ids={k:identity(v) for k,v in ps.items()}
  for k,(n,h) in PINS.items():need(ids[k]=={"bytes":n,"sha256":h},"same actual old input "+k)
  prefix=read(ps["prefix"])
  need(prefix["binding"]==PREFIX_BINDING and prefix["status"]=="completed-prefix" and
   prefix["outcome"]=="constant-unit-proved-quotient-field-profile-incomplete" and
   prefix["constantUnitPrime31Proved"] and prefix["all155448ConstantKernelPairingsZero"] and
   prefix["all113204ConstantLeftProductsZero"] and prefix["parameters"]["actualIncomingPrimitiveFieldRank"]==4 and
   prefix["parameters"]["programIdentity"]["sha256"]==PREPARER_SHA,"actual field-rank4 prefix, not a twelve-column field basis")
  outputs={z["file"]:z for z in prefix["outputs"]}
  mp=a.constant_preparation_out/"complete-original-constant-unit-model.json.gz";mid=identity(mp)
  need(mid=={k:outputs[mp.name][k] for k in ("bytes","sha256")},"actual full original constant model bytes")
  model=read(mp);need(model["binding"]==PREFIX_BINDING and model["actualOriginalConstantUnitPrime31Proved"] and
   model["allOriginalRowsAndKernelProductsVerified"] and model["actualIncomingFieldRank"]==4,
   "same completed full original constant model")
  ids["model"]=mid;ps["model"]=mp
  unit=read(ps["old_unit"]);of=read(ps["old_full"]);nf=read(ps["normal4_full"]);rr=read(ps["normal4_rref"])
  need(unit["binding"]==of["binding"]==OLD and of["status"]=="completed" and of["smallResidualRank"]==14,
   "paid complete old36 original residual rank14")
  need(nf["binding"]==rr["binding"]==N4 and nf["status"]=="completed" and
   nf["extendedSmallResidualRank"]==rr["rank"]==144 and nf["all4354OriginalSecondLeftProductsZero"],
   "complete paid166 rational residual profile")
  pp=list(map(int,rr["pivotColumns"]))
  need(pp==sorted(set(pp)) and len(pp)==144,"all true ordered144 pivot columns")
  selected=[j for j in pp if j<36]
  need(len(selected)==14,"actual first36 have14 true rational pivot columns")
  J=list(map(int,unit["originalSourceRows"]));need(J==model["originalSourceRows"],"same complete4354 source coordinates")
  material={"programIdentity":identity(__file__),"inputIdentities":ids,"prefixBinding":PREFIX_BINDING,
   "constantUnitSize":4318,"paidOldQuotientRank":14,"completeIncomingQuotientRank":12,
   "selectedOriginalHFandTColumns":selected,"targetHeadCoordinates":[15,18,19,20],"targets":18}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  rec["binding"]=binding;rec["parameters"].update(material);rec["parameters"].update(secondsLimit=a.seconds,memoryMiB=a.memory_mib)
  ip=out/"invocation.json"
  if ip.exists():need(read(ip)["binding"]==binding,"same portable18 preparation binding")
  save(ip,{**material,"binding":binding,"paths":{k:str(v.resolve()) for k,v in ps.items()}})
  prior=read(cp) if cp.exists() else None
  if prior and prior.get("binding")==binding and prior.get("status")=="completed":
   for z in prior["outputs"]:need(identity(out/z["file"])=={k:z[k] for k in ("bytes","sha256")},"actual complete18 output")
   prior["reusedCompletePreparation"]=True;save(cp,prior);print(json.dumps(prior),flush=True);return 0
  ck();check()
  F=[[int(v) for v in r] for r in unit["originalRightHandSideRows"]]
  need(len(F)==4354 and all(len(r)==36 for r in F),"all actual original HF/T rows")
  contents=list(map(int,model["originalHFandTColumnContents"]));need(len(contents)==36 and all(v>0 for v in contents),"all true original column contents")
  W=[]
  for j in selected:
   col=[r[j] for r in F];g=0
   for v in col:g=math.gcd(g,abs(v))
   need(g==contents[j] and g>0,"each selected original forcing content exactly restored")
   W.append([v//g for v in col])
  Q=[list(map(int,c)) for c in model["originalTargetRightHandSideColumns"]]
  need(len(Q)==4 and all(len(c)==4354 for c in Q) and model["missingHeadCoordinates"]==[15,18,19,20],
   "all actual four original target right sides")
  W+=Q;rows=[dict((int(j),int(v)) for j,v in row) for row in model["originalSparseRows"]]
  R=list(map(int,model["sourceUnitRowPositions"]));E=list(map(int,model["correctionOutputCoordinates"]))
  need(len(rows)==4354 and len(R)==len(set(R))==len(E)==len(set(E))==4318,"same proven constant unit shape")
  gr=[];hc=[0]*4318;un=[]
  for pos in R:
   row=rows[pos];g=0
   for v in row.values():g=math.gcd(g,abs(v))
   need(g>0 and g%31,"all row contents prime to31 for the proven unit")
   gr.append(g);ur={j:v//g for j,v in row.items()};un.append(ur)
   for j,v in ur.items():hc[j]=math.gcd(hc[j],abs(v))
  need(all(h>0 and h%31 for h in hc),"all true positive column contents prime to31")
  sparse=[]
  for row in un:
   need(all(v%hc[j]==0 for j,v in row.items()),"every original coefficient division exact")
   sparse.append([[j,str(v//hc[j])] for j,v in sorted(row.items())]);check()
  meta={"format":"isp-original-constant-unit-eighteen-rhs-v1","binding":binding,
   "modelIdentity":mid,"modelSourceBinding":PREFIX_BINDING,"prefixReceiptIdentity":ids["prefix"],
   "oldRationalResidualProfileIdentity":ids["normal4_rref"],"unitSize":4318,"targets":18,"incomingColumns":14,
   "originalSourceUnitRows":[J[i] for i in R],"sourceUnitRowPositions":R,
   "originalCorrectionOutputCoordinates":E,"positiveRowContents":[str(v) for v in gr],
   "positiveColumnContents":[str(v) for v in hc],"scaledSparseUnitRows":sparse,
   "wholeOriginalRightHandSideColumns":[[str(v) for v in c] for c in W],"rightHandSideSignForNative":-1,
   "selectedOriginalHFandTColumns":selected,"selectedIncomingColumnContents":[str(contents[j]) for j in selected],
   "targetHeadCoordinates":[15,18,19,20],"targetColumnContents":["1"]*4,
   "constantUnitPrime31Proved":True,"old36ForcingImageSpannedBySelected14ModuloM0":True,
   "selected14StillSpanFull12ImageModuloB0":True,"oldHFandT31SaturationAsserted":False,
   "allOriginalUnitCoefficientDivisionsVerified":True,"allWholeOriginalRowsRetained":True,
   "equation":"Mstar*x=-W on4318 original unit rows; x=diag(h)^(-1)Z; diag(g)Aprime Z=-W",
   "twoAdditionalSecondHeadsOnlyAfterActualQResidualKernelAndOriginalProducts":True}
  up=out/"constant-unit-eighteen-right-hand-sides.json.gz";rec["outputs"]=[save(up,meta)]
  rec.update(status="completed",phase="complete",outcome="complete-constant-unit-and-eighteen-rhs-prepared",
   constantUnitPrime31Proved=True,selectedFourteenCompleteOldQuotientBasis=True,
   actualRightHandSides=18,actualIncomingPrimitiveFieldRankRetained=4,
   fullTwelveQuotientColumnIndependenceNotAssumed=True,allFourOriginalTargetsRetained=True)
  rec["parameters"].update(nativeUnitInputIdentity=identity(up),originalConstantModelIdentity=mid,
   actualSparseUnitNonzeros=sum(len(r) for r in sparse),
   maximumOriginalCoefficientBits=max(abs(v).bit_length() for row in rows for v in row.values()),
   maximumScaledUnitCoefficientBits=max(abs(int(v)).bit_length() for row in sparse for j,v in row),
   maximumOriginalRightHandSideBits=[max(abs(v).bit_length() for v in c) for c in W],
   exactNewHomogeneousRelationDimensionToVerify=2)
  code=0
 except BudgetExpired as e:rec.update(status="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);code=1
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8")
 finally:ck()
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
