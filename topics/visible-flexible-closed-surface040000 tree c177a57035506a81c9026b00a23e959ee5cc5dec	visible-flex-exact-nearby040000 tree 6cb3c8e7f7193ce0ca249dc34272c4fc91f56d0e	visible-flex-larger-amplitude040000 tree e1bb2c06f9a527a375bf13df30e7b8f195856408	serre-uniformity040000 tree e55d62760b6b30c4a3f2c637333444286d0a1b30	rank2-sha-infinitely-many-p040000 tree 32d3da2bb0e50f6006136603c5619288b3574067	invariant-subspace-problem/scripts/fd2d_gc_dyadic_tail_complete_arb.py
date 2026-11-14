"""The complete R173 interval field with the explicit R170 tail domain.

These are new constructors, not a change to the closed legacy readers.  The
actual negative global Bernstein controls are decoded and certified by the
R170 archive reader.  Full raw/affine/atlas/nonlinear/primitive formulas are
inherited from their bound sources; the exact physical last cell is supplied
by its separately bound R170 constructor.  No sampled field or finite solver
residual is promoted to a continuous enclosure.
"""
from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import json

from flint import ctx

from fd2d_gc_archive_arrays import identity
from fd2d_gc_current_native_interval import (
    CurrentNativeIntervalPieces, rational, rational_pair)
from fd2d_gc_current_complete_field_arb import CompleteCurrentFieldArb
from fd2d_gc_current_accurate_domain_arb import (
    AccurateDomainCurrentFieldArb, ExactNormalizedCellPrimitive, digest)
from fd2d_gc_current_frozen_atlas_arb import FrozenAtlasArb
from fd2d_gc_r136_arb_profile import R136ArbProfile
from fd2d_gc_r136_bernstein_bumps import BernsteinBumpProfile
from fd2d_gc_dyadic_tail_archive_native import DyadicTailArchiveNativeField
from fd2d_gc_dyadic_tail_accurate_last_cell import DyadicTailAccurateLastCell

HERE = Path(__file__).resolve().parent
PARTS_SCHEMA = 'fd2d-R170-current-raw-interval-pieces-v1'
INTERIOR_SCHEMA = 'fd2d-R170-current-complete-interior-Arb-v1'
SCHEMA = 'fd2d-R170-current-complete-accurate-domain-Arb-v1'
FROZEN = {
    'fd2d_gc_current_native_interval.py':
        '8f4836a3926ce9f2e25d034b1b5489a3a719db38110458ef8267edcba326d6b1',
    'fd2d_gc_current_complete_field_arb.py':
        'c3dd41f4cf712f234dbde04456d31f8ef723f79bb76d807cb61ee6144d37a2fe',
    'fd2d_gc_current_accurate_domain_arb.py':
        '01600097f6bece6e8ba7ce56bb56bced28e832c0b8b58d5cf30cc0939ffc6c2c',
    'fd2d_gc_dyadic_tail_archive_native.py':
        'e4a5c9c30aff8bb008dda528da07f6a92b2d6a8f5d1c14487245c63b2e6230e8',
    'fd2d_gc_dyadic_tail_accurate_last_cell.py':
        '30401b51b3346405ba36544d17aadee8c1d389a26da4e506e799305ec37cb19f',
}


def checked_sources():
    result = []
    for name, expected in FROZEN.items():
        record = identity(HERE/name)
        if record['sha256'] != expected:
            raise ValueError('The inherited exact definition changed: '+name)
        result.append(record)
    return result


class DyadicTailIntervalPieces(CurrentNativeIntervalPieces):
    """Only the unchanged exact raw P1, scalar windows and bump polynomials.

    The legacy constructor and its positive-global-control decoder are not
    invoked.  The inherited binary-radius cut method is deliberately not an
    API of this new accurate constructor: use the complete domain's accurate
    cut method, whose constants are 4/5, 17/50 and 23/50.
    """
    def __init__(self, definition_path):
        sources = checked_sources()
        self.definition_path = Path(definition_path)
        self.original_definition = json.loads(self.definition_path.read_text())
        self.reader = DyadicTailArchiveNativeField.from_definition(self.definition_path)
        r = self.reader
        self.mesh = tuple(rational(v) for v in r.nodes)
        self.K, self.e, self.d = r.K, r.e, r.d
        self.coefficients = r.values
        self.parameters = tuple(rational(v) for v in r.parameters)
        self.profile_supports = tuple(tuple(rational(v) for v in row)
                                      for row in r.profile.supports)
        self.layout = r.explicit_parameter_layout
        self.entry, self.exit = map(rational, r.gauss_l_definition['support'])
        self.length = rational(r.coast_reference.length)
        self.rim = rational(float(r.coast_reference.length*r.reference_rim_fraction))
        self.trace_start, self.trace_stop, self.cut = (
            rational(r.positive_trace_definition[k]) for k in ('start','ramp_stop','cut'))
        self.tail_radius, self.tail_flat, self.tail_width = F(4,5), F(17,50), F(23,50)
        self._cell_cache = {}
        self.binding = dict(schema=PARTS_SCHEMA, source=identity(__file__),
            inherited_sources=sources,
            native_definition_identity=identity(self.definition_path),
            arrays_identity=identity(r.arrays_path),
            parameter_layout=self.layout,
            mesh_exact=[rational_pair(v) for v in self.mesh],
            tail_search_domain_kind=r.tail_search_domain_kind,
            tail_search_domain_definition=r.tail_search_domain_definition,
            tail_search_domain_certificate=r.tail.control_certificate,
            old_positive_global_control_constructor_invoked=False,
            mathematical_raw_corrections_changed=False,
            exact_rational_tail_constants=['4/5','17/50','23/50'])
        self.binding_sha256 = digest(self.binding)

    def definition(self):
        result = super().definition()
        result.update(schema=PARTS_SCHEMA, binding=self.binding,
            binding_sha256=self.binding_sha256,
            available_interval_parts=[
                'all actual saved P1 Fourier value/s/xi/xixi/sxi',
                'declared exact scalar quintic windows',
                'actual physical compact bump increments through derivative 3'],
            tail_interval_scope='Full rational tail is evaluated by the complete field, not this partial raw object',
            legacy_positive_global_control_constructor_invoked=False,
            saved_endpoint_is_accurate_physical_cut=False)
        return result

    def structural_partition(self):
        result = super().structural_partition()
        for point in result['points']:
            point['labels'] = ['saved_binary_cut_label' if name == 'accurate_cut' else name
                               for name in point['labels']]
        result['accurate_physical_endpoint_added_by_complete_domain'] = True
        return result

    def exact_cut_angular_box(self, *args, **kwargs):
        raise ValueError('Use DyadicTailAccurateDomainFieldArb.accurate_cut_angular(); '
                         'the raw-pieces saved endpoint is not the accurate physical S')


class DyadicTailCompleteInteriorArb(CompleteCurrentFieldArb):
    """R173's full analytic formulas on the saved interior, with R170 inputs."""
    def __init__(self, native_definition, profile_packet, *,
                 profile_packet_sha256, precision=256, atlas_options=None):
        ctx.prec = max(int(ctx.prec), int(precision))
        self.parts = DyadicTailIntervalPieces(native_definition)
        self.reader = self.parts.reader
        self.profile = R136ArbProfile.from_packet(profile_packet,
                                                expected_sha256=profile_packet_sha256)
        if self.profile.inputs['field_arrays']['sha256'] != identity(self.reader.arrays_path)['sha256']:
            raise ValueError('The accurate target and new-domain field must bind identical actual arrays')
        if self.profile.inputs['candidate']['sha256'] != identity(self.reader.candidate_path)['sha256']:
            raise ValueError('The accurate base candidate differs')
        if tuple(self.profile.delta) != tuple(self.parts.parameters[self.reader.profile_parameter_slice]):
            raise ValueError('The actual seven physical parameters differ')
        self.atlas = FrozenAtlasArb(self.parts, precision=precision,
                                   **({} if atlas_options is None else atlas_options))
        # The basis tag alone is never the domain identity. The explicit
        # archive constructor above has verified the R170 packet/certificate.
        self.tail_controls = tuple(self.parts.parameters[self.reader.tail_parameter_slice])
        self.saved_end = self.parts.mesh[-1]
        self.tail_start = rational(float(.42*float(self.saved_end)))
        self.tail_old_independent_width = rational(float(.58*float(self.saved_end)))
        self.tail_accurate_width = self.saved_end-self.tail_start
        self._binding = dict(schema=INTERIOR_SCHEMA, source=identity(__file__),
            inherited_sources=checked_sources(),
            native_definition=identity(native_definition),
            immutable_actual_arrays=identity(self.reader.arrays_path),
            raw_parts_binding_sha256=self.parts.binding_sha256,
            accurate_profile_packet=identity(profile_packet),
            profile_binding_sha256=self.profile.input_binding_sha256,
            full_atlas_binding_sha256=self.atlas.binding_sha256,
            complete_independent_layout=self.parts.layout,
            actual_mesh_exact=[rational_pair(q) for q in self.parts.mesh],
            accurate_tail_constants=dict(cut='4/5', flat='17/50', width='23/50'),
            actual_tail_controls=[rational_pair(q) for q in self.tail_controls],
            tail_search_domain_kind=self.reader.tail_search_domain_kind,
            tail_search_domain_definition=self.reader.tail_search_domain_definition,
            tail_search_domain_certificate=self.reader.tail.control_certificate,
            exact_tail_weight_endpoints=[rational_pair(self.tail_start),rational_pair(self.saved_end)],
            exact_tail_weight_width=rational_pair(self.tail_accurate_width),
            old_independent_float_tail_width=rational_pair(self.tail_old_independent_width),
            width_difference=rational_pair(self.tail_accurate_width-self.tail_old_independent_width),
            field_semantics='All R173 analytic formulas, all original controls and actual R170 archive; accurate target and atlas, not finite numeric interpolation',
            accurate_endpoint_extension_included=False,
            old_positive_global_control_constructor_invoked=False,
            old_numeric_sources_changed=False,
            old_numerical_samples_transferred_as_certificates=False)
        self.binding_sha256 = digest(self._binding)


class DyadicTailAccurateDomainFieldArb(AccurateDomainCurrentFieldArb):
    """Full saved mesh/atlas/windows plus the explicit accurate final cell.

    The inherited cell_box/primitive methods keep all physical U_s terms
    and true last-cell length S-b. The endpoint provides angular jets only.
    Nonpositive interval denominators remain unresolved, never replaced by
    the solver's finite evaluation floor.
    """
    def __init__(self, native_definition, profile_packet, *,
                 profile_packet_sha256, precision=256,
                 profile_backend='bernstein_bumps', atlas_options=None):
        self.interior = DyadicTailCompleteInteriorArb(native_definition,profile_packet,
            profile_packet_sha256=profile_packet_sha256,
            precision=precision,atlas_options=atlas_options)
        self.parts,self.reader,self.atlas = (
            self.interior.parts,self.interior.reader,self.interior.atlas)
        self.saved_mesh = self.parts.mesh
        self.last_cell = len(self.saved_mesh)-2
        if profile_backend == 'bernstein_bumps':
            tighter = BernsteinBumpProfile.from_packet(profile_packet,
                expected_sha256=profile_packet_sha256)
            if tighter.input_binding_sha256 != self.interior.profile.input_binding_sha256:
                raise ValueError('An enclosure backend may not alter the actual physical target')
            self.interior.profile = tighter
        elif profile_backend != 'original':
            raise ValueError('Unknown explicitly selected exact profile backend')
        self.profile = self.interior.profile
        self.terminal = DyadicTailAccurateLastCell(self.reader.arrays_path,profile_packet,
                                                  profile_sha256=profile_packet_sha256)
        if (self.terminal.b != self.saved_mesh[-2] or self.terminal.E != self.saved_mesh[-1]
                or self.terminal.profile.input_binding_sha256 != self.profile.input_binding_sha256
                or self.terminal.tail_control_certificate != self.reader.tail.control_certificate):
            raise ValueError('Complete interior, accurate terminal target and actual R170 domain differ')
        self.accurate_end = self.terminal.S
        self._binding = dict(schema=SCHEMA,source=identity(__file__),
            inherited_sources=checked_sources(),
            interior_binding_sha256=self.interior.binding_sha256,
            accurate_profile_definition=self.profile.definition(),
            profile_range_backend=profile_backend,
            terminal_definition=self.terminal.definition(),
            exact_saved_mesh=[rational_pair(q) for q in self.saved_mesh],
            final_cell=self.last_cell,
            tail_search_domain_kind=self.reader.tail_search_domain_kind,
            tail_search_domain_definition=self.reader.tail_search_domain_definition,
            tail_search_domain_certificate=self.reader.tail.control_certificate,
            complete_field_semantics='Saved accurate R173 interior through b; explicit R172 raw(sigma)+eta(sigma)*T(a(s),u), R155 K(s), complete R170 polynomial on final cell',
            physical_target_is_actual_rebound_packet=True,
            old27_delta_or_posterior_transferred=False,
            old_positive_global_control_constructor_invoked=False,
            accurate_rational_tail_constants=['4/5','17/50','23/50'],
            last_saved_cell_function_changed_explicitly=True,
            old_finite_residual_or_body_transferred=False,
            native_derivatives='physical s at fixed native xi; physical u through complete U_s/U_xi rule',
            cut_scope='Rational R132/R170 value/u/uu trace only; no invented radial II derivative',
            whole_surface_certificate=False)
        self.binding_sha256 = digest(self._binding)


__all__ = ['DyadicTailIntervalPieces','DyadicTailCompleteInteriorArb',
           'DyadicTailAccurateDomainFieldArb','ExactNormalizedCellPrimitive']
