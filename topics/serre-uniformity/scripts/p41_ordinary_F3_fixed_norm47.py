#!/usr/bin/env python3
"""Actual F3 divisor norm, with verified reuse of the same Phi's K and tangents."""
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
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


class F3Norm:
    def __init__(self, args):
        import p41_r2_matrix as r
        from p41_actual_differentials47 import ActualModel
        from p41_projective_jet_frames47 import ProjectiveJetFrames, install_exact_float_mm
        from p41_miller_unit_atlas47 import MillerUnitAtlas
        from p41_ordinary_B_fibre47 import Engine as BEngine
        from p41_ordinary_t2_etale_norm47 import SplitNorm
        install_exact_float_mm(r)
        self.a = a = ActualModel(args.script_dir)
        self.r, self.np, self.args = r, a.np, args
        self.inputs = dict(a.inputs)
        self.based = read(args.based_points)
        self.inputs[args.based_points.name] = sha(args.based_points)
        self.bases = a.read('p41_hecke3_abel_bases_checkpoint.json.gz')
        self.family = self.bases['families'][0]
        self.v1 = r.from_json(self.family['v_coefficients'])
        self.fb = r.from_json(self.based['f_b_coefficients'])
        BEngine.load(self, args.second_kind_certificate, args.multiplication,
                     args.transport_directory, args.principal_expression)
        self.preparer = MillerUnitAtlas.__new__(MillerUnitAtlas)
        self.preparer.a, self.preparer.r, self.preparer.np = a, r, a.np
        self.helper = ProjectiveJetFrames(a)
        self.support = read(args.fixed_support)
        self.reused = read(args.same_phi_F2_norm)
        self.t3norm = read(args.t3_norm)
        assert self.reused['disk_id'] == self.t3norm['disk_id'] == self.disk_id
        assert self.reused['complete_actual_first_variable_norm_on_F2_second_divisor']
        assert self.t3norm['complete_actual_principal_norm_on_T3_P']
        assert self.flat['combined_function_to_actual_A1_t']['f0_integer_exponent'] == 0
        # These are precisely the same first function, integer scale and physical endpoint.
        self.reused_edges = []
        for path in [args.principal_expression, args.second_kind_certificate,
                     args.multiplication, args.based_points]:
            for cert in [self.reused, self.t3norm]:
                matches = [v for k, v in cert['input_sha256'].items() if Path(k).name == path.name]
                assert matches and set(matches) == {sha(path)}, path
            self.reused_edges.append({'basename':path.name, 'sha256':sha(path)})
        assert self.reused['input_sha256'][args.canonical.name] == sha(args.canonical)
        self.points = []
        for group, weight in [('Z12', -9), ('Z0fix', -9), ('c11', -18), ('v', 27)]:
            g = self.support['groups'][group]
            assert g['actual_Frobenius_stable_mod47four'] and g['all_fc_unit']
            for point in g['points']:
                if group == 'Z0fix' and point['is_basepoint_b']:
                    continue
                self.points.append(dict(point, group=group, F3_divisor_weight=weight))
        assert len(self.points) == 31
        assert sum(x['F3_divisor_weight'] for x in self.points) == -252
        self.W0 = r.from_json([x['W_mod47four'] for x in self.points])
        assert self.W0[0].shape == (31, 73)
        assert r.equal(r.mm(self.W0, a.fc), r.column([[1, 0]]*31))
        self.inputs.update(a.inputs)
        for path in [args.fixed_support, args.same_phi_F2_norm, args.t3_norm, args.canonical]:
            self.inputs[path.name] = sha(path)
        self.dependency_sources = {name+'.py':sha(sys.modules[name].__file__) for name in [
            'p41_ordinary_B_fibre47', 'p41_projective_jet_frames47',
            'p41_miller_unit_atlas47', 'p41_ordinary_t2_etale_norm47']}
        self.process_chart = lambda chart: SplitNorm.process(self, chart)

    def run(self):
        from p41_miller_unit_atlas47 import ONE, ZERO, add, mul, power, scale, log_unit
        charts, rows, caches = [], [], []
        self.args.cache_dir.mkdir(parents=True, exist_ok=True)
        for index, chart in enumerate(self.helper.iter_charts(
                self.W0, order=27, max_points=16, label=self.disk_id+'_F3_fixed')):
            path = self.args.cache_dir/(self.disk_id+'_F3_fixed_chart'+str(index)+'_jets27.json.gz')
            cache = {name:[self.r.to_json(x) for x in chart[name]] for name in ['W', 'V2', 'V3']}
            cache.update({name:self.r.to_json(chart[name]) for name in ['frame', 'coordinate']})
            cache.update({'indices_0based':chart['indices_0based'], 'input_sha256':self.inputs,
                          'source_sha256':sha(__file__), 'order':27})
            save(path, cache)
            result = self.process_chart(chart)
            for row in result['rows']:
                point = self.points[row['target_branch_0based']]
                row['label'] = point['label']
                row['group'] = point['group']
                row['second_divisor_weight'] = point['F3_divisor_weight']
            charts.append(result)
            rows.extend(result['rows'])
            caches.append({'basename':path.name, 'sha256':sha(path), 'bytes':path.stat().st_size})
            print('PASS actual F3 fixed chart', index, len(result['rows']), 'points', flush=True)
        assert sorted(x['target_branch_0based'] for x in rows) == list(range(31))
        norm, logarithm = ONE, ZERO
        for row in rows:
            weight = row['second_divisor_weight']
            norm = mul(norm, power(row['actual_Phi_value'], weight))
            logarithm = add(logarithm, scale(row['actual_log_Phi_value'], weight))
        assert norm[1] == logarithm[1] == 0 and log_unit(norm) == logarithm
        collision = {x['label']:x for x in self.reused['fixed_and_collision_part']['rows']}
        collision_rows = [collision[x] for x in ['P_minus3', self.disk_id]]
        assert all(x['all455_actual_distinguished_relations_verified'] for x in collision_rows)
        collision_logs = [x['log_leading_unit_in_j_mod47four'] for x in collision_rows]
        assert all(x[1] == 0 for x in collision_logs)
        canonical_log = self.reused['full_canonical_degree106_log_norm']
        total = (logarithm[0] + 2*sum(x[0] for x in collision_logs) + 2*canonical_log
                 + 9*self.t3norm['actual_log_norm_Phi_T3_P_mod47four']) % Q
        output = {
            'level':41, 'auxiliary_prime':P, 'precision':4, 'modulus':Q, 'disk_id':self.disk_id,
            'complete_actual_first_variable_norm_on_F3_second_divisor':True,
            'actual_second_divisor':'9*T3(P)+27*v-9*Z12-9*(Z0fix-b)-18*c11+2*P+2*b+2*K_g1',
            'second_divisor_degree':9*4+27-9*22-9*7-18+2+2+2*106,
            'first_function':self.reused['first_function'],
            'actual_integer_scale':self.reused['actual_integer_scale'],
            'actual_log_norm_Phi_on_F3_second_divisor_mod47four':total,
            'fixed31_weighted_norm_mod47four':norm[0],
            'fixed31_weighted_log_norm_mod47four':logarithm[0],
            'fixed31_weighted_degree':-252,
            'fixed31_rows':rows, 'fixed31_charts':charts, 'jet_cache_manifest':caches,
            'reused_canonical_degree106_log_norm':canonical_log,
            'reused_P_and_b_in_the_same_j_tangents':collision_rows,
            'reused_same_Phi_input_hash_edges':self.reused_edges,
            'g1_actual73_coefficients':self.reused['g1_actual73_coefficients'],
            'weighted_T3_log_norm':9*self.t3norm['actual_log_norm_Phi_T3_P_mod47four'] % Q,
            'tame_symbol_sign_is_one_equal_even_collision_weights':True,
            'canonical_norm_reused_only_after_actual_input_identity_checks':True,
            'input_sha256':self.inputs, 'dependency_sources_sha256':self.dependency_sources,
            'source_sha256':sha(__file__),
            'complete_actual_local_sigma_F3_height':False,
            'complete_all53_local_QC_heights':False, 'complete_common_roots':False,
        }
        assert output['second_divisor_degree'] == 0
        save(self.args.output, output)
        print('PASS ACTUAL FULL F3 PRINCIPAL NORM', self.disk_id, total,
              'fixed31', logarithm[0], 'SHA', sha(self.args.output), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'fixed-support', 'same-phi-F2-norm', 't3-norm', 'canonical',
                 'principal-expression', 'transport-directory', 'based-points',
                 'second-kind-certificate', 'multiplication', 'cache-dir', 'output']:
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    F3Norm(args).run()


if __name__ == '__main__':
    main()
