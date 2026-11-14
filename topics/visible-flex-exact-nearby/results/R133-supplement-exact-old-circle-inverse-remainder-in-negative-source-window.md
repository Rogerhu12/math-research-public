# R133 supplement: exact old-circle inverse remainders in the complete negative source window

2026-11-14, phase_inverse.

**Proved identities and a finite norm recipe.** On every original open
radial piece this isolates the entire difference between the complete
ordered scalar operator and its retained Airy degree-zero expression.
It retains the old mean, both projections and the complete inverse $J$.
Its norm recipe uses the already certified real Airy two-derivative
operator estimate and a further explicitly paid negative window of $J$.
It introduces no integration at fixed canonical $T$ and no radial
holomorphic continuation across an original seam.

The quantitative constants defined below still require their directed
consumer. This is not a numerical strong-return bound or a cutoff-97
inverse.

## 1. Exact projected algebra

Use [the ordered scalarization](R133-supplement-ordered-scalar-root-operator-and-one-gain-radial-remainder.md).
Set $\partial=\partial_\phi$, $P=1-\Pi$, $I=\partial^{-1}P$,
$D=\partial_r-d\partial$ and $\mathcal D=PM_d\partial P$.
All means and derivatives are at fixed old $r$. Put

$$
 T_f=PM_fP,\qquad R_{f,g}=PM_f\Pi M_gP,\qquad c=-2b,
 \qquad c_B=-2bK.                                      \tag{U.1}
$$

On the appropriate nonmean parity spaces, exact identities are

$$
 T_fT_g=T_{fg}-R_{f,g},\quad
 \partial T_f=T_f\partial+T_{f_\phi},\quad
 IT_f\partial=T_f-IT_{f_\phi},
$$

$$
 [\mathcal D,T_f]=T_{d f_\phi}-R_{f,d_\phi},
 \qquad [\mathcal D,I]=IT_{d_\phi}.                    \tag{U.2}
$$

For example $\Pi M_g\partial=-\Pi M_{g_\phi}$, so the two
apparently additional mean terms in the first commutator cancel
exactly, leaving the displayed rank term. No rank term is discarded.

For scalar $p,q$ define

$$
 \begin{split}
 \mathcal C(p,q)={}&
 (T_{d p_\phi}-R_{p,d_\phi})IT_q
 +T_pIT_{d_\phi}T_q\\
 &+T_pI(T_{d q_\phi}-R_{q,d_\phi}).
 \end{split}                                         \tag{U.3}
$$

Then $[\mathcal D,T_pIT_q]=\mathcal C(p,q)$. For a radial scalar
$\kappa$, the full radial derivative is

$$
 (\kappa T_pIT_q)_r
 =\kappa_rT_pIT_q+
   \kappa T_{p_r}IT_q+\kappa T_pIT_{q_r}.              \tag{U.4}
$$

These formulas keep coefficient derivatives rather than differentiating
an interval error or interchanging the original primitive with a
coordinate change.

Retain the original notation

$$
 \begin{gathered}
 \ell=-2buv,\quad e=-b(1+3u^2+Kv^2),\quad
 b_0=b(1-u^2-3Kv^2),\\
 N_A=cT_{v_\phi}IT_u,\quad N_C=cT_{u_\phi}IT_v,\quad
 N_E=cT_{u_\phi}IT_u,\quad N_B=c_BT_{v_\phi}IT_v,\\
 L=T_\ell+N_A,\quad B=T_{b_0}+N_B,\quad
 A=\eta\partial+L,\quad J=A^{-1},\\
 t_Q=\eta_r/\eta+d_\phi+e,\qquad T_0=t_Q+b_0 .
 \end{gathered}                                       \tag{U.5}
$$

The letter $b_0$ in these formulas is the local operator coefficient,
not an Airy amplitude.

## 2. All one-gain coefficient remainders, explicitly

Let $V_{AC}$ be the exact bounded term in
$AC=-\eta^2\partial^2+V_{AC}$.
Its local multiplier and exact remainder are

$$
 v_{AC}=\ell^2-4b\eta v u_\phi,\qquad
 V_{AC}=T_{v_{AC}}+S_{AC},                              \tag{U.6}
$$

$$
 \begin{split}
 S_{AC}={}&c\eta\{-R_{u_\phi,v}
       +T_{u_{\phi\phi}}IT_v+R_{v_\phi,u}
       +T_{v_\phi}IT_{u_\phi}\}\\
 &-R_{\ell,\ell}
       +T_\ell N_C+N_AT_\ell+N_AN_C .
 \end{split}                                         \tag{U.7}
$$

To check the signs, use
$\partial N_C=c(T_{u_\phi}T_v+T_{u_{\phi\phi}}IT_v)$
and
$N_A\partial=c(T_{v_\phi}T_u-T_{v_\phi}IT_{u_\phi})$.
The local terms combine with $\eta\ell_\phi$ to give
$-4b\eta v u_\phi$.

Write the exact (O.15) numerator as

$$
 R_Q=T_{r_Q}+S_Q,\qquad
 r_Q=D\ell+\eta e_\phi-2b\eta u_\phi u
                    -\ell(\eta_r/\eta+d_\phi).       \tag{U.8}
$$

Its entire remainder is

$$
 \begin{split}
 S_Q={}&(N_A)_r-c\,\mathcal C(v_\phi,u)
       +R_{\ell,d_\phi}
       -c\eta R_{u_\phi,u}
       +c\eta T_{u_{\phi\phi}}IT_u\\
 &-R_{\ell,e}+R_{t_Q,\ell}
       +T_\ell N_E+N_AT_e+N_AN_E-T_{t_Q}N_A .
 \end{split}                                         \tag{U.9}
$$

Here $-c\eta R_{u_\phi,u}=2b\eta R_{u_\phi,u}$.
In particular the radial derivative $(N_A)_r$ in (U.4) includes
$b_r,u_r,v_{\phi r}$.

The exact ordered coefficient is $Q=T_{t_Q}+R_QJ$.
Put

$$
 V_0=t_Qb_0-Db_0-Kv_{AC},\qquad V=T_{V_0}+S_V .
                                                               \tag{U.10}
$$

Since $[D_0,T_{b_0}]=T_{Db_0}+R_{b_0,d_\phi}$,
expanding $V=QB-[D_0,B]-KV_{AC}$ gives

$$
 \begin{split}
 S_V={}&-R_{t_Q,b_0}-R_{b_0,d_\phi}
       +T_{t_Q}N_B+R_QJB\\
       &-(N_B)_r+c_B\mathcal C(v_\phi,v)-KS_{AC}.
 \end{split}                                         \tag{U.11}
$$

Every summand of (U.7), (U.9) and (U.11) contains a true primitive,
a true inverse or an explicit smooth rank map. These are finite
equalities. They do not mean that any of those summands is zero.

## 3. Exact inverse reconstruction of the radial principal term

Use the genuine Airy amplitude map $\mathcal U_{n,\epsilon}(w)$,
$n=4|j|$, $\epsilon=\operatorname{sgn}j$, of
[the old-circle Airy calculus](R133-supplement-original-primitive-on-actual-Airy-amplitudes-and-exact-mean.md).
Write

$$
 H=i\epsilon X_\phi\,1+
        T_\phi\begin{pmatrix}0&T\\1&0\end{pmatrix},
 \qquad
 H_D=i\epsilon DX\,1+
        DT\begin{pmatrix}0&T\\1&0\end{pmatrix}.        \tag{U.12}
$$

Thus $\partial\mathcal U(w)=\mathcal U(nHw+w_\phi)$ and
$D\mathcal U(w)=\mathcal U(nH_Dw+Dw)$ exactly.
The certified fold gives an actual inverse $H^{-1}$.

For an arbitrary admissible amplitude pair $w$ set

$$
 f=P\mathcal U(w),\quad
 W=nH_Dw+Dw,\quad
 h=\eta^{-1}H^{-1}H_Dw,\quad
 y=H^{-1}(vH_Dw),
$$

$$
 E_D=P\mathcal U(Dw-\eta h_\phi)-LP\mathcal U(h).
                                                               \tag{U.13}
$$

Then the complete old inverse satisfies

$$
              JD_0f=P\mathcal U(h)+JE_D.             \tag{U.14}
$$

Indeed $A P\mathcal U(h)
=P\mathcal U(nH_Dw+\eta h_\phi)+LP\mathcal U(h)$,
so (U.14) follows by subtracting from $D_0f$ and applying
the genuine $J$. There is no symbol inverse remainder hidden in
(U.14).

The primitive part has the equally exact identity

$$
 \begin{split}
 N_BD_0f=c_B\{&
 P\mathcal U(v_\phi y)
 +T_{v_\phi}IP\mathcal U(vDw-y_\phi)\\
 &-P v_\phi\,\Pi\mathcal U(y)
 -T_{v_\phi}I(Pv)\,\Pi\mathcal U(W)\}.
 \end{split}                                         \tag{U.15}
$$

For its proof first move the inner projection:
$T_vP\mathcal U(W)=P\mathcal U(vW)-Pv\,\Pi\mathcal U(W)$.
Next use $\partial P\mathcal U(y)
=P\mathcal U(nvH_Dw+y_\phi)$ and $I\partial=P$.
Finally apply the outer multiplier. The vector $I(Pv)$ in the
last term acts on the old scalar mean; it is not $IT_v$ applied
to a mean and accidentally annihilated.

With

$$
 \vartheta=r_Q/\eta-2bKvv_\phi,
 \qquad R_{-1}=N_B+R_QJ,
$$

one obtains

$$
 R_{-1}D_0f=P\mathcal U(\vartheta H^{-1}H_Dw)
                         +\mathcal E_R(w),            \tag{U.16}
$$

$$
 \begin{split}
 \mathcal E_R(w)={}&S_QP\mathcal U(h)+R_QJE_D
       +c_BT_{v_\phi}IP\mathcal U(vDw-y_\phi)\\
 &-Pr_Q\,\Pi\mathcal U(h)
       -c_BP v_\phi\,\Pi\mathcal U(y)\\
 &-c_BT_{v_\phi}I(Pv)\,\Pi\mathcal U(W).
 \end{split}                                         \tag{U.17}
$$

This accounts for the entire old primitive and inverse at this
retained order, including all moving projections.

## 4. Complete difference from the degree-zero Airy operator

Let $\mathcal P_{\rm sc}$ denote the un-divided scalar operator
(O.20). The actual $\mathcal T_\epsilon$ and $\mathcal L_0$ are
those in [the explicit first-forcing proof](R133-supplement-explicit-first-Airy-forcing-and-real-radial-inverse-jets.md).
Then

$$
 \boxed{\quad
 \mathcal P_{\rm sc}P\mathcal U(w)
 =P\mathcal U\{\mu(n\mathcal T_\epsilon w+\mathcal L_0w)\}
                      +\mathcal N(w),\quad}           \tag{U.18}
$$

$$
 \mathcal N(w)=S_VP\mathcal U(w)-\mathcal E_R(w)
         +PT_0\,\Pi\mathcal U(W)-PV_0\,\Pi\mathcal U(w).
                                                               \tag{U.19}
$$

The notation $PT_0$ in the last line means the function
$P(T_0)$ multiplying a scalar, and similarly for $PV_0$.
It is not the projected operator $T_{T_0}$ applied to a constant.

For completeness $D_0^2P=P D^2$ because the removed old mean
has only a radial derivative, which the outer $P$ annihilates.
The projection error in $-T_{T_0}D_0f$ is
$+P(T_0)\Pi D\mathcal U(w)$; the error in $T_{V_0}f$ is
$-P(V_0)\Pi\mathcal U(w)$. These are exactly the two final terms
of (U.19). No derivative of a moving projection has been omitted:
$\Pi$ is the fixed old-angle mean at fixed $r$ throughout.

## 5. An exact derivative identity pays the additional frequency

For $|j|\ge J_0\ge1$ define the density-scaled column operators

$$
 \mathsf S_\rho(w)c=\sum_j n^{1/6}\mathcal U_{n,\epsilon}(w_\epsilon)c_j,
 \qquad
 \mathsf T_\rho(w)c=\sum_j n^{7/6}\mathcal U_{n,\epsilon}(w_\epsilon)c_j.
$$

The amplitude pairs may depend on $\epsilon$, with uniform bounds
for both signs. All outputs are retained. Let
$\mathscr A_\rho(w)$ be the explicit bound from
[the complete real Airy seam theorem, A.1--A.14](R133-supplement-complete-real-Airy-seam-operator-in-negative-source-window.md):
it bounds $\mathsf S_\rho(w):H^{-4/3}_{|j|\ge J_0}\to H^{-5/3}$.
It consumes just the first two old angular derivatives of $w$,
the real map bounds and the genuine Airy profile factors.
In this section $\rho\ne0$; the radial integrability at zero is
addressed below.

Put $\mathfrak D w=\partial(H^{-1}w)$. The exact derivative rule
gives

$$
 \boxed{\quad
 \mathsf T_\rho(w)
       =\partial\mathsf S_\rho(H^{-1}w)
                           -\mathsf S_\rho(\mathfrak D w).\quad}
                                                               \tag{U.20}
$$

Since $\partial:H^{-5/3}\to H^{-8/3}$ has norm at most 1, and
$H^{-5/3}$ embeds contractively in $H^{-8/3}$, a complete bound is

$$
 \mathscr B_\rho(w)
 =\mathscr A_\rho(H^{-1}w)+\mathscr A_\rho(\mathfrak D w).
                                                               \tag{U.21}
$$

This requires at most three angular derivatives of $H^{-1}w$.
It does not require a third derivative bound on an Airy
oscillatory profile or a stronger asymptotic expansion.

Taking the old mean in (U.20) gives two exact identities:

$$
 \Pi\mathsf T_\rho(w)=-\Pi\mathsf S_\rho(\mathfrak D w),\qquad
 \Pi\mathsf T_\rho(nw)=\Pi\mathsf S_\rho(\mathfrak D^2w).
                                                               \tag{U.22}
$$

Here multiplication by $n$ acts on the input columns and commutes
with $\Pi$. In the second equality apply the first identity
twice. Define

$$
 M_0(w)=\mathscr A_\rho(\mathfrak D w),\quad
 M_1(w)=\mathscr A_\rho(\mathfrak D^2w),\quad
 M_D(w)=M_1(H_Dw)+M_0(Dw).                            \tag{U.23}
$$

These bound the full means of $\mathsf T_\rho(w)$ and of its
raw $D$ derivative. The second requires at most four angular
amplitude derivatives. A derivative of the complete Fourier
output, not a replacement mean in $X$, is what has zero mean.

The physical frequency is exactly $n=4|j|$; no factor 4 is
absorbed into the cutoff or the Sobolev weights.

## 6. Complete coefficient norms and the additional J window

For a scalar coefficient define the complete Wiener moment

$$
 m_3(f)=\sum_{k\in\mathbb Z}(1+|4k|)^3|\widehat f(k)|,\qquad
 m_0(f)=\sum_k|\widehat f(k)|.
$$

For both $s=-8/3$ and $s=-5/3$, multiplication by $f$ has
$H^s\to H^s$ norm at most $m_3(f)$. Moreover

$$
 \|I\|_{H^s\to H^{s+1}}=C_I=\sqrt{17}/4,\quad
 \|I\|_{H^s\to H^s}=1/4,\quad
 \|R_{f,g}\|_{H^s\to H^{s+1}}\le m_3(f)m_3(g).
                                                               \tag{U.24}
$$

For the multiplier bound use
$\langle4m\rangle/\langle4n\rangle\le1+|4(m-n)|$.
For the rank map apply Cauchy--Schwarz to its scalar functional
and use $\|P f\|_{H^{s+1}}\le m_3(f)$ and
$\|P g\|_{H^{-s}}\le m_3(g)$.
These inequalities include the whole original angular circle.

The complete integer one-gain bounds saved as
$\mathtt{one\_gain}[k]=H_k$ in each actual root row apply to $J$
and its adjoint, by the angular commutator recursion and adjoint argument
in [complete moving-root scalarization](R133-supplement-complete-moving-root-scalarization.md),
(N.11)--(N.15).
Duality and interpolation therefore give the additional declared
window

$$
 C_J=H_1^{1/3}H_2^{2/3},\qquad
 \|J\|_{H^{-8/3}\to H^{-5/3}}\le C_J.                 \tag{U.25}
$$

It must be evaluated from the actual saved row. It is not inferred
from $J$'s ordinary $L^2$ norm. The previously declared
$H^{-5/3}\to H^{-2/3}$ factor will be denoted $C_{J,-}$.

Let $C_Q$ be the sum of the one-gain costs in (U.9), using
(U.3)--(U.4) and (U.24) on both of the stated $s$ windows.
Let $C_{AC}$ be the corresponding sum for (U.7), and put

$$
 C_R=m_3(r_Q)+C_Q,\quad
 C_L=m_3(\ell)+|c|m_3(v_\phi)m_3(u)/4,\quad
 C_B=m_3(b_0)+|c_B|m_3(v_\phi)m_3(v)/4.
$$

For $C_V$ sum (U.11) with (U.24), using $C_R C_J C_B$
for the $R_QJB$ term and $|K|C_{AC}$ for the last term.
This is a finite, unambiguous norm algorithm. An $I$ supplying
the gain costs $C_I$; any remaining $I$ may cost $1/4$.
There is no assumption that these complete constants are small.

Only original coefficient values, their first radial derivatives
and a finite number of angular moments occur. The latter can be
paid from the already certified wider angular strip and its saved
derivative norms. For example a missing angular moment of order
$q>p$ is bounded by
$\sup_{x\ge0}x^{q-p}e^{-\sigma x}\|\partial^p f\|_{\mathcal A_\sigma}$.
This does not manufacture a fourth or fifth radial intrinsic jet.

## 7. Explicit nonlocal residual and full mean-source costs

In the rest of this section all $\mathscr A,\mathscr B,M$ refer
to one fixed real radial circle. Define

$$
 E_*(w)=\mathscr B(Dw-\eta h_\phi)+C_L\mathscr B(h).
                                                               \tag{U.26}
$$

Then $E_*$ bounds the density-scaled $E_D$ into $H^{-8/3}$.
From the exact decomposition (U.17)--(U.19), a sufficient complete
$H^{-4/3}\to H^{-5/3}$ cost for $\mathcal N$ is

$$
 \begin{split}
 C_{\rm nl}(w)={}&
 C_V\mathscr B(w)+C_Q\mathscr B(h)+C_R C_J E_*(w)\\
 &+|c_B|m_3(v_\phi)C_I\mathscr B(vDw-y_\phi)\\
 &+m_0(r_Q)M_0(h)+|c_B|m_0(v_\phi)M_0(y)\\
 &+\{|c_B|m_0(v_\phi)m_0(v)/4+m_0(T_0)\}M_D(w)
      +m_0(V_0)M_0(w).
 \end{split}                                         \tag{U.27}
$$

The last two lines are genuine old-mean maps. In particular the
coefficient $T_{v_\phi}I(Pv)$ is bounded in ordinary $L^2$
by $m_0(v_\phi)m_0(v)/4$, and the embedding into $H^{-5/3}$
has norm at most 1.

For the exact reconstructed trial

$$
 h_2=P\mathcal U(w),\qquad
 h_1=J(D_0-B)P\mathcal U(w)
       =P\mathcal U(h)+J\{E_D-BP\mathcal U(w)\},
                                                               \tag{U.28}
$$

the nonlocal part of the first original-row residual has source
norm at most $C_{J,-}C_{\rm nl}(w)$ in $H^{-2/3}$.

The independent even mean residual of this zero-mean trial is
still exactly

$$
 g_2=2bm\langle u h_1+K(v-m)h_2\rangle .
$$

The reflection coefficient has $\langle u\rangle=0$, while
$\langle v-m\rangle=0$ by definition; these are coefficient
identities, not suppression of the independent mean equation.
Its complete density-input norm is bounded by

$$
 C_{\rm mean}(w)=2|bm|\left\{
 M_0(uh)+m_3(u)C_J[E_*(w)+C_B\mathscr B(w)]
                 +|K|M_0((v-m)w)\right\}.            \tag{U.29}
$$

For the middle term pair the $H^{-5/3}$ reconstructed error
with the actual coefficient $u\in H^{5/3}$. A constant output
has the same norm in all Bessel Sobolev spaces, so this is also
an $H^{-2/3}$ source cost. A nonzero independently supplied mean
has its additional original source ports; (U.29) is the residual
of this explicitly specified zero-mean trial.

The identities are used on the actual reflected parity combination.
Complex signed columns are only a device for computing and bounding
that combination. The complete $J$ is applied on its proved parity
domain after the old projections; it is not commuted through a
projection or extended to an unproved constant mode.

## 8. Radial use and the exact remaining scope

All norms in (U.21)--(U.29) are taken on original real radial
pieces, with one-sided traces at seams. On a fixed root window,
the complete coefficient and amplitude angular derivatives are
bounded. The real Airy factors from A.7--A.11 have at worst
$|\rho|^{-1/4}$ growth as $\rho\to0$; their logarithmic angular
derivatives remain bounded because $A>0$ and
$T=-\rho A^{2/3}$. The inverse point matrix $H^{-1}$ has a
uniform genuine gap at zero.

Thus the displayed source costs are locally square integrable
at the root. A bound $C|\rho|^{-1/4}$ contributes exactly at most
$2C^2\sqrt R$ to its squared radial norm over a one-sided interval
of length $R$. The root is not replaced by a floating centre,
and no pointwise estimate is claimed at the singular scalar
upper-envelope itself. Genuine source functions remain regular
through the original analytic root germ.

For $w=w_0$, this computes the complete finite old $I/J$ difference
from the already certified first-forcing expression without a new
target or higher radial intrinsic solve. For $w=w_0+n^{-1}w_1$,
linearity and the exact identities remain valid, but evaluating
them needs the actual derivative bounds of $w_1$ as well.
The local residual $n^{-1}\mathcal L_0w_1$, subsequent corrections,
cutoff sources, all genuine seams and positive endpoint conversion
are still separate. No full $C_E$, numerical cutoff-97 inverse or
nonlinear PDE branch follows merely from the finite formulas here.
