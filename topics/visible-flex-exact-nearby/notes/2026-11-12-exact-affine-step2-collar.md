# 当前实际 affine family 的 delta2 根 collar

状态：**这个准确参数点的 collar 已完成完整有向计算。** 依主线安排，后续完整 beta 优先切到
更新的 delta3；本笔记不宣称 delta2 的 bulk 或全 beta，也不把另一个 D5 中心的37.0259诊断转授过来。

实际对象是 R57 的冻结 affine family，在准确参数

$$
\delta_2=-\frac{15291006546051}{9007199254740992}
$$

处取值。规范对象文件为 data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json，
SHA256 为 aa5df888dbf672c9e221f03e80cfa06c3c9c94a5dd7dd4f29fe15b1d795d99b1。
origin NPZ 的 SHA256 为

    0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b

direction NPZ 的 SHA256 为

    8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab

source scripts/fourfold_phase_beta_affine.py 的 SHA256 为

    b82724a2af026b9b9ee935f3df0eb95e7feb36ac5f65db9694085b5a4ad25991

它先在 Arb 中对每个冻结 raw phase 系数作 c0+delta2*v，对 mean amplitudes 作 alpha0+delta2*w，
随后才乘固定物理 base 的三次方/二次方并施加明确的偶奇对称；没有先生成一个舍入过的浮点 NPZ。
height 仍来自冻结 slope 的准确积分及准确奇对称，角向仍是完整无限 R33 primitive。
三个已冻结 native/bulk 依赖的哈希都记录在报告中。

## 本次完整有向结果

输入 tight-root 证书 SHA256 为 c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb。
完整无限 E 修正后的三次 Arb 区间 Newton 给出安全短区间

$$
0.23839687378107130494997869968483<t
<0.23839687378107130494997869974159.
$$

固定物理 cut 为准确有理数

$$
b=\frac{268136140074737}{1125899906842624}.
$$

使用与原对象相同的 R52 机制：192 bit、quarter grid512、角网格2048、24阶 G、72项径向 series，
真实复圆盘半径 .0006、归一化复角宽 .02；更大输入域为 R0=.003、RE=.0025、角宽 .32。
代码检查所有正负准确 binary knots，确认物理 collar 不跨 scalar span。

完整结果为

$$
\boxed{1307.2089803176<I_{\rm collar}(\delta_2)<1307.2089806206.}
$$

它包括准确参数算术、真根宽度、全部 infinite Fourier/alias 误差、完整目标 E、舍入、径向与角余项。
连续复域上各实际几何分母和 deflated 曲率的正实部门均通过。
实际 G 上界小于 .046634；径向尾不超过1.514489e-7，角求积误差不超过1.341133e-13。

完整报告 notes/2026-11-12-beta-exact-affine-step2-collar.json 的 SHA256 为

    2b6ea03cb3c415aaaa2a74825791f36ee3881dc25f2297144ce59fbfa466e076

本次约154秒。报告的 lower/upper 字符串用于后续有向汇总，不能用粗显示的 ball 中心当严格端点。

## 重放

```bash
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_affine.py collar \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json \
  --out notes/2026-11-12-beta-exact-affine-step2-collar.json
```

更换 delta3 只应传入对应的准确 object 与 root certificate；adapter 核查 origin、direction 和准确
delta 三者的一致性。当前对象的 collar 不能与原 sym 或旧 D5 中心的 bulk 混合。
完整相位危险格、实际 PDE 全网络、有限低块与非线性族仍须继续支付。
