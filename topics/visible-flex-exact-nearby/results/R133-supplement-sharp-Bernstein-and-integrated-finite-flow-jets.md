# R133 supplement: sharp Bernstein and integrated finite flow jets

2026-11-16, visible-exact. **WBF: a complete analytic improvement and a genuinely new 83-scalar contract.**

The old WX/WGS flow derivative bounds remain valid and immutable. This note proves a different complete majorant: sharp real trigonometric Bernstein bounds remove the finite-support square-root loss, and exact integration of the entire angular variational majorant replaces repeated interval-length overestimates. The new bounds use only the already saved first positive comparison budget. No old exponential, flow solve, coefficient enclosure, cut derivative or completed WDG target is evaluated again.

The consequence is a new complete set of all-shorter flow derivatives of orders 2–15, strict individual phase derivatives of orders 2–15 and strict relative-gap derivatives of orders 1–14. All formulas below are finite positive polynomial expressions or complete Bell compositions. The logarithm and exponential appearing in the proof are formal identities; a numerical consumer evaluates neither function.

## WBF1. Same actual reference, bandwidth and first budget

Use the same continuous degree-96 repaired real reference at fixed intrinsic $\eta_0$ on
$$
 0\le r\le c,\qquad c=\frac{76285779072683}{320000000000000},
 \qquad\phi\in\mathbb R/(\pi/2)\mathbb Z.
 \tag{WBF.1}
$$
The reference is not asserted to solve the nonlinear equation. As in [WX](R133-supplement-complete-true-waist-coordinates-from-saved-positive-products.md),
$$
 d=-\beta I(u_{\rm bg}^2+K v_{\rm bg}^2)
$$
is a complete trigonometric polynomial with label bandwidth at most 192. This is a property of the known reference, not a truncation of an unknown state. In the physical angle the maximum frequency is
$$
                         \Lambda_d=4\cdot192=768.
 \tag{WBF.2}
$$
The proof works for each flow of velocity $-d-\nu(r)$ with radial $\nu$, hence for both actual characteristics and the drift-only flow. Both orientations and all shorter real intervals are included. The true root, cut, phase lifts, winding, both physical means and all 3070 original interfaces are unchanged.

Let $D(r)\ge\|d_\phi(r,\cdot)\|_\infty$ be the original nonnegative comparison envelope. WX2 proves from the specific complete positive forward and reverse products that
$$
 \exp\!\left(\int_I D(r)\,dr\right)\le F
 \quad\text{for every shorter }I\subseteq[0,c],
 \qquad F\ge1.
 \tag{WBF.3}
$$
Here $F$ is the directed upper endpoint of the already saved original record flow_1. Its original ball is
$$
 [26.83218262517372598294179248503474475794481624416073
       \mathbin{+/-}9.36\,10^{-52}].
$$
The first angular flow derivative lies between $F^{-1}$ and $F$.

The use of (WBF.3) is essential. A generic upper bound for one flow derivative would not imply the integral inequality. WX.4–9 supplies it from the original positive algorithm and its original first diagonal products. The square root that produced the saved record has already been computed and is read unchanged.

## WBF2. Sharp real trigonometric Bernstein inequality, with proof

Let $T(\theta)=\sum_{|n|\le N}t_n e^{in\theta}$ with $N\ge1$, allowing complex coefficients. Set
$$
 \theta_k=\frac{(2k-1)\pi}{2N},\qquad
 w_k=\frac{(-1)^{k-1}}{4N\sin^2(\theta_k/2)},
                  \qquad k=1,\ldots,2N.
 \tag{WBF.4}
$$
The exact translation formula is
$$
               T'(\theta)=\sum_{k=1}^{2N}w_kT(\theta+\theta_k).
 \tag{WBF.5}
$$
To verify it, use the consecutive Fourier indices $n=-N+1,\ldots,N$. Orthogonality on the $2N$ half-shifted nodes gives the weights
$$
 w_k=\frac1{2N}\sum_{n=-N+1}^{N}in\,e^{-in\theta_k}.
$$
For
$$
 S(\theta)=\sum_{n=-N+1}^{N}e^{-in\theta}
          =e^{-i\theta/2}\frac{\sin(N\theta)}{\sin(\theta/2)},
$$
the sum is $-S'(\theta_k)/(2N)$. Since
$\cos(N\theta_k)=0$ and $\sin(N\theta_k)=(-1)^{k-1}$, differentiating this finite identity gives exactly (WBF.4). The missing index $-N$ is compatible too: its sample vector is the negative of the index-$N$ vector, and its derivative multiplier is also the negative. Thus (WBF.5) holds for the full bandwidth, including both endpoints.

The finite cotangent identity, obtained by logarithmically differentiating the finite product for $\sin(mz)$ and then differentiating once more, gives
$$
 \sum_{k=1}^{2N}\csc^2\frac{(2k-1)\pi}{4N}=4N^2.
$$
Equivalently it is the usual partial-fraction identity
$\sum_{k=0}^{m-1}\csc^2(z+k\pi/m)=m^2\csc^2(mz)$
with $m=2N$ and $z=\pi/(4N)$. There is no singular evaluation at these points. Hence
$$
                       \sum_{k=1}^{2N}|w_k|=N.
 \tag{WBF.6}
$$
Taking the supremum in the exact translation formula proves
$\|T'\|_\infty\le N\|T\|_\infty$. Repeated differentiation retains the same support, so
$$
                        \|T^{(j)}\|_\infty\le N^j\|T\|_\infty .
 \tag{WBF.7}
$$
This argument is on the real circle and is valid for complex-valued $T$ as well. It uses neither an unknown analytic strip nor a Fourier $A^0$ identification.

Apply (WBF.7) to $d_\phi$ with $\theta=4\phi$ and label bandwidth 192. For every $k\ge1$,
$$
          \|\partial_\phi^k d(r,\cdot)\|_\infty
                  \le \Lambda_d^{\,k-1}D(r).
 \tag{WBF.8}
$$
The first case is the original bound. Higher cases improve the sufficient finite-support estimate used in WX.10–11 without changing any old saved quantity. The known-reference support is what permits this improvement; no such support is imposed on a physical input.

## WBF3. Exact integration of the whole finite angular majorant

Take an oriented interval, parameterized in its positive traversal direction by $s$, and put
$A(s)=\int_0^s D$. Let $\chi(s,\phi)$ be any of the permitted flows with identity initial map. Its $j$-th angular variational equation has the linear term with $d_\phi\chi^{(j)}$ and all nonlinear terms
$$
 \sum_{k=2}^{j}(\pm\partial_\phi^k d)\,
       \mathsf B_{j,k}(\chi',\ldots,\chi^{(j-k+1)}).
 \tag{WBF.9}
$$
The radial function $\nu$ has no angular derivatives. The same inequalities apply under either orientation.

Consider the formal generating function $w(A,h)$ determined by
$$
 \partial_Aw=\frac{e^{\Lambda_dw}-1}{\Lambda_d},
 \qquad w(0,h)=h.
 \tag{WBF.10}
$$
For any fixed order, this is only a finite triangular coefficient system. Its coefficients are nonnegative. The coefficient of order one solves $G_1'=G_1$, $G_1(0)=1$; each higher ordinary derivative solves the same linear term plus the complete positive Bell forcing prescribed by (WBF.8). Induction and variation of constants therefore give
$$
               |\partial_\phi^j\chi(s,\phi)|
                 \le \partial_h^j w(A(s),0).
 \tag{WBF.11}
$$
This comparison does not divide by a possibly zero higher derivative. Piecewise integrable $D$ and the original continuous flow concatenate across every original interface. An extra radial differentiability assumption is not used.

Set $v=e^{-\Lambda_dw}$. Formally, $v_A=v-1$ and
$v(0,h)=e^{-\Lambda_dh}$. Solving that linear identity and writing $E=e^A$ yields
$$
 w(A,h)=h-\frac1{\Lambda_d}
        \log\{1-(E-1)(e^{\Lambda_dh}-1)\}.
 \tag{WBF.12}
$$
For the coefficient of order $j$, only finitely many terms of the logarithm and exponential contribute. No convergence radius or numerical logarithm/exponential evaluation is required for the finite-jet statement.

Let $S(j,k)$ be the nonnegative Stirling numbers of the second kind, characterized by
$$
 S(0,0)=1,\quad S(j,0)=0\ (j>0),\qquad
 S(j,k)=kS(j-1,k)+S(j-1,k-1).
$$
The finite coefficient identity
$$
 [h^j](e^{\Lambda_dh}-1)^k
      =\frac{\Lambda_d^j k!}{j!}S(j,k)
$$
then gives
$$
 G_1(E)=E,\qquad
 G_j(E)=\Lambda_d^{\,j-1}
       \sum_{k=1}^{j}(k-1)!\,S(j,k)(E-1)^k
                   \quad (j\ge2).
 \tag{WBF.13}
$$
For $E\ge1$ each is a nondecreasing polynomial in $E-1$. Combining (WBF.3), (WBF.11) and (WBF.13) proves the complete all-shorter bound
$$
           |\partial_\phi^j\chi_{b\leftarrow a}(\phi)|
             \le \widehat F_j:=G_j(F),\qquad j\ge2,
 \qquad \widehat F_1:=F.
 \tag{WBF.14}
$$
The inverse map is a flow on the opposite oriented interval and has the same bound. This covers both characteristics and the drift flow, including every partial interval used inside a full radial integral.

The subtraction $F-1$ uses a known positive comparison constant $F\ge1$. It is not subtraction of two norm upper bounds to infer the size or sign of an unknown operator difference. All later terms are nonnegative. The case $F=1$ gives zero higher majorants and remains well defined.

For clarity, (WBF.14) is a new bound recipe for the same mathematical derivatives. It is not a repeat evaluation of the old WX/DX/WGS formulas. The latter remain immutable safe alternatives.

## WBF4. Complete phase and relative-gap consequences

Let $C^\Phi_j$, $1\le j\le15$, be the complete already saved ordinary angular cut-phase bounds, for both branches. For orders one through four use the bound companion's cut_phase_j records; for orders five through fifteen use the WGS main's cut_phase_orders_5_through_15. They are not recomputed.

The exact root-labelled phase identity is
$\Phi_\sigma(r,\phi)=\Phi_\sigma(c,\chi^\sigma_{c\leftarrow r}(\phi))$.
For $2\le j\le15$ set
$$
 \widehat P_j=\sum_{k=1}^{j}C^\Phi_k
        \mathsf B_{j,k}(\widehat F_1,\ldots,\widehat F_{j-k+1}).
 \tag{WBF.15}
$$
Every old cut term and every Bell term is retained. This proves complete ordinary derivative bounds for both true phases throughout the original strict interval. The first phase bound is copied from the old complete WGS phase_1; its formula would be unchanged, so it is not a new target.

Read the same saved strict positive lower $m_\Phi$ unchanged. Since
$x=(\Phi_{+,\phi}+\Phi_{-,\phi})/2\ge m_\Phi$,
$$
                    \widehat X_b=\widehat P_{b+1}/m_\Phi,
                         \qquad1\le b\le14
 \tag{WBF.16}
$$
bounds $|x^{(b)}|/x$. Both phases and their half sum are retained.

Read the fourteen complete WDG cut-relative-gap records $C_b$ unchanged. In particular, neither WDG's ten high cut $t$ derivatives nor its fourteen relative cut derivatives are recomputed. The positive drift identity WDG.7 then gives
$$
 \widehat K_b=\sum_{k=1}^{b}C_k
        \mathsf B_{b,k}(\widehat F),\qquad
 \widehat B_b=\sum_{k=1}^{b}\widehat X_k
        \mathsf B_{b,k}(\widehat F).
 \tag{WBF.17}
$$
For $b=1$, the cut expression $C_1F$ is identical to the completed WDG quantity. Read its complete saved ordinary_cut_contribution_orders_1_through_14[0] record instead of evaluating it again. Only $\widehat K_2,\ldots,\widehat K_{14}$ are new cut-composition targets. All fourteen bulk compositions are new because their phase predecessors are new.

After both complete cut and bulk records are saved, set
$$
 \widehat R_b^\omega=\max(\operatorname{upper}\widehat K_b,
                          \operatorname{upper}\widehat B_b),
 \qquad
 \frac{|\partial_\phi^b\omega|}{\omega}
             \le\operatorname{upper}\widehat R_b^\omega,
                    \qquad1\le b\le14.
 \tag{WBF.18}
$$
WDG's proof differentiates the actual positive cut-plus-integral identity first and only then uses its positive normalized weights. That exact argument and the original ordinary $dr$ measure are unchanged. No cut atom, partial interval, interface or phase branch is discarded.

The new bounds remain real geometric suprema. They are not new Wiener norms, a complex root packet or relative order fifteen. In WSJ only the ordinary-to-normalized conversion $\widehat R_b^\omega/b!$ is performed, once. The frozen $t_0$ radial scale, complete mixed equations, absolute fifteenth edge, all inverse entries, profile weights and forcing are separate.

## WBF5. Exactly 83 genuinely new scalar conclusions

| New complete graph | New records | Count | Readonly unchanged companion |
|---|---|---:|---|
| Integrated Bernstein flow | $\widehat F_2,\ldots,\widehat F_{15}$ | 14 | Original $F_1$ |
| Complete strict phase | $\widehat P_2,\ldots,\widehat P_{15}$ | 14 | Original $P_1$ and all 15 cut bounds |
| Complete relative bulk | $\widehat X_1,\ldots,\widehat X_{14}$ | 14 | Original $m_\Phi$ |
| Complete drift composition | $\widehat K_2,\ldots,\widehat K_{14}$ and $\widehat B_1,\ldots,\widehat B_{14}$ | 27 | Original complete $K_1$ |
| Complete relative gap | $\widehat R_1^\omega,\ldots,\widehat R_{14}^\omega$ | 14 | Both complete predecessor compositions |

The numerical predecessor set consists of three complete files: the two WGS files and the completed WDG scientific conclusion. Thirty-three complete scalar records are copied: one $F_1$, one $P_1$, fifteen $C^\Phi_j$, one $m_\Phi$, fourteen $C_b$ and one $K_1$. The full file identities, complete admissions and original domain scopes must be checked. A numerical consumer must not replace these full inputs with a display table or strip all older qualifications.

The first graph evaluates only positive polynomial expressions with exact integer Stirling/factorial coefficients and directed Arb endpoints. The remaining four use positive finite Bell expressions, one original strictly positive denominator and directed maxima. No numerical trigonometric value is needed to apply the Bernstein theorem. There are zero new exponentials, logarithms, square roots, fractional powers, ODE solves or quadratures.

These are five complete natural conclusions, not a split certificate. Intermediate combinatorial tables are local to the scientific child. Each complete saved scalar is written and read back before its use by a later new graph. On failure, preserve the complete already saved graph/record prefix and identify the interrupted target before any continuation. All completed WGS and WDG targets remain frozen.

No numeric value of the 83 new quantities is claimed in this pure theorem. A later actual report must identify source, parameters, manifest, public run and output SHA-256, and state its full result even if the new whole comparison is insufficient.

## WBF6. Exact old identities and unchanged remaining obligations

The complete WGS main is Git blob 32ff92c516fcc5c43f3619930d4845d294289270, 72251 bytes, SHA-256 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e, at notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json.

Its complete bound companion is Git blob d6d13860e322d82ce354c8c0d0eb0f279ca63b3c, 31632 bytes, SHA-256 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66, at the same run directory's complete-original-inputs.json. The same source/module/manifest/run relation and all original gates, scopes and historical failures remain part of admission.

The complete WDG actual conclusion is Git blob 67c7070e6678223b5de63635d4b18f110500a742, 47714 bytes, SHA-256 04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395, at notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json. Its 80 successful new records are already frozen. The mathematical basis for reusing its cut records and full positive-gap identity is [WDG](R133-supplement-positive-drift-and-complete-relative-angular-fold-bounds.md), with actual status in [WDGA](R133-supplement-actual-positive-drift-relative-angular-bounds.md).

The proof of (WBF.3) is WX2, including the original ordered positive products. WBF2 proves the improved Bernstein step directly; WBF3 integrates the complete angular majorant directly. Neither step requires a new numerical coefficient or flow enclosure.

Both physical means, $J,J_r$, mean ODE, ordinary measures, source and jump norms, nonzero cut trace, genuine potential, true root, positive response and all four waist endpoints remain. The original root analytic packet stays separate. The 96 physical columns still require their actual signed normalization; radial head/coker, $\nu$, Theta, all seven ports, both right-hand sides, full high fees and $e+3dt<1$ are not supplied here. Complete mixed/profile reception, tame/background, nonlinear matching and the same closed fixed-metric family remain to be proved.
