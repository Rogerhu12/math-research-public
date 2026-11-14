#!/usr/bin/env python3
"""Losslessly reconstruct redundant native row reports from the final certificate.

The canonical complete report retains every original mathematical row.
This small manifest retains the original report headers, completion and
failure states, scope, actual hashes, and commands. Original files are
neither deleted nor modified. No numerical gate is rerun or relabelled.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json
from pathlib import Path


def digest(raw):return hashlib.sha256(raw).hexdigest()
def read(p):return json.loads(gzip.decompress(Path(p).read_bytes()))
def encoded(doc):return gzip.compress((json.dumps(doc,indent=2,allow_nan=False)+'\n').encode(),mtime=0)


def restore_entry(final,entry):
    rows=[]
    for i in range(entry['first_common_row'],entry['last_common_row_exclusive']):
        row={k:v for k,v in final['rows'][i].items() if k!='actual_v_L2_phi_upper'}
        if entry['original_rows_have_common_row']:row={'common_row':i,**row}
        rows.append(row)
    doc=dict(entry['original_header_template']);doc['rows']=rows
    raw=encoded(doc)
    if digest(raw)!=entry['original_sha256'] or len(raw)!=entry['original_bytes']:
        raise ValueError('the complete certificate cannot losslessly reconstruct an original native report')
    return raw


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--complete',type=Path,required=True)
    ap.add_argument('--original',type=Path,action='append')
    ap.add_argument('--out',type=Path)
    ap.add_argument('--manifest',type=Path)
    ap.add_argument('--restore-dir',type=Path)
    args=ap.parse_args();final=read(args.complete);complete_sha=digest(args.complete.read_bytes())
    if not final['complete'] or len(final['rows'])!=1528:raise ValueError('the actual full 1528-row certificate is required')
    if args.manifest:
        manifest=json.loads(args.manifest.read_text())
        if manifest['complete_certificate_sha256']!=complete_sha:raise ValueError('the actual complete certificate has changed')
        for entry in manifest['entries']:
            raw=restore_entry(final,entry)
            if args.restore_dir:
                path=args.restore_dir/Path(entry['original_path']).name
                if path.exists():raise FileExistsError('never overwrite an original or restored native')
                path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)
        print(dict(lossless_native_reports=len(manifest['entries']),restored=bool(args.restore_dir)))
        return
    if not args.original or not args.out or args.out.exists():raise ValueError('new manifest output and original reports are required')
    manifest=dict(kind='lossless_complete_moving_energy_native_reconstruction',complete=True,
        source_sha256=digest(Path(__file__).read_bytes()),complete_certificate=str(args.complete),
        complete_certificate_sha256=complete_sha,complete_certificate_contains_all_original_mathematical_rows=True,
        large_original_reports_remain_local_and_are_not_required_for_repository_reproduction=True,
        no_original_file_deleted_or_changed=True,entries=[])
    for path in args.original:
        original=read(path);first=original.get('first_common_row',0);last=first+len(original['rows'])
        header=dict(original);header['rows']=[]
        has_common=bool(original['rows'] and 'common_row' in original['rows'][0])
        producer=('scripts/fourfold_codazzi_moving_mean_energy_prefix_v2.py' if not has_common else
            'scripts/fourfold_codazzi_moving_mean_energy_direct_rows.py' if 'direct_complete' in original['kind'] else
            'scripts/fourfold_codazzi_moving_mean_energy_rows.py')
        candidate=next(k for k in original['inputs'] if k.endswith('-candidate.json'))
        command=f'PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python {producer} --candidate {candidate}'
        command+=(f' --first-row {first} --row-count {last-first}' if has_common else ' --right 119/500 --angles 4096')
        command+=f' --out {path}'
        entry=dict(original_path=str(path),original_sha256=digest(path.read_bytes()),original_bytes=path.stat().st_size,
            original_kind=original['kind'],original_source_sha256=original['source_sha256'],
            original_complete=original['complete'],original_failure=original['failure'],
            first_common_row=first,last_common_row_exclusive=last,original_rows_have_common_row=has_common,
            actual_original_command=command,
            original_process_observation=('normal exit 0 after the stated complete part' if original['complete'] else
                'session 7649 unavailable after 599 saved complete rows; no exit code or cause was observed'),
            reconstruction='remove the added actual_v_L2_phi_upper field; restore common_row if present; insert into the unchanged ordered header template; json indent=2 plus newline, deterministic gzip mtime=0',
            original_header_template=header)
        raw=restore_entry(final,entry)
        if raw!=path.read_bytes():raise ValueError('exact reconstructed bytes differ from the preserved original')
        entry['exact_byte_reconstruction_checked']=True;manifest['entries'].append(entry)
    args.out.write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')
    print(dict(complete=True,reports=len(manifest['entries']),manifest_bytes=args.out.stat().st_size,
        all_original_bytes_reconstructed_exactly=True,source_sha256=manifest['source_sha256']))


if __name__=='__main__':main()
