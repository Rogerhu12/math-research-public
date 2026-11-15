# R133 supplement: actual all-segment Darboux error and complete scalar receivers

2026-11-15, visible-exact / phase_inverse.

**The first public all-segment Darboux scalar computation completed successfully.** Run **43746008734/1** returned child code zero and passed all **23 gates**. It paid the new common gap for all 27 phase products, the complete all-segment integral functional and six scalar receivers, including both extra differential sources and all physical means. The new mathematical time was **0.0103302549999853 seconds**. No old successful scientific calculation was repeated.

This is the first scalar stage of the [IN theorem](R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md). Its error-profile functional maps $H^{-4/3}$ to old-angle $L^2$. Density zero retains a raw $H^{-1}$ scalar conclusion; density one has an $L^2$ scalar conclusion; the two additional differential sources have target $H^{-5/3}$. The original $J,L,B_{\rm op}$, radial $\eta^{-1}$, true strict-cut density frame and free $R_2,R_3$ have **not yet been composed**. This report does not claim the final physical $C_{\rm Dar}$, an incoming inverse or a complete return remainder.

## 1. Actual execution and immutable identities

The unique automatic push run is [43746008734/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43746008734), from deployment commit 96001fbab4e62356d30ebf5b105b381e7639fe06. The scientific checkout was that same commit. Job **132909338845** ran from **18:18:31 UTC** to **18:19:23 UTC** on 2026-11-15; its complete step list and conclusion are successful. The direct run-jobs response was read in full: 3221 UTF-8 bytes, SHA256 db1edc92c82a28c7813295003f943e597c21923a9a38cbe98f000f68bddb5f90.

The child wall time was **0.46492604499999857 seconds**. Its frozen runtime was Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5 and SciPy 1.17.0, using 320-bit Arb arithmetic.

| Item | Path | Bytes | SHA256 |
| --- | --- | --- | --- |
| Proof | results/R133-supplement-genuine-Darboux-comparison-and-complete-incoming-factorization.md | 33894 | d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75 |
| Science | scripts/fourfold_codazzi_all_segment_Darboux_scalar_receivers.py | 36387 | 726bdd98802c88e9c162f598ff983bc8a762d8cc8f8216164c56e6b960119874 |
| Manifest | notes/2026-11-15-R133-all-segment-Darboux-scalar-receivers-CI-inputs.json | 11524 | fc87dad98247598d6183d225f4dfca29ee66a8cd06c0918ffda59888091cfb74 |
| Worker | scripts/fourfold_codazzi_all_segment_Darboux_scalar_receivers_public_worker.py | 35288 | 793acef43ddb118ac68b566001fd912fcf4dde7bc05b2437a717ce7af0275909 |
| Workflow at repository root | .github/workflows/visible-all-segment-darboux-scalar-receivers.yml | 4272 | fa04a08f83ba5c662f3f9a761ac30a6567aefafc385790947c13da758fcc0f63 |

The two original small results are:

| Receipt | Git blob | Bytes | SHA256 |
| --- | --- | --- | --- |
| [execution.json](../notes/all_segment_Darboux_scalar_receivers_ci/run-43746008734-1/execution.json) | 64dab676807dbd3ee0913bdde1bb7cd732d8410a | 35387 | 816483884254f3e7ec06914b66afffc8434db11315dfab1712e71fbb7aae5ae1 |
| [actual-result.md](../notes/all_segment_Darboux_scalar_receivers_ci/run-43746008734-1/actual-result.md) | 1489f821f9774def05aec0da8b6990797caad80d | 15612 | 3bfc773c2a3980e95405de7e9eb5c1ee9f3682612b303c9c1fed4a1d8ce6f51e |

Both were read completely. Source, worker, manifest, parameters, runtime, all 23 actual gates, all twenty input identities and every reported ball were checked. Re-encoding the **already completed scientific JSON**, with no mathematical evaluation, recovers exactly 19999 bytes and SHA256 6c49494aa521be7d71f6d7665bd3ac7e35ef5f2fc866fcc0c27353a5a9224a2f. Reconstructing the prepublication stdout envelope likewise gives exactly 38529 bytes and SHA256 15a81425f46b76766232acb876d5c2d44a91c8866307dfc0fad50bee839e6e24.

## 2. Same physical cut, full parameter family and new phase gate

The calculation uses the original P.22 cut and root bracket:
$$
r_c=\frac{76285779072683}{320000000000000},\qquad
r_*\in\left[
\frac{1191984371497}{5000000000000},
\frac{2383968743003}{10000000000000}
\right].
$$
The recorded exact inward-radius interval is
$$
\rho=r_*-r_c\in
\left[\frac1{262144},\frac{1220703413}{320000000000000}\right].
\tag{INA.1}
$$
The frozen intrinsic parameter is $\eta_0$, the full real family is $|\delta|\le10^{-8}$, and the common potential retains its original complex $\delta$- and $z$-squares. Physical input frequencies are $n=4|j|\ge388$. Both carrier signs, both reference-column labels, all output Fourier modes and all means remain.

The three-factor variation-of-constants terms have phases
$X+c(\tau)\omega$, $|c(\tau)|\le3$, $\omega=2(-T)^{3/2}/3$.
The actual common gap is new; it is not a renamed one-phase gap:

| Complete cut quantity | Recorded directed ball |
| --- | --- |
| Lower modulus of $T$ | `[1.704434967474488803693916373996076475812617849511890e-5 +/- 2.56e-57]` |
| Upper modulus of $T$ | `[1.770003452093494028821174768740622261890335054334433e-5 +/- 1.07e-57]` |
| New common three-phase gap, lower bound | `[0.9999986308459262365495425814176916752876407345172316 +/- 1.52e-53]` |
| New common phase second derivative, upper bound | `[5.841724048059524384580068782555516075858297377113607e-5 +/- 7.91e-58]` |
| New common phase third derivative, upper bound | `[0.004984937854345038735264830795484622187300073068694190 +/- 4.26e-55]` |
| $|\partial_\phi^{1}\omega|$ upper bound | `[1.020031061297617833311600160047074894303522080159211e-12 +/- 4.08e-64]` |
| $|\partial_\phi^{2}\omega|$ upper bound | `[4.352133240125256350218506263981850294883473654304607e-11 +/- 1.20e-63]` |
| $|\partial_\phi^{3}\omega|$ upper bound | `[3.713820668660359809553471094754257026958416600245790e-9 +/- 3.61e-61]` |
| Accepted complete all-segment $T$ radius | `[5.316292457039263121941867247085722205456420784944265443115969375e-5 +/- 2.72e-69]` |
| Accepted common potential image radius, lower bound | `[0.0007429560501680405148374516366694093888676229432699305021969848895 +/- 4.86e-68]` |

The saved signed disk has radius
$125978014066294748203/10995116277760000000000000$.
The original complete profile cover is
$893368603925465506687/21990232555520000000000000$.
The actual gate checked the strict cut inside the original root piece and all $\tau T$, $0\le\tau\le1$, inside the original potential product. No real-angle jet was promoted to a complex strip.

For $H=\mathcal B''+V\mathcal B$, the new complete angular derivative bounds, uniform along the whole segment, are:

| Derivative | Recorded upper-bound ball |
| --- | --- |
| $\partial_\phi^{0}H(\tau T)$ | `[841924.0511650584880044334568083286285400390625000000 +/- 1e-50]` |
| $\partial_\phi^{1}H(\tau T)$ | `[0.1947121295850802632865747364673994068293941312810619 +/- 1.63e-53]` |
| $\partial_\phi^{2}H(\tau T)$ | `[8.307717634239456268798715417204653221306747255067879 +/- 3.68e-52]` |

They use the saved canonical derivatives $\mathcal B_0,\ldots,\mathcal B_4$ and $V_0,V_1,V_2$, including every chain term. No old Fuchsian quotient or potential closure was reevaluated.

## 3. Profile bound numbers recovered from the original positive coefficients

The accepted calibration contains eighteen coefficients, six for each of the same three original phases. Every candidate in its saved coefficient minimum bounds the same nonnegative algorithm coefficient. IN.17a–b gives these new upper triples without running the old profile or calibration:

| Phase | Profile | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- | --- |
| central | height | `[25.12246483569135891911359050636129227255203798713646 +/- 1.67e-51]` | `[1895.118073645011189606789812522329135843042988912246 +/- 3.70e-49]` | `[1.570154052230709932444599406647580767034502374196029 +/- 3.55e-52]` |
| central | derivative | `[0.6135031486996300311644023762024032705783195228869888 +/- 1.98e-53]` | `[78.34826463846283736130889338277765249701966200156368 +/- 1.14e-51]` | `[18812.00505193037232360844124443083023788706645354803 +/- 2.35e-48]` |
| positive_characteristic | height | `[26.23195887960163116725773508880761148513148739570568 +/- 5.76e-52]` | `[1978.812974960134689686075695010484123170514849002289 +/- 3.97e-49]` | `[1.639497429975101947953608443050475717820717962231605 +/- 3.60e-53]` |
| positive_characteristic | derivative | `[0.2548103194512416448468628892508911576150243463161467 +/- 2.52e-53]` | `[32.54091312226936753697885257980555495859039634283910 +/- 3.69e-52]` | `[7813.316923806329585880867186102660607098238659182674 +/- 6.33e-50]` |
| negative_characteristic | height | `[26.23195887960163116725773508880761148513148739570568 +/- 5.76e-52]` | `[1978.812974960134689686075695010484123170514849002289 +/- 3.97e-49]` | `[1.639497429975101947953608443050475717820717962231605 +/- 3.60e-53]` |
| negative_characteristic | derivative | `[0.2548103194512416448468628892508911576150243463161467 +/- 2.52e-53]` | `[32.54091312226936753697885257980555495859039634283910 +/- 3.69e-52]` | `[7813.316923806329585880867186102660607098238659182674 +/- 6.33e-50]` |

Their complete sums, used before the full product expansion, are:

| Sum | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- |
| All height profiles | `[77.58638259489462125362906068397651524281501277854782 +/- 2.83e-51]` | `[5852.744023565280568978941202543297382184072686916824 +/- 4.24e-49]` | `[4.849148912180913828351816292748532202675938298659239 +/- 4.27e-52]` |
| All derivative profiles | `[1.123123787602113320858128154704185585808368215519282 +/- 1.70e-52]` | `[143.4300908830015724352665985423887624142004546872419 +/- 1.97e-50]` | `[34438.63889954303149537017561663615145208354377191338 +/- 4.47e-48]` |

These are bounds on the original positive algorithm's profile parameters, not lower bounds on physical amplitudes. The original positive tail and the central piece are retained. The expansion includes all 27 phase products and all binomial factors. Its exact remaining integral is
$$
\int_0^1\tau^{-1/2}\,d\tau=2.
\tag{INA.2}
$$
No quadrature, finite $\tau$ grid or truncated improper integral is used.

## 4. All twenty-four new positive functional coefficients

The component order is
$$
(a,\ a_\phi,\ a_{\phi\phi},\ b,\ b_\phi,\ b_{\phi\phi}).
\tag{INA.3}
$$
Each functional is the positive dot product with the following six coefficients. The common cut factor $\rho_-^{-1/4}$ is included.

### 4.1 Original weak functional at the new cut

This retains the original complete profile window $H^{-4/3}\to H^{-5/3}$, used also for the free derivative-profile source.

| Component | Recorded coefficient upper-bound ball |
| --- | --- |
| a | `[438.8948580846712821532974427468469267863113668361724 +/- 4.25e-50]` |
| a_phi | `[1059459.836828684440330364865975292200343599756224646 +/- 4.98e-46]` |
| a_phiphi | `[12415.54496283614578512146327314795547277655964325756 +/- 4.48e-48]` |
| b | `[3117029.772889817369871000676101909706296569348593449 +/- 2.78e-46]` |
| b_phi | `[25963.61981173074377765164945527570771473775401056990 +/- 7.91e-49]` |
| b_phiphi | `[101.6535611296478747241068969648638865179410804655594 +/- 1.74e-50]` |

### 4.2 Complete zero-order functional

This is the IN.15–17 positive-budget domination of $L^2\to L^2$, not an upgrade of an arbitrary weak operator norm.

| Component | Recorded coefficient upper-bound ball |
| --- | --- |
| a | `[1755.579432338685128613189770987387707145245467344690 +/- 2.31e-49]` |
| a_phi | `[4237839.347314737761321459463901168801374399024898582 +/- 8.98e-48]` |
| a_phiphi | `[49662.17985134458314048585309259182189110623857303026 +/- 2.09e-48]` |
| b | `[12468119.09155926947948400270440763882518627739437380 +/- 2.90e-45]` |
| b_phi | `[103854.4792469229751106065978211028308589510160422796 +/- 3.17e-48]` |
| b_phiphi | `[406.6142445185914988964275878594555460717643218622377 +/- 3.06e-50]` |

### 4.3 Complete all-segment integral functional

The input factor $n^{-2}$ remains separate from these coefficients.

| Component | Recorded coefficient upper-bound ball |
| --- | --- |
| a | `[121516786278147.0009856398901641339945746568484876993 +/- 1.06e-38]` |
| a_phi | `[840166687685.7635674817136556500237310453217244371625 +/- 3.68e-41]` |
| a_phiphi | `[1507962240.611210140612404403869294942215382284581300 +/- 1.31e-43]` |
| b | `[2891975168361.913268982281693599856249739583398533126 +/- 2.55e-40]` |
| b_phi | `[14444121706.42271470996320289513903342041784821205812 +/- 3.16e-43]` |
| b_phiphi | `[21828937.07107407623330818681975808166543109151757694 +/- 3.26e-45]` |

### 4.4 Strong Darboux error-profile functional

This complete functional maps $H^{-4/3}\to L^2$.

| Component | Recorded coefficient upper-bound ball |
| --- | --- |
| a | `[4568579516349.679399398033501738605321800931281043720 +/- 3.36e-40]` |
| a_phi | `[101019705762.3646211951699890291572062809590155905831 +/- 3.80e-41]` |
| a_phiphi | `[870358573.2708518531338479079939297188268823925562695 +/- 2.74e-44]` |
| b | `[313004496233.4023753538276178097631546917659652334604 +/- 2.08e-42]` |
| b_phi | `[2244593659.960779098516528348266948834062271918946185 +/- 4.73e-43]` |
| b_phiphi | `[7482649.516348932311032248572234212494132976053793519 +/- 4.67e-47]` |

The root input matrix has the complete analytic multiplier bound **16384**, including the nonzero $\beta_n$. It was not estimated by a columnwise Hilbert–Schmidt sum. The integral's complete strong input multiplier has upper-bound ball `[0.03759604654519937983643799805942605779972069005570468 +/- 1.18e-54]`.
All twenty-four entries retain finite outputs, both reference columns and the means.

## 5. Six complete scalar receivers

### 5.1 Density zero

The saved columns are $B_Vw_0,B_Vp_0,B_Vg_0$.
The second identity in IN.24 retains the full derivative term, differentiated normalized column and its explicit inhomogeneous addition. Consequently this raw scalar target is **$H^{-1}$**, including its true mean.

| Column | Normalized value error, $L^2$ | Normalized derivative error, $L^2$ | Extra primitive error, $L^2$ | Complete raw scalar, $H^{-1}$ |
| --- | --- | --- | --- | --- |
| w0 | `[4698456526502.316615135346027136609109864768582486926 +/- 1.98e-40]` | `[1378170955.253611844572631832264051038152727455145181 +/- 3.53e-44]` | `[4.931544405555395667125963887140840266900543517563136e-8 +/- 1.21e-60]` | `[4699834697457.570227029234103024427117574180948813479 +/- 3.86e-40]` |
| p0 | `[1544924438937.369340819192233269554616396876728834372 +/- 3.23e-40]` | `[171590775.1153431464400879915243257908412501579369487 +/- 3.15e-44]` | `[696.2032940002864341404777871629144721832815301402731 +/- 2.34e-50]` | `[1545096030408.687977965918755401556729350632451175590 +/- 1.56e-40]` |
| g0 | `[7834229380256061.327988056164707202166305392780637406 +/- 2.75e-37]` | `[42447865826983.67041437551331333084995055121009655031 +/- 2.39e-40]` | `[0.007444056061626438496617565272804062529655256330311007 +/- 2.96e-55]` | `[7876677246083045.005846487739646971512873509263538019 +/- 4.35e-37]` |

The derivative term has zero mean by its exact full-circle identity. Every other mean remains; the output mean is not a virtual input at $j^{-2}=0$.

### 5.2 Density one

These three receivers use complete raw $w_1^V,p_1,g_1$ with the accepted angular orders $0,1,2$. No additional inverse is inserted.

| Column | Complete scalar error upper-bound ball, $L^2$ |
| --- | --- |
| w1 | `[303231440682.8363509111051613193537381836328449193906 +/- 4.07e-41]` |
| p1 | `[42747795362.41274772087755951406874433752986110194961 +/- 1.99e-42]` |
| g1 | `[39342851433011.31876163607348954712151284980565296939 +/- 1.74e-39]` |

The $g_1$ input is DG's complete signed-disk bound, not the maximum of RJ's six negative real rows. All physical means remain.

The $p_0,p_1$ rows are $\eta h_0,\eta h_1$. Their radial factor $\eta^{-1}$ is reserved for the physical receiver; it has not been charged or omitted by renaming $p$ as $h$.

## 6. Both exact inhomogeneous identities and their extra sources

The error profile has additional state row
$$
\mathfrak r_n=
\left(0,\frac{H_n(T)}{n^3}[F_n(T)]_{2,\alpha}\right).
$$
The primitive addition in density zero has input factor $n^{-2}$ and complete amplitude $Hy(B_Vw)_2$, likewise for $p_0,g_0$:

| Column | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- |
| w0 | `[5.089768590992910268862172377053708828860222764317589e-14 +/- 2.18e-67]` | `[4.343269269681183671259893186049193049283107575777103e-12 +/- 1.18e-65]` | `[5.559384726660844361468744767326378173887126436673282e-10 +/- 8.19e-63]` |
| p0 | `[0.001007524661968626376555603897531987502535298959434874 +/- 4.22e-55]` | `[0.04298777919317781869673348224007060904161016295962219 +/- 4.08e-54]` | `[3.668295574420239186520627232846017222506066775681694 +/- 1.03e-52]` |
| g0 | `[7.682851025959259055644618458885054602049324996790942e-9 +/- 3.20e-62]` | `[6.556085812657705227815253251762482868956951357963271e-7 +/- 9.22e-60]` | `[8.391846657316805334626478592264521651087787799954391e-5 +/- 1.48e-57]` |

Its scalar errors are already included in section 5 and must not be added twice.

The first identity in IN.24 has a separate differential source. Its input powers are $n^{-1}$ and $n^{-2}$ in the two densities. The exact second-row recovery is
$$
\Omega_0=
Qx(yZ_{w,a}+i\epsilon xZ_{w,b})
-y(yZ_{p,a}+i\epsilon xZ_{p,b}),
\qquad
\Omega_1=Qx\,b_1^V-y\,p_{1,b}.
\tag{INA.4}
$$
The second row of $H_V$ is exactly $(y,i\epsilon x)$; the first row, including $V$, stays in the other complete saved columns. The complete triples of $H\Omega_i$ are:

| Density | Order 0 | Order 1 | Order 2 |
| --- | --- | --- | --- |
| 0 | `[0.003022578124266115826079229553804231136476719289346428 +/- 9.09e-56]` | `[0.1289636959041082060214493740052860517030518797050878 +/- 8.54e-54]` | `[11.00493258883897460897564821850395265240192820296076 +/- 4.23e-52]` |
| 1 | `[3787628.916378855450756866338154173894394242897605348 +/- 3.10e-46]` | `[17165593.40163714240985309383585387957245777940382266 +/- 4.85e-45]` | `[87196007.29832964316311760700561463913451214653984869 +/- 1.27e-45]` |

After the complete weak profile functional and the stated input factors:

| Density | Input power | Complete source target | Recorded upper-bound ball |
| --- | --- | --- | --- |
| 0 | 1/n | $H^{-5/3}$ | `[35.79515711814448643335176133679287005602943611769937 +/- 4.11e-51]` |
| 1 | 1/n^2 | $H^{-5/3}$ | `[81442613.63184392262326691733627210102831672924630389 +/- 1.04e-45]` |

These sources still require the original $J:H^{-5/3}\to H^{-2/3}$ and full outer primitive–mean readout. They are not part of $g_i$ and were not discarded as homogeneous-profile errors.

## 7. Exact reuse, counts and gates

All twenty pinned inputs, totaling **754166 bytes**, were current immutable small texts. The four Python sources passed the immutable AST check. There were zero archives read and zero binary inputs restored.

The ten successful inputs were potential43685624307, RV43719681982, SV43722805762, HP43726426053, BG43726985545, DG43720766795, RJ43728317408, C43702688640, W43694458725 and PC43740173506, all attempt1. The new execution individually checked their source, manifest, actual zero exit status of each scientific child, exact runtime and gate counts.

| Operation | Actual count |
| --- | --- |
| Successful old small receipts read | 10 |
| Original positive coefficients read | 18 |
| Saved complete column derivative bounds read | 44 |
| New profile bound-number recoveries | 18 |
| New common phase gap closure | 1 |
| New complete $H$ derivative bounds | 3 |
| New functional coefficients | 24 |
| New complete functional evaluations | 14 |
| Density-zero scalar receivers | 3 |
| Density-one scalar receivers | 3 |
| Complete extra-source receivers | 5 |
| Old successful numerical calculations repeated | 0 |
| Old profile, partition or calibration calls | 0 |
| Old amplitude, Taylor-tail, potential, Fuchsian or inverse-closure calls | 0 |
| Old row, word, integral, PC, PW or SP producer calls | 0 |
| New $\tau$ quadrature or truncation | 0 |

The twenty-three actual gate names, all passed, are:

1. the immutable new manifest fixes the same source, IN contract, runtime and scalar parameters.
2. all inputs are immutable small text conclusions or primary identity evidence, with zero old imports.
3. accepted complete run 43685624307/1 retains immutable success and its exact runtime.
4. accepted complete run 43719681982/1 retains immutable success and its exact runtime.
5. accepted complete run 43722805762/1 retains immutable success and its exact runtime.
6. accepted complete run 43726426053/1 retains immutable success and its exact runtime.
7. accepted complete run 43726985545/1 retains immutable success and its exact runtime.
8. accepted complete run 43720766795/1 retains immutable success and its exact runtime.
9. accepted complete run 43728317408/1 retains immutable success and its exact runtime.
10. accepted complete run 43702688640/1 retains immutable success and its exact runtime.
11. accepted complete run 43694458725/1 retains immutable success and its exact runtime.
12. accepted complete run 43740173506/1 retains immutable success and its exact runtime.
13. the six complete saved columns retain their original derivative orders, signs and physical means.
14. all eighteen read coefficients bound the same original positive algorithm and fixed three branches.
15. the reused cut columns and fold constants retain the complete same real family and signed disk.
16. the entire segment uses original canonical V and Fuchsian bounds without new old quotient evaluation.
17. P22 lies strictly in the original root piece and every tauT lies in the paid canonical product.
18. the new all27-piece phase gap is strictly positive and retains both physical input signs.
19. the complete nonzero root matrix keeps the analytic16384 strong multiplier qualification.
20. the complete new H=BTT+VB retains every canonical derivative and all-segment chain factor.
21. the six new all-tau coefficients retain the exact factor2 and the full root plus integral error.
22. all six scalar receivers and both exact inhomogeneous source rows retain their separate windows.
23. all new scalar conclusions are complete in their stated windows and every old producer remains unused.

## 8. Real pulls, capacity and recoverable publication

The actual terminal pull and README checks were:

| UTC | Before | After | Actual README difference |
| --- | --- | --- | --- |
| 2026-11-15T18:19:07.600344+00:00 | 96001fbab4e62356d30ebf5b105b381e7639fe06 | 96001fbab4e62356d30ebf5b105b381e7639fe06 | Empty |
| 2026-11-15T18:19:10.875156+00:00 | 96001fbab4e62356d30ebf5b105b381e7639fe06 | 603479e418a26498233a000e2e85cab418a5379c | Empty |
| 2026-11-15T18:19:15.194323+00:00 | 7233312b2a222f96d2315c3a55e263372958b7f1 | e4527195767d1686aaf41b72d65e273241d975c5 | Empty |

The separately reviewed rule receipt stays SHA256 65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1.

The complete published-tree audit at commit e4527195767d1686aaf41b72d65e273241d975c5 counted **14305 blobs and 199821564 bytes**, with untruncated metadata and every blob size checked. The final two-file publication projected **199872563 bytes**, below 200000000. This is that publication boundary, not a measurement of a later main head.

The earlier current-topic field in this same execution is **199870961**, corresponding to the earlier 33785-byte execution encoding. The final projected field uses the final 35387-byte execution and unchanged 15612-byte result. Both exact owned-delta stages remain recorded.

Before any post-science sync, commit or push, the worker emitted the complete 38529-byte recoverable envelope identified in section 1. The temporary native was 4722 bytes, SHA256 8f45526d76d88fd03219905531150f356c1e4f04951656ca3f98de2df5300159; it was not published. No arrays, new data artifact or Release upload was created.

## 9. Completed scope and the next receiver

The all-segment comparison now has a genuine three-phase gap and explicit complete scalar coefficients. Its root matrix includes the original nonzero shear; its variation-of-constants integral includes the entire $[0,1]$ segment, both state rows and every phase product. The conclusions keep $L^2$, $H^{-1}$ and $H^{-5/3}$ separate.

The next receiver must read these successful scalars, then charge true $J,L,B_{\rm op},\eta^{-1}$, $n_gT(q)$ at this exact P.22 cut and both free $R_2,R_3$ terms. Later strict normalizers, first-symbol coordinates, incoming inverse, natural stable factor, finite cross blocks and both means remain explicit obligations. The SP cut at $r_+-1/200$ is a different location; its numerical frame factors cannot be transferred here by name.

No old ray, scalar finite-part, KAM or successful source enclosure needs to be repeated. This successful scalar computation is locked for read-only reuse.
