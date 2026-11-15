# Actual complete free-Airy first-omitted strict-cut scalars

Status: **proved numerical scalar consumer; successful computation locked**.
Public run **43763658978 / attempt 1**, job **132963817688**,
completed successfully on 2026-11-15 at 21:26:47 UTC. Its scientific child
returned 0 and passed all **24 structural gates**.

This is the first successful evaluation of the new finite scalar recipe
in [FA](R133-supplement-complete-free-Airy-first-omitted-strict-cut-columns.md).
It gives a complete strong error at the actual P22 cut and separately
bounds the corrected first-order map on the negative Sobolev window.
It retains the full original means, both physical signs, both
oscillatory branches, actual J and I, and the entire finite normalizer
difference. No successful old target was rerun.

The normalized cut error is approximately $3.87\,10^{25}$. This is a
finite complete upper bound; its size does not establish an incoming
inverse or a full return inverse. The corrected first-order negative-window
bound and its one radial conversion are separate quantities, listed below
with their exact directed upper enclosures.

## 1. Exact target and five completed readouts

Use the same terminal-Ai **free** P8 first column, not the later genuine
potential-corrected amplitude. The fixed cut is
$$
r_c=76285779072683/320000000000000,
$$
and the original root bracket gives
$$
\rho\in[1/262144,\;1220703413/320000000000000].
$$
The family is the original selected real family $|\delta|\le10^{-8}$
with the same fixed intrinsic parameter $\eta_0$, complete 193-mode
direction, continuous correction and original physical root piece 2549.
The input contains both signs with $n=4|j|$, $|j|\ge97$, hence
$n\ge388$. Both oscillatory branches are retained in each such column.

Let $F$ denote the full raw primitive-density column of FA, with radial
factor $n_gT(q)$ and no added reaction gauge. Let
$\mathcal N=(1+B_s)^{-1}(1+A_s)^{-1}$ be the same saved ordered TN
normalizer. Let $B_{\rm free}^{[1]}$ be exactly FA.28, including the
ordered correction $-S A_{\sigma,0}/(i\epsilon\kappa_\sigma)$.
The successful target is
$$
\|\mathcal NF-B_{\rm free}^{[1]}\|_{H^{-4/3}\to L^2}
\le C_{\rm free,cut}.
$$
The reference maps have the source and output conventions in FA; the
independent physical mean coordinates and complete finite cross blocks
remain in the surrounding coupled problem.

All balls below are copied verbatim from the complete scientific JSON.
They enclose directed upper bounds, not approximate computed solutions.

| Completed readout | Directed upper enclosure |
|---|---|
| Normalized free cut strong error C_free,cut | `[38664672163727558112968574.2577927306121087139570 +/- 2.23e-23]` |
| Raw cut error after one same-TN forward L2 fee | `[38729228626506483641614118.8970308928492768731554 +/- 2.56e-23]` |
| Uncorrected leading map on H^(-4/3) | `[1476580743563.54196295590382950892292918955431867 +/- 4.74e-37]` |
| Corrected B_free^[1] on H^(-4/3) | `[6772234063494.70164434247142371631881746312808436 +/- 1.83e-36]` |
| SF26 Kc_minus, corrected map divided once by the same-cut n_g lower bound | `[7054742132652.50198920429183415356661416038507582 +/- 3.19e-36]` |

The second row already includes the forward TN factor. The fifth row
already includes the radial $n_g^{-1}$ factor. Neither is to be
multiplied by the same factor again. The first row is not a waist norm.

The two cutoffs have different roles: the input starts at $|j|=97$;
the saved moving-circle normalizer cutoff is $J_s=268435456$.
Its finite difference has complete support through $J_s+191=268435647$.
No identification of a moving projector with a phase projector is made.

## 2. Actual identity, runtime and preservation

The event and scientific checkout both equal
`0c214d0b9b0c4cfa7c6ec363f253e419d14aae01`.
The job's twelve recorded steps all succeeded. The actual runtime is
Python 3.12.14, python-flint 0.9.0, with 320-bit Arb arithmetic.
There was one scientific child. Its wall time was
0.3130439539999941 seconds and the scientific stage counter was
0.0216311259999884 seconds.

| Published input | Git blob | Bytes | SHA256 |
|---|---|---|---|
| FA proof | `acfb0cfd9a2598c00a6b29c2db05041d0340cba9` | 27814 | `24216c6d78f1261e16b9d53030fb2b899a94e9e9d8900e7fea79746ef32d96af` |
| Scientific source | `9e0a75461e0b8302a82e0444828a2c86379c3443` | 48827 | `a6c89d502f7583bba3b663c4296ec462fd892ad01e94427dbe55bc1c3d304954` |
| Public worker | `8ad835e02ae5578a8e231fa684c845c08e0d1a96` | 49611 | `11088777a3e44ffde5a0f1ac26fcac35a0b9360c11a98349b7aad335b52be491` |
| Frozen manifest | `8ff0dbf8a5042f30f7f31ad68f9c29d93a6af95e` | 23418 | `d06951509b4af18ce5039997c032b6377c0c55be07bd01f79a686c2471e4dd6b` |
| Workflow | `547a6793c61ec7953e2d0d9fbb63dcbbeacb4cfd` | 4241 | `f443aa16bc8c2cf8c2695c4c90b5f2695f27cbbff4aaf99b58a4dcef9de57e98` |

The source is `scripts/fourfold_codazzi_free_Airy_first_omitted_cut_scalars.py`;
the worker adds `_public_worker` before `.py`. The manifest is
`notes/2026-11-15-R133-free-Airy-first-omitted-cut-scalars-CI-inputs.json`.
The workflow is the repository-root
`.github/workflows/visible-free-airy-first-omitted-cut-scalars.yml`.

All twenty inputs, totaling 646,791 bytes, matched their exact manifest
roles, byte counts and SHA256 values. Ten are current small texts and ten
are original historical inputs restored temporarily at commit
`a3d84d905ce72e3a854874bbe98d119623f3f8de`.
The historical tuples remain those of the frozen RV manifest with SHA256
`4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded`.
The full five-file AST closure passed. No old scientific source was
imported or executed, no original array was changed, and no old Taylor,
fold, radius, profile, J, normalizer, coordinate or integral was recalculated.

The first attempt, 43762821220/1, is separately recorded in
[the preserved identity-gate failure](R133-supplement-actual-free-Airy-cut-identity-gate-failure.md).
It stopped before any new numerical target. The successful source differs
only in checking the actual O.2 strings instead of the nonexistent word
`vartheta`; its mathematics is unchanged. The worker's independent repair
makes the displayed group counts and failure scope reflect the science.

## 3. Saved original sources actually consumed

The four successful small receipts are RR 43750683671/1,
TN 43752771157/1, TC 43754703603/1 and ST 43757644616/1.
Their full source, manifest, runtime and success identities were checked.
Their numerical conclusions were read, not re-created.

The original complete fold stage has 4,501 bytes. The complete original
free-amplitude radius stage has 20,924 bytes and SHA256
`8b31b1c0030f892ec763d32ecf7b4968d468c5f93b30bbfe7408d6bf0b4892d5`.
Its radius $9\,10^{-6}$ and physical strip $1/512$ strictly cover the
new cut and strip. The saved $p=0,1$, $q=0,\ldots,3$ amplitude bounds
are copied verbatim; the native stage also retains its full original
$p=0,1,2$ data. The original child 43669106351/1 passed all ten
mathematical gates before its independent formatter failure. That failure
identity is preserved, not relabeled as wrapper success.

The free $w_1$ is not substituted by $w_1^V$. The same complete
direction and full parameter disk are retained. The new higher angular
bounds use positive Cauchy margins between physical widths $1/512$
and $1/1024$; old finite Taylor sums and old tail bounds are not repeated.

## 4. New full-domain and coefficient gates

| Complete quantity | Directed enclosure |
|---|---|
| Negative real T lower bound t_minus | `[1.70443496747448880369391637399607647581261784951e-5 +/- 1.89e-53]` |
| Full original-strip T upper bound, from the same full A_p | `[1.77000345209349402882117476874062226189033505433e-5 +/- 4.44e-53]` |
| Full complex eta lower bound | `[1.25299547095054573079366467377879882466593863889 +/- 3.72e-48]` |
| Point determinant lower bound | `[0.999999088311039106977335269150430840071277597656 +/- 3.75e-49]` |
| Complete H_epsilon inverse entry-sum | `[2.00000273509604443523450264682372786161951102264 +/- 3.39e-48]` |
| Complete M_epsilon entry-sum | `[4.79944786675732313099369148555388459052902884296 +/- 4.78e-48]` |
| Raw radial wave entry-sum | `[11.2466119539119840182606731076929702100232413982 +/- 4.71e-47]` |
| Holomorphic x-1 | `[4.55844376549463516474490522033794083355064594078e-7 +/- 5.42e-56]` |
| Holomorphic y | `[2.68755176938555114142267323450591210618838716970e-11 +/- 4.07e-59]` |

The complete initial angular arrays for $H^{-1},M,\ell,b_{\rm loc},d,u,v,
w_0,w_{0,r},w_1,w_{1,r}$ through order six are saved in
`complete_new_initial_angular_jet_conclusion`. They are component-sum
majorants. Real TC phase derivatives are never promoted to holomorphic
suprema. The original fold full strip remains $3/128$, and the new
amplitude strip is $1/1024$.

## 5. Complete finite J/I calculus, with every mean

FA.13 constructs four new inverse-amplitude vectors. Their complete
angular arrays have lengths 7, 6, 5 and 4 respectively. No low residual
coefficient is dropped numerically: degrees $-1,0,1,2$ vanish by the
exact ordered FA.13 identities. The remaining four positive coefficients,
all six old-mean terms, both inner primitive tails and all six outer
coefficients are saved.

| New inverse vector | Highest saved angular derivative | Zero-order component-sum upper |
|---|---|---|
| g0 | 6 | `[7.81885007288524105703017108700854985723796416314 +/- 2.33e-48]` |
| g1 | 5 | `[8400.06222611334434199353399410073145359829476477 +/- 4.35e-45]` |
| g2 | 4 | `[2130648.57579397569559317965492174061828393594628 +/- 2.48e-42]` |
| g3 | 3 | `[994225778.682706299573306659921160076497709518597 +/- 7.27e-41]` |

| Complete positive residual coefficient | Directed upper |
|---|---|
| R3 | `[430491500156.928868192799144851448057572870739968 +/- 7.54e-39]` |
| R4 | `[7345729953.00380576511854092111829552695692097600 +/- 5.66e-40]` |
| R5 | `[3318937535091.69558585796690551991146182753423719 +/- 1.58e-36]` |
| R6 | `[1494845169210281.94842145051978836890408124209395 +/- 4.10e-33]` |

| Original-mean positive term in FA.15 order | Directed upper |
|---|---|
| 1 | `[34.4832000566239026526439424103813651426114748279 +/- 3.72e-47]` |
| 2 | `[1.54027211721239992180307438792692391438498565141 +/- 3.11e-48]` |
| 3 | `[14.6744178185408167992973284007087746452887014352 +/- 3.68e-47]` |
| 4 | `[0.617002205801901869030780306741396553305227534869 +/- 3.28e-49]` |
| 5 | `[0.000912996538856648206337031541020394460541758336305 +/- 3.82e-52]` |
| 6 | `[0.0259014734058831454345689569428334741542453514640 +/- 2.35e-50]` |

| Complete retained primitive quantity | Directed upper |
|---|---|
| Sum of all six original-mean terms | `[51.3417066681237610364160314942423141242051765592 +/- 2.40e-47]` |
| Inner uG primitive remainder | `[18542514989.1484788682978599149918737977871056030 +/- 4.68e-38]` |
| Inner vW primitive remainder | `[80213708.2242715753588954036274987806502185953207 +/- 1.11e-41]` |
| Full outer primitive derivative remainder | `[284309802823.282959789610699122122348277720702871 +/- 4.31e-37]` |

| Outer coefficient | Highest saved angular derivative | Zero-order entry-sum upper |
|---|---|---|
| B0 | 6 | `[198.828792126291438402931218609728192065527265885 +/- 2.94e-46]` |
| B1 | 5 | `[261183.114353438485730127323908507547455799206027 +/- 3.45e-43]` |
| B2 | 4 | `[146412765.346445332754461447457266695710844956793 +/- 2.79e-40]` |
| B3 | 3 | `[83865349097.8413585813379971317969361173718478099 +/- 4.24e-38]` |
| B4 | 2 | `[37893747247600.1748417917247324532555775328969132 +/- 8.83e-36]` |
| B5 | 1 | `[17059812897082859.9036370893084774277641650962546 +/- 8.99e-33]` |

These tables are compact readouts. The complete derivative arrays,
outer density-amplitude arrays and weighted residual coefficient remain
in `complete_new_finite_primitive_conclusion` in the scientific JSON.
All three original-I expansions retain their differentiated amplitudes
and projection means. The six mean terms are not imposed to be zero.

## 6. Global real Airy bounds and complete reconstruction

The real negative-argument remainder theorem in DLMF 9.7.iii is used with
the exact coefficients in 9.7.2 and the two real expansions 9.7.9--10.
The source records exact rational $u_0,\ldots,u_5$ and
$v_0,\ldots,v_5$, including $u_1=5/72$ and $v_1=-7/72$.
The valid domain is every real $t>0,n>0$. **No assumption
$n\omega\ge1$** is made at this very near-root cut. No Airy remainder
ball is differentiated.

| Complete profile or mean envelope | Directed upper enclosure |
|---|---|
| Real omega lower bound | `[4.69115080257431095640503384853980349120794632575e-8 +/- 4.13e-56]` |
| Scaled profile upper | `[55323364702560.7641059909040561282932699009043575 +/- 3.73e-35]` |
| First inverse-frequency profile | `[12998345.2652698766934582623680364434026787399684 +/- 4.27e-41]` |
| First omitted scaled Airy remainder coefficient | `[8328600610737627824.46483034686662944941446833415 +/- 2.64e-30]` |
| Original mean E_(13/6) | `[183906003.848061872723734857964922030161171499334 +/- 5.33e-41]` |
| Original mean E_(19/6) | `[999854641920.685047646351206906631448108756702796 +/- 3.82e-37]` |

The original mean uses physical contour width $1/1024$ and the proved
exponent lower $1/2048$. The full reconstructed column has the
$n^{-2}$ error required by FA.24--25. The actual full-$L^2$ inverse
constant used for J is $0.825332620$; the different RR
$H^{-5/3}$ inverse is not substituted.

| Reconstruction contribution | Directed upper enclosure |
|---|---|
| Full J error after the outer old I | `[56081295856933503116778918.1970632313276785688042 +/- 3.45e-23]` |
| Full outer old-I tail | `[3932243727526405793446820.59426429107809623393485 +/- 3.54e-24]` |
| Full outer old mean | `[1267553074025.32955997283308617667356212448805949 +/- 2.28e-36]` |
| Complete reconstruction coefficient | `[60013539584461176463299764.1208874952388609794127 +/- 5.00e-23]` |
| B2 through B5 times complete profiles | `[50141633950197633130588.6156622759727298713801237 +/- 2.81e-26]` |
| B1 times the first Airy correction | `[3394948297824.45791274780777275578473615651036191 +/- 4.48e-36]` |
| B0+z B1 times the complete Airy remainder | `[7262382727675470824103.93568566281628255867296030 +/- 3.85e-27]` |
| Complete Airy remainder coefficient | `[57404016681268052252517.0092606865967851858378201 +/- 2.47e-26]` |
| Full unnormalized first-omitted column coefficient C_pre | `[60070943601142444515552281.1301481818356461652505 +/- 2.98e-23]` |

## 7. First-frame error, finite normalizer and negative-window input

The exact first primitive contains $-\Pi(ea/\kappa)$.
FA.26--27 retain this term and its complete second-primitive remainder.
Their norms are charged in the first-frame error; they are not silently
inserted into or removed from the explicit leading map FA.28.
Any later independent waist projection rank remains separate.

| Same-cut factor or first-frame bound | Directed enclosure |
|---|---|
| Complete E0, each branch | `[8426739.19296109330998006904074816875340866489779 +/- 2.47e-42]` |
| Complete E1, each branch | `[57183087024.4089649613627543002173392769142793156 +/- 1.05e-38]` |
| Complete frame column coefficient | `[203043828978758494.187089909970396514874132189558 +/- 2.73e-31]` |
| Both-physical-sign Hilbert--Schmidt factor | `[0.642441524982631459322115502503065068162439190965 +/- 3.03e-49]` |
| True U_Phi on H^(-4/3), read verbatim | `[1.000030048188231229134115417801219276946586925788832 +/- 3.61e-52]` |
| Different U_Phi inverse factor, recorded and not used instead | `[1.000030048073558490599145897215313190215308870298426 +/- 2.28e-52]` |
| TN ordered L2 inverse, read verbatim | `[1.001672387764244768693237132423321294220230365454558 +/- 3.00e-53]` |
| TN ordered L2 forward, read verbatim | `[1.001669649816389437916461198297920696771426256888629 +/- 1.08e-52]` |
| Full strong TN R_N, read verbatim | `[1712923776.640779712602431596288453109737234585600165 +/- 3.77e-43]` |
| Complete finite F_S, read verbatim and norm-paid | `[3747336834.184293827011820228209080780492048319896249 +/- 2.05e-43]` |
| Same-cut n_g positive lower bound, read verbatim | `[0.9599548695266653840650933988066207983966154782959841 +/- 4.54e-53]` |

The complete split is the ordered FA.31 identity
$$
\mathcal NF-B_{\rm free}^{[1]}
=\mathcal N(F-\mathcal L)
 +[(1-SI)\mathcal L-B_{\rm free}^{[1]}]
 +(F_S+R_N)\mathcal L.
$$
Its three actual strong fees are:

| Complete strong contribution | Directed upper enclosure |
|---|---|
| `TN_inverse_times_full_n2_remainder` | `[38656609517610988178629321.2322443249795024423586 +/- 4.20e-23]` |
| `full_finite_FS_and_strong_RN_times_same_leading` | `[8062515672782806913028.41630171859285956514291989 +/- 2.88e-27]` |
| `full_first_frame_remainder` | `[130443787127426224.609246687039746706455415862269 +/- 5.42e-32]` |

The full first-omitted reconstruction dominates this particular upper
budget. This comparison is a description of the completed positive
bounds; it is not a lower bound on the true error.

The leading norm uses $M_aC_\Phi=M_{a/\kappa}U_\Phi$, not the inverse
density map. The input inverse-frequency norm is paid once.
For vector or matrix coefficients, the $H^2$ bound is the sum of scalar
component $H^2$ norms, with the actual majorant
$a_0+\sqrt2a_1+a_2$; it is not an uncharged Euclidean replacement.
The corrected first-order negative norm also includes the full band-192
S multiplier, including its zero mode. Its complete multiplier upper is
`[5325567.90984898512323347311417741472126866077049 +/- 1.61e-42]`.

The true same-cut TN forward conversion and the distinct ST radial lower
bound are used once in their respective final outputs. The cut density
constants are not reused as waist density constants. No finite
compression inverse follows from this calculation.

## 8. All twenty-four actual gates

Every item below is recorded with `passed=true` in the scientific JSON:

1. the public repository exact Python flint and320-bit runtime are actual.
2. all current texts and exact temporary historical originals match the frozen complete manifest.
3. the full old primitive J ordered coefficient and global real-Airy remainder identities are fixed.
4. read successful complete RR_execution with its exact source manifest runtime and all gates.
5. read successful complete TN_execution with its exact source manifest runtime and all gates.
6. read successful complete TC_execution with its exact source manifest runtime and all gates.
7. read successful complete ST_execution with its exact source manifest runtime and all gates.
8. all three saved receivers use the identical P22 root family and full original means.
9. read U_Phi and its inverse distinctly and retain both successful TN windows and the full finite difference.
10. the original4501-byte complete fold and full coefficient domain are consumed without a producer call.
11. the old whole-piece child and all ten mathematical gates succeeded before its preserved formatter failure.
12. the saved free correction has the same complete193 direction fixed eta piece and full parameter disk.
13. one complete old h9e-6 radius stage has its original native process publication and exact bytes.
14. the old full p0-p2 q0-q3 holomorphic budgets are read at width1/512 on a strict radial superset.
15. the new point inverse and complete old-strip domains are positive at the identical strict cut.
16. all initial complete component-sum jets and physical radial readout bounds are finite and correctly sized.
17. four new complete inverse coefficients six exact means two inner tails and all six outer coefficients are present.
18. every primitive has its differentiated coefficient and all low residual degrees are canceled only by FA13.
19. the complete real Airy profiles and original-mean envelopes cover all n>=388 without a large-phase assumption.
20. the complete J residual three outer-reconstruction fees and all Airy polynomial remainder groups are finite.
21. the complete first frame both sign inputs corrected negative-window map and same-cut forward conversion are paid once.
22. all exact old bytes remain unchanged and no successful old numerical target was called.
23. the full original means finite map and all new scalar groups survive in the saved conclusion.
24. all twenty-four structural gates are complete for the exact new strong-cut scalar scope.

## 9. Exact output and prepublication recovery

All three published outputs lie in
`notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/`.

| Complete output | Git blob | Bytes | SHA256 |
|---|---|---|---|
| `execution.json` | `bef7897d1b501751b8b29bbb82a46bdb05496d28` | 17821 | `735c8053b56cc240e3fdfb050d95ef2cbb17c26a376aa4132530d50687474c0a` |
| `actual-scientific-conclusion.json` | `2001f4e2eeece1cda56b18b90dccab04b7f6d336` | 35718 | `2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2` |
| `actual-result.md` | `51572d26d84fb9228c988c2dbea03c86533ecc52` | 4900 | `c3cb68dd503aa69c762fe37b71ce11d2469eb8f67a13e814afa2403f0beb8015` |

The 35,718-byte scientific file is complete, not a selected excerpt.
It contains every actual new scalar/jet group described above and all
retained source identities. The complete small science and report were
printed before any Git publication, in a 40,906-byte payload with SHA256
`8355ad15f8f2c11a7369561c842a75aa3c5068d8d6e4afe6c6daa480ca9fea71`.
Reconstructing that exact payload from the saved science and the report
before its later publication-time README entry reproduces both its byte
count and SHA256. The saved process prepublication record was 15,229
bytes, SHA256
`31bfc036ff8524072df6a68e6ce5d1afc9cf999b908ec10ca06bf118478f7a88`.

The temporary scalar-native serialization was 15,284 bytes with SHA256
`3154b201d1695d3d466ed1a9a039c5cc3c5f4b197d4f81cc83cb2b585bddaa77`.
It and the original three restored binary inputs remained outside Git.
No new arrays, artifact, or Release were persisted. The complete
scientific JSON is sufficient for all subsequent read-only scalar
consumers.

Actual true README pulls were recorded at 21:26:32.531118 and
21:26:39.235311 UTC, both to
`0c214d0b9b0c4cfa7c6ec363f253e419d14aae01` and both with empty README
diffs. The publication check at that base recorded 199,632,493 topic
bytes and a projected 199,690,932 bytes. These are the actual check's
historical values, not a claim about later repository size.

The successful numerical target is locked. Its complete scalar
conclusions may be consumed verbatim; its new coefficient, mean, tail,
profile and norm budgets must not be recomputed merely for a later
wrapper or report change.

## 10. Exact boundary of this conclusion

FA now supplies the complete strict-cut error and corrected negative-window
input needed by the later strict-propagation contract. The complete
original means, auxiliary finite terms and transported finite spans
remain mandatory.

This calculation does not provide the later waist leading receiver,
an incoming/outgoing inverse, a complete return $R_0$, a finite Schur
inverse, or a nonlinear PDE solution. Every such claim still requires its
own compatible full operator and boundary data.
