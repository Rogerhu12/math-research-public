#!/usr/bin/env python3
"""Stream the verified original zero-unit checkpoints and construct five Q duals.

No full mathematical matrix is passed to json.loads. Every parent gzip is checked
by compressed-byte, uncompressed-payload, and complete logical matrix SHA, while
only requested rows are retained. The completed parent is read-only. Field data
choose a unit and five free slots; all final conclusions require exact Q solves
and all 6188 original equations at each of eleven coefficients.
AI-assisted source, 2026-11-16.
"""
import argparse,gzip,hashlib,importlib.util,json,os,re,resource,signal,time,gc,sys
from pathlib import Path
from math import gcd,lcm
from flint import fmpq,fmpq_mat,nmod_mat
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)

FORMAT='r150-zero-relative-five-streamed-unit-v1'
UTILITY_SHA='313b09b432591d78eacb5aae393083995630e74df9c69d61cdfba6f9d9456b87'
PARENT_SOURCE_SHA='45b01f0206d7c74832e91602e40854728a7e376df860f2f6ad17f35b61084e4b'
PARENT_BINDING='9131c2f4dd530684bbc9f8f7c9005c1365de72cb170492bbdc1073f2c6a53a8a'
PARENT_MANIFEST_SHA='215d279bd8a145983ca0d1507cf9fa8c4be4d68139622436008dffc331aaa7c4'
GEN_SHA='2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186'
ACT_SHA='2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332'
OLD_SHA='0cbedfd59ef136dfdaba038101e86ab04e3e474dfb9b7da4f10116b432a4828f'
N=11;P=127
WHITELIST={'constant-profile','finite-field-row-profile'}|{f'{prefix}-{k:02d}' for prefix in ('unit-solution','full-schur') for k in range(N)}
QTEXT=re.compile(rb'-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?')

class BudgetStop(Exception):pass
def req(ok,msg):
    if not ok:raise AssertionError(msg)
def stop(signum,frame):raise BudgetStop('streamed-unit budget checkpoint')
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def fsha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def atomic(p,b):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);q=p.with_name(p.name+'.tmp-'+str(os.getpid()))
    with open(q,'wb') as f:f.write(b);f.flush();os.fsync(f.fileno())
    os.replace(q,p)
def module(name,p,expected):
    req(fsha(p)==expected,'Frozen source '+name);s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def zero(r,c):return fmpq_mat(r,c)
def sub(M,I,J):return fmpq_mat([[M[i,j] for j in J] for i in I])
def iszero(M):return all(not M[i,j] for i in range(M.nrows()) for j in range(M.ncols()))
def piv(R,r):return [next(j for j in range(R.ncols()) if R[i,j]) for i in range(r)]
def qmod(q):
    s=str(q).split('/');d=int(s[1]) if len(s)>1 else 1;req(d%P!=0,'127-integral field selection');return int(s[0])*pow(d,-1,P)%P
def field(M):return nmod_mat([[qmod(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())],P)
def trim():
    gc.collect()
    try:
        import ctypes
        ctypes.CDLL(None).malloc_trim(0)
    except (AttributeError,OSError):pass

class Parent:
    def __init__(self,root):
        self.root=Path(root);b=(self.root/'manifest.json').read_bytes();req(len(b)==7555 and sha(b)==PARENT_MANIFEST_SHA,'Pinned parent inventory')
        self.man=json.loads(b);req(self.man['binding']==PARENT_BINDING and set(self.man['phases'])==WHITELIST and all(z['verified'] for z in self.man['phases'].values()),'All and only 24 verified parent phases')
        self.checked=set();self.streams={}
    def path(self,name):
        req(name in WHITELIST,'Whitelisted original parent phase');z=self.man['phases'][name];p=self.root/z['file']
        if name not in self.checked:
            req(p.stat().st_size==z['bytes'] and fsha(p)==z['sha256'],'Complete parent compressed bytes '+name);self.checked.add(name)
        return p,z
    def small(self,name):
        p,z=self.path(name);req(z['bytes']<10000,'Only a small nonmatrix parent JSON may be loaded')
        b=gzip.decompress(p.read_bytes());req(sha(b)==z['payloadSHA256'],'Small parent payload');x=json.loads(b);req(x['binding']==PARENT_BINDING and x['phase']==name,'Small parent semantic identity');return x['value']
    def rows(self,name,shape,wanted_rows,wanted_cols):
        p,z=self.path(name);nr,nc=shape;wr=list(wanted_rows);wc=list(wanted_cols);req(len(set(wr))==len(wr) and len(set(wc))==len(wc),'Unique selected matrix coordinates')
        req(all(0<=i<nr for i in wr) and all(0<=j<nc for j in wc),'Selected rows in complete parent shape')
        im={v:i for i,v in enumerate(wr)};jm={v:j for j,v in enumerate(wc)};out=zero(len(wr),len(wc))
        ph=hashlib.sha256();lh=hashlib.sha256();lh.update(f'{nr},{nc}\n'.encode());count=0
        with gzip.open(p,'rb') as g:
            def read():
                b=g.read(1<<16);ph.update(b);return b
            buf=read();marker=b'"entries":['
            while marker not in buf:
                req(len(buf)<1<<20,'Bounded original JSON prefix');b=read();req(bool(b),'Original matrix entries marker');buf+=b
            at=buf.index(marker);prefix=buf[:at]+b'"entries":';buf=buf[at+len(marker):];pos=0;expect_value=True
            while True:
                while pos>=len(buf):
                    buf=read();pos=0;req(bool(buf),'Complete original matrix array')
                c=buf[pos]
                if expect_value:
                    if c==93:
                        suffix=buf[pos+1:];break
                    req(c==34,'Exact rational string token')
                    end=buf.find(b'"',pos+1)
                    while end<0:
                        buf=buf[pos:];pos=0;b=read();req(bool(b),'Complete rational string');buf+=b;req(len(buf)<(1<<26),'Bounded rational token');end=buf.find(b'"',1)
                    value=buf[pos+1:end];req(QTEXT.fullmatch(value) is not None,'Canonical exact rational token')
                    req(count<nr*nc,'Complete matrix entry count upper bound');i,j=divmod(count,nc)
                    lh.update(value);lh.update(b'\n' if j==nc-1 else b'\t')
                    if i in im and j in jm:out[im[i],jm[j]]=fmpq(value.decode('ascii'))
                    count+=1;pos=end+1;expect_value=False
                else:
                    if c==44:pos+=1;expect_value=True
                    else:
                        req(c==93,'Rational array delimiter');suffix=buf[pos+1:];break
                if pos>1<<16:buf=buf[pos:];pos=0
            for b in iter(read,b''):
                suffix+=b;req(len(suffix)<1<<20,'Bounded original JSON suffix')
        req(count==nr*nc,'All parent matrix coordinates streamed');req(ph.hexdigest()==z['payloadSHA256'],'Full decompressed payload SHA '+name)
        # Only the small skeleton is decoded as JSON; the mathematical array is [] here.
        x=json.loads(prefix+b'[]'+suffix);req(x['binding']==PARENT_BINDING and x['phase']==name,'Original streamed semantic identity')
        mat=x['value']['matrix'];req(mat['rows']==nr and mat['columns']==nc and mat['logicalSHA256']==lh.hexdigest(),'Complete logical matrix SHA '+name)
        self.streams[name]={'fullEntriesVerified':count,'logicalSHA256':lh.hexdigest(),'retainedRowsAtMost':max(len(wr),self.streams.get(name,{}).get('retainedRowsAtMost',0))}
        return out,x['value'].get('metadata',{})

class Cache:
    def __init__(self,root,binding,u):
        self.root=Path(root);self.root.mkdir(parents=True,exist_ok=True);self.path=self.root/'manifest.json';self.binding=binding;self.u=u
        self.man=json.loads(self.path.read_text()) if self.path.exists() else {'format':FORMAT+'-checkpoint','binding':binding,'phases':{}}
        req(self.man['binding']==binding and self.man['format']==FORMAT+'-checkpoint','Fresh or matching streamed child binding')
    def get(self,name):
        z=self.man['phases'].get(name)
        if z is None:return None
        p=self.root/z['file'];req(p.stat().st_size==z['bytes'] and fsha(p)==z['sha256'],'Small child phase bytes')
        b=gzip.decompress(p.read_bytes());req(sha(b)==z['payloadSHA256'],'Small child phase payload');x=json.loads(b);req(x['binding']==self.binding and x['phase']==name,'Small child identity');return x['value'],z['verified']
    def put(self,name,value,verified):
        b=canon({'format':FORMAT+'-phase','binding':self.binding,'phase':name,'value':value});hs=sha(b);p=self.root/(name+'-'+hs+'.json.gz')
        if not p.exists():
            q=p.with_name(p.name+'.tmp-'+str(os.getpid()))
            with open(q,'wb') as f:
                with gzip.GzipFile(filename='',fileobj=f,mode='wb',compresslevel=1,mtime=0) as g:g.write(b)
                f.flush();os.fsync(f.fileno())
            os.replace(q,p)
        self.man['phases'][name]={'file':p.name,'bytes':p.stat().st_size,'sha256':fsha(p),'payloadSHA256':hs,'verified':bool(verified)};atomic(self.path,canon(self.man)+b'\n')
    def matrix(self,name):
        z=self.get(name)
        return None if z is None else (self.u.unpack(z[0]['matrix']),z[0]['metadata'],z[1])
    def put_matrix(self,name,M,metadata,verified):self.put(name,{'matrix':self.u.pack(M),'metadata':metadata},verified)

def primitive_inplace(M):
    maxbits=0
    for i in range(M.nrows()):
        ns=[];ds=[];den=1
        for j in range(M.ncols()):
            a=str(M[i,j]).split('/');n=int(a[0]);d=int(a[1]) if len(a)>1 else 1;ns.append(n);ds.append(d);den=lcm(den,d)
        vals=[n*(den//d) for n,d in zip(ns,ds)];content=0
        for x in vals:content=gcd(content,abs(x))
        content=content or 1
        for j,x in enumerate(vals):x//=content;M[i,j]=x;maxbits=max(maxbits,abs(x).bit_length())
    return maxbits

def run(a,result,start):
    req(fsha(a.parent_source)==PARENT_SOURCE_SHA,'Original frozen parent source')
    u=module('paid_unit_utilities',a.unit_utilities,UTILITY_SHA);m=module('paid_original_generator',a.generator,GEN_SHA);act=module('paid_original_actions',a.actions,ACT_SHA)
    req(fsha(a.original_tenth_receipt)==OLD_SHA,'Complete original tenth receipt');old=json.loads(Path(a.original_tenth_receipt).read_text());req(old['exitCode']==0 and old['result']['status']=='completed','Successful original tenth ancestor')
    parent=Parent(a.parent_checkpoints);cp=parent.small('constant-profile');fp=parent.small('finite-field-row-profile')
    selection=[(d,c) for d in (0,1,2) for c in act.target_columns(d) if d<2 or sum(c[:2])==0 or (c[1]==0 and 1<=c[0]<=3 and all(2<=j<=5 for j in c[2]))]
    req(len(selection)==230,'Exact 230-coordinate original search support')
    semantic={'sourceSHA256':fsha(__file__),'utilitySHA256':UTILITY_SHA,'parentSourceSHA256':PARENT_SOURCE_SHA,'parentBinding':PARENT_BINDING,'parentManifestSHA256':PARENT_MANIFEST_SHA,'generatorSHA256':GEN_SHA,'actionsSHA256':ACT_SHA,'originalTenthSHA256':OLD_SHA,'precision':N,'selectedCoordinates':selection}
    binding=sha(canon(semantic));result['binding']=binding;result['parameters']['semanticInputs']=semantic;cache=Cache(Path(a.out)/'checkpoints',binding,u)
    if (done:=cache.get('complete-result')) is not None and done[1]:result.update(done[0]['smallResult']);return
    I=cp['rows'];J=cp['columns'];r=cp['rank'];used=cp['usedOriginalRows'];nr=len(used);H=[i for i in range(nr) if i not in set(I)];K=[j for j in range(230) if j not in set(J)];nf=len(K);req(r==203 and nf==27,'Actual inherited constant profile')
    allrows=list(fp['rows']);initial=list(allrows);unit_columns=None
    previous=cache.get('adaptive-original-rows')
    if previous is not None:
        pp,v=previous;req(v and pp['initial']==initial,'Explicit adaptive original row ancestry');allrows=pp['rows'];unit_columns=pp['unitColumns']
    target=[selection.index((2,(0,0,(j,j)))) for j in range(2,11)];jp={j:i for i,j in enumerate(J)};kp={j:i for i,j in enumerate(K)}
    unit_target_rows=sorted({jp[j] for j in target if j in jp});trp={v:i for i,v in enumerate(unit_target_rows)}
    query=zero(27,nf*N)
    for k in range(N):
        xx,meta=parent.rows(f'unit-solution-{k:02d}',(r,nf),unit_target_rows,range(nf))
        for shift in range(3):
            ell=N-1-shift-k
            if ell<0:continue
            for q,j in enumerate(target):
                if j in kp:
                    if k==0:query[shift*9+q,ell*nf+kp[j]]=1
                else:
                    for f in range(nf):query[shift*9+q,ell*nf+f]=xx[trp[jp[j]],f]
        del xx;trim()
    coeff=act.original_coefficients(m,'zero',N-1)
    for k,v in old['result']['parameters']['originalPhysicalHashes'].items():req(coeff['physical'].get(k)==v,'Original physical prefix '+k)
    indices={d:{c:i for i,(dd,c) in enumerate(selection) if dd==d} for d in (0,1,2)};source_rows=[(d,row) for d in range(4) for row in act.source_rows(d)];req(len(source_rows)==6188,'Complete original sources')
    terms=[[] for _ in range(N)];actual_used=set()
    for ri,(sd,row) in enumerate(source_rows):
        for k in range(N):
            for td in (0,1,2):
                for j,q in act.sparse_row_terms(coeff,k,row,td,indices[td]):
                    if q:terms[k].append((ri,j,q));actual_used.add(ri)
    req(sorted(actual_used)==used,'All original row supports match the verified parent')
    original_to_used={v:i for i,v in enumerate(used)};hpos={v:i for i,v in enumerate(H)}
    result['parameters'].update({'originalPhysicalHashes':coeff['physical'],'inherited203By27UnitProductsAlreadyVerified':True,'parentMatricesNeverDecodedAsWholeJSON':True,'originalSourceRows':6188,'finitePrecision':N,'usedOriginalRows':nr})
    for attempt in range(32):
        R=zero(len(allrows),nf*N);wanted=sorted({q%len(H) for q in allrows});pos={v:i for i,v in enumerate(wanted)}
        for k in range(N):
            ss,meta=parent.rows(f'full-schur-{k:02d}',(len(H),nf),wanted,range(nf));req(meta['allOriginalDependentRowsRetained'] and meta['coefficient']==k,'Verified complete original Schur metadata')
            for rr,q in enumerate(allrows):
                order,i=divmod(q,len(H));ell=order-k
                if ell>=0:
                    for j in range(nf):R[rr,ell*nf+j]=ss[pos[i],j]
            del ss;trim()
        bits=primitive_inplace(R);trim()
        if unit_columns is None:
            rf,rank=field(R).rref();req(rank==len(allrows),'Actual finite field row unit');unit_columns=piv(rf,rank)
        rank=len(unit_columns);req(rank==len(allrows),'All selected original rows independent');fc=[j for j in range(R.ncols()) if j not in set(unit_columns)]
        U=sub(R,range(rank),unit_columns);F=sub(R,range(rank),fc);chosen_free=None
        if len(allrows)==len(initial):
            Uf=field(U);qf=field(sub(query,range(27),fc))-field(sub(query,range(27),unit_columns))*(Uf.inv()*field(F));qrr,qr=qf.rref()
            if qr>=5:chosen_free=[fc[j] for j in piv(qrr,qr)[:5]]
        if chosen_free is None:
            trans=u.primitive_solve(cache,f'query-transpose-{attempt:02d}',U.transpose(),sub(query,range(27),unit_columns).transpose(),start)
            redq=sub(query,range(27),fc)-trans.transpose()*F;rr,qr=u.primitive_rows(redq)[0].rref();chosen_free=[fc[j] for j in piv(rr,qr)[:5]];del trans,redq
        count=len(chosen_free);print(json.dumps({'phase':'selected-five-original-unit','unitRows':rank,'actualRHS':count,'primitiveFiniteRowMaxBits':bits,'seconds':time.monotonic()-start}),flush=True)
        sol=u.primitive_solve(cache,f'five-dual-unit-{attempt:02d}',U,-sub(R,range(rank),chosen_free),start)
        chosen=zero(nf*N,count)
        for i,j in enumerate(unit_columns):
            for c in range(count):chosen[j,c]=sol[i,c]
        for c,j in enumerate(chosen_free):chosen[j,c]=1
        req(iszero(R*chosen),'All original selected finite equations')
        fs=[sub(chosen,range(k*nf,(k+1)*nf),range(count)) for k in range(N)]
        # Retain only the eleven small five-column cochains, never all 27-column X.
        lam=[zero(230,count) for _ in range(N)]
        for k in range(N):
            for i,j in enumerate(K):
                for c in range(count):lam[k][j,c]=fs[k][i,c]
        for k in range(N):
            xx,meta=parent.rows(f'unit-solution-{k:02d}',(r,nf),range(r),range(nf))
            for ell in range(N-k):
                part=xx*fs[ell]
                for i,j in enumerate(J):
                    for c in range(count):lam[k+ell][j,c]+=part[i,c]
                del part
            del xx;trim()
        for k,z in enumerate(lam):cache.put_matrix(f'candidate-cochain-{attempt:02d}-{k:02d}',z,{'coefficient':k,'originalOutputSelection':sha(canon(selection))},False)
        violation=None
        for k in range(N):
            residual=zero(6188,count)
            for i in range(k+1):
                for rr,cc,q in terms[i]:
                    for c in range(count):
                        v=lam[k-i][cc,c]
                        if v:residual[rr,c]+=q*v
            if not iszero(residual):
                rr=next(i for i in range(6188) if any(residual[i,c] for c in range(count)));ui=original_to_used[rr]
                req(ui in hpos,'Every original unit row remains exactly zero');violation=k*len(H)+hpos[ui];break
            del residual
        if violation is not None:
            req(violation not in allrows,'A new independent original compatibility row');vk,vi=divmod(violation,len(H));newrow=zero(1,nf*N)
            for k in range(vk+1):
                zz,meta=parent.rows(f'full-schur-{k:02d}',(len(H),nf),[vi],range(nf))
                for j in range(nf):newrow[0,(vk-k)*nf+j]=zz[0,j]
                del zz
            dual=u.primitive_solve(cache,f'new-original-row-{attempt:02d}',U.transpose(),sub(newrow,[0],unit_columns).transpose(),start);rem=newrow-dual.transpose()*R
            newcol=next(j for j in fc if rem[0,j]);req(all(not rem[0,j] for j in unit_columns),'New original row reduced against the exact unit');allrows.append(violation);unit_columns.append(newcol)
            cache.put('adaptive-original-rows',{'initial':initial,'rows':allrows,'unitColumns':unit_columns},True)
            del lam,fs,R,U,F,chosen,sol;trim();continue
        raw=zero(27,count)
        for shift in range(3):
            for q,j in enumerate(target):
                for c in range(count):raw[9*shift+q,c]=lam[N-1-shift][j,c]
        req(raw==query*chosen,'Direct original target readout equals the unit transport')
        req(raw.rank()==count,'Independent actual target detector columns')
        for shift in range(3,N):req(all(not lam[N-1-shift][j,c] for j in target for c in range(count)),'All s^3 and higher original target readouts vanish')
        for k,z in enumerate(lam):cache.put_matrix(f'candidate-cochain-{attempt:02d}-{k:02d}',z,{'coefficient':k,'allOriginalSourceProductsThroughOrder10Verified':True},True)
        if count<5:
            result['status']='restricted-positive-dimension-only';result['parameters']['detectedDimension']=count;result['parameters']['completePartitionNotClaimed']=True;return
        full=raw.transpose();rr,rrank=full.rref();req(rrank==5,'Five actual target functionals');bc=piv(rr,rrank);basis=sub(full,range(5),bc);shifted=zero(5,5)
        for c,j in enumerate(bc):
            if j<18:
                for i in range(5):shifted[i,c]=full[i,j+9]
        action=basis.solve(shifted,algorithm='dixon');coords=basis.solve(full,algorithm='dixon');req(basis*action==shifted and basis*coords==full,'Complete exact original target coordinates')
        for j in range(27):req(action*sub(coords,range(5),[j])==(sub(coords,range(5),[j+9]) if j<18 else zero(5,1)),'All 27 original parameter-action products')
        powers=[5];power=fmpq_mat([[int(i==j) for j in range(5)] for i in range(5)])
        for k in range(3):power=power*action;powers.append(power.rank())
        req(powers[2:]==[1,0] and powers[1] in (2,3),'Previously established two possible zero partitions')
        partition=[3,1,1] if powers[1]==2 else [3,2]
        result.update(status='completed',exactZeroTargetPartition=partition,targetActionRanks=powers)
        result['parameters'].update({'all27TargetShiftColumnsRetained':True,'all18PositiveShiftColumnsRetained':True,'all6188OriginalRowsThroughOrder10Verified':True,'originalProductCoordinates':6188*N*5,'actualSelectedFiniteEquationRank':rank,'additionalOriginalEquations':len(allrows)-len(initial),'finiteDualPairingSHA256':u.mh(raw),'targetActionSHA256':u.mh(action),'targetBasisColumnIndices':bc,'detectedTargetDimension':5,'allHigherShiftedTargetReadoutsZero':True,'fullToeplitzKernelNotClaimed':True,'usesProvedFullZeroTargetDimensionFive':True,'parentStreamingChecks':parent.streams,'newCochainSHA256':[u.mh(z) for z in lam]})
        cache.put('complete-result',{'smallResult':dict(result),'action':u.pack(action),'targetCoordinates':u.pack(coords),'finitePairing':u.pack(raw)},True);return
    raise RuntimeError('Bounded exact compatibility adaptation exhausted')

def main():
    ar=argparse.ArgumentParser()
    for name in ('parent-source','parent-checkpoints','unit-utilities','generator','actions','original-tenth-receipt','out'):ar.add_argument('--'+name,required=True)
    ar.add_argument('--seconds',type=int,default=600);ar.add_argument('--memory-mib',type=int,default=2048);a=ar.parse_args();Path(a.out).mkdir(parents=True,exist_ok=True)
    start=time.monotonic();result={'format':FORMAT,'status':'started','parameters':{'allMathematicalArraysTemporary':True}};code=0
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2));signal.signal(signal.SIGALRM,stop);signal.signal(signal.SIGTERM,stop);signal.alarm(a.seconds)
    try:run(a,result,start)
    except BudgetStop as e:result.update(status='budget-checkpoint',errorType=type(e).__name__,errorMessage=str(e));code=75
    except Exception as e:result.update(status='failed',errorType=type(e).__name__,errorMessage=str(e));code=1
    finally:
        signal.alarm(0);result['elapsedSeconds']=time.monotonic()-start;result['exitCode']=code;result['peakResidentKiB']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        p=Path(a.out)/'checkpoints'/'manifest.json'
        if p.exists():result['parameters']['checkpointManifest']={'bytes':p.stat().st_size,'sha256':fsha(p)}
        atomic(Path(a.out)/'zero-relative-five-streamed-unit-receipt.json',canon(result)+b'\n');print(json.dumps(result,sort_keys=True,ensure_ascii=False),flush=True)
    raise SystemExit(code)
if __name__=='__main__':main()
