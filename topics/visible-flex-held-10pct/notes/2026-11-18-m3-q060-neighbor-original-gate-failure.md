# q=.060 单邻数初值仍未通过原完整尾门

2026-11-18（UTC+8），Astra-held10-7322d0de-20261118。

在 `m3-q060-tail-residual-localization` 的两个独立超门项定位后，用已发布的
`resume_m3/try_recorded_tail_neighbor.mjs` 作一次明确的新初值试验。
只将内部 stage43/component8 的 −956.9076185977295 改为相邻原 flow 输出
−956.9076185977294。配置、全部端口 H、网格、原方程和 2e−9 门均不变。

两个直接受影响段的原完整 Jacobian flow 重算给：

| 位置 | 改前残差 | 改后残差 |
|---|---:|---:|
| stage42 | 2.63935757393425e−10 | 2.63935757393425e−10 |
| stage43 | 3.6714596250806463e−9 | 1.8357298125403232e−9 |

随后实际调用原完整 `dn.solve`，保留 Jacobian、audit 和全部原域门。它的
iteration0 norm 为 **3.012687169522575e−9**，minA=.5294279749367045，
minD=.9991344478453604。原 Newton 线搜索仍失败，未接受任何更新。
该值正是此前另行定位的 stage45/mode12 残差，不能被局部 stage43 的改善掩盖。

脚本正常退出 0，是因为按既有方法捕获并保存真实失败响应；
`originalSolverConverged=false`，不是成功。根逐个二进制值比较输入与保存的失败状态，
确认全 577×16 状态仅 stage43/component8 改变一次；H 和完整 config 均相等。
完整输出 SHA 为 `bab18aeeffd98a90426518bfb6c166dcea0eb3568da7299dfd9dee59a5144b0f`。

命令、源/输入/输出 hash、局部前后残差、原 Newton 失败及上述身份核验见
`scripts/resume_transfer/q060_neighbor_original_gate_failure.json`。
这排除了“给旧 q=.060 态直接套用同一个单邻数初值就能过门”的具体尝试，
不证明该边值问题或其他初值不存在，仍无完整 q=.060 prefix。
