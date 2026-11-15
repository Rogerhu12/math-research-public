#!/usr/bin/env python3
"""Byte-only release of two redundant ZIP wrappers; retain every extracted file."""
from pathlib import Path, PurePosixPath
import hashlib, json, os, stat, zipfile, zlib

ROOT = Path('/tmp/visible-larger-recovery-2207/actions-debug')
TARGETS = (
 ('visible-mainline-modelresponse-43668743706-1', 48375172, '9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c'),
 ('visible-mainline-modelresponse-43672150224-1', 10267458, '78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6'),
)
RECEIPT = Path('/tmp/2026-11-15-duplicate83-91-zip-byte-preservation.json')

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def durable_write(value):
    b = (json.dumps(value, indent=2, sort_keys=True)+'\n').encode()
    with RECEIPT.open('wb') as f:
        f.write(b); f.flush(); os.fsync(f.fileno())
    fd = os.open(str(RECEIPT.parent), os.O_RDONLY)
    try: os.fsync(fd)
    finally: os.close(fd)

audit = {'schema':'two-redundant-local-zip-byte-preservation-v1',
 'scientific_computation_performed':False,
 'extracted_original_files_deleted':False,
 'remote_artifacts_deleted':False, 'archives':[], 'released_archive_paths':[]}
for name, expected_size, expected_sha in TARGETS:
    zpath, directory = ROOT/(name+'.zip'), ROOT/name
    assert zpath.is_file() and not zpath.is_symlink()
    assert directory.is_dir() and not directory.is_symlink()
    assert zpath.stat().st_size == expected_size and digest(zpath) == expected_sha
    assert (directory/'.download-complete').read_text().strip() == expected_sha
    members, names = [], set()
    with zipfile.ZipFile(zpath) as z:
        for info in z.infolist():
            rel = PurePosixPath(info.filename)
            assert not rel.is_absolute() and '..' not in rel.parts and info.filename not in names
            names.add(info.filename)
            assert not stat.S_ISLNK(info.external_attr >> 16)
            path = directory.joinpath(*rel.parts)
            assert path.resolve().is_relative_to(directory.resolve())
            if info.is_dir():
                assert path.is_dir()
                continue
            assert path.is_file() and not path.is_symlink()
            assert path.stat().st_size == info.file_size
            h, count, crc = hashlib.sha256(), 0, 0
            with z.open(info) as f:
                for block in iter(lambda: f.read(1024*1024), b''):
                    h.update(block); count += len(block); crc = zlib.crc32(block, crc)
            assert count == info.file_size and crc == info.CRC
            sha = h.hexdigest()
            assert digest(path) == sha
            members.append({'name':info.filename,'bytes':count,'crc32':info.CRC,
                            'sha256':sha,'retained_file':str(path)})
    audit['archives'].append({'path':str(zpath),'bytes':expected_size,'sha256':expected_sha,
      'all_members_preserved':True,'member_count':len(members),'members':members})
durable_write(audit)
for entry in audit['archives']:
    zpath = Path(entry['path'])
    assert zpath.stat().st_size == entry['bytes'] and digest(zpath) == entry['sha256']
    for member in entry['members']:
        p = Path(member['retained_file'])
        assert p.is_file() and p.stat().st_size == member['bytes'] and digest(p) == member['sha256']
    zpath.unlink()
    audit['released_archive_paths'].append(str(zpath))
    durable_write(audit)
print(json.dumps({'receipt':str(RECEIPT),'receipt_bytes':RECEIPT.stat().st_size,
 'receipt_sha256':digest(RECEIPT),'released_bytes':sum(a['bytes'] for a in audit['archives']),
 'retained_member_counts':[a['member_count'] for a in audit['archives']],
 'scientific_computation_performed':False}))
