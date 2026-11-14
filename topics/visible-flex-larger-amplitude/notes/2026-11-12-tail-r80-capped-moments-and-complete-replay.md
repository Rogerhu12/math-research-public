# R80 实际 capped 五真矩与同候选完整重放

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

完整证明在 [R80](../results/R80-capped-source-positive-moment-refinement.md)。本包保持原 cell 0 / 段 1 的真实 capped source、全 warp、共享物理两 jet、20 个保存高度模和同一个 R48 候选。更紧的是积分与候选的外包围，不是另选积分区间中点作为新候选。

## 正式执行

| 项目 | 正式 session | tool / wait4 | 时间 | 实测峰 RSS |
|---|---:|---|---:|---:|
| 原 292 叶 capped 五真矩 | 69328 | 0 / 0 | 5.8445 s | 31776 KiB |
| 同候选全均值、真实导数、完整 J/R77 | 88305 | 0 / 0 | 10.1787 s | 32476 KiB |
| 完整九段精确有理数合成 | 28404 | 0 / 0 | 1.3795 s | 12896 KiB |

第一项的 4022 个 Taylor 子片保留每个实际 cap 分支及实际导数符号；35 个未决窄条带用完整可能分支并集和已证非负积分上界覆盖。所有准确有理端点依次拼成原 292 叶及整个 $[0,1]$。原 material 的全胞元归一坐标矩没有被误作局部段坐标矩；每个新积分均与冻结 `local_moments` 的同一旧正测度求交。

原 $I_b$ 区间是 $[0.0003009731443819706,0.0003762278176020860]$ 的更精确 dyadic 版本，相对半宽约 $0.111126$。新确切端点在 summary 中，其显示外包围为

$$
I_b\in[0.0003369416041344706911\ \pm 7.85\times10^{-23}].
$$

实际 dyadic 端点的相对半宽小于 $8.99\times10^{-20}$。对应的 $\lambda_2$ 同候选区间收紧到

$$
[-0.001388924999618096952357,
 -0.001388924999618096951169],
$$

以上十进制端点向外保留；正式计算始终用保存的 dyadic 端点。旧 $\lambda_2$ 相对半宽约 $0.284975$，新相对半宽小于 $4.277\times10^{-19}$。

重放先精确重现旧矩和旧 bubble 包围，才应用新真积分交集。它保留每个原叶原来的几何区间，重新计算候选自己的 $\bar K_x$ 和高度积分，以及完整隐式均值与其真实径向导数。没有用 PDE 二阶值替代候选导数，没有角采样截掉 $J$ 的带外项。

段 1 的完整物理 $J$ 上界小于 $0.014343673847353$；R77 后小于 $0.014343673795$，原已付上界为 $0.036032146505$。保留高度频带内非均值部分小于 $0.014343195687$，高度带外部分小于 $1.223\times10^{-22}$。这两个分项不意味着实际残差等于上界；它们只是完整同叶区间账本中的分解。

## 同候选的九段合成

| 原 source 段 | 连续叶数 | 物理 Darboux 缺陷上界（向上十进制） |
|---:|---:|---:|
| 0 | 1 | 0.012029528665 |
| 1 | 292 | 0.014343673795 |
| 2 | 16 | 0.002508797131 |
| 3 | 4211 | 0.000187163764 |
| 4 | 16 | 0.000594020090 |
| 5 | 1255 | 0.005646192561 |
| 6 | 16 | 0.029950028329 |
| 7 | 1740 | 0.007105295836 |
| 8 | 16 | 0.026296746763 |

合计仍为 7563 叶，全候选最大段为 6。合成器不会把更紧的积分区间称为与旧区间逐位相等；它明确核对 R80 的同真积分定义、原端点、正式资源及新旧 source 身份。每个新叶的完整频率、正门与准确有理覆盖均重新扫描。原完整均值高度界仍有效，因为数学候选相同。

这些结果没有支付真实外径向解的存在性或外侧 Green/Schur 逆。下一实际候选范围是段 6；外侧有源逆、参数修正与真实内头的接合仍与 exact 分支并行推进。

## 复算入口与完整证据

先在课题目录、单线程环境下执行真矩，再执行同候选重放，最后执行标准库合成。完整 argv 和输入/源码 SHA 已在下列计划与资源中保存，不能用说明文字重造数值输出：

- [真矩计划](2026-11-12-tail-r80-cell0-seg1-capped-moments-r1-plan.json)、[资源](2026-11-12-tail-r80-cell0-seg1-capped-moments-r1-resource.json)、[summary](2026-11-12-tail-r80-cell0-seg1-capped-moments-r1-summary.json)、[全部真积分原叶流](2026-11-12-tail-r80-cell0-seg1-capped-moments-r1-integrals.jsonl.gz)。
- [重放计划](2026-11-12-tail-r80-cell0-seg1-refined-moments-fullJ-r1-plan.json)、[资源](2026-11-12-tail-r80-cell0-seg1-refined-moments-fullJ-r1-resource.json)、[summary](2026-11-12-tail-r80-cell0-seg1-refined-moments-fullJ-r1.json)、[全部有符号 J 与实际高度 jet 原叶流](2026-11-12-tail-r80-cell0-seg1-refined-moments-fullJ-r1-segment1.jsonl.gz)。
- [九段合成](2026-11-12-tail-outer-cell0-components-R80-r1.json)与[资源及完整命令](2026-11-12-tail-outer-cell0-components-R80-r1-resource.json)。

三个独立入口是 [真实 capped 正矩](../computations/tail_outer_capped_true_moments.py)、[同候选重放](../computations/tail_outer_capped_moment_replay.py)、[完整叶合成](../computations/tail_outer_combine_refined_moments.py)。原始粗矩、旧 source 和全部旧审计继续保留。已完成 recovery 文件只是同一已存 primary 的冗余副本，不列入稳定发布清单。

两个计划所记 R80 证明 SHA 对应执行前的完整条件正文，现已按原字节保存为[执行前证明快照](2026-11-12-tail-r80-preexecution-proof-snapshot.md)，SHA 为 `84c385c30c2216527ea5daaef740aee70765139fb1505b6b53d55b17e391e11f`。正式 R80 只在其后追加第 6 节实际结果；所有已执行 Python 源和数学 primary 均未修改。这个版本差异属于文档补充，计划与资源仍保留当时真实记录。
