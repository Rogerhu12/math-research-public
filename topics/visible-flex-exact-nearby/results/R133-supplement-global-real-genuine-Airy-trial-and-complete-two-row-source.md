# R133 supplement: a global real genuine Airy trial with its complete two-row source

2026-11-16, newton_source.

**Proved construction and absolute source orders; no new numerical enclosure.**
For the same selected repaired background, this note specifies an actual finite Airy trial on the whole negative interval. Its fold comes from the true characteristic lifts. Its reference profile has the original genuine root matrix, including the terminal-Ai shear. Its first amplitude solves the complete forced transport. A scalar mean equation then makes the entire second ordinary residual zero.

The first-row residual and every state jump remain. A finite exact expansion of the old angular primitive, followed by the complete angular inverse, gives an absolute order $n^{-2}$ for the integrated primitive source and for the true strict-interval jumps. The factor $n^{7/6}$ in the original input is included in this order.

This is not yet a new upper for the whole corrected physical waist error. The positive correction, the root/cut difference and the complete new-trial-to-old-waist-row difference are retained in one signed identity below. In particular neither a relative Airy estimate nor the new strict-source order removes the original positive correction.

## WUA1. Objects, domains and the two physical rows

Fix the actual selected real parameter $\delta_*$, at the fixed intrinsic parameter $\eta_0$, inside the already qualified real family $|\delta|\le10^{-8}$. Use the original continuously repaired centre, its original radial pieces, full even mean and complete angular coefficients. It is not assumed to solve the nonlinear PDE.

Let $r_*$ be the same simple root, $K<0$ for $0\le r<r_*$, and
$$
 \rho=r_*-r,\quad q=\sqrt{-K},\quad
 m=\Pi v,\quad \eta=-\gamma m>0,\quad
 S=u^2+Kv^2,\quad \beta=a_{\rm phys}'/a_{\rm phys},
 \quad d=-\beta IS .
 \tag{WUA.1}
$$
The period is $\pi/2$, the angle measure is normalized, $\partial=\partial_\phi$, $P=Id-\Pi$, and $I=\partial^{-1}P$. Thus the physical nonzero frequencies are $n=4|j|$, with $n\ge388$ on the original high input. The true reflection class has $u,h_1$ odd and $v,h_2$ even.

The operators used throughout are exactly
$$
\begin{aligned}
 D_0&=\partial_r-PM_d\partial P,\\
 A&=P(\eta\partial+M_\ell-2\beta M_{v_\phi}IM_u)P,
       &\ell&=-2\beta uv,\\
 B&=P(M_{\beta(1-u^2-3Kv^2)}
                   -2\beta K M_{v_\phi}IM_v)P,\\
 E&=P(M_{-\beta(1+3u^2+Kv^2)}
                   -2\beta M_{u_\phi}IM_u)P,\\
 C&=P(-\eta\partial+M_\ell-2\beta M_{u_\phi}IM_v)P,\\
 b_2&=P\{\beta(1-u^2-3Kv^2)-2\beta K v_\phi Iv-\gamma u_\phi\},\\
 b_1&=K\{\ell-2\beta u_\phi Iv+\gamma v_\phi\}.
\end{aligned}
 \tag{WUA.2}
$$
Multipliers and primitives retain this order. For $f=Ph_2$ and $z=\Pi h_2$, the two projected equations and the missing mean are
$$
\begin{aligned}
 D_0f&=Ah_1+Bf+zb_2+Pg_2,\\
 (D_0-E)h_1-KCf-zb_1&=g_1,\\
 z_r&=a_z z-2\beta m\Pi\{uh_1+K(v-m)f\}+\Pi g_2,\\
 a_z&=\beta(1-\Pi S)-2\beta Km^2 .
\end{aligned}
 \tag{WUA.3}
$$
They are the complete original moving system, not a background-PDE simplification.

JI proves the same $J=A^{-1}:H^s_{\rm even,0}\to H^{s+1}_{\rm odd}$ on the entire strict interval $[0,r_c]$, where
$$
 r_c=\frac{76285779072683}{320000000000000}.
$$
Its exact denominator is at least $(79/128)e^{-7/4}>0$, using the already saved whole-interval Wiener bounds. The originally certified local root inverse covers $[r_c,r_*]$. On their actual common domain they agree by uniqueness of the inverse of this same $A$. No old root norm is enlarged to the strict interval. Every bound below that uses a global $J$ means a complete bound obtained from JI's formula and the original local bound on this union.

The construction and its qualitative finite constants also apply to any other member for which these same real domain qualifications are retained. No selected $c_i,c_o$, KAM map or corrected waist factorization is extended to that member by this observation.

## WUA2. A global real fold from the true root lifts

In the inward variable $\rho$, solve the original two real characteristic equations as degree-one lifts:
$$
 \partial_\rho H_\sigma(\rho,x)
       =d(r_*-\rho,H_\sigma(\rho,x))
             +\sigma\eta(r_*-\rho)q(r_*-\rho),
 \qquad H_\sigma(0,x)=x .
 \tag{WUA.4}
$$
Let $\Phi_\sigma(r,\cdot)=H_\sigma(r_*-r,\cdot)^{-1}$. The coefficients are continuous and piecewise smooth in $r$, smooth in the angle, with a Lipschitz angular coefficient on this compact interval. The real flow and its positive angular derivative therefore exist on the whole interval. No circle representative is reset during the comparison.

The scalar comparison equation for $H_+-H_-$ has the strictly positive forcing $2\eta q$. Hence
$$
 H_+(\rho,x)>H_-(\rho,x),\qquad
 \Phi_+(r,\phi)<\Phi_-(r,\phi)\quad(\rho>0)
 \tag{WUA.5}
$$
as real lifts. Define
$$
 \omega=\frac{\Phi_--\Phi_+}{2}>0,\quad
 X=\frac{\Phi_++\Phi_-}{2},\quad
 T=-\left(\frac{3\omega}{2}\right)^{2/3},\quad
 Q_f=\frac{\eta q}{\sqrt{-T}},\quad D=\partial_r-d\partial_\phi .
 \tag{WUA.6}
$$
The original root analytic germ defines the limiting values at $\rho=0$. Away from the root, direct differentiation gives
$$
\begin{aligned}
 D\omega&=-\eta q X_\phi,&
 DT&=Q_fX_\phi,& DX&=-Q_fT T_\phi,\\
 {\cal D}&=X_\phi^2+TT_\phi^2
             =\Phi_{+,\phi}\Phi_{-,\phi}>0,&
 \mu&=Q_f^2{\cal D},&
 \det\frac{\partial(T,X)}{\partial(r,\phi)}&=Q_f{\cal D}>0.
\end{aligned}
 \tag{WUA.7}
$$
For each $r$, $X(r,\cdot)$ is an increasing degree-one circle map. At fixed $X$,
$\partial_rT=Q_f{\cal D}/X_\phi>0$.
Consequently the image is a genuine real curved domain
$$
 {\cal R}=\{(T,X):T_{\rm waist}(X)\le T\le0\}.
 \tag{WUA.8}
$$
Every point is connected to the root by its actual characteristic segment in this domain.

Near the root the previously proved analytic fold has these same two characteristic labels and the same root normalization. Uniqueness of the real characteristic equations identifies the two folds there. Thus root regularity is inherited from that germ; it is not inferred by dividing the away-root expressions by $\rho$. In particular $T/\rho$ has a strictly negative nonzero root limit, and $-T/\rho$, $Q_f$ and ${\cal D}$ have positive minima on the whole compact real domain. These are existence statements for finite positive constants, not new evaluations of them.

The reflection identities imply $X(r,-\phi)=-X(r,\phi)$, $T(r,-\phi)=T(r,\phi)$. The actual reflected columns are assembled before applying the typed inverse $J$. This does not assert a new global inverse on an unrelated full signed circle.

No complex radial continuation across the original seams, global complex strip or global three-phase gap $X_\phi-3|\omega_\phi|>0$ is asserted. The real fold proves only $X_\phi>|\omega_\phi|$. The finite real calculations below do not substitute the former, stronger gap.

## WUA3. The complete leading and first forced amplitudes

Put $k_*=K_r(r_*)>0$, $\eta_*=\eta(r_*)$, and
$$
 E_G(r)=\exp\left[-2\int_{r_*}^{r}\beta(t)\Pi S(t)\,dt\right],
 \quad
 G=(k_*/\eta_*)^{1/6}(-T/q^2)^{1/4}E_G .
 \tag{WUA.9}
$$
At the root this is its original analytic definition and $G=1$. With $x=X_\phi$, $y=T_\phi$ and $\epsilon=\operatorname{sgn}j$, set
$$
 w_0=(a_0,b_0)^t,\qquad
 a_0=G(x^2-Ty^2),\qquad b_0=-2i\epsilon Gxy .
 \tag{WUA.10}
$$
For $s=\sqrt{-T}$,
$$
 v_{0,\sigma}=a_0+i\epsilon\sigma s b_0
             =G\Phi_{\sigma,\phi}^{\,2}>0.
 \tag{WUA.11}
$$
The square of the ray derivative belongs to this height normalization.

For clarity the complete forcing is restated. Let
$$
\begin{aligned}
 e&=-\beta(1+3u^2+Kv^2),&
 b_{\rm loc}&=\beta(1-u^2-3Kv^2),\\
 t_Q&=\eta_r/\eta+d_\phi+e,&
 T_0&=\eta_r/\eta-4\beta\Pi S+5d_\phi,\\
 r_Q&=D\ell+\eta e_\phi-2\beta\eta u_\phi u
                          -\ell(\eta_r/\eta+d_\phi),\\
 \vartheta&=r_Q/\eta-2\beta Kvv_\phi,&
 V_0&=t_Qb_{\rm loc}-Db_{\rm loc}
                    -K(\ell^2-4\beta\eta vu_\phi),\\
 K_T&=\begin{pmatrix}0&T\\1&0\end{pmatrix},&
 H&=i\epsilon x\,Id+yK_T,&
 H_D&=i\epsilon DX\,Id+DTK_T .
\end{aligned}
 \tag{WUA.12}
$$
Here $K_T$ names a matrix; it is not a derivative. The complete first forcing is
$$
 \binom{F_b}{F_a}=-{\cal L}_0w_0,\qquad
 {\cal L}_0w=\mu^{-1}
 \left[(D^2+\eta^2K\partial_\phi^2-T_0D)w
          +V_0w-\vartheta H^{-1}H_Dw\right].
 \tag{WUA.13}
$$
In particular the last term from the original one-gain radial operator is present. The projections and finite primitive/mean remainders are retained below, rather than folded into a false equality between the full scalar operator and its degree-zero coefficient.

The free transport is
$$
\begin{aligned}
 ({\cal T}_\epsilon w)_0
    &=b+2Tb_T+2i\epsilon T a_X+lTb+i\epsilon T^2ma,\\
 ({\cal T}_\epsilon w)_1
    &=2a_T+2i\epsilon T b_X+la+i\epsilon T^2mb .
\end{aligned}
 \tag{WUA.14}
$$
Only in this displayed transport, $m(T,X)$ denotes the canonical coefficient; the physical mean elsewhere is $\Pi v$. It is fixed with $l$ by the original exact fold formula
$$
 l=\frac{H_cDT}{\mu}-\frac1{2T},\qquad
 T^2m=\frac{H_cDX}{\mu},\qquad
 H_c=q_r/q+4\beta\Pi S-4d_\phi .
 \tag{WUA.15}
$$
The apparent root singularities have the original analytic limits.

Define $w_1=(a_1,b_1^{\rm amp})^t$ by
${\cal T}_\epsilon w_1=(F_b,F_a)^t$, with the original common trace $a_1(0,X)=0$. A concrete real formula is the following. For $\xi=\Phi_\sigma=X-\sigma\omega$, let
$$
\begin{aligned}
 R_\sigma(T,X)
   &=\int_0^T
       \frac{F_a/2-i\epsilon\sigma F_b/(2\sqrt{-\tau})}
                 {v_{0,\sigma}}
          \big(\tau,\xi+\sigma\omega(\tau)\big)\,d\tau,\\
 v_{1,\sigma}&=v_{0,\sigma}R_\sigma,\qquad
 a_1=(v_{1,+}+v_{1,-})/2,\qquad
 b_1^{\rm amp}=(v_{1,+}-v_{1,-})/(2i\epsilon\sqrt{-T}).
\end{aligned}
 \tag{WUA.16}
$$
Here $\omega(\tau)=2(-\tau)^{3/2}/3$ in the canonical characteristic. Indeed
$$
 (\partial_T-\sigma\sqrt{-T}\partial_X)v_\sigma
 =(-l/2+\sigma\sqrt{-T}\,Tm/2)v_\sigma
       +F_a/2-i\epsilon\sigma F_b/(2\sqrt{-T}).
$$
The physical tangent satisfies
$(D-\sigma\eta q\partial_\phi)T=Q_f\Phi_{-\sigma,\phi}>0$.
Thus the integral remains in the true curved domain, with its genuine orientation $0\to T<0$, rather than in an assumed rectangle.

The singular forcing in (WUA.16) is integrable. Analytic continuation of the original local germ, not integrability alone, gives the regular root quotient and $b_1^{\rm amp}(0,X)=F_b(0,X)$. On the remaining finite real pieces the formula defines the actual first transport with all one-sided derivatives and forcing jumps.

## WUA4. A specified genuine profile on the entire negative real axis

Keep the original common radial potential $V(z,T)$, $z=j^{-2}$, the original $L=1/2000$, $M=276$, and the original normalized root matrix
$$
 C_n=\begin{pmatrix}1&0\\\beta_n&1\end{pmatrix}.
 \tag{WUA.17}
$$
The old successful potential domain contains $|T|\le L$. The original terminal-Ai definition, its normalization by $a_n$, the full $\beta_n$, the second reference column and the positive-side profile are unchanged.

Here is a concrete auxiliary extension, without extending any physical polynomial piece. Let
$$
 p_{64}(s)=
 \frac{\displaystyle\int_0^s t^{64}(1-t)^{64}\,dt}
      {\displaystyle\int_0^1 t^{64}(1-t)^{64}\,dt}.
$$
This is an exact degree-129 polynomial; its denominator is $64!^2/129!$. Define the real $C^{64}$ cutoff
$$
 \chi_V(T)=
 \begin{cases}
 0,&T\le-L,\\
 p_{64}(2(T+L)/L),&-L<T<-L/2,\\
 1,&T\ge-L/2,
 \end{cases}
 \qquad
 V_{\rm ext}(z,T)=
 \begin{cases}
 0,&T\le-L,\\
 \chi_V(T)V(z,T),&-L<T\le L.
 \end{cases}
 \tag{WUA.18}
$$
Only the paid potential is used in the middle branch. All transition derivatives are actual derivatives of this polynomial times the old potential. They are finite new coefficients; their norm costs are not called zero. This extension is real $C^{64}$ in $T$, and retains the original parameter dependence. It is not asserted holomorphic across the transition.

Let $F_n$ be the original free two-state Airy matrix, $\lambda=n^{2/3}$, $\det F_n=\lambda/\pi$. Define the full genuine matrix by
$$
 \Psi_{\rm ext}'=
 \begin{pmatrix}0&1\\n^2T-V_{\rm ext}&0\end{pmatrix}\Psi_{\rm ext},
 \qquad \Psi_{\rm ext}(0)=F_n(0)C_n .
 \tag{WUA.19}
$$
It agrees with the original genuine matrix for $-L/2\le T\le L$, by uniqueness. This includes the original positive terminal column and both original root state rows.

In the interaction frame $Z_{\rm ext}=F_n^{-1}\Psi_{\rm ext}$,
$$
 Z_{\rm ext}'={\cal K}_{\rm ext}Z_{\rm ext},\quad
 {\cal K}_{\rm ext}=\frac{\pi V_{\rm ext}}{\lambda}
          \binom{\operatorname{Bi}(\lambda T)}
                {-\operatorname{Ai}(\lambda T)}
          \begin{pmatrix}\operatorname{Ai}(\lambda T)&
                          \operatorname{Bi}(\lambda T)\end{pmatrix},
 \quad Z_{\rm ext}(0)=C_n .
 \tag{WUA.20}
$$
For every negative segment the interaction is supported in $[-L,0]$, of length at most $L$. The old $8\pi ML/\lambda<1/10$ argument therefore proves directly, without multiplying two copies of the old transfer,
$$
 \|{\cal U}_{\rm ext}(T,S)^{\pm1}\|<10/9,\qquad
 \|Z_{\rm ext}(T)\|,\ \|Z_{\rm ext}(T)^{-1}\|
       <200/171<6/5 \quad(T,S\le0).
 \tag{WUA.21}
$$
For $T\le-L$ the exact ordered formula is
$\Psi_{\rm ext}(T)=F_n(T)Z_{\rm ext}(-L)$.
The relative frame is bounded; this is not an unweighted norm bound for the physical two-state matrix.

Define
$$
 {\cal B}_{\rm ext}(T)=\int_0^1V_{\rm ext}(\tau^2T)\,d\tau,\qquad
 {\cal B}_{\rm ext}+2T{\cal B}_{\rm ext}'=V_{\rm ext},
 \qquad
 w_1^{\rm ext}=w_1+{\cal B}_{\rm ext}K_Tw_0 .
 \tag{WUA.22}
$$
It agrees with the original ${\cal B}$ for $T\ge-L/2$. Below $-L$,
${\cal B}_{\rm ext}$ is generally a nonzero constant times $(-T)^{-1/2}$; it is not cut to zero with $V_{\rm ext}$. Its full derivatives, including ${\cal B}_{\rm ext}'$, remain.

The exact free transport identity
$$
 {\cal T}_\epsilon({\cal B}_{\rm ext}K_Tw_0)
           =V_{\rm ext}w_0
 \tag{WUA.23}
$$
follows from ${\cal T}_\epsilon w_0=0$ and (WUA.22). The full Darboux comparison also remains, with
$$
 {\cal D}_{\rm ext}=
 \begin{pmatrix}
 1&-{\cal B}_{\rm ext}/n^2\\
 -T{\cal B}_{\rm ext}&1-{\cal B}_{\rm ext}'/n^2
 \end{pmatrix},
 \qquad H_{\rm ext}={\cal B}_{\rm ext}''+
                              V_{\rm ext}{\cal B}_{\rm ext}.
 \tag{WUA.24}
$$
In particular the two finite remainders are
${\cal B}_{\rm ext}K_Tw_1^{\rm ext}
 +{\cal B}_{\rm ext}'E_{22}w_0$ and
${\cal B}_{\rm ext}'E_{22}w_1^{\rm ext}$, in the original IN.8 order.
They are not removed by (WUA.23).

## WUA5. Absolute uniform real profile bounds

The following improvement of the elementary negative-axis bound uses no new Airy evaluation. For either $y(s)=\operatorname{Ai}(-s)$ or $\operatorname{Bi}(-s)$, A.8 gives $|y|,|y'|<2$ on $0\le s\le1$. For $s\ge1$ set
$$
 t=\frac23s^{3/2},\qquad z(t)=s^{1/4}y(s).
$$
Direct substitution in $y''+sy=0$ gives
$$
 z_{tt}+\left(1+\frac5{36t^2}\right)z=0,\quad
 {\cal E}=z^2+z_t^2,\quad
 {\cal E}'\le\frac5{36t^2}{\cal E}.
 \tag{WUA.25}
$$
At $t=2/3$, $z=y$, $z_t=y'+y/4$, so
${\cal E}<4+25/4=41/4$.
The integral of $5/(36t^2)$ from $2/3$ to infinity is $5/24$. The already proved elementary $e^{1/2}<2$ then gives
${\cal E}<(41/4)e^{5/24}<41/2<25$.
Thus $|y|\le5s^{-1/4}$ and $|y'|\le(25/4)s^{1/4}$ for $s\ge1$. Combining both intervals yields
$$
 |\operatorname{Ai}(-s)|,\ |\operatorname{Bi}(-s)|
       \le6(1+s)^{-1/4},\qquad
 |\operatorname{Ai}'(-s)|,\ |\operatorname{Bi}'(-s)|
       \le7(1+s)^{1/4}.
 \tag{WUA.26}
$$
For the first inequality use $5\,2^{1/4}<6$, equivalently $1250<1296$.

Each of the two genuine columns $Y$ of (WUA.19) consequently satisfies, on the entire negative real axis,
$$
 |Y(T)|\le12(1+n^{2/3}|T|)^{-1/4},\qquad
 |Y_T(T)|\le12n^{2/3}(1+n^{2/3}|T|)^{1/4}.
 \tag{WUA.27}
$$
The two free rows contribute $\sqrt2$ and the complete interaction column contributes at most $6/5$; the larger derivative constant is $42\sqrt2/5<12$. The second estimate follows from the full two-state frame, not by differentiating the first upper bound.

For the first, normalized terminal-Ai column define
$$
 {\cal U}_{n,\epsilon}^{\rm ext}(a,b)
       =e^{i\epsilon nX}\{aY(T)+bY_T(T)/n\}.
 \tag{WUA.28}
$$
The same estimates hold for the second reference column when it is independently retained. On the compact fold domain, set $T_*=\sup|T|$ and choose the positive $t_*$ with $|T|\ge t_*\rho$. Then, for a complete amplitude norm,
$$
 \|{\cal U}_{n,\epsilon}^{\rm ext}(a,b)(r)\|_2
 \le C_{\rm prof}\|(a,b)\|_\infty
                  (1+n^{2/3}t_*\rho)^{-1/4}.
 \tag{WUA.29}
$$
For example $C_{\rm prof}=12(2+\sqrt{T_*})$ is sufficient for the component-sum norm, since
$n^{-1/3}(1+n^{2/3}|T|)^{1/2}
 \le n^{-1/3}+\sqrt{|T|}$.
Neither $T_*$ nor $t_*$ is evaluated here. The original reflected pair can be assembled with its declared normalization; this introduces its actual fixed pair factor, never an unexplained change of vector norm.

## WUA6. A finite exact primitive calculus, without a new profile determinant

The free matrix $H$ in (WUA.12) has determinant $-{\cal D}$, with a positive complete gap on the real domain. In contrast the point matrix obtained by inserting $V_{\rm ext}$ into the genuine profile derivative would have determinant
$-({\cal D}-n^{-2}V_{\rm ext}T_\phi^2)$. No new lower bound for this latter expression is assumed or needed.

Let $E_{12}(a,b)^t=(b,0)^t$, and define
$$
 {\cal A}_n=\partial_\phi-n^{-1}V_{\rm ext}T_\phi E_{12}.
$$
The exact old-angle derivative rule is
$$
 \partial_\phi{\cal U}^{\rm ext}(v)
       ={\cal U}^{\rm ext}(nHv+{\cal A}_nv).
 \tag{WUA.30}
$$
For a fixed finite $N$, set
$$
 v_0=H^{-1}v,\quad
 v_{k+1}=-H^{-1}{\cal A}_nv_k,\quad
 W_N={\cal U}^{\rm ext}
                  \left(\sum_{k=0}^{N-1}n^{-1-k}v_k\right).
$$
Then the following identities, including their full means, are exact:
$$
\begin{aligned}
 \partial_\phi W_N
     &={\cal U}^{\rm ext}(v)
            +n^{-N}{\cal U}^{\rm ext}({\cal A}_nv_{N-1}),\\
 I{\cal U}^{\rm ext}(v)
     &=W_N-\Pi W_N
          -n^{-N}I{\cal U}^{\rm ext}({\cal A}_nv_{N-1}),\\
 \Pi{\cal U}^{\rm ext}(v)
     &=-n^{-N}\Pi{\cal U}^{\rm ext}({\cal A}_nv_{N-1}).
\end{aligned}
 \tag{WUA.31}
$$
The last remainder uses the actual $I$, with its complete norm $1/4$. The extra power $n^{-1}$ in the leading terms was obtained by the identity, not by replacing this $1/4$ norm by $1/n$. A full old mean is a retained smooth functional, even when this formula gives it rapid decay on these particular columns.

There is an equally concrete finite identity for the complete $J$. Write $A=\eta\partial+L_A$ with $L_A$ exactly as in N/O, and $J_{\rm pr}=\eta^{-1}I$. On the original parity spaces,
$$
 J=J_{\rm pr}\sum_{k=0}^{N-1}(-L_AJ_{\rm pr})^k
                 +J(-L_AJ_{\rm pr})^N .
 \tag{WUA.32}
$$
It follows by repeatedly substituting $J=J_{\rm pr}-JL_AJ_{\rm pr}$.
There is no infinite-series convergence assumption and no requirement
$\|L_AJ_{\rm pr}\|<1$. The final $J$ is the already established complete inverse. Every $L_A$ in this identity still contains its original primitive and projections.

For subsequent order counting use total cutoff $N=6$: expand each primitive by (WUA.31) only as far as total input power $n^{-6}$, keep every mean and exact terminal operator, and do not generate or evaluate discarded higher terms. This is a finite algorithm. Products of multipliers and the finite identities (O.4), (O.5), (O.15) specify every coefficient. No finite Fourier section replaces an input or output.

A useful verification of the cutoff is as follows. The ordered scalar expression below contains at most two positive derivative powers of $n$. A terminal remainder at total order $n^{-6}$, before these powers and the declared input $n^{7/6}$, is therefore at most
$$
 C n^{7/6+2-6}(1+n^{2/3}t_*\rho)^{-1/4}
       =C n^{-17/6}(1+n^{2/3}t_*\rho)^{-1/4}.
 \tag{WUA.33}
$$
All lower-order terms are no worse. Means in the same expansion are bounded using the third line of (WUA.31), with the same total cutoff. Complete bounded terminal $I$ or $J$ factors are not assigned another unproved power.

Only finitely many angular derivatives are needed. With this total-order rule only six inverse-power steps are retained; the differential expression has order two, and at most two further leading primitive gains are used below. All derivative lists are obtained by these finite product and chain rules. The fixed $C^{64}$ cutoff leaves ample finite differentiability for this list, including separate differentiation of its intermediate products. On each original piece the required ordinary radial derivatives are the actual one-sided derivatives. Their finite suprema exist; a later numerical consumer must supply complete bounds for them rather than differentiate an interval upper.

## WUA7. The full ordered scalar cancellation and its absolute source order

For precision, the full scalar operator being expanded is
$$
\begin{aligned}
 Q_{\rm op}&=([D_0,A]+AE)J,\\
 V_{AC}&=AC+\eta^2\partial^2,\\
 {\mathscr Q}&=D_0^2+\eta^2K\partial^2
           -(B+Q_{\rm op})D_0
           +Q_{\rm op}B-[D_0,B]-KV_{AC}\\
 &=A\{(D_0-E)J(D_0-B)-KC\}.
\end{aligned}
 \tag{WUA.34}
$$
All of these are exact N/O operators. In particular
$Q_{\rm op}=PM_{t_Q}P+R_QJ$, with the complete O.15 $R_Q$, so no radial derivative of an unknown inverse has been hidden in the local forcing. The one-gain radial term is present and gives the $\vartheta H^{-1}H_D$ term already kept in (WUA.13).

Apply the finite rules (WUA.30)--(WUA.32) to this displayed expression. The coefficient of $n^2$ is zero by (WUA.7). The coefficient of $n$ is the original transport $\mu{\cal T}_\epsilon$. The degree-zero coefficient on a genuine-profile amplitude $w$ is
$$
             \mu({\cal L}_0w-V_{\rm ext}w).
 \tag{WUA.35}
$$
To check the new potential contribution directly, in canonical variables the free derivative matrix is $K_T$, while the genuine equation replaces it by $K_T-n^{-2}V_{\rm ext}E_{12}$. In physical variables the phase cross coefficient is
$DX\,DT+\eta^2KX_\phi T_\phi=0$, while
$(DT)^2+\eta^2KT_\phi^2=\mu$.
Thus the second-order local contribution is exactly
$-\mu V_{\rm ext}w$ before division by $\mu$, and
$-V_{\rm ext}w$ in the normalized degree-zero expression. Its remaining terms, including derivatives of $V_{\rm ext}$, carry at least $n^{-1}$. The already present one-gain nonlocal terms retain their degree-zero coefficient from the free $H$; their extra genuine derivative term starts at a lower degree. Projections introduce the full mean terms in (WUA.31), not a further local symbol.

Now put
$$
 f_n=P n^{7/6}{\cal U}_{n,\epsilon}^{\rm ext}
                 (w_0+n^{-1}w_1^{\rm ext})
 \tag{WUA.36}
$$
and assemble the actual reflected input pair. Equations (WUA.13), (WUA.23) cancel the entire degree-zero term:
${\cal T}_\epsilon w_1^{\rm ext}
     +{\cal L}_0w_0-V_{\rm ext}w_0=0$.
Thus the finite expansion gives an exact decomposition
$$
 {\mathscr Q} f_n
       =n^{1/6}P{\cal U}^{\rm ext}(r_n)+{\cal E}_{6,n}.
 \tag{WUA.37}
$$
Here $r_n$ is the retained finite sum of all coefficients of degrees $-1$ through the total cutoff, with the common $n^{-1}$ factored out. It includes the complete $R_Q,J,I,V_{AC}$, potential, derivative and projection products specified above. It is not just a local differential residual. The term ${\cal E}_{6,n}$ is the sum of the exact terminal operators and retained mean functionals from those same finite identities. Both are defined by that finite algorithm applied to (WUA.34), without a new asymptotic solution or an unspecified infinite symbol expansion.

On the compact finite-piece domain the amplitudes $r_n$, with the finite additional derivatives needed below, are uniformly bounded in $n$; the factors $z=j^{-2}$ and $n^{-1}$ remain in their original qualified compact ranges. Equation (WUA.33) bounds the complete terminal sum. Applying (WUA.31)--(WUA.32) once more to the retained amplitudes proves
$$
 \|I J{\mathscr Q}f_n(r)\|_2
 \le C_1 n^{-11/6}
                  (1+n^{2/3}t_*\rho)^{-1/4}.
 \tag{WUA.38}
$$
The leading two gains here are one genuine old $I$ and one complete $J$, before taking the norm. Terminal pieces use their complete bounded operator norms. Constants such as $C_1$ are finite complete coefficient recipes, not evaluated numbers.

This gives a specific absolute order: on a fixed strict subinterval, where $\rho$ has a positive lower bound, the right side is $O(n^{-2})$. On the whole real negative interval its ordinary radial integral is also $O(n^{-2})$, since
$$
 \int_0^{r_*}(1+n^{2/3}t_*(r_*-r))^{-1/4}dr
 \le\frac43 t_*^{-1/4}r_*^{3/4}n^{-1/6}.
 \tag{WUA.39}
$$
No radial receiver singularity has been estimated by (WUA.39). Its use for a received root-collar error still needs that receiver's actual qualification.

## WUA8. Exact mean completion and the remaining first-row residual

Define $h_{10}=J(D_0-B)f_n$, $k_2=Jb_2$, and
$$
 a_{\rm eff}=a_z+2\beta m\Pi(uk_2),\qquad
 F_{\rm mean}=2\beta m\Pi\{uh_{10}+K(v-m)f_n\}.
 \tag{WUA.40}
$$
Solve the single ordinary equation, with its actual negative orientation from the root,
$$
 z_n'=a_{\rm eff}z_n-F_{\rm mean},\qquad z_n(r_*)=0,
 \quad
 h_{1,n}=h_{10}-z_nk_2,\quad h_{2,n}=f_n+z_n .
 \tag{WUA.41}
$$
Its integrating-factor formula is unambiguous on all original pieces. Coefficients and forcing have their genuine one-sided values; the solution is continuous.

Substitution into (WUA.3) proves, on every open original piece,
$$
 g_{2,n}=0,\qquad
 g_{1,n}=(D_0-E)h_{1,n}-KCf_n-z_nb_1 .
 \tag{WUA.42}
$$
This is the complete second row, including its physical mean. The internal quantity $\Pi(uh_1)$ used in JI is not the state mean $z_n$.

The full first row can also be written
$$
\begin{aligned}
 g_{1,n}&=J{\mathscr Q}f_n
                  +F_{\rm mean}k_2-z_nR_{\rm mean},\\
 R_{\rm mean}&=(D_0-E)k_2+a_{\rm eff}k_2+b_1 .
\end{aligned}
 \tag{WUA.43}
$$
No $J_r$, coefficient derivative or full mean term is removed from this identity. It is often a useful ordered formula for a new complete calculation.

For the source order, the mean functional may be moved to its actual smooth adjoint test, for example
$\Pi(uJ(D_0-B)f)=\langle J^*u,(D_0-B)f\rangle$.
Apply the complete mean identity in (WUA.31), with $N=6$, to these actual tests and to the finite primitive terms in $B$. The sole positive derivative in $D_0f$ costs at most one power of $n$. Therefore
$$
 |F_{\rm mean}(r)|\le C_2 n^{7/6+1-6}
                   =C_2n^{-23/6},\qquad
 |z_n(r)|+|z_n'(r)|\le C_3n^{-23/6}.
 \tag{WUA.44}
$$
The finite constants contain the full adjoint tests, their required angular derivatives and the integrating-factor bound for $a_{\rm eff}$. These tests have the complete mean and repaired coefficients. They are not finite Fourier projections of the unknown state.

Consequently (WUA.38)--(WUA.44) prove
$$
 \int_0^{r_*}\|Ig_{1,n}(r)\|_2\,dr\le C_{\rm vol}n^{-2}.
 \tag{WUA.45}
$$
This is a complete ordinary first-row primitive source norm. It is not a claim that $g_1=0$, that the physical state mean vanishes, or that the root/positive received error has already been paid.

## WUA9. True seams and strict-interval receiving units

At every original strict seam the repaired $u,v$, all fixed angular derivatives, and intrinsic values agree. The intrinsic $q,q_r$ agree. The real ray equations therefore make $X_\phi,T_\phi$ radially $C^1$, and (WUA.9)--(WUA.10) make $G,w_0$ radially $C^1$. This requires no continuity of the repaired $m_r$.

The complete first forcing can jump. Its characteristic integral makes $w_1$ continuous, with its actual one-sided first derivatives. Since ${\cal B}_{\rm ext}K_Tw_0$ is $C^1$, the full height obeys
$$
 [f_n]=0,\qquad
 [\partial_rf_n]
       =P n^{1/6}{\cal U}_{n,\epsilon}^{\rm ext}
                                      ([\partial_rw_1]).
 \tag{WUA.46}
$$
The same $J,B,d,b_2$ are continuous on their typed spaces, and $z_n$ is continuous. Thus the actual state jumps are
$$
 j_n=[(h_{1,n},h_{2,n})]
             =(J[\partial_rf_n],0).
 \tag{WUA.47}
$$
These are retained impulses, not zero sources and not ordinary integrals. Each true seam has positive distance from the root. Equations (WUA.29)--(WUA.32) give
$$
 \sum_{\rm true\ seams}\|I j_{1,n}\|_2\le C_{\rm jump}n^{-2}.
 \tag{WUA.48}
$$
One may retain the original complete strict cover, including its zero-jump interfaces. No impulse is multiplied by an interval length. The $C^{64}$ auxiliary potential transition introduces no state-value jump.

For the original primitive-density coordinates the ordinary source and, after (WUA.47), each jump are exactly
$$
 \frac{n_g}{\sqrt{2q}}\,(Ig_1,Ig_1;0,0),\qquad
 \frac{n_g}{\sqrt{2q}}\,(Ij_1,Ij_1;0,0).
 \tag{WUA.49}
$$
The actual density conversion, and the declared placement of $n_g$, must be retained. More explicitly, the ungauged SP variables use $Y=\sqrt q\,\|ITh\|_2$. Their first-row source is $(Ig_1,Ig_1)/\sqrt{2q}$ before this weight, so its exact $Y$-size is $\|Ig_1\|_2$ and its direct mean component is zero. The gauged normalizer coordinates in (WUA.49) multiply this same vector by $n_g$.

On the already qualified strict interval $[0,r_c]$, use the complete saved SP/ST receiver in its original ungauged convention and its declared endpoint conversion. Its true first input column receives $\|Ig_1\|_2$ and $\|Ij_1\|_2$; its complete mean feedback stays in the propagation matrix. If the equivalent gauged source convention is used instead, the evolution and endpoint factors must be changed consistently. No extra $n_g$ is inserted into an already converted receiver. A second independent mean injection is not added after the exact zero $g_2$ proof. This is the precise place where the strict received source and jumps have order $n^{-2}$.

No formula in (WUA.49) divides by $q(r_*)=0$. The root collar is handled by its original qualified map or by a new complete endpoint/receiver estimate.

## WUA10. The same genuine root column and the full signed error

Let $h^G$ be the original genuine finite trial used on the positive side of PC, with its two physical state rows. Near the root, the new fold, $w_0,w_1$, $\Psi_{\rm ext}$ and ${\cal B}_{\rm ext}$ agree with their original objects. The new $z_n(r_*)=0$ therefore gives
$$
             {\mathscr U}_n(r_*)=h^G_n(r_*),
       \qquad {\mathscr U}_n=(h_{1,n},h_{2,n}).
 \tag{WUA.50}
$$
This is equality in the original genuine normalization, including the nonzero $\beta_n$. It does not identify the genuine column with free Ai.

Retain the original positive cutoff and correction $e_n^+$, with zero high stable correction and its original zero head/exterior data. If $P_F$ is the original complementary finite projector, the actual corrected column has root difference
$$
       e_n(r_*)=e_n^+(r_*)-P_Fh_n^G(r_*).
 \tag{WUA.51}
$$
The complete $P_F$ term is present even for a high input. Equality (WUA.50) preserves the same prescribed high stable trace after the same projections; it does not freely change the remaining physical head data.

On any qualified negative interval, let ${\cal E}_h(r,s)$ be the exact complete physical evolution, including its means. With $e=\Psi_A-{\mathscr U}$, the exact backward identity is
$$
 e(0)={\cal E}_h(0,r_c)e(r_c)
        +\int_0^{r_c}{\cal E}_h(0,r)g_{\mathscr U}(r)\,dr
        +\sum_{0<r_\lambda<r_c}
                    {\cal E}_h(0,r_\lambda)j_{\lambda,\mathscr U}.
 \tag{WUA.52}
$$
The cut value is the same root difference (WUA.51) plus the full collar source and any collar state jumps, propagated in the same orientation. Its finite interface and positive correction are not optional.

If the old WPL/SW waist principal is retained, with old complete trial $V_{\rm old}$, the actual error at the declared physical row is
$$
 {\cal R}_{\rm waist}(\Psi_A-V_{\rm old})
   ={\cal R}_{\rm waist}e(0)
        +{\cal R}_{\rm waist}({\mathscr U}(0)-V_{\rm old}(0)).
 \tag{WUA.53}
$$
In the raw-state equation (WUA.53), if the old object is given as SW's density trial $Y_{W,J}(0)$, the notation means exactly
$V_{\rm old}(0)=\mathfrak D_0^{-1}Y_{W,J}(0)$ on the smooth core, with the complete primitive-density conversion and both stored means. A raw state is not subtracted from a density state.
The observation includes the genuine primitive/mean row, its actual left normalization and its full right input map. If a new waist principal is chosen instead, both its leading map and its error change together. It is not legitimate to keep the old $T_i$ by naming the second term zero.

Equations (WUA.51)--(WUA.53) are a complete signed replacement target. Their proof uses the actual two-row evolution; an adjoint form may pair all terms before taking absolute values. Neither the old enormous positive scalar nor a new scalar is subtracted from another upper bound.

## WUA11. Exact endpoint comparison and the retained root shear

The following identity gives a concrete route to the second term of (WUA.53). Define, exactly as in IN,
$$
 N_n^{\rm root}=F_n(0)^{-1}{\cal D}_{\rm ext}(0)F_n(0),
 \qquad D_n^{\rm root}=C_n^{-1}(C_n-N_n^{\rm root}).
$$
Because (WUA.18) is identically one near zero, this is the original root matrix, with its original complete $O(n^{-4/3})$ qualification. On the whole extended negative axis,
$$
\begin{aligned}
 \Psi_{\rm ext}(T)-{\cal D}_{\rm ext}(T)F_n(T)
 ={}&\Psi_{\rm ext}(T)D_n^{\rm root}\\
 &+\int_0^T\Psi_{\rm ext}(T)\Psi_{\rm ext}(s)^{-1}e_2
       \frac{H_{\rm ext}(s)}{n^2}[F_n(s)]_{2,:}\,ds .
\end{aligned}
 \tag{WUA.54}
$$
This is a full two-state matrix identity, with its actual negative integration orientation. The input matrix $D_n^{\rm root}$ is not a separate arbitrary physical input column.

For a relative-frame bound on the integral, use (WUA.26)--(WUA.27), the exact Wronskian and (WUA.21). The height weight of the inverse column and the derivative weight of the free row cancel; the factor $\lambda$ cancels the Wronskian $1/\lambda$. Thus its integrand in the free frame is bounded by a complete constant times
$$
                 n^{-2}|H_{\rm ext}(s)|.
 \tag{WUA.55}
$$
On any fixed negative range its integral is finite. Below $-L$, the nonzero ${\cal B}_{\rm ext}$ tail and its second derivative belong to $H_{\rm ext}$ and are still present.

The order-$n^{-4/3}$ root matrix in (WUA.54) cannot be estimated by a weighted per-column Hilbert--Schmidt sum at that same endpoint. Its original input-diagonal matrix qualification, or a whole two-phase operator estimate with the actual angular derivatives, is needed. It must be charged only once when (WUA.54) is combined with the positive difference (WUA.51).

After (WUA.54), the finite amplitude multiplication is still exactly IN.8, with both $R_2,R_3$. A comparison to the old $c_i,c_o$ must additionally prove the common free first-symbol identity at the actual waist, retain every old primitive mean, the density rank, the same finite normalizer and the input order. These requirements specify a finite analytic comparison; they are not discharged solely by the relative-frame bound.

The new strict source order therefore does not by itself assign an order to the entire endpoint term in (WUA.53). Nor does it assert that the old free first-symbol factorization already holds for the whole new profile without this comparison.

## WUA12. The next numerical target and what may be reused

There is now a specified trial, rather than an unspecified uniform approximation:

1. Solve the two original real lifts on the existing physical pieces and form (WUA.6).
2. Use the closed $w_0$, the complete forcing (WUA.13) and the actual characteristic integrals (WUA.16).
3. Use the fixed extension (WUA.18)--(WUA.22) with the original root matrix.
4. Solve the scalar physical mean equation (WUA.41).
5. Evaluate the full signed first-row source (WUA.43), the true jumps (WUA.47), the same positive/root difference and the entire waist comparison.

A future authorized implementation may read the already successful full intrinsic/mixed bounds, the old potential/root matrix qualification, the local root fold and inverse, the strict propagation receiver, and the original complete source/mean conventions. It must not rerun their old producers or replace their scope. New global fold/amplitude derivatives and the finite residual coefficients are genuinely new targets; none has been numerically evaluated in this note.

For a useful replacement of the old whole error bound, the preferred next target is the entire signed received quantity (WUA.51)--(WUA.53), using the actual two-row adjoint or equivalent forward maps. The new $g_2=0$, $p=2$ volume and jump structure can be used before a norm is taken. The old positive correction and the endpoint shear are part of that target, not a separately forgotten remainder.

For the original $H^{-4/3}\to L^2$ goal, a complete per-column bound requires $p>11/6$, or a genuine dyadic block bound requires $p>4/3$. The strict source and jumps meet the former with $p=2$, but the endpoint/positive pieces must still be included. For graph compactness alone the complete-window alternatives $1<\sigma\le4/3$, $p>\sigma+1/2$ for columns and $p>\sigma$ for blocks remain available. The present construction does not promote a partial source exponent to one of these whole-error hypotheses.

No old successful target, profile, flow, derivative array, integral or norm is recomputed here. No new scalar, actual high contraction, physical finite inverse, complete incoming onto statement or nonlinear branch is granted. The actual independent second reference input, radial head, physical mean/amplitude equations and metric-parameter column remain outside this fixed homogeneous high-column construction.

## Immutable primary identities

| Primary and exact use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| N: complete moving rows, projections, mean and reconstruction | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| O: complete ordered scalar operator | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| F: closed leading amplitude and original seams | becc6a83aaa4c8813dec941c747f11f49bf4aa33 | 11462 | 679ab82202a4d65b8ce47db1ab353e51553e19b6cc1831a745e48c704b3e86a1 |
| L: complete first forcing and exact radial inverse derivatives | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| I: finite exact primitive and forced transport | ddc62b4539d640a950c2005505e08695f80910e7 | 14772 | 38e1495faf6d651401a94040566f9e59c1ccdd58732fc0aa4d176480c098210e |
| A: genuine root matrix and full relative frame | 62909c54de321da071a6bbc6e169e87b5888dde6 | 15528 | 0e56cf640b5c5f46c917699396e0ef6e5cce1fd5276cbddfc56ee1ed58d89c49 |
| IN: genuine Darboux identity and ordered first-amplitude correction | f13509b4d0afc691cfc95d86c0f8e5562f919129 | 33894 | d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75 |
| JI: exact full real-interval angular inverse and mean | 839fa641fe9ce3758ee69cfe3cb4299f59a3a239 | 11769 | 01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1 |
| PC: genuine positive trial, zero-stable correction and finite root complement | 35f3ddaec691c2d7c636ec43da3f52605ed6b329 | 37079 | 5368abae4c66f73800c16d5f2b906ddaa0f1d62d07e9bd9a3ca539061bdf5d68 |
| WTS: complete signed trial replacement and order tests | 08ec2cc5289729dcbfb3de3ebc5799ba8f7dce95 | 27396 | bb7dff28f8f8f0064029a63622b2a8ef949894733fa06384c8c3b4b084dbb94d |
| WRA: complete physical primitive/mean observation and same graph | ffe98b2256041bdc4a49d85146ddc48afb301e2c | 26647 | 40fb2167aa27c9f9e07bfcaea89c6f5d20059cc724eb7ba4930e02b16dd27889 |
| WPL: the old physical paired leading row and its retained terms | 582679b6e48a271153b90ecf1691deca2dc27c9c | 31021 | 052bd8ed9550ffebd9cb56744f7d4e56a9b6de5405c363d438813f9a100c8e24 |

The current proof is a real-domain extension and a finite exact calculation. Its immutable references identify the old formulas and scopes; they do not imply that any new global derivative constant or whole signed error has already been computed.
