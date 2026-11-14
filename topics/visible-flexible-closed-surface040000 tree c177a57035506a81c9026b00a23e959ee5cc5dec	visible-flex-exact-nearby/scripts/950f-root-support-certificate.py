#!/usr/bin/env python3
"""Exact rational support-curve certificates for a stored macro core.

The binary floating coefficients are treated as the exact defining rationals.
This certifies that planar core, not the current truncated prefix inlet, a
complete closed surface, or a sampled radius envelope.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def pack(q):
    return {"numerator":str(q.numerator),"denominator":str(q.denominator),
            "decimal_display":float(q)}


def certify(coefficients, ell):
    c=[Q.from_float(float(x)) for x in coefficients]
    assert c and c[0]>0
    h_lower=1-sum(abs(x) for x in c)
    rho_lower=1-sum(((3*j)**2-1)*abs(x) for j,x in enumerate(c,1))
    rho_upper=1+sum(((3*j)**2-1)*abs(x) for j,x in enumerate(c,1))
    monotone_margin=c[0]-sum(j*j*abs(x) for j,x in enumerate(c,1) if j>=2)
    assert min(h_lower,rho_lower,monotone_margin)>0
    rmax=1+sum(c)
    rmin=1+sum((-1)**j*x for j,x in enumerate(c,1))
    gap=rmax-rmin
    held=min(gap,ell)
    assert gap>0
    return {
        "coefficient_convention":"h(phi)=1+sum c_j cos(3j phi); each saved float is an exact binary rational",
        "coefficients_exact":[str(x) for x in c],
        "support_lower":pack(h_lower),"curvature_radius_lower":pack(rho_lower),
        "curvature_radius_upper":pack(rho_upper),"curvature_absolute_upper":pack(1/rho_lower),
        "monotonicity_margin":pack(monotone_margin),"exact_maximum_radius":pack(rmax),
        "exact_minimum_radius":pack(rmin),"phase_pi_over_3_support_gap":pack(gap),
        "central_half_length":pack(ell),"conditional_held_lower":pack(held),
        "maximum_full_diameter_for_5percent":pack(20*held),
        "conditional_held_ratio_if_full_D_le_31_over_10":pack(held/Q(31,10)),
        "proof_scope":"Exact core geometry only. A complete phase family with all noncentral points at |z|>=ell and an independent global diameter bound is still required."
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--summary',type=Path,required=True)
    parser.add_argument('--ell',default='4/25')
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    data=json.loads(args.summary.read_text())
    core=data.get('summary',data).get('core')
    result=certify(core['coefficients'],Q(args.ell))
    result['source']={'path':str(args.summary),'sha256':hashlib.sha256(args.summary.read_bytes()).hexdigest()}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k]['decimal_display'] for k in
        ('curvature_radius_lower','curvature_absolute_upper','phase_pi_over_3_support_gap',
         'maximum_full_diameter_for_5percent','conditional_held_ratio_if_full_D_le_31_over_10')}))
