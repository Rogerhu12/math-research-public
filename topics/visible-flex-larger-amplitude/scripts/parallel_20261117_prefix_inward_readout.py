#!/usr/bin/env python3
"""The actual C2 quintic reader, bound to a stored inward scalar metric."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import parallel_20261117_prefix_readout as reader
from parallel_20261117_inward_profile import InwardProfile


def main(args):
    data=json.loads(gzip.decompress(args.input.read_bytes()))
    spec=data.get('inward_scalar_profile')
    if not spec:raise ValueError('Missing the explicit new inward metric')
    source=Path(__file__).with_name('parallel_20261117_inward_profile.py')
    source_sha=hashlib.sha256(source.read_bytes()).hexdigest()
    if data.get('inward_profile_sha256')!=source_sha:
        raise ValueError('The inward scalar source differs from the solved field')
    reader.Profile=lambda geometry,origin: InwardProfile(geometry,origin,spec['cut'],
        spec['curvature'],spec['ramp_in'],spec['ramp_out'],spec['quadrature'])
    reader.main(args)
    report=json.loads(args.out.read_bytes())
    report['inward_scalar_profile']=spec
    report['inward_profile_sha256']=source_sha
    report['inward_reader_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='inward_metric_readout_bound',
        report_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int);p.add_argument('--radial-subdivisions',type=int,default=4)
    main(p.parse_args())
