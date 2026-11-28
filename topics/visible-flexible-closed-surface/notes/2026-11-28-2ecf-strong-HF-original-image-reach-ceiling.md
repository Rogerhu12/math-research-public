# 原 H65/HF 全 W 空间像的准确 reach 上限回执

[R279](../results/R279-actual-HF-strong-shape-and-strict-reach-failure-under-clocks.md)复算同时读取 [R272 原全帽场](../results/R272-actual-full-corrected-HF-kernel-and-fixed-cap-strong-shape.md)的实际 HF 字节、原径钟、[新正长度度量](2026-11-28-2ecf-strong-hf-new-diagonal-positive-length.md)及[选中的完整双材料钟](2026-11-28-2ecf-strong-hf-two-material-clocks-on-new-metric.md)。全双钟行列式有理下界的数值展示为 .68245730546，先前径钟的导数下界为 .86477806108。保相位的空间像、开平领与固定帽均相同。

原 HF+W 的有向真实导数给单个内点的径向法曲率下界，其数值展示约 24.08815814413，严格比较使用 $602/25$。有理 reach 上界为 $25/602$，以实际整面 $D\ge14/5$ 归一后的上界为 $125/8428$。只有这个已经严格转移的原空间像受此约束。

```bash
python "$SCRIPTS/2ecf-strong-hf-exact-curvature-and-full-warp.py" --field "$HF/strong-physical-hf64m80-W.json.field.npz" --angular-clock "$HF/strong-hf-physical-radial-clock01.json" --warp clock-hf-two-material-spectral.json --diagonal clock-hf-diagonal-d006.json --x 17/80 --u 11/10 --kappa 602/25 --output clock-hf-input-closed-shape-reach-ceiling.json
```

160 位外包算术使用[前项真实剪切见证](2026-11-28-2ecf-strong-HF-exact-diagonal-shear-floor.md)的相同整数核。旧场本身 SHA-256 为 `eaa0835dc7ea5207f2a93cb0ba9b1d1634f2e00c5cb8964fe954b47601990d86`，母径钟 `3f3ca37fe9ee55a9e20f13cd744c35bb2b6b1f169026bd1ad7897caffe3d25a0`，新双钟 `360c179fc1636776c6a44c5be3f658c427da824405f0b12a63b60092cbdb8fa5`。不含墙钟时间的完整准确回执 SHA-256 为 `b49ebfa9bb45a0cc9350edc700286c920077356ea5da8cd0b9574444e9c7fcae`。
