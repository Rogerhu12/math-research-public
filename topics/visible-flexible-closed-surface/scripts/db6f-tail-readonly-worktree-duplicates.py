#!/usr/bin/env python3
"""Read-only publication notes/repro versus primary and publication Git index.
No Git writes, credential query, network, candidate parsing, or deletion.
"""
import argparse
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

TOPIC='topics/visible-flexible-closed-surface'
PATHS=[TOPIC+'/notes',TOPIC+'/repro']


def digests(path):
    size=path.stat().st_size
    sha=hashlib.sha256()
    blob=hashlib.sha1(b'blob '+str(size).encode()+b'\0')
    if size==0:return sha.hexdigest(),blob.hexdigest()
    with path.open('rb') as f:
        while True:
            b=f.read(1024*1024)
            if not b:break
            sha.update(b);blob.update(b)
    return sha.hexdigest(),blob.hexdigest()


def statkey(p):
    s=p.stat()
    return [s.st_size,s.st_mtime_ns,s.st_ino,s.st_dev,s.st_nlink]


def git(repo,*args):
    command=['env','GIT_OPTIONAL_LOCKS=0','GIT_NO_LAZY_FETCH=1',
             'GIT_CONFIG_NOSYSTEM=1','GIT_CONFIG_GLOBAL=/dev/null',
             'git','-C',str(repo),'-c','core.fsmonitor=false','-c','core.untrackedCache=false',*args]
    r=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=False)
    if r.returncode not in [0,1]:raise RuntimeError('Read-only Git command failed: '+str(args[0]))
    return r.returncode,r.stdout


def safe_configs(repo):
    keys=['extensions.worktreeConfig','core.sparseCheckout','core.sparseCheckoutCone','index.sparse','core.bare','core.worktree']
    result={}
    for k in keys:
        c,b=git(repo,'config','--get',k)
        result[k]={'found':c==0,'value':b.decode().strip() if c==0 else None}
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--primary',type=Path,required=True)
    ap.add_argument('--publication',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();primary=a.primary.resolve();pub=a.publication.resolve();out=a.out.resolve()
    assert not out.exists() and primary!=pub and not out.is_relative_to(pub)
    gitfile=(pub/'.git').read_text().strip()
    assert gitfile.startswith('gitdir: ')
    admin=Path(gitfile[8:]).resolve()
    assert admin.is_relative_to(primary/'.git/worktrees')
    idx=admin/'index';head=admin/'HEAD'
    before={str(p):{'stat':statkey(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [idx,head]}
    cfg_before={'publication':safe_configs(pub),'primary':safe_configs(primary)}
    code,status0=git(pub,'status','--porcelain=v1','-z','--untracked-files=all','--ignored=matching')
    assert code==0
    # Never parse or expose contents of status paths; retain only status counts/hash.
    status_records=[x for x in status0.split(b'\0') if x]
    dirty_count=sum(x[:2] not in [b'??',b'!!'] for x in status_records)
    untracked_count=sum(x[:2]==b'??' for x in status_records)
    ignored_count=sum(x[:2]==b'!!' for x in status_records)
    code,raw=git(pub,'ls-files','--stage','-z','--',*PATHS)
    assert code==0
    rows=[]
    for line in raw.split(b'\0'):
        if not line:continue
        meta,path=line.split(b'\t',1)
        mode,oid,stage=meta.decode('ascii').split(' ')
        rel=path.decode('utf-8')
        assert stage=='0' and mode in ['100644','100755']
        assert any(rel.startswith(x+'/') for x in PATHS)
        if any(x.startswith('.') for x in Path(rel).parts):
            # The only allowed hidden tracked path is this known empty marker;
            # its zero bytes are certified by stat/index without opening it.
            assert rel==TOPIC+'/notes/.gitkeep' and oid=='e69de29bb2d1d6434b8b29ae775ad8c2e48c5391'
            assert (pub/rel).stat().st_size==(primary/rel).stat().st_size==0
        rows.append((rel,mode,oid))
    assert len({x[0] for x in rows})==len(rows)
    summary={'tracked_target_files':len(rows),'present_same_hash_and_index_blob':0,
             'publication_logical_bytes':0,'eligible_logical_bytes':0,
             'eligible_allocated_bytes':0,'eligible_single_link_distinct_inode_allocated_bytes':0,
             'same_inode_logical_bytes':0}
    exceptions=[];manifest=[];largest=[];endchecks=[]
    for rel,mode,oid in rows:
        p=pub/rel;q=primary/rel
        if not p.is_file() or p.is_symlink() or not q.is_file() or q.is_symlink():
            exceptions.append({'path':rel,'reason':'missing_or_nonregular'});continue
        sp=p.stat();sq=q.stat();kp=statkey(p);kq=statkey(q)
        summary['publication_logical_bytes']+=sp.st_size
        if sp.st_size!=sq.st_size:
            exceptions.append({'path':rel,'reason':'different_size','publication_bytes':sp.st_size,'primary_bytes':sq.st_size});continue
        hp,bp=digests(p);hq,bq=digests(q)
        if statkey(p)!=kp or statkey(q)!=kq:
            exceptions.append({'path':rel,'reason':'changed_during_hash'});continue
        if hp!=hq or bp!=oid or bq!=oid:
            exceptions.append({'path':rel,'reason':'hash_or_index_blob_mismatch','same_sha256':hp==hq,'publication_blob_matches_index':bp==oid,'primary_blob_matches_index':bq==oid});continue
        same_inode=(sp.st_dev,sp.st_ino)==(sq.st_dev,sq.st_ino)
        summary['present_same_hash_and_index_blob']+=1
        summary['eligible_logical_bytes']+=sp.st_size
        summary['eligible_allocated_bytes']+=sp.st_blocks*512
        if same_inode:summary['same_inode_logical_bytes']+=sp.st_size
        elif sp.st_nlink==1:summary['eligible_single_link_distinct_inode_allocated_bytes']+=sp.st_blocks*512
        manifest.append(rel+'\0'+mode+'\0'+oid+'\0'+hp+'\0'+str(sp.st_size)+'\n')
        largest.append({'path':rel,'bytes':sp.st_size,'sha256':hp,'index_blob_oid':oid,'publication_nlink':sp.st_nlink,'same_inode_as_primary':same_inode})
        endchecks.append((p,kp,q,kq))
    changed=[]
    for p,kp,q,kq in endchecks:
        if statkey(p)!=kp or statkey(q)!=kq:changed.append(str(p.relative_to(pub)))
    code,status1=git(pub,'status','--porcelain=v1','-z','--untracked-files=all','--ignored=matching')
    assert code==0
    after={str(p):{'stat':statkey(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [idx,head]}
    cfg_after={'publication':safe_configs(pub),'primary':safe_configs(primary)}
    assert before==after and cfg_before==cfg_after and status0==status1
    assert not changed,'A hashed file changed during interval; no closed report'
    patterns={}
    for label,p in [('publication',admin/'info/sparse-checkout'),('primary',primary/'.git/info/sparse-checkout')]:
        if p.is_file():
            b=p.read_bytes();patterns[label]={'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'text':b.decode()}
    result={'status':'READ_ONLY_TRACKED_NOTES_REPRO_COPY_PREFLIGHT','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'primary':str(primary),'publication':str(pub),'allowed_pathspecs':PATHS,
            'publication_git_admin':str(admin),'summary':summary,'exceptions':exceptions,
            'publication_status':{'dirty_records':dirty_count,'untracked_records':untracked_count,'ignored_records':ignored_count,
                'raw_status_sha256':hashlib.sha256(status0).hexdigest(),'clean_including_untracked_and_ignored':not status_records},
            'read_interval_index_head_status_configs_and_hashed_files_unchanged':True,
            'index_and_head':before,'effective_safe_config_values':cfg_before,'existing_sparse_patterns':patterns,
            'target_manifest_sha256':hashlib.sha256(''.join(sorted(manifest)).encode()).hexdigest(),
            'largest_verified_copies':sorted(largest,key=lambda x:x['bytes'],reverse=True)[:15],
            'git_commands_read_only':['status --porcelain -z --untracked-files=all --ignored=matching','ls-files --stage -z -- notes/repro','config --get on six explicit nonsensitive keys'],
            'optional_locks_fsmonitor_untracked_cache_disabled':True,'lazy_fetch_disabled':True,'global_and_system_config_disabled':True,
            'sparse_checkout_config_index_refs_or_files_changed':False,'solver_calls':0,
            'current_or_future_open_writer_absence_proved':False,
            'limitations':['A stable read interval and clean Git status do not prove that no process holds a file open or will start writing; the root publication-worktree owner must confirm quiescence before changing checkout scope.',
                           'Only the exact tracked notes/repro paths are compared; no new scan of other directories is performed.',
                           'Raw blob hashes match the publication index without clean/smudge transformations; the same bytes exist in primary.',
                           'Distinct inode/single-link allocated-block sums are a space estimate, not a guarantee of exact overlay free-space recovery.',
                           'No sparse-checkout, worktreeConfig, index, reference, or checkout mutation was performed.']}
    with out.open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'summary':summary,'clean':not status_records,'exceptions':len(exceptions),'changed':len(changed),'report_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))


if __name__=='__main__':main()
