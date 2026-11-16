#!/usr/bin/env python3
"""Complete original Bell saturation: bounded homogeneous source prefixes.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
All six means and all eleven Hankel coordinates remain variables.
The Singular stage is ONLY over the explicitly checked place p=127,d=100.
Every completed prefix includes original-source identities and a complete
Buchberger check through its stated weighted degree. A field witness is
not a characteristic-zero witness. Exact E lifting is a separate consumer.
No mathematical output is intended for permanent repository storage.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, os, resource
import shutil, signal, subprocess, sys, time
from pathlib import Path
from flint import fmpq, fmpq_poly, nmod_mpoly_ctx

FORMAT = "r150-original-full-bell-homogeneous-source-prefix-v1"
HELPER_NAME = "2026-11-16-r150-original-matched-bell-full-parameter-charts-v2-789f.py"
HELPER_SHA = "31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
HELPER_BYTES = 16964
PRIME, PLACE = 127, 100
WEIGHTS = (1,)*6 + (2,)*11 + (1,)
NAMES = tuple("y%d"%i for i in range(6)) + tuple("H%d"%i for i in range(11)) + ("tt",)
SOURCE_WEIGHTS = (4,)*11 + (5,)*6 + (3,)
SOURCE_LABELS = ["dH%d"%i for i in range(11)] + ["dy%d"%i for i in range(6)] + ["Bell-minus-tt-cubed"]
class Budget(Exception): pass
def need(ok, message):
    if not ok: raise ValueError(message)
def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",",":"), ensure_ascii=True).encode("ascii")
def digest(b): return hashlib.sha256(b).hexdigest()
def identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        while True:
            b=f.read(1048576)
            if not b: break
            h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def atomic(p, b):
    p.parent.mkdir(parents=True, exist_ok=True)
    q=p.with_name(p.name+".tmp"); q.write_bytes(b); os.replace(q,p)
def json_save(p,x):
    atomic(p,canonical(x)); return identity(p)
def gz_save(p,x):
    b=canonical(x); atomic(p,gzip.compress(b,compresslevel=1,mtime=0))
    return {**identity(p),"logicalBytes":len(b),"logicalSha256":digest(b)}
def gz_load(root,desc):
    p=root/desc["path"]; need(identity(p)=={k:desc[k] for k in ("path","bytes","sha256")},"complete compressed input SHA")
    b=gzip.decompress(p.read_bytes())
    need(len(b)==desc["logicalBytes"] and digest(b)==desc["logicalSha256"],"complete logical input SHA")
    return json.loads(b)
def module(p):
    s=importlib.util.spec_from_file_location("r150_exact_original_bell_helper",p)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def q127(q):
    q=fmpq(q); d=int(q.denom())%PRIME
    need(d!=0,"every original rational coefficient is integral at127")
    return int(q.numer())%PRIME*pow(d,-1,PRIME)%PRIME
def poly_record(d):
    return [[list(e),int(c)%PRIME] for e,c in sorted(d.items()) if int(c)%PRIME]
def record_dict(a,n):
    d={}
    for e,c in a:
        need(len(e)==n and all(isinstance(x,int) and x>=0 for x in e),"full original exponent tuple")
        e=tuple(e); need(e not in d,"no repeated polynomial monomial")
        c=int(c); need(0<c<PRIME,"canonical nonzero field coefficient"); d[e]=c
    return d
def add_term(d,e,c):
    c=(d.get(e,0)+c)%PRIME
    if c: d[e]=c
    elif e in d: del d[e]
def prepare(m):
    Ff=m.Field(); d=fmpq_poly([0,1])
    a=Ff.mul(-(521*d*d-46784*d+271360),Ff.inv(160*(5*d-704)))
    r=[a,(a+d)%Ff.f,Ff.zero,Ff.zero,Ff.zero,Ff.one]
    need((160*(5*d-704)*a+521*d*d-46784*d+271360)%Ff.f==0,"unchanged matched cubic direction")
    J,Ji=m.j3(); y=list(m.GEN[:6]); h=list(m.GEN[6:])
    H=[[h[i+j] for j in range(6)] for i in range(6)]
    p=m.mv(m.KRAW,y); f=m.dot(y,p)/2
    KH=m.mm(m.KRAW,H); KH2=m.mm(KH,KH); HKH=m.mm(H,KH); KHK=m.mm(m.KRAW,m.mm(H,m.KRAW))
    b=m.dot(p,m.mv(H,p)); c=m.dot(p,m.mv(HKH,p)); t2=m.tr(KH2); t3=m.tr(m.mm(KH2,KH))
    G=f**3-6*f*b+6*f*t2+12*c-8*t3
    polar=[sum((KHK[i][j] for i in range(6) for j in range(6) if i+j==k),m.ZERO) for k in range(11)]
    dp=m.conv(m.conv(p,p),p); ep=m.conv(polar,p)
    ell=[dp[i]-6*ep[i] for i in range(16)]
    ellinv=[sum((ell[j]*Ji[i,j] for j in range(16)),m.ZERO) for i in range(16)]
    R=G-m.dot(ell,ellinv)/2; m.weighted(R,6)
    eq=[R.derivative(6+i) for i in range(11)]+[R.derivative(i) for i in range(6)]
    for i,z in enumerate(eq): m.weighted(z,4 if i<11 else 5)
    V=[-z/4 for z in ellinv]; Hp=m.mv(H,p)
    N=[[f*y[i]*y[j]-2*f*H[i][j]-2*(y[i]*Hp[j]+Hp[i]*y[j])
        +4*sum((V[i+j+k]*p[k] for k in range(6)),m.ZERO)+4*HKH[i][j]
        for j in range(6)] for i in range(6)]
    KNK=m.mm(m.KRAW,m.mm(N,m.KRAW))
    original_H=[-6*sum((KNK[i][j] for i in range(6) for j in range(6) if i+j==k),m.ZERO) for k in range(11)]
    HKHp=m.mv(HKH,p)
    Gamma=[(f**2-2*b+2*t2)*y[i]-4*f*Hp[i]+8*HKHp[i]
        +4*sum((V[i+j+k]*p[j]*p[k] for j in range(6) for k in range(6)),m.ZERO)
        -8*sum((V[i+j+k]*KHK[j][k] for j in range(6) for k in range(6)),m.ZERO) for i in range(6)]
    need(eq==original_H+[3*z for z in m.mv(m.KRAW,Gamma)],"all17 original Schur and N/Gamma identities")
    need(6*R==sum((y[i]*eq[11+i] for i in range(6)),m.ZERO)+
        2*sum((h[i]*eq[i] for i in range(11)),m.ZERO),"full weighted Euler original-source identity")
    ar=[sum((y[i]*r[i][k] for i in range(6)),m.ZERO) for k in range(3)]
    rr=[Ff.zero for _ in range(11)]
    for i in range(6):
        for j in range(6): rr[i+j]=(rr[i+j]+Ff.mul(r[i],r[j]))%Ff.f
    cr=[Ff.zero for _ in range(16)]
    for i in range(6):
        for j in range(11): cr[i+j]=(cr[i+j]+Ff.mul(r[i],rr[j]))%Ff.f
    wr=[sum((cr[j]*Ji[i,j] for j in range(16)),Ff.zero)%Ff.f for i in range(16)]
    hr=[sum((h[i]*rr[i][k] for i in range(11)),m.ZERO) for k in range(3)]
    ar3=Ff.mul_polys(Ff.mul_polys(ar,ar),ar); ahr=Ff.mul_polys(ar,hr)
    bell=[ar3[k]-6*ahr[k]-sum((ell[i]*wr[i][k] for i in range(16)),m.ZERO) for k in range(3)]
    for z in bell: m.weighted(z,3)
    cubic=m.MATCHED
    ev=sum(cubic[i]*pow(PLACE,i,PRIME) for i in range(4))%PRIME
    derivative=sum(i*cubic[i]*pow(PLACE,i-1,PRIME) for i in range(1,4))%PRIME
    need(ev==0 and derivative!=0 and cubic[-1]%PRIME!=0,"legal simple127 place of original matched cubic")
    original=[]; affine=[]; integral_count=0
    for z in eq:
        field={}
        for e,q in z.to_dict().items():
            v=q127(q); integral_count+=1
            if v: field[tuple(map(int,e))+(0,)]=v
        original.append(poly_record(field))
        affine.append(poly_record({e[:-1]:c for e,c in field.items()}))
    field_bell={}
    for k,z in enumerate(bell):
        for e,q in z.to_dict().items():
            v=q127(q); integral_count+=1
            add_term(field_bell,tuple(map(int,e)),v*pow(PLACE,k,PRIME))
    fh={e+(0,):v for e,v in field_bell.items()}
    add_term(fh,(0,)*17+(3,),-1); original.append(poly_record(fh))
    fa=dict(field_bell); add_term(fa,(0,)*17,-1); affine.append(poly_record(fa))
    for i,row in enumerate(original):
        need(row and all(sum(x*w for x,w in zip(e,WEIGHTS))==SOURCE_WEIGHTS[i] for e,c in row),
            "all18 homogeneous original generators and every term retained")
    return {"K":m.KRAW,"J3Determinant":str(J.det()),"matchedCubic":cubic,
        "matchedDirection":[m.vals(x) for x in r],"R3":m.pv(R),
        "originalSeventeenGradients":[m.pv(z) for z in eq],
        "BellFieldComponents":[m.pv(z) for z in bell],
        "fieldHomogeneousGenerators":original,"fieldAffineGenerators":affine,
        "sourceLabels":SOURCE_LABELS,"sourceWeights":list(SOURCE_WEIGHTS),
        "variableNames":list(NAMES),"weights":list(WEIGHTS),
        "place":{"prime":PRIME,"root":PLACE,"polynomialValue":ev,"derivativeValue":derivative,
                 "leadingCoefficient":cubic[-1]%PRIME,"verifiedIntegralCoefficientCount":integral_count},
        "matchedCubicIrreducibility":m.irreducible(),
        "all512OriginalJ3InverseProductsVerified":True,
        "all17OriginalGradientPolynomialsVerified":True,
        "allWeightedEulerCoefficientsVerified":True,
        "allMeanAndHankelVariablesRetained":True,
        "noParameterSpecializationExceptCoefficientFieldPlace":True}
def singular_poly(a,names):
    parts=[]
    for e,c in a:
        mon="*".join(name+("^%d"%k if k!=1 else "") for name,k in zip(names,e) if k)
        parts.append(str(int(c)%PRIME)+("*"+mon if mon else ""))
    return "+".join(parts) if parts else "0"

def engine_script(original,names,weights,source_weights,degree,previous=None):
    n=len(names); m=len(original)
    lines=["// Exact original field-source degree prefix. No point in y,H is chosen.",
        "ring r=127,(%s),wp(%s);" % (",".join(names),",".join(map(str,weights))),
        "short=0; option(redSB); option(redTail);",
        "intvec ww="+",".join(map(str,weights))+";",
        "ideal Original="+",".join(singular_poly(p,names) for p in original)+";"]
    if previous is None:
        lines+=["ideal InBasis=Original;","matrix InSources[%d][%d];"%(m,m)]
        lines+=["InSources[%d,%d]=1;"%(i+1,i+1) for i in range(m)]
    else:
        old=previous["basis"]; lines+=["ideal InBasis="+",".join(singular_poly(p,names) for p in old)+";",
            "matrix InSources[%d][%d];"%(m,len(old))]
        for i,j,p in previous["sources"]:
            lines.append("InSources[%d,%d]=%s;"%(i+1,j+1,singular_poly(p,names)))
    lines += [
        'print("@@PHASE standard-basis-start");',
        "degBound=%d;"%degree,
        "matrix Step; ideal G=liftstd(InBasis,Step);",
        "matrix Sources=InSources*Step;",
        "int ng=size(G);",
        'if (ng==0) { print("@@FAIL empty-basis"); quit; }',
        'if (nrows(Sources)!=%d || ncols(Sources)!=ng) { print("@@FAIL source-matrix-shape"); quit; }'%m,
        "matrix OriginalDifference=matrix(Original)*Sources-matrix(G);",
        "int i; int j; int k;",
        "for (j=1;j<=ng;j++) {",
        '  if (G[j]==0 || OriginalDifference[1,j]!=0) { print("@@FAIL original-source-product"); quit; }',
        "}",
        "for (i=1;i<=%d;i++) {"%m,
        '  if (reduce(Original[i],G)!=0) { print("@@FAIL reverse-original-generator"); quit; }',
        "}",
        'print("@@PHASE all-original-source-identities-verified");',
        "int checkedPairs=0; int productPairs=0; int outsidePairs=0;",
        "intvec ei; intvec ej; int exponent; int pairWeight; int coprime;",
        "poly lm; poly sp; poly remainder;",
        "for (i=1;i<=ng;i++) {",
        "  ei=leadexp(G[i]);",
        "  for (j=i+1;j<=ng;j++) {",
        "    ej=leadexp(G[j]); lm=1; pairWeight=0; coprime=1;",
        "    for (k=1;k<=%d;k++) {"%n,
        "      exponent=ei[k]; if (ej[k]>exponent) { exponent=ej[k]; }",
        "      if (ei[k]>0 && ej[k]>0) { coprime=0; }",
        "      pairWeight=pairWeight+ww[k]*exponent;",
        "      if (exponent>0) { lm=lm*var(k)^exponent; }",
        "    }",
        "    if (pairWeight>%d) { outsidePairs++; }"%degree,
        "    else {",
        "      if (coprime==1) { productPairs++; }",
        "      else {",
        "        sp=(lm/lead(G[i]))*G[i]-(lm/lead(G[j]))*G[j];",
        "        remainder=reduce(sp,G);",
        '        if (remainder!=0) { print("@@FAIL complete-bounded-Buchberger-pair"); quit; }',
        "        checkedPairs++;",
        "      }",
        "    }",
        "  }",
        "}",
        'print("@@PHASE complete-bounded-Buchberger-check-verified");',
        "proc dumpPolynomial(poly value) {",
        "  while (value!=0) {",
        '    print("@@TERM "+string(int(leadcoef(value)))+" "+string(leadexp(value)));',
        "    value=value-lead(value);",
        "  }",
        "}",
        'print("@@BEGIN %d %d %d "+string(ng));'%(PRIME,n,m),
        'print("@@COUNTS "+string(checkedPairs)+" "+string(productPairs)+" "+string(outsidePairs));',
        "for (j=1;j<=ng;j++) {",
        '  print("@@G "+string(j-1)+" "+string(size(G[j])));',
        "  dumpPolynomial(G[j]);",
        '  print("@@ENDPOLY");',
        "}",
        "for (i=1;i<=%d;i++) {"%m,
        "  for (j=1;j<=ng;j++) {",
        "    if (Sources[i,j]!=0) {",
        '      print("@@S "+string(i-1)+" "+string(j-1)+" "+string(size(Sources[i,j])));',
        "      dumpPolynomial(Sources[i,j]);",
        '      print("@@ENDPOLY");',
        "    }",
        "  }",
        "}",
        'print("@@COMPLETE %d");'%degree,
        "quit;"
    ]
    return "\n".join(lines)+"\n"

def parse_engine(log, n, m, weights, source_weights, degree):
    begun=False; complete=False; basis=None; sources=[]; counts=None
    active=None; terms=[]; declared=0; source_keys=set()
    with log.open("r",encoding="utf-8",errors="replace") as f:
        for raw in f:
            s=raw.strip()
            if not s.startswith("@@"): continue
            if s.startswith("@@FAIL"): raise ValueError("Singular verification "+s)
            if s.startswith("@@PHASE"): continue
            bits=s.split()
            if bits[0]=="@@BEGIN":
                need(not begun and len(bits)==5,"unique structured engine header")
                p,nn,mm,ng=map(int,bits[1:])
                need(p==PRIME and nn==n and mm==m and ng>0,"exact field ring and source dimensions")
                basis=[None]*ng; begun=True
            elif bits[0]=="@@COUNTS":
                need(begun and counts is None and len(bits)==4,"complete bounded pair counts")
                counts=list(map(int,bits[1:])); need(min(counts)>=0,"nonnegative pair counts")
            elif bits[0] in ("@@G","@@S"):
                need(begun and active is None,"nonoverlapping whole polynomial records")
                if bits[0]=="@@G":
                    need(len(bits)==3,"basis header"); j,declared=map(int,bits[1:])
                    need(0<=j<len(basis) and basis[j] is None,"unique complete basis column")
                    active=("G",j)
                else:
                    need(len(bits)==4,"source header"); i,j,declared=map(int,bits[1:])
                    need(0<=i<m and 0<=j<len(basis) and (i,j) not in source_keys,"unique original source slot")
                    source_keys.add((i,j)); active=("S",i,j)
                need(declared>0,"only nonzero polynomial records"); terms=[]
            elif bits[0]=="@@TERM":
                need(active is not None,"term inside polynomial record")
                head,co,exps=s.split(None,2); co=int(co)%PRIME
                ee=exps.replace("[","").replace("]","").replace(" ","")
                e=tuple(int(x) for x in ee.split(","))
                need(len(e)==n and all(x>=0 for x in e) and co!=0,"every original monomial and coefficient")
                terms.append([list(e),co])
            elif bits[0]=="@@ENDPOLY":
                need(active is not None and len(terms)==declared,"complete declared polynomial payload")
                dd=record_dict(terms,n); need(len(dd)==declared,"unique monomials in engine polynomial")
                terms=poly_record(dd)
                if active[0]=="G": basis[active[1]]=terms
                else: sources.append([active[1],active[2],terms])
                active=None; terms=[]
            elif bits[0]=="@@COMPLETE":
                need(begun and active is None and int(bits[1])==degree,"complete whole degree identity")
                complete=True
            else: raise ValueError("unknown structured engine marker "+s[:100])
    need(begun and complete and active is None and counts is not None,"completed engine transaction")
    need(all(p for p in basis),"all complete nonzero basis columns")
    degs=[]
    for p in basis:
        ds={sum(a*b for a,b in zip(e,weights)) for e,c in p}
        need(len(ds)==1,"each retained basis polynomial is homogeneous")
        z=next(iter(ds)); need(0<z<=degree,"basis retained only through the paid degree"); degs.append(z)
    for i,j,p in sources:
        need(all(sum(a*b for a,b in zip(e,weights))==degs[j]-source_weights[i] for e,c in p),
            "every original source coefficient has the exact homogeneous weight")
    need(sum(counts)==len(basis)*(len(basis)-1)//2,"all basis pairs classified with none omitted")
    return {"basis":basis,"sources":sources,"basisWeights":degs,
        "verifiedThroughWeight":degree,"explicitBuchbergerPairs":counts[0],
        "coprimeLeadingProductCriterionPairs":counts[1],"higherWeightPairsRetainedForLater":counts[2],
        "allOriginalSourceProductsVerifiedInSingular":True,
        "allOriginalGeneratorsReducedToZero":True,
        "allPairsThroughBoundVerifiedOrCoprimeCriterion":True}

def verify_small_sources(original,data,names):
    ctx=nmod_mpoly_ctx.get(tuple(names),PRIME,"lex")
    orig=[ctx.from_dict(record_dict(p,len(names))) for p in original]
    products=[ctx.from_dict({}) for _ in data["basis"]]
    for i,j,p in data["sources"]: products[j]+=orig[i]*ctx.from_dict(record_dict(p,len(names)))
    need(all(x==ctx.from_dict(record_dict(p,len(names))) for x,p in zip(products,data["basis"])),
        "independent full small-source multiplication")
    return sum(len(x.to_dict()) for x in products)

def pure_parameter_column(data,n):
    for j,p in enumerate(data["basis"]):
        if len(p)==1:
            e,c=p[0]
            if e[-1]>0 and not any(e[:-1]):
                return j,int(e[-1]),int(c)
    return None

def field_positive(model,data,binding):
    chosen=pure_parameter_column(data,18)
    if chosen is None: return None
    j,power,co=chosen; inv=pow(co,-1,PRIME)
    source=[{} for _ in range(18)]
    for i,k,p in data["sources"]:
        if k==j:
            for e,c in p: add_term(source[i],tuple(e[:-1]),c*inv)
    ctx=nmod_mpoly_ctx.get(NAMES[:-1],PRIME,"lex")
    total=ctx.from_dict({}); terms=0
    for original,ss in zip(model["fieldAffineGenerators"],source):
        total+=ctx.from_dict(record_dict(original,17))*ctx.from_dict(ss); terms+=len(ss)
    need(total==ctx.from_dict({(0,)*17:1}),"independent full17-variable field source identity for one")
    return {"binding":binding,"prime":PRIME,"matchedPlace":PLACE,
        "homogeneousBasisColumn":j,"homogeneousParameterPower":power,
        "originalAffineSourceLabels":SOURCE_LABELS[:-1]+["Bell-minus-one"],
        "fullOriginalAffineSources":[poly_record(s) for s in source],
        "sourceTermCounts":[len(s) for s in source],"totalSourceTerms":terms,
        "allOriginal17ParametersRetained":True,"all18FieldOriginalSourceProductsVerified":True,
        "characteristicZeroOriginalIdentityVerified":False,
        "meaning":"Complete source for 1 only over F127 at the checked coefficient-field place; no characteristic-zero conclusion."}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--helper",type=Path,required=True)
    ap.add_argument("--out",type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--seconds",type=float,default=300)
    ap.add_argument("--memory-mib",type=int,default=4096)
    ap.add_argument("--through-degree",type=int,default=9)
    ap.add_argument("--through",choices=("prepared","field"),default="field")
    a=ap.parse_args()
    need(0<a.seconds<=1800 and 512<=a.memory_mib<=8192 and 5<=a.through_degree<=18,"bounded original-source execution")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    a.out.mkdir(parents=True,exist_ok=True); started=time.monotonic(); deadline=started+a.seconds
    source=identity(Path(__file__)); hp=identity(a.helper)
    need(hp["bytes"]==HELPER_BYTES and hp["sha256"]==HELPER_SHA,"exact original full-parameter helper")
    semantic={"format":FORMAT,"sourceSha256":source["sha256"],"helperSha256":HELPER_SHA,
        "prime":PRIME,"matchedPlace":PLACE,"variables":NAMES,"weights":WEIGHTS,
        "originalSourceWeights":SOURCE_WEIGHTS,"algorithm":"weighted-homogeneous-liftstd-plus-all-bounded-pairs"}
    binding=digest(canonical(semantic))
    rec={"format":FORMAT,"binding":binding,"source":source,"status":"running",
        "parameters":{"helper":hp,"seconds":a.seconds,"memoryMiB":a.memory_mib,
            "requestedThroughWeight":a.through_degree,"allSixMeanAndElevenHankelVariablesRetained":True,
            "onlyCoefficientFieldPlaceChosen":True,"characteristicZeroConclusion":False,
            "checkpointBoundary":"after complete original-source products, reverse containment, all bounded pairs and full parsed output",
            "stages":[]}}
    receipt=a.out/"original-full-bell-homogeneous-source-prefix-receipt.json"
    manifest_path=a.out/"manifest.json"; manifest={"format":FORMAT+"-manifest","binding":binding,"completedDegrees":[]}
    child=None
    def save():
        rec["elapsedSeconds"]=time.monotonic()-started
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        json_save(receipt,rec)
    def tick():
        if time.monotonic()>=deadline-2: raise Budget("whole-degree execution budget")
    def signum_stop(signum,frame): raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,signum_stop); signal.signal(signal.SIGINT,signum_stop)
    def run_engine(label,original,names,weights,source_weights,degree,previous):
        nonlocal child
        tick(); script=a.out/(label+".sing"); log=a.out/(label+".log")
        atomic(script,engine_script(original,names,weights,source_weights,degree,previous).encode("ascii"))
        stage={"name":label,"status":"running","degree":degree,"script":identity(script)}
        rec["parameters"]["stages"].append(stage); save(); begin=time.monotonic()
        try:
            with log.open("wb") as f:
                child=subprocess.Popen([str(engine),"-q",str(script)],stdout=f,stderr=subprocess.STDOUT)
                last_report=time.monotonic()
                while child.poll() is None:
                    tick()
                    if time.monotonic()-last_report>=30:
                        print(json.dumps({"phase":label,"status":"running","elapsedSeconds":time.monotonic()-begin,
                            "lastCompleteWeight":rec["parameters"].get("lastCompleteWeight",0)},separators=(",",":")),flush=True)
                        last_report=time.monotonic()
                    time.sleep(.2)
                code=child.returncode; child=None
            stage.update(exitCode=code,elapsedSeconds=time.monotonic()-begin,log=identity(log))
            need(code==0,"Singular process completed successfully")
            data=parse_engine(log,len(names),len(original),weights,source_weights,degree)
            stage.update(status="verified-whole-degree",basisColumns=len(data["basis"]),
                sourceNonzeroSlots=len(data["sources"]),sourceTerms=sum(len(z[2]) for z in data["sources"]),
                explicitPairs=data["explicitBuchbergerPairs"],productCriterionPairs=data["coprimeLeadingProductCriterionPairs"])
            save(); return data
        except BaseException:
            if child is not None and child.poll() is None:
                child.terminate()
                try: child.wait(timeout=5)
                except subprocess.TimeoutExpired: child.kill(); child.wait()
            child=None
            stage.update(status="unfinished-whole-degree",elapsedSeconds=time.monotonic()-begin)
            if log.exists():
                stage["log"]=identity(log)
                with log.open("rb") as f:
                    f.seek(max(0,log.stat().st_size-6000)); stage["logTail"]=f.read().decode("utf-8",errors="replace")
            save(); raise
    code=1
    try:
        save()
        if manifest_path.exists():
            manifest=json.loads(manifest_path.read_bytes())
            need(manifest.get("format")==FORMAT+"-manifest" and manifest.get("binding")==binding,"same original-source checkpoint binding")
        if "model" in manifest:
            model=gz_load(a.out,manifest["model"])["data"]
            need(model["all17OriginalGradientPolynomialsVerified"] and model["allMeanAndHankelVariablesRetained"],"paid complete original model")
            rec["parameters"]["modelReused"]=True
        else:
            tick(); m=module(a.helper); begin=time.monotonic(); model=prepare(m)
            desc=gz_save(a.out/"complete-original-full-bell-saturation-model.json.gz",
                {"format":FORMAT+"-model","binding":binding,"data":model})
            manifest["model"]=desc; json_save(manifest_path,manifest)
            rec["parameters"]["modelPreparationSeconds"]=time.monotonic()-begin
        rec["parameters"]["model"]=manifest["model"]
        rec["parameters"]["place"]=model["place"]
        rec["parameters"]["originalGradientTermCounts"]=[len(x) for x in model["originalSeventeenGradients"]]
        rec["parameters"]["all17OriginalPolynomialsAndEulerVerified"]=True; save()
        if a.through=="prepared":
            rec["status"]="completed-prefix"; rec["parameters"]["outcome"]="complete-original-model-prepared"; code=0
        else:
            engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(Path(a.singular).resolve())
            need(engine is not None,"Singular executable must be installed by the external workflow")
            engine=Path(engine).resolve()
            v=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                timeout=min(10,max(1,deadline-time.monotonic()-2)))
            need(v.returncode==0,"actual Singular version probe")
            rec["parameters"]["engine"]={"binary":identity(engine),"version":v.stdout.decode("utf-8",errors="replace")[:12000],
                "arguments":["-q"],"libraryStage":"only standard liftstd, reduce, leading monomials and polynomial identities"}
            if "selfTest" not in manifest:
                tiny=[[[[2,0],1],[[0,2],PRIME-1]],[[[1,1],1]]]
                td2=run_engine("independent-source-selftest-degree2",tiny,("xx","tt"),(1,1),(2,2),2,None)
                need(pure_parameter_column(td2,2) is None,"degree2 bound must not produce t^3 or another pure t power")
                verify_small_sources(tiny,td2,("xx","tt"))
                td=run_engine("independent-source-selftest-resume-degree3",tiny,("xx","tt"),(1,1),(2,2),3,td2)
                tc=pure_parameter_column(td,2); need(tc is not None and tc[1]==3,"continued degree3 must produce nontrivial original t^3 source")
                verify_small_sources(tiny,td,("xx","tt"))
                manifest["selfTest"]=gz_save(a.out/"complete-independent-original-source-selftest.json.gz",
                    {"format":FORMAT+"-selftest","binding":binding,"degree2":td2,"degree3":td,
                     "degree2HasNoPureParameterPower":True,"degree3ResumedWithSameOriginalSources":True,
                     "allIndependentFlintOriginalProductsVerified":True})
                json_save(manifest_path,manifest)
            else: gz_load(a.out,manifest["selfTest"])
            rec["parameters"]["selfTest"]=manifest["selfTest"]
            previous=None; last=4
            for item in manifest["completedDegrees"]:
                need(item["degree"]==last+1,"consecutive complete source degree checkpoints")
                stored=gz_load(a.out,item["output"]); need(stored["binding"]==binding,"same complete-degree payload binding")
                previous=stored["data"]; need(previous["verifiedThroughWeight"]==item["degree"],"true completed degree")
                last=item["degree"]
            rec["parameters"]["lastCompleteWeight"]=last if previous is not None else 0
            if "positiveCandidate" in manifest:
                candidate=gz_load(a.out,manifest["positiveCandidate"])
                need(candidate["binding"]==binding and candidate["all18FieldOriginalSourceProductsVerified"],"complete previous field source")
                rec["parameters"]["positiveCandidate"]=manifest["positiveCandidate"]
                rec["parameters"]["outcome"]="verified-field-source-for-one-awaiting-characteristic-zero-lift"
                rec["status"]="completed"; code=0
            else:
                for degree in range(last+1,a.through_degree+1):
                    data=run_engine("complete-original-weight-%02d"%degree,
                        model["fieldHomogeneousGenerators"],NAMES,WEIGHTS,SOURCE_WEIGHTS,degree,previous)
                    desc=gz_save(a.out/("complete-original-source-weight-%02d.json.gz"%degree),
                        {"format":FORMAT+"-degree","binding":binding,"data":data})
                    manifest["completedDegrees"].append({"degree":degree,"output":desc})
                    previous=data; rec["parameters"]["lastCompleteWeight"]=degree
                    json_save(manifest_path,manifest); save()
                    print(json.dumps({"phase":"complete-original-whole-degree","degree":degree,
                        "basisColumns":len(data["basis"]),"sourceTerms":sum(len(x[2]) for x in data["sources"]),
                        "allOriginalSourceIdentitiesVerified":True,"allBoundedPairsVerified":True},separators=(",",":")),flush=True)
                    candidate=field_positive(model,data,binding)
                    if candidate is not None:
                        cd=gz_save(a.out/"complete-original-affine-field-source-for-one.json.gz",candidate)
                        manifest["positiveCandidate"]=cd; json_save(manifest_path,manifest)
                        rec["parameters"]["positiveCandidate"]=cd
                        rec["parameters"]["candidateSupportTerms"]=candidate["totalSourceTerms"]
                        rec["parameters"]["candidateSourceTermCounts"]=candidate["sourceTermCounts"]
                        rec["parameters"]["outcome"]="verified-field-source-for-one-awaiting-characteristic-zero-lift"
                        rec["status"]="completed"; code=0; break
                else:
                    rec["parameters"]["outcome"]="complete-bounded-field-prefix-without-positive-source"
                    rec["parameters"]["notAnIdealNonmembershipOrCharacteristicZeroConclusion"]=True
                    rec["status"]="completed-prefix"; code=0
            rec["parameters"]["completeDegreeOutputs"]=manifest["completedDegrees"]
        rec["parameters"]["manifest"]=identity(manifest_path); save()
    except Budget as e:
        rec["status"]="budget-checkpoint"; rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        rec["parameters"]["noMathematicalNegativeConclusion"]=True; code=75
    except BaseException as e:
        rec["status"]="failed"; rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}; code=1
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try: child.wait(timeout=5)
            except subprocess.TimeoutExpired: child.kill(); child.wait()
        if manifest_path.exists(): rec["parameters"]["manifest"]=identity(manifest_path)
        save()
    print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
    return code
if __name__=="__main__": raise SystemExit(main())
