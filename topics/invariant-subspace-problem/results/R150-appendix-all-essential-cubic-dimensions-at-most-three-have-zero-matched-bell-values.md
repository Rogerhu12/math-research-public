# R150 appendix — all essential cubic dimensions at most three have zero matched Bell values

Author: normal_resume_2220 / Astra-ISP-1cf8c51d. Date: 2026-11-14 UTC.

Status: **proved** for the complete original scalar critical equations.

## 1. Statement

Keep the original six-mode matrix $K$, physical Hankel cumulants
$y,H,V$, and the complete ordinary third-moment tensor
$$
T_3=y^3-6yH+4V.
$$
Let $S_{r_1},S_{r_2},S_{r_3}$ be the three original matched
first Bell cubics selected by the exact square certificate.
Their values in the realified coordinates are $T_3(r_j)$.

**Theorem.** At every complete critical point of the original
$\mathcal Q_{F_0^3}$,
$$
\boxed{
\dim\operatorname{ess}(T_3)\le3
\quad\Longrightarrow\quad
S_{r_1}=S_{r_2}=S_{r_3}=0.
}
\tag{1.1}
$$

More precisely:

1. If $\dim\operatorname{ess}(T_3)\le2$, then $T_3=0$.
2. If $\dim\operatorname{ess}(T_3)=3$, then the complete critical
   equations hold if and only if, for one sign $\epsilon$,
   $y,H,V$ are all supported on the original physical isotropic
   plane $W_\epsilon$ and $Q_\epsilon\mid T_3$.

The second assertion is understood under the stipulated essential
dimension three. It is a full necessary and sufficient
classification there. The first assertion is only a necessary
condition for criticality: $T_3=0$ by itself is not asserted to
imply the lower critical equations.

No restriction on the mean rank is left in this theorem.

## 2. Dimensions zero, one and two

The complete highest physical gradient is
$$
T_3(Kv(z))\equiv0,
\tag{2.1}
$$
including its homogenization at infinity.
This uses every third-moment coordinate of the original problem.

Suppose $T_3$ is supported by at most two independent directions
$e_1,e_2$. Since $K$ is invertible, their physical polars
$p_i(z)=e_i^{\mathsf T}Kv(z)$ are linearly independent.
Thus $p_1/p_2$ is a nonconstant rational function.
A nonzero binary homogeneous cubic cannot vanish on its infinite
projective image. The one-direction case is even immediate.
Consequently (2.1) forces $T_3=0$.

This is the $h=3$ instance of the
[highest-moment essential-support theorem](R150-appendix-highest-moment-essential-support-and-cubic-projection-types.md).
It does not assume that other moments share the essential
space of $T_3$.
Every direction, including the three matched ones, has zero
third Bell value in this case.

## 3. Exhaustion of all mean ranks in dimension three

Now assume $\dim\operatorname{ess}(T_3)=3$.
The original mean catalecticant is
$$
\operatorname{Cat}(y)=(y_{i+j})_{0\le i\le2,\ 0\le j\le3}.
$$
Its rank is one of $0,1,2,3$.
The following list therefore exhausts all complex means.

| Mean catalecticant rank | Complete result in essential cubic dimension three |
|---:|---|
| $0$ | Empty |
| $1$ | Exactly common support $W_\pm$ and $Q_\pm\mid T_3$ |
| $2$ | Exactly common support $W_\pm$ and $Q_\pm\mid T_3$ |
| $3$ | Exactly common support $W_\pm$ and $Q_\pm\mid T_3$ |

For rank zero, $y=0$ and $T_3=4V$ is itself physical Hankel.
The original highest equation becomes $J_3V=0$.
The exact determinant in the
[third-moment Schur reduction](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)
is
$$
\det J_3=
23366320238786911411830138211362846399922176000\ne0.
$$
Hence $V=T_3=0$, inconsistent with essential dimension three.

The remaining three rows are the respective complete
classifications:

- [rank-one means](R150-appendix-rank-one-mean-essential-three-complete-critical-classification.md);
- [rank-two means](R150-appendix-rank-two-mean-essential-three-complete-critical-classification.md);
- [nonsecant, rank-three means](R150-appendix-nonsecant-mean-essential-three-complete-critical-classification.md).

Each theorem retains the full original low gradients and all
physical support multiplicities. Their statements include all
ranks of $H,V$, all inside/outside mean positions and infinity.
In particular no extra shared-support hypothesis is being
inserted when the three results are combined.

Thus every nonzero $T_3$ in the present dimension is supported
on precisely one of the two allowed planes, with
$$
T_3=Q_\pm\ell,\qquad \ell\ne0.
\tag{3.1}
$$
Conversely the complete isotropic-plane moment criterion proves
criticality whenever these original cumulants have that support
and satisfy (3.1).

## 4. Why the original three Bell directions vanish

The planes are the physical spans of the roots of
$$
P_+(z)=z^3-5z^2+\frac{32}{5}z-\frac85,\qquad
P_-(z)=z^3+27z^2+\frac{864}{5}z+\frac{864}{5}.
$$
In the canonical bases $E_\pm$ with first three rows the identity,
their physical projections satisfy
$$
E_\pm^{\mathsf T}Kv(z)=P_\pm(z)\psi_\pm(z),
\qquad Q_\pm(\psi_\pm(z))=0.
$$
The complete data and the sufficiency proof are in the
[isotropic-plane moment and matched-value appendix](R150-appendix-isotropic-three-plane-moment-critical-sections-and-matched-bell-values.md).

For an explicit specification of the unchanged matched
directions, let $d_j$ be the three real roots of
$$
3725d^3-43931504d^2+6080833024d+52565262336=0
$$
and put
$$
A_j=-\frac{521d_j^2-46784d_j+271360}{160(5d_j-704)},
\qquad B_j=A_j+d_j,\qquad
r_j=(A_j,B_j,0,0,0,1).
$$
The exact square certificate proves the denominators nonzero.
The isotropic-plane appendix proves, for both signs and every $j$,
$$
Q_\pm(E_\pm^{\mathsf T}r_j)=0.
$$
Therefore (3.1) gives
$$
S_{r_j}=T_3(r_j)
      =(Q_\pm\ell)(E_\pm^{\mathsf T}r_j)=0.
$$
This proves (1.1) in the remaining dimension.
Returning to the original first $iA_jU_1+B_jU_2+U_6$ only
multiplies the cubic by $i^3$, so its matched Bell value is also zero.

## 5. Exact consequence for the continuing problem

Every complete critical point at which at least one of these
three original matched Bell cubics is nonzero must satisfy
$$
\boxed{\dim\operatorname{ess}(T_3)\ge4.}
\tag{5.1}
$$
The only possible essential dimensions for that remaining scalar
problem are four, five and six.

This conclusion does not replace complete criticality by the
highest equation. The higher-dimensional problem still has the
same six original mean-gradient equations and eleven original
second-moment equations, in addition to its highest identity.

On the Schur critical section $Z=0$, the matched values also
equal the reduced polynomials $B_{r_j}(y,H)$.
Thus (1.1) is an exact statement about their values on the
low-essential-dimension part of the full reduced critical locus.
It is not a proof of vanishing on the remaining part, and it
does not supply a natural power $B_{r_j}^N$ in the full Jacobian
ideal. No original operator estimate or ordinary Hilbert
invariant-subspace conclusion is asserted by this aggregation.
