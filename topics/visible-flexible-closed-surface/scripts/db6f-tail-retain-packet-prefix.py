#!/usr/bin/env python3
"""Retain one already saved shard only if every represented span is complete.

No bound or data value is changed. The new finished flag concerns only the
explicit selected prefix; it never declares the interrupted full run done.
"""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('interrupted_manifest',type=Path);ap.add_argument('out',type=Path)
    args=ap.parse_args()
    old=json.loads(args.interrupted_manifest.read_text())
    if len(old['files'])!=1:raise ValueError('this exact-retention helper requires one saved shard')
    item=old['files'][0];path=Path(item['data_file'])
    if sha(path)!=item['sha256']:raise ValueError('saved shard hash mismatch')
    raw=path.read_bytes();raw=gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw
    data=np.load(io.BytesIO(raw),allow_pickle=False)
    ids=data['span_index'];left=data['u_left'];right=data['u_right']
    last=int(ids[-1])
    if set(map(int,ids))!=set(range(-1,last+1)):raise ValueError('prefix span indices are not consecutive from collar')
    for span in range(-1,last+1):
        where=np.flatnonzero(ids==span)
        if left[where[0]]!=0 or right[where[-1]]!=1 or not np.array_equal(right[where[:-1]],left[where[1:]]) or not np.all(left[where]<right[where]):
            raise ValueError('saved shard cuts or overlaps a span; do not retain it')
    if path.parent.resolve()!=args.out.parent.resolve():raise ValueError('keep the reference manifest in the data directory')
    result=dict(old)
    result.update(status='validated-background-selected-prefix-complete-full-run-interrupted',
                  finished=True,data_file=path.name,data_sha256=sha(path),span_selection=[-1,last+1],
                  parent_full_run_finished=old.get('finished',False),
                  interrupted_manifest=str(args.interrupted_manifest),interrupted_manifest_sha256=sha(args.interrupted_manifest),
                  retention_script_sha256=sha(__file__),selected_rows=len(ids),next_uncovered_span=last+1,
                  scope=__doc__+' Analytic bounds remain those of the hash-bound original supplier.')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'selected_rows':len(ids),'first_span':-1,'last_span':last,'next_uncovered_span':last+1}))


if __name__=='__main__':main()
