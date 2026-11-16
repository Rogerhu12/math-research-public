#!/usr/bin/env python3
"""Exact original low20 coordinates using two four-by-four E inverses.

Author: Astra-ISP-789f / normal_annihilator, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

This independent algorithm consumes the same verified original eleven-source
inverse.  It never restarts the terminated rational60 solve.  Its two rational12
solves, two-sided inverse products, original block reconstruction, and final
1000 E / 3000 rational / 400 selected products are separate whole phases.
No physical model, cubic C, CZ, or parameter-polynomial reconstruction is claimed.
"""
from __future__ import annotations
import argparse, gc, gzip, hashlib, importlib.util, itertools, json, os
import resource, signal, sys, time, zlib
from pathlib import Path

sys.set_int_max_str_digits(0)
FORMAT="r150-original-low20-two-four-exact-v1"
PROJECTION_SOURCE={"bytes":21178,"sha256":"a77cf71a3e3c4dcbd4b68f3f4d99f98a64bd4f64394f46507c8c42cc5aecf48f"}
PROJECTED_KEY="all50-original-low-source-projections"
FACTORS_KEY="complete-two-original-four-factorizations"
CANDIDATE_KEY="candidate-exact-original-low20-coordinates"
FINAL_KEY="complete-exact-original-low20-products"
LABEL_M="original A0 four-column unit"
LABEL_B="original four coupled kernel columns"

class Budget(Exception): pass

def need(ok,msg):
    if not ok:raise ValueError(msg)

def canon(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")

def sha(b):return hashlib.sha256(b).hexdigest()

def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}

def exact(p,d):
    a=identity(p);need(all(a[k]==d[k] for k in ("bytes","sha256")),"whole exact source "+Path(p).name)
    return a

def atomic(p,b):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);t=p.with_name(p.name+".tmp")
    with t.open("wb") as f:f.write(b);f.flush();os.fsync(f.fileno())
    os.replace(t,p)

def import_projection(p):
    exact(p,PROJECTION_SOURCE)
    sp=importlib.util.spec_from_file_location("original_verified_projection_functions",p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
    need(m.FORMAT=="r150-original-low20-projection-only-exact-v1","same literal original projection functions")
    return m

class EValue:
    __slots__=("value",)
    def __init__(self,v):self.value=v

def wrapped(A):return [[EValue(v) for v in row] for row in A]

def inverse_key(label):return "original-inverse-04-"+sha(label.encode("ascii"))[:12]

def main():
    ap=argparse.ArgumentParser()
    for k in ("projection-helper","exact-helper","parent-out","out"):
        ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--through",choices=("factors","candidate","final"),default="final")
    ap.add_argument("--seconds",type=float,default=180)
    ap.add_argument("--memory-mib",type=int,default=768)
    a=ap.parse_args()
    need(0<a.seconds<=900 and 256<=a.memory_mib<=2048,"bounded independent two-four computation")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True);started=time.monotonic();deadline=started+a.seconds
    own=identity(__file__);state=None;binding=None;h=None;p=None;code=1
    mp=a.out/"exact-low20-two-four-manifest.json"
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
        "oldRational60SolveRepeated":False,"originalParentConstantsCompleted":False,
        "newPhysicalModelReconstruction":False,"newCOrCZProducts":False,
        "newParameterPolynomialProducts":False,"unitIdealClaim":False}}
    allowed={PROJECTED_KEY,FACTORS_KEY,CANDIDATE_KEY,FINAL_KEY}
    for label in (LABEL_M,LABEL_B):
        allowed.update((inverse_key(label),inverse_key(label)+"-candidate"))
    def tick():
        if time.monotonic()+8>=deadline:raise Budget("whole two-four exact phase budget")
    def alarm(sig=None,frame=None):raise Budget("actual two-four wall budget")
    def event(name,**kw):
        rec["parameters"]["lastEvent"]=name
        if state is not None and name in state["phases"]:rec["parameters"]["lastWholePhase"]=name
        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-started,
            "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**kw},
            separators=(",",":")),flush=True)
    def phase(name,data):
        need(name in allowed,"declared whole phase only");tick()
        f=a.out/(name+".json.gz");tmp=f.with_name(f.name+".tmp")
        lh=hashlib.sha256();n=0
        def encode(x):
            if isinstance(x,EValue):return h.pack_e(x.value)
            raise TypeError("unapproved exact phase object "+type(x).__name__)
        enc=json.JSONEncoder(sort_keys=True,separators=(",",":"),ensure_ascii=True,default=encode)
        try:
            with tmp.open("wb") as out:
                with gzip.GzipFile(filename="",mode="wb",compresslevel=1,mtime=0,fileobj=out) as gz:
                    for piece in enc.iterencode({"format":FORMAT+"-phase","binding":binding,"data":data}):
                        b=piece.encode("ascii");lh.update(b);n+=len(b);gz.write(b)
                out.flush();os.fsync(out.fileno())
            os.replace(tmp,f)
        except BaseException:
            try:tmp.unlink()
            except FileNotFoundError:pass
            raise
        desc={**identity(f),"logicalBytes":n,"logicalSha256":lh.hexdigest()}
        state["phases"][name]=desc;atomic(mp,canon(state));return desc
    def read(name):
        d=state["phases"][name]
        return p.load_whole_phase(a.out/d["path"],d,FORMAT,binding)
    def inverse_reader(name):
        return read(name) if name in state["phases"] else None
    def inverse_writer(name,data):
        return phase(name,data)
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        import flint
        need(tuple(sys.version_info[:3])==(3,12,14) and flint.__version__=="0.9.0","exact pinned arithmetic and gzip runtime")
        p=import_projection(a.projection_helper);h=p.import_helper(a.exact_helper)
        d=p.dictionaries(h)
        sem={"format":FORMAT,"source":own,"projectionHelper":PROJECTION_SOURCE,
            "exactHelper":p.PARENT_SOURCE,"parentFormat":p.PARENT_FORMAT,
            "parentBinding":p.PARENT_BINDING,"parentManifest":p.PARENT_MANIFEST,
            "verifiedOriginalUI":p.UI_DESCRIPTOR,"originalUIInputSha256":p.UI_INPUT_SHA,
            "matchedCubic":p.MATCHED,"prime":p.P,"coefficientRoot":p.PLACE_ROOT,"dictionaries":d,
            "method":"A0 t_j=y_j; -sum A_j t_j=y0; two original4x4 E residue-unit inverses, each faithful rational12",
            "sourceTheorem":"same original RZ; R injective on ker(C); original canonical correction E-linear",
            "newProducts":"two4 inverse both sides;400 original block coordinates;1000 E;3000 rational;400 selected"}
        binding=sha(canon(sem));rec["binding"]=binding
        state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"phases":{}}
        if mp.exists():
            state=json.loads(mp.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and
                 state["semantic"]==sem and set(state["phases"])<=allowed,"same frozen independent complete-phase continuation")
        F=h.EField(inverse_reader=inverse_reader,inverse_writer=inverse_writer,progress=event,tick=tick)
        UI,parent=p.read_parent(a,h,d);rec["parameters"]["actualParent"]=parent
        rec["parameters"]["runtime"]={"python":sys.version.split()[0],"pythonFlint":flint.__version__,"zlib":zlib.ZLIB_VERSION}
        event("verified-original-UI-loaded",sourceIndexEntries=121)
        if PROJECTED_KEY not in state["phases"]:
            Z=p.projected(F,UI,d);del UI;gc.collect()
            A=[[row[j] for j in d["selectedLowColumns"]] for row in Z]
            det=int(h.nmod_mat(h.bar_m(A),p.P).det())
            need(det!=0,"same original projected20 source unit")
            phase(PROJECTED_KEY,{"projectedCoordinates":wrapped(Z),"dictionaries":d,
                "twentyUnitDeterminant127":det,"all165OriginalAlphaIndicesVerified":True,
                "allFourKeptAlphaColumnsZero":True,"literalProjectionEntries":1000,
                "verifiedOriginalUIDescriptor":p.UI_DESCRIPTOR,"originalUIInputSha256":p.UI_INPUT_SHA})
            event(PROJECTED_KEY,twentyUnitDeterminant127=det)
        else:
            del UI;gc.collect();x=read(PROJECTED_KEY)
            need(x["dictionaries"]==d and x["all165OriginalAlphaIndicesVerified"] and
                 x["allFourKeptAlphaColumnsZero"] and x["literalProjectionEntries"]==1000 and
                 x["verifiedOriginalUIDescriptor"]==p.UI_DESCRIPTOR and
                 x["originalUIInputSha256"]==p.UI_INPUT_SHA,"same whole original projected coordinates")
            Z=h.unpack_m(x["projectedCoordinates"]);det=x["twentyUnitDeterminant127"];del x;gc.collect()
            need(len(Z)==20 and all(len(r)==50 for r in Z),"whole original20x50")
            A=[[r[j] for j in d["selectedLowColumns"]] for r in Z]
            need(int(h.nmod_mat(h.bar_m(A),p.P).det())==det!=0,"same projected20 original unit")
            event(PROJECTED_KEY+"-reused")
        if FINAL_KEY in state["phases"]:
            r=read(FINAL_KEY)
            need(r["projectedPhase"]==state["phases"][PROJECTED_KEY] and
                 r["factorPhase"]==state["phases"][FACTORS_KEY] and
                 r["coordinatePhase"]==state["phases"][CANDIDATE_KEY] and
                 r["all1000OriginalEProductsVerified"] and r["all3000FaithfulRationalCoordinatesVerified"] and
                 r["all400SelectedIdentityCoordinatesVerified"] and
                 r["all1000LocalPlaceProductsVerified"],"whole final original products")
            # Recheck every referenced complete payload, including both inverse candidates.
            for key in state["phases"]:
                x=read(key);del x
            event(FINAL_KEY+"-reused");rec["status"]="completed";code=0;return code
        # Rows are (g,ell), g=0..3,ell=0..4. Selected columns are (j,k),
        # j=1..4,k=0..4. This reconstructs the original block shape in all400 slots.
        A0=[[A[5*g+1][k] for k in range(5)] for g in range(4)]
        Aj=[None]+[[[F.neg(A[5*g][5*(j-1)+k]) for k in range(5)] for g in range(4)] for j in range(1,5)]
        for g in range(4):
            for ell in range(5):
                for j in range(1,5):
                    for k in range(5):
                        expected=F.neg(Aj[j][g][k]) if ell==0 else A0[g][k] if ell==j else F.zero
                        need(A[5*g+ell][5*(j-1)+k]==expected,"all400 literal original selected block coordinates")
        if FACTORS_KEY not in state["phases"]:
            tick();cols=None
            for cs in itertools.combinations(range(5),4):
                M=[[A0[g][k] for k in cs] for g in range(4)]
                if int(h.nmod_mat(h.bar_m(M),p.P).det())!=0:cols=list(cs);break
            need(cols is not None,"actual original A0 rank4")
            free=next(k for k in range(5) if k not in cols)
            M=[[A0[g][k] for k in cols] for g in range(4)]
            MI,prM=F.invert(M,LABEL_M)
            L=[[F.zero]*4 for _ in range(5)]
            for j,k in enumerate(cols):L[k]=list(MI[j])
            eta=[F.zero]*5;eta[free]=F.one
            for j,k in enumerate(cols):eta[k]=F.neg(F.dot(MI[j],[A0[g][free] for g in range(4)]))
            al=F.matrix(A0,L)
            need(all(al[g][j]==(F.one if g==j else F.zero) for g in range(4) for j in range(4)),
                 "all16 original A0 right-inverse products")
            need(all(F.dot(row,eta)==F.zero for row in A0) and eta[free]==F.one,
                 "all4 original A0 kernel products and fixed free coordinate")
            B=[[F.dot(Aj[j][g],eta) for j in range(1,5)] for g in range(4)]
            BI,prB=F.invert(B,LABEL_B)
            phase(FACTORS_KEY,{"projectedPhase":state["phases"][PROJECTED_KEY],
                "originalA0PivotColumns":cols,"originalA0FreeColumn":free,
                "rightInverse":wrapped(L),"kernelVector":[EValue(v) for v in eta],
                "coupledMatrix":wrapped(B),"coupledInverse":wrapped(BI),
                "originalBlockCoordinatesVerified":400,"allA0RightInverseProductsVerified":16,
                "allA0KernelProductsVerified":4,"kernelFreeCoordinate":1,
                "MInversePhase":state["phases"][inverse_key(LABEL_M)],
                "BInversePhase":state["phases"][inverse_key(LABEL_B)],
                "MProfile":prM,"BProfile":prB,"bothFourInversesOriginalEProducts":64,
                "bothFourInversesRationalCoordinateProducts":192})
            event(FACTORS_KEY,pivotColumns=cols,freeColumn=free,
                firstDeterminant127=prM["determinant127"],coupledDeterminant127=prB["determinant127"])
        else:
            x=read(FACTORS_KEY)
            need(x["projectedPhase"]==state["phases"][PROJECTED_KEY] and
                 x["originalBlockCoordinatesVerified"]==400 and
                 x["allA0RightInverseProductsVerified"]==16 and x["allA0KernelProductsVerified"]==4 and
                 x["MInversePhase"]==state["phases"][inverse_key(LABEL_M)] and
                 x["BInversePhase"]==state["phases"][inverse_key(LABEL_B)] and
                 x["bothFourInversesOriginalEProducts"]==64,"same complete two-four factorization")
            cols=x["originalA0PivotColumns"];free=x["originalA0FreeColumn"]
            need(len(cols)==4 and sorted(cols)==cols and set(cols)|{free}==set(range(5)),
                 "same original four-column and free-index partition")
            L=h.unpack_m(x["rightInverse"]);eta=[h.unpack_e(v) for v in x["kernelVector"]]
            B=h.unpack_m(x["coupledMatrix"]);BI=h.unpack_m(x["coupledInverse"]);del x
            for key in (inverse_key(LABEL_M),inverse_key(LABEL_B)):
                inv=read(key);need(inv["bothOriginalEInverseProductsVerified"] and
                    inv["bothLocalPlaceInverseProductsVerified"] and inv["dimension"]==4 and
                    inv["originalEProductCount"]==32,"both originally verified complete4 inverses");del inv
            event(FACTORS_KEY+"-reused")
        if a.through=="factors":
            rec["status"]="completed-prefix";code=0;return code
        if CANDIDATE_KEY not in state["phases"]:
            tick();event("structured-original-fifty-right-hand-sides-start")
            Lam=[[F.zero]*50 for _ in range(20)]
            for c in range(50):
                tick()
                y=[[Z[5*g+ell][c] for g in range(4)] for ell in range(5)]
                v=[None]+[[F.dot(row,y[j]) for row in L] for j in range(1,5)]
                r=[F.add(y[0][g],F.total(F.dot(Aj[j][g],v[j]) for j in range(1,5))) for g in range(4)]
                lam=[F.neg(F.dot(row,r)) for row in BI]
                for j in range(1,5):
                    for k in range(5):Lam[5*(j-1)+k][c]=F.add(v[j][k],F.mul(lam[j-1],eta[k]))
                if c%10==9:event("structured-original-right-hand-sides",completedColumns=c+1)
            phase(CANDIDATE_KEY,{"coordinates":wrapped(Lam),"candidateOnly":True,
                "exactProductsVerified":False,"projectedPhase":state["phases"][PROJECTED_KEY],
                "factorPhase":state["phases"][FACTORS_KEY],"selectedLowColumns":d["selectedLowColumns"],
                "rightHandSides":50,"method":"two original4 E inverses and exact coupled block formula",
                "oldRational60SolveRepeated":False})
            event(CANDIDATE_KEY)
        else:
            x=read(CANDIDATE_KEY)
            need(x["candidateOnly"] and not x["exactProductsVerified"] and
                 x["projectedPhase"]==state["phases"][PROJECTED_KEY] and
                 x["factorPhase"]==state["phases"][FACTORS_KEY] and
                 x["selectedLowColumns"]==d["selectedLowColumns"] and x["rightHandSides"]==50 and
                 not x["oldRational60SolveRepeated"],"same complete honest two-four candidate")
            Lam=h.unpack_m(x["coordinates"]);del x
            need(len(Lam)==20 and all(len(row)==50 for row in Lam),"whole structured original20x50 candidate")
            event(CANDIDATE_KEY+"-reused")
        if a.through=="candidate":
            rec["status"]="completed-unverified-candidate";code=0;return code
        tick();event("all-original-projected-products-start",exactEProducts=1000)
        QA=h.rational_regular_matrix(F,A);QX=h.rational_columns(Lam);QZ=h.rational_columns(Z)
        need(QA*QX==QZ,"all3000 original faithful rational coordinates of all1000 E products")
        Ab=h.nmod_mat(h.bar_m(A),p.P);Lb=h.nmod_mat(h.bar_m(Lam),p.P);Zb=h.nmod_mat(h.bar_m(Z),p.P)
        need(Ab*Lb==Zb,"all1000 original local-place products")
        for j,c in enumerate(d["selectedLowColumns"]):
            for i in range(20):need(Lam[i][c]==(F.one if i==j else F.zero),"all400 selected original exact identities")
        f=read(FACTORS_KEY)
        result={"projectedPhase":state["phases"][PROJECTED_KEY],"factorPhase":state["phases"][FACTORS_KEY],
            "coordinatePhase":state["phases"][CANDIDATE_KEY],"all50OriginalLowLabels":d["all50LowLabels"],
            "selectedOriginalSeedIndices":p.LOW_IDS,"twentyUnitDeterminant127":det,
            "originalA0PivotColumns":f["originalA0PivotColumns"],"originalA0FreeColumn":f["originalA0FreeColumn"],
            "firstFourDeterminant127":f["MProfile"]["determinant127"],
            "coupledFourDeterminant127":f["BProfile"]["determinant127"],
            "bothFourInversesOriginalEProducts":64,"bothFourInversesRationalCoordinateProducts":192,
            "all400OriginalSelectedBlockCoordinatesVerified":True,
            "all1000OriginalEProductsVerified":True,"all3000FaithfulRationalCoordinatesVerified":True,
            "all1000LocalPlaceProductsVerified":True,"all400SelectedIdentityCoordinatesVerified":True,
            "allFiftyOriginalLowSourcesAccountedFor":True,"fieldCoefficientsLifted":False,
            "oldRational60SolveRepeated":False,"newPhysicalModelReconstruction":False,
            "newCProducts":0,"newCZProducts":0,"newFull55Products":0,"newParameterPolynomialProducts":0,
            "sourceTheorem":"both original sides lie in ker(C); exact R projections agree; R injective; canonical source correction E-linear",
            "ordinaryBModuleLowGenerators":20,"originalFullSeedBound":76,
            "completeTwoRoundColumnBound":670,"newHighCommutatorDeletionClaim":False,"unitIdealClaim":False}
        del f;phase(FINAL_KEY,result);event(FINAL_KEY,exactEProducts=1000,selectedIdentityCoordinates=400)
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
        atomic(a.out/"exact-low20-two-four-receipt.json",canon(rec))
        print(json.dumps(rec,separators=(",",":")),flush=True)

if __name__=="__main__":raise SystemExit(main())
