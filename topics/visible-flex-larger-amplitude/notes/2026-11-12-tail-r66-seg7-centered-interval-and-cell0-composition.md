# R66 application: same-quartic interval refinement on segment 7 and complete cell 0

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted). Date: 2026-11-12.

**Implementation correction, 2026-11-12:** the original executed helper's shifted-power expression used `delta**j`. In the installed python-flint binding this is nonfinite when the interval `delta` crosses zero, even for positive integer `j`. Its subsequent `intersection(old, nan)` returned an outward enclosure of the original five-basis interval, because the two `max/min` comparisons retained their first finite argument. Thus the recorded finite bounds below remain valid, but the first execution did **not** pay a tighter centered-polynomial enclosure. The improvement to $0.760858$ comes from the source-span subdivision and complete finite-$J$ bound. All old executable sources and primary numerical records are preserved. See [the explicit correction and replacement plan](2026-11-12-tail-r66-centered-power-correction.md); the replacement uses finite checked integer Horner evaluation and has separate execution records.

The new continuous audit of the **unchanged** outer cell 0, segment 7 candidate has formally completed. All **1740 intervals** covering all eight substages and 64 stored positive-integral bins pass the full R64 mean and domain gates. Including every finite residual frequency through $|m|=80$, the segment's full-angle physical Darboux defect is less than **0.760858**, improving its prior certified upper bound of $2.378359$.

Combining that audit with the completed [segment 5 audit](2026-11-12-tail-r66-seg5-complete-span-and-finite-J.md) and the unchanged remaining components gives the same **complete cell 0 candidate** a bound less than **0.760858** over **7563 continuous intervals**. This is still a candidate residual; no exact radial existence, outer Green/Schur bound, or corrected curvature claim follows from it alone.

## 1. The polynomial has not changed

Let $a_0,a_1$ denote the left endpoint's normalized slope and its $u$ derivative, let $b_0,b_1$ denote the corresponding right endpoint values, and let $\lambda$ be the unique bubble coefficient fixed by the five true positive R48 integrals. For each cosine mode the old R48 polynomial is

$$
k(u)=a_0q_{00}(u)+a_1q_{10}(u)
     +b_0q_{01}(u)-b_1q_{11}^{+}(u)
     +\lambda u^2(1-u)^2,
$$

where $q_{11}^{+}=u^2(1-u)$. Expanding that same polynomial gives

$$
\begin{aligned}
k(u)={}&a_0+a_1u+
(-3a_0-2a_1+3b_0-b_1+\lambda)u^2\\
&+(2a_0+a_1-2b_0+b_1-2\lambda)u^3+\lambda u^4.
\end{aligned}                                                   \tag{1}
$$

If $k(u)=\sum_{i=0}^{4}a_i^{*}u^i$ and $u=t+\delta$, the exact shifted coefficients are

$$
b_j^{*}=\sum_{i=j}^{4}\binom{i}{j}a_i^{*}t^{i-j},
\qquad k(u)=\sum_{j=0}^{4}b_j^{*}\delta^j.             \tag{2}
$$

For a finite implementation of (2), one may take $t$ to be the interval midpoint, evaluate its integer polynomial using multiplication and addition, and differentiate (1) exactly with the same $u_x$. Intersecting the resulting finite enclosure with the existing five-basis evaluation remains valid: both enclose the same exact polynomial or derivative. Possible interval dependence among the exact bubble and endpoint constants does not invalidate either enclosing calculation. This is the mathematical same-polynomial lemma; the first helper did not implement its shifted powers finitely on positive-width intervals, as recorded in the correction above.

The nonmean height $H$ is returned from the **unchanged** original weighted primitive evaluation. No moment, endpoint, bubble, source, mode, or candidate coefficient is selected anew. Thus (1)–(2) change interval evaluation only. The executable additionally checks all five basis identities and their derivatives at six exact rational values of $u$; these 30 checks are finite arithmetic checks, not numerical checks of the Darboux equation.

The adapter requires the exact SHA of the already executed span-refinement source and records a reversible metadata transformation. Its only numerical callable substitution is this same-polynomial interval evaluator. All root signs, inverse-domain conditions, actual derivative formulas, source subdivisions, and complete finite-$J$ calculations remain those of the original span audit.

## 2. Full continuous and angular coverage

The real source and polynomial interval conditions are the same as in the segment 5 application:

$$
\frac{\sup r_x}{\inf r_x}\leq2,\qquad
\operatorname{span}(\log w)\leq\frac1{32},\qquad
\operatorname{span}(u)\leq\frac1{32}.
$$

Every possible source branch is retained. The same whole stored bin bounds the height primitive and radius on each of its subsets. There are no new source integrals, radial flows, BVPs, or Node evaluations.

The complete scalar mean $c$ and its actual derivative $c_x$ come from the unchanged R64 implicit root. The complete numerator is

$$
J=J_{\rm lin}+J_{\rm quad}
  +cJ_{\rm lin}+c_x(k+EP_\theta)
  +c_x(1+c)+\ell(2c+c^2),
$$

with all terms and units as proved in the [same-candidate spectrum identity](2026-11-12-tail-r66-seg5-source-span-and-complete-spectrum.md). Every accepted interval stores every signed cosine coefficient for $m=0,2,\ldots,80$; negative modes are fixed by exact even symmetry. In particular, the band above the saved height cutoff $40$ is computed and retained, not discarded.

## 3. Actual segment bounds

The displayed upper bounds round outward from the exact dyadic records.

| Substage | Complete intervals | Full-angle physical Darboux bound from complete finite $J$ |
|---:|---:|---:|
| 0 | 37 | $<0.760858$ |
| 1 | 53 | $<0.009547$ |
| 2 | 125 | $<0.002666$ |
| 3 | 208 | $<0.001637$ |
| 4 | 304 | $<0.021508$ |
| 5 | 257 | $<0.020489$ |
| 6 | 256 | $<0.002516$ |
| 7 | 500 | $<0.009276$ |
| **Entire segment 7** | **1740** | **$<0.760858$** |

The exact stream checker takes the smaller of the original R64 and full finite-$J$ bound on each same interval. Its complete-segment upper endpoint is

$$
418285978785\,2^{-39}<0.760858.                       \tag{3}
$$

The complete mean satisfies $|c|<4.263\cdot10^{-5}$. Over the entire segment, the mean derivative with respect to its scalar argument is greater than $0.9986677$, $D>0.9999435$, $S>0.99999997$, $L>0.9986847$, and the Wiener denominator margin is greater than $0.9959048$.

The new maximum is in substage 0, bin 0, on

$$
\left[\frac1{256},\frac1{128}\right].
$$

This interval is on the certified cap branch, with $w$ close to $0.02$ and the recorded positive $r_x$ interval having upper/lower ratio below $1.955$. Here the mean contribution is below $0.001719$, the retained nonmean contribution is below $0.759139$, and the complete beyond-height band contributes less than $4.367240\cdot10^{-15}$. Over all segment 7 intervals, that last band is bounded by $1.647266\cdot10^{-13}$.

This identifies a retained-frequency, first-substage bottleneck in the current **upper bound**. It does not by itself prove that the candidate's actual pointwise residual reaches that value. The saved endpoint jets, bubble coefficients, source ranges and all signed $J$ coefficients support a targeted interval/point comparison before another change of candidate.

The actual signed nonmean physical second derivative is still evaluated from the candidate as $(w/r_x)(k_x+\ell k)$. Its recorded global $W^1_{1/64}$ upper bound is below $33.624880$. This remains an interval upper bound on one height-jet norm, not a statement about principal curvature.

## 4. Composition with the other eight segments

The independent standard-library composition reads the original complete nine-segment candidate manifest. For segments 5 and 7 it verifies that the new audit input SHA is **exactly** the original component candidate's SHA, that the complete stream checks are successful, and that the original common physical input identities match. No other component definition or endpoint is changed.

The resulting table is:

| Original source segment | Continuous intervals used | Physical Darboux upper bound |
|---:|---:|---:|
| 0 | 1 | $<0.012030$ |
| 1 | 292 | $<0.111805$ |
| 2 | 16 | $<0.002509$ |
| 3 | 4211 | $<0.193211$ |
| 4 | 16 | $<0.000595$ |
| 5 | 1255 | $<0.192327$ |
| 6 | 16 | $<0.029951$ |
| 7 | 1740 | $<0.760858$ |
| 8 | 16 | $<0.253540$ |
| **Complete cell 0** | **7563** | **$<0.760858$** |

Only the same physical Darboux quantity is compared. Source-coordinate residuals, radial derivatives, and finite source norms are not summed across the mixed source-$x$ and physical-$r$ charts. The complete mean definition and its one free additive height constant are inherited unchanged from the original complete candidate. No geometry or curvature audit is recomputed by this composition.

## 5. Formal execution and preservation

The numerical audit was tool session **35885**, with formal tool and wait4 child exit code **0**, no termination signal, $222.49724125862122$ seconds wall time, and peak RSS **31640 KiB**. All seven whole-segment gates are true.

The exact stored-evidence check was session **10432**, formal exit code **0**, $12.724931955337524$ seconds, and peak RSS **12288 KiB**. It checked all 1740 accepted intervals, 64 original bins, eight complete streams, source relative-span bounds after outward serialization, all positive recorded mean/domain margins, and every signed coefficient through $m=80$.

The complete-cell substitution was session **46279**, formal exit code **0**, $0.8990890979766846$ seconds, peak RSS **12336 KiB**, and all six identity/coverage/common-unit gates true. Both latter checks use only integer and Fraction arithmetic.

Primary segment audit: notes/2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r1.json, together with its eight part streams and exact stream-check output. The streams total 1843564 bytes, each below the per-file limit.

Complete-cell composition: notes/2026-11-12-tail-outer-cell0-components-357-span2-r1.json.

The accompanying manifest binds all executed sources, prepared parameters, primary data, resource records, checks, and this corrected note. Its correction field records the original note and manifest hashes; no original executable or primary bound is overwritten. The duplicate completed recovery summary is unnecessary for publication. The initially prepared narrow quartic diagnostic subsequently completed as session 24039 with tool and wait4 exit 0; it located the implementation fallback and has its own separate output/resource records.
