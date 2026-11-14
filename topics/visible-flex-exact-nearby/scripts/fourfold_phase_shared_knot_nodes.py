#!/usr/bin/env python3
"""One common adaptive knot-aligned time grid for all initial ray nodes.

Use the frozen exact-affine runner CLI with --block-size equal to --rays.
The geometry is unchanged. Every branch is split into at most 32 accepted
steps per gzip/NPZ file; the metadata explicitly identifies internal chunks.
All data are floating references, not validated trajectories.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

import fourfold_phase_exact_affine_nodes as runner
import fourfold_phase_knot_aligned_probe as alignment


def save_trace32(stem, arrays):
    references = []
    count = len(arrays["dense_h"])
    for first in range(0, count, 32):
        last = min(first+32, count)
        piece = dict(arrays)
        for key in ("dense_t_old", "dense_h", "dense_y_old", "dense_F"):
            piece[key] = arrays[key][first:last]
        for key in ("accepted_tau", "accepted_state"):
            piece[key] = arrays[key][first:last+1]
        piece["initial_angles"] = piece["accepted_state"][0, 0]
        metadata = json.loads(str(arrays["metadata"]))
        metadata.update(first_accepted_segment=first, accepted_segment_stop=last,
                        branch_total_accepted_segments=count,
                        chunk_initial_angles_semantics="accepted state at the chunk boundary; H only when first_accepted_segment is zero")
        piece["metadata"] = np.array(json.dumps(metadata, sort_keys=True))
        packed, extension = runner.packed_npz(piece)
        if len(packed) > 5_000_000:
            raise ValueError("a 32-step trace chunk exceeds the repository limit")
        path = stem.parent/(stem.name+f".part{first:04d}"+extension)
        path.write_bytes(packed)
        references.append(dict(path=str(path), sha256=runner.digest(path), bytes=len(packed),
                               first_accepted_segment=first, accepted_segment_stop=last))
    return references


class SharedKnotMap(alignment.KnotAlignedMap):
    def __init__(self, geometry, root, common, progress=None):
        cuts, metadata = alignment.radial_cuts(geometry.frozen, root, 1e-13)
        common.update(integration_strategy="all initial nodes share one DOP853 grid, restarted at numerical radial knot representatives",
                      integration_driver_source_sha256=runner.digest(Path(__file__)),
                      knot_alignment_source_sha256=runner.digest(Path(alignment.__file__)),
                      accepted_step_chunk_size=32, knot_alignment=metadata)
        super().__init__(geometry, root, common, cuts, progress)

    def branch(self, theta, *args, **kwargs):
        if self.common["block_size"] != self.common["rays"] or len(theta) != self.common["rays"]:
            raise ValueError("shared-grid entrypoint requires --block-size equal to --rays")
        return super().branch(theta, *args, **kwargs)


if __name__ == "__main__":
    runner.ExactAffineMap = SharedKnotMap
    runner.save_trace = save_trace32
    runner.main()
