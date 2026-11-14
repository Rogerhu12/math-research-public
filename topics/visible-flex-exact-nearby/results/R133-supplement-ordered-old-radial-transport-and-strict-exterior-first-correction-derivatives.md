# Ordered old-radial transport and strict exterior derivatives of the first Airy correction

**Status: proved analytic identity and complete directed-majorant contract.**
The numerical exterior bounds in this note have not yet been evaluated. The object is the same explicit repaired family, the same fixed original $\eta_0$, and the same root-normalized first correction used in the [complete old-radial Taylor recurrence](R133-supplement-old-radial-first-Airy-Taylor-and-complete-Fourier-root-recurrence.md). Numerical use below is on the complete real parameter disk $|\delta|\le10^{-8}$ and on each original open radial piece. No finite Fourier projection, new radial normalization, or discarded mean is introduced.

This supplies a two-component alternative to the strict exterior branch formula in [D.13--D.16](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md). It eliminates the need to divide by a chosen $\sqrt{-T}$ branch. Its actual numerical usefulness still requires the declared public consumer.

## E.1. Normalization, coordinates and forcing order

Write
$$
 \rho=r_*-r,\qquad D=\partial_r-d\partial_\phi
                    =-\partial_\rho-d\partial_\phi,
$$
$$
 x=X_\phi,\qquad y=T_\phi,\qquad
 K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 B_+=x^2+Ty^2.
$$
The subscript on $K_T$ distinguishes this matrix from the scalar Gauss curvature. The exact fold relations are
$$
 DT=Qx,\qquad DX=-QTy,\qquad \eta^2K=Q^2T.
\tag{E.1}
$$
The leading reconstruction is
$$
 M_0=\begin{pmatrix}a_0&Tb_0\\b_0&a_0\end{pmatrix},
 \quad
 a_0=G(x^2-Ty^2),\quad b_0=-2i\epsilon Gxy,
 \quad \det M_0=G^2B_+^2.
\tag{E.2}
$$
Let $w_1=(a_1,b_1)^t=M_0Z$ and $Z=(\mathcal A,\mathcal B)^t$. If
$$
 \binom{f_b}{f_a}=M_0^{-1}\binom{F_b}{F_a},
$$
then the exact normalized equations are
$$
 2\mathcal A_T-2i\epsilon T\mathcal B_X=f_a,\qquad
 2T\mathcal B_T+\mathcal B-2i\epsilon T\mathcal A_X=f_b.
\tag{E.3}
$$
The vector on the right after division by $2T$ in the second equation is therefore ordered as $(f_a,f_b)$, not $(f_b,f_a)$.

## E.2. Exact old-radial matrix identity

For $T\ne0$, put $f=(f_a,f_b)^t$. Then
$$
 \boxed{Z_\rho=CZ_\phi+MZ-Nf}
\tag{E.4}
$$
with
$$
 C=-dI-i\epsilon QK_T,\qquad
 M=\frac Q2
 \begin{pmatrix}0&-i\epsilon y\\0&x/T\end{pmatrix},
 \qquad
 N=\frac Q2
 \begin{pmatrix}x&-i\epsilon y\\-i\epsilon y&x/T\end{pmatrix}.
\tag{E.5}
$$
This is an exact identity on both strict sides of the root. There is no replacement of the old-circle primitive by a fixed-$T$ primitive.

Indeed, (E.1) gives the exact operator identity
$$
 D-i\epsilon QK_T\partial_\phi
  =Q(xI-i\epsilon yK_T)(\partial_T-i\epsilon K_T\partial_X).
\tag{E.6}
$$
The coefficient of $\partial_X$ follows from $K_T^2=TI$; the two scalar terms $xTy$ cancel. Substituting (E.3) gives
$$
 DZ-i\epsilon QK_TZ_\phi+
 \frac Q2(xI-i\epsilon yK_T)\operatorname{diag}(0,T^{-1})Z
 =
 \frac Q2(xI-i\epsilon yK_T)\operatorname{diag}(1,T^{-1})f .
$$
Now insert $D=-\partial_\rho-d\partial_\phi$ to obtain (E.4). The two products on this line are exactly the matrices $M,N$ in (E.5). Only $B_+$ occurs in the coordinate inverse; $B_-$ remains confined to $a_0$ in (E.2).

## E.3. Strict domains and original seams

Let $I$ be a closed subinterval inside one original radial piece, entirely outside a fixed physical inner window. Let
$$
 0<h_I\le|\rho|\le R_I,\quad
 |A|\ge A_->0,\quad |B_+|\ge b_->0,\quad |G|^{-1}\le G_i
\tag{E.7}
$$
hold on the declared angle strip. Since $T=-\rho A^{2/3}$ on the actual branch,
$$
 |T|\ge t_I:=h_I A_-^{2/3}>0.
\tag{E.8}
$$
All majorants below use this true lower bound. In particular they do not divide by an upper enclosure for $|T|$, or infer a complex lower bound from a real floating-point value.

Every derivative below is one-sided on its original radial piece. The original jumps remain separate and retain the order of the old $J$, projection and reconstructed source. None of these formulas declares that a true physical seam has zero source.

## E.4. Directed matrix majorants

A superscript bar in this section denotes a nonnegative entrywise majorant on a common strip and radial interval. Write $q,q_\rho,q_\phi$ for bounds for $Q,Q_\rho,Q_\phi$, and use $x_0,x_\rho,x_\phi$, $y_0,y_\rho,y_\phi$, $t_0,t_\rho,t_\phi$ and $d_0,d_\rho,d_\phi$ analogously. The symbols are upper bounds for moduli, regardless of the sign of the underlying real function.

One may take
$$
 \overline C=
 \begin{pmatrix}d_0&qt_0\\q&d_0\end{pmatrix},
\quad
 \overline C_\rho=
 \begin{pmatrix}d_\rho&q_\rho t_0+qt_\rho\\q_\rho&d_\rho\end{pmatrix},
\quad
 \overline C_\phi=
 \begin{pmatrix}d_\phi&q_\phi t_0+qt_\phi\\q_\phi&d_\phi\end{pmatrix}.
\tag{E.9}
$$
For $v\in\{\rho,\phi\}$, define
$$
 L_v=q_vy_0+qy_v,\qquad
 H_v=\frac{q_vx_0+qx_v}{t_I}
                  +\frac{qx_0t_v}{t_I^2}.
$$
Then
$$
 \overline M=\frac12
 \begin{pmatrix}0&qy_0\\0&qx_0/t_I\end{pmatrix},\qquad
 \overline M_v=\frac12\begin{pmatrix}0&L_v\\0&H_v\end{pmatrix},
\tag{E.10}
$$
$$
 \overline N=\frac12
 \begin{pmatrix}qx_0&qy_0\\qy_0&qx_0/t_I\end{pmatrix},\qquad
 \overline N_v=\frac12
 \begin{pmatrix}q_vx_0+qx_v&L_v\\L_v&H_v\end{pmatrix}.
\tag{E.11}
$$
These are ordinary derivative bounds. No factorial is suppressed in (E.9)--(E.11). The factors involving $y$ remain their actual small factors; they are not replaced by $1/t_I$.

## E.5. Complete forcing and normalized amplitude inputs

Let $\overline W_j$ be complete vector suprema for $\partial_\phi^jw_1$ on a sufficiently wide strip. A valid complete inverse bound is
$$
 \overline R_0=
 \frac{G_i^2}{b_-^2}
 \begin{pmatrix}
 |a_0|_{\rm up}&t_0|b_0|_{\rm up}\\
 |b_0|_{\rm up}&|a_0|_{\rm up}
 \end{pmatrix}
 \ \ge\ |M_0^{-1}|.
\tag{E.12}
$$
Thus $\overline Z_0=\overline R_0\overline W_0$ is a complete bound. This uses the full $w_1$ selected by its original regular root normalization.

If $\sigma_w$ is a paid strip for this complete bound and $0\le\sigma<\sigma_w$, put $\Delta=\sigma_w-\sigma$. Ordinary angular derivative bounds are
$$
 \overline Z_j=\frac{j!}{\Delta^j}\overline Z_0,\qquad j=1,2.
\tag{E.13}
$$
Previously paid sharper derivative bounds can be used if their domains and norms agree; a supremum and a Wiener norm must not be identified.

Write $P_s=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ and
$F=(F_b,F_a)^t$. Then
$$
 f=P_sM_0^{-1}F,\qquad
 f_\rho=P_s\left(M_0^{-1}F_\rho
            -M_0^{-1}(M_0)_\rho M_0^{-1}F\right).
\tag{E.14}
$$
It follows that valid majorants are
$$
 \overline f=P_s\overline R_0\,\overline F,\qquad
 \overline f_\rho=
 P_s\left(\overline R_0\,\overline F_\rho+
 \overline R_0\,\overline{(M_0)_\rho}\,
                  \overline R_0\,\overline F\right).
$$
The angular derivative $\overline f_\phi$ is obtained either by the analogous exact inverse identity or by a declared positive angular Cauchy loss. Every entry of $F,F_\rho$ retains the complete local forcing, with its original independent mean value.

## E.6. Only one radial forcing derivative is needed

Differentiate (E.4), without interchanging matrix factors:
$$
 Z_{\rho\phi}=C_\phi Z_\phi+CZ_{\phi\phi}
                   +M_\phi Z+MZ_\phi-N_\phi f-Nf_\phi,
\tag{E.15}
$$
$$
 Z_{\rho\rho}=C_\rho Z_\phi+CZ_{\rho\phi}
                   +M_\rho Z+MZ_\rho-N_\rho f-Nf_\rho.
\tag{E.16}
$$
In particular, no $f_{\rho\rho}$ is needed on the strict domain.

A complete entrywise majorant is furnished by the following ordered three-line recursion:
$$
 U_\rho=\overline C\,\overline Z_1+
           \overline M\,\overline Z_0+\overline N\,\overline f,
$$
$$
 U_{\rho\phi}=\overline C_\phi\,\overline Z_1+
 \overline C\,\overline Z_2+
 \overline M_\phi\,\overline Z_0+\overline M\,\overline Z_1+
 \overline N_\phi\,\overline f+\overline N\,\overline f_\phi,
$$
$$
 U_{\rho\rho}=\overline C_\rho\,\overline Z_1+
 \overline C\,U_{\rho\phi}+
 \overline M_\rho\,\overline Z_0+\overline M\,U_\rho+
 \overline N_\rho\,\overline f+\overline N\,\overline f_\rho.
\tag{E.17}
$$
Every product is an ordinary nonnegative $2\times2$ matrix times a two-component vector in the displayed order.

Reconstruction uses only already paid leading derivatives through order two:
$$
 (w_1)_\rho=(M_0)_\rho Z+M_0Z_\rho,
$$
$$
 (w_1)_{\rho\phi}=(M_0)_{\rho\phi}Z+(M_0)_\rho Z_\phi
                  +(M_0)_\phi Z_\rho+M_0Z_{\rho\phi},
$$
$$
 (w_1)_{\rho\rho}=(M_0)_{\rho\rho}Z+
                    2(M_0)_\rho Z_\rho+M_0Z_{\rho\rho}.
\tag{E.18}
$$
Equations (E.12)--(E.18) therefore give complete bounds for the exterior derivatives needed by the local second-order operator. Additional angular derivatives of $(w_1)_\rho$ may use a further declared strip loss; this does not introduce an additional radial derivative.

## E.7. Exact local forcing derivative

For clarity, let $\mathscr K(\rho)=K(r_*-\rho)$ be the scalar curvature. On one original open piece set
$$
 c_2=d^2+\eta^2\mathscr K,\qquad
 c_1=d_\rho+dd_\phi+T_0d,\qquad v=\vartheta Q.
$$
The exact local numerator for the leading vector $w_0=(a_0,b_0)^t$ is
$$
 \mathcal N=
 (w_0)_{\rho\rho}+2d(w_0)_{\rho\phi}
 +c_2(w_0)_{\phi\phi}+c_1(w_0)_\phi
 +T_0(w_0)_\rho+V_0w_0+i\epsilon vK_Tw_0.
\tag{E.19}
$$
The forcing convention of E.1 is $F=-\mu^{-1}\mathcal N$. Its exact radial derivative is
$$
 F_\rho=-\mu^{-1}\mathcal N_\rho-\frac{\mu_\rho}{\mu}F.
\tag{E.20}
$$
The second term has the displayed minus sign since $\mathcal N=-\mu F$. For absolute bounds it contributes $|\mu_\rho/\mu|\,|F|$.

Explicitly,
$$
\begin{aligned}
 \mathcal N_\rho={}&
 (w_0)_{\rho\rho\rho}
 +2d_\rho(w_0)_{\rho\phi}+2d(w_0)_{\rho\rho\phi}\\
 &+(c_2)_\rho(w_0)_{\phi\phi}+c_2(w_0)_{\rho\phi\phi}\\
 &+(c_1)_\rho(w_0)_\phi+c_1(w_0)_{\rho\phi}\\
 &+(T_0)_\rho(w_0)_\rho+T_0(w_0)_{\rho\rho}\\
 &+(V_0)_\rho w_0+V_0(w_0)_\rho\\
 &+i\epsilon(v_\rho K_T+v(K_T)_\rho)w_0
                      +i\epsilon vK_T(w_0)_\rho .
\end{aligned}
\tag{E.21}
$$
Here
$$
 (c_1)_\rho=d_{\rho\rho}+d_\rho d_\phi+
 d\,d_{\rho\phi}+(T_0)_\rho d+T_0d_\rho,
$$
$$
 (c_2)_\rho=2dd_\rho+2\eta\eta_\rho\mathscr K+
                    \eta^2\mathscr K_\rho,
$$
$$
 \mu_\rho=2QQ_\rho(x^2+Ty^2)
              +Q^2(2xx_\rho+T_\rho y^2+2Tyy_\rho).
\tag{E.22}
$$
No third derivative of a coefficient in $T_0,V_0,\vartheta$ is demanded. Their first derivatives follow from the complete original coefficient identities and the already saved ordinary background jets through order two.

## E.8. Where the one genuinely new exterior derivative enters

The only new leading radial derivative in (E.21) is $(w_0)_{\rho\rho\rho}$. The mixed derivatives of total order three may be obtained from the completed second-radial derivative envelopes by an angular Cauchy loss on each original piece.

The [third-jet exterior theorem](R133-supplement-third-jet-exterior-and-holomorphic-root-budget-for-first-Airy-residual.md) gives, with $k=-\mathscr K/\rho$,
$$
 \rho k_{\rho\rho\rho}+3k_{\rho\rho}=K_{rrr}(r_*-\rho),
\qquad
 |k_{\rho\rho\rho}|
 \le\frac{|K_{rrr}|+3|k_{\rho\rho}|}{h_I}.
\tag{E.23}
$$
The sign of $K_{rrr}$ on the right is positive in this formula. The previously proved integral bound for $k_{\rho\rho}$ may be used, giving $2\sup|K_{rrr}|/h_I$ if one uses a common whole-window bound.

Likewise, with $e=-d$,
$$
\begin{aligned}
 2\rho A_{\rho\rho\rho}+7A_{\rho\rho}={}&
 4(e_\rho A_\phi+eA_{\rho\phi})\\
 &+2\rho(e_{\rho\rho}A_\phi+
           2e_\rho A_{\rho\phi}+eA_{\rho\rho\phi})\\
 &+3(aX_\phi)_{\rho\rho}.
\end{aligned}
\tag{E.24}
$$
The exact equation
$$
 X_\rho=eX_\phi+\frac23a\rho^2A_\phi
$$
then supplies $X_{\rho\rho\rho}$ using only $a_{\rho\rho}$, $e_{\rho\rho}$, and the completed mixed derivatives through radial order two. An angular Cauchy estimate supplies $(X_\phi)_{\rho\rho\rho}$ on a smaller strip. The same procedure supplies $(T_\phi)_{\rho\rho\rho}$ from $T=-\rho A^{2/3}$.

Finally
$$
 \log G=\frac16\log(A/a_*)-\frac14\log(k/k_*)+\log E_G,
 \qquad (\log E_G)_\rho=2\beta\langle S\rangle,
\tag{E.25}
$$
shows that $G_{\rho\rho\rho}$ uses only (E.23), (E.24), and
$$
 (\log E_G)_{\rho\rho\rho}
 =2\left(\beta_{\rho\rho}\langle S\rangle+
       2\beta_\rho\langle S_\rho\rangle+
       \beta\langle S_{\rho\rho}\rangle\right).
$$
The full mean on this line is retained. Its derivatives are supplied by the completed original cubic and intrinsic jets; no nonmean projection is inserted in place of it.

Thus the exterior consumer needs no new fourth or fifth intrinsic target derivative, no new root FFT and no new characteristic solve. It adds a genuine new third-leading/first-forcing derivative budget from the already completed data.

## E.9. Exact inner/exterior partition

Let the same true root enclosure be $[r_{\rm lo},r_{\rm hi}]$ and let $h=9/10^6$. Use the fixed inner physical interval
$$
 I_{\rm in}=[r_{\rm lo}-h,r_{\rm hi}+h].
$$
The [actual old-radial Taylor result](R133-supplement-actual-complete-old-radial-first-Airy-Taylor-bounds.md) pays
$|\rho|\le h+(r_{\rm hi}-r_{\rm lo})$ on that interval. On either strict exterior complement, every allowed true root satisfies $|\rho|\ge h$.

The interior and exterior formulas refer to the same root-normalized $w_1$, so they split one norm integral. They do not multiply $w_1$ by a spatial cutoff and they do not restart (E.3) at either artificial endpoint. There is therefore no artificial interface source. The two bounds may be minimized on an overlap only after confirming identical domains and norms.

All true physical seams inside the exterior remain in the original ordered reconstruction/source contract. In particular the finite Taylor calculation inside the original root piece is not analytically continued across a neighboring physical spline seam.

## E.10. Data, norm and publication requirements for a consumer

A valid actual consumer must:

1. Pin the complete original root, first-forcing and first-seam natives and the successful small Taylor native by their byte hashes. Reuse their successful coefficient rows and amplitude stages.
2. Preserve the exact root interval, fixed $\eta_0$, same real $\delta$ disk and all $65/193$ original components.
3. Split only at exact original row/piece boundaries and the declared fixed inner endpoints. Use the true distance $h_I$ of each exterior subinterval from the whole root enclosure.
4. Retain separate two-component bounds, all means, the exact $B_+$ principal factor, every genuine physical seam and all old-circle remainders not yet paid.
5. Label strip-supremum and Wiener bounds separately, and explicitly pay any angular loss or full Fourier conversion.
6. Save every completed new derivative and integral prefix before attempting the next one. A failed exterior cell cannot authorize recomputation of an already completed root or Taylor stage.

Equations (E.4)--(E.25) prove this contract. They do not give a numerical strong-return constant, a global unknown-high inverse, or an actual cutoff-$97$ closure before those additional numerical source and interface gates have passed.
