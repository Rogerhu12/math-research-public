# R196 — 非均匀简单三次 B 样条与保持完整场的 Boehm 插入

## 1. 目的和准确对象

本结果为 R187/R190/R191 的径向参数提供非均匀三次 B 样条入口。它只改变表示空间；准确插入后的原场并不改善，也不变成新的解。主求解的旧源、当前接受态和有限目标均未被本组修改。

固定相同物理端点 $c<S$，令

$$
q=\frac{s-c}{S-c}.
$$

取准确简单 knots

$$
0=t_0<t_1<\cdots<t_m=1,\qquad m\ge4.
$$

定义 degree $p$ 的有限 Cox–de Boor 基函数

$$
N_{i,0}(q)=\mathbf1_{[t_i,t_{i+1})}(q),
$$

$$
N_{i,p}(q)=
\frac{q-t_i}{t_{i+p}-t_i}N_{i,p-1}(q)
+\frac{t_{i+p+1}-q}{t_{i+p+1}-t_{i+1}}N_{i+1,p-1}(q),
\quad 0\le i\le m-p-1. \tag{1}
$$

只用 $p=3$，basis 数为 $J=m-3$。区间外取零，$q=1$ 也按其连续两 jet 取零。没有端点重复 knot；本入口不能被误读为 clamped cubic spline。

当前 uniform centered B3 正好是

$$
t_i=\frac{i}{J+3},\qquad
N_{j,3}(q)=B_3((J+3)q-j-2). \tag{2}
$$

这里式 (2) 是相同准确 $c,S$ 下的实数恒等式。旧源中 binary64 的 $h=(S-c)/(J+3)$、中心 $c+(j+2)h$ 与新统一 $q$ 计算会有求值顺序差，须单独报告，不能称逐字相等。

## 2. 正则性、端点和局部性

每个 $N_{i,3}$ 非负，支撑为 $[t_i,t_{i+4}]$，内部 simple knots 处为 $C^2$。由式 (1) 逐次微分，

$$
N'_{i,p}=
\frac{p}{t_{i+p}-t_i}N_{i,p-1}
-\frac{p}{t_{i+p+1}-t_{i+1}}N_{i+1,p-1}. \tag{3}
$$

再用一次同式得到二阶导；degree $3$ 的一、二导在 simple knots 的左右极限一致。这也可从以下等价式直接看出：

$$
N_{i,p}(q)=(t_{i+p+1}-t_i)
[t_i,\ldots,t_{i+p+1}]\,(t-q)_+^p. \tag{4}
$$

式 (4) 的 divided difference 只在 knot 变量 $t$ 上取；由其递推式归纳即得式 (1)。当 $p=3$ 时，各截断三次幂都是 $q$ 的 $C^2$ 函数。

在首 span 上，唯一可能触及 $q=0$ 的 cubic basis 为

$$
N_{0,3}(q)=
\frac{q^3}{(t_1-t_0)(t_2-t_0)(t_3-t_0)}.
$$

因此值、一导、二导均在 $0$ 为零。右端同理含 $(1-q)^3$；其他 basis 在端点邻域恒零。零延拓整体为 $C^2$，保持中央及 cut 的两 jet。

任一非 knot 点最多四个 cubic basis 非零；在 knot 上零值/零两 jet 的端支撑可去掉，仍不超过四个。因此在按径向 block 排列的点态残差中，单行最多涉及四个相邻 block，另加原有全局量。R195 的局部 band 结构在这种排列下仍成立；附加全局约束或正则项应按其实际支撑另算。

有限 degree $p$ basis 的总和不超过 $1$。可从 degree $0$ 的总和开始归纳：将式 (1) 按下一级 basis 收集，内部两权之和为 $1$，边端只有一权且在其 basis 支撑上位于 $[0,1]$。

## 3. 准确 Boehm 插入，包括端部 span

在一个旧 span 中插入

$$
t_k<\xi<t_{k+1}.
$$

新 knot 向量是在 $k+1$ 位置加入 $\xi$。令旧系数 $P_i$ 在 $i<0$ 或 $i\ge J$ 时为零。新 $J+1$ 个系数为

$$
Q_i=\alpha_iP_i+(1-\alpha_i)P_{i-1}, \tag{5}
$$

其中

$$
\alpha_i=
\begin{cases}
1,&i\le k-3,\\
\dfrac{\xi-t_i}{t_{i+3}-t_i},&k-2\le i\le k,\\
0,&i\ge k+1.
\end{cases} \tag{6}
$$

只实际计算 $0\le i\le J$；超范围旧系数按上述零值消掉。分母严格为正，中间权位于 $[0,1]$。这套公式也适用于首三段及末三段，不需把端点重复或插入一个不合法的 clamped 定义。

**恒等式证明。** 对 old knot 的每个 cubic basis，有

$$
N_{i,3}^{\rm old}
=\alpha_i N_{i,3}^{\rm new}
 +(1-\alpha_{i+1})N_{i+1,3}^{\rm new}. \tag{7}
$$

插入点在该支撑外时，式 (7) 只是原 basis 不变或移一个索引。插入点在支撑内时，用式 (4) 即可验证。一般地，若 $a=x_0<\cdots<x_{p+1}=b$，在其间插入 $\xi$，令 $A$ 为增广列表去掉最大点，$B$ 为增广列表去掉最小点，则 divided difference 的递推给出

$$
[x_0,\ldots,x_{p+1}]f
=\frac{\xi-a}{b-a}[A]f
 +\frac{b-\xi}{b-a}[B]f. \tag{8}
$$

式 (8) 可由各节点的 barycentric divided-difference 系数逐项核对：对原内部节点 $x$，两系数合并后其新增因子 $x-\xi$ 抵消；新增节点 $\xi$ 的两系数相消；两个端点只出现在一项中。乘以旧 span $b-a$，再除以两项各自的新 span，就得到式 (7) 的两权。若插入点位于该局部首/末 span，相关分母也含 $\xi$，相应权准确为 $1$，正好给式 (6) 的常值分支。

将式 (7) 乘 $P_i$ 后相加，收集新 basis，得到

$$
\sum_{i=0}^{J-1}P_iN_{i,3}^{\rm old}(q)
=\sum_{i=0}^{J}Q_iN_{i,3}^{\rm new}(q)
\quad\text{对所有实数 }q. \tag{9}
$$

两边都是 $C^2$，故其零至二阶导也逐点相等。多个不同内点可逐次插入，期间保留准确有理系数，最终才转 binary64。不能重复插入同一个 knot；重复会降低连续阶数并改变本结果的前提。

每行插入矩阵非负，行和为 $1$，或在隐式零外系数被删去时小于 $1$。所以若所有旧系数落在同一个含零闭区间，则新系数仍在该区间。特别地，统一的半径系数绝对值盒不因插入而变坏。

## 4. 完整 R187/R190 位置场的同函数含义

将每个径向系数行的 channel 依次取为：

- $\theta$ 的全部角模式；
- $\phi$ 的全部角模式；
- 轴向高度；
- 半径修正。

对所有 channel 使用同一个式 (5)。中央曲线、gap、角模式、背景 profile、完整角 primitive、物理 $c,S$ 和独立 cut-height 标量原样保留。

由式 (9)，这些完整径向函数及其 $s$ 两 jet 不变，角导也不变。完整 trigonometric 切向量、它的混合导数以及线性 quarter primitives 因而不变。最终 $X$ 和其完整位置两 jet 在实数算术中一致；半径 $a$ 与目标度量也一致。不存在把旧场借给另一个新物理度量的步骤。

同物理点的精确残差亦不变。若新 factory 随 knots 生成新的径向求积点、权重或目标行，则有限离散目标是新的；不能因完整场同一而把两个不同采样目标说成逐项相同。本组没有启动这样的新 factory 或 BVP。

新增系数方向允许之后离开旧 spline 子空间。恒等式只描述旧状态的注入，并不证明后续求解成功或几何改善。

## 5. 保存舍入的全域标量两 jet 界

设最终准确新系数为 $Q_i$，保存的 binary64 系数为 $\widehat Q_i$，准确误差 $e_i=\widehat Q_i-Q_i$。则

$$
\left|\sum_i e_i N_{i,3}\right|\le \max_i|e_i|. \tag{10}
$$

给隐式外系数 $e_{-1}=e_J=0$，令

$$
d_i=\frac{3(e_i-e_{i-1})}{t_{i+3}-t_i},
\qquad
f_i=\frac{2(d_i-d_{i-1})}{t_{i+2}-t_i}, \tag{11}
$$

各级索引取其完整有限 degree $2$、degree $1$ basis 范围，外值同样为零。由式 (3) 收集系数，保存误差的一、二导分别是系数 $d_i,f_i$ 的低次 B 样条。利用总质量不超过 $1$，

$$
\|\delta F'\|_\infty\le\max_i|d_i|,
\qquad
\|\delta F''\|_\infty\le\max_i|f_i|. \tag{12}
$$

这是整个 $q\in[0,1]$ 上的准确有理界。物理 $s$ 导数再分别除以 $S-c$、$(S-c)^2$。它只计保存系数误差，不计 binary64 basis 求值、旧中心计算顺序、primitive 求积或非线性合成；这些不能混为一个误差来源。

实现将实际输入 binary64 准确转为有理数，全部 Boehm 运算用 BigInt。最终采用最近 binary64、ties-to-even，并将实际输出重新准确转为有理数计算式 (10)–(12)。这是显式舍入，不以容差冒成同系数。

## 6. 源和接口

源：[fd2d-cubic-spline-refinement-R196.cjs](../scripts/fd2d-cubic-spline-refinement-R196.cjs)。

createR196CubicSplines() 返回：

- uniformKnots(J)：准确有理 uniform knots。
- createBasis(knots)：count、knots、jets(q)、exactJets(q)、physicalJets(s,c,S)、exactPhysicalJets(s,c,S)。返回 sparse indices/value/first/second，最多四个 active block。
- insertionMatrix(knots,xi)：准确有理 sparse Boehm 矩阵。
- prolongCoefficients(knots,rows,insertedKnots)：rows 按 [basis][channel]，多次准确插入，最终准确和 binary64 系数、逐项保存误差及全域两 jet 界同时返回。
- evaluateExact(knots,rows,q)：准确有理 channel 两 jet，用于身份消费者。

ordinary jets 是浮点求值。若两个准确 knots 转 binary64 后相撞，浮点入口明确拒绝；exactJets 仍可用。程序不移动 knot、放宽连续性条件或增加一个近零 span。准确定义和浮点评价身份分别保留。

## 7. 实际 J27 注入小核

输入为已保存的真实 R191 J27/433 接受态：

[2026-11-12-fd2d-direct-position-R191-J27-curvature-weight02-01.json](../notes/2026-11-12-fd2d-direct-position-R191-J27-curvature-weight02-01.json)，

Git blob 为 52f36eb8accb540972bf4c8766db19f41c891008。角阶 $K=7$，16 个径向 channel；独立 cut-height 原样复制。

一次纯 JavaScript/V8 实际小核在 51 ms 完成，无 OS 子进程。插入 $q=3/20,23/60$，按输入浮点物理端点显示为 $s\approx0.2191792174807537,0.4021385557841484$。basis 数 $27\to29$，完整向量维数 $433\to465$，不是给旧 uniform factory 直接使用的 state。

13 个公共有理点上，16 channel 的零至二阶导共 624 个准确分量全部相等。端点零两 jet 与独立首/末 span 插入核也通过。所有浮点评价最多四个 active block。

保存 binary64 后，本次公共点的最大差为：

| 对照 | 值 | 物理一导 | 物理二导 |
|---|---:|---:|---:|
| 相同 normalized-q old basis 对 refined basis | $1.39\times10^{-17}$ | $7.22\times10^{-16}$ | $5.69\times10^{-14}$ |
| 旧 centered-uniform 执行顺序对 refined basis | $1.39\times10^{-16}$ | $6.11\times10^{-15}$ | $7.39\times10^{-13}$ |

准确 coefficient 保存误差的全域标量界另在报告中逐 channel 给出。上述实际差仅是所报点的浮点核；没有把它当全域浮点界，也没有重算完整 nonlinear 位置两 jet。完整实数位置同一来自第 4 节恒等式。

检查源：[fd2d-check-cubic-spline-refinement-R196.cjs](../scripts/fd2d-check-cubic-spline-refinement-R196.cjs)。报告含完整准确/保存系数、插入矩阵、身份和误差，不含新的 accepted BVP 或全曲面证书。
