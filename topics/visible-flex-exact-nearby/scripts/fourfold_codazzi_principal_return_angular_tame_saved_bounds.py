#!/usr/bin/env python3
"""New exact rational majorants for RPT, without old scientific targets."""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
PINS = {
    'results/R144-supplement-full-off-constraint-principal-return-Hessian.md':
        'e77c6e41b3ff7f40085d4a65821e6858795412e9aa5e743188a74a3da9684e21',
    'results/R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md':
        'b1751a475c30ec9ca823681598b60326befc85909d462a5ff7b18acaad237c23',
    'results/R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md':
        '141f98f90c236a6588223469e61f97ff9c133533ae06e7d496e7c2420a79db87',
}


def main():
    for path, digest in PINS.items():
        assert sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
    records = []

    def less(label, left, right):
        left, right = F(left), F(right)
        assert left < right, (label, left, right)
        records.append({'label': label, 'left': str(left), 'right': str(right), 'strict': True})

    def equal(label, left, right):
        left, right = F(left), F(right)
        assert left == right, (label, left, right)
        records.append({'label': label, 'left': str(left), 'right': str(right), 'equal': True})

    T, J, S = F(478,1000), F(27,25), F(2**25)
    less('complete compact A3 low budget, unknown tail retained',
         1+10*129**3+F(1,10**6), S)
    less('complete velocity including genuine mean',
         F(6,4)*10**2+7*F(103,100)*7, 256)
    less('fixed whole H1 velocity data', (256+600)*T, 2**10)
    less('whole second-angular Wiener budget', 2*6*10*10*T, 2**10)
    less('high velocity coefficient per angular moment', 60*T, 2**7)
    less('full transported degree-one derivative A0 embedding, squared',
         J**2+24**2, 25**2)
    equal('complete velocity jet ledger', 24*2**13*10**2*8, 157286400)
    less('jet ledger below common fixed coefficient', 157286400, 2**32)
    less('first source full product coefficient', 50*2**32+2**35, 2**44)
    less('second source full product coefficient', 50*2**32+2**36, 2**44)
    less('two mixed derivative product coefficients', 2**35+2**36, 2**44)
    less('transport K0 low realization', J, 2)
    less('transport K1 full H1 realization, squared', 2*J**4, 4**2)
    # The all-order induction comparison is symbolic. For a >= 1,
    # k >= 0 and b >= 0, the recurrence uses 4(1+ak+4b),
    # which exceeds 1+(1+a)k+b since 3a-1 >= 2.
    equal('transport recurrence constant surplus', 4-1, 3)
    less('transport recurrence coefficient lower margin', 0, 3*1-1)
    equal('transport recurrence high coefficient surplus', 4*4-1, 15)

    # Evaluate the first new angular transport order only; no old
    # flow, coefficient norm or phase target is called.
    K = [F(4),F(4)]
    K.append(F(2**4)*J**3*(1+2**12*K[1]+2**14))
    less('first new transport order is finite positive', 0, K[2])
    less('first new transport order convenient dyadic ceiling', K[2], 2**21)
    result = {
        'schema': 'visible-flex-exact-nearby/RPT-saved-rational-majorants/v1',
        'new_comparisons': len(records), 'all_passed': True,
        'old_scientific_targets_executed': 0,
        'old_carriers_or_integrals_restored': 0,
        'pins': PINS, 'records': records,
        'scope': 'Complete all-angular actual two-ray return derivatives, true parameter and means; no full regular inverse or final embedding.'
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

