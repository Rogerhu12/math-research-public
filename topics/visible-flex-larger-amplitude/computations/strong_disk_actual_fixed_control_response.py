#!/usr/bin/env python3
"""Optional disk storage for the original accepted fixed-g control response.

The input must still be a genuinely checked fixed view with M core parameters.
This does not relabel an M+3 design endpoint or create a new nonlinear solution.
All original complete-H identities, full-field forcing, half-step checks and
original matrix residual checks remain. Every QR solve additionally receives
the production backend's complete streamed numerical backward-error gate.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ORIGINAL = HERE/'strong_actual_fixed_control_response.py'
EXPECTED = {
    'strong_actual_fixed_control_response.py': 'a2552b5b67e7555b3d402f10127a89fcf99eea566d7768a4050535c8105c2de1',
    'strong_disk_actual_backend.py': '402830e66390f660d7f8e846165a2ae7c1e9858addc2317df06348dc1e8634f1',
    'root_disk_block_collocation.py': 'f252024e7193b0e98c6f243b9dc6814c94c28c358e059b8a901da8e6396620b2',
}


def digest(value):
    return hashlib.sha256(value).hexdigest()


def transformed_source():
    sources = {}
    for name, expected in EXPECTED.items():
        value = (HERE/name).read_bytes()
        actual = digest(value)
        if actual != expected:
            raise ValueError('Frozen response/backend source differs: '+name)
        sources[str(HERE/name)] = actual
    sources[str(Path(__file__))] = digest(Path(__file__).read_bytes())
    original = ORIGINAL.read_text()
    edits = [
        (
            "    hashes={str(Path(__file__)):digest(__file__)}\n",
            "    hashes={str(Path(__file__)):digest(__file__)}\n"
            "    hashes.update(DISK_WRAPPER_SOURCE_HASHES)\n",
        ),
        (
            "    if opts.metadata_only:\n",
            "    input_report['disk_response_adapter'] = DISK_WRAPPER_PROVENANCE\n"
            "    if opts.metadata_only:\n",
        ),
        (
            "    import root_block_collocation as blocks\n",
            "    from strong_disk_actual_backend import install_disk_backend\n"
            "    disk_runtime = install_disk_backend(bounded, prefix, DISK_WRAPPER_CONFIGURATION)\n"
            "    blocks = bounded.blocks\n",
        ),
        (
            "        output.write_text(json.dumps(result,indent=2)+'\\n')\n",
            "        result['disk_block_storage'] = dict(\n"
            "            adapter=DISK_WRAPPER_PROVENANCE, configuration=DISK_WRAPPER_CONFIGURATION,\n"
            "            stats=dict(disk_runtime.stats), original_full_field_checks_preserved=True,\n"
            "            numerical_backward_check_is_not_an_interval_inverse_certificate=True)\n"
            "        output.write_text(json.dumps(result,indent=2)+'\\n')\n",
        ),
        (
            "        for function,default in zip(functions,defaults):function.__defaults__=default\n",
            "        for function,default in zip(functions,defaults):function.__defaults__=default\n"
            "        disk_runtime.finish()\n",
        ),
    ]
    changed = original
    records = []
    for before, after in edits:
        count = changed.count(before)
        if count != 1:
            raise ValueError('Expected exactly one frozen response transform anchor: '+repr(before))
        changed = changed.replace(before, after, 1)
        records.append(dict(before=before, after=after, replacements=count))
    ast.parse(changed, filename='<disk-stored-original-fixed-control-response>')
    provenance = dict(
        scope=__doc__, original_source_sha256=digest(original.encode()),
        transformed_source_sha256=digest(changed.encode()), source_sha256=sources,
        explicit_transforms=records, original_source_file_unchanged=True,
        original_fixed_input_identity_gate_preserved=True,
        accepted_M_plus_3_design_requires_real_fixed_view_conversion=True,
        original_forcing_and_half_step_rules_preserved=True,
        original_full_matrix_residual_checks_preserved=True,
        independent_tail_worker_started=False,
    )
    return changed, provenance


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--disk-backward-error-tol', type=float, default=5e-11)
    parser.add_argument('--disk-heartbeat-seconds', type=float, default=20.)
    parser.add_argument('--disk-temporary-parent', type=Path)
    opts, remaining = parser.parse_known_args()
    if not 0 < opts.disk_backward_error_tol <= 5e-11:
        raise ValueError('Use the checked numerical backward-error threshold or a stricter one')
    if not 5 <= opts.disk_heartbeat_seconds <= 60:
        raise ValueError('Owned-process heartbeat must be between 5 and 60 seconds')
    configuration = dict(
        backward_error_tolerance=opts.disk_backward_error_tol,
        heartbeat_seconds=opts.disk_heartbeat_seconds,
        temporary_parent=None if opts.disk_temporary_parent is None else str(opts.disk_temporary_parent.resolve()),
        purpose='original accepted fixed-g complete control response with disk storage',
    )
    text, provenance = transformed_source()
    namespace = dict(
        __name__='strong_disk_stored_original_fixed_response', __file__=str(ORIGINAL),
        DISK_WRAPPER_CONFIGURATION=configuration,
        DISK_WRAPPER_SOURCE_HASHES=provenance['source_sha256'],
        DISK_WRAPPER_PROVENANCE=provenance,
    )
    old_argv = sys.argv
    sys.argv = [old_argv[0], *remaining]
    try:
        exec(compile(text, '<disk-stored-original-fixed-control-response>', 'exec'), namespace)
        namespace['main']()
    finally:
        sys.argv = old_argv


if __name__ == '__main__':
    main()
