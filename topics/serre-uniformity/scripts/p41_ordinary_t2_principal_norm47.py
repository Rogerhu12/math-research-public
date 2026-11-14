#!/usr/bin/env python3
"""Actual Norm over the full cubic T2(P) of the retained ordinary Phi_C."""
import argparse
import gzip
import hashlib
import json
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


class Cubic:
    def __init__(self, A, B):
        self.A, self.B = A, B

    def mul(self, a, b):
        c = [0]*5
        for i in range(3):
            for j in range(3):
                c[i+j] += a[i]*b[j]
        for k in [4, 3]:
            c[k-2] -= self.A*c[k]
            c[k-3] -= self.B*c[k]
        return [x % Q for x in c[:3]]

    def matrix(self, a):
        cols = [a, self.mul(a, [0, 1, 0]), self.mul(a, [0, 0, 1])]
        return [[cols[j][i] for j in range(3)] for i in range(3)]

    def norm(self, a):
        m = self.matrix(a)
        return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
                -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])) % Q

    def inv(self, a):
        m = self.matrix(a)
        d = pow(self.norm(a), -1, Q)
        out = [(m[1][1]*m[2][2]-m[1][2]*m[2][1])*d % Q,
               (m[1][2]*m[2][0]-m[1][0]*m[2][2])*d % Q,
               (m[1][0]*m[2][1]-m[1][1]*m[2][0])*d % Q]
        assert self.mul(a, out) == [1, 0, 0]
        return out

    def power(self, a, n):
        if n < 0:
            return self.power(self.inv(a), -n)
        out = [1, 0, 0]
        while n:
            if n & 1:
                out = self.mul(out, a)
            n >>= 1
            if n:
                a = self.mul(a, a)
        return out


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
    assert support['complete_actual_T2_support']
    assert flat['complete_exact_integer_principal_function_expression']
    assert support['source_disk_id'] == flat['disk_id']
    manifest_path = args.transport_directory/'transport_manifest47.json'
    assert flat['input_sha256'][manifest_path.name] == sha(manifest_path)
    manifest = read(manifest_path)
    A, B = support['source_curve']
    field = Cubic(A, B)
    W = [r.from_json([x]) for x in support['W_coefficients_ascending_in_kernel_root']]

    def pmul(x, y):
        out = [r.zeros(1, max(x[0][0].shape[1], y[0][0].shape[1])) for _ in range(5)]
        for i in range(3):
            for j in range(3):
                out[i+j] = r.add(out[i+j], r.mul(x[i], y[j]))
        for k in [4, 3]:
            out[k-2] = r.sub(out[k-2], a.scale(out[k], A))
            out[k-3] = r.sub(out[k-3], a.scale(out[k], B))
        return out[:3]

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
            assert norm % P
            values[rec['label']] = value
            records.append({'label': rec['label'], 'line_bundle_power': degree,
                            'actual_section_value_coefficients_in_kernel_root': value,
                            'actual_cubic_norm_mod47four': norm})
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
        assert norm % P
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
    norm_map = {rec['label']: rec['actual_cubic_norm_mod47four'] for rec in records}
    for factor in flat['section_factors']:
        independent = independent*pow(norm_map[factor['label']], factor['signed_integer_exponent'], Q) % Q
    assert independent == norm
    output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
              'disk_id': flat['disk_id'], 'complete_actual_principal_norm_on_T2_P': True,
              'complete_all53_local_QC_heights': False, 'complete_common_roots': False,
              'actual_target_degree': 3, 'target_kernel_polynomial_ascending': [B, A, 0, 1],
              'actual_function': 'Phi_C, divisor=scale*(P_center-P_minus3)-A1(t)',
              'actual_Phi_value_in_cubic_target_algebra': Phi,
              'actual_norm_Phi_T2_P_mod47four': norm,
              'actual_log_norm_Phi_T2_P_mod47four': logunit(norm),
              'all455_function_sections_and_fixed_factors_unit': True,
              'all_evaluated_rational_sections_descend_to_cubic_real_subalgebra': True,
              'direct_cubic_norm_and_integer_factor_norm_product_equal': True,
              'all_function_section_values_and_norms': records,
              'fixed_section_values_and_norms': fixed_records,
              'V3_coefficients_ascending_in_kernel_root': [r.to_json(v)[0] for v in V3],
              'input_sha256': dict(a.inputs, **{p.name: sha(p) for p in [args.support, args.principal_expression, manifest_path]}),
              'source_sha256': sha(__file__)}
    save(args.output, output)
    print('PASS ACTUAL ORDINARY MOVING T2 NORM', flat['disk_id'], 'value', norm, 'log', logunit(norm),
          'SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
