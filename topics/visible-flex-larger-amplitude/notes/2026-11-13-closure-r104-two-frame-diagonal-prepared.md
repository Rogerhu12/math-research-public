# Prepared finite-mode two-frame diagonal refinement for R104

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-13.

This is a complete comparison proof and a prepared independent Python entry.
The entry has not been AST-checked or executed. It makes no numerical
improvement, contraction, or new-solution claim. The previously preserved
single-frame source and all actual R104 primaries remain unchanged.

## 1. Exact object and why a second frame is relevant

Use the actual real background, source coordinate, exact original leaf
envelopes $V_I$, constant angular width $18/125$, and physical variables
$(P,\overline K)$ of R104. The only new objects are bounds on the
same-source/same-target blocks for modes94 and96 and source materials
$c_{\rm bg}V_I^p$, $p=2,1,0$, where
$c_{\rm bg}=s+|\ell|$, $s=r_x/r$, and $\ell=w_x/w$.

R68 minimized the high-frequency phase separately on each original leaf.
For a fixed finite mode, repeated changes of frame can instead dominate
the sufficient bound. It is legitimate to compare that original choice
with one frame held constant on the entire source segment. This does not
change the equation or presume that a different frame gives a better
answer.

The actual R104 primary required here has SHA256
62156ade93e31729c7500e79dbc01c3f4267d1a89a2b7730af7fe1c6440df45a.
All its offdiagonal source blocks and both independent physical initial
columns are retained. No high initial height or momentum is set to zero.

## 2. One-leaf comparison, including the source

Fix an exact positive dyadic $b$. On a source leaf let
$u=(P,\overline K/b)^T$. Its homogeneous matrix is
$$
A_m=\begin{pmatrix}
-s-\ell&-msb\\
-m\ell/b&-2\ell
\end{pmatrix}.
$$
The Hermitian part gives, also for complex Fourier coefficients,
$$
\frac{d}{dx}|u|_2
\le \alpha_m |u|_2+|N_m|/b,\qquad
\alpha_m=\max(-s-\ell,-2\ell)
 +\frac m2|sb+\ell/b|.
\tag{1}
$$
At a change from $b_-$ to $b_+$ the exact diagonal coordinate change has
Euclidean norm $\max(1,b_-/b_+)$.

On a leaf of exact length $\Delta$, choose a constant upper
$\alpha_*$ for (1), and $d_*\ge c_{\rm bg}V_I^p/b$.
The scalar comparison with incoming $q_0\ge0$ is
$$
q(t)=e^{\alpha_*t}q_0+d_*t\psi(\alpha_*t),\qquad
\psi(z)=\int_0^1e^{zt}\,dt.
\tag{2}
$$
It satisfies $q'=\alpha_*q+d_*$ and $q\ge0$. For $\alpha_*\ne0$,
the derivative has constant sign, and for $\alpha_*=0$ it is
nonnegative. Therefore
$$
\sup_{0\le t\le\Delta}q(t)=\max(q_0,q(\Delta)).
\tag{3}
$$
This does not assert that the actual vector solution is monotone.
The positive-integral definition of $\psi$ applies when its argument is
negative as well. The implementation bounds the quotient
$(e^z-1)/z$ with Arb; if this quotient is too broad, the independent bound
$\psi(z)\le e^{\max(0,z)}$ remains valid.

For each material and each frame choice, propagate (2), pay every frame
change, and bound physical components separately by $|P|\le q$ and
$|\overline K|\le bq$. Take their separate whole-segment radial suprema,
then multiply their sum by $1+m$.
This is the PHYSICAL strong output norm of R104, with no output $V_I$
division. Any later change to a local-$V$ output norm must separately
use the positive lower envelope on each actual target leaf.

The diagonal forced problem has zero initial state at its source-segment
entrance. Hence the constant-segment comparison has no interior frame
jump and requires no incoming conversion for this forced contribution.
It does not replace the complete nonzero initial trace of the actual
outer problem.

## 3. A rigorously selected constant candidate

Let $S>0$ and $L\ge0$ be complete upper sums on the source segment:
$$
S\ge\int s\,dx,\qquad L\ge\int|\ell|\,dx.
$$
The triangle bound gives
$$
\int \frac m2|sb+\ell/b|\,dx
\le\frac m2(bS+L/b).
$$
For $b\ge1$, a homogeneous physical-input-to-physical-output surrogate
has a frame-conversion factor at most $b$. Ignoring the diagonal term,
which is independent of $b$, its log bound is
$$
f_m(b)=\log b+\frac m2(bS+L/b).
\tag{4}
$$
Write $t=\log b\ge0$. Then
$f_m(e^t)=t+(m/2)(Se^t+Le^{-t})$ is convex, with strictly
positive second derivative unless $S=L=0$. Its interior stationary
condition is
$$
mSb^2+2b-mL=0.
$$
The constrained minimizer is
$$
b_{\rm cand}
=\max\left(1,\frac{mL}{1+\sqrt{1+m^2SL}}\right).
\tag{5}
$$
The formula is stable when $L$ is small; it also has the correct
$S=0$ limit, although the actual background has $S>0$.

The program evaluates the positive surrogate sums outward, chooses a
single dyadic upper point for (5), and clamps it to1. It records that
exact point, rather than only a rounded display. Then it discards the
triangle surrogate as a source bound and recomputes (1)-(3) on every
actual original leaf, retaining the signed combination $sb+\ell/b$.

Equation(5) optimizes only the stated homogeneous triangle surrogate.
It does not optimize the forced $1/b$ density, the two separate
component suprema, or the actual operator. Correctness of the new
kernel follows from the independent per-leaf verification, regardless
of whether this candidate improves the original bound.

## 4. Safe combination and Fourier quantifiers

For each source material, let $A_P,A_K$ be the original R104 component
bounds, and let $B_P,B_K$ and $C_P,C_K$ be the two new independent
scalar-comparison bounds. Then
$$
\min(A_P,B_P,C_P)+\min(A_K,B_K,C_K)
$$
is a valid strong component-sum bound for the same actual forced
linear map. The frame choices need not be the same for the two minima,
because each bound independently holds for the same component at every
point. There is no inference that one propagated state simultaneously
attains those minima.

For fixed source-mode masses
$$
a_m=\sup_{x\in I_j}
 \frac{e^{\tau |m|}|N_m(x)|}{c_{\rm bg}(x)V_I(x)^p},
$$
the componentwise estimates are first applied to each $m$ and then
summed. If a shared source norm is $\sum_m a_m$, the operator constant
is the maximum over $m$ of the two-component output row, not a sum
of per-mode maxima. A known pure-centre source has its own fixed
$a_m$ and can instead be multiplied row by row.
No step replaces $\sum_m\sup_x$ by $\sup_x\sum_m$.

The source envelopes are piecewise constant on the original leaves by
definition, and the source is measured with those same envelopes.
The method applies neither to an unproved new $V$ nor to a backward
or two-point operator. Complete mean and inverse bounds enter only in
a later nonlinear consumer; this linear operation cannot remove their
obligations.

## 5. Prepared entry and actual dependencies

New entry:
computations/closure_middle_two_frame_diagonal_materials_v2.py.

It consumes the actual R104 primary and its formal wait4 record,
the pinned original source summaries/groups, and the complete R68
frame packet and streams. The original R68 producer source was
read and its SHA256 rechecked as
ef41df6103a8c8b9cabc4ac8f2be133a244d5e0361e7d861ff7266426498e63b.
Its saved fields index, x_left, x_right and chosen_frame agree with
the prepared consumer's identity checks. The original V producer was
also read; V remains its exact upward80-bit sqrt(c0/4) definition.

The actual complete R68 main-packet SHA still has to be computed
from the restored file and passed explicitly. It is not guessed from
a displayed number. Both scans cover all10793 original leaves; all18
source segments and all three material powers are retained.

CLI:
--computations /absolute/frozen/topic/computations
--blocks /absolute/exact-owned/2026-11-13-closure-middle-causal-mixed-m94m96-r1.json
--blocks-resource /absolute/exact-owned/2026-11-13-closure-middle-causal-mixed-m94m96-r1-resource.json
--frame notes/2026-11-12-root-outer-optimal-frame-r1.json
--frame-sha256 <actual complete packet SHA256>
--precision 256
--rss-kib 98304
--out-prefix /fresh/tmp/owned-prefix

Run the ordinary wait4 wrapper and preserve each completed segment,
the full primary, resource and exact command. This work has no new
source quadrature, radius integral, Taylor flow, MJS, or Node worker.
The single small Arb slot remains with the root's already-started
geometry until its formal terminal state and release.
