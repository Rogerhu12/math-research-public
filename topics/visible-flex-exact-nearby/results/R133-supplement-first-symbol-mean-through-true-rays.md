# R133 supplement: the first-symbol mean through the true rays

2026-11-14, visible-exact-astra-0df / phase_inverse. **Proved.**

This closes the scalar transport part of
[the current complete first-symbol theorem](R133-supplement-complete-moving-first-symbol-and-root-subtractions.md).
On every strict negative segment, its first-symbol mean can be
integrated in the original moving angle. Recomputing the true ray
maps is unnecessary for that mean. The full nonmean coefficient,
root matching, positive-port reflection and quantitative strong
remainder remain separate terms in the full equation.

The object, complete primitive, mean states, continuous-centre
definition and physical Fourier factor four are unchanged. In this
note \(\Pi\) is normalized angular averaging and
\(I=\partial_\phi^{-1}(1-\Pi)\).

## 1. Complete primitive covariance, including the mean columns

Let \(\Phi(x)=x+p(x)\) be any smooth orientation-preserving
degree-one lift on the period \(\pi/2\). Define

\[
 C_\Phi f=f\circ\Phi,\qquad
 U_\Phi=M_{\Phi'}C_\Phi.
 \tag{M.1}
\]

The exact identity is

\[
 \boxed{\ I U_\Phi
   =C_\Phi I+(p-\Pi p)\Pi-\Pi C_\Phi I.\ }
 \tag{M.2}
\]

To prove it, differentiate both sides. Since
\(\Pi U_\Phi f=\Pi f\), the left derivative is
\(U_\Phi f-\Pi f\); the derivative of \(C_\Phi If\) is
\(U_\Phi f-\Phi'\Pi f\). The derivative of the middle term
supplies \((\Phi'-1)\Pi f\). Both sides have mean zero by the
last term. This proves the identity on every mode, including mean.

In particular a shorthand that retains only \(C_\Phi I\) is
incorrect on the full space. The two remaining finite-rank maps in
(M.2) stay in the original mean/low equations. Their smooth output
columns make them smoothing on any fixed finite Sobolev window,
with their genuine coefficient bounds; this does not set them to
zero.

For a multiplier \(a\), (M.2) gives

\[
 U_\Phi M_a I U_\Phi^{-1}
       =M_{\Phi'(a\circ\Phi)}I+\mathcal F_\Phi,
 \tag{M.3}
\]

where \(\mathcal F_\Phi\) is the corresponding complete smooth
finite-rank map. Equivalently, conjugating in the inverse direction
gives first coefficient
\((a/\Phi')\circ\Phi^{-1}\). The exact change of variables proves

\[
 \boxed{\ \Pi[\Phi'(a\circ\Phi)]=\Pi a,\qquad
 \Pi[(a/\Phi')\circ\Phi^{-1}]=\Pi a.\ }
 \tag{M.4}
\]

These identities do not require \(\Phi\) to be near the identity,
radial or a trigonometric polynomial. They therefore apply to the
true flows and the genuine final circle conjugacy, on their already
paid domains.

## 2. The complete strict scalar accumulation

After the exact primitive and cross-wave changes of the preceding
theorem, one branch has generator, modulo its retained order-minus-two
and mean terms,

\[
 c_\sigma\partial_\phi+(c_\sigma)_\phi+\ell+a_\sigma I,
 \quad \ell=-2R_0/m,
 \tag{M.5}
\]

with

\[
 a_\sigma=-d_{\phi\phi}
    -b(r_\sigma)_\phi r_{-\sigma}
          +\frac{\sigma B_+B_-}{2\eta q}.
 \tag{M.6}
\]

Let \(H_\sigma\) be the true ray
\(H_{\sigma,r}=-c_\sigma\circ H_\sigma\), and
\(J_\sigma=H_\sigma'>0\). The exact density change
\(X_\sigma=J_\sigma y_\sigma\circ H_\sigma\) cancels the first
two terms in (M.5). The remaining first coefficient is
\(J_\sigma(a_\sigma\circ H_\sigma)\), by (M.3).
Its mean is exactly \(\Pi a_\sigma\), by (M.4).

The common radial factor \(\ell\) can be removed by
\(X_\sigma=\exp(\int\ell)\widetilde X_\sigma\); it commutes
with \(I\) and every angular multiplier. This is an actual radial
state and source rescaling. Its endpoint factors and costs remain
in the complete port problem.

The first chronological term of the remaining propagator is

\[
 M_{\int J_\sigma(a_\sigma\circ H_\sigma)\,dr}\,I.
 \tag{M.7}
\]

The next chronological products contain at least two complete
inverse derivatives and therefore enter the strict order-minus-two
remainder. Thus the exact first scalar mean of a directed strict
leg is

\[
                         \int \Pi a_\sigma\,dr.
 \tag{M.8}
\]

Inverting a directed leg reverses that first coefficient. Composing
successive legs adds them after density coordinate changes, and
(M.4) preserves their means. Therefore a strict forward plus leg
followed by a strict inverse minus leg has signed mean

\[
 \int\Pi(a_+-a_-)\,dr
   =\int\left\langle
       \frac{B_+B_-}{\eta q}
                 -2bq(uv_\phi-vu_\phi)\right\rangle dr
   =\int\langle\Xi\rangle dr.
 \tag{M.9}
\]

The opposite ordering has the opposite sign. This statement fixes
the sign for the specified directed word; it does not assert which
root/positive-cap returned row has already been matched to that
word. Since \(Ie^{4ij\phi}=(4ij)^{-1}e^{4ij\phi}\), the
strict phase contribution for that word has scalar coefficient
\(-\tfrac14\int\langle\Xi\rangle dr\) in front of \(1/j\).

## 3. The half-density change does not alter that scalar

The unitary half-density principal generator is
\(c\partial_\phi+c_\phi/2\). On either nonzero sign cone,
conjugating the density generator by \(|D_\phi|^{-1/2}\) gives

\[
 |D_\phi|^{-1/2}(c\partial_\phi+c_\phi)|D_\phi|^{1/2}
  =c\partial_\phi+\frac12c_\phi
                 -\frac18c_{\phi\phi}I+\mathcal R_{-2}.
 \tag{M.10}
\]

Here is a full-symbol check with unambiguous signs. For same-sign
physical frequencies \(k,n\), the original matrix after conjugation
is \(ik\sqrt{|n|/|k|}\,\widehat c(k-n)\). For positive frequencies
its coefficient is \(i\sqrt{kn}\). The expansion

\[
 \sqrt{kn}=n+\frac{k-n}{2}
                      -\frac{(k-n)^2}{8n}
                      +O\!\left(\frac{|k-n|^3}{n^2}\right)
 \tag{M.11}
\]

on \(|k-n|\le |n|/2\) proves (M.10); the negative cone gives
the same operator formula. On the complementary frequency region
the full smooth coefficient bounds absorb the frequency ratios.
Summing the weighted Fourier kernel gives two complete angular
gains on any fixed finite Sobolev window. All opposite-cone and
finite low/mean maps are retained. This is an order statement;
the numerical strong constant is still to be evaluated.

Conjugation of an already order-minus-one term \(M_aI\) changes
its leading coefficient only at order minus two. The additional
coefficient in (M.10) has exact mean zero. More strongly, the two
current speeds satisfy
\((c_+)_{\phi\phi}=(c_-)_{\phi\phi}=d_{\phi\phi}\), so it
cancels even before averaging their signed difference.
Together with the primitive contribution \(-d_{\phi\phi}I\)
in (M.6), this is the \(-9d_{\phi\phi}/8\) obtained by directly
conjugating the quadratic density by \(|D_\phi|^{-3/2}\).
The two routes give the same scalar in (M.9).

## 4. The precise remaining identification

The finite-part consumer may consequently compute the scalar
ingredient (M.9) using complete Eulerian Fourier moments. It does
not need approximate or recomputed ray values for that mean.
The true rays remain necessary for the nonmean first coefficient
and its quantitative normalization.

The two-line Airy matching must still establish the endpoint
normalizers, exact finite-part convention, amplitude and Maslov
row. The current regular positive graph and all retained mean/head
columns must then be attached in the same directed word. Only
after those steps can the scaled integral be identified with the
first scalar coefficient of the full returned operator. No old
radial or reciprocal-centre phase value is imported by this mean
invariance argument.
