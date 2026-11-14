# R209 补充：较大相位充分域及第六态、R208 初值的准确消费

**状态：完整证明，实际 BigInt 有理消费已完成。** 本补充保留
[原 R209](../results/R209-strong-continuous-phase-domain-and-spline-refinement.md)
的 $A+M\le1\Rightarrow\Re Z>1/2$ 命题、实现和第五态证书。
这里另给一个更大的明确充分域，并消费两个不同的已保存实际数组。
没有把第五态证书转借给后续接受态，没有修改任何 LM 搜索域或停止判据。

## 1. 定义与已付种子

完整未归一化相位仍是

$$
\psi=\psi_{\rm seed}+\chi\psi_{\rm tail}
+\sum_jB_j(s)\sum_{k=1}^K
  \bigl(p_{jk}\sin 2ku+q_{jk}\cos2ku\bigr).
$$

沿用原 R209 的准确强 R197 材料 chart、全部相位正弦/余弦列、
非负简单三次基 $B_j$ 及其 $\sum_jB_j\le1$。
种子证书已经连续证明 $|H_{\rm seed}|\le3/4$，因此
$|\psi_{\rm seed}|\le\arcsin(3/8)<2/5$。
准确 R205 参考满足 $0\le A\le6/5<\pi/2$、
$0\le\chi\le1$ 和 $|\chi\psi_{\rm tail}|\le A$。

记

$$
M=\max_j\sum_{k=1}^K(|p_{jk}|+|q_{jk}|).
$$

此处全部保存 binary64 系数都按其准确有理值解释。
固定 seed 的 checkpoint SHA256 为
a1bf7fecdc3e0739b03329efc8886eecbaff2dca3c9843d909c2ac1f94b4275f，
原 64 个整格不等式的账本摘要为
09f4f1dd5676616a58705c4502b239e9e37e3f3bf29a2c70fdb581733f371c26。
本次只引用这份已付证明，没有重算任何 inverse cell 或 seed 不等式。

## 2. 扩展命题与完整证明

**命题。** 在上述完整定义及 $0\le A\le6/5$ 下，充分条件

$$
\boxed{A+M\le\frac{17}{16}}
$$

推出整个闭径向域和全部材料角上的

$$
|\psi|<\frac25+\frac{17}{16}=\frac{117}{80}.
$$

对准确半周积分 $Z(s)=\int_0^\pi e^{i\psi(s,u)}\,du$，于是

$$
\boxed{\Re Z(s)>\frac3{10},\qquad |Z(s)|>\frac3{10}.}
$$

**证明。** 非负基的分区和给完整相位修正绝对值不超过 $M$，
故前一不等式直接来自三项三角不等式。
$\frac{117}{80}<\frac32<\frac\pi2$，所以在该范围中余弦随绝对角度递减。
交错 Taylor 级数在此有下界

$$
\cos\frac{117}{80}
\ge 1-\frac{(117/80)^2}{2}
+\frac{(117/80)^4}{24}
-\frac{(117/80)^6}{720}
=\frac{2256070203359}{20971520000000}
>\frac1{10}.
$$

全部量都是准确有理数；没有依赖浮点三角函数。
积分即给 $\Re Z>\pi/10>3/10$，再由 $|Z|\ge\Re Z$ 得结论。
这仍在同一个右半平面内，故原 R209 的 $\beta=\arg Z$、
$\beta_s=\Im(Z_s/Z)$ 及
$\beta_{ss}=\Im(Z_{ss}/Z-(Z_s/Z)^2)$ 完整 $C^2$ 链直接适用。证毕。

更一般地，可以选择有理预算 $B\ge0$，令 $\gamma=2/5+B\le3/2$，
以及正有理 $c$。只要该六次余弦多项式在 $\gamma$ 的值严格大于 $c$，
$A+M\le B$ 就给 $\Re Z>3c$。本实现显式检查这些条件，
不允许用未验证的任意阈值替换它们。

这是充分域扩展。原单位预算失败不表示 $Z$ 实际为零；
扩展域之外也没有一般不存在性结论。归一化非奇异仍不推出位置图浸入、
等距、曲率上界或全局 reach。

## 3. 第六态与同场径向初值

读取固定 main commit
f0d16da0390bcefe7aadf7d29a0efec743d2caa0 的两个完整实际数组：

| 输入 | 维数、径向基数 | SHA256 |
|---|---:|---|
| notes/2026-11-13-fd2d-R201-R205-amplitude-06-checkpoint.json | 932，$J=30$ | f5363c0bb343c86ae0d2d11f0bb3ee9b3043bf14283c9d6c143de78d71c4aa8a |
| notes/2026-11-13-fd2d-R208-amplitude06-refined-initial-01.json | 1025，$J=33$ | 15531ffdf1dfd5d4b376b4536b90894867ee28973d9d4d93ea18be2b078969b0 |

二者 $K=7$，尾幅度逐位不变。相位正弦列、追加余弦列、幅度索引和准确 knots
全部从各自保存的显式 layout 读取；没有沿用旧维数去解码新数组。

准确得到二者相同的

$$
A=\frac{7199105781811249}{36028797018963968},\qquad
M=\frac{29531975551838278103}{36893488147419103232},
$$

$$
A+M=\frac{36903859872412997079}{36893488147419103232}
\approx1.0002811261692701.
$$

因此两者均明确不满足原来的 $A+M\le1$；
它们满足新域，准确余量为

$$
\frac{17}{16}-A-M
=\frac{2295471284219800105}{36893488147419103232}
\approx0.06221887383072995.
$$

最大行分别是旧径向第 16 行、新径向第 19 行。
这些是两个已保存状态的准确系数消费，不是对当前随后进行的 LM 步骤的声明。

一次纯 V8 系数核耗时 0.010 秒。
没有调用 provider、相位积分、F/J、normal、LM 或 BVP，
没有产生 OS 进程或退出码。完整精确每行范数保存在实际报告中。

## 4. R208 的实际末舍入

准确 Boehm 行对所有 $4K+3$ 个通道相同且非负、行和不超过 1；
因此准确实系数下同场细化不增最大相位行 $L^1$ 范数。
全局切口高度和尾幅度按 R208 明确逐位复制。

另读取已经保存的完整 prolongation 报告

notes/2026-11-13-fd2d-R208-amplitude06-prolongation-01.json，
SHA256 e8069c7da69cbdea261f8e44c189069035fb31e85dc5e667d1dd81e4129bce7f。

其 channel order 是 theta-sine、psi-sine、height、rho、theta-constant、
theta-cosine、psi-cosine。对 $K=7$，全部相位通道为
$7,\ldots,13$ 及 $24,\ldots,30$。
把这些通道已经证明的 value_per_channel 函数误差界准确相加，得到

$$
\|\widehat\psi_{\rm refined}-\psi_{\rm exact\ prolongation}\|_\infty
\le \frac{1705}{36893488147419103232}
\approx4.6214117602194626\cdot10^{-17}.
$$

这里只消费原误差包，没有重跑 Boehm 或其它浮点场比较。
该界远小于上述充分域余量，故也能从父态相位扇区直接转移到末舍入后的同场初值。
此外第 3 节已直接准确读取新数组验证了同一结论。

此处使用的是**函数值舍入界**，不是把共同点两 jet 差冒充系数或全域误差界；
基础数值求值本身的浮点误差不在这个 R208 包中。准确数学函数的非零性，
与以后要付的有限求值误差传播，仍分别记录。

## 5. 完整接口、执行来源与范围

另名源码 scripts/fd2d_R209_extended_phase_sector_certificate.cjs
导出 createR209ExtendedPhaseSectorCertificate(base)。
其中 base 是已经冻结的 createR201PhaseSectorCertificate()；
普通 Node 下省略参数时相对 require 原源。

- certifyState(parameters,layout,seed,options) 沿用原准确参数解码，
  默认取 budgetLimit=["17","16"]、cosineFloor=["1","10"]。
  返回原单位域是否通过、新域是否通过、全部准确余量和新的连续结论。
- consumeSplineRoundoff(prolongation) 只读实际 R208 明确 schema，
  核完整相位通道和不变全局幅度，再准确加和已存函数值误差界。

实际系数核先于末舍入 schema 名称对接。
最后仅将未执行的 roundoff 输入 guard 对齐到实际
fd2d-R201-R205-complete-radial-prolongation-v1；
两个状态的系数检查函数文本逐字未变。最终源的 roundoff 消费真执行 0.001 秒。
中间一次源文本替换因目标字符串拼写不同而在修改前断言停止，
没有执行数值运算、没有修改原冻结源，原实际记录在报告中保留。

完整实际报告见 notes/2026-11-13-fd2d-R209-extended-domain06-and-R208-report.json。
原 R209 的源、证明、第五态报告和闭 manifest 均保持原字节。
本补充不把证书注入任何运行中的 LM gate；后续接受态需要绑定自己的实际数组。

## 6. 机器报告的正则性短句澄清

准确结论是 $\beta$ 和 $e^{i\Phi}$ 为 $C^2$，一阶导数为 $C^1$，二阶导数连续。
原 v1 机器返回中的英文短句 “normalized phase and its two radial derivatives are C2”
不能读作二阶导数本身又是 $C^2$；该短句在此明确纠正为“归一化相位具有连续两 jet”。
原 R209 正文只使用两次微分和 $C^2$ 链，未证明或需要 $C^4$ 正则性。
本扩展返回的正则性说明采用这一准确含义；旧文件和已执行身份保留。
