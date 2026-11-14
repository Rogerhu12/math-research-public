# R150 appendix — complete rank-one-mean classification in essential cubic dimension three

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved, necessary and sufficient** for the stated stratum.

## 1. The complete criterion

Use the unchanged original six-mode matrix $K$, the physical curve
$v(z)=(1,z,\ldots,z^5)^{\mathsf T}$, and the original Hankel cumulant
tensors $H=(H_{i+j})$, $V=(V_{i+j+k})$. Put
$$
T_3=y^3-6yH+4V,\qquad
W=\operatorname{ess}(T_3).
$$
Suppose
$$
\operatorname{rank}\operatorname{Cat}(y)=1,\qquad \dim W=3.
\tag{1.1}
$$
Here the catalecticant is the original $3$ by $4$ Hankel matrix
$\operatorname{Cat}(y)=(y_{i+j})_{0\le i\le2,\ 0\le j\le3}$.
In particular the mean is a nonzero multiple of a physical value,
including a possible value at infinity.

**Theorem.** Under (1.1), the complete original critical equations
for $\mathcal Q_{F_0^3}$ hold if and only if there is a sign
$\epsilon\in\{+,-\}$ such that
$$
\boxed{
W=W_\epsilon,\qquad
y\in W_\epsilon,\quad
H\in\operatorname{Sym}^2W_\epsilon,\quad
V\in\operatorname{Sym}^3W_\epsilon,\qquad
Q_\epsilon\mid T_3.
}
\tag{1.2}
$$
The divisibility is in the symmetric algebra of that three-space.
Both $W_\epsilon$ and its conic $Q_\epsilon$ are the original,
already fixed ones.

All three original matched first Bell cubics vanish at every
point of this stratum.

There is no assumption on the ranks of $H$ or $V$ in this statement,
and there is no assumption that their common space was already
three-dimensional.

## 2. Exhaustion of the common-support possibilities

Let
$$
E=\operatorname{span}\bigl(
y,\operatorname{Ran}H,\operatorname{ess}(V)\bigr)
$$
be the minimal common space. Since $T_3$ is supported there,
$W\subset E$ and $\dim E\ge3$.

The two proved support reductions
[rank-one five-space bound and inside exclusion](R150-appendix-rank-one-mean-five-dimensional-bound-and-inside-five-space-exclusion.md)
and
[outside five-space exclusion and common four-bound](R150-appendix-rank-one-mean-outside-five-space-exclusion-and-common-four-bound.md)
give $\dim E\le4$ at every complete critical point satisfying (1.1).
They retain the full two-dimensional tangent conormal defect of a
rank-one mean. In particular they do not replace that defect by a
one-dimensional secant companion.

The
[complete outside-section theorem](R150-appendix-rank-one-mean-outside-essential-three-section-is-empty.md)
then excludes $y\notin W$ for either allowed common dimension.
Its physical-support argument also proves that any remaining
four-space is an exact physical length-four jet space $E_g$,
without assuming that $H$ or $V$ has rank four.

Thus a hypothetical common four-space has $y\in W$.
Write $s$ for the mean point and $n$ for its multiplicity in $g$.
The remaining cases are exactly $n=1,2,3,4$:

| Exact common space | Mean position / multiplicity | Proved result |
|---|---|---|
| Dimension five | Inside or outside $W$ | Excluded by the two common-support reductions |
| Dimension four | Outside $W$ | Excluded by the complete outside-section theorem |
| Dimension four | Inside $W$, $n=1$ or $2$ | Excluded by the double-mean-block four-space theorem |
| Dimension four | Inside $W$, $n=3$ or $4$ | Excluded by the triple/quadruple-mean-block four-space theorem |
| Dimension three | Necessarily $E=W$ | Exactly the common-three-space classification |

The two inside four-space exclusions are
[mean multiplicities one and two](R150-appendix-rank-one-inside-double-mean-block-four-space-is-empty.md)
and
[mean multiplicities three and four](R150-appendix-rank-one-inside-triple-and-quadruple-mean-block-four-space-is-empty.md).
The latter enumerates all four local annihilator pairs
$(n,j)=(3,2),(3,1),(4,3),(4,2)$.
Together these cover every physical length-four multiplicity,
all zero lower moment coefficients and the point at infinity.

Consequently $E=W$ at every point of the stratum.

## 3. The only remaining three-spaces

The
[rank-one common-three-space theorem](R150-appendix-rank-one-mean-common-three-dimensional-critical-classification.md)
applies now with exactly its stated hypotheses.
It proves that the complete critical equations on this common
three-space are equivalent to (1.2).

For clarity, the physical planes in that criterion are
$$
W_\pm=\operatorname{span}\{v(z):P_\pm(z)=0\},
$$
where
$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
\tag{3.1}
$$
Each polynomial has three distinct roots, and each plane is
totally isotropic for the original $K$.

Choose the canonical basis matrix $E_\pm$ whose first three rows
are the identity, as in
[the full isotropic-plane moment criterion](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md).
In those coordinates the exact conic matrices are
$$
C_+=
\begin{pmatrix}
279&121&608\\
121&-521&-608\\
608&-608&-1024
\end{pmatrix},
\qquad
C_-=
\begin{pmatrix}
-1769&1369&5024\\
1369&-969&-5024\\
5024&-5024&-1024
\end{pmatrix},
\qquad Q_\pm(u)=u^{\mathsf T}C_\pm u.
\tag{3.2}
$$
Their determinants are both $163840000$, so these conics are
nondegenerate. Thus the condition in (1.2) is concretely
$T_3=Q_\pm\ell$ for a linear form $\ell$.
In the present essential-dimension-three stratum $\ell$ is nonzero.

## 4. Sufficiency uses the complete original gradients

The preceding reductions prove necessity.
For sufficiency, suppose (1.2) holds.
The moment functional generated by $y,H,V$ and zero higher
cumulants factors through $W_\pm$.
This follows directly from its exponential generating function:
each of its three cumulant tensors lies in the indicated
symmetric power of $W_\pm$.

The full isotropic-plane moment criterion, at $h=3$, says that
all original gradients vanish precisely when $Q_\pm\mid T_3$.
It checks every original first, second and third physical
gradient, not merely the highest equation.

Arbitrary higher cumulants do not alter this assertion.
For the original physical curve,
$$
F_0(x+t\,v(z))=F_0(x)+t\,v(z)^{\mathsf T}Kx.
$$
Hence every physical derivative of order greater than three
annihilates $F_0^3$, and, by commutation, its derivatives as well.
The complete original cubic therefore depends only on $y,H,V$.
This is exactly the active-variable reduction in the
[third-moment Schur appendix](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md).

## 5. The matched values and the remaining scope

Let $r_j=(A_j,B_j,0,0,0,1)$, $j=1,2,3$, be the original three
real matched directions fixed by the exact square certificate.
The isotropic-plane appendix proves
$$
Q_\pm(E_\pm^{\mathsf T}r_j)=0.
$$
At the present critical point their complete Bell values are
$$
S_{r_j}=T_3(r_j)
       =(Q_\pm\ell)(E_\pm^{\mathsf T}r_j)=0.
\tag{5.1}
$$
The harmless factor $i^3$ returning to the original first
$iA_jU_1+B_jU_2+U_6$ preserves that vanishing.

The proof exhausts the rank-one-mean, essential-cubic-dimension-three
stratum. The precise common-four-space exclusions were published
as separate conclusions before this aggregation.
No new numerical evidence or independent audit condition is
needed for this logical combination.

This is a classification of complete scalar critical points and
their matched values. A uniform natural power in the full
Jacobian ideal, the higher essential-cubic dimensions and the
ordinary Hilbert invariant-subspace problem remain separate
questions.
