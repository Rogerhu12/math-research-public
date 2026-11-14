# δ₅ 准确前向参考：全部550段的连续非零导数

2026-11-12，reproduce_newton。已经实际完成全部550段；两端是准确 −π/2、+π/2，549个内部接缝的原始 U/L 与 Q 系数均按字节核对连续。

## 已证结论

对完整前向准确有限参考 Y(τ,x)，τ∈[−π/2,π/2]、全部标签 |Im x|≤1/512，有

$$
\operatorname{Re}\partial_xY>0.0303368062124528487>3/100,
\qquad |\partial_xY|<1.04603135083599372<21/20.
$$

这里 x 是周期2π的规范初始标签，Y 是物理角；导数的基准常数为1/4。界覆盖全部角位置、全部实时间和闭复标签带，不仅是配置节点。它不是真实流的变分界。

完整报告 notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz：SHA256 87aeff7e8824c7d6301c6f33cbeea506e584004c5bee1591512a556348cbfd8c，872852 B。另有 complete-summary.json，对报告全部550行、549个 U/L 接缝及549个 Q 接缝再次核查，并从保存的有向端点独立验证两个简洁常数。

## 同一准确有限对象

仍是原 δ₄ shared1032 的有限参考，加上显式 δ₅ retarget：

$$
Y=x/4+U_{4f}+Q_fa,\qquad
a=H_5/4-Y_{4f,\mathrm{start}}.
$$

a 是准确整数除2¹²²的完整有限 Fourier 定义，Q_f 是已保存的完整 degree7 Bernstein／degree128 Fourier 函数，未被宣称为准确 Jacobian。它与原 U/L 的时间网格逐项一致，首值 Q_f=1，故参考首值严格为 H₅/4。

已逐字恢复的前向 manifest SHA 为 43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0，Q_forward 为 f1e7556a13aef2a4e5661fc00c1e9c4eda961335fb8685d26bcef550b7b147ce。retarget descriptor 为 097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052。

验证源 scripts/fourfold_reference_derivative_gate.py 的 SHA 为 a947f3b6bb93f254c22f8d9f526964899a4708cd4286b6029ddda0d5a1dcaa65，数学和源码已有独立审查 notes/2026-11-12-reference-derivative-gate-independent-audit.md。本次是此前欠缺的整条真实输入运行。

## 连续门与实际代价

每段八个真实 Bernstein 控制以2048个角节点、六阶实角 Taylor 的完整闭cell余项验证。所有有限 Fourier 模均保留；节点数大于原 U 控制的双倍次数。边界实部的 cosh 权和调和最小值原理支付复标签内部，Bernstein 非负凸组合支付整段实时间。

完整 retarget 导数 Q_x a+Q a_x 的 A_s 费用另行扣除，未把乘积误差只计在节点。所有550段均在2048节点通过，没有触发8192上限。报告所记 CPU 为526.355421秒，wall为3802.664658秒；计算已经结束，报告不再是live checkpoint。

在课题根目录重放到一个新输出，避免改动冻结报告：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_reference_derivative_gate.py \
  --retarget-descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --widths 1/512 --nodes 2048 --max-nodes 8192 \
  --taylor-order 6 --bits 160 \
  --out /tmp/step5_forward_q_replay.json.gz
```

若需从中断处恢复该新输出，可以附加 --resume；其源、输入和参数必须与既存 checkpoint 完全一致。

## 可直接使用的几何后果与范围

固定实时间时，带状域是凸的。两点 z,w 的差商等于连接线段上 Y_x 的平均，因此 Re Y_x≥m>0 给 |Y(z)−Y(w)|≥m|z−w|。所以这个明确参考在完整标签带单叶。真实实性还给上、下边界的物理虚部分别不小于 mS、 不大于 −mS；结合实提升的周期和保向性，像包含物理带 |Imθ|<mS，逆导数模不超过1/m。

本证书可取 m=3/100、S=1/512，因此得到保守的物理逆带3/51200及逆导数上界100/3。这仅是有限参考的实时间结论，不包含复时间盘、真实场的无零点，或真实流的误差。

R77 允许以后将不同真实场的严格验证缩到同一前向半程，再准确复合；不能把此 q 门直接当作完整返回的证书。回向大数据仍按恢复要求完成，但不会因此默默把有限参考声明为真实解。

