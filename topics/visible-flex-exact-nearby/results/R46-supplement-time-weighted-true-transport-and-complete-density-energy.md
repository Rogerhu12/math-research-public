# R46 supplement: a true time weight for the full density transport

The exact first-derivative energy used here is

$$
 \mathcal E^2=\|\sqrt\lambda u\|_2^2+
                  \|Y_+\|_2^2+\|Y_-\|_2^2,\qquad \lambda=9,
 \quad
 Y_\sigma=\frac{\sqrt\mu\,u_\theta+\sigma p/\sqrt\mu}{\sqrt2}.
                                                               \tag{TW.1}
$$

It is the same complete physical energy as in
[the unshifted-density theorem](R46-supplement-unshifted-density-energy-and-full-mean.md).
The full original \(u\), its mean, the mean momentum and all other
angular modes are retained. The present change is to the estimate
of its principal transport, using the actual complete characteristic
reference and its already paid true-flow error.

The complete native calculation has passed all 550 segments and all
four gates. Uniformly on the original whole real parameter interval,
the complete physical energy has the two-sided Cauchy/source growth
\(G<7.067454946\cdot10^{10}\), with
\(\log G<24.981351365658\). This improves the preceding complete
energy bound by a factor greater than \(5711.18\), without discarding
the height mean, the mean momentum or any finite angular mode.

## 1. Put the full height row in the bounded interaction

Write \(\ell=\log\mu\), \(m=\mu^{-1/2}\), \(v=b/a\) and
\(\nu=\mu/a>0\). The exact full operator, physical momentum and
source are

$$
 Pu=\partial_r(au_r+bu_\theta)+
            \partial_\theta(bu_r+cu_\theta)+du=f,\qquad
 p=au_r+bu_\theta.
$$

The complete equations from the preceding theorem are

$$
 (Y_\sigma)_r+\partial_\theta[(v-\sigma\nu)Y_\sigma]
   =\frac{\ell_r+(v+\sigma\nu)\ell_\theta}{2}Y_{-\sigma}
       +\frac{\sigma(f-du)}{\sqrt{2\mu}}.                 \tag{TW.2}
$$

There is also an exact bounded full height equation:

$$
 \sqrt\lambda u_r
 =\frac{\sqrt\lambda}{\sqrt{2\mu}}
       [(\nu-v)Y_+-(\nu+v)Y_-].                         \tag{TW.3}
$$

Indeed \(u_\theta=(Y_++Y_-)/\sqrt{2\mu}\), so this is just
\(u_r=\nu(Y_+-Y_-)/\sqrt{2\mu}-v u_\theta\).
No angular antiderivative or projection was used. In particular
it holds on the height mean as well as on the nonzero modes.
This step removes the need for a third, independently estimated
height transport.

In the Hilbert direct sum
\(X=(\sqrt\lambda u,Y_+,Y_-)\), choose the uncoupled propagator
to be the identity on the first component and the two true
scalar-density transports on the others. The remaining
zero-order operator \(\mathcal B(r)\) has the complete positive
two-block majorant

$$
 \begin{pmatrix}0&A(r)\\B(r)&C(r)\end{pmatrix},\qquad
 A\ge\sup_\theta\sqrt{\frac{\lambda(\nu^2+v^2)}{\mu}},
 \quad
 B\ge\sup_\theta\frac{|d|}{\sqrt{\lambda\mu}},
$$
$$
 C\ge\frac12\sup_\theta
       (|\ell_r|+(|v|+\nu)|\ell_\theta|).                 \tag{TW.4}
$$

The blocks in this majorant refer to the full height and the
full two-wave pair. For example the exact height row has
pointwise Euclidean norm
\(\sqrt{\lambda(\nu^2+v^2)/\mu}\), and its reverse column
has norm \(|d|/\sqrt{\lambda\mu}\). The two-wave off-diagonal
block has norm at most \(C\). Thus

$$
 \|\mathcal B(r)\|\le k(r):=
 \left\|\begin{pmatrix}0&A\\B&C\end{pmatrix}\right\|_2.     \tag{TW.5}
$$

Writing \(t=A^2+B^2+C^2\), the exactly evaluated expression is

$$
 k^2=\frac{t+\sqrt{(B^2+C^2-A^2)^2+4A^2C^2}}2.           \tag{TW.6}
$$

The source in this state is exactly
\((0,mf/\sqrt2,-mf/\sqrt2)\), of norm \(\|mf\|_2\).
It is the original ordinary scalar in physical \(dr\), without
any weak-load substitution.

## 2. A time weight from the same entire exact reference

Use the complete reference and the actual true-flow identity of
[the same-label Jacobian theorem](R106-supplement-complete-same-label-real-relative-Jacobian.md).
Let \(F(\tau,x,p)=4\Theta(\tau,x,p)\) be the actual normalized
flow, and put

$$
 q(\tau,x)=1+4\,\partial_x U(\tau,x)
$$

for the derivative of the same complete finite degree-seven
Fourier/Bernstein reference. Here \(q\) is only the finite
reference; it is not declared to be the true Jacobian.

For each original segment \(I_i\), the already proved full
retarget fees and true-flow error give

$$
 |F_x-q|\le E_i,\qquad
 E_i=4\max_j(e_{i,j}+\epsilon_J),\qquad
 \epsilon_J=\frac{655848592}{254021484375}.               \tag{TW.7}
$$

All these bounds hold on the entire real parameter interval.
Suppose the complete calculation proves

$$
 q\ge q_{i,-}>E_i,\qquad
 |\partial_\tau\log q|\le L_i
 \quad\hbox{on }I_i\times\mathbb S^1.                    \tag{TW.8}
$$

Set

$$
 \delta=\max_i E_i/q_{i,-}<1,\qquad
 D_e=\sqrt{\frac{1+\delta}{1-\delta}},\qquad
 w(\tau)=\frac12\int_{-\pi/2}^{\tau}L(s)\,ds,             \tag{TW.9}
$$

where \(L\) is the nonnegative segmentwise constant \(L_i\).
The exact Bernstein seams ensure that \(q(\tau,x)\) is continuous
in \(\tau\) for each \(x\); its piecewise derivative is sufficient.
Therefore, for every two times and the same original label,

$$
 \frac{F_x(t,x,p)}{F_x(s,x,p)}
 \le\frac{1+\delta}{1-\delta}
       \exp\left|\int_s^tL(\tau)\,d\tau\right|.          \tag{TW.10}
$$

The reciprocal satisfies the identical estimate. The exact
relative-map derivative is the ratio on the left of (TW.10),
evaluated at the appropriate common label. Ordinary real
change of variables consequently gives

$$
 \|\mathcal D_\sigma(r,s)\|_{L^2\to L^2}
 \le D_e\exp|w(\tau(r))-w(\tau(s))|.                     \tag{TW.11}
$$

This is a bound for the actual full density propagation in both
directions, at every pair of interior times. The exact radial
substitution \(r=t(p)\sin\tau\) is monotone on the whole leg.
Its parameter dependence causes no extra source Jacobian in
(TW.11): the propagation estimate is indexed by \(r\), and
the ordinary Duhamel source continues to be integrated in \(dr\).
Reflection supplies the other characteristic branch, as in
the cited original theorem.

No bound for a complex derivative or a wider complex strip is
inferred from (TW.8)–(TW.11).

## 3. How every cell in (TW.8) is paid

All original 550 segments, eight controls, complete Fourier
coefficients and exact dyadic seams are consumed. At the 4096
centers \(x_n=2\pi n/4096\), native directed Arb DFTs enclose
both \(q_j(x_n)\) and \(\partial_xq_j(x_n)\). No finite
Fourier mode is removed, and the grid exceeds twice the
complete stored Fourier degree.

For \(h=\pi/4096\), let
\(M_{2,j}=2\sum_{k\ge1}k^2|\widehat q_j(k)|\).
Taylor's formula gives on the entire closed angular cell

$$
 |q_j(x)-q_j(x_n)|
 \le h|\partial_xq_j(x_n)|+\frac{h^2}{2}M_{2,j}.          \tag{TW.12}
$$

The full finite sum \(M_{2,j}\) bounds the second derivative at
every real angle; no true-flow derivative is substituted here.
The minimum of the eight lower bounds in (TW.12) is a lower
bound for the reference at every time in the segment.

If its exact duration is \(\Delta\tau_i\), the complete
time derivative has the seven Bernstein controls

$$
 q_{\tau,j}=\frac7{\Delta\tau_i}(q_{j+1}-q_j),
 \qquad j=0,\ldots,6.                                   \tag{TW.13}
$$

Differences in (TW.13) are taken using the exact full
coefficients. For each derivative control, the same
second-order angular Taylor estimate uses its complete
second-derivative Fourier sum. The node values and first
angular derivatives are the directed differences of the
already computed DFT values. The maximum of their complete
closed-cell upper bounds bounds \(|q_\tau|\) at every
intermediate time. Dividing by the positive reference lower
bound on that same cell proves \(L_i\); taking extrema over
all cells proves (TW.8).

The positivity check precedes both divisions. The true-flow
and retarget fees in (TW.7) remain separate from finite
reference differentiation. No derivative of a merely
bounded true-flow error is required.

## 4. Full Cauchy and ordinary source estimate

The uncoupled three-component propagator has norm at most
the right side of (TW.11), since its height block is the
identity and that right side is at least one. Apply the
exact Duhamel formula to (TW.2)–(TW.3). On a forward
interval multiply its norm inequality by
\(e^{-w(\tau(r))}\). The resulting Volterra inequality
has kernel \(D_e k(r)\). Gronwall gives

$$
 \mathcal E(r)\le
 D_e\exp\left(
      |w(\tau(r))-w(\tau(s))|+
      D_e\int_s^r k(t)\,|dt|\right)
 \left(\mathcal E(s)+\int_s^r\|m(t)f(t)\|_2\,|dt|\right).
                                                               \tag{TW.14}
$$

Reversing time proves the identical two-sided statement.
For a full strict interval let

$$
 Q=\int k(r)\,dr,\quad
 W=\frac12\sum_i\Delta\tau_i L_i,\quad
 G=D_e e^{W+D_eQ}.                                      \tag{TW.15}
$$

Using all 550 reference segments in \(W\), even where the
strict cuts exclude small end pieces, is a valid enlargement.
Every strict subinterval and both directions are bounded by
this same \(G\).

The 215 original positive strict cells and their exact
reflection give \(Q\). The upper moduli and positive density
lower bounds in (TW.4) are the original complete complex-field
bounds restricted to real angles; there is no recomputation
of an approximate field. Both halves' physical lengths are
included exactly once.

Equation (TW.14) is applied to the already existing actual
physical solutions. It does not assert that arbitrary
incompatible three-component initial states are physical
gradients. It supplies a new a priori estimate for the same
complete physical Cauchy/source realization.

## 5. Unchanged physical, amplitude, mean and source interfaces

Keep the old positive density bounds and the exact energy
comparisons \(h_-(N),h_+(N)\), the complete original frame
bound \(F_N\), and the old density conversion constants
\(W_E,Y_E\) from the unshifted-density theorem. They do not
depend on which propagation estimate was used to obtain \(G\).
The entire physical and ordinary-source bounds are

$$
 C_{1/2}(N)=G\sqrt{h_+(N)/h_-(N)},\qquad
 S_{1/2}(N)=\frac{G}{\sqrt{\mu_-h_-(N)}}.                 \tag{TW.16}
$$

The first bound holds at negative half order by the actual
reverse flux adjoint, and at every intermediate order by
interpolation of the same complete realization. The exact
old amplitude and inverse at base order obey

$$
 C_{\rm amp,0}(N)\le F_N^2C_{1/2}(N),\qquad
 S_{\rm amp,0}(N)\le F_N C_{1/2}(N).                     \tag{TW.17}
$$

The latter uses the original ordinary
\(L^1(dr;H_N^{-1/2})\) source. Optimizing this comparison
scale does not change the original amplitude space or
operator. The scale embedding in the preceding theorem
is unchanged.

The complete old-density base columns for the higher
bootstrap are

$$
 (M_C,Y_{0,C})=(W_E,Y_E)\,G\sqrt{h_+(N)},\qquad
 (M_S,Y_{0,S})=(W_E,Y_E)\,\frac{G}{\sqrt{\mu_-}}.          \tag{TW.18}
$$

The source has its physical \(dr\) measure throughout,
and no time derivative of \(f\) is required. All original
height, momentum, mean, finite-head and ordinary-source
rows remain in (TW.16)–(TW.18).

## 6. Executed native calculation and scope

The source is
`scripts/fourfold_strict_time_weighted_true_transport.py`.
It checks the same object, entire affine parameter interval,
the exact full reference and retarget descriptor, all
original shard hashes and 549 exact joins, and the complete
reference error and native field dependencies. Every
reference derivative and cell fee is computed in directed
192-bit Arb arithmetic. Each segment's strict lower bound,
true error, complete log-slope and exact-time integral is
saved, together with the complete 215 physical interaction
blocks and all old-frame/source comparison rows.

The executed 192-bit report is
`notes/2026-11-13-R46-time-weighted-true-transport.json.gz`.
Its complete native bounds, rounded outward here, are:

| Quantity | Bound |
| --- | ---: |
| Complete true/reference relative error \(\delta\) | \(<0.085943357990954\) |
| True transport error factor \(D_e\) | \(<1.089976243169\) |
| Full reference log-slope integral \(2W\) | \(<17.420805111336\) |
| Complete physical interaction integral \(Q\) | \(<14.848757494201\) |
| Complete energy logarithm \(\log G\) | \(<24.981351365658\) |
| Complete energy Cauchy factor \(G\) | \(<7.067454946\cdot10^{10}\) |
| Ordinary \(L^1(dr;L^2)\) source to energy | \(<2.117486178\cdot10^{11}\) |
| Improvement over the previous complete energy | \(>5711.18\) |

The comparison scale \(N=1\) gives, for the very same original
physical and amplitude realization,

$$
\begin{aligned}
C_{[-1/2,1/2]}(1)&<5.054623950\cdot10^{11},\\
S_{1/2}(1)&<2.831414747\cdot10^{11},\\
C_{\mathrm{amp},0}(1)&<2.792096594\cdot10^{20},\\
S_{\mathrm{amp},0}(1)&<1.187981411\cdot10^{16}.
\end{aligned}                                                   \tag{TW.19}
$$

The source in the last line has its original
\(L^1(dr;H_1^{-1/2})\) norm. The report also saves every requested
comparison row through \(N=2^{20}\), both old-density mean columns,
and both old-density wave columns. These are full-state bounds;
the displayed scale does not introduce a Fourier cutoff.

The first launched native process was interrupted before producing
a final report. Its last observed progress, absent final output and
original source identity are retained in
`notes/2026-11-13-R46-time-weighted-true-transport-attempt01-interrupted.json`.
The completed invocation reconsumed all 550 segments from the original
exact reference, checked every one of the 549 dyadic seams, and
finished normally in 609.76 seconds. The source now saves a small
SHA-bound consecutive-prefix checkpoint every five segments; this
completed invocation did not resume a saved prefix. The interrupted
attempt is not a failed mathematical gate and is not counted as a
certificate.

The completed source SHA-256 is
`104e9859fe8029d72c822ac091f0b70d72989f79d78d008de7ea3de326df9c0e`;
the compressed final report SHA-256 is
`7e7a8e21c4788532678218e1b04c70ce2aa401fdcc1e959cd1479219f88dbb8e`.
The decompressed JSON SHA-256 is
`3d33746658b0bbe1920fa72c401f2211b32797407daa9bda97cc0697cc37edfa`.

Reproduction from this topic directory uses a fresh output:

```sh
python3 scripts/fourfold_strict_time_weighted_true_transport.py \
  --out /tmp/strict-time-weighted-true-transport.json
```

The stronger density staircase and full returned strong
remainder require their subsequent explicit consumers.
This theorem does not solve the finite head, prove a full
feedback inverse, grant a new complex domain or transfer
old numerical constants to the new nonlinear body.
