#!/usr/bin/env python3
"""All-angle endpoint chord enclosure for the actual .995 cut.

Exact binary state coefficients, rational Machin pi intervals, fixed-point
outward Taylor intervals, and an analytic angular Lipschitz bound are used.
The reference radius/length box is an explicit assumption: this source does
not certify the separate meridian integral, solve a tail, or bound reach.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from math import factorial,isqrt
from pathlib import Path


S=10**24


def floor(q):return q.numerator//q.denominator
def ceil(q):return -(-q.numerator//q.denominator)
def interval(q):return (floor(q*S),ceil(q*S))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def multiply(a,b):
    p=[x*y for x in a for y in b]
    return (min(p)//S,-(-max(p)//S))
def scale(a,q):
    p=[q*a[0],q*a[1]]
    return (floor(min(p)),ceil(max(p)))


def atan_inverse(n):
    total=sum((Q((-1)**k,(2*k+1)*n**(2*k+1)) for k in range(64)),Q(0))
    # Last included term is negative; the alternating remainder is positive.
    return total,total+Q(1,129*n**129)


def pi_interval():
    a,b=atan_inverse(5),atan_inverse(239)
    low=16*a[0]-4*b[1];high=16*a[1]-4*b[0]
    return floor(low*S),ceil(high*S)


def sine_cosine(x):
    if max(abs(x[0]),abs(x[1]))>10*S:raise ArithmeticError('Taylor interval exceeds |x|<=10')
    X=(x[0]+x[1])//2;radius=max(X-x[0],x[1]-X)
    def series(sine):
        term=(X,X) if sine else (S,S);total=term
        for j in range(1,49):
            divisor=(2*j)*(2*j+1) if sine else (2*j-1)*(2*j)
            den=S*S*divisor
            term=((-term[1]*X*X)//den,-(-(-term[0]*X*X)//den))
            total=add(total,term)
        # Taylor remainder < one unit, since 10^98/98! < 1/S.
        return total[0]-radius-1,total[1]+radius+1
    return series(True),series(False)


def main(args):
    if 10**98*S>=factorial(98):raise ArithmeticError('Taylor remainder bound failed')
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Accepted prefix required')
    M=data['M'];state=[Q.from_float(float(v)) for v in data['states'][-1]]
    core=[Q.from_float(float(v)) for v in data['core']['coefficients']]
    if len(core)!=M:raise ValueError('Complete common core bandwidth required')
    rr=state[:M+1];tt=state[M+1:2*M+1];zz=state[2*M+1:]
    f=[2*k for k in range(1,M+1)];rho=[(1-k*k)*c for k,c in zip(f,core)]
    A=sum(abs(k*r+t) for k,r,t in zip(f,rr[1:],tt))
    B=abs(rr[0])+sum(abs(k*t+r) for k,r,t in zip(f,rr[1:],tt))
    C=sum(abs(k*z) for k,z in zip(f,zz[1:]));rho_upper=1+sum(map(abs,rho))
    speed=Q('5.765');density=Q('4.615')
    if A*A+B*B+C*C>=speed*speed or rho_upper>=density:
        raise ArithmeticError('The declared rational angular derivative budgets do not fit this parent')
    Rlo,Rhi=Q(args.radius_lower),Q(args.radius_upper);L=Q(args.length_lower);H=Q(args.height)
    radius_interval=(floor(Rlo*S),ceil(Rhi*S));pi=pi_interval();N=args.angles
    grid=[scale(pi,Q(2*j,N)) for j in range(N)]
    trig=[sine_cosine(a) for a in grid]
    maximum_square=-1;worst=-1;min_angle=10*S;max_angle=-10*S
    for j in range(N):
        R,T,Z=interval(rr[0]),(0,0),interval(zz[0]);theta=grid[j]
        for k in range(M):
            sn,cs=trig[(f[k]*j)%N]
            R=add(R,scale(cs,rr[k+1]));T=add(T,scale(sn,tt[k]));Z=add(Z,scale(cs,zz[k+1]))
            theta=add(theta,scale(sn,rho[k]/f[k]))
        min_angle=min(min_angle,theta[0]);max_angle=max(max_angle,theta[1])
        sp,cp=trig[j];st,ct=sine_cosine(theta)
        X=add(multiply(R,cp),neg(multiply(T,sp)))
        Y=add(multiply(R,sp),multiply(T,cp))
        dx=add(multiply(radius_interval,ct),neg(X))
        dy=add(multiply(radius_interval,st),neg(Y));dz=add(interval(H),neg(Z))
        square=sum(max(abs(a[0]),abs(a[1]))**2 for a in (dx,dy,dz))
        if square>maximum_square:maximum_square= square;worst=j
    root=isqrt(maximum_square)
    if root*root<maximum_square:root+=1
    sample_upper=Q(root,S);lip=speed+Rhi*density
    # pi<22/7 is also checked from the rigorous Machin interval.
    if Q(pi[1],S)>=Q(22,7):raise ArithmeticError('The elementary pi budget failed')
    angular_fee=lip*Q(22,7*N);all_upper=sample_upper+angular_fee
    margin=L-all_upper
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        parent_sha256=hashlib.sha256(raw).hexdigest(),cut=data['mesh'][-1],modes=M,angles=N,
        parameter_assumptions=dict(radius=[str(Rlo),str(Rhi)],length_lower=str(L),height=str(H)),
        exact_coefficient_budgets=dict(radial_component=float(A),tangential_component=float(B),
            vertical_component=float(C),speed_upper=str(speed),rho_l1=float(rho_upper),rho_upper=str(density)),
        sample_chord_upper_exact=str(sample_upper),sample_chord_upper=float(sample_upper),
        worst_sample_index=worst,chord_lipschitz_upper=str(lip),angular_cover_fee_exact=str(angular_fee),
        angular_cover_fee=float(angular_fee),all_angle_chord_upper_exact=str(all_upper),
        all_angle_chord_upper=float(all_upper),all_angle_margin_exact=str(margin),all_angle_margin=float(margin),
        all_chords_strictly_below_assumed_reference_length=bool(margin>0),
        arithmetic='Exact Python integers/Fraction; 10^24 fixed-point outward bounds; degree96/97 Taylor with <1 ulp remainder',
        reference_integrals_certified=False,nonlinear_tail_exists=False,closed_surface=False)
    text=json.dumps(out,indent=2)+'\n';args.out.write_text(text);print(text,end='')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--radius-lower',default='.531878');p.add_argument('--radius-upper',default='.531880')
    p.add_argument('--length-lower',default='1.289716');p.add_argument('--height',default='1.8')
    main(p.parse_args())
