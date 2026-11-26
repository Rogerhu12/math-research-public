# R144 supplement: the actual whole-positive high inverse in a full-tail neighbourhood

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all59 saved-rational comparisons pass.** The compact-centre
given-head high inverse extends to a genuine neighbourhood of unknown
backgrounds with arbitrary infinite Fourier tails. On the entire
positive interval the background perturbation has unweighted $A^3$
norm at most $10^{-6}$; its true outer endpoint separately has
unweighted $A^3$ norm at most $10^{-9}$. The two complete body feedback
bounds are $.310$ and $.801$. The actual physical exterior reflection
is below $.002402$ in both windows. The complete old-root reflection
bounds are $.453$ and $4.129$.

The derivative has the same source/state spaces as
[PH](R144-supplement-actual-positive-high-graph-for-compact-centres.md):

$$
 L^2_rH^{1/3}_\phi\longrightarrow L^2_{r,\phi},\qquad
 L^2_rH^{-2/3}_\phi\longrightarrow L^2_rH^{-1}_\phi .
 \tag{QN.1}
$$

All high modes $|j|\ge97$, both signs, original affine jumps, the
supplied moving mean, both independent physical mean paths, and
the true physical height and Robin inputs remain. The low193
reference, original $S_i$, root97 and outer96 observations are
unchanged. This is an actual high inverse with a supplied head;
the complete finite block, low/high Schur, negative return and
nonlinear iteration still require their own equations.

## QN1. The actual background domain

Let $I=[a,R]$, with the original true positive root $a$ and $R=25/8$.
By [SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md)
the compact centre on all of $I$ is one function $Q_*=(u,Mv/m)$,
independent of real $|\delta|\le10^{-10}$, with the original intrinsic
$K,\gamma,\beta$. In particular $Q_*(R)=Q_{\rm raw}(R)$ exactly.

For a pair use the component-sum Wiener norm

$$
 \|q\|_{A^j}
 =\sum_{k\in4\mathbb Z}(1+|k|)^j
                  (|q_{1,k}|+|q_{2,k}|).
 \tag{QN.2}
$$

The unknown background is $Q=Q_*+q$ in the real odd/even class, with

$$
 \sup_{r\in I}\|q(r)\|_{A^3}\le\rho=10^{-6},\qquad
                  \|q(R)\|_{A^3}\le e_R=10^{-9}.
 \tag{QN.3}
$$

Piecewise continuous radial coefficients suffice for the energy
realization; piecewise smooth states give the ordinary differential
identities directly. Original radial interfaces and their actual
affine jump conditions are retained. No derivative of $q$ in $r$
is inferred from (QN.3). The second bound is an independent endpoint
condition, not a trace conclusion from an interior $L^2$ norm.

The independent outer height background remains in the stated
original class

$$
 \|f_B\|_{\dot A^2_\sigma}\le b=2^{-60},\qquad \sigma\ge1/16.
 \tag{QN.4}
$$

An independent height direction will use
$\||D_\theta|^2\dot f_B\|_{H^s}$, not (QN.4). The new $q$ is not
assumed analytic in angle. In particular an $A^3$ ball gives no
positive spatial strip. Sections QN4--QN5 prove the needed
zero-width qualification of the nonlinear exterior module.

The four completed small inputs are exactly those in PH1, with
their recorded whole SHA256 values. The companion
[rational reader](../scripts/fourfold_codazzi_compact_nearby_high_saved_bounds.py)
only forms the positive combinations below from those conclusions.
It calls no old native producer, reference ODE, kernel sweep or
scientific target.

## QN2. The true mean change is absorbed in the principal reference

Write $m_Q=\langle Q_2\rangle=M+\langle q_2\rangle$. PH and PA give
$-M>1.068-2\,10^{-7}$. Thus the direct and inverse ratios of
$a_Q=-\gamma m_Q$ to $a_*=-\gamma M$ differ from one by less than
$\rho$:

$$
 {|\langle q_2\rangle|\over1.068-2\,10^{-7}-\rho}<\rho .
 \tag{QN.5}
$$

The true terminal coefficient is now
$p_{*,Q}=q_*/(-m_Q(R))$, with the same intrinsic regular multiplier
$q_*$. Its ratio to the compact terminal value differs from one by
at most $e_R/(5.84461145233-e_R)<\rho$.

Apply the complete variational comparison
[R.1--R.18](R133-supplement-relative-global-Riccati-reference-and-frequency-derivatives.md)
to these actual coefficients. The new references $p_Q(N),g_Q(N)$
use $g_Q(N,a)=N^{-1/3}$ and the actual $p_{*,Q}$ at $R$.
If the original family reference is denoted by a superscript $o$,
the composition with PH gives

$$
 \begin{gathered}
 \tau_0=1.894\,10^{-7},\quad
 \tau=\tau_0+\rho+\tau_0\rho,\quad
 \sigma=3.788\,10^{-7}+2\rho,\\
 (1-\tau)(p^o,g^o,W^o)
       \le(p_Q,g_Q,W_Q)\le(1+\tau)(p^o,g^o,W^o),\\
 k_Q(r)\ge(1-\sigma)k^o(r).
 \end{gathered}
 \tag{QN.6}
$$

Here $k^o$ is any original complete row damping lower function.
Throughout the body,

$$
 0<W_Q<4,\qquad {K\over W_Q}
       <{180\over(1-\tau_0)(1-\rho)}<181.
 \tag{QN.7}
$$

The upper bound follows from $K<4$, the two Riccati barriers
$p_Q,g_Q<2$, and the actual positive endpoint/initial data.
At the root collar the old uniform proof still gives $K/W_Q<1$.
Indeed the old speed bounds, enlarged by
$1.12(2.001\,10^{-7}+\rho)$, remain within $(1/2,1.26)$.
The unchanged intrinsic derivative gives
$29<K_s<122$ from
$59.74380437<K_r<60.465470$. These are precisely the hypotheses
of the original collar comparison, for any positive exterior
extension with terminal scalar in $(1/8,1/5)$.

The transformed principal rates are exactly
$\mp a_QNW_Q/2$. No small multiple of $\partial_\phi$ is put
into an ordinary-source Neumann series. The variational argument
allows piecewise measurable speeds; the exact frame derivatives
come from its two Riccati equations. In particular no estimate
of $m_Q'$ is required or supplied here.

## QN3. Full-frequency energy in both windows

Let

$$
 F_N=N^{-1/6}W_N^{-1/2}
        \begin{pmatrix}p_N&-g_N\\1&1\end{pmatrix},
 \qquad h_k=S_{\operatorname{sgn}k}^{-1}F_{|k|}Z_k .
 \tag{QN.8}
$$

In the negative window put $Y_k=|k|^{-1}Z_k$, so the raw frame
is $\widehat F_N=NF_N$. The exact rank-one identity I.6 in the
[all-frequency theorem](R133-supplement-all-frequency-frame-and-infinite-tail-neighbourhood.md)
gives, for either pair of signs and
$R_{MN}=\max(M,N)/\min(M,N)$,

$$
 \|F_M^{-1}S_\alpha S_\beta^{-1}F_N\|<3R_{MN}^{2/3},
 \qquad
 \|\widehat F_M^{-1}S_\alpha S_\beta^{-1}\widehat F_N\|
                         <3R_{MN}^{5/3}.
 \tag{QN.9}
$$

The logarithmic derivative of $\widehat F_N$ has norm below
$8/3$. For equal signs and $R_{MN}\le2$, integrating its
matrix ODE gives a difference at most $R_{MN}^{8/3}-1$;
the scalar mean-value inequality then gives

$$
 N\|\widehat F_M^{-1}\widehat F_N-I\|
       \le {8\over3}R_{MN}^{8/3}|M-N|<17|M-N|.
 \tag{QN.10}
$$

The strict inequality is for $M\ne N$; on the diagonal
the difference is exactly zero. The last strict test is
$(8/3)^3\,2^8<17^3$.
For $R_{MN}\ge2$ use (QN.9) and
$N/|M-N|\le2$, giving $8|M-N|R_{MN}^{5/3}$.
For opposite signs, $|k-n|=M+N\ge N$, giving
$4|k-n|R_{MN}^{5/3}$. The base window is covered by the
same larger bounds. In all cases
$R_{MN}\le1+|k-n|/388$.

Put

$$
 w(\ell)=(1+|\ell|/388)^{5/3}.
 \tag{QN.11}
$$

This is submultiplicative. Both $\|q_a\|_{A_w}$ and
$\|(q_a)_\phi\|_{A_w}$ are at most $\rho$ by (QN.3);
the largest required derivative order is $8/3<3$.
Retain the exact skew operator
$P_H(d\partial_\phi+d_\phi/2)P_H$ in each branch,
where $d=-\beta I(u^2+Kv^2)$.
The complete drift remainder is bounded by
$(35/2)\|d_\phi\|_{A_w}$ in either frame.

For a structured local coefficient
$B=(\begin{smallmatrix}a&Kb\\c&e\end{smallmatrix})$,
the same exact rank-one calculation gives the bound

$$
 2\{\|a\|_{A_w}+\|e\|_{A_w}
             +q_+\|b\|_{A_w}+4\|c\|_{A_w}\},
 \quad q_+=181
 \tag{QN.12}
$$

on the body; use $q_+=1$ in the collar. For the primitive
$-2\beta Q_\phi I(uh_1+Kvh_2)$ use
$\|I\|\le1/4$ on every nonzero intermediate mode.
The ordered double convolution is bounded with
$w(\ell_1+\ell_2)\le w(\ell_1)w(\ell_2)$.
No intermediate high projection is inserted. The exact zero
intermediate mode alone is removed.

The degree32 centre, and only that centre, obeys
$(129/97)^{5/3}<2$. Thus valid centre $A_w$ budgets are

$$
 (U,V,U_1,V_1)=(1.258,12.814,10.876,10.876).
 \tag{QN.13}
$$

In a single new frame compare the lower coefficients at $Q_*+q$
and $Q_*$. Set

$$
 \begin{aligned}
 dU^2&=2U\rho+\rho^2,&dV^2&=2V\rho+\rho^2,\\
 dUV&=(U+V)\rho+\rho^2,&dS&=dU^2+K_+dV^2,\\
 D(K_+,q_+)={}&{35\over2}dS
       +2\{4dS+2(q_++4)dUV\}\\
 &+(U_1+U)\rho+\rho^2
       +K_+\{(V_1+V)\rho+\rho^2\}\\
 &+q_+\{(U_1+V)\rho+\rho^2\}
       +4\{(V_1+U)\rho+\rho^2\}.
 \end{aligned}
 \tag{QN.14}
$$

The first line of the budget is the complete drift and local
reaction difference; the final two lines are all three
primitive words. Hence the full remainder increment is
at most $|\beta|D(4,181)$ on the body, with

$$
 D(4,181)<18000\rho,\qquad
 .211D(.00061,1)<92\rho
                    \quad\hbox{on the root collar}.
 \tag{QN.15}
$$

The rank $\gamma\langle h_2\rangle JQ_\phi$ is zero in
the high-to-high block because its input has zero mean.
Its new low-to-high column is generally nonzero and remains
in QN9 below.

The PH compact centre has a complete remainder at most
$1.003E_s^o$ in its own frame. Moving this finite degree32
majorant into the present frame costs at most
$(1-\rho)^{-1}$, exactly as in PH.11--PH.12.
The original positive expression satisfies $E_s^o\ge2|\beta|$.
Consequently a valid whole-row enlargement for both windows is

$$
 \lambda={1.003\over1-\rho}+{D(4,181)\over2},\qquad
                         E_s^Q\le\lambda E_s^o .
 \tag{QN.16}
$$

This uses a lower bound for the defining nonnegative majorant,
not a lower bound for a signed function inferred from its saved
upper ball. At $\beta=0$ the new increment is zero.

The collar's compact bounds $144$ and $432.18$ were proved
uniformly for every reference satisfying the coarse root
hypotheses. Adding (QN.15) gives the unchanged convenient
resolvents

$$
 (q_c,r_c,B_c)=
 (750/749,1/749,.009),\qquad
 (250/249,1/249,.009000020).
 \tag{QN.17}
$$

Indeed, for $h=9\,10^{-6}$,
$h(144+92\rho)<1/750$ and
$h(432.18+92\rho)<1/250$.
The original source/frame bounds below3, the negative Bessel
conversion, raw root factors below9 and all affine jump
conventions therefore remain. This estimate requires no
second angular commutator of the unknown background.

## QN4. A real endpoint chart places the new background in the exterior domain

All estimates in this section are at $R$, along the entire real
segment $Q_*+tq$, $0\le t\le1$.
The already proved raw endpoint numbers are

$$
 P=1.480385\,10^{-11},\quad
 U_\sigma=1.643190\,10^{-9},\quad
 V_\sigma=9.603792\,10^{-9},\quad
 5.84461145233<|m_*|<7 .
 \tag{QN.18}
$$

The known centre has strip $1/8$; the unknown correction uses
only its real $A^3$ norm. Write
$v=m+w$, $j=v/m$, $x=4\phi$, and

$$
 \begin{gathered}
 m_l=5.84461145233-e_R,\quad m_u=7+e_R,\\
 U_a=145U_\sigma+e_R,\quad W_a=145V_\sigma+e_R,\\
 U_1=3336U_\sigma+e_R,\quad V_1=3336V_\sigma+e_R .
 \end{gathered}
 \tag{QN.19}
$$

These bound $u,w,u_\phi,v_\phi$ in the real $A^2$
multiplier algebra. Subtracting an ordinary mean is contractive
in these norms. If $e^o=(8P,32P,192P,1536P)$, valid bounds for
$j-1,j_x,j_{xx},j_{xxx}$ are

$$
 e_{n+1}=e^o_{n+1}
           +{e_R(4^{-n}+e^o_{n+1})\over m_l},\quad0\le n\le3.
 \tag{QN.20}
$$

They follow by dividing the exact difference by the radial
constant $m$; they do not differentiate an $A^0$ error.
Also

$$
 b_j:=3336P+{e_R(1+3336P)\over m_l}
                  \ge\|j-1\|_{A^2},\qquad m_l-W_a>5.84.
 \tag{QN.21}
$$

For $j_l=1-e_1$, $j_u=1+e_1$, $j_2=4e_2$, the exact real
chain-rule and adjoint formulas N.20--N.22 give the four
$H^{\pm2}$ composition bounds

$$
 {j_u^2+j_2\over j_l},\quad
 {j_u(j_l+j_2)\over j_l^3},\quad
 {j_u(j_l+j_2)\over j_l^3(1-b_j)},\quad
 {(j_u^2+j_2)(1+b_j)\over j_l}
                    <c=1.000001 .
 \tag{QN.22}
$$

These control the actual real compositions and their inverses;
their difference from the identity is not asserted small.

The exact physical curvature variation, with the phase fixed
by the original mean-zero primitive, is

$$
 (DC[h])\circ\theta
 =-{h_2\over v^2}
       +{v_\phi\over v^3}I(h_2-zv/m),\qquad z=\langle h_2\rangle .
 \tag{QN.23}
$$

The multiplier reciprocal bound is $\|1/v\|_{A^2}<1/5.84$.
Thus (QN.22)--(QN.23) give

$$
 \|DC[h]\|_{H^2_\theta}
 \le c\left\{5.84^{-2}
       +{V_1\,5.84^{-3}\over4}(2+W_a/m_l)\right\}
                           \|h\|_{H^2_\phi}
 <.03\|h\|_{H^2_\phi}.
 \tag{QN.24}
$$

On the fourfold circle $\|f\|_{A^1}\le(6/5)\|f\|_{H^2}$:
the squared Cauchy--Schwarz sum is at most
$1+500/1536<(6/5)^2$. Integrating (QN.24) along the real
segment proves
$\|Z_Q-Z_*\|_{A^1_\theta}<.036e_R$.
The saved raw bounds $Z_{*,A^0}<2.533\,10^{-13}$ and
$\|(Z_*)_\theta\|_{A^0}<3.25\,10^{-11}$ therefore give

$$
             \|Z_Q\|_{A^0}<4\,10^{-11},\qquad
             \|(Z_Q)_\theta\|_{A^0}<7\,10^{-11}.
 \tag{QN.25}
$$

Here $Z=(C-C_{\rm ref})_{\ne0,\theta}$ is in the true physical
angle. The legacy saved field named Z_phi_A0 records precisely
the physical translation bound S.8; no moving/physical derivative
is silently exchanged.

## QN5. The exterior nonlinear module really admits zero-width backgrounds

The original long Dirichlet statement chose $\sigma>0$.
The module used in
[L.1--L.11](R133-supplement-final-regular-full-L2-and-Hilbert-Robin.md),
however, has explicitly unweighted background algebra
$\mathfrak A=\ell^1_k C^0_t$ and direction module
$\mathfrak M=\ell^2_k C^0_t$, with the radial supremum
taken before the final sequence norm.
For clarity the zero-width nonlinear value construction needed
here follows directly from the original formulas.

Drop only $e^{\sigma|k|}$ in
[R119 D.4--D.5](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md),
obtaining
$\mathcal Y_0,\mathcal F_0,\partial_0$ on the complete
signed set $4\mathbb Z$. They are complete spaces. The
Banach algebra inequality, mean read, primitive, radial
integral, convergent reciprocal and square-root series
have the same constants. The actual holonomy equation
therefore gives the same unique small root $\mu(h)$.
The original individual-mode Green D.15--D.17 still has
norm below32 and the actual two-end lift D.18--D.19
has norm at most16. Hence the actual nonlinear Dirichlet
map has, in these zero-width spaces, exactly the original

$$
 \|\mathcal Q(h)\|\le512\|h\|^2,\quad
 \operatorname{Lip}(\mathcal T)\le1/16,\quad
 \|(f_B,f_*)\|_{\partial_0}<2^{-25},\quad
                  \|h\|_{\mathcal Y_0}<2^{-20}.
 \tag{QN.26}
$$

All Fourier modes, the true finite long length and both
endpoint lifts are still present. Uniform complex contraction
proves holomorphy in the function parameters in these
unweighted Banach spaces.

The physical mean recovery also survives. Approximate the
two inputs in $\partial_0$ by finite Fourier inputs, choosing
for each approximation a positive strip small enough that
the same strict input margins hold. The original positive-strip
solutions agree with the unweighted solution by uniqueness and
converge in $\mathcal Y_0$. In particular
$h_{\theta\theta},h_{t\theta},h_{tt}$ converge in the full
joint algebra. The actual algebraic holonomy means converge
as well. On every approximant R119 Section5 gives

$$
 M_{\rm hol}=1,\qquad
 (M_{\rm hol})_t
  =w_{\rm long}^{\,2}
      \left\langle D^{-3/2}(1+K_{\rm rel}+EU)\right\rangle
           \mathfrak e=0 ,
 \tag{QN.27}
$$

with its bracket positive on real data and invertible on
the same complex small ball, so the pure mean PDE
residual $\mathfrak e$ is zero. The resulting formula for the
radial derivative of the mean is a continuous rational
function of the same convergent strong states. Its uniform
limit is the derivative of the limiting mean, by the
fundamental theorem of calculus. Thus the complete mean
equation, the true mean-height integral and both endpoint
mean slopes pass to the limit. No added angular derivative
of the holonomy formula is assumed.

The original curvature-to-Dirichlet contraction uses the same
algebra and Fourier multipliers. It consequently exists on
the full zero-width product ball

$$
 \|Z\|_{A^0}<\bar z=10^{-10},\qquad
               \|f_B\|_{\dot A^2_0}<\bar b=10^{-11}.
 \tag{QN.28}
$$

This is the same real nonlinear long graph, with both means;
the smaller actual background (QN.4),(QN.25) is inside it.
The unchanged wide-ball gates S.13 give
$2\bar F<2^{-25}$, $6\bar F<2^{-20}$, $\bar\kappa<10^{-3}$
and the actual curvature contraction self-map inequality.
The independently proved
[two-input zero-width cap/long theorem](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md),
M.2--M.5, uses precisely this type of unweighted value graph.

Finally apply the square-zero module L.1--L.5 to this
zero-width background construction. The complete per-mode
Green acts on $\mathfrak M$ with the same bound below32,
and $\|ax\|_{\mathfrak M}\le\|a\|_{\mathfrak A}\|x\|_{\mathfrak M}$.
The $\varepsilon$ component of the actual holonomy small root
is retained. Density of finite Fourier directions identifies
the resulting module derivative with the derivative of the
same value graph.

This proves the qualification needed for (QN.25). The complex
discs below are discs of **function parameters in $A^0_0$ and
$\dot A^2_0$**. They are not spatial strips and do not evaluate
an unknown $q$, $Z$ or height direction at a complex angle.

## QN6. Complete DN and physical outer bounds on the nearby domain

Keep the actual finite-length/regular fee
$0<\epsilon=2^{-512}$. For any allowed background radii $z,b$
use the original positive formulas

$$
 \begin{gathered}
 r_f=10(z+b),\quad F=r_f+b,\quad
 \kappa=36\cdot4096F,\\
 J_f={9\over1-\kappa},\qquad
 J_B={\epsilon+\kappa\over1-\kappa},\\
 T=\epsilon+4\cdot16384FJ_f,\quad C=(T-\epsilon)/8,\\
 U=\epsilon+4\cdot16384F(1+J_B),\quad V=(U-\epsilon)/8 .
 \end{gathered}
 \tag{QN.29}
$$

They bound the complete $L^2$ operators
$D_Zd,D_Zc_0,D_{f_B}d|D|^{-2},D_{f_B}c_0|D|^{-2}$,
respectively. Set the small ball to $(4\,10^{-11},2^{-60})$
and the wide ball to (QN.28). Legitimate function-parameter
disc radii at every actual background are
$r_Z=5\,10^{-11}$ and $r_B=9\,10^{-12}$.

Real translation covariance gives, for each of these four
operators $A$, including scalar mean outputs,

$$
 [\partial_\theta,A]
   =D_ZA[Z_\theta]+D_{f_B}A[(f_B)_\theta],\qquad
 \|[\partial_\theta,A]\|_2\le A_{\rm wide}\Xi,\quad
 \Xi={7\,10^{-11}\over r_Z}+{16\,2^{-60}\over r_B}.
 \tag{QN.30}
$$

Real translations are differentiable here because (QN.25)
gives $Z\in A^1$ and the stated height background supplies its
first derivative. The operator-valued Cauchy estimate is on
the legitimate module domain just proved, including complex
function directions. The $H^1$ derivative-vector estimate
gives $A_{\rm small}+\Xi A_{\rm wide}$. Applying the same
identity to the adjoint and then duality gives the same bound
on $H^{-1}$. Interpolation covers all $|s|\le1$, with

$$
 \begin{array}{c|rrrr}
 &D_Zd&D_Zc_0&D_{f_B}d|D|^{-2}&D_{f_B}c_0|D|^{-2}\\ \hline
 \text{whole norm}&.0012&.00015&.000134&.00001675 .
 \end{array}
 \tag{QN.31}
$$

The two scalar columns are genuine functionals on negative
spaces, obtained by the adjoint argument, not by discarding
their mean output.

The real Hilbert conjugation proof
[N.15--N.18](R133-supplement-final-regular-negative-window-and-height-ports.md)
needs only
the finite jets (QN.20). With $j_l=1-e_1$, define

$$
 \begin{aligned}
 K_0&=e_2/j_l+(1+\pi)e_1,\\
 K_{t1}&=e_3/j_l+e_2^2/j_l^2+[1+\pi(1+e_1)]e_2,\\
 K_{t2}&=e_4/j_l+3e_2e_3/j_l^2+2e_2^3/j_l^3\\
 &\quad+[1+\pi(1+e_1)]e_3
             +[2\pi+(1+e_1)\pi^2]e_2^2.
 \end{aligned}
 \tag{QN.32}
$$

Its exact regularized periodic kernel, with the two translation
commutators and adjoints, proves

$$
 \|\mathcal C J_\theta\mathcal C^{-1}-J_\phi\|_{H^s\to H^s}
 \le K_H:=K_0+8K_{t1}+16K_{t2}<6\,10^{-7},\quad |s|\le2 .
 \tag{QN.33}
$$

All bounds remain valid with $\pi<22/7$.
No analytic extension of the new $j$ was used.

For $f=\delta B\circ\theta$, $g=\delta C\circ\theta$ the
exact raw variation is

$$
 \begin{gathered}
 h_1=vf-uvg-u_\phi I(vg),\qquad
 h_2=-v^2g-v_\phi I(vg),\\
                         \langle h_2\rangle=-m^2\delta C_0 .
 \end{gathered}
 \tag{QN.34}
$$

This identity holds at an off-shell background as well.
Use $T=.0012$, $C=.00015$, $U_B=.000134$, $V_B=.00001675$,
$V_a=m_u+W_a$, $B_2=V_a^2+V_1V_a/4$, and $g_0=5.8$.
The exact onto nonmean chart in N.22--N.25 has

$$
 \begin{gathered}
 L_*={c(1+b_j)\over g_0^2},\qquad
 E_2=[W_a(2m_u+W_a)+V_1V_a/4]c(1+C),\\
             I_*={L_*\over1-L_*E_2}<.03 .
 \end{gathered}
 \tag{QN.35}
$$

The attached mean is part of this chart. It is not a free
second copy of the nonmean parameterization.

Let $\mathcal Rh=P_{\ne0}(-J_\phi h_1-p_{*,Q}h_2)$ and
$y=P_{\ne0}h_2$. The complete homogeneous row is
$\mathcal Rh=\mathcal Ey$, where

$$
 \begin{aligned}
 \|\mathcal E\|\le E:=I_*\{&
 m_u[c(T+\epsilon+C)+K_Hc(1+T+\epsilon)]\\
 &+W_ac(1+T+\epsilon)\\
 &+[V_a(U_a+U_1/4)
       +(W_a(2m_u+W_a)+V_1V_a/4)/g_0]c(1+C)\}.
 \end{aligned}
 \tag{QN.36}
$$

This is the original ordered physical calculation N.23--N.29
with each coefficient and DN norm now paid on the new real
domain. It keeps $Q_\theta-q_*I$, the actual holonomy mean
and the exact Hilbert difference. The affine row satisfies

$$
 \begin{gathered}
 \mathcal Rh=\mathcal Ey+\zeta,\qquad
 \|\zeta\|_{H^s}
 \le B_a(U_BF_B+\|r_B\|_{H^s})
                    +C_a(V_BF_B+|r_C|),\\
 B_a=V_ac,\quad
 C_a=V_a(U_a+U_1/4)+B_2/g_0+EB_2,\quad
 F_B=\||D_\theta|^2\dot f_B\|_{H^s}.
 \end{gathered}
 \tag{QN.37}
$$

The term $EB_2$ pays the affine shift of the onto chart.
Here $r_B$ is the independent physical nonmean Robin
residual and $r_C$ the independent physical mean residual.
The parameter $b$ in (QN.4) is not either residual.

Since $W_N(R)>1/8$, the exact Riccati outer equations in
the two windows use $s=1/6$ and $s=-5/6$, respectively.
The full high boundary feedback is at most
$A_o=(17/2)E$. Its Neumann series is on the entire high
Hilbert space, with no finite-band assumption:

$$
 {A_o\over1-A_o}<.002402<.0025 .
 \tag{QN.38}
$$

For each window let $X=Z$ or $Y$. The actual independent
boundary columns obey

$$
 \|X_{u,H}(R)\|
 <.0025\|X_{s,H}(R)\|
 +.001\|y_L\|_{H^s}
 +.004F_B+23\|r_B\|_{H^s}+28|r_C|.
 \tag{QN.39}
$$

The four affine constants are obtained from
$(51/16)(1-A_o)^{-1}(E,B_aU_B+C_aV_B,B_a,C_a)$.
In particular the entire physical low/head path remains.
The true attached moving mean separately satisfies

$$
 |\langle h_2\rangle|
 <.000219\|y\|_{H^s}
                 +.000822F_B+49.012|r_C| .
 \tag{QN.40}
$$

The exact three coefficients are
$m_u^2CI_*$, $m_u^2(1+CI_*B_2)V_B$ and
$m_u^2(1+CI_*B_2)$.
This is a physical compatibility row that the supplied
head must satisfy in the full problem. It is not imposed
automatically by solving the high graph.
The independent overall height translation remains outside
the nonmean norm. Both physical-density mean equations keep
their original identities.

## QN7. Actual whole body and collar/body inverse

The scalar two-branch comparison PH.13--PH.16 gives

$$
 T_s^Q\le{\lambda\over1-2\sigma}T_s^o,\qquad
 B_f^Q\le{B_f^o\over\sqrt{(1-\tau)(1-2\sigma)}},\qquad
 C_b^Q\le{C_b^o\over\sqrt{1-\tau}} .
 \tag{QN.41}
$$

Its scalar energies retain the exact skew transport in
each propagator. The factor2 in the damping denominator
pays both branch suprema, rather than assuming the saved
joint maximum equals either separate maximum.
At every affine jump the source-frame increase is at most
$(1-\tau)^{-1/2}$. No radial length factor is assigned to
a jump.

The complete saved balls, (QN.16) and (QN.38) now give

$$
 \begin{array}{c|cc}
 &\text{base}&\text{negative}\\ \hline
 \chi_s=T_s^Q+r_{o,s}^Q&<.310&<.801\\
 q_b&100/69&1000/199\\
 r_b&31/69&801/199\\
 B_f&.126142&.126142\\
 C_b&2.518&2.518\\
 \text{raw body-jump factor}&4.953&4.953 .
 \end{array}
 \tag{QN.42}
$$

For the negative source and jump entries the original
$(1+388^{-2})^{1/3}$ Bessel fee is already in the saved
constant. It is neither deleted nor paid a second time.
The new reconstruction factor is below $1.0000006$
and the source factor below $1.000003$ relative to
the respective saved original bounds.

The Hilbert realization is the same complete energy
construction as the original high theorem. Smooth finite
Fourier coefficient approximation gives the exact skew
identity and the same uniform majorants; the complete
Green equations and their contraction give the limit.
Uniqueness follows from the same strict feedback gates.
This supplies the actual infinite high inverse at every
background in (QN.3), not only a formal coefficient estimate.

Use the seven independent norms
$(s,F_c,F_b,B,J_c,J_s,J_u)$ of PH.26. Here $B$ contains
(QN.39)'s full affine exterior data and the complete
weighted body jumps; $J_c$ is the collar jump sum and
$J_s,J_u$ the two signed cut-jump inputs. Let
$\Lambda=r_cr_b$, $\Sigma=(1-\Lambda)^{-1}$. The exact
same-reference formulas are

$$
 \begin{aligned}
 X_b&=\Sigma\{q_cs+q_c(B_cF_c+J_c)+J_s
                  +r_c[q_b(B_fF_b+B)+J_u]\},\\
 Y_b&=r_bX_b+q_b(B_fF_b+B)+J_u,\\
 U_a&=r_cs+q_cY_b+q_c(B_cF_c+J_c),\\
 S_b&=q_b(X_b+B_fF_b+B),\\
 S_c&=q_c(s+Y_b+B_cF_c+J_c).
 \end{aligned}
 \tag{QN.43}
$$

The loops are below $.000600$ and $.016166$.
The raw full-interval state is bounded by
$(9hS_c^2+C_b^2S_b^2)^{1/2}$.
The true outer even $H^{-5/6}$ readout is bounded by
$(5/388)S_b$ in the base window and $4S_b$ in the negative
window. Thus the complete rational response tables are:

| Base output | $s$ | $F_c$ | $F_b$ | $B$ | $J_c$ | $J_s$ | $J_u$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Body frame sup | 1.452083 | .013070 | .183170 | 1.452083 | 1.452083 | 1.450147 | .001938 |
| Root outgoing | .452083 | .013070 | .183170 | 1.452083 | 1.452083 | .450147 | 1.001938 |
| Raw $L^2_{r,\phi}$ | 3.656366 | .032909 | .461223 | 3.656366 | 3.656366 | 3.651469 | .010252 |
| Outer even $H^{-5/6}$ | .018714 | .000170 | .002362 | .018714 | .018714 | .018689 | .000026 |

| Negative output | $s$ | $F_c$ | $F_b$ | $B$ | $J_c$ | $J_s$ | $J_u$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Body frame sup | 5.128207 | .046155 | .646884 | 5.128207 | 5.128207 | 5.107694 | .020514 |
| Root outgoing | 4.128207 | .046155 | .646884 | 5.128207 | 5.128207 | 4.107694 | 1.020514 |
| Raw $L^2_rH^{-1}$ | 12.912904 | .116218 | 1.628861 | 12.912904 | 12.912904 | 12.861224 | .052463 |
| Outer even $H^{-5/6}$ | 20.512822 | .184617 | 2.587530 | 20.512822 | 20.512822 | 20.430771 | .082053 |

Every table entry is a strict rational upper bound. The ordinary
sources use exactly (QN.1); an arbitrary rough source is not
assigned a stronger norm.

## QN8. Return to the original root coordinates

The original and new references have the exact same
$g_N(a)=N^{-1/3}$. Hence the relative root matrix is triangular:

$$
 C_N=(F_N^o)^{-1}F_N^Q
  =\begin{pmatrix}
     \sqrt{1+z_N}&0\\
     -z_N/\sqrt{1+z_N}&1/\sqrt{1+z_N}
    \end{pmatrix},\qquad |z_N|\le\tau .
 \tag{QN.44}
$$

The same formula applies to the negative frames.
The original stable input therefore has no coupling from
the new outgoing component. If $\mathcal R_Q$ is the complete
new root reflection, its original-coordinate form is exactly

$$
 \mathcal R_o=C_{us}C_{ss}^{-1}
               +C_{uu}\mathcal R_QC_{ss}^{-1},\qquad
 \|\mathcal R_o\|
       \le{\tau+\|\mathcal R_Q\|\over1-\tau}.
 \tag{QN.45}
$$

The table's first outgoing coefficient gives the strict
old-root bounds $.453$ and $4.129$.
All other frame input/output changes cost at most
$(1+3\tau)(1+4\tau)<1.00001$.
Multiplying all entries of the two tables by $1.00001$
is also sufficient for their old-frame versions, including
the additive first reflection term in (QN.45).
For this last term use $\tau<1.2\,10^{-6}$ and either
displayed new reflection upper $r>.45$; then
$(\tau+r)/[(1-\tau)r]<1.000004<1.00001$.
The physical raw-state and outer rows need only the input
conversion, so the same factor safely covers them.

There is no new normalization of low193, its source units,
root97 or outer96. In particular a physical-density mean
is not inserted into a singular power of the nonzero
frequency $N$.

## QN9. The new infinite cross columns are retained with usable fees

Let $\Delta A=D_QF(Q_*+q)-D_QF(Q_*)$.
Its exact formula is PA.5 with $Q_c=Q_*$, $e=q$ and
the principal mean difference $\langle q_2\rangle$.
This formula includes all three ordered primitive words,
the actual mean-input rank and the complete output mean.

Only the fixed centre has degree32. The new $\Delta A$
can have infinitely many cross entries; its carrier is
not the old shell97--160. With the whole-positive products
$B=|\beta|\max(1,K)<6$ and $G=\gamma\max(1,K)<14$
already proved in [WP](R144-supplement-actual-whole-positive-raw-hybrid-fees.md),
use the centre's Euclidean-pair Wiener budgets from
[TH](R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md)

$$
 q_0=6.407,\quad q_\phi=5.438,\quad
 q_{1/3}=8.732,\quad q_{A,1}=q_0+q_\phi,\quad
 q_{\phi,1/3}=5.06q_\phi,\quad q_{\phi,1}=129q_\phi .
 \tag{QN.46}
$$

The component-sum assumption on $q$ controls its Euclidean-pair
norms as well, with factor one. The last two factors concern
only the known degree32 centre.
For the unknown, its required $A^{1/3},A^1$ derivative
norms follow directly from (QN.3).
Use $P$ for the original full head and $H=I-P$. The following
are complete raw physical operator bounds:

$$
 \begin{array}{c|c}
 \text{map}&\text{uniform upper bound}\\ \hline
 H\Delta AP:L^2\to H^{1/3}&84000\rho\\
 H\Delta AP:L^2\to H^{-2/3}&7662\rho\\
 P\Delta AH:L^2\to L^2&7725\rho\\
 P\Delta AH:H^{-1}\to L^2&6300000\rho\\
 P\Delta AP:L^2\to L^2&13038\rho .
 \end{array}
 \tag{QN.47}
$$

Here is a direct accounting. For the first row, drift,
local reaction, primitive and mean-rank coefficients are
bounded, after division by $\rho$, by

$$
 3072\,{B\over4}(2q_{1/3}+\rho)
 +8(3B)(2q_{1/3}+\rho)
 +4B(q_{1/3}+q_{\phi,1/3}+\rho)+G<84000 .
 \tag{QN.48}
$$

The low derivative is at most384 and its $H^{1/3}$ weight
below8. The complete primitive still costs $1/4$, even
when its intermediate mode is low. For the second row
one may use the stronger ordinary $L^2$ output:

$$
 384\,{B\over4}(2q_0+\rho)
 +3B(2q_0+\rho)+{B\over2}(q_0+q_\phi+\rho)+G<7662 .
 \tag{QN.49}
$$

For high input, the radial principal change is diagonal
and has zero cross projection; the input mean is zero,
so its mean-input rank vanishes. Integrating the scalar
drift once against the actual low test function gives
the two drift fees $B(2q_0+\rho)$ and
$384(B/4)(2q_0+\rho)$. This yields

$$
 B(2q_0+\rho)\,97
       +3B(2q_0+\rho)+{B\over2}(q_0+q_\phi+\rho)<7725 .
 \tag{QN.50}
$$

For $H^{-1}$ input the same full adjoint is estimated
in $H^1$, with the low $H^1$ multiplier below385.
Its coefficient norms use $q_{A,1},q_{\phi,1}$, giving

$$
 385\{B(2q_{A,1}+\rho)\,97
       +3B(2q_{A,1}+\rho)+{B\over2}(q_{A,1}+q_{\phi,1}+\rho)\}
                                                   <6300000 .
 \tag{QN.51}
$$

This includes the adjoint of both ordered primitive
factors. It does not cut the high input to a finite shell.
For the low-to-low row add the principal mean fee
$G\rho\,384$ to (QN.49); the total is below $13038\rho$.

Two specifically nonzero new mean paths can be displayed.
Because the centre pairs exactly to zero against a high input,
the actual high-to-moving-mean row is

$$
 \pi_m\Delta AH
   =-2\beta m_Q\langle q_1h_1+Kq_2h_2\rangle,
 \quad
 \|\pi_m\Delta AH\|_{L^2\to\mathbb R},
 \ \|\pi_m\Delta AH\|_{H^{-1}\to\mathbb R}<77\rho .
 \tag{QN.52}
$$

The $H^{-1}$ bound uses the actual $A^1$ norm of $q$,
not a finite-band input. For a constant moving-mean
input, (QN.49) without its derivative term gives

$$
 \|H\Delta A\iota_m\|_{\mathbb R\to L^2}
 <\{18(2q_0+\rho)+3(q_0+q_\phi+\rho)+14\}\rho
 <281\rho .
 \tag{QN.53}
$$

This includes all polynomial and primitive terms as well
as $\gamma Jq_\phi$. Neither mean path is declared zero.

To combine with the old low Green, a low input still
enters as $\Delta A_{HL}S_i^{-1}$ or
$\Delta A_{LL}S_i^{-1}$; multiply its raw fee by
$\max(1,q_i^{-1})$. A high return enters as its raw
$\Delta A_{LH}$. The output weight is already inside
$\mathcal O G_L$, and is not applied to the raw source
a second time. Original atom identity blocks, exact
$S_+S_-^{-1}$ jump transmission, point receivers and
both boundary observations remain unchanged.

The actual high inverse QN1--QN8, the complete centre
fees WP and the new infinite fees (QN.47) are now
available for the full coupling argument. They do not
assert its smallness or remove the independent physical
finite rows. In particular the single-high tame
Hessian of TH and the present $A^3$ background
inverse have different roles; an $A^0$ remainder
bound alone does not establish membership in (QN.3).
