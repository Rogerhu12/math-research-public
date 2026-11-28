# 严格嵌入低帽支路上的实际位置和固定度量

[R291](../results/R291-embedded-infinite-low-cuff-strong-shape-family.md) 将真实低平领切端、正曲率的逐圈水平截线、固定物理极角处的严格单调高度，与完整强形变帽组成一个显式嵌入族。中央与 [R289](../results/R289-two-strong-shape-ratios-for-the-true-infinite-low-cuff-core.md) 相同，强握持比及允许全部刚体的商形变比分别至少 .203125、.05073291015625。此独立位置族保留全深母线和定义中的水平衰减量，原大幅 XYZ 位置已被替换。目标仍是同一准确低帽母线的旋转度量。R289 的优化误差不能转入此族。

两个物理位置步均用实际六个位置导数和真实非线性 Gram、曲率峰作接受判定。圆周累计弧长由严格正的曲率半径反演。在部分中间状态带步长截断的 Newton 未充分达到数值残差阈值，最终实现对其余角位置用单调区间二分。此次两步计算与所有观察自然结束。初态四个钟系数均为 1，其余为 0。训练目标用实际相对 Gram 算子范数峰加 0.025 倍超过 9.6 的绝对主曲率峰。

| 实际状态或网格 | 相对度量峰 | 最大绝对主曲率 |
|---|---:|---:|
| 训练初态 | 1.0012636021 | 42.36386845 |
| 第一道实际接受 | .9364435697 | 36.91668670 |
| 第二道实际接受 | .8263797547 | 30.42863027 |
| 703 个整核径点 × 120 角 | .8264669363 | 32.01562989 |
| 移位 711 个整核径点 × 149 角 | .8264763004 | 31.93198955 |
| 原生深部全部 17046 行 × 120 移位角 | .5433447182 | 5.79717728 |

最后一行按完整 13 分量 binary64 输入去掉重复，实际求值 10427 个不同记录。两个整核峰均在材料半径坐标约 .954 的外缓接口附近。嵌入与两个比例由连续证明取得，以上峰值是有限网格实际观察；规定的强固定度量精度和定量厚度仍未证实。

用[准确母线生产记录](2026-11-28-2ecf-similar-infinite-tails-and-true-low-wide-cap-physical-states.md)的公开输入和 `S`、`W`，在 NumPy、SciPy、单线程 BLAS 下运行：

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python "$S/2ecf-r291-injective-low-cuff-physical.py" --meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail-table "$W/g12-m2-exact-cuff32-tail.npz" --index 1 --steps 2 --clock 1 --kweight .025 --native --out "$W/r291-low575-convex-rings-full.json"
```

| 源或产物 | SHA-256 |
|---|---|
| `2ecf-r291-injective-low-cuff-physical.py` | `da5dbba6121771a4f2fb3ce11c760ce2ee284893ced545f527025860af36d463` |
| `r291-low575-convex-rings-full.json` | `7a30875385af513fd32fe0b0caed638208cc21e8d9744bbce80170644a2b3d0c` |
