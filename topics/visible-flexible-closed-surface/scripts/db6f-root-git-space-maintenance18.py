#!/usr/bin/env python3
"""Bound same-partition rescue and standard MIDX expiration of one proved duplicate.

No authentication or network operation. Refuse any changed frozen snapshot or
any zero-owner pack beyond the single reviewed target before expiration.
"""
from pathlib import Path
import datetime
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import time


TOPIC = Path(__file__).resolve().parents[1]
REPO = TOPIC.parents[1]
NOTES = TOPIC / 'notes'
PACKDIR = REPO / '.git/objects/pack'
PREFIX = '2026-11-09-db6f-'
TARGET = 'pack-d44586219587f80e0b96f6485973557d6a009d35'
CANONICAL = 'pack-2bb64ed7669d57870b10e387d4548e2513f95bfd'
SECONDARY = 'pack-3eb380dfcaea0a6293aa56f6489c90a1db7a93de'
PREFLIGHT = NOTES / (PREFIX + 'audit-git-maintenance18-preflight.json')
OUT = NOTES / (PREFIX + 'root-git-space-maintenance-18.json')


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def loose_names():
    result = set()
    for d in (REPO / '.git/objects').iterdir():
        if d.is_dir() and re.fullmatch('[0-9a-f]{2}', d.name):
            for p in d.iterdir():
                if p.is_file() and re.fullmatch('[0-9a-f]{38}', p.name):
                    result.add(bytes.fromhex(d.name+p.name))
    return result


def main():
    assert not OUT.exists()
    assert digest(PREFLIGHT) == 'ddb7a2e82f55f7b86f11cef2eb7cd4e6d7314e198ae3fee2580ef9fc1977068d'
    pre = json.loads(PREFLIGHT.read_text())
    reader = TOPIC / 'scripts/db6f-audit-git-maintenance17-preflight.py'
    assert digest(reader) == 'db3b33fd4426aef7c5c158fb3c1f494a367f4b70f45d9b15f80c266f623817be'
    spec = importlib.util.spec_from_file_location('frozen_idx_reader', reader)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert {k:list(v) for k,v in m.inventory(PACKDIR).items()} == pre['inventory_stats']
    assert m.refs_snapshot(REPO/'.git') == pre['refs_and_heads']
    before = {p.stem:m.read_idx(p) for p in sorted(PACKDIR.glob('pack-*.idx'))}
    assert len(before) == pre['pack_count'] == 23
    assert {p.stem for p in PACKDIR.glob('pack-*.pack')} == set(before)
    meta = {x['name']:x for x in pre['packs']}
    for name, row in before.items():
        assert row[2] == meta[name]
    old_p = set().union(*(set(v[0]) for v in before.values() if v[2]['promisor']))
    old_o = set().union(*(set(v[0]) for v in before.values() if not v[2]['promisor']))
    old_i, old_l = old_p | old_o, loose_names()
    assert not old_p & old_o
    for data, key in [(old_p,'promisor'),(old_o,'ordinary'),(old_i,'all_indexed'),
                      (old_l,'loose_names_only'),(old_i|old_l,'all_present_by_index_and_loose_names')]:
        assert m.set_summary(data) == pre[key]
    retained_p = set().union(*(set(v[0]) for n,v in before.items() if n != TARGET and v[2]['promisor']))
    missing = set(before[TARGET][0]) - retained_p
    assert m.set_summary(missing) == pre['rescue_missing'] and len(missing) == 27
    rescue_list = Path(pre['rescue_oids_file'])
    assert digest(rescue_list) == pre['rescue_oids_file_sha256']
    assert rescue_list.read_bytes() == m.oid_text(missing)
    original_times = {n:(PACKDIR/(n+'.pack')).stat() for n in before}
    tmp = Path(tempfile.mkdtemp(prefix='db6f-maintenance18-', dir='/dev/shm'))
    commands = []
    record = dict(status='STARTED', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  script_sha256=digest(Path(__file__)), preflight_sha256=digest(PREFLIGHT),
                  target_pack=TARGET, before_pack_count=len(before),
                  rescue_missing=pre['rescue_missing'], actual_subprocesses=commands,
                  temporary_directory=str(tmp), network_operations=0)
    stage = 'before-rescue'
    expired = False

    def run(args, **kwargs):
        argv = ['git','-c','gc.auto=0','-c','maintenance.auto=false',*args]
        env = dict(os.environ, GIT_NO_LAZY_FETCH='1', GIT_NO_REPLACE_OBJECTS='1')
        result = subprocess.run(argv, cwd=REPO, env=env, stderr=subprocess.PIPE, **kwargs)
        commands.append(dict(argv=argv, actual_exit_code=result.returncode,
                             stderr_sha256=hashlib.sha256(result.stderr).hexdigest()))
        if result.returncode:
            raise RuntimeError('Git subprocess failed: '+repr(args)+'; '+result.stderr.decode(errors='replace')[:2000])
        return result

    try:
        raw_pack = tmp/'rescue.pack'
        with raw_pack.open('xb') as h:
            run(['pack-objects','--stdout','--window=0','--threads=1'], input=rescue_list.read_bytes(), stdout=h)
        with raw_pack.open('rb') as h:
            h.seek(-20,2)
            pack_sha1 = h.read().hex()
        rescue_name = 'pack-'+pack_sha1
        assert rescue_name not in before
        pack = tmp/(rescue_name+'.pack')
        raw_pack.rename(pack)
        idx = tmp/(rescue_name+'.idx')
        result = run(['index-pack','--index-version=2','-o',str(idx),str(pack)], stdout=subprocess.PIPE)
        assert result.stdout.decode().strip() == pack_sha1
        (tmp/(rescue_name+'.promisor')).write_bytes(b'')
        rescue = m.read_idx(idx)
        assert set(rescue[0]) == missing and rescue[2]['promisor']
        record.update(rescue_pack=rescue_name, rescue_pack_bytes=pack.stat().st_size,
                      rescue_idx_sha256=digest(idx), rescue_pack_sha256=digest(pack))
        for suffix in ('.pack','.idx','.promisor'):
            dst = PACKDIR/(rescue_name+suffix)
            assert not dst.exists()
            staging = PACKDIR/(rescue_name+suffix+'.maintenance18-tmp')
            assert not staging.exists()
            shutil.copyfile(tmp/(rescue_name+suffix), staging)
            staging.rename(dst)
        stage = 'rescue-installed-all-old-packs-retained'
        current = {p.stem:m.read_idx(p) for p in sorted(PACKDIR.glob('pack-*.idx'))}
        assert set(current) == set(before)|{rescue_name}
        assert set().union(*(set(v[0]) for v in current.values())) == old_i
        assert m.refs_snapshot(REPO/'.git') == pre['refs_and_heads'] and loose_names() == old_l
        backup = tmp/'multi-pack-index-before'
        shutil.copyfile(PACKDIR/'multi-pack-index', backup)
        assert digest(backup) == pre['current_midx']['sha256']
        record['derived_midx_backup_sha256'] = digest(backup)
        newer = max(time.time_ns(),max(st.st_mtime_ns for st in original_times.values()))+10_000_000_000
        for i,(name,row) in enumerate(sorted(current.items())):
            if name != TARGET and row[2]['promisor']:
                p = PACKDIR/(name+'.pack')
                st = p.stat()
                stamp = newer+(1_000_000 if name == SECONDARY else i)
                os.utime(p, ns=(st.st_atime_ns,stamp))
        (PACKDIR/'multi-pack-index').unlink()
        run(['multi-pack-index','write','--no-bitmap','--preferred-pack='+CANONICAL+'.pack'], stdout=subprocess.PIPE)
        run(['multi-pack-index','verify'], stdout=subprocess.PIPE)
        midx = m.read_midx(PACKDIR/'multi-pack-index', current)
        assert set(midx['pack_names']) == set(current)
        assert midx['oid_set'] == m.set_summary(old_i)
        zeros = sorted(set(current)-set(midx['selected_owner_counts']))
        record['midx_before_expire'] = midx
        record['zero_owner_pack_names'] = zeros
        assert zeros == [TARGET], 'Unexpected zero-owner packs; stop before expiry: '+repr(zeros)
        assert set().union(*(set(current[x][0]) for x in current if x != TARGET and current[x][2]['promisor'])) == old_p
        assert set().union(*(set(v[0]) for v in current.values() if not v[2]['promisor'])) == old_o
        stage = 'proved-single-zero-owner-target-before-expiry'
        run(['multi-pack-index','expire'], stdout=subprocess.PIPE)
        expired = True
        stage = 'standard-expiry-returned'
        run(['multi-pack-index','verify'], stdout=subprocess.PIPE)
        after = {p.stem:m.read_idx(p) for p in sorted(PACKDIR.glob('pack-*.idx'))}
        assert set(after) == (set(before)-{TARGET})|{rescue_name}
        assert {p.stem for p in PACKDIR.glob('pack-*.pack')} == set(after)
        new_p = set().union(*(set(v[0]) for v in after.values() if v[2]['promisor']))
        new_o = set().union(*(set(v[0]) for v in after.values() if not v[2]['promisor']))
        assert new_p == old_p and new_o == old_o and not new_p & new_o
        assert loose_names() == old_l and m.refs_snapshot(REPO/'.git') == pre['refs_and_heads']
        for name,row in after.items():
            if name != rescue_name:
                assert row == before[name]
        post_midx = m.read_midx(PACKDIR/'multi-pack-index',after)
        assert set(post_midx['pack_names']) == set(after)
        assert post_midx['oid_set'] == m.set_summary(old_i)
        record.update(status='COMPLETED_ALL_SETS_PARTITIONS_REFS_PRESERVED',
                      removed_pack_names=[TARGET], after_pack_count=len(after),
                      after_pack_bytes=sum(v[2]['pack_bytes'] for v in after.values()),
                      indexed=m.set_summary(old_i), all_present=m.set_summary(old_i|old_l),
                      promisor=m.set_summary(old_p), ordinary=m.set_summary(old_o),
                      final_midx=post_midx, refs_and_heads_sha256=pre['refs_and_heads_sha256'])
    except BaseException as exc:
        record.update(status='STOPPED_REQUIRES_ROOT_OBSERVATION', failed_stage=stage,
                      exception=repr(exc), standard_expiry_returned=expired)
        raise
    finally:
        for name,st in original_times.items():
            p = PACKDIR/(name+'.pack')
            if p.exists():
                os.utime(p, ns=(st.st_atime_ns,st.st_mtime_ns))
        record['retained_original_pack_mtime_ns_restored'] = all(
            not (PACKDIR/(name+'.pack')).exists() or (PACKDIR/(name+'.pack')).stat().st_mtime_ns == st.st_mtime_ns
            for name,st in original_times.items())
        if not record['retained_original_pack_mtime_ns_restored']:
            record['status'] = 'FAILED_ORIGINAL_MTIME_RESTORATION'
        record['completed_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        fs = os.statvfs(REPO)
        record['available_bytes_after'] = fs.f_bavail*fs.f_frsize
        raw = (json.dumps(record,indent=2,sort_keys=True)+'\n').encode()
        (tmp/'root-maintenance18-record.json').write_bytes(raw)
        with OUT.open('xb') as h:
            h.write(raw)
        assert record['retained_original_pack_mtime_ns_restored'], 'Original retained pack mtime restoration failed'
    print(json.dumps({k:record[k] for k in ['status','rescue_pack','rescue_pack_bytes',
                                         'after_pack_count','after_pack_bytes','available_bytes_after']}))


if __name__ == '__main__':
    main()
