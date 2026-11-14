# R133：最终 ac1 物理 regular 端口的实际恢复

2026-11-14，完整最终候选恢复后，原端口程序实际正常返回 0，用时 0.702011 秒。全部 13 个明确门通过，原证明 [最终 moving 候选的完整物理 regular 端口](../results/R133-supplement-final-moving-centre-actual-regular-boundary.md) 的范围不变。

## 实际对象与完整计算

- 完整候选索引：`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，五个数据分片已逐字恢复。
- 原程序：`scripts/fourfold_codazzi_moving_actual_R_boundary.py`，SHA256 `aa98cdd2289b13ac125a0bdb193faa9ae389b566d9a561c0b0e93208d29937f1`。
- 新完成报告：[2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz](2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz)，SHA256 `bb2767633225f19f27c6c2646ac47c1142352a3a03882c916868e079f0fb055a`，84,003 字节。

本次准确消费最终片的全部 dyadic 端值，以 320-bit Arb、512 个完整周期节点计算 128 个正物理 Fourier 矩。全非线性角图、严格解析 alias、所有未保留物理频率、真实 regular 乘子误差、原参数半宽 \(10^{-9}\) 和全部 intrinsic primitive 尾均保留。没有假设有限梯形公式准确积分全角函数。

原生有向结果仍给下列严格外舍上界：

| 完整端口量 | 上界 |
|---|---:|
| \(\|(C-C_{\rm ref})_\perp\|_{A^0}\) | \(2.532986\times10^{-13}\) |
| \(\|B_\perp\|_{A^0}\) | \(2.532804\times10^{-13}\) |
| 完整真实线性 Robin | \(1.256750\times10^{-15}\) |
| 有限 BVP 的 \(j>32\) 真 Robin 全尾 | \(6.662282\times10^{-21}\) |
| 原先规定小球中的完整 nonlinear Robin 残差 | \(1.258388\times10^{-15}\) |
| 同一小球中的完整物理 \(C\) mean 残差 | \(2.048004\times10^{-19}\) |

\(B\) mean 由真实反射对称准确为零；独立 mean 高度和 far Dirichlet 数据没有被消去。小球半径在运行前固定，程序没有按结果反复选择半径。

## 重放命令与权限

```sh
PYTHONPATH=/workspace/scratch/ac0d699811ad/runtime-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python3 scripts/fourfold_codazzi_moving_actual_R_boundary.py \
  --candidate /workspace/scratch/ac0d699811ad/replay-final-20261114/stage06/moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json \
  --native notes/2026-11-14-R133-moving0765-actual-R-boundary-restored-native.json.gz \
  --progress
```

下一次重放须使用尚不存在的新输出路径。新报告含新实际路径和运行时间，不声称其容器字节等于失联前报告；候选科学数组和数学程序的身份已准确恢复。

这给出可消费的完整非零端口残差及真实长段入球。主体的完整 BVP 逆、参数 Schur 非零、far regular label 方程和闭面存在性仍须独立闭合。
