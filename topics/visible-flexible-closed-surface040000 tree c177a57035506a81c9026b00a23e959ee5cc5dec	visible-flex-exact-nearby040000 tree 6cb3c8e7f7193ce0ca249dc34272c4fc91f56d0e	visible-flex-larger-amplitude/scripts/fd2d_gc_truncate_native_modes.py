#!/usr/bin/env python3
"""Project a saved native field to a smaller space for branch exploration.

This deliberately changes the finite field. It provides a coarse initial
guess only, and neither improves accuracy nor constitutes same-g refinement.
The original full field is read without modification. All discarded native
coefficient bounds are reported, with the physical T retained.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field', type=Path, required=True)
    parser.add_argument('--dimension', type=int, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    old = load_npz(args.field)
    old_k = (old['values'].shape[0] - 1) // 2
    new_k = (args.dimension - 1) // 2
    if args.dimension != 2 * new_k + 1 or not 1 <= new_k < old_k:
        raise ValueError('Select a strictly smaller odd native dimension')
    if old['parameters'].shape != (2 * old_k + 1,):
        raise ValueError('The actual T-design parameter layout is required')
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name + '*')):
        raise FileExistsError(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    arrays = {'mesh': old['mesh'].copy()}
    discarded = {}
    for key in ('values', 'first'):
        value = old[key]
        arrays[key] = np.concatenate((value[:new_k+1],
                                     value[old_k+1:old_k+1+new_k]), axis=0)
        discarded[key] = dict(
            eta_coefficient_l1_at_nodes=float(np.max(np.sum(
                np.abs(value[new_k+1:old_k+1]), axis=0))),
            zeta_coefficient_l1_at_nodes=float(np.max(np.sum(
                np.abs(value[old_k+1+new_k:]), axis=0))))
    p = old['parameters']
    arrays['parameters'] = np.r_[p[:new_k], p[old_k:old_k+new_k], p[-1]]
    for key in ('physical_s', 'radial_scale'):
        if key in old:
            arrays[key] = old[key].copy()
    output = save_npz(stem.with_name(stem.name + '-field.npz'), **arrays)
    report = dict(schema='fd2d-coarse-native-branch-initializer-v1',
                  source=identity(__file__), source_field=identity(args.field),
                  old_dimension=2*old_k+1, new_dimension=2*new_k+1,
                  original_T=float(p[-1]), radial_nodes=len(arrays['mesh']),
                  discarded_native_coefficients=discarded,
                  retained_coefficients_copied_without_arithmetic=True,
                  same_exact_native_field=False, new_solution=False,
                  accuracy_claim=False, output=output)
    path = stem.with_name(stem.name + '-report.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
