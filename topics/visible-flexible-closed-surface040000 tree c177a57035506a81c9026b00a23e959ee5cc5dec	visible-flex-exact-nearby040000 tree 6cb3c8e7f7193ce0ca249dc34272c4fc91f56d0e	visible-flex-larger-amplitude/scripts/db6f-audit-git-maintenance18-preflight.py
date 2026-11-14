#!/usr/bin/env python3
"""Read-only, single-pack rescue preflight; never modifies Git state.

Freeze small index/set summaries and the exact same-partition missing OIDs.
No pack payload read, Git subprocess, network, garbage collection or solver.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True

TARGET = 'pack-d44586219587f80e0b96f6485973557d6a009d35'
READER_SHA = 'db3b33fd4426aef7c5c158fb3c1f494a367f4b70f45d9b15f80c266f623817be'


def sha(b):
    return hashlib.sha256(b).hexdigest()


def loose_names(gitdir):
    answer = set()
    for d in (gitdir/'objects').iterdir():
        if d.is_dir() and re.fullmatch('[0-9a-f]{2}', d.name):
            for p in d.iterdir():
                if p.is_file() and re.fullmatch('[0-9a-f]{38}', p.name):
                    answer.add(bytes.fromhex(d.name+p.name))
    return answer


def resolved_head(snapshot):
    head = snapshot['HEAD']['text'].strip()
    if not head.startswith('ref: '):
        return head
    ref = head[5:]
    if ref in snapshot:
        return snapshot[ref]['text'].strip()
    for line in snapshot.get('packed-refs',{}).get('text','').splitlines():
        if line and not line.startswith(('#','^')):
            oid, name = line.split(' ',1)
            if name == ref:
                return oid
    raise AssertionError('HEAD target absent from frozen references')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--expected-head', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--rescue-oids', required=True)
    args = ap.parse_args()
    assert re.fullmatch('[0-9a-f]{40}',args.expected_head)
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    gitdir = repo/'.git'
    pd = gitdir/'objects/pack'
    reader_path = topic/'scripts/db6f-audit-git-maintenance17-preflight.py'
    assert sha(reader_path.read_bytes()) == READER_SHA
    spec = importlib.util.spec_from_file_location('frozen_idx_reader',reader_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    refs = m.refs_snapshot(gitdir)
    assert resolved_head(refs) == args.expected_head, 'Wait for the parent publication/reset to finish'
    before = m.inventory(pd)
    loose = loose_names(gitdir)
    packs = {p.stem:m.read_idx(p) for p in sorted(pd.glob('pack-*.idx'))}
    assert set(packs) == {p.stem for p in pd.glob('pack-*.pack')}
    sets = {k:set(v[0]) for k,v in packs.items()}
    prom_names = {k for k,v in packs.items() if v[2]['promisor']}
    ordinary_names = set(packs)-prom_names
    assert ordinary_names == set(m.ORDINARY)
    assert set(m.CANONICAL) <= prom_names
    for k,digest in m.FIXED_IDX_SHA.items():
        assert packs[k][2]['idx_sha256'] == digest
    assert TARGET in prom_names and TARGET not in m.CANONICAL
    P = set().union(*(sets[k] for k in prom_names))
    O = set().union(*(sets[k] for k in ordinary_names))
    assert not P & O, 'Partition overlap: the old disjoint-owner maintenance protocol needs a new review'
    retained_prom_names = prom_names-{TARGET}
    retained_P = set().union(*(sets[k] for k in retained_prom_names))
    removed = sets[TARGET]
    missing = removed-retained_P
    covered = removed & retained_P
    assert missing <= P and not missing & O
    assert retained_P | missing == P
    assert len(covered)+len(missing) == len(removed)
    midx_path = pd/'multi-pack-index'
    midx = m.read_midx(midx_path,packs) if midx_path.is_file() else None
    out = Path(args.out).resolve()
    rescue_path = Path(args.rescue_oids).resolve()
    assert out != rescue_path and not out.exists() and not rescue_path.exists()
    assert gitdir not in out.parents and gitdir not in rescue_path.parents
    assert m.inventory(pd) == before
    assert m.refs_snapshot(gitdir) == refs
    assert loose_names(gitdir) == loose
    payload = m.oid_text(missing)
    result = {
        'status':'PASS_READ_ONLY_SINGLE_PROMISOR_PACK_RESCUE_PREFLIGHT',
        'reviewer':'/root/independent_geometry',
        'source_script_sha256':sha(Path(__file__).resolve().read_bytes()),
        'reader_sha256':READER_SHA, 'repo':str(repo),
        'published_head':args.expected_head,
        'refs_and_heads':refs, 'refs_and_heads_sha256':sha(m.dumps(refs)),
        'pack_count':len(packs), 'pack_bytes':sum(v[2]['pack_bytes'] for v in packs.values()),
        'packs':[packs[k][2] for k in sorted(packs)],
        'inventory_stats':before,
        'promisor':m.set_summary(P), 'ordinary':m.set_summary(O),
        'promisor_ordinary_intersection':0,
        'all_indexed':m.set_summary(P|O),
        'loose_names_only':m.set_summary(loose),
        'all_present_by_index_and_loose_names':m.set_summary(P|O|loose),
        'removal_scope':[TARGET],
        'target_pack_bytes':packs[TARGET][2]['pack_bytes'],
        'target_idx_sha256':packs[TARGET][2]['idx_sha256'],
        'target_oid_count':len(removed),
        'retained_promisor_pack_names':sorted(retained_prom_names),
        'retained_ordinary_pack_names':sorted(ordinary_names),
        'retained_promisor_before_rescue':m.set_summary(retained_P),
        'target_covered_by_retained_promisor':m.set_summary(covered),
        'rescue_missing':m.set_summary(missing),
        'rescue_oids_file':str(rescue_path), 'rescue_oids_file_bytes':len(payload),
        'rescue_oids_file_sha256':sha(payload),
        'same_partition_rescue_and_retained_union_exactly_equals_original_promisor':True,
        'ordinary_sets_used_to_cover_promisor':False,
        'ordinary_partition_exactly_retained':True,
        'fixed_canonical_and_ordinary_idx_hashes_passed':True,
        'current_midx':midx,
        'target_current_midx_status':(
            'indexed' if midx and TARGET in midx['pack_names'] else 'not-indexed'),
        'target_current_midx_selected_owners':(
            midx['selected_owner_counts'].get(TARGET,0) if midx and TARGET in midx['pack_names'] else None),
        'preconditions_for_later_root_mutation':[
            'Write and validate a known-promisor rescue pack whose exact idx OID set is rescue_missing; actual pack bytes are not inferred here.',
            'Keep every other current pack, all loose objects and all references intact.',
            'Rebuild MIDX including target, rescue and every retained pack. Check full indexed coverage and owner classification against the preserved disjoint partitions.',
            'Require target to be listed by that new MIDX with exactly zero selected owners; absence from the old MIDX is not this check.',
            'Only then use the standard MIDX expiration path and verify the exact removed-pack set, all original object sets, partitions and refs.'
        ],
        'read_interval_stable':True,
        'git_subprocess_calls':0, 'network_calls':0, 'pack_payload_reads':False,
        'loose_payload_reads':False, 'credential_or_environment_reads':False,
        'git_mutations_performed':False, 'new_full_oid_snapshot_created':False,
        'limitations':[
            'This is a preflight, not evidence that a rescue pack, updated MIDX or expiration has already completed.',
            'The small rescue OID count does not by itself bound its future compressed or reconstructed byte size.',
            'Object coverage is exact by validated indices and loose filenames; object payload decoding is outside scope.'
        ]
    }
    with rescue_path.open('xb') as f:
        f.write(payload)
    with out.open('xb') as f:
        f.write(m.dumps(result))
    print(json.dumps({'status':result['status'], 'packs':len(packs),
        'target_bytes':result['target_pack_bytes'], 'target_oids':len(removed),
        'same_partition_missing':len(missing), 'missing_hex_lf_sha256':sha(payload),
        'all_indexed':len(P|O), 'all_present':len(P|O|loose),
        'midx_target':result['target_current_midx_status'],
        'report_sha256':sha(out.read_bytes())}))


if __name__ == '__main__':
    main()
