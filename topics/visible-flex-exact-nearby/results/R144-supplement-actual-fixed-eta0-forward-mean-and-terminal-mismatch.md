# R144 supplement: the actual fixed-eta0 forward mean is positive but is not a nearby boundary-preserving centre

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved by the completed directed calculation.** Run
`45778507038/1` has completed the entire fixed-eta0, fixed-nu0 forward
mean target. Its reconstructed reciprocal mean is strictly positive
on the whole core. The same construction changes the moving state by
more than $10^{-4}$ and changes the physical outer curvature mean by
a strictly positive amount. These are certified violations for this
particular fixed-density retraction, not unresolved sufficient bounds.
They do not imply failure of the compact-density centre, singularity
of the full boundary problem, or nonexistence of the required family.

## 1. The exact object and the completed computation

This is the original piecewise raw candidate at

$$
 \alpha=\frac{6890507429876859}{9007199254740992},\qquad
 \eta_0=-\frac{7789843107295549}{4611686018427387904},\qquad
 \nu_0=-\frac{2572625729470897}{72057594037927936}.
 \tag{FM.1}
$$

The complete candidate has SHA256
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`.
The exact interval is $[0,R]$, $R=25/8$. The raw centre is neither
silently replaced by its continuous repair nor evaluated at the
selected implicit $\nu_0+\delta_*$.

Use the notation of
[the fixed-density subtraction theorem](R144-supplement-fixed-density-rotational-reference-subtraction.md),
(RS.1)--(RS.8):

$$
 m=\langle v\rangle_\phi<0,\quad j=v/m,\quad
 U=\langle u^2\rangle,\quad
 V=\langle(v-m)^2\rangle,\quad n=a^2/m^2.
$$

The retraction holds $u$ and $j$ fixed. It integrates

$$
 W'=2\beta UW+2\beta a^2
       \left(\frac{U}{s^2}+\frac{KV}{m^2}\right),\qquad W(0)=0,
 \tag{FM.2}
$$

and reconstructs

$$
 Y=W+\frac{a^2}{s^2},\quad D=Y-n,
 \qquad m^\flat=-\frac a{\sqrt Y},\qquad
 Q^\flat=(u,m^\flat j).
 \tag{FM.3}
$$

The identity theorem cited above proves that this is exactly the
waist-normalized, fixed-density mean retraction. In particular its
initial mean difference, signed bulk mean residual and all original
mean jumps remain in the reconstructed $D$; $W(0)=0$ has not discarded
them.

The executing source is
[`fourfold_codazzi_fixed_eta0_correlated_mean_retraction.py`](../scripts/fourfold_codazzi_fixed_eta0_correlated_mean_retraction.py),
SHA256
`b3e7b85933f6d1e5bae7f39b3a84a98a0d9a8db11255d22d9cefa0edc1a6bd4b`.
The exact inputs and the interval method are specified in the
[execution contract](../notes/2026-11-26-R144-fixed-eta0-correlated-mean-contract.md)
and [manifest](../notes/2026-11-26-R144-fixed-eta0-correlated-mean-inputs.json),
whose SHA256 is
`e99e081cd404c36e9f754c0839e9f8f7d95502fffa2db02bff093fe90a0599a8`.
The calculation uses 320-bit ball arithmetic, 512 primitive nodes,
degree-24 local source expansions and Cauchy radius eight times the
subcell halfwidth, retaining the full angular primitive tails and
radial remainders.

The [complete scientific result](../notes/fixed_eta0_mean_retraction_ci/run-45778507038-1/fixed-eta0-correlated-mean-retraction.json)
is 9273 bytes, SHA256
`c45df5750f1e888998d6b3ff47714fa23aa5b4c0163bcdb060bc3ba42cc9b124`.
The [execution receipt](../notes/fixed_eta0_mean_retraction_ci/run-45778507038-1/execution.json)
is 16188 bytes, SHA256
`aea8f0c0a908d730f2df7288357150c81f2d892dad090a11e7d6690c5a68a1fc`.
It records one scientific child, return code zero, no timeout and
no scientific failure. The target covers all 7296 common closed rows,
all 6144 original raw pieces and all 6143 mean interfaces, using
14668 accepted subcells. Its final point is exactly $25/8$; this is
not a prefix or a request for continuation. No old completed residual,
response, mean-Green or angular-solver target was called again.

## 2. Whole-core positivity and the failure of the moving-state gate

Every saved decimal ball denotes the interval

$$
 [(M-r)10^e,(M+r)10^e],
 \tag{FM.4}
$$

with the actual stored integers $M,r,e$. All inequalities below use
its outward endpoint, not its displayed midpoint. The saved minimum
over the complete closed subcells gives

$$
                  Y(r)>1.2574\,10^{-12}>0
                  \quad(0\le r\le R).
 \tag{FM.5}
$$

Thus the negative square-root branch in (FM.3) exists everywhere.
The complete field is evaluated with both one-sided raw values at
each original join. No assertion of nonmean continuity follows from
the continuity of this scalar $Y$.

At common row 7147 the saved directed witness is at the exact point

$$
                r_w=\frac{1542482872374395}{562949953421312}.
 \tag{FM.6}
$$

Its stored lower-ball midpoint integer is

~~~text
10019558906813269376450245856585536005869915268243265701743612580094109885396570
~~~

with radius integer $2$ and decimal exponent $-83$. Consequently

$$
 |m^\flat(r_w)-m(r_w)|
   >1.0019558906813\,10^{-4}>10^{-4}.
 \tag{FM.7}
$$

To explain why this is a state-distance lower bound, the unchanged
density satisfies $\langle j\rangle_\phi=1$. Hence

$$
 \left|\left\langle v^\flat-v\right\rangle_\phi\right|
  =|m^\flat-m|
  \le\|v^\flat-v\|_{C^0_\phi}.
 \tag{FM.8}
$$

The witness therefore certifies failure of the complete unnormalized
moving $C^0(r,\phi)$ gate. It is not an inference from a large upper
bound and does not concern a different fixed-physical-angle norm.
Here the actual material chart itself is unchanged because it depends
only on $j$.

There is also a stronger endpoint lower bound. The saved full ball
for `mean_shift_at_current_right` yields

$$
 -7.665841\,10^{-3}
 <m^\flat(R)-m(R)
 <-7.665839\,10^{-3}.
 \tag{FM.9}
$$

For scale, the saved whole-core state upper bound gives

$$
 \|v^\flat-v\|_{C^0(r,\phi)}<7.668937\,10^{-3}.
 \tag{FM.10}
$$

The source obtains this upper bound from the complete Fourier
majorant in (RS.20), on every closed subcell, including the mean.
The $u$ component is unchanged. The endpoint lower bound in
(FM.9) and the upper bound in (FM.10) refer to the same exact
fixed-density construction.

## 3. The physical outer mean is genuinely changed

The complete moving-to-physical mean identity is
$\langle C\rangle_\theta=1/m$. Therefore (RS.22) gives

$$
 \langle C^\flat\rangle_\theta(R)
      -\langle C\rangle_\theta(R)
 =-\frac{D(R)}{a(R)(\sqrt{Y(R)}+\sqrt{n(R)})}.
 \tag{FM.11}
$$

The saved full `physical_Cmean_shift_at_current_right` ball implies

$$
 2.2411927\,10^{-4}
 <\langle C^\flat\rangle_\theta(R)-\langle C\rangle_\theta(R)
 <2.2411930\,10^{-4}.
 \tag{FM.12}
$$

In particular it does not contain zero. The physical outer-mean row
is not preserved. This is a comparison with the original raw outer
state; it makes no assertion that the latter already matches a
genuine cap exactly.

For clarity about the amplified error, the same result has

$$
 -3.301986\,10^{-15}<D(R)<-3.301985\,10^{-15},
 \tag{FM.13}
$$

but (FM.11) contains the actual small outer radius and the actual
square roots. The tiny normalized reciprocal-mean difference in
(FM.13) therefore does not imply a tiny moving-state error or a
zero physical mean row. The full forward normalization has been
retained throughout.

## 4. Exact status and the continuing route

The final saved decisions are

| Full target or gate | Actual result |
|---|---|
| Complete fixed-eta0 target and all interfaces | Complete |
| Positive reconstructed reciprocal mean on the whole core | True |
| Complete moving-state distance at most $10^{-4}$ | False, by a directed lower witness |
| Unchanged physical outer curvature mean | False, by a signed ball excluding zero |
| Conjunction of these three gates (`proved`) | False |

The older full-eta row-range calculation had unknown gates; that
older record remains unchanged. The present exact-eta0 outcome
answers a different, previously unfinished target and needs no
remaining suffix run.

The [compact-density compensation](R144-supplement-compact-density-quadratic-mean-compensator.md)
changes $j$ on a compact interior window and then selects its
scalar root to restore the entire original outer point-state.
It is a different construction. Its already completed
[TM small-root result](R144-supplement-actual-terminal-mean-small-root-and-density.md)
and [LC whole-state result](R144-supplement-actual-localized-full-state-and-compact-sources.md)
are not contradicted by (FM.7)--(FM.12) and are not recomputed here.
Their remaining nonmean equations, full transmissions, genuine cap,
height, phase and fixed-metric existence obligations remain.

The present conclusion closes the raw fixed-density forward
calculation and rules out only its claimed nearby,
outer-mean-preserving use. It is not a final-topic result under
the README completion criteria.
