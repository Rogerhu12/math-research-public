#!/usr/bin/env python3
"""Verify and sparsely evict 66 recoverable old copies, then start true M14.

Every payload remains in a decoded-and-hashed local published Git object.
Only historical unmodified f64 copies are removed; no Git object is removed.
The numerical argv is the already-reviewed true-M14 guard launch, unchanged.
"""
import hashlib, json, os, shutil, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone

root=Path(__file__).resolve().parents[3];topic=root/'topics/visible-flexible-closed-surface';n=topic/'notes';s=topic/'scripts';pre='2026-11-09-db6f-'
def identity(p):
 p=Path(p).resolve();b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(row): assert identity(row['path'])==row,row['path']
def git(*args,data=None):
 env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_OPTIONAL_LOCKS='0')
 assert 'GIT_INDEX_FILE' not in env
 r=subprocess.run(['/usr/bin/git','-c','protocol.allow=never','-c','remote.origin.promisor=false','-c','core.fsmonitor=false','-c','gc.auto=0','-C',str(root),*args],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env)
 if r.returncode:raise RuntimeError('offline git '+args[0]+' exit '+str(r.returncode))
 return r.stdout

def main():
 manifests=[];rows=[]
 for name,sha,count in [('prefix-historical-data-recovery-candidates-01.json','cfc440e00797e6c68bbb3cb78077757f20d8bfa1f0f7902f594581f1b40c45c7',42),('root-additional-history-recovery-candidates.json','13e3da3d9e5361604e1ab299193513fff4fa068203e9ca35ccee0c258795c175',24)]:
  p=n/(pre+name);assert identity(p)['sha256']==sha;d=json.loads(p.read_text());assert len(d['files'])==count;rows+=d['files'];manifests.append(identity(p))
 paths=[r['path'] for r in rows];assert len(paths)==len(set(paths))==66
 assert all(p.startswith('topics/visible-flexible-closed-surface/notes/') and p.endswith('.f64.gz') for p in paths)
 launch=n/(pre+'root-spectral-true-m14q512-01-guard-launch.json')
 assert identity(launch)['sha256']=='e47b15876602732ffaadc15322cc7120b0ad560a1cd1abe659397e9383ca58a2'
 protected=set()
 for p in (launch,n/(pre+'root-linear-dn-pilot-v2-01-guard-launch.json'),n/(pre+'root-spectral-affine-m14q512-01-guard-launch.json')):
  d=json.loads(p.read_text())
  for r in d['bound_files']:verify(r);protected.add(str(Path(r['path']).resolve()))
 assert all(str(root/p) not in protected for p in paths)
 head=git('rev-parse','HEAD').decode().strip();assert head=='382f1aa79513f197500e5548f030ee747e7fdcec'
 anchor='fc197d3124c291d6da5e4ba496a123316fe31a83'
 trees=[]
 for ref in (head,anchor):
  tree={}
  for item in git('ls-tree','-rz','--full-tree',ref,'--',*paths).split(b'\0'):
   if item:
    meta,path=item.split(b'\t',1);mode,kind,oid=meta.decode().split();assert kind=='blob';tree[path.decode()]=(mode,oid)
  trees.append(tree)
 index={}
 for item in git('ls-files','--stage','-z','--',*paths).split(b'\0'):
  if item:
   meta,path=item.split(b'\t',1);mode,oid,stage=meta.decode().split();assert stage=='0';index[path.decode()]=(mode,oid)
 assert not git('status','--porcelain=v1','-z','--',*paths)
 before=shutil.disk_usage(root).free;snapshots={}
 for row in rows:
  path=row['path'];expected=(row['mode'],row['git_blob_sha1'])
  assert trees[0][path]==trees[1][path]==index[path]==expected
  payload=git('cat-file','blob',row['git_blob_sha1'])
  assert len(payload)==row['bytes'] and hashlib.sha256(payload).hexdigest()==row['sha256']
  assert hashlib.sha1(b'blob '+str(len(payload)).encode()+b'\0'+payload).hexdigest()==row['git_blob_sha1']
  p=root/path
  if p.exists():
   assert p.is_file() and not p.is_symlink() and p.stat().st_nlink==1
   assert identity(p)['sha256']==row['sha256'] and p.stat().st_size==row['bytes']
   snapshots[path]=(p.stat().st_ino,p.stat().st_mtime_ns,p.stat().st_size)
 out=n/(pre+'root-true-m14-66-worktree-start-observed.json');assert not out.exists()
 record={'status':'ALL_RECOVERY_GATES_PASSED_BEFORE_MUTATION','recorded_utc':datetime.now(timezone.utc).isoformat(),'launcher':identity(__file__),'manifests':manifests,'current_head':head,'published_anchor':anchor,'guard_launch':identity(launch),'protected_unique_paths_rehashed':len(protected),'file_count':66,'total_historical_bytes':sum(r['bytes'] for r in rows),'all_local_decoded_payloads_verified':True,'network_calls':0,'git_objects_removed':False,'free_bytes_before':before,'paths':paths,'removed_paths':[],'scope':'Recoverable sparse worktree residency only. This does not assert computation completion.'}
 def save():
  temp=out.with_name(out.name+'.tmp');temp.write_text(json.dumps(record,indent=2)+'\n');os.replace(temp,out)
 save()
 rules='/*\n!/*/\n/topics/\n!/topics/*/\n/topics/visible-flexible-closed-surface/\n'+''.join('!/'+p+'\n' for p in sorted(paths))
 git('sparse-checkout','set','--no-cone','--stdin',data=rules.encode())
 git('update-index','--skip-worktree','-z','--stdin',data=b''.join(p.encode()+b'\0' for p in paths))
 for row in rows:
  p=root/row['path']
  if p.exists():
   assert row['path'] in snapshots
   st=p.stat();assert (st.st_ino,st.st_mtime_ns,st.st_size)==snapshots[row['path']]
   assert identity(p)['sha256']==row['sha256'];p.unlink()
  record['removed_paths'].append(row['path'])
 assert not any((root/p).exists() for p in paths)
 assert not git('status','--porcelain=v1','-z','--',*paths)
 assert git('rev-parse','HEAD').decode().strip()==head
 after=shutil.disk_usage(root).free
 record.update(status='RECOVERABLE_HISTORICAL_COPIES_EVICTED_BEFORE_TRUE_M14_START',free_bytes_after=after,selected_paths_git_status_clean=True)
 save()
 print(json.dumps({'event':record['status'],'files':66,'protected_sources':len(protected),'free_bytes_before':before,'free_bytes_after':after,'recovery_report':identity(out)}),flush=True)
 assert after>=768*1024*1024,'The unchanged original disk start gate is not yet met'
 wrapper=s/'db6f-root-true-m14-resource-limited.py'
 argv=[sys.executable,str(wrapper),'--launch',str(launch),'--observation',str(n/(pre+'root-spectral-true-m14q512-01-guard-completion.json')),'--backup-observation','/tmp/db6f-spectral-true-m14q512-01-guard-backup.json']
 os.execv(sys.executable,argv)

if __name__=='__main__':main()
