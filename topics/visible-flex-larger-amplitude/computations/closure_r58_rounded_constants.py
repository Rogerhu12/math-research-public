#!/usr/bin/env python3
"""Exact integer comparisons for the displayed R58 certificate constants.

The full641 proof is in its separate Arb ledger. This tiny Fraction tool
only verifies the simpler rational bounds printed in the theorem.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path


def upper(row):
    endpoint=row['upper']
    return Fraction(int(endpoint['mantissa']))*Fraction(2)**int(endpoint['binary_exponent'])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate',type=Path,required=True)
    p.add_argument('--resource',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError('Use a fresh exact-constant ledger')
    raw=args.certificate.read_bytes()
    data=json.loads(gzip.decompress(raw))
    report=json.loads(args.resource.read_text())
    if not data['whole_head_closed'] or not all(data['gates'].values()) or report['exitcode']!=0:
        raise ValueError('The actual strict641 job must already be successful')
    T=upper(data['maximum_cell_total_radius'])
    q=upper(data['maximum_joint_Lipschitz'])
    rz=upper(data['far_normalized_radius'])
    gates=dict(total_below_4477_e_minus18=T<Fraction(4477,10**18),
        total_below_original_rho=T<Fraction(2)**-30,
        Lipschitz_below_969_over1000=q<Fraction(969,1000),
        reported_31_over32_target_was_not_met=q>Fraction(31,32) and not data['actual_target_met'],
        far_radius_below_2208_e_minus26=rz<Fraction(2208,10**26),
        relative_far_increment_below_2_minus51=2**24*rz<Fraction(2)**-51,
        actual_far_domain=(Fraction(2)**-2224+Fraction(2)**-2200*rz)<Fraction(2)**-2200)
    result=dict(status='Exact Fraction comparisons of the actual R58 dyadic upper endpoints',
        gates=gates,all_gates=all(gates.values()),
        endpoints={k:data[k] for k in ('maximum_cell_total_radius','maximum_joint_Lipschitz','far_normalized_radius')},
        true_far_conclusion='norm(z)<(1+2^-51)*2^-2224<2^-2200',
        certificate_sha256=hashlib.sha256(raw).hexdigest(),
        resource_sha256=hashlib.sha256(args.resource.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='R58 actual strong M20 real inner head only; this helper does not replace the full641 Arb proof.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(all_gates=result['all_gates'],gates=gates)),flush=True)
    if not result['all_gates']:raise SystemExit(1)


if __name__=='__main__':main()
