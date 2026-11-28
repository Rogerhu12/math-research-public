# 准确低平领活动核、完整固定宽帽及强形变图像

[R289](../results/R289-two-strong-shape-ratios-for-the-true-infinite-low-cuff-core.md) 在准确 $8/25$ 的无穷振荡 cuff 和 R215 高度窗内，给出一张整闭材料图像，完整固定帽和核共同实现两项强形变比。活动核的输入为[两折返低帽母线和实际 $p=32$ 中央](2026-11-28-2ecf-similar-infinite-tails-and-true-low-wide-cap-physical-states.md)；完整全角核被严格限于相位零的板 $|y|<915/1024$，所有相位的球半径小于 $1637/1024$。实际 cuff 高在 $[.5630563953,.5969432841]$，中央长轴支撑大于 1.450477，固定帽及两个三维握持排球均用到完整像的结论中。

实际位置层先在64段每坐标10奇偶通道的较软板约束状态上，试用一套只含轴限幅、球限幅的空间变换（轴参数 .78/.114、球参数 1.596/.003）。试算现场的球限幅在训练位置恒等。此第一版的独立整核误差 .15955479、曲率另由实际二阶导数给出。正式 R289 改用两套准确 dyadic 轴/球参数，同时加真实双三维排球。数值实现把几何有理数作为 binary64 近似求值。包含径向二阶链的完整场经 14 次实际位置接受，训练初态峰 .1595468511；两个独立整核组峰分别为 .132195835、.132142109，最大绝对主曲率分别 12.156136、12.155747。末组 935×225 上的核球半径 1.452987575、y 绝对值峰 .893554482。另 17046 个原生径点 × 120 移位角的深部真实峰为 .031623503、曲率 9.832274。这些结果保持同一个低帽目标 $g$；常规曲率峰约 12.16，当前误差远大于原基础容差，非局部 reach 与整闭嵌入仍待支付。

径向映射 $P\mapsto c+a(|P-c|)(P-c)$ 直接传递所有物理位置、切向、二阶导。原始空间更新对全部三层空间映射反向应用一、二、三阶链式公式，再由真实非线性峰作步长判定。最后两次径向推开的位置只在指定的三维球内改变；实际帽与中央、cuff 邻域均保持恒等。一次真实优化回退、原生深部漏峰和最终闭像的未付指标均不作为成功的形状/度量输入。

采用[低帽母线再生命令](2026-11-28-2ecf-similar-infinite-tails-and-true-low-wide-cap-physical-states.md)中的 `S`、`W`、原 manifest 与已有完整空间状态。NumPy、SciPy 和单线程 BLAS：

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
manifest="$S/../notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json"
b=(--meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail-table "$W/g12-m2-exact-cuff32-tail.npz")
a=(--index 1 --epsilon .34 --guide 9.4 --stadium-p 32 --stadium-mix 1 --vertical-scale .25 --horizontal-scale .75)
python "$S/2ecf-r289-full-core-slab-ball-solver.py" "${b[@]}" "${a[@]}" --parent "$W/g12-m2-true32-low575-stadium-slab64.json" --out "$W/r289-low575-eps034-physical64.json" --steps 28 --mu .055 --train-radial 252 --train-angular 112
python "$S/2ecf-r289-true-cuff-closed-image-maps.py" "${b[@]}" "${a[@]}" --parent "$W/r289-low575-eps034-physical64.json" --out "$W/r289-low575-holes-eps034-xyz64.json" --steps 26 --mu .045 --train-radial 250 --train-angular 112
python "$S/2ecf-r262-m2-exact-cuff-physical-central-budgets.py" --meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail "$W/g12-m2-exact-cuff32-tail.json" --manifest "$manifest" --state "$W/r289-low575-holes-eps034-xyz64.json" --out "$W/r289-true-cuff-low575-final-budgets.json"
```

| 源码或产物 | SHA-256 |
|---|---|
| `2ecf-r262-m2-exact-cuff-physical-central-budgets.py` | `cbb5bb9387cb510c975effb39a217dc4d041ef27813528620e91c0bdc86f5643` |
| `2ecf-r289-full-core-slab-ball-solver.py` | `85095230b83ff04c7dd5bd45fbd500e3e28645a6411122c1d7130603be3fddbf` |
| `2ecf-r289-slab-ball-full-chain.py` | `8b07660b17c5fce618cf8987a631b2bcf22b03bc652fe8542bed22bfe4bdd5df` |
| `2ecf-r289-true-cuff-closed-image-maps.py` | `50be9aae3e5a895ee7e81123c3eb4d31fe71fb477a9d93467916aacb5a8384e4` |
| `r289-low575-eps034-physical64.json` | `1435953c6ad0b1a5f9416ce60701b28e6d1089833da75ca0f132a50b41c2d05a` |
| `r289-low575-holes-eps034-xyz64.json` | `3f3efc048062c222bb26ac5c0e2f71e4aa78d0e475bf04e3c5a38225417928e7` |
| `r289-true-cuff-low575-final-budgets.json` | `e6e2ea0ae4b77fd18e54e326c498c56b95fa90c6f7167427731de12b8d91a5f9` |
