#!/usr/bin/env python3
"""Lossless local storage for frozen native inputs sharing a literal template.

The base is an independent raw-gzip archive, never another delta. Every byte
of a target is recovered by XOR with the decompressed base, then its original
SHA256 is checked. Scientific bytes/deltas remain outside Git. The prior
archive journal is immutable history; this new manifest records supersession.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time

import numpy as np

SCHEMA='held10-lossless-native-input-xor-v1'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def ref(path):
    path=Path(path).resolve()
    return dict(path=str(path),sha256=sha(path.read_bytes()))


def checked(item):
    data=Path(item['path']).read_bytes()
    if sha(data)!=item['sha256']:
        raise ValueError('A bound archive changed: '+item['path'])
    return data


def save(path,value):
    path=Path(path);temporary=path.with_name(path.name+'.tmp')
    with temporary.open('w') as stream:
        json.dump(value,stream,indent=2,allow_nan=False);stream.write('\n');stream.flush();os.fsync(stream.fileno())
    temporary.replace(path)


def base_bytes(manifest):
    base=manifest['base']
    if base['codec']!='gzip_of_complete_raw_template' or base.get('depends_on_delta') is not False:
        raise ValueError('The base must be independent complete original bytes')
    raw=gzip.decompress(checked(base['archive']))
    if len(raw)!=base['original_bytes'] or sha(raw)!=base['original_sha256']:
        raise ValueError('The complete original template did not recover')
    return raw


def recover(manifest,row,base=None):
    if manifest['schema']!=SCHEMA or row.get('delta_ready') is not True:
        raise ValueError('No complete verified delta is recorded')
    base=base_bytes(manifest) if base is None else base
    delta=gzip.decompress(checked(row['delta_archive']))
    if len(delta)!=len(base) or len(delta)!=row['original_bytes']:
        raise ValueError('Lossless XOR lengths differ')
    raw=np.bitwise_xor(np.frombuffer(base,dtype=np.uint8),np.frombuffer(delta,dtype=np.uint8)).tobytes()
    if sha(raw)!=row['original_sha256']:
        raise ValueError('The reconstructed complete original bytes failed SHA256')
    return raw


def archive(args):
    journal_path,out=args.journal.resolve(),args.outdir.resolve()
    prior=json.loads(journal_path.read_text());root=Path(prior['source_root']).resolve()
    repo=Path(__file__).resolve().parents[5]
    if out==repo or repo in out.parents or root==repo or repo in root.parents:
        raise ValueError('All scientific bytes and archives must remain outside Git')
    if prior.get('status')!='complete_frozen_native_lossless_archival' or out.exists():
        raise ValueError('Use a completed immutable archive journal and a new output directory')
    rows={row['relative_path']:row for row in prior['rows']}
    base_row=rows['static-template.bin'];base_path=root/base_row['archive_relative_path']
    if ref(base_path)['sha256']!=base_row['archive_sha256']:
        raise ValueError('The independent template archive changed')
    out.mkdir(parents=True);(out/'deltas').mkdir()
    manifest=dict(schema=SCHEMA,status='archiving',source=ref(__file__),source_root=str(root),
        prior_journal=ref(journal_path),base=dict(codec='gzip_of_complete_raw_template',depends_on_delta=False,
            archive=ref(base_path),original_bytes=base_row['original_bytes'],original_sha256=base_row['original_sha256']),
        target_codec='gzip(target_original_bytes XOR complete_template_bytes)',
        scientific_bytes_changed=False,large_payloads_in_git=False,rows=[],started_unix_time=time.time(),
        scratch_free_before=shutil.disk_usage(root).free,old_gzip_removal_requested=args.replace_old_gzip)
    path=out/'manifest.json';save(path,manifest);base=base_bytes(manifest)
    candidates=[r for r in prior['rows'] if Path(r['relative_path']).parent==Path('.')
        and r['relative_path'].endswith('-input.bin') and r['original_bytes']==len(base)]
    for old in candidates:
        original=(root/old['relative_path']).resolve()
        archived=(root/old['archive_relative_path']).resolve()
        if not original.is_relative_to(root) or not archived.is_relative_to(root):
            raise ValueError('The old journal escapes its frozen source root')
        old_ref=dict(path=str(archived),sha256=old['archive_sha256'])
        compressed=checked(old_ref);raw=gzip.decompress(compressed)
        if len(raw)!=old['original_bytes'] or sha(raw)!=old['original_sha256']:
            raise ValueError('The original target archive did not recover')
        delta=np.bitwise_xor(np.frombuffer(base,dtype=np.uint8),np.frombuffer(raw,dtype=np.uint8)).tobytes()
        packed=gzip.compress(delta,compresslevel=9,mtime=0)
        if len(packed)>=len(compressed):
            raise ValueError('A proposed delta does not improve actual storage')
        target=out/'deltas'/(old['relative_path']+'.xor.gz')
        with target.open('xb') as stream:
            stream.write(packed);stream.flush();os.fsync(stream.fileno())
        row=dict(relative_path=old['relative_path'],original_bytes=len(raw),
            original_sha256=old['original_sha256'],original_mode=old['original_mode'],
            original_mtime_ns=old['original_mtime_ns'],prior_gzip_archive=old_ref,
            prior_gzip_bytes=len(compressed),prior_gzip_allocated_bytes=archived.stat().st_blocks*512,
            delta_archive=ref(target),delta_gzip_bytes=len(packed),delta_allocated_bytes=target.stat().st_blocks*512,
            delta_ready=True,all_restored_bytes_equal_original=False,prior_gzip_unlinked=False)
        restored=recover(manifest,row,base)
        if restored!=raw:
            raise ValueError('The independent recovery routine did not match every original byte')
        row['all_restored_bytes_equal_original']=True
        manifest['rows'].append(row);save(path,manifest)
        if args.replace_old_gzip:
            # Durable recovery information and data already exist before removing
            # redundant gzip. A crash after unlink leaves a recoverable ready row.
            checked(old_ref)
            if ref(base_path)!=manifest['base']['archive']:
                raise ValueError('The retained independent base changed')
            archived.unlink();row['prior_gzip_unlinked']=True;save(path,manifest)
        print(json.dumps(dict(event='actual_lossless_delta_verified',file=old['relative_path'],
            old_bytes=len(compressed),new_bytes=len(packed),old_gzip_unlinked=row['prior_gzip_unlinked'])),flush=True)
    manifest.update(status='complete_frozen_native_lossless_xor_archival',finished_unix_time=time.time(),
        total_original_input_bytes=sum(r['original_bytes'] for r in manifest['rows']),
        prior_gzip_bytes=sum(r['prior_gzip_bytes'] for r in manifest['rows']),
        delta_gzip_bytes=sum(r['delta_gzip_bytes'] for r in manifest['rows']),
        allocated_bytes_saved=sum(r['prior_gzip_allocated_bytes']-r['delta_allocated_bytes'] for r in manifest['rows']) if args.replace_old_gzip else 0,
        scratch_free_after=shutil.disk_usage(root).free)
    save(path,manifest)
    print(json.dumps(dict(event='lossless_xor_archive_complete',manifest=ref(path),
        count=len(manifest['rows']),saved_bytes=manifest['allocated_bytes_saved'],free_bytes=manifest['scratch_free_after'])),flush=True)


def restore(args):
    manifest=json.loads(args.manifest.resolve().read_text());base=base_bytes(manifest)
    matches=[r for r in manifest['rows'] if r['relative_path']==args.relative_path]
    if len(matches)!=1:
        raise ValueError('Select exactly one recorded original input path')
    row=matches[0];raw=recover(manifest,row,base)
    root=Path(manifest['source_root']).resolve();target=(root/row['relative_path']).resolve()
    if not target.is_relative_to(root):
        raise ValueError('The restore path escapes the original frozen root')
    if not args.verify_only:
        if target.exists():
            if sha(target.read_bytes())!=row['original_sha256']:
                raise ValueError('An existing target has other bytes; it will not be overwritten')
        else:
            if shutil.disk_usage(root).free<len(raw)+16*1024**2:
                raise RuntimeError('Insufficient space to restore this complete original file')
            temporary=target.with_name(target.name+'.xor-restore-'+str(os.getpid()))
            with temporary.open('xb') as stream:
                stream.write(raw);stream.flush();os.fsync(stream.fileno())
            os.chmod(temporary,row['original_mode'])
            os.utime(temporary,ns=(row['original_mtime_ns'],row['original_mtime_ns']))
            os.link(temporary,target);temporary.unlink()
    print(json.dumps(dict(status='complete_original_bytes_verified' if args.verify_only else 'complete_original_bytes_restored',
        original_path=str(target),bytes=len(raw),sha256=sha(raw))),flush=True)


def main():
    ap=argparse.ArgumentParser(description=__doc__);sub=ap.add_subparsers(dest='mode',required=True)
    a=sub.add_parser('archive');a.add_argument('--journal',type=Path,required=True);a.add_argument('--outdir',type=Path,required=True)
    a.add_argument('--replace-old-gzip',action='store_true')
    r=sub.add_parser('restore');r.add_argument('--manifest',type=Path,required=True);r.add_argument('--relative-path',required=True)
    r.add_argument('--verify-only',action='store_true')
    args=ap.parse_args();archive(args) if args.mode=='archive' else restore(args)


if __name__=='__main__':
    main()
