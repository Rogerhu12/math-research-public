#!/usr/bin/env python3
"""Full original weight10 Macaulay; exact sparse input, whole-column state,
independent scalar certificates and original ten/eighteen/seventeen sources.

Author: Astra-ISP-789f / literature_audit, with /root. 2026-11-16.
AI-assisted: GPT-6 Astra Pro.
All arrays, raw receipts, certificates and checkpoints remain temporary.
No Singular basis, finite candidate rank or incomplete prefix proves a result.
"""
from __future__ import annotations
import argparse,gc,gzip,hashlib,importlib.util,json,os,resource,shutil,signal,struct,subprocess,sys,time
from collections import Counter
from pathlib import Path
sys.set_int_max_str_digits(0)

FORMAT="r150-original-weight10-full-macaulay127-v1"
NATIVE_FORMAT="r150-original-weight10-full-macaulay127-native-v1"
CHECKER_FORMAT="r150-original-weight10-full-ordinary-verifier127-v1"
PREPARED_FORMAT="r150-original-delta-weight10-homogeneous127-runtime-parent-v1"
P=127;M=77276;N=13808;G=200;TERMS=8037189;TARGET_TERMS=2604;INPUT_BYTES=73145375
ROW_WEIGHTS=(0,)+(2,)*5+(4,)*4
VARIABLE_WEIGHTS=(1,)*6+(2,)*6
COUNTS=(1,6,27,92,273,714,1715,3816,8007,15938,30381)
PINS={
 "prepared_source":"433e8942e30cde475bd6e7f13df43b4a6765a876dac495553de5fe6a53fd001f",
 "model_source":"4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4",
 "chart_source":"ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3",
 "producer_source":"20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa",
 "vector_helper":"54b082184273e254495be8e1eb788e6569e8ca9cc4b83a1a5d4330304e9d4246",
 "native_source":"0a53cd6179904977404db186dbc88bf1a04339c2bf4569b90a9007744f0a50df",
 "checker_source":"bf10b7ba832123c6208e8e7b4cf2a6e63ba1cfbd2f17cbf6d26e4f4c8a53f295",
 "bitplane_header":"03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3",
 "controls_driver":"fc5992ab257f3b6f535033a4fb6500af419ab84a8bc64d3f633de87bbfc1912c"}
HEADER_NAME="2026-11-15-r150-original-f127-bitplane-789f.hpp"
NATIVE_STATE_MAX=1030000000
CHECKER_STATE_MAX=244+8*M
MAX_JSON_PHASE=134217728
MAX_LOGICAL_PHASE=536870912

class Budget(Exception):pass
def need(v,s):
    if not v:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for q in iter(lambda:f.read(1048576),b""):h.update(q)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
    got=identity(p);need(got["bytes"]==d["bytes"] and got["sha256"]==d["sha256"],"whole exact file "+Path(p).name);return got
def atomic(p,body):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+".tmp")
    with tmp.open("wb") as f:f.write(body);f.flush();os.fsync(f.fileno())
    os.replace(tmp,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def module(p,expected,name):
    need(identity(p)["sha256"]==expected,"exact frozen source "+name)
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def monomials():
    ans=[]
    def rec(i,left,code,out):
        if i==12:
            if left==0:out.append(code)
            return
        for e in range(left//VARIABLE_WEIGHTS[i]+1):
            rec(i+1,left-e*VARIABLE_WEIGHTS[i],code+(e<<(5*i)),out)
    for w in range(11):
        out=[];rec(0,w,0,out);out.sort()
        need(len(out)==COUNTS[w] and len(set(out))==len(out),"all original weighted monomials")
        ans.append(out)
    return ans
def exponent(code):return tuple((code>>(5*i))&31 for i in range(12))
def pack_terms(terms):
    out=bytearray(9*len(terms))
    for j,(code,c) in enumerate(terms):struct.pack_into("<QB",out,9*j,code,c)
    return bytes(out)
def native_state_header(path,binding,input_sha):
    with Path(path).open("rb") as f:
        h=f.read(200)
        need(len(h)==200 and h[:8]==b"R15WS101","whole original native state header")
        version,p,m,n,g,cursor,rank,nw=struct.unpack_from("<8I",h,8)
        need((version,p,m,n,g,nw)==(1,127,M,N,G,(M+31)//32) and 0<=rank<=cursor<=N,"full native state dimensions")
        need(h[40:104].decode()==binding and h[104:168].decode()==input_sha,"same native state binding/input")
        size=200+N+rank*(16+7*nw*4)+rank*(rank-1)//2
        need(Path(path).stat().st_size==size<=NATIVE_STATE_MAX,"entire exact native state byte count")
        return {"completeColumns":cursor,"rank":rank,"bytes":size}
def verifier_state_header(path,binding,input_sha,certificate_sha,kind):
    with Path(path).open("rb") as f:h=f.read(244)
    need(len(h)==244 and h[:8]==b"R15WV101","whole independent progress header")
    version,p,m,n,k,rank,cursor,q=struct.unpack_from("<8I",h,8)
    need((version,p,m,n,k)==(1,127,M,N,kind) and 0<=rank<=N and 0<=cursor<=N,"full independent progress dimensions")
    need(h[40:104].decode()==binding and h[104:168].decode()==input_sha and h[168:232].decode()==certificate_sha,"same independent progress identities")
    count=struct.unpack_from("<I",h,240)[0]
    need(count==(M if kind==2 else 0) and Path(path).stat().st_size==244+8*count<=CHECKER_STATE_MAX,"whole independent progress accumulator")
    return {"verifiedColumns":cursor,"kind":kind,"rank":rank,"separatingRow":q}
def certificate_data(path,binding,input_sha):
    raw=Path(path).read_bytes()
    need(len(raw)>=176 and raw[:8]==b"R15WC101","whole original certificate protocol")
    version,p,m,n,kind,rank,cursor,q,readout,count=struct.unpack_from("<10I",raw,8)
    need((version,p,m,n,cursor)==(1,127,M,N,N) and rank<=N,"all original columns before certificate")
    need(raw[48:112].decode()==binding and raw[112:176].decode()==input_sha,"same exact original certificate identities")
    need((kind==1 and q<M and readout==1 and count==M) or
         (kind==2 and q==2**32-1 and readout==0 and count==N),"entire certificate kind")
    need(len(raw)==176+4*rank+count,"whole original certificate EOF")
    pivots=struct.unpack_from("<%dI"%rank,raw,176) if rank else ()
    need(list(pivots)==sorted(set(pivots)) and all(z<M for z in pivots),"all original pivot coordinates")
    values=raw[176+4*rank:];need(all(z<127 for z in values),"all original certificate coefficients")
    if kind==1:
        allowed=set(pivots)|{q};need(q not in pivots and values[q]!=0 and all(not z or i in allowed for i,z in enumerate(values)),"literal left witness support")
    return {"kind":kind,"rank":rank,"separatingRow":q,"readout":readout},values


def audit_native_state(path,desc,binding,input_sha,rowkeys,labels,tick):
    """Stream the complete original state; only one seven-plane column in RAM.
    The simultaneous row/column arrival order cancels both permutation signs.
    The original selected minor therefore has determinant product(factor) mod127.
    """
    info=native_state_header(path,binding,input_sha);whole=hashlib.sha256()
    rh=hashlib.sha256();ch=hashlib.sha256();rk=hashlib.sha256();cl=hashlib.sha256()
    seen=set();previous=-1;det=1;rank=info["rank"];cursor=info["completeColumns"];nw=(M+31)//32
    def take(f,n):
        b=f.read(n);need(len(b)==n,"every byte of full original native state");whole.update(b);return b
    with Path(path).open("rb") as f:
        take(f,200);classification=take(f,N)
        need(sum(z==1 for z in classification)==rank and
             all(z in (1,2) if j<cursor else z==0 for j,z in enumerate(classification)),
             "all original prefix columns classified and no future source")
        for k in range(rank):
            if k%64==0:tick(12)
            p,j,factor,length=struct.unpack("<4I",take(f,16))
            need(p<M and p not in seen and previous<j<cursor and classification[j]==1 and
                 1<=factor<127 and length==k,"all unique original source/pivot/factor labels")
            seen.add(p);previous=j
            raw=take(f,7*nw*4);view=memoryview(raw)
            planes=[int.from_bytes(view[4*nw*b:4*nw*(b+1)],"little") for b in range(7)]
            before=(1<<p)-1
            need(all(q&before==0 and q>>M==0 for q in planes),"all earlier output coordinates and all literal padding zero")
            need(sum(((q>>p)&1)<<b for b,q in enumerate(planes))==1,"every actual original pivot normalized to one")
            redundant=planes[0]
            for q in planes[1:]:redundant&=q
            need(redundant==0,"every full output field entry canonical, no redundant127")
            dag=take(f,k);need(max(dag,default=0)<127,"every preceding source-DAG coefficient canonical")
            det=det*factor%127
            rh.update(struct.pack("<I",p));ch.update(struct.pack("<I",j))
            rk.update(struct.pack("<Q",rowkeys[p]));cl.update(struct.pack("<IQ",*labels[j]))
        need(f.read(1)==b"","whole native state EOF")
    need(Path(path).stat().st_size==desc["bytes"]==info["bytes"] and whole.hexdigest()==desc["sha256"],
         "entire independently streamed original state SHA")
    need(det!=0,"nonzero original selected minor")
    return {"state":desc,"inputSHA256":input_sha,"completeOriginalColumns":cursor,"selectedRank":rank,
            "allOriginalInputsProcessed":cursor==N,"allRankOriginalSourceLabelsDistinct":True,
            "allRankOriginalOutputPivotsDistinct":True,"allRankFactorsNonzero":True,
            "allFullBitplanesCanonicalAndNormalized":True,"allEarlierCoordinatesAndPaddingZero":True,
            "allPrecedingDAGShapesAndCoefficientsVerified":True,
            "rowAndColumnOrder":"both in original pivot-arrival order; simultaneous permutation signs cancel",
            "originalSelectedMinorDeterminant127":det,"minorFormula":"product of the actual original normalization factors modulo127",
            "originalOutputRowIndicesSHA256":rh.hexdigest(),"originalSourceColumnIndicesSHA256":ch.hexdigest(),
            "originalOutputCoordinateCodesSHA256":rk.hexdigest(),"originalSourceLabelsSHA256":cl.hexdigest(),
            "stateWholeSHA256":whole.hexdigest(),"characteristicZeroConclusionClaimed":False}

def main():
    ap=argparse.ArgumentParser()
    for key in tuple(PINS)+("prepared-out","model-out","mean-out","weight8-out","producer-out","out"):
        ap.add_argument("--"+key.replace("_","-"),type=Path,required=(key=="out"))
    ap.add_argument("--through",choices=("controls","input","columns","verify","final"),default="input")
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=2048)
    ap.add_argument("--cxx",default="g++")
    ap.add_argument("--controls-out",type=Path)
    a=ap.parse_args()
    if a.through=="controls":
        need(30<=a.seconds<=300 and 256<=a.memory_mib<=2048,"bounded independent controls")
        need(all(getattr(a,k) is not None for k in ("native_source","checker_source","bitplane_header","controls_driver")),"only four frozen controls source files required")
        resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
        c=module(a.controls_driver,PINS["controls_driver"],"full_weight10_controls_only")
        return c.execute(a)
    need(all(getattr(a,k.replace("-","_")) is not None for k in tuple(PINS)+("prepared-out","model-out","mean-out","weight8-out","producer-out")),"full run requires every actual original parent and helper")
    need(120<=a.seconds<=1800 and 1024<=a.memory_mib<=6144,"bounded complete Macaulay consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    start=time.monotonic();deadline=start+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
    mp=a.out/"full-weight10-macaulay-manifest.json";rp=a.out/"full-weight10-macaulay-receipt.json"
    own=identity(Path(__file__));state=None;binding="";new_units=0;child=None;code=1
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
         "through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
         "originalIdealNonmembershipClaimed":False,"positiveOriginalSourceClaimed":False,
         "characteristicZeroConclusion":False,"stages":[]}}
    def remaining():return deadline-time.monotonic()
    def tick(reserve=12):
        if remaining()<reserve:raise Budget("whole verified phase budget")
    def alarm(*unused):raise Budget("complete original consumer deadline")
    def event(name,**kw):
        print(canon({"phase":name,"elapsedSeconds":time.monotonic()-start,**kw}).decode(),flush=True)
    def flush():
        if state is not None:save_json(mp,state)
    def checked(desc):
        p=a.out/desc["path"];exact(p,desc);return p
    def phase(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data})
        need(len(raw)<=MAX_LOGICAL_PHASE,"whole bounded child phase")
        dest=a.out/(name+".json.gz");packed=gzip.compress(raw,compresslevel=1,mtime=0)
        need(len(packed)<=MAX_JSON_PHASE,"whole bounded compressed child phase")
        atomic(dest,packed);desc={**identity(dest),"logicalBytes":len(raw),"logicalSha256":sha(raw)}
        return desc
    def phase_data(desc):
        p=checked(desc);need(desc["bytes"]<=MAX_JSON_PHASE and desc["logicalBytes"]<=MAX_LOGICAL_PHASE,"whole bounded child phase descriptor")
        raw=gzip.decompress(p.read_bytes())
        need(len(raw)==desc["logicalBytes"] and sha(raw)==desc["logicalSha256"],"whole child logical hash")
        z=json.loads(raw);need(z["format"]==FORMAT+"-phase" and z["binding"]==binding,"same complete child phase")
        return z["data"]
    def next_generation():
        state["generation"]+=1;need(state["generation"]<10000,"bounded immutable output generations");flush();return state["generation"]
    def run_process(label,argv,timeout):
        nonlocal child
        tick(20);generation=next_generation()
        log=a.out/("%04d-%s.log"%(generation,label));e={"name":label,"arguments":list(map(str,argv)),"status":"running"}
        rec["parameters"]["stages"].append(e);begin=time.monotonic();budget=False
        signal.setitimer(signal.ITIMER_REAL,0)
        try:
            with log.open("wb") as f:
                child=subprocess.Popen(list(map(str,argv)),stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
                last=begin
                while child.poll() is None:
                    now=time.monotonic()
                    if now-begin>timeout or remaining()<10:
                        budget=True;os.killpg(child.pid,signal.SIGTERM)
                        try:child.wait(timeout=3)
                        except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
                        break
                    if now-last>=30:event(label+"-running",childSeconds=now-begin);last=now
                    time.sleep(.2)
                rc=child.returncode
        finally:
            child=None
            if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
        e.update(exitCode=rc,outerBudgetStop=budget,elapsedSeconds=time.monotonic()-begin,log=identity(log),status="budget" if budget else "returned")
        need(not budget,"child failed to return a whole bound checkpoint before its outer deadline")
        return rc,e,log
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        need(tuple(sys.version_info[:3])==(3,12,14),"pinned Python3.12.14")
        import flint
        need(flint.__version__=="0.9.0","pinned python-flint0.9.0")
        for k,h in PINS.items():need(identity(getattr(a,k))["sha256"]==h,"every frozen complete source "+k)
        old=module(a.prepared_source,PINS["prepared_source"],"full_weight10_paid_runtime")
        v=module(a.vector_helper,PINS["vector_helper"],"full_weight10_original_vectors")
        prep_mp=a.prepared_out/"delta-weight10-manifest.json";prep_rp=a.prepared_out/"delta-weight10-receipt.json"
        prepared_identity=identity(prep_mp);prepared_receipt=identity(prep_rp)
        prepared=json.loads(prep_mp.read_bytes());pr=json.loads(prep_rp.read_bytes())
        pb=prepared["binding"]
        need(prepared["format"]==PREPARED_FORMAT+"-manifest" and sha(canon(prepared["semantic"]))==pb,"whole prepared200 semantic binding")
        need(prepared["semantic"]["source"]["sha256"]==PINS["prepared_source"] and
             all(prepared["semantic"][key]==PINS[arg] for key,arg in (
              ("modelSourceSHA256","model_source"),("chartSourceSHA256","chart_source"),
              ("producerSourceSHA256","producer_source"),("verifierSourceSHA256","vector_helper"))),"all prepared original source identities")
        need(pr["format"]==PREPARED_FORMAT and pr["binding"]==pb and pr["status"]=="completed-prefix" and
             pr["parameters"]["through"]=="prepare" and pr["source"]["sha256"]==PINS["prepared_source"],"actual completed prepare receipt, no partial or empty candidate")
        need(pr["parameters"]["manifest"]==prepared_identity and pr["parameters"]["completePreparedColumns"]==200,"actual prepare points to this complete manifest")
        for k in ("allCompletedOriginalParentHashesVerified","all200OriginalSourceProductsInheritedFromCompleteParent",
                  "all17OriginalTransportsRechecked","all24MeanCoordinatesRechecked","bothLiteralAdjugatesRechecked","all200OriginalSourceWeightsVerified"):
            need(pr["parameters"][k] is True,"actual complete original prepare gate "+k)
        need(pr["parameters"]["originalInputColumns"]==G and pr["parameters"]["originalInputTerms"]==TERMS and
             pr["parameters"]["targetTerms"]==TARGET_TERMS and len(prepared["prepared"])==G,"all200/8037189/2604 actual inputs")
        exact(a.producer_out/"complete210-sources-manifest.json",old.PARENT_MANIFEST)
        prod_mp=json.loads((a.producer_out/"complete210-sources-manifest.json").read_bytes())
        prod_rp=json.loads((a.producer_out/"complete210-sources-receipt.json").read_bytes())
        actual_parent=identity(a.producer_out/"complete210-sources-receipt.json")
        need(prepared["semantic"]["parentReceipt"]==actual_parent and prod_mp["binding"]==old.PARENT_BINDING and
             sha(canon(prod_mp["semantic"]))==old.PARENT_BINDING and prod_rp["binding"]==old.PARENT_BINDING and prod_rp["status"]=="completed","same actual complete210 execution")
        need(prod_rp["source"]["sha256"]==PINS["producer_source"] and
             prod_rp["parameters"]["manifest"]=={"path":"complete210-sources-manifest.json",**old.PARENT_MANIFEST} and
             prod_rp["parameters"]["completeModel"]==prod_mp["phases"]["complete-original210-source-model"]==old.PARENT_FINAL,"all paid complete210 mathematical identities")
        for k in ("all104NewOriginal18ProductsVerified","all104TenVectorsVerified","all210OriginalSourcesVerified"):
            need(prod_rp["parameters"][k] is True,"complete210 original gate "+k)
        full=old.read_phase(a.producer_out,old.PARENT_FINAL,old.PARENT_FORMAT,old.PARENT_BINDING)
        need(full["allColumnCount"]==210 and len(full["parentColumns"])==106 and len(full["newColumns"])==104 and
             full["all106ParentSourcesVerified"] and full["all104NewTenVectorsVerified"] and
             full["all104NewOriginal18ProductsVerified"] and full["all104NewBellSourceCoefficientsZero"],"entire complete210 final phase")
        refs=prepared["originalReferences"]
        need(len(refs)==G and Counter(r["weight"] for r in refs)=={5:6,6:20,7:30,8:40,9:24,10:80},"complete Gamma200 source weights")
        # Rebuild the literal selected dictionary from the paid final210 object.
        literal=[];deleted=[]
        for rr in full["parentColumns"]:
            fmt,bb=old.OLD[rr["parent"]];need((rr["format"],rr["binding"])==(fmt,bb),"same old original source phase")
            if rr["kind"]=="original-seed":
                sid=rr["seedIndex"]
                if 106<=sid<116:deleted.append(sid);continue
                need(sid in old.LOW or sid in old.HIGH or 100<=sid<106,"only original nonBell seeds")
                weight=5 if sid>=100 else 6 if sid in old.LOW else 8
            elif rr["kind"]=="mean-first-image":weight=7
            else:need(rr["kind"]=="commutator-first-image","entire original first-image dictionary");weight=8
            literal.append({"origin":rr,"weight":weight,"kind":"old"})
        need(deleted==list(range(106,116)) and len(literal)==96,"only ten literal Bell columns deleted")
        for rr in full["newColumns"]:
            job=rr["literalSource"]
            need(prod_mp["phases"][job["phaseKey"]]==rr["descriptor"] and tuple(job["orderedOperators"]) in old.KEEP,"every new ordered source path")
            need((job["family"]=="mean" and 100<=job["originalSeedIndex"]<106 and job["weight"]==9) or
                 (job["family"]=="commutator" and job["originalSeedIndex"] in old.LOW and job["weight"]==10),"all new original mean/commutator labels")
            literal.append({"kind":"new","weight":job["weight"],"origin":{"parent":"producer","format":old.PARENT_FORMAT,"binding":old.PARENT_BINDING,"descriptor":rr["descriptor"],"literalSource":job}})
        need(literal==refs and all(d["originalReference"]==refs[i] for i,d in enumerate(prepared["prepared"])),"exact original200 label sequence, no omitted zero or duplicate")
        controls_actual=None;controls_manifest=None
        if a.controls_out is not None:
            cmp=a.controls_out/"full-weight10-controls-manifest.json";crp=a.controls_out/"full-weight10-controls-receipt.json"
            cmid=identity(cmp);crid=identity(crp);cm=json.loads(cmp.read_bytes());cr=json.loads(crp.read_bytes())
            cf="r150-original-weight10-full-macaulay127-controls-v1"
            need(cm["format"]==cf+"-manifest" and sha(canon(cm["semantic"]))==cm["binding"] and
                 cm["semantic"]["source"]["sha256"]==PINS["controls_driver"] and
                 cm["semantic"]["sourceSHA256"]=={k:PINS[k] for k in ("native_source","checker_source","bitplane_header")},
                 "same complete standalone controls sources and semantic binding")
            need(cr["format"]==cf and cr["binding"]==cm["binding"] and cr["status"]=="completed" and
                 cr["source"]["sha256"]==PINS["controls_driver"] and cr["parameters"]["manifest"]==cmid and
                 cr["parameters"]["compiled"]==cm["compiled"] and cr["parameters"]["controls"]==cm["controls"] and
                 cr["parameters"]["allFrozenCppCompiled"] and cr["parameters"]["allNewNativeAndIndependentControlsVerified"],
                 "actual complete standalone controls receipt")
            qq=cm["controls"]
            need(qq["native"]["allComplete"] and qq["native"]["checkpointRoundtrip"] and
                 qq["native"]["oldExhaustiveChecks"]==244990 and qq["native"]["signedScalarChecks"]==2048256 and
                 qq["native"]["tinyOriginalProducts"]==43 and qq["ordinary"]["allComplete"] and
                 qq["ordinary"]["ordinaryChecks"]==93412,"all standalone controls gates")
            for k in ("nativeLog","ordinaryLog"):exact(a.controls_out/qq[k]["path"],qq[k])
            for k in ("native","checker"):exact(a.controls_out/cm["compiled"][k]["path"],cm["compiled"][k])
            controls_actual={"format":cf,"binding":cm["binding"],"manifest":cmid,"receipt":crid,"sourceSHA256":PINS["controls_driver"]}
            controls_manifest=cm
        sem={"format":FORMAT,"source":own,"prime":127,"coefficientRoot":100,"sourceSHA256":PINS,
             "actualStandaloneControls":controls_actual,"actualPreparedFormat":PREPARED_FORMAT,"actualPreparedBinding":pb,"actualPreparedManifest":prepared_identity,"actualPreparedReceipt":prepared_receipt,
             "actualComplete210Receipt":actual_parent,"paidComplete210Binding":old.PARENT_BINDING,"paidComplete210Manifest":old.PARENT_MANIFEST,"paidComplete210Final":old.PARENT_FINAL,
             "shape":[M,N],"originalSources":G,"originalTerms":TERMS,"originalTargetTerms":TARGET_TERMS,
             "rowWeights":list(ROW_WEIGHTS),"variableWeights":list(VARIABLE_WEIGHTS),"sourceWeightCounts":{"5":6,"6":20,"7":30,"8":40,"9":24,"10":80},
             "rowOrder":"original component ascending, then numeric twelve-five-bit-exponent code ascending",
             "columnOrder":"all200 paid source labels, then every complementary-weight parameter monomial in ascending exponent code",
             "sparseInputProtocol":"R15WM101 complete literal rows/labels/source frames/target; little endian",
             "literalTarget":"delta14*b^2*e0","deltaSHA256":old.DELTA_SHA,"originalMeanRows":[2,3,4,5],
             "negativeGate":"independent ordinary products for every one of the 13808 original columns; original target readout1",
             "positiveGate":"all77276 scalar coordinates; complete original200 multipliers; ten/eighteen/seventeen source products and Bell gluing",
             "singleBitplaneCopy":True,"allPrecedingSourceDAGCoefficientsRetained":True,"onlyWholeOriginalColumnsCommitted":True,
             "characteristicZeroConclusion":False}
        binding=sha(canon(sem));rec["binding"]=binding
        state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"generation":0,"sourceFrames":[],"nativeAttempts":[],"verifierAttempts":[]}
        if mp.exists():
            state=json.loads(mp.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==sem,"same exact complete Macaulay continuation")
        flush()
        roots={"model":a.model_out,"mean":a.mean_out,"weight8":a.weight8_out,"producer":a.producer_out}
        mono=monomials();rowkeys=[(mon<<4)|row for row in range(10) for mon in mono[10-ROW_WEIGHTS[row]]]
        labels=[(i,mon) for i,r in enumerate(refs) for mon in mono[10-r["weight"]]]
        need(len(rowkeys)==M and len(labels)==N,"complete independent Python dictionaries")
        rowbytes=b"".join(struct.pack("<Q",r) for r in rowkeys)
        labelbytes=b"".join(struct.pack("<IQ",i,q) for i,q in labels)
        state["dictionarySHA256"]={"rows":sha(rowbytes),"allOriginalSourceLabels":sha(labelbytes)};flush()
        def source_record(i):
            rr=refs[i]["origin"];z=old.read_phase(roots[rr["parent"]],rr["descriptor"],rr["format"],rr["binding"])
            need(z["fullOriginal18ProductVerified"] and len(z["vector"])==10 and len(z["original18Source"])==18 and z["original18Source"][17]==[],"entire original18 source and exact zero Bell slot")
            if refs[i]["kind"]=="new":
                need(z["literalSource"]==rr["literalSource"] and z["allTenImageCoordinatesVerified"] and z["originalBellSourceIsZero"],"same true new source")
            elif rr["kind"]=="original-seed":
                need(z["seedIndex"]==rr["seedIndex"] and z["allTenParameterCoordinatesRetained"],"same complete original seed")
            else:
                key="meanSeedIndex" if rr["kind"]=="mean-first-image" else "commutatorSeedIndex"
                need(z[key]==rr["seedIndex"] and z["operator"]==rr["operator"],"same complete first-image source")
            for k,poly in enumerate(z["original18Source"][:17]):
                need(all(len(ee)==17 and all(type(t)is int and t>=0 for t in ee) and
                         type(c)is int and 0<c<127 and sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==refs[i]["weight"] for ee,c in poly),"every original source term at its true weight")
            return z
        def vector_from_packed(data,weight):
            need(len(data)==10,"every original output component")
            terms=[]
            for row,poly in enumerate(data):
                for ee,c in poly:
                    need(len(ee)==17 and not any(ee[12:]) and all(type(e)is int and 0<=e<=10 for e in ee) and
                         type(c)is int and 0<c<127,"all original parameter coefficients, no moment variables")
                    terms.append((v.position(row,tuple(ee[:12])),c))
            return v.normalized_terms(terms,weight)[0]
        def frame_path(i):return a.out/("original-source-frame-%03d.bin"%i)
        def read_frame(d,i,weight):
            path=checked(d);need(d["bytes"]==88+9*d["terms"]<=88+9*M,"entire bounded original sparse frame")
            raw=path.read_bytes()
            need(raw[:8]==b"R15WF101" and struct.unpack_from("<IIQ",raw,8)==(i,weight,d["terms"]) and
                 raw[24:88].decode()==binding,"same whole source frame binding and label")
            terms=tuple(struct.unpack_from("<QB",raw,88+9*j) for j in range(d["terms"]))
            need(v.normalized_terms(terms,weight)[0]==terms,"all original source frame coefficients")
            return raw[88:]
        for i,d in enumerate(state["sourceFrames"]):
            need(d["originalReference"]==refs[i] and d["preparedVector"]==prepared["prepared"][i]["vector"],"same verified original source identity")
            read_frame(d,i,refs[i]["weight"])
        for i in range(len(state["sourceFrames"]),G):
            tick();z=source_record(i);terms=vector_from_packed(z["vector"],refs[i]["weight"]);pd=prepared["prepared"][i]["vector"]
            inherited=v.read_vector(a.prepared_out/pd["path"],pd,pb)
            need(inherited==terms,"entire complete original ten-vector equals its prepared sparse input")
            raw=b"R15WF101"+struct.pack("<IIQ",i,refs[i]["weight"],len(terms))+binding.encode()+pack_terms(terms)
            atomic(frame_path(i),raw)
            state["sourceFrames"].append({**identity(frame_path(i)),"terms":len(terms),"originalReference":refs[i],"preparedVector":pd,
                                          "allTenOriginalCoordinatesMatched":True,"allOriginal18SourceWeightsVerified":True})
            new_units+=1;flush();del z,terms,inherited,raw
            if i%10==9:event("complete-original-source-frames",columns=i+1)
        need(sum(d["terms"] for d in state["sourceFrames"])==TERMS,"all8037189 original terms")

        def original_target():
            # Reconstruct the target from the original mean matrix, never from
            # the native certificate or from an elimination residual.
            m=module(a.model_source,PINS["model_source"],"full_weight10_original_model")
            ch=module(a.chart_source,PINS["chart_source"],"full_weight10_original_chart")
            exact(a.model_out/"original-parameter-module-manifest.json",old.MODEL_MANIFEST)
            mm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes())
            need(mm["format"]==old.MODEL_FORMAT+"-manifest" and mm["binding"]==old.MODEL_BINDING,"same complete physical model")
            d=mm["phases"]["complete-original-ten-parameter-action127"]
            base=m.load_gz(a.model_out/d["path"],d,old.MODEL_BINDING)
            d=mm["phases"]["complete-original-global-chart127"]
            chart=m.load_gz(a.model_out/d["path"],d,old.MODEL_BINDING)
            A=m.unpackvec(base["allOriginal18Generators"]);physical=m.unpackvec(chart["originalComposedGradients"])
            J=[m.unpackvec(row) for row in base["sourceCoordinateChange"]]
            need(len(A)==18 and len(physical)==17 and len(J)==17 and all(len(r)==17 for r in J),"all original physical generators")
            need(all(m.dot(row,physical)==A[i] for i,row in enumerate(J)),"all seventeen literal source transports")
            for k,f in enumerate(A[:17]):
                need(all(sum(ee[:6])+2*sum(ee[6:])==(4 if k<11 else 5) for ee in f.to_dict()),"all original gradient weights")
            for k,f in enumerate(physical):
                need(all(sum(ee[:6])+2*sum(ee[6:])==(4 if k<11 else 5) for ee in f.to_dict()),"all physical gradient weights")
            Y=m.CTX.gens()[:6];W=m.CTX.gens()[6:12];bell=sum((y*w for y,w in zip(Y,W)),m.ZERO)
            need(A[17]==bell-1==m.unpack(chart["originalBellMinusOne"]),"same original Bell polynomial")
            means=[m.unpackvec(row) for row in base["allSixOriginalMeanColumns"]]
            need(len(means)==6 and all(len(row)==10 for row in means),"all original mean vectors")
            for k in range(4):
                for i in range(6):
                    need(means[i][6+k]==sum((int(base["allFourOriginalMeanMatrices"][k][i][j])*Y[j] for j in range(6)),m.ZERO),"all24 literal original mean coefficients")
            block=[[means[j][6+i] for j in (2,3,4,5)] for i in range(4)]
            delta=ch.det(block,m);adj=ch.adj(block,m)
            diag=[[delta if i==j else m.ZERO for j in range(4)] for i in range(4)]
            need(delta!=0 and ch.same(ch.mm(block,adj,m),diag) and ch.same(ch.mm(adj,block,m),diag) and
                 sha(canon(m.pack(delta)))==old.DELTA_SHA,"same literal delta14 and both original adjugate products")
            target=delta*bell**2;terms=v.normalized_terms(v.from_model_vector([target]+[m.ZERO]*9),10)[0]
            need(len(terms)==TARGET_TERMS,"every literal original target term")
            return m,A,physical,J,delta,bell,target,terms
        if "targetFrame" not in state:
            tick(30);m,A,physical,J,delta,bell,target,target_terms=original_target()
            td=prepared["target"];need(v.read_vector(a.prepared_out/td["path"],td,pb)==target_terms,"original target equals completed prepared target")
            raw=b"R15WF101"+struct.pack("<IIQ",2**32-1,10,len(target_terms))+binding.encode()+pack_terms(target_terms)
            p=a.out/"original-target-frame.bin";atomic(p,raw)
            state["targetFrame"]={**identity(p),"terms":len(target_terms),"preparedVector":td,
                "literalOriginalTargetRebuilt":True,"bothAdjugatesVerified":True,"all17OriginalTransportsVerified":True}
            new_units+=1;flush()
            del A,physical,J,delta,bell,target,target_terms,raw;gc.collect()
        target_body=read_frame(state["targetFrame"],2**32-1,10)
        need(state["targetFrame"]["preparedVector"]==prepared["target"],"same full original target descriptor")
        source_header=b"".join(struct.pack("<IIQ",i,r["weight"],state["sourceFrames"][i]["terms"]) for i,r in enumerate(refs))
        header=b"R15WM101"+struct.pack("<6I2Q",1,127,M,N,G,10,TERMS,TARGET_TERMS)+binding.encode()
        need(len(header)==112,"whole literal sparse header")
        if "input" not in state:
            tick(30);dest=a.out/"full-original-weight10-input.bin";tmp=dest.with_name(dest.name+".tmp")
            with tmp.open("wb") as f:
                f.write(header);f.write(bytes(ROW_WEIGHTS+VARIABLE_WEIGHTS));f.write(rowbytes);f.write(labelbytes);f.write(source_header)
                for i,r in enumerate(refs):f.write(read_frame(state["sourceFrames"][i],i,r["weight"]))
                f.write(target_body);f.flush();os.fsync(f.fileno())
            need(tmp.stat().st_size==INPUT_BYTES,"whole73145375 sparse input bytes");os.replace(tmp,dest)
            state["input"]=identity(dest);new_units+=1;flush()
        input_path=checked(state["input"]);need(state["input"]["bytes"]==INPUT_BYTES,"complete full input size")
        # A second full comparison is against the original prepared200 binary
        # vectors, independently of the native input parser and bit-plane basis.
        if "inputAudit" not in state:
            tick(30);chain=sha(canon({"binding":binding,"input":state["input"]}));coordinate_terms=0
            with input_path.open("rb") as f:
                need(f.read(112)==header and f.read(22)==bytes(ROW_WEIGHTS+VARIABLE_WEIGHTS) and
                     f.read(len(rowbytes))==rowbytes and f.read(len(labelbytes))==labelbytes and
                     f.read(len(source_header))==source_header,"all complete original input/header dictionaries")
                for i,dd in enumerate(prepared["prepared"]):
                    tick();terms=v.read_vector(a.prepared_out/dd["vector"]["path"],dd["vector"],pb)
                    actual=f.read(9*len(terms));need(actual==pack_terms(terms),"all original input coefficients matched directly to original prepared vector "+str(i))
                    coordinate_terms+=len(terms)
                    chain=sha(bytes.fromhex(chain)+canon({"originalIndex":i,"literalTerms":len(terms),"payloadSHA256":sha(actual),"parentVector":dd["vector"]}))
                m,A,physical,J,delta,bell,target,target_terms=original_target()
                need(f.read(9*TARGET_TERMS)==pack_terms(target_terms) and f.read(1)==b"" and coordinate_terms==TERMS,"all original target coefficients and literal full input EOF")
            state["inputAudit"]={"input":state["input"],"all200OriginalBinaryVectorsCompared":True,"all200OriginalPhaseVectorsMatched":True,
                "originalTenCoordinates":2000,"originalTerms":coordinate_terms,"all77276RowsAnd13808LabelsVerified":True,
                "targetReconstructedAgainFromOriginalMeanMatrix":True,"targetTerms":TARGET_TERMS,"prefixSHA256":chain}
            new_units+=1;flush();del A,physical,J,delta,bell,target,target_terms;gc.collect()
        need(state["inputAudit"]["input"]==state["input"] and state["inputAudit"]["originalTerms"]==TERMS and
             state["inputAudit"]["all200OriginalBinaryVectorsCompared"] and state["inputAudit"]["targetReconstructedAgainFromOriginalMeanMatrix"],"complete original input audit before elimination")
        rec["parameters"].update(completeSourceFrames=len(state["sourceFrames"]),fullInput=state["input"],fullInputAudit=state["inputAudit"])
        event("complete-original-macaulay-input",rows=M,columns=N,bytes=INPUT_BYTES)
        if a.through=="input":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all original sparse input prepared and independently matched; no new elimination";code=0;return code
        if controls_actual is not None and "compiled" not in state:
            for label in ("native","checker"):
                d=controls_manifest["compiled"][label];source=a.controls_out/d["path"];exact(source,d)
                dest=a.out/d["path"];atomic(dest,source.read_bytes());dest.chmod(0o755);exact(dest,d)
            state["compiled"]=controls_manifest["compiled"];state["controls"]=controls_manifest["controls"]
            state["actualControlsParent"]=controls_actual;new_units+=1;flush()
        if "compiled" not in state:
            tick(100);build=a.out/"build";build.mkdir(exist_ok=True)
            compiler=shutil.which(a.cxx) if not Path(a.cxx).is_file() else str(a.cxx)
            need(compiler is not None,"actual C++17 compiler")
            for src,name in ((a.native_source,"native.cpp"),(a.checker_source,"checker.cpp"),(a.bitplane_header,HEADER_NAME)):
                atomic(build/name,src.read_bytes())
            vp=subprocess.run([compiler,"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=10)
            need(vp.returncode==0,"actual C++ compiler version")
            for label in ("native","checker"):
                rc,st,log=run_process("compile-"+label,[compiler,"-O3","-std=c++17","-DNDEBUG","-Wall","-Wextra",str(build/(label+".cpp")),"-I",str(build),"-o",str(a.out/(label+".bin"))],min(120,remaining()-15))
                need(rc==0,"actual complete "+label+" compilation")
            state["compiled"]={"native":identity(a.out/"native.bin"),"checker":identity(a.out/"checker.bin"),
                "compiler":{"path":str(compiler),"versionFirstLine":vp.stdout.decode(errors="replace").splitlines()[0],"versionSHA256":sha(vp.stdout)},
                "flags":["-O3","-std=c++17","-DNDEBUG","-Wall","-Wextra"]};new_units+=1;flush()
        native=checked(state["compiled"]["native"]);checker=checked(state["compiled"]["checker"])
        if "controls" not in state:
            tick(80);test_dir=a.out/("native-selftest-%04d"%(state["generation"]+1))
            rc,st,log=run_process("native-controls",[native,"--selftest",test_dir],min(60,remaining()-15))
            need(rc==0,"actual new bit-plane/DAG/checkpoint controls")
            lines=log.read_bytes().splitlines();q=json.loads(lines[-1])
            need(q["format"]==NATIVE_FORMAT+"-selftest" and q["allComplete"] and q["checkpointRoundtrip"] and
                 q["oldExhaustiveChecks"]==244990 and q["signedScalarChecks"]==2048256 and q["tinyOriginalProducts"]==43,"all new exhaustive field and tiny original-source tests")
            rc,st2,log2=run_process("ordinary-controls",[checker,"--selftest"],min(30,remaining()-15))
            need(rc==0,"actual independent scalar/dictionary controls")
            qq=json.loads(log2.read_bytes().splitlines()[-1])
            need(qq["format"]==CHECKER_FORMAT+"-selftest" and qq["allComplete"] and qq["ordinaryChecks"]==93412,"independent ordinary controls")
            state["controls"]={"native":q,"nativeLog":identity(log),"ordinary":qq,"ordinaryLog":identity(log2)};new_units+=1;flush()
        if "certificate" not in state:
            tick(180);prior="-"
            if "nativeState" in state:
                prior=str(checked(state["nativeState"]["data"]))
                hh=native_state_header(prior,binding,state["input"]["sha256"])
                need(hh==state["nativeState"]["header"],"same complete native column checkpoint")
            gen=state["generation"]+1;seconds=int(min(1800,remaining()-45));need(seconds>=120,"enough reserved time for whole-column native attempt")
            rc,st,log=run_process("whole-original-columns",[native,input_path,a.out,seconds,state["input"]["sha256"],gen,prior],seconds+20)
            raw=a.out/("native-receipt-%04d.json"%gen)
            need(raw.is_file(),"native returned an actual complete receipt");rr=json.loads(raw.read_bytes())
            need(rr["format"]==NATIVE_FORMAT and rr["binding"]==binding and rr["inputSHA256"]==state["input"]["sha256"] and
                 rr["generation"]==gen and rr["exitCode"]==rc and rr["allOriginalSparseInputTermsVerified"] and
                 rr["all77276OutputsRetained"] and rr["all13808SourceLabelsRetained"],"complete native identities and all original input gates")
            need(rr["oldExhaustiveChecks"]==244990 and rr["signedScalarChecks"]==2048256,"actual all-field native arithmetic controls")
            record={"receipt":identity(raw),"log":identity(log),"summary":rr};state["nativeAttempts"].append(record)
            if rr["stateWritten"]:
                path=a.out/rr["stateFile"];desc=identity(path);hh=native_state_header(path,binding,state["input"]["sha256"])
                need(hh["completeColumns"]==rr["completeColumns"] and hh["rank"]==rr["rank"],"complete state equals actual native prefix")
                need(rr["completeColumns"]>rr["initialCompleteColumns"] and rr["newCompleteColumns"]==rr["completeColumns"]-rr["initialCompleteColumns"],"only genuinely new whole original columns")
                state["nativeState"]={"data":desc,"header":hh,"receipt":identity(raw)};new_units+=rr["newCompleteColumns"]
            if rr["certificateWritten"]:
                need(rc==0 and rr["completeColumns"]==N and rr["allColumnsProcessed"],"certificate only after entire original matrix")
                path=a.out/rr["certificateFile"];meta,values=certificate_data(path,binding,state["input"]["sha256"])
                need(meta["kind"]==rr["certificateKind"] and meta["rank"]==rr["rank"],"same full original certificate kind")
                state["certificate"]={"data":identity(path),"metadata":meta,"nativeReceipt":identity(raw)};new_units+=1
            flush()
            need(rc in (0,75),"actual original native failure")
            if rc==75:raise Budget("actual complete-column native prefix, no full certificate yet")
            need("certificate" in state,"actual complete original certificate required")
        cert_path=checked(state["certificate"]["data"]);meta,values=certificate_data(cert_path,binding,state["input"]["sha256"])
        need(meta==state["certificate"]["metadata"],"same complete literal certificate")
        need("nativeState" in state,"complete original native state retained with every certificate")
        ns=state["nativeState"];ns_path=checked(ns["data"])
        need(ns["header"]["completeColumns"]==N and ns["header"]["rank"]==meta["rank"],"whole original state agrees with complete certificate")
        if "completeMinorAudit" not in ns:
            tick(35);audit=audit_native_state(ns_path,ns["data"],binding,state["input"]["sha256"],rowkeys,labels,tick)
            need(audit["allOriginalInputsProcessed"] and audit["selectedRank"]==meta["rank"],"complete streamed original-minor audit")
            ad=phase("complete-original-minor-state-audit",audit);ns["completeMinorAudit"]=ad;new_units+=1;flush()
        audit=phase_data(ns["completeMinorAudit"])
        need(audit["state"]==ns["data"] and audit["selectedRank"]==meta["rank"] and
             audit["allOriginalInputsProcessed"] and audit["originalSelectedMinorDeterminant127"]!=0,
             "same true full original selected minor")
        rec["parameters"]["completeOriginalMinorAudit"]={"data":ns["completeMinorAudit"],"summary":audit}
        if a.through=="columns":
            rec["status"]="completed-prefix";rec["parameters"].update(outcome="complete original target certificate candidate; independent original-column verification pending",certificate=state["certificate"]);code=0;return code
        if "ordinaryVerification" not in state:
            tick(80);prior="-"
            if "verifierState" in state:
                prior=str(checked(state["verifierState"]["data"]))
                hh=verifier_state_header(prior,binding,state["input"]["sha256"],state["certificate"]["data"]["sha256"],meta["kind"])
                need(hh==state["verifierState"]["header"],"same independently verified original-column prefix")
            gen=state["generation"]+1;seconds=int(min(1800,remaining()-25));need(seconds>=30,"independent original verifier budget")
            rc,st,log=run_process("independent-whole-original-products",
                [checker,input_path,cert_path,a.out,seconds,state["input"]["sha256"],state["certificate"]["data"]["sha256"],gen,prior],seconds+10)
            raw=a.out/("ordinary-verifier-receipt-%04d.json"%gen)
            need(raw.is_file(),"actual independent verifier receipt");rr=json.loads(raw.read_bytes())
            need(rr["format"]==CHECKER_FORMAT and rr["binding"]==binding and rr["inputSHA256"]==state["input"]["sha256"] and
                 rr["certificateSHA256"]==state["certificate"]["data"]["sha256"] and rr["generation"]==gen and
                 rr["exitCode"]==rc and rr["certificateKind"]==meta["kind"],"all exact independent verifier identities")
            record={"receipt":identity(raw),"log":identity(log),"summary":rr};state["verifierAttempts"].append(record)
            if rr["stateWritten"]:
                path=a.out/rr["stateFile"];desc=identity(path)
                hh=verifier_state_header(path,binding,state["input"]["sha256"],state["certificate"]["data"]["sha256"],meta["kind"])
                need(hh["verifiedColumns"]==rr["verifiedOriginalColumns"] and rr["newVerifiedColumns"]==rr["verifiedOriginalColumns"]-rr["initialVerifiedColumns"]>0,"only complete independent original columns")
                state["verifierState"]={"data":desc,"header":hh,"receipt":identity(raw)};new_units+=rr["newVerifiedColumns"]
            if rc==0:
                need(rr["verifiedOriginalColumns"]==N and rr["allOriginalDictionariesAndCoefficientsVerified"] and
                     rr["all13808OriginalColumnProductsVerified"] and rr["all77276TargetCoordinatesVerified"] and
                     (meta["kind"]!=1 or rr["leftOriginalTargetReadout"]==1),"entire independent original matrix and original target")
                state["ordinaryVerification"]=record;new_units+=1
            flush();need(rc in (0,75),"actual independent ordinary verifier failure")
            if rc==75:raise Budget("actual complete ordinary-column verification prefix")
        rr=state["ordinaryVerification"]["summary"];exact(a.out/state["ordinaryVerification"]["receipt"]["path"],state["ordinaryVerification"]["receipt"])
        need(rr["certificateSHA256"]==state["certificate"]["data"]["sha256"] and rr["verifiedOriginalColumns"]==N and
             rr["all13808OriginalColumnProductsVerified"] and rr["all77276TargetCoordinatesVerified"],"same actual full original verification")
        rec["parameters"].update(nativeObservedRank=meta["rank"],certificate=state["certificate"],independentOriginalVerification=state["ordinaryVerification"])
        if meta["kind"]==1:
            rec["status"]="completed-negative"
            rec["parameters"].update(outcome="delta14*b^2 is not in the same complete F127 original seventeen-gradient ideal",
                originalIdealNonmembershipClaimed=True,all13808OriginalColumnsAnnihilated=True,literalOriginalTargetReadout=1,
                negativeConclusionUsesOnlyFullOriginalLeftWitness=True,originalBellIdealNonmembershipClaimed=False,
                allHigherBellPowersExcluded=False,characteristicZeroConclusion=False)
            code=0;return code
        if a.through=="verify":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all77276 original scalar source products verified; ten/eighteen/seventeen original-source lift still pending";code=0;return code

        # Positive branch: the ordinary checker has already verified the full
        # scalar matrix, but that alone is not an original-gradient certificate.
        tick(40);m,A,physical,J,delta,bell,target,target_terms=original_target()
        need(pack_terms(target_terms)==target_body,"positive source uses the same independently rebuilt original target")
        alphas=[m.ZERO for _ in range(G)];ad=[{} for _ in range(G)]
        for j,(i,mon) in enumerate(labels):
            c=values[j]
            if c:
                ee=exponent(mon)+(0,)*5
                need(ee not in ad[i],"every original multiplier occurs once")
                ad[i][ee]=int(c)
        for i in range(G):
            alphas[i]=m.CTX.from_dict(ad[i])
            need(all(sum(ee[:6])+2*sum(ee[6:12])==10-refs[i]["weight"] and not any(ee[12:]) for ee in alphas[i].to_dict()),"all200 literal source multiplier weights")
        del ad
        work={"next":0,"got":[m.ZERO for _ in range(10)],"sigma":[m.ZERO for _ in range(18)]}
        if "positivePrefix" in state:
            old_prefix=phase_data(state["positivePrefix"]["data"])
            need(old_prefix["nextOriginalSource"]==state["positivePrefix"]["next"] and
                 0<=old_prefix["nextOriginalSource"]<=G and old_prefix["certificateSHA256"]==state["certificate"]["data"]["sha256"],"same original200 source prefix")
            work={"next":old_prefix["nextOriginalSource"],"got":m.unpackvec(old_prefix["tenVectorSum"]),"sigma":m.unpackvec(old_prefix["original18Sum"])}
            need(len(work["got"])==10 and len(work["sigma"])==18 and work["sigma"][17]==0,"all positive prefix coordinates and zero Bell source")
        def commit_positive():
            nonlocal new_units
            previous=state.get("positivePrefix",{}).get("next",0)
            if work["next"]<=previous:return
            # The entire original-column transaction has already completed.
            # Only bounded serialization is protected from the one-shot alarm.
            signal.setitimer(signal.ITIMER_REAL,0)
            try:
                data={"nextOriginalSource":work["next"],"certificateSHA256":state["certificate"]["data"]["sha256"],
                      "tenVectorSum":m.packvec(work["got"]),"original18Sum":m.packvec(work["sigma"]),
                      "allCompletedOriginalSourceIdentitiesVerified":True,"allCompletedOriginalSourceWeightsVerified":True}
                d=phase("positive-original-prefix-%03d"%work["next"],data)
                state["positivePrefix"]={"next":work["next"],"data":d};new_units+=work["next"]-previous;flush()
            finally:
                if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
        try:
            while work["next"]<G:
                tick(35);i=work["next"];alpha=alphas[i]
                if alpha:
                    z=source_record(i);vv=m.unpackvec(z["vector"]);ss=m.unpackvec(z["original18Source"])
                    need(vector_from_packed(z["vector"],refs[i]["weight"])==
                         v.read_vector(a.prepared_out/prepared["prepared"][i]["vector"]["path"],prepared["prepared"][i]["vector"],pb),
                         "positive source still has every exact original ten coefficient")
                    next_got=[x+alpha*y for x,y in zip(work["got"],vv)]
                    next_sigma=[x+alpha*y for x,y in zip(work["sigma"],ss)]
                    need(next_sigma[17]==0,"every original-column transaction preserves zero Bell source")
                    # No partial transaction is exposed to checkpointing.
                    new_work={"next":i+1,"got":next_got,"sigma":next_sigma}
                    del z,vv,ss,next_got,next_sigma
                else:new_work={"next":i+1,"got":work["got"],"sigma":work["sigma"]}
                work=new_work
                if work["next"]%10==0 or work["next"]==G:
                    commit_positive();event("complete-positive-original-source-prefix",columns=work["next"])
        except Budget:
            commit_positive();raise
        commit_positive();tick(20)
        need(work["got"]==[target]+[m.ZERO]*9,"all ten original source coordinates equal target")
        sigma=work["sigma"]
        need(sigma[17]==0 and m.dot(A,sigma)==target,"complete original18 gradient source product and zero Bell coefficient")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==10 for ee in f.to_dict()) for k,f in enumerate(sigma[:17])),"all original source weights exactly ten")
        physical_sources=[]
        for i in range(17):
            tick(15);physical_sources.append(sum((sigma[j]*J[j][i] for j in range(17)),m.ZERO))
        need(m.dot(physical,physical_sources)==target,"full original17 physical gradient source multiplication")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==10 for ee in f.to_dict()) for k,f in enumerate(physical_sources)),"all physical source weights exactly ten")
        bell_source=-delta*(bell+1)
        need(m.dot(physical,physical_sources)+A[17]*bell_source==delta,"literal delta=b^2*delta-(b+1)*delta*(b-1) source identity")
        final=phase("complete-original-weight10-delta-source",{"prime":127,"coefficientRoot":100,
             "original200Coefficients":m.packvec(alphas),"original18GradientSource":m.packvec(sigma),
             "original17PhysicalSource":m.packvec(physical_sources),"delta":m.pack(delta),"BellCoefficientForDelta":m.pack(bell_source),
             "all77276OriginalScalarProductsVerified":True,"allTenOriginalCoordinatesVerified":True,
             "all18OriginalProductsVerified":True,"all17PhysicalProductsVerified":True,"literalBellGluingVerified":True,
             "sourceWeightBound":10,"characteristicZeroConclusion":False})
        state["positiveFinal"]=final;new_units+=1;flush()
        rec["status"]="completed-positive";rec["parameters"].update(
            outcome="same F127 original delta14 Bell source with original weighted source bound10",
            positiveOriginalSourceClaimed=True,allTenOriginalProductsVerified=True,all18OriginalProductsVerified=True,
            all17PhysicalProductsVerified=True,literalBellGluingVerified=True,sourceCertificate=final)
        code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="memory-error" if isinstance(e,MemoryError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        if child is not None and child.poll() is None:
            os.killpg(child.pid,signal.SIGTERM)
            try:child.wait(timeout=3)
            except subprocess.TimeoutExpired:os.killpg(child.pid,signal.SIGKILL);child.wait()
        flush();rec["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"].update(newWholeVerifiedUnitsThisRun=new_units,
            continuationEligible=(code==75 and new_units>0),
            parentPeakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            childPeakRssKiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss)
        if state is not None:
            rec["parameters"].update(manifest=identity(mp),completeSourceFrames=len(state["sourceFrames"]),
                nativeCompleteColumns=state.get("nativeState",{}).get("header",{}).get("completeColumns",0),
                independentVerifiedColumns=state.get("verifierState",{}).get("header",{}).get("verifiedColumns",0),
                completePositiveOriginalSourceColumns=state.get("positivePrefix",{}).get("next",0))
        save_json(rp,rec);print(canon(rec).decode(),flush=True)
if __name__=="__main__":raise SystemExit(main())
