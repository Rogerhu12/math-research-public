#!/usr/bin/env python3
"""Resume an actually saved accepted R111 prefix in disjoint native jobs.

The original producer is used unchanged. The complete existing collector is
the only authority for whole-cap coverage. No missing interval is synthesized.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from fractions import Fraction
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prefix', type=Path, required=True)
    ap.add_argument('--out-dir', type=Path, required=True)
    ap.add_argument('--parts', type=int, default=4)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--retained', type=Path)
    args = ap.parse_args()
    os.chdir(Path(__file__).resolve().parents[1])
    raw = args.prefix.read_bytes()
    prefix = json.loads(gzip.decompress(raw))
    if prefix['unresolved_intervals'] or prefix.get('pending_current_piece'):
        raise ValueError('Freeze a complete accepted prefix between scalar pieces')
    cursor = Fraction(1, 4)
    for row in prefix['intervals']:
        a, b = map(Fraction, row['radial_interval'])
        if row['kind'] != 'body' or a != cursor or not a < b:
            raise ValueError('Not an exact contiguous body prefix')
        cursor = b
    if not cursor < 3 or not 1 <= args.workers <= args.parts:
        raise ValueError('Invalid unfinished domain or worker count')
    args.out_dir.mkdir(parents=True, exist_ok=True)
    endpoints = [cursor+(3-cursor)*Fraction(i,args.parts) for i in range(args.parts+1)]
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    manifests = []
    for i, (a,b) in enumerate(zip(endpoints,endpoints[1:])):
        out = args.out_dir/f'continuation_{i}.json.gz'
        command = [sys.executable,'scripts/fourfold_phase_cap_parameter_comparison.py',
                   '--part','body','--body-left',str(a),'--body-right',str(b),
                   '--half-width',prefix['exact_half_width'],
                   '--parameter-radius',prefix['complex_offset_disk_radius'],
                   '--relative-target',prefix['relative_error_target'],
                   '--primitive-nodes',str(prefix['primitive_nodes']),
                   '--angles',str(prefix['angular_nodes']),
                   '--bits',str(prefix['bits']),'--out',str(out)]
        manifests.append(dict(part=i,command=command,output=str(out),
                              exact_interval=[str(a),str(b)],exit_code=None))
    record = dict(kind='actual_native_R111_disjoint_continuations',
                  prefix_path=str(args.prefix),prefix_sha256=hashlib.sha256(raw).hexdigest(),
                  prefix_accepted=len(prefix['intervals']),jobs=manifests,complete=False)
    manifest_path = args.out_dir/'execution_manifest.json'
    def save():
        manifest_path.write_text(json.dumps(record,indent=2)+'\n')
    def run(item):
        with (args.out_dir/f'continuation_{item["part"]}.log').open('w') as log:
            p = subprocess.run(item['command'],env=env,stdout=log,stderr=subprocess.STDOUT)
        return item,p.returncode
    save()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for future in as_completed([pool.submit(run,item) for item in manifests]):
            item,code = future.result()
            item['exit_code'] = code
            path = Path(item['output'])
            if path.exists():
                item['sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
                item['bytes'] = path.stat().st_size
            save()
            print('NATIVE_PART_FINISHED',item['part'],'exit',code,flush=True)
    if any(item['exit_code'] for item in manifests):
        raise RuntimeError('An actual continuation failed; inspect the retained original report')
    full = args.out_dir/'complete_cap_parameter_comparison.json.gz'
    summary = args.out_dir/'complete_cap_parameter_summary.json'
    command=[sys.executable,'scripts/fourfold_phase_cap_parameter_collect.py',
             '--body',str(args.prefix),*[item['output'] for item in manifests],
             '--out',str(full),'--summary',str(summary)]
    subprocess.run(command,env=env,check=True)
    record.update(complete=True,collector_command=command,
                  full_report=dict(path=str(full),sha256=hashlib.sha256(full.read_bytes()).hexdigest()))
    save()
    if args.retained:
        command=[sys.executable,'scripts/fourfold_phase_even_low_parameter_complete.py',
                 '--retained',str(args.retained),'--cap-comparison',str(full),
                 '--out',str(args.out_dir/'actual_whole_parameter_retained_model.json')]
        subprocess.run(command,env=env,check=True)


if __name__ == '__main__':
    main()
