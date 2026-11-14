#!/usr/bin/env python3
"""Read only idx/stat/allowed refs; report same-partition pack coverage.

No Git subprocess, pack or loose payload read, credential/environment read,
network, deletion, repack, ref mutation, or mathematical solver.
"""
from pathlib import Path
from collections import Counter, defaultdict
import argparse
import datetime
import hashlib
import json
import os
import re
import struct

HEX40 = re.compile(r'[0-9a-f]{40}')


def sha(b):
    return hashlib.sha256(b).hexdigest()


def stable_stat(p):
    s=p.stat()
    return [s.st_size,s.st_mtime_ns,s.st_ino]


def index_read(p):
    b=p.read_bytes()
    assert b[:8]==b'\xfftOc\x00\x00\x00\x02'
    assert hashlib.sha1(b[:-20]).digest()==b[-20:]
    assert b[-40:-20].hex()==p.stem[5:]
    fan=struct.unpack_from('>256I',b,8)
    assert list(fan)==sorted(fan)
    n=fan[-1]
    first=1032
    assert len(b)>=first+28*n+40
    oids=[b[first+20*i:first+20*(i+1)] for i in range(n)]
    assert oids==sorted(set(oids))
    hist=Counter(x[0] for x in oids)
    assert list(fan)==[sum(hist[x] for x in range(j+1)) for j in range(256)]
    off0=first+24*n
    large0=first+28*n
    assert (len(b)-large0-40)%8==0
    large_n=(len(b)-large0-40)//8
    offsets=[]
    for i in range(n):
        raw=struct.unpack_from('>I',b,off0+4*i)[0]
        if raw>>31:
            j=raw&0x7fffffff
            assert j<large_n
            raw=struct.unpack_from('>Q',b,large0+8*j)[0]
        offsets.append(raw)
    pack=p.with_suffix('.pack')
    size=pack.stat().st_size
    assert len(set(offsets))==n
    assert all(12<=x<size-20 for x in offsets)
    ordered=sorted(zip(offsets,oids))
    if ordered: assert ordered[0][0]==12
    spans={oid:(ordered[i+1][0] if i+1<n else size-20)-off
           for i,(off,oid) in enumerate(ordered)}
    assert all(x>0 for x in spans.values())
    assert sum(spans.values())==size-32
    return {'name':p.stem,'oids':set(oids),'spans':spans,
            'partition':'promisor' if p.with_suffix('.promisor').is_file() else 'ordinary',
            'idx_sha256':sha(b),'idx_bytes':len(b),'pack_bytes':size,
            'oid_count':n,'index_sha1_and_fanout_offsets_validated':True}


def pack_snapshot(pd):
    return {p.name:stable_stat(p) for p in sorted(pd.iterdir())
            if p.is_file() and (p.name.startswith('pack-') or p.name=='multi-pack-index')}


def ref_hashes(gitdir):
    files=[gitdir/'HEAD']
    if (gitdir/'packed-refs').is_file(): files.append(gitdir/'packed-refs')
    roots=[gitdir/'refs']
    worktrees=gitdir/'worktrees'
    if worktrees.is_dir():
        for w in sorted(worktrees.iterdir()):
            if w.is_dir():
                if (w/'HEAD').is_file():files.append(w/'HEAD')
                roots.append(w/'refs')
    for root in roots:
        if root.is_dir():files.extend(p for p in root.rglob('*') if p.is_file())
    answer={}
    for p in sorted(set(files)):
        assert not p.name.endswith('.lock'),'Active reference lock'
        raw=p.read_bytes()
        s=raw.decode('ascii')
        if p.name!='packed-refs':
            assert HEX40.fullmatch(s.strip()) or s.strip().startswith('ref: refs/')
        else:
            for line in s.splitlines():
                if not line or line.startswith('#'):continue
                if line.startswith('^'):assert HEX40.fullmatch(line[1:])
                else:
                    oid,name=line.split(' ',1)
                    assert HEX40.fullmatch(oid) and name.startswith('refs/')
        answer[str(p.relative_to(gitdir))]={'bytes':len(raw),'sha256':sha(raw)}
    return answer


def set_digest(s):
    return {'count':len(s),'sorted_raw_sha256':sha(b''.join(sorted(s)))}


def workspace_scan(root,repo):
    """Metadata only, no symlink traversal, no hidden directory traversal."""
    by_two=defaultdict(lambda:[0,0])
    by_three=defaultdict(lambda:[0,0])
    files=[]
    errors=[]
    skipped=[]
    total=0
    count=0
    own_replay=[]
    def err(e):errors.append({'path':e.filename,'error_type':type(e).__name__})
    for here,dirs,names in os.walk(root,topdown=True,onerror=err,followlinks=False):
        hp=Path(here)
        keep=[]
        for d in dirs:
            q=hp/d
            if d.startswith('.') or q.is_symlink():
                skipped.append(str(q.relative_to(root)))
            else:keep.append(d)
        dirs[:]=keep
        for name in names:
            p=hp/name
            if p.is_symlink() or name.startswith('.'):continue
            try:
                s=p.stat()
                if not p.is_file():continue
            except OSError as e:
                err(e);continue
            rel=p.relative_to(root)
            parts=rel.parts
            size=s.st_size
            total+=size;count+=1
            for target,depth in [(by_two,2),(by_three,3)]:
                k='/'.join(parts[:min(depth,len(parts)-1)]) or '.'
                target[k][0]+=size;target[k][1]+=1
            row={'path':str(rel),'bytes':size,'mtime_ns':s.st_mtime_ns}
            if size>=20*1024*1024:files.append(row)
            if 'db6f-tail-' in name and ('replay' in name or 'rerun' in name) and size>=1024*1024:
                own_replay.append(row)
    rank=lambda rows:sorted(rows,key=lambda x:x['bytes'],reverse=True)
    directory_rows=lambda d:[{'path':k,'bytes':v[0],'file_count':v[1]}
                              for k,v in sorted(d.items(),key=lambda x:x[1][0],reverse=True)[:30]]
    return {'root':str(root),'metadata_only':True,'hidden_directories_files_and_all_symlinks_skipped':True,
            'total_logical_regular_file_bytes':total,'file_count':count,
            'largest_two_level_directories':directory_rows(by_two),
            'largest_three_level_directories':directory_rows(by_three),
            'files_at_least_20MiB':rank(files)[:50],
            'all_files_at_least_20MiB_count':len(files),
            'own_replay_or_rerun_files_at_least_1MiB':rank(own_replay)[:40],
            'own_replay_or_rerun_large_files_total_bytes':sum(x['bytes'] for x in own_replay),
            'skipped_hidden_or_symlink_directory_count':len(skipped),
            'errors':errors,
            'limitations':['Metadata does not establish ownership, publication, or whether any file is disposable.',
                           'Directory totals are logical bytes, not allocated bytes or deduplicated storage.',
                           'No path outside this session workspace is scanned, including /home/oai/.cache.']}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--workspace',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    repo=args.repo.resolve();root=args.workspace.resolve();out=args.out.resolve()
    gd=repo/'.git';pd=gd/'objects/pack'
    assert gd.is_dir() and repo.is_relative_to(root)
    assert not out.exists() and not out.is_relative_to(gd)
    before=pack_snapshot(pd);refs=ref_hashes(gd)
    packs=[index_read(p) for p in sorted(pd.glob('pack-*.idx'))]
    assert {p['name'] for p in packs}=={p.stem for p in pd.glob('pack-*.pack')}
    groups={x:[p for p in packs if p['partition']==x] for x in ['promisor','ordinary']}
    counters={k:Counter(oid for p in group for oid in p['oids']) for k,group in groups.items()}
    unions={k:set(c) for k,c in counters.items()}
    rows=[]
    for p in packs:
        ctr=counters[p['partition']]
        unique={oid for oid in p['oids'] if ctr[oid]==1}
        unique_bytes=sum(p['spans'][oid] for oid in unique)
        rows.append({k:v for k,v in p.items() if k not in ['oids','spans']}|{
            'same_partition_unique':set_digest(unique),
            'covered_by_other_same_partition_count':p['oid_count']-len(unique),
            'unique_packed_entry_span_bytes_estimate':unique_bytes,
            'covered_packed_entry_span_bytes_estimate':p['pack_bytes']-32-unique_bytes,
            'fully_redundant_by_same_partition_idx_sets':not unique,
            'unique_packed_span_is_not_a_rescue_pack_size_bound':True})
    rows.sort(key=lambda x:x['pack_bytes'],reverse=True)
    no_unique=[p for p in rows if p['fully_redundant_by_same_partition_idx_sets']]
    # Independent single-pack removability is not simultaneous removability.
    remaining={p['name']:p for p in packs}
    removable=[]
    for candidate in sorted(packs,key=lambda p:p['pack_bytes'],reverse=True):
        others=[p for name,p in remaining.items() if name!=candidate['name'] and p['partition']==candidate['partition']]
        covered=set().union(*(p['oids'] for p in others)) if others else set()
        if candidate['oids']<=covered:
            removable.append(candidate['name']);remaining.pop(candidate['name'])
    residual={k:set().union(*(p['oids'] for p in remaining.values() if p['partition']==k)) for k in groups}
    assert residual==unions
    scan=workspace_scan(root,repo)
    assert pack_snapshot(pd)==before,'Pack inventory changed; retry only at stable parent checkpoint'
    assert ref_hashes(gd)==refs,'Refs changed during read'
    v=os.statvfs(repo)
    result={'status':'READ_ONLY_COVERAGE_AND_WORKSPACE_DIAGNOSTIC',
            'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'source_script_sha256':sha(Path(__file__).read_bytes()),
            'repo':str(repo),'available_bytes_at_end':v.f_bavail*v.f_frsize,
            'pack_count':len(packs),'pack_bytes':sum(p['pack_bytes'] for p in packs),
            'partition_object_sets':{k:set_digest(v) for k,v in unions.items()},
            'partition_intersection_count':len(unions['promisor']&unions['ordinary']),
            'all_indexed':set_digest(unions['promisor']|unions['ordinary']),
            'packs':rows,
            'individually_fully_redundant_pack_count':len(no_unique),
            'individually_fully_redundant_pack_bytes_sum_not_joint_claim':sum(p['pack_bytes'] for p in no_unique),
            'greedy_joint_same_partition_coverage_preserving_candidate_names':removable,
            'greedy_joint_candidate_pack_bytes':sum(p['pack_bytes'] for p in packs if p['name'] in removable),
            'joint_candidate_coverage_preserves_each_partition_exactly':True,
            'joint_candidate_at_least_500_decimal_MB':sum(p['pack_bytes'] for p in packs if p['name'] in removable)>=500_000_000,
            'pack_and_ref_read_interval_stable':True,'refs_hash_summary':refs,
            'workspace_metadata_scan':scan,
            'payload_and_operation_scope':{
                'pack_payload_read':False,'loose_payload_read':False,'credential_or_environment_read':False,
                'git_subprocess_calls':0,'network_calls':0,'git_mutations':False,
                'deletion_repack_ref_changes':False,'full_oid_arrays_written':False},
            'limitations':['Coverage is validated index identity only; payload decode and replacement availability are not newly verified.',
                           'Packed-entry spans include the stored delta form; they do not bound a reconstructed rescue pack size.',
                           'No candidate is authorized for deletion. A later mutation still needs current ownership/partition, MIDX owner, full coverage, reference preservation, and postcheck gates.',
                           'Individual redundancy cannot be summed for simultaneous deletion; only the separate greedy sequence is jointly coverage preserving by index sets.']}
    with out.open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps({'status':result['status'],'pack_count':len(packs),'pack_bytes':result['pack_bytes'],
                     'all_indexed_count':result['all_indexed']['count'],
                     'large_pack_summaries':[{'name':p['name'],'bytes':p['pack_bytes'],'partition':p['partition'],'unique_count':p['same_partition_unique']['count'],'unique_packed_span_bytes_estimate':p['unique_packed_entry_span_bytes_estimate']} for p in rows if p['pack_bytes']>=50*1024*1024],
                     'joint_redundant_candidate_bytes':result['greedy_joint_candidate_pack_bytes'],
                     'workspace_scanned_logical_bytes':scan['total_logical_regular_file_bytes'],
                     'large_file_count':scan['all_files_at_least_20MiB_count'],
                     'available_bytes':result['available_bytes_at_end'],'report_sha256':sha(out.read_bytes())}))


if __name__=='__main__':main()
