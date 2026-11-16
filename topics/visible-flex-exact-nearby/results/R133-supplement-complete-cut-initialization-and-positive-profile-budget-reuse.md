# R133 supplement: complete cut initialization and positive profile budget reuse

2026-11-16, phase_inverse.

The new scaled mixed packet needs the true free first-transport value at the original cut and a complete angular profile budget for the same genuine trial. This supplement supplies both interfaces. It retains the exact free/genuine distinction, the original two branches, the genuine input matrix, and every output Fourier mode.

The main results are an explicit cut initializer using only the original cut geometry and local free data, and a positive-budget normalization lemma that reuses complete old zeroth-order profile targets. The latter divides by fixed positive budget constants, never by an Airy or Jost function. New angular derivatives and complete downstream candidates remain uncomputed. No completed numerical target is evaluated again.

## WCPR1. Fixed objects and derivative conventions

Use WUA's real strict interval $0\le r\le c$ with
$$
 c=\frac{76285779072683}{320000000000000},\qquad
 t=-T>0,\quad s=\sqrt t,\quad a=\eta q>0,\quad
 D=\partial_r-d\partial_\phi .
 \tag{WCPR.1}
$$
The physical root is $r_*$; its upper enclosure $r_+$ is used only in specified positive length or coefficient bounds. The cut is unchanged. The physical period is $\pi/2$, with $n=4|j|\ge388$.

Write
$$
 \Phi_\sigma=X-\sigma\omega,\quad
 p_\sigma=\Phi_{\sigma,\phi}>0,\quad
 x=X_\phi,\quad y=T_\phi,\quad
 Q_f=\eta q/\sqrt t,\qquad \sigma=\pm1 .
 \tag{WCPR.2}
$$
Thus $p_\sigma=x+\sigma s y$. The free amplitudes are exactly WUA.10--16,
$$
 v_{0,\sigma}=G p_\sigma^2,\qquad
 v_{1,\sigma}=a_1+i\epsilon\sigma s\,b_1,\qquad
 R_\sigma=v_{1,\sigma}/v_{0,\sigma}.
 \tag{WCPR.3}
$$
Here $b_1$ is the free amplitude component; it is not the unrelated physical coupling coefficient with the same short label in N. The leading amplitude has $b_0=-2i\epsilon Gxy$, so the identity for $v_{0,\sigma}$ includes its phase and is real positive.

For angular budgets use normalized coefficients
$$
 A_j\ge\|\partial_\phi^j A\|_\infty/j!.
 \tag{WCPR.4}
$$
The old cut phase and $T$ records, the WDG relative records, and the free component tables are ordinary derivative bounds until explicitly divided by the relevant factorial. Full holomorphic bounds supply normalized Cauchy coefficients directly. No scalar sup bound is silently promoted to a Wiener norm.

## WCPR2. The exact nonzero cut initializer

At the original cut the complete identity is
$$
 \boxed{\quad
 R_\sigma(c,\phi)=
 G(c,\phi)^{-1}p_\sigma(c,\phi)^{-2}
       \bigl[a_1(c,\phi)+i\epsilon\sigma\sqrt{t(c,\phi)}\,b_1(c,\phi)\bigr].
 \quad}
 \tag{WCPR.5}
$$
All factors refer to the same actual root-normalized free germ. The initializer is not zero, and no new root condition is imposed at $c$.

A complete real angular budget through order 12 can be formed as follows.

1. For $p_\sigma$ use the original cut phase derivatives through order 13 and the original positive cut phase lower $m_c$. Do not replace this by the much weaker whole-strict lower. Both signs are covered by the existing common cut bounds.

2. For $G^{-1}$ use the full original holomorphic reciprocal-$G$ bound in the WGS companion object, on the actual fold strip $S_G=3/128$. Its normalized real angular coefficients obey
$$
       (G^{-1})_j\le G_{i,c}\,S_G^{-j},\qquad 0\le j\le12.
 \tag{WCPR.6}
$$
This is the complete holomorphic reciprocal, not an inversion of a positive upper for $G$ and not a replacement of the entire inverse by its determinant.

3. Read the separate ordinary $a_1,b_1$ cut tables through angular order 3. For orders 4 through 6, the already saved common radial-order-zero component-sum bound safely bounds either component. The saved labels free_old_0_q denote $a_1+b_1$ component sums at radial order zero; free_old_1_q denote radial order one. They are not separate $a_1$ and $b_1$ tables.

For $j=7,\ldots,12$, the original holomorphic bound for the third angular derivative on the saved strip $S_f=1/512$ gives the new ordinary estimate
$$
 \|\partial_\phi^j a_1(c)\|_\infty
       \le (j-3)!\,A^{\rm old}_{0,3}S_f^{-(j-3)}
 \tag{WCPR.7}
$$
and the same formula with the original separate $B^{\rm old}_{0,3}$ for $b_1$. Divide these ordinary bounds by $j!$ only when entering (WCPR.4). The cut belongs to the original saved free radial cover. No extension of that cover, complex strip, or piece label is asserted.

4. Read $t(c)$ upper/lower and old ordinary $T$ derivatives 1 through 4. Read the already completed WDG ordinary cut $T$ derivatives 5 through 12. These are existing targets, not new Cauchy evaluations in this consumer. Form a finite real square-root jet using the true positive lower for $t(c)$.

For precision, put
$$
 P(z)=\sum_{j=1}^{12}\frac{P^{c}_{j+1}}{j!}z^j,\qquad
 T_c(z)=\sum_{j=1}^{12}\frac{T^{c}_{j}}{j!}z^j .
$$
The complete normalized reciprocal-square coefficients are
$$
 [p_\sigma^{-2}]_0\le m_c^{-2},\qquad
 [p_\sigma^{-2}]_j
 \le\sum_{k=1}^{j}(k+1)m_c^{-k-2}[z^j]P(z)^k .
 \tag{WCPR.8}
$$
This is finite Faà di Bruno at a real positive base. It does not assume a convergent geometric series on a fixed angular disk.

Likewise a full square-root packet is
$$
 [s]_0\le\sqrt{t_c^+},\qquad
 [s]_j\le\sum_{k=1}^{j}\left|\binom{1/2}{k}\right|
          (t_c^-)^{1/2-k}[z^j]T_c(z)^k .
 \tag{WCPR.9}
$$
All exponents in the second formula are negative. Their bases are positive lower endpoints. The zeroth coefficient uses an upper endpoint. If an identical complete target is already saved, it is read; an unrecorded old working subexpression is not represented as a saved target.

The coefficientwise positive product
$$
 {\cal R}_c(z)=
       {\cal G}_i(z)\,{\cal P}_{-2}(z)
          \bigl[{\cal A}_1(z)+{\cal S}(z){\cal B}_1(z)\bigr]
          \pmod {z^{13}}
 \tag{WCPR.10}
$$
bounds both true $R_\sigma(c)$ through order 12. Taking the common component sum costs no additional factor 2: each branch has that bound. The actual later half-sum and half-difference reconstruct $a_1,b_1$ in their original order.

This construction does not read the old whole-strict grouped $v_0^{-1}$ packet into the cut initializer. It uses the cut's own reciprocal-$G$ and real phase gap, while preserving the exact function in (WCPR.5).

## WCPR3. Transport from that cut and the full genuine correction

The identities $D\Phi_\sigma=\sigma a p_\sigma$ and WUA.14--16 give the exact ordinary-radial equation
$$
 \partial_r R_\sigma=(d+\sigma a)\partial_\phi R_\sigma+
 \frac{Q_f p_{-\sigma}}{2G p_\sigma^2}
              \left(F_a-\frac{i\epsilon\sigma F_b}{s}\right).
 \tag{WCPR.11}
$$
Indeed the canonical transport direction has physical $T$ speed
$(D-\sigma a\partial_\phi)T=Q_f p_{-\sigma}$. The coefficient in (WCPR.11) is therefore the complete original forcing, with the opposite branch in the numerator and the same branch squared in the denominator.

Let $\chi^\sigma_{u\leftarrow r}$ solve the same original characteristic with velocity $-(d+\sigma a)$. The exact formula is
$$
 R_\sigma(r,\phi)=R_\sigma(c,\chi^\sigma_{c\leftarrow r}\phi)
 -\int_r^c {\cal K}_\sigma(u,\chi^\sigma_{u\leftarrow r}\phi)\,du,
 \tag{WCPR.12}
$$
where $\mathcal K_\sigma$ is the last term of (WCPR.11). The sign follows from integrating the differential equation from $r$ to $c$. A positive budget pays both the complete cut term and the complete ordinary-$dr$ integral. Existing all-shorter flow derivatives can be used in their original directions. Derivatives of the whole coefficient and all true seams remain.

The free amplitudes are reconstructed from $v_{1,\sigma}=G p_\sigma^2R_\sigma$. To obtain the genuine trial one must still add
$$
 w_1^{\rm ext}=w_1+{\cal B}_{\rm ext}K_Tw_0,\qquad
 {\cal B}_{\rm ext}+2T{\cal B}_{\rm ext}'=V_{\rm ext}.
 \tag{WCPR.13}
$$
All derivatives of $\mathcal B_{\rm ext}$, its nonzero tail below $-L$, the complete potential correction, and the finite Darboux cross terms remain. It would change the trial to use an extended cut value in (WCPR.12) while retaining the free kernel (WCPR.11).

The original genuine input matrix $C_n$ and its $\beta_n$ are unchanged. They depend on the input frequency, not on the angular or radial variables being differentiated here. Their existing complete bounds are read once, and no input-frequency derivative is introduced.

## WCPR4. A positive-budget normalization lemma

Suppose an original complete zeroth-order algorithm has fixed nonnegative coefficients $\lambda_i$ and fixed strictly positive budget constants $B_i$. Its saved upper $C_0$ satisfies
$$
                 C_0\ge\sum_{i=1}^m\lambda_iB_i .
 \tag{WCPR.14}
$$
Suppose a new complete normalized $j$th-derivative bound for each summand is $\lambda_iB_i R_{i,j}$. Then
$$
 \sum_i\lambda_iB_iR_{i,j}
       \le C_0\,\max_iR_{i,j}.
 \tag{WCPR.15}
$$
This preserves the entire positive sum. There is no subtraction of an old upper and no assumption that the underlying functions are nonzero.

A budget constant is the exact point-upper extracted from its complete saved record. A division by that point is evaluated outward. Using a positive lower no larger than that point is also safe and less sharp. Dividing by an upper for an unknown actual function, or identifying a budget constant with a lower bound for the function, is not licensed.

The comparison in (WCPR.14) is justified by the original complete positive algorithm. It must not be inferred merely because $C_0$ happens to bound the zeroth-order function. In the next two sections the original source supplies the precise complete positive sums.

If the old whole profile and its near/far pieces were saved separately, rounding need not give
$C_{\rm whole,0}\ge C_{\rm near,0}+2C_{\rm far,0}$ after the three saved records are independently reread at their upper endpoints. No such numerical inequality is required below.

## WCPR5. The complete near profile

Use exactly the old near partition, which depends only on ordinary radius and the dyadic input size. Its angular derivatives are zero. It is used for an estimate and is not inserted into the trial.

Let $A_0,\ldots,A_5$ be the complete saved near scaled-ODE derivative constants, each read at its upper endpoint. Let $X_*$ be the complete saved scaled-near-$T$ bound. The old algorithm is exactly
$$
 {\cal C}_{\rm near}
 =b_{\rm near}\left[
  {\rm FC}(A_0,\ldots,A_4;\xi)
  +n_0^{-1/3}{\rm FC}(A_1,\ldots,A_5;\xi)\right],
 \qquad n_0=388 ,
 \tag{WCPR.16}
$$
where $\mathrm{FC}$ denotes finite composition and the complete old $\xi$ scale and $b_{\rm near}$ are retained. In particular its original zeroth-order positive sum is
$b_{\rm near}(A_0+n_0^{-1/3}A_1)$.

Let $r_j$ be new bounds for $|\partial_\phi^jt|/(j!t)$, $1\le j\le4$, on the same strict patch. They arise from the complete scaled packet; the WDG ordinary ratio is first converted in its proper chain. Define
$$
 D(z)=\sum_{j=1}^4r_jz^j,\qquad X(z)=X_*D(z).
 \tag{WCPR.17}
$$
Since the actual scaled argument is a radial multiple of $t$, its positive angular derivatives are bounded by the coefficients of $X(z)$ on the original near partition. This reuses $X_*$ and does not recompute the old near scale or its fractional power.

The two complete relative composition packets are
$$
 N_0(z)=1+\sum_{k=1}^4\frac{A_k}{A_0k!}X(z)^k,\qquad
 N_1(z)=1+\sum_{k=1}^4\frac{A_{k+1}}{A_1k!}X(z)^k
                      \pmod {z^5}.
 \tag{WCPR.18}
$$
Both denominators are strictly positive saved budget constants. The new normalized near derivative candidate is
$$
 P^{\rm new}_{{\rm near},j}
   =C_{{\rm near},0}
          \max\{[z^j]N_0,[z^j]N_1\},
          \qquad 1\le j\le4 .
 \tag{WCPR.19}
$$
Equation (WCPR.15) proves it using the two complete summands in (WCPR.16). The saved zeroth record $C_{{\rm near},0}$ itself is copied, not recalculated as (WCPR.19) at $j=0$.

The full old near ODE list, original near radius, input powers, genuine normalization and both profile components are present. This is not a claim that $Y$ or $Y'$ is bounded away from zero.

## WCPR6. The complete two-phase far profile

To distinguish it from physical curvature, write $\mathfrak q=t/\rho$, where $\rho=r_*-r$. At fixed $r$, its relative angular derivatives are the same as those of $t$. The Jost variable is $\tau=(2/3)n t^{3/2}$, and
$\partial_\phi\log\tau=(3/2)\partial_\phi\log\mathfrak q$.
Only the far region $\tau\ge1$ is used.

Read the complete old Euler bounds $E_k$ for $a$ and $E'_k$ for $a'$ through order 4, including their distinct positive zeroth budget constants. These are the saved entire Jost construction for the same genuine input matrix. No Jost equation, exponential, or Euler recurrence is rerun.

The original positive algorithm for one far phase is
$$
 \frac65 b_{\rm far}\,
 {\mathfrak q}_{-1/4}
 \left[
  A+\sqrt{r_+}\,{\mathfrak q}_{1/2}
       \left(A+\frac{\tau^{-1}A}{6}+A'\right)
 \right].
 \tag{WCPR.20}
$$
Here the symbols for powers denote the original complete finite real power budgets. At order zero the exact original algorithm contains all four positive summands with baselines
$$
 q_{-1/4,0}E_0,\quad
 q_{-1/4,0}s_{q,0}E_0,\quad
 q_{-1/4,0}s_{q,0}E_0/6,\quad
 q_{-1/4,0}s_{q,0}E'_0 ,
 \tag{WCPR.21}
$$
where $s_{q,0}$ already includes $\sqrt{r_+}$. The outer $(6/5)b_{\rm far}$ is common. All these quantities are the old algorithm's fixed positive constants; they need not be evaluated anew to use (WCPR.15).

For the new relative derivatives define finite nonnegative polynomials
$$
 P_\alpha(z)=1+\sum_{k=1}^4\left|\binom{\alpha}{k}\right|D(z)^k,
 \quad
 L(z)=\frac32\sum_{k=1}^4\frac{D(z)^k}{k},
 \quad
 V(z)=\sum_{k=0}^4\frac{L(z)^k}{k!}
                     \pmod {z^5},
 \tag{WCPR.22}
$$
and
$$
 J_a(z)=1+\sum_{k=1}^4\frac{E_k}{E_0k!}L(z)^k,\qquad
 J_{a'}(z)=1+\sum_{k=1}^4\frac{E'_k}{E'_0k!}L(z)^k
                     \pmod {z^5}.
 \tag{WCPR.23}
$$
The four complete relative packets are
$$
 F_1=P_{-1/4}J_a,\qquad
 F_2=P_{1/4}J_a,\qquad
 F_3=P_{1/4}VJ_a,\qquad
 F_4=P_{1/4}J_{a'}
                    \pmod {z^5}.
 \tag{WCPR.24}
$$
They use the exact real product $\mathfrak q^{-1/4}\mathfrak q^{1/2}=\mathfrak q^{1/4}$ for derivatives. Its positive baseline is still the full old product in (WCPR.21); it is not replaced by an independently smaller, uncomputed power constant.

Finite Faà di Bruno proves that $P_\alpha$ bounds derivatives relative to the actual positive $\mathfrak q^\alpha$. The logarithmic derivative bound in $L$ and finite exponential in $V$ bound the derivatives of $\tau^{-1}$ relative to its zeroth majorant 1. Equations (WCPR.23) divide by positive budget constants, not by $a$ or $a'$.

Thus, for the complete old one-far-phase zeroth upper,
$$
 P^{\rm new}_{{\rm far},j}
  =C_{{\rm far},0}\max_{\ell=1,\ldots,4}[z^j]F_\ell,
       \qquad 1\le j\le4
 \tag{WCPR.25}
$$
is a full new angular candidate. Both Jost phases and the entire original input matrix are retained.

The complete profile packet is finally
$$
 P_0=C_{{\rm whole},0},\qquad
 P_j=P^{\rm new}_{{\rm near},j}+2P^{\rm new}_{{\rm far},j},
          \quad 1\le j\le4.
 \tag{WCPR.26}
$$
The zeroth record is copied verbatim. The factor 2 in the positive derivatives counts the two complete far phases exactly once. All entries bound derivatives of the same fixed genuine profile, so (WCPR.26) is a single valid derivative packet. It makes no comparison of entries belonging to different trial operators or different coordinates.

## WCPR7. Complete output weights and the actual source

Convert (WCPR.26) to ordinary profile derivatives by $\widehat P_j=j!P_j$. Keep the near map $X$ and each far map $\Phi_\sigma$ distinct. They may share complete positive derivative bounds $f_1,\ldots,f_4$ and a true positive lower $m_\Phi$; one map is not substituted for another.

For any such map the ordinary inverse derivative bounds are
$$
 u_1=m_\Phi^{-1},\quad u_2=f_2m_\Phi^{-3},\quad
 u_3=f_3m_\Phi^{-4}+3f_2^2m_\Phi^{-5},
$$
$$
 u_4=f_4m_\Phi^{-5}+10f_2f_3m_\Phi^{-6}
                       +15f_2^3m_\Phi^{-7}.
 \tag{WCPR.27}
$$
Use original individual phase derivatives instead of replacing them by unrelated grouped mixed maxima. The old complete $u_1$ and $L^2$ pullback target remain valid for the same actual maps and can be read directly. They are not recomputed merely because higher derivative bounds change.

The complete $H^{-2}$ pullback bound has the original form
$$
 K_2=\sqrt{f_1}\left[
 u_1+\sqrt2(u_2+u_1^2)+u_3+3u_1u_2+u_1^3\right],
 \qquad
 K_d=K_0^{1-d/2}K_2^{d/2},
 \tag{WCPR.28}
$$
where $K_0$ is the original full $L^2$ pullback bound. For $d=0,5/3,2$ and $b=0,\ldots,4$, the complete original full-output Schur algorithm is
$$
 {\cal W}_{d,b}=2^{d/2}K_d
 \left[
 {\bf1}_{b=0}\widehat P_0+
 \frac{17}{64}\sum_{j=\max(1,b)}^4
   B_{4,j}(u_1,u_2,u_3,u_4)
          \binom jb\,\widehat P_{j-b}
 \right].
 \tag{WCPR.29}
$$
$B_{4,j}$ is the ordinary exponential Bell polynomial. The constant $17/64$ bounds the entire physical-frequency-$4j$ off-diagonal Fourier sum, including low and zero outputs in the complete matrix argument. No orthogonality of output frequency blocks is assumed.

For a complete frequency-dependent amplitude family $v_j(r,\phi)$, let $\mathcal U_{[N,2N)}[v]$ map the full signed Fourier coefficient vector $(c_j)$ to the original sum of genuine profile columns with these amplitudes, for $N\le4|j|<2N$. The complete derivative norm below is the uniform component-sum norm over these input labels. No input-frequency derivative or sampled-column estimate is used. Then
$$
 \|{\cal U}_{[N,2N)}[v]\|_{\ell^2_{\rm signed}\to H^{-d}}
 \le N^{-d}(1+N^{2/3}\rho)^{-1/4}
       \sum_{b=0}^4{\cal W}_{d,b}
             \sup_j\|\partial_\phi^bv_j\|_{\infty,\mathrm{component\ sum}} .
 \tag{WCPR.30}
$$
It is the original full signed-Fourier block estimate. Its original normalized reflection restriction is already included. An additional factor 2 cannot be inserted for that same restriction. Independent reference ports and separate terminal-column assembly retain their own original factors.

The new angular weights do not pay missing amplitude derivatives, radial terms, $J$ or $J_r$, an ordinary source integral, an interface jump, or a mean row. Those are complete distinct predecessors. To use them in WUA/WNR/WRT, the full actual ordered scalar words, finite primitive and angular-mean remainders, all retained profiles and complete terminal constants must be supplied on their unchanged domains.

The local root packet is independent and stays on its original analytic domain. No $1/T$ formula from (WCPR.11) is moved to $r_*$, and no relative positive probability argument is moved into a complex strip.

## WCPR8. Input identities and a complete new-target contract

The following are read-only mathematical predecessors. Relative paths are inside topics/visible-flex-exact-nearby/.

| Object | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| WUA global genuine trial | 7b89251dcd51e8cb78fd3e8e42905114ef982ebf | 40111 | 9cd778ec8c97904b29524ae8b8252c14304eedfdc67d4ffec48affa79ae18bad |
| WGS actual main | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| WGS complete original inputs | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| WDG published relative-gap proof | 0e4bf6ce75e0450a3aab4a1fc2365ffdcacb9512 | 27168 | 212385b518812e52cb934ef381e0664b34e155d8967ac5572a7830514a8a5ebb |
| WDG completed actual | 67c7070e6678223b5de63635d4b18f110500a742 | 47714 | 04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395 |
| WSJ scaled mixed theorem | 10c6e4220377b772692095347f096e5d897afc5e | 31568 | 217cdff81516dd827122987ba6abe9a2cdacb6597d01fe9b4ee58a47faa8960d |
| Original complete profile source | d4f887d637a709331977ef24cd48d930ea396b40 | 73459 | c42b14e13c7357bb3aa60447ee8679592e0948fffe11f7ecdd846fc554bafdf4 |
| Original strict profile actual | f2a2687ae736d291c5d5b85e0309e625d729e5d8 | 9131 | 6e781157c43f7ba7f7e4ac454308545444164138920cbab027a7af56dd1d89a6 |
| Original complete Jost actual | ca23b0849f45ab46e34d8828da71cf55c7886739 | 6214 | cef16dab35db9bec8b585ed4220ea8d61247291ef101f388d48c45e455019851 |

The WGS pair is under notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/, with actual-scientific-conclusion.json and complete-original-inputs.json. WDG is under notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json. The original profile and Jost nodes are under notes/global_genuine_waist_error_posterior_ci/run-43827705714-1/graphs/profile_block_strict.json and graphs/Jost_scalars.json.

The profile/Jost nodes are complete successful nodes of a run whose later endpoint node failed. Their full identities, complete conclusions and dependency bindings are retained; the later failure does not authorize recomputing them.

The exact read-only paths are:

- WGS main: complete_higher_flow_and_cut_conclusion.cut_phase_lower and cut_phase_orders_5_through_15; cut orders 1 through 4 are in the companion scalar records.
- WGS companion: copied_original_scalar_records for cut_phase_1 through cut_phase_4, cut_t_1 through cut_t_4, t_cut_lower, t_cut_upper, and free_old_0_4 through free_old_0_6; copied_original_stage_records.fold.Gi and free_components.a1/b1["0"][0..3].
- WDG: complete_new_graphs.complete_new_cut_T_high_angular_conclusion.new_records.ordinary_cut_T_orders_5_through_14, and the full relative-omega list at complete_new_graphs.complete_new_relative_omega_angular_conclusion.new_records.complete_strict_relative_omega_angular_orders_1_through_14.
- Original profile: conclusion.complete_near_scaled_ODE_derivatives_0_5; conclusion.complete_profile_jets.near_profile, one_far_phase and complete_profile, each group_upper[0]; complete_scaled_near_T_upper and all other retained scalar geometry/profile values remain under conclusion.new_complete_records.
- Original Jost: conclusion.complete_Euler_a_0_4 and complete_Euler_aprime_0_4, with the complete original genuine/input-frequency scope.

The ordinary-to-normalized conversions are explicit in (WCPR.4), (WCPR.7)--10 and (WCPR.17). For the WSJ mixed packet the frozen scale is $t_0^p/(p!q!)$; it is not the differential operator $(t\partial_r)^p$. The root-to-cut identities and the complete free/genuine domain declarations are part of the admission, not optional comments.

A new consumer may declare complete targets for the cut inverse-phase and reciprocal-$G$ angular packets, only the missing free component derivatives, the complete cut initializer, the new strict transport and amplitude packets, positive near/far derivatives, and the complete three-by-five output weights. It must publish each complete new target before a downstream read and preserve every already calculated prefix. Its exact partition into saved targets and its maximum output bytes are frozen before execution; this proof does not require duplicating already saved zero-order targets.

For a new whole error candidate, both stored density means, the physical scalar-mean ODE with true initial condition $z_{\rm ph}(r_*)=0$, all 3070 genuine interfaces, ordinary-$dr$ source lengths, jumps with no artificial length, original positive/root correction, complete four waist endpoint terms, $n_g$ factors, original input normalizers and transported finite factors remain in their actual order. The actual 96 physical columns exist separately; their still uncomputed signed normalization, $\nu$, $\Theta$, cokernel rows, and independent radial functions are not supplied here.

Any whole comparison uses complete candidates for the same physical operator and coordinate map. Whole and reduced errors are compared separately to their own saved predecessors, with the declared tie rule. No old whole upper is reduced by subtracting a subtotal, and no smaller complete error, finite determinant, or inverse is asserted before the new targets exist.
