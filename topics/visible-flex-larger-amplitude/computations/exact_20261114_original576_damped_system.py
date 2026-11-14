#!/usr/bin/env python3
"""The complete saved actual28 original576 matrix, for a new R273 direction.

This adapter has no RHS, Jacobian, ODE or solve implementation.  It verifies
the original capture and exposes exactly its original J/r/cut/far/scales
with a new explicit full-system identity.  It does not import a 1372-step
system or reuse a 1372 matrix scope.  Scientific consumers run only in this
public repository's Actions; a trial binder can reuse this byte-only view.
"""
from __future__ import annotations

import hashlib
import importlib
import json
import os
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
CAPTURE_READER = 'geometry_20261114_native_captured_band_correction.py'
CAPTURE_READER_SHA = 'b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390'
CAPTURE_RESULT_SHA = 'ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7'
FULL_J_SHA = '394ca2cc7c28ead3ffb963502ad24df86126c32f6e4eef10079495a753320a19'
MATRIX_SCOPE = 'actual28-original576-finite-binary64-complete-J-r-sigma-chain'
INPUT_NAMES = ('base-states', 'stage-residuals', 'stage-out', 'original-scales',
               'cut-residual', 'end-residual', 'original-far-graph',
               'physical-height', 'cut-target')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('The original576 scientific consumer belongs only to this public repository Actions')


def file_sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                    allow_nan=False).encode()).hexdigest()


def load_binding():
    path = HERE / CAPTURE_READER
    if file_sha(path) != CAPTURE_READER_SHA:
        raise ValueError('The original capture byte reader changed')
    module = importlib.import_module(path.stem)
    if Path(module.__file__).resolve() != path:
        raise ValueError('Unexpected original capture reader import path')
    return module


class Original576System:
    """Borrow the original capture without evaluating any scientific map."""

    def __init__(self, capture_directory, B=None):
        require_actions()
        self.B = load_binding() if B is None else B
        B = self.B
        B.same(file_sha(B.__file__), CAPTURE_READER_SHA, 'frozen original capture reader bytes')
        self.original = B.CapturedArrays(capture_directory, CAPTURE_RESULT_SHA)
        self.directory = self.original.directory
        self.M, self.K, self.depth = self.original.M, self.original.K, self.original.depth
        B.same((self.M, self.K, self.depth), (112, 224, 576), 'complete actual28 original576 layout')
        self.original_depth = self.depth
        self.old_to_new = list(range(self.depth+1))
        self.arrays = self.original.arrays
        self.spec, self.live = self.original.spec, self.original.live
        self._raw_cache = {}
        for name in INPUT_NAMES:
            if name not in self.arrays:
                raise ValueError('Missing original input array: '+name)
        self.cells = [dict(originalStage=n, rawCell=row['rawCell'],
            rawSegment=row['rawSegment'], kind='original-native-macro-stage')
            for n,row in enumerate(self.live['stages'])]
        self.J_rows = []
        full = hashlib.sha256()
        for expected,(n,J) in enumerate(self.original.stages()):
            B.same(n, expected, 'original576 block order')
            raw = B.float_bytes(J)
            B.same(len(raw), self.K*self.K*8, 'all original macro-J words')
            full.update(raw)
            self.J_rows.append(dict(stage=n, original_stage=n, bytes=len(raw),
                raw_sha256=hashlib.sha256(raw).hexdigest(), origin='unchanged-actual28-original-J',
                original_stage_location=self.cells[n]))
        B.same(len(self.J_rows), self.depth, 'all576 original J blocks')
        B.same(full.hexdigest(), FULL_J_SHA, 'full original J stream identity')
        raw_hashes = {name:self.arrays[name]['raw_sha256'] for name in INPUT_NAMES}
        definition = dict(schema='original576-complete-finite-matrix-definition-v1',
            matrix_scope=MATRIX_SCOPE, M=self.M, K=self.K, depth=self.depth,
            row_order='cut112, all576 stage224 rows, far112',
            variable_order='original577 node-major (allQ112, allPi112)',
            original_J_full_raw_sha256=FULL_J_SHA,
            block_manifest=[{k:x[k] for k in ('stage','bytes','raw_sha256')} for x in self.J_rows],
            original_input_raw_sha256=raw_hashes,
            cut_formula='delta[0,Q]+stored_cut_residual',
            stage_formula='J[n]*delta[n+1]-delta[n]+stored_stage_residual[n]',
            far_formula='delta[576,Pi]-original_diagonal_G*delta[576,Q]+stored_end_residual',
            row_sigma_rule='cut:sigma0; stage n:sigma_n; far:sigma576')
        self.binding = dict(schema='actual28-original576-complete-linear-system-binding-v1',
            matrix_scope=MATRIX_SCOPE, adapter_source_sha256=file_sha(__file__),
            frozen_capture_reader_sha256=CAPTURE_READER_SHA,
            original_capture_result_sha256=CAPTURE_RESULT_SHA,
            original_capture_result=dict(file='result.json', bytes=(self.directory/'result.json').stat().st_size,
                                         sha256=CAPTURE_RESULT_SHA),
            original_capture_binding=self.original.binding,
            modes=self.M, shape_dimension=self.K, depth=self.depth, original_depth=self.depth,
            node_count=self.depth+1, old_to_new=self.old_to_new, cells=self.cells,
            complete_block_manifest=self.J_rows, original_J_full_raw_sha256=FULL_J_SHA,
            raw_array_sha256=raw_hashes, matrix_identity_definition=definition,
            new_matrix_identity_sha256=canonical_sha(definition),
            original_macro_J_and_r_and_base_and_boundaries_scales_H_reused_byte_for_byte=True,
            all_original_nonzero_modes_rows_and_nodes_retained=True,
            no_1372_or_direct_LD_target_imported=True, no_step_partition_or_G_transformation=True,
            new_RHS_calls=0, new_J_calls=0, new_ODE_steps=0,
            no_native_solve_or_trial=True, no_linear_residual_acceptance_gate=True,
            native_accepted=False, task_completed=False)

    def raw(self, name):
        if name not in INPUT_NAMES:
            raise ValueError('Use staged access for original J, and only the nine bound original inputs')
        if name not in self._raw_cache:
            pieces = []
            for desc in self.arrays[name]['chunks']:
                raw = self.B.safe_file(self.directory, desc['file']).read_bytes()
                self.B.same(len(raw), desc['bytes'], 'original raw chunk size')
                self.B.same(hashlib.sha256(raw).hexdigest(), desc['raw_sha256'], 'original raw chunk identity')
                pieces.append(raw)
            raw = b''.join(pieces)
            self.B.same(hashlib.sha256(raw).hexdigest(), self.arrays[name]['raw_sha256'],
                        'complete original non-J raw array')
            self._raw_cache[name] = raw
        return self._raw_cache[name]

    def all(self, name):
        return np.frombuffer(self.raw(name), dtype='<f8').reshape(self.arrays[name]['shape'])

    def stages(self):
        for n,J in self.original.stages():
            self.B.same(hashlib.sha256(self.B.float_bytes(J)).hexdigest(), self.J_rows[n]['raw_sha256'],
                        'same original J block on every consumer pass')
            yield n,J

    def stage_bytes(self):
        for n,J in self.stages():
            yield n,self.B.float_bytes(J)

    def stage_raw(self, n):
        if not 0 <= n < self.depth:
            raise ValueError('Original576 stage range')
        for desc in self.arrays['stage-jacobians']['chunks']:
            if desc['row_start'] <= n < desc['row_stop']:
                raw = self.B.safe_file(self.directory, desc['file']).read_bytes()
                self.B.same(len(raw), desc['bytes'], 'original witness chunk size')
                self.B.same(hashlib.sha256(raw).hexdigest(), desc['raw_sha256'], 'original witness chunk hash')
                size = self.K*self.K*8
                start = (n-desc['row_start'])*size
                block = raw[start:start+size]
                self.B.same(hashlib.sha256(block).hexdigest(), self.J_rows[n]['raw_sha256'],
                            'original witness full J block hash')
                return block
        raise ValueError('Original stage has no complete raw chunk')

    def export_inputs(self, output):
        result = {}
        for name in INPUT_NAMES:
            desc = output.save('original576-system-'+name, self.all(name),
                'Unchanged complete actual28 original576 input bytes; no new nonlinear evaluation')
            self.B.same(desc['sha256'], self.arrays[name]['raw_sha256'],
                        'original input export preserves every byte: '+name)
            result[name] = desc
        return result


class Original576ExactContext:
    """The frozen integer row kernel on its actual original576 dimensions."""

    def __init__(self, system, kernel):
        self.system, self.kernel = system,kernel
        system.B.same((system.M,system.K,system.depth), (kernel.M,kernel.K,kernel.DEPTH),
                      'actual original576 kernel dimension contract')

    def max_record(self, kind, node, row, value, sigma_word):
        record = self.kernel.max_record(kind,node,row,value,sigma_word)
        record.update(matrix_scope=MATRIX_SCOPE,
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'])
        if kind == 'stage':
            record['source_stage'] = self.system.cells[node]
        return record

    def row_order(self, kind, node, row):
        return self.kernel.row_order(kind,node,row)

    def worst_witness(self, record, direction_raw, inputs):
        result = self.kernel.worst_witness(self.system.original, record, direction_raw, inputs)
        result.update(matrix_scope=MATRIX_SCOPE,
            new_matrix_identity_sha256=self.system.binding['new_matrix_identity_sha256'],
            complete_direction_float64le_sha256=hashlib.sha256(direction_raw).hexdigest(),
            kind=record['kind'],node=record['node'],row=record['row'])
        return result
