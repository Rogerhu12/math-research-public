# R270 的物理角势、准确端口及闭集合成

[R270](../results/R270-corrected-physical-HF64-complete-suffix-embedding.md) 对已求 6615 维物理校正后的实际 HF64 位置证明了全闭带嵌入。径向材料钟保持其整张图像。冻结 128 个三次多项式后的全域正性来自两次向外区间包络。

依[真实 Hermite 基底生成记录](2026-11-28-2ecf-strong-accurate-hermite-fourier-position-with-literal-W.md)产生显式场，记其路径为 $F$。下列 shell 的 `S` 为公开课题 scripts 目录，`W` 为旧准确 ramp/coast 两个 master 所在目录，`OUT` 为新的可写目录。

```bash
set -eu
mkdir -p "$OUT"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
port=(--scripts "$S" --field "$F" --ramp "$W/gap105-prefix-ramp-master.npz" --coast "$W/gap105-prefix-coast-master.npz")
python "$S/2ecf-strong-hf-projected-potential.py" "${port[@]}" \
  --angles 256 --sectors 128 --degree 3 --output "$OUT/pot.json"
python "$S/2ecf-strong-hf-true-edge-defects.py" "${port[@]}" \
  --cells 2048 --integral-panels 4096 --output "$OUT/defects.json"
common=(--scripts "$S" --field "$F" --potential "$OUT/pot.json" --angles 2048 --positive-only)
python "$S/2ecf-strong-hf-interior-continuous-projection.py" "${common[@]}" \
  --radial-depth 2 --output "$OUT/interior.json"
python "$S/2ecf-strong-hf-edge-continuous-projection.py" "${common[@]}" \
  --edge-defects "$OUT/defects.json" --radial-depth 3 --output "$OUT/ends.json"
```

实际线性选择、2048 角末端界及两次全盒计算均自然返回 0。早期 512 角、径向仅二分的内域界能证明 $J>0$，但给 $N$ 的下界为负；完整 2048 角及四等分包住实际正裕度。早期 1024 个 native 端角盒也实际运行，最终表采用更细 2048 个端角盒和逐项向外绝对和。CPU 耗时随运行而变，不参与不等式。候选多项式文件的系数直接来自前述冻结选择；其浮点优化状态不充当证明。

| 对象 | SHA-256 |
|---|---|
| `2ecf-strong-hf-projected-potential.py` | `eaf54e9df2d9fe8027c61305c31717bea3b8a086c0db6cdc8c66897df4456795` |
| `2ecf-strong-hf-true-edge-defects.py` | `364a4ac32ecbac18f441dbedeb2579eb126dad497318d51f98fdff4f8d76a396` |
| `2ecf-strong-hf-interior-continuous-projection.py` | `11df57f4811b4a051ab9130bd085322079b012918c47015077121dbca2f7d366` |
| `2ecf-strong-hf-edge-continuous-projection.py` | `16008e3d13ae8d24859b872f0d53ed250974ac442c8bfe72de80b06dc7e3a269` |
| `strong-physical-hf64m80-W.json.field.npz` | `eaa0835dc7ea5207f2a93cb0ba9b1d1634f2e00c5cb8964fe954b47601990d86` |
| `strong-hf-sector-potentials.json` | `52ece3660b0f897a55d1479a667ffdd13ef686aab10fc7ea5f22179ab374cff8` |
| `strong-hf-true-edge-defects-2048.json` | `a75b6d8f84e5f01cf271047b140d3eae997334ba8cc75bc4295217de96c0083c` |
| `strong-hf-interior-projection-2048.json` | `e6619aa133e00bb8ec378856c2b299db6ab8191f58be14c6cfcf6b5537d32ae3` |
| `strong-hf-true-edge-projection-final.json` | `9bd87f17438c9ced486fd7b9c365302c87008201a81f4b439022604e4ef745f9` |
