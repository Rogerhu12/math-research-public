# 在同一 $g$ 上增加 936 个真实训练径点后的完整谱求解

**有限真实加密。** 取[14820 个实际位置变量与四向角对谱](2026-11-28-2ecf-strong-hf-real-refined-ring-spectrum.md)的第一阶段。保留原双 G10 全部 4291840 行、所有物理行原权重，增加原活动后缀各相邻训练径点的中点，前 .14 部分另取两个四分点。排除与原 G10 或 G11 任何实际径点相同的点，余下 936 个真实新径点。对每个新径点用原 1024 角真窗口／原后段 oracle 求半径、一次与二次导数，9 个原始径点复核差为零；2364 次供应器请求、955.22 秒后其真实 OS 自然退出 0。再作用原 36 个角半径系数、新对角修正和同一冻结正长度钟，旧点重算的目标两 jet 最大差 $3.56\cdot10^{-15}$ 以下。

每个新径点使用 224 个真实角，从 HF64M80、原 W、旧角径钟、双材料钟、6615 母位置及 14820 已知修正分别重建全部位移后角及物理导数。新网原行 $936\times224\times14=2935296$，合计 **7227136 个物理行**。新组按该后缀区间 Voronoi 径宽乘 $ds/dx$ 与原组同一归一化，整体权 .5；原两组未缩小。保留全物理形算子、原 14 行项、单角剪切及每组四向全部有序角对。G11 的 668 径点始终未入新增训练，其 540 个原两组外径点仍是训练外径点。新组自身暖场 metric 峰 .088225241、曲率 19.8788538，额外原成本 .0314777741。方向差分展示新全目标梯度绝对差 $1.45\cdot10^{-10}$ 以下。各阶段 64 次 L-BFGS-B 达到限额，合计 192 次、407.28 秒。

| 阶段 | 三训练组联合 metric | 三组联合曲率 | 三组原成本 | 独立 G11 metric | G11 曲率 | G11 held |
|---|---:|---:|---:|---:|---:|---:|
| 30 | .0848933082 | 19.6501473 | .088115657 | .0844952617 | 19.1609250 | .65927841 |
| 75 | .0829479759 | 18.4534047 | .088548390 | **.0812879335** | **18.0756435** | .65901146 |
| 140 | .0822533402 | 18.6686364 | .085105876 | .0813227239 | 18.0931245 | .65898219 |

终态三组分开的真实原成本为 .02836763792、.02836563171、.02837260663。第二阶段的独立 metric、曲率优于终态；有限加密虽比此前独立漏峰的 .11 改善，但距连续等距及全闭 reach 仍远。未把变更训练网与有限位置优化认作最终收敛。

```bash
python "$SCRIPTS/2ecf-strong-hf-new-radius-nodes.py" --scripts "$SCRIPTS" --prepared "$DATA/polar-physical-H65-prepared.json" --observer "$DATA/polar-physical-H65-independent.json" --diagonal clock-hf-diagonal-d006.json --ramp "$DATA/gap105-prefix-ramp-master.npz" --coast "$DATA/gap105-prefix-coast-master.npz" --candidate "$TOPIC/notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json" --window-target "$DATA/target-zero.json" --output clock-hf-new-radius-grid.json
python "$SCRIPTS/2ecf-strong-hf-fresh-grid-refined-ring-solve.py" "${hfargs[@]}" --diagonal clock-hf-diagonal-d006.json --warp clock-hf-two-material-spectral.json --warm clock-hf-full-joint-240-01.json --refined-state clock-hf-refined-ring-full-01.json --fresh-radius clock-hf-new-radius-grid.json --extra-angles 224 --extra-weight .5 --prefix clock-hf-new936-ring-full --metric-scale .080 --curvature-scale 18.5 --shear-scale .070 --spread-scale .074 --betas 30 75 140 --iterations 64 --frequency 32 --block 28
```

TOPIC 为主题目录。原 G10、G11、HF 供应器与目标零定义的重生见上引母记录及[原固定背景入口](2026-11-26-6a65-geometry-nonfold-polar-complete-baseline.md)。936 行半径输出 SHA-256 为 `9c8af072f91d3eda2fe0b000a3f7deabc45c08230b2d92fb607ef4f1d551bc0d`；三份位置状态依序为：

- `7d72de432c57769e62b053e16b1dd65988c07f289b48393730d1e29d500a28ba`
- `a6282fd073d18658cf4062fad5c119962441f07a79d137ee06fe37fb3141402d`
- `3186e118da69831771b6549a58fff878cb9ac06f7912ec428958b9487dbc33c2`
