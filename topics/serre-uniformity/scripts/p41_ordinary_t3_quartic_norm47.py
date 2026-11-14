#!/usr/bin/env python3
"""Actual unit-section Norm over the irreducible quartic T3(P) of retained Phi_C."""
import argparse
import gzip
import hashlib
import json
from itertools import permutations
from pathlib import Path
import sys

P, Q = 47, 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(gzip.compress(raw, mtime=0))
    tmp.replace(path)


def logunit(x):
    assert x % P
    z = (pow(x, P-1, Q)-1) % Q
    assert z % P == 0
    return (z-z*z*pow(2, -1, Q)+z*z*z*pow(3, -1, Q))*pow(P-1, -1, Q) % Q


class Quartic:
    def __init__(self, polynomial):
        assert len(polynomial) == 5 and polynomial[-1] == 1
        self.poly = [x % Q for x in polynomial]

    def mul(self, a, b):
        c = [0]*7
        for i in range(4):
            for j in range(4):
                c[i+j] += a[i]*b[j]
        for k in [6, 5, 4]:
            for j in range(4):
                c[k-4+j] -= self.poly[j]*c[k]
        return [x % Q for x in c[:4]]

    def matrix(self, a):
        cols = [self.mul(a, [int(i == j) for i in range(4)]) for j in range(4)]
        return [[cols[j][i] for j in range(4)] for i in range(4)]

    def norm(self, a):
        matrix = self.matrix(a)
        total = 0
        for perm in permutations(range(4)):
            sign = -1 if sum(perm[i] > perm[j] for i in range(4) for j in range(i+1, 4)) % 2 else 1
            product = sign
            for i in range(4):
                product *= matrix[i][perm[i]]
            total += product
        return total % Q

    def inv(self, a):
        matrix = [row+[int(i == 0)] for i, row in enumerate(self.matrix(a))]
        assert self.norm(a) % P
        for k in range(4):
            pivot = next(i for i in range(k, 4) if matrix[i][k] % P)
            matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            inverse = pow(matrix[k][k], -1, Q)
            matrix[k] = [x*inverse % Q for x in matrix[k]]
            for i in range(4):
                if i != k:
                    scale = matrix[i][k]
                    matrix[i] = [(x-scale*y) % Q for x, y in zip(matrix[i], matrix[k])]
        result = [row[-1] for row in matrix]
        assert self.mul(a, result) == [1, 0, 0, 0]
        return result

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv(a), -n)
        result = [1, 0, 0, 0]
        while n:
            if n & 1:
                result = self.mul(result, a)
            n >>= 1
            if n:
                a = self.mul(a, a)
        return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--support', type=Path, required=True)
    ap.add_argument('--principal-expression', type=Path, required=True)
    ap.add_argument('--transport-directory', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_actual_differentials47 import ActualModel
    install_exact_float_mm(r)
    a = ActualModel(args.script_dir)
    np = a.np
    support, flat = read(args.support), read(args.principal_expression)
    assert support['complete_actual_T3_support']
    assert flat['complete_exact_integer_principal_function_expression']
    assert support['source_disk_id'] == flat['disk_id']
    manifest_path = args.transport_directory/'transport_manifest47.json'
    assert flat['input_sha256'][manifest_path.name] == sha(manifest_path)
    manifest = read(manifest_path)
    A, B = support['source_curve']
    kernel = support['kernel_polynomial_ascending']
    assert support['kernel_factor_degrees_mod47'] == [[4, 1]]
    field = Quartic(kernel)
    W = [r.from_json([x]) for x in support['W_coefficients_ascending_in_kernel_root']]

    def pmul(x, y):
        out = [r.zeros(1, max(x[0][0].shape[1], y[0][0].shape[1])) for _ in range(7)]
        for i in range(4):
            for j in range(4):
                out[i+j] = r.add(out[i+j], r.mul(x[i], y[j]))
        for k in [6, 5, 4]:
            for j in range(4):
                out[k-4+j] = r.sub(out[k-4+j], a.scale(out[k], kernel[j]))
        return out[:4]

    def pmat(x, M):
        return [r.mm(v, M) for v in x]

    def pcols(x, I):
        return [r.cols(v, I) for v in x]

    V2 = pmat(pmul(pcols(W, a.a2), pcols(W, a.b2)), a.C2)
    assert [r.to_json(v)[0] for v in V2] == support['V2_coefficients_ascending_in_kernel_root']
    f = pmat(W, a.fc)
    raw = pmul(pcols(V2, a.b3), [r.sub(x, r.mul(y, a.lam)) for x, y in zip(pcols(W, a.a3), f)])
    extra = pmat(raw, a.E3)
    first = pmul(f, V2)
    V3 = [r.hcat(r.sub(r.mul(x, a.ifP2), r.mm(y, a.C)), y) for x, y in zip(first, extra)]
    basis = {1: W, 2: V2, 3: V3}
    functions = []
    for entry in manifest['functions']:
        if entry['phase'] == 'formal_extraction':
            continue
        path = args.transport_directory/entry['filename']
        assert sha(path) == entry['sha256']
        functions.append(read(path))
    functions.sort(key=lambda rec: (-1, 0) if rec['phase'] == 'initial_negative'
                   else (rec['bit'], 0 if rec['operation'] == 'double_addflip' else 1))
    assert len(functions) == 455
    values, records = {}, []
    for degree in [2, 3]:
        group = [f for f in functions if f['line_bundle_power'] == degree]
        coefficients = r.hcat(*[r.from_json(f['numerator_coefficients']) for f in group])
        evaluated = pmat(basis[degree], coefficients)
        assert all(not np.any(e[1]) for e in evaluated)
        for j, rec in enumerate(group):
            value = [int(e[0][0, j]) for e in evaluated]
            norm = field.norm(value)
            assert norm % P, ('Nonunit true quartic section requires Weierstrass preparation', rec['label'])
            values[rec['label']] = value
            records.append({'label': rec['label'], 'line_bundle_power': degree,
                            'actual_section_value_coefficients_in_kernel_root': value,
                            'actual_quartic_norm_mod47four': norm})
    endpoint = flat['combined_function_to_actual_A1_t']
    fixed = {'fb': (1, flat['f_b_coefficients']), 'fc': (1, flat['f0_coefficients']),
             'v1': (1, endpoint['v1_weight2_coefficients']),
             'FP': (2, endpoint['F_terminal_V2_coefficients']),
             'GQ': (2, endpoint['G_terminal_V2_coefficients'])}
    fixed_records = {}
    for name, (degree, co) in fixed.items():
        evaluated = pmat(basis[degree], r.from_json(co))
        assert all(not np.any(e[1]) for e in evaluated)
        value = [int(e[0][0, 0]) for e in evaluated]
        norm = field.norm(value)
        assert norm % P, ('Nonunit true quartic fixed section requires Weierstrass preparation', name)
        values[name] = value
        fixed_records[name] = {'degree': degree, 'value_coefficients': value, 'norm': norm}
    initial, final = manifest['initial_node']['point_sha256'], manifest['final_node']['point_sha256']
    invfc = field.inv(values['fc'])
    nodes = {initial: field.mul(values['fb'], invfc)}
    degrees = {d: field.power(invfc, d) for d in [2, 3]}
    for rec in functions:
        value = field.mul(values[rec['label']], degrees[rec['line_bundle_power']])
        for parent in rec['input_nodes']:
            value = field.mul(value, field.inv(nodes[parent['point_sha256']]))
        nodes[rec['output_node']['point_sha256']] = value
    Phi = field.mul(field.inv(nodes[final]),
                    field.mul(field.mul(values['v1'], invfc), field.mul(values['FP'], field.inv(values['GQ']))))
    norm = field.norm(Phi)
    independent = pow(fixed_records['fb']['norm'], endpoint['f_b_integer_exponent'], Q)
    independent = independent*pow(fixed_records['fc']['norm'], endpoint['f0_integer_exponent'], Q) % Q
    independent = independent*fixed_records['v1']['norm']*fixed_records['FP']['norm']*pow(fixed_records['GQ']['norm'], -1, Q) % Q
    norm_map = {rec['label']: rec['actual_quartic_norm_mod47four'] for rec in records}
    for factor in flat['section_factors']:
        independent = independent*pow(norm_map[factor['label']], factor['signed_integer_exponent'], Q) % Q
    assert independent == norm
    output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
              'disk_id': flat['disk_id'], 'complete_actual_principal_norm_on_T3_P': True,
              'complete_all53_local_QC_heights': False, 'complete_common_roots': False,
              'actual_target_degree': 4, 'target_kernel_polynomial_ascending': kernel,
              'actual_function': 'Phi_C, divisor=scale*(P_center-P_minus3)-A1(t)',
              'actual_Phi_value_in_quartic_target_algebra': Phi,
              'actual_norm_Phi_T3_P_mod47four': norm,
              'actual_log_norm_Phi_T3_P_mod47four': logunit(norm),
              'all455_function_sections_and_fixed_factors_unit': True,
              'all_evaluated_rational_sections_descend_to_quartic_real_subalgebra': True,
              'direct_quartic_norm_and_integer_factor_norm_product_equal': True,
              'all_function_section_values_and_norms': records,
              'fixed_section_values_and_norms': fixed_records,
              'V3_coefficients_ascending_in_kernel_root': [r.to_json(v)[0] for v in V3],
              'input_sha256': dict(a.inputs, **{p.name: sha(p) for p in [args.support, args.principal_expression, manifest_path]}),
              'source_sha256': sha(__file__), 'complete_actual_local_sigma_F3_height': False}
    save(args.output, output)
    print('PASS ACTUAL ORDINARY MOVING T3 NORM', flat['disk_id'], 'value', norm, 'log', logunit(norm),
          'SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
