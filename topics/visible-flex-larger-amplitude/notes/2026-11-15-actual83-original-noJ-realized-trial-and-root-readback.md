# 第 83 轮：原 noJ 实际试步、完整根返回与字节读回

日期：2026-11-15。作者：geometry 分支。分类：公开 Actions 原始回执和只读字节审计。

**结论：这一次实际原 `evaluate(false)` 完整返回，全部 576 段原域检查通过；原范数仍为 `6.0618737006888706e-5`，与第 73 轮末轮、末次试步的原值逐位相同，严格下降为 false。** 本轮只重放既定的一个试步，没有重新求方向、生成 J、调用原 native solve 或取得完整 native 接受。`native_accepted=false`、`task_completed=false`、`failure_cause_proven=false` 保持原义。

这不是状态完全没变的重放：完整 577×224 个原坐标状态词中，生产者保存的改变词数为 103,123，本次字节审计独立重数得到同一数目。另一方面，报告控制行对应的若干状态坐标确实保持原词。二者须同时保留，不能由局部词不变推成整个方向为零。

## 1. 唯一实际运行及原输入

公开运行：[request 83 / run 43668743706](https://github.com/Rogerhu12/math-research-public/actions/runs/43668743706)。工作流源提交 `8d199eda5c1f1df162ded244e8dfd012e0c8d127`，job `132673843713` 实际 success。官方 artifact 为 `14143009723`，48,375,172 字节，ZIP SHA-256：

`9eadec9633a1260597268a760b5870bf59bd18ef808e8c5eb6ac5e006df5634c`。

主控唯一下载并核对官方 tuple、ZIP 和 CRC；本分支读取该已完成目录，没有第二次下载，也没有重新执行其数学计算。本文负责 `actual73-realized-trial/`；同包后续精确增量分解由独立消费者及其正式报告负责。

| 原对象 | 实际 SHA-256 |
|---|---|
| 第 73 轮原 native result，7,583 B | `ade4fdac3adce104cb4e216e9d2f40b219bfca47d2c027ac548e6c65f65ab394` |
| 第 73 轮 iteration 002 snapshot result，1,313 B | `2f9bf170c0366e9d5adaf003a9d0746f28a536171a32339e8a5f502313495e92` |
| 同轮 QR direction result，4,596 B | `9d464f8239c375a2e95f207a3cfbad33e1f36037cd450cfefa2e3b165d86e3ff` |
| 原完整 base，577×224 binary64 | `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` |
| 原完整 delta，577×224 binary64 | `4b4b1aaacd96910635a03f97d45957ae995c724997a0e18b66ac1d06408e294a` |
| 本次原表达式实际形成的 trial state | `395ba7f618fdca317eba1fc720b1829437157e8fcb75a0a9b0fbe744756f07a4` |

选定的是原 call 1 / iteration 2 / trial 9，原事件时间 `2026-11-15T01:32:57.175Z`，原类型 `residual-not-decreasing`。步长严格为原第十项 `2**(-9)=1/512`，binary64 小端词 `000000000000603f`。实际状态形成仍为：

```javascript
const lambda=2**(-k),trial=states.map((s,n)=>Float64Array.from(s,(v,j)=>v+lambda*cor.delta[n][j]));
```

保存的完整 H、target、原 scales、far graph 均进入此次原求值，未投影 cut/far 方向、未把 H 截成零。base 无负零，原 delta 有 25 个负零，trial 无负零；三者原词完整保存。trial 共 129,248 个有限词，无 NaN 或无穷。原参数仍为 M=112、K=224、depth=576、steps=12、quadrature=2048、shootingParts=8、orientation=1、spacing=2；原 `solveTolerance=2e-9`、`maxIterations=32` 在配置中保持，本诊断没有进入 solve 循环。`rawNode` 仍为 `[0,72,144,216,288,360,432,504,576]`，不是 577 项的 shooting node 列表。

## 2. 此次真正执行与真正未执行的范围

| 原保存字段 | 读数 |
|---|---:|
| `original_noJ_evaluate_calls` | 1 |
| `original_native_solve_calls` / `newton_corrections` | 0 / 0 |
| `new_J_evaluations` / `new_withJ_evaluations` | 0 / 0 |
| `completed_stages` | 576 |
| `original_root_returns_observed` | 27,772 |
| `observer_failure_count` | 0 |
| worker exit | 0 |
| 原 noJ 段记录用时 | 70.766 s |
| Python 完整 probe result 用时 | 90.602832433 s |

原 constructor trace 实记 `fourier-root-and-product-moments-v1` / `full-shooting-tangent-v1`；stderr 为空。stdout 只有既定诊断开始和完成事件。所有 noJ flow 的 `J` 均为 null。保存的末轮 J 只以原完整 descriptor 身份绑定；本 native probe 没有读取 J payload，更没有据它重建一个替代 nonlinear 返回。后续 exact-h 消费者另行读取已保存 J，两项工作的范围不能混写。

本次完整返回了实际 cut、576×224 stage residual、far residual、各 stage output 和 meanHeight 增量；其原数组全部保存。`base_state_unchanged`、`direction_unchanged`、`actual_trial_state_unchanged_by_call`、`target_unchanged`、`scales_unchanged` 均为生产者实际 true 记录。

## 3. 原范数与控制行：复现了一个明确的 plateau

原 base withJ 范数、原第 73 轮 trial 9 范数和本次完整原 noJ 范数均为：

`6.0618737006888706e-5`，binary64 小端 `71f299f11bc80f3f`。

本次原规范化扫描也返回相同词；这项扫描在 Actions 内已经完成，本文仅读取其原结果，没有本地重算范数或 argmax。

| 原报告控制位置 | 原读数 |
|---|---|
| stage / rawCell / rawSegment | 10 / 0 / 7 |
| block / mode / frequency | Pi / 76 / 152 |
| stage 内零基列 / 完整零基行 | 187 / 2539 |
| 原 residual | `3.1340219048409113e-19` |
| residual 小端词 | `000000000020173c` |
| 原 scale | `5.170054771158893e-15` |
| scale 小端词 | `08d0dad5aa48f73c` |
| 非有限残差项 | 0 |
| 原严格范数下降 | false |

保存的 base 与本次 trial 的控制行描述逐字段相同；相应 residual/scales 的真实数组切片又独立匹配这些词。**这只证明控制读数与位置相同，不证明两个完整 residual 向量逐词相同。** 例如同 stage 的 Pi 第 73 模，保存的 base residual 为 `2.795208725939191e-20`，本次实际 residual 为 `6.903318520122548e-20`；这些也是直接解码原保存数组，未由 out−state 在本地重建。

## 4. 两个已报告位置对应的真实状态、输出词

下表给出 stage 10 的出端 node 10。Pi76 是原完整 noJ 的控制行；Pi73 是后续精确分解报告的另一重要行，本文不代替该分解计算。

| 原词对应对象 | Pi73，column 184 | Pi76，column 187 |
|---|---:|---:|
| base state | `-1.5265602177351432e-6` | `1.0198514712387176e-5` |
| actual trial state | `-1.5265602177351432e-6` | `1.0198514712387176e-5` |
| 原 delta | `1.548283387599687e-35` | `1.2386267100797497e-34` |
| 本次 stage output | `-1.5265602177350742e-6` | `1.019851471238749e-5` |
| 本次原 stage residual | `6.903318520122548e-20` | `3.1340219048409113e-19` |

Pi73 的 base/trial 小端词都是 `8402bcb5869cb9be`，out 为 `3e01bcb5869cb9be`；Pi76 的 base/trial 都是 `fae064304963e53e`，out 为 `b3e164304963e53e`。入端 node 11 的这两个分量也各自 base=trial，完整字面词及 delta 已保存于 [两行字面读数](actual83-two-rows-literal-words.json)。

这些是原数组索引、字节比较和 binary64 字面解码；本地没有计算 `alpha*delta`、`nextafter`、ULP、out−state、误差比或新的线性作用。也没有把后续“精确实际增量与理想增量之差”缩称为“最后一次加法”的误差：原表达式还包含步长乘法，只有完整 Actions 分解能够给出本次实际数值贡献。

## 5. 完整根返回：没有域异常或 roundoffFallback 返回

原求值观察到了 27,772 次成功 root 返回，完整归于 576 个 stage packet：545 个 packet 各 48 次，31 个各 52 次。保存的 `iterations` 字段为 0 的有 26,868 次，为 1 的有 904 次。全部记录的 `roundoffFallback_present=false` 且 `roundoffFallback=false`。这只是原字段计数，不是另算求解迭代、误差阈值或根精度。

每次 root packet 保留原 profile index、原 x、完整 226 状态 SHA、原 err/scale/iterations、原 L 和 moments SHA、原 geometry 的 r/drdx/logw/dlogwdx/oldR/oldDrdx/chi/w/w2/E，以及原 minA/minD/minS/maxQuad。每段入端 224 状态 SHA 与实际 trial 的 node n+1 字节行一致；每段输出、残差、scale、mean 的原字节又与 15 数组逐项对应。

stage 10 的 48 个 root 返回中，42 条的 iterations=1，6 条为 0；全部无 fallback。其第一个及最后一个原返回如下，未在本地形成任何 err/scale 比值：

| 原字段 | root return 0 | root return 47 |
|---|---:|---:|
| profile index | 0 | 0 |
| x | 0 | 1 |
| err | `6.979497708007332e-39` | `9.183549615799121e-40` |
| scale | `4.566791142683049e-12` | `3.676674651929948e-12` |
| r | `0.2965051898918676` | `0.2978214791588106` |
| drdx | `0.00018604093414859566` | `0.0018252499449338856` |
| w | `0.10368669699556751` | `0.09341689960422137` |
| E | `1.0107509311338507` | `1.0087267171316652` |
| minA | `0.9999999999869664` | `0.9999999999863609` |
| minD | `0.9999999999999886` | `0.9999999999999859` |
| minS | 1 | 1 |
| maxQuad | `7.98780643341984e-24` | `6.169567913770856e-24` |

本 noJ 总体返回的 minA/minD 都是原 `+Infinity` 占位词 `000000000000f07f`；每个 noJ flow 的相应可选字段缺省。它们不是一个新增 finite 门，也不能误报成域失败。实际 root 的那些局部原字段已另存，二者层级不同。

完整 stage 10 packet 的压缩 SHA 为 `9579efd8a88a5bb9397daf37a169dda34ca3c80e8072ff2b79a46a02a4feb6af`，14,799 B；解码 100,841 B，SHA `a7578634923a9642c8302c3173ba37d6bd401364f4d87d0a930aef7cde81bb78`。其所有 48 个返回已逐字段并入本文的压缩原读数文件，576 packets 的全部原件仍由固定 artifact 保留。

**不能扩大该证据：** root 的完整 226 状态、L、moments 在 packet 中只有 SHA，没有逐数值 payload。本次审计核其已存 SHA 格式和 packet 身份，不冒称重新核到了未导出的内部向量，也不从这些 SHA 重建高模分量。成功返回且无 fallback 不证明浮点 root/flow 已达到某个新精度，更不证明一个不可突破的真实误差底线。

## 6. 观察插入的原源码身份

冻结 producer 为 `305f5db2c6bc0fef85bd3115045531b1b366334b33300852634692a537f7d9cb`；hook 为 `c03f59e4c3b6555a7a47187f1905a70f1e5a92dafacc222c327f4913c3ccdce0`。

本次 observation 的 actual evaluate SHA 为 `61246ec260124b066e9cd705d4a3ae03df60ba79cea19cafd14ac2892aa0d326`，逆向撤回唯一 stageEnter/stageReturn 后恢复原 evaluate SHA `9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9`。完整保存的原/改 runtime core 和 root 源文本也分别独立做了精确替换撤回及 SHA 核对；原 residual/norm/boundary/guard 算式、root 两个原返回判据、原 line search/iterations 都没有被换掉。`Function.toString` 没有伪装。

原 root 正常返回观察的是同一原对象；fallback 分支仅在原 spread 返回对象上命名以观察它，未改数值或判据。本轮该分支没有实际被走到。原八个 engine instance 的 root/rhs/rk4/rhsWithJacobian/flowStateWithJacobian 方法身份一致，first_stage 仍是 0、72、144、216、288、360、432、504。真实 original ready/capacity 在求值之前已核；本次字节读回再核 89 项已保存的 launch/source digest 对应关系。

worker 只替换原请求 loop 以进行这一次诊断。worker 回执保存了前后源码 hash 及生产者的 roundtrip=true，但没有保存那两份完整 worker 文本；因此本文将其表述为原生产者回执，不冒称在此次 artifact 中重新独立做了 worker 文本还原。root/core/evaluate 则有完整文本，三项本次独立还原均通过。

## 7. 完整字节范围及输出身份

本次只读审计覆盖 probe 子目录全部 **613 件、14,299,594 字节**，不是仅挑摘要：

- 15 个完整 raw 数组，共 6,214,024 B，全部 shape/dtype/order/bytes/SHA 匹配，保留负零。
- 576 root packet 共 7,466,582 B 压缩原件，解码共 57,672,999 B，全部双层 SHA、位置、真实入端行及出端 flow 别名匹配。
- 27,772 root 返回逐项解析，共验证 473,295 个已存 numberRecord 的十六进制词、分类与 JSON 字面值一致；没有求新的科学极值。
- 576 段 output/residual 的完整行 SHA、scale 和 mean 单词全部对应到实际数组切片。
- 原 result/summary/spec/binding/manifest/source 回执相互对应；原最坏 residual/scale 真实词与报告一致。

审计状态为 PASS。它证明的是上述读取、身份和字节对应，不代替原科学验收。

| 本轮原件 | 字节 | SHA-256 |
|---|---:|---|
| result.json | 2,679 | `7be2d7f0a98445e5efcd0ba146b7f8257483fa7593a54a6b389e8279f7fcf6ea` |
| summary.json | 6,091 | `3142ac7893e2adc5d03168c38be69e5e513e999cd1d65a0e37ef4b084caffc5e` |
| array-manifest.json | 4,068 | `455a896ea3fa4842c349849bb3a2be203fad94009b2be6c225df750dd4b2c1ea` |
| complete-flow-return-metadata.json.gz | 70,711 | `8bec81df599a2e854a9a04ef0520fc75dfc93df0053105bbfa45bbd80f660bd2` |
| root-return-packet-manifest.json | 157,973 | `539b6729c26ed3e4ea8c591751bd09822bf097c7ef6026dd7e247f20fc4437f1` |

与本文同存的 [byte audit](2026-11-15-actual83-original-noJ-probe-byte-audit.json)、[全部件及段级 inventory](2026-11-15-actual83-original-noJ-probe-complete-byte-inventory.json.gz)、[完整原字段读数](2026-11-15-actual83-original-noJ-probe-literal-readout.json.gz) 给出全部原件清单、原 summary/result/flow metadata、根清单、完整 stage10 root 返回以及来源文本。字面读数文件是明确的字段转录，原文件字节身份仍以各自 SHA 为准。

本地只进行了 SHA/size、gzip/JSON、位分类、字节切片/比较、源码字符串还原和元数据计数；没有导入科学模块，没有重建 trial，没有重新计算差、norm、argmax、J 作用或精确分解。没有重新下载或重审完整第 73 轮原大包，也不把本包没有的父阵列 payload 标成已读。独立 exact-h 分解的完整逐行账、线性模型和原因范围应引用该分支的实际报告。

## 8. 对下一步的约束

第 83 轮已经补齐原第 73 轮没有保存的这个实际试步的完整 state、cut/stage/far residual、stage outputs 以及原根返回。现在可以把“理想步长方向”“实际 rounded trial state 的精确增量”“原 noJ 实际输出”作为三个有明确原件的对象比较。

这一新证据支持针对状态表示及实际 flow/tangent 差异作下一有因实验；它不支持仅重复同一方向的小步回溯，也不支持把某一行的主贡献提升成全向量唯一原因。原 32 轮、十个 alpha、完整 guards、严格原范数下降、最终 `2e-9` 和真实 final sensitivity/audit 均未因此改变。此次诊断的完成与本题完整 native/闭场完成仍是不同状态。
