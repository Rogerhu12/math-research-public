#!/usr/bin/env python3
"""Run the frozen ordinary Abel engine while retaining every true principal function.

For AddFlip, div(F/f0^3)=D_P+D_Q+D_R, where D_T=E_T-div(f0).
The actual F in the published V3 basis is retained, without evaluation-only
specialization.  Direct negative flips similarly retain their V2 function.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0) if str(path).endswith('.gz') else raw)
    temp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, add_help=False)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--workdir', type=Path, required=True)
    ap.add_argument('--transport-dir', type=Path, required=True)
    args, passthrough = ap.parse_known_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import numpy as np
    import p41_r2_matrix as r
    import p41_group_operations47 as group
    import p41_formal47_multiply as multiply
    import p41_ordinary_Abel_multiply47 as runner
    from p41_projective_jet_frames47 import matrix_digest
    from p41_cm4_divisor47 import kernel
    based = read(args.based_points)
    assert based['complete19_actual_based_points']
    based_index = {p['disk_id']: p for p in based['records']}
    args.transport_dir.mkdir(parents=True, exist_ok=True)
    sources, source_hashes = group.load_sources(args.script_dir/'data')
    cusp = sources[1]
    K1 = r.from_json(kernel(73, cusp['cusp_rank_columns_1based'], cusp['cusp_free_columns_1based'], cusp['canonical_kernel_block']))
    fc = r.mm(K1, r.column(cusp['canonical_coefficients']))
    run_data = {
        'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': 47**4,
        'source_sha256': sha(__file__),
        'underlying_engine_sha256': sha(runner.__file__),
        'group_operations_sha256': sha(group.__file__),
        'addflip_engine_sha256': sha(multiply.__file__),
        'basis_input_sha256': source_hashes,
        'based_points_sha256': sha(args.based_points),
        'f0_weight2_coefficients': r.to_json(fc),
        'f_b_weight2_coefficients': based['f_b_coefficients'],
        'initial_principal_transport': 'h=f_b/f0; D_initial=C+div(h), C=P_center-P_minus3',
        'node_divisor_convention': 'D_T=E_T-div(f0), where point coordinates are H0(2L-E_T)',
        'V2_basis': 'Published source V2, identity on cusp.square_pivot_rows_1based',
        'V3_basis': 'Published source V3, identity on group.cubic_pivot_rows_1based',
        'normalization': 'Retain the exact rational_trace flip section; no scalar rescaling after extraction',
    }
    run_path = args.transport_dir/'run_manifest47.json'
    if run_path.exists():
        assert read(run_path) == run_data
    else:
        save(run_path, run_data)
    functions, node_scalars = {}, {}
    for disk_dir in sorted(args.transport_dir.glob('ORD_j*')):
        if not disk_dir.is_dir():
            continue
        disk_id = disk_dir.name
        functions[disk_id] = {}
        node_scalars[disk_id] = {based_index[disk_id]['point_sha256']: 1}
        for path in sorted(disk_dir.glob('function_*.json.gz')):
            record = read(path)
            functions[disk_id][record['label']] = record
            for n in record['input_nodes']+[record['output_node']]:
                old = node_scalars[disk_id].setdefault(n['point_sha256'], n['scalar_coefficient_of_C'])
                assert old == n['scalar_coefficient_of_C']
    original_flip = group.flip
    original_addflip = multiply.addflip
    original_extract = runner.extract_Abel
    active = []

    def get_disk(label):
        disk_id = label.split()[0]
        assert disk_id in based_index
        if disk_id not in functions:
            functions[disk_id] = {}
            node_scalars[disk_id] = {based_index[disk_id]['point_sha256']: 1}
        return disk_id

    def node(disk_id, K, A):
        point_sha = multiply.point_hash(K, A)
        assert point_sha in node_scalars[disk_id], ('missing earlier actual transport', disk_id, point_sha)
        return {'point_sha256': point_sha, 'scalar_coefficient_of_C': node_scalars[disk_id][point_sha]}

    def retain(S, AS, M, rng, label, degree):
        disk_id = get_disk(label)
        if degree == 3:
            assert active and active[-1]['label'] == label
            context = active[-1]
        else:
            K = r.rows(S, M['P2'])
            assert r.equal(r.mm(M['V2'], K), S)
            context = {'label': label, 'same': False, 'input_nodes': [node(disk_id, K, AS)]}
        result, Aresult, witness = original_flip(S, AS, M, rng, label)
        f_values = r.mm(S, r.column(witness['f_coefficients']))
        basis = M['V3'] if degree == 3 else M['V2']
        pivots = M['P3'] if degree == 3 else M['P2']
        coeff = r.rows(f_values, pivots)
        assert coeff[0].shape == (325 if degree == 3 else 199, 1)
        assert r.equal(r.mm(basis, coeff), f_values)
        assert np.all(r.units(f_values))
        assert r.equal(r.mm(M['A'+str(degree)], r.conjugate(coeff)), coeff)
        output_sha = multiply.point_hash(result, Aresult)
        scalar = -sum(n['scalar_coefficient_of_C'] for n in context['input_nodes'])
        old_scalar = node_scalars[disk_id].setdefault(output_sha, scalar)
        assert old_scalar == scalar
        is_initial = 'initial negative' in label
        is_formal = 'formal' in label
        step = re.search(r'(double|add) bit([0-9]+)$', label)
        assert is_initial or is_formal or step
        record = {
            'label': label, 'disk_id': disk_id,
            'phase': 'initial_negative' if is_initial else 'formal_extraction' if is_formal else 'scalar_multiplication',
            'operation': 'negative_flip' if degree == 2 else 'double_addflip' if context['same'] else 'addflip',
            'bit': int(step.group(2)) if step else None,
            'input_nodes': context['input_nodes'],
            'output_node': {'point_sha256': output_sha, 'scalar_coefficient_of_C': scalar},
            'output_sign': 1 if scalar >= 0 else -1,
            'output_magnitude': abs(scalar),
            'line_bundle_power': degree, 'modulus': 47**4,
            'numerator_basis': 'V'+str(degree),
            'numerator_coefficients': r.to_json(coeff),
            'fixed_denominator': 'f0^'+str(degree),
            'run_manifest_sha256': sha(run_path),
            'divisor_relation': 'div(F/f0^3)=D_P+D_Q+D_output' if degree == 3 else 'div(F/f0^2)=D_P+D_output',
            'SLP_relation': 'f_output=(F/f0^3)/(f_P*f_Q)' if degree == 3 else 'f_output=(F/f0^2)/f_P',
            'SLP_invariant': 'D_node=scalar_coefficient_of_C*C+div(f_node); f_initial=f_b/f0',
            'full820_source_interpolation_verified': True,
            'unit_on_all820_source_points': True,
            'actual_numerator_Frobenius_fixed': True,
            'full820_values_sha256': matrix_digest(f_values),
            'actual_flip_f_coefficients': witness['f_coefficients'],
        }
        if label in functions[disk_id]:
            assert functions[disk_id][label] == record
        else:
            directory = args.transport_dir/disk_id
            directory.mkdir(parents=True, exist_ok=True)
            filename = 'function_'+label.replace(' ', '_')+'.json.gz'
            save(directory/filename, record)
            functions[disk_id][label] = record
        return result, Aresult, witness

    def capture_flip2(S, AS, M, rng, label):
        return retain(S, AS, M, rng, label, 2)

    def capture_flip3(S, AS, M, rng, label):
        return retain(S, AS, M, rng, label, 3)

    def capture_addflip(KP, AP, KQ, AQ, M, rng, label, same=False):
        disk_id = get_disk(label)
        inputs = [node(disk_id, KP, AP), node(disk_id, KQ, AQ)]
        active.append({'label': label, 'same': same, 'input_nodes': inputs})
        try:
            return original_addflip(KP, AP, KQ, AQ, M, rng, label, same=same)
        finally:
            active.pop()

    def disk_manifest(disk_id, multiplication_path, Abel_path=None):
        data = read(multiplication_path)
        assert data['bits_done'] == data['target_bits'] == 304 and len(data['steps']) == 454
        assert 'zero_test_mod47' in data
        primary = [x for x in functions[disk_id].values() if x['phase'] == 'scalar_multiplication']
        initial = [x for x in functions[disk_id].values() if x['phase'] == 'initial_negative']
        assert len(primary) == 454 and len(initial) == 1
        last = next(x for x in primary if x['output_node']['point_sha256'] == data['point_sha256'])
        assert last['output_node']['scalar_coefficient_of_C'] == data['sign']*multiply.H
        entries = []
        for path in sorted((args.transport_dir/disk_id).glob('function_*.json.gz')):
            rec = read(path)
            entries.append({'filename': path.name, 'sha256': sha(path), 'bytes': path.stat().st_size,
                            'label': rec['label'], 'phase': rec['phase']})
        manifest = {
            'disk_id': disk_id, 'complete_all454_multiplication_principal_functions': True,
            'complete_initial_negative_principal_function': True,
            'run_manifest_sha256': sha(run_path),
            'multiplication_sha256': sha(multiplication_path),
            'initial_node': {'point_sha256': based_index[disk_id]['point_sha256'], 'scalar_coefficient_of_C': 1},
            'final_node': last['output_node'],
            'final_principal_function': 'f_final^(-1); its divisor is sign*m*C-D_final',
            'initial_principal_function': 'f_b/f0',
            'functions': entries,
            'norm_derivative_interface': 'Evaluate retained V2/V3 section quotients on the actual family2 jets. Preserve Laurent principal parts and finite parts at intersections.',
            'completed_Abel_sha256': sha(Abel_path) if Abel_path is not None and Abel_path.exists() else None,
            'source_sha256': sha(__file__),
        }
        save(args.transport_dir/disk_id/'transport_manifest47.json', manifest)
        print('PASS all454 actual principal functions retained', disk_id, flush=True)

    def capture_extract(a, multiple, multiplication_path, tiny_path, output):
        disk_manifest(multiple['disk_id'], multiplication_path)
        result = original_extract(a, multiple, multiplication_path, tiny_path, output)
        disk_manifest(multiple['disk_id'], multiplication_path, output)
        return result

    group.flip = capture_flip2
    multiply.flip = capture_flip3
    multiply.addflip = capture_addflip
    runner.extract_Abel = capture_extract
    sys.argv = [str(Path(runner.__file__).resolve()), '--script-dir', str(args.script_dir),
                '--based-points', str(args.based_points), '--workdir', str(args.workdir)]+passthrough
    runner.main()
    for disk_id in functions:
        mp = args.workdir/(disk_id+'_multiply47.json.gz')
        ab = args.workdir/(disk_id+'_Abel47.json.gz')
        if mp.exists() and ab.exists():
            disk_manifest(disk_id, mp, ab)


if __name__ == '__main__':
    main()
