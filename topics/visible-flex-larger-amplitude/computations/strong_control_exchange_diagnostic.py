#!/usr/bin/env python3
"""Instrument one current successful-prefix response Jacobian, without solving.

This leaves strong_control_response.py and its equations unchanged. It saves
the exact coordinate mesh, warm state and linearized field directions, and
examines the small endpoint/parameter matrix after balanced QR elimination.
The reported condition numbers are for that reduced matrix, not the entire
collocation Jacobian and not a proof of a geometric fold. Physical control
column replacements are evaluated at the same successful baseline. No
nonlinear trial, accepted new surface, or fixed-g refinement is produced.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import sys
import types
import numpy as np

HERE = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def spectral_condition(matrix):
    singular = np.linalg.svd(matrix, compute_uv=False)
    return dict(dimension=list(matrix.shape), sigma_max=float(singular[0]),
                sigma_min=float(singular[-1]),
                condition_2=float(singular[0] / singular[-1]),
                singular_values=singular.tolist())


class ExchangeRecorder:
    def __init__(self, prefix, entry_hashes):
        self.prefix = prefix
        self.entry_hashes = entry_hashes
        self.arrays = []
        self.rows = []
        self.started = False

    def save(self, name, value):
        stream = io.BytesIO()
        np.save(stream, np.asarray(value), allow_pickle=False)
        path = Path(str(self.prefix) + '-' + name + '.npy.gz')
        payload = gzip.compress(stream.getvalue(), compresslevel=9, mtime=0)
        if len(payload) >= 5_000_000:
            raise ValueError('Direction checkpoint exceeds the repository file limit')
        path.write_bytes(payload)
        record = dict(file=str(path), shape=list(np.shape(value)),
                      bytes=len(payload), sha256=digest(payload))
        self.arrays.append(record)
        return record

    def start(self, obj, factor, x, y, p, baseline):
        if self.started:
            raise RuntimeError('Only one baseline Jacobian is permitted')
        self.started = True
        self.n, self.m, self.k = y.shape[0], y.shape[1], len(p)
        self.q = float(obj.q)
        self.coefficient_scales = np.asarray(obj.pscale[1:], float).copy()
        if self.k != obj.M or len(self.coefficient_scales) != self.k - 2:
            raise ValueError('This diagnostic requires the ordinary dual core layout')
        packed, pivots = factor.final_lu
        # The row permutation does not change singular values. L U therefore
        # suffices without undoing the LU pivots, for all later column changes.
        self.coarse = ((np.tril(packed, -1) + np.eye(len(packed)))
                       @ np.triu(packed))
        if self.coarse.shape != (2*self.n+self.k, 2*self.n+self.k):
            raise ValueError('Unexpected balanced QR root matrix')
        self.units = np.r_[np.full(2*self.n, self.q), np.ones(2),
                           self.coefficient_scales]
        self.baseline_conditions = dict(
            scope='Endpoint/parameter matrix after the same orthogonal interior elimination; not the full BVP condition number.',
            numerical_variable_units=spectral_condition(self.coarse),
            physical_correction_coefficient_and_core_column_units=spectral_condition(
                self.coarse / self.units[None, :]),
            column_unit_factors=self.units.tolist(),
            unit_definition='Physical Fourier correction coefficients=q*y at each endpoint; delta/LB have unit scale; actual c6 and higher coefficients=pscale*p. The moving reference geometry is not included in q*y alone. No row equilibration is inserted.',
            baseline=baseline)
        self.save('t', x)
        self.save('warm-y', y)
        self.save('warm-p', p)

    def record(self, name, direction, row):
        if not self.started:
            raise RuntimeError('No response baseline')
        row['physical_state_derivative_scope'] = (
            'The inherited q*max(abs(dy)) measures only the finite Fourier '
            'correction coefficients at fixed numerical coordinates. A '
            'physical position derivative also includes the moving reference '
            'geometry. The complete BVP direction and physical profile '
            'direction are saved separately for a valid warm predictor.')
        self.save('direction-' + name, direction)
        n, m = self.n, self.m
        edge = np.r_[direction[:n], direction[n*(m-1):n*m],
                     direction[n*m:]]
        # The response solves J u = -R_field. Eliminate the same internal
        # variables: the external unit-field column is -A_root u_edge.
        external_column = -self.coarse @ edge
        exchange_column = 2*n + 2  # Natural c6 parameter in the dual system.
        exchanged = self.coarse.copy()
        exchanged[:, exchange_column] = external_column
        units = self.units.copy()
        units[exchange_column] = 1.0  # One actual unit of the external field.
        physical = exchanged / units[None, :]
        dc6 = float(row['core_derivative'][2])
        record = dict(
            direction=name,
            scope='Linearized replacement of the natural-c6 unknown by one unit of this external physical direction at the same baseline; no nonlinear continuation.',
            replaced_parameter_index=2,
            natural_c6_derivative=dc6,
            scaled_column_replacement_determinant_ratio=float(-edge[exchange_column]),
            ratio_identity='det(J with c6 parameter column replaced by R_field)/det(J)=-dc6_dfield/pscale_c6, with the same column ordering.',
            physical_correction_coefficient_and_core_column_units=spectral_condition(physical),
            unchanged_c6_scale=float(self.coefficient_scales[0]),
            linearized_equation_relative_backward_error=row['equation_relative_backward_error'])
        # Column norm equilibration is reported separately as a numerical
        # comparison. It is not used in the solve or the physical prediction.
        norms = np.linalg.norm(physical, axis=0)
        record['column_l2_equilibrated'] = spectral_condition(
            physical / np.maximum(norms, np.finfo(float).tiny)[None, :])
        self.rows.append(record)
        return record

    def half(self, name, first, second):
        record = self.save('half-direction-' + name, second)
        units = np.r_[np.full(self.n*self.m, self.q), np.ones(2),
                      self.coefficient_scales]
        a, b = units*first, units*second
        record.update(
            scope='Same exact Jacobian with the external physical residual column evaluated at half the centered finite-difference width.',
            full_coefficient_and_parameter_direction_max_difference=float(np.max(abs(a-b))),
            full_coefficient_and_parameter_direction_relative_difference=float(
                np.max(abs(a-b))/max(np.max(abs(a)), np.finfo(float).tiny)),
            physical_parameter_derivative=b[self.n*self.m:].tolist(),
            c6_column_exchange_determinant_ratio=float(-second[self.n*self.m+2]))
        return record

    def result(self):
        return dict(scope=__doc__, entry_source_sha256=self.entry_hashes,
                    baseline_reduced_matrix=self.baseline_conditions,
                    control_column_exchanges=self.rows,
                    warm_only_tangent_arrays=self.arrays,
                    nonlinear_solution=False)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--exchange-array-prefix', type=Path, required=True)
    opts, remaining = parser.parse_known_args()
    sys.argv = [sys.argv[0]] + remaining
    response_path = HERE / 'strong_control_response.py'
    original = response_path.read_text()
    hashes = {name: digest((HERE / name).read_bytes()) for name in (
        'strong_control_exchange_diagnostic.py', 'strong_control_response.py',
        'strong_neck_bvp.py', 'strong_block_qr.py', 'root_block_collocation.py',
        'root_dual_core_bvp.py', 'strong_flow_lru.py')}
    recorder = ExchangeRecorder(opts.exchange_array_prefix, hashes)
    replacements = [
        ('        rows=[];target_delta=',
         '        _exchange.start(obj,factor,x,y,p,baseline)\n'
         '        rows=[];target_delta='),
        ('            rows.append(row);print(json.dumps(row),flush=True)',
         '            if second is not None:row["half_step_linearized_field"]=_exchange.half(name,direction,d2)\n'
         '            row["control_column_exchange"]=_exchange.record(name,direction,row)\n'
         '            rows.append(row);print(json.dumps(row),flush=True)'),
        ('        opts.response_output.write_text(json.dumps(result,indent=2)+\'\\n\')',
         '        result["exchange_diagnostic"]=_exchange.result()\n'
         '        opts.response_output.write_text(json.dumps(result,indent=2)+\'\\n\')')]
    source = original
    for old, new in replacements:
        if source.count(old) != 1:
            raise RuntimeError('Response instrumentation anchor changed: ' + repr(old))
        source = source.replace(old, new)
    module = types.ModuleType('strong_exact_response_exchange')
    module.__file__ = str(response_path)
    module.__dict__['_exchange'] = recorder
    exec(compile(source, str(response_path), 'exec'), module.__dict__)
    module.main()


if __name__ == '__main__':
    main()
