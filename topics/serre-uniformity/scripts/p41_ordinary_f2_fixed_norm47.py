#!/usr/bin/env python3
"""Actual fixed and collision Norms of Phi_C in the F2 second divisor.

No Jacobian chain is repeated.  The retained principal sections are evaluated
on the full canonical algebra and in complete disks at every low-degree
point.  All Weierstrass factors and both j-coordinate leading units survive
until the exact divisor cancellation has been checked.
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
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(gzip.compress(raw, mtime=0))
    tmp.replace(path)


class Engine:
    def __init__(self, args):
        import numpy as np
        import p41_r2_matrix as r
        from p41_actual_differentials47 import ActualModel
        from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
        from p41_miller_unit_atlas47 import MillerUnitAtlas
        from p41_ordinary_B_fibre47 import Engine as BEngine
        import p41_ordinary_t2_principal_norm47
        install_exact_float_mm(r)
        self.a = a = ActualModel(args.script_dir)
        self.r, self.np, self.args = r, np, args
        self.based = read(args.based_points)
        assert self.based['complete19_actual_based_points']
        self.inputs = dict(a.inputs)
        self.inputs[args.based_points.name] = sha(args.based_points)
        self.bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
        self.family = self.bases['families'][0]
        self.v1 = r.from_json(self.family['v_coefficients'])
        self.fb = r.from_json(self.based['f_b_coefficients'])
        self.preparer = MillerUnitAtlas.__new__(MillerUnitAtlas)
        self.preparer.a, self.preparer.r, self.preparer.np = a, r, np
        self.helper = ProjectiveJetFrames(a)
        BEngine.load(self, args.second_kind_certificate, args.multiplication,
                     args.transport_directory, args.principal_expression)
        self.cm = a.read('p41_cm_quadratic_jets47_raw.json.gz')
        self.low = a.read('p41_canonical_low_points47_certificate.json.gz')
        self.canonical = read(args.canonical_algebra)
        assert self.low['canonical_algebra_sha256'] == sha(args.canonical_algebra)
        assert self.canonical['degree'] == 106
        assert r.equal(r.from_json(self.canonical['denominator_coefficients']), a.fc)
        self.g1canonical = r.from_json(self.canonical['canonical_coefficients'])
        self.g1 = r.mm(a.K1, self.g1canonical)
        self.lifts = read(args.ordinary_lifts)
        self.lift = next(x for x in self.lifts['points'] if x['j_mod47'] == int(self.disk_id[-2:]))
        self.coarse = a.read('p41_elliptic_coarse_atlas47_verified.json.gz')
        self.cm3 = a.read('p41_cm3_logjets47_checkpoint.json.gz')
        self.t2norm = read(args.t2_norm)
        assert self.t2norm['complete_actual_principal_norm_on_T2_P']
        assert self.t2norm['disk_id'] == self.disk_id
        assert self.t2norm['input_sha256'][args.principal_expression.name] == sha(args.principal_expression)
        self.inputs.update(a.inputs)
        self.inputs.update({p.name: sha(p) for p in [args.canonical_algebra, args.ordinary_lifts, args.t2_norm]})
        self.dependency_sources = {name+'.py': sha(sys.modules[name].__file__) for name in [
            'p41_ordinary_B_fibre47', 'p41_projective_jet_frames47',
            'p41_miller_unit_atlas47', 'p41_ordinary_t2_principal_norm47']}
        self.prepare_points()

    def prepare_points(self):
        r = self.r
        points = []
        for rec in self.cm['records']:
            label = rec['label']
            if label in ['P_minus3', 'P_minus12', 'P_minus7'] or label.startswith('Z_minus8_'):
                weight = {'P_minus3': 4, 'P_minus12': 81, 'P_minus7': -54}.get(label, -27)
                points.append({'label': label, 'weight': weight,
                               'C_order': -1 if label == 'P_minus3' else 0,
                               'W0': rec['normalized_weight2_coefficients'][0]})
        assert len(points) == 23
        for rec in self.low['records']:
            points.append({'label': rec['label'], 'weight': 4, 'C_order': 0,
                           'W0': rec['normalized_weight2_values'],
                           'canonical_primitive_root': rec['primitive_root_mod47four']})
        points.append({'label': self.disk_id, 'weight': 4, 'C_order': 1,
                       'W0': self.lift['W_mod47four']})
        assert len(points) == 28 and sum(p['weight'] for p in points) == -489
        self.points, self.W0 = points, r.from_json([p['W0'] for p in points])
        for rec in points:
            if rec['label'].startswith('canonical1_'):
                assert r.iszero(r.mm(r.from_json([rec['W0']]), self.g1))

    def tangent_data(self, chart, local_index, metadata):
        from p41_miller_unit_atlas47 import ONE, inv, log_unit, mul, scale, unit
        r = self.r
        get = lambda M: tuple(int(x[0, 0]) for x in M)
        if metadata['C_order'] == 1:
            A, B = self.lift['curve_A'], self.lift['curve_B']
            delta = (4*A**3+27*B**2) % Q
            beta_over_dj = delta*pow(124416*A*A*B, -1, Q) % Q
            raw = r.from_json([metadata['W0']])
            raw_frame = get(r.mm(raw, chart['frame']))
            Hc = tuple(int(x[local_index, 0]) for x in chart['Hc'][0])
            alpha = scale(mul(raw_frame, Hc), beta_over_dj)
            omega_g1_over_dj = scale(get(r.mm(raw, self.g1)), beta_over_dj)
            description = 'beta/dj=Delta/(124416*A^2*B), raw ordinary weight2 values'
        else:
            assert metadata['label'] == 'P_minus3' and metadata['C_order'] == -1
            coarse = next(x for x in self.coarse['elliptic_charts'] if x['kind'] == 'CM3')
            raw = [r.from_json(x) for x in coarse['coarse_values'][:2]]
            vv = [get(r.mm(w, chart['frame'])) for w in raw]
            cc = [get(r.mm(w, chart['coordinate'])) for w in raw]
            from p41_miller_unit_atlas47 import sub
            alpha_u = mul(sub(mul(cc[1], vv[0]), mul(cc[0], vv[1])), mul(inv(vv[0]), inv(vv[0])))
            assert r.equal(r.mul(raw[0], r.inverse_values(r.mm(raw[0], chart['frame']))),
                           r.rows(chart['W'][0], [local_index]))
            alpha = scale(alpha_u, pow(256, -1, Q))
            omega = r.from_json(self.cm3['canonical_differential_coefficients'][0])
            omega_g1_over_dj = scale(get(r.mm(omega, self.g1canonical)), pow(256, -1, Q))
            description = 'actual CM3 coarse u=A^3/B^2, j=6912*u/(4*u+27), dj/du=256'
        assert unit(alpha) and unit(omega_g1_over_dj)
        return {'dz_over_dj': alpha, 'log_dz_over_dj': log_unit(alpha),
                'g1_differential_over_dj': omega_g1_over_dj,
                'log_g1_differential_over_dj': log_unit(omega_g1_over_dj),
                'normalization': description}

    def process_chart(self, chart):
        from p41_miller_unit_atlas47 import ONE, ZERO, add, sub, scale, poly_mul, exact_quotient
        a, r, prep = self.a, self.r, self.preparer
        I = chart['indices_0based']
        count = len(I)
        cubics = [f for f in self.functions if f['line_bundle_power'] == 3]
        assert len(cubics) == 454
        co = r.hcat(*[self.coeffs[f['label']] for f in cubics])
        logs, polynomials, hist = prep.section_data([r.mm(v, co) for v in chart['V3']])
        functions = {}
        for k, f in enumerate(cubics):
            functions[f['label']] = (r.cols(logs[0], [k]), {i: polynomials.get((i, k), [ONE]) for i in range(count)})
        negative = next(f for f in self.functions if f['line_bundle_power'] == 2)
        ll, ww, _ = prep.section_data([r.mm(v, self.coeffs[negative['label']]) for v in chart['V2']])
        functions[negative['label']] = (ll[0], {i: ww.get((i, 0), [ONE]) for i in range(count)})
        fixed = {}
        for name, (basis, coefficient) in self.fixed.items():
            ll, ww, _ = prep.section_data([r.mm(v, coefficient) for v in chart[basis]])
            fixed[name] = (ll[0], {i: ww.get((i, 0), [ONE]) for i in range(count)})
        ideals = {'initial': r.from_json(self.point['point_coordinates']),
                  'negative': r.from_json(self.multiple['negative_input_coordinates']),
                  'final': r.from_json(self.multiple['point_coordinates']),
                  'family1': r.from_json(self.second['endpoint']['family1_effective_point_coordinates'])}
        ideal_values = {name: [r.mm(v, K) for v in chart['V2']] for name, K in ideals.items()}
        initial_sha = self.manifest['initial_node']['point_sha256']
        final_sha = self.manifest['final_node']['point_sha256']
        rows = []
        for i, global_index in enumerate(I):
            metadata = self.points[global_index]
            getL = lambda item: tuple(int(x[i, 0]) for x in item[0])
            getW = lambda name: fixed[name][1][i]
            ws, witnesses = {}, {}
            for name, values in ideal_values.items():
                ws[name], witnesses[name] = prep.prepare_ideal(values, i)
            assert getW('fc') == [ONE]
            c = metadata['C_order']
            expected_initial = getW('fb')
            if c == 1:
                expected_initial = poly_mul(expected_initial, [ZERO, ONE])
            elif c == -1:
                expected_initial = exact_quotient(expected_initial, [ZERO, ONE])
            assert ws['initial'] == expected_initial, ('actual initial divisor', metadata['label'])
            assert ws['family1'] == getW('v1'), ('actual family1 divisor disjoint from this disk', metadata['label'])
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
            value = sub(add(sub(getL(fixed['v1']), getL(fixed['fc'])),
                            sub(getL(fixed['FP']), getL(fixed['GQ']))), node_L[final_sha])
            endpoint = self.flat['combined_function_to_actual_A1_t']
            reverse = add(scale(getL(fixed['fb']), endpoint['f_b_integer_exponent']),
                          scale(getL(fixed['fc']), endpoint['f0_integer_exponent']))
            reverse = add(reverse, add(getL(fixed['v1']), sub(getL(fixed['FP']), getL(fixed['GQ']))))
            for factor in self.flat['section_factors']:
                reverse = add(reverse, scale(getL(functions[factor['label']]), factor['signed_integer_exponent']))
            assert reverse == value
            row = {'label': metadata['label'], 'indices_0based': global_index, 'second_divisor_weight': metadata['weight'],
                   'Phi_actual_order': self.scale*c, 'Phi_distinguished_factor': {'z_integer_exponent': self.scale*c},
                   'log_leading_unit_in_chart_z_mod47four': value,
                   'all455_actual_distinguished_relations_verified': True,
                   'four_full73_ideal_Weierstrass': ws, 'ideal_witness_columns_1based': witnesses,
                   'fixed_Weierstrass': {name: getW(name) for name in fixed},
                   'fixed_unit_logs': {name: getL(item) for name, item in fixed.items()},
                   'negative_unit_log': getL(functions[negative['label']]),
                   'negative_Weierstrass': functions[negative['label']][1][i],
                   'cubic_residual_degree_histogram': dict(sorted(hist[i].items()))}
            if c:
                row['j_tangent'] = self.tangent_data(chart, i, metadata)
                row['log_leading_unit_in_j_mod47four'] = add(value, scale(row['j_tangent']['log_dz_over_dj'], self.scale*c))
            else:
                row['log_value_mod47four'] = value
            rows.append(row)
        return {'indices_0based': I, 'rows': rows,
                'frame': r.to_json(chart['frame']), 'coordinate': r.to_json(chart['coordinate']),
                'cubic_labels_in_order': [f['label'] for f in cubics],
                'cubic_unit_log_constants': r.to_json(logs[0]),
                'cubic_nonunit_Weierstrass': [{'point_0based_in_chart': i, 'column_0based': j, 'W': w}
                                            for (i, j), w in sorted(polynomials.items())]}

    def finite_norm(self):
        from p41_miller_unit_atlas47 import ZERO, add, scale
        cache_dir = self.args.cache_dir
        cache_dir.mkdir(parents=True, exist_ok=True)
        charts, rows, cache_manifest = [], [], []
        for index, chart in enumerate(self.helper.iter_charts(self.W0, order=27, max_points=16, label=self.disk_id+'_F2_fixed')):
            path = cache_dir/('p41_'+self.disk_id+'_F2_fixed_chart'+str(index)+'_jets27.json.gz')
            cache = {name: [self.r.to_json(c) for c in chart[name]] for name in ['W', 'V2', 'V3', 'Hc']}
            cache.update({name: self.r.to_json(chart[name]) for name in ['frame', 'coordinate']})
            cache.update({'indices_0based': chart['indices_0based'], 'order': 27,
                          'source_inputs_sha256': self.inputs,
                          'helper_sha256': sha(sys.modules['p41_projective_jet_frames47'].__file__)})
            save(path, cache)
            result = self.process_chart(chart)
            result['jet_cache_sha256'], result['jet_cache_basename'] = sha(path), path.name
            charts.append(result)
            rows.extend(result['rows'])
            cache_manifest.append({'basename': path.name, 'sha256': sha(path), 'bytes': path.stat().st_size})
            partial = {'complete': len(rows) == 28, 'charts': charts, 'rows': rows,
                       'jet_cache_manifest': cache_manifest, 'input_sha256': self.inputs,
                       'source_sha256': sha(__file__)}
            save(self.args.output.with_name(self.args.output.name.replace('.json.gz', '_finite_checkpoint.json.gz')), partial)
            print('PASS fixed/collision chart', index, 'total points', len(rows), flush=True)
        assert sorted(row['indices_0based'] for row in rows) == list(range(28))
        unit_total, tangent_total = ZERO, ZERO
        for row in rows:
            unit_total = add(unit_total, scale(row['log_leading_unit_in_chart_z_mod47four'], row['second_divisor_weight']))
            if row['Phi_actual_order']:
                tangent_total = add(tangent_total, scale(row['j_tangent']['log_dz_over_dj'],
                                                        row['Phi_actual_order']*row['second_divisor_weight']))
        total = add(unit_total, tangent_total)
        assert total[1] == 0
        assert sum(row['second_divisor_weight']*row['Phi_actual_order'] for row in rows) == 0
        return {'complete28_fixed_and_collision_points': True, 'charts': charts,
                'rows': rows, 'jet_cache_manifest': cache_manifest,
                'weighted_chart_unit_log': unit_total, 'weighted_j_tangent_correction': tangent_total,
                'weighted_actual_log_in_j': total, 'weighted_degree': -489,
                'tame_symbol_sign_is_one': True, 'all_four_full73_ideals_checked_at_all28_points': True}

    def high_norm(self):
        from flint import fmpz_poly, nmod_poly
        r, np = self.r, self.np
        H = [int(x) for x in self.low['high_factor_ascending']]
        L = [int(x) for x in self.low['low_factor_ascending']]
        Hq, Lq = nmod_poly(H, Q), nmod_poly(L, Q)
        assert Hq*Lq == nmod_poly(self.canonical['minimal_polynomial_ascending'], Q)
        Hp = nmod_poly(H, P)
        _, factors = Hp.factor()
        assert sorted((f.degree(), e) for f, e in factors) == [(6, 1), (8, 1), (22, 1), (31, 1), (35, 1)]
        Hinteger = fmpz_poly(H)
        Phi = {d: r.from_json(self.canonical['Phi'+str(d)]) for d in [1, 2, 3]}
        assert r.iszero(r.mm(Phi[1], self.g1))
        assert r.to_json(r.mm(Phi[1], self.a.fc)) == [[[1, 0]]]+[[[0, 0]]]*105
        values, norms, records = {}, {}, []

        def evaluate_matrix(labels, basis, coefficients):
            evaluated = r.mm(basis, coefficients)
            assert not np.any(evaluated[1]), 'actual rational section has descended polynomial coefficients'
            for k, label in enumerate(labels):
                raw = [int(x) for x in evaluated[0][:, k]]
                poly = nmod_poly(raw, Q) % Hq
                coefficients = [int(x) for x in poly.coeffs()]
                residue = nmod_poly(coefficients, P)
                assert Hp.gcd(residue).degree() == 0, ('nonunit high canonical section', label)
                norm = int(Hinteger.resultant(fmpz_poly(coefficients))) % Q
                assert norm % P
                values[label], norms[label] = poly, norm
                records.append({'label': label, 'polynomial_coefficients_mod_high_factor': [int(x) for x in poly.coeffs()],
                                'norm_mod47four': norm})

        for degree in [2, 3]:
            group = [f for f in self.functions if f['line_bundle_power'] == degree]
            evaluate_matrix([f['label'] for f in group], Phi[degree], r.hcat(*[self.coeffs[f['label']] for f in group]))
        for name, (basis, coefficient) in self.fixed.items():
            degree = {'W': 1, 'V2': 2}[basis]
            evaluate_matrix([name], Phi[degree], coefficient)
        initial, final = self.manifest['initial_node']['point_sha256'], self.manifest['final_node']['point_sha256']
        nodes = {initial: norms['fb']*pow(norms['fc'], -1, Q) % Q}
        for f in self.functions:
            value = norms[f['label']]*pow(norms['fc'], -f['line_bundle_power'], Q) % Q
            for parent in f['input_nodes']:
                value = value*pow(nodes[parent['point_sha256']], -1, Q) % Q
            nodes[f['output_node']['point_sha256']] = value
        norm = pow(nodes[final], -1, Q)*norms['v1']*pow(norms['fc'], -1, Q)*norms['FP']*pow(norms['GQ'], -1, Q) % Q
        endpoint = self.flat['combined_function_to_actual_A1_t']
        independent = pow(norms['fb'], endpoint['f_b_integer_exponent'], Q)*pow(norms['fc'], endpoint['f0_integer_exponent'], Q) % Q
        independent = independent*norms['v1']*norms['FP']*pow(norms['GQ'], -1, Q) % Q
        for factor in self.flat['section_factors']:
            independent = independent*pow(norms[factor['label']], factor['signed_integer_exponent'], Q) % Q
        assert independent == norm
        from p41_ordinary_t2_principal_norm47 import logunit
        output = {'complete_actual_high102_canonical_norm': True, 'degree': 102,
                  'actual_function': 'Phi_C', 'norm_mod47four': norm, 'log_norm_mod47four': logunit(norm),
                  'high_factor_ascending': H, 'low_factor_ascending': L,
                  'irreducible_factor_degrees_mod47': [6, 8, 22, 31, 35],
                  'all455_and_fixed_sections_unit_on_high102': True,
                  'all_rational_sections_descend_to_real_polynomial_subalgebra': True,
                  'forward_DAG_and_integer_flat_norms_equal': True,
                  'all460_evaluated_section_polynomials_and_norms': records,
                  'input_sha256': self.inputs, 'source_sha256': sha(__file__)}
        save(self.args.output.with_name(self.args.output.name.replace('.json.gz', '_high102_checkpoint.json.gz')), output)
        print('PASS full high102 canonical norm', norm, 'log', logunit(norm), flush=True)
        return output

    def result(self, finite, high):
        from p41_miller_unit_atlas47 import ZERO, add, scale
        total = add(finite['weighted_actual_log_in_j'], (4*high['log_norm_mod47four'] % Q, 0))
        t2part = 27*self.t2norm['actual_log_norm_Phi_T2_P_mod47four'] % Q
        total = add(total, (t2part, 0))
        assert total[1] == 0 and -489+4*102+27*3 == 0
        low = ZERO
        for row in finite['rows']:
            if row['label'].startswith('canonical1_'):
                low = add(low, row['log_value_mod47four'])
        canonical = add(low, (high['log_norm_mod47four'], 0))
        assert canonical[1] == 0
        output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
                  'disk_id': self.disk_id, 'actual_integer_scale': self.scale,
                  'complete_actual_first_variable_norm_on_F2_second_divisor': True,
                  'complete_actual_local_sigma_F2_height': False,
                  'complete_all53_local_QC_heights': False, 'complete_common_roots': False,
                  'first_function': 'div(Phi_C)=m*(P_center-P_minus3)-A1(t)',
                  'actual_second_divisor': '27*T2(P)+81*P_minus12-27*Z_minus8-54*P_minus7+4*P+4*P_minus3+4*K_g1',
                  'second_divisor_degree': 0, 'collision_parameter': 'j-j(Q) at P and b=P_minus3',
                  'actual_log_norm_Phi_on_F2_second_divisor_mod47four': total[0],
                  'full_canonical_degree106_log_norm': canonical[0],
                  'weighted_T2_log_norm': t2part,
                  'fixed_and_collision_part': finite, 'high102_canonical_part': high,
                  'g1_actual73_coefficients': self.r.to_json(self.g1),
                  'input_sha256': self.inputs, 'dependency_sources_sha256': self.dependency_sources,
                  'source_sha256': sha(__file__)}
        return output


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'based-points', 'second-kind-certificate', 'multiplication',
                 'transport-directory', 'principal-expression', 'canonical-algebra',
                 'ordinary-lifts', 't2-norm', 'cache-dir', 'output']:
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--only-high102', action='store_true')
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    started = time.monotonic()
    E = Engine(args)
    high = E.high_norm()
    if args.only_high102:
        return
    finite = E.finite_norm()
    result = E.result(finite, high)
    save(args.output, result)
    print('PASS ACTUAL FULL FIRST VARIABLE F2 NORM', E.disk_id,
          result['actual_log_norm_Phi_on_F2_second_divisor_mod47four'],
          'SHA', sha(args.output), 'seconds', round(time.monotonic()-started, 3), flush=True)


if __name__ == '__main__':
    main()
