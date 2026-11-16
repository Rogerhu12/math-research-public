#!/usr/bin/env python3
"""Actual squarefree 32-basis and fixed original constant reduction operators.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
All original q_i u^alpha columns are kept at degrees2...6.  The candidate
squarefree monomials are fixed before calculation.  A valid original
matched-field specialization (127,d=100) selects and verifies a true
constant unit at every degree.  Its exact inverse is specified by
adjugate/determinant over the same field; it is not claimed numerically
expanded.  Full regular-sequence Hilbert dimensions are supplied only
by the separately completed whole degree6 gate.
"""
import argparse,gzip,hashlib,itertools,json,os
from pathlib import Path
import resource,signal,sys,time
from flint import fmpq,fmpq_poly,nmod_mat

FORMAT="r150-original-five-moment-squarefree32-fixed-reduction-v1"
MODEL_BYTES=962420
MODEL_SHA="05301272897e83766ee604aa0873c0b5af977aa2fe5263fa37e51a0cd73dc6ca"
MODEL_LOGICAL="cef307471088203fcbb763223e132b90ecc3867158241366a364e934e16971d7"
MODEL_BINDING="35d8d699301fd0916097cf796078efad734787a8220b37e393a98b665ccc070a"
MATCHED=[52565262336,6080833024,-43931504,3725]
P=127;ROOT=100
HILB=[1,5,10,10,5,1,0]
def need(b,s):
    if not b:raise ValueError(s)
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def sha(x):return hashlib.sha256(x).hexdigest()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0)
    t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def mons(n):
    out=[]
    for a in itertools.combinations_with_replacement(range(5),n):
        e=[0]*5
        for j in a:e[j]+=1
        out.append(tuple(e))
    return out
def evalq(x):
    x=fmpq(x);d=int(x.denom())%P
    need(d!=0,"all original coefficient denominators at actual specialization are units")
    return int(x.numer())%P*pow(d,-1,P)%P
def evalfield(v):
    return sum(evalq(c)*pow(ROOT,j,P) for j,c in enumerate(v))%P
def squarefree(n):
    out=[]
    for a in itertools.combinations(range(5),n):
        e=[0]*5
        for j in a:e[j]=1
        out.append(tuple(e))
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--model",required=True);ap.add_argument("--out",required=True)
    ap.add_argument("--seconds",type=float,default=60);ap.add_argument("--memory-mib",type=int,default=1024)
    a=ap.parse_args();need(0<a.seconds<=180 and 512<=a.memory_mib<=2048,"fixed constant-operator budget")
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    started=time.monotonic();ss=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":ss,"parentBinding":MODEL_BINDING,
        "modelSha256":MODEL_SHA,"prime":P,"root":ROOT,"squarefreeCandidateFixed":True}))
    rec={"format":FORMAT,"sourceSha256":ss,"binding":binding,"status":"started",
         "parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib,"prime":P,"matchedResidue":ROOT}}
    def stop(sig,fr):raise TimeoutError("bounded squarefree basis selection")
    signal.signal(signal.SIGALRM,stop);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        raw=Path(a.model).read_bytes();need(len(raw)==MODEL_BYTES and sha(raw)==MODEL_SHA,"whole completed Jacobian gate bytes")
        logical=gzip.decompress(raw);need(sha(logical)==MODEL_LOGICAL,"whole completed Jacobian gate logical bytes")
        parent=json.loads(logical);need(parent["binding"]==MODEL_BINDING,"same complete Jacobian gate binding")
        m=parent["data"];need(m["matchedCubic"]==MATCHED and m["fullFieldRank"]==630,
                             "actual full previous630 rank gate")
        need(MATCHED[-1]%P!=0 and sum(c*pow(ROOT,j,P) for j,c in enumerate(MATCHED))%P==0,
             "actual fixed original matched-field residue homomorphism")
        Q=[{tuple(e):v for e,v in row} for row in m["allFiveQuadraticPartials"]]
        Qp=[{e:evalfield(v) for e,v in row.items()} for row in Q]
        stages=[];totalProducts=0;allW=[]
        for degree in range(7):
            W=squarefree(degree) if degree<=5 else []
            need(len(W)==HILB[degree],"exact chosen squarefree count agrees paid Hilbert dimensions")
            allW.extend(W)
            outputs=mons(degree);n=len(outputs);pos={e:i for i,e in enumerate(outputs)}
            if degree<2:
                stages.append({"degree":degree,"sourceCount":0,"outputCount":n,"standardMonomials":[list(e) for e in W],
                               "selectedOriginalSources":[],"unitDeterminantModulo127":1,"fieldRank":n})
                continue
            src=[];cols=[]
            for e in W:
                c=[0]*n;c[pos[e]]=1;cols.append(c)
            for j in range(5):
                for a0 in mons(degree-2):
                    c=[0]*n
                    for e,v in Qp[j].items():c[pos[tuple(x+y for x,y in zip(a0,e))]]=v
                    cols.append(c);src.append([j,list(a0)])
            A=nmod_mat([[c[i] for c in cols] for i in range(n)],P)
            red,rank=A.rref();rank=int(rank)
            piv=[]
            for i in range(rank):
                j=next((j for j in range(A.ncols()) if int(red[i,j])),None)
                need(j is not None and int(red[i,j])==1,"actual full original column profile")
                piv.append(j)
            need(rank==n,"actual candidate squarefree complement spans complete original output")
            need(piv[:len(W)]==list(range(len(W))),"all fixed squarefree monomials retained")
            selected=[k-len(W) for k in piv[len(W):]]
            need(len(selected)==n-len(W),"actual original source image has paid complete rank")
            U=nmod_mat([[cols[k][i] for k in piv] for i in range(n)],P)
            det=int(U.det());need(det!=0,"actual original constant square unit")
            inv=U.inv();I=nmod_mat([[int(i==j) for j in range(n)] for i in range(n)],P)
            need(U*inv==I and inv*U==I,"all original constant-unit inverse field products")
            totalProducts+=2*n*n
            stages.append({"degree":degree,"sourceCount":len(src),"outputCount":n,
               "standardMonomials":[list(e) for e in W],
               "completeOriginalSourceDictionary":src,
               "selectedOriginalSourceIndices":selected,
               "selectedOriginalSources":[src[j] for j in selected],
               "matrixColumnOrder":"fixed squarefree monomials, then selected original q_i multiples",
               "unitDeterminantModulo127":det,"fieldRank":rank,
               "completeFieldMatrixSha256":sha(bytes(x for c in cols for x in c)),
               "selectedUnitFieldMatrixSha256":sha(bytes(int(U[i,j]) for j in range(n) for i in range(n))),
               "selectedUnitInverseFieldSha256":sha(bytes(int(inv[i,j]) for j in range(n) for i in range(n))),
               "exactReductionOperator":"adj(U_degree)/det(U_degree) over E, from the original q_i coefficient columns",
               "exactInverseEntriesNumericallyExpanded":False})
        need(len(allW)==32 and len(set(allW))==32,"complete actual distinct32 squarefree monomial basis")
        model={"parentBinding":MODEL_BINDING,"matchedCubic":MATCHED,
               "originalFiveQuadraticPartials":m["allFiveQuadraticPartials"],
               "standardMonomials32":[list(e) for e in allW],"degreeStages":stages,
               "exactOperatorRecipe":{
                 "firstCoordinates":"coefficients of the standard monomials in degree d",
                 "remainingCoordinates":"coefficients of the selected original q_i*u^alpha sources",
                 "qToFReplacement":"replace q_i by F_i=q_i+lower_u; subtract selected source multiples and descend u-degree",
                 "allDenominatorsAreFixedNonzeroElementsOfE":True,
                 "allOriginalSourceLabelsRetained":True}}
        desc=save_gz(out/"complete-original-squarefree32-fixed-reduction-operators.json.gz",
                     {"format":FORMAT+"-model","binding":binding,"data":model})
        rec["parameters"].update({"model":desc,"standardBasisSize":32,"basisDegrees":HILB[:6],
            "actualSquarefreeMonomialBasisVerified":True,
            "allOriginalRationalCoefficientDenominators127Units":True,
            "originalMatchedPolynomialAtResidueVerified":True,
            "degreeUnitDimensions":[15,35,70,126,210],
            "degreeUnitDeterminants":[s["unitDeterminantModulo127"] for s in stages[2:]],
            "allOriginalFieldUnitProducts":totalProducts,
            "exactConstantReductionOperatorsDefinedByOriginalUnits":True,
            "allUnitNonvanishingLiftedToSameCharacteristicZeroField":True,
            "noParameterDenominatorIntroduced":True,
            "exactInverseEntriesNumericallyExpanded":False,
            "allRemainingTwelveGradientsSolved":False})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed"
        rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-started
        desc=save_json(out/"original-squarefree32-fixed-reduction-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"binding":binding,"exitCode":code,
                          "elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
