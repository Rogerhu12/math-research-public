# R271 appendix — a coherent good top with a growing negative prefix and an exact large-head metric test

Date: 2026-11-14 UTC. Author: Astra-ISP-1cf8c51d / boundary_resume_2220; AI-assisted, GPT-6 Astra Pro.

Status: **proved.** The previously paid growing $L+B$ negative-prefix correction can be performed at the same actual good top selected together with a fixed physical test space. Reconstructing all lower cuts from that one corrected minimum preserves a genuine source flow. The negative-prefix constraint can then be retained through the exact large-head $M_2$ deletion and the tail-adaptive joint quotient.

The initial negative-prefix correction pays the left norm and the original two-fee budget. Its ordinary complete right cost is not proved small. Complete right-cost transport in the later steps is only from the already corrected top. This distinction is retained in every formula below.

Dependencies:

- [R239 original columnwise prefix and near-common cost](R239-appendix-columnwise-head-budget-and-cubic-log-negative-prefix.md).
- [Exact source-flow range and fibers](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md).
- [Exact good-top projection and coherent lower flow](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md).
- [Ordered head and paid joint projection theorem](R271-appendix-joint-paid-flag-spectral-quotient-at-an-actual-good-top.md).
- [Tail-adaptive joint complete-cost transport](R271-appendix-tail-adaptive-joint-quotient-with-complete-top-cost-transport.md).
- [Fixed-test adjoint flow and joint good-top budget](R271-appendix-fixed-test-adjoint-source-flow-and-joint-good-top-budget.md).

## 1. Choose one actual cut before all corrections

Use the same original $m,d=2^m,A_m,D_m$ and a hypothetical fixed nonzero $w$, with $W_0=\|w\|$. Let $\varepsilon>0$ be its original tail-plus-lift error, $\rho=\varepsilon/W_0\to0$, and
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad K\asymp Q/d,\qquad K\ge Q/(4d).
$$
Fix a finite physical test space $\mathscr T_N$.
The adjoint-flow good-top theorem selects the same cut $b\ge Q/2$, $b+d\le Q$, such that the original future band $y_b$ and original source $r$ obey
$$
\|y_b\|^2\le 2\varepsilon^2/K,\qquad
\Xi(r)^2\le2\|y_b\|^2\le4\varepsilon^2/K,
\tag{1.1}
$$
$$
\|E_b^\dagger r-w\|\le\varepsilon,\qquad
D_b^{(N)}\preceq(4N/K)I.
\tag{1.2}
$$
The last matrix is the genuine fixed-test dissipation on $[b,b+d]$, not a source model.

At this one cut put
$$
L=J_{\rm left}^{-1},\quad B=J_{\rm bare}^{-1},\quad G=J_{\rm full},
\quad M_2=B+LGL,
$$
$$
u=B^{1/2}r,\quad H=B^{-1/2}LB^{-1/2},\quad
C=B^{1/2}GB^{1/2},\qquad 0<C\le I.
\tag{1.3}
$$
Then $\Xi(r)^2=\|u\|^2+\|C^{1/2}Hu\|^2$ and
$\mu(r)^2=\langle Hu,u\rangle$.

All source metrics below are original fixed-window operators, bounded and strictly positive there. No parameter-uniform inverse bound is inserted.

## 2. The original near-common prefix gives a small negative-relation defect

Let
$$
k_m=\max\left\{2,1+\left\lfloor
(\log m/7072)^{1/3}\right\rfloor\right\},
\qquad
\mathscr X_k=\mathscr R_b\cap\ker A_m^{k_m},
$$
and let $W_k=B^{1/2}\mathscr X_k$.
All original $d-i-1$ tail flags are retained.

The cited columnwise theorem gives on this whole source flag
$$
\lambda(s)^2\le(1+\psi_m^2)\alpha(s)^2,\qquad
\psi_m\le \frac{2}{m(1-m^{-1/2})}\longrightarrow0.
\tag{2.1}
$$
Consequently the compression of $C^{-1}-I$ to $W_k$ is at most
$\psi_m^2 I$.

The original same-future relation is
$$
C^{1/2}Hu=(I-C)^{1/2}z-C^{1/2}u,\qquad
\|u\|^2+\|z\|^2\le\|y_b\|^2.
$$
Hence
$$
(I+H)u=(C^{-1}-I)^{1/2}z.
$$
For the actual negative-relation defect
$$
\omega=P_{W_k}(I+H)u
$$
we therefore have
$$
\boxed{\|\omega\|\le\psi_m\|y_b\|.}
\tag{2.2}
$$
This is the original future-band statement, used before changing the source.

Define the actual closed prefix-negative graph
$$
\mathscr D_k
=\{s\in\mathscr R_b:
\langle(L+B)s,x\rangle=0\text{ for all }x\in\mathscr X_k\}.
\tag{2.3}
$$
It is contained in the basic source-flow range
$\mathscr N_b=\ker\iota_0^*(L+B)$ because $\mathscr X_k$ contains the entire first source head.

## 3. One paid correction, with its exact scope

Set
$$
v=(I+H)^{-1}\omega,\qquad
t=B^{-1/2}v,\qquad r^{\rm neg}=r-t.
\tag{3.1}
$$
Then
$$
P_{W_k}(I+H)(u-v)=0,
\qquad r^{\rm neg}\in\mathscr D_k.
\tag{3.2}
$$
Since both $r$ and $r^{\rm neg}$ lie in $\mathscr N_b$, the correction $t$ does too. Equivalently, the first-head normalized subspace is contained in $W_k$ and is orthogonal to the original $(I+H)u$, hence to $\omega$.

The original two-fee and left costs of $t$ satisfy
$$
\begin{aligned}
\Xi(t)^2+2\mu(t)^2
&=\|v\|^2+\|C^{1/2}Hv\|^2+2\langle Hv,v\rangle\\
&\le\|(I+H)v\|^2=\|\omega\|^2.
\end{aligned}
\tag{3.3}
$$
Also $x/(1+x)^2\le1/4$ for $x\ge0$, so
$$
\boxed{
\Xi(t)\le\psi_m\|y_b\|,\qquad
\mu(t)\le\tfrac12\psi_m\|y_b\|
\le\frac{\psi_m\varepsilon}{\sqrt{2K}}.
}
\tag{3.4}
$$
Thus, with $c_m=\sqrt2+\psi_m$,
$$
\boxed{
\Xi(r^{\rm neg})^2\le c_m^2\|y_b\|^2
\le\frac{2c_m^2\varepsilon^2}{K}.
}
\tag{3.5}
$$
The initial split (3.1) is not claimed to be orthogonal for $M_2$. Formula (3.5) uses its triangle inequality, not a false Pythagoras identity.

Nor is $t$ claimed to belong to $\mathscr X_k$: the full inverse $(I+H)^{-1}$ may leave the prefix. The estimate (2.1) therefore does not pay $\lambda(t)$.

## 4. Retain this negative graph through the later exact and joint tests

Perform the proved ordered construction with the definite constraint
$\mathscr D=\mathscr D_k$.

First set
$$
H_m=2^{\lfloor3m/4-2\rfloor},\qquad
Z_H=(\mathscr R_b\cap\ker A_m^{H_m})\cap\mathscr D_k,
$$
$$
p_H=P_{Z_H}^{M_2}r^{\rm neg},\qquad
r^{(0)}=r^{\rm neg}-p_H,\qquad
\mathscr D_1=\mathscr D_k\cap Z_H^{\perp_{M_2}}.
\tag{4.1}
$$
Then use the original triplet range
$$
\sigma=\min\{\rho^{-1/2},(d/m^2)^{1/4}\},\quad
R=\lfloor\sigma m\sqrt{Q/d}/128\rfloor,
$$
with the already paid births, and the original angle range
$$
B^{-1/2}\operatorname{Ran}
1_{[\max(\rho/K,K^{-2}),1]}(C).
$$
Intersect both with this very $\mathscr D_1$, let their true $M_2$ projections be $P_{\rm tr},P_{\rm ang}$, and put
$$
T_1=\tfrac12(P_{\rm tr}+P_{\rm ang}),\qquad
p_1=1_{[\sqrt\rho,1]}(T_1)r^{(0)},\qquad
r^{\rm fin}=r^{(0)}-p_1.
\tag{4.2}
$$

Because (3.5) is the original sharp bound with $\varepsilon$ multiplied by $c_m$, positive homogeneity in the paid proofs gives
$$
\mu(p_H)\le c_m a_m\varepsilon,\qquad
\lambda(p_H)\le c_m b_m\varepsilon,
$$
$$
a_m=8\sqrt d\,e^{-11d^3/128},\qquad
b_m=32\sqrt d\,e^{-3d^3/64},
\tag{4.3}
$$
$$
\boxed{
\mu(p_1)^2\le
\frac{c_m^2W_0^2\rho}{\sqrt K},\qquad
\lambda(p_1)^2\le2c_m^2W_0^2\sqrt\rho.
}
\tag{4.4}
$$
The choice of $\rho$ in the flags remains the original $\varepsilon/W_0$; it need not be replaced by a larger error parameter.

Only these last two stages have exact three-term Pythagoras:
$$
\boxed{
\Xi(p_H)^2+\Xi(p_1)^2+\Xi(r^{\rm fin})^2
=\Xi(r^{\rm neg})^2
\le2c_m^2\varepsilon^2/K.
}
\tag{4.5}
$$

The final terminal source simultaneously has:
$$
\boxed{\langle(L+B)r^{\rm fin},x\rangle=0
\quad(x\in\mathscr X_k),}
\tag{4.6}
$$
$$
\boxed{\langle M_2r^{\rm fin},z\rangle=0
\quad(z\in Z_H),}
\tag{4.7}
$$
$$
\boxed{
\|P_{\rm tr}r^{\rm fin}\|_{M_2}^2+
\|P_{\rm ang}r^{\rm fin}\|_{M_2}^2
\le2\sqrt\rho\,\Xi(r^{\rm fin})^2.
}
\tag{4.8}
$$
The $L+B$ prefix and the much larger $M_2$ head test are different constraints. Neither sets source coordinates to zero. No full common-cost graph beyond (2.3) is newly claimed.

## 5. One coherent lower source flow survives all three stages

The total source change is
$$
p=t+p_H+p_1.
$$
Its genuine left cost is bounded by
$$
\boxed{
\mu(p)\le\ell_m:=
\frac{\psi_m\varepsilon}{\sqrt{2K}}
+c_m\bigl(a_m\varepsilon+W_0\rho^{1/2}K^{-1/4}\bigr)
\longrightarrow0.
}
\tag{5.1}
$$
For every retained lower cut $a\le j\le b$, define from the single new top
$$
u_b^{\rm fin}=E_b^\dagger r^{\rm fin},\qquad
u_j^{\rm fin}=P_{\le j}u_b^{\rm fin},\qquad
r_j^{\rm fin}=A_m(u_b^{\rm fin})_j.
\tag{5.2}
$$
Exact left truncation makes these the true minimum left vectors for their sources. The whole family is one original source flow. This step is what is not provided merely by correcting each old cut independently.

If $v=E_b^\dagger p$ and $s_j=A_mv_j$, the true fiber identity gives
$$
\boxed{
\sum_{j=a}^{b-1}
\bigl(\|D_{j+1}^\dagger s_j\|^2+\|\Delta g_{j+1}\|^2\bigr)
\le\|v\|^2\le\ell_m^2.
}
\tag{5.3}
$$
Consequently
$$
\boxed{
\sup_{a\le j\le b}\|u_j^{\rm fin}-w\|
\le\varepsilon+\ell_m\longrightarrow0,
}
\tag{5.4}
$$
and the unchanged disjoint lower future bands, with (4.5) for the terminal cut, give
$$
\boxed{
\sum_{j\in I_b}\Xi_j(r_j^{\rm fin})^2
\le2(\varepsilon+\ell_m)^2+2c_m^2\varepsilon^2/K.
}
\tag{5.5}
$$
Only the selected terminal cut carries (4.6)–(4.8). The reconstructed lower cuts are not independently required to satisfy those extra tests.

The ordinary full right minimum chains at the last two stages obey
$$
\|F_b^\dagger r^{\rm neg}-F_b^\dagger r^{\rm fin}\|
\le c_m\bigl(b_m\varepsilon+\sqrt2W_0\rho^{1/4}\bigr)\to0.
\tag{5.6}
$$
There is no bound here for
$\|F_b^\dagger r-F_b^\dagger r^{\rm neg}\|=\lambda(t)$.
Thus (5.6) is not presented as complete-cost transport from the initial source.

## 6. The same fixed-test interface and the retained original future band

The Riesz test maps depend only on the original operators, $b$ and the fixed $f$, so the selection (1.2) and its actual test dissipation remain valid after every source change.

In particular,
$$
|\langle E_b^\dagger r^{\rm fin}-E_b^\dagger r,f\rangle|
\le\ell_m\|f\|.
\tag{6.1}
$$
The fixed-physical-test Gram can now be formed with the explicit negative graph $\mathscr D_k$ and its exact head intersection $Z_H$.
Since $c_m\to\sqrt2$, its required window-count order is unchanged.

More precisely, if a fixed finite-support unit $f$ has
$c=|\langle w,f\rangle|>0$, then for all sufficiently large $m$,
$$
\langle\mathbb K_{N,H_m}^{(\mathscr D_k)}f,f\rangle
\ge \frac{c^2K}{8c_m^2\varepsilon^2}.
\tag{6.2}
$$
This follows from (4.5), (5.4) and the exact minimum dual-chain representation. Its converse $O(K)$ upper bound remains open.

The original adjoint-flow weak-error estimate on $[b+1,b+d]$ continues to concern the original actual source flow induced by $u_Q$. The new coherent flow (5.2) is asserted only below $b$. No continuation beyond $b$ is invented to reuse that weak estimate on a different source.
Formula (6.1) is the paid connection between their terminal fixed-test values.

The finished conclusion is a coherent actual-source quotient with a growing negative prefix, an exact larger metric-head test and two simultaneous relative tests, with the whole lower flow and original two-fee budgets retained. The initial correction's full right cost, the genuine terminal dual-chain estimate and the ordinary ISP remain OPEN.
