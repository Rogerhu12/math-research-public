# R271 appendix — large-triplet and low-angle good-top quotients with complete constrained Schur terms

Date: 2026-11-14 UTC. Author: Astra-ISP-1cf8c51d / boundary_resume_2220; AI-assisted, GPT-6 Astra Pro.

Status: **proved.** The exact two-fee good-top construction has a larger range when the required transport is the actual left vector and its coherent source flow. It permits a fixed original triplet count of order $\sqrt Q$, and a spectral quotient down to angle threshold $K^{-2}$, where $K\asymp Q/d$. This paper gives the complete constrained Schur formula for that spectral quotient, including the full common-cost negative graph.

The remaining left/two-fee comparison is not proved. The ordinary complete right fee of the deleted part is not asserted to tend to zero in these larger ranges. No pure high inverse or ordinary Hilbert ISP conclusion is claimed.

Dependencies:

- [Exact two-fee good-top quotient](R271-appendix-exact-two-fee-good-top-quotient-and-tail-adaptive-mode-deletion.md).
- [Actual truncation and future bands](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md).
- [Joint original low-triplet retraction](R271-appendix-low-triplet-count-joint-retraction-and-original-high-energy-bound.md).
- [Linear distortion by prefix splitting](R271-appendix-linear-triplet-count-distortion-by-prefix-splitting.md).
- [Same-future-band angle identity and complete common-cost negative graph](R239-appendix-future-band-projection-angle-and-complete-common-cost-negative-graph.md).

## 1. The actual good top and the transport that is needed here

Retain the original $m,d=2^m,A_m,D_m$ and
$$
Q=\lfloor e^{d^3/4}\rfloor,\qquad
\varepsilon_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|
 +(e^{-74d^4}+e^{-75d^4})\|w\|,
$$
for the same fixed nonzero actual $w\in W=M\ominus N$.
Write $r_p$ for the actual source induced by the same original top
$u_Q=E_Q^\dagger r_Q$.

As in the good-top paper, take the step-$d$ disjoint grid $I$ starting at
$a\in[4d,5d)$, and its terminal half
$$
J=I\cap[\lceil Q/2\rceil,Q-d],\qquad K=|J|\ge Q/(4d).
$$
Select $b\in J$ with
$$
\Xi_b(r_b)^2\le2\varepsilon_m^2/K,\qquad
K\sim Q/(2d).
\tag{1.1}
$$
All selections use the original source before any projection.

On the original source space keep
$$
L=J_{\rm left}^{-1},\quad B=J_{\rm bare}^{-1},\quad
G=J_{\rm right},\quad
\mathfrak M=B+LGL,\qquad
\Xi(r)^2=\langle\mathfrak Mr,r\rangle.
$$
Thus $\Xi^2=\alpha^2+\lambda_{\rm flat}^2$, and
$\mu^2=\langle Lr,r\rangle$, $\lambda^2=\langle G^{-1}r,r\rangle$.
The actual source-flow negative graph is
$\mathscr N=\ker\iota_0^*(L+B)$.

Let $\mathscr D\subseteq\mathscr N$ be a closed linear constraint space
which this same $r_b$ already satisfies. Take a closed original source
space $\mathscr E$ with
$$
\lambda(s)\le\gamma\alpha(s)\quad(s\in\mathscr E),\qquad\gamma\ge1.
\tag{1.2}
$$
Define
$$
Z=\mathscr E\cap\mathscr D,\quad
s=P_Z^{\mathfrak M}r_b,\quad \widehat r_b=r_b-s.
\tag{1.3}
$$
The same positive-inverse Cauchy estimate gives
$$
\boxed{\mu(s)^2\le\frac{\gamma}{K}\varepsilon_m^2,\qquad
\Xi(\widehat r_b)^2\le\frac{2}{K}\varepsilon_m^2,\qquad
\iota_Z^*\mathfrak M\widehat r_b=0.}
\tag{1.4}
$$

Every lower residual is formed from this one new top:
$$
\widehat r_p=A_mP_pE_b^\dagger\widehat r_b,\qquad p\le b.
$$
It is the true source of the corresponding left minimum and obeys the
exact adjacent source-flow relation. The whole family satisfies
$$
\sup_{a\le p\le b}\|E_p^\dagger\widehat r_p-w\|
 \le(1+\sqrt{\gamma/K})\varepsilon_m,
\tag{1.5}
$$
$$
\boxed{\sum_{p\in I\cap[a,b]}\Xi_p(\widehat r_p)^2
 \le2[(1+\sqrt{\gamma/K})^2+K^{-1}]\varepsilon_m^2.}
\tag{1.6}
$$
The last term is the top metric Pythagoras; all lower selected terms
are paid by disjoint genuine future bands of the new top.
The sum of all squared single-step inverse and primitive feedback
changes is at most $\gamma\varepsilon_m^2/K$.

Consequently
$$
\boxed{\gamma\le c_0 K}
\tag{1.7}
$$
with fixed $c_0$ is enough to preserve the same fixed $w$, all flow,
the whole-window budget, and the feedback budget. This has no
additional tail-rate assumption.

The separately available ordinary right-fee bound is only
$$
|\lambda(r_b)-\lambda(\widehat r_b)|
 \le\sqrt2\,\gamma\varepsilon_m/\sqrt K.
\tag{1.8}
$$
Under (1.7) it need not tend to zero. This paper uses (1.4)--(1.7)
for the actual left/two-fee comparison, and does not infer an
unpaid complete-right or pure-high estimate from them.

## 2. A fixed original triplet range of order sqrt(Q)

For sufficiently large $m$, put
$$
\boxed{R=\lfloor\sqrt Q/64\rfloor,\qquad
s=R-1,\quad T=2R-1.}
\tag{2.1}
$$
For every terminal candidate $q\in J$, use exactly the original
$N_{\rm pair}=q-R+1$ adjacent pairs and
$J_{\rm tail}=m+2N_{\rm pair}$. Eventually
$$
R\ge d,\qquad R\le q/2,\qquad R\le N_{\rm pair}.
$$
The complete joint short-tower parameters are
$$
H=2R+d,\qquad P=2R+d-1.
$$
Since $J_{\rm tail}+1\ge q\ge Q/2$,
$$
\boxed{\theta=\frac{12HP}{J_{\rm tail}+1}
 \le\frac{216R^2}{Q}\le\frac{27}{512}<\frac18.}
\tag{2.2}
$$
Thus the previously proved original linear distortion bound applies:
$$
\gamma\le32(1+R/m)\le32+\frac{\sqrt Q}{2m}.
$$
In particular
$$
\boxed{\frac{\gamma}{K}
 \le\frac{128d}{Q}+\frac{2d}{m\sqrt Q}\longrightarrow0.}
\tag{2.3}
$$

The joint range retains all positions of up to $r\le R$ complete
triplet blocks, and the full far-tail primitive spaces with births
$$
0\le b_{\rm far}\le R-1\quad(r=0),\qquad
0\le b_{\rm far}\le R-r\quad(1\le r\le R).
\tag{2.4}
$$
Their active degree is $t=s+r-b_{\rm far}$, so
$\max(0,2r-1)\le t\le T$. Therefore every selected model high-input
domain is genuinely zero; the proved same-source inequality (1.2)
holds on this entire original closed range. No location count or
birth count is charged.

Intersecting it with the actual top constraint $\mathscr D$ and
using (1.3) pays all selected directions that also belong to that
constraint. It does not claim that the whole range automatically
lies in the negative graph.

Equations (1.4)--(1.6) now give
$$
\mu(s)^2\le
 \left(\frac{128d}{Q}+\frac{2d}{m\sqrt Q}\right)\varepsilon_m^2,
\qquad
\sum_{p\in I\cap[a,b]}\Xi_p(\widehat r_p)^2
 \le[2+o(1)]\varepsilon_m^2.
\tag{2.5}
$$
The entire coherent left family still converges to the same $w$.
This explicit $R\sim\sqrt Q/64$ is much larger than
$m\sqrt{Q/d}$, although it remains much smaller than
$N_{\rm pair}\asymp Q$.

The bound obtained from (1.8) contains a term
$\sqrt{2d}\,\varepsilon_m/m$. No rate for this quantity is assumed,
so complete top-right transport is not part of (2.5).
The exact top two-fee quotient and the actual-source comparison
remain valid independently of that unproved transport.

## 3. Original angle spectral flags are also legitimate cheap spaces

At the selected top use the exact bare normalization
$$
u=B^{1/2}r,\qquad
H=B^{-1/2}LB^{-1/2},\qquad C=B^{1/2}GB^{1/2}.
$$
The same-physical-band result gives $0<C\le I$. The normalized costs are
$$
\alpha(r)^2=\|u\|^2,\qquad
\lambda(r)^2=\langle C^{-1}u,u\rangle,\qquad
\mu(r)^2=\langle Hu,u\rangle,
$$
$$
\Xi(r)^2=\langle\mathsf M u,u\rangle,\qquad
\mathsf M=I+HCH.
\tag{3.1}
$$
All operators here are the actual fixed-window operators.
No commutation of $H$ and $C$ is assumed.

Define spectral projections
$$
\boxed{E=1_{[K^{-2},1]}(C),\qquad F=I-E,\qquad
P_1=1_{\{1\}}(C).}
\tag{3.2}
$$
The original closed space
$\mathscr E=B^{-1/2}\operatorname{Ran}E$ satisfies
$\lambda\le K\alpha$, directly from spectral calculus.

Moreover the initial actual $r_b$ has its full future band inside
$u_Q$. Hence the original angle identity proves
$$
P_1(I+H)u_b=0.
\tag{3.3}
$$
This includes every original source-flow kernel-head condition.
Choose the already satisfied top constraint
$$
\mathscr D=B^{-1/2}\ker[P_1(I+H)].
\tag{3.4}
$$
Then (1.3) is a true top projection onto the intersection, with
$\gamma=K$. Its residual obeys
$$
\boxed{
P_1(I+H)\widehat u=0,\qquad
\langle\mathsf M\widehat u,z\rangle=0
\quad\bigl(z\in\operatorname{Ran}E,\
 P_1(I+H)z=0\bigr).
}
\tag{3.5}
$$
This preserves the complete common-cost negative graph at the top.

The actual-source budgets are explicit:
$$
\boxed{
\mu(s)\le\varepsilon_m,\quad
\Xi(\widehat r_b)^2\le2\varepsilon_m^2/K,\quad
\sup_{a\le p\le b}\|E_p^\dagger\widehat r_p-w\|\le2\varepsilon_m,
}
\tag{3.6}
$$
$$
\sum_{p\in I\cap[a,b]}\Xi_p(\widehat r_p)^2
 \le(8+2/K)\varepsilon_m^2.
\tag{3.7}
$$
All feedback changes have total squared norm at most
$\varepsilon_m^2$.

This differs from imposing an unproved zero high-spectral coordinate:
the actual residual generally has a nonzero $E$ component.
It is determined by the constrained metric equations (3.5).
The next section supplies that component exactly.

## 4. The complete constrained Schur parametrization

Work in $\operatorname{Ran}E\oplus\operatorname{Ran}F$, and denote
the blocks of the true normalized metric by
$$
\mathsf M=
\begin{pmatrix}\mathcal A&\mathcal B\\
\mathcal B^*&\mathcal D\end{pmatrix},\qquad
\mathcal A\ge I_E.
$$
Define the two constraint rows
$$
\mathcal P=P_1(I_E+H_{EE}),\qquad
\mathcal Q=P_1H_{EF}.
\tag{4.1}
$$
They map into $\operatorname{Ran}P_1$. Since $P_1\le E$,
$\mathcal P$ is surjective: the bounded map
$(I_E+H_{EE})^{-1}P_1$ is a right inverse of norm at most one.
Thus there is no hidden closed-range assumption.

Set
$$
\mathcal S=\mathcal P\mathcal A^{-1}\mathcal P^*,\qquad
\mathcal T=\mathcal P\mathcal A^{-1}\mathcal B-\mathcal Q.
\tag{4.2}
$$
The right-inverse observation gives
$\|\mathcal P^*\eta\|\ge\|\eta\|$, so
$\mathcal S\ge\|\mathcal A\|^{-1}I_{P_1}$.
It has a bounded inverse for each fixed window.

For the residual write $f=F\widehat u$ and $x=E\widehat u$.
Its two equations (3.5) are exactly the KKT system
$$
\mathcal A x+\mathcal Bf=\mathcal P^*\eta,\qquad
\mathcal Px+\mathcal Qf=0.
\tag{4.3}
$$
Indeed the first equation is orthogonality to
$\ker\mathcal P\subseteq E$; surjectivity makes its orthogonal
complement precisely $\operatorname{Ran}\mathcal P^*$.

Solving without changing any multiplication order gives
$$
\eta=\mathcal S^{-1}\mathcal T f,\qquad
\boxed{x=\mathcal Xf,\quad
\mathcal X=-\mathcal A^{-1}\mathcal B
+\mathcal A^{-1}\mathcal P^*\mathcal S^{-1}\mathcal T.}
\tag{4.4}
$$
When $P_1=0$, the multiplier terms disappear.
The formula also applies to a zero-dimensional spectral block
with its natural zero-space conventions.

Completing the actual metric square yields
$$
\boxed{\Xi(\widehat r_b)^2
=\langle\mathsf M_{\rm eff}f,f\rangle,}
$$
$$
\boxed{\mathsf M_{\rm eff}
=\mathcal D-\mathcal B^*\mathcal A^{-1}\mathcal B
+\mathcal T^*\mathcal S^{-1}\mathcal T.}
\tag{4.5}
$$
In particular $\mathsf M_{\rm eff}\ge I_F$.
The exact actual left energy is
$$
\boxed{\mu(\widehat r_b)^2
=\langle H_{\rm eff}f,f\rangle,\qquad
H_{\rm eff}=H_{FF}+H_{FE}\mathcal X
+\mathcal X^*H_{EF}+\mathcal X^*H_{EE}\mathcal X.}
\tag{4.6}
$$
The extra positive term in (4.5), and all three feedback terms
beside $H_{FF}$ in (4.6), are retained. Neither expression is
replaced by a principal block.

Thus the actual residual is parametrized by the low-angle
coordinate $f\in\operatorname{Ran}1_{(0,K^{-2})}(C)$, while its
high-angle coordinate is the generally nonzero vector (4.4).

## 5. Exact remaining comparison and limitations

By (3.6), the left minimum at this one top converges to $w\ne0$,
but its two-fee energy is at most $2\varepsilon_m^2/K$.
Therefore
$$
\frac{\langle H_{\rm eff}f_m,f_m\rangle}
 {K\langle\mathsf M_{\rm eff}f_m,f_m\rangle}
\longrightarrow\infty
\tag{5.1}
$$
for these actual residual coordinates, if a nonzero defect exists.
Any uniform $O(K)$ comparison of (4.6) by (4.5), even only on
these actual good-top residuals along an infinite head subsequence,
would exclude that defect.

No such comparison follows from positivity alone.
For example an abstract one-dimensional choice
$0<C=c<K^{-2}$ and $H=c^{-1/2}$ has $\mathsf M=2$, so its ratio
is $1/(2\sqrt c)$, arbitrarily larger than $K$.
This is only an illustration about abstract positive operators;
it is not an original finite-head or actual-source counterexample.

The original matrices, their adjacent flow, and their constrained
Schur feedback must still provide the missing estimate.
The triplet quotient of section 2 and the spectral quotient of
sections 3--4 are individually paid alternatives. Their sum or
successive combination is not asserted to remain cheap without
additional estimates. The same qualification applies to combining
different physical pairings or retaining earlier orthogonality
conditions not included in the actual top constraint.
