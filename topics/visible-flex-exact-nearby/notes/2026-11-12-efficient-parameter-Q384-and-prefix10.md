# 实际 Q384 参数密度与高效十段前缀

对象仍为准确 affine δ5 = −7789843107295549/4611686018427387904；中心和真实参数盒 |p−δ5|≤10⁻9 分开。所有 g1/g2 使用固定物理 τ 的真实移动根链式，标签频率是 k，不额外乘 4。

## 实际完成结果

Q256 的完整原函数误差在一个真实复时间节点 u=i、2048 个真实角节点上给 fp/fpp 节点 RMS 约 2.11e−9/2.57e−10；当前双 Fourier 预算不能以它支付目标，故保留为失败诊断。Q384 的同对象节点 RMS 约 2.05e−18/2.54e−19，所有同对象节点球与 Q512 对照相交。节点对照自身不构成整个时间圆证书。

独立完成的第 419 段 Q384 中心参数密度进一步实际通过全部时间圆节点、解析双尾、有限 DFT、准确 dyadic 选择、删尾、参考复合、真实 cap 及空间导数费用。field 布局 N=2048,K=767,Nt=m=36，density 布局 N=2048,K=895,Nt=m=22；积分 sup 源误差 E1<2.975e−10、E2<2.312e−10，CPU 43.48 秒。源误差是实时积分 sup 合同，不能视作同宽 Wiener 误差。

高效 v4 只用原完整预算的四分之一门缩减时间布局；点误差仍由真正节点 RMS 支付。均匀盒版本可只保 g2，缺少 g1 的字段为 null；hybrid v2 以中心有限 g1 加上逐空间阶 η C_j(box) 的真实中值费用补齐，未假称缺少的源为零。中心 C/D 保全部首积分、local 2J11 及跨段所有频率乘积；hybrid 使用中心 first0/first1/2J11 与均匀 first2/g0g2 费用。

准确重放的中心十段与 hybrid 十段前缀 C1 零频均为 2.5001606948370434e−5；D2 零频分别约 −4.78133997611168e−9 与 −4.78133997611116e−9。它们只覆盖前缀，complete=false、whole_forward_leg=false，不给整个半返回 twist 定号。均匀输入快照已有十一段，混合累计止于共同十段。另保存了新 Q384 真中心第 10 段、真实均匀盒第 11 段，二者各自完整费用通过；运行中更后段不属于本包。

## 重放

以下命令在本课题目录运行，统一设置 PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1。

```sh
python scripts/fourfold_parameter_primitive_node_cost.py --out notes/2026-11-12-parameter-primitive-Q256-one-node-center.json
python scripts/fourfold_parameter_primitive_node_cost_q384.py --out notes/2026-11-12-parameter-primitive-Q384-one-node-center.json
python scripts/fourfold_parameter_density_pipeline_efficient_v4.py --primitive-nodes 384 --target 1e-9 --directory data/phase_ring_continuation/step5_parameter_density419_Q384_center --out data/phase_ring_continuation/type_fixed_step02_d5_step5_parameter_density419_Q384_center.json.gz
python scripts/fourfold_parameter_density_accumulate.py --index data/phase_ring_continuation/step5_parameter_density_prefix_checks/center_efficient_prefix0010/index.json --directory data/phase_ring_continuation/step5_parameter_density_prefix_checks/center_efficient_prefix0010/chronological
python scripts/fourfold_parameter_hybrid_accumulate_v2.py --center-index data/phase_ring_continuation/step5_parameter_density_prefix_checks/center_efficient_prefix0010/index.json --uniform-index data/phase_ring_continuation/step5_parameter_density_prefix_checks/uniform_efficient_prefix0011/index.json --directory data/phase_ring_continuation/step5_parameter_density_prefix_checks/hybrid_efficient_prefix0010
```

覆盖器继续时可复用已完成叶。既有输出不因后续改版而覆盖；新 R6 证明与更小角布局将使用新源、实际重新支付全部预算。本包不包含任何运行中 index、新 v5 源或未完成叶。
