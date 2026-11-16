#!/usr/bin/env python3
"""Recreate only the frozen 24-stage zero-dual parent prefix, then stop.
AI-assisted, 2026-11-16. The parent source, its binding and all phase contents
are unchanged. A verified finite-field-row-profile write is the sole stop hook.
No whole finite rational RREF is entered. Existing complete prefix is read-only.
"""
import argparse,gzip,hashlib,importlib.util,json,resource,signal,time,sys
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SOURCE_SHA='45b01f0206d7c74832e91602e40854728a7e376df860f2f6ad17f35b61084e4b'
BINDING='9131c2f4dd530684bbc9f8f7c9005c1365de72cb170492bbdc1073f2c6a53a8a'
MANIFEST_SHA='215d279bd8a145983ca0d1507cf9fa8c4be4d68139622436008dffc331aaa7c4'
NAMES={'constant-profile','finite-field-row-profile'}|{f'{p}-{k:02d}' for p in ('unit-solution','full-schur') for k in range(11)}
class PrefixComplete(Exception):pass
def req(x,s):
    if not x:raise AssertionError(s)
def sha(b):return hashlib.sha256(b).hexdigest()
def fsha(p,compressed=False):
    h=hashlib.sha256()
    with (gzip.open(p,'rb') if compressed else open(p,'rb')) as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()
def inventory(root):
    b=(root/'manifest.json').read_bytes();req(len(b)==7555 and sha(b)==MANIFEST_SHA,'Exact original 24-stage manifest')
    m=json.loads(b);req(m['binding']==BINDING and set(m['phases'])==NAMES,'Exact original prefix binding and phase set')
    total=0
    for name,z in m['phases'].items():
        req(z['verified'],'Only verified original parent phases')
        p=root/z['file'];req(p.stat().st_size==z['bytes'] and fsha(p)==z['sha256'],'All original compressed bytes '+name)
        req(fsha(p,True)==z['payloadSHA256'],'All original decompressed bytes '+name);total+=z['bytes']
    return {'bytes':len(b),'sha256':sha(b),'phaseCount':len(m['phases']),'temporaryCompressedBytes':total}
def main():
    ar=argparse.ArgumentParser()
    for x in ('parent-source','generator','actions','original-tenth-receipt','out'):ar.add_argument('--'+x,required=True)
    ar.add_argument('--seconds',type=int,default=600);ar.add_argument('--memory-mib',type=int,default=4096);a=ar.parse_args()
    root=Path(a.out)/'checkpoints';start=time.monotonic();req(fsha(a.parent_source)==SOURCE_SHA,'Exact frozen mathematical producer')
    spec=importlib.util.spec_from_file_location('frozen_zero_dual_producer',a.parent_source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1024**2,a.memory_mib*1024**2));signal.signal(signal.SIGALRM,m.stop);signal.signal(signal.SIGTERM,m.stop);signal.alarm(a.seconds)
    code=0;result={'format':'r150-zero-dual-prefix-reproduction-v1','status':'started','parentBinding':BINDING,'parentSourceSHA256':SOURCE_SHA,'sourceSHA256':fsha(__file__)}
    try:
        if root.joinpath('manifest.json').exists() and sha(root.joinpath('manifest.json').read_bytes())==MANIFEST_SHA:
            result['mode']='verify-existing-immutable-prefix'
        else:
            result['mode']='reconstruct-prefix-with-original-source'
            original_put=m.Cache.put
            def put(self,name,value,verified):
                original_put(self,name,value,verified)
                if name=='finite-field-row-profile':
                    req(verified,'The exact original profile must already be verified')
                    raise PrefixComplete()
            m.Cache.put=put
            try:m.run(a,{'format':m.FORMAT,'status':'started','parameters':{}},start)
            except PrefixComplete:pass
            else:raise AssertionError('Original 24-stage stop hook was not reached')
        result['inventory']=inventory(root);result['status']='completed-verified-prefix'
    except m.BudgetStop as e:result.update(status='budget-checkpoint',errorType=type(e).__name__,errorMessage=str(e));code=75
    except Exception as e:result.update(status='failed',errorType=type(e).__name__,errorMessage=str(e));code=1
    finally:
        signal.alarm(0);result.update(exitCode=code,elapsedSeconds=time.monotonic()-start,peakResidentKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        Path(a.out).mkdir(parents=True,exist_ok=True);p=Path(a.out)/'zero-dual-prefix-reproduction-receipt.json'
        p.write_text(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n')
        print(json.dumps(result,sort_keys=True),flush=True)
    raise SystemExit(code)
if __name__=='__main__':main()
