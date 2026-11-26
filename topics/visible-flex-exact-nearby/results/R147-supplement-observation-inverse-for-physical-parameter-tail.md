# R147 PO: the true physical parameter column from one new observation inverse

This supplement works with the **original selected** implicit family
\((Q_\delta,\nu_\delta)\), at intrinsic parameter \(\eta_0\).  Its inputs are the
actually completed NP two targets, NH twelve targets, JC seven targets, the
original complete RW96 definition and result, and NW's complete normalizer
conclusion.  It introduces a new96-dimensional observation inverse.  It does
not regenerate NP's trial, residual, signed pairings, or any old norm target.

All norms use the original normalized angular measure, period \(\pi/2\), and
physical Fourier frequency \(4j\).  The full PDE unknown remains infinite
dimensional.  Both independent physical means and every original interface
condition remain.  This observation inverse does not certify the full
incoming inverse or the true parameter Schur complement.

## 1. The exact finite object that the observations determine

NP's exact frozen reflected trial has \(h_1^a\) odd and \(h_2^a\) even, of
degree at most96.  At the waist its original density variables are

\[
 w_\pm^a=\frac{n_g}{\sqrt{2q}}(h_1^a\pm qh_2^a),\qquad
 y_\pm^a=Iw_\pm^a,\qquad \mu_\pm^a=\Pi w_\pm^a.                 \tag{PO.1}
\]

Here \(q,n_g\) are the same positive whole selected waist scalars used by NP.
The exact physical primitive

\[
 f^a=\tfrac12(y_+^a+y_-^a)
     =\frac{n_g}{\sqrt{2q}}Ih_1^a
     =\sum_{k=1}^{96}a_k\sqrt2\cos(4k\phi)                       \tag{PO.2}
\]

is even and mean zero.  Only this finite object is reconstructed below.
There is no claim to recover the odd primitive of \(h_2^a\), an amplitude
column, a phase functional, or any unobserved sine direction.  The exact
opposite-mean identity \(\mu_+^a+\mu_-^a=0\) does not set either individual
physical mean to zero.

The original complete RW trial is

\[
 p_j(\phi)=\sum_{|k|\le1024}c_{j,k}^{[4096]}e^{i4k\phi},\qquad
 c_{j,-k}^{[4096]}=c_{j,k}^{[4096]}\in\mathbb R.                  \tag{PO.3}
\]

It is the truncated **exact**4096-point DFT of the original exact sampled
compound cosine; it is not the midpoint of a ball.  NP already saved the
whole uninflated signed balls \(s_j\) for \(\langle p_j,f^a\rangle\), in
`complete_signed_trial_pairings.original_physical_primitive96`.  Both
Fourier signs and the two half-components in NP's actual pairing give

\[
 s=Ma,\qquad M_{jk}=\sqrt2\,c_{j,k}^{[4096]},\quad 1\le j,k\le96. \tag{PO.4}
\]

The corresponding194 inflated true observations remain a different input
object.  Their centers are never used as exact finite trial observations.

The new public child restores the entire original RW compound grid and all
96 complete1025-coefficient row carriers from their fixed definitions.  It
retains the original carrier receipts.  It then forms the new full matrix
\(M\), encloses its inverse, and solves (PO.4) with all96 **whole** raw balls.
These necessary carrier materializations do not run RW's old error or norm
targets, and do not evaluate NP's old pairings again.

For the dyadic point preconditioner \(R\), both complete products are paid:

\[
 \epsilon_M\ge\max(\|I-RM\|_F,\|I-MR\|_F)<1,\qquad
 \|M^{-1}\|_{2\to2}\le\frac{\|R\|_F}{1-\epsilon_M}.              \tag{PO.5}
\]

The full directed inverse and full observation column enclose the same
exact \(a\), even though the original interval entries share unknown
parameters.  Interval arithmetic does not discard these possibilities.
For complete recovered balls \(A_k\), the new direct candidates are

\[
 N_{0,\mathrm{direct}}\ge\left(\sum_{k=1}^{96}|A_k|_{\max}^2\right)^{1/2},\qquad
 N_1\ge\left(\sum_{k=1}^{96}(4k)^2|A_k|_{\max}^2\right)^{1/2}.   \tag{PO.6}
\]

Set \(N_0=\min(N_{0,\mathrm{direct}},H/\sqrt2)\), with outward rounding of
both complete candidates.  The second bound follows from the
actual NP bound \(H\ge\|(y^a,\mu^a)\|\), and not from an unobserved energy
subtraction.  No unobserved low sine or mean energy is subtracted anywhere.

## 2. Removing the actual mean translation, without fixing H(0)

Let \(H\) be the same true selected conjugacy used by RW, JC and NH.  Write

\[
 c=\Pi(H-\mathrm{Id}),\quad\psi=H-c=\mathrm{Id}+d,\quad\Pi d=0,
 \quad\eta=\|H'-1\|_{\mathcal A_0}\le H_1-1.                    \tag{PO.7}
\]

Here \(H_1\) is the original **complete derivative Wiener sum**, whose
constant coefficient is exactly1.  All nonzero Fourier modes are included.
Consequently

\[
 \|d\|_\infty\le\sum_{j\ne0}|d_j|
 \le\tfrac14\sum_{j\ne0}4|j||d_j|\le\eta/4=:\varepsilon.       \tag{PO.8}
\]

This argument does not replace the mean \(c\) by \(H(0)\).  The original
reflected output basis may use \(a=2H(0)\); that does not identify these
two translations.  We need neither their equality nor the value of \(c\).

For density pullback \(U_pv=(v\circ p)p'\),
\(H^{-1}=\psi^{-1}\circ R_{-c}\), hence

\[
 U_{H^{-1}}=U_{R_{-c}}U_{\psi^{-1}}.                            \tag{PO.9}
\]

The outer rigid translation is an isometry commuting with every ordinary
Fourier high projection.  Therefore it changes no high norm below.  This
does not identify any rotated **signed** entry with an unrotated entry.

Let \(m>0\) be JC's already proved lower for the complete homotopy including
the same true \(H'\); let \(M_0=1+\eta\).  For \(\rho=\psi^{-1}\),
\(\|\rho-\mathrm{Id}\|_\infty\le\varepsilon\), and the straight maps
\(\tau_t=\mathrm{Id}+t(\rho-\mathrm{Id})\) have derivative at least
\(1/M_0\).  The fundamental theorem of calculus and change of variables give

\[
 \|f\circ\rho-f\|_2\le\varepsilon\sqrt{M_0}\,\|f'\|_2.
\]

Also \(\|\rho'\|_\infty\le1/m\) and
\(\|\rho'-1\|_\infty\le\eta/m\).  Since \(P_{\ge97}f^a=0\),

\[
 \|P_{\ge97}U_{H^{-1}}f^a\|_2
 \le L_a:=\frac{\varepsilon\sqrt{M_0}N_1+\eta N_0}{m}.          \tag{PO.10}
\]

This is a bound on the full infinite density-pushforward tail.  No tail of
the composition is silently truncated.  The original (H), rather than
the approximate compound row lift, supplies \(m,\eta,\varepsilon\).

## 3. The complete true physical column and its original target normalizer

Let \(v_\nu\) be NP's true full-Fourier strict particular, with zero terminal
data at \(b=9/50\), extended by zero above \(b\).  Denote its full waist
density error from the exact trial by \(D\).  The physical reflection-fixed
primitive is

\[
 F_\nu=\tfrac12U_{H^{-1}}(1,1)Q_{R,y}\pi_yY(v_\nu).
\]

The original reflected parity is retained by the true linear problem.
The operator \(\tfrac12(1,1)\) has norm \(1/\sqrt2\), while \(Q_{R,y}\)
is orthogonal.  Thus, for the original full density receiver \(B_H\),

\[
 e_F=B_HD/\sqrt2,\quad
 \|F_\nu\|_2\le B_H(N_0+D/\sqrt2),\quad
 \|P_{\ge97}F_\nu\|_2\le L_a+e_F.                             \tag{PO.11}
\]

The original two mean observations remain in the parameter border.  Their
sum vanishes by reflected parity in this particular physical sum; this
does not remove their independent rows from the full inverse problem.

The whole NH bounds also give independent candidates \(F_{NH,0}/\sqrt2\)
and \(F_{NH,h}/\sqrt2\) in (PO.11).  This is a consequence of NH's **full
expressions**, not an inference comparing two different unknown operators:
NH's trial high expression includes the true physical pair, and its added
error is \(B_HK_WD\ge B_HD\); its whole expression is
\(B_HK_W(H+D)\ge B_H(H+D)\).  Both choices inside NH's whole minimum
therefore bound that same physical pair.  Taking the half-sum and using
the opposite-mean parity yields the stated candidates.  Each full
candidate is retained until the final minimum is taken.

The original target normalizer is

\[
 B=I+T_w I,\qquad
 T_w=\Pi_+M_w\Pi_++\Pi_-M_w\Pi_- .                            \tag{PO.12}
\]

This is the original same-sign operator.  It is not replaced by the
different whole projected multiplication \(P M_wP\).  The independent
physical parameter column is \(B^{-1}F_\nu\); no source \(W^{-1}A\) is
inserted into this column.  WBP's polynomial inverse gives

\[
 K_{B,0}=1+W_0/4\ge\|B^{-1}\|_{2\to2},\qquad
 B^{-1}F=F-T_w I B^{-1}F.                                     \tag{PO.13}
\]

The original full NW coefficient bounds \(W_0\) and \(W_{1/3}\) concern
the same selected rotation and the complete two-sign series.  On each
same-sign block, multiplication convolution has
\(H^{1/3}\) norm at most \(W_{1/3}\).  Also

\[
 \|I\|_{L^2_0\to H^{1/3}}=17^{1/6}/4<13/32,
 \qquad 13^6>17\,8^6.                                       \tag{PO.14}
\]

For the unchanged DG high index \(J_\dagger=2^{4608}\),
\(\Lambda_J^{-1/3}\le2^{-1536}\).  Combining the exact identity (PO.13)
with complete physical bounds \(F_0,F_h\) from (PO.11),

\[
 \|B^{-1}F_\nu\|_2\le K_{B,0}F_0,
\quad
 \|P_{J_\dagger}B^{-1}F_\nu\|_2
 \le F_h+2^{-1536}\tfrac{13}{32}W_{1/3}K_{B,0}F_0.             \tag{PO.15}
\]

The target subspace, means, finite rows and parameter border have not
changed.  In particular this is neither a new \(\Theta\) row nor an
estimate for an unpaid full inverse.  The numerical child publishes the
same original target-normalized bounds as two separate new records.

For the96 original physical cosine observations, JC's complete joint
scalar-row error \(E\) acts on this actual scalar \(f^a\).  The improved
whole joint error is therefore

\[
 \Xi_{\mathrm{phys}}\le EN_0+B_HD/\sqrt2.                     \tag{PO.16}
\]

The earlier whole NH \(\Xi_{\mathrm{phys}}\) is another complete candidate.
This error remains separate from the96 already saved raw signed balls.

## 4. Exact placement in the true parameter border

In the original sign convention the body row is
\(\mathcal D h-F_\nu^{\mathrm{body}}\kappa\), and
\(\mathcal Dv_\nu=F_\nu^{\mathrm{body}}\).  The frozen linear coordinate
change \(h=u+\kappa v_\nu\) therefore removes this one body column
exactly.  For every original remaining row \(\ell h+\omega\kappa\), it
leaves the actual column

\[
 \ell u+(\omega+\ell v_\nu)\kappa.                           \tag{PO.17}
\]

Its positive/root/local outer columns vanish where the compact forcing and
the strict particular are identically zero.  Nonlocal height and phase
functionals, the waist physical column (PO.11--16), independent means,
the amplitude row, and the selected scalar constraint are retained with
their true values.  Zero terminal state does not make a nonlocal phase or
height response zero.  This is the original RNS full block right shear;
it neither assumes nor proves invertibility of that full block.

## 5. Public computation and complete inputs

The source `fourfold_codazzi_physical_nu_observation_inverse_owner.py`
requires genuine complete NP, NH, JC and RW scientific/execution pairs,
the same original family identities, and the entire original NW execution.
Its manifest pins every current input and the four original native W/R31/K/H
objects.  It executes only on the public repository's Actions runner, at
the original320-bit directed runtime.  All original proof/data objects are
read whole; carrier reconstruction is limited to necessary exact RW inputs.

The child saves and reads back each of twelve complete scalar records
before dependent scalar arithmetic.  Complete matrix, inverse and recovered
coefficient balls are retained privately with readback receipts; no
reproducible array is published.  Actual failure preserves the complete
accepted prefix.  The full inverse gate in (PO.5) must actually pass before
the reconstructed norm claims are made.  This proof supplies the exact
new target; it does not declare an unexecuted numerical inverse successful.

Complete mathematical references, all in this topic's `results/` directory:

- `R147-supplement-actual-independent-strict-nu-particular-and-signed-column.md`
  and the unchanged NP source define the exact trial and its192 raw balls.
- `R147-supplement-mean-aware-complete-high-parameter-forcing.md` and
  `R147-supplement-actual-complete-high-parameter-forcing.md` retain the whole
  NH high candidates and all independent means.
- `R149-supplement-reflected-finite-waist-rows-from-complete-conjugacy.md`
  supplies the exact finite rows and their original phase convention.
- `R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md`
  supplies the unchanged polynomial target inverse; the NW execution is
  `notes/cohomological_normalizer_windows_sign_ci/run-43775614821-1/execution.json`,
 35204 bytes, SHA256
 `1e327e83dafb5d09ec98acc6ba887ae28962a7f242be7e82692a864c2f93cb0b`.
- `R133-supplement-actual-root-faithfulness-and-complete-incoming-parameter-Schur-reduction.md`
  retains the full parameter border and its coordinate-invariant Schur row.

