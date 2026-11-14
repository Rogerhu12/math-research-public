# Garayev 2026 第二分支的必零弱极限：一个完整 Hardy 空间检验

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：本文的构造、尾循环性和必零极限均已完整证明。** 它指出 arXiv:2607.16373 所取正文中 Theorem 3.1 的第二分支不能产生其所需的非零紧算子。它不是普通或超不变子空间问题的反例，也没有证明该文所声称的定理命题为假。本文给出的算子本身有很多不变子空间。

## 1. 来源与准确核查范围

核查对象：Mubariz T. Garayev，*On the solution of Kim, Pearcy and Shields problem and its consequences*，[官方 arXiv 入口](https://arxiv.org/abs/2607.16373)。

本次通过先前官方 URL 的检索记录打开了正文提取；直接打开当前 abs、PDF 与版本页面未成功。因此以下定位针对**本次实际取得的正文文本**，不把它冒充最新版本状态，也不据此声称已确认撤稿。

只需原文 Theorem 3.1 的以下步骤：

- 先取有界可逆的非标量 $A$，选可逆有界解析函数 $\varphi$，令 $Av=\varphi$，并写 $v=wAv$，即原式 (3.1)。
- 在 $w^*$ 不属于任何非平凡模型空间 $K_\theta$ 的分支，取 $V_\varepsilon\in K_{\theta_\varepsilon}$ 且 $V_\varepsilon\to w$，再取内函数 $\theta_\varepsilon$ 的弱极限 $\psi$。
- 原文声称此极限满足 $\psi\overline{w^*}\in H^2(\mathbb T)$，并在原式 (3.6) 定义
  $$
  K_1f=\langle \psi\overline{w^*},Cf\rangle v.
  \tag{1.1}
  $$

下面证明一个实际允许的 $A$ 必落在这一分支，并且任何满足所列解析性条件的 $\psi$ 都只能为零。这里 $Cf(z)=\overline{f(\bar z)}$，$w^*=Cw$；Hilbert 内积对第一变量线性。原文的 $\Delta(H^2)$ 要求紧交换子的秩恰为一；其引用的秩至多一形式也要求紧算子本身非零。零算子不能满足任一非零要求。

## 2. 有界可逆的实际算子

在通常的 Hardy 空间
$$
H^2(\mathbb D)=\left\{\sum_{n\ge0}f_nz^n:\sum_{n\ge0}|f_n|^2<\infty\right\}
$$
中，令 $S=M_z$，并定义
$$
c_n=2^{-n^2}\quad(n\ge0),\qquad
w(z)=\sum_{n=0}^{\infty}c_nz^n.
\tag{2.1}
$$

所有系数均实，故 $w^*=w$。级数在整个复平面局部一致收敛。对 $|z|\le1$，
$$
|w(z)-1|
\le \frac12+\sum_{n\ge2}2^{-n^2}
\le \frac12+\sum_{n\ge2}4^{-n}
=\frac7{12}<1.
\tag{2.2}
$$
因此 $w,1/w\in H^\infty$，且
$$
|w(z)|\ge\frac5{12},\qquad
\|1/w\|_\infty\le\frac{12}{5}.
$$

取
$$
A=M_{1/w},\qquad v=w,\qquad \varphi=1.
\tag{2.3}
$$
则 $A$ 有界可逆，逆为 $M_w$；它非标量，因为 $w$ 非恒定。同时
$$
Av=1,\qquad v=wAv.
\tag{2.4}
$$
这些都是原证明允许的对象，不涉及稠密定义的无界乘法算子。

实际上，固定这个 $A$ 后，若原证明任取 $\varphi\in H^{\infty,\mathrm{inv}}$，则
$$
v=A^{-1}\varphi=w\varphi,\qquad \frac{v}{Av}=w.
\tag{2.5}
$$
因此改变那里的 $\varphi$ 不会改变第二分支使用的函数 $w$。

## 3. 每一条后移轨道尾部都稠密

**引理 3.1。** 对每个整数 $N\ge0$，
$$
\overline{\operatorname{span}}\{(S^*)^nw:n\ge N\}=H^2.
\tag{3.1}
$$

**证明。** 设 $g(z)=\sum_{k\ge0}g_kz^k\in H^2$ 与上述全部向量正交。定义
$$
F_g(t)=\sum_{k=0}^{\infty}2^{-k^2}\overline{g_k}\,t^k.
\tag{3.2}
$$
对每个有限 $R$，Cauchy–Schwarz 给
$$
\sum_{k\ge0}2^{-k^2}|g_k|R^k
\le
\|g\|_2
\left(\sum_{k\ge0}2^{-2k^2}R^{2k}\right)^{1/2}<\infty.
$$
故 $F_g$ 是整函数。利用
$$
2^{-(n+k)^2}=2^{-n^2}2^{-k^2}(4^{-n})^k,
$$
得到每个 $n\ge N$ 上
$$
0=\langle(S^*)^nw,g\rangle
=\sum_{k\ge0}2^{-(n+k)^2}\overline{g_k}
=2^{-n^2}F_g(4^{-n}).
\tag{3.3}
$$
整函数 $F_g$ 的零点 $4^{-n}$ 在其定义域内积聚到 $0$，由恒等定理，$F_g\equiv0$。逐个系数即得 $g_k=0$，所以 $g=0$。正交补为零即为 (3.1)。$\square$

**推论 3.2。** 函数 $w^*=w$ 不属于任何非恒定内函数的模型空间
$$
K_\theta=H^2\ominus\theta H^2.
$$

**证明。** 每个 $K_\theta$ 都是闭的 $S^*$ 不变子空间：若 $f\perp\theta H^2$，则对任意 $h\in H^2$，
$$
\langle S^*f,\theta h\rangle
=\langle f,z\theta h\rangle=0.
$$
而 $K_\theta\ne H^2$，因为 $\theta H^2$ 非零。若 $w\in K_\theta$，其整个后移轨道都在这个真闭空间内，违背引理 3.1。$\square$

所以 (2.3) 不是误放进第二分支的特例；它严格满足该分支的排除模型空间条件。证明没有使用模型空间分类或后移循环性的外部判据。

## 4. 原文所需的解析性强迫弱极限为零

**定理 4.1。** 若 $\psi\in H^\infty$ 且
$$
\psi\,\overline{w}\in H^2(\mathbb T),
\tag{4.1}
$$
则 $\psi=0$。

**证明。** 对每个 $n\ge1$，(4.1) 的负 Fourier 系数为零，故
$$
0=\int_{\mathbb T}\zeta^n\psi(\zeta)\overline{w(\zeta)}\,dm(\zeta)
=\langle S^n\psi,w\rangle
=\langle\psi,(S^*)^nw\rangle.
\tag{4.2}
$$
引理 3.1 的 $N=1$ 情形表明这些轨道尾向量张成稠密子空间，所以 $\psi=0$。$\square$

原文选取的弱极限满足 $\|\psi\|_\infty\le1$，并以 (4.1) 为后续定义的依据。对当前 $A$，即使完全接受其取得 (4.1) 的步骤，定理 4.1 仍强迫
$$
\psi=0,\qquad K_1=0,\qquad [A,K_1]=0.
\tag{4.3}
$$

因此不能把式 (1.1) 称为非零秩一算子，也不能由它得到秩恰为一的交换子。这个问题不是“单位向量列可能弱收敛到零”这一一般提醒：在当前允许的算子上，**任何**满足原文后续解析性条件的候选极限都必须是零。

## 5. 一个满足全部逼近要求的显式零极限

为使原逼近机制完全可见，取
$$
\theta_N(z)=z^N,\qquad
V_N(z)=\sum_{k=0}^{N-1}c_kz^k.
\tag{5.1}
$$
则
$$
V_N\in K_{z^N}=\operatorname{span}\{1,z,\ldots,z^{N-1}\},
\qquad
\|V_N-w\|_2^2=\sum_{k\ge N}2^{-2k^2}\longrightarrow0.
\tag{5.2}
$$
同时 $\|\theta_N\|_2=1$，而 $\theta_N\rightharpoonup0$，因为它们是 Hardy 空间的一条正交基尾列。

在单位圆上，
$$
g_N:=\theta_N\overline{V_N^*}
=\sum_{k=0}^{N-1}c_kz^{N-k}\in H^2.
\tag{5.3}
$$
有 $\|g_N\|_2=\|V_N\|_2\le\|w\|_2$，且每个固定 Fourier 系数趋于零。因此 $g_N\rightharpoonup0$。相应的有界秩一算子
$$
Q_Nf=\langle g_N,Cf\rangle v
$$
对每个固定 $f$ 满足 $Q_Nf\to0$。这个独立的显式序列同时展示了：

1. 模型空间向量确实逼近 $w$；
2. 内函数都保持单位范数；
3. 所需乘积确实解析；
4. 所产生的强算子极限仍为零。

并不存在范数单位化自动保住非零极限的步骤。

## 6. 范围边界

算子 $A=M_{1/w}$ 自身并不是不变子空间问题的反例。例如 $zH^2$ 是它的非零真闭不变子空间，因为解析乘法保持因子 $z$。本文也没有证明不存在另一个紧算子满足 $A$ 的某种秩一交换子条件。

本文精确排除的是：用所取正文 Theorem 3.1 第二分支的弱极限与式 (3.6)，在不另付非零条件的情况下完成该定理的论证。本例甚至迫使该分支的解析候选极限全为零。它因此不能作为本仓库普通 Hilbert ISP 完成的有效外部证明。

本文不采用任何第三方撤稿或接受状态消息，也没有把文献中的声明当作公认结论。

## 7. 第一分支的待核记录；不作为本稿主结论

官方正文提取在第一次定义 $K$ 的未编号展示式处漏掉了公式，但保留了原式 (3.2) 的右端
$$
T_vP_{\mathbb C1}T_{\theta^*-A^*C(\theta\overline{w^*})}^*.
$$
后面的式 (3.6) 则完整显示 (1.1)。若第一次的 $K$ 确为与 (1.1) 同型、把 $\psi$ 换成 $\theta$ 的定义，那么以下是 (3.2) 的一个直接反例：

取实数 $0<c<1$，
$$
A=(I+cS)^{-1},\quad v=w=1+cz,\quad\theta=z^2,\quad h=z^2+cz.
$$
此时 $Av=1$、$w^*\in K_{z^2}$，且 $A^*h=z^2=\theta^*$。对 $K=v\otimes h$，右端为零，而
$$
[A,K]=c(1\otimes z-z\otimes z^2)
$$
把 $z$ 与 $z^2$ 分别映到 $c$ 与 $-cz$，所以秩为二。

上述张量计算自身准确，但本稿未取得原 PDF 中第一次 $K$ 定义的完整展示式，故只保留为**条件核查记录**，不把它当作已经核准原文全部符号的第一分支反证。第 2–6 节的主结论不依赖这一待核公式。

## 来源定位

- 官方条目及本次取得的正文：[arXiv:2607.16373](https://arxiv.org/abs/2607.16373)。
- 原文 §1：$\Delta(H^2)$ 的秩恰为一条件；所引秩至多一判据的非零紧算子条件。
- 原文 Theorem 3.1：式 (3.1)，排除全部模型空间的分支，式 (3.4)–(3.7)，尤其式 (3.6)。
- 本稿所有循环性、乘法可逆性与零极限判断均已在正文自含证明；没有把检索摘要当成这些数学结论的依据。
