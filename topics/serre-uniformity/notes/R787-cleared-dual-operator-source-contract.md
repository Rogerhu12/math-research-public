# 原清残差 dual 消费器：实际来源与实现契约

日期：2026-11-16。状态：来源与算法接口草稿；没有新的 dual 位数或接受结论。本篇不启动工作流，数学依据见[无逆转置证明](R787-original-inverse-free-cleared-transpose-value-acceptance.md)。

## 1. 独立身份

建议结果名 `R787-original-cleared-dual-CM-value-acceptance`，独立核心
`R787_cleared_dual_CM_value_acceptance.py`。数学 tag 至少绑定：

- 新核心及(D1)--(D21)证明 SHA；
- 冻结原 R787 核心 SHA `93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`，仅作为原算子规范及可复用 `ModularField` 的来源；
- 原 R781 字段核心 SHA `d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751`；
- 原 prime `1000000753`、chart/selection/稀疏 Z、十四 branch 的完整身份；
- 原 CM 候选 $q$ 的文件与所取 value 字段、准确 $e_0,e_0Z$ 来源；
- 原 field description、$J$ 的定义、行次序、$\mathcal S/\mathcal O$、目标清分母 $d$。

预算、允许追加位数和重构尝试间隔仅是运行控制。新 current 从本 RHS 的模 $\ell$ 解开始；没有 `initial_digits=518` 或把旧 primal current 改名的分支。

## 2. 已存在的 R787 输入

源是已结束 run `43737413555`，source
`4092d1cc4d1156bc24a10ff820fd39c5713e8ad7`，artifact `14181899102`。
平台 ZIP 为451202899字节，SHA
`343bee0a0fb5bf8d9143d2dbc8b8d8fc0f0da3649bbb1d94748ef34f19d87249`。
完整 manifest 为430709字节、1262项，SHA
`7a22beb22912c1d5c4c56a5faa577a529f6c5dab5bb4ea5251e9cd5c4264ba3f`。
旧数学 configuration SHA 为
`71ea66416a42e024de61cf5927bc493fbc8422dc1b5970d75c51bd788d88529d`。

纯 IO 必须逐原 manifest 取得：

| 成员 | 已核的身份/作用 |
|---|---|
| `R787-prime-1000000753-rational-blocks.json.gz` | 9169464字节，SHA `fb8a82957474e657fc476aa2baa0d8ce9f4c8b6cc86c2b55a79e75913d610b3b`；准确 Z、A选行及旧模逆 |
| `R787-prime-1000000753-chart.json.gz` | 5829字节，SHA `47ac1ce2a95781417a4e3b51f2128d2dd4836e5d1793cf2a50793911dcedce96`；真实rank1186/free1186 |
| `R787-prime-1000000753-selection.json.gz` | 5759字节，SHA `a420d94a9a2f56fa449946bac6379f437e7e53120a651d7df95b5f9ef9b07adb`；14合法原根及已成逆评价 |
| `R787-prime-1000000753-branch-00..13.json.gz` | 同一 manifest 的14条完整 stage，总202513410字节；每支的 chart SHA、根、1186 minor、逆、$C_{J,P}$ 和128个 inverse-clear 均须保持 |
| `R787-real-power5-row-0000..1233.json.gz` | 每条 `integer_t_coefficients` 为129×20；直接只读，禁止由旧 ξ 行重生成 |
| 原输入载体中的 R781/R786 子源 | 按旧 run/public/input receipt 与子 manifest 原 SHA 核；保 R781 原字段及000..129、R786原完整基身份 |

无需原 `dixon-00000518` 的73MB大向量，不需要14个旧临时 C-column blocks，
也不重算任一个旧逆。源 run 预算停不妨碍消费这些 `complete=true` 同标签阶段；
不得为便于使用而把其 core/run receipt 写成成功。

实际模逆字段名称已由冻结源码核定：

- `A_inverse_mod_prime`：1234×1234；`A_inverse_over_Q_computed` 仍为 false。
- 每个 branch 的 `Schur_minor_inverse_mod_prime`：1186×1186。
- 同 branch 的 `C_J_pivot_columns`：1234×1186。
- 同 branch 的 `inverse_original_clear_multipliers`：128×20，索引0对应 $1/(246^3\kappa^2)$，索引127对应 $1/(246^3\kappa^{129})$。
- selection 的 `inverse_evaluation_matrix`：旧14维坐标回收，不重新求逆。

载入可逐支解析 JSON 后只保 FLINT 模矩阵及小 header，释放大的 Python 整数列表；
不同时保留十四份完整 decoded JSON 和其矩阵副本。后续每一位只读这些完成对象。

## 3. CM 目标只读已完成的准确对象

原成功 CM 源是 run `43773420733`、source
`c3bcfc0dbbcd3a045349ec4500886100851a0d84`，最终证书 SHA
`5de210b5ebb2a8a7fefcc8799888a68353c9c2ac10725fafa239d2bd1082d20c`。
它的 full manifest SHA 为
`be2a58b2c87b6a79cb406d4cd1ecb04347f56f301373953e809d3bff68612642`。
这些小源已经通过 R841/R843 一日载体继续携带，允许从该已绑定载体提取；
仍以原 CM 的身份、原文件和原 tag 读取，不能改写为新 producer。

只需下列数学内容：

1. 原 `implicit_expression`、准确单位图和 $B_0\ne0$ 见证，用于确定是同一个原函数。
2. `power5_CM_values_and_jets` 指向的已有 power=5 块，每块 `rows` 中只消费 `value`；全1234项原顺序。其已成较低幂与 `derivative_z` 可在载体内保持，但不重新求值。
3. `exact_eZ` 的38个已成块，共1214个 `value`，已带原 Z 的负号。
4. 候选文件 `R787-implicit-CM-point-coordinate-reconstruction-candidates.json.gz`，6302字节，SHA `0be79ee2811881b0cbfe80a5fe71bf5dac0d9fdbeeb0631b69fa8e45596780f1`；只取其原 $y$ 的14个建议。

power5 与 eZ 的原值格式均是两个有理数，准确基已为
`1,s; s^2=-3`，不是旧 R790 的 `1,zeta`。两者的
`integer_scale=13744803133596058624`，即原幂五尺度已经应用。
将它们嵌入原14坐标时只放第0与第7槽；禁止再乘 $82^{10}$、
再改 $\zeta$、再乘 $\lambda^i$ 或插回原关系共同 denominator/content。

候选 $q$ 自己已经是原 $B=\lambda b,s$ 的14坐标，直接读取。
新目标 $qE_P$ 只是这两个来源的准确数域乘积。因 $E_P\in K$，
可用 $s^2=-3$ 的两块乘法形成，不需要新的七次最小多项式运算。
共同正分母 $d$ 的选择是本任务的新目标准备算术，不是重新计算 CM 响应。

## 4. 算子接口与形状

建议新 `ClearedDualOperator` 提供三个单一职责方法：

`apply_mod(chi, modulus)`：

- 输入128×280的原系数数组；280的次序仍是 $B^i s^j t^r$，$r$ 最内。
- 一次长度129反向卷积，原 $R$ 与 $\kappa$ 都只读已有正幂。
- 输出 `A` 1234×14、`P` 1186×14、`outside` 140×14 和 `free` 14；后者仅用于准确出口及诊断，不能混进平方求解目标。
- 对任意合数模数 $\ell^n$ 只用 monic 商环乘法、整数矩阵乘和原单位有理分母的标量逆，不使用合数模矩阵逆。

`solve_mod_prime(rhs)`：

- RHS 是上述前三块的2560×14。
- 依原14分支评价，先处理140项 outside 值，再用已成 A/Schur 逆转置作新矩阵向量乘；最后用128项旧 inverse-clear 得 $\chi$。
- 按原逆评价矩阵恢复2560×14并重新组织128×280；没有从数值拟合选择新行列。
- 对新的首 RHS 必须完整模乘回，之后每次修正也完整乘回。

`apply_exact(chi)`：

- 使用同一个(D10)--(D13)定义，输入准确有理向量，输出相同四块准确有理坐标。
- 先完整验证前三块等于准确目标，才读 free 块的单个 $L$ 残差 $\Delta$。
- 不允许只核某个 branch、随机点或部分坐标。

普通转置所用 $J$ 及整数逆先以新小 stage 完成一次。这个新配对不同于
原 trace/Hermitian 规范，不替换原曲线、极化或高度中的配对。

## 5. 断点、完成语义与禁止的冒称

建议新阶段前缀 `R787-cleared-dual-`，依次是：

- `source-audit`：原完整来源、形状、field/scale及选择闭包；
- `coefficient-pairing`：新20×20的 $J,J^{-1}$；
- `exact-target`：$q,d,e,-qE_P$ 的准确来源与共同清分母；
- `prime-solve`：本 RHS 的第一位，完整模乘回；
- `current-NNNNNNNN`：仅该 dual RHS 的实际新精度；
- `reconstruction-attempt-NNNNNNNN`：成功/失败坐标范围与实际重构证据；
- `exact-transpose-certificate`：前三块完整准确乘回；
- `exact-value-obstruction`：准确 $\Delta$ 与(D18)的原值解释。

每次只在“完整模乘回成功、current 原子写入、history SHA 更新”后推进精度。
旧大 current 可压缩为小 SHA 历史及最新完整数组，不能丢失尚未提交修正的唯一源。
准确 verifier 可按块保存已经完成的完整块，不重跑同 tag 的已成块。

终结状态须区分：

- `dual_linear_system_exactly_solved`；
- `original_value_rowspace_zero_A1_proved`（仅 $\Delta=0$）；
- `original_candidate_y_strictly_rejected`（仅解已准确完成且 $\Delta\ne0$）；
- `original_expanded_x_and_derivative_accepted`（还需原小L检查的真实通过来源）；
- 预算未到准确解时，以上接受/拒绝均为 false。

不论结果如何，旧 CM 四响应、原全129阶函数身份、非挠和 Hom 字 DAG
都没有被这份新 RHS 重算或替换。原同核 primal Dixon 可以独立继续。
当前只是完整执行契约，未创建 active request 或声称 dual current 已存在。

源码、参数、纸面证明及简明 run/SHA 可入 Git；全部机器向量、回执和矩阵
只在一日 active artifact/carrier 续传。
