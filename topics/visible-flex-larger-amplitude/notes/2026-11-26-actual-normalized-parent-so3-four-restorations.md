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
