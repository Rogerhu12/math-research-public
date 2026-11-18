# q060：已保存内解的新 H 经具名一步候选获原生接受

接续 `2026-11-18-q060-saved-inner-new-height-tied-peak.md`。
本条新增的是该原内解产生的完整新 H 的**原生有限尾部接受**。
前缀尚未从已保存内解后续接，不能据此宣称新的全域 metric 或闭面通过。

## 局部证据与唯一一步预算

复用原完整候选 baseline；只读检查原行 85/86 的分量 8、9，
没有重做全域 locator。失败输入 SHA-256 为
`845d89e7695d3bf158db56661632e64e38ade4c0d2ea707c32ed1f959eaef8f3`，
局部检查输出 SHA-256 为
`9dafa132672d8f9e73307199d17eccf28dbd441182adbfc84ef40e56edabebcd`。

行 86 的两个残差均是 `-1.1368683772161603e-13`，但其 ULP 数不同：
分量 8 的原 flow 是负方向一个邻数，分量 9 的原 flow 是负方向两个邻数。
本条唯一候选仍将两项**各向负方向移动一个 `nextafter`**：

| 节点/分量 | 原值 | 唯一新值 | 新残差 |
|---|---|---|---|
| 86/8 | `-955.7444723972236` | `-955.7444723972237` | 0 |
| 86/9 | `313.2432945255418` | `313.2432945255417` | `-5.684341886080802e-14` |

没有让分量 9 走第二步，也没有把它误记为已经抵达 flow。
`propose_tail_named_c8_c9_once.mjs` 锁定新 failure、baseline、local
的完整哈希及两坐标，记录原 flow 距离分别为 1、2，实际步数都为 1。
Python native 入口再独立用 `math.nextafter` 核对；其他所有状态、
两端边界、完整 H、参数、rawNode、配置和来源保持不变。

原行 85/86 重算后，唯一候选的完整原 full-Jacobian 残差重放为
`1.8339826971781208e-9 < 2e-9`，与只影响两行的预测逐位相同。
候选脚本不调用 DN 求解器，仍明确标记 `candidate_only=true`、
`solver_success=false`。

## 原 worker 的真实结果

原生入口首版没有执行。执行前发现 JSON 把零解为 Python 整数 0，
而严格二进制比较需要先转为 float；独立 v2 只在已记录的剩余残差
字段上加 `float(...)`，保留位比较和负零区分。
这个修正不改变候选、方程、门槛或允许变动，没有虚构一个失败 run。

会话 24526 真正执行原 worker，observer 记录退出码 0。
请求为同一完整新 H、`jacobian=true,audit=true`；M8、N128、depth8、
parts16、RK16、原 `2e-9` 门及原 sources 不变。
原 worker 在迭代 0 返回 `converged=true`，残差
`1.8339826971781208e-9`，208 个有限 Jacobian 标量和完整原 audit。
1153 个状态节点与候选逐位相同。

真实原生记录位于
`closed_work/q060-newheight-c8-c9-native/seed_tail_0001.json.gz`，SHA-256
`2bbce1774e35c2c9936405b61ff66e8fc2db05968be8da12d1fb85a234a823bd`。
该完整请求与原 `seed-inner-0000-debug.json.gz` 的 candidate H 逐项
相同，因此可以供准确的 post-tail 续接使用。它不能代替原非线性
boundary 检查、后续 outer 校正、完整 metric 与 mean/nonmean seam。

后续按已审的精确接续方案处理原 raw cubic 和旧 DN 锚，继续停在
`tail.solve(candidate)` 后的原控制流；不重启旧 warmup 或 inner0。
缺失的原 message、逐区间 RMS 等诊断不会补造。

紧凑来源记录：
`scripts/resume_transfer/q060_saved_inner_newheight_named_pair_native_execution.json`。
它包含实际运行、命令、完整新 H、两项具名一步、原 native 响应、
零边界修补/IO 映射和全部源码/输出哈希；大数组仅留在 scratch。
