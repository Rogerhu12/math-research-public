#!/usr/bin/env python3
"""Compact the completed halfwidth probe and identify each new raw moment basis.

Only the explicit 80-digit moment definitions are reevaluated.  The recorded
RMS/domain runs are not repeated, and no BVP or nonlinear tail is called.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_id(value):
    x=np.asarray(value,dtype='<f8',order='C')
    return dict(shape=list(x.shape),encoding='little-endian binary64, C order',
                sha256=hashlib.sha256(x.tobytes()).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();data=json.loads(a.input.read_text())
    for path,digest in data['source_sha256'].items():
        if sha(path)!=digest:raise ValueError('A completed probe source changed: '+path)
    sys.path.insert(0,str(Path(__file__).with_name('round_raw_lib')))
    from complementary_moment_basis import _constants
    rows=[];controls=None
    for old in data['rows']:
        row={k:v for k,v in old.items() if k!='physical_controls'}
        chosen=old['core_settings']
        const=_constants(3,data['modes'],chosen['halfwidth'],chosen['control_transition'],
                         1,chosen['coefficient_precision'],True)
        row['basis_identity']=dict(
            definition='B_j(phi)=W_a(phi)[cos(3*j*phi)-C_0j-C_1j*cos(3*phi)], j=2..M; '
                'C solves the weighted {1,cos3phi} 2x2 moment system at this a.',
            normalized_inner_product='(2*pi)^(-1) integral_0^(2*pi)',
            low_weighted_gram=const['gram'][:2,:2].tolist(),
            raw_constraints=array_id(const['raw_constraints']),
            supported_trigonometric_coefficients=array_id(const['canonical_trig_coefficients']),
            full_weighted_gram=array_id(const['gram']),
            high_precision_low_moment_residual=const['high_precision_moment_residual'],
            finite_basis_scope='The source defines exact moment inverses; these matrix identities '
                'record its 80-digit-to-binary64 evaluation, not a new interval certificate.')
        if 'physical_controls' in old:
            if controls is None:controls=old['physical_controls']
            elif controls!=old['physical_controls']:raise ValueError('Actual initial controls changed across a')
        rows.append(row)
    report={k:v for k,v in data.items() if k not in ('rows','source_sha256')}
    report.update(
        status='finite initial guesses only; no new BVP or tail solution',
        probe_execution=dict(session=12463,observed_returncode=0),
        full_probe=dict(path=str(a.input.resolve()),sha256=sha(a.input)),
        source_sha256=data['source_sha256'],
        collector=dict(path=str(Path(__file__).resolve()),sha256=sha(__file__),
                       command=sys.argv,scope=__doc__),
        shared_actual_physical_controls=controls,rows=rows,
        search_scope='A targeted rg of the topic notes/log found previous m3 halfwidth fixed '
            'at .21 and control-width screens, but no equivalent five-halfwidth lambda-one '
            'C2-initializer domain/RMS comparison. Historical n4 designs are different.')
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),sha256=sha(a.out),rows=len(rows))),flush=True)


if __name__=='__main__':main()
