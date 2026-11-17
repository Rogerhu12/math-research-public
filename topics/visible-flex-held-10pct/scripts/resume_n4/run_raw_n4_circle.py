#!/usr/bin/env python3
"""Run the actual n4 prefix BVP along the raw mean/c8 compact-control path."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import types

probe = argparse.ArgumentParser(add_help=False)
probe.add_argument('--restart',type=Path,required=True)
known,_ = probe.parse_known_args()
record = json.loads(gzip.decompress(known.restart.read_bytes()))
RAW_ANCHOR_MODES = int(record.get('raw_control_anchor_modes',record['config']['modes']))
from tight_moment_interval_bounds import install,PROVENANCE as INTERVAL_PROVENANCE
install()
import complementary_moment_basis
from raw_n4_complementary import make_raw_basis,provenance
RAW_PROVENANCE = provenance(RAW_ANCHOR_MODES)
RAW_PROVENANCE['anchor_input_checkpoint_sha256'] = hashlib.sha256(known.restart.read_bytes()).hexdigest()
complementary_moment_basis.ComplementaryMomentBasis = make_raw_basis(RAW_ANCHOR_MODES)
import large_radius_local_core
from second_order_large_radius_core import make_core_class as guarded_core,PROVENANCE as GUARD_PROVENANCE


def raw_core(reference):
    Core = guarded_core(reference)
    original_summary = Core.summary
    def summary(self):
        out = original_summary(self)
        out.update(control_family='Raw C4 controls with exact mean and physical c8 zero',
                   control_homotopy='Frozen original canonical low start to raw mean/c8 projected compact endpoint; higher moments may vary',
                   control_projection_order=RAW_ANCHOR_MODES,
                   raw_control_anchor_modes=RAW_ANCHOR_MODES,
                   raw_control_path='raw-mean-c8-with-frozen-canonical-low-start-v1')
        return out
    Core.summary = summary
    return Core


large_radius_local_core.make_core_class = raw_core
from run_large_radius_material_chain import OLD,NEW
source = Path(__file__).with_name('run_large_radius_circle.py')
text = source.read_text()
transforms = [
    (OLD,NEW),
    ('install();rows=[];sol=None;start=time.monotonic()',
     "install();from trace_domain_newton import install as trace_install\n    trace_install(args.out.with_name(args.out.name+'-newton.jsonl'));rows=[];sol=None;start=time.monotonic()"),
    ("core_kind='reflection_axis_local_flatten_bimodal_core'",
     "core_kind='n4_raw_mean_c8_local_circle'"),
    ('plateau_settings=dict(settings),gauge_amplitude=args.q,parameters=sol.p.tolist(),',
     'plateau_settings=dict(settings),raw_control_anchor_modes=RAW_ANCHOR_MODES,raw_control_provenance=RAW_PROVENANCE,gauge_amplitude=args.q,parameters=sol.p.tolist(),'),
    ('source_transforms=TRANSFORMS,rows=rows',
     'source_transforms=TRANSFORMS,raw_control_definition=RAW_PROVENANCE,coefficient_certificate=INTERVAL_PROVENANCE,complete_core_guard=GUARD_PROVENANCE,driver_transforms=DRIVER_TRANSFORMS,rows=rows')]
for before,after in transforms:
    if text.count(before) != 1:
        raise RuntimeError('Raw circle driver transform mismatch: '+before)
    text = text.replace(before,after)
print(json.dumps(dict(event='raw_circle_driver_definition',raw_control_definition=RAW_PROVENANCE,
                      driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      base_driver_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                      coefficient_certificate=INTERVAL_PROVENANCE,complete_core_guard=GUARD_PROVENANCE)),flush=True)
module = types.ModuleType('raw_n4_circle_literal')
module.__file__ = str(source)
module.__dict__.update(RAW_ANCHOR_MODES=RAW_ANCHOR_MODES,RAW_PROVENANCE=RAW_PROVENANCE,
                       INTERVAL_PROVENANCE=INTERVAL_PROVENANCE,GUARD_PROVENANCE=GUARD_PROVENANCE,
                       DRIVER_TRANSFORMS=transforms)
exec(compile(text,str(source),'exec'),module.__dict__)
module.main()
