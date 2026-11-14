#!/usr/bin/env python3
"""Restore original R160 Phi matrices using certified exact accelerators."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import runpy
import sys


def read(path):
    return json.loads(gzip.decompress(Path(path).read_bytes()))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--raw-output', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_native_r2_linear47 import install
    install_exact_float_mm(r)
    native = install(r, args.build_dir)
    original = args.script_dir/'p41_canonical_restriction47.py'
    expected_path = args.script_dir/'data/p41_canonical_restriction47_candidate1_compact.json.gz'
    expected = read(expected_path)
    temporary_compact = args.raw_output.with_name('p41_restored_candidate1_compact.json.gz')
    sys.argv = [str(original), '--script-dir', str(args.script_dir), '--canonical-candidate', '1',
                '--raw-output', str(args.raw_output), '--compact-output', str(temporary_compact)]
    runpy.run_path(str(original), run_name='__main__')
    actual = read(args.raw_output)
    keys = ['Phi_sha256', 'minimal_polynomial_ascending', 'canonical_coefficients',
            'denominator_coefficients', 'primitive_generator_coefficients',
            'krylov_unit_determinant', 'comparison_cubic_norm']
    for key in keys:
        assert actual[key] == expected[key], key
    for degree in [1, 2, 3]:
        digest = hashlib.sha256(json.dumps(actual['Phi'+str(degree)], separators=(',', ':')).encode()).hexdigest()
        assert digest == expected['Phi_sha256'][str(degree)]
    output = {'level': 41, 'auxiliary_prime': 47, 'precision': 4,
              'complete_actual_canonical_candidate1_Phi_restoration': True,
              'all_three_Phi_hashes_match_R160': True,
              'all_exact_comparison_keys': keys,
              'input_compact_sha256': sha(expected_path),
              'original_generator_sha256': sha(original),
              'raw_restored_sha256': sha(args.raw_output),
              'original_recorded_raw_sha256': expected['raw_rebuild_sha256'],
              'raw_bytes_identical_to_original_recorded': sha(args.raw_output) == expected['raw_rebuild_sha256'],
              'exact_native_engine': native, 'source_sha256': sha(__file__)}
    args.output.write_text(json.dumps(output, sort_keys=True, indent=2)+'\n')
    print('PASS ALL3 ORIGINAL CANONICAL PHI HASHES', sha(args.raw_output),
          'old exact bytes', output['raw_bytes_identical_to_original_recorded'], flush=True)


if __name__ == '__main__':
    main()
