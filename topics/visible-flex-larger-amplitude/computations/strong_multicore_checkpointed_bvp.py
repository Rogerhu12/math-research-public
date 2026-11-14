#!/usr/bin/env python3
"""Apply the unchanged atomic Newton observer to multicore tangent designs.

Only the inner warm-design entry path changes in memory. The Newton
observation, restore identity checks, acceptance and 16/12 batching retain
their original implementations and defaults are still explicit arguments.
"""
from pathlib import Path
import hashlib
import types
import strong_small_batch_bvp as batches

HERE = Path(__file__).resolve().parent


def main():
    original_path = HERE/'strong_checkpointed_tangent_bvp.py'
    source = original_path.read_text()
    entry_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    replacements = [
        ("inner = HERE/'strong_tangent_warm_bvp.py'",
         "inner = HERE/'strong_multicore_tangent_bvp.py'"),
        ('    recorder = Recorder(prefix, hashes)',
         '    hashes[_multicore_entry_file] = _multicore_entry_hash\n'
         '    recorder = Recorder(prefix, hashes)')]
    for before, after in replacements:
        if source.count(before) != 1:
            raise ValueError('The original observation entry changed')
        source = source.replace(before, after)
    module = types.ModuleType('strong_multicore_checkpoint_observer')
    module.__file__ = str(original_path)
    module.__dict__.update(_multicore_entry_file=str(Path(__file__)),
                           _multicore_entry_hash=entry_hash)
    exec(compile(source, str(original_path), 'exec'), module.__dict__)
    previous = batches.checkpointed
    batches.checkpointed = module
    try:
        batches.main()
    finally:
        batches.checkpointed = previous


if __name__ == '__main__':
    main()
