# R133: actual cached cap L1 and reference endpoint consumption

This records the actual public run [43692857656/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43692857656), from commit `3b6640505d2434e1c739059d0e7df8ec1a8b3c89`. The scientific child returned **0**, all **12 gates passed**, and the scientific work took **0.646627987 seconds**. The conclusion is a bound for known sources through the complete reference Green operator, including its true radial endpoint kernels. Nonlinear endpoint invariance has not yet been proved.

## Object, coverage, and exact reuse

The object is the fixed repaired M32 centre at the original physical parameter
$\eta_0=-7789843107295549/4611686018427387904$, with affine parameter offset zero, on $[9/10,25/8]$. The original $\nu=-2572625729470897/72057594037927936$ and $\alpha=6890507429876859/9007199254740992$ are unchanged. The independent even mean is retained.

The consumer read the complete **7296-row** residual container and selected its **1341** actual cap rows. It combined the **949** original reference rows and their **1346** complete closed intersections with these residual rows, giving **1346** new common intervals. It consumed all original interval bounds, the true $9/10$ endpoint, the complete continuous-repair difference, and the complete intrinsic germs.

There were **zero** original target, primitive, residual-enclosure, reference Riccati, or matrix recomputations. The old whole-interval L1 totals were copied without reaggregation. The new calculations were the cap L1 and endpoint kernel integrals and the stated outer-domain checks. The 22 pinned inputs passed their byte checks; 17 were restored only into temporary storage from the fixed public history commit `7c130fb94528de8f003a43e7049fb42768a64eec`.

## Actual directed upper bounds

All displayed decimal inequalities below are rounded outwards from the actual Arb records.

| Quantity | Strict upper bound |
|---|---:|
| Moving $U$ residual in $L^1_r A_0$ | $8.373446755\,10^{-9}$ |
| Moving $V$ residual in $L^1_r A_0$ | $2.734939457\,10^{-8}$ |
| Physical ordinary $B$ source in $L^1_r A_0$ | $1.182296110\,10^{-8}$ |
| Physical ordinary $C$ source in $L^1_r A_0$ | $1.198310967\,10^{-8}$ |
| Reference pair from the known body source | $3.038615335\,10^{-7}$ |
| Reference pair from all known affine loads | $3.038615461\,10^{-7}$ |
| Nonmean $C(R)$ from the known body source | $2.379200346\,10^{-14}$ |
| Nonmean $C(R)$ from body and right $d$ load | $2.486289618\,10^{-14}$ |
| Left $C$ to right $C$ attenuation | $3.701695746\,10^{-9}$ |
| Right $d$ to right nonmean $C$ gain | $0.823763628$ |

The independent right $C$-mean load is bounded by $2.05\,10^{-19}$; the known right $d$ load is bounded by $1.3\,10^{-15}$. These are separate channels. The complete reference ordinary-source gains satisfy $G_B<9.664149355$, $G_C<15.822493239$; the retained complete $Q$ gain satisfies $K_G<15.952406835$.

The endpoint bounds retain the radial damping and the prefix coupling bound through every actual interval. They do not replace the endpoint kernel by a whole-cap operator norm. The known degree-96 residual is composed at each fixed radius with the certified inverse angle; the actual composition factor is below $4.260011779<5$. This step uses the stated reflection parity, while keeping the complete even mean. It does not extend that primitive-constant simplification to arbitrary directions in the full fourfold class.

## Actual outer-domain diagnostics

The same run checked two complete true-long value balls, each with normalized height radius $2^{-60}$. The table records bounds conditional on preserving the endpoint domain. The body radius in these checks is $\rho=2^{-15}$.

| Curvature radius | Long fixed-point contraction | Body linear-plus-outer coefficient | Formal body image | Formal body Lipschitz |
|---|---:|---:|---:|---:|
| $10^{-10}$ | $<0.000147457$ | $<0.826239959$ | $<2.571184292\,10^{-5}$ | $<0.838897509$ |
| $10^{-9}$ | $<0.001474561$ | $<0.878289250$ | $<2.730026121\,10^{-5}$ | $<0.890946799$ |

Both complete long-domain/image gates and the conditional body image/Lipschitz gates passed. The known reference endpoint column also fits the remaining domain room. **The unknown linear $Q$, quadratic $Q$, and outer endpoint feedback have not been included in an endpoint invariance proof.** Neither a nonlinear cap solution nor the full infinite BVP inverse is claimed.

The twelve actual gates cover the original three-part/7296 identity, fixed physical parameter and mean, exact reference/intrinsic identity, complete 1346 reference coverage, complete repair, 1341 actual cap rows, full degree-96 physical units, composition factor, both-mean reference gains, finite nonnegative weighted integrals, retained regular multiplier difference, and the requested true-long value balls.

## Auditable process and output identities

The small original records are in:

`notes/cached_cap_L1_endpoint_ci/run-43692857656-1-cached-cap-L1-reference-endpoint/`

| Record | Bytes | SHA256 |
|---|---:|---|
| `process.json` | 13372 | `b782c9a2834df60b7e0961fff17d2dbaca0b96d965b042f1a4194545ebb9b2dc` |
| `actual-cap-L1-endpoint-summary.json` | 27436 | `f5eea9a8a1b3f198e19c94a42cc3f794226b99cae65cefbd2e631134aff42c3a` |
| Full temporary scientific output, not persisted | 5761966 | `58b354c6e3b6e88571df54ebeff38a864349843e4c590dd2f6a3136533996911` |

The actual science SHA256 is `106ec9308882b814ca773da904e561e93aa4475f4f46f84b9632c9716653992f`; the deployed worker is `b807521600dda52e6e4ea79e4b4feb952dd939a195ea54ab74019d5cae17994d`; the deployed input manifest is `6378581473d45a1af2c55748ea13a5111a0563e4be183a0e56a5029f9c2021a5`.

The original reference/intrinsic/repair SHA256 values are respectively `ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b`, `3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22`, and `35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff`. The exact reconstructed residual container is `6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1`.

The child ran at 08:05:38.926418--08:05:39.926802 UTC on 2026-11-15. Actual pulls occurred at 08:05:30.186356, 08:05:37.622448, and 08:05:40.200486 UTC. The last read commit was `ed7bdaf8e87b0386bcb6166fd5450c1f11f5de48`. Both README diffs were empty at every check. The run followed the reproducible-data rules: no new numerical data, Actions artifact, or Release upload was persisted.

The mathematical contracts are the [cached endpoint contract](2026-11-15-R133-cached-cap-L1-endpoint-source-contract.md) and the [complete physical L1 and nonlinear body-ball proof](../results/R133-supplement-physical-cap-L1-Wiener-sources-and-practical-nonlinear-body-ball.md). The latter's endpoint-preservation obligation remains open after this successful known-source consumption.
