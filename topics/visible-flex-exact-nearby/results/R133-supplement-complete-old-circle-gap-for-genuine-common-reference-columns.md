# R133 supplement: complete old-circle gap for the genuine common-radial columns

2026-11-15, phase_inverse.

**Proved scalar and matrix budget contract; the new numerical gates are not yet executed.**
This keeps the true potential of
[the actual common-radial calculation](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)
and the two genuine columns of
[the common-reference column proof](R133-supplement-genuine-common-radial-reference-columns-and-two-source-ports.md).
It pays the old-circle inverse matrix using the already completed fold.
No target, Fourier transform, original phase, potential, or old norm is recalculated.

The scope is the same fixed intrinsic $\eta_0$, the complete complex explicit
parameter box, and every $|j|\ge97$ with both input signs. The physical
independent mean, the old operators $P,I,J$, and every true reference seam
remain separate parts of the complete problem.

## 1. Exact original input and the smaller product

The original stage
**complete-original-reference-holomorphic-majorants.json.gz**
from public run **43676926141/1** has 4501 bytes and SHA256
**29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144**.
Its complete fold and coefficient payloads are the previously accepted
enclosures on
$$
 R_g=\frac3{8000},\qquad \Sigma_g=\frac3{128}.
 \tag{H.1}
$$
Their original source, helper, manifest, runtime, stage name, and payload
identity are kept intact. A historical read of that exact file is input
restoration, not a new computation of the fold.

Write its quantities as $D_1$, $A_+$, and $B_T$.
By (F.8)--(F.11) of
[the anchored-fold contract](R133-supplement-anchored-auxiliary-fold-and-direct-complex-leading-derivatives.md),
$D_1$ bounds the full old-circle drift derivative on the original larger
product, $A_+$ bounds the full divided phase, and $B_T$ bounds $T_\phi$
at radius $R_g$. The formula for $B_T$ retains the exact quadratic
radial zero and is
$$
 B_T=\frac25a_+D_2 A_-^{-1/3}R_g^2e^{4D_1R_g}
$$
or an already rounded-up value of this complete expression.
It is not a bound on $T$ itself.

Choose
$$
 h=\frac1{20000},\qquad
 \Sigma=\frac1{64},\qquad
 \Sigma'=\frac1{128},\qquad
 d_\phi=\Sigma_g-\Sigma=\frac1{128}.
 \tag{H.2}
$$
All new gates are evaluated on the full complex product
$|\rho|\le h$, $|\Im\phi|\le\Sigma$ and the same parameter box.
The original full-width bounds first give
$$
 e=e^{D_1h},\qquad d=e-1,\qquad
 t=h A_+^{2/3},\qquad
 y=B_T(h/R_g)^2 .
 \tag{H.3}
$$
For the same true fold, throughout the larger angle strip $\Sigma_g$,
$$
 |X_\phi-1|\le d,\qquad |X_\phi|\le e,\qquad
 |T|\le t,\qquad |T_\phi|\le y.
 \tag{H.4}
$$
The last inequality uses the displayed quadratic radial factor before taking
a supremum; it does not rescale an unrelated stored upper bound. Replacing
the smaller exponential by the already paid $e^{4D_1R_g}$ only enlarges it.
The smaller direct/inverse characteristic paths are contained in those
already paid for $R_g$.

Let $R_{\mathrm{im}}$ be the actual common-$T$ image radius from the
successful potential case $R=1/6000$, and put $L=1/2000$.
The new consumer must actually verify
$$
 h\ge h_{\mathrm{piece}},\qquad
 t<L<R_{\mathrm{im}},\qquad
 h<R_g,\qquad 0<\Sigma'<\Sigma<\Sigma_g,
 \tag{H.5}
$$
where
$$
 h_{\mathrm{piece}}=
 \frac{893368603925465506687}{21990232555520000000000000}
$$
is the full true-root interval cover of physical piece 2549.
The first gate identifies the full physical root piece with its original
auxiliary germ. It makes no such identification for other physical cubics.

In (H.5), the disk inclusion is valid for complex old angle and parameters.
The real-axis reference-column bounds themselves apply at a composed $T$
only when that $T$ is real. Existence of the column on the disk does not
supply its complex-angle norm.

## 2. Exact matrix, determinant, and complete inverse

Put $n=4|j|$, $n_0=388$, $\epsilon=\operatorname{sgn}j$, and
$$
 x=X_\phi,\quad y_{\mathrm{fun}}=T_\phi,\quad
 B_+=x^2+T y_{\mathrm{fun}}^2.
$$
Here $y$ without a subscript remains the scalar upper bound in (H.3).
The exact old-circle derivative matrix is
$$
 H_j^V=i\epsilon x\,\mathrm{Id}
   +\begin{pmatrix}0&y_{\mathrm{fun}}(T-V_j/n^2)\\
                       y_{\mathrm{fun}}&0\end{pmatrix}.
 \tag{H.6}
$$
This uses the principal $B_+$ rather than the distinct leading-amplitude
factor $B_-$. Its determinant is
$$
 \det H_j^V=-B_++y_{\mathrm{fun}}^2V_j/n^2.
$$

Read only the final complete bounds
$$
 M_0\ge|V|,\qquad M_1\ge|V_T|,\qquad M_2\ge|V_{TT}|
 \tag{H.7}
$$
from the actual potential execution. Their common image contains the product
by (H.5). Define
$$
 g=1-2d-d^2-t y^2,\qquad
 \theta=\frac{y^2M_0}{n_0^2g},\qquad
 g_V=g-\frac{y^2M_0}{n_0^2}.
 \tag{H.8}
$$
The complete new gates are $g>0$ and $\theta<1$, equivalently $g_V>0$.
They give $|B_+|\ge g$ and $|\det H_j^V|\ge g_V$ on the same full complex
domain, uniformly over the complete high-frequency set.
No mean Fourier output is removed by this pointwise estimate.

In the Euclidean two-component matrix norm put
$$
 H_0=e+\max\{y(t+M_0/n_0^2),y\},\qquad
 H_{\rm free}=e+\max\{yt,y\},\qquad
 b_{\rm free}=H_{\rm free}/g .
$$
Both the full adjugate estimate and the exact ordered
Sherman--Morrison formula are valid. Hence
$$
 b_0=\min\left\{\frac{H_0}{g_V},\
 b_{\rm free}+
   \frac{yM_0\,b_{\rm free}^2}{n_0^2(1-\theta)}\right\}
 \quad\Longrightarrow\quad
 \|(H_j^V)^{-1}\|_2\le b_0 .
 \tag{H.9}
$$
Every denominator is a strict lower bound. Numerical rounding must be
directed after a complete division, or use a lower bound for the denominator;
an upper endpoint of a positive denominator cannot be substituted.

## 3. Two angular derivatives without losing the potential terms

Cauchy on the original angle strip gives
$$
 x_0=e,\quad x_1=d/d_\phi,\quad x_2=2d/d_\phi^2,\qquad
 y_q=q!y/d_\phi^q\quad(q=0,1,2).
 \tag{H.10}
$$
The constant one in $X_\phi$ is subtracted before differentiating.
The complete composed-potential derivative bounds are
$$
 v_0=M_0,\qquad v_1=M_1y_0,\qquad
 v_2=M_2y_0^2+M_1y_1 .
 \tag{H.11}
$$
The $M_2y_0^2$ term cannot be dropped even though the potential is radial in
its own common coordinate.

Set $a_0=t+v_0/n_0^2$, $a_1=y_0+v_1/n_0^2$,
and $a_2=y_1+v_2/n_0^2$. Complete bounds for the upper-right entry of (H.6)
and its first two angular derivatives are
$$
 u_0=y_0a_0,\qquad
 u_1=y_1a_0+y_0a_1,\qquad
 u_2=y_2a_0+2y_1a_1+y_0a_2 .
 \tag{H.12}
$$
Thus $H_q=x_q+\max(u_q,y_q)$ bounds
$\|\partial_\phi^q H_j^V\|_2$ for $q=0,1,2$.
If $B_j=(H_j^V)^{-1}$, its exact ordered derivatives are
$$
 (B_j)_\phi=-B_j(H_j^V)_\phi B_j,
$$
$$
 (B_j)_{\phi\phi}
 =2B_j(H_j^V)_\phi B_j(H_j^V)_\phi B_j
       -B_j(H_j^V)_{\phi\phi}B_j .
$$
Consequently
$$
 b_1=b_0^2H_1,\qquad
 b_2=2b_0^3H_1^2+b_0^2H_2
 \tag{H.13}
$$
are complete two-derivative inverse bounds. No matrices have been commuted
and no derivative of the composed $V_j$ is suppressed.

## 4. Explicit narrower Wiener window

The preceding bounds are holomorphic strip suprema, not same-width
Wiener norms. For fourfold Fourier frequencies $4m$ the exact conversion
constant for $\Delta=\Sigma-\Sigma'>0$ is
$$
 C_\Delta=1+\frac2{e^{4\Delta}-1}.
 \tag{H.14}
$$
For a matrix function, the norm in the Fourier sum is the Euclidean
operator norm of each coefficient. Contour shifting bounds each coefficient
by the strip supremum times $e^{-4|m|\Sigma}$, so (H.14) includes both signs
and the full zero output.

There is a useful complete constant subtraction. Since
$H_j^V=i\epsilon\mathrm{Id}+\mathcal E_j$, put
$$
 e_0=d+\max\{y(t+M_0/n_0^2),y\}.
$$
The exact resolvent identity gives
$$
 B_j-(-i\epsilon\mathrm{Id})
       =i\epsilon B_j\mathcal E_j,\qquad
 \|B_j+i\epsilon\mathrm{Id}\|_{\infty,\Sigma}\le b_0e_0 .
$$
It follows that
$$
 \|B_j\|_{\mathcal A_{\Sigma'}}
       \le\min\{C_\Delta b_0,\ 1+C_\Delta b_0e_0\},
 \qquad
 \|\partial_\phi^qB_j\|_{\mathcal A_{\Sigma'}}
       \le C_\Delta b_q\quad(q=1,2).
 \tag{H.15}
$$
The minimum compares two complete bounds for the same matrix function.
It is not subtraction of two old upper bounds, nor a scalar denominator
Neumann argument in an unpaid Wiener algebra.

## 5. New public consumer and limits

The new scalar consumer reads:

- the complete original majorant stage and its exact old process/publication;
- the already published small execution of run 43685624307/1, retaining all
  original potential gaps, false smaller-domain image flags, and final bounds;
- these formulas and the genuine two-column contract.

It evaluates only the new rational/Arb gates (H.3)--(H.15) and the
two-column Volterra constants. It neither samples a column nor recalculates
the potential or original fold. All original successful science remains
unchanged. New large intermediate data, if any, remain temporary; only
necessary small final bounds, gates, script/parameter/run identities and
hashes are retained.

A successful consumer pays the declared complex old-circle inverse matrix
and its two derivatives, plus the real-axis two-column reference bounds.
It does not prove a full complex-angle column norm, a numerical strong-return
remainder, the actual positive boundary Schur denominator, the original
mean inverse, or the global low/high loop.

In particular the physical primitive identities and their complete
finite remainders in
[the old-circle interface](R133-supplement-common-radial-reference-old-circle-primitive-and-mean-interface.md)
still use the true $P,I,J$ and their declared parity domains. Any reference
matching seam contributes its actual distributional jump at every finite
primitive level. No such term is discarded by the small matrix gap.
