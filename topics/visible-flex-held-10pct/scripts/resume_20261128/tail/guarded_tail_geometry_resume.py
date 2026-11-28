#!/usr/bin/env python3
"""Continue the original complete geometry pipeline with byte-level disk gates.

Clone only the immutable stage0 progress JSON into a fresh continuation root;
all actual stage0/mean/source references keep their original absolute paths.
Every original calculation and all modes/stages are retained. The added
launchers only wait before writes whose actual bytes would exhaust reserve.
"""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

import geometry_disk_guard


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--stage0-resource-record', type=Path, required=True)
    p.add_argument('--outdir', type=Path, required=True)
    p.add_argument('--disk-reserve-mib', type=int, default=128)
    a = p.parse_args()
    resource_path, out = a.stage0_resource_record.resolve(), a.outdir.resolve()
    record = json.loads(resource_path.read_text())
    if record.get('returncode') != 0 or not record.get('full_spectrum_preserved'):
        raise ValueError('A genuine complete-spectrum stage0 must have returned')
    prior = Path(record['actual_geometry_summary']['path'])
    if ref(prior) != record['actual_geometry_summary']:
        raise ValueError('The original stage0 summary changed')
    state = json.loads(prior.read_text())
    if state.get('status') != 'actual_stage0_geometry_ready':
        raise ValueError('Stage0 did not meet its original continuous allocations')
    if out.exists() or out.parent != prior.parent.parent:
        raise ValueError('Use a fresh sibling continuation directory')
    original = Path(record['geometry_entry']['path'])
    if ref(original) != record['geometry_entry']:
        raise ValueError('The original complete pipeline source changed')
    out.mkdir()
    (out / 'logs').mkdir()
    (out / 'steps').mkdir()
    os.environ['HELD10_GEOMETRY_DISK_ROOT'] = str(out)
    os.environ['HELD10_GEOMETRY_DISK_FLOOR'] = str(a.disk_reserve_mib*1024**2)
    guard = geometry_disk_guard.install()
    (out / 'summary.json').write_bytes(prior.read_bytes())
    (out / 'inherited-stage0-summary.json').write_bytes(prior.read_bytes())
    if ref(out / 'summary.json')['sha256'] != ref(prior)['sha256']:
        raise ValueError('The inherited progress was not copied exactly')
    argv = list(record['actual_command'][2:])
    for flag, value in (('--outdir', str(out)), ('--phase', 'all')):
        if argv.count(flag) != 1:
            raise ValueError('Ambiguous original command option: ' + flag)
        argv[argv.index(flag)+1] = value
    if '--resume' in argv:
        raise ValueError('The source command was not the first stage0 execution')
    argv.append('--resume')
    here = Path(__file__).resolve().parent
    py_guard, js_guard = here/'geometry_disk_guard.py', here/'geometry_disk_guard.mjs'
    execution = dict(source=ref(__file__), original_pipeline=ref(original),
        original_stage0_resource_record=ref(resource_path), original_stage0_summary=ref(prior),
        initial_progress_bytes_preserved=True, inherited_snapshot=ref(out/'inherited-stage0-summary.json'),
        python_guard=ref(py_guard), node_guard=ref(js_guard), guard=guard,
        original_continuation_argv=[sys.executable, str(original), *argv],
        changed_numerical_parameters=False, omitted_stages_or_modes=False,
        prior_stage0_recomputed=False, actual_child_argv_recorded_by_original_pipeline=True)
    execution_path = out/'disk-guard-execution.json'
    execution_path.write_text(json.dumps(execution, indent=2)+'\n')
    sys.path.insert(0, str(original.parent))
    spec = importlib.util.spec_from_file_location('_guarded_original_geometry_pipeline', original)
    pipeline = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = pipeline
    spec.loader.exec_module(pipeline)
    Original = pipeline.Pipeline
    class Guarded(Original):
        def __init__(self, args):
            super().__init__(args)
            self.state['disk_guard_execution'] = ref(execution_path)
        def run(self, phase, command, *args, **kwargs):
            if Path(command[1]).suffix == '.mjs':
                command = [command[0], '--import', str(js_guard), *command[1:]]
            elif Path(command[1]).suffix == '.py':
                command = [command[0], str(py_guard), '--target', *command[1:]]
            else:
                raise ValueError('Unexpected unguarded original child command')
            return super().run(phase, command, *args, **kwargs)
    pipeline.Pipeline = Guarded
    sys.argv = [str(original), *argv]
    pipeline.main()


if __name__ == '__main__':
    main()
