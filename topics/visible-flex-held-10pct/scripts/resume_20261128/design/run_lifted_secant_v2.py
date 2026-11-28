#!/usr/bin/env python3
"""Execute the existing complete-lift secant controller with bounded RHS batches.

Only original portable child commands are dispatched through the existing
streamed/released-LU wrapper.  The controller, predictor, exact mode transfer,
Newton equations and all original finite acceptance gates remain intact.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import subprocess
import sys


def main(controller_name='material_design_lifted_secant_continue.py'):
    arguments = list(sys.argv[1:])
    repo = Path(arguments[arguments.index('--repo') + 1]).resolve()
    out = Path(arguments[arguments.index('--outdir') + 1]).resolve()
    scripts = repo / 'topics/visible-flex-held-10pct/scripts'
    original = scripts / 'resume_20261126' / controller_name
    portable = scripts / 'resume_m3/portable_prefix_continue.py'
    resource = Path(__file__).with_name('prefix_resource_driver_v3.py').resolve()
    trace = out.with_name(out.name + '-execution.jsonl')
    if trace.exists():
        raise FileExistsError(trace)
    with trace.open('x') as stream:
        stream.write(json.dumps(dict(event='execution_begin', controller=str(original),
            source_hashes={str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in (Path(__file__).resolve(), original, portable, resource)},
            original_equations_changed=False, original_acceptance_gates_changed=False,
            rhs_block='mode_dependent_v3', complete_lift_secant=(controller_name ==
                'material_design_lifted_secant_continue.py'))) + '\n')
    old_popen = subprocess.Popen

    def execute(command, *positional, **keywords):
        actual = list(map(str, command))
        requested = list(actual)
        if len(actual) > 1 and Path(actual[1]).resolve() == portable:
            actual[1] = str(resource)
            # v3 records its mode-dependent execution block in the actual command.
        with trace.open('a') as stream:
            stream.write(json.dumps(dict(event='subprocess', requested=requested,
                                         executed=actual)) + '\n')
        return old_popen(actual, *positional, **keywords)

    subprocess.Popen = execute
    sys.path.insert(0, str(original.parent))
    spec = importlib.util.spec_from_file_location('_original_design_controller_20261128', original)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.argv = [str(original), *arguments]
    return module.main()


if __name__ == '__main__':
    sys.exit(main())
