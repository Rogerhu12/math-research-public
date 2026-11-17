# q=.060：局部初值松弛后，原完整实际尾通过原门

2026-11-18，Astra-held10-7322d0de-20261118。

在此前[一邻数初值仍失败](2026-11-18-m3-q060-neighbor-original-gate-failure.md)的完整状态上，新的局部 flow 松弛初猜由原完整 DN 停止测试接受：

$$r_{\rm tail}=1.9930084352226262\times10^{-9}<2\times10^{-9}.$$

原物理参数、cut height、M8/quad128/depth8/parts8/RK16、残差缩放、根域守卫、Newton 和审计均未改变。这里尚未求出 q=.060 的实际前缀，更没有新的闭面或精确圆弧结论。

## 与先前一邻数试验的区别

原始失败的 stage43/mode3 一 ULP 峰已在此前初猜中消去；剩余 stage45/mode12 残差为65 ULP，对应归一值3.012687169522575e−9。该状态真实地被原 Newton 线搜索拒绝过，不能改写成此前已成功。

新的独立源 [probe_tail_residual_initializers.mjs](../scripts/resume_transfer/probe_tail_residual_initializers.mjs) 先复现这个完整原残差，再用预声明的8个松弛系数，对最坏的自由内部状态分量提出初猜。只有下游行已可过门而上游行超门时，才尝试最多5个相邻上游松弛系数。共计算28个局部候选；全局边界和其他状态不改，候选仍必须重新通过完整原 full-Jacobian 残差计算。

最佳候选取 alpha=1/3，未采用第二节点修正：

| 项目 | 数值 |
|---|---:|
| 内部状态 | stage45 / component11 / mode12 momentum |
| 原值 | 330.08195851786417 |
| 新值 | 330.0819585178654 |
| 实际 binary64 改变量 | 正向22 ULP |
| 完整原残差 | 1.9930084352226262e−9 |

这不是只允许一个 ULP 的旧生产重试。它是另一个明确的初值方法，未写入正在运行的 coupler，也没有调整原门。

## 原完整求解与审计

重新执行原 `dn.solve`，保持 `jacobian:true`、`audit:true` 和原全部 solver 选项。原 iteration0 停止测试真实返回 `converged=true`；没有额外 Newton 更新。随后完成完整 Jacobian 与原尾审计：

| 量 | 有限实际结果 |
|---|---:|
| full-Jacobian 数值项 | 208项全部有限 |
| 射击最小A | .5294279749367045 |
| 射击最小D | .9991344478453604 |
| 实际尾采样 metric | 3.984326513162273e−8 |
| 完整 Cartesian Darboux defect | .000281460784485168 |
| normalized full defect | .0008433606917995218 |
| formal curvature | 8.395840687333914 |

完整577×16状态逐位比较，仅上述一个分量与上一失败态不同；全cut height和全部config相同。上一轮stage43的一邻数修正继续保留。最终输出来自原求解器的实际返回，不由局部候选值拼造 `converged`。

这只支付一次有限尾部求解的原接受门。尾审计的全部数值如上保留，不能用射击残差替代 Darboux、连续 metric、收敛或几何证书。下一实际动作是以该尾为初值，接回同一 q=.060 的原前缀—尾联立；新请求的完整残差仍须重新验收。

## 执行身份

实际session64960，exit0，约30.19秒。原尾输出SHA：
`07af0841372e0d113f962ce7306c4a7f2ee557a9dcab40486403b5e66e28bb5d`。
完整命令、源/输入/输出SHA、选定局部行、原history和审计见
[q060_local_relaxation_tail_acceptance.json](../scripts/resume_transfer/q060_local_relaxation_tail_acceptance.json)。全部逐候选表及状态留在scratch，不入库。
