#!/usr/bin/env python3
"""First new exact scalar majorants for WT; no old scientific target."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'results/R144-supplement-complete-passive-world-height-Hessian-with-independent-ports.md':
        '8c7aad2c61881c91b2c7f8820cefb169eceb710dc9c68f8d1bb0365c99630330',
    'results/R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md':
        '141f98f90c236a6588223469e61f97ff9c133533ae06e7d496e7c2420a79db87',
}


def main():
    for path, digest in PINS.items():
        assert sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    A, R = F(2**20), F(25, 8)
    K, Lambda = F(2**30)*A, F(2**32)
    records = []

    def less(label, left, right):
        left, right = F(left), F(right)
        assert left < right, (label, left, right)
        records.append({'label': label, 'left': str(left), 'right': str(right), 'strict': True})

    def equal(label, left, right):
        left, right = F(left), F(right)
        assert left == right, (label, left, right)
        records.append({'label': label, 'left': str(left), 'right': str(right), 'equal': True})

    less('pair seven gives component sum below ten: squared', 2*7**2, 10**2)
    less('whole radial length below four', R, 4)
    less('true b beta K second derivative ledger', F(1,2)*6 + 2*1*4 + 2*8, 32)
    equal('complete coefficient jet integer count', 12*50*2*32*10**3*4, 153600000)
    less('whole coefficient jet count below fixed K/A', 153600000, 2**30)
    equal('fixed coefficient scale', K, 2**50)
    less('all relative rigid subpropagators', 2 + 630*R*A, Lambda)
    less('whole labelled jet bookkeeping per slot', 4*3*11*3*2*3, 2**16)
    equal('ordered jet scale', 2**16*K*Lambda, 2**98)
    # Symbolic linear exponent comparisons for every integer n >= 0.
    # D_n plus terminal, derivative and pair factors is bounded by
    # 2^(101*n+400) (n+2)!, which is below R_n.
    less('raw order exponent slope', 101, 128)
    less('raw order exponent intercept', 400, 128*8)
    less('inverse-angle denominator per order', 100**2, 2**14)
    less('inverse-angle low numerator per order', 11, 2**4)
    less('inverse-angle complete exponent slope', 14+4+1+2, 40)
    less('inverse-angle complete exponent intercept', 35+20+6+24, 40*6)
    # R_(n+2)*T_n has exponent 168*n+1520 and factorial
    # factors (n+10)!^4*(n+6)!^4.  The finite coloured-product
    # factors are bounded by 2^(8*n+64), leaving the stated gap.
    less('final height exponent slope with coloured products', 128+40+8, 200)
    less('final height exponent intercept with coloured products', 128*10+40*6+64, 200*12)
    less('raw factorial shift below final shift', 10, 12)
    less('composition factorial shift below final shift', 6, 12)
    equal('combined factorial multiplicity', 4+4, 8)
    print(json.dumps({
        'schema': 'visible-flex-exact-nearby/WT-saved-rational-majorants/v1',
        'new_comparisons': len(records), 'all_passed': True,
        'old_scientific_targets_executed': 0,
        'new_scientific_arrays_or_integrals': 0,
        'pins': PINS, 'records': records,
        'scope': 'All-order actual passive world map and fixed-physical-angle height tame derivatives; no signed carrier, inverse or final embedding.'
    }, indent=2))


if __name__ == '__main__':
    main()
