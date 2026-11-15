#!/usr/bin/env python3
"""Two independent regular202 mappers for the same original high-kernel quotient.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
All large arrays remain job temporary. No characteristic-zero high value is asserted.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,struct,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[k]="1"
P=31
PIN={
 "native_model":(128145,"291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6"),
 "selected_receipt":(75700,"5cd9543de68bdb562bbe21189d5b0712248e6943c5572fe38ff27ec4fc1f5f68"),
 "paid_source_summary":(14075,"ba8bd267563e7cb24f49704c76d0f12a5226e2255d5a3b70ffa7249e90f6b484"),
 "source_native":(23360,"d0748649a3cd280fb620c85c61b82cb9d6c6fabeef8e9db81afaf9b9b01a4b2c"),
 "outside_native":(12826,"92e534d74d465f99043ec293bdd5a82a67c661309767e42e476bf765e1244262")}
HEADERS={
 "2026-11-15-r150-saturated-global-common-789f.hpp":(11284,"f19a9c64b7f57175b757d445594fb5521d1a7a9c5b0b0fe57391a407323c41e1"),
 "2026-11-14-r150-f31-bitplane-789f.hpp":(3030,"73d113f207c718b230162c786dfc8d367c5113193ed5fe590166af414c6fe8ec")}
PREP_BINDING="9744524d391dfd960e85bf6700b7d242f012017155059fab91d2aff1772fa337"
FULL_BINDING="9e86556a7a82c1c2306b395c87a49a7059d0945f12db7d4962c789717bd35dc6"
OUTSIDE_BINDING="f07acb3347e775dc41658f95e015c2e169b4df34c6c1e829a2737fe83acb2781"
FULL_EXP=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
OUTSIDE_EXP=[1,1]+[2]*10+[3]*3+[4]*3+[5,6,8,8,9,10,10,11,12,13,14]
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
def read(p):
 b=pathlib.Path(p).read_bytes();return json.loads(gzip.decompress(b) if b[:2]==b"\x1f\x8b" else b)
def save(p,x):
 q=p.with_name(p.name+".partial");q.write_bytes(canonical(x)+b"\n");os.replace(q,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def save_bytes(p,b):
 q=p.with_name(p.name+".partial");q.write_bytes(b);os.replace(q,p)
 return {"file":p.name,**digest(b),"temporaryOnly":True}
def checked(p,pin):
 b=pathlib.Path(p).read_bytes()
 need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+str(p));return b
def zmat(n,m):
 from flint import nmod_mat
 return nmod_mat(n,m,[0]*(n*m),P)
def eye(n):
 from flint import nmod_mat
 return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],P)
def sub(M,ri,ci):
 from flint import nmod_mat
 return nmod_mat(len(ri),len(ci),[int(M[i,j]) for i in ri for j in ci],P)
def zero(M):return not any(M.entries())
def pivots(M):
 R,r=M.rref();r=int(r)
 cols=[next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
 need(cols==sorted(set(cols)),"strict complete original field pivot order");return cols
def field_read(p,magic,k,nr,nc,binding,item):
 b=p.read_bytes()
 need(digest(b)=={"bytes":item["bytes"],"sha256":item["sha256"]},"complete actual field file: "+p.name)
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(P,k,nr,nc)
      and b[24:88].decode()==binding and len(b)==88+nr*nc and all(v<P for v in b[88:]),
      "complete canonical original field extent/binding")
 return b[88:]
def series_write(p,series,binding):
 nr,nc=series[0].nrows(),series[0].ncols()
 need(all(M.nrows()==nr and M.ncols()==nc for M in series),"complete mapper series shape")
 b=b"R15RKM31"+struct.pack("<IIII",P,len(series)-1,nr,nc)+binding.encode()
 b+=b"".join(bytes(int(x) for x in M.entries()) for M in series)
 return save_bytes(p,b)
def series_read(p,binding,nr,nc,maximum):
 from flint import nmod_mat
 b=p.read_bytes()
 need(b[:8]==b"R15RKM31" and struct.unpack_from("<IIII",b,8)==(P,maximum,nr,nc)
      and b[24:88].decode()==binding and len(b)==88+(maximum+1)*nr*nc
      and all(v<P for v in b[88:]),"complete regular mapper coefficients")
 return [nmod_mat(nr,nc,list(b[88+k*nr*nc:88+(k+1)*nr*nc]),P) for k in range(maximum+1)]
def mul(A,B,count,check):
 out=[]
 for k in range(count):
  check();v=zmat(A[0].nrows(),B[0].ncols())
  for j in range(max(0,k-len(B)+1),min(k,len(A)-1)+1):v+=A[j]*B[k-j]
  out.append(v)
 return out
def inverse_series(U,check):
 n=U[0].nrows();inv=[U[0].inv()]
 for k in range(1,len(U)):
  check();v=zmat(n,n)
  for j in range(1,k+1):v+=U[j]*inv[k-j]
  inv.append(-inv[0]*v)
 for k in range(len(U)):
  check();v=zmat(n,n)
  for j in range(k+1):v+=U[j]*inv[k-j]
  need(v==(eye(n) if k==0 else zmat(n,n)),"every actual unit inverse coefficient")
 return inv
def regular_kernel(series,expected_rank,expected_exponents,check):
 """Actual unit Schur plus original-coordinate back substitution, never an arbitrary fixed minor."""
 n0=series[0].ncols();m0=series[0].nrows();free=n0-expected_rank
 need(free==202 and all(M.nrows()==m0 and M.ncols()==n0 for M in series),"actual rectangular mapper shape")
 steps=[];paid=[]
 def recurse(A,remaining,labels,height):
  check();nr,nc=A[0].nrows(),A[0].ncols();precision=len(A)-1
  need(nc-remaining==free and len(labels)==nc,"complete active source coordinate count")
  pc=pivots(A[0]);rank=len(pc);need(rank<=remaining,"actual rank respects paid full generic bound")
  pr=pivots(sub(A[0],list(range(nr)),pc).transpose()) if rank else []
  need(len(pr)==rank,"actual rectangular constant unit")
  prs,pcs=set(pr),set(pc);ri=pr+[i for i in range(nr) if i not in prs];ci=pc+[j for j in range(nc) if j not in pcs]
  steps.append({"exponent":height,"rows":nr,"columns":nc,"availableDegree":precision,"constantRank":rank,
    "unitRows":pr,"unitOriginalColumns":[labels[j] for j in pc]})
  paid.extend([height]*rank)
  if rank==0:
   need(zero(A[0]),"whole constant matrix zero before division")
   if remaining==0:
    need(all(zero(M) for M in A),"all retained free formal residual coefficients zero")
    return [eye(free) if k==0 else zmat(free,free) for k in range(len(A))],labels,height
   need(precision>0,"insufficient actual input precision for next positive factor")
   return recurse(A[1:],remaining,labels,height+1)
  U=[sub(M,ri[:rank],ci[:rank]) for M in A]
  V=[sub(M,ri[:rank],ci[rank:]) for M in A]
  IV=mul(inverse_series(U,check),V,len(A),check)
  if nr>rank:
   W=[sub(M,ri[rank:],ci[:rank]) for M in A]
   Z=[sub(M,ri[rank:],ci[rank:]) for M in A]
   WIV=mul(W,IV,len(A),check)
   S=[Z[k]-WIV[k] for k in range(len(A))]
  else:S=None
  if remaining==rank:
   if S is not None:need(all(zero(M) for M in S),"complete remaining zero formal rows")
   tail=[eye(free) if k==0 else zmat(free,free) for k in range(len(A))]
   free_labels=[labels[j] for j in ci[rank:]];last=height
  else:
   need(S is not None and zero(S[0]) and precision>0,"whole Schur constant zero before exact u division")
   tail,free_labels,last=recurse(S[1:],remaining-rank,[labels[j] for j in ci[rank:]],height+1)
  answer=[]
  for k in range(len(tail)):
   check();top=zmat(rank,free)
   for j in range(k+1):top-=IV[j]*tail[k-j]
   x=zmat(nc,free)
   for i in range(rank):
    for j in range(free):x[ci[i],j]=top[i,j]
   for i in range(nc-rank):
    for j in range(free):x[ci[rank+i],j]=tail[k][i,j]
   answer.append(x)
  return answer,free_labels,last
 N,fc,loss=recurse(series,expected_rank,list(range(n0)),0)
 need(paid==expected_exponents and loss==max(expected_exponents)
      and len(N)==len(series)-loss and len(fc)==202 and len(set(fc))==202,
      "whole paid Smith spectrum and actual independent precision loss")
 for k,M in enumerate(N):
  need(sub(M,fc,list(range(202)))==(eye(202) if k==0 else zmat(202,202)),
       "all202 original free coordinates form an exact constant unit")
  check();v=zmat(m0,202)
  for j in range(k+1):v+=series[j]*N[k-j]
  need(zero(v),"all original small-series equations for every retained mapper coefficient")
 return N,{"freeOriginalColumns":fc,"paidExponents":paid,"precisionLoss":loss,
   "maximumVerifiedDegree":len(N)-1,"originalRows":m0,"originalColumns":n0,"kernelColumns":202,
   "completeOriginalProductCoordinates":m0*202*len(N),"allOriginalRowsVerified":True,
   "all202OriginalFreeCoordinatesVerified":True,"steps":steps}
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in PIN:ap.add_argument("--"+key.replace("_","-"),required=True,type=pathlib.Path)
 for key in ("source_prepared_out","full_out","outside_out","out"):
  ap.add_argument("--"+key.replace("_","-"),required=True,type=pathlib.Path)
 ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args(argv);need(math.isfinite(a.seconds) and 15<=a.seconds<=600 and 512<=a.memory_mib<=4096,"explicit mapper budgets")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 prep=a.source_prepared_out.resolve();full=a.full_out.resolve();outside=a.outside_out.resolve()
 start=time.monotonic();stop=[False];files=[];binding=None;rc=1
 rp=out/"higher-two-regular202-mappers-receipt.json"
 rec={"format":"isp-two-original-regular202-mappers-preparation-v1","status":"running","phase":"inputs","field":31,
  "original202SourceTransportComplete":False,"original202OutsideLeftTransportComplete":False,
  "higherQuotientActuallyComputed":False,"characteristicZeroHighSmithComputed":False,
  "selectedLeadingCoefficientUnitProved":False,"largeDataUploadedOrCommitted":False,
  "parameters":{"secondsLimit":a.seconds,"memoryMiB":a.memory_mib},"events":[]}
 def sig(signum,frame):stop[0]=True
 signal.signal(signal.SIGTERM,sig);signal.signal(signal.SIGINT,sig)
 def check():
  if stop[0] or time.monotonic()-start>=a.seconds-4:raise BudgetExpired("shared regular-mapper budget; complete stages retained")
 def keep(p):
  item={"file":p.name,**identity(p),"temporaryOnly":True};files[:]=[x for x in files if x["file"]!=p.name];files.append(item);return item
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start;rec["parameters"]["temporaryFiles"]=files;save(rp,rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint();print(json.dumps({"phase":phase,"elapsedSeconds":rec["mathematicalElapsedSeconds"]}),flush=True);check()
 try:
  blobs={k:checked(getattr(a,k),v) for k,v in PIN.items()};ids={k:digest(v) for k,v in blobs.items()}
  header_ids={}
  for name,pin in HEADERS.items():
   for directory in (a.source_native.parent,a.outside_native.parent):checked(directory/name,pin)
   header_ids[name]={"bytes":pin[0],"sha256":pin[1]}
  ps=read(prep/"higher-kernel-original-216-source-receipt.json")
  need(ps["status"]=="completed" and ps["parameters"]["binding"]==PREP_BINDING
       and ps["actualKoszulTailConstantRank"]==1632 and ps["actualConstantUnitDeterminantModulo31"]==15
       and ps["sourceDirectSumOverZ31PowerSeriesProved"] and ps["all1632NaturalSyzygiesProvedByVerifiedOriginalAntisymmetry"],
       "actual same original1632 plus216 source direct sum")
  paid=json.loads(blobs["paid_source_summary"])["result"]
  for key in ("highComplementTailPositionsZeroBased","highComplementOriginalSourceRowsOneBased","actual1632UnitTailRowPositionsSHA256",
              "actualFieldReducedTransposeSHA256"):
   need(ps["parameters"][key]==paid["parameters"][key],"all paid logical source profile coordinates: "+key)
  pm=read(prep/"complete-stage-manifest.json");need(pm["binding"]==PREP_BINDING,"complete original source stage manifest")
  for name,item in pm["stages"].items():need(identity(prep/name)==item,"all complete original source preparation file bytes")
  cp=read(prep/"complete-original-high216-source-profile.json")
  need(cp["binding"]==PREP_BINDING and cp["actualConstantRank"]==1632 and cp["actualUnitDeterminantModulo31"]==15
       and cp["highComplementTailPositionsZeroBased"]==ps["parameters"]["highComplementTailPositionsZeroBased"],
       "same original source unit profile")
  fr=read(full/"full-infinity-natural-dual-schur-receipt.json")
  orc=read(outside/"koszul-outside-minimal-field-smith-receipt.json")
  need(fr["status"]=="completed" and fr["parameters"]["binding"]==FULL_BINDING and fr["completedNaturalDegree"]==32
       and fr["all66PaidOriginalPrefixCoefficientIdentitiesVerified"] and fr["fullInfinityTorsionLengthModulo31"]==66
       and fr["fullInfinityMaximumPositiveExponentModulo31"]==11
       and fr["parameters"]["smallSeriesSmith"]["paidExponents"]==FULL_EXP,"actual original full through32 and full spectrum")
  need(orc["status"]=="completed" and orc["parameters"]["binding"]==OUTSIDE_BINDING and orc["completedNaturalDegree"]==35
       and orc["all66PaidOriginalOutsidePrefixCoefficientIdentitiesVerified"]
       and orc["allOriginalNaturalOutsideCoefficientArraysRetained"] and orc["outsideTorsionLengthModulo31"]==149
       and orc["outsideMaximumPositiveExponentModulo31"]==14
       and orc["parameters"]["smallSeriesSmith"]["paidExponents"]==OUTSIDE_EXP,"actual original outside through35 and full spectrum")
  ff={x["file"]:x for x in fr["parameters"]["temporaryFiles"]}
  of={x["file"]:x for x in orc["parameters"]["temporaryFiles"]}
  def parent_file(directory,items,name):
   p=directory/name;it=items[name]
   need(identity(p)=={"bytes":it["bytes"],"sha256":it["sha256"]},"complete actual parent file: "+name)
   return p
  nr=read(parent_file(full,ff,"full-dual-receipt.json"))
  for key in ("unitOriginalSourceRowsOneBased","unitOriginalOutputIndicesZeroBased","tailOriginalSourceRowsOneBased"):
   need(nr[key]==cp[key],"same original full source and output dictionary: "+key)
  E=cp["highComplementTailPositionsZeroBased"];eraw=cp["highComplementOriginalSourceRowsOneBased"]
  need(len(E)==216 and eraw==[nr["tailOriginalSourceRowsOneBased"][i] for i in E],"exact original216 tail embedding")
  op=read(parent_file(outside,of,"outside-original-field-unit-profile.json"))
  need(op["binding"]==OUTSIDE_BINDING and op["actualOutsideConstantRank"]==1603,"same original outside constant unit")
  pr=list(op["unitRows"]);pc=list(op["unitColumns"]);tr=[i for i in range(1834) if i not in set(pr)]
  need(len(pr)==len(pc)==1603 and len(tr)==231 and len(set(pc))==1603,"whole original outside unit dictionary")
  for name in ("outside-original-natural-coefficients.bin","outside-constant-unit-inverse-field31.bin"):
   parent_file(outside,of,name)
  tok=iter(blobs["native_model"].decode().split());need(next(tok)=="R150_NATIVE_NF_V1","same original native model")
  def take(n):return [next(tok) for _ in range(n)]
  take(11*(66+121));need(int(next(tok))==3333,"complete original prebasis")
  pre=[list(map(int,take(4))) for _ in range(3333)];take(6*66*6)
  need(list(map(int,take(2)))==[2195,9],"complete native source schema");take(2195*3)
  need(list(map(int,take(9)))==list(range(2,11)) and next(tok,None) is None,"complete original model tail")
  selected=json.loads(blobs["selected_receipt"]);J=sorted([x[3] for x in pre]+list(map(int,selected["selectedSourceRows"])))
  need(len(J)==len(set(J))==4354 and selected["allOriginalSourceIdentitiesVerified"],"whole same selected J")
  Jc=sorted(set(range(1,6189))-set(J))
  need(hashlib.sha256(canonical(Jc)).hexdigest()==orc["parameters"]["originalOutsideRowsSHA256"],"same original outside source ordering")
  material={"version":"two-original-regular202-mappers-v1","source":identity(__file__),"inputs":ids,"headers":header_ids,
    "sourceDirectSumBinding":PREP_BINDING,"fullParentBinding":FULL_BINDING,"outsideParentBinding":OUTSIDE_BINDING,
    "parentReceipts":{"source":identity(prep/"higher-kernel-original-216-source-receipt.json"),
      "full":identity(full/"full-infinity-natural-dual-schur-receipt.json"),"outside":identity(outside/"koszul-outside-minimal-field-smith-receipt.json")},
    "sourceProfile":identity(prep/"complete-original-high216-source-profile.json"),
    "outsideProfile":identity(outside/"outside-original-field-unit-profile.json"),
    "field":31,"sourceDegree":32,"outsideDegree":35,"retainedMapperDegree":21,
    "sourceInversePole":11,"outsideInversePole":14,"independentPrecisionLosses":True,
    "originalOutsideRowsSHA256":hashlib.sha256(canonical(Jc)).hexdigest()}
  binding=hashlib.sha256(canonical(material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":material,"highComplementOriginalSourceRowsOneBased":eraw,
    "originalOutsideRowsSHA256":material["originalOutsideRowsSHA256"],
    "sameOriginalJVerified":True,"allOriginalConstantUnitDictionariesVerified":True})
  manifestpath=out/"complete-mapper-stage-manifest.json"
  manifest=read(manifestpath) if manifestpath.exists() else {"binding":binding,"stages":{}}
  need(manifest["binding"]==binding,"same complete mapper stage binding")
  def commit_stage(name,items):
   manifest["stages"][name]=[{"file":p.name,**identity(p)} for p in items];save(manifestpath,manifest);keep(manifestpath)
  def have_stage(name):
   if name not in manifest["stages"]:return False
   for x in manifest["stages"][name]:
    p=out/x["file"];need(identity(p)=={"bytes":x["bytes"],"sha256":x["sha256"]},"every complete cached mapper stage");keep(p)
   return True
  from flint import nmod_mat
  import flint
  rec["pythonFlintVersion"]=flint.__version__
  fullseries=out/"complete-high216-kernel202-series.bin";fullmeta=out/"complete-high216-kernel202-metadata.json"
  beat("same-original27-by216-regular-kernel")
  if have_stage("high-small-kernel"):
   high=series_read(fullseries,binding,216,202,21);hm=read(fullmeta);need(hm["binding"]==binding,"saved high kernel metadata")
   rec["events"].append({"reusedCompleteHigh216RegularKernel":True})
  else:
   A=[]
   for k in range(33):
    check();name="full-dual-schur-"+str(k)+".bin"
    bb=field_read(full/name,b"R15FDS31",k,1848,27,FULL_BINDING,ff[name])
    M=nmod_mat(1848,27,list(bb),P)
    A.append(sub(M,E,list(range(27))).transpose())
   high,hm=regular_kernel(A,14,FULL_EXP,check);need(len(high)==22,"full32 retains complete high mapper through21")
   hm["binding"]=binding;series_write(fullseries,high,binding);save(fullmeta,hm);commit_stage("high-small-kernel",[fullseries,fullmeta]);del A
  keep(fullseries);keep(fullmeta)
  outseries=out/"complete-outside231-left202-series.bin";outmeta=out/"complete-outside231-left202-metadata.json"
  beat("same-original29-by231-regular-kernel")
  if have_stage("outside-small-kernel"):
   left=series_read(outseries,binding,231,202,21);om=read(outmeta);need(om["binding"]==binding,"saved outside kernel metadata")
   rec["events"].append({"reusedCompleteOutside231RegularKernel":True})
  else:
   A=[]
   for k in range(36):
    check();name="outside-schur-"+str(k)+".bin"
    bb=field_read(outside/name,b"R15OSS31",k,231,29,OUTSIDE_BINDING,of[name])
    A.append(nmod_mat(231,29,list(bb),P).transpose())
   left,om=regular_kernel(A,29,OUTSIDE_EXP,check);need(len(left)==22,"outside35 retains complete left mapper through21")
   om["binding"]=binding;series_write(outseries,left,binding);save(outmeta,om);commit_stage("outside-small-kernel",[outseries,outmeta]);del A
  keep(outseries);keep(outmeta)
  beat("save-whole-original-transport-heads")
  hp=out/"high202-native-heads.bin";lp=out/"outside202-native-heads.bin"
  head=b"R15HKS31"+struct.pack("<IIIII",P,1,21,216,202)+binding.encode()+FULL_BINDING.encode()
  head+=struct.pack("<216H",*eraw)+struct.pack("<202H",*hm["freeOriginalColumns"])
  head+=b"".join(bytes(int(v) for v in M.entries()) for M in high)
  save_bytes(hp,head);keep(hp)
  head=b"R15OLH31"+struct.pack("<IIIII",P,1,21,231,202)+binding.encode()+OUTSIDE_BINDING.encode()
  head+=struct.pack("<1603H",*pr)+struct.pack("<1603H",*pc)+struct.pack("<231H",*tr)
  head+=struct.pack("<202H",*om["freeOriginalColumns"])
  head+=b"".join(bytes(int(v) for v in M.entries()) for M in left)
  save_bytes(lp,head);keep(lp)
  metadata={"format":"isp-complete-two-original-mapper-transport-heads-v1","binding":binding,"field":31,"maximumDegree":21,
    "sourceParentBinding":FULL_BINDING,"outsideParentBinding":OUTSIDE_BINDING,
    "highHeadOriginalSourceRowsOneBased":eraw,"highFreeHeadPositionsZeroBased":hm["freeOriginalColumns"],
    "outsideUnitRows":pr,"outsideUnitColumns":pc,"outsideTailRows":tr,"outsideFreeTailPositionsZeroBased":om["freeOriginalColumns"],
    "originalOutsideSourceRowsOneBased":Jc,
    "sourceHeads":{"file":hp.name,**identity(hp)},"outsideHeads":{"file":lp.name,**identity(lp)},
    "sourceNative":ids["source_native"],"outsideNative":ids["outside_native"],"headers":header_ids,
    "fullParentNativeProfile":dict(ff["prepared/full-original-constant-profile.txt"]),
    "outsideOriginalCoefficients":dict(of["outside-original-natural-coefficients.bin"]),
    "outsideConstantInverse":dict(of["outside-constant-unit-inverse-field31.bin"]),
    "highRegularKernel":hm,"outsideRegularKernel":om,
    "allOriginalSmallKernelProductsVerified":True,"bothOriginalFree202BlocksVerified":True,
    "independentPrecisionLossesVerified":True,"wholeOriginalNativeTransportStillRequired":True}
  mp=out/"prepared-two-original-mapper-transports.json";save(mp,metadata);keep(mp);commit_stage("native-heads",[hp,lp,mp])
  rec.update(status="completed",outcome="complete-two-original-regular202-mapper-heads",
    sourceSmallKernelRows=216,outsideSmallKernelRows=231,kernelColumns=202,
    maximumVerifiedMapperDegree=21,sourcePrecisionLoss=11,outsidePrecisionLoss=14,
    all119988OriginalHighSmallProductsVerified=True,all128876OriginalOutsideSmallProductsVerified=True,
    all202HighFreeCoordinatesVerified=True,all202OutsideFreeCoordinatesVerified=True,
    independentPrecisionLossesVerified=True)
  rec["parameters"].update({"highFreeOriginalSourceRowsOneBased":[eraw[i] for i in hm["freeOriginalColumns"]],
    "outsideFreeOriginalSourceRowsOneBased":[Jc[tr[i]] for i in om["freeOriginalColumns"]],
    "highSmallUnitSteps":hm["steps"],"outsideSmallUnitSteps":om["steps"],
    "preparedTransports":identity(mp),"nativeTransportRequiredBeforeQuotient":True});rc=0
 except BudgetExpired as ex:
  rec.update(status="budget-exhausted",outcome="checkpointed-two-regular-mappers",error=str(ex));rc=75
 except Exception as ex:
  rec.update(status="failed",error=str(ex),exceptionType=type(ex).__name__)
  p=out/"exception.log";p.write_text(traceback.format_exc());keep(p);rc=1
 finally:checkpoint()
 need(rp.stat().st_size<100000,"only small execution summaries may be published")
 print(json.dumps(rec,separators=(",",":")),flush=True);return rc
if __name__=="__main__":sys.exit(main())
