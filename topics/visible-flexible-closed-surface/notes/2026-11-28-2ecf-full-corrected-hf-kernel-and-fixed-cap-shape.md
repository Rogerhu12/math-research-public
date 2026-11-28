# R272 的整盘统一势、保真接口与两顶固定帽

[R272](../results/R272-actual-full-corrected-HF-kernel-and-fixed-cap-strong-shape.md) 对 gap 1.05 的实际完整闭核和已加 R210 两固定帽的相位族给出连续嵌入与整闭面形状变化量。实际 $D\le3.076641236$、$\delta_{\rm hold}\ge.6576$、$\delta_E\ge.1638$。这是一条已通过两项强变化量的具体几何分支；同一度量的实际误差收敛与足够大的整闭面 reach 各有自己的求解任务。

复用 [R270 生成记录](2026-11-28-2ecf-corrected-physical-hf64-complete-suffix-embedding.md) 的 HF64 完整物理场文件和准确端口缺陷，以及 [H65 生成记录](2026-11-28-2ecf-strong-same-g-genuine-physical-h-position-fields.md) 的 65 节点 master。令 `S` 为公开课题 scripts，`W` 为 gap105 两个旧 master 及 H65 G10/G11 prepared 所在目录，`F` 为 HF64 的 `strong-physical-hf64m80-W.json.field.npz`，`H65` 为准确物理 `ramp-65.npz`，`EDGE` 为 R270 生成的 2048 端角缺陷，`OUT` 为新的可写目录。

```bash
set -eu
mkdir -p "$OUT"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
ramp="$W/gap105-prefix-ramp-master.npz"
coast="$W/gap105-prefix-coast-master.npz"
python "$S/2ecf-strong-hf-upper-disk-potential.py" --scripts "$S" --field "$F" \
  --ramp "$ramp" --coast "$coast" --prepared "$W/polar-physical-H65-prepared.json" \
  --independent "$W/polar-physical-H65-independent.json" --angles 1024 --output "$OUT/pot.json"
p=(--scripts "$S" --potential "$OUT/pot.json")
python "$S/2ecf-strong-hf-upper-disk-native-prefix.py" "${p[@]}" --master "$H65" \
  --angles 1536 --central-partitions 48 --output "$OUT/native.json"
python "$S/2ecf-strong-hf-upper-disk-coast.py" "${p[@]}" --ramp "$ramp" --coast "$coast" \
  --angles 1024 --radials 4 --output "$OUT/coast.json"
hf=(--field "$F" --ramp "$ramp" --edge-defects "$EDGE")
python "$S/2ecf-strong-hf-upper-disk-suffix.py" "${p[@]}" "${hf[@]}" \
  --portion interior --angles 2048 --depth 2 --output "$OUT/interior.json"
python "$S/2ecf-strong-hf-upper-disk-suffix.py" "${p[@]}" "${hf[@]}" \
  --portion ends --angles 4096 --depth 3 --output "$OUT/edges.json"
python "$S/2ecf-strong-hf-upper-disk-R205.py" "${p[@]}" --ramp "$ramp" \
  --angles 1024 --radials 192 --integral-panels 8192 --output "$OUT/tail.json"
python "$S/2ecf-strong-hf-upper-disk-position-window.py" --scripts "$S" \
  --field "$F" --edge-defects "$EDGE" --angles 512 --output "$OUT/window.json"
python "$S/2ecf-strong-hf-upper-disk-and-graft-compose.py" "${p[@]}" --field "$F" \
  --native "$OUT/native.json" --coast "$OUT/coast.json" --interior "$OUT/interior.json" \
  --edges "$OUT/edges.json" --tail "$OUT/tail.json" --window "$OUT/window.json" \
  --output "$OUT/whole.json"
```

以上实际各进程均自然退出 0。角势挑选只用有限位置的线性规划，H65 的旧 192 角样本在候选选择阶段作周期插值；最终使用的 1152 个系数按实际 dyadic 解释，native H65 的真实全角导数和准确端口在后续各段独立包络。较粗候选在完整后缀区间未过正性，故没有计入实际整盘结果。径钟通过保向图像恒等式转移。三步、四步新增 XYZ 的不同场不在本次几何回执之内。

| 实际文件 | SHA-256 |
|---|---|
| `2ecf-strong-hf-upper-sector-check.py` | `a846dcd818f516606e571e0b21be917ef5eb7766243f88ef9e28acfcd02af802` |
| `2ecf-strong-hf-upper-disk-potential.py` | `56daca889170b6329d4e32e5b8d52b2e7703b3e5d43e68b1ef6df5269dfd22de` |
| `2ecf-strong-hf-upper-disk-native-prefix.py` | `5b2aec43dcb8d3034e3856d72eb56a37bb28e7dde0eb6494e94cadee51b854f2` |
| `2ecf-strong-hf-upper-disk-coast.py` | `808d50512b309e5f91a54ca24a93501abb9d8e55b8c3c872587803357f9d0e3c` |
| `2ecf-strong-hf-upper-disk-suffix.py` | `ea06d4e4e1349dc6e951c6a4f17de876bbb89d28d356a2f395ffca5b5728ddc6` |
| `2ecf-strong-hf-upper-disk-R205.py` | `22925afc64a399e8e8fb4001a17bb26ecfc86335c99d12f84e114b5239c7ad33` |
| `2ecf-strong-hf-upper-disk-position-window.py` | `87000d0b7ef4108233d196a725c0e3399ac812ef58c315b6070b95c807ac0663` |
| `2ecf-strong-hf-upper-disk-and-graft-compose.py` | `9878f98c9803a8fba36333e531ba8eec46a1122863ad66e8853c327f74cf832a` |
| `strong-hf-upper-disk-potentials-1024.json` | `6bc61c6b48b3568ac713e90d38bd9432c3e94f6f218b3a7b68fcee8a2aae5317` |
| `strong-upperdisk-central-H65-1536.json` | `1c79cfa79efe785c7498e6ca1c4dd4785aa9983af6d1969bb40a3795da7d2253` |
| `strong-upperdisk-accurate-coast.json` | `4415ace4d6056389c3011479bbae4575eb1f140bef89c054991ac8cd4ebcc0c8` |
| `strong-upperdisk-interior-1024fit.json` | `b53ad6977adbf3618a2e0f7fe40534c8ff07281aae676154ecbe475042aeb4d0` |
| `strong-upperdisk-edges-1024fit.json` | `2786899e605df702e2c896bf3b29b9d06fce8af748b3881895aea98c7410a138` |
| `strong-upperdisk-R205.json` | `39c307df6c2db19e37f9c46f9cb57812403fc24c1b4b934b4536902e26b3e1e3` |
| `strong-upperdisk-position-window.json` | `de7530a5aecec5d3ac098682c3fdca4c416e634eace793fa00b9324392418824` |
| `strong-upperdisk-actual-R210-graft.json` | `c79b3941d77dd7be3c1c270e95376f4ceec5e6690ed8c5ca3901cfaf31d1c25a` |
