# R133 supplement: complete fourth angle derivatives from saved cut and flow bounds

2026-11-15, visible-exact / root.

**Proved analytic bounds and a new scalar consumption contract.** The actual true common-input angle in WX has complete third and fourth derivative bounds obtainable from already saved FA, TC and WX quantities and the existing AC conjugacy theorem. This note proves the missing formulas. It performs no new numerical calculation, repeats no successful phase or flow target, and does not differentiate a remainder norm or an asymptotic Airy error.

The result concerns the same selected explicit reference. It is not a coordinate theorem for an unconstructed nonlinear solution. Its intended use is the complete transported sign-operator estimate following MS; no incoming inverse, finite Schur inverse or full return is asserted.

## DX1. One object and the exact orders

Use the original physical circle of length $\pi/2$, normalized measure, and Fourier frequencies $4j$. The real repaired family is
$$
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad
 |\delta|\le10^{-8},\qquad \eta_{\rm intrinsic}=\eta_0,
 \qquad r_c=\frac{76285779072683}{320000000000000}.
 \tag{DX.1}
$$
The actual root lies in the original complete interval
$$
 \left[\frac{1191984371497}{5000000000000},
             \frac{2383968743003}{10000000000000}\right].
 \tag{DX.2}
$$
At the same cut let $\rho=r_*(\delta)-r_c$. The complete old real and complex coefficient qualifications remain those of FA and TC.

Write $t=-T>0$, $\omega=2t^{3/2}/3$ and, in the physical characteristic convention of TC,
$$
 \Phi_\sigma^c=X-\sigma\omega,\qquad \sigma=\pm1.
 \tag{DX.3}
$$
The displayed sign of FA's oscillatory expansion is relabeled as in MS; all absolute derivative bounds here hold for both branches.

The true waist maps and the selected input map obey
$$
 X_{-\sigma}=\Phi_\sigma^c\circ\chi^\sigma_{0\to r_c},
 \qquad
 \psi=X_-\circ h,\qquad h=\mathcal H^{-1},
 \qquad
 \mathcal S=U_\psi=U_{\mathcal H^{-1}}U_{X_-}.
 \tag{DX.4}
$$
These are the same root-labelled maps as WX.3 and WX.22. The waist-based characteristic flow alone is not the root-labelled phase. The selected pair $(\delta_*,\mathcal H)$ has the AC scope
$|\delta_*|<9.368259853002\,10^{-11}$.
The full-family cut and flow estimates restrict to that same member before the final composition with $h$.

## DX2. The complete saved holomorphic inputs

The successful FA run 43763658978/1 stores, in
complete_new_cut_domain_conclusion, the following exact fields:

| Symbol | Saved field and mathematical meaning |
|---|---|
| $x$ | complete_x_deviation_holomorphic, bounding $X_\phi-1$ on the original fold strip |
| $y$ | complete_y_holomorphic, bounding $T_\phi$ on that same strip |
| $t_-$ | complete_negative_T_real_lower, a positive real-circle lower bound for $-T$ |
| $t_+$ | complete_T_holomorphic_upper_read_from_original_full_Ap, a full-strip modulus upper bound for $T$ |
| $s$ | original_fold_full_strip, exactly $3/128$ |

These meanings follow from the frozen FA source new_domain_and_jets, rather than from the variable names alone. The original complete fold source uses $j$ as the bound for $X_\phi-1$ and $B_T$ as the bound for $T_\phi$ on its full radial disk and angular strip. The exact root zeros are
$X_\phi-1=O(\rho)$ and $T_\phi=O(\rho^2)$.
FA restricts the radial disk by the Schwarz factors
$\rho_{\max}/R_G$ and $(\rho_{\max}/R_G)^2$, with
$R_G=3/8000$, at fixed angular strip $s=3/128$.
It stores the resulting $x,y$. Its separate output width $1/1024$ for the finite amplitude calculus does not reduce the domain of these two saved full-fold bounds.

The FA source explicitly distinguishes this complete holomorphic $t_+$ from real-circle phase derivative bounds. No TC real derivative jet is promoted to a holomorphic bound in this argument. In particular no fractional power of a complex $T$ is needed below: all differentiations of $\omega$ are at real $t\ge t_->0$.

For reference, the original records, unchanged, are
$$
\begin{split}
x:\;&[4.55844376549463516474490522033794083355064594078\,10^{-7}
                         \mathbin{+/-}5.42\,10^{-56}],\\
y:\;&[2.68755176938555114142267323450591210618838716970\,10^{-11}
                         \mathbin{+/-}4.07\,10^{-59}],\\
t_-:\;&[1.70443496747448880369391637399607647581261784951\,10^{-5}
                         \mathbin{+/-}1.89\,10^{-53}],\\
t_+:\;&[1.77000345209349402882117476874062226189033505433\,10^{-5}
                         \mathbin{+/-}4.44\,10^{-53}].
\end{split}
\tag{DX.5}
$$
A numerical consumer reads the original ball strings and takes the lower endpoint only for $t_-$ and upper endpoints for $x,y,t_+$. The formatted display above does not replace the original records.

## DX3. A fourth derivative of each genuine cut phase

Cauchy's estimate for the bounded periodic holomorphic functions
$X_\phi-1$ and $T_\phi$ gives
$$
 |X^{(4)}|\le\frac{6x}{s^3},\qquad
 |t^{(k)}|\le t_k:=\frac{(k-1)!\,y}{s^{k-1}},
 \quad 1\le k\le4.
 \tag{DX.6}
$$
Here derivatives are with respect to the original physical angle.
For an open strip, apply the estimate on every smaller disk and take the limit. Both Fourier signs and the complete analytic tail are included.

For $f(t)=2t^{3/2}/3$,
$$
 f'(t)=t^{1/2},\quad
 f''(t)=\frac1{2t^{1/2}},\quad
 f'''(t)=-\frac1{4t^{3/2}},\quad
 f''''(t)=\frac3{8t^{5/2}} .
 \tag{DX.7}
$$
The complete fourth chain rule is
$$
 \omega^{(4)}
 =t^{1/2}t^{(4)}
  +\frac{4t't'''+3(t'')^2}{2t^{1/2}}
  -\frac{3(t')^2t''}{2t^{3/2}}
  +\frac{3(t')^4}{8t^{5/2}} .
 \tag{DX.8}
$$
Consequently the following whole positive expression bounds both actual cut phases:
$$
 \boxed{\;
 P_4=
 \frac{6x}{s^3}
 +t_+^{1/2}t_4
 +\frac{4t_1t_3+3t_2^2}{2t_-^{1/2}}
 +\frac{3t_1^2t_2}{2t_-^{3/2}}
 +\frac{3t_1^4}{8t_-^{5/2}}
 \ \ge\ \max_\sigma\|(\Phi_\sigma^c)^{(4)}\|_\infty .
 \;}
 \tag{DX.9}
$$
Every term is a derivative of a known true phase coefficient. This is independent of the Airy first-omitted error estimate.

The already successful TC conclusion supplies the other cut quantities:
$$
 P_1=\operatorname{upper}(\text{phase_derivative_upper}),\quad
 P_2=\operatorname{upper}(\text{phase_second_derivative_upper}),\quad
 P_3=\operatorname{upper}(\text{complete_new_three_phase_third_derivative_upper}).
 \tag{DX.10}
$$
The first two fields are in complete_density_coordinate_conclusion; the third is in its accepted_phase_domain_read_verbatim.
The accepted $P_3$ record is
$[0.004984937854345038735264830795484622187300073068694190
\mathbin{+/-}4.26\,10^{-55}]$.
It is read as already proved, not reconstructed from an inverse-phase bound.
The actual positive first-derivative lower bound also remains the existing TC value.

## DX4. One additional derivative of every shorter true flow

WX proves, from the specific saved SP/ST positive algorithm, that
$$
 e^{\int D\,dr}\le M,\qquad
 D(r)\ge\|d_\phi(r)\|_\infty,\qquad M\ge1
 \tag{DX.11}
$$
for every shorter interval and either time orientation.
The complete drift $d$ has angular label degree at most $192$.
Read from the actual WX receipt
$$
 \kappa_2=768\sqrt{385},\qquad
 \kappa_3=768^2\sqrt{385},\qquad
 M=M_\chi,\quad F=F_\chi,\quad G=G_\chi.
 \tag{DX.12}
$$
All five values are existing outward records. Their old square roots, positive propagation products and second/third derivative targets are not recalculated.
The same finite-support inequality additionally gives
$$
 \|d_{\phi\phi\phi\phi}\|_\infty\le\kappa_4D,
 \qquad \kappa_4=768\kappa_3.
 \tag{DX.13}
$$
Only this new multiplication is required for the additional angular multiplier.

For the genuine directed flow write
$J=\chi'$, $K=\chi''$, $L_3=\chi'''$, $L_4=\chi''''$.
Besides the three WX variational equations, direct differentiation gives
$$
 \dot L_4=\pm d_\phi L_4
       \ \pm4d_{\phi\phi}JL_3
       \ \pm3d_{\phi\phi}K^2
       \ \pm6d_{\phi\phi\phi}J^2K
       \ \pm d_{\phi\phi\phi\phi}J^4 .
 \tag{DX.14}
$$
The initial values are $J=1$ and $K=L_3=L_4=0$.
The signs depend on time orientation and disappear only after absolute values.

Put $a=\int D$ and $m=e^a$. The same variation-of-constants argument used in WX gives
$$
 |K|\le\kappa_2m(m-1),\qquad
 |L_3|\le\frac m2
       \{3\kappa_2^2(m-1)^2+\kappa_3(m^2-1)\}.
 \tag{DX.15}
$$
Dividing (DX.14) by the positive $J$ and applying these estimates bounds the complete integral for $|L_4|/J$ by
$$
 \int\!\left\{
 9\kappa_2^3m(m-1)^2
 +2\kappa_2\kappa_3m(m^2-1)
 +6\kappa_2\kappa_3m^2(m-1)
 +\kappa_4m^3\right\}\,da .
 \tag{DX.16}
$$
For the term $K^2/J$, one uses
$|K|/J\le\kappa_2(m-1)$ and $|K|\le\kappa_2m(m-1)$;
an upper bound for $1/J$ is not substituted in place of this correlated estimate.

Integrate with $dm=m\,da$, and use $J\le m\le M$.
Every final polynomial in $M-1$ has nonnegative coefficients. The result is
$$
 \boxed{\;
 H_\chi=M\left\{
 3\kappa_2^3(M-1)^3
 +\frac{\kappa_2\kappa_3}{3}(M-1)^2(8M+7)
 +\frac{\kappa_4}{3}(M-1)(M^2+M+1)
 \right\}
 \ \ge\ \|\chi''''\|_\infty .
 \;}
 \tag{DX.17}
$$
The expression is valid for all shorter intervals and both orientations; the inverse flow is another such directed flow.
The factorized final term avoids subtracting two unrelated upper bounds.
No new exponential or radial integral is evaluated.
The common $M$ is justified by the original positive algorithm, not by inverting an arbitrary operator-norm upper bound.

## DX5. The actual root-labelled waist third and fourth derivatives

Apply the ordinary composition rule to (DX.4), with the true cut and directed flow in their stated order. New complete bounds are
$$
 \boxed{\quad
 W_3=P_3M^3+3P_2MF+P_1G ,
 \quad}
 \tag{DX.18}
$$
and
$$
 \boxed{\quad
 W_4=P_4M^4+6P_3M^2F+3P_2F^2+4P_2MG+P_1H_\chi .
 \quad}
 \tag{DX.19}
$$
They bound $\max_\sigma\|X_{-\sigma}'''\|_\infty$ and
$\max_\sigma\|X_{-\sigma}''''\|_\infty$ on the full real family.
The terms $3P_2F^2$ and $4P_2MG$ are distinct and are both retained.

The already successful WX fields
phase_derivative_upper and phase_second_derivative_upper in
complete_waist_density_coordinate_conclusion supply $W_1,W_2$.
Read those whole bounds unchanged. Do not recalculate their previous formula and do not rename a cut bound as a waist bound.

## DX6. The selected true inverse angle and the final composition

AC.2 and AC.9 already prove the complete real bounds
$$
 m_H=\frac{31}{32}\le\mathcal H'\le\frac{33}{32},\qquad
 \|\mathcal H''\|_\infty\le H_2=4,\quad
 \|\mathcal H'''\|_\infty\le H_3=1024,\quad
 \|\mathcal H''''\|_\infty\le H_4=393216 .
 \tag{DX.20}
$$
These use the full accepted Wiener strip and its infinite tail. They do not depend on the unfinished SN terminal calculation.

Read the existing WX inverse-angle first and second derivative bounds as $h_1,h_2$ from complete_selected_H_coordinate_conclusion.
Implicit differentiation of $\mathcal H\circ h=\mathrm{id}$ gives the new positive bounds
$$
 h_3=\frac{3H_2^2}{m_H^5}+\frac{H_3}{m_H^4},
 \qquad
 h_4=\frac{15H_2^3}{m_H^7}
        +\frac{10H_2H_3}{m_H^6}
        +\frac{H_4}{m_H^5}.
 \tag{DX.21}
$$
They bound the third and fourth derivatives of the same actual inverse $h$.
All inverse-Jacobian terms are present; a forward derivative bound is not assigned to the inverse by notation.

The two new complete selected input bounds are therefore
$$
 \boxed{\quad
 M_{\psi,3}=W_3h_1^3+3W_2h_1h_2+W_1h_3 ,
 \quad}
 \tag{DX.22}
$$
$$
 \boxed{\quad
 M_{\psi,4}=W_4h_1^4+6W_3h_1^2h_2
       +3W_2h_2^2+4W_2h_1h_3+W_1h_4 .
 \quad}
 \tag{DX.23}
$$
The complete positive lower bound $m_\psi$, first derivative upper bound and second derivative upper bound $M_{\psi,2}$ are the unchanged fields in WX's complete_selected_common_input_conclusion. Its four same-window density norms for $\mathcal S$ and $\mathcal S^{-1}$ are also read unchanged.

Equations (DX.22)--(DX.23), together with those saved fields, supply the full real $C^4$ input of the transported sign-operator lemma. They do not imply that $\mathcal S$ is unitary, that $Z^{\mathcal S}$ is finite rank, or that its original position may be changed without the corresponding exact operator term.

## DX7. A current-input-only numerical contract

A subsequent public Actions consumer may evaluate the new positive formulas (DX.6), (DX.9), (DX.13), (DX.17)--(DX.19), and (DX.21)--(DX.23). It must preserve, verbatim:

1. The four FA cut records, its full strip, and the original real parameter/root/cut qualifications.
2. The three TC cut derivative bounds, including the actual third derivative from the complete original phase-domain record.
3. The five WX shorter-flow records, the two existing waist derivatives, the two existing inverse-$\mathcal H$ derivatives, the complete selected input scope and its saved lower/second-derivative and density-norm records.
4. The exact AC analytic constants and selected-parameter restriction.

Only the additional fourth-derivative and composition expressions are new.
No successful fold, TC coordinate, WX shorter flow, KAM, root, ray, Airy, profile or source target may be rerun. No binary or original data arrays are needed by this consumer.
Original source files, if included for identity/AST closure, are evidence and are not imported as mathematical producers.

A separate complete sign estimate may consume these new same-map bounds and the existing MS/WE factors. Each whole operator remains in its stated order and source/target window. The independent physical mean ports are unaffected by these scalar angle estimates; density mean-identity differences and the nonconstant column $\mathcal S1$ remain explicit.

There is no numerical claim for $P_4,H_\chi,W_3,W_4,h_3,h_4,M_{\psi,3},M_{\psi,4}$ in this note.

## DX8. Immutable source identities

All paths below are relative to topics/visible-flex-exact-nearby unless stated otherwise.

| Input | Immutable Git blob | Bytes | SHA256 |
|---|---|---:|---|
| FA actual science, notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json | 2001f4e2eeece1cda56b18b90dccab04b7f6d336 | 35718 | 2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2 |
| FA actual source, scripts/fourfold_codazzi_free_Airy_first_omitted_cut_scalars.py | 9e0a75461e0b8302a82e0444828a2c86379c3443 | 48827 | a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954 |
| TC actual execution, notes/true_branch_density_coordinates_ci/run-43754703603-1/execution.json | 5fa965e523f957432d09528641aad9f836be4561 | 38057 | 37c2a5ae3b77e7f0895aa0c3130d8707868816f1d26a119a880272f9b92f902e |
| WX analytic contract | ef394649b79b06e27d7d3a36bdf98a7fcd801039 | 20033 | c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1 |
| WX actual execution, notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json | 5121a599896025d90e2861450756a256aaba659d | 43753 | e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12 |
| AC true selected conjugacy theorem | 30591d2714e45dcad6ae2de1774a9b7e333466de | 8974 | 6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4 |
| Original full-fold source, scripts/fourfold_codazzi_anchored_auxiliary_root_fold_direct_leading.py | 27427dd6302b1d9c4ce8e0dd4a9d48fa15f920c3 | 32009 | 410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783 |

The original full-fold source was read at immutable commit a3d84d905ce72e3a854874bbe98d119623f3f8de. No original fold body or archive was restored for this analytic derivation.

The primary proof links are [FA](R133-supplement-complete-free-Airy-first-omitted-strict-cut-columns.md), [TC](R133-supplement-true-branch-density-coordinates-and-complete-finite-conjugation.md), [WX](R133-supplement-complete-true-waist-coordinates-from-saved-positive-products.md), [AC](R133-supplement-actual-conjugacy-density-transfer-for-complete-first-coefficient.md), and [MS](R133-supplement-exact-Maslov-sign-operator-and-common-input-outgoing-order.md). Their complete domains, density conventions, actual selected member and independent physical mean equations are retained.
