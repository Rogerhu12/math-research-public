#!/usr/bin/env python3
"""Use measured, mode-dependent radial block sizes with the v2 CSR cache.

The current low-mode actual comparison found original full, block-eight and
cached block-eight RHS/Jacobians bitwise equal.  This entry reduces unnecessary
per-block collection at small M; all modes, radial nodes, equations and gates
are retained.  An explicit --rhs-block overrides the execution grouping.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from prefix_resource_driver_v2 import main as previous_main


def main():
    if '--rhs-block' not in sys.argv and '--modes' in sys.argv:
        modes = int(sys.argv[sys.argv.index('--modes') + 1])
        block = 64 if modes <= 16 else 32 if modes <= 24 else 16 if modes <= 32 else 8
        sys.argv[1:1] = ['--rhs-block', str(block)]
    return previous_main()


if __name__ == '__main__':
    main()
