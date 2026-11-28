#!/usr/bin/env python3
"""Independent original prefix driver with explicit exact prior-tail reuse.

The existing v2 radial batching/Fourier table cache runs unchanged. Only the
loaded tail client class gets the strict complete-request memoizer. Its own
sidecar binds the prior accepted packet and distinguishes reuse from new
native requests; differing requests still use the original client path.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

OWN = Path(__file__).resolve().parent
SCRIPTS = OWN.parents[1]
sys.path.insert(0, str(OWN))
sys.path.insert(0, str(OWN.parent/'design'))
import prefix_resource_driver_v2 as resource_driver
import verified_tail_response_memo as memo


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--memo-tail-summary', type=Path, required=True)
    options, forwarded = parser.parse_known_args()
    actual_command = list(sys.argv)
    manifest = os.environ.get('VISIBLE_FLEX_NATIVE_MANIFEST')
    if not manifest:
        raise ValueError('The actual original native manifest is required')
    records = []
    original_loader = resource_driver.previous.load_module
    def loader(name, path):
        loaded = original_loader(name, path)
        if Path(path).name == 'portable_prefix_continue.py':
            prior = loaded.module
            def source_module(source_name, source_path):
                module = prior(source_name, source_path)
                if Path(source_path).name == 'db6f-prefix-coupled.py':
                    memo.install(module.client, source_summary=options.memo_tail_summary,
                        current_manifest=manifest, repo=SCRIPTS.parents[2], records=records)
                return module
            loaded.module = source_module
        return loaded
    resource_driver.previous.load_module = loader
    delegated = [str(Path(resource_driver.__file__).resolve()), *forwarded]
    sys.argv = delegated
    try:
        resource_driver.main()
    finally:
        if '--outdir' in forwarded:
            out = Path(forwarded[forwarded.index('--outdir')+1])
            if out.is_dir():
                files = [Path(__file__).resolve(), Path(memo.__file__).resolve(),
                         Path(resource_driver.__file__).resolve()]
                report = dict(scope=__doc__, actual_command=actual_command,
                    delegated_resource_command=delegated,
                    source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                    complete_request_memoization_records=records, original_equations_changed=False,
                    original_acceptance_gates_changed=False, prior_response_reuse_explicit=True)
                (out/'tail-memo-wrapper.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__ == '__main__':
    main()
