# 低平领固定度量上的四次稀疏位置更新和原生两阶求值

[R289](../results/R289-two-strong-shape-ratios-for-the-true-infinite-low-cuff-core.md) 的固定度量、真实中央、空间硬约束与两帽保持原定义。将每个实际相对度量矩阵的两个有符号极值方向、真实主曲率峰的物理导数和样条二阶差分约束组成稀疏线性规划。每个提议都重算完整位置与曲率。五次提议得到四次实际接受，其一步线性规划在 45 秒时限内没有返回可用解；该步照实缩小物理信赖半径。四次接受的步长依次为 $1/2,1/4,1/4,1$。移位整核度量峰由 .132142109 降到 .122989024，曲率由 12.155747 降到 11.506422。深部两个峰均上升。

| 实际最终网格 | 相对度量算子峰 | 最大绝对主曲率 |
|---|---:|---:|
| 919 径点 × 192 角 | .122864376 | 11.507720 |
| 移位 911 径点 × 225 角 | .122989024 | 11.506422 |
| 原生深部全部 17046 行 × 120 移位角 | .081075826 | 10.160596 |

整核峰在 $s$ 接近 .017 处。另一次六轮尝试在末次 HiGHS 超时后，观察器误用了观察网格大小作中央支撑的指数，因而中止；已修正闭包，正式五轮自然结束。限时求解的实际接受序列会随机器负载改变。随存的[完整真实最终系数](2026-11-28-2ecf-r289-frozen-minimax-physical-coefficients.json)可独立直接重算上述观察。该状态具 R289 两项强形状比例；其嵌入和规定 reach 尚未取得。

任意材料两阶求值器 `2ecf-r289-physical-query.py` 的 `Field.grid(s,u)` 返回六个向量，依次是位置及 $s,u,ss,su,uu$ 导数。参数 $s$ 可跨中央取负，`phase_grid(s,u,alpha)` 同时处理全相位材料角和空间旋转。`native_grid(n,j,x,u)` 在保留的 $n=0,\ldots,159$ 原生层中按实际 $x$ 重算旋转 primitive，并从本原生段前邻二次模状态局部积分；$s=T$ 另以真圆平端迹赋值。极深原生模的 binary64 下溢和相邻材料坐标相同仍可能出现，端口的连续结论使用原无限源。

承接[实际低帽输入](2026-11-28-2ecf-similar-infinite-tails-and-true-low-wide-cap-physical-states.md)和 [R289 活动核](2026-11-28-2ecf-r289-low-cuff-strong-material-image-and-actual-metric.md)。NumPy、SciPy、单线程 BLAS 的独立最终状态复算命令如下。

```bash
set -eu
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python "$S/2ecf-r289-mapped-physical-minimax-positions.py" --meridian "$W/g12-m2-exact-cuff32-low-double-cut85.json" --buffer "$W/g12-m2-exact-cuff32-cut85-buffer.json" --tail-table "$W/g12-m2-exact-cuff32-tail.npz" --parent "$S/../notes/2026-11-28-2ecf-r289-frozen-minimax-physical-coefficients.json" --steps 0 --out "$W/r289-minimax-independent-check.json"
```

| 入口或状态 | SHA-256 |
|---|---|
| `2ecf-r289-mapped-physical-minimax-positions.py` | `937de9ee532fd9cdff96ace0034261322ea70f6dda0b53d1c4fd360ed9297fc7` |
| `2ecf-r289-physical-query.py` | `aaa32dff0bd75d43bbe4131f3eb21145ca41b5e9ea86f34e828373de662a08ff` |
| 真实最终系数及原观察 | `ebff75489deb8a48927ba0e8da1b673546782cb8bd39e8ab76dd3c8f3f9fa04b` |
