#!/usr/bin/env python3
"""Collect actual-state parameter and complete collocation conditioning scalars."""
import argparse
import hashlib
import json
from pathlib import Path
import shlex


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('parameters', 'collocation', 'resource', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    param, full, resource = (load(getattr(args, key))
                             for key in ('parameters', 'collocation', 'resource'))
    assert param['input_checkpoint_sha256'] == full['input_checkpoint_sha256']
    assert param['scratch_transform_sha256'] == full['transform_sha256']
    assert param['physical_profile'] == full['physical_profile']
    for row in (param, full, resource):
        row['actual_command'] = shlex.join(row.pop('command'))
    result = dict(scope='Read-only original raw M20 parameter and full finite collocation Jacobian diagnostics at one reconstructed complete-map seed. No preconditioned BVP solve was performed.',
                  collector_sha256=sha(__file__),
                  parameters=param, collocation=full, resource=resource,
                  input_output_hashes={name: sha(getattr(args, name))
                                       for name in ('parameters', 'collocation', 'resource')},
                  data_policy='Source, physical parameters, named scalar matrix diagnostics and hashes only. Complete matrices, SVD vectors and transform arrays remain scratch-only.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
