#!/usr/bin/env python3
"""Exact original low20 coordinates from a verified original UI checkpoint.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The parent constants run was terminated.  Only its independently pinned,
two-sided-verified original 11 by 11 inverse is consumed.  This program does
not reconstruct the physical model, C, CZ or the sixteen cubic source arrays.
Those identities are the previously proved original E20 kernel/source theorem.
New arithmetic is precisely the original projected20 by 50 system, its exact
faithful rational60 solve, all1000 E products and all400 selected identities.
Large phases are streamed to deterministic gzip; candidates are never success.
"""
from __future__ import annotations
import argparse, gc, gzip, hashlib, importlib.util, itertools, json, os
import resource, signal, sys, time, zlib
from pathlib import Path

sys.set_int_max_str_digits(0)
FORMAT = "r150-original-low20-projection-only-exact-v1"
P, PLACE_ROOT = 127, 100
MATCHED = [52565262336, 6080833024, -43931504, 3725]
PARENT_FORMAT = "r150-original-low-commutator-twenty-exact-constants-v2"
PARENT_SOURCE = {"bytes":33539,
    "sha256":"d9d98bc379e322e9c212b7ad7721399ec8b1bab9970a2755700338f7053d47da"}
PARENT_BINDING = "672c57bb68079e9a49cff09e4a7fdadd7b89dc017927913ee0d35261a08d2522"
PARENT_MANIFEST = {"bytes":3418,
    "sha256":"c7b010a2c16e2896782eaaad74f977d00e640af6c8142b623474a015b948bf9b"}
UI_KEY = "original-inverse-11-abb2c7a819cd"
UI_LABEL = "same original eleven quadratic sources"
UI_INPUT_SHA = "028c02fb11bb2acc1717b0c7d221edd91a0e1d6ab2fee34c4fe133d7207e89d5"
UI_DESCRIPTOR = {"path":UI_KEY+".json.gz","bytes":1473718,
    "sha256":"ec9d6e2758ae835f027fd0c3d8da26945814cb3599949057f96ac542b78300e6",
    "logicalBytes":2975996,
    "logicalSha256":"31bf451e26193eed026feba6bf00a71a9394a78ecce0a7571aea661380b76c05"}
KEEP = [(1,4),(2,3),(2,4),(3,4)]
LOW_IDS = [10*j+k for j in range(4) for k in range(1,6)]
PROJECTED_KEY = "all50-original-low-source-projections"
CANDIDATE_KEY = "candidate-exact-original-low20-coordinates"
FINAL_KEY = "complete-exact-original-low20-products"

class Budget(Exception): pass

def need(ok, message):
    if not ok: raise ValueError(message)

def canon(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")

def sha(raw): return hashlib.sha256(raw).hexdigest()

def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}

def exact(p,desc):
    a=identity(p)
    need(all(a[k]==desc[k] for k in ("bytes","sha256")),"whole exact file "+Path(p).name)
    return a

def atomic(p,raw):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp")
    with t.open("wb") as f:
        f.write(raw);f.flush();os.fsync(f.fileno())
    os.replace(t,p)

def logical_identity(p):
    h=hashlib.sha256();n=0
    with gzip.open(p,"rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b);n+=len(b)
    return {"logicalBytes":n,"logicalSha256":h.hexdigest()}

def load_whole_phase(p,desc,fmt,binding):
    exact(p,desc);ld=logical_identity(p)
    need(all(ld[k]==desc[k] for k in ld),"whole logical phase "+Path(p).name)
    with gzip.open(p,"rt",encoding="ascii") as f:obj=json.load(f)
    need(obj["format"]==fmt+"-phase" and obj["binding"]==binding,"same exact phase envelope")
    return obj["data"]

def import_helper(p):
    exact(p,PARENT_SOURCE)
    sp=importlib.util.spec_from_file_location("original_low20_pinned_exact_helper",p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    need(m.FORMAT==PARENT_FORMAT and m.MATCHED==MATCHED and m.PRIME==P and m.ROOT==PLACE_ROOT,
         "same original exact E field and paired local place")
    return m

def dictionaries(h):
    pairs=list(itertools.combinations(range(5),2))
    m2=[]
    for i,j in itertools.combinations_with_replacement(range(5),2):
        m2.append(tuple(int(k==i)+int(k==j) for k in range(5)))
    keep=[tuple(int(k==i)+int(k==j) for k in range(5)) for i,j in KEEP]
    elim=[j for j,e in enumerate(m2) if e not in keep]
    labels=[(i,j,k) for i,j in pairs for k in range(5)]
    selected=[j for j,(i,k,l) in enumerate(labels) if i==0]
    ids=[10*pairs.index((i,j))+1+k for i,j,k in labels]
    sources=[(g,k) for g in range(11) for k in range(5)]
    need(m2==h.M2 and elim==h.ELIM and KEEP==h.KEEP and labels==h.LABELS and
         selected==h.SELECTED and [ids[j] for j in selected]==LOW_IDS==h.LOW_IDS,
         "all original ordinary-monomial, alpha, low-column dictionaries")
    need(len(m2)==15 and len(elim)==11 and len(labels)==50 and len(selected)==20,
         "complete original source dictionary sizes")
    need(sources[35:]==[(g,k) for g in range(7,11) for k in range(5)],
         "R is exactly original cubic source coordinates35 through54")
    return {"quadraticMonomials":[list(e) for e in m2],"eliminatedQuadraticPositions":elim,
        "keptQuadraticPaths":[list(e) for e in KEEP],"all50LowLabels":[list(e) for e in labels],
        "all50OriginalSeedIndices":ids,"selectedLowColumns":selected,
        "selectedOriginalSeedIndices":LOW_IDS,"all55OriginalCubicSourceLabels":[list(e) for e in sources],
        "kernelProjectionOriginalColumns":list(range(35,55))}

def read_parent(a,h,d):
    mp=a.parent_out/"exact-low20-manifest.json";exact(mp,PARENT_MANIFEST)
    m=json.loads(mp.read_bytes())
    need(m["format"]==PARENT_FORMAT+"-manifest" and m["binding"]==PARENT_BINDING,
         "same actually interrupted parent with verified inverse checkpoints")
    sem=m["semantic"]
    need(sha(canon(sem))==PARENT_BINDING and sem["matchedCubic"]==MATCHED and
         sem["prime"]==P and sem["coefficientRoot"]==PLACE_ROOT and
         all(sem["source"][k]==PARENT_SOURCE[k] for k in PARENT_SOURCE) and
         sem["keptQuadraticPaths"]==d["keptQuadraticPaths"] and
         sem["kernelProjectionColumns"]==d["kernelProjectionOriginalColumns"] and
         sem["cubicUnitColumns"]==list(range(35)) and
         sem["twentyOriginalLowSeedIndices"]==LOW_IDS,
         "original source semantic binding and literal projection dictionaries")
    need("original-exact-constants" not in m["phases"] and len(m["phases"])==6,
         "retain actual parent partial scope, never a completed constants claim")
    need(m["phases"][UI_KEY]==UI_DESCRIPTOR,"exact verified UI descriptor in the interrupted parent")
    x=load_whole_phase(a.parent_out/UI_DESCRIPTOR["path"],UI_DESCRIPTOR,PARENT_FORMAT,PARENT_BINDING)
    need(x["label"]==UI_LABEL and x["dimension"]==11 and x["inputSha256"]==UI_INPUT_SHA and
         x["bothOriginalEInverseProductsVerified"] and x["bothLocalPlaceInverseProductsVerified"] and
         x["originalEProductCount"]==242 and x["faithfulRationalCoordinateCount"]==726 and
         x["determinant127"]==44 and not x.get("candidateOnly",False),
         "genuine complete original eleven-source inverse, not an unverified candidate")
    UI=h.unpack_m(x["inverse"])
    need(len(UI)==11 and all(len(row)==11 for row in UI),"UI rows are eleven G sources; columns are eleven eliminated monomials")
    for i in range(11):
        for j in range(11):need(h.pack_e(UI[i][j])==x["inverse"][i][j],"canonical original E inverse coordinates")
    need(int(h.nmod_mat(h.bar_m(UI),P).det())==pow(44,-1,P),"same original inverse determinant at the legal place")
    del x,m;gc.collect()
    return UI,{"manifest":{**identity(mp)},"binding":PARENT_BINDING,"verifiedInverse":UI_DESCRIPTOR,
        "originalInputMatrixSha256":UI_INPUT_SHA,"originalConstantsStageComplete":False,
        "reusedVerifiedInverseEProducts":242,"newInverseProductsClaimed":0}

class EValue:
    __slots__=("value",)
    def __init__(self,v):self.value=v

def wrapped(A):return [[EValue(v) for v in row] for row in A]

def projected(F,UI,d):
    m2=[tuple(e) for e in d["quadraticMonomials"]];pos={e:i for i,e in enumerate(m2)}
    elim=d["eliminatedQuadraticPositions"];epos={j:k for k,j in enumerate(elim)}
    alpha=[]
    for j in range(15):
        alpha.append([UI[g][epos[j]] if j in epos else F.zero for g in range(11)])
    need(all(alpha[j][g]==(UI[g][epos[j]] if j in epos else F.zero)
             for j in range(15) for g in range(11)),"all165 literal original alpha source-index entries")
    for i,j in KEEP:
        e=tuple(int(k==i)+int(k==j) for k in range(5))
        need(all(v==F.zero for v in alpha[pos[e]]),"all four kept ordinary quadratic alpha columns are zero")
    Z=[[F.zero]*50 for _ in range(20)]
    for c,(i,j,k) in enumerate(d["all50LowLabels"]):
        ik=pos[tuple(int(a==i)+int(a==k) for a in range(5))]
        jk=pos[tuple(int(a==j)+int(a==k) for a in range(5))]
        for g in range(7,11):
            for ell in range(5):
                Z[5*(g-7)+ell][c]=F.sub(alpha[ik][g] if ell==j else F.zero,
                                               alpha[jk][g] if ell==i else F.zero)
    return Z

def main():
    ap=argparse.ArgumentParser()
    for name in ("exact-helper","parent-out","out"):ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--through",choices=("projected","candidate","final"),default="final")
    ap.add_argument("--seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=1024)
    a=ap.parse_args()
    need(0<a.seconds<=900 and 256<=a.memory_mib<=2048,"bounded original projected exact computation")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();deadline=started+a.seconds
    own=identity(Path(__file__));code=1;state=None;mp=a.out/"exact-low20-projection-manifest.json"
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
        "originalParentConstantsCompleted":False,"newPhysicalModelReconstruction":False,
        "newCOrCZProducts":False,"newParameterPolynomialProducts":False,"unitIdealClaim":False}}
    h=None;binding=None
    def tick():
        if time.monotonic()+8>=deadline:raise Budget("whole original projected exact phase budget")
    def alarm(sig=None,frame=None):raise Budget("actual original projected exact wall budget")
    def event(name,**kw):
        rec["parameters"]["lastEvent"]=name
        if state is not None and name in state["phases"]:rec["parameters"]["lastWholePhase"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},separators=(",",":")),flush=True)
    def phase(name,data):
        tick();p=a.out/(name+".json.gz");tmp=p.with_name(p.name+".tmp")
        logical=hashlib.sha256();count=0
        def encode(v):
            if isinstance(v,EValue):return h.pack_e(v.value)
            raise TypeError("unapproved phase object "+type(v).__name__)
        enc=json.JSONEncoder(sort_keys=True,separators=(",",":"),ensure_ascii=True,default=encode)
        try:
            with tmp.open("wb") as physical:
                with gzip.GzipFile(filename="",mode="wb",compresslevel=1,mtime=0,fileobj=physical) as gz:
                    for piece in enc.iterencode({"format":FORMAT+"-phase","binding":binding,"data":data}):
                        b=piece.encode("ascii");logical.update(b);count+=len(b);gz.write(b)
                physical.flush();os.fsync(physical.fileno())
            os.replace(tmp,p)
        except BaseException:
            try:tmp.unlink()
            except FileNotFoundError:pass
            raise
        desc={**identity(p),"logicalBytes":count,"logicalSha256":logical.hexdigest()}
        state["phases"][name]=desc;atomic(mp,canon(state));return desc
    def read(name):
        desc=state["phases"][name]
        return load_whole_phase(a.out/desc["path"],desc,FORMAT,binding)
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","fixed exact and gzip runtime")
        h=import_helper(a.exact_helper);F=h.EField();d=dictionaries(h)
        semantic={"format":FORMAT,"source":own,"exactHelper":PARENT_SOURCE,"matchedCubic":MATCHED,
            "prime":P,"coefficientRoot":PLACE_ROOT,"parentFormat":PARENT_FORMAT,
            "parentBinding":PARENT_BINDING,"parentManifest":PARENT_MANIFEST,
            "verifiedOriginalUI":UI_DESCRIPTOR,"originalUIInputSha256":UI_INPUT_SHA,
            "dictionaries":d,"projectionFormula":"RZ_(g,ell;ij,k)=delta_ell,j alpha_ik,g - delta_ell,i alpha_jk,g",
            "sourceTheorem":"R kills original cubic border support0..34; R restricted to ker(C) is injective; canonical original source is E-linear",
            "newArithmetic":"exact original projected20x50 and faithful rational60 solve;1000 E products;400 selected identities"}
        binding=sha(canon(semantic));rec["binding"]=binding
        state={"format":FORMAT+"-manifest","binding":binding,"semantic":semantic,"phases":{}}
        if mp.exists():
            state=json.loads(mp.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and
                 state["semantic"]==semantic,"same exact independent projection continuation")
            need(set(state["phases"])<=set((PROJECTED_KEY,CANDIDATE_KEY,FINAL_KEY)),"only declared whole original phases")
        rec["parameters"]["runtime"]={"python":sys.version.split()[0],"pythonFlint":flint.__version__,"zlib":zlib.ZLIB_VERSION}
        UI,parent=read_parent(a,h,d);rec["parameters"]["actualParent"]=parent
        event("verified-original-UI-loaded",sourceIndexEntries=121)
        if PROJECTED_KEY not in state["phases"]:
            tick();Z=projected(F,UI,d);del UI;gc.collect()
            A=[[row[j] for j in d["selectedLowColumns"]] for row in Z]
            det=int(h.nmod_mat(h.bar_m(A),P).det())
            need(det!=0,"actual same original projected twenty source unit")
            data={"projectedCoordinates":wrapped(Z),"dictionaries":d,"twentyUnitDeterminant127":det,
                "all165OriginalAlphaIndicesVerified":True,"allFourKeptAlphaColumnsZero":True,
                "literalProjectionEntries":1000,"newCProducts":0,"newCZProducts":0,
                "verifiedOriginalUIDescriptor":UI_DESCRIPTOR,"originalUIInputSha256":UI_INPUT_SHA}
            phase(PROJECTED_KEY,data);del data;event(PROJECTED_KEY,twentyUnitDeterminant127=det)
        else:
            del UI;gc.collect();data=read(PROJECTED_KEY)
            need(data["dictionaries"]==d and data["all165OriginalAlphaIndicesVerified"] and
                 data["allFourKeptAlphaColumnsZero"] and data["literalProjectionEntries"]==1000 and
                 data["verifiedOriginalUIDescriptor"]==UI_DESCRIPTOR and data["originalUIInputSha256"]==UI_INPUT_SHA,
                 "same completed literal original projections")
            Z=h.unpack_m(data["projectedCoordinates"]);det=data["twentyUnitDeterminant127"];del data;gc.collect()
            need(len(Z)==20 and all(len(row)==50 for row in Z),"complete projected source dimensions")
            A=[[row[j] for j in d["selectedLowColumns"]] for row in Z]
            need(int(h.nmod_mat(h.bar_m(A),P).det())==det!=0,"same original twenty-source unit")
            event(PROJECTED_KEY+"-reused",twentyUnitDeterminant127=det)
        if a.through=="projected":
            rec["status"]="completed-prefix";code=0;return code
        if FINAL_KEY in state["phases"]:
            result=read(FINAL_KEY)
            need(result["projectedPhase"]==state["phases"][PROJECTED_KEY] and
                 result["coordinatePhase"]==state["phases"][CANDIDATE_KEY] and
                 result["all1000OriginalEProductsVerified"] and result["all3000FaithfulRationalCoordinatesVerified"] and
                 result["all400SelectedIdentityCoordinatesVerified"] and result["all1000LocalPlaceProductsVerified"],
                 "complete original product certificate with exact matrix descriptors")
            # Even a completed reuse rechecks every complete referenced file.
            candidate=read(CANDIDATE_KEY)
            need(candidate["candidateOnly"] and candidate["projectedPhase"]==state["phases"][PROJECTED_KEY],
                 "same coordinate payload subsequently verified by the final phase")
            del candidate,result;gc.collect();event(FINAL_KEY+"-reused")
            rec["status"]="completed";code=0;return code
        tick();Ab=h.nmod_mat(h.bar_m(A),P);Zb=h.nmod_mat(h.bar_m(Z),P);LB=Ab.inv()*Zb
        QA=h.rational_regular_matrix(F,A);QB=h.rational_columns(Z)
        if CANDIDATE_KEY not in state["phases"]:
            event("faithful-rational60-solve-start",rightHandSides=50)
            X=QA.solve(QB,algorithm="dixon")
            L=[[(h.fmpq_poly([X[3*i+k,j] for k in range(3)]),int(LB[i,j])) for j in range(50)] for i in range(20)]
            candidate={"coordinates":wrapped(L),"candidateOnly":True,"exactProductsVerified":False,
                "projectedPhase":state["phases"][PROJECTED_KEY],"selectedLowColumns":d["selectedLowColumns"],
                "rationalRows":60,"rightHandSides":50,"twentyUnitDeterminant127":det,
                "method":"faithful original E regular representation; exact rational Dixon solve; paired same-unit local solution"}
            phase(CANDIDATE_KEY,candidate);del candidate;event(CANDIDATE_KEY)
        else:
            candidate=read(CANDIDATE_KEY)
            need(candidate["candidateOnly"] and not candidate["exactProductsVerified"] and
                 candidate["projectedPhase"]==state["phases"][PROJECTED_KEY] and
                 candidate["selectedLowColumns"]==d["selectedLowColumns"] and
                 candidate["rationalRows"]==60 and candidate["rightHandSides"]==50 and
                 candidate["twentyUnitDeterminant127"]==det,"same honest full original coordinate candidate")
            L=h.unpack_m(candidate["coordinates"]);del candidate;gc.collect()
            need(len(L)==20 and all(len(row)==50 for row in L),"complete exact coordinate shape")
            need(h.bar_m(L)==[[int(LB[i,j]) for j in range(50)] for i in range(20)],
                 "candidate carries the same original local-unit solution, never arbitrary field lifting")
            X=h.rational_columns(L);event(CANDIDATE_KEY+"-reused")
        if a.through=="candidate":
            rec["status"]="completed-unverified-candidate";code=0;return code
        tick();event("all-original-projected-products-start",exactEProducts=1000)
        need(QA*X==QB,"all3000 faithful rational coordinates of all1000 original E products")
        need(Ab*LB==Zb,"all1000 original local-place projected products")
        for a0,j in enumerate(d["selectedLowColumns"]):
            for i in range(20):need(L[i][j]==(F.one if i==a0 else F.zero),"all400 exact selected source identity coordinates")
        result={"projectedPhase":state["phases"][PROJECTED_KEY],"coordinatePhase":state["phases"][CANDIDATE_KEY],
            "all50OriginalLowLabels":d["all50LowLabels"],"selectedOriginalSeedIndices":LOW_IDS,
            "twentyUnitDeterminant127":det,"all1000OriginalEProductsVerified":True,
            "all3000FaithfulRationalCoordinatesVerified":True,"all1000LocalPlaceProductsVerified":True,
            "all400SelectedIdentityCoordinatesVerified":True,"allFiftyOriginalLowSourcesAccountedFor":True,
            "fieldCoefficientsLifted":False,"newPhysicalModelReconstruction":False,
            "newCProducts":0,"newCZProducts":0,"newFull55Products":0,"newParameterPolynomialProducts":0,
            "sourceTheorem":"both original source sides lie in ker(C); their exact R projections agree; R is injective there; canonical correction is E-linear",
            "ordinaryBModuleLowGenerators":20,"originalFullSeedBound":76,"completeTwoRoundColumnBound":670,
            "newHighCommutatorDeletionClaim":False,"unitIdealClaim":False}
        phase(FINAL_KEY,result);event(FINAL_KEY,exactEProducts=1000,selectedIdentityCoordinates=400)
        rec["status"]="completed";code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        rec["parameters"]["elapsedSeconds"]=time.monotonic()-started
        rec["parameters"]["peakRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["exitCode"]=code
        rec["parameters"]["completePhases"]={} if state is None else state["phases"]
        if mp.exists():rec["parameters"]["manifest"]=identity(mp)
        atomic(a.out/"exact-low20-projection-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)

if __name__=="__main__":raise SystemExit(main())
