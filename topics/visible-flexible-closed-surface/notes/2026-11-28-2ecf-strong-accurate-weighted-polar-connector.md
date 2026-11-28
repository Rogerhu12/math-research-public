# 准确 Γ95/R205 端口与全闭正高度极坐标连接

[R265](../results/R265-accurate-weighted-polar-connector-global-embedding.md) 将 R246 的每个条件代入 R261 的准确末环与原 R205 cut。闭环带连续自嵌入、真实端口六 jets 一致、全域面积下界 $1.35\,10^{-14}$。全部区间计算是物理函数预算，原 G10 浮点端源和后缀场的误差仍须分开处理。

此前单一 1024 角盒、直接展开出口角导数的尝试退出 1；它已给正高度质量但 $d_2$ 下界为 $-1.690$。最终采用 R137 正交标架的准确 Gauss–Weingarten 公式，只有需要的左盒二分。区间工作进程 60.039 秒、自然退出 0，第二个确切有理数面积合成进程自然退出 0。左 1440 叶，右 256 叶及反射。初始失败未当作满足正性。

`SCRIPTS` 为课题的公开 scripts；`DATA` 含原 gap105 的 ramp/coast 两个 master（按 R261 原件记录生成），`OUT` 是新目录。

```bash
set -eu
mkdir -p "$OUT"
python "$SCRIPTS/2ecf-strong-accurate-polar-port-budgets.py" \
  --scripts "$SCRIPTS" --ramp "$DATA/gap105-prefix-ramp-master.npz" \
  --coast "$DATA/gap105-prefix-coast-master.npz" --cells 1024 \
  --output "$OUT/strong-accurate-polar-budgets.json"
python "$SCRIPTS/2ecf-strong-polar-connector-area.py" \
  --budgets "$OUT/strong-accurate-polar-budgets.json" \
  --output "$OUT/strong-accurate-polar-area.json"
```

| 对象 | 本次 SHA-256 |
|---|---|
| 2ecf-strong-accurate-polar-port-budgets.py | `0220bf8b852871208cf47cb3e1ba41ebce616c6d10dab8f8ed80d7fe98a3f88d` |
| 2ecf-strong-polar-connector-area.py | `ab0f5139b7c0e3f0a85e0a3a4b0ddbe193f591cf5137661bad72b4621ce3ee7a` |
| strong-accurate-polar-budgets.json | `98b784dd1e3da8a62363936c4385dd8c4ec3514710a0161562acb44e99e931a9` |
| strong-accurate-polar-area.json | `f0128d1d26c912157f7a1d343b0fdd6759b814283a5cd8a1ec290ea79dde6617` |

预算 JSON 含运行时长，再生时核对确定性的 rowSHA256 及准确有理数；两真实报告与各角盒原件不入 Git。
