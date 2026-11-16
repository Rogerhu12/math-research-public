#!/usr/bin/env python3
"""Independent original-200 binary/ASCII transport audit. All arrays stay TMP.
OpenAI ChatGPT /root, GPT-6 Astra Pro, 2026-11-16.
"""
import argparse,gc,gzip,hashlib,itertools,json,math,os,re,resource,signal,struct,time
from pathlib import Path
from flint import fmpz_mod_mpoly_ctx

def sha(b):return hashlib.sha256(b).hexdigest()
def checked(p,d):
    b=p.read_bytes();assert len(b)==d['bytes'] and sha(b)==d['sha256'],str(p)
    return b
def phase(root,d,binding):
    b=gzip.decompress(checked(root/d['path'],d))
    assert len(b)==d['logicalBytes'] and sha(b)==d['logicalSha256']
    j=json.loads(b);assert j['binding']==binding
    return j['data']
def vector_phase(root,d,binding):
    raw=gzip.decompress(checked(root/d['path'],d))
    assert len(raw)==d['logicalBytes'] and sha(raw)==d['logicalSha256']
    assert raw.startswith(('{"binding":"'+binding+'","data":{').encode('ascii'))
    text=raw.decode('ascii');needle='"vector":'
    assert text.count(needle)==1
    v,end=json.JSONDecoder().raw_decode(text,text.index(needle)+len(needle))
    assert len(v)==10
    return v

def code(row,e):return row+sum(x<<(4+5*i) for i,x in enumerate(e))
def decode(p,d,binding):
    b=gzip.decompress(checked(p,d));assert len(b)==d['logicalBytes'] and sha(b)==d['logicalSha256']
    assert b[:8]==b'R15ZGV01' and struct.unpack_from('<3I',b,8)==(1,10,12)
    assert b[24:88].decode()==binding
    degree=struct.unpack_from('<I',b,20)[0];n=struct.unpack_from('<Q',b,88)[0]
    assert degree==d['degree'] and n==d['terms'] and len(b)==96+9*n
    terms=[struct.unpack_from('<QB',b,96+9*i) for i in range(n)]
    assert terms==sorted(terms) and len(dict(terms))==n
    return terms
FACTOR=re.compile(r'([yw])([0-5])(?:\^([1-9][0-9]*))?\Z')
def polynomial(body,row):
    if body=='0':return {}
    shift=([0]+[2]*5+[4]*4)[row]
    if shift:
        prefix=f'zz^{shift}*(';assert body.startswith(prefix) and body.endswith(')')
        body=body[len(prefix):-1]
    assert body and 'zz' not in body
    ans={}
    for term in body.split('+'):
        parts=term.split('*');c=int(parts[0]);assert 0<c<127
        e=[0]*12
        for f in parts[1:]:
            m=FACTOR.fullmatch(f);assert m,f
            i=int(m[2])+(6 if m[1]=='w' else 0);power=int(m[3] or 1)
            assert e[i]==0 and 1<=power<=10
            e[i]=power
        t=code(row,e);assert t not in ans
        ans[t]=c
    return ans

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(1024*1048576,)*2);signal.alarm(360);start=time.monotonic()
    out=Path('/tmp/literature_bell_rank4_789f/original-delta-weight10-homogeneous127-v2')
    base=Path('/tmp/r150-normal-789f-20261116-1040')
    md={'bytes':410173,'sha256':'d6d4a4921c8b874def17e3de84db64c6fa9716cf9ea173a7207e8538f54b41c5'}
    mf=json.loads(checked(out/'delta-weight10-manifest.json',md));binding='dfb2420829d6b6243142e1232e4c2bdba4fa45fb1823fe81d119c4101493e488'
    assert mf['binding']==binding and sha(json.dumps(mf['semantic'],sort_keys=True,separators=(',',':'),ensure_ascii=True).encode())==binding
    assert len(mf['prepared'])==len(mf['originalReferences'])==200
    roots={'model':base/'original-ten-parameter-module127-v2','mean':base/'original-mean-first-frontier127','weight8':base/'original-complete-weight8-frontier127','producer':base/'original-two-round-complete210-sources127-v2'}
    checkpoint=Path('/tmp/isp-root-delta10-input-export-audit-v2-progress.json')
    source_sha=sha(Path(__file__).read_bytes())
    progress={'sourceSHA256':source_sha,'binding':binding,'inputManifest':md,'next':0,'termCount':0,'asciiBytes':0,'weights':{},'chainSHA256':sha(b'root-complete200-export-v2')}
    if checkpoint.exists():
        progress=json.loads(checkpoint.read_bytes())
        assert progress['sourceSHA256']==source_sha and progress['binding']==binding and progress['inputManifest']==md
        for k in range(progress['next']):
            item=mf['prepared'][k];rr=mf['originalReferences'][k]['origin']
            checked(out/item['vector']['path'],item['vector'])
            checked(out/item['ascii']['path'],item['ascii'])
            checked(roots[rr['parent']]/rr['descriptor']['path'],rr['descriptor'])
    term_count=progress['termCount'];ascii_bytes=progress['asciiBytes'];weights={int(k):v for k,v in progress['weights'].items()}
    for i in range(progress['next'],200):
        item=mf['prepared'][i]
        ref=mf['originalReferences'][i];assert item['originalReference']==ref
        rr=ref['origin'];original_vector=vector_phase(roots[rr['parent']],rr['descriptor'],rr['binding'])
        expected={}
        for row,terms in enumerate(original_vector):
            for e,c in terms:
                assert len(e)==17 and not any(e[12:]) and 0<c<127
                assert sum(e[:6])+2*sum(e[6:12])+([0]+[2]*5+[4]*4)[row]==ref['weight']
                t=code(row,e[:12]);assert t not in expected
                expected[t]=c
        got=decode(out/item['vector']['path'],item['vector'],binding)
        assert got==sorted(expected.items()) and item['vector']['degree']==ref['weight']
        raw=checked(out/item['ascii']['path'],item['ascii']);lines=raw.decode('ascii').splitlines();assert len(lines)==10
        parsed={}
        for row,line in enumerate(lines):
            head=f'OM[{row+1},{i+1}]=';assert line.startswith(head) and line.endswith(';')
            parsed.update(polynomial(line[len(head):-1],row))
        assert parsed==expected
        term_count+=len(expected);ascii_bytes+=len(raw);weights[ref['weight']]=weights.get(ref['weight'],0)+1
        progress.update(next=i+1,termCount=term_count,asciiBytes=ascii_bytes,weights=weights)
        progress['chainSHA256']=sha(bytes.fromhex(progress['chainSHA256'])+json.dumps({'index':i,'original':rr['descriptor']['sha256'],'binary':item['vector']['sha256'],'ascii':item['ascii']['sha256'],'allProducts':True},sort_keys=True,separators=(',',':')).encode())
        tmp=checkpoint.with_suffix('.tmp');tmp.write_text(json.dumps(progress,sort_keys=True,separators=(',',':')));os.replace(tmp,checkpoint)
        del original_vector,expected,got,raw,lines,parsed,terms
        if (i+1)%10==0:
            gc.collect()
            print(json.dumps({'completeOriginalColumns':i+1,'elapsedSeconds':time.monotonic()-start,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    assert weights=={5:6,6:20,7:30,8:40,9:24,10:80}
    assert term_count==8037189 and ascii_bytes==151071880
    bd={'bytes':776254,'sha256':'5cbba4f798ab95fe24538f35d23d4b3a2f0d6197ee3ed33f3149b7371b0d222c','logicalBytes':4442756,'logicalSha256':'f07c273c934e671f5e1069954771286c14e5d10ab7c4652d998a02f71beb7d05','path':'complete-original-ten-parameter-action127.json.gz'}
    original=phase(roots['model'],bd,'7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4')
    ctx=fmpz_mod_mpoly_ctx.get([f'x{i}' for i in range(12)],127)
    def poly(p):
        assert all(not any(e[12:]) for e,c in p)
        return ctx.from_dict({tuple(e[:12]):c for e,c in p})
    mat=[[poly(original['allSixOriginalMeanColumns'][j][6+i]) for j in (2,3,4,5)] for i in range(4)]
    delta=ctx.constant(0)
    for perm in itertools.permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        product=ctx.constant((-1)**inversions)
        for i in range(4):product*=mat[i][perm[i]]
        delta+=product
    x=ctx.gens();bell=sum((x[i]*x[i+6] for i in range(6)),ctx.constant(0));target=delta*bell**2
    target_terms={code(0,tuple(map(int,e))):int(c) for e,c in target.to_dict().items()}
    assert len(target_terms)==2604 and len(delta.to_dict())==124
    actual_target=decode(out/mf['target']['path'],mf['target'],binding)
    assert actual_target==sorted(target_terms.items()) and mf['target']['degree']==10
    text=checked(out/mf['targetASCII']['path'],mf['targetASCII']).decode('ascii').strip()
    prefix='matrix TM[10][1]; TM[1,1]=';suffix='; module Target=TM;'
    assert text.startswith(prefix) and text.endswith(suffix)
    assert polynomial(text[len(prefix):-len(suffix)],0)==target_terms
    result={'format':'isp-root-original200-weight10-export-independent-audit-v2','binding':binding,'inputManifest':md,'completeOriginalColumns':200,'originalParameterTerms':term_count,'all2000BinaryAndASCIICoordinatesMatchOriginalPhases':True,'completeASCIIBytes':ascii_bytes,'weightCounts':weights,'independentDeltaTerms':124,'independentTargetTerms':2604,'literalTargetBinaryAndASCIIMatch':True,'producerOrVerifierImported':False,'originalPolynomialProductsNotRepeated':True,'originalSourceArraysNotDecoded':True,'completePrefixChainSHA256':progress['chainSHA256'],'elapsedSeconds':time.monotonic()-start,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'status':'passed'}
    a.out.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n');print(json.dumps(result,sort_keys=True))
if __name__=='__main__':main()
