#!/usr/bin/env python3
"""Outward interval upper sum for the exact scalar warp cost A.

The first 24 cells use interval Riemann upper sums. The remaining finite
cells and the tiny exact source gap together have the analytic bound 1e-8
proved in the accompanying note. This establishes lambda>0, not a nonlinear
tail or a surface-reach certificate.
"""
import argparse,json,hashlib,time
from pathlib import Path
from fractions import Fraction
import mpmath
from mpmath import iv


def binary(x):
    p,q=float(x).as_integer_ratio();return iv.mpf(p)/iv.mpf(q)


def hull(lo,hi):return iv.mpf([lo.a,hi.b])


def clamp(x):return iv.mpf([max(iv.mpf(0),x.a),min(iv.mpf(1),x.b)])


def smooth_point(x):return x**3*(10+x*(-15+6*x))


def smooth(x):return hull(smooth_point(x.a),smooth_point(x.b))


def dsmooth(x):
    f=lambda t:30*t*t*(1-t)*(1-t)
    vals=[f(x.a),f(x.b)]
    if x.a<=iv.mpf('.5')<=x.b:vals.append(iv.mpf(15)/8)
    return iv.mpf([min(v.a for v in vals),max(v.b for v in vals)])


def S7(x):return x**4*(35+x*(-84+x*(70-20*x)))


def cap_point(z,c):
    d=z-c
    if d.b<=-2:return z
    if d.a>=2:return c
    t=clamp((d+2)/4)
    J=lambda u:u**5*(7+u*(-14+u*(10-iv.mpf('2.5')*u)))
    if t.b<=iv.mpf('.5'):I=t-J(t)
    elif t.a>=iv.mpf('.5'):I=iv.mpf('.5')-J(1-t)
    else:I=t-J(t)
    return c-2+4*I


def cap(z,c,zx,cx):
    # cap(z,c) is increasing in each argument; its derivative in z is
    # d=1-S7((z-c+2)/4), clipped to the constant branches.
    if z.b<=c.a-2:return z,zx
    if z.a>=c.b+2:return c,cx
    lo=cap_point(z.a,c.a);hi=cap_point(z.b,c.b);value=hull(lo,hi)
    t=clamp((z-c+2)/4)
    d=iv.mpf([max(iv.mpf(0),(1-S7(t.b)).a),min(iv.mpf(1),(1-S7(t.a)).b)])
    return value,d*zx+(1-d)*cx


def upper_fraction(x):
    sign,mantissa,exp,_=x._mpi_[1]
    q=Fraction((-1 if sign else 1)*int(mantissa))
    return q*(2**exp) if exp>=0 else q/Fraction(2**(-exp))


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('packet',type=Path);p.add_argument('out',type=Path)
    p.add_argument('--subdivisions',type=int,default=128);p.add_argument('--dps',type=int,default=40);args=p.parse_args()
    if args.out.exists():raise RuntimeError('unused output required')
    iv.dps=args.dps;data=json.loads(args.packet.read_text());cfg=data['config'];N=cfg['protectCell'];div=args.subdivisions
    assert N==160 and cfg['orientation']==1 and cfg['prefixR']==64 and cfg['capMode']=='cut-preserving'
    assert cfg.get('warpWeightLevels',[])==[] and cfg['capTransition']==2 and cfg['curvatureBound']==7
    assert cfg['rCut']==.5 and cfg['width']==.18 and cfg['wCut'] in (.1,.3)
    assert len(data['finite_source_alphas'])==160 and all(.5<=a<=2 for a in data['finite_source_alphas'])
    assert all(-5<=b<=5 for b in cfg['valleyControls'])
    for n,(c1,c2) in enumerate(cfg['pulseCaps']):
        assert Fraction.from_float(c1)==64*Fraction.from_float(c2)
        assert Fraction.from_float(cfg['valleyCaps'][n])==Fraction.from_float(c2)
        scaled=binary(c1)*iv.power(2,iv.mpf(7)*n/4)
        assert iv.mpf('.299')<scaled<iv.mpf('.301')
    d0=iv.mpf(3)/500;c0=iv.mpf(1)/20;a=iv.mpf(11)/4;root=iv.sqrt(12);cuff=iv.mpf(8)/25;wc=iv.mpf(str(cfg['wCut']))
    totalLog=6*d0+6*c0*d0/(1-iv.power(2,-iv.mpf(3)/2));oldCut=cuff*iv.exp(totalLog/root)
    logEpsilon=iv.log(wc)+7*iv.log(oldCut)-a*iv.log(2*d0)
    A=iv.mpf(0);rows=[];started=time.monotonic()
    report=dict(schema='fd2d-layered-positive-warp-interval-v1',packet_file=args.packet.name,
        packet_sha256=hashlib.sha256(args.packet.read_bytes()).hexdigest(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        config_sha256=data['config_sha256'],subdivisions=div,first_cells=24,dps=args.dps,mpmath_version=mpmath.__version__,
        rows=rows,completed=False,passed=False,scope=__doc__)
    for n in range(24):
        delta=d0*iv.power(2,-n);c=c0*iv.power(2,-iv.mpf(n)/2);alpha=binary(data['finite_source_alphas'][n]);beta=binary(cfg['valleyControls'][n])
        after=3*d0*iv.power(2,-n)+6*c0*d0*iv.power(2,-iv.mpf(3)*(n+1)/2)/(1-iv.power(2,-iv.mpf(3)/2))
        logR0=iv.log(cuff)+after/root;logMu=logEpsilon+a*iv.log(delta)
        levels=[iv.log(delta),iv.log(64),2*iv.log(delta)-iv.log(alpha)+beta,iv.mpf(0),iv.log(delta)+a*iv.log(2)]
        caps=[iv.mpf('.004'),binary(cfg['pulseCaps'][n][0]),binary(cfg['valleyCaps'][n]),binary(cfg['pulseCaps'][n][1]),iv.mpf('.004')]
        offset=iv.mpf(0);cellSum=iv.mpf(0)
        for j in range(9):
            k=j//2;length=delta*(c if j%2 or j in (0,8) else 1);segmentSum=iv.mpf(0)
            for i in range(div):
                x=iv.mpf([iv.mpf(i)/div,iv.mpf(i+1)/div]);S=smooth(x);Sp=dsmooth(x)
                lo=levels[k];hi=levels[k+1] if j%2 else lo
                logR=logR0+(offset+length*x)/root;rOld=iv.exp(logR);rxOld=length*rOld/root
                raw=logMu+lo+(hi-lo)*S-iv.log(delta)-7*logR
                rawx=(hi-lo)*Sp-7*length/root
                cl=iv.log(caps[k]);ch=iv.log(caps[k+1]) if j%2 else cl
                lc=cl+(ch-cl)*S;lcx=(ch-cl)*Sp
                z,zx=cap(raw,lc,rawx,lcx)
                if n==0 and j==7:
                    z,zx=S*raw+(1-S)*z,S*rawx+(1-S)*zx+Sp*(raw-z)
                if n==0 and j==8:z,zx=raw,rawx
                w=iv.exp(z);E=1+w*w
                chi=1-S if n==0 and j==8 else iv.mpf(1)
                j0=1+(iv.mpf('.5')/oldCut-1)*S if n==0 and j==8 else iv.mpf(1)
                integrand=(1-chi)*rxOld*j0+chi*abs(w*zx)/(7*E*iv.sqrt(E))
                segmentSum+=integrand/div
            cellSum+=segmentSum;offset+=length
        A+=cellSum
        rows.append(dict(cell=n,cost_interval=str(cellSum),accumulated_interval=str(A)))
        report['seconds']=time.monotonic()-started;args.out.write_text(json.dumps(report,indent=2)+'\n')
        if n%4==0:print(json.dumps(dict(cell=n,A=str(A),seconds=report['seconds'])),flush=True)
    remainder=iv.mpf(1)/10**8;bound=A+remainder;U=upper_fraction(bound)
    report.update(completed=True,passed=bool(bound<iv.mpf(9)/50),first24_cost_interval=str(A),
        remainder_and_deep_gap_upper='1/100000000',A_plus_deep_gap_upper_numerator=str(U.numerator),A_plus_deep_gap_upper_denominator=str(U.denominator),
        strict_width=bool(bound<iv.mpf(9)/50),upper_decimal_approx=float(U),
        positive_lambda_follows=bool(bound<iv.mpf(9)/50),B_positive_reason='chi*r_old_x/(1+w^2)>0 on a nonempty open body interval',
        seconds=time.monotonic()-started,nonlinear_tail_solved=False,actual_nonround_reach_certified=False)
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['completed','passed','upper_decimal_approx','seconds']}),flush=True)


if __name__=='__main__':main()
