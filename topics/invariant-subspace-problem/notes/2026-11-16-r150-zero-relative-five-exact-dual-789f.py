#!/usr/bin/env python3
"""Five exact original finite duals for the already proved length-five zero target module.

The 230-output restriction is only a search space. Every returned dual is checked
against all 6188 original sources through s^10. A deficient search never gives a
negative statement about the full module. No full source inverse is constructed.
All mathematical arrays and resumable checkpoints remain temporary.
AI-assisted source, 2026-11-16.
"""
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,time,sys
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from pathlib import Path
from itertools import combinations_with_replacement
from flint import fmpq,fmpq_mat,nmod_mat

GEN_SHA='2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186'
ACT_SHA='2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332'
OLD_SHA='0cbedfd59ef136dfdaba038101e86ab04e3e474dfb9b7da4f10116b432a4828f'
FORMAT='r150-zero-relative-five-exact-dual-v1'
PRECISION=11
PRIME=127

class BudgetStop(Exception):pass
def require(ok,msg):
    if not ok:raise AssertionError(msg)
def stop(signum,frame):raise BudgetStop('bounded exact-dual attempt')
def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def digest(b):return hashlib.sha256(b).hexdigest()
def file_sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def load_module(name,path,expected):
    require(file_sha(path)==expected,'Frozen helper '+name)
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def zero(r,c):return fmpq_mat(r,c)
def sub(M,I,J):return fmpq_mat([[M[i,j] for j in J] for i in I])
def mzero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def pivots(R,r):return [next(j for j in range(R.ncols()) if R[i,j]) for i in range(r)]
def mh(M):
    h=hashlib.sha256();h.update(f'{M.nrows()},{M.ncols()}\n'.encode())
    for i in range(M.nrows()):h.update(('\t'.join(str(M[i,j]) for j in range(M.ncols()))+'\n').encode())
    return h.hexdigest()
def qmod(q):
    ss=str(q).split('/');den=int(ss[1]) if len(ss)>1 else 1
    require(den%PRIME!=0,'Every coefficient used for the field profile is 127-integral')
    return int(ss[0])*pow(den,-1,PRIME)%PRIME
def field(M):return nmod_mat([[qmod(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())],PRIME)
def nqsub(M,I,J):return nmod_mat([[M[i,j] for j in J] for i in I],PRIME)
def pack(M):return {'rows':M.nrows(),'columns':M.ncols(),'entries':[str(M[i,j]) for i in range(M.nrows()) for j in range(M.ncols())],'logicalSHA256':mh(M)}
def unpack(x):
    M=fmpq_mat(x['rows'],x['columns'],[fmpq(v) for v in x['entries']]);require(mh(M)==x['logicalSHA256'],'Complete decoded matrix hash');return M
def atomic(path,data):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    with open(tmp,'wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)

class Cache:
    def __init__(self,out,binding):
        self.out=Path(out);self.out.mkdir(parents=True,exist_ok=True);self.path=self.out/'manifest.json';self.binding=binding
        self.man=json.loads(self.path.read_text()) if self.path.exists() else {'format':FORMAT+'-checkpoint','binding':binding,'phases':{}}
        require(self.man['format']==FORMAT+'-checkpoint' and self.man['binding']==binding,'Exact checkpoint ancestor binding')
    def get(self,name):
        z=self.man['phases'].get(name)
        if z is None:return None
        p=self.out/z['file'];b=p.read_bytes();require(len(b)==z['bytes'] and digest(b)==z['sha256'],'Immutable phase bytes '+name)
        raw=gzip.decompress(b);require(digest(raw)==z['payloadSHA256'],'Immutable payload '+name)
        x=json.loads(raw);require(x['binding']==self.binding and x['phase']==name,'Phase semantic identity');return x['value'],bool(z['verified'])
    def put(self,name,value,verified):
        raw=canonical({'format':FORMAT+'-phase','binding':self.binding,'phase':name,'value':value});hs=digest(raw)
        path=self.out/(name+'-'+hs+'.json.gz')
        if not path.exists():
            tmp=path.with_name(path.name+'.tmp-'+str(os.getpid()))
            with open(tmp,'wb') as f:
                with gzip.GzipFile(filename='',mode='wb',fileobj=f,compresslevel=1,mtime=0) as g:g.write(raw)
                f.flush();os.fsync(f.fileno())
            os.replace(tmp,path)
        b=path.read_bytes();require(digest(gzip.decompress(b))==hs,'New immutable phase payload')
        self.man['phases'][name]={'file':path.name,'bytes':len(b),'sha256':digest(b),'payloadSHA256':hs,'verified':bool(verified)}
        atomic(self.path,canonical(self.man)+b'\n')
    def matrix(self,name):
        z=self.get(name)
        return None if z is None else (unpack(z[0]['matrix']),z[0].get('metadata',{}),z[1])
    def put_matrix(self,name,M,metadata,verified):self.put(name,{'matrix':pack(M),'metadata':metadata},verified)

def nullspace(R,rank):
    piv=pivots(R,rank);fs=[j for j in range(R.ncols()) if j not in set(piv)];K=zero(R.ncols(),len(fs))
    for c,f in enumerate(fs):
        K[f,c]=1
        for i,p in enumerate(piv):K[p,c]=-R[i,f]
    return K

def run(a,result,started):
    m=load_module('original_zero_generator',a.generator,GEN_SHA);act=load_module('original_zero_actions',a.actions,ACT_SHA)
    require(file_sha(a.original_tenth_receipt)==OLD_SHA,'Original complete tenth small receipt')
    old=json.loads(Path(a.original_tenth_receipt).read_text())
    require(old['exitCode']==0 and old['result']['status']=='completed' and old['result']['parameters']['fullLeadingDimension']==14,'Original complete tenth ancestor')
    # Natural superset of the five field detectors, not a completeness assumption.
    selected=[(d,c) for d in (0,1,2) for c in act.target_columns(d)
              if d<2 or (c[0]+c[1]==0) or (c[1]==0 and 1<=c[0]<=3 and all(2<=j<=5 for j in c[2]))]
    require(len(selected)==230,'Declared 155+45+30 output search space')
    inputs={'sourceSHA256':file_sha(__file__),'generatorSHA256':GEN_SHA,'actionsSHA256':ACT_SHA,'originalTenthOuterSHA256':OLD_SHA,'precision':PRECISION,'selection':selected,'profilePrime':PRIME}
    binding=digest(canonical(inputs));result['binding']=binding;result['parameters']['inputs']=inputs
    cache=Cache(Path(a.out)/'checkpoints',binding)
    if (z:=cache.get('complete-five-dual-result')) is not None and z[1]:
        result.update(z[0]['smallResult']);result['parameters']['completedCheckpointReused']=True;return
    coeff=act.original_coefficients(m,'zero',PRECISION-1)
    for k,v in old['result']['parameters']['originalPhysicalHashes'].items():
        require(coeff['physical'].get(k)==v,'Every original physical coefficient prefix '+k)
    indices={d:{c:i for i,(dd,c) in enumerate(selected) if dd==d} for d in (0,1,2)}
    rows=[(d,c) for d in range(4) for c in act.source_rows(d)];require(len(rows)==6188,'All original source rows')
    terms=[];used=[]
    for ri,(sd,row) in enumerate(rows):
        ts=[]
        for k in range(PRECISION):
            for td in (0,1,2):
                for j,q in act.sparse_row_terms(coeff,k,row,td,indices[td]):
                    if q:ts.append((k,j,q))
        if ts:used.append(ri);terms.append(ts)
    n=len(selected);nr=len(used);A=[zero(nr,n) for _ in range(PRECISION)]
    for i,ts in enumerate(terms):
        for k,j,q in ts:A[k][i,j]+=q
    result['parameters'].update({'originalPhysicalHashes':coeff['physical'],'all6188OriginalRowsConstructed':True,'identicallyZeroRowsDiscardedOnlyAfterExactCoefficientCheck':6188-nr,'usedOriginalRowsSHA256':digest(canonical(used)),'originalCoefficientSHA256':[mh(x) for x in A]})
    oldprofile=cache.get('constant-profile')
    if oldprofile is None:
        a0=field(A[0]);rr,r=a0.rref();J=pivots(rr,r);rr,r2=nqsub(a0,range(nr),J).transpose().rref();require(r2==r,'Field constant column rank');I=pivots(rr,r)
        det=int(nqsub(a0,I,J).det());require(det!=0,'Actual original constant unit determinant modulo 127')
        cache.put('constant-profile',{'rows':I,'columns':J,'rank':r,'unitDeterminantModulo127':det,'constantSHA256':mh(A[0]),'usedOriginalRows':used},True)
    else:
        v,verified=oldprofile;require(verified and v['constantSHA256']==mh(A[0]) and v['usedOriginalRows']==used,'Rebuilt complete original constant profile');I=v['rows'];J=v['columns'];r=v['rank']
    H=[i for i in range(nr) if i not in set(I)];K=[j for j in range(n) if j not in set(J)];nf=len(K)
    require(1<=nf<=40,'Bounded actual free-coordinate search')
    U=[sub(x,I,J) for x in A];B=[sub(x,I,K) for x in A];C=[sub(x,H,J) for x in A];D=[sub(x,H,K) for x in A]
    result['parameters'].update({'constantShape':[nr,n],'actualConstantUnitSize':r,'freeCoordinates':nf,'dependentRows':len(H),'completeOriginalUnitRowIndices':[used[i] for i in I]})
    X=[];S=[]
    for k in range(PRECISION):
        name=f'unit-solution-{k:02d}';cached=cache.matrix(name)
        rhs=-B[k]
        for i in range(1,k+1):rhs-=U[i]*X[k-i]
        rhash=mh(rhs)
        if cached is None:
            t=time.monotonic();xx=U[0].solve(rhs,algorithm='dixon');cache.put_matrix(name,xx,{'rhsSHA256':rhash,'unitSHA256':mh(U[0])},False)
        else:
            xx,meta,verified=cached;require(meta['rhsSHA256']==rhash and meta['unitSHA256']==mh(U[0]),'Exact original unit RHS identity');t=time.monotonic()
        require(U[0]*xx==rhs,'All original unit rows at coefficient '+str(k));cache.put_matrix(name,xx,{'rhsSHA256':rhash,'unitSHA256':mh(U[0]),'originalProductCoordinates':r*nf},True);X.append(xx)
        sn=f'full-schur-{k:02d}';cs=cache.matrix(sn)
        if cs is None:
            y=fmpq_mat(D[k])
            for i in range(k+1):y+=C[i]*X[k-i]
            cache.put_matrix(sn,y,{'allOriginalDependentRowsRetained':True,'coefficient':k},True)
        else:
            y,meta,verified=cs;require(verified and meta['allOriginalDependentRowsRetained'] and meta['coefficient']==k,'Full saved Schur coefficient')
        S.append(y)
        print(json.dumps({'phase':'unit-and-full-schur','coefficient':k,'unitShape':[r,nf],'seconds':time.monotonic()-started}),flush=True)
    require(mzero(S[0]),'The constant Schur vanishes exactly over Q')
    # The finite Toeplitz matrix has only 27*11 columns. Its field profile
    # selects genuine original equations, never a field kernel lifted to Q.
    prof=cache.get('finite-field-row-profile')
    if prof is None:
        Sf=[field(x) for x in S];T=nmod_mat(len(H)*PRECISION,nf*PRECISION,PRIME)
        for k in range(PRECISION):
            for ell in range(k+1):
                z=Sf[k-ell]
                for i in range(len(H)):
                    for j in range(nf):
                        if z[i,j]:T[k*len(H)+i,ell*nf+j]=z[i,j]
        rt,frank=T.transpose().rref();selection=pivots(rt,frank)
        cache.put('finite-field-row-profile',{'rows':selection,'rankModulo127':frank,'shape':[T.nrows(),T.ncols()]},True)
        del T,rt,Sf
    else:
        pp,verified=prof;require(verified,'Saved finite profile');selection=pp['rows']
    query=zero(27,nf*PRECISION);target=[selected.index((2,(0,0,(j,j)))) for j in range(2,11)];jpos={j:i for i,j in enumerate(J)};kpos={j:i for i,j in enumerate(K)}
    reads=[zero(9,nf) for _ in range(PRECISION)]
    for q,j in enumerate(target):
        if j in kpos:reads[0][q,kpos[j]]=1
        else:
            for k in range(PRECISION):
                for f in range(nf):reads[k][q,f]=X[k][jpos[j],f]
    for shift in range(3):
        for ell in range(PRECISION-shift):
            z=reads[PRECISION-1-shift-ell]
            for q in range(9):
                for f in range(nf):query[shift*9+q,ell*nf+f]=z[q,f]
    initial=list(selection)
    previous=cache.get('adaptive-original-equations')
    if previous is not None:
        pp,verified=previous;require(verified and pp['initialRows']==selection,'Adaptive profile ancestor');selection=pp['rows']
    for attempt in range(32):
        R=zero(len(selection),nf*PRECISION)
        for rr,q in enumerate(selection):
            k,i=divmod(q,len(H))
            for ell in range(k+1):
                z=S[k-ell]
                for j in range(nf):R[rr,ell*nf+j]=z[i,j]
        rr,rk=R.rref();kernel=nullspace(rr,rk);require(mzero(R*kernel),'All selected original finite equations')
        pairing=query*kernel;red,qr=pairing.rref();choice=pivots(red,qr)[:5];count=len(choice)
        chosen=sub(kernel,range(kernel.nrows()),choice);fs=[sub(chosen,range(k*nf,(k+1)*nf),range(count)) for k in range(PRECISION)]
        violation=None
        for k in range(PRECISION):
            z=zero(len(H),count)
            for i in range(k+1):z+=S[i]*fs[k-i]
            if not mzero(z):
                violation=k*len(H)+next(i for i in range(len(H)) if any(z[i,c] for c in range(count)));break
        if violation is not None:
            require(violation not in selection,'A genuinely new original compatibility equation');selection.append(violation)
            cache.put('adaptive-original-equations',{'initialRows':initial,'rows':selection,'lastSelectedRank':rk},True)
            print(json.dumps({'phase':'additional-original-equation','attempt':attempt,'selectedRank':rk,'candidatePairingRank':qr,'seconds':time.monotonic()-started}),flush=True);continue
        # Lift to the complete original output frame; omitted coordinates are 0.
        lam=[]
        for k in range(PRECISION):
            low=zero(r,count)
            for i in range(k+1):low+=X[i]*fs[k-i]
            out=zero(n,count)
            for i,j in enumerate(J):
                for c in range(count):out[j,c]=low[i,c]
            for i,j in enumerate(K):
                for c in range(count):out[j,c]=fs[k][i,c]
            lam.append(out)
        cache.put('five-original-dual-candidate',{'cochains':[pack(z) for z in lam],'selectedOutputCoordinates':selected,'candidateColumns':count},False)
        for k in range(PRECISION):
            z=zero(nr,count)
            for i in range(k+1):z+=A[i]*lam[k-i]
            require(mzero(z),'All 6188 original rows at order '+str(k))
        raw=zero(27,count)
        for shift in range(3):
            for q,j in enumerate(target):
                for c in range(count):raw[shift*9+q,c]=lam[PRECISION-1-shift][j,c]
        require(raw==sub(pairing,range(27),choice),'Independent direct target coefficient readout')
        # The previously proved s^3 target relation is also checked on every dual.
        for shift in range(3,PRECISION):
            require(all(not lam[PRECISION-1-shift][j,c] for j in target for c in range(count)),'All higher shifted original target pairings vanish')
        pairing_rank=raw.rank();require(pairing_rank==count,'Independent returned exact target functionals')
        cache.put('five-original-dual-candidate',{'cochains':[pack(z) for z in lam],'selectedOutputCoordinates':selected,'candidateColumns':count,'allOriginalProductsZero':True,'originalProductCoordinates':6188*PRECISION*count,'pairing':pack(raw)},True)
        if count<5:
            result['status']='restricted-positive-dimension-only';result['parameters'].update({'detectedTargetDimension':count,'noCompleteZeroPartitionClaimed':True});return
        full=raw.transpose();red,pr=full.rref();require(pr==5,'Full target module dimension five detected');bcols=pivots(red,pr);basis=sub(full,range(5),bcols)
        shifted=zero(5,5)
        for c,index in enumerate(bcols):
            shift,j=divmod(index,9)
            if shift<2:
                for i in range(5):shifted[i,c]=full[i,index+9]
        action=basis.solve(shifted,algorithm='dixon');require(basis*action==shifted,'Exact selected target basis action')
        coords=basis.solve(full,algorithm='dixon');require(basis*coords==full,'All 27 original target coordinates')
        for j in range(27):
            wanted=sub(coords,range(5),[j+9]) if j<18 else zero(5,1)
            require(action*sub(coords,range(5),[j])==wanted,'All 27 original shift identities')
        ranks=[5];power=fmpq_mat([[int(i==j) for j in range(5)] for i in range(5)])
        for k in range(1,4):power=power*action;ranks.append(power.rank())
        require(ranks[2:]==[1,0] and ranks[1] in (2,3),'The two previously proved possible zero partitions')
        partition=[3,1,1] if ranks[1]==2 else [3,2]
        small={'status':'completed','exactZeroTargetPartition':partition,'targetActionRanks':ranks,'parameters':dict(result['parameters'],detectedTargetDimension=5,all27OriginalTargetAndShiftColumnsRetained=True,all18PositiveShiftColumnsRetained=True,all6188OriginalRowsThroughOrder10Verified=True,originalProductCoordinates=6188*PRECISION*5,allHigherShiftedTargetPairingsZero=True,finiteDualPairingSHA256=mh(raw),targetActionSHA256=mh(action),targetBasisColumnIndices=bcols,actualSelectedFiniteEquationRank=rk,additionalOriginalEquations=attempt,fullToeplitzKernelNotClaimed=True,conclusionUsesPreviouslyProvedFullZeroTargetLengthFive=True)}
        cache.put('complete-five-dual-result',{'smallResult':small,'action':pack(action),'targetCoordinates':pack(coords),'cochains':[pack(z) for z in lam]},True)
        result.update(small);return
    raise RuntimeError('Original finite compatibility adaptation did not terminate within its bounded attempt')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--generator',required=True);ap.add_argument('--actions',required=True);ap.add_argument('--original-tenth-receipt',required=True);ap.add_argument('--out',required=True);ap.add_argument('--seconds',type=int,default=600);ap.add_argument('--memory-mib',type=int,default=4096);a=ap.parse_args()
    Path(a.out).mkdir(parents=True,exist_ok=True);started=time.monotonic();result={'format':FORMAT,'status':'started','parameters':{'temporaryMathematicalArraysOnly':True}};code=0
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2));signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop);signal.alarm(a.seconds)
    try:run(a,result,started)
    except BudgetStop as e:result.update(status='budget-checkpoint',errorType=type(e).__name__,errorMessage=str(e));code=75
    except Exception as e:result.update(status='failed',errorType=type(e).__name__,errorMessage=str(e));code=1
    finally:
        signal.alarm(0);result['elapsedSeconds']=time.monotonic()-started;result['exitCode']=code
        mp=Path(a.out)/'checkpoints'/'manifest.json'
        if mp.exists():result['parameters']['checkpointManifest']={'bytes':mp.stat().st_size,'sha256':file_sha(mp)}
        atomic(Path(a.out)/'zero-relative-five-exact-dual-receipt.json',canonical(result)+b'\n');print(json.dumps(result,ensure_ascii=False,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=='__main__':main()
