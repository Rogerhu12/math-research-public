#!/usr/bin/env python3
"""Read-only idx/MIDX/refs snapshot; writes new audit artifacts outside .git.

No Git subprocess, pack-content read, credentials/config/environment read,
object mutation, or mathematical solver. A PASS is a preparation condition,
not authorization to delete packs before the replacement/owner checks.
"""
from pathlib import Path
from collections import Counter
from bisect import bisect_left
import argparse
import datetime
import gzip
import hashlib
import json
import re
import struct


CANONICAL = (
    'pack-2bb64ed7669d57870b10e387d4548e2513f95bfd',
    'pack-3eb380dfcaea0a6293aa56f6489c90a1db7a93de',
)
ORDINARY = (
    'pack-0f524eb7958f201e4f000b748b34dbf1323ba5b5',
    'pack-e07605da004ea53b3f0615dd32b445802bb1bcd2',
)
FIXED_IDX_SHA = {
    CANONICAL[0]: 'e81f0e5a1e25f7fcab2619f6f374864bf94897998ddff0092b51a6ce8cf91894',
    CANONICAL[1]: '46f54983d1ce1ee665bafa2bd8b9d551e5868e443c1782d2ef09e98c8d9c59cc',
    ORDINARY[0]: 'c9f8feb1f8820adb848729948869bfd1614bd9669d5723b2c023b9c88368e03a',
    ORDINARY[1]: 'ad67b0cff135db4704b37e0abb1208079a22cb0b1946e2135a7f9e5635f40f4c',
}
HEX40 = re.compile(r'[0-9a-f]{40}')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def dumps(data):
    return (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + '\n').encode()


def oid_text(oids):
    return ''.join(x.hex() + '\n' for x in sorted(oids)).encode('ascii')


def set_summary(oids):
    return {'count': len(oids), 'sorted_hex_lf_sha256': sha(oid_text(oids)),
            'sorted_raw_sha256': sha(b''.join(sorted(oids)))}


def inventory(packdir):
    answer = {}
    for p in sorted(packdir.iterdir()):
        if p.is_file() and (p.name.startswith('pack-') or p.name == 'multi-pack-index'):
            st = p.stat()
            answer[p.name] = (st.st_size, st.st_mtime_ns, st.st_ino)
    return answer


def refs_snapshot(gitdir):
    files = [gitdir / 'HEAD']
    if (gitdir / 'packed-refs').exists():
        files.append(gitdir / 'packed-refs')
    roots = [gitdir / 'refs']
    if (gitdir / 'worktrees').exists():
        for w in sorted((gitdir / 'worktrees').iterdir()):
            if w.is_dir():
                files.append(w / 'HEAD')
                roots.append(w / 'refs')
    for root in roots:
        if root.exists():
            files.extend(p for p in sorted(root.rglob('*')) if p.is_file())
    result = {}
    for p in sorted(set(files)):
        assert not p.name.endswith('.lock'), 'active ref lock; retry only after owner closes it'
        raw = p.read_bytes()
        text = raw.decode('ascii')
        if p.name != 'packed-refs':
            value = text.strip()
            assert HEX40.fullmatch(value) or value.startswith('ref: refs/'), str(p)
        else:
            for line in text.splitlines():
                if not line or line.startswith('#'):
                    continue
                if line.startswith('^'):
                    assert HEX40.fullmatch(line[1:])
                else:
                    oid, ref = line.split(' ', 1)
                    assert HEX40.fullmatch(oid) and ref.startswith('refs/')
        result[str(p.relative_to(gitdir))] = {'bytes': len(raw), 'sha256': sha(raw), 'text': text}
    return result


def read_idx(path):
    b = path.read_bytes()
    assert b[:8] == b'\xfftOc\x00\x00\x00\x02'
    assert hashlib.sha1(b[:-20]).digest() == b[-20:]
    assert b[-40:-20].hex() == path.stem[5:]
    fan = struct.unpack_from('>256I', b, 8)
    n = fan[-1]
    assert list(fan) == sorted(fan)
    start = 8 + 1024
    oids = [b[start + 20*i:start + 20*(i+1)] for i in range(n)]
    assert oids == sorted(set(oids))
    count = Counter(x[0] for x in oids)
    assert list(fan) == [sum(count[j] for j in range(i+1)) for i in range(256)]
    offstart = start + 24*n
    largestart = start + 28*n
    assert len(b) >= largestart + 40 and (len(b) - largestart - 40) % 8 == 0
    largecount = (len(b) - largestart - 40)//8
    offsets = []
    for i in range(n):
        x = struct.unpack_from('>I', b, offstart+4*i)[0]
        if x & 0x80000000:
            assert (x & 0x7fffffff) < largecount
            x = struct.unpack_from('>Q', b, largestart+8*(x & 0x7fffffff))[0]
        offsets.append(x)
    pack = path.with_suffix('.pack')
    packbytes = pack.stat().st_size
    assert all(12 <= x < packbytes-20 for x in offsets)
    marker = path.with_suffix('.promisor')
    return oids, offsets, {
        'name': path.stem, 'idx_sha256': sha(b), 'idx_bytes': len(b),
        'pack_bytes': packbytes, 'promisor': marker.is_file(),
        'promisor_bytes': marker.stat().st_size if marker.is_file() else None,
        'oid_set': set_summary(oids), 'idx_checksum_and_offsets_passed': True,
    }


def read_midx(path, packs):
    b = path.read_bytes()
    assert b[:6] == b'MIDX\x01\x01' and b[7] == 0
    assert hashlib.sha1(b[:-20]).digest() == b[-20:]
    count = b[6]
    npacks = struct.unpack_from('>I', b, 8)[0]
    chunks = {}
    entries = []
    for i in range(count+1):
        ident = b[12+12*i:16+12*i]
        off = struct.unpack_from('>Q', b, 16+12*i)[0]
        entries.append((ident, off))
    assert entries[-1][0] == b'\0\0\0\0' and entries[-1][1] == len(b)-20
    assert all(entries[i][1] <= entries[i+1][1] for i in range(count))
    for i in range(count):
        chunks[entries[i][0]] = b[entries[i][1]:entries[i+1][1]]
    names = [x.decode('ascii').removesuffix('.idx') for x in chunks[b'PNAM'].split(b'\0')[:npacks]]
    assert len(set(names)) == npacks and all(x in packs for x in names)
    fan = struct.unpack('>256I', chunks[b'OIDF'])
    n = fan[-1]
    assert len(chunks[b'OIDL']) == 20*n and len(chunks[b'OOFF']) == 8*n
    oids = [chunks[b'OIDL'][20*i:20*(i+1)] for i in range(n)]
    assert oids == sorted(set(oids))
    counters = Counter(x[0] for x in oids)
    assert list(fan) == [sum(counters[j] for j in range(i+1)) for i in range(256)]
    owners = Counter()
    for i, oid in enumerate(oids):
        packid, offset = struct.unpack_from('>II', chunks[b'OOFF'], 8*i)
        assert packid < len(names)
        if b'LOFF' in chunks and offset & 0x80000000:
            idx = offset & 0x7fffffff
            assert 8*(idx+1) <= len(chunks[b'LOFF'])
            offset = struct.unpack_from('>Q', chunks[b'LOFF'], 8*idx)[0]
        name = names[packid]
        pos = bisect_left(packs[name][0], oid)
        assert pos < len(packs[name][0]) and packs[name][0][pos] == oid
        assert packs[name][1][pos] == offset
        owners[name] += 1
    indexed_names_union = set().union(*(set(packs[x][0]) for x in names))
    assert set(oids) == indexed_names_union
    return {'sha256': sha(b), 'bytes': len(b), 'pack_names': names,
            'oid_set': set_summary(oids), 'selected_owner_counts': dict(sorted(owners.items())),
            'all_owners_have_matching_oid_and_exact_idx_offset': True,
            'exact_union_of_named_pack_indices': True, 'checksum_passed': True}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', required=True)
    ap.add_argument('--out-prefix', required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    gitdir = repo / '.git'
    assert gitdir.is_dir(), 'This bounded reader expects the current primary .git directory'
    packdir = gitdir / 'objects' / 'pack'
    out = Path(args.out_prefix).resolve()
    assert gitdir not in out.parents and out.parent.exists()
    paths = {k: Path(str(out)+v) for k,v in {
        'report': '.json', 'sets': '-oid-sets.json.gz', 'delta': '-promisor-delta-oids.txt'}.items()}
    assert all(not p.exists() for p in paths.values())
    before = inventory(packdir)
    refs = refs_snapshot(gitdir)
    packs = {}
    for path in sorted(packdir.glob('pack-*.idx')):
        packs[path.stem] = read_idx(path)
    pack_names = {p.stem for p in packdir.glob('pack-*.pack')}
    assert pack_names == set(packs), 'Unindexed pack present; no maintenance decision'
    for name, expected in FIXED_IDX_SHA.items():
        assert packs[name][2]['idx_sha256'] == expected, 'fixed pack index changed'
    ordinary_names = tuple(n for n in sorted(packs) if not packs[n][2]['promisor'])
    assert ordinary_names == tuple(sorted(ORDINARY)), 'new ordinary pack requires a new partition plan'
    assert all(packs[n][2]['promisor'] for n in CANONICAL)
    canonical = set().union(*(set(packs[n][0]) for n in CANONICAL))
    ordinary = set().union(*(set(packs[n][0]) for n in ordinary_names))
    promisor = set().union(*(set(v[0]) for v in packs.values() if v[2]['promisor']))
    indexed = promisor | ordinary
    delta = promisor - canonical
    assert not (ordinary & promisor), 'ordinary/promisor overlap requires revised review'
    assert len(canonical) == sum(len(packs[n][0]) for n in CANONICAL)
    assert len(ordinary) == sum(len(packs[n][0]) for n in ordinary_names)
    assert (canonical | delta | ordinary) == indexed
    loose = set()
    for d in (gitdir / 'objects').iterdir():
        if d.is_dir() and re.fullmatch(r'[0-9a-f]{2}', d.name):
            for p in d.iterdir():
                if p.is_file() and re.fullmatch(r'[0-9a-f]{38}', p.name):
                    loose.add(bytes.fromhex(d.name+p.name))
    midx = read_midx(packdir / 'multi-pack-index', packs)
    assert inventory(packdir) == before, 'pack inventory changed during read'
    assert refs_snapshot(gitdir) == refs, 'refs/HEAD changed during read'
    extra_names = sorted(set(packs)-set(CANONICAL)-set(ORDINARY))
    payload = {'format': 'sorted-sha1-hex-lists-v1',
        'pack_oids': {n: [x.hex() for x in v[0]] for n,v in sorted(packs.items())},
        'loose_oids': [x.hex() for x in sorted(loose)]}
    packed_payload = gzip.compress(dumps(payload), compresslevel=6, mtime=0)
    delta_bytes = oid_text(delta)
    assert len(packed_payload) < 5_000_000 and len(delta_bytes) < 1_000_000
    source = Path(__file__).resolve()
    report = {'status': 'PASS_READ_ONLY_PREPARATION_NOT_MAINTENANCE_COMPLETION',
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'script': str(source), 'script_sha256': sha(source.read_bytes()),
        'repo': str(repo), 'packs': [v[2] for _,v in sorted(packs.items())],
        'pack_count': len(packs), 'pack_bytes': sum(v[2]['pack_bytes'] for v in packs.values()),
        'canonical_names': list(CANONICAL), 'ordinary_names': list(ORDINARY),
        'canonical': set_summary(canonical), 'ordinary': set_summary(ordinary),
        'known_promisor': set_summary(promisor), 'indexed': set_summary(indexed),
        'loose_names': set_summary(loose), 'allpresent_by_idx_and_loose_names': set_summary(indexed|loose),
        'promisor_delta': set_summary(delta), 'ordinary_promisor_intersection_count': 0,
        'three_replacement_partitions_pairwise_disjoint': True,
        'three_replacement_partitions_exact_indexed_union': True,
        'fixed_four_idx_hashes_unchanged_from_prior_audit': True,
        'midx': midx, 'refs_and_heads': refs, 'refs_and_heads_sha256': sha(dumps(refs)),
        'read_interval_pack_inventory_and_refs_stable': True,
        'current_extra_promisor_pack_names': extra_names,
        'extra_promisor_pack_bytes_before_replacement': sum(packs[n][2]['pack_bytes'] for n in extra_names),
        'future_expire_required_conditions': [
            'new .promisor replacement idx OID set equals this frozen delta exactly',
            'all current indexed and loose-name OID sets and refs/HEAD preserved',
            'MIDX selected owners: exact canonical, new delta, both ordinary; all other packs zero',
            'only after those checks may root expire zero-selected packs and verify again'],
        'oid_sets_file': str(paths['sets']), 'oid_sets_sha256': sha(packed_payload),
        'oid_sets_bytes': len(packed_payload),
        'delta_input_file': str(paths['delta']), 'delta_input_sha256': sha(delta_bytes),
        'delta_input_bytes': len(delta_bytes),
        'pack_contents_read': False, 'loose_contents_read': False,
        'credentials_or_environment_read': False, 'git_subprocess_calls': 0,
        'git_mutations_performed': False, 'fetch_run': False}
    paths['sets'].write_bytes(packed_payload)
    paths['delta'].write_bytes(delta_bytes)
    paths['report'].write_bytes(dumps(report))
    print(json.dumps({'status': report['status'], 'pack_count': len(packs),
        'pack_bytes': report['pack_bytes'], 'canonical': len(canonical),
        'ordinary': len(ordinary), 'promisor_delta': len(delta),
        'indexed': len(indexed), 'allpresent': len(indexed|loose),
        'extra_promisor_pack_bytes': report['extra_promisor_pack_bytes_before_replacement'],
        'report_sha256': sha(paths['report'].read_bytes()), 'oid_sets_bytes': len(packed_payload)}))


if __name__ == '__main__':
    main()
