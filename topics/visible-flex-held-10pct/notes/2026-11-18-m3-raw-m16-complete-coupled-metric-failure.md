# raw λ=.02 固定整 g 的 M16 完整联立终态：有限门通过，完整 metric 未通过

2026-11-18，Astra-held10-7322d0de-20261118 / m3_true_coupling。

这次已完成原前缀求解、实际非线性尾、最终完整尾审计及前缀全角审计，进程和 worker 均 exit 0。
它解决了此前单个二进制相邻数导致的有限尾接受平台，但**没有通过课题的完整 metric 门**，不构成同 g 收敛或完成证书。

## 身份与原有限门

运行目录为 `m3_work/beta4625-q040-raw-lam002-fixed-m16-neighbor`；它从已登记的 raw
`λ=.02/M8` 实际联立态升至 M16。完整 `frozen_profile`、材料角 chart、warp reference、
物理尾参数及 cut、圆核设置逐项不变。固定材料轴长度精确保持
`Lbin=1.3603133321372538`，δ=`0.06105141410261685`。

未知支撑 q 可在同 g 的边值问题中调整，本次得到 `q=0.03991248545080898`。
设置为 prefix angular 512 / audit 1024、1143 径向节点、tail quad 256 / parts 16 / steps 16；
tail 的原 `2e-9` 门和所有正性/平方根/域检查未改。

| 检查 | 完整终态 |
|---|---:|
| prefix collocation RMS | `9.98729234675214e-7` |
| 原 outer BC residual | `1.6796869995676767e-8 < 1e-7` |
| 对应物理 nonmean 一阶边界残差 | `3.3593739991353536e-10 < 2e-9` |
| 最终实际 tail residual | `1.3784657706205193e-9 < 2e-9` |
| 最终 shooting min A | `.7427151521096769` |
| 最终 shooting min D | `.9994289564949012` |
| tail sampled actual metric | `6.645140575014973e-11` |
| tail normalized full defect | `1.2817041705188545e-7` |

call 3 在原 Newton 及十次线搜索后触发已登记的 optional 单邻数初值候选：只把内部
`stage=86/component=16` 从 `-644.5647395585236` 改成 `-644.5647395585235`，原完整
Jacobian 路径重算为 `1.3784657706205187e-9` 并接受。最终 call 4 重新计算端口高度后
初始残差为 `2.7569315412410387e-9`；它由原 Newton 自行迭代至上表终值，没有在该调用使用第二次邻数候选。
最终 audit 和 800 个有限 DN Jacobian 数值都已返回。

## 完整 metric 与接缝仍未过门

| 审计量 | M8 已登记态 | 本次 M16 |
|---|---:|---:|
| 全角 prefix metric FFT l1 | `8.30077505696214e-5` | `9.357262954211186e-5` |
| Cartesian Darboux FFT l1 | `.0479319986` | `.2099487199999625` |

本次 prefix 还给出 flow defect `.0006944754508419545`、cut metric FFT l1
`2.458936549945892e-6`。mean 一阶/二阶接缝缺口分别为
`8.516760968690917e-8` / `-1.994479536193694e-6`；nonmean 二阶缺口
`3.3439118749925396e-7`。这些有限采样已经不能支付 `1e-6` 的完整 metric 目标，
不为这个状态继续铺闭图连续盒，也不把有限接受误写成精确 C² 接缝。

同 g 的这一次 M8→M16 没有显示完整 metric 改善。它不证明所有更高维精化不可能，
但不给出盲目继续 M24 的依据。后续按新设计分支处理明确的 `λ=1` 圆弧入口，
先以本次完整实际十五个控制系数支付原 rho 门和全控制预算；不继续把 λ 的名义增加当成趋圆证据。

## 可重放记录

[raw_m16_complete_coupled_record.json](../scripts/resume_m3/raw_m16_complete_coupled_record.json)
包含实际命令、全部输入/输出及源 SHA-256、物理参数、十五个控制系数、原门、worker exit 和逐项同 g 身份检查。
完整数组仅留在 scratch：

- `seed.json.gz`：`6f5a973c746e1112f827e5478432b9abe9d14931df90157f2a19381cc670b91e`；
- 配套 `seed_coeff_00.npy.gz`：`6637680be24885749acace4d688299ade99249c0760558bf5dc7c42186202f22`；
- 最终 `seed_tail_0004.json.gz`：`220fab12b9d25daa0f23c91f00945321b9c447813b3120281aa00d2793dd1910`。

前缀 metadata 和 coefficient chunk 共同组成可恢复的完整 checkpoint，不能只复制前者。
