#!/usr/bin/env python3
"""Exact B-only row-content profile after paid column normalization.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Only profiles true seven-column denominator clearing; performs no new solve/pivot.
"""
import argparse,gzip,hashlib,json,math,os,pathlib,resource,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
S_BYTES=80674893
S_SHA="54288bdab2af917695df1a9e2e681cafffaee435ef0fcc86d766f058324d94ba"
S_BINDING="044ea5d75d28042c53c2db1896ec186173b6b320e598cc35208d761f48dbdad0"
C_BYTES=109635
C_SHA="1b8ce16d22d6435ae3c61ec00a4b7cd2a583bc17c1b93231e0011b3a3d3fab2e"
C_BINDING="63419ca6d607815ca50d4cf2ba0f6c74855339441e5da4289c1fca03fca7e8ed"
class BudgetExpired(Exception):pass
def need(v,s):
 if not v:raise ValueError(s)
def sha(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   z=f.read(1048576)
   if not z:break
   n+=len(z);h.update(z)
 return {"bytes":n,"sha256":h.hexdigest()}
def read(p):
 with gzip.open(p,"rt",encoding="utf-8") as f:return json.load(f)
def save(p,x):
 p=pathlib.Path(p);t=p.with_name(p.name+".tmp")
 with (gzip.open(t,"wt",encoding="utf-8",compresslevel=1) if p.suffix==".gz" else t.open("w")) as f:json.dump(x,f,separators=(",",":"))
 os.replace(t,p);return {"file":p.name,**sha(p),"temporaryOnly":True}
def native_environment():
 start=time.monotonic();info={}
 try:
  import flint
  module=pathlib.Path(flint.__file__).resolve();site=module.parent.parent
  info["pythonFlintModule"]=str(module)
  info["flintVersions"]={k:str(getattr(flint,k)) for k in ("__version__","__FLINT_VERSION__","__FLINT_RELEASE__") if hasattr(flint,k)}
  commands=[("pkgConfigVersion",["pkg-config","--modversion","flint"]),
    ("pkgConfigFlags",["pkg-config","--cflags","--libs","flint"]),
    ("wheelHeaderAndLibraryPaths",["rg","--files",str(site),"-g","flint.h","-g","fmpz_mat.h","-g","nmod_mat.h","-g","*flint*.so*"]),
    ("systemFlintLibraries",["ldconfig","-p"])]
  for key,cmd in commands:
   try:
    p=subprocess.run(cmd,capture_output=True,text=True,timeout=4)
    output=p.stdout
    if key=="systemFlintLibraries":output="\n".join(x for x in output.splitlines() if "flint" in x.lower())
    info[key]={"exitCode":p.returncode,"stdout":output[:6000],"stderr":p.stderr[:1000]}
   except Exception as e:info[key]={"error":type(e).__name__+": "+str(e)[:300]}
  info["standardHeaders"]={str(p):p.is_file() for p in
    [pathlib.Path("/usr/include/flint/flint.h"),pathlib.Path("/usr/local/include/flint/flint.h"),
     pathlib.Path("/usr/include/flint/fmpz_mat.h"),pathlib.Path("/usr/local/include/flint/fmpz_mat.h")]}
 except Exception as e:info["error"]=type(e).__name__+": "+str(e)[:300]
 return info,time.monotonic()-start
def main(argv):
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ["state","columns","out"]:ap.add_argument("--"+k,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=30);ap.add_argument("--memory-mib",type=int,default=2048)
 ap.add_argument("--denominator-bit-gate",type=int,default=65536)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 0<a.seconds<=60 and 0<a.memory_mib<=4096,"bounded exact scaling profile")
 need(1<=a.denominator_bit_gate<=1000000,"explicit denominator gate")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 native_info,native_seconds=native_environment()
 start=time.monotonic();deadline=start+a.seconds-min(2,a.seconds/10)
 out=a.out.resolve();need(not out.exists() or not any(out.iterdir()),"fresh row-scale output");out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-seven-exact-row-and-column-scale-profile-v1","status":"running",
  "newPivotsPerformed":0,"newRationalSolvePerformed":False,"originalStateUnchanged":True,
  "largeDataUploadedOrCommitted":False,"events":[],"parameters":{
     "secondsLimit":a.seconds,"memoryMiB":a.memory_mib,"denominatorBitGate":a.denominator_bit_gate,
     "nativeEnvironment":native_info,"nativeEnvironmentElapsedSeconds":native_seconds}}
 code=1;temps=[]
 def check():
  if time.monotonic()>=deadline:raise BudgetExpired("actual scale-profile deadline")
 try:
  need(sha(a.state)=={"bytes":S_BYTES,"sha256":S_SHA},"same paid2751 state")
  need(sha(a.columns)=={"bytes":C_BYTES,"sha256":C_SHA},"same fully verified column contents")
  cs=read(a.columns);st=read(a.state)
  need(st["binding"]==S_BINDING and cs["binding"]==C_BINDING and cs["inputBinding"]==S_BINDING,"paid source/column bindings")
  need(cs["all424921EntriesExactlyDivisible"] and len(st["reverseSubstitutionDAG"])==1567,"full actual source invariants")
  active=set(map(int,st["remainingSourceColumnPositions"]));source=st["sourceOriginalRows4325"]
  h={int(j):int(v) for j,v in cs["columnPositionsAndPositiveContents"]}
  need(set(h)==active and len(h)==2751 and all(v>0 for v in h.values()),"complete positive column scale")
  rawrows=st.pop("rows");del st["reverseSubstitutionDAG"];st.pop("initialRowContentDivisors",None)
  material={"codeSHA256":sha(__file__)["sha256"],"state":{"bytes":S_BYTES,"sha256":S_SHA},
       "columnContents":{"bytes":C_BYTES,"sha256":C_SHA},"sourceBinding":S_BINDING,"columnBinding":C_BINDING}
  binding=hashlib.sha256(json.dumps(material,sort_keys=True,separators=(",",":")).encode()).hexdigest()
  scales=[];erows=[];D=[1]*7;Dexact=[True]*7;nnz=0;amx=0;asum=0;rmax=0;nonunit=0;verify=0
  for z,r in enumerate(rawrows):
   i=int(r["originalOutputRow"]);terms=r.pop("coefficients");vals=[];g=0
   for j,vv in terms:
    j=int(j);v=int(vv);need(v%h[j]==0,"paid column division exact");v//=h[j];vals.append((j,v));g=math.gcd(g,abs(v))
   need(g>0,"positive nonzero B-only row content")
   scales.append([i,str(g)]);rmax=max(rmax,g.bit_length());nonunit+=g!=1
   for j,v in vals:
    need(v%g==0,"B-only row content divides every coefficient");b=abs(v//g).bit_length();amx=max(amx,b);asum+=b;verify+=1
   ee=list(map(int,r["rightHandSideSeven"]));need(len(ee)==7,"all seven RHS")
   erows.append((i,g,ee));nnz+=len(vals)
   for t,e in enumerate(ee):
    if Dexact[t]:
     d=g//math.gcd(g,abs(e));D[t]=math.lcm(D[t],d)
     if D[t].bit_length()>a.denominator_bit_gate:Dexact[t]=False
   if z%32==0:check()
  del rawrows
  need(nnz==verify==424921 and len(scales)==2751,"all actual rows/entries profiled")
  rhsmax=None
  if all(Dexact):
   rhsmax=0
   for z,(i,g,ee) in enumerate(erows):
    for t,e in enumerate(ee):
     num=D[t]*e;need(num%g==0,"each actual seven-column RHS denominator clears")
     rhsmax=max(rhsmax,abs(num//g).bit_length())
    if z%64==0:check()
  data={"format":"isp-seven-exact-two-sided-scales-v1","binding":binding,"sourceBinding":S_BINDING,
    "inputIdentity":material,"sourceOriginalRows4325":source,
    "columnPositionsAndPositiveContents":[[j,str(h[j])] for j in sorted(h)],
    "originalOutputRowsAndPositiveContents":scales,
    "rightHandSideColumnDenominators":[str(v) for v in D],"denominatorsExact":Dexact,
    "all424921CoefficientDivisionsExact":True,
    "identity":"U=R*Ubalanced*C; W=C*X*diag(D); Ubalanced*W=R^-1*E*diag(D); restore X=C^-1*W*diag(D)^-1 before inherited DAG",
    "allSevenRHSDenominatorsCleared":all(Dexact),
    "incompleteDenominatorMeansOnlyDivisorLowerBound":True}
  temps.append(save(out/"seven-exact-row-column-scale-factors.json.gz",data))
  rec.update({"status":"completed","actualUnitSize":2751,"actualNonzeroEntries":nnz,
    "nonunitBOnlyRowContentsAfterPaidColumns":nonunit,"maximumBOnlyRowContentBits":rmax,
    "balancedIntegerMatrixMaximumBits":amx,"balancedIntegerMatrixSumBits":asum,
    "sevenCommonRHSColumnDenominatorBits":[v.bit_length() for v in D],
    "sevenCommonRHSColumnDenominatorsExact":Dexact,
    "balancedIntegerRHSMaximumBits":rhsmax,
    "all424921CoefficientDivisionsExact":True,"allSevenRHSDenominatorsCleared":all(Dexact)})
  rec["parameters"].update({"binding":binding,"inputIdentity":material,
    "sevenCommonRHSColumnDenominatorBits":rec["sevenCommonRHSColumnDenominatorBits"],
    "sevenCommonRHSColumnDenominatorsExact":Dexact})
  code=0
 except BudgetExpired as e:rec.update(status="budget-exhausted",error=str(e));code=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__);(out/"exception.log").write_text(traceback.format_exc());code=1
 finally:
  rec["parameters"]["temporaryFiles"]=temps;rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  save(out/"seven-exact-row-content-profile-receipt.json",rec)
 need((out/"seven-exact-row-content-profile-receipt.json").stat().st_size<100000,"small persistent receipt")
 print(json.dumps(rec),flush=True);return code
if __name__=="__main__":sys.exit(main(sys.argv[1:]))
