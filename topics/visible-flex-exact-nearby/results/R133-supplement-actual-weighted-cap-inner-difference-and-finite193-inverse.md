# R133：实际加权帽内端差通过，并闭合两个原域内的 finite193 反馈

2026-11-15。状态：公开 Actions 实际完成；完整内端算子差与 conditional finite193 inverse 已证明。未知 core 的帽准入、affine/nonlinear matching、waist 和无限 high inverse 仍未由本篇支付。

依据 [CP 完整解析合同](R133-supplement-weighted-actual-cap-Poisson-difference-and-complete-inner-receiver.md)、[原 F 实际两 case](R133-supplement-actual-selected-parameter-finite193-feedback-and-cap-difference-threshold.md) 与 [RW 实际值和完整 receiver](R133-supplement-actual-radial-weighted-cap-and-complete-left-receivers.md)。本篇复制实际有向球，不另作本地数学计算。

## CPA1. 实际运行与可复核身份

[公开 run 43741463694/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43741463694)，job 132895348272，push head 1116f90cbe02f1c24325bf54d1a7ff6724b7111c。
GitHub 实际开始 2026-11-15T17:30:20Z、完成状态更新 17:31:14Z；全部 job steps 成功。
scientific child return 0、complete true、failure null，18 个结构门全部通过；5 个 weighted prerequisites 及两个 gamma case 各自的三个 finite strict gates 另行全部通过。

- [完整 execution](../notes/weighted_actual_cap_poisson_difference_ci/run-43741463694-1/execution.json)：blob 9294bddcbe96ce07379a169fe2abbbb44782b135，56480 B，SHA256 6865e7e88c9d1be02b6fe062765750fa2f66a1186ab4ff9d43127f2c9c92f4b8。
- [完整 actual-result](../notes/weighted_actual_cap_poisson_difference_ci/run-43741463694-1/actual-result.md)：blob 1d3b0d93abf6cd431b4fa67e4baf70e3613c7f2e，10555 B，SHA256 d959ef6090fd281b69485ab4d1e2bfd2752da1f3384230d1cb22da8270b34abc。
- execution 内完整 actual_scientific_receipt 按原 sorted compact JSON 加 LF 无损恢复为 43039 B，SHA256 77ed0069075971a5c1a9c229d265adb7750a3e6a87a07e7411eeaa2684bd7246，与实际 child output hash 完全相等。
- scientific source SHA256 c8aaace95295a58d761d1b74422a38d1de721fdf7fd27867b8a7c4e87e88c5b1；worker df8c44b55c231f06865294d5c2580e3daa85a540f3b44ed73f7d8c3d353d17b5。
- [完整 manifest](../notes/2026-11-15-R133-weighted-actual-cap-poisson-difference-CI-inputs.json) SHA256 fc5acb986c2f8c55e9f6bd25a093a8d9e0594890ad8fbf24175e46e74abe001c。21 个小文本输入总 440405 B，全部原字核验；科学 inventory SHA256 2d9284297b52a28c0cdbca5084c44c9d25ea42c568422cdc43851d44fa3e5201，4 个 Python AST 全过。
- math 后首次 Git publication 前，完整科学结论的恢复 payload 已输出到 stdout：54023 B，SHA256 983fac65ac5d16c10e57a23c091c0b9500e4da912f9ec249bae862ddde6880b8。未持久化 native arrays、Release 或 artifact。

两个 real pull 均到 de9a730a8f9cf8ea1f3e31fa6f6dd9cfb64e1d80，README diff 空；publication 预计 topic 为 199406126 B。以上仅身份和完整性核验，没有重算任何原数学。

## CPA2. 先前丢失的新结果保留失败历史

首次 run 43740644806/1 的 worker 完成输入/AST 核验后记录 child return 1；未保存科学 conclusion，990 B child log 当时仅留 hash，故真实异常与数学完成状态均未知。
不能据此把第一次写成数学成功、数学失败或“零新数学”。

本次只重新执行该次未保存的新 CP 标量；相较首版，修复仅涉及重复 metadata、先写完整科学文件再做大小门、完整 serialization status 和缺失 science 时的 child 日志保存。CP 的数学式、参数与 18 个结构门没有改变。旧 RW、F 的所有成功积分、目标、Gram、sweep、cap 解和 accepted case 均未重算。
本次成功现在冻结，不因后续文稿或包装再次运行。

## CPA3. 同一真实帽、两分量 Hilbert 范数与完整 mean

保持实际帽 $[9/10,25/8]$、原 continuous centre、同 fixed intrinsic metric、同 physical $\theta$、Bodd/Ceven 反射族、完整 Cmean，以及原 nonmean normalized height 球 $\|f_B\|_{\dot A^2}<2^{-60}$。
旧 $K_0$ 仍是固定原缓存 reference；新的 $f_B$ 可以在原已证明 product 内与旧值不同。

本篇新量只控制
$$
 (K_*-K_0)_{\rm inner}:
 L^2_{\theta,\mathrm e,\perp}\longrightarrow
 L^2_{\theta,\mathrm o}\oplus_1\mathbb R ,
 \tag{CPA.1}
$$
最后标量是完整 ordinary Cmean。全 physical Fourier modes、原 mean normalization 和 97 行共同单位均保留，不截 unknown high，也不乘 $\sqrt{97}$。

RW 的 joint Wiener pair budget 没有直接作为 Hilbert pair-sum 界。CP.7a--c 从同一 positive algorithm 的
$k_M=D_M+(1+q)c_M$、$b_M=D_M+qc_M$，分别取得 B/C 全模包络，再与独立 Cmean 合并。下面是本次有向结论：

| 完整 Hilbert/weighted 系数 | 实际有向球 |
|---|---|
| B nonmean envelope | `[7.796679632092299807581297167166758170974032781311479560075066377 +/- 2.65e-65]` |
| C nonmean envelope | `[5.026937367189319834493203628734668844614636050069787578300833379 +/- 1.20e-64]` |
| $K_H=B_{\rm env}+\max(C_{\rm env},K_{\rm mean})$ | `[12.82361700241600802275390641765485604317755316606858831817627460 +/- 2.39e-63]` |
| weighted old-reference feedback $\chi_0$ | `[0.6596041009231103704459585021876837927968253836391013121464579896 +/- 2.16e-65]` |
| 严格 gap $1-\chi_0$ | `[0.3403958990768896295540414978123162072031746163608986878535420104 +/- 2.16e-65]` |
| backward divergence rate lower | `[1.520263586777316740155220031738281250000000000000000000000000000 +/- 3e-68]` |
| 原完整 Hessian 的 weighted body source | `[0.001173863321181487433754097858463835569498782301843389971843681343 +/- 4.91e-67]` |
| 原完整 Hessian 的 inner $B+C$mean source | `[0.0001003821996168284175868658955844375098236124368443477903698078393 +/- 4.18e-68]` |

这里使用准确对称差恒等
$$
 D_0(K_*-K_0)=V\,T_QK_*-H_0K_0 ,
 \tag{CPA.2}
$$
旧 Hessian 仍作用在 $K_0$，旧/新 outer 与 Cmean 的独立项全部保留；没有再次外乘旧 Hessian resolvent。
U_w、V_w 只由同一 RW 已成正预算逐项支配回读，不从任意物理 residual norm 反推 moving norm。

## CPA4. 原 F 结果原字保存；本次只替换新的第二列费用

原 F run 43737257903/1 的完整科学 SHA256
1596b511a3867cf677f060f4f7414d37007f4dff690e5c063da292b2da1edc85；
原 RW run 43729429382/1 的完整科学 SHA256
ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9。
本次保存原 F 两个完整 case，并逐 JSON 原字核等：$\kappa=0$ 仍通过，$\kappa=1/5$ 的 cut diagonal 与 determinant 仍失败。旧失败不能改写为奇异性证明，也不因新证明成功而删除。

原三窗的四个 source 类型、全部旧 scalar、coordinate fee 和 sufficient-threshold diagnostic 全部原字复制。新 case 保持原反馈矩阵第一列，只用新的 complete inner $\kappa$ 更新第二列
$\epsilon=\epsilon_{\rm coord}+c_{\rm cap}\kappa$。
三份旧 loads 以准确字段引用同一完整旧 case，新的 high-cut load 单独完整保存；随后给出的四份 transferred columns 均在新科学结论内完整保存。

旧 threshold 的严格比较仅作诊断；实际证明使用每个新 case 自身的两个正 diagonal gaps 和正 determinant，未由 threshold 名称代替实际测试。
### CPA5. 完整物理 gamma 球

物理输入半径为 1/1000000000，非mean normalized height 仍在原 $2^{-60}$ 球。
完整 inner $B$ 的 $L^2$ 与 $C$ mean 的 norm-sum 差界为 `[0.001995250213303986953789151895423820874750174591807147100677283357 +/- 3.55e-67]`。
中间 weighted body 差界 `[0.009305328484469189521770309647126128592010660316505933885934037907 +/- 4.53e-67]` 只用于同权 receiver，不能改称 unweighted whole-cap 算子差。

| 完整新标量 | 有向球 |
|---|---|
| full 97 row $\epsilon$ | `[0.001221753982256937396572381635676706229767641041488826987188298546 +/- 3.68e-67]` |
| body diagonal gap | `[0.7651435538900629840276521792792448860194807868106771571718776832 +/- 2.78e-65]` |
| cut diagonal gap | `[0.4809255510705936016726579286671434859261235499871813251805918751 +/- 3.60e-65]` |
| 完整 $2\times2$ determinant | `[0.2461287684628665107423611655294704451877231178180531911908801983 +/- 4.31e-65]` |

三个 strict gates 分别全通过：body diagonal、cut diagonal、完整 determinant。下表四个独立输入均保留；每个球逐字来自本次完整科学结论。

| 输入 | whole $[0,9/10]$ | 原固定负窗 | 真 cut $r=9/10$ |
|---|---|---|---|
| ordinary 全 core 源 | `[90930.61580565585047449457866013203903824726100970236315247867274 +/- 2.84e-60]` | `[43119.50272202381192986739476701689548159430246715228177243474815 +/- 4.61e-60]` | `[25837.87897467519521388760392531293738034723844192574898276092089 +/- 2.64e-60]` |
| 独立原 97 右端行 | `[6073.436897284254207052391042224515987121569936607164425031035403 +/- 6.65e-62]` | `[2896.393647026294601048470807854696989913181939839329652327413863 +/- 4.24e-61]` | `[1725.971372367795404164542797572554759453905924652309800226100764 +/- 2.53e-61]` |
| 独立 high body | `[356.0492388728231070337616143609554398816888598902448872677287821 +/- 2.32e-62]` | `[170.9037308348454370769404795073589276167856463958754838746782104 +/- 4.90e-62]` | `[100.1944047903402182774475260848052418833807911334071891828975120 +/- 3.39e-62]` |
| 独立 high cut | `[7.837542172311805264622274766437793859800656404636571922660903941 +/- 2.43e-64]` | `[3.736785745747934331006245594490023998638014751772518664896962047 +/- 4.34e-64]` | `[2.238355133979597446240575225419477819490598826732890255838396063 +/- 4.46e-64]` |

额外参数列仅消费原已经明确的 volume 源 $\Delta F_\nu+\Delta A Z$：
whole `[0.3932194716319963194039248300053604382193602721454872655711921562 +/- 3.19e-66]`，
负窗 `[0.1864655586807761294493614204112869315110913108404173933588009860 +/- 2.64e-65]`，
cut `[0.1117330728324540997887888613745607068733821229181202140122425998 +/- 2.67e-65]`。
它不包含旧 exact-response residual、实际边界 affine、waist 或 particular traces。

### CPA6. tail 物理 gamma 子球

物理输入半径为 1/128000000000，非mean normalized height 仍在原 $2^{-60}$ 球。
完整 inner $B$ 的 $L^2$ 与 $C$ mean 的 norm-sum 差界为 `[0.001965078425369347160008235817147715634525227743105540668501925603 +/- 4.32e-67]`。
中间 weighted body 差界 `[0.009175853205132489927244909034261257655504170901016061155115812482 +/- 3.06e-67]` 只用于同权 receiver，不能改称 unweighted whole-cap 算子差。

| 完整新标量 | 有向球 |
|---|---|
| full 97 row $\epsilon$ | `[0.001203280096128216741137543807526719435145050605521924127590565098 +/- 2.08e-67]` |
| body diagonal gap | `[0.7651435538900629840276521792792448860194807868106771571718776832 +/- 2.78e-65]` |
| cut diagonal gap | `[0.4887743671179421789041901932190964695011281907172770073532592544 +/- 3.90e-65]` |
| 完整 $2\times2$ determinant | `[0.2539766823508917922058772021020635256466868341555860404380083624 +/- 1.09e-65]` |

三个 strict gates 分别全通过：body diagonal、cut diagonal、完整 determinant。下表四个独立输入均保留；每个球逐字来自本次完整科学结论。

| 输入 | whole $[0,9/10]$ | 原固定负窗 | 真 cut $r=9/10$ |
|---|---|---|---|
| ordinary 全 core 源 | `[88121.18604650594053041083678697408999832095865033988497081329671 +/- 2.32e-61]` | `[41779.69881135718774033733440637048949433262899761341414267342834 +/- 3.32e-60]` | `[25039.48501438903005880596836824618317556299439798538066016797881 +/- 9.31e-61]` |
| 独立原 97 右端行 | `[5885.766874457550758758643068168106303943103275279009446260388863 +/- 4.53e-61]` | `[2806.894690991104711894314920164042091087114820858330820121070229 +/- 4.49e-61]` | `[1672.638623163578096817282680470693216733975601493937310008466827 +/- 2.20e-61]` |
| 独立 high body | `[345.1548019573861398306526372039902874459098789102184305184887748 +/- 3.76e-62]` | `[165.7082248300147873202558871610604198996070251148297618420449086 +/- 7.37e-63]` | `[97.09838411010245714605884687282707065240821122812142341909603369 +/- 3.87e-63]` |
| 独立 high cut | `[7.485426145566132973148097002159864670365842587920245212440376348 +/- 2.98e-64]` | `[3.568863259661293528770053920419063071199723311536448078746678058 +/- 1.74e-64]` | `[2.138289521675849609166572252714676731387490504614816152430442124 +/- 2.48e-65]` |

额外参数列仅消费原已经明确的 volume 源 $\Delta F_\nu+\Delta A Z$：
whole `[0.3810704008741205002267908015286792623484849578664910016123773416 +/- 3.81e-65]`，
负窗 `[0.1806717236651988644716276010199486728124747703682721124359738181 +/- 1.78e-65]`，
cut `[0.1082805057467006157345784839996646289307073717856461980383059945 +/- 2.44e-65]`。
它不包含旧 exact-response residual、实际边界 affine、waist 或 particular traces。

## CPA7. 实际有限逆的准确用途

令 $B,N,C$ 分别表示 whole core $[0,9/10]$、原固定负窗和真 cut $r=9/10$。
每个表中四列分别乘同原合同定义的 ordinary volume source、独立原97右端源、独立 high whole-body 状态和独立 high actual-cut 状态。
ordinary body source 与 raw 状态输出使用原 moving $\phi$ 的完整 orthonormal Euclidean pair，未乘 $\alpha$；whole body 使用真实 $dr$，even mean 权为 1，输出已经撤去原 weighted-state 变换。独立右端输入保持原 F 的 Euclidean 97 行规范，不能改称 physical 裸迹或另乘角变换。两份 high 输入保持各自原 body/cut 类型。表中的 cut 不能当成任意 collar 点，也不能向右帽区间免费延拓。

在同一真实帽域已成立的前提下，CP 的 full 97 比较与 F 的正 $2\times2$ 消元给本篇 conditional finite193 inverse。所有四个独立列与完整 even mean 均保留。它不提供 high 块的右逆，不把 high-body/high-cut 两列当成已知零，也不授无限 Schur、参数 Schur 或 core 非线性存在性。

实际应用仍须给定同一个选定背景和同一未知态的真实 source，包括非零 cap affine、边界非线性 chart、独立 normalized height、原96 waist 行、旧 exact-response residual 及实际参数边界列。当前 $\gamma$ 必须由真实 physical chart 进入对应 A0 球；本次没有把 whole $C^0$ 或小角位移升级为该准入。

因此新的实质结论是：原 $\kappa=1/5$ 粗界未通过的 actual-cap finite 门，已由同一原帽域内的两个完整新内端差界分别严格通过。实际 low/shell/cut 数据、unknown high 与真正全域 matching 继续独立保留。
