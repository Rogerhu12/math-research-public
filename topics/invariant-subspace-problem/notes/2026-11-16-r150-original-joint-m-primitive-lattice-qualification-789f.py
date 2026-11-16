#!/usr/bin/env python3
"""Qualify the primitive free lattice of the nine original targets over Z_(31).
Author: ChatGPT (AI), literature_audit. Date: 2026-11-16.

Read only a freshly completed, exactly pinned selected-source parent.  All 225
original target Krylov columns, the full315 quotient, and all16 actual coefficient
torsion directions are retained.  A failed rank qualification is diagnostic, not
a nonmembership theorem.  This program does not compute high-p coordinates.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
os.environ["PYTHONDONTWRITEBYTECODE"]="1"
P=31
FORMAT="r150-original-joint-m-primitive-lattice-qualification-v1"
BASE_NAME="2026-11-16-r150-joint-b-true16-source-rebuild-p9-789f.py"
BASE_SHA="e4b2b935882e899a55d7db10d590e5ce8d35f5fedcab6063a14008a5efe4b69e"
BASE_BYTES=38570
PARENT_BINDING="0a0b38c3107add8f719b0fac0d99ec75f44c48d842b830dadb1ed1e7b1f84ce1"
PARENT_FORMAT="r150-joint-b-true16-selected-source-rebuild-p9-v1"
PARENT_PACK_FORMAT="r150-joint-b-selected-true16-parent-p9-v1"
OLD_FULL_BINDING="712f9b426017d3f63c05e755a314e14d79ac03d22bce6a4b3f943efcd80d7093"
HELPERS={
 "2026-11-14-r150-ninth-first-matrices-789f.py":"3f0da5d1814dac10b3dcfa31ac07c67dec38cab420eeedb3037bb4575c61b00a",
 "2026-11-14-r150-torsion-characteristic-789f.py":"8825680181815794c9b361d267fde5dc679dc1fa2fced44a36470d6c45416ec2"}
STATE_PIN=(1470456,"06bfc5632e0485221587ede871b99bf89eb2efa3cde209458a749b6787f1cfaf")
RECIPE_PIN=(709918,"d4d486d0d1c6a33e091da3e99d58cb604d7b2ef828a84a20ba23edf76d19a63c")
RECIPE_BINDING="918f7a2c9663741bcb670bded5dff4b22a7a9b84d19e579faaad6501703a8b05"
U16_SHA="679132fd4727fd305b77c82beb5d3f2e002df1860045200c3392158ab8eb48b9"
J16_SHA="59d09cbeec71ebf7cda6f12ddd21c1b7ffe1c83a3f9de81b776df0a97df687d8"
LABELS=list(range(2,11))
EXP16=[1,1,2,2,2,2,2,3,3,4,4,4,4,5,5,6]
CLASS_NAMES={"L3":"L3-selected8-paid-class-check","L4":"L4-selected7-paid-class-check",
             "L5":"L5-selected3-paid-class-check","L6":"L6-selected1-complete-class"}
COUNTS={"L3":8,"L4":7,"L5":3,"L6":1}
class BudgetStop(Exception):pass
def check(ok,message):
 if not ok:raise ValueError(message)
def canonical(x):
 return (json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)+"\n").encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
 q=hashlib.sha256()
 with p.open("rb") as f:
  for block in iter(lambda:f.read(1048576),b""):q.update(block)
 return {"bytes":p.stat().st_size,"sha256":q.hexdigest()}
def pin(p,size,digest,label):
 r=identity(p);check(r=={"bytes":size,"sha256":digest},"exact "+label);return r
def atomic(p,data):
 p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(data);os.replace(q,p)
def atomic_json(p,x):atomic(p,canonical(x))
def module(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def safe(root,name):
 q=Path(name);check(not q.is_absolute() and ".." not in q.parts,"parent relative path")
 p=root/q;check(p.resolve().is_relative_to(root.resolve()),"parent path stays in completed parent");return p
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def mr(M):
 return {"rows":M.nrows(),"columns":M.ncols(),"sha256":sha(bytes(z for r in rows(M) for z in r))}
def poly_coeff(p):return [int(p[i]) for i in range(p.degree()+1)]
def imul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c

def main():
 ap=argparse.ArgumentParser()
 for name in ("notes-root","parent-out","state","recipe","out"):ap.add_argument("--"+name,type=Path,required=True)
 ap.add_argument("--seconds",type=float,default=120)
 ap.add_argument("--memory-mib",type=int,default=2048)
 a=ap.parse_args()
 check(0<a.seconds<=300 and 512<=a.memory_mib<=4096,"bounded read-only qualification resources")
 resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
 a.out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();deadline=start+a.seconds
 rp=a.out/"original-joint-m-primitive-lattice-qualification.json"
 rec={"format":FORMAT,"status":"running","parameters":{"prime":31,"originalTargetLabels":LABELS,
      "originalKrylovPowers":list(range(25)),"completeOriginalTargetColumns":225,
      "largeArraysTemporaryOnly":True,"full210Recomputed":False,"highPCoordinatesComputed":False}}
 def save():
  rec["elapsedSeconds"]=time.monotonic()-start;atomic_json(rp,rec)
 def tick():
  if time.monotonic()>deadline-1:raise BudgetStop("read-only qualification budget")
 def stop(signum,frame):raise BudgetStop("qualification signal "+str(signum))
 signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
 signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,a.seconds)
 try:
  from flint import nmod_mat
  sourcepins={}
  for name,digest in HELPERS.items():
   sourcepins[name]=identity(a.notes_root/name);check(sourcepins[name]["sha256"]==digest,"frozen complete-state helper "+name)
  sourcepins[BASE_NAME]=pin(a.notes_root/BASE_NAME,BASE_BYTES,BASE_SHA,"actual selected-source parent program")
  inputs={"state":pin(a.state,*STATE_PIN,"whole original315 state")}
  prp=a.parent_out/"selected-true16-source-rebuild-receipt.json"
  ppp=a.parent_out/"selected-true16-parent.json"
  parent=json.loads(prp.read_bytes());pack=json.loads(ppp.read_bytes())
  inputs["parentReceipt"]=identity(prp);inputs["parentPack"]=identity(ppp)
  check(parent["format"]==PARENT_FORMAT and parent["status"]=="completed"
        and pack["format"]==PARENT_PACK_FORMAT and pack["status"]=="completed","actually completed fresh selected parent")
  sem=parent["parameters"]["inputIdentity"]
  check(sha(canonical(sem))==parent["binding"]==pack["binding"]==PARENT_BINDING,
        "the one explicitly admitted actual parent binding")
  check(sem["driver"]==sourcepins[BASE_NAME] and sem["format"]==PARENT_FORMAT
        and sem["paidFull210Binding"]==OLD_FULL_BINDING and sem["precisionChain"]==[35,30,25,20,15],
        "original parent mathematical scope and precision")
  check({k:parent["parameters"]["parentPack"][k] for k in ("bytes","sha256")}==inputs["parentPack"],
        "completed receipt authenticates the full parent pack")
  check(pack["sourceSHA256"]==BASE_SHA and pack["full210OriginalTheoremBinding"]==OLD_FULL_BINDING
        and pack["complete210Recomputed"] is False and pack["sources"]==sem["sources"]
        and pack["inputs"]==sem["inputs"],"parent code and original-input identity")
  st=parent["parameters"]["stages"]
  check(len(st)==30 and all(v.get("status")=="completed" for v in st.values()),"all30 actual original source stages")
  for key in ("allOriginalIntegerCarriesVerified","allLowerPaid315ClassesMatched","all104LocalFreeChecks",
              "all505GlobalFreeChecks","samePaid25PrefixAndComplete35OriginalGAndV","canonicalOriginalColumnRecipesPreserved"):
   check(pack.get(key) is True,"actual parent gate "+key)
  raw=gzip.decompress(a.recipe.read_bytes())
  check((len(raw),sha(raw))==RECIPE_PIN,"complete210 recipe mathematical payload, not a new210 run")
  recipe=json.loads(raw);check(recipe["binding"]==RECIPE_BINDING,"same actual recipe")
  inputs["recipePayload"]={"bytes":len(raw),"sha256":sha(raw)}
  check(sem["inputs"]["recipePayload"]==inputs["recipePayload"] and sem["inputs"]["state"]==inputs["state"],
        "same state and recipe as the actual parent")
  h=module(a.notes_root/"2026-11-14-r150-ninth-first-matrices-789f.py","r150_joint_m_matrix_helper")
  rd=module(a.notes_root/"2026-11-14-r150-torsion-characteristic-789f.py","r150_joint_m_state_reader")
  classes={}
  for key,n in COUNTS.items():
   d=pack["classes"][key];p=safe(a.parent_out,d["path"]);inputs[key+"Classes"]=identity(p)
   check(inputs[key+"Classes"]=={k:d[k] for k in ("bytes","sha256")},"all actual class bytes "+key)
   q=json.loads(p.read_bytes());z=q["matrixRows"]
   check(q["binding"]==PARENT_BINDING and len(z)==315 and all(len(row)==n for row in z)
         and all(type(c) is int and 0<=c<31 for row in z for c in row),"all315 class coordinates "+key)
   M=nmod_mat(z,31)
   check(mr(M)==q["matrix"]==d["matrix"]==parent["parameters"]["comparisons"][CLASS_NAMES[key]]["matrix"],
         "exact whole315 class hash "+key)
   for flag in ("all104LocalFreeChecks","all315OriginalCoordinateReconstruction","all505GlobalFreeChecks","sameOriginalSAction"):
    check(q.get(flag) is True,"paid class scope "+key+" "+flag)
   if key!="L6":check(q.get("matchesPaidClass") is True,"original lower class comparison "+key)
   classes[key]=M
  U13=nmod_mat(recipe["true13Full315"],31)
  check((U13.nrows(),U13.ncols())==(315,13)
        and h.sub(U13,range(315),[8])==h.sub(classes["L3"],range(315),[0])
        and h.sub(U13,range(315),range(9,13))==h.sub(classes["L4"],range(315),range(4)),
        "the actual source sections in the true13 basis")
  U16=h.join(U13,h.sub(classes["L5"],range(315),[0,1]),classes["L6"])
  check(mr(U16)=={"rows":315,"columns":16,"sha256":U16_SHA} and U16.rank()==16,
        "complete true coefficient-torsion basis, not a pointwise surrogate")
  state=rd.load_state(a.state)
  check((state["stateDimension"],state["torsionDimension"],state["observabilityRank"])==(820,315,505),
        "whole original quotient dimensions")
  J=nmod_mat(state["matrices"]["action"],31)
  K=nmod_mat(state["matrices"]["kernelTranspose"],31).transpose()
  A=nmod_mat(state["matrices"]["A"],31)
  O=nmod_mat(state["observabilityEchelon"],31)
  Xi=nmod_mat(state["matrices"]["targetCoordinates"],31).transpose()
  Targets=nmod_mat(state["matrices"]["targets"],31).transpose()
  check(K.rank()==315 and K*Xi==Targets and A*K==K*J and h.zero(O*K) and h.zero(O*Targets),
        "all original target/action/complete505 products")
  uj=h.solve_span(U16,J*U16)
  check(uj["indices"]==list(range(16)) and h.zero(uj["residual"]),"true16 full original parameter closure")
  J16=uj["solution"]
  check(mr(J16)=={"rows":16,"columns":16,"sha256":J16_SHA}
        and J*U16==U16*J16,"same actual true16 action and all5040 products")
  inputs["true16"]=mr(U16);inputs["true16Action"]=mr(J16)
  semantic={"format":FORMAT,"driver":identity(Path(__file__)),"sources":sourcepins,"inputs":inputs,
            "parentBinding":PARENT_BINDING,"KrylovPowers":list(range(25)),"targetLabels":LABELS,
            "noHighPCoordinateOrGlobal210Recomputation":True}
  binding=sha(canonical(semantic));rec["binding"]=binding;rec["parameters"]["inputIdentity"]=semantic
  save();tick()
  fp=[-8,32,-25,5];fm=[864,864,135,5];e8=[9600,-25472,-3392,15936,-2888,-936,153,50,5]
  hs=imul([0,0,0,1],imul(imul(fp,fp),imul(imul(fm,fm),e8)))
  check(len(hs)==24 and hs[-1]==3125,"original exact hstar polynomial")
  ann=h.mul(hs,h.mul([-2,1],[-2,1]))
  check(len(ann)==26 and h.zero(h.action(ann,J,Xi)),"paid full original x-square-hstar annihilator on all nine targets")
  polynomials={"originalHStar":hs,"fieldAnnihilator":ann}
  power=Xi;blocks=[]
  for k in range(25):blocks.append(power);power=J*power
  Krylov=h.join(*blocks)
  check((Krylov.nrows(),Krylov.ncols())==(315,225),"all nine by25 original columns")
  km=h.solve_span(Krylov,J*Krylov)
  check(h.zero(km["residual"]),"all225 original parameter products belong to the full target span")
  MT=km["basis"];rm=MT.ncols()
  ja=h.solve_span(MT,J*MT)
  check(h.zero(ja["residual"]) and J*MT==MT*ja["solution"],"full original target field module")
  JM=ja["solution"]
  project,Jq,qrows,qfree,qinv,qUf=h.quotient(J,U16)
  Free=project(Krylov)
  fb=h.solve_span(Free,Jq*Free)
  check(h.zero(fb["residual"]),"full225 free-quotient closure")
  F=fb["basis"];rf=F.ncols()
  fa=h.solve_span(F,Jq*F)
  check(h.zero(fa["residual"]) and Jq*F==F*fa["solution"],"all free image parameter products")
  JF=fa["solution"]
  check(rf<=25,"field free rank cannot exceed the paid rational rank25 in the true flat quotient")
  expected_free_char=h.mul([0,0,1],[z*pow(hs[-1]%31,-1,31)%31 for z in hs])
  free_char=poly_coeff(JF.charpoly()) if rf else [1]
  primitive=(rf==25)
  if primitive:check(free_char==expected_free_char,"the exact primitive free25 characteristic polynomial")
  wh=h.solve_span(h.join(U16,Krylov),J*h.join(U16,Krylov))
  check(h.zero(wh["residual"]),"true torsion plus all target columns is invariant")
  W=wh["basis"];zw=h.solve_span(W,J*W);JW=zw["solution"]
  check(h.zero(zw["residual"]) and J*W==W*JW and W.ncols()==16+rf,"complete combined field subspace and free dimension")
  w_targets=h.solve_span(W,Xi);w_tors=h.solve_span(W,U16)
  check(h.zero(w_targets["residual"]) and h.zero(w_tors["residual"]),"original target and true16 coordinates in combined space")
  TX=w_targets["solution"];TU=w_tors["solution"]
  whole_char=poly_coeff(J.charpoly());whole_min=poly_coeff(J.minpoly());wchar=JW.charpoly()
  unit,factors=wchar.factor()
  check(int(unit)==1,"monic combined characteristic factorization")
  product=[1]
  for fac,e in factors:
   for _ in range(int(e)):product=h.mul(product,poly_coeff(fac))
  check(product==poly_coeff(wchar),"complete combined characteristic factor multiplication")
  wmin=poly_coeff(JW.minpoly())
  eye=nmod_mat([[int(i==j) for j in range(W.ncols())] for i in range(W.ncols())],31)
  zero=nmod_mat(W.ncols(),W.ncols(),31);projector_sum=zero
  primary=[];primary_data=[];target_primary_char=[1];target_primary_min=[1];target_minimum_generators=0
  for fac,e in factors:
   tick();f=poly_coeff(fac);n=fac.degree();power_f=[1]
   whole_remainder=whole_char[:];multiplicity=0
   while True:
    q,r=h.divmodp(whole_remainder,f)
    if r:break
    multiplicity+=1;whole_remainder=q
   check(multiplicity>=int(e),"combined factor occurs in the whole original characteristic")
   for _ in range(multiplicity):power_f=h.mul(power_f,f)
   comp,rem=h.divmodp(whole_char,power_f);check(not rem,"whole original primary exact division")
   projector_poly=h.divmodp(h.mul(comp,h.inverse_mod(comp,power_f)),whole_char)[1]
   reduced=h.divmodp(projector_poly,wmin)[1]
   Pi=h.action(reduced,JW,eye)
   check(Pi*Pi==Pi and JW*Pi==Pi*JW,"actual full primary projector identities")
   for old in primary_data:check(Pi*old["projector"]==zero and old["projector"]*Pi==zero,"distinct actual primary projectors")
   projector_sum+=Pi
   Xw=Pi*TX;Uw=Pi*TU
   X=W*Xw;U=W*Uw
   check(J*X==W*(JW*Xw) and J*U==W*(JW*Uw),"all original315 primary transports")
   up=h.solve_span(U,J*U);check(h.zero(up["residual"]),"complete true torsion primary closure")
   Up=up["basis"];td=Up.ncols()
   Y=project(X);xblocks=[];z=X;fblocks=[];v=Y
   for k in range(25):
    xblocks.append(z);fblocks.append(v);z=J*z;v=Jq*v
   XK=h.join(*xblocks);FK=h.join(*fblocks)
   local_target=h.solve_span(XK,J*XK)
   check(h.zero(local_target["residual"]),"complete primary target module closure")
   local_free=h.solve_span(FK,Jq*FK)
   check(h.zero(local_free["residual"]),"complete primary free image closure")
   local_dimension=local_target["basis"].ncols();free_dimension=local_free["basis"].ncols()
   check(local_dimension>=free_dimension,"primary target/free quotient dimensions")
   if local_dimension:
    MB=local_target["basis"];ma=h.solve_span(MB,J*MB);MJ=ma["solution"]
    check(h.zero(ma["residual"]) and J*MB==MB*MJ,"full primary target action")
    MI=nmod_mat([[int(i==j) for j in range(local_dimension)] for i in range(local_dimension)],31)
    nullity=local_dimension-h.action(f,MJ,MI).rank()
    check(nullity%n==0,"irreducible-field generator count is integral")
    minimum_generators=nullity//n
    mc=poly_coeff(MJ.charpoly());mn=poly_coeff(MJ.minpoly())
   else:minimum_generators=0;mc=[1];mn=[1]
   check(0<=minimum_generators<=9,"complete primary target image is generated by the original nine targets")
   target_minimum_generators=max(target_minimum_generators,minimum_generators)
   target_primary_char=h.mul(target_primary_char,mc);target_primary_min=h.mul(target_primary_min,mn)
   center=(-f[0])%31 if n==1 else None
   target_coordinate_rank=Y.rank()
   item={"factorCoefficientsAscending":f,"degree":n,"wholeCharacteristicMultiplicity":multiplicity,
         "wholePrimaryDimension":n*multiplicity,"combinedPrimaryDimension":Pi.rank(),
         "completeTorsionResidueDimension":td,"targetFieldDimension":local_dimension,"targetCharacteristicCoefficientsAscending":mc,
         "targetMinimalCoefficientsAscending":mn,"minimumFieldPolynomialGenerators":minimum_generators,
         "freeTargetDimension":free_dimension,"constantNineFreeRank":target_coordinate_rank,
         "targetPrimary":mr(X),"trueTorsionPrimary":mr(U),"all25PowersPrimary":mr(XK),
         "freeAll25PowersPrimary":mr(FK),"all315OriginalPrimaryProductsVerified":True,
         "fullOriginalCRTProjector":projector_poly,"center":center}
   if center in (1,2):
    expected_td=2 if center==1 else 14
    expected_exp=[1,2] if center==1 else [1,2,2,2,2,3,3,4,4,4,4,5,5,6]
    check(td==expected_td and free_dimension<=1,"complete paid root coefficient-torsion component and rational free bound")
    local_primitive=(free_dimension==target_coordinate_rank==1)
    selected=next((j for j in range(9) if not h.zero(h.sub(Y,range(Y.nrows()),[j]))),None)
    if local_primitive:
     check(selected is not None and h.zero(Jq*Y-center*Y),"one complete primitive free Hensel line")
     qf=h.solve_span(h.sub(Y,range(Y.nrows()),[selected]),Y)
     check(h.zero(qf["residual"]),"all original nine free residues use the selected actual target")
     c=poly_coeff(fac)
     hs_value=sum(hs[i]*center**i for i in range(len(hs)))
     hs_derivative=sum(i*hs[i]*center**(i-1) for i in range(1,len(hs)))
     check(hs_value%31==0 and hs_value%(31**2)!=0 and hs_derivative%31!=0,"the genuine simple Hensel factor of original hstar")
     item["primitiveTargetLabel"]=LABELS[selected]
     item["constantFreeCoordinatesInSelectedTarget"]=rows(qf["solution"])[0]
     item["originalHStarValue"]=str(hs_value)
     item["originalHStarValueOver31Modulo31"]=(hs_value//31)%31
     item["originalHStarDerivativeModulo31"]=hs_derivative%31
    residual_dimension=local_dimension-free_dimension
    check(residual_dimension<=td,"complete target intersection with actual coefficient torsion")
    item.update(primitiveFreeLineQualified=local_primitive,
                torsionIntersectionResidueDimension=residual_dimension,
                torsionIntersectionEqualsCompleteComponent=local_primitive and residual_dimension==td,
                completeComponentDExponents=expected_exp,
                explicitFiniteDGeneratingFamilySize=9 if center==1 else 27,
                generatingFamilyIsNotClaimedToBeIndependent=True)
   else:
    check(td==0,"the full coefficient torsion has only roots1 and2")
   primary.append(item)
   primary_data.append({"factor":f,"projector":Pi,"originalTargets":X,"originalTorsion":U,
                        "targetKrylov":XK,"freeKrylov":FK})
  check(projector_sum==eye,"complete primary projector sum on all true16 and all225 targets")
  target_char=poly_coeff(JM.charpoly());target_min=poly_coeff(JM.minpoly())
  check(target_primary_char==target_char and target_primary_min==target_min,
        "all primary characteristic and minimal polynomials reconstruct the complete original target action")
  check(target_minimum_generators<=9,"complete whole field target generator bound")
  joint_m_generator_interval=[max(8,target_minimum_generators),9]
  intersections=rm-rf
  check(0<=intersections<=16,"global complete torsion-intersection residue dimension")
  free_labels=[{"sourceColumn":i,"targetLabel":LABELS[i%9],"powerOfS":i//9} for i in fb["indices"]]
  summaries={"completeOriginalKrylovColumns":225,"originalTargetFieldDimension":rm,
   "originalTargetFieldCharacteristic":target_char,"originalTargetFieldMinimum":target_min,
   "completeTorsionResidueCharacteristic":poly_coeff(J16.charpoly()),
   "completeTorsionResidueMinimum":poly_coeff(J16.minpoly()),
   "minimumFieldPolynomialGeneratorsOfTargetImage":target_minimum_generators,
   "originalJointMMinimumDPolynomialGeneratorInterval":joint_m_generator_interval,
   "originalJointMHasExactlyNineGenerators":target_minimum_generators==9,
   "combinedTargetAndTrueTorsionDimension":W.ncols(),"freeTargetDimensionModuloFullTrue16":rf,
   "paidRationalFreeDimension":25,"completePrimitiveFreeLatticeQualified":primitive,
   "freeCharacteristicCoefficientsAscending":free_char,"expectedRationalCharacteristicReduction":expected_free_char,
   "freeMinimalCoefficientsAscending":poly_coeff(JF.minpoly()) if rf else [1],
   "selectedOriginalFreeBasisColumns":free_labels,"wholeStateCharacteristic":whole_char,"wholeStateMinimum":whole_min,
   "globalTargetTorsionIntersectionResidueDimension":intersections,
   "targetContainsCompleteCoefficientTorsionByNakayama":primitive and intersections==16,
   "originalKrylovMatrix":mr(Krylov),"fieldTargetBasis":mr(MT),"fieldTargetAction":mr(JM),
   "trueFreeQuotientKrylov":mr(Free),"freeImageBasis":mr(F),"freeImageAction":mr(JF),
   "completeCombinedBasis":mr(W),"completeCombinedAction":mr(JW),"primary":primary,
   "all225OriginalParameterProductsVerified":True,"all315CoordinatesRetained":True,
   "all505OriginalFreeChecksVerified":True,"actualTrue16OriginalSourceBasisUsed":True,
   "extraWholeFieldDefectDirectionNotIdentifiedWithOriginalFreeCarrier":True,
   "highPCoordinatesAndCompleteJointMStructureNotClaimed":True,
   "qualificationFailureIsNotNonmembership":True,"full210NotRecomputed":True}
  payload={"binding":binding,"inputIdentity":semantic,"polynomials":polynomials,"true16":rows(U16),
   "true16Action":rows(J16),"originalNineTargets":rows(Xi),"all225OriginalKrylov":rows(Krylov),
   "targetFieldBasis":rows(MT),"targetFieldAction":rows(JM),"freeQuotientProjectionPivotRows":qrows,
   "freeQuotientRemainingRows":qfree,"freeQuotientInverse":rows(qinv),"freeQuotientLower":rows(qUf),
   "freeImageBasis":rows(F),"freeImageAction":rows(JF),"combinedBasis":rows(W),"combinedAction":rows(JW),
   "primaryMatrices":[{k:(rows(v) if hasattr(v,"nrows") else v) for k,v in z.items()} for z in primary_data],
   "summary":summaries}
  pp=a.out/"complete-original-joint-m-qualification-data.json";atomic_json(pp,payload)
  summaries["temporaryCompleteDataFile"]=identity(pp)
  rec["parameters"]["final"]=summaries;rec["status"]="completed";save();return 0
 except BudgetStop as e:
  rec["status"]="budget-checkpoint";rec["errorType"]=type(e).__name__;rec["error"]=str(e);rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};save();return 75
 except BaseException as e:
  rec["status"]="failed";rec["errorType"]=type(e).__name__;rec["error"]=str(e);rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};save();return 1
 finally:
  signal.setitimer(signal.ITIMER_REAL,0);save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
if __name__=="__main__":raise SystemExit(main())
