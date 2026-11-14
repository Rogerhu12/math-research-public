#!/usr/bin/env python3
"""Inspect the full-mean geometry of an actual two-accepted-field secant.

The initial field and physical profile come only from the unchanged
strong_secant_actual_bvp_v2.prepare/verified_secant constructor. The original
all-core M or M+3 restart, prescribed-core correction and inlet correction
remain in strong_actual_augmented_core. The only replaced callback is the
existing explicit unsolved geometry inspection. No residual quadrature,
Newton solve, tail worker, accepted solution or continuous geometry theorem
is produced. All original raw nodes must occur in the supplied common grid.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import inspect
import json
import os
from pathlib import Path
import sys

for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def one(argv, name):
    if argv.count(name) != 1:
        raise ValueError('Require exactly one explicit argument '+name)
    return argv[argv.index(name)+1]


def transformed_main(entry, verified_secant):
    """Install the same three secant hooks without changing any source file."""
    original = inspect.getsource(entry.main)
    edits = [
        ('    if external_shifts and not options.response_data:\n',
         '    if external_shifts and not options.response_data and not verified_secant(\n'
         '            options.actual_reference, options.actual_reference_raw, target, external_shifts):\n'),
        ('    warm = None\n',
         '    warm = verified_secant(options.actual_reference, options.actual_reference_raw,\n'
         '        target, external_shifts, payload=True)\n'),
        ("complete_actual_tangent_warm=warm['provenance'] if warm else None",
         "complete_accepted_secant_warm=warm['provenance'] if warm else None"),
        ('Complete actual-J warm field on the original residual quadrature and a complete-mean C2 cubic physical image; unsolved comparison only.',
         'Complete two-accepted-field secant warm with the original full production mean and actual physical C2 cubic; geometry samples only, with no control derivative or new accepted solution.'),
    ]
    source = original
    for before, after in edits:
        if source.count(before) != 1:
            raise ValueError('The explicit geometry secant source anchor changed')
        source = source.replace(before, after, 1)
    ast.parse(source, filename='<complete-mean-secanted-geometry>')
    namespace = dict(entry.main.__globals__)
    namespace['verified_secant'] = verified_secant
    exec(compile(source, '<complete-mean-secanted-geometry>', 'exec'), namespace)
    return namespace['main'], dict(
        original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
        transformed_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
        source_transforms=[dict(before=a, after=b, count=1) for a, b in edits],
        original_source_files_unchanged=True)


def check_grid(record, argv):
    import numpy as np
    import strong_secant_actual_bvp_v2 as secant
    import strong_actual_augmented_core as augmented
    from strong_actual_fixed_control_response import raw_flat
    current_raw = Path(record['current_raw'])
    raw = secant.read(current_raw)
    current = secant.read(record['current_reference'])
    grid_path = Path(one(argv, '--geometry-grid'))
    grid = json.loads(grid_path.read_text())
    t = np.asarray(grid['numerical_t'], dtype=float)
    hashes = {}
    x = np.asarray(raw_flat(current_raw, raw, 'x', hashes)).reshape(raw['arrays']['x']['shape'])
    M = int(current['modes'])
    if (raw['arrays']['p']['shape'] == [M+3]
            and raw['identity'].get('parameter_layout') != augmented.LAYOUT):
        raise ValueError('The M+3 input must use the original all-core plus physical-offset layout')
    if raw['arrays']['p']['shape'] == [M] and not raw['identity'].get('fixed'):
        raise ValueError('The M-only input must be the original fixed all-core view')
    if (grid.get('raw_sha256') != sha(current_raw)
            or t.ndim != 1 or not np.isfinite(t).all()
            or len(t) < len(x) or t[0] != 0. or t[-1] != 1.
            or not np.all(np.diff(t) > 0) or not np.isin(x, t).all()):
        raise ValueError('The common grid must be bound to and include every current raw node')
    angular = int(grid['angular'])
    if angular < 768 or angular % 768:
        raise ValueError('Retain the original 768-angle curvature witness grid or a full integer refinement')
    for witness in grid.get('known_reference_witnesses', []):
        i, j = int(witness['radial_index']), int(witness['angular_index'])
        if not 0 <= i < len(t) or not 0 <= j < angular:
            raise ValueError('A saved common-grid witness has an invalid index')
        if 'numerical_t' in witness and t[i] != witness['numerical_t']:
            raise ValueError('A saved radial witness was omitted')
        eta = witness.get('eta', j*2*np.pi/angular)
        if abs(np.angle(np.exp(1j*(j*2*np.pi/angular-eta)))) > 1e-13:
            raise ValueError('A saved angular witness was omitted')
    minimum_mean = max(512, 16*(3*M+1))
    requested_mean = int(one(argv, '--mean-angular')) if '--mean-angular' in argv else 0
    if requested_mean and requested_mean < minimum_mean:
        raise ValueError('The complete original production mean cannot be reduced')
    return dict(grid_file=str(grid_path), grid_sha256=sha(grid_path),
        current_raw_sha256=sha(current_raw), original_raw_nodes=len(x),
        geometry_radial_nodes=len(t), angular=angular,
        complete_mean_angular=requested_mean or minimum_mean,
        original_mean_angular=minimum_mean, all_raw_nodes_present=True,
        saved_witnesses_checked=len(grid.get('known_reference_witnesses', [])),
        raw_array_sha256=hashes, original_parameter_count=raw['arrays']['p']['shape'][0],
        M_or_Mplus3_layout_preserved=True)


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--secant-previous-reference', type=Path, required=True)
    parser.add_argument('--secant-previous-raw', type=Path, required=True)
    parser.add_argument('--secant-scale', type=float, required=True)
    parser.add_argument('--secant-hold-initial-height', action='store_true')
    parser.add_argument('--secant-geometry-prepare-only', action='store_true')
    options, remaining = parser.parse_known_args()
    if any(flag in remaining for flag in (
            '--response-data', '--target-core', '--neutral-control-step',
            '--resume-actual-iterate', '--resume-tail-config', '--inspect-local-output',
            '--prepare-only', '--fixed-reference', '--postprocess-only')):
        raise ValueError('The original two accepted fields supply the complete explicit secant predictor')
    if '--inspect-warm-output' not in remaining:
        raise ValueError('This adapter is restricted to the explicit unsolved geometry inspection')
    import strong_secant_actual_bvp_v2 as secant
    import strong_actual_three_control_bvp as entry
    import root_actual_geometry_field_complete_mean as geometry
    prepared = secant.prepare(options, remaining)
    record, warm = prepared
    grid = check_grid(record, remaining)
    output = Path(one(remaining, '--out-prefix'))
    metadata = Path(str(output)+'-secant-geometry-prepared.json')
    if metadata.exists():
        raise FileExistsError('Use a fresh secant geometry output prefix')
    output.parent.mkdir(parents=True, exist_ok=True)
    patched, transform = transformed_main(entry, secant.verified_secant)
    files = [Path(__file__), Path(secant.__file__), Path(entry.__file__),
             Path(geometry.__file__), HERE/'strong_actual_augmented_core.py',
             HERE/'root_geometry_array_io_resident.py', Path(grid['grid_file'])]
    hashes = dict(record['source_sha256'])
    hashes.update({str(p):sha(p) for p in files})
    metadata.write_text(json.dumps(dict(schema='actual-secanted-complete-mean-geometry-preparation-v1',
        scope=__doc__, prepared_only=True, geometry_executed_by_this_record=False,
        source_and_input_sha256=hashes, original_secant=record,
        source_transform=transform, common_grid=grid,
        baseline_parameter_offsets_rebased_by_original_restart=True,
        original_prescribed_core_and_inlet_corrections_retained=True,
        original_production_mean_and_geometry_code_retained=True,
        new_nonlinear_solution=False, new_true_tail_evaluation=False,
        original_worker_forbidden_during_warm_inspection=True), indent=2)+'\n')
    old_active, old_main, old_argv = secant._ACTIVE, entry.main, sys.argv
    secant._ACTIVE = prepared
    try:
        assert secant.verified_secant(Path(record['current_reference']), Path(record['current_raw']),
                                      record['target_core'], record['external_shifts'], payload=True) is warm
        if options.secant_geometry_prepare_only:
            print(json.dumps(dict(event='actual_secant_geometry_prepared',
                record=str(metadata), sha256=sha(metadata), grid=grid,
                target_core=record['target_core'], original_parameter_count=grid['original_parameter_count'],
                complete_geometry_run=False, worker_started=False)), flush=True)
            return
        remaining += ['--target-core', *map(repr, record['target_core'])]
        for name, value in record['external_shifts'].items():
            remaining += ['--neutral-control-step', name+'='+repr(value)]
        entry.main = patched
        sys.argv = [old_argv[0], *remaining]
        geometry.main()
        for p in files:
            if sha(p) != hashes[str(p)]:
                raise ValueError('A source or common grid changed during the complete geometry run')
    finally:
        secant._ACTIVE, entry.main, sys.argv = old_active, old_main, old_argv


if __name__ == '__main__':
    main()
