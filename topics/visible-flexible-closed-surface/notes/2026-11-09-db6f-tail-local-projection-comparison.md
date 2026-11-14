# 四个冻结点的显式低阶投影量测

状态：**数值诊断已完整执行，待独立脚本/结果审查。没有实现或接入新 engine，没有改变活动 continuation。** `/root/tail_theory`，2026-11-09；第4个成功 root 输入由 `/root/coupled_prefix` 独立提取。

结论：所选四点上，显式 $q_2/B^L/UK$ 投影比原角求和更接近理想等距角点的高精度参照；仅在旧节点改写点态代数没有稳定收益。改动的原尺度归一 moment 差最大约 $4.77\cdot10^{-16}$，不能消掉失败点约 $0.022$ 的现有残差。**这些量测不支持把该次 global shooting 停滞归因于这几项投影舍入。** 它们也不是对所有径向点或所有高模的统一误差界。

## 1. 输入与执行范围

只使用以下四点，均保持原 guard `.05`：

| 点 | M/N | 来源与标签 | 原 min A |
|---|---|---|---:|
| M15 failed-default | 15/256 | 已闭 $\lambda=1/16$ stage35 失败案的合法默认 L；不是 root | .1623348281 |
| M15 failed-last | 15/256 | 同案最后一个接受的 L；不是 root | .05000005866 |
| M15 base-control | 15/256 | 原已闭 iteration0 同 stage35 的成功控制；重新计算一次原 root | .1721491935 |
| M14 control | 14/512 | 完整已解 M14/N512 tail 的 stage37/raw0/segment4/raw x=.25；一次原 root | .1179156034 |

最后一个点是预选对照，不称为整尾最坏点。两个 M15 失败点直接取已保存向量，没有再运行 root。M15 成功控制的 minA/minD/minS/residual/scale 与旧已审报告逐值一致；M14 root 用5次原 Newton 迭代、无 roundoff fallback。提取总计调用两次原局部 root，没有运行新的尾 shooting、RK、flow、DN 或变分 flow。

原 moment Newton 的小矩阵 B 仍由原 `evaluateL(...,needJac=True)` 取得，这是本计划比较的对象，不是新的整尾 Jacobian 计算。

输入包：

- `tail-local-projection-points-three.json.gz`，SHA `be48b24e08a8cdd6aec1b6c4c377ab62cb1a10bb989d19c98293bd666c7dbc86`，8895 bytes。
- `prefix-m14-q512-stage37-projection-input.json.gz`，SHA `62076b6b944cd1665fde25f3d4858322c5019af8b916e8e13ec663004781af4f`，113244 bytes。

本报告的 notes 短名均位于 `notes/2026-11-09-db6f-` 下。包内保存具体 CP、state 指针、L 来源、profile 点及原源码 hash，不从只有 minA/残差的摘要反推 L。

## 2. 实际比较定义

三种 binary64 评估如下：

1. **original**：原 pointwise moment q、原 B 和原 split nonlinear flux 求和。
2. **algebraSameTable**：同一 rounded 三角表，同一 N，改写 $q=q_2+R_q$、$b_m=L+R_B$ 和 nonlinear flux $=UK+R_F$，然后仍在全部角点累加。
3. **analyticLowProjection**：用已审系数公式投影 $q_2/B^L/UK$，只把余项在原表求和，最后相加。

所有原 pointwise P/Pt/L/U 和原 moments/quad/B 都被比较器独立重建并逐值核对相同。完整原 q 继续用于 `rows.quad` 语义、`maxQuad` 和 scale；没有用余项替代原尺度，没有降低 floor 或放宽原停止条件。原 B 中实际使用的是 `1+am`，其中 `am=Lv+w2*Pt`；比较器保留这一本来的浮点分组，不把它与 guard A 的另一浮点分组混同。

两个高精度参照统一固定相同 binary 的 E、w2、p、pt、L、U sine 系数。此层不重新施加 `E=1+w2`、`w2=w*w` 或重新形成 p/pt/U，因而没有把物理输入重派生混入投影差：

- **rounded-table**：把实际保存的 binary64 三角表视为精确常数，再高精度求和。它保留该表的正交缺陷。
- **ideal-grid**：对相同冻结系数，在理想等距角点与真正 $\sqrt2$ 的高精度近似上求和。

这三项纯投影的实数恒等式对上述独立固定标量仍成立。这里比较 B 的原数值定义，不额外将独立 E/w2 输入解释为新的物理 exact Jacobian。

参照以标准库 Decimal 的80位、120位分别计算；$\pi$ 用 Machin 公式，三角值用有限 Taylor，理想表利用整数模 N 的对称角索引。两档结果最大差约 $1.19\cdot10^{-78}$。**这是高精度稳定性诊断，不是有向区间误差证。** 全部参照计算耗时约1.42秒，没有调用 root。

## 3. 对理想等距参照的局部误差

以下是实际保存数字与120位参照的数值差，不是严格误差上界。quad 指 nonlinear moment 的投影向量，B 取所有条目最大绝对差：

| 点 | original quad 最大差 | analytic quad 最大差 | original B 最大差 | analytic B 最大差 |
|---|---:|---:|---:|---:|
| M15 failed-default | $1.1723\cdot10^{-16}$ | $1.2178\cdot10^{-17}$ | $2.4773\cdot10^{-15}$ | $1.4608\cdot10^{-16}$ |
| M15 failed-last | $1.1015\cdot10^{-16}$ | $1.2783\cdot10^{-17}$ | $2.1728\cdot10^{-15}$ | $1.9312\cdot10^{-16}$ |
| M15 base-control | $8.2594\cdot10^{-17}$ | $6.7730\cdot10^{-18}$ | $2.1128\cdot10^{-15}$ | $1.4509\cdot10^{-16}$ |
| M14 control | $7.4649\cdot10^{-17}$ | $3.0651\cdot10^{-17}$ | $2.1326\cdot10^{-15}$ | $1.3417\cdot10^{-16}$ |

quad 的最大差约改善2.4至12.2倍，B 条目最大差约改善11.3至17倍。nonlinear flux 的全模最大差也下降，完整逐模/矩阵数据在机读报告。使用原 pref 乘频率后的 nonlinear momentum RHS 部分差单独保存；没有把它冒充完整 RHS 或整条积分误差。

最高四个 quad 模的最大差，依次为

$$
(1.17\cdot10^{-16},1.07\cdot10^{-16},3.31\cdot10^{-17},3.79\cdot10^{-17})
$$

降至

$$
(9.85\cdot10^{-18},3.18\cdot10^{-18},5.55\cdot10^{-18},3.06\cdot10^{-18}).
$$

但不能声称每个单模都改善：第一个点的最高单模误差由约 $2.91\cdot10^{-18}$ 增至 $9.85\cdot10^{-18}$。完整高模收益是这四点的有限统计，不是单调改进定理。

两个成功控制点的最高单个 quad 模误差分别由约 $1.12\cdot10^{-17}$、$3.61\cdot10^{-17}$ 降至 $8.37\cdot10^{-19}$、$5.71\cdot10^{-19}$。不过，这些点的最高 $q_2$ 模本身分别约为 $-.007134$、$-.001434$；两个失败点则约为 $.034014$、$.037869$。因此所选点并未直接展示“最高 q2 系数已经小到机器噪声”的情形。

仅做 `algebraSameTable` 的 quad 最大差有时升、有时降；B 最大差仍与 original 相同量级。rounded-table 与 ideal-grid 参照之间的 quad 差约为 $7.45\cdot10^{-17}$ 至 $1.14\cdot10^{-16}$，说明表与原点态评估的舍入结构不能被忽略。本数据的改善主要来自显式投影，而不是仅把原节点上的表达式换一种写法。

## 4. 与失败残差的实际尺度比较

在原始固定 L 上，三个评估给出的最大目标残差为：

| 点 | original | analyticLowProjection |
|---|---:|---:|
| M15 failed-default | .04161005981724321 | .041610059817243264 |
| M15 failed-last | .022098839777481026 | .022098839777481047 |
| M15 base-control | $2.77556\cdot10^{-17}$ | $8.32667\cdot10^{-17}$ |
| M14 control | $5.55112\cdot10^{-17}$ | $7.52436\cdot10^{-17}$ |

新旧 moment 向量的最大差除以原 scale，四点依次约为

$$
4.77\cdot10^{-16},\quad4.46\cdot10^{-16},\quad
4.08\cdot10^{-16},\quad2.95\cdot10^{-16}.
$$

它们都远小于原局部 root 的 $8\cdot10^{-14}$ 常规相对停止门。失败点的约 $0.022$ 残差保持不变，两个成功控制点在新评估下仍远在原门内。这些都是固定输入的数值事实；没有运行改变后的 Newton，也没有证明全局 shooting 对这些差量的放大系数。

因此本轮没有把它作为恢复全尾求解的理由。它保留了一个有真实局部精度收益的后续备选，若未来出现经过量化的舍入 floor，再单独考虑已审派生实现。

## 5. 冻结文件与复跑

| 文件 | SHA256 |
|---|---|
| `scripts/db6f-tail-local-projection-points.mjs` | `837a2361bdf17731903fdf31afaadd1c46023db63bcff665feeec0f2f621a377` |
| `scripts/db6f-tail-local-projection-values.mjs` | `99aec526e2cc5c7949a2050f18b3f98c02cd8c270821fbb44a09c6f21b889444` |
| `scripts/db6f-tail-local-projection-reference.py` | `5ab87f037a40579bae5164ef0b50b9e701d58703411177569a91ec94b810249a` |
| `tail-local-projection-values.json.gz` | `8146e56b0a1d9f9dcd03d5bc5f81ea955112d2f8f8962ad65d6611f79f8595a3` |
| `tail-local-projection-reference.json.gz` | `89886e6ed3b5d68adb07ebe3f82473061ae5a91ff8d44c6aaf537a9f2dc3e601` |
| `tail-local-projection-summary.json` | `9f13b792b14e7e486e365cfc13659ad417fff3af75d82eaf9e2ab19d2f2d96a8` |

source extraction、binary64比较、高精度参照均实际退出码0。比较层已经逐值复核原输入和原输出；完整独立审查另行记录。值/参照两层复跑只读取两个冻结点包，调用0次 root，故不需要重新计算全部尾或重复任何扫描。

所有结果只属于这四个冻结点。它们不改变已审闭图，不证明真实高模联解、全域 metric 收敛或无限非线性尾存在，也不构成 README 完成。
