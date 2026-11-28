#!/usr/bin/env python3
"""Exact rational Darboux enclosure for the gap-.92 prefix and full R205 caps."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path

D = 10**17
N = 512
R = F(97,1000)
A0 = F(float.fromhex("0x1.68493d1d794f0p+0"))
B0 = F(float.fromhex("0x1.f31079949d8dep-2"))
CF = F(17,50)
L = F(23,50)
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def lo(x):
    return F(x.numerator*D//x.denominator,D)
def hi(x):
    return -lo(-x)
def trig(x):
    return (lo(sum((-1)**k*x**(2*k)/factorial(2*k) for k in range(8))),
            hi(sum((-1)**k*x**(2*k+1)/factorial(2*k+1) for k in range(7))))
def budget(amplitude, min_height, yp, zp):
    c=CF
    h=F(0)
    held=(A0-CF)**2+min_height**2
    sep=(min_height-zp)**2
    sep_i=held_i=-1
    for i in range(N):
        t=F(i+1,N)
        smooth=t**5*(126+t*(-420+t*(540+t*(-315+70*t))))
        cos_lower,sin_upper=trig(amplitude*smooth)
        h+=L/N*sin_upper
        # c at the left endpoint is a certified lower bound throughout this cell.
        d=max(0,c-yp)**2+max(0,min_height-h-zp)**2
        if d<sep:sep_i,sep=i,d
        # For all smaller amplitudes C can grow, but C(y)<=y remains valid.
        d=(A0-(CF+L*t))**2+max(0,min_height-h)**2
        if d<held:held_i,held=i,d
        c+=L/N*cos_lower
    return dict(amplitudeUpper=str(amplitude),heightLower=str(min_height),prefixVsTailSquared=str(sep),
            minimizerCell=sep_i,heldTailSquared=str(held),heldMinimizerCell=held_i,
            trueTailBottomLower=str(min_height-h),outerCutHorizontalRadiusLower=str(c),
            prefixVsTailLowerMillionths=isqrt(sep.numerator*10**12//sep.denominator),
            heldTailLowerMillionths=isqrt(held.numerator*10**12//held.denominator),
            provesNonlocalSeparation=sep>(2*R)**2,provesHeld=held>F(64,100)**2)
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--prefix-proof',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();src=json.loads(a.prefix_proof.read_text())
    if sha(a.prefix_proof)!='cdf47a7f031f879f1d80bd8b1c6eb03a674abd8effd14801e53f94e6416ead4b':
        raise ValueError("Actual R267 output required")
    b=src['exactBounds'];yp=B0+F(b['horizontalDisplacementUpper']);zp=F(13,128)+F(b['meridianLength'])
    assert yp<F('.498568') and zp<F('.181563')
    rows=[budget(A,Z,yp,zp) for A,Z in [(F(6,5),F('.44')),(F(6,5),F('.50')),(F(6,5),F('.51')),(F(6,5),F('.52')),(F('1.06'),F('.44')),(F('.875'),F('.44'))]]
    for row in rows:
        assert F(row['trueTailBottomLower'])>R and F(row['outerCutHorizontalRadiusLower'])>F('.32')+2*R
    required=rows[1]
    assert required['provesNonlocalSeparation'] and required['provesHeld']
    assert 315*F(6,5)/(128*L)<F('6.42')<F(1,1)/R
    assert F('.44')-zp>2*R
    result=dict(schema='exact-gap092-entire-R205-and-complete-R219-caps-v1',prefixProofSHA256=sha(a.prefix_proof),
        checkerSHA256=sha(__file__),cells=N,scale=D,exactPrefixYUpper=str(yp),exactPrefixZUpper=str(zp),rows=rows)
    with a.output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    for row in rows:print(row['amplitudeUpper'],row['heightLower'],row['prefixVsTailLowerMillionths'],row['heldTailLowerMillionths'])
if __name__=='__main__':main()
