# Prefix-controls run: actual RMS domain failure and a targeted circle probe

## Actual returned computation

Public Actions run `43585737152`, source
`085dcb540a6a2d6ba1f223db37b8df4f9c14d64e`, returned artifact
`14110621529` (`visible-mainline-coupling-43585737152-1`).  Its new prefix
control RHS check and full boundary directional check completed.  The
coupled solve stopped in the expanded **domain preflight**, before any QR
factorization or any new tail request.  Thus this run neither accepted a
field nor tested the rank of the three new prefix controls.

The actual off-midpoint RMS fractions were
`0.17267316464601146` and `0.8273268353539885`.  The returned report gives:

| Mesh | Nodes | Bad lower-fraction queries | Bad upper-fraction queries | Total |
| --- | ---: | ---: | ---: | ---: |
| Original saved warm | 690 | 171 | 160 | 331 |
| New prefix-control support joins included | 696 | 171 | 160 | 331 |
| Those 331 bad positions inserted | 1027 | 444 | 402 | 846 |

The next insertion would exceed the declared 1200-node budget.  The driver
returned `phase="exception"` after `5.316184611000011` seconds with the
explicit RMS-domain budget exception.  No tolerance, node limit or branch
gate was changed to hide it.

All 331 first-round inserted positions are between
`s=1.4544146704921554` and `s=2.270143354423797`, after the original seed's
taper end `s=1.2856181831427507`.  Of these positions, 103 lie before the
turn end `1.7290454578568766`, 198 in the coast, and 30 in the finite bridge
beginning at `2.220792953504268`.  The first bad point has

\[
a=1.0774673869307716,\qquad
a_s=-0.7066140530028113,\qquad
\min_\varphi\beta^2=-0.0033732612859231903.
\]

The nearby saved samples include negative margins of order `1e-2`, so this
is not a residual at the scale of floating-point roundoff.  The count
increase under one insertion round does not establish that further mesh
refinement can never work.  It does establish that merely repeating the
previous midpoint preflight did not protect the actual RMS queries.

Relevant actual file digests are:

| File in the artifact | SHA-256 |
| --- | --- |
| `preparation/prepared.json.gz` | `c7641c5f72b4afaddc259fc2cca36b0d554b6d62372d22f3334dd375308145a0` |
| `full-DN/RMS-domain-preflight.json` | `f27d52100b0e71de9f5539bedb6ef6394e056d4e78361a3b1c8eeeabd3b8611f` |
| `full-DN/driver-status.json` | `d0e4fa228b36aad5690ba012cdc575334908ab7cc5c699b3e7dd99c2fa5ed0dc` |
| `scalar-RHS-response.json` | `31ca6f8640e2fc65438a71a9cd065ac315fddfde54d817d36a7b8a9fd4df0322` |
| `boundary-response/response-check.json` | `6355f32dfe993577efaefb6a3833c6c1108a45eae51c1397018df3c9493c6dc4` |

## An exact interpolation identity explaining what must be checked

The complete result, hypotheses and proof are in
[`R247-affine-coast-hermite-midpoint-blindness.md`](../results/R247-affine-coast-hermite-midpoint-blindness.md).
In particular, R247 distinguishes the domain check from the collocation
residual, which does detect the derivative mismatch.

Let the fixed material angle be

\[
\Phi_c(\varphi)=\varphi+
\sum_{m=1}^{96}\frac{1-4m^2}{2m}c_m\sin(2m\varphi),
\quad \rho_c=\partial_\varphi\Phi_c.
\]

The full material circle in the rotating frame is
`C_c=(cos(Phi_c-phi),sin(Phi_c-phi),0)`.  The existing seed uses its finite
projection `P_M C_c`, not the complete analytic circle.  Even though the
core has 96 modes, this nonlinear angular reparameterization generally has
infinitely many modes.  The actual saved core includes nonzero modes
33–96: the maximum `(1+4m^2)|c_m|` in modes 33–64 is about `4.65e-5`, and
in modes 65–96 about `3.29e-5`.  These modes must remain in every diagnostic.

On a coast with constant `a_s`, the finite seed

\[
y(s)=a(s)P_M C_c+Z(s)e_{z,0},\qquad
Z_s=\sqrt{1-a_s^2},
\]

is affine in `s`.  Scaling a fixed latitude by `a` scales its curvature by
`1/a`; hence the original finite Frenet velocity and its projection `f`
are independent of `s` on that coast.  They need not equal the derivative
`v` of the seed.  The cubic Hermite interpolant with the seed's endpoint
values but the original ODE's endpoint derivatives satisfies the exact
algebraic identity

\[
y_H(s_i+th)=y(s_i+th)+h\,t(1-t)(1-2t)(f-v).
\]

At `t=1/2` this correction vanishes.  At the two RMS fractions it equals
`±h sqrt(3/7)/7` times the full derivative mismatch.  In particular, when
the node height has zero nonmean coefficients but the finite RHS has
nonzero high height modes, the two RMS queries receive opposite height
wiggles.  Taking two angular derivatives amplifies mode `m` by `(2m)^2`.
This identity supplies a mechanism for the midpoint/RMS discrepancy.  It
does not by itself quantify the actual derivative mismatch or establish
which M/N change is sufficient; the probe below measures those quantities.

For the **untruncated** physical circle

\[
F=a(s)(\cos\Phi_c,\sin\Phi_c,0)+Z(s)e_z,
\]

the complete angular derivatives are

\[
F_\varphi=a\rho_c e_\theta,\qquad
F_{\varphi\varphi}=a(\rho_{c,\varphi}e_\theta-\rho_c^2e_r).
\]

When `rho_c>0`, these give `kappa=1/a`, `alpha=-a_s`, and
`beta^2=1-a_s^2`.  Every high angular mode participates in this identity.
Removing their contribution is not a valid way to make the original
finite field satisfy the exact-circle equation.

## Independently named short Actions probe

The new entry point is
[`geometry_20261114_material_circle_domain_probe.py`](../computations/geometry_20261114_material_circle_domain_probe.py).
It consumes the two actual files above, reconstructs the same frozen
scalar formula, preserves all 96 original core coefficients, and selects
only actual bad intervals and a few turn/coast/bridge representatives.
It does not scan the whole 690-node curve again.

The default cases are `(M,N)=(96,1024),(96,2048),(112,2048),(128,2048),
(160,4096)`.  Appended core coefficients are exactly zero; original
coefficients are neither damped nor deleted.  It records:

1. Replay of the original saved endpoint RHS and saved Hermite curve.
2. First/second angular error and curvature error of the finite circle
   projection relative to the complete analytic circle.
3. The original finite RHS minus the derivative of the analytic seed,
   with the full sampled even spectrum of the height velocity, including
   frequencies beyond the field cutoff.
4. Actual finite-RHS Hermite margins at both RMS fractions and the
   midpoint.
5. Separately labeled compatible-circle-derivative and untruncated-circle
   references.  These comparisons never replace the ODE derivative in
   item 4.

Example from a public Actions checkout, with `A` the original artifact
directory and `OUT` a new output directory:

```sh
python "$C/geometry_20261114_material_circle_domain_probe.py" \
  --warm "$A/preparation/prepared.json.gz" \
  --rms-report "$A/full-DN/RMS-domain-preflight.json" \
  --out "$OUT/material-circle-domain-probe.json.gz"
```

The module requires the existing public Python sources and NumPy/SciPy;
it does not initialize the true tail or a Newton factorization.  Source
hashes and original input hashes are written into the report, and each
completed M/N case is saved before the next begins.  At creation only an
AST parse was performed locally.  Its numerical result must come from
the public repository's Actions.

## Possible subsequent representation change, not yet a solver result

If the probe confirms that the circular projection is the dominant source,
one candidate is to retain its complete analytic high-mode remainder as
an explicit part of the field,

\[
F=Y_M+\chi(s)a(s;p)(C_c-P_M C_c),
\]

where `chi` is identically zero on the accepted prefix, turns on with
zero first/second endpoint jets, and equals one on the circular region.
That is a new, completely specified field representation.  It would
require a new projected evolution equation, explicit core and scalar
derivatives, source-bound serialization and full-field geometric readout.
In particular, the previous argument that the local RHS has zero explicit
core columns would no longer apply.  The existing finite field, its
acceptance gates, and its saved failures must remain unchanged.  This
note does not assert that the enriched equation has been implemented,
that its Newton problem is nonsingular, or that a complete tail/closed
surface has been obtained.
