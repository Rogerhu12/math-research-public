#!/usr/bin/env python3
"""Restore redundant strong coefficient parts from the full H1 certificate.

Only original ordered headers, actual identities, and reproduction commands
are kept in the small manifest. The complete certificate already contains
every mathematical row. No original file or completion flag is changed.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json
from pathlib import Path


def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))
def encode(doc):return gzip.compress((json.dumps(doc,indent=2,allow_nan=False)+'\n').encode(),mtime=0)


def rebuild(final,entry):
    lo,hi=entry['first_common_row'],entry['last_common_row_exclusive']
    doc=dict(entry['original_ordered_header']);doc['rows']=final['rows'][lo:hi]
    raw=encode(doc)
    if sha(raw)!=entry['original_sha256'] or len(raw)!=entry['original_bytes']:
        raise ValueError('the complete strong certificate cannot reconstruct the original part')
    return raw


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--complete',type=Path,required=True)
    ap.add_argument('--part',type=Path,action='append')
    ap.add_argument('--out',type=Path)
    ap.add_argument('--manifest',type=Path)
    ap.add_argument('--restore-dir',type=Path)
    args=ap.parse_args();final=read(args.complete);digest=sha(args.complete.read_bytes())
    if not final['complete'] or final['kind']!='actual_full_moving_H1_and_fractional_Cauchy_source':
        raise ValueError('a complete same-kind strong certificate is required')
    if args.manifest:
        manifest=json.loads(args.manifest.read_text())
        if manifest['complete_certificate_sha256']!=digest:raise ValueError('the full certificate changed')
        for entry in manifest['entries']:
            raw=rebuild(final,entry)
            if args.restore_dir:
                p=args.restore_dir/Path(entry['original_path']).name
                if p.exists():raise FileExistsError('preserve every original or restored part')
                p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
        print(dict(losslessly_reconstructed_parts=len(manifest['entries']),restored=bool(args.restore_dir)))
        return
    if not args.part or not args.out or args.out.exists():raise ValueError('new output and original parts are required')
    manifest=dict(kind='lossless_complete_moving_H1_native_reconstruction',complete=True,
        source_sha256=sha(Path(__file__).read_bytes()),complete_certificate=str(args.complete),
        complete_certificate_sha256=digest,all_original_mathematical_rows_in_complete_certificate=True,
        large_parts_remain_local_and_are_not_needed_in_git=True,no_original_file_changed=True,entries=[])
    cursor=0
    for path in args.part:
        part=read(path);lo=part['first_common_row'];hi=part['last_common_row_exclusive']
        if lo!=cursor or not part['complete'] or len(part['rows'])!=hi-lo:
            raise ValueError('the original complete parts do not form the complete ordered union')
        if final['inputs'].get(str(path))!=sha(path.read_bytes()):raise ValueError('the canonical input identity differs')
        header=dict(part);header['rows']=[]
        candidate=next(p for p in part['inputs'] if p.endswith('-candidate.json'))
        energy=next(p for p in part['inputs'] if 'moving-mean-energy' in p and p.endswith('-complete-native.json.gz'))
        command=('PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps OPENBLAS_NUM_THREADS=1 '
            'OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_codazzi_moving_sobolev_rows.py '
            f'--candidate {candidate} --energy {energy} --first-row {lo} --row-count {hi-lo} --out {path}')
        entry=dict(original_path=str(path),original_sha256=sha(path.read_bytes()),original_bytes=path.stat().st_size,
            original_source_sha256=part['source_sha256'],original_kind=part['kind'],
            original_complete=part['complete'],original_failure=part['failure'],
            original_process_observation='normal exit 0 after the stated complete part',
            first_common_row=lo,last_common_row_exclusive=hi,actual_reproduction_command=command,
            original_ordered_header=header,reconstruction='unchanged complete rows into original ordered header; JSON indent=2 and newline; gzip mtime=0')
        if rebuild(final,entry)!=path.read_bytes():raise ValueError('the original bytes do not match')
        entry['exact_byte_reconstruction_checked']=True;manifest['entries'].append(entry);cursor=hi
    if cursor!=len(final['rows']):raise ValueError('the complete strong report has uncovered rows')
    args.out.write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')
    print(dict(complete=True,parts=len(manifest['entries']),rows=cursor,manifest_bytes=args.out.stat().st_size))


if __name__=='__main__':main()
