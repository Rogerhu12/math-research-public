# R133 supplement: exact radial cancellation of the genuine local source and negative-side reuse of completed Taylor budgets

2026-11-15, visible-exact / phase_inverse.

**Proved exact identities and a conditional scalar-consumer contract.** The first complete local residual can be written using the already completed correlated free numerator, without a separately bounded second derivative of the genuine first correction and without the large radial part of $c_T$. A second, independent bound evaluates the second local vector in the original physical variables. Both preserve the same trial, genuine columns, complete parameter squares, old-circle sources, means and interfaces. New numerical bounds, or any improvement of them, are not asserted before their public execution.

The primary identities are G.4--G.9 of [the ordered genuine sources](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), P.11 and P.17 of [the regular first-local reduction](R133-supplement-exact-first-local-vector-reduction-through-regular-transport.md), and the completed [free correlated numerator](R133-supplement-correlated-complete-local-numerator-from-old-radial-Taylor.md). The immutable original whole-piece output of run43669106351/1 contains the free numerator and free correction used below. Its mathematical process succeeded before a separate formatter failure; the independently published receipt run43671024244/1 preserves that distinction.

## 1. The same original amplitudes and operators

Fix the original physical root piece2549, the fixed intrinsic parameter eta_0, the complete allowed complex delta square, and the original complex square for $z=j^{-2}$. Let $n=4|j|$, $|j|\ge97$, $\epsilon=\operatorname{sgn}j$. Work first on one common analytic reference branch and use
$$
 E=E_{12},\qquad
 K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 J_+=\operatorname{diag}(1,-1),\qquad J_-=-J_+ .
 \tag{R.1}
$$
The sign $J_+$ in this paper is deliberately opposite to P.1's $J_-$. The scalar intrinsic curvature is $K_{\rm sc}$.

Retain the original leading amplitude and matrix
$$
 w_0=(a_0,b_0)^t,\qquad M=[w_0,Kw_0]=a_0I+b_0K.
$$
Write $w_1$ for the original free first correction and $w_1^V$ for the actual genuine first correction. They obey
$$
 w_1^V=w_1+\mathcal B(T)Kw_0,\qquad
 \mathcal B+2T\mathcal B'=V(T),\qquad
 \mathcal B(0)=V(0).
 \tag{R.2}
$$
Here every $V,\mathcal B$ and $T$ derivative is evaluated at the same actual canonical coordinate $T(r,\phi)$ and the same input label. A derivative with respect to the old $r$ is not substituted for a $T$ derivative.

Let $\mathfrak A^0$ be exactly G.6's raw local operator with $V=0$:
$$
 \mathfrak A^0 w
 =(D^2+\eta^2K_{\rm sc}\partial_\phi^2-T_0D+V_0)w
                    +i\epsilon\vartheta QKw,\qquad
 D=\partial_r-d\partial_\phi .
 \tag{R.3}
$$
Thus $\mathfrak A^V=\mathfrak A^0-\mu V$. Define
$$
 N_{\rm old}=\mathfrak A^0w_1,\qquad N_0=\mathfrak A^0w_0,
 \qquad f^V=(f_b^V,f_a)^t
     =M^{-1}(Vw_0-\mu^{-1}N_0).
 \tag{R.4}
$$
The order of the two normalized forcing components in (R.4) is fixed. These are the complete forcing functions whose signed Taylor coefficients were added before taking norms in the successful whole-reference computation. In particular
$$
 N_0=\mu(Vw_0-Mf^V).
 \tag{R.5}
$$
No division by $\mu$ is made in the final raw local source.

The required first two vectors are
$$
 L_1^V=\mathfrak A^V w_1^V-\mu E\{2Vw_{0,T}
                              +(V_T+c_TV)w_0\},
$$
$$
 L_2^V=-\mu E\{2Vw_{1,T}^V+(V_T+c_TV)w_1^V\}
                                      +\mathfrak R(w_0).
 \tag{R.6}
$$
The unchanged third vector is $\mathfrak R(w_1^V)$. Their input weights remain exactly $1,n^{-1},n^{-2}$, as in G.9.

## 2. Remove the radial connection before taking a norm

Put $\mathcal L=\mu^{-1}\mathfrak A^0$. Its differential part is
$\partial_T^2+T\partial_X^2+c_T\partial_T+c_X\partial_X$.
The remaining zeroth-order scalar and $K$ terms commute with $K$. Since $K_T=E$, one obtains
$$
 [\mathcal L,K]w=E(2w_T+c_Tw).
 \tag{R.7}
$$
Expanding $[\mathcal L,\mathcal B K]w_0$, without interchanging matrices, and using
$V=\mathcal B+2T\mathcal B'$ and
$V_T=3\mathcal B'+2T\mathcal B''$, gives
$$
 \begin{split}
 L_1^V={}&N_{\rm old}-\mu Vw_1^V+\mathcal B K N_0\\
 &+\mu\{2\mathcal B'KJ_+w_{0,T}
       +(\mathcal B''+c_T\mathcal B')KJ_+w_0
       -\mathcal B'Ew_0\}.
 \end{split}
 \tag{R.8}
$$
In this computation $K-2TE=KJ_+$. In particular the last term in (R.8) has a minus sign.

Let $\mathsf C=M_T+c_TM/2$ and $\Xi=c_X/T$, with its original removable root extension. The original leading intertwiner, not a new reference normalization, gives
$$
 \mathsf C=-i\epsilon KM_X-\frac{i\epsilon}{2}\Xi KM
                         +\frac{b_0}{2T}KJ_- .
 \tag{R.9}
$$
The identities
$$
 KJ_+K=-TJ_+,\qquad KJ_+KJ_-=TI,\qquad Ew_0=b_0e_1
$$
show that $2\mathcal B'KJ_+\mathsf Ce_1$ contains
$+\mathcal B'b_0e_1$. This cancels the last term in (R.8) exactly. Therefore
$$
 \boxed{\begin{split}
 L_1^V={}&N_{\rm old}-\mu Vw_1^V+\mathcal B K N_0\\
 &+\mu\{\mathcal B''KJ_+w_0+
      i\epsilon T\mathcal B'J_+(2w_{0,X}+\Xi w_0)\}.
 \end{split}}
 \tag{R.10}
$$
Neither $c_T$ nor $w_{0,T}$ remains in (R.10). No upper bounds have been subtracted to obtain this identity.

Using (R.2) and (R.5) also cancels the exact two occurrences of $\mu V\mathcal B Kw_0$:
$$
 \boxed{\begin{split}
 L_1^V={}&N_{\rm old}-\mu Vw_1-\mu\mathcal B KMf^V\\
 &+\mu\{\mathcal B''KJ_+w_0+
      i\epsilon T\mathcal B'J_+(2w_{0,X}+\Xi w_0)\}.
 \end{split}}
 \tag{R.11}
$$
This form uses the accepted free $w_1$, not a relabeling of the genuine correction. Explicitly,
$$
 KM f^V=
 \begin{pmatrix}
 T(b_0f_b^V+a_0f_a)\\
 a_0f_b^V+Tb_0f_a
 \end{pmatrix},\qquad
 KJ_+w_0=(-Tb_0,a_0)^t .
 \tag{R.12}
$$
All functions in these formulas include their complete amplitude means. An amplitude mean is not the independent physical even-mean source.

## 3. Only the actual negative cover is used

Keep the true root bracket $r_*\in[r_-,r_+]$ and the original physical piece $[a,b]$. The already integrated negative source is supported on
$$
 I_-=[a,r_+],\qquad
 a=\frac{2147184947341121}{9007199254740992},\qquad
 r_+=\frac{2383968743003}{10^{13}} .
 \tag{R.13}
$$
Set $h=r_+-a$. On this entire cover, including its one-sided uncertain-root charge,
$|r-r_*|\le h$. This is a restriction of the same original piece, not a new physical seam. The old full-piece radius remains
$$
 H=\frac{893368603925465506687}{21990232555520000000000000}.
$$
A consumer checks $0<h<H<1/8000<3/20000<3/8000$ exactly. It does not enlarge any old holomorphic disk or move the physical cut.

Restore the original whole-piece native, process and publication identities and the complete original natural rows. Select exactly the six negative rows, check their ordered cover of (R.13), their uncertain-root flag and their original radius-budget payload hashes. Read, for each such row, the accepted real-angle strip-sup jets
$$
 \|\partial_\phi^q N_{{\rm old},i}\|_\infty,\qquad
 \|\partial_\phi^q (w_1)_i\|_\infty,\qquad i=a,b,\quad0\le q\le2.
 \tag{R.14}
$$
These are the complete stored `complete_Nraw_derivative_budgets` and
`first_amplitude_budgets`, with width0. The full finite correlation and infinite tails in them are read verbatim. Taking their maximum over the six rows gives a uniform bound on (R.13). The original source-weight integral is not recomputed.

The native's successful scientific identity is distinct from the original formatter's failure. The old process has mathematical return code0, all10 mathematical gates passed, and a complete/proved native with the same source, input manifest and runtime. Neither its wrapper failure nor its header is relabeled.

## 4. Recover finite positive budgets without reconstructing coefficients

The successful whole-reference result stores, for each field
$f_a,f_b^V,a_1^V,b_1^V$, each required $p=0,1$, and each $0\le q\le3$, a complete positive number
$$
 W_{p,q}(H)=F_{p,q}(H)
       +\bigl[M_{\rm old}R_0^{-p}T_p(H/R_0)
              +M_{\rm add}R_A^{-p}T_p(H/R_A)\bigr]S_q(\Sigma_0).
 \tag{R.15}
$$
Here $F_{p,q}$ is the actual finite norm sum through degree12; its signed Fourier coefficients were added before their moduli. The fixed radii are
$R_0=1/6000,\ R_A=3/40000,\ \Sigma_0=1/128$.
The old function $f_a$ has $M_{\rm add}=0$.
Use the exact complete kernels
$$
 T_0(t)=\frac{t^{13}}{1-t},\qquad
 T_1(t)=\frac{13t^{12}}{1-t}+\frac{t^{13}}{(1-t)^2},
 \quad0\le t<1.
 \tag{R.16}
$$
Writing $v=e^{-4\sigma}$, both Fourier signs and the $q=0$ zero mode give
$$
 S_0(\sigma)=\frac{1+v}{1-v},\quad
 S_1(\sigma)=\frac{8v}{(1-v)^2},\quad
 S_2(\sigma)=\frac{32v(1+v)}{(1-v)^3},\quad
 S_3(\sigma)=\frac{128v(1+4v+v^2)}{(1-v)^4}.
 \tag{R.17}
$$

Evaluate a directed lower bound $\lambda_{p,q}$ for the identical old positive tail addend in (R.15), using lower bounds for its actual saved positive budget parameters. This is a lower bound for an algorithm's numerical addend, never a lower bound for a true error or amplitude. The old algorithm rounded these factors upward, so
$$
 F_{p,q}(h)\le F_{p,q}(H)
                   \le W_{p,q}(H)^+-\lambda_{p,q}.
 \tag{R.18}
$$
A strictly negative final enclosure is an identity/precision failure and must not be clipped to zero. No unknown finite coefficient is set to zero, and the finite sum is not rescaled by a guessed power of $h/H$.

Use the already completed S forcing product
$R_F=3/20000,\ \Sigma_F=1/64$, with its full normalized forcing moduli, and the already completed B amplitude product
$R_B=1/8000,\ \Sigma_B=3/512$, with its full genuine amplitude moduli. Their original image, inverse and regular-path gates are read, not recomputed. For the corresponding field $u$, set
$$
 U_{p,q}^{\rm new}
 =W_{p,q}(H)^+-\lambda_{p,q}
       +M_u R_u^{-p}T_p(h/R_u)S_q(\Sigma_u).
 \tag{R.19}
$$
Then (R.19) bounds the complete joint Fourier norm
$\sum_\ell\sup_{|\rho|\le h}|\partial_\rho^p u_\ell|\,|4\ell|^q$,
with the usual inclusion of the zero mode at $q=0$.
A whole-bound minimum with the saved W or S bound is permitted for that same derivative. The additional radial zero of the added $a_1$ term has already been included in its saved $M_{\rm add}$; it is not applied a second time.

This operation creates new scalar inequalities on a different physical evaluation radius. It does not recompute any accepted Taylor coefficient, Fourier norm, transport, potential, target or repaired cubic.

## 5. Scalar jets for the exact first-vector formula

All following arrays bound ordinary angular derivatives at real old $\phi$. Products use
$(u*v)_q=\sum_{k=0}^q\binom qk u_kv_{q-k}$.
Scalar coefficients are still bounded uniformly on the original complete parameter squares.

Let $R_G=3/8000,\ \Sigma_G=3/128,\ \tau=h/R_G$.
Read the complete saved fold moduli $j,BT,BA,A_-,Q_+,G_+$. The original root zeros and identities give
$$
 X_0=1+\tau j,\quad X_q=q!\Sigma_G^{-q}\tau j\ (q\ge1),
$$
$$
 Y_q=q!\Sigma_G^{-q}\tau^2BT,\qquad
 Z_q=q!\Sigma_G^{-q}\frac{2\tau BA}{3A_-}.
 \tag{R.20}
$$
Here $X,Y,Z$ bound $x=X_\phi,y=T_\phi,\zeta=y/T$.
The actual $T$ image is bounded by
$T_h=(h/H)T_H$, because the accepted $T_H$ is exactly the full-fold expression $HA_+^{2/3}$.
Set $\mathsf T_0=T_h,\ \mathsf T_{q+1}=Y_q$.

The complete $Q$ and $G$ jets follow from
$Q_\phi=-Q\zeta/2,\ G_\phi=G\zeta/4$.
They retain the full radial mean of $G$. Bound
$$
 a_0=G(x^2-Ty^2),\quad b_0=-2i\epsilon Gxy,\quad
 \mu=Q^2(x^2+Ty^2)
 \tag{R.21}
$$
by their full differentiated products. Only after differentiation are absolute values taken. The complete old $\Xi$ modulus on the full $H\times\Sigma_G$ product gives
$\Xi_q\le q!\Sigma_G^{-q}\Xi_+$ on the new restriction.
If the completed AJ angular-jet receipt is available, its complete $c_T$ and $\Xi$ derivative bounds may instead be read and restricted to $h\le H$, or compared with those whole Cauchy bounds. Their producer is not called again.

For $w_{0,X}$, the accepted leading inverse product has canonical radius
$R_c=27/32000$, width $\Sigma_c=1/64$, and bounds
$|a_0|\le M_*,\ |b_0/T^2|\le B_2$.
Let $X_H$ be the saved complete old-angle image at strip $s=1/256$.
The exact root value $a_0(0,X)=1$, Caratheodory on the $T$ disk and Cauchy in $X$ give
$$
 \|a_{0,X}\|\le
 \frac{2(M_*-1)T_h}{(R_c-T_h)(\Sigma_c-X_H)},\qquad
 \|b_{0,X}\|\le \frac{B_2T_h^2}{\Sigma_c-X_H}.
 \tag{R.22}
$$
Use a nonnegative upper for $M_*-1$; the input must prove $M_*\ge1$.
Both denominators must be positive. These estimates hold on the actual old-angle strip $s$; hence its $q$th real-angle derivative costs $q!s^{-q}$.
This is a new bound for the needed $X$ derivative. It does not charge the constant1 in $a_0$ as an angular derivative.

Read the successful complete $T$-derivative moduli for $V$ and $\mathcal B$ through order2. They hold on the original common $T$ disk of radius $I_T$. Require $d_T=I_T-T_h>0$. The two additional complete bounds are
$$
 \|\mathcal B^{(3)}\|\le\frac{\|V_{TT}\|}{7d_T},\qquad
 \|\mathcal B^{(4)}\|\le\frac{2\|V_{TT}\|}{9d_T^2}.
 \tag{R.23}
$$
Indeed $\mathcal B^{(p)}(T)=\frac12\int_0^1
s^{p-1/2}V^{(p)}(sT)\,ds$; its mass is $1/(2p+1)$.
Every $sT$ remains in the same star-shaped disk. For a scalar $F(T)$ use
$$
 F_\phi=F_Ty,\qquad F_{\phi\phi}=F_{TT}y^2+F_Ty_\phi .
 \tag{R.24}
$$
In particular the large radial value of $\mathcal B''$ is not multiplied by a generic $\Sigma_G^{-2}$ angular fee.

Apply the complete product rule to (R.11), using (R.12), (R.14) and (R.19)--(R.24). This gives six nonnegative bounds for
$(L_{1,a},L_{1,a,\phi},L_{1,a,\phi\phi},
  L_{1,b},L_{1,b,\phi},L_{1,b,\phi\phi})$.
All four complete summands of (R.11) are retained, including $N_{\rm old}$ and the exact factor $\mu$.

## 6. A second complete bound in physical variables

Write $w_1^V=(a_1^V,b_1^V)^t$.
G.4 gives the exact physical-coordinate expression
$$
 \begin{split}
 (L_2^V)_a={}&
 -2QV\{x\,b_{1,r}^V+(QTy-xd)b_{1,\phi}^V\}\\
 &-\mu(V_T+c_TV)b_1^V+\mathfrak R(w_0)_a,\\
 (L_2^V)_b={}&\mathfrak R(w_0)_b .
 \end{split}
 \tag{R.25}
$$
Thus $a_1^V$ does not enter the $E_{12}$ correction. For a bound, the sign change $b_{1,r}=-b_{1,\rho}$ is taken only after the exact expression is established.

On the original complete nonzero determinant domain,
$$
 \mathfrak R(w_0)
 =-\vartheta QVG\,\frac{x^2+Ty^2}{\Delta_V}
          (xy,\ i\epsilon y^2)^t,\qquad
 \Delta_V=x^2+(T-V/n^2)y^2 .
 \tag{R.26}
$$
Use its complete accepted determinant lower and differentiate the reciprocal through order2 by the exact product identity
$\Delta_V\Delta_V^{-1}=1$.
For a uniform complex-square coefficient bound, use
$|n^{-2}|=|z|/16\le2/388^2$; the final real-label input weight remains exactly $1/n$.
The two rank components retain respectively $xy$ and $y^2$, without replacing them by the full pair's larger norm.

For (R.25) use (R.19)'s $b_1^V$ jets through angular order3 and its first radial derivative through angular order2, the original full drift jets, and the already completed $c_T$ modulus with legitimate angular Cauchy loss. Apply the complete Leibniz rule through angular order2. No second derivative of $w_1^V$ is needed for this second vector either.

## 7. Same full operator and unchanged radial integration

Read the eighteen successful positive coefficient bounds from the complete genuine-column consumer. For any six complete amplitude-jet bounds $\mathbf u$, their same three branches give
$$
 \mathcal A_{\rm new}(\mathbf u)
 \le\sum_{\text{three branches}}\sum_{k=1}^6 c_k u_k,
 \qquad
 \|\mathsf S^V(u)\|\le|\rho|^{-1/4}\mathcal A_{\rm new}(\mathbf u).
 \tag{R.27}
$$
Both genuine columns, both signed input labels, every output including the mean, and the original profile/partition are the same. No new Airy profile or positive coefficient calibration is evaluated.

Compare each new raw local-vector coefficient against the original C algorithm's positive numerical coefficient for that same vector. A strictly positive lower bound $\beta_i$ for this saved number yields the sufficient uniform ratio
$q_i=\min(1,\mathcal A_{\rm new}(L_i)/\beta_i)$.
The denominator is not an amplitude or error lower bound.
Multiplying the corresponding already completed original term-L2 bound by $q_i$ preserves exactly the original six outer-$J$ coefficients, the common $|\rho|^{-1/4}$ envelope, true $dr$, input weight $1$ or $1/388$, and one-sided root-band integration. Keep the minimum with the latest successful complete term.

Only `local_raw_1` and `local_raw_2` may change.
The third local term, all eighteen nonlocal terms, all ten independent-mean terms, both source windows and every original seam/port obligation remain verbatim. Recombining complete upper bounds is allowed; subtracting one upper bound from an unrelated upper bound is not.

## 8. Execution and exact remaining obligations

The new public consumer restores the original whole-piece native and its natural stages by exact bytes and SHA, reads successful S/W/B/C/G small conclusions and the original4501-byte fold stage, and performs only the new scalar operations above. It does not rerun the old whole-piece, numerator, Taylor, forcing, transport, inverse, profile or matrix-word producers.

All complete restored inputs and new intermediate arrays remain temporary on the runner. The permanent output consists of small conclusions: exact identities and domains, original input hashes, complete scalar local bounds, the retained31-term ledger, source/manifest/run identity, counters and actual gates. The original successful process records remain unchanged.

The theorem is a complete negative-volume source estimate on the declared branch and physical support. It does not turn the root or affine-jump source into zero, remove a physical/reference interface, identify a positive growing column with a selected two-end solution, or supply the complete strong-return norm or coupled high inverse. Failure of a sufficient scalar improvement is recorded as such; it is not a lower bound on the true residual.
