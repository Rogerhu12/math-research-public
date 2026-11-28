"""The unchanged exact frozen target radius for the NEW Cartesian verifier.

This profile-only adapter builds no field or mean. Prefix normalization and
bridge Taylor enclosures are the existing exact definitions. The terminal
Hermite correction uses the UNIQUE true bridge endpoint jet; enclosing its
coefficients never chooses interval midpoints or changes the target metric.
"""
from bisect import bisect_right
from fractions import Fraction as Q
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path.insert(0, str(SCRIPTS/'resume_m3'))
sys.path.insert(0, str(SCRIPTS/'resume_20261126'))
import certify_bridge_metric_fourier_taylor as b
import seam_m3_prefix_pieces as pieces
import seam_certify_true_cut_height as height
import seam_bridge_endpoint_primitive as primitive
import seam_bridge_cut_trace as cut
from warm_certify_bridge_geometry import HERMITE

I = b.I


def fq(value):
    return Q.from_float(float(value))


class FrozenTarget:
    def __init__(self, flow, record):
        self.f = flow
        self.entry, self.end = fq(flow.prefix_end), fq(flow.end)
        self.spec = flow.cfg['multistage_flat']
        if (flow.base_mode != 3 or self.spec != record['frozen_profile']['multistage_flat']
                or fq(flow.delta) != fq(record['frozen_profile']['delta'])
                or flow.cfg['prefix_bridge'] != dict(kind='turn_plateau_v1', curvature=4, peak_fraction=.2)):
            raise ValueError('Use the actual unchanged complete frozen profile')
        eta = Q(self.spec['eta'])
        amplitude = fq(flow.delta)/Q(self.spec['reference_delta'])
        reference, time, area = [], Q(0), Q(0)
        for name in ('up', 'down'):
            for row in self.spec[name]:
                v0, v1, length = map(Q, row)
                reference.append((time, length, v0, v1, area))
                area += length*(v0+v1)/2
                time += length
        if area != 0 or reference[0][2] != 0 or reference[-1][3] != 0:
            raise ValueError('The exact original prefix must return with zero slope')
        duration = self.entry/time
        self.prefix_pieces = []
        turns = pieces._turn_polynomials(eta)
        for start, length0, v0, v1, old_area in reference:
            origin, length = duration*start, duration*length0
            dv = v1-v0
            zones = [(Q(0), Q(1), [Q(0)])] if dv == 0 else [
                (Q(0), eta, turns[0]), (eta, 1-eta, turns[1]), (1-eta, Q(1), turns[2])]
            for left, right, turn in zones:
                aa = [Q(1)+amplitude*old_area, amplitude*length0*v0]
                pieces._add_scaled(aa, turn, amplitude*length0*dv)
                pl, pr = origin+length*left, origin+length*right
                center, uc = (pl+pr)/2, ((pl+pr)/2-origin)/length
                centered = [sum((aa[k]*math.comb(k,j)*uc**(k-j)
                                  for k in range(j,len(aa))), Q(0))/length**j
                            for j in range(len(aa))]
                back = [sum((centered[k]*math.comb(k,j)*(origin-center)**(k-j)
                             for k in range(j,len(centered))), Q(0))*length**j
                        for j in range(len(centered))]
                if back != aa:
                    raise ArithmeticError('Exact original prefix polynomial identity failed')
                derivatives = [centered]
                for _ in range(3):
                    derivatives.append(pieces.qder(derivatives[-1]))
                self.prefix_pieces.append(dict(left=pl, right=pr, center=center,
                    derivatives=[[I.rational(x) for x in row] for row in derivatives]))
        self.prefix_starts = [row['left'] for row in self.prefix_pieces]
        bridge = flow.bridge
        self.peak, self.eps, self.L1, self.L2, self.L3 = map(
            fq, (bridge.peak, bridge.eps, bridge.L1, bridge.L2, bridge.L3))
        if not (bridge.astart == 1. and 0 < self.eps < self.peak < 2
                and min(self.L1, self.L2, self.L3) > 0):
            raise ValueError('The actual true bridge phase is outside its analytic scope')
        first = primitive.sin_polynomial([Q(0), Q(0), 3*self.peak, -2*self.peak], 40)
        last = primitive.sin_polynomial([self.peak, Q(0), -self.eps], 40)
        self.first_integral = [I(0)]+[I.rational(x/(j+1)) for j,x in enumerate(first)]
        self.last_integral = [I(0)]+[I.rational(x/(j+1)) for j,x in enumerate(last)]
        self.drop1 = I.rational(self.L1)*height.ipoly(self.first_integral, I(1))
        self.plateau = I.rational(primitive.sin_polynomial([self.peak], 40)[0])
        self.bridge_remainder = self.peak**41/math.factorial(41)
        self.length = Q(1,1000)
        self.patch_start = self.end-self.length
        if not self.length < self.L3:
            raise ValueError('The same target correction must lie in the last bridge piece')
        Rc, w = map(fq, (record['physical_tail_parameters']['rCut'],
                         record['physical_tail_parameters']['wCut']))
        if Rc != fq(.3) or w != fq(.08) or fq(record['physical_tail_cut']['radius']) != Rc:
            raise ValueError('Use the declared unchanged R58 true-tail cut')
        wR, E = -7*w/Rc, 1+w*w
        exact, phase = cut.true_radius(primitive, bridge, self.end-self.entry)
        actual = [I(I.rational(lo).x[0], I.rational(hi).x[1]) for lo,hi in exact]
        desired = [I.rational(Rc), -1/I.rational(E).sqrt(), I.rational(-w*wR/E**2)]
        self.delta = [x-y for x,y in zip(desired, actual)]
        for j, poly in enumerate(HERMITE):
            for k in range(3):
                if primitive.value(poly,Q(0)) != (1 if j == k else 0) or primitive.value(poly,Q(1)) != 0:
                    raise ArithmeticError('Exact target Hermite endpoint identity failed')
                poly = primitive.derivative(poly)
        self.grid = sorted(set([Q(0),self.entry,self.end,self.patch_start,
                                self.entry+self.L1,self.entry+self.L1+self.L2]
                               +[r[key] for r in self.prefix_pieces for key in ('left','right')]))
        if self.grid[0] != 0 or self.grid[-1] != self.end:
            raise ValueError('Target partition leaves the actual full prefix/bridge domain')
        self.definition = dict(metric='ds^2+a_hat(s)^2 dtheta^2',
            prefix='Original exact multistage amplitude profile, normalized to the literal prefix endpoint',
            prefix_end_exact=str(self.entry), end_exact=str(self.end),
            bridge='Unique true primitive of minus sine of the frozen literal ShortBridge phase, a(entry)=1',
            bridge_phase=phase, true_tail_R_exact=str(Rc), true_tail_w_exact=str(w),
            true_tail_wR_exact=str(wR), patch_length_exact=str(self.length),
            correction='sum_j (-L)^j h_j((end-s)/L) d_j on [end-L,end], zero elsewhere',
            endpoint_coefficients='Unique true-tail radius two-jet minus unique true bridge endpoint two-jet',
            coefficient_midpoints_chosen=False, independent_of_field_and_M=True)

    def correction(self, left, right, order):
        if right <= self.patch_start:
            return I(0)
        if not self.patch_start <= left <= right <= self.end:
            raise ValueError('Split the exact target correction join')
        u = I(I.rational((self.end-right)/self.length).x[0],
              I.rational((self.end-left)/self.length).x[1])
        value = I(0)
        for j, poly in enumerate(HERMITE):
            for _ in range(order):
                poly = primitive.derivative(poly)
            value += I.rational((-self.length)**j*(-1/self.length)**order)*height.ipoly(
                [I.rational(x) for x in poly],u)*self.delta[j]
        return value

    def jets(self, s, left, right):
        """Enclose a_hat and its first three derivatives on one exact piece."""
        if not 0 <= left <= right <= self.end:
            raise ValueError('Target query leaves its frozen physical domain')
        if right <= self.entry:
            if left == right == self.entry:
                return [I(1), I(0), I(0), I(0)]
            index = max(0,bisect_right(self.prefix_starts,(left+right)/2)-1)
            row = self.prefix_pieces[index]
            if not row['left'] <= left <= right <= row['right']:
                raise ValueError('Split every exact original profile breakpoint')
            x = s-I.rational(row['center'])
            return [height.ipoly(c,x) for c in row['derivatives']]
        if left < self.entry:
            raise ValueError('Split the prefix/bridge join')
        # The existing rigorous primitive enclosure keeps the analytic end
        # extension; it does not clip u to one or differentiate GL64 data.
        radius, _ = height.MeanMap.bridge(self,left,right)
        x = b.D2(s-I.rational(self.entry),1)
        first,last = left-self.entry,right-self.entry
        peak = b.D2(I.rational(self.peak))
        if last <= self.L1:
            u=x/I.rational(self.L1)
            phase=peak*(3*u*u-2*u*u*u)
        elif first >= self.L1 and last <= self.L1+self.L2:
            phase=peak
        elif first >= self.L1+self.L2:
            u=(x-I.rational(self.L1+self.L2))/I.rational(self.L3)
            phase=peak-u*u*I.rational(self.eps)
        else:
            raise ValueError('Split every true bridge phase join')
        sine,_=b.trig(phase)
        ap=-sine
        values=[radius,ap.v,ap.d,ap.d2]
        return [value+self.correction(left,right,k) for k,value in enumerate(values)]
