#!/usr/bin/env python3
"""Extract the exact retained physical-angle height trace from a saved prefix.

No material-angle Fourier re-expansion occurs.  This is a finite numerical
interface, with the original state and saved velocity as its explicit input.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_profile import Profile


def main(a):
    raw=a.input.read_bytes();d=json.loads(gzip.decompress(raw))
    if not d.get('success'):raise ValueError('Need an accepted prefix')
    M=d['M'];s=float(d['mesh'][-1]);y=np.array(d['states'][-1]);ys=np.array(d['rhs'][-1])
    geometry=d.get('fixed_scalar_profile',d.get('inherited_profile'))['geometry']
    origin=float(d.get('analytic_extension_origin',d.get('extension_scalar',{}).get('start',s)))
    r,ap,app=Profile(geometry,origin)(s)
    if not 0<ap<1:raise ValueError('This trace convention requires 0<a_prime<1')
    w=np.sqrt(1-ap*ap)/ap;wr=-app/(ap**3*np.sqrt(1-ap*ap))
    freq=2*np.arange(1,M+1)
    report=dict(input_sha256=hashlib.sha256(raw).hexdigest(),s=s,M=M,r=float(r),
                a_prime=float(ap),a_second=float(app),w=float(w),w_r=float(wr),rho_mean=1.,
                rho_cos_coefficients=((1-freq*freq)*np.array(d['core']['coefficients'])).tolist(),
                Ptilde_sin_coefficients=(-freq*y[2*M+2:]/(r*w)).tolist(),
                K_cos_coefficients=(ys[2*M+2:]/(ap*w)).tolist(),
                K_mean=float(ys[2*M+1]/(ap*w)-1),
                height_cos_coefficients=y[2*M+2:].tolist(),height_mean=float(y[2*M+1]))
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(input_sha256=report['input_sha256'],M=M,s=s,r=float(r),w=float(w),w_r=float(wr),
                         output_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest(),
                         source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    main(p.parse_args())
