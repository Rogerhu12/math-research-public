"""Restore only the original Z carrier with its actually verified BLAS core.

The original full restore module remains byte-pinned. Only the explicit
carrier-child environment and its truthful runtime receipt change. The
original nodal producer, full cubic/index/shard gates and TC science do not.
"""
from pathlib import Path
import hashlib
import importlib.util

BASE_NAME = "fourfold_codazzi_true_root_trial_restore.py"
BASE_BYTES = 13266
BASE_SHA256 = "c3ffe72b9234f84f59b0df5a12339c463bbab351f7ffc0fe3f0459882ec8988b"
ACTUAL_SHA256 = "e60132d11b0fec9ef70257d5237f05b52b59c1037446764c78f7ed7665803d3f"
EXECUTION_SHA256 = "95ba072a52abadbb9047faf2820dcc7437b8d5cf901ed59e29d36abea694f102"
CONTRACT = {"kind": "TC_verified_original_Hermite_runtime_v1", "run_id": "45924740082",
    "run_attempt": "1", "CORETYPE": "SkylakeX", "actual_bytes": 13467,
    "actual_sha256": ACTUAL_SHA256, "execution_bytes": 11662, "execution_sha256": EXECUTION_SHA256,
    "original_historical_CORETYPE": "unset", "same_original_cubic_and_all14_shards": True,
    "original_TC_trial_CORETYPE": "Haswell", "TC_scientific_parameters_changed": False}


def _TCVR_admit_actual(plan, inputs_root, roles):
    import json
    require(plan["verified_runtime"] == CONTRACT
            and plan["original_reconstruction_OPENBLAS_CORETYPE"] == "unset",
            "the original historical dispatch stays unchanged; the new verified dispatch is separate")
    def read(role, expected_bytes, expected_sha):
        spec = roles[role]
        raw = (Path(inputs_root)/spec["path"]).read_bytes()
        require(len(raw) == spec["bytes"] == expected_bytes
                and sha(raw) == spec["sha256"] == expected_sha,
                "the complete actually successful original carrier proof: "+role)
        return json.loads(raw)
    actual = read("verified_runtime_actual", 13467, ACTUAL_SHA256)
    execution = read("verified_runtime_execution", 11662, EXECUTION_SHA256)
    runtime_manifest = read("verified_runtime_manifest", 90787,
        "0789f442e26f02644f7e958d9fa11db249a4063a6946c3b57c3f3f5f54bb62cd")
    require(runtime_manifest["input_restoration"] == {k: v for k, v in plan.items() if k != "verified_runtime"}
            and actual["input_manifest_sha256"] == execution["manifest_sha256"]
                == "0789f442e26f02644f7e958d9fa11db249a4063a6946c3b57c3f3f5f54bb62cd",
            "the complete successful diagnostic used the identical original input recipe")
    require(actual["kind"] == "R149_input_only_original_nodal_runtime_identification_v1"
            and actual["complete"] is actual["proved"] is True and actual["failure"] is None
            and actual["run_id"] == "45924740082" and actual["run_attempt"] == "1"
            and actual["accepted_schedule"] == "SkylakeX"
            and actual["necessary_input_reconstruction_children"] == 1
            and actual["TC_scientific_children"] == actual["new_TC_integrated_cells"] == 0
            and len(actual["schedule_results"]) == 1
            and execution["complete"] is True and execution["failure"] is None
            and execution["run_id"] == "45924740082" and execution["run_attempt"] == "1"
            and execution["finished_utc"] is not None and execution["scientific_children"] == 0,
            "the whole genuinely ended one-producer input-only success")
    attempted = actual["schedule_results"][0]
    report = attempted["actual_report"]
    require(attempted["complete"] is attempted["original_whole_SHA_verified"] is True
            and attempted["actual_returncode"] == 0 and attempted["OPENBLAS_CORETYPE"] == "SkylakeX"
            and attempted["actual_selected_BLAS_cores"] == ["SkylakeX"]
            and report["complete"] is True and report["failure"] is None
            and report["finite_QR_solve_reexecuted"] is False
            and report["actual_reconstructed_cubic_sha256"] == plan["original_cubic_sha256"]
            and report["all_original_shards_match"] is True,
            "the verified dispatch restored the original cubic rather than a substitute")
    expected = [{key: item[key] for key in ("path", "bytes", "sha256")}
                for item in plan["generated_direction_inputs"]]
    require(len(expected) == 14 and actual["complete_original_carrier_receipts"] == expected,
            "every original full direction shard is bound by the successful whole result")
    return actual


def _TCVR_readonly_dispatch(inputs_root, environment, state):
    import json
    import subprocess
    import sys
    # No old producer is started until the actual assigned CPU has the
    # required instructions. No retry or fallback to the failed Haswell.
    actual_cpu = {}
    for line in Path('/proc/cpuinfo').read_text().split('\n\n', 1)[0].splitlines():
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            if key in ('vendor_id', 'cpu family', 'model', 'model name', 'stepping', 'flags'):
                actual_cpu[key] = value
    flags = set(actual_cpu.get('flags', '').split())
    supported = {'avx512f', 'avx512dq', 'avx512bw', 'avx512vl'}.issubset(flags)
    state["necessary_runtime_CPU_admission"] = {"cpu": actual_cpu,
        "actual_AVX512F_DQ_BW_VL_present": supported, "known_failed_Haswell_replayed": False}
    require(supported, "this actual runner lacks verified SkylakeX instructions; no old producer may run")
    code = '''import json, numpy as np
from pathlib import Path
cpu={}
for line in Path('/proc/cpuinfo').read_text().split('\\n\\n',1)[0].splitlines():
 if ':' in line:
  k,v=map(str.strip,line.split(':',1))
  if k in ('vendor_id','cpu family','model','model name','stepping','flags'):cpu[k]=v
print(json.dumps(dict(cpu=cpu,numpy_cpu_features={k:bool(v) for k,v in np._core._multiarray_umath.__cpu_features__.items()}),sort_keys=True,separators=(',',':')))
'''
    probe_environment = dict(environment, OPENBLAS_CORETYPE="SkylakeX", OPENBLAS_VERBOSE="2")
    observed = subprocess.run([sys.executable, "-c", code], cwd=Path(inputs_root)/TOPIC,
        env=probe_environment, capture_output=True, text=True, timeout=90)
    require(observed.returncode == 0, "the actual read-only verified-core probe completed")
    value = json.loads(observed.stdout)
    flags = set(value["cpu"].get("flags", "").split())
    require({"avx512f", "avx512dq", "avx512bw", "avx512vl"}.issubset(flags),
            "this actual runner lacks verified SkylakeX instructions; no old producer may run")
    cores = [line.split(":", 1)[1].strip() for line in observed.stderr.splitlines() if line.startswith("Core:")]
    require(cores == ["SkylakeX"], "the actual library selected the genuinely verified core")
    value["OPENBLAS_CORETYPE"], value["actual_BLAS_core_lines"] = "SkylakeX", cores
    value["actual_probe_stderr"] = observed.stderr
    return value


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the complete original restoration source changed")
    source = raw.decode()
    old = '''    require(plan["original_reconstruction_OPENBLAS_CORETYPE"] == "unset",
            "the original successful reconstruction did not force a BLAS core")
    environment.pop("OPENBLAS_CORETYPE",None)
'''
    new = '''    _TCVR_admit_actual(plan, inputs_root, roles)
    environment["OPENBLAS_CORETYPE"] = "SkylakeX"
    environment["OPENBLAS_VERBOSE"] = "2"
'''
    if source.count(old) != 1:
        raise ValueError("the one original environment-selection block changed")
    source = source.replace(old, new)
    old = '    record = dict(necessary_input_reconstruction=True,old_QR_solve_called=False,\n'
    new = '''    actual_dispatch = _TCVR_readonly_dispatch(inputs_root, environment, state)
    record = dict(necessary_input_reconstruction=True,old_QR_solve_called=False,
'''
    if source.count(old) != 1:
        raise ValueError("the original whole reconstruction receipt block changed")
    source = source.replace(old, new)
    old = '        reconstruction_OPENBLAS_CORETYPE="unset",\n'
    new = '''        reconstruction_OPENBLAS_CORETYPE="SkylakeX",
        original_historical_reconstruction_OPENBLAS_CORETYPE="unset",
        verified_runtime_contract=dict(CONTRACT),actual_readonly_dispatch=actual_dispatch,
'''
    if source.count(old) != 1:
        raise ValueError("the truthful actual dispatch receipt field changed")
    return source.replace(old, new)


exec(compile(patched_source(), __file__, "exec"), globals())
