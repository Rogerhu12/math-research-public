# 完整已知响应在精确连续中心上的实际差源验收

**状态：已证明（完整已知差源及其实际执行）。**

本记录消费公开 Actions [43597921732](https://github.com/Rogerhu12/math-research-public/actions/runs/43597921732) 的实际成功过程。它补齐原完整均值修正准解在原中心到精确连续中心之间的算子差源和参数列差源；它不授予连续逆或真正参数响应误差。

## 1. 不改变的对象和实际过程

原 M32 中心索引的 SHA256 为
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
精确连续中心的定义 SHA256 为
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
本次直接复用原完整 193 态物理响应索引
`ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6`，
以及实际完整主体与两个标量均值证书
`a4f31dccc4b54661b43fc06bac59b6afbb4fa2d6d19614f68f71e044be6e5870`。
记该完整准解为 $q_*=q_{\rm raw}+e_z e_2$。所有原非均值跳跃仍保留。

公开运行使用部署提交
`6b294fc02b1327f0b7024d2e78bb8c5a901f1595`，
新数学子过程退出码为 $0$，实际墙钟时间 $40.001323531$ 秒；
native 自记数学时间为 $36.849375972$ 秒。
全部 $47$ 项身份、维数、原 part 与覆盖检查通过：
原 $40$ 个已成 part 恰覆盖 $7721$ 格、全闭区间 $[0,25/8]$，
没有重算旧残差、均值流、候选重建或目标原函数。

实际证据见[原过程](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/process.json)和
[完整摘要](../notes/response_repair_source_ci/run-43597921732-1-complete-known-response-centre-repair/evidence/complete-known-response-centre-repair-source-summary.json)；压缩 native 保留在同一目录：

| 文件 | SHA256 |
|---|---|
| `native/complete-known-response-centre-repair-source.json.gz` | `05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4` |
| `process.json` | `4bb16cb2c349977243a5e07ce1f9abdae7a9130f403277b68e5b64ffdafd5386` |
| `evidence/complete-known-response-centre-repair-source-summary.json` | `7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec` |

native 中 `actual_completed_common_rows=7680` 是最后一次每 $256$ 格保存的前缀游标；
最终独立字段 `complete_common_rows=7721`、完整行数组与末端覆盖门才是最终覆盖记录。
保留原字节，不把前缀游标改写成另一个过程。

## 2. 实际新费用

所有表中数值均是对实际定向球上端再向外放宽的十进制界。
角测度归一化，完整 pair 范数包含第二分量的独立均值。

| 全 $[0,25/8]$ 新源 | $L^2_r L^2_\phi$ 上界 | 逐点 pair $A^0$ 上界 |
|---|---:|---:|
| $(A_{\rm repaired}-A_{\rm raw})q_*$ | $4.999549\cdot10^{-16}$ | $8.520181\cdot10^{-16}$ |
| $F_{\nu,\rm repaired}-F_{\nu,\rm raw}$ | $1.173787\cdot10^{-16}$ | $4.405121\cdot10^{-16}$ |
| 两项合计的逐格源包络 | $5.597282\cdot10^{-16}$ | $1.131920\cdot10^{-15}$ |

相应地，原完整响应主体残差与新源逐格相加后得到：

$$
\|\mathcal R_{\rm repaired}(q_*)\|_{L^2_rL^2_\phi}
<0.001284069679776281,
$$

$$
\|\mathcal R_{\rm repaired}(q_*)\|_{L^2_rH^{1/3}_\phi}
<0.011057020099385894,
$$

$$
\|\mathcal R_{\rm repaired}(q_*)\|_{L^2_rH^1_\phi}
<0.821013371405893.
$$

每格实际新源、原标量 germ、原候选/响应片号、完整 $M_0,M_1$、
已知 $q_*$ 的 $A^0$ 与角导数界，均在完整 native 行数组中。
因此后续可以保持径向分布消费，而无须先压成全域统一常数。

## 3. 证明接口和范围

新费用遵循
[完整差源合同](../notes/2026-11-14-R133-complete-response-repair-source-contract.md)。
对一般未知 $h$ 保留真正的一阶项

$$
\|(A_{\rm repaired}-A_{\rm raw})h\|_{L^2_\phi}
\le M_1\|\partial_\phi h\|_{L^2_\phi}+M_0\|h\|_{L^2_\phi}.
$$

本次只将该不等式应用于已经保存全部 $193$ 态立方系数的 $q_*$，
没有把主部均值变化当作 $L^2\to L^2$ 有界扰动。
参数列差源包含完整均值项与非局部 $I$；其真实紧支撑外准确为零。
已知差源角支撑至 $n=160$，用于本次已知源的 Sobolev 升阶，
没有赋给未知高模任何有限支撑。

原背景上的标量均值残差准确为零；改变背景后新增的完整均值残差
包含于本次差源包络，**没有继续设置为零**。
本记录仅使用仿射参数偏移 $\eta=0$，即固定物理 $\eta_0$ 与原 $\nu$。

仍需消费内段的全部原非均值跳跃、真正 regular/cap 的切面边界源、
未知高模的反馈，以及完整连续逆。完成这些步骤之前，
不能将以上残差界称为 $\|q_\nu-q_*\|$ 或真正 Schur 非零证书。
