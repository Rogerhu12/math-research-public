# post43 旧连续 metric 结果的范围更正与 R246

原 26 件历史文件保持原字节，恢复清单见
`2026-11-14-geometry-post43-recovery-manifest.json`。其中旧 handoff 用
“连续 metric 误差 <1e-6”概括的结果，准确含义由旧报告自己的公式确定：
三个归一化 Gram 分量各严格小于 `1e-6`。不能直接将这个概括当作
`relative_metric_operator <1e-6`。

[R246](../results/R246-finite-prefix-continuous-component-metric-bound.md)
现已给出完整有限对象、Bernstein/区间 FFT/全角 Taylor 的证明、旧实际
415 片执行证据与散列，并明确直接谱算子结论只有 `<2e-6`。连续浸入则
确实成立，归一化 Gram 行列式严格大于 `1-2e-6`。

执行出处仍是旧工作区在 2026-11-14 09:29 UTC 完成的本地历史，wall
`1080.2680027490023 s`；后继只读核对和论证整理不是一次新的公开
Actions 计算。本次没有重算、没有覆盖历史字节、没有恢复旧 fixed32
求解。公开复现命令与新 scalar 适配边界已单独保存在
`2026-11-14-public-metric-interval-replay-interface.md`。

当前 `.9975` 和未来完整 fullDN 不能承接旧 `.984` 的已付结论，R241
使用的 `1e-6` 算子封套也没有因此得到支付。新候选上的完整 metric 门
将绑定其自身的实际场和同一个冻结完整 scalar 公式。
