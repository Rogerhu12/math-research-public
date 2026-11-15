# R133 supplement: shifted Sobolev control of the complete gauge Hessian and cap--tail Schur

2026-11-15, visible-exact-astra-0df9.

**Proved at the same fixed repaired centre.** This note upgrades the complete normalized-gauge residual bridge to every angular Sobolev exponent $-3/2\le s\le1024$. It retains both curvature means, the true long-output $B_0$ column, every physical cap port, and all Fourier modes. The argument first uses a Fourier weight with a large fixed scale; it then pays the finite conversion back to the usual Sobolev norm.

The centre definition is $440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47$, at the actual fixed $\eta_0,\delta=0$. The equation treated here is exactly $F_{\rm cov}=F-AQ_\phi$ of [the complete angle-gauge theorem](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md), (G.10)--(G.22). For the original moving forced equation its scalar phase row, residual source $aR_{0,\phi}$, and true endpoint phase remain separate explicit data. They are not discarded below.

## 1. Physical modules and the two complete Green operators

Physical frequencies are $k\in4\mathbb Z$, including $k=0$. All circular measures are normalized. On the unchanged cap $I=[9/10,25/8]$ put
$$
 \|x\|_{\mathfrak M_s}
 =\left(\sum_k\langle k\rangle^{2s}
                     \sup_{r\in I}|x_{B,k}(r)|^2\right)^{1/2}
 +\left(\sum_k\langle k\rangle^{2s}
                     \sup_{r\in I}|x_{C,k}(r)|^2\right)^{1/2}.
 \tag{S.1}
$$
The supremum also retains any prescribed one-sided traces. Ordinary sources use $L^2_rH^s_\theta$, angular-divergence source potentials use $\mathfrak M_s$, and independent physical jumps use their original sum of $H^s$ norms. No radial derivative is part of (S.1).

Let $G_*$ be the already completed repaired physical cap inverse with its full Robin and $C_0$ graph, but with its outer $B_0$ prescribed independently. The [all-mode cap theorem](R133-supplement-actual-final-all-mode-physical-cap-Green.md), (C.24)--(C.28), and [continuous repair theorem](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md), (C.8)--(C.10), give an outer-$B_0$ lift $P_b$ of norm less than $8$.

The actual additional long graph is the scalar row
$b_0=D_Zb_0\,Z+D_fb_0\,f_B+b_0^{\rm aff}$.
The [full fourfold cap--long graph](R133-supplement-complete-fourfold-periodic-cap-long-graph-with-true-B-mean.md), (B.9)--(B.18), gives $\|D_Zb_0\|<2^{-49}$ at this background in the complete Hilbert module. Thus, with $E_Rx=(x_C(R))_\perp$,
$$
 K_b=P_bD_Zb_0E_R,\qquad
 \|K_b\|_{\mathfrak M_0\to\mathfrak M_0}<2^{-46},\qquad
             G=(I-K_b)^{-1}G_* .
 \tag{S.2}
$$
The affine $B_0$ charge and $D_fb_0$ column are retained in their corresponding right sides. In particular (S.2) does not set the true curvature mean to zero.

Write $H_Rx=D^2\Psi[R_0,D\Psi^{-1}x]$ with the full weighted-mean normalization of (G.4)--(G.8), and $K=GH_R$. The already proved complete unknown-input bound (G.26) therefore gives
$$
 \|G_*H_R\|_{\mathfrak M_0}<1/128,\qquad
                  \|K\|_{\mathfrak M_0}<1/64 .
 \tag{S.3}
$$
This is the only smallness estimate used. It applies to arbitrary full $4\mathbb Z$ directions.

## 2. A uniformly bounded complex angular family

Let $C_zf(\theta)=f(\theta+z)$ initially on finite Fourier polynomials and set $\sigma=1/128$. Translate every physical coefficient and every true boundary functional by the same $z$. The [physical cap--tail theorem](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md), (L.3)--(L.8), proves on $|\operatorname{Im}z|\le\sigma$
$$
 \chi_z<.9,\qquad
 \|G_{o,z}:L^2_rL^2_\theta\to\mathfrak M_0\|<2^{10},\qquad
 \|G_{d,z}:\mathfrak M_0\to\mathfrak M_0\|<2^{10}.
 \tag{S.4}
$$
Here the constants have merely been widened from the original ordinary and divergence gains and the resolvent less than $10$. This family includes the genuine $B_0$ row and both other exterior derivative rows. The repair is covered by (C.8)--(C.9) of the continuous repaired cap and Section 9 of the physical cap--tail theorem. No assertion about arbitrary unknown analytic directions is required: the translated objects are coefficients of a bounded operator on the unweighted module.

The inverse-angle coefficients are analytic in the joint coefficientwise-radial-supremum algebra. At width $1/64$ their paid bounds imply
$$
 |m|<8,\quad \|u\|<1,\quad \|v\|<8,\quad
 \|B\|,\|C\|,\|W_\theta\|<1,\quad
 \|\Phi-\mathrm{id}\|<1/256,\quad \|\Phi_\theta\|<2 .
 \tag{S.5}
$$
The signed functions remain signed; the inequalities are absolute coefficient bounds.

A deliberately coarse bound for the complete physical residual is sufficient here. On each original residual cell let $r_{U,0},r_{V,0}$ be the exact repaired moving $A^0$ bounds of the [local triangular Hessian theorem](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md), (L.7)--(L.10).
Its actual coefficients satisfy $E_1<1.470644\,10^{-7}$ and $Z_{BC}<2.835041\,10^{-5}$.
The already paid $|v|<6$ and $|m|>3$ imply that its constants may only be upper bounds with $C_*>1/6$, $V_*>3$ and $H_2>9$. Consequently
$$
 r_{V,0}<3E_1<1/2,\qquad
 r_{U,0}<4Z_{BC}<1/2.
 \tag{S.6}
$$
Indeed $E_1=2C_*r_{V,0}$ and
$Z_{BC}\ge C_*^2H_2r_{U,0}>r_{U,0}/4$.
This inference uses the existing complete source inequalities, not a new residual evaluation.

The repaired moving residual has exact degree at most $96$, hence at most $193$ coefficients and physical frequency at most $384$. Taking each coefficient's radial supremum costs at most $193$. Composing with the same actual $\Phi$ at width $\sigma$ costs at most
$e^{384(\sigma+1/256)}<e^5<3^5<2^8$.
Thus, for $\widehat R=R_0\circ\Phi$,
$$
       \|\widehat R\|_{\mathscr A_\sigma,\rm pair}<2^{16},
 \qquad
       \|\widehat R_\theta\|_{\mathscr A_\sigma,\rm pair}<2^{26}.
 \tag{S.7}
$$
The second bound uses the exact factor $384$ before composition and $\|\Phi_\theta\|<2$. The finite degree is a property only of these coefficients. The composed residual and every unknown retain their complete infinite Fourier support.

## 3. Complete analytic Hessian budget, including its rank-one means

All formulas in this section are in the same physical angle. Put
$$
 p_c=I_\theta(c-mC\langle c\rangle),\qquad
 {\cal H}x=S'(x-vW_\theta p_c),\qquad
 E_h=-vp_c,\qquad \mu_h=-m\langle c\rangle ,
$$
$$
 S'=\begin{pmatrix}v&-uv\\0&-v^2\end{pmatrix},\quad
 t=P\widehat R,\quad
 e=I_\theta(C\widehat R_2)-m\langle C I_\theta(C\widehat R_2)\rangle,
 \quad g=C\widehat R_2.
 \tag{S.8}
$$
The second term in $e$ is written even though its value vanishes for the actual reflection residual; the corresponding full unknown mean terms are never suppressed.

On every translated coefficient family, $I_\theta$ has norm $1/4$ and the complete mean projection has norm $1$. From (S.5)--(S.7) one may take
$$
 \|p_c\|\le4\|c\|,\quad \|{\cal H}\|<2^{13},\quad
 \|E_h\|\le2^5\|x\|,\quad |\mu_h|\le2^3\|x\|,
$$
$$
 \|t\|<2^{17},\quad \|t_\theta\|<2^{28},\quad
 \|g\|<2^{16},\quad \|e\|<2^{18},\quad
                         \|e_\theta\|<2^{17}.
 \tag{S.9}
$$
These are joint multiplier/module bounds, not point samples.

Equation (G.8) has exactly the decomposition
$$
 H_Rx=\partial_\theta(-ex)+O_Rx,
$$
$$
 O_Rx=e_\theta x+DP[t]{\cal H}x-t_\theta E_h
                              +W_\theta(gE_h+e\mu_h).
 \tag{S.10}
$$
There is no unbounded differentiated unknown in $O_R$.
The matrix $DP[t]$ has norm less than $2^{19}$.
The four terms in (S.10), using (S.9), give safely
$$
                  \|O_{R,z}\|<2^{36},\qquad
                  \|M_{e,z}\|<2^{18}.
 \tag{S.11}
$$
Every finite-rank mean functional is included in these bounds. The ordinary-source input norm costs an additional $\sqrt{|I|}<2$ from $\mathfrak M_0$ to $L^2_rL^2_\theta$. Combining (S.4) and (S.11) proves the uniformly bounded analytic family
$$
 K_z=G_{o,z}O_{R,z}+G_{d,z}(-M_{e,z}),\qquad
               \sup_{|\operatorname{Im}z|\le\sigma}\|K_z\|<2^{64}.
 \tag{S.12}
$$
The large bound in (S.12) is used only for a commutator. The real operator keeps the much smaller bound (S.3).

Uniqueness of the full physical cap problem and the exact coefficient identities imply $K_z=C_zKC_{-z}$ on finite Fourier data. No new radial derivatives or pointwise Hessian computations enter this identity. One-sided ordinary residual jumps are harmless: (S.10) contains no radial derivative of $R_0$.

## 4. An operator-valued Fourier-lag lemma

The following argument works for the actual $\ell^2$ of radial supremum spaces in (S.1); it does not require replacing that space by $L^\infty_rL^2_\theta$.

Suppose an operator $T$ has an analytic translation family $T_z=C_zTC_{-z}$ with uniform bound $B$ for $|\operatorname{Im}z|\le\sigma$.
Its angular lag-$\ell$ component, $\ell\in4\mathbb Z$, is the Fourier coefficient of $a\mapsto C_aTC_{-a}$. Contour shift gives
$$
                    \|T_\ell\|\le B e^{-\sigma|\ell|}.
 \tag{S.13}
$$
Each such component takes input frequency $n$ to output $n+\ell$ while preserving the original radial source/solution spaces. In particular its estimate is a full operator norm; it does not sum unrelated entrywise suprema without a row/column argument.
The absolutely convergent sum $\sum_\ell T_\ell$ equals $T$, first on finite Fourier data and then by completion.

For $M\ge1$ define
$$
 W_{s,M}(k)=(1+k^2/M^2)^{s/2},\qquad
                   \tau={|s|\over2M}.
 \tag{S.14}
$$
The logarithm of this weight has derivative bounded by $\tau$, so
$$
 \left|{W_{s,M}(n+\ell)\over W_{s,M}(n)}-1\right|
                              \le e^{\tau|\ell|}-1 .
$$
For $\tau\le\sigma/2$, (S.13), applied to each complete lag band, yields
$$
 \begin{aligned}
 \|W_{s,M}TW_{s,M}^{-1}-T\|
 &\le B\sum_{\ell\in4\mathbb Z}
           e^{-\sigma|\ell|}(e^{\tau|\ell|}-1)\\
 &\le2B\tau\sum_{j\ge1}j e^{-(\sigma-\tau)j}
 \le {8B\tau\over\sigma^2}.
 \end{aligned}
 \tag{S.15}
$$
The second line harmlessly includes every integer lag.
For the last inequality use
$\sum_{j\ge1}je^{-aj}=1/(4\sinh^2(a/2))\le a^{-2}$.
Mean-to-nonmean, nonmean-to-mean, and mean-to-mean blocks are all in this same lag decomposition.

## 5. Uniform inversion through order 1024

Take the exact fixed scale
$$
                         M=2^{256}.
$$
For every $-3/2\le s\le1024$, (S.12)--(S.15), with $B=2^{64}$ and $\sigma=2^{-7}$, give
$$
 \|W_{s,M}KW_{s,M}^{-1}-K\|<2^{-166}.
 \tag{S.16}
$$
Indeed $\tau\le2^{-247}$; all comparisons are exact powers of two.
With (S.3),
$$
 \|W_{s,M}KW_{s,M}^{-1}\|<1/32,\qquad
        \|(I-W_{s,M}KW_{s,M}^{-1})^{-1}\|<2 .
 \tag{S.17}
$$
There is no upper frequency cutoff. The mean weight is exactly one.

Let $\mathfrak M_{s,M}$ denote (S.1) with $W_{s,M}$ instead of $\langle k\rangle^s$. For $s\ge0$,
$M^{-s}\|x\|_{\mathfrak M_s}\le\|x\|_{\mathfrak M_{s,M}}\le\|x\|_{\mathfrak M_s}$.
For $s<0$ the inequalities reverse in the corresponding way, giving the same total norm conversion $M^{|s|}$, rather than its square. Consequently
$$
 \boxed{\quad
 \|(I-K)^{-1}:\mathfrak M_s\to\mathfrak M_s\|
       <2M^{|s|}\le2^{262145},
       \qquad -3/2\le s\le1024 .
 \quad}
 \tag{S.18}
$$
This pays the residual-sensitive bridge at negative as well as high order. It is not an inference that a small unweighted norm remains small after an arbitrary Sobolev conjugation.

The same analytic-lag argument, without a smallness claim, transfers each original physical Green input column to its declared weighted source/trace space. Ordinary, divergence, independent mean, and jump columns remain separately identified. In particular a derivative source is consumed through the already paid divergence column in (S.10), not through an ordinary-source norm that would lose one derivative.

## 6. Returning to the actual moving angle

The norms in (S.1) are physical Fourier modules. A radially varying angle map is not declared to preserve the different moving-angle $\ell^2\sup_r$ module.

At each fixed $r$, the actual $\Theta,\Phi$ and their inverses have positive Jacobian and real $L^2$ measure ratios below $2$. Their first derivatives are bounded by $2$ in an analytic strip of width at least $1/128$. For an integer $q\le1030$, the complete one-variable chain rule and Cauchy give
$$
 {|\partial_\theta^j\Phi|\over j!},
 \ {|\partial_\phi^j\Theta|\over j!}\le2\,128^j
 \quad(j\ge1).
$$
The sum over partitions in the chain rule has at most $2^q$ terms; $q!\le2^{11q}$. Including all lower derivatives and the binomial equivalence with the Bessel-potential norm, either positive-order pullback is bounded by $2^{32768}$. Negative-order pullback follows from its actual density adjoint
$C_\Phi^*=M_{\Theta'}C_\Theta$, retaining the Jacobian, and Hilbert interpolation covers noninteger orders.

For completeness, an analytic multiplier $a$ with joint $\mathscr A_{1/128}$ norm at most $2^{32}$ has, throughout this exponent window, a Sobolev multiplier bound less than $2^{21000}$. One uses the full coefficient sum and
$$
 \sup_{x\ge0}(1+x)^q e^{-x/128}
                \le2^{q+1}q!\,128^q,\qquad q\le1030 .
 \tag{S.19}
$$
Thus both complete angle pullbacks, including negative orders, have norm less than $2^{65536}$.

The full forward differential (G.4) consists of analytic multipliers, $I$, and complete mean projections, with at most three ordered multipliers in its rank-one term. Its inverse (G.5) can be expanded as
$$
 {\cal H}x=S'x-S'vW_\theta I c
                     +mS'vW_\theta(IC)\langle c\rangle .
 \tag{S.20}
$$
All displayed coefficient products are bounded by $2^{32}$ in the same algebra. Equations (S.19)--(S.20) therefore bound each same-angle differential by $2^{65536}$, and each full moving/physical differential by $2^{131072}$.

It follows that an ordinary moving source in $L^2_rH^s_\phi$ has its complete physical $D\Psi$ source in $L^2_rH^s_\theta$ with that factor. A physical solution in $\mathfrak M_s$ gives a moving solution in $L^\infty_rH^s_\phi$ with the same factor. Each genuine endpoint or jump is transformed at its own exact angle with its full mean. These statements use fixed-$r$ or integrated pointwise bounds and do not assert an unproved maximal Fourier composition estimate.

## 7. Closing the same normalized-gauge cap--tail interface

Use exactly the physical interfaces of (L.1)--(L.28) and the
[complete 1024-order network](R119-supplement-complete-1024-angular-Sobolev-network-and-physical-cap-Schur.md), (U.1)--(U.28).
The tail remains at the same actual common five-box parameter point, with its full high, deep-low, finite remaining band, mean equations and physical constant-height gauge.

The complete physical cap column $f_B\mapsto x_{\rm phys}$ satisfies, throughout the required Sobolev window,
$$
 \|{\cal C}_f^{\rm phys}:H^{s+2}_\perp\to\mathfrak M_s\|
                                      <2^{40+65536}.
 \tag{S.21}
$$
This is the full-state version of the original complex translation argument; (L.8) already controls both curvature outputs before its final $Z$ projection. Its signed-lag bound has input factor $|n|^2$, so the shift from $s+2$ to $s$ costs only the same finite analytic-lag moment used in U. In particular (S.21) includes $s=-3/2$ and does not require an unknown analytic input.

For the normalized moving equation in physical variables the exact column is
$\mathcal C_f^{\rm cov}=(I-K)^{-1}\mathcal C_f^{\rm phys}$.
By (S.18), its final $Z=(C(R)-C_{\rm ref})_\perp$ output obeys the safe common bound
$$
 \|{\cal C}_f^{\rm cov}:H^{1/2}_\perp\to H^{-3/2}_\perp\|
                                      <2^{400000}.
 \tag{S.22}
$$
Both curvature means were retained during this inversion; only this original interface output is projected.

The unchanged actual long and complete tail columns have
$$
 \|{\cal Q}_Z:H^{-3/2}_\perp\to{\cal B}_0\|
                     <2^{64+65536}s_B\epsilon_L,\qquad
 \|{\cal T}_B:{\cal B}_0\to H^{1/2}_\perp\|
                     <2^{1600000}/s_B,
$$
$$
 s_B=a_Bw_B>0,\quad \epsilon_L<2^{-33554432},\quad
 {\cal B}_0=\{b\in H^{-1/2}:\langle b\rangle=0\}.
 \tag{S.23}
$$
Membership in $\mathcal B_0$ is the actual long mean/holonomy identity of (L.11)--(L.13), not a deletion of its raw mean correction.

Therefore the complete same-interface round trip satisfies
$$
 \boxed{\quad
 \|{\cal C}_f^{\rm cov}{\cal T}_B{\cal Q}_Z\|
 <2^{400000+1600000+64+65536}\epsilon_L
 <2^{-31000000}.
 \quad}
 \tag{S.24}
$$
The small physical factor $s_B$ cancels exactly. All original affine columns enter the same Schur solve with resolvent less than $2$.
The totalflux compatibility or its original auxiliary charge, independent physical height gauge, true $B_0,C_0$ curvature equations, and canonical-wave means remain distinct.

## 8. Precise scope

The complete normalized-gauge cap residual bridge is now paid on $H^{-3/2}$ and on the entire finite angular window through order $1024$, with a compatible complete cap--tail Schur at this fixed repaired centre. This result contains no new numerical experiment; it consumes the existing actual constants and explicit complete operator formulas.

Returning to the original moving forced equation still uses
$a'=DA[h]$ and
$L_{\rm orig}(h+aQ_{0,\phi})=L_{\rm cov}h+aR_{0,\phi}$.
Its phase source and actual endpoints cannot be removed by (S.18) or (S.24). Neither a nonzero $\delta$ ball, an analytic weight $224$ inverse, the full mixed inner-body high feedback, the true $\nu$ Schur condition, nor the nonlinear existence and geometric matching follow without their remaining equations.

All original successful native records, source identities, genuine jumps, and failed attempts are unchanged. The next steps retain these precise permissions while paying those remaining columns.
