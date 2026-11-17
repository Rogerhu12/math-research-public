#!/usr/bin/env python3
"""Keep selected actual-control n4 primary-width comparisons and source hashes."""
import argparse
import hashlib
import json
from pathlib import Path
import shlex


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('probe', 'resource', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    raw = json.loads(args.probe.read_text())
    resource = json.loads(args.resource.read_text())
    rows = raw.pop('rows')
    source_root = Path(raw['command'][0]).resolve().parent
    raw['executed_source_root'] = str(source_root)
    raw['executed_source_full_paths'] = {}
    for name, digest in raw['source_sha256'].items():
        file = source_root / name
        if sha(file) != digest:
            raise ValueError('Executed source identity changed: ' + str(file))
        raw['executed_source_full_paths'][str(file)] = digest
    raw['actual_command'] = shlex.join(raw.pop('command'))
    resource['actual_command'] = shlex.join(resource.pop('command'))
    selected = {}
    for lam, width, name in ((.02, .08, 'lambda002_original_width'),
                             (.02, .16, 'lambda002_selected_new_width'),
                             (1., .08, 'circle_candidate_original_width'),
                             (1., .24, 'circle_candidate_wider_primary')):
        row = next(r for r in rows if r['homotopy'] == lam and r['primary_transition'] == width)
        assert row['success']
        selected[name] = {key: row[key] for key in
                          ('primary_transition', 'homotopy', 'is_accepted_checkpoint_core',
                           'flatten_beta', 'rho_guard_lower', 'rho_sampled_min',
                           'circle_radius_at_lambda_one', 'arc_rho_defect',
                           'arc_center_variation', 'center_norm_sample',
                           'original_core_difference', 'complete_lift_reconstruction')}
        selected[name].update(
            actual_psi_Fpsipsi_fft_l1_above_81=row['actual_chart_spectrum']['F_psipsi_perturbation']['20'],
            actual_psi_Fpsipsi_fft_l1_above_97=row['actual_chart_spectrum']['F_psipsi_perturbation']['24'],
            material_Fuu_fft_l1_above_81=row['material_spectrum']['F_uu']['20'],
            reference_lift_Fpsipsi_max=row['unrepresented_reference_jet_max']['F_psipsi'])
    assert selected['lambda002_original_width']['original_core_difference'] == 0
    old, new = selected['lambda002_original_width'], selected['lambda002_selected_new_width']
    result = dict(
        scope='Read-only width selection using all nineteen actual n4 controls and the actual frozen bimodal chart. Changed designs are unsolved. Complete exact-lift jets are retained, not discarded at the finite Fourier cutoff.',
        collector_sha256=sha(__file__), provenance=raw, resource=resource,
        selected_diagnostics=selected,
        selection_rule='Choose the smallest sampled actual-psi second-jet tail above the M20 vector cutoff at the original lambda=.02, among four tested primary widths.',
        selected_width=.16, full_probe_rows=len(rows),
        original_to_selected_tail_ratio=new['actual_psi_Fpsipsi_fft_l1_above_81'] / old['actual_psi_Fpsipsi_fft_l1_above_81'],
        original_to_selected_reference_jet_ratio=new['reference_lift_Fpsipsi_max'] / old['reference_lift_Fpsipsi_max'],
        raw_probe_sha256=sha(args.probe), resource_sha256=sha(args.resource),
        data_policy='Only four selected scalar comparisons and source/input/output hashes. All sampled fields and the full regenerated eight-case table remain scratch-only.',
        geometry_limit='The optional 2*c*sin(a) quantity in the raw scratch probe is a maximal-phase scale only. No common-H budget, actual held displacement, closed diameter, reach or non-Euclidean witness is asserted.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
