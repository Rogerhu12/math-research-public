# Cells 15–24: actual port columns and complete local source columns

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Claim and fixed object

This certificate gives positive endpoint operators for the original inner
R33/R42 field on cells 15 through 24. It reuses the pinned original positive
canonical matrices, the complete R42 density bounds and the original closed
port formula. It integrates no new ODE and introduces no new far boundary.
The consumer must supply the complete original field on cell 25, and every
local nonlinear source, including its mean, inverse and infinite tail costs.
This statement is independent of the new q122 strong candidate.

The primary has schema `inner-true-cells15to24-point-and-whole-source-v1`,
source SHA `29df3ab22016a280a2e144d5cfd0a941d407046f9a7f90c8c19c1ee170f9d1ae`
and primary SHA `220fe04036eea830a66f407890f2ba91d6808ea189c45e8ffc99e05b99726fdf`.
The owned run exited 0 in 3.538619052 s, with peak RSS 34,540 KiB and 297
successful gates. The input and helper source identities are recorded in the
primary and were checked before computing any column.

## One input mass, two positive columns

Fix a cell n, a mode m in a saved window [l,h], and its actual inward port.
Write U=|B_(n+1) p_m| and V=|kappa_m| at that single port. The existing
strong norm, which takes each component's radial supremum before the Fourier
sum, implies a bound for U+V at this point. It does not give two independent
unit budgets.

Use the original canonical state (Q,Y), where Y=Xi/nu_m and
nu_m=m^2(m^2-1)/12. The original physical-to-canonical identities give

\[
 |Q|\leq\frac{U}{B_{n+1}m r_{\rm in}^{3}},\qquad
 |Y|\leq\frac{r_{\rm in}^{4}w_{\rm in}}{\sqrt{12}\,\mu_n\nu_m}
             \left(\frac{mU}{B_{n+1}}+V\right).
\]

The producer uses lower denominators and upper numerators throughout. Thus
the first column is bounded by

\[
 v_U=\left(\frac1{B_{n+1,-}l r_{{\rm in},-}^{3}},
              z\frac h{B_{n+1,-}}\right),\quad
 v_V=(0,z),\quad
 z=\frac{r_{{\rm in},+}^{4}w_{{\rm in},+}}
          {\sqrt{12}\,\mu_{n,-}\nu_l}.
\]

The positive output covector is

\[
 c_{\rm out}=\left((B_{n,+}h+h^2)r_{{\rm out},+}^{3},
 \frac{\sqrt{12}\,\mu_{n,+}\nu_h}
 {r_{{\rm out},-}^{4}w_{{\rm out},-}}\right).
\]

Let A be the saved positive whole-cell comparison matrix for a window
covering [l,h]. With the complete original strip loss
Delta tau=tau_inner-tau_outer, the two output columns are

\[
 K_U=\frac{1+h}{1+l}e^{-l\Delta\tau}c_{\rm out}A v_U,
 \qquad K_V=\frac{1+h}{1+l}e^{-l\Delta\tau}c_{\rm out}A v_V.
\]

All quantities on the right are rounded upward. Their maximum consumes the
single input mass U+V. There is no additional factor 2: the two physical
output components have already been added by c_out. There is no additional
frame jump: the actual input frame B_(n+1) occurs in the columns themselves.
For the singleton windows 94 and 96 the strong-weight ratio is exactly 1.
They still use the original covering [94,96] matrix; no single-mode ODE is
claimed. The remaining windows retain the stated strong-weight ratio.

## Actual port normalization

Let S=257/256, and let X_(n+1), a_(n+1), mu_(n+1) be the original R42
envelope data. At the actual input port the same original field satisfies

\[
 V'_{n+1}({\rm port})\leq S X_{n+1}
 \left(a_{n+1}r_{{\rm in},+}^{3}
 +\frac{\sqrt{12}\,\mu_{n+1,+}}
 {r_{{\rm in},-}^{4}w_{{\rm in},-}}\right).
\]

The index of this mu is n+1; it is different from the current canonical
system's mu_n. The producer evaluates the actual closed-port w formula and
uses the original rigorous radius domain r_c <= r <= R at ports 15–25.
It invents no saved panels for these ports. Every resulting point upper
bound is checked against the old whole-cell upper bound. Multiplying a
whole-cell normalized field bound by this point upper bound is legitimate
at that port. It does not turn the point upper bound into a lower bound or
into a replacement whole-cell envelope.

## Complete local sources

Before multiplication by S, the current-cell complete physical envelope is

\[
 V_n\leq V_{n,\max}=X_n\left(a_nR^3+
 \frac{\sqrt{12}\,\mu_{n,+}}{r_c^4w_{n,-}}\right).
\]

For a weak paired Fourier coefficient of the two physical source materials

\[
 d_1=\frac{(S V_n)^2}{r w},\qquad
 d_\lambda=\left|\frac{w_r}{w}\right|\frac{(S V_n)^2}{w},
\]

the complete canonical source integrals, before S^2, are bounded by

\[
 I_1\leq\frac{R^4 V_{n,\max}^2}{\sqrt{12}\,\mu_{n,-}}
                    (\Delta\log r)_{n,+},\qquad
 I_\lambda\leq\frac{R^4 V_{n,\max}^2}{\sqrt{12}\,\mu_{n,-}}
                    {\rm TV}_n(\log w)_+.
\]

These follow directly by multiplying the physical forcing by the original
canonical conversion r^4 w/(sqrt(12) mu_n), then using dr=r d log r in
the first material. The original full width and total variation are paid.

The frozen positive generator has nonnegative off-diagonal entries and
diagonal (m^2-4)r_x/r >= 0. Every prefix fundamental matrix is therefore
entrywise at least the identity. In the ordered identity
Phi(b,a)=Phi(b,s)Phi(s,a), positivity gives Phi(b,s) <= Phi(b,a) <= A.
Consequently the saved whole A bounds every forcing suffix. Mere
nonnegativity of the endpoint A would not by itself prove this fact.

The reported absolute source columns are the upward-rounded quantities

\[
 L_j=\frac{2(1+h)S^2}{\nu_l}
       (c_{{\rm out},1}A_{12}+c_{{\rm out},2}A_{22}) I_j,
       \qquad j\in\{1,\lambda\}.
\]

The conservative original source factor 2 remains. No whole-cell angular
decay is credited to a source that may occur at the output endpoint. The
source's actual two material amplitudes remain inputs to the consumer;
this packet does not replace them by homogeneous data.

## Stable loading interface and scope

The top-level `cells` array is ordered 15 through 24. Each cell retains
`tau_input`, `tau_inner`, `tau_output`, actual w bounds, the direct input
and output frame bounds, and `nextcell_Vprime_boundary_upper`. The exact
adjacent strip equality is checked for every cell. Each `rows` array holds
11 windows covered by the original nine matrices. The uncovered windows
[2050,4096] and [4098,8190], and all higher modes, keep their original
certified bounds.

The fields `input_absolute_mass_to_absolute_endpoint` and
`input_nextcell_Vprime_mass_to_absolute_endpoint` distinguish an absolute
input mass from one normalized by the actual next-cell port envelope.
`source_two_material_to_absolute_endpoint` gives the two complete local
source columns. The corresponding `*_to_cut` fields additionally divide
by the current cell's true w_out lower bound. Only cell 12 is the original
head cut; intermediate divisions are explicitly labelled readout units.

A consumer may start with the unchanged complete cell-25 field, propagate
24 down to 15, add every local source, and intersect with the old valid
point bound at each stage. This is finite positive substitution in the
same field, not a new fixed-point or cut-consistency theorem. All far,
mean, inverse and remaining-frequency obligations remain intact.
