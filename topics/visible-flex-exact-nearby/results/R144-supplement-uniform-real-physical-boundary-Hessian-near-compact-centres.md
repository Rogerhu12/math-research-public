# R144 UH: a uniform full-mean physical boundary Hessian near the compact centres

2026-11-27, visible-exact-astra-fb31ed6-20261127.

**Proved on a stated real, nonanalytic neighbourhood.** At both the original
cut \(L=9/10\) and the actual outer endpoint \(R=25/8\), the compact centre
admits the same uniform full-Fourier physical-chart estimate

\[
 \|D^2\Psi(Q)[h,k]\|_{L^2_\theta\oplus_1L^2_\theta}
 \le2\bigl(\|h\|_{H^1_\phi\oplus_1H^1_\phi}
                 \|k\|_{L^2_\phi\oplus_1L^2_\phi}
          +\|k\|_{H^1_\phi\oplus_1H^1_\phi}
                 \|h\|_{L^2_\phi\oplus_1L^2_\phi}\bigr).
 \tag{UH.1}
\]

Here \(Q=Q_*+q\), with the complete component-sum \(A^3\) norm of
\(q\) at the relevant endpoint at most \(10^{-6}\).
The two moving means, both physical curvature means, and the normalized
angle are retained. The background may have an arbitrary infinite tail.
Only a single direction in each product in (UH.1) pays one derivative.

The exact chart and its differentials are already proved in
[G.1--G.9](R133-supplement-complete-normalized-angle-gauge-and-residual-Hessian.md).
The fixed selected-cut remainder in
[CH](R133-supplement-real-H1-physical-chart-remainder-and-complete-boundary-error.md)
is also an existing conclusion. They are not claimed anew.
The new content is the explicit uniform domain at the **compact** centres,
including the actual raw outer endpoint, and the common small, full-mean
bilinear estimate there. This domain is much larger in its low norms than
the previous high-background cap neighbourhood.

This is the physical chart's Hessian, not the entire nonlinear long DN
map or a full inverse. In particular the outer DN qualification in
[QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md)
still has its independent smaller endpoint bound \(10^{-9}\), its
height domain, and all its actual mean/Robin/height ports.

## UH1. Spaces and the two genuine background domains

All means and \(L^2\) norms use normalized measure on the period
\(\pi/2\) circle, and all physical frequencies are \(4j\).
Use \(I=\partial_\phi^{-1}P_{\ne0}\), with zero Fourier constant.
For a pair, \(E(h)\) and \(H(h)\) denote respectively the component-sum
\(L^2\) and \(H^1\) norms. Thus \(E(h)\le H(h)\); no Euclidean pair
conversion is implicit. The component-sum Wiener norm is

\[
 \|q\|_{A^3}
   =\sum_{j\in\mathbb Z}(1+4|j|)^3
                      (|q_{1,j}|+|q_{2,j}|).
 \tag{UH.2}
\]

It bounds the component-sum suprema of each of the first three physical
angular derivatives as well as the values. No positive spatial strip
follows from (UH.2).

Fix the same intrinsic \(\eta_0\), the same true selected metric, and the
same compact centres from
[SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md).
At every \(r\ge9/50\), these centres are exactly the single function
\(Q_*=(u,Mv/m)\), independently of the original
\(|\delta|\le10^{-10}\). They are not declared to solve the nonmean PDE.

### The original cut \(L=9/10\)

Use the existing CH.1--CH.2 at the original repaired centre
\(Q_c=Q^{\rm sel}_0(L)\). In particular

\[
 \begin{gathered}
 |m_c|>25/8,\quad m_c<0,\quad 63/64<j_c<65/64,\quad
 \|j_c'\|_\infty<1/16,\quad \|u_c\|_\infty<1/50,\\
 \|u_c'\|_\infty+\|v_c'\|_\infty<1/2,\qquad
 \|u_c''\|_\infty+\|v_c''\|_\infty<192 .
 \end{gathered}
 \tag{UH.3}
\]

The compact-to-repaired difference in
[PA.1--PA.2](R144-supplement-complete-positive-hybrid-adapter-for-compact-centres.md)
is degree32 and satisfies the complete pair bounds

\[
 \|Q_*-Q_c\|_{A^0,\mathrm{pair}}<3.848\,10^{-7},\qquad
 \|\partial_\phi(Q_*-Q_c)\|_{A^0,\mathrm{pair}}<1.020\,10^{-6}.
 \tag{UH.4}
\]

For a safe conversion to component sums use \(\sqrt2<2\).
Only this known difference uses the degree32 derivative factor128.
For \(Q=Q_*+q\), \(\|q\|_{A^3}\le10^{-6}\), its total displacement
from \(Q_c\) has value and first-derivative bounds

\[
 e_0<2\,10^{-6},\qquad e_1<4\,10^{-6},
\quad
 \|(Q-Q_c)''\|_{\infty,\oplus_1}
 <128(2.040\,10^{-6})+10^{-6}<.001 .
 \tag{UH.5}
\]

The last estimate is not a finite-support claim about \(q\).
Using
\(j-j_c=(\Delta v-j_c\Delta m)/m\) and
\(j'-j_c'=(\Delta v'-j_c'\Delta m)/m\), the full mean
\(\Delta m=\langle\Delta v\rangle\) gives all the bounds in (UH.7).

### The actual outer endpoint \(R=25/8\)

PA gives the exact identity \(Q_*(R)=Q_{\rm raw}(R)\), including the mean
and all angular derivatives. The existing complete raw endpoint theorem
[F.4, F.9--F.10](R133-supplement-final-moving-centre-actual-regular-boundary.md)
gives

\[
 \begin{gathered}
 -m_{\rm raw}>5.84461145233,\quad
 U_\sigma=1.643190\,10^{-9},\quad
 V_\sigma=9.603792\,10^{-9},\\
 \|u_{\rm raw}\|_{A^0}\le U_\sigma,\qquad
 \|v_{\rm raw}-m_{\rm raw}\|_{A^0}\le V_\sigma .
 \end{gathered}
 \tag{UH.6}
\]

The known raw field has degree32. Its first and second derivative
component sums are at most \(128(U_\sigma+V_\sigma)\) and
\(128^2(U_\sigma+V_\sigma)\). An unknown \(A^3\) perturbation of size
\(10^{-6}\) costs \(10^{-6}\) in each of these norms. This proves the
same following domain at \(R\). Neither the known spatial strip nor its
finite degree is assigned to the unknown perturbation.

At either endpoint, on the entire convex stated ball, one therefore has

\[
 \boxed{
 \begin{gathered}
 m<0,\quad v<0,\quad |m|>3,\quad |v|>3,\quad
 31/32<j=v/m<33/32,\quad \|j'\|_\infty<1/15,\\
 \|u\|_\infty<U:=21/1000,\quad
 \|u'\|_\infty+\|v'\|_\infty<P_1:=51/100,\quad
 \|u''\|_\infty+\|v''\|_\infty<P_2:=193 .
 \end{gathered}}
 \tag{UH.7}
\]

These are real full-circle bounds. They hold for full real pairs,
including variations of both moving means. The reflected subspace is
a permitted restriction, not a reason to delete a mean in the formulas.

## UH2. Complete angle variations and their uniform bounds

Keep the exact normalized chart of G:

\[
 m=\langle v\rangle,\quad j=v/m,\quad
 \Theta=\mathrm{id}+I(j-1),\quad
 \Phi=\Theta^{-1},\quad
 a(Q)=(u/v,1/v),\quad \Psi(Q)=a(Q)\circ\Phi .
 \tag{UH.8}
\]

For a moving direction \(h\) held fixed in \(\phi\), put
\(\mu_h=\langle h_2\rangle\), and denote

\[
 \ell_h=D\Theta[h]=m^{-1}I(h_2-j\mu_h),\qquad
 \xi_h=D\Phi[h]=-(\ell_h/j)\circ\Phi .
 \tag{UH.9}
\]

The primitive input has exactly zero mean. In particular (UH.9) includes
the changing scalar mean and the original angle normalization.

On this circle \(\|I:L^2\to L^\infty\|=\pi/(4\sqrt3)<1/2\), and
\(\|f\|_\infty\le2\|f\|_{H^1}\).
Since \(\|j-1\|_\infty<1/32\), (UH.7) gives

\[
 \|\ell_h\|_\infty\le\frac{11}{64}\|h_2\|_2,\quad
 \|\xi_h\|_\infty\le\frac{11}{62}\|h_2\|_2<\frac15\|h_2\|_2,
 \quad
 \|\ell_h'\|_\infty\le\frac{97}{96}\|h_2\|_{H^1}
                      <\frac{33}{32}\|h_2\|_{H^1}.
 \tag{UH.10}
\]

For the second direction \(k\),

\[
 \Theta_{hk}
   =-\frac{\mu_k}{m}\ell_h-\frac{\mu_h}{m}\ell_k,\qquad
 \|\Theta_{hk}\|_\infty
       \le\frac{11}{96}\|h_2\|_2\|k_2\|_2 .
 \tag{UH.11}
\]

Twice differentiating the same identity \(\Theta_Q\circ\Phi_Q=\mathrm{id}\)
gives, with all coefficients evaluated at \(\Phi\),

\[
 D^2\Phi[h,k]
 =-\frac{\Theta_{hk}+\ell_h'\xi_k+\ell_k'\xi_h
                         +j'\xi_h\xi_k}{j}.
 \tag{UH.12}
\]

This formula is symmetric in the two directions. It uses neither a
new angle constant nor an unweighted replacement of G's weighted
physical normalization.

Write \(T(h,k)=H(h)E(k)+H(k)E(h)\).
Using \(\|h_2\|_2\|k_2\|_2\le T(h,k)/2\), one obtains

\[
 \|D^2\Phi[h,k]\|_\infty
 \le \frac{32}{31}
       \left\{\frac{33}{160}
           +\frac12\left(\frac1{375}+\frac{11}{96}\right)\right\}T(h,k)
 <\frac13T(h,k).
 \tag{UH.13}
\]

All quantities in (UH.10)--(UH.13) include the full infinite direction.

## UH3. Ratios before composition

The exact first and second ratio differentials are

\[
 \begin{aligned}
 a_h&=(h_1/v-uh_2/v^2,\,-h_2/v^2),\\
 a_{hk}&=\left(-\frac{h_1k_2+k_1h_2}{v^2}
                    +\frac{2uh_2k_2}{v^3},
                         \frac{2h_2k_2}{v^3}\right).
 \end{aligned}
 \tag{UH.14}
\]

The signs of \(v\) in these identities remain their actual signs.
Only the estimates use \(|v|\).
From the full \(H^1\) embedding and
\(2\min(H(f)E(g),H(g)E(f))\le H(f)E(g)+H(g)E(f)\),

\[
 \|a_{hk}\|_{L^2\oplus_1L^2}\le\frac29T(h,k).
 \tag{UH.15}
\]

Indeed the mixed \(h_1k_2,k_1h_2\) products cost \(2/9\), and the
remaining product coefficient is
\(2(U+1)/27<2/9\). The derivative of the entire first ratio obeys

\[
 \|a_h'\|_{L^2\oplus_1L^2}\le\frac25H(h).
 \tag{UH.16}
\]

For clarity the coefficients of \(\|h_1\|_{H^1}\) and
\(\|h_2\|_{H^1}\) before widening are respectively bounded by

\[
 \frac13+\frac{P_1}{9},\qquad
 \frac{U+1}{9}+\frac{P_1}{9}+\frac{2(U+1)P_1}{27},
 \tag{UH.17}
\]

both below \(2/5\). No derivative of a direction has been hidden
inside a coefficient norm.

The background ratio derivatives are bounded in component-sum sup norm:

\[
 \|a'\|_{\infty,\oplus_1}<P_1/3=17/100,\qquad
 \|a''\|_{\infty,\oplus_1}
 <\frac{P_2}{3}+\frac{P_1^2}{18}
                      +\frac{2(U+1)P_1^2}{27}<65 .
 \tag{UH.18}
\]

For the second inequality use
\(|u'v'|\le(|u'|+|v'|)^2/4\).
The second derivatives of \(u,v\) have a **joint** sum bound, so their
largest ratio coefficient is \(1/3\); they do not each cost \(P_2/3\).

## UH4. The full Hessian and one-high-factor estimate

The actual change of variables gives

\[
 \|f\circ\Phi\|_{L^2_\theta}
 \le\sqrt{33/32}\|f\|_{L^2_\phi}
 <\frac{33}{32}\|f\|_2 .
 \tag{UH.19}
\]

For smooth directions the complete second chain rule is

\[
 D^2\Psi[h,k]
 =a_{hk}\circ\Phi
  +(a_h'\circ\Phi)\xi_k+(a_k'\circ\Phi)\xi_h
  +(a''\circ\Phi)\xi_h\xi_k
  +(a'\circ\Phi)D^2\Phi[h,k].
 \tag{UH.20}
\]

Together (UH.10), (UH.13), and (UH.15)--(UH.19) give the coefficient

\[
 \frac{33}{32}\left(\frac29+\frac{2}{25}\right)
          +\frac{65}{50}+\frac{17}{300}<2
 \tag{UH.21}
\]

in front of \(T(h,k)\). This proves (UH.1).

The map is twice differentiable from an open \(A^3\) domain into the
displayed physical \(L^2\) space. Smooth Fourier approximants to a
background converge in \(C^2\), their inverse lifts and the coefficients
in (UH.20) converge with the fixed positive gaps, and approximating
directions converge in \(H^1\). The estimates extend the Hessian to
every \(H^1\times H^1\) direction at each such background, with the same
constant. This does **not** assert a uniformly \(C^2\) chart on an open
rough \(H^1\) background ball.

For a convex path entirely in the stated \(A^3\) ball, set

\[
 \mathcal R_\Psi(h)=\Psi(Q_*+h)-\Psi(Q_*)-D\Psi(Q_*)h .
\]

The complete Taylor integral gives the concrete low-norm bounds

\[
 \boxed{\ \|\mathcal R_\Psi(h)\|_{L^2_\theta\oplus_1L^2_\theta}
                    \le2H(h)E(h).\ }
 \tag{UH.22}
\]

For two such perturbations, \(H(h),H(k)\le\rho_1\),

\[
 \boxed{\ \|\mathcal R_\Psi(h)-\mathcal R_\Psi(k)\|
                      \le4\rho_1H(h-k).\ }
 \tag{UH.23}
\]

To prove (UH.23), use the line segment \(z=k+t(h-k)\), subtract
\(D\Psi(Q_*)\), integrate the Hessian along \(Q_*+sz\), and use
\(H(z),E(z)\le\rho_1\).
Every path stays in the same \(A^3\) background ball by convexity.
There is no assertion that the condition \(H(h)\le\rho_1\) alone supplies
that \(A^3\) background qualification.

## UH5. Both physical means and the exact endpoint use

The complete identities, before any reflection restriction, are

\[
 \langle B_Q\rangle_\theta=\frac{\langle u\rangle_\phi}{m},
 \qquad \langle C_Q\rangle_\theta=\frac1m .
 \tag{UH.24}
\]

Consequently the two Hessian mean rows are exactly

\[
 \begin{aligned}
 \langle(D^2\Psi[h,k])_B\rangle_\theta
   &=-\frac{\langle h_1\rangle\mu_k+\langle k_1\rangle\mu_h}{m^2}
       +\frac{2\langle u\rangle\mu_h\mu_k}{m^3},\\
 \langle(D^2\Psi[h,k])_C\rangle_\theta
   &=\frac{2\mu_h\mu_k}{m^3}.
 \end{aligned}
 \tag{UH.25}
\]

In particular the second mean has absolute value at most
\(2|\mu_h\mu_k|/27\), and is generally nonzero.
The first mean vanishes in the exact original reflection sector for its
actual parity reason. No independent mean is removed from the full chart.

At either endpoint a specified bounded **fixed** physical observation
operator \(\mathcal O\) can consume (UH.1), (UH.22), (UH.23) with its own
complete operator norm. A nonlinear DN observation instead also needs
its full first and second differential, independent height derivatives,
and scalar mean output. These terms cannot be paid by the chart estimate
alone. Moving low193, weighted \(S_i\), physical low96, and complete
mean outputs must still use their own original observation maps.

The propagated radial phase of G.17--G.20 has not been reset or removed.
The present normalized endpoint chart does not identify it with the
geometric PD phase row. Likewise no height equation, holonomy equation,
true parameter Schur, low/high inverse, residual-in-ball gate, or final
geometric conclusion follows just from this Hessian.

The companion
[saved rational reader](../scripts/fourfold_codazzi_compact_uniform_physical_chart_saved_bounds.py)
checks only the displayed positive combinations of completed CH, PA,
and raw-endpoint bounds. No old rows, integrals, native numerical
producer, DFT, trial, or scientific norm target is recomputed.
