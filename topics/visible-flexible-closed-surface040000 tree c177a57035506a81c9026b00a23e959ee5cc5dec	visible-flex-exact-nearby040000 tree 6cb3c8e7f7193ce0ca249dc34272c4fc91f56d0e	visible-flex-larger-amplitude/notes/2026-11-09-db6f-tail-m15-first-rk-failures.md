# M15 已关闭 trial 的首个 RK/root 失败点

状态：**只读数值诊断，原方程与原 floor=.05 不变；不是无解证明，也不是新的 stage 或 shooting 解。**

作者：/root/tail_theory，2026-11-09。依据 root 的明确诊断任务，只读取 coupled_prefix 已关闭并保存的五个失败 stage 输入。没有修改当前 worker、源文件、物理 g、已发布检查点或证书。

## 1. 输入与复放方法

输入为 notes/2026-11-09-db6f-prefix-m15-trial-replay-02-stage-input-call1-iteration0-trial0.json.gz 至 trial4.json.gz，每件约 1.75 KB；各自 SHA256、完整参数、输入状态及 trial 元数据都绑定在输出中。共同配置为同 stem 的 config.json。它们来自 base norm=6.60078222010092 的已关闭 trial 表，不是收敛 shooting 状态。

新脚本 scripts/db6f-tail-diagnose-failed-stage.mjs，SHA256 d46112eb867814128862b276a2775524840dd13ab6692bd6c593279d779fd8a2。
输出 notes/2026-11-09-db6f-tail-m15-failed-stage-diagnostic.json.gz，SHA256 4c26f1876891aa340c8d36fab3b098ca2a302909dc201095781c818cffde29d0。原 JSON 约 2.31 MB，已按根目录规矩 gzip 为 163,024 bytes；没有将数组读入对话。

脚本由原 factory 重建同一 physical source 并使用原 subdividePhysical。以原 fast split engine 的公共 root、rhs 和 geometry 为数学入口。为了记录 RK 子点，从冻结 split 源中原样抽取其 rk4 函数；成功 root 作为 knownRoot 传给原 split RHS。为了记录 Newton 回溯，从冻结 momentum 源原样抽取 solveSPD 和 root 两个函数，绑定原 geometry 和仅加记录的 evaluateL。抽取片段及全部源文件均有 hash。

每个 root 内的成功 evaluateL，独立记录器用同样原运算顺序重算全部角点 D/S/A，并要求其三个最小值与原 evaluateL 逐值相同。原未仪表化 rk4 也在同一个输入重放，要求首个错误字符串一致。五案都在首次 root 失败，因此**没有成功的完整 RK 步可作字节对比**；输出中的成功步计数为零，不能把这一空集合当作额外轨道验证。

## 2. 五个失败都在 stage 入口

设置为 M15、spacing3、N256、每 stage 32 步、parts8、floor=.05。全部位置都是 raw0/segment4 plateau，没有 cusp integration breakpoint。

| 外层 trial 步长 | stage | 原 profile x | 第一失败位置 | 默认初猜 minA | minD | minS |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 32 | .875 | 第0步 k1，stage x=0 | -1.2807030605 | .9998353402 | .9999971076 |
| 1/2 | 32 | .875 | 同上 | -.0848806748 | .9999006665 | .9999977224 |
| 1/4 | 33 | .75 | 同上 | -.1880498498 | .9999211696 | .9999983079 |
| 1/8 | 34 | .625 | 同上 | -.0695548023 | .9999354487 | .9999989003 |
| 1/16 | 35 | .5 | 同上，但失败在 root 内部 | .1623348281 | .9999235667 | .9999991087 |

这里“原 profile x”是该 raw segment 的坐标；stage 自身坐标均为零。不能把它们说成尚未保存的 RK 中间状态。

前四案的原 root 在第一次 evaluateL 就被 A guard 拒绝，D 与 S 远离 floor。最后一案初猜通过 guard，接着发生真正的 Newton 线搜索失败。

## 3. lambda=1/16 的内部路径

该入口半径约 .4738235418774038，背景 w 约 .0072584641261549685。原 Newton 有 9 次已接受迭代评估；最后一次：

$$
A_{\min}=.05000005866277186,\qquad
D_{\min}=.9999254827267974,
$$
$$
\|{\rm residual}\|_\infty=.022098839777481026,\qquad
{\rm scale}=.26435382764343157.
$$

随后原来的 20 个 backtracking 候选都未被接受，原函数抛出 momentum Newton line search failed。残差不是接近 binary64 舍入或原 root 求解容差的量级。观察到的是迭代路径逼近 A=.05 的 guard；尚未得到该目标的实际 root，不能把最后迭代值称为“真实 root 的最小 A”。

## 4. 只在失败点试可行初猜

这部分仍保持同一个 Q、target、r、w、原 floor=.05、原函数和全部 Newton 停止/接受规则。没有把任何替代初猜的结果送入 RK 或 shooting 过程。

试了两类种子：

1. $L=-w^2P_\theta$、均值零，实数模型中 A 恒为 1；实际原浮点评估的 minA 为 .9999999999999999。
2. 保持默认 target 的非均值系数，只调均值到 D/A 线性半空间的明确内部。使用数值可行区间，仅作初猜；仍重新执行全部原 guard。

这两类初猜在五案都通过初始 D/S/A guard，但所有原 root 调用仍失败。A=1 种子的最后已接受迭代如下：

| trial 步长 | 已接受评估数 | 最后 minA | 最后 residual infinity norm |
|---:|---:|---:|---:|
| 1 | 12 | .0500003172 | .0708331685 |
| 1/2 | 18 | .0500005251 | .0863335943 |
| 1/4 | 13 | .0500001667 | .1949475761 |
| 1/8 | 12 | .0500002717 | .0495303622 |
| 1/16 | 11 | .0500002261 | .0119154878 |

mean-only 种子的相同原算法也停在 A 接近 .05、残差非微小的状态。因此，“初次 guard 失败”是前四案直接抛错的原因，但“换一个已可行初猜就恢复整个 trial”并未发生。这与此前已保存 base 节点的默认初猜良好并不矛盾：这里检查的是不同的实际 rejected trial 输入。

## 5. 已确定与未确定

本诊断排除了“需要更深挖入未保存 RK 内点才找到此次第一个错误”的解释；五案在实际 stage 入口就失败。也没有 D/S 近零、cusp 分支或 roundoff fallback 已足够的迹象。

数值结果支持 A=.05 guard 是这些 root 路径的直接限制，但不能仅凭失败迭代证明这个 guard 域内无 root，更不能证明 A>0 的物理正支路无解。root 随后明确授权的较低正 floor 只读探针会另存独立文件，仍不得修改活 worker 或把局部入口结果当作完整 joint 解。
