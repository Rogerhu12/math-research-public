# 2026-11-14：R252 新有限测试的独立完整切口审计接口

**状态：独立消费者已写；没有本地几何数值运行，也没有新场接受结论。** 数学对象和投影缺项见 [R252](../results/R252-physical-angle-DN-Galerkin-boundary.md)。本接口配合另存的 `physical_test_boundary/response/full_dn`，不修改原有限场、尾 DN、scalar 或接受门。

## 1. 调用方式

[`geometry_20261114_physical_test_cut_audit.py`](../computations/geometry_20261114_physical_test_cut_audit.py) 导出

```python
from geometry_20261114_physical_test_cut_audit import audit_cut

report = audit_cut(
    boundary, flow, endpoint, native_response,
    angular_levels=(4096, 8192),
)
```

- `boundary` 是新的 `PhysicalTestBoundary`，保留原 `FullDNBoundary` 的全部物理/trace API，另有 `physical_angles` 和 `pullback(core, slope)`。
- `flow` 是同一实际完整 `AugmentedFlow`；`endpoint` 包含全部物理、常值核心和 scalar 行。当前 $M=112$ 时是 453 行，不只传物理 338 行。
- `native_response` 是该端点原材料角输入对应的真实、已收敛 native 尾响应，包含完整 `checkpoint.cutHeight`、`jets.height/slope/meanSlope` 和同一配置。消费者不求解新尾。
- 当前新 full driver 在最终真尾 audit 后调用它，输出 `physical-test-final-cut-audit.json`，并在 `actual.json.gz` 中附完整报告及外部文件 SHA。原 `final_height_seam` 的旧材料角均值/一二阶测量仍保留。

数值入口检查自己运行于 `Rogerhu12/math-research-public` 的 GitHub Actions；本地仅作 AST 和源码核对。它不是一个另行启动 BVP 的 CLI。

## 2. 固定真实 DN 输入，精化只作测量

消费者先用 **原** `boundary.trace.N`、完整端点核心和高度重新计算 $H=e_hPz$，与实际 `checkpoint.cutHeight` 比较。使用现闭包消费者已有的 $10^{-12}$ 输入绑定容差，同时报告最大差和数组逐项数值完全相等与否（`np.array_equal`；正负零在此比较中相等）；两个独立 binary64 数组哈希保留实际字节身份。这不是新设的接缝或 PDE 容差。native 的模数、spacing、原 solveTolerance、cut 的 radius/E/Ep/backgroundSlope/backgroundSecond 也与当前原切口核对。

所有 4096/8192 层使用同一已求出的 $d=D(H)$ 和同一 `meanSlope`。8192 的重新投影高度单独报告与实际 $H$ 的差，**不调用** `D(H8192)`，也不把仿射内层图在新输入处的值冒充真实尾。源码中没有 `tail_map(...)`、`TailClient.solve(...)` 或任何新的全局 Jacobian/分解。

输出绑定完整 endpoint、实际物理 RHS、原 $H$、native checkpoint 高度、返回高度/斜率的 binary64 SHA256，以及 native 配置的 canonical JSON SHA256。外层原 driver 继续保留实际响应文件本身的 SHA。

## 3. 报告内容

在原实际两套角规则上独立重建 $P,S$，与实现的矩阵作共点对照，给出全部系数的 $R_\varphi$、原 $R_\theta$，以及

$$
(I-SP)v_+,
\qquad \gamma(PS-I)d,
$$

并核对 R252 两个有限矩阵恒等式的数值余差。每个加密层同样报告这些量；其中 native 响应保持固定。

均值部分保留完整物理 $z_0$。材料高度的共同平移使用完整有限核心的解析公式

$$
e_h\left(z_0+\sum_j\frac{1-4j^2}{2}c_jz_j\right).
$$

物理斜率均值使用 $v_0-\gamma(\beta+\mu^{\mathsf T}d)$；材料均值同时报告解析有限核心公式和本层实际求积公式，并报告 $\mu^{\mathsf T}+\lambda_N^{\mathsf T}S_N$ 的有限求积缺项。

全角读出包含：

- 完整材料高度及其各频带、相对于实际请求/实际返回有限尾高度的样点最大差和 $L^2$；
- 拉回后的完整 native 非均值斜率及其物理角高谱，扣除实际均值和前 $M$ 个物理 cosine 后的样点余项；
- 两种角度下，同一完整前缀斜率与同一真实尾斜率的完整样点差；
- 新旧残差、重新投影高度和正确物理均值相对原实际角规则的双层差。

谱报告明确区分有限 DFT、Nyquist 单系数和未证明的无限频率余项；没有把样点最大值写成连续角上确界。这里的 $L^2$ 也是该层完整样点均方根。

## 4. 接线核对与结论范围

原 main 的 inner、重新计算真实尾后的 true、最终 audit 三处 BC 检查都调用同一个分离边界；用新 `PhysicalTestBoundary` 后，三处自然检查 $R_\varphi$。原 `true_height` 保留原材料投影，正是所需的同一 $H$。原 `final_height_seam` 只在接受后生成测量报告，不参与上述 BC 接受；保留它能如实显示旧材料角门仍有多少未付误差。

当前 strict `exact_20261114_seeded_zero_tail_client.py` 及 `VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR` 继续承担已完成真实 T112 零输入/J 的复用。消费者不新增缓存层；任何新高度与最终 `audit=True` 仍由原真尾流程处理。

报告本身不新增接受阈值，不把新有限测试成功标作原材料测试成功，也不宣称完整 cut 九 jet、整面 metric、嵌入、reach 或真实像 Hausdorff 幅度已经满足。特别是重新投影高度的小误差、两条有限矩阵恒等式的小运算余差和实际遗漏谱是三种不同的信息，必须分别解释。
