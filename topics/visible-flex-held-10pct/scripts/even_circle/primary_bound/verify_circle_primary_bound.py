"""Exact Fraction certificate for the R20 circle/primary lower bound."""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def fraction_text(x):return str(x.numerator)+'/'+str(x.denominator)


def decimal_text(x):
    with localcontext() as ctx:
        ctx.prec=40
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path)
    args=p.parse_args()
    # For 0<x<1 the successive cosine Taylor term magnitudes strictly
    # decrease. The even and following odd partial sums enclose cos(x).
    a=F(29,200);x=4*a;assert 0<x<1
    upper=sum(F((-1)**k)*x**(2*k)/math.factorial(2*k)for k in range(9))
    lower=upper-x**18/math.factorial(18)
    assert 0<lower<upper<1
    coefficient_lower=15*(1-upper)/(1+upper)
    coefficient_upper=15*(1-lower)/(1+lower)
    decimal_lower=F(13357528678,10**10)
    decimal_upper=F(13357528679,10**10)
    assert decimal_lower<coefficient_lower<coefficient_upper<decimal_upper
    rows=[]
    for q in (F(1,200),F(1,25),F(3,50)):
        rows.append(dict(q=fraction_text(q),nonprimary_lower_fraction=fraction_text(q*decimal_lower),
            nonprimary_lower_decimal=decimal_text(q*decimal_lower),
            nonprimary_upper_decimal_for_minimax_constant=decimal_text(q*decimal_upper),
            necessary_quadratic_coefficient_lower=decimal_text(decimal_lower/q)))
    report=dict(scope='Exact rational cosine bounds and cross-multiplied positive rational inequalities. No numerical BVP is used.',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        halfwidth=fraction_text(a),cosine_argument=fraction_text(x),
        cosine_lower=fraction_text(lower),cosine_upper=fraction_text(upper),
        coefficient_lower=fraction_text(coefficient_lower),coefficient_upper=fraction_text(coefficient_upper),
        asserted_decimal_lower=fraction_text(decimal_lower),asserted_decimal_upper=fraction_text(decimal_upper),
        coefficient_lower_decimal=decimal_text(coefficient_lower),coefficient_upper_decimal=decimal_text(coefficient_upper),
        q_cases=rows,all_assertions_passed=True)
    if args.out:args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
