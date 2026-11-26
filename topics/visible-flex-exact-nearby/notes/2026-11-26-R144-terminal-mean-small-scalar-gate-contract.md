# R144 terminal mean small-scalar gate contract

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

This is one new scalar gate target for the fixed original raw eta0/nu0
centre. It implements
[TM1--TM5](../results/R144-supplement-terminal-mean-small-ball-controls-normalized-forward-constant.md),
proof SHA256
`5a7a5bf8b6873976d173bfc5be8c3b25fbcd03174e97ba56a4abd99e06440986`.

It does not scan or restore a native, call a radial ODE, recompute an
old Green maximum, run a primitive or DFT, or read an uncompleted
future forward endpoint.

## 1. Exact complete small inputs

The new actual C0/profile result is run45787608966/1, with all
7721 closed cells, 6143 mean interfaces, 7721 reverse rows and 52
whole scalar fields complete:

- science SHA256 `0ce421d4a1e14a57915531261c531ce8231a8874aba5dfd704d37f67bb8d7641`;
- execution SHA256 `9e21d438e609b207274e6a510d7e7b3ce87522e19a3547635206ab609a91bedc`.

The consumer verifies the actual complete science and execution,
the same original candidate and mean native, the complete counters,
the strict compact-leverage gate, and the exact fixed parameters.

The already completed full-eta original forward result run45772466407/1,
SHA256 `7cddc5856510c7e602a2e22d504492c8ab4732f900331c02e646f14b04da1635`,
is read **only for its saved initial field**
`complete_new_scalars.initial_D`. Its completed signed forward flow
and unknown gates remain unchanged and are not evaluated again.
This original initial-value enclosure includes the fixed centre.

The old complete mean readable result, SHA256
`232a4bf0741eed57c5d5ae7e149795df1541e05236dc7afa05a60dc997094991`,
is read at the exact whole field

`complete_waist_mean_gain_if_log_Gamma_below_100/ordinary_mean_source_L2_r`.

Its full saved ball, with the saved radius, is the original
ordinary-mean $L^2_r$ to waist-value norm. The old whole-body
$L^2\to L^2$ constant is not substituted for it.

The original raw residual note, SHA256
`84ae53db92194d7ff9753aa6f3a37e0042462d138e7effaede8756156f65671e`,
supplies the normalized bound $8.194504\,10^{-8}$ for the second
ordinary residual. The physical source bound multiplies by the
original exact $\alpha$ once.

All input paths, full bytes, Git blobs and SHA256 values are pinned.
The scientific source also verifies these full SHA256 values.
No historical large container is an input of this target.

## 2. Five dependent mathematical stages

First form $E_*=K_0R_*+K_JJ_*$ from the actual complete fields.
For $\xi=0$ propose a radius using the whole upper of

$$
 b_0^{\rm proposal}
 =\frac{17E_*^+}{16(1-C_{10}^+)}.
$$

The denominator gap must be positive, and the actual saved values
must still pass $b_0<m_*$, the CP self-map inequality and its strict
Lipschitz inequality. No proposed radius proves its own gate.

Second, the already proved zero-parameter terminal solution has
waist bound

$$
 b_w\le\min\left[
 b_0,\ L_{w,2}E_v+K_JJ_*+
 C_{10}b_0+C_{20}b_0^2+C_{30}b_0^3\right].
$$

Using the saved $d_0\ge|D_0|$ and $t=b_w/m_*<1$ gives

$$
 |\overline D|
 =|D_R/H_R|
 \le d_0+(1+d_0)\frac{t(2-t)}{(1-t)^2}.
$$

This is TM7, derived from the terminal solution and the exact common
linear equation. It is a new absolute bound, not another evaluation
of the old signed W or D flow.

Third, propose the compact parameter radius from the whole upper
of $17d/(16a_-)$ and verify both $0<\rho<1$ and the strict root
inequality $d<a_-\rho(1-\rho/2)$.

Fourth, form the complete CP profile polynomials $A_0,\ldots,A_3$
at this same $\rho$. Propose the uniform mean radius from
$17(E_*+A_0)^+/(16(1-A_1^+))$, verify its positive denominator,
and check the actual uniform self-map, Lipschitz and negative-mean
inequalities.

Fifth, check the independent density gate
$8\rho\sqrt{V_*}<g_*$. Also evaluate, separately, the sufficient
same-material-angle bound

$$
 b\big(1+(1+\rho)8Z_*\big)+8\rho\sqrt{V_*}\le10^{-4}.
$$

This last inequality does not control physical-angle composition.
Its failure does not invalidate a separately proved mean root,
and is not a geometric nonexistence result.

## 3. Whole-file readback and exact radius convention

Every new derived upper is stored in the complete decimal-ball
format, atomically written, and actually parsed from the saved
output before a dependent expression uses it. No saved radius
is discarded.

If a proposal is stored as $(m\pm r)10^e$, the exact rational
radius is $(m+r)10^e$, constructed with integer/Fraction arithmetic.
It is not $m10^e$, a binary floating point conversion, or a guessed
short decimal. The rational string is also saved and read back
before evaluation at that radius.

The root test requires a lower bound for its right side.
The consumer saves and reads a separate complete lower record
for $a_-\rho(1-\rho/2)$. An upper right side is never used to
prove this inequality.

All complete dependent gates are saved and read back before
`complete` and `proved` can become true. A runtime exception
resets both to false and preserves the last complete scalar
prefix with its actual error.

If a sufficient gate fails, the declared attempt ends with
`complete=true` and `proved=false`, the exact first failed
gate, the saved preceding scalars and remaining unknown gates.
It is a complete failed sufficient test, not a failed execution
and not proof of nonexistence. No automatic retry or unrecorded
radius adjustment occurs.

## 4. Meaning of a successful outcome

A successful `proved` flag proves an exact compact mean root
for the original raw fixed metric, a strictly negative whole
terminal mean with positive $Y$, and a positive material density.
The same scalar solution has the prescribed waist mean and
returns to the original outer mean.

It does not solve the ordinary nonmean equations or their actual
joins. It does not inherit the selected phase or inverse, establish
physical-angle closeness, repair radial cap jets, match height,
or complete the final closed fixed-metric family. The source
computation in CS and all physical comparisons retain their own
exact inputs and obligations.

The worker uses the same public-only runtime, current-input and
AST admission, real pull/rebase and immediate README checks,
capacity accounting, separate consumed marker and non-fast-forward
publication retry as the preceding public entries. It publishes
only the small scalar outcome, exact radii, counts and full hashes.
There are no arrays, artifacts or Releases.
