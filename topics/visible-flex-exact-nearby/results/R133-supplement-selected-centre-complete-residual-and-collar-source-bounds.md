# R133 supplement: complete residuals of the selected continuous centre and their collar source bounds

2026-11-15, visible-exact-astra-0df9.

This note converts the already proved selected-parameter operator and parameter-source differences into a complete residual bound for the same explicit continuous centre. It also gives an exact quadratic/cubic formula on the positive collar, where the intrinsic bump vanishes. The independent mean and all original radial interfaces are retained. No numerical residual value, nonlinear core solution or passed collar gate is asserted.

## 1. The exact centre and the residual convention

Use the same continuous centre and continuous physical response
$$
 Q_\delta=Q_0+\delta Z,\qquad
 \nu_\delta=\nu_0+\delta,\qquad |\delta|\le d=10^{-10}.
 \tag{R.1}
$$
Their definition hashes are respectively
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47
and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
The physical intrinsic parameter remains $\eta_0$. The field $v$ contains its genuine mean; it is not the original scalar radial reference.

Write the full nonlinear moving field as
$$
 \mathcal F(Q,\nu)
 =-\beta I(S)Q_\phi+GmJ(K)Q_\phi
                         +\beta(-u,v)-\beta SQ,
$$
$$
 S=u^2+Kv^2,\qquad m=\langle v\rangle_\phi,\qquad
 J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix}.
 \tag{R.2}
$$
Here $I=\partial_\phi^{-1}P_{\ne0}$ has Fourier frequencies $4j$ and preserves the full convention used in [D](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md). Set
$$
 f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta),
 \qquad
 A_\delta=D_Q\mathcal F(Q_\delta,\nu_\delta),
$$
$$
 s_\delta=\mathcal F_\nu(Q_\delta,\nu_\delta)
                              -(\partial_r-A_\delta)Z .
 \tag{R.3}
$$
Both are complete ordinary two-row sources, including the independent even mean. In particular $s_\delta$ is the negative parameter derivative of $f_\delta$.

All following identities hold almost everywhere on the original radial pieces. Since $Q_0$ and $Z$ are exactly continuous at their interfaces, their distributional radial derivatives have no value-jump Dirac masses. Different one-sided coefficient or derivative bounds are nevertheless kept on their original pieces. This argument does not erase a jump of an unrelated approximate iterate.

## 2. A complete integral identity and a quadratic remainder

Differentiating (R.3), and then using (D.21), gives
$$
 \frac{d}{d\delta}f_\delta=-s_\delta,\qquad
 s_\delta-s_0
   =\mathcal F_\nu(Q_\delta,\nu_\delta)
                -\mathcal F_\nu(Q_0,\nu_0)
                           +(A_\delta-A_0)Z .
 \tag{R.4}
$$
Thus the exact identity is
$$
 \boxed{\quad
 f_\delta=f_0-\delta s_0
 -\int_0^\delta
   \{\Delta\mathcal F_\nu(t)+\Delta A(t)Z\}\,dt .
 \quad}
 \tag{R.5}
$$
The plus sign inside the braces and the minus sign in front of the integral are both essential.

On one original closed radial cell, use the fixed nonnegative coefficient bounds in (D.5)--(D.6), (D.19)--(D.20). For $0\le x\le d$ let
$$
 B(x)=\mathcal N_\nu(x)+M_1(x)Z_1^\#+M_0(x)Z_0^\#,
 \tag{R.6}
$$
where those formulas are evaluated with half-width $x$, $E_0=xZ_0^\#$, $E_1=xZ_1^\#$ and a fixed complete bound $E_m=xm_Z^\#$ on the genuine response mean. The coefficients $b,g,k,t,W,W_1,Q_0^\#,Q_1^\#,Z_0^\#,Z_1^\#,m_0^\#,m_Z^\#$ do not change with $x$.

These explicit positive budgets satisfy
$$
 B(0)=0,\qquad
                    B(x)\le\frac{x}{d}B(d).
 \tag{R.7}
$$
Here is a direct proof, avoiding a derivative of an interval enclosure. A nonnegative function $b_0(x)$ with $b_0(x)\le xb_0(d)/d$ keeps this property when multiplied by any nonnegative nondecreasing function. Sums and maxima of functions with this property retain it. Each $e^{cx}-1$, $c\ge0$, has the property by convexity and its zero value at zero. Each $x^j$, $j\ge1$, has it as well. Every summand in $M_0,M_1,\mathcal N_\nu$ contains at least one such vanishing factor; its remaining factors are nonnegative and nondecreasing. In particular $K_+(x)=\max\{1,e^{xW}(k+xtW_1)\}$ is nondecreasing, and both branches of each vanishing matrix-difference maximum satisfy the required property. This proves (R.7) for the complete formulas, including the separate intrinsic and mean-rank terms.

For either sign of $\delta$, (R.4)--(R.7) imply the pointwise angular bound
$$
 \left\|f_\delta-f_0+\delta s_0\right\|_{L^2_\phi}
                  \le\frac{|\delta|^2}{2d}B(d).
 \tag{R.8}
$$
The same conclusion holds on any exact radial window $I$:
$$
 \boxed{\quad
 \|f_\delta\|_{L^2(I;L^2_\phi)}
 \le \|f_0\|_{L^2(I;L^2_\phi)}
      +|\delta|\|s_0\|_{L^2(I;L^2_\phi)}
      +\frac{|\delta|^2}{2d}\|B(d)\|_{L^2(I)} .
 \quad}
 \tag{R.9}
$$
This uses the triangle inequality for these three complete sources. It does not treat them as orthogonal. A cellwise upper bound for the last norm is the square root of the sum of the exact restricted cell lengths times $B(d)^2$. The compact support, fixed negative output window and complete core window remain distinct.

The new scalar consumer of (D.22) can therefore be reused directly in (R.9). The factor $|\delta|^2/(2d)$ does not require a second traversal of the original numerical rows. At $\delta=0$ all changed terms vanish exactly.

## 3. Paying the continuous response repair in the linear source

The accepted complete response-repair summary
[43597921732](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json)
has SHA256
7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec.
Its original construction uses a scalar mean-completed response trial. As proved in [MC.4--MC.9](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md), the same nonnegative budget bounds the raw nonmean residual plus the complete centre-repair fee. It does **not** include the independent raw response mean $r^0$. The actual complete source is $s_0=b_0-r^0e_2$; the mean fee must be added before using this summary in (R.9) or (R.14).

By [the exact continuous direction](R133-supplement-explicit-continuous-response-direction-and-true-strip-norms.md), (Q.2)--(Q.3), on each original cubic piece
$$
 Z=q_{\rm raw}+e_j,\qquad \partial_re_j=0
 \quad\hbox{almost everywhere},\qquad
 \|e_j\|_{A^0,\mathrm{pair}}\le E_Z .
 \tag{R.10}
$$
One may use the already proved complete bound $E_Z=2.292\,10^{-16}$. The offsets include all 193 components and the genuine mean. Since they have angular degree at most 96,
$$
                    \|(e_j)_\phi\|_{A^0,\mathrm{pair}}\le384E_Z.
 \tag{R.11}
$$
The distributional jumps of $q_{\rm raw}$ and $e_j$ cancel exactly; one does not estimate either collection of Dirac masses as an ordinary source.

For the unchanged centre, define the whole-cell positive coefficients
$$
 k_+=\max\{1,|K|\},\qquad b\ge|\beta|,\quad g\ge G,
$$
$$
 \begin{split}
 C_1={}&bk_+(Q_0^\#)^2/4+gk_+m_0^\#,\\
 C_0={}&b+3bk_+(Q_0^\#)^2
                  +bk_+Q_0^\#Q_1^\#/2+gk_+Q_1^\#.
 \end{split}
 \tag{R.12}
$$
The complete operator (D.4) gives
$$
 \|A_0h\|_2\le C_1\|h_\phi\|_2+C_0\|h\|_2 .
 \tag{R.13}
$$
The drift uses $\|I(S)\|_{A^0}\le\|S\|_{A^0}/4$. The local cubic differential costs $3bk_+(Q_0^\#)^2$, the complete primitive rank term costs $bk_+Q_0^\#Q_1^\#/2$, and the independent mean-rank term costs $gk_+Q_1^\#$. Thus no mean or first-order term has been dropped.

If $s_{\rm raw}=\mathcal F_\nu(Q_0,\nu_0)-(\partial_r-A_0)q_{\rm raw}$ on the original open pieces, then
$$
 s_0=s_{\rm raw}+A_0e_j,\qquad
 \|s_0\|_{L^2(I;L^2_\phi)}
 \le\|s_{\rm raw}\|_{L^2(I;L^2_\phi)}
                        +E_Z\|384C_1+C_0\|_{L^2(I)} .
 \tag{R.14}
$$
After adding the independent raw mean fee as in MC.12--MC.14, the complete whole-body bound can bound a smaller interval, but does not determine its sharper value. A sharper restriction must consume every old closed row meeting that interval and its genuine measure. The exact identities (R.10)--(R.14) themselves are unchanged.

The historical field $\texttt{actual\_completed\_common\_rows}=7680$ in that old summary is its last 256-row progress checkpoint. The original producer sets the final $\texttt{complete\_common\_rows}=7721$ after checking the complete cover. New consumers retain the old bytes and independently verify all 40 part identities and the full row order; they do not reinterpret the progress field as a terminal count.

An old residual of the uncorrected background likewise requires its own already proved centre-repair conversion before being used for $f_0$ in (R.9). Equation (R.14) pays only the response-direction repair.

## 4. Exact polynomial residual on the genuine positive collar

The intrinsic bump is supported in $[1/20,9/50]$. On any collar contained in $[17/20,19/20]$, all intrinsic functions are exactly independent of $\delta$. In this section write $Q=Q_0$, $Z=(\xi,\zeta)$ and
$$
 B_Q=u\xi+Kv\zeta,\qquad S_Z=\xi^2+K\zeta^2,
                 \qquad m_Z=\langle\zeta\rangle_\phi .
$$
Expanding the actual field (R.2) gives the exact finite identity
$$
 \mathcal F(Q+\delta Z)=
     \mathcal F(Q)+\delta A_0Z+\delta^2T_2+\delta^3T_3,
 \tag{R.15}
$$
where
$$
 \begin{split}
 T_2={}&-\beta\{
      I(S_Z)Q_\phi+2I(B_Q)Z_\phi
                         +S_ZQ+2B_QZ\}
                              +Gm_ZJ(K)Z_\phi,\\
 T_3={}&-\beta\{I(S_Z)Z_\phi+S_ZZ\}.
 \end{split}
 \tag{R.16}
$$
The entire principal mean contribution is present in the last term of $T_2$. The parameter source is exactly zero here, so $s_0=-(\partial_r-A_0)Z$. Consequently
$$
 \boxed{\qquad
 f_\delta=f_0-\delta s_0-\delta^2T_2-\delta^3T_3.
 \qquad}
 \tag{R.17}
$$
No small-root quotient, angle change or radial derivative of a forcing term appears in this expansion.

Complete cellwise pair Wiener bounds give the ordinary angular $L^2$ bounds
$$
 \begin{split}
 t_2={}&bk_+\{
       (Z_0^\#)^2Q_1^\#/4
       +Q_0^\#Z_0^\#Z_1^\#/2
       +3Q_0^\#(Z_0^\#)^2\}
                          +gk_+m_Z^\# Z_1^\#,\\
 t_3={}&bk_+\{
       (Z_0^\#)^2Z_1^\#/4+(Z_0^\#)^3\}.
 \end{split}
 \tag{R.18}
$$
For example the two undifferentiated quadratic products in $T_2$ give $1+2=3$, and the factor $2I(B_Q)$ gives the exact primitive fee $1/2$. The genuine mean may use its own closed-row bound $m_Z^\#$ or the valid wider $Z_0^\#$; it is not set to zero.

Let $\|t_i\|_{2,I}$ denote the square-integrated whole-cell bound on the actual collar. Then
$$
 \|f_\delta\|_{2,I}
 \le\|f_0\|_{2,I}+|\delta|\|s_0\|_{2,I}
                    +|\delta|^2\|t_2\|_{2,I}
                    +|\delta|^3\|t_3\|_{2,I}.
 \tag{R.19}
$$
This formula and (R.9) are separate valid complete bounds. If both are evaluated in exactly the same norm and on the same interval, one may take the smaller final upper bound. There is no subtraction of unrelated upper bounds.

## 5. Complete angular source windows for the collar theorem

The repaired centre has angular degree 32 and $Z$ has degree 96. On this fixed collar, their complete residual species have degrees at most
$$
 \deg_\phi f_0\le96,\qquad
 \deg_\phi s_0\le160,\qquad
 \deg_\phi T_2\le224,\qquad
 \deg_\phi T_3\le288 .
 \tag{R.20}
$$
The cubic products and the primitive in (R.16) prove these bounds. The independent mean has degree zero and is included. Radial coefficient functions and one-sided radial derivatives do not enlarge angular degree. No band assertion is transferred through a physical-angle composition.

Use the genuine radial matrix
$P=\operatorname{diag}(K^{-1/4},K^{1/4})$ from
[the positive collar energy theorem](R133-supplement-positive-collar-energy-and-residual-sensitive-first-angular-cut-trace.md).
Define actual source norms
$$
 F_0^\#\ge\|Pf_0\|_{2,I},\quad
 S_0^\#\ge\|Ps_0\|_{2,I},\quad
 T_i^\#\ge\|PT_i\|_{2,I}.
$$
These may be bounded with the corresponding complete rowwise $P$ factor. Multiplication by a single global $p_+=\sup_I\|P\|$ is also valid but may be weaker.

For any finite $N$ and $\sigma\ge0$, (R.17)--(R.20) give
$$
 \begin{split}
 \sum_{q=0}^{N}\frac{\sigma^q}{q!}
                   \|\partial_\phi^q(Pf_\delta)\|_{2,I}
 \le{}&
 e^{384\sigma}F_0^\#
 +|\delta|e^{640\sigma}S_0^\#\\
 &+|\delta|^2e^{896\sigma}T_2^\#
       +|\delta|^3e^{1152\sigma}T_3^\#.
 \end{split}
 \tag{R.21}
$$
The radial $P$ commutes with angular derivatives. Bernstein's inequality is applied separately to each complete finite band before the triangle inequality. This does not exchange a Fourier supremum and a radial integral, and it does not give a Wiener estimate for the unknown state.

For the ordinary first angular derivative, the same reasoning gives
$$
 \|\partial_\phi(Pf_\delta)\|_{2,I}
 \le384F_0^\#+640|\delta|S_0^\#
       +896|\delta|^2T_2^\#+1152|\delta|^3T_3^\# .
 \tag{R.22}
$$
Thus both source inputs of the low trace theorem and the complete finite factorial source of the high trace theorem can use the same scalar conclusion.

If a true continuous $H^1$ core state at the same $\nu_\delta$ has already been constructed and satisfies the complete PDE, its comparison source is exactly $-Pf_\delta$. Equations (R.21)--(R.22) then pay that source without assuming high angular regularity of the true state. An approximate iterate retains its own complete residual in addition to the known reference residual, as required by [H](R133-supplement-finite-factorial-collar-bounds-and-complete-high-inner-trace-gate.md) and [A](R133-supplement-sharper-low-constants-in-finite-collar-trace.md).

## 6. Remaining actual inputs

The new conclusions are exact identities and scalar inequalities. A numerical collar consumer still needs the actual closed-row bounds for the repaired $f_0$, the full $s_{\rm raw}$ plus (R.14), the moving mean and the other low coefficients. Its square integrals must use the true interval and every original one-sided row.

The true nonlinear core, complete regular boundary and mean equations, waist condition, phase selection and low physical inner-curvature radius remain independent obligations. The residual expansion supplies usable ordinary source budgets for those tasks; it does not assert their solution.
