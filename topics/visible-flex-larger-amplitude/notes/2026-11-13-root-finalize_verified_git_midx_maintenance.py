#!/usr/bin/env python3
"""Verify all MIDX-selected objects, give the selected old pack a stable name,
rebuild the derived index, and verify complete original OID/ref preservation.
No Git object content, commit, reference, or scientific file is changed.
"""
from pathlib import Path
import json,hashlib,struct,subprocess,time,shutil
B=Path('/workspace/scratch/d1aa462cfc02');R=B/'math-research';P=R/'.git/objects/pack'
old=json.loads((B/'git_midx_maintenance_20261113T1334-before.json').read_text());saved=(B/'git_midx_maintenance_20261113T1334-oids.bin').read_bytes()
def refs():return subprocess.check_output(['git','for-each-ref','--format=%(refname) %(objectname)'],cwd=R,text=True)
def all_oids():
    ids=set();records=[]
    for idx in sorted(P.glob('*.idx')):
        raw=idx.read_bytes();assert raw[:8]==b'\xfftOc\0\0\0\x02';assert hashlib.sha1(raw[:-20]).digest()==raw[-20:]
        n=struct.unpack('>I',raw[1028:1032])[0];oid=[raw[1032+i*20:1052+i*20] for i in range(n)]
        assert len(set(oid))==n and oid==sorted(oid);pack=idx.with_suffix('.pack')
        with pack.open('rb') as f:f.seek(-20,2);assert f.read(20)==raw[-40:-20]
        ids.update(oid);records.append({'index':idx.name,'objects':n,'pack_bytes':pack.stat().st_size,'index_sha256':hashlib.sha256(raw).hexdigest(),'pack_trailer_sha1':raw[-40:-20].hex()})
    raw=b''.join(sorted(ids));assert raw==saved,'Complete original OID set must be byte-identical'
    assert refs()==old['refs_before']
    return {'count':len(ids),'oid_sha256':hashlib.sha256(raw).hexdigest(),'records':records,'refs_exactly_unchanged':True}
report={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'started_utc':time.strftime('%FT%TZ',time.gmtime()),'before':all_oids(),'renames':[],'commands':[]}
out=B/'git_midx_maintenance_20261113T1347-final.json'
def save():out.write_text(json.dumps(report,indent=2)+'\n')
save();stem='.tmp-35-pack-585608d86dba09797a031e76a1c7fc46ed87b7ef';stable='pack-585608d86dba09797a031e76a1c7fc46ed87b7ef'
for src in sorted(P.glob(stem+'.*')):
    assert src.suffix in ['.pack','.idx','.rev','.bitmap','.promisor']
    dst=P/(stable+src.suffix);assert not dst.exists();st=src.stat();src.rename(dst);now=dst.stat()
    assert (st.st_dev,st.st_ino,st.st_size,st.st_mtime_ns)==(now.st_dev,now.st_ino,now.st_size,now.st_mtime_ns)
    report['renames'].append({'from':src.name,'to':dst.name,'same_inode_size_mtime':True,'bytes':now.st_size});save()
report['after_pack_name_stabilization']=all_oids();save()
midx=P/'multi-pack-index';backup=B/'git_midx_20261113T1347-derived-index-before-stable-names.bin';assert not backup.exists();midx.rename(backup)
commands=[(['git','multi-pack-index','write','--preferred-pack='+stable+'.pack','--stdin-packs'],('\n'.join(p.name for p in sorted(P.glob('pack-*.idx')))+'\n').encode()),(['git','multi-pack-index','verify'],None)]
for command,data in commands:
    start=time.monotonic();r=subprocess.run(command,cwd=R,input=data,capture_output=True)
    report['commands'].append({'command':command,'exitcode':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':r.stdout.decode(),'stderr':r.stderr.decode()});save();assert r.returncode==0,report['commands'][-1]
report['after']=all_oids();report['free_after']=shutil.disk_usage(B).free;report['pack_bytes_after']=sum(x['pack_bytes'] for x in report['after']['records']);report['all_original_object_bytes_preserved']=True;report['formal_success']=True;report['completed_utc']=time.strftime('%FT%TZ',time.gmtime());save()
print(json.dumps({k:report[k] for k in ['formal_success','pack_bytes_after','free_after','completed_utc']}),flush=True)
print('OID_COUNT',report['after']['count'],'OID_SHA',report['after']['oid_sha256'],'REFS_UNCHANGED',report['after']['refs_exactly_unchanged'],flush=True)
