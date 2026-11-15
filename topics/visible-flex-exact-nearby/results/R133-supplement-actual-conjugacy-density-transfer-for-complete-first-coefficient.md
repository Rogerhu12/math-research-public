# R133 supplement: the actual conjugacy gives a complete H3 density-coefficient transfer

2026-11-15, newton_source.

**Proved analytic consequence of an already completed actual conjugacy.**
The exact real angle supplied by the physical Wiener strip theorem converts a complete first coefficient in the original moving angle to the coefficient required by the [full-circle normalizer](R133-supplement-exact-full-circle-subprincipal-normalizer-and-strong-remainder-budget.md). The conversion costs at most $2^{20}$ in the precise $H^3$ norm below. Its input retains the mean-dependent Jacobian term.

This note evaluates no new KAM gate and assigns no numerical value to the complete first coefficient. The known angle is the conjugacy of the same selected explicit family; it is not a coordinate map of an unconstructed nonlinear solution.

## 1. Exact actual input and the selected object

Use the exact selected pair $(\delta_*,\mathcal H)$ supplied by [the actual physical Wiener conjugacy on strip 1/128](R133-supplement-actual-physical-Wiener-conjugacy-strip.md). Its provenance is:

| Input | Immutable identity |
| --- | --- |
| Published strip theorem | Git blob a79a7ad7c147076b044389e98a15ab2f341d0d0c; 6138 bytes; SHA256 1e8d001a5878da2894b4c9ab88baf00555ca8364b23f49df8c827c23a7da88c3 |
| Actual public execution | Run 43588332723, attempt 1 |
| Original strip-refinement scientific source | SHA256 c1ca128ce18007ec118565beb013a97eaf7c0ccb11962caee474eec092a6c069 |
| Original complete native | 3356 bytes; SHA256 dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854 |
| Its original R31 input | SHA256 d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61 |
| Its same-run K48 input | SHA256 a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60 |

The original native path is notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz. It is cited as existing evidence and is not regenerated here.

Write $x=\mathcal H(\phi)$ and $j(\phi)=\mathcal H'(\phi)$. Both angles have period $\pi/2$ and normalized measure. The variable $\phi$ here is the original moving angle; the word physical in the cited strip theorem refers to this angular scale, rather than the normalized variable $4\phi$. It does not identify $\phi$ with the separate implicit curvature angle.

The existing theorem gives
$$
 \mathcal H\circ P_{\delta_*}=\mathcal H+\Omega_{15},\qquad
 |\delta_*|<9.368259853002\,10^{-11},\qquad
 \|j\|_{\mathcal A_{1/128}}<1.016384090833 .
 \tag{AC.1}
$$
The true lift has degree one, so $\langle j\rangle_\phi=1$ exactly. Since the Wiener norm is the complete sum of absolute Fourier coefficients, (AC.1) implies
$$
 \|j-1\|_{\mathcal A_{1/128}}<\frac1{32},
 \qquad \frac{31}{32}\le j(\phi)\le\frac{33}{32}
 \quad\hbox{on the real circle}.
 \tag{AC.2}
$$
The selected-family root and scalar phase results apply to this same explicit family and its certified parameter range. This note does not identify parameters obtained using different R31 losses by an unproved uniqueness argument.

## 2. Complete coefficient covariance and its mean

Let $c_0\in H^3$ be the real complete first coefficient of the returned operator in the original moving angle, after the prescribed root, waist and density transformations and before the true principal angle conjugacy. Its defining operator convention is a principal density pullback followed by $\operatorname{Id}+M_{c_0}I_\phi$, with every preceding strong remainder and finite row still retained.

For any degree-one diffeomorphism $F$, define
$$
 U_F f=F'(f\circ F),\qquad I_\phi=\partial_\phi^{-1}(1-\Pi_\phi).
 \tag{AC.3}
$$
The exact primitive covariance, including its finite-rank mean maps, is proved in [the first-symbol mean through true rays](R133-supplement-first-symbol-mean-through-true-rays.md), Git blob 5a758bd310a5d6c35e029ef51f1f9fd7b2d2de36, 7324 bytes, SHA256 964537f77f037212afd697cc7cd0ac71d4bd9c21a6e6165d092128f58e62ac3e.

In the inverse conjugation direction its order-minus-one coefficient is
$$
 c(x)=\left(\frac{c_0}{j}\right)\circ\mathcal H^{-1}(x).
 \tag{AC.4}
$$
The additional exact finite-rank maps from primitive covariance remain in the complete operator and its mean rows. Formula (AC.4) identifies its first coefficient; it does not set those maps or their strong-norm costs to zero.

The real change of variables $dx=j\,d\phi$ gives
$$
 \mu:=\langle c_0\rangle_\phi=\langle c\rangle_x.
 \tag{AC.5}
$$
Define the complete mean-corrected input
$$
 g=c_0-\mu j,\qquad
 \langle g\rangle_\phi=0,\qquad
 c-\mu=(g/j)\circ\mathcal H^{-1}.
 \tag{AC.6}
$$
Thus the norm needed in the full-circle theorem is
$C=\|c-\mu\|_{H_x^3}$. Both the complete coefficient and the true Jacobian occur in $g$. For example, a constant $c_0=\mu$ generally becomes the nonconstant function $(\mu/j)\circ\mathcal H^{-1}$.

## 3. The exact H3 norm and four known angle derivatives

On either circle use the Fourier convention
$$
 f(t)=\sum_{k\in\mathbb Z}f_k e^{4ikt},\qquad
 \|f\|_{H^3}^2=\sum_{k\in\mathbb Z}(1+16k^2)^3|f_k|^2 .
 \tag{AC.7}
$$
Parseval and the binomial identity give, with the same normalized measure,
$$
 \|f\|_{H^3}^2
 =\|f\|_2^2+3\|f'\|_2^2+3\|f''\|_2^2+\|f'''\|_2^2 .
 \tag{AC.8}
$$
Every derivative of order at most three has $L^2$ norm at most $\|f\|_{H^3}$.

For the complete Fourier sum, $n^q\le q!\,\sigma^{-q}e^{\sigma n}$ for $n\ge0$. Applying this with $\sigma=1/128$ to $j-1$ in (AC.2) proves
$$
 \|j'\|_\infty\le4,\qquad
 \|j''\|_\infty\le1024,\qquad
 \|j'''\|_\infty\le393216 .
 \tag{AC.9}
$$
These are bounds on $\mathcal H''$, $\mathcal H'''$ and $\mathcal H''''$. Both Fourier signs and the complete analytic tail are included; no finite-frequency interpretation is used.

The denominator and real-measure bounds needed below are
$$
 j^{-m}<2\quad(1\le m\le7),\qquad
 \sqrt{\sup j}<\frac{17}{16}.
 \tag{AC.10}
$$
Indeed $32/31<17/16$, $(17/16)^7<2$, and $33/32<(17/16)^2$. These are elementary rational inequalities. No new numerical gate or inverse-composition solve is required.

## 4. Full chain rule through the third output derivative

Put $F_q=(\partial_x^q(c-\mu))\circ\mathcal H$. Then
$\partial_x=j^{-1}\partial_\phi$ under this pullback. Direct differentiation gives
$$
 F_0=\frac{g}{j},
 \qquad
 F_1=\frac{g'}{j^2}-\frac{g j'}{j^3},
 \tag{AC.11}
$$
$$
 F_2=\frac{g''}{j^3}
      -\frac{3g'j'}{j^4}
      -\frac{g j''}{j^4}
      +\frac{3g(j')^2}{j^5},
 \tag{AC.12}
$$
and
$$
 \begin{aligned}
 F_3={}&\frac{g'''}{j^4}
      -\frac{6g''j'}{j^5}
      -\frac{4g'j''}{j^5}
      +\frac{15g'(j')^2}{j^6}\\
      &-\frac{g j'''}{j^5}
      +\frac{10g j'j''}{j^6}
      -\frac{15g(j')^3}{j^7}.
 \end{aligned}
 \tag{AC.13}
$$
All derivatives on the right are in the original moving variable $\phi$.

Let $G_q=\|\partial_\phi^q g\|_{L^2_\phi}$. Combining (AC.9)--(AC.13), using multiplication by a bounded coefficient only after the full chain rule, gives
$$
 \begin{pmatrix}
 \|F_0\|_2\\
 \|F_1\|_2\\
 \|F_2\|_2\\
 \|F_3\|_2
 \end{pmatrix}
 \le
 \begin{pmatrix}
 2&0&0&0\\
 8&2&0&0\\
 2144&24&2&0\\
 870272&8672&48&2
 \end{pmatrix}
 \begin{pmatrix}G_0\\G_1\\G_2\\G_3\end{pmatrix}.
 \tag{AC.14}
$$
For clarity, the three terms in the bottom-left entry are
$2\cdot393216+20\cdot4\cdot1024+30\cdot4^3=870272$.
The next entry is $8\cdot1024+30\cdot4^2=8672$.
These retain every inverse-Jacobian derivative.

The actual output measure is not omitted:
$$
 \|\partial_x^q(c-\mu)\|_{L^2_x}^2
  =\int |F_q(\phi)|^2j(\phi)\,\frac{d\phi}{\pi/2}
  \le\frac{33}{32}\|F_q\|_{L^2_\phi}^2 .
 \tag{AC.15}
$$

## 5. The complete constant and its input scope

The row sums of (AC.14) are $2,10,2170,878994$.
Use $G_q\le\|g\|_{H_\phi^3}$, (AC.8), the triangle inequality for the four-component Euclidean norm, and $\sqrt3<2$. Then
$$
 \begin{aligned}
 C=\|c-\mu\|_{H_x^3}
 &\le\frac{17}{16}
       \big(2+2\cdot10+2\cdot2170+878994\big)
            \|g\|_{H_\phi^3}\\
 &=\frac{3754263}{4}\|g\|_{H_\phi^3}\\
 &\le 2^{20}\|g\|_{H_\phi^3}.
 \end{aligned}
 \tag{AC.16}
$$
Thus the explicit full-circle normalizer and its strong-remainder budget may use the rigorously transformed input
$$
 \boxed{\displaystyle
 C\le2^{20}\|c_0-\mu\mathcal H'\|_{H_\phi^3},
 \qquad \mu=\langle c_0\rangle_\phi.}
 \tag{AC.17}
$$
The two norms in this formula use the physical Fourier factor $4k$ and the exact normalized measures specified above.

What is already paid is the complete angle and density conversion. A bound for the full function $c_0-\mu\mathcal H'$ still requires the actual strict first coefficient, its root/waist endpoint terms and their stated coordinate conventions. The scalar interval for $\beta_*=-\mu/4$, a single local $\Xi$, and an ordinary volume-residual norm do not supply that function norm. The preceding full strong remainder, finite rows and source ports remain independent inputs to the full-circle theorem. No actual value of $C$, cutoff-97 pass, physical high inverse or nonlinear branch is asserted here.
