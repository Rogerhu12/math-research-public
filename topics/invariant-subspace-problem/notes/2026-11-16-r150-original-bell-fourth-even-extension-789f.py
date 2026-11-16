#!/usr/bin/env python3
"""Find original Bell fourth-power sources through an even finite-free extension.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The ideal has all seventeen original gradients and all seventeen variables.
Only target sources are extracted. Neither a nonzero reduction nor a budget
exit is a nonmembership certificate. Exact Q multiplication is a separate gate.
All polynomial arrays and Singular SSI checkpoints are temporary only.
"""
from __future__ import annotations
import argparse,gc,hashlib,importlib.util,json,re,resource,shutil,signal,subprocess,time
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_mpoly_ctx

FORMAT="r150-original-bell-fourth-even-extension-three-rational-targets-v1"
MODEL_BYTES=31156
MODEL_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
HELPER_BYTES=16964
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
AUDIT_BYTES=8329
AUDIT_SHA="33560119cb8f19902f323b5a1f5fb5a3bb59d38aad6d55108950107bd545579e"
AUDIT_FORMAT="r150-original-bell-cube-complete-prime7-coefficient-audit-v1"
AUDIT_BINDING="4baed1013b72717e2773607c308a3f534b029c92f35592dcb6c5ff1025587339"
AUDIT_LOGICAL_SHA="df9fb9657926a52a4c3c1a895a0ba5aa34f2d5f537d747d7f07e00d42f81bdfa"
P=7
WEIGHTS=(1,)*6+(2,)*11
SOURCE_WEIGHTS=(4,)*11+(5,)*6
ALGORITHM="original17-square-extension-equal-weight-slimgb12-target-only17by3-lift-even-projection"

class Budget(Exception):pass
def need(ok,message):
    if not ok:raise ValueError(message)
def module(p,name):
    sp=importlib.util.spec_from_file_location(name,p)
    z=importlib.util.module_from_spec(sp);sp.loader.exec_module(z);return z
def raw_identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def semantic(own_sha):
    return {"format":FORMAT,"sourceSha256":own_sha,"modelDriverSHA256":MODEL_SHA,
        "helperSHA256":HELPER_SHA,"auditDriverSHA256":AUDIT_SHA,
        "auditBinding":AUDIT_BINDING,"auditModelLogicalSHA256":AUDIT_LOGICAL_SHA,
        "prime":P,"originalVariableCount":17,"originalGradientCount":17,"targetCount":3,
        "weight":12,"extendedOrdinaryDegree":12,"extension":"H_i=z_i^2",
        "coefficientBasis":["1","d","d^2"],"algorithm":ALGORITHM}
def ss(p,mode=""):
    s=str(p)
    need(not any(x in s for x in ('"',"\\","\r","\n")),"literal safe Singular temporary path")
    return '"'+mode+s+'"'
def read_markers(p):
    markers=[];bad=[]
    with p.open("r",encoding="utf-8",errors="replace") as f:
        for line in f:
            s=line.strip()
            if s.startswith("@@"): markers.append(s)
            if s.startswith("@@FAIL") or s.startswith("?"): bad.append(s[:500])
    need(len(markers)<=10000 and len(bad)<=10000,"bounded diagnostic marker count")
    return markers,bad
def marker_once(markers,prefix,required=True):
    z=[x for x in markers if x.startswith(prefix)]
    need(len(z)<=1,"unique stage marker "+prefix)
    if required: need(len(z)==1,"complete stage marker "+prefix)
    return z[0] if z else None
def parse_fast_polynomial(p,names):
    """Parse only Singular short=0 expanded prime-field monomials, not code."""
    text="".join(p.read_text(encoding="ascii").split())
    if text=="0": return {}
    need(text and text[0] not in "*^","nonempty expanded polynomial")
    pieces=re.findall(r"[+-]?[^+-]+",text)
    need("".join(pieces)==text,"complete expanded polynomial tokenization")
    where={s:i for i,s in enumerate(names)};out={}
    for term in pieces:
        coefficient=1
        if term[0] in "+-":
            if term[0]=="-": coefficient=-1
            term=term[1:]
        need(term,"nonempty signed monomial")
        exponent=[0]*len(names)
        for factor in term.split("*"):
            if factor.isdigit():
                coefficient=coefficient*int(factor)%P;continue
            z=factor.split("^")
            need(len(z)<=2 and z[0] in where,"literal variable in expanded monomial")
            k=1 if len(z)==1 else int(z[1])
            need(k>=0 and (len(z)==1 or z[1].isdigit()),"nonnegative literal exponent")
            exponent[where[z[0]]]+=k
        e=tuple(exponent);out[e]=(out.get(e,0)+coefficient)%P
    return {e:c for e,c in out.items() if c}
def q7(q):
    q=fmpq(q);den=int(q.denom())%P
    need(den!=0,"each actual rational coefficient is 7-integral")
    return int(q.numer())%P*pow(den,-1,P)%P
def record7(d):
    return [[list(e),int(c)] for e,c in sorted(d.items()) if int(c)%P]
def dict7(records,n=17):
    out={}
    for ee,c in records:
        e=tuple(ee)
        need(len(e)==n and all(type(x) is int and x>=0 for x in e) and e not in out and
             type(c) is int and 1<=c<P,"distinct canonical nonzero prime7 original monomial")
        out[e]=c
    return out
def extend(e):
    return tuple(e[:6])+tuple(2*x for x in e[6:])
def descend(e):
    need(all(x%2==0 for x in e[6:]),"all eleven square-variable exponents even")
    return tuple(e[:6])+tuple(x//2 for x in e[6:])
def singular7(records,names,even=True):
    parts=[]
    for ee,c in records:
        e=extend(ee) if even else tuple(ee)
        need(len(e)==len(names) and 0<int(c)<P,"literal prime7 Singular input")
        mon="*".join(x+("^%d"%k if k!=1 else "") for x,k in zip(names,e) if k)
        parts.append(str(c)+("*"+mon if mon else ""))
    return "+".join(parts) if parts else "0"
def qpoly(m,p):
    d={}
    for ee,c in p:
        e=tuple(ee);q=fmpq(c)
        need(len(e)==17 and e not in d and q!=0,"all original rational monomials")
        d[e]=q
    return m.CTX.from_dict(d)
def prepare(fd,m,a,state,binding,checkpoint,tick):
    audit=json.loads(a.audit_receipt.read_bytes())
    need(audit["format"]==AUDIT_FORMAT and audit["binding"]==AUDIT_BINDING and
         audit["status"]=="completed","complete same original prime7 admission")
    par=audit["parameters"]
    need(par["prime7CompleteOriginalModelAdmitted"] and par["allOriginalCoefficients7Integral"] and
         par["allThreeF7CoefficientAlgebraCubeProductsVerified"] and
         par["allCompleteOriginalRationalProductsVerified"],"all paid original model and field gates")
    need(par["temporaryCompleteModel"]["logicalSha256"]==AUDIT_LOGICAL_SHA,
         "same full original rational model logical SHA")
    if "baseModel" not in state:
        tick();data=fd.gz_load(a.audit_out,par["temporaryCompleteModel"])
        need(data["format"]==AUDIT_FORMAT+"-complete-data" and data["binding"]==AUDIT_BINDING and
             data["field7ModelAdmitted"],"actual complete original model payload")
        old=data["completeOriginalRationalModel"];field=data["allField7Polynomials"]
        need(old["matchedCubic"]==m.MATCHED and old["all17OriginalGradientPolynomialsVerified"] and
             old["allWeightedEulerCoefficientsVerified"],"full original physical model identities")
        F=m.Field();table=[]
        for i in range(3):
            one=[]
            for j in range(3):
                z=F.mul(fmpq_poly([0]*i+[1]),fmpq_poly([0]*j+[1]))
                one.append([str(z[k]) for k in range(3)])
            table.append(one)
        core={"originalVariableNames":old["variableNames"][:-1],
            "extendedVariableNames":old["variableNames"][:6]+["z%d"%i for i in range(11)],
            "originalSeventeenGradients":old["originalSeventeenGradients"],
            "sourceLabels":old["sourceLabels"][:17],"sourceWeights":list(SOURCE_WEIGHTS),
            "BellFieldComponents":old["BellFieldComponents"],
            "naturalCubeRationalComponents":old["naturalCubeRationalComponents"],
            "fieldOriginalSeventeenGenerators":field["gradients"],
            "fieldBellComponents":field["bellComponents"],
            "fieldCubeComponents":field["cubeComponents"],
            "matchedCubic":old["matchedCubic"],"J3Determinant":old["J3Determinant"],
            "coefficientMultiplicationTable":table,"parentAuditBinding":AUDIT_BINDING,
            "all17OriginalGradientPolynomialsVerified":True,
            "allWeightedEulerCoefficientsVerified":True,
            "allOriginalMeanAndHankelVariablesRetained":True}
        del data,old,field
        state["baseModel"]=fd.gz_save(a.out/"complete-original-even-extension-base-model.json.gz",
            {"format":FORMAT+"-base-model","binding":binding,"data":core})
        checkpoint();gc.collect()
    packed=fd.gz_load(a.out,state["baseModel"])
    need(packed["format"]==FORMAT+"-base-model" and packed["binding"]==binding,"whole original base-model")
    core=packed["data"];del packed
    need(core["matchedCubic"]==m.MATCHED and core["parentAuditBinding"]==AUDIT_BINDING and
         len(core["originalVariableNames"])==len(core["extendedVariableNames"])==17,
         "same original coordinate and coefficient-field dictionaries")
    for i,p in enumerate(core["fieldOriginalSeventeenGenerators"]):
        need(all(sum(x*w for x,w in zip(e,WEIGHTS))==SOURCE_WEIGHTS[i] for e in dict7(p)),
             "each original generator is homogeneous of its actual weight")
    need(len(core["fieldOriginalSeventeenGenerators"])==17,"all seventeen original gradients")
    state.setdefault("targetComponents",[])
    need([z["component"] for z in state["targetComponents"]]==list(range(len(state["targetComponents"]))) and
         len(state["targetComponents"])<=3,"complete rational target component prefix")
    if len(state["targetComponents"])<3:
        tick()
        cube=[qpoly(m,p) for p in core["naturalCubeRationalComponents"]]
        bell=[qpoly(m,p) for p in core["BellFieldComponents"]]
        table=core["coefficientMultiplicationTable"]
        ctx=nmod_mpoly_ctx.get(tuple(core["originalVariableNames"]),P,"lex")
        fc=[ctx.from_dict(dict7(p)) for p in core["fieldCubeComponents"]]
        fb=[ctx.from_dict(dict7(p)) for p in core["fieldBellComponents"]]
        conv=[ctx.from_dict({}) for _ in range(5)]
        for i in range(3):
            for j in range(3):conv[i+j]+=fc[i]*fb[j];tick()
        cubic=list(map(int,core["matchedCubic"]));need(cubic[-1]%P!=0,"original field leading coefficient 7-unit")
        f=[c%P*pow(cubic[-1]%P,-1,P)%P for c in cubic[:3]]
        for d in range(4,2,-1):
            z=conv[d]
            for k in range(3):conv[d-3+k]-=f[k]*z
            conv[d]=ctx.from_dict({})
        del fc,fb;gc.collect()
        for k in range(len(state["targetComponents"]),3):
            tick();started=time.monotonic();target=m.ZERO
            for i in range(3):
                for j in range(3):
                    c=fmpq(table[i][j][k])
                    if c:target+=(cube[i]*bell[j])*c;tick()
            m.weighted(target,12)
            rational=m.pv(target);reduced={}
            for e,c in rational:
                v=q7(c)
                if v:reduced[tuple(e)]=v
            need(ctx.from_dict(reduced)==conv[k],"every coefficient of independent prime7 fourth component "+str(k))
            field=record7(reduced)
            qdesc=fd.gz_save(a.out/("original-rational-fourth-component-%d.json.gz"%k),
                {"format":FORMAT+"-rational-fourth","binding":binding,"component":k,
                 "targetWeight":12,"records":rational,"allCoefficients7Integral":True,
                 "identity":"coefficient of d^k in original_Bell^4 modulo the original matched cubic"})
            fdesc=fd.gz_save(a.out/("original-field7-fourth-component-%d.json.gz"%k),
                {"format":FORMAT+"-field-fourth","binding":binding,"component":k,"targetWeight":12,
                 "records":field,"allIndependentFieldProductCoordinatesVerified":True})
            state["targetComponents"].append({"component":k,"rational":qdesc,"field":fdesc,
                "rationalTerms":len(rational),"fieldTerms":len(field),
                "everyCoefficient7Integral":True,"fullIndependentPrime7ProductVerified":True})
            checkpoint()
            print(json.dumps({"phase":"complete-original-fourth-component","component":k,
                "rationalTerms":len(rational),"fieldTerms":len(field),
                "elapsedSeconds":time.monotonic()-started,
                "peakRssKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},separators=(",",":")),flush=True)
            del target,rational,reduced,field;gc.collect()
        del cube,bell,conv;gc.collect()
    targets=[]
    for k,desc in enumerate(state["targetComponents"]):
        need(desc["component"]==k and desc["everyCoefficient7Integral"] and
             desc["fullIndependentPrime7ProductVerified"],"all complete new rational target gates")
        # Only field coefficients are loaded for the subsequent native discovery.
        qpath=a.out/desc["rational"]["path"]
        need(raw_identity(qpath)=={x:desc["rational"][x] for x in ("path","bytes","sha256")},
             "entire saved rational target SHA")
        field=fd.gz_load(a.out,desc["field"])
        need(field["format"]==FORMAT+"-field-fourth" and field["binding"]==binding and
             field["component"]==k and field["targetWeight"]==12 and
             len(field["records"])==desc["fieldTerms"],"whole original fourth field component")
        need(all(sum(x*w for x,w in zip(e,WEIGHTS))==12 for e in dict7(field["records"])),
             "all original fourth target weights")
        targets.append(field["records"])
    core["fieldNaturalFourthRationalComponents"]=targets
    return core
def ring(fd,model):
    names=tuple(model["extendedVariableNames"])
    return ["ring r=7,("+",".join(names)+"),dp;",
        "short=0; option(redSB); option(redTail);",
        "ideal Original="+",".join(singular7(p,names) for p in model["fieldOriginalSeventeenGenerators"])+";",
        "ideal Targets="+",".join(singular7(p,names) for p in model["fieldNaturalFourthRationalComponents"])+";"]
def selftest_script(out):
    g=out/"selftest-degree2.ssi";s=out/"selftest-single-source.ssi"
    lines=[
        "ring r=7,(x,tt),dp; short=0; option(redSB); option(redTail);",
        "ideal Original=x^2-tt^2,x*tt;",
        "int i; int k; int power; int pure; int found; intvec ex;",
        "degBound=2; ideal G2=slimgb(Original);",
        "for(i=1;i<=ncols(G2);i++){",
        "if(G2[i]!=0){",
        "poly z=G2[i]; while(z!=0){ex=leadexp(z);",
        'if(ex[1]+ex[2]>2){print("@@FAIL degree2-bound");quit;} z=z-lead(z);}',
        "if(size(G2[i])==1){ex=leadexp(G2[i]);",
        'if(ex[1]==0){print("@@FAIL degree2-pure");quit;}} }}',
        "write("+ss(g,"ssi:w ")+",G2); def G2copy=read("+ss(g,"ssi:r ")+");",
        'if(ncols(G2copy)!=ncols(G2)){print("@@FAIL ssi-shape");quit;}',
        "for(i=1;i<=ncols(G2);i++){",
        'if(G2[i]!=G2copy[i]){print("@@FAIL ssi-polynomial");quit;}}',
        'print("@@SELFTEST-DEGREE2 "+string(ncols(G2)));',
        "degBound=3; ideal G3=slimgb(G2copy+Original); found=0;",
        "for(i=1;i<=ncols(G3);i++){if(size(G3[i])==1){ex=leadexp(G3[i]);",
        "if(ex[1]==0 && ex[2]==3){found=1;}}}",
        'if(found!=1){print("@@FAIL continued-degree3");quit;}',
        'print("@@SELFTEST-DEGREE3 "+string(ncols(G3)));',
        "degBound=0; ideal Target=tt^3; matrix Units;",
        'matrix Source=lift(Original,Target,Units,"slimgb");',
        'if(nrows(Source)!=2 || ncols(Source)!=1){print("@@FAIL lift-shape");quit;}',
        'if(nrows(Units)!=1 || ncols(Units)!=1 || Units[1,1]!=1){print("@@FAIL lift-unit");quit;}',
        "matrix Difference=matrix(Original)*Source-matrix(Target);",
        'if(Difference[1,1]!=0){print("@@FAIL lift-original-product");quit;}',
        "write("+ss(s,"ssi:w ")+",Source); def SourceCopy=read("+ss(s,"ssi:r ")+");",
        'if(nrows(SourceCopy)!=2 || ncols(SourceCopy)!=1){print("@@FAIL source-ssi-shape");quit;}',
        'for(i=1;i<=2;i++){if(Source[i,1]!=SourceCopy[i,1]){print("@@FAIL source-ssi-product");quit;}}',
        "write("+ss(out/"selftest-source-0.txt",":w ")+",Source[1,1]);",
        "write("+ss(out/"selftest-source-1.txt",":w ")+",Source[2,1]);",
        "write("+ss(out/"selftest-parser.txt",":w ")+",-5*x^4+3*x*tt^3+2);",
        'print("@@SELFTEST-COMPLETE");',
        "degBound=0; ideal Targets3=tt^3,x*tt^2,x^2*tt; matrix Units3;",
        'matrix Sources3=lift(Original,Targets3,Units3,"slimgb");',
        'if(nrows(Sources3)!=2 || ncols(Sources3)!=3){print("@@FAIL three-source-shape");quit;}',
        'if(nrows(Units3)!=3 || ncols(Units3)!=3){print("@@FAIL three-unit-shape");quit;}',
        "int j; matrix Diff3=matrix(Original)*Sources3-matrix(Targets3);",
        "for(i=1;i<=3;i++){",
        'if(Diff3[1,i]!=0){print("@@FAIL three-original-product");quit;}',
        'for(j=1;j<=3;j++){if(Units3[i,j]!=(i==j)){print("@@FAIL three-unit-entry");quit;}}}',
        "write("+ss(out/"selftest-three-source.ssi","ssi:w ")+",Sources3);",
        "def Copy3=read("+ss(out/"selftest-three-source.ssi","ssi:r ")+");",
        'if(nrows(Copy3)!=2 || ncols(Copy3)!=3){print("@@FAIL three-source-SSI-shape");quit;}',
        "for(i=1;i<=2;i++){for(j=1;j<=3;j++){",
        'if(Copy3[i,j]!=Sources3[i,j]){print("@@FAIL all6-source-SSI");quit;}}}',
    ]
    for k in range(3):
        for i in range(2):
            lines+=["write("+ss(out/("selftest-three-%d-%d.txt"%(k,i)),":w ")+",Sources3[%d,%d]);"%(i+1,k+1)]
    lines+=['print("@@THREE-TARGET-SELFTEST-COMPLETE");quit;']
    return "\n".join(lines)+"\n"
def discovery_script(fd,model,out):
    gp=out/"whole-original17-discovery-basis.ssi"
    lines=ring(fd,model)+[
        'print("@@SLIMGB17-START 12");',"degBound=12; ideal G=slimgb(Original);",
        'print("@@SLIMGB17-RETURN "+string(ncols(G)));',
        "write("+ss(gp,"ssi:w ")+",G);",
        "def Copy=read("+ss(gp,"ssi:r ")+");",
        'if(ncols(Copy)!=ncols(G)){print("@@FAIL original17-basis-copy-shape");quit;}',
        "int i; int j; int hd; int td; intvec ex; poly term;",
        "for(i=1;i<=ncols(G);i++){",
        'if(Copy[i]!=G[i]){print("@@FAIL original17-basis-copy-product");quit;}',
        "if(G[i]!=0){hd=deg(G[i]);",
        'if(hd>12){print("@@FAIL returned-degree-bound");quit;}',
        "term=G[i]; while(term!=0){ex=leadexp(term);td=0;",
        "for(j=1;j<=17;j++){td=td+ex[j];",
        'if(j>=7 && (ex[j]%2)!=0){print("@@FAIL returned-not-even");quit;}}',
        'if(td!=hd){print("@@FAIL returned-not-homogeneous");quit;}',
        "term=term-lead(term);}}}",
        'print("@@SLIMGB17-SSI-ROUNDTRIP");',
        'print("@@SLIMGB17-ALL-MONOMIALS-HOMOGENEOUS-EVEN-DEGREE12");',
        "degBound=0; int nonzero=0;",
    ]
    for k in range(3):
        lines+=["poly residual%d=reduce(Targets[%d],G);"%(k,k+1),
            "write("+ss(out/("discovery-target-residual-%d.txt"%k),":w ")+",residual%d);"%k,
            "if(residual%d!=0){nonzero++;}"%k,
            'print("@@TARGET-REDUCTION '+str(k)+' "+string(size(residual%d)));'%k]
    lines+=['print("@@SLIMGB17-END "+string(ncols(G))+" "+string(nonzero));',"quit;"]
    return "\n".join(lines)+"\n"
def lift_script(fd,model,out):
    sp=out/"whole-original17-three-target-sources.ssi"
    return "\n".join(ring(fd,model)+[
        "degBound=0; matrix Units;",
        'print("@@THREE-ORIGINAL-LIFT-START");',
        'matrix Sources=lift(Original,Targets,Units,"slimgb");',
        'print("@@THREE-ORIGINAL-LIFT-RETURN");',
        'if(nrows(Sources)!=17 || ncols(Sources)!=3){print("@@FAIL full17-by3-source-shape");quit;}',
        'if(nrows(Units)!=3 || ncols(Units)!=3){print("@@FAIL full3-unit-shape");quit;}',
        "int i; int j; for(i=1;i<=3;i++){for(j=1;j<=3;j++){",
        'if(Units[i,j]!=(i==j)){print("@@FAIL full3-unit-entry");quit;}}}',
        "write("+ss(sp,"ssi:w ")+",Sources);",
        "def Copy=read("+ss(sp,"ssi:r ")+");",
        'if(nrows(Copy)!=17 || ncols(Copy)!=3){print("@@FAIL source-copy-shape");quit;}',
        "for(i=1;i<=17;i++){for(j=1;j<=3;j++){",
        'if(Copy[i,j]!=Sources[i,j]){print("@@FAIL whole51-source-copy-product");quit;}}}',
        'print("@@THREE-ORIGINAL-LIFT-CANDIDATE-END");',"quit;"])+"\n"
def verify_script(fd,model,out,first,product_paid):
    lines=ring(fd,model)+[
        "degBound=0;",
        "def Sources=read("+ss(out/"whole-original17-three-target-sources.ssi","ssi:r ")+");",
        'if(nrows(Sources)!=17 || ncols(Sources)!=3){print("@@FAIL verify17-by3-shape");quit;}']
    if not product_paid:
        lines+=["matrix Difference=matrix(Original)*Sources-matrix(Targets);","int i;",
            "for(i=1;i<=3;i++){",
            'if(Difference[1,i]!=0){print("@@FAIL three-full-original-products");quit;}}',
            'print("@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED");']
    for index in range(first,51):
        k,i=divmod(index,17)
        lines+=["write("+ss(out/("source-%02d.txt"%index),":w ")+",Sources[%d,%d]);"%(i+1,k+1),
            'print("@@SOURCE-TEXT '+str(index)+' "+string(size(Sources[%d,%d])));'%(i+1,k+1)]
    lines+=['print("@@ALL-51-SOURCE-TEXTS-END");',"quit;"]
    return "\n".join(lines)+"\n"
def even_projection_fixture():
    c=nmod_mpoly_ctx.get(("h","k"),P,"lex")
    z=nmod_mpoly_ctx.get(("z","v"),P,"lex")
    original=[c.from_dict({(1,0):1}),c.from_dict({(2,0):1})]
    extended=[z.from_dict({(2,0):1}),z.from_dict({(4,0):1})]
    src=[{(3,0):1,(2,0):1},{(1,0):6,(0,0):1}]
    need(sum((extended[i]*z.from_dict(src[i]) for i in range(2)),z.from_dict({}))==
         z.from_dict({(4,0):2}),"tiny odd source cancellation before even projection")
    even=[{(e[0]//2,e[1]//2):v for e,v in p.items() if all(t%2==0 for t in e)} for p in src]
    need(sum((original[i]*c.from_dict(even[i]) for i in range(2)),c.from_dict({}))==
         c.from_dict({(2,0):2}),"tiny literal original source identity after even projection")
    e=(1,0,0,0,0,0,2,1,0,0,0,0,0,0,0,0,0)
    need(descend(extend(e))==e and sum(extend(e))==sum(x*w for x,w in zip(e,WEIGHTS)),
         "literal17 exponent and weighted-degree transport")
    return {"oddTermsCancelInExtendedRing":True,"evenProjectionGivesOriginalSource":True,
            "all17ExponentAndDegreeCoordinatesPreserved":True}
def main():
    ap=argparse.ArgumentParser()
    for name in ("model-driver","helper","audit-driver","audit-receipt","audit-out","out"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--singular",default="Singular")
    ap.add_argument("--through",choices=("prepare","final"),default="final")
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    a=ap.parse_args()
    need(0<a.seconds<=3600 and 512<=a.memory_mib<=8192,"bounded field resources")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    pins={}
    for name,p,size,digest in [
        ("model",a.model_driver,MODEL_BYTES,MODEL_SHA),("helper",a.helper,HELPER_BYTES,HELPER_SHA),
        ("audit",a.audit_driver,AUDIT_BYTES,AUDIT_SHA)]:
        pins[name]=raw_identity(p)
        need(pins[name]["bytes"]==size and pins[name]["sha256"]==digest,"exact frozen "+name)
    fd=module(a.model_driver,"r150_even_original_model")
    own=raw_identity(Path(__file__));sem=semantic(own["sha256"]);binding=fd.digest(fd.canonical(sem))
    a.out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();deadline=start+a.seconds;child=None
    receipt=a.out/"original-bell-fourth-even-extension-receipt.json"
    manifest=a.out/"manifest.json"
    state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,
        "generation":0,"sourceTexts":[],"verifiedFieldComponents":[],"targetComponents":[]}
    rec={"format":FORMAT,"binding":binding,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"pinnedSources":pins,
        "allOriginal17VariablesAnd17GradientsRetained":True,"targetCount":3,"targetWeight":12,
        "completeWeightTwelveMatrixConstructed":False,
        "sourceExtensionRank":2048,"squareVariableCount":11,"boundedStandardBasisCompletenessClaimed":False,
        "characteristicZeroConclusion":False,"stages":[]}}
    def save():
        rec["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        rec["parameters"]["wholePhaseState"]=state
        fd.json_save(receipt,rec)
    def checkpoint():
        fd.json_save(manifest,state);rec["parameters"]["manifest"]=fd.identity(manifest);save()
    def tick():
        if time.monotonic()>=deadline-8:raise Budget("three-target whole-phase budget")
    def stop(signum,frame):raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def checked(desc):
        p=a.out/desc["path"];need(fd.identity(p)==desc,"whole temporary file SHA");return p
    def run_stage(name,script):
        nonlocal child
        tick();state["generation"]+=1;checkpoint();g=state["generation"]
        sp=a.out/("%04d-%s.sing"%(g,name));lp=a.out/("%04d-%s.log"%(g,name))
        fd.atomic(sp,script.encode("ascii"));stage={"name":name,"script":fd.identity(sp),"status":"running"}
        rec["parameters"]["stages"].append(stage);save();begin=time.monotonic();budget=False
        try:
            with lp.open("wb") as f:
                child=subprocess.Popen([str(engine),"-q",str(sp)],stdout=f,stderr=subprocess.STDOUT)
                report=time.monotonic()
                while child.poll() is None:
                    tick()
                    if time.monotonic()-report>=30:
                        print(json.dumps({"phase":name,"elapsedSeconds":time.monotonic()-begin,
                            "wholeDiscoverySaved":"discovery" in state,
                            "wholeThreeSourcesSaved":"threeSources" in state},separators=(",",":")),flush=True)
                        report=time.monotonic()
                    time.sleep(.2)
                rc=child.returncode;child=None
        except Budget:
            budget=True
            if child is not None and child.poll() is None:
                child.terminate()
                try:child.wait(timeout=5)
                except subprocess.TimeoutExpired:child.kill();child.wait()
            child=None;rc=75
        markers,bad=read_markers(lp)
        with lp.open("rb") as f:
            f.seek(max(0,lp.stat().st_size-4096));tail=f.read().decode("utf-8",errors="replace")
        stage.update(status="budget" if budget else "returned",exitCode=rc,
            elapsedSeconds=time.monotonic()-begin,log=fd.identity(lp),actualMarkers=markers,diagnosticTail=tail)
        save();need(not bad,"explicit Singular failure: "+repr(bad[:3]))
        if not budget:need(rc==0,"successful exact Singular process")
        return lp,markers,budget
    code=1
    try:
        if manifest.exists():
            state=json.loads(manifest.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and
                 state["semantic"]==sem,"same exact original even-extension checkpoint")
        rec["parameters"]["evenProjectionArithmeticSelftest"]=even_projection_fixture()
        m=fd.module(a.helper)
        model=prepare(fd,m,a,state,binding,checkpoint,tick)
        names=tuple(model["originalVariableNames"])
        extended_names=tuple(model["extendedVariableNames"])
        rec["parameters"].update(
            originalGradientTermCounts=[len(p) for p in model["originalSeventeenGradients"]],
            rationalFourthComponentTermCounts=[z["rationalTerms"] for z in state["targetComponents"]],
            integralNewTargetCoefficientCount=sum(z["rationalTerms"] for z in state["targetComponents"]),
            originalCoefficientField=model["matchedCubic"],
            allOriginalFourthCoefficients7Integral=True,
            allThreeIndependentFieldFourthProductsVerified=True)
        if a.through=="prepare":
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="all-three-original-fourth-targets-prepared"
            checkpoint();return 0
        engine=shutil.which(a.singular) if not Path(a.singular).is_file() else str(a.singular)
        need(engine is not None,"actual installed Singular");engine=Path(engine).resolve()
        version=subprocess.run([str(engine),"--version"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=15)
        need(version.returncode==0,"actual Singular version")
        actual={"binary":fd.identity(engine),"versionFirstLine":version.stdout.splitlines()[0]}
        if "engine" in state:need(state["engine"]==actual,"same engine for SSI checkpoints")
        else:state["engine"]=actual;checkpoint()
        rec["parameters"]["engine"]=actual
        if "selftest" not in state:
            lp,markers,budget=run_stage("slimgb-two-degree-SSI-and-three-target-lift-selftest",selftest_script(a.out))
            complete=marker_once(markers,"@@THREE-TARGET-SELFTEST-COMPLETE",False)
            if complete:
                need(marker_once(markers,"@@SELFTEST-COMPLETE") and
                     marker_once(markers,"@@SELFTEST-DEGREE2 ") and
                     marker_once(markers,"@@SELFTEST-DEGREE3 "),"all independent two-degree gates")
                ctx=nmod_mpoly_ctx.get(("x","tt"),P,"lex")
                orig=[ctx.from_dict({(2,0):1,(0,2):6}),ctx.from_dict({(1,1):1})]
                expected=[ctx.from_dict({(0,3):1}),ctx.from_dict({(1,2):1}),ctx.from_dict({(2,1):1})]
                for k in range(3):
                    total=ctx.from_dict({})
                    for i in range(2):
                        total+=orig[i]*ctx.from_dict(parse_fast_polynomial(
                            a.out/("selftest-three-%d-%d.txt"%(k,i)),("x","tt")))
                    need(total==expected[k],"independent full original three-target fixture "+str(k))
                need(parse_fast_polynomial(a.out/"selftest-parser.txt",("x","tt"))==
                     {(4,0):2,(1,3):3,(0,0):2},"same safe literal expanded polynomial parser")
                state["selftest"]={"log":fd.identity(lp),"degree2NoPureParameter":True,
                    "actualDegree2PrefixContinuesTo3":True,"wholeSSIRoundtrip":True,
                    "liftDegBoundZero":True,"threeByThreeUnitsIdentity":True,
                    "allThreeNativeOriginalProducts":True,"allThreeIndependentFlintProducts":True}
                checkpoint()
            if budget:raise Budget("only complete actual selftest marker is reusable")
            need(complete is not None,"actual complete three-target selftest")
        else:
            markers,bad=read_markers(checked(state["selftest"]["log"]))
            need(not bad and marker_once(markers,"@@THREE-TARGET-SELFTEST-COMPLETE") and
                 all(v is True for k,v in state["selftest"].items() if k!="log"),"whole paid selftest")
        if "discovery" not in state:
            lp,markers,budget=run_stage("original17-even-slimgb-degree12-and-three-reductions",discovery_script(fd,model,a.out))
            end=marker_once(markers,"@@SLIMGB17-END ",False)
            if end:
                n,count=map(int,end.split()[1:])
                need(n>0 and 0<=count<=3 and marker_once(markers,"@@SLIMGB17-SSI-ROUNDTRIP") and
                     marker_once(markers,"@@SLIMGB17-ALL-MONOMIALS-HOMOGENEOUS-EVEN-DEGREE12"),
                     "whole original17 discovery metadata")
                residuals=[]
                for k in range(3):
                    marker=marker_once(markers,"@@TARGET-REDUCTION "+str(k)+" ")
                    parts=marker.split();need(len(parts)==3 and int(parts[1])==k,"all three target reductions")
                    residuals.append({"component":k,"terms":int(parts[2]),
                        "file":fd.identity(a.out/("discovery-target-residual-%d.txt"%k))})
                need(sum(z["terms"]>0 for z in residuals)==count,"literal number of nonzero reduced targets")
                state["discovery"]={"log":fd.identity(lp),"basis":fd.identity(a.out/"whole-original17-discovery-basis.ssi"),
                    "basisColumns":n,"nonzeroReducedTargetCount":count,"residuals":residuals,
                    "wholeSSIRoundtripVerified":True,"allBasisMonomialsHomogeneousEvenAndDegreeAtMost12":True,
                    "standardBasisCompletenessClaimed":False}
                checkpoint()
            if budget:raise Budget("slimgb phase is retained only after actual whole end marker")
            need(end is not None,"actual whole original17 discovery")
        discovery=state["discovery"]
        markers,bad=read_markers(checked(discovery["log"]));checked(discovery["basis"])
        need(not bad and marker_once(markers,"@@SLIMGB17-SSI-ROUNDTRIP") and
             marker_once(markers,"@@SLIMGB17-ALL-MONOMIALS-HOMOGENEOUS-EVEN-DEGREE12"),"paid complete discovery transcript")
        need(list(map(int,marker_once(markers,"@@SLIMGB17-END ").split()[1:]))==
             [discovery["basisColumns"],discovery["nonzeroReducedTargetCount"]],"same actual discovery metadata")
        for k,z in enumerate(discovery["residuals"]):
            need(z["component"]==k and len(parse_fast_polynomial(checked(z["file"]),extended_names))==z["terms"],
                 "complete actual reduced polynomial file")
        if discovery["nonzeroReducedTargetCount"]:
            rec["status"]="completed-discovery";rec["parameters"].update(
                outcome="at-least-one-rational-target-has-nonzero-discovery-remainder",
                noNonmembershipConclusion=True,noExactOriginalSourceYet=True)
            checkpoint();return 0
        if "threeSources" not in state:
            lp,markers,budget=run_stage("lift-only-three-original-targets",lift_script(fd,model,a.out))
            end=marker_once(markers,"@@THREE-ORIGINAL-LIFT-CANDIDATE-END",False)
            if end:
                state["threeSources"]={"log":fd.identity(lp),
                    "sourceSSI":fd.identity(a.out/"whole-original17-three-target-sources.ssi"),
                    "rows":17,"columns":3,"unitsIdentityVerified":True,
                    "wholeSSIRoundtripVerified":True,"allOriginalProductsVerified":False,"degBound":0}
                checkpoint()
            if budget:raise Budget("three whole source columns saved only after exact SSI marker")
            need(end is not None,"complete original17-by3 source candidate")
        checked(state["threeSources"]["sourceSSI"])
        markers,bad=read_markers(checked(state["threeSources"]["log"]))
        need(not bad and marker_once(markers,"@@THREE-ORIGINAL-LIFT-CANDIDATE-END"),"actual source candidate transcript")
        if "nativeProducts" in state:
            markers,bad=read_markers(checked(state["nativeProducts"]))
            need(not bad and marker_once(markers,"@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED"),
                 "actual full original native products")
        for i,z in enumerate(state["sourceTexts"]):
            need(z["index"]==i,"consecutive complete source text prefix");checked(z["file"])
        if len(state["sourceTexts"])<51:
            lp,markers,budget=run_stage("verify-three-sources-and-dump51",
                verify_script(fd,model,a.out,len(state["sourceTexts"]),"nativeProducts" in state))
            mark=marker_once(markers,"@@ALL-THREE-ORIGINAL-PRODUCTS-VERIFIED",False)
            if mark:state["nativeProducts"]=fd.identity(lp)
            for line in markers:
                if line.startswith("@@SOURCE-TEXT "):
                    i,n=map(int,line.split()[1:])
                    need(i==len(state["sourceTexts"]) and 0<=i<51 and n>=0,"next whole source text")
                    state["sourceTexts"].append({"index":i,"termsBeforeHomogeneousExtraction":n,
                        "file":fd.identity(a.out/("source-%02d.txt"%i))})
            checkpoint()
            if budget:raise Budget("whole native products and consecutive text files retained")
            need(marker_once(markers,"@@ALL-51-SOURCE-TEXTS-END") and
                 len(state["sourceTexts"])==51 and "nativeProducts" in state,"all original source texts")
        ctx=nmod_mpoly_ctx.get(names,P,"lex")
        sources=[[None for _ in range(17)] for _ in range(3)];discarded=0
        for index,z in enumerate(state["sourceTexts"]):
            tick();k,i=divmod(index,17);raw=parse_fast_polynomial(checked(z["file"]),extended_names)
            need(len(raw)==z["termsBeforeHomogeneousExtraction"],"complete source term count")
            pp={descend(e):c for e,c in raw.items() if sum(e)==12-SOURCE_WEIGHTS[i] and all(x%2==0 for x in e[6:])}
            discarded+=len(raw)-len(pp);sources[k][i]=record7(pp)
        need(state["verifiedFieldComponents"]==list(range(len(state["verifiedFieldComponents"]))) and
             len(state["verifiedFieldComponents"])<=3,"whole original component verification cursor")
        for k in range(3):
            if k in state["verifiedFieldComponents"]:continue
            tick();total=ctx.from_dict({})
            for i in range(17):
                total+=ctx.from_dict(dict7(model["fieldOriginalSeventeenGenerators"][i]))*\
                       ctx.from_dict(dict7(sources[k][i]))
                tick()
            need(total==ctx.from_dict(dict7(model["fieldNaturalFourthRationalComponents"][k])),
                 "independent full original17-variable target product "+str(k))
            state["verifiedFieldComponents"].append(k);checkpoint()
            print(json.dumps({"phase":"complete-original-field-rational-component","component":k,
                "allOriginalPolynomialCoordinatesVerified":True},separators=(",",":")),flush=True)
        slots=set()
        for component in sources:
            for i,p in enumerate(component):
                for e,c in p:slots.add((i,tuple(e)))
        positive={"format":FORMAT+"-positive","binding":binding,"prime":P,
            "targetWeight":12,"originalGradientCount":17,"rationalTargetCount":3,
            "coefficientBasis":["1","d","d^2"],"matchedCubic":model["matchedCubic"],
            "allOriginalSourcePolynomialsByTarget":sources,"sourceTermCountsByTarget":[
                sum(len(p) for p in component) for component in sources],
            "unionOriginalSourceSupportSize":len(slots),"oddOrNonWeightTwelveSourceTermsDiscarded":discarded,
            "originalSquareExtension":"H_i=z_i^2","allEvenProjectionApplied":True,
            "allThreeFullOriginalFieldPolynomialProductsVerified":True,
            "allOriginal17VariablesRetained":True,"characteristicZeroIdentityVerified":False,
            "completeWeightTwelveRankOrNegativeConclusion":False}
        state["positiveCandidate"]=fd.gz_save(a.out/"complete-original-three-target-field-sources.json.gz",positive)
        state["positiveDataSHA256"]=fd.digest(fd.canonical(positive))
        rec["parameters"].update(outcome="three-verified-original-field-sources-for-rational-fourth-components",
            positiveCandidate=state["positiveCandidate"],unionSourceSupportSize=len(slots),
            sourceTermCountsByTarget=positive["sourceTermCountsByTarget"],
            allThreeFullOriginalFieldPolynomialProductsVerified=True)
        rec["status"]="completed";checkpoint();code=0
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        rec["parameters"]["noMathematicalNegativeConclusion"]=True;code=75
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try:child.wait(timeout=5)
            except subprocess.TimeoutExpired:child.kill();child.wait()
        if manifest.exists():rec["parameters"]["manifest"]=fd.identity(manifest)
        save()
        print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
    return code
if __name__=="__main__":raise SystemExit(main())
