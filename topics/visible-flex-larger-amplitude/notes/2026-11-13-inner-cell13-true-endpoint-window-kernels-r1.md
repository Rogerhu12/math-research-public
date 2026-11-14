# Actual cell13 endpoint kernels on the original continuous strip

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Object and units

This calculation uses the same original inner real geometry as R33 and
R42, the complete 1,975 saved cell13 panels, and the original positive
canonical matrices. It does not change the metric, tail height,
continuous strip, source equation, or auxiliary parameter domain.
It evaluates no ODE, new radial quadrature, or nonlinear field.

Write \(Y=(B_n p,\kappa_\perp)\), \(V'=S V_s\), \(S=257/256\).
The input to the homogeneous column is absolute strong paired Fourier
mass at physical node14, in the cell14 frame and width
\(\tau_{14,\mathrm{outer}}\). The output is the corresponding absolute
mass at physical node13 in frame \(B_{13}\) and width
\(\tau_{13,\mathrm{outer}}\). The primary also supplies the output
mass divided by the true \(w\) at node13. These two output units are
separately named and must not be interchanged.

The two physical source materials are

\[
 d_1\,dr=\frac{V'^2}{w}\,d\log r,\qquad
 d_\lambda\,dr=\frac{V'^2}{w}\,|d\log w|.
\tag{1}
\]

Their inputs are weak Fourier pair masses, with the original
radial-supremum-first norm and continuous width. They are the physical
source in the equation for \(\kappa_\perp\). R106's relative source
\(\mathcal N\) is multiplied by \(w\) before using (1).

The thirteen windows are 94, 96, 98–104, 106–112, 114–128, 130–184,
186–192, 194–256, 258–512, 514–1024, 1026–2048, 2050–4096, and
4098–8190. They cover every even frequency from94 through8190.
The infinite band is outside this finite readout and is unchanged.

## Full ordered physical propagation

R33 (33.66)–(33.68) bounds the logarithmic norm of the actual weighted
physical homogeneous system by

\[
 (1-m/B)_+(-\lambda)_+-m\chi.
\]

For a window \([l,h]\), set \(q=(1-l/B)_+\). Each original panel
provides upper bounds for its downward variation \(D\) of \(\log w\)
and an interval \(J_-\le\int\chi\le J_+\). The original panel
`material_cV_over_w` divided by the original fixed \(k\) encloses this
integral; the same \(k\), frame, and two strip endpoints are checked
against both the old q density and the strong density. Thus

\[
 P=\exp(qD-lJ_-),\qquad A=\exp(qD)
\]

are valid positive upper factors. Starting with \(G=1\) and
\(H_1=H_\lambda=0\), the complete endpoint recurrence is

\[
 G_{\rm new}=PG,\qquad
 H_{j,\rm new}=PH_j+A\min(M_j,M_c),
\tag{2}
\]

where the panel's original q envelope is denoted \(V\), and

\[
 M_1=V_+(V/w)_+\,\Delta\log r_+,
 \quad M_\lambda=V_+(V/w)_+\,\operatorname{TV}(\log w),
\]

\[
 M_c=\frac{k_+V_+}{l}(1-e^{-lJ_+}).
\tag{3}
\]

Both source materials are bounded by the common density
\(d=kV\chi\). The identity
\(\int_s^r\chi(u)e^{-l\int_u^r\chi}\,du
 =(1-e^{-l\int_s^r\chi})/l\)
proves the second alternative in (3). The first alternatives simply
bound their entire panel integrals. Every term is nonnegative, so
intersecting these two bounds is valid, and the same-panel growth
factor in (2) is paid to both. The recurrence is ordered: the source
is propagated only through the current remainder and later panels.

All9 original segments are traversed in their exact rational panel
order, with no gaps or overlaps. The final endpoint state is kept;
no whole-cell radial maximum is substituted for it.

Let \(\sigma_{13}=\overline X^{s}_{13}/\overline X^{q}_{13}\).
The two envelopes have the same physical shape and the same strip,
so the source change from the original q panels to \(V'\) is exactly
\((S\sigma_{13})^2\). The delivered absolute source columns are

\[
 K_j=2(1+h)(S\sigma_{13})^2H_j.
\tag{4}
\]

The factor \(1+h\) converts weak source mass to the strong output
norm. The safe factor2 for the two physical components is retained
from the original proof, even at the endpoint. Input homogeneous
mass is already strong, so it is not charged another \(1+h\).

The cell14-to13 frame change costs
\(J_B=\max(1,B_{13}/B_{14})\). The original strip satisfies
\(\tau_{13,\mathrm{inner}}\le\tau_{14,\mathrm{outer}}\), so this
interface requires no extra angular payment. The physical
homogeneous column is \(2J_BG\).

## Independent canonical homogeneous column

For windows covered by an original actual canonical matrix, R33
(33.71)–(33.72) gives

\[
 Z=(Q,\Xi/\nu_m),\quad \nu_m=m^2(m^2-1)/12,
\]

\[
 Q=\frac{p}{imr^3},\qquad
 Z_2=\frac{r^4w}{\sqrt{12}\mu_{13}\nu_m}
      (\kappa_\perp+imp).
\tag{5}
\]

The saved positive matrix bounds the complete true cell13
propagator in this same cell's canonical frame. For unit absolute
physical input, positive conversion vectors are

\[
 c_{\rm in}=\left(
  \frac1{B_-l r_{\rm in,-}^3},
  \frac{r_{\rm in,+}^4w_{\rm in,+}}
       {\sqrt{12}\mu_-\nu_l}\max(1,h/B_-)
 \right),
\]

\[
 c_{\rm out}=\left(
 (B_+h+h^2)r_{\rm out,+}^3,
 \frac{\sqrt{12}\mu_+\nu_h}{r_{\rm out,-}^4w_{\rm out,-}}
 \right).
\tag{6}
\]

Let \(C_{13}\) be the saved covering matrix and
\(\Delta\tau=\tau_{13,\mathrm{inner}}-\tau_{13,\mathrm{outer}}>0\).
The canonical absolute homogeneous column is

\[
 2J_B\frac{1+h}{1+l}e^{-l\Delta\tau}
    c_{\rm out}\,C_{13}\,c_{\rm in}.
\tag{7}
\]

This uses actual endpoint radius intervals, the original actual
\(\mu_{13}\), and true endpoint \(w\). Both coordinate conversions
use cell13's \(\mu\), because the input is a physical state at the
shared boundary. A canonical cell14-to13 interface multiplier
\(1/\rho\) is therefore not additionally applied. Its effect would
only be required if the input itself were cell14 canonical data.
The physical frame jump \(J_B\) is paid explicitly.

For94 and96, the original94–96 matrix covers each singleton. The
original130–192 matrix covers the130–184 and186–192 windows. The
first11 output windows are covered by the original nine matrices.
No canonical matrix is extrapolated into2050–4096 or4098–8190;
these windows retain their physical column. The selected homogeneous
column is the minimum of (7) and \(2J_BG\). Source columns (4) are
retained unchanged, so this intersection cannot erase cell13 forcing.

## Actual boundary geometry and input normalization

The exact original source formula for physical node \(k\) uses
\(n=k-1\), \(\delta=\delta_0 2^{-n}\), and \(q=2^{-3/2}\):

\[
 a_n=3\delta+\frac{6c_0\delta_0q^{n+1}}{1-q},\quad
 r_o=r_c e^{a_n/\sqrt{12}},\quad
 \mu_n=\epsilon\delta^{11/4},\quad w_k=\mu_n/r_o^7.
\tag{8}
\]

The original constants are fixed exact dyadics from the pinned ready
packet. Formula (8) evaluates \(w\) without instantiating the original
radial-integrating provider. The old radius \(r_o\) in (8) is distinct
from the actual warped physical radius \(r\). The latter is read
from the first and last original panel endpoint intervals. The
computed true \(w\) intervals are checked inside the corresponding
original first/last panel \(w\) intervals; all actual panel radii also
obey the original \(r_c\le r\le257r_c/256\) domain.

The cell14 envelope at the input boundary has the explicit bound

\[
 V'_{14}(r_{\rm in})\le
 S\overline X_{14}\left[
 a_{14}r_{\rm in,+}^3+
 \frac{\sqrt{12}\overline\mu_{14}}
      {r_{\rm in,-}^4w_{\rm in,-}}\right].
\tag{9}
\]

The primary supplies homogeneous columns multiplied by this bound,
for directly consuming a cell14 whole-cell normalized strong cap.
Any deeper source and far dependence of that same field remains in
this input; it has not been removed. The actual complete source on
cell13 must separately be multiplied by (4), then added. A consumer
may intersect this endpoint result with an existing valid endpoint
or whole-cell bound for the same field only after all these terms
are paid.

For a shared near/rest window mass, use the maximum of the respective
window columns once, or a positive support calculation using the
window caps together with the original common mass. Summing one
full copy of a shared mass for every window would overpay; dropping
that mass or replacing it by an unrelated pointwise norm is invalid.

## Arithmetic and scope

All computations use256-bit Arb with each positive recurrence state
rounded upward to160 significant binary bits. Denominator lower
endpoints are strictly positive. Every fixed input and relevant
frozen source is SHA256 pinned, the full saved panel coverage is
checked, and the owned run records its real wait4 status and peak
RSS. Results and resource figures are in the adjacent immutable
primary and resource record; the manifest binds their final bytes.

This is a finite source/endpoint operator result for the original
inner geometry. It neither proves a new fixed point nor closes the
complete cut equation. It does not transfer any old-g certificate
to the separately constructed q098/q106/q122 metrics.
