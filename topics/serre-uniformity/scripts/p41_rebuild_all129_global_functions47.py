#!/usr/bin/env python3
"""Rebuild the exact R304 snapshot, keeping the earlier pure j01 chain distinct."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir',type=Path,required=True)
    ap.add_argument('--snapshot',type=Path,required=True)
    ap.add_argument('--input-root',type=Path)
    ap.add_argument('--work-dir',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    scripts=args.script_dir.resolve()
    root=(args.input_root or scripts/'data').resolve()
    snapshot=json.loads(args.snapshot.read_text())
    core=Path(__file__).resolve().with_name('p41_all129_global_functions47.py')
    assert sha(core)==snapshot['assembler_sha256']
    assert sha(scripts/'p41_three_ordinary_CM_anchors47.py')==snapshot['global_series_module_sha256']
    ordinary=args.work_dir.resolve()/'ordinary-inputs'
    ordinary.mkdir(parents=True,exist_ok=True)
    def resolve(record):
        rel=Path(record['published_relative_path'])
        assert not rel.is_absolute() and '..' not in rel.parts
        p=(root/rel).resolve(strict=True)
        assert sha(p)==record['sha256'],rel
        return p
    for record in snapshot['ordinary_inputs']:
        for kind in ['Abel','multiply']:
            source=resolve(record[kind])
            target=ordinary/(record['disk_id']+'_'+kind+'47.json.gz')
            if target.exists():assert sha(target)==record[kind]['sha256']
            else:target.symlink_to(source)
    common={k:resolve(v) for k,v in snapshot['common_inputs'].items()}
    subprocess.run([sys.executable,str(core),'--script-dir',str(scripts),
        '--known113',str(common['known113']),'--tiny',str(common['tiny']),
        '--polynomials',str(common['polynomials']),'--ordinary-workdir',str(ordinary),
        '--output',str(args.output)],check=True)
    assert sha(args.output)==snapshot['expected_output_sha256']
    print('PASS exact R304 snapshot and byte-identical global output',sha(args.output))


if __name__=='__main__':main()
