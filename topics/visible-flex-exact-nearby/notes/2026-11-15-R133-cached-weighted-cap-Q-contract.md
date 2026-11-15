# R133 cached weighted Q consumer: exact inputs and scope

2026-11-15. This is a new, limited numerical consumer of the already completed
cap certificates. It does not execute an old target, coefficient convolution,
residual enclosure, reference Riccati equation, physical endpoint moment, or
source integral.

The mathematical object is fixed physical $\eta_0$, the original ac1 candidate
and its 440866 continuous repair, on $[L,R]=[9/10,25/8]$. The intrinsic
$\nu$ bump is identically zero here. Parameter offset zero means the fixed
physical $\eta_0$, not physical parameter zero. The original coefficient
enclosures at half width $10^{-9}$ cover this object. No nonzero $\delta$ or
unknown background is transferred.

## Q1. Original evidence

The native complete positive coefficient file has 4650 closed rows and SHA256
ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d.
Its 6223338 original gzip bytes are restored by joining the payloads of its
four existing byte parts. Every compressed byte hash, payload hash, original
offset, and complete container hash is checked. No new parts are created.

The original all-mode physical cap certificate is
ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b.
Its 949 reference rows, 1346 complete closed intersections, complete two-sided
$Q_B$ and $Q_C$ coefficient envelopes, exact parameter, and original intrinsic
cache identity are retained. Every selected positive row must have the original
same_intrinsic_cap_v2 provenance.

The original candidate index is
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413.
Only its existing part004 is read:
314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c.
This part contains intervals 5384 through 6143 and the whole true cap.
The exact dyadic knots and the descending PPoly ordering are verified.
The only newly enclosed candidate component is slot32, the actual even mean.
The other 64 slots are not recomputed as Fourier products.

Continuous repair and the actual inverse-angle bound come from
35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff.
The original producer is pinned as well: it constructs the raw moving $U,V$
bounds and repair on width $1/32$, although the output field names also state
the allowed resulting physical width $1/64$.

The completed L1/endpoint run is 43692857656/1, child return code0 and all12
scientific gates. Its exact process and genuine summary are pinned; the summary
SHA is f5eea9a8a1b3f198e19c94a42cc3f794226b99cae65cefbd2e631134aff42c3a.
Neither its 7296 original residual rows nor its new cap source integrals are
recomputed by this consumer.

## Q2. The single new polynomial enclosure

On an exact common cell $[a,b]$ within one original cubic piece with left knot
$x_0$, write the original binary64 coefficients as exact rationals:
$$
 p(x_0+t)=c_0+c_1t+c_2t^2+c_3t^3.
$$
With $x=a-x_0$ and $h=b-a$, the normalized cell polynomial has coefficients
$$
 d_0=c_0+c_1x+c_2x^2+c_3x^3,\qquad
 d_1=h(c_1+2c_2x+3c_3x^2),
$$
$$
 d_2=h^2(c_2+3c_3x),\qquad d_3=h^3c_3.
$$
Its four Bernstein controls are
$$
 d_0,\quad d_0+d_1/3,\quad
 d_0+2d_1/3+d_2/3,\quad d_0+d_1+d_2+d_3.
$$
The maximum of their exact absolute values, multiplied once by the original
exact $\alpha$, bounds $|\alpha p_{32}|$ on the whole closed cell. Arithmetic
through these four controls is rational; conversion to Arb is outward.
No difference of two independent interval means is used.

## Q3. Raw complete row totals

Let $U_i$ and $V_{\ne0,i}$ be the original whole-row moving Wiener bounds,
$K_i$ the original intrinsic interval, and $s_i=1/C_{\rm ref,i}$. Define
$$
 D_{v,i}=|\alpha p_{32}|_i+V_{\ne0,i},\qquad
 L_{B,i}=2U_i,
$$
$$
 L_{C,i}=U_i^2+|K_i|\bigl(2|s_i|D_{v,i}+D_{v,i}^2\bigr).
 \tag{Q.1}
$$
This follows from $Q_B=2u$ and
$Q_C=\ell-u^2-Kv^2=-u^2-K(2s(v-s)+(v-s)^2)$ with $\ell=Ks^2$.
The scalar $s$ is the same intrinsic reference as in the original rows.
All means are retained; only the known odd $u$ has its prescribed zero mean.
$U_i$ already contains the physical amplitude, so no second $\alpha$ is applied.

## Q4. Exact common partition and directed radial weight

The common partition includes the clipped4650 edges, all949 reference edges,
the original1346 closed-cover edges, and all original candidate knots in the
cap. A cell must lie in its original candidate germ and original true scalar
germ. Its union is the exact $[9/10,25/8]$, with neither gaps nor overlaps.

For the original positive $s_{C,i}$ lower bounds, set
$$
 S(r)=\int_r^R s_C(t)\,dt,\qquad w(r)=e^{-2S(r)}.
 \tag{Q.2}
$$
The reverse sweep keeps a directed lower bound for $S$ at each right endpoint.
It multiplies the original lower rate by the exact common cell length. Since
$w$ increases, $w(b_i)$ is an upper bound for $w$ on that complete cell.
The exponential is rounded upward. No reference differential equation is solved.

## Q5. Joint norm: maximum before sum

Write $a_{B,k},a_{C,k}$ for the original complete global envelopes. Each mode
has the valid local upper bound
$$
 |(Q_B)_k(r)|\le\min(a_{B,k},L_{B,i}),\qquad
 |(Q_C)_k(r)|\le\min(a_{C,k},L_{C,i}).
$$
First compute, separately for every two-sided mode including the mean,
$$
 A_{B,k}=\max_i w(b_i)\min(a_{B,k},L_{B,i}),\qquad
 A_{C,k}=\max_i w(b_i)\min(a_{C,k},L_{C,i}).
 \tag{Q.3}
$$
Only afterwards sum the angular weights. In particular a maximum of whole-row
Wiener sums is never promoted to the joint sum of radial suprema.

Let $\sigma=1/8192$ and let $h_*$ be the original repaired inverse displacement
in joint $A_{1/64}$. The new gate verifies
$$
 h_*+\sigma<1/64.
$$
Using the same repaired inverse angle for both the raw and repaired fields,
the standard exponential series in this Banach algebra gives
$$
 \|wQ_B^{\rm raw}\circ\Phi\|_{\mathscr A_\sigma}
 \le\sum_{k=-32}^{32} A_{B,k}e^{4|k|(h_*+\sigma)},
$$
$$
 \|wQ_C^{\rm raw}\circ\Phi\|_{\mathscr A_\sigma}
 \le\sum_{k=-64}^{64} A_{C,k}e^{4|k|(h_*+\sigma)}.
 \tag{Q.4}
$$
The radial scalar weight commutes with the composition. The finite support is
used only for these known coefficient fields, never for the unknown solution.

## Q6. Complete repair

Let $E$ be the original joint pair repair at width $1/32$, and let $U_*,V_*,K_*$
be the original complete bounds at the stated compatible widths. Their input
producer is pinned, and the new consumer explicitly checks $E<4.832\,10^{-18}$,
$U_*<1/50$ and $V_*<6$. The same inverse angle and $w\le1$ give the additional
fees
$$
 \Delta_B=2E,\qquad
 \Delta_C=2U_*E+E^2+K_*(2V_*E+E^2).
 \tag{Q.5}
$$
Both complete means and all repair coefficients remain present. These are
added to (Q.4); no repair fee is subtracted from an old independent upper bound.
The required actual gate is
$$
 \max(\|wQ_B\|_{\mathscr A_\sigma},\|wQ_C\|_{\mathscr A_\sigma})<10^{-5}.
 \tag{Q.6}
$$

## Q7. Existing endpoint kernel and scalar compatibility only

The conditional theorem is
[R133 weighted endpoint invariance](../results/R133-supplement-weighted-Q-endpoint-invariance-and-small-analytic-cap-ball.md),
SHA256 0e6c0f6acfa4a40378176cf56e03ee941d1932885149a64cd145a7b4e9b91cfe.
The endpoint moment and tail inputs are
[original complete physical endpoint F9--F20](../results/R133-supplement-final-moving-centre-actual-regular-boundary.md),
SHA256 f4ae237c86542f29f2127f7e43d5ab97827756fcce86e71bcff8c0a610ec81af.

The original completed L1 summary supplies $T_{DC}$ directly. The old cap
supplies $T,q_+,K_C$. The consumer checks
$$
 K_e=T_{DC}T+(1+q_+T_{DC})K_C<5.
 \tag{Q.7}
$$
It does not recompute the L1 endpoint integral or its prefix supremum.
It also consumes the same successful larger outer ball and its independent
mean derivative, retaining the complete reference source and boundary units.

Small positive-width source factors, original analytic endpoint tails,
known affine source loads and the fixed rational radii are only scalar
checks from the pinned conditional endpoint theorem. The finite-mode
weights are not applied to an unknown infinite source. The source code
will explicitly retain every original infinite tail in these scalar checks.

For these scalar checks, original F9--F20 give the exact safe inputs
$$
 U_{1/8}<1.643190\,10^{-9},\qquad
 P_{1/8}<1.480385\,10^{-11},\qquad |m|>5.8.
$$
Set $d=1/8-P_{1/8}$, $x=e^{-4(d-\sigma)}$ and $J=128$. Both complete tails are
retained using
$$
 T_C=\frac{8P_{1/8}}{5.8}
       \frac{x^{J+1}[(J+1)-Jx]}{(1-x)^2},\qquad
 T_B=\frac{2U_{1/8}}{5.8}\frac{x^{J+1}}{1-x}.
 \tag{Q.8}
$$
The new scalar gate checks $x<2/3$ and $T_B+T_C<10^{-30}$. The finite weight
$e^{512\sigma}$ multiplies the old complete regular and $Z$ upper bounds;
adding these new tails only overcounts their old tail contributions and never
subtracts two independent upper bounds. The original regular-multiplier
comparison is also kept.

The complete first differential of the physical change of variables along the
original repair path gives
$$
 \Delta B\le(C+BC+B_\theta C/4)E,\qquad
 \Delta C\le(C^2+C_\theta C/4)E.
 \tag{Q.9}
$$
Here $C,B,C_\theta,B_\theta$ are the nonnegative original full norm bounds
from the successful L1 summary, and the independent right $C$ mean change is
read from the original35db certificate. The weighted primitive constant
vanishes only for the stipulated odd/even known repair path.

The complete smaller long graph is evaluated by its original scalar
majorant at $z=10^{-12}$ and $b=2^{-60}$, with
$r_f=10(z+b)$, $F=r_f+b$ and the same nonzero safe reflection
$\epsilon=2^{-256}$. Its full value contributions are bounded by
$\epsilon z+\epsilon b+2^{14}F^2$ and $2^{11}F^2$, after all original domain
and image gates are checked. This uses the true graph at the repaired input;
it does not also add a second difference of that graph.

The newly widened known affine loads are
$$
 \eta_\sigma=e^{384\sigma}\eta_{\rm body}
             +H_C\,10^{-9}+H_D r_D+r_{C0},\qquad
 e_\sigma=e^{384\sigma}e_{\rm body}
             +a_L\,10^{-9}+T_{DC}r_D.
 \tag{Q.10}
$$
The consumer checks their stated $3.23\,10^{-7}$ and $3\,10^{-14}$ margins,
the complete even mean and the fixed rational conditional body/endpoint
inequalities. All these are scalar consumptions of prior complete certificates.
They do not repeat an original integral.

The independently proved conditional theorem uses the full unknown linear
$Q$, quadratic $Q$, outer graph feedback, the independent even mean and the
true inner nonmean data. This consumer reports its new coefficient and scalar
gates; it does not relabel a known-source endpoint bound as complete invariance
or declare a whole PDE solution. The coordinator must separately apply the
complete theorem with the actual successful result.

## Q8. Public execution and storage

The immutable manifest fixes every scientific byte and runtime. Old deleted
inputs are restored only to temporary runner storage from the explicit public
history commit. The original four byte parts are reassembled exactly in memory.
No old numerical producer is called.

Before any scientific child, the worker checks the current topic tree at the
actual pulled commit. Exact Git path/SHA metadata are compared with GitHub tree
size metadata; the file byte sum must be at most200000000. This avoids the
partial-clone behavior of ls-tree -l, which can fetch blobs merely to find sizes.
An over-budget result is a real failure with a small receipt; no unknown file
is silently deleted.

All new cell arrays and per-mode arrays are temporary and only their output
SHA/bytes are persisted. Actual script/parameters/run, finite gates, source
identities and genuine summary are retained below60000 UTF8 bytes per file.
No new Actions artifact or Release data is uploaded. A failed mathematical
gate remains a failure. Success reuse requires exact science identity and the
actual child0/full-gate receipt, even if an old publication step failed.
