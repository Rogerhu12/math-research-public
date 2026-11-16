#!/usr/bin/env python3
"""Original critical positive jets with the complete quadratic tangent-degree2 slice.

Astra-ISP-789f / literature_audit; AI-assisted with GPT-6 Astra Pro.
2026-11-16. Same original17/6188/4367 frame, exact Q(alpha).
Reads immutable completed weak-slice parents. No parent is mutated.
Reuses the paid eleven canonical low chains and their actual25 unit.
Only positive full-jet lower bounds are reported. A zero gain is restricted.

The high slice has270 coordinates initially; genuine pure d^2 kills45.
A34x20 pencil followed by a153x(at most49) symmetric compatibility system
gives at most5 legal high columns. Full products verify all6086 outside rows.
The102x59 low block uses all old36 coordinates, five pure degree4 coordinates,
and18 one-normal c^2/cd coordinates. Its new canonical heads are the old11
plus two exact pure degree4 columns; no new canonical series is solved.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq

FORMAT="r150-critical-quadratic-tangent-two-positive-jets-v1"
WEAK_SHA="f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b"
PINS={
 "generator":"2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
 "jet_actions":"2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
 "low_generator":"4d215c80fa40d5f3548fd604e4ed77c6317db44b5b80518a03cf15e2ceeffa2f",
 "field_helper":"54f88bdbd926d38fb7a78fdaa1128f6bae96617461e4d2d4e4064736f6cf842c"}

PARENT_PINS={
  "plus": {
    "receiptBytes": 29268,
    "receiptSHA256": "30043fb3e263f861166f439c198af93bc10a69a8c5940acad42fe0429c3d86e6",
    "binding": "fc1dd340764a2c3f419f2f8fa2cb13581585be8af1a680871ddac1d7fa157593",
    "rawBytes": 14425,
    "rawSHA256": "c7b70b2ec6155d0d9e3e4dc706ba5c39b3cd6433383458551f695c162600557e",
    "manifest": {
      "bytes": 10739,
      "file": "checkpoints/manifest.json",
      "sha256": "3a6c668298211eb5831ab35876f59ce88be6f164f50077a7dbb2e8f402aa8e98"
    }
  },
  "minus": {
    "receiptBytes": 29275,
    "receiptSHA256": "708cc521471fd10e493be27c206420ca34ef89db71a52791e3e0b5e21eb1954f",
    "binding": "108c040d0df21708a57e1bdc8ba64d796ad894d066476efa56871abd2ffa976d",
    "rawBytes": 14429,
    "rawSHA256": "79ef5a020dcdbf1a113eed0940208f5bad7449a6b4467f6c886429c708776885",
    "manifest": {
      "bytes": 10740,
      "file": "checkpoints/manifest.json",
      "sha256": "529a47b394c74f08558ef775f9a477c88d8a966ad536e06f85a10268dd6e8098"
    }
  },
  "e8": {
    "receiptBytes": 29037,
    "receiptSHA256": "8b17d7ffc4bc63f6a8d8d7be42df1767c8fe1088958e4a8745e394ef4898d211",
    "binding": "6b2bd281d07a3796c302c5ca8a09d00f22433fb9501c62ff0df682733d8ce7f5",
    "rawBytes": 14267,
    "rawSHA256": "dc8f194bbc11634cf60b3b40968ff3123d2cd60f61a87a752e7925e8744c90f7",
    "manifest": {
      "bytes": 10411,
      "file": "checkpoints/manifest.json",
      "sha256": "555f91cb50825c78aec5bafc8289bc277fd9f8a30e76a775f7aaa33bf49fdcf3"
    }
  }
}

def require(ok,message):
    if not ok:
        raise AssertionError(message)

def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":")).encode()

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for x in iter(lambda:f.read(1048576),b""):
            h.update(x)
    return h.hexdigest()

def module_at(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec)
    sys.modules[name]=m
    spec.loader.exec_module(m)
    return m

class BudgetStop(Exception):
    pass

class Cache:
    def __init__(self,root,binding):
        self.root=Path(root)
        self.root.mkdir(parents=True,exist_ok=True)
        self.binding=binding
        self.path=self.root/"manifest.json"
        if self.path.exists():
            self.manifest=json.loads(self.path.read_text())
            require(self.manifest["format"]==FORMAT and
                    self.manifest["binding"]==binding,"Same immutable phase ancestry")
        else:
            self.manifest={"format":FORMAT,"binding":binding,"stages":{}}
            self.flush()
    def flush(self):
        tmp=self.path.with_name("manifest.json.tmp")
        tmp.write_bytes(canonical(self.manifest))
        tmp.replace(self.path)
    def put(self,name,obj,verified):
        require("/" not in name,"Local phase name")
        payload={"format":FORMAT,"binding":self.binding,"stage":name,
                 "verified":bool(verified),"payload":obj}
        raw=canonical(payload)
        digest=hashlib.sha256(raw).hexdigest()
        path=self.root/(name+"-"+digest+".json.gz")
        if not path.exists():
            tmp=path.with_name(path.name+".tmp")
            with open(tmp,"wb") as f:
                with gzip.GzipFile(filename="",fileobj=f,mode="wb",
                                   compresslevel=1,mtime=0) as z:
                    z.write(raw)
            tmp.replace(path)
        record={"file":path.name,"bytes":path.stat().st_size,
                "sha256":sha_file(path),"payloadSHA256":digest,
                "verified":bool(verified),"temporaryOnly":True}
        self.manifest["stages"][name]=record
        self.flush()
        return record
    def get(self,name):
        r=self.manifest["stages"].get(name)
        if r is None:
            return None
        path=self.root/r["file"]
        require(path.stat().st_size==r["bytes"] and sha_file(path)==r["sha256"],
                "Saved phase complete bytes and SHA")
        with gzip.open(path,"rb") as z:
            raw=z.read()
        require(hashlib.sha256(raw).hexdigest()==r["payloadSHA256"],
                "Saved phase canonical payload SHA")
        obj=json.loads(raw)
        require(obj["format"]==FORMAT and obj["binding"]==self.binding and
                obj["stage"]==name and obj["verified"]==r["verified"],
                "Saved phase semantic binding and verified status")
        return obj["payload"]


class Parent:
    """Read only; a failed or unbound phase is never promoted."""
    def __init__(self,w,root,receipt,field):
        pin=PARENT_PINS[field]
        path=Path(receipt)
        require(path.stat().st_size==pin["receiptBytes"] and
                sha_file(path)==pin["receiptSHA256"],"Exact completed parent outer")
        outer=json.loads(path.read_text())
        result=outer["result"]
        require(outer["exitCode"]==0 and result["status"]=="completed" and
                result["scriptSHA256"]==WEAK_SHA and
                result["binding"]==pin["binding"] and
                outer["fullTemporaryReceiptBytes"]==pin["rawBytes"] and
                outer["fullTemporaryReceiptSHA256"]==pin["rawSHA256"],
                "Same completed original weak-slice parent")
        params=result["parameters"]
        require(params["field"]==field and params["allOriginal6188JetProductsZero"]
                and params["actualCanonicalLow"]["allEarlierRowsZero"]
                and params["candidateLeadingRank"]==9,
                "Original parent mathematical gates")
        self.root=Path(root)/"checkpoints"
        manifest=self.root/"manifest.json"
        require(manifest.stat().st_size==pin["manifest"]["bytes"] and
                sha_file(manifest)==pin["manifest"]["sha256"],"Pinned parent manifest")
        self.cache=w.Cache(self.root,pin["binding"])
        self.result=result
        self.pin=pin
    def get(self,name):
        record=self.cache.manifest["stages"].get(name)
        require(record is not None and record["verified"],
                "Only a complete verified original parent phase: "+name)
        value=self.cache.get(name)
        require(value is not None,"Required original parent phase")
        return value

def original_low_support(actions):
    cols=actions.target_columns(0)+actions.target_columns(1)
    low=[key for key in cols if
         (not key[2] and sum(key[:2])<=4) or
         (len(key[2])==1 and sum(key[:2])<=2 and key[1]<=1)]
    exact=[key for key in actions.target_columns(0)
           if sum(key[:2])==5 and key[1]<=1]
    full=[row for r in range(4) for row in actions.source_rows(r)]
    rows=[i for i,(_,a,b,mon) in enumerate(full) if not mon and a+b<=2]
    old_rows=[i for i,(_,a,b,mon) in enumerate(full) if not mon and a+b<=1]
    require((len(low),len(exact),len(rows),len(old_rows))==(59,2,102,51),
            "Complete original expanded low support")
    return low,exact,rows,old_rows

def expanded_low(F,h,w,actions,coeff,parent,cache,order,report):
    low,exact,rows,old_rows=original_low_support(actions)
    oldpoly=parent.get("original-polynomial-model")
    oldlow=[(a,b,tuple(mon)) for a,b,mon in oldpoly["meta"]["lowTargetColumns"]]
    require(len(oldlow)==36,"All original parent low columns")
    oldjets=parent.get("canonical-low-jets")
    Xold=[F.matrix_from_json(a) for a in oldjets["jets"]]
    require(len(Xold)==order+1 and all(h.shape(a)==(36,11) for a in Xold),
            "All eleven parent canonical chains")
    oldunitmeta=parent.get("constant-low-kernel")
    require(oldunitmeta["rank"]==25,"Original parent constant unit")
    oldpos={r:i for i,r in enumerate(old_rows)}
    rowpos={r:i for i,r in enumerate(rows)}
    index={key:i for i,key in enumerate(low)}
    embed_columns=[index[key] for key in oldlow]
    old_rows_in_new=[rowpos[r] for r in old_rows]
    oldnorm=oldjets["normalization"]["nonzeroRationalRowContents"]
    E=w.embed_low(F,h,actions,low,h.identity(F,59))
    raw=[]
    allowed=set(rows)
    for k in range(order+1):
        product=w.action(F,h,actions,coeff,k,E,59)
        require(all(not x for i,row in enumerate(product)
                    if i not in allowed for x in row),
                "Every expanded low coefficient kills all6086 other sources")
        raw.append(h.submatrix(product,rows,range(59)))
    _,units=w.rational_rows(raw[0])
    for r in old_rows:
        units[rowpos[r]]=fmpq(oldnorm[oldpos[r]])
    series=[[[x/units[i] for x in row] for i,row in enumerate(a)] for a in raw]
    require(all(x*units[i]==y for A,B in zip(series,raw)
                for i,(ra,rb) in enumerate(zip(A,B)) for x,y in zip(ra,rb)),
            "All original expanded row-content identities")
    # Parent jets and old low Taylor products are not recomputed by elimination.
    # Their original physical columns are compared after exact row transport.
    def old_series_hashes():
        return [F.matrix_hash(h.submatrix(a,old_rows_in_new,embed_columns)) for a in series]
    require(hashlib.sha256(canonical(old_series_hashes())).hexdigest()==
            oldjets["seriesIdentity"],"Every old Taylor matrix matches parent identity")
    extra=[key for key in exact_degree_four(actions) if key in index]
    require(len(extra)==2,"Exactly two newly included exact pure degree4 heads")
    jets=[]
    for k,X in enumerate(Xold):
        Y=h.zeros(F,59,13)
        for i,j in enumerate(embed_columns):
            Y[j][:11]=X[i][:]
        if k==0:
            for j,key in enumerate(extra):
                Y[index[key]][11+j]=F.one
        jets.append(Y)
    residual=None
    for k in range(order+1):
        R=h.zeros(F,102,13)
        for i in range(k+1):
            R=w.add_matrices(R,h.product(F,series[i],jets[k-i]))
        if k<order:
            require(h.zero_matrix(R),"All expanded earlier51+51 rows vanish")
        residual=R
    oldR=F.matrix_from_json(oldjets["exitResidual"])
    require(h.submatrix(residual,old_rows_in_new,range(11))==oldR and
            all(not residual[i][j] for i in range(102) for j in (11,12)),
            "Original eleven exit columns and two exact new columns retained")
    oldpivrows=[old_rows_in_new[i] for i in oldunitmeta["independentRows"]]
    oldpivcols=[embed_columns[i] for i in oldunitmeta["independentColumns"]]
    U=h.submatrix(series[0],oldpivrows,oldpivcols)
    saved=parent.get("canonical-low-original-unit-unit-lu")
    require(saved["inputSHA256"]==F.matrix_hash(U),"Exact old25 unit reused")
    factor=(F.matrix_from_json(saved["L"]),F.matrix_from_json(saved["U"]),saved["rows"])
    require(h.product(F,factor[0],factor[1])==[U[i] for i in factor[2]],
            "All625 reused original LU products")
    payload={"series":[F.matrix_json(a) for a in series],
             "jets":[F.matrix_json(a) for a in jets],
             "exitResidual":F.matrix_json(residual),
             "lowColumns":[[a,b,list(mon)] for a,b,mon in low],
             "originalLowSourceRows":rows,"rowContents":[str(x) for x in units],
             "oldUnitRows":oldpivrows,"oldUnitColumns":oldpivcols,
             "oldUnitSHA256":F.matrix_hash(U),
             "allParentTaylorMatricesExactlyMatched":True,
             "allOriginalExpandedEmbeddingRowsVerified":True}
    cache.put("expanded-original-low-and-parent-chains",payload,True)
    return low,exact,rows,units,series,jets,residual,oldpivrows,oldpivcols,U,factor

def exact_degree_four(actions):
    return [key for key in actions.target_columns(0)
            if sum(key[:2])==4 and key[1]<=1]

def slice_columns(F,h,w,actions,coeff,parent,cache,report,rows,units):
    L=[[coeff["linear"][j][0][0][i] for j in range(2,11)] for i in range(17)]
    C=[[coeff["linear"][j][1][0][i] for j in range(2,11)] for i in range(17)]
    D=[[coeff["linear"][j][2][0][i] for j in range(2,11)] for i in range(17)]
    vmeta=parent.get("normal-linear-kernel")
    require(vmeta["rank"]==8 and vmeta["inputSHA256"]==F.matrix_hash(L),
            "Exact original rank8 L from the same field")
    V=F.matrix_from_json(vmeta["kernel"])
    require(h.shape(V)==(9,1) and h.zero_matrix(h.product(F,L,V)),
            "Original linear weak vector product")
    v=[row[0] for row in V]
    Cv,Dv=h.product(F,C,V),h.product(F,D,V)
    pencil=h.zeros(F,34,20)
    for i in range(17):
        pencil[i][:9]=L[i][:]
        pencil[i][18]=Cv[i][0]
        pencil[i][19]=Dv[i][0]
        pencil[17+i][9:18]=L[i][:]
        pencil[17+i][19]=Cv[i][0]
    W,wm=w.exact_kernel(F,h,pencil,cache,"tangent-two-top-pencil",report)
    k=h.shape(W)[1]
    require(2<=k<=4,"Two separate weak-vector gauges; at most four top parameters")
    pairs=[(j,l) for j in range(9) for l in range(j,9)]
    Tc,Td,Tcc,Tcd=[],[],[],[]
    for a in range(k):
        tc=[[F.mul(v[j],W[l][a])+F.mul(W[j][a],v[l])
             for l in range(9)] for j in range(9)]
        td=[[F.mul(v[j],W[9+l][a])+F.mul(W[9+j][a],v[l])
             for l in range(9)] for j in range(9)]
        tcc=[[F.mul(W[18][a],F.mul(v[j],v[l])) for l in range(9)] for j in range(9)]
        tcd=[[F.mul(W[19][a],F.mul(v[j],v[l])) for l in range(9)] for j in range(9)]
        require(h.zero_matrix(h.product(F,L,tcc)) and h.zero_matrix(h.product(F,L,tcd)),
                "All top c^2/cd original source equations")
        require(h.zero_matrix(w.add_matrices(h.product(F,L,tc),
                    w.add_matrices(h.product(F,C,tcc),h.product(F,D,tcd)))) and
                h.zero_matrix(w.add_matrices(h.product(F,L,td),h.product(F,C,tcd))),
                "All next c/d original source equations")
        Tc.append(tc);Td.append(td);Tcc.append(tcc);Tcd.append(tcd)
    M=h.zeros(F,153,45)
    for p,(j,l) in enumerate(pairs):
        for i in range(17):
            M[9*i+j][p]=M[9*i+j][p]+L[i][l]
            if j!=l:
                M[9*i+l][p]=M[9*i+l][p]+L[i][j]
    rhs=h.zeros(F,153,k)
    for a in range(k):
        B=w.add_matrices(h.product(F,C,Tc[a]),h.product(F,D,Td[a]))
        for i in range(17):
            for j in range(9):
                rhs[9*i+j][a]=B[i][j]
    combined=w.join_columns(M,rhs)
    Q,qm=w.exact_kernel(F,h,combined,cache,"tangent-two-symmetric-compatibility",report)
    q=h.shape(Q)[1]
    require(1<=q<=k+1<=5,"At most five actual quadratic high columns")
    columns=actions.target_columns(2)
    index={key:i for i,key in enumerate(columns)}
    Z=h.zeros(F,len(columns),q)
    for p,(j,l) in enumerate(pairs):
        for a in range(q):
            Z[index[(0,0,(j+2,l+2))]][a]=Q[p][a]
            for key,matrices in (((1,0),Tc),((0,1),Td),((2,0),Tcc),((1,1),Tcd)):
                Z[index[(key[0],key[1],(j+2,l+2))]][a]=sum(
                    (F.mul(matrices[b][j][l],Q[45+b][a]) for b in range(k)),F.zero)
    # The d^2 block is zero because the ORIGINAL pure coefficient q is a unit
    # vector. Verify that coefficient and all original high rows, not just M.
    require(any(coeff["pure"][0]),"Original noncontact pure d^2 coefficient is nonzero")
    product=w.action(F,h,actions,coeff,0,{2:Z},q)
    allowed=set(rows)
    require(all(not x for i,row in enumerate(product) if i not in allowed for x in row),
            "All6086 original source rows outside pure tangent<=2 vanish")
    _,zm=w.exact_kernel(F,h,Z,cache,"tangent-two-high-column-rank",report)
    require(zm["rank"]==q,"All actual high columns independent")
    parent_high=F.matrix_from_json(parent.get("weak-quadratic-original-columns")["highColumns"])
    _,nested=w.exact_kernel(F,h,w.join_columns(Z,parent_high),cache,
                           "tangent-two-contains-paid-weak-slice",report)
    require(nested["rank"]==q,"The complete old135 slice is contained in the new slice")
    G=[[x/units[i] for x in product[r]] for i,r in enumerate(rows)]
    payload={"highColumns":F.matrix_json(Z),"originalProduct":F.matrix_json(product),
             "scaledLowReturn":F.matrix_json(G),"topPencilKernel":F.matrix_json(W),
             "compatibilityKernel":F.matrix_json(Q),
             "all6086OutsideRowsZero":True,"allOldHighColumnsIncluded":True}
    cache.put("complete-tangent-two-high-slice",payload,True)
    return Z,G,{"topPencil":w.compact_kernel(wm),
                "symmetricCompatibility":w.compact_kernel(qm),
                "highDimension":q,"highSHA256":F.matrix_hash(Z),
                "lowReturnSHA256":F.matrix_hash(G),
                "all6086OutsideRowsZero":True,"allOldHighColumnsIncluded":True,
                "originalProductCoordinates":6188*q}

def kernel_using_parent_unit(F,h,w,A,rows,cols,U,factor,cache,prefix,report):
    nr,nc=h.shape(A)
    require(h.submatrix(A,rows,cols)==U and len(rows)==len(cols)==25,
            "Same paid25 original unit within the larger equation")
    keep=[j for j in range(nc) if j not in set(cols)]
    rest=[i for i in range(nr) if i not in set(rows)]
    key=prefix+"-old-unit-graph"
    old=cache.get(key)
    digest=F.matrix_hash(A)
    if old is None:
        rhs=w.negate(h.submatrix(A,rows,keep))
        X=h.lu_solve(F,factor,rhs)
        require(h.product(F,U,X)==rhs,"All old25 actual new right-hand sides")
        graph=h.zeros(F,nc,len(keep))
        for j,c in enumerate(keep):
            graph[c][j]=F.one
        for i,c in enumerate(cols):
            graph[c]=X[i][:]
        full=h.product(F,A,graph)
        require(h.zero_matrix(h.submatrix(full,rows,range(len(keep)))),
                "All original reused unit rows zero")
        schur=h.submatrix(full,rest,range(len(keep)))
        cache.put(key,{"inputSHA256":digest,"graph":F.matrix_json(graph),
                      "fullProduct":F.matrix_json(full),"schur":F.matrix_json(schur),
                      "allUnitEquationsVerified":True},True)
    else:
        require(old["inputSHA256"]==digest and old["allUnitEquationsVerified"],
                "Same actual extended equation for continued Schur")
        graph=F.matrix_from_json(old["graph"])
        schur=F.matrix_from_json(old["schur"])
    K,km=w.exact_kernel(F,h,schur,cache,prefix+"-complete-schur",report)
    full_kernel=h.product(F,graph,K)
    require(h.zero_matrix(h.product(F,A,full_kernel)),
            "All original expanded equation rows times the complete kernel")
    meta={"inputShape":[nr,nc],"reusedUnitRank":25,
          "schurShape":list(h.shape(schur)),"schurRank":km["rank"],
          "rank":25+km["rank"],"kernelDimension":h.shape(full_kernel)[1],
          "originalInputSHA256":digest,"kernelSHA256":F.matrix_hash(full_kernel),
          "allOriginalRowsVerified":True}
    cache.put(prefix+"-complete-kernel",{"metadata":meta,
              "kernel":F.matrix_json(full_kernel)},True)
    return full_kernel,meta

def finish(F,h,w,actions,coeff,low,exact,rows,units,S,X,R,Z,G,order,upper,
           unit_rows,unit_cols,U,factor,cache,report,params):
    base,basem=kernel_using_parent_unit(F,h,w,S[0],unit_rows,unit_cols,U,factor,
                                      cache,"expanded-low-constant",report)
    require(basem["rank"]==46 and h.shape(base)[1]==13,
            "Actual complete low constant rank46 / thirteen heads")
    q=h.shape(Z)[1]
    A=w.join_columns(S[0],G,R)
    K,km=kernel_using_parent_unit(F,h,w,A,unit_rows,unit_cols,U,factor,
                                 cache,"expanded-jet-equation",report)
    H=h.submatrix(K,range(59+q,72+q),range(h.shape(K)[1]))
    _,hm=w.exact_kernel(F,h,H,cache,"expanded-actual-leading-image",report)
    r=hm["rank"]
    require(11<=r<=13,"Eleven low formal free heads included")
    choice=hm["independentColumns"]
    selected=h.submatrix(K,range(72+q),choice)
    c=h.submatrix(selected,range(59+q,72+q),range(r))
    x=h.submatrix(selected,range(59),range(r))
    a=h.submatrix(selected,range(59,59+q),range(r))
    Y=[h.product(F,z,c) for z in X]
    Y[-1]=w.add_matrices(Y[-1],x)
    high=h.product(F,Z,a)
    full=[]
    for k,Yk in enumerate(Y):
        sections=w.embed_low(F,h,actions,low,Yk)
        sections[2]=high if k==order else h.zeros(F,450,r)
        full.append(sections)
    pure=h.zeros(F,20,2)
    ix={key:j for j,key in enumerate(actions.target_columns(0))}
    for j,key in enumerate(exact):
        pure[ix[key]][j]=F.one
    for k in range(order+1):
        for degree in (0,1,2):
            extra=pure if k==0 and degree==0 else \
                  h.zeros(F,len(actions.target_columns(degree)),2)
            full[k][degree]=w.join_columns(full[k][degree],extra)
    width=r+2
    lead=full[0][0]+full[0][1]+full[0][2]
    _,lm=w.exact_kernel(F,h,lead,cache,"expanded-full-original-leading-rank",report)
    require(lm["rank"]==width,"All original full leading heads independent")
    hashes=[]
    for k in range(order+1):
        product=h.zeros(F,6188,width)
        for j in range(k+1):
            product=w.add_matrices(product,w.action(F,h,actions,coeff,j,full[k-j],width))
        require(h.zero_matrix(product),"All6188 original products, Taylor order"+str(k))
        hashes.append(F.matrix_hash(product))
    gain=r-11
    lower=2*order+gain
    require(lower<=upper,"Actual positive bound cannot exceed the paid full bound")
    square_rows=[actions.target_columns(2).index((0,0,(j,j))) for j in range(2,11)]
    squares=[]
    for k in range(order+1):
        a=h.submatrix(full[k][2],square_rows,range(width))
        squares.append({"order":k,"shape":[9,width],"sha256":F.matrix_hash(a),
                        "nonzeroEntries":sum(bool(x) for row in a for x in row)})
    pack=cache.put("expanded-full-positive-jets-verified",{
        "cochains":[{str(d):F.matrix_json(a) for d,a in sections.items()}
                    for sections in full],
        "highTargetSectors3Through5ExactlyZero":True,
        "leadingMap":F.matrix_json(c),"selectedEquationKernel":F.matrix_json(selected),
        "all6188OriginalProductsZero":True,"originalProductSHA256":hashes,
        "fullLeadingRank":width,"gain":gain},True)
    params.update({"expandedLowConstant":basem,"expandedCombined":km,
                   "actualLeadingRank":r,"fullLeadingRank":width,
                   "additionalPositiveLengthLowerBound":gain,
                   "fullOriginalLengthLowerBound":lower,"paidFullLocalUpperBound":upper,
                   "all6188OriginalJetProductsZero":True,
                   "originalJetProductCoordinates":6188*width*(order+1),
                   "originalProductSHA256":hashes,
                   "nineOriginalSquareReadouts":squares,"completeCochainCheckpoint":pack,
                   "zeroGainOnlyConcernsTheStatedSupportAndLowerJets":True,
                   "noFullConnectionLowerBoundOrGlobalMembershipClaimed":True})

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    ap.add_argument("--weak-driver",required=True)
    ap.add_argument("--field",choices=tuple(PARENT_PINS),required=True)
    ap.add_argument("--parent-out",required=True)
    ap.add_argument("--parent-receipt",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,
            "Explicit mathematical and memory budgets")
    for key,value in PINS.items():
        require(sha_file(getattr(a,key))==value,"Pinned actual helper "+key)
    require(sha_file(a.weak_driver)==WEAK_SHA,"Exact original parent source")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    w=module_at("critical_weak_parent_driver",a.weak_driver)
    parent=Parent(w,a.parent_out,a.parent_receipt,a.field)
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"sourceSHA256":source_sha,
               "helpers":PINS,"parentSourceSHA256":WEAK_SHA,"field":a.field,
               "parent":PARENT_PINS[a.field]})).hexdigest()
    out=Path(a.out)
    out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-quadratic-tangent-two-positive-jets-receipt.json"
    start=time.monotonic()
    setting=w.FIELDS[a.field]
    result={"format":FORMAT,"status":"started","binding":binding,
            "scriptSHA256":source_sha,"parameters":{
                "field":a.field,"fieldPolynomialAscending":setting["polynomial"],
                "naturalParameter":"t=s-alpha","parent":PARENT_PINS[a.field],
                "helperSHA256":PINS,"parentSourceSHA256":WEAK_SHA,
                "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
                "originalEquations":17,"originalSourceRows":6188,
                "originalTargetCoordinates":4367,"lastJetOrder":setting["exit"],
                "parentIsReadOnly":True,"newCanonicalSeriesSolved":False,
                "completeHighSpaceBeyondThisSliceNotClaimed":True,
                "largeDataUploadedOrCommitted":False}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        result["parameters"]["checkpointManifest"]={
          "file":"checkpoints/manifest.json","bytes":cache.path.stat().st_size,
          "sha256":sha_file(cache.path)}
        raw=canonical(result)
        require(len(raw)<90000,"Small exact receipt")
        tmp=receipt.with_name(receipt.name+".tmp")
        tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):
        raise BudgetStop("Shared tangent-two budget exhausted")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        m=w.load_module("critical_t2_original",a.generator)
        actions=w.load_module("critical_t2_actions",a.jet_actions)
        h=w.load_module("critical_t2_field_helper",a.field_helper)
        F=w.make_field(h,setting["polynomial"])
        _,poly,poly_meta=w.decode_polynomial_model(m,parent.get("original-polynomial-model"))
        coeff=w.field_coefficients(F,poly,setting["exit"])
        qp=w.physical_quadratic_constant(F,h,m,coeff)
        require(qp==parent.result["parameters"]["quadraticPhysicalChecks"],
                "All constant original quadratic physical identities match the parent")
        result["parameters"]["quadraticPhysicalChecks"]=qp
        data=expanded_low(F,h,w,actions,coeff,parent,cache,setting["exit"],report)
        low,exact,rows,units,S,X,R,ur,uc,U,factor=data
        result["parameters"].update({
          "expandedLowShape":[102,59],"original25UnitSHA256":F.matrix_hash(U),
          "allParentTaylorCoefficientsMatched":True,
          "allOldCanonicalHeadsRetained":11,"newExactDegreeFourHeads":2,
          "allExpandedLowEmbeddingRowsVerified":True})
        save()
        Z,G,meta=slice_columns(F,h,w,actions,coeff,parent,cache,report,rows,units)
        result["parameters"]["completeQuadraticTangentTwoSlice"]=meta
        save()
        finish(F,h,w,actions,coeff,low,exact,rows,units,S,X,R,Z,G,setting["exit"],
               setting["upper"],ur,uc,U,factor,cache,report,result["parameters"])
        result["parameters"]["fieldArithmetic"]={
          "multiplications":F.mul_count,"verifiedInverses":F.inv_count}
        result["status"]="completed";code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};code=75
    except Exception as exc:
        result["status"]="failed"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)};code=1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
              "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
              "elapsedSeconds":result["elapsedSeconds"],
              "gain":result["parameters"].get("additionalPositiveLengthLowerBound")},
              sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
