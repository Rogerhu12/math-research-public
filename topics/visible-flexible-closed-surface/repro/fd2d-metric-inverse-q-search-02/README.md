# Closed endpoint-refined inverse-Q optimizer snapshot

This contains the actual source and complete closed output of process36713.
It uses the unchanged `positive_q.py` and its `explore_inverse.py` dependency
from the sibling search-01 snapshot. In a scratch copy, place those dependencies
on PYTHONPATH and keep the supplied height64-11 starting report in the working
directory before running `OPENBLAS_NUM_THREADS=1 python optimize_coupled12.py`.
The source snapshot preserves the actual fixed repository path in the older
trajectory reader; use a new operational copy to adapt that location elsewhere.

The final background is directly defined by candidate04 and the portable MJS
provider. Rerunning the optimizer is not needed to evaluate that background.
The optimizer stopped at its iteration limit; the full parameter iterate was
kept and its endpoint error is handled by the explicit S5 calibration.
