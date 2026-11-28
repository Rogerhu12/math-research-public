"""BNC continuation with original historical filenames and sibling paths.

The earlier worker renamed every historical file to role.json.gz. A genuine
candidate .json index then hit the deliberately forbidden single-file loader,
before any of the seven BNC targets. Preserve the original relative path;
the existing whole-byte checks, all inputs and every mathematical target stay.
"""
from pathlib import Path
import hashlib
import importlib.util


def patched_source():
    path = Path(__file__).with_name("fourfold_codazzi_target_normalized_strict_nu_public_worker.py")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != "1a667009d1e59ff64bfb094a1f037b4ec68f2ad1d729660bd6028a0c7725be95":
        raise ValueError("the complete original BNC publication wrapper changed")
    spec = importlib.util.spec_from_file_location("_BNC_native_paths_original_worker", path)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    source = original.patched_source()
    old = 'target = history_dir/(spec["role"]+".json.gz")'
    new = 'target = history_dir/topic_path(spec["path"])'
    if source.count(old) != 1:
        raise ValueError("the unique original historical materialization statement changed")
    source = source.replace(old, new)
    old = 'state["complete_old_input_admission_before_target_reservation"] = True'
    new = old+'\n        state["native_path_recovery"] = dict(failed_run="45941963989/1", original_relative_paths_and_siblings_retained=True, unchanged_BNC_targets=7, completed_predecessor_targets_recomputed=0)'
    if source.count(old) != 1:
        raise ValueError("the unique complete-admission receipt statement changed")
    return source.replace(old, new)


if __name__ == "__main__":
    exec(compile(patched_source(), __file__, "exec"), {"__name__": "__main__", "__file__": __file__})
