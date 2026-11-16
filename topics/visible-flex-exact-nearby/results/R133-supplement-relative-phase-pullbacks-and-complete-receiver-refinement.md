# R133 supplement: relative phase pullbacks and complete receiver refinement

2026-11-16. Exact same-operator identities and a 40-target continuation contract. No scientific arithmetic is executed.

WJR supplies relative ordinary derivatives of each positive phase derivative and their positive average. The same ratios improve inverse-phase derivatives and the full negative-Sobolev pullback. The latter follows by differentiating the exact density adjoint before taking norms. All output frequencies, the angular mean, and the original physical coordinates remain present.

## WRP1. The same maps, measure, and ordinary units

Use the selected strict real interval
$$
 I_{\rm s}=[0,c],\qquad c=\frac{76285779072683}{320000000000000}.
 \tag{WRP.1}
$$
The maps are the two genuine lifted far phases $\Phi_+,\Phi_-$ and the near phase $X$. Each is increasing of degree one on $\mathbb T_{\pi/2}=\mathbb R/(\pi/2)\mathbb Z$. For any one of them write
$$
 p=\Phi_\phi>0,\qquad \chi=\Phi^{-1}.
 \tag{WRP.2}
$$
The maps stay distinct; common complete estimates apply to each separately. The two exponential signs are carried by signed Fourier inputs, not by replacing an increasing map with a decreasing one.

Both circles use normalized measure $d\phi/(\pi/2)$. Physical frequencies are $4j$, and the full Bessel spaces, including $j=0$, are
$$
 \|f\|_{H^s}^2=\sum_{j\in\mathbb Z}(1+16j^2)^s|\widehat f(j)|^2,
 \qquad
 \|f\|_{H^2}^2=\|f\|_2^2+2\|f'\|_2^2+\|f''\|_2^2.
 \tag{WRP.3}
$$
Every derivative below is an ordinary physical angular derivative. A saved normalized coefficient of order $j$ is converted by $j!$ exactly once.

By WJR.21--22, common complete ordinary records $\mathcal P_b$ satisfy
$$
 |\partial_\phi^bp|\le\mathcal P_b p,\qquad b=1,2,3.
 \tag{WRP.4}
$$
For $X$ this is the proved inequality for $X_\phi=(\Phi_{+,\phi}+\Phi_{-,\phi})/2>0$, with no extra factor two.

Read the already saved complete pointwise inverse-first-derivative and $L^2$ pullback records:
$$
 \|\chi'\|_\infty\le U,\qquad
 \|C_\Phi\|_{L^2\to L^2}\le K_0,\qquad C_\Phi f=f\circ\Phi.
 \tag{WRP.5}
$$
Their original qualification covers all three maps on (1), using the genuine global strict phase lower $m_\Phi>0$. The cut lower used inside WJR is a different object. It cannot replace $m_\Phi$.

The first statement of (5) is pointwise; an arbitrary operator-norm upper is not relabeled as $U$. This proof reads the existing complete $U,K_0$ without recalculating either target or assuming an inequality between separately re-expanded old algorithm sums.

## WRP2. Relative inverse-phase derivatives

Let $r=p'/p$, $s=p''/p$, and $t=p'''/p$ be actual signed functions. Ordinary inverse differentiation gives
$$
 \chi'=\frac1{p\circ\chi},\quad
 \chi''=-\frac{r\circ\chi}{(p\circ\chi)^2},\quad
 \chi'''=\frac{(3r^2-s)\circ\chi}{(p\circ\chi)^3},
$$
$$
 \chi''''=\frac{(-15r^3+10rs-t)\circ\chi}{(p\circ\chi)^4}.
 \tag{WRP.6}
$$
Indeed $r'=s-r^2$ and $s'=t-rs$. These exact identities precede all absolute values. They imply the complete common bounds
$$
 u_1=U,\quad
 u_2=\mathcal P_1U^2,\quad
 u_3=(\mathcal P_2+3\mathcal P_1^2)U^3,
$$
$$
 u_4=(\mathcal P_3+10\mathcal P_1\mathcal P_2+15\mathcal P_1^3)U^4.
 \tag{WRP.7}
$$
Only $u_2,u_3,u_4$ are new targets. No ratio of two saved upper bounds is used to infer (4), and no periodic bound is assigned to a zeroth lift value.

## WRP3. Exact density-adjoint differentiation

Changing variables $y=\Phi(\phi)$ in the normalized inner product gives the exact adjoint
$$
 T_\Phi=C_\Phi^*,\qquad
 T_\Phi g=\chi'(g\circ\chi)=\left(\frac gp\right)\circ\chi .
 \tag{WRP.8}
$$
The period normalizations cancel. The density and its mean row remain part of this operator.

Since $\partial_y=(p^{-1}\partial_\phi)\circ\chi$, direct differentiation yields
$$
 (T_\Phi g)'=T_\Phi[p^{-1}(g'-rg)],
$$
$$
 (T_\Phi g)''=
 T_\Phi[p^{-2}\{g''-3rg'+(3r^2-s)g\}].
 \tag{WRP.9}
$$
In particular the density $p^{-1}$ in (8) has been differentiated. For a check, differentiating $p^{-1}(g'-rg)$ and applying the first identity again produces $2r^2-r'=3r^2-s$.

Adjoint equality gives $\|T_\Phi\|_{2\to2}=\|C_\Phi\|_{2\to2}\le K_0$. Apply this same complete $L^2$ bound to each entire expression in (9):
$$
 \|T_\Phi g\|_2\le K_0\|g\|_2,
$$
$$
 \|(T_\Phi g)'\|_2\le K_0U(\|g'\|_2+\mathcal P_1\|g\|_2),
$$
$$
 \|(T_\Phi g)''\|_2
 \le K_0U^2[\|g''\|_2+3\mathcal P_1\|g'\|_2
                   +(3\mathcal P_1^2+\mathcal P_2)\|g\|_2].
 \tag{WRP.10}
$$
There is no separate change-of-variables estimate with a global upper for $p$ after this step. The full original $K_0$ handles the density adjoint on the same measure.

## WRP4. A complete three-by-three bound and both negative windows

Set
$$
 h(g)=(\|g\|_2,\sqrt2\|g'\|_2,\|g''\|_2)^{\mathsf T}.
$$
This is a comparison vector in Euclidean $\mathbb R^3$. Its norm is exactly (3). Its three components are derivative seminorms; they are not a new physical state or three boundary ports.

Equation (10) gives componentwise
$$
 h(T_\Phi g)\le K_0M h(g),\qquad
 M=\begin{pmatrix}
 1&0&0\\
 \sqrt2\mathcal P_1U&U&0\\
 (3\mathcal P_1^2+\mathcal P_2)U^2&
      3\mathcal P_1U^2/\sqrt2&U^2
 \end{pmatrix}.
 \tag{WRP.11}
$$
The comparison matrix is entrywise nonnegative. Define complete row and column sums by
$$
 a=\sqrt2\mathcal P_1U,\quad
 b=(3\mathcal P_1^2+\mathcal P_2)U^2,\quad
 c_1=3\mathcal P_1U^2/\sqrt2,\quad d_1=U^2,
$$
$$
 R=\max\{1,a+U,b+c_1+d_1\},\qquad
 C=\max\{1+a+b,U+c_1,d_1\}.
 \tag{WRP.12}
$$
The positive finite-matrix Schur bound gives
$$
 \|M\|_2\le\sqrt{RC},\qquad
 \boxed{K_2^{\rm rel}=K_0\sqrt{RC}}.
 \tag{WRP.13}
$$
All entries and rows belong to this one complete comparison matrix. No off-diagonal term is deleted. A saved upper for $\sqrt2$ may be used for both $\sqrt2$ and $1/\sqrt2=\sqrt2/2$; no old upper is inverted.

Initially take smooth $g$. Equation (10) and density extend $T_\Phi$ to full $H^2$. Duality then bounds the same $C_\Phi:H^{-2}\to H^{-2}$ by (13), with distributional pullback defined through (8), agreeing with ordinary composition on smooth functions.

Interpolation of that same operator on the same fixed Bessel scale gives
$$
 K_d^{\rm rel}=K_0^{1-d/2}(K_2^{\rm rel})^{d/2},
 \quad 0\le d\le2,\qquad
 K_{5/3}^{\rm rel}=K_0^{1/6}(K_2^{\rm rel})^{5/6}.
 \tag{WRP.14}
$$
No mean-zero restriction is imposed before duality or interpolation. The two physical means in the original problem are unrelated to the auxiliary dimension three of (11).

As a symbolic normalization check, the identity phase with sharp $U=K_0=1$ and $\mathcal P_1=\mathcal P_2=0$ makes $M$ the identity and (13) equals 1.

## WRP5. All fifteen profile weights, including zero and low outputs

Let $\widehat P_0,\ldots,\widehat P_4$ be the already saved complete ordinary angular derivative envelopes for the same genuine profile packet: its near term, both far terms and all fixed frequency-dependent genuine normalization matrices. If the table stores normalized coefficients $P_j$, use $\widehat P_j=j!P_j$ once.

The saved complete zeroth envelope remains its own bound. It need not equal a sum of upper endpoints from separately printed near and far records. No near ODE, Jost scalar, potential extension or profile derivative is recalculated.

For $d\in\{0,5/3,2\}$ and $b=0,\ldots,4$, define all fifteen complete new weights
$$
 \boxed{
 W^{\rm rel}_{d,b}=2^{d/2}K_d^{\rm rel}
 \left[
 {\bf1}_{b=0}\widehat P_0+
 \frac{17}{64}\sum_{j=\max(1,b)}^4
 B_{4,j}(u_1,u_2,u_3,u_4)\binom jb\,\widehat P_{j-b}
 \right]}.
 \tag{WRP.15}
$$
Here the ordinary partial Bell polynomials are
$$
 B_{4,1}=u_4,\quad
 B_{4,2}=4u_1u_3+3u_2^2,\quad
 B_{4,3}=6u_1^2u_2,\quad B_{4,4}=u_1^4.
 \tag{WRP.16}
$$
Equations (7), (13), (14) replace their complete inverse-phase and pullback predecessors in WCPR.27--29. The profile functions and their complete saved envelopes are unchanged.

For a complete frequency-dependent amplitude family $v_j$, the original full signed-Fourier block proof therefore gives, on $N\le4|j|<2N$,
$$
 \|\mathcal U_{[N,2N)}[v]\|_{\ell^2_{\rm signed}\to H^{-d}}
 \le N^{-d}(1+N^{2/3}\rho)^{-1/4}
   \sum_{b=0}^4W^{\rm rel}_{d,b}
     \sup_j\|\partial_\phi^bv_j\|_{\infty,\rm component\ sum}.
 \tag{WRP.17}
$$
The unchanged $17/64$ is the complete physical-frequency-$4j$ summation bound of WCPR.29. Zero, low and high output modes all remain in the matrix argument. Neither output-band orthogonality nor input-frequency differentiation is assumed.

The original normalized reflection restriction is already isometric in (17) and is not charged twice. Independent reference columns, terminal-column assembly and scalar-mean rows retain their own original factors. The near and two far maps use their own actual compositions while sharing these bounds.

## WRP6. Exact continuation of a completed N6/profile receiver

This continuation consumes a complete first WSM result and the complete WJR result. It does not rerun WSM's profile construction or ordered N6 calculation.

The required old data are the complete WJR scope and three ratios; the complete WSM profile node with all five derivative envelopes and old $U,K_0$; the full WSM N6 node with all ten scalar words, internal means, retained powers, final even-mean-zero projection and terminal bounds; and the complete WSM receiver/index with the original physical tuple and provenance.

Copy the already saved complete ordinary amplitude bounds
$$
 A_b\ge\sup_{n\ge388}
 \|\partial_\phi^b(v_1+n^{-1}v_2)\|_{\infty,\rm component\ sum},
 \qquad 0\le b\le4 .
 \tag{WRP.18}
$$
They are the receiver's existing complete regrouping. Copy its moved-tail $C_3$, its same-$J$ bounds, the full collar and strict terminal receipts, and its whole terminal dyadic contribution. None depends on changing (15).

The only new retained-profile budgets are
$$
 Q_c=\sum_{b=0}^4W^{\rm rel}_{5/3,b}A_b,\qquad
 Q_t=\sum_{b=0}^4W^{\rm rel}_{2,b}A_b.
$$
Using the already saved factor $2^{1/6}$ and actual inverse norms once, set
$$
 B_c=2^{1/6}J_{-5/3}Q_c,\qquad
 B_t=2^{1/6}(IJ)_{-2}Q_t,\qquad
 B_u=\max(B_c,B_{c,\rm local}).
 \tag{WRP.19}
$$
Here $J_{-5/3}$ is the same even-mean-zero to odd inverse in its original window; $(IJ)_{-2}$ is its original ordered primitive composition. The complete original parity projection is applied before $J$. An isolated signed summand is not fed into an inverse with the wrong domain.

Every symbol in the following ordinary-source formulas, apart from the new $B_u,B_t$, is an original complete saved target:
$$
 O_c=\sqrt2\,\ell_+^{1/4}B_u+\sqrt{\ell_+}M_c\,388^{-5/3},
$$
$$
 O_t=c_{\rm PW}
       [\ell_-^{-1/4}B_t+M_t\,388^{-4/3}],
$$
$$
 R_c=C_OO_c+C_R\mathcal J_c,\qquad
 R_t=C_1(O_t+\mathcal J_t).
 \tag{WRP.20}
$$
$M_c,M_t$ are the whole mean contributions. $\mathcal J_c,\mathcal J_t$ are the complete original jump sums. The original PW cut, ordinary-$dr$ lengths and receiver windows remain unchanged. Jumps receive no artificial radial length.

Let $N_T$ be the copied whole terminal dyadic contribution, including its original $S_{1/6}$ and complete point-profile/inverse factors. Then
$$
 N_c=R_cS_{1/3},\quad N_t=R_tS_{2/3},\quad
 E_-=C_{\rm Bessel}(N_c+N_t+N_T).
 \tag{WRP.21}
$$
No old terminal upper is reduced by a subtotal or reassigned a retained-profile decay.

Copy the complete original positive response $R_+$, four-waist-endpoint sum $E_{\rm end}$, root factor fee $R_F$, ordered final readout $L_{\rm rec}$, and the separate $C_{\rm alg},D_\infty$. Define
$$
 S_{\rm nr}=R_++E_-+E_{\rm end},\qquad S_{\rm all}=S_{\rm nr}+R_F,
$$
$$
 C_{\rm whole}^{\rm rel}=C_{\rm alg}+L_{\rm rec}S_{\rm all},\qquad
 C_{\rm red}^{\rm rel}=D_\infty+L_{\rm rec}S_{\rm nr}.
 \tag{WRP.22}
$$
Compare whole and reduced separately with their own complete already selected predecessors. Preserve both candidates and let the old record win equal saved upper endpoints. A reduced candidate is not a whole candidate.

The physical scalar mean retains its exact root condition $z_{\rm ph}(r_*)=0$, both stored density means, full feedback and all original couplings. All 3070 actual interfaces, original positive/root correction, four waist terms, $n_g$ factors, normalizers, ordinary radial terms and original domains remain in their existing order. No new root, endpoint, jump or local-patch fee is calculated here.

## WRP7. Forty new targets and preserved prefixes

A complete first continuation has three graphs:

| Graph | Complete new targets | Count |
|---|---|---:|
| Relative inverses and pullbacks | $u_2,u_3,u_4,R,C,K_2^{\rm rel},K_{5/3}^{\rm rel}$ | 7 |
| Full-output profile | All $W^{\rm rel}_{d,b}$, three windows and five angles | 15 |
| Receiver and two full errors | $Q_c,Q_t,B_c,B_t,B_u,O_c,O_t,R_c,R_t,N_c,N_t,E_-,S_{\rm nr},S_{\rm all},L_{\rm rec}S_{\rm all},C_{\rm whole}^{\rm rel},L_{\rm rec}S_{\rm nr},C_{\rm red}^{\rm rel}$ | 18 |

The first graph saves $R,C$ before (13) reads their upper endpoints, and $K_2^{\rm rel}$ before interpolation. Each of the fifteen weights is complete for its declared row and window. Each received-source record is saved before its complete final error reads it. Copies of $U,K_0$, profile values, amplitudes, terminal contribution and the remaining physical tuple are verbatim original records.

This version requires only one new square root in (13) and two positive fractional powers in (14). Old $\sqrt2$ and $2^{1/6}$ are read, with integer powers for the original full-output prefactor. This note evaluates none of them.

Before execution, bind the complete successful WSM index and three actual node files by their full path, bytes, Git and SHA256. Admit their full mathematical scope. If they have only a failure prefix, this continuation does not promote it to success or authorize a rerun; an exact remaining-only contract would be required instead.

Every new record must be atomically persisted with its complete prefix before downstream use, parsed back for directed upper endpoints, and preserved on failure. The 56 WJR targets and all first-WSM targets remain immutable. Zero-order profiles and old complete products are not regenerated under new names.

No smaller bound or high-gate success is asserted before the new targets exist. The actual 96 physical columns and their still uncomputed signed normalization, $\nu,\Theta$, radial head, function-valued independent ports, cokernel rows, transported finite factors, signed finite inverses and nonlinear obligations keep their previous status.

## WRP8. Exact primary identities and read-only paths

All paths are relative to topics/visible-flex-exact-nearby/.

| Primary object | Complete identity |
|---|---|
| WJR positive phase/average ratio theorem | results/R133-supplement-relative-flow-Jacobians-and-positive-phase-ratio-bounds.md; Git b6cd802c613f7ec193329af609c63f59a6efded3; 19752 B; SHA256 741df919addd04766685724f1e6d131eef8b03bc6875f9a50ff7de9ad5061c2f |
| WJR completed actual, run 43873739440/1 | notes/relative_flow_Jacobian_ci/run-43873739440-1/actual-scientific-conclusion.json; Git 80499e42f643e607db47c973b54f2243629a05e8; 69002 B; SHA256 806fbeaaab33ddff424fcfe70e40f83f46d1f85e089f9f01f941ed38ee249660 |
| WCPR full profile and fifteen-weight proof | results/R133-supplement-complete-cut-initialization-and-positive-profile-budget-reuse.md; Git da15190045b2cb05cffdfd410ab91fc9e5673286; 23905 B; SHA256 642e6fd207af3c632ee616eadbfe9ed15797e2df5baf8f6aff050984ac84a1ad |
| Original complete strict profile node | notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_strict.json; Git f2a2687ae736d291c5d5b85e0309e625d729e5d8; 9131 B; SHA256 6e781157c43f7ba7f7e4ac454308545444164138920cbab027a7af56dd1d89a6 |

The WJR ratios are indices 0 through 2 of
complete_new_graphs.complete_new_positive_phase_average_ratio_conclusion.new_records.ordinary_common_positive_phase_and_average_ratios_1_through_14.
Its complete flags ordinary_physical_angular_derivatives, relative_ratio, common_positive_phase_average_ratio and complete_original_cut_and_all_shorter_flow are retained with the full strict interval.

The original $U,K_0$ records are inverse_phase_derivative_1_upper and complete_phase_pullback_L2_upper under the original profile's conclusion.new_complete_records. WSM copies these into its complete profile node; the continuation verifies the exact copies and original qualification.

The successful WSM receiver supplies new_records.strict_regrouping.ordinary_angles_0_4 and new_records.new_negative_receiver.complete_terminal_dyadic_contribution_upper, its copied_original_records and complete choices. Its profile supplies the saved complete_profile jet, converted to ordinary derivatives once. The full N6 node and index certify their same-source connection.

No prospective WSM Git or result is invented: those exact first-run identities are fixed only when the files actually exist. This note proves the same-operator replacement and complete continuation while performing zero scientific evaluations.
