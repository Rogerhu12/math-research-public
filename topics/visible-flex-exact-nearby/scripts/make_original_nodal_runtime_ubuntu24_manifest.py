"""A single declared Ubuntu24 input-only successor after actual zero-child AMD.

No model, producer or SHA condition changes. The original short generator
is retained whole; only the new actual predecessor and runner label differ.
"""
from pathlib import Path
import hashlib

BASE_NAME = "make_original_nodal_runtime_manifest.py"
BASE_BYTES = 8902
BASE_SHA256 = "e15798cf2aac474db3f0b5cc3b74de52c08e13120ef93b1e6072ef0f3b15fd38"


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the whole original input-only generator changed")
    code = raw.decode()
    changes = [
        ('GENERATOR = TOPIC+"/scripts/make_original_nodal_runtime_manifest.py"',
         'GENERATOR = TOPIC+"/scripts/make_original_nodal_runtime_ubuntu24_manifest.py"'),
        ('PROOF = TOPIC+"/notes/2026-11-27-TCX-zero-child-runtime-identification.md"',
         'PROOF = TOPIC+"/notes/2026-11-27-original-carrier-AMD-zero-child-and-ubuntu24.md"'),
        ('2026-11-27-original-nodal-runtime-identification-inputs.json',
         '2026-11-27-original-nodal-runtime-identification-ubuntu24-inputs.json'),
        ('fourfold-codazzi-original-nodal-runtime-identification-public.yml',
         'fourfold-codazzi-original-nodal-runtime-identification-ubuntu24-public.yml'),
        ('original-nodal-runtime-after-zero-child-TCX-45920124552',
         'original-nodal-runtime-ubuntu24-after-zero-child-45923136710'),
        ('consumed-after-45920124552.json', 'consumed-ubuntu24-after-45923136710.json'),
        ('visible-exact-original-nodal-runtime-20261127', 'visible-exact-original-nodal-runtime-ubuntu24-20261127'),
        ('name: R149 original nodal carrier runtime identification',
         'name: R149 original nodal carrier runtime identification on Ubuntu24'),
        ('runs-on: ubuntu-latest', 'runs-on: ubuntu-24.04'),
        ('    manifest = json.loads(parent_raw)\n', '''    previous_actual_path = TOPIC+"/notes/original_nodal_runtime_ci/run-45923136710-1/actual-original-nodal-runtime.json"
    previous_execution_path = TOPIC+"/notes/original_nodal_runtime_ci/run-45923136710-1/execution.json"
    previous_actual_raw = (root/previous_actual_path).read_bytes()
    previous_execution_raw = (root/previous_execution_path).read_bytes()
    require(len(previous_actual_raw) == 5187 and sha(previous_actual_raw)
            == "c99fc9f96ed753e6c493d44d55906b97450f0fcbfe584dda5b7ec9ce1e6d5c29"
            and len(previous_execution_raw) == 12330 and sha(previous_execution_raw)
            == "e6f8e2c9a8aae7a483dc8698ad877a757462d043ae5d2175b7299a4f503818be",
            "both entire actual zero-child results are unchanged")
    previous = json.loads(previous_actual_raw)
    previous_execution = json.loads(previous_execution_raw)
    require(previous["complete"] is False and previous["necessary_input_reconstruction_children"] == 0
            and previous["TC_scientific_children"] == previous["new_TC_integrated_cells"] == 0
            and previous["accepted_schedule"] is None
            and len(previous["schedule_results"]) == 2
            and all(row["skipped_for_known_hardware_capability"] is True
                    and row["actual_returncode"] is row["actual_report"] is None
                    for row in previous["schedule_results"])
            and previous["actual_readonly_runtime"]["OPENBLAS_verbose_stderr"] == "Core: Haswell\\n"
            and previous_execution["run_id"] == "45923136710"
            and previous_execution["run_attempt"] == "1"
            and previous_execution["finished_utc"] is not None
            and previous_execution["complete"] is False
            and previous_execution["scientific_children"] == 0,
            "no producer ran on the unsupported actual AMD dispatch; both declared candidates remain unused")
    manifest = json.loads(parent_raw)
'''),
        ('            ("runtime_identification_proof", PROOF), ("prior_Haswell_failure_record", HISTORY)):\n',
         '''            ("runtime_identification_proof", PROOF), ("prior_Haswell_failure_record", HISTORY),
            ("previous_runtime_actual", previous_actual_path),
            ("previous_runtime_execution", previous_execution_path),
            ("original_runtime_generator", TOPIC+"/scripts/make_original_nodal_runtime_manifest.py"),
            ("original_runtime_proof", TOPIC+"/notes/2026-11-27-TCX-zero-child-runtime-identification.md")):
'''),
    ]
    for old, new in changes:
        if old not in code:
            raise ValueError("the explicit Ubuntu24 metadata adaptation did not match: "+old)
        code = code.replace(old, new)
    return code


exec(compile(patched_source(), __file__, "exec"), globals())
