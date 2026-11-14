#!/usr/bin/env python3
"""Snapshot/restore immutable exact-stage files without changing any float byte.

Archives are only recoverable component evaluations, never accepted solutions.
Restoration checks every archive and member checksum and refuses a different
existing file. No executable is read from an archive or executed by this tool.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import tarfile


def sha(b):return hashlib.sha256(b).hexdigest()


def atomic(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        if path.read_bytes()!=data:raise FileExistsError('Different immutable file: '+str(path))
        return
    temporary=path.with_name(path.name+'.tmp-'+str(os.getpid()))
    with temporary.open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())
    try:
        try:os.link(temporary,path)
        except FileExistsError:
            if path.read_bytes()!=data:raise
    finally:temporary.unlink()


def safe_name(value):
    p=PurePosixPath(value)
    if p.is_absolute() or not p.parts or any(x in ('..','.') for x in p.parts):
        raise ValueError('Unsafe archive member')
    return p


def inspect_archive(path,row,expected,restore_root=None):
    data=path.read_bytes()
    if len(data)!=row['bytes'] or sha(data)!=row['sha256']:
        raise ValueError('Archive bytes changed')
    seen=set()
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as tar:
        for member in tar:
            name=str(safe_name(member.name))
            if not member.isfile() or name in seen or name not in expected:
                raise ValueError('Unexpected/duplicate/non-file archive member')
            info=expected[name];b=tar.extractfile(member).read()
            if len(b)!=info['bytes'] or sha(b)!=info['sha256']:
                raise ValueError('Archived exact-stage member changed')
            if restore_root is not None:atomic(restore_root/Path(name),b)
            seen.add(name)
    if seen!=set(row['members']):raise ValueError('Archive member list differs')
    return len(seen)


def snapshot(args):
    root=args.cache_root.resolve()
    if len(root.name)!=64 or any(c not in '0123456789abcdef' for c in root.name):
        raise ValueError('Cache root must be one explicit complete identity directory')
    files=sorted(p for p in root.rglob('*') if p.is_file() and (p.suffix=='.bin' or p.name=='identity.txt'))
    if not any(p.name=='identity.txt' for p in files):raise ValueError('Complete cache identity is missing')
    rows=[]
    for p in files:
        if p.is_symlink():raise ValueError('Refuse linked cache input')
        b=p.read_bytes();rows.append(dict(path=p.relative_to(root.parent).as_posix(),bytes=len(b),sha256=sha(b)))
    bins=[r for r in rows if r['path'].endswith('.bin')]
    if args.expected_stages is not None and len(bins)!=args.expected_stages:
        raise ValueError('Complete expected cache size differs')
    archives=[];current=[];size=0;groups=[]
    for row in rows:
        if current and size+row['bytes']>3_500_000:groups.append(current);current=[];size=0
        current.append(row);size+=row['bytes']
    if current:groups.append(current)
    expected={r['path']:r for r in rows}
    for index,group in enumerate(groups):
        buf=io.BytesIO()
        with gzip.GzipFile(fileobj=buf,mode='wb',mtime=0,compresslevel=6) as gz:
            with tarfile.open(fileobj=gz,mode='w|') as tar:
                for row in group:
                    p=root.parent/row['path'];b=p.read_bytes()
                    if len(b)!=row['bytes'] or sha(b)!=row['sha256']:raise ValueError('Snapshot input changed')
                    info=tarfile.TarInfo(row['path']);info.size=len(b);info.mtime=0;info.mode=0o600
                    tar.addfile(info,io.BytesIO(b))
        data=buf.getvalue()
        if len(data)>=5_000_000:raise ValueError('Archive exceeds repository limit')
        p=args.out_prefix.with_name(args.out_prefix.name+'-%03d.tar.gz'%index);atomic(p,data)
        row=dict(path=str(p),bytes=len(data),sha256=sha(data),members=[r['path'] for r in group])
        row['all_member_bytes_verified_after_compression']=inspect_archive(p,row,expected)==len(group)
        archives.append(row)
    report=dict(schema='exact-stage-cache-immutable-archive-v1',scope=__doc__,
        stage_identity_sha256=root.name,stage_files=len(bins),complete_files=len(rows),
        original_cache_root=str(root),files=rows,archives=archives,
        snapshot_tool_sha256=sha(Path(__file__).read_bytes()),
        every_completed_original_stage_output_retained=True,nonlinear_solution_accepted=False,
        partial_or_complete_cache_is_not_a_tail_acceptance=True,
        restore_argv=['python','computations/strong_exact_stage_cache_archive.py','restore',
            '--manifest',str(args.out_prefix)+'.json','--cache-parent',str(root.parent)],
        identity_runtime_source_parameter_guard_still_applies=True)
    atomic(Path(str(args.out_prefix)+'.json'),(json.dumps(report,indent=2)+'\n').encode())
    print(json.dumps(dict(manifest=str(args.out_prefix)+'.json',stage_files=len(bins),
        archives=len(archives),total_archive_bytes=sum(r['bytes'] for r in archives))))


def restore(args):
    manifest=json.loads(args.manifest.read_text())
    if manifest.get('schema')!='exact-stage-cache-immutable-archive-v1':raise ValueError('Unknown archive schema')
    identity=manifest['stage_identity_sha256'];expected={row['path']:row for row in manifest['files']}
    if any(safe_name(path).parts[0]!=identity for path in expected):raise ValueError('Member identity differs')
    count=0
    for row in manifest['archives']:
        count+=inspect_archive(Path(row['path']),row,expected,args.cache_parent.resolve())
    if count!=len(expected):raise ValueError('Incomplete archive manifest')
    print(json.dumps(dict(restored_or_identical_files=count,stage_identity_sha256=identity,
        nonlinear_solution_accepted=False,original_runtime_and_source_identity_gates_still_required=True)))


def main():
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('snapshot');p.add_argument('--cache-root',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True);p.add_argument('--expected-stages',type=int)
    p=sub.add_parser('restore');p.add_argument('--manifest',type=Path,required=True)
    p.add_argument('--cache-parent',type=Path,required=True)
    args=parser.parse_args();(snapshot if args.command=='snapshot' else restore)(args)


if __name__=='__main__':main()
