#!/usr/bin/env python3
"""Same-Hold scalar polynomial enclosures for complete-field Gram bounds.

Uses existing exact a boxes at the original nodes/midpoints as anchors.
No numerical a interpolation and no rerun of the old integral certificate.
Old pieces are the exact binary quintics.  Extension pieces use the exact
curvature law, a Taylor polynomial, and a complete Bell derivative bound.
"""
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path


class Scalar:
    def __init__(self, reader, scalar_input, degree=5):
        self.r, self.I = reader, reader.I
        self.degree = int(degree)
        if self.degree < 3:
            raise ValueError('Scalar Taylor degree must be at least three')
        self.path = Path(scalar_input).resolve()
        raw = self.path.read_bytes()
        self.input_sha = hashlib.sha256(raw).hexdigest()
        report = json.loads(reader.node_report_path.read_text())
        if self.input_sha != report['input_sha256']:
            raise ValueError('The scalar input is not the original same-Hold input')
        data = json.loads(gzip.decompress(raw))
        geometry = data['fixed_scalar_profile']['geometry']
        knots = geometry['knots']
        self.x = [F(float(k['s'])) for k in knots]
        jets = [tuple(F(float(k[v])) for v in ('a', 'ap', 'app')) for k in knots]
        law = geometry['initial_law']
        length, velocity, k0 = (F(float(law[k])) for k in ('length', 'velocity', 'k0'))
        s = self.x[0]; u = s/length
        b, c, d = k0*length, 3*velocity-2*k0*length, k0*length-2*velocity
        jets[0] = (1+length*(b*u*u/2+c*u**3/3+d*u**4/4),
                   b*u+c*u*u+d*u**3, (b+2*c*u+3*d*u*u)/length)
        self.old_power = []
        for j, (left, right) in enumerate(zip(jets, jets[1:])):
            h = self.x[j+1]-self.x[j]
            a0, a1, a2 = left[0], h*left[1], h*h*left[2]/2
            dy = right[0]-a0-a1-a2
            dv = h*right[1]-a1-2*a2
            da = h*h*right[2]-2*a2
            self.old_power.append([a0, a1, a2, 10*dy-4*dv+da/2,
                                   -15*dy+7*dv-da, 6*dy-3*dv+da/2])
        scalar = report['scalar']
        self.origin, self.cut = F(scalar['origin_exact']), F(scalar['cut_exact'])
        if self.origin != self.x[-1]:
            raise ValueError('Scalar origin must be the last exact stored knot')
        self.f, self.hold, self.rise, self.out = [F(v) for v in scalar['durations_exact']]
        self.kn, self.kp = F(-5, 2), F(3, 2)
        box = lambda d: reader.bounds(F(d['lower_exact']), F(d['upper_exact']))
        self.K, self.alpha_cut = box(scalar['K']), box(scalar['alpha_cut'])
        I = self.I; frac = reader.fraction
        self.A1 = I.sub(self.alpha_cut, I.mul(I.add(self.K, frac(self.kn)), frac(self.f/2)))
        self.A2 = I.sub(self.A1, frac(self.kn*self.hold))
        self.A3 = I.sub(self.A2, frac((self.kn+self.kp)*self.rise/2))
        pi = reader.bounds(F(reader.transform.pi_integer[0], reader.transform.F),
                           F(reader.transform.pi_integer[1], reader.transform.F))
        self.A4 = I.add(I.scale(pi, -.5), frac(self.kp*self.out/2))
        self.t1, self.t2, self.t3 = self.cut+self.f, self.cut+self.f+self.hold, self.cut+self.f+self.hold+self.rise
        # Exact segment endpoints are affine in the same exact S.
        self.segments = []
        for j in range(len(self.old_power)):
            self.segments.append(dict(left=(F(0), self.x[j]), right=(F(0), self.x[j+1]),
                                      kind='old_exact_quintic', old_index=j))
        self.segments += [
            dict(left=(F(0), self.origin), right=(F(0), self.cut), kind='constant',
                 angle=I.add(self.alpha_cut, I.mul(self.K, frac(self.cut-self.origin))), k=self.K),
            dict(left=(F(0), self.cut), right=(F(0), self.t1), kind='ramp',
                 angle=self.alpha_cut, kl=self.K, kr=frac(self.kn), width=self.f),
            dict(left=(F(0), self.t1), right=(F(0), self.t2), kind='constant', angle=self.A1, k=frac(self.kn)),
            dict(left=(F(0), self.t2), right=(F(0), self.t3), kind='ramp',
                 angle=self.A2, kl=frac(self.kn), kr=frac(self.kp), width=self.rise),
            dict(left=(F(0), self.t3), right=(F(1), -self.out), kind='constant', angle=self.A3, k=frac(self.kp)),
            dict(left=(F(1), -self.out), right=(F(1), F(0)), kind='ramp',
                 angle=self.A4, kl=frac(self.kp), kr=frac(F(0)), width=self.out),
        ]
        self.anchors = []
        for j, d in enumerate(report['true_a_stage_boxes']):
            edge = (reader.nodes[j//2] if j % 2 == 0 else
                    tuple((a+b)/2 for a, b in zip(reader.nodes[j//2], reader.nodes[j//2+1])))
            self.anchors.append((edge, box(d), j))
        self.anchors += [((F(0), self.cut), box(scalar['cut_radius']), 'cut_radius'),
                         ((F(0), self.origin), frac(jets[-1][0]), 'exact_origin'),
                         ((F(1), F(0)), reader.R, 'terminal_R')]

    def cmp(self, left, right):
        if left == right:
            return 0
        d = self.r.width_box(left, right)
        if float(d[0]) > 0:
            return -1
        if float(d[1]) < 0:
            return 1
        raise ValueError('The given S box does not order two distinct scalar boundaries')

    def pieces(self, cell):
        """Intersect every original cell with both scalar and lift pieces."""
        out = []
        for l, rr, _, _, active in self.r._cell_pieces(cell):
            for segment in self.segments:
                if self.cmp(segment['right'], l) <= 0 or self.cmp(rr, segment['left']) <= 0:
                    continue
                left = segment['left'] if self.cmp(l, segment['left']) < 0 else l
                right = segment['right'] if self.cmp(segment['right'], rr) < 0 else rr
                h = self.r.width_box(self.r.nodes[cell], self.r.nodes[cell+1])
                u0 = self.I.div(self.r.width_box(self.r.nodes[cell], left), h)
                u1 = self.I.div(self.r.width_box(self.r.nodes[cell], right), h)
                if left == self.r.nodes[cell]: u0 = self.I.exact(0.)
                if right == self.r.nodes[cell+1]: u1 = self.I.exact(1.)
                out.append((left, right, u0, u1, active, segment))
        if not out:
            raise ValueError('The cell had no scalar/lift piece')
        return out

    def power(self, a, n):
        out = self.I.exact(1.)
        for _ in range(n): out = self.I.mul(out, a)
        return out

    def power_to_piece(self, coefficients, shift, width):
        """Power polynomial in t, where t=shift+width*u, to Bernstein."""
        I, frac = self.I, self.r.fraction
        n = len(coefficients)-1
        power = []
        for k in range(n+1):
            value = I.exact(0.)
            for j in range(k, n+1):
                value = I.add(value, I.scale(I.mul(coefficients[j], self.power(shift, j-k)), math.comb(j, k)))
            power.append(I.mul(value, self.power(width, k)))
        controls = []
        for j in range(n+1):
            value = I.exact(0.)
            for k in range(j+1):
                value = I.add(value, I.mul(frac(F(math.comb(j, k), math.comb(n, k))), power[k]))
            controls.append(value)
        return I.stack(controls)

    def alpha_power(self, segment, anchor):
        """Exact curvature integral expanded in physical s-anchor."""
        I, frac = self.I, self.r.fraction
        x = self.r.width_box(segment['left'], anchor)
        if segment['kind'] == 'constant':
            return [I.sub(segment['angle'], I.mul(segment['k'], x)), I.neg(segment['k'])], [I.absolute_upper(segment['k'])]
        w = segment['width']; W = frac(w)
        u = I.div(x, W); delta = I.sub(segment['kr'], segment['kl'])
        P = [F(0), F(0), F(0), F(0), F(5, 2), F(-3), F(1)]
        coefficients = []
        for k in range(7):
            value = I.exact(0.)
            for j in range(k, 7):
                value = I.add(value, I.mul(frac(P[j]*math.comb(j, k)), self.power(u, j-k)))
            value = I.neg(I.mul(delta, I.mul(frac(w**(1-k)), value)))
            if k == 0:
                value = I.add(value, I.sub(segment['angle'], I.mul(segment['kl'], x)))
            elif k == 1:
                value = I.sub(value, segment['kl'])
            coefficients.append(value)
        bounds = [max(float(I.absolute_upper(segment['kl'])), float(I.absolute_upper(segment['kr'])))]
        controls = I.exact([0., 0., 0., 1., 1., 1.])
        for _ in range(1, 6):
            controls = self.r.derivative(controls, W)
            bounds.append(float(I.absolute_upper(I.mul(delta, controls)).max()))
        return coefficients, bounds

    def approximation(self, piece):
        I, frac = self.I, self.r.fraction
        left, right, _, _, _, segment = piece
        width = self.r.width_box(left, right)
        if segment['kind'] == 'old_exact_quintic':
            j = segment['old_index']; h = self.x[j+1]-self.x[j]
            shift = I.div(self.r.width_box((F(0), self.x[j]), left), frac(h))
            controls = self.power_to_piece([frac(c) for c in self.old_power[j]], shift, I.div(width, frac(h)))
            return controls, 0., dict(kind=segment['kind'], degree=5, old_scalar_index=j, remainder_upper=0.)
        center = tuple((a+b)/2 for a, b in zip(left, right))
        available = [(edge, box, idx) for edge, box, idx in self.anchors
                     if self.cmp(segment['left'], edge) <= 0 and self.cmp(edge, segment['right']) <= 0]
        if not available:
            raise ValueError('No existing exact scalar anchor in this analytic piece')
        anchor, a0, anchor_id = min(available, key=lambda t: float(I.absolute_upper(self.r.width_box(t[0], center))))
        alpha, alpha_bounds = self.alpha_power(segment, anchor)
        sn, cs = self.r.sine_cosine(alpha[0])
        sine, cosine = [sn], [cs]
        n = self.degree
        for j in range(n-1):
            sv, cv = I.exact(0.), I.exact(0.)
            for k in range(min(j+1, len(alpha)-1)):
                coefficient = I.scale(alpha[k+1], k+1)
                sv = I.add(sv, I.mul(coefficient, cosine[j-k]))
                cv = I.sub(cv, I.mul(coefficient, sine[j-k]))
            sine.append(I.div(sv, I.exact(j+1)))
            cosine.append(I.div(cv, I.exact(j+1)))
        coefficients = [a0]+[I.div(sine[j], I.exact(j+1)) for j in range(n)]
        controls = self.power_to_piece(coefficients, self.r.width_box(anchor, left), width)
        # Complete Bell bound for the n-th derivative of exp(i alpha).
        bell = [I.exact(1.)]
        for j in range(n):
            value = I.exact(0.)
            for k in range(min(j+1, len(alpha_bounds))):
                value = I.add(value, I.scale(I.mul(I.exact(alpha_bounds[k]), bell[j-k]), math.comb(j, k)))
            bell.append(value)
        radius = max(float(I.absolute_upper(self.r.width_box(anchor, edge))) for edge in (left, right))
        error_exact = F(float(bell[n][1]))*F(radius)**(n+1)/math.factorial(n+1)
        error = float(frac(error_exact)[1])
        return controls, error, dict(kind=segment['kind'], degree=n, anchor_stage=anchor_id,
            anchor_exact=[str(v) for v in anchor], anchor_a_box=[float(a0[0]), float(a0[1])],
            maximum_anchor_distance_upper=radius,
            a_derivative_order=n+1, a_derivative_bound_upper=float(bell[n][1]),
            remainder_upper=error, remainder_exact_upper=str(error_exact),
            scalar_source='Existing same-Hold a box plus exact curvature law; no sampled-a interpolation')
