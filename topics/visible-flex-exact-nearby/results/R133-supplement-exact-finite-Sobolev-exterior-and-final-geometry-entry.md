# R133 supplement: exact finite-Sobolev exterior and the existing final geometry gates

2026-11-15, visible-exact-astra-0df9.

**Proved analytic transfer on the stated input domain.**
The actual exterior obtained from S.38--S.46 and T.25--T.34 satisfies the curvature, intrinsic-length and common-world conclusions needed by the existing final geometry theorem. No positive angular analyticity and no membership in the old label graph X_224 are asserted for the Nash limit.

The fixed physical inner datum is real-even, with
$$
 \|\gamma/r_\gamma\|_{A_0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576},
 \qquad r_\gamma=10^{-9}.
 \tag{G.1}
$$
The underlying controlled metric and its parameter boxes are exactly those of S. The complete inner core matching is still a hypothesis when this exterior is attached to the core.

## 1. Primary inputs and what is being extended

Use the following already proved results on the same object:

- [S, nonlinear far matching and exact Nash limit](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md), especially S.38--S.46.
- [T, single frame and true C2 flat disk](R119-supplement-positive-collar-principal-invariance-and-single-frame-reconstruction.md), T.25--T.34.
- [E, reference graph scale](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md), E.3 and E.22.
- [M, finite-Sobolev holonomy mean](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md), M.2--M.4 and M.15.
- [F, actual cap input budgets](R119-supplement-actual-cap-fixed-input-budget-and-body-Nash-entry.md), F.5--F.8.
- [The two-input zero-width cap](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md), M.3--M.7 and its finite-Sobolev output.
- [The original complete exterior geometry](R133-supplement-current-complete-exterior-curvature-and-common-world-caps.md), denoted E_ext below.
- [The complete final C0 geometry theorem](R133-supplement-final-geometry-from-complete-C0-ball.md), denoted B below.

E_ext's original analytic tail input was X=||X_Pi(a)||_X224. The new limit lives in E_1856. We therefore prove its actual pointwise curvature bounds directly. The old numerical geometry, exact profile inequalities, radial length and final rational budget are read without recomputation.

## 2. The true four states are uniformly small, including their mean

Write
$$
 R_u=16\|u_\infty\|_{E_{1856}}.
$$
The already proved seed bound and S.39 imply R_u<2^-24. At zero ordinary residual, E.22 gives the complete true four-state bound X_20^true<=R_u. This state contains the holonomy small root in K; it is not a bound only for K_perp.

On every infinite-tail cell the true H2 bound of each of P,K,U,V is at most C_j R_u, where M.4 gives sup C_j<2^-12. On the actual finite connector the bound is at most 2^-440 R_u. Using the already employed full-circle embedding A0<=2H2, the complete pointwise sum
$$
 N=|P|+|K|+|U|+|V|
 \tag{G.2}
$$
therefore satisfies
$$
 N_{\rm tail}<8\,2^{-12}R_u<2^{-18},\qquad
 N_{\rm connector}<8\,2^{-440}R_u<2^{-18}.
 \tag{G.3}
$$
The reference-to-true conversion is exactly E.22, including the current first parameter and all mean terms. No unknown finite-Sobolev function is evaluated at a complex angle.

All fixed-profile inequalities from E_ext.2 remain valid on the same real controlled parameter box:
$$
 0<w/a<1/8,\qquad |w_a|<1/8
 \quad\hbox{on the entire infinite mixed tail}.
 \tag{G.4}
$$
They concern only the metric profile. They do not require the nonradial solution to lie in the original analytic label graph.

## 3. The actual long segment also satisfies the old strong small ball

Let f_B=u_infinity(B)/s_B and f_*=Phi_gamma(f_B), with the same original physical scales s_B and s_R. F.8 and the actual zero-width cap value bound give
$$
 \|f_B\|_{\dot A^2_0}<2^{-100},\qquad
 \|f_*\|_{\dot A^2_0}<10^{-8}.
$$
Consequently,
$$
 \|(f_B,f_*)\|_{\partial,0}
 <2^{-100}+10^{-8}<2^{-25}.
 \tag{G.5}
$$
This is precisely the sum of the two full |m|^2-weighted boundary norms. There is no omitted angular mean: the two boundary data are nonmean, and their complete slope mean is the unique holonomy root.

For clarity, the [actual nonlinear long Dirichlet theorem](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md), D.4--D.22, extends to angular width zero here directly. Its exact two-ended Green kernel, lift bounds 32 and 16, Banach-algebra products and the 1/16 contraction use only the multiplicative Fourier weights; each argument still holds with weight one. This is a proof on the full zero-width Banach space, not a limit that assumes the input has a positive analytic width. The unique solution has
$$
 \|h\|_{\mathcal Y_0}\le2^{-20},\qquad
 |K_0|\le256\|h\|_{\mathcal Y_0}^{\,2},\qquad N<4\|h\|_{\mathcal Y_0}\le2^{-18}.
 \tag{G.6}
$$
The long solution is the one already used by the actual cap graph; identical boundary data and uniqueness in this same ball identify it.

There is enough finite regularity to justify its full equations and geometry. The present f_B has more than six finite angular derivatives by S/F, and the cap's M one-high estimates give f_* in H6 from the finite input norms. Thus their one angular derivative has finite dot A2 norm. Real angular translation is strongly continuous in Y0. Difference quotients of the fixed-point equation obey [I-G_D integral(DQ)] Delta h=Delta h_D, where the integral is along the segment between h and its translate. Its operator norm is at most 1/16 by the original D.13 bound, so the inverse has norm at most 16/15. The boundary derivative makes Delta h_D converge in Y0, and continuity of DQ makes these inverses converge there. Thus h_theta belongs to Y0. This supplies the angular derivatives in the identity for the radial derivative of the holonomy functional in section 5 of the long Dirichlet theorem. The nonmean equation and that identity recover the full mean equation, without a positive strip or an additional free mean boundary condition.

The two mean slopes and the mean-height span remain D.24 and the same single height constant. At B they match the S solution by its true far value equation and common holonomy root.

## 4. Exact curvature formula with the large slope coefficient paid correctly

At a true solution put
$$
 A=\frac{aw_a}{w},\quad q=w^2,\quad E=1+q,\quad
 J=1+K+EU,\quad D=1-q(2K+K^2+EP^2).
$$
The physical orthonormal shape matrix from E_ext.20 is
$$
 \mathsf S=\frac{w/a}{n_z}
 \begin{pmatrix}
  [A(1+K)/E+K_t]/E &(V-P)/\sqrt E\\
  (V-P)/\sqrt E&U+(1+K)/E
 \end{pmatrix},\qquad n_z=\sqrt{D/E}.
 \tag{G.7}
$$
An overall vertical reflection only reverses the common orientation sign; the absolute curvature bounds are unchanged.

The exact equation, valid also when A is large, is
$$
 K_t=-AU-2AK+\mathcal R,\qquad
 \mathcal R=\frac{E(V-P)^2+
          A(K^2+2EKU+EU^2-qP^2)}{J}.
 \tag{G.8}
$$
The old estimate |R|<=64N^2 used |A|<=7 and is not applied to the infinite tail.

On that tail, q<1/4 by M.3--M.4 and N<=2^-18 by (G.3), so E<2, J>1-3N>1/2, D>1/2, and n_z^-1<2. The two numerator groups in (G.8) have absolute values at most 8N^2 and 8|A|N^2. Since (w/a)|A|=|w_a|, the complete bound is
$$
 \frac wa|\mathcal R|
 \le16\left(\frac wa+|w_a|\right)N^2.
 \tag{G.9}
$$
It retains the actual physical derivative w_a. There is no isolated inverse physical-radius charge.

Using (G.4), the first row sum of (G.7) is bounded above by
$$
 2\left\{\frac18(1+4N)+4N^2+\frac14N\right\}
   =\frac14+\frac32N+8N^2<\frac12.
 \tag{G.10}
$$
The second row sum is at most
$$
 \frac14(1+4N)<\frac12.
 \tag{G.11}
$$
Every displayed bound uses the full K, not K_perp. Thus the entire infinite tail has |kappa_i|<1/2. This conclusion uses the true equation and full low states, rather than the old analytic vector-C2 difference E_ext.14.

On the finite connector, its unchanged metric coefficients still satisfy the actual 0<w/a<5/18 and |A|<=7 conditions of E_ext.18. The two real bumps in any infinite cell belong instead to the already covered profile (G.4); a large A is never put in the finite bound. On the long segment A=1 and w/a<5/28. With (G.3) and (G.6), the original complete calculation E_ext.19--E_ext.22 applies directly to these finite pieces and gives |kappa_i|<2.

The true flat disk supplied by T has zero second fundamental form. All finite seams and the accumulation circle are genuinely C2 by S/T. Hence the entire exact exterior satisfies
$$
                         |\kappa_i|<2.
 \tag{G.12}
$$

## 5. The same world position, normal and flat-disk conclusions

The reference metric is unchanged and a_R<7*10^-6. Its true slopes satisfy w/a<5/18 everywhere outside R, including (G.4) and the flat disk. Therefore E_ext.24 gives, without any new norm conversion,
$$
 \int_0^{a_R}\sqrt{1+w(a)^2}\,da<8\cdot10^{-6}=:\ell_*.
 \tag{G.13}
$$
Once the complete core B,C and curvature means are matched, use the single actual frame and height constant of T. Then every exterior point is reached from its actual same-angle core endpoint by this material radial curve. Exact isometry and (G.12) give
$$
 |F(a,\theta)-F(R,\theta)|<\ell_*,
 \qquad |N(a,\theta)-N(R,\theta)|<2\ell_*.
 \tag{G.14}
$$
In particular, for the same common world origin,
$$
 |F|<R_B+\ell_*,\qquad
 F\cdot N>s_B-\ell_*(1+2R_B)
 \tag{G.15}
$$
if R_B,s_B are the actual core endpoint bounds. No exterior height is reset.

T's flat disk has a strictly positive radius at most a_R. After the actual core and waist conditions are solved, T also gives the common axis and mirrored lower disk. The fixed phase offsets of the two disks need not be equal: each obeys the same full material-circle equivariance. Thus E_ext's height intervals and the frozen-metric phase construction apply without assuming two independently normalized angular phases.

## 6. Exactly what remains before the final geometric theorem applies

Suppose that the same complete core solution, including its actual cap on [9/10,25/8], has been obtained, with all waist u, physical fourth Robin, both mean and true inner-cap matching rows, and that it satisfies
$$
 \max(\|\widetilde u-u_{\rm ac1}\|_{C^0},
      \|\widetilde v-v_{\rm ac1}\|_{C^0})\le10^{-4},
 \qquad |\widetilde\nu-\nu_0|\le10^{-5},\qquad\eta=\eta_0.
 \tag{G.16}
$$
This complete state comparison includes the repair, every unknown high mode, the true mean and the actual moving-angle conversion. The cap value ball alone is not identified with (G.16).

The other missing input is the actual physical inner curvature datum (G.1) produced by this core, with its full high norm. A moving finite-97 trace is not a finite physical Fourier tail.

Under these remaining hypotheses, (G.12)--(G.15) supply the geometric conclusions for which B used the old analytic exterior sphere. They are the same curvature, length, positive disk and common-world bounds, now proved for the actual finite-Sobolev Nash solution. No assertion of old analytic-label membership is needed.

The rest of B is already complete. In particular its B.2--B.3 uses the full periodic frame and the actual mean interval to obtain the integer winding one and m_0=-a_0, before invoking a global embedding argument. Its B.6 uses the already paid complete141 waist comparison fees
$$
 b_{Q,0}<0.000108594777739,\qquad
 b_{F,0}<0.000232681812735.
$$
Those are reference-model comparison fees, not independent prescribed world anchors. Its full forward-state and geometry arithmetic, including public run43584188751's 26 gates, is reused without rerunning the geometry, profiles, model ODE, quadratures or rational budget.

Thus (G.16), true core/waist/phase matching, and (G.1) are a sufficient same-object entry to the already established final geometric inequalities and fixed-metric marker-phase family. This paper has not solved those core equations, supplied the full core inverse or verified (G.16), and does not declare the research complete.
