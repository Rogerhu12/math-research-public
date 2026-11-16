#!/usr/bin/env python3
"""Original critical-field positive jets using at most three weak quadratic columns.

Astra-ISP-789f / literature_audit; AI-assisted, GPT-6 Astra Pro.
2026-11-16. Exact Q(alpha), original seventeen equations and all6188 sources.

This is a positive-certificate probe, not a complete higher-normal solver.
For Fplus/Fminus the paid low exits are (3,3); for E8 they are (2,2).
A true kernel of [L,Cv,Dv] produces legal two-normal last corrections.
The returned leading rank gives a lower bound for the FULL local length.
Failure to increase that bound is only a statement about this candidate family.

Every source, number-field coefficient, head rank and complete jet product is
checked. Large cochains/checkpoints remain temporary; only small metadata is
published. No finite-field calculation or old normal form is rerun.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from math import comb, gcd
from pathlib import Path
import resource
import signal
import sys
import time
from flint import fmpq, fmpq_mat, fmpq_poly

FORMAT = "r150-original-critical-weak-quadratic-positive-jets-v1"
PINS = {
    "generator": "2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186",
    "jet_actions": "2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332",
    "low_generator": "4d215c80fa40d5f3548fd604e4ed77c6317db44b5b80518a03cf15e2ceeffa2f",
    "field_helper": "54f88bdbd926d38fb7a78fdaa1128f6bae96617461e4d2d4e4064736f6cf842c",
}
FIELDS = {
    "plus": {"polynomial": [-8,32,-25,5], "exit": 3, "upper": 8},
    "minus": {"polynomial": [864,864,135,5], "exit": 3, "upper": 8},
    "e8": {"polynomial": [9600,-25472,-3392,15936,-2888,-936,153,50,5],
           "exit": 2, "upper": 5},
}

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",",":")).encode("utf-8")

def sha_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for block in iter(lambda:f.read(1048576),b""):
            h.update(block)
    return h.hexdigest()

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

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

def make_field(helper,raw):
    class OriginalField(helper.Field):
        def __init__(self):
            self.degree=len(raw)-1
            self.modulus=fmpq_poly([fmpq(x,raw[-1]) for x in raw])
            self.zero=fmpq_poly([])
            self.one=fmpq_poly([1])
            self.alpha=fmpq_poly([0,1])
            self.mul_count=0
            self.inv_count=0
            require(self.modulus.degree()==self.degree and
                    self.modulus[self.degree]==1,"Original monic number field")
        def inv(self,a):
            require(bool(a),"Only actual nonzero field elements are inverted")
            self.inv_count+=1
            g,s,t=a.xgcd(self.modulus)
            require(g.degree()==0 and bool(g) and s*a+t*self.modulus==g,
                    "Original irreducible field / complete Bezout identity")
            value=(s/g[0])%self.modulus
            require(self.mul(a,value)==self.one,"Actual field inverse product")
            return value
        def scalar(self,a):
            return fmpq_poly([fmpq(a)])
    return OriginalField()

def join_columns(*matrices):
    require(bool(matrices) and len({len(a) for a in matrices})==1,
            "Complete column concatenation shape")
    return [sum((a[i] for a in matrices),[]) for i in range(len(matrices[0]))]

def add_matrices(a,b):
    require(len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b)),
            "Exact matrix addition shape")
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]

def negate(a):
    return [[-x for x in row] for row in a]

def rational_rows(a):
    """Only nonzero rational row contents, never a vanishing parameter factor."""
    units=[]
    for row in a:
        vals=[q for x in row for q in x.coeffs() if q]
        den=1
        for q in vals:
            den=den//gcd(den,int(q.q))*int(q.q)
        num=0
        for q in vals:
            num=gcd(num,abs(int(q.p)*(den//int(q.q))))
        units.append(fmpq(num,den) if num else fmpq(1))
    b=[[x/u for x in row] for row,u in zip(a,units)]
    require(all(y*u==x for row,new,u in zip(a,b,units)
                for x,y in zip(row,new)),"All rational row-content identities")
    return b,units

def exact_kernel(F,h,a,cache,prefix,report):
    digest=F.matrix_hash(a)
    old=cache.get(prefix+"-kernel")
    if old is not None:
        require(old["inputSHA256"]==digest and old["allOriginalRowsVerified"],
                "Complete kernel checkpoint for identical input")
        return F.matrix_from_json(old["kernel"]),old
    b,units=rational_rows(a)
    rows,cols,_=h.bareiss_profile(F,b,cache,prefix,report)
    rank=len(cols)
    nr,nc=h.shape(a)
    free=[j for j in range(nc) if j not in set(cols)]
    kernel=h.zeros(F,nc,len(free))
    for j,c in enumerate(free):
        kernel[c][j]=F.one
    if rank and free:
        unit=h.submatrix(b,rows,cols)
        rhs=negate(h.submatrix(b,rows,free))
        fac=h.lu_factor(F,unit,cache,prefix)
        solution=h.lu_solve(F,fac,rhs)
        require(h.product(F,unit,solution)==rhs,"Every selected unit equation")
        for i,c in enumerate(cols):
            kernel[c]=solution[i][:]
    require(h.zero_matrix(h.product(F,a,kernel)),
            "Complete original field matrix times its kernel")
    require(h.submatrix(kernel,free,range(len(free)))==h.identity(F,len(free)),
            "Complete free-coordinate identity")
    meta={"inputSHA256":digest,"rank":rank,"shape":[nr,nc],
          "independentRows":rows,"independentColumns":cols,"freeColumns":free,
          "rationalRowContents":[str(u) for u in units],
          "kernel":F.matrix_json(kernel),"kernelSHA256":F.matrix_hash(kernel),
          "allOriginalRowsVerified":True,"allUnitRowsVerified":True}
    cache.put(prefix+"-kernel",meta,True)
    return kernel,meta

def compact_kernel(meta):
    return {k:v for k,v in meta.items() if k not in
            ("kernel","rationalRowContents")}

def encode_polynomial_model(m,small,coeff,meta):
    return {
        "small":[[[str(x[i,j]) for j in range(x.ncols())]
                  for i in range(x.nrows())] for x in small],
        "pure":[[str(x) for x in row] for row in coeff["pure"]],
        "linear":{str(j):[[[str(x) for x in row] for row in mode]
                          for mode in coeff["linear"][j]] for j in range(2,11)},
        "physical":coeff["physical"],"meta":meta,
    }

def decode_polynomial_model(m,obj):
    small=[m.fmpq_mat([[m.fmpq(x) for x in row] for row in a])
           for a in obj["small"]]
    coeff={"chart":"zero","maxOrder":25,"pure":[[m.fmpq(x) for x in row]
             for row in obj["pure"]],"linear":{
             int(j):[[[m.fmpq(x) for x in row] for row in mode] for mode in a]
             for j,a in obj["linear"].items()},"quadratic":{},
             "physical":obj["physical"]}
    return small,coeff,obj["meta"]

def original_model(m,actions,base,cache):
    old=cache.get("original-polynomial-model")
    if old is None:
        small,coeff,meta=base.original_low_polynomial_model(m,actions)
        cache.put("original-polynomial-model",
                  encode_polynomial_model(m,small,coeff,meta),True)
        return small,coeff,meta
    return decode_polynomial_model(m,old)

def field_coefficients(F,coeff,order):
    powers=[F.one]
    for _ in range(25):
        powers.append(F.mul(powers[-1],F.alpha))
    def taylor(values):
        require(len(values)==26,"All original parameter coefficients retained")
        return [sum((values[k]*comb(k,j)*powers[k-j] for k in range(j,26)
                     if values[k]),F.zero) for j in range(order+1)]
    pure=h_transpose([taylor([coeff["pure"][k][i] for k in range(26)])
                      for i in range(17)])
    linear={}
    for j in range(2,11):
        linear[j]=[h_transpose([taylor([coeff["linear"][j][mode][k][i]
                                      for k in range(26)])
                                 for i in range(17)]) for mode in range(3)]
    return {"pure":pure,"linear":linear,"quadratic":{},
            "chart":"s=alpha+t","maxOrder":order}

def h_transpose(a):
    return [list(v) for v in zip(*a)]

def physical_quadratic_constant(F,h,m,local_coeff):
    """Original quadratic normal coefficients at alpha only; no fake higher jets."""
    def qmatrix(a):
        return [[F.scalar(a[i,j]) for j in range(a.ncols())] for i in range(a.nrows())]
    Kq=m.fmpq_mat(m.ORIGINAL_K)
    J2=m.polynomial_power_kernel(Kq,2)
    J3=m.polynomial_power_kernel(Kq,3)
    inverse=J3.inv()
    require(inverse*J3==m.fmpq_mat([[int(i==j) for j in range(16)]
                                  for i in range(16)]),"Original J3 rational inverse")
    K=qmatrix(Kq)
    powers=[F.one]
    for _ in range(10):
        powers.append(F.mul(powers[-1],F.alpha))
    y=powers[:6]
    p=[sum((Kq[i,j]*y[j] for j in range(6)),F.zero) for i in range(6)]
    B=[[p[i-j] if 0<=i-j<6 else F.zero for j in range(11)] for i in range(16)]
    tensor_map=h.product(F,h.product(F,qmatrix(inverse),B),qmatrix(J2))
    def mm(a,b):
        return h.product(F,a,b)
    def trace(a):
        return sum((a[i][i] for i in range(len(a))),F.zero)
    def moments(j):
        return [comb(i,j)*powers[i-j] if i>=j else F.zero for i in range(11)]
    def polar(a):
        z=mm(mm(K,a),K)
        return [sum((z[i][j] for i in range(6) for j in range(6) if i+j==d),
                    F.zero) for d in range(11)]
    def data(v):
        M=[[v[i+j] for j in range(6)] for i in range(6)]
        tensor=[row[0] for row in mm(tensor_map,[[x] for x in v])]
        KM=mm(K,M)
        KMK=mm(KM,K)
        quad=mm(mm(M,K),M)
        tau=trace(mm(KM,KM))
        polar_quad=polar([[4*x for x in row] for row in quad])
        qp=[row[0] for row in mm(quad,[[x] for x in p])]
        contract=[sum((F.mul(tensor[i+j+k],KMK[j][k])
                       for j in range(6) for k in range(6)),F.zero) for i in range(6)]
        gamma=[2*F.mul(tau,y[i])+8*qp[i]-12*contract[i] for i in range(6)]
        lp=[[sum((F.mul(tensor[i+j+k],p[k]) for k in range(6)),F.zero)
             for j in range(6)] for i in range(6)]
        linear=polar([[6*x for x in row] for row in lp])+[F.zero]*6
        return polar_quad+gamma,linear
    original=[moments(j) for j in range(11)]
    vals=[data(v) for v in original]
    require(all(not x for x in vals[0][0]+vals[0][1]+vals[1][1]),
            "Original c tangent and both tangent linear parts")
    require(vals[1][0]==local_coeff["pure"][0],
            "All17 actual d-squared coefficients at alpha")
    mixed,_=data([a+b for a,b in zip(original[0],original[1])])
    require(mixed==local_coeff["pure"][0],"Original mixed tangent identity")
    quadratic={}
    for j in range(2,11):
        require(vals[j][1]==local_coeff["linear"][j][0][0],
                "Original linear normal coefficient, all17")
        quadratic[(j,j)]=[vals[j][0]]
        for mode in (1,2):
            t=mode-1
            both,_=data([a+b for a,b in zip(original[t],original[j])])
            cross=[both[i]-vals[t][0][i]-vals[j][0][i] for i in range(17)]
            require(cross==local_coeff["linear"][j][mode][0],
                    "Original c/d-normal polarization, all17")
        for l in range(j+1,11):
            both,_=data([a+b for a,b in zip(original[j],original[l])])
            quadratic[(j,l)]=[[both[i]-vals[j][0][i]-vals[l][0][i]
                               for i in range(17)]]
    local_coeff["quadratic"]=quadratic
    return {"originalJ2SHA256":m.matrix_hash(J2),"originalJ3SHA256":m.matrix_hash(J3),
            "quadraticConstantSHA256":F.matrix_hash([quadratic[pair][0]
                                       for pair in sorted(quadratic)]),
            "ordinaryMonomialPairs":[list(pair) for pair in sorted(quadratic)],
            "all17PureAnd27LinearCrossChecksVerified":True,
            "higherQuadraticTaylorCoefficientsNotFabricated":True}

def action(F,h,actions,coeff,order,sections,ncols):
    """Full original6188 source product, retaining the original source partition."""
    result=[]
    for r in range(4):
        rows=actions.source_rows(r)
        out=h.zeros(F,len(rows),ncols)
        for degree,X in sections.items():
            if degree<r or degree>r+2 or h.zero_matrix(X):
                continue
            cols=actions.target_columns(degree)
            require(h.shape(X)==(len(cols),ncols),"Actual target-sector dimensions")
            if degree==r+2:
                require(order==0,"Only real order0 quadratic data is available")
            index={key:j for j,key in enumerate(cols)}
            for i,row in enumerate(rows):
                for c,value in actions.sparse_row_terms(coeff,order,row,degree,index):
                    for j,x in enumerate(X[c]):
                        if x:
                            out[i][j]=out[i][j]+F.mul(value,x)
        result.extend(out)
    require(len(result)==6188,"All original17 times364 multipliers retained")
    return result

def embed_low(F,h,actions,low,X):
    nc=h.shape(X)[1]
    result={r:h.zeros(F,len(actions.target_columns(r)),nc) for r in (0,1)}
    indices={r:{key:i for i,key in enumerate(actions.target_columns(r))} for r in (0,1)}
    for k,(a,b,mon) in enumerate(low):
        degree=len(mon)
        result[degree][indices[degree][(a,b,tuple(mon))]]=X[k][:]
    return result

def row_indices(actions):
    full=[row for r in range(4) for row in actions.source_rows(r)]
    low=[i for i,(eq,a,b,mon) in enumerate(full) if not mon and a+b<=1]
    require(len(full)==6188 and len(low)==51,"Full and low source dictionaries")
    return full,low

def canonical_low_jets(F,h,small,order,cache,report):
    old=cache.get("canonical-low-jets")
    series,meta=h.normalize_and_taylor(F,small,order)
    # The helper only removes six globally zero pure columns. Restore them
    # explicitly so all36 original low coordinates and all11 heads are retained.
    keep=meta["retainedOriginalLowColumns"]
    series36=[]
    for a in series:
        b=h.zeros(F,51,36)
        for i in range(51):
            for jj,j in enumerate(keep):
                b[i][j]=a[i][jj]
        series36.append(b)
    require(len(keep)==30 and len(meta["sixIdenticallyZeroOriginalColumns"])==6,
            "All six exact low pure columns restored")
    digest=hashlib.sha256(canonical([F.matrix_hash(a) for a in series36])).hexdigest()
    if old is not None:
        require(old["seriesIdentity"]==digest and old["allEarlierRowsZero"],
                "Same verified original low Taylor series")
        return series36,[F.matrix_from_json(a) for a in old["jets"]], \
               F.matrix_from_json(old["exitResidual"]),meta,old
    kernel,kmeta=exact_kernel(F,h,series36[0],cache,"constant-low",report)
    require(kmeta["rank"]==25 and h.shape(kernel)==(36,11),
            "Paid critical low constant rank25 / eleven independent heads")
    rows,cols=kmeta["independentRows"],kmeta["independentColumns"]
    U=h.submatrix(series36[0],rows,cols)
    factor=h.lu_factor(F,U,cache,"canonical-low-original-unit")
    jets=[kernel]
    residual=None
    for k in range(1,order+1):
        key="canonical-low-order-"+str(k)
        saved=cache.get(key)
        if saved is not None:
            require(saved["seriesIdentity"]==digest,"Exact same local coefficient prefix")
            X=F.matrix_from_json(saved["jet"])
            R=F.matrix_from_json(saved["residual"])
        else:
            forcing=h.zeros(F,51,11)
            for i in range(1,k+1):
                forcing=add_matrices(forcing,h.product(F,series36[i],jets[k-i]))
            rhs=negate(h.submatrix(forcing,rows,range(11)))
            solved=h.lu_solve(F,factor,rhs)
            require(h.product(F,U,solved)==rhs,"All25 original unit equations")
            X=h.zeros(F,36,11)
            for i,c in enumerate(cols):
                X[c]=solved[i][:]
            R=add_matrices(forcing,h.product(F,series36[0],X))
            require(h.zero_matrix(h.submatrix(R,rows,range(11))),
                    "Actual original unit rows killed")
            if k<order:
                require(h.zero_matrix(R),"Every earlier original51 row vanishes")
            cache.put(key,{"seriesIdentity":digest,"jet":F.matrix_json(X),
                           "residual":F.matrix_json(R),"allUnitRowsVerified":True,
                           "allRowsZero":h.zero_matrix(R)},True)
        require(k==order or h.zero_matrix(R),"All earlier Taylor products zero")
        jets.append(X)
        residual=R
    _,exitmeta=exact_kernel(F,h,residual,cache,"paid-low-exit",report)
    require(exitmeta["rank"]==2,"The two actual low exits at the paid order")
    payload={"seriesIdentity":digest,"jets":[F.matrix_json(a) for a in jets],
             "exitResidual":F.matrix_json(residual),
             "normalization":meta,"constantKernel":compact_kernel(kmeta),
             "exitRank":2,"allEarlierRowsZero":True,
             "allOriginalUnitRowsVerified":True}
    cache.put("canonical-low-jets",payload,True)
    return series36,jets,residual,meta,payload

def weak_columns(F,h,actions,coeff,low_rows,row_units,cache,report):
    L=[[coeff["linear"][j][0][0][i] for j in range(2,11)] for i in range(17)]
    C=[[coeff["linear"][j][1][0][i] for j in range(2,11)] for i in range(17)]
    D=[[coeff["linear"][j][2][0][i] for j in range(2,11)] for i in range(17)]
    V,vm=exact_kernel(F,h,L,cache,"normal-linear",report)
    require(vm["rank"]==8 and h.shape(V)==(9,1),"Actual original normal linear rank8")
    Cv,Dv=h.product(F,C,V),h.product(F,D,V)
    pencil=join_columns(L,Cv,Dv)
    W,wm=exact_kernel(F,h,pencil,cache,"weak-quadratic-pencil",report)
    q=h.shape(W)[1]
    require(1<=q<=3,"At most three genuine weak quadratic parameters")
    cols=actions.target_columns(2)
    index={key:i for i,key in enumerate(cols)}
    Z=h.zeros(F,len(cols),q)
    for j in range(2,11):
        for l in range(j,11):
            vi,vl=V[j-2][0],V[l-2][0]
            for a in range(q):
                Z[index[(0,0,(j,l))]][a]=F.mul(vi,W[l-2][a])+F.mul(W[j-2][a],vl)
                vv=F.mul(vi,vl)
                Z[index[(1,0,(j,l))]][a]=F.mul(W[9][a],vv)
                Z[index[(0,1,(j,l))]][a]=F.mul(W[10][a],vv)
    _,zm=exact_kernel(F,h,Z,cache,"weak-quadratic-independent-columns",report)
    require(zm["rank"]==q,"True independent quadratic coefficient functionals")
    product=action(F,h,actions,coeff,0,{2:Z},q)
    allowed=set(low_rows)
    require(all(not x for i,row in enumerate(product) if i not in allowed for x in row),
            "All6137 original source rows outside the low51 vanish")
    G=[[x/fmpq(row_units[i]) for x in product[r]] for i,r in enumerate(low_rows)]
    data={"L":F.matrix_json(L),"linearKernel":F.matrix_json(V),
          "pencilKernel":F.matrix_json(W),"highColumns":F.matrix_json(Z),
          "originalProduct":F.matrix_json(product),"scaledLowReturn":F.matrix_json(G),
          "pencilKernelMetadata":compact_kernel(wm),
          "all6137OriginalHighAndOtherRowsZero":True,
          "all6188OriginalProductsComputed":True,
          "ordinaryDiagonalValuesUseNoDividedPowerNormalization":True}
    cache.put("weak-quadratic-original-columns",data,True)
    return Z,G,{"dimension":q,"normalLinear":compact_kernel(vm),
                 "pencil":compact_kernel(wm),"highColumnSHA256":F.matrix_hash(Z),
                 "lowReturnSHA256":F.matrix_hash(G),
                 "all6137OriginalHighAndOtherRowsZero":True,
                 "originalProductCoordinates":6188*q}

def finish_probe(F,h,m,actions,coeff,low,exact_pure,series,jets,R,Z,G,
                 order,upper,cache,report,params):
    q=h.shape(Z)[1]
    combined=join_columns(series[0],G,R)
    K,km=exact_kernel(F,h,combined,cache,"candidate-jet-equation",report)
    headrows=range(36+q,47+q)
    H=h.submatrix(K,headrows,range(h.shape(K)[1]))
    _,hm=exact_kernel(F,h,H,cache,"candidate-leading-projection",report)
    r=hm["rank"]
    require(9<=r<=11,"True head rank includes the nine low formal free heads")
    chosen=hm["independentColumns"]
    selected=h.submatrix(K,range(47+q),chosen)
    heads=h.submatrix(selected,headrows,range(r))
    x=h.submatrix(selected,range(36),range(r))
    a=h.submatrix(selected,range(36,36+q),range(r))
    last_high=h.product(F,Z,a)
    low_jets=[h.product(F,X,heads) for X in jets]
    low_jets[-1]=add_matrices(low_jets[-1],x)
    full=[]
    for k,X in enumerate(low_jets):
        sections=embed_low(F,h,actions,low,X)
        if k==order:
            sections[2]=last_high
        full.append(sections)
    exact=h.zeros(F,20,4)
    index0={key:i for i,key in enumerate(actions.target_columns(0))}
    require(len(exact_pure)==4,"The four additional exact pure coordinates")
    for j,(aa,bb,mon) in enumerate(exact_pure):
        require(not mon and bb<=1 and 4<=aa+bb<=5,"Exact pure support")
        exact[index0[(aa,bb,())]][j]=F.one
    for k in range(order+1):
        for degree in (0,1,2):
            old=full[k].get(degree,h.zeros(F,len(actions.target_columns(degree)),r))
            extra=exact if k==0 and degree==0 else \
                  h.zeros(F,len(actions.target_columns(degree)),4)
            full[k][degree]=join_columns(old,extra)
    width=r+4
    leading=full[0][0]+full[0][1]+full[0][2]
    _,lm=exact_kernel(F,h,leading,cache,"full-original-leading-heads",report)
    require(lm["rank"]==width,"All original constant heads are independent")
    product_hashes=[]
    for k in range(order+1):
        total=h.zeros(F,6188,width)
        for i in range(k+1):
            total=add_matrices(total,action(F,h,actions,coeff,i,full[k-i],width))
        require(h.zero_matrix(total),"All original6188 coefficient products at order"+str(k))
        product_hashes.append(F.matrix_hash(total))
    hgain=r-9
    length=2*order+hgain
    require(length<=upper,"Positive original lower bound respects paid full upper bound")
    square_rows=[actions.target_columns(2).index((0,0,(j,j))) for j in range(2,11)]
    square_meta=[]
    for k in range(order+1):
        read=h.submatrix(full[k][2],square_rows,range(width))
        square_meta.append({"order":k,"shape":[9,width],
                            "sha256":F.matrix_hash(read),
                            "nonzeroEntries":sum(bool(z) for row in read for z in row)})
    payload={"targetSectors":[0,1,2],"higherTargetSectorsExactlyZero":[3,4,5],
             "cochains":[{str(d):F.matrix_json(X) for d,X in sections.items()}
                         for sections in full],
             "leadingMap":F.matrix_json(heads),
             "candidateSelectedKernel":F.matrix_json(selected),
             "canonicalLowJetTransportRetained":True,
             "all6188OriginalProductsZero":True,
             "originalProductsCoordinates":6188*width*(order+1),
             "originalProductSHA256":product_hashes,
             "fullLeadingRank":width,"gain":hgain}
    pack=cache.put("complete-positive-jets-verified",payload,True)
    params.update({
        "combinedShape":[51,47+q],"combinedRank":km["rank"],
        "combinedKernelDimension":h.shape(K)[1],
        "candidateLeadingRank":r,"fullOriginalLeadingRank":width,
        "constantHeadCount":15,"fullGenericFreeHeadCount":13,
        "additionalPositiveLengthLowerBound":hgain,
        "fullOriginalLengthLowerBound":length,
        "paidFullOriginalLengthUpperBound":upper,
        "allOriginal6188JetProductsZero":True,
        "originalJetProductCoordinates":6188*width*(order+1),
        "originalProductSHA256":product_hashes,
        "allOriginalLeadingHeadsIndependent":True,
        "ordinaryNineSquareReadouts":square_meta,
        "verifiedCochainCheckpoint":pack,
        "completeHighCorrectionSpaceNotClaimed":True,
        "zeroGainIsNotAFullConnectionLowerBound":True,
        "noFullGenericOrGlobalTargetMembershipClaimed":True})
    return payload

def main():
    ap=argparse.ArgumentParser()
    for name in PINS:
        ap.add_argument("--"+name.replace("_","-"),required=True)
    ap.add_argument("--field",choices=tuple(FIELDS),required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--remaining-seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=2048)
    args=ap.parse_args()
    require(0<args.remaining_seconds<=1800 and 512<=args.memory_mib<=8192,
            "Explicit shared mathematical and memory budgets")
    for key,digest in PINS.items():
        require(sha_file(getattr(args,key))==digest,"Pinned helper "+key)
    resource.setrlimit(resource.RLIMIT_AS,(args.memory_mib*1024**2,)*2)
    source_sha=sha_file(__file__)
    settings=FIELDS[args.field]
    binding=hashlib.sha256(canonical({"format":FORMAT,"sourceSHA256":source_sha,
             "helpers":PINS,"field":args.field,"settings":settings,
             "originalSourceCount":6188,"originalTargetCount":4367})).hexdigest()
    out=Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    cache=Cache(out/"checkpoints",binding)
    receipt=out/"critical-weak-quadratic-positive-jets-receipt.json"
    start=time.monotonic()
    result={"format":FORMAT,"status":"started","binding":binding,
            "scriptSHA256":source_sha,"parameters":{
                "field":args.field,"fieldPolynomialAscending":settings["polynomial"],
                "fieldDegree":len(settings["polynomial"])-1,
                "actualNaturalParameter":"t=s-alpha",
                "originalMomentChange":"m_i=sum_j binom(i,j)(alpha+t)^(i-j)n_j",
                "helperSHA256":PINS,"remainingSeconds":args.remaining_seconds,
                "memoryMiB":args.memory_mib,"lastJetOrder":settings["exit"],
                "paidOriginalConstantRank":4352,"paidOriginalGenericRank":4354,
                "paidLowConstantRank":25,"paidLowGenericRank":27,
                "paidLowPositiveSpectrum":[settings["exit"],settings["exit"]],
                "newGainNotPrespecified":True,
                "originalEquations":17,"originalSourceColumns":6188,
                "originalTargetRows":4367,"largeDataUploadedOrCommitted":False,
                "newFiniteFieldCalculation":False,
                "largeOriginalEliminationRecomputed":False}}
    def save():
        result["elapsedSeconds"]=time.monotonic()-start
        result["parameters"]["checkpointManifest"]={
            "file":"checkpoints/manifest.json","bytes":cache.path.stat().st_size,
            "sha256":sha_file(cache.path)}
        raw=canonical(result)
        require(len(raw)<90000,"Small exact receipt, no matrix data published")
        tmp=receipt.with_name(receipt.name+".tmp")
        tmp.write_bytes(raw)
        tmp.replace(receipt)
    def report(phase,step):
        result["parameters"]["currentPhase"]={"name":phase,"step":step}
        save()
    def stop(signum,frame):
        raise BudgetStop("Shared critical-field mathematical budget exhausted")
    signal.signal(signal.SIGALRM,stop)
    signal.signal(signal.SIGTERM,stop)
    signal.setitimer(signal.ITIMER_REAL,args.remaining_seconds)
    exit_code=1
    try:
        m=load_module("critical_original_generator",args.generator)
        actions=load_module("critical_original_actions",args.jet_actions)
        base=load_module("critical_original_low",args.low_generator)
        h=load_module("critical_number_field_helper",args.field_helper)
        F=make_field(h,settings["polynomial"])
        require(h.shape(h.identity(F,F.degree))==(F.degree,F.degree),"Actual field setup")
        g=fmpq_poly([0,0,24,-8,-2])%F.modulus
        derivative=fmpq_poly([i*settings["polynomial"][i]
                               for i in range(1,len(settings["polynomial"]))])%F.modulus
        require(bool(g) and bool(derivative),"Noncontact and separable original field")
        F.inv(g);F.inv(derivative)
        small,poly_coeff,meta=original_model(m,actions,base,cache)
        result["parameters"]["originalPolynomialEmbedding"]=meta
        save()
        order=settings["exit"]
        coeff=field_coefficients(F,poly_coeff,order)
        series,jets,R,norm,lowmeta=canonical_low_jets(F,h,small,order,cache,report)
        result["parameters"]["actualCanonicalLow"]={
            "shape":[51,36],"constantRank":25,"headRank":11,
            "exitRank":lowmeta["exitRank"],"allEarlierRowsZero":True,
            "seriesIdentity":lowmeta["seriesIdentity"],
            "nonzeroRationalRowContentsSHA256":
                hashlib.sha256(canonical(norm["nonzeroRationalRowContents"])).hexdigest()}
        result["parameters"]["quadraticPhysicalChecks"]=physical_quadratic_constant(
            F,h,m,coeff)
        _,low_rows=row_indices(actions)
        low=[(a,b,tuple(mon)) for a,b,mon in meta["lowTargetColumns"]]
        exact_pure=[(a,b,tuple(mon)) for a,b,mon in meta["exactPureTargetColumns"]]
        require(len(low)==36 and len(set(low))==36,"All original low coordinates")
        # Cross-check the field Taylor block against the full sparse original
        # action on its36 original coefficient functionals, for every order.
        E=embed_low(F,h,actions,low,h.identity(F,36))
        low_allowed=set(low_rows)
        for k in range(order+1):
            complete=action(F,h,actions,coeff,k,E,36)
            require(all(not x for i,row in enumerate(complete)
                        if i not in low_allowed for x in row),
                    "All6137 rows outside low embedding for every Taylor order")
            reduced=[[x/fmpq(norm["nonzeroRationalRowContents"][i])
                      for x in complete[r]] for i,r in enumerate(low_rows)]
            require(reduced==series[k],"All original low Taylor coordinates")
        result["parameters"]["all6188LowEmbeddingRowsVerifiedThroughOrder"]=order
        save()
        Z,G,wmeta=weak_columns(F,h,actions,coeff,low_rows,
                              norm["nonzeroRationalRowContents"],cache,report)
        result["parameters"]["weakQuadraticColumns"]=wmeta
        save()
        finish_probe(F,h,m,actions,coeff,low,exact_pure,series,jets,R,Z,G,
                     order,settings["upper"],cache,report,result["parameters"])
        result["parameters"]["fieldArithmetic"]={
            "exactMultiplications":F.mul_count,"verifiedInverses":F.inv_count,
            "regularRepresentationExpansionUsed":False}
        result["status"]="completed"
        exit_code=0
    except BudgetStop as exc:
        result["status"]="budget-checkpoint"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
        exit_code=75
    except Exception as exc:
        result["status"]="failed"
        result["parameters"]["error"]={"type":type(exc).__name__,"message":str(exc)}
        exit_code=1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        save()
        print(json.dumps({"status":result["status"],"receipt":str(receipt),
                          "bytes":receipt.stat().st_size,"sha256":sha_file(receipt),
                          "elapsedSeconds":result["elapsedSeconds"],
                          "gain":result["parameters"].get("additionalPositiveLengthLowerBound")},
                         sort_keys=True),flush=True)
    return exit_code

if __name__=="__main__":
    sys.exit(main())
