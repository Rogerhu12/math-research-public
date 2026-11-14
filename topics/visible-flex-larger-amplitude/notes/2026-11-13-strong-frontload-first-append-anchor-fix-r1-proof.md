# First-append anchor repair for the original frontload provider

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

The original `NeckPrefix.__init__` initializes `Pieces(1.)` and calls the
overridable first append with only `kind`, `length`, `k0`, and `v1`. The base
`Pieces.append` subsequently copies the segment and injects
`a0=self.aend`, `s0=self.end`, and `h0=self.height`. The frozen frontload
override attempted to read `segment['a0']` before that injection. This is the
observed `KeyError('a0')` in the first nonzero frontload response column.

The fresh `strong_monotone_initial_speed_anchor.py` checks the complete
frozen original provider SHA, changes exactly the early argument
`segment['a0']` to `self.aend`, parses the transformed source, and verifies
that reversing this one edit recovers the original bytes. The argument is
therefore exactly the same current anchor that the original parent append
will inject. No physical formula, polynomial coefficient construction,
length equation, derivative-control gate, pulse exclusion, or other append
operation changes. The old source remains untouched.

Install the fresh adapter instead of the frozen frontload hook, after the
original angle and pulse hooks. Installing it over a previously installed
unfixed hook is an explicit error. Reinstallation of the fixed hook is
idempotent. The same fresh adapter and source identity must be used by any
future actual response, geometry, saved-field audit, or accepted solver that
uses nonzero frontload. The unchanged zero-weight candidate remains the
original physical metric.

The owned replay ended with exit 0 and 54 gates. It loads the actual accepted
q122 profile and the real provider, whose final source block installs the
angle-boost hook, then installs the original pulse and the chosen frontload
hook. The complete zero-weight segment metadata, profile metadata,
breakpoints and original scalar fields agree exactly. Nonzero weights
`-0.01`, `-0.005`, `0.005`, `0.01`, and `0.5` construct the entire prefix.
All binary Bernstein velocity controls lie in the actual `[0,vu]`, all
acceleration controls are nonnegative, the true parent append receives the
original radius/position/height anchor, and the new length propagates to
`S` and `Tu` as intended.

The endpoint definitions are checked explicitly: `(a,a_s,a_ss)` at the left
is `(1,0,k0)` and at the right is `(1+delta,vu,0)`, with the observed binary
roundoff bounded by the recorded 64-epsilon check. The complete prefix still
ends at the original loop radius. These are implementation and finite
endpoint checks. They do not certify continuous floating evaluation error,
produce a new BVP solution, or prove the new metric's isometry or reach.
No Flow, ODE, Node worker or Newton solve runs in this replay.
