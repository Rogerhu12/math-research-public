# R66 application: complete segment 5 source-span refinement and finite $J$

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted). Date: 2026-11-12.

The actual same-candidate execution is complete: **1255 of 1255 continuous intervals** cover all eight substages and all 64 original positive-integral bins of outer cell 0, original source segment 5. All original complete-mean and inverse-domain gates pass. The complete full-angle physical Darboux defect of this segment is less than **0.192327**. This replaces the previous segment 5 upper bound of $4.023377$ for the **same** R48 height.

This is a continuous residual certificate for the finite compatible candidate, not existence of an exact outer radial solution or a bound on the eventual corrected surface.

## 1. Fixed candidate and precise refinement

The candidate is the one defined in [the executed segment 5 application](2026-11-12-tail-r66-seg5-substage-application.md). Its nine shared physical two-jets, all twenty Fourier modes, five exact positive weighted moments on each substage, bubble coefficients, height primitives, and physical metric are unchanged.

The new executable consumes the saved true integral bins and the same ready/source identities. It does not perform a source integral, background flow, ODE, Node evaluation, BVP, finite root solve, or new candidate construction. At an evaluation interval within a saved bin, both height-primitive formulas keep the original bin's complete monotone prefix/suffix bounds. The radius keeps the same two-sided bin enclosure.

Starting from each entire saved bin, it bisects only the verification interval until all of the following hold:

1. The union of every possible real source branch is finite and has logarithmic $w$ span at most $1/32$.
2. The true positive radius derivative is enclosed with $\sup r_x/\inf r_x\leq2$.
3. The local R48 polynomial coordinate has span at most $1/32$.
4. The unchanged [R64 complete mean and actual residual routine](../results/R64-general-outer-mean-and-compatible-defect.md) passes all of its sign, monotonicity, real-domain, and Wiener inverse gates.

The maximum binary subdivision level is 28; the stated panel budget is 100000; the actual run used 1255 intervals. These limits are safeguards, not mathematical assumptions replacing successful coverage.

The actual normalized derivative $k_x$ is differentiated from the same R48 quartic. The mean derivative $c_x$ is restored by R64's complete implicit root and compatibility argument. No right-hand-side value is substituted for either actual derivative.

## 2. Complete Fourier residual

Use $K=c+k$, $P=h_\theta/(rw)$, $T=P_\theta$, $U=k_\theta-P$, $z=w^2$, $E=1+z$, $s=r_x/r$, and $\ell=w_x/w$. The complete numerator is the exact polynomial identity

$$
\begin{aligned}
J_{\rm lin}&=k_x+\ell(2k+T),\\
J_{\rm quad}&=(k+ET)k_x-EsU^2+\ell(k^2+zP^2+kT),\\
J&=J_{\rm lin}+J_{\rm quad}
  +cJ_{\rm lin}+c_x(k+ET)+c_x(1+c)+\ell(2c+c^2).
\end{aligned}
$$

The derivation and support argument are in [the same-candidate witness proof](2026-11-12-tail-r66-seg5-source-span-and-complete-spectrum.md). Every accepted interval computes all coefficients through $|m|=80$, including the scalar mean. The candidate is real and even in angle; the two independently enclosed conjugate Fourier entries are intersected and saved as cosine coefficients for $m=0,2,\ldots,80$. Negative coefficients are determined by this exact symmetry, not omitted. Above $|m|=40$, the numerator equals the corresponding coefficients of $J_{\rm quad}$ and is independent of $c,c_x$.

Consequently the following full-angle bound holds on each entire accepted radial interval:

$$
\left|\frac{w^2J}{r\,r_xE^2}\right|
\leq
\sup\frac{w^2}{r\,r_xE^2}
\left(|J_0|+\sum_{m=2,4,\ldots,80}|J_m^{\cos}|\right).
$$

This is a zero-strip Fourier $\ell^1$ estimate, with no angular samples. The original R64 $W^1_{1/64}$ estimate is also recorded; the independent stream check takes their smaller physical upper bound only when both refer to the same radial interval.

The scalar root is the same root across adjacent verification intervals. Their symmetric root brackets all contain zero. At a shared point, the larger of two such brackets retains the certified positive derivative and contains both roots, so uniqueness identifies them. Across substage boundaries, the original shared nonmean physical two-jets identify the scalar root and its physical first derivative by the same implicit equation. Thus this verification bounds the already defined single compatible mean height up to its one free additive constant; it does not introduce independent means on separate panels.

## 3. Complete actual bounds

All displayed decimal inequalities round outward from the stored exact dyadic endpoints.

| Substage | Complete accepted intervals | Original R64 physical bound after span refinement | Complete finite-$J$ full-angle bound |
|---:|---:|---:|---:|
| 0 | 32 | $<0.030989$ | $<0.006420$ |
| 1 | 80 | $<0.031109$ | $<0.006147$ |
| 2 | 195 | $<0.014196$ | $<0.002255$ |
| 3 | 522 | $<0.032421$ | $<0.010274$ |
| 4 | 106 | $<0.029142$ | $<0.008769$ |
| 5 | 64 | $<0.015403$ | $<0.004354$ |
| 6 | 128 | $<0.018796$ | $<0.005380$ |
| 7 | 128 | $<0.596438$ | $<0.192327$ |
| **Entire original segment 5** | **1255** | **$<0.596438$** | **$<0.192327$** |

The separately checked per-interval minimum of the two valid physical bounds has exact upper endpoint

$$
422931315185\,2^{-41}<0.192327.
$$

The complete mean is bounded by $|c|<0.001137$. Over the full segment, the certified mean derivative with respect to its scalar argument is greater than $0.9482148$, $D>0.9999782$, $S>0.99999998$, $L>0.9482193$, and the Wiener denominator margin is greater than $0.8372814$. Every stated margin is a continuous interval margin for the same true source.

The largest accepted $r_x$ upper/lower ratio is less than $1.999667$. The independent standard-library checker also recomputed that ratio from the outward serialized dyadic source intervals, so the stored records themselves preserve the specified strict margin below 2.

The remaining maximum is in substage 7, bin 7, on

$$
\left[\frac{255}{256},\frac{1021}{1024}\right].
$$

On that interval the retained nonmean frequencies contribute less than $0.192143$, the mean contributes less than $0.000184565$, and the entire band $42\leq|m|\leq80$ contributes less than $6.936973\cdot10^{-16}$. The last number also bounds that band over the complete segment. Thus the new remaining large upper bound does not come from the beyond-height band. The recorded true $r_x$ interval on this new witness has ratio below $1.09$, so the earlier factor-148 source-span pathology is absent there.

The signed actual nonmean physical second derivative is evaluated as $(w/r_x)(k_x+\ell k)$; its complete $W^1_{1/64}$ upper bound is less than $8.377336$. It is not an upper bound for the principal curvatures, and it has not yet been normalized by an outer Green inverse.

## 4. Preserved evidence and formal execution

Actual Arb/source audit:

- Tool session **26873**, formal tool exit code **0**.
- Independent wait4 child exit code **0**, no signal.
- Wall time $131.6844780445099$ seconds; observed child peak RSS **32140 KiB**.
- Precision 192 bits; one numerical process; no new integral, ODE, Node, or BVP.
- All seven completion/identity/domain/spectrum gates true.

Exact stored-evidence check:

- Tool session **61841**, formal tool and wait4 child exit code **0**.
- Wall time $6.23522686958313$ seconds; observed child peak RSS **12288 KiB**.
- Only standard-library integers and Fractions; no new Arb/source evaluation.
- All eight stream-hash, full-coverage, positive-domain, complete-spectrum, source-span, and same-panel-bound checks true.

The primary is notes/2026-11-12-tail-outer-cell0-seg5-span2-finiteJ-r1.json, with eight referenced part00 through part07 compressed JSONL streams. Each stream includes its exact source coverage, every accepted interval's real source bounds, complete R64 margins and residual bounds, all 41 signed cosine coefficient intervals, and a complete trailer. Endpoints are directed outward to exact 40-significant-bit dyadics, with no exponent cutoff. The final summary keeps the uncompressed high-precision global bounds and their witnesses.

The eight stream files total 1373622 bytes. Every individual file is below 5 MB. A recoverable checkpoint was written after every completed bin; the final summary and complete streams contain all successful data, so the duplicate final recovery file need not be committed.

The accompanying executed manifest lists both executables, their exact commands and hashes, the prepared plan, both resource records, the primary, every complete stream, this proof note, and the exact stream-check output.

## 5. Remaining outer work

The full current cell 0 composition still has a larger stored physical residual bound in original segment 7. This new result changes only the certificate for the already fixed segment 5 candidate. It does not alter the other eight segment certificates.

Before another change of candidate, the new segment 5 end witness can be tested with an algebraically identical centered evaluation of its quartic normalized slope and cubic derivative, intersected with the original basis evaluation. This changes interval enclosure only. A midpoint test alone would not replace a continuous certificate.

The full outer existence proof still needs its true-head matching center, signed residual functional, finite Green/Schur inverse, high-frequency analytic propagation and nonlinear closure. The complete finite-$J$ bound above is an input to those obligations, not a substitute for them.
