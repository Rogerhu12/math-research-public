# M112 完整有限场的物理读出与自身尾闭面入口

**可信度：已完成源代码与静态接口接线；尚无本入口的数值成功回执。** 本条没有重算 BVP、Frenet、尾或网格。M112 的真正完整求解仍由公开 Actions 的独立 full-DN driver 决定；准备场或零补高模初值不能进入这里。

## 输入身份

消费 `geometry_20261114_lifted_modes_profile.py` 的
`complete-prefix-controls-independent-field-modes-v3`：

- `base_prefix_M=96` 保留实际接受来源的原身份；`field_modes=tail_modes=112` 指本次完整场和实际尾。
- `field_representation` 明确为原有限 rotating-phi Fourier full state，原角向 quadrature 为 2048；没有 analytic-circle lift。
- 物理状态是 $3M+2=338$ 维的完整 `r0..rM,t1..tM,z0..zM`；增强状态是 $4M+5=453$ 维。完整 $z_0$ 已包含在状态中。
- 三个控制的支撑、degree-6 bump 定义、全部最终控制值和完整 scalar 来源 hash 都由 v3 保存并重构，不能换成拟合的单个 quintic。
- 入口保留原接受门：真 `success=true/status=0`、完整实际尾、collocation RMS 与 frozen-physical RMS 不超过 $10^{-6}$、BC 不超过 $10^{-11}$。没有另加机器精度的 C² 收敛门。

## 五个独立新源

| 文件（`computations/`） | 作用 |
|---|---|
| `geometry_20261114_lifted_modes_saved_prefix.py` | 将真正接受的 v3 完整场接到原 LargeCoreSavedPrefix；保留原物理 quintic、全 $z_0$、材料角逆映射、六 jet 与九 jet |
| `geometry_20261114_lifted_modes_readout.py` | 在同一物理场上作 2048/4096 材料角与径向 2/4 网格读出，同时计算分量和真实相对算子度量误差、曲率、最差点 |
| `geometry_20261114_lifted_modes_material_tail_packet.py` | 复用原完整角投影、六 jet 和 core-map 导数算法，改用完整冻结 scalar 身份；诊断实际尾模数及较高预算的截断误差 |
| `geometry_20261114_lifted_modes_closed_assembly.py` | 对本次实际尾作原径向读出，使用一次 proper SE(2)、本场自己的材料均值、完整角向九 jet 的 outer correction，组装闭面 |
| `geometry_20261114_lifted_modes_after_accept.py` | 顺序执行前述读出与闭面，并汇总整个闭面的已检查样本误差与曲率；不重解 BVP 或 DN |

原源码和旧报告的 hash 不变。静态验证包括五文件的 Python AST 解析、未解析全局名检查、维数/字段路径核对，以及原闭面和 packet 的算子范数公式检查。没有用伪造的成功 checkpoint 作数值“测试”。

## 一条公开 Actions 调用

在 full-DN driver 真正生成 `actual.json.gz` 后运行；下面环境变量均为该公开 job 已有路径，`VISIBLE_112_CONFIG` 必须是该实际尾调用的原 config。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_lifted_modes_after_accept.py" \
  --checkpoint "$VISIBLE_FULL_DN/actual.json.gz" \
  --port "$VISIBLE_ORIGINAL_PORT" \
  --tail-config "$VISIBLE_112_CONFIG" \
  --tail-response "$VISIBLE_FULL_DN/actual-tail-final-audit.json.gz" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_OUT/accepted-112-physical-closed" \
  --angles 2048 4096 \
  --radial-subdivisions 2 4 \
  --readout-levels 1,2,4
```

该入口先核对 checkpoint 的实际最终尾 response SHA、原 config SHA、完整原 port 和全状态维数。然后生成：

1. `physical-material-prefix.json`：相同完整物理 quintic 的材料角读出。
2. `material-cut-packet/`：默认实际 $M$ 与 $2M$ 的诊断预算；它不以新的诊断投影替换已接受尾的完整 $H$。
3. `closed/surface-actual-tail-readout/`：由这次实际尾的 shooting 状态重新求出的原径向读出，含真实 RK 中点与原 source 背景。
4. `closed/surface-plan.json`、`closed/surface-assembly.json`、若干相位的二进制 PLY 与 normal packet。
5. 顶层 `summary.json`：物理 prefix 读出及 closed 的 prefix/tail/collar 样本联合最大值，以及各执行日志/退出状态。

`--readout-levels` 须按原读出规则整除这次实际尾的 RK steps；当前 `1,2,4` 沿用原真实读出入口，不修改尾的物理参数、RK 状态或接受门。完整径向中间场可重建；不要求将所有大节点包提交入库。

## 两个容易混淆的度量范数

对归一化 Gram 误差

$$
Q=\begin{pmatrix}e&f\\f&d\end{pmatrix},
\qquad e=E-1,\ f=F/a,\ d=G/a^2-1,
$$

新 prefix 读出同时保存

$$
\max(|e|,|f|,|d|),\qquad
\|Q\|_{\rm op}=\frac{|e+d|+\sqrt{(e-d)^2+4f^2}}2.
$$

旧 `geometry_20261114_material_quintic_readout.py` 的 `metric_sample` 是前一分量值，不能改名为后一算子值。原 `exact_20261114_refined_closed_assembly.sampled_geometry` 和 `exact_20261114_material_tail_packet.metric_readout` 已明确计算两者；新入口沿用其正确算子逻辑。整个闭面的汇总分别取所有已检查 prefix、tail、collar 的样本最大值。固定帽和标记的参考度量是它们自己的不随相位改变的诱导度量，不能在标记上误用平帽度量。

这些都是数值读出，未冒充连续外包或新的非线性加密解。仅加密读出点并不能代替 README 第 5 条的同度量求解精化。

## 显示网格预算保留实际 C² 节点

新 planner 将实际 `saved.sol.x` 和全部 scalar breaks 一并放入 prefix rings。它不为省显示体积删除任何物理状态、真实 quintic 接点或 scalar 接点。尾/帽显示请求仍按已有去近重规则避免退化重复圈。

原相位范围为 $\alpha\in[0,\pi/2]$，$P$ 个含端点相位要求

$$
N_{\rm display}\equiv0\pmod{4(P-1)}.
$$

因此九相位时允许 64 或 32，48 不满足原规则；五相位时才允许 48。新入口逐一用实际完整 ring 数计算

$$
V=N_{\rm rings}N_{\rm display}+2,\quad
F=2N_{\rm rings}N_{\rm display},\quad
\text{PLY byte bound}=25V+13F+4096<5{,}000{,}000.
$$

按此式选 64/48/32 显示档，并保存尝试值、选中值、全部真实节点保留断言及字节预算。原默认 `angular=96` 是显示参数，不能因其数值为 96 就当成物理 M96；降低显示档也不降低物理 M112/N2048 或独立材料角读出的 2048/4096 点数。

## 明确仍未声称的事项

本入口不声称新完整场已经存在或已经达到振幅门。真接受后的闭包仍须根据实际读出处理 finite collar、outer correction 的度量缺陷、反射接口、空间/全相位 reach、整面像的 Hausdorff 见证及 $\delta_E$。旧 A 的 q8 覆盖结果不转移到这张新面。同 $g$ 精化要求仍按 README 的等距误差下降判据，不另设所有 C² jet 差都必须达到机器精度的门。
