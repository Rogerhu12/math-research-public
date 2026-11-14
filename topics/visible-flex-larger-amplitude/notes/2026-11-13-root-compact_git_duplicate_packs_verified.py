#!/usr/bin/env python3
"""Canonical small MIDX batches, preserving the complete registered OID union."""
from pathlib import Path
import subprocess,json,hashlib,struct,time,os,signal,shutil
B=Path('/workspace/scratch/d1aa462cfc02');R=B/'math-research';P=R/'.git/objects/pack'
BASE=B/'git_midx_maintenance_20261113T1334-before.json'
before=json.loads(BASE.read_text());saved=(B/'git_midx_maintenance_20261113T1334-oids.bin').read_bytes()
assert len(saved)==20*before['unique_oid_count_before']
assert hashlib.sha256(saved).hexdigest()==before['sorted_oid_sha256_before']
def refs():return subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)'],cwd=R,text=True)
assert refs()==before['refs_before']
assert not (R/'.git/index.lock').exists() and not (R/'.git/rebase-merge').exists() and not (R/'.git/rebase-apply').exists()
assert (B/'publisher_quiesced_20261113T1328.json').exists()
report={'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'refs_before':before['refs_before'],'oid_count_before':before['unique_oid_count_before'],'oid_sha256_before':before['sorted_oid_sha256_before'],'steps':[],'free_before':shutil.disk_usage(B).free,'started_utc':time.strftime('%FT%TZ',time.gmtime())}
out=B/'git_midx_maintenance_20261113T1337-report.json'
def save():out.write_text(json.dumps(report,indent=2)+'\n')
def run(args,label):
    start=time.monotonic();log=B/('git_midx_20261113T1337-'+label+'.log')
    command=['git','-c','pack.threads=1','-c','pack.window=0',*args]
    with log.open('xb') as f:
        child=subprocess.Popen(command,cwd=R,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
        aborted=False
        while child.poll() is None:
            if shutil.disk_usage(B).free<400*1024*1024:
                os.killpg(child.pid,signal.SIGTERM);aborted=True;break
            time.sleep(1)
        code=child.wait()
    rec={'command':command,'exitcode':code,'aborted_for_disk_reserve':aborted,'wall_seconds':time.monotonic()-start,'log':str(log),'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest(),'free_after':shutil.disk_usage(B).free}
    report['steps'].append(rec);save();print(json.dumps(rec),flush=True)
    if code or aborted:raise RuntimeError('Owned canonical Git command did not complete; original pack data retained')
def union():
    ids=set();records=[]
    for idx in sorted(P.glob('pack-*.idx')):
        raw=idx.read_bytes();assert raw[:8]==b'\xfftOc\0\0\0\x02'
        assert hashlib.sha1(raw[:-20]).digest()==raw[-20:]
        n=struct.unpack('>I',raw[1028:1032])[0];oid=[raw[1032+i*20:1052+i*20] for i in range(n)]
        assert len(set(oid))==n and oid==sorted(oid)
        pack=idx.with_suffix('.pack')
        with pack.open('rb') as f:f.seek(-20,2);assert f.read(20)==raw[-40:-20]
        ids.update(oid);records.append({'pack':pack.name,'objects':n,'bytes':pack.stat().st_size,'index_sha256':hashlib.sha256(raw).hexdigest()})
    current=b''.join(sorted(ids));assert current==saved,'Registered object union changed'
    assert refs()==before['refs_before'],'A reference changed during owned pack maintenance'
    return {'registered_pack_count':len(records),'pack_bytes':sum(x['bytes'] for x in records),'oid_count':len(ids),'oid_sha256':hashlib.sha256(current).hexdigest(),'all_oid_bytes_and_refs_exactly_unchanged':True,'free_bytes':shutil.disk_usage(B).free}
run(['multi-pack-index','write','--preferred-pack=pack-1beac3da7406801423b2119401a37f696f3c4881.pack'],'write')
run(['multi-pack-index','verify'],'verify-before')
run(['multi-pack-index','expire'],'expire-initial')
report['initial_verification']=union();save();print(json.dumps(report['initial_verification']),flush=True)
for i in range(12):
    if shutil.disk_usage(B).free>=8*1024**3:break
    run(['multi-pack-index','repack','--batch-size=10000000'],f'batch{i:02d}-repack')
    run(['multi-pack-index','expire'],f'batch{i:02d}-expire')
    check=union();report.setdefault('batch_verifications',[]).append(check);save();print(json.dumps(check),flush=True)
run(['multi-pack-index','verify'],'verify-after')
report['final_verification']=union();report['completed_utc']=time.strftime('%FT%TZ',time.gmtime());report['formal_success']=True;save();print(json.dumps(report['final_verification']),flush=True)
