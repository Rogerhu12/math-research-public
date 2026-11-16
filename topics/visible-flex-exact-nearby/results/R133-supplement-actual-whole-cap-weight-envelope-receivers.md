# R133 supplement: actual whole-cap second- and fourth-power envelope receivers

**Status: proved scalar consumer, complete original successful run retained.**
This note records the first and only execution of the whole-cap envelope consumer. Public Actions run **43780532148, attempt 1**, job **133016457266**, completed successfully with child return code **0**, all **22** scientific gates, all **12** complete weight/domain rows, both powers in all **24** full-interval integrals, and both complete posterior selections.

The two selected complete affine97 bounds are approximately $1.3682160215\times10^{-7}$ and $1.3630116203\times10^{-7}$. Their exact directed records appear below. They improve the corresponding complete SC3 posterior rows for the same physical objects and domains. The nonlinear body term remains the dominant paid error. The known signed97 model has not been substituted for an unknown-solution error.

The proof is the frozen [whole-cap envelope theorem](R133-supplement-whole-cap-envelope-from-completed-radial-weights.md), CEB.5–27, followed by the new directed scalar calculation and the complete saved-input checks described here. No old Gram, Hessian, signed97 model, radial weight, root, flow, source, or interval producer was executed again.

## 1. Actual public run and immutable scientific records

The workflow is [visible-whole-cap-weight-envelope.yml](../../../.github/workflows/visible-whole-cap-weight-envelope.yml). Its unique push event used commit `aecb91ea0fb33f32e68021169c6999531332e0d9`; the run was created at **2026-11-16 00:28:03 UTC** and the completed/success API record was updated at **00:28:51 UTC**. The actual job contains **12** successful step records; their recorded step numbers are not a count of scientific gates.

The following are the complete original publications, with paths relative to this topic:

| Original file | Git blob | Bytes | SHA256 |
|---|---|---:|---|
| [actual-scientific-conclusion.json](../notes/whole_cap_weight_envelope_ci/run-43780532148-1/actual-scientific-conclusion.json) | `5491df458307aaaf3cfca61c6eb1699b44b89e60` | 52340 | `96de85be729484f66cb0509138053c19638e39c359c244731587e17eb1cc9694` |
| [execution.json](../notes/whole_cap_weight_envelope_ci/run-43780532148-1/execution.json) | `f98df8d8bcf5133ee01aca30e031235a63936276` | 14855 | `8031cf3f4654344617750c2af8e12ac62e5db5445285a2bdb5096a7eec40f7ac` |
| [actual-result.md](../notes/whole_cap_weight_envelope_ci/run-43780532148-1/actual-result.md) | `93785087d9ceab0e3934f10af499de8a07d0db0b` | 8700 | `489b0d134384c7070a8eeae4de03793bec728ed46632e6fbe8cb52c2ec470b92` |

The complete scientific file has `complete=true`, `proved=true`, `actual_returncode=0`, no failure, and `complete_whole_cap_envelope_consumer_paid=true`. The execution independently records the complete mathematical receipt and zero child return. Python **3.12.14**, python-flint **0.9.0**, and **320-bit** directed arithmetic are the exact actual runtime.

The scientific checkout is `7b648f9ee59fb6c91752e1981def7cfde00bab5b`. It is separately recorded from the workflow event commit. Successful target identity is given by the frozen source, parameters, mathematical input hashes, and runtime; neither a later documentation commit nor a local publication commit changes that identity.

## 2. Identical physical object, parameters, and measures

Let $y=W_*(\gamma,f)-\widehat W$ be the **same physical cap pair** used by SC3, in its original physical angle. Its $C$ mean is retained. It is not the moving-coordinate difference $Q_{\rm cap}-\bar Q$, and the body is not recentered.

The exact retained parameters are

$$
I=[9/10,25/8],\qquad \ell=89/40,\qquad
\rho=3/10^6,\qquad \zeta=99/10^{11},\qquad d=10^{-10}.
\tag{CEBA.1}
$$

The radial measure is the actual ordinary $dr$. Angular $L^2$ uses the normalized full physical circle. The original reflection convention and all signed angular modes are retained. No factor of angular length or $\sqrt2$ is introduced.

The two domains retain their original physical trace hypotheses:

| Domain | Complete physical $\gamma$ bound | Other retained cap hypotheses |
|---|---:|---|
| Full original cap product | $10^{-9}$ | The original cap radius, outer $C$ nonmean radius, and normalized height ball |
| Tail inner-curvature subdomain | $1/(128\cdot10^9)$ | The same hypotheses, with this stricter condition on the same true $\gamma$ |

In both rows, the actual input $\gamma$ must equal the selected physical $C$ trace specified by SC3. These are conditional receiver bounds on those original domains; this consumer does not establish that a new nonlinear solution has such a trace. The normalized outer-height radius remains $2^{-60}$.

The continuous centre and response conventions are inherited through the original successful records. In particular, the candidate identity is `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413` and the continuous-centre definition is `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`. No binary candidate or response was restored for this consumer.

## 3. Complete new envelope and body readout

For each of the six existing weights
$k\in\{1/16,1/8,1/4,3/8,1/2,3/4\}$, read the original complete weighted prior as $X=X_{\rm affine}+X_\gamma\Gamma$, its complete rate upper $a$, and its positive terminal weight. The rate bound covers the full cap; it is not the old local $[0.9,0.95]$ integral.

CEB gives, on the entire physical interval and circle,

$$
|y(r,\theta)|\le m(t):=\min\{\rho,Xe^{at}\},
\qquad t=r-9/10,\qquad 0\le t\le\ell.
\tag{CEBA.2}
$$

The pointwise bound is inherited from the same complete joint Wiener prior, followed by the original cap existence radius. All new integrations use

$$
J_p=\int_0^\ell m(t)^p\,dt,\qquad p=2,4.
\tag{CEBA.3}
$$

All twelve actual rows selected the complete crossing branch. Their crossing balls are strictly ordered against the full interval by directed bounds, without midpoint tests. On that branch,

$$
t_*=\frac{\log(\rho/X)}{a},\qquad
J_p=\frac{\rho^p-X^p}{pa}+\rho^p(\ell-t_*).
\tag{CEBA.4}
$$

The source also retains the zero, zero-rate, initially capped, completely uncapped, and uncertain-order fallback branches; none was silently chosen by a point estimate. The actual calculation contains **12 new crossing logarithms and 0 new exponentials**. Each whole integral is additionally compared with the complete existence-ball bound, with no subtraction of independent upper bounds.

Write $D$ and $Q$ for the **already completed ordinary norms** from SC3. They are not squared Gram traces. The new full body error is

$$
E_{\rm body}=D\sqrt{J_2}+13QY_{\rm quad},
\qquad
Y_{\rm quad}\le\min\{\sqrt{J_4},\,\rho\sqrt{J_2}\}.
\tag{CEBA.5}
$$

Here $\sqrt{J_4}$ bounds the $L^2(dr\,d\theta)$ norm of $|y|^2$. It is **not** the usual $L^4$ norm of $y$. The original pointwise rational remainder bound $13|y|^2$ is used on its unchanged $\rho$ domain. The $Q$ term retains the complete adjoint fields, coefficients, and physical mean.

The endpoint and known terms keep their original order and object:

$$
Y_{L,\delta}=\min\{\rho,X\}+10d,\qquad
Z_R=\min\{\zeta,X/w_R\},
\tag{CEBA.6}
$$

$$
E_{\rm unknown}=E_{\rm body}+E_{L,\delta}Y_{L,\delta}
 +(E_R+L_D Z_B+L_m Z_m)Z_R,
\tag{CEBA.7}
$$

$$
A_{97}=K_{\rm known}+K_{\rm outer}+E_{\rm unknown}.
\tag{CEBA.8}
$$

The known $10d$ change is paid only in the left endpoint. The complete outer omission and complete signed97 known model are each included once. The right nonmean bound and physical $C$-mean feedback are retained; no endpoint is dropped on the strength of a body improvement.

For each domain all six new rows are completed first. The seventh candidate is the entire original SC3 posterior row, read verbatim. The selected answer is a minimum between **complete rows on one domain**. It is not a componentwise mixture of favorable terms from different weights.

## 4. Complete old records retained verbatim

The eleven non-weight records used in the new expressions are:

| Original record | Complete saved directed value |
|---|---|
| `D` | `[0.0015465793004759426780873818467653024195000000821397595656 +/- 4.31e-59]` |
| `Q` | `[886.98934496575707415360313522320860342696568104527728485 +/- 2.04e-54]` |
| `known_uniform` | `[3.8443257050419816041516922171654266930791477245352640214e-13 +/- 6.06e-70]` |
| `known_outer` | `[1.4585218641964752729239441964689769415852303130931203608e-29 +/- 1.72e-85]` |
| `ELdelta` | `[6.2854944232106525775375716449632019773224256011298802831e-9 +/- 9.89e-66]` |
| `ER` | `[1.0705663743994713389061710823943489734980675022153556245e-40 +/- 2.31e-96]` |
| `ZB` | `[3.5661407095496135401752219745818316087507299291606855104e-26 +/- 3.34e-84]` |
| `Zm` | `[7.1147408009358014146416082871548739171623118634231434726e-11 +/- 3.92e-67]` |
| `selected_left_shift` | `[1.0000000000000000000000000000000000000000000000000000000e-9 +/- 3e-69]` |
| `LD` | `0.006` |
| `Lm` | `0.00075` |

Thirty further original records are the five complete quantities for each of the six weights: $X_{\rm affine}$, $X_\gamma$, the whole rate upper, the positive right-end weight, and the original rate lower. The rate lower is retained as provenance and an original domain check; it is not substituted for the rate upper in CEBA.2.

The scientific output retains all **41** original scalar records plus the following **six** complete objects: original RW scope, original RW counts, SC3 body cover, SC3 unknown-operator norms, SC3 error accounting, and both SC3 complete posterior rows. Exact canonical comparisons with the original inputs gave:

| Complete copied object | SHA256 |
|---|---|
| Eleven original source/endpoint/known records | `c5d5e87f52babf88582af59bff34bd01dab6a818a85528b995b9cc609fe0c6b2` |
| Thirty original weight records | `4eb8e6b0f65ccf807b3f6be706ca73212e7bf1a9ff79961f4e4726877755e58c` |
| Six complete original objects | `719c35ee1ceef7781323798d52011028419b2ebc5effecf89a2b7f6fa7aa5111` |
| Original complete signed97 parameter model | `8b62a196845f51fb023f53c859de942d1df324babcc2700f7282bb160cb0da5f` |
| Original SC3 scientific identity | `19b3571f38e1fb89634b07c65ee08ae3b203c95296c69b61c427d524bf19d2ca` |
| Original SC3 numerical-error scope | `ae5f4dedbe937389a905fb7f2c8a9a48769b7b23c11b19a8e5be553900d4a4d7` |

All six hashes were independently reconstructed from the original small input JSON, and every copied scalar string and complete object agrees exactly. The original 7908-body cover, 32 slices, four pilot contributions, the complete signed97 parameter model with its independent mean, and the repaired outer omission remain those of SC3. They were not integrated, enclosed, or regenerated by this run.

## 5. All twelve complete new rows

The following are the original directed records. The third and fourth columns are distinct quantities: the ordinary $L^2$ envelope and the quadratic $L^2$ envelope.

| Physical domain | Original weight | $\sqrt{J_2}$ | $\sqrt{J_4}$ | Complete affine97 posterior |
|---|---|---|---|---|
| full | 1/16 | `[4.00480733442806423906664892531912851592907910395641672863999e-6 +/- 1.07e-66]` | `[1.13285079565023106901530620371124716231666868237089899765445e-11 +/- 4.50e-71]` | `[1.36821602154331278434011678938459908402951469941266883450736e-7 +/- 2.54e-67]` |
| full | 1/8 | `[4.01564241607880890512272015363858751156177729795662862130277e-6 +/- 2.65e-66]` | `[1.15778639466767826533162534774141153840183723493328354539437e-11 +/- 3.06e-71]` | `[1.39713645950809824907409083131671851452783801845112525193145e-7 +/- 3.33e-67]` |
| full | 1/4 | `[4.06923250188726976153851999167429426890369484050953260856854e-6 +/- 2.60e-66]` | `[1.19349790781636252231387245343534397174978065801360216286586e-11 +/- 2.39e-71]` | `[1.43914369727992308677269757093447548646960478643429122272621e-7 +/- 5.28e-68]` |
| full | 3/8 | `[4.11838023801604083031356779801894182581971038595995100021025e-6 +/- 3.97e-67]` | `[1.21674935385909397531419358366411070398940625259287312502560e-11 +/- 1.44e-71]` | `[1.46671471426727490370093081907476104287719598569860841954181e-7 +/- 4.46e-67]` |
| full | 1/2 | `[4.15833744909264149833349190580275279136669692578755485128506e-6 +/- 3.44e-66]` | `[1.23333137606002849465606759082709727999048084718532212502603e-11 +/- 2.96e-71]` | `[1.48645317769034801799305930208287798201763519882000214420781e-7 +/- 3.80e-67]` |
| full | 3/4 | `[4.22047577746331001984473443782754098053231352653924028323324e-6 +/- 2.27e-66]` | `[1.25673284743538730619438014089121179663815879601342697085997e-11 +/- 1.84e-72]` | `[1.51439810226929090855300914716845287467170466803683950719370e-7 +/- 4.88e-67]` |
| tail | 1/16 | `[3.99385503279585708409896956121904676576737942588739494007400e-6 +/- 4.75e-66]` | `[1.12848424043949935670687708606544389510964426036515620048246e-11 +/- 2.78e-71]` | `[1.36301162031690758192224771950192797486765635906506585779848e-7 +/- 2.85e-67]` |
| tail | 1/8 | `[4.00817844617472458435929716656313181615210541921890576193845e-6 +/- 1.33e-66]` | `[1.15517209312346979272943985248972122298410819326425536731907e-11 +/- 2.93e-71]` | `[1.39400650769529371947520590369343718181159581203580424522142e-7 +/- 4.43e-67]` |
| tail | 1/4 | `[4.06394821184040497934143118536531825759121411551751563974360e-6 +/- 3.01e-67]` | `[1.19180572158024287190715862385140625738645341674752334075017e-11 +/- 2.50e-71]` | `[1.43711073448249681836286470855713396021542849746699332799211e-7 +/- 1.87e-67]` |
| tail | 3/8 | `[4.11382734617849172263083761468264328418070708203338183712998e-6 +/- 2.46e-66]` | `[1.21533335091278335769733349388162579046246741536851303679021e-11 +/- 1.72e-71]` | `[1.46501152631187167298026214033804846469459752740921518791278e-7 +/- 3.20e-67]` |
| tail | 1/2 | `[4.15408242213479213429137585486357803191375013237880833398328e-6 +/- 1.48e-66]` | `[1.23202469578734134047915234734671491602765084937051005997745e-11 +/- 1.44e-71]` | `[1.48488065493970495392913366694043116742092174817456319649026e-7 +/- 3.50e-67]` |
| tail | 3/4 | `[4.21634588188775786052686054076058482524211012691962817372270e-6 +/- 1.39e-66]` | `[1.25547750603076360094077183828285538764017602050365785419583e-11 +/- 2.35e-71]` | `[1.51288671290771817552113935200386886814971268451430713921387e-7 +/- 2.61e-67]` |

In every new row the selected quadratic candidate is the complete $\sqrt{J_4}$ bound. Its retained upward-rounded selected record is stored independently from the original candidate record; the saved rounding radii are not normalized or replaced in this note.

## 6. Two selected rows, with every type and endpoint separated

### Full original cap product

Every entry in this table is copied from the completed weight `1/16` row. The integral branch is `crossing`; the selected quadratic candidate is `sqrt_integral_m4`.

| Complete quantity | Original directed record |
|---|---|
| X (complete same-weight prior) | `[1.51404938620684983790597610898160783349982634473254639234794e-6 +/- 1.04e-66]` |
| a (whole-cap rate upper) | `0.702516143661341629922389984130859375000000000000000000000000` |
| t_* (complete crossing ball) | `[0.973393310128724252720708301535110980739276628180368331291126 +/- 1.36e-62]` |
| J_2 | `[1.60384817858888171642577288546102375061608668786565682817961e-11 +/- 2.19e-71]` |
| J_4 | `[1.28335092520536159235817944319822449594709061637576901283384e-22 +/- 3.95e-82]` |
| sqrt(J_2) | `[4.00480733442806423906664892531912851592907910395641672863999e-6 +/- 1.07e-66]` |
| sqrt(J_4), original direct record | `[1.13285079565023106901530620371124716231666868237089899765445e-11 +/- 4.50e-71]` |
| selected quadratic L2 upper | `[1.13285079565023106901530620371124716231666868237089899765445e-11 +/- 4.51e-71]` |
| alternative rho sqrt(J_2) | `[1.20144220032841927171999467759573855477872373118692501859200e-11 +/- 3.32e-71]` |
| formal body error | `[6.19375212582068021918241250138477551686321468068033977128134e-9 +/- 3.60e-69]` |
| nonlinear body error | `[1.30627456073105573297826980243018523592832668695059396473166e-7 +/- 3.53e-68]` |
| complete body error | `[1.36821208198926253517009392744403299109695883375739736244447e-7 +/- 3.09e-67]` |
| left Y including the original 10d shift | `[1.51504938620684983790597610898160783349982634473254639234794e-6 +/- 1.04e-66]` |
| complete left defect error | `[9.52283446789187683885765559552576815405349369524735265387538e-15 +/- 4.25e-75]` |
| right C nonmean bound | `[9.90000000000000000000000000000000000000000000000000000000000e-10 +/- 1e-73]` |
| complete outer feedback error | `[5.28269504469485373324720888851552963086631182984253372347444e-23 +/- 5.28e-85]` |
| complete unknown error | `[1.36821217721760774235836678550596227107552922584529740154918e-7 +/- 2.61e-67]` |
| complete affine97 posterior | `[1.36821602154331278434011678938459908402951469941266883450736e-7 +/- 2.54e-67]` |

### Tail inner-curvature subdomain

Every entry in this table is copied from the completed weight `1/16` row. The integral branch is `crossing`; the selected quadratic candidate is `sqrt_integral_m4`.

| Complete quantity | Original directed record |
|---|---|
| X (complete same-weight prior) | `[1.50026407539263141813895905889631424935764639772420033164675e-6 +/- 1.93e-66]` |
| a (whole-cap rate upper) | `0.702516143661341629922389984130859375000000000000000000000000` |
| t_* (complete crossing ball) | `[0.986413126653039376028157647734490307161098611173992056388450 +/- 6.40e-62]` |
| J_2 | `[1.59508780229887966647964220344895582682096423856416925635293e-11 +/- 1.75e-71]` |
| J_4 | `[1.27347668092031379526085786702971287316440678597108421415210e-22 +/- 4.58e-82]` |
| sqrt(J_2) | `[3.99385503279585708409896956121904676576737942588739494007400e-6 +/- 4.75e-66]` |
| sqrt(J_4), original direct record | `[1.12848424043949935670687708606544389510964426036515620048246e-11 +/- 2.78e-71]` |
| selected quadratic L2 upper | `[1.12848424043949935670687708606544389510964426036515620048246e-11 +/- 2.79e-71]` |
| alternative rho sqrt(J_2) | `[1.19815650983875712522969086836571402973021382776621848202220e-11 +/- 1.43e-71]` |
| formal body error | `[6.17681352282373975222745395110139473656652250867847326753834e-9 +/- 2.67e-69]` |
| nonlinear body error | `[1.30123954640109487767990409609665091689486318602556275936357e-7 +/- 4.06e-67]` |
| complete body error | `[1.36300768162933227520217863560766486426052841111234749203895e-7 +/- 6.29e-68]` |
| left Y including the original 10d shift | `[1.50126407539263141813895905889631424935764639772420033164675e-6 +/- 1.93e-66]` |
| complete left defect error | `[9.43618697364688146105302529729322536228323838461701648695420e-15 +/- 1.21e-75]` |
| right C nonmean bound | `[9.90000000000000000000000000000000000000000000000000000000000e-10 +/- 1e-73]` |
| complete outer feedback error | `[5.28269504469485373324720888851552963086631182984253372347444e-23 +/- 5.28e-85]` |
| complete unknown error | `[1.36300777599120253994049771562329116191367088549769442484030e-7 +/- 2.78e-67]` |
| complete affine97 posterior | `[1.36301162031690758192224771950192797486765635906506585779848e-7 +/- 2.85e-67]` |

The selected body terms show the remaining limitation directly: the nonlinear part is still of order $10^{-7}$, while the complete known signed97 contribution remains of order $10^{-13}$. These are bounds on different objects. A small known model is not an upper bound on the unknown nonlinear body error.

## 7. Whole posterior comparison with the unchanged SC3 result

| Same physical domain | Complete original SC3 posterior | Complete selected new posterior | Selected whole candidate |
|---|---|---|---|
| full_original_cap_product | `[1.6172061997813531673031309748854092189288146750224838248e-7 +/- 1.62e-63]` | `[1.36821602154331278434011678938459908402951469941266883450736e-7 +/- 2.54e-67]` | `new_complete_weight_1/16` |
| tail_inner_curvature_subdomain | `[1.6172061993151374416148417736469107340322840913117758472e-7 +/- 1.28e-63]` | `[1.36301162031690758192224771950192797486765635906506585779848e-7 +/- 2.85e-67]` | `new_complete_weight_1/16` |

Both selected candidate indices are **1** in the stored seven-candidate lists, whose index 0 is the original SC3 row. This identifies the new complete $k=1/16$ row in each domain. The source records `same_complete_object_and_domain=true` and `no_entrywise_mixing=true`.

The two rows must not be minimized across their different physical $\gamma$ hypotheses. Each retains its own true-input condition, full cap interval, physical mean, height, and reflection domain.

## 8. Frozen source and eleven complete text inputs

The final source is [fourfold_codazzi_whole_cap_weight_envelope.py](../scripts/fourfold_codazzi_whole_cap_weight_envelope.py). The worker is [fourfold_codazzi_whole_cap_weight_envelope_public_worker.py](../scripts/fourfold_codazzi_whole_cap_weight_envelope_public_worker.py). The manifest is [2026-11-16-R133-whole-cap-weight-envelope-CI-inputs.json](../notes/2026-11-16-R133-whole-cap-weight-envelope-CI-inputs.json).

| Input role | Bytes | Exact Git blob | SHA256 |
|---|---:|---|---|
| `source` | 42542 | `4633c291d8d829a8adc3397b4331bc55eb243bd2` | `21506f21e886083b835112fec346554f4c9ee01937730b84a5f10649eb72eb70` |
| `worker` | 55439 | `6aeb92e50591714e78d28e8fd41ee6be0615a830` | `a93adea668e8d64a31935f4fd9018e5018e37aa7d53a06fa09177961deb5252c` |
| `rules` | 2461 | `5c5d020913d717bb5bc8ce891297e00eaa8944f7` | `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1` |
| `contract` | 17071 | `4f7476c14e4ce8185c034537d1fc773e6bff9870` | `ff118cc75152796bf68de616b43e6e6fac0f6d1eb859ce0af2ef73f36ea40462` |
| `RW_science` | 57702 | `a4d46696df6125524d7491cd1d4efde156794aee` | `ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9` |
| `RW_process` | 16350 | `df608c6a12fb193106fba64fb23fd7afad37de29` | `daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6` |
| `RW_source` | 31066 | `a44357cfc1e8b5034a1daa587aff9bcaaf7d93ab` | `f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb` |
| `SC_science` | 23672 | `a05d881b0b160299d39cb522ee88304a45b20af0` | `f0838341d4f661714328da407c9a45f7ef137c43e8ab1ca7f4adfc2b12e7893c` |
| `SC_execution` | 43738 | `34050b25b7197fb27d886b40c8f3366726e34f08` | `9ce9955fade952563c6d2dc2ca7650b43a3752d3b10e9051a798ffd73fe2c5e9` |
| `SC_source` | 44167 | `a3e2150166472fd5c08b5508cd30dda12be7836f` | `41b8f50cd7faafc438f37f3f4514caa24142af63d9921044d91ead67d6fcd1dd` |
| `SA_contract` | 23561 | `f7db2f18230e62d216f8a901b990bfd9e6d703c0` | `85e07aba2d895c160be6c307da9ff0740fb817bbad6f3813d0acf3242e0f35d1` |

The manifest itself has Git blob `9d185f67071d8cd07d4f736d88f7ef5172194b86`, **15165** bytes, SHA256 `c76151ac1634f9d6d3fd19f58849ac682ae9c5717b25e3c2445b5808efb03350`. The workflow has Git blob `d62f7cf41f08edc24e78c242d6629b438ba86640`, **4101** bytes, SHA256 `b23dbb9610952422f7f73328c79e6fbdde0f1745d8782d4dfd95fa394c6b4e39`.

All eleven full text inputs total **357769** bytes. The actual complete receipt inventory agrees with all manifest tuples, including role, full path, bytes, and SHA256. Its canonical SHA256 is `0e87e2181368c532322ada00449dda5f85b0d6191ee38f8163eee1de8614a1c1`. All **four** Python text inputs passed the immutable AST closure before the unique child. The complete AST inventory SHA256 is `b97eae14905604990747e7db496f472e05831374c743e57d73aec230eec37a5b`.

The two older producer sources are identity evidence only. The new source does not import or execute either old scientific producer. The original RW success is its 15-gate run 43729429382/1, and SC3 is its 20-gate run 43754452928/1; their source, manifest, runtime, output identity, and same-object domain links were read and checked.

## 9. Lossless plain-JSON publication and preservation before Git

The original scientific publication contains `complete_new_result_field_table` using `lossless_named_column_tables_v1`. It is a plain, named-column JSON representation of exactly two collections: the twelve complete new rows and the two whole-posterior conclusions. Original scalar strings, branch records, complete candidate values, known/left/right terms, and every scope flag are preserved.

Each dictionary row refers to an explicit sorted field-name list. Lists have a distinct null tag. This is not binary data, base64, gzip data embedded in text, or a replacement of numeric balls by hashes. The exact decoder and complete-document functions are in both pinned Python sources. The source verifies an exact JSON round trip before saving. The 41 old scalars and six complete old objects remain ordinary JSON and are not encoded by this table.

The complete published science was independently reconstructed byte for byte from its canonical JSON: **52340 bytes**, SHA256 `96de85be729484f66cb0509138053c19638e39c359c244731587e17eb1cc9694`. Adding its original two science-output markers gives the complete child scientific stdout: **52422 bytes**, SHA256 `307f0f69e4cf004c7a8c9e8c7dc32900c4da4de8cdcd53cc227bf080d708eeec`.

Before any Git publication, the worker preserved the full encoded science and complete report together. That exact payload was independently reconstructed as **61461 bytes**, SHA256 `3c98e979484b0cf949193f672fe730e890d62c43f47aaf6648ed707bd6fe0622`. The original execution also records its separate prepublication process payload as **9856 bytes**, SHA256 `569e052ac96a87a125a2dcbe2da98956a6a24c69bb2ae4cee3cf80d09ee09455`.

The temporary native result was **15080 bytes**, SHA256 `a24278795dab7c2f6e1179de77ad57e3f7f04b7efd5fd68017d5126a8cc2b7dd`. It was a temporary runner output only and was not uploaded or published. The full small scientific JSON is the durable complete conclusion. A formatting or publication failure would not license repeating this completed mathematics.

## 10. Actual publication and capacity accounting

Three real README synchronization checks are recorded at **00:28:32**, **00:28:37**, and **00:28:42 UTC**. All actual README diffs are empty and all use the separately reviewed rules SHA256 `65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1`. The third check records the non-fast-forward recovery from local `15877ff7608318a9015f10c3277125f4da0d899e` to published `a0d71ea94446f0fcf64d1f69e4dbadd5910204ba`; the scientific child was not restarted.

The published capacity base is `a0d71ea94446f0fcf64d1f69e4dbadd5910204ba`, with **199471543** topic bytes. The final actual three-file projection is **199547438** bytes. The worker kept its 120000-byte pre-child reserve rule and final capacity check.

The local owned-head identity `a65dff20f7f63b3f41791b9b31be6b0911c18821` appears in the execution's live-index observation and exact-owned-delta record. It is a **local publication head**, not a claimed public restore commit or immutable scientific input anchor. Its intermediate execution snapshot was 12435 bytes; the final published execution is the separate 14855-byte file listed in Section 1. The three owned paths are exactly the final report, science, and execution for this run. The published-base metadata and the exact local owned delta are kept distinct.

The final process records zero original-input-array recomputations, zero old scientific producer or integral calls, zero old root/flow/mean/Airy recomputations, zero restored binary parts or artifacts, and zero new arrays, artifacts, or Releases retained after the job. There is one new scientific child.

## 11. Complete actual gate list

| Gate | Actual complete check | Result |
|---:|---|---|
| 1 | only the new scalar envelope arithmetic runs in public Actions at the fixed runtime | PASS |
| 2 | eleven current small text inputs and all new mathematical parameters are fixed | PASS |
| 3 | every complete input size and SHA is checked without binary or archive restoration | PASS |
| 4 | the original complete rate and same physical posterior definitions are text evidence only | PASS |
| 5 | RW is the original complete child0 fifteen-gate six-weight success | PASS |
| 6 | the complete RW small science and its process fields are exactly linked | PASS |
| 7 | all six complete whole-cap weighted solution priors keep both means and their original domains | PASS |
| 8 | SC3 is the completed original twenty-gate signed97 success with its exact runtime | PASS |
| 9 | SC3 output SHA size full model identities and direct RW input links match the successful record | PASS |
| 10 | the same complete physical body formal norms mean and continuous97 trial are retained | PASS |
| 11 | selected left changes known outer terms and gamma conditions never recenter the physical body | PASS |
| 12 | both original complete posterior rows have their full domain and exact selected-trace condition | PASS |
| 13 | eleven complete source endpoint and known records plus thirty weight records are finite and typed | PASS |
| 14 | all twelve same-object weight-domain rows and twenty-four closed integrals are complete | PASS |
| 15 | every new integral covers the full physical interval without midpoint branch selection | PASS |
| 16 | two complete domain choices compare seven whole affine97 candidates each | PASS |
| 17 | the unchanged known model outer mean and selected-left terms enter every completed new row once | PASS |
| 18 | all old scalar weight and complete object payloads remain verbatim after new arithmetic | PASS |
| 19 | the complete physical scope retains every independent mean height waist and core input | PASS |
| 20 | all successful old mathematics and original input bytes remain untouched | PASS |
| 21 | all complete retained and new directed ball records are finite | PASS |
| 22 | all complete mathematics is saved before any small-publication formatting guard | PASS |

## 12. Exact scope of the completed result

This execution pays the new complete $p=2$ and $p=4$ scalar envelopes, the associated complete ordinary body and endpoint readouts, and the two whole posterior comparisons on their stated original physical domains.

It retains both complete old posterior rows and every independent original low-trace, waist, core, high, finite, mean, and height input. The actual physical $\gamma$ condition is not inferred from this affine receiver. No moving-coordinate body shift is dropped, and the selected known left change is not applied to the body.

The explicit scientific flags for a new low-trace gate, core selfmap, actual nonlinear background, finite Schur inverse, full physical incoming inverse, and full return $R_0$ are all **false**. This is a completed improvement to one full affine97 receiver, not a proof of those subsequent gates. The successful run and all original completed targets are frozen.
