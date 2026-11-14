# 抽象 Lefschetz 正性不控制 primitive 最小逆：五层完整反例

日期：2026-11-13（UTC）。作者：0c/root；AI-assisted，GPT-6 Astra Pro。
状态：已证明的适用范围反例；不反驳正权 Boolean 模型的相邻 Gram 猜想。

本文核查一个可能的结构捷径：能否只由 Poincaré 对偶、Hard Lefschetz 和全部 Hodge–Riemann 正性，推出本文使用的 primitive Moore–Penrose 相邻序？答案是否定的。下面保持层维数 $(1,4,6,4,1)$、一个酉反射、真实 Hilbert 伴随和完整层逆，给出最佳相邻常数趋于无穷的明确族。中间互补层映射及全部 primitive 交形式甚至不随参数改变。

这里构造的是抽象有限分级模块。本文没有将它写成 $\sum_i a_iE_i$，不能把结论称为四位正权 Boolean 反例。原正权张量模型、原无限尾和普通 ISP 均未由本稿解决或否定。

## 1. 五层 Hilbert 空间与固定对偶

令
$$
\mathcal H=\bigoplus_{r=0}^{4}\mathcal H_r,\qquad
(\dim\mathcal H_0,\ldots,\dim\mathcal H_4)=(1,4,6,4,1),
$$
各层用标准复 Hilbert 内积，层间正交。
用同一标准坐标识别 $\mathcal H_1,\mathcal H_3$ 与 $\mathbb C^4$，其基记为 $e_0,e_1,e_2,e_3$；$\mathcal H_2=\mathbb C^6$ 的基记为 $f_0,\ldots,f_5$。

置
$$
J=\operatorname{diag}(1,-1,-1,-1),\qquad
R_2=\operatorname{diag}(1,-1,-1,-1,1,1),
$$
$$
E=\begin{pmatrix}I_4&0_{4\times2}\end{pmatrix},\qquad
S=\operatorname{diag}(\sqrt6,\sqrt2,\sqrt2,\sqrt2).
\tag{1.1}
$$
定义全空间线性酉对合 $R$：它按上述坐标恒等交换 $\mathcal H_0,\mathcal H_4$ 及 $\mathcal H_1,\mathcal H_3$，在 $\mathcal H_2$ 上取 $R_2$。因而 $R^*=R=R^{-1}$，中间层的正负指标均为 $3$。

对应的非退化 Hermitian 次数配对为
$$
\mathcal B(x,y)=\langle Rx,y\rangle.
\tag{1.2}
$$
它只在次数互补的两层之间非零。本文所称 Poincaré 对偶就是这个明确非退化配对，不假设尚未构造的乘法环。

## 2. 保持交形式的参数族

对任意 $t\ge0$，令 $B_t$ 在 $\operatorname{span}\{e_0,e_1\}$ 上为
$$
B_t=
\begin{pmatrix}
\cosh(t/2)&\sinh(t/2)\\
\sinh(t/2)&\cosh(t/2)
\end{pmatrix},
$$
在 $e_2,e_3$ 上为恒等算子。它是实对称、严格正定的矩阵，且直接相乘给
$$
B_tJB_t=J,\qquad
B_t^2\big|_{\{e_0,e_1\}}=
\begin{pmatrix}\cosh t&\sinh t\\\sinh t&\cosh t\end{pmatrix}.
\tag{2.1}
$$
定义
$$
A_t=SB_tE:\mathcal H_2\longrightarrow\mathcal H_1.
$$
则
$$
A_tR_2A_t^*
=SB_tJB_tS
=SJS
=\operatorname{diag}(6,-2,-2,-2)
=:T.
\tag{2.2}
$$
特别，$T$ 与 $t$ 无关。

现在定义降低一次数的算子 $D_t$，其四个层块依次为
$$
\begin{aligned}
D_{1,t}&=2e_0^*:\mathcal H_1\to\mathcal H_0,\\
D_{2,t}&=A_t:\mathcal H_2\to\mathcal H_1,\\
D_{3,t}&=R_2A_t^*:\mathcal H_3\to\mathcal H_2,\\
D_{4,t}&=2e_0:\mathcal H_4\to\mathcal H_3.
\end{aligned}
\tag{2.3}
$$
各未列块均为零。由定义
$$
RD_tR=D_t^*.
\tag{2.4}
$$
若 $\mathfrak c$ 是所有标准坐标中的复共轭，则 $C=R\mathfrak c$ 是反线性等距对合，且同样满足 $CD_tC=D_t^*$。这里没有把反线性 $C$ 与线性 $R$ 混用。

记真正 Hilbert 伴随升算子为
$$
L_t=D_t^*.
$$
由 (2.4)，$RL_t=D_tR$，从而
$$
\mathcal B(L_tx,y)=\mathcal B(x,L_ty).
\tag{2.5}
$$
因此 $L_t$ 对固定 Poincaré 配对自伴。

## 3. Hard Lefschetz 与全部 Hodge–Riemann 正性

在全部互补层上，
$$
L_t^2:\mathcal H_1\longrightarrow\mathcal H_3
=A_tR_2A_t^*=T,
$$
而
$$
L_t^4:\mathcal H_0\longrightarrow\mathcal H_4
=(2e_0^*)T(2e_0)=24.
\tag{3.1}
$$
这些都是可逆映射；次数 $2$ 的互补映射是恒等。
故所有 $0\le r\le2$ 上的
$$
L_t^{4-2r}:\mathcal H_r\longrightarrow\mathcal H_{4-r}
$$
都为同构，即完整 Hard Lefschetz 性成立。

定义各 primitive 空间
$$
P_t^r=\ker\!\left(
L_t^{5-2r}:\mathcal H_r\longrightarrow\mathcal H_{5-r}
\right),\qquad 0\le r\le2,
$$
其中超出 $0,\ldots,4$ 的层为零。
它们可以逐个准确算出：
$$
P_t^0=\mathcal H_0,
$$
$$
P_t^1=\ker\bigl((2e_0^*)T\bigr)
=e_0^\perp,
$$
$$
P_t^2=\ker(A_tR_2)
=\operatorname{span}\{f_4,f_5\}.
\tag{3.2}
$$
最后一步用 $SB_t$ 可逆及 $E$ 只删除末两坐标。
同时
$$
P_t^1=\ker D_{1,t},\qquad
P_t^2=\ker D_{2,t}.
\tag{3.3}
$$
所以这些 primitive 空间也正是下面最小逆所用的真实删除核；没有更换 primitive 定义。

考虑通常符号约定下的全部 primitive Hermitian 交形式
$$
Q_t^r(x,y)=(-1)^r
\mathcal B(L_t^{4-2r}x,y),\qquad x,y\in P_t^r.
$$
由 (3.1)–(3.2)，准确得到
$$
Q_t^0(x,x)=24\|x\|^2,\qquad
Q_t^1(x,x)=2\|x\|^2,\qquad
Q_t^2(x,x)=\|x\|^2.
\tag{3.4}
$$
三者均严格正，而且不随 $t$ 变化。
这完整验证了各次数的 Hodge–Riemann 正性，非仅度数一的一个标量不等式。

## 4. 真实完整层 Moore–Penrose 逆

固定出生 $s=1$，高度为 $h=4-2s=2$，源空间
$$
K=P_t^1=e_0^\perp
=\operatorname{span}\{e_1,e_2,e_3\}.
$$
其内积就是原标准内积。记 $P_K$ 为其正交投影，并定义
$$
J_{n,t}
=\left(D_t^n/n!\big|_{\mathcal H_{1+n}\to\mathcal H_1}\right)^\dagger
\big|_K,\qquad
\Gamma_{n,t}=J_{n,t}^*J_{n,t},\qquad n=0,1,2.
\tag{4.1}
$$
对 $n=1,2$，括号中的完整层映射都满射；先取其整个最小逆，再限制源为 $K$。

### 4.1 中间层

$A_t$ 满行秩，故
$$
J_{1,t}=A_t^*(A_tA_t^*)^{-1}\big|_K,\qquad
\Gamma_{1,t}
=P_K(A_tA_t^*)^{-1}\big|_K.
$$
由 $EE^*=I_4$，
$$
A_tA_t^*=SB_t^2S,\qquad
(A_tA_t^*)^{-1}=S^{-1}B_t^{-2}S^{-1}.
\tag{4.2}
$$
在前两个坐标上，
$$
B_t^{-2}
=\begin{pmatrix}\cosh t&-\sinh t\\-\sinh t&\cosh t\end{pmatrix}.
$$
因此在 $K$ 的基 $e_1,e_2,e_3$ 中，
$$
\boxed{
\Gamma_{1,t}
=\operatorname{diag}\!\left(
\frac{\cosh t}{2},\frac12,\frac12
\right).
}
\tag{4.3}
$$
特别，不能先压缩 $A_tA_t^*$ 后求逆；那会给第一项 $1/(2\cosh t)$，完全改变结论。

### 4.2 最高层

整个层映射为
$$
D_t^2/2:\mathcal H_3\longrightarrow\mathcal H_1
=T/2=\operatorname{diag}(3,-1,-1,-1).
$$
它可逆；其逆限制到 $K$ 恰为 $-I_K$（把 $K$ 送到第三层对应坐标）。
故
$$
\boxed{\Gamma_{0,t}=I_K,\qquad \Gamma_{2,t}=I_K.}
\tag{4.4}
$$
这里不存在未支付的参数最小化、核选择或短层边界。

## 5. 最佳相邻常数任意大，归一范数仍无效

在当前唯一相邻阶 $n=1$，真实算子比准确为
$$
\Gamma_{1,t}\Gamma_{2,t}^{-1}\Gamma_{1,t}
=\operatorname{diag}\!\left(
\frac{\cosh^2t}{4},\frac14,\frac14
\right).
$$
所以
$$
\boxed{
\inf\{c:\Gamma_{1,t}\Gamma_{2,t}^{-1}\Gamma_{1,t}
\preceq c\Gamma_{0,t}\}
=\frac{\cosh^2t}{4}\longrightarrow\infty.
}
\tag{5.1}
$$
系数 $1$ 在 $\cosh t>2$ 时已经失败。

即使额外规定降低算子范数为 $1$，也不能修复抽象命题。
令 $M_t=\|D_t\|>0$，取 $\widehat D_t=D_t/M_t$。
它仍保留所有分级、对偶和严格 Hodge–Riemann 性。
第 $n$ 个最小源和 Gram 分别变为
$$
\widehat J_{n,t}=M_t^nJ_{n,t},\qquad
\widehat\Gamma_{n,t}=M_t^{2n}\Gamma_{n,t}.
$$
相邻比较中的次数正好抵消，(5.1) 的最佳常数不变。
因此固定层维数、范数归一及全部上述正性都不足以给有限统一常数。

## 6. 对本课题的准确含义

本例排除的是从一般 Poincaré/Hard Lefschetz/Hodge–Riemann 数据直接推出本文 physical Hilbert 范数下的 MP 相邻序。它没有否定这些结构本身，也没有将真实 Hilbert 范数替换成由 $L_t$ 另行构造的 Hodge 度量。

四位正权 Boolean 删除算子属于更窄的张量类；其完整 primitive 系数 $1$ 已由本课题的三异常权结果覆盖。本稿的 $D_t$ 不声称属于该类。一般有限正权的相邻问题仍须使用乘积权、具体包含矩阵、真正低次多项式商或其他已经支付的结构。

相应地，原连续尾的 Gram 常数、实际窄返回源的三 Gram 比较和普通 ISP 完成标准均保持原状态。
