#!/usr/bin/env python3
"""Rebuild the lost temporary same-I,J natural-u session from historical inputs.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Original first-connection and Schur engines stay byte-identical. New input bytes
have a new binding; the complete paid0..16 arrays are compared after header-only
binding normalization. No release assets or large-data publication are used.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,itertools,json,math,os,pathlib,resource,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[k]="1"
PIN={
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "point_model":(87459,"97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"),
 "selected_receipt":(75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "kernel36":(222788,"c008e57b7a7e80312f8ba292bb24241d53bb59d4c57b2a8d07ec1017b9de0744"),
 "source_dag":(957557,"c50e7bb8558a7f637d9d6951f64ae002c96cdce06dfcb7d1a4619ea6dc07337a"),
 "primitive_equations":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "paid16_summary":(93340,"938d1796c73b780d3fdb379c83e21907381618dcd9e81c7b281b21c6e4a1484f"),
 "first_runner":(20861,"45991f0744fe8b020170c77a6f99e4b6e3e9433a3f18ca4c0405cdd76132bab6"),
 "schur_runner":(21664,"80f6815133250cf559f81afb557f138952f7268ce2d2b43e2c15bfb822775e67")}
OLD_BINDING="1fdb07aa85a565c45d7adfe04721a29cdbe6911cc0cb50ca45044c51f88ccc01"
FIRST_NAMES={"receipt":"selected-natural-first-connection-f31-receipt.json",
 "product":"whole-natural-first-product-field31.json.gz",
 "cokernel":"complete-selected-cokernel36-field31.json.gz",
 "full_connection":"full-output-selected-first-connection49-field31.bin"}
FREE=[1271,1204,1205,1256,1206,1223,1257,1156,1207,1224,2393,3328,4093,2326,3261,4501,4026,4281,4502,4587,2327,2378,3262,3313,4027,4078,4248,4282,4503,1716,1733,1750,1767,1784,1801,1818]
class BudgetExpired(Exception):pass
def need(x,s):
 if not x:raise ValueError(s)
def ident(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def read(p):
 p=pathlib.Path(p)
 with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open("r",encoding="utf-8")) as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);q=p.with_name(p.name+".tmp");q.write_text(json.dumps(x,separators=(",",":"),ensure_ascii=False)+"\n",encoding="utf-8");os.replace(q,p)
def unchanged_json(p,x):
 b=(json.dumps(x,separators=(",",":"),ensure_ascii=False)+"\n").encode()
 if p.exists():need(p.read_bytes()==b,"existing exact rebuilt input is unchanged: "+p.name)
 else:p.write_bytes(b)
 return digest(b)
def imported(name,p):
 sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in list(PIN)+["repo-notes","out"]:ap.add_argument("--"+key.replace("_","-"),type=pathlib.Path,required=True)
 ap.add_argument("--maximum-degree",type=int,default=32);ap.add_argument("--seconds",type=float,default=60)
 ap.add_argument("--memory-mib",type=int,default=512);ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args(argv);need(16<=a.maximum_degree<=32 and math.isfinite(a.seconds) and 0<a.seconds<=600 and 0<a.memory_mib<=2048 and 0<a.compile_seconds<=30,"bounded exact session rebuild")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 inputs=out/"rebuilt-inputs";inputs.mkdir(exist_ok=True);firstdir=out/"rebuilt-first";schurdir=out/"natural-u"
 rec={"format":"isp-same-IJ-natural-u-minimal-temporary-rebuild-v1","status":"running","phase":"historical-inputs",
  "lostRunId":"43679903558","lostSessionReason":"session ended after32 computation; execution summary exceeded100000bytes before publication",
  "oldTemporaryBinaryFilesClaimedRecovered":False,"largeDataUploadedOrCommitted":False,
  "originalMathematicalEngineBytesUnchanged":True,"newInputBindingExplicit":True,
  "noRational585NullspaceRequired":True,"noLargeOriginalEliminationRepeated":True,
  "leadingUnitProved":False,"characteristicZeroInfinityOrderComputed":False,"parameters":{},"events":[]}
 code=1;preseconds=None;poststart=None
 def checkpoint():
  rec["wallSeconds"]=time.monotonic()-start;save(out/"selected-natural-u-minimal-rebuild-receipt.json",rec)
 try:
  ids={}
  for key,pin in PIN.items():
   ids[key]=ident(getattr(a,key));need(ids[key]=={"bytes":pin[0],"sha256":pin[1]},"historical/published exact input "+key)
  wrapper=ident(__file__);rec["parameters"].update(inputIdentities=ids,wrapperIdentity=wrapper,
   secondsLimit=a.seconds,memoryMiB=a.memory_mib,compileSecondsLimit=a.compile_seconds,requestedMaximumDegree=a.maximum_degree)
  point=read(a.point_model);old=read(a.selected_receipt);paid16=read(a.paid16_summary)
  paid=paid16["result"];par16=paid["parameters"]
  need(paid16["runId"]=="43679903558" and paid16["stepId"]=="selected-natural-u-schur-through16" and
   paid["status"]=="completed" and paid["completedNaturalDegree"]==16 and par16["binding"]==OLD_BINDING,"paid16 actual summary scope")
  need(paid["all4354SelectedJetIdentitiesVerified"] and paid["all4367OriginalResidualCoordinatesRetained"] and
   paid["all36FreeSourceCoordinatesVerified"] and paid["all33CompleteOriginalFirstCorrectionsVerified"],"paid16 complete original flags")
  need(point["characteristicZeroSameOriginal17Verified"] and old["selectedFullConstantRankModulo31"]==4318,"original historical point and selected profile")
  tok=iter(a.native_model.read_text().split());need(next(tok)=="R150_NATIVE_NF_V1","same original native model")
  def take(n):return [next(tok) for _ in range(n)]
  take(11*(66+11*11));need(int(next(tok))==3333,"all3333 original prebasis records")
  pre=[tuple(map(int,take(4))) for _ in range(3333)]
  take(6*66*6);need(tuple(map(int,take(2)))==(2195,9),"same2195 source dictionary")
  take(2195*3);need(list(map(int,take(9)))==list(range(2,11)) and next(tok,None) is None,"complete original model tail")
  mult=[q for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  whole=[q for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  keys=[sum(8**j for j in q) for q in whole];ki={k:i for i,k in enumerate(keys)}
  mulkeys=[sum(8**j for j in q) for q in mult]
  need(len(whole)==4367 and len(mult)==364,"original complete monomial dictionaries")
  for e,mu,piv,raw in pre:need(1<=raw<=6188 and e==(raw-1)%17 and mu==mulkeys[(raw-1)//17] and piv in ki,"all original prebasis raw/multiplier/output records")
  sources=list(map(int,point["selectedSourceRows"]));outputs=list(map(int,point["selectedOutputIndicesZeroBased"]));ind=list(map(int,point["independentSelectedSourceIndicesZeroBased"]))
  need(sources==list(map(int,old["selectedSourceRows"])) and ind==list(map(int,old["independentSelectedSourceIndicesZeroBased"])),"same historical1021 and985 original source identities")
  need(len(set(sources))==len(set(outputs))==1021 and len(set(ind))==985,"all distinct paid lower dictionaries")
  J=sorted([r[3] for r in pre]+sources);I=sorted([ki[r[2]] for r in pre]+outputs)
  need(len(J)==len(set(J))==len(I)==len(set(I))==4354,"same complete original4354 I,J from original3333+1021")
  free=list(map(int,old["selectedConstantKernelFreeOriginalRows"]))
  need(free==FREE==par16["selectedFreeOriginalRows"] and set(free)==set(sources)-{sources[i] for i in ind},"same36 original free coordinates")
  need(I==sorted(par16["oldCokerOriginalOutputIndices"]+par16["nativeSummary"]["unitOriginalOutputIndices"]) if "unitOriginalOutputIndices" in par16.get("nativeSummary",{}) else True,"paid original I if retained verbatim")
  # These are lean original-index manifests, not fabricated old gzip files.
  selected_path=inputs/"same-selected-original-source-indices.json"
  profile_path=inputs/"same-selected-original-output-indices.json"
  selid=unchanged_json(selected_path,{"format":"isp-rebuilt-exact-selected-source-dictionary-v1","rebuildCodeSHA256":wrapper["sha256"],
   "historicalNativeIdentity":ids["native_model"],"historicalPointIdentity":ids["point_model"],"selectedRows":J,"freeRows":free})
  profid=unchanged_json(profile_path,{"format":"isp-rebuilt-exact-selected-output-dictionary-v1","rebuildCodeSHA256":wrapper["sha256"],
   "historicalNativeIdentity":ids["native_model"],"historicalPointIdentity":ids["point_model"],"originalOutputI":I})
  F0=[list(map(int,row)) for row in point["primitivePointCoefficients"]]
  need(len(F0)==17 and all(len(row)==77 for row in F0),"all original1309 primitive point coefficients")
  terms=[(j,) for j in range(11)]+[(j,k) for j in range(11) for k in range(j,11)]
  need(all(not F0[e][j] for e in range(17) for j,m in enumerate(terms) if all(v>=9 for v in m)),"actual pure critical plane")
  proj=[i for i,q in enumerate(whole) if 1<=sum(v<=8 for v in q)<=2];oi={whole[i]:j for j,i in enumerate(proj)}
  active=[r for r in J if sum(v<=8 for v in mult[(r-1)//17])<=1]
  need(len(proj)==585 and len(active)==954,"same lost original585 by954 projection")
  columns=[]
  for raw in active:
   e=(raw-1)%17;mu=mult[(raw-1)//17];c={}
   for k,t in enumerate(terms):
    if not F0[e][k]:continue
    m=tuple(sorted(mu+t))
    if m in oi:c[oi[m]]=c.get(oi[m],0)+F0[e][k]
   columns.append([[j,str(v)] for j,v in sorted(c.items()) if v])
  projected_path=inputs/"same-original-second-transverse-integer-input.json"
  projid=unchanged_json(projected_path,{"format":"isp-rebuilt-original585-projection-v1","rebuildCodeSHA256":wrapper["sha256"],
   "historicalNativeIdentity":ids["native_model"],"historicalPointIdentity":ids["point_model"],"originalSourceRows":active,
   "originalOutputIndices":proj,"originalOutputMonomials":[list(whole[i]) for i in proj],"originalSparseColumns":columns,
   "allOtherSelectedSourceColumnsProjectToZeroByTransverseDegree":True})
  rec["parameters"].update(rebuiltInputs={"selected_model":selid,"unit_profile":profid,"projected_input":projid},
   selectedSourceCount=4354,selectedOutputCount=4354,selectedFreeOriginalRows=free,projectedOutputCount=585,projectedSourceCount=954,
   originalIFromPrebasisPlusPointSHA256=digest((json.dumps(I,separators=(",",":"))+"\n").encode())["sha256"],
   originalJFromPrebasisPlusPointSHA256=digest((json.dumps(J,separators=(",",":"))+"\n").encode())["sha256"])
  rec["phase"]="rebuild-lost-finite-first-caches";checkpoint()
  F=imported("frozen_natural_first",a.first_runner)
  need(F.PIN["selected_model"]==(814572,"0aa2d6d5c368b9885e279cd5b8e2cc7a59ba574ca161c0535193c30defe52d3d"),"frozen first module expected input ABI")
  F.PIN=dict(F.PIN)
  for key,v in [("selected_model",selid),("unit_profile",profid),("projected_input",projid)]:F.PIN[key]=(v["bytes"],v["sha256"])
  firstcache=out/"rebuilt-first-stage-cache.json"
  fm={"engine":ids["first_runner"],"inputs":{k:v for k,v in ids.items() if k in ["point_model","native_model","kernel36","primitive_equations"]},"rebuilt":rec["parameters"]["rebuiltInputs"]}
  firsttag=hashlib.sha256(json.dumps(fm,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  if firstcache.exists():
   fc=read(firstcache);need(fc["binding"]==firsttag,"same rebuilt complete first-stage binding")
   for name,v in fc["outputs"].items():need(ident(firstdir/name)==v,"all actual rebuilt first files intact")
   rec["events"].append({"reusedCompleteRebuiltFirstCache":True})
  else:
   remain=a.seconds-(time.monotonic()-start)
   if remain<=2:raise BudgetExpired("shared clock before first-cache rebuild; deterministic inputs retained")
   args=["--point-model",str(a.point_model),"--selected-model",str(selected_path),"--unit-profile",str(profile_path),
    "--kernel36",str(a.kernel36),"--projected-input",str(projected_path),"--native-model",str(a.native_model),
    "--primitive-equations",str(a.primitive_equations),"--out",str(firstdir),"--seconds",str(min(30,remain-1)),"--memory-mib",str(a.memory_mib)]
   with (out/"rebuild-first.log").open("w",encoding="utf-8") as log:
    with contextlib.redirect_stdout(log):firstcode=F.main(args)
   if firstcode==75:raise BudgetExpired("actual first-cache rebuild reached shared clock; complete files retained")
   need(firstcode==0,"actual original first-cache rebuild failed; see rebuild-first.log")
   fr=read(firstdir/FIRST_NAMES["receipt"]);need(fr["status"]=="completed" and fr["all4367ConstantKernelProductsZero"] and
    fr["all1309ExactPrimitiveConstantCoefficientsVerified"] and fr["allOriginalParameterCoefficientsModulo31Verified"],"complete actual rebuilt natural first products")
   fc={"binding":firsttag,"inputIdentity":fm,"newFirstBinding":fr["parameters"]["binding"],
    "outputs":{name:ident(firstdir/name) for name in FIRST_NAMES.values()}}
   # The coefficient and field-array files are also useful to the subsequent Q task.
   for item in fr["parameters"]["temporaryFiles"]:fc["outputs"][item["file"]]={"bytes":item["bytes"],"sha256":item["sha256"]}
   save(firstcache,fc)
  fr=read(firstdir/FIRST_NAMES["receipt"]);need(fr["parameters"]["selectedFreeOriginalRows"]==free and
   fr["selectedNaturalFirstConnectionRankModulo31"]==fr["fullOutputSelectedFirstConnectionRankModulo31"]==3,"same actual rebuilt49/36 first ranks")
  S=imported("frozen_natural_schur",a.schur_runner);S.PIN=dict(S.PIN)
  for key,v in [("selected_model",selid),("unit_profile",profid)]:S.PIN[key]=(v["bytes"],v["sha256"])
  S.FIRST={k:(name,fc["outputs"][name]["bytes"],fc["outputs"][name]["sha256"]) for k,name in FIRST_NAMES.items()}
  S.FIRST_BINDING=fc["newFirstBinding"]
  oldsave=S.jsave
  reconstruction={"wrapperIdentity":wrapper,"historicalInputsVerified":True,"sameIAndJReconstructedFromOriginalRecords":True,
   "oldMathematicalEngineSHA256":ids["schur_runner"]["sha256"],"newFiniteFirstBinding":fc["newFirstBinding"],"oldPaidSchurBinding":OLD_BINDING,
   "gzipContainerBytesNotAssumedReproducible":True,"lostSessionFilesRecomputedRatherThanClaimedRestored":True}
  def compactsave(p,o):
   if pathlib.Path(p).name=="selected-natural-u-schur-pipeline-receipt.json":
    o=dict(o)
    if isinstance(o.get("nativeStatistics"),dict):
     nr=dict(o["nativeStatistics"]);nr.pop("unitOriginalOutputIndices",None);o["nativeStatistics"]=nr
    par=dict(o.get("parameters",{}));par["minimalTemporaryReconstruction"]=reconstruction;o["parameters"]=par
   return oldsave(p,o)
  S.jsave=compactsave
  preseconds=time.monotonic()-start;remain=a.seconds-preseconds
  if remain<=2:raise BudgetExpired("shared mathematical clock before Schur engine; complete rebuilt first cache retained")
  rec["phase"]="actual-natural-u-source-schur";rec["parameters"]["rebuiltFirstBinding"]=fc["newFirstBinding"];rec["preSchurMathematicalSeconds"]=preseconds;checkpoint()
  args=["--native-model",str(a.native_model),"--point-model",str(a.point_model),"--selected-model",str(selected_path),
   "--unit-profile",str(profile_path),"--kernel36",str(a.kernel36),"--source-dag",str(a.source_dag),"--repo-notes",str(a.repo_notes),
   "--first-dir",str(firstdir),"--out",str(schurdir),"--maximum-degree",str(a.maximum_degree),"--seconds",str(remain),
   "--memory-mib",str(a.memory_mib),"--compile-seconds",str(a.compile_seconds)]
  with (out/"natural-u-engine.log").open("a",encoding="utf-8") as log:
   with contextlib.redirect_stdout(log):sc=S.main(args)
  poststart=time.monotonic();sr=read(schurdir/"selected-natural-u-schur-pipeline-receipt.json")
  rec["parameters"]["actualNaturalEngineReceipt"]=ident(schurdir/"selected-natural-u-schur-pipeline-receipt.json")
  rec["parameters"]["actualNaturalStageStatus"]=sr.get("status");rec["parameters"]["actualCompletedNaturalDegree"]=sr.get("completedNaturalDegree",sr.get("parameters",{}).get("actualLastCompleteNativeDegree"))
  need(sc in (0,75),"actual natural-u engine arithmetic/input failure; see retained engine receipt")
  newbinding=sr["parameters"]["binding"];n=int(sr["parameters"]["actualLastCompleteNativeDegree"])
  need(newbinding!=OLD_BINDING,"new actual rebuilt input bytes have a distinct explicit binding")
  oldfiles={x["file"]:x for x in par16["temporaryFiles"]};compared=[]
  for k in range(min(n,16)+1):
   for kind,magic,rows in [("source",b"R150US31",6188),("schur",b"R150UJ31",36),("residual",b"R150UR31",4367)]:
    name="natural-%s-%d.bin"%(kind,k);b=(schurdir/name).read_bytes();oldfile=oldfiles[name]
    need(len(b)==88+rows*36 and b[:8]==magic and b[24:88].decode()==newbinding,"complete actual rebuilt jet header and extent")
    normalized=b[:24]+OLD_BINDING.encode()+b[88:]
    need(digest(normalized)=={"bytes":oldfile["bytes"],"sha256":oldfile["sha256"]},"all original coefficients equal paid16: "+name)
    compared.append({"file":name,"paidHeaderNormalizedSHA256":oldfile["sha256"]})
  need(len(compared)==3*(min(n,16)+1),"all available paid-prefix coefficient files verified")
  rec["parameters"].update(newSchurBinding=newbinding,oldPaidSchurBinding=OLD_BINDING,
   headerNormalizationChangesOnly64ByteBinding=True,paidPrefixComparison=compared,
   smallSeriesSmith=sr["parameters"].get("smallSeriesSmith"),nativeSummary=sr["parameters"].get("nativeSummary"),
   originalEngineSources=sr["parameters"]["inputIdentity"]["sources"])
  for k in ["all33CompleteOriginalFirstCorrectionsVerified","all4367FirstCorrectedProductsZero","completedNaturalDegree",
   "all4354SelectedJetIdentitiesVerified","all4367OriginalResidualCoordinatesRetained","all36FreeSourceCoordinatesVerified",
   "sameSelectedSourceSupportVerified","completeSelectedInfinitySmithLengthComputed","selectedMinorInfinityOrderModulo31",
   "selectedMinorInfinityOrderModulo31LowerBound"]:
   if k in sr:rec[k]=sr[k]
  rec["all51PaidPrefixFilesCoefficientIdentitiesVerified"]=n>=16
  rec["allSeventeenPaidSmallSchurCoefficientsVerified"]=n>=16
  rec["actualVerifiedPaidPrefixMaximumDegree"]=min(n,16)
  rec["mathematicalElapsedSeconds"]=preseconds+sr["mathematicalElapsedSeconds"]+(time.monotonic()-poststart)
  rec["compile"]=sr.get("compile",{})
  rec.update(status="completed" if sc==0 and n==a.maximum_degree else "checkpointed-time-budget",phase="complete")
  code=0 if rec["status"]=="completed" else 75
 except BudgetExpired as e:
  rec.update(status="checkpointed-time-budget",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed-or-incomplete",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  rec["parameters"]["temporaryStateLocations"]={"rebuiltInputs":"rebuilt-inputs","rebuiltFirst":"rebuilt-first","naturalSourceJets":"natural-u","originalCompletedLayerManifest":"natural-u/complete-jet-checkpoint-files.json"}
  checkpoint()
 need((out/"selected-natural-u-minimal-rebuild-receipt.json").stat().st_size<100000,"small permanent rebuild receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
