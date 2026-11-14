#!/usr/bin/env python3
"""Apply the proven nonnegative domain when loading R85 partial integrals.

The first replay is preserved: its generic endpoint-to-Arb reader rounded a
zero lower endpoint below zero before any complete-mean call.  Only the two
partial-integral readers change here.  The existing positive-integral loader
encloses intersection with [0,infinity), without selecting a new integral.
All candidate, physical derivative, full R64/J/R77 calls remain unchanged.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import ast
import hashlib
from pathlib import Path
import types


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    original=Path(__file__).with_name("tail_outer_physical_r_moment_replay.py")
    if sha(original)!="c8c565c2fef055430a2185a5545e0c44821a3a59bd6e2ce257ec680ade5c862e":
        raise ValueError("The preserved original physical-r replay changed")
    positive=Path(__file__).with_name("tail_outer_candidate_domain.py")
    if sha(positive)!="17d6b7d85be80f8f40b3eec411ae49a73c51c6b624d030df57b94202a7d08690":
        raise ValueError("The existing exact nonnegative-integral reader changed")
    from tail_outer_candidate_domain import nonnegative_integral
    raw=original.read_text()
    edits=[
        ('before={key:ball(row["prefix_moments"][key]) for key in MOMENT_KEYS}',
         'before={key:_positive_integral(row["prefix_moments"][key]) for key in MOMENT_KEYS}'),
        ('after={key:ball(row["suffix_moments"][key]) for key in MOMENT_KEYS}',
         'after={key:_positive_integral(row["suffix_moments"][key]) for key in MOMENT_KEYS}'),
        ('sources[Path(__file__).name]=digest(__file__)',
         'sources[Path(__file__).name]=digest(__file__)\n'
         '    sources[Path(_entry_source).name]=digest(_entry_source)\n'
         '    sources["tail_outer_candidate_domain.py"]=digest(Path(__file__).with_name("tail_outer_candidate_domain.py"))'),
        ('original_coefficient_enclosures_intersected=True),',
         'original_coefficient_enclosures_intersected=True,\n'
         '            partial_integrals_intersect_proven_nonnegative_domain=True),'),
    ]
    changed=raw
    for before,after in edits:
        if changed.count(before)!=1:raise ValueError("A narrow reader anchor changed")
        changed=changed.replace(before,after)
    reverse=changed
    for before,after in reversed(edits):reverse=reverse.replace(after,before)
    if reverse!=raw:raise AssertionError("The original replay was not exactly recovered")
    ast.parse(changed)
    module=types.ModuleType("tail_r85_nonnegative_integral_replay")
    module.__file__=str(original)
    module._entry_source=str(Path(__file__).resolve())
    module._positive_integral=nonnegative_integral
    exec(compile(changed,str(original),"exec"),module.__dict__)
    module.__doc__=__doc__
    module.main()


if __name__=="__main__":main()
