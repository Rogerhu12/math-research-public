#!/usr/bin/env python3
"""Shared knot-aligned rays with bounded-size chunks for grids above 516.

The maximum is 32 accepted steps and 16512 step-times-ray cells per file.
Thus 516 rays use 32 steps, 1032 rays use 16. Each file also has an explicit
5 MB guard. No exact geometric object or numerical integration rule changes.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import fourfold_phase_exact_affine_nodes as runner
import fourfold_phase_shared_knot_nodes as previous


def save_adaptive_trace(stem, arrays):
    count=len(arrays["dense_h"])
    rays=arrays["accepted_state"].shape[-1]
    if rays>16512:
        raise ValueError("ray count exceeds the supported one-step chunk size")
    chunk_steps=min(32,max(1,16512//rays))
    references=[]
    for first in range(0,count,chunk_steps):
        last=min(first+chunk_steps,count)
        piece=dict(arrays)
        for key in ("dense_t_old","dense_h","dense_y_old","dense_F"):
            piece[key]=arrays[key][first:last]
        for key in ("accepted_tau","accepted_state"):
            piece[key]=arrays[key][first:last+1]
        piece["initial_angles"]=piece["accepted_state"][0,0]
        metadata=json.loads(str(arrays["metadata"]))
        metadata.update(first_accepted_segment=first,accepted_segment_stop=last,
            branch_total_accepted_segments=count,maximum_segments_per_chunk=chunk_steps,
            chunk_initial_angles_semantics="accepted state at the chunk boundary; H only when first_accepted_segment is zero")
        piece["metadata"]=np.array(json.dumps(metadata,sort_keys=True))
        packed,extension=runner.packed_npz(piece)
        if len(packed)>5_000_000:
            raise ValueError("adaptive chunk still exceeds the repository limit")
        path=stem.parent/(stem.name+f".part{first:04d}"+extension)
        path.write_bytes(packed)
        references.append(dict(path=str(path),sha256=runner.digest(path),bytes=len(packed),
            first_accepted_segment=first,accepted_segment_stop=last))
    return references


class AdaptiveSharedMap(previous.SharedKnotMap):
    def __init__(self, geometry, root, common, progress=None):
        super().__init__(geometry,root,common,progress)
        common.update(integration_driver_source_sha256=runner.digest(Path(__file__)),
            previous_shared_driver_sha256=runner.digest(Path(previous.__file__)),
            dense_chunk_policy="min(32,max(1,floor(16512/rays))) accepted steps; strict 5 MB guard")
        common.pop("accepted_step_chunk_size",None)


if __name__=="__main__":
    runner.ExactAffineMap=AdaptiveSharedMap
    runner.save_trace=save_adaptive_trace
    runner.main()
