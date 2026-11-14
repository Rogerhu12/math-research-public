#!/usr/bin/env python3
"""Independent read-only reconstruction after single-pack maintenance 18."""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib.util
import json
import re
import sys
sys.dont_write_bytecode = True


def sha(b):
    return hashlib.sha256(b).hexdigest()


def checked(path, expected):
    b = path.read_bytes()
    assert sha(b) == expected, str(path)
    return json.loads(b)


def loose_names(gitdir):
    result = set()
    for d in (gitdir/'objects').iterdir():
        if d.is_dir() and re.fullmatch('[0-9a-f]{2}',d.name):
            for p in d.iterdir():
                if p.is_file() and re.fullmatch('[0-9a-f]{38}',p.name):
                    result.add(bytes.fromhex(d.name+p.name))
    return result


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',required=True)
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    repo=topic.parents[1]
    notes=topic/'notes'
    gitdir=repo/'.git'
    pd=gitdir/'objects/pack'
    readerpath=topic/'scripts/db6f-audit-git-maintenance17-preflight.py'
    reader_sha='db3b33fd4426aef7c5c158fb3c1f494a367f4b70f45d9b15f80c266f623817be'
    assert sha(readerpath.read_bytes())==reader_sha
    spec=importlib.util.spec_from_file_location('frozen_idx_reader',readerpath)
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    hashes={
        'preflight':'ddb7a2e82f55f7b86f11cef2eb7cd4e6d7314e198ae3fee2580ef9fc1977068d',
        'binding':'fbb5ae06d13ce7dec28b6771fd1c425ac4b76ab681c0fc6991630cebafcf7a70',
        'payload':'8bdea818a0156aa955a10218e92ac0b3853804ca807d1efe3f5b545c657cdc7a',
        'root_report':'300bb6762758c9ff03ef872540aa1a59aafd4af529b84c14f553eb8f06062bb0',
        'root_observed':'c3e96e17f5b9ec807b573105f5ff76a88b72b6f948bfa09f6a7a5116b72c4b1e',
        'root_script':'1f82bf0328f46b570831c8a0046d6cacc8e1fc3ec4df680ef203f857b96be34f'
    }
    stem='2026-11-09-db6f-audit-git-maintenance18'
    pre=checked(notes/(stem+'-preflight.json'),hashes['preflight'])
    binding=checked(notes/(stem+'-payload-binding.json'),hashes['binding'])
    packed=(notes/(stem+'-target-and-loose.json.gz')).read_bytes()
    assert sha(packed)==hashes['payload']==binding['payload_sha256']
    payload=json.loads(gzip.decompress(packed))
    root=checked(notes/'2026-11-09-db6f-root-git-space-maintenance-18.json',hashes['root_report'])
    observed=checked(notes/'2026-11-09-db6f-root-git-space-maintenance18-observed-execution.json',hashes['root_observed'])
    assert sha((topic/'scripts/db6f-root-git-space-maintenance18.py').read_bytes())==hashes['root_script']==root['script_sha256']
    assert observed['actual_exit_code']==0
    assert root['status']=='COMPLETED_ALL_SETS_PARTITIONS_REFS_PRESERVED'
    target='pack-d44586219587f80e0b96f6485973557d6a009d35'
    rescue='pack-54c9604895d20ebd3d60fe9d9246d0fb7832fd4b'
    assert pre['removal_scope']==root['removed_pack_names']==[target]
    assert root['zero_owner_pack_names']==[target]
    assert root['rescue_pack']==rescue
    oldmeta={p['name']:p for p in pre['packs']}
    before=m.inventory(pd)
    refs=m.refs_snapshot(gitdir)
    assert refs==pre['refs_and_heads']
    current={p.stem:m.read_idx(p) for p in sorted(pd.glob('pack-*.idx'))}
    assert set(current)==(set(oldmeta)-{target})|{rescue}
    assert set(current)=={p.stem for p in pd.glob('pack-*.pack')}
    oldsets={}
    retained_mtime_count=0
    for name,row in current.items():
        if name==rescue:
            continue
        assert row[2]==oldmeta[name],name
        oldsets[name]=set(row[0])
        st=(pd/(name+'.pack')).stat()
        oldstat=pre['inventory_stats'][name+'.pack']
        assert [st.st_size,st.st_mtime_ns,st.st_ino]==oldstat
        assert st.st_mtime_ns==binding['original_pack_file_mtime_ns'][name+'.pack']
        retained_mtime_count+=1
    for name,oldstat in pre['inventory_stats'].items():
        if name=='multi-pack-index':
            continue
        if name.startswith(target+'.'):
            assert not (pd/name).exists(),name
        else:
            assert name in before and list(before[name])==oldstat,name
    assert {n for n in before if n not in pre['inventory_stats']}=={rescue+s for s in ('.pack','.idx','.promisor')}
    assert payload['target_pack_name']==target
    assert payload['target_idx_sha256']==oldmeta[target]['idx_sha256']
    targetoids=[bytes.fromhex(x) for x in payload['target_oids']]
    assert targetoids==sorted(set(targetoids))
    oldsets[target]=set(targetoids)
    assert m.set_summary(oldsets[target])==oldmeta[target]['oid_set']==binding['target_oid_set']
    old_p=set().union(*(v for k,v in oldsets.items() if oldmeta[k]['promisor']))
    old_o=set().union(*(v for k,v in oldsets.items() if not oldmeta[k]['promisor']))
    old_l={bytes.fromhex(x) for x in payload['loose_oids']}
    assert len(old_l)==len(payload['loose_oids'])
    for value,key in [(old_p,'promisor'),(old_o,'ordinary'),(old_p|old_o,'all_indexed'),(old_l,'loose_names_only'),(old_p|old_o|old_l,'all_present_by_index_and_loose_names')]:
        assert m.set_summary(value)==pre[key]
    retained_p=set().union(*(v for k,v in oldsets.items() if k!=target and oldmeta[k]['promisor']))
    missing=oldsets[target]-retained_p
    assert len(missing)==27 and m.set_summary(missing)==pre['rescue_missing']==root['rescue_missing']
    assert set(current[rescue][0])==missing
    assert current[rescue][2]['promisor']
    assert current[rescue][2]['pack_bytes']==root['rescue_pack_bytes']==414447
    assert current[rescue][2]['idx_sha256']==root['rescue_idx_sha256']
    new_p=set().union(*(set(v[0]) for v in current.values() if v[2]['promisor']))
    new_o=set().union(*(set(v[0]) for v in current.values() if not v[2]['promisor']))
    assert new_p==old_p and new_o==old_o and not new_p&new_o
    loose=loose_names(gitdir)
    assert loose==old_l
    assert new_p|new_o|loose==old_p|old_o|old_l
    midx=m.read_midx(pd/'multi-pack-index',current)
    assert set(midx['pack_names'])==set(current)
    assert midx['oid_set']==m.set_summary(old_p|old_o)
    assert midx==root['final_midx']
    assert midx['selected_owner_counts']==root['midx_before_expire']['selected_owner_counts']
    assert sum(v[2]['pack_bytes'] for v in current.values())==root['after_pack_bytes']==5290124822
    assert len(current)==root['after_pack_count']==23 and retained_mtime_count==22
    assert m.inventory(pd)==before and m.refs_snapshot(gitdir)==refs and loose_names(gitdir)==loose
    out=Path(args.out).resolve()
    assert not out.exists() and gitdir not in out.parents
    result={
        'status':'PASS_INDEPENDENT_READ_ONLY_MAINTENANCE18_POSTCHECK',
        'reviewer':'/root/independent_geometry',
        'script_sha256':sha(Path(__file__).resolve().read_bytes()),
        'frozen_reader_sha256':reader_sha, 'input_sha256':hashes,
        'reconstruction':'Unchanged retained indices plus frozen removed-target OIDs and frozen loose filenames; actual set equality, not only copied root summaries.',
        'removed_pack_names_exact':[target], 'new_pack_name_exact':rescue,
        'rescue_oid_count':len(missing), 'rescue_pack_bytes':414447,
        'rescue_idx_sha256':current[rescue][2]['idx_sha256'],
        'rescue_exactly_equals_frozen_same_partition_missing':True,
        'all_retained_idx_and_metadata_exactly_unchanged':True,
        'retained_original_pack_mtime_ns_exactly_restored_count':retained_mtime_count,
        'original_retained_pack_inodes_sizes_and_mtimes_unchanged':True,
        'original_target_files_all_absent':True,
        'original_loose_oid_set_exactly_unchanged':True,
        'promisor':m.set_summary(new_p), 'ordinary':m.set_summary(new_o),
        'indexed':m.set_summary(new_p|new_o), 'all_present':m.set_summary(new_p|new_o|loose),
        'all_reconstructed_old_sets_equal_current_sets':True,
        'ordinary_promisor_intersection':0,
        'refs_and_heads_raw_files_exactly_unchanged':True,
        'refs_and_heads_sha256':pre['refs_and_heads_sha256'],
        'pack_count':len(current), 'pack_bytes':5290124822,
        'pack_byte_reduction':pre['pack_bytes']-5290124822,
        'current_midx':midx,
        'current_midx_all_owner_oid_offsets_independently_checked':True,
        'current_selected_owner_counts_equal_root_preexpire_counts':True,
        'read_interval_stable':True,
        'git_subprocess_calls':0, 'network_calls':0, 'pack_payload_reads':False,
        'loose_payload_reads':False,'credential_or_environment_reads':False,
        'git_mutations':False,'new_full_oid_snapshot_created':False,
        'limitations':[
            'Historical pre-expiry zero-owner and subprocess execution are bound to the reviewed root source and root execution report; the past MIDX was not independently observed by this postcheck.',
            'Index checksums, OID sets and offsets, metadata and current MIDX were checked; pack payloads were not decoded or hashed.',
            'Original pack mtime_ns is independently checked against the preflight. Original atime was not frozen by this reviewer and is not certified here.'
        ]
    }
    with out.open('xb') as f:f.write(m.dumps(result))
    print(json.dumps({'status':result['status'],'packs':len(current),'rescue_oids':len(missing),
        'retained_mtime_exact':retained_mtime_count,'indexed':len(new_p|new_o),
        'all_present':len(new_p|new_o|loose),'byte_reduction':result['pack_byte_reduction'],
        'report_sha256':sha(out.read_bytes())}))


if __name__=='__main__':
    main()
