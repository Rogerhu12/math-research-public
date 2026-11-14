# Actual q098/q106 Gauss64 primitives through two derivatives

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

## Statement and scope

For the two actually accepted q098 and q106 ideal analytic neck profiles,
use the original 64 binary64 Gauss nodes and weights, but evaluate the
integrands and all arithmetic as exact real expressions. Keep the exact
analytic segment lengths and parameters aligned, and start both primitive
constructions at the same zero anchor. The resulting piecewise primitives
and the exact analytic primitives satisfy the uniform physical arclength
bounds

\[
 |\Delta I|\le2^{-44},\qquad
 |\partial_s\Delta I|\le2^{-44},\qquad
 |\partial_s^2\Delta I|\le2^{-31}.                 \tag{1}
\]

These bounds apply separately to the meridian radial and height
primitives; paying the Hermite height cost also in the radial bound is
harmless. Derivatives in (1) are the one-sided derivatives on each
original smooth phase subpiece. The exact-table quadrature primitive is
continuous, but it need not have equal first or second derivatives at
joins. Its corresponding derivative jumps are bounded by twice the last
two constants. No C2 repair has yet been performed or charged.

The inputs are the actual accepted primary SHAs
88175797998edbbe6d7ed18065fb8786cc58cec5e255b0efb95da9d08c728699
and 83c4c9fdb2b493a42ed4328c507b977c4d12fa5d5839a901bfa20f488621a293.
Their two actual profile domain certificates are consumed by SHA. The
producer explicitly rejects nonzero initial-speed pulse or frontload
keys. Thus this result is not a certificate for a future nonzero
degree22 frontload profile.

The conclusion is an integration-rule bridge, not a complete floating
provider certificate. Initial floating asin, atan, square root and
segment-endpoint assembly, floating affine-node and phase arithmetic,
vector trigonometric evaluation, dot products and subsequent accumulation
remain unpaid. Alignment of the analytic and realized segment lengths,
the C2 seam repair, the full Fourier-field mean and Cartesian jet
propagation remain separate tasks. In particular, an old metric or old
tail H certificate is not being transferred.

## 1. The actual table

The earlier actual-table primary
`2026-11-13-strong-newg-Gauss64-table-bridge.json`, SHA
0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d,
isolates all 64 roots of P64, proves their disjointness and completeness,
and encloses every positive normalized exact Gauss weight. It binds the
actual imported binary nodes and weights and proves all 399 original
gates. This consumer checks that entire identity before use.

Let \(v_i,w_i\) denote the exact normalized Gauss data, and let
\(\widehat v_i,\widehat w_i\) be the exact real values of the actual
binary64 table. The primary supplies upward rational bounds

\[
 E_u\ge\max_i|\widehat v_i-v_i|,\qquad
 E_w\ge\sum_i|\widehat w_i-w_i|,\qquad
 E_c=\left|\sum_i\widehat w_i-1\right|.
\]

Both node sets lie in [0,1], the exact weights are positive, and their
sum is one. All stored upward dyadics are consumed as exact rationals.

## 2. Moving the upper endpoint and differentiating

For a fixed smooth integrand f on one normalized piece define

\[
 G(u)=\int_0^u f(t)\,dt,\qquad
 Q(u)=u\sum_i w_i f(uv_i),\qquad 0\le u\le1.
\]

The binary-table expression \(\widehat Q\) replaces only the nodes and
weights in this formula. It is differentiated as a real function:

\[
 Q'(u)=\sum_iw_i\{f(uv_i)+uv_i f'(uv_i)\},
\]

\[
 Q''(u)=\sum_iw_i\{2v_i f'(uv_i)+uv_i^2f''(uv_i)\}.
\]

If \(\sup|f^{(j)}|\le M_j\) for j=0,1,2,3, the weight perturbation
and the node mean-value theorem give respectively

\[
 T_0=E_wM_0+E_uM_1,
\]

\[
 T_1=E_w(M_0+M_1)+E_u(2M_1+M_2),
\]

\[
 T_2=E_w(2M_1+M_2)+E_u(2M_1+4M_2+M_3).       \tag{2}
\]

For example, differentiating
\(2v f'(uv)+uv^2f''(uv)\) with respect to v gives
\(2f'+4uvf''+u^2v^2f'''\). This accounts for every term in the last
node-error charge. The proof uses the exact weights' total mass once;
it does not multiply by a mode count or by 64.

Choose a single degree127 polynomial p on the whole fixed piece, and
write r=f-p with \(\sup|r^{(j)}|\le R_j\). The exact Gauss rule
integrates p over every partial interval exactly, as does the derivative
of that identity. Therefore

\[
 |Q-G|\le2R_0,\quad
 |Q'-G'|\le2R_0+R_1,\quad
 |Q''-G''|\le3R_1+R_2.                         \tag{3}
\]

The polynomial is fixed as u changes. Selecting a new approximation at
each u and differentiating it without accounting for that dependence
would not prove (3).

## 3. Exact Cauchy tails

If f is analytic on the disk of radius R about 1/2, with modulus at
most M, its Taylor coefficients satisfy \(|a_k|\le M/R^k\). Put
\(q=(1/2)/R\) and K=128. On the real interval [0,1], the degree127
remainder and its first two derivatives are bounded by

\[
 R_0=M\frac{q^K}{1-q},
\]

\[
 R_1=2M q^K\left(\frac K{1-q}+\frac q{(1-q)^2}\right),
\]

\[
 R_2=4M q^K\left(\frac{K(K-1)}{1-q}
 +\frac{2Kq}{(1-q)^2}+\frac{2q^2}{(1-q)^3}\right).       \tag{4}
\]

These are exact sums of nonnegative coefficient tails. They are
calculated with rational arithmetic, not decimal estimates.

## 4. The initial Hermite height integral

For the actual initial Hermite piece, its speed is

\[
 v(t)=bt+(3V-2b)t^2+(b-2V)t^3,\qquad b=k_0L.
\]

Both actual profile certificates prove \(4/5<L<9/10\), monotonicity
of v and \(0\le v\le V<1/3\). Set \(z=t-1/2\). The exact identity

\[
 v(1/2+z)=V/2+b/8+(3V/2-b/4)z-(b/2)z^2+(b-2V)z^3
\]

and the entire permitted b interval prove \(|v|<4/5\) on
\(|z|\le3/4\) for each actual profile. The computed upper values
are below 0.736 for q098 and 0.730 for q106. Thus
\(\operatorname{Re}(1-v^2)>0\); the positive real square root
\(f=\sqrt{1-v^2}\) extends analytically to this whole disk and has
modulus less than 2. Formula (4) is used with R=3/4, M=2.

For the real derivative bounds, v' has quadratic Bernstein controls
\([b,3V-b,0]\), while v'' is affine and v'''=6(b-2V). Let d_j be
the resulting exact upper bounds on their absolute values, and use
\(f>9/10\). Direct differentiation gives

\[
 |f'|\le Vd_1/(9/10),
\]

\[
 |f''|\le d_1^2/(9/10)^3+Vd_2/(9/10),
\]

\[
 |f'''|\le3Vd_1^3/(9/10)^5
 +3d_1d_2/(9/10)^3+Vd_3/(9/10).
\]

The actual rational gates prove these are respectively less than
1/4, 1 and 4. Equations (2) and (3) therefore pay the entire Hermite
height integral, including its two endpoint derivatives. The Hermite
radial primitive is polynomial and introduces no Gauss quadrature cost.

## 5. Angular pieces and constant coasts

The already proved actual phase bounds are
\(|\phi|<8/5\), \(|\phi_u|<4\), \(|\phi_{uu}|<65\), and
\(|\phi_{uuu}|<3300\). For f=sin(phi) or cos(phi), these imply

\[
 (M_0,M_1,M_2,M_3)=(1,4,81,4144).
\]

The pinned implementation splits a flat turn at 0, epsilon,
1-epsilon and 1, with epsilon the exact binary value of .08. The
normalized span d of a complete smooth subpiece is therefore epsilon,
1-2epsilon, or 1 for an unsplit brake. After normalizing the subpiece,
use \((1,4d,81d^2,4144d^3)\) in (2).

On each fixed normalized subpiece, the earlier phase certificate proves
analyticity on the disk of radius2 about 1/2 with modulus below2^20.
Use (4) with R=2 and M=2^20. The actual parent piece length is greater
than27/10000. Thus a normalized primitive error vector B converts to
physical errors \((LdB_0,B_1,B_2/(Ld))\). The code keeps d explicitly
when paying the last quotient; it does not divide by the wrong parent
length or forget the ramp factor.

The total nonconstant angular length is below4. A constant coast has
exact-table error \(LE_c|f|\), first-derivative error \(E_c|f|\), and
zero second-derivative error. For these two actual profiles, all coast
lengths sum to less than

\[
 C+\frac{42}{25v_d}
 +\frac{2(q-1)R_{\rm loop}}{v_{\rm loop}}
 +\frac{10R_{\rm loop}}9<4.
\]

Here the first inward leg uses the already proved radial interval
(3/25,9/5); the two symmetric loop turns have zero radial displacement;
the terminal coast starts below R_loop, ends at a positive radius and
has speed magnitude greater than9/10. These facts follow from the
actual pinned construction, the proved positive coast margins and
the bound on its terminal angle. All inequalities are rechecked on
the two actual profile records.

## 6. One common anchor and the remaining work

For the value error, sum the Hermite length cost, all nonconstant
angular length costs, and all constant coast costs. The same accumulated
anchor is used throughout; no independent segment recentering is
allowed. For first and second derivatives, take the maximum over the
active piece. These exact sums and maxima prove (1).

At a quadrature split, Q itself is continuous: the preceding partial
piece becomes a fixed full contribution and the new partial piece
starts with width zero. Its derivative need not match, so the proof
retains the explicit two-sided jump bounds. The production provider
also supplies analytic velocity and acceleration separately from the
quadrature radius; those supplied jets do not automatically equal
the derivatives of its quadrature expression. The bound here quantifies
that integration-rule mismatch in the ideal aligned setting. It does
not silently resolve the floating or seam realization.

The owned producer formally exited0 in0.326707154 seconds, peak12,416 KiB,
with45 exact rational or identity gates. The primary SHA is
dfed27e391db068a17e109e6e843b92b5bdbdec12990ebd234453981cfee05a7.
There were zero ODE, Node or Newton calls. The full reproducible command,
actual accepted identities, source identities, rational coefficients,
individual table and ideal-Gauss charges, and remaining unpaid costs
are saved in the primary and resource record.
