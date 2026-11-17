#!/usr/bin/env python3
"""Run the fixed-g actual-tail refinement with the tighter same-core certificate."""
import argparse
import hashlib
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--prefix-loader-dir', type=Path, required=True)
    args, _ = parser.parse_known_args()
    sys.path.insert(0, str(args.prefix_loader_dir.resolve()))
    from tight_moment_interval_bounds import install, PROVENANCE
    install()
    source = Path(__file__).with_name('refine_actual_tail.py')
    program = source.read_text()
    needle = 'scope=__doc__, command=sys.argv, solver_success=False,'
    if program.count(needle) != 1:
        raise RuntimeError('Actual refinement provenance anchor changed')
    program = program.replace(
        needle, needle + '\n        coefficient_certificate=TIGHT_CERTIFICATE,')
    provenance = dict(PROVENANCE)
    provenance.update(
        wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        base_driver_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    exec(compile(program, str(source), 'exec'), dict(
        __name__='__main__', __file__=str(source),
        TIGHT_CERTIFICATE=provenance))


if __name__ == '__main__':
    main()
