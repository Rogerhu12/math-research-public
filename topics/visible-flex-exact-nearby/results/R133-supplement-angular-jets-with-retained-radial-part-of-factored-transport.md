# R133 supplement: angular jets that retain the radial part of the factored transport

2026-11-15, visible-exact-astra-0df9.

**Proved complete identities and a new scalar budget.** The large angularly constant part of the transport coefficient is retained at order zero. Its positive angular derivatives are estimated from the exact original mean decomposition. The leading-matrix inverse and the scalar principal factor receive their full angular derivatives; neither is treated as radial.

The result supplies an alternative complete derivative budget for the already identified transport sources. Its numerical evaluation and any improvement of a complete source term require a new public consumer. No new numerical constant or strong-return contraction is asserted here.

The primary identities are U.5 in [the exact old-circle inverse remainder](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md), G.2--G.3 and G.24--G.25 in [the ordered genuine sources](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md), and F.1--F.14 in [the exact leading-matrix factorization](R133-supplement-exact-leading-matrix-factorization-of-complete-transport-source.md). The original coefficient and fold moduli are those of [the anchored-fold producer](../scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py). The completed [factored-source computation](R133-supplement-actual-factored-transport-and-complete-companion-source-bounds.md) remains unchanged.

## 1. Exact radial mean and reciprocal transport identities

Use the original physical derivative, orientation and branch:
$$
 D=\partial_r-d\partial_\phi,\qquad x=X_\phi,\qquad
 y=T_\phi,\qquad \zeta=y/T=\frac23 A_\phi/A.
 \tag{AJ.1}
$$
The quotient at the root is its original holomorphic extension.
The exact identities are
$$
 Q_\phi=-\frac12Q\zeta,\qquad G_\phi=\frac14G\zeta,\qquad
 B_+=x^2+Ty^2,\qquad \mu=Q^2B_+ .
 \tag{AJ.2}
$$
In particular the sign in $B_+$ is plus. The distinct leading amplitude contains $x^2-Ty^2$.

Let $b$ denote the intrinsic coefficient used in the original scalarization. Its complete mean decomposition is
$$
 t(r)=\frac{\eta_r}{\eta}-4b\langle u^2+Kv^2\rangle_\phi,
 \qquad d_\phi=-bP_{\ne0}(u^2+Kv^2),\qquad
 T_0=t+5d_\phi.
 \tag{AJ.3}
$$
The mean is taken at the same fixed old $r$ over the whole circle. It is radial even when the allowed parameters are complex. Thus
$$
 \partial_\phi^qT_0=5\partial_\phi^{q+1}d
 \quad(q\ge1).
 \tag{AJ.4}
$$
The complete value of $t$ is retained. This identity does not erase any independent mean source in the original equation.

Define
$$
 F=Q^{-1},\qquad
 L=-F_r+dF_\phi-(t+4d_\phi)F.
 \tag{AJ.5}
$$
It follows from (AJ.2) that $F_\phi=F\zeta/2$.
For the original
$H_Q=DQ+Qd_\phi-T_0Q$, the signed identity
$$
 H_Q/Q^2=-DF+(d_\phi-T_0)F=L
 \tag{AJ.6}
$$
holds on the entire common product. Therefore the original coefficients are exactly
$$
 \boxed{\quad
 c_T=\frac{Lx-y^2/2}{B_+},\qquad
 \Xi=-\frac{Ly+x\zeta/2}{B_+}.
 \quad}
 \tag{AJ.7}
$$
To verify the first formula, use
$\mu c_T=H_Qx-Q^2y^2/2$.
For the second use
$\mu\Xi=-(H_Qy+Q^2x\zeta/2)$.
These are complete scalar equalities, before taking any modulus.

All radial derivatives in (AJ.5)--(AJ.7) are derivatives of the underlying analytic functions. No derivative of an interval bound or a radial partition envelope is taken.

## 2. Full leading-matrix inverse and two combined scalar factors

Write $s=i\epsilon$, $\epsilon=\pm1$, and
$$
 \mathcal K=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 U_\pm=x\,{\rm Id}\pm sy\mathcal K,\qquad
 M=G U_-^2.
$$
Since $\mathcal K^2=T\,{\rm Id}$ and $U_+U_-=B_+{\rm Id}$,
$$
 \boxed{\quad
 M^{-1}
 =G^{-1}B_+^{-2}
   \left\{(x^2-Ty^2){\rm Id}+2sxy\mathcal K\right\}.
 \quad}
 \tag{AJ.8}
$$
The two off-diagonal entries contain respectively $2sTxy$ and $2sxy$. Their order is fixed. Formula (AJ.8) is for the full matrix, including both input columns and every scalar mean.

For
$$
 P=QG/2,\qquad V=G^{-1},
$$
one has the two exact differential identities
$$
 P_\phi=-\frac14\zeta P,\qquad
 V_\phi=-\frac14\zeta V .
 \tag{AJ.9}
$$
The radial factor of $G$, including its original full mean integral, is unchanged. The opposite signs in the derivatives of $Q$ and $G$ have been combined before taking a norm. No subtraction of numerical upper bounds is used.

For comparison, direct differentiation of the original principal factor gives
$$
 \mu_\phi=Q^2\{2xx_\phi+2Ty y_\phi-\zeta x^2\}.
 \tag{AJ.10}
$$
Here $T_\phi=y$ and $\zeta T=y$ cancel two cubic terms. It would be incorrect to set $\mu_\phi$ to zero. The reciprocal $B_+^{-1}$ in (AJ.7)--(AJ.8) pays the same dependence explicitly.

## 3. The existing product and the meaning of the input moduli

Use exactly the accepted fold radius and angular strip
$$
 R=3/8000,\qquad \Sigma=3/128,
$$
and the same full physical root-piece radius
$$
 H=\frac{893368603925465506687}{21990232555520000000000000}<R.
 \tag{AJ.11}
$$
The original fixed $\eta_0$, complete complex $\delta$ square of halfwidth $10^{-8}$ and complex $z=j^{-2}$ square of halfwidth $1/9409$ remain in force. Final Hilbert-space operator estimates restrict to the original real parameters.

Read the accepted complete fold moduli
$$
 A_-,A_+,\ a_-,\ Q_+,\ G_+,\ G^{-1}_+,\ J_+,\ Y_+,\ A_{\phi,+},
 \qquad b_->0 .
$$
Their precise meanings and original fields are as follows.

| Modulus | Original complete field or meaning |
|---|---|
| $A_-,A_+$ | nonzero modulus lower and modulus upper of $A$; fold fields Am and Ap |
| $a_-$ | the original nonzero modulus lower for $a_\infty$; coefficient field am |
| $Q_+,G_+,G^{-1}_+$ | fold fields Q, G and Gi |
| $J_+$ | the whole-fold bound for $x-1$; field j |
| $Y_+$ | the whole-fold bound for $y=T_\phi$; field BT |
| $A_{\phi,+}$ | the whole-fold bound for $A_\phi$; field BA |
| $b_-$ | the already proved lower modulus of $B_+$; field gap |

All these bounds refer to the same full original product $|\rho|\le R$, $|\operatorname{Im}\phi|\le\Sigma$, with the original root branch. In particular, gap is the saved positive lower obtained by bounding $B_+-1$; it is not a new sampled determinant or an entrywise minimum. The original coefficient field am must not be replaced by a mean of $u$ or by the scalar intrinsic radius.

Also read the original complete coefficient bounds
$$
 D_q\ge\sup|\partial_\phi^qd|,\quad 0\le q\le4,
 \qquad T_+\ge\sup|T_0|.
 \tag{AJ.12}
$$
Because $t=\langle T_0\rangle$, the same $T_+$ bounds $|t|$. This follows from the exact mean identity, not from subtracting $5D_1$ from an upper bound.

The original anchored fold proves the radial zeros
$x-1=O(\rho)$, $y=O(\rho^2)$ and $\zeta=O(\rho)$.
Set
$$
 \tau=H/R,\qquad Z_+=\frac{2A_{\phi,+}}{3A_-},
 \qquad F_+=A_+^{1/3}/a_- .
 \tag{AJ.13}
$$
The identity $Q=a_\infty A^{-1/3}$ proves the complete $F_+$ bound. It retains the original nonzero branch.

These are scalar combinations of saved enclosures. No old intrinsic solve, fold construction, coefficient derivative, Fourier transform, target, repair, reference profile or radial source integral is rerun.

## 4. Complete ordinary angular jets

All jets below are bounds for ordinary derivatives, not factorial-normalized coefficients. For nonnegative arrays define
$$
 (a*b)_q=\sum_{i=0}^q {q\choose i}a_i b_{q-i}.
 \tag{AJ.14}
$$
Repeated products use this associative operation with enough retained orders.

For $0\le q\le4$, define
$$
 \begin{aligned}
 X_0&=1+\tau J_+,&
 X_q&=q!\Sigma^{-q}\tau J_+\quad(q\ge1),\\
 Y_q&=q!\Sigma^{-q}\tau^2Y_+,&
 Z_q&=q!\Sigma^{-q}\tau Z_+,\\
 \overline Z_q&=q!\Sigma^{-q}Z_+ .
 \end{aligned}
 \tag{AJ.15}
$$
Schwarz at the actual anchored radial zero and then angular Cauchy prove that $X,Y,Z$ bound the real-angle jets of $x,y,\zeta$ on the complete physical piece. The outer array $\overline Z$ bounds the same $\zeta$ derivatives on the full radial disk $R$. The two radial domains are not identified.

Let $\mathsf T_0$ be the already completed physical $T$ image in the factored-source receipt. Its accepted definition is $HA_+^{2/3}$, so it is valid on the full original angular strip. Set
$$
 \mathsf T_q=Y_{q-1}\quad(1\le q\le4).
 \tag{AJ.16}
$$
These are the exact differentiated identities $T_\phi=y$.

Construct inner and outer reciprocal-$Q$ jets by
$$
 F_0=\overline F_0=F_+,\qquad
 F_{q+1}=\frac12(F*Z)_q,\qquad
 \overline F_{q+1}=\frac12(\overline F*\overline Z)_q .
 \tag{AJ.17}
$$
Use $F$ through order4 and $\overline F$ through order3. The signed identity $F_\phi=F\zeta/2$ proves both recurrences. The positive angular orders retain a factor of $\zeta$ instead of applying angular Cauchy to the angularly constant part of $F$.

For $0\le q\le3$, radial Cauchy on the larger disk now gives
$$
 \sup_{|\rho|\le H,\ \phi\ {\rm real}}
 |\partial_r\partial_\phi^qF|
 \le \frac{\overline F_q}{R-H}.
 \tag{AJ.18}
$$
The sign change between $\partial_r$ and $\partial_\rho$ is irrelevant only after the absolute value. Formula (AJ.18) uses the outer jet, not the smaller inner $F_q$. This pays the entire radial margin for each actual differentiated function.

Define
$$
 L_q^\#=\frac{\overline F_q}{R-H}
       +\sum_{i=0}^q{q\choose i}D_iF_{q-i+1}
       +T_+F_q
       +4\sum_{i=0}^q{q\choose i}D_{i+1}F_{q-i}.
 \tag{AJ.19}
$$
Then $L_q^\#\ge\sup|\partial_\phi^qL|$.
The four terms are respectively the true radial derivative,
$dF_\phi$, the retained radial $tF$, and $4d_\phi F$.
All cross derivatives of the nonradial drift are present.

In particular, no $q!\Sigma^{-q}T_+$ is inserted for a positive angular derivative of $t$.

## 5. The reciprocal principal factor and transport coefficients

Set
$$
 B_q^\#=(X*X)_q+(\mathsf T*Y*Y)_q,\qquad 0\le q\le4.
 \tag{AJ.20}
$$
For the full reciprocal, take
$$
 R_0^\#=b_-^{-1},\qquad
 R_q^\#=b_-^{-1}\sum_{i=1}^q{q\choose i}
                      B_i^\# R_{q-i}^\#\quad(q\ge1).
 \tag{AJ.21}
$$
Differentiating $B_+B_+^{-1}=1$ proves (AJ.21). Hence every angular derivative of the inverse in (AJ.7)--(AJ.8) is paid.

Let
$$
 N_q=(L^\#*X)_q+\tfrac12(Y*Y)_q,\qquad
 E_q=(L^\#*Y)_q+\tfrac12(X*Z)_q,\qquad 0\le q\le3 .
 \tag{AJ.22}
$$
The complete saved factored-source receipt already contains
$c_{\rm old}\ge\sup|c_T|$ and
$\xi_{\rm old}\ge\sup|\Xi|$ on the stated physical radial disk and original angular strip. Read these two values without rebuilding their old budgets.

A new complete recursive choice is
$$
 C_0^\#=\min(c_{\rm old},N_0/b_-),\qquad
 E_0^\#=\min(\xi_{\rm old},E_0/b_-),
$$
$$
 \begin{aligned}
 C_q^\#&=b_-^{-1}\left\{N_q+
       \sum_{i=1}^q{q\choose i}B_i^\#C_{q-i}^\#\right\},\\
 E_q^\#&=b_-^{-1}\left\{E_q+
       \sum_{i=1}^q{q\choose i}B_i^\#E_{q-i}^\#\right\},
       \qquad 1\le q\le3 .
 \end{aligned}
 \tag{AJ.23}
$$
Here $E_q$ without a superscript is the numerator bound in (AJ.22), whereas $E_q^\#$ bounds the full coefficient $\Xi$. This distinction must be explicit in an implementation.

The exact equations $B_+c_T=Lx-y^2/2$ and
$B_+\Xi=-Ly-x\zeta/2$, differentiated before estimating, prove (AJ.23) by induction. In particular the large zero-order value multiplies only the actual positive-order derivatives of $B_+$; it does not create a false angular derivative of the radial part.

One may retain the smaller of each displayed derivative bound and the independent complete old Cauchy bound for the same scalar derivative. Such a minimum is a comparison of whole proved bounds. It is never a minimum of signed matrix or Gram entries.

## 6. Complete leading inverse and transport prefactor jets

Start with
$$
 P_0^\#=Q_+G_+/2,\qquad V_0^\#=G^{-1}_+ .
$$
The exact signed identities (AJ.9) give
$$
 P_{q+1}^\#=\tfrac14(P^\#*Z)_q,\qquad
 V_{q+1}^\#=\tfrac14(V^\#*Z)_q .
 \tag{AJ.24}
$$
Thus the complete prefactor $QGB_+/2$ has jet bound
$P^\#*B^\#$, with all scalar means retained.

Put
$$
 A_q^\#=(X*X)_q+(\mathsf T*Y*Y)_q,\qquad
 B_q^{\rm lo}=2(X*Y)_q,\qquad
 B_q^{\rm up}=2(\mathsf T*X*Y)_q .
$$
Through any retained order at most3, the four full matrix entries of $M^{-1}$ are bounded by
$$
 \begin{pmatrix}
 V^\#*R^\#*R^\#*A^\#&
 V^\#*R^\#*R^\#*B^{\rm up}\\
 V^\#*R^\#*R^\#*B^{\rm lo}&
 V^\#*R^\#*R^\#*A^\#
 \end{pmatrix}.
 \tag{AJ.25}
$$
This is just the complete ordered formula (AJ.8). Both diagonal entries include the same exact signed $x^2-Ty^2$ before its absolute upper is taken. The factor $s$ has modulus one for both input signs. Multiplying this matrix on the left of the two already completed $w_1$ jets bounds $Z=M^{-1}w_1$ with its full mean and both columns.

The complete transport sources then use the unchanged factored identities F.8 and F.10--F.14. In particular the regular quotient $(f_b-B)/T$, its genuine root condition, every actual rank term with $n^{-2}$, $q=v_{\rm bg}g-(v_{\rm bg})_\phi p$, and the independent physical mean source remain. Replacing their full products by the leading zero-frequency coefficient would not follow from this theorem.

## 7. Numerical consumer and exact remaining scope

A new consumer may read the saved original coefficient/fold moduli, original correction jets, the completed factored-source small receipt, original inverse/profile/word coefficients and the already integrated same-six-row radial weight. It then evaluates (AJ.13)--(AJ.25) as a new positive scalar closure and inserts the resulting complete jets into the existing full operator recipe.

It must preserve the original physical support, uncertain-root one-sided bands, both density windows, all31 source terms, true ordinary $dr$ measure, both genuine columns, both signs, complete means and every actual seam. Any replaced term must be a new bound for that same complete operator. An unaffected complete term is read verbatim from the latest successful ledger; the old successful source pipeline is not rerun.

The old Cauchy-based transport bound remains a valid comparison even if a new scalar candidate is larger. A failed sufficient improvement does not prove that the actual operator is large. The completed old receipt and its successful source are not modified.

This theorem supplies angular derivative budgets only. The exact given-root negative cut readout, root and affine jumps, strict propagation, positive two-end graph, physical-angle bridge, complete strong-return norm, finite border and coupled full core inverse retain their independent obligations.
