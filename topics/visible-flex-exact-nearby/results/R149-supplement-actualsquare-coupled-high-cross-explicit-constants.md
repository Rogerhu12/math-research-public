# R149 ASQ5. Explicit complete cross-block costs at the original cutoff

**Proved for the selected coupled waist operator when its stated positive
input is admitted.** At the original $J=2^{4608}$ the coupling costs below
use the actual global $\Theta$ bound and distinguish a high-to-high
compression from a high-to-all waist output. The latter retains a finite
reference correction absent in the former. The estimates multiply the
whole signed column error of CFC; no CFC outcome is asserted.

Let $A_+$ denote the upper endpoint of the actual
`common_high_WPL_physical_primitive_upper` in
[CG.4](R149-supplement-positive-feedback-in-the-complete-graph-high-block.md).
Put $P=P_J$ and $K=K_E+K_{\rm ref}+K_+$ in the notation of
[WDH.22–28](R133-supplement-explicit-dyadic-high-block-gate-from-complete-waist-error.md)
and CG.9. Their original same-source and selected-exterior qualifications
remain necessary. Define
$$
 h=2^{-44}+2^{-1337}A_+,\qquad k=h+2^{-1194}.
$$
Then $\|PKP\|<h$ and $\|KP\|<k$ for the complete coupled operator.
Indeed the WDH bound on $E\widetilde P\overline G P$ before the left
projection is already $2^{1492}\Lambda_J^{-1/3}<2^{-44}$.
CG.14 before the left projection contributes at most
$2^{199}A_+\Lambda_J^{-1/3}\le 2^{-1337}A_+$.
Finally $K_{\rm ref}$ lands in the first 96 reflected modes, so
$PK_{\rm ref}=0$. For its *full output* use WGB.13:
$$
 (2+|\nu_i|/4)\Lambda_{96}^{4/3}<2^{17}.
$$
This follows from $|\nu_i|<2^6$, $\Lambda_{96}<2^9$. The WDH
transported projection costs $2^{316}$ and the high model inverse
costs $2^9\Lambda_J^{-1/3}$. Thus $\|K_{\rm ref}P\|<2^{-1194}$.
This term cannot be deleted from a low output just because its high
output vanishes. For $h<1$ the high inverse norm is bounded by
$(1-h)^{-1}$; its denominator need not pay the finite reference cost.

The complete BFP target 16, `complete_original_Theta_trial_Frobenius_upper`,
is below $10.123545$ including its radius. It bounds the norm of the
same normalized finite trial operator in DCP.22. The actual global
difference is below $6.957962$. Hence
$$
 \|\Theta\|<17.082 .
$$
These statements use the [full BFP result](R147-supplement-actual-full-target-nu-forward-and-Theta-column.md),
[DCP.22](R149-supplement-particular-density-Theta-and-complete-opposite-leakage.md)
and [WMA.1](R149-supplement-actual-complete-weighted-model-Theta-receiver.md).
The WMA error alone is not a norm of $\Theta$.

Let $D,e_\Theta,\delta_X$ be the actual signed matrix, its whole
error and the complete target-column error in
[ASQ4.4](R149-supplement-actualsquare-CFC-physical-cross-and-tail-budget.md).
Then the sharper replacement for the high-feedback term there is
$$
 \|S_{cc}-D\|\le e_\Theta+17.082\,k\,(1-h)^{-1}\delta_X .
$$
The following sufficient implications are strict and apply to the same
one complete $96\times96$ block.

| Whole positive WPL receiver upper | Additive cost beyond $e_\Theta$ |
|---|---|
| $A_+\le 2^{1335}$ | $<5.695\,\delta_X$ if $\delta_X>0$ |
| $A_+\le 2^{1330}$ | $<0.135\,\delta_X$ if $\delta_X>0$ |
| $A_+\le 2^{1293}$ | $<2^{-38}\delta_X$ if $\delta_X>0$ |

At $\delta_X=0$ the entire additional term vanishes.
The [exact rational consumer](../scripts/fourfold_codazzi_actualsquare_high_cross_budget.py)
checks the new scalar combinations. No old norm, large finite operator,
selected positive Poisson map or CFC target was evaluated. In these
same units the low-waist high feedback costs at most $k\delta_X/(1-h)$.
The other columns, source and rows still require the full signed
$H^{-1}PKQ$, $H^{-1}Pg$, $H^{-1}Pf$ and the actual low/high physical
phase and height evaluations. None of the three thresholds is assumed
for the pending actual coupled receiver.
