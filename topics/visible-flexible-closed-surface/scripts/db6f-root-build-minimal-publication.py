#!/usr/bin/env python3
"""Reapply a closed own-topic commit onto a shallow latest-main tree, offline.

No network or credentials are used here. Every changed existing topic path must
still have its published base blob (or already have the desired blob). Root LOG
is append-only and is merged separately. This never updates a remote ref.
"""
import argparse, hashlib, json, os, pathlib, subprocess

p=argparse.ArgumentParser()
p.add_argument('--source-repo',required=True)
p.add_argument('--bare-repo',required=True)
p.add_argument('--base',required=True)
p.add_argument('--source',required=True)
p.add_argument('--parent',required=True)
p.add_argument('--parent-log',required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
root=pathlib.Path(a.source_repo).resolve(); bare=pathlib.Path(a.bare_repo).resolve()
topic='topics/visible-flexible-closed-surface/'
env=os.environ.copy()
env['GIT_NO_LAZY_FETCH']='1'
env['GIT_TERMINAL_PROMPT']='0'
env['GIT_INDEX_FILE']='/tmp/db6f-minimal-publish-index'
# Existing authentication variables are neither read nor serialized.
def git(repo,*args,data=None,extra_env=None):
    e=env.copy()
    if extra_env: e.update(extra_env)
    r=subprocess.run(['git','-c','protocol.allow=never','-c','remote.origin.promisor=false','-C',str(repo),*args],input=data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=e)
    if r.returncode:
        raise RuntimeError('offline git operation failed: '+args[0]+'; exit='+str(r.returncode))
    return r.stdout

def entry(repo,commit,path):
    raw=git(repo,'ls-tree','-z',commit,'--',path)
    if not raw: return None
    parts=raw.rstrip(b'\0').split(b'\0')
    assert len(parts)==1, (commit,path,'multiple entries')
    meta, gotpath=parts[0].split(b'\t',1)
    mode,kind,oid=meta.decode('ascii').split()
    assert gotpath.decode('utf-8')==path and kind=='blob'
    assert mode in ('100644','100755'), (path,'unsupported file mode')
    return (mode,oid)

def blob(repo,oid): return git(repo,'cat-file','blob',oid)
def obj_sha(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def put(data):
    got=git(bare,'hash-object','-w','--stdin',data=data).decode().strip()
    assert got==obj_sha(data)
    return got

git(root,'merge-base','--is-ancestor',a.base,a.source)
git(bare,'cat-file','-e',a.parent+'^{commit}')
raw=git(root,'diff-tree','--no-commit-id','-r','--name-only','-z',a.base,a.source)
paths=[x.decode('utf-8') for x in raw.split(b'\0') if x]
assert paths and len(paths)==len(set(paths))
assert all(x=='LOG.md' or x.startswith(topic) for x in paths)
assert 'LOG.md' in paths
assert all('\n' not in x and '\t' not in x and not x.lower().endswith('.pdf') for x in paths)
source_log_entry=entry(root,a.source,'LOG.md'); base_log_entry=entry(root,a.base,'LOG.md')
parent_log_entry=entry(bare,a.parent,'LOG.md')
source_log=blob(root,source_log_entry[1]); base_log=blob(root,base_log_entry[1])
assert source_log.startswith(base_log), 'source LOG must be append-only relative to base'
delta=source_log[len(base_log):]
assert delta and delta.endswith(b'\n')
nonempty=[s for s in delta.decode('utf-8').splitlines() if s]
assert len(nonempty)==1 and len(nonempty[0])<=200, 'exactly one bounded own log line'
parent_log=pathlib.Path(a.parent_log).read_bytes()
assert obj_sha(parent_log)==parent_log_entry[1], 'fetched LOG bytes do not match latest parent'
assert len(parent_log)<50_000, 'root LOG rotation requires separate review'
assert parent_log.endswith(b'\n')
merged_log=parent_log if nonempty[0] in parent_log.decode('utf-8').splitlines() else parent_log+delta
assert len(merged_log)<50_000
plan=[]
for path in paths:
    if path=='LOG.md': continue
    old=entry(root,a.base,path); new=entry(root,a.source,path); remote=entry(bare,a.parent,path)
    assert new is not None, (path,'deletions require separate review')
    assert remote==old or remote==new, (path,'conflicting latest-main edit')
    data=blob(root,new[1])
    assert len(data)<5_000_000, (path,'file size limit')
    if len(data)>1_000_000: assert path.endswith('.gz'), (path,'uncompressed data size')
    plan.append((path,new,data,remote))
# Mutation starts only after all source, parent and per-path gates pass.
git(bare,'read-tree',a.parent)
index_rows=[]; files=[]
for path,new,data,remote in plan:
    assert put(data)==new[1]
    index_rows.append(f'{new[0]} {new[1]}\t{path}\0'.encode())
    files.append({'path':path,'mode':new[0],'git_blob':new[1],'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'already_present':remote==new})
log_oid=put(merged_log)
index_rows.append(f'{parent_log_entry[0]} {log_oid}\tLOG.md\0'.encode())
git(bare,'update-index','-z','--index-info',data=b''.join(index_rows))
# Unchanged blob:none parent blobs already belong to the remote parent.
# All newly written blobs were copied and hash-verified above; no lazy fetch.
tree=git(bare,'write-tree','--missing-ok').decode().strip()
changed=git(bare,'diff-tree','--no-commit-id','-r','--name-only','-z',a.parent,tree)
changed_paths=[x.decode() for x in changed.split(b'\0') if x]
assert set(changed_paths).issubset(set(paths))
for path,new,_,_ in plan: assert entry(bare,tree,path)==new
assert entry(bare,tree,'LOG.md')==(parent_log_entry[0],log_oid)
identity=git(root,'show','-s','--format=%an%x00%ae',a.source).rstrip(b'\n').split(b'\0')
assert len(identity)==2
commit_env={'GIT_AUTHOR_NAME':identity[0].decode(),'GIT_AUTHOR_EMAIL':identity[1].decode(),'GIT_COMMITTER_NAME':identity[0].decode(),'GIT_COMMITTER_EMAIL':identity[1].decode()}
source_message=git(root,'show','-s','--format=%B',a.source).rstrip(b'\n')
assert source_message and b'\0' not in source_message and len(source_message)<10000
message=source_message+b'\n\nReapplied closed own-topic source '+a.source.encode()+b' onto latest main, preserving unrelated trees and the append-only root LOG.\n'
commit=git(bare,'commit-tree',tree,'-p',a.parent,data=message,extra_env=commit_env).decode().strip()
git(bare,'update-ref','refs/heads/db6f-publish',commit)
report={'status':'PREPARED_OFFLINE_AWAITING_ORDINARY_FAST_FORWARD_PUSH','source_base':a.base,'source_commit':a.source,'latest_parent':a.parent,'candidate_commit':commit,'candidate_tree':tree,'changed_path_count':len(changed_paths),'topic_files':files,'topic_total_bytes':sum(x['bytes'] for x in files),'root_log_bytes':len(merged_log),'root_log_sha256':hashlib.sha256(merged_log).hexdigest(),'per_path_conflict_gate':True,'unrelated_paths_preserved':True,'network_calls':0,'remote_ref_updates':0}
out=pathlib.Path(a.output); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('status','latest_parent','candidate_commit','candidate_tree','changed_path_count','topic_total_bytes','root_log_bytes')},ensure_ascii=False))
