# Analytic T derivative of the independent three-field finite equations

## Status, API, and scope

The closed implementation is scripts/fd2d_gc_raw_analytic_T.py.
Its SHA256 is
177a6b00c754d1d9ed11f0cf3051e5acfa9b39adc4c576e39a8320268050f857.
It defines AnalyticTRawLiftedDAE and also exports the alias RawLiftedDAE.
Construction arguments are the same as the original raw provider.

The new class leaves the frozen base provider unchanged. At a fixed vector,
its original residual and field values are returned by that base provider.
It assembles the same state, tail, central, and boundary columns, while the
T column is supplied by the chain-rule formulas below. No neighboring T value
is evaluated by the production derivative.

For a new caller:

~~~
from fd2d_gc_raw_analytic_T import AnalyticTRawLiftedDAE

problem = AnalyticTRawLiftedDAE(candidate, **recorded_settings)
F, J, data = problem.evaluate(vector, jacobian=True)
~~~

The returned data includes:

* fields_T, with axes (angle,node,(n,m,l)), for both curvature and full-Gauss
  finite merits;
* field_T, an alias for the same array;
* K_T, the scalar target-curvature derivative at each node;
* analytic_T, which also contains op_T, forcing_T, lift_x_T, lift_xi_T,
  velocity_T, gauss_T, and raw_F_T.

Thus the optional curvature helper can use field_T=data['fields_T'] without
another lifting evaluation or a finite difference. The complete finite
Gauss derivative is
\[
 G_T=l(n_T)+n(l_T)-2m(m_T)-K_T,
\]
where n_T,m_T,l_T are the three fields_T entries.

T remains an outer physical metric-design parameter. Changing T is not
same-g refinement. The purpose here is to differentiate the already stated
finite design problem accurately, including near its open physical boundary.

## 1. Why the old boundary difference is unsuitable

The frozen provider used a centered T difference with
\[
 \varepsilon=\min(10^{-6}(1+|T|),.2T,.2(T_{\max}-T)).
\]
When an actual finite search reached approximately
\(T_{\max}-2.25\times10^{-13}\), this rule gave a step around
\(4.5\times10^{-14}\). Cancellation then becomes a concrete numerical risk.

The selected positive-clock profile already supplies analytic a_T, c_T,
K_T, and J_T, where J=S_x. The tail supplies \(\kappa_y\), and the native
reader supplies analytic \(\kappa_{yy}\). These are enough to differentiate
the complete raw equations, including the x derivative in the lifting force.
There is no need to enlarge the physical domain or extrapolate beyond it.

## 2. Fixed-coordinate scalar operators

All derivatives in this note hold fixed the stored computational x and xi,
the nodal correction coefficients, the central coefficients, and the tail
controls. The fixed reference mesh, angle map U(x,xi), its derivatives,
and the lifting weights have zero T derivative.

Write
\[
 \omega=U_\xi,\quad v=U_x/\omega,\quad
 \zeta=\frac{J}{a\omega},\quad \gamma=Jc,\quad c=a_s/a.
\]
Then
\[
 \zeta_T=\frac{J_T-Ja_T/a}{a\omega},\qquad
 \gamma_T=J_Tc+Jc_T,\qquad v_T=0.
\]
The correction velocity before angular projection is
\[
 f_n=\zeta m_\xi+\gamma(l-n)+vn_\xi,\qquad
 f_m=\zeta l_\xi-2\gamma m+vm_\xi.
\]
Consequently its operator derivative consists of:

* n-to-n: \(-\gamma_T\);
* m-to-n: \(\zeta_T\partial_\xi\);
* l-to-n: \(+\gamma_T\);
* m-to-m: \(-2\gamma_T\);
* l-to-m: \(\zeta_T\partial_\xi\).

The advection blocks have no T derivative. Projecting these expressions by
the same even/odd matrices PE and PO gives exactly op_T in the new class.
No second-form entry appears in a denominator.

## 3. T derivatives of the full lifting

In component order (n,m,l), let
\[
 V(U)=(\cos^2U,-\sin U\cos U,\sin^2U),\qquad y=a\sin U.
\]
The complete lifting is
\[
 L=w_t(x)\kappa(y)V(U)+(w_c(x)n_*(\xi),0,0).
\]
The central term is independent of T. Since U is fixed,
\[
 y_T=a_T\sin U,\quad
 y_\xi=a\cos U\,U_\xi,\quad
 y_{\xi T}=a_T\cos U\,U_\xi.
\]
Also
\[
 a_x=a_sJ,\qquad
 (a_x)_T=(a_s)_T J+a_sJ_T,
\]
and therefore
\[
\begin{aligned}
 y_x&=a_x\sin U+a\cos U\,U_x,\\
 y_{xT}&=(a_x)_T\sin U+a_T\cos U\,U_x .
\end{aligned}
\]

Put \(W=\kappa(y)V(U)\). Direct differentiation gives
\[
\begin{aligned}
 W_T&=\kappa_y y_TV,\\
 W_{xT}
  &=(\kappa_{yy}y_Ty_x+\kappa_y y_{xT})V
    +\kappa_y y_TU_xV_u,\\
 W_{\xi T}
  &=(\kappa_{yy}y_Ty_\xi+\kappa_y y_{\xi T})V
    +\kappa_y y_TU_\xi V_u.
\end{aligned}
\]
Hence
\[
 L_T=w_tW_T,\qquad
 L_{xT}=w_t'W_T+w_tW_{xT},\qquad
 L_{\xi T}=w_tW_{\xi T}.
\]
The derivative of every finite Fourier correction at fixed stored
coefficients is zero, so the full field derivative is L_T.

The \(\kappa_{yy}\) required here is the third derivative of the explicitly
given one-dimensional generator angle. It is available for both the
C4 signed-bubble family and the positive Bernstein family. This introduces
no C3 regularity requirement on the reconstructed surface. All the
surface regularity statements remain those of the existing C2 native-field
definition.

## 4. Complete forcing and raw residual derivative

The exact-lifting forces before projection are
\[
\begin{aligned}
 b_n&=\zeta L_{m,\xi}+\gamma(L_l-L_n)+vL_{n,\xi}-L_{n,x},\\
 b_m&=\zeta L_{l,\xi}-2\gamma L_m+vL_{m,\xi}-L_{m,x}.
\end{aligned}
\]
Their derivatives are therefore
\[
\begin{aligned}
 (b_n)_T={}&\zeta_TL_{m,\xi}+\zeta L_{m,\xi T}
 +\gamma_T(L_l-L_n)+\gamma(L_{l,T}-L_{n,T})
 +vL_{n,\xi T}-L_{n,xT},\\
 (b_m)_T={}&\zeta_TL_{l,\xi}+\zeta L_{l,\xi T}
 -2\gamma_TL_m-2\gamma L_{m,T}
 +vL_{m,\xi T}-L_{m,xT}.
\end{aligned}
\]
Projection gives forcing_T. If the saved correction vector at a node is y,
the complete projected velocity derivative is
\[
 f_T=op_T\,y+forcing_T .
\]

The computational cell widths are fixed. Thus the derivative of a
trapezoidal Codazzi residual is
\[
 -\tfrac12(f_T(x_{j+1})+f_T(x_j)).
\]
The full sampled Gauss derivative is
\[
 (nl-m^2-K)_T=lL_{n,T}+nL_{l,T}-2mL_{m,T}-K_T.
\]
The original projected Gauss rows use the same PE projection as before.

All raw correction boundary rows are independent of T. The actual central
axis-gap equation is also independent of T at fixed central coefficients:
the central a0 and the actual central curve definition do not change with
this coast parameter. Accordingly their T entries are zero. These blocks
form raw_F_T in exactly the original residual order.

This supplies the entire Jacobian column. It does not replace the nonlinear
residual by a linearized model and does not delete any projected or unprojected
Gauss mode.

## 5. Actual implementation checks

The final source was genuinely checked using the saved K15 initializer
notes/2026-11-12-fd2d-local-recovery01-k15.npz. The input's explicit
profile/tail/base kinds and candidate SHA were used. The final check is

notes/2026-11-12-fd2d-metric-raw-analytic-T-check-02.json.

It naturally completed with exit 0 in session 33442, chunk a52a96, about
27.95 seconds. Its exit receipt is stored alongside the report.

The comparison with the frozen provider at the actual interior parameter
gave exact floating equality for:

* the original residual F;
* the complete independent fields;
* every Jacobian column except the deliberately replaced T column.

For the analytic column, independent centered differences at the actual
interior T gave a final relative L2 difference of
\(6.744\times10^{-10}\) for raw_F_T. The complete fields_T check was
nonzero and had relative difference \(7.637\times10^{-10}\).

A separately labelled synthetic derivative probe retained the same saved
state and controls but set
\(T=T_{\max}-2.25\times10^{-13}\). It is not a new solved field.
Second-order backward differences used only physical-domain points
T, T-h, and T-2h, with h down to \(2.5\times10^{-6}\). The final raw_F_T
relative difference was \(1.044\times10^{-9}\); fields_T gave
\(8.940\times10^{-10}\). Every finite probe was strictly inside the
actual physical interval.

These finite checks support the implementation of the displayed analytic
formulas. They are not interval bounds for floating roundoff or a proof
that the supplied finite field solves the surface problem.

An earlier successful version-01 check is preserved together with the exact
executed source snapshot. The only subsequent change added direct data keys
fields_T and K_T; the final source was then actually rerun and bound by
version 02 rather than reusing the earlier source identity.

## 6. Use with a finite Gauss complement

For the angular complement \(P_h=I-E\,PE\) on the same recorded finite grid,
the derivative is
\[
 (P_hG)_T=P_h(lL_{n,T}+nL_{l,T}-2mL_{m,T}-K_T).
\]
In exact Fourier arithmetic, \(P_hK_T=0\) because K_T is angularly constant.
A floating implementation can measure its small projection roundoff
explicitly; the new data keys retain K_T so no term needs to be hidden.

This is still a finite-grid residual. High modes beyond that grid and all
continuous radial/angular errors remain separate. The analytic T column
does not turn an underresolved finite search into a continuous certificate.

