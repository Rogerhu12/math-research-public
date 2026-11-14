"""Explicit R170 complete-field reader with a certified tail override.

The parent is loaded by its unchanged, legitimate native decoder. Its saved
arrays and sources remain intact. A separately declared new field replaces
only the tail block and all copies of its plain lifting by the new R170
class. No negative controls are submitted to an old archive guard, no class
is renamed, and no old schema is assigned to the resulting field.

This is a field/body factory, not a modification of a solver's domain or
QP. Existing finite solvers need an explicit new domain integration before
they can use negative global controls.
"""
from __future__ import annotations
import copy
from hashlib import sha256
import json
from pathlib import Path
import numpy as np
from fd2d_gc_raw_native_field import identity, locate_bound
from fd2d_gc_independent_tail_native_field import (
    IndependentTailPositiveTraceNativeField, SCHEMA as PARENT_SCHEMA)
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField
from fd2d_dyadic_bernstein_tail import DyadicBernsteinFlatDevelopableFamily

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-complete-parent-native-with-dyadic-Bernstein-tail-v1'
BODY_SCHEMA = 'fd2d-dyadic-tail-native-angular-body-view-v1'


def array_identity(value):
    value = np.asarray(value)
    return dict(shape=list(value.shape), dtype=value.dtype.str,
        c_order_bytes_sha256=sha256(value.tobytes(order='C')).hexdigest())


class DyadicBernsteinTailNativeField(PositiveTraceNativeField):
    def __init__(self, parent_definition, controls):
        parent_path = Path(parent_definition)
        parent_meta = json.loads(parent_path.read_text())
        if parent_meta.get('schema') != PARENT_SCHEMA:
            raise ValueError('This explicit override requires the independent-tail complete parent schema')
        parent = IndependentTailPositiveTraceNativeField.from_definition(parent_path)
        if parent.tail_parameter_count != 16:
            raise ValueError('The R170 domain has exactly 16 tail controls')
        # Build a different, explicitly defined field; do not mutate parent,
        # its archive, or its frozen evaluation sources.
        self.__dict__.update(parent.__dict__)
        self._parent_definition_path = parent_path
        self._parent_definition_metadata = parent_meta
        self._parent_definition_input = identity(parent_path)
        self._parent_parameters = parent.parameters
        old_tail = parent.tail
        self.tail = DyadicBernsteinFlatDevelopableFamily(controls,
            cut_radius=old_tail.cut_radius, flat_radius=old_tail.flat_radius,
            cuff_radius=old_tail.cuff_radius, plane_height=old_tail.plane_height,
            quadrature_order=old_tail.quadrature_order,
            quadrature_chunk=old_tail.quadrature_chunk)
        self.parameters = parent.parameters.copy()
        self.parameters[self.tail_parameter_slice] = self.tail.coefficients
        self.parameters.flags.writeable = False
        self._inverse_seed_cache = {}
        self.tail_domain_kind = 'degree15_eight_dyadic_Bernstein_box'
        # This old string selects the already frozen polynomial derivative
        # formula in curvature_second_y. It is NOT a class/domain identity.
        self.tail_kind = 'positive_bernstein'
        self.representation_kind = 'complete_parent_native_with_explicit_dyadic_tail_override_v1'
        plain = copy.copy(parent._plain_lifting_view)
        plain.tail = self.tail
        plain.parameters = self.parameters
        plain.tail_kind = self.tail_kind
        plain.tail_domain_kind = self.tail_domain_kind
        plain.representation_kind = self.representation_kind
        plain._inverse_seed_cache = {}
        self._plain_lifting_view = plain
        # The new exact-cut guard has precisely the same geometric premise:
        # the actual tail is PSD. R170 certifies that premise from P>=0,
        # rather than from the strictly stronger global coefficient box.
        if not np.all(self.values[-1] == 0.):
            raise ValueError('The complete cut correction must still be exactly zero')
        if self.profile.jet([self.trace_cut])['K'][0] != 0.:
            raise ValueError('The parent must still supply its explicitly flat cut')
        if not self.tail.control_certificate['passed']:
            raise ValueError('The declared polynomial must have the exact R170 certificate')
        self.positive_trace_definition = copy.deepcopy(parent.positive_trace_definition)
        self.positive_trace_definition['tail_contract'] = (
            'Cut raw correction is exactly zero; the new R170 eight-piece '
            'Bernstein certificate gives 0<=P<=6/5 and hence the actual PSD tail trace')
        self.positive_trace_definition['tail_domain_override'] = self.tail.control_box.definition()
        self.positive_trace_definition['cut_guard_source_sha256'] = identity(__file__)['sha256']
        self._minimum_sampled_active_n = None
        self._maximum_consumed_abs_K_s = 0.
        self._maximum_terminal_abs_K_s = 0.

    def definition(self):
        parent = self._parent_definition_metadata
        return dict(schema=SCHEMA,
            class_name=type(self).__module__+'.'+type(self).__name__,
            sources=[identity(HERE/name) for name in (
                'fd2d_gc_dyadic_tail_native.py','fd2d_dyadic_bernstein_tail.py')],
            parent_definition_input=self._parent_definition_input,
            complete_parent_definition=parent,
            tail_override=self.tail.definition(),
            actual_parameter_layout=self.explicit_parameter_layout,
            actual_arrays={key:array_identity(value) for key,value in (
                ('mesh',self.nodes),('corrections',self.values),('parameters',self.parameters))},
            parameter_override_slice=[self.tail_parameter_slice.start,self.tail_parameter_slice.stop],
            same_field_as_parent=bool(np.array_equal(self.parameters, self._parent_parameters)),
            raw_central_profile_metric_atlas_and_windows_unchanged=True,
            tail_parameters_and_plain_lifting_replaced_together=True,
            parent_archive_rewritten=False, old_decoder_given_negative_controls=False,
            old_class_or_schema_identity_forged=False,
            tail_evaluator_basis_tag=self.tail_kind,
            tail_evaluator_basis_tag_is_not_domain_or_class_identity=True,
            positive_trace_definition=self.positive_trace_definition,
            exact_cut_scope='Actual values and angular two-jet; no radial II derivative is invented',
            native_jet_methods='Frozen PositiveTraceNativeField inherited without modification',
            domain_scope=('R170 proves the tail control domain and its inherited tail geometry. '
                'No prefix Gauss/Codazzi/metric/reach/held or seam certificate is transferred. '
                'The original active-coast evaluation checks remain in force.'),
            solver_or_finite_objective_created=False)

    @classmethod
    def from_definition(cls, path):
        path = Path(path)
        meta = json.loads(path.read_text())
        if meta.get('schema') != SCHEMA:
            raise ValueError('Require the explicit R170 complete-field schema')
        for row in meta['sources']:
            locate_bound(path, row)
        parent_path = locate_bound(path, meta['parent_definition_input'])
        if json.loads(parent_path.read_text()) != meta['complete_parent_definition']:
            raise ValueError('The complete embedded parent definition is not its bound input')
        tail = DyadicBernsteinFlatDevelopableFamily.from_definition(meta['tail_override'], owner=path)
        obj = cls(parent_path, tail.coefficients)
        expected = obj.definition()
        for key in expected:
            if key not in ('sources','parent_definition_input','tail_override'):
                if meta.get(key) != expected[key]:
                    raise ValueError('Changed explicit complete-field definition: '+key)
        # Geometry, polynomial, controls and domain must agree even when
        # a source file has been relocated without changing its bytes.
        for key in expected['tail_override']:
            if key != 'sources' and meta['tail_override'].get(key) != expected['tail_override'][key]:
                raise ValueError('Changed tail override: '+key)
        return obj


class DyadicTailBodyAngularView:
    def __init__(self, native):
        if type(native) is not DyadicBernsteinTailNativeField:
            raise TypeError('Require the distinct, explicitly validated R170 native class')
        self.native = native

    def __getattr__(self, name):
        return getattr(self.native, name)

    def physical(self, x, u, *, side='right'):
        return self.native.physical_angular(x, u, side=side)

    def definition(self):
        return self.native.definition()

    def body_adapter_definition(self):
        return dict(schema=BODY_SCHEMA, source=identity(__file__), native_schema=SCHEMA,
            dispatch='native.physical_angular(x,u,side=side)',
            exact_cut_radial_scope_extended=False, actual_saved_mesh_retained=True,
            original_body_ODE_and_actual_twojet_formulas_unchanged=True,
            body_ODE_run_by_factory=False)


def load_dyadic_tail_body_reader(definition):
    """Explicit new body dispatch; existing old-schema factories stay unchanged."""
    return DyadicTailBodyAngularView(DyadicBernsteinTailNativeField.from_definition(definition))
