#!/usr/bin/env python3
"""Use the same fixed-g actual solver with cached engines and native diagnostics.

The owned source is produced by install_shared_tail_engines.py. This wrapper
only preserves that client's stderr handle, installs the previously proved
same-core coefficient enclosure, and records the initial iterate status.
All equations, nested remesh, actual outer loop, and audit gates are unchanged.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(add_help=False)
    for name in ('prefix-loader-dir', 'tail-source', 'tail-initial'):
        parser.add_argument('--' + name, type=Path, required=True)
    args, _ = parser.parse_known_args()
    sys.path.insert(0, str(args.prefix_loader_dir.resolve()))
    from tight_moment_interval_bounds import install, PROVENANCE
    install()
    source = Path(__file__).with_name('refine_actual_tail.py')
    program = source.read_text()
    replacements = {
        "kwargs['stderr'] = stderr": "kwargs.setdefault('stderr', stderr)",
        'scope=__doc__, command=sys.argv, solver_success=False,':
            'scope=__doc__, command=sys.argv, solver_success=False,\n'
            '        coefficient_certificate=TIGHT_CERTIFICATE,\n'
            '        execution_wrapper=SHARED_WRAPPER,\n'
            '        tail_initial_record_status=INITIAL_TAIL_STATUS,'}
    for before, after in replacements.items():
        if program.count(before) != 1:
            raise RuntimeError('Original driver anchor changed: ' + before)
        program = program.replace(before, after)
    provenance = dict(PROVENANCE)
    provenance.update(wrapper_sha256=digest(__file__),
                      base_driver_sha256=digest(source))
    initial = args.tail_initial.read_bytes()
    initial = json.loads(gzip.decompress(initial)
                         if str(args.tail_initial).endswith('.gz') else initial)
    response = initial.get('response', {})
    status = dict(converged=response.get('converged', False),
                  failed=response.get('failed'),
                  last_iteration=response.get('lastIteration'),
                  residual=response.get('residual'),
                  scope='Initial iteration data only; acceptance requires the new complete nonlinear tail and all original audits.')
    wrapper = dict(scope=__doc__, sha256=digest(__file__),
                   base_driver_sha256=digest(source),
                   source_sha256={name: digest(args.tail_source / 'scripts' / name)
                                  for name in ('950f-tail-stage-core.mjs',
                                               '950f-tail-stage-split.mjs',
                                               '950f-tail-client-v3.py')})
    exec(compile(program, str(source), 'exec'), dict(
        __name__='__main__', __file__=str(source),
        TIGHT_CERTIFICATE=provenance, SHARED_WRAPPER=wrapper,
        INITIAL_TAIL_STATUS=status))


if __name__ == '__main__':
    main()
