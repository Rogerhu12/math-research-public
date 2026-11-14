# Accepted q098 and q106: independently recomputed analytic profile domains

2026-11-13, geometry_audit, GPT-6 Astra Pro, AI-assisted.

## Result and exact objects

The fresh checker `strong_newg_analytic_profile_bounds.py` has completed with
formal exit 0 on each of the two actually accepted primary packets. Each run
passed all 39 identity and rational guards. It reads each packet's own
`frozen_profile` and the actual tagged port, interprets every saved binary64
constant as its exact rational value, and evaluates the inequalities again.
No certificate for q096, q098, or a planned warm profile is transferred to
another accepted field.

For the **intended exact analytic meridian** of each input, the result is

\[
 3/25<a(s)<9/5,\qquad |a_s(s)|<499/500,
 \qquad |a_{ss}(s)|\le 15/2.
\]

Every nonconstant angular-program segment following the Hermite inlet has physical length greater than
\(27/10000\); the sum of those lengths is less than 4. On its normalized
coordinate \(u\), the piecewise polynomial phase satisfies

\[
 |\phi|<8/5,\qquad |\phi_u|<4,
 \qquad |\phi_{uu}|<65,
 \qquad |\phi_{uuu}|<3300.
\]

The Hermite inlet is treated by its explicit speed polynomial, not by this
phase-polynomial assertion. After splitting a flat turn at its two ramp boundaries, each phase polynomial
has degree at most four. The brake has degree two. These statements concern
the analytic formulas whose constants come from the accepted packets. The
floating primitive, assembled floating segment endpoints, material chart,
surface mean, Cartesian surface jets, curvature, and reach require separate
quantitative bridges.

| Accepted field | Actual primary SHA256 | Formal wall time | Peak RSS |
|---|---|---:|---:|
| q098, M28, original p31 | `88175797998edbbe6d7ed18065fb8786cc58cec5e255b0efb95da9d08c728699` | 0.08131814002990723 s | 12580 KiB |
| q106, M28, original p31 | `83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293` | 0.11707854270935059 s | 12844 KiB |

The two formal resource records and the complete rational evidence are
separate files. Neither run evaluated an ODE, Node worker, Newton step, or
surface sampling grid. The original accepted data remain unchanged.

## Source and input guards

The checker pins the complete physical formulas in
`alternative-neck-provider.py`, `alternative-neck-flatturn.py`,
`alternative-neck-excursion.py`, `strong_angle_boost.py`, and
`root_dual_core_bvp.py`. Each hash is checked before deriving any bound.
The packet must have `solver_success=true`, `audit_pending=false`, and the
actual nonlinear-tail configuration. Its original physical-port SHA must
match the supplied port.

The loader calls `tagged_port` with the current profile. Consequently the
actual terminal bridge curvature is the current profile's
\(K=15/2\), rather than the old default value in the untagged port. The
checker verifies that value explicitly. The radius \(r_c\), slope \(w\),
and second derivative \(w'\) come from the original cut data.

The proof allows a nonnegative outward coast \(C\). Its first-turn upper
radius bound explicitly includes \(v_p C\). Both present packets have
\(C=0\), but this term is retained in the checker. It does not assume that
arbitrary future profiles satisfy these fixed guards: a changed profile must
run the checker and pass every guard again.

All comparisons below use Python `Fraction`. The alternating arctangent
series and the exact identity

\[
 \tan\bigl(4\arctan(1/5)-\arctan(1/239)\bigr)=1
\]

give a rational enclosure of \(\pi\). The angle lies in \((0,1)\), and
\(\pi/2>1\) follows from
\(\arctan 1=\int_0^1(1+x^2)^{-1}dx>1/2\); hence the correct branch is
\(\pi/4\). Sine and cosine comparisons use their Taylor polynomials and
explicit next-order remainder bounds. Decimal fields are displays only.

## Hermite inlet, boost, and descending turn

Let \(V=v_u\), \(k_0\) be the inlet acceleration, and \(\delta\) the
inlet radial change. The positive Hermite length \(S_0\) is the unique root
of

\[
 k_0 S_0^2+6VS_0=12\delta.
\]

The two endpoint signs and monotonicity give \(4/5<S_0<9/10\).
The degree-two Bernstein coefficients of the speed derivative are
\([k_0,3V/S_0-k_0,0]\). The checker proves that they are nonnegative and
bounded above by a value less than 1. The speed therefore increases from
zero to \(V\), and the radius increases from 1 to \(1+\delta\).

Put \(\epsilon=\operatorname{binary64}(.08)\). Exact sine comparisons
put the boost's endpoint angles between \(8/25\) and \(21/20\). Its
angular speed therefore has the upper bound

\[
 K_B<\frac{73}{100L_B(1-\epsilon)}<15/2.
\]

The first descending turn has length
\(L_1<\pi/[K_s(1-\epsilon)]\). Since radial speed has magnitude at most
one, its radius lies between

\[
 1+\delta-L_1\quad\hbox{and}\quad
 1+\delta+L_B+v_p C+L_1.
\]

The checker places these strictly inside \((3/25,9/5)\). The arcsine
derivative on the sync interval is at most 6, because the guard
\(36(1-v_\ell^2)\ge1\) holds. Thus its length is at most
\(6(v_\ell-v_d)/[K_{\rm sync}(1-\epsilon)]\). The available radial
decrease before the loop exceeds this quantity plus \(R\); hence the
descending coast has positive length.

## Symmetric loops and terminal bridge

For a symmetric loop turn,
\(\phi(1-u)=-\phi(u)\), so its exact radial integral is zero.
The largest inward loss is at most half its arclength. The lower radius is
therefore at least

\[
 R-\frac{\pi}{2K(1-\epsilon)}>3/25.
\]

The outward-turn radius is at most
\(\mathrm{ratio}\,R+\pi/[2K(1-\epsilon)]<9/5\).
The two intervening coasts have positive lengths because
\(\mathrm{ratio}>1\). This exact cancellation does not itself establish
cancellation for a floating quadrature or its accumulated endpoints.

Write the terminal angle and preceding peak as

\[
 \phi_t=-\pi/2+\arctan w,\qquad
 \phi_{\rm peak}=-\pi/2+(1-f)\arctan w.
\]

The exact inequality
\(\arctan w\ge w/(1+w^2)\) gives
\(\eta_0=(1-f)w/(1+w^2)\). The Taylor cosine enclosure proves
\(|\sin\phi_{\rm peak}|\le\cos\eta_0<499/500\).
All other speed endpoints are also below that constant. In particular the
loop speed alone is not a valid global speed bound.

The brake length is

\[
 L_{\rm brake}
 =\frac{2f\arctan(w)(1+w^2)^{3/2}}{-w'}.
\]

The checker bounds it above by
\(2fw(1+w^2)^2/(-w')\), and below by
\(2fw/[(1+w^2)(-w')]\). Its angular rate is less than
\(-w'<15/2\). The preceding terminal turn has length less than
\((9/50)/[K(1-\epsilon)]\). The remaining bridge coast has a strictly
positive radial budget after paying both lengths. Every bridge radial
velocity is negative; its radius stays between its endpoints, with terminal
radius \(r_c>3/25\).

Since \(a_s=\sin\phi\), the angular-rate bound implies
\(|a_{ss}|=|\cos\phi\,\phi_s|\le15/2\) on the non-Hermite pieces;
the inlet bound is smaller. The ideal segment constructions match the
endpoint values and the vanishing turn accelerations. The final brake uses
the declared port jet.

## Phase and length constants

For a flat turn, the ramp formula gives

\[
 |\phi_u|\le\frac{\pi}{1-\epsilon},\quad
 |\phi_{uu}|\le\frac{3\pi}{2\epsilon(1-\epsilon)},\quad
 |\phi_{uuu}|\le\frac{6\pi}{\epsilon^2(1-\epsilon)}.
\]

The exact upper endpoints are below 4, 65, and 3300. The boost obeys the
same ramp formula, and the brake obeys these looser bounds. The JSON records
positive lower bounds for the boost, first turn, sync, both loop turns,
terminal turn, and brake; the minimum is strictly greater than
\(27/10000\). It also checks an upper bound below 4 for their sum.

These actual-profile constants can be consumed by a subsequent proof of the
Gauss64 realization and complete mean. They prove neither that the provider's
returned analytic derivative fields are exact derivatives of its floating
primitive nor that the accepted physical surface has the required curvature,
Euclidean amplitude, fixed-subset amplitude, or reach.
