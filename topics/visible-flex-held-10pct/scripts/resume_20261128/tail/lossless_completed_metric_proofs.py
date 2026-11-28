#!/usr/bin/env python3
"""Losslessly archive completed, inactive metric-proof JSON; restore exact paths.

The actual complete closed metric receipt gates the operation. Summary, contract,
map, mean, node index, F and memo inputs are never selected. Every independent
gzip is streamed back and compared byte-for-byte before the original is removed.
No mathematical value is changed or recomputed. Permanent restore metadata stays
outside Git with the complete scientific archives.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import time

COMPLETE_SHA='57ef6e7a86ab6ad6206df6134be31c8c9b174858a69482ac7a4c7b0fba49286a'
SCHEMA='held10-complete-inactive-metric-proof-json-gzip-v1'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ref(p):
    p=Path(p).resolve();return dict(path=str(p),sha256=sha(p))
def save(p,d):
    t=p.with_name(p.name+'.tmp')
    with t.open('w') as f:json.dump(d,f,indent=2,allow_nan=False);f.write('\n');f.flush();os.fsync(f.fileno())
    t.replace(p)
    fd=os.open(p.parent,os.O_RDONLY|os.O_DIRECTORY)
    try:os.fsync(fd)
    finally:os.close(fd)

def no_readers(paths):
    paths=set(map(str,paths))
    for p in Path('/proc').iterdir():
        if not p.name.isdigit():continue
        try:entries=list((p/'fd').iterdir())
        except OSError:continue
        for fd in entries:
            try:name=os.readlink(fd)
            except OSError:continue
            if name in paths:raise ValueError('An active proof reader exists: '+name)

def archive(a):
    root=a.root.resolve();out=a.outdir.resolve();complete=a.complete_metric.resolve()
    if sha(complete)!=COMPLETE_SHA:raise ValueError('Use the actual already completed same-field closed metric receipt')
    c=json.loads(complete.read_text())
    if c['status']!='actual_complete_marked_column_closed_metric_certified' or not c['full_same_fixed_metric_gate_passed']:raise ValueError('The complete proof gate is unpaid')
    finite_path=Path(c['complete_finite_tail_metric']['path']);finite=json.loads(finite_path.read_text())
    if sha(finite_path)!=c['complete_finite_tail_metric']['sha256'] or not finite['complete_finite_chain_metric_certified']:raise ValueError('The actual complete finite proof changed')
    prior_root=Path(c['original_complete_tail_certificate']['path']).parent.parent/'remaining-certify-001'
    current_root=finite_path.parent
    if root not in (prior_root.resolve(),current_root.resolve()):raise ValueError('Only the two explicitly completed metric-proof output roots are permitted')
    if root==prior_root.resolve():paths=sorted(root.glob('stage-[0-9][0-9][0-9][0-9].json'))
    else:paths=sorted(p for p in root.glob('stage-*/*.json') if p.name=='certificate.json' or p.name=='progress.json' or p.name.startswith('Taylor-'))
    if not paths:raise ValueError('No complete frozen proof JSON selected')
    no_readers(paths)
    repo=Path(__file__).resolve().parents[5]
    if out.exists() or out==repo or repo in out.parents:raise ValueError('Use a new scratch-only archive root')
    out.mkdir(parents=True);(out/'proofs').mkdir()
    m=dict(schema=SCHEMA,status='archiving_completed_inactive_metric_proofs',source=ref(__file__),
        complete_metric=ref(complete),complete_finite_metric=ref(finite_path),source_root=str(root),
        selected_files=len(paths),summaries_contracts_maps_means_indices_F_and_memo_untouched=True,
        active_reader_scan_passed=True,scientific_values_or_original_bytes_changed=False,
        maintenance_reserve_bytes=a.reserve_mib*1024**2,rows=[],scratch_free_before=shutil.disk_usage(root).free,
        started_unix_time=time.time(),original_paths_require_explicit_restore_before_reverification=True)
    mp=out/'manifest.json';save(mp,m)
    for i,p in enumerate(paths):
        if p.is_symlink() or not p.is_file():raise ValueError('A selected cold proof path changed type')
        raw=p.read_bytes();doc=json.loads(raw);stage=doc['stage'];relative=str(p.relative_to(root));st=p.stat()
        if stage<0 or stage>=1152:raise ValueError('A selected file is not an original finite-stage proof')
        packed=gzip.compress(raw,compresslevel=9,mtime=0)
        if len(packed)>=len(raw):raise ValueError('This proposed proof archive does not save space')
        while shutil.disk_usage(root).free < len(packed)+m['maintenance_reserve_bytes']:
            print(json.dumps(dict(event='waiting_for_exact_proof_archive_write',pending_bytes=len(packed),free=shutil.disk_usage(root).free)),flush=True);time.sleep(5)
        dest=out/'proofs'/(relative.replace('/','__')+'.gz')
        with dest.open('xb') as f:f.write(packed);f.flush();os.fsync(f.fileno())
        h=hashlib.sha256();n=0
        with gzip.open(dest,'rb') as g,p.open('rb') as old:
            while True:
                b=g.read(1024**2)
                if not b:break
                if old.read(len(b))!=b:raise ValueError('Full streaming restored proof bytes differ')
                h.update(b);n+=len(b)
            if old.read(1):raise ValueError('Unexpected original trailing proof bytes')
        if n!=len(raw) or h.hexdigest()!=hashlib.sha256(raw).hexdigest():raise ValueError('Full restored proof SHA or byte count changed')
        row=dict(relative_path=relative,original_path=str(p),original_sha256=h.hexdigest(),original_bytes=n,
            original_mode=st.st_mode&0o777,original_mtime_ns=st.st_mtime_ns,original_link_count=st.st_nlink,
            original_allocated_bytes=st.st_blocks*512,archive=ref(dest),archive_bytes=len(packed),
            archive_allocated_bytes=dest.stat().st_blocks*512,streamed_complete_bytes_equal_original=True,
            original_unlinked=False)
        m['rows'].append(row);save(mp,m)
        if sha(p)!=row['original_sha256'] or sha(dest)!=row['archive']['sha256']:raise ValueError('A just-verified original or gzip changed')
        p.unlink();row['original_unlinked']=True;save(mp,m)
        if i==0 or (i+1)%100==0:
            saved=sum((x['original_allocated_bytes'] if x['original_link_count']==1 else 0)-x['archive_allocated_bytes'] for x in m['rows'])
            print(json.dumps(dict(event='actual_completed_proof_archives_verified',files=i+1,total_files=len(paths),allocated_bytes_saved=saved,free_bytes=shutil.disk_usage(root).free)),flush=True)
    m.update(status='all_selected_completed_metric_proofs_losslessly_archived',finished_unix_time=time.time(),
        allocated_bytes_saved=sum((x['original_allocated_bytes'] if x['original_link_count']==1 else 0)-x['archive_allocated_bytes'] for x in m['rows']),
        original_bytes=sum(x['original_bytes'] for x in m['rows']),archive_bytes=sum(x['archive_bytes'] for x in m['rows']),scratch_free_after=shutil.disk_usage(root).free)
    save(mp,m);print(json.dumps(dict(status=m['status'],manifest=ref(mp),files=len(paths),saved_bytes=m['allocated_bytes_saved'],free_bytes=m['scratch_free_after'])),flush=True)

def restore(a):
    m=json.loads(a.manifest.read_text())
    if m['schema']!=SCHEMA:raise ValueError('Wrong full-proof restoration schema')
    rows=m['rows'] if a.all else [x for x in m['rows'] if x['relative_path']==a.relative_path]
    if not rows or not a.all and len(rows)!=1:raise ValueError('Select --all or one exact original relative path')
    for row in rows:
        p=Path(row['original_path']);arc=Path(row['archive']['path'])
        if not p.resolve().is_relative_to(Path(m['source_root']).resolve()) or sha(arc)!=row['archive']['sha256']:raise ValueError('A restored proof path or immutable archive changed')
        if p.exists():
            if sha(p)!=row['original_sha256']:raise ValueError('An existing original path has other bytes')
            continue
        if not a.verify_only and shutil.disk_usage(p.parent).free <row['original_bytes']+16*1024**2:raise RuntimeError('Not enough space for complete original proof restoration')
        temp=p.with_name(p.name+'.proof-restore-'+str(os.getpid()));f=None;h=hashlib.sha256();n=0
        try:
            if not a.verify_only:f=temp.open('xb')
            with gzip.open(arc,'rb') as stream:
                while True:
                    b=stream.read(1024**2)
                    if not b:break
                    h.update(b);n+=len(b)
                    if f:f.write(b)
            if n!=row['original_bytes'] or h.hexdigest()!=row['original_sha256']:raise ValueError('Restored complete proof SHA failed')
            if f:
                f.flush();os.fsync(f.fileno());f.close();f=None;os.chmod(temp,row['original_mode']);os.utime(temp,ns=(row['original_mtime_ns'],row['original_mtime_ns']));os.link(temp,p);temp.unlink()
        finally:
            if f:f.close()
    print(json.dumps(dict(status='complete_original_proofs_verified' if a.verify_only else 'complete_original_proofs_restored',files=len(rows))),flush=True)

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='mode',required=True)
    a=sub.add_parser('archive');a.add_argument('--root',type=Path,required=True);a.add_argument('--complete-metric',type=Path,required=True);a.add_argument('--outdir',type=Path,required=True);a.add_argument('--reserve-mib',type=int,default=64)
    r=sub.add_parser('restore');r.add_argument('--manifest',type=Path,required=True);r.add_argument('--relative-path');r.add_argument('--all',action='store_true');r.add_argument('--verify-only',action='store_true')
    args=p.parse_args()
    if args.mode=='archive':
        if args.reserve_mib<64:raise ValueError('Keep the authorized cold-maintenance reserve')
        archive(args)
    else:
        if bool(args.all)==bool(args.relative_path):raise ValueError('Select one restoration mode')
        restore(args)
if __name__=='__main__':main()
