#!/usr/bin/env python3
"""Unconditionally certify h(H11)=1 using PARI bnfcertify(...,1).

The flag certifies that the true class group is a quotient of the computed
group.  Since the computed group is trivial, this proves the asserted class
number.  It does not claim a full certification of the fundamental units.
"""
import argparse
import json
from pathlib import Path

from cypari2 import Pari


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate')
    parser.add_argument('--debug', type=int, default=0)
    args = parser.parse_args()
    C = json.loads(Path(args.certificate).read_text())
    f = list(map(int, C['small_field_arithmetic']['reduced_polynomial_coefficients_ascending']))
    P = Pari()
    P.allocatemem(256*1024*1024)
    P.default('debug', args.debug)
    polynomial = P.Polrev(f, 'y')
    nf = P.nfinit(polynomial)
    assert int(nf.disc()) == -86**10
    assert [int(x) for x in nf.nf_get_sign()] == [1, 5]
    bnf = P.bnfinit(nf, 1)
    assert int(bnf.bnf_get_no()) == 1
    result = int(P.bnfcertify(bnf, 1))
    assert result == 1
    print(json.dumps({
        'status': 'PASS', 'PARI_version': str(P.version()),
        'polynomial_coefficients_ascending': f,
        'discriminant': str(nf.disc()), 'signature': [1, 5],
        'computed_class_number': 1, 'bnfcertify_flag': 1,
        'bnfcertify_return_value': result,
        'unconditional_class_number': 1,
        'complete_fundamental_units_certified': False,
        'actual_norm_preimage_computed': False, 'actual_L_computed': False,
    }), flush=True)


if __name__ == '__main__':
    main()
