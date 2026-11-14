#!/usr/bin/env python3
"""Actual Phi_C Norm over all T2 targets, preparing split-target nonunits.

Irreducible cubic targets use R254.  Split targets use full ideal and actual
Weierstrass identities in unit projective charts.  f0 may be nonunit: its
distinguished factors cancel by the exact total zero f0 exponent of R252.
"""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import runpy
import sys
import time

P, Q = 47, 47**4


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(gzip.compress(raw, mtime=0))
    tmp.replace(path)


class SplitNorm:
    def __init__(self, args):
        import p41_r2_matrix as r
        from p41_actual_differentials47 import ActualModel
        from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
        from p41_miller_unit_atlas47 import MillerUnitAtlas
        from p41_ordinary_B_fibre47 import Engine as BEngine
        install_exact_float_mm(r)
        self.a = a = ActualModel(args.script_dir)
        self.r, self.np, self.args = r, a.np, args
        self.inputs = dict(a.inputs)
        self.based = read(args.based_points)
        self.inputs[args.based_points.name] = sha(args.based_points)
        self.bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
        self.family = self.bases['families'][0]
        self.v1, self.fb = r.from_json(self.family['v_coefficients']), r.from_json(self.based['f_b_coefficients'])
        BEngine.load(self, args.second_kind_certificate, args.multiplication,
                     args.transport_directory, args.principal_expression)
        self.preparer = MillerUnitAtlas.__new__(MillerUnitAtlas)
        self.preparer.a, self.preparer.r, self.preparer.np = a, r, a.np
        self.helper = ProjectiveJetFrames(a)
        self.support = read(args.support)
        assert self.support['complete_actual_T2_support'] and self.support['source_disk_id'] == self.disk_id
        assert self.flat['combined_function_to_actual_A1_t']['f0_integer_exponent'] == 0
        self.W0 = r.from_json([x['W_actual_values_in_R2'] for x in self.support['branch_records']])
        assert self.W0[0].shape == (3, 73)
        self.inputs.update(a.inputs)
        self.inputs[args.support.name] = sha(args.support)
        self.dependency_sources = {name+'.py': sha(sys.modules[name].__file__) for name in [
            'p41_ordinary_B_fibre47', 'p41_projective_jet_frames47', 'p41_miller_unit_atlas47']}

    def process(self, chart):
        from p41_miller_unit_atlas47 import ONE, ZERO, mul, inv, power, add, sub, scale, log_unit, poly_mul, exact_quotient, prepare_series
        r, prep, np = self.r, self.preparer, self.np
        count = len(chart['indices_0based'])
        groups = {}
        functions = {}
        histories = [Counter() for _ in range(count)]

        def sections(labels, basis, coefficients):
            values = [r.mm(v, coefficients) for v in chart[basis]]
            logs, polynomials, hist = prep.section_data(values)
            units = (values[0][0].copy(), values[0][1].copy())
            for (i, k), W in polynomials.items():
                ww, U, degree = prepare_series(prep.germ(values, i, k))
                assert ww == W
                units[0][i, k], units[1][i, k] = U[0]
            assert np.all(r.units(units))
            for k, label in enumerate(labels):
                functions[label] = {'U': r.cols(units, [k]), 'logU': r.cols(logs[0], [k]),
                                    'W': {i: polynomials.get((i, k), [ONE]) for i in range(count)}}
            group_key = basis+'_'+str(len(labels)) if len(labels) > 1 else labels[0]
            groups[group_key] = {
                'labels': labels, 'unit_values': r.to_json(units), 'unit_logs': r.to_json(logs[0]),
                'nonunit_Weierstrass': [{'point_0based': i, 'column_0based': k, 'W': w}
                                      for (i, k), w in sorted(polynomials.items())]}
            for i, h in enumerate(hist):
                histories[i].update(h)

        for degree, basis in [(2, 'V2'), (3, 'V3')]:
            ff = [f for f in self.functions if f['line_bundle_power'] == degree]
            sections([f['label'] for f in ff], basis, r.hcat(*[self.coeffs[f['label']] for f in ff]))
        for name, (basis, coefficient) in self.fixed.items():
            sections([name], basis, coefficient)
        ideals = {'initial': r.from_json(self.point['point_coordinates']),
                  'negative': r.from_json(self.multiple['negative_input_coordinates']),
                  'final': r.from_json(self.multiple['point_coordinates']),
                  'family1': r.from_json(self.second['endpoint']['family1_effective_point_coordinates'])}
        ideal_values = {name: [r.mm(v, K) for v in chart['V2']] for name, K in ideals.items()}
        initial = self.manifest['initial_node']['point_sha256']
        final = self.manifest['final_node']['point_sha256']
        rows = []
        for i, global_index in enumerate(chart['indices_0based']):
            get = lambda name, key: tuple(int(x[i, 0]) for x in functions[name][key])
            W = lambda name: functions[name]['W'][i]
            ws, witnesses = {}, {}
            for name, values in ideal_values.items():
                ws[name], witnesses[name] = prep.prepare_ideal(values, i)
            # These full-ideal equalities establish actual separation from C
            # and A1(t) in each target disk, not just disjoint displayed points.
            assert ws['initial'] == W('fb')
            assert ws['family1'] == W('v1')
            nodeW = {initial: ws['initial']}
            nodeU = {initial: mul(get('fb', 'U'), inv(get('fc', 'U')))}
            nodeL = {initial: sub(get('fb', 'logU'), get('fc', 'logU'))}
            for f in self.functions:
                label, degree = f['label'], f['line_bundle_power']
                divisor = [ONE]
                U = mul(get(label, 'U'), power(get('fc', 'U'), -degree))
                L = sub(get(label, 'logU'), scale(get('fc', 'logU'), degree))
                for parent in f['input_nodes']:
                    key = parent['point_sha256']
                    divisor = poly_mul(divisor, nodeW[key])
                    U, L = mul(U, inv(nodeU[key])), sub(L, nodeL[key])
                key = f['output_node']['point_sha256']
                nodeW[key] = exact_quotient(W(label), divisor)
                nodeU[key], nodeL[key] = U, L
                assert log_unit(U) == L
                if f['phase'] == 'initial_negative':
                    assert nodeW[key] == ws['negative']
            assert nodeW[final] == ws['final']
            assert poly_mul(W('v1'), W('FP')) == poly_mul(ws['final'], W('GQ'))
            Phi = mul(inv(nodeU[final]), mul(mul(get('v1', 'U'), inv(get('fc', 'U'))),
                                           mul(get('FP', 'U'), inv(get('GQ', 'U')))))
            logarithm = sub(add(sub(get('v1', 'logU'), get('fc', 'logU')),
                               sub(get('FP', 'logU'), get('GQ', 'logU'))), nodeL[final])
            assert log_unit(Phi) == logarithm
            endpoint = self.flat['combined_function_to_actual_A1_t']
            independent = power(get('fb', 'U'), endpoint['f_b_integer_exponent'])
            independent = mul(independent, power(get('fc', 'U'), endpoint['f0_integer_exponent']))
            independent = mul(independent, mul(get('v1', 'U'), mul(get('FP', 'U'), inv(get('GQ', 'U')))))
            for factor in self.flat['section_factors']:
                independent = mul(independent, power(get(factor['label'], 'U'), factor['signed_integer_exponent']))
            assert independent == Phi
            rows.append({'target_branch_0based': global_index, 'actual_Phi_value': Phi,
                         'actual_log_Phi_value': logarithm, 'final_distinguished_factor_is_one': True,
                         'four_complete73_ideal_Weierstrass': ws, 'ideal_witness_columns_1based': witnesses,
                         'fixed_Weierstrass': {name: W(name) for name in self.fixed},
                         'all455_actual_effective_divisor_relations_verified': True,
                         'forward_DAG_and_flat_integer_unit_values_equal': True,
                         'section_residual_degree_histogram': dict(sorted(histories[i].items()))})
        return {'rows': rows, 'groups': groups, 'indices_0based': chart['indices_0based'],
                'frame': r.to_json(chart['frame']), 'coordinate': r.to_json(chart['coordinate'])}

    def run(self):
        from p41_miller_unit_atlas47 import ONE, ZERO, add, mul, log_unit
        charts, rows, caches = [], [], []
        self.args.cache_dir.mkdir(parents=True, exist_ok=True)
        for index, chart in enumerate(self.helper.iter_charts(self.W0, order=27, max_points=3, label=self.disk_id+'_T2')):
            cache_path = self.args.cache_dir/(self.disk_id+'_T2_chart'+str(index)+'_jets27.json.gz')
            cache = {name: [self.r.to_json(x) for x in chart[name]] for name in ['W', 'V2', 'V3']}
            cache.update({name: self.r.to_json(chart[name]) for name in ['frame', 'coordinate']})
            cache.update({'indices_0based': chart['indices_0based'], 'input_sha256': self.inputs,
                          'source_sha256': sha(__file__), 'order': 27})
            save(cache_path, cache)
            result = self.process(chart)
            charts.append(result)
            rows.extend(result['rows'])
            caches.append({'basename': cache_path.name, 'sha256': sha(cache_path), 'bytes': cache_path.stat().st_size})
        assert sorted(row['target_branch_0based'] for row in rows) == [0, 1, 2]
        norm, logarithm = ONE, ZERO
        for row in rows:
            norm = mul(norm, row['actual_Phi_value'])
            logarithm = add(logarithm, row['actual_log_Phi_value'])
        assert norm[1] == logarithm[1] == 0 and log_unit(norm) == logarithm
        output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
                  'disk_id': self.disk_id, 'complete_actual_principal_norm_on_T2_P': True,
                  'actual_target_degree': 3, 'target_kernel_polynomial_ascending': self.support['kernel_polynomial_ascending'],
                  'actual_function': 'Phi_C, divisor=scale*(P_center-P_minus3)-A1(t)',
                  'actual_norm_Phi_T2_P_mod47four': norm[0],
                  'actual_log_norm_Phi_T2_P_mod47four': logarithm[0],
                  'all_three_actual_target_disks_prepared': True,
                  'all455_actual_distinguished_relations_in_each_disk': True,
                  'f0_may_be_nonunit_and_its_exact_final_integer_exponent_is_zero': True,
                  'rows': rows, 'charts': charts, 'jet_cache_manifest': caches,
                  'input_sha256': self.inputs, 'dependency_sources_sha256': self.dependency_sources,
                  'source_sha256': sha(__file__),
                  'complete_all53_local_QC_heights': False, 'complete_common_roots': False}
        save(self.args.output, output)
        print('PASS ACTUAL SPLIT T2 PRINCIPAL NORM', self.disk_id, norm[0], logarithm[0],
              'SHA', sha(self.args.output), flush=True)
        return output


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'support', 'principal-expression', 'transport-directory',
                 'based-points', 'second-kind-certificate', 'multiplication', 'cache-dir', 'output']:
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    support = read(args.support)
    if 'branch_records' not in support:
        import p41_ordinary_t2_principal_norm47 as sealed
        sys.argv = [sealed.__file__, '--script-dir', str(args.script_dir), '--support', str(args.support),
                    '--principal-expression', str(args.principal_expression),
                    '--transport-directory', str(args.transport_directory), '--output', str(args.output)]
        runpy.run_path(sealed.__file__, run_name='__main__')
        return
    E = SplitNorm(args)
    E.run()


if __name__ == '__main__':
    main()
