# R271 appendix — a tail-adaptive joint quotient with complete top-cost transport

Date: 2026-11-14 UTC. Author: Astra-ISP-1cf8c51d / boundary_resume_2220; AI-assisted, GPT-6 Astra Pro.

Status: **proved.** At one original actual good top, the growing physical source-head flag can first be removed exactly in the two-fee metric. A subsequent joint spectral quotient can then impose two simultaneous relative tests while preserving both the same actual left vector and the original complete right minimum. The thresholds below use only the actual tail error of the same fixed defect vector; no extra tail rate is assumed.

This is a full-cost version of the joint construction, with the specified tail-dependent triplet range and angle cutoff. It does not assert complete-cost transport for the larger ranges in the earlier left-only application. It does not prove the remaining fixed-test Gram bound, a pure high-Schur inverse estimate, unweighted $N=M$, or the ordinary Hilbert ISP.

Dependencies:

- [Exact good-top two-fee quotient and tail-dependent original triplet range](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md).
- [Joint paid-flag theorem and ordered exact-head intersection](R271-appendix-joint-paid-flag-spectral-quotient-at-an-actual-good-top.md).
- [Dyadic original-head repair with explicit costs](R271-appendix-dyadic-original-heads-birth-one-repair-and-explicit-growing-quotient.md).
- [Original linear triplet-count distortion](R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md).
- [Fixed physical tests and the minimum same-source two-chain Gram](R271-appendix-fixed-physical-tests-and-minimum-two-chain-local-gram.md).

## 1. The same original top and the same two costs

Use the original $A_m,D_m$, $d=2^m$, and
$$
Q=\lfloor e^{d^3/4}\rfloor.
$$
For a hypothetical fixed nonzero $w\in W$, put $W_0=\|w\|$ and retain the exact actual error
$$
\varepsilon=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|
 +(e^{-74d^4}+e^{-75d^4})W_0,\qquad
\rho=\varepsilon/W_0.
\tag{1.1}
$$
Thus $\rho>0$ and $\rho\to0$, without an imposed rate. All claims below apply for sufficiently large $m$, so $0<\rho<1$.

The original disjoint future bands give $K$ candidate cuts in the upper half, with
$$
K\ge Q/(4d),\qquad K\asymp Q/d.
$$
Choose one actual good cut $b$ before any deletion. Its original source satisfies
$$
r=r_b\in\mathscr D,\qquad
\Xi(r)^2\le 2\varepsilon^2/K,\qquad
\|E_b^\dagger r-w\|\le\varepsilon.
\tag{1.2}
$$
Here $\mathscr D$ is one fixed closed original constraint already satisfied by this source and contained in the true source-flow range
$\mathscr N_b=\ker\iota_0^*(L+B)$.
One may use the full common-cost negative graph, or just this basic negative graph, but the same choice is used throughout.

At this one window write
$$
L=J_{\rm left}^{-1},\quad B=J_{\rm bare}^{-1},\quad G=J_{\rm full},
\quad M_2=B+LGL.
$$
The costs are
$$
\mu(r)^2=\langle Lr,r\rangle,\quad
\alpha(r)^2=\langle Br,r\rangle,\quad
\lambda(r)^2=\langle G^{-1}r,r\rangle,
$$
$$
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle M_2r,r\rangle.
\tag{1.3}
$$
In particular $\alpha\le\lambda$. The maps $E_b^\dagger$ and $F_b^\dagger$ are the genuine linear minimum left and complete right selectors. No flat source is reselected.

All projections below are orthogonal in the actual $M_2$ inner product, denoted by $(\cdot,\cdot)_M$.

## 2. Remove the growing head flag exactly

Set
$$
H_m=2^{\lfloor3m/4-2\rfloor},\qquad
Z_H=(\mathscr R_b\cap\ker A_m^{H_m})\cap\mathscr D,
$$
$$
p_H=P_{Z_H}^{M_2}r,\qquad r^{(0)}=r-p_H,\qquad
\mathscr D_1=\mathscr D\cap Z_H^{\perp_M}.
\tag{2.1}
$$
The dyadic head theorem uses the original $d$-dependent tail flags and gives
$$
\mu(p_H)\le a_m\varepsilon,\qquad
\lambda(p_H)\le b_m\varepsilon,
$$
$$
a_m=8\sqrt d\,e^{-11d^3/128},\qquad
b_m=32\sqrt d\,e^{-3d^3/64}.
\tag{2.2}
$$
These bounds remain valid on the smaller intersection with $\mathscr D$. We have
$r^{(0)}\in\mathscr D_1$ and exact metric Pythagoras.

This first step is retained exactly. Every further subspace will be intersected with $\mathscr D_1$, so none of the later corrections can undo the head condition.

## 3. Two closed original flags with a paid second moment

### 3.1 The actual triplet range

Choose
$$
\sigma=\min\left\{\rho^{-1/2},(d/m^2)^{1/4}\right\},\qquad
X=\sqrt{Q/d},
$$
$$
R=\left\lfloor\frac{\sigma mX}{128}\right\rfloor,\qquad
s=R-1,\qquad T_{\rm height}=2R-1.
\tag{3.1}
$$
At the actual top $b$ take $N_{\rm pairs}=b-R+1$ original adjacent pairs and
$J_{\rm tail}=m+2N_{\rm pairs}$.
The whole original joint range $\mathscr E_{\rm tr}$ includes every location of $\ell\le R$ complete triplet blocks, with far-tail primitive birth restrictions
$$
0\le j_{\rm far}\le R-1\quad(\ell=0),\qquad
0\le j_{\rm far}\le R-\ell\quad(1\le\ell\le R).
\tag{3.2}
$$
The active model degree is $s+\ell-j_{\rm far}$, between
$\max(0,2\ell-1)$ and $2R-1$.
Thus all model high-input spaces vanish on precisely this proved range.
The full original head, all its source-tail flags, and the same pair partition are retained.

For large $m$, $\sigma\to\infty$, $R\ge d$, and $R\le b/2$.
The original joint tower parameter obeys
$$
\theta=
\frac{12(2R+d)(2R+d-1)}{J_{\rm tail}+1}
\le \frac{216R^2}{Q}
\le \frac{27\sigma^2m^2}{2048d}
\longrightarrow0.
\tag{3.3}
$$
Indeed $\sigma^2m^2/d\le m/\sqrt d\to0$.
The proved original linear distortion therefore gives
$$
\lambda|_{\mathscr E_{\rm tr}}\le C_{\rm tr}\alpha,\qquad
C_{\rm tr}\le32(1+R/m)\le\sigma\sqrt K
\le\sqrt{K/\rho}.
\tag{3.4}
$$
For completeness, the middle bound follows from
$32(1+R/m)\le32+\sigma X/4\le\sigma X/2$
eventually and $\sqrt K\ge X/2$.
No count of modes or births has been discarded.

### 3.2 The tail-dependent angle flag

In the original bare-normalized coordinates put
$$
\mathcal C=B^{1/2}GB^{1/2},\qquad 0<\mathcal C\le I.
$$
Choose the cutoff
$$
\tau=\max\{\rho/K,K^{-2}\},\qquad
\mathscr E_{\rm ang}
=B^{-1/2}\operatorname{Ran}1_{[\tau,1]}(\mathcal C).
\tag{3.5}
$$
It is a closed original source space. For $z$ in this space,
$$
\lambda(z)^2
=\langle\mathcal C^{-1}B^{1/2}z,B^{1/2}z\rangle
\le\tau^{-1}\alpha(z)^2.
$$
Consequently
$$
C_{\rm ang}=\tau^{-1/2}
=\min\{\sqrt{K/\rho},K\}\le\sqrt{K/\rho}.
\tag{3.6}
$$
The maximum in (3.5) ensures that this angle flag never exceeds the previously used range $\mathcal C\ge K^{-2}$. No relation between the unknown rate $\rho$ and $K^{-1}$ is assumed.

Intersect both flags with the already fixed head residual constraint:
$$
Z_{\rm tr}=\mathscr E_{\rm tr}\cap\mathscr D_1,\qquad
Z_{\rm ang}=\mathscr E_{\rm ang}\cap\mathscr D_1.
\tag{3.7}
$$
Their inequalities survive restriction. If their true metric projections on $\mathscr D_1$ are $P_{\rm tr},P_{\rm ang}$, the average
$$
T_1=\tfrac12(P_{\rm tr}+P_{\rm ang})
\tag{3.8}
$$
is positive and contractive in the $M_2$ metric.
Its two paid constant moments satisfy
$$
\overline C=\tfrac12(C_{\rm tr}+C_{\rm ang})\le\sqrt{K/\rho},
\qquad
\overline{C^2}=\tfrac12(C_{\rm tr}^2+C_{\rm ang}^2)\le K/\rho.
\tag{3.9}
$$
The second bound is needed for the complete right cost.

## 4. Pay the joint overlap without losing the complete cost

Take
$$
\delta=\sqrt\rho,\qquad
p_1=1_{[\delta,1]}(T_1)r^{(0)},\qquad
r^{\rm fin}=r^{(0)}-p_1.
\tag{4.1}
$$
All these spectra use the actual $M_2$ Hilbert structure on $\mathscr D_1$.

We recall the paid joint estimate, including its proof. If
$p\in\operatorname{Ran}1_{[\delta,1]}(T_1)$, set $z=T_1^{-1}p$.
Then
$p=(P_{\rm tr}z+P_{\rm ang}z)/2$ and
$$
\frac12\bigl(\|P_{\rm tr}z\|_M^2+\|P_{\rm ang}z\|_M^2\bigr)
=(T_1z,z)_M=\|T_1^{-1/2}p\|_M^2.
$$
On either flag,
$\mu(x)^2\le\lambda(x)\lambda_{\rm flat}(x)
\le C_j\Xi(x)^2/2$ and $\lambda(x)\le C_j\Xi(x)$.
Linearity of the true minimum selectors, the triangle inequality and weighted Cauchy--Schwarz give
$$
\mu(p)^2\le\frac{\overline C}{2\delta}\Xi(p)^2,\qquad
\lambda(p)^2\le\frac{\overline{C^2}}{\delta}\Xi(p)^2.
\tag{4.2}
$$
This pays every overlap through the inverse spectrum. It assumes neither commuting flag projections nor a gap on their whole span.

Since $p_H\perp_M\mathscr D_1$, the two stages have exact three-term Pythagoras:
$$
\boxed{
\Xi(p_H)^2+\Xi(p_1)^2+\Xi(r^{\rm fin})^2
=\Xi(r)^2\le 2\varepsilon^2/K.
}
\tag{4.3}
$$
Substituting (3.9) and $\varepsilon=W_0\rho$ into (4.2) yields
$$
\boxed{
\mu(p_1)^2\le \frac{W_0^2\rho}{\sqrt K},\qquad
\lambda(p_1)^2\le 2W_0^2\sqrt\rho.
}
\tag{4.4}
$$
Both bounds tend to zero for every allowed actual tail.

For the total correction $p=p_H+p_1$, no cross-term orthogonality in the left or complete metrics is assumed. Their triangle inequalities give
$$
\boxed{
\mu(p)\le \ell_m:=
a_m\varepsilon+W_0\rho^{1/2}K^{-1/4}\longrightarrow0,
}
\tag{4.5}
$$
$$
\boxed{
\lambda(p)\le r_m:=
b_m\varepsilon+\sqrt2\,W_0\rho^{1/4}\longrightarrow0.
}
\tag{4.6}
$$
In particular the original minimum complete right chains themselves satisfy
$$
\boxed{
\|F_b^\dagger r-F_b^\dagger r^{\rm fin}\|
=\lambda(p)\le r_m.
}
\tag{4.7}
$$
Thus $|\lambda(r)-\lambda(r^{\rm fin})|\le r_m$ as well.
This is the ordinary full minimum, with all its original Schur contributions. It is not an assertion about the pure high correction selected by a different minimum problem.

## 5. Exact and relative tests on this same terminal source

The terminal source remains in $\mathscr D$ and obeys
$$
\boxed{
\langle M_2r^{\rm fin},z\rangle=0
\quad
\bigl(z\in(\mathscr R_b\cap\ker A_m^{H_m})\cap\mathscr D\bigr).
}
\tag{5.1}
$$
As $H_m\to\infty$, this includes each fixed original prefix-head source flag intersected with the same $\mathscr D$, eventually.

At the same time, positivity of the two projections and the residual spectrum give
$$
\boxed{
\|P_{\rm tr}r^{\rm fin}\|_M^2+
\|P_{\rm ang}r^{\rm fin}\|_M^2
\le2\sqrt\rho\,\Xi(r^{\rm fin})^2.
}
\tag{5.2}
$$
For either $Z_j$ and any $z\in Z_j$,
$$
|\langle M_2r^{\rm fin},z\rangle|
\le \sqrt2\,\rho^{1/4}\,\Xi(r^{\rm fin})\Xi(z).
\tag{5.3}
$$
These are the projections onto the intersections (3.7), not the old projections before imposing (2.1). A full common-cost choice of $\mathscr D$ does not create tests on its larger basic negative graph.

Neither (5.1) nor (5.2) deletes physical coordinates. In the exact primitive source coordinates, the head flag is the slanted strip proved in the fixed-test appendix.

## 6. Reconstruct one original lower flow and pay all feedback

Let $v=E_b^\dagger p$ and
$u_b^{\rm fin}=E_b^\dagger r-v$.
For every retained lower cut $a\le j\le b$, define
$$
u_j^{\rm fin}=P_{\le j}u_b^{\rm fin},\qquad
r_j^{\rm fin}=A_m(u_b^{\rm fin})_j,\qquad
s_j=A_mv_j.
\tag{6.1}
$$
The exact truncation theorem makes these the true left minimum vectors for their sources. In particular all lower sources belong to one actual flow. No lower window independently chooses a spectrum or a new source.

For the true tail inverses and original primitive feedback changes,
$$
\boxed{
\sum_{j=a}^{b-1}
\left(\|D_{j+1}^{\dagger}s_j\|^2+\|\Delta g_{j+1}\|^2\right)
=\|v\|^2-\|P_{\le a}v\|^2\le\ell_m^2.
}
\tag{6.2}
$$
The original minimum-prefix identities retain the physical head weights in this formula.

All retained left vectors satisfy
$$
\boxed{
\sup_{a\le j\le b}\|u_j^{\rm fin}-w\|
\le\varepsilon+\ell_m\longrightarrow0.
}
\tag{6.3}
$$
Use the unchanged disjoint future bands for the lower windows ending by $b-d$. Their total two-fee budget is at most $2(\varepsilon+\ell_m)^2$.
Pay the terminal cut separately by (4.3). Hence
$$
\boxed{
\sum_{j\in I_b}\Xi_j(r_j^{\rm fin})^2
\le 2(\varepsilon+\ell_m)^2+2\varepsilon^2/K
\longrightarrow0.
}
\tag{6.4}
$$
The sharp terminal estimate remains
$\Xi_b(r^{\rm fin})^2\le2\varepsilon^2/K$,
without replacing $\varepsilon$ by $\varepsilon+\ell_m$.
The new exact and relative tests in §5 apply at this terminal cut; they are not imposed for free at every lower cut.

## 7. The fixed-direction obstruction remains in the same source class

The terminal source still satisfies the exact head test needed for the fixed-physical-test Gram
$$
\mathbb K_{n,H_m}=\mathcal A_n^*
(\mathbb R_{\mathfrak D}-\mathbb R_{\mathfrak Z_{H_m}})
\mathcal A_n.
$$
All these operators use the same original $\mathscr D$, source metric and zero-source inverse as in that appendix.
The later joint step stays in this exact residual space, so its minimum two-chain representation continues to apply.

If $w\ne0$, fix one finite-support unit vector $f$ with
$c=|\langle w,f\rangle|>0$.
Equation (6.3) and the unchanged sharp terminal two-fee bound force, for all sufficiently large $m$,
$$
\boxed{
\langle\mathbb K_{n,H_m}f,f\rangle
\ge \frac{c^2K}{8\varepsilon^2},
}
\tag{7.1}
$$
where $n$ contains the support of this same fixed $f$.
The terminal sources producing this requirement now also obey (5.2), and their complete right minimum chains differ from the original actual ones by a norm tending to zero.

The $O(K)$ finite-test Gram bound is still not proved. The added relative tests cannot be silently replaced by exact coordinate conditions in a proposed estimate.

## 8. A family of paid exponents

The choices above are one point in a useful explicit family.
For fixed positive numbers $a_0,b_0$ with $a_0+b_0<2$, take
$$
\delta=\rho^{a_0},\quad
\sigma=\min\{\rho^{-b_0/2},(d/m^2)^{1/4}\},\quad
\tau=\max\{\rho^{b_0}/K,K^{-2}\}.
\tag{8.1}
$$
Use the same formula for $R$, the same exact head step and the same true intersections.
Then $\theta\to0$ as before, and
$$
\overline C\le\sqrt K\,\rho^{-b_0/2},\qquad
\overline{C^2}\le K\rho^{-b_0}.
$$
The identical proof gives
$$
\mu(p_1)^2\le
\frac{W_0^2\rho^{\,2-a_0-b_0/2}}{\sqrt K},\qquad
\lambda(p_1)^2\le
2W_0^2\rho^{\,2-a_0-b_0},
\tag{8.2}
$$
and the sum of the two relative projection squares is at most
$2\rho^{a_0}\Xi(r^{\rm fin})^2$.
Both corrections are paid because $2-a_0-b_0>0$.
The displayed application uses $a_0=1/2,b_0=1$.

This family explicitly separates the cost of a small joint-overlap threshold from the cost of a larger angle range. No uniform tail rate, free union of original flags, or pure high inverse has been used. The complete-cost transport is a finished conclusion; the remaining actual fixed-test estimate and the ordinary ISP remain OPEN.
