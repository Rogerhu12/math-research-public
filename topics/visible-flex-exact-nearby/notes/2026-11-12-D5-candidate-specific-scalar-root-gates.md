# D5 原点标量门与旧 rounded 第二步根：恢复后实际重算

2026-11-12。本文件区分两个实际输入。执行器丢失后的三个输出均
重新运行获得，所列 SHA 为这次输出的真实字节；不沿用旧未推报告
的 hash。它们不是当前准确仿射第三步对象的替代品。

## 1. D5 原点的连续标量门

输入 `data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz`
SHA256 `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`。
对应原始数值图为 `0dcfb37f...`；本门针对其明确径向对称、准确
高度积分及无限 R33 原函数定义的实际对象。

由完整290个闭样条 span 凸包，不用角节点取最小值，在
$|r|\le\operatorname{binary64}(.24)$ 有向得到

$$
F_z/r\ge .944863615255741,\qquad
F_{r,z}\ge .9427265717734656,\qquad
|F_\theta\times F_r|\ge .8556915581753776.
$$

腰圈商用准确连续延拓。数值端点与丢失前记录一致；新报告路径
字段按下面课题目录内命令保存，所以不冒用旧报告的字节 hash。

报告 `data/phase_ring_continuation/type_fixed_step02_d5_jet_core_scalar_gate.json`
SHA256 `c2484a7843c8afa434d4aea93bef7d9bbab2b0f37988edea2e2baaa0afd745c0`。
源 `scripts/fourfold_phase_core_scalar_gate.py` 保持
`2ccb284015ff136be73771f32d89722de9d2b1fc8e6eef0a309d0f4565d29978`。

## 2. 旧 rounded 第二步自身的局部 simple root

这个旧预测点的 checkpoint 为
`type_fixed_step02_d5_actual_Newton129_step2_probe.npz`，SHA256
`3453e5be05f8ada2dc333d3e2eab5bcbf58d668eea4817ec7cda85913ca77fa7`。
其完整标量输入由已推 checkpoint 实际重新物化，并逐字节恢复为
`type_fixed_step02_d5_actual_Newton129_step2_interval_inputs.npz`，SHA256
`1ef92be77cff11904b656c33b3e74994d6415428160319cd92b5df2717d36e14`。
这与准确实数组合 $S_0+\delta V$ 的族点保持区分。

在该输入自身的明确对称无限原函数上，重新计算根函数
$C=a_rE_r-2a_{rr}E$，严格验证左右异号和 $C_r>0$，故存在唯一根

$$
t\in[\operatorname{binary64}(.2383966),
       \operatorname{binary64}(.2383972)].
$$

根及闭 collar 都在共同样条单元
$[.23750000000000002,.23969803864366687]$ 内。实际有向 collar
为 $[.23815275937499997,.23864104062500002]$，其中

$$
53.12509<K_0'<67.10127,\qquad a>1.09697,\qquad E>1.50725.
$$

程序保留全部角三角函数/DFT 舍入、无穷 primitive 尾及平均乘积
补偿。这只排除 collar 内第二根，未宣称该 rounded 图的整个核心
只剩一对根；准确仿射全族的型别证书不能直接移到它身上。

报告 `data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_root_interval.json`
SHA256 `2f642a3f57f9087978095d7093c713d7b82dc42e1f82ee3254c85b50b321105a`。
源 `scripts/fourfold_phase_root_interval.py` 保持
`07cde6d560bd2681b69bc4a4487178276a21bda8fd3e0a56cdd43800ddd0f840`。

## 3. 该旧 rounded 图的独立控制盒 membership

完整输入与 R57 原点的44个固定字段准确相等。19296个原始 phase
控制值和3个均值参数都在 R57 已认证的独立控制盒中；比较有限
binary64 端点与控制值是准确 dyadic 比较，不再有比较舍入误差。

因此该明确对称的 rounded 图在 $|r|\le\operatorname{binary64}(.24)$
继承同一盒已证的

$$
-N_{\rm raw}\ge .4250393264037103,\qquad
N=N_{\rm raw}/\mathrm{area}\le-.30865948539175136.
$$

这个 membership 不证明它恰在仿射一维曲线上，也不把旧近似
mirror 射线认成当前明确对称图的严格返回。

报告 `data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_N_membership.json`
SHA256 `77ca07c7d7dffd54ebdca40219488c3f816bc293428b6e2819996c8e22af2a9e`。
源 `scripts/fourfold_phase_N_tube_membership.py` 保持
`4d111873e4228bc449a8c4e4f0be1e34f0d30cc87771e3ca20e7cad41a627a93`。
所用 R57 盒证书 SHA 为
`b52537b755e7b5475dc945a5781c0d57a93e71ccdf39ec90891c236fcae2438a`。

## 4. 准确重放命令

在课题目录执行，输出另用 `/tmp`，不覆盖冻结输入：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_core_scalar_gate.py \
  --inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --core .24 --out /tmp/visible-D5-origin-scalar.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_root_interval.py \
  --inputs data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_interval_inputs.npz \
  --left .2383966 --right .2383972 --collar-radius .000244140625 \
  --out /tmp/visible-D5-rounded-step2-root.json

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_N_tube_membership.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz \
  --candidate-inputs data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_interval_inputs.npz \
  --origin-inputs data/phase_ring_continuation/type_fixed_step02_d5_jet_interval_inputs.npz \
  --frozen-direction data/phase_ring_continuation/type_fixed_step02_d5_actual_parameter_direction.npz \
  --tube-certificate data/phase_ring_continuation/type_fixed_step02_d5_parameter_N_interval.json \
  --out /tmp/visible-D5-rounded-step2-N-membership.json
```

三份数据分别补回原点标量门与旧 rounded 点的两项记录。
当前主计算继续使用明确的准确仿射对象与其自身紧根、参数 jet、
整族实/复图表及真实 ODE；这些历史复现不改变主对象。
