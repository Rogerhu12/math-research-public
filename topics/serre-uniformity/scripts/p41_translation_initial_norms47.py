#!/usr/bin/env python3
"""Actual h_D=R_g1^2*h^324/F_build norms at the two CM formal first frames.

The initial divisor is the actual common 3D_b representative.  All values
come from its saved short SLP and the same Weierstrass/KS normalization.
No long Jacobian multiplication is repeated.
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
    parser.add_argument('--bases', type=Path, help='R145 compact by default; the original complete Abel-bases checkpoint is also accepted')
    parser.add_argument('--jets', type=Path)
    parser.add_argument('--cm-endpoints', type=Path)
    parser.add_argument('--output', type=Path, default=Path('/tmp/p41_translation_initial_norms47_checkpoint.json.gz'))
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_hecke3_hessian47 import section_jets
    from p41_poincare_norms47 import pair_mul, pair_inverse
    from p41_formal47_multiply import write_checkpoint
    started = time.monotonic()
    build, build_sha = read(args.build)
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
    assert build['source_sha256'] == bases_source == cm_source == hashes
    assert build['status'].startswith('complete actual integral point 3*D_b')
    assert len(build['steps']) == 24 and build['current_expression'] == [486, -162, -81, -6, 17]
    V2, V3 = section_jets(W, sources, M, r)
    values = {1: W, 2: V2, 3: V3}
    f0 = r.from_json(build['base_f0_coefficients'])
    g1 = r.from_json(build['actual_g1_coefficients'])
    fb = r.from_json(build['initial_h_coefficients'])
    for coefficient in [f0, g1, fb]:
        assert r.equal(r.mm(M['A1'], r.conjugate(coefficient)), coefficient)
    del M, sources
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
        records.append({'discriminant': -discriminant, 'family_index': 0,
                        'actual_formal_point_sha256': target['point_sha256'],
                        'actual_delta_norm': deltanorm, 'actual_raw_g1_norm': Wgnorm,
                        'actual_f0_norm': f0norm, 'actual_g1_over_f0_norm': hgnorm,
                        'actual_R_f0_norm': Rf0norm, 'actual_R_g1_norm': Rnorm,
                        'actual_h_norm': hnorm, 'actual_negative_basis_norms': negative,
                        'short_SLP_norms': steps, 'actual_Fbuild_norm': cumulative,
                        'actual_initial_h_D_norm': hDnorm, 'log_initial_h_D_norm': logarithm(hDnorm),
                        'all_actual_principal_values_units': True,
                        'formula': 'N(h_D)=N(R_g1)^2*N(f_b/f0)^324/N(F_build)',
                        'meaning': 'actual initial principal transport evaluated on A_family0(mC); this is one required factor, not the complete height'})
        print('ACTUAL COMMON INITIAL TRANSPORT NORM', discriminant, 'R', Rnorm, 'h', hnorm,
              'Fbuild', cumulative, 'hD', hDnorm, 'log', logarithm(hDnorm), flush=True)
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'input_sha256': {'short_build': build_sha, 'bases': bases_sha, 'actual_source_jets': jets_sha, 'CM_formal_endpoints': cm_sha},
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'records': records,
              'status': 'complete actual initial-transport norms of the common3Db point on both CM first formal frames; canonical change and short SLP retained; no full height claimed'}
    sha, size = write_checkpoint(args.output, result)
    print('ACTUAL COMMON INITIAL TRANSPORT NORMS SAVED', size, sha, 'seconds', round(time.monotonic()-started, 2), 'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
