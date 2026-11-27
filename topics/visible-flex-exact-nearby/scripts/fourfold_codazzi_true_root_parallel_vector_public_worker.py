"""TCXV public worker: only new owner/worker paths in the full TCX worker."""
from pathlib import Path
import hashlib
import importlib.util

PARENT_NAME = "fourfold_codazzi_true_root_parallel_trial_public_worker.py"
PARENT_BYTES = 3430
PARENT_SHA256 = "0c3716823dbecdd789d7f9f6fbd4ef238a87e2b84f7af3c14b88cfaa60e6b7b6"


def patched_source():
    path = Path(__file__).with_name(PARENT_NAME)
    raw = path.read_bytes()
    if len(raw) != PARENT_BYTES or hashlib.sha256(raw).hexdigest() != PARENT_SHA256:
        raise ValueError("the entire original parallel public worker is immutable")
    spec = importlib.util.spec_from_file_location("_TCXV_original_parallel_worker", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    source = module.patched_source()
    for old, new in (
        ('OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"',
         'OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_trial_owner.py"'),
        ('WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py"',
         'WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_vector_public_worker.py"'),
    ):
        if source.count(old) != 1:
            raise ValueError("one exact public entry path is required: "+old)
        source = source.replace(old, new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
