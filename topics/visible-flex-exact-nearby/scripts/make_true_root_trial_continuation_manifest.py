"""Metadata-only continuation entry after an actual TC predecessor ENDS.

No workflow is generated without complete prior execution and natural
objects. The unchanged large original generator is byte-pinned and used
only for metadata; this small adapter adds the complete source-identity
transition proof and the corrected predecessor metadata owner.
"""
from pathlib import Path
import hashlib

GENERATOR_BASE_NAME = "make_true_root_trial_residual_manifest.py"
GENERATOR_BASE_BYTES = 40003
GENERATOR_BASE_SHA256 = "3a1f8b689a6df196274dc02f75d18c4c5c5ed90c41057c6512f6ff4bae42df38"


def patched_source():
    raw = Path(__file__).with_name(GENERATOR_BASE_NAME).read_bytes()
    if len(raw) != GENERATOR_BASE_BYTES or hashlib.sha256(raw).hexdigest() != GENERATOR_BASE_SHA256:
        raise ValueError("the whole original TC metadata generator changed")
    source = raw.decode()
    replacements = [
        ('OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"',
         'OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_continuation_owner.py"'),
        ('GENERATOR = TOPIC+"/scripts/make_true_root_trial_residual_manifest.py"',
         'GENERATOR = TOPIC+"/scripts/make_true_root_trial_continuation_manifest.py"'),
        ('BASE_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-separated-grid-inputs"',
         'BASE_MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-same-prefix-inputs"'),
        ('BASE_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-separated-grid-public"',
         'BASE_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-same-prefix-public"'),
        ('    add(GENERATOR,whole_small(root,GENERATOR),role="generator")\n',
         '    add(GENERATOR,whole_small(root,GENERATOR),role="generator")\n'
         '    add(OWNER,whole_small(root,OWNER),role="owner")\n'
         '    original_generator = TOPIC+"/scripts/make_true_root_trial_residual_manifest.py"\n'
         '    add(original_generator,whole_small(root,original_generator),role="original_TC_generator")\n'
         '    continuation_proof = TOPIC+"/results/R149-supplement-same-trial-prefix-continuation-after-input-restoration.md"\n'
         '    add(continuation_proof,whole_small(root,continuation_proof),role="continuation_proof")\n'),
        ('require(len(definitions) == 78,"the complete fixed text closure has78 unique whole files")',
         'require(len(definitions) == 81,"the original whole78 text inputs plus3 explicit continuation inputs")'),
        ('def build(root,prior_manifest_path=None,prior_execution_path=None):\n',
         'for _TC_spec in EXTRA_CURRENT:\n'
         '    if _TC_spec["role"] == "owner":\n'
         '        _TC_spec["role"] = "original_TC_owner"\n\n\n'
         'def build(root,prior_manifest_path=None,prior_execution_path=None):\n'
         '    require(prior_manifest_path is not None and prior_execution_path is not None,\n'
         '            "continuation only: an ended actual predecessor and all whole objects are required")\n'),
    ]
    for old, new in replacements:
        if source.count(old) != 1:
            raise ValueError("the fixed complete TC metadata patch did not match: "+old)
        source = source.replace(old, new)
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
