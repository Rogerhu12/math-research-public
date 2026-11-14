# A shorter initial meridian with the same inlet and radius increment

This is a new metric design budget, not an actual BVP continuation or a
closed-surface certificate. The exact rational calculations concern only the
axisymmetric background of the initial meridian segment. The accepted q095
field, its full core, and all current q096 tail calculations remain unchanged.

## Exact family

Read the binary64 values of `delta`, `vu`, and `start_acceleration` from the
accepted actual q095 frozen profile and interpret them as exact rationals
\(\delta,V,k_0\). In this record they are approximately
\(0.16134505278447636,0.32,0.45\). Let \(b\ge0\), and choose the unique positive
root \(S\) of

\[
 \frac{k_0S^2}{12}+\left(\frac V2+\frac{16b}{35}\right)S=\delta.
\]

For \(t=s/S\in[0,1]\), set

\[
 v_b(t)=k_0St+(3V-2k_0S)t^2+(k_0S-2V)t^3
       +64b\,t^3(1-t)^3,
 \qquad
 r_b(s)=1+S\int_0^{s/S}v_b(u)\,du.
\]

The pulse has maximum one before multiplication by \(b\), integral
\(16/35\), and vanishes together with its first two derivatives at both
ends. The full segment therefore satisfies

\[
 r_b(0)=1,\quad r_b'(0)=0,\quad r_b''(0)=k_0,
 \qquad
 r_b(S)=1+\delta,\quad r_b'(S)=V,\quad r_b''(S)=0.
\]

The higher derivatives of the full segment are **not** asserted equal to the
old segment after changing \(S\). The initial speed can increase and then
decrease; no monotonicity of the full speed is imposed. The radius remains
increasing. Thus the radius and its first two meridian derivatives still match
the original inlet and the unchanged outgoing boost segment. The initial
\(k_0\) used in the core inlet condition is preserved.

## Exact domain and curvature checks

For each tested \(b\), 100 rational bisections bracket the positive root
\(S\). Exact inequalities verify \(k_0S\le3V\) and \(V+b<1\). The original
cubic Hermite speed is then monotone from zero to \(V\), so
\(0\le v_b\le V+b<1\) everywhere. Consequently \(r_b\ge1\), and the
parallel curvature of this background is at most one.

The meridian curvature bound \(|\kappa_{\mathrm{mer}}|<8\) is equivalent to

\[
 64S^2(1-v_b(t)^2)-(v_b'(t))^2>0.
\]

The code constructs this degree twelve polynomial with rational interval
coefficients enclosing the exact algebraic \(S\). It converts power
coefficients to Bernstein coefficients and subdivides by exact midpoint
de Casteljau operations. Every accepted leaf has a strictly positive exact
rational coefficient lower bound. The saved leaves cover the entire closed
parameter interval. All five choices below pass this bound.

Height is \(S\int_0^1\sqrt{1-v_b(t)^2}\,dt\). The recorded height bounds use
256 exact Bernstein subintervals and integer-square-root rational bounds,
not quadrature convergence extrapolation. The exact rational endpoints in
the JSON are the certificate. Decimal intervals below have been rounded
outward; other floating displays in the JSON are approximations to its
exact rational fields.

| Pulse height \(b\) | Segment length, approximate | Background height, outward decimal enclosure | Height reduction from \(b=0\), outward enclosure | Sample meridian curvature maximum |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0.84217433 | [0.82194834, 0.82212134] | baseline | 0.51500 |
| 0.2 | 0.58982564 | [0.56152900, 0.56181417] | [0.26013418, 0.26059233] | 1.91611 |
| 0.35 | 0.47748544 | [0.44091237, 0.44142314] | [0.38052521, 0.38120896] | 3.53144 |
| 0.5 | 0.39980046 | [0.35311703, 0.35389849] | [0.46804986, 0.46900430] | 5.73761 |
| 0.6 | 0.36030825 | [0.30548565, 0.30648961] | [0.51545873, 0.51663568] | 7.63260 |

The curvature samples are design diagnostics. The full-interval certificate
is the weaker strict bound eight; no claim identifies those samples as exact
maxima.

## Meaning for the amplitude search

At fixed scalar profile parameters, this extra control can remove roughly
0.47 of initial background height for \(b=0.5\), while retaining the radius
increment, outgoing speed and the initial \(k_0\). Downstream background
pieces can retain their shapes and radial data, with the meridian coordinate
and accumulated height shifted appropriately. This makes it a useful candidate
for lowering a future complete diameter budget.

The actual deformed-field curvature, diameter, mean-height channel, full tail
coupling, and response of \(\delta,L_B,v_p\) under held core constraints have
not been calculated for this family. Such responses can offset the scalar
height benefit. The appropriate next numerical use is an explicit small new
physical control near \(b=0\), with complete actual-J forcing and the existing
true-H acceptance gates. This budget supplies no new fixed-g refinement, no
new accepted core amplitude, and no reach certificate.

## Reproduction and resource record

Run `computations/strong_initial_speed_pulse_budget.py` with
`--accepted-reference notes/2026-11-12-root-q095-design-fixed-actual-m24-tol7-frozen-r1.json.gz`
and a fresh `--out` path. The completed result is
`notes/2026-11-12-strong-initial-speed-pulse-budget-r1.json`; the companion
resource record confirms formal exit zero, 11.04 seconds wall time, and
13,556 KiB peak RSS. No physical Flow, RHS, Node worker, or BVP was constructed.
The source and accepted input hashes are recorded with the exact data.
