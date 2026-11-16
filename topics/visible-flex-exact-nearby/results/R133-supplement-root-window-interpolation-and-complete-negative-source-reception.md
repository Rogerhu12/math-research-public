# R133 supplement: root-window interpolation and complete negative-source reception

2026-11-16, visible-exact / tail_connector.

**Proved analytic source and impulse estimates; no new numerical evaluation.** The complete mean-corrected trial of WUA has one odd ordinary source. Its actual angular inverse gives an $L^2_\phi$ estimate, and its additional primitive gives an $H^{-1}_\phi$ estimate. Interpolating these two estimates, then integrating in the true radial measure, puts the whole root-window source in the exact old PW input space with column decay $n^{-5/3}$. Every true root-window impulse has the same decay after a separate mixed-norm estimate.

The old radius-$1/200$ receiver keeps its original cut. Its complete constants are read from the successful SP receipt. The new near-root cut, the old PW cut, and the auxiliary potential transition are three different objects. The resulting negative-source map is bounded from the original high root space $H^{-\sigma}$ for every $1<\sigma<7/6$. A complete physical error also needs the original positive/root trace and the entire waist comparison in the final signed identity.

No old source, propagator, matrix, Fourier target, Airy value, inverse, scalar product or successful calculation is recomputed. All coefficient constants newly defined below remain unevaluated finite recipes.

## WUC1. One actual object, two cuts and one source convention

Fix WUA's selected real $\delta_*$ inside the original repaired family
$Q_\delta=Q_0+\delta Z_{\rm can}$, $|\delta|\le10^{-8}$, at the same fixed intrinsic parameter $\eta_0$ and $\nu=\nu_0+\delta$. Keep the exact physical moving angle, the original normalized circle, the full continuous repairs, the original reflection class, and the original homogeneous high root input. A supplied finite head or an independent second-reference input is not made part of this homogeneous column by notation.

Use
$$
 n=4|j|\ge388,\qquad \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_\phi^{-1}(Id-\Pi),\qquad \|I\|_{2\to2}\le1/4 .
 \tag{WUC.1}
$$
Every input column already contains WUA's declared $n^{7/6}$ normalization. The following decay statements are absolute column orders after that normalization.

Write the original exact root bracket and the two distinct cuts as
$$
 r_-=\frac{1191984371497}{5000000000000},\quad
 r_+=\frac{2383968743003}{10000000000000},\quad
 c_{\rm PW}=r_+-\frac1{200}
           =\frac{2333968743003}{10000000000000},
$$
$$
 c_{\rm new}=\frac{76285779072683}{320000000000000}.
 \tag{WUC.2}
$$
The old SP/PW receipt admits $[c_{\rm PW},r_*]$ through its complete root Cauchy theorem and $[0,c_{\rm PW}]$ through its complete strict propagation. The later ST receipt explicitly preserves the tail interval $[c_{\rm PW},c_{\rm new}]$ and the whole interval $[0,c_{\rm new}]$. Thus
$$
 0<c_{\rm PW}<c_{\rm new}<r_*,\qquad
 0<\ell_{\rm col}:=r_*-c_{\rm PW}\le1/200 .
 \tag{WUC.3}
$$
In particular the strict part $[0,c_{\rm PW}]$ is a restriction of WUA/WUR's strict domain. This uses the recorded cut identities; it does not move the old root Cauchy bound to $c_{\rm new}$.

The auxiliary profile cutoff in WUA is $L_V=1/2000$ in the $T$ coordinate. It is unrelated to $\ell_{\rm col}$ or either physical cut. Its specified $C^{64}$ regularity suffices for the finite $N=6$ calculation; no analytic continuation or unlimited derivatives across that cutoff are assumed.

The old received source spaces, including their actual measures, are exactly
$$
 F_-=\|(g_1,g_2)\|_{L^2([c_{\rm PW},r_*];
                         H^{-2/3}_\phi\oplus\mathbb C)},\qquad
 J_-=\sum_{\lambda\ {\rm in\ collar}}
       \|j_\lambda\|_{H^{-2/3}_\phi\oplus H^{-1}_\phi}.
 \tag{WUC.4}
$$
Here the second ordinary-source component is the independent angular constant allowed by PW. It is not a general uncharged second nonmean source. WUA's exact second equation and its physical mean give $g_2=0$, so this particular source belongs to (WUC.4). The state $h_2=f+z$ and its physical mean $z$ are not zero.

The coefficients $d,\eta=-\gamma m,\beta,K$ and the density factors remain those of the same original family. No value of $\gamma$, input coordinate, selected conjugacy or mean is replaced at the interface. The PW output remains the original moving-angle density pair and both full stored means. Any later selected, true-phase or physical-angle conversion keeps its own ordered window.

## WUC2. The complete first source and the two angular bounds

Let $\mathscr U_n=(h_{1,n},h_{2,n})$ be WUA's actual finite genuine trial with its scalar mean completion. On every open original piece,
$$
 g_{2,n}=0,\qquad
 g_{1,n}=G_n+M_n,\quad G_n=J\mathscr Q f_n,\quad
 M_n=F_{{\rm mean},n}k_2-z_nR_{\rm mean}.
 \tag{WUC.5}
$$
The exact operators and coefficients are WUA.34 and WUA.40--43:
$\mathscr Q=A\{(D_0-E)J(D_0-B)-KC\}$,
$k_2=Jb_2$, and
$R_{\rm mean}=(D_0-E)k_2+a_{\rm eff}k_2+b_1$.
Their primitives, projections, genuine potential, coefficient derivatives, nonlocal products and the complete mean equation are retained. In particular $\mathscr Q$ is not only the local differential part of L.5.

Set $\rho=r_*-r$, and take WUA's actual $t_*>0$ with
$|T(r,\phi)|\ge t_*\rho$. Put
$$
 b_n(\rho)=(1+t_*n^{2/3}\rho)^{-1/4}.
 \tag{WUC.6}
$$
The full genuine-profile estimate WUA.29 and its exact finite primitive formulas imply finite, unevaluated constants $A_0,A_1$ such that
$$
 \boxed{\quad
 \|G_n(r)\|_2\le A_0n^{-5/6}b_n(\rho),\qquad
 \|IG_n(r)\|_2\le A_1n^{-11/6}b_n(\rho).
 \quad}
 \tag{WUC.7}
$$
These inequalities include the actual assembly of the reflected physical column. If a different complete reference column is retained independently, its own complete constants and input multiplicity must also be retained.

For completeness, the first inequality does not assume that a general inverse gains $1/n$ on arbitrary functions. WUA.37 is the exact decomposition
$$
 \mathscr Qf_n=n^{1/6}P_{e0}\mathcal U_n^{\rm ext}(r_n)
                         +\mathcal E_{6,n}.
$$
For each retained amplitude $v$, the first finite primitive identity gives
$$
 \|IP_{e0}\mathcal U_n^{\rm ext}(v)\|_2
                       \le C_I(v)n^{-1}b_n(\rho).
$$
The exact same-parity relation
$$
 J=\eta^{-1}(I-JL_AI)
$$
therefore gives
$$
 \|JP_{e0}\mathcal U_n^{\rm ext}(v)\|_2
 \le \eta_-^{-1}(1+J_0L_0)C_I(v)n^{-1}b_n(\rho),
 \tag{WUC.8}
$$
where $J_0,L_0$ are complete norms on the admitted common radial domain. At the root these are supplied by the original local inverse; on the strict interval they come from JI's actual formula, with equality on their common domain. A root numerical constant is not extended by renaming it.

The full $N=6$ terminal sum obeys WUA.33. A terminal $J$ is bounded by its actual norm, without another claimed frequency gain. Its contribution $O(n^{-17/6}b_n)$ is smaller than the first bound in (WUC.7). This proves that bound with a complete positive constant. The second is WUA.38, or the same finite two-gain argument in WUR.25--30 with the common profile factor $b_n$ in place of its strict-interval $n^{-1/6}$ factor. This uses the whole WUA.30--37 calculation, not the first forcing or a formal symbol label alone.

The full smooth adjoint-test argument in WUA.44 gives
$$
 |F_{{\rm mean},n}(r)|\le C_Fn^{-23/6},\qquad
 |z_n(r)|\le C_zn^{-23/6}.
$$
Consequently, with complete one-sided coefficient norms,
$$
 \|M_n(r)\|_{H^{-2/3}}\le M_0n^{-23/6},\qquad
 M_0=C_F\sup_r\|k_2(r)\|_2+
                         C_z\sup_r\|R_{\rm mean}(r)\|_2 .
 \tag{WUC.9}
$$
The constants contain the actual angular derivatives of the smooth dual tests and the complete scalar integrating factor. An old $J_0$ number alone does not supply these derivatives. No endpoint term in the mean equation is dropped.

## WUC3. Root-window interpolation in the true radial measure

Both $G_n$ and $g_{1,n}$ are odd, hence have zero angular mean. On this exact space,
$$
 \|G_n\|_{H^{-1}}^2
   =\sum_{j\ne0}\Lambda_j^{-2}|(G_n)_j|^2
   \le\sum_{j\ne0}(4|j|)^{-2}|(G_n)_j|^2
   =\|IG_n\|_2^2 .
 \tag{WUC.10}
$$
No high-output support is assumed: low nonzero outputs are included in this inequality. The vanishing mean follows from physical parity, not from a Fourier truncation of the residual.

Hölder's inequality on the full Fourier sequence gives
$$
 \|v\|_{H^{-2/3}}\le
                   \|v\|_2^{1/3}\|v\|_{H^{-1}}^{2/3}.
$$
Applying it to the two bounds in (WUC.7) yields
$$
 \|G_n(r)\|_{H^{-2/3}}
 \le A_0^{1/3}A_1^{2/3}n^{-3/2}b_n(\rho).
 \tag{WUC.11}
$$
All intermediate frequencies and the complete original mean equations remain in the operator used to obtain this bound.

The radial integral is ordinary physical $dr=-d\rho$. Direct integration gives the uniform estimate
$$
 \begin{aligned}
 \int_0^{\ell_{\rm col}}b_n(\rho)^2\,d\rho
 &\le (t_*n^{2/3})^{-1/2}
             \int_0^{\ell_{\rm col}}\rho^{-1/2}\,d\rho\\
 &=2t_*^{-1/2}\ell_{\rm col}^{1/2}n^{-1/3}.
 \end{aligned}
 \tag{WUC.12}
$$
The integrable upper at $\rho=0$ is used only under this integral. No pointwise division by $q(r_*)=0$ occurs. Combining (WUC.9)--(WUC.12),
$$
 \begin{aligned}
 F_{-,n}
 &=\|g_{1,n}\|_{L^2_rH^{-2/3}}\\
 &\le \sqrt2\,\ell_{\rm col}^{1/4}t_*^{-1/4}
          A_0^{1/3}A_1^{2/3}n^{-5/3}
             +\sqrt{\ell_{\rm col}}M_0n^{-23/6}\\
 &\le C_{\rm col}n^{-5/3},
 \end{aligned}
$$
$$
 C_{\rm col}=
 \sqrt2\,\ell_{\rm col}^{1/4}t_*^{-1/4}A_0^{1/3}A_1^{2/3}
       +\sqrt{\ell_{\rm col}}M_0\,388^{-13/6}.
 \tag{WUC.13}
$$
The last line is a positive sufficient recipe using $n\ge388$. Nothing here evaluates a new power, exponential, integral constant or old saved ball.

The two separate operations matter: angular interpolation supplies $n^{-3/2}$, and the ordinary radial $L^2$ norm supplies the further $n^{-1/6}$. The $L^1$ primitive estimate in WUA.45 is not, by itself, an input to the old root receiver.

## WUC4. Every true collar impulse

Use WUA.46--47 with the true one-sided state values. Its leading amplitude is $C^1$ in $r$ across each strict seam; the complete first forcing may jump but its characteristic integral is continuous. The scalar mean solution is continuous. Thus
$$
 [h_{2,n}]_\lambda=0,\qquad
 [h_{1,n}]_\lambda=J[\partial_rf_n]_\lambda,\qquad
 [\partial_rf_n]_\lambda
       =P_{e0}n^{1/6}\mathcal U_n^{\rm ext}
                                   ([\partial_rw_1]_\lambda).
 \tag{WUC.14}
$$
This is an exact state-jump identity, not an inference from two interval upper bounds. The $C^{64}$ auxiliary transition adds no state-value jump.

Every actual interior seam in the root window has its fixed positive distance $\rho_\lambda=r_*-r_\lambda$. Applying the same one- and two-gain formulas and
$b_n(\rho_\lambda)\le(t_*\rho_\lambda)^{-1/4}n^{-1/6}$ gives finite constants $D_{0,\lambda},D_{1,\lambda}$ with
$$
 \|j_{1,n,\lambda}\|_2\le D_{0,\lambda}n^{-1},\qquad
 \|Ij_{1,n,\lambda}\|_2\le D_{1,\lambda}n^{-2}.
 \tag{WUC.15}
$$
The constants contain the actual jumps of the first forced amplitude and all needed angular derivatives. They can grow when a seam is close to the root; no root-independent numerical size is asserted. A state discrepancy at $r_*$ itself belongs to the separate root trace, not to (WUC.15).

The full mixed jump norm in PW now satisfies
$$
 \|j_{n,\lambda}\|_{H^{-2/3}\oplus H^{-1}}
 =\|j_{1,n,\lambda}\|_{H^{-2/3}}
 \le D_{0,\lambda}^{1/3}D_{1,\lambda}^{2/3}n^{-5/3}.
$$
Hence, for the complete finite list of true root-window interfaces,
$$
 J_{-,n}\le C_{{\rm col},J}n^{-5/3},\qquad
 C_{{\rm col},J}=\sum_\lambda
                  D_{0,\lambda}^{1/3}D_{1,\lambda}^{2/3}.
 \tag{WUC.16}
$$
No radial length multiplies a jump. All original strict-cover interfaces, including the full 3070-row-boundary list when that cover is used, stay in the ledger; any additional true interface in the collar is also retained. An artificial subdivision has zero jump only when equality of the actual functions proves it. A join at the chosen splitting cut is assigned exactly once to an admitted jump port. Merely splitting an already continuous trial creates no impulse.

If continuity of an ingredient in (WUC.14) is not established for a different trial, that trial must supply its full two-row jump instead. Its second row cannot be assigned zero from the ordinary equation $g_2=0$.

## WUC5. Read the old complete receiver without moving its cut

The successful SP execution is 43731464771/1, child return code0, with all20 original gates true. Its complete endpoint object contains the following exact paths:
$$
 \text{actual_scientific_receipt.complete_endpoint_readout_conclusion}.
$$

| Symbol | Exact field in that object | Original input |
|---|---|---|
| $C_R$ | root_or_affine_jump_to_waist_density_gain | full root or collar jump in $H^{-2/3}\oplus H^{-1}$ |
| $C_O$ | ordinary_root_window_source_to_waist_density_gain | true $L^2_r(H^{-2/3}\oplus\mathbb C)$ on $[c_{\rm PW},r_*]$ |
| $C_1$ | strict_L1_Hminus1_source_to_waist_density_gain | true $L^1_r(H^{-1}\oplus H^{-1})$ on $[0,c_{\rm PW}]$; impulses have no length |
| $C_2$ | strict_L2_Hminus1_source_to_waist_density_gain | the same complete strict ordinary source in true radial $L^2$ |

These are complete original balls, not new arithmetic targets. Their already paid Cauchy conversion, primitive multiplier, strict propagation, density factors and endpoint normalization are not multiplied a second time. In particular neither $C_O$ nor $C_R$ is the ordinary scalar $1/4$ bound.

The recorded input definitions are
centre SHA256 440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47,
direction SHA256 6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04,
fixed $\eta_0$, and full real radius $1/100000000$. The old complete selected parameter interval and compact-metric domain stay attached to that receipt. It retains all Fourier variations, both Cauchy directions, all ordinary sources and affine impulses, and both stored physical mean coordinates.

The current genuine source contribution already printed in that receipt belongs to its original trial. It is neither recalculated nor relabelled as the new WUA source. The only quantities from that output used here are the already qualified linear receiver and its exact saved constants.

On the strict subinterval the WUA/WUR estimate gives
$$
 F_{{\rm st},1,n}+J_{{\rm st},n}\le C_{\rm st}n^{-2}.
 \tag{WUC.17}
$$
Indeed the strict raw source is $(g_1,0)$, the strict true jumps are $(j_1,0)$, and their $H^{-1}$ norms are bounded by their actual primitive norms. Formula (WUC.10) already includes this conversion. If the new correlated receiver $O_0m_{11}$ of WUR is used instead, it is another complete qualified strict route on this subinterval; its new product has not been evaluated here. The direct old route below needs only $C_1$.

Let $\mathcal T_{\rm neg}$ be the linear map from the original normalized homogeneous high root input to the waist density and both means, formed from this new complete ordinary source and all of its negative-side true jumps, with zero root trace. PW.15, with its original cuts, proves the per-column estimate
$$
 \boxed{\quad
 \|\mathcal T_{\rm neg}e_j\|_{\mathcal Y_{\rm waist}}
 \le (C_OC_{\rm col}+C_RC_{{\rm col},J})n^{-5/3}
                         +C_1C_{\rm st}n^{-2}.
 \quad}
 \tag{WUC.18}
$$
This is a new symbolic source-bound recipe. No product in it has been numerically computed. The ordinary source and jumps are restrictions of one actual trial; none is counted in both windows.

Here
$$
 \mathcal Y_{\rm waist}
       =L^2_\phi(\mathbb C^2)\oplus\mathbb C^2
$$
means the original primitive density and its full means, exactly PW.13. Although the direct second residual is zero, the true evolving second state, its physical mean equation and the receiver's interior mean feedback remain. Subsequent physical observation may use its genuine bounded row on this space. WPL's further left/right normalization is a distinct typed composition.

## WUC6. The strict exponent and the remaining whole-error terms

Let $\{e_j\}$ be the original orthonormal reflected high root basis. If a full signed representation or independently retained reference columns are used instead, keep that actual finite multiplicity in the sum. No output orthogonality is assumed.

For a complete column bound $A(4|j|)^{-5/3}$, Cauchy--Schwarz gives
$$
 \|\mathcal T_{\rm neg}\|_{H^{-\sigma}_{\rm high}
                                  \to\mathcal Y_{\rm waist}}
 \le A\left(\sum_{|j|\ge97}^{\rm actual\ input}
          \Lambda_j^{2\sigma}(4|j|)^{-10/3}\right)^{1/2}.
 \tag{WUC.19}
$$
The $n^{-2}$ term in (WUC.18) may be retained separately in this same positive estimate. The sum for the slower term converges exactly under the sufficient strict inequality
$$
 \boxed{\qquad 1<\sigma<7/6.\qquad}
 \tag{WUC.20}
$$
At $\sigma=7/6$ this particular column argument reaches the harmonic threshold. It proves neither a bound nor failure of the actual operator there. It does not supply the original $\sigma=4/3$ window. A better block estimate could change that conclusion only after its true whole-block qualification.

All finite coefficient recipes used in (WUC.7)--(WUC.17) are for WUA's selected object. The old receiver is uniform on its larger recorded real family. A uniform new source estimate on that whole family additionally requires uniform values for the new fold gaps, amplitude derivatives, complete $J$ and dual-test bounds, and all true seam constants. It is not obtained merely from the old receiver's larger domain.

To locate precisely what has and has not been proved, write the full raw evolution as $\mathcal E_h$ and the complete root difference as
$$
 e_*=e^+(r_*)-P_Fh^G(r_*).
$$
WUA's genuine root identity gives
$$
 \begin{aligned}
 \mathfrak D_0(\Psi_A-V_{\rm old})(0)
 ={}&\mathfrak D_0\mathcal E_h(0,r_*)e_*\\
 &+\mathcal T_{\rm neg}
 +\mathfrak D_0\{\mathscr U(0)-V_{\rm old}(0)\}.
 \end{aligned}
 \tag{WUC.21}
$$
This is an identity of operators with the same original input. If an old principal is specified as a density trial, its raw reconstruction is exactly $V_{\rm old}(0)=\mathfrak D_0^{-1}Y_{W,J}(0)$ on the smooth core, with both mean slots. A raw state is never subtracted from a density state.

The first term keeps the complete positive correction, genuine stable normalization, finite root complement and all original head/mean qualifications. The last keeps the entire new waist profile, its root matrix shear, primitive ranks, finite normalizer and the scalar state mean. Neither is set to zero by the source estimates. An already received PC or AW bound is not multiplied by $C_R$ again; $C_R$ is applied only to an actual unreceived mixed root trace.

Consequently a complete error bound in the desired selected coordinates still requires the exact ordered left/right conversions and complete bounds for the first and last terms of (WUC.21), in the same $H^{-\sigma}$ window. Only then may their three nonnegative operator bounds be added, or two bounds for the entire same operator be compared. The present theorem supplies the middle map. It does not treat an old positive cutoff upper as a lower obstruction or remove its terms by subtracting upper bounds.

Independent physical means, amplitude/metric equations, supplied radial head, genuinely independent second-reference input, true low rows, finite cross maps and the final Schur remain. No complete incoming inverse, finite determinant, small perturbation, parameter transversality or nonlinear branch is asserted.

## WUC7. Immutable evidence and the next permitted computation

Repository paths are relative to topics/visible-flex-exact-nearby.

| Primary and use | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| PW: exact root collar, old cuts, ordinary and mixed impulse spaces | d22fc84975785bfdf0e0ba91b100d53c9d4c32a3 | 16459 | 246c81ac387392c75a3267faaa934a7f0a4b978fdad8b8ac7cbbd4bd5c413562 |
| SP: exact primitive/mean evolution and complete source conversions | 9fc2e2c565738b1a6d0fc5962703e01f43b483bf | 20730 | ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4 |
| SP actual: 43731464771/1, all20 gates, unchanged complete receiver balls | 9998526894560d41523454334a444f062fe371a4 | 35259 | a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12 |
| ST actual: exact old-to-new cut tail and all-shorter strict insertions | 94eb4c7d643edc33f696d101753e4d23a7936a26 | 47282 | b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637 |
| WUA: actual finite trial, complete N=6 residual and true seams | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WUR: same-parity finite IJ proof and complete signed adjoint/receiver | a1a7520488196fc8edefe6649a2e82661bedf4ca | 23938 | 948ad1928003feae6ee4a183b7d4136b673000cee6507100a6bbca917947bde1 |

PW is results/R133-supplement-seven-positive-ports-and-mixed-root-to-waist-density.md.
SP is results/R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md.
The original successful SP execution is notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json.
The later ST execution is notes/strict_tail_true_cut_to_waist_ci/run-43757644616-1/execution.json.
WUA is results/R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md.
WUR is results/R133-supplement-mean-completed-scalar-flux-adjoint-and-first-row-reception.md.

A future authorized scalar consumer may read the old complete receiver records and compute new complete coefficient and whole-error recipes. It must first close the remaining same-column root and waist interfaces in (WUC.21). It must not rerun old propagation, old Cauchy arithmetic, old source producers or the successful WAD target. No scientific execution, new numerical upper or stored reproducible array is part of this proof.
