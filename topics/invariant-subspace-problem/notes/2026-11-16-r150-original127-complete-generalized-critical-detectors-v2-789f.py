#!/usr/bin/env python3
"""Complete original-GB generalized critical detectors over F127 extension jets.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Remove only actual degree-zero GB unit rows. Keep all positive-degree rows,
solve the complete truncated local kernel, and certify that selected detectors
separate the entire paid critical primary in its original299 coordinates.
This file prepares NF-component jets only; original4367 transport, integer
p^2 products and all1834 global-source Bockstein scans belong to the consumer.
"""
from __future__ import annotations
import argparse,array,gzip,hashlib,importlib.util,json,math,os,resource,signal,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
P=127
FORMAT="r150-original127-complete-generalized-critical-detectors-v1"
HELPER="2026-11-16-r150-original127-nine-target-cyclic-module-789f.py"
HELPER_PIN=(20947,"d520b190ac84f1990ed8ee84d405cc34c31d09e140ad26b8442c099872d26ed3")
GB_BINDING="9e8510d9519e43fe4f8765a6672194c9dba6d1776a9adf652ac343c5261ebc3e"
GB_PIN=(43787388,"144871db774835d8b5c369f243cebb441258bc4419d577ed0a0ba3062e21129d")
GB_RECEIPT_PIN=(5289,"3442ad58f08ff1b7b7b4865bfc7715f43e747f40b65e702e1d4b191142ad17f2")
PROFILE_BINDING="7fd6a5d4a535e55f7fb06909bcec10634e7c8e0706f8fa1bd6dfd115a6da51c2"
PROFILE_RECEIPT_PIN=(7885,"5685d638b0cd509481fa482571435c6310b39c85873082fc1421b1a0a63c695f")
PROFILE_MANIFEST_PIN=(1379,"1a5901c7b7621dbfcc4b73bf3ee032872948e0a988291b6c7a3ac1d8017cd654")
LABELS=("FPlus-1","FMinus-1","E8-1","E8-2","E8-3")
stopped=False
class Budget(Exception):pass
def need(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def digest(b):return hashlib.sha256(b).hexdigest()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def verify(p,pin,what):
 need(p.is_file() and p.stat().st_size==pin[0] and sha(p)==pin[1],"exact paid bytes: "+what)
def atomic(p,x):
 t=p.with_name(p.name+".tmp");t.write_bytes(canonical(x)+b"\n");os.replace(t,p)
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def request_stop(signum,frame):
 global stopped
 stopped=True
def identity(n,nmod_mat):
 return nmod_mat(n,n,[int(i==j) for i in range(n) for j in range(n)],P)
def rowcol(A,rows,cols,nmod_mat):
 return nmod_mat(len(rows),len(cols),[int(A[i,j]) for i in rows for j in cols],P)
def kernel(A,helper,nmod_mat):
 R,rank=A.rref();rank=int(rank);piv=helper.pivots(R,rank);used=set(piv)
 free=[j for j in range(A.ncols()) if j not in used];q=len(free)
 flat=[0]*(A.ncols()*q)
 for j,f in enumerate(free):
  flat[f*q+j]=1
  for i,p in enumerate(piv):flat[p*q+j]=(-int(R[i,f]))%P
 K=nmod_mat(A.ncols(),q,flat,P)
 need(helper.choose_rows(K,free,nmod_mat)==identity(q,nmod_mat),"complete kernel free identity")
 need(helper.zero(A*K),"all finite kernel products")
 return K,rank,piv,free
def read_original_basis(path,nmod_mat,beat):
 raw=path.read_bytes()
 need(raw[:8]==b"R15GB127" and raw[8:72].decode()==GB_BINDING and raw[-8:]==b"ENDGB127","complete original GB header and footer")
 need(struct.unpack_from("<5I",raw,72)==(127,1034,45,1021,9),"actual original GB geometry")
 q=1034;W=33;nw=46*W;off=92;rows=[];meta=[];previous=0;coefficient_checks=0
 for i in range(1021):
  beat();component,degree,node,scale=struct.unpack_from("<HBIB",raw,off);off+=8
  need(previous<component<=q and degree<=8 and 1<=node<=2855+69407428 and 1<=scale<P,"actual original final GB source label")
  previous=component;w=array.array("I");w.frombytes(raw[off:off+28*nw]);off+=28*nw
  if sys.byteorder!="little":w.byteswap()
  need(w.itemsize==4 and len(w)==7*nw,"whole packed GB row")
  for bit in range(7):
   need(all(x==0 for x in w[bit*nw+(degree+1)*W:(bit+1)*nw]),"all higher parameter coefficients actually zero")
   need(all((w[bit*nw+k*W+W-1]>>10)==0 for k in range(degree+1)),"original component padding zero")
  powers=[]
  for k in range(degree+1):
   a=[]
   for c in range(q):
    v=sum(((w[bit*nw+k*W+c//32]>>(c%32))&1)<<bit for bit in range(7))
    need(v<P,"canonical original GB coefficient");a.append(v);coefficient_checks+=1
   powers.append(a)
  need(powers[degree][component-1]==1 and all(v==0 for v in powers[degree][:component-1]),"actual monic graded leading component")
  rows.append(powers);meta.append({"componentOneBased":component,"degree":degree,"node":node,"scale":scale})
 off+=9*28*nw
 need(off==len(raw)-8,"all nine targets skipped at exact paid GB boundary")
 maxd=max(x["degree"] for x in meta)
 B=[]
 for k in range(maxd+1):
  B.append(nmod_mat(1021,1034,[rows[i][k][c] if k<len(rows[i]) else 0 for i in range(1021) for c in range(1034)],P))
 hist={str(k):sum(x["degree"]==k for x in meta) for k in range(maxd+1)}
 return B,meta,{"basisRows":1021,"components":1034,"maximumDegree":maxd,"degreeHistogram":hist,
  "allOriginalPolynomialCoefficientsRead":coefficient_checks,"allOriginalLeadingTermsVerified":True,
  "allHigherCoefficientsAndPaddingZero":True,"allOriginalPositiveRowsRetained":True}
def alpha_powers(h,upto):
 d=len(h)-1;out=[[1]+[0]*(d-1)]
 for _ in range(upto):
  old=out[-1];last=old[-1];new=[0]+old[:-1]
  out.append([(new[j]-last*h[j])%P for j in range(d)])
 return out
def evaluate_expanded(coeff,h,order,nmod_mat,beat):
 """Regular representation of coefficient matrices at s=alpha+t."""
 m=coeff[0].nrows();n=coeff[0].ncols();D=len(coeff)-1;d=len(h)-1
 need(all(A.nrows()==m and A.ncols()==n for A in coeff),"same polynomial coefficient matrix dimensions")
 ap=alpha_powers(h,D+d)
 stack=nmod_mat(D+1,m*n,[int(v) for A in coeff for v in A.entries()],P)
 out=[]
 for k in range(order):
  beat();weights=[]
  for eo in range(d):
   for ei in range(d):
    for degree in range(D+1):
     weights.append(0 if degree<k else (math.comb(degree,k)*ap[degree-k+ei][eo])%P)
  values=nmod_mat(d*d,D+1,weights,P)*stack
  out.append(nmod_mat(m*d,n*d,[int(values[eo*d+ei,i*n+j]) for i in range(m) for eo in range(d) for j in range(n) for ei in range(d)],P))
 return out
def expand_original_components(E,core_jets,d,nmod_mat):
 n=E.ncols();q=core_jets[0].ncols();out=[]
 for A in core_jets:
  parts=[E*nmod_mat(n,q,[int(A[i*d+e,j]) for i in range(n) for j in range(q)],P) for e in range(d)]
  out.append(nmod_mat(E.nrows()*d,q,[int(parts[e][i,j]) for i in range(E.nrows()) for e in range(d) for j in range(q)],P))
 return out
def verify_original_gb(B,original_jets,h,order,nmod_mat,beat):
 d=len(h)-1;count=original_jets[0].ncols();m=B[0].nrows();n=B[0].ncols();D=len(B)-1
 ap=alpha_powers(h,D+d);res=[[[0]*count for _ in range(m*d)] for _ in range(order)]
 for j,A in enumerate(original_jets):
  grouped=nmod_mat(n,d*count,[int(A[i*d+e,c]) for i in range(n) for e in range(d) for c in range(count)],P)
  for degree,M in enumerate(B):
   beat();values=M*grouped
   for k in range(min(degree,order-1-j)+1):
    comb=math.comb(degree,k)%P;target=res[j+k]
    for i in range(m):
     for eo in range(d):
      dst=target[i*d+eo]
      for ei in range(d):
       weight=comb*ap[degree-k+ei][eo]%P
       if weight:
        for c in range(count):dst[c]+=weight*int(values[i,ei*count+c])
 for k in range(order):
  need(all(v%P==0 for row in res[k] for v in row),"all original1021 GB equations at every actual jet coefficient")
 return m*d*count*order
def main():
 ap=argparse.ArgumentParser()
 for key in ("gb-out","whole-out","profile-out","sources-root","out"):ap.add_argument("--"+key,type=Path,required=True)
 ap.add_argument("--factor",choices=LABELS,default="E8-1")
 ap.add_argument("--seconds",type=float,default=300);ap.add_argument("--memory-mib",type=int,default=4096)
 a=ap.parse_args();need(10<=a.seconds<=1800 and 1024<=a.memory_mib<=8192,"bounded generalized detector preparation")
 a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();deadline=started+a.seconds
 rp=a.out/("original127-generalized-detectors-"+a.factor+"-receipt.json");mp=a.out/"generalized-detectors-manifest.json"
 r={"format":FORMAT,"status":"running","parameters":{"author":"Astra-ISP-789f / normal_annihilator",
  "aiAssisted":"GPT-6 Astra Pro","prime":P,"factorLabel":a.factor,"finiteFieldScopeOnly":True,
  "normalFormsRecomputed":False,"gradedBasisRecomputed":False,"wholeTorsionRecomputed":False,
  "allLargeArraysTemporaryOnly":True,"coefficientBocksteinComputed":False,
  "original4367TransportComplete":False,"characteristicZeroConclusionInferred":False},"events":[]}
 manifest=None;rc=1
 def save():
  r["elapsedSeconds"]=time.monotonic()-started;atomic(rp,r)
 def beat():
  if stopped or time.monotonic()>=deadline:raise Budget("stop before next complete detector operation; all completed phases retained")
 def put(name,data):
  raw=canonical({"format":FORMAT+"-temporary-phase","binding":r["binding"],"phase":name,"data":data})
  p=a.out/(name+".json.gz");t=p.with_name(p.name+".tmp")
  with t.open("wb") as f:
   with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0,compresslevel=1) as z:z.write(raw)
  os.replace(t,p);desc=record(p);desc["payloadSHA256"]=digest(raw)
  manifest["phases"][name]=desc;atomic(mp,manifest)
  r["events"].append({"phase":name,"reused":False,"elapsedSeconds":time.monotonic()-started});save();return data
 def get(name):
  desc=manifest["phases"].get(name)
  if desc is None:return None
  p=a.out/desc["file"];verify(p,(desc["bytes"],desc["sha256"]),"complete generalized detector phase")
  with gzip.open(p,"rb") as f:raw=f.read()
  need(digest(raw)==desc["payloadSHA256"],"detector payload hash");x=json.loads(raw)
  need(x["format"]==FORMAT+"-temporary-phase" and x["binding"]==r["binding"] and x["phase"]==name,"same complete detector phase")
  r["events"].append({"phase":name,"reused":True});return x["data"]
 try:
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
  signal.signal(signal.SIGTERM,request_stop)
  hp=a.sources_root/HELPER;verify(hp,HELPER_PIN,"paid whole-state matrix reader")
  spec=importlib.util.spec_from_file_location("paid_original127_reader",hp);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
  verify(a.gb_out/"gb-basis.bin",GB_PIN,"complete original GB")
  verify(a.gb_out/"original127-graded-module-pipeline-receipt.json",GB_RECEIPT_PIN,"original complete GB receipt")
  gbp=json.loads((a.gb_out/"original127-graded-module-pipeline-receipt.json").read_text())
  need(gbp["status"]=="completed" and gbp["binding"]==GB_BINDING,"same completed original GB")
  for name,pin in helper.PAID.items():verify(a.whole_out/name,pin,"complete original whole "+name)
  verify(a.profile_out/"original127-critical-primary-receipt.json",PROFILE_RECEIPT_PIN,"complete actual critical profile")
  verify(a.profile_out/"critical-primary-manifest.json",PROFILE_MANIFEST_PIN,"complete critical-primary manifest")
  pp=json.loads((a.profile_out/"original127-critical-primary-receipt.json").read_text())
  pm=json.loads((a.profile_out/"critical-primary-manifest.json").read_text())
  need(pp["status"]=="completed" and pp["binding"]==PROFILE_BINDING and pm["binding"]==PROFILE_BINDING and pp["parameters"]["allFiveCriticalFactorsComplete"] and pp["parameters"]["allPrimaryBasesDirectSumVerified"],"all actual primary directions paid")
  pdesc=pm["phases"]["primary-"+a.factor];pf=a.profile_out/pdesc["file"]
  verify(pf,(pdesc["bytes"],pdesc["sha256"]),"complete selected original primary")
  with gzip.open(pf,"rb") as f:praw=f.read()
  need(digest(praw)==pdesc["payloadSHA256"],"complete primary payload")
  px=json.loads(praw);need(px["binding"]==PROFILE_BINDING and px["phase"]=="primary-"+a.factor,"actual primary identity")
  pdata=px["data"];ps=pdata["summary"]
  need(ps["label"]==a.factor and ps["allPrimaryDirectionsRetained"] and ps["allOriginalPrimaryActionProductsVerified"],"complete primary has original action")
  h=ps["coefficients"];d=ps["degree"];order=ps["maximumExponent"];primary_dim=ps["primaryDimension"];blocks=ps["cyclicBlockCount"]
  ident={"algorithm":"degree-zero-GB-unit-quotient-complete-local-jet-kernel-and-whole-primary-restriction-v1",
   "wrapperSHA256":sha(__file__),"helperSHA256":HELPER_PIN[1],"prime":P,
   "originalGBBinding":GB_BINDING,"originalGBBytes":GB_PIN[0],"originalGBSHA256":GB_PIN[1],
   "wholeBinding":helper.WHOLE_BINDING,"wholeStateSHA256":helper.PAID["torsion-whole-state.bin"][1],
   "profileBinding":PROFILE_BINDING,"profileManifestSHA256":PROFILE_MANIFEST_PIN[1],
   "phasesIndependentlyKeyedByAllFiveFactorLabels":True}
  r["binding"]=digest(canonical(ident));r["parameters"].update({"identity":ident,"seconds":a.seconds,"memoryMiB":a.memory_mib,
   "factorCoefficients":h,"extensionDegree":d,"jetOrder":order,"primaryDimension":primary_dim,"cyclicBlockCount":blocks})
  if mp.exists():
   manifest=json.loads(mp.read_text());need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==r["binding"],"same all-factor detector continuation")
  else:
   need(not any(a.out.glob("*.json.gz")),"no unbound detector phases")
   manifest={"format":FORMAT+"-manifest","binding":r["binding"],"phases":{}};atomic(mp,manifest)
  import flint
  from flint import nmod_mat
  r["parameters"]["pythonFlintVersion"]=getattr(flint,"__version__","unknown")
  B,meta,ba=read_original_basis(a.gb_out/"gb-basis.bin",nmod_mat,beat);r["parameters"]["originalGBAudit"]=ba;save()
  core=get("original-degree-zero-unit-quotient")
  if core is None:
   zr=[i for i,x in enumerate(meta) if x["degree"]==0];pos=[i for i,x in enumerate(meta) if x["degree"]>0]
   Z=helper.choose_rows(B[0],zr,nmod_mat);E,zrank,zpiv,zfree=kernel(Z,helper,nmod_mat)
   need(zrank==len(zr) and E.ncols()==len(pos)+13,"all and only actual degree-zero unit relations removed")
   Q=[helper.choose_rows(M,pos,nmod_mat)*E for M in B]
   core=put("original-degree-zero-unit-quotient",{"constantOriginalGraph":helper.mat_data(E),
    "positivePolynomialCoefficients":[helper.mat_data(M) for M in Q],
    "zeroDegreeOriginalGBRows":zr,"positiveDegreeOriginalGBRows":pos,
    "originalFreeNFComponentsZeroBased":zfree,"removedOriginalPivotComponentsZeroBased":zpiv,
    "summary":{"removedConstantUnitRows":zrank,"remainingRows":len(pos),"remainingColumns":E.ncols(),
     "allOriginalZeroRowProductsVerified":True,"zeroRowProductCoordinates":len(zr)*E.ncols(),
     "allPositiveOriginalRowsProjected":True,"positiveCoefficientProducts":len(Q)*len(pos)*E.ncols(),
     "constantGraphHasOriginalFreeIdentity":True,"polynomialDegreeBound":len(Q)-1}})
  E=helper.from_data(core["constantOriginalGraph"],nmod_mat)
  Q=[helper.from_data(v,nmod_mat) for v in core["positivePolynomialCoefficients"]]
  need(E.nrows()==1034 and Q[0].ncols()==E.ncols() and Q[0].ncols()-Q[0].nrows()==13,"same original quotient and free rank13")
  r["parameters"]["degreeZeroQuotient"]=core["summary"];save()
  name=a.factor+"-constant-unit-formal-graph";graph=get(name)
  if graph is None:
   G=evaluate_expanded(Q,h,order,nmod_mat,beat);M=G[0].nrows();N=G[0].ncols()
   beat();RR,rank=G[0].rref();rank=int(rank);C=helper.pivots(RR,rank);Cset=set(C);F=[j for j in range(N) if j not in Cset]
   need(rank==M-d*blocks and len(F)==d*(13+blocks),"actual complete local constant rank matches all primary blocks")
   beat();Rt,rankt=helper.choose_columns(G[0],C,nmod_mat).transpose().rref()
   need(int(rankt)==rank,"original unit columns have full rank")
   rows=helper.pivots(Rt,rank);rowset=set(rows);tail=[i for i in range(M) if i not in rowset]
   U=rowcol(G[0],rows,C,nmod_mat);inverse=U.inv()
   need(U*inverse==identity(rank,nmod_mat),"actual original scalar unit inverse")
   nf=len(F);X=[];S=[];Grows=[helper.choose_rows(A,rows,nmod_mat) for A in G]
   for k in range(order):
    beat();rhs=nmod_mat(rank,nf,P)
    if k==0:rhs=rowcol(G[0],rows,F,nmod_mat)
    else:
     for i in range(1,k+1):rhs+=Grows[i]*X[k-i]
    sol=inverse*rhs;flat=[0]*(N*nf)
    for i,c in enumerate(C):
     for j in range(nf):flat[c*nf+j]=(-int(sol[i,j]))%P
    if k==0:
     for j,f in enumerate(F):flat[f*nf+j]=1
    x=nmod_mat(N,nf,flat,P);X.append(x)
    residual=nmod_mat(M,nf,P)
    for i in range(k+1):residual+=G[i]*X[k-i]
    need(helper.zero(helper.choose_rows(residual,rows,nmod_mat)),"all original constant-unit graph products at each order")
    if k==0:need(helper.zero(residual),"complete original constant kernel")
    S.append(helper.choose_rows(residual,tail,nmod_mat))
   graph=put(name,{"expandedOriginalCoefficientMatrices":[helper.mat_data(A) for A in G],
    "regularGraphCoefficients":[helper.mat_data(A) for A in X],
    "allRemainingRowSchurCoefficients":[helper.mat_data(A) for A in S],
    "originalUnitRows":rows,"originalUnitColumns":C,"originalFreeColumns":F,"allOtherRows":tail,
    "summary":{"expandedRows":M,"expandedColumns":N,"constantRank":rank,"constantKernelDimension":nf,
     "allConstantUnitInverseProductsVerified":True,"allOriginalUnitJetProductsVerified":True,
     "allResidualRowsRetained":True,"schurRows":len(tail),"ordersRetained":order}})
  G=[helper.from_data(v,nmod_mat) for v in graph["expandedOriginalCoefficientMatrices"]]
  X=[helper.from_data(v,nmod_mat) for v in graph["regularGraphCoefficients"]]
  S=[helper.from_data(v,nmod_mat) for v in graph["allRemainingRowSchurCoefficients"]]
  r["parameters"]["regularGraph"]=graph["summary"];save()
  localname=a.factor+"-complete-truncated-kernel";local=get(localname)
  if local is None:
   beat();nr=S[0].nrows();nf=S[0].ncols();N=X[0].nrows()
   toeplitz=nmod_mat(order*nr,order*nf,[int(S[k-j][i,c]) if j<=k else 0
    for k in range(order) for i in range(nr) for j in range(order) for c in range(nf)],P)
   Y,trank,tpiv,tfree=kernel(toeplitz,helper,nmod_mat);nk=Y.ncols()
   need(nk==13*d*order+primary_dim,"complete local-ring kernel has all free jets and all primary functionals")
   A=[]
   for k in range(order):
    beat();z=nmod_mat(N,nk,P)
    for i in range(k+1):
     Ypart=helper.choose_rows(Y,list(range((k-i)*nf,(k-i+1)*nf)),nmod_mat)
     z+=X[i]*Ypart
    A.append(z)
   local=put(localname,{"coreComponentJetCoefficients":[helper.mat_data(z) for z in A],
    "smallSchurKernel":helper.mat_data(Y),"smallSchurKernelFreeColumns":tfree,
    "summary":{"completeKernelDimension":nk,"freePolynomialJetDimension":13*d*order,
     "criticalPrimaryDimension":primary_dim,"smallSchurRows":toeplitz.nrows(),"smallSchurColumns":toeplitz.ncols(),
     "smallSchurRank":trank,"allSmallOriginalSchurProductsVerified":True,
     "allConstantUnitAndResidualRowsCovered":True,"noHigherIncomingDirectionDeleted":True}})
  A=[helper.from_data(v,nmod_mat) for v in local["coreComponentJetCoefficients"]]
  r["parameters"]["completeLocalKernel"]=local["summary"];save()
  finalname=a.factor+"-complete-original-component-detectors";final=get(finalname)
  if final is None:
   beat();whole=(a.whole_out/"torsion-whole-state.bin").read_bytes()
   need(whole[:8]==b"R15TS127" and whole[8:72].decode()==helper.WHOLE_BINDING and whole[-8:]==b"ENDTS127","same complete original whole state")
   coords=list(struct.iter_unpack("<HB",whole[184:184+3*805]));body=184+3*805+26
   flags=body+805*805+13*805+9*805;ka=flags+18;ja=ka+299*805
   need(ja==909073 and len(coords)==805,"same original805 source coordinate order")
   K=nmod_mat(299,805,list(whole[ka:ja]),P).transpose()
   Up=helper.from_data(pdata["original299Basis"],nmod_mat)
   need(Up.nrows()==299 and Up.ncols()==primary_dim,"entire paid original primary basis")
   W=K*Up;window_coeff=[]
   for power in range(8):
    idx=[i for i,(c,k) in enumerate(coords) if k==power]
    Wp=helper.choose_rows(W,idx,nmod_mat)
    Ep=helper.choose_rows(E,[coords[i][0]-1 for i in idx],nmod_mat)
    window_coeff.append(Wp.transpose()*Ep)
   Pjet=evaluate_expanded(window_coeff,h,order,nmod_mat,beat)
   nk=A[0].ncols();images=[]
   for k in range(order):
    beat();z=nmod_mat(primary_dim*d,nk,P)
    for i in range(k+1):z+=Pjet[i]*A[k-i]
    images.append(z)
   candidates=[]
   for j in range(nk):
    candidates.append(nmod_mat(order*d,primary_dim,[int(images[k][i*d+e,j]) for k in range(order) for e in range(d) for i in range(primary_dim)],P))
   all_rows=nmod_mat(nk*order*d,primary_dim,[int(v) for M in candidates for v in M.entries()],P)
   need(int(all_rows.rank())==primary_dim,"all original local jets separate the complete whole primary")
   chosen=[];covered=nmod_mat(0,primary_dim,P);coverage=0;coverage_history=[]
   while coverage<primary_dim:
    beat();best=None;best_rank=coverage;best_matrix=None
    current=[int(v) for v in covered.entries()]
    for j,M in enumerate(candidates):
     if j in chosen:continue
     trial=nmod_mat(covered.nrows()+M.nrows(),primary_dim,current+[int(v) for v in M.entries()],P)
     rank=int(trial.rank())
     if rank>best_rank:best=j;best_rank=rank;best_matrix=trial
    need(best is not None,"a complete separating detector family exists")
    chosen.append(best);covered=best_matrix;coverage=best_rank;coverage_history.append(coverage)
   Jp=helper.from_data(pdata["primaryAction"],nmod_mat)
   apowers=alpha_powers(h,d+1);theta=[0]*(order*d*order*d)
   for k in range(order):
    for eo in range(d):
     for ei in range(d):theta[(k*d+eo)*(order*d)+k*d+ei]=apowers[ei+1][eo]
    if k:
     for e in range(d):theta[(k*d+e)*(order*d)+(k-1)*d+e]=1
   theta_matrix=nmod_mat(order*d,order*d,theta,P)
   for j in chosen:
    need(candidates[j]*Jp==theta_matrix*candidates[j],"complete primary detector intertwines the original parameter action")
   selected=[helper.choose_columns(z,chosen,nmod_mat) for z in A]
   original=expand_original_components(E,selected,d,nmod_mat)
   original_products=verify_original_gb(B,original,h,order,nmod_mat,beat)
   for k in range(order):
    residual=nmod_mat(G[0].nrows(),len(chosen),P)
    for i in range(k+1):residual+=G[i]*selected[k-i]
    need(helper.zero(residual),"all complete positive-row original jet products")
   final=put(finalname,{"original1034ComponentJetCoefficients":[helper.mat_data(z) for z in original],
    "selectedLocalKernelColumns":chosen,"completePrimaryRestrictions":[helper.mat_data(candidates[j]) for j in chosen],
    "originalPrimaryBasis":pdata["original299Basis"],
    "summary":{"factorLabel":a.factor,"factorCoefficients":h,"extensionDegree":d,"jetOrder":order,
     "detectorCount":len(chosen),"originalNFComponentCount":1034,"primaryDimension":primary_dim,
     "coverageRanks":coverage_history,"completePrimaryRestrictionRank":coverage,
     "allCriticalPrimaryDirectionsSeparated":True,"allPrimaryParameterIntertwiningProductsVerified":True,
     "primaryIntertwiningProductCoordinates":len(chosen)*order*d*primary_dim,"allOriginalGBJetProductsVerified":True,
     "originalGBJetProductCoordinates":original_products,"allOriginalPositiveRowJetProductsVerified":True,
     "coefficientOrder":"parameter-t-power,original-NF-component,alpha-power,detector-column",
     "fieldAlphaRelationCoefficients":h,"original4367TransportComplete":False,
     "coefficientBocksteinComputed":False,"characteristicZeroConclusionInferred":False}})
  r["parameters"]["completeGeneralizedDetectors"]=final["summary"]
  r["status"]="completed";r["outcome"]="complete-critical-primary-separated-by-original-GB-jets";rc=0
 except Budget as e:
  r["status"]="budget-checkpoint";r["outcome"]="complete-generalized-detector-phases-retained"
  r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=75
 except BaseException as e:
  r["status"]="failed";r["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};rc=1
 finally:
  if manifest is not None:
   r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
   if mp.exists():r["parameters"]["temporaryManifest"]=record(mp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],
  "error":r["parameters"].get("error")}),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
