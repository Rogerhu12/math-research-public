# 准确极坐标连接的真实材料度量与总变差

[R266](../results/R266-accurate-polar-ray-metric-and-radius-variation.md) 将同一源的点误差、整射线长度和任何可能修正的必要幅度分开。原侧射线的实际加权点给 $\delta>.93572118$；全部单调高度重分配仍共同满足 $\delta>.43150655$。自然退出 0。

沿用 R265 的两个 master，执行以下命令。程序先确定 R265 的真实极角，再比较同一条射线；扫描只用来选择有理见证，全部证明数字由区间数给出。

```bash
set -eu
mkdir -p "$OUT"
python "$SCRIPTS/2ecf-strong-polar-physical-ray-metric.py" \
  --scripts "$SCRIPTS" --ramp "$DATA/gap105-prefix-ramp-master.npz" \
  --coast "$DATA/gap105-prefix-coast-master.npz" \
  --output "$OUT/strong-accurate-polar-physical-ray-tv.json"
```

| 对象 | SHA-256 |
|---|---|
| 2ecf-strong-polar-physical-ray-metric.py | `0d067a29be0e430d429062d4421cc298704adc840c4f3daff52c2dbe3f791588` |
| strong-accurate-polar-physical-ray-tv.json | `7341854d2260f53568a22b4b40ab56ac76e0a02677a80b4272bb0b8b83e06ae1` |
| 2ecf-strong-accurate-polar-port-budgets.py | `0220bf8b852871208cf47cb3e1ba41ebce616c6d10dab8f8ed80d7fe98a3f88d` |
