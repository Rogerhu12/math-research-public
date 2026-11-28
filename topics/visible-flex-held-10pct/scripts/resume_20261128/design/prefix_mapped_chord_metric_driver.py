#!/usr/bin/env python3
"""Observe the one original audit in a new complete mapped design process.

The frozen metric observer retains the original FFT and arithmetic and reads
only their existing arrays. The complete mapped/chord/V5 driver is delegated
unchanged. There is no second audit, model evaluation, Jacobian or new gate.
No module or numerical source belonging to an active process is modified.
"""
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1]/'resume_m3'))
import prefix_mapped_chord_checkpoint_driver as base
import metric_audit_observer_v2 as observer

previous = base.previous


def main():
    command = list(sys.argv)
    if '--help' in command or '-h' in command:
        return base.main()
    out = Path(command[command.index('--outdir')+1]).resolve()
    source = Path(command[command.index('--source-topic')+1]).resolve()/'scripts'
    coupler = source/'db6f-prefix-coupled.py'
    adaptive = source/'950f-prefix-adaptive-chart-bvp-v2.py'
    portable = HERE.parents[1]/'resume_m3/portable_prefix_continue.py'
    files = (Path(__file__).resolve(), Path(base.__file__).resolve(),
             Path(observer.__file__).resolve(), coupler, adaptive, portable)
    hashes = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    installations = []
    original_loader = previous.load_module

    def save():
        if out.is_dir():
            record = dict(scope=__doc__, actual_command=command, source_hashes=hashes,
                actual_installations=installations,
                audit_execution_observation='See the actual run prefix_audit.metric_observation; installation alone is not an audit return.',
                added_model_or_RHS_or_J_or_FFT_calls=0,
                original_acceptance_gates_changed=False,
                old_accepted_audits_rerun=False)
            (out/'metric-audit-observer-execution.json').write_text(
                json.dumps(record, indent=2, allow_nan=False)+'\n')

    def load(name, filename):
        loaded = original_loader(name, filename)
        if Path(filename).resolve() != portable:
            return loaded
        source_loader = loaded.module

        def source_module(source_name, source_filename):
            actual = source_loader(source_name, source_filename)
            if Path(source_filename).resolve() == coupler:
                if Path(actual.adaptive.__file__).resolve() != adaptive:
                    raise ValueError('The actual adaptive audit module is not the declared original')
                installations.append(observer.install(actual.adaptive))
                save()
            return actual

        loaded.module = source_module
        return loaded

    previous.load_module = load
    try:
        return base.main()
    finally:
        previous.load_module = original_loader
        save()


if __name__ == '__main__':
    main()
