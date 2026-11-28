#!/usr/bin/env python3
"""Regenerate the original accepted design and continue with complete secants.

The previously recorded q/zero-lambda/M24 recovery is unchanged.  Its original
delta-design bootstrap reaches .016, after which the existing complete-lift
secant continuation is used.  All portable solves execute through the existing
bounded-radial/released-LU wrapper.  The actual original driver still writes its
own equation, source, input, RMS, boundary and full metric provenance.  Every
subprocess substitution is recorded here; generated arrays stay outside Git.

Earlier achieved lambda values are regenerated inputs, not new conclusions.
Even a lambda-one prefix would still owe nonlinear DN and the closed-family
geometry and fixed-problem convergence requirements.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    repo, work, out = (x.resolve() for x in (args.repo, args.work, args.outdir))
    if repo == work or repo in work.parents or work not in out.parents:
        raise ValueError('Generated execution data must stay under work outside Git')
    scripts = repo / 'topics/visible-flex-held-10pct/scripts'
    original = scripts / 'resume_20261126/lowq_prefix_recovery_secant_design.py'
    portable = scripts / 'resume_m3/portable_prefix_continue.py'
    resource = Path(__file__).with_name('prefix_resource_driver.py').resolve()
    secant = scripts / 'resume_20261126/material_design_secant_continue.py'
    controller = Path(__file__).with_name('run_lifted_secant.py').resolve()
    bootstrap = scripts / 'resume_20261126/material_design_continue.py'
    bootstrap_wrapper = Path(__file__).with_name('run_bootstrap_design.py').resolve()
    metadata = out.with_name(out.name + '-execution.jsonl')
    if metadata.exists():
        raise FileExistsError(metadata)
    files = (Path(__file__).resolve(), original, portable, resource, secant,
             controller, bootstrap, bootstrap_wrapper)
    with metadata.open('x') as stream:
        stream.write(json.dumps(dict(event='execution_begin', source_hashes={
            str(p): sha(p) for p in files}, original_equations_changed=False,
            original_acceptance_gates_changed=False, previous_recovery_recomputed=True,
            old_achieved_lambda_is_new_result=False)) + '\n')
    old_popen = subprocess.Popen

    def execute(command, *positional, **keywords):
        actual = list(map(str, command))
        before = list(actual)
        if '--driver' in actual and actual[actual.index('--driver') + 1] == str(portable):
            actual[actual.index('--driver') + 1] = str(resource)
        # The original recovery launches its child controllers with python -u.
        script_index = 2 if len(actual) > 2 and actual[1] == '-u' else 1
        if len(actual) > script_index and actual[script_index] == str(secant):
            actual[script_index] = str(controller)
        if len(actual) > script_index and actual[script_index] == str(bootstrap):
            actual[script_index] = str(bootstrap_wrapper)
        with metadata.open('a') as stream:
            stream.write(json.dumps(dict(event='subprocess', requested=before,
                                         executed=actual)) + '\n')
        return old_popen(actual, *positional, **keywords)

    subprocess.Popen = execute
    spec = importlib.util.spec_from_file_location('_original_design_recovery_20261128', original)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    sys.argv = [str(original), '--repo', str(repo), '--work', str(work), '--outdir', str(out)]
    return module.main()


if __name__ == '__main__':
    sys.exit(main())
