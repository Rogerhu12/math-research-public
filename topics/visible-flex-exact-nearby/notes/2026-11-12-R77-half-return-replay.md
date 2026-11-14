# R77 与准确前向终点的重放包

2026-11-12，reproduce_newton。R77 是显式对称族的结构证明；下面的计算只认证已定义有限参考相对半旋转的预测误差，不认证真实半返回。

## 定义与身份

输入来自已逐字恢复的 δ₄ shared1032 前向参考及准确 δ₅ retarget 定义。旧前向 manifest SHA256 为 43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0，Q_forward manifest 为 f1e7556a13aef2a4e5661fc00c1e9c4eda961335fb8685d26bcef550b7b147ce。descriptor 为 097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052。

δ₅ 准确定义为 −7789843107295549/4611686018427387904，同一 exact-affine origin/direction，且径向偶奇投影准确施加。target object SHA256 为 91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848，target H₅ 为 0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2。

最后一段 549 的完整独立包保留八个 U/L、Q 控制以及原始 JSON 全字节，不只保存一个端点数值。最后 Q 控制与 Q_forward,end 再按字节核对。准确终点 τ=+π/2，选择 Bernstein 最末控制，没有把 binary64 的 π/2 当成真端点。

## 重放

以下命令在课题根目录执行，设置 OPENBLAS_NUM_THREADS=1、OMP_NUM_THREADS=1、PYTHONDONTWRITEBYTECODE=1。第一条只在原始分片仍存在时提取新包；重放半预测只需要已保存的小包和仓库源码。

```bash
python scripts/fourfold_retarget_reference_segment_package.py \
  --descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --segment 549 \
  --out /tmp/replay_forward549.npz.gz \
  --report /tmp/replay_forward549_extraction.json

python scripts/fourfold_retarget_reference_segment_package.py \
  --check data/phase_ring_continuation/step5_forward549_exact_reference_package.npz.gz

python scripts/fourfold_half_return_predictor.py \
  --package data/phase_ring_continuation/step5_forward549_exact_reference_package.npz.gz \
  --bits 256 --nodes 4096 --widths 0,1/512,1/256,1/128 \
  --out /tmp/replay_half_return_prediction.json
```

提取器拒绝覆盖已存在的包和报告。重新提取可能因新的报告时间元数据而改变外部提取报告，但小包的全部准确输入和内嵌原始 JSON 仍须匹配既有身份；本次冻结包的 SHA 以 manifest 为准。

## 有限函数与费用

直接从最后 Bernstein 控制读取 U_end 和 Q_end，以 Arb 多项式乘法保留 U_end+Q_end a 的完整 Laurent 乘积。其最高正频率为 644。H₅ 的全部 516 正频率均保留；α=2π(15121+√5)/27422 在 Arb 中定义，旋转 Fourier 系数按 exp(ikα/2) 计算。

对每个宽度 s，源码计算准确有限残差的 A_s 包络：|e₀|+2Σ_{k>0}|e_k|exp(ks)。这控制完整标签带，而不只是 4096 个样本。采样字段只是另列的有限函数诊断。

报告中的 half_lift_integer=0,1 表示两个圆周半旋转选择 d₀=α/2 与 d₁=d₀+π；它不是说同一个圆周映射的两个提升仅相差 π。同一个映射的自然实提升仍相差 2π，R77 已明确 ODE 的未取模约定。

已得到正确选择的 A₀<2.768×10⁻¹¹、A_{1/512}<3.003×10⁻¹¹、A_{1/128}<6.939×10⁻¹¹。另一个选择的平均残差约 −3.14159265359250333069。以上误差均未含真 δ₅ 的场缺陷校正。

这次计算没有使用完整返回的小残差去推断半返回的小残差。R77 的平方恒等与这个明确有限预测是两件不同的成果。完整返回后续必须作 A∘H⁻¹∘A 或等价的前共轭复合，保持域和误差；不能直接把保存终点 A=p∘H 当成 p。

