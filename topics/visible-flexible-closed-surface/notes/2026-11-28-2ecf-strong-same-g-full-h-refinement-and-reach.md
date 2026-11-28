# 强前缀同 g 两次物理 h 与整环带 reach 的实际记录

[R261](../results/R261-strong-same-metric-physical-refinement-and-complete-prefix-reach.md) 证明三个同定义、同 g 的原生位置图在整前缀上实际变好。H33、H65 均有自己的连续 Gram 与自身曲率证书，H65 全域严格小于 $2\times10^{-9}$。原归一化图的 R258 见证与三个原生图的见证各自使用自己的位置定义。

## 原件与运行

先依 [物理 h 生成记录](2026-11-28-2ecf-strong-same-g-genuine-physical-h-position-fields.md) 产生 H33/H65 master 和 `report.json`。令 `SCRIPTS` 为公开课题 scripts，`DATA` 为旧两个 master 所在目录，`FINE` 为新物理数据目录，`OUT` 为新的可写目录。

```bash
set -eu
mkdir -p "$OUT"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
old="$DATA/gap105-prefix-ramp-master.npz"
coast="$DATA/gap105-prefix-coast-master.npz"
for n in 33 65; do
  python "$SCRIPTS/2ecf-strong-ramp-refined-continuous.py" \
    --scripts "$SCRIPTS" --old "$old" --coast "$coast" --refinement "$FINE/report.json" \
    --nodes "$n" --out "$OUT/strong-physical-h${n}-raw-continuous.json"
done
python "$SCRIPTS/2ecf-strong-ramp-h-radial-witnesses.py" --old "$old" \
  --refinement "$FINE/report.json" --out "$OUT/strong-physical-h-radial-witnesses.json"
python "$SCRIPTS/2ecf-strong-ramp-refinement-composition.py" \
  --h33 "$OUT/strong-physical-h33-raw-continuous.json" --h65 "$OUT/strong-physical-h65-raw-continuous.json" \
  --witness "$OUT/strong-physical-h-radial-witnesses.json" --old "$old" --coast "$coast" \
  --results "$SCRIPTS/../results" --out "$OUT/strong-physical-h-whole-prefix.json"
```

此次 H33（30611）、H65（21359）、三层真实点下界（8103）和最终合成均实际自然返回 0。两次完整根证明分别运行 286.981736、597.053157 秒。可重生 JSON 记录本机实际耗时，重生核数学行、域和绑定内容。逐物理格的小回执只在计算盘；每个总报告绑定全部小回执的 SHA。

| 原件 | SHA-256 |
|---|---|
| `2ecf-strong-ramp-refined-continuous.py` | `11c50f40a9206aba0a3679d59ac3d5dfc3c9eb65a281ed28265491e4d30e4184` |
| `2ecf-strong-ramp-h-radial-witnesses.py` | `e6a2af2c4389295022365d1f9faa41acc5db6945b904e8ee4a2df169a21997e8` |
| `2ecf-strong-ramp-refinement-composition.py` | `4aa90a38cba24930077ae0be8196da43cf27299abe871091030dd8ef7f4d737c` |
| `strong-physical-h33-raw-continuous.json` | `7fe5f10a94a9455079001077472c63e4c0bcbc24f65c4619a06de68472a96daf` |
| `strong-physical-h65-raw-continuous.json` | `61111014bb6a27994ac4b5fe5bbf09205ea583fe6c3d3c0909c9c81cfd2b4279` |
| `strong-physical-h-radial-witnesses.json` | `b58439a164bbe639176e99e1f824cc8ea79c876a0d3deacaa2f78d9392055081` |
| `strong-physical-h-whole-prefix.json` | `88c023e35f60d9c30f9b6504d0a3b71a3ae7b4d9a56a9763e86d9bba8f8e023d` |

H33 与 H65 最坏度量格分别为 19、63，最坏曲率格分别为 16、32。完整新物理图仍只消费准确中央、真实全部 ramp、准确 coast 及镜像；全闭后段与其交叉法球没有被加入这些报告。
