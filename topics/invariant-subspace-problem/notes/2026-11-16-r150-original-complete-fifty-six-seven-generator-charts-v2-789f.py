#!/usr/bin/env python3
"""All56 original three-minor charts of the complete critical presentation.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
Use only the56 original minors selected by the paid cubic coefficient unit.
Each chart stores a shared-base DAG extension and the complete7x54
denominator-cleared Schur matrix, all original18 sources and both maps.
No generic parameter point, free rank7, rank4 or empty quotient is assumed.
"""
import argparse,gc,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
sys.set_int_max_str_digits(0)
FORMAT="r150-original-complete-fifty-six-critical-seven-generator-charts-v2"
PARENT={"bytes":12551,"sha256":"f008cb6bfbb51d0efbe929399b18ef2d7384cb7739b24dc942b25b016211259c","logicalSha256":"e96e100317ead08232c6e4d6ef2a4dc1a33339a3909cb5e761d02983b709957a","binding":"11473d55e9cf229685bcbebf59fe30fea9c2b00e8fa225bac6d3d0ca71b7ef76"}
MINORS={"bytes":16989,"sha256":"0758cde1aea1561d6c15c09be9bcd624fc872fd18b36b5d05888e5d5863b00c7","logicalSha256":"1a714682b89b903e7f1c9dbd1eebee799eff29db096caacc5f2bb649a6c5d740","binding":"49cec78fbc0845655333ef7dc4b6614d0a02eb1adbdd9ba82554cfd9ada16edd"}
SIX={"bytes":1395,"sha256":"bd300391aff8f1f95860cbf614feb6a53f8a16c2d855b5fdf1df178d7337f061","logicalSha256":"9961cbd32e7dc693bdfb1ab5819ca419372d6e297ca5af23149ae480d6dac4a1","binding":"2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0"}
def need(b,s):
    if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save_json(p,x):
    b=json.dumps(x,sort_keys=True,indent=2).encode();t=p.with_name(p.name+".tmp");t.write_bytes(b);os.replace(t,p)
    return {"path":p.name,"bytes":len(b),"sha256":sha(b)}
def save_gz(p,x):
    b=canon(x);z=gzip.compress(b,compresslevel=1,mtime=0);t=p.with_name(p.name+".tmp");t.write_bytes(z);os.replace(t,p)
    return {"path":p.name,"bytes":len(z),"sha256":sha(z),"logicalBytes":len(b),"logicalSha256":sha(b)}
def load_gz(p,desc,binding):
    z=p.read_bytes();need(len(z)==desc["bytes"] and sha(z)==desc["sha256"],"whole original input bytes "+p.name)
    b=gzip.decompress(z);need(sha(b)==desc["logicalSha256"],"whole original input logical bytes "+p.name)
    v=json.loads(b);need(v["binding"]==binding,"same original input binding "+p.name);return v["data"]
def padd(a,b):
    r=dict(a)
    for e,c in b.items():
        r[e]=r.get(e,0)+c
        if not r[e]:del r[e]
    return r
def pneg(a):return {e:-c for e,c in a.items()}
def pmul(a,b):
    r={}
    for e,c in a.items():
        for f,d in b.items():
            k=tuple(x+y for x,y in zip(e,f));r[k]=r.get(k,0)+c*d
    return {e:c for e,c in r.items() if c}
def universal_adjugate():
    n=9;A=[]
    for i in range(3):
        row=[]
        for j in range(3):
            e=[0]*n;e[3*i+j]=1;row.append({tuple(e):1})
        A.append(row)
    adj=[[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
            v=padd(pmul(A[rr[0]][cc[0]],A[rr[1]][cc[1]]),pneg(pmul(A[rr[0]][cc[1]],A[rr[1]][cc[0]])))
            adj[i][j]=pneg(v) if (i+j)%2 else v
    det={}
    for j in range(3):det=padd(det,pmul(A[0][j],adj[j][0]))
    count=0
    for i in range(3):
        for j in range(3):
            x={};y={}
            for k in range(3):x=padd(x,pmul(A[i][k],adj[k][j]));y=padd(y,pmul(adj[i][k],A[k][j]))
            need(x==(det if i==j else {}) and y==(det if i==j else {}),"all18 universal integer adjugate products");count+=2
    return count
class Extension:
    def __init__(self,base):
        self.base=base;self.offset=len(base["nodes"]);self.nodes=[];self.weights=[];self.degrees=[];self.cache={}
        need(base["nodes"][:3]==[{"op":"integer","value":0},{"op":"integer","value":1},{"op":"integer","value":-1}],"actual base zero/one/sign IDs")
        self.zero=0;self.one=1;self.minus=2
    def wt(self,x):return self.base["nodeWeights"][x] if x<self.offset else self.weights[x-self.offset]
    def ud(self,x):return self.base["nodeUDegreeUpperBounds"][x] if x<self.offset else self.degrees[x-self.offset]
    def put(self,n,w,d):
        k=json.dumps(n,sort_keys=True,separators=(",",":"))
        if k in self.cache:return self.cache[k]
        i=self.offset+len(self.nodes);self.nodes.append(n);self.weights.append(w);self.degrees.append(d);self.cache[k]=i;return i
    def mul(self,*x):
        if 0 in x:return 0
        v=sorted(a for a in x if a!=1)
        if not v:return 1
        if len(v)==1:return v[0]
        w=None if any(self.wt(a) is None for a in v) else sum(self.wt(a) for a in v)
        return self.put({"op":"multiply","args":v},w,sum(self.ud(a) for a in v))
    def neg(self,x):return self.mul(2,x)
    def add(self,*x):
        v=sorted(a for a in x if a!=0)
        if not v:return 0
        if len(v)==1:return v[0]
        ww={self.wt(a) for a in v};w=next(iter(ww)) if len(ww)==1 else None
        return self.put({"op":"add","args":v},w,max(self.ud(a) for a in v))
    def adjugate(self,A):
        adj=[[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
                v=self.add(self.mul(A[rr[0]][cc[0]],A[rr[1]][cc[1]]),self.neg(self.mul(A[rr[0]][cc[1]],A[rr[1]][cc[0]])))
                adj[i][j]=self.neg(v) if (i+j)%2 else v
        det=self.add(*(self.mul(A[0][j],adj[j][0]) for j in range(3)))
        return adj,det
def fpoly_minor(matrices,label,p):
    R=label["rows"];C=label["columns"];zero=(0,)*6;out={}
    for perm in itertools.permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3));q={zero: -1 if inv%2 else 1}
        for i in range(3):
            linear={}
            for j,v in enumerate(matrices[C[perm[i]]][R[i]]):
                if v:
                    e=[0]*6;e[j]=1;linear[tuple(e)]=v
            q=pmul(q,linear)
        out=padd(out,q)
    return {e:c%p for e,c in out.items() if c%p}
def main():
    ap=argparse.ArgumentParser()
    for s in ["presentation-out","minor-out","six-out","out"]:ap.add_argument("--"+s,required=True)
    ap.add_argument("--seconds",type=float,default=90);ap.add_argument("--memory-mib",type=int,default=512);a=ap.parse_args()
    need(0<a.seconds<=180 and 256<=a.memory_mib<=2048,"bounded complete chart consumer")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2);out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    source_sha=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":source_sha,"parent":PARENT,"minors":MINORS,"six":SIX}))
    start=time.monotonic();rec={"format":FORMAT,"binding":binding,"sourceSha256":source_sha,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    def event(s):
        rec["parameters"]["lastCompletedPhase"]=s;print(json.dumps({"phase":s,"elapsedSeconds":time.monotonic()-start,"maxResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded complete original56 charts")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        parent=load_gz(Path(a.presentation_out)/"complete-original-ten-generator-critical-presentation.json.gz",PARENT,PARENT["binding"])
        base=load_gz(Path(a.presentation_out)/parent["arithmeticDag"]["path"],parent["arithmeticDag"],PARENT["binding"])
        mn=load_gz(Path(a.minor_out)/"complete-original-mean-three-minor-gate.json.gz",MINORS,MINORS["binding"])
        six=load_gz(Path(a.six_out)/"complete-original-six-mean-ten-generator-model.json.gz",SIX,SIX["binding"])
        tensor=load_gz(Path(a.six_out)/six["completeQuadraticTensor"]["path"],six["completeQuadraticTensor"],SIX["binding"])
        need(mn["parentBinding"]==SIX["binding"] and len(base["nodes"])==105774,"same complete source/pivot ancestry")
        fid=[v for v in base["originalInputFiles"] if v["directoryRole"]=="six" and v["path"]=="complete-original-six-mean-ten-generator-model.json.gz"]
        need(len(fid)==1 and fid[0]["sha256"]==SIX["sha256"],"same complete original mean source model")
        p=mn["prime"];root=mn["root"];need(p==127 and root==100,"actual original coefficient unit field")
        matrices=[];rational=0
        for mat in tensor["matrices"]:
            rm=[]
            for row in mat:
                rr=[]
                for v in row:
                    a0=0
                    for k,s in enumerate(v):
                        parts=s.split("/");n=int(parts[0]);d=int(parts[1]) if len(parts)==2 else 1
                        need(d%p!=0,"all original tensor denominators are127 units");rational+=1
                        a0=(a0+(n%p)*pow(d%p,-1,p)*pow(root,k,p))%p
                    rr.append(a0)
                rm.append(rr)
            matrices.append(rm)
        need(rational==432 and matrices==mn["allFourOriginalResidueMatrices"],"all actual original four-tensor residue coordinates")
        cert=mn["completeOriginalUnitCertificate"];selected=cert["selectedOriginalSourceColumns"]
        labels=mn["all80OriginalMinorLabels"];mons=[tuple(e) for e in mn["all56CubicMonomials"]]
        need(len(selected)==len(set(selected))==56 and len(labels)==80 and len(mons)==56,"exact56 selected original minors among80")
        need(cert["degree"]==3 and cert["selectedOriginalSourceLabels"]==[{"minorIndex":j,"multiplier":[0]*6} for j in selected],"complete original degree3 selected labels with zero multiplier")
        U=cert["unit"];V=cert["inverse"];need(len(U)==len(V)==56 and all(len(r)==56 for r in U+V),"complete actual coefficient unit")
        products=0
        for i in range(56):
            for j in range(56):
                need(sum(U[i][k]*V[k][j] for k in range(56))%p==int(i==j),"whole right original coefficient inverse")
                need(sum(V[i][k]*U[k][j] for k in range(56))%p==int(i==j),"whole left original coefficient inverse");products+=2
        minorcoords=0
        for j,s in enumerate(selected):
            poly=fpoly_minor(matrices,labels[s],p);co=[poly.get(e,0) for e in mons]
            need(co==mn["all80CompleteResidueMinorCoefficientRows"][s] and co==[U[i][j] for i in range(56)],"all56 coefficients of each selected original minor")
            need(any(co),"every selected original minor is nonzero");minorcoords+=56
        adjproducts=universal_adjugate();event("complete-original56-unit-minor-cover-and-universal-adjugate")
        P=parent["finitePresentationColumns"];S=parent["finitePresentationSourceColumns"]
        need(len(P)==len(S)==68 and all(len(c)==10 for c in P) and all(len(c)==18 for c in S),"full actual parent presentation/source")
        prescols=list(range(50))+list(range(61,68))
        need(len(prescols)==57,"exact derived57 original column subset")
        for j in prescols:
            for node in P[j]:need(base["nodeUDegreeUpperBounds"][node]<=1,"all57 parent columns linear in u")
        charts=[];totalentries=0;totalsources=0;graphrules=0;maxnodes=0
        for ordinal,s in enumerate(selected):
            lab=labels[s];R=lab["rows"];C=lab["columns"]
            E=[6+j for j in C];K=[i for i in range(10) if i not in E]
            pc=[61+j for j in R];rest=[j for j in prescols if j not in pc]
            need(len(E)==len(pc)==3 and len(K)==7 and len(rest)==54,"complete original chart dimensions")
            for j in pc:need(parent["finitePresentationColumnLabels"][j]["type"]=="completeOriginalMean","actual original mean pivot columns")
            ext=Extension(base)
            A=[[P[pc[j]][E[i]] for j in range(3)] for i in range(3)]
            need(all(ext.wt(x)==1 and ext.ud(x)==0 for row in A for x in row),"same exact original linear-y pivot block")
            adj,delta=ext.adjugate(A);need(ext.wt(delta)==3 and ext.ud(delta)==0,"original cubic chart determinant")
            BB=[[P[j][i] for j in rest] for i in E]
            CC=[[P[j][i] for j in pc] for i in K]
            adjB=[[ext.add(*(ext.mul(adj[i][k],BB[k][j]) for k in range(3))) for j in range(54)] for i in range(3)]
            Ca=[[ext.add(*(ext.mul(CC[i][k],adj[k][j]) for k in range(3))) for j in range(3)] for i in range(7)]
            child=[];source=[]
            for j,col in enumerate(rest):
                cc=[ext.add(ext.mul(delta,P[col][K[i]]),ext.neg(ext.add(*(ext.mul(CC[i][k],adjB[k][j]) for k in range(3))))) for i in range(7)]
                ss=[ext.add(ext.mul(delta,S[col][h]),ext.neg(ext.add(*(ext.mul(S[pc[k]][h],adjB[k][j]) for k in range(3))))) for h in range(18)]
                need(all(ext.ud(x)<=1 for x in cc),"every original child matrix entry linear in u")
                child.append(cc);source.append(ss);totalentries+=7;totalsources+=18
            graphsource=[[ext.add(*(ext.mul(S[pc[k]][h],adj[k][j]) for k in range(3))) for j in range(3)] for h in range(18)]
            graphrules+=3
            for i,node in enumerate(ext.nodes):
                need(all(0<=j<ext.offset+i for j in node.get("args",[])),"complete shared-base chart DAG has no forward reference")
            maxnodes=max(maxnodes,len(ext.nodes))
            desc=save_gz(out/("complete-original-seven-generator-chart-%02d.json.gz"%(ordinal+1)),{"format":FORMAT+"-complete-chart","binding":binding,"data":{
                "originalSelectedMinorIndex":s,"originalMinorRows":R,"originalMinorColumns":C,
                "baseArithmeticDag":parent["arithmeticDag"],"baseNodeCount":ext.offset,
                "extensionNodes":ext.nodes,"extensionWeights":ext.weights,"extensionUDegreeUpperBounds":ext.degrees,
                "originalEliminatedBasisRows":E,"originalRetainedBasisRows":K,"retainedOriginalMonomials":[parent["basisMonomials"][i] for i in K],
                "originalPivotPresentationColumns":pc,"originalRemainingPresentationColumns":rest,
                "originalPivotLabels":[parent["finitePresentationColumnLabels"][i] for i in pc],
                "originalRemainingLabels":[parent["finitePresentationColumnLabels"][i] for i in rest],
                "pivotBlock":A,"adjugateBlock":adj,"deltaNode":delta,"all7x54SchurColumns":child,"all18x54OriginalSourceColumns":source,
                "eliminatedGeneratorGraphNumerator":Ca,"all18x3GraphOriginalSources":graphsource,
                "localization":"only this original cubic minor delta is inverted",
                "sourceIdentity":"m_K*(delta*D-C*adj(A)*B)=originalGenerators*(delta*S_remaining-S_pivot*adj(A)*B)",
                "graphIdentity":"delta*m_E+m_K*C*adj(A)=originalGenerators*S_pivot*adj(A)",
                "localCokernelIsCompleteOriginalBellNormalizedCriticalQuotient":True,
                "childMatrixUDegreeAtMostOne":True,"parameterFreenessClaimed":False,"chartEmptinessClaimed":False}})
            charts.append(desc)
            save_json(out/"original56-seven-generator-chart-checkpoint.json",{"format":FORMAT+"-checkpoint","binding":binding,"completeCharts":charts,"completedCount":len(charts)})
            if ordinal%8==7 or ordinal==55:event("complete-original-charts-through-%02d"%(ordinal+1))
            del ext,child,source;gc.collect()
        need(len(charts)==56 and totalentries==56*7*54 and totalsources==56*18*54 and graphrules==168,"all original56 charts and complete source coordinates")
        final=save_gz(out/"complete-original56-seven-generator-critical-cover.json.gz",{"format":FORMAT+"-complete-cover","binding":binding,"data":{
            "parentPresentation":PARENT,"baseArithmeticDag":parent["arithmeticDag"],"selectedMinorCertificate":MINORS,
            "selectedOriginalMinorIndices":selected,"all56CompleteCharts":charts,
            "coverProof":"these56 original minors are the E-basis selected by the actual full56 cubic coefficient unit; they generate (y)^3, hence their opens cover Bell=1",
            "localPresentationShape":[7,54],"localMatrixUDegreeAtMostOne":True,
            "originalFullGeneratorOrder":parent["originalFullGeneratorOrder"],
            "onlyEachChartOriginalMinorInverted":True,"noGenericParameterRestriction":True,
            "rankThreeExceptionRetained":True,"globalFreeSevenClaimed":False,"criticalQuotientEmptyClaimed":False}})
        rec["parameters"].update({"model":final,"completeCharts":56,"all432OriginalTensorRationalResiduesVerified":True,
            "all6272OriginalCoefficientUnitProductsVerified":products==6272,"all3136SelectedOriginalMinorCoefficientsVerified":minorcoords==3136,
            "all18UniversalAdjugateProductsVerified":adjproducts==18,"completeChildMatrixCoordinates":totalentries,
            "completeOriginalSourceCoordinates":totalsources,"completeEliminatedGeneratorGraphIdentities":graphrules,
            "maximumNewNodesInOneChart":maxnodes,"sharedBaseNodesNotCopied":len(base["nodes"]),
            "all56LocalPresentationsCompleteAndLinearInU":True,"allOriginalLabelsAndSourceColumnsRetained":True,
            "globalFreeSevenClaimed":False,"criticalQuotientEmptyClaimed":False})
        rec["status"]="completed";code=0
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original56-seven-generator-critical-cover-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
