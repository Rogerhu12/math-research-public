#!/usr/bin/env python3
"""Correct the original-piece evaluator's complete finite-J angular weight table.

The r1 wrapper stopped before its first accepted leaf with KeyError:0.
Only the weight dictionary is extended from height modes to m=0,2,...,2*mmax;
all old positive-height weights retain exactly their arithmetic. The original
failed source and resource are preserved. All same-candidate, mean, full-J,
R77 and resource gates remain. No new physical or numerical model is used.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path
import types


def main():
    original = Path(__file__).with_name("tail_outer_original_piece_finite_j.py")
    raw = original.read_text()
    if hashlib.sha256(raw.encode()).hexdigest() != "b5196622ed649c6e3a3d6ad3227f30b0c54651d402c5866cfa2102d5e6def2d4":
        raise ValueError("The preserved original-piece failure source changed")
    edits = [
        ('weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in modes}',
         'weights = {m: ((1+m)*(exact_q(tau)*m).exp()).upper() for m in range(0, 2*max(modes)+1, 2)}'),
        ('source_hashes[Path(__file__).name] = digest(__file__)',
         'source_hashes[Path(__file__).name] = digest(__file__)\n'
         '    source_hashes[Path(_replay_source_path).name] = digest(_replay_source_path)'),
    ]
    changed = raw
    for before, after in edits:
        if changed.count(before) != 1:
            raise ValueError("A narrow complete-weight replacement anchor changed")
        changed = changed.replace(before, after)
    reverse = changed
    for before, after in reversed(edits):
        reverse = reverse.replace(after, before)
    if reverse != raw:
        raise AssertionError("The exact original failed source was not reconstructed")
    ast.parse(changed, filename=str(original))
    module = types.ModuleType("tail_outer_complete_angular_weights")
    module.__file__ = str(original)
    module._replay_source_path = str(Path(__file__).resolve())
    exec(compile(changed, str(original), "exec"), module.__dict__)
    module.main()


if __name__ == "__main__":
    main()
