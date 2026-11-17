# m3 首谷新物理设计：实际尾启动结果与线性余量的边界

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。实际计算 UTC
2026-11-17。承接首谷线性 screen，本批只将 beta[0] 从 3.125 改成
3.625，后面的 159 个 valley controls、双脉冲、warp weights、cut、
背景曲率约束、M8/spacing3/depth8/parts8/steps16 均保留。这个变化是
**新物理 g 的设计**，不是原 g 的 refinement。

## 实际有限尾的终态

在已接受旧 q=.025 联合场的完整 cut height 向量 H 上，两个不同的
显式新 g 初值都未通过原全局 `2e-9` 门槛：

| 新 g 的初值 | 初始 shooting 残差 | 最后 shooting 残差 | 最后 min A | 结论 |
|---|---:|---:|---:|---|
| 直接把旧 normalized state 当任意坐标 | 约 2.95e5 | 175933.90380359834 | .05006183189083893 | 原线搜索失败 |
| 新 g 的实际线性态 + 旧 g 的非线性余项 | 295081.57118532696 | 1.718001964099018e-8 | .055370968986246404 | 原线搜索失败 |

第二个初值显著降低了最终误差，但这仍不是合格的新 q=.025 尾响应，
更不是已完成新前缀–尾部联立。prefix 校正尚未进入。它不能用来
推断这个新 g 的尾部在所有可能 H 上无解，或在调整实际 prefix H 后
仍然失败。

采用原 coupler 的 H warmup 序列 [.2,.4,.6,.8,1] 的一次独立启动，
worker 在第一个 request 后中止，未返回数值响应。保留的证据只有
`Weighted tail worker stopped`，没有退出信号或确定的根因；故机器
记录标记为 `worker_stopped_without_response`，不计作数学失败。
后续重型 DN 计算顺序执行，避免同时构建多份完整尾部。

## 不是遗漏线性高次谐波造成的表面增益

对旧 q=.025 的完整 H，按相同真实物理 factory 分别计算 3,6,...,24
各谐波的线性 T 正性阈值。每个分量使用 128 steps、far 48；把
`|H_j|/H_A,j` 求和只得到一个采样线性三角上界：

| beta[0] | 主谐波比值 | 全 8 谐波三角和 |
|---:|---:|---:|
| 3.125 | .7105395807895121 | .7287595195759206 |
| 3.625 | .42502945935814745 | .4363683090886031 |

所以线性改善并非只来自漏掉较小高谐波。它与真实非线性尾部的
min A 仍有明显差别。三角和小于 1 只说明该**线性 lift 的采样**有
余量，不蕴含非线性分支存在、唯一、可达、闭合或具有相同余量。
R25 的唯一性也只适用于固定 Q 的局部角向 root，不能升级为全尾
边值问题的唯一性。

## 显式新 g 初始化接口

`install_valley_design_initializer.py` 给独立 scratch 源副本加入
`designInitialCheckpoint`。它要求输入 checkpoint 曾通过旧真实尾部
门槛、只允许第一项 beta 改变、检查其余参数和有限维度一致；随后
仅把旧状态当新方程的任意初始坐标。旧 `initialCheckpoint` 的同 g
检查并没有放宽。全部新物理 factory、root、ODE、shooting 方程及
原门槛仍实际执行。

`install_valley_linear_difference.py` 在这个显式接口之后，构造

    new_guess = old_nonlinear_state - old_linear_state + new_linear_state

两份 linear state 都由对应物理 g 的原有限线性 DN 计算，均使用
同一个记录的 H。这只改变初值，不能被解释成跨 g 的物理解传输。
节点 normalized correction 的 L∞ 为 157.2446112391615。

`couple_new_first_valley.py` 在 prefix 端临时装入**字节匹配的旧 port**
以调用原 restart；随后恢复新 port，清空 flow cache，并在新方程
上重新求解 delta 和其余未知量。旧、新 cut 具有同一个解析参数，
但 factory 浮点 r 为 .29999999999999993 与 .3。脚本检查两边各
cut 分量都在解析公式的显式 64 ULP 舍入界内，记录最大原/新差
`5.551115123125783e-17`，没有改写两边原始数值。这个舍入检查不是
精确几何 C² 接缝证明。

在正确接口建立之前，还有两个工程拒绝已保留：原 restart 报
`Physical tail metric differs`；首版显式 wrapper 又因上述 1 ULP
差异拒绝。两次都发生在实际尾求解之前，不计为新物理尾数学失败。

## 复现入口和下一条实际计算

`scripts/resume_m3/continue_valley_design.py` 接受 `--beta0`、
`--amplitude`、旧 prefix/tail/port 三个输入及 source/chart/helper，
自动导出新物理 worker port 并保存全部命令和输入散列。新增的
`--warmup-scales` 直接传给原 coupler 的实际尾 warmup；`--cold-tail`
明确从新 g 的线性态起步，两者都不改接受门槛。

`new_first_valley_start_record.json` 保留这 5 个已结束启动的分类、
精确命令、参数、输出及源 SHA-256，还有逐谐波 scalar screen。
`screen_tail_harmonic_margins.mjs` 是该 screen 的可复现源码。
场、checkpoint 和逐次轨迹不入仓库。

当前正向续算是在新 beta[0]=3.625 下，先真正联立 q=.02，再以上述
新 g 的 accepted prefix H 为基础增幅。它尚未在本记录中宣称完成；
终态另行登记，不能把这一工作安排当成已有结果。
