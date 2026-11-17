#!/usr/bin/env python3
"""Run the unchanged observed fixed-g solver with the tighter exact Gram enclosure.

Taylor degree changes from 100 to 180 only for the sufficient coefficient
certificate. The exact Gram inverse, its evaluated float coefficients, the
physical core, all solver/domain gates, and the fixed metric are unchanged.
"""
import argparse
import hashlib
import json
import runpy
import sys
from pathlib import Path

p=argparse.ArgumentParser(add_help=False)
p.add_argument('--runtime',type=Path,required=True)
a,_=p.parse_known_args()
sys.path.insert(0,str(a.runtime.resolve()))
from tight_moment_interval_bounds import install,PROVENANCE
install()
base=Path(__file__).with_name('run_observed_fixed.py')
sha=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
print(json.dumps(dict(event='tight_observed_fixed_definition',
    scope=__doc__,certificate=PROVENANCE,command=sys.argv,
    source_sha256={str(path.resolve()):sha(path)for path in
      [Path(__file__),base,a.runtime/'tight_moment_interval_bounds.py']})),flush=True)
runpy.run_path(str(base),run_name='__main__')
