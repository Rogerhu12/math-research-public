# E89 原 degree178 来源及第五读者的实际公开执行

日期：2026-11-26；会话 Astra-rank2-Sha-7d29daa5-20261126。

## 1. 完整 CM 共同核

脚本 `scripts/check-r943-degree178-full-cm-source.py`，参数 `--workers=4`，python-flint 0.9.0；run [45764784007](https://github.com/Rogerhu12/math-research-public/actions/runs/45764784007)，job 139722963336，来源 `ab5d8cefd5ccfc294ebf85408e539a4565b3362f`，实际 success。

在原 norm7、norm13 运算和完整30维来源中，共同零质量核维数为1；所选规范向量的原首项阶为6。两个运算完整交换，共同稳定闭包的秩29保持为29。此处读取的是全部来源，不是两个特征值推测全局角色。

| 记录 | SHA-256 |
|---|---|
| 脚本 | `b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67` |
| 原完整矩阵 | `6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665` |
| stdout，2915 bytes | `bf8fb4b3536157c8ec802ee81050c9f40bbc81edbe483fda972836e44fa5b2e0` |
| 工具返回完整日志，UTF-8 保留 BOM，16132 bytes | `77459e236b632c74b6f3c6f821052692c259b0dad4bcc18a5a84089b6f5fa06e` |

## 2. 第五低轴、实际角帽和有限89范数

脚本 `scripts/check-r943-original-degree178-fifth-axis.py`，参数为空，python-flint 0.9.0；run [45766655437](https://github.com/Rogerhu12/math-research-public/actions/runs/45766655437)，job 139729057126，来源 `2063772449e2208962076fd740b714a7b2ad2bb8`，2026-11-26 06:13:33 UTC 实际 success。

本脚本在同一次 run 重生第1节的完整30维来源和矩阵，只在内存读取系数，不用已生成系数表作为输入。完整旧四轴锚点与新五轴返回均通过。按列 $w^5,\ldots,w$ 的五轴行列式为

$$
\det B_5=-\frac{104568614585465172496900768457847209984}
 {46188380197265625}\ne0.
$$

有限89处实际 $\tau(g)=g^{60}$ 的投影给 $C=5$，原常数 $\sqrt{89}-5$ 和范数平方 $45(89-5\sqrt{89})$ 非零。

实际新来源 $W_{178}$ **不属于**旧 $B_{89}$：原角因子在 $t=0$ 仅一重，旧归一化要求两重，且角次数29超过28。实际有 $S_{34}W_{178}\in B_{106}$，旧导子返回权为11086；这些是有成本的乘法关系，不能传播指定中央零。原 $S_{34}$ 也确实整除 $W_{178}$，商的 $X$ 次数24，同样不把两条中央条件合并。

| 记录 | SHA-256 |
|---|---|
| 第五读者脚本 | `c4226727954c4f5fc8477bb17987a49242ef73103049ff7de8e004d442698ec6` |
| stdout，1996 bytes | `48a39280ed06fd2e8579da8df6815287c68cfdd59b294d6e396ce83474f0e949` |
| 工具返回完整日志，UTF-8 保留 BOM，15034 bytes | `22cb81d7e811e3cc1d71dcdec8af241ac96de4b5fef7639511855675ae6b5137` |

## 3. 已付范围

以上只登记实际完整来源、低轴线性独立和局部投影。完整 E89 Schwartz、全局角色、周期、通常全 Selmer 桥及五轴后的真实原窗口已由 [R943](../results/R943-original-e89-fifth-central-full-selmer-and-five-axis-gate.md) 逐项证明。当前未由计算得到原深核、全局底非零、ordinary 或无穷素数结论。全部可重算输出和系数不入库。
