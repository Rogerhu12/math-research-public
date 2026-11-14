# R118: paid common strip, actual old-middle physical cap, and conditional infinite high inverse

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved on all 10793 original leaves.** A single actual strip with terminal width

$$0.015804967241529647\ldots>1/64$$

simultaneously supports the R117 hybrid finite-frequency comparison and the R93 complete source inverse with high threshold $M=34816$. Both changes of strip are paid through nondecreasing additional losses. The still uncomputed finite gap $5760,5762,\ldots,34814$ contains14528 positive even modes; the strip theorem does not solve their equations or claim the coupled fixed point.

## 1. Exact charges of the original two methods

Let $h_I\ge0$ be the complete continuous width loss of the R115/R117 strip on an original leaf $I$. It is exactly $\rho q_I\Delta_I$, $\rho=33/32$, with the R115 energy choice only on cell10/segment3.

For the same original positive R68 frames use the R93 notation $g_I,n_I^\pm,J_I^\pm,p_I^\pm$ and the identical exact positive-log algorithm. Set

$$
\epsilon=2^{-25},\quad L_I=\max(0,J_I^+-\epsilon),\quad
a_I=\max(0,n_I^+-L_I),\quad
c_I=(p_I^++p_I^-)/\Delta_I,\quad \kappa=2^{-18}.
$$

R93 gives $a_I+J_I^+\le p_I^++\epsilon$ and $c_I\ge s+|\ell|$. For any even $M\ge5760$, the original high construction has continuous loss

$$k_I(M)=g_I+a_I/M+\kappa(p_I^++p_I^-),$$

and an entering downward jump $J_I^+/M$. These are actual exact rational charges, with the same original frame on every leaf. The arbitrary $M$ version follows from the same proof as R93: for $|m|\ge M$, $m a_I/M\ge a_I$ and $mJ_I^+/M\ge J_I^+$.

The consumer independently reproduces the three R93 exact totals, rather than subtracting unrelated upper bounds:

$$\sum_I g_I=G_{\rm ph},\qquad \sum_I p_I^+=P_+,\qquad \sum_I p_I^-=P_-.$$

It also reproduces exactly $\sum_I h_I$, the R115 hybrid width loss. All four identities passed on the complete original source/frame streams.

## 2. A common strip with two monotone loss differences

Start $\sigma(b)=18/125$. On each leaf take continuous loss

$$\ell_I(M)=\max\{h_I,k_I(M)\},$$

and at its entrance pay the entire additional jump $J_I^+/M$. In other words,

$$-\sigma'=\ell_I(M)/\Delta_I\quad\text{inside }I.$$

Let $\tau_F$ be the original hybrid strip and $\tau_H^{(M)}$ the original high strip with threshold $M$. Their differences from $\sigma$ are

$$
\delta_F=\tau_F-\sigma,\qquad \delta_H=\tau_H^{(M)}-\sigma.
$$

On a leaf, $\delta_F$ increases by $\max(0,k_I-h_I)$ and $\delta_H$ increases by $\max(0,h_I-k_I)$. At entry, $\delta_F$ increases by $J_I^+/M$ and $\delta_H$ has no extra jump. Both differences start at0 and are nondecreasing on the entire source interval, including both sides of every interface.

The complete exact evaluation gives:

| High threshold $M$ | Common terminal width | Strictly above $1/64$ |
|---:|---:|:---:|
| 5760 | $-0.015697313337361796\ldots$ | no |
| 8192 | $-0.003939065250895164\ldots$ | no |
| 16384 | $0.009312010562954682\ldots$ | no |
| 32768 | $0.015462570291217136\ldots$ | no |
| 33792 | $0.015639526422496212\ldots$ | yes |
| **34816** | **$0.015804967241529647\ldots$** | **yes** |
| 65536 | $0.01811446770324772\ldots$ | yes |

The chosen $34816$ leaves a larger strict margin than the tested $33792$ while requiring only one more geometric frequency window. No minimality over all possible profiles or all even thresholds is asserted. The resulting extra finite-strip loss is

$$\delta_F(\mathrm{end})=0.0058317126673672216\ldots.$$

Because every continuous and jump charge is nonnegative, the terminal inequality also proves $\sigma(x)>1/64$ at every partial leaf position and on both sides of interfaces. Conversely, the old5760 profiles cannot be identified without a cost: the actual minimum of $\tau_F-\tau_H^{(5760)}$ is negative. Positivity of their two separate terminal widths was not a common-space argument.

## 3. Why both actual causal source inverses restrict

For any physical Fourier propagator $U_m(x,y)$ and $y\le x$, replacing a strip $\tau$ by $\sigma=\tau-\delta$ multiplies its weighted kernel by

$$
e^{-|m|(\delta(x)-\delta(y))}.
$$

For nondecreasing $\delta$ this factor is at most1. This is a statement about the entire weighted source kernel and its Duhamel integral, so it controls sources whose norm is given directly in $\sigma$; it does not assume that such sources belong to the wider-strip space. All physical component/frame conversions are unchanged.

Applying this with $\delta_H$ preserves the R93 pointwise attenuation bound

$$
e^{|m|\sigma(x)}\|U_m^u(x,y)\|_2e^{-|m|\sigma(y)}
\le \exp\left(-|m|\kappa\int_y^x c(t)\,dt\right),\qquad |m|\ge34816.
$$

The weak-to-strong source inverse on this actual common strip is consequently

$$
\|\mathcal G_H f\|_{X_H(\sigma)}
\le G_H\|f\|_{Y_H(\sigma)},\qquad
G_H=\frac{1+1/34816}{\kappa}=\frac{4456576}{17}.
$$

The spaces use the original R93 frames and $b_Ic_I$ source normalization, with all radial suprema inside the signed modal sum. The physical factors256 for the initial trace,18555 for the two separate output component suprema, and257 for a balanced derivative direction remain paid. None is removed by the strip change.

## 4. Exact reuse of every completed old finite window

The original126 window packets need no new source or ODE evaluation. Let $d_i^-$ and $d_i^+$ be the minimum and maximum of the nondecreasing $\delta_F$ on the original25 comparison block $J_i$. The exact new interface packet saves these two endpoints for every block, with both sides of jumps accounted for. For $j<i$ define

$$D_{ij}=d_i^- -d_j^+\ge0,$$

and take $D_{ii}=0$. If an old window $W=[m_-,m_+]$ has material bound $\gamma^{(p)}_{ijW}$, a valid bound in the shared strip is

$$\widetilde\gamma^{(p)}_{ijW}
\le e^{-m_-D_{ij}}\gamma^{(p)}_{ijW},\qquad p=2,1,0.$$

The initial-column target gains additionally receive $e^{-m_-d_i^-}$; this combines with the already paid true-head strip gap. Source positions within a diagonal block retain the old bound, since their ordered additional loss is nonnegative. Both genuine initial columns and all three materials remain present.

No exponent is assigned an unchecked floating-point value. One exact rational option is a positive Taylor lower bound for $e^z$. A faster outward dyadic option used by the new consumer is

$$e^{-z}\le(1+z/65536)^{-65536},\qquad z\ge0.$$

Round $(1+z/65536)^{-1}$ upward to96 dyadic significant bits, then square16 times, rounding upward after every square. Taking the minimum with1 is valid because the desired decay is also at most1. This provides a proved upper decay factor without the large unrelated rational denominators of the unrounded Taylor implementation. It changes no strip charge or mathematical gate.

The finite nonlinear budget still needs to consume these bounds. In particular, the conclusion of this section alone is not a statement that the new physical middle radius or all coupling rows passed.

## 5. Conditional nonlinear high response on the same space

Keep the same original real R74 parameters and the same complete low centre. R101 gives its physical norm at the constant strip at most $10\cdot2^{-40}$, hence the same at $\sigma$. For any given continuous signed-even finite field $E$ supported in $94\le|m|\le34814$ with

$$\|E\|_{\mathrm{ph},\sigma}\le r_M=2^{-43},$$

set $r_H=2^{-149}+r_M/50$. The original R98 domain gate still applies:

$$10\cdot2^{-40}+r_M+18555r_H<2^{-34}.$$

The complete nonlinear high derivative has bound

$$q_H=G_H\,4\cdot257\cdot2^{-34}
\le\frac{1480577}{94371840}<1/60,$$

because the new $G_H$ is no larger than the paid5760 value. This includes the same full mean root and inverse denominator.

The true head for $|m|\ge34816$ is a subset of the R78 infinite band; its old conservative $2^{-152}$ balanced lift remains valid. The same centre has support at most92. The old complete Neumann source tail for $|m|\ge5760$ therefore also bounds the new high projection, while the new source inverse is smaller; its conservative field cap $2^{-2053}$ remains valid. Consequently

$$2^{-152}+2^{-2053}+(r_M+r_H)/60<r_H$$

and the same contraction proof gives a unique conditional solution

$$H=H_{\rm bd}+\mathcal G_H\Pi_{|m|\ge34816}N(C_L+E+H)$$

in that high ball. This is a genuine high response theorem on the shared strip. It treats $E$ as a given field satisfying the stated norm. It does not assert that the still incomplete enlarged finite middle block satisfies that norm, or that high-to-finite and low feedback are already closed.

## 6. Completed data and exact scope

`2026-11-13-exact-resume-common-strip-v1.py` consumes every original frame/leaf and checks the four exact total identities. Its first threshold run formally exited0 in30.720512629 seconds, peak16880 KiB. The refined threshold run also formally exited0 in19.370809555 seconds, peak15868 KiB.

`2026-11-13-exact-resume-common-strip-v2.py` repeats the same exact evaluation for the selected34816 case and saves its entire per-leaf continuous loss and entering jump, with the original certified coefficient fields unchanged. It formally exited0 in20.382578850 seconds, peak16748 KiB. This is exact rational postprocessing of completed true data; there is no new physical/background ODE, interval source evaluation, frame optimization or tolerance change.

The full primary and resource names are `2026-11-13-exact-resume-common-strip-r1`, `common-strip-r2`, and `common-strip34816-r1` under the common date/prefix. The last includes `-leaves.jsonl.gz`, binding every future additional finite-frequency window to this exact shared profile. The old failed threshold comparisons remain in their actual packets.

The remaining numerical work uses the completed126 finite windows through the legitimate reweighting above, adds only59 new windows for the14528 missing positive modes, and then checks the complete finite/high/low self-map and distance equations. This note pays the common space and the conditional high source inverse; it leaves those further equations explicit.


## 7. The complete old126-window reweighting has now passed

The actual `2026-11-13-exact-resume-common-strip-middle-budget-v4.py` consumer has completed all126 original windows, all2833 positive even modes94..5758, and every one of the25 causal nonlinear budget blocks on the chosen common strip. It retains both genuine initial columns, all three source materials and the full shared source/head masses exactly as in R117. The inverse cutoff34816 used to define the shared strip does not silently add the missing finite frequencies to this statement.

The complete self-map and distance gates are true. The principal displays are

$$\max_i r_i=13885.685860895625\ldots<13886,$$
$$\max_i\Phi_i(r)/r_i=0.5007640545256378\ldots<501/1000,$$
$$\max_i(JW)_i/W_i=0.49999999999993827\ldots<1/2,$$
$$\max_i(10+r_i)V_{i,\max}=9.428494289160467\ldots\,10^{-13}<2^{-34}.$$

Most importantly, the exact full physical sum is

$$\|v_{94:5758}\|_{\mathrm{ph},\sigma}
\le\sum_i r_iV_{i,\max}
=2.0387647955717797\ldots\,10^{-14}<2^{-45}<2^{-43}.$$

Thus the old complete finite block really satisfies the physical input cap on the same strip as the new conditional high response. The failure of that cap in the original R117 hybrid norm was preserved, not relabelled. This conclusion is obtained by changing the fixed comparison space with all actual costs paid; the physical source and projected equation remain identical.

The v4 exact dyadic binomial consumer formally exited0 in27.862873793 seconds, peak27280 KiB. Its primary is `2026-11-13-exact-resume-common-middle-34816-r3.json.gz`. It contains all25 exact radii, complete three-material matrices, actual attaining windows, strict self-map and metric rows, and the unpaid enlarged finite gap.

A second completed implementation, v3, uses the exact degree24 Taylor lower bound followed by an upward96-bit dyadic ceiling. It formally exited0 in90.780868053 seconds, peak27256 KiB, with slightly sharper physical sum $2.0387024038416142\ldots\,10^{-14}$. The final v4 bound above is deliberately the one used for the next consumer, so neither implementation's improved field is silently substituted into another budget.

The earlier unrounded v2 attempt formally exited1 in366.198679447 seconds, peak20332 KiB, at Python's4300-digit integer serialization gate. Its unrelated rational Taylor denominators had grown too large. Its source and actual failure resource remain archived. No integer limit or mathematical margin was weakened; the fresh v3/v4 computations use proved outward dyadic ceilings and both completed.

The exact case data used by the successful reweighting are also identical to the single34816 common-leaf producer case, checked as full JSON exact records. This binds the subsequent new59 finite windows to the same actual profile. Until those windows and both directions of nonlinear feedback are consumed, the additional14528 positive finite modes and the coupled finite/high problem remain open. Low feedback and the all46 cut remain separate obligations as well.
