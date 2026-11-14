#!/usr/bin/env python3
"""Independent exact rank check: triple products plus 720-term Leibniz sum.

Does not import the author's checker or use Gaussian elimination.
Only scalar receipts are printed; no matrix or solver arrays are printed.
"""
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path


def sign_permutation(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i + 1, len(p))) % 2 else 1


def exterior_cross(a, b):
    out = [F(0), F(0), F(0)]
    for p in itertools.permutations(range(3)):
        out[p[0]] += sign_permutation(p) * a[p[1]] * b[p[2]]
    return out


def inner(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def seed_column(c, s):
    epsilon = F(1, 10)
    position = [c, s, epsilon*(c*c-s*s)]
    velocity = [-s, c, -4*epsilon*c*s]
    acceleration = [-c, -s, -4*epsilon*(c*c-s*s)]
    exterior = exterior_cross(velocity, acceleration)
    projected_acceleration = exterior_cross(exterior, velocity)
    speed_squared = inner(velocity, velocity)
    w = [x+speed_squared*y for x, y in zip(projected_acceleration, exterior)]
    assert inner(projected_acceleration, velocity) == 0
    assert inner(projected_acceleration, [c, s, F(0)]) == -speed_squared
    assert inner(w, velocity) == 0 and inner(w, w) > 0
    return w + exterior_cross(position, w)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--report', type=Path, required=True)
    args = ap.parse_args()
    if args.report.exists():
        raise RuntimeError('Refusing to overwrite previous independent receipt')
    points = [(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),
              (F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-3,5),F(4,5))]
    columns = [seed_column(c,s) for c,s in points]
    denominators = [math.lcm(*(entry.denominator for entry in col)) for col in columns]
    integer_columns = [[int(entry*den) for entry in col]
                       for col,den in zip(columns,denominators)]
    positive = 0
    negative = 0
    nonzero = 0
    terms = 0
    for p in itertools.permutations(range(6)):
        term = sign_permutation(p)*math.prod(integer_columns[p[i]][i] for i in range(6))
        terms += 1
        nonzero += (term != 0)
        if term > 0:
            positive += term
        else:
            negative -= term
    integer_det = positive-negative
    det = F(integer_det, math.prod(denominators))
    expected = F(15838112388562926448768487424,9876209658570587635040283203125)
    assert terms == 720 and det == expected and det > 0
    report = {
        'status':'PASS_INDEPENDENT_EXACT_LEIBNIZ_RANK',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'column_construction':'D=(gamma_v cross gamma_vv) cross gamma_v; W=D+speed_squared*(gamma_v cross gamma_vv)',
        'determinant_method':'positive column denominator clearing; complete 720-term integer Leibniz sum',
        'permutation_terms':terms,'nonzero_terms':nonzero,
        'positive_sum':str(positive),'negative_absolute_sum':str(negative),
        'integer_determinant':str(integer_det),
        'denominator_product':str(math.prod(denominators)),
        'determinant':str(det),'rank':6,
        'pde_runs':0,'ode_runs':0,'optimization_runs':0,
        'scope':'Exact finite endpoint derivative only; no nonlinear family or closed surface execution.'
    }
    args.report.write_text(json.dumps(report,indent=2)+chr(10))
    print(report['status'])
    print('permutation_terms='+str(terms))
    print('rank=6')
    print('report_bytes='+str(args.report.stat().st_size))
    print('report_sha256='+hashlib.sha256(args.report.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
