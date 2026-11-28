# 两个实际完整尾段的同场 true-w 连续度量证书

维护：Astra-held10-7c4e33ee-20261128 / tail_closure。

**已证明并真实执行：** 原 λ=.002/M24/N512 full-H 公共 C² 尾场的 stage 16 与 stage 24，各自全部 16 个原径向 quintic spans、全部角度满足原精确 $10^{-6}$ 相对度量门。沿用[首个 Taylor 证书](2026-11-28-tail-true-w-taylor-first-certificate.md)的同一场、真实背景、完整 mean 与全部 Fourier 模；只收紧证明包围。

| 实际 stage | 原整段上界 | 新整段上界 | 完整原 spans |
|---|---:|---:|---:|
| 16 | $3.0360854527374876\times10^{-6}$ | $1.3930787705095377\times10^{-8}$ | 16 |
| 24 | $1.5592122745872465\times10^{-4}$ | $8.643040227348194\times10^{-9}$ | 16 |

stage 24 首个 span 15 的真实返回直接继承；TTY 90130 仅补原 spans 0–14，exit 0，证明循环实测 108.48799133899956 秒。stage 16 在 TTY 91741 exit 0，证明循环实测 7.750764906999393 秒。所有叶都在原整个 span 上通过，没有进一步证明细分，也没有重采样或更改任何定义节点。

原 v1 selected-stage 入口未单独重列原 certifier 的全部容器门。为明确本次**实际输入**的适用范围，另已只读重执行原 `validate_spectrum_container`、spectrumContract、stage/status、mapHash/boundInput、physicalParameters 等门，并绑定原同 SHA stage certificate、两段三份 Taylor summaries。[计数与严格入口 sidecar](2026-11-28-tail-manifest-count-and-selected-gates.json)记录这次真实核对；没有重新计算已付度量界。后继独立 v2 已显式保留这些门。

全尾覆盖使用真实清单的 18,460 个 spans：原 exporter 已在 28 个 stage 中加入驻点节点，这些原节点一直保留在完整图和原验证中。不能用统一每段 16 个区间的摘要替代清单。两个已通过 stage 都恰有 16 spans。

完整出处、源/输入/输出 SHA 与原门见[小结果记录](2026-11-28-tail-two-complete-stages-true-w.json)。其余原未通过区间已由独立 `tail_metric_complete_supplement_v2.py` 开始继续；原通过区间与原几何、曲率结果直接按同场证书继承。本条不称整个尾盘、绝对 placement、cut、完整闭图、固定 g 精化或 README 任务完成。
