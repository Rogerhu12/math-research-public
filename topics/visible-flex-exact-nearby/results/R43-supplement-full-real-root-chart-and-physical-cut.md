# R43 supplement: the full real root chart reaches the actual strict cut

The exact signed-density cancellation also controls the real characteristic
chart far beyond the small complex inverse disk. For the same whole actual
family, this note proves a real canonical diffeomorphism from the root through
the physical cut used by the strict R46 calculation. The physical cut is a
nonconstant canonical graph. Its tilt is paid explicitly, together with the
exact full graph conormal and ordinary-source transformation.

This supplies the geometry needed for the remaining graph/trace gluing. It
does not assert that the graph is a constant canonical section, or that the
pointwise gradient calculation already supplies the full Sobolev gluing norm.

## 1. The actual complete real characteristic chart

All notation is that of the preceding
[exact cancellation and enlarged chart](R43-supplement-exact-characteristic-cancellation-and-enlarged-chart.md).
In particular, on the entire actual \(R=13/50000\) root collar,

\[
 D_\sigma F_\sigma=2s\mathcal C F_\sigma,
 \qquad F_\sigma(0)=1,\qquad
 |\mathcal C|\le M_C<101.014849.
\]

The previously checked nested complex paths construct the complete labels for
\(0\le\rho=s^2\le R\), every real angle and the whole real parameter box.
For real variables the scalar equation has its actual positive exponential
solution. Hence

\[
 e^{-M_C\rho}\le F_\sigma\le e^{M_C\rho}.                    \tag{G.1}
\]

The exact common-characteristic formula
\(D_0(T_+-T_-)=2s^2(F_++F_-)\) makes \(\Delta\) a positive weighted average
of these two values at earlier real times. It follows that

\[
 e^{-M_C\rho}\le\Delta\le e^{M_C\rho},
 \quad \xi=\rho\Delta^{2/3},\quad
 \phi=(T_++T_-)/2.                                         \tag{G.2}
\]

This lower bound is slightly stronger than subtracting the complex error
from one. Both statements concern the full exact labels.

Differentiation of the exact labels gives

\[
 \phi_\theta=\frac{F_++F_-}{2k}>0,
 \qquad
 \det D_{\rho,\theta}(\xi,\phi)
       =\sqrt{\rho/\xi}\,\frac{F_+F_-}{k}>0.                \tag{G.3}
\]

At zero the expressions have their removable limits, respectively \(Y_0'\)
and \(Y_0'\). At fixed \(\phi\), (G.3) gives the particularly useful identity

\[
 \boxed{\left.\frac{\partial\xi}{\partial\rho}\right|_\phi
   =2\sqrt{\rho/\xi}\,\frac{F_+F_-}{F_++F_-}.}              \tag{G.4}
\]

The harmonic mean of two numbers in \([e^{-M_C\rho},e^{M_C\rho}]\) lies
in that same interval. Combining this with (G.2),

\[
 e^{-4M_CR/3}\le\left.\xi_\rho\right|_\phi
                                      \le e^{4M_CR/3}.      \tag{G.5}
\]

At every fixed real \(\rho\), the angular map \(\theta\mapsto\phi\) is
strictly increasing, with the same actual root quarter period as \(Y_0\).
It is therefore a diffeomorphism of the complete circle. After solving this
angular equation for each \(\rho,\phi\), (G.4) is strictly increasing in
\(\rho\), starts at zero, and reaches at least

\[
 X_R=R e^{-2M_CR/3}>.000255487220464293.                     \tag{G.6}
\]

It follows directly that the complete real canonical rectangle
\(0\le\xi\le X_R\), with every canonical angle, has one unique smooth
inverse in the actual root collar. The root is included. This is a global
real inverse argument, not an extrapolation of the small complex inverse.

The complete directed numerical bounds are

| Quantity, on the whole real root collar | Bound |
|---|---:|
| \(\phi_\theta\) | \(.0512439370634<\phi_\theta<.368948530844\) |
| \(\left.\xi_\rho\right|_\phi\) | \(.965587571310<\left.\xi_\rho\right|_\phi<1.035638848006\) |
| \(\det D(\xi,\phi)\) | \(.0494805087334<J_\Psi<.382097431457\) |

For the first line use the complete real lower bound
\(U_0>.0263038151084\), the complete upper bound
\(1/k=2U_0<.359384659911\), and (G.1). The determinant line follows by
multiplication of the first two positive bounds. All field bounds are for the
same full parameter box.

## 2. The actual strict physical cut is a uniformly spacelike graph

The positive strict physical endpoint is

\[
 r_c=268136140016943/1125899906842624.
\]

Its moving-root distance is the full actual interval
\(\rho_c(p)=t(p)-r_c\), not a rounded center value. The consumer rereads
both endpoints of the true moving-root enclosure, checks
\(0<\rho_c<R\), and applies (G.2). The complete image is the graph

\[
 \xi=\chi_p(\phi),\qquad
 .000240160024215254<\chi_p(\phi)
                       <.000248188362538822<X_R.            \tag{G.7}
\]

Thus the whole physical cut lies inside the full real canonical rectangle.
The graph need not be constant. Its exact slope is

\[
 \boxed{\sqrt\xi\,\chi_p'(\phi)
       =\frac{F_+-F_-}{F_++F_-}.}                           \tag{G.8}
\]

Since the two positive logarithms in (G.1) differ by at most
\(2M_C\rho_c\),

\[
 |\sqrt\xi\,\chi_p'|\le\tanh(M_C\rho_{c,\max})
 <.024656887167=:\kappa_c<1/32,                             \tag{G.9}
\]

\[
 1-\xi(\chi_p')^2>.999392037915.                            \tag{G.10}
\]

Equation (G.10) is the exact spacelike inequality for the canonical principal
operator \(\partial_\xi^2-\xi\partial_\phi^2\). It holds uniformly around
the entire physical cut, without replacing it by a radial section.

## 3. The complete graph gradient and its conormal

For the canonical scalar height \(U\), define its true graph trace and
canonical graph conormal density by

\[
 u_g(\phi)=U(\chi_p(\phi),\phi),\qquad
 p_g=U_\xi+\xi\chi_p' U_\phi.
                                                               \tag{G.11}
\]

The plus sign is forced by the divergence flux
\((U_\xi,-\xi U_\phi)\) paired with the oriented graph normal
\((1,-\chi_p')\). Also
\(u_{g,\phi}=\chi_p'U_\xi+U_\phi\). Consequently,

\[
 \binom{p_g}{\sqrt\xi\,u_{g,\phi}}
 =\begin{pmatrix}1&\sqrt\xi\chi_p'\\
                  \sqrt\xi\chi_p'&1\end{pmatrix}
   \binom{U_\xi}{\sqrt\xi\,U_\phi}.                         \tag{G.12}
\]

This is an exact two-component transformation, including both characteristic
rows. Its pointwise Euclidean norm is at most
\(1+\kappa_c<1.024656888\); its inverse norm is at most
\((1-\kappa_c)^{-1}<1.025280219\). In particular the exact inverse is

\[
 U_\xi=\frac{p_g-\xi\chi_p' u_{g,\phi}}
                  {1-\xi(\chi_p')^2},\qquad
 U_\phi=\frac{u_{g,\phi}-\chi_p'p_g}
                  {1-\xi(\chi_p')^2}.                     \tag{G.13}
\]

The pointwise matrix bound gives the corresponding two-component weighted
\(L^2\) bound with the same graph angular measure. Higher angular Sobolev
norms additionally require the actual multiplier and composition estimates;
they are not supplied by (G.12) alone.

## 4. The actual grounded density, shear, source and periods remain present

Let \(w\) denote the actual grounded height before the final canonical
height conjugation. In canonical coordinates its divergence density is
\(\alpha_c\operatorname{diag}(1,-\xi)\), where

\[
 \alpha_c=\sqrt{\rho\mathcal U/\xi},\qquad
 L=\log\alpha_c,\qquad w=\alpha_c^{-1/2}U.
\]

The complete grounded graph conormal is therefore

\[
 p_g^{\rm gr}
 =\alpha_c(w_\xi+\xi\chi_p'w_\phi)
 =\sqrt{\alpha_c}\left[
       p_g-\tfrac12(L_\xi+\xi\chi_p'L_\phi)U\right].        \tag{G.14}
\]

The actual normal shear includes the angular derivative along the tilted
normal. It is not replaced by the radial shear at a constant section.
The Piola law on the physical cut gives the exact density identity

\[
 \boxed{p_\rho^{\rm gr}\,d\theta=p_g^{\rm gr}\,d\phi,
       \qquad d\phi=\phi_\theta\,d\theta.}                  \tag{G.15}
\]

Thus the full physical grounded conormal can be reconstructed from the actual
graph data (G.11), the full shear in (G.14), and the true angle derivative.
The preceding physical ground-state transformation must also be retained
when expressing this in the original R46 height and momentum. R46's exact
height-conjugation identity applies to that transformation; its norms are not
set to one here.

If the physical grounded equation has ordinary source \(f_{\rm gr}\), the
canonical ordinary source is exactly

\[
 \boxed{f_U=\alpha_c^{-1/2}
             \left(\frac{f_{\rm gr}}{J_\Psi}\right)
                       \circ\Psi^{-1}.}                   \tag{G.16}
\]

This is obtained first from the coordinate density Jacobian, then from the
height-conjugated equation. Boundary loads use (G.15). These identities retain
all modes and the actual mean charge. They make no assertion that a weak
metric divergence-source load already has the ordinary-source norm required
by a subsequent consumer.

The physical angular period is \(\pi/2\); the canonical period is the true
root quarter period, with \(q_c\ell_c=2\pi\). The unnormalized flux integrals
in (G.15) agree. A normalized mean has the corresponding actual period factor,
which must stay in a change to a normalized \(2\pi\) label. No mean row is
deleted by the coordinate change.

## 5. Executed consumer and remaining quantitative interface

The directed consumer is

    scripts/fourfold_negative_canonical_full_real_cut.py

and its complete report is

    notes/2026-11-13-negative-canonical-full-real-cut.json

with SHA256

    d0304d1c06b441c63d3b3ad6d665ec974f79ed116ad4b1ae28173c8d6be4165c

Run from the topic directory with a fresh output path:

~~~bash
python3 scripts/fourfold_negative_canonical_full_real_cut.py \
  --out notes/2026-11-13-negative-canonical-full-real-cut.json
~~~

The actual second root follows by the exact radial reflection, including the
simultaneous conormal orientation reversal. The chart is a genuine real
bridge from the root to the strict physical cut, and the cut has a uniformly
small paid spacelike tilt. What remains for a full operator bridge is the
whole Sobolev graph-Cauchy propagation and multiplier/frame budget from the
small R43 collar to this graph. The present note does not replace that budget,
the positive Ai/contact inputs, or the full returned strong remainder.
