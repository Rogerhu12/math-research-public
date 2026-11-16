# R133 supplement: complete scalar-flux adjoint and first-row reception of mean-completed Airy trials

2026-11-16, visible-exact / tail_connector.

**Proved analytic identities and conditional decay estimates.** Completing the second moving equation and its physical mean leaves one odd raw source. Its two characteristic injections are exactly correlated. In the original SP weighted coordinates their curvature factors cancel, so the complete saved first-row receiver charges that source and qualified jumps by $O_0m_{11}$, without the old separate source-injection factor.

The complete three-block adjoint and a mean normal form are retained. Radial integration by parts moves derivatives; it does not itself create a frequency gain. A finite primitive argument proves two angular gains for $IJ$ on a qualified real Airy expression, using only the actual odd/even inverse. This gives an $n^{-2}$ jump bound under the specified continuous-leading-amplitude hypotheses. The body estimate below is a precise sufficient interface for the complete ordered scalar residual, not an assertion inferred from the first forcing alone.

No scientific value, old calculation, profile, ray, source integral or propagator is evaluated. The published WAD first-row success is unchanged. Repository paths below are relative to topics/visible-flex-exact-nearby.

## WUR1. Same physical object and complete scalarization

Keep N/WAD's repaired explicit reference, selected real parameter, intrinsic parameter, physical moving angle and homogeneous high root column. The independent supplied head and other ports retain that column's fixed values. Its input normalization, including $n^{7/6}$ when used, belongs to the column before any residual estimate. Here $n=4|j|$, $|j|\ge97$.

On the original normalized circle set
$$
 \partial=\partial_\phi,\quad \Pi f=\langle f\rangle,\quad
 P=Id-\Pi,\quad I=\partial^{-1}P,\quad I^*=-I,\quad \|I\|_{2\to2}\le1/4 .
 \tag{WUR.1}
$$
Write $Rf(\phi)=f(-\phi)$, $P_o=(Id-R)/2$, $P_e=(Id+R)/2$, and $P_{e0}=PP_e$. The physical state has $h_1$ odd and $h_2$ even. Put $w=h_1$, $f=P_{e0}h_2$, $z=\Pi h_2$.

Use exactly N.4--7:
$$
 \mathcal D=PM_d\partial P,\quad D_0=\partial_r-\mathcal D,\quad
 A=\eta\partial+L,\quad J=A^{-1},
$$
$$
 L=P_{e0}M_\ell P_o-2\beta P_{e0}M_{v_\phi}IM_uP_o,
 \qquad \ell=-2\beta uv,\quad \eta=-\gamma m,\quad m=\Pi v .
 \tag{WUR.2}
$$
The operators $B,E,C,b_1,b_2$ retain all N.5 projections and primitives. Every use of $J$ is on its admitted odd-to-even-zero realization and actual inverse. A root inverse and the whole strict inverse are identified only on their common admitted domain by uniqueness; neither an unqualified full-signed realization nor a root numerical constant is extended by notation.

Define
$$
 H_1=\mathcal D+E,\quad H_2=\mathcal D+B,\quad
 a_z=\beta(1-\langle u^2+Kv^2\rangle)-2\beta Km^2,
$$
$$
 \ell_1w=-2\beta m\Pi(uw),\qquad
 \ell_2f=-2\beta mK\Pi((v-m)f).
 \tag{WUR.3}
$$
The complete raw equation is
$$
 \begin{pmatrix}w\\f\\z\end{pmatrix}'=
 \begin{pmatrix}
 H_1&KC&b_1\\ A&H_2&b_2\\ \ell_1&\ell_2&a_z
 \end{pmatrix}
 \begin{pmatrix}w\\f\\z\end{pmatrix}
 +\begin{pmatrix}g_1\\Pg_2\\\Pi g_2\end{pmatrix}.
 \tag{WUR.4}
$$
Its last row is the physical moving mean N.7.

For a chosen even-zero height $f$, set
$$
 k=Jb_2,\quad w_{10}=J(\partial_r-H_2)f,\quad
 a_{\rm eff}=a_z-\ell_1k=a_z+2\beta m\Pi(uk),
$$
$$
 F_m=-\ell_1w_{10}-\ell_2f
     =2\beta m\Pi\{uw_{10}+K(v-m)f\}.
 \tag{WUR.5}
$$
Solve
$$
 z'=a_{\rm eff}z-F_m,\qquad z(r_*)=0
 \tag{WUR.6}
$$
when that is the declared root trace, and reconstruct $w=w_{10}-zk$, $h_2=f+z$. On each actual smooth piece the second nonmean row and its physical mean are exact. The full ordinary residual is therefore $(g_1,0)$, with
$$
 g_1=(D_0-E)J[(D_0-B)f-zb_2]-KCf-zb_1 .
 \tag{WUR.7}
$$
Zero second residual is not zero second state or zero mean.

Substitution of the actual mean equation gives
$$
 \mathcal L_{\rm sc}=(D_0-E)J(D_0-B)-KC,\qquad
 R_m=(D_0-E)k+a_{\rm eff}k+b_1,\qquad
 g_1=\mathcal L_{\rm sc}f+F_m k-zR_m .
$$
$$
 \mathcal Q=A\mathcal L_{\rm sc}
   =D_0^2+\eta^2K\partial^2-\mathcal T D_0+\mathcal V,\qquad
 \boxed{\quad Ig_1=IJ\mathcal Qf+F_m Ik-zIR_m .\quad}
 \tag{WUR.8}
$$
Here $\mathcal T,\mathcal V$ are O.8--20 in their original order. This $\mathcal Q$ is the complete scalar operator, not the old strict normalizer remainder. Its one-gain radial term, mean/projection remainders and L.5 first forcing remain. $R_m$ still contains the true derivative of $Jb_2$.

## WUR2. Full physical adjoint and weak scalar flux

On the selected real family write the raw adjoint as
$\lambda=(\xi,\theta+\zeta)$, with $\xi$ odd, $\theta$ even mean-zero and $\zeta=\Pi\lambda_2$. It satisfies
$$
 \begin{aligned}
 -\xi'&=H_1^*\xi+A^*\theta+\ell_1^*\zeta,\\
 -\theta'&=KC^*\xi+H_2^*\theta+\ell_2^*\zeta,\\
 -\zeta'&=b_1^*\xi+b_2^*\theta+a_z\zeta ,
 \end{aligned}
 \tag{WUR.9}
$$
where
$$
 \mathcal D^*=-\partial M_dP,\quad
 \ell_1^*\zeta=-2\beta m u\zeta,\quad
 \ell_2^*\zeta=-2\beta mK(v-m)\zeta .
$$
Coefficient derivatives in $-\partial M_dP$ remain. Complex-parameter adjoints would require coefficient conjugation; they are not asserted by the real notation.

On the original strict interval $[0,c]$, $c=r_c$, let $q=\sqrt{-K}>0$. Put
$$
 T(q)=\frac1{\sqrt{2q}}\begin{pmatrix}1&q\\1&-q\end{pmatrix},
 \qquad \mathfrak D_r=(I,\Pi)n_g(r)T(q(r)).
 \tag{WUR.10}
$$
WAD's dimensionless physical primitive row is
$\mathcal B_\partial=B_\partial Q_R$, with
$B_\partial(y,\zeta)=(y_++y_-)/\sqrt2$. On a true reflected state it equals $n_g(0)Ih_1(0)/\sqrt{q(0)}$. For even mean-zero $b$ its raw adjoint data are
$$
 \lambda_b(0)=-\frac{n_g(0)}{\sqrt{q(0)}}(Ib,0).
 \tag{WUR.11}
$$
Only the initial second component is zero. Equations (WUR.9) generally generate both its nonmean and mean parts.

One radial integration by parts on a smooth piece gives
$$
 \begin{aligned}
 \int_a^b\langle\xi,g_1\rangle\,dr
 ={}&[\langle\xi,w\rangle]_a^b\\
 &+\int_a^b\{\langle\theta,Aw\rangle+
       \langle\zeta,\ell_1w\rangle
       -\langle KC^*\xi,f\rangle
       -\langle b_1^*\xi,z\rangle\}\,dr .
 \end{aligned}
 \tag{WUR.12}
$$
It does not differentiate the reconstructed oscillatory flux in the volume. In particular it does not require separately bounding $J_rf_r$ and $Jf_{rr}$ there. The actual adjoint, flux and both endpoint pairings must still be paid in their true spaces.

Substitute $Aw=f'-H_2f-zb_2$ and $\ell_1w=z'-a_zz-\ell_2f$, and integrate once more. The last two adjoint equations cancel every remaining volume term:
$$
 \int_a^b\langle\xi,g_1\rangle\,dr
  =[\langle\xi,w\rangle+\langle\theta,f\rangle
                                   +\langle\zeta,z\rangle]_a^b .
$$
For increasing-$r$ state jumps and the actual continuous adjoint transmission,
$$
 \boxed{\quad
 \int_0^c\langle\xi,g_1\rangle\,dr
 +\sum_\lambda\langle\lambda(r_\lambda),[\mathscr U]_\lambda\rangle
   =\langle\lambda(c),\mathscr U(c)\rangle
                         -\langle\lambda(0),\mathscr U(0)\rangle .
 \quad}
 \tag{WUR.13}
$$
A different background with nonidentity transmission must retain its dual transmission. These are primal--adjoint Green identities, not a self-pairing of primal solutions.

They hold first on the smooth core and then in N's weak source/flux duality. No source derivative is created by definition. An equivalent weak scalar adjoint retains the flux
$$
 \theta=J^*(-\xi'-H_1^*\xi-\ell_1^*\zeta)
 \tag{WUR.14}
$$
and the other two equations of (WUR.9). No independent second cut condition is imposed.

The disappearance of radial derivatives from (WUR.12) is not a new frequency gain: (WUR.13) places them in the complete actual adjoint and endpoint/jump tuple.

## WUR3. Exact source correlation and cancellation of the source weight

Odd $g_1$ has even mean-zero primitive. Directly,
$$
 \boxed{\quad
 \mathfrak D_r(g_1,0)
 =\frac{n_g(r)}{\sqrt{2q(r)}}(Ig_1,Ig_1;0,0).
 \quad}
 \tag{WUR.15}
$$
Both primitive entries are the same signed function. Zero stored-mean injection follows from the source parity, not from deleting the evolving even physical mean.

The WAD reflection isometry
$\mathfrak E(a,\alpha)=(a,Ra;\alpha,-\alpha)/\sqrt2$
compresses this source to $(n_g Ig_1/\sqrt q,0)$. In the ungauged SP source coordinates,
$$
 s_y=(Ig_1,Ig_1)/\sqrt{2q},\qquad s_z=0,\qquad
 \sqrt q\,\|s_y\|_{L^2\oplus L^2}=\|Ig_1\|_2 .
 \tag{WUR.16}
$$
The actual $q,n_g$ are radial and commute with $I$. The equality uses the same $q$ in both components before any interval bounds or separate wave magnitudes.

Let $m_{11}$ be the complete first entry of ST's saved reverse positive matrix and $O_0=n_g(0)/\sqrt{q(0)}$. Its original all-shorter-subproduct qualification proves
$$
 \boxed{\quad
 \|\text{received first-row source and qualified jumps}\|
 \le O_0m_{11}\left[
    \int_0^c\|Ig_1(r)\|_2\,dr+\sum_\lambda\|Ij_{1,\lambda}\|_2
                  \right].
 \quad}
 \tag{WUR.17}
$$
For operator-valued inputs the integrand and impulse norms are the full norms in one common declared input space. A source written only in $H^{-1}$ needs its actual $I:H^{-1}\to L^2$ conversion; (WUR.17) already uses the complete primitive.

This is a new symbolic product, not a numerical evaluation. There is no extra $J_\star$, $q_-^{-1/2}$, wave multiplicity or $n_g$ factor. The complete $m_{11}$ still pays all interior primitive-to-mean-to-primitive feedback. The cut term still has both comparison inputs.

Only a proved jump $(j_1,0)$ may use this formula. General jumps keep both rows and their means. No jump receives a radial-length factor. The volume integral is ordinary physical $dr$; a changed variable needs its Jacobian. None of this extends the strict receiver to the root where $q=0$.

The original record paths inside the ST execution's actual_scientific_receipt are:
- complete_new_strict_propagation_conclusion.complete_reverse_matrix[0][0];
- complete_endpoint_and_source_conclusion.waist_output_factor.

Their entire same-family domain and all-shorter-product qualification are retained. The scalar source mean is zero; the independent physical mean state and its feedback are not.

## WUR4. The whole signed tuple with the original endpoint target fixed

Fix WAD's original $Y_{W,J}(0)$ and its homogeneous $Y_{\rm free}$ below the cut. For the new raw trial define
$$
 V_{\mathscr U}=\mathfrak D_r\mathscr U,\qquad
 e_c^{\mathscr U}=Y_{\rm free}(c)-V_{\mathscr U}(c),\qquad
 e_0^{\mathscr U}=V_{\mathscr U}(0)-Y_{W,J}(0).
$$
The complete same-row identity is
$$
 \begin{aligned}
 E_*={}&E_{\rm AW}+U_D(0,c)e_c^{\mathscr U}
 +\int_0^cU_D(0,r)\mathfrak D_r(g_1,0)\,dr\\
 &+\sum_\lambda U_D(0,r_\lambda)
                    \mathfrak D_{r_\lambda}[\mathscr U]_\lambda
 +e_0^{\mathscr U}.
 \end{aligned}
 \tag{WUR.18}
$$
Every term has the same original natural root input. The cut difference is not assumed to have first-row form. $E_{\rm AW}$ retains PC/ST4 and the full genuine/free/positive-side qualification. Equality of two trial root traces does not make the actual positive correction zero.

For each original observation $b$, with $v_b$ and $\Gamma_b$ as in WAD, the row dual is
$$
 \begin{aligned}
 E_\partial^*b={}&E_{\rm AW}^*v_b+
 (e_c^{\mathscr U})^*\Gamma_b(c)
       +\int_0^c g_1(r)^*\lambda_{b,1}(r)\,dr\\
 &+\sum_\lambda[\mathscr U]_\lambda^*\lambda_b(r_\lambda)
 +(e_0^{\mathscr U})^*v_b .
 \end{aligned}
 \tag{WUR.19}
$$
This is a single signed dual sum before a norm. Only the first adjoint component pairs with the completed ordinary source, while all adjoint components evolve.

For $B=V_{\mathscr U}-Y_{W,T}$ relative to WAD's full old trial, the exact replacement rules are
$$
 F_{\mathscr U}=F_{\rm old}+(\partial_r-G_D)B,\quad
 j_{\mathscr U}=j_{\rm old}+[B],\quad
 e_c^{\mathscr U}=e_c^{\rm old}-B(c),\quad
 e_0^{\mathscr U}=e_0^{\rm old}+B(0).
 \tag{WUR.20}
$$
Distributional Duhamel makes these changes cancel in (WUR.18). The root/cut and waist changes cannot be omitted independently of the new source.

A sufficient positive same-row bound is consequently
$$
 C_\partial^{\mathscr U}\le
 C_{\rm PC}+C_{\rm ST4}+g_c C_{\rm cut}^{\mathscr U}
 +O_0m_{11}(C_{Ig_1}+C_{Ij})+C_{\rm waist}^{\mathscr U}.
 \tag{WUR.21}
$$
Each constant must bound its full operator in the same input/output units. An old whole upper can be compared only after that identity is established. A new waist principal changes leading row and error together. Independent ports, physical mean/amplitude rows, finite cross maps and the metric Schur remain separate.

## WUR5. Exact mean normal form

Define scalar functionals
$$
 \ell_f=2\beta m\,\Pi M_uJ,\qquad
 \kappa_f=-\ell_fH_2+2\beta mK\,\Pi M_{v-m}.
$$
Then $F_m=\ell_f f'+\kappa_f f$. With $\widetilde z=z+\ell_f f$ one has
$$
 \boxed{\quad
 \widetilde z'=a_{\rm eff}\widetilde z+
       (\ell_f'-a_{\rm eff}\ell_f-\kappa_f)f,\qquad
 \widetilde z(r_*)=\ell_f(r_*)f(r_*) .
 \quad}
 \tag{WUR.22}
$$
Even when $z(r_*)=0$, the displayed new root value is retained. Reconstruct $z=\widetilde z-\ell_f f$ before using (WUR.8).

The derivative $\ell_f'$ contains the real $J_r$ and coefficient derivatives. They act in a fixed smooth dual row; they have not been set to zero. If $\ell_f f$ has a genuine seam jump, $\widetilde z$ has that jump too. Under the continuous-reference/continuous-height hypotheses below it is continuous.

A finite mean expansion can estimate the pairing of this complete smooth row with the Airy expression. It must retain the root value and all projection terms. Mean-zero height alone does not imply $\ell_f f=0$.

## WUR6. A finite two-primitive lemma using the actual parity inverse

This is a conditional finite lemma whose profile and coefficient hypotheses must be supplied for the chosen complete family.

Let $\mathscr A_n(v)$ be a linear two-profile expression including the declared signs and reflection realization. On the fixed strict interval assume
$$
 \partial\mathscr A_n(v)
   =\mathscr A_n(nHv+\mathcal A_nv),\qquad
 \mathcal A_n=\partial+n^{-1}M_{R_n},\qquad
 \|H^{-1}\|<\infty ,
 \tag{WUR.23}
$$
and an actual complete real-profile bound
$$
 \|\mathscr A_n(v)\|_2\le B_A n^{-1/6}\|v\|_\infty .
 \tag{WUR.24}
$$
All coefficient jets used below are uniformly bounded in $r,n$. $B_A$ must apply to the whole reflected column; separate signed bounds cannot be silently merged. For the extended-potential construction the matrix term in $\mathcal A_n$ includes the full $-V_{\rm ext}T_\phi E_{12}$. WUA.19--29 specifies the genuine real profile: on $[0,c]$, its positive $\rho_c=r_*-c$ makes its complete profile bound at most a fixed multiple of $n^{-1/6}(t_*\rho_c)^{-1/4}$. This supplies a finite $B_A$ only in that strict domain. The original reflected-pair factor is included in it; no numerical value is evaluated here.

Set $\mathcal R_nv=\mathcal A_n(H^{-1}v)$. The identity
$$
 I\mathscr A_n(v)=n^{-1}P\mathscr A_n(H^{-1}v)
                         -n^{-1}I\mathscr A_n(\mathcal R_nv)
 \tag{WUR.25}
$$
is exact, by differentiating $\mathscr A_n(H^{-1}v)$ and applying the original $I$. The projection and the final primitive remainder remain.

Define finite complete seminorms
$$
 k(v)=\sup_{r,n}\{\|H^{-1}v\|_\infty+
                       \tfrac14\|\mathcal R_nv\|_\infty\},
 \qquad k_2(v)=k(H^{-1}v)+\tfrac14k(\mathcal R_nv).
$$
A second use of (WUR.25), with the remaining outer $\|I\|\le1/4$, gives
$$
 \|I\mathscr A_n(v)\|_2\le B_A k(v)n^{-7/6},\qquad
 \|I^2\mathscr A_n(v)\|_2\le B_A k_2(v)n^{-13/6}.
 \tag{WUR.26}
$$
Only finitely many actual angular derivatives are used.

Assume the same actual inverse has $\|J\|_{2\to2}\le J_0$, $\eta\ge\eta_->0$ and $\|L\|_{2\to2}\le L_0$. The exact identity
$$
                         J=\eta^{-1}(I-JLI)
 \tag{WUR.27}
$$
implies
$$
 \|JP_{e0}\mathscr A_n(v)\|_2\le B_A j(v)n^{-7/6},\qquad
 j(v)=\eta_-^{-1}(1+J_0L_0)k(v).
 \tag{WUR.28}
$$
The parity of $u,\ell,v_\phi$ supplies the complete ordered identity
$$
 LP_o\mathscr A_n(a)
 =P_{e0}\mathscr A_n(\ell a)
       -2\beta P_{e0}v_\phi I P_e\mathscr A_n(ua).
 \tag{WUR.29}
$$
No unqualified full-signed inverse is needed. With $\beta_*\ge|\beta|$ and $V_1\ge\|v_\phi\|_\infty$, set
$$
 l(a)=j(\ell a)+2\beta_*V_1J_0k(ua).
$$
Then $\|JLP_o\mathscr A_n(a)\|_2\le B_A l(a)n^{-7/6}$.

Apply $I$ to (WUR.27), and use (WUR.25) in its inner $IP_{e0}\mathscr A_n(v)$. The identities $IP_e=P_oI$ and the same final $1/4$ bound give
$$
 \boxed{\quad
 \|IJP_{e0}\mathscr A_n(v)\|_2
          \le B_A c_{IJ}(v)n^{-13/6},\quad}
$$
$$
 c_{IJ}(v)=\eta_-^{-1}
 \{k_2(v)+\tfrac14 l(H^{-1}v)
                    +\tfrac14J_0L_0 k(\mathcal R_nv)\}.
 \tag{WUR.30}
$$
To see the last remainder explicitly, write
$IP_{e0}\mathscr A_n(v)=n^{-1}P_o\mathscr A_n(H^{-1}v)
-n^{-1}IP_e\mathscr A_n(\mathcal R_nv)$ inside $IJLI$.
The first term uses (WUR.29); the second uses its existing inner primitive gain and the actual norms of $I,J,L$.

Thus every remainder is an actual bounded operator. Neither the old $1/4$ bound nor a formal order label was renamed $1/n$. The two frequency gains arise from the finite identities before norm bounds.

## WUR7. True jump order and the complete body interface

Suppose the new trial is
$$
 f_n=P_{e0}n^{7/6}\mathscr A_n(w_0+n^{-1}w_1^V),
 \qquad w_1^V=w_1+B_{\rm ext}K_Tw_0 .
 \tag{WUR.31}
$$
Here $K_T=\begin{pmatrix}0&T\\1&0\end{pmatrix}$ is the original matrix, not a derivative. WUA.18 fixes a real $C^{64}$ potential cutoff, which is sufficient for the finite derivative lists used here; no unlimited differentiability or holomorphic continuation across its endpoints is asserted.

Its continuity requirements are explicit: the repaired $d,\eta$ and necessary angular derivatives are continuous at original joins; the intrinsic $q$ is smooth on the strict side; the actual rays and their necessary angular derivatives solve their first-order equations; $w_0$ is exactly L.22; $w_1$ is the actual piecewise-forced characteristic integral with its declared common root trace; and $B_{\rm ext},K_T$ are smooth on the admitted real profile domain.

Away from the root the first-order ray equations give continuous first radial derivatives of $X,T$ and their necessary angular derivatives. L.16 expresses the first radial derivative of the fold amplitude in continuous values, without assuming $m_r$ or $\eta_r$ continuous across a seam. Therefore
$$
 G=(k_*/\eta_*)^{1/6}(-T/q^2)^{1/4}E_G,\quad
 a_0=G(X_\phi^2-TT_\phi^2),\quad
 b_0=-2i\epsilon GX_\phi T_\phi
$$
give $w_0\in C_r^1$ at strict seams. A bounded step in the forcing preserves the continuity of $w_1$ but may give a jump in $w_{1,r}$. The added $B_{\rm ext}K_Tw_0$ is $C_r^1$. Hence
$$
 [f_n]_\lambda=0,\qquad
 [f_{n,r}]_\lambda
       =P_{e0}n^{1/6}\mathscr A_n([w_{1,r}]_\lambda).
 \tag{WUR.32}
$$
These are true one-sided derivatives of the same functions, not derivatives of unrelated interval bounds.

The continuous actual $A,B,d,b_2$ and same qualified inverse make $J$ continuous. The mean ODE makes $z$ continuous even when its ordinary source has a bounded step. Consequently
$$
 [h_2]_\lambda=0,\qquad [h_1]_\lambda=J[f_r]_\lambda .
 \tag{WUR.33}
$$
Its density impulse has the correlated form (WUR.15). The finite profile lemma proves
$$
 \sum_\lambda\|I[h_1]_\lambda\|_2
 \le B_A\left(\sum_\lambda
              c_{IJ}([w_{1,r}]_\lambda)\right)n^{-2}.
 \tag{WUR.34}
$$
All 3070 original interfaces can be included. An artificial grid join contributes zero only when continuity of the actual functions proves it. The finite full sum keeps the exponent; no radial length is inserted. This is a strict-interval conclusion with its admitted positive real profile gaps, not a root receiver estimate.

For the body, a sufficient exact expansion is
$$
 \mathcal Qf_n=n^{1/6}P_{e0}\mathscr A_n(r_n)+s_n,\qquad
 \int_0^c c_{IJ}(r_n)\,dr\le C_r,\qquad
 \int_0^c\|s_n\|_2\,dr\le C_s n^{-2}.
 \tag{WUR.35}
$$
The whole $s_n$ includes all remaining ordered terms, primitive/inverse endpoints, projections and means. L.5 first forcing alone does not prove this expansion. WUA.30--45 gives the separate finite $N=6$ construction and its complete operator-order bookkeeping for this target; it must be consumed in full, with its real $C^{64}$ cutoff and original input power. The present shorter $IJ$ lemma does not replace that scalar-operator calculation. No old $q_\star$ norm is subtracted to infer the new bound.

If the actual mean completion also gives
$$
 \int_0^c|F_{m,n}|\,dr\le C_F n^{-2},\qquad
 \int_0^c|z_n|\,dr\le C_z n^{-2},
$$
then (WUR.8) yields
$$
 \int_0^c\|Ig_{1,n}\|_2\,dr
 \le\left[B_A C_r+\tfrac14J_0C_s+
       \|Ik\|_{L^\infty_rL^2_\phi}C_F+
       \|IR_m\|_{L^\infty_rL^2_\phi}C_z\right]n^{-2}.
 \tag{WUR.36}
$$
The finite mean expansion and (WUR.22) can establish those two separate mean bounds, retaining the root value. $\Pi f_n=0$ alone cannot.

Thus the complete strict source and all jumps have column power $p=2$ once these finite hypotheses and the full scalar expansion have been proved. The original $n^{7/6}$ is already included. This suffices for WGT's column criterion at every $1<\sigma\le4/3$, since $2>\sigma+1/2$. It does not supply a dyadic block estimate by assumed output orthogonality.

The actual positive/root correction, the cut difference and the waist/principal replacement must still fit the same whole operator before this strict result can be called a bound for the final physical row. No small-perturbation test, finite determinant, complete incoming inverse or physical mean/metric Schur claim follows here.

## WUR8. Frozen evidence and consumption boundary

| Source | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| N: complete rows, mean and parity inverse | 8a57ec851fc9029e4319650b87360b9867d22a97 | 15539 | 0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af |
| O: full ordered scalar operator | 7a2f4fc25f209cbd5909733c8b955f24ec0ef8c8 | 12221 | 66bde1b99a6b6f51e3dadae608f53ad2e7e92d84160b582636f2ca4c7f0eae00 |
| L: first forcing and actual leading fold | 2451ca1c639f04dd69de5c01ff25e59c65a6abb3 | 15780 | a798e93d73aa64115cb43313985054e0d682a41fd1393f4efea4704301699e3a |
| JI: complete strict odd/even inverse recipe | 839fa641fe9ce3758ee69cfe3cb4299f59a3a239 | 11769 | 01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1 |
| WAD: actual adjoint, signed tuple and saved receiver | 1dfa6d56a249157b27d23d6249fb451cb9fdb6d0 | 28366 | 0a92e2e5e5c1f0e1e93bc509ad5883d20630ad9909be3b33eaff7546f641702a |
| ST actual: complete reverse matrix and source units | 94eb4c7d643edc33f696d101753e4d23a7936a26 | 47282 | b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637 |
| WUA: specified global genuine trial, finite scalar expansion and root/waist tuple | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WTS: whole trial replacement and decay criteria | 08ec2cc5289729dcbfb3de3ebc5799ba8f7dce95 | 27396 | bb7dff28f8f8f0064029a63622b2a8ef949894733fa06384c8c3b4b084dbb94d |
| WGT: weaker-window graph/high-block interface | 2827aec2afb53d395218c7d6dbf488083eb66df4 | 20433 | 231ff8b11d405591cdd23c56831a33796a61976cb813165787b6212dd2511d08 |

N, O and L have their exact original titles in the repository. The ST receipt is notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json. Its saved 25 gates and complete scope are unchanged; a later WAD consumer does not replace that count.

The next complete target is a same-column certificate for (WUR.35)--(WUR.36), the finite sum in (WUR.34), and the exact root/cut and waist terms. A later authorized consumer may read $O_0,m_{11}$ from the frozen small receipt and evaluate their new product once. It must not rerun old propagation or reuse the old $Q/F_0/F_1/T_1F_2$ trial costs under the new scalar residual's name.

All new profile, amplitude and source qualifications are explicit. No current successful numerical object is changed, and no scientific execution is asserted.
