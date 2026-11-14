#!/usr/bin/env python3
"""Run the frozen full BVP with separately identified lossless QR storage."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import gzip
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

P = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, P/filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    hashes = {name: hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
              ('geometry_20261114_compressed_qr_driver.py',
               'geometry_20261114_separated_qr_compressed.py',
               'geometry_20261114_separated_qr_bvp.py',
               'geometry_20261114_projected_core_bvp.py')}
    driver = load('compressed_projected_driver', 'geometry_20261114_projected_core_bvp.py')
    previous = driver.module

    def redirected(name, filename):
        if filename == 'geometry_20261114_separated_qr_bvp.py':
            return load(name, 'geometry_20261114_separated_qr_compressed.py')
        return previous(name, filename)

    driver.module = redirected
    print(json.dumps(dict(event='lossless_qr_driver', source_hashes=hashes,
                          storage_only_change=True)), flush=True)
    driver.main()
    output = Path(sys.argv[sys.argv.index('--out')+1])
    if output.exists():
        data = json.loads(gzip.decompress(output.read_bytes()))
        data['lossless_qr_storage_source_hashes'] = hashes
        data['base_linear_backend_source_sha256'] = data.get('linear_backend_source_sha256')
        data['linear_backend_source_sha256'] = hashes['geometry_20261114_separated_qr_compressed.py']
        data['storage_only_change'] = True
        output.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(), mtime=0))


if __name__ == '__main__':
    main()
