#!/usr/bin/env python3
"""Full original CSR design with a nodal RAM and scratch-backing gate.

The complete checkpoint is saved before this gate by the stable V5 wrapper.
The original Jacobian/QR construction peak is retained in the budget. Only
actual anonymous RSS is a credit against MemAvailable, and all future factor
backing plus at least 512MiB disk margin must be available before any J.
The exact original equations, domain tests, boundary and final gates remain.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import time
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import prefix_csr_assembly_driver as base
import complete_mapped_memory_budget as budget
import exception_safe_radial_batches as lifecycle
import literal_design_nodal_restart as literal

previous = base.previous


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--memory-baseline-mib', type=float, default=180.7109375)
    parser.add_argument('--memory-misc-mib', type=float, default=64.)
    parser.add_argument('--memory-external-margin-mib', type=float, default=512.)
    parser.add_argument('--storage-disk-margin-mib', type=float, default=512.)
    parser.add_argument('--literal-nodal-restart', type=Path)
    options, rest = parser.parse_known_args()
    if min(options.memory_external_margin_mib, options.storage_disk_margin_mib) < 512:
        raise ValueError('Both RAM and scratch require at least 512MiB external margin')
    if '--help' in rest or '-h' in rest:
        sys.argv = [str(Path(base.__file__)), *rest]
        return base.main()
    out = Path(rest[rest.index('--outdir')+1]).resolve()
    trace = out.with_name(out.name+'-mapped-nodal-budget.jsonl')
    life_trace = out.with_name(out.name+'-flow-lifecycle.jsonl')
    if trace.exists() or life_trace.exists():
        raise FileExistsError('A mapped-resource output trace already exists')
    command = list(sys.argv)
    hashes = {str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in
        (Path(__file__).resolve(), Path(base.__file__).resolve(), Path(budget.__file__).resolve(),
         HERE/'complete_factor_mmap.py', Path(lifecycle.__file__).resolve(),
         Path(literal.__file__).resolve())}
    started = time.monotonic()
    with life_trace.open('x') as stream:
        stream.write(json.dumps(dict(event='exception_safe_collection_installed',
            actual_command=command, source_hashes=hashes, live_caches_cleared=False))+'\n')

    def life_event(row):
        with life_trace.open('a') as stream:
            stream.write(json.dumps(dict(elapsed=time.monotonic()-started,
                                         lifecycle=row), allow_nan=False)+'\n')

    life_stats, restore_life = lifecycle.install(previous, life_event)
    original = _bvp.prepare_sys
    count = 0

    def prepare(n, m, k, fun, bc, fun_jac, bc_jac, x, h):
        col_fun, sys_jac = original(n,m,k,fun,bc,fun_jac,bc_jac,x,h)

        def guarded(y, p, y_middle, f, f_middle, bc0):
            nonlocal count
            count += 1
            pointer = json.loads((out/'latest-unaccepted-nodal-checkpoint.json').read_text())
            if (pointer['nodes'] != m or pointer['state_components'] != n
                    or pointer['parameters'] != k or pointer['accepted_bvp'] is not False):
                raise ValueError('The complete original nodal checkpoint must precede storage gating')
            initial_memory = budget.memory()
            estimate = budget.budget(n,m,k,
                baseline_mib=initial_memory['current_process_rss_bytes']/budget.MIB,
                misc_mib=options.memory_misc_mib,
                external_mib=options.memory_external_margin_mib)
            disk_needed = (estimate['disk_backing']['total_backing_and_manifest_upper_bytes']+
                           int(options.storage_disk_margin_mib*budget.MIB))
            waited = 0
            while True:
                actual = budget.memory()
                disk = shutil.disk_usage(out)
                # Clean mapped pages may already be in MemAvailable. Neither
                # logical mapped size nor file RSS can be an extra credit.
                credit = min(actual['current_process_anonymous_RSS_bytes'],
                             estimate['non_J_baseline_bytes'])
                ram_needed = estimate['process_peak_estimate_bytes']-credit+estimate['external_margin_bytes']
                ram_ok, disk_ok = actual['available_bytes'] >= ram_needed, disk.free >= disk_needed
                row = dict(event='complete_nodal_mapped_storage_gate', ordinal=count,
                    waited_seconds=waited, allowed=ram_ok and disk_ok,
                    RAM_allowed=ram_ok, disk_allowed=disk_ok,
                    anonymous_RSS_credit_bytes=credit,
                    estimated_additional_RAM_required_bytes=ram_needed,
                    full_factor_backing_plus_disk_margin_bytes=disk_needed,
                    current_memory=actual, current_disk=dict(free_bytes=disk.free,total_bytes=disk.total),
                    estimate=estimate, checkpoint=pointer,
                    actual_command=command, source_hashes=hashes,
                    mapped_logical_bytes_credited_as_RSS=False,
                    original_J_and_QR_construction_peak_unchanged=True,
                    original_nonlinear_or_acceptance_gates_changed=False)
                with trace.open('a') as stream:
                    stream.write(json.dumps(row, allow_nan=False)+'\n')
                if (estimate['process_peak_estimate_bytes']+estimate['external_margin_bytes'] > actual['total_bytes']
                        or disk_needed > disk.total):
                    raise MemoryError('The complete current-mesh RAM or scratch budget exceeds host capacity')
                if row['allowed']:
                    return sys_jac(y,p,y_middle,f,f_middle,bc0)
                time.sleep(15)
                waited += 15

        return col_fun, guarded

    restore_literal = None
    if options.literal_nodal_restart is not None:
        if Path(rest[rest.index('--raw-restart')+1]).resolve() != options.literal_nodal_restart.resolve():
            raise ValueError('Literal recovery must use the actual complete original raw input')
        restore_literal = literal.install(previous, options.literal_nodal_restart, out)
    _bvp.prepare_sys = prepare
    sys.argv = [str(Path(base.__file__)), *rest]
    try:
        return base.main()
    finally:
        _bvp.prepare_sys = original
        if restore_literal is not None:
            restore_literal()
        restore_life()
        if out.is_dir():
            (out/'mapped-storage-and-flow-lifecycle.json').write_text(json.dumps(dict(
                scope=__doc__, actual_command=command, source_hashes=hashes,
                radial_lifecycle_statistics=life_stats, map_scope='factor-only',
                original_math_and_gates_changed=False), indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
