#!/usr/bin/env python3
"""Complete original F127 nine-target cyclic module and exact h-star action.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Only the paid 299-dimensional action and its nine original target coordinates
are consumed. No normal form, Groebner basis, whole torsion, or Q claim is redone.
All dense arrays and source-power recipes remain in temporary checkpoints.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,resource,signal,struct,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
P=127
FORMAT="r150-original127-nine-target-cyclic-module-and-hstar-v1"
WHOLE_BINDING="05c13d9a57fee12f0751d40feccbfb601686b3d02f497d0e8a99092c44db4211"
GB_BINDING="9e8510d9519e43fe4f8765a6672194c9dba6d1776a9adf652ac343c5261ebc3e"
PAID={
 "original127-whole-torsion-pipeline-receipt.json":(9819,"2c1054b2c3224c7c27c4ff09e1852bbab3a219429f8d08528832d81041de8c07"),
 "torsion-whole-state.bin":(1414575,"948d6e78dc96e8d9e367797d33919ce4c1e1deb406dee346505200da00ea4d60"),
 "whole-torsion-characteristic.json":(2560,"ee048002bcda7090ed599709d88ad2d74ecd46448e647bfb3513fa3ad9b64bd6")}
HSTAR_PIN=(1286,"e04560989cfe0d888995290fa917b457f09f6caa975f59889ee0864e5b82ae31")
TARGETS=list(range(2,11))
stop_requested=False
class Budget(Exception):pass
def check(ok,msg):
 if not ok:raise ValueError(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(p):
 h=hashlib.sha256()
 with Path(p).open("rb") as f:
  for b in iter(lambda:f.read(1048576),b""):h.update(b)
 return h.hexdigest()
def digest(b):return hashlib.sha256(b).hexdigest()
def record(p):return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p),"temporaryOnly":True}
def atomic(p,obj):
 temp=p.with_name(p.name+".tmp");temp.write_bytes(canonical(obj)+b"\n");os.replace(temp,p)
def verify(p,pin,what):
 check(p.is_file() and p.stat().st_size==pin[0] and sha(p)==pin[1],"actual paid bytes: "+what)
def integer_mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def read_hstar(p):
 verify(p,HSTAR_PIN,"original h-star parameters");x=json.loads(p.read_text())
 check(x["format"]=="r150-original-hstar-integer-parameters-v1" and x["coefficientOrder"]=="ascending","h-star original schema")
 check(x["sourceBlob"]=="4aadf7e744f7da751cdbf847dbd66709905905e8" and x["targetRawLabels"]==TARGETS,"same original target labels and integer authority")
 fp=list(map(int,x["FPlus"]));fm=list(map(int,x["FMinus"]));e=list(map(int,x["E8"]))
 check(fp==[-8,32,-25,5] and fm==[864,864,135,5] and e==[9600,-25472,-3392,15936,-2888,-936,153,50,5],"original integer factors")
 h=integer_mul([0,0,0,1],integer_mul(integer_mul(fp,fp),integer_mul(integer_mul(fm,fm),e)))
 check(h==list(map(int,x["hStarCoefficients"])) and len(h)==24 and h[-1]==3125 and x["hStarDegree"]==23 and int(x["hStarLeadingCoefficient"])==3125,"all 24 original integer h-star coefficients")
 check(h[-1]%P!=0,"h-star leading coefficient is a field unit")
 return h
def read_state(path,nmod_mat):
 b=path.read_bytes();check(b[:8]==b"R15TS127" and b[-8:]==b"ENDTS127","whole source state magic and EOF")
 check(b[8:72].decode()==WHOLE_BINDING and b[72:136].decode()==GB_BINDING,"whole source and original GB bindings")
 geom=struct.unpack_from("<12I",b,136)
 check(geom==(127,1034,45,1021,8,701,805,13,299,9,506,57),"actual complete whole-state geometry, not an old 31 profile")
 _,q,D,rank,B,total,n,nf,t,nt,obs,stable=geom
 body=184+3*n+2*nf
 flags=body+n*n+nf*n+nt*n
 check(list(b[flags:flags+nt])==[1]*nt and list(b[flags+nt:flags+2*nt])==[1]*nt,"all nine original targets are bounded and in the complete torsion")
 kernel_at=flags+2*nt;action_at=kernel_at+t*n;targets_at=action_at+t*t
 expected=targets_at+nt*t+obs*(4+n)+obs*8+8
 check(len(b)==expected and action_at==909073,"complete original state layout")
 action=b[action_at:targets_at];targets=b[targets_at:targets_at+nt*t]
 kernel=b[kernel_at:action_at]
 targetstates=b[body+n*n+nf*n:flags]
 check(all(x<P for x in action+targets+kernel+targetstates),"canonical original field action, basis and target arrays")
 J=nmod_mat(t,t,list(action),P)
 T=nmod_mat(nt,t,list(targets),P).transpose()
 K=nmod_mat(t,n,list(kernel),P).transpose()
 original=nmod_mat(nt,n,list(targetstates),P).transpose()
 check(K*T==original,"all 805 by 9 original target-state coordinate products")
 audit={"prime":P,"torsionDimension":t,"wholeStateDimension":n,"observationRank":obs,
  "originalTargetLabels":TARGETS,"allNineBoundedAndTorsion":True,
  "allOriginalTargetCoordinateProductsVerified":True,"originalTargetCoordinateProductCount":n*nt,
  "actionSHA256":digest(action),"originalTargetCoordinatesSHA256":digest(targets),
  "completeSourceAndFreeDirectionsInheritedFromPaidWholeState":True}
 return J,T,audit
def mat_data(M):
 vals=bytes(int(x) for x in M.entries())
 return {"rows":M.nrows(),"columns":M.ncols(),"entriesHex":vals.hex(),"entriesSHA256":digest(vals)}
def from_data(x,nmod_mat):
 b=bytes.fromhex(x["entriesHex"])
 check(len(b)==x["rows"]*x["columns"] and all(v<P for v in b) and digest(b)==x["entriesSHA256"],"complete cached canonical field matrix")
 return nmod_mat(x["rows"],x["columns"],list(b),P)
def poly_coeff(p):return [int(x) for x in p.coeffs()]
def monic(p,nmod_poly):
 c=poly_coeff(p);check(c and c[-1],"nonzero polynomial for monic normalization")
 a=pow(c[-1],-1,P);return nmod_poly([(v*a)%P for v in c],P)
def exact_quot(a,b,nmod_poly):
 q,r=divmod(a,b);check(r==nmod_poly([],P),"exact field polynomial division");return q
def lcm(a,b,nmod_poly):return monic(exact_quot(a,a.gcd(b),nmod_poly)*b,nmod_poly)
def poly_summary(p,nmod_poly):
 unit,factors=p.factor();product=nmod_poly([int(unit)],P);out=[]
 for f,e in factors:
  product*=f**int(e);out.append({"degree":int(f.degree()),"coefficients":poly_coeff(f),"multiplicity":int(e)})
 check(product==p,"complete polynomial factor product")
 return {"degree":int(p.degree()),"coefficients":poly_coeff(p),"coefficientSHA256":digest(bytes(poly_coeff(p))),"factorizationUnit":int(unit),"factors":out,"factorProductVerified":True}
def choose_rows(M,rows,nmod_mat):
 return nmod_mat(len(rows),M.ncols(),[int(M[i,j]) for i in rows for j in range(M.ncols())],P)
def choose_columns(M,cols,nmod_mat):
 return nmod_mat(M.nrows(),len(cols),[int(M[i,j]) for i in range(M.nrows()) for j in cols],P)
def pivots(R,rank):
 out=[];previous=-1
 for i in range(rank):
  row=[int(R[i,j]) for j in range(R.ncols())]
  pos=next((j for j,v in enumerate(row) if v),None)
  check(pos is not None and pos>previous and row[pos]==1,"actual canonical RREF pivot sequence")
  out.append(pos);previous=pos
 check(all(int(R[i,j])==0 for i in range(rank,R.nrows()) for j in range(R.ncols())),"all RREF remaining rows vanish")
 return out
def scaled(M,c,nmod_mat):
 return nmod_mat(M.nrows(),M.ncols(),[(int(x)*c)%P for x in M.entries()],P)
def apply_poly(J,c,S,nmod_mat,beat):
 out=nmod_mat(J.nrows(),S.ncols(),P)
 for v in reversed(c):
  beat();out=J*out
  if v%P:out+=scaled(S,v%P,nmod_mat)
 return out
def zero(M):return all(int(x)==0 for x in M.entries())
def individual_summary(d):
 return {"label":d["label"],"cyclicDimension":d["cyclicDimension"],"firstDependencyPower":d["firstDependencyPower"],
  "minimalPolynomial":{k:v for k,v in d["minimalPolynomial"].items() if k not in ("factors","factorizationUnit")},
  "allOriginal299RelationCoordinatesVerified":d["allOriginal299RelationCoordinatesVerified"],
  "minimalityCertifiedByIndependentPrecedingPowers":d["minimalityCertifiedByIndependentPrecedingPowers"]}
def main():
 ap=argparse.ArgumentParser()
 for key in ("whole-out","hstar","out"):ap.add_argument("--"+key,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
 a=ap.parse_args();check(1<=a.seconds<=600 and 256<=a.memory_mib<=4096,"bounded target consumer")
 a.out.mkdir(parents=True,exist_ok=True);start=time.monotonic();deadline=start+a.seconds
 rp=a.out/"original127-nine-target-cyclic-receipt.json";mp=a.out/"target-cyclic-manifest.json"
 r={"format":FORMAT,"status":"running","parameters":{"author":"Astra-ISP-789f / normal_annihilator",
  "aiAssisted":"GPT-6 Astra Pro","prime":P,"scope":"complete joint original-nine-target module inside paid whole F127 torsion",
  "allLargeArraysTemporaryOnly":True,"normalFormsRecomputed":False,"gradedBasisRecomputed":False,
  "wholeTorsionRecomputed":False,"characteristicZeroMembershipInferred":False,
  "coefficient31TorsionBoundsTransferred":False},"events":[]}
 manifest=None;rc=1
 def save():
  r["elapsedSeconds"]=time.monotonic()-start;atomic(rp,r)
 def beat():
  if stop_requested or time.monotonic()>=deadline:raise Budget("stopped at a completed target-module phase boundary or next exact operation")
 def load_phase(name):
  d=manifest["phases"].get(name)
  if d is None:return None
  p=a.out/d["file"];verify(p,(d["bytes"],d["sha256"]),"complete target phase "+name)
  with gzip.open(p,"rb") as f:raw=f.read()
  check(digest(raw)==d["payloadSHA256"],"target phase payload "+name);x=json.loads(raw)
  check(x["format"]==FORMAT+"-temporary-phase" and x["binding"]==r["binding"] and x["phase"]==name,"same target phase identity")
  r["events"].append({"phase":name,"reusedCompletedPhase":True});return x["data"]
 def put_phase(name,data):
  raw=canonical({"format":FORMAT+"-temporary-phase","binding":r["binding"],"phase":name,"data":data})
  p=a.out/(name+".json.gz");temp=p.with_name(p.name+".tmp")
  with temp.open("wb") as f:
   with gzip.GzipFile(filename="",mode="wb",fileobj=f,mtime=0,compresslevel=1) as g:g.write(raw)
  os.replace(temp,p);d=record(p);d["payloadSHA256"]=digest(raw)
  manifest["phases"][name]=d;atomic(mp,manifest)
  r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
  r["events"].append({"phase":name,"reusedCompletedPhase":False,"elapsedSeconds":time.monotonic()-start})
  save();return data
 try:
  resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2);resource.setrlimit(resource.RLIMIT_CORE,(0,0))
  signal.signal(signal.SIGTERM,request_stop)
  for name,pin in PAID.items():verify(a.whole_out/name,pin,"whole127 "+name)
  parent=json.loads((a.whole_out/"original127-whole-torsion-pipeline-receipt.json").read_text())
  pp=parent["parameters"];ns=pp["nativeStatistics"]
  check(parent["status"]=="completed" and parent["binding"]==WHOLE_BINDING and pp["wholeAffineDegreeVerified"] and pp["wholeAffineTorsionDegree"]==299,"actual complete original affine torsion")
  check(pp["completeOriginalSourceCount"]==6188 and pp["identity"]["parentGBBinding"]==GB_BINDING and ns["phase"]==5 and ns["allKernelAndActionProductsVerified"] and ns["actualObservationStableRowReductionVerified"] and ns["wholeTorsionNotOnlyTargets"],"complete original source and free-module scope")
  h=read_hstar(a.hstar)
  identity={"algorithm":"original-target-power-bases-first-dependencies-and-verified-joint-actions-v1",
   "prime":P,"wrapperSHA256":sha(__file__),"wholeBinding":WHOLE_BINDING,"wholeOriginalGBBinding":GB_BINDING,
   "paidFiles":{k:{"bytes":v[0],"sha256":v[1]} for k,v in PAID.items()},
   "hStarParameters":{"bytes":HSTAR_PIN[0],"sha256":HSTAR_PIN[1]},"originalTargetLabels":TARGETS,
   "krylovPowerRangeInclusive":[0,299]}
  r["binding"]=digest(canonical(identity));r["parameters"].update({"identity":identity,"seconds":a.seconds,"memoryMiB":a.memory_mib,
   "all24IntegerHStarCoefficientsVerified":True,"hStarIntegerDegree":23,"hStarLeading127Unit":True})
  if mp.exists():
   manifest=json.loads(mp.read_text());check(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==r["binding"],"same exact target-module continuation")
  else:
   check(not any(a.out.glob("*.json.gz")),"no unbound target-module checkpoint")
   manifest={"format":FORMAT+"-manifest","binding":r["binding"],"phases":{}};atomic(mp,manifest)
  import flint
  from flint import nmod_mat,nmod_poly
  r["parameters"]["pythonFlintVersion"]=getattr(flint,"__version__","unknown")
  J,T,audit=read_state(a.whole_out/"torsion-whole-state.bin",nmod_mat)
  r["parameters"]["originalStateAudit"]=audit
  char=json.loads((a.whole_out/"whole-torsion-characteristic.json").read_text())
  check(char["binding"]==WHOLE_BINDING and char["wholeStateSHA256"]==PAID["torsion-whole-state.bin"][1] and char["completeFactorProductVerified"] and char["characteristicDegree"]==299,"paid complete characteristic identity")
  full_char=nmod_poly(char["coefficients"],P);check(full_char.degree()==299 and poly_coeff(full_char)[-1]==1,"paid whole characteristic degree299")
  n=J.nrows();nt=T.ncols()
  def krylov(name,S):
   d=load_phase(name)
   if d is not None:return from_data(d["matrix"],nmod_mat)
   blocks=[];current=S
   for power in range(n+1):
    beat();blocks.append([int(x) for x in current.entries()])
    if power<n:current=J*current
   K=nmod_mat(n,nt*(n+1),[blocks[power][i*nt+j] for i in range(n) for power in range(n+1) for j in range(nt)],P)
   put_phase(name,{"matrix":mat_data(K),"seedSHA256":mat_data(S)["entriesSHA256"],
    "powerRangeInclusive":[0,n],"targetOrder":TARGETS,"allPowersGeneratedByPaidOriginalAction":True})
   return K
  def cyclic_polynomials(prefix,K):
   out=[];common=nmod_poly([1],P)
   for target_index,label in enumerate(TARGETS):
    name=prefix+"-target-"+str(label);d=load_phase(name)
    if d is None:
     beat();one=choose_columns(K,[power*nt+target_index for power in range(n+1)],nmod_mat)
     R,rank=one.rref();rank=int(rank);pivot=pivots(R,rank)
     check(pivot==list(range(rank)) and rank<=n,"all first Krylov powers independent until the first actual dependence")
     coef=[(-int(R[i,rank]))%P for i in range(rank)]+[1]
     # This verifies the first dependence in all original299 torsion coordinates.
     for row in range(n):
      check(sum(coef[k]*int(one[row,k]) for k in range(rank+1))%P==0,"all original rows of first minimal target relation")
     pol=nmod_poly(coef,P);exact_quot(full_char,pol,nmod_poly)
     d=put_phase(name,{"label":label,"cyclicDimension":rank,"firstDependencyPower":rank,
       "independentOriginalPowers":pivot,"minimalPolynomial":poly_summary(pol,nmod_poly),
       "allOriginal299RelationCoordinatesVerified":True,"relationProductCoordinates":n,
       "minimalityCertifiedByIndependentPrecedingPowers":True})
    check(d["label"]==label and d["allOriginal299RelationCoordinatesVerified"] and d["minimalityCertifiedByIndependentPrecedingPowers"],"complete target minimal relation")
    pol=nmod_poly(d["minimalPolynomial"]["coefficients"],P);common=lcm(common,pol,nmod_poly);out.append(d)
   exact_quot(full_char,common,nmod_poly)
   return out,common
  def module(prefix,K,S,common):
   name=prefix+"-complete-module";d=load_phase(name)
   if d is not None:return d
   beat();R,rank=K.rref();rank=int(rank);cols=pivots(R,rank)
   check(all(c//nt<n for c in cols),"no characteristic-degree power needed for original module basis")
   B=choose_columns(K,cols,nmod_mat)
   if rank:
    Rt,rr=B.transpose().rref();check(int(rr)==rank,"independent original target-power basis")
    rows=pivots(Rt,rank);U=choose_rows(B,rows,nmod_mat);det=int(U.det())
    check(det!=0,"true original-coordinate unit minor for target basis")
    inverse=U.inv();check(U*inverse==nmod_mat(rank,rank,[1 if i==j else 0 for i in range(rank) for j in range(rank)],P),"actual target-coordinate inverse")
    JB=J*B;action=inverse*choose_rows(JB,rows,nmod_mat);seed=inverse*choose_rows(S,rows,nmod_mat)
    check(B*action==JB,"all original299 module invariance coordinates")
    check(B*seed==S,"all original299 target generator coordinates")
    minimal=action.minpoly();characteristic=action.charpoly()
   else:
    rows=[];det=1;action=nmod_mat(0,0,P);seed=nmod_mat(0,nt,P)
    check(zero(S),"zero target module has zero original generators")
    minimal=nmod_poly([1],P);characteristic=nmod_poly([1],P)
   check(minimal==common,"joint action minimal polynomial equals lcm of nine independently certified first-dependence polynomials")
   check(characteristic.degree()==rank and poly_coeff(characteristic)[-1]==1,"joint module characteristic degree")
   exact_quot(characteristic,common,nmod_poly);exact_quot(full_char,characteristic,nmod_poly)
   d=put_phase(name,{"basis":mat_data(B),"action":mat_data(action),"originalGeneratorCoordinates":mat_data(seed),
    "originalTorsionUnitRows":rows,"unitDeterminant127":det,
    "originalPowerRecipes":[{"targetLabel":TARGETS[c%nt],"parameterPower":c//nt} for c in cols],
    "generatorPolynomialMultiplierIntegerCoefficients":([1] if prefix=="original" else h),
    "summary":{"dimension":rank,"basisColumnCount":rank,"allBasisColumnsArePowersOfDeclaredOriginalGenerators":True,
     "allOriginalModuleInvarianceProductsVerified":True,"moduleInvarianceProductCoordinates":n*rank,
     "allOriginalGeneratorCoordinateProductsVerified":True,"generatorProductCoordinates":n*nt,
     "completeInvariantModuleContainingAllNineGenerators":True,"completeByMutualContainment":True,
     "commonMinimalPolynomial":poly_summary(common,nmod_poly),
     "characteristicPolynomial":poly_summary(characteristic,nmod_poly),
     "characteristicDividesPaidWholeCharacteristic":True,"jointMinpolyEqualsNineFirstRelationsLCM":True}})
   return d
  K=krylov("original-target-krylov",T)
  individual,common=cyclic_polynomials("original",K)
  joint=module("original",K,T,common)
  r["parameters"]["originalTargetModule"]=joint["summary"]
  r["parameters"]["originalIndividualTargets"]=[individual_summary(d) for d in individual];save()
  images=load_phase("hstar-exact-original-action")
  if images is None:
   beat();H=apply_poly(J,[x%P for x in h],T,nmod_mat,beat);H0=J*H-scaled(H,2,nmod_mat)
   action=from_data(joint["action"],nmod_mat);coordinates=from_data(joint["originalGeneratorCoordinates"],nmod_mat)
   basis=from_data(joint["basis"],nmod_mat)
   hcoord=apply_poly(action,[x%P for x in h],coordinates,nmod_mat,beat)
   check(basis*hcoord==H,"exact h-star original action and restricted action agree in all299 coordinates")
   hc=nmod_poly([x%P for x in h],P);hzero=nmod_poly([-2,1],P)*hc
   ann_after=monic(exact_quot(common,common.gcd(hc),nmod_poly),nmod_poly)
   ann_hzero=monic(exact_quot(common,common.gcd(hzero),nmod_poly),nmod_poly)
   flags=[all(int(H[i,j])==0 for i in range(n)) for j in range(nt)]
   flags0=[all(int(H0[i,j])==0 for i in range(n)) for j in range(nt)]
   images=put_phase("hstar-exact-original-action",{"hStarImages":mat_data(H),"hZeroImages":mat_data(H0),
    "hStarRestrictedCoordinates":mat_data(hcoord),"integerHStarCoefficientSHA256":digest(canonical(h)),
    "summary":{"hStarDegree":23,"hStarCoefficientResidues":[x%P for x in h],
     "all24IntegerCoefficientsVerified":True,"allOriginal299RestrictedActionProductsVerified":True,
     "restrictedActionProductCoordinates":n*nt,"targetLabels":TARGETS,
     "hStarTargetZeroFlags":flags,"hZeroTargetZeroFlags":flags0,
     "hStarImageRank":int(H.rank()),"hZeroImageRank":int(H0.rank()),
     "hStarKillsAllNineOriginalTargets":all(flags),"hZeroKillsAllNineOriginalTargets":all(flags0),
     "predictedHStarCommonMinimalPolynomial":poly_summary(ann_after,nmod_poly),
     "hZeroCommonMinimalPolynomialFromVerifiedOriginalModule":poly_summary(ann_hzero,nmod_poly),
     "hStarAnnihilatorFormulaUsedOnlyWithFullTargetModule":True}})
  H=from_data(images["hStarImages"],nmod_mat);r["parameters"]["hStarAction"]=images["summary"];save()
  HK=krylov("hstar-target-krylov",H)
  hindividual,hcommon=cyclic_polynomials("hstar",HK)
  hjoint=module("hstar",HK,H,hcommon)
  check(poly_coeff(hcommon)==images["summary"]["predictedHStarCommonMinimalPolynomial"]["coefficients"],"actual complete h-star target module agrees with m/gcd(m,h-star)")
  r["parameters"]["hStarTargetModule"]=hjoint["summary"];r["parameters"]["hStarIndividualTargets"]=[individual_summary(d) for d in hindividual]
  r["parameters"]["allHStarTargetModuleAnnihilatorIdentitiesVerified"]=True
  r["parameters"]["finiteFieldScopeOnly"]=True
  r["status"]="completed";r["outcome"]="complete-original-nine-target-cyclic-modules-and-hstar-action";rc=0
 except Budget as e:
  r["status"]="budget-checkpoint";r["outcome"]="complete-target-phases-retained";r["parameters"]["budgetMessage"]=str(e);rc=75
 except BaseException as e:
  r["status"]="failed";r["errorType"]=type(e).__name__;r["error"]=str(e)
  r["parameters"]["errorType"]=type(e).__name__;r["parameters"]["errorMessage"]=str(e);rc=1
 finally:
  if manifest is not None:
   r["parameters"]["completedTemporaryPhases"]=manifest["phases"]
   if mp.exists():r["parameters"]["temporaryManifest"]=record(mp)
  save()
 print(json.dumps({"status":r["status"],"outcome":r.get("outcome"),"elapsedSeconds":r["elapsedSeconds"],"error":r.get("error")}),flush=True)
 return rc
def request_stop(signum,frame):
 global stop_requested
 stop_requested=True
if __name__=="__main__":sys.exit(main())
