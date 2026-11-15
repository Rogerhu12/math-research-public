# R133 supplement: actual raw-response mean fee and corrected high-collar domain

2026-11-15. Actual public execution of the separate mean-source correction
[MC](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md).
The new run restores the complete source estimate for exactly five retained
collar cases. All 91 historical records remain unchanged; the other ten
historically passing cases are not reauthorized by this restricted run.

## 1. Actual execution and immutable identity

Public Actions run
[43717700427/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43717700427)
completed successfully. The actual scientific child returned zero, all
twelve identity and coverage gates passed, and all five newly evaluated
retained cases passed their original numerical thresholds. The scientific
process took less than three seconds.

The full small receipt is
[execution.json](../notes/raw_response_mean_collar_fee_ci/run-43717700427-1/execution.json).
Its Git blob is
0f796b9c77076f6907e426afcddd5c8e933a6706, its size is 36310 bytes,
and its SHA256 is
c5424be21b98cf5e195ea7246ccba46cf746d1f16d9c118042fda1fad433e408.
The companion
[actual-result.md](../notes/raw_response_mean_collar_fee_ci/run-43717700427-1/actual-result.md)
has blob 1f01ceb54048b2380b7dfb03152d78983228b742, 6696 bytes,
and SHA256
5d77fee7c29808b9f31c7916d55b16cd0722c59fb669904c7b235b26de8e3df8.

The embedded scientific conclusion, recovered with its exact original
canonical JSON serialization, has 23297 bytes and SHA256
aa24a677083ae68044362e6895e30b2e8a1daa4ab9b46e2d2ce299ea38d2a055.
That digest agrees with the execution's original output receipt.
The mathematical source and manifest are respectively

- [the new scalar consumer](../scripts/fourfold_codazzi_raw_response_mean_collar_fee.py),
  SHA256 7547ece2825854a18e59c27294b12e8dbdcb13671c8fb0d8fba6af218d86f7f2;
- [its complete pinned-input manifest](../notes/2026-11-15-R133-raw-response-mean-collar-fee-CI-inputs.json),
  SHA256 5157dfea0e7d44c7a6659ffd14505ac2a09248ea12ed7333a53a08b11103f7e9.

The actual checkout was
ec6c38bc8cc9bfedfc50c7a1d4eddac5c5dfe561.
The successful source, inputs and output are fixed. This report does not
request or perform another run.

## 2. The source identity that is now paid

Keep the three response objects in MC separate: the original finite
response $q_{\rm raw}$, its scalar-mean-completed version $q^\sharp$,
and the continuous response direction $Z=q_{\rm raw}+e_{\rm cont}$.
The original mean completion is generally radially varying. It is not
the small piecewise constant continuity repair.

Let $s_0$ be the complete response source of the continuous direction at
the repaired centre, and let $r_0$ be the independent signed raw
second-mean residual in the original closed rows. MC.4--MC.13 prove
that the previously saved nonnegative budget, including its centre-repair
and continuity fees, is a bound for
$$
 b_0=s_0+r_0e_2,\qquad s_0=b_0-r_0e_2.                 \tag{MA.1}
$$
The old source budget is not subtracted as a vector. Its mean-completion
additions and the enlarged $H_0$ in the centre-repair operator fee are
nonnegative upper bounds for the corresponding raw nonmean quantities.
This is the monotonicity argument in MC.5--MC.8. No identification of
$q^\sharp$ with $Z$ is made.

On the true collar, with the intrinsic bump absent, the exact selected
reference residual therefore has the form
$$
 f_\delta
 =f_0-\delta b_0+\delta r_0e_2
           -\delta^2T_2-\delta^3T_3,\qquad
 |\delta|\le d=10^{-10}.                               \tag{MA.2}
$$
The new term has positive sign. Its complete absolute norm is paid.
Both scalar means and the original repair of radial jumps remain.

For
$$
 P(r)=\operatorname{diag}(K^{-1/4},K^{1/4}),
$$
the square weight on this new second mean is exactly $\sqrt K$.
The angular measure is the normalized circle, so a constant coefficient
has norm equal to its absolute value: no $\alpha$, $1/2$, or $\sqrt2$
factor occurs.

For each requested interval $I$, the new computation uses
$$
 M_I^2
 =\sum_i |I\cap I_i|\,
           \sup_{I_i}\sqrt K\,\sup_{I_i}|r_0|^2 ,
 \qquad \|P r_0e_2\|_{L^2(I\times\mathbb T)}\le M_I.    \tag{MA.3}
$$
Every intersection and radial length is exact. The signed mean enclosure
and positive $K$ enclosure are original complete closed-row data.
Positive angular derivatives of this source are identically zero.

## 3. Both actual raw-mean windows

The entire restored input contains the same forty natural parts and
7721 complete rows on $[0,25/8]$. Its canonical row payload SHA256 is
06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6,
identical to the earlier successful independent receipt.

Only these two new restrictions were evaluated. Every displayed decimal
is rounded outward from the complete directed ball in the execution.

| Window | Exact radial length | Original closed rows | $\|r_0\|_{L^2}$ upper | $\|P r_0e_2\|_{L^2}$ upper |
|---|---:|---:|---:|---:|
| $[17/20,19/20]$ | $1/10$ | 140 | $7.5259836670\cdot10^{-7}$ | $5.1638705526\cdot10^{-7}$ |
| $I_*=[589819/655360,589829/655360]$ | $1/65536$ | 2 | $7.0162792351\cdot10^{-10}$ | $4.9636769817\cdot10^{-10}$ |

The signed raw mean ranges are contained in
$[-8.6700000424,8.6700000424]\cdot10^{-6}$ on the full available collar
and $[-2.5400000104,2.5400000104]\cdot10^{-7}$ on $I_*$.
The scaled suprema are below $5.9917049742\cdot10^{-6}$ and
$1.7969485850\cdot10^{-7}$, respectively.
These suprema are recorded separately; no $L^1$ estimate has been
substituted for an $L^2$ estimate.

For the retained cases, $c=9/10$ and $\ell=2^{-18}$, so
$I_*=[c-2\ell,c+2\ell]$. The missing source fee is now
$$
 dM_{I_*}<4.9636769817\cdot10^{-20}.                    \tag{MA.4}
$$
The complete response source bound, before multiplication by $d$, is
$$
 \|Ps_0\|_{L^2(I_*)}<0.00220961864332.                 \tag{MA.5}
$$
Its predecessor $0.002209618146950\ldots$ retains its correct meaning:
a bound for $Pb_0$, not for the complete $Ps_0$.

The complete selected-reference source budgets satisfy
$$
\begin{aligned}
 F_{\rm value}&<5.8836159444\cdot10^{-11},\\
 F_{\rm factorial}&<5.8836164717\cdot10^{-11},\\
 F_{\rm angle}&<2.2649653192\cdot10^{-8}.
\end{aligned}                                         \tag{MA.6}
$$
The first two have received (MA.4). The third is exactly the original
directed record, because the new source has angular degree zero.
No old source array has been edited.

## 4. Every newly checked numerical case

These are the five complete retained rows of the old 91-case result.
All use $I_*$, $\ell=2^{-18}$, the original coefficient constants and
the original thresholds. The start, linear and positive-speed gates
are unchanged. The nonlinear gate and factorial readout have been
reevaluated with the new complete source.

| Raw pair $C^0$ radius | Corrected nonlinear gate upper | Corrected factorial prefactor upper | All five gates |
|---|---:|---:|---|
| $2^{-20}$ | $0.064961859821$ | $0.000180323441$ | passed |
| $2^{-24}$ | $0.004059992336$ | $1.127018311\cdot10^{-5}$ | passed |
| $2^{-28}$ | $0.000253751161$ | $7.043922153\cdot10^{-7}$ | passed |
| $2^{-32}$ | $1.586157785\cdot10^{-5}$ | $4.403043173\cdot10^{-8}$ | passed |
| $2^{-36}$ | $9.934808229\cdot10^{-7}$ | $2.757820834\cdot10^{-9}$ | passed |

The nonlinear threshold is $1/8$. The factorial prefactor threshold is
the original $2^{1024}$. The five gates are positive actual speed,
low start, complete linear absorption, complete nonlinear absorption,
and the factorial readout. The largest corrected $A_N$ is below
$0.001680461997$.

The old result still has 91 original verdicts and 15 original scalar
passes. This computation does not change those records. Its new
mathematical authorization covers exactly the five rows above; it
does not infer corrected source values or gate verdicts for the other
ten old passing rows.

## 5. Restored conditional high-trace theorem

Fix one of these five radii. Let $Q$ be one real continuous two-sided
$H^1$ solution of the full moving PDE on $I_*$, with zero ordinary
residual, in that raw pair $C^0$ ball about the continuous selected
reference $Q_\delta$. Use the same fixed intrinsic parameter,
$|\delta|\le10^{-10}$, the original reflection class, the same moving
angle, and the complete source convention (MA.1)--(MA.3).

Then the finite-difference theorem
[H.34--H.40](R133-supplement-finite-factorial-collar-bounds-and-complete-high-inner-trace-gate.md),
with the sharper constants in
[A](R133-supplement-sharper-low-constants-in-finite-collar-trace.md),
applies with all source components paid. At the actual cut,
$$
 \|Q(c)-Q_\delta(c)\|_{H^{8193}}<2^{377903}.             \tag{MA.7}
$$
The already paid finite-band selected-reference difference gives
$$
 \|Q(c)-Q_0(c)\|_{H^{8193}}
 <2^{377904}<2^{393000}.                               \tag{MA.8}
$$
The finite-difference proof obtains this regularity from the two-sided
$H^1$ solution. High angular differentiability is not assumed at the
bootstrap starting point. This is a conditional local regularity and
trace statement. It does not assert existence of the two-sided solution,
actual core closure, or a finite/high Schur gate.

For approximate states with nonzero ordinary residual, H still requires
the full actual residual and its finite factorial source array. This
evaluation does not replace an iterate's residual by the true-solution
condition $f=0$.

## 6. Low entry remains open

The MC.17 ordinary $H^1$ diagnostic also includes the new mean fee.
Its selected-reference cut upper bounds, in increasing radius precision,
are
$$
 25.442759248,\quad 1.590167703,\quad 0.099386293,\quad
 0.006212477,\quad 0.000389113.                         \tag{MA.9}
$$
These are upper bounds, not lower bounds on the actual correction.
They remain too large to prove the
[known-base sharp low curvature entry](R133-supplement-known-finite-cut-Wiener-angle-and-sharp-low-curvature-entry.md).
The old false low-entry verdict is preserved for every row.

The next input must control the actual unknown correction more sharply,
including its finite 193-dimensional cut component, unknown high
component, and the complete two-sided body and source data. The high
trace (MA.7) can be used only for the same actual state satisfying this
theorem's hypotheses.

## 7. No old numerical work repeated

The receipt records zero target, Fourier, cubic, mean-flow,
residual-integral and Green recomputations. All forty natural parts
were restored byte-for-byte into temporary Actions storage and remained
unchanged. The scalar mean flow was not solved again.

The only new radial calculation was (MA.3) on two explicit windows,
followed by five complete retained-case evaluations. The temporary
row audit is identified by its hash in the small receipt and is not
persisted as recomputable data. Full means, original jump repairs,
real radial measures, source species and all scope restrictions remain.
