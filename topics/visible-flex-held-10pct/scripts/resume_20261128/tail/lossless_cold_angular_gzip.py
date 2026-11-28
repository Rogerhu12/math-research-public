#!/usr/bin/env python3
"""Losslessly archive complete, explicitly cold prefix angular-table NPZ files.

Only an outer gzip stream is added. The original ZIP bytes and every array are
unchanged. A durable manifest and complete on-disk decompression verification
precede removal of each original. Summary/defining-jets/active inputs are untouched.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import time
import zlib

CHUNK = 1024**2


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def durable(path, value):
    temp=path.with_name(path.name+'.tmp')
    with temp.open('w') as stream:
        json.dump(value,stream,indent=2,allow_nan=False)
        stream.write('\n');stream.flush();os.fsync(stream.fileno())
    temp.replace(path)
    fd=os.open(path.parent,os.O_RDONLY)
    try:os.fsync(fd)
    finally:os.close(fd)


def unpack_check(path, expected_size, expected_sha, output=None):
    digest=hashlib.sha256();length=0
    with gzip.open(path,'rb') as stream:
        while data:=stream.read(CHUNK):
            length+=len(data);digest.update(data)
            if output is not None:output.write(data)
    if length!=expected_size or digest.hexdigest()!=expected_sha:
        raise ValueError('Complete restored original bytes/SHA differ')
    return dict(restored_bytes=length,restored_sha256=digest.hexdigest())


def archive(args):
    if args.reserve_mib<128:
        raise ValueError('Keep at least 128 MiB free during this cold-file maintenance')
    out=args.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    reserve=args.reserve_mib*1024**2
    record=dict(schema='complete-cold-prefix-angular-npz-outer-gzip-v1',
                status='preparing',source=ref(__file__),zlib_version=zlib.ZLIB_VERSION,
                algorithm='zlib gzip wrapper wbits31, level6, 1048576-byte source chunks, final flush',
                reserve_bytes=reserve,entries=[],actual_allocated_bytes_released=0,
                old_summary_and_exact_defining_jets_modified=False,
                numerical_arrays_or_inner_zip_bytes_changed=False)
    manifest=out/'manifest.json'
    expected=[]
    for summary_path in args.table_summary:
        summary_ref=ref(summary_path)
        value=json.loads(Path(summary_path).read_text())
        target=value['angular_tables'];path=Path(target['path']).resolve()
        if (path.name!='continuous-angular-three-jets.npz'
                or path.parent!=Path(summary_path).resolve().parent
                or sha(path)!=target['sha256'] or path.stat().st_nlink!=1):
            raise ValueError('Use the complete single-link explicitly selected cold angular NPZ')
        if path in [v[0] for v in expected]:
            raise ValueError('A cold file was listed twice')
        expected.append((path,target,summary_ref))
    record['status']='archiving';durable(manifest,record)
    started=time.monotonic()
    for number,(path,target,summary_ref) in enumerate(expected):
        before=path.stat()
        # This intentionally generous envelope exceeds gzip/deflate framing.
        # Every actual write is separately checked, so outside disk users
        # cannot make this initial estimate consume the protected reserve.
        worst=before.st_size+before.st_size//100+CHUNK
        while shutil.disk_usage(out).free<reserve+worst:
            print(json.dumps(dict(event='cold_archive_waiting_before_write',path=str(path),
                                  free_bytes=shutil.disk_usage(out).free,
                                  worst_complete_archive_bytes=worst,reserve_bytes=reserve)),flush=True)
            time.sleep(5)
        archive_path=out/f'{number:02d}-complete-angular-table.npz.gz'
        temp=archive_path.with_name(archive_path.name+'.tmp')
        raw_hash=hashlib.sha256();gz_hash=hashlib.sha256();raw_bytes=gz_bytes=0
        compressor=zlib.compressobj(6,zlib.DEFLATED,31)
        try:
            with path.open('rb') as source,temp.open('xb') as destination:
                def emit(data):
                    nonlocal gz_bytes
                    if not data:return
                    if shutil.disk_usage(out).free<reserve+len(data)+CHUNK:
                        raise OSError('External disk use reached the live-science reserve; original retained')
                    destination.write(data);gz_hash.update(data);gz_bytes+=len(data)
                    if gz_bytes>worst:
                        raise ArithmeticError('Conservative complete-file gzip envelope exceeded')
                while block:=source.read(CHUNK):
                    raw_hash.update(block);raw_bytes+=len(block);emit(compressor.compress(block))
                emit(compressor.flush());destination.flush();os.fsync(destination.fileno())
            if raw_hash.hexdigest()!=target['sha256'] or raw_bytes!=before.st_size:
                raise ValueError('Cold source changed while being read')
            if sha(temp)!=gz_hash.hexdigest():
                raise ValueError('On-disk archive bytes differ from the written stream')
            restored=unpack_check(temp,raw_bytes,target['sha256'])
            if sha(path)!=target['sha256'] or path.stat().st_size!=before.st_size:
                raise ValueError('Original changed before replacement')
            temp.replace(archive_path)
            row=dict(original=target,source_table_summary=summary_ref,
                     original_bytes=raw_bytes,original_allocated_bytes=before.st_blocks*512,
                     original_mode=stat.S_IMODE(before.st_mode),original_mtime_ns=before.st_mtime_ns,
                     archive=ref(archive_path),archive_bytes=gz_bytes,
                     archive_allocated_bytes=archive_path.stat().st_blocks*512,
                     on_disk_full_decompression_verified=restored,
                     original_second_full_SHA_verified=True,
                     state='archive_verified_original_still_present')
            record['entries'].append(row);durable(manifest,record)
            path.unlink()
            row['state']='archived_original_exactly_restorable'
            row['actual_allocated_bytes_released']=row['original_allocated_bytes']-row['archive_allocated_bytes']
            record['actual_allocated_bytes_released']+=row['actual_allocated_bytes_released']
            record['seconds']=time.monotonic()-started;durable(manifest,record)
            print(json.dumps(dict(event='cold_angular_archive_verified',original=str(path),
                                  original_bytes=raw_bytes,archive_bytes=gz_bytes,
                                  actual_allocated_bytes_released=row['actual_allocated_bytes_released'])),flush=True)
        except Exception as exc:
            # Any incomplete candidate has no unique scientific bytes. Keep
            # every original until its independent restoration proof exists.
            if temp.exists():temp.unlink()
            record.update(status='cold_archive_stopped_original_preserved',error=repr(exc),
                          seconds=time.monotonic()-started)
            durable(manifest,record);raise
    record.update(status='all_selected_cold_angular_files_losslessly_archived',
                  seconds=time.monotonic()-started)
    durable(manifest,record)
    print(json.dumps(dict(status=record['status'],manifest=ref(manifest),
                          actual_allocated_bytes_released=record['actual_allocated_bytes_released'])),flush=True)


def restore(args):
    record=json.loads(args.manifest.read_text())
    path=args.original_path.resolve()
    rows=[row for row in record['entries'] if Path(row['original']['path'])==path]
    if len(rows)!=1:
        raise ValueError('The manifest does not identify this exact original path')
    row=rows[0]
    if ref(row['archive']['path'])!=row['archive']:
        raise ValueError('The complete gzip archive changed')
    if args.verify_only:
        result=unpack_check(row['archive']['path'],row['original_bytes'],row['original']['sha256'])
    elif path.exists():
        if path.stat().st_size!=row['original_bytes'] or sha(path)!=row['original']['sha256']:
            raise ValueError('Refusing to overwrite different current bytes')
        result=dict(existing_original_verified=True)
    else:
        if args.reserve_mib<128 or shutil.disk_usage(path.parent).free<row['original_bytes']+args.reserve_mib*1024**2:
            raise OSError('Not enough actual space to restore the complete original while preserving the reserve')
        temp=path.with_name(path.name+'.restore-tmp')
        try:
            with temp.open('xb') as output:
                result=unpack_check(row['archive']['path'],row['original_bytes'],row['original']['sha256'],output)
                output.flush();os.fsync(output.fileno())
            if sha(temp)!=row['original']['sha256']:
                raise ValueError('On-disk restored bytes differ')
            os.chmod(temp,row['original_mode']);os.utime(temp,ns=(row['original_mtime_ns'],row['original_mtime_ns']))
            temp.replace(path)
        except Exception:
            if temp.exists():temp.unlink()
            raise
    print(json.dumps(dict(original_path=str(path),verify_only=args.verify_only,**result)),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='operation',required=True)
    a=sub.add_parser('archive');a.add_argument('--table-summary',type=Path,action='append',required=True)
    a.add_argument('--outdir',type=Path,required=True);a.add_argument('--reserve-mib',type=int,default=128)
    r=sub.add_parser('restore');r.add_argument('--manifest',type=Path,required=True)
    r.add_argument('--original-path',type=Path,required=True);r.add_argument('--verify-only',action='store_true')
    r.add_argument('--reserve-mib',type=int,default=128)
    args=p.parse_args();archive(args) if args.operation=='archive' else restore(args)


if __name__=='__main__':main()
