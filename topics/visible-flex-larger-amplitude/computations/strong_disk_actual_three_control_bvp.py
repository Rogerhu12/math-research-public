#!/usr/bin/env python3
"""Run the original exact-raw actual continuation with explicit disk storage.

Only collocation/QR storage, streamed numerical backward checks and owned
resource telemetry are added. All original physical equations, actual core
targets, raw restore guards, nonlinear checks and true-tail gates remain.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
TEMPLATE=HERE/'strong_exact_raw_three_control_bvp.py'
EXPECTED='4c0030c38a34f99b4c9c58c02b7c74e32c2795eb55190c623d71f9771e80cc98'
DISK_EXPECTED='f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--disk-temporary-parent',type=Path)
    parser.add_argument('--disk-backward-error-tol',type=float,default=5e-11)
    parser.add_argument('--disk-heartbeat-seconds',type=float,default=20.)
    own,remaining=parser.parse_known_args()
    if sha(TEMPLATE)!=EXPECTED or sha(HERE/'root_disk_block_collocation.py')!=DISK_EXPECTED:
        raise ValueError('The reviewed production or disk template differs')
    config=dict(temporary_parent=str(own.disk_temporary_parent.resolve()) if own.disk_temporary_parent else None,
        backward_error_tolerance=own.disk_backward_error_tol,
        heartbeat_seconds=own.disk_heartbeat_seconds)
    if not 0<config['backward_error_tolerance']<=1e-8 or not 5<=config['heartbeat_seconds']<=60:
        raise ValueError('Invalid explicit numerical backward-check or heartbeat setting')
    metadata=dict(scope=__doc__,configuration=config,
        entry_sha256=sha(__file__),exact_raw_template_sha256=EXPECTED,
        disk_backend_sha256=sha(HERE/'strong_disk_actual_backend.py'),
        disk_collocation_sha256=DISK_EXPECTED,
        mathematical_equations_and_original_nonlinear_acceptance_unchanged=True,
        every_linear_solve_checked_by_complete_streamed_original_matvec=True)
    spec=importlib.util.spec_from_file_location('strong_disk_original_exactraw_entry',TEMPLATE)
    entry=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(entry)
    additions=[
        ("'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs')",
         "'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs',\n"
         "        'strong_disk_actual_three_control_bvp.py', 'strong_disk_actual_backend.py',\n"
         "        'root_disk_block_collocation.py')"),
        ('    import root_actual_bounded_neck as bounded',
         '    import root_actual_bounded_neck as bounded\n'
         '    from strong_disk_actual_backend import install_disk_backend\n'
         '    disk_runtime = install_disk_backend(bounded, out, '+repr(config)+')'),
        ('    provenance = dict(scope=__doc__, exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status=',
         '    provenance = dict(scope=__doc__, disk_block_backend='+repr(metadata)+', exact_raw_warm_storage_adapter=EXACT_RAW_SOURCE_TRANSFORM, status='),
        ('        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()',
         '        for function, default in zip((radial.value, radial.state_jacobian, bounded.blocks.prepare_sys), defaults):\n'
         '            function.__defaults__ = default\n        gc.collect()\n        disk_runtime.finish()')]
    entry.EDITS=list(entry.EDITS)+additions
    sys.argv=[sys.argv[0]]+remaining
    entry.main()


if __name__=='__main__':
    main()
