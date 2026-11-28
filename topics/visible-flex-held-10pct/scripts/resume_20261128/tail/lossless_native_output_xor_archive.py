#!/usr/bin/env python3
"""Losslessly archive cold complete native OUTPUTS against one permanent output.

This is an explicit output protocol, never an input/template alias. The complete
independent base gzip stays in place. Every target is streamed back, compared
byte for byte with its old gzip, and checked against its original full SHA before
any old copy is removed. The old journal remains unchanged. No solver is run.
"""
import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import time
import numpy as np

SCHEMA='held10-lossless-complete-native-output-xor-v1'
BLOCK=1024**2


def digest(data):return hashlib.sha256(data).hexdigest()
def ref(path):
    p=Path(path).resolve();return dict(path=str(p),sha256=digest(p.read_bytes()))
def checked(item):
    raw=Path(item['path']).read_bytes()
    if digest(raw)!=item['sha256']:raise ValueError('Immutable archive changed: '+item['path'])
    return raw

def save(path,obj):
    path=Path(path);tmp=path.with_name(path.name+'.tmp')
    with tmp.open('w') as f:
        json.dump(obj,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    tmp.replace(path)
    fd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
    try:os.fsync(fd)
    finally:os.close(fd)


def decoded_base(manifest):
    b=manifest['base']
    if b['codec']!='gzip_of_complete_raw_native_output' or b['depends_on_delta']:
        raise ValueError('A complete independent raw-output gzip base is mandatory')
    raw=gzip.decompress(checked(b['archive']))
    if len(raw)!=b['original_bytes'] or digest(raw)!=b['original_sha256']:
        raise ValueError('The permanent full output base failed exact recovery')
    return raw


def restored_chunks(manifest,row):
    if manifest['schema']!=SCHEMA or not row['delta_ready']:raise ValueError('Incomplete output recovery contract')
    checked(manifest['base']['archive']);checked(row['delta_archive'])
    base_hash=hashlib.sha256();result_hash=hashlib.sha256();length=0
    with gzip.open(manifest['base']['archive']['path'],'rb') as b, gzip.open(row['delta_archive']['path'],'rb') as d:
        while True:
            x=b.read(BLOCK);y=d.read(BLOCK)
            if len(x)!=len(y):raise ValueError('XOR base and complete output lengths differ')
            if not x:break
            z=np.bitwise_xor(np.frombuffer(x,dtype=np.uint8),np.frombuffer(y,dtype=np.uint8)).tobytes()
            base_hash.update(x);result_hash.update(z);length+=len(z);yield z
    if (base_hash.hexdigest()!=manifest['base']['original_sha256']
            or length!=manifest['base']['original_bytes'] or length!=row['original_bytes']
            or result_hash.hexdigest()!=row['original_sha256']):
        raise ValueError('Streaming complete original-output recovery failed full SHA or byte count')


def archive(args):
    prior=json.loads(args.journal.read_text());root=Path(prior['source_root']).resolve();out=args.outdir.resolve()
    repo=Path(__file__).resolve().parents[5]
    if repo==out or repo in out.parents or out.exists():raise ValueError('Use a new scratch-only archive directory')
    if prior['status']!='complete_frozen_native_lossless_archival' or not prior['current_pipeline_dependencies_confirmed_external_to_this_root']:
        raise ValueError('Use the already frozen inactive native archive')
    checked(prior['worker_exit'])
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():continue
        try:argv=(p/'cmdline').read_bytes().decode().split('\0')
        except (OSError,UnicodeError):continue
        if str(root.parent) in argv and any('worker' in x or 'wrapper' in x for x in argv):
            raise ValueError('An old native worker identity is still active')
    candidates={r['relative_path']:r for r in prior['rows'] if Path(r['relative_path']).parent==Path('.') and r['relative_path'].endswith('-jac-output.bin')}
    if args.base_output not in candidates:raise ValueError('Select an actual complete top-level native J output as base')
    b=candidates[args.base_output];bp=root/b['archive_relative_path'];bref=dict(path=str(bp),sha256=b['archive_sha256']);checked(bref)
    out.mkdir(parents=True);(out/'deltas').mkdir()
    m=dict(schema=SCHEMA,status='archiving',source=ref(__file__),source_root=str(root),prior_journal=ref(args.journal),
        actual_frozen_worker_exit=prior['worker_exit'],output_role='complete original native state/J wire bytes with all headers and diagnostics',
        base=dict(codec='gzip_of_complete_raw_native_output',depends_on_delta=False,original_relative_path=args.base_output,
            archive=bref,original_bytes=b['original_bytes'],original_sha256=b['original_sha256']),
        rows=[],skipped=[],scientific_bytes_changed=False,current_F_memo_or_fullbundle_modified=False,
        base_permanently_retained=True,large_payloads_in_git=False,maintenance_reserve_bytes=args.reserve_mib*1024**2,
        scratch_free_before=shutil.disk_usage(root).free,started_unix_time=time.time())
    mp=out/'manifest.json';save(mp,m);base=decoded_base(m)
    for name,old in sorted(candidates.items()):
        if name==args.base_output:continue
        if old['original_bytes']!=len(base):raise ValueError('Only complete outputs of equal original lengths may use this base')
        oldp=root/old['archive_relative_path'];oldref=dict(path=str(oldp),sha256=old['archive_sha256']);oldpacked=checked(oldref);raw=gzip.decompress(oldpacked)
        if len(raw)!=old['original_bytes'] or digest(raw)!=old['original_sha256']:raise ValueError('Old target output failed original full SHA')
        delta=np.bitwise_xor(np.frombuffer(base,dtype=np.uint8),np.frombuffer(raw,dtype=np.uint8)).tobytes();packed=gzip.compress(delta,compresslevel=9,mtime=0)
        if len(packed)>=len(oldpacked):
            m['skipped'].append(dict(relative_path=name,reason='actual delta does not reduce storage'));save(mp,m);continue
        while shutil.disk_usage(root).free < len(packed)+m['maintenance_reserve_bytes']:
            print(json.dumps(dict(event='waiting_for_exact_pending_delta_write_reserve',file=name,pending_bytes=len(packed),free=shutil.disk_usage(root).free)),flush=True);time.sleep(5)
        dest=out/'deltas'/(name+'.xor.gz')
        with dest.open('xb') as f:f.write(packed);f.flush();os.fsync(f.fileno())
        stat=oldp.stat();row=dict(relative_path=name,original_bytes=len(raw),original_sha256=old['original_sha256'],
            original_mode=old['original_mode'],original_mtime_ns=old['original_mtime_ns'],prior_gzip_archive=oldref,
            prior_gzip_bytes=len(oldpacked),prior_allocated_bytes=stat.st_blocks*512,prior_link_count=stat.st_nlink,
            delta_archive=ref(dest),delta_gzip_bytes=len(packed),delta_allocated_bytes=dest.stat().st_blocks*512,
            delta_ready=True,streaming_complete_bytes_equal_original=False,prior_gzip_unlinked=False)
        with gzip.open(oldp,'rb') as f:
            for restored in restored_chunks(m,row):
                if restored!=f.read(len(restored)):raise ValueError('A restored output differs byte-for-byte from its complete original')
            if f.read(1):raise ValueError('The old original output has trailing bytes')
        row['streaming_complete_bytes_equal_original']=True;m['rows'].append(row);save(mp,m)
        if args.replace_old_gzip:
            checked(oldref);checked(m['base']['archive']);oldp.unlink();row['prior_gzip_unlinked']=True;save(mp,m)
        saved=(row['prior_allocated_bytes'] if stat.st_nlink==1 and args.replace_old_gzip else 0)-row['delta_allocated_bytes']
        print(json.dumps(dict(event='actual_complete_output_lossless_xor_verified',file=name,old_bytes=len(oldpacked),new_bytes=len(packed),allocated_bytes_saved=saved,old_gzip_unlinked=row['prior_gzip_unlinked'])),flush=True)
    m.update(status='complete_frozen_native_output_lossless_xor_archival',finished_unix_time=time.time(),
        logical_bytes_saved=sum(x['prior_gzip_bytes']-x['delta_gzip_bytes'] for x in m['rows'] if x['prior_gzip_unlinked']),
        allocated_bytes_saved=sum((x['prior_allocated_bytes'] if x['prior_link_count']==1 else 0)-x['delta_allocated_bytes'] for x in m['rows'] if x['prior_gzip_unlinked']),
        scratch_free_after=shutil.disk_usage(root).free)
    save(mp,m);print(json.dumps(dict(status=m['status'],manifest=ref(mp),saved_bytes=m['allocated_bytes_saved'],free_bytes=m['scratch_free_after'])),flush=True)


def restore(args):
    m=json.loads(args.manifest.read_text());decoded_base(m);rows=[x for x in m['rows'] if x['relative_path']==args.relative_path]
    if len(rows)!=1:raise ValueError('Select one exact original output path')
    row=rows[0];root=Path(m['source_root']).resolve();target=(root/row['relative_path']).resolve()
    if not target.is_relative_to(root):raise ValueError('Restoration escapes its frozen output root')
    if args.verify_only:
        for _ in restored_chunks(m,row):pass
    elif target.exists():
        if digest(target.read_bytes())!=row['original_sha256']:raise ValueError('An existing original path has different bytes')
    else:
        if shutil.disk_usage(root).free <row['original_bytes']+16*1024**2:raise RuntimeError('Insufficient space for complete exact restoration')
        temp=target.with_name(target.name+'.output-xor-restore-'+str(os.getpid()))
        with temp.open('xb') as f:
            for block in restored_chunks(m,row):f.write(block)
            f.flush();os.fsync(f.fileno())
        os.chmod(temp,row['original_mode']);os.utime(temp,ns=(row['original_mtime_ns'],row['original_mtime_ns']));os.link(temp,target);temp.unlink()
    print(json.dumps(dict(status='complete_original_output_verified' if args.verify_only else 'complete_original_output_restored',path=str(target),bytes=row['original_bytes'],sha256=row['original_sha256'])),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='mode',required=True)
    a=sub.add_parser('archive');a.add_argument('--journal',type=Path,required=True);a.add_argument('--base-output',required=True);a.add_argument('--outdir',type=Path,required=True);a.add_argument('--replace-old-gzip',action='store_true');a.add_argument('--reserve-mib',type=int,default=64)
    r=sub.add_parser('restore');r.add_argument('--manifest',type=Path,required=True);r.add_argument('--relative-path',required=True);r.add_argument('--verify-only',action='store_true')
    args=p.parse_args()
    if args.mode=='archive':
        if args.reserve_mib<64:raise ValueError('Preserve the authorized 64 MiB cold-maintenance reserve')
        archive(args)
    else:restore(args)
if __name__=='__main__':main()
