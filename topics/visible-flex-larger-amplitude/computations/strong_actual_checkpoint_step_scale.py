#!/usr/bin/env python3
"""Read-only coordinate-scale diagnostic between two saved inner iterates.

No physical RHS, Jacobian, tail, geometry audit or new BVP is evaluated. The
finite difference of two complete saved states reconstructs the accepted
Newton direction and its original Euclidean merit. A coordinate scaling is
reported only as arithmetic; no different line search is run or endorsed.
"""
from __future__ import annotations
import argparse
import array
import ast
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read_document(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data), sha(data)


def read_vector(path, record, key, hashes):
    spec = record['arrays'][key]
    values = array.array('d')
    for chunk in spec['chunks']:
        name = chunk['file']
        if Path(name).name != name or chunk['first'] != len(values):
            raise ValueError('Nonlocal or noncontiguous raw chunk')
        source = path.parent/name
        compressed = source.read_bytes()
        if sha(compressed) != chunk['sha256']:
            raise ValueError('Raw chunk SHA differs')
        hashes[str(source)] = chunk['sha256']
        data = gzip.decompress(compressed)
        if data[:6] != b'\x93NUMPY' or data[6:8] not in (b'\x01\x00', b'\x02\x00'):
            raise ValueError('Only the actual plain npy format is supported')
        size = 2 if data[6] == 1 else 4
        length = int.from_bytes(data[8:8+size], 'little')
        offset = 8+size+length
        header = ast.literal_eval(data[8+size:offset].decode())
        if (header['descr'] != '<f8' or header['fortran_order'] or
                header['shape'] != (chunk['count'],) or len(data)-offset != 8*chunk['count']):
            raise ValueError('Unexpected exact raw float64 array layout')
        piece = array.array('d')
        piece.frombytes(data[offset:])
        if sys.byteorder != 'little':
            piece.byteswap()
        if not all(map(math.isfinite, piece)):
            raise ValueError('Nonfinite raw coordinate')
        values.extend(piece)
    if len(values) != math.prod(spec['shape']):
        raise ValueError('Incomplete raw array')
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('before', 'after', 'scale-response', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--alpha', type=float, required=True)
    parser.add_argument('--original-merit', type=float, required=True)
    args = parser.parse_args()
    if not 0 < args.alpha <= 1 or args.original_merit <= 0 or args.out.exists():
        raise ValueError('Positive original step/merit and a fresh output are required')
    before, h0 = read_document(args.before)
    after, h1 = read_document(args.after)
    response, hr = read_document(args.scale_response)
    hashes = {str(args.before): h0, str(args.after): h1, str(args.scale_response): hr,
              str(Path(__file__)): sha(Path(__file__).read_bytes())}
    first, second = before['identity'], after['identity']
    keys = ('modes', 'angular', 'gauge', 'fixed', 'reference_coefficients',
            'reference_frequencies', 'numerical_reference_knots', 'parameter_layout',
            'physical_tail_parameters', 'physical_tail_cut')
    if any(first[k] != second[k] for k in keys):
        raise ValueError('The saved coordinates or fixed physical tail differ')
    if after['provenance']['phase'] != 'accepted-newton' or after['solver_success']:
        raise ValueError('Expected the explicitly pending accepted inner iterate')
    if response['baseline']['gauge'] != first['gauge']:
        raise ValueError('Coefficient-scale gauge differs')
    vectors0 = {k: read_vector(args.before, before, k, hashes) for k in ('x', 'y', 'p')}
    vectors1 = {k: read_vector(args.after, after, k, hashes) for k in ('x', 'y', 'p')}
    if vectors0['x'] != vectors1['x'] or before['arrays']['y']['shape'] != after['arrays']['y']['shape']:
        raise ValueError('This diagnostic requires the same full numerical mesh')
    M, q = first['modes'], first['gauge']
    n, nodes = before['arrays']['y']['shape']
    if len(vectors0['p']) != M+3 or len(vectors1['p']) != M+3 or n != 3*M+1:
        raise ValueError('Expected the original complete augmented layout')
    ds_y = [(b-a)/args.alpha for a,b in zip(vectors0['y'], vectors1['y'])]
    ds_p = [(b-a)/args.alpha for a,b in zip(vectors0['p'], vectors1['p'])]
    norm_y = math.fsum(v*v for v in ds_y)
    norm_p = math.fsum(v*v for v in ds_p)
    cost = norm_y+norm_p
    relative = abs(cost/args.original_merit-1)
    if relative > 2e-10:
        raise ValueError('Saved full difference does not reproduce the supplied original Newton merit')
    scales = response['physical_core_parameter_scales'][1:]
    if len(scales) != M-1:
        raise ValueError('All coefficient scales are required')
    derivative_units = [q*math.exp(vectors0['p'][0]), *scales, 1., 1., 1.]
    physical_deltas = [q*(math.exp(vectors1['p'][0])-math.exp(vectors0['p'][0]))]
    physical_deltas += [(vectors1['p'][j]-vectors0['p'][j])*derivative_units[j] for j in range(1,M+3)]
    weighted = [(derivative_units[j]/q if j<M else 1.)*ds_p[j] for j in range(M+3)]
    rows = [dict(index=j, role=('c'+str(2*(j+1)) if j<M else ('delta','boost_length','boost_speed')[j-M]),
                 raw_step=ds_p[j], raw_merit_fraction=ds_p[j]**2/cost,
                 exact_accepted_physical_delta=physical_deltas[j],
                 initial_physical_derivative_unit=derivative_units[j]) for j in range(M+3)]
    field_index = max(range(len(ds_y)), key=lambda i: abs(ds_y[i]))
    result = dict(scope=__doc__, source_sha256=hashes, original_alpha=args.alpha,
        supplied_original_merit=args.original_merit, reconstructed_original_merit=cost,
        merit_relative_difference=relative, raw_field_squared_norm=norm_y,
        raw_parameter_squared_norm=norm_p, raw_parameter_merit_fraction=norm_p/cost,
        maximum_raw_field_step=abs(ds_y[field_index]),
        maximum_field_location=dict(state_component=field_index//nodes, node=field_index%nodes),
        maximum_raw_parameter_step=max(abs(v) for v in ds_p),
        raw_parameter_rows=rows,
        parameter_rows_descending_merit=sorted(rows,key=lambda r:r['raw_merit_fraction'],reverse=True),
        arithmetic_alternative_cost_field_plus_core_in_gauge_units=norm_y+math.fsum(v*v for v in weighted),
        exact_accepted_core_rho_change_Fourier_l1=math.fsum((4*(j+1)**2-1)*abs(physical_deltas[j]) for j in range(M)),
        all_actual_core_modes_retained=True, original_y_order='state-major C order from raw manifest',
        physical_field_warning='q times the state coefficient difference is not the full Cartesian immersion change when profile/chart change.',
        alternative_merit_was_not_used=True, alternative_trial_acceptance_unknown=True,
        physical_surface=False, actual_coupled_acceptance_pending=True,
        used_arrays=['x','y','p'], cubic_not_reaudited_by_this_arithmetic=True,
        physical_RHS_evaluations=0, Jacobian_evaluations=0, tail_workers=0)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('reconstructed_original_merit','merit_relative_difference',
        'raw_parameter_merit_fraction','maximum_raw_field_step','maximum_raw_parameter_step',
        'arithmetic_alternative_cost_field_plus_core_in_gauge_units',
        'exact_accepted_core_rho_change_Fourier_l1')}), flush=True)


if __name__ == '__main__':
    main()
