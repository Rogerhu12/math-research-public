# PHI actual zero-prefix scalar-power failure and complete continuation

Session: `visible-exact-astra-fb31ed6-20261127`; date: 2026-11-27.

The explicit first continuation
[`45914123725/1`](https://github.com/Rogerhu12/math-research-public/actions/runs/45914123725)
finished with `failure`.  It ran one scientific child from
2026-11-27 00:01:48.749119 UTC through 00:02:11.262496 UTC, returned1,
and did not time out.  Its completed target set is empty, its accepted
whole-germ phase prefix is null, and no signed mathematical value is
claimed from its unfinished local work.

| Complete actual object | Bytes | SHA256 |
|---|---:|---|
| [Scientific result](strict_nu_phase_ci/run-45914123725-1/actual-strict-nu-phase.json) | 10102 | `cd4487056ad752ffdeda4fbf5ae70046e24cd6d2a4724ba97f6088b90411b407` |
| [Execution](strict_nu_phase_ci/run-45914123725-1/execution.json) | 32942 | `5975debd2466c29236dd54a3d4eb5bd598e70d186809d7712a8de5f5318a77c4` |

The idempotent 315-file input materialization worked.  All7721 original
body rows were admitted.  All four original NP arrays were necessarily
restored and read back with their exact original whole hashes and trial
definition `83da6322dbb4702fe6ae308acbcfb7bb1ed9410d17e0cded65bc1215dec233db`.
Old residual, norm and signed pairing counters stayed zero.  This
successful input restoration is retained separately from the failed new
phase calculation.

The new square-root jet then raised
`ValueError: finite explicit scalar polynomial coefficient`.
The complete original first-row input
`2026-11-14-R133-correlated-body-row0000-native.json.gz` is unchanged
(8201 bytes, SHA256
`feb3bbf9294dc995b88f5dc7c1e2ba866d3bd8c22dc84834dda7591cc9f644f0`).
Its full `K1` whole-row ball is `[+/- 0.252]`; the separately saved
whole endpoints also straddle zero.  Its negative-curvature denominator
is strictly positive.  The failure is not a lost curvature gap.

The original new PHI formula computes the cubic term as `r1**3`.
In the fixed runtime, [python-flint0.9.0 `arb.__pow__`](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/arb.pyx)
calls the generic `arb_pow`.  Its integer shortcut excludes a special
midpoint, including zero.  A nonzero-radius ball centred at zero can
therefore reach the logarithm path, which is indeterminate across zero;
see the primary [FLINT power implementation](https://github.com/flintlib/flint/blob/v3.3.1/src/arb/pow.c).

The successor uses the literal product `r1*r1*r1` for exactly this one
finite integer power.  This encloses the entire cube for every real ball,
including sign-changing balls.  The four original complete derivative
objects, both exponents `1/2` and `-1/2`, midpoint uncertainty, full
third-derivative remainder and all interval radii remain.  No absolute
value is substituted for a signed coefficient and no midpoint is used
as an exact derivative.  The metadata generator checks that this is the
only AST change in the overwritten function.  All other formulas are
loaded from the whole pinned first PHI math source.

The new worker explicitly admits both complete actual files and the
preceding manifest before continuing.  Original markers and failure
objects remain, and a separate consumed-after-45914123725 marker selects
one new public first attempt.  There are95 current files, the same315
historical files, and the same six still-missing targets.  The scientific
owner, original phase recurrence and original NP carrier restorer are
unchanged.  The corrected idempotent input lifecycle is retained.

No old phase residual, old phase norm, old NP residual, old signed waist
pairing, original QR or KAM target is recomputed.  Necessary input carrier
reconstruction remains separate from those targets.  Success still
requires the complete new signed phase integral, its entire field and
background error, and the true infinite-dimensional PDE error.  No
physical height, rigid-port or final Schur conclusion follows from this
implementation correction alone.
