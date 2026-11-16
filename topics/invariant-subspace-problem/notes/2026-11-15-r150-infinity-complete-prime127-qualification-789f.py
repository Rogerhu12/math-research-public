#!/usr/bin/env python3
"""Qualify prime 127 on the complete original natural-infinity module.

Author: Astra-ISP-789f / literature_audit. AI-assisted: GPT-6 Astra Pro.
Date: 2026-11-15.
Read-only paid rational ancestors. This does not reuse a 31-normal-form frame.
Every high row (5100), low row (1088), and target coordinate (4367) is retained.
The last exponent is checked by an actual new eleventh original forcing.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import signal
import struct
import subprocess
import sys
import time
from flint import nmod_mat

P=127
FORMAT="r150-infinity-complete-prime127-qualification-v1"
ACTIONS_SHA="2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332"
NATIVE_SHA="450784102b43b178f93913167ca74e36ba8f420a8d0003f283bfeeecf4fd8727"
HEADER_SHA="03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"
Q13_SHA="2057846f5adb75ed84f20a144f4cb2da436f9b1db5674612ac376f9b4b503248"
Q13_BYTES=52012
PINS=json.loads(r'''{"projection":{"root":"infinity-small-original-projection-smith/temporary","binding":"01ba6e6d1f1d0c0ae9ae22a319615887dce4c313d29c9ce1bde346445ae10766","phases":{"original-projection-coefficients":{"bytes":267400,"file":"original-projection-coefficients-94cffcf53fe22e7693e4c22bd67b237fe9d65933a50571891647c378a4b98034.json.gz","sha256":"94cffcf53fe22e7693e4c22bd67b237fe9d65933a50571891647c378a4b98034"},"Q-smith-state":{"bytes":12208895,"file":"Q-smith-state-839af8f6f6ae87d75c2cfcd206323a0ceb6193dd49a398134fdb8448e693b5ae.json.gz","sha256":"839af8f6f6ae87d75c2cfcd206323a0ceb6193dd49a398134fdb8448e693b5ae"}},"receiptBytes":28395,"receiptSHA256":"ea44027e462054b9fdb9c9101065faaba0b14dc5ab9b1a5602c06fecbb765207","receipt":"43740928483-infinity-small-original-projection-smith.json"},"fifth":{"root":"infinity-fifth-true-incoming-checkpoint","phases":{"high-fifth-lifts":{"bytes":15355,"file":"high-fifth-lifts-d8dff9e38bad4a0a41a21679e5654609f36b7da36dbb84f996a0778bfa73eb50.json.gz","matrixSHA256":"4411183498cbdb63db83317b53436ac4deb4e374b517e22155254392cf2b3093","sha256":"d8dff9e38bad4a0a41a21679e5654609f36b7da36dbb84f996a0778bfa73eb50"}},"receiptBytes":22769,"receiptSHA256":"17361fc2f385bbc1ffe8b843d185d0c3acd2998276579d08e5d76e8233eaf036","receipt":"43740928483-infinity-fifth-true-shifted-incoming.json","binding":"ccacc20f5bf3e678c4b3fcab2090e25b84c72abb35440c9b0c8473fa007a8576"},"sixth":{"root":"infinity-complete-sixth-two-projection-failures","phases":{"prepared-complete-low":{"bytes":1123181,"file":"prepared-complete-low-017fa58f1168b117eb32ffea5f58ed47b6068664ba8d26e4fc08db5c1a454202.json.gz","sha256":"017fa58f1168b117eb32ffea5f58ed47b6068664ba8d26e4fc08db5c1a454202","temporaryOnly":true},"complete-sixth-cochains-verified":{"bytes":505256,"file":"complete-sixth-cochains-verified-d7795e363ab82725feb4666a735d815cf2406f033811bf25f4b322e247e0714d.json.gz","sha256":"d7795e363ab82725feb4666a735d815cf2406f033811bf25f4b322e247e0714d","temporaryOnly":true}},"receiptBytes":15274,"receiptSHA256":"9f126c0bd4d2cd15f44257d3a21e13d6987beb2061f7bbf6e9146e7a1c771ba4","receipt":"43740928483-infinity-complete-sixth-two-projection-failures.json","binding":"835fcb2ddcede187e1be808472d23a9e5a12472108b1320ac795e13be7f2e917"},"seventh":{"root":"infinity-complete-seventh-after-high-probe","phases":{"prepared-complete-low":{"bytes":1496220,"file":"prepared-complete-low-811eb06f809856f3f82856e9aef04b07edc6ec065a501d66ea921b9b5ad2527b.json.gz","sha256":"811eb06f809856f3f82856e9aef04b07edc6ec065a501d66ea921b9b5ad2527b","temporaryOnly":true},"complete-seventh-cochains-verified":{"bytes":610369,"file":"complete-seventh-cochains-verified-0bb0b469006bc7a15ffff11b7bcfedc772813cfcd75f8bda8ecdaede49a01841.json.gz","sha256":"0bb0b469006bc7a15ffff11b7bcfedc772813cfcd75f8bda8ecdaede49a01841","temporaryOnly":true}},"receiptBytes":12517,"receiptSHA256":"6faacedfb22582d79a2cefc73d97a8a11eeb0cdb024bc5c6d93de995a3102e65","receipt":"43740928483-infinity-complete-seventh-after-high-probe.json","binding":"8a9a52e60045cb4124f90e73ce2cb210d98f88acae2802287bd5e17a56d2ab42"},"eighth":{"root":"infinity-complete-eighth-after-high-probe","phases":{"prepared-complete-low":{"bytes":1957402,"file":"prepared-complete-low-cea2fd78c43d28a63f0755c38c3d2ef1ceb4454e335ef330a9c9a35f59e9da54.json.gz","sha256":"cea2fd78c43d28a63f0755c38c3d2ef1ceb4454e335ef330a9c9a35f59e9da54","temporaryOnly":true},"complete-eighth-cochains-verified":{"bytes":1067051,"file":"complete-eighth-cochains-verified-670b77067daff765b91ae4de5f7ba0f7cdfdf5be4593d1832768a021679c2950.json.gz","sha256":"670b77067daff765b91ae4de5f7ba0f7cdfdf5be4593d1832768a021679c2950","temporaryOnly":true}},"receiptBytes":13454,"receiptSHA256":"9c549e7fa9afbfa1e03aeb6844cda9a3ccd985357650612d114abc1ac0eb677a","receipt":"43756208221-infinity-complete-eighth-after-high-probe.json","binding":"a7e0fb67ccb7a92a8d98f8fcafd5442c64bb241fea5b59630e3644421f54b96e"},"ninth":{"root":"infinity-complete-ninth-after-high-probe","phases":{"prepared-complete-low":{"bytes":2529110,"file":"prepared-complete-low-9292577911853712a3494921a4f486321188a9e848fe580fc5ba0ef74371932d.json.gz","sha256":"9292577911853712a3494921a4f486321188a9e848fe580fc5ba0ef74371932d","temporaryOnly":true},"complete-next-cochains-verified":{"bytes":1738478,"file":"complete-next-cochains-verified-8ecbdc751bf5e4d35ffb8d950a033771a0e01c9ebf719cb33fee24c9b6ef7cd0.json.gz","sha256":"8ecbdc751bf5e4d35ffb8d950a033771a0e01c9ebf719cb33fee24c9b6ef7cd0","temporaryOnly":true}},"receiptBytes":14700,"receiptSHA256":"ef106d3f18b736ed0c5c76c0c0699d324ee2565ba92eecbcf400f6f5afb5035e","receipt":"43756208221-infinity-complete-ninth-after-high-probe.json","binding":"62f42f6e9a7add4a092bfeab2854f85af392ed11d6cf7741804d6addf6aa0435"},"tenth":{"root":"infinity-complete-tenth-after-high-probe","phases":{"prepared-complete-low":{"bytes":3062735,"file":"prepared-complete-low-8e785e4d6010f2fadacd7ef420126da5c65f32533106a8cca60d66ae3af9a118.json.gz","sha256":"8e785e4d6010f2fadacd7ef420126da5c65f32533106a8cca60d66ae3af9a118","temporaryOnly":true},"complete-next-cochains-verified":{"bytes":1380995,"file":"complete-next-cochains-verified-7e24eb520084c57124332ff6ece203eab95780325df9a6a26331d992bb1e9946.json.gz","sha256":"7e24eb520084c57124332ff6ece203eab95780325df9a6a26331d992bb1e9946","temporaryOnly":true}},"receiptBytes":15355,"receiptSHA256":"bd3bd1c9395562b2b34baed09864f2b2a5650f4f3a9da949c35f843e0b2cf0ad","receipt":"43756208221-infinity-complete-tenth-after-high-probe.json","binding":"a1d09b054f20b2830f448ea030c2ebd8ef805849ee0cf1ac616be69e163b43df"}}''')
PHASE_FORMATS={
 "projection":"r150-infinity-small-projection-temporary-v1",
 "fifth":"r150-infinity-fifth-shifted-incoming-temporary-v1",
 "sixth":"r150-infinity-complete-sixth-temporary-v1",
 "seventh":"r150-infinity-complete-seventh-temporary-v1",
 "eighth":"r150-infinity-complete-eighth-temporary-v1",
 "ninth":"r150-infinity-complete-next-temporary-v1",
 "tenth":"r150-infinity-complete-next-temporary-v1"}
EXPECTED=[4,0,1,3,1,1,1,1,0,1,1]
SPECTRUM=[1,1,1,1,3,4,4,4,5,6,7,8,10,11]
STOP=False
DEADLINE=0
REC=None
OUT=None
CACHE=None
BINDING=None
AUDIT={"rationalCoefficientsActuallyReduced":0,"maximumNumeratorDigits":0,
       "maximumDenominatorDigits":0,"allUsedDenominatorsUnitsModulo127":True}
INV=[0]+[pow(i,-1,P) for i in range(1,P)]

class GateFailure(Exception):pass
def require(ok,msg):
    if not ok:raise AssertionError(msg)
def gate(ok,msg):
    if not ok:raise GateFailure(msg)
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def objhash(x):return hashlib.sha256(canonical(x)).hexdigest()
def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for x in iter(lambda:f.read(1048576),b""):h.update(x)
    return h.hexdigest()
def atomic(path,obj):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp");t.write_bytes(canonical(obj));os.replace(t,p)
def check(stage):
    if STOP or time.monotonic()>=DEADLINE:raise TimeoutError(stage)
def stop(*_):
    global STOP
    STOP=True
def flush():
    if REC is None:return
    REC["elapsedSeconds"]=time.monotonic()-REC["_start"]
    REC["parameters"]["coefficientAudit"]=AUDIT
    x={k:v for k,v in REC.items() if not k.startswith("_")}
    require(len(canonical(x))<85000,"Small receipt remains below publishing limit")
    atomic(OUT,x)
def event(name,**kw):
    REC["events"].append({"phase":name,**kw});flush()
def qmod(value,label):
    s=str(value)
    if "/" in s:a,b=s.split("/")
    else:a,b=s,"1"
    n=int(a);d=int(b)
    require(d>0,"Positive canonical rational denominator")
    AUDIT["rationalCoefficientsActuallyReduced"]+=1
    AUDIT["maximumNumeratorDigits"]=max(AUDIT["maximumNumeratorDigits"],len(a.lstrip("-")))
    AUDIT["maximumDenominatorDigits"]=max(AUDIT["maximumDenominatorDigits"],len(b))
    if d%P==0:
        AUDIT["allUsedDenominatorsUnitsModulo127"]=False
        REC["parameters"]["firstNonintegralCoefficient"]={
            "label":label,"numeratorDigits":len(a.lstrip("-")),"denominatorDigits":len(b),
            "numeratorModulo127":n%P,"denominatorModulo127":0}
        raise GateFailure("This paid representative has a 127 denominator: "+label)
    return n%P*INV[d%P]%P
def mat(r,c,values=None):return nmod_mat(r,c,[0]*(r*c) if values is None else list(values),P)
def sub(M,rows,cols):
    rows=list(rows);cols=list(cols)
    return mat(len(rows),len(cols),(int(M[i,j]) for i in rows for j in cols))
def cat(blocks):
    require(blocks and len({x.nrows() for x in blocks})==1,"Horizontal dimensions")
    r=blocks[0].nrows()
    return mat(r,sum(x.ncols() for x in blocks),(int(x[i,j]) for i in range(r) for x in blocks for j in range(x.ncols())))
def vcat(blocks):
    require(blocks and len({x.ncols() for x in blocks})==1,"Vertical dimensions")
    return mat(sum(x.nrows() for x in blocks),blocks[0].ncols(),
               (int(x[i,j]) for x in blocks for i in range(x.nrows()) for j in range(x.ncols())))
def zero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def rank(M):return M.rref()[1]
def mh(M):
    h=hashlib.sha256();h.update(("%d,%d\n"%(M.nrows(),M.ncols())).encode("ascii"))
    for i in range(M.nrows()):
        h.update(("\t".join(str(int(M[i,j])) for j in range(M.ncols()))+"\n").encode("ascii"))
    return h.hexdigest()
def readM(x,label):
    require(isinstance(x,dict) and x.get("_exactMatrix") is True,"Complete exact matrix "+label)
    r,c=x["shape"];rows=x["rows"]
    require(len(rows)==r and all(len(row)==c for row in rows),"Exact shape "+label)
    return mat(r,c,(qmod(v,label+"[%d,%d]"%(i,j)) for i,row in enumerate(rows) for j,v in enumerate(row)))
def load_phase(a,key,name):
    spec=PINS[key];d=spec["phases"][name]
    p=Path(a.work_root)/spec["root"]/d["file"]
    require(Path(d["file"]).name==d["file"],"Paid phase basename")
    require(p.stat().st_size==d["bytes"] and sha(p)==d["sha256"],"Paid complete phase bytes: "+key+"/"+name)
    with gzip.open(p,"rt",encoding="utf-8") as f:o=json.load(f)
    require(o["format"]==PHASE_FORMATS[key] and o["binding"]==spec["binding"] and
            o["phase"]==name and o["complete"] is True,"Paid full phase identity: "+key+"/"+name)
    return o
def coefficient_decode(x):
    require(x["chart"]=="infinity" and x["maxOrder"]>=11,"Original natural infinity through eleven")
    c={"pure":[[qmod(v,"pure") for v in row] for row in x["pure"]],
       "linear":{int(j):[[[qmod(v,"linear") for v in row] for row in mode] for mode in modes]
                 for j,modes in x["linear"].items()},
       "quadratic":{(a,b):[[qmod(v,"quadratic") for v in row] for row in q] for a,b,q in x["quadratic"]}}
    require(len(c["pure"])>=12 and all(len(row)==17 for row in c["pure"]),"All original seventeen equations")
    require(set(c["linear"])==set(range(2,11)) and len(c["quadratic"])==45,"All normal linear/quadratic terms")
    require(all(not x for i in (0,1) for x in c["pure"][i]),"Actual F0/F1 pure vanish")
    return c
def phase_record(name,data):
    p=CACHE/(name+".json")
    payload={"format":FORMAT,"binding":BINDING,"complete":True,"data":data}
    if p.exists():
        old=json.loads(p.read_bytes())
        require(old==payload,"Same completed finite-field phase on continuation")
    else:atomic(p,payload)
    REC["parameters"].setdefault("completedPhaseIdentities",{})[name]={"bytes":p.stat().st_size,"sha256":sha(p)}
    flush()
def get_ledger(name,identity):
    p=CACHE/(name+".json")
    if p.exists():
        o=json.loads(p.read_bytes())
        require(o["format"]==FORMAT and o["binding"]==BINDING and o["identity"]==identity,"Same original verification ledger")
        return o
    return {"format":FORMAT,"binding":BINDING,"identity":identity,"orders":[],"productCoordinates":0}
def put_ledger(name,o):
    atomic(CACHE/(name+".json"),o)
    REC["parameters"].setdefault("originalVerificationLedgers",{})[name]={
        "orders":o["orders"],"productCoordinates":o["productCoordinates"],"sha256":sha(CACHE/(name+".json"))}
    flush()

class Original:
    def __init__(self,j,c):
        self.j=j;self.c=c
        self.rows=[j.source_rows(i) for i in range(4)]
        self.cols=[j.target_columns(i) for i in range(6)]
        self.indices=[{v:k for k,v in enumerate(x)} for x in self.cols]
        require([len(x) for x in self.rows]==[170,918,2295,2805],"All 6188 original sources")
        require([len(x) for x in self.cols]==[20,135,450,990,1485,1287],"All 4367 original outputs")
        require(len(set(sum(self.rows,[])))==6188,"No original source duplicates")
        self.terms={};self.nonzero={}
    def block_terms(self,k,sd,td):
        key=(k,sd,td)
        if key not in self.terms:
            check("complete original block")
            out=[]
            for i,row in enumerate(self.rows[sd]):
                vals={}
                for col,v in self.j.sparse_row_terms(self.c,k,row,td,self.indices[td]):
                    vals[col]=(vals.get(col,0)+int(v))%P
                out.append([(col,v) for col,v in sorted(vals.items()) if v])
            self.terms[key]=out
        return self.terms[key]
    def block(self,k,sd,td):
        M=mat(len(self.rows[sd]),len(self.cols[td]))
        for i,row in enumerate(self.block_terms(k,sd,td)):
            for c,v in row:M[i,c]=v
        return M
    def action(self,k,section,width):
        out=[]
        for sd in range(4):
            flat=[0]*(len(self.rows[sd])*width)
            for td,X in section.items():
                if not(sd<=td<=sd+2) or zero(X):continue
                require(X.nrows()==len(self.cols[td]) and X.ncols()==width,"All actual sector coordinates")
                nz=[[(b,int(X[a,b])) for b in range(width) if X[a,b]] for a in range(X.nrows())]
                for i,row in enumerate(self.block_terms(k,sd,td)):
                    base=i*width
                    for c,v in row:
                        for b,w in nz[c]:flat[base+b]+=v*w
            out.append(mat(len(self.rows[sd]),width,(v%P for v in flat)))
        return vcat(out)
    def jet(self,L,n):
        require(L,"Nonempty actual cochain")
        width=next(iter(L[0].values())).ncols();V=mat(6188,width)
        for k in range(min(n,len(L)-1)+1):
            check("whole original jet product")
            V+=self.action(n-k,L[k],width)
        return V
    def chain(self,name,L,nmax):
        width=next(iter(L[0].values())).ncols()
        identity=objhash({"through":nmax,"cochain":[{str(r):mh(M) for r,M in sec.items()} for sec in L]})
        ledger=get_ledger(name,identity)
        require(ledger["orders"]==list(range(len(ledger["orders"]))),"Complete ascending original products")
        for n in range(len(ledger["orders"]),nmax+1):
            V=self.jet(L,n);require(zero(V),"All 6188 original products: "+name+" order "+str(n))
            ledger["orders"].append(n);ledger["productCoordinates"]+=6188*width
            put_ledger(name,ledger)
        return ledger["productCoordinates"]

def lowseries(maps,high=None):
    require(not high or set(high).issubset(set(range(len(maps)))),"No high coefficient omitted by its order")
    L=[]
    for k,M in enumerate(maps):
        require(M.nrows()==155,"All original pure/one-normal coordinates")
        sec={0:sub(M,range(20),range(M.ncols())),1:sub(M,range(20,155),range(M.ncols()))}
        if high and k in high:sec.update(high[k])
        L.append(sec)
    return L
def head(L):return vcat([L[0][0],L[0][1]])
def select_series(L,cols):
    cols=list(cols);return [{r:sub(M,range(M.nrows()),cols) for r,M in sec.items()} for sec in L]
def high_decode(x,label):
    return {int(k):{int(r):readM(M,label) for r,M in sec.items()} for k,sec in x.items()}
def pack_series(pack,order):
    width=pack.ncols();L=[]
    require(pack.nrows()==930+1595*(order-5),"All actual packed coefficients")
    for k in range(order+1):
        p=155*k if k<6 else 930+1595*(k-6)
        sec={0:sub(pack,range(p,p+20),range(width)),1:sub(pack,range(p+20,p+155),range(width))}
        if k>=6:
            sec[2]=sub(pack,range(p+155,p+605),range(width))
            sec[3]=sub(pack,range(p+605,p+1595),range(width))
        L.append(sec)
    return L
def native_high(a,O,rhs,summary):
    require(rhs.nrows()==5100 and rhs.ncols()==1,"One actual original eleventh high RHS")
    root=Path(a.out)/"native";root.mkdir(parents=True,exist_ok=True)
    input_path=root/"original-high-one-rhs.bin"
    tmp=root/"original-high-one-rhs.bin.tmp";offset=[0,990,2475]
    original_zero=0
    with tmp.open("wb") as f:
        f.write(b"R15H7127");f.write(struct.pack("<4I",127,5100,3762,1));f.write(BINDING.encode("ascii"))
        pos=0
        for sd in (2,3):
            terms=[O.block_terms(0,sd,td) for td in (3,4,5)]
            for i in range(len(O.rows[sd])):
                row=[]
                for td,T in enumerate(terms):
                    row.extend((offset[td]+c,v) for c,v in T[i])
                row=sorted(row)
                require(len(row)<=77 and len({c for c,v in row})==len(row),"All original high row terms")
                if not row:original_zero+=1
                f.write(struct.pack("<H",len(row)))
                for c,v in row:f.write(struct.pack("<HB",c,v))
                f.write(bytes([int(rhs[pos,0])]))
                pos+=1
        require(pos==5100,"All original high rows written")
    os.replace(tmp,input_path)
    input_id={"bytes":input_path.stat().st_size,"sha256":sha(input_path)}
    cache=root/"checked-native-result.json"
    if cache.exists():
        o=json.loads(cache.read_bytes())
        require(o["binding"]==BINDING and o["input"]==input_id,"Same high input continuation")
        rp=root/"native-high-field127-receipt.json"
        require(sha(rp)==o["receiptSHA256"],"Saved actual native receipt")
        z=json.loads(rp.read_bytes())
    else:
        source=Path(a.native_source);header=Path(a.native_header)
        binary=root/"high127"
        log=root/"compile.log"
        cmd=["g++","-O3","-std=c++17","-I",str(header.parent),str(source),"-o",str(binary)]
        check("native compilation")
        with log.open("wb") as f:
            p=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=max(1,DEADLINE-time.monotonic()))
        require(p.returncode==0,"Native compilation: "+log.read_text(errors="replace")[-1500:])
        log=root/"run.log";check("native original high block")
        with log.open("wb") as f:
            p=subprocess.run([str(binary),str(input_path),str(root),str(max(1,DEADLINE-time.monotonic()-3))],
                stdout=f,stderr=subprocess.STDOUT,timeout=max(1,DEADLINE-time.monotonic()))
        if p.returncode==124:raise TimeoutError("native complete high block")
        require(p.returncode==0,"Native original high: "+log.read_text(errors="replace")[-2000:])
        rp=root/"native-high-field127-receipt.json";z=json.loads(rp.read_bytes())
        require(z["binding"]==BINDING and z["status"]=="completed","Actual complete native result")
        o={"binding":BINDING,"input":input_id,"receiptSHA256":sha(rp)}
        if z["rhsCompatible"]:o["particularSHA256"]=sha(root/"actual-high-particular.json")
        atomic(cache,o)
    require(z["prime"]==127 and z["originalSourceRows"]==5100 and z["originalTargetCoordinates"]==3762
        and z["all5100OriginalRowsRetained"] and z["all3762OriginalColumnsRetained"]
        and z["allDependentOriginalCoefficientRowsZero"] and z["actualUnitMinorVerified"],"Native complete scope")
    summary["nativeHigh"]=z;summary["nativeInput"]=input_id;flush()
    gate(z["rank"]==3760,"The fixed-127 complete high block does not have the paid rational rank")
    particular=None
    if z["rhsCompatible"]:
        pp=root/"actual-high-particular.json"
        require(sha(pp)==o["particularSHA256"],"Actual compatible particular bytes")
        v=json.loads(pp.read_bytes())
        require(v["binding"]==BINDING and v["all5100OriginalProductsVerified"] and len(v["values"])==3762,
                "Actual original high particular")
        particular={3:mat(990,1,v["values"][:990]),4:mat(1485,1,v["values"][990:2475]),
                    5:mat(1287,1,v["values"][2475:])}
        checkv=O.action(0,particular,1)
        require(sub(checkv,range(1088,6188),[0])==rhs,"Independent all5100 particular products")
    # Never read a stale particular when rhsCompatible is false.
    phase_record("complete-high",{"rank":z["rank"],"compatible":z["rhsCompatible"],
        "augmentedRank":z["augmentedRank"],"input":input_id,"nativeReceiptSHA256":o["receiptSHA256"]})
    return z,particular

def main():
    global DEADLINE,REC,OUT,CACHE,BINDING
    p=argparse.ArgumentParser()
    for x in ("work-root","receipt-dir","q13-receipt","jet-actions","native-source","native-header","out"):
        p.add_argument("--"+x,required=True)
    p.add_argument("--remaining-seconds",type=float,default=600)
    p.add_argument("--memory-mib",type=int,default=4096)
    a=p.parse_args()
    require(60<=a.remaining_seconds<=1800 and 1024<=a.memory_mib<=8192,"Finite qualification budget")
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    start=time.monotonic();DEADLINE=start+a.remaining_seconds-min(12,a.remaining_seconds/10)
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    OUT=out/"infinity-complete-prime127-qualification-receipt.json"
    CACHE=out/"checkpoints";CACHE.mkdir(parents=True,exist_ok=True)
    REC={"format":FORMAT,"status":"running","outcome":"pending-paid-integral-inputs","_start":start,
       "scriptSHA256":sha(__file__),"parameters":{"prime":127,"author":"Astra-ISP-789f / literature_audit",
       "aiAssisted":"GPT-6 Astra Pro","inputSourceRows":6188,"inputOutputCoordinates":4367,
       "usesOld5528SourceFrame":False,"new4340GaussianEliminations":0,
       "allAncestorFilesReadOnly":True,"largeDataUploadedOrCommitted":False,
       "completeInfinityQualification":False,"remainingSeconds":a.remaining_seconds,
       "memoryMiB":a.memory_mib,"allArraysTemporaryOnly":True},"events":[]}
    code=1
    try:
        require(sha(a.jet_actions)==ACTIONS_SHA and sha(a.native_source)==NATIVE_SHA
             and sha(a.native_header)==HEADER_SHA,"Exact source/header/action pins")
        require(Path(a.q13_receipt).stat().st_size==Q13_BYTES and sha(a.q13_receipt)==Q13_SHA,"Actual Q13 receipt")
        q13=json.loads(Path(a.q13_receipt).read_bytes())["result"]
        require(q13["status"]=="completed" and q13["all17WholeNaturalPhysicalPolynomialsMatched"]
             and q13["all4433OriginalParameterCoefficientsVerified"]
             and q13["sourceAndOutputChangesArePolynomialUnits"],"Same original primitive natural parameter")
        scales=[qmod(v,"original primitive row scale") for v in q13["parameters"]["actual17ConstantRowScales"]]
        gate(len(scales)==17 and all(scales),"All original seventeen row scales are 127 units")
        # Exact determinants of the paid polynomial coordinate changes.
        d2=-64701092257700249600
        d3=23366320238786911411830138211362846399922176000
        gate(d2%P and d3%P,"Original physical coordinate determinant units")
        REC["parameters"]["original17RowScalesModulo127"]=scales
        REC["parameters"]["physicalCoordinateDeterminantsModulo127"]=[d2%P,d3%P]
        receipts={}
        for key,spec in PINS.items():
            fp=Path(a.receipt_dir)/spec["receipt"]
            require(fp.stat().st_size==spec["receiptBytes"] and sha(fp)==spec["receiptSHA256"],
                    "Paid complete parent receipt "+key)
            o=json.loads(fp.read_bytes());r=o.get("result",o)
            require(r["status"]=="completed","Completed paid parent "+key);receipts[key]=r
        BINDING=objhash({"format":FORMAT,"sourceSHA256":sha(__file__),"prime":127,
            "paidAncestors":PINS,"q13SHA256":Q13_SHA,"actionsSHA256":ACTIONS_SHA,
            "nativeSHA256":NATIVE_SHA,"headerSHA256":HEADER_SHA})
        REC["parameters"]["binding"]=BINDING
        REC["parameters"]["paidReceiptIdentities"]={k:{"bytes":v["receiptBytes"],"sha256":v["receiptSHA256"]}
                                                   for k,v in PINS.items()}
        spec=importlib.util.spec_from_file_location("r150_127_original_actions",a.jet_actions)
        j=importlib.util.module_from_spec(spec);spec.loader.exec_module(j)
        raw=load_phase(a,"projection","original-projection-coefficients")["data"]
        coeff=coefficient_decode(raw["coefficients"]);O=Original(j,coeff)
        REC["parameters"]["originalCoefficientFieldSHA256"]=objhash({
          "pure":coeff["pure"],"linear":coeff["linear"],
          "quadratic":[[list(k),v] for k,v in sorted(coeff["quadratic"].items())]})
        for r in (0,1):
            require(zero(O.block(0,r,0)),"All omitted pure constant target columns exactly zero")
        zobj=load_phase(a,"fifth","high-fifth-lifts")
        require(zobj["shape"]==[999,11],"Paid full high-fifth lift dimensions")
        zrows=[row[:2] for row in zobj["matrix"][:990]]
        Z3=mat(990,2,(qmod(v,"actual full homogeneous Z3") for row in zrows for v in row))
        gate(rank(Z3)==2,"Two actual homogeneous high columns retain rank")
        Zaction=O.action(0,{3:Z3},2)
        require(zero(sub(Zaction,range(1088,6188),range(2))),"All10200 actual homogeneous high products")
        C=cat([vcat([cat([O.block(0,sd,td) for td in (1,2)]) for sd in (0,1)]),
               sub(Zaction,range(1088),range(2))])
        require((C.nrows(),C.ncols())==(1088,587),"Complete constant low correction block")
        constant_rank=rank(C);gate(constant_rank==580,"Complete low constant rank modulo127")
        phase_record("constant-low",{"rank":constant_rank,"shape":[1088,587],"matrixSHA256":mh(C),
                                     "homogeneousHighProducts":10200})
        event("original coefficient units and complete constant low block verified",rank=constant_rank)
        state=load_phase(a,"projection","Q-smith-state")["data"]
        require(state["complete"] is True,"Paid complete rational projected Smith state")
        projected=[]
        for gi,g in enumerate(state["positive"]):
            e=g["exponent"]
            maps=[readM(M,"projected positive %d/%d"%(e,k)) for k,M in enumerate(g["map"][:e+1])]
            L=lowseries(maps);O.chain("projected-positive-%d"%gi,L,e-1)
            R=O.jet(L,e);require(zero(sub(R,range(1088,6188),range(R.ncols()))),"All original high rows of projected maps")
            projected.append({"exponent":e,"series":L,"residual":sub(R,range(1088),range(R.ncols()))})
        free=lowseries([readM(M,"projected free %d"%k) for k,M in enumerate(state["map"][:12])])
        require(len(free)==12,"Projected free maps through eleven")
        gate(rank(head(free))==13,"Thirteen original free heads retain rank")
        O.chain("projected-free-through-eleven",free,11)
        allheads=cat([head(g["series"]) for g in projected]+[head(free)])
        gate(allheads.ncols()==27 and rank(allheads)==27,"Complete original constant head frame modulo127")
        O.chain("all-projected-constant-heads",
                [{0:sub(allheads,range(20),range(27)),1:sub(allheads,range(20,155),range(27))}],0)
        previous=0;early=[];W=[]
        for e in range(1,6):
            W.extend(g["residual"] for g in projected if g["exponent"]==e)
            actual=rank(cat([C]+W));beta=actual-constant_rank-previous
            gate(beta==EXPECTED[e-1],"Original early connection differs at order "+str(e))
            previous=actual-constant_rank;early.append(beta)
        require(previous==9,"All nine early incoming directions")
        phase_record("first-five",{"ranks":early,"headFrameRank":27,"incomingRank":previous,
            "constantRankConditionalOnCompleteHigh":4340,
            "allOriginalProjectedMapsVerified":True})
        REC["parameters"]["firstFiveConnectionsConditionalOnHigh"]=early
        latest=None
        headcounts={6:17,7:16,8:15,9:15,10:14}
        for n,key in zip(range(6,11),("sixth","seventh","eighth","ninth","tenth")):
            check("paid complete stage "+key)
            d=load_phase(a,key,"prepared-complete-low")["data"]
            M=readM(d["M"],key+" complete low")
            require(sub(M,range(1088),range(587))==C,"Same full original constant block at "+key)
            imaps=[readM(x,key+" incoming") for x in d["incomingMaps"]]
            map_key="twoMaps" if n<=8 else "representativeMaps"
            rmaps=[readM(x,key+" representative") for x in d[map_key]]
            require(len(imaps)==n+1 and len(rmaps)==n+1,"Every prepared coefficient is retained")
            # The seventh/eighth creators predate the generic dictionary schema.
            # Read each actual historical key, including its nonzero high parts.
            if n==6:
                ih={};rh={}
            elif n==7:
                ih={}
                rh={6:{2:readM(d["sixthNormalTwo"],key+" representative order6 normal2"),
                       3:readM(d["sixthNormalThree"],key+" representative order6 normal3")}}
            elif n==8:
                ih={7:{2:readM(d["incomingSeventhNormalTwo"],key+" incoming order7 normal2"),
                       3:readM(d["incomingSeventhNormalThree"],key+" incoming order7 normal3")}}
                rh={6:{2:readM(d["sixthNormalTwo"],key+" representative order6 normal2"),
                       3:readM(d["sixthNormalThree"],key+" representative order6 normal3")},
                    7:{2:readM(d["seventhNormalTwo"],key+" representative order7 normal2"),
                       3:readM(d["seventhNormalThree"],key+" representative order7 normal3")}}
            else:
                ih=high_decode(d["incomingHigh"],key+" incoming high")
                rh=high_decode(d["representativeHigh"],key+" representative high")
            incoming=lowseries(imaps,ih);reps=lowseries(rmaps,rh)
            require(zero(head(incoming)),"Every lower incoming map has zero original leading head")
            O.chain(key+"-all-incoming",incoming,n-1);O.chain(key+"-all-representatives",reps,n-1)
            WI=O.jet(incoming,n);RR=O.jet(reps,n)
            require(zero(sub(WI,range(1088,6188),range(WI.ncols()))) and
                    zero(sub(RR,range(1088,6188),range(RR.ncols()))),
                    "All 5100 original forcing rows vanish only after actual verification")
            WI=sub(WI,range(1088),range(WI.ncols()));RR=sub(RR,range(1088),range(RR.ncols()))
            require(M==cat([C,WI,RR]),"All actual complete low columns reproduced")
            pref=rank(cat([C,WI]));total=rank(M);beta=total-pref
            gate(pref==580+sum(EXPECTED[:n-1]) and WI.ncols()==sum(EXPECTED[:n-1]),
                 "Complete independent incoming image at "+key)
            gate(beta==EXPECTED[n-1],"Complete field connection differs at "+key)
            pname="complete-"+key+"-cochains-verified" if n<=8 else "complete-next-cochains-verified"
            done=load_phase(a,key,pname)["data"];pack=readM(done["pack"],key+" full actual cochain")
            L=pack_series(pack,n)
            gate(pack.ncols()==headcounts[n] and rank(head(L))==headcounts[n],"All full original heads retain rank")
            O.chain(key+"-complete-cochain",L,n)
            md={"order":n,"prefixRank":pref,"totalRank":total,"connectionRank":beta,
                "fullHeadCount":headcounts[n],"wholeCochainSHA256":mh(pack),
                "completeLowSHA256":mh(M),"all6188OriginalProductsVerified":True,"conditionalOnHighRank3760":True}
            phase_record(key,md);REC["parameters"].setdefault("actualConnections",[]).append(md)
            event("whole original connection qualified conditional on high rank",order=n,beta=beta,heads=headcounts[n])
            latest={"L":L,"incoming":incoming,"representatives":reps,"W":WI,"R":RR}
        # No old F31 upper bound is used for the new eleventh page.
        L=latest["L"];H=head(L);F=head(free)
        gate(rank(cat([F,H]))==14,"Thirteen free heads are in the actual fourteen-head space")
        choice=next((c for c in range(14) if rank(cat([F,sub(H,range(155),[c])]))==14),None)
        require(choice is not None,"One complete eleventh quotient representative")
        last=select_series(L,[choice]);R11=O.jet(last,11)
        incoming12=latest["W"];R10=latest["R"]
        failed=next((c for c in range(R10.ncols()) if rank(cat([C,incoming12,sub(R10,range(1088),[c])]))==593),None)
        require(failed is not None,"A true independent tenth failed class")
        incoming13=cat([incoming12,sub(R10,range(1088),[failed])])
        require(rank(cat([C,incoming13]))==593,"Complete thirteen-dimensional lower incoming image")
        # These are whole previous maps multiplied by u, not only their last coefficients.
        zero_in={r:mat(M.nrows(),M.ncols()) for r,M in latest["incoming"][0].items()}
        shifted_in=[zero_in]+latest["incoming"]
        failseries=select_series(latest["representatives"],[failed])
        shifted_fail=[{r:mat(M.nrows(),1) for r,M in failseries[0].items()}]+failseries
        O.chain("eleventh-whole-shifted-incoming12",shifted_in,10)
        O.chain("eleventh-whole-shifted-failure1",shifted_fail,10)
        Q1=O.jet(shifted_in,11);Q2=O.jet(shifted_fail,11)
        require(zero(sub(Q1,range(1088,6188),range(12))) and zero(sub(Q2,range(1088,6188),[0])),
                "All eleventh incoming high coordinates actually zero")
        require(cat([sub(Q1,range(1088),range(12)),sub(Q2,range(1088),[0])])==incoming13,
                "Complete incoming original transports")
        Rhigh=sub(R11,range(1088,6188),[0]);Rlow=sub(R11,range(1088),[0])
        REC["parameters"]["eleventhPreparation"]={"chosenFullTenthHead":choice,
            "chosenOriginalTenthFailure":failed,"originalHighForcingZero":zero(Rhigh),
            "originalHighForcingSHA256":mh(Rhigh),"originalLowForcingSHA256":mh(Rlow),
            "incomingColumns":13,"incomingRank":13,"incomingSHA256":mh(incoming13),
            "allWholeIncomingMapsRetained":True,"allLowerOriginalProductsVerified":True}
        phase_record("eleventh-inputs",REC["parameters"]["eleventhPreparation"])
        z,particular=native_high(a,O,-Rhigh,REC["parameters"])
        REC["parameters"]["fullOriginalConstantRankModulo127"]=3760+580
        REC["parameters"]["firstTenConnections"]=EXPECTED[:10]
        REC["parameters"]["allConditionalHighRankGatesDischarged"]=True
        if not z["rhsCompatible"]:
            beta11=1;corrected=None
            reason="actual complete high RHS is outside the complete high image"
        else:
            extra=O.action(0,particular,1)
            require(zero(sub(R11+extra,range(1088,6188),[0])),"Actual complete eleventh high correction")
            corrected=Rlow+sub(extra,range(1088),[0])
            rr=rank(cat([C,incoming13,corrected]))
            require(rr in (593,594),"One actual final head class")
            beta11=rr-593;reason="actual complete high particular and full low quotient"
        REC["parameters"]["eleventhConnection"]={"rank":beta11,"reason":reason,
            "correctedLowSHA256":None if corrected is None else mh(corrected),
            "originalAll6188RowsRetained":True,"oldField31LengthUpperUsed":False,
            "stableOriginalFreeHeadCount":13}
        actual=EXPECTED[:10]+[beta11]
        if beta11==1:
            REC["parameters"].update({"completeInfinityQualification":True,
              "completeField127ConnectionRanks":actual,"completeField127PositiveSpectrum":SPECTRUM,
              "completeField127PositiveLength":66,"completeField127SubmaximalLength":55,
              "completeField127MaximumPositiveIndex":11,"completeField127GenericRank":4354,
              "completeField127FreeRank":13,"sameNaturalOriginalQAndField127Spectrum":True,
              "genericRankUpperUsesExactOriginalRationalVanishingMinors":True,
              "lastPositiveIndexElevenActuallyChecked":True})
            REC["outcome"]="complete-original-infinity-prime127-qualified"
        else:
            REC["parameters"].update({"completeInfinityQualification":False,
              "completeField127ConnectionRanksThroughEleven":actual,
              "anyAdditionalPositiveIndexIsAtLeast":12,
              "remainingDirectionMayInsteadBeGenericallyFree":True,
              "sameNaturalOriginalQAndField127Spectrum":False})
            REC["outcome"]="actual-eleventh-page-disproves-this-spectrum-agreement"
        phase_record("final",{"outcome":REC["outcome"],"ranks":actual,
                              "completeInfinityQualification":REC["parameters"]["completeInfinityQualification"]})
        REC["status"]="completed";code=0
    except GateFailure as e:
        REC["status"]="qualification-gate-not-met";REC["outcome"]="no-prime127-qualification-inferred"
        REC["parameters"]["failedGate"]=str(e);code=3
    except (TimeoutError,subprocess.TimeoutExpired) as e:
        REC["status"]="prefix-completed";REC["outcome"]="verified-phases-saved-before-budget"
        REC["parameters"]["budgetBoundary"]=str(e);code=75
    except BaseException as e:
        REC["status"]="failed";REC["outcome"]="no-unverified-qualification"
        REC["parameters"]["errorType"]=type(e).__name__;REC["parameters"]["errorMessage"]=str(e);code=1
    finally:
        flush();print(json.dumps({"status":REC["status"],"outcome":REC["outcome"],
            "receipt":str(OUT),"elapsedSeconds":time.monotonic()-start}),flush=True)
    if code:raise SystemExit(code)
if __name__=="__main__":main()
