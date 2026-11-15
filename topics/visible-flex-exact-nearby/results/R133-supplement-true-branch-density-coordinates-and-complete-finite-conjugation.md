# R133 supplement: true branch density coordinates and complete finite conjugation at the strict cut

2026-11-15, visible-exact / phase_inverse.

**Exact coordinate identities and a new scalar recipe.** The two canonical oscillatory phases are the actual root-labelled characteristic coordinates on the original negative root piece. Their completed IN derivative bounds give explicit density-change norms on both required Sobolev windows. The complete mean blocks and the finite operators created by a primitive remain. The two branches need not use the same circle.

This result concerns the exact P.22 cut and the same real family $|\delta|\le10^{-8}$, with the original physical $\eta_0$. It does not evaluate an incoming coefficient, an incoming inverse, an interval propagator, or the full return remainder. The proposed scalar consumer reads the completed IN phase bounds and TN/RR conclusions; it evolves no ray and repeats no source, fold, profile, or curvature enclosure.

## 1. The phases are the true characteristic maps

Retain the exact [G.2 canonical identities](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md)
$$
 D=\partial_r-d\partial_\phi,\quad
 DT=QX_\phi,\quad DX=-QT T_\phi,\quad
 \eta^2K=Q^2T .
 \tag{TC.1}
$$
Here $Q$ is the scalar on its original real positive branch, $\eta>0$, $K<0$, and $T<0$. Hence $Q\sqrt{-T}=\eta\sqrt{-K}$.
Write $q=\sqrt{-K}$ and
$$
 \omega=\frac23(-T)^{3/2},\qquad
 \Phi_\sigma=X-\sigma\omega,\qquad
 D_\sigma=\partial_r-(d+\sigma\eta q)\partial_\phi,
 \qquad \sigma=\pm1 .
 \tag{TC.2}
$$
Direct differentiation gives
$$
 \begin{split}
 D\Phi_\sigma&=-QT T_\phi+\sigma Q\sqrt{-T}\,X_\phi\\
 &=\sigma\eta q\{X_\phi+\sigma\sqrt{-T}\,T_\phi\}
   =\sigma\eta q\,\partial_\phi\Phi_\sigma,
 \qquad D_\sigma\Phi_\sigma=0 .
 \end{split}\tag{TC.3}
$$
The original canonical root data are $T(r_*,\phi)=0$ and $X(r_*,\phi)=\phi$, so $\Phi_\sigma(r_*,\phi)=\phi$. The characteristic velocity is continuous at the root and locally Lipschitz in the angular variable on this piece; its radial square-root is integrable. Uniqueness of the angular characteristic equation identifies (TC.2) with the actual two root-labelled maps. No characteristic integration is repeated.

The labels match the two velocities in S.1. The free/genuine carrier convention may exchange the two labels or absorb a Fourier sign, as in IN.20; neither branch is discarded. Each map is real and satisfies $\Phi_\sigma(\phi+\pi/2)=\Phi_\sigma(\phi)+\pi/2$.

At P.22 read the complete actual IN fields
`complete_new_three_phase_gap_lower` and
`complete_new_three_phase_second_derivative_upper`, denoted $m_*,F_*$.
They belong to
`notes/all_segment_Darboux_scalar_receivers_ci/run-43746008734-1/execution.json`,
SHA256 `816483884254f3e7ec06914b66afffc8434db11315dfab1712e71fbb7aae5ae1`.
The frozen source defines
$m_*=(1-x_*-3\omega_{1,*})_-$ and
$F_*=X_{2,*}+3\omega_{2,*}$ with all summands nonnegative. Its full 23-gate actual receipt proves $0<m_*\le1$ on this same cut and real family.

For directed consumption put
$$
 m=\operatorname{lower}(m_*),\quad
 \varepsilon=1-m,\quad M=1+\varepsilon,\quad
 F=\operatorname{upper}(F_*).
 \tag{TC.4}
$$
The complete consequences, for both branches, are
$$
 m\le\Phi_\sigma'\le M,\qquad
 |\Phi_\sigma'-1|\le\varepsilon,\qquad
 |\Phi_\sigma''|\le F .
 \tag{TC.5}
$$
The upper estimate uses the original $x_*+3\omega_{1,*}$ positive sum. It does not claim that an arbitrary lower derivative bound controls an upper derivative. This particular algorithmic identity is part of the qualification.

## 2. Full-circle density maps and independent means

For a real fourfold orientation-preserving map $\Phi$ define the ordinary pullback and density pullback by
$$
 C_\Phi f=f\circ\Phi,\qquad
 U_\Phi f=\Phi' f\circ\Phi,\qquad
 U_\Phi^{-1}=U_{\Phi^{-1}} .
 \tag{TC.6}
$$
All circle integrals are normalized. Both $U_\Phi$ and its inverse preserve the full integral and the zero-mean subspace. They do not fix a constant function in general.

The physical primitive--mean state of S.5 is $(y,z)$ with $\langle y\rangle=0$ and two independent means $z$. On
$$
 \mathcal X^t=H^t_{\ne0}(\mathbb T;\mathbb C^2)\oplus\mathbb C^2
$$
choose the block coordinate change
$$
 \mathscr U(y_+,y_-,z)
       =(U_{\Phi_+}y_+,U_{\Phi_-}y_-,z).
 \tag{TC.7}
$$
Its inverse has the inverse density maps and the identical mean block. The complete equation is conjugated by this one operator; source-to-mean and mean-to-density blocks remain. Equation (TC.7) imposes no zero-mean restriction on the original curvature state.

For a scalar component, identify $H^t_{\ne0}\oplus\mathbb C$ isometrically with full $H^t$ by $f=y+z$. The block map is then
$$
 \mathscr U_\Phi=U_\Phi P_{\ne0}+\Pi
       =U_\Phi-(\Phi'-1)\Pi,\qquad
 \mathscr U_\Phi^{-1}
       =U_\Phi^{-1}-\{(\Phi^{-1})'-1\}\Pi .
 \tag{TC.8}
$$
Thus the independent physical mean convention is explicitly distinguished from the auxiliary full-circle map $U_\Phi$. If a preceding chart uses full $U_\Phi$, the rank-one difference in (TC.8) must remain.

## 3. Positive norms and the required negative window

Put $\mathfrak p(a,b)=\max(1,a,a^2)+b/\sqrt2$.
The exact Fourier norm satisfies
$\|f\|_{H^2}^2=\|f\|_2^2+2\|f'\|_2^2+\|f''\|_2^2$.
Changing variables and differentiating $f\circ\Phi$ gives
$$
 \|C_\Phi\|_{L^2\to L^2}\le m^{-1/2},\qquad
 \|C_\Phi\|_{H^2\to H^2}
          \le m^{-1/2}\mathfrak p(M,F).
 \tag{TC.9}
$$
On the derivative vector $(f,\sqrt2 f',f'')$ the diagonal bounds are $1,M,M^2$ and the additional entry is $F/\sqrt2$ from $f'$ to the second derivative. The matrix norm is at most the diagonal maximum plus that entry. No pointwise pair is replaced by a sum of component suprema without its matrix fee.

For the inverse map, $|(\Phi^{-1})'|\le m^{-1}$ and
$|(\Phi^{-1})''|\le Fm^{-3}$. Therefore
$$
 \|C_{\Phi^{-1}}\|_{L^2\to L^2}\le M^{1/2},\qquad
 \|C_{\Phi^{-1}}\|_{H^2\to H^2}
          \le M^{1/2}\mathfrak p(m^{-1},Fm^{-3}).
 \tag{TC.10}
$$
The exact adjoint relations are $U_\Phi^*=C_{\Phi^{-1}}$ and
$(U_\Phi^{-1})^*=C_\Phi$. Interpolation between the positive $H^0,H^2$ Fourier spaces, followed by duality, gives
$$
 \begin{array}{ll}
 A_0=M^{1/2},&
 A_-=M^{1/2}\mathfrak p(m^{-1},Fm^{-3})^{2/3},\\[2pt]
 B_0=m^{-1/2},&
 B_-=m^{-1/2}\mathfrak p(M,F)^{2/3}.
 \end{array}\tag{TC.11}
$$
They bound $U_\Phi$ on $L^2,H^{-4/3}$ and its inverse on those same windows, respectively. Since $m\le1\le M$, these four numbers are at least one. They also bound (TC.7): its zero-mean restriction has the same bounds and its independent mean block has norm one. The two-branch norm is the maximum of the scalar branch norms, so a common bound requires no additional $\sqrt2$.

These are one common distributional inverse and its two norms, not two unrelated choices of inverse.

## 4. Primitive conjugation keeps both circles and all finite rows

For one lift $\beta$ set
$$
 p_\beta=\beta-\mathrm{id}-\langle\beta-\mathrm{id}\rangle,\qquad
 t_\beta=\beta^{-1}-\mathrm{id}
                   -\langle\beta^{-1}-\mathrm{id}\rangle .
$$
The complete primitive $I=\partial_\phi^{-1}P_{\ne0}$ satisfies
$$
 I U_\beta=C_\beta I
       -1\otimes\Pi C_\beta I+p_\beta\otimes\Pi .
 \tag{TC.12}
$$
The derivative agrees because the constant input contributes
$\Pi f(\beta'-1)$; comparison of means supplies the remaining row. All terms are defined first on smooth periodic functions and then by the stated Sobolev bounds.

For the independent-mean convention,
$$
 I\mathscr U_\beta=C_\beta I-1\otimes\Pi C_\beta I,\qquad
 \Pi C_\beta I f=-\langle t_\beta,f\rangle .
 \tag{TC.13}
$$
For a smooth scalar multiplier $a$, define
$$
 b_{\alpha,a}=(a/\alpha')\circ\alpha^{-1},\qquad
 q_{\beta,a}=I\,U_\beta^{-1}(a-\langle a\rangle),\qquad
 j_\alpha=(\alpha^{-1})'.
$$
The complete two-chart formula is
$$
 \boxed{\ 
 \mathscr U_\alpha^{-1}M_a I\mathscr U_\beta
 =M_{b_{\alpha,a}}C_{\beta\circ\alpha^{-1}}I
   +(U_\alpha^{-1}a)\otimes t_\beta
   -(1-j_\alpha)\otimes q_{\beta,a}.
 \ }\tag{TC.14}
$$
Here $(u\otimes v)f=u\langle v,f\rangle$, with the full normalized bilinear pairing or its equivalent complex-dual formulation. The last row follows from
$$
 \langle a(C_\beta I-\Pi C_\beta I)f\rangle
   =\langle U_\beta^{-1}(a-\langle a\rangle),If\rangle
   =-\langle q_{\beta,a},f\rangle .
$$
Both displayed input rows have mean zero. The output mean of the complete right side equals the unchanged physical mean of the left side.

When $\alpha\ne\beta$, the main term in (TC.14) retains the actual map
$\beta\circ\alpha^{-1}$. For an off-diagonal TN entry, these are opposite true characteristic phases. They are not identified. The wrong-branch cancellation of the trial is still the original exact P/PF statement; it is not proved by omitting this pullback.

For an explicit strong estimate, suppose $a$ has quarter-label bandwidth $b$ and $\|a\|_\infty\le A$. Scalar Bernstein gives $\|a'\|_\infty\le4bA$. The two finite rows in (TC.14) have this sufficient total $H^{-4/3}\to L^2$ bound:
$$
 \mathcal F_{\rm chart}(A,b)
 =\frac{A}{\sqrt m}
       \left\{\frac{33}{16}\frac{\varepsilon^2}{m^2}
                    +\frac{F^2}{m^6}\right\}^{1/2}
 +\frac{\varepsilon}{m}\frac{\sqrt{17}}4\,A
       \left\{\frac4{m^2}
           +\left(\frac{4b}{m^2}+\frac{2F}{m^3}\right)^2\right\}^{1/2}.
 \tag{TC.15}
$$
Indeed $t_\beta$ has zero mean, derivative at most $\varepsilon/m$, and second derivative at most $F/m^3$. Fourfold Poincare has factor $1/4$; hence the first square root bounds its $H^2$, and therefore $H^{4/3}$, norm. Next $G=U_\beta^{-1}(a-\langle a\rangle)$ has
$$
 \|G\|_2\le2A/m,\qquad
 \|G'\|_2\le4bA/m^2+2AF/m^3 .
$$
The complete primitive maps $H^{1/3}_{\ne0}$ to $H^{4/3}_{\ne0}$ with norm at most $\sqrt{17}/4$, and $\|1-j_\alpha\|_2\le\varepsilon/m$. This proves (TC.15) in the correct dual row window. No $L^2$ row is declared to be an $H^{4/3}$ row.

For the TN first normalizer, use $b=192$ and $A=S_*$. Its off-diagonal entries act on different input components, so the common scalar row bound controls the full pair. Every other original rank and mean contribution remains.

## 5. Ordered transfer of TN and the finite projector

Use the exact TN ordered inverse
$$
 \mathcal N=(1+B)^{-1}(1+A)^{-1},
 \quad A=P_JSIP_J,\quad B=P_JS_2I^2P_J .
 \tag{TC.16}
$$
The normalizer is the identity on its complete finite complement and on the independent mean coordinates. Define
$$
 \mathcal N_\Phi=\mathscr U^{-1}\mathcal N\mathscr U,\qquad
 P_\Phi=\mathscr U^{-1}P_J\mathscr U .
 \tag{TC.17}
$$
No commutation with $P_J$ is made. $P_\Phi$ is the exact transported projection, and need not be a Fourier projection in either new branch angle. The complete inverse bounds are
$$
 \|\mathcal N_\Phi\|_{\mathcal X^0\to\mathcal X^0}
       \le B_0K_0A_0,\qquad
 \|\mathcal N_\Phi\|_{\mathcal X^{-4/3}\to\mathcal X^{-4/3}}
       \le B_-K_-A_- .
 \tag{TC.18}
$$
The corresponding forward bounds are multiplied by these coordinate factors on their own windows.

For the exact TN identity $\mathcal N=1-SI+F_S+R_N$,
$$
 \mathcal N_\Phi
 =1-\mathscr U^{-1}SI\mathscr U
       +\mathscr U^{-1}F_S\mathscr U
       +\mathscr U^{-1}R_N\mathscr U .
 \tag{TC.19}
$$
The last two strong constants are multiplied by precisely $B_0A_-$.
The first term is interpreted by (TC.14), not by dropping its pullback or finite rows. If it is later split into a principal pullback and finite rows, (TC.15) pays those rows separately.

The old finite support $|j|\le J+191$ of $F_S$ becomes a finite span of actual transformed rows and columns. Its Fourier support in the new angles is not asserted finite. Its strong norm is at most $B_0A_-$ times the complete TN finite norm. The dual row window $H^{4/3}$ and all modes $97\le|j|<J$ remain; no finite Schur block is inverted by this estimate.

## 6. Complete physical comparison columns

For any complete RR physical map $E_k$, with original input $H^{-4/3}$ and moving output $\mathcal X^0$, apply the cut normalizer first and then the actual branch-density chart:
$$
 E_{k,\Phi}=\mathscr U^{-1}\mathcal N E_k,\qquad
 \|E_{k,\Phi}\|_{H^{-4/3}\to\mathcal X^0}
        \le B_0\,C_{k,\mathrm{TN}} .
 \tag{TC.20}
$$
Here $C_{k,\mathrm{TN}}$ already includes $K_0$. The scalar consumer does not charge $K_0$ a second time or add an input-chart factor: RR input labels remain the original reference-column/root labels.

The original complete same-side sum is read and multiplied by the same $B_0$ before taking a maximum over sides. The four columns remain separate. The two independent physical means have identity blocks throughout (TC.7); every other mean source and charge equation remains.

A subsequent change of input coordinates requires its actual input factor in the specified order. Equation (TC.20) is not declared to be the whole incoming error $E_i$ or $E_o$ in IN.31. Leading trial factors, the free remainder, positive correction, stable spanning and finite equations keep their own qualifications and fees.

## 7. Minimal new public scalar computation

Read only:

1. The full accepted IN execution and its original source formula for $m_*,F_*$.
2. The accepted TN same-cut coefficient, two-window, strong, finite and four normalized physical conclusions.
3. Their same-cut RR identities and the exact G/S definitions as primary evidence.

The new arithmetic is (TC.4), (TC.11), (TC.15) with $A=S_*,b=192$, and the ordered multiplications (TC.18)--(TC.20). It saves all four coordinate norms, the finite primitive-chart fee, the complete transformed strong/finite bounds, the four physical columns and same-side sum. Every old ball and complete source qualification remains an input.

No original phase, ray, root, profile, potential, amplitude, source, normalizer or physical receiver is re-evaluated. Numerical conclusions are separate from this contract. This is a single strict-cut result in the stated base windows; it asserts neither all-Sobolev tame estimates nor a full return or nonlinear solution.
