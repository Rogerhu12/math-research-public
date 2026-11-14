# R188 严格 quarter primitive：完整非线性例子与实际执行恢复说明

本组消费完整 [R188](../results/R188-quarter-periodic-primitives-and-certified-cell-integration.md) 公式，给出可复用的 cell Taylor 包积分器。已实际完成的例子不是 R187/R190 的主状态或新 BVP/闭曲面。此次失联前说明文档的写入调用没有返回；本文是从完整工具输入保存的 UTF8 恢复文本，不声称其 SHA 是一个未读到的旧文件 SHA。

## 1. 完整函数和真实参数列

固定准确 $p=1/10,q=1/20,s=1/2$，

$$
\Theta=u+ps\sin(2u),\qquad \Phi=qs\sin(2u),
$$

$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi).
$$

实际积分七个完整向量
$T,T_s,T_{ss},T_p,T_q,T_{sp},T_{sq}$。
它们包含非零三角复合的无限 Fourier 尾，未作角投影。全部导数固定物理 $s,u$；例如

$$
T_{sp}=T_\Theta\sin(2u)+T_{\Theta\Theta}\Theta_s s\sin(2u)
+T_{\Theta\Phi}\Phi_s s\sin(2u).
$$

$q$ 列同理保留全部链式项。

## 2. 真实角余项

在复 strip $|\operatorname{Im}z|\le1$ 上，

$$
|\operatorname{Im}\Theta|<6/5,\qquad |\operatorname{Im}\Phi|<1/10.
$$

这是由 $\sinh2<4$、$ps=1/20$、$qs=1/40$ 得到的。
严格简单常数可直接有理证明：

$$
e<11/4,\qquad e^2<121/16<8,\qquad
e^{13/10}< (11/4)(10/7)=55/14<4.
$$

其中 $\sum_{k=0}^3 1/k!=8/3$，其尾不超过
$(1/24)/(1-1/5)=5/96$，所以 $e<11/4$；
$e^{3/10}<\sum_{k\ge0}(3/10)^k=10/7$。
另由 $|\sin z|,|\cos z|\le e^{|\operatorname{Im}z|}$，
$T$ 以及对 $\Theta,\Phi$ 的一二阶偏导每个 Cartesian 分量均小于 4，
$|\sin(2z)|<8$。

由完整链式项，七个 channel 可分别取逐分量复上界

| channel | 上界 $B$ |
|---|---:|
| $T$ | 4 |
| $T_s,T_{ss}$ | 8 |
| $T_p,T_q$ | 16 |
| $T_{sp},T_{sq}$ | 64 |

例如 $T_s$ 不超过 $4(3/20)8=24/5$，
$T_{ss}$ 不超过 $4((3/20)8)^2=144/25$，
mixed 列不超过 $32+96/5=256/5$。

这些函数 entire。对每个实点使用半径 1 的 Cauchy 积分公式，
$|\partial_u^nV|\le n!B$。
令 $A=\pi/2,t=u/A$，可取归一 Taylor 余项

$$
|R_n|\le BA^n|t-c|^n.
$$

实际取 $n=12$、quarter 的 16 个完整 cell、查询 $t_0=1/4$，
即 $u=\pi/8$。余项使用准确 $A$ 的上端点和 R188 (16)–(17)。
这只是角解析余项，不给曲面增加径向 $C^3$ 门。

## 3. 完整包围的算术依据

源 scripts/fd2d_R188_exact_quarter_primitive.cjs，11478 B，SHA256
5c04a135eed859a6d6d583877e53681cdc1dddc6102c913152adfc1913a9f97e。

所有端点是 BigInt 有理数；每次区间运算向外取整至 $2^{-160}$ 网格。
Number 仅用于显示。准确 $A$ 使用 Machin 恒等式
$\pi/4=4\arctan(1/5)-\arctan(1/239)$ 和两份交错级数的首遗漏项，
分别 40 项及 12 项。角支可由
$\tan(2\arctan(1/5))=5/12$、$\tan(4\arctan(1/5))=120/119$
及减角后正切为 1 核定。

sin/cos 的实区间求值用 36 项 Taylor 多项式：
sin 可视为次数 72（该偶次系数为零），余项 $|x|^{73}/73!$；
cos 可视为次数 71，余项 $|x|^{72}/72!$。
完整复合 Taylor 系数由
$(\sin z)'=z'\cos z$、$(\cos z)'=-z'\sin z$
逐阶区间卷积得到，余项仍来自第 2 节完整函数。

竖向 cell 权先准确合为查询左侧的 $t$、右侧的 $t-1$；
x/y 权分别使用准确 prefix/suffix。Fubini 均值未丢失。
没有 DFT，也没有将数值 primitive 的 u 导数代为 T。

## 4. 可复用接口的准确范围

createR188ExactPrimitive() 暴露 F/I 准确数及区间构造器、
consume(packet,query)、analyticFixturePacket() 和 record()。

packet.schema 为 fd2d-R188-complete-channel-Taylor-packets-v1，
逐 cell 给准确 left/right、Taylor order 和每个 channel 的三分量系数区间及余项界。
consumer 核完整 [0,1] 覆盖、查询真实分片和固定物理导数声明。
实际内存 API 使用 F/I 构造的 BigInt 数组；未经解码的 JSON 字符串数组不能直接参与算术。
后续外部 reader 必须逐项解码并核来源、参数和域绑定。

该线性积分器不替 caller 证明 Taylor 输入正确。唯一已执行 producer
是本 note 的明确 entire 例子。R187/R190 主角表示必须给自身同定义的
完整系数盒和余项，再复用本积分器；不能只替换标识充作已付。

## 5. 真实运行与失联状态

原 functions cell g3:52 在 host generation 变化后不可恢复，wait 的实际返回为
“cell belongs to a stale code-mode host generation”，store 结果不可得。
没有给它填 exit 0、137 或完成值。

源码从原完整工具输入逐字恢复到本地，再用 sha256sum 核定为同一 5c04…97e。
独立 wrapper scripts/fd2d-metric-R188-quarter-primitive-check.py
随后实际启动一次 Node 子进程：

- session 19106，首 chunk 11decf，最终 chunk fd5a38；
- 实际退出码 0，38.02164778199949 秒，子进程峰 RSS 84964 KiB；
- 16 cell、12 阶、7 个 channel、21 个积分分量全部返回；
- 最大严格区间宽显示为 $2.270317215141131\cdot10^{-15}$。

完整原 report 已写
notes/2026-11-12-fd2d-metric-R188-quarter-primitive-02-report.json，
14492 B，SHA256
33493d898ce6cfb4067254e1c74b714a7cfe42ff3964e31bee025e7e9a56a043。

原 process receipt 已写同 stem 的 process-receipt.json，
1491 B，SHA256
c21f0d372b5d83cf47fd11ee55034f3cb44e3abcbc1ef3f58f3940092be650e2。
stdout.json/stderr.txt 同时已写；此次恢复没有读到它们的完整字节或 SHA，不补造身份。

原 report 的全部字节当前不在会话内存；新观察摘要仅保存真正已读字段，
不能冒称原 report 或重复执行所得文件。待真实环境恢复后，应核这些原实体；
数学已真完成，无需重算。

第四次环境失联发生在随后说明文档和 closed manifest 写入期间。
functions g2:13 对应这次后处理，最后由 owner 终止阻塞调用；
是否已经部分写入应以后读盘核定。它不是上述 Node 数学进程。

该实际例子证明这个严格消费者可以同时支付完整 nonlinear primitive 和全部真实参数/mixed 列。
主线等距、曲率、reach、闭帽与幅度证书均未由这个独立例子代付。
