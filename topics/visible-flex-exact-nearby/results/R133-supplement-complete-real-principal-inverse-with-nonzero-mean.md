# R133 supplement: complete real principal inverse with nonzero mean

2026-11-15, visible-exact / newton_source.

**Proved full-circle principal inverse and a conditional high-block consequence.** For a real coefficient $c$, the complete operator $1+M_cI$ is invertible with its actual mean couplings retained. Its inverse has explicit bounds on $L^2$ and $H^{-4/3}$ that do not grow with $|\langle c\rangle|$. This extends the mean-zero normalizer formula to the individual incoming coefficient identified in IC. It does not discard the complete incoming error, any finite row, or the physical mean coordinates.

No new scientific computation is performed. Numerical use of the coefficient bounds awaits the complete same-object terminal columns and their true-angle conversion.

## 1. Spaces and a complete shifted primitive

Use the normalized circle of length $P=\pi/2$, physical frequencies $4j$, and
$$
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 \|f\|_{H^s}^2=\sum_{j\in\mathbb Z}(1+16j^2)^s|\widehat f_j|^2.
 \tag{MI.1}
$$
Let $c$ be real, with
$$
 \nu=\langle c\rangle,\qquad b=c-\nu,\qquad
 p=Ib,\qquad a=e^p .
 \tag{MI.2}
$$
It suffices that $b\in H^3$; then all products and dual rows below have the stated regularity. In particular $p$ is real and has mean zero. The parameter $\nu$ here is the mean of this coefficient, not the unrelated geometric parameter that has appeared elsewhere.

For real $\nu$ define, on nonzero modes,
$$
 \widehat{I_\nu f}_j=\frac{\widehat f_j}{i4j+\nu},\qquad
 \widehat{I_\nu f}_0=0,\qquad
 J_\nu=\Pi+\nu I_\nu .
 \tag{MI.3}
$$
At $\nu=0$, these are exactly $I_0=I$ and $J_0=\Pi$. For every $s$,
$$
 \|I_\nu:H^s\to H^s\|\le\frac14,\quad
 \|I_\nu:H^s\to H^{s+1}\|\le\frac{\sqrt{17}}4,\quad
 \|J_\nu:H^s\to H^s\|\le1 .
 \tag{MI.4}
$$
The last assertion includes the mean multiplier one. None of these bounds divides by $\nu$.

For $\nu\ne0$, the complete formula on periodic functions is
$$
 J_\nu f(x)=
 \frac{\nu}{1-e^{-\nu P}}\int_0^P e^{-\nu t}f(x-t)\,dt .
 \tag{MI.5}
$$
The weight is positive and has total mass one for both signs of $\nu$.
For negative $\nu$ it concentrates in the opposite cyclic direction. The limit at zero is the complete normalized mean $\Pi$. In particular $J_\nu$ and its adjoint preserve positivity and constants.

## 2. A strictly positive denominator with all mean terms

Set
$$
 d_\nu=\langle a^{-1}J_\nu a\rangle .
 \tag{MI.6}
$$
For each translation in (MI.5), Jensen's inequality gives
$$
 \left\langle e^{p(x-t)-p(x)}\right\rangle\ge
 \exp\langle p(x-t)-p(x)\rangle=1 .
$$
Averaging over its positive kernel, or using $J_0=\Pi$, proves
$$
                         d_\nu\ge1 .
 \tag{MI.7}
$$
Also $\langle a\rangle,\langle a^{-1}\rangle\ge1$. These inequalities use real $p$ and the complete circle. They are not claimed for complex coefficients or complex angular shifts.

For an input $f$ define, in this order,
$$
 \begin{split}
 m(f)&=\frac{\langle a^{-1}J_\nu(af)\rangle}{d_\nu},\\
 u(f)&=I_\nu[a(f-m(f))],\\
 \kappa(f)&=-\frac{\langle a^{-1}u(f)\rangle}
                         {\langle a^{-1}\rangle},\\
 v(f)&=a^{-1}(u(f)+\kappa(f)),\\
 h(f)&=f-cv(f).
 \end{split}\tag{MI.8}
$$
Every mean in (MI.8) is retained. For distributional $f$, it denotes the pairing against the corresponding smooth real row, extended by the proved Sobolev bounds.

Here is the necessary constant identity. With $g=a(f-m(f))$, the definition of $m$ gives
$$
 0=\langle a^{-1}J_\nu g\rangle
   =\langle a^{-1}\rangle\langle g\rangle
          +\nu\langle a^{-1}I_\nu g\rangle,
 \qquad
                  \langle g\rangle=\nu\kappa(f).
 \tag{MI.9}
$$
Thus the added constant $\kappa$ is not arbitrary: it simultaneously enforces the zero mean of $v$ and the missing constant equation. Since
$(\partial_\phi+\nu)u=(1-\Pi)g$, (MI.9) gives
$$
 (\partial_\phi+\nu)(u+\kappa)=g,\qquad
                    v'+cv=f-m(f).
 \tag{MI.10}
$$
As a result,
$$
 \langle v\rangle=0,\qquad h=v'+m(f),\qquad Ih=v,\qquad
                         (1+M_cI)h=f.
 \tag{MI.11}
$$

Conversely, if $(1+M_cI)h=f$, put $v=Ih$ and $m=\langle h\rangle$.
Then $v'+cv=f-m$ and $\langle v\rangle=0$. Multiplication by $a$ and application of $J_\nu$ yield precisely the scalar condition (MI.9), and hence the unique $m$ in (MI.8), since $d_\nu>0$. The nonmean part and the mean of $av$ are then respectively $u$ and $\kappa$. Thus (MI.8) is the complete two-sided inverse.

At $\nu=0$ the first line reduces exactly to
$$
                  m(f)=\frac{\langle af\rangle}{\langle a\rangle},
$$
the original CN/LN formula. For $b=0$, the whole result reduces to the exact constant-coefficient Fourier inverse. No case is obtained by dividing by a vanishing mean.

## 3. The constant mean has a contractive exact inverse

Let
$$
 T_\nu=1+\nu I .
$$
Its nonmean Fourier inverse multiplier is
$$
 \frac{i4j}{i4j+\nu},
$$
and its mean multiplier is one. Consequently,
$$
                  \|T_\nu^{-1}:H^s\to H^s\|\le1
 \tag{MI.12}
$$
for real $\nu$ and every $s$.

Using $Ih=v$ in (MI.11), the exact alternative formula is
$$
             h=T_\nu^{-1}\{f-bv(f)\}.
 \tag{MI.13}
$$
This is the order used for the following bounds. Estimating $f-cv$ directly would introduce an unnecessary factor $|\nu|$; (MI.13) proves why it is absent. It does not commute $T_\nu^{-1}$ with the variable multiplier $b$.

## 4. A complete L2 inverse bound from low-order data

Let $P_0\ge\|p\|_\infty$ and $V_0\ge\|b\|_\infty$, and set $M_0=e^{P_0}$.
The first row of (MI.8) has the positive probability density
$$
 k_\nu=\frac{a\,J_\nu^*(a^{-1})}{d_\nu},\qquad
 m(f)=\langle k_\nu f\rangle,\qquad
 k_\nu\ge0,\quad\langle k_\nu\rangle=1.
 \tag{MI.14}
$$
Equations (MI.5)--(MI.7) give $k_\nu\le M_0^2$. Therefore
$$
             \|k_\nu\|_2^2\le M_0^2\langle k_\nu\rangle=M_0^2,
 \qquad |m(f)|\le M_0\|f\|_2 .
 \tag{MI.15}
$$
This uses positivity of the complete row, not the sign of the input.

Successively applying (MI.4), $\|a^{\pm1}\|_\infty\le M_0$, and
$\langle a^{-1}\rangle\ge1$ gives
$$
 \begin{split}
 \|u(f)\|_2&\le\frac14M_0(1+M_0)\|f\|_2,\\
 |\kappa(f)|&\le M_0\|u(f)\|_2,\\
 \|v(f)\|_2&\le Z(P_0)\|f\|_2,\qquad
 Z(P)=\frac14e^{2P}(1+e^P)^2 .
 \end{split}\tag{MI.16}
$$
Thus the complete principal inverse satisfies
$$
 \boxed{\quad
 \|(1+M_cI)^{-1}:L^2\to L^2\|
       \le K_0:=1+V_0Z(P_0).
 \quad}\tag{MI.17}
$$
The right side is uniform in every real $\nu$, including zero. It is exactly one when $b=0$.

If the actual complete bound also has $V_0<4$, then the ordered factorization
$$
 1+M_cI=T_\nu[1+T_\nu^{-1}M_bI]
$$
gives the additional complete bound $(1-V_0/4)^{-1}$.
The smaller of this whole bound and (MI.17) may be used. Failure of the strict Neumann gate does not invalidate the explicit inverse (MI.8).

## 5. The same inverse on the negative window

For $\alpha=4/3$ define the complete weighted Wiener norm
$$
 W_\alpha(f)=\sum_{j\in\mathbb Z}(1+|4j|)^\alpha|\widehat f_j|.
 \tag{MI.18}
$$
Its convolution weight is submultiplicative. Moreover, for $|s|\le\alpha$,
$$
 \|M_f:H^s\to H^s\|\le W_\alpha(f).
$$
This follows directly from
$\Lambda_m/\Lambda_n\le1+|4(m-n)|$, including the negative-weight case.

Let $P_\alpha\ge W_\alpha(p)$,
$B_\alpha\ge W_\alpha(b)$, and $M_\alpha=e^{P_\alpha}$.
The complete exponential series gives
$W_\alpha(a),W_\alpha(a^{-1})\le M_\alpha$.
For every $s\in[-4/3,0]$, the scalar mean row in (MI.8) obeys
$$
 |m(f)|\le M_\alpha^2\|f\|_{H^s}.
 \tag{MI.19}
$$
Indeed multiplication by $a$, the same-space contraction $J_\nu$, and the dual row $a^{-1}$ cost respectively $M_\alpha$, one, and $M_\alpha$; the denominator is at least one.

Using the same-space norm $1/4$ of $I_\nu$ and the full dual row for $\kappa$ gives
$$
 \begin{split}
 \|u(f)\|_{H^s}
      &\le\frac14M_\alpha(1+M_\alpha^2)\|f\|_{H^s},\\
 |\kappa(f)|&\le M_\alpha\|u(f)\|_{H^s},\\
 \|v(f)\|_{H^s}
      &\le V_\alpha\|f\|_{H^s},\qquad
 V_\alpha=\frac14M_\alpha^2(1+M_\alpha)(1+M_\alpha^2).
 \end{split}\tag{MI.20}
$$
In particular the same distributional inverse, rather than a second choice of inverse, satisfies
$$
 \boxed{\quad
 \|(1+M_cI)^{-1}:H^{-4/3}\to H^{-4/3}\|
       \le K_-:=1+B_\alpha V_\alpha .
 \quad}\tag{MI.21}
$$
The same formula holds throughout the displayed interval of $s$.
If $B_\alpha<4$, its whole-bound minimum with
$(1-B_\alpha/4)^{-1}$ is valid. Neither estimate contains $|\nu|$.

For verification of the differential identities on distributions one may first use smooth inputs, then apply density and these same-space estimates. Alternatively, (MI.4) also gives $u,v\in H^{s+1}$; all required multiplication windows satisfy $|s+1|\le4/3$ here. The equations and both mean identities therefore survive the limit.

These are only the stated base windows. No unproved all-Sobolev tame family is added.

## 6. Application to the actual individual incoming first coefficient

Use the published [individual branch identification IC.18--IC.29](R133-supplement-individual-branch-first-coefficients-and-common-root-normalization.md), in its exact common true phase chart and common root normalization:
$$
 c_i=-\frac{\mu}{2}+v_i,\qquad
 \langle v_i\rangle=0,\qquad
 v_i=U_{H^{-1}}q_+ .
 \tag{MI.22}
$$
Here $\mu$ is the actual selected return first mean. In (MI.2) take
$\nu=-\mu/2$, $b=v_i$. Do not replace $q_+$ by $c_i$ or change the order of the true density pullback.

The complete future SN positive-branch derivative columns, the complete finite-angle error and the actual inverse-density matrix of IC give the full norms of $v_i$. The [lower-order budgets LN](R133-supplement-lower-order-normalizer-budgets-from-complete-terminal-columns.md) or direct signed Fourier estimates may then pay $V_0,P_0,B_\alpha,P_\alpha$ separately. An $H^3$ upper bound is not divided by powers of frequency to invent its lower derivative components.

The proof gives an exact inverse for the entire principal factor
$$
                         T_i=1+M_{c_i}I.
 \tag{MI.23}
$$
It is not the inverse of the complete physical incoming operator.
All finite root gauges and primitive-conjugation ranks from IC, the original free first-neglected term, the genuine Darboux comparison, positive correction, true coordinate changes and stable normalization must still be included in the actual remainder.

The auxiliary full-circle mean in (MI.23) is retained by (MI.8)--(MI.11).
If the physical formulation adjoins two separate mean coordinates, extend $T_i$ by their identity blocks and preserve every rank difference between that convention and the full-density convention. An independent physical mean is not identified with the auxiliary zero mode merely to remove a row.

## 7. A precise high-block consequence after complete preconditioning

Suppose, in this same chart, the fully qualified incoming map really has
$$
                  \mathcal B_i=T_i+E_i,\qquad
 E_i:H^{-4/3}\longrightarrow L^2,\quad \|E_i\|\le C_i.
 \tag{MI.24}
$$
Every finite-rank term included in $E_i$ must have its complete $H^{4/3}$ dual-row fee. If one has not established (MI.24), the following remains a conditional interface.

Let $P_J$ be the actual Fourier projection $|j|\ge J$ in this declared chart and $Q_J=1-P_J$, keeping any adjoined physical means in $Q_J$.
Premultiply the complete map, without commuting any projection:
$$
 \widehat{\mathcal B}_i=T_i^{-1}\mathcal B_i=1+T_i^{-1}E_i,\qquad
 D_J=P_J\widehat{\mathcal B}_iP_J .
 \tag{MI.25}
$$
The complete strong norm of $T_i^{-1}E_i$ is at most $K_0C_i$.
Consequently on both $L^2$ and $H^{-4/3}$,
$$
 \|P_JT_i^{-1}E_iP_J\|
       \le\chi_J:=K_0C_i\Lambda_J^{-4/3}.
 \tag{MI.26}
$$
On $L^2$ this is the high-input embedding; on $H^{-4/3}$ it is the high-output embedding after the full $L^2$ principal inverse. Thus this particular high-block smallness uses $K_0$ in both cases, not an incorrectly exchanged input/output norm.

If $\chi_J<1$, one common ordered Neumann inverse gives
$$
 \|D_J^{-1}\|_{L^2\to L^2},\
 \|D_J^{-1}\|_{H^{-4/3}\to H^{-4/3}}
                        \le(1-\chi_J)^{-1}.
 \tag{MI.27}
$$
The inverse on a general right source still consumes
$P_JT_i^{-1}f$ and hence the appropriate full $K_0$ or $K_-$ source bound. The preconditioned output projector is not the old physical high-output projector.

The finite Schur block is exactly
$$
 Q_J\widehat{\mathcal B}_iQ_J
 -Q_J\widehat{\mathcal B}_iP_JD_J^{-1}
                P_J\widehat{\mathcal B}_iQ_J .
 \tag{MI.28}
$$
It and every independent physical matching row remain to be proved invertible.
Premultiplication changes finite output functionals; they must be read in this order, with their full dual-window norms. Old physical finite Green rows cannot be reused as unchanged rows of (MI.28).

This supplies a concrete alternative to spending the nonmean first coefficient as an additional $J^{-1}$ perturbation: the complete real principal factor is solved first. It supplies neither an actual $C_i$ nor a finite Schur inverse, and it is not a substitute for the separate strong-return arithmetic or the nonlinear core construction.
