"""R170: exact eight-piece Bernstein box for the unchanged degree-15 tail.

The matrix entries are dyadic and exactly representable in binary64. A
floating matrix-vector product need not be exact: ``certificate`` therefore
uses exact integer/rational arithmetic on the actual supplied controls.
No legacy class name, guard, source, parameter column, or polynomial changes.
"""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from math import comb, isfinite
from pathlib import Path
import numpy as np
from fd2d_positive_flat_developable_family import (
    PositiveFlatDevelopableFamily, primitive_weights)

DEGREE = 15
PARTS = 8
DENOMINATOR = PARTS**DEGREE
UPPER = Fraction(6, 5)
BOX_SCHEMA = 'fd2d-degree15-eight-dyadic-Bernstein-box-v1'
TAIL_SCHEMA = 'fd2d-dyadic-Bernstein-curvature-flat-tail-v1'
HERE = Path(__file__).resolve().parent


def _identity(path):
    path = Path(path)
    data = path.read_bytes()
    return dict(path=str(path.resolve()), bytes=len(data), sha256=sha256(data).hexdigest())


def _fraction(value):
    if isinstance(value, (float, np.floating)):
        if not isfinite(float(value)):
            raise ValueError('Controls must be finite')
        return Fraction.from_float(float(value))
    if isinstance(value, (int, np.integer)):
        return Fraction(int(value))
    return Fraction(value)


@lru_cache(maxsize=1)
def restriction_numerators():
    """N[j*16+k,i], with S=N/2**45; exact integer blossom formula."""
    rows = []
    for j in range(PARTS):
        for k in range(DEGREE+1):
            row = []
            for i in range(DEGREE+1):
                value = 0
                for r in range(max(0, i-k), min(i, DEGREE-k)+1):
                    s = i-r
                    value += (comb(DEGREE-k, r)*comb(k, s)*
                        j**r*(PARTS-j)**(DEGREE-k-r)*
                        (j+1)**s*(PARTS-j-1)**(k-s))
                row.append(value)
            if min(row) < 0 or sum(row) != DENOMINATOR:
                raise ArithmeticError('Invalid exact restriction row')
            rows.append(row)
    result = np.asarray(rows, dtype=np.int64)
    result.flags.writeable = False
    return result


class DyadicBernsteinControlBox:
    """The 128 two-sided exact inequalities 0 <= S b <= 6/5.

    ``linear_constraints`` supplies floating coefficients for a finite QP;
    ``certificate`` decides membership in the mathematical domain. The
    latter is not replaced by a tolerance, clipping, or a sampled P value.
    """
    def __init__(self):
        self.numerators = restriction_numerators()
        self.matrix = self.numerators.astype(np.float64)/DENOMINATOR
        self.matrix.flags.writeable = False

    def definition(self):
        exact_bytes = json.dumps(self.numerators.tolist(), separators=(',', ':')).encode()
        return dict(schema=BOX_SCHEMA, degree=DEGREE, parts=PARTS,
            interval_endpoints_exact=[str(Fraction(j, PARTS)) for j in range(PARTS+1)],
            row_order='j*(degree+1)+k: local Bernstein coefficient k on interval j',
            shape=list(self.matrix.shape), numerator_denominator=str(DENOMINATOR),
            numerator_matrix_json_sha256=sha256(exact_bytes).hexdigest(),
            numerator_matrix_json_encoding='compact JSON integer nested list, no newline',
            exact_lower='0', exact_upper=str(UPPER),
            numerator_formula=('sum_{r+s=i} C(15-k,r) C(k,s) j^r (8-j)^(15-k-r) '
                               '(j+1)^s (7-j)^(k-s)'),
            matrix_entries_exact_in_binary64=True,
            floating_matrix_vector_product_claimed_exact=False,
            selected_sufficient_domain_not_necessary_function_range=True)

    def coefficients_exact(self, controls):
        values = list(controls)
        if len(values) != DEGREE+1:
            raise ValueError('This explicit domain requires exactly 16 controls')
        b = [_fraction(v) for v in values]
        # Actual binary64 inputs have a common power-of-two denominator.
        # Generic exact Fraction inputs are also supported for proof witnesses.
        from math import lcm
        denominator = lcm(*(v.denominator for v in b))
        integers = [v.numerator*(denominator//v.denominator) for v in b]
        output_denominator = denominator*DENOMINATOR
        return tuple(Fraction(sum(int(n)*v for n, v in zip(row, integers)),
                              output_denominator) for row in self.numerators)

    def certificate(self, controls, *, include_local_coefficients=False):
        b = tuple(_fraction(v) for v in controls)
        c = self.coefficients_exact(b)
        bad = [i for i, v in enumerate(c) if not 0 <= v <= UPPER]
        lo, hi = min(c), max(c)
        result = dict(schema='fd2d-exact-dyadic-Bernstein-membership-v1',
            passed=not bad, exact_arithmetic=True, controls_interpreted_as_exact_values=True,
            degree=DEGREE, parts=PARTS, rows=len(c),
            local_lower_exact=str(lo), local_upper_exact=str(hi),
            minimum_lower_slack_exact=str(lo), minimum_upper_slack_exact=str(UPPER-hi),
            global_lower_exact=str(min(b)), global_upper_exact=str(max(b)),
            global_control_box_passed=all(0 <= v <= UPPER for v in b),
            global_negative_indices=[i for i, v in enumerate(b) if v < 0],
            violated_rows=[dict(row=i, interval=i//16, local_index=i % 16,
                                value_exact=str(c[i])) for i in bad])
        if include_local_coefficients:
            result['local_coefficients_exact'] = [str(v) for v in c]
        return result

    def linear_constraints(self, current=None):
        """Return A, lower, upper, plus exact right sides for absolute/step b.

        A is the same 128x16 exact binary64 matrix. Bounds returned for a
        finite linear solve are rounded binary64 representatives of the
        separate exact fractions, never a certificate of a computed step.
        """
        current_exact = ((Fraction(0),)*(DEGREE+1) if current is None
                         else tuple(_fraction(v) for v in current))
        c = self.coefficients_exact(current_exact)
        lower = tuple(-v for v in c)
        upper = tuple(UPPER-v for v in c)
        return dict(matrix=self.matrix,
            lower=np.asarray([float(v) for v in lower]),
            upper=np.asarray([float(v) for v in upper]),
            lower_exact=[str(v) for v in lower], upper_exact=[str(v) for v in upper],
            kind='absolute_controls' if current is None else 'increments_from_exact_current_controls',
            floating_QP_feasibility_is_not_exact_domain_certificate=True,
            definition=self.definition())

    def repair_toward_constant(self, controls):
        """Explicit new controls near the exact segment toward constant 3/5.

        This never changes an input in place and is not a permissive domain
        test. The exact segment is first contracted by the smallest needed
        theta; binary64 rounding is then certified again. If necessary a
        recorded dyadic extra contraction is increased. The final case is
        the rounded constant 3/5, so the bounded loop terminates.
        """
        original = np.asarray(controls, dtype=np.float64)
        if original.shape != (16,) or not np.all(np.isfinite(original)):
            raise ValueError('Require 16 finite binary64 controls')
        before = self.certificate(original)
        b = tuple(Fraction.from_float(float(v)) for v in original)
        c = self.coefficients_exact(b)
        anchor = Fraction(3, 5)
        minimum = Fraction(0)
        for v in c:
            if v < 0:
                minimum = max(minimum, -v/(anchor-v))
            elif v > UPPER:
                minimum = max(minimum, (v-UPPER)/(v-anchor))
        extras = [Fraction(0)]+[Fraction(1, 2**k) for k in range(52, -1, -1)]
        for attempt, extra in enumerate(extras):
            theta = minimum+(1-minimum)*extra
            target = tuple((1-theta)*v+theta*anchor for v in b)
            actual = np.asarray([float(v) for v in target])
            certificate = self.certificate(actual)
            if certificate['passed']:
                actual_exact = tuple(Fraction.from_float(float(v)) for v in actual)
                change = tuple(v-old for v, old in zip(actual_exact, b))
                error = tuple(v-exact for v, exact in zip(actual_exact, target))
                info = dict(schema='fd2d-explicit-tail-contraction-to-three-fifths-v1',
                    input_certificate=before, output_certificate=certificate,
                    exact_anchor=str(anchor), exact_minimum_theta=str(minimum),
                    exact_used_theta=str(theta), extra_fraction_of_remaining_segment=str(extra),
                    attempts=attempt+1, input_modified_in_place=False,
                    saved_binary64_controls_claimed_exactly_on_segment=False,
                    maximum_actual_parameter_change_exact=str(max(map(abs, change))),
                    maximum_rounding_error_from_exact_segment_exact=str(max(map(abs, error))),
                    actual_parameter_changes_exact=[str(v) for v in change],
                    input_controls_hex=[float(v).hex() for v in original],
                    output_controls_hex=[float(v).hex() for v in actual],
                    field_changed=any(change), exact_recheck_passed=True)
                actual.flags.writeable = False
                return dict(controls=actual, info=info)
        raise ArithmeticError('The certified constant anchor was not reached')


def strict_witness_controls():
    """Exact degree-15 controls of (q-1/2)^2+1/128."""
    return tuple(Fraction(i*(i-1), DEGREE*(DEGREE-1))-Fraction(i, DEGREE)+
                 Fraction(33, 128) for i in range(DEGREE+1))


class DyadicBernsteinFlatDevelopableFamily(PositiveFlatDevelopableFamily):
    """A new explicit domain, with the inherited unchanged polynomial jets.

    Inheritance reuses the actual Bernstein integral formulas; this is a
    real distinct class and is never renamed or passed through a legacy
    negative-coefficient guard. All coefficients are immutable binary64.
    """
    def __init__(self, coefficients, **kwargs):
        controls = np.asarray(coefficients, dtype=np.float64)
        if controls.shape != (DEGREE+1,) or not np.all(np.isfinite(controls)):
            raise ValueError('Require exactly 16 finite binary64 controls')
        self.control_box = DyadicBernsteinControlBox()
        self.control_certificate = self.control_box.certificate(controls)
        if not self.control_certificate['passed']:
            raise ValueError('The actual controls fail the exact eight-piece Bernstein box')
        super().__init__(controls, **kwargs)

    def sufficient_bounds(self):
        packet = self.control_certificate
        upper = float(_fraction(packet['local_upper_exact']))
        weights, exact = primitive_weights(DEGREE)
        return dict(degree=DEGREE,
            controls_lower=float(self.coefficients.min()), controls_upper=float(self.coefficients.max()),
            global_control_box_passed=packet['global_control_box_passed'],
            selected_dyadic_box_0_to_6_over_5=True,
            polynomial_lower_exact=packet['local_lower_exact'],
            polynomial_upper_exact=packet['local_upper_exact'],
            endpoint_angle=float(weights@self.coefficients), endpoint_weights_exact=list(exact),
            curvature_nonnegative_sufficient=True,
            absolute_curvature_upper=upper*315/(128*self.width),
            absolute_angle_upper=upper,
            positive_projection_sufficient=upper < np.pi/2,
            absolute_deflection_upper=upper*self.width/2,
            standard_R132_uniform_bounds_exact=dict(curvature='4725/736',
                total_turn='12/5', depression='69/250', full_cylinder_reach='736/4725'),
            standard_uniform_bounds_require_exact_R132_geometry=True,
            scope=('Function bounds follow from all 128 exact restricted coefficients. '
                   'Displayed ordinary floating derived bounds are numerical representatives; '
                   'R170 proves the exact R132 standard constants. No core certificate is transferred.'))

    def definition(self):
        return dict(schema=TAIL_SCHEMA,
            class_name=type(self).__module__+'.'+type(self).__name__,
            polynomial_formula='P(q)=sum_{i=0}^{15} b_i B_i^15(q)',
            angle_formula='sign(y)*630*integral_0^q t^4*(1-t)^4*P(t)dt, with clipped q',
            polynomial_basis_kind='bernstein_curvature_integral',
            legacy_evaluator_basis_tag='positive_bernstein',
            legacy_basis_tag_is_not_a_domain_or_class_identity=True,
            controls_hex=[float(v).hex() for v in self.coefficients],
            geometry_hex={key:float(getattr(self, key)).hex() for key in
                          ('cut_radius','flat_radius','cuff_radius','plane_height')},
            quadrature_order=self.quadrature_order, quadrature_chunk=self.quadrature_chunk,
            position_integral_is_mathematical_definition_not_GL_rule=True,
            control_box=self.control_box.definition(), exact_certificate=self.control_certificate,
            parameter_dimension=16, parameter_columns_changed=False,
            sources=[_identity(HERE/name) for name in (
                'fd2d_dyadic_bernstein_tail.py',
                'fd2d_positive_flat_developable_family.py',
                'fd2d_flat_developable_family.py')])

    @classmethod
    def from_definition(cls, definition, *, owner=None):
        if isinstance(definition, (str, Path)):
            owner = Path(definition)
            meta = json.loads(owner.read_text())
        else:
            meta = definition
        if meta.get('schema') != TAIL_SCHEMA:
            raise ValueError('Require the explicit dyadic-tail schema')
        for row in meta['sources']:
            name = Path(row['path']).name
            options = [Path(row['path']), HERE/name]
            if owner is not None:
                options.append(Path(owner).parent/name)
            if not any(p.is_file() and _identity(p)['sha256'] == row['sha256'] for p in options):
                raise ValueError('Missing or changed defining source: '+name)
        obj = cls([float.fromhex(v) for v in meta['controls_hex']],
            **{key:float.fromhex(v) for key,v in meta['geometry_hex'].items()},
            quadrature_order=meta['quadrature_order'], quadrature_chunk=meta['quadrature_chunk'])
        expected = obj.definition()
        for key in expected:
            if key != 'sources' and meta.get(key) != expected[key]:
                raise ValueError('Changed dyadic-tail definition: '+key)
        return obj
