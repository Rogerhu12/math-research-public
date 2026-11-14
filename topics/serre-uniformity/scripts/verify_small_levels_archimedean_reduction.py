#!/usr/bin/env python3
"""Verify the R101 integer witnesses, independently of their search routine.

Finite orbit data are rebuilt by inverse-cusp bucketing, rather than by
multiplying the generator's chosen Cartan lifts.  Continued fractions are
not needed: each saved rational approximation is checked as an integer
witness.  python-flint Arb supplies directed transcendental enclosures.
"""
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from flint import arb, arb_mat, fmpq, ctx

LEVELS=(41,47,59,83)


def verify_level(level,bits,margin_bits):
    ctx.prec=bits
    p=level['p'];d=(p-1)//2;m=2
    assert p in LEVELS
    g,xi=level['g'],level['xi']
    assert pow(xi,d,p)==p-1
    index={}
    for k in range(d):
        z=pow(g,k,p)
        assert z not in index and (-z)%p not in index
        index[z]=index[-z%p]=k
    assert set(index)==set(range(1,p))
    assert len(level['cusps'])==d
    assert [c['s'] for c in level['cusps']]==list(range(1,d+1))

    # Independent formulas for logarithms of the specified circular units.
    logarithms={a:(2*(arb.pi()*a/p).sin()).log() for a in range(1,p)}
    E=arb_mat([[2*logarithms[pow(g,k,p)]]+
               [logarithms[(j*pow(g,k,p))%p]-logarithms[pow(g,k,p)]
                for j in range(2,d+1)] for k in range(d)])
    A=E.inv()
    identity=arb_mat([[int(i==j) for j in range(d)] for i in range(d)])
    assert (E*A-identity).contains(arb_mat(d,d))
    kappa=arb(fmpq(level['kappa_upper_numerator'],2**margin_bits))
    for i in range(d):assert sum(abs(A[i,j]) for j in range(d))<=kappa
    theta_error=kappa*m*p*2*(p+1)

    divisor=next(n for n in range(3,d+1) if d%n==0)
    omega=arb(30)**(divisor+5)*arb(divisor)**fmpq(9-4*divisor,2)*arb(p)**(6*divisor+5)*arb(p).log()**2
    S_initial=int(level['S_initial'])
    assert arb(S_initial)>=omega+10000

    # The elementary j-series majorant used for the initial q-bound.
    rr=Fraction(1,200)
    majorant=((1+240*rr*(1+4*rr+rr**2)/(1-rr)**5)**3/(1-24*rr/(1-rr)**2)-1)/rr
    assert majorant<10000
    assert arb(200).log()<arb.pi()*arb(3).sqrt()

    witness_count=0
    for c in level['cusps']:
        u,b,v,w=c['matrix']
        assert (u*w-b*v)%p==1
        assert (u*u-xi*v*v)%p==c['s']
        counts=[0]*d
        moments=[0]*d
        gammas=[{} for _ in range(d)]
        quadratic=[0,0,0]
        for x in range(p):
            for y in range(p):
                if x==0 and y==0:continue
                xx=(w*x-v*y)%p
                yy=(-b*x+u*y)%p
                k=index[(xi*xx*xx-yy*yy)%p]
                counts[k]+=1
                moments[k]+=6*x*x-6*p*x+p*p
                if x==0:gammas[k][y]=gammas[k].get(y,0)+1
                if k==0:
                    quadratic[0]+=xx*xx;quadratic[1]+=xx*yy;quadratic[2]+=yy*yy
        assert counts==[2*(p+1)]*d
        assert m*counts[0]%12==0
        assert all(t%p==0 for t in quadratic)
        vv=[Fraction(-m*z,12*p*p) for z in moments]
        assert sum(vv)==0
        assert all((p*z).denominator==1 for z in vv)
        gg=[[[a,n] for a,n in sorted(row.items())] for row in gammas]
        assert [[z.numerator,z.denominator] for z in vv]==c['v']
        assert gg==c['gamma']
        vcol=arb_mat([[arb(fmpq(z.numerator,z.denominator))] for z in vv])
        wcol=arb_mat([[m*sum(n*logarithms[a] for a,n in row)] for row in gg])
        delta=A*vcol;theta=A*wcol
        assert delta[0,0].contains(0) and theta[0,0].contains(m)
        S=S_initial
        for step in c['steps']:
            assert int(step['S_before'])==S
            i,j=step['i'],step['j']
            assert 0<i<d and 0<j<d and i!=j
            assert abs(delta[i,0])>0
            B=int(step['B'])
            assert arb(B)>=abs(delta[i,0])*S+abs(theta[i,0])+theta_error
            ratio=delta[j,0]/delta[i,0]
            offset=ratio*theta[i,0]-theta[j,0]
            n,r,nearest=map(int,(step['n'],step['r'],step['nearest_lambda']))
            assert r>0
            distance=abs(r*offset-nearest)
            assert distance<arb('0.5')
            margin=distance-B*abs(r*ratio-n)
            certified_margin=arb(fmpq(step['gap_lower_numerator'],2**margin_bits))
            assert certified_margin>0 and margin>=certified_margin
            upper=p*(r*(1+abs(ratio))*theta_error/certified_margin).log()
            assert arb(step['S_after'])>=upper
            assert step['S_after']<S
            S=step['S_after'];witness_count+=1
        assert S==c['S_final']
    assert level['S_uniform']==max(c['S_final'] for c in level['cusps'])
    print(f'p={p}: all {d} cusps and {witness_count} integer witnesses verified; bound {level["S_uniform"]}.',flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificate',type=Path,default=Path(__file__).with_name('data')/'small_levels_archimedean_reduction.json')
    parser.add_argument('--precision',type=int,default=4096)
    args=parser.parse_args()
    raw=args.certificate.read_bytes();cert=json.loads(raw)
    assert cert['version']==1 and cert['unit_exponent']==2
    assert tuple(row['p'] for row in cert['levels'])==LEVELS
    assert args.precision>=cert['precision_bits']
    for level in cert['levels']:verify_level(level,args.precision,cert['margin_bits'])
    print('SHA256',hashlib.sha256(raw).hexdigest())
    print('First reduction only: no claim about the remaining compact intervals.')

if __name__=='__main__':main()
