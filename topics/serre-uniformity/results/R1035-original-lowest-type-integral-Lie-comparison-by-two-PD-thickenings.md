# R1035：原最低型的两次 PD 比较与实际 Lie 整格

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
global_route / o2_high_coefficient / root。

**已证明：R1029 的实际最低惯性型，其原特殊晶体的 Lie 角色格，
整地识别为原 \(\mathcal G_1/R\) 的实际 Lie 格。**
比较保留原 split-Hecke 作用，也保留真正的本地 \(T_5\) 与 deck 作用，
但后两者须使用本篇明确的协变约定。
该识别通过两次合法 PD 厚化得到；它不是只在特殊纤维上的同构，
也不使用可能产生分母的 Frobenius-Hodge 补空间。

本篇只完成实际整格比较。不据此宣称原 MW 饱和空间与 CM jet 横截，
也不预先假设一个尚待构造和核算的交错配对是单位。

## 1. 实际群、晶体和作用约定

保留原
\[
p=12g-1>37,\qquad m=(p-1)/2,\qquad
e_0=m(p+1),\qquad \pi_0^{e_0}=p,\qquad
\varepsilon=\pi_0^m.
\]
令 \(W=W(k)\)，其中可先取包含原全部剩余数据及 tame 角色的
有限未分歧底域，再作基变换。
\(R=W[\pi_0]\) 取其完整整数环。
R1029 已构造真实整 Hecke 幂等元 \(e_1\)，给
\[
\mathcal J[p^\infty]=\mathcal G_1\times\mathcal G_{\rm rest}.
\]
以下从这个已存在的整群因子出发，写
\[
G_0=\mathcal G_1\otimes_R k,\qquad
M=\mathbb D(G_0)(W).
\]

全篇使用 **协变** Dieudonné 晶体；其实际 Hodge 序列是
\[
0\longrightarrow\omega_{\mathcal G_1^t}
 \longrightarrow \mathbb D(\mathcal G_1)
 \longrightarrow \operatorname{Lie}\mathcal G_1
 \longrightarrow0.
\tag{1035.1}
\]
它的商上是实际群自同态的 Lie 作用。
原 split-Hecke 为 Rosati 自伴，故 \(e_1\) 亦自伴；
原主极化将这个 BT 因子与其对偶整地识别。

由 R1029 的整惯性角色投影，\(M\) 分为仅有的两格，
角色集合为 \(\{\xi^m,\xi^{-m}\}\)。
其中一格的模 \(p\) 恰为 Hodge 子空间；记它为 \(M_H\)，
另一格记为 \(M_L\)。因此
\[
\boxed{\quad
M=M_H\oplus M_L,\qquad
\operatorname{Fil}_k=M_H/pM_H,\qquad
M_L/pM_L\simeq\operatorname{Lie}G_0.
\quad}
\tag{1035.2}
\]
这里最后一项是 R1023 原 \(f_s\) 所在的 Picard 切空间，
不新选一个抽象同维空间。

为避免混用自然曲线拉回与协变作用，下面不靠
\(M_H\) 的正负名字作推理：
从 \(M_H\) 到 \(M_L\) 的 graph 系数角色恰为
\(\xi^{2m}\) 或 \(\xi^{-2m}\)，两种约定的证明完全相同。
原半线性下降数据始终随比较一起运输。

若借主极化把 \(M\) 写成曲线的一阶 crystalline cohomology，
对 Jacobian 的真实自同态 \(u\)，协变作用对应
\((u^\dagger)^*\)。故 split-Hecke 的旧作用不变；
对 deck \(\delta_*\)，则应使用
\[
(\delta^{-1})^*,
\tag{1035.3}
\]
而不能把自然 \(\delta^*\) 无声改称实际 Lie 作用。
原 Serre 归一仍由
\(\operatorname{Res}(f_s\omega_s)=-2\) 固定，不另改变配对尺度。

此外，所用群确在 Zink 的 formal 范围内。晶体 Frobenius \(F\)
半线性且与惯性作用相容；\(p\) 在阶 \(p+1\) 的角色上取逆，
故 \(F\) 交换 \(M_H,M_L\)。协变 Hodge 满足
\(VM/pM=\ker\bar F\)，于是 \(F(M_L)=M_H\)。
另有 \(F(M_H)\subset pM_L\)，而 \(V\) 也交换两格，
由 \(FV=p\) 得反向包含。因此
\[
F(M_H)=pM_L,\qquad F^2M=pM,\qquad V^2M=pM.
\tag{1035.3a}
\]
所以 \(G_0\) 的 \(F,V\) 均 topologically nilpotent，
它及上述实际形式提升适用 Zink 的 formal BT 比较。
这里只是整格等式；没有预设算术线性化 Frobenius 的平方符号。

## 2. 第一次厚化：实际群模 \(\varepsilon^2\) 是常数群

置
\[
I=(\varepsilon^2)=(\pi_0^{2m}),\qquad
S=R/I\simeq k[\pi_0]/(\pi_0^{p-1}).
\tag{1035.4}
\]
这里 \(p\in I\)，所以 \(S\) 的特征为 \(p\)。
在 \(S\to k\) 的核 \(J=(\pi_0)\) 上取
\[
\gamma_n(x)=
\begin{cases}
x^n/n!,&n<p,\\
0,&n\ge p.
\end{cases}
\tag{1035.5}
\]
这是一个真正的 nilpotent PD 结构。
\(n<p\) 的分母可逆；所有在加法或复合公理中出现的
总次数至少 \(p-1\) 的项均因 \(J^{p-1}=0\) 消失，
所以越过 \(p\) 的公理也相容。
它与基底上 \(p=0\) 的 canonical PD 相容，并由 tame 下降保持。

晶体的 PD 基变换给
\[
\mathbb D(G_0)(S)=M\otimes_W S.
\tag{1035.6}
\]
实际 \(\mathcal G_1/S\) 的 Hodge 子空间约化为 \(M_H/p\)。
因此相对于 (1035.2)，它唯一地写成 graph
\[
\phi:M_H\otimes S\longrightarrow M_L\otimes S,
\qquad \phi\bmod\pi_0=0.
\tag{1035.7}
\]
令 \(\sigma(\pi_0)=\xi\pi_0\)，\(\sigma\) 固定 \(W\)。
实际 Hodge 下降相容要求 \(\phi\) 的各系数具有角色
\(\xi^{2m}\) 或 \(\xi^{-2m}\)。

但 \(S\) 中可出现的 \(\pi_0\) 次数只有
\(0,\ldots,2m-1\)。角色 \(2m\) 不在其中；
角色 \(-2m\bmod e_0=e_0-2m\) 也不在其中，因为
\(e_0>4m\)。故
\[
\boxed{\quad \phi=0.\quad}
\tag{1035.8}
\]

真正的常数群 \(G_0\times_k S\) 在同一个晶体中也有 Hodge
子空间 \(M_H\otimes S\)。Grothendieck–Messing 的对象与态射
分类遂给一个保持原特殊纤维标记的唯一同构
\[
\boxed{\quad
\mathcal G_1\otimes_R S\simeq G_0\times_k S.
\quad}
\tag{1035.9}
\]
这是实际群模 \(I\) 的同构，不是只由特殊纤维相同而猜出的同构。
也不需要事先构造一个新的未分歧 CM abelian variety。

## 3. 第二次厚化：\((\varepsilon^2)\) 上的完整 PD 结构

现在在 \(R\to S\) 的核 \(I\) 上取通常的有理表达式
\[
\gamma_n(x)=x^n/n!.
\tag{1035.10}
\]
必须验证它实际落在 \(I\)，而非只在 \(R[1/p]\) 中有意义。
用 \(v_{\pi_0}(\pi_0)=1\)，对 \(x\in I\) 有
\[
\begin{aligned}
v_{\pi_0}(\gamma_n(x))
&\ge2mn-e_0v_p(n!)\\
&\ge2m+(n-1)\left(2m-\frac{e_0}{p-1}\right)\\
&=2m+(n-1)\frac{m(p-3)}{p-1}.
\end{aligned}
\tag{1035.11}
\]
这里使用 \(v_p(n!)\le(n-1)/(p-1)\)。
最后一项至少为 \(2m\)，且随 \(n\) 趋向无穷。
故 (1035.10) 是 \(I\) 上 topologically nilpotent 的 PD 结构；
PD 公理可在无 \(p\) 挠的分式环中核对再限制回来。

该结构与 canonical \((p)\)-PD 相容。
每个 \(p^aR\)（\(a\ge1\)）也是 PD 子理想：
对 \(x\in p^aR\)，
\(v_p(x^n/n!)\ge an-v_p(n!)\ge a\)。
于是可在每个 \(R/p^aR\to S\) 上应用 nilpotent PD 比较，
再取相容极限；这同时给全部态射的比较。

使用的 PD 基变换图准确是
\[
\begin{matrix}
(W,(p))&\longrightarrow&(R,I)\\
\downarrow&&\downarrow\\
k&\longrightarrow&S .
\end{matrix}
\tag{1035.12}
\]
**没有使用 \(R\to k\) 的核 \((\pi_0)\) 上的 PD 结构。**
大分歧情形在那个更大理想上的通常阶乘除法并不自动整；
本篇只使用已逐项验证的 \(I=(\varepsilon^2)\)。

将 (1035.9) 与 (1035.12) 合并，得到实际群的晶体评价
\[
\boxed{\quad
\mathbb D(\mathcal G_1/S)(R)
 \simeq\mathbb D(G_0\times_k S)(R)
 \simeq M\otimes_W R.
\quad}
\tag{1035.13}
\]
实际提升 \(\mathcal G_1/R\) 的 Hodge 子格在这个整格中
约化为 \(M_H\otimes S\)，故为一个 \(I\)-值 graph
\[
\Phi:M_H\otimes R\longrightarrow M_L\otimes R,\qquad
\Phi(M_H)\subset I(M_L\otimes R).
\tag{1035.14}
\]
这里的 graph 可以非零；没有把实际提升宣称为常数提升。

## 4. 实际 Lie 格的整同构和态射相容性

由 (1035.14)，包含再取商给
\[
\boxed{\quad
M_L\otimes_W R
 \ \xrightarrow{\ \sim\ }\
 (M\otimes_W R)/\operatorname{Fil}
 \ \xrightarrow{\ \sim\ }\
 \operatorname{Lie}\mathcal G_1 .
\quad}
\tag{1035.15}
\]
第一个映射的逆只是沿 graph 的投影：
\(h+\ell\mapsto\ell-\Phi(h)\)，全在 \(R\) 中。
因此没有 \(\pi_0\) 或 \(p\) 分母，约化到原特殊纤维就是
(1035.2) 的标记识别；反转 \(p\) 后亦是实际 generic Lie 的同构。

设 \(T\) 为原 \(\mathcal G_1/R\) 的一个整自同态，
其特殊作用与 tame 惯性交换。
它的特殊晶体作用保持 \(M_H,M_L\)。
第一次 GM 比较的态射部分保证：
在 (1035.9) 下，实际 \(T\bmod I\) 正是常数特殊自同态。
第二次晶体比较的自然性进一步保证：
实际 \(T\) 的晶体矩阵是同一个 \(M\) 上的矩阵经 \(R\) 基变换。
实际 \(T\) 也保持实际 \(\operatorname{Fil}\)。
所以 (1035.15) 与 \(T\) 的真实 Lie 作用相容。

这适用于全部原 split-Hecke 对应与其整 \(p\)-进完备化。
亦适用于下列已存在的实际对应：

- 本地 \(T_5\)：\(p\equiv2\bmod3\) 时
  \(\sqrt[3]{4}\in\mathbf Q_p\)，由原 canonical 曲线运输到
  \(X_1\) 的 \(T_5\) 是真实 \(\mathbf Q_p\) 对应，与 \(p\)-惯性相容。
  不因此宣称它是原 \(X_1\) 上的 \(\mathbf Q\) 对应。
- 原 deck \(\delta_*\)：在包含 \(\zeta\) 的未分歧底环定义，
  与 \(p\)-惯性相容，采用 (1035.3) 的协变作用。

半线性算术下降的相容性按同一个自然性论证处理：
先对基环自同构作 pullback，再应用态射分类。
含外部 \(W\) 系数的线性组合可随后作用于晶体与 Lie 格；
不把这种组合自动称为 BT 自同态。

## 5. 本条支付的内容与仍需完成的比较

(1035.15) 给出了可用于实际 generic Lie 的整搬运，
从而以后若在 \(M_L\) 上构造一个原 Hecke 平衡的整双线性形式，
可以通过此式将它搬到实际 Lie 格，并保留其特殊纤维读数。
这填补了“仅有特殊纤维配对”与“实际饱和 MW 格”之间的比较步骤。

但配对本身、算术 Frobenius 的实际下降与平方、
全部 \(F_0\) 作用及同源重数上的相容性，
以及它对 R1023 原首 log 和 R1032 原 jet 的实际取值，
仍须各自证明。
本条不从 \(F_0\) 上一个循环子空间的交错性，
直接推断多重同源因子的整个 MW 空间均被消去。
也不把 R1033 整个类型块的 \(M=1\) 自动传给指定 Néron 商格。

本条从头到尾没有选用 Frobenius-Hodge 补空间作为整补空间；
真正使用的是 (1035.14) 已证的 graph 与 \(M_L\)。
Serre 主目标仍 OPEN。

## 来源与审核

- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)：
  原真实整 BT 因子、两种特殊惯性角色、纯 Hodge 与原 bottom 格。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)、
  [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)：
  原 Picard 基、Serre 归一及后继要比较的真实两列。
- Thomas Zink, *The display of a formal p-divisible group*,
  Astérisque 278 (2002), 127–248，
  [已实读作者全文](https://www.math.uni-bielefeld.de/~zink/display.pdf)。
  本文使用作者页码的 Theorem 46 后 topological PD remark、
  (74)–(75) 的基变换、Theorem 48 的对象和态射分类、
  Theorem 94/Corollary 95 的 formal BT 晶体比较，
  以及 Theorem 103 的完备局部环范围。
  对应 PDF 第43–45、89、93–94页。
  未声称本轮另行取得 Messing 原书全文。

global_route、o2_high_coefficient 与 root 纸核两个不同 PD 理想、
全部阶乘赋值、PD 子理想、角色缺失、准确 basechange 图、
实际 graph 商和协变/Rosati约定；root 亲读上述 Zink 原文。
没有数学执行或旧窗口重算。
