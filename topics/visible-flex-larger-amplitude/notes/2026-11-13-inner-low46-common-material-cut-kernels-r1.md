# Complete low46 true-cut kernels for the original common physical material

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## 1. Original saved kernel and exact source units

This certificate extracts the raw base integrals already computed in
all46 original R82 mode files, on every source cell12 through224.
The original complete archive has SHA
`9b2971944041c2964bfee1cc9d1d7fa40e5392f28b401a9c2ace22618e681a1a`.
It pins every source file and formal resource result. All46 original
owned runs had exit0; the present extractor verifies those bytes,
all source and mode coverage, the identical continuous q strip,
the same10 main dependency identities, all12 shallow panel providers
and all6 actual normalized linear column groups.

The raw R82 field `phi_source_integrals.base` is R63's
\(I^B_{n,m}\). Its material is

\[
 d_s(r)=\frac{V_s(r)^2}{r w(r)}+
        \left|\frac{w_r(r)}{w(r)}\right|\frac{V_s(r)^2}{w(r)}.
\tag{1}
\]

The source-to-canonical factor is \(r^4w/(\sqrt{12}\mu_n)\), so

\[
 I^B_{n,m}\ge\int_{I_n}
 |\Phi_{Q,m}(r)|e^{-m\tau(r)}
 \frac{r^4w(r)}{\sqrt{12}\mu_n}\,d_s(r)\,dr.
\tag{2}
\]

Here \(\Phi_{Q,m}(b)=1\), and \(\tau(r)\) is the original continuous
q strip. R82's producer constructs (2) with a coefficient exactly1
for its `base` material. In the shallow cells it intersects its
complete whole-cell bound with the already paid ordered source-panel
bound after the explicit strong-envelope scaling. No quadratic
constant, reference-strip spectral gain or auxiliary source cap is
included in this saved base integral.

Let \(V'=S V_s\), \(S=257/256\). The new common material is
\(d'=S^2d_s\). The extractor pays this factor \(S^2\) exactly once.
The input coefficient \(a_{n,m}\) must bound the complete weak
signed-pair source mass in this material:

\[
 a_{n,m}\ge\sum_{j\in\{-m,m\}}
 \sup_{r\in I_n}\frac{e^{m\tau(r)}|f_j(r)|}{d'(r)}.
\tag{3}
\]

The physical source is in the equation for
\(\kappa_\perp\). In the notation of R106 it is \(w\mathcal N\),
not \(\mathcal N\) itself. In particular (1) has one division by w.

## 2. Accurate true-cut Wronskian conversion

R63 (63.4) applies to the source response with zero shallow
Dirichlet datum and the original linear far condition:

\[
 e_{\Xi_{12},m}(b)=\pm\sum_{n=12}^{224}
 \frac{\mu_n}{\mu_{12}}\int_{I_n}\Phi_{Q,m}F_{n,m}\,dr.
\tag{4}
\]

The sign does not affect the positive upper kernel. All changes of
canonical cell frame are contained in \(\mu_n/\mu_{12}\). They are
not additional independent jumps to be paid again.

At the shallow endpoint the source response has \(e_Q(b)=0\),
so its physical p component vanishes and

\[
 \frac{e_{\kappa_\perp,m}(b)}{w_b}
   =\frac{\sqrt{12}\mu_{12}}{b^4w_b^2}
       e_{\Xi_{12},m}(b).
\tag{5}
\]

The original saved `point_cut_K_conversion` is a positive upper
bound for the factor in (5), using the accurate inner \(\mu_{12}\),
true physical b, and true w. The extractor checks its equality across
all46 mode files and that it dominates a fresh256-bit evaluation
using those same certified endpoint bounds. This is a small algebraic
check, with no new geometric integration.

Writing \(c_b\) for that saved conversion upper bound, the delivered
raw paired coefficient is

\[
 K_{n,m}=S^2c_b\left(\frac{\mu_n}{\mu_{12}}\right)_+
                 I^B_{n,m}.
\tag{6}
\]

It gives
\(\sum_{j=\pm m}|e_{\kappa_\perp,j}/w_b|
 \le\sum_n K_{n,m}a_{n,m}\).
A real cosine or sine amplitude is the sum of its two complex half
amplitudes, so neither (3) nor (6) requires an extra factor2.

The two saved strong output columns are

\[
 K^\sigma_{n,m}=(1+m)e^{m\sigma}K_{n,m},\quad\sigma=1/64,
\]

\[
 K^b_{n,m}=(1+m)e^{m\tau_b}K_{n,m}.
\tag{7}
\]

The primary records the accurate original \(\tau_b\), not a rounded
display value. The source norm in all three columns is unchanged:
it is still measured at the original continuous \(\tau(r)\).

## 3. Shared masses and complete-source obligation

The rows of the primary are indexed by cell12..224; each of
`Kbar_pair_upper`, `W_sigma1_upper`, and `W_head1_upper` has46 entries
in the separately saved mode order2,4,...,92. The original base
integral and mu ratio are also retained for every entry.

If the cell input is one shared low46 mass
\(\sum_m a_{n,m}\le A_n\), a valid total-output coefficient is
\(\max_m K_{n,m}\) (or the corresponding strong column). It is not
\(\sum_mK_{n,m}\), which corresponds to independently spending a
unit input at every frequency. Both aggregates are saved with these
separate meanings. More precise per-mode caps may be intersected
with the common mass by a positive support calculation.

If a source is split into two physical materials, a common bound for
(3) must be established coefficientwise before the radial supremum
and mode sum. Taking a maximum of two unrelated total material masses
would not establish that bound. For the newly extracted DQ kernels,
the separately proved inequality \(\beta_\ell\le\beta_s\) supplies
such a common positive convolution majorant; for complete quadratic
and higher remainder terms their original complete common-source
bounds must still be used.

The kernel is linear and independent of the particular auxiliary
source used in R82. It can therefore read the complete actual source
of the same R100 field on the same metric and domain once that source
has been bounded in (3). It contains none of the constants3/2,
23/18,23/9,270R, or any source-polynomial/window cap. It does not prove
those source estimates by itself.

The nonlinear far boundary response is not a source integral in
(4). It remains a separate positive term and must be added once
under its correct same-field mass. In particular the original
auxiliary far lift cannot be silently omitted or replaced by an
unrelated full-minus-auxiliary correction. All complete mean and
pointwise inverse contributions belong in the supplied source;
they are not removed by this extraction.

## 4. Actual execution and scope

All9,798 source-mode entries are strictly positive. The actual
extractor passed20,279 saved identity, domain, positivity and
outward-rounding gates, formally exited0 after19.736275787 seconds,
and used55,596 KiB peak RSS. It uses256-bit Arb and rounds positive
output coefficients upward to160 significant binary bits. There is
no new ODE, radial quadrature, Node call, field solve or fixed point.

The primary SHA is
`2181172e2cd395167e40887e0b464bd56b3cd28baa6d9a9271e81eee1f335a83`.
The source, primary, complete proof and formal resource record are
bound in the adjacent immutable manifest. This result is restricted
to the original inner geometry; it is not a certificate for the new
q106 or q122 metrics, nor is it a new cut-closure theorem.
