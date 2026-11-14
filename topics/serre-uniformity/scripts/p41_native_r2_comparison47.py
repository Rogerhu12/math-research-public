#!/usr/bin/env python3
"""Compare an entire actual AddFlip under the old and native eliminators."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--input', type=Path, required=True)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_formal47_multiply import addflip, point_hash, restore_tuple
    from p41_native_r2_linear47 import install
    d = json.loads(gzip.decompress(args.input.read_bytes()))
    a = ActualModel(args.script_dir.resolve())
    r = a.r
    install_exact_float_mm(r)
    K, A = r.from_json(d['point_coordinates']), r.from_json(d['point_frobenius'])
    assert point_hash(K, A) == d['point_sha256']
    assert r.equal(r.mm(K, A), r.mm(a.M['A2'], r.conjugate(K)))
    assert r.equal(r.mm(A, r.conjugate(A)), r.eye(73))
    rng = random.Random()
    rng.setstate(restore_tuple(d['random_state']))
    start = time.monotonic()
    old = addflip(K, A, K, A, a.M, rng, 'original benchmark', same=True)
    oldtime = time.monotonic()-start
    state = rng.getstate()
    manifest = install(r, args.build_dir)
    rng.setstate(restore_tuple(d['random_state']))
    start = time.monotonic()
    new = addflip(K, A, K, A, a.M, rng, 'native benchmark', same=True)
    newtime = time.monotonic()-start
    assert r.equal(old[0], new[0]) and r.equal(old[1], new[1])
    assert old[2] == new[2] and rng.getstate() == state
    out = {'complete_actual_AddFlip_comparison': True,
           'entire_point_coordinates_and_Frobenius_matrices_equal': True,
           'same_operation_witness_and_PRNG_state': True,
           'original_seconds': oldtime, 'native_seconds': newtime,
           'input_checkpoint_sha256': sha(args.input),
           'output_point_sha256': point_hash(new[0], new[1]),
           'native_manifest': manifest}
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2)+'\n')
    print('PASS entire actual AddFlip comparison', 'original', oldtime, 'native', newtime,
          'same point', point_hash(new[0], new[1]), flush=True)


if __name__ == '__main__':
    main()
