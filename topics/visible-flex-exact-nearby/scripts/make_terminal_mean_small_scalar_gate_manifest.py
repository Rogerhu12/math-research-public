#!/usr/bin/env python3
"""Complete metadata for one new terminal/root scalar gate; no science."""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PREFIX = '2026-11-26-R144-terminal-mean-small-scalar-gate'
SOURCE = 'fourfold_codazzi_terminal_mean_small_scalar_gate.py'
WORKER = 'fourfold_codazzi_terminal_mean_small_scalar_gate_public_worker.py'
GENERATOR = 'make_terminal_mean_small_scalar_gate_manifest.py'

STATIC = json.loads(r'''{"kind":"R144_terminal_mean_small_scalar_gate_inputs_v1","repository":"Rogerhu12/math-research-public","problem_id":"R144_terminal_mean_small_scalar_root_gate_v1","scientific_kind":"R144_terminal_mean_small_scalar_root_gate_v1","historical_inputs":[],"runtime":{"python":"3.12.14","packages":{"python-flint":"0.9.0","numpy":"2.3.5"}},"parameters":{"arithmetic_bits":320,"exact_alpha":"6890507429876859/9007199254740992","exact_nu":"-2572625729470897/72057594037927936","exact_eta":"-7789843107295549/4611686018427387904","exact_interval":["0","25/8"],"original_candidate_sha256":"ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413","original_mean_native_sha256":"e233ece0f264eb73f93dfe5b43c5d45b4d5d6db06da2418b9c20fb545a01889b","old_waist_source_field":"complete_waist_mean_gain_if_log_Gamma_below_100/ordinary_mean_source_L2_r","old_initial_field":"complete_new_scalars.initial_D","complete_c0_scalar_input_count":52,"proposal_factor":"17/16","proposal_convention":"exact Fraction of complete saved (midpoint_integer+radius_integer)*10^decimal_exponent","dependent_scalar_actual_readback":true,"actual_future_forward_endpoint_required":false,"scientific_stage_count":5},"allowed_scientific_fields":["complete","complete_new_scalars","completed_scalar_stages","exact_parameters","failure","forward_W_targets_called","identity","native_rows_scanned","old_scientific_targets_recomputed","primitive_or_DFT_calls","proved","published_arrays","radial_ODE_calls","saved_readback_count","scope","seconds","stage","strict_gates","unproved_gate"],"allowed_new_scalar_fields":["E_ordinary_and_mean_jumps_upper","absolute_saved_initial_D_upper","b0_proposal_upper","b_proposal_upper","density_numerator_change_upper","normalized_forward_constant_absolute_upper","physical_raw_Rv_L2_upper","profile_A0_upper","profile_A1_upper","profile_A2_upper","profile_A3_upper","rho_proposal_upper","root_margin_rhs_lower","same_phi_moving_C0_upper","terminal_waist_from_L2_upper","terminal_waist_relative_shift_upper","terminal_waist_shift_upper","uniform_Lipschitz_upper","uniform_selfmap_upper","zero_parameter_Lipschitz_upper","zero_parameter_selfmap_upper"],"required_gate_fields":["zero_parameter_contraction_gap","zero_parameter_ball","zero_parameter_Lipschitz","zero_parameter_mean_negative","waist_relative_shift_below_one","root_radius_in_unit_interval","unique_compact_root","uniform_contraction_gap","uniform_mean_ball","uniform_mean_Lipschitz","uniform_mean_negative","density_positive","same_phi_moving_C0_sufficient_1e4"],"zero_call_counters":["old_scientific_targets_recomputed","native_rows_scanned","radial_ODE_calls","primitive_or_DFT_calls","forward_W_targets_called","published_arrays"],"scope":{"new_target":"terminal mean ball and waist bound imply compact root and uniform mean-density certificate","mathematical_target_count":1,"native_scans":0,"old_targets_recomputed":0,"failed_sufficient_gate_is_not_nonexistence":true,"independent_same_phi_norm_is_not_physical_angle_C0":true,"no_old_selected_inverse_or_topic_completion":true},"operation":{"child_timeout_seconds":1800,"readme_pull_interval_seconds":1800,"topic_maximum_bytes":200000000,"reserve_bytes":120000,"maximum_total_publication_bytes":95000,"maximum_execution_bytes":65000,"maximum_scientific_bytes":26000,"output_base":"topics/visible-flex-exact-nearby/notes/terminal_mean_small_scalar_gate_ci","consumed_marker":"topics/visible-flex-exact-nearby/notes/terminal_mean_small_scalar_gate_ci/R144_terminal_mean_small_scalar_gate_v1-consumed.json","automatic_scientific_retry":false,"no_artifacts":true,"no_Releases":true,"no_new_arrays":true,"publication":"whole small scalar gates, exact rational radii, complete actual input/run metadata, or genuine saved prefix"}}''')
CURRENT = json.loads(r'''[["reviewed_rules","notes/2026-11-20-reviewed-public-CI-rules.json"],["c0_result","notes/compact_mean_c0_receivers_ci/run-45787608966-1/compact-mean-c0-receivers.json"],["c0_execution","notes/compact_mean_c0_receivers_ci/run-45787608966-1/execution.json"],["initial_result","notes/forward_mean_retraction_ci/run-45772466407-1/forward-mean-retraction.json"],["old_readable","notes/2026-11-14-R133-final-complete-scalar-mean-readable-bounds.json"],["raw_bounds","notes/2026-11-14-R133-final-complete-moving-residual.md"],["proof","results/R144-supplement-terminal-mean-small-ball-controls-normalized-forward-constant.md"]]''')
WORKFLOW = r'''name: R144 terminal mean and compact root from complete scalars

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-terminal-mean-small-scalar-gate-public.yml

permissions:
  contents: write

concurrency:
  group: r144-terminal-mean-small-scalar-gate-v1
  cancel-in-progress: false

jobs:
  complete-terminal-mean-small-scalar-gate:
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_terminal_mean_small_scalar_gate_public_worker.py
            topics/visible-flex-exact-nearby/notes/2026-11-26-R144-terminal-mean-small-scalar-gate-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0 numpy==2.3.5
      - name: Read complete scalars and certify terminal mean and compact root
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: "1"
          OMP_NUM_THREADS: "1"
          MKL_NUM_THREADS: "1"
          NUMEXPR_NUM_THREADS: "1"
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_terminal_mean_small_scalar_gate_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest topics/visible-flex-exact-nearby/notes/2026-11-26-R144-terminal-mean-small-scalar-gate-inputs.json --manifest-sha __MANIFEST_SHA__
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
    files.append(spec('terminal_mean_contract', relative, selected(contract, relative)))
    files.extend(spec(role, TOPIC+'/'+relative) for role, relative in CURRENT)
    by_role = {item['role']: item for item in files}
    if len(files) != 11 or len(by_role) != 11:
        raise ValueError('complete distinct small-input closure')
    review = json.loads((root/by_role['reviewed_rules']['path']).read_bytes())
    for path, expected in review['readme_sha256'].items():
        if sha((root/path).read_bytes()) != expected:
            raise ValueError('unread README change: '+path)
    required = {
        'c0_result': '0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641',
        'c0_execution': '9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc',
        'initial_result': '7cddc5856510c7e602a2e22d504492c8ab4732f900331c02e646f14b04da1635',
        'old_readable': '232a4bf0741eed57c5d5ae7e149795df1541e05236dc7afa05a60dc997094991',
        'raw_bounds': '84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e',
        'proof': '5a7a5bf8b6873976d173bfc5be8c3b25fbcd03174e97ba56a4abd99e06440986'}
    for role, digest in required.items():
        if by_role[role]['sha256'] != digest:
            raise ValueError('complete accepted scalar input changed: '+role)
    manifest = dict(STATIC, files=files, expected_current_input_count=len(files))
    if (len(manifest['allowed_scientific_fields']) != 19
            or len(manifest['allowed_new_scalar_fields']) != 21
            or len(manifest['required_gate_fields']) != 13):
        raise ValueError('exact complete scalar gate schema')
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()
    (out/(PREFIX+'-inputs.json')).write_bytes(raw)
    (out/'fourfold-codazzi-terminal-mean-small-scalar-gate-public.yml').write_text(
        WORKFLOW.replace('__MANIFEST_SHA__', sha(raw)))
    print(json.dumps(dict(manifest_bytes=len(raw), manifest_sha256=sha(raw),
        current_inputs=len(files), historical_inputs=0, new_target_count=1), sort_keys=True))


if __name__ == '__main__':
    main()
