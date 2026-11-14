#!/usr/bin/env python3
"""Retain the finite closed map while removing near-duplicate display rings.

The old plan could request both 0.031249999999999993 and
0.031249999999999997 on the cap. Some rounded Cartesian vertices coincided,
creating zero-area display triangles. Only the display query grid changes;
the fixed g, map, coefficients, collar, cut width and phase interval do not.
"""
import hashlib
import importlib.util
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'exact_20261114_refined_closed_assembly.py'
merges=[]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def display_anchors(values,lo,hi):
    # Later entries are named landmarks; explicit outer/inner anchors have
    # the highest priority. Do not replace a physical source knot or curve.
    values=[float(x) for x in values]+[float(lo),float(hi)]
    tolerance=32*np.finfo(float).eps*max(1.,abs(lo),abs(hi))
    indexed=sorted(enumerate(values),key=lambda x:x[1])
    groups=[]
    for row in indexed:
        if not groups or row[1]-groups[-1][-1][1]>tolerance:
            groups.append([row])
        else:
            groups[-1].append(row)
    result=[]
    for group in groups:
        chosen=max(group,key=lambda x:x[0])[1]
        result.append(chosen)
        distinct=sorted(set(x[1] for x in group))
        if len(distinct)>1:
            merges.append(dict(values=distinct,chosen=chosen,maximum_shift=max(abs(chosen-v) for v in distinct)))
    result=np.asarray(result)
    if result[0]!=lo or result[-1]!=hi or np.any(np.diff(result)<=tolerance):
        raise ValueError('Display ring deduplication lost anchors or strict separation')
    return result


def main():
    source_hash=sha(__file__);base_hash=sha(ORIGINAL)
    spec=importlib.util.spec_from_file_location('exact_closed_distinct_display_base',ORIGINAL)
    base=importlib.util.module_from_spec(spec);sys.modules[spec.name]=base;spec.loader.exec_module(base)
    original_write=base.write
    def write(path,obj):
        if isinstance(obj,dict):
            obj['display_query_adapter']=dict(source_sha256_at_start=source_hash,
                original_assembly_sha256_at_start=base_hash,merged_near_equal_display_requests=merges,
                physical_function_unchanged=True,
                definition='Only generated display query radii within 32 binary64 eps*max(1,|endpoints|) are merged; named landmarks and endpoints take priority. No source radial node, coefficient, field or parameter is moved.')
        original_write(path,obj)
    base.anchors=display_anchors
    base.write=write
    # The inherited CLI records the actually launched adapter as its entry
    # source; the untouched implementation hash is recorded above as well.
    base.__file__=__file__
    base.main()


if __name__=='__main__':main()
