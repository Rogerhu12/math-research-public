#!/usr/bin/env python3
"""Actual selected SS second-kind integrals and explicit terminal divisor transport from retained principal functions.

The terminal divisor is explicitly moved to the R141 first small Abel
family.  Its degree126 base section v1/f0 is retained.  Together with
every actual multiplication function this gives all54 R240 integrals.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys

P = 47
Q = P**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


class Engine:
    def __init__(self, script_dir, based_path, nu_path, build_dir):
        import p41_r2_matrix as r
        from p41_projective_jet_frames47 import install_exact_float_mm
        from p41_native_r2_linear47 import install
        from p41_actual_differentials47 import ActualModel
        from p41_hecke3_hessian47 import section_jets
        from p41_elliptic_coarse_atlas47 import Series
        from p41_scalar_primitive_atlas47 import scalar_gm
        install_exact_float_mm(r)
        self.native = install(r, build_dir)
        self.a = a = ActualModel(script_dir)
        self.r, self.np, self.M = r, a.np, a.M
        self.inputs = dict(a.inputs)
        self.based = read(based_path)
        self.nu = read(nu_path)
        self.inputs[based_path.name], self.inputs[nu_path.name] = sha(based_path), sha(nu_path)
        assert self.based['complete_selected_SS_actual_based_points']
        assert self.nu['all54_actual_variational_second_kind_forms_complete']
        assert self.nu['integral_de_Rham_basis_dimension'] == 108
        self.nu_path = nu_path
        base_path = script_dir/'data/p41_hecke3_abel_bases_checkpoint.json.gz'
        jets_path = script_dir/'data/p41_source_cubic47_full_saved.json.gz'
        self.base, self.jets = read(base_path), read(jets_path)
        self.inputs[base_path.name], self.inputs[jets_path.name] = sha(base_path), sha(jets_path)
        assert self.base['jets_sha256'] == sha(jets_path)
        self.family = self.base['families'][0]
        self.I1 = [j-1 for j in self.family['points_1based']]
        self.I2 = [j-1 for j in self.nu['pole_indices_1based']]
        assert self.family['points_1based'] == self.nu['calibration_indices_1based']
        assert self.base['families'][1]['points_1based'] == self.nu['pole_indices_1based']
        self.tau2 = [self.I2.index(self.M['tau'][i]) for i in self.I2]
        allpoints = [x-1 for x in self.jets['point_indices_1based']]
        assert allpoints == list(range(820))
        self.W = [r.from_json(x) for x in self.jets['evaluation_coefficients']]
        assert len(self.W) == 4 and r.equal(self.W[0], self.M['W'])
        sources = [a.model, a.cusp, a.cm4, a.group]
        self.V2, self.V3 = section_jets(self.W[:3], sources, self.M, r)
        assert r.equal(self.V2[0], self.M['V2']) and r.equal(self.V3[0], self.M['V3'])
        self.family2_jets = {
            1: [r.rows(w, self.I2) for w in self.W[:2]],
            2: [r.rows(v, self.I2) for v in self.V2[:2]],
            3: [r.rows(v, self.I2) for v in self.V3[:2]],
        }
        self.dlog_f0 = self.dlog_section(a.fc, 1)
        self.fb = r.from_json(self.based['f_b_coefficients'])
        self.dlog_initial = r.sub(self.dlog_section(self.fb, 1), self.dlog_f0)
        self.v1 = r.from_json(self.family['v_coefficients'])
        self.dlog_family_base = r.sub(self.dlog_section(self.v1, 1), self.dlog_f0)
        # Actual second-kind differentials along the first physical Abel family.
        den = r.from_json(self.nu['denominator_linear_section'])
        numer = r.from_json(self.nu['numerator_cubic_sections'])
        values = [r.mm(r.rows(w, self.I1), den) for w in self.W[:3]]
        assert self.np.all(r.units(values[0]))
        s = Series(a, 3)
        inverse_squared = s.power(s.inverse(values), 2)
        numerator = [r.mm(r.rows(v, self.I1), numer) for v in self.V3[:3]]
        quotient = s.mul(numerator, inverse_squared)
        aa, beta = scalar_gm((1, 0), (32, 0), False, 3)
        self.nu_series = []
        for n in range(3):
            value = r.zeros(54, 54)
            for k in range(n+1):
                assert beta[n-k][1] == 0
                value = r.add(value, a.scale(quotient[k], beta[n-k][0]))
            self.nu_series.append(value)
        assert r.equal(self.nu_series[0], r.from_json(self.nu['calibration_parameter_matrix']))
        self.inputs.update(a.inputs)

    def dlog_section(self, coefficient, degree):
        r, np = self.r, self.np
        J = self.family2_jets[degree]
        value, derivative = r.mm(J[0], coefficient), r.mm(J[1], coefficient)
        assert np.all(r.units(value))
        result = r.mul(derivative, r.inverse_values(value))
        return result[0].T.copy(), result[1].T.copy()

    def covariance(self, row):
        assert self.r.equal(self.r.cols(row, self.tau2), self.r.conjugate(row))

    def endpoint(self, Abel_path, multiple_path):
        from p41_formal47_exponential import construct_point
        from p41_cm4_divisor47 import kernel
        from p41_formal47_multiply import point_hash
        from p41_group_operations47 import flip
        a, r, np, M = self.a, self.r, self.np, self.M
        ab, multiple = read(Abel_path), read(multiple_path)
        assert ab['complete_actual_center_Abel_constant']
        assert ab['input_sha256'][multiple_path.name] == sha(multiple_path)
        assert multiple['bits_done'] == multiple['target_bits'] == 304 and 'zero_test_mod47' in multiple
        assert multiple['disk_id'] == ab['disk_id']
        K, A = r.from_json(multiple['point_coordinates']), r.from_json(multiple['point_frobenius'])
        assert point_hash(K, A) == multiple['point_sha256'] == ab['actual_multiple_point_sha256']
        target = r.from_json(ab['canonical_log_signed_mC_mod47four'])
        KQ, AQ, exponential = construct_point(target, self.family, self.jets, a.cusp, M, r, kernel)
        negative = ab['negative_witness']
        KR = r.from_json(kernel(199, negative['rank_columns_1based'], negative['free_columns_1based'], negative['kernel_block']))
        AR = r.from_json(negative['frobenius_matrix'])
        assert r.equal(r.mm(KR, AR), r.mm(M['A2'], r.conjugate(KR)))
        rng = random.Random(2440147+int(ab['disk_id'][-2:]))
        for attempt in range(20):
            if attempt:
                KR, AR, negative = flip(r.mm(M['V2'], K), A, M, rng, ab['disk_id']+' endpoint negative alternative')
            relation_matrix = r.hcat(KQ, r.neg(KR))
            rr, cc = r.rank_pivots(relation_matrix)
            if len(rr) != 145:
                continue
            relation, free, block = r.kernel_from_rows(r.rows(relation_matrix, rr), rr, cc)
            assert relation[0].shape == (146, 1) and r.iszero(r.mm(relation_matrix, relation))
            G = r.mm(KQ, r.rows(relation, list(range(73))))
            assert r.equal(G, r.mm(KR, r.rows(relation, list(range(73, 146)))))
            gv = r.mm(M['V2'], G)
            choices = [i for i in range(820) if M['tau'][i] == i and r.units(gv)[i, 0]]
            assert choices
            normalization = choices[0]
            G = r.mul(G, r.inverse_values(r.rows(gv, [normalization])))
            assert r.equal(r.mm(M['A2'], r.conjugate(G)), G)
            F = r.mm(K, r.column(negative['f_coefficients']))
            Fvalues = r.mm(M['V2'], F)
            assert np.all(r.units(Fvalues))
            assert r.equal(r.mm(M['A2'], r.conjugate(F)), F)
            # Verify the full divisor transport, not merely membership in the
            # intersection (which by itself need not handle common support).
            # Multiplication by G/F carries the entire actual ideal of E_final
            # isomorphically to the entire actual ideal of E_Q.
            Gvalues = r.mm(M['V2'], G)
            ratio = r.mul(Gvalues, r.inverse_values(Fvalues))
            transported = r.mul(ratio, r.mm(M['V2'], K))
            transported_coeff = r.rows(transported, M['P2'])
            assert r.equal(r.mm(M['V2'], transported_coeff), transported)
            qr, qc = r.rank_pivots(KQ)
            assert len(qr) == 73
            change = r.mm(r.inverse_matrix(r.rows(KQ, qr)), r.rows(transported_coeff, qr))
            assert r.equal(r.mm(KQ, change), transported_coeff)
            assert len(r.rank_pivots(change)[0]) == 73
            # Numerator F and denominator G differ exactly by E_final-E_Q.
            dlog = r.add(self.dlog_family_base, r.sub(self.dlog_section(F, 2), self.dlog_section(G, 2)))
            self.covariance(dlog)
            break
        else:
            raise AssertionError('No complete actual terminal divisor transport')
        t = r.from_json(exponential['parameters'])
        assert t[0].shape == (1, 54) and all(not np.any(x % P) for x in t)
        tiny = r.zeros(1, 54)
        power = t
        for n in range(3):
            tiny = r.add(tiny, a.scale(r.mm(power, self.nu_series[n]), pow(n+1, -1, Q)))
            power = r.mul(power, t)
        self.covariance(tiny)
        actual = r.add(tiny, dlog)
        self.covariance(actual)
        result = {
            'disk_id': ab['disk_id'],
            'complete_actual_terminal_family1_transport': True,
            'canonical_log_target_mod47four': r.to_json(target),
            'family1_physical_parameters_mod47four': r.to_json(t),
            'family1_points_1based': self.family['points_1based'],
            'family1_effective_point_coordinates': r.to_json(KQ),
            'family1_effective_point_frobenius': r.to_json(AQ),
            'full_exponential_reconstruction': exponential,
            'negative_divisor_point_sha256': point_hash(KR, AR),
            'negative_divisor_witness': negative,
            'terminal_transport_numerator_V2': r.to_json(F),
            'terminal_transport_denominator_V2': r.to_json(G),
            'terminal_transport_denominator_normalization_point_1based': normalization+1,
            'intersection_rank': 145, 'intersection_rank_rows_0based': rr,
            'intersection_rank_columns_0based': cc,
            'intersection_kernel_block': r.to_json(block),
            'full_principal_ideal_transport_change_matrix': r.to_json(change),
            'full820_by73_principal_ideal_transport_verified': True,
            'principal_transport_ideal_change_rank': 73,
            'alternative_negative_attempt_0based': attempt,
            'terminal_transport_function': '(v1/f0)*(F/G)',
            'terminal_transport_divisor': 'D_final-A1(t), A1(t)=sum(P1_j(t_j)-P1_j(0))',
            'base_section_factor_v1_over_f0_retained': True,
            'terminal_transport_log_norm_derivative_at_family2_mod47four': r.to_json(dlog),
            'actual_second_kind_tiny_integrals_at_family1_mod47four': r.to_json(tiny),
            'actual_second_kind_integrals_over_Dfinal_mod47four': r.to_json(actual),
            'all54_family2_evaluation_denominators_unit': True,
            'family2_Frobenius_covariance_verified': True,
            'multiplication_sha256': sha(multiple_path), 'Abel_sha256': sha(Abel_path),
        }
        print('PASS actual family1 endpoint, rank145 principal transport and54 tiny second-kind integrals', ab['disk_id'], flush=True)
        return result, actual, multiple

    def chain(self, disk_id, directory, multiple):
        from p41_formal47_multiply import H
        a, r = self.a, self.r
        manifest_path = directory/'transport_manifest47.json'
        manifest = read(manifest_path)
        run_path = directory.parent/'run_manifest47.json'
        run = read(run_path)
        assert manifest['complete_all454_multiplication_principal_functions']
        assert manifest['complete_initial_negative_principal_function']
        assert manifest['run_manifest_sha256'] == sha(run_path)
        assert run['f0_weight2_coefficients'] == r.to_json(a.fc)
        assert run['f_b_weight2_coefficients'] == r.to_json(self.fb)
        based_point = next(p for p in self.based['records'] if p['disk_id'] == disk_id)
        initial_sha = based_point['point_sha256']
        values = {initial_sha: self.dlog_initial}
        scalars = {initial_sha: 1}
        functions = []
        for entry in manifest['functions']:
            if entry['phase'] == 'formal_extraction':
                continue
            path = directory/entry['filename']
            assert sha(path) == entry['sha256']
            functions.append(read(path))
        functions.sort(key=lambda rec: (-1, 0) if rec['phase'] == 'initial_negative'
                       else (rec['bit'], 0 if rec['operation'] == 'double_addflip' else 1))
        assert len(functions) == 455
        function_derivatives = []
        for rec in functions:
            assert rec['disk_id'] == disk_id and rec['run_manifest_sha256'] == sha(run_path)
            assert rec['unit_on_all820_source_points'] and rec['full820_source_interpolation_verified']
            degree = rec['line_bundle_power']
            coefficient = r.from_json(rec['numerator_coefficients'])
            derivative = r.sub(self.dlog_section(coefficient, degree), a.scale(self.dlog_f0, degree))
            self.covariance(derivative)
            answer = derivative
            scalar = 0
            for parent in rec['input_nodes']:
                key = parent['point_sha256']
                assert scalars[key] == parent['scalar_coefficient_of_C']
                answer = r.sub(answer, values[key])
                scalar -= scalars[key]
            output = rec['output_node']
            assert scalar == output['scalar_coefficient_of_C']
            key = output['point_sha256']
            if key in values:
                assert r.equal(values[key], answer) and scalars[key] == scalar
            values[key], scalars[key] = answer, scalar
            function_derivatives.append({'label': rec['label'], 'log_norm_derivative_at_family2': r.to_json(derivative)})
        final = multiple['point_sha256']
        assert scalars[final] == multiple['sign']*H
        assert manifest['final_node']['point_sha256'] == final
        self.covariance(values[final])
        output = {'complete_all454_actual_chain_norm_derivatives': True,
                  'initial_log_norm_derivative_f_b_over_f0': r.to_json(self.dlog_initial),
                  'log_norm_derivative_f_final': r.to_json(values[final]),
                  'log_norm_derivative_of_sign_mC_minus_Dfinal_principal_function': r.to_json(r.neg(values[final])),
                  'function_log_norm_derivatives': function_derivatives,
                  'all455_principal_functions_unit_on_family2': True,
                  'transport_manifest_sha256': sha(manifest_path), 'transport_run_manifest_sha256': sha(run_path)}
        print('PASS455 exact principal norm derivatives and complete scalar DAG', disk_id, flush=True)
        return output, values[final]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--second-kind', type=Path, required=True)
    ap.add_argument('--Abel', type=Path, required=True)
    ap.add_argument('--multiplication', type=Path, required=True)
    ap.add_argument('--transport-directory', type=Path)
    ap.add_argument('--build-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    E = Engine(args.script_dir.resolve(), args.based_points, args.second_kind, args.build_dir)
    endpoint, actual, multiple = E.endpoint(args.Abel, args.multiplication)
    out = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
           'disk_id': multiple['disk_id'], 'complete_terminal_second_kind_integrals': True,
           'complete_actual54_second_kind_center_integrals': False,
           'complete_local_QC_heights': False, 'complete_common_roots': False,
           'endpoint': endpoint,
           'pole_family2_indices_1based': E.nu['pole_indices_1based'],
           'input_sha256': dict(E.inputs, **{args.Abel.name: sha(args.Abel), args.multiplication.name: sha(args.multiplication)}),
           'native': E.native, 'source_sha256': sha(__file__)}
    if args.transport_directory is not None:
        chain, derivative = E.chain(multiple['disk_id'], args.transport_directory, multiple)
        value = E.a.scale(E.r.sub(actual, derivative), multiple['sign']*pow(multiple['target_multiplier'], -1, Q))
        E.covariance(value)
        out.update(complete_actual54_second_kind_center_integrals=True,
                   actual54_second_kind_integrals_of_C_mod47four=E.r.to_json(value),
                   principal_chain=chain,
                   formula='sign*m*integral_C(nu)=tiny_A1(t)(nu)+dlog((v1/f0)*(F/G))|Z2-dlog(f_final)|Z2')
    save(args.output, out)
    print('Actual selected SS second-kind result', multiple['disk_id'], 'complete', out['complete_actual54_second_kind_center_integrals'],
          'SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
