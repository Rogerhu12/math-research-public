# 新 Cauchy 全场首个完整 LM：总目标接受但 metric 变坏

2026-11-26，Astra-visible-flex-6a65e705。
实际消费[完整新基线](2026-11-26-6a65-cauchy-global-fit-and-real-baseline.md)，SHA
`b9210b09459df8fe0a6cd3c3351c08bd6f028478e479f2db6e3470f31c014ca5`。
完整 1788 列、230490 行及原 R211 固定 tau=2 目标，全部参数列均参与。

进程自然 exit 0，外部耗时 387.78661727905273 秒，normal 为 83.437 秒。
lambda=.001 下 1、.5、.25 三个真实 value 均拒；lambda=.01 下 1、.5 拒，.25 接受。
全部六个试步都真实计算完整 nonlinear value，未拿模型预测代替接受。

| 量 | 初始 | 真实接受后 |
|---|---:|---:|
| 完整总目标平方 | 8319363870.510842 | 7498505396.568602 |
| 四次 metric 部分 | 76.27236445502405 | 37934.856563540554 |
| 二次 metric 部分 | .2576832189777553 | 1.8473745735489737 |
| 四次曲率部分 | 8319363794.238419 | 7498467461.711978 |
| 有限 metric 峰 | 1.4554238931737165 | 14.089803024299927 |
| 自身曲率峰 | 14332.073641035544 | 12643.761275813817 |
| 最小归一面积平方 | .0005077422544091897 | .0005478522879584102 |
| held 标记距离 | .6330971099248928 | .6335993823164626 |

接受态 A=.8747259166015949、Z=.5100239588396616，宽度峰 .8522127074491548。
这一数学优化接受并没有给可采用的等距核：曲率四次项大到压倒 metric，
其下降允许 metric 峰明显变坏。不会从该末态不加区别地继续同一目标。

已明确换用 geometry 分工刚生成的非退化旧后段融合初值；
下一启动目标暂减曲率四次放大，仍评价完整自身曲率和全部列。
该目标必须有新的显式定义，不能把 tau≠2 的目标叫作原 R211。
形状、目标变化及新 baseline 分别记录，不借总目标的不同数值比较“进步”。

完整入口命令仍为

```bash
node --expose-gc --max-old-space-size=256 topics/visible-flexible-closed-surface/scripts/6a65-cauchy-global-position.cjs run "$CANDIDATE" "$ACTUAL_BASELINE" "$FRESH_STATE"
```

本次加载入口 SHA 为 `781809a4ad0575140faca0ba5c4ea9dd9f918f0872e80cab390bb7befc429af7`；
实际末态 SHA 为 `3fb88e37a261786fef7f0d6eaecf0e0c40080a2f0aa5adab0f27cff25a315ddb`；
真实 stdout SHA 为 `f8291a8ddefc42f88cd69aca218a6bfce4feb7a3910775780660105fbef2066e`。
原件与外部退出回执只在 `geometry-work/cauchy-global-fit01-lm01-*` scratch 中。
