#!/usr/bin/env python3
"""Independently compare current idx/MIDX/refs to the frozen pre-maintenance sets.

Only the small report is written. No Git command or pack-content read.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_checked(path, expected):
    assert sha(path) == expected, str(path)
    return json.loads(path.read_text())


def loose_names(gitdir):
    found = set()
    for d in (gitdir / 'objects').iterdir():
        if d.is_dir() and re.fullmatch('[0-9a-f]{2}', d.name):
            for p in d.iterdir():
                if p.is_file() and re.fullmatch('[0-9a-f]{38}', p.name):
                    found.add(bytes.fromhex(d.name+p.name))
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    notes = topic / 'notes'
    reader_path = topic / 'scripts/db6f-audit-git-maintenance17-preflight.py'
    assert sha(reader_path) == 'db3b33fd4426aef7c5c158fb3c1f494a367f4b70f45d9b15f80c266f623817be'
    spec = importlib.util.spec_from_file_location('preflight_reader', reader_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    pre_path = notes / '2026-11-09-db6f-audit-git-maintenance17-preflight.json'
    pre = load_checked(pre_path, 'f6be4675466dd82f9589fc10cb16021cd09d38bc56bca07b5e5eaf9f40b839bf')
    root_path = notes / '2026-11-09-db6f-root-git-space-maintenance-17.json'
    root = load_checked(root_path, '7c1e20145df61c3ef1563f93eb3f9063ba61b3b34d61c32415ca41773688ef24')
    payload_path = Path(pre['oid_sets_file'])
    assert sha(payload_path) == pre['oid_sets_sha256']
    payload = json.loads(gzip.decompress(payload_path.read_bytes()))
    old = {k: {bytes.fromhex(x) for x in v} for k,v in payload['pack_oids'].items()}
    old_meta = {x['name']: x for x in pre['packs']}
    old_promisor = set().union(*(v for k,v in old.items() if old_meta[k]['promisor']))
    old_ordinary = set().union(*(v for k,v in old.items() if not old_meta[k]['promisor']))
    old_indexed = old_promisor | old_ordinary
    old_loose = {bytes.fromhex(x) for x in payload['loose_oids']}
    removed = {'pack-46684770d20796511bfae2110567a4142002db43',
               'pack-b3912fcc6bb924c11f068dafb20f865248f1fa61'}
    rescue = 'pack-181ee1706f018d61bf0f1640334ebaf1a4d8ecf0'
    assert set(root['removed_zero_selected_pack_names']) == removed
    assert root['rescue_pack'] == rescue
    joint_missing = set().union(*(old[k] for k in removed)) - set().union(
        *(v for k,v in old.items() if k not in removed and old_meta[k]['promisor']))
    assert len(joint_missing) == 66
    assert hashlib.sha256(m.oid_text(joint_missing)).hexdigest() == root['rescue_hex_lines_sha256']
    gitdir = Path(pre['repo']) / '.git'
    packdir = gitdir / 'objects/pack'
    before = m.inventory(packdir)
    refs = m.refs_snapshot(gitdir)
    assert refs == pre['refs_and_heads']
    current = {p.stem: m.read_idx(p) for p in sorted(packdir.glob('pack-*.idx'))}
    assert {p.stem for p in packdir.glob('pack-*.pack')} == set(current)
    assert set(current) == (set(old)-removed)|{rescue}
    for name, (oids, _, meta) in current.items():
        if name == rescue:
            assert set(oids) == joint_missing and meta['promisor']
            assert meta['pack_bytes'] == root['rescue_pack_bytes'] == 845485
        else:
            assert set(oids) == old[name]
            assert meta['idx_sha256'] == old_meta[name]['idx_sha256']
            assert meta['promisor'] == old_meta[name]['promisor']
            assert meta['pack_bytes'] == old_meta[name]['pack_bytes']
    promisor = set().union(*(set(v[0]) for v in current.values() if v[2]['promisor']))
    ordinary = set().union(*(set(v[0]) for v in current.values() if not v[2]['promisor']))
    assert promisor == old_promisor and ordinary == old_ordinary and not promisor & ordinary
    indexed = promisor | ordinary
    loose = loose_names(gitdir)
    assert indexed == old_indexed and indexed | loose == old_indexed | old_loose
    assert len(indexed) == root['all_indexed_oid_count'] == 115207
    assert m.set_summary(indexed)['sorted_raw_sha256'] == root['all_indexed_sorted_raw_sha256']
    assert len(indexed|loose) == root['all_present_oid_count'] == 115682
    assert m.set_summary(indexed|loose)['sorted_raw_sha256'] == root['all_present_sorted_raw_sha256']
    midx = m.read_midx(packdir / 'multi-pack-index', current)
    assert set(midx['pack_names']) == set(current)
    assert midx['oid_set'] == m.set_summary(indexed)
    assert midx['selected_owner_counts'] == root['selected_owners_before_expire']
    assert sum(v[2]['pack_bytes'] for v in current.values()) == root['pack_bytes_after'] == 5261709057
    assert m.inventory(packdir) == before and m.refs_snapshot(gitdir) == refs
    assert loose_names(gitdir) == loose
    out = Path(args.out).resolve()
    assert not out.exists() and gitdir not in out.parents
    result = {
        'status': 'PASS_INDEPENDENT_READ_ONLY_POST_MAINTENANCE_CHECK',
        'source_script_sha256': sha(Path(__file__).resolve()),
        'reader_script_sha256': sha(reader_path), 'root_report_sha256': sha(root_path),
        'frozen_preflight_sha256': sha(pre_path), 'frozen_oid_sets_sha256': sha(payload_path),
        'current_pack_count': len(current), 'current_pack_bytes': root['pack_bytes_after'],
        'removed_pack_names_exact': sorted(removed), 'new_pack_name_exact': rescue,
        'rescue_idx_sha256': current[rescue][2]['idx_sha256'],
        'rescue_exactly_equals_joint_missing_66': True,
        'rescue_sorted_hex_lf_sha256': root['rescue_hex_lines_sha256'],
        'unchanged_retained_idx_hashes': True, 'unchanged_retained_pack_sizes': True,
        'indexed': m.set_summary(indexed), 'allpresent_by_idx_and_loose_names': m.set_summary(indexed|loose),
        'promisor': m.set_summary(promisor), 'ordinary': m.set_summary(ordinary),
        'all_four_sets_exactly_equal_frozen_original_sets': True,
        'ordinary_promisor_intersection': 0,
        'refs_and_heads_raw_files_exactly_unchanged': True,
        'refs_and_heads_sha256': pre['refs_and_heads_sha256'],
        'midx': midx,
        'midx_owners_respect_preserved_partition_by_membership_and_disjointness': True,
        'current_owners_equal_root_reported_pre_expiry_owners': True,
        'read_interval_stable': True,
        'pack_contents_read': False, 'loose_contents_read': False,
        'git_subprocess_calls': 0, 'git_mutations_performed': False,
        'new_full_oid_snapshot_created': False,
        'original_mtime_restore_independently_checked': False,
        'limitations': ['Original timestamps were not saved in this reviewer\'s frozen preflight; root\'s restoration statement is not independently certified here.',
                       'Object-set comparison reads indices and loose filenames, not decompressed object contents.'],
    }
    out.write_bytes(m.dumps(result))
    print(json.dumps({'status': result['status'], 'packs': len(current), 'indexed': len(indexed),
        'allpresent': len(indexed|loose), 'promisor': len(promisor), 'ordinary': len(ordinary),
        'rescue': len(joint_missing), 'report_sha256': sha(out)}))


if __name__ == '__main__':
    main()
