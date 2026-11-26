"""R149 complete exact reflected waist-row carriers and three error bounds.

Only old complete W/R31/K48/H and fixed-Js normalizer conclusions are read.
The new numerical target is the 96 exact sampled-DFT row trials in RW.14.
Every complete private carrier is saved and read back. Only small row
conclusions and complete carrier hashes become public; no old target runs.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, importlib.util, json, os
from pathlib import Path
import platform, sys, time, traceback
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_reflected_finite_waist_rows_v1"
STAGE = "reflected_finite_waist_rows"
MANIFEST_KIND = "R149_complete_reflected_finite_waist_row_inputs_v1"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_reflected_waist_rows_manifest.py"

ROW_PARAMETERS = {
    "arithmetic_bits": 320,
    "row_modes": 96,
    "grid_points": 4096,
    "trial_fourier_cutoff": 1024,
    "fixed_original_waist_normalizer_cutoff": 268435456,
    "physical_frequency_factor": 4,
    "original_conjugacy_strip": "1/128",
    "original_selected_run": "43588332723/1",
    "original_selected_loss": "1/250",
    "exact_H_constant_term": "0",
    "exact_K48_constant_term": "0",
    "exact_H_nonmean_degree": 24,
    "exact_real_basis": "sqrt(2)*cos(4*j*(x-a/2)); a=2*H(0); j=1..96",
    "compound_lift": "(G(phi)-G(-phi))/2; G=K48 composed with H_fin",
    "exact_trial": "truncated exact L-point DFT of sqrt(2)*cos(4*j*G_odd)",
    "arbitrary_midpoint_trial_selection": False,
    "incoming_row_full_old_angle_mean_retained": True,
    "physical_primitive_row_has_two_half_nonmean_components": True,
    "independent_density_mean_rows": 2,
    "target_B_inverse_or_Theta_rows_included": False,
    "old_KAM_or_old_receiver_scientific_calls": 0
}
PARAMETERS = {
    "arithmetic_bits": 320,
    "row_modes": 96,
    "grid_points": 4096,
    "trial_fourier_cutoff": 1024,
    "fixed_original_waist_normalizer_cutoff": 268435456,
    "physical_frequency_factor": 4,
    "original_conjugacy_strip": "1/128",
    "original_selected_run": "43588332723/1",
    "original_selected_loss": "1/250",
    "exact_H_constant_term": "0",
    "exact_K48_constant_term": "0",
    "exact_H_nonmean_degree": 24,
    "exact_real_basis": "sqrt(2)*cos(4*j*(x-a/2)); a=2*H(0); j=1..96",
    "compound_lift": "(G(phi)-G(-phi))/2; G=K48 composed with H_fin",
    "exact_trial": "truncated exact L-point DFT of sqrt(2)*cos(4*j*G_odd)",
    "arbitrary_midpoint_trial_selection": False,
    "incoming_row_full_old_angle_mean_retained": True,
    "physical_primitive_row_has_two_half_nonmean_components": True,
    "independent_density_mean_rows": 2,
    "target_B_inverse_or_Theta_rows_included": False,
    "old_KAM_or_old_receiver_scientific_calls": 0,
    "decimal_record_digits": 50,
    "private_coefficient_digits": 80,
    "maximum_scientific_wall_seconds": 1200,
    "continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_direction_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "exact_nu_centre": "-2572625729470897/72057594037927936",
    "exact_alpha": "6890507429876859/9007199254740992",
    "fixed_intrinsic_parameter": "eta_0",
    "old_numerical_producers_called": 0,
    "new_public_arrays": 0,
    "new_complete_row_records": 96,
    "small_scalar_records_per_row": 5,
    "target_row_scope": "96 original physical reflected primitive rows and 96 declared incoming cosine observations; independent density means retained",
    "receiver_operator_BH_norm_not_newly_evaluated": True
}
TARGETS = ["row_%03d" % j for j in range(1, 97)]
SCI_FIELDS = ["actual_returncode", "candidate_record", "complete", "completed_targets", "copied_prior_scalar_records", "current_target", "definition_sha256", "exact_definition", "failure", "identity", "new_Releases", "new_arrays_published", "new_artifacts", "new_records", "old_scientific_target_calls", "parameters", "pending_row", "private_complete_row_count", "private_grid_receipt", "proved", "reference_identity", "result", "runtime", "saved_record_count", "selected_member_identity", "stage", "wall_seconds", "whole_completed_inputs"]
FIXED_INPUTS = {
    "reviewed_rules": {
        "role": "reviewed_rules",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-20-reviewed-public-CI-rules.json",
        "bytes": 2112,
        "sha256": "26da0165d2a7ec5f968959332c9fd04aae7259059de2b56f41e76b49b61fc051",
        "git_blob_sha": "71787717a9a58933f311091d20261a61a7581252"
    },
    "proof": {
        "role": "proof",
        "path": "topics/visible-flex-exact-nearby/results/R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md",
        "bytes": 14331,
        "sha256": "af3e1888066b4e88d8f1e5eff525c832d6d98b03fa8b401bcb15c9d6e2920db3",
        "git_blob_sha": "545154324f51ad793aa581e2ecb95e4983d2026f"
    },
    "row_math": {
        "role": "row_math",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_row_trials_math.py",
        "bytes": 12663,
        "sha256": "c8f40a0d50c6b55c58016adca749aed00c8236f3eab653987ddd941f047cdf09",
        "git_blob_sha": "65ff3491563d78a670f046f4bd706829bff15151"
    },
    "proof_SC": {
        "role": "proof_SC",
        "path": "topics/visible-flex-exact-nearby/results/R149-supplement-signed-finite-columns-and-full-negative-residual-sources.md",
        "bytes": 21533,
        "sha256": "059c4d0490ab5725aa01bcefa31446101d4464f151bc3801b1b8530aa1ef1ec0",
        "git_blob_sha": "01efc774c206583123cd838ee26b0e745e29af4c"
    },
    "proof_W": {
        "role": "proof_W",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-actual-physical-Wiener-conjugacy-strip.md",
        "bytes": 6138,
        "sha256": "1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3",
        "git_blob_sha": "a79a7ad7c147076b044389e98a15ab2f341d0d0c"
    },
    "proof_RRF": {
        "role": "proof_RRF",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-true-reflection-rigidity-and-selected-waist-target.md",
        "bytes": 15266,
        "sha256": "803302f2924da51022e2aa16a36c928ee0789fde93277f5ea9fd9c2ae2a3630f",
        "git_blob_sha": "cdb4b957f6976c7b72e974fcccc8f2a15afbee74"
    },
    "proof_WTA": {
        "role": "proof_WTA",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-actual-right-waist-normalizer-and-complete-two-window-inverse.md",
        "bytes": 15465,
        "sha256": "f90ba8a15255ec5326b0680f436e8f8ff25dcadad60188a9ecbc3a24bbbb4e39",
        "git_blob_sha": "93b5c208f1c4c8b0abae5d256b74a2d1a09ef677"
    },
    "proof_WY": {
        "role": "proof_WY",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-four-ordered-waist-receivers-and-complete-strong-error-assembly.md",
        "bytes": 31615,
        "sha256": "698ee0e67c65c5c7ba5ff7a4714620620f5082f2858bdbe4a2ed540e3e7cd536",
        "git_blob_sha": "351a2a9578e4f2eab2a6058810e8c03151e81ee3"
    },
    "proof_WPL": {
        "role": "proof_WPL",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-complete-coefficient-reflection-and-physical-paired-waist-leading-row.md",
        "bytes": 31021,
        "sha256": "052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24",
        "git_blob_sha": "582679b6e48a271153b90ecf1691deca2dc27c9c"
    },
    "proof_WUE": {
        "role": "proof_WUE",
        "path": "topics/visible-flex-exact-nearby/results/R133-supplement-complete-global-genuine-trial-physical-waist-error.md",
        "bytes": 32557,
        "sha256": "e191f96acc39ab802adb93ace2d1e57691b017629ed762ddd39624d3bcb61ce1",
        "git_blob_sha": "9b5b13f0178c9a292ae8ba11264051c1fe438c14"
    },
    "W_source": {
        "role": "W_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_R31_strip_refinement.py",
        "bytes": 6640,
        "sha256": "c1ca128ce18007ec118565beb013a97eaf7c0ccb11962caee474eec092a6c069",
        "git_blob_sha": "44a11c484652d83eb01859684c02356dac967394"
    },
    "W_driver": {
        "role": "W_driver",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_strip_refinement_CI.py",
        "bytes": 4249,
        "sha256": "de7461d96ee784208966def4026994789d2ecfa0419a49a3abfde360cad446ef",
        "git_blob_sha": "d885a63e7901d9bd73d88332156b243811a3f7b7"
    },
    "H_source": {
        "role": "H_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_final_phase_root_sliver_budget.py",
        "bytes": 8343,
        "sha256": "7cef3cecedb730d288eb48991503015cf08fd289b4cbda75ef30f95e09b8bc17",
        "git_blob_sha": "5d4e96116eacdbb4628e722af8eb3e7c88b0d214"
    },
    "H_transport_source": {
        "role": "H_transport_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_full_transport_Taylor.py",
        "bytes": 21725,
        "sha256": "3254a9225f4933ae11ffbfa1862a50ed1c7c585f03aa11e56606ad758ccc6961",
        "git_blob_sha": "d1eb1daf70bec86892309adea4c5701086ffaac3"
    },
    "K_source": {
        "role": "K_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_terminal_postcomposition.py",
        "bytes": 13936,
        "sha256": "73ff7aa0438b722e5fbc70151d24431524ddf76d6d2020cfefc02f209116f69c",
        "git_blob_sha": "ff70de7ff74072529321667e73bd0d22ec0ee18d"
    },
    "R31_source": {
        "role": "R31_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_explicit_family_R31.py",
        "bytes": 14666,
        "sha256": "df58ef8806461a03870e413e6a8d564947c3cd20a6074127a14a8d4bae5d0163",
        "git_blob_sha": "67eadd436bffdb61e51c05ff59c0f3ae88d66633"
    },
    "nine_driver": {
        "role": "nine_driver",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_phase_small_consumers_CI.py",
        "bytes": 7578,
        "sha256": "9d8d5a36cc79bbf0e9d85b53e52ef8c034de05046813f0b142c3aa1c750fa8c0",
        "git_blob_sha": "913edad0d74d328524c0008807153d48cfc85744"
    },
    "WTA_source": {
        "role": "WTA_source",
        "path": "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_waist_normalizer_coefficients.py",
        "bytes": 26205,
        "sha256": "7cde6f7f6d03bbfa107a93abdd4ee925b332f47ac7c4a2257d6557e00927a393",
        "git_blob_sha": "7f0a7713998a96d10e8b28fbbc3a33f8783359d6"
    },
    "W_process": {
        "role": "W_process",
        "path": "topics/visible-flex-exact-nearby/notes/phase_strip_refinement_ci/run-43588332723-1/consumers/process.json",
        "bytes": 1958,
        "sha256": "ea6fe86bd9331f8e14caedc1c46dcf5de26e275cff023c87ead717d6adbafdff",
        "git_blob_sha": "9d1772abd1c3e2494c03899e84a285e59833c62e"
    },
    "W_manifest": {
        "role": "W_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-phase-strip-refinement-CI-inputs.json",
        "bytes": 16673,
        "sha256": "ca3c3f2b056d8d75bf563eeb3aa0c8c56ad587e6c0587317ca089cb18e9af657",
        "git_blob_sha": "65003983d0865cde4d62e47b22c910e11621be8a"
    },
    "W_publication": {
        "role": "W_publication",
        "path": "topics/visible-flex-exact-nearby/notes/phase_strip_refinement_ci/run-43588332723-1/publication.json",
        "bytes": 1966,
        "sha256": "6d6654635ced294b1ecd4b5d9f225f5a1dec3fc747d5c12c99efaa2dbc8a411d",
        "git_blob_sha": "64bf144b7575d28bdb420c3f5321ee87165c8cea"
    },
    "nine_process": {
        "role": "nine_process",
        "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/consumers/process.json",
        "bytes": 12773,
        "sha256": "3319762cb2bb007f616f712c1a3f257e6aba18382e2abd321a770cd6abe53072",
        "git_blob_sha": "22d8b3aabba0f9e09352c7ced0376daf8ab289d6"
    },
    "nine_manifest": {
        "role": "nine_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-phase-small-consumers-CI-inputs.json",
        "bytes": 65000,
        "sha256": "6c6d9fbf7a9155d054f9b455ee9c5010a0a7856ecd0bc82be959f7818844fc21",
        "git_blob_sha": "011ef3f498c36f28915c708786f7c6d35fb6008a"
    },
    "nine_publication": {
        "role": "nine_publication",
        "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/publication.json",
        "bytes": 3999,
        "sha256": "87c9461e6634482a2dabedabc2a06153c4499c37e851e7044c72097d857a793d",
        "git_blob_sha": "3846165f756c675e1c7e10c1f79136b50e6b4c83"
    },
    "WTA_actual": {
        "role": "WTA_actual",
        "path": "topics/visible-flex-exact-nearby/notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json",
        "bytes": 27619,
        "sha256": "2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d",
        "git_blob_sha": "b742d3167f68c05ef197450a3112eb5b8edcacac"
    },
    "WTA_execution": {
        "role": "WTA_execution",
        "path": "topics/visible-flex-exact-nearby/notes/waist_normalizer_coefficients_ci/run-43763134339-1/execution.json",
        "bytes": 16607,
        "sha256": "571e0993583844079d0aad828cd2da093336761429551d1e25b88e912f40fcf7",
        "git_blob_sha": "14739c6ccfd5134b3ad41b184e9fab81ddf83530"
    },
    "WTA_manifest": {
        "role": "WTA_manifest",
        "path": "topics/visible-flex-exact-nearby/notes/2026-11-15-R133-waist-normalizer-coefficients-CI-inputs.json",
        "bytes": 22152,
        "sha256": "4cec7ef0ba21373190dd0bf142d10546823d46bb832a58df66529822990ad125",
        "git_blob_sha": "2990b2427399790eeda3e84002a1e8e41a8f2e54"
    }
}
HISTORICAL_INPUTS = [{
    "role": "W_native",
    "path": "topics/visible-flex-exact-nearby/notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz",
    "bytes": 3356,
    "sha256": "dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854",
    "git_blob_sha": "259b77db8fe824b83e27223b8903c858a83efcfd",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "restore_only": True
}, {
    "role": "R31_native",
    "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/consumers/R31.json.gz",
    "bytes": 3560,
    "sha256": "d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61",
    "git_blob_sha": "eb72e2fd385328289c2879f7fdcab8b4c017967a",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "restore_only": True
}, {
    "role": "K_native",
    "path": "topics/visible-flex-exact-nearby/notes/phase_small_consumers_ci/run-43586895661-1/consumers/post48.json.gz",
    "bytes": 20486,
    "sha256": "a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60",
    "git_blob_sha": "b3df5d240d44b5b2a9abe940dc1e525f25937c7c",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "restore_only": True
}, {
    "role": "H_native",
    "path": "topics/visible-flex-exact-nearby/notes/2026-11-14-R133-final-phase-root-sliver-and-transport-contract-native.json.gz",
    "bytes": 3089,
    "sha256": "1910bdc2ee84cd23a7a92d94689d8cd90a3a5c25cf56caa3cc585159a9c5af43",
    "git_blob_sha": "614a6762a240a0f89f5ab991174544ff3d38bde3",
    "commit": "46f127c7153f5393dcd2a00f42d4c1d3662c294d",
    "encoding": "gzip-json",
    "restore_only": True
}]
ZERO_TRANSLATION_QUALIFICATIONS = [{
    "role": "H_transport_source",
    "function": "initial_state",
    "source": "def initial_state(root,N):\n    state=[(Fraction(0),Fraction(0)) for _ in range(2*N+1)]\n    a=list(map(Fraction,root['exact_H_sine_coefficients']))\n    b=list(map(Fraction,root['exact_H_cosine_coefficients']))\n    for j,(s,c) in enumerate(zip(a,b),1):\n        state[N+j]=(c/2,-s/2);state[N-j]=(c/2,s/2)\n    return [list(state),list(state)]\n"
}, {
    "role": "K_source",
    "function": "trig_norm",
    "source": "def trig_norm(sines, cosines, width, derivative=0):\n    return sum(((exact_arb(a)**2 + exact_arb(b)**2).sqrt()\n                * (4*j)**derivative * (4*j*width).exp()\n                for j, (a, b) in enumerate(zip(sines, cosines), 1)), arb(0)).upper()\n"
}, {
    "role": "K_source",
    "function": "propose",
    "source": "def propose(state, modes, grid, omega):\n    N = (len(state[0])-1)//2\n    x = np.arange(grid, dtype=float) * (np.pi/(2*grid))\n    values = []\n    for side in state:\n        w = np.full(grid, float(side[N][0]))\n        for j in range(1, N+1):\n            a, b = side[N+j]\n            w += 2*(float(a)*np.cos(4*j*x)-float(b)*np.sin(4*j*x))\n        values.append(w)\n    ap, am = x+values[0], x+values[1]\n    columns = [np.sin(4*j*am)-np.sin(4*j*ap) for j in range(1, modes+1)]\n    columns += [np.cos(4*j*am)-np.cos(4*j*ap) for j in range(1, modes+1)]\n    columns += [-np.ones(grid)]\n    matrix = np.stack(columns, axis=1)\n    answer, _, rank, singular = np.linalg.lstsq(\n        matrix, -(values[1]-values[0]-float(omega)), rcond=None)\n    if rank != 2*modes+1 or not np.isfinite(answer).all():\n        raise ArithmeticError(\"the proposed terminal fit is rank deficient or nonfinite\")\n    a = [Fraction(float(z)) for z in answer[:modes]]\n    b = [Fraction(float(z)) for z in answer[modes:2*modes]]\n    proposed = omega + Fraction(float(answer[-1]))\n    return a, b, proposed, dict(\n        method=\"binary64 sampled least squares, used only to choose exact dyadic coefficients\",\n        grid=grid, rank=int(rank), smallest_singular_value=float(singular[-1]),\n        sampled_residual_not_used_as_a_bound=True)\n"
}]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def all_gates(document, expected, label):
    gates = document["gates"]
    require(document["complete"] is True and len(gates) == expected
            and all(type(item["passed"]) is bool and item["passed"] for item in gates),
            "complete original "+label+" gates")


def old_pin(manifest, spec):
    pins = manifest["files"]
    if isinstance(pins, dict):
        require(pins[spec["path"]] == spec["sha256"], "whole old manifest pin")
    else:
        found = [item for item in pins if item["path"] == spec["path"]]
        require(len(found) == 1 and found[0]["sha256"] == spec["sha256"],
                "unique complete old manifest pin: "+spec["role"])
        if "bytes" in found[0]:
            require(found[0]["bytes"] == spec["bytes"], "old whole input byte size")


def publication_record(publication, relative, spec):
    found = [item for item in publication["files"] if item["file"] == relative]
    require(len(found) == 1 and found[0]["sha256"] == spec["sha256"]
            and found[0]["bytes"] == spec["bytes"]
            and found[0]["original_sha256"] == spec["sha256"],
            "complete original published file receipt: "+relative)


def qualify_zero_translations(contents):
    # Parse the complete old sources; never import or execute an old producer.
    # The exact initial H has a zero central slot. The complete K definition
    # contains only j>=1 sine/cosine modes; proposed is a separate rotation.
    for item in ZERO_TRANSLATION_QUALIFICATIONS:
        tree = ast.parse(contents[item["role"]].decode("utf-8"))
        functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                     and node.name == item["function"]]
        expected = ast.parse(item["source"]).body
        require(len(functions) == len(expected) == 1
                and ast.dump(functions[0], include_attributes=False)
                    == ast.dump(expected[0], include_attributes=False),
                "full original zero-translation definition: "+item["function"])
    return {"H_constant": "0", "K_constant": "0",
            "H_source_function": "initial_state; all central slots initially exactly zero",
            "K_source_functions": ["trig_norm", "propose"],
            "terminal_rotation_is_not_a_K_constant_translation": True,
            "original_source_bytes_and_complete_AST_checked": True}


def admit_complete_inputs(contents, specs):
    require(set(specs) == set(FIXED_INPUTS) | {"science", "worker", "generator"}
                | {item["role"] for item in HISTORICAL_INPUTS}
            and set(contents) == set(specs), "all current and original native input roles")
    expected = dict(FIXED_INPUTS)
    expected.update({item["role"]: item for item in HISTORICAL_INPUTS})
    for role, spec in expected.items():
        require(specs[role] == spec, "same immutable complete input: "+role)
    for role, spec in specs.items():
        raw = contents[role]
        require(type(raw) is bytes and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole original byte identity: "+role)
        if role not in {item["role"] for item in HISTORICAL_INPUTS}:
            require(0 < len(raw) < 100000, "complete small current text input")
            raw.decode("utf-8")
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode("utf-8"), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH,
            "exact current source paths")
    native = {}
    for item in HISTORICAL_INPUTS:
        decoded = gzip.decompress(contents[item["role"]])
        require(0 < len(decoded) < 1000000, "complete original native JSON size")
        native[item["role"]] = parse(decoded)
    w, r31, post, root = (native[name] for name in
                           ("W_native", "R31_native", "K_native", "H_native"))
    wp, wm, wpub, np, nm, npub, wa, we, wam = (
        parse(contents[name]) for name in
        ("W_process", "W_manifest", "W_publication", "nine_process",
         "nine_manifest", "nine_publication", "WTA_actual", "WTA_execution", "WTA_manifest"))

    require(wp["kind"] == "actual_public_completed_R31_strip_refinement_execution"
            and wp["repository"] == REPO and wp["run_id"] == "43588332723"
            and wp["run_attempt"] == "1" and wp["complete"] is True
            and wp["actual_returncode"] == 0
            and wp["source_sha256"] == specs["W_driver"]["sha256"]
            and wp["mathematical_source_sha256"] == specs["W_source"]["sha256"]
            and wp["manifest_sha256"] == specs["W_manifest"]["sha256"]
            and wp["native_sha256"] == specs["W_native"]["sha256"]
            and wp["original_transport_postcomposition_and_R31_not_recomputed"] is True,
            "whole actual W execution and original mathematical source")
    require(wm["kind"] == "complete_public_R31_physical_strip_consumer_inputs"
            and wm["public_repository"] == REPO
            and wm["original_completed_public_run"] == 43586895661
            and wm["original_transport_postcomposition_and_R31_not_recomputed"] is True,
            "whole original W input manifest")
    for role in ("H_native", "R31_native", "K_native", "H_transport_source",
                 "K_source", "R31_source", "W_source", "W_driver", "nine_driver"):
        old_pin(wm, specs[role])
    require(wm["input_paths"] == {
                "R31": specs["R31_native"]["path"],
                "postcomposition": specs["K_native"]["path"],
                "root_contract": specs["H_native"]["path"]},
            "all three actual W argument objects")
    require(wpub["repository"] == REPO and wpub["run_id"] == "43588332723"
            and wpub["complete"] is True and wpub["actual_returncode"] == 0,
            "complete old W publication")
    publication_record(wpub, "consumers/R31-strip-refinement.json.gz", specs["W_native"])
    publication_record(wpub, "consumers/process.json", specs["W_process"])

    require(np["kind"] == "actual_public_Actions_small_phase_consumer_DAG"
            and np["repository"] == REPO and np["run_id"] == "43586895661"
            and np["run_attempt"] == "1" and np["complete"] is True
            and np["manifest_sha256"] == specs["nine_manifest"]["sha256"]
            and np["source_sha256"] == specs["nine_driver"]["sha256"]
            and np["original127_and_public_remaining42_not_recomputed"] is True,
            "complete original nine-step R31/K48 execution")
    step_names = ["wiener", "actual_twist", "proposal48", "post48", "K48_row",
                  "response_contract", "target15", "sharp_twist", "R31"]
    require([item["name"] for item in np["steps"]] == step_names
            and all(item["exit_code"] == 0 for item in np["steps"]),
            "every original DAG step really completed")
    for name, native_role, source_role in (("post48", "K_native", "K_source"),
                                         ("R31", "R31_native", "R31_source")):
        step = next(item for item in np["steps"] if item["name"] == name)
        require(step["native_sha256"] == specs[native_role]["sha256"]
                and step["mathematical_source_sha256"] == specs[source_role]["sha256"],
                "original same source and whole native: "+name)
    require(nm["kind"] == "pinned_public_Actions_complete_phase_small_consumer_DAG_inputs"
            and nm["public_repository"] == REPO
            and nm["input_paths"]["root_contract"] == specs["H_native"]["path"],
            "original complete R31 input manifest")
    for role in ("H_native", "H_transport_source", "K_source", "R31_source", "nine_driver"):
        old_pin(nm, specs[role])
    require(npub["repository"] == REPO and npub["run_id"] == "43586895661"
            and npub["complete"] is True and npub["actual_returncode"] == 0,
            "complete original R31/K48 publication")
    for filename, role in (("post48.json.gz", "K_native"), ("R31.json.gz", "R31_native"),
                           ("process.json", "nine_process")):
        publication_record(npub, "consumers/"+filename, specs[role])

    all_gates(root, 10, "finite H24 root-contract")
    require(root["kind"] == "actual_final_complete_phase_root_sliver_and_residual_contract"
            and root["source_sha256"] == specs["H_source"]["sha256"]
            and root["derived_definition_sha256"] == PARAMETERS["continuous_centre_definition_sha256"]
            and root["whole_original_eta"] is True
            and Fraction(root["exact_nu"]) == Fraction(PARAMETERS["exact_nu_centre"])
            and len(root["exact_H_sine_coefficients"]) == len(root["exact_H_cosine_coefficients"]) == 24,
            "full same-centre original finite H24 and independent terminal rotation")
    all_gates(post, 6, "whole terminal K48")
    require(post["kind"] == "actual_full_Laurent_terminal_postcomposition_certificate"
            and post["source_sha256"] == specs["K_source"]["sha256"]
            and post["original_producer_sha256"] == specs["H_transport_source"]["sha256"]
            and post["root_contract_sha256"] == specs["H_native"]["sha256"]
            and post["whole_negative_domain"] is True
            and post["scalar_cache_and_transport_reference_not_recomputed"] is True
            and post["all_complete_unprojected_frequencies_and_even_mean_retained"] is True
            and len(post["exact_postcomposition_sine_coefficients"])
                == len(post["exact_postcomposition_cosine_coefficients"]) == 48,
            "whole same original K48 map, both coefficient lists and mean scope")
    all_gates(r31, 11, "selected explicit family R31")
    require(r31["kind"] == "actual_complete_explicit_family_R31_parameter_circle_certificate"
            and r31["source_sha256"] == specs["R31_source"]["sha256"]
            and r31["inputs"]["root-contract"]["sha256"] == specs["H_native"]["sha256"]
            and r31["inputs"]["postcomposition"]["sha256"] == specs["K_native"]["sha256"]
            and r31["exact_family"] == "F_delta(x)=4G(P_delta(G^{-1}(x/4))); Q_delta=Qbar+delta Z, nu_delta=nu0+delta"
            and r31["actual_affine_parameter"] == PARAMETERS["fixed_intrinsic_parameter"]
            and r31["exact_affine_offset"] == "0" and r31["initial_lift"] == "identity"
            and Fraction(r31["original_nu"]) == Fraction(PARAMETERS["exact_nu_centre"])
            and r31["exact_parameter_radius"] == "1/100000000"
            and r31["R0"] == "1" and r31["sigma0"] == "1/20" and r31["circle_K"] == "17/4"
            and r31["all_complete_modes_and_even_means_and_true_root_retained"] is True
            and r31["genuine_PDE_solution_branch_or_full_body_inverse_claimed"] is False,
            "whole selected explicit family, same parameter and exact G composition")
    require(w["kind"] == "actual_public_R31_smaller_loss_and_physical_conjugacy_strip"
            and w["complete"] is True and w["source_sha256"] == specs["W_source"]["sha256"]
            and w["R31_native_sha256"] == specs["R31_native"]["sha256"]
            and w["postcomposition_native_sha256"] == specs["K_native"]["sha256"]
            and w["root_contract_sha256"] == specs["H_native"]["sha256"]
            and w["public_run_id"] == "43588332723" and w["public_run_attempt"] == "1"
            and w["physical_requested_strip"] == PARAMETERS["original_conjugacy_strip"]
            and w["true_explicit_family_parameter_conjugacy_proved"] is True
            and w["physical_true_conjugacy_strip_proved"] is True
            and w["circle_homological_K"] == "17/4",
            "the entire original W selected physical-strip conclusion")
    losses = ["3/200", "1/100", "3/400", "1/200", "1/250", "7/2000", "3/1000", "1/400"]
    require([item["exact_loss"] for item in w["all_actual_loss_trials"]] == losses,
            "all original successful and unsuccessful W losses retained")
    chosen = w["selected"]
    require(chosen == next(item for item in w["all_actual_loss_trials"]
                           if item["exact_loss"] == PARAMETERS["original_selected_loss"])
            and chosen["actual_R31_gates_passed"] is True
            and chosen["physical_conjugacy_A1over128_proved"] is True
            and w["original_genuine_PDE_branch_or_full_body_inverse_claimed"] is False
            and w["first_scalar_phase_and_strong_operator_remainder_not_paid"] is True,
            "exact same selected loss; no invented numerical point or PDE inverse")

    all_gates(wa, 20, "fixed-cutoff complete waist normalizer")
    require(wa["kind"] == "actual_waist_normalizer_coefficients_and_two_window_gates_v1"
            and wa["proved"] is True and wa["actual_returncode"] == 0 and wa["failure"] is None
            and wa["public_repository"] == REPO and wa["run_id"] == "43763134339"
            and wa["run_attempt"] == "1" and wa["arithmetic_bits"] == 320
            and wa["source_sha256"] == specs["WTA_source"]["sha256"]
            and wa["input_manifest_sha256"] == specs["WTA_manifest"]["sha256"]
            and wa["parameters"] == wam["parameters"] and wa["input_sha256"] == wam["mathematical_input_sha256"]
            and wam["source_sha256"] == specs["WTA_source"]["sha256"]
            and wam["expected_actual_gate_count"] == 20,
            "whole unchanged WTA science and manifest")
    old_pin(wam, specs["WTA_source"])
    require(we["complete"] is True and we["actual_returncode"] == 0
            and we["actual_failure"] is None and we["repository"] == REPO
            and we["run_id"] == "43763134339" and we["run_attempt"] == "1"
            and we["source_sha256"] == specs["WTA_source"]["sha256"]
            and we["input_manifest_sha256"] == specs["WTA_manifest"]["sha256"],
            "whole actual WTA execution")
    receipt = we["scientific_conclusion"]
    require(receipt["file"] == "actual-scientific-conclusion.json"
            and receipt["sha256"] == specs["WTA_actual"]["sha256"]
            and receipt["bytes"] == specs["WTA_actual"]["bytes"]
            and receipt["complete"] is True and receipt["actual_returncode"] == 0
            and receipt["actual_gate_count"] == receipt["actual_passed_gate_count"] == 20
            and any(item["file"] == receipt["file"] and item["bytes"] == receipt["bytes"]
                    and item["sha256"] == receipt["sha256"] for item in we["output_hashes"]),
            "complete actual WTA output linked to this entire result")
    family = wa["copied_SP_family_identity"]
    wp0 = wa["parameters"]
    require(family["continuous_centre_definition_sha256"] == PARAMETERS["continuous_centre_definition_sha256"]
            and family["continuous_response_definition_sha256"] == PARAMETERS["continuous_direction_definition_sha256"]
            and family["exact_alpha"] == PARAMETERS["exact_alpha"]
            and family["exact_nu_centre"] == PARAMETERS["exact_nu_centre"]
            and family["fixed_current_eta"] == PARAMETERS["fixed_intrinsic_parameter"]
            and family["original_candidate_sha256"] == root["candidate_sha256"]
            and wp0["fixed_test_cutoffs"] == [97, PARAMETERS["fixed_original_waist_normalizer_cutoff"]]
            and wp0["physical_frequency_factor"] == 4 and wp0["independent_mean_coordinates"] == 2
            and wp0["exact_delta_half_width"] == r31["exact_parameter_radius"],
            "same full selected repaired family and both normalizer means")
    require([item["J"] for item in wa["complete_fixed_cutoff_results"]]
                == wp0["fixed_test_cutoffs"]
            and wa["new_coefficient_scope"]["all_true_means_retained"] is True
            and wa["old_source_or_integral_calls"] == 0
            and wa["original_numerical_enclosures_recomputed"] == 0,
            "all original fixed results retained without repeating old targets")
    fixed = next(item for item in wa["complete_fixed_cutoff_results"]
                 if item["J"] == PARAMETERS["fixed_original_waist_normalizer_cutoff"])
    require(fixed["inverse_on_both_windows_proved"] is True
            and fixed["finite_complement_and_two_means_identity"] is True
            and fixed["strict_tests_total"] == fixed["strict_tests_passed"] == 4
            and len(fixed["all_four_strict_tests"]) == 4
            and all(item["passed"] is True for item in fixed["all_four_strict_tests"]),
            "the original fixed Js inverse; the independent dyadic result is not substituted")

    zeros = qualify_zero_translations(contents)
    Hs, Hc = ([str(Fraction(value)) for value in root[name]] for name in
              ("exact_H_sine_coefficients", "exact_H_cosine_coefficients"))
    Ks, Kc = ([str(Fraction(value)) for value in post[name]] for name in
              ("exact_postcomposition_sine_coefficients", "exact_postcomposition_cosine_coefficients"))
    # These are exact rational metadata checks, never new numerical enclosures.
    require(2*PARAMETERS["trial_fourier_cutoff"] < PARAMETERS["grid_points"]
            and PARAMETERS["trial_fourier_cutoff"] < fixed["J"]
            and all(Fraction(value).denominator > 0 for values in (Hs, Hc, Ks, Kc) for value in values),
            "complete exact input coefficients and finite/alias separation")
    return {"W": w, "chosen": chosen, "family": family, "fixed": fixed,
            "H_sines": Hs, "H_cosines": Hc, "K_sines": Ks, "K_cosines": Kc,
            "zero_translation_qualification": zeros}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one declared new numerical target in the authorized public Actions")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "complete pinned row-input manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS
            and manifest["complete_record_counts"] == [96]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS
            and manifest["historical_inputs"] == HISTORICAL_INPUTS,
            "the complete fixed new row target")
    all_specs = manifest["files"]+manifest["historical_inputs"]
    specs = {item["role"]: item for item in all_specs}
    require(len(specs) == len(all_specs), "unique complete current and historical inputs")
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "whole materialized input closure")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the running owner is the exact pinned current mathematical source")
    prior = admit_complete_inputs(contents, specs)
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole metadata admission precedes numerical imports")
    require(not args.output.exists(), "a previous numerical prefix is never overwritten")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    private = args.output.parent/"private-complete-row-carriers"
    private.mkdir(exist_ok=False)
    definition = {
        "formula": "RW.14 exact L-point DFT, truncated to k=-N..N",
        "input_H_contract_sha256": specs["H_native"]["sha256"],
        "input_K48_native_sha256": specs["K_native"]["sha256"],
        "all_H24_and_K48_rational_coefficients_included": True,
        "explicit_constant_translations": copy.deepcopy(prior["zero_translation_qualification"]),
        "row_parameters": copy.deepcopy(ROW_PARAMETERS),
        "coefficient_carriers_are_enclosures_of_this_exact_trial": True,
        "midpoint_selection": False,
        "reflection_centre": "a=2*H_selected(0), not asserted zero",
        "exact_grid_endpoints": "G_odd(0)=0 and G_odd(pi/4)=pi/4",
        "incoming_density": "(P p_j,0;Pi p_j,0)",
        "physical_primitive_density": "(P p_j/2,P p_j/2;0,0)",
        "independent_density_mean_rows": ["(0,0;1,0)", "(0,0;0,1)"],
    }
    old_records = {
        "selected_H_minus_G": copy.deepcopy(prior["chosen"]["physical_true_conjugacy_minus_G_norm"]),
        "complete_G_periodic_norm": copy.deepcopy(prior["W"]["exact_G_periodic_norm"]),
        "fixed_Js_same_inverse_L2": copy.deepcopy(prior["fixed"]["same_inverse_two_window_bounds"]["L2"]),
    }
    document = {
        "identity": {
            "kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"],
            "row_math_sha256": specs["row_math"]["sha256"],
            "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"],
        },
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_original_conjugacy_and_fixed_normalizer_inputs_admitted",
        "parameters": copy.deepcopy(PARAMETERS),
        "reference_identity": copy.deepcopy(prior["family"]),
        "selected_member_identity": {
            "run": PARAMETERS["original_selected_run"],
            "loss": PARAMETERS["original_selected_loss"],
            "physical_strip": PARAMETERS["original_conjugacy_strip"],
            "whole_W_native_sha256": specs["W_native"]["sha256"],
            "selected_parameter_replaced_by_a_numeric_point": False,
            "true_reflection_centre_replaced_by_zero": False,
        },
        "exact_definition": definition, "definition_sha256": sha(canonical(definition)),
        "whole_completed_inputs": {role: copy.deepcopy(item) for role, item in specs.items()},
        "copied_prior_scalar_records": old_records,
        "runtime": {}, "wall_seconds": 0.0,
        "completed_targets": [], "saved_record_count": 0, "new_records": {},
        "current_target": None, "candidate_record": None, "pending_row": None,
        "private_grid_receipt": None, "private_complete_row_count": 0,
        "result": None, "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0,
    }
    require(sorted(document) == SCI_FIELDS, "complete exact row-result schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "one bounded new row target; preserve any whole prefix")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "whole row conclusion fits its declared public byte budget")
        atomic(args.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "fixed directed row runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb
        spec = importlib.util.spec_from_file_location("_R149_complete_reflected_rows", paths["row_math"])
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        require(module.PARAMETERS == ROW_PARAMETERS, "whole exact pure row parameters")

        def old_upper(record):
            require(type(record) is dict and "ball" in record, "entire old scalar record")
            if "lower" in record and "upper" in record:
                ball = arb(record["lower"]).lower().union(arb(record["upper"]).upper())
            else:
                ball = arb(record["ball"])
            require(ball.is_finite() and ball.lower() >= 0, "nonnegative old complete enclosure")
            return ball.upper()

        def public_ball(value, kind):
            require(value.is_finite() and kind in ("signed", "upper"), "whole finite new row scalar")
            point = value if kind == "signed" else value.upper()
            if kind == "upper":
                require(point >= 0, "directed nonnegative new upper")
            return {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": kind}, point

        def check_record(record, originals):
            for name, original in originals.items():
                value = arb(record[name]["ball"])
                require(value.is_finite() and value.contains(original),
                        "whole saved "+name+" includes its original directed ball")
            return record

        def private_carrier(filename, kind, values, extra):
            original = list(values)
            carrier = {"kind": kind, "definition_sha256": document["definition_sha256"],
                       **extra, "all_real_balls": [value.str(PARAMETERS["private_coefficient_digits"])
                                                 for value in original]}
            raw = canonical(carrier)
            target = private/filename
            atomic(target, raw)
            read_raw = target.read_bytes()
            require(read_raw == raw, "entire private carrier saved byte for byte")
            read = parse(read_raw)
            require(read == carrier and len(read["all_real_balls"]) == len(original),
                    "every declared private carrier coefficient retained")
            restored = [arb(value) for value in read["all_real_balls"]]
            require(all(value.is_finite() and value.contains(old)
                        for value, old in zip(restored, original)),
                    "all complete private-carrier balls survive whole readback")
            return restored, {"bytes": len(raw), "sha256": sha(raw),
                              "complete_real_count": len(original)}

        eh = old_upper(old_records["selected_H_minus_G"])
        g0 = old_upper(old_records["complete_G_periodic_norm"])
        kw = old_upper(old_records["fixed_Js_same_inverse_L2"])
        factory = module.ReflectedRowFactory(flint, prior["H_sines"], prior["H_cosines"],
            prior["K_sines"], prior["K_cosines"],
            H_constant=prior["zero_translation_qualification"]["H_constant"],
            K_constant=prior["zero_translation_qualification"]["K_constant"])
        grid = factory.materialize_whole_compound_grid()
        saved_grid, grid_receipt = private_carrier("whole-compound-cosine-grid.json",
            "R149_complete_exact_compound_cosine_grid_carrier_v1", grid,
            {"grid_points": PARAMETERS["grid_points"]})
        # The same exact samples remain enclosed after serialization. Use the
        # saved carrier as the only numerical grid input to every declared row.
        factory.base_cosines = saved_grid
        factory.previous = [arb(1) for value in saved_grid]
        factory.current = list(saved_grid)
        document["private_grid_receipt"] = grid_receipt
        document["stage"] = "whole_compound_grid_saved_and_read_back"
        save()

        for name in TARGETS:
            require(document["current_target"] is None and document["pending_row"] is None
                    and document["candidate_record"] is None,
                    "no new row starts over an unfinished mathematical prefix")
            j, coefficients = factory.next_complete_row()
            require(name == TARGETS[j-1] and j == document["saved_record_count"]+1,
                    "exactly the next declared complete reflected row")
            restored, receipt = private_carrier(name+".json",
                "R149_complete_exact_DFT_real_row_carrier_v1", coefficients,
                {"mode": j, "nonnegative_modes": [0, PARAMETERS["trial_fourier_cutoff"]],
                 "negative_modes": "equal by exact evenness, not selected by midpoint"})
            document["private_complete_row_count"] += 1
            document["current_target"] = name
            base = {"mode": j, "carrier": receipt}
            originals = {}
            base["mean"], originals["mean"] = public_ball(restored[0], "signed")
            base["trial_l2"], originals["trial_l2"] = public_ball(
                module.complete_trial_l2_upper(flint, restored), "upper")
            base["compound_error"], originals["compound_error"] = public_ball(
                module.compound_row_error_upper(flint, j, eh, g0), "upper")
            # First save and verify all three independent new scalars.
            document["candidate_record"] = {"name": name, "phase": "base", "record": base}
            document["stage"] = "whole_new_row_base_candidate_saved"
            save()
            candidate = parse(args.output.read_bytes())["candidate_record"]
            require(candidate == {"name": name, "phase": "base", "record": base},
                    "whole exact base candidate readback")
            check_record(candidate["record"], originals)
            document["pending_row"] = copy.deepcopy(candidate["record"])
            document["candidate_record"] = None
            document["stage"] = "formal_base_row_components_saved"
            save()
            pending = parse(args.output.read_bytes())["pending_row"]
            require(pending == base, "identical formally saved independent row components")
            check_record(pending, originals)
            epsilon = arb(pending["compound_error"]["ball"]).upper()
            full = copy.deepcopy(pending)
            full["incoming_error"], originals["incoming_error"] = public_ball(
                module.incoming_row_error_upper(flint, epsilon, kw), "upper")
            full["physical_error"], originals["physical_error"] = public_ball(
                module.physical_primitive_row_error_upper(flint, epsilon), "upper")
            # These two dependent bounds use the formal saved epsilon upper.
            document["candidate_record"] = {"name": name, "phase": "complete", "record": full}
            document["stage"] = "whole_complete_row_candidate_saved"
            save()
            candidate = parse(args.output.read_bytes())["candidate_record"]
            require(candidate == {"name": name, "phase": "complete", "record": full},
                    "whole complete row candidate readback")
            check_record(candidate["record"], originals)
            require(candidate["record"]["carrier"]["complete_real_count"]
                    == PARAMETERS["trial_fourier_cutoff"]+1,
                    "the candidate is backed by the complete private row")
            document["new_records"][name] = copy.deepcopy(candidate["record"])
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = None
            document["pending_row"] = None
            document["current_target"] = None
            document["stage"] = "complete_reflected_row_saved"
            save()
            formal = parse(args.output.read_bytes())["new_records"][name]
            require(formal == full, "formal complete row retains all verified fields")
            check_record(formal, originals)
            print("COMPLETE_NEW_ROW "+name+" "+canonical(formal).decode("utf-8"), end="", flush=True)

        require(document["completed_targets"] == TARGETS
                and document["saved_record_count"] == document["private_complete_row_count"] == 96
                and factory.next_row == 97
                and document["candidate_record"] is document["pending_row"] is document["current_target"] is None,
                "all 96 declared rows and every complete private carrier finished")
        document["result"] = {
            "kind": KIND, "complete_new_record_count": 96,
            "complete_new_record_order": list(TARGETS),
            "complete_private_row_carriers": 96, "real_coefficients_per_row": 1025,
            "small_scalar_records_per_row": 5, "complete_small_scalar_count": 480,
            "complete_compound_grid_points": 4096,
            "incoming_declared_cosine_rows": 96, "original_physical_primitive_rows": 96,
            "independent_density_mean_rows": 2, "independent_density_mean_norm_exact": "1",
            "signed_row_mean_retained": True,
            "all_DFT_alias_and_infinite_compound_tails_paid": True,
            "old_H_minus_G_error_paid_once_by_odd_projection": True,
            "fixed_Js_finite_complement_and_its_adjoint_identity_used": True,
            "both_dependent_bounds_use_formal_saved_compound_upper": True,
            "whole_private_grid_and_rows_saved_and_read_back": True,
            "exact_trial_is_original_DFT_not_a_midpoint": True,
            "complete_B_inverse_or_Theta_rows_proved": False,
            "rotated_outgoing_rows_included": False,
            "signed_PDE_columns_or_finite_inverse_proved": False,
            "complete_incoming_inverse_proved": False,
            "full_nu_phase_mean_Schur_proved": False,
            "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_reflected_row_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:2000],
                               "traceback": traceback.format_exc()[-8000:]}
        print(traceback.format_exc(), flush=True)
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
