# R279 — 原有限来源上的第三层进位：非常数首共振及完整余项的准确作用

日期：2026-11-13。**状态：以下同一原有限来源的模 $p^3$ 比较、第三层进位的两块显式公式及其准确有限商均已证明。没有证明该商中的类消失，也没有由原中央条件构造新的深关系。**

本篇直接计算 R272 的原有限目标。R272 的完成来源换参含
$D^{-1}=(rA+qA')^{-1}$；本篇证明，在共有的模 $p^2$ 原核上，
第三层的实际差异可完全不经这份完成来源换参计算。
结果继续保留原有限一次除幂像，不能以整个完成来源替代它。

## 1. 原目标、原有限带与确定的两个来源

固定
$$
p=4r-1\ge19,\qquad k=2r+s,\qquad 0\le s<r.
$$
在整环 $\mathcal O$ 上，置
$$
T=\mathcal O[q,z]/(q^r-pz,z^3,q^sz^2).
\tag{1}
$$
其整基是 $q^l,zq^l$（$0\le l<r$）及
$z^2q^l$（$0\le l<s$）。当 $s=0$ 时第三组为空。
这正是 R252/R272 的同一加权窗口，$q^{3r}=0$。

保留 R272 的准确
$$
A(q)=a_0h_+(q),\quad a_0=p[q^r]Z,\quad
L_0(q)=[\log F_{\rm rad}]_{<r},\quad f(q)=qe^{L_0(q)},
\tag{2}
$$
以及原 $U(q)$，使
$$
\log F_{\rm rad}=L_0+q^rA/p+q^rU.
\tag{3}
$$
$A$ 的常数为单位。实际只使用 $f$ 到次数 $3r-1<p$，
其指数中的全部阶乘都是单位；超过该窗口的任意整提升不参与计算。
同样只取原 $U\bmod q^{2r}$，而不假设其无穷级数整。

原有限来源是 R249/R252 已付 conductor 后的
$$
V_n=\bigoplus_{0\le m\le n,\ 0\le j\le24m}
\mathcal O R^mq^j.
\tag{4}
$$
以下也适用于任意由这些单项式选出的有限整子格，只要它被
$\mathcal M=R\partial_R$ 保持。对 (4)，$\mathcal M$ 在原基中
就是乘整数 $m$，所以没有新增来源或角次数。

令 $e_2(X)=1+X+X^2/2$，定义两个实际整评价
$$
J(P)=P(q,f(q)e_2(A(q)z)),\qquad
J_U(P)=P(q,f(q)e_2((A(q)+pU(q))z)).
\tag{5}
$$
$J_U$ 是完整原来源，$J$ 是 R252 的确定首模型。
所有等式都在同一个 $T$ 或 $T/p^NT$ 中读取。

## 2. 任意原多项式的准确三块公式

对 $P\in V_n$ 定义真实低轴函数
$$
W_j(q)=(\mathcal M^jP)(q,f(q)),\qquad j\ge0.
\tag{6}
$$
这些函数保留 (2) 的真正低对数，不任取它的模 $p$ 提升。
由 $z^3=0$，准确有
$$
J(P)=W_0+AzW_1+\tfrac12A^2z^2W_2.
\tag{7}
$$

记 $[H]_{<a}$ 为低于 $a$ 次的截断，并用
$$
S(H)=q^{-r}(H-[H]_{<r})
\tag{8}
$$
表示普通系数的移块。它不是对目标中的零因子作除法。
把 (7) 写进 (1) 的唯一整基，三个系数多项式分别为
$$
\boxed{\begin{aligned}
J_0(P)&=[W_0]_{<r},\\
J_1(P)&=[AW_1+pS(W_0)]_{<r},\\
J_2(P)&=[A^2W_2/2+pS(AW_1)+p^2S^2(W_0)]_{<s}.
\end{aligned}}
\tag{9}
$$
这同时保留非常数 $A$ 与各个低轴函数相乘后发生的进位。
例如 $S(AW_1)$ 不能在特征零中直接换成 $AS(W_1)$。

同一展开给
$$
\boxed{
J_U(P)=J(P)+pzU J(\mathcal MP)
+\frac{p^2z^2U^2}{2}J(\mathcal M^2P).
}
\tag{10}
$$
此式在 $T$ 中准确成立，不只是其关联分次上的恒等式。

## 3. 两个共有低层及原第三层的定义

记
$$
\Lambda_a=\{P\in V_n:J(P)\in p^aT\},\qquad
\mathcal F_a=\operatorname{im}(\Lambda_a\longrightarrow V_n/pV_n).
\tag{11}
$$
R252 的同一个目标自同构
$$
q\longmapsto q,\qquad z\longmapsto z(1+pU/A)
\tag{12}
$$
在 $T/p^2T$ 上成立，并把 $J$ 送到 $J_U$。
它模 $p$ 为恒等。于是二者的 $\Lambda_1,\Lambda_2$ 及
$\mathcal F_1,\mathcal F_2$ 完全相同。

在 $T_1=T/pT$ 中，任意 $\overline P\in\mathcal F_1$ 满足
$$
\boxed{
z\,j(\mathcal MP)=0,\qquad
z^2j(\mathcal M^2P)=0,
}
\tag{13}
$$
其中 $j=J\bmod p$。一种证明是对 (9) 约化：
$A$ 为单位先迫 $W_1\equiv0\bmod(q^r,p)$，
再迫 $W_2\equiv0\bmod(q^s,p)$。
代入 $zj(\mathcal MP)$ 和 $z^2j(\mathcal M^2P)$ 即得 (13)。
这不需要在不被 $\partial_z$ 保持的截断环上非法求导。

对 $\overline P\in\mathcal F_2$，任选 $P\in\Lambda_2$ 提升，定义
$$
\boxed{
\eta(\overline P)=
\overline{\frac{zJ(\mathcal MP)}p}\in T_1.
}
\tag{14}
$$
除 $p$ 由 (13) 合法。若换成 $P+pQ$，共有二层条件给
$Q\in\Lambda_1$，变化为 $zj(\mathcal MQ)=0$。
故 (14) 是良定义的原有限来源线性映射。

必须使用的原一次除幂像为
$$
\mathcal V_1=
\left\{\overline{J(Q)/p}:Q\in\Lambda_1\right\}\subset T_1.
\tag{15}
$$
它对 $J_U$ 也相同，原因仍是 (12) 模 $p$ 为恒等。
原第三层 Bockstein 的目标是准确的 $T_1/\mathcal V_1$；
$\mathcal V_1$ 没有被扩大为目标理想或任意形式函数像。

## 4. 非常数首共振下的两块显式进位

**定理 1。** 对 (14)，完整三个块准确为
$$
\boxed{\begin{aligned}
\eta_0(\overline P)&=0,\\
\eta_1(\overline P)&=-[\overline A^{-1}S(\overline W_0)]_{<r},\\
\eta_2(\overline P)&=-[S(\overline W_1)]_{<s}.
\end{aligned}}
\tag{16}
$$
这里的 $W_j$ 是 (6) 的同一实际提升，随后约化。

**证明。** (7) 作用于 $\mathcal MP$，再乘 $z$，其基系数为
$$
0,\qquad [W_1]_{<r},\qquad
[AW_2+pS(W_1)]_{<s}.
\tag{17}
$$
$P\in\Lambda_2$ 及 (9) 的中间行给
$$
\overline{[W_1]_{<r}/p}
=-[\overline A^{-1}S(\overline W_0)]_{<r}.
\tag{18}
$$
注意左边仅把已知整除的低于 $r$ 次部分除以 $p$。

最后一行先模 $p$ 给 $[W_2]_{<s}\in p\mathcal O[q]$，
再除 $p$ 并模 $p$，得到
$$
[\overline A\,([W_2]_{<s}/p)]_{<s}
=-2[\overline A^{-1}S(\overline A\,\overline W_1)]_{<s}.
\tag{19}
$$
由 $[\overline W_1]_{<r}=0$，此时才有合法等式
$S(\overline A\,\overline W_1)=\overline A S(\overline W_1)$。
因此 (19) 为 $-2[S(\overline W_1)]_{<s}$。
将它与 (17) 的另一项 $+[S(\overline W_1)]_{<s}$ 相加，
得到 (16) 的末行。第一行显然，第二行是 (18)。$\square$

因此这里保留非常数 $A$ 后，第二个进位块仍准确不含 $A$；
第一个块只用原有限截断中的 $A^{-1}$，没有出现 $D^{-1}$。
若 $s=0$，所有末块式子为空，不增加任何不存在的行。

## 5. 完整原余项对第三层的唯一作用

**定理 2。** 对共有的 $\mathcal F_2$，有
$$
\boxed{
\beta_{2,U}(\overline P)-\beta_2(\overline P)
=\overline U\,\eta(\overline P)
\quad\text{于 }T_1/\mathcal V_1.
}
\tag{20}
$$
特别地，完整原来源的第三层恰为
$$
\boxed{
\mathcal F_{3,U}
=\ker\bigl(\beta_2+\overline U\eta:
\mathcal F_2\longrightarrow T_1/\mathcal V_1\bigr).
}
\tag{21}
$$

**证明。** 对原 $P\in\Lambda_2$，将 (10) 除以 $p^2$ 并约化。
一次项给 $\overline U\eta$；二次项由 (13) 的第二式准确消失。
两份一次除幂像相同，故 (20) 在指定的同一有限商中成立。
若该类为零，选 $Q\in\Lambda_1$ 使
$J_U(P)/p^2\equiv J_U(Q)/p\pmod p$，则 $P-pQ$ 是同一模 $p$ 影的
原三层提升；反向同理。因此第三 Bockstein 的核正是所求
primitive 三层方向，得到 (21)。$\square$

这里先保留 (10) 的二次项，再用共有原核证明它消失。
不能将此说成完整来源算子本身没有 $U^2$ 或 $UU'$ 项；
R272 的 (30)--(31) 仍是其正确展开。
两种表达的区别在于 (20) 已经对同一原二层核取了第三层商。

同一个 $\eta$ 也不随上述径向改变：将 (10) 用于
$\mathcal MP$，乘 $z/p$ 后约化，新增项由
$z^2j(\mathcal M^2P)=0$ 消失。
又因为 $T_1$ 中 $q^r=0$，(20) 只读取原
$U\bmod(q^r,p)$，即 (3) 中原次数 $r$ 至 $2r-1$ 的整余项。
它不读取 R273 的更晚第二单位 carry，也不以那个单位替代当前类。

## 6. 实际公共因子的支持与尚未付出的有限像

上述式子允许直接对实际核分子计算支持，而不先清掉完成来源的高极。
例如在同一 $\mathbb F_p[q,R]$ 中，若
$\overline P=G^mH$，置
$$
h=\operatorname{ord}_qG(q,\overline f),\quad
\mu=\operatorname{ord}_q(\mathcal MG)(q,\overline f),
$$
$$
z_0=\operatorname{ord}_qH(q,\overline f),\quad
z_1=\operatorname{ord}_q(\mathcal MH)(q,\overline f).
$$
所有这些阶数在所需的原有限轴上计算；零函数取无穷。
由乘法和原 $\mathcal M$ 的 Leibniz 公式，
$$
\operatorname{ord}_q\overline W_0=mh+z_0,
\qquad
\operatorname{ord}_q\overline W_1\ge
\min((m-1)h+\mu+z_0,mh+z_1).
\tag{22}
$$
于是 (16) 给 $\eta_1$ 的起始角阶至少 $mh+z_0-r$，
$\eta_2$ 的起始角阶至少 (22) 右侧减 $r$，负下界取零。
超出该块长度即表示该块为零。$A^{-1}$ 常数为单位，
不会降低前一个阶数；乘整 $\overline U$ 也不会降低这些支持界。

这是一份同一有限核的明确计算，并不证明
$\overline U\eta(\overline P)\in\mathcal V_1$。
也不能把 $G$ 的角次数预算与 R242 的原 $(A,C)$ 平面预算混同；
若调用后者，仍须使用 R249/R252 已支付的来源转换。

R272 的固定 $q=4$ 强迫留数依然成立，但其完成来源中的
$(1-q/4)^{-(r-1)}$ 不是计算 (20) 必须先付的清分母成本。
本篇实际需要解决的是 (21) 中已明确的有限像，而非完成局部环的可解性。
原三条完整中央零也没有自动给出该像包含关系。

依赖：R249/R252 的原有限带与真实首模型，R233 的原提升层，
R272 的完整 $A,L_0,U$。原常数共振版本已见
[首进位记录](../notes/2026-11-13-deep-original-first-carry-gauge.md)；
本篇保留原 $q$ 参数的非常数 $A$，并给出 (16)、(20)、(21)
在 R272 同一有限来源上的完整证明。
