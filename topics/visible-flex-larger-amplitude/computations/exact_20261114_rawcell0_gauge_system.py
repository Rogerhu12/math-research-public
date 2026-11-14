#!/usr/bin/env python3
"""Same actual1372 block matrix in explicitly stored height/slope node coordinates.

Actions only. This module binds original actual28/41 bytes and forms a separately
identified binary64 shadow of G_left J G_right^-1 using NumPy longdouble.
It does not evaluate an ODE, root, J, nonlinear trial, or acceptance condition.
The original matrix remains the only matrix for exact residual readback.
"""
from __future__ import annotations

import gzip
import hashlib
import importlib
import json
import math
import os
from pathlib import Path
import struct
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ADAPTER_NAME = 'exact_20261114_rawcell0_step_system.py'
ADAPTER_SHA = 'fde0e03918814c9400a37eeb7719ecd0894c204490ee830fa128a3a49797cc81'
STEP_RESULT_SHA = '6e9485dcc8bc512481d714d794f87e76f785b577fd6f714ae12fd9d8e9468adf'
ORIGINAL_MATRIX_SHA = 'e929e642a9738c98d97dc06129c396b8fdff09aac32430892a412701d5dd4521'
POLICY = 'actual41-field0-single-node-anchor-cut-field3-port-localG-restI-v1'
FORMATION = 'longdouble-recipe-to-saved-binary64-G-then-longdouble-block-conjugacy-to-binary64-v1'


def actions_only():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Gauge matrix formation is restricted to the public repository Actions')


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for data in iter(lambda: stream.read(1 << 20), b''):
            h.update(data)
    return h.hexdigest()


def load_adapter():
    source = HERE / ADAPTER_NAME
    if file_sha(source) != ADAPTER_SHA:
        raise ValueError('The frozen original1372 system binder changed')
    result = importlib.import_module(Path(ADAPTER_NAME).stem)
    if Path(result.__file__).resolve() != source.resolve():
        raise ImportError('Unexpected original1372 system import path')
    return result


def finite_record(value):
    return dict(value=float(value), float64le_hex=struct.pack('<d', float(value)).hex())


def decode_record(record, label):
    if not isinstance(record, dict) or not isinstance(record.get('float64le_hex'), str):
        raise ValueError('A complete actual binary64 record is required: ' + label)
    raw = bytes.fromhex(record['float64le_hex'])
    if len(raw) != 8:
        raise ValueError('One original binary64 word is required: ' + label)
    value = struct.unpack('<d', raw)[0]
    if not math.isfinite(value):
        raise ValueError('Nonfinite original coordinate anchor: ' + label)
    return value


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


class FormationLedger:
    """Actual cast diagnostics; no claim of a rigorous floating error enclosure."""
    def __init__(self):
        self.entries = self.changed = self.zeroed = self.nonfinite = 0
        self.examples = []

    def cast(self, values, location):
        values = np.asarray(values, dtype=np.longdouble)
        with np.errstate(over='ignore', under='ignore', invalid='ignore'):
            stored = np.asarray(values, dtype=np.float64)
            changed = stored.astype(np.longdouble) != values
            zeroed = (values != 0) & (stored == 0)
            bad = ~np.isfinite(values) | ~np.isfinite(stored)
        self.entries += int(values.size)
        self.changed += int(np.count_nonzero(changed))
        self.zeroed += int(np.count_nonzero(zeroed))
        self.nonfinite += int(np.count_nonzero(bad))
        for index in np.flatnonzero(changed.reshape(-1))[:max(0, 8-len(self.examples))]:
            self.examples.append(dict(
                location=location, flat_index=int(index),
                longdouble_decimal_diagnostic=np.format_float_scientific(
                    values.flat[index], precision=36, unique=False),
                stored_float64le_hex=struct.pack('<d', float(stored.flat[index])).hex()))
        if np.any(bad):
            raise FloatingPointError('Nonfinite gauge representation at ' + str(location))
        return stored

    def report(self):
        f = np.finfo(np.longdouble)
        return dict(
            entries=self.entries, values_changed_by_final_binary64_cast=self.changed,
            nonzero_rounded_to_zero=self.zeroed, nonfinite=self.nonfinite,
            examples=self.examples, NumPy=np.__version__,
            longdouble_dtype=np.dtype(np.longdouble).str,
            longdouble_storage_bytes=np.dtype(np.longdouble).itemsize,
            longdouble_significand_bits=int(f.nmant)+1,
            longdouble_minexp=int(f.minexp), longdouble_maxexp=int(f.maxexp),
            longdouble_eps_decimal=str(f.eps),
            longdouble_padding_bytes_not_used_as_numeric_identity=True,
            exact_conjugacy_claimed=False, rigorous_roundoff_bound_claimed=False,
            actual_saved_binary64_coefficients_are_the_coordinate_definition=True)


class RawCell0GaugeSystem:
    """A finite candidate representation; the supplied original system is immutable."""
    def __init__(self, original, output, max_transformed_j_bytes=512*1024**2):
        actions_only()
        self.original = original
        self.B = original.B
        self.output = output
        self.directory = output.directory
        self.M, self.K, self.depth = original.M, original.K, original.depth
        self.source_sha = file_sha(__file__)
        self.B.same(original.step_result_sha256, STEP_RESULT_SHA, 'actual41 completed result')
        self.B.same(original.binding['new_matrix_identity_sha256'], ORIGINAL_MATRIX_SHA,
                    'same actual42 original1372 matrix')
        self.B.same((self.M, self.K, self.depth), (112, 224, 1372), 'complete actual dimensions')
        parameters = original.original.live['parameters']
        self.B.same(parameters['orientation'], 1, 'original engine orientation')
        self.B.same(parameters['spacing'], 2, 'every original nonzero Fourier frequency')
        self.spacing = parameters['spacing']
        self.orientation = parameters['orientation']
        self.active_last = original.old_to_new[72]
        self.B.same(self.active_last, 868, 'actual868 original rawCell0 steps')
        self.changed_count = self.active_last + 1
        self.transformed_bytes = self.changed_count*self.K*self.K*8
        if self.transformed_bytes > max_transformed_j_bytes:
            raise MemoryError('Complete transformed J storage exceeds the declared byte budget; no block is omitted')
        self.formation = FormationLedger()
        self.alpha = np.ones(self.depth+1, dtype=np.float64)
        self.beta = np.zeros((self.depth+1, self.M), dtype=np.float64)
        self.eta = np.ones(self.depth+1, dtype=np.float64)
        self.anchors = [None]*(self.depth+1)
        self._build_anchors()
        self.coefficient_files = {
            'alpha': output.save('gauge-alpha', self.alpha, 'Saved binary64 alpha for each complete node'),
            'beta': output.save('gauge-beta', self.beta, 'Saved binary64 beta for every node and all112 modes'),
            'eta': output.save('gauge-eta', self.eta, 'Saved binary64 Pi coefficient including the cut port only')}
        anchor_report = dict(
            schema='native-actual41-height-slope-node-anchors-v1',
            source_sha256=self.source_sha, adapter_sha256=ADAPTER_SHA,
            original_matrix_identity_sha256=ORIGINAL_MATRIX_SHA,
            original_step_result_sha256=STEP_RESULT_SHA, policy=POLICY,
            node_order='complete Q-all followed by Pi-all at every shooting node',
            active_nodes=[0, self.active_last], identity_nodes=[self.active_last+1, self.depth],
            mixed_interface_stage=self.active_last,
            mixed_interface_original_stage=72,
            original_source_mu_and_pi_to_engine_factor_kept_separate=True,
            alpha_formula='r2=r*r; r3=r2*r; r4=r3*r; alpha=r4',
            beta_formula='beta_j=(spacing*(j+1))^2*r3',
            eta_formula='(((orientation*sqrt(longdouble(12)))*mu)*port)/(r4*w)',
            raw_coefficient_files=self.coefficient_files,
            formation=self.formation.report(), anchors=self.anchors)
        self.anchor_file = self.B.write(self.directory/'node-gauge-anchors.json.gz',
                                       anchor_report, compressed=True)
        self.coefficient_identity = canonical_sha(dict(
            source_sha256=self.source_sha, original_matrix=ORIGINAL_MATRIX_SHA,
            actual_step_result=STEP_RESULT_SHA, policy=POLICY, formation=FORMATION,
            raw_G={key:value['sha256'] for key,value in self.coefficient_files.items()},
            node_anchors_sha256=self.anchor_file['sha256']))
        self.block_rows = []
        self._form_blocks()
        self.binding = dict(
            schema='native-original1372-saved-height-slope-gauge-binding-v1',
            producer_source_sha256=self.source_sha, original_adapter_source_sha256=ADAPTER_SHA,
            original_matrix_identity_sha256=ORIGINAL_MATRIX_SHA,
            original_step_result_sha256=STEP_RESULT_SHA,
            original_input_binding_sha256=canonical_sha(original.binding),
            coordinate_identity_sha256=self.coefficient_identity,
            policy=POLICY, formation=FORMATION,
            alpha_beta_eta=self.coefficient_files, anchors=self.anchor_file,
            original_cut_residual_sha256=hashlib.sha256(original.raw('cut-residual')).hexdigest(),
            original_stage_residual_sha256=hashlib.sha256(original.raw('stage-residuals')).hexdigest(),
            original_far_residual_sha256=hashlib.sha256(original.raw('end-residual')).hexdigest(),
            original_sigma_sha256=hashlib.sha256(original.raw('original-scales')).hexdigest(),
            original_far_graph_sha256=hashlib.sha256(original.raw('original-far-graph')).hexdigest(),
            original_H_sha256=hashlib.sha256(self.B.float_bytes(
                original.original.all('physical-height'))).hexdigest(),
            cut_row_equation='xi_u + alpha0 * original_cut_residual = 0; original target/H unchanged',
            cut_left_row_multiplier_is_explicit=True,
            cut_left_row_multiplier_float64le_hex=struct.pack('<d', float(self.alpha[0])).hex(),
            stage_equation='formed_J * xi_next - xi_current + exact_saved_G * original_r = 0',
            minus_identity_is_written_directly=True,
            far_equation_is_original=True, far_node_is_identity=True,
            G_conjugacy_of_exact_original_matrix_is_not_claimed_after_formation=True,
            all_original_cross_mode_couplings_retained=True,
            original_scientific_sigma_norm_is_unchanged=True,
            actual_full_new_J_virtual_raw_sha256=self.full_J_sha,
            formed_changed_blocks=self.changed_file, complete_block_rows=self.block_rows,
            original576_restriction_is_not_original576_linear_solution_claim=True,
            native_accepted=False, task_completed=False)
        self.binding['formed_matrix_identity_sha256'] = canonical_sha(self.binding)
        self.binding_file = self.B.write(self.directory/'gauge-matrix-binding.json.gz',
                                        self.binding, compressed=True)
        self.B.write(self.directory/'gauge-formation-summary.json', self.small_report())

    def _build_anchors(self):
        S = load_adapter()
        assigned = set()
        for n in range(72):
            report = self.original.stage_reports[n]
            window = self.original.json_descriptor(report['identity'])
            packet_descriptor = report['field_observations']
            self.B.same(packet_descriptor,
                        self.original.metadata_packets[packet_descriptor['file']],
                        'actual already verified field packet')
            packet = self.B.read(self.B.safe_file(self.original.directory, packet_descriptor['file']))
            self.B.same(packet['schema'], 'original-native-rawcell0-actual-field-geometry-v1',
                        'original returned root.g observations')
            self.B.same(packet['stage'], n, 'field packet original stage')
            self.B.same(packet['partial'], False, 'complete actual root.g observations')
            count = self.original.step_counts[n]
            fields = packet['fields']
            self.B.same(len(fields), 4*count, 'all four fields per actual step')
            window_mu = decode_record(window['mu'], 'stage mu')
            self.B.same(S.number_bits(window['mu']),
                        S.number_bits(self.original.original.live['stages'][n]['mu']),
                        'same engine/cell mu bits')
            full = self.original.step_arrays.all(self.original.stage_arrays[n]['full_states'])
            for k in range(count):
                group = fields[4*k:4*k+4]
                for f, row in enumerate(group):
                    self.B.same((row['global_step'], row['field_index']), (k, f),
                                'actual field observation order')
                node = self.original.old_to_new[n] + count-k
                if node in assigned:
                    raise ValueError('Every node must have exactly one chosen coordinate anchor')
                row = group[0]
                schedule = report['schedule'][k]
                for key in ('profile_index', 'grid_index', 'grid_branch'):
                    self.B.same(row[key], schedule[key], 'same actual field0 schedule '+key)
                for key in ('x', 'h'):
                    self.B.same(S.number_bits(row[key]), S.number_bits(schedule[key]),
                                'same actual field0 schedule bytes '+key)
                self.B.same(row['state_float64le_sha256'],
                            hashlib.sha256(self.B.float_bytes(full[k])).hexdigest(),
                            'field0 is the complete actual step input state')
                self._assign(node, n, k, row, window_mu, 1., window,
                             packet_descriptor, report['identity'], 'original-step-field0')
                assigned.add(node)
            if n == 0:
                row = fields[-1]
                port = decode_record(report['original_port_ratio'], 'cut original exit port')
                self._assign(0, 0, count-1, row, window_mu, port, window,
                             packet_descriptor, report['identity'], 'cut-last-field3-geometry')
                assigned.add(0)
        if assigned != set(range(self.active_last+1)):
            raise ValueError('The actual active node anchor map is incomplete')
        for node in range(self.active_last+1, self.depth+1):
            self.anchors[node] = dict(node=node, kind='identity',
                alpha_float64le_hex='000000000000f03f',
                eta_float64le_hex='000000000000f03f',
                beta_is_exact_positive_zero_for_every_mode=True,
                no_fictitious_geometry_mu_or_port=True)
        if (not np.isfinite(self.alpha).all() or not np.isfinite(self.beta).all() or
                not np.isfinite(self.eta).all() or np.any(self.alpha == 0) or np.any(self.eta == 0)):
            raise FloatingPointError('The explicitly saved coordinate map is not finite and invertible')

    def _assign(self, node, stage, step, row, mu, port, window,
                packet_descriptor, window_descriptor, kind):
        geometry = row['geometry_number_fields']
        r = decode_record(geometry['r'], 'original root.g.r')
        w = decode_record(geometry['w'], 'original root.g.w')
        if r <= 0 or w <= 0 or mu <= 0 or port == 0:
            raise ValueError('The declared height/slope coordinate recipe needs positive r,w,mu and nonzero port')
        LD = np.longdouble
        r1 = LD(r)
        r2 = r1*r1
        r3 = r2*r1
        r4 = r3*r1
        frequencies = np.arange(1, self.M+1, dtype=np.int64)*self.spacing
        beta = (frequencies.astype(LD)*frequencies.astype(LD))*r3
        eta = (((LD(self.orientation)*np.sqrt(LD(12)))*LD(mu))*LD(port))/(r4*LD(w))
        self.alpha[node] = self.formation.cast(r4, dict(kind='alpha', node=node)).item()
        self.beta[node] = self.formation.cast(beta, dict(kind='beta', node=node))
        self.eta[node] = self.formation.cast(eta, dict(kind='eta', node=node)).item()
        if self.alpha[node] == 0 or self.eta[node] == 0:
            raise FloatingPointError('A nonzero coordinate diagonal rounded to zero at node '+str(node))
        self.anchors[node] = dict(
            node=node, kind=kind, original_stage=stage, original_step=step,
            field_index=row['field_index'], profile_index=row['profile_index'],
            grid_index=row['grid_index'], grid_branch=row['grid_branch'],
            x=row['x'], h=row['h'], field_packet=packet_descriptor,
            original_window=window_descriptor, source_r=geometry['r'], source_w=geometry['w'],
            source_mu=window['mu'], pi_to_engine_factor=finite_record(port),
            original_full_field_state_sha256=row['state_float64le_sha256'],
            field3_state_not_claimed_equal_final_RK_state=(kind=='cut-last-field3-geometry'),
            cut_port_multiplies_G_Pi_column=(node==0),
            coefficient_source_uses_root_g_not_oldR_or_recomputed_w=True)

    def _transform(self, n, J):
        M = self.M
        LD = np.longdouble
        left_alpha, left_eta = LD(self.alpha[n]), LD(self.eta[n])
        right_alpha, right_eta = LD(self.alpha[n+1]), LD(self.eta[n+1])
        left_beta = self.beta[n].astype(LD)[:, None]
        right_ratio = (self.beta[n+1].astype(LD)/right_eta)[None, :]
        A = J[:M, :M].astype(LD)
        B = J[:M, M:].astype(LD)
        C = J[M:, :M].astype(LD)
        D = J[M:, M:].astype(LD)
        out = np.empty((self.K, self.K), dtype=LD)
        lower_Pi = left_beta*B + left_eta*D
        out[:M, :M] = (left_alpha*(A-B*right_ratio))/right_alpha
        out[:M, M:] = (left_alpha*B)/right_eta
        out[M:, :M] = (left_beta*A+left_eta*C-lower_Pi*right_ratio)/right_alpha
        out[M:, M:] = lower_Pi/right_eta
        return self.formation.cast(out, dict(kind='complete-gauge-J', stage=n))

    def _form_blocks(self):
        name = 'large-arrays/formed-gauge-changed-stage-J.f64le'
        path = self.directory/name
        whole = hashlib.sha256()
        changed = hashlib.sha256()
        count = 0
        started = time.monotonic()
        try:
            with path.open('xb') as stream:
                for n, J in self.original.stages():
                    self.B.same(n, count, 'complete original stage order')
                    self.B.same(hashlib.sha256(self.B.float_bytes(J)).hexdigest(),
                                self.original.J_rows[n]['raw_sha256'], 'source J raw bytes')
                    if n < self.changed_count:
                        value = self._transform(n, J)
                        raw = self.B.float_bytes(value)
                        stream.write(raw)
                        changed.update(raw)
                        origin = 'saved-longdouble-formed-binary64-gauge-block'
                    else:
                        raw = self.B.float_bytes(J)
                        origin = 'unchanged-original1372-block'
                    whole.update(raw)
                    self.block_rows.append(dict(
                        stage=n, original_source_stage=self.original.cells[n],
                        source_J_raw_sha256=self.original.J_rows[n]['raw_sha256'],
                        formed_J_raw_sha256=hashlib.sha256(raw).hexdigest(),
                        bytes=len(raw), origin=origin,
                        file=name if n < self.changed_count else None,
                        byte_offset=n*self.K*self.K*8 if n < self.changed_count else None))
                    count += 1
                    if count % 64 == 0 or count == self.depth:
                        print(json.dumps(dict(event='native_gauge_matrix_formation',
                            complete_blocks=count, expected_blocks=self.depth,
                            changed_blocks=min(count, self.changed_count),
                            elapsed_seconds=time.monotonic()-started)), flush=True)
            if count != self.depth or path.stat().st_size != self.transformed_bytes:
                raise ValueError('The complete gauge block stream is incomplete')
        finally:
            self.B.write(self.directory/'gauge-formation-progress.json', dict(
                complete_blocks=count, expected_blocks=self.depth,
                changed_blocks_completed=min(count, self.changed_count),
                expected_changed_blocks=self.changed_count,
                formation=self.formation.report(), elapsed_seconds=time.monotonic()-started,
                stream_completed=count==self.depth, native_accepted=False))
        self.full_J_sha = whole.hexdigest()
        self.changed_file = dict(
            name='formed-gauge-changed-stage-J', file=name, dtype='<f8', order='C',
            shape=[self.changed_count, self.K, self.K],
            bytes=self.transformed_bytes, sha256=changed.hexdigest(),
            role='Every changed full block, including the old72 mixed-coordinate interface; artifact only')
        self.output.entries.append(self.changed_file)

    def stages(self):
        block_bytes = self.K*self.K*8
        path = self.directory/self.changed_file['file']
        if path.stat().st_size != self.transformed_bytes:
            raise ValueError('The saved formed block stream changed length')
        with path.open('rb') as stream:
            for n in range(self.changed_count):
                raw = stream.read(block_bytes)
                self.B.same(hashlib.sha256(raw).hexdigest(),
                            self.block_rows[n]['formed_J_raw_sha256'], 'same saved formed J block')
                yield n, np.frombuffer(raw, dtype='<f8').reshape(self.K, self.K)
            if stream.read(1):
                raise ValueError('Unexpected trailing formed J bytes')
        expected = self.changed_count
        for old, J in self.original.original.stages():
            n = self.original.old_to_new[old]
            if n < self.changed_count:
                continue
            self.B.same(n, expected, 'same complete unchanged outer block order')
            self.B.same(hashlib.sha256(self.B.float_bytes(J)).hexdigest(),
                        self.block_rows[n]['formed_J_raw_sha256'], 'same unchanged outer J block')
            yield n, J
            expected += 1
        self.B.same(expected, self.depth, 'all complete saved-gauge matrix blocks')

    def all(self, name):
        if name in ('original-scales', 'original-far-graph'):
            return self.original.all(name)
        raise ValueError('Do not substitute rounded transformed residuals for exact original-G RHS: '+name)

    def restore(self, xi, label):
        xi = np.asarray(xi, dtype=np.float64)
        if xi.shape != (self.depth+1, self.K) or not np.isfinite(xi).all():
            raise ValueError('One complete finite saved-coordinate direction is required')
        # Identity nodes are copied, retaining their signed zero and all bytes.
        result = xi.copy()
        stop = self.active_last+1
        LD = np.longdouble
        q = xi[:stop, :self.M].astype(LD)/self.alpha[:stop, None].astype(LD)
        pi = (xi[:stop, self.M:].astype(LD)-self.beta[:stop].astype(LD)*q)/self.eta[:stop, None].astype(LD)
        ledger = FormationLedger()
        result[:stop, :self.M] = ledger.cast(q, dict(kind='restore-Q', label=label))
        result[:stop, self.M:] = ledger.cast(pi, dict(kind='restore-Pi', label=label))
        detail = dict(
            label=label, formula='Q=xi_u/alpha; Pi=(xi_k-beta*Q)/eta, then binary64',
            active_nodes=[0, self.active_last], identity_nodes_copied_byte_for_byte=True,
            saved_G_raw_identity=self.coefficient_identity, formation=ledger.report(),
            recovered_original_delta_sha256=hashlib.sha256(self.B.float_bytes(result)).hexdigest(),
            original_full_exact_readback_required=True)
        return result, detail

    def small_report(self):
        return dict(
            schema='native-original1372-height-slope-gauge-formation-summary-v1',
            source_sha256=self.source_sha, original_adapter_sha256=ADAPTER_SHA,
            original_matrix_identity_sha256=ORIGINAL_MATRIX_SHA,
            original_step_result_sha256=STEP_RESULT_SHA, policy=POLICY, formation_recipe=FORMATION,
            coordinate_identity_sha256=self.coefficient_identity,
            formed_matrix_identity_sha256=self.binding['formed_matrix_identity_sha256'],
            full_formed_J_virtual_raw_sha256=self.full_J_sha,
            modes=self.M, shape_dimension=self.K, depth=self.depth,
            active_nodes=[0, self.active_last], identity_nodes=[self.active_last+1, self.depth],
            changed_stages=self.changed_count, unchanged_stages=self.depth-self.changed_count,
            mixed_interface_stage=self.active_last, mixed_interface_original_stage=72,
            changed_J_bytes=self.transformed_bytes,
            complete_mode_couplings_preserved=True, original_far_is_identity_gauge=True,
            original_cut_target_and_H_kept=True, cut_alpha_row_multiplier_explicit=True,
            coefficient_files=self.coefficient_files, anchors=self.anchor_file,
            binding_file=self.binding_file, formation=self.formation.report(),
            new_native_calls=0, new_J_calls=0, new_ODE_steps=0,
            original_sigma_only_for_final_exact_norm=True,
            finite_representation_not_exact_conjugacy=True,
            native_accepted=False, task_completed=False)


class GaugeScaleContext:
    """Only unchanged sigma data are requested by the frozen equilibration loop."""
    def __init__(self, gauge, kernel):
        self.gauge, self.kernel = gauge, kernel

    def read_raw_array(self, capture, name):
        if capture is not self.gauge or name != 'original-scales':
            raise ValueError('Only the identical original sigma is delegated for equilibration')
        return self.gauge.original.raw(name)

    def decode_bits(self, word):
        return self.kernel.decode_bits(word)
