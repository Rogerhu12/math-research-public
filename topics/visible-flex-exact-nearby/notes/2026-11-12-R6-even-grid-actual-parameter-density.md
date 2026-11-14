# 实际 R6 参数补集与偶数角网格

准确对象仍为 δ5 = −7789843107295549/4611686018427387904。新源 efficient_v5 保留旧 R3 点模型和全部真实 cap，以独立 Q512 已证 R6 包支付补集；真实点网格使用 Q384 的无限原函数预算。完整数学接口在 R84-independent-time-complements-and-even-angle-grids.md。

第 18 段已分别完成中心 signed g1/g2 和整个真实 |p−δ5|≤10⁻9 的 g2-only 证书。两个报告共用相同准确 reference、主芽及真实 Q512 R6 包，不能互相替代参数作用域。

| 作用域 | 真场角 N / K / 时间 Nt=m | 有限密度角 N / K / 时间 Nt=m | 积分 sup 源误差 | CPU 秒 |
| --- | --- | --- | --- | --- |
| 中心 g1/g2 | 1280 / 639 / 22 | 1792 / 895 / 14 | E1<2.248e−10, E2<1.959e−10 | 28.13 |
| 真参数盒 g2-only | 1024 / 511 / 18 | 1024 / 511 / 10 | E2<4.674e−8 | 20.10 |

所有真实节点、双重 alias/tail、准确有限选择、删尾、参考复合、空间 jet 和 cap 费用均包含在各自报告。中心保有完整首积分与 local 2J11；均匀报告缺少 g1 的字段明确为 null，必须由中心 g1 与逐阶中值费用进入 hybrid，不能称它为零。

最初试算已通过完整解析 N1280 预算，但旧 sample 的二次幂节点 guard 在采样前拒绝。该失败报告和源 initial 版本单独保存。独立 native_even_grid 逐项保留旧真实样本公式，只使用 NativeSeriesFFT 已有的任意长度 Arb DFT，并核有限频率注入。numerical 代理亦逐段读核，未重跑节点；实际完成结论只来自后来成功报告。

## 准确重放

在本课题目录，以 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 运行：

```sh
python scripts/fourfold_parameter_density_pipeline_efficient_v5.py --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0018_r.json.gz --reference-certificate data/phase_ring_continuation/step5_forward_density_complete/forward_0018_ef134f2a18.json.gz --reference-source scripts/fourfold_forward_density_pipeline_layout_v8.py --expanded-parameter-proof notes/2026-11-12-actual-expanded-parameter-domain18-R6-Q512.json.gz --primitive-nodes 384 --target 1e-9 --directory data/phase_ring_continuation/step5_parameter_density18_R6_Q384_center --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_density18_R6_Q384_center.json.gz
python scripts/fourfold_parameter_density_pipeline_efficient_v5.py --domain data/phase_ring_continuation/step5_sharp_time_domain_full/forward_0018_r.json.gz --reference-certificate data/phase_ring_continuation/step5_forward_density_complete/forward_0018_ef134f2a18.json.gz --reference-source scripts/fourfold_forward_density_pipeline_layout_v8.py --expanded-parameter-proof notes/2026-11-12-actual-expanded-parameter-domain18-R6-Q512.json.gz --primitive-nodes 384 --uniform-half-width 1/1000000000 --second-only --target 1e-7 --directory data/phase_ring_continuation/step5_parameter_density18_R6_Q384_uniform --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_density18_R6_Q384_uniform.json.gz
```

覆盖器 v2 可由 --pipeline 指向冻结 v5，并把这两个报告分别作为 center/uniform 的 --seed；中心和均匀真实参数源的独立扩大域证明缓存可共享。无已证扩大域时保持 R3；扩大域证明失败不会变成密度通过。实际节点阶数、原函数频率注入、误差目标等任何门未通过，该叶不进入完成 index。全 550 段、半返回参数定号及最终 KAM 仍未由本两段报告证明。
