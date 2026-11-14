# R131 续篇：完整列分批计算与中断任务的准确恢复

2026-11-13，visible-exact-astra-ac0d。

本篇保留两次被系统终止的完整运行记录，给出一个具有独立身份的
小批次 producer，并执行原完整闭盒的逐字段核对。它没有把任何
未完成报告的 `complete` 改为真，也没有从首盒推断整个 \([0,.2]\)
的延拓。

## 1. 实际中断及完整原数据

原 `fourfold_codazzi_positive_weight_cubic_native.py` 的两个进程
实际以 exit code 137、`Killed` 退出：

| 原请求 | 已完整记录的闭盒 | 原旗标 |
|---|---:|---|
| 8192闭角格、全部579行 | 33/579 | `complete=false`, `failure=null` |
| 4096闭角格、原行0至192 | 11/193 | `complete=false`, `failure=null` |

这是进程终止记录。`failure=null` 只表示原 producer 没有捕获到一个
Python 数学门异常，不表示整个请求成功。它也不能用来推断真实解或
其比较屏障不存在。

两个原 native 的全部 checkpoint 字节原样保留；完整原日志压缩
保存。统一记录为
`notes/2026-11-13-Codazzi-positive-weight-cubic-exit137-record.json`，
其中列出准确覆盖、原请求、源 SHA、全部字节 SHA、进程编号和 exit
状态。未完成原报告仍被既有分片消费者拒绝。

## 2. 按完整多项式列分批不改变任何包围

原 `angular_coefficients` 同时处理若干完整有限多项式
\(P_j\)。每个 \(P_j\) 的三列是自身的零、一、二阶角导数，
离散 FFT 沿角坐标轴执行；不同 \(j\) 的列之间没有求和、乘积、
投影或共享误差分配。每一列都带其完整的准确有限 Fourier 支撑。

新 producer
`scripts/fourfold_codazzi_positive_weight_batched_native.py`
将这些完整多项式每八个分为一批。每批调用原同一列运算：准确实
有限中心、同一有向 FFT 蝶形、真实物理频率 \(4n\)、闭角格一、二
阶 Taylor 项、完整三阶 Fourier 余项和原完整 Wiener 误差。

批末只把各多项式的闭包围按原顺序接回列表。径向 Horner 仍在全部
相应角系数到齐后按原式执行。清分母 numerator 的 Fourier 乘法
在此前已经完整完成，因而分批也不改变任何多项式乘积或抵消。

所以这是有限数组的存储安排变化。全部 mean、频率、径向系数、
scalar Taylor 余项、真实参数盒和非线性管费用保持不变。
新程序保留原 producer 源为明确 dependency，并使用独立的新 kind
和自身源 SHA；没有将修改后的程序冒称为旧 producer。

## 3. 已执行的完整原首盒比较

使用相同的192位精度、4096乘积网格和8192闭角格，新程序实际完成
准确首盒
\[
[0,1152921504606847/2305843009213693952].
\]
输出为
`notes/2026-11-13-Codazzi-positive-weight-batched-s10-first-native.json.gz`。
root 将其整行 JSON 与第一项原8192角运行已经算出的首行逐字段
比较，全部相同；比较包括各个权界、五管费用、全部 scalar 模型、
全部模型余项、原 residual/gap/真实系数和全部分区身份。

此处使用原 checkpoint 的一行仅作有限计算的逐字段比较。新首盒
自己的完整 native 和严格屏障才是本次首盒存在结论的输入，不将
原未完成请求标为通过。

新的显式分片消费者为
`scripts/fourfold_codazzi_positive_weight_batched_piece_C0.py`。
它逐片分别接受旧 v2 或本篇新 producer 的准确 kind/source 配对；
新格式还必须有完整八列批次合同。每片均须真正完整、无失败、准确
覆盖其请求，并逐项核查全部 input/dependency 字节。
同一目标、全部完整候选/正权字节、初值、真实 germ、原 partition
index、准确连续端点、一次传播的误差与独立真梯度等检查均保持。

新首盒的五管全部实际通过；完整报告为
`notes/2026-11-13-Codazzi-positive-weight-batched-s10-first-C0-native.json.gz`。
最优管 \(T=1/500\) 的未加权误差小于
\(3.47000628\times10^{-8}\)。其略不同于旧4096角首盒的值来自
这里明确使用的8192角完整包围，不是改换有限候选或误差初值。

root 的实际逐字段比较保存在
`notes/2026-11-13-R131-small-batch-root-equivalence-review.json`。
newton_source 另行逐项审查两份新源码对旧源码的差异、完整列分批的
数学理由及原完整性门，审查文件为
`notes/2026-11-13-R131-small-batch-positive-weight-independent-newton-review.json`。
后者明确不宣称又执行了一次首盒 native。

## 4. 完整请求的恢复方式

失去的原行0至192分成0至95、96至192两个新完整请求重新计算；
原行193至385和386至578的两份未中断计算继续使用原 producer。
四片计划准确覆盖原全部579行。这里只记录恢复计划，不提前宣布
任一在跑请求已经完成。

只有四片各自真正完成后，新分片消费者才可沿同一个连续权传播
一次误差和真实梯度；它仍须通过全部未加权管、正 gap、负曲率和
严格仿射 margin。原中断报告不作为完整片拼入。

完整 \([0,.2]\) 的存在与嵌入、帽/尾/mean 接合和最终共同度量闭面
族的全部要求继续保留。本篇没有以资源中断或有限首盒成功替代它们。
