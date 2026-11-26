"""Metadata-only TCX entry after the complete original predecessor ends.

No actual launch is created while the preceding TC science is running.
The whole published generator and its continuation adapter are retained;
the additional inputs describe fixed disjoint whole-cell continuation.
"""
from pathlib import Path
import hashlib
import importlib.util

CONT_GENERATOR_NAME = "make_true_root_trial_continuation_manifest.py"
CONT_GENERATOR_BYTES = 3322
CONT_GENERATOR_SHA256 = "40ffe4fb7ca8dc3c403b03219834388e8b6b51953c17908ee49f435252061892"
BASE_WORKER_NAME = "fourfold_codazzi_true_root_trial_public_worker.py"
BASE_WORKER_BYTES = 43200
BASE_WORKER_SHA256 = "fca2c64ec4b479c2599d13377d4d658242d42b028455c30c1c11482f73840c37"


def _TCX_generator_source():
    path = Path(__file__).with_name(CONT_GENERATOR_NAME)
    raw = path.read_bytes()
    if len(raw) != CONT_GENERATOR_BYTES or hashlib.sha256(raw).hexdigest() != CONT_GENERATOR_SHA256:
        raise ValueError("the entire original continuation generator changed")
    spec = importlib.util.spec_from_file_location("_TCX_pinned_continuation_generator",path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.patched_source()


def patched_source():
    source = _TCX_generator_source()
    old_worker = Path(__file__).with_name(BASE_WORKER_NAME).read_bytes()
    if len(old_worker) != BASE_WORKER_BYTES or hashlib.sha256(old_worker).hexdigest() != BASE_WORKER_SHA256:
        raise ValueError("the whole immutable public worker dependency changed")
    worker_blob = hashlib.sha1(b"blob "+str(len(old_worker)).encode()+b"\0"+old_worker).hexdigest()
    replacements = [
        ('OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_continuation_owner.py"',
         'OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"'),
        ('WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py"',
         'WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py"'),
        ('GENERATOR = TOPIC+"/scripts/make_true_root_trial_continuation_manifest.py"',
         'GENERATOR = TOPIC+"/scripts/make_true_root_parallel_trial_manifest.py"'),
        ('BASE_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-same-prefix-inputs"',
         'BASE_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-disjoint-prefix-inputs"'),
        ('BASE_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-same-prefix-public"',
         'BASE_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-disjoint-prefix-public"'),
        ('    add(OWNER,whole_small(root,OWNER),role="owner")\n',
         '''    add(OWNER,whole_small(root,OWNER),role="owner")
    add(WORKER,whole_small(root,WORKER),role="worker")
    for role,name in (
            ("original_TC_continuation_owner","fourfold_codazzi_true_root_trial_continuation_owner.py"),
            ("original_TC_continuation_generator","make_true_root_trial_continuation_manifest.py"),
            ("parallel_math","fourfold_codazzi_true_root_parallel_cell_slices.py")):
        path = TOPIC+"/scripts/"+name
        add(path,whole_small(root,path),role=role)
    parallel_proof = TOPIC+"/results/R149-supplement-disjoint-same-trial-cell-continuation.md"
    add(parallel_proof,whole_small(root,parallel_proof),role="parallel_proof")
'''),
        ('require(len(definitions) == 81,"the original whole78 text inputs plus3 explicit continuation inputs")',
         'require(len(definitions) == 86,"all original78 plus8 exact continuation/scheduling text inputs")'),
        ('        _TC_spec["role"] = "original_TC_owner"\n',
         '        _TC_spec["role"] = "original_TC_owner"\n'
         '    elif _TC_spec["role"] == "worker":\n'
         '        _TC_spec.update(role="original_TC_worker",bytes='+str(BASE_WORKER_BYTES)
         +',sha256="'+BASE_WORKER_SHA256+'",git_blob_sha="'+worker_blob+'")\n'),
        ('        "continuation":continuation,\n',
         '        "continuation":continuation,"parallel_continuation":owner.TCX_CONTRACT,\n'),
        ('"maximum_state_bytes":18000,"maximum_matrix_bytes":26000',
         '"maximum_state_bytes":95000,"maximum_matrix_bytes":26000'),
        ('"maximum_execution_bytes":35000,"maximum_total_publication_bytes":170000',
         '"maximum_execution_bytes":35000,"maximum_total_publication_bytes":280000'),
        ('            "all96_all5_source_exact_complete_cell_prefix":True,\n',
         '''            "all96_all5_source_exact_complete_cell_prefix":True,
            "maximum_disjoint_arithmetic_children":3,
            "all_four_original_trial_arrays_verified_once_before_fork":True,
            "whole_original_seed_and_fixed_disjoint_slice_ledger_retained":True,
            "all_prior_accepted_slice_cells_reintegrated":False,
            "new_boundaries_or_source_windows_created":False,
'''),
        ('            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py\n',
         '            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py\n'
         '            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py\n'),
        ('          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py\n',
         '          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py\n'),
        ('name: R149 complete true-root finite trials @LABEL@',
         'name: R149 complete true-root disjoint cell continuation @LABEL@'),
    ]
    for old,new in replacements:
        if source.count(old) != 1:
            raise ValueError("the exact TCX generator adaptation did not match: "+old)
        source = source.replace(old,new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
