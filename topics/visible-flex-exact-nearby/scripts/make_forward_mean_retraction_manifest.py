#!/usr/bin/env python3
"""Create exact metadata for one new forward mean retraction; no science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
REPO = 'Rogerhu12/math-research-public'
PREFIX = '2026-11-26-R144-forward-mean-retraction'
SOURCE = 'fourfold_codazzi_forward_mean_retraction.py'
WORKER = 'fourfold_codazzi_forward_mean_retraction_public_worker.py'
GENERATOR = 'make_forward_mean_retraction_manifest.py'
NATIVE = 'e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b'
CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
OLD_SOURCE = '6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93'
ORIGINALS = [
  {
    "role": "original_mean_part_0",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part000.bin.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 1993756,
    "git_blob_sha": "4ea829678abbd743217cc83fa3a20a8288eb91ec",
    "sha256": "da3519251f356cca9c0176b62d1dfe86e22eafb45f2f1e950af6af611ffe6b5c"
  },
  {
    "role": "original_mean_part_1",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part001.bin.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 1967753,
    "git_blob_sha": "74fcdc6572a9de01d420e8a4d3763bc2eef2e6ae",
    "sha256": "7a5c8486a0fa6223b39755dd3d68cefe76ecce65f274c7a0c01f447da87c88a2"
  },
  {
    "role": "original_mean_part_2",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part002.bin.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 1977063,
    "git_blob_sha": "fc6fd6abf819a43639ff1a6a6670aa6f6f19645d",
    "sha256": "0cbdaafab3c04341fb660e8469d90edb6c51bbc5d11e6791299fe40addd4d27d"
  },
  {
    "role": "original_mean_part_3",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part003.bin.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 1938002,
    "git_blob_sha": "f3a866b4fd96c58b16d3ca317d5a48801fbfee04",
    "sha256": "5755a8a5b92e248b9eb28633b3b67f112cab9494640d217f61e8f55f07907a07"
  },
  {
    "role": "original_mean_part_4",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part004.bin.gz",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "bytes": 56148,
    "git_blob_sha": "58aff428808afbf4a907be10e51f7fe5a3176993",
    "sha256": "98a3b660ad4ca691fcc70545b323f42d67b436def486a6adc5f2ed4da8d95404"
  }
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, required=True)
    ap.add_argument('--source-dir', type=Path, default=Path(__file__).resolve().parent)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    root, source_dir, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    def spec(role, relative, preferred=None):
        path = Path(preferred) if preferred is not None else root/relative
        raw = path.read_bytes()
        if not 0 < len(raw) < 100000:
            raise ValueError('complete small current input required: '+str(path))
        raw.decode('utf-8')
        if relative.endswith('.py'):
            ast.parse(raw, filename=relative)
        return dict(role=role, path=relative, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw))

    def selected(name, relative):
        p = source_dir/name
        return p if p.exists() else root/relative

    files = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('forward_mean_contract', relative, selected(contract, relative)))
    current = [
        ('reviewed_rules', 'notes/2026-11-20-reviewed-public-CI-rules.json'),
        ('mean_parts_index', 'notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json'),
        ('waist', 'notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json'),
        ('old_process', 'notes/2026-11-14-R133-final-complete-scalar-mean-process.json'),
        ('old_definition', 'scripts/fourfold_codazzi_final_scalar_mean_cached.py'),
        ('old_mean_definition_helper', 'scripts/fourfold_codazzi_final_moving_strict_energy_v2.py'),
        ('first_trace_proof', 'results/R133-supplement-actual-exact-selected-waist-data-and-original96-rows.md'),
    ]
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in current)
    by_role = {item['role']: item for item in files}
    if by_role['old_definition']['sha256'] != OLD_SOURCE:
        raise ValueError('the original native producer definition changed')
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected:
            raise ValueError('unread rule change: '+path)
    parts = json.loads((root/by_role['mean_parts_index']['path']).read_bytes())
    if (parts['original_sha256'] != NATIVE or parts['original_bytes'] != 8058137
            or parts['complete_native_rows'] != 7721 or len(parts['parts']) != 5):
        raise ValueError('same whole original scalar-mean container')
    for i, (old, part) in enumerate(zip(ORIGINALS, parts['parts'])):
        if (old['role'] != 'original_mean_part_'+str(i)
                or Path(old['path']).name != part['file']
                or old['bytes'] != part['compressed_bytes']
                or old['sha256'] != part['compressed_sha256']):
            raise ValueError('one immutable original mean container part differs')
    zeros = ('old_scientific_targets_called old_mean_Green_targets_called '
             'old_response_targets_called old_target_ODE_calls old_angular_solver_calls '
             'published_arrays').split()
    fields = ('identity complete proved failure stage expected_common_cells completed_common_cells '
              'expected_mean_interfaces completed_mean_interfaces current_exact_right '
              'complete_new_scalars strict_gates scope private_trace seconds').split()+zeros
    scalar_fields = (
        'initial_D D_at_current_right forward_multiplier_at_current_right '
        'propagated_initial_at_current_right signed_bulk_at_current_right '
        'mean_interface_at_current_right Y_lower_over_completed_cells '
        'v_difference_upper_on_positive_certified_cells D_at_R Y_at_R '
        'whole_v_difference_upper mean_shift_at_R first_unresolved_positivity_row '
        'first_certified_outside_ball_row certified_violation_witness '
        'certified_negative_Y_witness').split()
    if len(fields) != 21 or len(set(fields)) != 21 or len(set(scalar_fields)) != 16:
        raise ValueError('exact complete small new scientific schema')
    manifest = dict(kind='R144_forward_mean_retraction_inputs_v1', repository=REPO,
        problem_id='R144_raw_nu0_signed_forward_mean_retraction_v1',
        scientific_kind='R144_raw_nu0_signed_forward_mean_retraction_v1',
        files=files, expected_current_input_count=len(files), historical_inputs=ORIGINALS,
        accepted_natives=dict(mean=NATIVE, candidate=CANDIDATE, source=OLD_SOURCE),
        runtime=dict(python='3.12.14', packages={'python-flint': '0.9.0', 'numpy': '2.3.5'}),
        parameters=dict(arithmetic_bits=320, exact_alpha='6890507429876859/9007199254740992',
            exact_nu='-2572625729470897/72057594037927936',
            original_parameter_half_width='1/1000000000', exact_interval=['0', '25/8'],
            raw_nonmean_modes=32, expected_closed_cells=7721, expected_mean_interfaces=6143,
            fixed_shapes='u_raw and j_raw=v_raw/mean_phi(v_raw)',
            new_initial_Y='1', comparison_radius='1/10000',
            equation="D'=2 beta <u_raw^2> D - tau R0",
            jump_equation='D+ = D- - [n]',
            complete_native_signed_rows_used=True, original_boxes_not_cropped=True,
            all_original_mean_interfaces_retained=True,
            selected_delta_or_repair_not_inherited=True),
        allowed_scientific_fields=sorted(fields), allowed_new_scalar_fields=sorted(scalar_fields),
        zero_call_counters=zeros, expected_complete_new_scalar_field_count=16,
        scope=dict(new_target='whole signed forward mean retraction with positivity and C0 gates',
            mathematical_target_count=1, old_producer_calls=0, old_completed_targets_recomputed=0,
            old_native_read_only=True, complete_false_and_unknown_outcomes_retained=True,
            no_point_eta0_or_selected_delta_claim=True,
            no_nonmean_BVP_or_inverse_or_topic_completion=True),
        operation=dict(child_timeout_seconds=1800, readme_pull_interval_seconds=1800,
            topic_maximum_bytes=200000000, reserve_bytes=120000,
            maximum_total_publication_bytes=95000, maximum_execution_bytes=65000,
            maximum_scientific_bytes=26000,
            output_base=TOPIC+'/notes/forward_mean_retraction_ci',
            consumed_marker=TOPIC+'/notes/forward_mean_retraction_ci/R144_forward_mean_retraction_v1-consumed.json',
            automatic_scientific_retry=False, no_artifacts=True, no_Releases=True, no_new_arrays=True,
            publication='whole small signed conclusion or genuine prefix, execution, parameters and hashes'))
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = """name: R144 whole signed forward mean retraction

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-forward-mean-retraction-public.yml

permissions:
  contents: write

concurrency:
  group: r144-forward-mean-retraction-v1
  cancel-in-progress: false

jobs:
  complete-signed-forward-mean:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 60
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_forward_mean_retraction_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-26-R144-forward-mean-retraction-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Restore original mean records and enclose one whole signed forward flow
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_forward_mean_retraction_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-R144-forward-mean-retraction-inputs.json --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace('__MANIFEST_SHA__', sha(raw))
    (out/'fourfold-codazzi-forward-mean-retraction-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
        expected_current_input_count=len(files), historical_inputs=len(ORIGINALS),
        complete_scientific_fields=len(fields), new_target_count=1), sort_keys=True))


if __name__ == '__main__':
    main()
