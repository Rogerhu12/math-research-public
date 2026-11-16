#!/usr/bin/env python3
"""One global nine-generator presentation of the original Bell=1 critical ideal.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Solve only the fixed E6 matrix T1, verify both exact inverse products,
and transport all57 original columns through a relation with a literal
unit coefficient at v1. No parameter inverse or GL6 completion is used.
"""
import argparse,gzip,hashlib,importlib.util,json,math,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,fmpz_mat
sys.set_int_max_str_digits(0)
FORMAT="r150-original-global-nine-generator-critical-presentation-v1"
HELPER_SHA="c1fb5a29177fda97390f62eec8abcb3e4ea4a7cb72034bd606202cd945c7c27b"
PARENT={"bytes":12551,"sha256":"f008cb6bfbb51d0efbe929399b18ef2d7384cb7739b24dc942b25b016211259c","logicalSha256":"e96e100317ead08232c6e4d6ef2a4dc1a33339a3909cb5e761d02983b709957a","binding":"11473d55e9cf229685bcbebf59fe30fea9c2b00e8fa225bac6d3d0ca71b7ef76"}
SIX={"bytes":1395,"sha256":"bd300391aff8f1f95860cbf614feb6a53f8a16c2d855b5fdf1df178d7337f061","logicalSha256":"9961cbd32e7dc693bdfb1ab5819ca419372d6e297ca5af23149ae480d6dac4a1","binding":"2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0"}
MATCHED=[52565262336,6080833024,-43931504,3725]
FMOD=fmpq_poly([fmpq(x,MATCHED[-1]) for x in MATCHED])
ZERO=fmpq_poly();ONE=fmpq_poly([1])
def need(b,s):
    if not b:raise ValueError(s)
def sha(x):return hashlib.sha256(x).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def fv(x):return [str(x[i]) for i in range(3)]
def main():
    ap=argparse.ArgumentParser()
    for s in ["presentation-out","six-out","chart-helper","out"]:ap.add_argument("--"+s,required=True)
    ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=768);a=ap.parse_args()
    need(0<a.seconds<=600 and 256<=a.memory_mib<=2048,"bounded original global-nine consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    start=time.monotonic();source_sha=sha(Path(__file__).read_bytes())
    binding=sha(canon({"format":FORMAT,"sourceSha256":source_sha,"helperSha256":HELPER_SHA,"parent":PARENT,"six":SIX}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":source_sha,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(s):
        rec["parameters"]["lastCompletedPhase"]=s;print(json.dumps({"phase":s,"elapsedSeconds":time.monotonic()-start,"maxResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded exact fixed-unit/global-nine consumer")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        hp=Path(a.chart_helper);need(sha(hp.read_bytes())==HELPER_SHA,"exact original shared-DAG helper")
        spec=importlib.util.spec_from_file_location("paid_chart_helper",hp);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
        parent=h.load_gz(Path(a.presentation_out)/"complete-original-ten-generator-critical-presentation.json.gz",PARENT,PARENT["binding"])
        base=h.load_gz(Path(a.presentation_out)/parent["arithmeticDag"]["path"],parent["arithmeticDag"],PARENT["binding"])
        six=h.load_gz(Path(a.six_out)/"complete-original-six-mean-ten-generator-model.json.gz",SIX,SIX["binding"])
        tensor=h.load_gz(Path(a.six_out)/six["completeQuadraticTensor"]["path"],six["completeQuadraticTensor"],SIX["binding"])
        need(base["fieldCubic"]==MATCHED and len(tensor["matrices"])==4,"same complete original field and four matrices")
        need(tensor["symmetryIdentities"]==[True]*4,"same complete exact original symmetry flags")
        T=[[fmpq_poly([fmpq(x) for x in v]) for v in row] for row in tensor["matrices"][0]]
        need(len(T)==6 and all(len(row)==6 for row in T),"complete fixed original T1")
        for i in range(6):
            for j in range(6):need(T[i][j]==T[j][i],"all36 actual original symmetric coordinates")
        Q=fmpq_mat(18,18);R=fmpq_mat(18,6);count=0
        for i in range(6):
            for j in range(6):
                for k in range(3):
                    z=T[i][j]*fmpq_poly([0]*k+[1])%FMOD
                    for l in range(3):Q[3*i+l,3*j+k]=z[l];count+=1
        for i in range(6):R[3*i,i]=1
        need(count==324,"all324 original fixed-field multiplication coordinates")
        ts=time.monotonic();X=Q.solve(R,algorithm="dixon");solve=time.monotonic()-ts
        need(X.nrows()==18 and X.ncols()==6,"all complete fixed inverse candidates")
        Ti=[[fmpq_poly([X[3*i+k,j] for k in range(3)]) for j in range(6)] for i in range(6)]
        candidate=save_gz(out/"complete-original-first-mean-matrix-inverse-candidate.json.gz",{"format":FORMAT+"-complete-candidate","binding":binding,"data":{
            "parentTensor":six["completeQuadraticTensor"],"matchedCubic":MATCHED,"matrix":tensor["matrices"][0],"inverse":[[fv(z) for z in row] for row in Ti],"savedBeforeVerification":True}})
        rec["parameters"]["inverseCandidate"]=candidate;rec["parameters"]["fixedDixonSeconds"]=solve
        event("complete-original-six-field-inverse-candidates-saved")
        rd=[math.lcm(*(int(Q[i,j].denom()) for j in range(18))) for i in range(18)]
        cd=[math.lcm(*(int(X[i,j].denom()) for i in range(18))) for j in range(6)]
        U=fmpz_mat(18,18);N=fmpz_mat(18,6)
        for i in range(18):
            for j in range(18):
                z=Q[i,j]*rd[i];need(z.denom()==1,"complete original right-inverse row scaling");U[i,j]=z.numer()
        for i in range(18):
            for j in range(6):
                z=X[i,j]*cd[j];need(z.denom()==1,"complete original right-inverse column scaling");N[i,j]=z.numer()
        Z=U*N
        for i in range(18):
            for j in range(6):need(Z[i,j]==(rd[i]*cd[j] if i==3*j else 0),"all108 original rational right inverse products")
        left=0
        for i in range(6):
            for j in range(6):
                need(sum((Ti[i][k]*T[k][j] for k in range(6)),ZERO)%FMOD==fmpq_poly([int(i==j)]),"all36 original E left inverse products");left+=1
        inverse=save_gz(out/"complete-verified-original-first-mean-matrix-inverse.json.gz",{"format":FORMAT+"-verified-inverse","binding":binding,"data":{
            "parentTensor":six["completeQuadraticTensor"],"matchedCubic":MATCHED,"matrix":tensor["matrices"][0],"inverse":[[fv(z) for z in row] for row in Ti],
            "all108OriginalRationalRightProductsVerified":True,"all36OriginalELeftProductsVerified":left==36,
            "noParameterSpecializedOrInverted":True}})
        rec["parameters"]["verifiedInverse"]=inverse;event("complete-original-fixed-E-inverse-both-directions-verified")
        ext=h.Extension(base);new_file_id=len(base["originalInputFiles"])
        inverse_nodes=[[ext.put({"op":"originalConstantE","file":new_file_id,"pointer":["data","inverse",i,j]},0,0) for j in range(6)] for i in range(6)]
        def variable(family,i):
            hits=[j for j,n in enumerate(base["nodes"]) if n=={"op":"variable","family":family,"index":i}]
            need(len(hits)==1,"same original coordinate variable node");return hits[0]
        w=[variable("w",i) for i in range(6)];u=[variable("u",i) for i in range(5)]
        eta=[ext.add(*(ext.mul(w[k],inverse_nodes[k][i]) for k in range(6))) for i in range(6)]
        P=parent["finitePresentationColumns"];sources=parent["finitePresentationSourceColumns"]
        need(len(P)==len(sources)==68 and parent["basisMonomials"][6]==[0,1,0,0,1],"same actual original v1 and full matrix")
        prescols=list(range(50))+list(range(61,68));mean_cols=list(range(61,67));pivot=6;K=[i for i in range(10) if i!=pivot]
        rawr=[ext.add(*(ext.mul(eta[j],P[61+j][i]) for j in range(6))) for i in range(10)]
        c=[rawr[i] for i in K]
        need(all(ext.ud(x)==0 for x in c),"all global replacement coefficients are parameter polynomials")
        r_h=[ext.one if i==pivot else rawr[i] for i in range(10)]
        bellminus=parent["bellNormalizationNode"];v1=ext.mul(u[1],u[4])
        need(P[67]==[bellminus]+[0]*9 and sources[67]==[0]*17+[1],"complete original Bell column")
        need(P[15][6]==2 or P[15][6]==ext.neg(1),"retained v1 border has minus one pivot")
        expected15=[0]*10;expected15[5]=u[1];expected15[6]=2
        expected40=[0]*10;expected40[0]=u[4];expected40[5]=2
        need(P[15]==expected15 and P[40]==expected40,"two complete literal cyclic border relations")
        need(sources[15]==sources[40]==[0]*18,"both literal cyclic border sources are zero")
        relation_combination=[0]*68
        for j in range(6):relation_combination[61+j]=eta[j]
        relation_combination[15]=bellminus;relation_combination[40]=ext.mul(bellminus,u[1]);relation_combination[67]=ext.neg(v1)
        sr=[ext.add(*(ext.mul(eta[j],sources[61+j][k]) for j in range(6))) for k in range(18)]
        sr[17]=ext.add(sr[17],ext.neg(v1))
        child=[];child_sources=[]
        for col in prescols:
            cc=[ext.add(P[col][i],ext.neg(ext.mul(rawr[i],P[col][pivot]))) for i in K]
            ss=[ext.add(sources[col][j],ext.neg(ext.mul(P[col][pivot],sr[j]))) for j in range(18)]
            need(all(ext.ud(n)<=1 for n in cc),"all global-nine matrix entries linear in u")
            child.append(cc);child_sources.append(ss)
        need(child[-1]==[bellminus]+[0]*8,"the only Bell base relation is literal in the child")
        for i,n in enumerate(ext.nodes):need(all(0<=j<ext.offset+i for j in n.get("args",[])),"complete global-nine shared DAG has no forward reference")
        graph=save_gz(out/"complete-original-global-nine-arithmetic-extension.json.gz",{"format":FORMAT+"-arithmetic-extension","binding":binding,"data":{
            "baseArithmeticDag":parent["arithmeticDag"],"baseNodeCount":ext.offset,
            "appendedOriginalInputFiles":[{"directoryRole":"globalNineOutput",**inverse,"binding":binding}],
            "extensionNodes":ext.nodes,"extensionWeights":ext.weights,"extensionUDegreeUpperBounds":ext.degrees,
            "fixedInverseFileId":new_file_id,"parameterInversesPresent":False}})
        model=save_gz(out/"complete-original-global-nine-critical-presentation.json.gz",{"format":FORMAT+"-complete-model","binding":binding,"data":{
            "parentPresentation":PARENT,"arithmeticExtension":graph,"verifiedFixedInverse":inverse,
            "retainedOriginalBasisRows":K,"retainedOriginalMonomials":[parent["basisMonomials"][i] for i in K],
            "eliminatedOriginalBasisRow":pivot,"original57PresentationColumns":prescols,"original57ColumnLabels":[parent["finitePresentationColumnLabels"][i] for i in prescols],
            "etaNodes":eta,"rawMeanRelationVector":rawr,"literalUnitRelationVector":r_h,
            "literalUnitRelationOriginal68ColumnCombination":relation_combination,"literalUnitRelationOriginal18Source":sr,
            "complete9x57Columns":child,"complete18x57OriginalSourceColumns":child_sources,
            "originalFullGeneratorOrder":parent["originalFullGeneratorOrder"],
            "relationIdentity":"r_h=sum eta_j*h_j+(Bell-1)*(R_1,u4+u1*R_4,0)-u1*u4*R_Bell",
            "constantUnitIdentity":"w^T*T1^{-1}*(T1*y)=Bell; hence r_h[v1]=1 globally",
            "projectionIdentity":"P(e_v1)=-sum_{i!=v1} r_h[i]*e_i; P(e_i)=e_i for retained i",
            "sourceIdentity":"source(new_column)=source(old_column)-old_column[v1]*source(r_h)",
            "globalPresentationMeaning":"complete original Bell-normalized critical quotient over E[y,w,u], with no parameter localization",
            "overBellBaseQuotient":{"ring":"E[y,w]/(Bell-1)[u]","shape":[9,56],"omitFinalChildColumn":True},
            "freeNineClaimed":False,"criticalQuotientEmptyClaimed":False,"rankFourAssumed":False,
            "allIdentitiesCertifiedByExactFixedInverseAndOriginalSourceTransport":True,"expandedParameterProductsClaimed":False}})
        rec["parameters"].update({"arithmeticExtension":graph,"model":model,"completeGlobalPresentationShape":[9,57],
            "completeBellBasePresentationShape":[9,56],"all324OriginalFixedUnitCoordinatesVerified":count==324,
            "all108OriginalRationalRightInverseProductsVerified":True,"all36OriginalELeftInverseProductsVerified":left==36,
            "allNineUnitProjectionRowsRetained":True,"all57OriginalRelationColumnsRetained":True,
            "completeOriginalSourceCoordinates":18*57,"completeChildMatrixCoordinates":9*57,
            "newArithmeticNodes":len(ext.nodes),"maximumOriginalSourceUDegree":max(ext.ud(x) for row in child_sources for x in row),
            "literalUnitRelationInOriginal57Image":True,"allChildEntriesLinearInU":True,
            "noParameterInversesOrUnimodularCompletion":True,"freeNineClaimed":False,"criticalQuotientEmptyClaimed":False})
        rec["status"]="completed";code=0;event("complete-original-global-nine-presentation-and-all-original-sources")
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-global-nine-critical-presentation-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
