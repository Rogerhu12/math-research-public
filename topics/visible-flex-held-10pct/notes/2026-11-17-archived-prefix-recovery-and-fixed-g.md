# Archived short-prefix recovery and one fixed-metric refinement

Session: held10-true-a-prefix-analysis, 2026-11-17.

These files reproduce two **finite open prefixes**. They do not produce a
closed surface, an exact nonlinear tail, a fixed holding patch or a reach
certificate. The old q20 point-cloud ratio of about 13.246% therefore does not
satisfy this topic's completion criterion.

## Immutable inputs

`prefix_recovery_manifest.json` names every individually fetched Git path,
full commit, byte count and SHA256. The two archived state/coefficients/summary
triples come from `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`. The small Python
source closure and linear port come from
`46fe93d4bb708fdfb7935e91b8141ea77586f0d2`. The manifest contains 23 source files
and six checkpoint-related files, about 2.32 MB in total. A sparse,
`--filter=blob:none` clone suffices: `git show <commit>:<path>` lazily obtains only
these explicit blobs. The tool writes recovered arrays and source copies to a
chosen directory outside the repository.

The first clean recovery exposed an unregistered dynamic import of
`950f-prefix-flat-accel-screen.py`; that source is now explicitly in the
manifest. A second clean run succeeded. Every field of the regenerated q20
endpoint array was compared with the previously reconstructed array and was
bitwise equal (maximum difference zero).

## Recovery and endpoint interface

From this topic's scripts directory, run:

```bash
python recover_prefix.py --repo /path/to/math-research-public --dest /path/to/scratch/held10-prefix
```

The default outputs include `restored_prefix/q18_endpoint.npz` and
`restored_prefix/q20_endpoint.npz`. Their fields are `X`, `Xs`, `Xss`,
`Xtheta`, `Xthetatheta`, `Xstheta`, `theta`, `s`, and `height`; the six array
fields have shape `(512,3)`. The meridian derivatives use the physical
unit-speed terminal coordinate, and the angular chart is checked to be the
identity at the terminal circle. The mean height, mean vertical velocity and
mean vertical acceleration are added from the full Frenet velocity, so the
stored nonmean height is not incorrectly treated as the full position.

For q20 the endpoint is at `s=1.628925980576648`, mean height
`1.2879820451408475`, mean vertical velocity `0.44848922954447534`, and mean
vertical acceleration `3.693567419027544`. The sampled largest norms of the
first and second meridian derivatives are `1.0000000000625848` and
`4.268594221955577`.

Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0 were used for the new run. Exact
checkpoint gzip bytes may depend on timestamps; the manifest hashes bind the
archived input files, not a claim that every future gzip output is byte-identical.

## New fixed-metric q18 computation

The archived q18 design is outward `vu=.55`, `vd=.6`, `ramp=.4`, one cycle,
flat acceleration law with `ramp_eta=.05`, `r_cut=.6`, and `w_cut=.5`.
Its physical design parameter is frozen at
`delta=.17053856686761762`. The same archived adaptive angular chart and
`warp_reference=.18` are used at every refinement.

| Finite prefix | Modes | Nodes | Max collocation residual | Sampled metric L1 | Sampled max principal curvature |
|---|---:|---:|---:|---:|---:|
| Archived design | 10 | 496 | 1.9584543e-6 | 1.6170394e-6 | 6.1616262 |
| New fixed profile | 16 | 1479 | 1.9969332e-8 | 2.5485326e-7 | 6.1628348 |

The new solve succeeded in about 125 seconds. Its actual primary support
amplitude is `0.18000025079843018`, maximum sampled height
`1.302122630678921`, maximum sampled radius `1.2529820466339898`, and largest
terminal nonmean height coefficient `0.009763646606006203`. The sampled flow
defect decreased from `4.76419399e-6` to `6.10036265e-7`; the Darboux L1 defect
decreased from `0.00154520821` to `0.000313659017`. These latter defects remain
substantially larger than the collocation tolerance, so this is evidence of
improvement, not a completed convergence certificate.

The q18 M16 state file SHA256 is
`579db14b1d762b54a2058ed21221adf124d65a1bdb511af18d73fa7d2af4f3fa`;
the coefficient file SHA256 is
`134083d18ecea180c52dbd60e2c0004e9b85198981b46b9ed60f9a0fd6036454`.
The state and coefficient files remain outside the repository.

The exact launch arguments are in the manifest. To repeat the computation:

```bash
python recover_prefix.py --repo /path/to/math-research-public --dest /path/to/scratch/held10-prefix --refine q18-fixed-m16 --endpoints q18-fixed-m16
```

A following M24 fixed-profile refinement is also specified by the manifest:

```bash
python recover_prefix.py --repo /path/to/math-research-public --dest /path/to/scratch/held10-prefix --refine q18-fixed-m24 --endpoints q18-fixed-m24
```

It uses 24 modes, angular quadrature 768, audit quadrature 1536, tolerance
`2e-9`, 1501 requested initial radial nodes, and at most 6500 nodes. If M16 is
absent the script first runs M16. The M24 entry is a reproducible requested
experiment; no successful M24 outcome is claimed in this note yet.

## Scope of the remaining geometric problem

The q18 terminal height is still about `0.00976`. An exact closed family
requires a nonlinear tail accepting the whole terminal Fourier vector and
matching the prefix jets, plus the infinite closure, fixed caps, global
separation, held Hausdorff lower bound and all-phase reach. Independently
thickening the old tail changes its metric and its Dirichlet-to-Neumann map;
any improved tail must therefore be coupled to a new prefix solve. Increasing
the tail height allowance from about `.05` to `.20` can preserve the old cut
and sampled background curvature, but does not alone preserve the linear
stable direction.
