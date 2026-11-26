# 实际父场 SO3 的四次完整恢复与剩余正违约

类型：公开Actions实际数值证据；尚无满足几何验收的场，不是连续度量或存在证明。

## 1. 真正返回与完整来源

公开[run45800076687/1阶段43/44](2026-11-26-public-actions-45800076687-1-part-004.md)已正常返回。阶段43完整执行2304.2760560449988秒、exit0；原四输入绑定修复已真正通过，不再是此前39/40的旧profile拒绝。实际源码提交 `f340991d3fb57e5c95215237365802183ea3d56c`。

| 对象 | 实际SHA256 | 字节数/职责 |
|---|---|---|
| 完整driver | `7e9095b3a765f064baae9a36e9593667d5c469686232b6095065e0c3cf22c55b` | 全变量/原约束/完整几何与Phase I |
| 完整launcher | `b5342ef4558d1e4da58618e308e5382eee50f9e4fab2a9dd95dc1acea8c8d826` | 实际阶段43入口 |
| 实际父绑定 | `9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55` | 完整四输入与准确profile绑定 |
| 原父bundle | `d021a50a492b941004ee75f5cba138d5b5bc07092073a642a027bde4f97bb478` | 同实际38父 |
| 新初场 | `18e2e2f9178194387da2b07708b032df9e939297828689478b6407550af2e31d` | 10720258 |
| 新末场 | `3ef8568c75bee9e2fbc85756abc5d90a579059e25c1bb9a3f25aad02ea132077` | 10720258 |
| 完整实际报告 | `3b73d81a30e1cb9925278549ee505462b175afae7da54b7e00b1c02948576b10` | 38828691，仅runner |
| 完整实际命令 | `2c84057350ba4eeb3ea8a52d389c560868156db921e72791e6f16110e6848904` | 10875，仅runner |

完整实际父绑定源SHA为 `9ca39afd9f840ba89fbb75d7365220c2d85d26ddb26b2d66b6c55e611313fd55`。固定准确profile为 `0a223b986f35263c168e26d30295fd84048e134c6b053ba90c7cd39beaf1f5cb`；重建context模型 `2ac30303c248e5f9f430ff16d567897a7795d485484970ea6380f3e9b9eb8af4`，四输入实际相等为true。完整绑定身份 `c0c49f9eaacb49accdfc05bafeece147652a560ddbb0dc49dd350d44896c36cb`；新场模型 `ad01742ce5051188bafddf8e93046468788eb27e7ec948c26903578742f5bb92`。

原完整准备/全部argv见[实际父绑定说明](2026-11-26-so3-actual-fixed-parent-binding.md)及[完整两步参数](../computations/resume-20261126-so3-actual-profile-complete-ready-steps.json)。没有由SHA补造原轨迹，没有复用旧场几何证书。

## 2. 四次恢复不等于一个度量下降方向

全部M160/J923/N2048、1333370个自由量、45324288原残差行保留。本次实际metric方向0、J/Jtranspose均0；4条restoration全部接受，理由是完整物理违约下降，不是Phi下降。

| 实际量 | 初场 | 末场 |
|---|---|---|
| max relative Gram | 0.03681563936938992 | 0.036815450191478395 |
| centered Phi | 0.00674442253617799 | 0.0067444403949395845 |
| maximum physical g | 0.033086027501670445 | 2.1482238210523974e-10 |

同目标Phi变化实际纯reader给 `1.7858761594546912e-8`，因此本次不是Phi下降结果。末必要reach product为 `0.9920000002148224`，仍略高声明的算法筛阈值.992；`final_geometry_feasible=false`与停止原因 `declared_restoration_budget; actual_violation_remains_and_is_not_accepted` 都保留。不能将一个小正数舍成0，不能将共松弛值或正常exit码当几何可行。

末幅度五项g分别为body `-0.047818882308271915`、plus `-0.09045752540391638`、minus `-3.3090759486067167`、cap `-0.1267448949002583`、Hfloor `-0.9649116523628666`。末2775曲率/2743半径位置、全部永久地点和双符号均实际重读。原正范数身份 `c4b2b25d8e8964139c82103b748a8573409cf9c996ebceb3c687596eabeba0fa`；metric和restoration末mu均.01。

初完整setup/read花1815.246737731999秒，子计算总计2298.754460926999秒，峰值RSS2105464KiB。实际residual调用6、point covectors784、parent jet读取16383次/22968792点、完整field读取41642578点、inverse chart求解19810次；最大实际逆残差4.440892098500626e-16、最小实际root rho .16590034724574898。这些工作残差不是准确连续root误差盒。

## 3. 纯读出与继续

阶段44原完整eb26 reader在6.1971624180005165秒exit0返回，实际source commit `a1c5fb8849fcfce75c7451b9c8169e484e77be01`；读出SHA `7f0877526e6421f481b95acccf6967f87cacee67f05a51a8ad41bb8a31adc497`，63072字节。其完整driver/目标/原prefix/实际final核对全部通过，summary errors和missing outputs均为空。

已排[四条完整恢复的纯标量归因](../computations/resume-20261126-normalized-parent-first-restoration-details-step.json)，读取实际alpha、全C计数、QP/Pg/容差、每次真实违约与slack。未读的具体内层状态不猜；后继从真实3ef85/3b73继续，准确g与所有来源保持。正违约必须继续处理，达到物理验收后才进实际metric方向；有限恢复、预算结束或约.0368的度量误差均不能完成课题。

## 4. 阶段45全部四次恢复的实际归因

[02实际阶段45](2026-11-26-public-actions-45800076687-1-part-004.md)已在6.161214300000211秒exit0返回，source commit `eba0597de81622f54e1b51580784b3243cb75ef7`；原eb261a78完整reader、3b73报告、3ef85末场及0a223固定目标均保持。读出仍为 `7f0877526e6421f481b95acccf6967f87cacee67f05a51a8ad41bb8a31adc497` / 63072字节，summary errors和missing outputs为空；本阶段只公开已有标量，没有新F/J。

| 修复 | 实际QP停止原因 / advances | Pg / 原容差 | common slack | 修复后真实g |
|---|---|---|---|---|
| 0 | face_and_unit_release_direction_tolerances / 20 | 6.980960468657986e-18 / 3.3086027501678233e-8 | 0.000003308271942198404 | 0.0023074479264456604 |
| 1 | face_and_unit_release_direction_tolerances / 15 | 7.686841535225377e-20 / 2.3074479264541203e-9 | 2.3072172151234957e-7 | 0.0000023221382660087997 |
| 2 | numerical_kkt_tolerance / 13 | 3.3591594073100078e-22 / 2.322138274468578e-12 | 2.3219062229996502e-10 | 0.000001966879851100778 |
| 3 | numerical_kkt_tolerance / 10 | 3.5554366815606782e-22 / 1.966879859560556e-12 | 1.9666832190872905e-10 | 2.1482238210523974e-10 |

全部四次均为alpha1、一次试步、真实违约下降后接受；每次原192几何行加5幅度行完整保留，原mu均.01，真实物理可行旗标全部false。活动面行数依次19、14、12、9。前两次达到face/release方向容差，末两次达到数值KKT容差；它们不是64步预算耗尽，因此直接增加内层预算不能解释已观察到的停止。

原Phase I允许所有行满足 $g_i+dg_i[Tz]\le\tau$，以 $.5\tau^2+.5\mu^2(|z|^2+\delta\tau^2)$ 平衡共松弛和步范数，$\tau=\tau_0+\delta\tau\ge0$。这个目标本身允许最优共松弛仍正；实际表中残余slack与正物理违反量都保留，不能称几何可行。

后继从真实3ef85/3b73继续，以明确正margin在Phase I搜索式中改为 $g_i+dg_i[Tz]+\varepsilon_{\rm in}\le\tau$。原物理$g_i$、全部原C及正行缩放、目标g、原norm和所有真正几何验收保持；这是更严格的内点搜索目标，不能作为允许正g的验收容差。实际新源/参数另行完整发表后才执行，若继续正违反就继续处理。
