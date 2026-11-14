# 准确仿射第四点的独立根包络

新的参数点准确为

\[
\delta_4=-\frac{7789866024620307}{4611686018427387904},
\]

其 binary64 表示为 `-0x1.bacd7853ed113p-10`。这是同一 origin 加同一
direction 的准确仿射组合；没有先物化再舍入控制点。

本次用冻结的 `fourfold_phase_affine_root_point.py`（SHA
`3227cb85a8153a1860384ece21fb2e262a8cb88da9fd24f59b3e3ddef75eebd3`）
重新计算，得到真正无限原函数同步目标度量的唯一正根

\[
t_*(\delta_4)\in
[0.23839687429955836,\ 0.23839687429956505].
\]

报告给出的有向宽度上界为
\(6.689093723366569\times10^{-15}\)。
`0.2383968742995617` 仅为参考中心；整个上述区间才是认证输入。

| 输入或输出 | SHA256 |
|---|---|
| `type_fixed_step02_d5_exact_affine_step4_object.json` | `87566dee6e119bb4127200c2dae38f9cdf692a18475c1cde23961a56605919b5` |
| origin `type_fixed_step02_d5_jet_interval_inputs.npz` | `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b` |
| direction `type_fixed_step02_d5_actual_parameter_direction.npz` | `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab` |
| whole-family `type_fixed_step02_d5_parameter_root_interval.json` | `b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8` |
| 本次 `type_fixed_step02_d5_exact_affine_step4_root_tight.json` | `03a0863733b25b6c4058a39590648dda2292a2943e783021747e3bc3f27c86f4` |

证明沿用已认证全参数族区间内的唯一根与正导数，再对当前准确单点做
四次有向实均值定理收缩。本次单独重算，未迁移第三点的根区间。
这份文件只提供新点的根输入；新点的 ODE、共轭、残差和参数导数仍须
使用各自对应的报告。

在课题目录重放：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_affine_root_point.py \
  --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --common-root-certificate data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json \
  --delta=-7789866024620307/4611686018427387904 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/exact_affine_step4_root_replay.json
```
