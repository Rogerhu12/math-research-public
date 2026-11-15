#!/usr/bin/env python3
"""Original natural-u Koszul outside Smith selector over F31.
Astra-ISP-789f / normal_annihilator; AI-assisted, GPT-6 Astra Pro.
Reuse the actual 1603 original unit profile; retain all 1834 outside rows.
No characteristic-zero solve, no old4318 elimination, no data publication.
"""
import argparse,gzip,hashlib,itertools,json,math,os,pathlib,resource,signal,struct,sys,time,traceback
sys.dont_write_bytecode=True
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):os.environ[name]="1"
PIN={
 "primitive":(65159,"44350c49f9f60c61427b7278bf7f3d24b6cb2e6583848a113b03bb109516d4fe"),
 "coefficients":(20580,"7ab537a3c8f9a3d13b924a23f37f8d4ce4fa7621e3608920404ed0051b2fd5c1"),
 "selected":(21285,"20373c07422701e37b9226fe1fe72cb8ee1e7848df505ebbacd92cf818093c2a"),
 "paid_bound":(26242,"e57d4bc56bbd50e1d1700b819a3f5f6499c92b885788ec3fe55089b5a6755657")}
PRIMITIVE_RAW_SHA="fa2e5d80e9fbd47e1e237ae60c548900a15922a0543e02be77fc972dc52944b3"
PAID_Q_BINDING="2d9b068281400ec635fc2c912edf29e59d2bec1e3686bf6c3f6abd6ac01890f2"
PAID_FIRST_BINDING="c11dd73f0b8f469a8c1abee84de0b8ff7a38906a992376a16129a44fcad8607b"
PAID_B_BINDING="43124d7d621b24353e3686cb1db8932ee6259822f22c1dbb1f8e0cd1d7b54600"
HELPER_SHA="9332d9d394b1a17444c9ccc20b3971cf74b7e932cffc8d9189e4e2f64fe0c428"
POINT_SHA="97d31570a0bd99d33066fc6ea47984203b2964521ceeb50920f0a49dd3bb8074"
SUPPORT_CODE_SHA="0689aec8f35c098a3d1e831297b94102ec38596fe724ac63cdf4bbc9c012e7a2"
FIELD=31
class BudgetExpired(Exception):pass
def need(x,msg):
 if not x:raise ValueError(msg)
def digest(b):return {"bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def identity(p):
 h=hashlib.sha256();n=0
 with pathlib.Path(p).open("rb") as f:
  while True:
   b=f.read(1048576)
   if not b:break
   n+=len(b);h.update(b)
 return {"bytes":n,"sha256":h.hexdigest()}
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def read(p):
 b=pathlib.Path(p).read_bytes()
 return json.loads(gzip.decompress(b) if b[:2]==b"\x1f\x8b" else b)
def save(p,x):
 p=pathlib.Path(p);tmp=p.with_name(p.name+".tmp")
 if p.suffix==".gz":
  with gzip.open(tmp,"wt",encoding="utf-8",compresslevel=1) as f:json.dump(x,f,separators=(",",":"))
 else:tmp.write_text(json.dumps(x,separators=(",",":"))+"\n",encoding="utf-8")
 os.replace(tmp,p)
 return {"file":p.name,**identity(p),"temporaryOnly":True}
def check_pin(p,pin):
 b=pathlib.Path(p).read_bytes()
 need(digest(b)=={"bytes":pin[0],"sha256":pin[1]},"complete pinned input: "+str(p))
 return b
def matrix_rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def zero(M):return not any(M.entries())
def select(M,rows,cols):
 from flint import nmod_mat
 return nmod_mat(len(rows),len(cols),[int(M[i,j]) for i in rows for j in cols],FIELD)
def pivots(M):
 R,r=M.rref();r=int(r)
 p=[next(j for j in range(M.ncols()) if R[i,j]) for i in range(r)]
 need(p==sorted(set(p)),"strict field pivot order")
 return p
def write_field(path,magic,degree,rows,binding,cols=None):
 if hasattr(rows,"nrows"):
  nr,nc=rows.nrows(),rows.ncols();body=bytes(int(v) for v in rows.entries())
 else:
  nr=len(rows);nc=cols if cols is not None else (len(rows[0]) if nr else 0)
  need(all(len(row)==nc for row in rows),"complete field row extents")
  body=b"".join(bytes(row) for row in rows)
 need(len(magic)==8 and len(body)==nr*nc and all(x<FIELD for x in body),"canonical complete field array")
 raw=magic+struct.pack("<IIII",FIELD,degree,nr,nc)+binding.encode()+body
 need(len(raw)==88+nr*nc,"bound field extent")
 tmp=path.with_name(path.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,path)
 return {"file":path.name,**digest(raw),"rows":nr,"cols":nc,"degree":degree,"temporaryOnly":True}
def read_field(path,magic,degree,nr,nc,binding):
 b=path.read_bytes()
 need(b[:8]==magic and struct.unpack_from("<IIII",b,8)==(FIELD,degree,nr,nc)
      and b[24:88].decode()==binding and len(b)==88+nr*nc,"saved bound field header")
 need(all(x<FIELD for x in b[88:]),"saved canonical field entries")
 return [bytearray(b[88+i*nc:88+(i+1)*nc]) for i in range(nr)]
def add_sparse(O,X,Y,check):
 for i,row in enumerate(O):
  y=Y[i]
  for j,v in row:
   x=X[j]
   for k in range(29):y[k]+=v*x[k]
  if i%128==0:check()
def reduced_rows(Y):return [bytearray(v%FIELD for v in row) for row in Y]
def rectangular_smith(series,check):
 """True unit Schur reduction of every retained row; precision includes degree0."""
 from flint import nmod_mat
 mats=series;nr=mats[0].nrows();nc=mats[0].ncols();free=nr-nc
 need(free==202 and all(M.nrows()==nr and M.ncols()==nc for M in mats),"231 by29 original small series")
 height=0;paid=[];steps=[]
 while nc:
  check();precision=len(mats)-1;pc=pivots(mats[0]);rank=len(pc)
  if rank:
   pr=pivots(select(mats[0],list(range(nr)),pc).transpose())
   need(len(pr)==rank,"complete actual rectangular unit profile")
   rs=set(pr);cs=set(pc)
   rows=pr+[i for i in range(nr) if i not in rs]
   cols=pc+[j for j in range(nc) if j not in cs]
  else:rows=list(range(nr));cols=list(range(nc))
  steps.append({"uExponent":height,"rows":nr,"columns":nc,"availableDegree":precision,
    "constantRank":rank,"unitRows":rows[:rank],"unitColumns":cols[:rank]})
  paid.extend([height]*rank)
  if rank==nc:
   nr-=rank;nc=0;break
  mr=nr-rank;mc=nc-rank
  if rank:
   U=[select(M,rows[:rank],cols[:rank]) for M in mats]
   V=[select(M,rows[:rank],cols[rank:]) for M in mats]
   W=[select(M,rows[rank:],cols[:rank]) for M in mats]
   Z=[select(M,rows[rank:],cols[rank:]) for M in mats]
   inverse=[U[0].inv()]
   for degree in range(1,precision+1):
    check();q=nmod_mat(rank,rank,[0]*(rank*rank),FIELD)
    for a in range(1,degree+1):q+=U[a]*inverse[degree-a]
    inverse.append(-inverse[0]*q)
   eye=nmod_mat([[int(i==j) for j in range(rank)] for i in range(rank)],FIELD)
   z=nmod_mat(rank,rank,[0]*(rank*rank),FIELD)
   for degree in range(precision+1):
    check();q=nmod_mat(rank,rank,[0]*(rank*rank),FIELD)
    for a in range(degree+1):q+=U[a]*inverse[degree-a]
    need(q==(eye if degree==0 else z),"whole rectangular unit-series inverse")
   WI=[]
   for degree in range(precision+1):
    q=nmod_mat(mr,rank,[0]*(mr*rank),FIELD)
    for a in range(degree+1):q+=W[a]*inverse[degree-a]
    WI.append(q)
   schur=[]
   for degree in range(precision+1):
    check();q=Z[degree]
    for a in range(degree+1):q=q-WI[a]*V[degree-a]
    schur.append(q)
  else:schur=mats
  need(zero(schur[0]),"all rectangular constant Schur entries zero")
  nr,nc=mr,mc;height+=1
  if precision==0:
   return {"complete":False,"paidExponents":paid,"unresolvedCount":nc,
      "unresolvedExponentAtLeast":height,"torsionLengthLowerBound":sum(paid)+height*nc,
      "freeCokernelRank":free,"steps":steps}
  mats=schur[1:]
 need(nr==free and len(paid)==29 and all(1<=x<=21 for x in paid),"all29 positive exponents within proved cutoff")
 return {"complete":True,"paidExponents":paid,"unresolvedCount":0,
   "torsionLength":sum(paid),"maximumPositiveExponent":max(paid),"freeCokernelRank":free,"steps":steps}
def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 for key in ("pairing-root","primitive-equations","rebuild-root","paid-schur-summary","out"):
  ap.add_argument("--"+key,type=pathlib.Path,required=True)
 ap.add_argument("--seconds",type=float,default=120)
 ap.add_argument("--memory-mib",type=int,default=1024)
 ap.add_argument("--maximum-degree",type=int,default=21)
 a=ap.parse_args(argv)
 need(math.isfinite(a.seconds) and 0<a.seconds<=300,"finite selector clock <=300s")
 need(0<a.memory_mib<=2048 and 0<=a.maximum_degree<=21,"finite memory and proved jet cutoff")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
 start=time.monotonic();deadline=start+a.seconds-min(3,a.seconds/10);stopped=[False]
 def stop(sig,frame):stopped[0]=True
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 out=a.out.resolve();out.mkdir(parents=True,exist_ok=True)
 rec={"format":"isp-original-koszul-outside-field-smith-selector-v1","status":"running","phase":"inputs",
  "field":31,"characteristicZeroSmithComputed":False,"leadingCoefficientUnitProved":False,
  "old1603RationalSolveRepeated":False,"old4318EliminationRepeated":False,
  "largeDataUploadedOrCommitted":False,"parameters":{},"events":[]}
 rp=out/"koszul-outside-field-smith-receipt.json";binding=None;temps=[];rc=1
 def check():
  if stopped[0] or time.monotonic()>=deadline:raise BudgetExpired("shared selector time or signal; complete layers retained")
 def keep(path):
  z={"file":path.name,**identity(path),"temporaryOnly":True}
  temps[:]=[x for x in temps if x["file"]!=z["file"]];temps.append(z);return z
 def checkpoint():
  rec["mathematicalElapsedSeconds"]=time.monotonic()-start
  rec["parameters"]["temporaryFiles"]=temps
  save(rp,rec)
 def beat(phase):
  rec["phase"]=phase;checkpoint()
  print(json.dumps({"phase":phase,"elapsedSeconds":time.monotonic()-start}),flush=True);check()
 try:
  prepared=a.pairing_root/"reconstructed-source-model";support=a.pairing_root/"reconstructed-source29"
  paths={"source_model":prepared/"exact-original-koszul-outside-model.json.gz",
    "core":prepared/"exact-koszul-sparse-core-and-dag.json.gz",
    "support_receipt":support/"koszul-exact-rational-support-receipt.json",
    "unit_profile":support/"exact-unit-block-profile.json",
    "primitive":a.primitive_equations,
    "coefficients":a.rebuild_root/"rebuilt-first"/"same-original-natural-constant-and-first-coefficients.json.gz",
    "selected":a.rebuild_root/"rebuilt-inputs"/"same-selected-original-source-indices.json",
    "paid_bound":a.paid_schur_summary}
  ids={}
  for name,p in paths.items():
   ids[name]=identity(p)
   if name in PIN:need(ids[name]=={"bytes":PIN[name][0],"sha256":PIN[name][1]},"pinned "+name)
  sr=read(paths["support_receipt"]);model=read(paths["source_model"]);core=read(paths["core"]);pr=read(paths["unit_profile"])
  need(sr["status"]=="completed" and sr["allOriginal4367IntegerProductsZero"]
       and sr["completeKernelDimensionCertifiedOverQ"] and sr["selectedStandardKoszulDimensionOverQ"]==29,"paid complete original29 source scope")
  material={"codeSHA256":SUPPORT_CODE_SHA,"core":ids["core"],"original":ids["source_model"],
    "helper":HELPER_SHA,"point":POINT_SHA}
  need(hashlib.sha256(canonical(material)).hexdigest()==PAID_Q_BINDING
       and sr["parameters"]["binding"]==pr["binding"]==PAID_Q_BINDING
       and sr["parameters"]["inputIdentity"]==material,"complete actual original model/core/source binding")
  sf={x["file"]:x for x in sr["parameters"]["temporaryFiles"]}
  need(paths["unit_profile"].name in sf,"saved actual unit profile identity")
  pp=sf[paths["unit_profile"].name]
  need(ids["unit_profile"]=={"bytes":pp["bytes"],"sha256":pp["sha256"]}
       and pr["coreFileIdentity"]==ids["core"],"actual unit profile bytes")
  need(model["binding"]==core["binding"] and not core["eliminationDAG"]
       and core["activeVariables"]==list(range(1632)),"same unpeeled original1632 variables; no Q-only row operation reused")
  selected=read(paths["selected"]);J=list(map(int,model["selectedRows"]));outside=list(map(int,model["outsideRows"]));free=list(map(int,model["freeRows"]))
  need(len(J)==4354 and len(set(J))==4354 and set(J)==set(map(int,selected["selectedRows"]))
       and free==list(map(int,selected["freeRows"])) and len(set(free))==36
       and outside==sorted(set(range(1,6189))-set(J)),"complete same original J and outside split")
  bound=read(paths["paid_bound"]);br=bound["result"];bs=br["parameters"]["smallSeriesSmith"]
  need(bound["runId"]==43702348535 or str(bound["runId"])=="43702348535","paid current session bound run")
  need(bound["exitCode"]==0 and br["completeSelectedInfinitySmithLengthComputed"]
       and br["all51PaidPrefixFilesCoefficientIdentitiesVerified"] and bs["complete"]
       and sum(bs["paidExponents"])==243 and max(bs["paidExponents"])==21
       and br["parameters"]["newSchurBinding"]==PAID_B_BINDING
       and br["parameters"]["rebuiltInputs"]["selected_model"]==ids["selected"],"paid sameB full243/max21 bound")
  cb=read(paths["coefficients"])
  need(cb["binding"]==PAID_FIRST_BINDING and cb["all1309ConstantIdentitiesVerified"]
       and cb["all4433ParameterFieldIdentitiesVerified"],"paid same original natural coefficient scope")
  raw=gzip.decompress(paths["primitive"].read_bytes())
  need(hashlib.sha256(raw).hexdigest()==PRIMITIVE_RAW_SHA,"complete decompressed original equations")
  eq=json.loads(raw)["equations"];need(len(eq)==17 and all(len(row)==77 for row in eq),"17 by77 polynomial records")
  F=[[[0]*77 for _ in range(17)] for __ in range(11)]
  for e,row in enumerate(eq):
   for j,poly in enumerate(row):
    vals=list(map(int,poly));need(bool(vals),"nonempty original coefficient")
    if e>=11 and j<11:
     need(not any(vals),"Gamma linear term identically zero");continue
    degree=10 if e<11 and j<11 else 0 if e<11 else 5
    need(not any(vals[degree+1:]),"original natural parameter degree")
    for k in range(degree+1):F[k][e][j]=vals[degree-k] if degree-k<len(vals) else 0
  need(F[0]==[[int(v) for v in row] for row in cb["constant"]]
       and F[1]==[[int(v) for v in row] for row in cb["naturalFirst"]],"every original F0/F1 coefficient")
  binding_material={"version":"original-koszul-outside-field-schur-v1","source":identity(__file__),
   "inputs":ids,"paidSourceBinding":PAID_Q_BINDING,"paidSelectedBinding":PAID_B_BINDING,
   "field":31,"outsideRows":1834,"familyColumns":1632,"constantUnitRank":1603,
   "familyOrder":"i<j lex; factor1,m0,...,m10; Fi source signs +Fj*ei-Fi*ej"}
  binding=hashlib.sha256(canonical(binding_material)).hexdigest()
  rec["parameters"].update({"binding":binding,"inputIdentity":binding_material,"secondsLimit":a.seconds,
   "memoryMiB":a.memory_mib,"requestedMaximumDegree":a.maximum_degree,
   "paidSelectedLength31":243,"paidSelectedMaximumExponent31":21,
   "maximumDegreeIsInclusive":True,"newCharacteristicZeroSolve":False})
  beat("same-original-outside-polynomial")
  variables=[8**i for i in range(11)]
  multipliers=[sum(variables[i] for i in q) for degree in range(4) for q in itertools.combinations_with_replacement(range(11),degree)]
  mi={key:i for i,key in enumerate(multipliers)}
  terms=variables+[variables[i]+variables[j] for i in range(11) for j in range(i,11)]
  oi={row-1:i for i,row in enumerate(outside)}
  phi0=[{} for _ in range(6188)]
  O=[[{} for _ in outside] for __ in range(11)];column=0
  for i in range(17):
   for j in range(i+1,17):
    for factor in [0]+variables:
     for source,pol,sign in ((i,j,1),(j,i,-1)):
      for q,key in enumerate(terms):
       source_row=17*mi[key+factor]+source
       v0=sign*F[0][pol][q]
       if v0:phi0[source_row][column]=phi0[source_row].get(column,0)+v0
       if source_row in oi:
        rr=oi[source_row]
        for k in range(11):
         v=(sign*F[k][pol][q])%FIELD
         if v:O[k][rr][column]=(O[k][rr].get(column,0)+v)%FIELD
     column+=1
    check()
  need(column==1632 and len(multipliers)*17==6188,"complete original family/monomial extent")
  phi0=[{j:v for j,v in row.items() if v} for row in phi0]
  old=[{int(j):int(v) for j,v in row} for row in model["phiRows"]]
  need(phi0==old,"all6188 original constant Koszul coefficients")
  del old
  ids_core=list(map(int,core["coreOriginalRowIds"]))
  need(ids_core==[i for i,row in enumerate(outside) if phi0[row-1]],"all original nonzero core rows")
  need(len(ids_core)==len(core["coreRows"]),"complete core row dictionary")
  for t,i in enumerate(ids_core):
   need({int(j):int(v) for j,v in core["coreRows"][t]}==phi0[outside[i]-1],"actual core is original raw row, no scaling")
  O=[[[ (int(j),int(v)) for j,v in sorted(row.items()) if v] for row in mat] for mat in O]
  rows=[ids_core[int(t)] for t in pr["unitRowPositions"]]
  pc=list(map(int,pr["pivotVariables"]));fc=list(map(int,pr["freeVariables"]))
  need(len(rows)==len(set(rows))==len(pc)==len(set(pc))==1603 and len(fc)==29
       and sorted(pc+fc)==list(range(1632)),"actual complete1603 plus29 profile")
  tail=[i for i in range(1834) if i not in set(rows)];need(len(tail)==231,"all231 nonunit outside rows")
  rec.update(allOriginalNaturalCoefficientsMatched=True,all6188ConstantKoszulCoefficientsMatched=True,
    sameOriginalKoszulFamilyRetained=True,all1834OutsideRowsRetained=True)
  rec["parameters"].update({"nonzeroOutsideCoefficientsByDegree":[sum(map(len,M)) for M in O],
   "constantUnitRank":1603,"outsideSchurShape":[231,29],
   "outsideOriginalRowsSHA256":hashlib.sha256(canonical(outside)).hexdigest(),
   "unitOutsideRowPositionsSHA256":hashlib.sha256(canonical(rows)).hexdigest(),
   "unitFamilyColumnsSHA256":hashlib.sha256(canonical(pc)).hexdigest(),
   "freeFamilyColumns":fc,"originalFreeRows36":free,
   "exactSyzygyConstruction":"all136 antisymmetric original Fi/Fj pairs times1 and11 variables; polynomial commutativity"})
  from flint import nmod_mat
  unitpath=out/"outside-constant-unit-inverse-field31.bin";unitcache=out/"outside-constant-unit-cache.json"
  od=[dict(row) for row in O[0]]
  U=nmod_mat(1603,1603,[od[i].get(j,0) for i in rows for j in pc],FIELD)
  beat("actual1603-unit-inverse")
  if unitcache.exists():
   uc=read(unitcache);need(uc["binding"]==binding and uc["allOriginalUnitInverseProductsVerified"]
      and identity(unitpath)==uc["inverseIdentity"],"complete saved original unit inverse")
   invrows=read_field(unitpath,b"R15OIV31",0,1603,1603,binding)
   inverse=nmod_mat(1603,1603,[v for row in invrows for v in row],FIELD);del invrows
   rec["events"].append({"reusedCompleteOriginalUnitInverse":True})
  else:
   inverse=U.inv();check()
   eye=nmod_mat([[int(i==j) for j in range(1603)] for i in range(1603)],FIELD)
   need(U*inverse==eye,"complete1603 original inverse identity")
   z=write_field(unitpath,b"R15OIV31",0,inverse,binding)
   save(unitcache,{"binding":binding,"inverseIdentity":{"bytes":z["bytes"],"sha256":z["sha256"]},
      "allOriginalUnitInverseProductsVerified":True,"unitRank":1603})
  del U;keep(unitpath);keep(unitcache)
  rec["actualOriginal1603UnitVerified"]=True
  ledgerpath=out/"outside-complete-jet-ledger.json";graphs=[];residuals=[];small=[];records=[]
  if ledgerpath.exists():
   ledger=read(ledgerpath);need(ledger["binding"]==binding and ledger["allCompletedLayersVerified"],"complete old layer binding")
   records=ledger["layers"]
   need([x["degree"] for x in records]==list(range(len(records))),"contiguous completed layer prefix")
   for layer in records:
    k=layer["degree"]
    for kind,magic,nr in (("source",b"R15OKS31",1632),("residual",b"R15ORS31",1834),("schur",b"R15OSS31",231)):
     p=out/layer[kind]["file"]
     need(identity(p)=={"bytes":layer[kind]["bytes"],"sha256":layer[kind]["sha256"]},"every completed layer identity")
     value=read_field(p,magic,k,nr,29,binding)
     if kind=="source":graphs.append(value)
     elif kind=="residual":residuals.append(value)
     else:small.append(nmod_mat(231,29,[v for row in value for v in row],FIELD))
     keep(p)
   rec["events"].append({"reusedCompleteOutsideDegrees":len(records)})
   keep(ledgerpath)
  def commit_layer(k,X,R):
   S=[R[i] for i in tail]
   z={"degree":k}
   for kind,magic,value in (("source",b"R15OKS31",X),("residual",b"R15ORS31",R),("schur",b"R15OSS31",S)):
    p=out/("outside-"+kind+"-"+str(k)+".bin")
    z[kind]=write_field(p,magic,k,value,binding);keep(p)
   records.append(z)
   save(ledgerpath,{"binding":binding,"completedDegree":k,"layers":records,"allCompletedLayersVerified":True})
   keep(ledgerpath);graphs.append(X);residuals.append(R)
   small.append(nmod_mat(231,29,[v for row in S for v in row],FIELD))
   rec["completedNaturalDegree"]=k;checkpoint()
  if not graphs:
   V=nmod_mat(1603,29,[od[i].get(j,0) for i in rows for j in fc],FIELD)
   Z=-(inverse*V)
   X=[bytearray(29) for _ in range(1632)]
   for j,f in enumerate(fc):X[f][j]=1
   for t,p in enumerate(pc):X[p]=bytearray(int(Z[t,j]) for j in range(29))
   Y=[[0]*29 for _ in range(1834)];add_sparse(O[0],X,Y,check);R=reduced_rows(Y)
   need(not any(any(row) for row in R),"all1834 original constant kernel products")
   commit_layer(0,X,R)
  X0=graphs[0]
  need(all(X0[f]==bytearray(int(i==j) for j in range(29)) for i,f in enumerate(fc)),"all29 constant free coordinates")
  G=[]
  for rawrow in free:
   row=[0]*29
   for j,v in phi0[rawrow-1].items():
    for k in range(29):row[k]+=v*X0[j][k]
   G.append([v%FIELD for v in row])
  need(int(nmod_mat(G,FIELD).rref()[1])==29,"original36 free coordinates prove full29 constant source independence")
  rec.update(constantOutsideRank1603Verified=True,originalKoszulConstantRank1632Verified=True,
     all29OriginalConstantSourcesIndependent=True)
  del phi0,od
  for k in range(len(graphs),a.maximum_degree+1):
   beat("original-outside-jet-"+str(k))
   Y=[[0]*29 for _ in range(1834)]
   for degree in range(1,min(10,k)+1):add_sparse(O[degree],graphs[k-degree],Y,check)
   rhs=reduced_rows(Y)
   V=nmod_mat(1603,29,[v for i in rows for v in rhs[i]],FIELD)
   Z=-(inverse*V)
   X=[bytearray(29) for _ in range(1632)]
   for t,p in enumerate(pc):X[p]=bytearray(int(Z[t,j]) for j in range(29))
   Y=[list(row) for row in rhs];add_sparse(O[0],X,Y,check);R=reduced_rows(Y)
   need(not any(any(R[i]) for i in rows),"all1603 original unit output coefficients vanish")
   need(not any(any(X[i]) for i in fc),"all29 higher free source coefficients zero")
   commit_layer(k,X,R)
  rec.update(all1603OriginalUnitJetRowsZero=True,all1834OriginalOutsideJetCoordinatesRetained=True,
     all29FreeFamilyCoordinatesVerified=True)
  beat("full231-by29-series-smith")
  smith=rectangular_smith(small[:a.maximum_degree+1],check)
  rec["parameters"]["smallSeriesSmith"]=smith
  if a.maximum_degree==21:need(smith["complete"],"proved21 cutoff must resolve all29 original outside exponents")
  if smith["complete"]:
   need(smith["torsionLength"]<=243 and smith["maximumPositiveExponent"]<=21,"sameB torsion injection bounds")
   rec.update(status="completed",phase="complete",outcome="complete-outside-field-smith",
      completeOutsideSmithLengthComputed=True,outsideTorsionLengthModulo31=smith["torsionLength"],
      outsideMaximumPositiveExponentModulo31=smith["maximumPositiveExponent"],
      outsidePositiveExponentCount=29,outsideFreeCokernelRank=202)
   rc=0
  else:
   rec.update(status="completed-prefix",outcome="checkpointed-outside-field-jets",
      completeOutsideSmithLengthComputed=False);rc=75
 except BudgetExpired as e:
  rec.update(status="budget-exhausted",outcome="checkpointed-outside-field-jets",error=str(e));rc=75
 except Exception as e:
  rec.update(status="failed",error=str(e),exceptionType=type(e).__name__)
  (out/"exception.log").write_text(traceback.format_exc(),encoding="utf-8");rc=1
 finally:
  rec["parameters"]["largeDataRemainOnlyInCurrentJob"]=True
  checkpoint()
 need(rp.stat().st_size<100000,"only small source-parameter execution summary")
 print(json.dumps(rec,separators=(",",":")),flush=True)
 return rc
if __name__=="__main__":sys.exit(main())
