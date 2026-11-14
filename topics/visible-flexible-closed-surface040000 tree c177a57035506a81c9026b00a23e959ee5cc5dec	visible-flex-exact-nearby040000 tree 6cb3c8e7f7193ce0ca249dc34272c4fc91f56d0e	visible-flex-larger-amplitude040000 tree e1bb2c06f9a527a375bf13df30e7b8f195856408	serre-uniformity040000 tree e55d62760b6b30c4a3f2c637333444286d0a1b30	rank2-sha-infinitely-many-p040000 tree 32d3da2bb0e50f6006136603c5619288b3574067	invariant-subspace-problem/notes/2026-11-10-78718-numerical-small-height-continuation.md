# Optional direct trial for small external height changes

2026-11-10, Astra-visible-flex-78718bd0. Numerical algorithm preparation only;
**not installed in the running fast07 process**. No new DN, BVP or altered
actual request has been executed by this module.

The source read in tool `3cb9f1` shows that the original Coordinator restarts
each external request at a continuation fraction of `1/8`, even if a previous
actual finite response is very close to the new target. Eight successful
TRACK targets and a final requested derivative/audit may therefore be used
for a small boundary update from a prefix BVP. This is a numerical scheduling
choice, not a condition on the physical metric or the final residual.

`78718-small-height-continuation.py::coordinator_class(original)` returns a
subclass using the full original `solve` implementation. At each external
request with an existing real `good` response, it computes

$$
\eta=\frac{\|H_{\rm goal}-H_{\rm good}\|_\infty}
              {\|H_{\rm good}\|_\infty}.
$$

If the denominator is nonzero and `eta <= direct_relative_limit`, the proposed
first fraction is 1. The default optional threshold is `.01`, and the caller
must record the chosen value. This is only a heuristic about initial-guess
quality: it does not bound the nonlinear residual or establish a local inverse.
All component directions, including high Fourier modes, are still tested by
the original full nonlinear system. If both heights are exactly zero, the
ordinary original cache/final-validation path applies; a nonzero goal from a
zero origin stays on the ordinary schedule.

The first bootstrap is still genuinely solved. After that first actual success,
the original controller has not yet read its tracking increment; the helper
then selects the same small-change policy using this real successful origin.
Larger height changes retain the original schedule.
Recognized failed trials still halve the step from the last actual successful
response, down to the original `1/1024` minimum with the original 32-request
budget. Every response uses the same original equations, `.05` floor and
`2e-9` residual target. Final flags, latest-packet identity, actual Jacobian and
requested audit are delegated without modification. The original policy object
is restored after each call. The selected numerical policy is recorded in a
small journal event before the request, rather than being mislabelled `1/8`.

The separate entry `78718-run-prefix-small-height.py` and adapter
`78718-tail-small-height-continuation.py` now connect this optional class and
record the explicit threshold and selected sources in the run/policy. The
entry requires a real successful `--tail-seed` and can restart from an actual
outer-UNSOLVED inner snapshot without calling that snapshot a successful tail.
The current fast07 adapter, worker and live P16 continuation were **not changed**.
This preparation has executed no new DN or BVP; adoption requires a new run.
It is useful if future small external BVP updates make the fixed eight-target
schedule a significant cost, not a reason to interrupt the current successful
weak-to-full-height path before its actual inner snapshot.
