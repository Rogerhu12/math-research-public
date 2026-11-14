# R133 补充：完整 quarter 缓存的中心残差与同向 Hessian 实际验收

## 1. 实际范围和过程

公开 Actions [43628443697](https://github.com/Rogerhu12/math-research-public/actions/runs/43628443697) 的数学子进程返回 0，21 门全部通过，科学计算用时 1059.644887728 秒。它消费此前完整 1977 父格、7908 quarter 的已存 scalar jets；新执行 7844 个中心残差包络，**新的 target 求值为 0**，原物理帽 residual、1341 行 trial 范数和端点数组均未重算。

完整 1341 行全部进入消费者，其中 16 行因原 64 个 pilot quarter 没有保存所需 midpoint 而整行保留原合法界。其余行使用已有 midpoint/whole-third jets。没有将派生 midpoint 冒充原生 point jets，也没有删除 fallback 行。原完整 quarter native 为
`770106a925812df4fc380785ca3e715b2a30a649a355fb888e0dcbe0e6a65298`。

实际输出目录：

`notes/cached_quarter_centre_Hessian_v2_ci/run-43628443697-1-cached-quarter-centre-residual-Hessian-v2/`

| 原件 | SHA256 |
| --- | --- |
| `native/complete-cached-quarter-centre-residual-Hessian.json.gz` | `8d652d2515359e3ad1bf91c8ad03fbf66a646ddf0b6bdef1f0aa20d2adcbf12c` |
| 当前仓库 `process.json` | `c2f962e5d9b4b282b3ee1a33e05749d626e510103064b8252e00ad542e10167a` |
| `evidence/complete-cached-quarter-centre-Hessian-summary.json` | `f68bd0f1b9937bcd7b8296feca054de360ca85d77e5ea466bf4817a6b84e10cc` |

完整 native 为 28,761,355 字节，原字节经 15 个 lossless parts 保存；19,740 字节摘要保留全部验收门和全局输出。后继 Green 真正消费的 artifact process 为 `cd7fdccd2e87f0099b9bde6a82774cc2ddc827ea52b8b06f9664b1514721d5e8`，与上表仓库过程快照分别记录，不能用一个 SHA 代替另一个。

科学源 `fourfold_codazzi_cached_quarter_centre_Hessian_v2.py` SHA256 为 `dfcc4dabe42638ba1ebd2af2b8a51cccd85dfb7f63738bbbae1b6fe38d3f28c7`；worker 为 `b5029d5d69085114cef9219007488f1780e53e9d5ad73f44c3a0d88500ed9d64`，184 件固定输入 manifest 为 `47ff50fc768a24269ea7dab3de284581fdf8be1abd04fb867d4a55be78b1368d`。

## 2. 真正通过的同向上界

同一个已固定输入 $w_0$，完整选定四源为

| 源 | 严格上界 |
| --- | ---: |
| ordinary B | $1.020829564027\,10^{-9}$ |
| ordinary C | $1.066027722582\,10^{-9}$ |
| divergence B | $1.050812166395\,10^{-8}$ |
| divergence C | $9.964838986169\,10^{-9}$ |

四个既成 Green 增益加权后的完整物理源小于 $6.392698482469\,10^{-7}$；再付原 Hessian resolvent，得到

$$
E_H(Tw_0)<6.417342110712\,10^{-7}.
$$

此前 residual-split 的合法上界为 $9.333169144103\,10^{-7}$。原乘数保持
$H<1.003854964897$，故本结论只授权同一 $w_0$ 的
$H\epsilon_{\rm phys}(w_0)+E_H(Tw_0)$；未知输入的完整误差算子范数没有改善。

这里 pointwise 系数界按各子格最大值合并，joint Wiener 界按逐 Fourier 槽最大值加全部余项合并。完整 $|j|\le96$ 支撑、A1 余项因子 385、物理角 composition、独立 even mean、精确 alpha 只乘一次及完整 repair 费用均保留。每个 local 行只在完整四源向量间选择，最终四个全区平方和与对应 Green 增益共同消费；没有逐项拼装不相容分解。

## 3. 规则核查及严格限制

真实过程有七次 pull/README 核查，全部 `changed=false` 且实际 diff 为空；运行中在 18:57:18 UTC 完成定期核查，最终已读提交为
`f52c1b2f1bb4cd1ad3fb136a70282c504ce89d08`。已人工读规则的提交仍为 `ee26c0a65a2e63c15f2ccfba6714181584416542`。

本结果固定物理 $\eta_0$（仿射偏移为 0）、同一 repaired M32 中心及同一 $w_0$。$Z-w_0$ 仍必须乘原完整 moving 误差算子，真实 97 行、独立 mean、已知全高输出及原六个边界费继续保留。它没有证明新的帽算子范数、完整无限维逆、真正 $\nu$ 响应误差或参数 Schur。新数值实际合成另见后继完整 same-$Z$ Green 结果。
