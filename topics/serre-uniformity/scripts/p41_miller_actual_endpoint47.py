#!/usr/bin/env python3
"""Actual final CM/common Miller frame isomorphisms in the fixed or newS chart.

Every output retains the actual t/s and v_frame/f0 factors.  The target
class is independently supplied by R167 or R179, and the complete73-
dimensional ideal isomorphism is checked, not inferred from logarithms.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw), hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, required=True)
    parser.add_argument('--class-name', choices=['cm12', 'cm7', 'common'], required=True)
    parser.add_argument('--frame', choices=['original', 'newS'], default='original')
    parser.add_argument('--miller', type=Path)
    parser.add_argument('--endpoints', type=Path)
    parser.add_argument('--base', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.class_name == 'common':
        assert args.frame == 'original'
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_cm_endpoint_transport47 import actual_transport
    from p41_formal47_multiply import point_hash, write_checkpoint
    started = time.monotonic()
    default_miller = '/tmp/p41_translation_window47_rolling.json.gz' if args.class_name == 'common' else '/tmp/p41_'+args.class_name+'_slp47_rolling.json.gz'
    slp, slp_sha = read(args.miller or Path(default_miller))
    multiplier = slp['target_multiplier']
    if args.class_name == 'common':
        assert slp['point_label'] == 'three_D_b' and slp['current_node'] == 369
        assert len(slp['nodes']) == 369 and slp['current_exponent'] == multiplier
        assert 'zero_test_mod47_in_working_chart' in slp
    else:
        discriminant = int(args.class_name[2:])
        assert slp['point_label'] == 'P_minus'+str(discriminant)
        assert slp['bits_done'] == 304 and slp['sign'] == 1 and slp['magnitude'] == multiplier
        assert len(slp['steps']) == 454
        assert 'zero_test_mod47' in slp or 'zero_test_mod47_in_working_chart' in slp
    assert slp['status'].startswith('complete actual')
    preserved = ['source_sha256', 'point_coordinates', 'point_frobenius', 'point_sha256', 'initial_source_sha256']
    if 'working_chart' in slp:
        preserved.append('working_chart')
    slp = {key: slp[key] for key in preserved}
    if args.class_name == 'common':
        endpoints, endpoints_sha = read(args.endpoints or folder/'data/p41_translation_formal_endpoints47_checkpoint.json.gz')
        base, base_sha = read(args.base or folder/'data/p41_hecke3_formal_height47_compact.json.gz')
        assert endpoints['target_multiplier'] == multiplier and endpoints['integer_factor'] == 3
        assert endpoints['family_index'] == 1
        assert endpoints['input_sha256']['original_Abel_bases'] == base['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']
        target = endpoints['targets']['three_m_D_b']['exponentials']['positive']
        assert target['family_index'] == 1
        base_coefficients = base['families'][1]['base_section_coefficients']
        target_description = 'R141 family1 at3mD_b'
    elif args.frame == 'original':
        endpoints, endpoints_sha = read(args.endpoints or folder/'data/p41_cm_formal_endpoints47_checkpoint.json.gz')
        base, base_sha = read(args.base or folder/'data/p41_hecke3_formal_height47_compact.json.gz')
        assert endpoints['target_multiplier'] == multiplier
        assert endpoints['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz'] == base['input_sha256']['p41_hecke3_abel_bases_checkpoint.json.gz']
        target = endpoints['targets']['x'+str(discriminant)]['targets']['m']['exponentials'][0]
        assert target['family_index'] == 0
        base_coefficients = base['families'][0]['base_section_coefficients']
        target_description = 'R141 family0 at mC'+str(discriminant)
    else:
        endpoints, endpoints_sha = read(args.endpoints or folder/('data/p41_t2_cm'+str(discriminant)+'_formal_transport47_checkpoint.json.gz'))
        base, base_sha = read(args.base or folder/'data/p41_t2_cm_abel_base47_checkpoint.json.gz')
        assert endpoints['class_name'] == 'x'+str(discriminant)
        assert endpoints['new_base_sha256'] == base_sha
        target = endpoints['endpoints'][0]
        base_coefficients = base['family']['v_coefficients']
        target_description = 'R179 newS at mC'+str(discriminant)
    assert slp['source_sha256'] == endpoints['source_sha256'] == base['source_sha256']
    target = {key: target[key] for key in ['point_coordinates', 'point_frobenius', 'point_sha256']}
    del endpoints, base
    gc.collect()
    sources, hashes = load_sources(folder/'data')
    assert slp['source_sha256'] == hashes
    M0 = make_model(sources)
    original_A2 = M0['A2']
    Kold, Aold = r.from_json(slp['point_coordinates']), r.from_json(slp['point_frobenius'])
    Knew, Anew = r.from_json(target['point_coordinates']), r.from_json(target['point_frobenius'])
    old_sha, target_sha = slp['point_sha256'], target['point_sha256']
    assert point_hash(Kold, Aold) == old_sha and point_hash(Knew, Anew) == target_sha
    for coefficients, action in [(Kold, Aold), (Knew, Anew)]:
        assert r.equal(r.mm(original_A2, r.conjugate(coefficients)), r.mm(coefficients, action))
    C2 = r.eye(199)
    if 'working_chart' in slp:
        omitted = {j-1 for j in slp['working_chart']['omitted_evaluation_rows_1based']}
        keep = [j for j in range(820) if j not in omitted]
        assert len(keep) > 504 and all(M0['tau'][j] in omitted for j in omitted)
        V2, P2, columns, C2 = r.normalize(r.rows(M0['V2'], keep), 199)
        assert columns == list(range(199))
        assert hashlib.sha256(json.dumps(r.to_json(C2), separators=(',', ':')).encode()).hexdigest() == slp['working_chart']['V2_change_sha256']
        inverse = r.inverse_matrix(C2)
        Kold, Knew = r.mm(inverse, Kold), r.mm(inverse, Knew)
    else:
        V2, P2 = M0['V2'], M0['P2']
    M = {'V2': V2, 'P2': P2}
    del M0, sources, slp, target
    gc.collect()
    try:
        ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:
        pass
    seed = 4104718203 if args.class_name == 'common' else 4104718200+discriminant+(100 if args.frame == 'newS' else 0)
    numerator, denominator, record = actual_transport(Kold, Aold, Knew, Anew, M, random.Random(seed), r)
    numerator, denominator = r.mm(C2, numerator), r.mm(C2, denominator)
    for coefficients in [numerator, denominator]:
        assert r.equal(r.mm(original_A2, r.conjugate(coefficients)), coefficients)
    record.update({'new_section_coefficients': r.to_json(numerator),
                   'old_section_coefficients': r.to_json(denominator),
                   'v1_coefficients': base_coefficients})
    result = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'source_sha256': hashes,
              'class_name': args.class_name, 'frame': args.frame, 'target_description': target_description,
              'target_multiplier': multiplier,
              'input_sha256': {'miller': slp_sha, 'formal_endpoints': endpoints_sha, 'base': base_sha},
              'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'actual_transport_helper_sha256': hashlib.sha256(Path(actual_transport.__code__.co_filename).read_bytes()).hexdigest(),
              'old_final_point_sha256': old_sha, 'new_formal_point_sha256': target_sha,
              'transport': record,
              'transport_function': 'g=(new/f0^2)/(old/f0^2)/(v_frame/f0), div(g)=A_frame-A_old',
              'true_function': 'f=F_chain/(g*h_initial^m); h_initial=h_D for common3Db and f_b/f0 for CM',
              'status': 'complete actual final point equals independent formal target; full73-dimensional ideal isomorphism and true frame function retained; no norm or height assigned'}
    if args.class_name != 'common':
        result['discriminant'] = -discriminant
    output = args.output or Path('/tmp/p41_'+args.class_name+'_'+args.frame+'_endpoint47_certificate.json.gz')
    sha, size = write_checkpoint(output, result)
    print('ACTUAL MILLER ENDPOINT PASS', args.class_name, args.frame, size, sha,
          'seconds', round(time.monotonic()-started, 2),
          'peak_MiB', round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024, 2), flush=True)


if __name__ == '__main__':
    main()
