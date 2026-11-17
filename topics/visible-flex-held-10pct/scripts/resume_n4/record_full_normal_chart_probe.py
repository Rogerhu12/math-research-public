#!/usr/bin/env python3
"""Keep compact scalar evidence for the read-only full-core chart comparison."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('result', 'checkpoint', 'resource', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    a = p.parse_args()
    row = json.loads(a.result.read_text())
    raw = a.checkpoint.read_bytes()
    cp = json.loads(gzip.decompress(raw))
    assert sha(a.checkpoint) == row['input_checkpoint_sha256']
    source = Path(row['source_root'])
    for name, expected in row['source_sha256'].items():
        if sha(source / name) != expected:
            raise ValueError('Executed dependency changed: ' + name)
    script = source / 'probe_full_core_normal_chart.py'
    assert sha(script) == row['script_sha256']
    assert sha(Path(__file__).with_name(script.name)) == row['script_sha256']
    chunks = {}
    for item in cp.get('pp_coefficient_chunks', []):
        file = a.checkpoint.parent / item['file']
        assert sha(file) == item['sha256']
        chunks[item['file']] = item['sha256']
    selected = {}
    for item in row['rows']:
        lam = str(item['homotopy'])
        name = item['chart']
        s = item['spectra']['F_psipsi_perturbation']
        selected.setdefault(lam, {})[name] = dict(
            same_solved_core=item['same_solved_core'],
            actual_solved_chart=item['solved_chart'],
            second_reference_jet_fft_l1_above_81=s['20'],
            second_reference_jet_fft_l1_above_97=s['24'],
            minimum_sampled_du=item['minimum_sampled_du'],
            normal_chain_identity=item.get('direct_normal_chain_identity'),
            normal_arc_inverse_error=item.get('normal_arc_inverse_error'))
    ratios = {}
    for lam, item in selected.items():
        ratios[lam] = (
            item['frozen_full_normal']['second_reference_jet_fft_l1_above_81'] /
            item['original_bimodal']['second_reference_jet_fft_l1_above_81'])
    resource = json.loads(a.resource.read_text())
    assert resource['status'] == 'observed_terminal' and resource['child_returncode'] == 0
    result = dict(
        scope='Read-only numerical coordinate comparison at the identical complete core. The full normal-angle chart worsens the sampled M20 second-jet tail for this input; this is not a BVP failure or a claim about every possible chart. Lambda one uses the same physical controls as an unsolved endpoint candidate.',
        collector_sha256=sha(__file__), result_sha256=sha(a.result),
        resource_sha256=sha(a.resource), executed_script=str(script),
        executed_script_sha256=row['script_sha256'],
        executed_source_root=str(source), source_sha256=row['source_sha256'],
        input_checkpoint_sha256=sha(a.checkpoint), input_chunk_hashes=chunks,
        actual_q=row['actual_q'], gauge_q=row['gauge_q'], controls=row['controls'],
        physical_control_sha256=row['physical_control_sha256'],
        physical_profile=row['physical_profile'], settings=row['settings'],
        samples=row['samples'], original_chart_warp_e=row['original_chart_warp_e'],
        scalar_comparison=selected, normal_to_original_M20_ratios=ratios,
        spatial_chart_inherited_rho_guard_lower={
            str(item['homotopy']): item['analytic_continuous_du_lower']
            for item in row['spatial_chain']},
        terminal_seconds=resource['seconds'], child_returncode=0,
        scope_of_chain_test='Normal geometric derivatives and material-chain derivatives agree at sampled angles. The exact mathematical inequality is theta_psi >= min(1,inf rho_core) for 0<=c<=1; the two reported instance numbers come only from the original numerical core rho guard/allowance. This probe adds no strict continuous transcendental interval certificate. C2 identity at the cut follows from the original fade polynomial.',
        executed_probe_field_scope='The executed source key analytic_continuous_du_lower is preserved in the scratch result and hash; it is interpreted here only as an inherited numerical rho guard, not a new unconditional continuous certificate.',
        data_policy='Full spectral arrays, fields and regenerable multi-cutoff table remain scratch-only; selected scalar comparisons and hashes suffice to replay this decision.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
