# R133 supplement: actual complete old-circle inverse remainder source budgets

2026-11-14, phase_inverse.

**Actual public computation completed.** Public
[run 43629465215](https://github.com/Rogerhu12/math-research-public/actions/runs/43629465215)
returned mathematical status zero, passed all seven gates, and paid the
complete old-circle inverse and independent even-mean source terms on
all 1328 saved common rows and all six root windows. The resulting bounds
are finite but very large. They do **not** prove a small strong-return
remainder or the cutoff-97 inverse.

The exact operator being bounded is the leading-column nonlocal and
mean remainder in
[U.14--U.29](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md).
The numerical rule is
[B.1--B.13](R133-supplement-real-root-remainder-budgets-and-radial-matrix-parts.md).
The local term $\mathcal L_0w_1$ and the complete corrected return operator
remain outside this calculation.

## 1. Actual execution and immutable evidence

The workflow event and actual immutable scientific checkout were both
`2e4825ab88e542428702c5a432d93f186b55d9fc`.
The mathematical child took 52.329909693 seconds. It computed 1328 new
coefficient norm rows, with zero such rows reused from a prior attempt.
It reused the already completed coefficient, forcing, fold and seam
objects; the number of new target, candidate, response, ray or amplitude
solves was exactly zero.

| Evidence | SHA256 |
|---|---|
| Mathematical source | `56b68983f36bb3d88e1427081ba9e60a8f6cf43dcd9578a0d925e1834292555d` |
| Fifteen-file input manifest | `7290cbb07293c15a239ffafb0e342e6c1b7ea812106f569e88bbe4d2502180df` |
| Complete new native, 4,837,715 bytes | `7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c` |
| Mathematical process receipt, 48,987 bytes | `f888e47e69f41b4b5c73656ac9afd321289a806ce948816d9612111a045d99e4` |
| Actual worker receipt, 2,772 bytes | `5938996acf66b44ee3f8adf06955a53a06a0fadc685e663f6883ef5e2864fdb6` |

The complete native and both receipts are under
[the actual run directory](../notes/leading_old_circle_remainder_sources_ci/run-43629465215-1/).
The mathematical receipt is
[consumers/process.json](../notes/leading_old_circle_remainder_sources_ci/run-43629465215-1/consumers/process.json);
the original native is
[consumers/leading-old-circle-remainder-sources.json.gz](../notes/leading_old_circle_remainder_sources_ci/run-43629465215-1/consumers/leading-old-circle-remainder-sources.json.gz).

The three consumed original natives remain:

| Original object | Actual public run | SHA256 |
|---|---:|---|
| Complete piecewise root fold, 1300 rows | 43616813816 | `dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212` |
| Complete first forcing, 1328 rows | 43624260519 | `54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47` |
| Complete first seams, 1079 seams | 43625828234 | `871aa54de8c4ee1caa47cdab39c8033bb9cd02e9d4d1f404b711ab8c28825642` |

The worker records two real pulls. The first remained at the scientific
commit; the second advanced to
`46d6140c760b58a111c15ef8aef1ca808e713275`.
Both root/topic README diffs were empty. The checked rule hashes and
reviewed README commit remain explicit in the worker receipt.

## 2. Exact family, source norm and cover

The input is the same explicit real parameter family
$|\delta|\le10^{-8}$, at the fixed $\eta_0$, with the complete original
65-component candidate and complete repaired 193-component direction.
The genuine root interval is
$$
 r_*\in
 \left[
 {1191984371497\over5000000000000},
 {2383968743003\over10000000000000}
 \right].
 \tag{O.1}
$$
The full common cover is
$$
 \left[
 {1091984371497\over5000000000000},
 {2583968743003\over10000000000000}
 \right].
 \tag{O.2}
$$
Every radius case includes the original root uncertainty. The input
Fourier window is $|j|\ge97$, physical frequency $n=4|j|$, with density
column normalization $n^{7/6}$ and input space $H^{-4/3}$.

Let $\mathcal E_{\rm old}^{\pm}(R)$ be the complete first-row old-$I/J$
source and independent second-row even-mean source for the leading
column, on the indicated side of the true root. Their output source
space is
$$
 L^2_r\bigl(H^{-2/3}_{\phi}\times H^{-1}_{\phi}\bigr).
 \tag{O.3}
$$
The receipt labels both source entries by $H^{-2/3}$. Its second entry
is solely the independent even constant mode, so its $H^{-2/3}$ and
$H^{-1}$ norms are exactly equal; (O.3) makes no additional regularity
claim or change of numerical gain.

All Fourier outputs are retained. In particular the input cutoff is
not imposed on the output, the old projections remain in their original
order, and the even mean is not set to zero.

The radial scalar integrals bound the common envelope
$|\rho|^{-1/4}$. Inside the uncertain root bracket the negative and
positive parts each receive their own $2\sqrt{\text{cell length}}$
bound for the squared envelope. The positive source is additionally
split at the actual fixed cut
$$
 r_b={1192029371497\over5000000000000}.
 \tag{O.4}
$$
This only separates the raw collar/body source norms. It does not apply
a given-head positive high graph to the entire low/mean system.

## 3. Actual complete volume source bounds

Every entry below is rounded upwards from its directed native record.
The columns are operator-norm upper bounds for (O.3), not lower bounds
for the actual error.

| Radius $R$ | Complete common rows | Negative source | Positive collar source | Positive body source |
|---:|---:|---:|---:|---:|
| $1/1000$ | 144 | $1.524430\times10^{18}$ | $6.335406\times10^{16}$ | $1.952137\times10^{17}$ |
| $1/500$ | 274 | $5.284810\times10^{18}$ | $1.835025\times10^{17}$ | $6.799788\times10^{17}$ |
| $1/200$ | 627 | $3.772746\times10^{19}$ | $1.029725\times10^{18}$ | $4.774952\times10^{18}$ |
| $1/100$ | 898 | $1.810496\times10^{20}$ | $4.228701\times10^{18}$ | $2.264829\times10^{19}$ |
| $3/200$ | 1106 | $3.895247\times10^{20}$ | $8.635468\times10^{18}$ | $4.939566\times10^{19}$ |
| $1/50$ | 1328 | $6.484752\times10^{20}$ | $1.410761\times10^{19}$ | $8.357174\times10^{19}$ |

The corresponding full positive source bounds are, in this order,
$2.052368\times10^{17}$,
$7.043041\times10^{17}$,
$4.884721\times10^{18}$,
$2.303968\times10^{19}$,
$5.014482\times10^{19}$, and
$8.475412\times10^{19}$.
The native computes the collar and body squared integrals separately
before taking square roots.

Using the actual complete negative Cauchy source gain from
[the full real large-root energy calculation](R133-supplement-actual-full-real-large-root-Cauchy-energies.md),
and its already paid primitive conversion, gives:

| $R$ | Negative source to primitive $L^2$ gain | Leading old inverse/mean component, $H^{-4/3}\to L^2$ |
|---:|---:|---:|
| $1/1000$ | $0.151571538329$ | $2.310602\times10^{17}$ |
| $1/500$ | $0.255567574018$ | $1.350626\times10^{18}$ |
| $1/200$ | $0.797099837334$ | $3.007255\times10^{19}$ |
| $1/100$ | $5.236990884613$ | $9.481551\times10^{20}$ |
| $3/200$ | $36.050297857851$ | $1.404249\times10^{22}$ |
| $1/50$ | $220.840346093658$ | $1.432095\times10^{23}$ |

This is a bound for the stated linear source component. It is not the
full positive/negative return error, and no numerical strong inverse
is inferred from it.

## 4. The actual dominant terms and the significance of the result

At the smallest radius the complete moment bounds include
$$
 C_Q<3.101155\times10^8,\qquad
 C_V<2.281704\times10^{12},\qquad
 C_{J,\mathrm{new}}<8.988047.
 \tag{O.5}
$$
The individually integrated negative first-row terms, already including
the outer $J$ source conversion, are bounded by:

| Exact term family from U.27 | Ordinary radial $L^2$ source upper bound |
|---|---:|
| $S_V$ | $1.425289\times10^{15}$ |
| $S_Q$ | $1.846052\times10^{13}$ |
| $R_QJ E_D$ | $1.523238\times10^{18}$ |
| Complete primitive error | $1.706579\times10^8$ |
| Old $r_Q$ mean term | $3.035090\times10^5$ |
| Old $v_\phi$ mean term | $1.237199\times10^4$ |
| Old raw-$D$ mean term | $5.422887\times10^6$ |
| Old $V_0$ mean term | $1.816427\times10^5$ |

The native also saves every corresponding positive term and the
per-row independent even-mean cost. The very large $R_QJ E_D$ bound is
the main bottleneck in this particular estimate. This is an observed
cost of the complete moment/Cauchy bound, not a proof that the true
operator has large norm or that cutoff 97 is impossible.

The constant radial parts of $H^{-1}$ and $H_D$ were already removed
before angular Cauchy differentiation. For example at $R=1/1000$ the
actual bound for the oscillatory part of $H^{-1}$ is below
$0.000104684095$, while that of $H_D$ is below $0.003668083061$.
Thus this run preserves that genuine cancellation, but does not by
itself remove the much larger costs of repeated full-space multiplier
and inverse compositions.

## 5. Exact scope left open

All seven gates passed: original complete objects and their actual
zero-return receipts; the same family and root; the full negative
source windows; the same positive split cut; complete 1328-row moment
and inverse costs; and all six source integrations. No failed prefix
was replaced by a claim of success.

The native explicitly leaves the following false:
local $\mathcal L_0w_1$ paid; complete positive source-to-root conversion;
complete strong-return norm evaluated; cutoff-97 inverse proved; and
actual nonlinear PDE branch proved. Higher radial intrinsic jets were
neither invented nor recomputed. Any improved estimate must preserve
the original full means, old projections, true finite head and all
output frequencies while paying the remaining local amplitude and
propagation terms.
