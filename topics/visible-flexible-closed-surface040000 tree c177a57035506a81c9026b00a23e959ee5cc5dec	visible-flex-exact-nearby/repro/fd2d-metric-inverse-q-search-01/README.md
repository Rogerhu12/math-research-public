# Closed exploratory inverse-Q source and report snapshot

These are the actual closed exploratory sources and reports used before the
nonuniform constraint-grid run. They do not define a completed nonlinear tail.
No active run files are included.

The final explicit background is independently reproducible from the candidate
JSON and `scripts/fd2d-metric-inverse-q-buffer.mjs`; it does not require rerunning
an optimizer. The exploratory Python sources use NumPy/SciPy and the original
wc01 trajectory. `explore_inverse.py` retains the actual session absolute topic
path used when run. For another checkout, adapt that one location in a new
operational copy, preserving this snapshot. Run each script from this directory
so its relative input report paths resolve. Limit BLAS threads with
`OPENBLAS_NUM_THREADS=1`.

`positive-q-widen-02.json` was written by an inline driver whose process could not
be polled after the model resume: `Unknown process id 21162`. The file exists,
but no exit code is asserted. Its parameters define the recorded finite samples;
no standalone driver execution is falsely claimed. Other observed process exits
are recorded in the adjacent execution-history JSON.

For wide03, the 192-cell optimization missed a narrow endpoint curvature peak.
The separate 4097-point provider check found 7.43584565, so that candidate is
explicitly rejected for the current background curvature budget. The later
nonuniform run addresses this observed issue; it is not included in this closed
snapshot.
