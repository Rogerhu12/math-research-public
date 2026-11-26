#!/usr/bin/env python3
"""Complete same-field signed meridian integrals with outward error fees.

Consumes the complete a846 whole-cell/all-angle envelope and the 1371 actual
node evaluator. Every original integration node, signed partial weight and
working-width word is kept. Exact rational reconstruction separates integral
error from later closure/field arithmetic. This is not a core, Gram or reach
certificate. Scientific execution is only in public repository Actions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid
import numpy as np

SCHEMA = 'complete-same-field-signed-SO3-meridian-integral-fees-v1'
CELL_SCHEMA = 'complete-same-field-signed-SO3-integral-node-cell-v1'
REQUEST_SCHEMA = 'same-field-signed-SO3-integral-literal-requests-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
NODE_RELATIVE = 'scripts/resume_20261126/so3_axisymmetric_outward_nodes.py'
NODE_SHA = '1371e4936af27d2122a84bb720e8c67db5d0db712df42eec12a4579f91943f89'
CONTINUOUS_SHA = 'a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6'
LOW_ORDER_SHA = '30ae7dc70ea836ab6f30e34b9b886f968c6e61c6646c807cd96a8611029c2636'
OPERATOR_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
ENVELOPE_SCHEMA = 'continuous-direct-R690-SO3-integrand-input-bounds-v1'
KEYS = ('T', 'Tp', 'Tpp')
BOUND_NAMES = {
    'T': ('T_norm', 'T_radial_Lipschitz'),
    'Tp': ('Tphi_norm', 'Tphi_radial_Lipschitz'),
    'Tpp': ('Tphiphi_norm', 'Tphiphi_radial_Lipschitz'),
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific signed integrals require this public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, np.ndarray):
        return serialize(value.tolist())
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        value = float(value)
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Nonfinite scientific values cannot be serialized')
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialize(item) for item in value]
    return value


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(serialize(value), indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def load(name, path, expected):
    if sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def fraction_array(values, shape, *, nonnegative=False):
    array = np.asarray(values, dtype=object)
    if array.shape != shape:
        raise ValueError('Wrong complete rational array shape')
    result = np.empty(shape, dtype=object)
    for index in np.ndindex(shape):
        result[index] = F(array[index])
        if nonnegative and result[index] < 0:
            raise ValueError('An error bound cannot be negative')
    return result


def float_hex_array(values):
    return np.vectorize(lambda value: float(value).hex(), otypes=[object])(values).tolist()


def read_float_hex_array(node, values, shape):
    raw = np.asarray(values, dtype=object)
    if raw.shape != shape:
        raise ValueError('Wrong complete working-vector shape')
    result = np.empty(shape, dtype=np.float64)
    for index in np.ndindex(shape):
        result[index] = node.literal_float(raw[index])
    return result


def exact_vector_sum(terms):
    result = [F(0), F(0), F(0)]
    for coefficient, vector in terms:
        coefficient = F(coefficient)
        for j in range(3):
            value = vector[j]
            rational = F(float(value)) if isinstance(value, (float, np.floating)) else F(value)
            result[j] += coefficient*rational
    return tuple(result)


class SignedMeridianIntegrals:
    """Complete-cell actual integration data and arbitrary signed queries.

    Keys T/Tp/Tpp denote the three angular orders. Public array shapes:
      integrated_working[key] : float64((J-1)*Q,A,3)
      integrated_error[key]   : Fraction((J-1)*Q,A)
      cell_exact[key]         : Fraction(J-1,A,3)
      cell_error[key]         : Fraction(J-1,A)
      prefix_exact[key]       : Fraction(J,A,3)
      prefix_error[key]       : Fraction(J,A)
      total_exact[key]        : Fraction(A,3), only after complete prepare
      total_error[key]        : Fraction(A), only after complete prepare
    """
    def __init__(self, actual, node, *, envelope_report, envelope_journal):
        require_actions()
        node_module = sys.modules.get(node.__class__.__module__)
        actual_module = sys.modules.get(actual.__class__.__module__)
        if (node_module is None or sha(node_module.__file__) != NODE_SHA
                or actual_module is None or sha(actual_module.__file__) != CONTINUOUS_SHA
                or node.actual is not actual):
            raise ValueError('Use the complete 1371 node evaluator with its actual a846 input')
        self.actual, self.node, self.q = actual, node, node.q
        self.node_module, self.continuous, self.kernel = node_module, actual_module, node.kernel
        if (sha(actual.paths['operator']) != OPERATOR_SHA
                or sha(actual.paths['low_order']) != LOW_ORDER_SHA
                or self.q.model != actual.model or self.q.identity != actual.identity):
            raise ValueError('The complete integral field or mathematical error kernel changed')
        self.C, self.Q = self.q.J-1, self.q.integration_order
        self.gauss_u = np.array(self.q.gauss_u, dtype=np.float64, copy=True)
        self.gauss_w = np.array(self.q.gauss_w, dtype=np.float64, copy=True)
        self.width_words = np.array(np.diff(self.q.mesh), dtype=np.float64, copy=True)
        if (self.gauss_u.shape != (self.Q,) or self.gauss_w.shape != (self.Q,)
                or not np.isfinite(self.gauss_u).all() or not np.isfinite(self.gauss_w).all()
                or np.any(self.gauss_u < 0) or np.any(self.gauss_u > 1)
                or np.any(self.gauss_w <= 0) or np.any(self.width_words <= 0)
                or not np.array_equal(self.q.integration_cells, np.repeat(np.arange(self.C), self.Q))
                or not np.array_equal(self.q.integration_u, np.tile(self.gauss_u, self.C))):
            raise ValueError('Retain every actual complete working quadrature node and positive whole weight')
        for array in (self.gauss_u, self.gauss_w, self.width_words):
            array.setflags(write=False)
        self.nodes_exact = tuple(F(float(v)) for v in self.gauss_u)
        self.weights_exact = tuple(F(float(v)) for v in self.gauss_w)
        self.widths_exact = tuple(F(float(v)) for v in self.width_words)
        self.envelope_report_path = Path(envelope_report)
        self.envelope_journal_path = Path(envelope_journal)
        self.bounds, self.envelope_identity = self._read_envelope()
        self.whole_peano = self.kernel.peano_functional(self.nodes_exact, self.weights_exact)
        self.binding = dict(schema=SCHEMA, source_sha256=sha(__file__),
            node_source_sha256=NODE_SHA, continuous_source_sha256=CONTINUOUS_SHA,
            low_order_source_sha256=LOW_ORDER_SHA, actual_operator_source_sha256=OPERATOR_SHA,
            actual=actual.binding, node_binding_identity_sha256=canonical(node.binding),
            envelope_identity=self.envelope_identity,
            actual_gauss_u_hex=[float(v).hex() for v in self.gauss_u],
            actual_gauss_w_hex=[float(v).hex() for v in self.gauss_w],
            actual_integrator_width_hex=[float(v).hex() for v in self.width_words],
            original_complete_cells=self.C, original_complete_nodes_per_cell=self.Q,
            exact_scalar_and_rotation_coefficients_unchanged=True,
            whole_quadrature_reconstruction='literal np.diff(mesh)*sum(literal gauss_w*actual meridian words), all rational',
            signed_definition='hhat*integral_0^s Tj -(1-hhat)*integral_s^S Tj',
            hhat_and_one_minus_hhat_are_exact_rationals_of_one_actual_h_word=True,
            current_cell_normalization='actual query.partial / literal complete-integrator width',
            signed_weights_and_nonzero_mass_retained=True,
            prior_solver_batches_not_assumed_bitwise_identical=True,
            closure_field_Gram_and_geometry_not_in_this_component=True)
        self.phi = None
        self.complete, self.completed_cells = False, 0
        self.integrated_working, self.integrated_error = {}, {}
        self.cell_exact, self.cell_error = {}, {}
        self.prefix_exact, self.prefix_error = {}, {}
        self.total_exact, self.total_error = {}, {}
        self._journal_directory = None
        self._journal_entries = []
        self._journal_chain = None
        self._angle_identity = None
        self._current_read_identity = None
        self.counts = dict(new_node_cells=0, restored_node_cells=0, recovered_atomic_node_cells=0,
            new_node_vectors=0, signed_queries=0, signed_query_vectors=0,
            whole_cell_error_kernel_calls=0, signed_cell_error_kernel_calls=0,
            closure_reads=0, full_F_reads=0, full_J_reads=0, full_Jtranspose_reads=0)
        self.source_commit = subprocess.check_output(
            ['git', '-C', str(actual.repo), 'rev-parse', 'HEAD'], text=True).strip()

    def _read_envelope(self):
        report = json.loads(self.envelope_report_path.read_text())
        if (report.get('schema') != ENVELOPE_SCHEMA or report.get('source_sha256') != CONTINUOUS_SHA
                or report.get('complete') is not True or report.get('all_original_cells_completed') is not True
                or report.get('all_angles_enclosed') is not True
                or report.get('completed_cells') != self.C or report.get('total_cells') != self.C
                or report.get('binding') != self.actual.binding):
            raise ValueError('Use the complete same-actual-field all-cell/all-angle a846 envelope report')
        identity = report.get('identity', {})
        if (identity.get('schema') != ENVELOPE_SCHEMA or identity.get('source_sha256') != CONTINUOUS_SHA
                or identity.get('bound_input_identity_sha256') != canonical(self.actual.binding)
                or identity.get('integer_scale') != str(self.node.d.SCALE)
                or identity.get('sqrt_dyadic_bits') != 96
                or canonical(identity) != report.get('identity_sha256')):
            raise ValueError('The complete envelope identity differs from this exact actual field')
        subdivisions = identity.get('subdivisions')
        if not isinstance(subdivisions, int) or subdivisions < 1:
            raise ValueError('The entire envelope needs a declared positive complete subdivision')
        if (report['journal']['sha256'] != sha(self.envelope_journal_path)
                or report['journal']['bytes'] != self.envelope_journal_path.stat().st_size):
            raise ValueError('The actual complete envelope journal bytes differ')
        for role, record in report['source_records'].items():
            if role not in self.actual.paths or record['sha256'] != sha(self.actual.paths[role]):
                raise ValueError('A complete envelope dependency differs: '+role)
        if set(report['source_records']) != set(self.actual.paths):
            raise ValueError('Retain every envelope source role')
        if (report['evaluator'].get('complete_actual_omega_modes') != self.actual.n
                or report['evaluator'].get('fixed_chart_used') is not True
                or report['evaluator'].get('current_core_never_substituted_for_fixed_chart') is not True):
            raise ValueError('The envelope must retain all modes on the actual fixed chart')
        chain, bounds = report['identity_sha256'], []
        with self.envelope_journal_path.open() as stream:
            for line in stream:
                entry = json.loads(line)
                row = entry['record']
                cell = len(bounds)
                if (cell >= self.C or row.get('cell') != cell
                        or entry.get('previous_record_identity_sha256') != chain
                        or entry.get('record_identity_sha256') != canonical(dict(previous=chain, record=row))):
                    raise ValueError('The complete envelope journal has a changed, missing or reordered cell')
                chain = entry['record_identity_sha256']
                if (row.get('whole_exact_cell') is not True or row.get('all_angles') is not True
                        or row.get('scalar_whole_interval_not_point_query') is not True
                        or row.get('angular_sample_grid_used') is not False
                        or len(row['subintervals']) != subdivisions):
                    raise ValueError('Every envelope cell must cover its entire exact radial/angular domain')
                for index, piece in enumerate(row['subintervals']):
                    low, high = F(index, subdivisions), F(index+1, subdivisions)
                    expected = [self.continuous.affine(self.actual.context.nodes, cell, u) for u in (low, high)]
                    if (list(map(F, piece['local_exact'])) != [low, high]
                            or [[F(v) for v in pair] for pair in piece['exact_affine_endpoints']]
                            != [list(pair) for pair in expected]):
                        raise ValueError('The complete exact envelope partition or physical endpoints changed')
                B, L = {}, {}
                for j, key in enumerate(KEYS):
                    value_name, derivative_name = BOUND_NAMES[key]
                    B[key], L[key] = F(row['B'][j]), F(row['L'][j])
                    if (B[key] < 0 or L[key] < 0 or B[key] != F(row['meridian'][value_name])
                            or L[key] != F(row['meridian'][derivative_name])
                            or B[key] != max(F(piece['meridian'][value_name]) for piece in row['subintervals'])
                            or L[key] != max(F(piece['meridian'][derivative_name]) for piece in row['subintervals'])):
                        raise ValueError('The complete whole-cell B/L maxima are inconsistent')
                if B['T'] != 1:
                    raise ValueError('The same exact rotated unit meridian must retain B0=1')
                width_record = row['complete_physical_width']
                recorded = self.node.d.box(F(width_record['lower_exact']), F(width_record['upper_exact']))
                fresh = self.node.scalar.width_box(self.actual.context.nodes[cell], self.actual.context.nodes[cell+1])
                width = self.node.d.intersect(recorded, fresh)
                physical_width = (F(width[0], self.node.d.SCALE), F(width[1], self.node.d.SCALE))
                if (physical_width[0] <= 0 or row['numerical_width_carrier_hex'] != float(self.width_words[cell]).hex()):
                    raise ValueError('The exact complete cell width or actual working width changed')
                bounds.append(dict(B=B, L=L, physical_width=physical_width,
                    envelope_record_identity_sha256=chain))
        if (len(bounds) != self.C or chain != report['final_journal_chain_sha256']
                or report.get('partial_bounds_not_promoted_to_full_domain') is not False):
            raise ValueError('Every original exact cell must be completed before integral assembly')
        return bounds, dict(report=file_record(self.envelope_report_path),
            journal=file_record(self.envelope_journal_path), identity_sha256=report['identity_sha256'],
            final_chain_sha256=chain, complete_cells=self.C, all_angles=True,
            subdivisions=subdivisions, source_sha256=CONTINUOUS_SHA)

    def _assert_working_rule(self):
        if (not np.array_equal(self.q.gauss_u, self.gauss_u)
                or not np.array_equal(self.q.gauss_w, self.gauss_w)
                or not np.array_equal(np.diff(self.q.mesh), self.width_words)
                or self.q.integration_order != self.Q or self.q.model != self.actual.model):
            raise ValueError('The complete actual working integration rule changed after binding')

    def _initialize_angle(self, phi):
        raw = np.asarray(phi)
        if raw.ndim != 1 or not len(raw):
            raise ValueError('Use a nonempty one-dimensional literal angle block')
        angles = np.empty(len(raw), dtype=np.float64)
        for index, value in enumerate(raw):
            rational = self.node_module.exact(value)
            word = float(value)
            if not math.isfinite(word) or F(word) != rational:
                raise ValueError('prepare requires literal binary64 angles')
            angles[index] = word
        angles.setflags(write=False)
        if (self.phi is not None and [float(v).hex() for v in self.phi]
                == [float(v).hex() for v in angles]):
            return False
        if self.phi is not None and not self.complete and self.completed_cells and self._journal_directory is None:
            raise ValueError('Persist or finish the current partial angle block before replacing its paid nodes')
        self.phi = angles
        A = len(angles)
        self.complete, self.completed_cells = False, 0
        self.integrated_working = {key: np.empty((self.C*self.Q, A, 3), dtype=np.float64) for key in KEYS}
        self.integrated_error = {key: np.empty((self.C*self.Q, A), dtype=object) for key in KEYS}
        self.cell_exact = {key: np.empty((self.C, A, 3), dtype=object) for key in KEYS}
        self.cell_error = {key: np.empty((self.C, A), dtype=object) for key in KEYS}
        self.prefix_exact = {key: np.empty((self.C+1, A, 3), dtype=object) for key in KEYS}
        self.prefix_error = {key: np.empty((self.C+1, A), dtype=object) for key in KEYS}
        self.total_exact = {key: None for key in KEYS}
        self.total_error = {key: None for key in KEYS}
        for key in KEYS:
            self.prefix_exact[key][0] = F(0)
            self.prefix_error[key][0] = F(0)
        self._angle_identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
            binding_identity_sha256=canonical(self.binding), phi_hex=[float(v).hex() for v in angles],
            original_nodes_per_cell=self.Q, original_complete_cells=self.C)
        self._journal_chain = canonical(self._angle_identity)
        self._journal_entries = []
        self._journal_directory = None
        self._current_read_identity = None
        return True

    def _cell_data(self, cell, working, errors):
        """Exact rational reconstruction; no floating reduction error is asserted."""
        A = len(self.phi)
        exacts, fees = {}, {}
        bound, width = self.bounds[cell], self.widths_exact[cell]
        for key in KEYS:
            if (working[key].shape != (self.Q, A, 3) or errors[key].shape != (self.Q, A)
                    or not np.isfinite(working[key]).all()):
                raise ValueError('A full cell must retain every real working node and error')
            exacts[key] = np.empty((A, 3), dtype=object)
            fees[key] = np.empty(A, dtype=object)
            for a in range(A):
                exacts[key][a] = exact_vector_sum((width*w, working[key][j, a])
                    for j, w in enumerate(self.weights_exact))
                result = self.kernel.quadrature_error(self.whole_peano,
                    physical_width=bound['physical_width'], width_carrier=width,
                    value_norm_upper=bound['B'][key], radial_derivative_norm_upper=bound['L'][key],
                    node_value_errors=[errors[key][j, a] for j in range(self.Q)], arithmetic_error=F(0))
                fees[key][a] = result['upper_error']
                self.counts['whole_cell_error_kernel_calls'] += 1
        return exacts, fees

    def _accept_cell(self, cell, working, errors, exacts, fees):
        if cell != self.completed_cells:
            raise ValueError('Accept full cells only in the original contiguous order')
        section = slice(cell*self.Q, (cell+1)*self.Q)
        for key in KEYS:
            self.integrated_working[key][section] = working[key]
            self.integrated_error[key][section] = errors[key]
            self.cell_exact[key][cell] = exacts[key]
            self.cell_error[key][cell] = fees[key]
            self.prefix_exact[key][cell+1] = self.prefix_exact[key][cell]+exacts[key]
            self.prefix_error[key][cell+1] = self.prefix_error[key][cell]+fees[key]
        self.completed_cells += 1
        self.complete = self.completed_cells == self.C
        if self.complete:
            for key in KEYS:
                self.total_exact[key] = np.array(self.prefix_exact[key][-1], copy=True)
                self.total_error[key] = np.array(self.prefix_error[key][-1], copy=True)
                self.total_exact[key].setflags(write=False)
                self.total_error[key].setflags(write=False)
                for collection in (self.integrated_working, self.integrated_error, self.cell_exact,
                        self.cell_error, self.prefix_exact, self.prefix_error):
                    collection[key].setflags(write=False)

    def _payload(self, cell, working, errors, exacts, fees, node_counts):
        return dict(schema=CELL_SCHEMA, source_sha256=sha(__file__),
            source_commit=self.source_commit, node_source_sha256=NODE_SHA,
            angle_identity_sha256=canonical(self._angle_identity), cell=cell,
            exact_original_local_nodes=[str(v) for v in self.nodes_exact],
            phi_hex=[float(v).hex() for v in self.phi],
            actual_checkpoint_sha256=self.actual.inputs['checkpoint']['sha256'],
            envelope_record_identity_sha256=self.bounds[cell]['envelope_record_identity_sha256'],
            working_hex={key: float_hex_array(working[key]) for key in KEYS},
            node_norm_error_upper=serialize(errors),
            cell_exact=serialize(exacts), cell_error=serialize(fees),
            node_binding_identity_sha256=canonical(self.node.binding),
            node_counts_after_actual_read=node_counts,
            complete_cell_nodes=True, no_integral_arithmetic_error_assumed_zero=True,
            exact_rational_quad_has_no_additional_floating_reduction=True)

    def _read_payload(self, path, cell):
        payload = json.loads(gzip.decompress(Path(path).read_bytes()))
        if (payload.get('schema') != CELL_SCHEMA or payload.get('source_sha256') != sha(__file__)
                or payload.get('node_source_sha256') != NODE_SHA
                or payload.get('angle_identity_sha256') != canonical(self._angle_identity)
                or payload.get('cell') != cell or payload.get('complete_cell_nodes') is not True
                or payload.get('actual_checkpoint_sha256') != self.actual.inputs['checkpoint']['sha256']
                or payload.get('node_binding_identity_sha256') != canonical(self.node.binding)
                or payload.get('envelope_record_identity_sha256') != self.bounds[cell]['envelope_record_identity_sha256']
                or payload.get('exact_original_local_nodes') != [str(v) for v in self.nodes_exact]
                or payload.get('phi_hex') != [float(v).hex() for v in self.phi]):
            raise ValueError('A persisted exact-node cell belongs to another actual read or field')
        A = len(self.phi)
        working = {key: read_float_hex_array(self.node_module, payload['working_hex'][key], (self.Q, A, 3)) for key in KEYS}
        errors = {key: fraction_array(payload['node_norm_error_upper'][key], (self.Q, A), nonnegative=True) for key in KEYS}
        exacts, fees = self._cell_data(cell, working, errors)
        for key in KEYS:
            saved_exact = fraction_array(payload['cell_exact'][key], (A, 3))
            saved_fee = fraction_array(payload['cell_error'][key], (A,), nonnegative=True)
            if not np.array_equal(saved_exact, exacts[key]) or not np.array_equal(saved_fee, fees[key]):
                raise ValueError('The saved rational quadrature or complete fee changed')
        return payload, working, errors, exacts, fees

    def _state(self):
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            angle_identity=self._angle_identity,
            angle_identity_sha256=canonical(self._angle_identity),
            binding_identity_sha256=canonical(self.binding),
            complete=self.complete, completed_cells=self.completed_cells, total_cells=self.C,
            paid_node_vectors=self.completed_cells*self.Q*len(self.phi),
            all_total_integrals_available=self.complete,
            exact_total_three_jet_reconstruction=serialize(self.total_exact) if self.complete else None,
            total_error_maxima={key: str(max(self.total_error[key])) for key in KEYS} if self.complete else None,
            current_read_identity_sha256=self._current_read_identity,
            raw_cell_files=len(self._journal_entries),
            raw_cell_bytes=sum(entry['record']['payload']['bytes'] for entry in self._journal_entries),
            final_journal_chain_sha256=self._journal_chain,
            actual_counts=dict(self.counts), actual_counts_are_this_execution_only=True,
            partial_cells_not_promoted_to_total_integrals=not self.complete,
            closure_field_Gram_or_geometry_certified=False)

    def _write_state(self):
        if self._journal_directory is None:
            return
        write_json(self._journal_directory/'state.json', self._state())

    def _append_raw(self, record):
        next_chain = canonical(dict(previous=self._journal_chain, record=record))
        entry = dict(previous_record_identity_sha256=self._journal_chain,
            record_identity_sha256=next_chain, record=record)
        self._journal_entries.append(entry)
        self._journal_chain = next_chain
        if self._journal_directory is not None:
            path = self._journal_directory/'cells.jsonl'
            temporary = path.with_name(path.name+'.partial')
            with temporary.open('w') as stream:
                for item in self._journal_entries:
                    stream.write(json.dumps(item, separators=(',', ':'), allow_nan=False)+'\n')
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(path)
        self._current_read_identity = canonical(dict(angle=self._angle_identity,
            completed_cells=self.completed_cells, journal_chain=self._journal_chain))
        self._write_state()

    def _attach_journal(self, directory, resume):
        if directory is None:
            return
        directory = Path(directory).resolve()
        if directory == self.actual.repo or self.actual.repo in directory.parents:
            raise ValueError('Raw paid node data must remain outside the Git repository')
        if self._journal_directory is not None:
            if directory != self._journal_directory:
                raise ValueError('Do not switch the current angle block to another raw journal')
            return
        if self.completed_cells:
            raise ValueError('Attach a persistent journal before paying the first cell')
        header_path, journal_path = directory/'identity.json', directory/'cells.jsonl'
        if directory.exists():
            if not resume or not header_path.is_file() or not journal_path.is_file():
                raise ValueError('An existing raw directory needs an explicit complete journal resume')
            if json.loads(header_path.read_text()) != self._angle_identity:
                raise ValueError('The persisted angle block has another complete identity')
        else:
            if resume:
                raise ValueError('Resume requires the existing exact raw directory')
            directory.mkdir(parents=True)
            write_json(header_path, self._angle_identity)
            journal_path.write_text('')
        self._journal_directory = directory
        with journal_path.open() as stream:
            for line in stream:
                entry = json.loads(line)
                record = entry['record']
                cell = self.completed_cells
                if (cell >= self.C or record.get('cell') != cell
                        or entry.get('previous_record_identity_sha256') != self._journal_chain
                        or entry.get('record_identity_sha256') != canonical(dict(previous=self._journal_chain, record=record))):
                    raise ValueError('The paid-node journal has a changed, missing or reordered cell')
                path = directory/('cell-'+str(cell).zfill(4)+'.json.gz')
                if (record['payload']['sha256'] != sha(path)
                        or record['payload']['bytes'] != path.stat().st_size):
                    raise ValueError('A saved full scientific node cell changed bytes')
                _, working, errors, exacts, fees = self._read_payload(path, cell)
                self._accept_cell(cell, working, errors, exacts, fees)
                self._journal_entries.append(entry)
                self._journal_chain = entry['record_identity_sha256']
                self.counts['restored_node_cells'] += 1
        self._current_read_identity = canonical(dict(angle=self._angle_identity,
            completed_cells=self.completed_cells, journal_chain=self._journal_chain))
        self._write_state()

    def prepare(self, phi, *, journal_directory=None, resume=False,
                admission_seconds=None, progress=None):
        """Pay complete cells until full preparation or a natural budget return.

        A partial return has complete=False and never exposes total integrals.
        Repeating this method on the same object continues without new reads of
        paid cells. A new process restores exact raw cells with resume=True.
        """
        require_actions()
        if admission_seconds is not None and (not math.isfinite(admission_seconds) or admission_seconds < 0):
            raise ValueError('Use a finite nonnegative natural budget, or None')
        started = time.monotonic()
        self._assert_working_rule()
        self._initialize_angle(phi)
        self._attach_journal(journal_directory, resume)
        initial = self.completed_cells
        while self.completed_cells < self.C:
            if admission_seconds is not None and time.monotonic()-started >= admission_seconds:
                break
            cell = self.completed_cells
            path = None if self._journal_directory is None else (
                self._journal_directory/('cell-'+str(cell).zfill(4)+'.json.gz'))
            if path is not None and path.exists():
                # An atomic complete chunk may precede the journal rename if
                # a process was interrupted. Rebind it before adopting it.
                _, working, errors, exacts, fees = self._read_payload(path, cell)
                origin = 'recovered complete atomic raw cell after interrupted journal commit'
                self.counts['recovered_atomic_node_cells'] += 1
            else:
                result = self.node.evaluate(np.full(self.Q, cell, dtype=np.int64), self.gauss_u, self.phi)
                working = {key: result['working'][key] for key in KEYS}
                errors = {key: result['norm_error_upper'][key] for key in KEYS}
                exacts, fees = self._cell_data(cell, working, errors)
                payload = self._payload(cell, working, errors, exacts, fees, dict(self.node.counts))
                if path is not None:
                    raw = json.dumps(serialize(payload), sort_keys=True, separators=(',', ':'),
                        allow_nan=False).encode()
                    temporary = path.with_name(path.name+'.partial')
                    temporary.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
                    temporary.replace(path)
                origin = 'new complete actual 1371 meridian-node read'
                self.counts['new_node_cells'] += 1
                self.counts['new_node_vectors'] += self.Q*len(self.phi)
            self._accept_cell(cell, working, errors, exacts, fees)
            if path is None:
                content_identity = canonical(dict(
                    working_hex={key: float_hex_array(working[key]) for key in KEYS},
                    node_norm_error_upper=serialize(errors), cell_exact=serialize(exacts),
                    cell_error=serialize(fees)))
                record = dict(cell=cell, origin=origin, in_memory_cell_identity_sha256=content_identity,
                    payload=dict(path=None, sha256=content_identity, bytes=0))
            else:
                record = dict(cell=cell, origin=origin, payload=file_record(path))
            self._append_raw(record)
            if progress is not None:
                progress(dict(event='complete_actual_integral_node_cell', cell=cell,
                    completed_cells=self.completed_cells, total_cells=self.C, origin=origin,
                    actual_seconds=time.monotonic()-started))
        self._write_state()
        return dict(complete=self.complete, completed_cells=self.completed_cells, total_cells=self.C,
            newly_completed_cells=self.completed_cells-initial,
            phi_hex=[float(v).hex() for v in self.phi],
            actual_seconds=time.monotonic()-started, admission_seconds=admission_seconds,
            current_read_identity_sha256=self._current_read_identity,
            journal_directory=None if self._journal_directory is None else str(self._journal_directory),
            all_total_integrals_available=self.complete)

    def query(self, cells, local_u):
        """Exact signed reconstruction and error at arbitrary same-mesh nodes."""
        require_actions()
        if not self.complete or self.phi is None:
            raise ValueError('Finish every original integration cell before a total/signed integral query')
        self._assert_working_rule()
        cells, local, _ = self.node._literal_arrays(cells, local_u, self.phi)
        query = self.q.make_query(cells, local)
        partial = np.array(query['partial'].detach().numpy(), dtype=np.float64, copy=True)
        h_words = np.array(query['h'].detach().numpy()[:, 0, 0], dtype=np.float64, copy=True)
        if partial.shape != (len(cells), self.Q) or not np.isfinite(partial).all() or not np.isfinite(h_words).all():
            raise FloatingPointError('Every actual partial weight and h carrier must be finite')
        P, A = len(cells), len(self.phi)
        signed_exact = {key: np.empty((P, A, 3), dtype=object) for key in KEYS}
        signed_error = {key: np.empty((P, A), dtype=object) for key in KEYS}
        hhat = np.empty(P, dtype=object)
        normalized_partial = np.empty((P, self.Q), dtype=object)
        peano_records = []
        for p, (cell, u) in enumerate(zip(cells, local)):
            cell, u = int(cell), F(float(u))
            h = hhat[p] = F(float(h_words[p]))
            one_minus_h = 1-h
            width = self.widths_exact[cell]
            partial_exact = tuple(F(float(value)) for value in partial[p])
            normalized_partial[p] = tuple(value/width for value in partial_exact)
            weights = tuple(value/width-one_minus_h*w for value, w in zip(partial_exact, self.weights_exact))
            peano = self.kernel.peano_functional(self.nodes_exact, weights, split=u,
                density_left=h, density_right=-one_minus_h)
            peano_records.append(dict(cell=cell, local_u=u, hhat=h,
                density_left=h, density_right=-one_minus_h, normalized_signed_weights=weights,
                mass=peano['mass'], peano_L1=peano['peano_L1'],
                sum_absolute_weights=peano['sum_absolute_weights'],
                integrator_width_carrier=width,
                query_width_carrier=F(float(query['widths'][p])),
                query_width_matches_integrator_word=float(query['widths'][p]).hex() == float(self.width_words[cell]).hex()))
            section = slice(cell*self.Q, (cell+1)*self.Q)
            bound = self.bounds[cell]
            for key in KEYS:
                for a in range(A):
                    partial_vector = exact_vector_sum((weight, self.integrated_working[key][cell*self.Q+j, a])
                        for j, weight in enumerate(partial_exact))
                    signed_exact[key][p, a] = tuple(
                        self.prefix_exact[key][cell, a, component]+partial_vector[component]
                        -one_minus_h*self.total_exact[key][a, component] for component in range(3))
                    current = self.kernel.quadrature_error(peano,
                        physical_width=bound['physical_width'], width_carrier=width,
                        value_norm_upper=bound['B'][key], radial_derivative_norm_upper=bound['L'][key],
                        node_value_errors=list(self.integrated_error[key][section, a]), arithmetic_error=F(0))
                    before = self.prefix_error[key][cell, a]
                    after = self.total_error[key][a]-self.prefix_error[key][cell+1, a]
                    if after < 0:
                        raise ArithmeticError('The full exact nonnegative error prefix became inconsistent')
                    signed_error[key][p, a] = abs(h)*before+abs(one_minus_h)*after+current['upper_error']
                    self.counts['signed_cell_error_kernel_calls'] += 1
        self.counts['signed_queries'] += 1
        self.counts['signed_query_vectors'] += P*A
        return dict(query=query, cells=cells, local_u=local, phi=self.phi,
            signed_exact=signed_exact, signed_error=signed_error, hhat=hhat,
            actual_partial_working=partial, normalized_partial_exact=normalized_partial,
            signed_current_cell_records=peano_records,
            current_read_identity_sha256=self._current_read_identity,
            binding_identity_sha256=canonical(self.binding),
            signed_exact_is_rational_reconstruction_of_these_working_nodes=True,
            all_actual_partial_weight_signs_and_masses_retained=True,
            current_cell_signed_functional_not_replaced_by_two_absolute_integrals=True,
            no_closure_field_Gram_or_geometry_certificate=True)

    def metadata(self):
        return dict(schema=SCHEMA, binding=self.binding, binding_identity_sha256=canonical(self.binding),
            complete_current_angle_block=self.complete, completed_cells=self.completed_cells, total_cells=self.C,
            current_phi_hex=None if self.phi is None else [float(v).hex() for v in self.phi],
            current_read_identity_sha256=self._current_read_identity,
            journal_directory=None if self._journal_directory is None else str(self._journal_directory),
            actual_counts=dict(self.counts), actual_counts_are_this_execution_only=True,
            source_commit=self.source_commit, whole_rule_peano=serialize(self.whole_peano),
            scalar_profile_recomputed_from_current_field=False,
            all_original_integration_nodes_retained=True,
            all_922_cells_required_before_query=True,
            closure_arithmetic_included=False, complete_field_arithmetic_included=False,
            core_cap_inverse_and_Gram_errors_included=False,
            continuous_metric_or_reach_certified=False, closed_isometry_accepted=False)


def cli_query_plan(component, requests):
    q, node = component.q, component.node_module
    if requests is None:
        phi = np.array(q.phi, copy=True)
        cells, local = np.array(q.observation_cells, copy=True), np.array(q.observation_u, copy=True)
        scope = dict(kind='all original complete observation addresses and angular orbits',
            original_full_angles=q.full_N, original_observations=q.P)
    else:
        payload = json.loads(Path(requests).read_text())
        if payload.get('schema') != REQUEST_SCHEMA:
            raise ValueError('Use the complete signed-integral literal request schema')
        phi = np.array([node.literal_float(value) for value in payload['phi_hex']], dtype=np.float64)
        cells = np.asarray(payload['cells'])
        local = np.array([node.literal_float(value) for value in payload['local_u_hex']], dtype=np.float64)
        scope = dict(kind='explicit complete literal requested addresses',
            request_file=file_record(requests), original_full_grid_coverage_not_assumed=True)
    cells, local, phi = component.node._literal_arrays(cells, local, phi)
    if (np.any(cells < 0) or np.any(cells >= component.C) or np.any(local < 0) or np.any(local > 1)):
        raise ValueError('Every query must belong to its exact original cell')
    scope.update(phi_hex=[float(v).hex() for v in phi], cells=[int(v) for v in cells],
        local_u_hex=[float(v).hex() for v in local], queried_radial_addresses=len(cells),
        queried_angle_addresses=len(phi), requested_point_vectors=len(cells)*len(phi))
    return cells, local, phi, scope


def write_raw_query(path, component, answer, *, angle_start, query_begin, query_end, identity):
    payload = dict(schema=SCHEMA, source_sha256=sha(__file__),
        integral_binding_identity_sha256=canonical(component.binding),
        overall_query_identity_sha256=canonical(identity),
        current_read_identity_sha256=component._current_read_identity,
        angle_start=angle_start, query_begin=query_begin, query_end=query_end,
        result=serialize({key: value for key, value in answer.items() if key != 'query'}))
    raw = json.dumps(payload, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    if path.exists():
        # A previously atomic query payload may precede its journal commit.
        prior = json.loads(gzip.decompress(path.read_bytes()))
        if prior != payload:
            raise ValueError('An uncommitted query payload differs from this complete exact reconstruction')
        recovered = True
    else:
        temporary = path.with_name(path.name+'.partial')
        temporary.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
        temporary.replace(path)
        recovered = False
    return file_record(path), recovered


def main(args):
    require_actions()
    started = time.monotonic()
    args.repo, args.outdir = args.repo.resolve(), args.outdir.resolve()
    if args.outdir == args.repo or args.repo in args.outdir.parents:
        raise ValueError('Raw complete node/integral records must remain outside the Git repository')
    node_path = args.repo/TOPIC/NODE_RELATIVE
    node_module = load('_signed_integral_actual_nodes', node_path, NODE_SHA)
    actual = node_module.load_actual(args)
    node = node_module.NodeOutwardEvaluator(actual,
        working_cache_directory=args.outdir.parent/(args.outdir.name+'-working-cache-'+uuid.uuid4().hex),
        exp_order=args.exp_order)
    component = SignedMeridianIntegrals(actual, node,
        envelope_report=args.envelope_report, envelope_journal=args.envelope_journal)
    cells, local, phi, plan = cli_query_plan(component, args.requests)
    angle_block = component.q.angle_block
    identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
        binding_identity_sha256=canonical(component.binding), query_plan_sha256=canonical(plan),
        working_angle_block=angle_block, query_block=args.query_block,
        actual_node_exp_order=args.exp_order)
    identity_sha = canonical(identity)
    report_path, journal = args.outdir/'report.json', args.outdir/'queries.jsonl'
    entries, chain = [], identity_sha
    angle_start, query_begin, completed_vectors = 0, 0, 0
    maxima = {key: F(0) for key in KEYS}
    if args.outdir.exists():
        if not args.resume or not report_path.is_file() or not journal.is_file():
            raise ValueError('Existing integral output needs its explicit bound natural journal resume')
        prior = json.loads(report_path.read_text())
        if prior.get('identity') != identity or prior.get('query_plan') != plan:
            raise ValueError('Do not resume another complete actual field or query plan')
        with journal.open() as stream:
            for line in stream:
                entry = json.loads(line)
                record = entry['record']
                expected_end = min(len(cells), query_begin+args.query_block)
                if (angle_start >= len(phi) or record.get('angle_start') != angle_start
                        or record.get('angle_end') != min(len(phi), angle_start+angle_block)
                        or record.get('query_begin') != query_begin or record.get('query_end') != expected_end
                        or entry.get('previous_record_identity_sha256') != chain
                        or entry.get('record_identity_sha256') != canonical(dict(previous=chain, record=record))):
                    raise ValueError('The complete signed-query journal has a changed or missing block')
                payload_path = args.outdir/record['payload_relative_path']
                if (sha(payload_path) != record['payload']['sha256']
                        or payload_path.stat().st_size != record['payload']['bytes']):
                    raise ValueError('A completed actual signed-query payload changed')
                chain = entry['record_identity_sha256']
                entries.append(entry)
                completed_vectors += record['point_vectors']
                for key in KEYS:
                    maxima[key] = max(maxima[key], F(record['maxima'][key]))
                query_begin = expected_end
                if query_begin == len(cells):
                    angle_start += angle_block
                    query_begin = 0
    else:
        if args.resume:
            raise ValueError('Resume requires an existing actual integral output')
        args.outdir.mkdir(parents=True)
        journal.write_text('')
    query_directory = args.outdir/'raw-signed-queries'
    query_directory.mkdir(exist_ok=True)
    failure = None
    prepare_status = None
    initial_vectors = completed_vectors

    def save():
        complete = angle_start >= len(phi) and failure is None
        report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=component.source_commit,
            identity=identity, identity_sha256=identity_sha, query_plan=plan, actual_binding=actual.binding,
            component=serialize(component.metadata()), complete=complete,
            complete_requested_finite_queries=complete, completed_point_vectors=completed_vectors,
            requested_point_vectors=len(cells)*len(phi), new_point_vectors=completed_vectors-initial_vectors,
            next_angle_start=min(angle_start, len(phi)), next_query_begin=query_begin,
            current_prepare_status=prepare_status,
            paid_current_node_cells=component.completed_cells,
            full_current_angle_integrals_available=component.complete,
            processed_signed_error_maxima=serialize(maxima),
            requested_scope_signed_error_maxima=serialize(maxima) if complete else None,
            signed_query_journal=file_record(journal), signed_query_journal_chain_sha256=chain,
            signed_query_payload_files=len(entries),
            signed_query_payload_bytes=sum(item['record']['payload']['bytes'] for item in entries),
            partial_queries_not_promoted_to_complete_scope=not complete,
            failure=failure, actual_seconds=time.monotonic()-started, admission_seconds=args.admission_seconds,
            complete_core_cap_or_closure_error_paid=False,
            full_field_arithmetic_error_paid=False, metric_or_reach_certified=False,
            closed_isometry_accepted=False,
            execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'), attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        write_json(report_path, report)
        return report

    save()
    try:
        while angle_start < len(phi):
            remaining = args.admission_seconds-(time.monotonic()-started)
            if remaining <= 0:
                break
            angles = phi[angle_start:angle_start+angle_block]
            raw_nodes = args.outdir/('integrals-angle-'+str(angle_start).zfill(4))
            prepare_status = component.prepare(angles, journal_directory=raw_nodes,
                resume=raw_nodes.exists(), admission_seconds=remaining,
                progress=lambda record: print(json.dumps(record, separators=(',', ':'), allow_nan=False), flush=True))
            save()
            if not prepare_status['complete']:
                break
            while query_begin < len(cells):
                if time.monotonic()-started >= args.admission_seconds:
                    break
                query_end = min(len(cells), query_begin+args.query_block)
                answer = component.query(cells[query_begin:query_end], local[query_begin:query_end])
                relative = 'raw-signed-queries/angle-'+str(angle_start).zfill(4)+'-query-'+str(query_begin).zfill(5)+'.json.gz'
                payload, recovered = write_raw_query(args.outdir/relative, component, answer,
                    angle_start=angle_start, query_begin=query_begin, query_end=query_end, identity=identity)
                point_vectors = (query_end-query_begin)*len(angles)
                record = dict(angle_start=angle_start, angle_end=min(len(phi), angle_start+angle_block),
                    query_begin=query_begin, query_end=query_end, point_vectors=point_vectors,
                    current_read_identity_sha256=component._current_read_identity,
                    payload_relative_path=relative, payload=payload,
                    recovered_previously_atomic_query_payload=recovered,
                    maxima={key: str(max(answer['signed_error'][key].flat)) for key in KEYS})
                next_chain = canonical(dict(previous=chain, record=record))
                entries.append(dict(previous_record_identity_sha256=chain,
                    record_identity_sha256=next_chain, record=record))
                temporary = journal.with_name(journal.name+'.partial')
                with temporary.open('w') as stream:
                    for entry in entries:
                        stream.write(json.dumps(entry, separators=(',', ':'), allow_nan=False)+'\n')
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary.replace(journal)
                chain = next_chain
                completed_vectors += point_vectors
                for key in KEYS:
                    maxima[key] = max(maxima[key], F(record['maxima'][key]))
                query_begin = query_end
                save()
                print(json.dumps(dict(event='complete_actual_signed_integral_query',
                    angle_start=angle_start, next_query=query_begin, point_vectors=point_vectors,
                    maxima=record['maxima']), separators=(',', ':'), allow_nan=False), flush=True)
            if query_begin < len(cells):
                break
            angle_start += angle_block
            query_begin = 0
            save()
    except Exception as exc:
        failure = dict(type=type(exc).__name__, message=str(exc),
            angle_start=angle_start, query_begin=query_begin,
            prepared_original_cells=component.completed_cells)
        save()
        raise
    report = save()
    print(json.dumps(dict(event='complete_actual_signed_integral_admission_returned',
        complete=report['complete'], completed_point_vectors=completed_vectors,
        prepared_current_original_cells=component.completed_cells,
        report_sha256=sha(report_path), actual_seconds=report['actual_seconds'],
        no_full_field_Gram_or_geometry_claim=True), separators=(',', ':'), allow_nan=False), flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'report', 'checkpoint', 'reference-bundle', 'carrier', 'node-report',
                 'scalar-input', 'preparation-report', 'envelope-report', 'envelope-journal', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--state', choices=('initial', 'final'), default='final')
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--exp-order', type=int, default=24)
    p.add_argument('--requests', type=Path)
    p.add_argument('--query-block', type=int, default=64)
    p.add_argument('--admission-seconds', type=float, default=600.)
    p.add_argument('--resume', action='store_true')
    args = p.parse_args()
    if (args.panels < 1 or args.exp_order < 2 or args.query_block < 1
            or not math.isfinite(args.admission_seconds) or args.admission_seconds <= 0):
        raise ValueError('Use explicit positive complete arithmetic/block and natural-return budgets')
    return args


if __name__ == '__main__':
    main(parse_args())
