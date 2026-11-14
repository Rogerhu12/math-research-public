#!/usr/bin/env python3
"""Compare two audited actual tails at exactly the same complete physical H."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def load(path):
    data = path.read_bytes()
    obj = json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)
    response = obj['response']
    if not response.get('converged') or response.get('failed'):
        raise ValueError(f'An actual successful tail is required: {path}')
    if not response.get('audit'):
        raise ValueError(f'A complete finite-tail audit is required: {path}')
    return obj, hashlib.sha256(data).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--coarse', type=Path, required=True)
    p.add_argument('--fine', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    coarse, coarse_hash = load(a.coarse)
    fine, fine_hash = load(a.fine)
    hc, hf = coarse['request']['height'], fine['request']['height']
    if len(hf) < len(hc) or hf[:len(hc)] != hc or any(hf[len(hc):]):
        raise ValueError('The complete original H must be exactly preserved and new modes strictly zero')
    # These fields control the discretization, nonlinear iteration, or records;
    # every other constructor field, including physical depth, is held fixed.
    numerical = {
        'modes', 'quadrature', 'shootingParts', 'steps', 'auditSteps',
        'maxIterations', 'initialCheckpoint', 'iterationCheckpointFile',
        'traceFile', 'trialDiagnosticFile',
    }
    cc, cf = coarse['config'], fine['config']
    all_keys = sorted(cc.keys() | cf.keys())
    changes = {k: [cc.get(k), cf.get(k)] for k in all_keys if cc.get(k) != cf.get(k)}
    unexpected = set(changes) - numerical
    if unexpected:
        raise ValueError(f'Physical or unapproved algorithmic changes: {sorted(unexpected)}')
    shared_hashes = coarse['source_sha256'].keys() & fine['source_sha256'].keys()
    changed_hashes = [k for k in sorted(shared_hashes)
                      if coarse['source_sha256'][k] != fine['source_sha256'][k]]
    if changed_hashes:
        raise ValueError(f'Shared source files differ: {changed_hashes}')

    def summary(obj, path, file_hash):
        c, r = obj['config'], obj['response']
        audit = dict(r['audit'])
        audit['originalProfileNormalizedFullDefect'] = (
            c['shootingParts'] * audit['normalizedFullDefect'])
        return {
            'file': str(path), 'sha256': file_hash,
            'discretization': {k: c[k] for k in
                               ['modes', 'quadrature', 'depth', 'shootingParts',
                                'steps', 'auditSteps', 'projectionFloor']},
            'steps_per_original_profile': c['shootingParts'] * c['steps'],
            'audit_steps_per_original_profile': c['shootingParts'] * c['auditSteps'],
            'nonlinear_residual': r['residual'], 'audit': audit,
            'cut_jets': r['jets'],
        }

    sc = summary(coarse, a.coarse, coarse_hash)
    sf = summary(fine, a.fine, fine_hash)
    metrics = ['fullD', 'originalProfileNormalizedFullDefect', 'actualMetric',
               'formalCurvature', 'minLeading', 'minD', 'holonomy']
    ratios = {k: sf['audit'][k] / sc['audit'][k] if sc['audit'][k] else None
              for k in metrics}
    jc, jf = coarse['response']['jets'], fine['response']['jets']
    jet_differences = {}
    for k in ['height', 'slope', 'second']:
        diff = [yf - yc for yc, yf in zip(jc[k], jf[k])]
        jet_differences[k] = {
            'common_mode_differences': diff,
            'max_absolute_common_mode_difference': max(map(abs, diff), default=0),
            'new_mode_max_absolute_value': max(map(abs, jf[k][len(jc[k]):]), default=0),
        }
    for k in ['meanSlopeCorrection', 'meanSecondCorrection']:
        jet_differences[k] = jf[k] - jc[k]
    result = {
        'scope': 'Same physical metric parameters and depth, exact complete original height vector with strictly zero added modes. These are audited finite nonlinear tails; this comparison does not establish infinite-tail closure, a continuous enclosure, or a closed-surface reach bound.',
        'normalization': 'The source normalizedFullDefect uses the current subprofile r_x. Multiply by shootingParts to compare in the original physical-profile parameter. Physical fullD, metric, curvature, and cut jets need no such correction.',
        'checks': {
            'original_physical_height_preserved_exactly': True,
            'added_height_modes_strictly_zero': True,
            'physical_constructor_fields_preserved_exactly': True,
            'common_source_hashes_equal': True,
            'common_source_file_count': len(shared_hashes),
            'steps_per_original_profile_equal': sc['steps_per_original_profile'] == sf['steps_per_original_profile'],
            'audit_steps_per_original_profile_equal': sc['audit_steps_per_original_profile'] == sf['audit_steps_per_original_profile'],
        },
        'configuration_changes': changes, 'coarse': sc, 'fine': sf,
        'fine_to_coarse_ratios': ratios, 'cut_jet_differences': jet_differences,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    with a.out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'output': str(a.out), 'checks': result['checks'],
                      'fine_to_coarse_ratios': ratios,
                      'fine_audit': sf['audit']}))


if __name__ == '__main__':
    main()
