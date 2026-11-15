#!/usr/bin/env python3
"""Same original deleted13-output projection of the complete formal left kernel.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
All recomputable arrays remain temporary; only source/parameters/run/hashes persist.
"""
import argparse,hashlib,itertools,json,math,os,pathlib,resource,shutil,signal,struct,subprocess,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for key in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[key]="1"
P=31
PARENT_BINDING="3e51cbe960ac668c9addb12be36856d2aaf13686f5acc15571317ccf3dd7d2ad"
PARENT_RECEIPT=(21358,"540fd2d44e7d49f9d4284d8966e9994397320f145e353c1560c7807f76caf9b4")
PIN={
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "selected_receipt":(75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "original_native_source":(21017,"82ce435444ea112e78d842a7975df4a6b6103f6ea0bf03efc73f58631985d6f9"),
 "extension_native_source":(21017,"54631a695dbd6dc41c446c8c3ab60ba527c5dd4f34fbe70187cdd0613caef1fb")}
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":(11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":(3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
RAW={
 "forward.bin":(2378937,"66ab292e67681fa17d286fee516d830fa25017138e354f82dbb9c33e7f50976e"),
 "backward.bin":(3052119,"cb396444652183924167e9cacaae888125c0e758e639af92b9784f7d1534132f"),
 "full_operations.bin":(8548344,"d2555a117c9f79db448e8eb183d5420952fe001707f5ca81e20e98705b83a3ad")}
PAID_EXP=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
class BudgetExpired(Exception):pass
def need(x,msg):
 if not x:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(pathlib.Path(p).read_text())
def save(p,obj):
 p=pathlib.Path(p);q=p.with_name(p.name+".partial")
 q.write_bytes(canonical(obj)+b"\n");os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def checked(p,pin):
 b=pathlib.Path(p).read_bytes()
 need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+str(p))
 return b
def sub(M,ri,ci):
 from flint import nmod_mat
 return nmod_mat(len(ri),len(ci),[int(M[i,j]) for i in ri for j in ci],P)
def zmat(n,m):
 from flint import nmod_mat
 return nmod_mat(n,m,[0]*(n*m),P)
def eye(n):
 from flint import nmod_mat
 return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],P)
def zero(M):return not any(M.entries())
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def pivots(M):
 R,r=M.rref();r=int(r)
 pp=[next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
 need(pp==sorted(set(pp)),"strict field pivot order")
 return pp
def field_read(p,magic,degree,nr,nc,binding,expected=None):
 b=pathlib.Path(p).read_bytes()
 if expected is not None:need(hashlib.sha256(b).hexdigest()==expected,"complete inherited field SHA256")
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(P,degree,nr,nc)
      and b[24:88].decode()==binding and len(b)==88+nr*nc
      and all(v<P for v in b[88:]),"same bound original field coordinates")
 return b[88:]
def field_write(p,magic,degree,M,binding):
 nr,nc=M.nrows(),M.ncols();body=bytes(int(x) for x in M.entries())
 b=magic+struct.pack("<IIII",P,degree,nr,nc)+binding.encode()+body
 need(len(magic)==8 and len(b)==88+nr*nc,"complete output field extent")
 q=p.with_name(p.name+".partial");q.write_bytes(b);os.replace(q,p)
 return {"file":p.name,**digest(b),"rows":nr,"columns":nc,"degree":degree,"temporaryOnly":True}
def inverse_series(U,check):
 inv=[U[0].inv()];n=U[0].nrows()
 for k in range(1,len(U)):
  check();v=zmat(n,n)
  for j in range(1,k+1):v+=U[j]*inv[k-j]
  inv.append(-inv[0]*v)
 for k in range(len(U)):
  check();v=zmat(n,n)
  for j in range(k+1):v+=U[j]*inv[k-j]
  need(v==(eye(n) if k==0 else zmat(n,n)),"all coefficients of real unit inverse")
 return inv
def mul_series(A,B,count,check):
 result=[]
 for k in range(count):
  check();v=zmat(A[0].nrows(),B[0].ncols())
  for j in range(max(0,k-len(B)+1),min(k,len(A)-1)+1):v+=A[j]*B[k-j]
  result.append(v)
 return result
def solve_regular_square(A,B,check,steps,height=0):
 """Solve A X+B=0 by actual unit blocks, retaining the honest loss of precision."""
 n=A[0].nrows();precision=len(A)-1
 need(n==A[0].ncols() and len(B)==len(A) and B[0].nrows()==n,
      "actual selected14 square equations")
 pc=pivots(A[0]);rank=len(pc)
 pr=pivots(sub(A[0],list(range(n)),pc).transpose()) if rank else []
 need(len(pr)==rank,"actual square unit row rank")
 steps.append({"uExponent":height,"rows":n,"rank":rank,"availableDegree":precision,"unitRows":pr,"unitColumns":pc})
 if not rank:
  need(zero(B[0]),"regular formal kernel requires every divided RHS constant zero")
  need(precision>0,"insufficient true source precision")
  return solve_regular_square(A[1:],B[1:],check,steps,height+1)
 ri=pr+[i for i in range(n) if i not in set(pr)]
 ci=pc+[i for i in range(n) if i not in set(pc)]
 U=[sub(M,ri[:rank],ci[:rank]) for M in A]
 rhs=[sub(M,ri[:rank],list(range(13))) for M in B]
 inv=inverse_series(U,check);rb=mul_series(inv,rhs,len(A),check)
 if rank==n:
  answer=[]
  for k in range(len(A)):
   x=zmat(n,13)
   for i in range(n):
    for j in range(13):x[ci[i],j]=-rb[k][i,j]
   answer.append(x)
  return answer,height
 V=[sub(M,ri[:rank],ci[rank:]) for M in A]
 W=[sub(M,ri[rank:],ci[:rank]) for M in A]
 Z=[sub(M,ri[rank:],ci[rank:]) for M in A]
 Q=[sub(M,ri[rank:],list(range(13))) for M in B]
 iv=mul_series(inv,V,len(A),check)
 wi=mul_series(W,inv,len(A),check)
 wiv=mul_series(wi,V,len(A),check)
 wir=mul_series(wi,rhs,len(A),check)
 SA=[Z[k]-wiv[k] for k in range(len(A))]
 SB=[Q[k]-wir[k] for k in range(len(A))]
 need(zero(SA[0]) and zero(SB[0]),"all constant Schur/RHS coordinates before exact u division")
 need(precision>0,"positive Schur factor needs another actual coefficient")
 tail,last=solve_regular_square(SA[1:],SB[1:],check,steps,height+1)
 answer=[]
 for k in range(len(tail)):
  check();top=-rb[k]
  for j in range(k+1):top-=iv[j]*tail[k-j]
  x=zmat(n,13)
  for i in range(rank):
   for j in range(13):x[ci[i],j]=top[i,j]
  for i in range(n-rank):
   for j in range(13):x[ci[rank+i],j]=tail[k][i,j]
  answer.append(x)
 return answer,last
def main(argv=None):
 ap=argparse.ArgumentParser()
 ap.add_argument("--full-out",required=True,type=pathlib.Path)
 ap.add_argument("--outside-out",required=True,type=pathlib.Path)
 ap.add_argument("--native-model",required=True,type=pathlib.Path)
 ap.add_argument("--selected-receipt",required=True,type=pathlib.Path)
 ap.add_argument("--original-native-source",required=True,type=pathlib.Path)
 ap.add_argument("--extension-native-source",required=True,type=pathlib.Path)
 ap.add_argument("--out",required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=180)
 ap.add_argument("--memory-mib",type=int,default=1024)
 ap.add_argument("--compile-seconds",type=float,default=30)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 10<=a.seconds<=600 and 1<=a.compile_seconds<=30
      and 512<=a.memory_mib<=2048,"explicit bounded original projection consumer")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024*1024,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True);full=a.full_out.resolve()
 rp=out/"full-kernel-deleted-output-projection-receipt.json";start=time.monotonic();files={};stop=[False];active=[None]
 rec={"format":"isp-full-natural-kernel-deleted13-output-projection-v1","status":"running","phase":"inputs",
  "field":31,"characteristicZeroOutputProjectionComputed":False,"selectedLeadingCoefficientUnitProved":False,
  "largeDataUploadedOrCommitted":False,"newLargeGaussianEliminations":0,"oldNormalFormsRecomputed":False,
  "parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib},"events":[]}
 def keep(p):
  p=pathlib.Path(p);q=str(p.relative_to(out)) if p.is_relative_to(out) else str(p.relative_to(full))
  files[(str(p.parent),p.name)]={"file":q,**identity(p),"temporaryOnly":True}
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=list(files.values());save(rp,rec)
 def check():
  if stop[0] or time.monotonic()-start>=a.seconds-3:raise BudgetExpired("shared consumer deadline; complete stages retained")
 def interrupt(signum,frame):
  stop[0]=True
  if active[0] is not None and active[0].poll() is None:active[0].terminate()
 signal.signal(signal.SIGTERM,interrupt);signal.signal(signal.SIGINT,interrupt)
 def beat(phase):
  rec["phase"]=phase;checkpoint()
  print(json.dumps({"phase":phase,"elapsedSeconds":rec["mathematicalElapsedSeconds"]}),flush=True)
 rc=1
 try:
  blobs={k:checked(getattr(a,k),pin) for k,pin in PIN.items()}
  parentpath=full/"full-infinity-natural-dual-schur-receipt.json"
  parent=json.loads(checked(parentpath,PARENT_RECEIPT))
  need(parent["status"]=="completed" and parent["outcome"]=="complete-full-original-infinity-field-smith"
       and parent["parameters"]["binding"]==PARENT_BINDING
       and parent["fullInfinityTorsionLengthModulo31"]==66
       and parent["fullInfinityMaximumPositiveExponentModulo31"]==11
       and parent["fullOriginalFreeCokernelRank"]==13,"paid complete original full spectrum")
  for key in ("all4433OriginalParameterCoefficientsVerified","all6188OriginalJetResidualCoordinatesRetained",
    "all4340OriginalUnitJetCancellationsVerified","all80444OriginalFormalKernelConstantProductsVerified"):
   need(parent[key] is True,"paid full original identity: "+key)
  outside_path=a.outside_out/"koszul-outside-minimal-field-smith-receipt.json"
  outside_pin=(15832,"eeddfe8782d06338d15d834bdf387de5cd2f85d8334415f59411d24bfca244a6")
  outside=json.loads(checked(outside_path,outside_pin))
  need(outside["status"]=="completed" and outside["completeOutsideSmithLengthComputed"]
       and outside["outsideTorsionLengthModulo31"]==149 and outside["outsidePositiveExponentCount"]==29
       and outside["all126643OriginalConstantSourceProductsZero"]
       and outside["parameters"]["inputIdentity"]["paidSelectedBinding"]==parent["parameters"]["inputIdentity"]["paidSelectedBinding"]
       and outside["parameters"]["inputIdentity"]["inputs"]["selected_receipt"]==digest(blobs["selected_receipt"]),
       "same selectedB and actual complete outside length149")
  smith=parent["parameters"]["smallSeriesSmith"]
  need(smith["paidExponents"]==PAID_EXP and smith["complete"] and smith["allRetainedFreeRemainderCoefficientsZero"],
       "paid original14 positive indices and formal13")
  pc=smith["selectedOriginalHeadColumns"];pr=smith["selectedOriginalSchurRows"];fc=smith["freeOriginalHeadColumns"]
  need(len(pc)==len(pr)==14 and len(fc)==13 and sorted(pc+fc)==list(range(27)),"actual original14/13 mapper dictionary")
  inherited={x["file"]:x for x in parent["parameters"]["temporaryFiles"]}
  def inherited_read(name):
   p=full/name;x=inherited[name];b=p.read_bytes()
   need(digest(b)=={"bytes":x["bytes"],"sha256":x["sha256"]},"complete inherited original file: "+name)
   return b
  recipe=json.loads(inherited_read("full13-original-formal-kernel-mapper.json"))
  need(recipe["binding"]==PARENT_BINDING and recipe["selectedHeadColumns"]==pc and recipe["freeHeadColumns"]==fc,
       "same complete original formal kernel recipe")
  freeout=list(map(int,recipe["freeOriginalOutputs"]));unitout=list(map(int,recipe["unitOriginalOutputs"]))
  unitsource=list(map(int,recipe["unitOriginalSources"]));tailsource=list(map(int,recipe["tailOriginalSources"]))
  need(len(freeout)==27 and len(unitout)==len(unitsource)==4340 and len(tailsource)==1848
       and sorted(freeout+unitout)==list(range(4367))
       and sorted(unitsource+tailsource)==list(range(1,6189)),"whole original output/source dictionary partitions")
  needle=b"maximum>=1&&maximum<=21&&std::isfinite(limit)"
  need(blobs["original_native_source"].count(needle)==1
       and blobs["extension_native_source"]==blobs["original_native_source"].replace(
        needle,b"maximum>=1&&maximum<=39&&std::isfinite(limit)"),
       "only native inclusive degree guard changed; no mathematical or checkpoint code changed")
  header_ids={}
  for name,pin in HEADERS.items():
   b=checked(a.extension_native_source.parent/name,pin);header_ids[name]=digest(b)
  for name,pin in RAW.items():checked(full/"prepared"/name,pin)
  need(digest(inherited_read("prepared/full-original-constant-profile.txt"))==
       identity(full/"prepared"/"full-original-constant-profile.txt"),"same original profile bytes")
  tok=iter(blobs["native_model"].decode().split())
  need(next(tok)=="R150_NATIVE_NF_V1","complete native source model")
  def take(n):return [next(tok) for _ in range(n)]
  take(11*(66+121));need(int(next(tok))==3333,"all original prebasis records")
  pre=[list(map(int,take(4))) for _ in range(3333)]
  take(6*66*6);need(list(map(int,take(2)))==[2195,9],"whole native source/target counts")
  take(2195*3);need(list(map(int,take(9)))==list(range(2,11)) and next(tok,None) is None,"complete native model tail")
  var=[8**i for i in range(11)]
  mons=[sum(var[i] for i in q) for d in range(5,0,-1) for q in itertools.combinations_with_replacement(range(11),d)]
  mindex={m:i for i,m in enumerate(mons)}
  multipliers=[sum(var[i] for i in q) for d in range(4) for q in itertools.combinations_with_replacement(range(11),d)]
  need(len(mons)==4367 and len(mindex)==4367,"full original output monomial dictionary")
  for e,m,p,r in pre:
   need(1<=r<=6188 and e==(r-1)%17 and m==multipliers[(r-1)//17] and p in mindex,"original prebasis source/output dictionary")
  preout={mindex[x[2]] for x in pre};components=[i for i in range(4367) if i not in preout]
  selected=json.loads(blobs["selected_receipt"])
  need(selected["status"]=="completed" and selected["selectedOriginalMinorRetained"]
       and selected["allOriginalSourceIdentitiesVerified"],"paid same original selected matrix")
  comps=list(map(int,selected["selectedOutputComponents"]))
  need(len(preout)==3333 and len(components)==1034 and len(comps)==len(set(comps))==1021,
       "same original3333 plus1021 selected outputs")
  need([mons[components[c-1]] for c in comps]==list(map(int,selected["selectedOutputMonomialKeys"])),
       "every selected original output monomial key")
  I=sorted(preout|{components[c-1] for c in comps});Ic=sorted(set(range(4367))-set(I))
  need(len(I)==4354 and len(Ic)==13 and
       Ic==[components[int(c)-1] for c in selected["excluded13OutputComponents"]],
       "same thirteen deleted original outputs, not arbitrary full free outputs")
  need(set(Ic)<=set(freeout),"all deleted outputs belong to the paid27 original free coordinates")
  ih=[freeout.index(i) for i in Ic]
  common=set(ih)&set(fc);missing=list(set(fc)-set(ih));extra=list(set(ih)-set(fc))
  need(len(common)==12 and missing==[15] and extra==[22]
       and ih==[4,5,9,10,13,14,16,17,22,23,24,25,26],
       "actual one-row replacement in original free13 chart")
  material={"version":"same-original-deleted13-field-projection-v1","source":identity(__file__),
    "parentMathematicalBinding":PARENT_BINDING,"parentReceipt":{"bytes":PARENT_RECEIPT[0],"sha256":PARENT_RECEIPT[1]},
    "actualOutsideReceipt":{"bytes":outside_pin[0],"sha256":outside_pin[1]},
    "inputs":{k:digest(v) for k,v in blobs.items()},"headers":header_ids,
    "paidFullLength31":66,"paidOutsideLength31":149,"paidSelectedLength31":243,
    "remainingProjectionAndHigherKernelLength":28,"maximumContinuationDegree":39,
    "originalDeletedOutputIndices":Ic,"originalDeletedHeadCoordinates":ih}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"parentMathematicalBinding":PARENT_BINDING,
    "originalSelectedOutputCount":len(I),"originalSelectedOutputIndicesSHA256":hashlib.sha256(canonical(I)).hexdigest(),
    "deletedOriginalOutputIndicesZeroBased":Ic,
    "deletedOriginalOutputMonomialKeys":[mons[i] for i in Ic],
    "deletedHeadCoordinates":ih,"formalFreeHeadCoordinates":fc,"commonUnitRows":12,
    "omittedFreeHead":15,"insertedHead":22,"selectedSchurRows":pr,"selectedSchurColumns":pc,
    "continuationChangesOnlyInclusiveDegreeGuard":True,"maximumSourceDegreeIfNeeded":39,
    "maximumInversePoleOrder":11,"projectionLengthUpperBoundModulo31":28,
    "inputFiles":[{"role":k,**digest(v)} for k,v in blobs.items()]})
  rec["sameThirteenOriginalDeletedOutputsVerified"]=True
  rec["allTwelveCommonFreeRowsVerified"]=True
  plan=out/"compatible-native-continuation-plan.json"
  if plan.exists():need(read(plan)==material,"same consumer source/input continuation binding")
  else:save(plan,material)
  keep(plan)
  from flint import nmod_mat
  import flint
  rec["pythonFlintVersion"]=flint.__version__
  def load_layers():
   lp=full/"full-dual-ledger.txt";lt=lp.read_text().split()
   need(lt[:2]==["R15FDJLEDGER1",PARENT_BINDING],"same complete old mathematical ledger")
   degree=int(lt[2]);need(21<=degree<=39 and len(lt)==3+3*(degree+1),"complete contiguous original layers")
   L=[];S=[]
   for d in range(degree+1):
    check();data={}
    for key,magic,nr,ix in (("cochain",b"R15FDL31",4367,0),("residual",b"R15FDR31",6188,1),("schur",b"R15FDS31",1848,2)):
     name="full-dual-"+key+"-"+str(d)+".bin";fp=full/name
     bb=field_read(fp,magic,d,nr,27,PARENT_BINDING,lt[3+3*d+ix]);data[key]=bb
     if d<=21:
      expected=inherited[name]
      need(identity(fp)=={"bytes":expected["bytes"],"sha256":expected["sha256"]},
           "all66 original completed prefix files remain byte identical")
    lb,rb,sb=data["cochain"],data["residual"],data["schur"]
    for i,raw in enumerate(freeout):
     need(lb[raw*27:(raw+1)*27]==bytes(int(d==0 and i==j) for j in range(27)),
          "all27 full free coordinates at every actual source degree")
    for raw in unitsource:need(not any(rb[(raw-1)*27:raw*27]),"all4340 original unit residual rows remain zero")
    need(b"".join(rb[(raw-1)*27:raw*27] for raw in tailsource)==sb,
         "all1848 small rows equal the same full6188 original residual")
    L.append(nmod_mat(4367,27,list(lb),P));S.append(nmod_mat(1848,27,list(sb),P))
   rec["parameters"]["actualNativeDegree"]=degree
   rec["parameters"]["actualNativeLedger"]={"file":"full-dual-ledger.txt",**identity(lp)}
   rec["all66PaidOriginalPrefixFilesUnchanged"]=True
   rec["allFullOriginalResidualRowsRetained"]=True
   return degree,L,S
  def mapper(S):
   check();AA=[sub(M,pr,pc) for M in S];BB=[sub(M,pr,fc) for M in S];steps=[]
   X,last=solve_regular_square(AA,BB,check,steps)
   paid=[s["uExponent"] for s in steps for _ in range(s["rank"])]
   need(paid==PAID_EXP and last==11 and len(X)==len(S)-11,
        "actual original14 square has complete paid Smith spectrum and exact11 precision loss")
   Ns=[]
   for k,x in enumerate(X):
    m=zmat(27,13)
    for i in range(14):
     for j in range(13):m[pc[i],j]=x[i,j]
    if k==0:
     for j in range(13):m[fc[j],j]=1
    Ns.append(m)
   need(rows(Ns[0])==recipe["constantMapper"],"whole actual constant mapper unchanged")
   for k in range(len(Ns)):
    check();v=zmat(1848,13)
    for j in range(k+1):v+=S[j]*Ns[k-j]
    need(zero(v),"all1848 original tail-source equations for each formal mapper coefficient")
   rec["parameters"]["smallSquareSteps"]=steps
   rec["parameters"]["verifiedMapperMaximumDegree"]=len(Ns)-1
   rec["parameters"]["allOriginalProductCoordinates"]=6188*13*len(Ns)
   rec["all6188OriginalFormalKernelProductsVerifiedThroughRetainedDegree"]=True
   return Ns
  def projection(Ns):
   G=[sub(M,ih,list(range(13))) for M in Ns];rr=ih.index(22);cc=fc.index(15)
   for k,M in enumerate(G):
    for i,h in enumerate(ih):
     if h in common:
      need([int(M[i,j]) for j in range(13)]==[int(k==0 and fc[j]==h) for j in range(13)],
           "all twelve common original free rows are exact constant units")
   co=int(sub(G[0],[i for i in range(13) if i!=rr],[j for j in range(13) if j!=cc]).det())
   sign=co*(1 if (rr+cc)%2==0 else -1)%31
   need(sign in (1,30),"exact one-row determinant cofactor sign")
   scalar=[int(N[22,cc]) for N in Ns];det=[sign*x%31 for x in scalar]
   first=next((k for k,x in enumerate(det) if x),None)
   rec["parameters"].update({"determinantCofactorSignModulo31":sign,
     "scalarMapperRow":22,"scalarFreeHead":15,"scalarFreeColumnPosition":cc,
     "scalarCoefficientsModulo31":scalar,"determinantCoefficientsModulo31":det})
   return G,first
  beat("read-paid-original-series-and-construct-kernel")
  degree,L,S=load_layers();Ns=mapper(S);G,order=projection(Ns)
  if order is None and len(Ns)-1<28:
   rec["events"].append({"existing21DegreePrefixMapperVerified":True,
     "knownProjectionZeroThroughDegree":len(Ns)-1,"additionalNativeDegreesNeeded":39-degree})
   beat("continue-only-missing-natural-dual-degrees")
   build=out/"native-build";build.mkdir(exist_ok=True)
   for name in HEADERS:shutil.copyfile(a.extension_native_source.parent/name,build/name)
   ns=build/a.extension_native_source.name
   if ns.exists():need(identity(ns)==digest(blobs["extension_native_source"]),"same continuation native source")
   else:ns.write_bytes(blobs["extension_native_source"])
   exe=build/"full-dual-through39";cp=build/"compile-cache.json"
   cb=hashlib.sha256(canonical({"source":digest(blobs["extension_native_source"]),"headers":header_ids,
     "flags":["g++","-std=c++17","-O2"]})).hexdigest()
   cache=read(cp) if cp.exists() else {}
   if exe.exists() and cache.get("binding")==cb and cache.get("binary")==identity(exe):
    rec["compileElapsedSeconds"]=0.0
   else:
    check();t=time.monotonic();lp=build/"compile.log"
    with lp.open("wb") as f:
     c=subprocess.run(["g++","-std=c++17","-O2",str(ns),"-o",str(exe)],cwd=build,
       stdout=f,stderr=subprocess.STDOUT,timeout=min(a.compile_seconds,max(.1,a.seconds-(time.monotonic()-start)-5)))
    rec["compileElapsedSeconds"]=time.monotonic()-t;keep(lp)
    if c.returncode:
     rec["compileLogTail"]=lp.read_text(errors="replace")[-4000:];raise ValueError("actual degree-only extension compilation failed")
    save(cp,{"binding":cb,"binary":identity(exe)})
   keep(cp)
   log=out/"continuation-native.log";remaining=max(.1,a.seconds-(time.monotonic()-start)-10)
   cmd=[str(exe),str(a.native_model.resolve()),str(full/"prepared"/"full-original-constant-profile.txt"),
     str(full/"prepared"/"forward.bin"),str(full/"prepared"/"backward.bin"),
     str(full/"prepared"/"full_operations.bin"),str(full/"full-dual"),"39",str(remaining)]
   t=time.monotonic()
   with log.open("ab") as f:
    proc=subprocess.Popen(cmd,stdout=f,stderr=subprocess.STDOUT);active[0]=proc
    try:ret=proc.wait(timeout=max(.1,a.seconds-(time.monotonic()-start)-4))
    except subprocess.TimeoutExpired:
     proc.terminate()
     try:ret=proc.wait(timeout=10)
     except subprocess.TimeoutExpired:proc.kill();ret=proc.wait()
     raise BudgetExpired("native retained its last complete original layer")
   active[0]=None;rec["nativeExecutionSeconds"]=time.monotonic()-t;rec["nativeExitCode"]=ret;keep(log)
   if ret not in (0,75):
    rec["nativeLogTail"]=log.read_text(errors="replace")[-4000:]
    raise ValueError("actual original natural continuation failed")
   nr=read(full/"full-dual-receipt.json")
   need(nr["inputBinding"]==PARENT_BINDING and nr["restoredCompletedDegree"]==degree,
        "native restored all and only old completed source degrees")
   rec["parameters"]["continuationNativeSummary"]={k:v for k,v in nr.items() if k not in
     ("unitOriginalOutputIndicesZeroBased","unitOriginalSourceRowsOneBased","tailOriginalSourceRowsOneBased")}
   degree,L,S=load_layers();Ns=mapper(S);G,order=projection(Ns)
   if ret==75 and order is None:raise BudgetExpired("additional complete source layers retained")
  if order is None:
   need(len(Ns)-1<28,"projection must be nonzero by the proved complete remaining length28")
   rec.update(status="completed-prefix",outcome="checkpointed-deleted-output-projection",unresolvedProjectionOrderAtLeast=len(Ns));rc=75
  else:
   need(0<=order<=28,"actual output-projection length lies in complete remaining28")
   beat("save-complete-original-formal-kernel-and-projection")
   kstage=out/"original-kernel-layer-ledger.json"
   old=read(kstage) if kstage.exists() else {"binding":binding,"layers":[]}
   need(old["binding"]==binding,"same complete mapper output checkpoint")
   paidlayers={int(x["degree"]):x for x in old["layers"]};done=[]
   for k in range(len(Ns)):
    check()
    np=out/("formal-kernel-mapper-"+str(k)+".bin")
    gp=out/("deleted-original-output-projection-"+str(k)+".bin")
    kp=out/("original-formal-kernel-"+str(k)+".bin")
    if k in paidlayers:
     item=paidlayers[k]
     for key,p,magic,nr in (("mapper",np,b"R15PGN31",27),("projection",gp,b"R15PGG31",13),("originalKernel",kp,b"R15PGK31",4367)):
      need(identity(p)=={"bytes":item[key]["bytes"],"sha256":item[key]["sha256"]},"same completed original kernel layer")
      bb=field_read(p,magic,k,nr,13,binding,item[key]["sha256"])
      if key=="mapper":need(list(bb)==[int(x) for x in Ns[k].entries()],"saved whole mapper agrees with current exact series")
      if key=="projection":need(list(bb)==[int(x) for x in G[k].entries()],"saved actual deleted-row series")
    else:
     K=zmat(4367,13)
     for j in range(k+1):K+=L[j]*Ns[k-j]
     need(sub(K,Ic,list(range(13)))==G[k],"actual original4367 kernel projects to the selected deleted13 rows")
     need(sub(K,[freeout[j] for j in fc],list(range(13)))==(eye(13) if k==0 else zmat(13,13)),
          "all13 original formal free coordinates form a unit at every computed degree")
     item={"degree":k,
      "mapper":field_write(np,b"R15PGN31",k,Ns[k],binding),
      "projection":field_write(gp,b"R15PGG31",k,G[k],binding),
      "originalKernel":field_write(kp,b"R15PGK31",k,K,binding)}
    done.append(item)
    for p in (np,gp,kp):keep(p)
    save(kstage,{"binding":binding,"layers":done});keep(kstage)
   rec.update(status="completed",outcome="complete-original-deleted-output-projection",
     completeOutputProjectionSmithComputed=True,outputProjectionRank=13,
     outputProjectionTorsionLengthModulo31=order,
     outputProjectionMaximumPositiveExponentModulo31=order,
     outputProjectionUnitFactorCount=12+(1 if order==0 else 0),
     outputProjectionPositiveExponents=[] if order==0 else [order],
     remainingHigherKernelQuotientLengthModulo31=28-order,
     selectedOutputDeterminantalLengthModulo31=66+order,
     fullOriginalFormalKernelMaximumVerifiedDegree=len(Ns)-1,
     all13OriginalFormalFreeCoordinatesVerified=True,
     all4367OriginalKernelCoordinatesRetained=True,
     all13DeletedOriginalOutputRowsVerified=True,
     characteristicZeroOutputProjectionComputed=False,selectedLeadingCoefficientUnitProved=False)
   rec["parameters"]["exactFieldLengthDecomposition"]={"selectedMinor":243,"fullOriginalTorsion":66,
     "deletedOutputProjection":order,"outsideKoszulTorsion":149,"remainingHigherKernelQuotient":28-order}
   rc=0
 except (BudgetExpired,subprocess.TimeoutExpired) as e:
  rec.update(status="budget-exhausted",outcome="checkpointed-original-output-projection",error=str(e));rc=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  p=out/"exception.log";p.write_text(traceback.format_exc());keep(p);rc=1
 finally:
  checkpoint()
 need(rp.stat().st_size<100000,"only small execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
