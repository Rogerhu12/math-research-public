# R147 SB: short-interval full-frequency parameter error and the nonlocal receiver

NP's strict particular and its exact trial are both zero above
\(b=9/50\).  Their complete error equation therefore has zero terminal
state at \(b\), and all its source terms are contained in \([0,b]\).
This note preserves the entire already completed SP nonradial comparison
matrix and all its mean components, and replaces only its coarse
full-domain radial scalar factor by a new genuine short-interval cost.
The old PDE trial, residual integrals, source estimates and matrix
exponentials are not evaluated again.

This also supplies the norm required by the genuinely nonlocal phase and
passive-height rows: a uniform interior primitive-plus-mean bound.  A
waist-only density bound or an old \(L^2\)-state phase norm does not supply
that norm by itself.

## 1. The same original SP comparison

Use the complete original SP execution
`notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json`,
SHA256 `a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12`.
It concerns the original selected family on
\([0,2333968743003/10^{13}]\), which strictly contains \([0,b]\), and
retains the full Fourier state and two physical means.  The complete
nonnegative matrix factors are entrywise at least the identity.  Hence
their whole ordered product bounds every shorter interval and every
source insertion time in the original order.

The original complete `reverse_nonradial_product` satisfies

\[
 \|\mathcal P_-\|_F<2.165=433/200.                            \tag{SB.1}
\]

This full four-entry conclusion was already paid in the original SP/STC
analysis.  SB uses this existing complete upper, rather than recomputing
an old matrix product.  Its radial factor is the separate scalar

\[
 c_-(r)=\max(0,-q_\delta'(r)/q_\delta(r)),\qquad
 q_\delta=\sqrt{-K_\delta}.                                  \tag{SB.2}
\]

The old complete logarithmic variation fee \(J_q\) covers the difference
between the original base \(q_0\) and the entire selected \(q_\delta\),
including both compact endpoints.  This is the original saved
`new_compact_log_variation_fee_upper`; its wider selected interval
contains the actual NP member.  Positivity of the variation integrand
allows the same fee on the shorter interval.  No subtraction of two
unrelated upper bounds is used.

## 2. The only new radial integral

On a true complete original scalar cell, \(K_0<0\), and

\[
 \max(0,-q_0'/q_0)=\frac{\max(0,K_0')}{-2K_0}.                 \tag{SB.3}
\]

Intersect the original body rows with \([0,b]\), preserving every
original intrinsic seam and both one-sided definitions.  At the midpoint
\(c_i\) of each original cell, the already saved full Taylor data give

\[
 K_0'(r)\in K'_{0,i}+K''_{0,i}(r-c_i)
             +\tfrac12[K_0''']_i(r-c_i)^2.                    \tag{SB.4}
\]

All coefficients in (SB.4) are the entire original midpoint/whole-cell
balls.  No intrinsic ODE or derivative target is rerun.  If
\(U_i\) encloses the whole right side on the true intersection and
\([K_0]_i\) is the complete original curvature ball, define

\[
 C_{-,b}^0:=\sum_i |I_i\cap[0,b]|
       \frac{\max(0,\sup U_i)}{-2\sup[K_0]_i},
\qquad C_{-,b}:=C_{-,b}^0+J_q.                                \tag{SB.5}
\]

Every denominator must actually be proved positive.  The last cell is
restricted at the exact endpoint \(9/50\); no full-cell length is
silently omitted.  The bound is valid for every shorter source interval
because its integrand is nonnegative.  Continuity of \(q_\delta\) through
the original intrinsic and compact seams is the old SP qualification;
candidate cubic knots introduce no artificial curvature impulse.

Only (SB.5) is a new scientific radial target.  The consumer retains all
7721 complete original rows as input, uses the exact prefix intersecting
\([0,b]\), and reports the number of used original parents.  It does not
recalculate a previously completed full-domain curvature budget.

## 3. New strict receivers, including the interior norm

For the original SP coordinates

\[
 Y=\sqrt q\|IT(q)h\|_2,\quad Z=\sqrt q|\Pi T(q)h|,
\quad T(q)h=\frac{(h_1+qh_2,h_1-qh_2)}{\sqrt{2q}},
\]

the exact identity is

\[
 Y^2+Z^2=\|Ih_1\|_2^2+q^2\|Ih_2\|_2^2
                   +|\Pi h_1|^2+q^2|\Pi h_2|^2.              \tag{SB.6}
\]

The already saved complete source injection is

\[
 C_{\rm inj}\ge\frac{\sqrt{17}}4\max(1,q),
\qquad
 \sqrt q\|(ITf,\Pi Tf)\|
       \le C_{\rm inj}\|f\|_{H^{-1}\oplus H^{-1}}.            \tag{SB.7}
\]

Let \(n_{0,+}\), \(q_{0,-}\), and \(q_{\min,-}>0\) be the complete
old selected waist-density upper, waist \(q\) lower, and entire-interval
\(q\) lower.  All are retained as whole records, with lower endpoints
used only for denominators.  From (SB.1--7),

\[
 C_b=\frac{n_{0,+}}{\sqrt{q_{0,-}}}
              \frac{433}{200}e^{C_{-,b}}C_{\rm inj},
\qquad
 U_b=\frac{433e^{C_{-,b}}C_{\rm inj}}
                {200\min(1,q_{\min,-})}.                     \tag{SB.8}
\]

For every complete source supported in \([0,b]\), with zero terminal
state at \(b\), the original full selected propagation satisfies

\[
 \|\mathfrak D_0h\|_{\mathcal Y_0}
       \le C_b\|f\|_{L^1([0,b];H^{-1}\oplus H^{-1})},
\]
\[
 \sup_{0\le r\le b}
 \|(Ih_1,Ih_2,\Pi h_1,\Pi h_2)(r)\|
       \le U_b\|f\|_{L^1([0,b];H^{-1}\oplus H^{-1})}.          \tag{SB.9}
\]

Affine impulses add their entire \(H^{-1}\)-norms with no radial length
factor.  These bounds include the two means and every true Fourier
frequency.  No new finite193 approximation, no positive inverse, and no
cut normalizer are used.  In particular the second line has **no waist
density factor** inserted at an interior point.

## 4. Recombining the original complete NP error source

Keep the entire original NP and D records:
\(R,H_0,H_1,M_0,M_1,N_C\).  Their roles and support are exactly those in
NP.4--7, so the full selected error source has the whole upper

\[
 S_\nu=R+\vartheta(M_1H_1+M_0H_0)
               +\vartheta\sqrt{13/100}\,N_C,
 \qquad\vartheta=936826/10^6.                                 \tag{SB.10}
\]

The source has no part above \(b\), because both the true strict
particular and the exact frozen trial are zero there.  The exact trial
is continuous at every node and has zero terminal jets; all original
state jumps are zero.  The old complete operator difference is retained
on all of \([0,b]\), and only the parameter-source difference uses the
smaller compact length \(13/100\).

Thus

\[
 D_{\nu,b}\le\min(D_\nu,C_bS_\nu),\qquad
 E_{\nu,b}:=U_bS_\nu
 \ge\sup_{r\in[0,b]}
       \|(I(v_\nu-h^a),\Pi(v_\nu-h^a))(r)\|.                  \tag{SB.11}
\]

The minimum takes two complete bounds for the same original error.  It
does not reconstruct an integrand by dividing an old bound or subtract
unrelated upper records.  All new scalar results are formally saved and
read back before dependent arithmetic.  The old NP/PDE targets remain
completed and are not rerun.

## 5. Consequence for actual nonlocal rows

For an already specified full distributed state row
\(\ell h=\int_0^b\langle\ell_1h_1+\ell_2h_2\rangle\,dr\),
angular integration by parts gives the exact identity

\[
 \ell h=\int_0^b
 \left[-\langle(\partial_\phi\ell_1)Ih_1+
                     (\partial_\phi\ell_2)Ih_2\rangle
       +(\Pi\ell_1)\Pi h_1+(\Pi\ell_2)\Pi h_2\right]dr.
\]

Consequently its true NP response error is bounded by

\[
 |\ell(v_\nu-h^a)|\le E_{\nu,b}
   \int_0^b\left(\|\partial_\phi\ell_1\|_2^2+
                  \|\partial_\phi\ell_2\|_2^2+
                  |\Pi\ell_1|^2+|\Pi\ell_2|^2\right)^{1/2}dr.
                                                               \tag{SB.12}
\]

This supplies the correct full error norm for the original nonlocal
phase and passive-height rows.  Their actual coefficients, exact
parameter terms, and signed trial pairings must still be retained and
paid.  The formula does not assert that any nonlocal functional vanishes
merely because the local root and outer state are zero.

## 6. The same short interval also pays the complete raw L2 error

The exact strong comparison proved in
[NR.5--8](R144-supplement-actual-negative-and-root-propagation-in-a-full-tail-neighbourhood.md)
applies to the original selected background by setting its background
increment to zero. With \(\xi=T(q)h\), its coordinates are

\[
 H=\sqrt q\|P_\perp\xi\|_2,\qquad Z=\sqrt q|\Pi\xi|,
\quad H^2+Z^2=\|h_1\|_2^2+q^2\|h_2\|_2^2.                \tag{SB.13}
\]

The true differential inequality is dominated by
\(D_4\mathcal A D_4^{-1}+c_-I_2\), where
\(D_4=\operatorname{diag}(4,1)\) and \(\mathcal A\) is exactly
SP's old complete matrix. This is the NR energy proof for the full
equation, not inversion of the primitive on an arbitrary state. The
old four complete entries give the already proved bound

\[
 \|D_4\mathcal P_-D_4^{-1}\|_F<2.185=437/200.            \tag{SB.14}
\]

The constant in (SB.14) uses the original selected matrix. None of
NR's later nearby-centre amplification or compact-background constants
is used. Similarity preserves positivity and the identity, so every
shorter ordered product and source insertion is still dominated.
The full strong source injection obeys the exact identity

\[
 \sqrt q\|(P_\perp Tf,\Pi Tf)\|
     =\|\operatorname{diag}(1,q)f\|_2
     \le\max(1,q)\|f\|_2.                              \tag{SB.15}
\]

In particular there is no \(\sqrt{17}/4\) primitive conversion in
this strong source slot. Let \(q_{\max,+}\) be SP's whole selected
`new_entire_q_upper`. Then the same new radial cost gives

\[
 V_b=\frac{437}{200}e^{C_{-,b}}
             \frac{\max(1,q_{\max,+})}{\min(1,q_{\min,-})},
\qquad
 \sup_{r\in[0,b]}\|h(r)\|_2\le V_b\|f\|_{L^1_rL^2_\phi}.
                                                               \tag{SB.16}
\]

For the NP error source, the factor needed to convert its known
\(H^{-1}\) residual has a specific and limited scope. The original
`certify_cell` first forms

\[
 r_0=(\partial_r-DF(Q_c))h^a-\partial_\nu F(Q_c),       \tag{SB.17}
\]

at the exactly repaired degree32 centre. The exact trial has degree96;
the complete centre source has degree at most96; the fully formed
centre residual is certified to have degree at most160. The producer
explicitly requires this support after every primitive, product, both
rows and the mean have been assembled. Physical frequency is \(4j\).
Consequently

\[
 \|r_0\|_{L^1_rL^2_\phi}
     \le\sqrt{1+640^2}\|r_0\|_{L^1_rH^{-1}_\phi}
     <641R.                                             \tag{SB.18}
\]

Only \(R\) in (SB.10) is the residual (SB.17). The selected background
\(Q_{\delta_*}=Q_c+\delta_*Z\) includes degree96 state components;
its full operator/source differences can reach degree288 and are
**not** assigned the degree160 support. Those terms already have the
complete ordinary \(L^2\) estimates in D/NP and retain those units:

\[
 S_{\nu,2}=641R+\vartheta(M_1H_1+M_0H_0)
                    +\vartheta\sqrt{13/100}N_C.          \tag{SB.19}
\]

There is no Fourier projection in (SB.19), and the unknown true error
remains full Fourier. The actual trial jumps are zero; no independent
impulse is converted using an unjustified degree assertion. Combining
(SB.16--19) gives

\[
 E_{\nu,2}=V_bS_{\nu,2},\qquad
 \sup_{r\in[0,b]}\|v_\nu-h^a\|_2\le E_{\nu,2},
\quad
 \|v_\nu-h^a\|_{L^2([0,b];L^2)}\le\sqrt{9/50}E_{\nu,2}.
                                                               \tag{SB.20}
\]

These are the original unnormalized physical moving pair, with both
means. A phase or passive-height row with a paid full \(L^2_rL^2\)
dual norm can consume (SB.20) directly. No waist trace is extended
to the interior, and no old same-centre phase constant is automatically
transferred to a different selected background.

The pure algorithm is
`scripts/fourfold_codazzi_short_strict_nu_error_math.py`.  It has no IO
or numerical import. Its eleven ordered targets comprise (SB.5)'s two
radial costs, the complete weak source, two weak receivers, the weak
waist and interior errors, followed by (SB.19), (SB.16) and the two
errors in (SB.20). The public owner reads the entire genuine NP/SP
outcomes, original degree160 producer and all forty complete original
row descriptors before execution. Its full `admit_all_rows` input
reader restores the complete7721-row payload; it does not restore
unneeded centre, direction, trial or RW arrays. The original public
worker's capacity, README checks, actual-prefix preservation and
pull/rebase/push loop are retained unchanged.
This note supplies a new exact target and propagation theorem; it does
not label the unexecuted short radial integral successful.

