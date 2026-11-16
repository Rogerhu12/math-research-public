#!/usr/bin/env python3
"""One genuine nonfree critical chain, extended by one original order.

Astra-ISP-789f / literature_audit; AI-assisted GPT-6 Astra Pro,2026-11-16.
Only a positive certificate is inferred from the 162-coordinate ansatz.
All6188 original rows and the nonfree leading head are verified.
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
from flint import fmpq, fmpq_poly

FORMAT="r150-critical-one-nonfree-original-positive-prolongation-v1"
FIRST_SHA="4938d26273a72b16185af28c185ea304771a4c91cea0054b1a538de1ef0993ad"
WEAK_SHA="f211696b5cb789f054e259648a54be7a60f2d8c7c7772d410143bc0025025b1b"
HIGH_SHA="de723d530fe0f2b3ab7876b76c8fc605a5156702309482f02a38c7b582a54753"
CUBIC_SHA="634b258dec87cdba34d01a2be8f1ab61fce7f944b910b5c9438343b3b423a314"
HELPER_KEYS=("generator","jet_actions","low_generator","field_helper")
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


class RestrictedIncompatible(Exception):
    pass

def read_only_phase(cache,name):
    record=cache.manifest["stages"].get(name)
    require(record is not None and record["verified"],"Paid verified phase: "+name)
    value=cache.get(name)
    require(value is not None,"Complete paid phase")
    return value

def checked_factor(F,h,A,saved):
    require(saved["inputSHA256"]==F.matrix_hash(A) and
            saved["allOriginalUnitEntriesVerified"],"Same genuine paid original unit")
    fac=(F.matrix_from_json(saved["L"]),F.matrix_from_json(saved["U"]),saved["rows"])
    require(h.product(F,fac[0],fac[1])==[A[i] for i in fac[2]],
            "All paid unit factor entries multiplied back")
    return fac

def solve_original_profile(F,h,w,A,B,meta,factor):
    """Free variables zero; complete original product, not just selected rows."""
    require(meta["inputSHA256"]==F.matrix_hash(A) and
            meta["allOriginalRowsVerified"],"Exact proved complete matrix profile")
    rows,cols=meta["independentRows"],meta["independentColumns"]
    primitive,contents=w.rational_rows(A)
    require([str(x) for x in contents]==meta["rationalRowContents"],
            "Original whole-row contents, same units on both sides")
    U=h.submatrix(primitive,rows,cols)
    require(h.product(F,factor[0],factor[1])==[U[i] for i in factor[2]],
            "Original selected unit retained")
    rhs=[[x/contents[i] for x in B[i]] for i in rows]
    x=h.lu_solve(F,factor,rhs)
    require(h.product(F,U,x)==rhs,"All actual selected unit equations")
    solution=h.zeros(F,len(A[0]),len(B[0]))
    for i,c in enumerate(cols):
        solution[c]=x[i][:]
    residual=w.add_matrices(h.product(F,A,solution),w.negate(B))
    require(h.zero_matrix(h.submatrix(residual,rows,range(len(B[0])))),
            "Original unit rows of residual are zero")
    return solution,residual

def first_parent(F,h,x,a):
    p=Path(a.first_receipt)
    require(p.stat().st_size==a.first_receipt_bytes and sha_file(p)==a.first_receipt_sha,
            "Exact actual completed first-exit outer")
    outer=json.loads(p.read_text());r=outer["result"];pp=r["parameters"]
    require(outer["exitCode"]==0 and r["status"]=="completed" and
            r["scriptSHA256"]==FIRST_SHA and pp["field"]==a.field,
            "Same actual first-exit mathematical generator")
    require(pp["completeConnectionRank"]==1 and pp["completeLeadingHeads"]==14
            and pp["constantLowRank"]==86 and pp["highReturnRankModuloLow"]==7
            and pp["fullOriginalConstantRank"]==4352 and
            pp["allEarlierFullConnectionsZero"] and
            pp["allOriginal6188ProductsZero"] and
            pp["all1870OriginalExitSpanningCoordinatesVerified"],
            "The original complete rank-one first-exit branch")
    root=Path(a.first_out)/"checkpoints";mi=pp["checkpointManifest"]
    mf=root/"manifest.json"
    require(mf.stat().st_size==mi["bytes"] and sha_file(mf)==mi["sha256"],
            "Exact immutable completed first-exit manifest")
    cache=x.Cache(root,r["binding"])
    value=read_only_phase(cache,"complete-original-first-critical-exit")
    require(value["connectionRank"]==1 and value["fullLeadingRank"]==14 and
            value["allOriginalProductsZero"] and value["exactEarlierConnectionsZero"],
            "All original first-exit saved proof gates")
    identity={"outerBytes":a.first_receipt_bytes,"outerSHA256":a.first_receipt_sha,
              "binding":r["binding"],"manifest":mi,
              "cochain":cache.manifest["stages"]["complete-original-first-critical-exit"]}
    return value,cache,identity

def coefficients_through_true_quadratic_one(F,h,w,m,poly,parent,cache):
    old=cache.get("original-quadratic-orders-zero-and-one")
    base=w.field_coefficients(F,poly,1)
    if old is not None:
        require(old["fieldModulus"]==F.encode(F.modulus) and
                old["originalParameterModelSHA256"]==parent.cache.manifest["stages"]["original-polynomial-model"]["payloadSHA256"],
                "Same actual original polynomial model")
        for p,values in zip(old["pairs"],old["quadratic"]):
            base["quadratic"][tuple(p)]=F.matrix_from_json(values)
        return base,old["metadata"]
    # The same physical formula is evaluated in Q[s]/Phi^2. This invocation
    # has only rational constant inverses (J3); no quotient-algebra inverse.
    raw=w.FIELDS[parent.result["parameters"]["field"]]["polynomial"]
    square=fmpq_poly(raw)*fmpq_poly(raw)
    require(all(q==int(q) for q in square.coeffs()),"Original integer polynomial square")
    raw_square=[int(q) for q in square.coeffs()]
    Ring=w.make_field(h,raw_square)
    require(Ring.modulus==F.modulus*F.modulus and Ring.degree==2*F.degree,
            "The exact squared original irreducible polynomial")
    ring_coeff=w.field_coefficients(Ring,poly,0)
    ringmeta=w.physical_quadratic_constant(Ring,h,m,ring_coeff)
    require(Ring.inv_count==0,"No parameter or quotient-algebra inverses introduced")
    def value(x):
        return x%F.modulus
    def first(x):
        cs=x.coeffs()
        return fmpq_poly([j*cs[j] for j in range(1,len(cs))])%F.modulus
    for i in range(17):
        q=ring_coeff["pure"][0][i]
        require(value(q)==base["pure"][0][i] and first(q)==base["pure"][1][i],
                "All original pure values and ordinary first derivatives")
    for j in range(2,11):
        for mode in range(3):
            for i in range(17):
                q=ring_coeff["linear"][j][mode][0][i]
                require(value(q)==base["linear"][j][mode][0][i] and
                        first(q)==base["linear"][j][mode][1][i],
                        "All original27 linear values and first derivatives")
    pairs=sorted(ring_coeff["quadratic"])
    require(len(pairs)==45,"Every ordinary normal quadratic pair")
    for p in pairs:
        values=ring_coeff["quadratic"][p][0]
        base["quadratic"][p]=[[value(q) for q in values],[first(q) for q in values]]
    q0=[base["quadratic"][p][0] for p in pairs]
    q1=[base["quadratic"][p][1] for p in pairs]
    paid=parent.result["parameters"]["quadraticPhysicalChecks"]
    require(F.matrix_hash(q0)==paid["quadraticConstantSHA256"] and
            ringmeta["originalJ2SHA256"]==paid["originalJ2SHA256"] and
            ringmeta["originalJ3SHA256"]==paid["originalJ3SHA256"],
            "Every765 original quadratic constants equal the actual paid model")
    meta={"method":"Original physical polynomial modulo Phi^2, then ordinary derivative modulo Phi",
      "allOriginal765QuadraticConstantsMatched":True,
      "allOriginalPureAndLinearFirstDerivativesMatched":True,
      "constantQuadraticSHA256":F.matrix_hash(q0),
      "firstQuadraticSHA256":F.matrix_hash(q1),
      "quotientAlgebraInversesUsed":0,"higherQuadraticOrdersNotFabricated":True,
      "originalJ2SHA256":paid["originalJ2SHA256"],"originalJ3SHA256":paid["originalJ3SHA256"]}
    cache.put("original-quadratic-orders-zero-and-one",{
      "fieldModulus":F.encode(F.modulus),
      "originalParameterModelSHA256":parent.cache.manifest["stages"]["original-polynomial-model"]["payloadSHA256"],
      "pairs":[list(p) for p in pairs],
      "quadratic":[F.matrix_json(base["quadratic"][p]) for p in pairs],
      "metadata":meta},True)
    return base,meta

def action(F,h,actions,coeff,order,sections,ncols):
    result=[]
    for r in range(4):
        rows=actions.source_rows(r);out=h.zeros(F,len(rows),ncols)
        for degree,X in sections.items():
            if degree<r or degree>r+2 or h.zero_matrix(X):
                continue
            cols=actions.target_columns(degree)
            require(h.shape(X)==(len(cols),ncols),"Complete original target sector")
            if degree==r+2:
                require(order<=1 and all(len(v)>order for v in coeff["quadratic"].values()),
                        "Only genuinely computed quadratic Taylor orders may be used")
            index={key:j for j,key in enumerate(cols)}
            for i,row in enumerate(rows):
                for c,v in actions.sparse_row_terms(coeff,order,row,degree,index):
                    for j,b in enumerate(X[c]):
                        if b:out[i][j]+=F.mul(v,b)
        result.extend(out)
    require(len(result)==6188,"All original6188 source rows")
    return result

def normal_data(F,h,w,coeff,high):
    L=[[coeff["linear"][j][0][0][i] for j in range(2,11)] for i in range(17)]
    C=[[coeff["linear"][j][1][0][i] for j in range(2,11)] for i in range(17)]
    D=[[coeff["linear"][j][2][0][i] for j in range(2,11)] for i in range(17)]
    q=[[x] for x in coeff["pure"][0]]
    v=F.matrix_from_json(high["v"]);z=[[F.decode(x)] for x in high["z"]]
    require(h.shape(v)==h.shape(z)==(9,1) and
            h.zero_matrix(h.product(F,L,v)) and h.product(F,L,z)==q,
            "All original identities Lv=0 and Lz=q")
    v=[r[0] for r in v];z=[r[0] for r in z]
    T=[[[F.mul(v[i],v[j]) for j in range(9)] for i in range(9)],
       [[F.mul(v[i],z[j])+F.mul(z[i],v[j]) for j in range(9)] for i in range(9)],
       [[F.mul(z[i],z[j]) for j in range(9)] for i in range(9)]]
    Z=[[F.zero]*9,[-a for a in v],[-a for a in z]]
    for k in range(3):
        require(h.zero_matrix(w.add_matrices(h.product(F,L,T[k]),h.product(F,q,[Z[k]]))),
                "All153 original symmetric homogeneous equations")
    pairs=[(i,j) for i in range(9) for j in range(i,9)]
    A=h.zeros(F,153,60)
    CT=[h.product(F,C,t) for t in T];DT=[h.product(F,D,t) for t in T]
    for i in range(17):
        for j in range(9):
            row=9*i+j
            for k,(a,b) in enumerate(pairs):
                if j==a:A[row][k]+=L[i][b]
                if j==b and a!=b:A[row][k]+=L[i][a]
            A[row][45+j]=q[i][0]
            for k in range(3):
                A[row][54+k]=CT[k][i][j];A[row][57+k]=DT[k][i][j]
    require(F.matrix_hash(A)==high["smallSystemSHA256"],
            "Exactly the paid153-by60 matrix, not a new large elimination")
    return L,C,D,q,v,z,T,Z,pairs,A

def restricted_high_particular(F,h,w,actions,coeff,forcing,high,hcache,parent,cache,report,params):
    old=cache.get("complete-original-high-particular")
    fd=F.matrix_hash(forcing)
    if old is not None:
        require(old["forcingSHA256"]==fd and old["all6018OriginalHighRowsVerified"],
                "Same fully verified actual high right-hand side")
        Z1=F.matrix_from_json(old["oneNormal"]);Z2=F.matrix_from_json(old["twoNormal"])
        product=action(F,h,actions,coeff,0,{1:Z1,2:Z2},1)
        require(w.add_matrices(product[170:],forcing[170:])==h.zeros(F,6018,1),
                "All original high rows rechecked on continuation")
        return {1:Z1,2:Z2},product
    original_rows=[row for degree in range(4) for row in actions.source_rows(degree)]
    index={row:i for i,row in enumerate(original_rows)}
    selected=[]
    YY=[]
    for a,b in ((0,0),(1,0),(0,1)):
        Y=h.zeros(F,17,9)
        for i in range(17):
            for j in range(9):
                r=index[(i,a,b,(j+2,))]
                selected.append(r);Y[i][j]=-forcing[r][0]
        YY.append(Y)
    require(len(set(selected))==459 and min(selected)>=170,
            "Exactly the459 original n,cn,dn source rows")
    outside=[i for i in range(170,6188) if i not in set(selected)]
    if not h.zero_matrix(h.submatrix(forcing,outside,[0])):
        params["restrictedFailure"]="High forcing has original rows outside the declared162 support"
        raise RestrictedIncompatible(params["restrictedFailure"])
    params["all5559OtherOriginalHighForcingRowsZero"]=True
    L,C,D,q,v,z,T,Z,pairs,A=normal_data(F,h,w,coeff,high)
    paid=parent.get("normal-linear-kernel")
    rows,cols=paid["independentRows"],paid["independentColumns"]
    U=h.submatrix(L,rows,cols)
    factor=checked_factor(F,h,U,read_only_phase(hcache,"original-eight-normal-unit-unit-lu"))
    # First solve L M=[Yc,Yd]. Since q=Lz, this is a necessary condition
    # for a solution in the declared162-coordinate support.
    rhs=w.join_columns(YY[1],YY[2])
    partial=h.lu_solve(F,factor,h.submatrix(rhs,rows,range(18)))
    require(h.product(F,U,partial)==h.submatrix(rhs,rows,range(18)),
            "All144 original eight-unit high RHS products")
    M=h.zeros(F,9,18)
    for i,c in enumerate(cols):M[c]=partial[i][:]
    if h.product(F,L,M)!=rhs:
        params["restrictedFailure"]="Original Yc or Yd is outside im L in the declared support"
        raise RestrictedIncompatible(params["restrictedFailure"])
    Mc=h.submatrix(M,range(9),range(9));Md=h.submatrix(M,range(9),range(9,18))
    skewpairs=[(i,j) for i in range(9) for j in range(i+1,9)]
    symmetry=h.zeros(F,36,18);right=h.zeros(F,36,2)
    for r,(i,j) in enumerate(skewpairs):
        symmetry[r][j]+=v[i];symmetry[r][i]-=v[j]
        symmetry[r][9+j]-=z[i];symmetry[r][9+i]+=z[j]
        right[r]=[Mc[j][i]-Mc[i][j],Md[j][i]-Md[i][j]]
    _,sm=w.exact_kernel(F,h,symmetry,cache,"actual36-by18-high-symmetry",report)
    require(sm["rank"]==15,"Exact symmetry rank from independent v,z")
    primitive,_=w.rational_rows(symmetry)
    su=h.submatrix(primitive,sm["independentRows"],sm["independentColumns"])
    sf=checked_factor(F,h,su,read_only_phase(cache,"actual36-by18-high-symmetry-unit-lu"))
    ab,sres=solve_original_profile(F,h,w,symmetry,right,sm,sf)
    if not h.zero_matrix(sres):
        params["restrictedFailure"]="Actual36-row symmetry RHS is incompatible in declared support"
        raise RestrictedIncompatible(params["restrictedFailure"])
    partT=[];partV=[]
    for k,B in enumerate((Mc,Md)):
        aa=[ab[i][k] for i in range(9)];vv=[ab[9+i][k] for i in range(9)]
        tensor=[[B[i][j]+F.mul(v[i],aa[j])-F.mul(z[i],vv[j])
                 for j in range(9)] for i in range(9)]
        require(all(tensor[i][j]==tensor[j][i] for i in range(9) for j in range(9)),
                "Every ordinary tensor entry is symmetric")
        require(w.add_matrices(h.product(F,L,tensor),h.product(F,q,[vv]))==YY[k+1],
                "All153 original inhomogeneous LT+qv equations")
        partT.append(tensor);partV.append(vv)
    top=w.add_matrices(YY[0],w.negate(w.add_matrices(
              h.product(F,C,partT[0]),h.product(F,D,partT[1]))))
    topcolumn=[[top[i][j]] for i in range(17) for j in range(9)]
    km=read_only_phase(hcache,"actual-153-by60-high-system-kernel")
    require(km["rank"]==53 and km["inputSHA256"]==F.matrix_hash(A),
            "Same exact53 original high unit")
    apr,_=w.rational_rows(A)
    au=h.submatrix(apr,km["independentRows"],km["independentColumns"])
    af=checked_factor(F,h,au,read_only_phase(hcache,"actual-153-by60-high-system-unit-lu"))
    sol,tres=solve_original_profile(F,h,w,A,topcolumn,km,af)
    if not h.zero_matrix(tres):
        params["restrictedFailure"]="Original153-row top RHS incompatible in the declared162 support"
        raise RestrictedIncompatible(params["restrictedFailure"])
    Z1=h.zeros(F,135,1);Z2=h.zeros(F,450,1)
    i1={key:i for i,key in enumerate(actions.target_columns(1))}
    i2={key:i for i,key in enumerate(actions.target_columns(2))}
    for j in range(9):
        Z1[i1[(0,2,(j+2,))]][0]=sol[45+j][0]
        for mode,key in enumerate(((1,2),(0,3))):
            Z1[i1[(key[0],key[1],(j+2,))]][0]=partV[mode][j]+sum(
                (F.mul(Z[k][j],sol[54+3*mode+k][0]) for k in range(3)),F.zero)
    for i,(j,l) in enumerate(pairs):
        Z2[i2[(0,0,(j+2,l+2))]][0]=sol[i][0]
        for mode,key in enumerate(((1,0),(0,1))):
            Z2[i2[(key[0],key[1],(j+2,l+2))]][0]=partT[mode][j][l]+sum(
                (F.mul(T[k][j][l],sol[54+3*mode+k][0]) for k in range(3)),F.zero)
    product=action(F,h,actions,coeff,0,{1:Z1,2:Z2},1)
    require(h.zero_matrix(w.add_matrices(product[170:],forcing[170:])),
            "All6018 original high source equations, not only459 selected rows")
    cache.put("complete-original-high-particular",{
      "forcingSHA256":fd,"oneNormal":F.matrix_json(Z1),"twoNormal":F.matrix_json(Z2),
      "all6018OriginalHighRowsVerified":True,"originalProductSHA256":F.matrix_hash(product),
      "symmetryRank":15,"originalTopUnitRank":53},True)
    params["highCorrection"]={"all6018OriginalHighRowsVerified":True,
       "symmetryShape":[36,18],"symmetryRank":15,"reusedOriginalUnitRanks":[8,53],
       "oneNormalSHA256":F.matrix_hash(Z1),"twoNormalSHA256":F.matrix_hash(Z2)}
    return {1:Z1,2:Z2},product

def prolong(F,h,w,x,cubic,m,actions,parent,high,hcache,first,fcache,cache,report,params):
    order=w.FIELDS[params["field"]]["exit"]
    require(order==3,"This one extra positive page is requested only for the two cubic fields")
    small,poly,physical=w.decode_polynomial_model(m,parent.get("original-polynomial-model"))
    coeff=w.field_coefficients(F,poly,order+1)
    q01,qmeta=coefficients_through_true_quadratic_one(F,h,w,m,poly,parent,cache)
    coeff["quadratic"]=q01["quadratic"]
    paid_coeff,low36,exact,_,X,R,_,_,_,_,_,_,_=cubic.prepare(
        F,h,w,m,actions,parent,order)
    for k in range(order+1):
        require(coeff["pure"][k]==paid_coeff["pure"][k],"All paid pure Taylor coefficients")
        for j in range(2,11):
            for mode in range(3):
                require(coeff["linear"][j][mode][k]==paid_coeff["linear"][j][mode][k],
                        "Every paid original linear Taylor coefficient")
    params["quadraticFirstPhysicalChecks"]=qmeta
    full=[{int(k):F.matrix_from_json(v) for k,v in sec.items()} for sec in first["cochains"]]
    require(len(full)==order+1 and all(h.shape(sec[d])==(len(actions.target_columns(d)),14)
                          for sec in full for d in (0,1,2)),
            "All14 completed original heads and every coefficient retained")
    C=F.matrix_from_json(first["leadingMap"])
    em=parent.get("paid-low-exit-kernel")
    exitkernel=F.matrix_from_json(em["kernel"]);ec=em["independentColumns"]
    require(h.shape(C)==(11,10) and h.submatrix(C,range(11),range(9))==exitkernel,
            "Original first9 exit-null heads unchanged")
    special=h.submatrix(C,range(11),[9])
    require(any(special[c][0] for c in ec) and
            all(not special[i][0] for i in range(11) if i not in set(ec)),
            "Chosen true surviving direction has nonzero independent exit coordinates")
    target=[{d:h.submatrix(sec[d],range(len(sec[d])),[9]) for d in (0,1,2)}
            for sec in full]
    freecols=list(range(9))+list(range(10,14))
    freehead=sum((h.submatrix(full[0][d],range(len(full[0][d])),freecols) for d in (0,1,2)),[])
    nonfreehead=sum((target[0][d] for d in (0,1,2)),[])
    _,hm=w.exact_kernel(F,h,w.join_columns(freehead,nonfreehead),
                       cache,"nonfree-leading-head-against-thirteen-free",report)
    require(hm["rank"]==14,"Actual chosen head is outside all13 formal-free leading heads")
    params["nonfreeLeadingHead"]={"originalCochainColumnZeroBased":9,
       "independentExitCoordinates":F.matrix_json(h.submatrix(special,ec,[0])),
       "rankWithThirteenFormalFreeHeads":14,
       "headSHA256":F.matrix_hash(nonfreehead)}
    for k in range(order+1):
        total=h.zeros(F,6188,1)
        for j in range(k+1):
            total=w.add_matrices(total,action(F,h,actions,coeff,j,target[k-j],1))
        require(h.zero_matrix(total),"Actual original chosen chain through the paid first exit")
    forcing=h.zeros(F,6188,1)
    for j in range(1,order+2):
        forcing=w.add_matrices(forcing,action(F,h,actions,coeff,j,target[order+1-j],1))
    cache.put("actual-next-original-forcing",{"forcing":F.matrix_json(forcing),
       "originalSourceRows":6188,"forcingSHA256":F.matrix_hash(forcing),
       "trueQuadraticFirstCoefficientUsed":True},True)
    params["actualNextOriginalForcingSHA256"]=F.matrix_hash(forcing)
    Zpart,prod=restricted_high_particular(F,h,w,actions,coeff,forcing,high,hcache,
                                         parent,cache,report,params)
    S=F.matrix_from_json(first["originalS"])
    lowrhs=w.add_matrices(forcing[:170],prod[:170])
    lp=read_only_phase(fcache,"complete-low-unit-profile")
    require(lp["rank"]==86 and lp["inputSHA256"]==F.matrix_hash(S),"Same original complete low unit")
    spr,units=w.rational_rows(S);rows,cols=lp["rows"],lp["columns"]
    U=h.submatrix(spr,rows,cols)
    fac=checked_factor(F,h,U,read_only_phase(fcache,"complete-low-original86-unit-unit-lu"))
    rhs=[[-lowrhs[i][0]/units[i]] for i in rows]
    solved=h.lu_solve(F,fac,rhs)
    require(h.product(F,U,solved)==rhs,"All86 new original low unit products")
    lowpart=h.zeros(F,101,1)
    for i,c in enumerate(cols):lowpart[c]=solved[i][:]
    remainder=w.add_matrices(lowrhs,h.product(F,S,lowpart))
    require(h.zero_matrix(h.submatrix(remainder,rows,[0])),"All original low unit rows killed")
    old=read_only_phase(fcache,"nine-actual-original-unit-right-hand-sides")
    oldlift=F.matrix_from_json(old["lowLift"]);V=F.matrix_from_json(old["fullResidual"])
    G=F.matrix_from_json(first["originalHighReturn"]);Rfull=F.matrix_from_json(first["originalExitResidual"])
    B=w.join_columns(G,h.submatrix(Rfull,range(170),ec))
    require(old["inputSHA256"]==F.matrix_hash(S) and old["rhsSHA256"]==F.matrix_hash(B)
            and w.add_matrices(h.product(F,S,oldlift),B)==V,
            "Every1530 original paid low residual coordinate retained")
    vm=read_only_phase(fcache,"complete-two-exits-modulo-original-image-kernel")
    require(vm["rank"]==8 and vm["inputSHA256"]==F.matrix_hash(V),
            "Actual complete rank-one first-exit image, including all7 high returns")
    vp,_=w.rational_rows(V)
    vu=h.submatrix(vp,vm["independentRows"],vm["independentColumns"])
    vf=checked_factor(F,h,vu,read_only_phase(fcache,"complete-two-exits-modulo-original-image-unit-lu"))
    weights,obstruction=solve_original_profile(F,h,w,V,w.negate(remainder),vm,vf)
    if not h.zero_matrix(obstruction):
        params["restrictedFailure"]="The retained original high particular and incoming cochains do not yield this positive prolongation"
        params["newLowResidualSHA256"]=F.matrix_hash(obstruction)
        raise RestrictedIncompatible(params["restrictedFailure"])
    a=h.submatrix(weights,range(7),[0]);y=h.submatrix(weights,[7,8],[0])
    Z1=F.matrix_from_json(high["oneNormal"]);Z2=F.matrix_from_json(high["twoNormal"])
    lowtop=w.add_matrices(lowpart,h.product(F,oldlift,weights))
    lowcols=[(0,key) for key in actions.target_columns(0)]+[
             (1,key) for key in actions.target_columns(1) if key[1]<2]
    top=x.embed_low101(F,h,actions,lowcols,lowtop)
    top[1]=w.add_matrices(top[1],w.add_matrices(Zpart[1],h.product(F,Z1,a)))
    top[2]=w.add_matrices(Zpart[2],h.product(F,Z2,a))
    selector=h.zeros(F,11,2)
    for j,c in enumerate(ec):selector[c][j]=F.one
    incoming=h.product(F,selector,y)
    chain=[{d:[r[:] for r in sec[d]] for d in (0,1,2)} for sec in target]
    chain.append({d:h.zeros(F,len(actions.target_columns(d)),1) for d in (0,1,2)})
    for k in range(1,order+2):
        shifted=w.embed_low(F,h,actions,low36,h.product(F,X[k-1],incoming))
        for d in (0,1):
            chain[k][d]=w.add_matrices(chain[k][d],shifted[d])
    for d in (0,1,2):chain[order+1][d]=w.add_matrices(chain[order+1][d],top[d])
    require(all(chain[0][d]==target[0][d] for d in (0,1,2)),
            "The genuinely nonfree original leading head is unchanged")
    hashes=[]
    for k in range(order+2):
        total=h.zeros(F,6188,1)
        for j in range(k+1):
            total=w.add_matrices(total,action(F,h,actions,coeff,j,chain[k-j],1))
        require(h.zero_matrix(total),"All6188 original source products at final order"+str(k))
        hashes.append(F.matrix_hash(total))
    square=[actions.target_columns(2).index((0,0,(j,j))) for j in range(2,11)]
    readouts=[]
    for k in range(order+2):
        a0=h.submatrix(chain[k][2],square,[0])
        readouts.append({"order":k,"sha256":F.matrix_hash(a0),
            "values":[F.encode(r[0]) for r in a0]})
    record=cache.put("complete-original-nonfree-positive-prolongation",{
      "cochains":[{str(d):F.matrix_json(a0) for d,a0 in sec.items()} for sec in chain],
      "nonfreeHeadUnchanged":True,"all6188OriginalProductsZero":True,
      "originalProductSHA256":hashes,"incomingOriginalExitWeights":F.matrix_json(y),
      "oldHighKernelWeights":F.matrix_json(a),"exactPositiveSpectrum":[3,5],
      "fullOriginalLength":8,"originalSquareReadouts":readouts},True)
    params.update({"positiveProlongationVerified":True,"all6188OriginalProductsZero":True,
       "originalProductCoordinates":6188*(order+2),"nonfreeLeadingHeadUnchanged":True,
       "newTrueCochainOrder":order+1,"exactFullPositiveSpectrum":[3,5],
       "exactFullOriginalLength":8,"allLowerCochainCoefficientsPreservedWithExplicitIncoming":True,
       "allOriginalSquareReadouts":[{"order":r["order"],"sha256":r["sha256"],
          "nonzeroEntries":sum(bool(F.decode(v)) for v in r["values"])} for r in readouts],
       "positiveCochainCheckpoint":record})

def main():
    ap=argparse.ArgumentParser()
    for name in HELPER_KEYS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    for name in ("weak-driver","cubic-helper","high-driver","first-driver",
                 "parent-out","parent-receipt","high-out","high-receipt",
                 "high-receipt-sha","first-out","first-receipt","first-receipt-sha","out"):
        ap.add_argument("--"+name,required=True)
    ap.add_argument("--high-receipt-bytes",type=int,required=True)
    ap.add_argument("--first-receipt-bytes",type=int,required=True)
    ap.add_argument("--field",choices=("plus","minus"),required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    a=ap.parse_args()
    require(0<a.remaining_seconds<=1800 and 512<=a.memory_mib<=8192,"Explicit resources")
    require(sha_file(a.first_driver)==FIRST_SHA and sha_file(a.weak_driver)==WEAK_SHA
            and sha_file(a.high_driver)==HIGH_SHA and sha_file(a.cubic_helper)==CUBIC_SHA,
            "Exact previously completed original mathematical sources")
    x=module_at("critical_prolongation_first",a.first_driver)
    for key,value in x.PINS.items():
        require(sha_file(getattr(a,key))==value,"Every frozen original physical helper")
    require(Path(a.out).resolve() not in
            {Path(p).resolve() for p in (a.parent_out,a.high_out,a.first_out)},
            "All original ancestors remain read only")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
    w=module_at("critical_prolongation_weak",a.weak_driver)
    q7=module_at("critical_prolongation_high",a.high_driver)
    cubic=module_at("critical_prolongation_cubic_prepare",a.cubic_helper)
    m=module_at("critical_prolongation_original",a.generator)
    actions=module_at("critical_prolongation_actions",a.jet_actions)
    h=module_at("critical_prolongation_field",a.field_helper)
    F=w.make_field(h,w.FIELDS[a.field]["polynomial"])
    parent=x.Parent(w,a.parent_out,a.parent_receipt,a.field)
    high,hi=x.read_high(a,q7)
    hcache=q7.Cache(Path(a.high_out)/"checkpoints",hi["binding"])
    first,fcache,fi=first_parent(F,h,x,a)
    firstouter=json.loads(Path(a.first_receipt).read_text())["result"]["parameters"]
    require(firstouter["parent"]==x.PARENT_PINS[a.field] and
            firstouter["highParent"]==hi,"Same original first/high ancestry")
    source_sha=sha_file(__file__)
    binding=hashlib.sha256(canonical({"format":FORMAT,"scriptSHA256":source_sha,
      "helperSHA256":x.PINS,"firstSourceSHA256":FIRST_SHA,"weakSourceSHA256":WEAK_SHA,
      "highSourceSHA256":HIGH_SHA,"cubicSourceSHA256":CUBIC_SHA,
      "field":a.field,"weakParent":x.PARENT_PINS[a.field],
      "highParent":hi,"firstParent":fi})).hexdigest()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-one-nonfree-positive-prolongation-receipt.json"
    start=time.monotonic()
    result={"format":FORMAT,"status":"started","binding":binding,"scriptSHA256":source_sha,
      "parameters":{"field":a.field,"firstParent":fi,"highParent":hi,
      "weakParent":x.PARENT_PINS[a.field],"helperSHA256":x.PINS,
      "remainingSeconds":a.remaining_seconds,"memoryMiB":a.memory_mib,
      "allParentsReadOnly":True,"largeArraysTemporaryOnly":True,
      "positiveProlongationNotPrespecified":True,
      "restrictedFailureDoesNotClaimACompleteHigherConnection":True}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        result["parameters"]["checkpointManifest"]={"file":"checkpoints/manifest.json",
          "bytes":cache.path.stat().st_size,"sha256":sha_file(cache.path)}
        raw=canonical(result);require(len(raw)<90000,"Small exact positive-prolongation receipt")
        tmp=receipt.with_name(receipt.name+".tmp");tmp.write_bytes(raw);tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step};save()
    def stop(signum,frame):
        raise BudgetStop("Actual original nonfree positive-prolongation budget")
    signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,a.remaining_seconds)
    code=1
    try:
        prolong(F,h,w,x,cubic,m,actions,parent,high,hcache,first,fcache,cache,report,
                result["parameters"])
        result["status"]="completed";code=0
    except RestrictedIncompatible as exc:
        result["parameters"]["positiveProlongationVerified"]=False
        result["parameters"]["onlyDeclaredCorrectionSupportWasIncompatible"]=True
        result["parameters"]["restrictedFailure"]=str(exc)
        result["status"]="completed";code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint";code=75
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    except Exception as exc:
        result["status"]="failed";code=1
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
          "elapsedSeconds":result["elapsedSeconds"],
          "positiveProlongationVerified":result["parameters"].get("positiveProlongationVerified")},
          sort_keys=True),flush=True)
    return code

if __name__=="__main__":
    sys.exit(main())
