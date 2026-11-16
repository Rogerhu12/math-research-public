# R133 supplement: ordered genuine root input powers and the complete mean row

2026-11-16, visible-exact / phase_inverse.

**Proved exact input-frequency identities and a conditional scalar recipe. No new numerical evaluation.** The complete genuine root products of RBG admit an exact separation in powers of the original input frequency. The frequency-dependent third ordinary derivative occurs only in a term with input power $N^{-10/3}$. The constant part of the potential derivative remains in the main multiplier. The original positive projection-generated mean rank and every low intermediate frequency are retained.

## RBO1. Same family, operators and immutable inputs

Use the same repaired real family, original intrinsic parameter and $|\delta|\le10^{-8}$ root domain as RD1 and RBG1. All coefficient functions, means, radial derivatives, reference solutions and inverse bounds must cover this same family. Any additional interval denoted by $\nu$ must be explicitly covered by every input used on that interval; a fixed-$\nu$ enclosure does not become a uniform $\nu$ enclosure. Intrinsic coefficients retain their actual stipulated parameter dependence.

Ordinary $r$ derivatives are taken at fixed physical parameters and fixed frequency parameter before restriction to the same true root $r_*$. A complex family may enclose these quantities, with its original bilinear Fourier products. The positive-diagonal and coercivity statements below apply to real parameters only.

| Primary | Complete Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [RBG, complete genuine cancellation and RD substitution](R133-supplement-exact-genuine-root-b-jets-with-common-radial-cancellation.md) | 6fcf438b00220d8823f86dd619aaf32659b597c8 | 22284 | 157795fdc7fc415156229f5c0b9674b18f92cce1e8cef8ce8df65a271775f268 |
| [RD, full projected root products and stable gate](R133-supplement-exact-leading-root-derivative-and-complete-stable-trace-gate.md) | 24b3523585bdfe9f1d96b57e3ca2e4f0727fd2d4 | 17725 | 34eec24f901205c6e8002aa767484fed4832f590fbbfbb89b3a9f2ece218b81f |
| [C, exact rational-frequency reference](R133-supplement-common-radial-Langer-reference-and-complete-source-ports.md) | 5fe6c61c14db1bcc560f5361eceb13e59cae1a8c | 15993 | 8d4119cbd42577fc1ab498350f4a8fd77b2923f7e207db4c4519f7a345225392 |
| A, genuine terminal-normalized reference and rational Airy bounds | 62909c54de321da071a6bbc6e169e87b5888dde6 | 15528 | 0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49 |
| [RDA, complete signed first-amplitude derivative](R133-supplement-exact-root-first-Airy-amplitude-derivative.md) | 5a7b91eea967053bb1e68e0cc60a41fd5183cd69 | 11486 | 8d2570c7b28304001c785e7b7a6d4261cf127909dd59d594262fd22d42caa205 |

Let $P=1-\Pi$, $I=\partial_\phi^{-1}P$, and $P_H=P_{|j|\ge97}$. The circle has period $\pi/2$ and normalized measure. On the original high input set
$$
 N e_j=4|j|e_j,\qquad N_*=388,\qquad
 z=j^{-2}=16N^{-2},\qquad \xi=N^{-1/3}.
 \tag{RBO.1}
$$
Thus $z=16\xi^6$. The symbol $z$ always denotes the exact rational-frequency parameter, not $\xi$. A function $f(z)$ gives the input diagonal $D_f e_j=f(j^{-2})e_j$. Such diagonals commute with each other and with $N$; they are not commuted through physical multiplication or the full inverse $J$.

All operator identities below are maps on $P_HL^2$, with the original reflection restriction when imposed. Rightmost $P_H$ is implicit where an expression is already defined on that space. No physical mean coordinate is assigned an inverse power of $N$.

## RBO2. The exact constant and the remaining rational terms

Retain RBG.29:
$$
 \alpha(z)=\frac{\beta}{i}
       \sum_{\ell=1}^{M}\frac{\ell}{1-\ell^2z}u_\ell v_{-\ell},
 \qquad M\le96 .
$$
The identity $1/(1-\ell^2z)=1+\ell^2z/(1-\ell^2z)$ gives
$$
 \alpha(z)=\alpha_0+z\alpha_1(z),\qquad
 \alpha_0=\frac{\beta}{i}\sum_{\ell=1}^{M}\ell u_\ell v_{-\ell},
 \qquad
 \alpha_1(z)=\frac{\beta}{i}
       \sum_{\ell=1}^{M}\frac{\ell^3}{1-\ell^2z}u_\ell v_{-\ell}.
 \tag{RBO.2}
$$
This is an exact removable factorization, including $z=0$.

Use the complete $\mathfrak q,Q_1,\bar t,\eta_*,\lambda,k_1$ of RBG.2, RBG.6 and RBG.29--34. All expressions in the following display are restricted to the root after the displayed ordinary derivatives:
$$
 \begin{split}
 q_\Delta(z)&=\frac12(Q_1)_r-\frac12\mathfrak q Q_1
                                      -\frac z4 Q_1^2,\\
 \mathfrak c_0(z)&=\lambda^{-2}q_\Delta(z),\\
 d_{10}&=-32k_1\eta_*\alpha_0/\lambda^2,\\
 \mathfrak c_1(z)&=\lambda^{-2}\left[
 \frac12(Q_1)_{rr}
 -\frac12\{\mathfrak q_rQ_1+\mathfrak q(Q_1)_r\}
 -\frac z2Q_1(Q_1)_r-4\bar t q_\Delta(z)\right.\\
 &\hspace{35mm}\left.
       -32k_1\eta_*\alpha_1(z)-16k_1\alpha(z)^2\right].
 \end{split}
 \tag{RBO.3}
$$
Substitution into RBG.31--33 proves
$$
 \boxed{\Delta_0(z)=z\mathfrak c_0(z),\qquad
        \Delta_1(z)=d_{10}+z\mathfrak c_1(z),\qquad
        V_j(0)=V_r+z\mathfrak c_0(z).}
 \tag{RBO.4}
$$
Here $V_r=V_{\rm rad}(0)$ is the complete radial potential value of RBG.22. In particular $d_{10}$ is generally nonzero. It is not charged as a term with an extra $N^{-2}$ factor.

The functions in (RBO.3) remain full rational functions of $z$. There is no Taylor truncation in $z$, and no free-amplitude or potential upper bound is subtracted from another upper bound.

## RBO3. Exact ordered root products

Write
$$
 a_*=A_0-b_{\rm op},\qquad
 h_0={\cal E}_1-b_{\rm op}{\cal E}_0+d_{10}/3 .
$$
RBG.35--38 and (RBO.4) give
$$
 \begin{split}
 {\mathsf B}^V&=M_{{\cal E}_0}P_H
                 +16D_{\mathfrak c_0}N^{-2}P_H,\\
 {\cal H}:={\mathsf B}^V_r-M_{b_{\rm op}}{\mathsf B}^V
     &=M_{h_0}P_H
        +16\left(M_{a_*}D_{\mathfrak c_0}
                         +\tfrac13D_{\mathfrak c_1}\right)N^{-2}P_H,\\
 D_V&=V_r\,{\rm Id}+16D_{\mathfrak c_0}N^{-2}
                     \quad\hbox{on }P_HL^2 .
 \end{split}
 \tag{RBO.5}
$$
Only the scalar $V_r$, which is independent of angle and input label, is moved through multiplication. In particular
$$
 {\mathsf B}^VD_V=
 V_rM_{{\cal E}_0}P_H
 +16(M_{{\cal E}_0}+V_r{\rm Id})
                         D_{\mathfrak c_0}N^{-2}P_H
 +256D_{\mathfrak c_0}^2N^{-4}P_H .
 \tag{RBO.6}
$$

Retain the genuine input diagonals $D_A,D_D$ from RD.11, including the original nonzero $\beta_n$, and the complete signed $\mathsf A_r$ of RDA.21. The entire RBG.39 operators are exactly
$$
 \boxed{E_2=
 P M_{{\cal E}_0}D_DN^{-4/3}
       +16P D_{\mathfrak c_0}D_DN^{-10/3}.}
 \tag{RBO.7}
$$
$$
 \boxed{\begin{aligned}
 R_0={}&P M_{a_*}D_A+P{\mathsf A}_rD_AN^{-1}
          +P M_{h_0}D_DN^{-4/3}\\
 &+16P\left(M_{a_*}D_{\mathfrak c_0}
                   +\tfrac13D_{\mathfrak c_1}\right)D_DN^{-10/3}\\
 &-\lambda V_r P M_{{\cal E}_0}D_AN^{-2}\\
 &-16\lambda P(M_{{\cal E}_0}+V_r{\rm Id})
                                  D_{\mathfrak c_0}D_AN^{-4}\\
 &-256\lambda P D_{\mathfrak c_0}^2D_AN^{-6}\\
 &+P M_{b_{\rm op}}\Pi M_{{\cal E}_0}D_DN^{-4/3}.
 \end{aligned}}
 \tag{RBO.8}
$$
The last positive rank term is retained. Its rational-diagonal subterm vanishes for the precise reason
$$
 \Pi D_{\mathfrak c_0}D_DN^{-10/3}P_H=0 .
 \tag{RBO.9}
$$
Every factor between $\Pi$ and $P_H$ in (RBO.9) is an input diagonal, so it preserves the nonzero high modes. This does not imply
$\Pi M_{{\cal E}_0}D_DN^{-4/3}P_H=0$.
The latter complete row, its multiplication by $b_{\rm op}$, the independent two physical means and the original supplied-head/source ports all remain.

For bookkeeping only, the powers in (RBO.7) are $\xi^4,\xi^{10}$. The successive lines of (RBO.8) contain $\xi^0,\xi^3,\xi^4;\xi^{10};\xi^6;\xi^{12};\xi^{18};\xi^4$. Their coefficients still depend on the exact $z=16\xi^6$. This is a finite exact operator expression, not an asymptotic expansion.

## RBO4. Complete prospective scalar bounds and the original stable gate

Suppose complete common-domain bounds are available:
$$
 \begin{gathered}
 \|{\cal E}_0\|_\infty\le E,\quad
 \|h_0\|_\infty\le H,\quad \|a_*\|_\infty\le A,\quad
 \|\mathsf A_r\|_{L^2\to L^2}\le A_1,\quad
 \|b_{\rm op}\|_\infty\le b,\\
 \sup_{0\le z\le97^{-2}}|\mathfrak c_0(z)|\le C_0,\quad
 \sup_{0\le z\le97^{-2}}|\mathfrak c_1(z)|\le C_1,\quad
 |V_r|\le V,\quad \lambda\le\lambda_+,\\
 \sup_n|A_n|\le A_*,\qquad \sup_n|D_n|\le D_* .
 \end{gathered}
 \tag{RBO.10}
$$
All suprema also run over the stated real parameter family. $H$ may be bounded as the correlated complete expression defining $h_0$; separate triangle bounds are permitted but not required. The two physical frequency signs share the same b coefficients and do not require an extra factor of two.

A complete unprojected amplitude bound and a projected bound are
$$
 e_{\rm amp}=D_*(E N_*^{-4/3}+16C_0N_*^{-10/3}),
 \qquad e_2\le e_{\rm amp}.
 \tag{RBO.11}
$$
A complete $R_0$ bound is
$$
 \begin{aligned}
 r_0={}&AA_*+A_1A_*N_*^{-1}+HD_*N_*^{-4/3}\\
 &+16(AC_0+C_1/3)D_*N_*^{-10/3}\\
 &+\lambda_+VEA_*N_*^{-2}
   +16\lambda_+(E+V)C_0A_*N_*^{-4}
   +256\lambda_+C_0^2A_*N_*^{-6}\\
 &+bED_*N_*^{-4/3}.
 \end{aligned}
 \tag{RBO.12}
$$
The last line uses the unprojected multiplier ${\cal E}_0$. Its absence of $C_0$ follows from the exact zero (RBO.9), not from replacing an unprojected norm by a smaller projected one.

Keep RD's full $J,L$, its original parity domains and complete same-domain constants $J_1,L_0,\eta_-$. The stable error is still bounded by
$$
 e=e_2+\frac{N_*^{-2/3}}{\eta_-}
 \left[r_0+J_1L_0
       \left(\lambda_+D_*N_*^{-1/3}+\frac{r_0}{4}\right)\right].
 \tag{RBO.13}
$$
In particular $\|IR_0\|\le r_0/4$: the physical multipliers in (RBO.8) can create low nonzero outputs from high input. The input powers displayed there do not move through $I,J,L$ or become output powers. No new band assumption about these inverse operators is used.

There is no need to discard the Airy derivative term from RD.13. For the same real terminal-normalized reference, suppose the original uniform nonzero-shear bound $|\beta_n|<1/19$ holds for every $|j|\ge97$ and every declared parameter. Then
$$
 \begin{aligned}
 g_n&=A_n-\frac{\lambda}{\eta_*}D_n\\
 &=\operatorname{Ai}(0)(1+\sqrt3\,\beta_n)
       +\frac{\lambda}{\eta_*}|\operatorname{Ai}'(0)|
                                      (1-\sqrt3\,\beta_n)\\
 &>\frac{17}{19}
       \left(\operatorname{Ai}(0)
          +\frac{\lambda}{\eta_*}|\operatorname{Ai}'(0)|\right).
 \end{aligned}
 \tag{RBO.14}
$$
Thus actual common-domain lower and upper inputs give the usable lower certificate
$$
 g_-=\frac{17}{19}
       \left(A_{\rm Ai,-}
          +\frac{\lambda_-}{\eta_+}D_{\rm Ai,-}\right)
       \le\inf_{|j|\ge97}g_n ,
 \tag{RBO.15}
$$
where $A_{\rm Ai,-}\le\operatorname{Ai}(0)$,
$D_{\rm Ai,-}\le|\operatorname{Ai}'(0)|$, and
$0<\lambda_-\le\lambda,\ \eta_*\le\eta_+$.
The entire expression is evaluated downward for a numerical lower certificate. Its Airy normalization and $\beta_n$ domain are those of RD4; a fixed-parameter shear estimate cannot authorize a larger family. This formula retains the true nonzero shear and supplies no actual value in this note.

A.4--5 and the original P.20 bounds also give a fully rational choice without a new Airy or gamma evaluation:
$$
 \frac13<\operatorname{Ai}(0)<\frac59,\qquad
 \frac4{21}<|\operatorname{Ai}'(0)|<\frac13 .
 \tag{RBO.15a}
$$
Indeed $|\operatorname{Ai}'(0)|=[3^{1/3}\Gamma(1/3)]^{-1}$,
$\Gamma(1/3)<7/2$ and $3^{1/3}<3/2$ give its lower bound. The value formula
$\operatorname{Ai}(0)=[3^{2/3}\Gamma(2/3)]^{-1}$, with
$\Gamma(2/3)>9/10$ and $3^{2/3}>2$, gives its upper bound. The lower bound $1/4$ for the ratio $-\operatorname{Ai}'(0)/\operatorname{Ai}(0)$ in A.5 is not a lower bound for $|\operatorname{Ai}'(0)|$.

Together with $\sqrt3<2$ and the same $|\beta_n|<1/19$, complete permissible inputs are
$$
 A_*=\frac{35}{57},\qquad D_*=\frac7{19},\qquad
 g_-=\frac{17}{19}
       \left(\frac13+\frac{4\lambda_-}{21\eta_+}\right).
 \tag{RBO.15b}
$$
Here A.20 already proves the shear inequality for the exact common potential on its original complex parameter square
$|\Re\delta|,|\Im\delta|\le10^{-8}$, using the successful potential input of run 43685624307/1. Only the real subfamily is used for (RBO.14)--(RBO.15b). These are analytic consequences of those original complete bounds, not newly stored per-frequency values of $\beta_n$.

Only a proved strict $e<g_-$ closes RD's stable-trace gate. Same-domain complete alternatives for $e_2,r_0$ or $e$ may be compared as whole valid bounds. A failed sufficient inequality would not prove a kernel or failure of the actual incoming map.

## RBO5. Finite rational sums from original Wiener derivative bounds

These sums can be enclosed without recomputing a reference solution or potential. For an actual finite scalar Fourier function $f$, define
$$
 {\cal A}_s(f)=\sum_{k\in\mathbb Z}(4|k|)^s|f_k|,
 \qquad {\cal A}_0(f)=\sum_{k\in\mathbb Z}|f_k|.
$$
For integer $s\ge0$, each available choice $a+b=s$ gives
$$
 \sum_{\ell=1}^{M}\ell^s|f_\ell g_{-\ell}|
 \le4^{-s}{\cal A}_a(f){\cal A}_b(g).
 \tag{RBO.16}
$$
The product contains the diagonal sum as a subset of nonnegative terms. One may take the minimum of complete available right sides for the same pair, including $M^s{\cal A}_0(f){\cal A}_0(g)$. Denote such a valid complete bound by ${\cal W}_s(f,g)$. Missing angular jets can instead be bounded by the actual finite-band identity
${\cal A}_s(f)\le(4M)^s{\cal A}_0(f)$; a pointwise sup is not silently treated as a Wiener norm.

The genuine denominator is
$$
 |1-\ell^2z|\ge d_M:=1-M^2/97^2
                  \ge1-96^2/97^2>0
       \quad (|z|\le97^{-2}).
 \tag{RBO.17}
$$
At fixed $z$, complete ordinary derivatives obey
$$
 \begin{split}
 |\partial_r^m U(z)|
   &\le\frac{2}{d_M}\sum_{a=0}^{m}\binom ma
       {\cal W}_2(\partial_r^a u,\partial_r^{m-a}u),\\
 |\partial_r^m W(z)|
   &\le\frac{2}{d_M}\sum_{a=0}^{m}\binom ma
       {\cal W}_2(\partial_r^a v,\partial_r^{m-a}v),\\
 |\partial_r^m\alpha(z)|
   &\le\frac{1}{d_M}
       \sum_{a+b+c=m}\frac{m!}{a!b!c!}
       |\beta^{(a)}|
          {\cal W}_1(\partial_r^b u,\partial_r^c v),\\
 |\alpha_1(z)|&\le\frac{|\beta|}{d_M}{\cal W}_3(u,v).
 \end{split}
 \tag{RBO.18}
$$
The bound for $\alpha_0$ uses the same last degree-one pairing with denominator one. These are bilinear formulas also on a complex enclosing family; conjugacy is not required to justify the absolute bounds.

The quotient $h=\alpha/\eta$ retains its full Leibniz derivatives through order three. The separate gap for $1+zh$ in RBG.29--34 must also hold on the claimed domain. The positive number $d_M$ does not pay that second gap. Original complete Fourier/jet bounds can be read directly; finite algebraic combinations and any missing quotient gap are new obligations if not already saved.

## RBO6. A finite derivative inventory, with third derivatives isolated

The common nonradial coefficients ${\cal E}_0,{\cal E}_1,h_0,V_r$ use the exact RBG formulas. Their input orders can be checked without taking a derivative of a root-only identity. For the original $S=u^2+Kv^2$, differentiation in the neighborhood followed by $K=0$ gives
$$
 \begin{split}
 S_*&=u^2,\\
 (S_r)_*&=2uu_r+k_1v^2,\\
 (S_{rr})_*&=2u_r^2+2uu_{rr}+k_2v^2+4k_1vv_r,\\
 S_\phi|_*&=2uu_\phi,\qquad
 S_{\phi\phi}|_*=2u_\phi^2+2uu_{\phi\phi},\\
 S_{r\phi}|_*&=2u_ru_\phi+2uu_{r\phi}+2k_1vv_\phi.
 \end{split}
 \tag{RBO.19}
$$
Since $d=-\beta I S$, its ordinary derivatives are
$$
 d_r=-\beta_r I S-\beta I S_r,\qquad
 d_{rr}=-\beta_{rr}I S-2\beta_r I S_r-\beta I S_{rr}.
 \tag{RBO.20}
$$
Every subtracted mean in $I$ or $P$ remains. In particular $D$ is not interchanged with $P$. Together with the complete means in RBG.21, these identities give the following sufficient inventory.

| Target | Ordinary intrinsic data | State data beyond its complete value |
|---|---|---|
| ${\cal E}_0,{\cal E}_1,h_0,V_r,a_*,\mathsf A_r$ | $K_r,K_{rr},K_{rrr}$; $\beta,\beta_r,\beta_{rr}$; $\eta,\eta_r,\eta_{rr}$, with all required complete means | $u_\phi,u_{\phi\phi},u_r,u_{r\phi},u_{rr}$; $v_\phi,v_r$; the complete mean $\langle v_{rr}\rangle$ if used to form $\eta_{rr}$ |
| $\mathfrak c_0$ | $\beta,\eta$ through order two; $K_r$; the complete radial means in $\mathfrak q$ | complete Fourier coefficients or certified Wiener bounds for $u,v$ through ordinary radial order two, with the finite weighted pairings in (RBO.18) |
| $\mathfrak c_1$ | $\beta,\eta$ through order three; $K_r,K_{rr}$; $\mathfrak q_r,\bar t$ | complete Fourier coefficients or certified Wiener bounds for $u,v$ through ordinary radial order three, and the value pairing for $\alpha_1$ |

The first row includes all zeroth state modes, not just the nonmean part of $v$. The same complete $\eta=-\gamma\langle v\rangle$ is differentiated by its full product rule; no missing mean derivative is set to zero. Where the physical background contains its true radial scalar $s_{\nu_0}$, its true ordinary derivatives remain. Piecewise constant canonical repairs have zero positive-order radial derivative only inside the same genuine piece; this does not authorize omitting derivatives of $s_{\nu_0}$ or crossing a piece interface.

In the new rational recipe, the third derivative enters through
$$
 (Q_1)_{rr}\supset\frac{h_{rrr}}{1+zh}.
$$
All its terms, including the derivatives of $\beta$, the full $\eta_{rrr}$, and the two reference functions, are retained. They occur only in $\mathfrak c_1$, hence only in the $16D_{\mathfrak c_1}D_DN^{-10/3}/3$ contribution in (RBO.8). Neither $K_{rrrr}$ nor a free $D^3a_0$ bound is needed in this new factorization. This does not alter the original requirements of any already successful reference/profile producer.

## RBO7. Numerical use and retained obligations

A new consumer must first bind all successful original inputs, their precise $\nu/\delta$ scopes, the true root interval and single analytic germ, actual positive gaps, original Airy terminal normalization, and complete means. It then reads saved bounds or evaluates only the newly specified finite combinations. It does not rerun old fold, potential, amplitude, inverse, or source producers, and it does not evaluate a cancellation by subtracting unrelated positive upper bounds.

A scalar receipt should retain $d_{10},C_0,C_1,E,H,V,A,A_1$, the exact domain and both rational denominator qualifications, each complete summand of (RBO.11)--(RBO.13), and the full lower construction (RBO.15). Its source/target are RD's ordinary $L^2$ root operator and actual stable trace. No negative-window norm, incoming inverse, finite Schur inverse, supplied-head solution, coupled mean solution or nonlinear result is granted by this pure identity.

All original finite/low rows, cross maps, true nonzero $\beta_n$, independent physical means and source ports remain in their original order.
