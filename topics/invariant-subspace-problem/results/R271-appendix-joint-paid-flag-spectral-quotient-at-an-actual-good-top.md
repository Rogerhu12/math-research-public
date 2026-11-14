# R271 appendix — a joint spectral quotient for several original paid flags at one actual good top

Date: 2026-11-14 UTC. Author: Astra-ISP-1cf8c51d / boundary_resume_2220; AI-assisted, GPT-6 Astra Pro.

Status: **proved.** Several overlapping original cheap source flags can be used together if their overlap is measured in the actual two-fee metric. A positive average of their genuine metric projections supplies that measurement. Deleting its spectrum above a paid threshold preserves the same actual left vector, the whole lower source flow, every primitive feedback budget, and the exact top two-fee bound. The residual has a quantitative simultaneous small-projection condition for every selected flag.

We apply this to three already proved original flags: the large-triplet range, the high-angle source space, and the first three original source heads. No sum of flags is declared cheap without paying its spectral threshold. The new joint remainder is not asserted to satisfy the exact individual Schur condition from either separate quotient. The ordinary full right cost and pure high inverse remain unpaid in the application below.

Dependencies: [exact good-top two-fee quotient and coherent flow](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md), [large-triplet and low-angle original quotients](R271-appendix-large-triplet-and-low-angle-good-top-quotients.md), and [three original source heads](R271-appendix-three-original-source-heads-and-uniform-complete-to-bare-bound.md).

## 1. All flags and costs live in the same original source space

Fix one legal original window, with head $A_m$, tail $D_m$, and source space $\mathscr R_b$. Write
$$
L=J_{\rm left}^{-1},\qquad B=J_{\rm bare}^{-1},\qquad G=J_{\rm full},
\qquad M_2=B+LGL.
$$
For every source $r$ the five actual costs are
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
$$
$$
\lambda_{\rm flat}(r)^2=\langle GLr,Lr\rangle,\qquad
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle M_2r,r\rangle.
\tag{1.1}
$$
The first and third costs are norms of the genuine bounded linear maps
$E_b^\dagger$ and $F_b^\dagger$ at this fixed window.
All fixed-window source metrics are bounded and strictly positive.
No parameter-uniform norm equivalence is assumed.

Let $\mathscr D\subset\mathscr R_b$ be a closed source constraint satisfied by the actual source. For the source-flow application we require
$$
\mathscr D\subset
\mathscr N_b=\ker\iota_0^*(L+B).
\tag{1.2}
$$
The full common-cost negative graph used below is one such choice.
Give $\mathscr D$ its actual Hilbert inner product
$$
(r,s)_M=\langle M_2r,s\rangle,\qquad \|r\|_M=\Xi(r).
$$

Let $\mathscr E_1,\ldots,\mathscr E_N$ be closed original source flags with proved bounds
$$
\lambda(z)\le C_j\alpha(z)
\quad(z\in\mathscr E_j),\qquad C_j\ge1.
\tag{1.3}
$$
Intersect each with the same constraint:
$$
Z_j=\mathscr E_j\cap\mathscr D,\qquad
P_j=P_{Z_j}^{M_2}:\mathscr D\to\mathscr D.
\tag{1.4}
$$
These are the genuine orthogonal projections for $(\cdot,\cdot)_M$.
They are not the physical coordinate projections onto those flags.

The original same-source Cauchy--Schwarz inequality is
$$
\mu(z)^2
=\langle G^{-1/2}z,G^{1/2}Lz\rangle
\le\lambda(z)\lambda_{\rm flat}(z).
$$
On $Z_j$, (1.3) therefore gives both estimates
$$
\mu(z)^2\le\frac{C_j}{2}\Xi(z)^2,\qquad
\lambda(z)\le C_j\Xi(z).
\tag{1.5}
$$
The first uses $2\alpha\lambda_{\rm flat}\le\alpha^2+\lambda_{\rm flat}^2$.
It does not exchange either Gram with $L$.

## 2. The weighted projection spectrum pays all overlap

Choose positive weights $w_j$ with $\sum_jw_j=1$, and define on $\mathscr D$
$$
T=\sum_{j=1}^Nw_jP_j,\qquad
\overline C=\sum_jw_jC_j,\qquad
\overline{C^2}=\sum_jw_jC_j^2.
\tag{2.1}
$$
Then $T$ is self-adjoint in the actual $M_2$ metric and
$$
0\preceq_M T\preceq_M I,\qquad
(Tr,r)_M=\sum_jw_j\|P_jr\|_M^2.
\tag{2.2}
$$
All spectra and inverse powers of $T$ in this manuscript use this Hilbert structure.

For $0<\delta\le1$, set
$$
\mathscr Y_\delta=\operatorname{Ran}1_{[\delta,1]}(T).
\tag{2.3}
$$
It is a closed original source subspace inside $\mathscr D$.
On it, the inverse of $T$ is bounded by $\delta^{-1}$.

**Joint paid-space theorem.** For every $p\in\mathscr Y_\delta$,
$$
\boxed{
\mu(p)^2\le\frac{\overline C}{2}
\|T^{-1/2}p\|_M^2
\le\frac{\overline C}{2\delta}\Xi(p)^2,
}
\tag{2.4}
$$
$$
\boxed{
\lambda(p)^2\le\overline{C^2}
\|T^{-1/2}p\|_M^2
\le\frac{\overline{C^2}}{\delta}\Xi(p)^2.
}
\tag{2.5}
$$
There is no assumption on the pairwise angles, commuting projections, or closedness of the unweighted sum of the $Z_j$.

To prove this, put $z=T^{-1}p$. In the same original source space,
$$
p=Tz=\sum_jw_jP_jz.
\tag{2.6}
$$
Linearity of $E_b^\dagger$, the triangle inequality, (1.5), and weighted Cauchy--Schwarz give
$$
\begin{aligned}
\mu(p)
&\le\sum_jw_j\mu(P_jz)\\
&\le\sum_jw_j\sqrt{C_j/2}\,\|P_jz\|_M\\
&\le\sqrt{\overline C/2}
\left(\sum_jw_j\|P_jz\|_M^2\right)^{1/2}\\
&=\sqrt{\overline C/2}\,(Tz,z)_M^{1/2}
=\sqrt{\overline C/2}\,\|T^{-1/2}p\|_M.
\end{aligned}
$$
This proves (2.4). Replacing the first bound in (1.5) by the second, and using linearity of $F_b^\dagger$, proves (2.5).

Thus the inverse spectral factor pays exactly the possible cancellation in (2.6). In particular, the conclusion is a bound in $\Xi$, not an unproved bound $\lambda\lesssim\alpha$ on the whole sum.

## 3. One joint projection and the exact residual conditions

For an actual $r\in\mathscr D$, perform the single metric projection
$$
p=1_{[\delta,1]}(T)r,\qquad
\widehat r=1_{[0,\delta)}(T)r=r-p.
\tag{3.1}
$$
Both sources stay in $\mathscr D$, and
$$
\boxed{\Xi(p)^2+\Xi(\widehat r)^2=\Xi(r)^2.}
\tag{3.2}
$$
Consequently
$$
\mu(p)^2\le\frac{\overline C}{2\delta}\Xi(r)^2,\qquad
\lambda(p)^2\le\frac{\overline{C^2}}{\delta}\Xi(r)^2.
\tag{3.3}
$$
The exact joint condition is
$$
1_{[\delta,1]}(T)\widehat r=0.
\tag{3.4}
$$
From (2.2) and the residual spectrum one gets, with no discarded cross term,
$$
\boxed{
\sum_jw_j\|P_j\widehat r\|_M^2
=(T\widehat r,\widehat r)_M
\le\delta\,\Xi(\widehat r)^2.
}
\tag{3.5}
$$
For each positive weight this implies
$$
\boxed{
\|P_j\widehat r\|_M
\le\sqrt{\delta/w_j}\,\Xi(\widehat r).
}
\tag{3.6}
$$
Equivalently, every original test $z\in Z_j$ satisfies
$$
|\langle M_2\widehat r,z\rangle|
\le\sqrt{\delta/w_j}\,\Xi(\widehat r)\Xi(z).
\tag{3.7}
$$

These are simultaneous relative bounds in the true two-fee metric.
They do not say that any physical head coordinate, triplet coordinate, or bare-normalized angle coordinate vanishes.
Nor do they say $P_j\widehat r=0$ for fixed positive $\delta$.
The kernel of $T$ is exactly the simultaneous metric orthogonal complement of all $Z_j$, but projection onto that whole kernel has not been paid by (2.4) without a positive spectral threshold.

## 4. Coherent transport of the same actual good-top source

Retain the original setup of the exact good-top theorem.
For a hypothetical nonzero fixed defect vector $w\in W$, put $W_0=\|w\|$ and
$$
d=2^m,\qquad Q=\lfloor e^{d^3/4}\rfloor.
$$
The original top left minimum $u_Q$ is within the paid lift error of the corresponding truncation of $w$.
Write $\varepsilon=\varepsilon_m$ for that error plus the actual tail above $4d$; thus $\varepsilon/W_0\to0$ without any rate assumption.

The disjoint future bands provide $K\asymp Q/d$ candidate cuts in the upper half of the interval, with $K\ge Q/(4d)$ for all sufficiently large $m$.
Select the good cut $b$ before any projection. Its original source satisfies
$$
r_b\in\mathscr D,\qquad
\Xi_b(r_b)^2\le\frac{2\varepsilon^2}{K}.
\tag{4.1}
$$
Apply (3.1) only at this selected cut.
Set
$$
v=E_b^\dagger p,\qquad
\widehat u_b=E_b^\dagger\widehat r_b=u_b-v.
$$
Then
$$
\boxed{
\|v\|^2=\mu_b(p)^2
\le\frac{\overline C}{\delta K}\varepsilon^2,\qquad
\lambda_b(p)^2\le
\frac{2\overline{C^2}}{\delta K}\varepsilon^2.
}
\tag{4.2}
$$
These costs concern the same original correction $p$.

For every lower cut $a\le\ell\le b$, reconstruct
$$
\widehat u_\ell=P_{\le\ell}\widehat u_b,\qquad
\widehat r_\ell=A_m(\widehat u_b)_\ell,
\qquad
s_\ell=A_m v_\ell.
\tag{4.3}
$$
The exact left-truncation theorem makes these the true minimum left vectors for their sources.
All lower sources belong to one original source flow; no window chooses an independent correction.

The source-flow energy identity applied to $v$ pays every primitive feedback and tail inverse:
$$
\boxed{
\sum_{\ell=a}^{b-1}
\left(\|\mathcal D_{\ell+1}^{\dagger}s_\ell\|^2
+\|\delta g_{\ell+1}\|^2\right)
=\|v\|^2-\|P_{\le a}v\|^2
\le\frac{\overline C}{\delta K}\varepsilon^2.
}
\tag{4.4}
$$
The original nonfirst-head primitive variables, and the true head weights relating them to source increments, are exactly those in the source-flow theorem.

For the retained lower disjoint windows with endpoint at most $b-d$, the true future bands remain disjoint inside the new prefix.
Their total two-fee budget is at most
$2(\varepsilon+\|v\|)^2$.
The terminal cut has no reconstructed future beyond $b$, so it is paid separately by the exact Pythagoras identity (3.2).
Thus
$$
\boxed{
\sum_{\ell\in I_b}\Xi_\ell(\widehat r_\ell)^2
\le
2\left(1+\sqrt{\frac{\overline C}{\delta K}}\right)^2
\varepsilon^2+\frac{2\varepsilon^2}{K}.
}
\tag{4.5}
$$
Every retained left minimum differs from the same fixed $w$ by at most
$$
\boxed{
\varepsilon+\sqrt{\frac{\overline C}{\delta K}}\,\varepsilon.
}
\tag{4.6}
$$
Only the top satisfies the new joint spectral condition (3.4); no such condition is imposed for free on lower cuts.

For preservation of the actual left vector and all these budgets, it is enough that
$$
\frac{\overline C\,\varepsilon^2}{\delta K}\longrightarrow0.
\tag{4.7}
$$
For the ordinary complete top right-cost difference to tend to zero, the additional sufficient condition is
$$
\frac{\overline{C^2}\,\varepsilon^2}{\delta K}\longrightarrow0.
\tag{4.8}
$$
Indeed $|\lambda_b(r_b)-\lambda_b(\widehat r_b)|\le\lambda_b(p)$.
Condition (4.8) is not inferred from (4.7).

## 5. Three concrete original flags can now be used simultaneously

We give a fully specified application that uses only already proved original ranges.

### 5.1 The common original constraint

In bare-normalized coordinates define
$$
u=B^{1/2}r,\quad H=B^{-1/2}LB^{-1/2},\quad
C=B^{1/2}GB^{1/2},\quad P_1=1_{\{1\}}(C).
$$
Here $0<C\le I$, and the actual same-future source obeys the full common-cost negative graph.
Choose
$$
\mathscr D=B^{-1/2}\ker[P_1(I+H)].
\tag{5.1}
$$
It is closed at fixed parameters and contained in $\mathscr N_b$.
The latter inclusion is the original common-first-head block of the same full negative relation.
The actual source selected in (4.1) satisfies (5.1).

### 5.2 Large-triplet range

Use the original adjacent-pair construction with
$$
R=\lfloor\sqrt Q/64\rfloor,\qquad
s=R-1,\qquad T_{\rm height}=2R-1,
$$
$$
N_{\rm pairs}=b-R+1,\qquad
J=m+2N_{\rm pairs}.
\tag{5.2}
$$
The paid joint range $\mathscr E_{\rm tr}$ contains all choices of at most $R$ complete three-dimensional pair blocks and all the specified far-tail primitive births, with the original full head and joint source flags.
For $r$ selected pair blocks, the allowed births are $0,\ldots,R-1$ when $r=0$, and $0,\ldots,R-r$ when $r\ge1$.
They give active height between $\max(0,2r-1)$ and $2R-1$, so every model high input is absent.
All cross-birth terms use the same already proved short section.

The large-triplet theorem pays
$$
\theta\le27/512<1/8,\qquad
\lambda|_{\mathscr E_{\rm tr}}
\le C_{\rm tr}\alpha,\qquad
C_{\rm tr}\le32(1+R/m)
\le32+\frac{\sqrt Q}{2m}.
\tag{5.3}
$$
In particular $C_{\rm tr}/K\to0$.
No new pairing partition or unproved whole-mode range is inserted.

### 5.3 Original high-angle source space

Let
$$
\mathscr E_{\rm ang}
=B^{-1/2}\operatorname{Ran}1_{[K^{-2},1]}(C).
\tag{5.4}
$$
It is closed and satisfies
$$
\lambda(r)^2=\langle C^{-1}u,u\rangle
\le K^2\|u\|^2=K^2\alpha(r)^2,
$$
so we may take $C_{\rm ang}=K$.

### 5.4 First three original source heads

Take
$$
\mathscr E_{\rm hd}
=\mathscr R_b\cap(\ker A_m^3\otimes\mathcal H_b).
\tag{5.5}
$$
The complete three-head theorem proves
$$
\lambda|_{\mathscr E_{\rm hd}}\le13\kappa\,\alpha,
\tag{5.6}
$$
where $\kappa$ is the norm of the fixed original two-dimensional inverse from the first three heads.
It is independent of $m,b$; its actual potentially large value is retained.
Thus $C_{\rm hd}=13\kappa$ and $C_{\rm hd}/K\to0$.

Intersect all three spaces with the same $\mathscr D$ in (5.1).
Let their actual metric projections be $P_{\rm tr},P_{\rm ang},P_{\rm hd}$ and set
$$
\boxed{
T=\frac13(P_{\rm tr}+P_{\rm ang}+P_{\rm hd}).
}
\tag{5.7}
$$
For sufficiently large $m$, all three constants are at most $K$, hence
$$
\overline C\le K,\qquad \overline{C^2}\le K^2.
\tag{5.8}
$$
More precisely $\overline C/K\to1/3$ and $\overline{C^2}/K^2\to1/3$.
No pairwise angle estimate is needed; the spectrum of this very $T$ pays the overlap.

## 6. A tail-adaptive threshold gives all three relative conditions

For the same hypothetical fixed nonzero $w$, choose
$$
\delta_m=\min\{1/4,\varepsilon_m/W_0\}.
\tag{6.1}
$$
The actual lift error in $\varepsilon_m$ is positive; if instead $\varepsilon_m=0$ at a cut, (4.1) already forces its source and left vector to vanish and yields the corresponding contradiction directly.
Thus the projection is defined for the continuing nonzero case.

For all sufficiently large $m$, $\delta_m=\varepsilon_m/W_0$ and (4.2), (5.8) give
$$
\boxed{\mu_b(p)^2\le\varepsilon_m W_0\longrightarrow0.}
\tag{6.2}
$$
The same actual defect vector survives:
$$
\|\widehat u_\ell-w\|
\le\varepsilon_m+\sqrt{\varepsilon_mW_0}\longrightarrow0.
\tag{6.3}
$$
All feedback and window budgets in (4.4)–(4.5) tend to zero, while the sharp terminal estimate stays
$$
\boxed{\Xi_b(\widehat r_b)^2\le2\varepsilon_m^2/K.}
\tag{6.4}
$$

At this same terminal source, (3.5) now supplies the simultaneous result
$$
\boxed{
\|P_{\rm tr}\widehat r_b\|_M^2+
\|P_{\rm ang}\widehat r_b\|_M^2+
\|P_{\rm hd}\widehat r_b\|_M^2
\le3\delta_m\,\Xi_b(\widehat r_b)^2.
}
\tag{6.5}
$$
Each relative metric projection therefore tends to zero.
This single source retains the full common-cost negative graph, the original physical head/tail flags, and its coherent lower flow.

On the other hand our available complete top bound is only
$$
\lambda_b(p)^2\le2K\varepsilon_mW_0.
\tag{6.6}
$$
There is no assumed rate for $\varepsilon_m$, so (6.6) need not tend to zero.
The joint construction is consequently an actual-left-source reduction with exact original two-fee control. It is not a claimed ordinary full-right-cost transport in this parameter range.

## 7. The remaining actual comparison is unchanged in strength

For a hypothetical nonzero $w$, (6.3) gives
$\mu_b(\widehat r_b)\to W_0$.
Together with (6.4),
$$
\frac{\mu_b(\widehat r_b)^2}
{K\,\Xi_b(\widehat r_b)^2}\longrightarrow\infty,
\tag{7.1}
$$
unless a zero terminal source has already contradicted (6.3).
Therefore an $O(K)$ bound for the left/two-fee quotient on these actual joint remainders would exclude $w$.
The new information is that the same remainders also satisfy all three relative tests (6.5), with a paid vanishing threshold.

No such $O(K)$ bound is proved here.
In particular, one may not replace (6.5) by exact zero coordinates, claim a spectral gap for $T$, apply the exact individual low-angle KKT formula without its new residual term, or infer a pure $S_H^\dagger$ bound from the completed energy.
The fixed-three-head flag can be replaced in this theorem by any further original flag once its actual constant is proved; its weight and contribution to both moments in (2.1) must then be retained.

This is a complete simultaneous original-source quotient, including its overlap cost, original flow transport, and all remaining limitations. The ordinary ISP and $N=M$ remain OPEN.


## 8. Keeping an exact growing-head condition before the joint quotient

The subsequently proved [dyadic original-head theorem](R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md) supplies a larger actual head flag with a strict complete-cost margin. It can be removed first, and its exact metric condition can be preserved throughout a following joint quotient.

Use the same actual good cut $b$, $M_2$, and any one fixed choice of the closed original constraint $\mathscr D$ from §1, with $r_b\in\mathscr D$. In particular one may keep the full common-cost negative graph (5.1). Put
$$
H_m=2^{\lfloor3m/4-2\rfloor},\qquad
Z_H=\mathscr E_{H_m,b}\cap\mathscr D,\qquad P_H=P_{Z_H}^{M_2}.
$$
The dyadic theorem remains valid on this smaller intersection. For
$$
p_H=P_Hr_b,\qquad r_b^{(0)}=r_b-p_H
$$
it gives
$$
\mu(p_H)\le a_m\varepsilon,\qquad
\lambda(p_H)\le b_m\varepsilon,
$$
$$
a_m=8\sqrt d\,e^{-11d^3/128},\qquad
b_m=32\sqrt d\,e^{-3d^3/64}.
\tag{8.1}
$$
Now define the actual residual constraint
$$
\mathscr D_1=\mathscr D\cap Z_H^{\perp_M}.
\tag{8.2}
$$
It is closed, is contained in the original source-flow range, and contains $r_b^{(0)}$.

Intersect the large-triplet and high-angle spaces from §§5.2–5.3 with this very $\mathscr D_1$:
$$
Z_{\rm tr}'=\mathscr E_{\rm tr}\cap\mathscr D_1,\qquad
Z_{\rm ang}'=\mathscr E_{\rm ang}\cap\mathscr D_1.
$$
Their bounds $C_{\rm tr}\le K$ and $C_{\rm ang}=K$ are inherited by restriction. Let $P_{\rm tr}',P_{\rm ang}'$ be their true metric projections inside $\mathscr D_1$, and put
$$
T_1=\frac12(P_{\rm tr}'+P_{\rm ang}').
$$
Choose the same $\delta=\min(1/4,\varepsilon/W_0)$ as before and set
$$
p_1=1_{[\delta,1]}(T_1)r_b^{(0)},\qquad
r_b^{\rm fin}=r_b^{(0)}-p_1.
\tag{8.3}
$$
This is an application of the joint theorem on $\mathscr D_1$, not an alternating use of projections on incompatible spaces.

Because $p_H$ is metric orthogonal to all of $\mathscr D_1$, and (8.3) is an orthogonal split within it, there is exact three-term Pythagoras:
$$
\boxed{
\Xi(p_H)^2+\Xi(p_1)^2+\Xi(r_b^{\rm fin})^2
=\Xi(r_b)^2\le2\varepsilon^2/K.
}
\tag{8.4}
$$
For all sufficiently large $m$,
$$
\mu(p_1)^2\le\varepsilon W_0,\qquad
\lambda(p_1)^2\le2K\varepsilon W_0.
\tag{8.5}
$$
The total correction $p_H+p_1$ need not be orthogonal in the left or full-right metrics. Using their triangle inequalities, and no false cross-term cancellation, gives
$$
\boxed{
\mu(p_H+p_1)\le a_m\varepsilon+\sqrt{\varepsilon W_0},
}
\tag{8.6}
$$
$$
\lambda(p_H+p_1)
\le b_m\varepsilon+\sqrt{2K\varepsilon W_0}.
\tag{8.7}
$$

Rebuild all lower sources from the one new top left minimum
$E_b^\dagger r_b^{\rm fin}$.
The source-flow and disjoint-future argument of §4 applies to this total correction. In particular all primitive and MP feedback differences have total squared norm at most the square of (8.6), all retained left vectors tend to the same $w$, and
$$
\sum_{\ell\in I_b}\Xi_\ell(r_\ell^{\rm fin})^2
\le
2\bigl[(1+a_m)\varepsilon+\sqrt{\varepsilon W_0}\bigr]^2
+2\varepsilon^2/K\longrightarrow0.
\tag{8.8}
$$
The terminal sharp bound is still (8.4).

The final terminal source now has both of the following simultaneous properties:
$$
\boxed{
\langle M_2r_b^{\rm fin},z\rangle=0
\quad(z\in\mathscr E_{H_m,b}\cap\mathscr D),
}
\tag{8.9}
$$
$$
\boxed{
\|P_{\rm tr}'r_b^{\rm fin}\|_M^2+
\|P_{\rm ang}'r_b^{\rm fin}\|_M^2
\le2\delta\,\Xi(r_b^{\rm fin})^2.
}
\tag{8.10}
$$
Since $H_m\to\infty$, (8.9) includes each fixed original prefix head flag intersected with the same $\mathscr D$ for all sufficiently large $m$.

The primes in (8.10) matter. These are the flags after intersection with the exact head residual constraint (8.2), not the earlier flags on all of $\mathscr D$. If $\mathscr D$ is the full common-cost graph, (8.9) is not an assertion about the larger intersection with only $\mathscr N_b$. If instead one initially chooses $\mathscr D=\mathscr N_b$, the theorem gives that larger head test but does not newly impose the full common-cost graph.

Thus one can keep an exact growing-head metric test while also imposing two simultaneous relative tests, with all actual-source transport paid. Neither (8.9) nor (8.10) deletes physical head coordinates. Bound (8.7) still does not pay convergence of the ordinary full right-cost difference, and the fixed physical test/Riesz interface remains a separate problem.
