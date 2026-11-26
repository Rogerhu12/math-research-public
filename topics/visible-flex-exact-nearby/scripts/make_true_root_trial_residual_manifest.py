"""Metadata-only exact TC launch and same-object continuation generator.

A later manifest requires an actual whole predecessor manifest/execution
and every published formal object.  All three objects complete means no
new scientific launch.  Native values and old targets are never computed
here; the worker admits their entire restored bytes before reservation.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_true_root_trial_residual_manifest.py"
BASE_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-rematerialized-inputs"
BASE_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-rematerialized-public"
OUTPUT_BASE = TOPIC+"/notes/true_root_trial_residual_ci"
REVIEWED_RULES_SHA256 = "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051"

EXTRA_CURRENT = [{
    "role": "RW_manifest",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-26-reflected-waist-rows-inputs.json",
    "bytes": 14822,
    "sha256": "be8da3e31973d9c3725a4dcb4834287a1add06121e3853ea4308b08b656fac05",
    "git_blob_sha": "4b24e937843efdafb328bf692bbcfa9f19dd4f9c"
}, {
    "role": "NW_manifest",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-26-negative-nu-waist-inputs.json",
    "bytes": 11815,
    "sha256": "b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d",
    "git_blob_sha": "269792eebdc8aa8da068178acca72641cb2812ec"
}, {
    "role": "RW_actual",
    "path": "topics/visible-flex-exact-nearby/notes/reflected_waist_rows_ci/run-45787309600-1/actual-reflected-waist-rows.json",
    "bytes": 86146,
    "sha256": "b0faf218c059b6f7ee113a5f127a7518e78d2c87dc70b4dcf650ce97594c7fa4",
    "git_blob_sha": "05e179aa3a8815c84e8d09db9f2693f0e1930374"
}, {
    "role": "RW_execution",
    "path": "topics/visible-flex-exact-nearby/notes/reflected_waist_rows_ci/run-45787309600-1/execution.json",
    "bytes": 16042,
    "sha256": "3cfc1cbc9f8b1c5fe450c779146042c6b7f4bd4f42ca48606c4c9309e94a0b00",
    "git_blob_sha": "7d60a03a1ea9fe101724cba161bb1402cf4c6cb6"
}, {
    "role": "old_body_manifest",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-body-CI-pinned-inputs.json",
    "bytes": 31806,
    "sha256": "c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784",
    "git_blob_sha": "b4a96180d2e1abca2ae90e7ba363e6a0c78149d9"
}, {
    "role": "old_response_summary",
    "path": "topics/visible-flex-exact-nearby/notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json",
    "bytes": 18829,
    "sha256": "7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec",
    "git_blob_sha": "b4baed45ea0038c6aa38de8bd2939447ef2d39e0"
}, {
    "role": "old_rows_worker",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_selected_parameter_core_scalar_fees_ci.py",
    "bytes": 42106,
    "sha256": "2e1527bfecb2b33ca911d7f8215d8c09e896e36b58144446b34b4a6f01fcc52f",
    "git_blob_sha": "b3f5aeb44d5ad712c13baad65d633b3197e28708"
}, {
    "role": "original_row_source",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_correlated_head_residual_rows.py",
    "bytes": 13043,
    "sha256": "1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07",
    "git_blob_sha": "3af195a36ccb30630dbfcab0caef3564738ab169"
}, {
    "role": "original_scalarization_manifest",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-current-root-scalarization-CI-inputs.json",
    "bytes": 4942,
    "sha256": "b1e47bdc43fdb5f9742ee8feb087f5a66dd72457439405abecb1816012b1c746",
    "git_blob_sha": "a4de300fe8338875cb7f8062efaee60da7dc4864"
}, {
    "role": "candidate_reader",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_candidate_shards.py",
    "bytes": 4187,
    "sha256": "5c9d35584793129d07723f00a9405a43e9764c18810ef1b2fc4560a3c5557c5e",
    "git_blob_sha": "81a21dba0077137601382781b6b3298bdd7d5ade"
}, {
    "role": "repair_source",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_final_continuous_value_repair.py",
    "bytes": 9076,
    "sha256": "51a3f7968991ed85211b74c23befae7021bb192796daf0ae2d12ec5a1d45329b",
    "git_blob_sha": "67d7de2adf36c916123f7c9cf7a5db09af3c7b58"
}, {
    "role": "direction_source",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_explicit_response_direction.py",
    "bytes": 12528,
    "sha256": "9c08e253d2b4cdd951392a31aafc190b2341793a162c46aaadd914780894bf5c",
    "git_blob_sha": "0cb590036ade83a066766a741a1c294d98319faa"
}, {
    "role": "box_math",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_phase_root_interval.py",
    "bytes": 18526,
    "sha256": "07cde6d560bd2681b69bc4a4487178276a21bda8fd3e0a56cdd43800ddd0f840",
    "git_blob_sha": "75a8da3bb8141c20b30960a370369cf486a50a00"
}, {
    "role": "fft_math",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_phase_beta_bulk_box.py",
    "bytes": 20229,
    "sha256": "b880a940d30860ed0998509b1a29f7b1f13ac5ac646f4628d91ea87ea3ccba4a",
    "git_blob_sha": "e97a7d95dcd17493944605c616f2a303a8c575d6"
}, {
    "role": "proof",
    "path": "topics/visible-flex-exact-nearby/results/R149-supplement-true-root-continuous-PDE-trials-and-complete-residuals.md",
    "bytes": 17014,
    "sha256": "6313fc86c667e9e0c74675e9773bc7160bf3a555c2f326659bf54ad060e7d13f",
    "git_blob_sha": "60d1fb64b02d6cdf9ef5e287579cfc510b686968"
}, {
    "role": "trial_math",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_residual_math.py",
    "bytes": 26193,
    "sha256": "1131c70ad0f568a692321dd2aab9de76b194aa5abb3f160924ab3befa290771c",
    "git_blob_sha": "ca149aa9ae39d27818ea3fcbd955ab1bd4d2a03b"
}, {
    "role": "proposal_math",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_proposal.py",
    "bytes": 12027,
    "sha256": "a50faff5db45a96cd2fb8ffa7b9e0881d7df992d1e67ae7b587efed7feb49025",
    "git_blob_sha": "777e00bc7eedf134a05ba1bb8913fc091b5c8030"
}, {
    "role": "inputs_math",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_inputs.py",
    "bytes": 19454,
    "sha256": "4409dd3c8733972e3d9479ef6449ab85b39f2d2900cd5fe4376dda5cd335c826",
    "git_blob_sha": "5a50a95d49561ed3bca2d3a5c00d2151803ecec2"
}, {
    "role": "owner",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_owner.py",
    "bytes": 62761,
    "sha256": "0a94eae9a86a168c8a31b2739c08b9f9c273fee387ac755ed23a21744922f3b1",
    "git_blob_sha": "821335205dca3da7553eef523baa032d36dd0918"
}, {
    "role": "worker",
    "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py",
    "bytes": 44572,
    "sha256": "ad342a6ab803f53d609063c3f12fe8587de79800d287187a2ed7cdc79c1bbe11",
    "git_blob_sha": "caa35cca4d540284073c7dfe5a923cb0e16170f6"
}, {
    "role": "contract",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-26-true-root-trial-residual-contract.md",
    "bytes": 10002,
    "sha256": "44d1581f0960a6c89c8a69ade7ed00a7d4ced689f6bb4b7050d315042840c918",
    "git_blob_sha": "e9379343811013ad1d5b7dbadfce93300160331b"
}]
HISTORICAL_INPUTS = [{
    "bytes": 3356,
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "git_blob_sha": "259b77db8fe824b83e27223b8903c858a83efcfd",
    "path": "topics/visible-flex-exact-nearby/notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz",
    "restore_only": True,
    "role": "W_native",
    "sha256": "dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854"
}, {
    "bytes": 3560,
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "git_blob_sha": "eb72e2fd385328289c2879f7fdcab8b4c017967a",
    "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/consumers/R31.json.gz",
    "restore_only": True,
    "role": "R31_native",
    "sha256": "d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61"
}, {
    "bytes": 20486,
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "git_blob_sha": "b3df5d240d44b5b2a9abe940dc1e525f25937c7c",
    "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/consumers/post48.json.gz",
    "restore_only": True,
    "role": "K_native",
    "sha256": "a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60"
}, {
    "bytes": 3089,
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "git_blob_sha": "614a6762a240a0f89f5ab991174544ff3d38bde3",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz",
    "restore_only": True,
    "role": "H_native",
    "sha256": "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43"
}, {
    "role": "base_index",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json",
    "bytes": 6750,
    "sha256": "ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413",
    "git_blob_sha": "2257c4327fcafcad3ed50f0362fb089e9cfd56d2",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "utf-8-json",
    "restore_only": True
}, {
    "role": "base_part000",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part000.npz.gz",
    "bytes": 2738500,
    "sha256": "5dae124eef0b3004bfea08334c2f2546ade3edc5cb926c665591e42b842babc4",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "base_part001",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part001.npz.gz",
    "bytes": 2738003,
    "sha256": "3aeb38bf0577207cafcad3a59e43ed5a04a4c9cf9a703c4c3c4088c963a09106",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "base_part002",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part002.npz.gz",
    "bytes": 2738686,
    "sha256": "a317c6f491295d8e46aa5d4b3da84c1f26bd16d5fb65260f3d3459e1f9c6210e",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "base_part003",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part003.npz.gz",
    "bytes": 2732843,
    "sha256": "7b67e5a4b11ae45476d1507e842ae23919ca44e4ed2d64bc81bdea78e0b4007c",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "base_part004",
    "path": "topics/visible-flex-exact-nearby/data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part004.npz.gz",
    "bytes": 1532492,
    "sha256": "314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_index",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full.json",
    "bytes": 11295,
    "sha256": "ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6",
    "git_blob_sha": "51de488e7caca745bd3f1a9ccc13aa63cad106b5",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "utf-8-json",
    "restore_only": True
}, {
    "role": "direction_part000",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part000.npz.gz",
    "bytes": 2704054,
    "sha256": "113bbea9a72c1c899f2ef56b4b0b8f0f1799bcfecec711cbbe4444ceee1dcde1",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part001",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part001.npz.gz",
    "bytes": 2711019,
    "sha256": "f1b5ef3f1bdcd85e26127e31b968e1b202da7995f203542dcdd416aedbce5b8d",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part002",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part002.npz.gz",
    "bytes": 2706706,
    "sha256": "f55dd0cce50d85f84f34d923dcb2ff5a47a5a7a679403c8a0fed2817489ddfcf",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part003",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part003.npz.gz",
    "bytes": 2697663,
    "sha256": "ff1c4c2ba06544cb116832106648248e6386fc5b5578a9e48a6344cb4360ec55",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part004",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part004.npz.gz",
    "bytes": 2699786,
    "sha256": "12f06fd89466659ddbcef6abdc52b561189f12bd67d55b0e5a73acd971bb9cee",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part005",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part005.npz.gz",
    "bytes": 2698707,
    "sha256": "ce29c19c81e77cb2f2ea9b70edc59af96a869116fa96e2e5375ffa4d61927917",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part006",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part006.npz.gz",
    "bytes": 2700421,
    "sha256": "68090bc73a3d099b9631b01419ac9607ff34cf4b0398518db242fec5ac32dc31",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part007",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part007.npz.gz",
    "bytes": 2699509,
    "sha256": "7c58e4b73ecbec48e5376a3c72b944a38e70bca56a1201fd4f18c1b263c289b9",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part008",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part008.npz.gz",
    "bytes": 2702191,
    "sha256": "47b4d5bb6c0f48e535365d4d3445bc084aae8d79118d41a8ea9c36b00bb7a990",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part009",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part009.npz.gz",
    "bytes": 2693136,
    "sha256": "4682236e686d4aa083854b2e3852eab9df1cdf95754c5518ea3548c6bda61b94",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part010",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part010.npz.gz",
    "bytes": 2695973,
    "sha256": "d3c0f61644f6366bacb04f1b6e0e6f439b9a46c2cf1117f00175ba372ccbe0ec",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part011",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part011.npz.gz",
    "bytes": 2700962,
    "sha256": "8d29b2082d81e56d7177db7c4c0894d53a20402d704404dec596cc246f614469",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part012",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part012.npz.gz",
    "bytes": 2698989,
    "sha256": "777337c853329f26719b148e34db079c5ca0ed34991aa40220f25624e4af0b3c",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "direction_part013",
    "path": "topics/visible-flex-exact-nearby/data/body_regular_nodal_resume_20261114/response-full-part013.npz.gz",
    "bytes": 1517845,
    "sha256": "4a863085ec89c7d7104b4fdf566f9ae380d22eb7b4e4f8b2146cd190c3b4b037",
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-npz",
    "restore_only": True
}, {
    "role": "old_centre_repair",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-exact-continuous-value-repair-native.json.gz",
    "sha256": "6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc",
    "bytes": 14226,
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-json",
    "restore_only": True
}, {
    "role": "old_direction_repair",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-explicit-continuous-response-direction-native.json.gz",
    "sha256": "87ed2f618bcaf77b0649abf561daea7225c9b7d667edc22afb91d86255da8f88",
    "bytes": 502954,
    "commit": "7c130fb94528de8f003a43e7049fb42768a64eec",
    "encoding": "gzip-json",
    "restore_only": True
}]

WORKFLOW_TEMPLATE = """name: R149 complete true-root finite trials @LABEL@
on:
  push:
    branches: [main]
    paths:
      - '@WORKFLOW@'
  workflow_dispatch:
permissions:
  contents: write
  actions: read
concurrency:
  group: visible-flex-exact-true-root-finite-trials-20261126
  cancel-in-progress: false
jobs:
  complete-new-finite-trial-objects:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 360
    env:
      OPENBLAS_CORETYPE: Haswell
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py
            /@MANIFEST@
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed finite-trial runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Whole old inputs, true-root finite trial and only missing complete objects
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest @MANIFEST@
          --manifest-sha @MANIFEST_SHA@
"""


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
                       ensure_ascii=False,allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw,parse_constant=lambda x:(_ for _ in ()).throw(ValueError(x)))


def safe(root,relative):
    require(isinstance(relative,str) and not relative.startswith("/")
            and all(p not in ("",".","..") for p in relative.split("/")),"safe repository path")
    path = (root/relative).resolve()
    require(path.is_relative_to(root),"entire file stays within this checkout")
    return path


def descriptor(path,raw):
    return {"path":path,"bytes":len(raw),"sha256":sha(raw),"git_blob_sha":blob(raw)}


def whole_small(root,path):
    raw = safe(root,path).read_bytes()
    require(0 < len(raw) < 100000,"one whole small UTF8 input: "+path)
    raw.decode()
    if path.endswith(".py"):
        ast.parse(raw.decode(),filename=path)
    return raw


def import_source(path,name):
    spec = importlib.util.spec_from_file_location(name,path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def original_small_index(root,spec):
    require(spec["role"] in ("base_index","direction_index")
            and spec["encoding"] == "utf-8-json" and spec["restore_only"] is True,
            "only two original entire small index texts are read during metadata generation")
    commit,path = spec["commit"],spec["path"]
    require(commit == "7c130fb94528de8f003a43e7049fb42768a64eec"
            and path.startswith(TOPIC+"/"),"exact original body input commit")
    def git(*arguments,check=True):
        return subprocess.run(["git",*arguments],cwd=root,capture_output=True,check=check)
    if git("cat-file","-e",commit+"^{commit}",check=False).returncode:
        git("fetch","--filter=blob:none","--no-tags","--depth=1","origin",commit)
    observed = git("rev-parse",commit+":"+path).stdout.decode().strip()
    raw = git("show",commit+":"+path).stdout
    require(observed == spec["git_blob_sha"] and blob(raw) == observed
            and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],
            "whole original lossless cubic index bytes")
    return parse(raw)


def build(root,prior_manifest_path=None,prior_execution_path=None):
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "launch generation is metadata only")
    require(Path(__file__).resolve() == safe(root,GENERATOR),"this entire current generator")
    sys.dont_write_bytecode = True
    definitions,contents,roles = {},{},{}
    def add(path,raw,expected=None,role=None):
        require(path.startswith(TOPIC+"/"),"every scientific input is in this authorized topic")
        observed = descriptor(path,raw)
        if expected is not None:
            require(all(observed[key] == expected[key] for key in observed),
                    "whole immutable current input: "+path)
        if path in definitions:
            require(definitions[path] == observed and contents[path] == raw,
                    "deduplication preserves the same complete original object")
        definitions[path],contents[path] = observed,raw
        if role is not None:
            require(role not in roles or roles[role] == path,"unique declared semantic role")
            roles[role] = path
    for spec in EXTRA_CURRENT:
        # The input-only public-worker repair is a new explicit source;
        # every mathematical TC source retains its original exact identity.
        expected = None if spec["role"] == "worker" else spec
        add(spec["path"],whole_small(root,spec["path"]),expected,spec["role"])
    add(GENERATOR,whole_small(root,GENERATOR),role="generator")
    rwm,nwm = (parse(contents[roles[name]]) for name in ("RW_manifest","NW_manifest"))
    for old in (rwm,nwm):
        for spec in old["files"]:
            add(spec["path"],whole_small(root,spec["path"]),spec)
    require(len(definitions) == 78,"the complete fixed text closure has78 unique whole files")
    roles["reviewed_rules"] = next(s["path"] for s in rwm["files"] if s["role"] == "reviewed_rules")
    roles["old_rows_manifest"] = next(s["path"] for s in nwm["files"] if s["role"] == "D_manifest")
    helper_path = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_restore.py"
    add(helper_path,whole_small(root,helper_path),role="restoration_helper")
    restoration = import_source(safe(root,helper_path),"_TC_metadata_exact_restoration")
    extra_current,history,input_restoration = restoration.build_plan(root,HISTORICAL_INPUTS)
    for spec in extra_current:
        add(spec["path"],whole_small(root,spec["path"]),spec)
    for spec in history:
        require(spec["path"] not in definitions and
                (spec["restore_only"] is True or spec.get("reconstruct_only") is True),
                "each original input has one explicit restoration or reconstruction source")
        roles[spec["role"]] = spec["path"]
    require(len(history) == 32 and len({s["path"] for s in history}) == 32,
            "original27 inputs plus3 exact nodal ranges and2 original geometry arrays")
    inherited = {s["path"]:s for s in history}
    for spec in rwm["historical_inputs"]:
        require(inherited[spec["path"]] == spec,"all four original RW native qualifications preserved verbatim")
    old_body = parse(contents[roles["old_body_manifest"]])
    scalarization = parse(contents[roles["original_scalarization_manifest"]])
    for role,dimension,parts in (("base_index",65,5),("direction_index",193,14)):
        index_spec = next(s for s in history if s["role"] == role)
        index = original_small_index(root,index_spec)
        require(index["kind"] == "complete_lossless_radial_cubic_shards_v1"
                and index["coefficient_shape"] == [4,6144,dimension]
                and index["radial_nodes_count"] == 6145 and len(index["parts"]) == parts
                and old_body["files"][index_spec["path"]] == index_spec["sha256"],
                "same whole original base or physical response definition")
        for part in index["parts"]:
            path = str(Path(index_spec["path"]).parent/part["file"])
            got = inherited[path]
            require(got["sha256"] == part["sha256"] and got["bytes"] == part["bytes"]
                    and got["encoding"] == "gzip-npz"
                    and ((role == "base_index" and got["commit"] == index_spec["commit"])
                         or (role == "direction_index" and got.get("reconstruct_only") is True)),
                    "every original complete shard is pinned; missing direction shards are explicit reconstruction")
    for role in ("old_centre_repair","old_direction_repair"):
        spec = next(s for s in history if s["role"] == role)
        require(any(old["path"] == spec["path"] and old["bytes"] == spec["bytes"]
                    and old["sha256"] == spec["sha256"] for old in scalarization["files"]),
                "same complete original signed repair-native identity")
    owner = import_source(safe(root,OWNER),"_TC_metadata_owner")
    require(owner.SOURCE_PATH == OWNER and owner.KIND == "R149_complete_true_root_finite_trial_residuals_v1"
            and all(definitions[roles[role]]["sha256"] == value for role,value in owner.SOURCE_HASHES.items()),
            "the complete exact reviewed finite-trial definition closure")
    nw_owner_path = next(s["path"] for s in nwm["files"] if s["role"] == "science")
    nw_owner = import_source(safe(root,nw_owner_path),"_TC_readonly_original_NW_admission")
    nws = {s["role"]:s for s in nwm["files"]}
    nw = nw_owner.admit_complete_inputs({role:contents[spec["path"]] for role,spec in nws.items()},nws)
    actual,execution = (parse(contents[roles[name]]) for name in ("RW_actual","RW_execution"))
    expected_rows = ["row_%03d"%j for j in range(1,97)]
    require(actual["complete"] is actual["proved"] is True
            and actual["actual_returncode"] == 0 and actual["failure"] is None
            and actual["completed_targets"] == expected_rows
            and actual["saved_record_count"] == actual["private_complete_row_count"] == 96
            and actual["identity"]["manifest_sha256"] == definitions[roles["RW_manifest"]]["sha256"]
            and actual["reference_identity"] == nw["family"]
            and execution["complete"] is True and execution["actual_child_returncode"] == 0
            and execution["run_id"] == "45787309600" and execution["run_attempt"] == "1"
            and execution["scientific_files"] == [{
                "path":roles["RW_actual"],"bytes":definitions[roles["RW_actual"]]["bytes"],
                "sha256":definitions[roles["RW_actual"]]["sha256"]}],
            "whole actual successful RW96 and exact same selected family")
    require(nw["difference"]["complete_original_rows_verified"] == 7721
            and nw["difference"]["original_rows_canonical_payload_sha256"]
                == "06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6"
            and len(nw["difference"]["original_part_receipts"]) == 40
            and Fraction(nwm["parameters"]["selected_parameter_absolute_upper"])
                == Fraction(owner.PARAMETERS["exact_selected_delta_absolute_upper"]),
            "the entire original rows and narrower actual selected member, without redoing old scalar fees")
    source_manifest = parse(contents[roles["old_rows_manifest"]])
    accepted = parse(contents[roles["old_response_summary"]])
    table = lambda values:{tuple(s["indices"]):s["sha256"] for s in values}
    require(source_manifest["original_body_manifest_sha256"] == definitions[roles["old_body_manifest"]]["sha256"]
            and source_manifest["original_accepted_response_summary_sha256"]
                == definitions[roles["old_response_summary"]]["sha256"]
            and table(source_manifest["original_complete_native_part_sha256"])
                == table(accepted["original_parts"])
                == table(nw["difference"]["original_part_receipts"])
            and len(source_manifest["historical_natural_parts"]) == 6
            and len(source_manifest["original_row_archives"]) == 8,
            "all original six history parts and eight complete archives lead to the same forty-part table")
    review = parse(contents[roles["reviewed_rules"]])
    require(definitions[roles["reviewed_rules"]]["sha256"] == REVIEWED_RULES_SHA256
            and review["repository"] == REPO
            and review["new_unread_rules_must_still_be_reported_and_applied"] is True
            and set(review["readme_sha256"]) == {"README.md",TOPIC+"/README.md"}
            and review["large_data_policy"]["maximum_topic_bytes"] == 200000000
            and review["large_data_policy"]["original_completed_mathematics_must_not_be_recomputed"] is True
            and review["large_data_policy"]["keep_only_scripts_parameters_runs_output_hashes_and_conclusions"] is True,
            "current explicitly read actual two-README rules and complete large-data policy")
    for path,want in review["readme_sha256"].items():
        require(sha(whole_small(root,path)) == want,"current complete README differs from explicit review: "+path)
    require((prior_manifest_path is None) == (prior_execution_path is None),
            "a continuation must supply both entire actual predecessor documents")
    continuation,prior_admission,suffix = None,None,""
    new_targets = list(owner.TARGETS)
    if prior_manifest_path is not None:
        for role,path in (("prior_manifest",prior_manifest_path),("prior_execution",prior_execution_path)):
            add(path,whole_small(root,path),role=role)
        prior_manifest = parse(contents[prior_manifest_path])
        prior_execution = parse(contents[prior_execution_path])
        require(prior_execution["manifest_sha256"] == definitions[prior_manifest_path]["sha256"]
                and prior_execution["input_manifest_path"] == prior_manifest_path,
                "actual previous execution binds the entire exact prior input manifest")
        base = prior_manifest["operation"]["output_base"]+"/run-"+prior_execution["run_id"]+"-"+prior_execution["run_attempt"]+"/"
        for name,filename in owner.FILES.items():
            matches = [s for s in prior_execution["scientific_files"] if s["path"] == base+filename]
            require(len(matches) <= 1,"one complete original formal predecessor object")
            if matches:
                spec = matches[0]
                raw = whole_small(root,spec["path"])
                require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],
                        "the entire actual predecessor publication is unchanged")
                add(spec["path"],raw,role="prior_"+name)
        continuation = {"kind":"R149_same_exact_trial_complete_prefix_continuation_v1",
            "original_run_id":prior_execution["run_id"],"original_run_attempt":prior_execution["run_attempt"]}
        source_names = ("owner","trial_math","proposal_math","inputs_math","box_math","fft_math",
                        "candidate_reader","repair_source","direction_source")
        role_specs = {role:(definitions.get(path) or inherited[path]) for role,path in roles.items()}
        prior_admission = owner.admit_prior_metadata({"continuation":continuation},role_specs,contents,{
            "scientific_sources":{name:role_specs[name]["sha256"] for name in source_names},
            "same_selected_family":nw["family"]})
        new_targets = prior_admission["missing_targets"]
        require(new_targets,"no new target remains after the complete actual predecessor")
        require(prior_execution["run_id"].isdigit() and prior_execution["run_attempt"] == "1",
                "one concrete original first-attempt run")
        suffix = "-continue-"+prior_execution["run_id"]+"-"+definitions[prior_execution_path]["sha256"][:12]
    manifest_path,workflow_path = BASE_MANIFEST+suffix+".json",BASE_WORKFLOW+suffix+".yml"
    problem = "R149_complete_true_root_finite_trials_restored_20261127"+suffix
    manifest = {
        "repository":REPO,"kind":owner.MANIFEST_KIND,"scientific_kind":owner.KIND,
        "stage":"true_root_finite_trial_residuals","problem_id":problem,
        "parameters":owner.PARAMETERS,"runtime":owner.RUNTIME,
        "target_order":owner.TARGETS,"new_target_order":new_targets,
        "allowed_scientific_fields":owner.STATE_FIELDS,
        "files":[definitions[path] for path in sorted(definitions)],
        "historical_inputs":history,"roles":roles,"input_restoration":input_restoration,
        "expected_current_input_count":len(definitions),"expected_historical_input_count":len(history),
        "continuation":continuation,
        "actual_prior_natural_object_metadata_admission":prior_admission,
        "operation":{
            "topic_maximum_bytes":200000000,"reserve_bytes":120000,
            "readme_pull_interval_seconds":1800,"automatic_scientific_retry":False,
            "consumed_marker":OUTPUT_BASE+"/consumed-restored-20261127"+suffix+".json","output_base":OUTPUT_BASE,
            "maximum_state_bytes":18000,"maximum_matrix_bytes":26000,
            "maximum_negative_bytes":50000,"maximum_positive_bytes":52000,"maximum_prefix_bytes":20000,
            "maximum_execution_bytes":35000,"maximum_total_publication_bytes":170000,
            "child_timeout_seconds":17400},
        "scope":{
            "complete_original_rows":7721,"complete_original_natural_parts":40,
            "complete_original_cubic_shards":19,"complete_original_signed_repair_chains":2,
            "necessary_original_nodal_Hermite_reconstruction_separately_counted":True,
            "original40_row_objects_restored_from_Git_without_archive_dependency":True,
            "original_failed_45806282910_manifest_and_execution_unchanged":True,
            "fixed_original_eta_width_retained":"1/1000000000",
            "selected_Q0_plus_delta_Z_and_both_means_retained":True,
            "old_completed_scalar_row_KAM_Gram_or_inverse_targets_recomputed":0,
            "whole_native_admission_before_scientific_target_reservation":True,
            "whole_exact_dyadic_proposal_saved_and_read_back":True,
            "true_root_is_not_a_proposal_midpoint":True,
            "complete_original_dr_and_all288_Fourier_outputs":True,
            "complete_new_scalar_count_if_first_launch":584,
            "formal_candidate_full_readback_before_complete_object":True,
            "all96_all5_source_exact_complete_cell_prefix":True,
            "all_already_complete_formal_objects_required_even_if_old_marker_lagged":True,
            "all_three_prior_objects_complete_forbids_new_science":True,
            "new_private_arrays_published_or_uploaded":False,
            "true_PDE_columns_or_full_inverse_proved":False,
            "SC_true_column_scientific_target_called":False}}
    require(not any(name in sys.modules for name in ("numpy","flint","scipy")),
            "all launch qualification and actual continuation admission remained metadata only")
    raw = canonical(manifest)
    require(0 < len(raw) < 100000,"one entire concrete small input manifest")
    label = "first" if continuation is None else "continue "+continuation["original_run_id"]
    replacements = {"@LABEL@":label,"@WORKFLOW@":workflow_path,
                    "@MANIFEST@":manifest_path,"@MANIFEST_SHA@":sha(raw)}
    workflow = WORKFLOW_TEMPLATE
    for key,value in replacements.items():
        workflow = workflow.replace(key,value)
    require(not any(key in workflow for key in replacements)
            and workflow.count("${{ secrets.GITHUB_TOKEN }}") == 1,
            "one concrete complete new-target workflow, no unresolved launch placeholders")
    return manifest_path,raw,workflow_path,workflow.encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--prior-manifest")
    parser.add_argument("--prior-execution")
    args = parser.parse_args()
    root = args.repo.resolve()
    manifest_path,raw,workflow_path,workflow = build(root,args.prior_manifest,args.prior_execution)
    outputs = [(safe(root,manifest_path),raw),(safe(root,workflow_path),workflow)]
    require(all(not path.exists() for path,raw in outputs),
            "never overwrite a previously concrete target or its actual continuation")
    for path,body in outputs:
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open("xb") as stream:
            stream.write(body)
    print(canonical({"metadata_only":True,"scientific_calls":0,"dispatch_or_publication_performed":False,
        "manifest":descriptor(manifest_path,raw),"workflow":descriptor(workflow_path,workflow),
        "new_target_order":parse(raw)["new_target_order"],
        "complete_actual_prior_objects_consumed":parse(raw)["actual_prior_natural_object_metadata_admission"],
        "current_both_READMEs_checked":True}).decode(),end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
