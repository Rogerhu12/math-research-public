# R55 N 因式和两个完整单元的独立复核

复核者：reproduce-newton。这里只审查 R55 的新 D5 snapshot
`0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`，
没有把原 step02 的连续结论搬过来。

逐式检查通过以下关键点：旋转角中必须保留的常数 $1$；
$T\times e_\phi=e_\gamma$、$T\times e_\gamma=-e_\phi$ 导出的
$N$ 因式；每个横向模的 $\max(|U_m|,|V_m|)$ 向量范数界；
竖直下界和无限原函数尾；真实相位角导数的 Lipschitz gap；
极窄闭 knot 单元中固定同一 span 的 Taylor 系数。
`inner>0,c>0` 连同非负损失项已蕴含代码未另列出的 $Z>0$，
所以正乘子替换没有遗漏符号条件。

对报告中最弱因式单元 0 和实际 root 附近单元 587 重放，
`CoreNGate.evaluate` 的所有字段分别与保存报告**逐字段精确相等**。
再对同一输入、同一闭区间使用另一源 `CoreTarget.evaluate_core` 的
直接叉积公式 $N_{\rm raw}=-a^2F_x\cdot(T\times T_\theta)$，
以及独立的整个 $N_{\rm raw}$ 角 Lipschitz 补偿，得到：

| 单元 | 区间 | 因式法 $N$ 上界 | 直接法 $N_{\rm raw}$ 上界 | 直接法 $N$ 上界 |
|---|---|---:|---:|---:|
| 0 | $[0,.00045259580718443065]$ | $-.35136309932$ | $-.40922868581$ | $-.34529399969$ |
| 587 | $[.23837921545746676,.23881882318620012]$ | $-.35422771525$ | $-.76253991931$ | $-.56338557437$ |

两个不同包络的强弱可以不同，符号和对象一致。直接法同样支付
有向三角/DFT 舍入、无限 primitive 尾和角节点间部分；不是以另一个
普通浮点采样来“证明”原报告。

完整复核数值和双方源 hash 见本目录
`2026-11-12-R55-independent-cell-review.json`。从仓库根将
`PYTHONPATH=topics/visible-flex-exact-nearby/scripts` 后执行以下完整入口：

```python
from fourfold_phase_core_N_interval import CoreNGate
from fourfold_phase_core_interval import CoreTarget
import numpy as np
input_path = ('topics/visible-flex-exact-nearby/data/phase_ring_continuation/'
              'type_fixed_step02_d5_jet_interval_inputs.npz')
with np.load(input_path, allow_pickle=False) as saved:
    frozen = {key: saved[key].copy() for key in saved.files}
factor = CoreNGate(frozen, 256, 4096)
direct = CoreTarget(frozen, 256, 4096)
for left, right in [(0., .00045259580718443065),
                    (.23837921545746676, .23881882318620012)]:
    print(factor.evaluate(left, right))
    print(direct.evaluate_core(left, right))
```

完整592单元的准确覆盖已由 R55 的专用 Fraction checker 支付；本复核
没有重复宣称另跑了所有单元。两个 resumable 程序的依赖 hash 都应在
恢复前核对；当前被冻结的依赖一致，此程序管理事项不改变当前证书。
