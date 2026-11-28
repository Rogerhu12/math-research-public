# AWSS：同一 selected member 的两列整域有符号体源已实际完成

公开 [run 46136409179/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46136409179) 的 job `140952590682` 于 2026-11-28 11:05:10 UTC 成功结束。事件为 `5949465f4b0bf038142986183632ba06fca00a01`，真实 science checkout 为 `612cebd64b2e06da4a3486345c8c7b0691988363`。原 [WSS](R149-supplement-whole-signed-selected-both-ordinary-sources.md) 的两个目标全部 complete/proved，返回码为零；这是整件 source 结果，不是 PDE 解。

## 完整原对象与实际回执

保持原 $Q_\delta=Q_c+\delta Z$、同一隐式 $\delta_*$ 与整原实参数窗、固定 $\eta_0$、真 compact metric、全部原 Fourier 行及 independent even mean。两列严格为 `ordinary_Newton_minus_f_delta` 和 `ordinary_nu_proposal_defect_s_delta`。完整区间是 $[0,25/8]$，原 7721 个 intrinsic 行及 6144 个三次片的全部接缝，连同真 compact 导数和不确定根的两侧，形成 7728 个闭物理分片。其完整 partition 编码 645044 B，SHA256 `1d5b40e32b82f1db5e82a6a66c15b7dc9eb4f43a335c61e7ff27a5101300711f`。

每片都保原 577×2 的有符号实物理坐标，包括每列的原均值行。全部私有 source 文件共 145219356 B，61 个原始完整 chunk；完整 index SHA256 为 `429fe4b919ddfa47108b84c4651c8493a808a0b6ba33d65be7a7646e6cb2e090`。只有原小结论和身份公开，没有发布大数组。

| 完整对象 | bytes | SHA256 |
|---|---:|---|
| [actual](../notes/whole_selected_signed_sources_ci/run-46136409179-1/whole-selected-signed-source.json) | 15263 | `d3135d3cf9855b2312a922c9bfd9162da3debd844855eea22668ba0d8318b16e` |
| [execution](../notes/whole_selected_signed_sources_ci/run-46136409179-1/execution.json) | 24536 | `fb1e7e7a828cc8a8086ecd9eb50d96bc895b194a58017271aad210cf986a563a` |
| [manifest](../notes/2026-11-28-whole-selected-signed-sources-inputs.json) | 7995 | `dc6422b48e17064f7493510aa289a6cc9111887c95d7cb38093241663b5c4bb9` |

root 独立从完整实际日志 ZIP 134831 B / `fce994f97d30a295cf55dcfc65c6060f4040dd4fd1abd482902c790f0e306faa` 恢复上述最后两个 complete 文件，逐字节与仓库版本相同。日志早先的 13262 B / `bee0b6d5…` actual 与 24915 B / `280d7d59…` execution 是未完成前缀，没有被误当成最终结果。实际 API、whole metadata admission 及以上区别见 [root 完整准入](../notes/whole_selected_signed_sources_ci/run-46136409179-1/root-complete-admission.json)。

## 整域有符号内积及接收资格

第二目标还完整积分了两列的 signed inner product：完整 $[0,25/8]$ 用 7728 片，固定负围窗 $[0,2383968743003/10000000000000]$ 用 3073 片，正围窗 $[1191984371497/5000000000000,25/8]$ 用 4656 片。两个围窗在不确定根附近相交，不能把片数相加当成互不相交的分割。所有中心、半径与十进制指数完整保在原 actual 的三个 `signed_inner_product` 对象中，未丢弃符号或半径，也未把这些球解读成已确定正负的相关性。

原实际 scientific wall 为 1243.6728537469999 秒，aggregate RSS 峰值 1752854528 B，native 与 private 合计峰值 325857280 B；四个单线程 worker、全部原 CPU 与 directed backend 身份门通过。科学没有重算原 TC norm 或原已成功 target。

root 再以原 owner validator 和新 SRR terminal 接收合同读取 complete/proved、两个目标、原运行与 checkout、全部来源和每个原 chunk。随后逐字节核完原 19 个新 current 及 TCXV 全 184 个 current 文件的 bytes/SHA/Git blob 和 Python AST，核原 32 个历史完整 descriptor 与实际已完成 preflight 身份。这个接收过程没有导入 NumPy/Flint，没有重建 145 MB 私有数组，也没有运行新的数值目标。

该实际载体现在供 [SAR 的两列有符号解](R149-supplement-signed-selected-affine-columns-and-true-high-return-at-the-cut.md) 消费。使用前还须取得同一个 GG 全部两个 actual 目标，并将旧 source 的每个 chunk 和整个 index 逐字节恢复；原 signed 解、全部 193 个自由边值、正侧反馈、两均值、height、waist 和 world 方程继续保留。这里没有授予 full response、非线性解或最终闭曲面族的成功。
