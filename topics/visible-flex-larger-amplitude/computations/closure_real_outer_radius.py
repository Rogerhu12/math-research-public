#!/usr/bin/env python3
"""Enclose the true outer radius of R26's fixed real source metric.

Cells 0..11 retain every frozen valley control, slope-cap branch, endpoint
blend, chi, captured oldCut and positive warp weight. Cap branches and signs
of the slope derivative are certified on real dyadic panels. Analytic panels
use Arb/Acb integration; unresolved boundary strips use interval range times
length. No binary quadrature is reused as a mathematical integral, and the
frozen warp alpha is never recalibrated to force the radius to nominal rCut.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import acb, arb, ctx
from closure_real_head_source_enclosure import RealHead, exact_q, ball_record, power2


def smooth(x):
    return x*x*x*(10+x*(-15+6*x))


def dsmooth(x):
    return 30*x*x*(1-x)*(1-x)


def cap_integral(t):
    return t**5*(7+t*(-14+t*(10-arb(5)*t/2)))


def cap_derivative(t):
    return t**4*(35+t*(-84+t*(70-20*t)))


class OuterCell:
    def __init__(self, head, n, guard_bits=100):
        self.head, self.n, self.p = head, n, head.params
        p = self.p
        if p.get('flatOuterThroughCell') is not None or p.get('rejoinR20At') is not None:
            raise ValueError('This expression covers the present unflattened, unrejoined source')
        if p['orientation'] != 1 or p['capMode'] != 'cut-preserving':
            raise ValueError('This expression requires the recorded outward cut-preserving source')
        if p['capTransition'] != 2 or p['curvatureBound'] != 8:
            raise ValueError('Unexpected cap transition or curvature redistribution')
        self.guard_width = Q(1, 2**guard_bits)
        delta = head.d0*power2(-n)
        c = head.c0*(-arb(n)*head.log2/2).exp()
        mu = head.eps_phys*(head.a*delta.log()).exp()
        q32 = (-arb(3)*head.log2/2).exp()
        after = 3*delta+6*head.c0*head.d0*q32**(n+1)/(1-q32)
        log_r = head.rc.log()+after/head.sqrt12
        row = head.data[n]
        logs = [arb(0), exact_q(row['R']).log()-delta.log(),
                delta.log()-exact_q(row['alpha']).log(), -delta.log(),
                head.a*head.log2]
        pieces = [(0,0,c),(0,1,c),(1,1,arb(1)),(1,2,c),(2,2,arb(1)),
                  (2,3,c),(3,3,arb(1)),(3,4,c),(4,4,c)]
        offset = arb(0); self.segments = []
        for j, (lo, hi, ratio) in enumerate(pieces):
            length = delta*ratio
            self.segments.append(dict(j=j, length=length,
                log_r0=log_r+offset/head.sqrt12,
                log_w0=mu.log()+logs[lo]-7*(log_r+offset/head.sqrt12),
                jump=logs[hi]-logs[lo], transition=lo!=hi))
            offset += length
        self.beta = exact_q((p.get('valleyControls', [])+[0]*12)[n])
        base_cap = p['slopeCap']
        pulse = p.get('pulseCaps', [])
        pulse = pulse[n] if n < len(pulse) and pulse[n] is not None else [base_cap,base_cap]
        valley = p.get('valleyCaps', [])
        valley = valley[n] if n < len(valley) and valley[n] is not None else base_cap
        self.cap_values = [base_cap,pulse[0],valley,pulse[1],base_cap]
        self.caps = [exact_q(v).log() for v in self.cap_values]
        weights = p.get('warpWeightLevels', [])
        weights = weights[n] if n < len(weights) and weights[n] is not None else [1]*5
        if len(weights) != 5 or weights[0] != 1 or weights[-1] != 1 or min(weights) <= 0:
            raise ValueError('Unexpected positive warp weights')
        self.weight_values = weights
        self.weights = [exact_q(v).log() for v in weights]
        self.integration_count = 0

    def raw_cap(self, seg, x):
        j = seg['j']; s = smooth(x); ds = dsmooth(x)
        v, dv = ((s, ds) if j == 3 else (1, 0) if j == 4 else
                 (1-s, -ds) if j == 5 else (0, 0))
        raw = seg['log_w0']-7*seg['length']*x/self.head.sqrt12+self.beta*v
        derivative = -7*seg['length']/self.head.sqrt12+self.beta*dv
        if seg['transition']:
            raw += seg['jump']*s; derivative += seg['jump']*ds
        if j % 2 == 0:
            cap, dcap = self.caps[j//2], arb(0)
        else:
            first = (j-1)//2
            # Identical dyadic cap levels have exactly zero log ratio. Do not
            # subtract two enclosures of the same logarithm and manufacture
            # derivative uncertainty on a genuinely constant cap plateau.
            jump = (arb(0) if self.cap_values[first+1] == self.cap_values[first]
                    else (exact_q(self.cap_values[first+1])/exact_q(self.cap_values[first])).log())
            cap = self.caps[first]+jump*s; dcap = jump*ds
        return raw, derivative, cap, dcap

    def profile(self, seg, x, branch):
        raw, derivative, cap, dcap = self.raw_cap(seg, x)
        if branch == 'raw' or (self.n == 0 and seg['j'] == 8):
            g, dg = raw, derivative
        elif branch == 'cap':
            g, dg = cap, dcap
        elif branch in ('transition-low', 'transition-high'):
            L = exact_q(self.p['capTransition'])
            if branch == 'transition-low':
                t = (raw-cap+L)/(2*L)
                g = raw-2*L*cap_integral(t)
                dg = derivative-cap_derivative(t)*(derivative-dcap)
            else:
                # Exact polynomial identities from the pinned source's two
                # endpoint formulas avoid 1-S(t) cancellation at t=1.
                u = (cap+L-raw)/(2*L)
                g = cap-2*L*cap_integral(u)
                dg = dcap+cap_derivative(u)*(derivative-dcap)
        else:
            raise ValueError(branch)
        if self.n == 0 and seg['j'] == 7:
            eta = 1-smooth(x)
            g, dg = (raw+eta*(g-raw),
                     derivative+eta*(dg-derivative)-dsmooth(x)*(g-raw))
        return g, dg

    def classify(self, seg, lo, hi):
        interval = exact_q(lo).union(exact_q(hi))
        raw, _, cap, _ = self.raw_cap(seg, interval)
        z = raw-cap; L = exact_q(self.p['capTransition'])
        if self.n == 0 and seg['j'] == 8:
            branch = 'raw'
        elif z <= -L:
            branch = 'raw'
        elif z >= L:
            branch = 'cap'
        elif z >= -L and z <= L:
            if z <= 0:
                branch = 'transition-low'
            elif z >= 0:
                branch = 'transition-high'
            else:
                return None
        else:
            return None
        _, derivative = self.profile(seg, interval, branch)
        if derivative > 0:
            return branch, 1
        if derivative < 0:
            return branch, -1
        if derivative == 0:
            return branch, 0
        return None

    def integrand(self, seg, x, branch, sign, analytic=False):
        logw, logw_x = self.profile(seg, x, branch)
        w = logw.exp(); E = 1+w*w
        ro = (seg['log_r0']+seg['length']*x/self.head.sqrt12).exp()
        rx = seg['length']*ro/self.head.sqrt12
        j = seg['j']; s = smooth(x)
        if self.n == 0 and j == 8:
            chi = 1-s
            j0 = 1+(exact_q(self.p['rCut'])/exact_q(self.p['oldCut'])-1)*s
        else:
            chi, j0 = 1, 1
        if j % 2 == 0:
            log_weight = self.weights[j//2]
        else:
            first = (j-1)//2
            jump = (arb(0) if self.weight_values[first+1] == self.weight_values[first]
                    else (exact_q(self.weight_values[first+1])/exact_q(self.weight_values[first])).log())
            log_weight = self.weights[first]+jump*s
        if isinstance(E, acb):
            root = E.sqrt(analytic=analytic)
        else:
            root = E.sqrt()
        magnitude = abs(logw_x) if sign is None else sign*logw_x
        return (rx*j0*(1-chi)+chi*w*magnitude/(8*E*root)+
                self.head.alpha*chi*rx*log_weight.exp()/E)

    def partition(self, seg):
        pending = [(Q(0), Q(1))]; pieces = []; visited = 0
        while pending:
            visited += 1
            if visited > 30000:
                raise ArithmeticError('Certified panel budget exceeded; no integral was accepted')
            lo, hi = pending.pop(); kind = self.classify(seg, lo, hi)
            bounded_strip = False
            if kind is None and hi-lo <= Q(1,128):
                value = self.range_integral(seg, lo, hi)
                bounded_strip = (value.is_finite() and
                                 value.upper()-value.lower() <= power2(-100))
            if kind is None and hi-lo > self.guard_width and not bounded_strip:
                middle = (lo+hi)/2
                pending.extend([(middle,hi),(lo,middle)])
            else:
                if pieces and pieces[-1][1] == lo and pieces[-1][2] == kind:
                    pieces[-1] = pieces[-1][0], hi, kind
                else:
                    pieces.append((lo,hi,kind))
        if pieces[0][0] != 0 or pieces[-1][1] != 1 or any(
                a[1] != b[0] for a,b in zip(pieces,pieces[1:])):
            raise AssertionError('Dyadic partition does not cover the full segment')
        return pieces

    def range_integral(self, seg, lo, hi):
        """Enclose an entire unresolved strip, retaining only possible branches.

        The width of this rigorous integral enclosure, rather than an arbitrary
        need to decide a near-zero derivative, may end the subdivision.
        """
        interval = exact_q(lo).union(exact_q(hi))
        raw, _, cap, _ = self.raw_cap(seg, interval)
        z = raw-cap; L = exact_q(self.p['capTransition'])
        if self.n == 0 and seg['j'] == 8:
            possible = ['raw']
        else:
            possible = []
            if not z > -L:
                possible.append('raw')
            if not z < L:
                possible.append('cap')
            if not (z < -L or z > L):
                if not z > 0:
                    possible.append('transition-low')
                if not z < 0:
                    possible.append('transition-high')
        if not possible:
            raise AssertionError('No real cap branch remains')
        values = [self.integrand(seg, interval, branch, None) for branch in possible]
        box = values[0]
        for value in values[1:]:
            box = box.union(value)
        return box*exact_q(hi-lo)

    def segment_width(self, seg):
        parts = self.partition(seg); total = arb(0); unknown = arb(0); records = []
        for lo, hi, kind in parts:
            interval = exact_q(lo).union(exact_q(hi))
            if kind is None:
                # Each actual branch is included, including its full derivative.
                # This interval remainder covers branch/critical boundaries.
                enclosure = self.range_integral(seg, lo, hi)
                unknown += enclosure
                method = 'real interval range times exact strip width'
            else:
                branch, sign = kind
                middle = exact_q((lo+hi)/2)
                scale = arb(abs(self.integrand(seg, middle, branch, sign)).upper())
                if not scale > 0:
                    raise ArithmeticError('No positive integrand scale')
                def f(z, analytic):
                    return self.integrand(seg, z, branch, sign, analytic)/scale
                value = acb.integral(f, acb(exact_q(lo)), acb(exact_q(hi)),
                    rel_tol=power2(-96), abs_tol=power2(-116),
                    deg_limit=64, eval_limit=100000, depth_limit=40)
                self.integration_count += 1
                if not value.is_finite() or not value.imag.contains(0):
                    raise ArithmeticError(f'Integral failed for cell{self.n} segment{seg["j"]}')
                enclosure = scale*value.real
                method = 'rigorous analytic Arb/Acb integral'
            if not enclosure.is_finite():
                raise ArithmeticError('Nonfinite radius contribution')
            total += enclosure
            records.append(dict(left=str(lo),right=str(hi),branch_sign=kind,
                                method=method,width=ball_record(enclosure)))
        if not total > 0:
            raise ArithmeticError('Physical width not strictly positive')
        return dict(segment=seg['j'],width=ball_record(total),panels=records,
                    boundary_strip_contribution=ball_record(unknown)), total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ready', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--precision', type=int, default=192)
    parser.add_argument('--guard-bits', type=int, default=100)
    parser.add_argument('--cells', type=int, nargs='+')
    args = parser.parse_args(); ctx.prec = args.precision
    started = time.monotonic(); ready = json.loads(args.ready.read_text())
    head = RealHead(ready, start=12, far=96, exact_through=23)
    selected = list(range(11,-1,-1)) if args.cells is None else args.cells
    if any(n < 0 or n > 11 for n in selected) or len(set(selected)) != len(selected):
        raise ValueError('Unique shallow cells 0..11 required')
    result = dict(scope=__doc__, status='running', ready=str(args.ready),
                  ready_sha256=hashlib.sha256(args.ready.read_bytes()).hexdigest(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  real_head_source_sha256=hashlib.sha256(Path(__file__).with_name(
                      'closure_real_head_source_enclosure.py').read_bytes()).hexdigest(),
                  precision_bits=args.precision,guard_bits=args.guard_bits,
                  node12=ball_record(head.node_radii[12]),cells=[],
                  complete_outer_radius=False, frozen_alpha=ball_record(head.alpha),
                  binary_quadrature_reused=False, warp_alpha_recalibrated=False)
    total = head.node_radii[12]
    for n in selected:
        cell = OuterCell(head,n,args.guard_bits); rows=[]; width=arb(0)
        for segment in cell.segments:
            record,part=cell.segment_width(segment);rows.append(record);width+=part
        total += width
        result['cells'].append(dict(cell=n,width=ball_record(width),segments=rows,
                                    analytic_integrals=cell.integration_count))
        result.update(seconds=time.monotonic()-started,
                      peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        args.out.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(dict(event='real_outer_cell',cell=n,width=str(width),
                             seconds=result['seconds'],rss_kib=result['peak_rss_kib'])),flush=True)
    if set(selected) == set(range(12)):
        result.update(complete_outer_radius=True,outer_radius=ball_record(total),
                      outer_radius_minus_nominal=ball_record(total-exact_q(head.params['rCut'])))
    result.update(status='complete',seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='real_outer_complete',complete=result['complete_outer_radius'],
                         seconds=result['seconds'])),flush=True)


if __name__ == '__main__':
    main()
