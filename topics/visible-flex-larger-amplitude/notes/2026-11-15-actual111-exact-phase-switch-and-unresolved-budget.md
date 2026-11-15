# actual111：准确相位换门完成，较小预算诚实保留未付叶

/root GPT-6 Astra Pro（AI-assisted），2026-11-15。R281证明先前已直接登记；本笔记只记录新有理配置的实际公开执行。

## 实际运行

[run43685039861](https://github.com/Rogerhu12/math-research-public/actions/runs/43685039861)，source `77d65ad2b07185f8b3c4caec87aae5f62d846e17`，job132723637032，attempt1，Python3.12.14。两个完整执行均与提交的解析分区相符，`analytic_comparison_failures=[]`，job实际success。

同一组输入为 $p_0=(1,0,0)$、$q_0=(1/2,0,2)$、$n_0=(-3/5,0,4/5)$、$m_0=(3/5,0,4/5)$，四误差半径0、$τ=6/5$。两次均sqrt-bits128、max-cells16，只有最大深度分别为2和1。它是新的有理条件配置，不是本课题实际闭场数据。

| 实际执行 | 已测单元 | 二分 | 终止叶 | 已付 | 未付 | 全相位条件门 |
|---|---:|---:|---:|---:|---:|---|
| complete-depth2 | 8 | 3 | 5 | 5 | 0 | true |
| limited-depth1 | 4 | 1 | 3 | 1 | 2 | false（本次预算未完成） |

两次旧整圆距离、moving、fixed、joint四门都false，旧整圆normal-chord门也false；新区间算法确实被执行。深度2并非退回旧全圆证书。

## 实际完整五叶

| 相位图 | 闭区间 | 实际支付门 | 左/右端点多项式值 | 内部不同实根数 |
|---|---|---|---|---:|
| t | $[-1,1]$ | moving | $41/25,41/25$ | 0 |
| u | $[-1,-1/2]$ | moving | $41/25,29/100$ | 0 |
| u | $[-1/2,0]$ | distance | $9/64,49/100$ | 0 |
| u | $[0,1/2]$ | distance | $49/100,9/64$ | 0 |
| u | $[1/2,1]$ | moving | $29/100,41/25$ | 0 |

每叶都由严格端点和准确有限Sturm根数共同支付，覆盖共享端点；不是角采样。表中数值是乘正分母后的原多项式值，不与真实距离余量混用。

在u根区间 $[-1,1]$，moving的两个端点均 $41/25>0$，但实际变号数由2降至1，所以内部有一个不同实根，严格门false；fixed与joint同样计1，亦false。距离项两端均 $-51/25<0$，未尝试输出未经定义的根数。内部偶重零没有被忽略。

深度1实际只支付整个t图；u的 $[-1,0]$ 和 $[0,1]$ 两叶保留为 `maximum_dyadic_depth_reached`，没有删失队列，没有把有限预算失败改写成几何失败。两次都明确 `finite_budget_failure_is_geometric_failure=false`。

## 原运行和输出身份

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 实际紧凑报告（含末LF） | 7898 | `7279b591b8ccba81abf2d351afbf7288f398cee62cccfc557fbdeb8d3c50db2e` |
| depth2完整临时输出 | 38169 | `876be9cda66d4bfb4f87909f69fc555528c3c46e59a6b49b844d7b2af3bdc96c` |
| depth1完整临时输出 | 28682 | `010f91f30fa363971850b260a9a033f49c512f6148ba36330539579729358cdc` |
| 实际job log | 42421 | `b52c13fec1473c85a6e54effe5901dca9c1d8ffb60ae1042ce7c0d87cd5493d3` |

input SHA `d0e2158daf0f4fd063d629a3e2cdce4e4f64029b2b76193929b38947449d360d`；request `ee9d115df498362d48507a7ee89a5f6be6345619fcb1eec611e8a2feaec8ffe7`；workflow `7f5ff78090a563bf818d9584e50e394c8396aa133e499a4f3aa379773c3fe259`。

执行三源：R281 `f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537`、R280 `c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466`、原R62 `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6`。root只读取原短log/JSON及字节hash，无本地数学重算；可重算完整输出不存Git、artifact或Release。

## 范围与继续

没有旧fixture、没有相位采样、没有native/BVP/RHS/J/ODE调用；`full_surface_certified=false`、`actual_reach_certified=false`。本次只表明正确连续球假设下的相位区间换门实现符合该完整解析例。真实闭面仍需实际求解、全空间块对清单、正确位置/单位法向球与全部曲率/同g/幅度条件；不能将本条件例冒成当前闭场或reach。后续直接补实际闭面流水线所需的连续球接口，不增加旧案例重审门。
