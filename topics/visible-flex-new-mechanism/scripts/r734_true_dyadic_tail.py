"""Certified R734 fixed-j dyadic tail lines and finite two-jet spinor ports. Public Actions only."""
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

D = Decimal
LOW = Context(prec=84, rounding=ROUND_FLOOR)
HIGH = Context(prec=84, rounding=ROUND_CEILING)
NEAR = Context(prec=96, rounding=ROUND_HALF_EVEN)


class I:
    """Closed interval, with every arithmetic endpoint rounded outwards."""
    __slots__ = ('lo','hi')
    def __init__(self, lo, hi=None):
        if isinstance(lo,I):
            self.lo,self.hi=lo.lo,lo.hi
        else:
            self.lo=D(lo);self.hi=self.lo if hi is None else D(hi)
        if self.lo>self.hi:raise ValueError('Empty interval.')
    def __add__(self, other):
        o=I(other)
        return I(LOW.add(self.lo,o.lo),HIGH.add(self.hi,o.hi))
    __radd__=__add__
    def __neg__(self):return I(self.hi.copy_negate(),self.lo.copy_negate())
    def __sub__(self, other):return self+(-I(other))
    def __rsub__(self, other):return I(other)+(-self)
    def __mul__(self, other):
        o=I(other);pairs=((self.lo,o.lo),(self.lo,o.hi),(self.hi,o.lo),(self.hi,o.hi))
        return I(min(LOW.multiply(a,b) for a,b in pairs),max(HIGH.multiply(a,b) for a,b in pairs))
    __rmul__=__mul__
    def __truediv__(self, other):
        o=I(other)
        if o.lo<=0<=o.hi:raise ArithmeticError('Interval denominator contains zero.')
        return self*I(LOW.divide(D(1),o.hi),HIGH.divide(D(1),o.lo))
    def __rtruediv__(self, other):return I(other)/self
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError('Integer power required.')
        if n<0:return 1/(self**(-n))
        y=I(1);x=self
        while n:
            if n&1:y=y*x
            n//=2
            if n:x=x*x
        return y
    def norm(self):return max(self.lo.copy_abs(),self.hi.copy_abs())
    def distance_from_zero(self):
        return D(0) if self.lo<=0<=self.hi else min(self.lo.copy_abs(),self.hi.copy_abs())
    def bounds(self):return [str(self.lo),str(self.hi)]


def monotone_trans(a,name):
    # Decimal exp, ln and sqrt are correctly rounded nearest; expand by a NEAR ulp.
    q=I(a);f=getattr(NEAR,name)
    return I(LOW.plus(NEAR.next_minus(f(q.lo))),HIGH.plus(NEAR.next_plus(f(q.hi))))


def hull(a,b):return I(min(a.lo,b.lo),max(a.hi,b.hi))


def sym(upper):return I(upper.copy_negate(),upper)


def positive_power(x,h):
    if x.lo<=0 or x.hi>1 or h.lo<0 or h.hi>1:raise ValueError('Outside bounded exponential chart.')
    if h.lo==h.hi==0:return I(1)
    if h.lo==h.hi==1:return x
    v=monotone_trans(h*monotone_trans(x,'ln'),'exp')
    return I(max(D(0),v.lo),min(D(1),v.hi))


B=I(11)/50
L0=I(1)/512
MID=I(3)/4
HALF=I(1)/2
ONE=I(1)
ZERO=I(0)


def matrix_product(a,b):
    return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])


def matrix_norm(m):return max(HIGH.add(m[0].norm(),m[1].norm()),HIGH.add(m[2].norm(),m[3].norm()))


def integral_power(a,b,k):
    return (b**(k+1)-a**(k+1))/(k+1)


def constants(j):
    k=j*j;b0=I(256*k*(k-1))/B**2
    a=integral_power(HALF,MID,-5);b=b0*integral_power(MID,ONE,3)
    trace=17-a*b
    ls=32/(trace-monotone_trans(trace**2-64,'sqrt'));lu=trace-ls
    # First stable coordinate has unit Z, second unstable coordinate has unit F.
    p=(a/(ls-1+a*b),ONE,ONE,(16-ls)/a)
    det=p[0]*p[3]-p[1]*p[2]
    pin=tuple(v/det for v in (p[3],-p[1],-p[2],p[0]))
    kap=(1+a)*(1+b);c=8*(64+2*b0)+256*k+8*k*b0+64+2*b0
    cond=I(matrix_norm(p))*I(matrix_norm(pin))
    n=0
    while True:
        delta=L0/(I(2)**n*B)
        u=kap**2*c*delta
        if delta.hi<=(ONE/(8*k)).lo and u.hi< D('.1'):
            # e^u - 1 <= u/(1-u), for 0<=u<1.
            err=cond*16*kap*u/(1-u)
            if err.hi<=(ONE/128).lo:break
        n+=1
        if n>2048:raise ArithmeticError('The first proven tail cone exceeds this resolution.')
    e=err.hi
    hmax=((I(ls.norm())+2*I(e))/(I(lu.distance_from_zero())-2*I(e))).hi
    z=sym(hmax)
    line=(p[0]+z,ONE+p[3]*z)
    return n,line,dict(lam_stable=ls.bounds(),lam_unstable=lu.bounds(),cone_index=n,
           eigenbasis_error=err.bounds(),slope_next_in_unit_cone=sym(hmax).bounds(),
           asymptotic_line=[v.bounds() for v in line])


def smooth(y):
    # Monotone scalar quintic, evaluated only on [0,1] and clamped to its proven range.
    def point(z):
        if z<=0:return ZERO
        if z>=1:return ONE
        t=I(z)
        return t**3*(10+t*(-15+6*t))
    return I(max(D(0),point(y.lo).lo),min(D(1),point(y.hi).hi))


def profile(t,delta):
    h=(1-smooth((t-HALF-delta/2)/(delta/2)))/2
    h=h+smooth((t-MID+delta)/(2*delta))-smooth((t-ONE+delta)/(delta/2))/2
    return I(max(D(0),h.lo),min(D(1),h.hi))


def coefficients(t,L,H,j,sign):
    k=j*j;R=1-sign*L*t/B
    small=L**2*t**2/256
    a=R**(-2*k)*t**(-5)*positive_power(small,H)
    b=I(256*k*(k-1))/B**2*R**(2*k-2)*t**3*positive_power(small,1-H)
    return a,b


def interval_step(j,L,left,right,kind,sign):
    """Outward propagation from right to left. Time width is right-left."""
    q=hull(left,right);dt=right-left
    if dt.lo<=0:raise ArithmeticError("Declared arithmetic precision cannot separate these subdivision endpoints.")
    H=(ZERO if kind=='low' else ONE if kind=='high' else HALF if kind=='seam' else profile(q,L/B))
    a,b=coefficients(q,L,H,j,sign)
    z=dt**2*I(a.hi)*I(b.hi)
    if z.hi>=D('.2'):return None
    if kind in ('low','high','seam'):
        # Exact moment of the t power, enclosing only the positive radial multiplier.
        k=j*j;R=1-sign*L*q/B;base=(256*k*(k-1))/B**2
        if kind=='low':pa,pb=-5,5;ca,cb=ONE,L**2/256
        elif kind=='high':pa,pb=-3,3;ca,cb=L**2/256,ONE
        else:pa,pb=-4,4;ca,cb=L/16,L/16
        ia=R**(-2*k)*ca*integral_power(left,right,pa)
        ib=base*R**(2*k-2)*cb*integral_power(left,right,pb)
    else:ia=dt*a;ib=dt*b
    diag=(z/(2*(1-z/12))).hi
    odd=z/(6*(1-z/20))
    return (1+sym(diag),ia+sym((dt*I(a.hi)*odd).hi),
            -ib+sym((dt*I(b.hi)*odd).hi),1+sym(diag))


def pieces(L):
    d=L/B
    return [(HALF,HALF+d/2,'seam'),(HALF+d/2,HALF+d,'change'),
            (HALF+d,MID-d,'low'),(MID-d,MID+d,'change'),(MID+d,ONE-d,'high'),
            (ONE-d,ONE-d/2,'change'),(ONE-d/2,ONE,'seam')]


def projective(m,line):
    f,z=line
    x=m[3]*f-m[1]*z;y=m[0]*z-m[2]*f
    if max(x.distance_from_zero(),y.distance_from_zero())==0:
        return None
    return (ONE,y/x) if x.distance_from_zero()>y.distance_from_zero() else (x/y,ONE)


def cut_port(j,line,weight,sign):
    k=j*j;r=B-sign*L0
    if line[0].distance_from_zero()==0:return dict(normalization='homogeneous',line=[v.bounds() for v in line])
    # Physical choice f(cut)=1 is made only after certifying a nonzero first component.
    z_over_f=line[1]/line[0]
    f=ONE;w=weight*16*L0**4
    y=sign*(B/r)**(2*k)*weight*L0**4*z_over_f
    fp=k/r+y/w;fpp=sign*(4/L0)*(fp-k/r)
    U=r*y/(k-1);Up=-w*fp;Upp=sign*4/L0*w*fp-w*fpp
    def divided(a,ap,app):return (a/r,ap/r-a/r**2,app/r-2*ap/r**2+2*a/r**3)
    d=tuple((k-1)*v/j for v in divided(U,Up,Upp))
    e=tuple(-j*v for v in divided(f,fp,fpp))
    def jets(arr,sign):return [(sign*v/8).bounds() for v in arr]
    return dict(normalization='f(cut)=1',r=r.bounds(),w=w.bounds(),w_r=(-sign*4*w/L0).bounds(),
            f_0_1_2=[v.bounds() for v in (f,fp,fpp)],
            U_0_1_2=[v.bounds() for v in (U,Up,Upp)],V_0_1_2=[(-v/j).bounds() for v in (U,Up,Upp)],
            half_modes=[str(j)+'-1/2',str(j)+'+1/2'],
            stereo_za_real=[jets(d,-1),jets(d,1)],stereo_za_imag=[jets(e,-1),jets(e,1)],
            stereo_zb_real=[jets(d,-1),jets(d,-1)],stereo_zb_imag=[jets(e,-1),jets(e,-1)])

class Pause(Exception):
    pass


class Book:
    def __init__(self,limit,cfg):
        self.start=time.monotonic();self.limit=limit
        directory=Path(os.environ['RUNNER_TEMP'])/'r734-paid-tail'
        directory.mkdir(parents=True,exist_ok=True)
        self.path=directory/'tail.jsonl';self.records={}
        self.fingerprint=hashlib.sha256(Path(__file__).read_bytes()+json.dumps(cfg,sort_keys=True).encode()).hexdigest()
        if self.path.exists():
            with self.path.open() as f:
                for row in f:
                    record=json.loads(row)
                    if record['scientific_fingerprint']!=self.fingerprint:raise ValueError('Different paid tail.')
                    if record['key'] in self.records:raise ValueError('Duplicate paid unit.')
                    self.records[record['key']]=record['value']
        self.out=self.path.open('a',buffering=1)
        self.prior=sum(float(v.get('seconds',0.)) for v in self.records.values())
        self.next=None
    def once(self,key,fn):
        if key in self.records:return self.records[key]['data']
        self.next=key
        if time.monotonic()-self.start+3>=self.limit:raise Pause()
        start=time.monotonic();data=fn()
        record=dict(data=data,seconds=time.monotonic()-start)
        self.out.write(json.dumps(dict(scientific_fingerprint=self.fingerprint,key=key,value=record),
                                  separators=(',',':'),sort_keys=True,allow_nan=False)+'\n')
        self.records[key]=record;self.next=None
        return data


def leaf_system(j,n,part,depth,offset,segments,L,book,sign):
    tag=f'side{sign}_m{j}_n{n}_p{part}_h{depth}_i{offset}'
    def measure():
        a,b,kind=segments[part]
        lo=a+(b-a)*I(offset)/(2**depth);hi=a+(b-a)*I(offset+1)/(2**depth)
        local=interval_step(j,L,lo,hi,kind,sign)
        return None if local is None else [v.bounds() for v in local]
    receipt=book.once(tag,measure)
    if receipt is not None:return tuple(I(*v) for v in receipt)
    if depth>=48:raise ArithmeticError('Cell Peano enclosure requires more than 48 subdivisions in one direction.')
    key=tag+'_adaptive_children'
    if key not in book.records:
        left=leaf_system(j,n,part,depth+1,2*offset,segments,L,book,sign)
        right=leaf_system(j,n,part,depth+1,2*offset+1,segments,L,book,sign)
        book.once(key,lambda:[v.bounds() for v in matrix_product(left,right)])
    return tuple(I(*v) for v in book.records[key]['data'])


def reduced_cell(j,n,depth,book,sign):
    key=f'side{sign}_m{j}_n{n}_depth{depth}_complete'
    if key in book.records:return tuple(I(*v) for v in book.records[key]['data'])
    L=L0/(I(2)**n);segments=pieces(L)
    m=(ONE,ZERO,ZERO,ONE)
    # Each segment maps larger t to smaller t; left multiplication preserves this order.
    for part in reversed(range(len(segments))):
        for offset in reversed(range(2**depth)):
            prefix=f'side{sign}_m{j}_n{n}_depth{depth}_p{part}_i{offset}_outward_prefix'
            if prefix not in book.records:
                q=leaf_system(j,n,part,depth,offset,segments,L,book,sign)
                book.once(prefix,lambda:[v.bounds() for v in matrix_product(q,m)])
            m=tuple(I(*v) for v in book.records[prefix]['data'])
    m=(m[0],m[1],16*m[2],16*m[3])
    data=book.once(key,lambda:[v.bounds() for v in m])
    return tuple(I(*v) for v in data)


def widths(line):
    if line is None:return None
    x,z=line
    measured=x if z.lo==z.hi==1 else z
    return (I(measured.hi)-I(measured.lo)).hi,HIGH.divide((I(measured.hi)-I(measured.lo)).hi,
                                                           max(measured.distance_from_zero(),D('1e-70')))


def solve_mode(j,weight,tolerance,maximum_depth,book,sign):
    starting=book.once(f'm{j}_tail_cone',lambda:constants(j)[2])
    nstar=starting['cone_index']
    line=tuple(I(*v) for v in starting['asymptotic_line'])
    history=[]
    for n in range(nstar-1,-1,-1):
        key=f'side{sign}_m{j}_n{n}_accepted_line'
        if key in book.records:
            accepted=book.records[key]['data']
        else:
            best=None
            for depth in range(maximum_depth+1):
                candidate=projective(reduced_cell(j,n,depth,book,sign),line)
                if candidate is None:continue
                if best is not None:
                    # If charts differ, re-express the old enclosure only on a certified denominator.
                    old=best
                    if candidate[1].lo==candidate[1].hi==1:
                        if old[1].distance_from_zero():old=(old[0]/old[1],ONE)
                        else:old=None
                    else:
                        if old[0].distance_from_zero():old=(ONE,old[1]/old[0])
                        else:old=None
                    if old is not None:candidate=tuple(I(max(a.lo,b.lo),min(a.hi,b.hi)) for a,b in zip(candidate,old))
                best=candidate
                _,relative=widths(best)
                if relative<=tolerance:
                    accepted=book.once(key,lambda:dict(cell=n,depth=depth,line=[v.bounds() for v in best],relative_width=str(relative)))
                    break
            else:
                return dict(kind='unclosed_at_resolution',cell=n,last_completed_outer=n+1,
                        maximum_depth=maximum_depth,actual_enclosure=None if best is None else [v.bounds() for v in best],
                        paid_outer_lines=history,asymptotic_cone=starting)
        line=tuple(I(*v) for v in accepted['line']);history.append(accepted)
    return dict(kind='certified_tail_port',mode=j,side='outer' if sign==1 else 'inner',actual_cut_port=cut_port(j,line,weight,sign),paid_outer_lines=history,
                asymptotic_cone=starting,certificate='fixed angular mode on the stated entire infinite collar',
                whole_annulus_closure=False,finite_angle_solution=False)


def main():
    if (os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY','').lower()!='rogerhu12/math-research-public'
        or not os.environ.get('GITHUB_RUN_ID','').isdigit()):
        raise SystemExit('Public scientific Actions runner required.')
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-seconds',type=float,required=True);ap.add_argument('--maximum-depth',type=int,default=10)
    ap.add_argument('--relative-width',default='.025');ap.add_argument('--weight',default='.03125')
    ap.add_argument('--sides',nargs='+',choices=('outer','inner'),default=['outer','inner'])
    ap.add_argument('--modes',nargs='+',type=int,default=[2,3]);args=ap.parse_args()
    if any(j<2 for j in args.modes) or not (0<D(args.relative_width)<1 and D(args.weight)>0):
        raise ValueError('Invalid declared physical target.')
    book=Book(args.max_seconds,dict(modes=args.modes,sides=args.sides,width=args.relative_width,W=args.weight,decimal_precision=LOW.prec))
    result={}
    try:
        for side in args.sides:
            for j in args.modes:
                result[side+str(j)]=solve_mode(j,I(args.weight),D(args.relative_width),args.maximum_depth,book,1 if side=='outer' else -1)
        kind='terminal'
    except Pause:
        kind='paid_partial'
    finally:
        book.out.flush();book.out.close()
    summary=dict(kind=kind,source_fingerprint=book.fingerprint,completed_modes=result,pending=book.next,
        paid_units=len(book.records),previous_paid_unit_seconds=book.prior,current_elapsed_seconds=time.monotonic()-book.start,
        actual_cut='11/50 - sign/512, sign=+1 outer or -1 inner',scientific_new=True,README_completion_claim=False)
    print('R734_FINAL '+json.dumps(summary,sort_keys=True,separators=(',',':'),allow_nan=False),flush=True)


if __name__=='__main__':main()
