# λ=1 / bp=.32 / bc=.4 首次实际联立终态：前缀未过门，尾诊断通过

2026-11-18，Astra-held10-7322d0de-20261118 / m3_true_coupling。

已经完成此前登记的明确新圆弧设计入口。原进程和 worker 均 exit 0，但 prefix
`solver_success=false`；**没有获得新的 λ=1 accepted coupled state**。
原程序随后对该失败态完成了实际尾和全前缀审计，因而下列结果来自完整终态，不是被中断的猜测。

| 项目 | 实际结果 |
|---|---:|
| q / λ / a / bp / bc | `.03991248545080898 / 1 / .21 / .32 / .4` |
| 求解后的 δ | `.061051825418417784` |
| 原前缀节点数 | `3729` |
| 前缀退出原因 | 下一次所需加密超过 `max_nodes=6000` |
| 最大 collocation RMS | `12.954327511719086` |
| 域拒绝 / merit 拒绝 | `86 / 45` |
| 接受步数 / 无步次数 | `5 / 3` |
| 最小 line-search α | `1.9073486328125e-6` |
| 全角 prefix metric FFT l1 | `.4218800439824124` |
| Cartesian Darboux FFT l1 | `10093.34207380097` |
| 最终实际 tail residual | `1.0868685260037325e-9 < 2e-9` |
| 最终 tail sampled metric | `8.960222236657173e-11` |

实际尾初始化先从 `1.3591317379969402e-7` 经原 Newton 到 `1.3784657706205187e-9`，
之后前缀内解失败。失败态的真实尾诊断 call3 从 `145.66806248648513` 降至上表最终残差；
最终 call4 的 Jacobian 和完整 audit 也返回。有限尾通过不能挽救前缀失败，更不能替代全 metric。

失败态仍有正的完整核心数值审计：rho 样本最小值 `.6336446837662876`，
原保守下界 `.23486838000663285`。但 raw 坐标已显著变化：例如 c6 由初始约 `.0002112835`
变为 `.05696000857`，c9 变为 `-.04967115893`，后续控制呈大幅交替。
完整十五 c 记录在附带 JSON；不能只看某一个 raw 系数把完整曲线当成同等幅度的变化。
这项现象支持进一步检查实际线性化及参数表示，尚不能证明失败单由条件数造成。

本次同时跨过 λ=.02→1 和主/控制宽度变化。原 m3 initializer 只回拉旧有限材料修正，
再用 Tu/2 内的短 cubic 修补入口值；新 exact integral reference lift 已改变。
已有 n4 入口使用旧完整表示到新参考的全角投影，并以与 exact lift 相同的
`a(s)χ(s)`、`(.5,.9)*prefix_end` C² 窗修补入口。
接下来先对这些初猜进行独立只读的 domain、边界、径向 jets 和实际残差比较，
并按 R42 检查实际保存态 Jacobian 的可逆块预条件；不改变本次运行来源，也不把 L² Gram 当作 BVP Jacobian 的代理。

初始 q/δ 和失败后的 q/δ 均在 R40 局部窗内，但这一必要设计检查没有保证 BVP 成功。
本次不证明所有 λ=1 初猜失败，也不证明圆弧核心不存在。

## 复算与完整记录

[raw_circle_endpoint_first_failure_record.json](../scripts/resume_m3/raw_circle_endpoint_first_failure_record.json)
保存实际命令、全部来源/输出 SHA、参数、所有物理控制、失败统计和尾审计。
目录为 `m3_work/beta4625-q039912-raw-lam1-b032-w040-m16`；metadata
`seed.json.gz` 的 SHA 是 `32abed1ae7e1ae98a23fcb5f171a6a7d38c88530af48dfa8da552a2f31dcf017`，
它的完整失败场另有三个 `seed_coeff_*.npy.gz` 分块。最终 tail4 SHA 是
`8b6df5d05f4c150d24ce4c40b95256c375372d307df0b4588cc13a91c41e6ce8`。
数据不提交仓库；生产 accepted loader 应继续拒绝该 `solver_success=false` 状态。
