#!/usr/bin/env python3
"""Actual local circle design with full material restarts and observed Newton.

Only initialization, exact coefficient enclosure degree, the sufficient
C2 interpolation positivity certificate, and diagnostic logging differ from the base
runner. Core values, equations, physical gates and solver tests are unchanged.
"""
import hashlib,json,types
from pathlib import Path
from tight_moment_interval_bounds import install,PROVENANCE as INTERVAL_PROVENANCE
install()
import large_radius_local_core
from second_order_large_radius_core import make_core_class,PROVENANCE as GUARD_PROVENANCE
large_radius_local_core.make_core_class=make_core_class
from run_large_radius_material_chain import OLD,NEW
source=Path(__file__).with_name('run_large_radius_circle.py')
text=source.read_text();transforms=[(OLD,NEW),
 ('install();rows=[];sol=None;start=time.monotonic()',
  "install();from trace_domain_newton import install as trace_install\n    trace_install(args.out.with_name(args.out.name+'-newton.jsonl'));rows=[];sol=None;start=time.monotonic()"),
 ('source_transforms=TRANSFORMS,rows=rows',
  'source_transforms=TRANSFORMS,coefficient_certificate=INTERVAL_PROVENANCE,complete_core_guard=GUARD_PROVENANCE,driver_transforms=DRIVER_TRANSFORMS,rows=rows')]
for before,after in transforms:
    if text.count(before)!=1:raise RuntimeError('Circle driver literal transform mismatch: '+before)
    text=text.replace(before,after)
print(json.dumps(dict(event='circle_driver_definition',base_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),coefficient_certificate=INTERVAL_PROVENANCE,complete_core_guard=GUARD_PROVENANCE,driver_transforms=transforms)),flush=True)
mod=types.ModuleType('tight_material_circle_literal');mod.__file__=str(source)
mod.__dict__.update(INTERVAL_PROVENANCE=INTERVAL_PROVENANCE,GUARD_PROVENANCE=GUARD_PROVENANCE,DRIVER_TRANSFORMS=transforms)
exec(compile(text,str(source),'exec'),mod.__dict__)
mod.main()
