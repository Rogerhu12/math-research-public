#!/usr/bin/env python3
"""Propagate the unchanged geometry Path-write guard to nested Python children.

The parent supplies the original Node write guard through NODE_OPTIONS, so
stage-zero's nested Node exporter is protected too. Only execution wrapping
and resource waiting change. No mathematical source, argv value, array,
serialized scientific byte or numerical acceptance test is changed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys

import geometry_disk_guard


def wrapped(command):
    if not isinstance(command, (list, tuple)) or len(command) < 2:
        return command
    value = list(map(str, command))
    index = 2 if value[1] == '-u' else 1
    if len(value) <= index:
        return command
    target = Path(value[index])
    if (target.suffix != '.py' or not target.is_file()
            or target.resolve() == Path(__file__).resolve()
            or 'python' not in Path(value[0]).name.lower()):
        return command
    return [*value[:index], str(Path(__file__).resolve()), '--target',
            str(target.resolve()), *value[index+1:]]


def main():
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument('--target', type=Path, required=True)
    args, rest = parser.parse_known_args()
    target = args.target.resolve()
    if target == Path(__file__).resolve():
        raise ValueError('The recursive resource guard cannot execute itself')
    geometry_disk_guard.install()
    original = subprocess.Popen
    trace = Path(os.environ['HELD10_GEOMETRY_DISK_ROOT'])/(
        'recursive-python-dispatch-'+str(os.getpid())+'.jsonl')
    source = dict(path=str(Path(__file__).resolve()), sha256=hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest())

    def popen(command, *positional, **keywords):
        actual = wrapped(command)
        process = original(actual, *positional, **keywords)
        if isinstance(command, (list, tuple)):
            previous = trace.read_text() if trace.is_file() else ''
            trace.write_text(previous+json.dumps(dict(source=source, pid=os.getpid(),
                child_pid=process.pid, requested=list(map(str, command)),
                actual=list(map(str, actual)), child_returncode=None,
                scope='Observed dispatch only; no child terminal status inferred'),
                allow_nan=False)+'\n')
        return process

    subprocess.Popen = popen
    sys.path.insert(0, str(target.parent))
    sys.argv = [str(target), *rest]
    try:
        runpy.run_path(str(target), run_name='__main__')
    finally:
        subprocess.Popen = original


if __name__ == '__main__':
    main()
