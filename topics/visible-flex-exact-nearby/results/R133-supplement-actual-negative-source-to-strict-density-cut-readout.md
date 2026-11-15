# R133 supplement: actual negative source to strict density cut readout

2026-11-15, visible-exact-astra-0df9 / phase_inverse.

**Actual public computation completed.** Run **43716450174/1** returned child code zero and passed all **17 identity and scalar-completeness gates**. It evaluated six new cut budgets in **0.551217555000008 seconds**, with **zero old numerical enclosures recomputed**. Four cuts passed both strict cutoff97 inverse tests. The two closer cuts retain their complete raw-density conclusions but have no normalized conclusion from this sufficient test.

The smallest certified normalized ordinary-source gain among these six tested cuts occurs at $R=1/200$:
$$
 L_{\mathrm{ord},\,1/200}
 \ \text{has upper-bound ball}\ 
 [1.070261671286535620575711494618990773602113519183717666224766388
 \mathbin{+/-}2.10\,10^{-64}].
 \tag{A.1}
$$
Applying it to the unchanged complete genuine-source bound gives the upper-bound ball
$$
 [592508906452628.6432490715221676295460813990128011310960367890955
 \mathbin{+/-}1.2\,10^{-52}].
 \tag{A.2}
$$
These are upper bounds for the volume-source contribution to the specified old-circle density and its retained means. The actual root columns and affine-jump columns have separate gains below and were not evaluated in this run. No complete return, positive selection, raw-state $L^2$ inverse or core GH is asserted.

## 1. Immutable public execution

The deployed four-file commit is
$6d87bc850bc8150bd6acbe87ee9df5b885beaf3e$.
[The public run](https://github.com/Rogerhu12/math-research-public/actions/runs/43716450174)
used job $132818927229$, which ran from **12:57:19 UTC** to **12:58:04 UTC** and completed successfully. The mathematical child wall time was **0.8666110749999945 seconds**. Its runtime was Python 3.12.14, python-flint 0.9.0, NumPy 2.3.5 and SciPy 1.17.0, with 320-bit Arb arithmetic.

The exact producer, parameters and definitions are:

| Item | Repository path relative to this topic | SHA256 |
|---|---|---|
| Scientific source | scripts/fourfold_codazzi_negative_source_strict_density_cut.py | 179cc14abfeff1d8281a8971d5e6192439106839213f461e5be8bd1b9150e63c |
| Input manifest | notes/2026-11-15-R133-negative-source-strict-density-cut-CI-inputs.json | 7c07d303931747ef2d64779a0681a0a0bb5e452e15e2af330952028e2992f4fe |
| Public worker | scripts/fourfold_codazzi_negative_source_strict_density_cut_public_worker.py | 28e2d96e389830c40c3f6267f3b43952041612cc8cb2e1392492213c6f667a17 |
| Workflow, at repository root | .github/workflows/visible-exact-negative-source-strict-density-cut.yml | 3db5ae210260cf8f3372cd53a0bccc10b61ee1a8fe5c8922e334d548b130e46b |
| Mathematical contract | results/R133-supplement-complete-negative-source-to-strict-density-cut-readout.md | 4d44bbe7082d4ee967ebf9d02284b3510624624ab98adb087b8d0499eb030376 |

The exact invocation is the scientific source with
`--repo <immutable-science-root> --manifest <the pinned manifest> --manifest-sha 7c07d303931747ef2d64779a0681a0a0bb5e452e15e2af330952028e2992f4fe --out-dir <temporary-output>/consumers`.

The two published original small receipts are:

| Original receipt | Bytes | Git blob | SHA256 |
|---|---:|---|---|
| [execution.json](../notes/negative_source_strict_density_cut_ci/run-43716450174-1/execution.json) | 44767 | 79ef9ded8999c73c57f7911d7c5d289002320de7 | 318dd25bd0ac69f54c1d5c89e2e227e13d49b9b90cf8770656900d2646eb519c |
| [actual-result.md](../notes/negative_source_strict_density_cut_ci/run-43716450174-1/actual-result.md) | 7879 | 2c10511a1050dd055f7db74d226dfc4af3da13b2 | 72745bf35a11c472dd9f117989c3b19e90bf3b23822085ddda7265531bd70296 |

Both originals were read in full for this report. Scientific source, manifest and worker SHA values match the deployed files. All six cuts, the four successful normalized conclusions, all 17 gates and both original archives were checked against the execution metadata. The accepted source's first-row ball, mean ball, pair ball, full physical cover and canonical complete-conclusion hash agree exactly with the earlier successful G execution.

## 2. Typed conclusion and exact cut convention

Use the definitions and ordered matrices of the [proved N contract](R133-supplement-complete-negative-source-to-strict-density-cut-readout.md). Physical frequencies are $4j$, with
$$
 \Lambda_j=(1+16j^2)^{1/2},\qquad
 I=\partial_\phi^{-1}(1-\Pi),\qquad
 P_H=P_{\{|j|\ge97\}} .
$$
The original root remains inside
$$
 r_-\le r_*\le r_+,\qquad
 r_-=\frac{1191984371497}{5000000000000},\quad
 r_+=\frac{2383968743003}{10000000000000}.
 \tag{A.3}
$$
Every fixed cut is **$r_c=r_+-R$**. Thus its actual distance to the root is in
$[R-(r_+-r_-),R]$. This convention preserves the previously proved radius-$R$ Cauchy domain, including the entire uncertain-root band.

At the cut let
$$
 q=\sqrt{-K},\quad \eta=-\gamma m,\quad
 n_g=\frac{a_{\rm phys}^2}{m^2},\quad
 T(q)=\frac1{\sqrt{2q}}
 \begin{pmatrix}1&q\\1&-q\end{pmatrix},
$$
$$
 w=n_gT(q)h,\qquad y=Iw,\qquad z=\Pi w .
 \tag{A.4}
$$
The radial multiplication commutes with both $I$ and $\Pi$. The complete pair of means $z$ stays in the output. The previously certified multiplier
$C_I=\sqrt{17}/4$ is already included in the saved Cauchy fields consumed here; this run did not multiply it again.

The strict normalizers are the original ordered operators
$$
 T_1={\rm Id}+P_H S I P_H,\qquad
 T_2={\rm Id}+P_H S_2 I^2P_H,\qquad
 \widehat y=T_2^{-1}T_1^{-1}y .
 \tag{A.5}
$$
The finite head is the identity under both operators. Their complete coefficient bounds give
$$
 \tau_1=S_*/388,\qquad \tau_2=S_{2,*}/388^2.
$$
Only where both strict inequalities $\tau_1<1$, $\tau_2<1$ hold does the report use
$$
 K_{\rm inv}=\frac1{(1-\tau_1)(1-\tau_2)}.
 \tag{A.6}
$$

For an ordinary first source in $L^2_rH^{-2/3}$ and an independent constant second source in $L^2_r$, write its pair norm as $F_{\rm ord}$. Write the original mixed root norm as $B_{\rm root}$ and the sum of the actual affine-jump norms as $B_{\rm jump}$, exactly as N.3. The raw and, where certified, normalized bounds have the forms
$$
 \|(y,z)\|_{L^2\oplus\mathbb C^2}
 \le L_{\rm raw,root}(B_{\rm root}+B_{\rm jump})
      +L_{\rm raw,ord}F_{\rm ord},
 \tag{A.7}
$$
$$
 \|(\widehat y,z)\|_{L^2\oplus\mathbb C^2}
 \le L_{\rm norm,root}(B_{\rm root}+B_{\rm jump})
      +L_{\rm norm,ord}F_{\rm ord}.
 \tag{A.8}
$$
The vector density in these expressions has both wave rows. The second ordinary source is not projected away merely because it is angularly constant.

The original repaired family, frozen $\eta_0$, real $|\delta|\le10^{-8}$, full193 direction, physical even mean, circle measure and true $dr$ source measure are unchanged. For the accepted genuine source, the incoming coefficient window is the original two-column $H^{-4/3}$ space, with both signs $|j|\ge97$; the resulting old-circle density and mean output is complete, rather than projected back onto those input labels.

## 3. All six actual cut and normalizer tests

The table displays the saved ball centers to shortened precision for reading. The full directed balls, including both margins, are in the two original receipts. The logical conclusions use those full balls.

| $R$ | Exact $r_c$ | $\tau_1$ approximately | $\tau_2$ approximately | Both strict tests |
|---|---|---:|---:|---|
| $1/1000$ | $2373968743003/10000000000000$ | 1.149370049987 | 8.927655880126 | Not proved |
| $1/500$ | $2363968743003/10000000000000$ | 0.395446526530 | 1.071289959028 | Not proved |
| $1/200$ | $2333968743003/10000000000000$ | 0.088836237622 | 0.049280680551 | Passed |
| $1/100$ | $2283968743003/10000000000000$ | 0.019687923533 | 0.006464496728 | Passed |
| $3/200$ | $2233968743003/10000000000000$ | 0.001870889018 | 0.002175978776 | Passed |
| $1/50$ | $2183968743003/10000000000000$ | 0.006849896275 | 0.000606662689 | Passed |

At $R=1/1000$ both sufficient tests fail. At $R=1/500$ the first passes and the second fails. This is a limitation of these computed sufficient bounds; it is not a singularity theorem. Neither normalized output is asserted for these two cuts.

Every tested cut lies in exactly one saved one-sided row. The original common-row indices are, in increasing $R$ order, **3044, 2979, 2803, 2665, 2560, 2456**. The source checks the original complete norm row, forcing row, intrinsic row, common interval and analytic germ together. It would retain both sides at an exact join; no such double-side case occurred here.

The complete map factors are moderate; their displayed centers are:

| $R$ | $a_{\rm phys}$ upper budget | $|m|$ lower budget | $q$ lower budget | $n_g\|T(q)\|$ upper budget |
|---|---:|---:|---:|---:|
| $1/1000$ | 1.096885113689 | 1.119553062028 | 0.259200305575 | 1.885450635320 |
| $1/500$ | 1.096650475863 | 1.119323783907 | 0.392394786535 | 1.532369095476 |
| $1/200$ | 1.095961545137 | 1.118434581980 | 0.681533008856 | 1.163123982373 |
| $1/100$ | 1.094841218902 | 1.116300105623 | 0.949713965230 | 0.987060869261 |
| $3/200$ | 1.093753205414 | 1.113750302258 | 1.023191653992 | 0.975547714906 |
| $1/50$ | 1.092711415341 | 1.111261188523 | 0.991603369763 | 0.970978626040 |

All actual $q$, $\eta$ and $|m|$ lower bounds are positive. The failure at the closest two cuts arises in the explicit normalizer budgets, not in these basic nonzero gates.

## 4. Raw density gains remain available at every cut

These are independent complete conclusions even when the strict-normalizer test fails.

| $R$ | Raw root/jump gain, approximately | Raw ordinary-source gain, approximately | Accepted G source contribution, approximately |
|---|---:|---:|---:|
| $1/1000$ | 9.037177754400 | 0.285780653237 | $1.582113859420\times10^{14}$ |
| $1/500$ | 8.756975551979 | 0.391623852231 | $2.168073721139\times10^{14}$ |
| $1/200$ | 13.111540743422 | 0.927125937148 | $5.132673531165\times10^{14}$ |
| $1/100$ | 51.692287748763 | 5.169228774876 | $2.861743226704\times10^{15}$ |
| $3/200$ | 287.151932769019 | 35.168785696904 | $1.946983556787\times10^{16}$ |
| $1/50$ | 1516.257950915744 | 214.431255824108 | $1.187115565345\times10^{17}$ |

The contribution column uses the same unchanged complete pair-source bound at every cut. It is not a new radial integration, not a subtraction of two upper bounds, and not a minimum between different cuts.

## 5. Complete certified normalized results

For each passing cut the following are the exact recorded upper-bound balls. The mean coordinates remain in the common norm throughout.

### R = 1/200

| Final constant | Recorded upper-bound ball |
|---|---|
| Ordered inverse norm | `[1.154386506086905772432341511691351869495600060068403699177040055 +/- 1.67e-64]` |
| Root and affine-jump bracket gain | `[15.13578570821513993093484386426113638575447208934161386870284849 +/- 4.05e-64]` |
| Ordinary-source gain | `[1.070261671286535620575711494618990773602113519183717666224766388 +/- 2.10e-64]` |
| Accepted complete G source contribution | `[592508906452628.6432490715221676295460813990128011310960367890955 +/- 1.2e-52]` |

### R = 1/100

| Final constant | Recorded upper-bound ball |
|---|---|
| Ordered inverse norm | `[1.026720554111424489825817805261569726182610193610290319262867238 +/- 2.57e-65]` |
| Root and affine-jump bracket gain | `[53.07353432069722166256122557687794776646837504756946980491130847 +/- 4.02e-63]` |
| Ordinary-source gain | `[5.307353432069722166256122557687794776646837504756946980491130847 +/- 4.02e-64]` |
| Accepted complete G source contribution | `[2938210591446411.411710885341261210782332264586477975199836405143 +/- 4.82e-49]` |

### R = 3/200

| Final constant | Recorded upper-bound ball |
|---|---|
| Ordered inverse norm | `[1.004059207329237630226075239093055439497221880273424776803898599 +/- 1.36e-65]` |
| Root and affine-jump bracket gain | `[288.3175419991199086784411644178076252873417311343376645061028940 +/- 2.22e-62]` |
| Ordinary-source gain | `[35.31154308956511867778023580197218880364586657430797103524921062 +/- 2.73e-63]` |
| Accepted complete G source contribution | `[19548867667103120.42431992026430146606392712650481025686503590167 +/- 2.90e-48]` |

### R = 1/50

| Final constant | Recorded upper-bound ball |
|---|---|
| Ordered inverse norm | `[1.007508358705664002034361349061235794365342940651615580966900752 +/- 4.59e-64]` |
| Root and affine-jump bracket gain | `[1527.642559501534565660688369842702030121335326036299207720776432 +/- 1.02e-61]` |
| Ordinary-source gain | `[216.0412826105418017857886692311277728237168504435370296397369408 +/- 2.45e-62]` |
| Accepted complete G source contribution | `[119602885483437005.8110049583826020615860251569322864346562224223 +/- 4.43e-47]` |


The four cuts are separate output locations and separate coordinate maps. Their gains must not be combined entry by entry into an unstated common operator. The $R=1/200$ conclusion is the smallest displayed complete normalized source contribution among the tested cuts; no continuum optimization is claimed.

## 6. Exactly what was reused and what was new

The accepted source is the successful G execution **43714194714/1**, scientific SHA256
$a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7$
and manifest SHA256
$bbfbdbc206f4d724288f8ecb5d9613523f5103ae7c1276ff59f2aaa055476665$.
Its exact negative physical support is
$$
 [2147184947341121/9007199254740992,\ 
   2383968743003/10000000000000].
$$
Only the source is extended by zero outside that already paid interval when inserted in the larger negative Cauchy domain. No affine impulse is thereby removed.

The old source ledger retains all **21 first-row terms and ten independent-mean terms**, including all three raw local terms, both density windows, the complete nonlocal words, the Piola factors, the physical means and the original uncertain-root-band weight. Its canonical complete-conclusion SHA256 is
$39217d2ceb93906e4f4faa07d19a1259ea392e64fb40fb28e6bb874ec0aeb07c$.

The three accepted aggregate balls were consumed byte-for-byte:

| Accepted G aggregate | Original upper-bound ball |
|---|---|
| First row | `[553601189236066.1263364956026546096351225843168051840125046266325 +/- 4.63e-50]` |
| Independent physical mean | `[3338315864266.082933296737943933621627342049304710558785120835132 +/- 4.38e-52]` |
| Complete pair | `[553611254470496.0277809199507349102461437715614759105011257403224 +/- 4.23e-50]` |

The run restored all 1328 original norm rows and their matching original forcing rows, the six previously completed Cauchy cases and only three complete intrinsic natural parts. The physical radius was read from the original whole-cell intrinsic jet; it was not reconstructed from a different interval. No old target, FFT, repair, intrinsic jet, angular norm, fold, Airy transport, Taylor coefficient, Cauchy energy, source row or radial source integral was recomputed.

The new mathematics consists of six cut coefficient closures, their explicit $\tau_1,\tau_2$ tests, and multiplication of each accepted complete source bound by the new complete readout gain. No additional source terms were accepted as zero.

## 7. Original restoration and scientific gates

All **22 pinned inputs** were verified before scientific execution: seven exact current small texts, five exact historical blobs, six current texts identical to the pinned legacy input, and four exact members of two original Actions archives. The immutable Python closure contained five source files and passed AST parsing before the unique scientific child.

The two original archives were downloaded only into temporary work. Their complete ZIP hashes and every natural-member hash were checked:

| Original archive | Bytes | SHA256 |
|---|---:|---|
| 14124978138, original forcing run43624260519/1 | 6529847 | 4f23a806604bec41670b77af93bf79cbaf131a011bdaf68cbf7bbf16e7319e10 |
| 14110242321, original body rows2133--3066 run43583838026/1 | 4357089 | 0fba4d340b7f17375a3131e002f300a3248a0148db2f2af4c9db0ca43cb1636b |

The forcing member is 6577892 bytes, SHA256
$54a79bf80df641797b28f998fe547c93d64b58ea329b675f3d62d23d4f161d47$.
The three whole intrinsic parts are:

| Original natural part | Bytes | SHA256 |
|---|---:|---|
| rows-02389-02645.json.gz | 1170241 | 846a2cbb93477eb545661c93dec4acf80517f6ff634dada2993d2af3055e5c8d |
| rows-02645-02901.json.gz | 1170546 | c7b0e333d4f9f113e148cc3f712e9c468be09cc6f443b0fb0d08f93bc2f7995a |
| rows-02901-03066.json.gz | 753252 | 47478cc195c394afd6a396faeb2c473fcde534812823c90391c84f0b678e4d8f |

None was reuploaded or modified. The complete input-receipt hashes are recorded separately for worker and scientific scopes in execution.json.

The 17 passed scientific gates establish: exact source/input identity; original native and completed-child identities; the same full real parameter family and root bracket; all 1328 row matches; both original Cauchy windows at all six radii; unchanged intrinsic identity; restoration of exactly the three required intrinsic parts; correct fixed cuts and zero intrinsic bump there; the already successful G child and all 25 G gates; unchanged source windows and all 31 terms; saved same-germ cut jets and physical radius; complete cut evaluation; exact correspondence between asserted normalized conclusions and the two strict tests; reuse without reintegration; separate root/jump/head/mean columns; only new cut arithmetic; and no unproved upgrade to raw $L^2$, GH, positive graph or full strong return.

The gate count therefore certifies **six faithfully evaluated budgets and four proved normalized readouts**. It does not silently reclassify the two failed sufficient inverse tests as successful.

## 8. Publication and capacity evidence

The actual terminal pull and README checks occurred at:

| UTC | Before and after commit | Actual root/topic README diff |
|---|---|---|
| 12:57:50.924619 | bdf728aa37980d247e279f404390c11991b2cbdc | Empty |
| 12:57:58.750589 | bdf728aa37980d247e279f404390c11991b2cbdc | Empty |

The separately reviewed rule receipt SHA256 is
$65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1$.

The published-tree API inventory was complete, untruncated and requested no blob bodies. It counted **14113 blobs and 199064002 bytes** in this topic at the recorded base commit. The exact two owned small-file additions gave a projected publication size of **199116648 bytes**, below 200000000. This is the run's audited commit-specific size, not a claim about later unrelated commits.

Before any post-science Git publication, the worker emitted a recoverable UTF-8 stdout envelope of **42859 bytes**, SHA256
$f215352d38df437dd1e3fb190e87487842a5a50376a19a88f318da48dd42ea83$,
containing the actual small conclusion and scientific identity/gates. The temporary scientific process was 40327 bytes, SHA256
$98cd609c1cdd49e33c8efcd2e5a26a213572a6557ec4e5fa7dbf3c4bc36dae4f$.
The temporary native was 16269 bytes, SHA256
$f952ce74f78e46556b33e97d6c9920e7fd4b75317cbc6f4c43a98be77e76f1fe$.
Only their hashes are retained here. No native, arrays, new data artifact or Release upload was published.

## 9. Consequences and the remaining operator chain

This execution pays a concrete missing type conversion: the completed negative ordinary-source estimate now reaches the exact old-circle strict density coordinates and their means at four certified cuts. It does not identify an $H^{-1}$ physical state with an $L^2$ state. The primitive and both ordered normalizers are explicit.

For later use, the $R=1/200$ result supplies the complete volume-source gain in (A.1), the complete G source contribution in (A.2), and the independent root/jump gain recorded above. A successor may read those concluded scalars directly. It must not recompute this successful cut arithmetic or the successful source enclosure.

A complete return still has to account for the actual root/affine-jump inputs, propagation from the selected cut in the same density coordinates, ray and KAM coordinate maps, positive regular boundary selection, finite/high couplings, and the full return remainder in its proved Sobolev window. In particular, the genuine source contribution in (A.2) is an upper bound for one retained operator contribution; its large size neither proves failure of the true inverse nor makes the remaining contributions dispensable.

The two nearer cuts may be revisited only through a separately identified new bound or new mathematically justified normalizer choice. Their failed sufficient tests and their valid raw readouts remain part of the immutable record.
