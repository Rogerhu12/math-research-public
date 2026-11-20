"""Exact C2 prefix pieces used by the accepted M24 prefix-height certificate.

Pure representation library: import does not load a field, run a solver, or
execute an integral/certificate.  Set ``b.m.K`` before constructing
``PrefixPieces(o,z)``.  The shared Y/e coefficients and normalized multistage
profile are exactly those in ``resume_n4/certify_m24_prefix_height.py``.
Fractions define the functions; floating interval coefficients only enclose
those exact fractions.  Third derivatives are one-sided on each grid cell;
the common endpoint contract is C2, not a claim of C3 at Hermite/lift joins.
"""
from bisect import bisect_right
from fractions import Fraction as Q
from math import comb
import numpy as np
import certify_bridge_metric_fourier_taylor as b

I = b.I


def fq(x):
    return Q.from_float(float(x))


def qval(poly, x):
    value = Q(0)
    for c in poly[::-1]:
        value = value*x+c
    return value


def qder(poly):
    return [(i+1)*poly[i+1] for i in range(len(poly)-1)]


def right_correction(poly, h, target):
    old = [qval(poly,h),qval(qder(poly),h),qval(qder(qder(poly)),h)]
    d0,d1,d2 = [v-u for u,v in zip(old,target)]
    return [Q(0),Q(0),Q(0),(10*d0-4*h*d1+h*h*d2/2)/h**3,
            (-15*d0+7*h*d1-h*h*d2)/h**4,
            (6*d0-3*h*d1+h*h*d2/2)/h**5]


def _iarray(values):
    pairs = [I.rational(v).x for v in values]
    return I(np.asarray([float(v[0]) for v in pairs]),
             np.asarray([float(v[1]) for v in pairs]))


def _poly(c, x, size=None):
    value = I(0) if size is None else I(np.zeros(size))
    for item in c[::-1]:
        value = value*x+item
    return value


def _power(coef, n):
    out = [Q(1)]
    for _ in range(n):
        new = [Q(0)]*(len(out)+len(coef)-1)
        for i,u in enumerate(out):
            for j,v in enumerate(coef):
                new[i+j] += u*v
        out = new
    return out


def _add_scaled(dst, src, factor):
    while len(dst)<len(src):
        dst.append(Q(0))
    for i,c in enumerate(src):
        dst[i] += factor*c


def _turn_polynomials(eta):
    """Exact P,F in u for the same three original turn-ramp branches."""
    den = 1-eta
    low = [Q(0)]*6
    low[4],low[5] = 1/(4*eta**2*den),-1/(10*eta**3*den)
    middle = [Q(3,20)*eta**2/den,-eta/(2*den),1/(2*den)]
    high = [-Q(1,2),Q(1)]
    _add_scaled(high,_power([Q(1),-Q(1)],4),1/(4*eta**2*den))
    _add_scaled(high,_power([Q(1),-Q(1)],5),-1/(10*eta**3*den))
    return (low,middle,high)


class PrefixPieces:
    def __init__(self, o, z):
        if b.m.K is None:
            raise ValueError('Set b.m.K to the outward interval kernel first')
        self.o,self.z = o,z
        o.initial(z.p)
        self.f = f = o.flow(z.p[0])
        self.M,self.n = int(o.M),int(o.n)
        if self.M!=24 or f.base_mode!=3:
            raise ValueError('This representation is the declared m3 M24 prefix')
        self.q = I(o.q)
        self.q_exact = fq(o.q)
        self.entry,self.end = fq(f.prefix_end),fq(f.end)
        self.xx = [fq(v) for v in z.x]
        if not self.entry<Q(3,4)*self.end:
            raise ValueError('The unchanged late angular cutoff enters this prefix')
        self.frequencies = np.asarray(f.even,int)
        self.field_coefficients_exact = {}
        self.field_right_targets_exact = {}
        self.pc = {}
        for i in range(len(self.xx)-1):
            if self.xx[i]>=self.entry:
                break
            h = self.xx[i+1]-self.xx[i]
            if h<=0:
                raise ValueError('Nonincreasing physical field grid')
            rows,targets = [],[]
            for j in range(self.n):
                pp = [fq(z.sol.c[5-k,i,j]) for k in range(6)]
                if i+1<len(self.xx)-1:
                    target = [fq(z.sol.c[5,i+1,j]),fq(z.sol.c[4,i+1,j]),
                              2*fq(z.sol.c[3,i+1,j])]
                else:
                    target = [qval(pp,h),qval(qder(pp),h),
                              qval(qder(qder(pp)),h)]
                cc = right_correction(pp,h,target)
                rows.append([a+c for a,c in zip(pp,cc)])
                targets.append(target)
            self.field_coefficients_exact[i] = rows
            self.field_right_targets_exact[i] = targets
            self.pc[i] = [_iarray([row[k] for row in rows]) for k in range(6)]
        self.spx = [fq(v)*self.end for v in f.spline.x]
        self.chart_coefficients_exact,self.ec = {},{}
        self.chart_right_targets_exact = {}
        for i in range(len(self.spx)-1):
            if self.spx[i]>=self.entry:
                break
            pp = [fq(f.spline.c[3-k,i])/self.end**k for k in range(4)]+[Q(0),Q(0)]
            h = self.spx[i+1]-self.spx[i]
            if i+1<len(self.spx)-1:
                target = [fq(f.spline.c[3,i+1]),fq(f.spline.c[2,i+1])/self.end,
                          2*fq(f.spline.c[1,i+1])/self.end**2]
            else:
                target = [qval(pp,h),qval(qder(pp),h),qval(qder(qder(pp)),h)]
            cc = right_correction(pp,h,target)
            exact = [(a+c)*fq(f.warp_e) for a,c in zip(pp,cc)]
            self.chart_coefficients_exact[i] = exact
            self.chart_right_targets_exact[i] = [v*fq(f.warp_e) for v in target]
            self.ec[i] = [I.rational(v) for v in exact]
        spec = f.cfg['multistage_flat']
        self.eta = eta = Q(spec['eta'])
        self.amplitude_ratio = fq(f.delta)/Q(spec['reference_delta'])
        reference,t,area = [],Q(0),Q(0)
        for name in ('up','down'):
            for row in spec[name]:
                v0,v1,L = map(Q,row)
                reference.append((t,L,v0,v1,area))
                area += L*(v0+v1)/2
                t += L
        if area!=0 or reference[0][2]!=0 or reference[-1][3]!=0:
            raise ValueError('The exact reference prefix does not return')
        self.reference = reference
        self.duration_ratio = self.entry/t
        self.velocity_ratio = self.amplitude_ratio/self.duration_ratio
        self.segments,self.profile_pieces = [],[]
        turns = _turn_polynomials(eta)
        for start,L,v0,v1,old_area in reference:
            origin,length = self.duration_ratio*start,self.duration_ratio*L
            self.segments.append((origin,length,v0,v1,old_area,L))
            dv = v1-v0
            zones = [(Q(0),Q(1),[Q(0)])] if dv==0 else [
                (Q(0),eta,turns[0]),(eta,1-eta,turns[1]),(1-eta,Q(1),turns[2])]
            for left,right,P in zones:
                # Same exact a = 1 + r*(area + L*(v0*u + dv*P(u))).
                aa = [Q(1)+self.amplitude_ratio*old_area,
                      self.amplitude_ratio*L*v0]
                _add_scaled(aa,P,self.amplitude_ratio*L*dv)
                derivatives = [aa]
                for _ in range(3):
                    derivatives.append(qder(derivatives[-1]))
                values = [[I.rational(c/length**k) for c in d]
                          for k,d in enumerate(derivatives)]
                physical_left,physical_right = origin+length*left,origin+length*right
                center = (physical_left+physical_right)/2
                uc = (center-origin)/length
                # Exact identity a(u)=sum centered[j]*(s-center)**j.
                # This changes interval representation only; aa remains the
                # defining original u polynomial used in endpoint reports.
                centered = [sum((aa[k]*comb(k,j)*uc**(k-j)
                                 for k in range(j,len(aa))),Q(0))/length**j
                            for j in range(len(aa))]
                back = [sum((centered[k]*comb(k,j)*(origin-center)**(k-j)
                             for k in range(j,len(centered))),Q(0))*length**j
                        for j in range(len(centered))]
                if back!=aa:
                    raise ArithmeticError('Exact midpoint representation identity failed')
                cd = [centered]
                for _ in range(3):
                    cd.append(qder(cd[-1]))
                centered_values = [[I.rational(c) for c in d] for d in cd]
                self.profile_pieces.append(dict(left=physical_left,
                    right=physical_right,origin=origin,length=length,
                    coefficients_exact=aa,derivatives=values,center=center,
                    centered_coefficients_exact=centered,
                    centered_derivatives=centered_values))
        self.profile_starts = [p['left'] for p in self.profile_pieces]
        self.lift_lo,self.lift_hi = fq(.5)*self.entry,fq(.9)*self.entry
        self.lift_coefficients_exact = [Q(1),Q(0),Q(0),-Q(10),Q(15),-Q(6)]
        derivatives = [self.lift_coefficients_exact]
        for _ in range(3):
            derivatives.append(qder(derivatives[-1]))
        self.lift_derivatives = [[I.rational(c/(self.lift_hi-self.lift_lo)**k)
                                 for c in d] for k,d in enumerate(derivatives)]
        self.grid = sorted(set([Q(0),self.entry,self.lift_lo,self.lift_hi]+
            [v for v in self.xx if 0<v<self.entry]+
            [v for v in self.spx if 0<v<self.entry]+
            [p['left'] for p in self.profile_pieces]+
            [p['right'] for p in self.profile_pieces]))

    def _domain(self,left,right):
        left,right = Q(left),Q(right)
        if not 0<=left<=right<=self.entry:
            raise ValueError('A prefix interval must lie in [0,entry]')
        return left,right,(left+right)/2

    def _index(self,knots,available,left,right):
        left,right,mid = self._domain(left,right)
        i = min(max(available),max(0,bisect_right(knots,mid)-1))
        if left<knots[i] or right>knots[i+1]:
            raise ValueError('Split at every exact polynomial breakpoint')
        return i

    def field(self,sI,leftQ,rightQ,order=0):
        if not isinstance(order,int) or order<0:
            raise ValueError('A nonnegative derivative order is required')
        i = self._index(self.xx,self.pc,leftQ,rightQ)
        c = self.pc[i]
        for _ in range(order):
            c = b.m.pder(c)
        x = I(sI)-I.rational(self.xx[i])
        c1,c2 = b.m.pder(c),b.m.pder(b.m.pder(c))
        return b.D2(_poly(c,x,self.n)*self.q,_poly(c1,x,self.n)*self.q,
                    _poly(c2,x,self.n)*self.q)

    def chart(self,sI,leftQ,rightQ):
        i = self._index(self.spx,self.ec,leftQ,rightQ)
        c = self.ec[i]
        x = I(sI)-I.rational(self.spx[i])
        values = []
        for _ in range(4):
            values.append(_poly(c,x));c = b.m.pder(c)
        return b.D2(*values[:3]),b.D2(*values[1:4])

    def profile(self,sI,leftQ,rightQ):
        left,right,mid = self._domain(leftQ,rightQ)
        if mid==self.entry:
            return b.D2(1,0,0),b.D2(0,0,0)
        i = max(0,bisect_right(self.profile_starts,mid)-1)
        p = self.profile_pieces[i]
        if left<p['left'] or right>p['right']:
            raise ValueError('Split at every exact profile breakpoint')
        x = I(sI)-I.rational(p['center'])
        values = [_poly(c,x) for c in p['centered_derivatives']]
        return b.D2(*values[:3]),b.D2(*values[1:4])

    def lift(self,sI,leftQ,rightQ):
        left,right,_ = self._domain(leftQ,rightQ)
        if right<=self.lift_lo:
            return b.D2(1,0,0),b.D2(0,0,0)
        if left>=self.lift_hi:
            return b.D2(0,0,0),b.D2(0,0,0)
        if left<self.lift_lo or right>self.lift_hi:
            raise ValueError('Split at the exact lift cutoff points')
        u = (I(sI)-I.rational(self.lift_lo))/I.rational(self.lift_hi-self.lift_lo)
        values = [_poly(c,u) for c in self.lift_derivatives]
        return b.D2(*values[:3]),b.D2(*values[1:4])

    def exact_endpoint_report(self):
        """Only exact endpoint algebra; no mean integral or metric certificate."""
        field_count = 0
        for i,rows in self.field_coefficients_exact.items():
            h = self.xx[i+1]-self.xx[i]
            for j,pp in enumerate(rows):
                got = [qval(pp,h),qval(qder(pp),h),qval(qder(qder(pp)),h)]
                if got!=self.field_right_targets_exact[i][j]:
                    raise ArithmeticError('Shared field endpoint mismatch')
                field_count += 1
        for i,pp in self.chart_coefficients_exact.items():
            h = self.spx[i+1]-self.spx[i]
            got = [qval(pp,h),qval(qder(pp),h),qval(qder(qder(pp)),h)]
            if got!=self.chart_right_targets_exact[i]:
                raise ArithmeticError('Shared chart endpoint mismatch')
        def jets(piece,at):
            u = (at-piece['origin'])/piece['length'];c = piece['coefficients_exact']
            out = []
            for k in range(4):
                out.append(qval(c,u)/piece['length']**k);c = qder(c)
            return out
        for left,right in zip(self.profile_pieces[:-1],self.profile_pieces[1:]):
            if left['right']!=right['left'] or jets(left,left['right'])!=jets(right,right['left']):
                raise ArithmeticError('Exact profile jets through order three do not join')
        if jets(self.profile_pieces[0],Q(0))!=[1,0,0,0] or jets(self.profile_pieces[-1],self.entry)!=[1,0,0,0]:
            raise ArithmeticError('Exact profile endpoint normalization failed')
        chi = self.lift_coefficients_exact
        for at,target in ((Q(0),[1,0,0]),(Q(1),[0,0,0])):
            got = [qval(chi,at),qval(qder(chi),at),qval(qder(qder(chi)),at)]
            if got!=target:
                raise ArithmeticError('Lift common two-jet mismatch')
        return dict(status='exact_endpoint_algebra_passed',field_scalar_pieces=field_count,
            field_pieces=len(self.pc),chart_pieces=len(self.ec),profile_pieces=len(self.profile_pieces),
            grid_intervals=len(self.grid)-1,entry_exact=str(self.entry),end_exact=str(self.end),
            amplitude_ratio_exact=str(self.amplitude_ratio),duration_ratio_exact=str(self.duration_ratio),
            velocity_ratio_exact=str(self.velocity_ratio),field_and_chart_common_jet_order=2,
            profile_common_jet_order=3,lift_common_jet_order=2,
            mathematical_mean_or_metric_certificate_executed=False)
