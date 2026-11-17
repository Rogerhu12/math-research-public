#!/usr/bin/env python3
"""Sharp outward integration of the SAME frozen R21 physical background.

Ordinary A and AH are total variations of w/sqrt(1+w^2) and
-1/sqrt(1+w^2).  A panel with certified monotonicity therefore has an
endpoint formula.  Unresolved turning panels use a complete derivative
range, with adaptive subdivision.  B and BH, and the exceptional outer
piece, use Simpson's rule with an interval fourth-derivative remainder.

The retained branchwise cap is C4.  Interval Taylor coefficients are
enclosed over every panel, including every eligible branch at a cap
crossing.  All fixed binary input constants are imported as exact
rationals.  No source quadrature value is used as a certified integral.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import heapq
import json
import math
import time

import mpmath as mp


mp.mp.dps = 90
iv = mp.iv
iv.dps = 60


def lower(z):
    return mp.make_mpf(z._mpi_[0])


def upper(z):
    return mp.make_mpf(z._mpi_[1])


def interval(lo, hi):
    assert lo <= hi
    return iv.mpf([lo, hi])


def q(x):
    f = Fraction(x) if isinstance(x, int) else Fraction.from_float(float(x))
    return iv.mpf(f.numerator) / f.denominator


def hull(xs):
    return interval(min(lower(v) for v in xs), max(upper(v) for v in xs))


def absmax(x):
    return max(abs(lower(x)), abs(upper(x)))


def nonnegative(x):
    assert upper(x) >= 0
    return interval(max(mp.mpf(0), lower(x)), upper(x))


class Jet:
    """Taylor coefficients f^(j)/j!, with interval arithmetic throughout."""

    def __init__(self, coefficients):
        self.c = list(coefficients)
        self.n = len(self.c) - 1

    @classmethod
    def constant(cls, x, n):
        return cls([x if hasattr(x, '_mpi_') else iv.mpf(x)] + [iv.mpf(0)] * n)

    @classmethod
    def variable(cls, x, n):
        return cls([x] + ([iv.mpf(1)] + [iv.mpf(0)] * (n - 1) if n else []))

    def coerce(self, other):
        if isinstance(other, Jet):
            assert self.n == other.n
            return other
        return Jet.constant(other, self.n)

    def __add__(self, other):
        other = self.coerce(other)
        return Jet([a + b for a, b in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return Jet([-a for a in self.c])

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        return Jet([sum((self.c[k] * other.c[j-k] for k in range(j+1)), iv.mpf(0))
                    for j in range(self.n+1)])

    __rmul__ = __mul__

    def inverse(self):
        assert not (lower(self.c[0]) <= 0 <= upper(self.c[0]))
        b = [1 / self.c[0]]
        for j in range(1, self.n+1):
            b.append(-sum((self.c[k] * b[j-k] for k in range(1, j+1)), iv.mpf(0)) / self.c[0])
        return Jet(b)

    def __truediv__(self, other):
        return self * self.coerce(other).inverse()

    def __rtruediv__(self, other):
        return self.coerce(other) * self.inverse()

    def exp(self):
        b = [iv.exp(self.c[0])]
        for j in range(1, self.n+1):
            b.append(sum((k * self.c[k] * b[j-k] for k in range(1, j+1)), iv.mpf(0)) / j)
        return Jet(b)

    def sqrt(self):
        assert lower(self.c[0]) > 0
        b = [iv.sqrt(self.c[0])]
        for j in range(1, self.n+1):
            b.append((self.c[j] - sum((b[k] * b[j-k] for k in range(1, j)), iv.mpf(0))) / (2*b[0]))
        return Jet(b)


def smooth(x):
    value = x*x*x*(10+x*(-15+6*x))
    # The input here is the original interval variable in [0,1].  S5 is
    # monotone, so tighten only its value enclosure; derivative coefficients
    # still come from the same polynomial and retain their full intervals.
    lo, hi = lower(x.c[0]), upper(x.c[0])
    assert 0 <= lo <= hi <= 1
    vals = [iv.mpf(t)**3*(10+iv.mpf(t)*(-15+6*iv.mpf(t))) for t in (lo,hi)]
    value.c[0] = interval(max(mp.mpf(0),lower(vals[0])),min(mp.mpf(1),upper(vals[1])))
    if x.n:
        assert lower(x.c[1]) == upper(x.c[1]) == 1
        assert all(lower(z) == upper(z) == 0 for z in x.c[2:])
        # S5' has one maximum at 1/2. Its factored expression avoids
        # cancellation that would obscure the sign near either endpoint.
        dvals = [30*iv.mpf(t)**2*(1-iv.mpf(t))**2 for t in (lo,hi)]
        if lo <= mp.mpf('.5') <= hi:
            dvals.append(iv.mpf(15)/8)
        value.c[1] = hull(dvals)
    return value


def capped(z, cap, transition):
    rel = z - cap
    pieces = []
    if lower(rel.c[0]) <= -lower(transition):
        pieces.append(z)
    if upper(rel.c[0]) >= lower(transition):
        pieces.append(cap)
    if upper(rel.c[0]) >= -upper(transition) and lower(rel.c[0]) <= upper(transition):
        # Restrict the VALUE to this branch's t in [0,1], retaining every
        # derivative coefficient of t(x).  This is a range intersection on
        # the branch domain, not differentiation of a clamped function.
        t = (rel+transition)/(2*transition)
        t.c[0] = interval(max(mp.mpf(0),lower(t.c[0])),min(mp.mpf(1),upper(t.c[0])))
        t2 = t*t
        t4 = t2*t2
        primitive = t-t4*t*(7+t*(-14+t*(10-t*q(2.5))))
        branch = cap-transition+primitive*(2*transition)
        if z.n:
            # I'=1-S7 decreases from 1 to 0.  The first derivative
            # D*z'+(1-D)*cap' retains this exact positive convex form.
            def dprimitive(u):
                return (1-u)**4*(1+u*(4+u*(10+20*u)))
            ds = [dprimitive(iv.mpf(v)) for v in (lower(t.c[0]),upper(t.c[0]))]
            d = interval(max(mp.mpf(0),lower(ds[1])),min(mp.mpf(1),upper(ds[0])))
            branch.c[1] = d*z.c[1]+(1-d)*cap.c[1]
        pieces.append(branch)
    assert pieces
    result = Jet([hull([v.c[j] for v in pieces]) for j in range(z.n+1)])
    # The cap is no larger than either z or cap and never smaller than
    # min(z,cap-L); these bounds hold across all eligible branches.
    result.c[0] = interval(max(lower(result.c[0]),min(lower(z.c[0]),lower((cap-transition).c[0]))),
                           min(upper(result.c[0]),upper(z.c[0]),upper(cap.c[0])))
    return result


class Background:
    def __init__(self, data, cells):
        self.data = data
        self.cfg = cfg = data['parameters']
        assert 16 <= cells < 160 and cfg['protectCell'] == 160
        assert cfg['orientation'] == 1 and cfg['curvatureBound'] == 8
        assert cfg['prefixEnd'] == 15 and cfg['rejoinR20At'] is None
        assert not cfg.get('flatOuterThroughCell', False)
        assert cfg['a'] == 2.75 and cfg['etaPower'] == 1.5
        assert all(v['lengthScale'] == 1 for v in data['cells'])
        assert all(.5 <= v['calibrationAlpha'] <= 2 for v in data['cells'])
        assert all(v == 0 for v in cfg['valleyControls'][16:])
        assert all(all(v == 1 for v in z) for z in cfg.get('warpWeightLevels', [])[1:])
        assert len(cfg.get('pulseCaps', [])) <= 1 and len(cfg.get('valleyCaps', [])) <= 1
        assert all(v['R'] == 64 for v in data['cells'][16:])
        self.delta0, self.c0 = q(cfg['delta0']), q(cfg['etaRatioAtN0'])
        self.eta0 = self.delta0*self.c0
        self.aa, self.cut = q(cfg['rCuff']), q(cfg['rCut'])
        self.wcut, self.ae = q(cfg['wCut']), q(cfg['a'])
        self.L, self.sqrt12 = q(cfg['capTransition']), iv.sqrt(12)
        self.two = iv.mpf(2)
        self.eta_ratio = self.two**(-q(1.5))
        self.Y = 6*self.delta0+6*self.eta0/(1-self.eta_ratio)
        self.oldcut = self.aa*iv.exp(self.Y/self.sqrt12)

    def pieces(self, n):
        cfg = self.cfg
        cell = self.data['cells'][n]
        delta = self.delta0*self.two**(-n)
        c = self.c0*self.two**(-iv.mpf(n)/2)
        after = 3*self.delta0*self.two**(-n)+6*self.eta0*self.two**(-q(1.5)*(n+1))/(1-self.eta_ratio)
        ld = iv.ln(delta)
        values = [ld, iv.ln(q(cell['R'])), 2*ld-iv.ln(q(cell['calibrationAlpha'])),
                  iv.mpf(0), ld+self.ae*iv.ln(2)]
        beta = q(cfg['valleyControls'][n])
        levels = [q(cfg['slopeCap'])]*5
        if n < len(cfg.get('pulseCaps', [])):
            levels[1], levels[3] = [q(v) for v in cfg['pulseCaps'][n]]
        if n < len(cfg.get('valleyCaps', [])):
            levels[2] = q(cfg['valleyCaps'][n])
        weights = cfg.get('warpWeightLevels', [])
        weights = [q(v) for v in weights[n]] if n < len(weights) else [iv.mpf(1)]*5
        offset = iv.mpf(0)
        base = iv.ln(self.wcut)-self.ae*iv.ln(2*self.delta0)+(self.ae-1)*ld
        for j in range(9):
            transition = j % 2 == 1
            k = (j-1)//2 if transition else j//2
            length = delta*(c if transition or j in (0,8) else 1)
            params = dict(n=n, j=j, transition=transition, k=k, length=length,
                          after=after, offset=offset, base=base, beta=beta,
                          v0=values[k], vdiff=values[k+1]-values[k] if transition else iv.mpf(0),
                          cap0=iv.ln(levels[k]),
                          capdiff=iv.ln(levels[k+1]/levels[k]) if transition else iv.mpf(0),
                          weight0=weights[k],
                          weightdiff=iv.ln(weights[k+1]/weights[k]) if transition else iv.mpf(0))
            yield Piece(self, params)
            offset += length

    def remainders(self, N):
        W = 256*self.two**(-iv.mpf(7*N)/4)
        HN = 17+iv.mpf(7*N)/5
        qq = iv.mpf(3)/10
        TV = W*((4*HN+1)/(1-qq)+(iv.mpf(28)/5)*qq/(1-qq)**2)
        Yrest = 6*self.delta0*self.two**(-N)+6*self.eta0*self.two**(-q(1.5)*N)/(1-self.eta_ratio)
        radial_rest = self.aa*iv.expm1(Yrest/self.sqrt12)
        Arest, Brest = TV/8+radial_rest, radial_rest
        return [Arest, Brest, W*Arest, W*Brest]


class Piece:
    def __init__(self, background, parameters):
        self.bg, self.p = background, parameters
        self.point_cache = {}
        self.evaluations = 0
        self.minimum_panel_width = mp.mpf(1)

    def evaluate(self, x, order):
        self.evaluations += 1
        bg, p = self.bg, self.p
        x = Jet.variable(x, order)
        S = smooth(x)
        logp = S*p['vdiff']+p['v0']
        rawz = logp+p['base']+7*(-x*p['length']+bg.Y-p['after']-p['offset'])/bg.sqrt12
        if p['j'] == 3:
            rawz += S*p['beta']
        elif p['j'] == 4:
            rawz += p['beta']
        elif p['j'] == 5:
            rawz += (1-S)*p['beta']
        caplog = S*p['capdiff']+p['cap0']
        z = capped(rawz, caplog, bg.L)
        special = p['n'] == 0 and p['j'] == 8
        if special:
            z = rawz
        elif p['n'] == 0 and p['j'] == 7:
            z = rawz+(1-S)*(z-rawz)
        w = z.exp()
        E = 1+w*w
        r_old = ((x*p['length']+p['after']+p['offset'])/bg.sqrt12).exp()*bg.aa
        rx = r_old*p['length']/bg.sqrt12
        chi = 1-S if special else Jet.constant(1, order)
        weight = (S*p['weightdiff']).exp()*p['weight0']
        B = chi*rx/E*weight
        if special:
            j0 = 1+S*(bg.cut/bg.oldcut-1)
            # rawz is affine here, so -w_x = 7*length/sqrt(12)*w.
            A = rx*j0*S+chi*(7*p['length']/bg.sqrt12)*w/(8*E*E.sqrt())
            vals = [A, B, w*A, w*B]
        else:
            vals = [None, B, None, w*B]
        return w, vals

    def point(self, x):
        key = x._mpf_
        if key not in self.point_cache:
            w, vals = self.evaluate(iv.mpf(x), 0)
            w = w.c[0]
            E = 1+w*w
            self.point_cache[key] = (w/iv.sqrt(E), -1/iv.sqrt(E),
                                     [v.c[0] if v is not None else None for v in vals])
        return self.point_cache[key]

    def panel(self, left, right):
        width = right-left
        # With 90 decimal digits these dyadics, their sums, differences and
        # midpoints are exact.  An unexpectedly deep recursion must stop,
        # not silently use a rounded Simpson midpoint.
        assert mp.mp.prec > 256 and width >= mp.mpf(2)**(-128)
        self.minimum_panel_width = min(self.minimum_panel_width,width)
        mid = (left+right)/2
        w, vals = self.evaluate(interval(left, right), 4)
        a, m, b = self.point(left), self.point(mid), self.point(right)
        result = [None]*4
        for j in (1,3) if vals[0] is None else range(4):
            S = iv.mpf(width)/6*(a[2][j]+4*m[2][j]+b[2][j])
            # f'''' = 24*jet[4]; Simpson error <= h^5*f''''/2880.
            error = iv.mpf(width)**5*abs(vals[j].c[4])/120
            result[j] = nonnegative(S+interval(-upper(error), upper(error)))
        if vals[0] is None:
            if lower(w.c[1]) >= 0:
                result[0], result[2] = nonnegative((b[0]-a[0])/8), nonnegative((b[1]-a[1])/8)
            elif upper(w.c[1]) <= 0:
                result[0], result[2] = nonnegative((a[0]-b[0])/8), nonnegative((a[1]-b[1])/8)
            else:
                E = 1+w.c[0]*w.c[0]
                Aupper = iv.mpf(width)*abs(w.c[1])/(8*E*iv.sqrt(E))
                result[0] = interval(0, upper(Aupper))
                result[2] = interval(0, upper(Aupper*w.c[0]))
        return result

    def integrate(self, tolerance, max_panels):
        # Priority estimates only choose refinement; the returned enclosure
        # is an outward sum of all leaf enclosures, independent of estimates.
        serial = 0
        first = self.panel(mp.mpf(0), mp.mpf(1))
        err = max(upper(v)-lower(v) for v in first)
        heap = [(-err, serial, mp.mpf(0), mp.mpf(1), first)]
        while True:
            largest = -heap[0][0]
            # Never subtract a formerly enormous cap-branch range from an
            # accumulated estimate: cancellation can leave a phantom error.
            # These conditions only decide when to sum the actual leaves.
            check = largest <= tolerance and (len(heap) % 32 == 0 or largest*len(heap) <= tolerance)
            if check or len(heap) >= max_panels:
                total = [sum((row[4][j] for row in heap), iv.mpf(0)) for j in range(4)]
                actual = max(upper(v)-lower(v) for v in total)
                if actual <= tolerance:
                    return total, len(heap)
                if len(heap) >= max_panels:
                    raise ArithmeticError(f'panel cap: {self.p["n"]}:{self.p["j"]}; width {actual}')
            _, _, left, right, _ = heapq.heappop(heap)
            mid = (left+right)/2
            for lo, hi in ((left,mid),(mid,right)):
                vals = self.panel(lo,hi)
                err = max(upper(v)-lower(v) for v in vals)
                serial += 1
                heapq.heappush(heap,(-err,serial,lo,hi,vals))


def bound(z):
    lo = math.nextafter(float(lower(z)), -math.inf)
    hi = math.nextafter(float(upper(z)), math.inf)
    return dict(lower=lo, upper=hi, lower_exact=str(Fraction.from_float(lo)),
                upper_exact=str(Fraction.from_float(hi)),
                interval_lower=str(lower(z)), interval_upper=str(upper(z)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--cells',type=int,default=48)
    parser.add_argument('--piece-width',default='1e-17')
    parser.add_argument('--max-panels',type=int,default=65536)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    bg = Background(data,args.cells)
    tolerance = mp.mpf(args.piece_width)
    assert tolerance > 0
    started = time.monotonic()
    rows, counts = [], []
    for n in range(args.cells):
        cell, stats = [iv.mpf(0)]*4, []
        for piece in bg.pieces(n):
            vals, panels = piece.integrate(tolerance,args.max_panels)
            cell = [a+b for a,b in zip(cell,vals)]
            stats.append(dict(piece=piece.p['j'],panels=panels,evaluations=piece.evaluations,
                              maximum_dyadic_depth=-piece.minimum_panel_width._mpf_[2],
                              widths=[str(upper(v)-lower(v)) for v in vals]))
            print(json.dumps(dict(cell=n,piece=piece.p['j'],panels=panels,
                                  seconds=time.monotonic()-started)),flush=True)
        rows.append(cell)
        counts.append(stats)
        print(json.dumps(dict(cell=n,A=[float(lower(cell[0])),float(upper(cell[0]))],
                              panels=sum(v['panels'] for v in stats),seconds=time.monotonic()-started)),flush=True)
    remainder = bg.remainders(args.cells)
    totals = [sum((row[j] for row in rows),iv.mpf(0)) for j in range(4)]
    complete = [interval(lower(z),upper(z+r)) for z,r in zip(totals,remainder)]
    Y160 = 6*bg.delta0*bg.two**(-160)+6*bg.eta0*bg.two**(-240)/(1-bg.eta_ratio)
    rdeep = bg.aa*iv.exp(Y160/bg.sqrt12)
    normalization = (bg.cut-rdeep-complete[0])/complete[1]
    assert lower(normalization)>0
    deep_height = 256*bg.two**(-280)*bg.aa*iv.expm1(Y160/bg.sqrt12)
    height = complete[2]+normalization*complete[3]+interval(0,upper(deep_height))
    inner = [sum((row[j] for row in rows[1:]),iv.mpf(0)) for j in range(4)]
    inner = [interval(lower(z),upper(z+r)) for z,r in zip(inner,remainder)]
    r1 = rdeep+inner[0]+normalization*inner[1]
    result = dict(scope=__doc__,input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  cells=args.cells,piece_width=args.piece_width,interval_decimal_precision=iv.dps,
                  complete_integrals={k:bound(v) for k,v in zip(['A','B','AH','BH'],complete)},
                  positive_exact_normalization=bound(normalization),exact_background_height=bound(height),
                  cell0_inner_radius=bound(r1),
                  analytic_deep_remainder={k:bound(v) for k,v in zip(['A','B','AH','BH'],remainder)},
                  cell_integrals=[{k:bound(v) for k,v in zip(['A','B','AH','BH'],row)} for row in rows],
                  adaptive_counts=counts,seconds=time.monotonic()-started,
                  nonrotational_metric_certified=False)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(alpha=result['positive_exact_normalization'],
                          height=result['exact_background_height'],seconds=result['seconds'])),flush=True)


if __name__ == '__main__':
    main()
