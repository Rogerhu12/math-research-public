# M24/N512 的真正完整 H、fresh J、height J 与 audit 已返回

## 原求解器的真实接受

2026-11-28 11:34:53 UTC，独立原 worker 从明确未接受的单 ULP 完整初猜返回成功，控制 exec 19975 以 0 退出。实际包位于 `held10-design-work/tail-fullheight-ulp-20261128-a/tail_0001.json.gz`，SHA-256 为 `81f6eb0f5c253c13d6aaaa320adbf95bfc6c59dca7a45b888bacd7b6991b770c`。

这次请求使用原 λ=0.002、M24 前缀的全部 24 个实际 H 系数，幅度因子严格为 1。它保留 M24、N512、spacing=3、物理深度 8、shootingParts=16、全部 1,152 段与 55,344 个未知量，原 16 步 RK、16 步 audit、36 次上限、chord3 和 `2e-9` shooting 门不变。唯一初猜及 trace 路径变化已经单独登记；没有在新 solver 中复用旧 native 行。

原 fresh J 在 iteration 0 给出完整 residual **3.652377088977401e-10**，低于 `2e-9`。真正的全段变分记录状态为 complete；其输入、输出、manifest 和 static metadata 均复核绑定。请求随后实际返回了全部 **1,776** 个有限 height-J 数值，以及原 audit。返回的 55,344 个完整 state 与这次初猜逐位相等；此次没有再作 Newton 修正，并不意味着省略了 fresh J 或 audit。

## 原 audit 的全部标量

| 字段 | 实际返回 |
|---|---:|
| fullD | 7.189741049203119e-7 |
| normalizedFullDefect | 1.964293875679799e-5 |
| minLeading | 0.5559990629241172 |
| minD | 0.9991573422405592 |
| formalCurvature | 8.385038066890585 |
| maxPhysicalPV | 0.00032211040508152867 |
| actualMetric | 1.924760351121307e-11 |
| holonomy | 3.9641307367623766e-19 |

`normalizedFullDefect` 并不小于 `1e-6`；此记录完整保留它，不把它改称连续 metric 证书，也不把 `actualMetric` 的离散数值当作全尾连续界。这里的原有限接受门是完整 shooting 通过、原 audit 实际存在、完整 height J 有限及源/状态身份齐全。后继必须对同一新场的全有限谱和深端 collar 重新支付连续几何门。

## 范围

此包是本次恢复得到的真正 factor=1 原非线性尾响应，补上此前只有 factor=.5 真包的缺口。它仍以 λ=.002 的设计前缀为源；原 8outer 耦合、最终 λ=1、公共 Cartesian 接缝、完整闭图和课题完成均未由本条证明。大场和完整 J 留在仓库外，同名 JSON 保存实际来源、完整哈希和小标量。
