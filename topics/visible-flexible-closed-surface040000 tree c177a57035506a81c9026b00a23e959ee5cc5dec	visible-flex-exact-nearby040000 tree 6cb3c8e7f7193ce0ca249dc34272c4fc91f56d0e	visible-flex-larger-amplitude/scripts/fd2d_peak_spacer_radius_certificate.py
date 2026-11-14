#!/usr/bin/env python3
"""Exact-rational positivity/radius packet for a peak-spacer scalar metric.

No sampled derivative sign or floating quadrature is used in the verdict.
The fixed a0 interval is reused from the published Taylor moment certificate.
Both exact binary64 and exact-decimal readings of numerical shared jets are
checked. The geometric cut is exactly 4/5 and the terminal phase is -pi/2.
"""
from __future__ import annotations
import argparse,hashlib,json,math,time
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def interval(a,b=None):return (F(a),F(a if b is None else b))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    q=[x*y for x in a for y in b];return min(q),max(q)
def scale(a,q):return mul(a,interval(q))
def div(a,b):
    if b[0]<=0<=b[1]:raise ZeroDivisionError('interval contains zero')
    return mul(a,(1/b[1],1/b[0]))
def packet(a):return {'lower_exact':str(a[0]),'upper_exact':str(a[1]),'lower_display':float(a[0]),'upper_display':float(a[1])}


def atan_unit(q,terms=16):
    x=F(1,q);s=F(0)
    for j in range(terms):s+=(-1)**j*x**(2*j+1)/F(2*j+1)
    next_term=x**(2*terms+1)/F(2*terms+1)
    return (s,s+next_term) if terms%2==0 else (s-next_term,s)


def pi_interval():return sub(scale(atan_unit(5),16),scale(atan_unit(239),4))


def sin_point(x):
    if x<0:
        lo,hi=sin_point(-x);return -hi,-lo
    if x>2:raise ValueError('Taylor bound here assumes |x|<=2')
    s=F(0)
    for j in range(10):s+=(-1)**j*x**(2*j+1)/math.factorial(2*j+1)
    return s,s+x**21/math.factorial(21)


def sin_interval(a):
    # All phase intervals in this proof are contained in [-pi/2,.3].
    return sin_point(a[0])[0],sin_point(a[1])[1]


def asin_small(x):
    lo,hi=x,F(3,10)
    if not 0<x<sin_point(hi)[0]:raise ValueError('positive phase bracket failed')
    for unused in range(64):
        mid=(lo+hi)/2;s=sin_point(mid)
        if s[1]<x:lo=mid
        elif s[0]>x:hi=mid
        else:break
    return lo,hi


def quintic(h,j0,j1):
    c0=j0[0];c1=h*j0[1];c2=h*h*j0[2]/2
    d=j1[0]-c0-c1-c2;v=h*j1[1]-c1-2*c2;acc=h*h*j1[2]-2*c2
    return [c0,c1,c2,10*d-4*v+acc/2,-15*d+7*v-acc,6*d-3*v+acc/2]


def bernstein(power):
    n=len(power)-1
    return [sum(F(math.comb(i,j),math.comb(n,j))*power[j] for j in range(i+1)) for i in range(n+1)]


def split_half(b):
    row=list(b);left=[row[0]];right=[row[-1]]
    while len(row)>1:
        row=[(row[i]+row[i+1])/2 for i in range(len(row)-1)]
        left.append(row[0]);right.append(row[-1])
    return left,list(reversed(right))


def nonnegative(b,depth=0):
    if min(b)>=0:return True,[(depth,min(b),max(b))]
    if depth>=16:return False,[(depth,min(b),max(b))]
    left,right=split_half(b);ok0,r0=nonnegative(left,depth+1);ok1,r1=nonnegative(right,depth+1)
    return ok0 and ok1,r0+r1


def dyadic(data):
    sign,mantissa,exponent,bits=map(int,data)
    return F((-1 if sign else 1)*mantissa)*(F(2)**exponent)


def ramp_integral(u):
    if u<F(2,25):
        t=u/F(2,25);return F(2,25)*(t**3-t**4/2)
    if u>F(23,25):
        t=(1-u)/F(2,25);return F(23,25)-F(2,25)*(t**3-t**4/2)
    return u-F(1,25)


def phase_at(piece,u):
    p0,p1=piece['P0'],piece['P1'];kind=piece['kind']
    if kind in ('coast','coast_to'):return p0
    if kind=='turn':return add(p0,scale(sub(p1,p0),ramp_integral(u)/F(23,25)))
    if kind!='phase_bridge':raise ValueError('unexpected phase piece')
    h00=(1-u)**2*(1+2*u);h01=u*u*(3-2*u)
    extra=piece['L']*(u*(1-u)**2*piece['ps0']-u*u*(1-u)*piece['ps1'])
    return add(add(scale(p0,h00),scale(p1,h01)),interval(extra))


def phase_integral_enclosure(piece,steps):
    L=piece['L']
    previous=sin_interval(phase_at(piece,F(0)));lo=hi=F(0)
    for j in range(1,steps+1):
        current=sin_interval(phase_at(piece,F(j,steps)))
        lo+=min(previous[0],current[0]);hi+=max(previous[1],current[1]);previous=current
    return (L*lo/steps,L*hi/steps)


def run_encoding(path,a0,steps,binary):
    raw=json.loads(path.read_text(),parse_float=(float if binary else Decimal))
    q=lambda x:F(x)
    rows=raw['segments'];certs=[];all_v=True;all_acc=True
    for index,p in enumerate(rows):
        if p['kind']!='hermite':continue
        h=q(p['L']);j0=list(map(q,p['jet0']));j1=list(map(q,p['jet1']))
        c=quintic(h,j0,j1)
        vb=bernstein([j*c[j]/h for j in range(1,6)])
        ab=bernstein([j*(j-1)*c[j]/(h*h) for j in range(2,6)])
        ok_v,vr=nonnegative(vb);ok_acc,ar=nonnegative(ab)
        upper_v=max(x[2] for x in vr)
        all_v &= ok_v and upper_v<1;all_acc &= ok_acc
        certs.append(dict(index=index,velocity_nonnegative=ok_v,velocity_upper_exact=str(upper_v),
            acceleration_nonnegative=ok_acc,velocity_leaf_count=len(vr),acceleration_leaf_count=len(ar),
            acceleration_control_lower_exact=str(min(x[1] for x in ar)),
            acceleration_control_upper_exact=str(max(x[2] for x in ar))))
    last=next(p for p in reversed(rows) if p['kind']=='hermite')
    speed=q(last['jet1'][1]);P=asin_small(speed)
    radius=add(a0,interval(q(last['jet1'][0])))
    phase_rows=[];negative_after_cross=False;crossings=0;phase_ok=True
    deep_before=None;deep_phase=None;brake_integral=None
    start=next(i for i,p in enumerate(rows) if p.get('label')=='outward_peak_spacer')
    for rawp in rows[start:]:
        p=dict(rawp);kind=p['kind'];p['P0']=P
        p['P1']=scale(pi_interval(),F(-1,2)) if p.get('exact_endpoint_phase')=='-pi/2' else interval(q(p['p1']))
        if kind in ('coast','coast_to'):p['P1']=P
        if kind=='coast_to':
            deep_before=radius;deep_phase=P
            P=p['P1'];continue
        if p.get('length_from_turn_rate'):
            difference=sub(p['P1'],P)
            if difference[0]!=difference[1]:raise ValueError('only exact endpoint turn lengths are supported')
            p['L']=abs(difference[0])/(q(p['K'])*F(23,25))
        else:p['L']=q(p['L'])
        if kind=='phase_bridge':
            p['ps0']=q(p['ps0']);p['ps1']=q(p['ps1'])
            middle=sub(scale(sub(p['P1'],P),3/p['L']),interval(p['ps0']+p['ps1']))
            controls=[interval(p['ps0']),middle,interval(p['ps1'])]
            decreasing=all(x[1]<=0 for x in controls)
            increasing=all(x[0]>=0 for x in controls)
            monotone=decreasing or increasing
        else:monotone=True
        if not monotone:phase_ok=False
        if negative_after_cross and max(P[1],p['P1'][1])>0:phase_ok=False
        if P[0]>0 and p['P1'][1]<0:
            crossings+=1;negative_after_cross=True
        if min(P[0],p['P1'][0])<scale(pi_interval(),F(-1,2))[0]:phase_ok=False
        if max(P[1],p['P1'][1])>F(3,10):phase_ok=False
        integral=(p['L']*speed,p['L']*speed) if p.get('label')=='outward_peak_spacer' else phase_integral_enclosure(p,steps)
        if p.get('label')=='cut_second_jet_brake':brake_integral=integral
        elif deep_before is None:radius=add(radius,integral)
        phase_rows.append(dict(label=p.get('label'),L_exact=str(p['L']),monotone_proved=monotone,
            start_phase=packet(P),end_phase=packet(p['P1']),radial_integral=packet(integral)))
        P=p['P1']
    if deep_before is None or brake_integral is None:raise ValueError('missing derived final coast')
    # a_before + Ldeep*sin(Pdeep) + Ibrake = 4/5 exactly.
    numerator=sub(sub(interval(F(4,5)),brake_integral),deep_before)
    deep=div(numerator,sin_interval(deep_phase))
    good=all_v and phase_ok and crossings==1 and deep[0]>0 and a0[0]>F(4,5)
    return dict(encoding='exact binary64 numerical data' if binary else 'exact written decimal numerical data',
        hermite_velocity_nonnegative_and_less_than_one=bool(all_v),
        hermite_acceleration_nonnegative=bool(all_acc),hermite_rows=certs,
        phase_rows=phase_rows,one_positive_to_negative_phase_crossing=crossings==1,
        phase_sign_pattern_proved=bool(phase_ok),derived_deep_coast=packet(deep),
        exact_radius_lower='4/5' if good else None,radius_lower_proved=bool(good),
        retained_feedback_Gauss_curvature_nonpositive=bool(all_acc and good))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    root=Path(__file__).resolve().parent.parent
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--moments',type=Path,default=root/'notes/2026-11-12-fd2d-balanced-moments-taylor-01.json')
    ap.add_argument('--steps',type=int,default=512)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError(args.out)
    start=time.monotonic();mom=json.loads(args.moments.read_text());row=mom['enclosures']['a0']
    if mom['parameters']['reference_A']!='1.4' or mom['parameters']['reference_B']!='0.5':raise ValueError('Wrong reference ellipse')
    a0=(dyadic(row['binary_lower']),dyadic(row['binary_upper']))
    rows=[run_encoding(args.candidate,a0,args.steps,binary) for binary in (True,False)]
    report=dict(schema='fd2d-peak-spacer-exact-radius-lower-v1',actual_execution=True,
        candidate_file=args.candidate.name,candidate_sha256=digest(args.candidate),
        source_sha256=digest(__file__),a0_source_sha256=digest(args.moments),a0=packet(a0),
        pi_method='Machin identity with 16 alternating rational terms for each arctangent',
        sin_method='Alternating Taylor terms through degree 19, bounded by degree-21 next term',
        radial_integral_method='Monotone endpoint interval Riemann sums using exact rationals',
        cells_per_phase_piece=args.steps,encodings=rows,
        passed=all(r['radius_lower_proved'] for r in rows),seconds=time.monotonic()-start,
        scope='Scalar continuous a>=4/5 and retained feedback K<=0 only. No nonlinear embedding, normal ball or strong-target claim.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='encodings'},allow_nan=False))
    print(json.dumps([{'encoding':r['encoding'],'radius_lower_proved':r['radius_lower_proved'],
        'feedback_K_nonpositive':r['retained_feedback_Gauss_curvature_nonpositive'],
        'deep':r['derived_deep_coast']} for r in rows]))
    if not report['passed']:raise SystemExit(1)
if __name__=='__main__':main()
