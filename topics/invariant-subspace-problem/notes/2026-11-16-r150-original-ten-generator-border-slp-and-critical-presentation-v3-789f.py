#!/usr/bin/env python3
"""Original ten-generator border operators and a finite critical presentation.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
All parameter polynomials remain exact references to the verified original
files. Constant inverses and all16 original cubic sources are actual
certificates. The output is an exact arithmetic DAG, not an expansion.
Addition/multiplication nodes share earlier nodes without flattening.
Large mean rows are streamed one original monomial pair at a time;
all original compressed and logical SHA hashes remain mandatory.
Universal substitution identities are specified in the output; no free
rank10 or finite number of stability iterations is claimed.
"""
import argparse,gc,gzip,hashlib,itertools,json,os,resource,signal,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly

FORMAT="r150-original-ten-generator-border-slp-and-finite-critical-presentation-v3"
MATCHED=[52565262336,6080833024,-43931504,3725]
FMOD=fmpq_poly([fmpq(v,MATCHED[-1]) for v in MATCHED])
NF={"bytes":1921,"sha256":"ca4c3d98675ab404cb2b8e05c8ddacd32c02d936f751cf05fe572eb57d510e48","logicalSha256":"d58cf0f99c7d2fee7087ca76297d30e70dd4b8ba830ab7b42709b7ab8c6ccc52","binding":"8fb21996da88d9abaa7d8a0c96208129603808d7c5c1e03b9acf6caa1dca6545"}
LEAD={"bytes":1653920,"sha256":"005484500176a294a3a14788843f1ad50031f2e2bce3e599c512e45ac5dacbb6","logicalSha256":"da5839f34930081d56df84d9d803daf2b226ac98de8364135463f6f94b6db1d2","binding":"41ee91c353da2b8a33bbb631d46bc48e11709dcf42e131ebf4d417c7a3e98b63"}
SIX={"bytes":1395,"sha256":"bd300391aff8f1f95860cbf614feb6a53f8a16c2d855b5fdf1df178d7337f061","logicalSha256":"9961cbd32e7dc693bdfb1ab5819ca419372d6e297ca5af23149ae480d6dac4a1","binding":"2c120983a234d63f52e19d0f81a8f486b3d5dad5ca010f1ad74ebe9c7045e7f0"}
VERIFIED={"bytes":2679,"sha256":"e5277e55afd111ce7038aead9989d1d1a236adae38edd7962cbd3548f8fe569e","logicalSha256":"9d492e238da77ee3610bad61987bc8442f9caac3e39c91226c7c83a2b4c7168c","binding":"bb79e9288b5fe0c033b2a3c51c62938b3cb9ae50c482ff30ab3c7e72af90930f"}
CANDIDATE_BINDING="883430390f24f79cf127df1df44645f091b345372ef2b36915c212c1787ae35e"
ZERO=fmpq_poly()
ONE=fmpq_poly([1])
def need(b,s):
    if not b:raise ValueError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":")).encode()
def save_json(p,x):
    raw=json.dumps(x,sort_keys=True,indent=2).encode();tmp=p.with_name(p.name+".tmp");tmp.write_bytes(raw);os.replace(tmp,p)
    return {"path":p.name,"bytes":len(raw),"sha256":sha(raw)}
def digest_file(path):
    h=hashlib.sha256();n=0
    with open(path,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b);n+=len(b)
    return n,h.hexdigest()
def save_gz(p,x):
    tmp=p.with_name(p.name+".tmp");h=hashlib.sha256();logical=0
    class Writer:
        def __init__(self,z):self.z=z
        def write(self,s):
            nonlocal logical
            b=s.encode();self.z.write(b);h.update(b);logical+=len(b);return len(s)
    with open(tmp,"wb") as f:
        with gzip.GzipFile(filename="",mode="wb",fileobj=f,compresslevel=1,mtime=0) as z:
            json.dump(x,Writer(z),sort_keys=True,separators=(",",":"))
    os.replace(tmp,p);n,hs=digest_file(p)
    return {"path":p.name,"bytes":n,"sha256":hs,"logicalBytes":logical,"logicalSha256":h.hexdigest()}

class JsonStream:
    def __init__(self,f):self.f=f;self.buf="";self.pos=0;self.eof=False;self.decoder=json.JSONDecoder()
    def more(self):
        if self.pos:
            self.buf=self.buf[self.pos:];self.pos=0
        if self.eof:return False
        b=self.f.read(65536)
        if not b:self.eof=True;return False
        self.buf+=b;return True
    def peek(self):
        while True:
            while self.pos<len(self.buf) and self.buf[self.pos].isspace():self.pos+=1
            if self.pos<len(self.buf):return self.buf[self.pos]
            if not self.more():return ""
    def take(self,c):
        need(self.peek()==c,"exact original streaming JSON punctuation "+c);self.pos+=1
    def value(self):
        need(self.peek()!="","complete original streaming JSON value")
        while True:
            try:v,end=self.decoder.raw_decode(self.buf,self.pos)
            except json.JSONDecodeError:
                need(self.more(),"complete original streaming JSON token");continue
            if end==len(self.buf) and not self.eof:
                self.more();continue
            self.pos=end;return v
    def keys(self):
        self.take("{")
        if self.peek()=="}":self.pos+=1;return
        while True:
            k=self.value();need(isinstance(k,str),"original JSON object key");self.take(":");yield k
            c=self.peek()
            if c=="}":self.pos+=1;return
            self.take(",")
    def indices(self):
        self.take("[")
        if self.peek()=="]":self.pos+=1;return
        i=0
        while True:
            yield i;i+=1
            c=self.peek()
            if c=="]":self.pos+=1;return
            self.take(",")

def key(*indices):
    v=[0]*5
    for i in indices:v[i]+=1
    return tuple(v)
def efield(values):
    need(len(values)==3,"complete E coefficient triple")
    return fmpq_poly([fmpq(v) for v in values])
def constpoly(poly):
    a=[fmpq(0)]*3
    for e,c in poly:
        need(len(e)==18 and 0<=e[0]<3 and not any(e[1:]),"actual fixed E coefficient in original polynomial")
        a[e[0]]+=fmpq(c)
    return fmpq_poly(a)
def inverse_check(U,V,label):
    n=len(U);need(len(V)==n and all(len(r)==n for r in U+V),"complete actual "+label+" unit dimensions")
    for i in range(n):
        for j in range(n):
            need(sum((U[i][k]*V[k][j] for k in range(n)),ZERO)%FMOD==fmpq_poly([int(i==j)]),"complete original "+label+" right inverse product")
    return n*n

class DAG:
    def __init__(self):
        self.nodes=[];self.weights=[];self.degrees=[];self.cache={}
        self.zero=self.intern({"op":"integer","value":0},None,0)
        self.one=self.intern({"op":"integer","value":1},0,0)
        self.minus=self.intern({"op":"integer","value":-1},0,0)
    def intern(self,node,weight,udeg):
        k=json.dumps(node,sort_keys=True,separators=(",",":"))
        if k in self.cache:
            j=self.cache[k];need(self.weights[j]==weight and self.degrees[j]==udeg,"consistent exact DAG type");return j
        j=len(self.nodes);self.nodes.append(node);self.weights.append(weight);self.degrees.append(udeg);self.cache[k]=j;return j
    def var(self,family,index):
        return self.intern({"op":"variable","family":family,"index":index},1 if family=="y" else 2,1 if family=="u" else 0)
    def constant(self,value,file_id,pointer):
        value%=FMOD
        if not value:return self.zero
        if value==ONE:return self.one
        if value==-ONE:return self.minus
        return self.intern({"op":"originalConstantE","file":file_id,"pointer":pointer},0,0)
    def parameter(self,poly,file_id,pointer,weight,stats):
        if not poly:return self.zero
        for exp,c in poly:
            need(len(exp)==18 and all(isinstance(v,int) and v>=0 for v in exp) and exp[0]<3,"complete original parameter monomial")
            need(not any(exp[13:]) and sum(exp[1:7])+2*sum(exp[7:13])==weight,"complete original parameter support and weight")
            need(fmpq(c)!=0,"canonical nonzero original rational coefficient")
            stats["originalParameterTermsVerified"]+=1
        return self.intern({"op":"originalParameterPolynomial","file":file_id,"pointer":pointer,"weight":weight},weight,0)
    def mul(self,*args):
        parts=[]
        for a in args:
            if a==self.zero:return self.zero
            if a==self.one:continue
            parts.append(a)
        if not parts:return self.one
        if len(parts)==1:return parts[0]
        parts.sort()
        wt=None if any(self.weights[a] is None for a in parts) else sum(self.weights[a] for a in parts)
        return self.intern({"op":"multiply","args":parts},wt,sum(self.degrees[a] for a in parts))
    def neg(self,a):return self.mul(self.minus,a)
    def add(self,*args):
        parts=[]
        for a in args:
            if a==self.zero:continue
            parts.append(a)
        if not parts:return self.zero
        if len(parts)==1:return parts[0]
        parts.sort();weights={self.weights[a] for a in parts}
        wt=next(iter(weights)) if len(weights)==1 else None
        return self.intern({"op":"add","args":parts},wt,max(self.degrees[a] for a in parts))
    def weighted(self,node,weight,message):
        need(node==self.zero or self.weights[node]==weight,message)
    def read_graph(self):
        for i,n in enumerate(self.nodes):
            for j in n.get("args",[]):need(0<=j<i,"every exact arithmetic DAG edge points backward")
        return len(self.nodes)

def main():
    ap=argparse.ArgumentParser()
    for name in ["low-out","leading-out","six-out","candidate-out","verified-out","out"]:ap.add_argument("--"+name,required=True)
    ap.add_argument("--seconds",type=float,default=180);ap.add_argument("--memory-mib",type=int,default=4096);a=ap.parse_args()
    need(0<a.seconds<=600 and 1024<=a.memory_mib<=8192,"bounded exact original border presentation")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,)*2)
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    source_sha=sha(Path(__file__).read_bytes());binding=sha(canon({"format":FORMAT,"sourceSha256":source_sha,"nf":NF,"leading":LEAD,"six":SIX,"verified":VERIFIED,"candidateBinding":CANDIDATE_BINDING}))
    rec={"format":FORMAT,"binding":binding,"sourceSha256":source_sha,"parameters":{"seconds":a.seconds,"memoryMiB":a.memory_mib}}
    stats={"originalParameterTermsVerified":0,"originalConstantTopCoefficientsCompared":0,"completeRightInverseProducts":0}
    files=[];filecache={};g=None
    def checked_file(root,label,name,desc,parent_binding):
        path=Path(root)/name;n,hs=digest_file(path)
        need(n==desc["bytes"] and hs==desc["sha256"],"complete actual input bytes "+name)
        h=hashlib.sha256();nb=0
        with gzip.open(path,"rb") as f:
            for b in iter(lambda:f.read(1024*1024),b""):h.update(b);nb+=len(b)
        need(h.hexdigest()==desc["logicalSha256"],"complete actual input logical bytes "+name)
        if "logicalBytes" in desc:need(nb==desc["logicalBytes"],"complete actual logical byte count "+name)
        fd={"directoryRole":label,"path":name,**desc,"binding":parent_binding};k=(label,name)
        if k in filecache:
            fid=filecache[k];need(files[fid]==fd,"same original file descriptor")
        else:fid=len(files);files.append(fd);filecache[k]=fid
        return fid,path
    def load_file(root,label,name,desc,parent_binding):
        fid,path=checked_file(root,label,name,desc,parent_binding)
        with gzip.open(path,"rt",encoding="utf-8") as f:obj=json.load(f)
        need(obj["binding"]==parent_binding,"complete actual input parent binding "+name)
        return fid,obj.get("data",obj)
    def stream_mean(desc,i):
        fid,path=checked_file(a.six_out,"six",desc["path"],desc,SIX["binding"])
        vectors={};metadata={};rootmeta={};rootkeys=set();datakeys=set()
        specs={"normalFormTenCoefficients":(10,lambda j:5-2*sum(basis[j])),
               "originalFiveUGradientSourceCoefficients":(5,lambda j:1),
               "originalSixWGradientSourceCoefficients":(6,lambda j:1)}
        with gzip.open(path,"rt",encoding="utf-8") as f:
            st=JsonStream(f)
            for k in st.keys():
                need(k not in rootkeys,"no repeated original root key");rootkeys.add(k)
                if k!="data":
                    need(k in ("binding","format"),"only original mean root metadata");rootmeta[k]=st.value();continue
                for dk in st.keys():
                    need(dk not in datakeys,"no repeated original mean key");datakeys.add(dk)
                    if dk not in specs:
                        need(dk in ("row","identity","completeSixteenCoefficientIdentityVerified"),"complete original mean fields")
                        metadata[dk]=st.value();continue
                    count,weight=specs[dk];vn=[]
                    for j in st.indices():
                        need(j<count,"all and only original coefficient columns");node=g.zero
                        for term in st.indices():
                            pair=st.value();need(isinstance(pair,list) and len(pair)==2,"complete original streamed monomial/coefficient pair")
                            node=g.parameter([pair],fid,["data",dk,j],weight(j),stats)
                        vn.append(node)
                    need(len(vn)==count,"complete original streamed coefficient array");vectors[dk]=vn
            need(st.peek()=="","no trailing original JSON bytes")
        need(rootkeys=={"binding","format","data"} and rootmeta["binding"]==SIX["binding"],"same complete original streamed mean binding")
        need(rootmeta["format"]=="r150-original-six-mean-relations-in-ten-generators-v1-complete-mean-row","same original streamed mean format")
        need(datakeys==set(specs)|{"row","identity","completeSixteenCoefficientIdentityVerified"},"all original streamed mean fields retained")
        need(metadata["row"]==i and metadata["completeSixteenCoefficientIdentityVerified"],"complete original streamed mean identity")
        return vectors

    def event(p):
        rec["parameters"]["lastCompletedPhase"]=p
        if g is not None:rec["parameters"]["arithmeticNodesAtLastPhase"]=len(g.nodes)
        print(json.dumps({"phase":p,"elapsedSeconds":time.monotonic()-start,"arithmeticNodes":len(g.nodes) if g is not None else 0,"maxResidentKiB":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    def timeout(sig,fr):raise TimeoutError("bounded complete original border SLP")
    signal.signal(signal.SIGALRM,timeout);signal.setitimer(signal.ITIMER_REAL,a.seconds);code=1
    try:
        _,nf=load_file(a.low_out,"low","complete-original-twelve-gradient-low-normal-forms.json.gz",NF,NF["binding"])
        lead_id,lead=load_file(a.leading_out,"leading","complete-original-eleven-quadratic-leading-model.json.gz",LEAD,LEAD["binding"])
        _,six=load_file(a.six_out,"six","complete-original-six-mean-ten-generator-model.json.gz",SIX,SIX["binding"])
        _,verified=load_file(a.verified_out,"verified","complete-verified-original-cubic-border-sources.json.gz",VERIFIED,VERIFIED["binding"])
        need(nf["matchedCubic"]==lead["matchedCubic"]==verified["matchedCubic"]==MATCHED,"same complete original cubic field")
        need(lead["parentBinding"]==six["parentNormalFormBinding"]==NF["binding"] and six["parentLeadingBinding"]==LEAD["binding"],"same complete original parameter ancestry")
        need(verified["parentBinding"]==LEAD["binding"] and verified["candidateBinding"]==CANDIDATE_BINDING,"same completed original cubic sources")
        need(verified["all1680OriginalRationalProductsVerified"] and verified["all560OriginalEProductsVerified"],"complete actual source verification gate")
        basis=[tuple(v) for v in lead["tenOriginalGeneratingMonomials"]]
        need(basis==[key()]+[key(i) for i in range(5)]+[key(1,4),key(2,3),key(2,4),key(3,4)],"all ten original generators in fixed order")
        need(six["tenGeneratingMonomials"]==[list(v) for v in basis],"same original six-mean basis")
        cross=list(itertools.combinations(range(5),2));square=[key(i,i) for i in range(5)]
        quad=square+[key(i,j) for i,j in cross];qindex={e:i for i,e in enumerate(quad)}
        selected=lead["actualFieldCertificate"]["wQuadraticSelectedColumns"];need(selected==list(range(6)),"same six original eliminated mixed coordinates")
        eliminated=square+[key(*cross[j]) for j in selected];kept=basis[6:]
        g=DAG();zero=g.zero;one=g.one
        yy=[g.var("y",i) for i in range(6)];ww=[g.var("w",i) for i in range(6)];uu=[g.var("u",i) for i in range(5)]
        qfield=[];qnode=[]
        for row,terms in enumerate(lead["allElevenLeadingQuadratics"]):
            f={tuple(e):efield(v) for e,v in terms};qfield.append([f.get(e,ZERO) for e in quad])
            index={tuple(e):i for i,(e,v) in enumerate(terms)}
            qnode.append([g.constant(f.get(e,ZERO),lead_id,["data","allElevenLeadingQuadratics",row,index[e],1]) if e in index else zero for e in quad])
        need(len(qfield)==11,"all original eleven quadratics retained")
        five_id,five=load_file(a.low_out,"low",nf["fiveGradientModel"]["path"],nf["fiveGradientModel"],NF["binding"])
        need(five["matchedCubic"]==MATCHED,"original five-gradient field")
        A=five["fiveULinearHessianCoefficients"];b=five["fiveUConstantCoefficients"]
        need(len(A)==len(b)==5 and all(len(r)==5 for r in A),"all original five lower rows")
        L=[[g.parameter(A[i][j],five_id,["data","fiveULinearHessianCoefficients",i,j],2,stats) for j in range(5)] for i in range(5)]
        c=[g.parameter(b[i],five_id,["data","fiveUConstantCoefficients",i],4,stats) for i in range(5)]
        Q=[[efield(v) for v in r] for r in five["squareCoefficientMatrix"]]
        Qi=[[efield(v) for v in r] for r in five["squareCoefficientMatrixInverse"]]
        Qn=[[g.constant(Qi[i][j],five_id,["data","squareCoefficientMatrixInverse",i,j]) for j in range(5)] for i in range(5)]
        for i,terms in enumerate(five["sameFiveTopQuadratics"]):
            f={tuple(e):efield(v) for e,v in terms}
            for j,e in enumerate(quad):
                need(f.get(e,ZERO)==qfield[i][j],"all original five top quadratic coefficients")
                stats["originalConstantTopCoefficientsCompared"]+=1
            need([qfield[i][qindex[e]] for e in square]==Q[i],"same original five-square unit")
        stats["completeRightInverseProducts"]+=inverse_check(Q,Qi,"five-square")
        del five,A,b;gc.collect()
        H=[]
        for h,desc in enumerate(nf["completeVerifiedNormalFormRows"][6:]):
            fid,row=load_file(a.low_out,"low",desc["path"],desc,NF["binding"])
            need(row["row"]==h+6 and row["gradient"]=="dw%d"%h and row["completeOriginalPolynomialSourceIdentityVerified"],"exact original w normal-form identity")
            co=row["normalFormCoefficients"];src=row["originalFiveGradientSourceCoefficients"]
            need(len(co)==16 and len(src)==5,"all original w coefficients and correction sources")
            c.append(g.parameter(co[0],fid,["data","normalFormCoefficients",0],4,stats))
            L.append([g.parameter(co[1+j],fid,["data","normalFormCoefficients",1+j],2,stats) for j in range(5)])
            H.append([g.constant(constpoly(src[i]),fid,["data","originalFiveGradientSourceCoefficients",i]) for i in range(5)])
            for j,pair in enumerate(cross):
                need(constpoly(co[6+j])==qfield[5+h][qindex[key(*pair)]],"all original w top coefficients match the cubic source model")
                stats["originalConstantTopCoefficientsCompared"]+=1
            need(all(qfield[5+h][qindex[e]]==ZERO for e in square),"all six w rows have no square coefficient")
            del row,co,src;gc.collect()
        cid,cv=load_file(a.six_out,"six",six["constantUnit"]["path"],six["constantUnit"],SIX["binding"])
        need(cv["selectedOriginalMixedColumns"]==selected,"same actual six-mixed unit")
        C=[[efield(x) for x in row] for row in cv["unit"]];Ci=[[efield(x) for x in row] for row in cv["inverse"]]
        for i in range(6):need(C[i]==[qfield[5+i][qindex[e]] for e in eliminated[5:]],"complete actual six-mixed coefficient unit")
        stats["completeRightInverseProducts"]+=inverse_check(C,Ci,"six-mixed")
        Cn=[[g.constant(Ci[i][j],cid,["data","inverse",i,j]) for j in range(6)] for i in range(6)]
        D=[[zero]*11 for _ in range(11)]
        for i in range(5):
            for j in range(5):D[i][j]=Qn[i][j]
            for j in range(6):
                D[i][5+j]=g.neg(g.add(*(g.mul(Qn[i][a0],qnode[a0][qindex[eliminated[5+b0]]],Cn[b0][j]) for a0 in range(5) for b0 in range(6))))
        for i in range(6):
            for j in range(6):D[5+i][5+j]=Cn[i][j]
        V=[[qnode[i][qindex[e]] for e in kept] for i in range(11)]
        event("all66-original-parameter-coefficients-and-constant-units-verified")
        qr={};qs={}
        for i,e in enumerate(eliminated):
            rr=[g.neg(g.add(*(g.mul(D[i][a0],c[a0]) for a0 in range(11))))]
            rr += [g.neg(g.add(*(g.mul(D[i][a0],L[a0][j]) for a0 in range(11)))) for j in range(5)]
            rr += [g.neg(g.add(*(g.mul(D[i][a0],V[a0][j]) for a0 in range(11)))) for j in range(4)]
            qr[e]=rr;qs[e]=list(D[i])
        for j,e in enumerate(kept):
            qr[e]=[one if k==6+j else zero for k in range(10)];qs[e]=[zero]*11
        need(set(qr)==set(quad),"all fifteen original quadratic products retained")
        for e,rr in qr.items():
            for i,node in enumerate(rr):g.weighted(node,4-2*sum(basis[i]),"exact quadratic normal-form coefficient weight")
            for node in qs[e]:g.weighted(node,0,"exact constant quadratic source coefficient")
        targets=[tuple(e) for e in verified["all16OriginalBorderMonomials"]]
        need(set(targets)=={tuple(a0+b0 for a0,b0 in zip(e,key(i))) for e in kept for i in range(5)} and len(targets)==16,"complete original cubic border")
        selected_cols=verified["selectedOriginalSourceColumns"];need(selected_cols==list(range(35)),"same actual35 cubic source columns")
        cr={};cs={}
        for j,(e,desc) in enumerate(zip(targets,verified["completeVerifiedSourceColumns"])):
            fid,obj=load_file(a.candidate_out,"candidates",desc["path"],desc,CANDIDATE_BINDING)
            need(obj["targetIndex"]==j and obj["targetMonomial"]==list(e) and obj["selectedOriginalSourceColumns"]==selected_cols,"complete original cubic candidate coordinates")
            co=obj["completeEFieldSourceCoefficients"];need(len(co)==35,"complete original cubic source length")
            xn=[g.constant(efield(v),fid,["data","completeEFieldSourceCoefficients",l]) for l,v in enumerate(co)]
            rr=[zero]*10;ss=[zero]*11
            for l,x in enumerate(xn):
                a0,k=divmod(l,5)
                rr[1+k]=g.add(rr[1+k],g.neg(g.mul(x,c[a0])))
                ss[a0]=g.add(ss[a0],g.mul(x,uu[k]))
                for b0 in range(5):
                    factor=g.neg(g.mul(x,L[a0][b0]));pair=key(k,b0)
                    for i in range(10):rr[i]=g.add(rr[i],g.mul(factor,qr[pair][i]))
                    for i in range(11):ss[i]=g.add(ss[i],g.mul(factor,qs[pair][i]))
            cr[e]=rr;cs[e]=ss
            for i,node in enumerate(rr):g.weighted(node,6-2*sum(basis[i]),"exact cubic lower normal-form coefficient weight")
            for node in ss:
                g.weighted(node,2,"exact cubic original source weight");need(g.degrees[node]<=1,"cubic source u degree at most one")
            del obj,co;gc.collect()
        event("all16-actual-cubic-sources-refilled-as-exact-parameter-SLP")
        def original_source(ss):
            return [g.add(ss[i],g.neg(g.add(*(g.mul(ss[5+h],H[h][i]) for h in range(6))))) for i in range(5)]+list(ss[5:])
        N=[[[zero]*10 for _ in range(10)] for _ in range(5)]
        S=[[[zero]*10 for _ in range(11)] for _ in range(5)]
        for i in range(5):
            for j,bm in enumerate(basis):
                e=tuple(a0+b0 for a0,b0 in zip(bm,key(i)))
                if sum(e)==1:
                    rr=[one if k==1+i else zero for k in range(10)];ss=[zero]*11
                elif sum(e)==2:rr,ss=qr[e],qs[e]
                else:rr,ss=cr[e],cs[e]
                oo=original_source(ss)
                for k in range(10):
                    N[i][k][j]=rr[k];g.weighted(rr[k],2+2*sum(bm)-2*sum(basis[k]),"all50 original multiplication-column coefficient weights")
                for k in range(11):
                    S[i][k][j]=oo[k]
                    if oo[k]!=zero:g.weighted(oo[k],2+2*sum(bm)-4,"all50 source-column weights after original w transport")
        routes=[[]]+[[i] for i in range(5)]+[[1,4],[2,3],[2,4],[3,4]]
        for i in range(5):
            need([N[i][k][0] for k in range(10)]==[one if k==i+1 else zero for k in range(10)],"all five literal cyclic routes from e0")
        for j,pair in enumerate(routes[6:]):
            i,k=pair;need([N[i][a0][1+k] for a0 in range(10)]==[one if a0==6+j else zero for a0 in range(10)],"all four retained mixed cyclic routes")
        event("all50-original-border-columns-and-nine-literal-cyclic-routes")
        mean=[];meansource=[]
        for i,desc in enumerate(six["sixCompleteMeanRows"]):
            row=stream_mean(desc,i)
            mean.append(row["normalFormTenCoefficients"])
            sc=[g.neg(x) for x in row["originalFiveUGradientSourceCoefficients"]]
            sc += [g.neg(x) for x in row["originalSixWGradientSourceCoefficients"]]
            sc += [one if j==i else zero for j in range(6)]+[zero];meansource.append(sc)
            del row;gc.collect();event("complete-original-mean-reference-%02d"%(i+1))
        bell=g.add(*(g.mul(yy[i],ww[i]) for i in range(6)));bellminus=g.add(bell,g.minus)
        columns=[];colsource=[];labels=[]
        for i in range(5):
            for j in range(10):
                columns.append([g.add(uu[i] if k==j else zero,g.neg(N[i][k][j])) for k in range(10)])
                colsource.append([S[i][k][j] for k in range(11)]+[zero]*7)
                labels.append({"type":"originalBorder","u":i,"basis":j})
        for a0 in range(11):
            terms=[c[a0]]+[g.mul(L[a0][j],uu[j]) for j in range(5)]
            for j,e in enumerate(quad):
                factors=[uu[k] for k,n in enumerate(e) for _ in range(n)]
                terms.append(g.mul(qnode[a0][j],*factors))
            gn=g.add(*terms);columns.append([gn]+[zero]*9)
            sc=[zero]*11
            if a0<5:sc[a0]=one
            else:
                sc=[g.neg(H[a0-5][i]) for i in range(5)]+[one if h==a0-5 else zero for h in range(6)]
            colsource.append(sc+[zero]*7);labels.append({"type":"originalMomentGeneratorAtE0","gradient":a0})
        for i in range(6):
            columns.append(mean[i]);colsource.append(meansource[i]);labels.append({"type":"completeOriginalMean","gradient":i})
        columns.append([bellminus]+[zero]*9);colsource.append([zero]*17+[one]);labels.append({"type":"originalBellNormalization"})
        need(len(columns)==len(colsource)==len(labels)==68,"complete finite10x68 original critical presentation")
        comm=[];commsource=[];comm_labels=[]
        for i in range(5):
            for j in range(i+1,5):
                for b0 in range(10):
                    co=[g.add(g.add(*(g.mul(N[i][k][a0],N[j][a0][b0]) for a0 in range(10))),
                              g.neg(g.add(*(g.mul(N[j][k][a0],N[i][a0][b0]) for a0 in range(10))))) for k in range(10)]
                    sc=[]
                    for h in range(11):
                        sc.append(g.add(g.add(*(g.mul(S[j][h][a0],N[i][a0][b0]) for a0 in range(10))),
                                        g.mul(uu[j],S[i][h][b0]),
                                        g.neg(g.add(*(g.mul(S[i][h][a0],N[j][a0][b0]) for a0 in range(10)))),
                                        g.neg(g.mul(uu[i],S[j][h][b0]))))
                    comm.append(co);commsource.append(sc);comm_labels.append([i,j,b0])
        need(len(comm)==100 and all(len(x)==10 for x in comm) and all(len(x)==11 for x in commsource),"all100 complete nonfree commutator columns and sources")
        event("all100-complete-original-commutator-source-columns")
        node_count=g.read_graph()
        arithmetic=save_gz(out/"complete-original-ten-generator-border-arithmetic-dag.json.gz",{"format":FORMAT+"-arithmetic-dag","binding":binding,"data":{
            "fieldCubic":MATCHED,"originalInputFiles":files,"nodes":g.nodes,"nodeWeights":g.weights,"nodeUDegreeUpperBounds":g.degrees,
            "coefficientParameters":{"y":6,"w":6},"ordinaryPolynomialVariablesU":5,
            "parameterInversesPresent":False,"allInversesArePreviouslyVerifiedFixedEConstants":True,
            "expandedParameterProductsClaimed":False}})
        model=save_gz(out/"complete-original-ten-generator-critical-presentation.json.gz",{"format":FORMAT+"-complete-model","binding":binding,"data":{
            "arithmeticDag":arithmetic,"basisMonomials":[list(e) for e in basis],"basisCyclicRoutes":routes,
            "originalMomentGradientOrder":["du%d"%i for i in range(5)]+["dw%d"%i for i in range(6)],
            "originalFullGeneratorOrder":["du%d"%i for i in range(5)]+["dw%d"%i for i in range(6)]+["dy%d"%i for i in range(6)]+["Bell-1"],
            "fiveMultiplicationRepresentatives":N,"all50OriginalBorderSources":S,
            "finitePresentationColumns":columns,"finitePresentationSourceColumns":colsource,"finitePresentationColumnLabels":labels,
            "all100CommutatorColumns":comm,"all100CommutatorSources":commsource,"all100CommutatorLabels":comm_labels,
            "completeSixOriginalMeanRelations":mean,"bellPolynomialNode":bell,"bellNormalizationNode":bellminus,
            "quadraticFormula":"z=-D*(V*v+L*u+c)+D*G, D=[[Qinv,-Qinv*P_E*Cinv],[0,Cinv]]",
            "cubicFormula":"t= -sum X*L*rho(uk*ua)-sum X*c*uk + (sum X*uk*eg -sum X*L*sigma(uk*ua))*G",
            "borderIdentity":"ui*m = m*Ni + (F5,Gw6)*Si",
            "commutatorIdentity":"m*(Ni*Nj-Nj*Ni)=(F5,Gw6)*(Sj*Ni+uj*Si-Si*Nj-ui*Sj)",
            "finitePresentationMeaning":"coker over E[y,w,u] of the 10x68 matrix; it is the complete original gradient quotient with Bell=1",
            "proofOfCompleteness":["all ten basis vectors equal their original monomials times e0 by the nine literal routes",
                "all eleven original moment generators annihilate e0",
                "all six original mean generators and Bell-1 annihilate e0 by complete original source identities",
                "the reverse map e_b to the original monomial kills every presentation column by its saved original source",
                "the maps are inverse on e0 and every basis vector"],
            "freenessOfTenGeneratorsClaimed":False,"commutativityOnFreeTenClaimed":False,
            "parameterStableClosureComputed":False,"bellNormalizedQuotientEmptyClaimed":False,
            "allParameterIdentitiesCertifiedByExactUniversalSubstitution":True,"expandedParameterCoefficientProductsClaimed":False}})
        rec["parameters"].update(stats);rec["parameters"].update({"arithmeticDag":arithmetic,"model":model,"originalInputsVerified":len(files),
            "arithmeticNodes":node_count,"complete50BorderColumns":True,"completeFinitePresentationShape":[10,68],
            "complete100CommutatorColumnsAndSources":True,"allNineLiteralCyclicRoutesVerified":True,
            "allElevenMomentAndSixMeanAndBellRelationsRetained":True,"originalConstantCubicSolveRepeated":False,
            "noParameterInversesPresent":True,"allParameterIdentitiesCertifiedByExactUniversalSubstitution":True,
            "expandedParameterCoefficientProductsClaimed":False,"parameterStableClosureComputed":False,
            "freenessOfTenGeneratorsClaimed":False,"bellNormalizedQuotientEmptyClaimed":False})
        rec["status"]="completed";code=0;event("complete-original-ten-generator-SLP-and-finite-critical-presentation")
    except BaseException as e:
        rec["status"]="budget-checkpoint" if isinstance(e,TimeoutError) else "failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        code=75 if isinstance(e,TimeoutError) else 1
    finally:
        signal.setitimer(signal.ITIMER_REAL,0);rec["elapsedSeconds"]=time.monotonic()-start;rec["maxResidentKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        desc=save_json(out/"original-ten-generator-border-presentation-receipt.json",rec)
        print(json.dumps({"status":rec["status"],"exitCode":code,"binding":binding,"elapsedSeconds":rec["elapsedSeconds"],"receipt":desc,"parameters":rec["parameters"]},sort_keys=True),flush=True)
    return code
if __name__=="__main__":sys.exit(main())
