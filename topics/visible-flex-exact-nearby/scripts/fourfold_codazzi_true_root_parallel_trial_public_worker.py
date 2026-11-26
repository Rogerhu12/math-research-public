"""TCX public worker: preserve the whole disjoint ledger at a stable prefix.

The original complete worker remains byte-pinned. Only the new owner/worker
paths, whole-state budget and disjoint-progress publication predicates
change. Its complete input restoration, immutable numerical runtime,
READMEs, single-use reservation and all natural-result validators remain.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_true_root_trial_public_worker.py"
BASE_BYTES = 43200
BASE_SHA256 = "fca2c64ec4b479c2599d13377d4d658242d42b028455c30c1c11482f73840c37"


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the entire original public TC worker changed")
    source = raw.decode()
    replacements = [
        ('OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"',
         'OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_owner.py"',1),
        ('WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py"',
         'WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py"',1),
        ('op["maximum_total_publication_bytes"] == 170000',
         'op["maximum_total_publication_bytes"] == 280000\n'
         '            and op["maximum_state_bytes"] == 95000',1),
        ('            qualified = [target for name,target in zip(("matrix","negative","positive"),TARGETS)\n',
         '''            if not owner.validate_parallel_checkpoint(
                    doc,files.get(output_dir+"/"+FILES["prefix"])):
                # The atomic prefix can briefly precede the corresponding
                # whole state. Preserve only the matching whole checkpoint.
                continue
            if doc["complete"]:
                ledger = doc["preparation"].get(owner.PARALLEL_KEY)
                require(isinstance(ledger,dict) and ledger["complete"] is True
                        and ledger["accepted_union_complete_cells"]
                            == ledger["contiguous_next_cell"] == ledger["complete_total_cells"],
                        "every disjoint accepted cell is present in the complete final source domain")
            qualified = [target for name,target in zip(("matrix","negative","positive"),TARGETS)
''',1),
        ('        state["qualified_complete_cells"] = -1 if prefix_raw is None else parse(prefix_raw)["next_cell"]\n',
         '''        state["qualified_complete_cells"] = -1 if prefix_raw is None else parse(prefix_raw)["next_cell"]
        ledger = result["preparation"].get(owner.PARALLEL_KEY)
        state["parallel_accepted_complete_cells"] = (state["qualified_complete_cells"]
            if ledger is None else ledger["accepted_union_complete_cells"])
''',1),
        ('current_cells = state["qualified_complete_cells"]',
         'current_cells = state["parallel_accepted_complete_cells"]',1),
        ('last_published_cells = state["qualified_complete_cells"]',
         'last_published_cells = state["parallel_accepted_complete_cells"]',1),
    ]
    for old,new,count in replacements:
        if source.count(old) != count:
            raise ValueError("the exact TCX public-worker adaptation did not match: "+old)
        source = source.replace(old,new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
