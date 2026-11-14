# 同一显式对称 step02 图的紧根区间

状态：已用既有有向 simple-root 程序补算，不替换原宽根/实 collar
证书。仍是 snapshot `bd9b4d14...` 所定义的无限角图，未作 Gaussian
平滑，未改候选。

新报告 `data/phase_ring_continuation/type_fixed_step02_symmetric_root_tight_interval.json`
把真实 target 根包含于输入的两个 **binary64 实数端点**

$$
[.23836991573145,\ .23836991573148].
$$

若要完全以十进制有理数书写，可向外放宽为

$$
.2383699157314499<t<.2383699157314801.
$$

左端 $C$ 的上界为 $-3.025357742103551\cdot10^{-12}$，右端
$C$ 的下界为 $4.000466624631826\cdot10^{-12}$；整个窄区间的
$C'$ 下界是 $300.54150306970865$。故这仍是无限原函数的真实唯一
局部根证书，不是有限角近似的 root 拟合。

当前点值区间的 $C$ 宽度约 $2\cdot10^{-12}$，相当于根宽约
$7\cdot10^{-15}$；继续把端点机械压缩会遇到当前 binary64 区间算术
的舍入宽度。这不影响原证书中固定实 collar 与共同 knot span。

重放命令：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python topics/visible-flex-exact-nearby/scripts/fourfold_phase_root_interval.py \
  --inputs topics/visible-flex-exact-nearby/data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz \
  --left .23836991573145 --right .23836991573148 --quarter-nodes 256 \
  --out /tmp/visible-root-tight.json
```

报告 SHA256：
`3d6018b0a17e1ea5ec1b21fd28d886bc7454a91973fbcfd0cfaa3d7ee4ecc66b`。
所用既有源 SHA256：
`07cde6d560bd2681b69bc4a4487178276a21bda8fd3e0a56cdd43800ddd0f840`。
该根可供同对象的高精度局部 Taylor 项核对；本证书不把有限原函数
Taylor 系数或旧近似镜像返回图自动提升为无限对象的已付数据。
