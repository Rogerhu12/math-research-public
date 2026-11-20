# R141 补篇：完整试算子返回范数的首次实际有向上界

2026-11-20，visible-exact-astra-ac637-20261120。

**本次完成的是一个新完整源范数目标。** 公开运行
[44734581045/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44734581045)
给同一连续修补中心、同一原参考和真实区间上的
$$
 \|\Pi_0 F\mathcal B_c\|_{L^2_r(\mathbb R^{193})\to L^2_r(\mathbb R^{128})}<8828,
 \qquad \mathcal B_c=B_{HL,c}S^{-1}.
 \tag{FBA.1}
$$
这里 $S^{-1}$ 只出现一次，$F=P+Q^*-Q^*\mathcal L_cP$ 是原 WJK 的有限
试算子，$\Pi_0$ 返回 $97\le j\le160$。本次没有把它认作真实无限高频逆
$G_H$，没有计算低 Green 接收器，也没有宣称反馈收缩。

该有限上界较大；它既不是 $\|\Pi_0 F\mathcal B_c\|$ 的下界，也不排除
更小的真实范数或真正 BVP 的可逆性。下一步对真实 $G_H$ 的独立源费用
不需重复本目标。

## 1. 完整定义和精确支持

原[接收器外置合同](R141-supplement-receiver-free-complete-FBc-comparison.md)
的全部定义继续有效。实际计算保持：

- 同一个 degree32 连续修补中心和原实际 $\eta_\delta$；独立 even mean 留在
  193 维输入中，纯中心 mean 到 high 的零仅是该有限支持恒等式。
- 原 153 父片、4650 完整闭行、4801 交集和全部 3594 接口；两个 collar
  切点加入后为 155 比较片。原 $24480$ 细胞、真实根与原 $D,S$ 定义不改。
- $P\mathcal B_c$ 的中间频率至 $224$，完整
  $R_c=(\mathcal L_cP-I)\mathcal B_c$ 至 $288$，返回投影依带宽精确实施。
  实际无限 high 未被截断为这些试函数频率。
- 完整五项 $R_c$ 先消去准确 collar 常项，再形成正核；$Q^*$ 保持真实
  $J^*$ 上端 $R=25/8$，没有把它改成 collar 内积分。

具体比较对象是
$$
 \Pi_0F\mathcal B_c
 =\Pi_0P\mathcal B_c-\Pi_0Q^*\Pi_1R_c.
 \tag{FBA.2}
$$
本次先对 (FBA.2) 的两个完整项使用三角上界，因此没有声称保住两项间的
有符号抵消。原完整 $F$ 的代数定义和所有项均保留。

## 2. 保存的三个完整球

以下逐字复制 actual 的 `new_records`。所有值均是完整正比较的有向
上界记录；它们不声称包围未知算子的准确范数值。

| 新记录 | 保存的 Arb 球 |
|---|---|
| `complete_projected_WJK_FBc_raw_row_ratio_upper` | `[8499.63666658512470493207520456028007099632872386913596675852240209831856724 +/- 8.06e-73]` |
| `complete_projected_WJK_FBc_raw_column_ratio_upper` | `[9167.92028547821487355851135182897504062831356622680611699468771851874448994 +/- 1.57e-72]` |
| `complete_projected_WJK_FBc_raw_norm_upper` | `[8827.45667872576982919739695658398412364986743402050253577761433133137118324 +/- 4.44e-72]` |

数学模块在 $320$ bits 下形成完整 row/column Schur 比较，保存 $75$ 位球，
重新解析并核其包含原 upper，然后按实际保存的字节读回。后继消费者必须
使用这个保存球的 upper，不能将中点替代有向上界。
保存的 norm 球整个小于整数 $8828$，故 (FBA.1) 是严格有理放宽。

若未来获得合同中的低 Green body 返回界 $g_B$，使用 (FBA.1) 的充分门为
$8828g_B<1$；193 个 atom 仍作为独立输出费用支付。这里 $g_B$ 尚未给出，
所以本次不判该门真假。完整 body/atom 反演公式、有限 $\rho$ 连接和两个
实际 RHS 也没有从这一个源范数推出。

## 3. 实际执行和完整身份

触发提交 `72017be969e4c9b3c612f6f74a3ba71c6b9e46a4`；科学实际 checkout
`f74a0d6b5ad3f1ba4cc4555c1ac990a43110a1bd`。Python `3.12.14`、
python-flint `0.9.0`、BLAS threads `1`、320 bits。
实际数学时间 `108.555616977` 秒，child wall `114.212442391` 秒，返回码 0。
一个完整新目标、三个新球；全部 25 门通过，原失败/未付门未被改为成功。

| 完整公开文件 | 字节 | SHA256 |
|---|---:|---|
| [actual](../notes/complete_FBc_raw_ci/run-44734581045-1/actual-scientific-conclusion.json) | 45900 | `97cee455c93771c71c1bd8e4a3c96d682f97255e658d90924c08d1cd4a259193` |
| [execution](../notes/complete_FBc_raw_ci/run-44734581045-1/execution.json) | 52746 | `25f2078a75919a0b9562429b7d76aa9cd0f38f0a2f4b2b06d75a18ac37388145` |
| [report](../notes/complete_FBc_raw_ci/run-44734581045-1/report.md) | 527 | `a99391917fde611a7b87c6f1c9ccc894694f210f57b81a3dc78df4000a4e2841` |
| [首次输入清单](../notes/2026-11-20-complete-FBc-raw-inputs.json) | 60000 | `743c49f915562f304d44518a96fd4d6c35ec542c8ba6ae20a0b812d930e35ef4` |

root 逐件复核 67 当前文件的 bytes/SHA/blob，actual、execution、manifest 的
完整 67 项列表相等；21 历史输入的原 commit/path/blob/bytes 和整恢复对象
一致。完整恢复对象是 15033B、SHA
`8213b004a48508c580440cb7a38239d796c7afc9eece83bbd3f5a02e5b2d7ed4`，
原 $L$ 三量和 centre mean 下界的两个科学/执行完整对象继续原字引用。
四次实际 pull 的两 README 差异均为空，规则读点仍为
`96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`。

没有旧目标重算，没有调用原 50 条小 $K$ 配方、低逆或 atom/endpoint 目标，
没有重新生产旧 native/candidate/repair；新数组、artifacts、Releases 均为零。
实际执行的完整科学模块清单和全部 36 顶层字段保于 actual，不能仅保本页表格
而丢弃原适用域。

## 4. 继续保留的未付义务

这个成功只冻结本完整源上界。R141 的实际低逆、完整 $CFB$、真实全 family、
全部七输入 ports、193 atoms、实际物理 outer 行、两 physical mean、$\Theta$、
$\nu$、原 finite $\rho$ 及两 RHS 继续分别待付。实际 $G_H$ 的源路线有自己的
全频定义和 source 单位，不能用这里的有限 $F$ 替换。

负侧完整径向 head、真正 nonlinear residual、所有 matching 与同一固定度量的
精确闭等距族尚未构造；本次不是本课题完成。
