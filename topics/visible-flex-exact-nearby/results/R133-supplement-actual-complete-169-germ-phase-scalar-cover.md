# R133 supplement — the actual complete 169-germ phase scalar cover

## 1. Exact scope and completed result

The complete high-seven scalar cache now covers

$$
 I=[0,r_b],\qquad
 r_b=\frac{1249886203106135147}{5242880000000000000}
     =r_{*,\mathrm{lower}}-2^{-32}.                         \tag{S.1}
$$

The actual affine parameter is fixed at $\eta=\eta_0$, equivalently its
offset is $\delta\eta=0$. The compact metric parameter remains

$$
 \nu=-\frac{2572625729470897}{72057594037927936}.             \tag{S.2}
$$

There are exactly 169 genuine target/bump germs and 626 accepted Taylor
cells. The stored 457 rejected adaptive cells remain in their original
native reports. The largest actual adaptive depth is 24. No interval
crosses a genuine target or compact-bump germ. All five scalar functions

$$
 \beta,\quad K,\quad s,\quad\gamma,\quad q=\sqrt{-K}         \tag{S.3}
$$

have explicit exact dyadic degree-seven models on every accepted cell,
together with complete uniform value errors. The complete angular
exponential and primitive tails are included. This statement concerns
the actual intrinsic target, not a finite Fourier truncation of that
target.

The actual integrated complete scalar errors, re-summed directly from
all model remainders, satisfy

| Scalar | Strict upper bound for the integrated complete error |
|---|---:|
| $\beta$ | $1.250485\,10^{-21}$ |
| $K$ | $9.415570\,10^{-16}$ |
| $s$ | $5.058810\,10^{-16}$ |
| $\gamma$ | $2.258182\,10^{-16}$ |
| $q$ | $3.565935\,10^{-14}$ |
| Their sum, evaluated before display rounding | **$3.733261\,10^{-14}$** |

In particular

$$
 \sum_{J\text{ accepted}} |J|
       \sum_{f\in\{\beta,K,s,\gamma,q\}}\epsilon_{f,J}
 <3.733261\,10^{-14}<2^{-42}.                               \tag{S.4}
$$

Every true negative square-root branch is strictly positive. The weakest
saved whole-cell bounds still give

$$
 q>0.0001024061486286682,\qquad
 K<-1.3774837808160772\,10^{-8}.                            \tag{S.5}
$$

These are conservative minimum/maximum bounds over the entire completed
cover. They are not assertions about the missing positive side of the
root. The final root sliver is handled by the separately proved actual
two-ray cancellation theorem.

This result completes the scalar-cache obligation on (S.1). It does not
by itself prove a true return, circle conjugacy, phase arithmetic for the
actual return, parameter inverse, or body inverse. In particular a bound
for a scalar model error must still be multiplied by the true field and
transport factors when consumed by the phase PDE residual.

## 2. What was computed and what was only consumed

The mathematical producer and complete scalar-jet provider are the ones
proved in
`R133-supplement-complete-Arb-scalar-jets-and-directed-high-Taylor-models.md`.
Their exact SHA256 values are

```text
cache source:
972790fc21768745cdbc9c842187f5a283e65a8a4f53ac948e86f67250780f61
complete scalar-jet provider:
b57e794709edcb8c3281df909f463a56a906aec8a8ba8a8b3f49394f10e4590f
```

The previously completed genuine germ zero was reused with native SHA

```text
b6f1892d8d09749a7279e23c86d5cca622785b919891bf8a0e46c3add382aa01.
```

The other 168 germs were actually computed in the public repository's
own GitHub Actions run `43573003976`, by four disjoint ranges:

| Range of germ indices | Number of complete reports | Actual child exit |
|---|---:|---:|
| $1\le j<43$ | 42 | 0 |
| $43\le j<85$ | 42 | 0 |
| $85\le j<127$ | 42 | 0 |
| $127\le j<169$ | 42 | 0 |

The complete original process records, logs and range manifests are in
`notes/phase_scalar_high7_ci/run-43573003976-1-germsNNNN-MMMM/`.
All four published process records declare successful completion and
retain their actual terminal exit, exact source/input verification, and
README checks. Their checkpoint worker SHA is

```text
602e696db855f1aca2765bef23fd7d9190c1fdd6d4f05528b758e0a515167323.
```

All ranges use the same 52-item pinned scientific input manifest

```text
eb25464d038f44dc87a8214662ec9275250fc414c42ca04c9763bf08f8802535.
```

No private candidate replay is an input to these intrinsic scalar jobs.
The actual near-body target and its two complete affine NPZ inputs are
the public same-object inputs already listed in that manifest. The
maximum actual one-sided exponential frequency cutoff was 456; its
complete tail was bounded, not set to zero.

The earlier run `43572460867` failed before any mathematical child due
to a worker entry-name collision. Its actual four process/trace records
are preserved in
`2026-11-14-R133-phase-high7-CI-first-run-entry-failure.json`.
That failure was not changed into a successful scalar computation. The
separate old cap-six jet-truncation attempt remains excluded.

The new cover consumer only reads the completed reports and re-sums
their mathematical bounds with 256-bit Arb arithmetic. It does not
reevaluate any primitive, exponential, whole derivative, or candidate.
The actual cover check took 1.12 seconds and passed eleven gates.

## 3. Why this is a complete cover

For each index $j$, the consumer checks the full configuration, original
producer/provider SHA, all six original mathematical gates, and the
native SHA recorded by its successful range manifest. The exact
rational intervals of successive germs must meet and must occur once
only, starting at zero. Inside a germ the accepted exact rational cells
must also meet in order and end at the original genuine germ endpoint.

Every accepted cell additionally checks its centre and containing actual
scalar germ, all five model entries, eight exact dyadic polynomial
coefficients, seven normalized point jets, and the complete high-jet
exponential-tail declaration. The strict signs in (S.5) are checked on
the original whole-cell true-value enclosures.

For each scalar model the consumer evaluates

$$
 |J|\,\operatorname{upper}(\epsilon_{f,J})                  \tag{S.6}
$$

with outward arithmetic. It sums these quantities independently of the
old displayed germ totals. The resulting sum must remain below that
germ's original lower allocation. The resulting full sum must remain
below the global exact allocation $2^{-42}$. Thus neither a printed
midpoint nor a gap between accepted cells can hide in (S.4).

The 626 accepted cells, all field remainders, original failed subdivision
records, and their exact model coefficients remain available through the
169 original SHA-bound natives. The aggregate report lists all 169
paths, SHA256 values, exact intervals, cell counts, and reconsumed scalar
fees, plus all four actual process records. This avoids a redundant
copy of the same intermediate models.

## 4. Files and exact reproduction

- `scripts/fourfold_codazzi_phase_complete_scalar_cache_cover.py`
- `notes/2026-11-14-R133-complete-169-germ-phase-scalar-cover-native.json.gz`

From the topic directory after the four actual CI result directories are
available:

```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps python -u \
  scripts/fourfold_codazzi_phase_complete_scalar_cache_cover.py \
  --out /path/to/new-complete-scalar-cover-native.json.gz
```

The first-germ/native and actual run ID have explicit defaults; the
command can select their exact paths with `--first`, `--ci-root`, and
`--run-id`. The consumer refuses an existing output, a failed process,
an altered input manifest, a missing field/germ, an unproved square-root
sign, or an exceeded original error allocation.

The next chronological consumer is the exact finite phase transport in
`R133-supplement-complete-finite-phase-transport-and-all-frequency-residual.md`.
It retains all $N+64$ output frequencies of the projected $N$-mode
reference, both actual mean-speed terms, and exact matching of its phase
values at every original candidate/scalar interface. The present scalar
result supplies all of its required intrinsic germs without enlarging
the affine-parameter scope.
