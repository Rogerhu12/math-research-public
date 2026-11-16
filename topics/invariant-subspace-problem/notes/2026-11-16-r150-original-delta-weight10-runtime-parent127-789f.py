#!/usr/bin/env python3
"""Bounded homogeneous delta*b^2 consumer of the completed original Gamma200.

Author: Astra-ISP-789f / literature_audit, with /root.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Singular supplies a candidate only. Negative conclusions require independent
ordinary F127 verification of all input columns and every S-pair of weight
at most ten. Positive conclusions require sources in the original 200 columns
and complete ten-coordinate / seventeen-gradient multiplication.
All mathematics and runtime checkpoints are temporary, never repository data.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,re,resource,shutil,signal,subprocess,sys,time
from collections import Counter
from pathlib import Path

sys.set_int_max_str_digits(0)
FORMAT="r150-original-delta-weight10-homogeneous127-runtime-parent-v1"
P=127;ROOT=100;WEIGHTS=(0,)+(2,)*5+(4,)*4
NAMES=tuple("y%d"%i for i in range(6))+tuple("w%d"%i for i in range(6))+("zz",)
MODEL_SHA="4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4"
CHART_SHA="ee9bdabfdd325150b622e77a91d20eb814c642c8cb66bbf4734106466af630e3"
PRODUCER_SHA="20cb960bc20fea18001488e84dae35518d74f3338697dfed619eaadae6a6b2aa"
VERIFIER_SHA="54b082184273e254495be8e1eb788e6569e8ca9cc4b83a1a5d4330304e9d4246"
MODEL_BINDING="7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4"
MODEL_FORMAT="r150-original-ten-generator-complete-parameter-seeds127-v2"
MODEL_MANIFEST={"bytes":30466,"sha256":"9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2"}
PARENT_FORMAT="r150-original-two-round-complete210-sources127-v2"
PARENT_BINDING="41638323f597133aadeb65b2a1639899a162e2afbe6e7f7c477e93fae912cd80"
PARENT_MANIFEST={"bytes":144113,"sha256":"74eb5557203192b2b3e37b43189ceaa7ec34afeb698884f336331210d1bcf2ff"}
PARENT_RECEIPT={"bytes":32576,"sha256":"77724520a9b2aa89086d7bb39e7dcef48bbc1cef2faaef00e9d98fcc588b24ea"}
PARENT_FINAL={"path":"complete-original210-source-model.json.gz","bytes":35044,"sha256":"ed0b6811561a0799dff2cab99b2c7685a2ed820978be00c397a69f110972fed5","logicalBytes":148424,"logicalSha256":"f8b17d755d1515726632280fe110788dcf03128705172944a67d44f12de14bee"}
OLD={
 "model":(MODEL_FORMAT,MODEL_BINDING),
 "mean":("r150-original-mean-first-source-frontier127-v1","9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd"),
 "weight8":("r150-original-complete-weight8-source-frontier127-v1","1fdb39f00f53e51f33cbecef6c25c503c43e85575ad79abbd189ade9fdc7d069"),
 "producer":(PARENT_FORMAT,PARENT_BINDING)}
LOW=(1,2,3,4,5,11,12,13,14,15,21,22,23,24,25,31,32,33,34,35)
HIGH=(6,7,8,9,16,17,18,19,26,27,28,29,36,37)
KEEP=((1,4),(2,3),(2,4),(3,4))
DELTA_SHA="eff3070880440dd84f3b8d6bcfac5fc71461537d55b9f3d2c323a4287cdde0f6"
MAX_SSI=1073741824
MAX_CANDIDATE_COLUMNS=65536
MAX_PHASE=67108864
MAX_LOGICAL=268435456

class Budget(Exception):pass
def need(v,s):
    if not v:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):return hashlib.sha256(b).hexdigest()
def identity(p):
    p=Path(p);h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
    v=identity(p);need(v["bytes"]==d["bytes"] and v["sha256"]==d["sha256"],"whole exact file "+Path(p).name);return v
def atomic(p,b):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+".tmp");q.write_bytes(b);os.replace(q,p)
def save_json(p,x):atomic(p,canon(x));return identity(p)
def load_module(p,h,name):
    need(identity(p)["sha256"]==h,"exact immutable helper "+p.name)
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def read_phase(root,d,fmt,binding):
    p=root/d["path"];exact(p,d)
    need(0<d["bytes"]<=MAX_PHASE and 0<d["logicalBytes"]<=MAX_LOGICAL,"bounded complete original phase")
    raw=gzip.decompress(p.read_bytes());need(len(raw)==d["logicalBytes"] and sha(raw)==d["logicalSha256"],"whole logical original phase")
    z=json.loads(raw);need(z["format"]==fmt+"-phase" and z["binding"]==binding,"same complete original phase binding");return z["data"]
def ss(p,mode=""):
    s=str(p);need(not any(c in s for c in ('"',"\\","\n","\r")),"safe literal Singular path");return '"'+mode+s+'"'
def ring():
    return ["ring r=127,("+",".join(NAMES)+"),(wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C);",
            "short=0; degBound=10; option(redSB); option(redTail);"]
def markers(p):
    good=[];bad=[]
    with p.open("r",encoding="utf8",errors="replace") as f:
        for line in f:
            s=line.strip()
            if s.startswith("@@"):good.append(s)
            if s.startswith("@@FAIL") or s.startswith("?"):bad.append(s[:800])
    need(len(good)<=1000000 and len(bad)<=10000,"bounded complete marker log");return good,bad
def one(lines,prefix,required=True):
    z=[s for s in lines if s==prefix or s.startswith(prefix+" ") or (prefix.endswith(" ") and s.startswith(prefix))];need(len(z)<=1,"unique exact completion marker "+prefix)
    if required:need(len(z)==1,"whole completion marker "+prefix)
    return z[0] if z else None
def write_polynomial(f,terms,zz_power):
    if not terms:f.write("0");return
    if zz_power:f.write("zz^%d*("%zz_power)
    first=True
    for ee,c in terms:
        if not first:f.write("+")
        first=False;f.write(str(c))
        for name,e in zip(NAMES[:12],ee):
            if e:f.write("*"+name+("^%d"%e if e!=1 else ""))
    if zz_power:f.write(")")

def main():
    ap=argparse.ArgumentParser()
    for n in ("model-source","chart-source","producer-source","verifier-source","model-out","mean-out","weight8-out","producer-out","out"):
        ap.add_argument("--"+n,type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--through",choices=("prepare","candidate","verify","final"),default="prepare")
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args();need(0<a.seconds<=1800 and 1024<=a.memory_mib<=6144,"bounded weight-ten consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    begun=time.monotonic();deadline=begun+a.seconds;a.out.mkdir(parents=True,exist_ok=True)
    own=identity(Path(__file__))
    actual_parent_receipt=identity(a.producer_out/"complete210-sources-receipt.json")
    sem={"format":FORMAT,"source":own,"prime":P,"coefficientRoot":ROOT,
         "modelSourceSHA256":MODEL_SHA,"chartSourceSHA256":CHART_SHA,"producerSourceSHA256":PRODUCER_SHA,"verifierSourceSHA256":VERIFIER_SHA,
         "parentFormat":PARENT_FORMAT,"parentBinding":PARENT_BINDING,"parentManifest":PARENT_MANIFEST,"parentReceipt":actual_parent_receipt,"paidHistoricalParentReceipt":PARENT_RECEIPT,"parentFinalPhase":PARENT_FINAL,
         "literalTarget":"delta14*b^2*e0","deltaSHA256":DELTA_SHA,"originalMeanRows":[2,3,4,5],
         "originalNonBellColumns":200,"targetWeight":10,"rowShifts":list(WEIGHTS),"variableWeights":[1]*6+[2]*6+[1],
         "ordering":"wp(1,1,1,1,1,1,2,2,2,2,2,2,1),C","candidateEngine":"std, degBound=10",
         "negativeGate":"all original200 inputs; all same-component S-pairs with lcm weighted degree at most10; complete independent irreducible target remainder",
         "positiveGate":"lift to original200; zz=0 and homogeneous coefficient projection; complete original10/18/17 products; literal Bell gluing",
         "characteristicZeroConclusion":False,"maxCandidateColumns":MAX_CANDIDATE_COLUMNS,"maxSSIBytes":MAX_SSI}
    binding=sha(canon(sem));mp=a.out/"delta-weight10-manifest.json";rp=a.out/"delta-weight10-receipt.json"
    state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"generation":0,"phases":{},"prepared":[],"candidateColumns":[],"sourceTexts":[]}
    if mp.exists():
        state=json.loads(mp.read_bytes());need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and state["semantic"]==sem,"same exact homogeneous continuation")
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{"through":a.through,"seconds":a.seconds,"memoryMiB":a.memory_mib,
         "originalIdealNonmembershipClaimed":False,"positiveOriginalSourceClaimed":False,"characteristicZeroConclusion":False,"stages":[]}}
    child=None;code=1;new_units=0;engine=None
    def remaining():return deadline-time.monotonic()
    def tick():
        if remaining()<8:raise Budget("whole homogeneous verification unit budget")
    def alarm(*unused):raise Budget("actual homogeneous consumer budget")
    def flush():save_json(mp,state)
    def event(name,**kw):
        rec["parameters"]["lastWholePhase"]=name;print(canon({"phase":name,"elapsedSeconds":time.monotonic()-begun,**kw}).decode(),flush=True)
    def phase(name,data):
        raw=canon({"format":FORMAT+"-phase","binding":binding,"data":data});need(len(raw)<=MAX_LOGICAL,"bounded complete child phase")
        p=a.out/(name+".json.gz");atomic(p,gzip.compress(raw,compresslevel=1,mtime=0))
        d={**identity(p),"logicalBytes":len(raw),"logicalSha256":sha(raw)};state["phases"][name]=d;flush();return d
    def child_phase(name):return read_phase(a.out,state["phases"][name],FORMAT,binding)
    def checked(desc):
        p=a.out/desc["path"];exact(p,desc);return p
    def run(name,lines):
        nonlocal child
        tick();state["generation"]+=1;g=state["generation"];flush()
        sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name))
        atomic(sp,("\n".join(lines)+"\n").encode("ascii"))
        st={"name":name,"script":identity(sp),"status":"running"};rec["parameters"]["stages"].append(st)
        start=time.monotonic();budget=False;rc=1;signal.setitimer(signal.ITIMER_REAL,0)
        try:
            with lp.open("wb") as out:
                child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=out,stderr=subprocess.STDOUT)
                last=start
                while child.poll() is None:
                    if remaining()<8:
                        budget=True;child.terminate()
                        try:child.wait(timeout=3)
                        except subprocess.TimeoutExpired:child.kill();child.wait()
                        break
                    if time.monotonic()-last>=30:event(name+"-running",childSeconds=time.monotonic()-start);last=time.monotonic()
                    time.sleep(.2)
                rc=child.returncode
        finally:
            child=None
            if remaining()>0:signal.setitimer(signal.ITIMER_REAL,remaining())
        good,bad=markers(lp)
        st.update(status="budget" if budget else "returned",exitCode=rc,budget=budget,elapsedSeconds=time.monotonic()-start,log=identity(lp),markers=good)
        need(not bad,"actual Singular explicit failure "+repr(bad[:3]))
        if not budget:need(rc==0,"actual Singular nonzero exit "+str(rc))
        return st
    def original_lines():
        checked(state["originalSSI"]["data"]);checked(state["targetASCII"])
        return ring()+["def Original=read("+ss(a.out/"original-shifted200.ssi","ssi:r ")+");",
          'if(ncols(Original)!=200){print("@@FAIL original200-shape");quit;}',
          "matrix OM[10][200]=Original;","< "+ss(a.out/state["targetASCII"]["path"])+";"]
    def candidate_lines():
        checked(state["candidate"]["data"])
        return ring()+["def G=read("+ss(a.out/"complete-weight10-candidate.ssi","ssi:r ")+");",
          'if(ncols(G)!='+str(state["candidate"]["columns"])+'){print("@@FAIL candidate-shape");quit;}']
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,a.seconds)
    try:
        need(tuple(sys.version_info[:3])==(3,12,14),"pinned Python3.12.14 phase identity")
        import flint
        need(flint.__version__=="0.9.0","pinned python-flint0.9.0")
        m=load_module(a.model_source,MODEL_SHA,"weight10_original_model")
        ch=load_module(a.chart_source,CHART_SHA,"weight10_original_chart")
        v=load_module(a.verifier_source,VERIFIER_SHA,"weight10_independent_divider")
        need(identity(a.producer_source)["sha256"]==PRODUCER_SHA,"exact completed104 original producer")
        rec["parameters"]["independentTinyControls"]=v.selftest()
        roots={"model":a.model_out,"mean":a.mean_out,"weight8":a.weight8_out,"producer":a.producer_out}
        exact(a.producer_out/"complete210-sources-manifest.json",PARENT_MANIFEST)
        exact(a.producer_out/"complete210-sources-receipt.json",actual_parent_receipt)
        pm=json.loads((a.producer_out/"complete210-sources-manifest.json").read_bytes())
        pr=json.loads((a.producer_out/"complete210-sources-receipt.json").read_bytes())
        need(pm["format"]==PARENT_FORMAT+"-manifest" and pm["binding"]==PARENT_BINDING and sha(canon(pm["semantic"]))==PARENT_BINDING,"complete104 actual semantic binding")
        need(pr["format"]==PARENT_FORMAT and pr["status"]=="completed" and pr["binding"]==PARENT_BINDING and pr["source"]["sha256"]==PRODUCER_SHA,"completed full original210 parent, never a prefix")
        need(pr["parameters"]["manifest"]=={"path":"complete210-sources-manifest.json",**PARENT_MANIFEST},"this actual complete execution points to the exact paid mathematical manifest")
        rec["parameters"]["actualParentReceipt"]=actual_parent_receipt
        rec["parameters"]["paidHistoricalParentReceiptByteMatch"]=all(actual_parent_receipt[k]==PARENT_RECEIPT[k] for k in ("bytes","sha256"))
        rec["parameters"]["parentExecutionScope"]="same frozen sources, semantic binding and every paid mathematical phase; independently bound actual execution metadata"
        need(all(pr["parameters"][k] for k in ("all104NewOriginal18ProductsVerified","all104TenVectorsVerified","all210OriginalSourcesVerified")) and pr["parameters"]["completeNewMeanColumns"]==24 and pr["parameters"]["completeNewCommutatorColumns"]==80,"all106/104 completed original arithmetic gates")
        need(pm["phases"]["complete-original210-source-model"]==pr["parameters"]["completeModel"]==PARENT_FINAL,"same whole final210 phase")
        final=read_phase(a.producer_out,PARENT_FINAL,PARENT_FORMAT,PARENT_BINDING)
        need(final["allColumnCount"]==210 and final["all106ParentSourcesVerified"] and final["all104NewTenVectorsVerified"] and final["all104NewOriginal18ProductsVerified"] and final["all104NewBellSourceCoefficientsZero"],"complete final-source mathematics")
        need(final["parentColumns"]==pm["parentMathematics"]["old106"] and len(final["parentColumns"])==106 and len(final["newColumns"])==104,"every old106/new104 original reference")
        refs=[];deleted=[]
        for rr in final["parentColumns"]:
            tag=rr["parent"];fmt,bb=OLD[tag]
            need(rr["format"]==fmt and rr["binding"]==bb,"same literal old source identity")
            if rr["kind"]=="original-seed":
                sid=rr["seedIndex"]
                if 106<=sid<116:deleted.append(sid);continue
                need(sid in LOW or sid in HIGH or 100<=sid<106,"exact nonBell seed labels")
                weight=5 if sid>=100 else 6 if sid in LOW else 8
            elif rr["kind"]=="mean-first-image":weight=7
            else:need(rr["kind"]=="commutator-first-image","known complete first-image kind");weight=8
            refs.append({"origin":rr,"weight":weight,"kind":"old"})
        need(deleted==list(range(106,116)) and len(refs)==96,"only the ten literal Bell columns removed")
        for item in final["newColumns"]:
            job=item["literalSource"];need(pm["phases"][job["phaseKey"]]==item["descriptor"] and tuple(job["orderedOperators"]) in KEEP,"all exact second-image descriptors")
            need((job["family"]=="mean" and 100<=job["originalSeedIndex"]<106 and job["weight"]==9) or (job["family"]=="commutator" and job["originalSeedIndex"] in LOW and job["weight"]==10),"all104 literal source labels and weights")
            refs.append({"kind":"new","weight":job["weight"],"origin":{"parent":"producer","format":PARENT_FORMAT,"binding":PARENT_BINDING,"descriptor":item["descriptor"],"literalSource":job}})
        need(len(refs)==200 and Counter(rr["weight"] for rr in refs)=={5:6,6:20,7:30,8:40,9:24,10:80},"complete homogeneous Gamma200 dictionary")
        if "originalReferences" in state:need(state["originalReferences"]==refs,"unchanged original200 source dictionary")
        else:state["originalReferences"]=refs;flush()
        def source_record(index):
            rr=refs[index]["origin"];z=read_phase(roots[rr["parent"]],rr["descriptor"],rr["format"],rr["binding"])
            need(z["fullOriginal18ProductVerified"] and len(z["vector"])==10 and len(z["original18Source"])==18 and z["original18Source"][17]==[],"all original source coordinates and zero Bell slot")
            if refs[index]["kind"]=="new":need(z["literalSource"]==rr["literalSource"] and z["allTenImageCoordinatesVerified"] and z["originalBellSourceIsZero"],"same completed new original source")
            elif rr["kind"]=="original-seed":need(z["seedIndex"]==rr["seedIndex"] and z["allTenParameterCoordinatesRetained"],"same literal original seed")
            else:
                key="meanSeedIndex" if rr["kind"]=="mean-first-image" else "commutatorSeedIndex"
                need(z[key]==rr["seedIndex"] and z["operator"]==rr["operator"],"same exact first-image source")
            for k,poly in enumerate(z["original18Source"][:17]):
                gw=4 if k<11 else 5
                need(all(len(ee)==17 and sum(ee[:6])+2*sum(ee[6:])+gw==refs[index]["weight"] for ee,c in poly),"all literal original source coefficients have the declared weight")
            return z
        exact(a.model_out/"original-parameter-module-manifest.json",MODEL_MANIFEST)
        mm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes())
        need(mm["binding"]==MODEL_BINDING and mm["format"]==MODEL_FORMAT+"-manifest","same original full model")
        base=m.load_gz(a.model_out/mm["phases"]["complete-original-ten-parameter-action127"]["path"],mm["phases"]["complete-original-ten-parameter-action127"],MODEL_BINDING)
        oldchart=m.load_gz(a.model_out/mm["phases"]["complete-original-global-chart127"]["path"],mm["phases"]["complete-original-global-chart127"],MODEL_BINDING)
        A=m.unpackvec(base["allOriginal18Generators"]);physical=m.unpackvec(oldchart["originalComposedGradients"])
        J=[m.unpackvec(row) for row in base["sourceCoordinateChange"]]
        need(len(A)==18 and len(physical)==17 and len(J)==17 and all(len(row)==17 for row in J),"all original gradient coordinates")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])==(4 if k<11 else 5) for ee in f.to_dict()) for k,f in enumerate(A[:17])),"all17 original generators have their literal weights4/5")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])==(4 if k<11 else 5) for ee in f.to_dict()) for k,f in enumerate(physical)),"all17 physical gradient weights4/5")
        need(all(m.dot(row,physical)==A[i] for i,row in enumerate(J)),"all17 complete original gradient transports")
        means=[m.unpackvec(row) for row in base["allSixOriginalMeanColumns"]]
        Y=m.CTX.gens()[:6];W=m.CTX.gens()[6:12];bell=sum((y*w for y,w in zip(Y,W)),m.ZERO)
        need(A[17]==bell-1==m.unpack(oldchart["originalBellMinusOne"]),"literal original Bell polynomial")
        for k in range(4):
            for i in range(6):need(means[i][6+k]==sum((int(base["allFourOriginalMeanMatrices"][k][i][j])*Y[j] for j in range(6)),m.ZERO),"all24 original mean coordinates")
        B=[[means[j][6+i] for j in (2,3,4,5)] for i in range(4)]
        delta=ch.det(B,m);adj=ch.adj(B,m);diagonal=[[delta if i==j else m.ZERO for j in range(4)] for i in range(4)]
        need(ch.same(ch.mm(B,adj,m),diagonal) and ch.same(ch.mm(adj,B,m),diagonal) and delta!=0 and sha(canon(m.pack(delta)))==DELTA_SHA,"both original adjugate products and exact same delta14")
        target=delta*bell**2;target_vector=[target]+[m.ZERO]*9
        target_terms=v.from_model_vector(target_vector)
        rec["parameters"].update(allCompletedOriginalParentHashesVerified=True,all200OriginalSourceProductsInheritedFromCompleteParent=True,all17OriginalTransportsRechecked=True,all24MeanCoordinatesRechecked=True,bothLiteralAdjugatesRechecked=True)
        for i in range(len(state["prepared"])):
            d=state["prepared"][i];need(d["originalReference"]==refs[i],"unchanged complete prepared source")
            v.read_vector(checked(d["vector"]),d["vector"],binding);checked(d["ascii"])
        for i in range(len(state["prepared"]),200):
            tick();z=source_record(i);vv=m.unpackvec(z["vector"]);terms=v.from_model_vector(vv)
            vector=v.write_vector(a.out/("input-%03d.bin.gz"%i),terms,refs[i]["weight"],binding)
            path=a.out/("input-%03d.sing"%i);tmp=path.with_name(path.name+".tmp")
            with tmp.open("w",encoding="ascii",newline="\n") as f:
                for row in range(10):
                    tt=[(v.exponents(t),c) for t,c in terms if (t&15)==row]
                    f.write("OM[%d,%d]="%(row+1,i+1));write_polynomial(f,tt,WEIGHTS[row]);f.write(";\n")
            os.replace(tmp,path);need(path.stat().st_size<=33554432,"one full original ASCII column size")
            state["prepared"].append({"originalReference":refs[i],"vector":vector,"ascii":identity(path)});new_units+=1;flush()
            if i%10==9:event("complete-original-input-prefix",columns=i+1)
            del z,vv,terms
        if "target" not in state:
            state["target"]=v.write_vector(a.out/"literal-delta-b-square.bin.gz",target_terms,10,binding)
            path=a.out/"literal-target.sing";tmp=path.with_name(path.name+".tmp")
            with tmp.open("w",encoding="ascii",newline="\n") as f:
                f.write("matrix TM[10][1]; TM[1,1]=");write_polynomial(f,[(v.exponents(t),c) for t,c in target_terms],0);f.write("; module Target=TM;\n")
            os.replace(tmp,path);state["targetASCII"]=identity(path);new_units+=1;flush()
        need(v.read_vector(checked(state["target"]),state["target"],binding)==v.normalized_terms(target_terms,10)[0],"same complete original target")
        checked(state["targetASCII"])
        rec["parameters"].update(originalInputColumns=200,originalInputTerms=sum(d["vector"]["terms"] for d in state["prepared"]),originalASCIITotalBytes=sum(d["ascii"]["bytes"] for d in state["prepared"]),targetTerms=len(target_terms),inputWeightCounts=dict(sorted(Counter(rr["weight"] for rr in refs).items())),all200OriginalSourceWeightsVerified=True)
        event("all-original200-homogeneous-inputs",columns=200,terms=rec["parameters"]["originalInputTerms"])
        if a.through=="prepare":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all200 original homogeneous inputs prepared; no candidate computation";code=0;return code
        engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
        need(engine is not None,"actual installed Singular executable")
        ver=subprocess.run([str(engine),"-v"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=min(15,remaining()-8))
        need(ver.returncode==0 and re.search(rb"4\.4\.1",ver.stdout),"pinned Singular4.4.1 actual runtime")
        runtime={"binary":identity(engine),"versionFirstLine":ver.stdout.decode(errors="replace").splitlines()[0],"wholeVersionSHA256":sha(ver.stdout)}
        if "engine" in state:need(state["engine"]==runtime,"same exact Singular runtime for candidate continuation")
        else:state["engine"]=runtime;flush()
        if "engineSelftest" not in state:
            lines=ring()+["degBound=3; matrix O[10][2];O[1,1]=y0^2;O[2,1]=zz^2;O[1,2]=y0*y1;module Q=O;",
              "matrix T[10][1];T[2,1]=y1*zz^2;module U=T;module G=std(Q);",
              'if(reduce(U[1],G)!=0){print("@@FAIL shifted-positive-control");quit;}',
              "vector n=zz^2*gen(2);",
              'if(reduce(n,G)==0){print("@@FAIL shifted-negative-control");quit;}',
              'matrix Units;matrix Sources=lift(Q,U,Units,"std");',
              'if(nrows(Sources)!=2 || ncols(Sources)!=1 || nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL shifted-lift-shape");quit;}',
              'matrix DD=O*Sources-T;int j;for(j=1;j<=10;j++){if(DD[j,1]!=0){print("@@FAIL shifted-lift-product");quit;}}',
              'print("@@SHIFTED-ENGINE-CONTROL-COMPLETE");quit;']
            st=run("shifted-small-controls",lines)
            if not one(st["markers"],"@@SHIFTED-ENGINE-CONTROL-COMPLETE",False):
                if st["budget"]:raise Budget("tiny engine controls incomplete")
                raise ValueError("missing shifted engine control")
            state["engineSelftest"]=st;new_units+=1;flush()
        if "originalSSI" not in state:
            lines=ring()+["matrix OM[10][200];"]
            lines+=["< "+ss(a.out/d["ascii"]["path"])+";" for d in state["prepared"]]
            lines+=["module Original=OM;","write("+ss(a.out/"original-shifted200.ssi","ssi:w ")+",Original);",
              "def Copy=read("+ss(a.out/"original-shifted200.ssi","ssi:r ")+");",
              'if(ncols(Copy)!=200){print("@@FAIL original-shifted200-SSI-shape");quit;}',
              'matrix CM[10][200]=Copy;int i;int j;for(i=1;i<=10;i++){for(j=1;j<=200;j++){if(CM[i,j]!=OM[i,j]){print("@@FAIL full-original2000-SSI-product");quit;}}}',
              'print("@@ALL-ORIGINAL2000-SSI-COORDINATES");quit;']
            st=run("materialize-all200-original-columns",lines)
            if not one(st["markers"],"@@ALL-ORIGINAL2000-SSI-COORDINATES",False):
                if st["budget"]:raise Budget("original module SSI incomplete")
                raise ValueError("missing whole original SSI gate")
            d=identity(a.out/"original-shifted200.ssi");need(d["bytes"]<=MAX_SSI,"bounded whole original SSI")
            state["originalSSI"]={"data":d,"evidence":st};new_units+=1;flush()
        if "candidate" not in state:
            lines=original_lines()+['print("@@WEIGHT10-CANDIDATE-START");module G=std(Original);',
              'print("@@WEIGHT10-CANDIDATE-RETURN "+string(ncols(G)));',
              "write("+ss(a.out/"complete-weight10-candidate.ssi","ssi:w ")+",G);",
              "def Copy=read("+ss(a.out/"complete-weight10-candidate.ssi","ssi:r ")+");",
              'if(ncols(Copy)!=ncols(G)){print("@@FAIL candidate-SSI-shape");quit;}int i;',
              'for(i=1;i<=ncols(G);i++){if(Copy[i]!=G[i]){print("@@FAIL candidate-SSI-full-column");quit;}}',
              'print("@@WHOLE-WEIGHT10-CANDIDATE-SAVED "+string(ncols(G)));quit;']
            st=run("bounded-homogeneous-candidate",lines)
            end=one(st["markers"],"@@WHOLE-WEIGHT10-CANDIDATE-SAVED ",False)
            if end is None:
                rec["parameters"]["candidateAbsentNoEmptyRetry"]=True
                if st["budget"]:raise Budget("no complete candidate returned; do not repeat an empty candidate run")
                raise ValueError("missing whole weight-ten candidate")
            count=int(end.split()[-1]);need(0<count<=MAX_CANDIDATE_COLUMNS,"bounded complete candidate column count")
            d=identity(a.out/"complete-weight10-candidate.ssi");need(d["bytes"]<=MAX_SSI,"bounded whole candidate SSI")
            state["candidate"]={"data":d,"columns":count,"evidence":st,"verifiedStandardBasis":False};new_units+=1;flush()
        if a.through=="candidate":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="whole candidate saved; no negative claim";code=0;return code
        count=state["candidate"]["columns"]
        for item in state["candidateColumns"]:
            if item.get("vector"):v.read_vector(checked(item["vector"]),item["vector"],binding)
        while len(state["candidateColumns"])<count:
            tick();start=len(state["candidateColumns"]);stop=min(count,start+16)
            lines=candidate_lines()+["matrix GM[10]["+str(count)+"]=G;int i;"]
            for j in range(start,stop):
                for i in range(10):lines.append("write("+ss(a.out/("candidate-%05d-%02d.txt"%(j,i)),":w ")+",GM[%d,%d]);"%(i+1,j+1))
                lines.append('print("@@EXPORTED-WHOLE-CANDIDATE-COLUMN '+str(j)+'");')
            lines+=['print("@@CANDIDATE-EXPORT-BATCH-COMPLETE");quit;']
            st=run("export-complete-candidate-columns-%05d"%start,lines)
            for j in range(start,stop):
                if not one(st["markers"],"@@EXPORTED-WHOLE-CANDIDATE-COLUMN %d"%j,False):break
                paths=[a.out/("candidate-%05d-%02d.txt"%(j,i)) for i in range(10)]
                texts=[identity(p) for p in paths];terms,weight=v.shifted_text_vector(paths)
                if terms:
                    d=v.write_vector(a.out/("candidate-%05d.bin.gz"%j),terms,weight,binding,normalize=True)
                    item={"singularIndex":j,"texts":texts,"vector":d}
                else:item={"singularIndex":j,"texts":texts,"zero":True}
                state["candidateColumns"].append(item);new_units+=1;flush()
            if len(state["candidateColumns"])<stop:
                if st["budget"]:raise Budget("only whole exported candidate columns retained")
                raise ValueError("incomplete candidate export")
        catalog=[q["vector"] for q in state["candidateColumns"] if q.get("vector")]
        need(catalog,"nonzero independently parsed candidate")
        catalog_hash=sha(canon(catalog))
        def load_candidate(i):return v.read_vector(a.out/catalog[i]["path"],catalog[i],binding)
        divider=v.Divider(catalog,load_candidate,tick)
        proof=state.setdefault("independentProof",{"catalogSHA256":catalog_hash,"inputNext":0,"pairI":0,"pairJ":1,"pairsExamined":0,"relevantPairsVerified":0,"chainSHA256":sha(b"R150-full-weight10-verification-prefix-v1"),"ordinaryReductions":0,"ordinaryTermUpdates":0})
        need(proof["catalogSHA256"]==catalog_hash,"same entire candidate for the verified prefix")
        def record(unit,stats):
            proof["chainSHA256"]=sha(bytes.fromhex(proof["chainSHA256"])+canon({"unit":unit,"division":stats,"remainderZero":True}))
            proof["ordinaryReductions"]+=stats["reductions"];proof["ordinaryTermUpdates"]+=stats["ordinaryTermUpdates"]
        while proof["inputNext"]<200:
            tick();i=proof["inputNext"];d=state["prepared"][i]["vector"];terms=v.read_vector(a.out/d["path"],d,binding)
            rem,stats=divider.normal_form(terms,d["degree"])
            if rem:
                bad=v.write_vector(a.out/"incomplete-input-remainder.bin.gz",rem,d["degree"],binding)
                rec["status"]="completed-diagnostic";rec["parameters"].update(outcome="candidate does not contain all original inputs",firstFailedInput=i,remainder=bad);code=0;return code
            record(["input",i],stats);proof["inputNext"]+=1;new_units+=1;flush()
        n=len(catalog)
        while proof["pairI"]<n:
            tick();i,j=proof["pairI"],proof["pairJ"]
            if j>=n:proof["pairI"]+=1;proof["pairJ"]=proof["pairI"]+1;flush();continue
            q=divider.pair(i,j)
            if q is not None:
                terms,weight,lcm=q;rem,stats=divider.normal_form(terms,weight)
                if rem:
                    bad=v.write_vector(a.out/"incomplete-pair-remainder.bin.gz",rem,weight,binding)
                    rec["status"]="completed-diagnostic";rec["parameters"].update(outcome="candidate fails a relevant complete S-pair",firstFailedPair=[i,j],lcmCode=lcm,remainder=bad);code=0;return code
                record(["pair",i,j,lcm],stats);proof["relevantPairsVerified"]+=1;new_units+=1
            proof["pairsExamined"]+=1;proof["pairJ"]+=1
            if q is not None or proof["pairsExamined"]%1000==0:flush()
        need(proof["pairsExamined"]==n*(n-1)//2 and proof["inputNext"]==200,"every complete candidate pair and original input considered")
        if "targetIndependentRemainder" not in state:
            rem,stats=divider.normal_form(target_terms,10)
            d=v.write_vector(a.out/"complete-independent-target-remainder.bin.gz",rem,10,binding)
            state["targetIndependentRemainder"]={"vector":d,"division":stats,"zero":not rem,"completeIrreducibilityVerified":True};new_units+=1;flush()
        rem=v.read_vector(checked(state["targetIndependentRemainder"]["vector"]),state["targetIndependentRemainder"]["vector"],binding)
        need(bool(rem)!=state["targetIndependentRemainder"]["zero"],"same complete independent target remainder")
        rec["parameters"].update(all200OriginalInputsReducedToZero=True,allRelevantSPairsIndependentlyReducedToZero=True,candidateNonzeroColumns=n,
          candidatePairsConsidered=proof["pairsExamined"],relevantPairsVerified=proof["relevantPairsVerified"],independentVerification=proof,targetRemainder=state["targetIndependentRemainder"])
        if rem:
            rec["status"]="completed-negative"
            rec["parameters"].update(outcome="delta14*b^2 is not in the same F127 original17 gradient ideal",originalIdealNonmembershipClaimed=True,
              negativeProofUsesOnlyCertifiedContainingModule=True,originalBellIdealNonmembershipClaimed=False,allHigherBellPowersExcluded=False)
            code=0;return code
        if a.through=="verify":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="independent target remainder is zero; original source extraction still required";code=0;return code
        if "sourceCandidate" not in state:
            lines=original_lines()+['print("@@ORIGINAL200-LIFT-START");matrix Units;matrix Sources=lift(Original,Target,Units,"std");',
              'if(nrows(Sources)!=200 || ncols(Sources)!=1 || nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL original200-lift-shape");quit;}',
              'matrix D=OM*Sources-TM;int i;for(i=1;i<=10;i++){if(D[i,1]!=0){print("@@FAIL all-ten-shifted-source-products");quit;}}',
              "write("+ss(a.out/"complete-original200-target-sources.ssi","ssi:w ")+",Sources);",
              "def Copy=read("+ss(a.out/"complete-original200-target-sources.ssi","ssi:r ")+");",
              'if(nrows(Copy)!=200 || ncols(Copy)!=1){print("@@FAIL source200-SSI-shape");quit;}',
              'for(i=1;i<=200;i++){if(Copy[i,1]!=Sources[i,1]){print("@@FAIL full-source200-SSI-product");quit;}}',
              'print("@@COMPLETE-ORIGINAL200-LIFT");quit;']
            st=run("original200-target-only-lift",lines)
            if not one(st["markers"],"@@COMPLETE-ORIGINAL200-LIFT",False):
                if st["budget"]:raise Budget("no complete original target lift returned")
                raise ValueError("missing complete original lift")
            d=identity(a.out/"complete-original200-target-sources.ssi");need(d["bytes"]<=MAX_SSI,"bounded complete source SSI")
            state["sourceCandidate"]={"data":d,"evidence":st};new_units+=1;flush()
        checked(state["sourceCandidate"]["data"])
        while len(state["sourceTexts"])<200:
            first=len(state["sourceTexts"]);stop=min(200,first+20)
            lines=ring()+["def Sources=read("+ss(a.out/"complete-original200-target-sources.ssi","ssi:r ")+");",
              'if(nrows(Sources)!=200 || ncols(Sources)!=1){print("@@FAIL source-export-shape");quit;}']
            for i in range(first,stop):
                lines+=["write("+ss(a.out/("source-%03d.txt"%i),":w ")+",Sources[%d,1]);"%(i+1),'print("@@SOURCE-COEFFICIENT '+str(i)+'");']
            lines+=['print("@@SOURCE-EXPORT-BATCH-COMPLETE");quit;'];st=run("export-original-source-prefix-%03d"%first,lines)
            for i in range(first,stop):
                if not one(st["markers"],"@@SOURCE-COEFFICIENT %d"%i,False):break
                state["sourceTexts"].append(identity(a.out/("source-%03d.txt"%i)));new_units+=1;flush()
            if len(state["sourceTexts"])<stop:
                if st["budget"]:raise Budget("only whole source coefficients retained")
                raise ValueError("incomplete original coefficient export")
        alphas=[];discard_z=discard_weight=0
        for i,d in enumerate(state["sourceTexts"]):
            tick();poly=v.parse_polynomial(checked(d));ans={}
            for ee,c in poly.items():
                if ee[12]:discard_z+=1;continue
                if sum(ee[:6])+2*sum(ee[6:12])!=10-refs[i]["weight"]:discard_weight+=1;continue
                ans[tuple(ee[:12])+(0,)*5]=c
            alphas.append(m.CTX.from_dict(ans))
        got=[m.ZERO for unused in range(10)]
        for i,alpha in enumerate(alphas):
            tick()
            if alpha:
                terms=v.read_vector(a.out/state["prepared"][i]["vector"]["path"],state["prepared"][i]["vector"],binding)
                for row in range(10):
                    f=m.CTX.from_dict({v.exponents(t)+(0,)*5:c for t,c in terms if (t&15)==row});got[row]+=alpha*f
        need(got==target_vector,"independent all-ten original source product after exact zz evaluation and homogeneous projection")
        sigma=[]
        for k in range(18):
            name="complete-original18-coefficient-%02d"%k
            if name in state["phases"]:
                z=child_phase(name);need(z["generator"]==k,"same original gradient index");s=m.unpack(z["coefficient"])
            else:
                s=m.ZERO
                for i,alpha in enumerate(alphas):
                    tick()
                    if alpha:s+=alpha*m.unpack(source_record(i)["original18Source"][k])
                phase(name,{"generator":k,"coefficient":m.pack(s)});new_units+=1
            sigma.append(s)
        need(sigma[17]==0 and m.dot(A,sigma)==target,"all18 original generators and exact zero Bell coefficient")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==10 for ee in f.to_dict()) for k,f in enumerate(sigma[:17])),"all original18 gradient sources have complete weight10")
        osig=[]
        for i in range(17):
            tick();s=sum((sigma[j]*J[j][i] for j in range(17)),m.ZERO);osig.append(s)
        need(m.dot(physical,osig)==target,"complete original17 physical gradient source product")
        need(all(all(sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==10 for ee in f.to_dict()) for k,f in enumerate(osig)),"all physical17 gradient sources have complete weight10")
        bellsource=-delta*(bell+1)
        need(m.dot(physical,osig)+A[17]*bellsource==delta,"literal delta=b^2*delta-(b+1)*delta*(b-1) source gluing")
        cert=phase("complete-original-delta-weight10-source",{"prime":127,"coefficientRoot":100,"targetWeight":10,
          "delta":m.pack(delta),"original200Coefficients":m.packvec(alphas),"original18GradientSource":m.packvec(sigma),
          "original17PhysicalSource":m.packvec(osig),"BellCoefficientForDelta":m.pack(bellsource),
          "allTenOriginalProductsVerified":True,"all18OriginalProductsVerified":True,"all17PhysicalProductsVerified":True,
          "literalBellGluingVerified":True,"zzEvaluationDiscardedTerms":discard_z,"homogeneousProjectionDiscardedTerms":discard_weight})
        rec["status"]="completed-positive";rec["parameters"].update(outcome="same F127 original delta14 Bell source of weight at most10",positiveOriginalSourceClaimed=True,
          allTenOriginalProductsVerified=True,all18OriginalProductsVerified=True,all17PhysicalProductsVerified=True,literalBellGluingVerified=True,certificate=cert)
        code=0;return code
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=75;return code
    except BaseException as e:
        rec["status"]="memory-error" if isinstance(e,MemoryError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1;return code
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        if child is not None and child.poll() is None:
            child.terminate()
            try:child.wait(timeout=3)
            except subprocess.TimeoutExpired:child.kill();child.wait()
        flush();rec["elapsedSeconds"]=time.monotonic()-begun
        rec["parameters"].update(newCompleteVerificationUnitsThisRun=new_units,
          continuationEligible=(code==75 and new_units>0 and not rec["parameters"].get("candidateAbsentNoEmptyRetry",False)),
          parentPeakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,childPeakRssKiB=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
          completePreparedColumns=len(state["prepared"]),completeParsedCandidateColumns=len(state["candidateColumns"]),manifest=identity(mp))
        save_json(rp,rec);print(canon(rec).decode(),flush=True)
if __name__=="__main__":raise SystemExit(main())
