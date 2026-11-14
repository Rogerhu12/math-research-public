# Cell 12: ordered canonical forcing column for modes 98–104

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Result and identity

This is an algebraic replay of the original 1,873 physical panels for the
same original inner field. It does not solve another ODE, evaluate a new
radial quadrature, or alter the nonlinear source. The source SHA is
`a3bdb0d238c89ca4e42099174b60a44bb3774ba1350e4f4b9f7cd898b0345169`;
the primary SHA is
`24efddbcaee51e0636771b9265c0f548bb83d45db38f53e2912793985d35cfbc`.
The owned actual run exited 0 in 10.073863580 s, peak RSS 27,776 KiB, with
13,135 successful gates. Every one of the original panels is present in
its original order, including all nine original segments.

This extends the already frozen 94/96 ordered-panel proof to the single
window [98,104]. The comparison matrix uses upper mode 104, source
normalization uses nu_98, angular loss uses mode 98, and the final physical
covector and strong multiplier use mode 104. It is a covering-window bound,
not an independently computed mode-98 matrix.

## Original positive comparison on each panel

Write nu_m=m^2(m^2-1)/12. In the original canonical variables (Q,Xi/nu_m),
the integrated off-diagonal coefficients satisfy

\[
 A_p\leq \nu_{104}\sqrt{12}\,\mu_+
                  r_-^{-7}w_-^{-1}\Delta\log r_+,
 \qquad
 B_p\leq \frac{\sqrt{12}}{\mu_-}r_+^7w_+\Delta\log r_+.
\]

These are the identities a dr=sqrt(12) mu r^-8 dr/w and
b_0 dr=sqrt(12) r^6 w dr/mu, with dr=r d log r. The diagonal integral is
at most d_p=(104^2-4) Delta log r_+. The complete original panel enclosures
for r, w, width, total variation and source envelope are retained.

For p=A_p B_p<1 the original `positive_peano` comparison gives

\[
 D=1+p+\frac{p^2}{4(1-p)},\qquad
 E=1+\frac p2+\frac{p^2}{12(1-p)},\qquad
 P=\begin{pmatrix}D&A_pE\\B_pE&D\end{pmatrix}.
\]

The panel transfer is bounded by exp(d_p)P. The actual maximum p over all
1,873 panels is bounded by 0.543928220353664, strictly below 1; no panel
subdivision was required. All matrix entries are nonnegative and both
diagonals are at least 1.

## Ordered strip and source recurrence

The same original strip is
tau= tau_inner - Delta_tau * btau_prefix / btau_total. On each panel use

\[
 \Delta\tau_{p,-}=
 \frac{\Delta\tau\,({\rm btau}_p)_-}{({\rm btau}_{\rm cell})_+}.
\]

Each loss is nonnegative, and the sum of all these lower losses is checked
not to exceed the actual whole-cell loss. For either source material let
I_p be its complete unscaled canonical L1 integral. The two positive state
bounds, initialized at zero, follow the original order:

\[
 Y_{p+1}\leq e^{-98\Delta\tau_{p,-}}A_p^{\rm transfer}Y_p
                 +A_p^{\rm transfer}(0,I_p/\nu_{98}).
\]

The first term retains only a lower bound on actual angular damping. The
current-panel source receives no angular damping credit; its complete
positive contribution is paid. Using the whole panel transfer on that
source is valid because the original nonnegative generator bounds all
its suffixes by the full panel transfer. Positivity and actual ordering
therefore prove this recurrence by induction.

The two material integrals are bounded separately by

\[
 I_{1,p}\leq \min\left(
 \frac{r_+^4 V_{q,+}^2}{\sqrt{12}\mu_-}\Delta\log r_+,
 I_{{\rm original},p}\right),
\quad
 I_{\lambda,p}\leq \min\left(
 \frac{r_+^4 V_{q,+}^2}{\sqrt{12}\mu_-}{\rm TV}_p(\log w)_+,
 I_{{\rm original},p}\right).
\]

Both arguments of each minimum are bounds for the same material integral.
The original physical source scale (S sigma_12)^2 is included exactly once
after the recurrence. The original complete source factor 2 remains.

## Physical output and exact scope

At the true original output port the positive covector is

\[
 c=\left((B_+104+104^2)r_+^3,
       \frac{\sqrt{12}\mu_+\nu_{104}}{r_-^4 w_-}\right).
\]

The two absolute source columns are
2(1+104)(S sigma_12)^2 c Y_final. Division by the same true w_- gives
`source_two_material_to_cut`. The reported upward bounds are approximately
5.058131701907834e-42 for d1 and 2.134718495629600e-41 for d_lambda;
the actual stored dyadics are authoritative. `chosen_same_material_to_cut`
also intersects each material separately with its already certified
whole-cell source column. No subtraction of source budgets is performed.

This packet supplies one [98,104] window only. It does not authorize the
same Peano denominator for mode 112, 128, or any larger window without an
actual fresh domain check. All original incoming, other-frequency, mean,
inverse and far contributions remain duties of the same-field consumer.
The saved homogeneous matrix is not claimed to improve the old incoming
column. The result is a source kernel and does not itself establish a new
fixed point, a cut solution, a continuous strong geometry certificate, or
the q122 target metric.
