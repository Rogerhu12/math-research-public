# 同一精确背景的换网格：独立审查和重放

2026-11-09，`/root/independent_geometry`。已全文审读 `scripts/db6f-root-transfer-background.py`，冻结修正版 SHA256 为 `35aa82514ec2be4b78cf3670e97343d0ba50085a7a6a687273108fbb6eb09705`。已完成 M8/32→M8/64 的 coarse 重放，以及最终 M8 tight 包→M12 的完整独立重放，并另以精确 Fraction 检查随机普通盒和边界薄盒的全部系数端点。结论为 **PASS：背景值包可转移**，不据此转移旧曲面本身的 metric 或曲率界。

## 1. 固定 g 的参数判定

程序逐项比较旧、新 manifest 参数，只允许明确列入白名单的数值求解/评估设置变化。有限 source calibration 的 `calibrationSteps=512`、`protectCell=160`、所有 cap/valley/weight 控制、源指数、半径以及未知物理字段仍要求完全一致。原包的解析定义和证书 hash 保留。

原版 `e7b90916…` 对 `physicalDepth` 的保守拒绝实际阻止了 M12 试跑。审查者核读了真实源调用链：

* `closing_recalibrated_tail.mjs` 显式向 source 传 `depth:protectCell`，并只以 protectCell 控制几何的有限修改和径向组装。
* `db6f-prefix-tail-shared-core.mjs` 先创建 physical 背景，再把 `physicalDepth` 用于 shooting 子分段及有限稳定图；该字段随后写入 checkpoint 元数据。
* 已审解析 `FrozenSource` 根本不读取 `physicalDepth`。

因此此次 10→12 是数值求解覆盖深度的变化，背景仍修改固定的 160 个 source cells；将该字段加入数值白名单是对已有定义的核实，不是改 g 或放宽一个真正的物理参数约束。相应源文件 hash 为：shared core `95cd3c52b16f5c1605c52c9d67125cd914eb66370524fe1c22059c382888df39`，closing recalibrated `4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6`，weighted wrapper `740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e`。

旧、新整个物理半径域的 cuff 和 cut 必须精确相同。每个 increment 格式的网格先用保存的二进增量乘精确有理归一化常数，再按 Fraction 累加；外锚等式和严格递增均被检查。

## 2. 物理分割和二进薄盒

原 packet 的各行从原 span 的局部二进 u 精确变换成物理 r 端点。程序重新检查这些端点形成完整、无重叠的物理分割。

对每个新 geometry span，所有落在其内部的旧包边界都先用 Fraction 算出新局部坐标。若它不能由 binary64 精确表示，则同时加入向下和向上的相邻浮点数，将边界包进一个薄盒。排序去重后，每个新局部区间都有正长度；首尾为 0、1。

旧 owner 的选择是精确的正长度相交条件：旧右端点大于新左端点，旧左端点小于新右端点。仅在端点相遇的额外旧片不纳入，避免无用的远距离多项式外推。正长度 owner 的闭区间已经覆盖新盒全部端点。真正跨旧边界的薄盒仍纳入两侧 owner；多个边界落在同一个浮点邻接盒时同样逐一覆盖。

## 3. 仿射系数和逐点 hull

若旧包局部变量 x 与新包变量 τ 满足 $x=\alpha+\beta\tau$，则系数变换为

$$
\widetilde c_j=\beta^j\sum_{k=j}^d\binom{k}{j}c_k\alpha^{k-j}.
$$

α、β 先从精确物理 Fraction 得到，再向外包围。每次乘加均使用已审 I 区间后端。修正版也把 binomial 系数经 `qbounds(Fraction(...))` 输入，故其包含性不依赖 binomial 能否精确表示为 float。当前实际包为 degree 8；原版在此次输入中也没有整数转换问题。

跨旧片的薄盒对每个变换后的系数取区间 hull，统一余项取最大值。该包的语义是**逐点**区间多项式包围：对新盒中每一个 r，选择实际包含它的旧片，就得到一个属于所取系数盒的系数向量和合法余项。这个系数向量可以随 r 所属旧片改变。Bernstein 和后续乘法界是对盒中所有系数、所有 τ 同时成立的，因此仍包含实际值。

没有把结果误称为一个可微的单一精确多项式。w_r 是原包独立证明的真实 w_r 值包，不是对换网格后的 w 近似多项式求导。现有 consumer 正好只使用这些值；其所有 metric、曲率和协变 Hessian 公式都符合此作用域。

## 4. 完整重放

原版 coarse M8/32→M8/64 独立重放给 18514 行，4636 行跨两个旧片，所有 NPZ 数组与 root 输出逐元素相同。记录为 `2026-11-09-db6f-audit-transfer-coarse-m8s64.json`。

修正版对最终 M8 tight 包换至正式 M12 increment manifest，独立重放给 28928 行，其中 5235 行跨两个旧片。全部数组与 root 输出逐元素相同；完整新网格还被独立作者的 consumer 重新验证无缝覆盖。记录为 `2026-11-09-db6f-audit-transfer-tight-m12.json`。

以上是同一算法的独立执行。为另外检查浮点包含性，审查者另写 `scripts/db6f-audit-transfer-rational-samples.py`，使用精确 Fraction 重建物理域和 owner，并独立计算所选行的每个仿射系数的**精确最小、最大端点**。固定随机种子 56175，普通行和多 owner 行分别抽取 256 个候选，并加入首尾，去重后共 511 行，其中 295 行为多 owner 薄盒。

它实际检查 806 个正长度 owner、14508 个精确系数端点包含关系，以及每个 owner 的余项不被减小，全部通过。另完整检查了旧、新所有物理盒的连续分割。记录为 `2026-11-09-db6f-audit-transfer-tight-m12-rational.json`。这是一组可复现的随机有理抽查，未声称逐个有理检查全部 28928 行；全文算法审查和全数组重放负责全体行，随机精确计算提供不同实现的交叉核验。

## 5. 结论和边界

固定背景的 w、w_r 包可按此方法转到新的 geometry 网格，不必重做 source primitive 或 inverse 积分。它不更改背景、参数、有限扰动或物理域。旧包的解析合法性仍是明确依赖；新有限扰动的完整 metric、实际曲率、公共接缝、体积矩和其它闭图量仍必须重新计算，不能沿用 M8 的数值。该转移审查本身不支付 README 的固定 g 收敛或完成要求。
