# Actual three-field definition and fixed-material reconstruction

## Status and source identity

This note specifies the mathematical object read by
scripts/fd2d_gc_raw_native_field.py. The source was reconstructed after the
executor became unavailable; its new Git blob is
d386d2b0cfbddb61250ba6b4754dc88d43531e79. This is a new source identity, not
the SHA of the earlier local reader. Its floating implementation still needs
the restored implementation check to run in an available executor.

The earlier local comparison, derivative, and flat-tail reconstruction checks
were observed to finish before the environment was lost. They are historical
observations until their output files are found in a published commit or the
checks are actually rerun. This note does not recreate their JSON reports or
claim that lost numerical arrays are saved.

The object is an explicitly selected finite field and an ODE-defined map. It
does not claim that a raw finite solver iterate solves Gauss--Codazzi, that its
cut correction vanishes, or that its formal shape eigenvalues are the actual
curvatures of the reconstructed map. R119, R124, R125 and R129 give the relevant
posterior statements. The helper imposes no additional acceptance criterion.

## 1. Bound input and independent fields

The bound array packet contains:

* strictly increasing computational nodes \(x_i\);
* corrections \(c_i\in\mathbb R^{3K+2}\), in the order
  \(n_0,n_2,\ldots,n_{2K};m_2,\ldots,m_{2K};l_0,l_2,\ldots,l_{2K}\);
* parameters consisting of \(K\) central curvature coefficients, \(K+1\)
  tail controls, and the physical coast length \(T\).

Each saved binary floating number denotes that exact binary rational in the
mathematical definition. A floating evaluator approximates this definition;
its roundoff is not silently declared zero.

For \(x_i\le x\le x_{i+1}\), define the coefficient function by
\[
 c(x)=(1-t)c_i+t c_{i+1},\qquad
 t=\frac{x-x_i}{x_{i+1}-x_i}.
\]
The actual derivative in the cell is
\[
 c_x=\frac{c_{i+1}-c_i}{x_{i+1}-x_i}.
\]
At a node, a selected left or right derivative changes this last quantity
only. The value and every angular derivative have the same value from
either side. The implementation returns saved endpoint values directly.

There are three independent fields. The reader never reconstructs \(l\) by
dividing by \(n\), including at flat arcs where all three fields vanish.

The definition records the selected physical-profile factory and the
selected tail-family factory. It does not infer a positive clock or a
positive tail from missing metadata. The supported explicit alternatives
are legacy_coast / positive_clock and signed_bubble / positive_bernstein.
The central base_kind is also explicit. A circle base and a balanced-seed
base have the same prescribed circumference but are different functions.

The reference coast length specifies the stored computational mesh.
Changing that reference without remapping the saved coefficients changes
the object; the reader does not perform such an unrecorded recentering.

## 2. Target and angle charts

Let \(s=S(x)\), \(J=S_x>0\) denote the selected radial chart for the chosen
physical profile. Write
\[
 g=ds^2+a(s)^2du^2,\qquad
 c=\frac{a_s}{a},\qquad K_g=-\frac{a_{ss}}a .
\]
The field uses the recorded moving angular chart
\[
 u=U(x,\xi)=(1-\beta(x))U_*(\xi)+\beta(x)\xi .
\]
Here \(U_*\) is the fixed balanced-seed material-angle map and \(\beta\)
is the quintic step on the recorded blend interval. In particular the
chart is independent of the central curvature parameters.

Put \(\omega=U_\xi>0\) and \(v=U_x/\omega\). The physical derivatives are
\[
 \partial_u=\omega^{-1}\partial_\xi,\qquad
 \partial_s=J^{-1}(\partial_x-v\partial_\xi).
\]
For any scalar field \(f\),
\[
 f_u=f_\xi/\omega,\qquad
 f_{uu}=\frac{f_{\xi\xi}-f_uU_{\xi\xi}}{\omega^2}.
\]
These formulas convert derivatives of the actual finite function, not
values of a solver's ODE right-hand side.

The inverse \(U(x,\xi)=u\) used for numerical evaluation is bracketed.
The implementation starts from the seed inverse / identity interpolation,
uses safeguarded Newton steps, and caches at most two seed inverse arrays.
It does not keep an unbounded point cache. Its reported inversion error
is a numerical diagnostic, not an interval inverse certificate.

## 3. Complete liftings

Let \(S_5(t)=10t^3-15t^4+6t^5\) on \([0,1]\), extended by 0 and 1.
For the recorded domain endpoint \(x_e\), the current lifting uses
\[
 w_t(x)=S_5\!\left(\frac{x-.42x_e}{.58x_e}\right),\qquad
 w_c(x)=1-S_5\!\left(\frac{x}{\min(.55,.4x_e)}\right).
\]
These expressions are part of the definition, rather than a freedom to
change the function after a residual is computed.

For the chosen developable generator, let
\(\kappa(y)=\alpha'(y)\), \(y=a(s)\sin U\), and
\[
 V(U)=(\cos^2U,-\sin U\cos U,\sin^2U).
\]
The full lifting, in the order \(n,m,l\), is
\[
 {\cal L}(x,\xi)=w_t(x)\kappa(y)V(U)
       +(w_c(x)n_*(\xi),0,0).
\]
For balanced_seed, \(n_*=1/\rho_*(\xi)\); for circle, \(n_*=1/a_0\).
The finite Fourier correction is added to this full function. There is
no angular projection of the developable lifting in this definition.

A signed-bubble tail and a positive-Bernstein tail are separate factories.
For the latter,
\[
 \kappa(y)=\frac{630}{a_c-c_0}
 q^4(1-q)^4\sum_{i=0}^{P-1}p_i B_i^{P-1}(q),
 \qquad q=\frac{|y|-c_0}{a_c-c_0},
\]
on \(0<q<1\), and zero outside. Equal controls \(p_i=A\)
recover the exact \(A S_9\) generator by partition of unity.

The evaluator differentiates the chosen lifting analytically. For example,
with \(y=a\sin U\),
\[
\begin{aligned}
 y_x&=a_sJ\sin U+a\cos U\,U_x,\\
 y_\xi&=a\cos U\,U_\xi,\\
 y_{\xi\xi}&=a(-\sin U\,U_\xi^2+\cos U\,U_{\xi\xi}),\\
 y_{x\xi}&=a_sJ\cos U\,U_\xi
 +a(-\sin U\,U_xU_\xi+\cos U\,U_{x\xi}).
\end{aligned}
\]
For \(W=\kappa(y)V(U)\),
\[
\begin{aligned}
 W_\xi&=\kappa_y y_\xi V+\kappa V_uU_\xi,\\
 W_x&=\kappa_y y_xV+\kappa V_uU_x,\\
 W_{\xi\xi}
 &= (\kappa_{yy}y_\xi^2+\kappa_y y_{\xi\xi})V
 +2\kappa_y y_\xi V_uU_\xi
 +\kappa(V_{uu}U_\xi^2+V_uU_{\xi\xi}),\\
 W_{x\xi}
 &= (\kappa_{yy}y_xy_\xi+\kappa_y y_{x\xi})V
 +\kappa_y(y_xU_\xi+y_\xi U_x)V_u
 +\kappa U_xU_\xi V_{uu}+\kappa U_{x\xi}V_u .
\end{aligned}
\]
Thus no numerical derivative of \(l,m,n\) is used by the native evaluator.

## 4. The piecewise field produces a C2 actual map

Let
\[
 A=\begin{pmatrix}0&0&-l\\0&0&-m\\l&m&0\end{pmatrix}.
\]
At fixed physical material angle \(u\), define
\[
 F_s=FA,\qquad X_s=Fe_1,
\]
from the actual central curve and its actual frame for the saved central
parameter vector. The standard basis vector \(e_1=(1,0,0)^T\) in these
matrix formulas is distinct from the moving vector \(Fe_1\).

Because the coefficient functions are continuous piecewise linear,
all of their angular derivatives are continuous across radial nodes.
The full liftings have the same property. The chart change preserves
continuity of \(A,A_u,A_{uu}\). The radial derivative \(A_s\) need not
be continuous, and no such assumption is made.

On each compact material rectangle, the integral equation
\[
 F(s,u)=F(0,u)+\int_0^sF(t,u)A(t,u)\,dt
\]
has a unique solution. Differentiating this integral equation once and
twice with respect to \(u\) gives linear integral equations with continuous
coefficients and inhomogeneous terms. Their solutions \(F_u,F_{uu}\)
are continuous. In particular,
\[
 X_s=Fe_1,\quad X_{ss}=FAe_1=lFe_3,\quad
 X_{su}=F_ue_1
\]
are continuous, and differentiation of
\[
 X(s,u)=X(0,u)+\int_0^sF(t,u)e_1\,dt
\]
twice in \(u\) gives continuous \(X_{uu}\). Therefore the actual map is
\(C^2\) across every computational radial node.

This proves exactly the regularity needed here. It does not assert that
the independent auxiliary second form is the second form of \(X\).
That latter assertion is an exact compatibility consequence or is paid
for by a posterior estimate. It also does not assert \(C^1\) second form
or \(C^3\) immersion; neither is necessary for this construction.

The fields \(m,n\) are locally absolutely continuous in \(s\), piecewise
\(C^1\). Their distributional first derivatives have no delta terms because
the fields themselves are continuous. The R119 defect equations can
therefore be integrated cell by cell with shared endpoint values and no
additional jump term.

## 5. Residuals with all three fields independent

Define
\[
 G=ln-m^2-K_g,\quad
 R_m=m_s-l_u/a+2cm,\quad
 R_n=n_s-m_u/a-c(l-n).
\]
The native derivative formulas above provide these quantities directly.
No \(1/n\) occurs. With
\[
 B=\begin{pmatrix}0&-a_s&-am\\a_s&0&-an\\am&an&0\end{pmatrix},
\]
direct multiplication gives
\[
 BA+A_u-AB-B_s
 =a\begin{pmatrix}0&G&R_m\\-G&0&R_n\\-R_m&-R_n&0\end{pmatrix}.
\]
The spectral norm of this skew matrix is
\(a\sqrt{G^2+R_m^2+R_n^2}\).
This is the three-component residual already used in R119/R129.

Let \(D=F_u-FB\) and \(C=X_u-aFe_2\).
Then, almost everywhere and hence in the integral sense,
\[
 D_s=DA+F(BA+A_u-AB-B_s),\qquad C_s=De_1.
\]
Because \(A\) is skew, its propagator is orthogonal. Thus the resulting
error bound has no artificial exponential factor. All angular modes of
\(G,R_m,R_n\), including unresolved product modes, contribute to the
actual residual. A projected collocation residual is not a substitute.

An exact central core can differ from the finite angular representation
used by a solver. If this creates a nonzero initial \(D\), it is included
in the initial posterior error. The reader binds the actual core and
does not silently replace it by a sampled curve.

Likewise, an exact cut lifting is only the function added at the cut.
The actual full cut field is exact only when the saved correction is
zero there. The reader reports the saved endpoint condition and never
zeros a nonzero correction on input.

## 6. R124 fixed-material two-jet state

The numerical body interface carries the 24 entries
\[
 [X_3,F_9,r_3,b_3,v_3,q_3],
\]
where
\[
 r=\operatorname{vee}(F^TF_u),\quad b=F^TX_u,\quad
 v=r_u,\quad q=b_u.
\]
Write \(\alpha=(m,-l,0)\). At fixed \(u\), the equations are
\[
\begin{aligned}
 F_s&=F[\alpha]_\times,&X_s&=Fe_1,\\
 r_s&=r\times\alpha+\alpha_u,&
 b_s&=-\alpha\times b+r\times e_1,\\
 v_s&=v\times\alpha+r\times\alpha_u+\alpha_{uu},&
 q_s&=-\alpha\times q-\alpha_u\times b+v\times e_1 .
\end{aligned}
\]
The computational \(x\) right-hand side is multiplied by \(J=S_x\).
The material angle is held fixed; following a fixed computational angle
without the appropriate drift would define a different calculation.

At the actual central core,
\[
 r=(a_0n_{\rm core},0,0),\quad b=(0,a_0,0),\quad
 v=(a_0(n_{\rm core})_u,0,0),\quad q=0.
\]
The actual Cartesian derivatives are
\[
\begin{aligned}
 X_s&=Fe_1,&X_u&=Fb,&X_{ss}&=F(0,0,l)^T,\\
 X_{su}&=F(r\times e_1),&
 X_{uu}&=F(r\times b+q).
\end{aligned}
\]
The actual normal is computed from \(X_s\times X_u\), and the actual
Gram matrix is computed from those derivatives. These expressions remain
the right numerical quantities when the independent auxiliary \(n\)
differs from the normal curvature of the ODE map. Integration, roundoff,
and coefficient errors still require the stated posterior bounds before
these floating values can be used as global certificates.

## 7. Recovery and verification record

The prior local implementation run observed comparisons at native nodes,
one-sided interfaces, and arbitrary angles; safeguarded inverse checks;
centered finite-difference checks of the analytic angular/radial derivatives;
and a 24-angle exact-developable-tail reconstruction. The observed successful
run was session 19511, chunk 6bdf30, exit 0. An earlier naive inverse run,
session 33819, chunk 53f85d, actually failed with exit 1 and was replaced
by the bracketed inverse; that failure must not be erased from any recovered
record.

Those session identifiers describe the old execution, not a new verification
of this reconstructed source. The corresponding arrays and reports must be
recovered from an existing published commit or recomputed. A new run must
bind the new source bytes and its own actual exit receipt. Nothing in this
note upgrades an unfinished BVP or a finite sample into a full-surface result.
