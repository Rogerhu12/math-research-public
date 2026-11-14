#!/usr/bin/env python3
"""Small canonical MIDX repacks under the sole publisher's exclusive Git ownership.
All current indexed objects and ref tips must remain exactly unchanged.
"""
from pathlib import Path
import argparse,json,hashlib,struct,subprocess,time,shutil,os,signal

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out-prefix',type=Path,required=True);ap.add_argument('--target-free',type=int,default=8*1024**3);ap.add_argument('--max-batches',type=int,default=12);a=ap.parse_args()
    B=Path('/workspace/scratch/d1aa462cfc02');R=B/'math-research';P=R/'.git/objects/pack';out=Path(str(a.out_prefix)+'-report.json')
    assert not out.exists()
    assert not (R/'.git/index.lock').exists() and not (R/'.git/rebase-merge').exists() and not (R/'.git/rebase-apply').exists()
    def refs():return subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)'],cwd=R,text=True)
    def inventory():
        ids=set();rows=[]
        for idx in sorted(P.glob('*.idx')):
            raw=idx.read_bytes();assert raw[:8]==b'\xfftOc\0\0\0\x02';assert hashlib.sha1(raw[:-20]).digest()==raw[-20:]
            n=struct.unpack('>I',raw[1028:1032])[0];oid=[raw[1032+i*20:1052+i*20] for i in range(n)]
            assert len(set(oid))==n and oid==sorted(oid)
            pack=idx.with_suffix('.pack')
            with pack.open('rb') as f:f.seek(-20,2);assert f.read(20)==raw[-40:-20]
            ids.update(oid);rows.append({'index':idx.name,'objects':n,'pack_bytes':pack.stat().st_size,'index_sha256':hashlib.sha256(raw).hexdigest(),'pack_trailer_sha1':raw[-40:-20].hex()})
        return b''.join(sorted(ids)),rows
    baseline,rows=inventory();initial_refs=refs()
    report={'schema':'sole-publisher-canonical-small-pack-maintenance-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'start_utc':time.strftime('%FT%TZ',time.gmtime()),'initial_refs':initial_refs,'initial_inventory':rows,'original_oid_count':len(baseline)//20,'original_oid_sha256':hashlib.sha256(baseline).hexdigest(),'free_before':shutil.disk_usage(B).free,'steps':[],'renames':[]}
    def save():out.write_text(json.dumps(report,indent=2)+'\n')
    def check():
        ids,rs=inventory();assert ids==baseline,'The complete indexed OID union changed';assert refs()==initial_refs,'Refs changed during pack maintenance'
        return {'pack_count':len(rs),'pack_bytes':sum(x['pack_bytes'] for x in rs),'oid_count':len(ids)//20,'oid_sha256':hashlib.sha256(ids).hexdigest(),'all_original_oid_bytes_and_ref_tips_identical':True,'free_bytes':shutil.disk_usage(B).free}
    def run(args,label,data=None):
        command=['git','-c','pack.threads=1','-c','pack.window=0',*args];start=time.monotonic();log=Path(str(a.out_prefix)+'-'+label+'.log')
        with log.open('xb') as stream:
            child=subprocess.Popen(command,cwd=R,stdin=subprocess.PIPE if data is not None else None,stdout=stream,stderr=subprocess.STDOUT,start_new_session=True)
            if data is not None:child.stdin.write(data);child.stdin.close()
            cancelled=False
            while child.poll() is None:
                if shutil.disk_usage(B).free<400*1024**2:
                    os.killpg(child.pid,signal.SIGTERM);cancelled=True;break
                time.sleep(.5)
            code=child.wait()
        rec={'command':command,'exitcode':code,'wall_seconds':time.monotonic()-start,'disk_reserve_cancelled':cancelled,'log':str(log),'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),'free_after':shutil.disk_usage(B).free};report['steps'].append(rec);save();print(json.dumps(rec),flush=True)
        if code or cancelled:raise RuntimeError('Canonical Git command failed; stop before further object-store mutations')
    # Some inherited auto-GC packs have a temporary basename but are real MIDX
    # members. Stabilize their names without changing inode/content.
    for idx in sorted(P.glob('.tmp-*-pack-*.idx')):
        stable='pack-'+idx.name.split('-pack-',1)[1].removesuffix('.idx');source_stem=idx.stem
        if (P/(stable+'.idx')).exists():continue
        for src in sorted(P.glob(source_stem+'.*')):
            assert src.suffix in ['.pack','.idx','.rev','.bitmap','.promisor']
            dst=P/(stable+src.suffix);assert not dst.exists();st=src.stat();src.rename(dst);after=dst.stat()
            assert (st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns)
            report['renames'].append({'from':src.name,'to':dst.name,'same_inode_size_mtime':True})
    report['before_midx_write']=check();save()
    # MIDX is a reproducible cache. Preserve an exact backup and rebuild from
    # the current complete inventory, avoiding references to absent old names.
    midx=P/'multi-pack-index'
    if midx.exists():
        backup=Path(str(a.out_prefix)+'-prior-midx.bin');assert not backup.exists();midx.rename(backup)
        report['prior_midx_backup']={'path':str(backup),'sha256':hashlib.sha256(backup.read_bytes()).hexdigest()};save()
    _,current=inventory();preferred=max(current,key=lambda x:x['objects'])['index'].removesuffix('.idx')+'.pack'
    data=('\n'.join(x['index'] for x in current)+'\n').encode()
    run(['multi-pack-index','write','--preferred-pack='+preferred,'--stdin-packs'],'write',data)
    run(['multi-pack-index','verify'],'verify-before')
    run(['multi-pack-index','expire'],'expire-initial');prior=check();report['initial_expire_verification']=prior;save()
    for i in range(a.max_batches):
        if shutil.disk_usage(B).free>=a.target_free:break
        # Git only collects packs smaller than batch-size. A fixed10MB bound
        # cannot consume today's100MB+ fetched packs. Keep a conservative
        # disk reserve while allowing canonical consolidation of those packs.
        free=shutil.disk_usage(B).free
        batch_size=min(1024**3,max(16*1024**2,(free-800*1024**2)//3))
        report.setdefault('declared_batch_sizes',[]).append(batch_size);save()
        run(['multi-pack-index','repack','--batch-size='+str(batch_size)],f'batch{i:02d}-repack')
        run(['multi-pack-index','expire'],f'batch{i:02d}-expire')
        after=check();report.setdefault('batch_verifications',[]).append(after);save();print(json.dumps(after),flush=True)
        if after['pack_bytes']>=prior['pack_bytes'] and after['pack_count']>=prior['pack_count']:break
        prior=after
    run(['multi-pack-index','verify'],'verify-after');report['final']=check();report['formal_success']=True;report['end_utc']=time.strftime('%FT%TZ',time.gmtime());save();print(json.dumps(report['final']),flush=True)
if __name__=='__main__':main()
