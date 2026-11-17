#!/usr/bin/env python3
"""Refine the same moving-frame fast-Schur finite boundary family.

Lift the accepted warm and earlier reference by zero added coefficients;
rebuild their full finite RHS/connection at M, and select M-3 Schur rows.
The spectral threshold must select complete real blocks of that dimension.
This is a finite family, not a claim of convergent tail DN conditions.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

BASE=Path(__file__).with_name('2026-11-17-parallel-geometry-schur-bvp.py')
spec=importlib.util.spec_from_file_location('frozen_schur_bvp',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)


def main(args):
    base.main(args)
    result=json.loads(gzip.decompress(args.out.read_bytes()))
    result['moving_frame_schur_refinement']=dict(
        scope=__doc__,modes=args.modes,angles=args.angles,
        wrapper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        base_driver_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest())
    result['moving_frame_schur_boundary']['scope']=__doc__
    args.out.write_bytes(gzip.compress((json.dumps(result)+'\n').encode(),mtime=0))
    print(json.dumps(dict(event='schur_refinement_bound',success=result['success'],
        M=result['M'],N=result['N'],output=str(args.out),
        output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--boundary-input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--modes',type=int,default=128)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--max-nodes',type=int,default=2000)
    p.add_argument('--tol',type=float,default=1e-8)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    p.set_defaults(duration=0.,step=.00025,fixed_modes=3,core_first=None,curvature=None,ramp=.02)
    main(p.parse_args())
