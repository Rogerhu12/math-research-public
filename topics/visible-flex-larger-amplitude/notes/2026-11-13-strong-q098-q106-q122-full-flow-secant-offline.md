# Two accepted full-flow tangents: an offline q122 warm diagnostic

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

This is a numerical initial-guess comparison. It neither evaluates a new
nonlinear residual nor changes any running solve or acceptance rule.

## Same tail and complete data

The q098 accepted bootstrap and q106 accepted final response have identical
complete tangent identities, including the original physical parameters,
all 576 stage descriptions, nine raw-node locations, frozen profile
fingerprints, far graph, radius, backend and every source SHA. Their
identity SHA is recorded in the primary. All eight compressed flow blocks
and the base block of each snapshot pass both compressed and uncompressed
SHA checks. The 577 by 56 states, complete 28-component heights and every
56 by 56 stage Jacobian are retained.

The q122 original linear seed and its saved accepted iteration02 trial
have the same complete target height, stage parameters and raw-node map.
The reference trial's normalized residual is 1.499946469287228e-9. This
reference is not a final coupled q122 acceptance. No result here replaces
the original residual, full Jacobian, positivity or physical audit gates.

## Formulas and numerical implementation check

For each original flow block split into A, B, C, D, the original predictor
uses G_N = diag(farGraph), T_n = (A_n + B_n G_(n+1))^(-1), and
G_n = (C_n + D_n G_(n+1)) T_n. A Dirichlet height increment is divided
by the common radius to the fourth power, transported by T, and paired
with G times that transported increment. These same formulas are
implemented in NumPy; no new physical flow or derivative is generated.

The independently evaluated linear prediction differs from the archived
original predictor by at most 1.137e-13 in absolute state and 1.453e-15
in node-relative state. These are observed numerical agreements, not
rigorous floating-point error bounds. They are respectively more than
seven orders below the original seed error under the explicit gates.

Let dH = H106 - H098, alpha be the projection coefficient of the current
target increment onto dH, and v_i = J_i dH. The actual data give
alpha = 2.000000000000006 and a relative orthogonal remainder below
7.35e-18. The second-order correction is alpha^2 (v_1-v_0)/2.

For cubic Hermite extrapolation, write d = s_1-s_0. Add to the original
linear seed the correction

    alpha^2 [(v_0-d)+2(v_1-d)] + alpha^3 [(v_0-d)+(v_1-d)].

At exactly alpha=2 this is the usual two-value, two-tangent cubic
28 s_0 + 12 v_0 - 27 s_1 + 18 v_1 after inclusion of the linear part.
The correction form avoids direct cancellation of the large base states.
A separate direct long-double evaluation agrees within 1.137e-13.
All original cut Dirichlet values are restored bit for bit in both
predicted fields.

## Complete-state comparison

Node-relative error divides every component at a node by the maximum
absolute component of the reference state at that same node, with a
1e-250 floor. This is a diagnostic convention, not the original nonlinear
residual norm. Every one of the 32,312 state entries is compared.

| Diagnostic | Original linear seed | Secant second order | Cubic Hermite |
| --- | ---: | ---: | ---: |
| Maximum absolute state error | 0.2685817973 | 0.001436850042 | 0.00003140269226 |
| Maximum node-relative state error | 0.01111366061 | 0.0001650234888 | 0.000005860173869 |
| RMS node-relative state error | 0.0002452209027 | 0.000004473941218 | 0.00000005386980324 |
| Maximum cut momentum error | 0.02825809083 | 0.0002135892288 | 0.0000007944363007 |

The cubic improves the maximum absolute and maximum node-relative errors
by factors about 8,553 and 1,896 in this one actual comparison. It is a
promising future warm predictor. It does not establish a Hessian remainder,
a convergence radius, a residual improvement or a saved Newton iteration.
The current q122 job remains unchanged.

The owned run formally exited zero after 4.963774677 seconds, with
79,828 KiB peak RSS and 88 explicit complete-data or comparison gates.
There were zero Node, ODE, Newton or residual evaluations. The primary
contains the full command and all consumed SHA identities; all inputs
remain immutable.
