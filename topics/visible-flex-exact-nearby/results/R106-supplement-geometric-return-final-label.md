# R106 supplement: both geometric phase legs on the actual final circle label

The complete actual forward finite-part phase has now been bounded in
[the forward-phase theorem](R106-supplement-complete-actual-forward-phase.md).
This supplement pays the actual second geometric leg and the remaining
R101 label change. It gives a complete geometric returned phase with
an explicit analytic norm:

\[
 \boxed{\ \sup_{|\Im x|\le1/4096}|b_{\rm geom}(x)|<26410.\ }     \tag{1}
\]

The parameter is the actual \(p_\infty\) supplied by R101.
The complete Ai/contact/port propagation identity and its strong remainder
are still required to identify this geometric coefficient with the operator
coefficient \(b\) in R104. This supplement does not prove that identity,
the full \(R_*\), an effective cutoff or the PDE inverse.

## 1. The actual half map is a translation in the final label

Let \(P\) be the actual half-return map in normalized physical angle.
R77 proves the exact natural-lift identity \(R=P^2\) for this same explicitly
symmetrized affine family. There is no extra angular reflection or shift.
Write the actual R101 conjugacy as

\[
 \chi=H\circ J\circ\Phi,\qquad
 R\circ\chi=\chi\circ T_{2d_*}.
\]

All of these are actual real orientation-preserving degree-one circle
diffeomorphisms, with the natural lifts used in R77/R100/R101.
Set \(L=\chi^{-1}P\chi\). Then

\[
 L^2=T_{2d_*},\qquad LT_{2d_*}=T_{2d_*}L.
\]

Thus \(u(x)=L(x)-x\) is a continuous \(2\pi\)-periodic function satisfying
\(u(x+2d_*)=u(x)\). The actual quadratic rotation \(d_*/\pi\) is irrational,
so its real orbit is dense. Continuity gives \(u\equiv c\).
The natural-lift square identity gives \(2c=2d_*\), hence

\[
 \boxed{\ \chi^{-1}P\chi=T_{d_*}.\ }                          \tag{2}
\]

If only circle maps were retained, the same argument first gives the two
possible half translations; the already fixed natural lifts select (2).
No approximate half-return residual is promoted to an exact identity here.
The argument uses the actual full conjugacy and exact square relation.

## 2. Equality of the two geometric legs

The exact radial reflection of R77 has \(a_0,c_0,d,\mu\) even in \(r\)
and \(b_0\) odd. Consequently the complete original R37 density
\(\mathcal F/\mu\) is even. Its ground-state correction is included:
the ratio \(F_{\theta,z}/F_z\) and its smooth waist version are preserved by
the reflection.

The reverse characteristic becomes the forward one under \(r\mapsto-r\),
with the branch exchange specified by R77 and R46. The reversal of physical
radial orientation and the amplitude-branch convention give the same real
half-phase coefficient, exactly as in R46 Section 9.
The two root finite parts are reflected in the same original inward
coordinate and use the same physical cuts.
Therefore the second geometric half-phase is the pullback of the first
by the actual half map. No mean, root constant or endpoint is discarded.

Let \(h_{\rm fwd}\,dx\) be the complete phase on the original saved label,
whose physical initial angle is \(H(x)/4\).
With \(\Psi=J\circ\Phi\), define

\[
 h_{\rm circ}(x)
   =h_{\rm fwd}(\Psi(x),p_\infty)\Psi'(x).
\]

The exact one-form transformation of R106 (106.33), followed by (2), gives
the complete geometric two-leg coefficient

\[
 b_{\rm geom}(x)=h_{\rm circ}(x)+h_{\rm circ}(x+d_*).            \tag{3}
\]

The averaging identity for one-form pullback and the R50 material finite
part recover the previously certified scalar mean. This is a consequence
of (3); that scalar mean was not used to replace its nonmean part.

## 3. The final composition domains and derivative

R101 supplies the actual bounds on the strip \(1/2048\)

\[
 \|\phi\|<1.102524382\,10^{-8},\qquad
 \|\phi'\|<3.284319905\,10^{-5}.
\]

The actual finite preNewton report supplies, on \(5/2048\),

\[
 \|w\|<8.550795472\,10^{-12},\qquad
 \|w'\|<1.134572570\,10^{-9}.
\]

The new consumer uses the full exact rational R31 bounds and full saved
preNewton endpoint balls. At \(s=1/4096\),

\[
 s+\|\phi\|<5/2048,\qquad
 s+\|\phi\|+\|w\|<1/2048.
\]

Thus \(J\circ\Phi\) stays inside the actual forward phase's paid strip.
Its derivative is bounded by

\[
 M_\Psi=(1+\|\phi'\|)(1+\|w'\|)
 <1.000032844333651.
\]

The actual parameter movement, including the exact preNewton increment,
is also checked to remain strictly inside the original \(10^{-9}\) phase
family. The unchanged \(H\) hash is matched between the original true-ray
descriptor and both stages of the circle construction, so the final
relative label change is really \(\Psi\); no extra \(H\) is inserted.

The complete forward bound, pulled back by this actual derivative, gives

\[
 \|b_{\rm geom}\|_{\sup,s}
 \le2M_\Psi\|h_{\rm fwd}\|_{\sup,1/2048}
 \le26409.294891525955<26410.
\]

Real translation by \(d_*\) does not change an analytic-strip supremum.
For any integer \(0\le q\le12\), the full nonmean Fourier norm on
\(s_w=1/8192\) is bounded, with the unrounded \(M\) from (1), by

\[
 2^{q/2+1}M\,q!\left((1-e^{-(s-s_w)})^{-q-1}-1\right).
\]

This sums every Fourier mode, including the uncomputed complement. The
report retains all these directed values.

## 4. Executed certificate and remaining operator obligation

The new executable is
[geometric return budget](../scripts/fourfold_subprincipal_geometric_return_budget.py).
Its actual report is

    notes/2026-11-13-R106-geometric-two-leg-final-circle-phase.json

SHA256:

    ef54df89ca4d85f44fac159c7650f5f2002a1ab60fc221c477d506eb2c7dbc05

It binds the complete forward report, original true-ray descriptor,
exact preNewton report and exact R31 report, checks the actual common
initial label and the complete composition/parameter domains, and executes
the displayed directed budget. Reproduce from the topic directory:

~~~bash
python3 scripts/fourfold_subprincipal_geometric_return_budget.py \
  --out notes/2026-11-13-R106-geometric-two-leg-final-circle-phase.json
~~~

This resolves the geometric two-leg phase and final label loss.
To use it as \(M_{S+3}(b-\beta)\) in a completed R104 feedback certificate,
one must still establish the actual whole-operator realization of R46
Section 9, including both canonical collars, complete positive-side
Ai/contact/regular-port/source terms, all cone/mean blocks and the full
strong \(4/3\) remainder. The report leaves that identification and all
strong-inverse completion flags false.
