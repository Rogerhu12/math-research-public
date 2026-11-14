#!/usr/bin/env python3
"""Independently replay the finite M8 suffix plan and exact packet assembly.

The completed 4999-row root prefix replay and complete root primitive replay
are inputs. This script does not modify the supplier or optimize any map.
Only scalar comparison results are printed; all numerical arrays stay local.
"""
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT/'notes'
SCRIPTS = ROOT/'scripts'
PREFIX = '2026-11-09-db6f-'


def path(name):
    return NOTES/(PREFIX+name)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load_arrays(report):
    meta = json.loads(report.read_text())
    data = report.parent/meta['data_file']
    if sha(data) != meta['data_sha256']:
        raise ValueError('Data hash mismatch')
    content = data.read_bytes()
    if content[:2] == b'\x1f\x8b':
        content = gzip.decompress(content)
    with np.load(io.BytesIO(content), allow_pickle=False) as z:
        return {k: np.array(z[k], copy=True) for k in z.files}


def run(script, args, log):
    command = [sys.executable, str(SCRIPTS/script), *map(str, args)]
    with log.open('w') as stream:
        subprocess.run(command, cwd=ROOT, stdout=stream,
                       stderr=subprocess.STDOUT, check=True)
    return command


def main():
    started = time.time()
    records = []
    cases = [
        ('tail-background-tight-int2-suffix-wide', 'root-review-background-suffix-wide'),
        ('audit-tail-critical-depth2', 'root-review-background-critical-depth2'),
        ('audit-tail-critical-4568-depth3', 'root-review-background-critical-4568-depth3'),
        ('audit-tail-critical-4571-depth3', 'root-review-background-critical-4571-depth3')]
    for old, new in cases:
        author = path(old+'.json')
        settings = dict(json.loads(author.read_text())['settings'])
        settings['out_prefix'] = str(path(new))
        settings['primitive'] = str(path('root-review-background-primitive-stable-depth2.json.gz'))
        args = []
        for key, value in settings.items():
            args.extend(('--'+key.replace('_', '-'), str(value)))
        command = run('db6f-tail-background-packet.py', args, path(new+'.log'))
        replay = path(new+'.json')
        a, b = load_arrays(author), load_arrays(replay)
        identical = a.keys() == b.keys() and all(np.array_equal(a[k], b[k]) for k in a)
        if not identical:
            raise ValueError('Supplier replay differs: '+old)
        records.append({'author': str(author), 'author_sha256': sha(author),
                        'replay': str(replay), 'replay_sha256': sha(replay),
                        'all_arrays_identical': True, 'rows': len(a['span_index']),
                        'command': command})
        print(json.dumps({'replayed': new, 'all_arrays_identical': True}), flush=True)
    # The root prefix excludes the collar. The reviewed coarse collar is
    # identical to the retained fine collar after exact zero padding.
    current = path('tail-background-coarse-int2.json')
    packets = [path('root-review-background-packet-prefix.json')]
    packets += [path(new+'.json') for _, new in cases]
    assembly = []
    for index, fine in enumerate(packets):
        target = path('root-review-final-overlay-'+str(index)+'.json')
        command = run('db6f-audit-overlay-tail-packet.py', [current, fine, target],
                      target.with_suffix('.log'))
        assembly.append({'command': command, 'output': str(target),
                         'sha256': sha(target)})
        current = target
    final = path('root-review-final-reconstructed-packet.json')
    command = run('db6f-audit-tail-inherit-coarse-wr.py',
                  [current, path('tail-background-coarse-int2.json'), final,
                   '--minimum-span', '4423'], final.with_suffix('.log'))
    assembly.append({'command': command, 'output': str(final), 'sha256': sha(final)})
    author = path('audit-tail-tight-final-packet.json')
    a, b = load_arrays(author), load_arrays(final)
    identical = a.keys() == b.keys() and all(np.array_equal(a[k], b[k]) for k in a)
    if not identical:
        raise ValueError('Final exact row assembly differs')
    report = {'status': 'independent-finite-supplier-plan-and-assembly-replay-pass',
              'script_sha256': sha(__file__), 'supplier_cases': records,
              'assembly': assembly, 'final_author_sha256': sha(author),
              'final_replay_sha256': sha(final), 'all_final_arrays_identical': True,
              'final_rows': len(a['span_index']),
              'scope': 'Finite suffix settings, exact row overlays and inherited constant wr; reviewed coarse packet, root prefix and primitive are inputs.',
              'seconds': time.time()-started}
    path('root-review-final-background-replay.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'finished': True, 'final_rows': report['final_rows'],
                      'all_final_arrays_identical': True, 'seconds': report['seconds']}))


if __name__ == '__main__':
    main()
