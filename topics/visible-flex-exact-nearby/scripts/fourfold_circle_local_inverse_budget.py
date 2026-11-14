#!/usr/bin/env python3
"""Directed finite-H local inverse and Hardy/Wiener conversion budgets.

Only exact dyadic polynomials are inputs. No actual return-map error is
supplied or asserted by this finite calculation.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from flint import arb, ctx


def exact(value):
    value=Fraction(value)
    return arb(value.numerator)/value.denominator


def record(value):
    def dyadic(x):
        a,b=x.man_exp()
        return str(Fraction(int(a))*Fraction(2)**int(b))
    return dict(enclosure=str(value),lower_exact=dyadic(value.lower()),
                upper_exact=dyadic(value.upper()),display=float(value))


def coefficients(rows):
    out={k:(int(a),int(b)) for k,(a,b) in enumerate(rows)}
    if out[0][1]:
        raise ValueError('real constant required')
    out.update({-k:(a,-b) for k,(a,b) in list(out.items()) if k})
    return out


def multiply(a,b):
    result={}
    for i,(ar,ai) in a.items():
        for j,(br,bi) in b.items():
            old=result.get(i+j,(0,0))
            result[i+j]=(old[0]+ar*br-ai*bi,old[1]+ar*bi+ai*br)
    return result


def norm(coeff,denominator,width,derivatives=0):
    return sum(((arb(a*a+b*b).sqrt()/denominator)*abs(k)**derivatives
                *(abs(k)*width).exp() for k,(a,b) in coeff.items()),arb(0))


def run(path,width,radius):
    raw=path.read_bytes(); data=json.loads(raw)
    if data['kind']!='exact_dyadic_trigonometric_polynomials_H_and_q':
        raise ValueError('exact dyadic H and q required')
    D=2**int(data['denominator_power_of_two'])
    h=coefficients(data['h_nonnegative_integer_coefficients'])
    q=coefficients(data['q_nonnegative_integer_coefficients'])
    hp={k:(-k*b,k*a) for k,(a,b) in h.items()};hp[0]=(D,0)
    product=multiply(hp,q)
    a,b=product.get(0,(0,0));product[0]=(a-D*D,b)
    s,r=exact(width),exact(radius)
    if not s>=0 or not r>0:raise ValueError('invalid widths')
    error=norm(product,D*D,s).upper()
    if not error<1:raise ValueError('Neumann inverse gate failed')
    qnorm=norm(q,D,s).upper(); inverse=(qnorm/(1-error)).upper()
    derivative_at_zero=Fraction(sum(a for a,b in hp.values()),D)
    if derivative_at_zero<=0:raise ValueError('positive real orientation unresolved')
    B=norm(h,D,s+r,2).upper()
    kappa=(inverse*B*r).upper()
    if not kappa<=exact(Fraction(1,2)):raise ValueError('local inverse contraction gate failed')
    return dict(polynomials=str(path),polynomials_sha256=hashlib.sha256(raw).hexdigest(),
        H_degree=data['H_degree'],q_degree=data['q_degree'],strip_width=str(width),
        displacement_radius=str(radius),exact_Hprime_at_zero=str(derivative_at_zero),
        Hprime_positive_on_real_circle=True,product_error=record(error),q_norm=record(qnorm),
        inverse_Hprime_bound=record(inverse),Hsecond_on_enlarged_strip=record(B),
        contraction_bound=record(kappa),
        admissible_actual_return_error_upper_limit=record((r/(2*inverse)).lower()),
        perturbed_inverse_bound=record((inverse/(1-kappa)).upper()),
        local_inverse_finite_budget_proved=True,actual_return_error_supplied=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--polynomials',type=Path,nargs='+',required=True)
    p.add_argument('--strip',default='1/128');p.add_argument('--radius',default='1/1000')
    p.add_argument('--bits',type=int,default=192);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    results=[run(path,Fraction(args.strip),Fraction(args.radius)) for path in args.polynomials]
    factors=[]
    for gap in [Fraction(1,512),Fraction(1,256),Fraction(1,128)]:
        d=exact(gap)
        factors.append(dict(strip_gap=str(gap),
            Hardy_Parseval_factor=record((1+4/((2*d).exp()-1)).sqrt()),
            earlier_coefficientwise_factor=record((d/2).cosh()/(d/2).sinh())))
    report=dict(kind='exact_finite_H_local_inverse_and_Hardy_Wiener_budgets',complete=True,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),bits=args.bits,
        finite_inverse_budgets=results,endpoint_factors=factors,
        limitations=['No actual continuous return residual is an input to this report.',
                     'The actual preconjugated return and KAM gate remain unproved here.'])
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
