#!/usr/bin/env python3
"""One read-only after-check of the actual necessary Git 2.43 fetch.

Read indices, frozen metadata/OID bytes and file stats only. Write one small
report outside .git. No Git, network, pack-body, auth-log or solver calls.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True


def sha(data):
    return hashlib.sha256(data).hexdigest()


def checked(path, digest):
    b = path.read_bytes()
    assert sha(b) == digest, str(path)
    return json.loads(b)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    repo = topic.parents[1]
    notes = topic / 'notes'
    reader_path = topic / 'scripts/db6f-audit-git-maintenance17-preflight.py'
    reader_sha = 'db3b33fd4426aef7c5c158fb3c1f494a367f4b70f45d9b15f80c266f623817be'
    assert sha(reader_path.read_bytes()) == reader_sha
    spec = importlib.util.spec_from_file_location('frozen_idx_reader', reader_path)
    reader = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reader)
    root_path = notes / '2026-11-09-db6f-root-fetch243-publication-observation.json'
    root_sha = 'a82e8c2757dc22e24c6670ffcb8dc3307d756b86d15494f22e2cd76e40a4e53e'
    root = checked(root_path, root_sha)
    before_path = Path('/dev/shm/db6f-fetch243-observation/before.json')
    before_sha = '1666643fb66c4106af7835838009740f6625bfe2e283caa5135e0acf10b2a436'
    before = checked(before_path, before_sha)
    for k, v in before.items():
        if k != 'status':
            assert root[k] == v, k
    raw_path = Path(before['temporary_oid_checkpoint'])
    assert raw_path == Path('/dev/shm/db6f-fetch243-observation/before-oid-set.bin')
    raw = raw_path.read_bytes()
    assert len(raw) == 20 * before['packed_oid_count_before']
    assert sha(raw) == before['packed_oid_raw_sha256_before']
    old_list = [raw[i:i+20] for i in range(0, len(raw), 20)]
    assert old_list == sorted(set(old_list))
    old = set(old_list)
    packdir = repo / '.git/objects/pack'
    stable_before = reader.inventory(packdir)
    packs = {p.stem: reader.read_idx(p) for p in sorted(packdir.glob('pack-*.idx'))}
    assert set(packs) == {p.stem for p in packdir.glob('pack-*.pack')}
    def metadata(name):
        oids, _, info = packs[name]
        return {'name': name, 'idx_sha256': info['idx_sha256'],
                'objects': len(oids), 'pack_bytes': info['pack_bytes'],
                'promisor': info['promisor']}
    old_records = {x['name']: x for x in before['packs_before']}
    new_records = {x['name']: x for x in root['new_pack_records']}
    assert len(old_records) == 19 and len(new_records) == 2
    assert set(old_records).isdisjoint(new_records)
    assert set(packs) == set(old_records) | set(new_records)
    for name, record in {**old_records, **new_records}.items():
        assert metadata(name) == record, name
    reconstructed_old = set().union(*(set(packs[k][0]) for k in old_records))
    assert reconstructed_old == old
    current = set().union(*(set(packs[k][0]) for k in packs))
    fresh_packs = set().union(*(set(packs[k][0]) for k in new_records))
    assert old <= current
    assert len(old) == 117057
    assert len(current) == root['packed_oid_count_after'] == 117740
    assert len(current-old) == root['new_packed_oid_count'] == 683
    fresh_bytes = sum(packs[k][2]['pack_bytes'] for k in new_records)
    max_bytes = max(packs[k][2]['pack_bytes'] for k in new_records)
    assert fresh_bytes == root['new_pack_bytes_total'] == 7549991
    assert max_bytes == root['largest_new_pack_bytes'] == 7525795
    assert reader.inventory(packdir) == stable_before
    assert sha(root_path.read_bytes()) == root_sha
    assert sha(before_path.read_bytes()) == before_sha
    out = Path(args.out).resolve()
    assert not out.exists() and (repo/'.git') not in out.parents
    result = {
        'status': 'PASS_INDEPENDENT_READ_ONLY_FETCH243_POSTCHECK',
        'reviewer': '/root/independent_geometry',
        'script_sha256': sha(Path(__file__).resolve().read_bytes()),
        'frozen_reader_sha256': reader_sha,
        'root_report_sha256': root_sha,
        'before_metadata_sha256': before_sha,
        'before_raw_oid_sha256': sha(raw),
        'old_pack_count': len(old_records), 'current_pack_count': len(packs),
        'old_pack_idx_hash_bytes_count_promisor_all_unchanged': True,
        'old_indices_union_exactly_equals_frozen_raw_set': True,
        'all_old_packed_oids_retained': True,
        'packed_oid_count_before': len(old), 'packed_oid_count_after': len(current),
        'new_distinct_packed_oids': len(current-old),
        'current_sorted_raw_oid_sha256': sha(b''.join(sorted(current))),
        'new_pack_records': [metadata(k) for k in sorted(new_records)],
        'new_pack_bytes_total': fresh_bytes, 'largest_new_pack_bytes': max_bytes,
        'new_pack_index_oid_occurrences': sum(len(packs[k][0]) for k in new_records),
        'new_pack_distinct_oids': len(fresh_packs),
        'new_pack_distinct_oids_already_in_old_packs': len(fresh_packs & old),
        'read_interval_metadata_stable': True,
        'git_subprocess_calls': 0, 'network_calls': 0, 'pack_body_reads': 0,
        'credential_or_auth_log_reads': 0, 'solver_or_backend_calls': 0,
        'git_mutations': False, 'new_full_oid_snapshot_created': False,
        'limitations': [
            'Indices/checksums and pack sizes/markers were read; pack object bodies were not decoded or rehashed.',
            'The actual fetch executable, flags, merge/push execution and absence of intervening GC are historical execution claims in the bound root record; this postcheck did not inspect authentication loops or logs.',
            'This one observed publication does not prove a universal size bound, absence of all duplicate objects or the cause of every prior repeated pack.',
            'The raw before-set remains a temporary checkpoint; the bound unchanged old indices independently reconstruct exactly the same set.'
        ]
    }
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'], 'old_packs':len(old_records),
        'new_packs':len(new_records), 'retained_oids':len(old),
        'new_oids':len(current-old), 'new_pack_bytes':fresh_bytes,
        'overlap_with_old':len(fresh_packs & old),
        'report_sha256':sha(out.read_bytes())}))


if __name__ == '__main__':
    main()
