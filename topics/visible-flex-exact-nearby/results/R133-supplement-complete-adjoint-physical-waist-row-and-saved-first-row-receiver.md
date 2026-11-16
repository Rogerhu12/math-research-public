# R133 supplement: exact adjoint of the complete physical waist row and its saved first-row receiver

2026-11-16, visible-exact / tail_connector.

**Proved here:** the complete formal adjoint of the actual moving Jacobi equation, its same-coordinate dual Cauchy realization, and an exact terminal-data formula for the one reflected physical waist row in WRA.24. The formula combines both characteristic waves before taking a norm. It retains the even mean, the ordinary source, all 3070 trial interfaces, the cut difference, PC/ST4 and the waist normalizer correction.

A second conclusion is a new, unevaluated scalar receiver for that same whole row. It uses the first row of the already saved complete ST positive matrix and the separately saved SW primitive, mean and interface budgets. It requires no old propagation, source integral, enclosure, trial or normalizer to be recomputed. No new numerical bound, incoming inverse, finite determinant, observability assertion or nonlinear solution is claimed.

All repository paths in the evidence tables are relative to `topics/visible-flex-exact-nearby`.

## WAD1. The one actual object and its spaces

Use the same continuous repaired reference and direction,
$$
 Q_\delta=\bar Q+\delta Z_{\rm can},\qquad
 \nu_\delta=\nu_0+\delta,\qquad |\delta|\le10^{-8},
 \qquad 0\le r\le r_c
       =\frac{76285779072683}{320000000000000}.
 \tag{WAD.1}
$$
The intrinsic parameter remains the fixed $\eta_0$. The reference and direction definition hashes are respectively
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47` and
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`.
The original strict denominator and coefficient qualifications are unchanged. This is the explicit reference family; its nonlinear residual is not set to zero.

The raw adjoint and propagation identities below hold on their originally qualified full real family. Consumption of the particular completed SW trial and its selected common-angle coefficients is restricted to that same selected parameter and same original root column. A broader propagation certificate does not enlarge the selected SW coefficient domain.

The moving circle has period $\pi/2$, normalized measure and physical frequencies $4j$. Put
$$
 \partial=\partial_\phi,\qquad
 \Pi f=\langle f\rangle,\qquad P=Id-\Pi,\qquad
 I=\partial^{-1}P,\qquad I^*=-I .
 \tag{WAD.2}
$$
The full primitive--mean Hilbert state is
$$
 \mathcal Y=
    (L^2_0(\mathbb T))^2\oplus\mathbb C^2
 \tag{WAD.3}
$$
with the Euclidean sum norm. The real Fourier-conjugate realization is retained. The source of the homogeneous high-column strong difference is the original reflected natural root space $\mathcal H_{\rm nat}^{-4/3}$, with the same cutoff $|j|\ge97$. Its dual below means the corresponding $H^{4/3}$ natural subspace with the original distributional pairing. None of the angular projectors replaces an independent radial head, source or positive-side port.

Write $R f(\phi)=f(-\phi)$ and let $E$ exchange the two characteristic components. On $\mathcal Y$ the physical reflection projector is exactly WRA.23:
$$
 Q_R(y,z)=\left(\frac{y+ERy}{2},\frac{z-Ez}{2}\right).
 \tag{WAD.4}
$$
The actual reflected state is fixed by $Q_R$. The comparison trial need not already be fixed; it is projected in the actual row.

Only the primitive component of WRA's dimensionless row will be written:
$$
 B_\partial(y,z)=\frac{y_++y_-}{\sqrt2},\qquad
 \mathcal B_\partial=B_\partial Q_R .
 \tag{WAD.5}
$$
Its target is $L^2_{\rm even,0}$. The second, raw-first-mean component of WRA.22 is exactly zero on $Q_R\mathcal Y$. This is the reflected redundancy identified in WPM; it does not remove the independent even physical mean or its equation.

The complete target is
$$
 E_\partial
 =\mathcal B_\partial(Y_A-Y_{W,J})
 :\mathcal H_{\rm nat}^{-4/3}\longrightarrow L^2_{\rm even,0}.
 \tag{WAD.6}
$$
Its leading row remains $\mathcal B_\partial Y_{W,J}$. In particular the CG fee for changing to a different scalar principal is not appended to this state difference.

## WAD2. The full raw generator and its actual adjoint

Use the coefficients of moving N.2--3, writing $\beta=a_{\rm phys}'/a_{\rm phys}$ to avoid confusion with a test function. Put
$$
 \begin{gathered}
 S=u^2+Kv^2,\quad d=-\beta IS,\quad
 m=\Pi v,\quad \eta=-\gamma m,\quad q=\sqrt{-K}>0,\\
 L_{11}=-\beta(1+3u^2+Kv^2),\qquad
 L_{22}=\beta(1-u^2-3Kv^2),\qquad
 \ell=-2\beta uv,\\
 A_v=\begin{pmatrix}d&-K\eta\\ \eta&d\end{pmatrix},
 \qquad
 L=\begin{pmatrix}L_{11}&K\ell\\ \ell&L_{22}\end{pmatrix},\\
 p=\binom{u_\phi}{v_\phi},\qquad
 a=\binom{u}{Kv},\qquad
 c=\gamma\binom{Kv_\phi}{-u_\phi},\qquad e_2=\binom{0}{1} .
 \end{gathered}
 \tag{WAD.7}
$$
Here $\eta$ is the characteristic coefficient, not $\eta_0$. The full raw equation, including its even mean, is
$$
 h_r=G_hh+f,\qquad
 G_h=A_v\partial+M_L-2\beta M_p I M_{a^t}
                    +M_c\Pi_2,\qquad \Pi_2h=\Pi h_2.
 \tag{WAD.8}
$$
This is exactly N.3 after moving $d\partial$ to the right side. Neither a mean-zero replacement of $h_2$ nor a nonlinear equation for $m$ has been used.

On the real coefficient family, the complete formal adjoint in the original normalized angular pairing is
$$
 \boxed{\quad
 G_h^*\lambda
   =-\partial(A_v^t\lambda)+L^t\lambda
      +2\beta M_a I(p^t\lambda)
      +e_2\,\Pi(c^t\lambda).
 \quad}
 \tag{WAD.9}
$$
For complex inputs the pairing is Hermitian; the real coefficient transpose in this formula is its conjugate transpose.

Indeed $(A_v\partial)^*=-\partial M_{A_v^t}$, so the coefficient derivatives are retained. The two negative signs from $-2\beta$ and $I^*=-I$ give the positive third term. The adjoint of $M_c\Pi_2$ is the constant second-component injection $e_2\Pi M_{c^t}$. In particular the last term is
$$
 e_2\gamma\,\Pi(Kv_\phi\lambda_1-u_\phi\lambda_2),
 \tag{WAD.10}
$$
and is not zero in general. Nor does the nonlocal primitive commute past either multiplier.

The direct and adjoint equations have the exact identity
$$
 \lambda_r=-G_h^*\lambda
 \quad\Longrightarrow\quad
 \frac{d}{dr}\langle\lambda,h\rangle
       =\langle\lambda,f\rangle
 \tag{WAD.11}
$$
on each genuine coefficient piece. This is a pairing between a direct solution and its adjoint. It is not a conserved quadratic energy of two direct solutions and does not assert that $G_h$ is skew-adjoint or self-adjoint.

Raw reflection is $\mathscr R_h=\operatorname{diag}(-R,R)$. The original odd $u$, even $v$ and radial $K,\eta,\beta,\gamma$ give
$[G_h,\mathscr R_h]=0$, hence also
$[G_h^*,\mathscr R_h]=0$ on the smooth core. Thus the adjoint has an odd first and even second component on the physical reflected class. The latter still has a scalar mean.

## WAD3. Density coordinates, the radial gauge and the dual initial value

Use exactly the original strict matrix and radial density:
$$
 T(q)=\frac1{\sqrt{2q}}
          \begin{pmatrix}1&q\\1&-q\end{pmatrix},\qquad
 n_g=\frac{a_{\rm phys}^2}{m^2}.
 \tag{WAD.12}
$$
Define
$$
 \mathscr J\xi=(I\xi,\Pi\xi),\qquad
 \mathscr K(y,z)=\partial y+z,\qquad
 \mathfrak D_r=\mathscr J\,n_gT(q).
 \tag{WAD.13}
$$
They are the complete $H^{-1}$ raw-state / $\mathcal Y$ isomorphisms:
$\mathscr K\mathscr J=Id$ and $\mathscr J\mathscr K=Id_{\mathcal Y}$.
The mean is part of both equalities. Their dual formulas are
$$
 \mathscr J^*(g,\zeta)=-Ig+\zeta,\qquad
 \mathfrak D_r^*(g,\zeta)
      =n_gT(q)^t(-Ig+\zeta).
 \tag{WAD.14}
$$
The constant vector $\zeta$ in this expression is injected on the circle.

Let $G_{\rm SP}$ be the full ungauged primitive--mean block in SP.6 or SF.6--7. The density generator and evolution are
$$
 G_D=(\mathfrak D_r)_r\mathfrak D_r^{-1}
              +\mathfrak D_rG_h\mathfrak D_r^{-1}
       =G_{\rm SP}+\frac{n_g'}{n_g}Id,\qquad
 U_D(r,s)=\mathfrak D_r\mathcal E(r,s)\mathfrak D_s^{-1}.
 \tag{WAD.15}
$$
The derivative in the first term is the full derivative of the actual coordinate. In particular its $m'$ and background mean residual are retained. Formula (WAD.15) does not impose $m'=\beta m(1-\langle S\rangle)$.

For $b\in L^2_{\rm even,0}$ let
$$
 v_b=Q_RB_\partial^*b
      =\left(\frac b{\sqrt2},\frac b{\sqrt2};0,0\right),
 \qquad
 \Gamma_b(r)=U_D(0,r)^*v_b .
 \tag{WAD.16}
$$
Then
$$
 \Gamma_b'=-G_D^*\Gamma_b,\qquad \Gamma_b(0)=v_b.
 \tag{WAD.17}
$$
This is the waist-specified adjoint evolved toward the cut. No independent boundary condition is imposed at the cut.

The associated raw adjoint is $\lambda_b(r)=\mathfrak D_r^*\Gamma_b(r)$. Equations (WAD.14)--(WAD.17) give its exact initial value
$$
 \boxed{\quad
 \lambda_b(0)
       =-\frac{n_g(0)}{\sqrt{q(0)}}\binom{Ib}{0}.
 \quad}
 \tag{WAD.18}
$$
There is no extra characteristic factor $\sqrt2$. For the unscaled physical row $Ih_1(0)$ the corresponding initial value is simply $(-Ib,0)^t$. The second component is zero only at this initial point; (WAD.9) generally creates an even second component and its mean immediately.

A useful exact radial re-expression is
$$
 \Xi_b(r)=\frac{n_g(r)}{n_g(0)}\Gamma_b(r),
 \qquad
 \Xi_b'=-G_{\rm SP}^*\Xi_b,\qquad \Xi_b(0)=v_b.
 \tag{WAD.19}
$$
The scalar gauge cancels because the coefficients are real and radial.
For an ungauged source $F=(F_y,F_z)$, a corresponding impulse $j$ and a density cut value $e_c$ this yields, in their respective exact units,
$$
 \begin{aligned}
 \langle\Gamma_b(r),n_g(r)F(r)\rangle
       &=n_g(0)\langle\Xi_b(r),F(r)\rangle,\\
 \langle\Gamma_b(r_\ell),n_g(r_\ell)j_\ell\rangle
       &=n_g(0)\langle\Xi_b(r_\ell),j_\ell\rangle,\\
 \langle\Gamma_b(r_c),e_c\rangle
       &=\frac{n_g(0)}{n_g(r_c)}
                                \langle\Xi_b(r_c),e_c\rangle .
 \end{aligned}
 \tag{WAD.20}
$$
The last line is a density cut pairing; it is not assigned the same injection factor as an ungauged volume source.

## WAD4. Exact reflection compression before any wave norm

The involution on $\mathcal Y$ is $\operatorname{diag}(ER,-E)$. The raw intertwining
$\mathfrak D_r\mathscr R_h
=\operatorname{diag}(ER,-E)\mathfrak D_r$
and (WAD.8) prove that $G_D$, its evolution and its adjoint commute with $Q_R$.

There is a particularly simple isometry onto the physical reflected state:
$$
 \mathfrak E(f,\zeta)
   =\frac1{\sqrt2}(f,Rf;\zeta,-\zeta),
 \quad
 \mathfrak E^*(F_+,F_-;\zeta_+,\zeta_-)
   =\left(\frac{F_++RF_-}{\sqrt2},
          \frac{\zeta_+-\zeta_-}{\sqrt2}\right).
 \tag{WAD.21}
$$
It maps $L^2_0\oplus\mathbb C$ onto $Q_R\mathcal Y$, with
$\mathfrak E\mathfrak E^*=Q_R$ and
$\mathfrak E^*\mathfrak E=Id$.
Moreover
$$
 B_\partial\mathfrak E(f,\zeta)
                =\Pi_R^+f,\qquad \Pi_R^+=(Id+R)/2 .
 \tag{WAD.22}
$$
The scalar $\zeta$ is still a state coordinate, even though it has no direct output in this row.

Thus the compressed adjoint
$\widehat\Gamma_b=\mathfrak E^*\Gamma_b$
has initial value $(b,0)$ and generator
$-(\mathfrak E^*G_D\mathfrak E)^*$.
For every complete source, including one whose comparison trial was not reflected in advance,
$$
 \langle\Gamma_b,F\rangle
     =\left\langle\widehat\Gamma_b,
           \left(\frac{F_++RF_-}{\sqrt2},
                 \frac{F_{z,+}-F_{z,-}}{\sqrt2}\right)\right\rangle .
 \tag{WAD.23}
$$
This is the actual signed two-wave contraction. Replacing the two entries on the right by separate magnitudes before forming them would discard this correlation. No extra sum of two identical wave bounds or unqualified factor two is required.

The actual repaired background and direction have identity homogeneous transmission, as proved in SP.6--7. Accordingly this adjoint has continuous state transmission at the same joins. This assertion is specific to that continuous reference. It does not replace the nontrivial density transmission of a different discontinuous raw candidate by the identity.

## WAD5. The complete row is one dual sum

Retain the full ordered normalizer and the same SW single-symbol trial:
$$
 T=(1+\mathbf S I)(1+\mathbf ZI^2),\qquad
 Y_{W,T}=n_g\binom{PTW}0,\qquad
 Y_{W,J}=n_g\binom{P\mathscr T_{J_s}W}0,
 \quad J_s=268435456 .
 \tag{WAD.24}
$$
Bold $\mathbf Z$ is the second normalizer, not the Fourier sign.
Write, in the exact increasing-$r$ jump convention,
$$
 \begin{gathered}
 F=(P[T D_W-\mathcal QW],\,-Z_yTW),\qquad
 F_D=n_gF,\\
 j_\ell=(PT_1[\mathbf Z]_\ell I^2W,0),\qquad
 j_\ell^D=n_g(r_\ell)j_\ell,\\
 e_c=Y_{\rm free}(r_c)-Y_{W,T}(r_c),\qquad
 e_0=n_g(0)\binom{P(T-\mathscr T_{J_s})(0)W(0)}0,\\
 E_{\rm AW}=Y_A-Y_{\rm free}(0).
 \end{gathered}
 \tag{WAD.25}
$$
The full $\mathcal Q$, including $F_0,F_1,T_1F_2$, is retained.
$Z_yTW$ is its independent complete mean source; it has not been projected away. The cut state $Y_{\rm free}$ is the original free-cut state continued by the actual homogeneous physical equation below the cut.

Exactly WRA.29--30 gives
$$
 E_{*,W}
  =E_{\rm AW}+U_D(0,r_c)e_c
       +\int_0^{r_c}U_D(0,r)F_D(r)\,dr
       +\sum_{\ell=1}^{3070}U_D(0,r_\ell)j_\ell^D+e_0.
 \tag{WAD.26}
$$
All displayed signs are positive: the forward error equation has forcing $-F_D$ and jump $-j_\ell^D$, and is integrated toward decreasing $r$. Every impulse is a state jump with no artificial radial length. The 2549 genuine and 521 conservative joins are both retained.

Take adjoints of the **whole** identity, restricted to the same natural high input. For every even meanzero $b$,
$$
 \boxed{\begin{aligned}
 E_\partial^*b={}&E_{\rm AW}^*v_b+e_c^*\Gamma_b(r_c)\\
  &+\int_0^{r_c}F_D(r)^*\Gamma_b(r)\,dr
       +\sum_{\ell=1}^{3070}(j_\ell^D)^*\Gamma_b(r_\ell)
       +e_0^*v_b .
 \end{aligned}}
 \tag{WAD.27}
$$
Each star on a source or endpoint operator is its actual dual from $\mathcal Y$ to $(\mathcal H_{\rm nat}^{-4/3})^*$. Thus the complete norm is exactly
$$
 \|E_\partial\|
   =\sup_{\substack{b\in L^2_{\rm even,0}\\\|b\|_2=1}}
       \left\|E_{\rm AW}^*v_b+e_c^*\Gamma_b(r_c)
          +\int F_D^*\Gamma_b\,dr
          +\sum_\ell(j_\ell^D)^*\Gamma_b(r_\ell)
          +e_0^*v_b\right\|_{(\mathcal H_{\rm nat}^{-4/3})^*}.
 \tag{WAD.28}
$$
The right side is a single signed dual sum. It is not a sum of its separate norms and it is not a finite set of adjoint test vectors.

The identities first hold on the original smooth core, piece by piece, with the original joins. The complete old strong majorants make the source integral and interface sum well-defined in duality and extend the difference to the stated negative input space. This argument does not assert that the oscillatory trial by itself maps that input into $L^2$.

Equations (WAD.23) and (WAD.27) are a precise place to use reflected or source-endpoint cancellation. A numerical certificate that seeks such cancellation must bound the full operator in (WAD.28), with the complete angular complement. No finite sample of adjoint data, and no subtraction of saved norm uppers, establishes that full bound.

## WAD6. What the already saved positive matrix pays for this row

SP.31--32 constructs a nonnegative $2\times2$ backward matrix $\mathsf M$ for the comparison coordinates
$$
 Y(r)=\sqrt{q(r)}\,\|y(r)\|_2,\qquad
 Z(r)=\sqrt{q(r)}\,|z(r)|.
 \tag{WAD.29}
$$
These are **ungauged** coordinates. The complete ST matrix includes the full prefix, both tails and the original curvature costs. The positive construction proves entrywise domination of every shorter ordered product and every source insertion, not merely a norm bound for one full evolution.

Let $m_{11},m_{12}$ be outward upper endpoints of its stored first-row records. Read the already completed upper bounds
$$
 O_0\ge\frac{n_g(0)}{\sqrt{q(0)}},\qquad
 I_c\ge\frac{\sqrt{q(r_c)}}{n_g(r_c)},\qquad
 J_*\ge\sup_{0\le r\le r_c}\sqrt{q(r)} .
 \tag{WAD.30}
$$
They are respectively ST's `waist_output_factor`,
`cut_input_factor` and
`complete_source_injection_upper`.
For the last field, the actual source algorithm proves
$J_*\ge C_I\max(1,q)\ge\sqrt q$ with $C_I=\sqrt{17}/4$,
including the entire saved prefix. No norm is inverted to obtain a denominator lower bound.

At the waist,
$$
 \|\mathcal B_\partial(y_D,z_D)\|_2
       \le\|y_D\|_2=\frac{n_g(0)}{\sqrt{q(0)}}Y(0).
 \tag{WAD.31}
$$
The equality is a change of coordinates; the inequality is the exact row contraction. The even mean state may contribute to $Y(0)$ through $m_{12}$ and is not deleted.

Consequently define the new, unevaluated positive row gains
$$
 \begin{aligned}
 g_c^{(1)}&=O_0I_c\sqrt{m_{11}^2+m_{12}^2},\\
 g_y^{(1)}&=O_0J_*m_{11},\qquad
 g_z^{(1)}=O_0J_*m_{12}.
 \end{aligned}
 \tag{WAD.32}
$$
They pay, respectively, a complete density cut error, an ungauged primitive volume source or impulse, and an ungauged complete mean source or impulse. An impulse uses the same gain without a length factor. A genuine $L^2_r$ source would require its actual $\sqrt{\text{length}}$ conversion; the saved SW budgets used below are already ordinary $L^1(dr)$ and receive no additional length.

Equivalently, testing the two input columns separately gives the actual adjoint bounds
$$
 \begin{aligned}
 \|\Gamma_{b,y}(r)\|_2
    &\le O_0\frac{\sqrt{q(r)}}{n_g(r)}
                            m_{11}\|b\|_2,\\
 |\Gamma_{b,z}(r)|
    &\le O_0\frac{\sqrt{q(r)}}{n_g(r)}
                            m_{12}\|b\|_2 .
 \end{aligned}
 \tag{WAD.33}
$$
Their two-column cut combination is (WAD.32). These estimates are a positive majorant of the signed adjoint formula, not a claim that its sign cancellations have already been evaluated.

This construction consumes the literal first matrix row. It does not recover a component from ST's whole Frobenius upper, and it does not identify $\mathsf M$ with the physical density propagator. The exact radial factors in (WAD.30) are essential.

## WAD7. A new complete current-only scalar candidate

The successful SW conclusion stores the following four separate complete budgets:
$$
 \begin{aligned}
 F_{\rm lead}^\#&\ge\int_0^{r_c}\|PTD_W\|\,dr,&
 F_{\mathcal Q}^\#&\ge\int_0^{r_c}\|P\mathcal QW\|\,dr,\\
 F_{\rm mean}^\#&\ge\int_0^{r_c}|Z_yTW|\,dr,&
 J_y^\#&\ge\sum_{\ell=1}^{3070}\|j_{\ell,y}\|.
 \end{aligned}
 \tag{WAD.34}
$$
They were produced as separate nonnegative expressions, with the original complete moving-angle input windows. Their exact saved paths are listed below. In particular $F_{\mathcal Q}^\#$ is the whole $\mathcal Q$ budget, not a selected term after a cancellation.

Read also the already completed whole density cut upper $E_c^\#$, the complete physical waist correction $E_0^\#$, and the independent $C_{\rm PC},C_{\rm ST4}$. A sufficient new full row bound is
$$
 \boxed{\begin{aligned}
 C_{\partial,1}={}&C_{\rm PC}+C_{\rm ST4}
          +g_c^{(1)}E_c^\#\\
      &+g_y^{(1)}(F_{\rm lead}^\#+F_{\mathcal Q}^\#+J_y^\#)
          +g_z^{(1)}F_{\rm mean}^\#+E_0^\# .
 \end{aligned}}
 \tag{WAD.35}
$$
Proof: apply (WAD.32) to the complete five terms of (WAD.26), retaining both source rows. The interface has zero mean component in this particular same-reference trial; its complete primitive jump remains. The AW bracket is bounded by its whole $C_{\rm PC}+C_{\rm ST4}$, without claiming a smaller component. The final waist record already contains its single $n_g(0)$ factor, so none is added again.

All terms have the same $\mathcal H_{\rm nat}^{-4/3}\to L^2_{\rm even,0}$ type. This is the same projected physical row as (WAD.6), with the same compressed trial. Its old whole-state upper $C_{*,W}^{\rm old}$ is independently valid for the row. A future scalar consumer may therefore retain both complete records and select
$$
 C_\partial^\#=
       \min\{C_{*,W}^{\rm old},\,C_{\partial,1}\}.
 \tag{WAD.36}
$$
The comparison must use upper endpoints of the final serialized outward records, retaining the old candidate on a tie. It is a whole-bound comparison. No individual entrywise minimum, subtraction from the total, or comparison of errors for different trials is used.

At the level of exact nonnegative budget expressions, taking a first row instead of a whole matrix norm removes the unnecessary second output. A numerical improvement, its size and its usefulness for a boundary inverse still require the new scalar calculation. This theorem does not predict that the remaining source budget becomes small.

The raw primitive $Ih_1$ differs by the original actual factor $\sqrt{q(0)}/n_g(0)$. If a numerical upper for that raw row is wanted, the saved ST `waist_input_factor` can be multiplied once into the **whole** selected bound. It is not permissible to divide by the upper $O_0$. Reconstructing raw $h_1$ supplies an $H^{-1}$ row, not a free raw $L^2$ derivative estimate.

## WAD8. Exact scalar read set and an admissible new execution scope

The current successful ST execution is
`notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json`.
Write `S = actual_scientific_receipt` within that object.
The current successful SW scientific conclusion is
`notes/single_root_first_symbol_trial_ci/run-43781399696-1/actual-scientific-conclusion.json`.
Write `W` for its root object.

| Symbol | Exact current record path |
|---|---|
| $m_{11}$ | `S.complete_new_strict_propagation_conclusion.complete_reverse_matrix[0][0]` |
| $m_{12}$ | `S.complete_new_strict_propagation_conclusion.complete_reverse_matrix[0][1]` |
| $O_0$ | `S.complete_endpoint_and_source_conclusion.waist_output_factor` |
| $I_c$ | `S.complete_endpoint_and_source_conclusion.cut_input_factor` |
| $J_*$ | `S.complete_endpoint_and_source_conclusion.complete_source_injection_upper` |
| $F_{\rm lead}^\#$ | `W.complete_new_source_and_interface_conclusion.complete_ordinary_leading_defect_L1_upper` |
| $F_{\mathcal Q}^\#$ | `W.complete_new_source_and_interface_conclusion.complete_ordinary_Q_F0_F1_T1F2_L1_upper` |
| $F_{\rm mean}^\#$ | `W.complete_new_source_and_interface_conclusion.complete_ordinary_independent_mean_L1_upper` |
| $J_y^\#$ | `W.complete_new_source_and_interface_conclusion.complete_all_interface_impulses_upper` |
| $E_c^\#$ | `W.complete_new_full_and_compressed_trial_conclusion.original_fullT_cut_error_read_verbatim` |
| $E_0^\#$ | `W.complete_new_full_and_compressed_trial_conclusion.complete_physical_waist_FT_W_correction_upper` |
| $C_{\rm PC}$ | `W.copied_complete_scalar_inputs_read_verbatim.C_PC` |
| $C_{\rm ST4}$ | `W.copied_complete_scalar_inputs_read_verbatim.C_ST4` |
| $C_{*,W}^{\rm old}$ | `W.complete_new_ordered_paid_conclusion.complete_Cstar_singleW_upper` |

These are 14 saved scalar records, with no recovery of a summand from a whole upper. The full ST positive-product conclusion and the full SW source/interface and trial scope objects should also be retained as exact identity evidence. ST's second matrix row may be preserved read-only in that complete object; no new second-row propagation is needed.

The intended new arithmetic, if authorized for one public Actions consumer, consists only of (WAD.32), the complete contributions in (WAD.35), and the whole selection (WAD.36). Its exact inputs include the old real family, selected parameter, original root column, $J_c=97$, $J_s=268435456$, ordinary interval, 3070 interfaces and the original physical means. Every old ball stays verbatim. All old exponentials, grouped products, source integrals, trial coefficients, endpoint normalizers and successful targets remain read-only.

A structurally complete run may show no improvement. Such a result is retained as the actual whole candidate and does not justify a second run of an already completed target. No bound in this note is an actual numerical result before that execution.

## WAD9. What a stronger signed certificate would have to establish

Formula (WAD.28) makes an additional exact target available: one may certify the norm of the full dual sum itself, using (WAD.23) before taking absolute values. That could retain oscillatory or reflected correlations lost in the positive majorant (WAD.35).

Such a certificate must cover every normalized even meanzero dual datum, the entire original input angular space, and every original coefficient piece. The exact flow, although generated by finite-band coefficients, is not thereby finite band. A finite Fourier Gram matrix or a finite set of adjoint terminal vectors needs its own complete complementary estimate. The complete even-mean dual column in (WAD.10), all source terms, both endpoints and all 3070 trial interfaces remain in that certificate.

Nothing in the existing norm records determines the signs needed for this stronger result. In particular the large old $\mathcal Q$ norm cannot be subtracted against another old upper. No new adjoint numerical trajectory, signed pairing or complete complementary bound is asserted here.

The single-row result also does not prove range surjectivity or observability. The same-graph stable coordinate inverse changes both the row and its leading map by the same right factor. Independent PW/source, radial head, second-reference, even-mean, amplitude, exterior and metric-parameter data remain independent columns of the actual matching problem.

In the selected target angle, the normalized physical state row of WPL.45 is precisely
$$
 \frac1{\sqrt2}U_{\mathcal H^{-1}}E_\partial N_i .
 \tag{WAD.37}
$$
This follows directly from $B_\partial=e^T/\sqrt2$ and the actual common input order. A symbolic upper is
$K_{H^{-1},0}C_\partial^\#\|N_i\|/\sqrt2$.
The full leading row must undergo that same left and right change. There is no additional WT inverse in this particular readout, and no coordinate cancellation removes an interior source.

## WAD10. Frozen evidence and scope

| Primary | Path | Git blob | Bytes | SHA256 |
|---|---|---|---:|---|
| Complete raw moving scalarization | `results/R133-supplement-complete-moving-root-scalarization.md` | `8a57ec851fc9029e4319650b87360b9867d22a97` | 15539 | `0645cf460507ea587056b6969b01dc532b6623179db5598e2bffe4f53a8275af` |
| Complete primitive/mean propagation | `results/R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md` | `9fc2e2c565738b1a6d0fc5962703e01f43b483bf` | 20730 | `ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4` |
| Complete strict first-symbol defect | `results/R133-supplement-complete-strict-first-symbol-propagation-defect.md` | `0f93e925d354133675b84ffeaa959a0b58d339a0` | 35289 | `add091118ef1af71bc8c4be275742d4124a076d6cf2ebaf00d35c66f8348f2b4` |
| Same single-symbol trial | `results/R133-supplement-single-complete-root-first-symbol-trial-and-ordered-waist-error.md` | `d01094f9dd6b858dd80fe12da5d0790f0c210d1a` | 24343 | `72bb6b3c9a7ae6ac660ded4d08ac67a986a43d58fcd3d1d7a95e3deb14d0ae6d` |
| Actual complete reflected row | `results/R133-supplement-complete-reflected-incoming-error-and-physical-waist-row-defect.md` | `ffe98b2256041bdc4a49d85146ddc48afb301e2c` | 26647 | `40fb2167aa27c9f9e07bfcaea89c6f5d20059cc724eb7ba4930e02b16dd27889` |
| Complete mean-rank ledger | `results/R133-supplement-physical-reflection-mean-rank-and-complete-scalar-row-ledger.md` | `f6bc0eafe774149bb768bb71c9dfc4ea39e82a15` | 23951 | `65cc1edec37adb5b0a3667c7e37df2a94bb24201697a53f4a1c7f9bc341f68c7` |
| Actual complete ST execution | `notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json` | `94eb4c7d643edc33f696d101753e4d23a7936a26` | 47282 | `b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637` |
| Frozen ST scalar source, read only | `scripts/fourfold_codazzi_strict_tail_true_cut_to_waist.py` | `e47bdce4d3716b800f6282be6a45cc3323b8119b` | 50111 | `743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5` |
| Actual SW scientific conclusion | `notes/single_root_first_symbol_trial_ci/run-43781399696-1/actual-scientific-conclusion.json` | `3dbcf931b1b98fb7a7822ef5c1ed7df10135b894` | 27687 | `f16a1dc6177ef8a76d34e859fa37a51461a6ed142f20714e3dcb9212a3647659` |
| Actual SW proof | `results/R133-supplement-actual-single-complete-root-first-symbol-trial-and-ordered-waist-error.md` | `de4d6199fefd76ab553ae1d7dd97188d333f2553` | 24024 | `803afd6aa54195839837cfc7a82810e4e087770be4e83da4ad29fd37e65b555d` |

The ST source was read for its original `propagate` and
`endpoint_readouts` construction only. It was not imported or executed. The SW scientific conclusion was read for the exact separate complete records and their source, interval, mean and interface scope. No old binary, native array or successful scientific target was restored or evaluated for this note.

The output is an analytic identity and a conditional new scalar recipe. All original successes remain frozen.
