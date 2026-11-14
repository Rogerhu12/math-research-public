# R173 完整准确字段消费者：实际输入、接口与范围

本组把当前 131-node、K31、独立 tail16、物理 δ7 的完整有限字段接到
R119/R125 连续后验。完整证明直接登记于
`results/R173-complete-current-field-intervals-and-zero-end-posterior-interface.md`。
这里只给实现入口、真实运行和未付范围。没有新 BVP、whole F/J 或 body。

## 输入与函数定义

唯一实际场是
`notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz`，
SHA256 `2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f`。
54 参数仍按 `central[0:31] / tail[31:47] / profile[47:54]` 解码。
完整原 native definition 保存在 `...current-complete-arb-02-native-definition.json`。

准确 g 由 R171 packet
`2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz`
（SHA `7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c`）定义。
R175 可选 backend 仅改变相同 bump 多项式的区间范围算法。

两处准确函数语义必须保持明确：

- R149 出口整函数为 `N(f,xi)`，故 closed coast 采用准确 `sigma=s-e`。
  实际 `f-e-Lsaved=2^-54`；旧数值 endpoint shortcut 的差异不是零。
- R132 尾常数为准确 `4/5,17/50,23/50`。16 个原 controls 是 dyadic。
  旧二进制 `.8/.34` 求值差只属于数值比较，不能代换准确 g 的 cut。

R172 在整个末格另定义
`s=b+(S-b)t, sigma=b+(E-b)t`，原 raw/eta 复合 sigma，尾 shape 取
`a(s)`，R155 取 `K(s)`。这是明确的新末格有限表示，g 不变。旧 finite
residual/body 不转移。

## 可直接调用的完整入口

```python
from fractions import Fraction as F
from fd2d_gc_current_accurate_domain_arb import (
    AccurateDomainCurrentFieldArb, ExactNormalizedCellPrimitive)

field = AccurateDomainCurrentFieldArb(
    "notes/2026-11-12-fd2d-metric-current-complete-arb-02-native-definition.json",
    "notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz",
    profile_packet_sha256="7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c",
    precision=256,
    profile_backend="bernstein_bumps")

# 每个实际物理单元均有规范化标签；返回导数仍是物理 s / native xi。
q = field.cell_box(cell, F(1, 4), F(3, 4), F(1, 8), F(1, 8))
# q['fields'] 顺序 n,m,l，五项为 value,s,xi,xixi,sxi。
# q['chart'] 供物理 u 链式；q['connection'] 给 G,Rn,Rm,h_vector,alpha。

# 原末格之前也可使用物理有理坐标。
q = field.box(cell, physical_left, physical_right, xi_left, xi_right,
              angle_unit="radians", side="right")

# 准确 cut 只给真正的角 value/u/uu。
cut = field.accurate_cut_angular(F(1, 4), F(1, 4))
assert cut["connection"] is None
assert all(f.s is None and f.sxi is None for f in cut["fields"])
```

`angle_unit='pi'` 表示所给端点乘 π；`'radians'` 把输入有理数当作准确弧度。
所有请求须明确选一个保存 P1 单元。遇 atlas 径向界可选
`side='left'/'right'/'coast'/'both'`；完整角迹相同，径向侧迹不强行相同。

`field.box()` 不允许旧最后单元，以免不慎把 E 当作 S；最后单元使用
`field.cell_box(field.last_cell,tlo,thi,...)`。归一标签仅用于定位。
包含退化 cut 的一般 h 导数盒会如实 `UnresolvedInterval`，不被角迹 bypass
提升为完整 forcing。

### 零端 primitive

`ExactNormalizedCellPrimitive` 的 cos/sin 输入为形状
`(3, radial_degree+1, angular_modes+1)` 的准确有理数组。
P 近似完整 `(-a Rn,+a Rm,-a G)`，不是只含两条 Codazzi。

```python
primitive = ExactNormalizedCellPrimitive(
    field, cell, cosine, sine,
    provenance={"kind": "explicit finite P; its error is not assumed zero"})
budget = field.cell_primitive_box(
    primitive, cell, tlo, thi, xi_left, xi_right, angle_unit="pi")
```

其中 `q=(true cell length)*q_unit`。最后的 true length 为准确 `S-b`，不以
区间中点重新定义它。端点 q 和 q_xi 严格为零，q_s=P-mean 严格成立。
完整区间实际计算 `H-P`，并保留 `+(Us/Uxi)*q_xi + q cross alpha`。
该局部预算没有支付初始 frame/position 缺陷、整圈覆盖或完整径向递推。

## 实际运行

第一轮 `...current-complete-arb-01` 真实 exit1：检查器对恰在 P1 节点上的
实际样本取对称盒，越过声明单元。数学源没有修改，失败 report/receipt
原样保留。

另名 v2 只将正宽小盒限制在声明单元内：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python \
  scripts/fd2d-metric-current-complete-arb-check-v2.py \
  --field notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz \
  --out-prefix notes/REPLAY-current-complete-arb --precision 256
```

实际 77341/9eb94f true0，0.516585870002018 s，92652 KiB。10 实际点×15
jets、10 连续小盒、4 atlas 共迹、3 reference 恒等式、4 cut 角迹与非零
primitive 已消费。最大准确区间减旧浮点点值为 2.349174980954546e-11；
这是有限比较，非全域旧程序误差。

准确全域 wrapper 的小核：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python \
  scripts/fd2d-metric-current-accurate-domain-check.py \
  --native-definition notes/2026-11-12-fd2d-metric-current-complete-arb-02-native-definition.json \
  --out-prefix notes/REPLAY-current-accurate-domain --precision 256
```

实际 1030/d076db true0，0.6937043269972492 s，92796 KiB。
完整 binding 为 `d8f0ef5da9239458f1bf46de845332746f7bec16cd55d654d34f799f252388d8`。
R172 左端全部三个分量的 value/xi/xixi 共迹相容；cut 保持仅角导范围。
单位 primitive 的两端精确零与完整实际 H-P 小盒已运行。
原 2b 输入字节未变。

## 本组不支付的量

尚未对当前 2b 场运行完整 n 正性覆盖或全域 forcing polynomial 余项；
没有初始相容预算、退化 cut 可积强迫预算、完整 R125 累积、实际 body、
Cartesian 接缝或 reach 证书。两个示例 E 上界约 .3714 和 .9163，明确是
未完成场的局部链路实例。接续工作应使用实际完整函数和明确覆盖输入，
不能把小核 true0 写成候选已过 tol。
