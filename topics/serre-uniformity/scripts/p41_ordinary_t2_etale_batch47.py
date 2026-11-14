#!/usr/bin/env python3
"""Checkpoint all nineteen actual ordinary T2 etale supports."""
import argparse
from pathlib import Path
import subprocess
import sys

from p41_ordinary_t2_etale_support47 import read, save, sha


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--ordinary-lifts', type=Path, required=True)
    ap.add_argument('--output-dir', type=Path, required=True)
    ap.add_argument('--seed-dir', type=Path)
    ap.add_argument('--aggregate', type=Path, required=True)
    args = ap.parse_args()
    source = Path(__file__).with_name('p41_ordinary_t2_etale_support47.py')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    lifts = read(args.ordinary_lifts)
    records = []
    for point in sorted(lifts['points'], key=lambda p: p['j_mod47']):
        j = point['j_mod47']
        disk = 'ORD_j'+str(j).zfill(2)
        output = args.output_dir/(disk+'_actual_T2_support47.json.gz')
        seed = args.seed_dir/output.name if args.seed_dir is not None else None
        if not output.exists() and seed is not None and seed.exists():
            seed_data = read(seed)
            assert seed_data['complete_actual_T2_support'] and seed_data['source_disk_id'] == disk
            output.write_bytes(seed.read_bytes())
        complete = output.exists() and read(output)['complete_actual_T2_support']
        if not complete:
            subprocess.run([sys.executable, str(source), '--script-dir', str(args.script_dir),
                            '--ordinary-lifts', str(args.ordinary_lifts), '--j', str(j),
                            '--output', str(output)], check=True)
        data = read(output)
        assert data['complete_actual_T2_support'] and data['all54_canonical_T2_trace_identity_verified']
        assert data['all2701_actual_quadratic_products_verified']
        assert data['source_curve'] == [point['curve_A'], point['curve_B']]
        assert data['input_sha256'][args.ordinary_lifts.name] == sha(args.ordinary_lifts)
        records.append({'disk_id': disk, 'j_mod47': j, 'basename': output.name,
                        'sha256': sha(output), 'bytes': output.stat().st_size,
                        'kernel_factor_degrees_mod47': data.get('kernel_factor_degrees_mod47', [[3, 1]]),
                        'all54_actual_T2_trace_and2701_quadratic_identities_verified': True})
        aggregate = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
                     'complete_all19_actual_T2_supports': len(records) == 19,
                     'completed_disk_count': len(records), 'records': records,
                     'input_sha256': {args.ordinary_lifts.name: sha(args.ordinary_lifts)},
                     'source_sha256': sha(__file__), 'etale_executor_sha256': sha(source),
                     'complete_local_QC_heights': False, 'complete_common_roots': False}
        save(args.aggregate, aggregate)
        print('CHECKPOINT all19 actual T2 supports', len(records), '/19', disk, 'SHA', sha(output), flush=True)


if __name__ == '__main__':
    main()
