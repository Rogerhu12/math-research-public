# R144 GHR: the actual seed metric reference-height and complete endpoint column

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all 17 new exact rational and integer comparisons pass.**
For the complete actual second-parameter direction
\(\mathfrak a\in{\cal P}_2\), including its radial first compensation and
the whole selected first-principal response, the independent reference-height
column satisfies
\[
 \|H_{\rm met}[\mathfrak a]\|_{C^2_r}
       \le \rho\varepsilon_s\,2^{1024}\|\mathfrak a\|_{{\cal P}_2}.
\]
The norm includes the whole original infinite tail, its flat-end extension,
and the same constant-height continuation through the finite connector.
The original two endpoint heights and the true conormal column remain
outputs. In particular the actual seed's gamma direction obeys
\[
 \|H_{\rm met}[D_\gamma\mathfrak q(\gamma)\eta]\|_{C^2_r}
   <\rho\varepsilon_s\,2^{1024-110000000}
                      r_\gamma^{-1}\|\eta\|_{A^0}.
\]
This is the metric reference-height column, with its reference \(1\).
It is separate from the endpoint-graph height column and the independent
rigid height parameter. It is not a vanishing ordinary-source estimate.

## 1. The same physical object and the exact column

Use the completed actual objects and conventions of:

- [GF: complete actual parameter forcing](R144-supplement-complete-parameter-forcing-for-the-selected-exact-tail-family.md), especially GF.4, GF.15--GF.19 and GF.24;
- [GA: complete mixed A0 parameter forcing](R144-supplement-separated-end-A0-parameter-forcing-with-complete-mixed-height.md), especially its full principal operator continuity;
- [T: the actual selected family](R119-supplement-continuous-exact-tail-selection-and-true-second-phase-response.md), especially T.C.5--T.C.14;
- [Mhol: the true holonomy mean and height chart](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md), especially M.1--M.14 and M.28--M.36;
- [G: the complete metric mean and reference-height column](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md), especially G.12--G.14 and G.28--G.29;
- [E: the original graph and actual radial jets](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md), especially E.3, E.13, E.18 and E.22;
- [Qmet: exact ordinary sources and reference-height lifts](R119-supplement-exact-nonlinear-ordinary-sources-and-Gamma-reference-height-lifts.md), especially Q.19--Q.24c.

The real physical object, material coordinate \(r\), scale \(\rho\), shape,
fixed stop, and original \(\Omega\) are fixed. Only the actual two metric
parameters vary. All the changes are the original compact radial bumps.
The exterior component \(o=(129,2)\) is the second descending slope in
the original cell 129, as specified in G section 6. It is not a bump in
the newly added finite connector.

Use the true S/T family at a fixed physical nonmean \(w\), on
\[
 \|w\|_{E_{1856}^+}\le2^{-49000000},\qquad
 \gamma\in{\cal D}_\gamma,\qquad r_\gamma=10^{-9}.
\]
Write \(u={\cal U}_\gamma w\). The positive B-collar lift is zero on
the entire metric-bump region and on every principal input domain.
Thus the same actual principal map is evaluated at \(u\) and at \(w\)
there, for every admitted second parameter.

For \(\mathfrak a\in{\cal P}_2\), put
\[
 \tau=\|\mathfrak a\|_{{\cal P}_2},\qquad
 \psi=D_{\mathfrak q}\log w_{\rm metric}(u,\mathfrak q)
                                             [\mathfrak a].
                                                               \tag{GHR.1}
\]
The derivative in (GHR.1) is GF's complete one. It includes the actual
radial first compensation and the full inverse
\((I-D_pT)^{-1}\); it is not the derivative of an uncompensated second
bump.

At a fixed physical nonmean height, the actual mean variation is
\[
 \dot\kappa=
 \frac{\psi D_{(P,K_\perp)}\Phi_q[P,K_\perp]
                      -2q\psi\,\partial_q\Phi_q}
      {\langle A_W\rangle},\qquad
 A_W=JD^{-3/2}.                                                \tag{GHR.2}
\]
Every derivative here uses Mhol's removable holonomy quotient and its
same small root. The denominator is \(>3/4\), without division by a
small \(q=w_{\rm metric}^2\).

Define the single directed height integral
\[
 \begin{split}
 (H_{\rm met})_t
   &=a_{\rm ph}w_{\rm metric}
                    \{\psi(1+\kappa)+\dot\kappa\},\\
 H_{\rm met}(t)
   &=\int_{t_f}^t a_{\rm ph}(s)w_{\rm metric}(s)
                    \{\psi(1+\kappa)+\dot\kappa\}(s)\,ds,
 \qquad H_{\rm met}(t_f)=0 .
 \end{split}                                                   \tag{GHR.3}
\]
This is exactly G.14/GF.24. The reference \(1\) in (GHR.3) remains
present even at zero nonmean state. A separately varied rigid height
adds its one independent scalar constant to (GHR.3).

## 2. Actual radial mean derivatives, rather than differentiation of a value bound

Let \(Z=(P,K_\perp,U,V)\), with the original derivative constraints,
and \(n=\|Z\|_{H^2}\). Define the analytic scalar function
\[
 {\cal L}(Z,q)=\kappa+
 \frac{D_{(P,K_\perp)}\Phi_q[P,K_\perp]
                   -2q\partial_q\Phi_q}{\langle A_W\rangle}.
\]
Then, including at points where \(\psi=0\),
\[
 \psi\kappa+\dot\kappa=\psi{\cal L},\qquad
 (H_{\rm met})_t=a_{\rm ph}w_{\rm metric}\psi(1+{\cal L}).
                                                               \tag{GHR.4}
\]
G.13's complete algebra gives
\(|{\cal L}|\le2^{16}n^2\). The same absolute rational and binomial
series in Mhol.8 are valid for complex \(|q|<1/4\) and sufficiently
small complex \(Z\), with the same nonzero mean denominator.
Moreover \({\cal L}(0,q)=D_Z{\cal L}(0,q)=0\).

We spell out the derivative that will be used. The actual
\(q<2^{-1062}\): Mhol.3 gives
\(w_{\rm metric}<2^{129}\varepsilon_s\delta_{129}^5
<2^{-531}\) at the largest layer, and its two subsequent profile
pieces decrease. Thus a complex \(q\) circle of radius \(1/8\)
about the actual \(q\) is within the preceding algebraic domain.

At an actual \(Z\) of norm \(n\), use a complex direction circle of
radius \(n\) in the normalized \(Z\) direction. Its points have norm
at most \(2n\), strictly inside the same small-root domain. Cauchy
applied to the stated quadratic bound gives
\(\|D_Z{\cal L}\|\le2^{18}n\).
The independent \(q\) circle gives
\(|\partial_q{\cal L}|\le2^{19}n^2\).
At \(n=0\) the assertion follows from the exact double zero.
Consequently the actual radial derivative obeys
\[
 |{\cal L}_t|
 \le2^{24}\{n\|Z_t\|_{H^2}+(1+|A|)n^2\},
 \qquad A=(\log w_{\rm metric})_t .                            \tag{GHR.5}
\]
This is differentiation of the actual analytic small-root formula
on a specified function-parameter domain. It does not infer a
radial derivative from a small real value alone, and it assumes no
spatial analytic strip.

Here is the uniform actual radial-jet budget. GF.11, the fixed-reference
comparison, and E.22 allow
\[
 \max\{n,\ell_j\|Z_t\|_{H^2}\}\le C_j R,\qquad
 R=2^{-47000000},\qquad
 \ell_j=2^{-64}J_j^{-2}\delta_j^4 .                            \tag{GHR.6}
\]
The factor 16 in E.22 and the common-reference comparison fit well
inside \(-48000000+5<-47000000\). The input is a true graph member,
so the radial derivative in (GHR.6) is one of its already required
ordinary broken jets. No raw \(L^2_r\) trace is used.

Recall the exact layer formula
\(C_j=2^{200}h_j^{-5}(\zeta_j/\mu_j)\delta_j^{-2}\).
By Mhol.1, \(\zeta_j/\mu_j\le1\) on the entire original profile.
Thus
\[
 \begin{split}
 C_j^2\ell_j^{-1}
 &=2^{464}J_j^2h_j^{-10}
                   (\zeta_j/\mu_j)^2\delta_j^{-8}\\
 &\le2^{464}J_j^3h_j^{-10}
                   (\zeta_j/\mu_j)\delta_j^{-57/2}
 <2^{262608}.
 \end{split}                                                   \tag{GHR.7}
\]
The last inequality is T.C.13's complete finite-prefix and deep-tail
bound, with both profile junctions retained.
The original \(1+|A|\le2^{13}J_j\delta_j^{-3/2}\) is smaller than
\(\ell_j^{-1}\). Equations (GHR.5)--(GHR.7) give
\[
 |{\cal L}|<1/4,\qquad
 |{\cal L}_t|
      \le2^{25}C_j^2\ell_j^{-1}R^2
      <2^{262633-94000000}<1/4.                              \tag{GHR.8}
\]
This estimate uses the complete radial jets of the background and
the exact small-root derivative. It is valid off shell on the
stated holonomy-one graph; no equation \(K_t=F\) was assumed.

## 3. Whole two-parameter bump profile, including the actual shallow exception

GF.19 supplies, for the internal components, the actual support sum
\[
 g_j\le2^{64}J_j^3\delta_j^{-5}C_j^\#\tau,\qquad
 |\psi|\le g_j,\qquad
 |\psi_t|\le2^{64}\delta_j^{-3/2}g_j .                         \tag{GHR.9}
\]
The full six-neighbor \(C_j^\#<2^{256}C_j\) is used. This is the
completed scalar metric profile after the first-principal feedback
has been retained and absorbed in its actual low-state margin.

The separate \(o\) contribution has
\[
                  g_{129,o}\le2^{14}\tau .                   \tag{GHR.10}
\]
It uses the actual finite bump polynomial in the original cell 129;
its first derivative satisfies the same ordinary bump bound in
(GHR.9). It has not been replaced by an internal weight containing
a nonexistent small \(C_{129}\) factor.

All these bumps have their original support endpoints and zero
jets of orders 0, 1, and 2 there. The root germs and fixed stop do
not move. No derivative jump beyond the original broken convention
is silently removed.

## 4. Two material derivatives and the full directed integral

On every original cell,
\[
 1\le r\le2,\qquad
 a_{\rm ph}w_{\rm metric}\le\rho\,2^{130}\mu_j\delta_j^{-1},
 \qquad |I_j|_t<4\delta_j.
\]
Use (GHR.4) and (GHR.8), keeping
\((a_{\rm ph}w_{\rm metric})_t=(1+A)a_{\rm ph}w_{\rm metric}\).
The three contributions to the second derivative are
\[
 (H_{\rm met})_{tt}
 =a_{\rm ph}w_{\rm metric}
 \{(1+A)\psi(1+{\cal L})
          +\psi_t(1+{\cal L})+\psi{\cal L}_t\}.
                                                               \tag{GHR.11}
\]
In particular the derivative of the mean feedback has been paid.
Equations (GHR.8)--(GHR.11) give the convenient bounds
\[
 \begin{split}
 |(H_{\rm met})_t|
       &\le\rho\,2^{131}\mu_j\delta_j^{-1}g_j,\\
 |(H_{\rm met})_r|+|(H_{\rm met})_{rr}|
       &\le\rho\,2^{198}J_j\mu_j\delta_j^{-5/2}g_j,\\
 \int_{I_j}|(H_{\rm met})_t|\,dt
       &\le\rho\,2^{133}\mu_jg_j .
 \end{split}                                                   \tag{GHR.12}
\]
For the second line,
\(H_r=H_t/r\) and \(H_{rr}=(H_{tt}-H_t)/r^2\);
the displayed coefficient includes both terms.

Inserting (GHR.9) and the full neighbor factor yields
\[
 \begin{split}
 |H_r|+|H_{rr}|
 &\le\rho\,2^{718}
          J_j^4h_j^{-5}\zeta_j\delta_j^{-19/2}\tau,\\
 \int_{I_j}|H_t|\,dt
 &\le\rho\,2^{653}
          J_j^3h_j^{-5}\zeta_j\delta_j^{-7}\tau .
 \end{split}                                                   \tag{GHR.13}
\]
These estimates are in material \(r\), with the actual physical
height scale \(\rho\) retained. The second line will be summed
before any endpoint height is read.

## 5. The finite prefix, both junctions, and infinite tail

Here are complete bounds for the two profiles in (GHR.13):
\[
 \begin{split}
 \sup_{j\ge129}
  J_j^4h_j^{-5}\zeta_j\delta_j^{-19/2}
                  &<2^{20}\varepsilon_s,\\
 \sum_{j\ge129}
  J_j^3h_j^{-5}\zeta_j\delta_j^{-7}
                  &<2^{-300}\varepsilon_s .
 \end{split}                                                   \tag{GHR.14}
\]
We give the actual three-piece argument, so these statements do
not substitute a deep asymptotic formula for the prefix.

Through \(j=4096\), \(h=9/100\) and
\(\zeta_j=\varepsilon_s\delta_j^{39/4}\).
At \(j=129\), \(J_j<2^8\), \(h^{-5}<2^{18}\), and
\(\delta_j<2^{-132}\).
The first profile is therefore \(<2^{17}\varepsilon_s\);
the second is \(<2^{-321}\varepsilon_s\).

For every later layer the polynomial ratio is at most
\((135/134)^4<2^{1/8}\), since
\(135^{32}<2\cdot134^{32}\).
The first profile in this shallow range has power \(\delta^{1/4}\),
so it decreases. The second has power \(\delta^{11/4}\),
so its consecutive ratio is \(<1/4\).

At the change to \(h_j=8\delta_j^{1/256}\), the actual jump in
\(h_j^{-5}\) is less than \(2^{50}\), as already included in Qmet.
Use \(J_{4096}<2^{13}\) and
\(\delta_{4096}<2^{-4099}\).
For the first profile, including the next layer's polynomial
ratio and this full jump, the exponent is less than
\[
             52+18-4099/4+50+1<-900 .
\]
For the second it is less than
\[
             39+18-11\cdot4099/4+50+1<-11160 .
\]
Thus this junction does not approach either displayed budget.

In the middle range the first profile has positive power
\(\delta^{1/4-5/256}\), and
\(1/4-5/256=59/256>1/8\), so it decreases despite the polynomial.
The second still has consecutive ratio \(<1/4\).
At \(j=8192\) the exact normalization of \(\zeta_j\) is continuous;
after that point the first profile has exponent
\(131-19/2-5/256=121+123/256>121\), and the second has exponent
\(124-5/256\). Both are strictly positive and decrease with
ample margin.

Summing the shallow geometric sequence and the entire sequence
after the first junction gives respectively bounds
\(2^{-320}\varepsilon_s\) and
\(2^{-11160}\varepsilon_s\), whose sum is below
\(2^{-319}\varepsilon_s<2^{-300}\varepsilon_s\).
This proves (GHR.14) with both normalization factors retained.

For the separate \(o\) contribution, \(\mu_{129}
=\varepsilon_s\delta_{129}^{6}\) and (GHR.10) apply directly:
\[
 \begin{split}
 |(H_o)_r|+|(H_o)_{rr}|
   &<\rho\varepsilon_s2^{198+14+8-7\cdot132/2}\tau
     =\rho\varepsilon_s2^{-242}\tau,\\
 \int |(H_o)_t|\,dt
   &<\rho\varepsilon_s2^{133+14-6\cdot132}\tau
     =\rho\varepsilon_s2^{-645}\tau .
 \end{split}                                                   \tag{GHR.15}
\]
This is the actual finite shallow exception, not an assignment of
a deep index to it.

Combining (GHR.13)--(GHR.15), and summing the single directed
integral from the flat end, gives
\[
 \boxed{\qquad
 \|H_{\rm met}[\mathfrak a]\|_{C^2_r}
   \le\rho\varepsilon_s\,2^{1024}\tau .
 \qquad}                                                       \tag{GHR.16}
\]
The internal derivative budget is \(2^{738}\); the integral budget
is \(2^{353}\). Even after the component sum and the shallow
exception, fewer than 743 bits suffice. The displayed 1024-bit
bound is a conservative common bound, not a newly computed profile.

The deep exponents in (GHR.13) are positive, and the directed
integral tail tends to zero. Thus the height and its first two
material derivatives extend continuously to the original flat end.
The zero bump jets retain the true matching at every original
support endpoint and root germ.

## 6. Both heights, conormal units, and the finite continuation

The actual complete conormal column is
\[
 \pi_{H_{\rm met}}
    =w_{\rm metric}^2 A_W
                     \{\psi(1+\kappa)+\dot\kappa\}.
                                                               \tag{GHR.17}
\]
Both \(H_{\rm met}(t_{\rm left})\) and
\(H_{\rm met}(t_{\rm right})\) are the values of (GHR.3) at the
original material endpoints. They are not reset independently.
Where an endpoint lies outside all bump supports, (GHR.17)
vanishes there, but the height in (GHR.3) can be a nonzero
constant. At an endpoint inside a support the complete formula
(GHR.17) must be used.

The finite connector has no varying design bump. The column
there is the same constant inherited from the original cell 129,
so its derivatives vanish while its value remains in the
matching data. No new source or arbitrary boundary condition is
introduced by this continuation.

Formula (GHR.17) is the original conormal of the height column.
It is not substituted for the nonlinear holonomy charge, which
has its own exact variation. The ordinary source of GF/GA and the
height column (GHR.3) are complementary parts of the same metric
direction.

For the original physical Cartesian height readout, retain the
already paid conversion factor:
\[
 \|H_{\rm met}[\mathfrak a]\|_{C^2_{\rm Cartesian}}
 \le\rho\varepsilon_s\,2^{1032}
          \max(1,\rho^{-2})\tau .                             \tag{GHR.18}
\]
The physical scale is explicit. This is the scalar height column;
it does not by itself replace the complete coframe, spatial frame,
or position reconstruction.

## 7. Actual gamma direction and joint operator continuity

T.C.9 supplies the true direction
\[
 \mathfrak a=D_\gamma\mathfrak q(\gamma)[\eta],\qquad
 \tau<2^{-110000000}r_\gamma^{-1}\|\eta\|_{A^0}.
\]
Therefore
\[
 \boxed{\qquad
 \|H_{\rm met}[D_\gamma\mathfrak q(\gamma)\eta]\|_{C^2_r}
 <\rho\varepsilon_s\,2^{1024-110000000}
                       r_\gamma^{-1}\|\eta\|_{A^0}.
 \qquad}                                                       \tag{GHR.19}
\]
The same estimate with the conversion factor in (GHR.18) gives
the physical Cartesian scalar-height bound.

This operator is jointly continuous in gamma with its relative
\(A^0\) topology and in the nonmean background with its common
\(E_{20}^+\) topology, restricted to the stated value domain.
On a fixed finite set of original cells, the complete principal
operator continuity of GA section 6, the actual polynomial
bumps, the holonomy small-root formula, and the genuine first
radial graph jet prove continuity in the displayed \(C^2_r\)
norm. The directed height integral has the same property.

For the infinite remainder, the two actual profiles in (GHR.13)
tend to zero uniformly, including the tails of their directed
integrals. The complete \({\cal P}_2\)-operator bound is uniform,
not merely a statement for one coordinate direction.
Finite-prefix continuity plus these uniform tails proves
continuity in the whole operator norm. The true seed derivative
is itself continuous \(A^0\to{\cal P}_2\) by T.C.3--T.C.9.
No density of Fourier polynomials in a whole-layer supremum
space is required.

The full partial gamma derivative of the mean height also has
the separate endpoint-graph contribution caused by
\(D_\gamma{\cal U}_\gamma(w)\), and any separately varied rigid
height contributes its scalar derivative. Those are not deleted
or included in (GHR.19). The present result pays the independent
metric reference column which cannot be charged to a source
bound proportional to the nonmean state.

## 8. New exact saved-bound combinations

The companion
[fourfold_codazzi_seed_metric_height_saved_bounds.py](../scripts/fourfold_codazzi_seed_metric_height_saved_bounds.py)
contains 17 new comparisons of the completed GF/T/Mhol/E/G constants.
Their first execution used exact BigInt for the polynomial ratio
and exact integer or dyadic-rational exponents in code mode after
the local environment became unavailable. All 17 passed. The
Python reader records those same comparisons with Fraction.

No prior native arrays, scientific integrations, old target
values, or earlier saved-bound comparisons were rerun. The
proof preserves both original profile junctions, the actual
shallow exception, the independent height gauge, the reference
\(1\), and all original endpoint units.
