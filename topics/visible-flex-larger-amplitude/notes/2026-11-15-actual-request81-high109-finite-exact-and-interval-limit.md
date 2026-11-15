# Actual 81：保存有限系数的全部高 109 模非奇异；声明实数区间模型仍有 103 模未排零

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：公开 Actions 实际数值与原件字节审计。** 完整数学计算来自实际 run 43664236768。本文只解析原 JSON、读取已保存数值和字符串、比较原文件与数组字节/SHA、核对模式和字段身份；没有在本地重算行列式、Arb 包络、RHS/J、矩阵作用、范数或候选优化。

**实际结果：在 actual78 的同一保存参数上，全部 109 个自由高模的保存有限系数两端矩阵均有精确非零行列式见证，且全部单位入口映射存在，因此这个有限模型的高 core Schur 块非奇异。另行定义的声明实数 Arb 模型，在最高 640 位后仅解决高模 4–9，模式 10–112 仍未排零。** 这两类结论分别成立，不能把前者替换成后者，也不能把区间未排零说成高模实际奇异。父低三共振仍未解；本次没有非零幅度场、真正非零 H 尾求解、full-DN 接受或闭曲面。

## 1. 实际运行与原件

| 身份 | 原值 |
|---|---|
| 公开运行 | [43664236768](https://github.com/Rogerhu12/math-research-public/actions/runs/43664236768) |
| source commit | `f19737ecf545a351551e8a73b6e5435e66bfd1c0` |
| job | `132659970694`，实际 success |
| 原 artifact | `14141865813`，`visible-mainline-high109-43664236768-1` |
| ZIP | 36,922,801 B；`c39178b549e88d8353026d286539280171909bb1781050ddba1b41954c7669a0` |
| 完整解包 | 476 个原文件；37,001,002 B |
| 科学源码 | `exact_20261115_r259_high_core_two_end.py`，49,546 B；`f60db29ef0c235cc4d5d2fa2ffecd480dccc4d54b46aafe655a60ba88af7013f` |
| 终态 phase | `bounded-diagnostic-completed-with-unresolved-high-intervals` |
| `diagnostic_completed` | `true` |
| `success` / `new_coupled_finite_acceptance` | `false` / `false` |
| 原保存用时 | 29.672122171000005 s |

root 已唯一下载完整 ZIP，核 size/SHA、全部 ZIP CRC、路径安全和完成 marker。本次审计从该已解包原目录读出，未再次下载 ZIP。原报告中的 `success=false` 是没有宣称原非线性 BVP 成功；它与这次诊断已完整执行、工作流 success 不冲突。原 `exception`、`unsupported_scope`、`budget_exhaustion` 均为 null。

全部结论可由本次 [逐模原值 readout](2026-11-15-actual81-original-readout.json) 追到原报告。其 112 行表逐模保留有限见证的符号/缺陷显示值、最新区间精度、排零标志、单位映射标志和原包络字符串；未重新求值。

## 2. 输入严格是 actual78 的候选，尚无低三共振

实际父 run 为 `43662193286`，source `11b5d25c436d84d734a73d4609092bde749daea5`。四个原父件在本次科学运行前完整保留，本文逐个 SHA/长度复核：

| 父件 | 字节数 | SHA256 |
|---|---:|---|
| `request78-input-and-source-identity.json` | 28,516 | `57a5d443b0f13193a385a40a13c5dc038dae768e97095074e08a6edca5fc5b58` |
| `resonance-status.json` | 50,438 | `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40` |
| `circle-reference.json.gz` | 139,996 | `6c56f190c6e07538582bc6271caa6abe9d8eb5c59362579b8f87ee6d13f8afb1` |
| `complete-scalar-domain.json.gz` | 79,207 | `8efa0be35549651bf8f8369cf7587c0b7cda240cebad67569686a9be9242be71` |

原保存参数为：

```json
[0.09365081258727412, -0.13201200770909496, -0.12389206129693811]
```

这三个值在父 status、父完整 scalar spec、本次 binding 和 finite model 中逐字节相同。本次没有修改或搜索参数。父 `low_mode_candidate_has_small_full_recorded_right_residual=false`，原低三单位缺陷为：

```json
[207.5687844070032, -173656.79940813163, 316223.4753016916]
```

父完整 112 行首阶右残差的前三项是 `[95.8775470268212, 10366.357976313051, 4974.213172451416]`，其余 109 项为原保存的零；这组三个值已乘固定低 core 目标，不能与单位缺陷混称。三个目标 `[0.4619073494154277, -0.05969451246161594, 0.015730056624372334]` 均非零。actual81 补的是完整高块消元条件，不会把原低三缺陷清零。

父 circle 是 699 个节点、每节点 453 个完整增广坐标的 **zero-core 圆形参考场**，保留实际半径和完整均值高度。它的 `full_native_tail_at_nonzero_height_computed=false`、`success=false`、`new_coupled_finite_acceptance=false`。读取完整 circle 并构成线性化，不产生可供非零同伦续接的已接受 parent。

四个原数学输入仍绑定原 accepted96、prepared112、真正 T112 零高度尾响应和 T112 config；原 SHA 分别为 `b4d2b98a…`、`0f94dd88…`、`e788a28d…`、`01930f3b…`。完整 SHA/长度在 [字节审计](2026-11-15-actual81-original-byte-audit.json) 的 `original_four_input_bindings` 中。request、运行前 identity、consumer binding、父 status 四处一致。本文另对现存同 SHA prepared/config 原件重读字节；accepted96 和旧零尾 wrapper 不包含在本次 81 artifact，未宣称在此重新读取它们的完整 payload。

## 3. 保持完整 112 模、全部节点和原尾矩阵

原完整尾 slope J 为 112×112，所有 12,544 个条目被消费和保存，原记录非零非对角数为 0。完整数组是 `<f8` C-order、100,352 B，raw SHA：

`44039f96cb20b0edca76a843a44f40235fbfbf72c19093a12a212c1cf6eb655d`。

逐模分解依据这个实际全矩阵的对角事实，没有阈值化条目，没有用 ready linear 图替代真正零尾 J。源码遇到真实非对角 J 时会明确报告本逐模分解不适用；本次没有进入该分支。

每模保留 699 个节点、698 个 2×2 L/R cell，以及左端 $H_j(0)=0$ 和完整末端行。因此每模两端方程维数为 1,398，全部 112 模共有 78,176 个 cell。高模入口 $U_j(0)$ 是自由 core，不被固定成零来省去未知数。

原 B/Bmid/L/R 块按原返回的 a/ap、保存 circle 半径和原 midpoint 表达式构成。有限模型末端行使用保存 B、gamma、height sign、完整 J 作为精确二进操作数，末端差没有再先做一次 binary64 舍入。模型身份为：

`4a58055035bac150de73fe3b8653e000cae8f0f028d2d9bf14eb389a1ab442e0`。

前三模从扩展到 112 模的 B/Bmid/L/R 中取出的原字节，与独立原三模宽度表达式的重放字节全部相同；这是本次保存的四个 true 标志，不是对所有后续计算的默认假设。

## 4. 第一层结果：保存有限系数的精确高块消元已完成

对第 j 模，原见证采用 [R277](../results/R277-complete-two-end-chain-determinant-and-high-core-elimination.md) 的完整两端恒等式：

$$v_0=e_1,\qquad v_{i+1}=-\operatorname{adj}(R_i)L_iv_i,\qquad \det\mathcal A_j=-\ell_jv_{698}.$$

这些精确运算已在 Actions 完成。本文读取它们的奇整数十六进制/二的幂见证和原布尔结论，未在本地再次递推或计算行列式。

| 完整原记录 | 结果 |
|---|---|
| 已完成 exact 模式 | 112 / 112 |
| 已完成自由高模式 | 109 / 109，模式 4–112 |
| 高模完整两端矩阵非奇异 | 全部 true |
| 高模单位入口映射存在 | 全部 true |
| 高模 singularity 列表 | `[]` |
| 高模 IVP elimination failure 列表 | `[]` |
| 109×109 core Schur 非奇异（保存 cell 模型） | true |
| 全部模式保存的单步右块行列式记录 | 78,176 条，原 singular-right-cell 列表均空 |
| 浮点传播逆 / 浮点秩阈值 | 均未用于此判定 |

完整 `finite-full-mode-schur.json.gz` 留下所有 112 模对应行。每行中的 unit-right-defect、inverse-diagonal map 和 flags 与该模独立 exact witness 逐值相同。该模型中左右低/高交叉块为零，高块对低三的 Schur 修正为零；全部高齐次内部场和自由高 core 的唯一解为零。**这个有限模型层面的条件已支付，不再只是“某个低三试探的高行残差为零”。**

这个结果没有给出良好条件数或逆的统一界；也没有证明所保存的块就是真正连续流或普通 FFT 程序的精确导数。输出 `finite_arrays_are_not_the_exact_mathematical_FFT_or_tail_derivative=true`，各 witness 的 `exact_original_FFT_or_tail_derivative_rank_claimed=false`。

## 5. 第二层结果：声明实数模型的区间排零只到高模 9

本层将原 binary64 节点、原 `np.diff` 宽度和原舍入 midpoint 位置作为精确离散常数，以完整 scalar descriptor 评价声明实数 a 与原 returned-ap，再用 Arb 重建圆半径及平方根分支。尾 J 仍是已保存的精确输入常数。这与“把保存的 binary64 半径和 L/R 条目当作精确常数”的第一层是两个明确不同的离散对象。

全部三个精度层的 shared-circle 包络均成功。各层都保存 699 个 node 和 698 个 midpoint 的完整 scalar、q、半径、平方根、margin 及 radius-cell 分母包络；本次未出现圆重建失败。

| 原精度层 | 实际评价的模式 | 本层排除两端行列式零的模式 | 本层剩余未排零模式 |
|---|---|---|---|
| 160 bits | 1–112，共 112 模 | 1、2、3 | 4–112，共 109 模 |
| 320 bits | 4–112，共 109 模 | 4、5 | 6–112，共 107 模 |
| 640 bits | 6–112，共 107 模 | 6、7、8、9 | 10–112，共 103 模 |

全部 328 份逐模 Arb 报告均保存：`unit_inlet_map_certified_defined=true`、`unresolved_right_cell_indices=[]`、有限的 boundary projective numerator。最高层未解决的 103 模不是由于某个右 cell 尚未建立单位入口 chart，也不是由于 source/域/超时异常。其完整末端行列式包络仍包含零。原示例为：

| 模式 / 最新精度 | 原完整两端行列式包络字符串 | 本模排零 |
|---|---|---|
| 4 / 320 | `[60015635.62818170207585660712137458159697 +/- 2.56e-33]` | true |
| 9 / 640 | `[1.3834753e+20 +/- 5.05e+12]` | true |
| 10 / 640 | `[+/- 1.72e+45]` | false |
| 50 / 640 | `[+/- 4.65e+1077]` | false |
| 112 / 640 | `[+/- 9.29e+1962]` | false |

这些字符串逐字来自原报告。它们不是本文新求得的数，也不能按打印近似值判断精确符号。原高块 summary 为：

- `all_high109_unit_inlet_maps_proved_defined=true`；
- `all_high109_two_end_blocks_proved_nonsingular_in_declared_model=false`；
- `high_free_core_Schur_is_diagonal_and_nonsingular_in_declared_model=false`；
- `unresolved_high_modes=[10,...,112]`；
- `wall_clock_budget_ended_interval_work=false`。

因此有限精度上限留下的是**尚未证明**。它没有证明上述高模奇异，不能用第一层 exact finite 非零见证把这些 interval flags 改为 true。也不能从这份记录直接断言增加位数必能解决全部高模，或直接将单个包络宽度归为某个物理失效。

低三模式在 160 位也已有原 unit-right-defect 包络：

```text
mode 1: [207.5687844069523566262755165122092694464 +/- 4.88e-39]
mode 2: [-173656.799408078428371006149626040 +/- 4.31e-28]
mode 3: [316223.4753016554 +/- 2.85e-11]
```

它们在本声明模型的这一个参数处同样没有给出低三共振。与第一层十进制显示或父普通数值缺陷之间的差异没有在本文作新的误差估计。

## 6. 全部原字节、身份及范围

完整 [byte audit](2026-11-15-actual81-original-byte-audit.json) 和 [紧凑审计摘要](2026-11-15-actual81-byte-audit-summary.json) 已保存。本次实际检查范围为：

| 对象 | 本次只读核对 |
|---|---|
| 全部 476 原文件 | 路径/长度/SHA 文件清单；与 root 已核解包计数和 37,001,002 B 一致 |
| 17 个 defining f64 数组 | 每个 gzip 文件长度/SHA/CRC、完整 raw 长度/SHA、dtype/order/shape；合计 10,188,696 raw B |
| 其中 B/Bmid/L/R | 完整 112 模所有块保留，合计 10,010,112 raw B |
| 112 个 exact-mode witness | 每件压缩 SHA/长度/CRC、完整 JSON、mode/node/频率/行序字段、每模 698 个右块记录；不重算见证 |
| 完整有限 Schur 表 | 112 行及 109 个高解值；逐值对应所有独立 exact 原件 |
| 328 个 Arb 模式与 3 个 circle | 所有原压缩文件 SHA/长度/CRC；全部原 JSON；history 请求序列、模式/精度及 latest 字段一致 |
| 全部 large payload | 461 件，receipt 指向集合与目录实际集合完全一致，无遗漏或新增未绑定模式文件 |
| 当前 source ledger | 69 个源码文件全部本地长度/SHA 对上本次原 identity；其中 11 个直接消费科学源独立对应 |
| 父来源 | 68 项父 ledger 逐项保留核对；publisher 的历史/当前范围按原 binding 保留 |
| 父 circle 原数组 | 只将原 mesh、半径、均值高度逐值打包为 `<f8` 字节，三个 raw SHA 与保存 defining 数组一致 |
| 模型身份 | 17 个原数组 descriptor 与 finite-model 全对应；按原 canonical JSON 元数据规则核回 model SHA |

这里的字节核查没有重新证明 integer/Arb 运算本身。保存的精确 witness 与其 source/输入一起形成可复查证据；本文没有独立执行另一套 determinant 或区间实现。

原 restored-source-preparation 报告记录恢复了原 manifest 的 78 / 91 项公开数值文件。本文读取并核其 source commit/manifest 身份，没有将这 78 个外部恢复 payload 全部再作一次独立本地审计；它们与这里实际重新核到的 69 项当前 computations source ledger 不是同一个计数。

完整 1,398×1,398 两端稠密矩阵没有形成，109×109 高 Schur 也未作稠密分解；本次不存在另行导出的完整 QR 因子。原 coefficient arrays、全部精确整数见证和 Arb 包络已完整保留，不能把这份清单表述为一个未导出完整矩阵/因子的逐字节审计。

## 7. 资源回执与剩余责任

原预算为 1,800 s、每整数最大 4,000,000 bit；最大实际观察整数位数为 85,956，峰值 RSS 280,944 KiB，三个 BLAS 线程环境均为 1。实际 29.672122171000005 s 结束，区间工作没有被时间预算截断。大整数操作的费用不被当作常数。

[R259](../results/R259-small-core-homotopy-and-resonance-conditions.md) 的低三共振、相应参数横截、共同域和非零幅度完整 BVP 仍未由本次完成。声明实数高块还剩 103 模排零；真正数学尾导数的误差、完整连续 ODE 的非共振、普通 FFT 导数误差和全 s 圆 Frenet 域也没有在此支付。原父 scalar certificate 的 494 leaves、51 splits、0 unresolved，只绑定它声明的 a/ap 范围，不能补成这些更强结论。

本次 exact finite 高块结论只绑定 actual78 这个参数、原 699 节点和保存的完整零尾 J。之后低三搜索若改变参数，不能直接继承本次高块非奇异。它也不阻塞当前 prefix 或 native 实际求解；没有增加接受门或把此诊断变成其前置批准。

## 8. 关键原件与审计身份

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| 原 `high109-diagnostic/summary.json` | 5,319 | `86793b12206f247adb4328ec52ce5e040d5f234f0a4787d1716efaec1f1f0345` |
| 原 `result.json.gz` | 163,089 | `bd7305b520f02ba963f66934ec016c5e606f07b67a9674d8cda4b78583720647` |
| 原 `input-binding.json` | 31,173 | `b96f23f3949023fcd9ed14a197f2eed27565fc66a7c599ba6dab48edf947fade` |
| 原 `finite-model.json` | 6,174 | `1a1904159094262c1132e9c0a1adf79d0aa1833f1e2c55b933990bcbba57aecd` |
| 原 `array-manifest.json` | 8,005 | `81d8db71d03337fdf20ade763daa2f6a2914660ce6ac77db5ba5c7a5c38a0e8f` |
| 原 `large-arrays/finite-full-mode-schur.json.gz` | 3,508,217 | `925a716805929d5089a4bfbd3509474ff392820f14965b5ade5f78331670d55b` |
| 本文 literal readout | 77,219 | `1a7326bcfcb7c58f239ccc699926056b233d8d05c1427944cf0fddca946297ba` |
| 本文完整 byte audit | 436,571 | `2b597c82ef8d5d02ffb745cc06661d6c56f616fb26fff7671ce44e114e8e26ea` |
| 本文紧凑 byte audit summary | 19,474 | `2ebfd6997b84ae1d0589b0f57e0b900757d1ac3398a80dab15903dafef99ec97` |

源码和解释依据为 [原消费者](../computations/exact_20261115_r259_high_core_two_end.py)、[冻结接口](2026-11-15-R259-complete-high109-two-end-diagnostic-interface.md) 与已证明 [R277](../results/R277-complete-two-end-chain-determinant-and-high-core-elimination.md)。本次没有改动它们，也没有将审计结果作为新的科学门。
