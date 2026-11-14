#!/usr/bin/env python3
"""Close completed prefix metric rows after an interrupted or cleanly stopped consumer.

The existing row bounds are retained verbatim; no new numerical bound is
inferred. A resumed consumer must independently check every exact interval
against its reconstructed full partition and verify all input identities.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path
import zlib


def identity(p):
    p=Path(p).resolve();return dict(file=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--progress',type=Path,required=True);p.add_argument('--rows',type=Path,required=True)
    p.add_argument('--reference',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--closed-rows',type=Path,required=True);p.add_argument('--session',type=int,required=True)
    p.add_argument('--recorded-exit-code',type=int,required=True)
    args=p.parse_args()
    if args.out.exists() or args.closed_rows.exists():raise FileExistsError('Use new checkpoint paths')
    progress=json.loads(args.progress.read_text());reference=json.loads(args.reference.read_text())
    if progress['field']['sha256']!=reference['field']['sha256']:raise ValueError('Changed actual field')
    oldsource=Path(reference['script']['file'])
    if not oldsource.exists():oldsource=Path(__file__).resolve().parent/oldsource.name
    if identity(oldsource)['sha256']!=reference['script']['sha256']:raise ValueError('Changed actual consumer source')
    for key in ('geometry','target','field'):
        if identity(reference[key]['file'])['sha256']!=reference[key]['sha256']:raise ValueError('Changed actual input '+key)
    decoder=zlib.decompressobj(16+zlib.MAX_WBITS);payload=args.rows.read_bytes();text=decoder.decompress(payload)
    lines=text.splitlines(keepends=True)
    if lines and not lines[-1].endswith(b'\n'):lines=lines[:-1]
    first,stop,subdivisions=progress['start'],progress['next_cell'],progress['radial_subdivisions']
    rows=[json.loads(line) for line in lines]
    rows=[r for r in rows if first<=r['cell']<stop]
    expected=[(i,j) for i in range(first,stop) for j in range(subdivisions)]
    if [(r['cell'],r['subdivision']) for r in rows]!=expected:raise ValueError('Incomplete or duplicate completed-cell rows')
    if any(not (math.isfinite(r['linear_operator_upper']) and r['linear_operator_upper']>=0 and
                Q(r['left_exact'])<Q(r['right_exact'])) for r in rows):raise ValueError('Invalid completed row')
    maximum=max(r['linear_operator_upper'] for r in rows)
    if maximum!=progress['maximum']:raise ValueError('Progress maximum disagrees with complete rows')
    args.closed_rows.write_bytes(gzip.compress((''.join(json.dumps(r,separators=(',',':'))+'\n' for r in rows)).encode(),mtime=0))
    keys=('geometry','target','field','target_data','field_bindings','geometry_bindings','tail_storage_adapter')
    report=dict(schema='fd2d-prefix-linear-closed-checkpoint-v1',scope=__doc__,script=identity(__file__),
        old_consumer=reference['script'],input_identity_reference=identity(args.reference),
        inputs={k:reference[k] for k in keys},source_progress=identity(args.progress),
        source_rows=identity(args.rows),source_gzip_eof_present=bool(decoder.eof),
        recorded_actual_session=args.session,recorded_exit_code=args.recorded_exit_code,
        row_data=identity(args.closed_rows),row_format='gzip JSON lines',start=first,stop=stop,
        radial_subdivisions=subdivisions,total_radial_cells=progress['total_radial_cells'],
        linear_operator_upper=maximum,complete_prefix_domain=False,
        bounds_recomputed=False,exact_partition_must_be_rechecked_by_resumed_consumer=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),start=first,stop=stop,maximum=maximum,original_gzip_closed=decoder.eof)))


if __name__=='__main__':main()
