# R149 supplement DT: the original same-sign source Toeplitz and exact row action

2026-11-27, `visible-exact-astra-fb31ed6-20261127`.

**Proved clarification and complete signed finite action.** The original
source normalizer uses the two same-sign multiplication blocks. This
note corrects one descriptive sentence in DB and gives the exact finite
row assembly needed after IR. All already proved DB/SDI bounds continue
to apply to the original operator. No existing numerical target is
repeated and no currently pinned IR input is changed.

## DT1. Keep exactly the original source operator

The original definition is
[WBN.14](R133-supplement-exact-two-sided-reflected-waist-first-coefficient-normalization.md),
also repeated in WBP.3--4:

\[
 \mathcal T_\alpha
 =\Pi_+M_\alpha\Pi_++\Pi_-M_\alpha\Pi_-,\qquad
 A=Id-\mathcal T_\alpha I,\qquad I=\partial_x^{-1}P.
                                                               \tag{DT.1}
\]

Here $\alpha=v_i-w$ is the same real, mean-zero coefficient with
$R_b\alpha=-\alpha$ for the actual source reflection
$b=a+\Omega$. The metric parameter, the cohomological divisor and the
nonzero phase are not reset. The coefficient $w$ is the original
cohomological solution; (DT.1) does not authorize a repeated solve.

The sentence following DB.19 saying
`mathcal T_alpha=P alpha P` is a notational error. It must be read as
(DT.1). In general these two compressions differ: $PM_\alpha P$ also
contains the opposite-sign blocks
$\Pi_+M_\alpha\Pi_-+\Pi_-M_\alpha\Pi_+$.
Those extra blocks must never be inserted into the original signed
coordinate rows. This is not a new choice of source normalizer.

For the actual (DT.1), the orthogonal sign decompositions prove

\[
 \mathcal T_\alpha^*=\mathcal T_\alpha,\qquad
 \|\mathcal T_\alpha\|_{L^2_0\to L^2_0}\le\|\alpha\|_\infty,
 \quad
 \|\mathcal T_\alpha-\mathcal T_{\widehat\alpha}\|
       \le\|\alpha-\widehat\alpha\|_\infty.                 \tag{DT.2}
\]

There is no additional factor for two signs. These are exactly the
coefficient properties used in DB.19--25. In particular

\[
 A^*=Id+I\mathcal T_\alpha,\qquad
 N A^*G e=e-Z\mathcal T_\alpha G e,\qquad
 G=N^{-1},\quad N=|\partial_x|,
                                                               \tag{DT.3}
\]

because $NI=-Z$. Thus no angular derivative of $\alpha$ is needed for
the full $H^1$ row error. Every DB/SDI estimate is unchanged when the
correct definition is inserted. Their distributional inverse theorem
for the separate sign-compressed density $C$ is independent of
$\alpha$ altogether. The running IR calculation constructs only
$E_{96}^*D_+^{-1}C^{-1}$ and does not assemble $A$.

## DT2. Exact finite same-sign convolution

Let $\widehat z_j$, $1\le j\le96$, be the whole fixed finite real
trials for $(C^\dagger)^{-1}b_j$ from IR, with positive coefficients
$c_{nj}$, $1\le n\le M$. The original IR choice has $M=192$.
Let $\widehat\alpha$ be one declared real mean-zero trigonometric
polynomial with coefficients $a_\ell$, $|\ell|\le L$, where
$a_0=0$ and $a_{-\ell}=\overline {a_\ell}$. A future actual consumer
must separately provide its complete error
$e_\alpha\ge\|\alpha-\widehat\alpha\|_\infty$.

The trial row for $V_Q=E_{96}^*D_+^{-1}C^{-1}A$ is

\[
 \widehat r_j
 =G\widehat z_j+I\mathcal T_{\widehat\alpha}G\widehat z_j.
                                                               \tag{DT.4}
\]

All physical frequencies are $4n$. Therefore its positive coefficient
is exactly

\[
 (\widehat r_j)_k
 =\mathbf1_{k\le M}\frac{c_{kj}}{4k}
   +\frac1{4ik}\sum_{n=1}^{M}a_{k-n}\frac{c_{nj}}{4n},
 \quad 1\le k\le M+L,                                     \tag{DT.5}
\]

with $a_\ell=0$ outside $[-L,L]$. The output mean is zero and the
negative coefficients are the conjugates of (DT.5). The sum contains
**only positive input indices**. Using negative $n$ in this positive
output formula would compute the erroneous full compression instead.
All $k>M+L$ coefficients of this finite trial are exactly zero; this
does not claim that a true row or its error is finite dimensional.

The [pure finite assembly](../scripts/fourfold_codazzi_original_source_Theta_row_action.py)
implements (DT.5), deriving negative coefficients by conjugation rather
than treating them as independent unknowns. It takes all96 complete
columns. Coefficients may be exact or certified enclosures of a single
declared finite trial; a float fit or a sampled maximum alone supplies
neither that definition nor $e_\alpha$.

The exact complete trial operator norm
$Z_G=\|G\widehat Z:\ell^2_{96}\to L^2_0\|$ may, for example, be
bounded by its full Hilbert--Schmidt expression

\[
 Z_G^2\le2\sum_{j=1}^{96}\sum_{n=1}^{M}
                      \frac{|c_{nj}|^2}{(4n)^2}.             \tag{DT.6}
\]

This is a new finite norm if it has not already been evaluated; it is
not a reason to rerun the now completed IR residual targets. A tighter
whole Gram norm is also permitted, but an entrywise mixture of
different candidate matrices is not an operator certificate.

## DT3. Complete joint errors before and after the original model inverse

Use the **same** complete joint residual bounds $\epsilon_H,\epsilon_0$
of IR, not a prefix or a sum of rounded column centres. Put
$K_A=1+A_0/4$, $A_0\ge\|\alpha\|_\infty$. The exact energy inverse
and $\|G:\mathscr H\to L^2\|=1/2$ give

\[
 \|V_Q-\widehat V_Q\|_{L^2\to\ell^2}
 \le \frac{K_A}{2}\epsilon_H+\frac{e_\alpha}{4}Z_G.
                                                               \tag{DT.7}
\]

The second term uses the physical primitive norm $1/4$ once.
For the full one-loss model map
$\overline G:Y_a^0\to H^{-1}$, use the already paid actual
[SDI](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md)
and the same $K_G\ge\|\overline G\|$. For
$\widehat\Theta=\widehat V_Q\overline G$,

\[
 \boxed{\quad
 \|\Theta-\widehat\Theta\|
 \le K_G\left\{\frac{1071}{1000}K_A
          (\epsilon_0+\tfrac{10}{9}\epsilon_H)
                 +\frac{21}{20}e_\alpha Z_G\right\}.
 \quad}                                                       \tag{DT.8}
\]

The trial Theta rows are the genuine bounded adjoint actions
$\overline G^*\widehat r_j$. In an actual signed computation their
original reflected source/target phases and the original low/high
Fourier multipliers must be used. A norm for $V_Q$ alone cannot replace
this step; no projection is commuted through $\overline G$ or $A$.
There is no extra $\sqrt{96}$ after either joint estimate.

The two physical density means, the target normalizer's scalar rank,
all independent height and boundary inputs, and the metric/phase
finite border are unchanged. The zero auxiliary mean in (DT.1) is
not an elimination of any of those equations. The actual signed
$\alpha$ carrier, complete Theta action, full physical matrix and
nonlinear family still require their declared inputs and gates.
