"""TCXV: original all-source cells with exact-zero vector checkpoint repair.

Admit the entire actually ended TCX predecessor and its truthful verified
SkylakeX input restoration. All eight numerical sources and the complete
original cell body are unchanged. Old accepted cells are never evaluated.
"""
from pathlib import Path
import hashlib
import importlib.util

TCX_OWNER_NAME = "fourfold_codazzi_true_root_parallel_trial_owner.py"
TCX_OWNER_PATH = "topics/visible-flex-exact-nearby/scripts/"+TCX_OWNER_NAME
TCX_OWNER_BYTES = 12756
TCX_OWNER_SHA256 = "3c10e359e6f7687a8a4500c8d845fde4b4cfd5e8028766eb72218f6f77bb1b10"
path = Path(__file__).with_name(TCX_OWNER_NAME)
raw = path.read_bytes()
if len(raw) != TCX_OWNER_BYTES or hashlib.sha256(raw).hexdigest() != TCX_OWNER_SHA256:
    raise ValueError("the entire original parallel owner is an immutable actual input")
spec = importlib.util.spec_from_file_location("_TCXV_original_parallel_owner", path)
_original_TCX = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_original_TCX)
for name in ("BASE_NAME", "BASE_BYTES", "BASE_SHA256", "BASE_PATH", "CONT_NAME",
             "CONT_BYTES", "CONT_SHA256", "CONT_PATH", "TCX_CONTRACT", "PARALLEL_KEY"):
    globals()[name] = getattr(_original_TCX, name)
ADAPTER_PATH = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"
PARALLEL_NAME = "fourfold_codazzi_true_root_parallel_vector_slices.py"
PARALLEL_PATH = "topics/visible-flex-exact-nearby/scripts/"+PARALLEL_NAME
VERIFIED_RUNTIME = {"CORETYPE": "SkylakeX", "TC_scientific_parameters_changed": False,
    "actual_bytes": 13467, "actual_sha256": "e60132d11b0fec9ef70257d5237f05b52b59c1037446764c78f7ed7665803d3f",
    "execution_bytes": 11662, "execution_sha256": "95ba072a52abadbb9047faf2820dcc7437b8d5cf901ed59e29d36abea694f102",
    "kind": "TC_verified_original_Hermite_runtime_v1", "original_TC_trial_CORETYPE": "Haswell",
    "original_historical_CORETYPE": "unset", "run_attempt": "1", "run_id": "45924740082",
    "same_original_cubic_and_all14_shards": True}


def _TCXV_whole_original_runtime(execution, result, contract, previous_manifest):
    require(result["original_container"] == contract["original_container"]
            and result["runtime"] == contract["original_runtime"],
            "the original whole container, Python and every package remain fixed")
    if "verified_runtime" not in contract:
        return (result["reconstruction_OPENBLAS_CORETYPE"]
                == contract["original_reconstruction_OPENBLAS_CORETYPE"] == "unset")
    require(contract["verified_runtime"] == VERIFIED_RUNTIME
            and result["verified_runtime_contract"] == VERIFIED_RUNTIME
            and result["reconstruction_OPENBLAS_CORETYPE"] == "SkylakeX"
            and result["original_historical_reconstruction_OPENBLAS_CORETYPE"]
                == contract["original_reconstruction_OPENBLAS_CORETYPE"] == "unset",
            "truthful separate historical-unset and actually verified-SkylakeX identities")
    expected = {
        "verified_runtime_actual": (13467, VERIFIED_RUNTIME["actual_sha256"]),
        "verified_runtime_execution": (11662, VERIFIED_RUNTIME["execution_sha256"]),
        "verified_runtime_manifest": (90787, "0789f442e26f02644f7e958d9fa11db249a4063a6946c3b57c3f3f5f54bb62cd"),
    }
    for role, (size, sha) in expected.items():
        matches = [item for item in previous_manifest["files"]
                   if item["path"] == previous_manifest["roles"][role]]
        require(len(matches) == 1 and matches[0]["bytes"] == size and matches[0]["sha256"] == sha,
                "the preceding whole manifest retains the entire actual runtime proof")
    dispatch = result["actual_readonly_dispatch"]
    flags = set(dispatch["cpu"].get("flags", "").split())
    require(dispatch["OPENBLAS_CORETYPE"] == "SkylakeX"
            and dispatch["actual_BLAS_core_lines"] == ["SkylakeX"]
            and {"avx512f", "avx512dq", "avx512bw", "avx512vl"}.issubset(flags)
            and execution["necessary_runtime_CPU_admission"]["actual_AVX512F_DQ_BW_VL_present"] is True
            and execution["necessary_runtime_CPU_admission"]["known_failed_Haswell_replayed"] is False,
            "the actual preceding producer really selected the supported verified core")
    return True


def patched_source():
    source = _original_TCX.patched_source()
    replacements = (
        ('SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"',
         'SOURCE_PATH = TOPIC+"scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"'),
        ('previous["owner"] in (BASE_SHA256,CONT_SHA256,here)',
         'previous["owner"] in (BASE_SHA256,CONT_SHA256,TCX_OWNER_SHA256,here)'),
        ('    choices = {BASE_PATH:original,CONT_PATH:continuation,ADAPTER_PATH:current}\n',
         '''    parallel_previous = roles["original_TCX_owner"]
    require(parallel_previous["path"] == TCX_OWNER_PATH
            and parallel_previous["bytes"] == TCX_OWNER_BYTES
            and parallel_previous["sha256"] == TCX_OWNER_SHA256,
            "the previous entire parallel owner is separately retained")
    choices = {BASE_PATH:original,CONT_PATH:continuation,TCX_OWNER_PATH:parallel_previous,ADAPTER_PATH:current}
'''),
        ('''    require(result["original_container"] == contract["original_container"]
            and result["reconstruction_OPENBLAS_CORETYPE"]
                == contract["original_reconstruction_OPENBLAS_CORETYPE"] == "unset"
            and result["runtime"] == contract["original_runtime"],
            "the same explicitly pinned original Hermite runtime")
''',
         '''    require(_TCXV_whole_original_runtime(execution,result,contract,previous_manifest),
            "the whole original runtime or its whole actually verified same-byte restoration")
'''),
        ('            and execution["scientific_started_utc"]\n',
         '            and execution["scientific_started_utc"]\n'
         '            and execution["scientific_finished_utc"] and execution["finished_utc"]\n'),
    )
    for old, new in replacements:
        expected = 2 if old == '            and execution["scientific_started_utc"]\n' else 1
        if source.count(old) != expected:
            raise ValueError("the exact TCXV whole-source adaptation did not match: "+old)
        source = source.replace(old, new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
