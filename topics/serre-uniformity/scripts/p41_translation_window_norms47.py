#!/usr/bin/env python3
"""Actual norm and all54 cubic jets of the common width-five Miller DAG.

The complete short initial transport, signed precomputation functions and
optional true endpoint frame are retained.  No group operations are repeated.
The resulting function norms are not themselves global heights.
"""
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import sys
import resource
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--build', type=Path, default=Path('/tmp/p41_translation_build47_complete.json.gz'))
    parser.add_argument('--miller', type=Path, default=Path('/tmp/p41_translation_window47_rolling.json.gz'))
    parser.add_argument('--endpoint', type=Path)
    parser.add_argument('--initial-norms', type=Path)
    parser.add_argument('--bases', type=Path, help='R145 compact by default; the original complete Abel-bases checkpoint is also accepted')
    parser.add_argument('--jets', type=Path)
    parser.add_argument('--cm-endpoints', type=Path)
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_translation_window_norms47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_norms47 import pair_mul, pair_inverse
    from p41_formal47_multiply import write_checkpoint
    from p41_poincare_miller_jets47 import evaluate_jet
    from p41_cm4_divisor47 import kernel
    started = time.monotonic()
    build, build_sha = read(args.build)
    slp, slp_sha = read(args.miller)
    slp = {key: slp[key] for key in ['source_sha256', 'initial_source_sha256', 'target_multiplier', 'current_node', 'current_exponent', 'plan_sha256', 'plan', 'nodes', 'point_sha256', 'status']}
    assert slp['initial_source_sha256'] == build_sha
    assert slp['current_node'] == len(slp['nodes']) and slp['nodes']
    assert slp['current_exponent'] == slp['nodes'][-1]['exponent']
    expected, expected_sha = read(args.initial_norms or folder/'data/p41_translation_initial_norms47_checkpoint.json.gz')
    assert expected['input_sha256']['short_build'] == build_sha
    expected_initial = {abs(record['discriminant']): record for record in expected['records']}
    endpoint = None
    endpoint_sha = None
    if args.endpoint:
        endpoint, endpoint_sha = read(args.endpoint)
        assert slp['current_node'] == 369 and slp['current_exponent'] == slp['target_multiplier']
        assert slp['status'].startswith('complete actual')
        assert endpoint['class_name'] == 'common' and endpoint['frame'] == 'original'
        assert endpoint['input_sha256']['miller'] == slp_sha

    needed = ['source_sha256', 'status', 'steps', 'current_expression', 'base_f0_coefficients',
              'actual_g1_coefficients', 'initial_h_coefficients', 'negative_basis_quadratic_coefficients']
    build = {key: build[key] for key in needed}
    bases, bases_sha = read(args.bases or folder/'data/p41_hecke3_formal_height47_compact.json.gz')
    bases_source = bases['source_sha256']
    expected_jets_sha = bases.get('jets_sha256')
    original_bases_sha = bases_sha if expected_jets_sha is not None else bases['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']
    labels = [i-1 for i in bases['families'][0]['points_1based']]
    del bases
    assert 253 not in labels
    jets, jets_sha = read(args.jets or folder/'data/p41_source_cubic47_full_saved.json.gz')
    if expected_jets_sha is not None:
        assert expected_jets_sha == jets_sha
    W = [r.rows(r.from_json(matrix), labels) for matrix in jets['evaluation_coefficients']]
    del jets
    assert len(W) >= 4
    cm, cm_sha = read(args.cm_endpoints or folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
    assert cm['input_sha256']['p41_source_cubic47_checkpoint.json.gz'] == jets_sha
    assert cm['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz'] == original_bases_sha
    cm_source = cm['source_sha256']
    cm_targets = {}
    for discriminant in [12, 7]:
        target = cm['targets']['x'+str(discriminant)]['targets']['m']['exponentials'][0]
        assert target['family_index'] == 0
        cm_targets[discriminant] = {'parameters': target['parameters'], 'point_sha256': target['point_sha256']}
    del target, cm
    gc.collect()
    sources, hashes = load_sources(folder/'data')
    M = make_model(sources)
    assert build['source_sha256'] == bases_source == cm_source == slp['source_sha256'] == expected['source_sha256'] == hashes
    assert expected['input_sha256']['CM_formal_endpoints'] == cm_sha
    if endpoint is not None:
        assert endpoint['source_sha256'] == hashes
    assert build['status'].startswith('complete actual integral point 3*D_b')
    assert len(build['steps']) == 24 and build['current_expression'] == [486, -162, -81, -6, 17]
    V2, V3 = section_jets(W, sources, M, r)
    values = {1: W, 2: V2, 3: V3}
    f0 = r.from_json(build['base_f0_coefficients'])
    g1 = r.from_json(build['actual_g1_coefficients'])
    fb = r.from_json(build['initial_h_coefficients'])
    for coefficient in [f0, g1, fb]:
        assert r.equal(r.mm(M['A1'], r.conjugate(coefficient)), coefficient)
    permutation = [labels.index(M['tau'][j]) for j in labels]
    divisors = sources[1]
    K1 = r.from_json(kernel(73, divisors['cusp_rank_columns_1based'], divisors['cusp_free_columns_1based'], divisors['canonical_kernel_block']))
    Omega = tuple(a*(-3*pow(27652, -1, r.Q) % r.Q) % r.Q for a in r.mm(W[0], K1))
    Omega_inverse = r.inverse_matrix(Omega)
    canonical_frobenius = r.from_json(divisors['canonical_frobenius_matrix'])
    del M, sources, divisors, expected
    gc.collect()
    one = r.column([[1, 0] for _ in range(54)])

    def scale(a, c):
        return tuple(x*(int(c) % r.Q) % r.Q for x in a)

    def product(a):
        answer = [1, 0]
        assert np.all(r.units(a))
        for j in range(54):
            answer = pair_mul(answer, [int(a[0][j, 0]), int(a[1][j, 0])])
        return answer

    def ratio_norm(shifted, original):
        answer = pair_mul(product(shifted), pair_inverse(product(original)))
        assert answer[1] == 0 and answer[0] % 47 == 1
        return answer[0]

    def logarithm(a):
        assert a % 47 == 1
        z = (a-1) % r.Q
        return (z-z*z*pow(2, -1, r.Q)+z*z*z*pow(3, -1, r.Q)) % r.Q

    def raw_log_jet(coefficients):
        assert len(coefficients) >= 4 and np.all(r.units(coefficients[0]))
        inverse = r.inverse_values(coefficients[0])
        u, v, w = [r.mul(coefficients[j], inverse) for j in [1, 2, 3]]
        return r.hcat(u, r.sub(v, scale(r.mul(u, u), pow(2, -1, r.Q))),
                      r.add(r.sub(w, r.mul(u, v)), scale(r.mul(r.mul(u, u), u), pow(3, -1, r.Q))))

    f0jet = raw_log_jet([r.mm(v, f0) for v in values[1]])

    def section_jet(coefficient, degree):
        answer = r.sub(raw_log_jet([r.mm(v, coefficient) for v in values[degree]]), scale(f0jet, degree))
        assert r.equal(r.rows(answer, permutation), r.conjugate(answer))
        return answer

    delta_coefficients = [scale(one, -16*(4+27*32**2)), scale(one, -16*54*32),
                          scale(one, -16*27), r.zeros(54, 1)]
    Rjet = r.sub(raw_log_jet(delta_coefficients), scale(raw_log_jet([r.mm(v, g1) for v in values[1]]), 6))
    hjet = section_jet(fb, 1)
    negative_jets = {label: scale(section_jet(r.from_json(coefficient), 2), -1)
                     for label, coefficient in build['negative_basis_quadratic_coefficients'].items()}
    Fbuildjet = r.zeros(54, 3)
    for step in build['steps']:
        jet = section_jet(r.from_json(step['principal_section_coefficients']), step['principal_section_degree'])
        if step['operation'] == 'double':
            Fbuildjet = scale(r.add(scale(Fbuildjet, 2), jet), -1)
        elif step['operation'] == 'add':
            operand = r.zeros(54, 3) if step['operand_sign'] == 1 else negative_jets[step['operand']]
            Fbuildjet = scale(r.add(r.add(Fbuildjet, operand), jet), -1)
        else:
            assert step['operation'] == 'flip'
            Fbuildjet = scale(r.add(Fbuildjet, jet), -1)
    initial_jet = r.sub(r.add(scale(Rjet, 2), scale(hjet, 324)), Fbuildjet)
    assert r.equal(r.rows(initial_jet, permutation), r.conjugate(initial_jet))
    function_jets = {0: r.zeros(54, 3)}
    integer_expressions = {0: 1}
    for planned, node in zip(slp['plan'], slp['nodes']):
        for key, value in planned.items():
            assert node[key] == value
        number, left = node['node'], node['left']
        assert number == len(function_jets) and left < number
        encoded = node['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest() == node['principal_coefficient_sha256']
        jet = section_jet(r.from_json(encoded), node['principal_section_degree'])
        if node['operation'] == 'flip':
            assert node['principal_section_degree'] == 2
            function_jets[number] = scale(r.add(function_jets[left], jet), -1)
            exponent = -integer_expressions[left]
        else:
            assert node['principal_section_degree'] == 3
            right = node['right']; assert right < number
            function_jets[number] = scale(r.add(r.add(function_jets[left], function_jets[right]), jet), -1)
            exponent = -integer_expressions[left]-integer_expressions[right]
        assert exponent == node['exponent']
        integer_expressions[number] = exponent
    current_jet = function_jets[slp['current_node']]
    true_jet = None
    if endpoint is not None:
        tr = endpoint['transport']
        transition_jet = r.sub(r.sub(section_jet(r.from_json(tr['new_section_coefficients']), 2),
                                      section_jet(r.from_json(tr['old_section_coefficients']), 2)),
                               section_jet(r.from_json(tr['v1_coefficients']), 1))
        true_jet = r.sub(r.sub(current_jet, transition_jet), scale(initial_jet, slp['target_multiplier']))
        actual_lie_gradient = r.mm(Omega_inverse, r.cols(true_jet, [0]))
        assert r.equal(r.mm(canonical_frobenius, r.conjugate(actual_lie_gradient)), actual_lie_gradient)
    records = []
    for discriminant in [12, 7]:
        target = cm_targets[discriminant]
        parameters = r.from_json(target['parameters'])
        t = parameters[0].T, parameters[1].T
        assert t[0].shape == (54, 1) and all(np.all(a % 47 == 0) for a in t)
        shifted = {}
        for degree, coefficients in values.items():
            total = r.zeros(54, coefficients[0][0].shape[1])
            for coefficient in reversed(coefficients):
                total = r.add(r.mul(total, t), coefficient)
            shifted[degree] = total
        f0norm = ratio_norm(r.mm(shifted[1], f0), r.mm(W[0], f0))

        def section_norm(coefficient, degree):
            raw = ratio_norm(r.mm(shifted[degree], coefficient), r.mm(values[degree][0], coefficient))
            return raw*pow(f0norm, -degree, r.Q) % r.Q

        hnorm = section_norm(fb, 1)
        Wgnorm = ratio_norm(r.mm(shifted[1], g1), r.mm(W[0], g1))
        B = r.add(scale(one, 32), t)
        delta = scale(r.add(scale(one, 4), scale(r.mul(B, B), 27)), -16)
        delta0 = scale(one, -16*(4+27*32**2))
        deltanorm = ratio_norm(delta, delta0)
        Rnorm = deltanorm*pow(Wgnorm, -6, r.Q) % r.Q
        # Check the fixed f0 version and the exact g1/f0 change separately.
        Rf0norm = deltanorm*pow(f0norm, -6, r.Q) % r.Q
        hgnorm = section_norm(g1, 1)
        assert Rnorm == Rf0norm*pow(hgnorm, -6, r.Q) % r.Q
        negative = {label: section_norm(r.from_json(coefficient), 2)
                    for label, coefficient in build['negative_basis_quadratic_coefficients'].items()}
        cumulative = 1
        steps = []
        for index, step in enumerate(build['steps'], 1):
            encoded = step['principal_section_coefficients']
            assert hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest() == step['principal_coefficient_sha256']
            degree = step['principal_section_degree']
            norm = section_norm(r.from_json(encoded), degree)
            if step['operation'] == 'double':
                cumulative = pow(cumulative*cumulative % r.Q*norm % r.Q, -1, r.Q)
            elif step['operation'] == 'add':
                operand = 1 if step['operand_sign'] == 1 else pow(negative[step['operand']], -1, r.Q)
                cumulative = pow(cumulative*operand % r.Q*norm % r.Q, -1, r.Q)
            else:
                assert step['operation'] == 'flip' and degree == 2
                cumulative = pow(cumulative*norm % r.Q, -1, r.Q)
            steps.append({'step_index_1based': index, 'principal_coefficient_sha256': step['principal_coefficient_sha256'],
                          'actual_principal_norm': norm, 'cumulative_actual_Fbuild_norm': cumulative})
        hDnorm = pow(Rnorm, 2, r.Q)*pow(hnorm, 324, r.Q)*pow(cumulative, -1, r.Q) % r.Q
        assert logarithm(hDnorm) == (2*logarithm(Rnorm)+324*logarithm(hnorm)-logarithm(cumulative)) % r.Q
        assert hDnorm == expected_initial[discriminant]['actual_initial_h_D_norm']
        assert evaluate_jet(initial_jet, target['parameters'], r) == logarithm(hDnorm)
        function_norms = {0: 1}
        window_records = []
        for node in slp['nodes']:
            norm = section_norm(r.from_json(node['principal_section_coefficients']), node['principal_section_degree'])
            parent = function_norms[node['left']]
            if node['operation'] != 'flip':
                parent = parent*function_norms[node['right']] % r.Q
            value = pow(parent*norm % r.Q, -1, r.Q)
            function_norms[node['node']] = value
            assert evaluate_jet(function_jets[node['node']], target['parameters'], r) == logarithm(value)
            window_records.append({'node': node['node'], 'principal_coefficient_sha256': node['principal_coefficient_sha256'],
                                   'actual_principal_norm': norm, 'actual_Fnode_norm': value})
        final_norm = function_norms[slp['current_node']]
        additional = {'window_nodes': window_records, 'actual_current_F_norm': final_norm,
                      'log_actual_current_F_norm': logarithm(final_norm)}
        if endpoint is not None:
            transition_norm = section_norm(r.from_json(tr['new_section_coefficients']), 2)
            transition_norm = transition_norm*pow(section_norm(r.from_json(tr['old_section_coefficients']), 2), -1, r.Q) % r.Q
            transition_norm = transition_norm*pow(section_norm(r.from_json(tr['v1_coefficients']), 1), -1, r.Q) % r.Q
            assert evaluate_jet(transition_jet, target['parameters'], r) == logarithm(transition_norm)
            true_norm = final_norm*pow(transition_norm*pow(hDnorm, slp['target_multiplier'], r.Q) % r.Q, -1, r.Q) % r.Q
            assert evaluate_jet(true_jet, target['parameters'], r) == logarithm(true_norm)
            additional.update({'actual_endpoint_transition_norm': transition_norm,
                               'true_f_D_norm': true_norm, 'log_true_f_D_norm': logarithm(true_norm)})
        record = {'discriminant': -discriminant, 'family_index': 0,
                        'actual_formal_point_sha256': target['point_sha256'],
                        'actual_delta_norm': deltanorm, 'actual_raw_g1_norm': Wgnorm,
                        'actual_f0_norm': f0norm, 'actual_g1_over_f0_norm': hgnorm,
                        'actual_R_f0_norm': Rf0norm, 'actual_R_g1_norm': Rnorm,
                        'actual_h_norm': hnorm, 'actual_negative_basis_norms': negative,
                        'short_SLP_norms': steps, 'actual_Fbuild_norm': cumulative,
                        'actual_initial_h_D_norm': hDnorm, 'log_initial_h_D_norm': logarithm(hDnorm),
                        'all_actual_principal_values_units': True,
                        'formula': 'N(h_D)=N(R_g1)^2*N(f_b/f0)^324/N(F_build)',
                        'meaning': 'actual common-window function evaluated on A_family0(mC), retaining the initial and optional endpoint transport; not a height'}
        record.update(additional)
        records.append(record)
        print('ACTUAL COMMON WINDOW NORM', discriminant, 'node', slp['current_node'], 'F', final_norm, 'hD', hDnorm, 'true_f_D', additional.get('true_f_D_norm'), flush=True)
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'input_sha256': {'short_build': build_sha, 'bases': bases_sha, 'actual_source_jets': jets_sha, 'CM_formal_endpoints': cm_sha, 'miller': slp_sha, 'initial_transport_norms': expected_sha, 'endpoint': endpoint_sha},
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'records': records, 'current_node': slp['current_node'], 'current_exponent': slp['current_exponent'],
              'target_multiplier': slp['target_multiplier'], 'actual_h_D_log_jet': r.to_json(initial_jet),
              'actual_Fcurrent_log_jet': r.to_json(current_jet),
              'status': 'actual common width5 Miller DAG norms and all54 cubic jets through the saved prefix; no height claimed'}
    if endpoint is not None:
        result.update({'actual_endpoint_transition_log_jet': r.to_json(transition_jet),
                       'true_f_D_log_jet': r.to_json(true_jet),
                       'true_f_D_Lie_log_gradient_mod47four': r.to_json(actual_lie_gradient),
                       'status': 'complete actual f_D=F/(g*h_D^m) norms on both CM first formal frames and all54 cubic jets; div(f_D)=3mD_b-A_family1; this remains a function input, not a global height'})
    sha, size = write_checkpoint(args.output, result)
    print('ACTUAL COMMON WINDOW NORMS SAVED', size, sha, 'seconds', round(time.monotonic()-started, 2), 'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
