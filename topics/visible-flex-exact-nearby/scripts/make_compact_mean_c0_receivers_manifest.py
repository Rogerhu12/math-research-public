#!/usr/bin/env python3
"""Create complete metadata for new compact moments and C0 receivers; no science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PREFIX = '2026-11-26-R144-compact-mean-c0-receivers'
SOURCE = 'fourfold_codazzi_compact_mean_c0_receivers.py'
WORKER = 'fourfold_codazzi_compact_mean_c0_receivers_public_worker.py'
GENERATOR = 'make_compact_mean_c0_receivers_manifest.py'

STATIC = json.loads(r'''{"kind":"R144_compact_mean_c0_receivers_inputs_v1","repository":"Rogerhu12/math-research-public","problem_id":"R144_raw_nu0_compact_moments_complete_C0_receivers_v1","scientific_kind":"R144_raw_nu0_compact_moments_complete_C0_receivers_v1","historical_inputs":[{"role":"original_mean_part_0","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part000.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1993756,"git_blob_sha":"4ea829678abbd743217cc83fa3a20a8288eb91ec","sha256":"da3519251f356cca9c0176b62d1dfe86e22eafb45f2f1e950af6af611ffe6b5c"},{"role":"original_mean_part_1","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part001.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1967753,"git_blob_sha":"74fcdc6572a9de01d420e8a4d3763bc2eef2e6ae","sha256":"7a5c8486a0fa6223b39755dd3d68cefe76ecce65f274c7a0c01f447da87c88a2"},{"role":"original_mean_part_2","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part002.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1977063,"git_blob_sha":"fc6fd6abf819a43639ff1a6a6670aa6f6f19645d","sha256":"0cbdaafab3c04341fb660e8469d90edb6c51bbc5d11e6791299fe40addd4d27d"},{"role":"original_mean_part_3","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part003.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1938002,"git_blob_sha":"f3a866b4fd96c58b16d3ca317d5a48801fbfee04","sha256":"5755a8a5b92e248b9eb28633b3b67f112cab9494640d217f61e8f55f07907a07"},{"role":"original_mean_part_4","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part004.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":56148,"git_blob_sha":"58aff428808afbf4a907be10e51f7fe5a3176993","sha256":"98a3b660ad4ca691fcc70545b323f42d67b436def486a6adc5f2ed4da8d95404"}],"accepted_natives":{"mean":"e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b","candidate":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","source":"6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93"},"runtime":{"python":"3.12.14","packages":{"python-flint":"0.9.0","numpy":"2.3.5"}},"parameters":{"arithmetic_bits":320,"exact_alpha":"6890507429876859/9007199254740992","exact_nu":"-2572625729470897/72057594037927936","exact_eta":"-7789843107295549/4611686018427387904","original_parameter_half_width":"1/1000000000","exact_interval":["0","25/8"],"compact_interval":["1/20","9/50"],"raw_nonmean_modes":32,"expected_closed_cells":7721,"expected_mean_interfaces":6143,"expected_new_reverse_cells":7721,"profile_kernel_indices":["01","02","10","11","12","20","21","22","30","31","32"],"saved_old_scalar_reads":4,"normalized_moments":["abar=-A_R/H_R","bbar=-B_R/H_R"],"H_prefix_equation":"H'=2 beta U H; H(0)=1","compact_profile":"chi=4096 t^6 (1-t)^6 on [1/20,9/50]","old_Gamma_and_row_maxima_read_only":true,"actual_forward_endpoint_required":false},"allowed_scientific_fields":["complete","complete_new_scalars","completed_common_cells","completed_compact_cells","completed_mean_interfaces","completed_prefix_cells","completed_weighted_reverse_cells","current_H_exact_right","current_exact_right","expected_common_cells","expected_mean_interfaces","failure","forward_W_targets_called","identity","old_Gamma_or_old_row_maxima_recomputed","old_angular_solver_calls","old_mean_Green_targets_called","old_residual_targets_called","old_saved_scalar_reads","old_scientific_targets_called","old_target_ODE_calls","primitive_or_DFT_calls","private_trace","proved","published_arrays","scalar_scope","scope","seconds","stage","strict_gates","weighted_next_original_row"],"allowed_new_scalar_fields":["C01_profile_kernel_upper","C02_profile_kernel_upper","C10_profile_kernel_upper","C11_profile_kernel_upper","C12_profile_kernel_upper","C20_profile_kernel_upper","C21_profile_kernel_upper","C22_profile_kernel_upper","C30_profile_kernel_upper","C31_profile_kernel_upper","C32_profile_kernel_upper","H_at_compact_right","K0_ordinary_mean_C0_upper","K1_full_nonmean_C0_upper","K2_nonlinear_C0_upper","KJ_all_common_jumps_C0_upper","K_betaK_weighted_ordinary_C0_upper","abar","bbar","beta_K_abs_upper","density_variance_ratio_sqrt_upper","kernel_01_maximum_before_Gamma","kernel_01_suffix","kernel_02_maximum_before_Gamma","kernel_02_suffix","kernel_10_maximum_before_Gamma","kernel_10_suffix","kernel_11_maximum_before_Gamma","kernel_11_suffix","kernel_12_maximum_before_Gamma","kernel_12_suffix","kernel_20_maximum_before_Gamma","kernel_20_suffix","kernel_21_maximum_before_Gamma","kernel_21_suffix","kernel_22_maximum_before_Gamma","kernel_22_suffix","kernel_30_maximum_before_Gamma","kernel_30_suffix","kernel_31_maximum_before_Gamma","kernel_31_suffix","kernel_32_maximum_before_Gamma","kernel_32_suffix","mean_abs_lower","mean_abs_upper","prefix_inverse_tau_max","raw_mean_jump_sum_upper","raw_mean_residual_upper","raw_v_gap_lower","variance_upper","weighted_maximum_before_Gamma","weighted_suffix_before_Gamma"],"zero_call_counters":["old_scientific_targets_called","old_mean_Green_targets_called","old_Gamma_or_old_row_maxima_recomputed","old_residual_targets_called","old_target_ODE_calls","old_angular_solver_calls","primitive_or_DFT_calls","forward_W_targets_called","published_arrays"],"expected_complete_new_scalar_field_count":52,"scope":{"new_target":"normalized compact positive moments and complete C0 mean receivers including eleven profile weights","mathematical_target_count":1,"old_producer_calls":0,"old_completed_targets_recomputed":0,"old_native_read_only":true,"complete_false_and_unknown_outcomes_retained":true,"original_affine_box_only_encloses_its_fixed_centre":true,"partial_zero_state_is_not_whole_upper":true,"no_forward_endpoint_or_selected_delta_claim":true,"no_nonmean_BVP_or_inverse_or_topic_completion":true},"operation":{"child_timeout_seconds":1800,"readme_pull_interval_seconds":1800,"topic_maximum_bytes":200000000,"reserve_bytes":120000,"maximum_total_publication_bytes":95000,"maximum_execution_bytes":65000,"maximum_scientific_bytes":26000,"output_base":"topics/visible-flex-exact-nearby/notes/compact_mean_c0_receivers_ci","consumed_marker":"topics/visible-flex-exact-nearby/notes/compact_mean_c0_receivers_ci/R144_compact_mean_c0_receivers_v1-consumed.json","automatic_scientific_retry":false,"no_artifacts":true,"no_Releases":true,"no_new_arrays":true,"publication":"whole small new scalar conclusion or genuine accepted prefix, execution, parameters and hashes"}}''')
CURRENT = json.loads(r'''[["reviewed_rules","notes/2026-11-20-reviewed-public-CI-rules.json"],["mean_parts_index","notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json"],["old_process","notes/2026-11-14-R133-final-complete-scalar-mean-process.json"],["old_readable","notes/2026-11-14-R133-final-complete-scalar-mean-readable-bounds.json"],["raw_bounds","notes/2026-11-14-R133-final-complete-moving-residual.md"],["strict_proof","results/R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md"],["receiver_proof","results/R144-supplement-complete-C0-mean-receiver-and-compact-moments.md"],["kernel_proof","results/R144-supplement-profile-weighted-mean-feedback-polynomial.md"],["old_definition","scripts/fourfold_codazzi_final_scalar_mean_cached.py"],["old_mean_definition_helper","scripts/fourfold_codazzi_final_moving_strict_energy_v2.py"],["object","data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"]]''')
WORKFLOW = r'''name: R144 compact moments and complete C0 mean receivers

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-compact-mean-c0-receivers-public.yml

permissions:
  contents: write

concurrency:
  group: r144-compact-mean-c0-receivers-v1
  cancel-in-progress: false

jobs:
  complete-compact-moments-and-c0-receivers:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_compact_mean_c0_receivers_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-26-R144-compact-mean-c0-receivers-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Read old records and compute new compact moments and C0 kernels
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_compact_mean_c0_receivers_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-R144-compact-mean-c0-receivers-inputs.json --manifest-sha __MANIFEST_SHA__
'''

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
        path = source_dir/name
        return path if path.exists() else root/relative

    files = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('compact_mean_contract', relative, selected(contract, relative)))
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in CURRENT)
    by_role = {x['role']: x for x in files}
    if len(files) != 15 or len(by_role) != 15:
        raise ValueError('exact complete current input closure')
    if by_role['old_definition']['sha256'] != STATIC['accepted_natives']['source']:
        raise ValueError('old defining producer changed')
    if by_role['receiver_proof']['sha256'] != '1f55171ae49a3cda07f44c2bc073a41887a7169c9fe210774a373f22599fe81f':
        raise ValueError('complete audited C0 receiver proof changed')
    if by_role['kernel_proof']['sha256'] != 'c9b2469ce02c5553aceee6401a3cc388607aa7ea83d661759aa79078aef797a1':
        raise ValueError('complete audited eleven-profile proof changed')
    if by_role['object']['sha256'] != '91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848':
        raise ValueError('actual original affine object changed')
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected:
            raise ValueError('unread rule change: '+path)
    parts = json.loads((root/by_role['mean_parts_index']['path']).read_bytes())
    if (parts['original_sha256'] != STATIC['accepted_natives']['mean']
            or parts['original_bytes'] != 8058137 or parts['complete_native_rows'] != 7721
            or len(parts['parts']) != 5):
        raise ValueError('same complete original mean native')
    for i, (old, part) in enumerate(zip(STATIC['historical_inputs'], parts['parts'])):
        if (old['role'] != 'original_mean_part_'+str(i)
                or Path(old['path']).name != part['file']
                or old['bytes'] != part['compressed_bytes']
                or old['sha256'] != part['compressed_sha256']):
            raise ValueError('immutable original container part differs')
    manifest = dict(STATIC, files=files, expected_current_input_count=len(files))
    if len(manifest['allowed_scientific_fields']) != 31 or len(manifest['allowed_new_scalar_fields']) != 52:
        raise ValueError('exact complete science schema')
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small input manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = WORKFLOW.replace('__MANIFEST_SHA__', sha(raw))
    (out/'fourfold-codazzi-compact-mean-c0-receivers-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
                         current_inputs=len(files), historical_inputs=5,
                         complete_scientific_fields=31, new_scalar_fields=52,
                         mathematical_target_count=1), sort_keys=True))


if __name__ == '__main__':
    main()
