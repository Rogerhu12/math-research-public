# R133 supplement: directed analytic matrix budgets for the complete old-circle remainder

2026-11-14, phase_inverse.

**Proved operator norm identities and a new numerical recipe.**
The actual complete source bounds in
[the first old-circle calculation](R133-supplement-actual-leading-old-circle-remainder-sources.md)
are large because a third angular moment is charged repeatedly to
intermediate factors. Here each entire operator product is first
bounded in a complete Fourier matrix algebra. Its Sobolev conversion
is charged only at the end. No input or output block is deleted.

The scalar consumer reads the original 1328 completed norm rows and
the same complete root/forcing/seam natives. It evaluates new matrix
costs only. It does not recompute a target, a response, a ray,
an amplitude or an already saved coefficient row.

## 1. Complete exponential matrix algebra

Use the same fourfold modes and physical weights
$\Lambda_j=(1+16j^2)^{1/2}$, including mode zero.
For a matrix $K=(K_{mn})_{m,n\in\mathbb Z}$ define

$$
 \|K\|_{\sigma,\mathrm{mat}}=
 \max\left\{
 \sup_m\sum_n e^{4\sigma|m-n|}|K_{mn}|,
 \sup_n\sum_m e^{4\sigma|m-n|}|K_{mn}|
 \right\}.
 \tag{M.1}
$$

Use the complete complex Fourier matrices of the displayed coefficient
operators, with the nonmean inverses extended by zero only in their
mean row and column. Do not insert an even/odd reflection projection
inside (M.1): its antidiagonal need not have finite exponential lag
norm. The original parity restrictions are imposed only after the
complete estimates, where their Sobolev norms are at most one.
Below the actual contraction constructs a full nonmean extension of
$J$; its restriction agrees with the original parity inverse by
uniqueness.

The triangle inequality for $|m-n|$ proves the Banach algebra
inequality

$$
 \|AB\|_{\sigma,\mathrm{mat}}
 \le\|A\|_{\sigma,\mathrm{mat}}\|B\|_{\sigma,\mathrm{mat}}.
 \tag{M.2}
$$

For multiplication by an actual coefficient $f$ its matrix norm is
at most the complete Wiener norm $\|f\|_{\mathcal A_\sigma}$.
The fixed $P,\Pi$ have norm at most 1. The old primitive $I$ has

$$
 \|I\|_{\sigma,\mathrm{mat}}\le1/4,\qquad
 \|I\Lambda\|_{\sigma,\mathrm{mat}}
 =\|\Lambda I\|_{\sigma,\mathrm{mat}}\le C_I=\sqrt{17}/4 .
 \tag{M.3}
$$

Write $z_K,d_K,g_K$ for valid bounds respectively on
$\|K\|_{\sigma,\mathrm{mat}}$,
$\|[\partial_\phi,K]\|_{\sigma,\mathrm{mat}}$ and
$\|K\Lambda\|_{\sigma,\mathrm{mat}}$.
The last is a right one-gain bound and need not exist for a
general multiplication operator.
The entries of the commutator are exactly
$4i(m-n)K_{mn}$, so $d_K$ also bounds its entrywise absolute
lag moment.

For a product $AB$ sufficient bounds are

$$
 z_{AB}=z_Az_B,\qquad d_{AB}=d_Az_B+z_Ad_B,
 \tag{M.4}
$$

$$
 g_{AB}\le z_Ag_B
 \quad\hbox{when }g_B\hbox{ is available},\qquad
 g_{AB}\le g_Az_B+z_Ad_B
 \quad\hbox{when }g_A,d_B\hbox{ are available}.
 \tag{M.5}
$$

If both alternatives are available their minimum is valid.
The second follows from
$AB\Lambda=A\Lambda B+A[B,\Lambda]$ and
$|\Lambda_m-\Lambda_n|\le4|m-n|$.
One must not commute $\Lambda$ through a multiplier without
the second term. Sums and scalar multiples use their full
triangle bounds. An unavailable derivative/gain remains
unavailable; it is not replaced by zero.

## 2. Complete old rank maps and the true inverse

For $T_f=PM_fP$ let $f_0,f_1$ bound the complete
$\mathcal A_\sigma$ norms of $f,f_\phi$. Then
$z_{T_f}\le f_0$, $d_{T_f}\le f_1$.
A valid nonmean bound is

$$
 f_P=\min(f_0,f_1/4).
 \tag{M.6}
$$

For the complete old rank map $R_{f,g}=PM_f\Pi M_gP$,

$$
 z_{R_{f,g}}\le f_Pg_P,\qquad
 d_{R_{f,g}}\le f_1g_P+f_Pg_1,\qquad
 g_{R_{f,g}}\le C_I f_Pg_1 .
 \tag{M.7}
$$

Indeed its entries are $\widehat f(m)\widehat g(-n)$ for
$m,n\ne0$. The exponential weight is bounded by the product of
the two single-index weights. In the last inequality use
$\Lambda_n\le C_I|4n|$. Thus true constant factors vanish from
the rank map, while every nonmean Fourier coefficient remains.

For the same actual angular inverse
$A=\eta\partial_\phi+L$, $J=A^{-1}$, suppose the original row
at width $\sigma$ proves

$$
 c_\sigma={L_0\over4\eta_-}<1,\qquad
 \|L\|_{\sigma,\mathrm{mat}}\le L_0,\quad
 \|[\partial_\phi,L]\|_{\sigma,\mathrm{mat}}\le L_1 .
 \tag{M.8}
$$

The complete original root row already supplies these Wiener
bounds for the displayed coefficients. They apply to the full
nonmean complex Fourier matrix. Thus the same contraction constructs
an inverse there, and the Neumann identity is

$$
 J=(1+IL/\eta)^{-1}I/\eta .
$$

Consequently

$$
 z_J\le {1\over4\eta_-(1-c_\sigma)},\qquad
 g_J\le {C_I\over\eta_-(1-c_\sigma)},\qquad
 d_J\le z_J^2L_1 .
 \tag{M.9}
$$

For $d_J$ use $[\partial_\phi,J]=-J[\partial_\phi,L]J$.
Equation (M.9) is a bound for the complete Fourier matrix;
it is stronger information than an isolated scalar Wiener
operator norm. Its proof uses the convolution envelopes of
the actual $L$, so it applies to both row and column sums.
It is not a diagonal inverse. The independently retained old mean
equation is not part of this nonmean inverse.

## 3. One Sobolev conversion after the entire product

For $s>0$ define

$$
 \kappa_s(\sigma)=
 \sup_{x\ge0}(1+x)^s e^{-\sigma x}
 =
 \begin{cases}
  e^\sigma\{s/(e\sigma)\}^s,&0<\sigma\le s,\\
  1,&\sigma\ge s .
 \end{cases}
 \tag{M.10}
$$

The complete ratio satisfies
$\Lambda_n/\Lambda_m\le1+4|m-n|$. Thus the ordinary Schur
test gives

$$
 \boxed{\quad
 \|K\|_{H^{-8/3}\to H^{-5/3}}
 \le\kappa_{5/3}(\sigma)\,g_K .\quad}
 \tag{M.11}
$$

The weighted entry is
$(K_{mn}\Lambda_n)(\Lambda_n/\Lambda_m)^{5/3}$.
There is a single conversion (M.11) after the whole product;
a separate $\kappa$ is not paid at every multiplication.
Output mode zero is explicitly included. Applying $\Pi$
after this map costs at most one and gives the same bound
for the scalar mean.

The widths used by the consumer are $1/16,1/32,1/64$.
A width is usable only where its actual original (M.8) passes.
Each product is formed entirely at that one width. Only after
(M.11) is applied may independent valid bounds for the same
actual operator be minimized across widths.

## 4. Exact complete operator words to be evaluated

All notation and signs in this section are those of
[U.1--U.19](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md).
Set $c=-2b$, $c_B=-2bK$ and retain the exact words

$$
 \begin{gathered}
 N_A=cT_{v_\phi}IT_u,\quad N_C=cT_{u_\phi}IT_v,\quad
 N_E=cT_{u_\phi}IT_u,\quad N_B=c_BT_{v_\phi}IT_v,\\
 L=T_\ell+N_A,\qquad B=T_{b_0}+N_B .
 \end{gathered}                                         \tag{M.12}
$$

The exact commutator word is

$$
 \mathcal C(p,q)=
 (T_{dp_\phi}-R_{p,d_\phi})IT_q+
 T_pIT_{d_\phi}T_q+
 T_pI(T_{dq_\phi}-R_{q,d_\phi}).
 \tag{M.13}
$$

It can be evaluated directly with (M.4)--(M.7). In particular
the projected multiplier products are kept as products;
they are not incorrectly identified with multiplication by
an unprojected scalar product.

The complete remainders are

$$
\begin{split}
 S_{AC}={}&c\eta\{-R_{u_\phi,v}
       +T_{u_{\phi\phi}}IT_v+R_{v_\phi,u}
       +T_{v_\phi}IT_{u_\phi}\}\\
 &-R_{\ell,\ell}+T_\ell N_C+N_AT_\ell+N_AN_C,\\
 S_Q={}&(N_A)_r-c\mathcal C(v_\phi,u)
       +R_{\ell,d_\phi}-c\eta R_{u_\phi,u}
       +c\eta T_{u_{\phi\phi}}IT_u\\
 &-R_{\ell,e}+R_{t_Q,\ell}
       +T_\ell N_E+N_AT_e+N_AN_E-T_{t_Q}N_A,\\
 R_Q={}&T_{r_Q}+S_Q,\\
 S_V={}&-R_{t_Q,b_0}-R_{b_0,d_\phi}
       +T_{t_Q}N_B+R_QJB-(N_B)_r\\
 &+c_B\mathcal C(v_\phi,v)-KS_{AC}.
\end{split}                                            \tag{M.14}
$$

Radial derivatives in $(N_A)_r,(N_B)_r$ keep all three
Leibniz terms, including $b_r$ and $(bK)_r$. The actual
first radial derivatives and all angular derivatives needed
here are already contained in the completed forcing rows.
No fourth radial derivative is introduced.

Every term of $S_Q,S_{AC},S_V,R_QJ,R_QJL$ has an available
right one-gain bound from (M.3)--(M.9). For example,

$$
 g_{R_QJL}\le z_{R_Q}(g_Jz_L+z_Jd_L),\qquad
 g_{R_QJB}\le z_{R_Q}(g_Jz_B+z_Jd_B).
 \tag{M.15}
$$

These inequalities are evaluated before the sole conversion
(M.11). The previous product of three independently converted
negative-Sobolev norms is not used.

## 5. Full leading nonlocal source and independent mean

Use the actual amplitude columns and exact functions of U.14:

$$
 h=\eta^{-1}H^{-1}H_Dw,\quad y=H^{-1}(vH_Dw),\quad
 g_d=Dw-\eta h_\phi,\quad q_v=vDw-y_\phi .
 \tag{M.16}
$$

Let $\mathscr B,\mathscr A,M_0,M_D$ be the already proved
complete amplitude bounds in U.20--U.23, with the same
density normalization $n^{7/6}$ and full output. Their
values may be reused unchanged from the earlier recipe.

The exact source difference contains
$\mathsf E_D=\mathsf T(g_d)-L\mathsf T(h)$.
Thus its contribution is evaluated as the two complete
operator products

$$
 R_QJ\mathsf E_D
       =R_QJ\mathsf T(g_d)-R_QJL\mathsf T(h).
 \tag{M.17}
$$

For each complete operator $K$ below write
$\widehat g_K=\min_\sigma\kappa_{5/3}(\sigma)g_K$,
using only actual admissible widths. A complete first-row
scalar bound is

$$
\begin{split}
 \mathfrak N(w)={}&
 \widehat g_{S_V}\mathscr B(w)
 +\widehat g_{S_Q}\mathscr B(h)
 +\widehat g_{R_QJ}\mathscr B(g_d)
 +\widehat g_{R_QJL}\mathscr B(h)\\
 &+\widehat g_{c_BT_{v_\phi}I}\mathscr B(q_v)
 +\|Pr_Q\|_0M_0(h)
 +|c_B|\|v_\phi\|_0M_0(y)\\
 &+\{|c_B|\|v_\phi\|_0\|Pv\|_0/4+\|PT_0\|_0\}M_D(w)
 +\|PV_0\|_0M_0(w).
\end{split}                                             \tag{M.18}
$$

A previously proved larger full coefficient norm may replace
a $P$-norm in this formula. The final actual
$J:H^{-5/3}\to H^{-2/3}$ cost multiplies $\mathfrak N(w)$.
The source does not commute the high projection through $J$.

For the independent even mean, form the complete words
$\Pi M_uJ$, $\Pi M_uJL$, $\Pi M_uJB$ in the same algebra.
Because $J$ already has nonmean output, $\Pi M_u$ here is
the complete scalar functional on that output; its norm
and commutator bounds are no greater than those for $M_u$.
The mean equation is bounded by

$$
\begin{split}
 \mathfrak M(w)=2|bm|\big[&
 M_0(uh)
 +\widehat g_{\Pi M_uJ}\mathscr B(g_d)
 +\widehat g_{\Pi M_uJL}\mathscr B(h)\\
 &+\widehat g_{\Pi M_uJB}\mathscr B(w)
 +|K|M_0((v-m)w)\big].
\end{split}                                             \tag{M.19}
$$

This is precisely the full expansion of U.29. Neither a
radially moving mean nor a mean-free replacement for $v$
has been substituted into the original equation.

## 6. Actual numerical use and scope

Each new matrix row refers to the exact original common-row
identity. The new native saves all usable widths and their
operator triples, all unavailable width gates, the final
componentwise valid minima, and every completed source
integration. A resume accepts only the same source, manifest
and complete original native identities.

The unchanged amplitude and radial envelope recipe B.4--B.5
then bounds the new complete first/mean source by
$|\rho|^{-1/4}$ times its row constant. Both sides of the
uncertain root bracket are charged separately. The negative
Cauchy/primitive gain and the exact positive collar/body
split are taken from their original actual receipts.

This theorem proves the new norm recipe. Numerical improvement
or smallness requires its public directed execution. The
local $\mathcal L_0w_1$, later full amplitudes, complete
positive low/mean response, return cutoff and nonlinear
branch remain separate until actually paid.
