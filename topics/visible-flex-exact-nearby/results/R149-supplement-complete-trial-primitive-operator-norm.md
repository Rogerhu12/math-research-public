# R149 supplement GYN: the whole original trial primitive as an operator

2026-11-27, `visible-exact-astra-fb31ed6-20261127 / trial_restore`.

**Proved.** The complete original IR trial gives a finite real matrix for
the operator $GY:\mathbb R^{96}\to L^2_0$. Its full Schur norm bound can
replace the Hilbert--Schmidt upper in UDR's Linfinity product candidate.
The new full induced-norm targets have not been computed. The old OT
Hilbert--Schmidt and vector Wiener targets remain unchanged.

## GYN.1: exact space, all coefficients, and the physical factor4

Use the original physical period $\pi/2$ and normalized measure
$2\,dx/\pi$. Thus

\[
 c_n(x)=\sqrt2\cos(4nx),\qquad s_n(x)=\sqrt2\sin(4nx),
 \quad n\ge1,
\]

is a real orthonormal basis of $L^2_0$. Let the original exact IR trial
columns be

\[
 Y_j(x)=\sum_{n=1}^{192}
      \left(y_{nj}e^{4inx}+\overline{y_{nj}}e^{-4inx}\right),
 \qquad j=1,\ldots,96.                                  \tag{GYN.1}
\]

These are the entire original192-by96 complex dyadic coefficients, with
their exact conjugate negative modes and zero means. The whole private
trial is the294912-byte object with SHA
`02ee6051166f1f23139b39984dbd309592c415405620f99982a3972d8dd49db1`
from the complete [IR actual](../notes/inverse_density_rows_ci/run-45899761652-1/actual-original-inverse-density-rows.json).
Its entire actual receipt and OT qualification are prerequisites; a
selected coefficient block does not establish this identity.

For $G=|\partial_x|^{-1}$ the complete real matrix $B$ of $GY$ in the
displayed orthonormal basis has384 rows and96 columns:

\[
 B_{2n-1,j}={\sqrt2\,\Re y_{nj}\over4n},\qquad
 B_{2n,j}=-{\sqrt2\,\Im y_{nj}\over4n}.
                                                               \tag{GYN.2}
\]

Indeed $y e^{4inx}+\bar y e^{-4inx}
=2\Re y\cos(4nx)-2\Im y\sin(4nx)$. Parseval therefore gives the exact
operator identity

\[
 \|GY:\mathbb R^{96}\to L^2_0\|=\|B:\mathbb R^{96}\to\mathbb R^{384}\|_2.
                                                               \tag{GYN.3}
\]

The normalization contains neither an extra96-column sum nor an omitted
negative half. Source and target phase rotations do not license changing
the signed carrier; the formula uses every original complex coefficient
in the original coordinate. The two physical mean observations are
separate from these mean-zero trial columns.

## GYN.2: three new whole induced-norm targets

Form every entry of (GYN.2) as a directed real ball. Save and read the
entire384-by96 ball carrier before taking any absolute value. If
$b_{ij}^+$ is the full upper for $|B_{ij}|$, compute

\[
 M_\infty=\max_{1\le i\le384}\sum_{j=1}^{96}b_{ij}^+,
 \qquad
 M_1=\max_{1\le j\le96}\sum_{i=1}^{384}b_{ij}^+.
                                                               \tag{GYN.4}
\]

These two entire scalar results must be saved/read before the third,

\[
 J_S=(M_\infty M_1)^{1/2}\ge\|B\|_2.                  \tag{GYN.5}
\]

This is the ordinary rectangular Schur inequality, applied to every
entry of the complete matrix. It pays all directed radii, including the
normalizing square root and exact physical divisions. No singular-value
estimate from unverified floating arithmetic is used.

Let $J_{HS}$ be OT's **already completed whole** Hilbert--Schmidt upper.
After saving/reading both whole candidates, take

\[
 J_* = \min(J_S,J_{HS})\ge\|GY\|.                     \tag{GYN.6}
\]

No Frobenius or Hilbert--Schmidt reducer is run again. The new targets
are the two different complete induced norms and their Schur candidate.
Either candidate may be smaller; no actual comparison is asserted here.

## GYN.3: direct use in the complete original joint error

The original same-sign compression satisfies
$\|T_f\|_{L^2_0\to L^2_0}\le\|f\|_\infty$: each sign projection is
orthogonal, and its two orthogonal blocks are separately bounded by the
full real multiplication operator. Therefore

\[
 \|T_{\alpha-\widehat\alpha}GY\|
 \le D_\infty J_*,                                    \tag{GYN.7}
\]

where $D_\infty$ is only the proof abbreviation in UDR.9. The actual
new product is accumulated directly from the same whole2048 residuals
and entire original tail. The complete L2 product
$\sqrt2D_2B_G$ is still saved independently. Both whole products precede
their minimum. UDR's two full inverse-error products, original finite
alpha norm, and VQ/Theta row formulas are unchanged.

In particular GYN does not omit the coefficient error on the infinite
IR inverse error, infer exact orthogonality of approximate rows, or
replace the full target operator by its low block. It only supplies a
potentially smaller legitimate norm of one **entire existing finite
operator**. All aliases, source errors, true phases, selected-member
qualification, physical means, and subsequent low-square/full-Schur
obligations remain as in
[UDR](R149-supplement-unit-disk-phase-errors-in-original-Theta-rows.md)
and [TQL](R149-supplement-exact-low-model-isometry-and-Theta-square-error.md).

The accompanying [pure formulas](../scripts/fourfold_codazzi_trial_primitive_operator_norm.py)
contain no IO, runtime import or old scientific target. A first actual
owner must preserve the whole original trial SHA, all36864 signed real
matrix entries, the complete two induced norms, and both whole final
operator candidates before applying (GYN.7).
