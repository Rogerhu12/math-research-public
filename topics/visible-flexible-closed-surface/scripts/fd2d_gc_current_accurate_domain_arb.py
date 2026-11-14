"""Complete R173 interval field on the accurate R171/R172 physical domain.

The old saved cells precede the R172 completed final cell.  The latter has
the explicitly new raw/weight pullback and the unchanged physical metric.
Every derivative remains a physical-s/native-xi derivative even when the
query uses a normalized cell label.  No old finite solver/body result is
transferred to this accurate representation.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json

from flint import arb

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_complete_field_arb import CompleteCurrentFieldArb
from fd2d_gc_accurate_last_cell import AccurateLastCell
from fd2d_gc_r136_bernstein_bumps import BernsteinBumpProfile
from fd2d_gc_current_native_interval import (
    aq, rational, rational_pair, bound_record, ProfileBox, ChartBox,
    connection_box, UnresolvedInterval)
from fd2d_gc_current_primitive_interval_v2 import (
    ExactZeroEndPrimitive, cross, norm_upper)

SCHEMA = 'fd2d-current-complete-accurate-domain-Arb-v1'
PRIMITIVE_SCHEMA = 'fd2d-current-exact-normalized-physical-cell-primitive-v1'


def portable(value):
    """Locations are display metadata; immutable bytes and SHA bind inputs."""
    if isinstance(value, dict):
        return {key: portable(item) for key, item in value.items()
                if not (key == 'path' and 'sha256' in value and 'bytes' in value)}
    if isinstance(value, (list, tuple)):
        return [portable(v) for v in value]
    return value


def digest(value):
    return hashlib.sha256(json.dumps(portable(value), sort_keys=True,
        separators=(',', ':'), allow_nan=False).encode()).hexdigest()


class AccurateDomainCurrentFieldArb:
    """Full defining functions, with explicit unresolved derivative boxes.

    box() takes physical rational endpoints and is restricted to cells
    before the final one.  cell_box() takes 0<=tlo<=thi<=1 for ANY saved
    cell, using its true physical length.  The final length is S-b, not the
    old binary64 label E-b.  A query including the degenerate cut has only
    the scope supplied by the separately proved R172 consumer.
    """
    def __init__(self, native_definition, profile_packet, *,
                 profile_packet_sha256, precision=256,
                 profile_backend='bernstein_bumps', atlas_options=None):
        self.interior = CompleteCurrentFieldArb(native_definition, profile_packet,
            profile_packet_sha256=profile_packet_sha256,
            precision=precision, atlas_options=atlas_options)
        self.parts, self.reader, self.atlas = (
            self.interior.parts, self.interior.reader, self.interior.atlas)
        self.saved_mesh = self.parts.mesh
        self.last_cell = len(self.saved_mesh)-2
        if profile_backend == 'bernstein_bumps':
            tighter = BernsteinBumpProfile.from_packet(profile_packet,
                expected_sha256=profile_packet_sha256)
            if tighter.input_binding_sha256 != self.interior.profile.input_binding_sha256:
                raise ValueError('A range backend may not change the physical target')
            # Only the method of enclosing the same exact bump polynomials
            # changes.  The original class/source and packet are untouched.
            self.interior.profile = tighter
        elif profile_backend != 'original':
            raise ValueError('Unknown explicitly selected profile range backend')
        self.profile = self.interior.profile
        self.terminal = AccurateLastCell(self.reader.arrays_path, profile_packet,
            profile_sha256=profile_packet_sha256)
        if (self.terminal.b != self.saved_mesh[-2]
                or self.terminal.E != self.saved_mesh[-1]
                or self.terminal.profile.input_binding_sha256 != self.profile.input_binding_sha256):
            raise ValueError('The accurate last-cell definition and interior do not match')
        self.accurate_end = self.terminal.S
        self._binding = dict(schema=SCHEMA, source=identity(__file__),
            interior_binding_sha256=self.interior.binding_sha256,
            interior_source=identity(__import__('fd2d_gc_current_complete_field_arb').__file__),
            accurate_profile_definition=self.profile.definition(),
            profile_range_backend=profile_backend,
            terminal_definition=self.terminal.definition(),
            exact_saved_mesh=[rational_pair(q) for q in self.saved_mesh],
            final_cell=self.last_cell,
            complete_field_semantics='Saved accurate mathematical interior through b; R172 raw(sigma)+eta(sigma)*T(a(s),u), then R155 with K(s), on the entire final cell',
            physical_g_changed=False,
            last_saved_cell_function_changed_explicitly=True,
            old_finite_residual_or_body_transferred=False,
            native_derivatives='physical s at fixed native xi; physical u via the complete U_s/U_xi chain rule',
            cut_scope='exact rational R132 value/u/uu trace only; no invented radial II derivative',
            whole_surface_certificate=False)
        self.binding_sha256 = digest(self._binding)

    def cell_definition(self, cell):
        cell = int(cell)
        if not 0 <= cell <= self.last_cell:
            raise IndexError('Actual physical cell index outside the bound mesh')
        if cell == self.last_cell:
            return dict(cell=cell, left_exact=rational_pair(self.terminal.b),
                right_definition='S: the R171 exact phase-integral cut',
                right_enclosure=bound_record(self.accurate_end),
                physical_length=bound_record(self.terminal.length),
                normalized_label='s=b+(S-b)*t; 0<=t<=1',
                source_binding_sha256=self.terminal.definition()['binding_sha256'])
        left, right = self.saved_mesh[cell:cell+2]
        return dict(cell=cell, left_exact=rational_pair(left), right_exact=rational_pair(right),
            length_exact=rational_pair(right-left),
            normalized_label='s=left+(right-left)*t; 0<=t<=1')

    def cell_length(self, cell):
        cell = int(cell)
        self.cell_definition(cell)
        return self.terminal.length if cell == self.last_cell else aq(self.saved_mesh[cell+1]-self.saved_mesh[cell])

    def box(self, cell, lo, hi, angular_lo, angular_hi, *,
            angle_unit='pi', side='both', connection=True):
        cell = int(cell)
        if not 0 <= cell < self.last_cell:
            raise ValueError('Use cell_box() with normalized labels for the completed final cell')
        result = self.interior.box(cell, lo, hi, angular_lo, angular_hi,
            angle_unit=angle_unit, side=side, connection=connection)
        result.update(binding_sha256=self.binding_sha256,
            complete_accurate_domain_definition_bound=True,
            evaluated_patch='original saved physical cell before R172 completion',
            mathematical_field_source_binding=self.interior.binding_sha256,
            physical_derivatives=True)
        return result

    def cell_box(self, cell, tlo, thi, angular_lo, angular_hi, *,
                 angle_unit='pi', side='both', connection=True):
        cell = int(cell); tlo, thi = map(rational, (tlo, thi))
        if not 0 <= tlo <= thi <= 1:
            raise ValueError('Normalized true physical cell labels must lie in [0,1]')
        definition = self.cell_definition(cell)
        if cell != self.last_cell:
            left, right = self.saved_mesh[cell:cell+2]
            result = self.box(cell, left+(right-left)*tlo, left+(right-left)*thi,
                angular_lo, angular_hi, angle_unit=angle_unit, side=side, connection=connection)
            result.update(normalized_cell_labels=[rational_pair(tlo), rational_pair(thi)],
                          cell_definition=definition)
            return result
        q = self.terminal.box(tlo, thi, angular_lo, angular_hi, angle_unit=angle_unit)
        p = q['profile']
        profile = ProfileBox(p['a'], p['a_s'], p['a_ss'], p['a_sss'])
        chart = ChartBox(arb(1), arb(0), arb(0), arb(0))
        result = dict(q, profile_box=p, profile=profile, chart=chart,
            cell=cell, cell_definition=definition,
            normalized_cell_labels=[rational_pair(tlo), rational_pair(thi)],
            field_order=['n','m','l'], binding_sha256=self.binding_sha256,
            evaluated_patch='R172 entire explicitly completed final cell',
            physical_derivatives=True, complete_accurate_domain_definition_bound=True,
            old_finite_residual_or_body_transferred=False,
            continuous_global_surface_certificate=False)
        if connection:
            result['connection'] = (None if q['cut'] else connection_box(q['fields'], profile, chart))
            result['connection_available'] = not q['cut']
        return result

    def accurate_cut_angular(self, lo, hi, *, angle_unit='pi'):
        return self.cell_box(self.last_cell, F(1), F(1), lo, hi, angle_unit=angle_unit)

    def primitive_box(self, primitive, cell, lo, hi, angular_lo, angular_hi, *,
                      angle_unit='pi', side='both'):
        if primitive.field_binding_sha256 != self.binding_sha256:
            raise ValueError('Primitive must bind the complete accurate-domain field')
        q = self.box(cell, lo, hi, angular_lo, angular_hi,
                     angle_unit=angle_unit, side=side, connection=True)
        result = primitive.conditional_box(q['connection'], q['chart'],
            lo, hi, angular_lo, angular_hi, field_binding_sha256=self.binding_sha256,
            angle_unit=angle_unit)
        result.update(complete_actual_field_inputs_supplied=True, source_cell=int(cell),
                      initial_compatibility_supplied=False, whole_surface_certificate=False)
        return result

    def cell_primitive_box(self, primitive, cell, tlo, thi, angular_lo, angular_hi, *,
                           angle_unit='pi', side='both'):
        q = self.cell_box(cell, tlo, thi, angular_lo, angular_hi,
                         angle_unit=angle_unit, side=side, connection=True)
        if q['connection'] is None:
            raise UnresolvedInterval('Cut angular traces alone do not supply the full R125 forcing')
        return primitive.conditional_box(self, q, cell, tlo, thi,
                                         angular_lo, angular_hi, angle_unit=angle_unit)

    def definition(self):
        return dict(self._binding, binding_sha256=self.binding_sha256,
            full_interior=self.interior.definition(),
            exact_zero_end_primitive_extension='Normalized cell P; physical q=(true cell length)*unit-cell q. The R171 cut definition, not its enclosure midpoint, defines the final length.',
            remaining_unpaid=['continuous unknown n positivity where R153 is active for this actual input',
                'R155 one-sided forcing bounds on boxes reaching the degenerate cut',
                'actual forcing polynomial remainder coverage and accumulated R125 budget',
                'initial frame/position compatibility and actual full-surface posterior'],
            new_nonlinear_solution_inferred=False, whole_surface_certificate=False)


class ExactNormalizedCellPrimitive:
    """Exact finite P(t,xi) with q=L*integral_0^t(P-mean) for true L.

    L is defined by a bound actual cell, including the exact nonrational
    R171 last length.  Its Arb enclosure is used only for evaluation.  The
    zero-end and q_s=P-mean identities are exact, not rounding tests.
    """
    def __init__(self, field, cell, cosine, sine, *, provenance):
        self.cell = int(cell)
        self.cell_definition = field.cell_definition(self.cell)
        self.field_binding_sha256 = field.binding_sha256
        self.unit = ExactZeroEndPrimitive(F(0), F(1), cosine, sine,
            field_binding_sha256=self.field_binding_sha256, provenance=provenance)
        self.exact_identities = dict(self.unit.exact_identities,
            physical_q_s_exact_P_minus_mean=True,
            true_length_not_enclosure_midpoint_defines_polynomial=True)
        self.packet_sha256 = digest(self.definition(include_hash=False))

    def definition(self, include_hash=True):
        result = dict(schema=PRIMITIVE_SCHEMA, source=identity(__file__),
            field_binding_sha256=self.field_binding_sha256,
            cell_definition=self.cell_definition, unit_cell_polynomial=self.unit.definition(),
            physical_primitive='q=L*q_unit, with L the exact physical cell length defined by the bound field',
            exact_identities=self.exact_identities,
            all_three_Gauss_Codazzi_components_retained=True,
            actual_H_minus_P_or_complete_posterior_asserted=False)
        if include_hash:result['packet_sha256']=self.packet_sha256
        return result

    def polynomial_boxes(self, field, tlo, thi, angular_lo, angular_hi, *, angle_unit='pi'):
        if (field.binding_sha256 != self.field_binding_sha256
                or field.cell_definition(self.cell) != self.cell_definition):
            raise ValueError('Normalized primitive belongs to another exact physical field/cell')
        p = self.unit.polynomial_boxes(tlo, thi, angular_lo, angular_hi, angle_unit=angle_unit)
        length = field.cell_length(self.cell)
        if not length > 0:raise UnresolvedInterval('The bound true physical cell length is not positive')
        p.update(q=tuple(length*v for v in p['q']), q_xi=tuple(length*v for v in p['q_xi']),
                 exact_zero_endpoints=self.exact_identities, physical_length_enclosure=length)
        return p

    def conditional_box(self, field, evaluated, cell, tlo, thi, angular_lo, angular_hi, *, angle_unit='pi'):
        if int(cell) != self.cell or evaluated['binding_sha256'] != self.field_binding_sha256:
            raise ValueError('The complete evaluated forcing and normalized primitive do not match')
        connection, chart = evaluated['connection'], evaluated['chart']
        if connection is None:raise UnresolvedInterval('No full R125 forcing is available at the degenerate cut')
        p = self.polynomial_boxes(field, tlo, thi, angular_lo, angular_hi, angle_unit=angle_unit)
        remainder = tuple(a-b for a,b in zip(connection['h_vector'], p['P']))
        commutator = cross(p['q'], connection['alpha'])
        E = tuple(m+r+chart.drift()*v+c for m,r,v,c in
                  zip(p['mean'], remainder, p['q_xi'], commutator))
        return dict(E=E, E_norm_upper=norm_upper(E),
            Q_e1_norm_upper=norm_upper(p['q'][1:]), Q_norm_upper=norm_upper(p['q']),
            q=p['q'], q_xi=p['q_xi'], remainder=remainder,
            field_binding_sha256=self.field_binding_sha256,
            primitive_sha256=self.packet_sha256, source_cell=self.cell,
            physical_cell_length_enclosure=bound_record(p['physical_length_enclosure']),
            physical_Us_term_included=True, Gauss_third_component_included=True,
            complete_actual_field_inputs_supplied=True,
            H_minus_P_method='complete actual interval forcing minus exact finite P',
            initial_compatibility_supplied=False, whole_surface_certificate=False)
