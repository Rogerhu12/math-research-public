#!/usr/bin/env python3
"""Actual ordinary Poincare fibre values against B=Z_minus4-D_cusp.

All retained principal functions are evaluated.  The CM4 calculation
prepares nonunits in complete residue disks and checks the exact divisor
DAG; the cusp calculation uses the complete degree80 field and degree20
Frobenius orbit.  The endpoint is the actual R248 first Abel family.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

P, Q = 47, 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


class Engine:
    def __init__(self, script_dir, based_path, cache_dir):
        import numpy as np
        import p41_r2_matrix as r
        from p41_actual_differentials47 import ActualModel
        from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
        from p41_miller_unit_atlas47 import MillerUnitAtlas
        from p41_hecke3_hessian47 import section_jets
        from p41_elliptic_coarse_atlas47 import Series
        from p41_scalar_primitive_atlas47 import scalar_gm
        install_exact_float_mm(r)
        self.a = a = ActualModel(script_dir)
        self.r, self.np = r, np
        self.based = read(based_path)
        assert self.based['complete19_actual_based_points']
        self.inputs = dict(a.inputs)
        self.inputs[based_path.name] = sha(based_path)
        self.bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
        self.family = self.bases['families'][0]
        self.v1 = r.from_json(self.family['v_coefficients'])
        self.fb = r.from_json(self.based['f_b_coefficients'])
        self.preparer = MillerUnitAtlas.__new__(MillerUnitAtlas)
        self.preparer.a, self.preparer.r, self.preparer.np = a, r, np
        helper = ProjectiveJetFrames(a)
        self.helper = helper
        cache_dir.mkdir(parents=True, exist_ok=True)
        cache_path = cache_dir/'p41_true_CM4_twenty_projective_jets27.json.gz'
        W0 = r.from_json(a.cm4['coarse_point_values'])
        assert W0[0].shape == (20, 73)
        if cache_path.exists():
            cache = read(cache_path)
            assert cache['source_inputs_sha256'] == a.inputs
            assert cache['helper_sha256'] == sha(sys.modules['p41_projective_jet_frames47'].__file__)
            self.cm_chart = {name: [r.from_json(c) for c in cache[name]] for name in ['W', 'V2', 'V3']}
            self.cm_chart['frame'] = r.from_json(cache['frame'])
            self.cm_chart['coordinate'] = r.from_json(cache['coordinate'])
            assert r.equal(self.cm_chart['W'][0], r.mul(W0, r.inverse_values(r.mm(W0, a.fc))))
        else:
            charts = list(helper.iter_charts(W0, order=27, max_points=20, label='true_Z_minus4'))
            assert len(charts) == 1 and charts[0]['indices_0based'] == list(range(20))
            self.cm_chart = charts[0]
            cache = {name: [r.to_json(c) for c in charts[0][name]] for name in ['W', 'V2', 'V3']}
            cache.update({'frame': r.to_json(charts[0]['frame']), 'coordinate': r.to_json(charts[0]['coordinate']),
                          'helper_sha256': sha(sys.modules['p41_projective_jet_frames47'].__file__),
                          'source_inputs_sha256': dict(a.inputs), 'actual_point_count': 20, 'order': 27})
            save(cache_path, cache)
        assert r.equal(self.cm_chart['frame'], a.fc)
        self.inputs[cache_path.name] = sha(cache_path)
        # Actual eta_B in the physical first Abel family, to sufficient order.
        eta = a.read('p41_eta_calibration47_complete.json.gz')
        jets = a.read('p41_source_cubic47_full_saved.json.gz')
        assert self.bases['jets_sha256'] == a.inputs['p41_source_cubic47_full_saved.json.gz']
        assert eta['coefficient_precision'] == 3
        W = [r.from_json(v) for v in jets['evaluation_coefficients'][:3]]
        assert r.equal(W[0], a.M['W'])
        V2, V3 = section_jets(W, [a.model, a.cusp, a.cm4, a.group], a.M, r)
        I1 = [i-1 for i in self.family['points_1based']]
        numerator, denominator = r.from_json(eta['numerator_coefficients']), r.from_json(eta['denominator_coefficients'])
        nums = [r.mm(r.rows(v, I1), numerator) for v in V3]
        dens = [r.mm(r.rows(v, I1), denominator) for v in V2]
        assert np.all(r.units(dens[0]))
        quotient = Series(a, 3).mul(nums, Series(a, 3).inverse(dens))
        _, beta = scalar_gm((1, 0), (32, 0), False, 3)
        self.eta_series = []
        for n in range(3):
            value = r.zeros(54, 1)
            for k in range(n+1):
                assert beta[n-k][1] == 0
                value = r.add(value, a.scale(quotient[k], beta[n-k][0]))
            self.eta_series.append(value)
        self.setup_cusp()
        self.inputs.update(a.inputs)

    def setup_cusp(self):
        a, r, np = self.a, self.r, self.np
        a.field_setup()
        self.one = np.zeros(80, dtype=np.int64)
        self.one[0] = 1
        self.cusp_W = np.asarray(a.cusp['cusp_values'][0], dtype=np.int64)
        self.cusp_V2 = a.field_rows([a.field_mul(self.cusp_W[i], self.cusp_W[j]) for i, j in zip(a.a2, a.b2)], a.C2)
        extra = a.field_rows([a.field_mul(self.cusp_W[i], self.cusp_V2[j]) for i, j in zip(a.a3, a.b3)], a.E3)
        self.cusp_V3 = [(-x) % Q for x in a.field_rows(extra, a.C)]+extra
        assert not np.any(a.field_rows(self.cusp_W, a.fc)[0])
        orbit, j = [], 0
        while j not in orbit:
            orbit.append(j)
            j = a.cusp['cusp_frobenius_permutation_1based'][j]-1
        assert j == 0 and len(orbit) == 20
        self.cusp_orbit = orbit
        torsion = a.read('p41_local47_torsion_certificate.json')
        frob = np.asarray(torsion['frobenius_lift'], dtype=np.int64)
        phi = np.zeros(80, dtype=np.int64)
        phi[1] = 1
        for _ in range(20):
            phi = self.field_subst(phi, frob)
        self.phi20 = phi
        poly = a.field_polynomial
        trace = [80]
        for k in range(1, 80):
            value = k*int(poly[80-k])
            for j in range(1, k):
                value += int(poly[80-j])*trace[k-j]
            trace.append(-value % Q)
        self.trace = trace

    def field_power(self, value, exponent):
        out = self.one.copy()
        while exponent:
            if exponent & 1:
                out = self.a.field_mul(out, value)
            exponent >>= 1
            if exponent:
                value = self.a.field_mul(value, value)
        return out

    def field_subst(self, value, argument):
        out = self.np.zeros(80, dtype=self.np.int64)
        for c in reversed(value):
            out = self.a.field_mul(out, argument)
            out[0] = (out[0]+int(c)) % Q
        return out

    def batch_inverse(self, values):
        prefix, current = [], self.one.copy()
        for value in values:
            assert self.np.any(value % P)
            prefix.append(current)
            current = self.a.field_mul(current, value)
        inverse = self.field_power(current, (P**80-1)*P**3-1)
        assert self.np.array_equal(self.a.field_mul(current, inverse), self.one)
        out = [None]*len(values)
        for j in range(len(values)-1, -1, -1):
            out[j] = self.a.field_mul(inverse, prefix[j])
            inverse = self.a.field_mul(inverse, values[j])
        assert self.np.array_equal(inverse, self.one)
        return out

    def load(self, second_path, multiple_path, directory, flat_path):
        r = self.r
        self.second, self.multiple, self.flat = read(second_path), read(multiple_path), read(flat_path)
        manifest_path = directory/'transport_manifest47.json'
        self.manifest = read(manifest_path)
        assert self.second['complete_actual54_second_kind_center_integrals']
        assert self.flat['complete_exact_integer_principal_function_expression']
        assert self.flat['input_sha256'][second_path.name] == sha(second_path)
        assert self.flat['input_sha256'][manifest_path.name] == sha(manifest_path)
        assert self.second['input_sha256'][multiple_path.name] == sha(multiple_path)
        disk_id = self.second['disk_id']
        assert disk_id == self.multiple['disk_id'] == self.manifest['disk_id'] == self.flat['disk_id']
        self.disk_id = disk_id
        self.scale = self.manifest['final_node']['scalar_coefficient_of_C']
        assert self.flat['combined_function_to_actual_A1_t']['formal_divisor'] == {'C=P_center-P_minus3': self.scale, 'A1(t)': -1}
        self.functions = []
        for entry in self.manifest['functions']:
            if entry['phase'] == 'formal_extraction':
                continue
            path = directory/entry['filename']
            assert sha(path) == entry['sha256']
            self.functions.append(read(path))
        self.functions.sort(key=lambda f: (-1, 0) if f['phase'] == 'initial_negative'
                            else (f['bit'], 0 if f['operation'] == 'double_addflip' else 1))
        assert len(self.functions) == 455
        self.coeffs = {f['label']: r.from_json(f['numerator_coefficients']) for f in self.functions}
        self.fixed = {'fb': ('W', self.fb), 'fc': ('W', self.a.fc), 'v1': ('W', self.v1),
                      'FP': ('V2', r.from_json(self.second['endpoint']['terminal_transport_numerator_V2'])),
                      'GQ': ('V2', r.from_json(self.second['endpoint']['terminal_transport_denominator_V2']))}
        self.point = next(x for x in self.based['records'] if x['disk_id'] == disk_id)
        assert self.point['point_sha256'] == self.manifest['initial_node']['point_sha256']
        assert r.equal(r.from_json(self.flat['f_b_coefficients']), self.fb)
        assert r.equal(r.from_json(self.flat['f0_coefficients']), self.a.fc)
        endpoint = self.flat['combined_function_to_actual_A1_t']
        assert r.equal(r.from_json(endpoint['v1_weight2_coefficients']), self.v1)
        assert r.equal(r.from_json(endpoint['F_terminal_V2_coefficients']), self.fixed['FP'][1])
        assert r.equal(r.from_json(endpoint['G_terminal_V2_coefficients']), self.fixed['GQ'][1])
        assert endpoint['actual_A1_physical_parameters'] == self.second['endpoint']['family1_physical_parameters_mod47four']
        assert self.family['points_1based'] == self.second['endpoint']['family1_points_1based']
        for name, digest in self.inputs.items():
            if name in self.second['input_sha256']:
                assert digest == self.second['input_sha256'][name]
        self.inputs.update({p.name: sha(p) for p in [second_path, multiple_path, flat_path, manifest_path]})

    def cm_norm(self):
        from p41_miller_unit_atlas47 import ONE, ZERO, add, sub, scale, poly_mul, exact_quotient
        a, r, np = self.a, self.r, self.np
        chart, prep = self.cm_chart, self.preparer
        cubics = [f for f in self.functions if f['line_bundle_power'] == 3]
        assert len(cubics) == 454
        matrix = r.hcat(*[self.coeffs[f['label']] for f in cubics])
        logs, polynomials, hist = prep.section_data([r.mm(v, matrix) for v in chart['V3']])
        functions = {}
        for k, f in enumerate(cubics):
            functions[f['label']] = (r.cols(logs[0], [k]), {i: polynomials.get((i, k), [ONE]) for i in range(20)})
        negative = next(f for f in self.functions if f['line_bundle_power'] == 2)
        ll, ww, hh = prep.section_data([r.mm(v, self.coeffs[negative['label']]) for v in chart['V2']])
        functions[negative['label']] = (ll[0], {i: ww.get((i, 0), [ONE]) for i in range(20)})
        fixed = {}
        for name, (basis, coefficient) in self.fixed.items():
            ll, ww, _ = prep.section_data([r.mm(v, coefficient) for v in chart[basis]])
            fixed[name] = (ll[0], {i: ww.get((i, 0), [ONE]) for i in range(20)})
        ideals = {'initial': r.from_json(self.point['point_coordinates']),
                  'negative': r.from_json(self.multiple['negative_input_coordinates']),
                  'final': r.from_json(self.multiple['point_coordinates']),
                  'family1': r.from_json(self.second['endpoint']['family1_effective_point_coordinates'])}
        ideal_values = {name: [r.mm(v, K) for v in chart['V2']] for name, K in ideals.items()}
        initial_sha, final_sha = self.manifest['initial_node']['point_sha256'], self.manifest['final_node']['point_sha256']
        # Full coefficient rows are kept, so the same data can later be used
        # at nearby Hecke targets without repeating any group operation.
        rows = []
        for i in range(20):
            getL = lambda item: tuple(int(x[i, 0]) for x in item[0])
            getW = lambda name: fixed[name][1][i]
            ws, witnesses = {}, {}
            for name, values in ideal_values.items():
                ws[name], witnesses[name] = prep.prepare_ideal(values, i)
            assert getW('fc') == [ONE]
            assert ws['initial'] == getW('fb'), ('initial actual support at CM4', i)
            assert ws['family1'] == getW('v1'), ('family1 physical support at CM4', i)
            node_W = {initial_sha: ws['initial']}
            node_L = {initial_sha: sub(getL(fixed['fb']), getL(fixed['fc']))}
            for f in self.functions:
                W, value = functions[f['label']][1][i], getL(functions[f['label']])
                divisor = [ONE]
                value = sub(value, scale(getL(fixed['fc']), f['line_bundle_power']))
                for parent in f['input_nodes']:
                    key = parent['point_sha256']
                    divisor = poly_mul(divisor, node_W[key])
                    value = sub(value, node_L[key])
                key = f['output_node']['point_sha256']
                node_W[key] = exact_quotient(W, divisor)
                node_L[key] = value
                if f['phase'] == 'initial_negative':
                    assert node_W[key] == ws['negative']
            assert node_W[final_sha] == ws['final']
            assert poly_mul(getW('v1'), getW('FP')) == poly_mul(ws['final'], getW('GQ'))
            # All distinguished factors of Phi cancel as actual polynomials.
            value = sub(add(sub(getL(fixed['v1']), getL(fixed['fc'])),
                            sub(getL(fixed['FP']), getL(fixed['GQ']))), node_L[final_sha])
            # Independent reverse-DAG integer weights, including all frames.
            flat = self.flat['combined_function_to_actual_A1_t']
            reverse = add(scale(getL(fixed['fb']), flat['f_b_integer_exponent']),
                          scale(getL(fixed['fc']), flat['f0_integer_exponent']))
            reverse = add(reverse, add(getL(fixed['v1']), sub(getL(fixed['FP']), getL(fixed['GQ']))))
            for factor in self.flat['section_factors']:
                reverse = add(reverse, scale(getL(functions[factor['label']]), factor['signed_integer_exponent']))
            assert reverse == value
            rows.append({'CM4_point_1based': i+1, 'log_Phi_mod47four': value,
                         'all455_actual_distinguished_relations_verified': True,
                         'complete_final_distinguished_factor_is_one': True,
                         'ideal_Weierstrass': ws, 'ideal_witness_columns_1based': witnesses,
                         'fixed_Weierstrass': {name: getW(name) for name in fixed},
                         'cubic_residual_degree_histogram': dict(sorted(hist[i].items()))})
        total = ZERO
        for row in rows:
            total = add(total, row['log_Phi_mod47four'])
        assert total[1] == 0
        print('PASS actual20 CM4 norm and all455 distinguished relations', self.disk_id, total[0], flush=True)
        return {'point_count': 20, 'rows': rows, 'log_norm20': total[0],
                'all_four_full73_column_ideals_checked': True,
                'all_final_orders_zero_no_tangent_adjustment': True,
                'cubic_unit_log_constants': r.to_json(logs[0]),
                'cubic_nonunit_Weierstrass': [{'point_0based': i, 'column_0based': j, 'W': w}
                                            for (i, j), w in sorted(polynomials.items())]}

    def cusp_norm(self):
        a, np, r = self.a, self.np, self.r
        values = {}
        for degree, basis in [(2, self.cusp_V2), (3, self.cusp_V3)]:
            group = [f for f in self.functions if f['line_bundle_power'] == degree]
            block = a.field_rows(basis, r.hcat(*[self.coeffs[f['label']] for f in group]))
            values.update({f['label']: value for f, value in zip(group, block)})
        for name, (basis, coefficient) in self.fixed.items():
            if name == 'fc':
                values[name] = np.asarray(a.cusp['canonical_cusp_leading_values'][0], dtype=np.int64)
            else:
                fields = self.cusp_W if basis == 'W' else self.cusp_V2
                values[name] = a.field_rows(fields, coefficient)[0]
        assert all(np.any(value % P) for value in values.values())
        names = list(values)
        inverses = dict(zip(names, self.batch_inverse([values[name] for name in names])))
        mul = a.field_mul
        fc, ifc = values['fc'], inverses['fc']
        fcp = {d: self.field_power(fc, d) for d in [2, 3]}
        ifcp = {d: self.field_power(ifc, d) for d in [2, 3]}
        initial = self.manifest['initial_node']['point_sha256']
        node = {initial: (mul(values['fb'], ifc), mul(inverses['fb'], fc))}
        for f in self.functions:
            d, label = f['line_bundle_power'], f['label']
            value, inverse = mul(values[label], ifcp[d]), mul(inverses[label], fcp[d])
            for parent in f['input_nodes']:
                pv, pi = node[parent['point_sha256']]
                value, inverse = mul(value, pi), mul(inverse, pv)
            assert np.array_equal(mul(value, inverse), self.one)
            node[f['output_node']['point_sha256']] = value, inverse
        final = self.manifest['final_node']['point_sha256']
        Phi = mul(node[final][1], mul(mul(values['v1'], ifc), mul(values['FP'], inverses['GQ'])))
        # The full integer expression has no remaining f0 factor.  Other
        # factors are all units at the complete cusp orbit, so no hidden
        # zero or q41 tangent survives in the actual function.
        assert self.flat['combined_function_to_actual_A1_t']['f0_integer_exponent'] == 0
        assert np.array_equal(self.field_subst(Phi, self.phi20), Phi)
        E = P**80-1
        z = (self.field_power(Phi, E)-self.one) % Q
        assert not np.any(z % P)
        z2, z3 = mul(z, z), mul(mul(z, z), z)
        log = (z-z2*pow(2, -1, Q)+z3*pow(3, -1, Q)) % Q
        log = log*pow(E % Q, -1, Q) % Q
        assert np.array_equal(self.field_subst(log, self.phi20), log)
        answer = sum(int(x)*t for x, t in zip(log, self.trace))*pow(4, -1, Q) % Q
        print('PASS complete20 cusp norm, full field Frobenius20 and all unit inverses', self.disk_id, answer, flush=True)
        return {'cusp_frobenius_orbit_1based': [i+1 for i in self.cusp_orbit],
                'unit_Phi_in_degree80_field': Phi.astype(int).tolist(),
                'log_Phi_in_degree80_field': log.astype(int).tolist(),
                'trace_basis': self.trace, 'log_norm20': answer,
                'Phi_and_log_Frobenius20_fixed': True,
                'all455_sections_and_fixed_numerators_are_units': True,
                'all_final_orders_zero_no_tangent_adjustment': True,
                'normalization': 'Tr_R80(log Phi)/4, the complete degree20 cusp orbit'}

    def result(self, cm, cusp):
        r, a, np = self.r, self.a, self.np
        t = r.from_json(self.second['endpoint']['family1_physical_parameters_mod47four'])
        assert t[0].shape == (1, 54) and not np.any(t[0] % P) and not np.any(t[1] % P)
        tiny, power = r.zeros(1, 1), t
        for n in range(3):
            tiny = r.add(tiny, a.scale(r.mm(power, self.eta_series[n]), pow(n+1, -1, Q)))
            power = r.mul(power, t)
        assert not tiny[1][0, 0]
        tiny = int(tiny[0][0, 0])
        norm = (cm['log_norm20']-cusp['log_norm20']) % Q
        height = (tiny+norm)*pow(self.scale % Q, -1, Q) % Q
        return {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
                'disk_id': self.disk_id,
                'complete_actual_ordinary_B_Poincare_fibre': True,
                'complete_all53_local_QC_heights': False, 'complete_common_roots': False,
                'first_divisor': 'C=P_center-P_minus3', 'second_divisor': 'B=Z_minus4-D_cusp',
                'fibre_element': 'canonical norm element e(C,B)=1, supports disjoint',
                'actual_integer_scale': self.scale,
                'principal_function_divisor': 'scale*C-A1(t)',
                'CM4_norm': cm, 'cusp_norm': cusp,
                'log_Phi_B_mod47four': norm,
                'actual_eta_B_tiny_over_A1_t_mod47four': tiny,
                'actual_Poincare_Lambda_e_C_B_mod47four': height,
                'formula': '(integral_A1(t) eta_B + log Norm_B Phi_C)/scale',
                'eta_B_physical_coefficients_0to2': [r.to_json(v) for v in self.eta_series],
                'actual_family1_physical_parameters': r.to_json(t),
                'input_sha256': self.inputs, 'source_sha256': sha(__file__)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--based-points', type=Path, required=True)
    ap.add_argument('--second-kind-certificate', type=Path, required=True)
    ap.add_argument('--multiplication', type=Path, required=True)
    ap.add_argument('--transport-directory', type=Path, required=True)
    ap.add_argument('--principal-expression', type=Path, required=True)
    ap.add_argument('--cache-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    started = time.monotonic()
    E = Engine(args.script_dir.resolve(), args.based_points, args.cache_dir)
    E.load(args.second_kind_certificate, args.multiplication, args.transport_directory, args.principal_expression)
    cm = E.cm_norm()
    save(args.output.with_name(args.output.name.replace('.json.gz', '_CM4_checkpoint.json.gz')),
         {'disk_id': E.disk_id, 'CM4_norm': cm, 'input_sha256': E.inputs, 'source_sha256': sha(__file__)})
    cusp = E.cusp_norm()
    result = E.result(cm, cusp)
    save(args.output, result)
    print('ACTUAL ORDINARY POINCARE FIBRE', E.disk_id, result['actual_Poincare_Lambda_e_C_B_mod47four'],
          'SHA', sha(args.output), 'seconds', round(time.monotonic()-started, 3), flush=True)


if __name__ == '__main__':
    main()
