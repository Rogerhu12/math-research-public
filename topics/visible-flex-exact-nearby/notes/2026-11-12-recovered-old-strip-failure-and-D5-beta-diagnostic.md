# 已丢失结果的实际重算：旧复门失败和 D5 相位诊断

2026-11-12。下述两项均在 07:46 UTC 环境重置后重新实际运行，
不以旧摘要替代数据。失败和普通数值结果保持各自原有性质。

## 宽度 1/128 的旧实部门失败

源 `fourfold_phase_modulus_characteristic_strip.py` 的 SHA256 为
62c925991a373a2af66c4dc3fcf7667646675b850ec23c8ac6e2b852aad3ec7d。
沿完整 R57 独立控制盒的 592 个准确径向单元重跑物理角 strip1/128。
输出为
`data/phase_ring_continuation/type_fixed_step02_d5_modulus_and_old_gate_1over128.json.gz`，
SHA256
5a17696f27e7823b0e1c8ed4e10756c4c478ba384c5ec96296e4c313c6ba6822。

新 moving-frame 模长门 592 个全部通过，最小下界
|nraw|≥.3938911136595034。原来的 Re nraw<0 证明门仍有 31 个失败，
索引为 0..30，最大实部上界为 +.12243668982463747。
失败是该估计无法证明目标实部符号，不是实际 nraw 在域内必为零。
它复现了旧失败，不能被新的模长结论抹去。
完整 1/64 模长门及其适用分支说明已见 R59。

## 原 D5 中心的 MP Taylor 诊断

固定输入是 `type_fixed_step02_d5_jet_interval_inputs.npz`，
SHA256 0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b。
源 `fourfold_phase_beta_taylor.py` SHA256
3a7084be73ade614c2ba29c90dc1c109c682a65151a354758dbaf072f0efc700。
在本课题目录执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/fourfold_phase_beta_taylor.py \
  --frozen-inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --quarter-nodes 256 --angles 512 --dps 50 --degrees 8 12 \
  --collars 1/2048 --gauss 12 --root-initial 0.238396977519 \
  --zero-order ground-state --out notes/2026-11-12-D5-root-taylor-beta-mp50-q256-a512.json
```

新输出 SHA256 为
50f6ee73c82f4adb248cd774ceb0f038707d891da85bdaf954d466f308bca791。
有限模型根约 .23839697751927484249495158，
g₀≈−.00642940900558569993，g₁≈−1.38495190325200854。
8/12 阶分别得到 collar≈531.4953306925421、531.4953307193696；
bulk≈−457.4434877070346；β≈37.02592149275376、37.02592150616750。

这里没有有向包围、完整无限尾或完整角/径向余项。
这些值是恢复后的普通诊断，不是严格 β 区间，也不属于准确 δ₂/δ₃。
当前主线的严格 collar/bulk 继续按各自准确 affine 对象重算。
