# Actual78：原三模共振搜索八次极小步接受，尚无共振候选

作者：ChatGPT / geometry  
日期：2026-11-15 UTC  
分类：公开 Actions 原件读回、来源与字节核对；本地未运行科学计算。

## 1. 实际结论

第 78 次请求使用未修改的 R259 诊断源，从真实 actual77 的 `final.parameters` 继续八步 Newton 候选搜索，并将该源已有的回溯预算设为 20。程序正常完成，八个方向都由原 Armijo 规则接受；但每次都要缩到第 18 次试探，即 $\alpha=2^{-17}=0.00000762939453125$。最终三个单位方程仍为

$$
(207.5687844070032,\;-173656.79940813163,\;316223.4753016916).
$$

完整 112 项一阶右残差前三项仍为

$$
(95.8775470268212,\;10366.357976313051,\;4974.213172451416).
$$

原 `low_mode_candidate_has_small_full_recorded_right_residual` 明确为 false，`success=false`；没有非零 $\lambda$ 解、native solve 或 fullDN 接受。本次扩展回溯找到了真实下降步，但没有得到可视作共振根的候选。来源为[完整原 status](public-actions-43662193286-1-smallcoreresonance/resonance/resonance-status.json)，其中保留全部 144 次实际试探。

最终完整标量实表达的 Arb 域检查和零核圆参考检查完成了各自的有限范围。它们不将上述大的一阶共振残差核销，也不能把零核圆场变成原非零核目标的父解。

## 2. 运行、父输入与唯一原件身份

| 项目 | 实际值 |
|---|---|
| Run | [43662193286](https://github.com/Rogerhu12/math-research-public/actions/runs/43662193286) |
| Source commit | `11b5d25c436d84d734a73d4609092bde749daea5` |
| Job | `132653733174` |
| Job 时间 | 2026-11-15 01:15:10–01:15:50 UTC |
| 原科学 step | 01:15:37–01:15:42 UTC，exit success |
| 诊断源内部 seconds | `3.297941905000002` |
| Artifact | `14140956036`；`248708` B |
| ZIP SHA256 | `7e1f38cff494224463fb784ce3af3ac10912aae4e23f3f2f5e4d86e59502f014` |
| 科学源 | `geometry_20261114_small_core_resonance.py`，25799 B |
| 科学源 SHA256 | `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |
| 实际网格 | 699 站点；field/tail $M=T=112$；物理角 2048；材料/边界角 4096 |
| 原运行预算 | `newton_steps=8`，`backtracks=20`，candidate tolerance $10^{-8}$，Arb 160 bit / depth 14 |

根代理唯一下载了该原包并核 ZIP/CRC；本次读回使用已完成标记的原目录，没有再次下载。完整命令见[exact-diagnostic-command.json](public-actions-43662193286-1-smallcoreresonance/exact-diagnostic-command.json)，原来源清单见[request78-input-and-source-identity.json](public-actions-43662193286-1-smallcoreresonance/request78-input-and-source-identity.json)。

| 四个既有数学输入 | 原 SHA256 |
|---|---|
| accepted96 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112 / 699 站点 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 真实 T112 零尾完整响应/J | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原 tail config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

父 actual77 为 run `43661078498`、job `132650310904`、source `1200c13713b0a4ce4d125a0534610583223ed4ef`。其完整 status 为 23659 B，SHA `e003cc07e52789fa075289794f4bee76993b88cbdf1dc7b639a46872019fcc14`，已作为本包 `prior-candidate/actual77-resonance-status.json` 保存并重新核字节。

实际命令的初始参数与父 `final.parameters`、本轮 `initial.parameters` 完全一致：

$$
p_0=(0.09307073916632971,\;-0.1321108634591744,\;-0.1241786723386648).
$$

这并不表示整份 initial 诊断是旧报告的字节复用。新一次计算的若干末位与 actual77 final 不同，例如第二单位缺陷分别为 `-173667.38459813764` 和 `-173667.38459813932`。完整差异字段和原值保存在 companion readout；本记录没有将两个报告冒成同一字节对象，也没有由这点差异推定数值原因。

## 3. 八个方向与全部 144 次原试探

原搜索用单位三方程 $r(p)$ 的未加权 merit $\frac12\|r\|_2^2$，方向由原 $3\times3$ 参数 Jacobian 解出，并检查真实记录的方向斜率；每次试探再实际调用原 `model.evaluate(p+\alpha d)`。接受规则仍为原 `.2` Armijo，不因本次读回增设或放宽阈值。[原科学源](../computations/geometry_20261114_small_core_resonance.py) 中的这一搜索与 fullBVP/native 验收是不同层次。

每一轮实际试探结构完全一致：

- $\alpha=1,1/2,1/4,1/8$：四次均记录原异常 `Original node/mid scalar domain failed; no interval claim is made by this test`。这些试探没有实际 merit 字段，不能填作下降或有限失败。
- $\alpha=2^{-4},\ldots,2^{-16}$：十三次均实际有限，原记录的 merit 大于该轮 `merit_before`，故原 Armijo 拒绝。
- $\alpha=2^{-17}$：第十八次试探实际接受；本轮随即结束，没有执行本预算还允许的 $2^{-18},2^{-19}$。

因此全部记录计数为：144 次试探，32 次标量 node/mid 域拒，104 次有限 merit 拒，8 次真实接受。不是 160 次，也不是二十次全拒。完整每个 alpha/merit/异常/接受旗和每轮参数、残差、Jacobian 已保存在原 status 与[完整原读数 companion](2026-11-15-actual78-complete-original-readout.json)，本地没有重算它们。

| 原迭代 | 原 `merit_before` | 最近拒绝 $2^{-16}$ 的原 merit | 接受 $2^{-17}$ 的原 merit |
|---|---:|---:|---:|
| 0 | 65080884368.110664 | 65080932356.225334 | 65080399929.64479 |
| 1 | 65080399929.64479 | 65080447578.24023 | 65079915410.014175 |
| 2 | 65079915410.014175 | 65079962727.090225 | 65079430811.326546 |
| 3 | 65079430811.326546 | 65079477804.49445 | 65078946135.3012 |
| 4 | 65078946135.3012 | 65078992812.737946 | 65078461384.0295 |
| 5 | 65078461384.0295 | 65078507753.78834 | 65077976559.747856 |
| 6 | 65077976559.747856 | 65078022629.39597 | 65077491663.69031 |
| 7 | 65077491663.69031 | 65077537441.54965 | 65077006698.67795 |

原八个斜率都有限且为负，首个为 `-130161768736.21344`，最后为 `-130154983327.37125`。这解释了为何原程序有严格下降方向可试，不能据此保证能接受大步；本次实际回溯记录恰好显示大步在域或原 merit 上失败。

最终参数为

$$
p_8=(0.09365081258727412,\;-0.13201200770909496,\;-0.12389206129693811).
$$

| 项目 | 实际 initial | 实际 final |
|---|---|---|
| 单位方程 1 | 207.58149305614725 | 207.5687844070032 |
| 单位方程 2 | -173667.38459813932 | -173656.79940813163 |
| 单位方程 3 | 316229.92453749065 | 316223.4753016916 |
| 完整右残差第 1 项 | 95.883417245262 | 95.8775470268212 |
| 完整右残差第 2 项 | 10366.989854069874 | 10366.357976313051 |
| 完整右残差第 3 项 | 4974.314619295717 | 4974.213172451416 |

两份完整 112 项右残差都已导出，其高 109 项是原记录的负零；byte reader 确认 final 的负零数量为 109。原保存零尾 slope J 的所有 $112\times112$ 项已被诊断消费，原报告 offdiagonal maximum=0、nonzero count=0；这里实际用单位 $d_j$ 三方程符合原程序声明。高 109 项为零并不证明高核非共振，也不等于做过自由高核 Schur 消元。原 `high_free_core_Schur_elimination_computed` 与 `high_mode_nonresonance_proved` 都为 false。

## 4. 参数 Jacobian 与独立 FD 原读数

最终 $3\times3$ 参数 Jacobian 的原奇异值为

$$
(97599090.79852706,\;288778.53654451016,\;32.70194203275624),
$$

原 numerical condition 为 `2984504.4279255928`。这些是实际浮点诊断，不是区间横截性、唯一根或存在性证明。

| 实参数中心差分步长 | initial 原最大相对误差 | final 原最大相对误差 | 两端 valid |
|---|---:|---:|---|
| $2\cdot10^{-5}$ | 5.703773048305697e-09 | 5.838617692506499e-09 | true |
| $10^{-5}$ | 1.421710145901838e-09 | 1.4413267916294802e-09 | true |
| $5\cdot10^{-6}$ | 7.647593101659591e-10 | 4.754446417280586e-10 | true |

此处 FD 核的是这个三参数低模诊断的 `model.jacobian`；不能拿它替代后续 fullDN 当前非零 H 的真实 tail/J、完整边界 FD 或原验收。

## 5. Arb 的完整表达域与圆参考分别证明到哪里

原 [complete-scalar-domain.json.gz](public-actions-43662193286-1-smallcoreresonance/resonance/complete-scalar-domain.json.gz) 为 79207 B，SHA `8efa0be35549651bf8f8369cf7587c0b7cda240cebad67569686a9be9242be71`；解压原 JSON 428019 B。其精确声明的覆盖区间为

$$
[0,\;5113846463878377/2251799813685248].
$$

在原 160 bit、最大深度 14 预算下，报告 494 个叶子、51 次细分、0 个 unresolved leaf，`complete_declared_real_expression_domain_certified=true`。本次字节/JSON核确认全部叶记录完整、相邻端点记录相接、所有原叶的 $a>0,|ap|<1$ 判定为 true、definite failure 为 false；没有重新运行 Arb。

该 descriptor 的完整 scalar specification SHA 为 `df3a2d457c45ac09251f2a2b19de0636dab8be0265440fccab58c389966aabee`，数学表达 identity 为 `7e0ba93041ebd6abcb15939ab84b67f3926202ddba95f020a00bf4bdfd00cb86`。它保留原 finite-Gauss 表达与 source 独立返回的 `ap`，并明确不把 `ap` 等同于该 finite-Gauss $a$ 的字面导数。

原证书明确**没有**覆盖 literal binary64 evaluator roundoff、$a/ap/app$ 精确导数兼容或 C² 接口，也没有据此证明实际圆轨道 $R$ 或整个 Frenet 场的连续全域条件。报告这些界限不是给 README 增加新的门。

原 [circle-reference.json.gz](public-actions-43662193286-1-smallcoreresonance/resonance/circle-reference.json.gz) 为 139996 B，SHA `6c56f190c6e07538582bc6271caa6abe9d8eb5c59362579b8f87ee6d13f8afb1`；解压原 JSON 3568405 B。它完整保存 699×453 states/RHS、699 站点以及两个 699×3×2 低模数组。完整 scalar profile 的 final p 与本次 status 一致。

原圆参考读数：node-domain failures=0、midpoint-domain failures=0、原 4096 uniform-$\phi$ rho guard valid，minimum rho=1；两侧各 698 个原 RMS 查询的 invalid_count 均为 0。原 physical collocation max 为 `3.851492692483194e-16`，left、complete boundary、constant collocation max 均为 0。

这份圆参考的 `fixed_core_targets=[0,0,0]`，`original_large_core_targets_retained=false`；`full_native_tail_at_nonzero_height_computed`、`new_coupled_finite_acceptance`、`complete_closed_surface` 都为 false。它不是原大核非零边界的父解。有限圆轨道按原 $R'=ap\,R/a$ 的 collocation recurrence 构造，不暗中设 $R=a$。

最终 source-circle node/mid 最小半径为 `0.2999999984127463`、最小 beta² 为 `0.005153125420182092`；原 `R-a` node maximum 为 `1.987978948125857e-09`。三低模完整 FFT 方向核覆盖节点 0、349、698 的全部物理行，末端三项相对误差分别为 `4.344325842379889e-14`、`9.431641555030797e-14`、`2.464009425681324e-13`。这些仍是所列有限节点的原读数。

## 6. 本次身份审计及后继判断

[字节与记录审计](2026-11-15-actual78-original-byte-audit.json) 全部检查通过，范围为本包 10 个原 artifact 文件加根下载 marker，共 11 件；完整 gzip 解码、原 status/companion alias、父参数/完整父 status、全部 144 trial、圆数组尺寸、全部 494 叶记录、原 source receipts。另在本 checkout 逐 SHA 核了所有 68 个 pinned source，全部匹配。

本地没有四个大原数学输入的文件副本，故只交叉核本轮 Actions 的 verified input descriptors 与 request/status；没有声称再次独立读取 accepted/prepared/anchor/config 原 payload。78-of-91 原公共源恢复也沿该次真实 Actions 原 receipt，明确省略的是未执行的 Markdown 及未消费 client，而不是补造“91 件全恢复”。

下一步若继续此支线，机械地再续八个同样 Newton 小步缺乏本次证据支持。一个具体可评估的源级候选是：保留同一个三方程、同一个 `model.jacobian`、原标量域、未加权 merit 和 `.2` Armijo/20 回溯，只将参数方向改为显式正阻尼的列尺度增广最小二乘，并保持有限预算。它改变的是诊断搜索算法，不是共振必要条件或 BVP/native 门。任何阻尼参数、候选方向或更大接受步都须由新的公开 Actions 实际给出；本次不提供成功保证，也不预先替代独立高 109 模诊断。
