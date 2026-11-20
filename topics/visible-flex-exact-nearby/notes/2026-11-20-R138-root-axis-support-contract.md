# R138 new two-scalar root input: execution contract

This is a new scientific target, not a replay of the old whole geometry.
Run it only in the repository's public GitHub Actions environment. The source
has received static AST and mathematical review; it has not been executed
locally. Root owns its eventual repository source path and workflow.

## New result and exact scope

The output encloses, at the genuine parameter-dependent root and at the
same reflection axis `phi=theta=0`, the two real numbers

    q = (F^{P,c} - (0,0,1/2)) dot X^{P,c}
    s = (F^{P,c} - (0,0,1/2)) dot n^{P,c}.

The centre is exactly the existing Qrepair definition
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`,
with the same whole-circle physical radial anchor, eta0 and nu0 as
`R138-supplement-actual-positive-support-for-repaired-physical-frame.md`.
Every actual positive candidate interface is retained. The vector state is
continuous there; the true coefficient one-sided values are used on their
original closed rows. At this reflection axis, the true angle fixes zero
on both sides, so there is no omitted angle-interface jump.

The output publishes only the two support coordinates, cumulative error,
counts, hashes, parameters and the associated conclusion. The original
root Fourier definition may be materialized privately by the separate
`private_root_angular_definition` helper inside a later angular consumer;
no new Fourier array or row coefficient checkpoint is published. This
axis result does not prove the full angular comparison, a root mean
denominator, root energy positivity, a full inverse, or the final theorem.

## Inputs, restored without recomputation

1. Original positive coefficient native, 6,223,338 bytes:
   `notes/2026-11-14-R133-current-positive-complete-ac1-native.json.gz`,
   SHA-256 `ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d`.
   Restore exact existing bytes from the old four-part index
   `notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json`
   or an already restored accepted copy. This consumer reads the 4,650
   original signed intrinsic/mean rows; it calls no old target or primitive.
2. Accepted joint root germ:
   `notes/2026-11-13-R133-actual-moving0765-physical-complex-turning-germ-native.json.gz`,
   SHA-256 `397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`.
   All real intrinsic balls and the complete root collar are consumed as
   stored, including the true K ball; no scalar germ is reevaluated.
3. Original candidate index:
   `data/phase_transport_resume127_20261114/candidate/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json`,
   SHA-256 `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`,
   with all five lossless npz.gz shards in its original sibling paths.
   Only the axis cosine-sum definition is materialized from exact binary
   coefficients. The old component norms,
   original residuals, old mean flow, and old geometry are not rerun.

Python dependencies are `python-flint` and `numpy`. The source sets Arb
precision to 320 bits before creating any new scientific interval.

## Command

```text
python fourfold_codazzi_root_axis_support.py \
  --positive <restored-positive-native.json.gz> \
  --germ <accepted-root-germ-native.json.gz> \
  --candidate <original-candidate-index.json> \
  --output <new-axis-output.json>
```

The source refuses scientific execution unless `GITHUB_ACTIONS=true`.
An interrupted successful prefix can resume with the same paths and
`--resume`; a complete or failed result is preserved. Every 64 rows the
current nominal two-vector and the cumulative Euclidean error are saved
with outward readback. The row polynomial stays in private memory; after
interruption its exact definition is materialized again, without replaying
any completed row propagation. Each new source or input identity requires
a new result path.

## Enclosure proof used by the source

On each original closed row, the new signed axis function is the stored
signed mean plus the exact physical-amplitude cosine-sum polynomial.
With `e=a*gamma`, `w=e*K*v_axis`, the accurate state solves

    (q,s)' = w [[0,1],[-1,0]] (q,s) + (e,0).

The reference row uses the midpoints of the two **complete row balls**,
and propagates their constant skew matrix and affine force exactly by
Arb sine/cosine. The row error is bounded by

    width * (rad(e) + (222/125 + 16*epsilon)*rad(w)),
    epsilon = 4/10^18.

This follows from variation of constants against the reference orthogonal
propagator, using the paid true Qrepair bound `|F-p|<222/125` and the
independent `16*epsilon` comparison to the original raw candidate.
No error norm receives a general matrix exponential. Every arithmetic
radius of the nominal row update is added to the Euclidean error before
the nominal state is replaced by its exact Arb midpoint.

The last segment from the fixed old body cut to every possible true root
is bounded using the stored full joint germ and its exact interval.
The original-to-Qrepair error is paid once by `16*epsilon`. Both arise
from the same exterior anchor. The output stores the actual cumulative
error and retains the actual interval rather than any root midpoint.

## Next consumer

Use the resulting two support coordinates to anchor one full `0..2*pi`
angular comparison in coordinates `X0=ez`, `Y0=ey`, `n0=ex`. Its whole
root input is the original degree-32 definition, materialized privately
over the complete true root interval, with the paid componentwise repair.
This local `ez` is
the fixed vector `ell=X(root,0)`, not the original world rotation axis.
The exact mean denominator in U.8 can use this `ell`; proving that
denominator nonzero also proves that `ell` has nonzero axial projection.

The full-circle comparison must preserve its holonomy and position end
defects and transfer to the one actual periodic physical radial frame.
The actual frame/position angular defects, including Qrepair and the
original joins, remain separate fees. The source intentionally marks
those conclusions false until their own new consumer proves them.
