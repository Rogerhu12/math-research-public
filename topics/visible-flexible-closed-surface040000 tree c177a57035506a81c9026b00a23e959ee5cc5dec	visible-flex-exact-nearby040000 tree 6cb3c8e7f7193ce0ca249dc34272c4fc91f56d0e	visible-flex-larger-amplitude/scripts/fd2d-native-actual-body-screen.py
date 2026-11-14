#!/usr/bin/env python3
"""Thin explicit-native CLI for the unchanged finite R124/R126 body screen.

Only reader dispatch and report provenance are adapted in this fresh module
instance. The frozen integration, actual Cartesian geometry and single-rigid
cut comparison are called without copying or changing their formulas.
This is a future finite diagnostic entry; creating it performs no body solve.
"""
from __future__ import annotations
import os
for _thread_key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_key] = '1'
import argparse
import importlib.util
from pathlib import Path
import sys
from fd2d_gc_raw_native_field import identity
from fd2d_gc_actual_body_reader_factory import load_actual_body_reader

HERE = Path(__file__).resolve().parent


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, add_help=False)
    ap.add_argument('--native-definition',type=Path,required=True)
    ap.add_argument('-h','--help',action='store_true')
    args,rest = ap.parse_known_args(argv)
    if any(v == key or v.startswith(key+'=') for v in rest for key in ('--field','--report')):
        ap.error('The field and report are fixed by --native-definition; do not override them')
    if args.help:
        print(__doc__)
        print('Required: --native-definition FILE --out-prefix FRESH_PREFIX')
        print('Forwarded unchanged: --angles 8|16|32|64, --radial-samples-per-span N, '
              '--rtol R, --atol A, --max-step S, --max-rhs-evaluations N')
        return 0
    reader = load_actual_body_reader(args.native_definition)
    native_definition = reader.definition()
    definition_identity = identity(args.native_definition)
    source_path = HERE/'fd2d-metric-bump-body-screen-v2.py'
    spec = importlib.util.spec_from_file_location('fd2d_explicit_native_body_driver_instance', source_path)
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    original_bound_reader, original_write = driver.bound_reader, driver.BODY.atomic_json

    def explicit_bound_reader(field, report, report_path):
        if identity(field)['sha256'] != native_definition['arrays']['sha256']:
            raise ValueError('The body field differs from the explicit native input')
        if identity(report_path)['sha256'] != definition_identity['sha256']:
            raise ValueError('The native definition changed after loading')
        if report.get('schema') != native_definition['schema']:
            raise ValueError('Unexpected native definition schema')
        return reader, reader.body_adapter_definition()

    def truthful_report(path, packet):
        if packet.get('schema') == 'fd2d-physical-bump-actual-body-finite-screen-v2':
            packet = dict(packet)
            packet.update(schema='fd2d-explicit-native-actual-body-finite-screen-v1',
                source=identity(__file__), unchanged_finite_integration_driver=identity(source_path),
                bound_native_definition=definition_identity,
                adapter_definition=reader.body_adapter_definition(),
                consumer_sources=native_definition['sources']+[identity(HERE/name) for name in (
                    'fd2d_gc_actual_body_reader_factory.py','fd2d-metric-raw-body-screen.py',
                    'fd2d_gc_raw_native_field.py','fd2d_gc_archive_arrays.py')],
                legacy_seed_only_reader_invoked=False,
                complete_R153_R155_functions_consumed=True,
                exact_cut_radial_II_derivatives_requested=False,
                original_integration_and_registration_formulas_unchanged=True)
        return original_write(path,packet)

    old_argv = sys.argv
    driver.bound_reader = explicit_bound_reader
    driver.BODY.atomic_json = truthful_report
    sys.argv = [str(Path(__file__)), '--field', str(reader.arrays_path),
        '--report',str(args.native_definition),*rest]
    try:
        return driver.main()
    finally:
        driver.bound_reader = original_bound_reader
        driver.BODY.atomic_json = original_write
        sys.argv = old_argv


if __name__ == '__main__':
    raise SystemExit(main())
