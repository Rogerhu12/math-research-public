# Actual request42: a second complete-QR warm, with 32 requested working rows

Request42 continued the actual request40 warm with the unchanged complete-QR
entry and a requested working-row budget of 32. It accepted the first
nonlinear warm trial at alpha **1**. The current fixed-weight merit
decreased from **44.28521851182767** to **44.27560683679009**. All original
node, midpoint, and both RMS query checks passed at that trial. The fresh
affine physical-angle boundary Jacobian check also passed its unchanged
threshold. This remains a warm; it is not an accepted nonlinear
prefix/tail solution.

This note reports the small original JSON reports and necessary original
text excerpts available through the public GitHub connector. The large
artifact and its binary arrays have **not** been independently reread in
the current unavailable-terminal environment. The helper's last unrepaired
working-set result and internal radial factor are in the original
compressed report and are not inferred from the already-feasible outer
candidate.

## Execution and original identities

- Public run: [43623850723](https://github.com/Rogerhu12/math-research-public/actions/runs/43623850723).
- Prefix job **132535274004**, lane **twelvequeryqr**.
- Scientific source commit: **34abbdf26804307a61fa4d18139c969c1cf9c445**.
- Original artifact **14125192919**, **512553339 bytes**.
- Reported original ZIP SHA-256:
  **5a608eb40ae9f51b992111450e2a8ecdffa9fe96857813cabab2cc0563b193b5**.
- [Public output directory](public-actions-43623850723-1-twelvequeryqr).
- The original publisher recorded **2026-11-14T18:06:28.047968+00:00**.
- Warm, response, and publication completed successfully. This is job
  execution success, not the research completion criterion.

The actual parent is request40:

| Input | SHA-256 |
| --- | --- |
| Parent warm | c62a7f12db331993698ed7e5d9086193d8e43d399dbd98adb2b869430e19aeda |
| Paired parent status | 30f19320351f37344c5e75c6dd8614707f26692c7888c2d0eafcdb532f24d359 |
| Original prepared 699-node source | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| Original accepted M96 source | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| Actual T112 zero-height response/J | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| Actual T112 configuration | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

The entry remains geometry_20261114_twelve_query_qr_projection_warm.py,
SHA-256 **4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67**.
The complete chain QR source remains
**596356c06f710869b3bc26931ddaa87d66fe892bcf7920a25b42453b66bfa722**.
The helper remains
**d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c**.
No changed physical equation, scalar profile, native map, or original
nonlinear acceptance threshold is assigned to this continuation.

The preserved new outputs are:

| Output, relative to the public output directory | Bytes | SHA-256 |
| --- | ---: | --- |
| twelve-query-qr-warm/warm-001.json.gz | 4740550 | 3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317 |
| twelve-query-qr-warm/driver-status.json | 528261 | 26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04 |
| twelve-query-qr-warm/model-000.json | 246935 | fe7523e69982312d339d0bf0b99626cb266ff6cb5b1b7dae648a2c1afdb47f17 |
| physical-response/response-check.json | 321173 | 346a4f6a193b682f747c96dfb4408c62c17d4c4db850e8700717475d10db22d4 |
| twelve-query-qr-warm/full-H-result.json.gz | 1328308 | 0e57a7c02c2f1ceb85538ae5e0b33db532ac2139b17caf730ed90c1926a29884 |
| twelve-query-qr-warm/full-H-versus-C-comparison.json | 13430 | 5fc48cd7068d8b0b6f2f5e61bf673131ed6ed50195cac12cc7c957433db2a008 |
| twelve-query-qr-warm/full-H-final-selected-evidence.json | 13013 | aa8f3da16825c34c3ae1492f6e890bad0bd593b427784e247c122dc7a427d79b |

These are preserved producer/publication identities. Listing them is not
a claim that this connector-only review independently hashed the large
binary payloads.

## Same complete model and actual C/H comparison

The read
[block-qr-live-model-binding.json](public-actions-43623850723-1-twelvequeryqr/twelve-query-qr-warm/block-qr-live-model-binding.json)
records one CompleteLinearization construction and the same returned
original A object for the C and H choices. There are **236036** exact
coordinates and **24576** selected angle inequalities. The full B model
identifier is
**6cde0db22854b6d4e53069061ebe7f1a5cdecb7c7966dc5f58ba4b777a582b96**.

The current row-weight identity is
**1db36176916d0b51486482b98f70105b7384b9ece20653f962ec571df99d2278**;
the unchanged coordinate-scale identity is
**5e95867a8c414d43ed09592d07d494aba4643a636eeb3e76b45e8284524e9430**.

The damped model still uses lambda **270**. Only the baseline C projection
has correction support at nodes 471–482 and the three global controls,
with the complete outside offset retained. The H candidate still uses
all 236036 coordinates. The 12 selected queries remain nine left RMS
queries at intervals 470, 471, 472, 473, 475, 477, 479, 480, and 481,
and original collocation midpoints at 473, 475, and 477. Every query
contains all 2048 original physical-angle samples.

| Quantity in this one fixed model | Baseline C candidate | Selected complete-H candidate |
| --- | ---: | ---: |
| Damped objective | 44.28320644526789 | **44.27662694608533** |
| Actual original directional derivative | -0.0020154585881280774 | **-0.008625583545194881** |
| Damped model decrease | 0.0020120665597697326 | **0.008591565742343087** |
| Final reserve-slack minimum | 8.465450562766819e-16 | **3.3584246494910985e-15** |
| Final negative-slack count | 0 | 0 |

The helper was attempted, completed, and produced a usable direction.
Its recorded complete action counts are A **212**, AT **105**, B **181**,
BT **102**, and H **33**. The publication lists 33 individual inverse
reports, numbered 000 through 032. This count does not establish its
precise stopping reason or the accuracy of all individual inverses.

The C vector required full-vector radial factor
**0.0024643647594107024**, following slack minimum
**-24.11082862159513** and **258** negative slacks. The repaired original
raw ray used factor **0.00010487656730257165**. For the H vector supplied
to the outer selector, the additional candidate factor was 1, the
feasible-segment parameter was 1, and the final composed factor was 1.
These outer factors do **not** imply that the helper had no earlier
radial reduction. Its internal record remains a separate original file.

The final direction array identity is
**d94830f2b15b8fd27227a94f41d5786d22b64234a992230b550ea8222eda79b8**.
The saved full-model readout gives:

- Squared original weighted A action: **3.138871812579211e-05**.
- Damping penalty: **3.664688757779554e-05**.
- Scaled direction L2: **2.2420989938423077e-05**.
- Maximum coefficient direction: **1.3623824449870006e-06**.
- Final stationarity L2 with its reported multipliers:
  **992702.5381993352**.
- Best saved R267 lower-bound readout: **43.73844101866751**.
- Final cross-point gap readout: **0.5381859274178211**.
- Final cross-point distance-bound readout: **0.0038425311995731806**.

The R267 numbers are ordinary floating-point evaluations of the proved
algebra, not outward-certified enclosures. The final stationarity and
gap are retained. The warm success is not called a full-QP optimum.

### Two actual inverse reports, not an audit of all 33

The independent exact-refinement reader fetched the two small original
reports 000 and 032. The first is the center inverse (solve index 1);
the last is solve index 33 for original B row **15317**.

| Readout | Report 000 | Report 032 |
| --- | ---: | ---: |
| Original H residual L2 | 7.001149895483071e-10 | 1.2879118613795623e-10 |
| Original H residual relative value | 6.996961997768729e-16 | 4.643556735686165e-16 |
| Same-vector supplied/frozen A difference | 0 | 0 |
| Same-vector supplied/frozen AT difference | 0 | 0 |

Both bind the stated QR/entry sources, actual40 parent pair, lambda 270,
no extra column preconditioner, and one complete linearization. Their four
factor array hashes agree. The factors have no exported file and only
reported in-memory identities; this is not an independent factor-byte
audit. No assertion about the other 31 inverse residuals follows from
these two reports.

## The actual nonlinear warm trial

The first actual trial, alpha **1**, was accepted. Its unregularized
predicted reduction was **0.008609889186131986**. Re-evaluation of the
original nonlinear residual gave:

| Readout | Actual value |
| --- | ---: |
| Current fixed-weight merit before | 44.28521851182767 |
| Current fixed-weight merit after | 44.27560683679009 |
| Actual decrease | **0.009611675037582756** |
| Actual/predicted ratio | **1.116352932052175** |
| Node domain failures | 0 |
| Midpoint domain failures | 0 |
| Original left RMS invalid queries | 0 of 698 |
| Original right RMS invalid queries | 0 of 698 |
| Original uniform-phi rho minimum | 0.16604058243275 |
| Raw physical collocation maximum | **0.007110297531831894** |
| Complete physical-angle boundary maximum | **7.934223734010612e-08** |
| Left-boundary residual maximum | 0 |
| Constant-state collocation maximum | 0 |

Before the step, the physical maximum was **0.0071103080271700675**
and the boundary maximum **7.997334910447051e-08**. These raw maxima
differ from the weighted sum merit. No worst-cell or worst-Fourier-mode
location is invented from these saved scalars.

The original midpoint observer reported no bad midpoint on the initial
state or successful trial. Its flags say it did not recompute the whole
flow/Jacobian or alter the returned finite decision or residual bytes.
The actual nonlinear midpoint construction and all original query checks
remain in the trial evaluation.

| Query kind | Interval | Original minimum beta-squared | Angle index |
| --- | ---: | ---: | ---: |
| Left RMS | 470 | 0.11865918481579207 | 0 |
| Left RMS | 471 | 0.033511042449148376 | 0 |
| Left RMS | 472 | 0.13633518160395597 | 0 |
| Left RMS | 473 | 0.2821212589136618 | 87 |
| Left RMS | 475 | 0.14744340949894275 | 22 |
| Left RMS | 477 | 0.12204271364191199 | 970 |
| Left RMS | 479 | 0.15435216827418097 | 991 |
| Left RMS | 480 | 0.005372927139519534 | 0 |
| Left RMS | 481 | 0.08276776836676403 | 11 |
| Collocation midpoint | 473 | 0.0208697930947076 | 54 |
| Collocation midpoint | 475 | 0.12324908677998947 | 22 |
| Collocation midpoint | 477 | 0.33396148452879737 | 970 |

The left RMS fraction is the original **0.17267316464601146**.
Midpoint entries use the actual collocation midpoint, not that fraction.
Each minimum is an existing producer readout, not a local recomputation
or continuous-angle enclosure.

Weights were newly frozen for request42. Its initial merit
44.28521851182767 cannot be subtracted from request40's final
44.28040624161529 as if they were one fixed objective. The comparison
inside this execution uses exactly one fixed set of weights.

## Fresh affine boundary check

Necessary original summary and identity excerpts were read from
[physical-response/response-check.json](public-actions-43623850723-1-twelvequeryqr/physical-response/response-check.json).

- Maximum fourth-order Richardson relative directional error:
  **7.171478513023801e-10**.
- Maximum ordinary second-order error: **9.883446242732107e-06**.
- Original threshold: **5e-05**.
- Original contraction tests and implementation check: passed.
- Consumed warm SHA:
  **3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317**.
- Response source SHA:
  **721f6337fa5ef07684ff99775c9d4b8e8d98f4b3d3d6a7aa220111a1b4657367**.

This is the current complete affine physical-angle boundary map with the
genuinely computed zero-height T112 Jacobian held explicitly as an affine
anchor. It is not a fresh nonlinear native solution at the new endpoint
height. Neither this job nor this note changes that distinction.

## Evidence scope and the next concrete computation

The new checkpoint uses the same
**exact-constraint-twelve-query-complete-QR-H-alternative-warm-v1** schema.
It is not an accepted full BVP or closed large-amplitude family. The
small comparison explicitly records nonlinear native solved **false**
and full BVP accepted **false**.

This connector-only review read three complete small selection/evidence/
binding reports, two small inverse reports, and necessary model/status/
response excerpts. It has not performed a complete domain/full-H/QR
NPZ byte audit or read the compressed helper's last unrepaired stage,
stop reason, and internal repair. These missing facts remain missing
until the originals are read. A separate public Actions receipt-only
summary is prepared to SHA-bind and extract existing fields without
calling A, AT, B, a norm, or any scientific solver.

The proved [R270 condensation](../results/R270-exact-local-support-damped-QP-condensation.md)
gives a concrete implementation alternative for this same model:
retain all 4397 coordinates on which the complete B acts, eliminate the
outside variables with their full affine optimum, and keep all 24576
inequalities. The actual original gradient must pass through the
square-root affine right-hand side. This is source development; it does
not relabel request42 as a failed execution or claim that a new method
has already produced an accepted field. The recovered full vector must
still be compared with the original A/AT/B, the same fixed objective,
and the original nonlinear trial and boundary checks.
