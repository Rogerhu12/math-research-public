# 精确仿射第二步参数点的紧根区间

恢复状态：执行器更换后已从同一冻结输入完整重跑。源码与原版逐字
匹配，重生成的完整 JSON 与丢失前报告的 SHA256 完全一致；本页据实际
重放结果恢复有限证书，不由汇总值补造数据。

本页针对 R57 准确仿射族的参数

$$
\delta_2=-\frac{15291006546051}{9007199254740992}
=\operatorname{binary64}(-0.001697642753711981),
$$

其十六进制为 `-0x1.bd06e06e10600p-10`。原始 phase 控制与 mean
系数在实数中取 $c_0+\delta v$、$\alpha_0+\delta w$，之后才施加
固定 base 物理权重、显式偶奇平均、准确 slope 积分及真实无限
R33 原函数。逐坐标舍入的第二步 checkpoint 是另一个对象。

## 准确输入与已重现的根区间

原点 `type_fixed_step02_d5_jet_interval_inputs.npz` SHA256：

`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。

方向 `type_fixed_step02_d5_actual_parameter_direction.npz` SHA256：

`8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。

共同根证书 `type_fixed_step02_d5_parameter_root_interval.json`
SHA256：

`b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8`。

对 $E=\langle F_x\cdot F_x\rangle$，取
$C=a'E'-2a''E$、$K_0=C/(2aE^2)$。恢复后重跑得到准确 binary64 端点

$$
t(\delta_2)\in[.23839687378106797,.23839687378107466],
$$

宽度上界 `6.689093723366569e-15`。普通十进制外包可用
$.2383968737810679<t<.2383968737810747$。参考中心
`.23839687378107133` 仅为近似数，后续 ODE 必须保留整个根区间。

## 有向 interval Newton 的存在逻辑

共同根证书已在全部 $|\delta|\le\operatorname{binary64}(.01)$ 上
证明根存在于 $I_0=[.238394,.2384]$，且在共同 collar 中唯一简单。
对当前区间 $I$ 和其中一个准确 binary64 中点 $m$，有向包住
$C(m)$ 与整段 $C'(I)$，且验证后者下端为正。实均值定理给

$$
t=m-\frac{C(m)}{C'(\xi)},\qquad \xi\in I.
$$

因此取 $I\cap(m-[C(m)]/[C'(I)])$ 保留已经知道存在的同一个根。
最后的窄区间不需要重复证明两个端点的符号。相位径向导数保持
$S_0^{(j)}+\delta V^{(j)}$，未先改成独立系数盒。

恢复后重跑的三次步骤：

| 步骤 | $C'(I)$ 包络 | 新区间 |
|---|---|---|
| 1 | $[299.83786598896955,300.65019314329743]$ | $[.23839687360779935,.23839687394930525]$ |
| 2 | $[300.2548838001023,300.25493002154394]$ | $[.23839687378106797,.23839687378107466]$ |
| 3 | $[300.2549066927236,300.254906695089]$ | 不再收缩 |

第三步点 $C$ 的区间宽度已由完整区间 DFT/primitive 舍入与尾预算
主导；没有把浮点零残差当作准确根。R58 的参数一、二阶根 jets
保持独立，本页不重复其证明。

## 源与重放

已逐字恢复源码 `scripts/fourfold_phase_affine_root_point.py`，SHA256：

`3227cb85a8153a1860384ece21fb2e262a8cb88da9fd24f59b3e3ddef75eebd3`。

原报告
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step2_root_tight.json`
重跑 SHA256（与丢失前完全一致）：

`c2cfad858f64a0082d131eb492993c6a237ab249220dfe61593323c8d1cdfeeb`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_affine_root_point.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --common-root-certificate topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json \
  --delta=-15291006546051/9007199254740992 --quarter-nodes 256 --iterations 4 \
  --out /tmp/visible-D5-affine-step2-root-tight.json
```

这是根定位证书，不代付实际 ODE、共轭、帽、全频逆或闭合等距族。
