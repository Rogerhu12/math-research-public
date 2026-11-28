# 两个 HF 实际位置场的整环自由对角目标

**有限数值应用。** 对[新正长度真实双钟母场](2026-11-28-2ecf-strong-hf-two-material-clocks-on-new-metric.md)及[同 $g$ 的 75 次真实 Cartesian 联合谱位置](2026-11-28-2ecf-strong-hf-true-XYZ-joint-spectral-solve.md)，从实际两阶物理数据组成各材料角的完整第一基本形式。完整 G10 在每个共同 $x$ 处并入两套全角（128+192）；独立 G11 每个 $x$ 用全部 256 个错移角。按[R274](../results/R274-all-angle-invariant-metric-centre-and-diagonal-reduction.md)放开每个环的两个径向目标特征值及它们之间的全部兼容条件。

先在实际固定 $g$ 的正交标架算 $E,F,G$，这种与 $u$ 无关的对角基变换不改自由对角最优值。令 $a=Ee^{-t},d=Ge^t$。在单项特征值可微点，其 $\log\mu$ 导数是 $(d-a)/\sqrt{(a-d)^2+4F^2}$。每次分别选取最大的 $\mu$ 与 $\mu/(EG-F^2)$，两处斜率相加给凸函数的次梯度，在所有 $\log(E/G)/2$ 的范围内二分 58 次。最终以真实特征值重算 $U,L$ 和半和目标。程序保存每一个有限径点自己的 $t$、最优尺度及最坏环上的上下角。数表为浮点最优化，未把有限样本或浮点测试伪称全域有向证明。

| 真实位置 | 网格 | 冻结原 $g$ metric | 逐环最佳对角 metric 的最大值 | 最坏 $x$ |
|---|---|---:|---:|---:|
| 选中双材料钟的 HF | 双 G10 | .105652510 | .104649306 | .198693227 |
| 同上 | G11 | .108374660 | .105973192 | .190368644 |
| 75 次真实 XYZ 后 | 双 G10 | .087118369 | .086345468 | .191823387 |
| 同上 | G11 | .090945443 | .088467447 | .187360116 |

前一实际场在 G11 的一个内部材料点 $x\simeq.2506432982,u\simeq3.031146037$ 还有单角归一化剪切 .098111543；后一场在 $x\simeq.2809066355,u\simeq6.197282383$ 的单角剪切为 .083585309。即使每一环目标自由浮动，现固定材料识别下的误差仍约 .1；更换实际位置或材料角识别可以改变这些值。表中没有把随径点独立的最优量当作平滑目标，更没有延伸到完备全时闭族。

沿用上引两记录的 hfargs 与实际母场回执：

```bash
python "$SCRIPTS/2ecf-strong-hf-all-angle-free-diagonal-floor.py" "${hfargs[@]}" --diagonal clock-hf-diagonal-d006.json --warp clock-hf-two-material-spectral.json --fields clock-hf-full-joint-spectrum-03.json --output clock-hf-all-angle-r274.json
```

程序仅写两套真实场的逐径对角参数和汇总，没有写出可重生的大位置数组。完整报告 SHA-256 为 `2d5495dd94a7f2af9bc0366443c9c0e9ad689ecd830806f71c76471c912833f3`。
