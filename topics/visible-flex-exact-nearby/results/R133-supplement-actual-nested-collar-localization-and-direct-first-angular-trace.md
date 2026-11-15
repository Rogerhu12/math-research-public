# R133 supplement: actual nested-collar localization and complete direct first-angular trace rows

2026-11-15, tail_connector. Actual public scalar run completed; the conditional inequalities below are the already proved NC/BD theorems instantiated with that run. No core solution, unknown body norm, cut match or low-curvature self-map is asserted.

The first and only public run is [43733916510/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43733916510), at deployment commit `b17528a1f443e1250c2102f2296e904a3ec71445`. Job `132872203592` ran from 16:09:58 to 16:10:37 UTC and concluded `success`. The actual scientific child returned zero; its internal scalar duration was `0.07085503000000415` seconds.

All 16 structural gates and all 12 independent first-angular absorption gates passed. All 768 parameter triples were examined, and all 1536 complete NC/BD formula rows were evaluated. The successful science is frozen: no repeated scalar run is authorized by this note.

## 1. Exact small inputs and public output identity

The consumer reads only the completed LC compact science, its original final process and lossless recovery record, the completed WC source, and the final NC/BD proofs. It does not read or reconstruct the old native, original target grid, Fourier product, source integral, mean flow or Green propagation.

| Item | Bytes | SHA256 |
|---|---:|---|
| Scientific source | 25200 | `57ca8b5b9357a875180c7aec2caef7ab975a2e1b5d64b0ae6b88f510dd606204` |
| Worker | 35594 | `954f9ae55a43e9f554ac389a03f11f719e170094284eab17a3305bea2222dbb1` |
| Complete input manifest | 14492 | `191aec33eee20cae472857dc10d5d7cc81f2023738310e56fe02feabb30f0e1d` |
| Complete actual science | 35707 | `83e06a289105254022cba13ae23ff102ce384c1ae9e2ade468e5cdc979654df6` |
| Actual process | 15995 | `3157ed355d059c032662f130b40f5952f564c7337a7ef986e8429ae019bc4057` |
| Complete selected-row report | 9765 | `b88b9e5400de720791b37461c7a6bd8fa5402ead4b463c51f3b2294a68a4fa33` |

The three actual files are respectively
[science](../notes/nested_collar_direct_trace_ci/run-43733916510-1-nested-collar-direct-trace/actual-nested-collar-direct-trace.json),
[process](../notes/nested_collar_direct_trace_ci/run-43733916510-1-nested-collar-direct-trace/process.json), and
[report](../notes/nested_collar_direct_trace_ci/run-43733916510-1-nested-collar-direct-trace/actual-result.md).
All nine frozen input receipts in the process agree with the complete manifest.

The LC input is the complete 55770-byte compact object with SHA256 `44b4da07b50dcca9be7671b8cb59b227999e76871237c25a1bc0aec4bc02492c`. Reformatting that object exactly reproduces the original 74725-byte science with SHA256 `903a537a0454464e8c30ff57034b2811d1c43ad47a18979f5a7d8403c888b981`. The earlier LC publication-format failure is retained in this new conclusion; it is not confused with a failed mathematical child.

The complete new science and report were printed before terminal publication as one 46305-byte payload with SHA256 `be17391bd7da8067d56c50c81504af46ae6a06079bd6056ac3af323ff870057e`. It is independently reproduced from the published science and report by the worker's exact sorted JSON formatting. The 1261253-byte full temporary audit has SHA256 `323d80d17896e972a3e6ff4ef52981f0b0f7acb48299437474ad6a21e38dd475`; it was not persisted or uploaded.

## 2. The actual conditional mathematical statement

Use the same real, continuous, two-sided $H^1$ solution $Q$ as in
[LC](R133-supplement-saved-positive-collar-component-bounds-and-high-frequency-coercivity.md),
[NC](R133-supplement-nested-collar-localization-and-direct-projected-first-angular-trace.md), and
[BD](R133-supplement-complete-degree32-splitting-of-the-differentiated-collar-equation.md).
The exact interval, cut and selected-family domain are
$$
 I=[17/20,19/20],\qquad c=9/10,\qquad
 Q_\delta=Q_0+\delta Z_{\rm can},\qquad |\delta|\le10^{-10}.
 \tag{NCA.1}
$$
Here $Q_0$ and $Z_{\rm can}$ are the same continuously repaired centre and canonical direction fixed by LC. The selected-reference difference is $h=Q-Q_\delta$. For the row with radius $\rho$, retain the original LC hypothesis
$\|h\|_{C^0(I\times\mathbb T)}\le\rho$. This hypothesis must hold on the full collar for this one state. The separately proved right-cap bound does not by itself supply the left half or a smaller radius.

Let $P(r)=\operatorname{diag}(K(r)^{-1/4},K(r)^{1/4})$, $z=P h$, and use the original normalized moving angle $\phi$, with physical frequencies $4j$. For $J=96$ or $288$, put
$$
 \begin{split}
 H_J&=1-\Pi_{\le J},&
 Z_L&=\|\Pi_{\le J}z\|_{L^2(I\times\mathbb T)},\\
 Z_S&=\|(\Pi_{\le J}-\Pi_{\le J-64})z\|_{L^2(I\times\mathbb T)},&
 B_0&=\|H_Jz\|_{L^2(I\times\mathbb T)} .
 \end{split}
 \tag{NCA.2}
$$
Thus the two shells are precisely $33\le |j|\le96$ and $225\le |j|\le288$. The low projection includes both independent means, and hence the full even mean in the reflection class. All radial norms use the true measure $dr$.

Write $F_0,F_1$ for the complete ordinary high source and its angular derivative in the NC equation. For each complete row $(a_1,a_0,a_S,a_L,a_H)$ displayed below, the independently proved NC or BD estimate gives
$$
 \boxed{\ \|H_Jh(c)\|_{H^1_\phi}
 \le a_1F_1+a_0F_0+a_SZ_S+a_LZ_L+a_HB_0.\ }
 \tag{NCA.3}
$$
The global LC $P$-norm upper bound is used as an upper bound for the same-cut inverse multiplier, and is paid exactly once in these coefficients. No additional physical, pair-sum, moving-angle or density conversion is silently included.

For the same true residual-zero solution, the complete known source is the high part of the canonical selected-reference residual. Its already certified WC values are copied without reintegration:
$$
 \begin{split}
 F_{0,96}
 &\le [3.99102136293534761091854531800642551370305234335{\rm e}{-16}
          \ \pm 3.59{\rm e}{-64}],\\
 F_{1,96}
 &\le [3.25933891844640712031103436048467012281784016050{\rm e}{-13}
          \ \pm 4.38{\rm e}{-61}],\\
 F_{0,288}&=F_{1,288}=0 .
 \end{split}
 \tag{NCA.4}
$$
A bound represented by an interval means its upper endpoint. The additional complete bound $F_{1,96}\le1152F_{0,96}$ was checked; the smaller original WC angular bound was used. The high-$288$ zero follows from the complete selected residual's degree-$288$ support, including all four source species and its raw mean. It is not inferred from the degree of the reference alone.

The full low mean, primitive and rank contributions are retained in LC/NC/BD. Only an exact high output projection removes the corresponding finite-output rank term. For a nonzero-residual iterate, its ordinary source, angular source and residual contribution to the mean/log-speed must be supplied on their declared domains; this actual table does not pay those missing inputs.

## 3. All twelve new first-angular gates

The two completed LC zero-order energy tests are preserved as inputs. The new, separate test is $t_1=c_p^\sharp A_1/[4(J+1)]<1$, using the full actual $A_1$. The smaller base mixing coefficient in BD is used only for its shell column, never as a replacement in this gate.

Every one of these twelve new gates passed. The number in the last column counts the finite choices with $r_N<1$; rows with $r_N\ge1$ were also evaluated as finite positive-polynomial bounds.

| Wide rho | J | t1 ball | Passed | Selected N | N with r<1 |
|---|---|---|---|---|---|
| 1/10000 | 96 | [0.0163545234235794766015984 +/- 4.73e-26] | True | 13 | 34 |
| 1/10000 | 288 | [0.00547705952321710898424046 +/- 8.12e-28] | True | 39 | 64 |
| 1/1048576 | 96 | [0.0163486575505496687992741 +/- 1.90e-26] | True | 13 | 34 |
| 1/1048576 | 288 | [0.00547509759634183221425400 +/- 3.62e-27] | True | 39 | 64 |
| 1/16777216 | 96 | [0.0163486046036030607132163 +/- 4.36e-26] | True | 13 | 34 |
| 1/16777216 | 288 | [0.00547507988745443996654287 +/- 4.00e-27] | True | 39 | 64 |
| 1/268435456 | 96 | [0.0163486012944206889594846 +/- 4.95e-26] | True | 13 | 34 |
| 1/268435456 | 288 | [0.00547507878064957225854081 +/- 2.10e-27] | True | 39 | 64 |
| 1/4294967296 | 96 | [0.0163486010875967977219507 +/- 3.31e-27] | True | 13 | 34 |
| 1/4294967296 | 288 | [0.00547507871147427034830351 +/- 3.99e-27] | True | 39 | 64 |
| 1/68719476736 | 96 | [0.0163486010746703045469372 +/- 4.10e-26] | True | 13 | 34 |
| 1/68719476736 | 288 | [0.00547507870715081398798208 +/- 3.66e-27] | True | 39 | 64 |



## 4. Complete selected five-column rows

For each fixed $\rho,J$, all $N=1,\ldots,64$ use the finite positive sum
$\sigma_N=k_J\sum_{i=0}^{N-1}(40Nk_J)^i$ and $\eta_N=(40Nk_J)^N$. No denominator $1-r_N$ is used. The announced rule selects the smallest certified $\eta_N$ upper endpoint, breaking a tie by the smallest $N$. It selects $N=13$ for every $J=96$ case and $N=39$ for every $J=288$ case.

The same $N$ is retained for both formulas. Each row below is one complete operator bound in (NCA.3). Taking a columnwise minimum between NC and BD, or between different $N$, is not justified. Once the actual nonnegative inputs are available, one may compare the two complete right sides.

All displayed numeric strings are complete outward Arb balls from the successful run. Internal arithmetic used 320 bits. The printed ball format may widen from 24 to at least 16 significant digits to respect the fixed complete-output size limit; no directional endpoint is dropped.

| rho / J / N | Formula | F1 | F0 | Zshell | Zlow | Bhigh |
|---|---|---|---|---|---|---|
| 1/10000 / 96 / 13 | NC | [0.0465706566667857696796929 +/- 2.23e-26] | [1.13103335075625865288328 +/- 4.99e-24] | [21.7126005018114006721710 +/- 1.17e-23] | [745.269087345134791831134 +/- 3.87e-22] | [0.000222301562673658758130855 +/- 3.29e-28] |
| 1/10000 / 96 / 13 | BD | [0.0465706566667857696796929 +/- 2.23e-26] | [1.13103326012228075357995 +/- 2.18e-24] | [365.767919235888076420791 +/- 3.19e-22] | [6.93529719257276066133565 +/- 1.07e-24] | [0.000222301353981594426163903 +/- 3.87e-28] |
| 1/10000 / 288 / 39 | NC | [0.0266552925943882915250596 +/- 4.62e-26] | [0.602739402969943887897691 +/- 4.95e-25] | [33.3694987552408105875055 +/- 1.90e-23] | [2403.27875779581575140113 +/- 2.37e-21] | [6.93914712056843007448657e-16 +/- 4.30e-40] |
| 1/10000 / 288 / 39 | BD | [0.0266552925943882915250596 +/- 4.62e-26] | [0.602739385833284115107962 +/- 2.23e-25] | [1732.45908462090796732852 +/- 9.54e-22] | [33.8158847095088766533532 +/- 4.46e-23] | [6.93914052577345309175541e-16 +/- 6.63e-41] |
| 1/1048576 / 96 / 13 | NC | [0.0465655130591713885477800 +/- 3.43e-26] | [1.13086171714460393865582 +/- 2.99e-24] | [21.7093056281102405123441 +/- 3.70e-24] | [740.232385242740650299454 +/- 3.46e-22] | [0.000222163890444382528543725 +/- 2.79e-28] |
| 1/1048576 / 96 / 13 | BD | [0.0465655130591713885477800 +/- 3.43e-26] | [1.13086171628252897719599 +/- 2.00e-25] | [365.726626072391361675422 +/- 3.56e-22] | [0.0662153678743499913672127 +/- 4.28e-26] | [0.000222163888460206702053990 +/- 4.50e-28] |
| 1/1048576 / 288 / 39 | NC | [0.0266524662604480114411850 +/- 1.37e-26] | [0.602653451684587785661887 +/- 3.77e-25] | [33.3647402289265041971713 +/- 3.52e-23] | [2379.39403405404916698397 +/- 2.94e-21] | [6.92872900308966669708481e-16 +/- 1.70e-40] |
| 1/1048576 / 288 / 39 | BD | [0.0266524662604480114411850 +/- 1.37e-26] | [0.602653451521589464240005 +/- 1.57e-25] | [1732.27416789518777806736 +/- 3.43e-21] | [0.322859979921265221052651 +/- 6.64e-26] | [6.92872894044393991150788e-16 +/- 5.11e-41] |
| 1/16777216 / 96 / 13 | NC | [0.0465654666304946004091757 +/- 4.35e-27] | [1.13086016794868169044186 +/- 4.70e-24] | [21.7092758879861881848686 +/- 4.92e-23] | [740.186925933662664930479 +/- 1.11e-22] | [0.000222162648109873142424879 +/- 2.84e-28] |
| 1/16777216 / 96 / 13 | BD | [0.0465654666304946004091757 +/- 4.35e-27] | [1.13086016789682064397243 +/- 2.50e-24] | [365.726253341421468946615 +/- 1.42e-22] | [0.00421760749520573408444711 +/- 1.92e-27] | [0.000222162647990508754343326 +/- 2.68e-28] |
| 1/16777216 / 288 / 39 | NC | [0.0266524407484522168512882 +/- 3.91e-26] | [0.602652675865837191918742 +/- 3.46e-25] | [33.3646972772251475806139 +/- 3.82e-23] | [2379.17845850220822774399 +/- 4.64e-21] | [6.92863503365959301581299e-16 +/- 5.00e-40] |
| 1/16777216 / 288 / 39 | BD | [0.0266524407484522168512882 +/- 3.91e-26] | [0.602652675856031473830417 +/- 9.71e-26] | [1732.27249873960324250779 +/- 1.40e-21] | [0.0205625724181638664186560 +/- 2.08e-26] | [6.92863502989097077350709e-16 +/- 3.51e-40] |
| 1/268435456 / 96 / 13 | NC | [0.0465654637287032231431928 +/- 2.13e-26] | [1.13086007112399798221751 +/- 1.66e-24] | [21.7092740292296142383785 +/- 1.40e-24] | [740.184084730354285955671 +/- 2.34e-23] | [0.000222162570464205547221031 +/- 3.43e-28] |
| 1/268435456 / 96 / 13 | BD | [0.0465654637287032231431928 +/- 2.13e-26] | [1.13086007112277522372297 +/- 3.25e-24] | [365.726230045743839916262 +/- 3.37e-22] | [0.000342752193853945252954923 +/- 4.79e-29] | [0.000222162570461391223266458 +/- 7.96e-29] |
| 1/268435456 / 288 / 39 | NC | [0.0266524391539528995993696 +/- 2.13e-26] | [0.602652627377191913976682 +/- 1.69e-25] | [33.3646945927452873411037 +/- 3.46e-23] | [2379.16498504605683358939 +/- 1.13e-21] | [6.92862916061335236582574e-16 +/- 4.85e-40] |
| 1/268435456 / 288 / 39 | BD | [0.0266524391539528995993696 +/- 2.13e-26] | [0.602652627376960718774309 +/- 3.39e-25] | [1732.27239441740744910370 +/- 4.76e-21] | [0.00166900634168307940094492 +/- 2.32e-27] | [6.92862916052449740052859e-16 +/- 1.20e-40] |
| 1/4294967296 / 96 / 13 | NC | [0.0465654635473412656656006 +/- 1.70e-26] | [1.13086006507245549042321 +/- 1.55e-24] | [21.7092739130573329734542 +/- 2.38e-24] | [740.183907155161219275762 +/- 2.43e-23] | [0.000222162565611352257055606 +/- 3.31e-28] |
| 1/4294967296 / 96 / 13 | BD | [0.0465654635473412656656006 +/- 1.70e-26] | [1.13086006507439762460791 +/- 2.72e-24] | [365.726228589764019309913 +/- 1.70e-22] | [0.000100573755966109668292353 +/- 2.77e-28] | [0.000222162565615822309566893 +/- 1.51e-28] |
| 1/4294967296 / 288 / 39 | NC | [0.0266524390542966939113970 +/- 2.14e-26] | [0.602652624346651688144958 +/- 1.98e-25] | [33.3646944249653018360881 +/- 5.48e-24] | [2379.16414295510924121484 +/- 8.75e-22] | [6.92862879354813083590027e-16 +/- 4.94e-42] |
| 1/4294967296 / 288 / 39 | BD | [0.0266524390542966939113970 +/- 2.14e-26] | [0.602652624347018900565057 +/- 2.56e-25] | [1732.27238789727032232864 +/- 8.11e-22] | [0.000488158547420433231803035 +/- 1.01e-28] | [6.92862879368926112324205e-16 +/- 1.28e-40] |
| 1/68719476736 / 96 / 13 | NC | [0.0465654635360061433373196 +/- 4.93e-26] | [1.13086006469423408562345 +/- 3.01e-25] | [21.7092739057965654123915 +/- 2.77e-23] | [740.183896056711706151258 +/- 4.67e-22] | [0.000222162565308048930070793 +/- 4.45e-28] |
| 1/68719476736 / 96 / 13 | BD | [0.0465654635360061433373196 +/- 4.93e-26] | [1.13086006469637402559936 +/- 3.30e-24] | [365.726228498765280643923 +/- 2.22e-22] | [8.54376036701771736463005e-5 +/- 4.20e-29] | [0.000222162565312974256101267 +/- 5.00e-28] |
| 1/68719476736 / 288 / 39 | NC | [0.0266524390480681810623060 +/- 1.83e-27] | [0.602652624157242924436880 +/- 3.36e-25] | [33.3646944144790527645245 +/- 4.82e-23] | [2379.16409032442525837018 +/- 3.62e-21] | [6.92862877060655514852464e-16 +/- 1.53e-40] |
| 1/68719476736 / 288 / 39 | BD | [0.0266524390480681810623060 +/- 1.83e-27] | [0.602652624157647537333157 +/- 2.16e-25] | [1732.27238748976175233611 +/- 1.12e-21] | [0.000414355560613070194266592 +/- 3.96e-28] | [6.92862877076205951336661e-16 +/- 1.76e-40] |



## 5. What is and is not paid by these actual rows

The selected high-body coefficients are now direct $H^1$ trace coefficients. Their derivation uses the finite nested ordinary-energy argument and the independently paid first-angular absorption gate. It does not invoke the narrow MA $H^{8193}$ bound or its interpolation factor, and does not enlarge that narrow domain.

The JSON also preserves, for each complete row, the known-source contribution, the separate conditional contribution obtained from $B_0\le\|P\|_\infty\rho\sqrt{|I|}$, and their sum. These readouts explicitly omit the still unknown shell and low terms; they are not estimates of the whole trace. In particular the tiny high-$288$ conditional term cannot remove the $225\ldots288$ shell or its low leg.

For the widest $\rho=1/10000$, the conditional high-body term in the selected high-$288$ BD row is the exact saved ball
$[3.76238172104828614243706{\rm e}{-20}\pm4.56{\rm e}{-44}]$.
For $\rho=1/16777216$, the selected high-$96$ BD sum of known source and conditional high body is
$[7.19536203059695907373917{\rm e}{-12}\pm3.99{\rm e}{-36}]$.
The latter depends on that smaller whole-collar $C^0$ hypothesis. Neither number includes $Z_S$ or $Z_L$.

The remaining actual task is to bound the finite low/shell terms for the same matched two-sided state, and to supply whichever complete collar domain is used. The current original Green output is only on the inner body and its true cut; an independent right-cap estimate must refer to that same solution. An input-side Gram cannot be truncated to fabricate an output-band receiver.

No actual unknown low, shell or cut norm, no physical inner-curvature entry, no core existence and no full matching has been proved by this scalar run. All means, same-state requirements, ordinary sources, parameter units and independent geometry remain in their original contracts.
