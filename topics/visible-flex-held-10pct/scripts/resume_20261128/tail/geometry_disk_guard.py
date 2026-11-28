#!/usr/bin/env python3
"""Wait before each geometry write if its real bytes would consume the reserve.

The original numerical producer and serialized bytes are unchanged. Waiting
retains the already computed stage in memory and resumes that same write.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import shutil
import sys
import time


def install(root=None, floor=None):
    root = Path(root or os.environ['HELD10_GEOMETRY_DISK_ROOT']).resolve()
    floor = int(floor if floor is not None else os.environ['HELD10_GEOMETRY_DISK_FLOOR'])
    if floor < 16*1024**2 or not root.is_dir():
        raise ValueError('Require an existing output root and a meaningful disk reserve')
    original_text, original_bytes = Path.write_text, Path.write_bytes
    source = dict(path=str(Path(__file__).resolve()),
                  sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    status = root / ('disk-guard-python-' + str(os.getpid()) + '.json')
    def note(event, path, needed, free):
        value = dict(event=event, source=source, pid=os.getpid(), utc_unix_time=time.time(),
                     pending_path=str(path), pending_bytes=needed, free_bytes=free,
                     reserve_bytes=floor, geometry_bytes_changed=False)
        original_text(status, json.dumps(value, indent=2)+'\n')
        if event != 'disk_write_gate_resumed':
            print(json.dumps(value), file=sys.stderr, flush=True)
    def before(path, needed):
        path = Path(path).resolve()
        if not path.is_relative_to(root):
            return
        waiting = False
        last = 0.
        while True:
            free = shutil.disk_usage(root).free
            if free >= floor + needed:
                if waiting:
                    note('disk_write_gate_resumed', path, needed, free)
                return
            now = time.monotonic()
            if now-last >= 30 or not waiting:
                note('disk_write_gate_waiting', path, needed, free)
                last = now
            waiting = True
            time.sleep(5)
    def write_text(path, data, *args, **kwargs):
        encoding = kwargs.get('encoding') or (args[0] if args else None) or 'utf-8'
        before(path, len(data.encode(encoding)))
        return original_text(path, data, *args, **kwargs)
    def write_bytes(path, data):
        before(path, memoryview(data).nbytes)
        return original_bytes(path, data)
    Path.write_text, Path.write_bytes = write_text, write_bytes
    return dict(source=source, output_root=str(root), reserve_bytes=floor,
                guard='free >= serialized new write bytes + reserve before every Path write',
                old_file_replacement_space_conservatively_counted_again=True,
                mathematical_producer_and_output_bytes_changed=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True)
    args, remainder = parser.parse_known_args()
    install()
    sys.path.insert(0, str(args.target.resolve().parent))
    sys.argv = [str(args.target.resolve()), *remainder]
    runpy.run_path(str(args.target.resolve()), run_name='__main__')
