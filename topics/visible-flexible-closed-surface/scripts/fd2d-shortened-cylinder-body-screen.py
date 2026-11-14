#!/usr/bin/env python3
"""Explicit complete-native body dispatch, including R168 cylinder shortening.

Arguments are --native-definition DEFINITION and the existing finite body
settings. Either the current independent-tail native schema or its explicit
shortened-cylinder wrapper is accepted. No schema is inferred from dimensions.
Only dispatch/report metadata changes; all finite integration and actual
Cartesian/cut formulas are reused from the frozen body driver.
"""
from __future__ import annotations
import os
for _thread_key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_thread_key]='1'
import argparse
import importlib.util
import json
from pathlib import Path
import sys
from fd2d_gc_raw_native_field import identity
from fd2d_gc_actual_body_reader_factory import load_actual_body_reader
from fd2d_gc_independent_tail_native_field import SCHEMA as INDEPENDENT_SCHEMA
from fd2d_gc_shortened_cylinder_native import load_shortened_body_reader,SCHEMA as SHORTENED_SCHEMA

HERE=Path(__file__).resolve().parent


def load_reader(path):
    schema=json.loads(Path(path).read_text()).get('schema')
    if schema==SHORTENED_SCHEMA:return load_shortened_body_reader(path)
    if schema==INDEPENDENT_SCHEMA:return load_actual_body_reader(path)
    raise ValueError('Unsupported explicitly bound native schema: '+str(schema))


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__,add_help=False)
    ap.add_argument('--native-definition',type=Path,required=True)
    ap.add_argument('-h','--help',action='store_true')
    args,rest=ap.parse_known_args(argv)
    if any(v==key or v.startswith(key+'=') for v in rest for key in ('--field','--report')):
        ap.error('The field and report are bound by --native-definition')
    if args.help:
        print(__doc__)
        print('Required: --native-definition FILE --out-prefix FRESH_PREFIX; '
              'forwarded: --angles, --radial-samples-per-span, --rtol, --atol, '
              '--max-step, --max-rhs-evaluations')
        return 0
    reader=load_reader(args.native_definition)
    native_definition=reader.definition()
    definition_identity=identity(args.native_definition)
    path=HERE/'fd2d-metric-bump-body-screen-v2.py'
    spec=importlib.util.spec_from_file_location('fd2d_complete_body_driver_instance',path)
    driver=importlib.util.module_from_spec(spec);spec.loader.exec_module(driver)
    original_bound,original_write=driver.bound_reader,driver.BODY.atomic_json

    def explicit_bound(field,report,report_path):
        if identity(field)['sha256']!=native_definition['arrays']['sha256']:
            raise ValueError('Selected actual parent coefficient archive changed')
        if identity(report_path)['sha256']!=definition_identity['sha256']:
            raise ValueError('Native definition changed after binding')
        if report.get('schema')!=native_definition['schema']:
            raise ValueError('Different bound native schema')
        return reader,reader.body_adapter_definition()

    def truthful_report(output,packet):
        if packet.get('schema')=='fd2d-physical-bump-actual-body-finite-screen-v2':
            packet=dict(packet)
            packet.update(schema='fd2d-complete-native-actual-body-finite-screen-v2',
                source=identity(__file__),unchanged_finite_integration_driver=identity(path),
                bound_native_definition=definition_identity,
                adapter_definition=reader.body_adapter_definition(),
                consumer_sources=native_definition['sources']+[identity(HERE/name) for name in (
                    'fd2d_gc_actual_body_reader_factory.py','fd2d-metric-raw-body-screen.py',
                    'fd2d_gc_raw_native_field.py','fd2d_gc_archive_arrays.py')],
                legacy_seed_only_reader_invoked=False,
                auxiliary_l_is_independent=False,auxiliary_n_is_independent=False,
                auxiliary_fields='Actual complete R153 coast / R155 terminal functions, with an optional exact R168 pullback',
                mathematical_metric_changed_from_parent=bool(native_definition.get('physical_metric_changed_from_parent',False)),
                exact_cut_radial_II_derivatives_requested=False,
                original_integration_and_registration_formulas_unchanged=True)
        return original_write(output,packet)

    old_argv=sys.argv
    driver.bound_reader=explicit_bound;driver.BODY.atomic_json=truthful_report
    sys.argv=[str(Path(__file__)),'--field',str(reader.arrays_path),
        '--report',str(args.native_definition),*rest]
    try:return driver.main()
    finally:
        driver.bound_reader=original_bound;driver.BODY.atomic_json=original_write
        sys.argv=old_argv


if __name__=='__main__':raise SystemExit(main())
