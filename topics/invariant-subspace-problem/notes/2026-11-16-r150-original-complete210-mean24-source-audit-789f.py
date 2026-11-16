#!/usr/bin/env python3
"""Independent complete products for the 24 actual second mean images.
Author: OpenAI ChatGPT /root, GPT-6 Astra Pro, 2026-11-16.
No producer helper is imported. Mathematical payloads remain temporary.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import fmpz_mod_mpoly_ctx

def digest(b): return hashlib.sha256(b).hexdigest()
def checked(path,desc):
    b=path.read_bytes()
    assert len(b)==desc['bytes'] and digest(b)==desc['sha256'],str(path)
    return b
def phase(root,desc,binding):
    raw=gzip.decompress(checked(root/desc['path'],desc))
    assert len(raw)==desc['logicalBytes'] and digest(raw)==desc['logicalSha256']
    z=json.loads(raw); assert z['binding']==binding
    return z['data']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True); a=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1024*1048576,)*2)
    start=time.monotonic(); r=a.root
    out=r/'original-two-round-complete210-sources127-v2'
    md={'bytes':121269,'sha256':'965d7980bcd7d95bebb353371fe78f78f460f1d526b2c0dda64492ae366130e8'}
    mf=json.loads(checked(out/'mean120-complete210-sources-manifest.json',md))
    binding='41638323f597133aadeb65b2a1639899a162e2afbe6e7f7c477e93fae912cd80'
    assert mf['binding']==binding
    assert digest(json.dumps(mf['semantic'],sort_keys=True,separators=(',',':'),ensure_ascii=True).encode())==binding
    base_desc={'bytes':776254,'sha256':'5cbba4f798ab95fe24538f35d23d4b3a2f0d6197ee3ed33f3149b7371b0d222c','logicalBytes':4442756,'logicalSha256':'f07c273c934e671f5e1069954771286c14e5d10ab7c4652d998a02f71beb7d05','path':'complete-original-ten-parameter-action127.json.gz'}
    assert mf['parentMathematics']['base']==base_desc
    base=phase(r/'original-ten-parameter-module127-v2',base_desc,'7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4')
    ctx=fmpz_mod_mpoly_ctx.get([f'x{i}' for i in range(17)],127)
    def poly(p):
        assert all(len(e)==17 and all(type(i) is int and i>=0 for i in e) and type(c) is int and 0<c<127 for e,c in p)
        assert len({tuple(e) for e,c in p})==len(p)
        return ctx.from_dict({tuple(e):c for e,c in p})
    def vec(v):return [poly(p) for p in v]
    def dot(v,w):return sum((x*y for x,y in zip(v,w)),ctx.constant(0))
    def wt(e):return sum(e[:6])+2*sum(e[6:])
    A=vec(base['allOriginal18Generators'])
    N=[[vec(row) for row in op] for op in base['allFiveOriginalParameterMatrices']]
    S=[[vec(row) for row in op] for op in base['allFiveOriginalBorderSourceMatrices']]
    degrees=[]
    for p in base['allOriginal18Generators'][:17]:
        ws={wt(e) for e,c in p}; assert len(ws)==1
        degrees.append(next(iter(ws)))
    assert sorted(degrees)==[4]*11+[5]*6
    monexp=[[0]*5]+[[int(j==i) for j in range(5)] for i in range(5)]
    monexp += [[int(i==p)+int(i==q) for i in range(5)] for p,q in [(1,4),(2,3),(2,4),(3,4)]]
    assert base['tenOriginalMonomials']==monexp
    M=[ctx.from_dict({tuple([0]*12+e):1}) for e in monexp]
    weights=[0]+[2]*5+[4]*4; U=ctx.gens()[12:]
    phase(out,mf['phases']['complete-original106-parent-validation'],binding)
    expected=[f'second-mean-p{p}-q{q}-seed{sid:03d}' for p,q in [(1,4),(2,3),(2,4),(3,4)] for sid in range(100,106)]
    assert set(mf['phases'])==set(expected)|{'complete-original106-parent-validation'}
    jobs={j['phaseKey']:j for j in mf['parentMathematics']['new104']}
    vt=st=stored=logical=0; first_cache={}
    for key in expected:
        d=mf['phases'][key]; z=phase(out,d,binding); job=jobs[key]
        assert z['literalSource']==job and job['family']=='mean' and job['weight']==9
        p,q=job['orderedOperators']; rr=job['firstImage']; firstkey=rr['phaseKey']
        assert firstkey==f'frontier-i{q}-mean{job["originalSeedIndex"]-100}'
        assert rr['parent']=='mean' and rr['binding']=='9502b11bf94390e8833cdc236a1ad85746d9823f9f4fe1e62de60f1932434bfd'
        if firstkey not in first_cache:
            f=phase(r/'original-mean-first-frontier127',rr['descriptor'],rr['binding'])
            first_cache[firstkey]=(vec(f['vector']),vec(f['original18Source']))
        v1,s1=first_cache[firstkey]; v=vec(z['vector']); s=vec(z['original18Source'])
        assert len(v)==10 and len(s)==18 and not s[17]
        assert v==[dot(row,v1) for row in N[p]]
        assert s==[U[p]*s1[i]-dot(S[p][i],v1) for i in range(18)]
        assert dot(M,v)==dot(A,s)
        for i,polydata in enumerate(z['vector']):
            assert all(not any(e[12:]) and wt(e)+weights[i]==9 for e,c in polydata)
        for i,polydata in enumerate(z['original18Source'][:17]):
            assert all(wt(e)+degrees[i]==9 for e,c in polydata)
        assert max((sum(e[12:]) for polydata in z['original18Source'] for e,c in polydata),default=0)==z['sourceMaximumUDegree']==2
        av=sum(map(len,z['vector'])); ass=sum(map(len,z['original18Source']))
        assert av==z['vectorTerms'] and ass==z['sourceTerms']
        vt+=av;st+=ass;stored+=d['bytes'];logical+=d['logicalBytes']
    result={'format':'isp-root-complete210-mean-source-independent-audit-v1','binding':binding,'manifest':md,'columns':24,'wholeNewTenCoordinateRecurrences':240,'wholeNewEighteenSourceRecurrences':432,'wholeOriginalPolynomialProducts':24,'newPhaseHashesVerified':24,'parentValidationPhaseHashVerified':True,'allNewSourcesHomogeneousWeight9':True,'original17GeneratorWeights':degrees,'newVectorTerms':vt,'newSourceTerms':st,'newPhaseBytes':stored,'newPhaseLogicalBytes':logical,'noProducerImport':True,'elapsedSeconds':time.monotonic()-start,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'status':'passed'}
    a.out.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__':main()
