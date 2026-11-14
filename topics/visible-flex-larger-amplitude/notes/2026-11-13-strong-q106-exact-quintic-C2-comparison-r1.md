# Exact C2 comparison repair of the accepted q106 physical quintic vector

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## 1. The statement concerns a new comparison field

The accepted q106 primary is SHA
`83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293`.
Its complete physical quintic representation contains85 real state
components on2,227 intervals, with all six coefficients saved as exact
binary64 arrays. The accepted raw state and final full-H nonlinear-tail
response are bound by the original accepted-loader checks and the
complete source/input identity in the primary certificate.

We interpret every saved coefficient and every physical knot as an
exact dyadic real number. The adjacent original polynomials need not
have exactly equal endpoint jets under this interpretation. We define
a new piecewise polynomial vector and enclose its difference from the
original vector through two physical-s derivatives. The construction
preserves every original polynomial's left value and first two jets,
as well as both original global endpoint jets through order2.

All original accepted files and the prescribed metric g remain
unchanged. Componentwise repair does not imply that any differential
relations among the85 state components continue to hold exactly.
It does not certify the PDE, metric error, full mean, Cartesian
surface, tail/cap joins or reach. Those require separate estimates
using the explicitly bounded comparison perturbation.

## 2. Exact repair on one physical interval

Let the physical interval be \([s_i,s_{i+1}]\), let
\(h=s_{i+1}-s_i>0\), and set \(t=(s-s_i)/h\). For one state component,
write the original polynomial as

\[
 p_i(s)=\sum_{j=0}^5q_j(s-s_i)^j.
\]

For every nonfinal interval, let \(\Delta_0,\Delta_1,\Delta_2\) be the
next original polynomial's left value, first derivative and second
derivative minus the corresponding right jets of \(p_i\). Put

\[
 u=\Delta_0,\qquad v=h\Delta_1,\qquad
 w=\tfrac12 h^2\Delta_2.
\]

The correction is the exact polynomial

\[
 R_i(t)=u(10t^3-15t^4+6t^5)
       +v(-4t^3+7t^4-3t^5)
       +w(t^3-2t^4+t^5).
\tag{1}
\]

Equivalently its only nonzero normalized power coefficients are

\[
 r_3=10u-4v+w,\quad r_4=-15u+7v-2w,\quad r_5=6u-3v+w.
\tag{2}
\]

The constant, linear and quadratic coefficients of (1) vanish, hence
its left value and first two derivatives vanish. At the right endpoint

\[
 r_3+r_4+r_5=u,\qquad
 3r_3+4r_4+5r_5=v,\qquad
 6r_3+12r_4+20r_5=2w.
\tag{3}
\]

After dividing normalized derivatives by h and h squared, these are
exactly the three needed physical jet corrections. Thus
\(\widetilde p_i=p_i+R_i\) agrees through order2 with the next original
polynomial at the common endpoint. The next polynomial's own repair
has zero left jets, so both repaired polynomials also agree through
order2 there. This argument applies independently to every state and
every internal interface.

On the final interval set \(R_i=0\). The first interval's left jets
are unchanged by (1), and the final interval is unchanged everywhere.
The entire repaired vector therefore has the original0/1/2 jets at
both global endpoints and is C2 across all2,226 internal physical
knots. Nothing in this argument identifies its derivatives with
separately stored state components or with the nonlinear RHS.

## 3. Whole-interval exact derivative bounds

The degree5 Bernstein coefficients of (1), including the initial
three zeros, are

\[
 0,0,0,\quad u-\tfrac25v+\tfrac1{10}w,\quad
 u-\tfrac15v,\quad u.
\tag{4}
\]

The degree4 Bernstein coefficients of its first normalized derivative
are

\[
 0,0,\quad5u-2v+\tfrac12w,\quad v-\tfrac12w,\quad v,
\tag{5}
\]

and the degree3 coefficients of its second normalized derivative are

\[
 0,\quad20u-8v+2w,\quad-20u+12v-4w,\quad2w.
\tag{6}
\]

The convex-hull property on \(0\le t\le1\) gives the complete
correction bounds

\[
 A_0=\max|\text{coefficients in (4)}|,\quad
 A_1=h^{-1}\max|\text{coefficients in (5)}|,\quad
 A_2=h^{-2}\max|\text{coefficients in (6)}|.
\tag{7}
\]

These enclose every physical point of each interval. No sample mesh,
numerical root finder or derivative substitution is used. The
producer computes all original endpoint differences exactly as
rational numbers and checks (3), the repaired-right/next-left
identities, positive interval lengths, terminal invariance, and
outward rounding on the complete finite data.

For each state and derivative order, the primary stores the maximum
of (7) over all physical intervals. It also stores the sum of those
statewise suprema. This is the conservative order
\(\sum_j\sup_s |D_s^d(\widetilde Y_j-Y_j)|\). It does not replace that
norm by \(\sup_s\sum_j\), or identify a state-component norm with a
Fourier norm without the actual field's separate basis conversion.
The local rows give maxima and sums on individual intervals for a
future Cartesian patch consumer. Their meaning is explicitly
separate from the global statewise norm.

## 4. Reproducible exact field, without large derived arrays

The field definition is the original exact coefficient arrays, knots,
and equations (1)–(2). It does not require a second floating coefficient
array. Re-rounding the repaired coefficients independently could
reintroduce jet jumps and is not part of this definition.

For complete reproducibility the producer additionally hashes the
stream, ordered first by interval and then by state, of the exact
rational h,u,v,w,r3,r4,r5. The exact serialization rule and final stream
SHA256 are included in the primary. All inputs and the unchanged
accepted-loader sources are SHA pinned. Every error bound is rounded
upward to at most128 significant dyadic bits and that inequality is
checked exactly. The primary contains all2,227 local rows and all85
global state rows; the much larger exact coefficient stream is cheap
to reproduce and is not stored as a redundant artifact.

The actual owned process records formal wait4 completion, runtime and
peak RSS in the adjacent resource record. The immutable archive
manifest binds the complete source, primary, resource and this proof.
The calculation uses only the accepted numerical representation and
exact algebra; it performs no ODE, Newton, Node or geometry sampling.

## 5. What remains before a continuous surface certificate

The result supplies a concrete C2 vector and a fully paid difference
from the original saved physical quintics. The original differential
relations must still be assessed on this vector. Its perturbation
must be propagated through the complete mean and the actual Cartesian
formula on a certified nondegenerate domain. The exact background,
floating function and quadrature evaluation, seam assembly, infinite
tail/closing pieces, prescribed metric refinement and all nonlocal
reach inequalities also retain their own unpaid requirements.

In particular this comparison does not alter or strengthen the
accepted numerical BVP status, and it never substitutes an old
inner-g certificate for q106 or a future q122 metric.

## Actual completed result

The owned run formally exited0 after259.246062043 seconds with peak86,428 KiB. All1,712,415 identity, coverage, exact jet, Bernstein and outward-rounding checks passed. The2,226 internal seams cover every one of the85 original physical components. The certified sums of statewise physical-s correction suprema are strictly below2^-59,2^-48,2^-33 for orders0,1,2 respectively (approximately1.04783402e-18,2.44579060e-15,9.13029487e-11). These three displayed dyadic inequalities were checked by exact rational comparison against the saved upward bounds. They quantify the new comparison field only; the unpaid nonlinear and geometric transfers listed above remain unpaid.
