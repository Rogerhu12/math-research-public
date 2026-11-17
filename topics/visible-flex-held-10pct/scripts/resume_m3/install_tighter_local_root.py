#!/usr/bin/env python3
"""Tighten local root residual tolerances in the optional continuation engine.

This is a numerical accuracy variant. D/S/A guards, physical parameters, root
equations and the outer shooting tolerance are unchanged. Both the usual root
stopping tolerance and its existing roundoff fallback are made ten times
smaller. Immutable source-root files are never changed.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--source-topic',type=Path,required=True)
    a=p.parse_args()
    file=a.source_topic/'scripts/local-root-continuation/general_root_tail_momentum.mjs'
    before=file.read_text()
    if before.count('8e-14*scale')!=3 or before.count('5e-12*scale')!=1:
        raise ValueError('Expected original residual constants in optional root engine')
    after=before.replace('8e-14*scale','8e-15*scale').replace('5e-12*scale','5e-13*scale')
    file.write_text(after)
    print(json.dumps(dict(scope=__doc__,usual_relative_tolerance=[8e-14,8e-15],
                          fallback_relative_tolerance=[5e-12,5e-13],
                          before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                          after_sha256=hashlib.sha256(after.encode()).hexdigest()),indent=2))


if __name__=='__main__':main()
