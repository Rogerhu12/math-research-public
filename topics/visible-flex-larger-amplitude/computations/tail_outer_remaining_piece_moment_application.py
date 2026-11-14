#!/usr/bin/env python3
"""Apply the frozen R80 moment/replay/composition tools to other original pieces.

Only original cell0 pieces 0,2,4,6 are allowed. Their whole-piece R48 candidate
definitions and shared endpoints already occur in the original complete data.
The original source, positive integrals, interval intersections, complete mean,
actual derivatives, all finite J modes and R77 gates are unchanged. This entry
only changes the explicit segment guard and records its additional identity.
It does not apply to the distinct substage candidates or the physical-r piece8.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path
import sys
import types


def load_owned(name, checksum, edits, label):
    path = Path(__file__).with_name(name)
    raw = path.read_text()
    if hashlib.sha256(raw.encode()).hexdigest() != checksum:
        raise ValueError("The frozen R80 application source changed: "+name)
    transformed = raw
    for before,after in edits:
        if transformed.count(before) != 1:
            raise ValueError("A remaining-original-piece application anchor is not unique")
        transformed = transformed.replace(before,after)
    reverse = transformed
    for before,after in reversed(edits):
        reverse = reverse.replace(after,before)
    if reverse != raw:
        raise AssertionError("The exact original R80 source was not recovered")
    ast.parse(transformed,filename=str(path))
    module = types.ModuleType("tail_remaining_original_piece_"+label)
    module.__file__ = str(path)
    module._application_source = str(Path(__file__).resolve())
    exec(compile(transformed,str(path),"exec"),module.__dict__)
    module.__doc__ = __doc__+"\nSelected phase: "+label
    return module


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("moments","replay","compose"):
        raise ValueError("Use moments, replay or compose, followed by its original explicit arguments")
    phase = sys.argv.pop(1)
    if phase == "moments":
        module = load_owned("tail_outer_capped_true_moments.py",
            "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b", [
            ('a.segment == 1 and a.order >= 8',
             'a.segment in (0,2,4,6) and a.order >= 8'),
            ('This first actual capped application is original cell0/segment1',
             'Use one unchanged original cell0 piece from 0,2,4,6'),
            ('source_hashes[Path(__file__).name] = digest(__file__)',
             'source_hashes[Path(__file__).name] = digest(__file__)\n'
             '    source_hashes[Path(_application_source).name] = digest(_application_source)'),
        ],phase)
    elif phase == "replay":
        module = load_owned("tail_outer_capped_moment_replay.py",
            "d4bb3fd3c8c1cafb901ce6bbe5a1ceba707a42f8b9f0b578d34e5117799c2980", [
            ('if segment != 1:', 'if segment not in (0,2,4,6):'),
            ('This completed capped-moment certificate covers original segment1 only',
             'Use the matching complete certificate for one original piece 0,2,4,6'),
            ('if selected != [1]:',
             'if len(selected) != 1 or selected[0] not in (0,2,4,6):'),
            ('Use this actual capped certificate only on original segment1',
             'Use the matching capped certificate on one original piece 0,2,4,6'),
            ('source_hashes[Path(__file__).name] = digest(__file__)',
             'source_hashes[Path(__file__).name] = digest(__file__)\n'
             '    source_hashes[Path(_application_source).name] = digest(_application_source)'),
        ],phase)
    else:
        module = load_owned("tail_outer_combine_refined_moments.py",
            "a592fbb3a15677eb804c275c815ad7d70218dd55f65b8f0e5e22ee9b835e080a", [
            ('module._entry_source = str(Path(__file__).resolve())',
             'module._entry_source = _application_source'),
        ],phase)
    module.main()


if __name__ == "__main__":
    main()
