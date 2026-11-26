"""TC continuation adapter: fix ONLY complete predecessor metadata admission.

The original running owner remains unchanged. This adapter byte-pins that
entire source, changes only explicit predecessor-qualification predicates,
and retains its parameters, trial choice, all full array SHA checks, signed
matrices, residual integrands, exact partition, accumulators and stopping
logic. A completed target is inherited verbatim and never recomputed.
"""
from pathlib import Path
import hashlib
import re

BASE_NAME = "fourfold_codazzi_true_root_trial_owner.py"
BASE_SHA256 = "193a317166204eef3870f12e5aee08be5a3de46e18b65de4b471b2a478f253dc"
BASE_BYTES = 63363
BASE_PATH = "topics/visible-flex-exact-nearby/scripts/"+BASE_NAME
ADAPTER_PATH = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_continuation_owner.py"

METADATA_ADMISSION = '''
def _same_complete_scientific_sources(previous,current):
    """Exactly eight original numerical sources; only this metadata adapter differs."""
    names = {"owner","trial_math","proposal_math","inputs_math","box_math","fft_math",
             "candidate_reader","repair_source","direction_source"}
    require(set(previous) == set(current) == names,
            "all nine whole original scientific source identities")
    here = digest(Path(__file__).read_bytes())
    return (current["owner"] == here
            and previous["owner"] in (BASE_SHA256,here)
            and all(previous[name] == current[name] for name in names-{"owner"}))


def _same_complete_owner_manifest(previous_manifest,roles):
    """The old actual owner remains pinned, rather than relabelled as this file."""
    current = roles["owner"]
    original = roles["original_TC_owner"]
    here = Path(__file__).read_bytes()
    require(current["path"] == ADAPTER_PATH and current["sha256"] == digest(here)
            and current["bytes"] == len(here)
            and original["path"] == BASE_PATH and original["bytes"] == BASE_BYTES
            and original["sha256"] == BASE_SHA256,
            "complete current adapter and immutable original owner source")
    old_path = previous_manifest["roles"]["owner"]
    matches = [spec for spec in previous_manifest["files"] if spec["path"] == old_path]
    require(len(matches) == 1, "one whole exact original predecessor owner")
    expected = original if old_path == BASE_PATH else current
    return all(matches[0][key] == expected[key]
               for key in ("path","bytes","sha256","git_blob_sha"))


def _qualified_original_input_reconstruction(execution,previous_manifest):
    """One separately counted original Hermite input restoration, zero old targets."""
    contract = previous_manifest["input_restoration"]
    result = execution.get("necessary_input_reconstruction")
    require(isinstance(result,dict)
            and contract["kind"] == "TC_exact_original_Git_rows_and_nodal_Hermite_v1"
            and contract["expected_cubic_pieces"] == 6144
            and contract["expected_direction_shards"] == 14
            and contract["old_QR_or_residual_or_norm_targets"] == 0
            and contract["new_array_publication"] is False
            and execution["old_numerical_producers_called"] == 1
            and execution["necessary_input_reconstruction_children"] == 1
            and result["necessary_input_reconstruction"] is True
            and result["complete"] is True and result["actual_returncode"] == 0
            and result["old_QR_solve_called"] is False
            and result["old_residual_or_norm_targets_called"] == 0
            and result["new_arrays_published"] == 0
            and result["whole_original_cubic_SHA_verified"] is True,
            "the separately counted producer is only a complete original input restoration")
    require(result["original_container"] == contract["original_container"]
            and result["reconstruction_OPENBLAS_CORETYPE"]
                == contract["original_reconstruction_OPENBLAS_CORETYPE"] == "unset"
            and result["runtime"] == contract["original_runtime"],
            "the same explicitly pinned original Hermite runtime")
    expected = [{key:spec[key] for key in ("path","bytes","sha256")}
                for spec in contract["generated_direction_inputs"]]
    require(len(expected) == 14
            and result["complete_direction_input_receipts"] == expected,
            "every entire original direction shard matched its unchanged full SHA")
    report = result["actual_report"]
    sources = [spec for spec in previous_manifest["files"]
               if spec["path"] == contract["reconstructor"]]
    require(len(sources) == 1
            and report["kind"] == "actual_same_regular_trial_from_original_nodal_answer_v1"
            and report["complete"] is True and report["failure"] is None
            and report["source_sha256"] == sources[0]["sha256"]
            and report["role"] == "response"
            and report["trial_piece_count"] == contract["expected_cubic_pieces"]
            and report["actual_reconstructed_cubic_sha256"]
                == report["expected_original_cubic_sha256"] == contract["original_cubic_sha256"]
            and report["original_answer_sha256"] == contract["original_nodal_answer_sha256"]
            and report["finite_QR_solve_reexecuted"] is False
            and report["actual_new_reconstruction_separate_from_historical_solve"] is True
            and report["historical_case_refers_to_original_nodal_solution"] is True
            and report["all_finite_mean_and_nonmean_columns_retained"] is True
            and report["all_original_one_sided_derivatives_reconstructed"] is True
            and report["all_original_shards_match"] is True,
            "the entire original reconstruction report includes cubic, all columns and one-sided derivatives")
    path = previous_manifest["roles"]["direction_index"]
    indices = [spec for spec in previous_manifest["historical_inputs"] if spec["path"] == path]
    require(len(indices) == 1
            and report["outputs"]["full"]["sha256"]
                == report["outputs"]["full"]["expected_sha256"] == indices[0]["sha256"],
            "the exact old whole direction index is also unchanged")
    require(execution["old_completed_targets_recomputed"] == 0
            and execution["new_arrays_published"] == execution["new_artifacts"] == execution["new_Releases"] == 0,
            "no old mathematical target or original public array was replayed")
    return True


'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("whole original running TC source changed")
    source = raw.decode()
    replacements = [
        ('SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_trial_owner.py"',
         'SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_trial_continuation_owner.py"', 1),
        ('previous["input_identity"]["scientific_sources"] == current_identity["scientific_sources"]',
         '_same_complete_scientific_sources(previous["input_identity"]["scientific_sources"],current_identity["scientific_sources"])', 1),
        ('previous["input_identity"]["scientific_sources"] == input_identity["scientific_sources"]',
         '_same_complete_scientific_sources(previous["input_identity"]["scientific_sources"],input_identity["scientific_sources"])', 1),
        ('prefix["scientific_sources"] == current_identity["scientific_sources"]',
         '_same_complete_scientific_sources(prefix["scientific_sources"],current_identity["scientific_sources"])', 1),
        ('prefix["scientific_sources"] == input_identity["scientific_sources"]',
         '_same_complete_scientific_sources(prefix["scientific_sources"],input_identity["scientific_sources"])', 1),
        ('execution["old_numerical_producers_called"] == 0',
         '_qualified_original_input_reconstruction(execution,old_manifest)', 2),
    ]
    for old, new, count in replacements:
        if source.count(old) != count:
            raise ValueError("the explicit TC metadata patch did not match: "+old)
        source = source.replace(old, new)
    owner_predicate = re.compile(
        r'old_manifest\["roles"\]\["owner"\] == roles\["owner"\]\["path"\]'
        r'\s+and any\(item\["path"\] == roles\["owner"\]\["path"\]'
        r' and item\["sha256"\] == roles\["owner"\]\["sha256"\]'
        r'\s+and item\["bytes"\] == roles\["owner"\]\["bytes"\]'
        r' for item in old_manifest\["files"\]\)')
    source, count = owner_predicate.subn('_same_complete_owner_manifest(old_manifest,roles)', source)
    if count != 2:
        raise ValueError("both entire old-owner metadata predicates must match exactly")
    location = source.index("def admit_prior_metadata(manifest,roles,raws,current_identity):\n")
    source = source[:location]+METADATA_ADMISSION+source[location:]
    return source


# Export the exact original owner with only the explicit metadata adapter.
# On import __name__ is not __main__, so its numerical main is not called.
exec(compile(patched_source(), __file__, "exec"), globals())
