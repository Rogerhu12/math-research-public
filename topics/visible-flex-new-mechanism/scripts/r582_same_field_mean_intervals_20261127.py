#!/usr/bin/env python3
"""Exact-current and exact-reference a/z two-jets for the same 97q surface.

Consumes the endpoint/angle interface and one R611 v2 validated height
integral object.  The analytic infinite oscillatory tail is retained at
every positive delta; only its interval estimate changes near delta=0.
No scientific execution, full coverage, or candidate acceptance is implicit.
"""
import hashlib
from pathlib import Path


BINDINGS = {
    'r582_same_field_radial_intervals_20261127.py':
        'ed167c5850ccb4e438f02a3c8d7aac051466103af2e559c0e3356001bf3ecb28',
    'r611_circular_reference_global_geometry_20261127.py':
        'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f',
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError('same-field mean source changed: '+filename)
from r582_same_field_radial_intervals_20261127 import (
    EnvelopedSpline, exact, rational_interval, add_jets, scale_jets, multiply_jets,
)

SCHEMA = 'r582-same-field-current-reference-mean-two-jets-with-full-tail-v1'


class IntervalEnvelopedSpline(EnvelopedSpline):
    """Same spline for interval coefficients, including exact rational differences."""
    def __init__(self, coefficients, backend):
        self.backend = backend
        if len(coefficients) != 8:
            raise ValueError('eight original radial coefficients required')
        item = (tuple(float(v) for v in backend.KNOTS),
                [backend.I.as_interval(v) for v in coefficients], 5)
        self.polynomials = [item]
        for _ in range(2):
            item = backend.derivative_spline(*item)
            self.polynomials.append(item)


def exponential_jets(jets, backend):
    value = backend.exp_i(jets[0])
    return value, value*jets[1], value*(jets[2]+jets[1]**2)


class SameFieldMeanGeometry:
    def __init__(self, radial_design, validated_height_provider, reference_q=None):
        self.design, self.height_provider = radial_design, validated_height_provider
        self.b, self.I = radial_design.b, radial_design.I
        # The supplied provider must be the bound R611 v2 method, which fixes
        # -AMP*ELL by forming the prefactor inside interval arithmetic.
        if (type(validated_height_provider).__name__ != 'CompactGeometry'
                or type(validated_height_provider).__module__ !=
                   'r611_circular_reference_global_geometry_20261127'):
            raise TypeError('the actual hash-bound R611 v2 validated height object is required')
        q = self.design.q
        reference = tuple(float(x) for x in (self.b.Q if reference_q is None else reference_q))
        if len(reference) not in (81,97):
            raise ValueError('reference mean must come from a full original81q or actual97q')
        self.reference_uses_original_Q = reference_q is None
        self.reference_mean_coefficients = reference[64:80]+(reference[-1],)
        self.current_alpha = EnvelopedSpline(q[64:72], self.b)
        self.current_z = EnvelopedSpline(q[72:80], self.b)
        # This is the chosen comparison surface, which may carry the NEW
        # current mean controls.  It NEVER changes design.reference_alpha:
        # the material seed quotient retains its original frozen radius.
        self.reference_alpha = EnvelopedSpline(reference[64:72], self.b)
        self.reference_z = EnvelopedSpline(reference[72:80], self.b)
        qa_delta = tuple(exact(a)-exact(b) for a,b in zip(q[64:72], reference[64:72]))
        qz_delta = tuple(exact(a)-exact(b) for a,b in zip(q[72:80], reference[72:80]))
        self.alpha_equal = all(v == 0 for v in qa_delta)
        self.z_equal = all(v == 0 for v in qz_delta)
        self.alpha_difference = IntervalEnvelopedSpline(
            [rational_interval(self.b,v) for v in qa_delta], self.b)
        self.z_difference = IntervalEnvelopedSpline(
            [rational_interval(self.b,v) for v in qz_delta], self.b)
        self.height_difference = rational_interval(self.b, exact(q[-1])-exact(reference[-1]))
        self.mu = self.I(-.040019082162222074)
        self.nu = self.I(-.048942275258064924)
        self.reference_height = self.I(reference[-1])
        self.current_height = self.I(q[-1])
        self.counts = {'compact_exact_height_queries':0, 'analytic_infinite_tail_boxes':0,
                       'complete_current_reference_mean_boxes':0}

    def analytic_height_jets(self, s):
        """H,H_s,H_ss of the FULL source integral, including every inner tail."""
        b, I = self.b, self.I
        if s.lo == b.L and s.hi == b.L:
            return I(0), I(0), I(0)
        delta = (I(b.L)-s)/b.ELL
        if delta.lo < 0:
            # The real (L-s)/ell is nonnegative on the supplied domain.
            if s.hi > b.L:
                raise ValueError('height interval extends beyond the actual cap seam')
            delta = I(0,delta.hi)
        if delta.hi <= .08:
            h = I(delta.hi)
            if h.hi == 0:
                return I(0), I(0), I(0)
            # exp(-1/d)*d^-j is increasing for d<=1/j, j=2,4;
            # h<=.08<1/4.  This includes delta=0 by its flat limit.
            decay = b.exp_i(-1/h)
            w = I(b.AMP)*decay
            ws = I(b.AMP)/b.ELL*decay*(3/h**2+2/h**4)
            height = I(b.AMP)*b.ELL*h*decay
            self.counts['analytic_infinite_tail_boxes'] += 1
            return I(-height.hi,0), I(0,w.hi), I(-ws.hi,ws.hi)
        if delta.lo < b.original.CUT:
            raise ArithmeticError('height interval crosses compact/tail scopes; subdivide')
        phase = delta**-2
        sine, cosine = b.sin_i(phase), b.cos_i(phase)
        w = I(b.AMP)*b.exp_i(-(2-sine)/delta)
        ws = -w*((2-sine)/delta**2-2*cosine/delta**4)/b.ELL
        height = self.height_provider.exact_tail_height(delta)
        self.counts['compact_exact_height_queries'] += 1
        return height,w,ws

    def _alpha_jets(self, s, reference):
        polynomial = self.reference_alpha if reference else self.current_alpha
        return add_jets(polynomial.jets(s), scale_jets(self.b.bump_jets(s),self.mu))

    def _radius_jets(self, s, core_radius, reference):
        I,b = self.I,self.b
        if s.hi <= b.C:
            return core_radius,I(0),I(0)
        (bg,bg1,bg2),_ = self.design.background_jets(s)
        tail = I(b.RC)+b.L-s
        base = ((1-bg)*core_radius+bg*tail,
                bg1*(tail-core_radius)-bg,
                bg2*(tail-core_radius)-2*bg1)
        return multiply_jets(exponential_jets(self._alpha_jets(s,reference),b),base)

    def _height_jets(self, s, tail_height, reference):
        I,b = self.I,self.b
        if s.hi <= b.C:
            return I(b.original.CORE_HALF)+s,I(1),I(0)
        (bg,bg1,bg2),_ = self.design.background_jets(s)
        H,w,ws = tail_height
        final = self.reference_height if reference else self.current_height
        central,tail = I(b.original.CORE_HALF)+s,final+H
        spline = self.reference_z if reference else self.current_z
        correction = add_jets(spline.jets(s),scale_jets(b.bump_jets(s),self.nu))
        return ((1-bg)*central+bg*tail+correction[0],
                1-bg+bg1*(tail-central)+bg*w+correction[1],
                -2*bg1+bg2*(tail-central)+2*bg1*w+bg*ws+correction[2])

    @staticmethod
    def dictionary(radius,height):
        return dict(zip(('a','a_s','a_ss','z','z_s','z_ss'),radius+height))

    def boxes(self,left,right,current_core_radius):
        """Six jets for both surfaces and direct, correlated difference jets.

        current_core_radius encloses the EXACT normalized rounded-ellipse
        perimeter, e.g. rounded_core_angular_boxes(...)["a0"].  A stored
        ordinary elliptic-integral value is not accepted as certification.
        """
        self.design.hermite.check()
        I,b = self.I,self.b
        if not isinstance(current_core_radius,I) or current_core_radius.lo <= 0:
            raise TypeError('positive same-core normalized perimeter interval required')
        if not 0 <= left <= right <= b.L:
            raise ValueError('complete body interval must lie in [0,L]')
        if left < b.C < right:
            raise ArithmeticError('split at the original exact core boundary')
        s = I(left,right)
        reference_core = I(self.design.reference_core_radius)
        if right <= b.C:
            tail_height = (I(0),I(0),I(0))
        else:
            tail_height = self.analytic_height_jets(s)
        a0 = self._radius_jets(s,reference_core,True)
        a = self._radius_jets(s,current_core_radius,False)
        z0 = self._height_jets(s,tail_height,True)
        z = self._height_jets(s,tail_height,False)
        (bg,bg1,bg2),complement = self.design.background_jets(s)
        delta_core = current_core_radius-reference_core
        delta_base = scale_jets(complement,delta_core)
        if self.alpha_equal:
            e_current = exponential_jets(self._alpha_jets(s,False),b)
            da = multiply_jets(e_current,delta_base)
        else:
            da_alpha = self.alpha_difference.jets(s)
            exp_delta = exponential_jets(da_alpha,b)
            exp_delta_minus_one = (exp_delta[0]-1,exp_delta[1],exp_delta[2])
            da = add_jets(multiply_jets(a0,exp_delta_minus_one),
                multiply_jets(exponential_jets(self._alpha_jets(s,False),b),delta_base))
        dz_controls = (I(0),I(0),I(0)) if self.z_equal else self.z_difference.jets(s)
        dz = add_jets(scale_jets((bg,bg1,bg2),self.height_difference),dz_controls)
        self.counts['complete_current_reference_mean_boxes'] += 1
        return {'current':self.dictionary(a,z),'reference':self.dictionary(a0,z0),
                'difference':self.dictionary(da,dz),
                'differences_use_same_analytic_height_and_fixed_mu_nu':True}

    def cap_disk_difference(self):
        """Both exact Cartesian disks: only their fixed vertical translations differ."""
        return {'height_difference':self.height_difference,
                'C0_upper':max(abs(self.height_difference.lo),abs(self.height_difference.hi)),
                'C1_difference_upper':0.,'reference_covariant_C2_difference_upper':0.,
                'same_disk_radius':float(self.b.RC),
                'no_positive_width_body_annulus_is_replaced_by_this_disk':True}

    def receipt(self):
        return {'schema':SCHEMA,'new_counts':dict(self.counts),
            'comparison_reference_uses_original_SOURCE_Q':self.reference_uses_original_Q,
            'comparison_reference_mean_entries64_80_and_final_height':list(self.reference_mean_coefficients),
            'new_comparison_reference_geometry_requires_its_own_certificate':not self.reference_uses_original_Q,
            'material_seed_frozen_radius_design_reference_alpha_not_changed':True,
            'R611_object_supplies_only_same_analytic_height_not_new_reference_curvature':True,
            'full_analytic_oscillatory_height_not_numerically_zero_suffix':True,
            'exact_same_material_field_radius_and_height_formulas':True,
            'shared_height_cancels_only_in_the_explicit_difference_jets':True,
            'all_current_original_mean_controls_and_final_height_retained':True,
            'mean_geometry_has_no_ODE_or_FFT_query':True,
            'full_coverage_and_R604_certificate_not_issued_by_this_interface':True}
