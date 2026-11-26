#!/usr/bin/env python3
"""Read an actual completed research command log without rerunning its solver."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--log', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--check', type=Path, action='append', default=[])
    args = parser.parse_args()
    work = args.work.resolve()
    for path in [args.log, args.outdir, *args.check]:
        if work not in path.resolve().parents:
            raise ValueError('Only the declared runner scratch directory is inspected')
    args.outdir.mkdir(parents=True, exist_ok=False)
    data = args.log.read_bytes()
    tail = data[-12000:].decode('utf-8', 'replace')
    result = dict(status='actual_command_log_read', result=dict(
        solver_invoked=False, log=str(args.log.resolve()),
        log_sha256=hashlib.sha256(data).hexdigest(), log_bytes=len(data),
        log_tail=[tail[i:i+1600] for i in range(0, len(tail), 1600)],
        checked_paths=[dict(path=str(path.resolve()), exists=path.exists(),
            is_file=path.is_file(), is_directory=path.is_dir()) for path in args.check]))
    (args.outdir/'summary.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], log_bytes=len(data))), flush=True)


if __name__ == '__main__':
    main()
