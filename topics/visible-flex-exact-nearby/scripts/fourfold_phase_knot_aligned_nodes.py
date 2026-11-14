#!/usr/bin/env python3
"""Full actual H-node grid with knot-aligned integration of the same field.

This entry point reuses the frozen exact-affine runner and its CLI, adding an
explicit, hash-recorded integration strategy. No frozen source file changes.
All limitations of the floating runner still apply; the new dense references
need continuous residual validation of their own.
"""
from pathlib import Path

import fourfold_phase_exact_affine_nodes as runner
import fourfold_phase_knot_aligned_probe as alignment


class FullKnotAlignedMap(alignment.KnotAlignedMap):
    def __init__(self, geometry, root, common, progress=None):
        cuts, metadata = alignment.radial_cuts(geometry.frozen, root, 1e-13)
        # Update the caller's dictionary too, so the completed grid and every
        # branch identity record the same solver strategy and source hashes.
        common.update(
            integration_strategy="DOP853 restarted at numerical radial knot representatives",
            integration_driver_source_sha256=alignment.digest(Path(__file__)),
            knot_alignment_source_sha256=alignment.digest(Path(alignment.__file__)),
            knot_alignment=metadata,
        )
        super().__init__(geometry, root, common, cuts, progress)


if __name__ == "__main__":
    runner.ExactAffineMap = FullKnotAlignedMap
    runner.main()
