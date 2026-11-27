# R149 supplement DWT: the same target w from the complete unit-disk input

2026-11-27, `visible-exact-astra-fb31ed6-20261127 / trial_restore`.

**Proved.** A first signed trial for the original target coefficient $w$
can be obtained directly from the new complete unit-disk input. Its
cohomological denominator, source reflection and zero mean are the
original ones. The full already completed ASR tail envelope also bounds
this coefficient: no old tail or scalar target has to be executed again.
This is an input theorem for the original $B=Id+T_wI$ problem; no actual
$w$ carrier or inverse gate is asserted here.

## 1. The original coefficient and all phases

Use the normalized physical circle of period $\pi/2$, with Fourier
frequency $4n$, as in
[AS](R149-supplement-original-source-alpha-signed-carrier-and-complete-errors.md)
and [UDR](R149-supplement-unit-disk-phase-errors-in-original-Theta-rows.md).
The original selected source coefficient is $v_i$, and

\[
 \alpha=v_i-w,\qquad
 a=2H(0),\qquad b=a+\Omega,\qquad
 q_n=e^{-4in\Omega},\quad t_n=e^{-4inb}.                 \tag{DWT.1}
\]

The three coefficients $v_i,\alpha,w$ are real and mean zero in their
original normalizations. The raw source192 used to obtain the nonzero
Fourier coefficients of $v_i$ retains its complete original constant;
one must not remove that raw constant before the nonunitary transport.

The original full cohomological equation gives, for every $n\ne0$,

\[
 \alpha_n={q_nv_{i,n}+t_n\overline{v_{i,n}}\over q_n-1},
 \qquad
 \boxed{w_n=-{v_{i,n}+t_n\overline{v_{i,n}}\over q_n-1}.} \tag{DWT.2}
\]

The second formula is the exact difference $v_{i,n}-\alpha_n$.
It changes neither the normalizer nor the selected member. The original
both-sign small-divisor estimate remains

\[
 |q_n-1|^{-1}\le68|n|.                                  \tag{DWT.3}
\]

The factor68 is the original physical-frequency factor4 times the
AS bound17, rather than a new rotation or denominator estimate.

The target reflection is also exact. Set $r_n=e^{-4ina}=t_n/q_n$.
Since $\overline q_n=q_n^{-1}$ and $\overline t_n=t_n^{-1}$,
(DWT.2) implies

\[
 r_n\overline{w_n}
 ={t_n\overline{v_{i,n}}+v_{i,n}\over q_n-1}
 =-w_n.                                                \tag{DWT.4}
\]

Thus $R_aw=-w$ in the original target reflection and
$w_{-n}=\overline{w_n}$. The coefficient mean $w_0=0$ is its original
normalization. Neither this equality nor (DWT.4) eliminates either
independent physical mean slot or the separate first-coefficient mean
parameter.

## 2. A first finite trial from all8192 nodes and all2048 modes

Let $K=2048$. For every $1\le n\le K$ use the complete saved UDR disk
$\mathcal Q_n$ from all8192 original grid points. The disk enclosure
includes every input radius, phase recurrence residual, summation radius
and decimal conversion in UDR.2--5. Reuse the whole completed original
ASR source/model/alias inputs, in their original units:

\[
 |v_{i,n}-Q_n|\le F_n:=E_n+M_n+A_n,\qquad Q_n\in\mathcal Q_n,
                                                               \tag{DWT.5}
\]
\[
 E_n=\min_{0\le r\le3}{E_r\over(4n)^r},\quad
 M_n=4nE_HTe^{-4nm\sigma},\quad
 A_n={2T e^{4nG_1\sigma}e^{-4\sigma N}\over1-e^{-4\sigma N}},
 \quad N=8192,\quad\sigma=1/128.                        \tag{DWT.6}
\]

All four source derivative columns, the whole true-map difference,
the complete analytic raw192 bound, the positive Jacobian lower and the
entire alias sum are retained. In particular the maximum raw support is
the corrected full192; the failed smaller-support AS entry is not used.

With the full saved $\Omega$ and $b$ balls, compute the directed ball

\[
 \mathcal W_n=-{\mathcal Q_n+t_n\overline{\mathcal Q_n}\over q_n-1},
 \qquad 0<d_n^-\le|q_n-1|.                              \tag{DWT.7}
\]

A rectangular enclosure of the complete disk is allowed at this single
cohomological operation; it is not iterated2048 times. Any exact dyadic
number may be chosen as the new trial coefficient $\widehat w_n$.
In particular one may choose a directed-ball midpoint, save its exact
rational representation and read it back before using it. Then

\[
 \boxed{\Delta_n^w\ge
    |\mathcal W_n-\widehat w_n|
           +{2F_n\over d_n^-}}
 \quad\Longrightarrow\quad
 |w_n-\widehat w_n|\le\Delta_n^w.                        \tag{DWT.8}
\]

Here the absolute value is the upper of the full ball, not its center.
Both numerator terms have modulus-one exact phase, so their perturbation
cost is at most $2F_n$. All phase and divisor uncertainty within
$\mathcal W_n$, all disk radii, and all trial rounding are included
separately from this source/model/alias payment.

Set $\widehat w_0=0$, $\widehat w_{-n}=\overline{\widehat w_n}$ and
$\widehat w_n=0$ for $|n|>K$. This is a new independent finite carrier,
whose whole bytes and hash must be saved and read before consumption.
It need not satisfy exact parity about an unknown true phase: (DWT.8)
already pays its full error to the exactly reflected true $w$.
The original ASR alpha carrier, every old coefficient and its whole SHA
remain unchanged.

## 3. The same already completed whole tail envelope

This reuse is justified by the formulas, not by an inferred comparison
between the actual norms of $w$ and $\alpha$. For either coefficient the
cohomological numerator has modulus at most $2|v_{i,n}|$. Hence the
original same universal majorant is

\[
 |w_n|\le136|n|\,|v_{i,n}|,\qquad
 |\alpha_n|\le136|n|\,|v_{i,n}|.                         \tag{DWT.9}
\]

Apply the original AS.13--14 decomposition of $v_i$ into the complete
analytic raw transport and its full source $H^3$ error. Write $T$ for
the same complete analytic bound, $E_3$ for the same complete source
derivative-column bound, and $m>0$ for the same true Jacobian lower.
For $q=e^{-4m\sigma}$ the entire analytic tail of either coefficient
has the original majorant

\[
 B_{\rm an}
  =272T\,{q^{K+1}(K+1-Kq)\over(1-q)^2}.                 \tag{DWT.10}
\]

For the full nonanalytic source error, the multiplier from its third
physical derivative has size

\[
 {136|n|\over(4|n|)^3}={17\over8|n|^2}.
\]

The original both-sign Cauchy--Schwarz sum and the full $L^2$ multiplier
bound therefore give

\[
 B_\infty=B_{\rm an}+{17E_3\over8}\sqrt{{2\over3K^3}},
 \qquad
 B_2=B_{\rm an}+{17E_3\over8(K+1)^2}.                  \tag{DWT.11}
\]

For the first inequality use
$\sum_{n>K}n^{-4}\le\int_K^\infty x^{-4}dx=1/(3K^3)$;
for the second use the supremum at $K+1$. The analytic part may be
bounded in $L^2$ by its complete Wiener tail. These are exactly the
ASR tail formulas with the same complete inputs and normalization.
Consequently the saved whole records `complete_Linf_tail` and
`complete_L2_tail` are already valid directed upper bounds for the
tail of true $w$. Reuse those entire formal records directly.
There is no new execution of an old tail reducer, and no need to run
an intermediate $v_i$ tail target merely to recover this same bound.

## 4. New whole errors and the exact downstream scope

Every one of the2048 new records in (DWT.8) must be saved and read in
natural order. Only after the whole prefix and its exact finite carrier
are complete, combine the complete tail records to obtain

\[
 \boxed{e_{w,\infty}
       =2\sum_{n=1}^{K}\Delta_n^w+B_\infty,}\qquad
 \boxed{e_{w,2}
       =\left(2\sum_{n=1}^{K}(\Delta_n^w)^2+B_2^2\right)^{1/2}.}
                                                               \tag{DWT.12}
\]

The finite and tail Fourier supports are orthogonal in the second
formula. These are the first two DWT whole error targets for this new
direct $w$ trial, rather than replacements for the completed ASR scalar
conclusions. A partial prefix or a copied progress number is insufficient.

The original target operator remains

\[
 B=Id+T_wI,\qquad
 T_w=\Pi_+M_w\Pi_++\Pi_-M_w\Pi_-,\qquad I=\partial_x^{-1}.
                                                               \tag{DWT.13}
\]

Its future inverse-row consumer must explicitly admit the new DWT
carrier, its full provenance and the complete errors (DWT.12). It may
not call this an unexecuted BW trial, or treat the SC raw pairings as
full $B^{-1}$ columns. The already proved complete BR residual method
still retains all2240 output modes and its entire infinite coefficient
tail. All source/target phases, both physical means, the positive PDE
inverse, the phase/parameter border and the physical full Schur
obligations remain separate.

The accompanying [pure formulas](../scripts/fourfold_codazzi_direct_target_w_unit_disk.py)
implement (DWT.7--8,12). They contain no scientific runtime or file I/O.
A first actual owner must use public Actions, the exact original whole
carrier SHA gates, every8192-node disk input, every2048-mode signed
coefficient, and the original full tail records. This proof alone does
not assert that such an actual run has occurred.
