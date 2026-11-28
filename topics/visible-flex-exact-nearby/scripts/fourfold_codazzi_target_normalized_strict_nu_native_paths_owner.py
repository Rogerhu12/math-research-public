"""Resume BNC's seven uncomputed targets after the native-path packaging failure.

The original mathematical owner is byte-pinned and changed only in the three
entry-point path constants. Every target, input contract and numerical formula
remains the original one. This module does no numerical work when imported.
"""
from pathlib import Path
import hashlib

_original = Path(__file__).with_name("input_original_BNC_owner.py")
if not _original.exists():
    _original = Path(__file__).with_name("fourfold_codazzi_target_normalized_strict_nu_owner.py")
_raw = _original.read_bytes()
if hashlib.sha256(_raw).hexdigest() != "36e6c16e7cb71412b5a92b8445f5fb4cc9c9cb6a5ed32291733ffd89c962180d":
    raise ValueError("the complete original BNC mathematical owner changed")
_source = _raw.decode("utf-8")
for _old, _new in (
    ("fourfold_codazzi_target_normalized_strict_nu_owner.py", "fourfold_codazzi_target_normalized_strict_nu_native_paths_owner.py"),
    ("fourfold_codazzi_target_normalized_strict_nu_public_worker.py", "fourfold_codazzi_target_normalized_strict_nu_native_paths_public_worker.py"),
    ("make_target_normalized_strict_nu_manifest.py", "make_target_normalized_strict_nu_native_paths_manifest.py"),
):
    if _source.count(_old) != 1:
        raise ValueError("the unique original BNC entry constant changed: "+_old)
    _source = _source.replace(_old, _new)
exec(compile(_source, __file__, "exec"), globals())
