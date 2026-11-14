# R133 supplement: exact old-mean compression and complete nonlocal budgets for the first correction

2026-11-14, visible-exact / root.

**Proved identities and two complete norm recipes.** The old-angle mean
of the raw radial derivative is exactly the mean of the already
retained inverse defect. This combines terms before absolute values
are taken. It does not remove the independent even-mean equation.

For the first correction, its actual factor $n^{-1}$ also permits a
direct density-$n^{1/6}$ estimate. This needs fewer amplitude angular
derivatives than first promoting the amplitude to density $n^{7/6}$
and then paying an input-cutoff factor. Both estimates are valid; their
minimum may be used after each has been paid completely.

Numerical values require a new public directed consumer. No old target,
coefficient matrix row, successful fold, or physical seam is to be
recomputed or redefined.

## 1. The exact mean identity is on the original circle

Use all definitions of
[the complete old-circle identities](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md),
(U.1)--(U.19), and
[the directed matrix algebra](R133-supplement-directed-analytic-matrix-old-circle-remainders.md),
(M.1)--(M.19). In particular
$\Pi$ is the original mean at fixed physical $r$,
$P=1-\Pi$, $D=\partial_r-d\partial_\phi$, and $n=4|j|$.

For any admissible two-component amplitude $w=w_\epsilon$ set
$$
 h=\eta^{-1}H^{-1}H_Dw,\qquad
 y=H^{-1}(vH_Dw),\qquad
 g_d=Dw-\eta h_\phi,\qquad q_v=vDw-y_\phi .
 \tag{Y.1}
$$
All factors have their complete original parameter dependence.
The same $H,H_D$ and actual inverse $H^{-1}$ occur on both sides.

The two exact Airy derivative rules give
$$
 \begin{aligned}
 D\mathcal U_{n,\epsilon}(w)
     &=\mathcal U_{n,\epsilon}(nH_Dw+Dw),\\
 \partial_\phi\mathcal U_{n,\epsilon}(\eta h)
     &=\mathcal U_{n,\epsilon}(nH\eta h+\eta h_\phi).
 \end{aligned}
$$
Here $\eta_\phi=0$ is its original radial-scalar identity, and
$H\eta h=H_Dw$. Subtracting therefore proves
$$
 \boxed{\quad
 D\mathcal U(w)-\partial_\phi\mathcal U(\eta h)
                  =\mathcal U(g_d),\qquad
 \Pi D\mathcal U(w)=\Pi\mathcal U(g_d).
 \quad}
 \tag{Y.2}
$$
The second equality uses periodicity of the complete output at fixed
old $r$. It does not commute $D$ with $\Pi$:
$\Pi(d\,\partial_\phi f)$ need not vanish. It also does not replace
the old mean by the canonical $X$-mean.

The same identity holds after summing any common scalar input weights,
in particular the two original densities
$$
 \mathsf S_\rho(w)c=\sum_j n^{1/6}\mathcal U_{n,\epsilon}(w_\epsilon)c_j,
 \qquad
 \mathsf T_\rho(w)c=\sum_j n^{7/6}\mathcal U_{n,\epsilon}(w_\epsilon)c_j.
 \tag{Y.3}
$$
Here $D$ differentiates the column map with its input coefficients
fixed. It applies to the actual reflected parity combination. Signed
complex columns are retained until that combination is made.

## 2. The canceled fold expressions apply to every amplitude

By the already proved
[ordered fold cancellation](R133-supplement-exact-fold-matrix-cancellation-and-leading-inverse-defect.md),
$$
 H^{-1}H_D=-i\epsilon Q\,\mathsf K(T),\qquad
 \mathsf K(T)=\begin{pmatrix}0&T\\1&0\end{pmatrix}.
$$
Consequently (Y.1) has the exact alternative form
$$
 \begin{aligned}
 h&=-i\epsilon\,\frac Q\eta\,\mathsf K(T)w,\\
 y&=-i\epsilon\,vQ\,\mathsf K(T)w,\\
 g_d&=Dw+i\epsilon\,\partial_\phi\{Q\mathsf K(T)w\},\\
 q_v&=v g_d+i\epsilon\,v_\phi Q\mathsf K(T)w .
 \end{aligned}
 \tag{Y.4}
$$
These are matrix identities with the displayed order, including the
derivative of $T$ in $\partial_\phi\mathsf K(T)$.
They hold for $w_0$ and for the genuine $w_1$ separately.
The special leading-amplitude cancellation in the four terms of
$\zeta_\epsilon$ is not asserted for an arbitrary $w_1$.

In particular the last mean in the full primitive identity (U.15)
and in (U.17), originally written as $\Pi\mathcal U(W)$ with
$W=nH_Dw+Dw$, equals $\Pi\mathcal U(g_d)$. Its coefficient is still
the actual vector $T_{v_\phi}I(Pv)$ multiplying a scalar. It is not
$IT_v$ acting on a constant and is not zero.

## 3. A sharper complete mean entry at the old density

Let $\mathscr A_\rho$ be the complete real Airy operator bound used
in (U.20)--(U.23), and put
$\mathfrak D w=\partial_\phi(H^{-1}w)$.
The existing exact derivative identity gives
$$
 \Pi\mathsf T_\rho(w)=-\Pi\mathsf S_\rho(\mathfrak D w).
$$
Applying it after (Y.2) yields
$$
 \boxed{\quad
 \Pi D\mathsf T_\rho(w)
      =-\Pi\mathsf S_\rho(\mathfrak D g_d).
 \quad}
 \tag{Y.5}
$$
Thus a valid replacement for the former separate raw-derivative mean
cost is
$$
 \widetilde M_D(w)=
 \min\left\{
 M_1(H_Dw)+M_0(Dw),\;
 \mathscr A_\rho(\mathfrak D g_d)
 \right\}.
 \tag{Y.6}
$$
The first alternative is the original valid cost and remains valid.
The second is exactly $M_0(g_d)$ in the notation of (U.23).
The minimum is taken only after both full bounds have been obtained.

Replace $M_D(w)$ by $\widetilde M_D(w)$ in the single bracket where
it occurs in (M.18), or in (U.27). Every other term, the whole
$R_QJ$ and $R_QJL$ words, all old projections, and the final
$J:H^{-5/3}\to H^{-2/3}$ window remain unchanged.
This is a possible improvement even for the already computed leading
amplitude. It does not assert a numerical improvement before evaluation.

## 4. Direct density for the actual first correction

The first corrected trial is $w_0+n^{-1}w_1$ on the original
input columns. The nonlocal part is linear in $w$ for the fixed
background, so its $w_1$ contribution has density
$n^{7/6}n^{-1}=n^{1/6}$ exactly.

Work on the real negative source window where the previously proved
$\mathscr A_\rho$ theorem applies, with the original complete
$H^{-4/3}$ input and all output Fourier modes retained.
Write
$$
 A(w)=\mathscr A_\rho(w),\qquad
 \|\mathsf S_\rho(w):H^{-4/3}\to H^{-5/3}\|\le A(w).
 \tag{Y.7}
$$
No corresponding unweighted growing Airy estimate on the positive
side is inferred from (Y.7). Positive collar/body conversion continues
to use its own original complete weighted contract.

For a complete operator word $K$, let $z_{K,\sigma}$ be an actual
bound in the full exponential row-and-column algebra (M.1).
The same Schur argument as (M.11), with no extra gain, gives
$$
 Z_K:=\min_{\text{admissible }\sigma}
       \kappa_{5/3}(\sigma)z_{K,\sigma},
 \qquad
 \|K:H^{-5/3}\to H^{-5/3}\|\le Z_K.
 \tag{Y.8}
$$
Indeed the weighted entry is
$K_{mn}(\Lambda_n/\Lambda_m)^{5/3}$, including $m=0$.
Each complete product must first be evaluated at a single admissible
width. Only final bounds for that same operator may be minimized
across widths. Missing $z$ data are unavailable, not zero.

The old matrix contraction constructs the same full nonmean
extension of $J$, which agrees on the proved parity space by
uniqueness. Equation (Y.8) does not give $J$ an inverse on a constant
mode. The independent mean equation is handled separately below.

For the rest of the proof $w=w_1$ and $h,y,g_d,q_v$ mean (Y.1).
The inverse reconstruction becomes
$$
 J D_0P\mathsf S_\rho(w)
 =P\mathsf S_\rho(h)+J E_1,\qquad
 E_1=P\mathsf S_\rho(g_d)-L P\mathsf S_\rho(h).
 \tag{Y.9}
$$
Moreover (Y.2) gives
$\Pi D\mathsf S_\rho(w)=\Pi\mathsf S_\rho(g_d)$.
This equality is available before any operator norm is taken.

## 5. All nine nonlocal terms and the independent mean

Use complete coefficient Wiener $\mathcal A_0$ bounds denoted
$\|f\|_0$; these also bound the actual $L^\infty$ and normalized
$L^2$ coefficient norms.
With $c_B=-2bK$, a complete direct scalar source bound is
$$
 \begin{aligned}
 N_S(w)={}&
 Z_{S_V}A(w)+Z_{S_Q}A(h)
 +Z_{R_QJ}A(g_d)+Z_{R_QJL}A(h)\\
 &+Z_{c_BT_{v_\phi}I}A(q_v)
 +\|Pr_Q\|_0A(h)+|c_B|\|v_\phi\|_0A(y)\\
 &+\bigl\{|c_B|\|v_\phi\|_0\|Pv\|_0/4
                         +\|PT_0\|_0\bigr\}A(g_d)
 +\|PV_0\|_0A(w).
 \end{aligned}
 \tag{Y.10}
$$
This is exactly (U.17)--(U.19) at density $\mathsf S$, using
(Y.2) for their raw derivative mean. It has not removed a rank
term or projected the output high. In the scalar-mean terms,
$\|\Pi f\|\le\|f\|_{H^{-5/3}}$ and
$\|a\|_{H^{-5/3}}\le\|a\|_{L^2}$ justify the stated constants.

After the actual final inverse window,
$$
 \|\text{first original-row nonlocal source}\|_{H^{-2/3}}
       \le C_{J,-}N_S(w).
 \tag{Y.11}
$$
For the zero-mean reconstructed trial
$h_2=P\mathsf S_\rho(w)$,
$h_1=J(D_0-B)P\mathsf S_\rho(w)$, the original independent
even-mean residual is still
$2bm\langle u h_1+K(v-m)h_2\rangle$.
Its complete direct bound is
$$
 \begin{aligned}
 M_S(w)=2|bm|\bigl[&
 A(uh)+Z_{\Pi M_uJ}A(g_d)
 +Z_{\Pi M_uJL}A(h)\\
 &+Z_{\Pi M_uJB}A(w)+|K|A((v-m)w)\bigr].
 \end{aligned}
 \tag{Y.12}
$$
Here $\langle u\rangle=0$ and $\langle v-m\rangle=0$ are the
original coefficient identities. They permit moving $P$ across
these two scalar pairings; they do not erase the even-mean source.
A separately supplied mean has its original additional source ports.

The $A$ evaluations in (Y.10)--(Y.12) require two old angular
derivatives of their displayed amplitudes. By (Y.4), it is sufficient
to know $w$ through three old angular derivatives and $w_r$ through
two, together with the corresponding complete coefficient and fold
jets. There is no need here for four angular derivatives of
$H_Dw$ or for a third angular derivative of an Airy profile.
Any uncomputed amplitude angular derivative must still be paid by
a genuine positive strip margin.

## 6. The independent input-cutoff bound remains available

Let $|j|\ge J_0\ge1$ and $n=4|j|$. The input multiplier $n^{-1}$
commutes with the input Sobolev weights and has exact norm at most
$(4J_0)^{-1}$. Let $\widetilde N_T(w)$ be the complete old
density-$\mathsf T$ source bound (M.18) with (Y.6), and let
$M_T(w)$ be the complete old (M.19).
Then another fully valid pair of bounds for the same first correction
is
$$
 \begin{aligned}
 \|\text{first-row nonlocal source}\|_{H^{-2/3}}
       &\le \frac{C_{J,-}}{4J_0}\widetilde N_T(w),\\
 \|\text{independent even-mean source}\|
       &\le\frac1{4J_0}M_T(w).
 \end{aligned}
 \tag{Y.13}
$$
This multiplier acts only on the original input columns. It is not
moved through the output old inverse or through a full mean map.
Consequently the actual available pointwise bounds may be chosen as
$$
 \begin{aligned}
 C_{\mathrm{nl},1}(\rho)&=
 C_{J,-}\min\{N_S(w),\widetilde N_T(w)/(4J_0)\},\\
 C_{\mathrm{mean},1}(\rho)&=
 \min\{M_S(w),M_T(w)/(4J_0)\}.
 \end{aligned}
 \tag{Y.14}
$$
Each alternative remains separately recorded. A smaller unavailable
quantity may not be inserted as if it had been certified.

## 7. Original radial measure, seams and remaining obligations

All identities are on each original real piece and use one-sided
values at original seams. The analytic inner and strict exterior
bounds describe the same first correction by the already proved
[D1--D24 overlap identity](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md).
Choosing the better bound does not introduce a partition of unity,
a new trial or an artificial interface source.

Where the complete source envelope has the form
$C|\rho|^{-1/4}$, its squared integral on a one-sided interval of
length $R$ is at most $2C^2\sqrt R$ in the actual radial measure.
The uncertain true root must be retained in all original partition
intersections. Root point singularities of an upper envelope do not
authorize a pointwise statement about an infinite norm of the actual
analytic source.

A consumer can reuse the complete coefficient operator triples and
their admissible-width gates from the original 1328-row matrix native.
Only missing actual amplitude evaluations, the new mean combination
and the resulting source integrals are new mathematics. All accepted
old leading amplitudes, fold domains, matrix words, original positive
weights and genuine 1079 seam sources remain unchanged.

The local $n^{-1}\mathcal L_0w_1$, strict exterior derivative budget,
positive low/mean response, true finite-head feedback and complete
return composition are separate terms. Equations (Y.2)--(Y.14)
provide their missing nonlocal/mean interface; they do not by
themselves prove a small global strong return, cutoff-97 inverse
or nonlinear PDE branch.
