#!/usr/bin/env python3
"""Create exact metadata for the new localized state/source target; no science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PREFIX = '2026-11-26-R144-localized-full-state-and-compact-sources'
SOURCE = 'fourfold_codazzi_localized_full_state_and_compact_sources.py'
WORKER = 'fourfold_codazzi_localized_full_state_and_compact_sources_public_worker.py'
GENERATOR = 'make_localized_full_state_compact_sources_manifest.py'

STATIC = json.loads(r'''{"kind":"R144_localized_full_state_compact_sources_inputs_v1","repository":"Rogerhu12/math-research-public","problem_id":"R144_raw_nu0_localized_full_state_C0_and_compact_sources_v1","scientific_kind":"R144_raw_nu0_localized_full_state_C0_and_compact_sources_v1","historical_inputs":[{"role":"original_mean_part_0","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part000.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1993756,"git_blob_sha":"4ea829678abbd743217cc83fa3a20a8288eb91ec","sha256":"da3519251f356cca9c0176b62d1dfe86e22eafb45f2f1e950af6af611ffe6b5c"},{"role":"original_mean_part_1","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part001.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1967753,"git_blob_sha":"74fcdc6572a9de01d420e8a4d3763bc2eef2e6ae","sha256":"7a5c8486a0fa6223b39755dd3d68cefe76ecce65f274c7a0c01f447da87c88a2"},{"role":"original_mean_part_2","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part002.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1977063,"git_blob_sha":"fc6fd6abf819a43639ff1a6a6670aa6f6f19645d","sha256":"0cbdaafab3c04341fb660e8469d90edb6c51bbc5d11e6791299fe40addd4d27d"},{"role":"original_mean_part_3","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part003.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":1938002,"git_blob_sha":"f3a866b4fd96c58b16d3ca317d5a48801fbfee04","sha256":"5755a8a5b92e248b9eb28633b3b67f112cab9494640d217f61e8f55f07907a07"},{"role":"original_mean_part_4","path":"topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts-part004.bin.gz","commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","bytes":56148,"git_blob_sha":"58aff428808afbf4a907be10e51f7fe5a3176993","sha256":"98a3b660ad4ca691fcc70545b323f42d67b436def486a6adc5f2ed4da8d95404"},{"bytes":2738500,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"634c08e6d18ed7d16308881b378cc5a9420be3a4","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part000.npz.gz","role":"original_candidate_part_0","sha256":"5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4"},{"bytes":2738003,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"ed630e376a1e91b19e34ac8be8080161a15f6200","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part001.npz.gz","role":"original_candidate_part_1","sha256":"3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106"},{"bytes":2738686,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"5cc4d26fb15282ec922057eead9d6728e2a2b0cc","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part002.npz.gz","role":"original_candidate_part_2","sha256":"a317c6f491295d8e46aa5d4b3da84c1f26bd16d5fb65260f3d3459e1f9c6210e"},{"bytes":2732843,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"7a4ce33c8adf353574c34085e2cd8713245f59d3","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part003.npz.gz","role":"original_candidate_part_3","sha256":"7b67e5a4b11ae45476d1507e842ae23919ca44e4ed2d64bc81bdea78e0b4007c"},{"bytes":1532492,"commit":"46f127c7153f5393dcd2a00f42d4c1d3662c294d","git_blob_sha":"7c9414280441e5831fa4507fab8707043511c57a","path":"topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part004.npz.gz","role":"original_candidate_part_4","sha256":"314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c"}],"accepted_natives":{"mean":"e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b","candidate":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","source":"6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93"},"runtime":{"python":"3.12.14","packages":{"python-flint":"0.9.0","numpy":"2.3.5"}},"parameters":{"arithmetic_bits":320,"exact_alpha":"6890507429876859/9007199254740992","exact_nu":"-2572625729470897/72057594037927936","exact_eta":"-7789843107295549/4611686018427387904","original_parameter_half_width":"1/1000000000","exact_interval":["0","25/8"],"compact_interval":["1/20","9/50"],"raw_nonmean_modes":32,"original_candidate_pieces":6144,"expected_closed_cells":7721,"expected_mean_interfaces":6143,"expected_compact_cells":1156,"geometry_norm":"max component complete physical unnormalized C0_r_phi at the same moving angle","actual_radii_source":"TM run45791979634/1 complete exact_parameters rho,b","compact_profile":"chi=4096 t^6 (1-t)^6 on [1/20,9/50]","all_old_means_and_jump_sums_read_only":true,"exact_intrinsic_box_centre_only":true,"physical_theta_grid_required":false},"allowed_scientific_fields":["complete","complete_new_scalars","completed_common_cells","completed_compact_cells","completed_mean_interfaces","current_candidate_piece","current_exact_right","exact_parameters","expected_common_cells","expected_mean_interfaces","failure","finite_coefficient_rows_evaluated","forward_W_targets_called","identity","old_compact_moment_calls","old_mean_Green_or_Gamma_calls","old_residual_target_calls","old_scientific_targets_recomputed","physical_theta_grid_calls","primitive_or_DFT_calls","private_trace","proved","published_arrays","radial_ODE_calls","saved_readback_count","scalar_scope","scope","seconds","stage","strict_gates","terminal_mean_gate_targets_called"],"allowed_new_scalar_fields":["Fu_complete_L2_upper","Fv_complete_L2_upper","Qu_complete_L2_upper","Qv_complete_L2_upper","anisotropic_Hminus2over3_Hminus1_pair_upper","cosine_nonmean_A0_upper","cv_operator_upper","density_A0_upper","first_row_Hminus2over3_upper","fu_L2_upper","fu_squared_integral_upper","fv_chi_L2_upper","fv_chi_squared_integral_upper","isotropic_Hminus2over3_pair_upper","new_complete_v_jump_A0_upper","qu_L2_upper","qu_squared_integral_upper","qv_L2_upper","qv_squared_integral_upper","same_phi_C0_upper","second_row_Hminus1_upper","second_row_Hminus2over3_upper","sine_A0_upper","unchanged_raw_Ru_L2_upper","unchanged_raw_Rv_L2_upper","unchanged_raw_u_jump_A0_upper","unchanged_raw_v_jump_A0_upper"],"prefix_state_scalar_fields":["same_phi_C0_upper","sine_A0_upper","cosine_nonmean_A0_upper","density_A0_upper","fu_squared_integral_upper","qu_squared_integral_upper","fv_chi_squared_integral_upper","qv_squared_integral_upper","cv_operator_upper"],"zero_call_counters":["old_scientific_targets_recomputed","old_mean_Green_or_Gamma_calls","old_residual_target_calls","old_compact_moment_calls","terminal_mean_gate_targets_called","radial_ODE_calls","primitive_or_DFT_calls","forward_W_targets_called","physical_theta_grid_calls","published_arrays"],"expected_complete_new_scalar_field_count":27,"scope":{"new_target":"localized unnormalized same-phi full-state C0 and complete compact ordinary/flux source receivers","mathematical_target_count":1,"old_producer_calls":0,"old_completed_targets_recomputed":0,"old_native_read_only":true,"complete_false_and_unknown_outcomes_retained":true,"actual_complete_TM_radii_required":true,"partial_prefix_is_not_whole_upper":true,"no_physical_theta_grid_target":true,"no_nonmean_BVP_or_inverse_or_topic_completion":true},"operation":{"child_timeout_seconds":3600,"readme_pull_interval_seconds":1800,"topic_maximum_bytes":200000000,"reserve_bytes":120000,"maximum_total_publication_bytes":95000,"maximum_execution_bytes":65000,"maximum_scientific_bytes":26000,"output_base":"topics/visible-flex-exact-nearby/notes/localized_full_state_compact_sources_ci","consumed_marker":"topics/visible-flex-exact-nearby/notes/localized_full_state_compact_sources_ci/R144_localized_full_state_compact_sources_v1-consumed.json","automatic_scientific_retry":false,"no_artifacts":true,"no_Releases":true,"no_new_arrays":true,"publication":"whole small new scalar bounds or genuine accepted row prefix, execution, parameters and hashes"}}''')
CURRENT = json.loads(r'''[["reviewed_rules","notes/2026-11-20-reviewed-public-CI-rules.json"],["mean_parts_index","notes/2026-11-14-R133-final-complete-scalar-mean-native-binary-parts.json"],["old_process","notes/2026-11-14-R133-final-complete-scalar-mean-process.json"],["candidate_index","data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json"],["tm_result","notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/terminal-mean-small-scalar-gate.json"],["tm_execution","notes/terminal_mean_small_scalar_gate_ci/run-45791979634-1/execution.json"],["c0_result","notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json"],["c0_execution","notes/compact_mean_c0_receivers_ci/run-45787608966-1/execution.json"],["raw_bounds","notes/2026-11-14-R133-final-complete-moving-residual.md"],["source_proof","results/R144-supplement-compact-centre-ordinary-and-divergence-residual.md"],["localized_proof","results/R144-supplement-localized-full-state-C0-and-compact-source-receivers.md"],["geometry_proof","results/R133-supplement-complete-C0-state-and-nu-geometry-response.md"],["old_definition","scripts/fourfold_codazzi_final_scalar_mean_cached.py"],["old_mean_definition_helper","scripts/fourfold_codazzi_final_moving_strict_energy_v2.py"],["object","data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"]]''')
ACCEPTED_CURRENT_SHA = json.loads(r'''{"reviewed_rules":"26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051","mean_parts_index":"d405693083532a2e7c8962b0e715a24169f56b8badabd525275f1f75336b76db","old_process":"444efc6e1bc8d9ef5ccc8d02367c1ffd5211b30ddf0b7cbf2db592d05a342e76","candidate_index":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","tm_result":"a74d11052da41570a7588d5a79545cfb7295ccf437b3bae971390d59f2b99de6","tm_execution":"af0b8f547c4e4215bbfcd42f7e0546391ec247765c3a94c9634c3950acd5fe34","c0_result":"0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641","c0_execution":"9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc","raw_bounds":"84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e","source_proof":"72252cbf0e2972e4f2248ce6711a0274c3d9a1b134b2aad276ccdb0304177d11","localized_proof":"16ed825fea674e2239c8e727c294cce2a396e5edf7064cc422f4ccef3652b471","geometry_proof":"366914bfb1ad8acfba99fe77c4a37237957ed6a777eef01072a039370525f2fe","old_definition":"6edd8abf820c4e11a25b496c08d0585fb7c943397e7f919ed3774a0b841b0d93","old_mean_definition_helper":"c6baae3e8448b4ceec95eeed50a38e8761207b1ca622173c1a8bccce3245b526","object":"91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"}''')
WORKFLOW = r'''name: R144 localized full-state norm and compact sources

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-localized-full-state-and-compact-sources-public.yml

permissions:
  contents: write

concurrency:
  group: r144-localized-full-state-compact-sources-v1
  cancel-in-progress: false

jobs:
  complete-localized-state-and-source-receivers:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 90
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_localized_full_state_and_compact_sources_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-26-R144-localized-full-state-and-compact-sources-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Read proved mean radii and compute localized state and source bounds
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_localized_full_state_and_compact_sources_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-R144-localized-full-state-and-compact-sources-inputs.json --manifest-sha __MANIFEST_SHA__
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
        local = source_dir/name
        return local if local.exists() else root/relative

    files = []
    for role, name in (('worker', WORKER), ('science', SOURCE), ('metadata_generator', GENERATOR)):
        relative = TOPIC+'/scripts/'+name
        path = Path(__file__) if role == 'metadata_generator' else selected(name, relative)
        files.append(spec(role, relative, path))
    contract = PREFIX+'-contract.md'
    relative = TOPIC+'/notes/'+contract
    files.append(spec('localized_source_contract', relative, selected(contract, relative)))
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in CURRENT)
    by_role = {x['role']: x for x in files}
    if len(files) != 19 or len(by_role) != 19:
        raise ValueError('exact complete current input closure')
    for role, expected in ACCEPTED_CURRENT_SHA.items():
        if by_role[role]['sha256'] != expected:
            raise ValueError('complete accepted original or actual input changed: '+role)
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected:
            raise ValueError('unread rule change: '+path)
    parts = json.loads((root/by_role['mean_parts_index']['path']).read_bytes())
    if (parts['original_sha256'] != STATIC['accepted_natives']['mean']
            or parts['original_bytes'] != 8058137 or parts['complete_native_rows'] != 7721
            or len(parts['parts']) != 5):
        raise ValueError('same complete original mean container')
    for i, (old, part) in enumerate(zip(STATIC['historical_inputs'][:5], parts['parts'])):
        if (old['role'] != 'original_mean_part_'+str(i)
                or Path(old['path']).name != part['file']
                or old['bytes'] != part['compressed_bytes']
                or old['sha256'] != part['compressed_sha256']):
            raise ValueError('immutable original mean part differs')
    index = json.loads((root/by_role['candidate_index']['path']).read_bytes())
    if (index['kind'] != 'complete_lossless_radial_cubic_shards_v1'
            or index['coefficient_shape'] != [4, 6144, 65] or len(index['parts']) != 5):
        raise ValueError('same complete original finite candidate definition')
    next_interval = 0
    for i, (old, part) in enumerate(zip(STATIC['historical_inputs'][5:], index['parts'])):
        if (old['role'] != 'original_candidate_part_'+str(i)
                or Path(old['path']).name != part['file']
                or old['bytes'] != part['bytes'] or old['sha256'] != part['sha256']
                or part['first_interval'] != next_interval):
            raise ValueError('immutable original cubic candidate shard differs')
        next_interval = part['last_interval_exclusive']
    if next_interval != 6144:
        raise ValueError('complete exact candidate radial coverage')
    tm = json.loads((root/by_role['tm_result']['path']).read_bytes())
    c0 = json.loads((root/by_role['c0_result']['path']).read_bytes())
    if (tm['complete'] is not True or tm['proved'] is not True
            or tm['scope']['passed_scalar_mean_root'] is not True
            or c0['complete'] is not True or c0['proved'] is not True
            or c0['completed_compact_cells'] != STATIC['parameters']['expected_compact_cells']):
        raise ValueError('actual complete prior objects; no hypothetical future input')
    manifest = dict(STATIC, files=files, expected_current_input_count=len(files))
    if (len(manifest['allowed_scientific_fields']) != 31
            or len(manifest['allowed_new_scalar_fields']) != 27
            or len(manifest['historical_inputs']) != 10):
        raise ValueError('exact complete science schema and original input set')
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    if len(raw) >= 100000:
        raise ValueError('complete small input manifest required')
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    workflow = WORKFLOW.replace('__MANIFEST_SHA__', sha(raw))
    (out/'fourfold-codazzi-localized-full-state-and-compact-sources-public.yml').write_text(workflow)
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
        current_inputs=len(files), historical_inputs=10, complete_scientific_fields=31,
        new_scalar_fields=27, mathematical_target_count=1), sort_keys=True))


if __name__ == '__main__':
    main()
