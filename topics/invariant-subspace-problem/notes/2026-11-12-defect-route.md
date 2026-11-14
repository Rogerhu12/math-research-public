# 小秩一扰动到原算子：WOT 支撑、固定锚点和图变换

日期：2026-11-12。会话：Astra-ISP-b382c564；并行推导：defect-route。

**状态：以下带完整证明的命题均为已证明的中间结论，不声称新颖；没有证明完整 ISP。** 本笔记不将“有小扰动的不变半空间”等同于“原算子有不变子空间”。resolvent 半空间的具体结构障碍已单独登记在 [R2](../results/R2-resolvent-halfspace-obstruction.md)。

## 1. 外部输入的精确范围

A. Tcaciuc, *Invariant subspace problem for rank-one perturbations: the quantitative version*, J. Funct. Anal. **283** (2022), no. 5, 109548，Theorem 1.1，证明：对无穷维复 Banach 空间上的任意有界算子 $T$ 和任意 $\varepsilon>0$，存在秩至多一的 $F$、$\|F\|\le\varepsilon$，使 $T+F$ 有不变半空间。正式发表年份是 **2022**；预印本为 [arXiv:2006.11954v2](https://arxiv.org/abs/2006.11954v2)。[作者机构存档](https://roam.macewan.ca/items/a84e5fe0-6b46-4860-8a99-1c87bf84b4d0) 提供发表信息和作者版本。

在 Hilbert 空间上，若 $P_n$ 为相应半空间的正交投影、$\|F_n\|\to0$，则

$$
(I-P_n)(T+F_n)P_n=0,
\qquad
\varepsilon_n:=\|(I-P_n)TP_n\|\le\|F_n\|\to0.
\tag{1.1}
$$

没有外部定理保证这些半空间在 $n\to\infty$ 时保留某个固定非零向量，或者在弱极限中保留非零核。下面精确区分“可取弱极限”与“弱极限足够非退化”。

## 2. WOT 极限不必是投影，但它的支撑仍可用

### 命题 A：支撑不变性

设 $P_n$ 是正交投影，$P_n\to P$ 于弱算子拓扑，并满足 (1.1)。则 $0\le P\le I$，且

$$
TPT^*\le\|T\|^2P,
\qquad
T^*(I-P)T\le\|T\|^2(I-P).
\tag{2.1}
$$

因此

$$
\overline{\operatorname{Ran}P}=(\ker P)^\perp
\quad\text{和}\quad
\ker(I-P)
\tag{2.2}
$$

都是闭 $T$-不变子空间。特别地，若 $P\ne0$ 且 $\ker P\ne\{0\}$，就得到非零真闭不变子空间。

**证明。** $0\le P_n\le I$ 的二次型不等式可直接取弱极限，得到 $0\le P\le I$。设 $D_n=(I-P_n)TP_n$，$C=\|T\|$。对任意 $y\in H$，

$$
P_nT^*y=P_nT^*P_ny+D_n^*y,
$$

因而

$$
\|P_nT^*y\|\le C\|P_ny\|+\varepsilon_n\|y\|.
$$

取平方后令 $n\to\infty$。由于投影性质，

$$
\|P_nT^*y\|^2=\langle P_nT^*y,T^*y\rangle
\longrightarrow\langle PT^*y,T^*y\rangle,
$$

且 $\|P_ny\|^2\to\langle Py,y\rangle$。故

$$\langle TPT^*y,y\rangle\le C^2\langle Py,y\rangle.$$

这就是第一个算子不等式。对 $T^*$ 和 $I-P_n$ 使用同一论证，因为

$$P_nT^*(I-P_n)=D_n^*,$$

得到第二个不等式。

若 $y\in\ker P$，第一式给出

$$0\le\langle PT^*y,T^*y\rangle\le C^2\langle Py,y\rangle=0.$$

正算子的零二次型等价于属于其核，所以 $T^*y\in\ker P$。其正交补于是 $T$-不变。若 $x\in\ker(I-P)$，第二式同理直接给出 $Tx\in\ker(I-P)$。证毕。

**较弱的充分假设。** 第一个不等式其实只需 $D_n^*\to0$ 于强算子拓扑，因为上面的证明只用了对每个固定 $y$ 有 $\|D_n^*y\|\to0$。第二个不等式只需 $D_n\to0$ 强。范数趋零同时保证两者。相应地，若 $(T+F_n)\operatorname{Ran}P_n\subset\operatorname{Ran}P_n$ 且 $F_n^*\to0$ 强，则 $D_n^*=-P_nF_n^*(I-P_n)$ 的强零性**不能**仅由此自动推出，因为 $I-P_n$ 的输入也在变化；仍需直接控制 $D_n^*$。这里不能再次漏掉变量依赖。

**对整个多项式代数的加强。** 对每个固定多项式 $p$，同一个极限 $P$ 还满足

$$
p(T)Pp(T)^*\le\|p(T)\|^2P,
\qquad
p(T)^*(I-P)p(T)\le\|p(T)\|^2(I-P).
\tag{2.4}
$$

证明如下。对任一正交投影 $Q$，记 $B=QTQ$、$D=(I-Q)TQ$，归纳得

$$T^kQ-B^k=\sum_{j=0}^{k-1}T^{k-1-j}DB^j\quad(k\ge1).$$

这里第 $j=0$ 项按 $B^0=I$ 解释。因此

$$\|(I-Q)T^kQ\|\le k\|T\|^{k-1}\|D\|.$$

对 $p(z)=\sum_kc_kz^k$，有

$$\|(I-P_n)p(T)P_n\|\le\varepsilon_n\sum_{k\ge1}|c_k|k\|T\|^{k-1}\longrightarrow0.$$

将命题 A 用于 $p(T)$ 即得 (2.4)，并可由范数连续性推广到 $T$ 生成的含单位范数闭代数。此论证没有给依赖 $n$、次数或系数可能无界的多项式族提供统一缺陷界。

### 命题 B：足够的固定锚点

设 $H$ 可分，$P_n$ 满足 (1.1)。若存在固定的 $x,y\in H$、$y\ne0$ 和 $\delta>0$，使

$$
\liminf_n\|P_nx\|\ge\delta,
\qquad
\|P_ny\|\longrightarrow0,
\tag{2.3}
$$

则 $T$ 有非零真闭不变子空间。

**证明。** $B(H)$ 的单位球在 WOT 下紧，且 $H$ 可分时其 WOT 在该球上可度量，因此可抽子列使 $P_n\to P$。也可以直接对可数稠密集合上的矩阵元使用对角抽取，并用统一范数界延拓极限双线性型。由

$$
\langle Px,x\rangle=\lim_n\|P_nx\|^2\ge\delta^2,
\qquad
\langle Py,y\rangle=\lim_n\|P_ny\|^2=0,
$$

得 $P\ne0$ 和 $y\in\ker P\setminus\{0\}$。应用命题 A。证毕。

两个方向可以对偶交换：若 $\|(I-P_n)x\|\to0$，且对某固定 $y$ 有 $\liminf\|(I-P_n)y\|>0$，则 $\ker(I-P)$ 为非零真 $T$-不变子空间。

**剩余难点。** (2.3) 的第二个要求是真正的趋零。把它改成“$\|(I-P_n)y\|$ 有正下界”不够，因为这只排除 $P=I$，不能保证 $\ker P\ne0$。同理，仅知 $P\ne0,I$ 也不够。

### 这是条件性桥梁，不是对任意算子的证明

事实上，存在 $0\ne P\ge0$、$\ker P\ne0$、$TPT^*\le\|T\|^2P$，本身就等价于存在非零真不变子空间：一个方向由命题 A 的核论证；另一个方向若 $M$ 不变，取 $P=P_M$，有 $TP=P TP$，因而 $TPT^*\le\|T\|^2P$。这说明“找到边界退化但非零的正极限”承载了真正的困难。

## 3. 两个极限反例和一种无效归一化

### 例 C1：半空间投影的强极限可为零或恒等

令 $H=\ell^2(\mathbb Z)$，$Ue_k=e_{k+1}$。子空间

$$M_n=\overline{\operatorname{span}}\{e_k:k\ge n\}$$

全是不变半空间，缺陷恰为零。但 $P_{M_n}\to0$ 强，因为对每个 $x\in\ell^2(\mathbb Z)$，其 $n$ 之后的平方和趋零。同样，$P_{M_{-n}}\to I$ 强。无限维和无限余维在这种极限下均不能保证非平凡性。

### 例 C2：非零、非恒等的 WOT 极限也可没有边界核

仍取 $H=\ell^2(\mathbb Z)$，令

$$J_ne_k=e_{n-k},\qquad P_n=(I+J_n)/2.$$

$J_n^*=J_n$ 且 $J_n^2=I$，故 $P_n$ 是正交投影。反射的两点轨道给出无限多个线性无关的正、负特征向量，所以 $P_n$ 的值域和核均无限维。

对固定 $i,j$，$\langle J_ne_i,e_j\rangle$ 只可能在 $n=i+j$ 时非零。因此 $J_n\to0$ 于 WOT（先在有限支撑向量上，再用统一范数界推广），从而

$$P_n\longrightarrow\tfrac12I\quad\text{于 WOT}.$$

取非标量算子 $T=U+U^*$。由 $J_nU=U^*J_n$ 和 $J_nU^*=UJ_n$，可知 $P_nT=TP_n$；所以这里的缺陷仍恰为零。但是极限 $P=I/2$ 满足

$$\overline{\operatorname{Ran}P}=H,\qquad\ker P=\ker(I-P)=\{0\}.$$

命题 A 不会在该极限中产生非平凡子空间。对于 $n>0$，

$$P_ne_0=(e_0+e_n)/2,$$

该序列没有范数收敛子列，故这些投影也没有 SOT 收敛子列。这个例子否定的是不成立的紧致性步骤；它当然不是 ISP 的反例。

也可以让极限为**非标量**而仍无边界核。对 $q\ge2$，在 $H^{\oplus q}$ 上定义等距嵌入

$$V_{n,q}f=q^{-1/2}(f,U^nf,\ldots,U^{(q-1)n}f).$$

其值域投影 $Q_{n,q}=V_{n,q}V_{n,q}^*$ 的第 $(i,j)$ 块为 $q^{-1}U^{(i-j)n}$（$i,j=0,\ldots,q-1$）。非零整数次幂 $U^{kn}\to0$ 于 WOT，故 $Q_{n,q}\to I/q$。这些投影的秩和余秩均无限：用块对角酉算子消去各分量的 $U^{in}$ 后，其值域就是对角子空间 $\{(f,\ldots,f):f\in H\}$。每个 $Q_{n,q}$ 都与 $(U+U^*)^{\oplus q}$ 交换。因此取 $q=2,3$ 的直和便得到缺陷为零的半空间投影，其 WOT 极限为

$$P=\tfrac12I_{H^{\oplus2}}\oplus\tfrac13I_{H^{\oplus3}}.$$

这个 $P$ 非标量，且 $P$ 与 $I-P$ 都可逆。即使增加“极限非标量”的条件，仍不能凭支撑和边界核自动取得子空间。

### 例 C3：不能靠无界标量放大零投影极限

若非零正交投影 $P_n\to0$ 强，试图选择 $c_n\to\infty$ 使 $c_nP_n$ 有非零的有界 WOT 极限也不可行。WOT 收敛的算子序列必然一致范数有界：先对每个 $x$ 对向量序列 $(c_nP_nx)$ 用一致有界原理，再对算子族用一次。因此 $\sup_n\|c_nP_n\|<\infty$，即 $\sup_n|c_n|<\infty$。而有界的 $c_n$ 又使 $c_nP_n\to0$ 强。

## 4. Riccati 方程给出的定量去缺陷条件

### 命题 D：有可控 Sylvester 逆时能构造真不变图

相对于 $H=H_0\oplus H_1$，写

$$T=\begin{pmatrix}A&B\\C&D\end{pmatrix}.$$

令 $\mathcal S:B(H_0,H_1)\to B(H_0,H_1)$ 为

$$\mathcal S(X)=DX-XA.$$

假设 $\mathcal S$ 可逆，$\kappa=\|\mathcal S^{-1}\|$，并且

$$4\kappa^2\|B\|\|C\|<1.\tag{4.1}$$

则存在有界 $X:H_0\to H_1$，满足

$$\|X\|\le2\kappa\|C\|,$$

且其图 $\mathcal G(X)=\{(u,Xu):u\in H_0\}$ 为 $T$-不变闭子空间。若 $H_0,H_1$ 都无限维，则该图为半空间。

**证明。** 图不变当且仅当对每个 $u$ 有

$$Cu+DXu=X(Au+BXu),$$

也就是

$$\mathcal S(X)=XBX-C.\tag{4.2}$$

若 $C=0$，取 $X=0$。否则置 $r=2\kappa\|C\|$，并在 $\|X\|\le r$ 的完备闭球上定义

$$\Phi(X)=\mathcal S^{-1}(XBX-C).$$

有

$$
\|\Phi(X)\|
\le\kappa\|C\|+\kappa\|B\|r^2
=\kappa\|C\|(1+4\kappa^2\|B\|\|C\|)<r.
$$

又有

$$
\|\Phi(X)-\Phi(Y)\|
\le\kappa\|B\|(\|X\|+\|Y\|)\|X-Y\|
\le4\kappa^2\|B\|\|C\|\|X-Y\|.
$$

所以压缩映射原理给出固定点，满足 (4.2)。有界算子的图闭；映射 $u\mapsto(u,Xu)$ 给出它与 $H_0$ 的同构，而商映射 $(u,v)\mapsto v-Xu$ 的核恰为该图，故商空间同构于 $H_1$。证毕。

**一个直接可检查的逆条件。** 若对某 $\lambda\in\mathbb C$，$D-\lambda I$ 可逆，设

$$d=\|(D-\lambda I)^{-1}\|,\qquad a=\|A-\lambda I\|,$$

且 $da<1$，则

$$\kappa\le\frac d{1-da}.\tag{4.3}$$

事实上，$\mathcal S(X)=Y$ 等价于

$$X-(D-\lambda I)^{-1}X(A-\lambda I)=(D-\lambda I)^{-1}Y,$$

左边是在 $B(H_0,H_1)$ 上范数小于一的算子的 $I-K$，故 Neumann 级数给出逆及 (4.3)。

**与 ISP 的缺口。** 小秩一扰动定理只给 $\|C\|$ 小。它不给可逆的 $\mathcal S$，也不给 $\kappa$ 与 $\|C\|$ 之间满足 (4.1) 的控制。通常 resolvent 构造靠近谱边界，不能无理由假定 $D-\lambda I$ 在边界上仍有有界逆。

## 5. 任意小秩一缺陷甚至不保证任何近邻不变图

### 命题 E：固定半空间的图修正可彻底失败

取 $H_0=H_1=\ell^2(\mathbb N)$，固定单位向量 $u_0\in H_0$、$v_0\in H_1$。对任意 $\varepsilon>0$，令

$$
C_\varepsilon u=\varepsilon\langle u,u_0\rangle v_0,
\qquad
T_\varepsilon=\begin{pmatrix}0&0\\C_\varepsilon&0\end{pmatrix},
\qquad
P_0=P_{H_0\oplus0}.
$$

（内积约定第一变量线性。）则 $\|(I-P_0)T_\varepsilon P_0\|=\varepsilon$，缺陷秩一，但任何闭 $T_\varepsilon$-不变子空间 $M$ 的正交投影都满足

$$\|P_M-P_0\|=1.\tag{5.1}$$

**证明。** 若 $\mathcal G(X)$ 是定义在整个 $H_0$ 上的有界图，则

$$T_\varepsilon(u,Xu)=(0,C_\varepsilon u).$$

图中第一分量为零的向量只能是零，所以图不变要求 $C_\varepsilon u=0$ 对一切 $u$ 成立，这与 $C_\varepsilon\ne0$ 矛盾。

再证明若闭子空间 $M$ 满足 $\|P_M-P_0\|=\eta<1$，它必是这种图。对 $m\in M$，

$$\|P_0m\|\ge(1-\eta)\|m\|,$$

故 $P_0|_M$ 单射且值域闭。若 $x\in H_0$ 正交于其值域，则 $x\perp M$，从而 $P_Mx=0$，但

$$\|(P_0-P_M)x\|=\|x\|$$

迫使 $x=0$。所以该闭值域也稠密，即等于 $H_0$。因此 $P_0|_M$ 是有界同构，

$$X=(I-P_0)(P_0|_M)^{-1}:H_0\to H_1$$

有界，且 $M=\mathcal G(X)$。上一段说明这种 $M$ 不可能不变。故所有不变子空间的投影距离都至少一；两个正交投影之差的范数至多一，于是得到 (5.1)。证毕。

$T_\varepsilon$ 本身当然有很多不变子空间（例如 $0\oplus H_1$）。这个例子只说明从一个给定的近不变半空间出发，范数很小、甚至秩一的缺陷，不足以保证小图修正。

## 6. 下一步的确切问题

1. 能否为任意无特征值的 $T$ 选择缺陷趋零的投影，并取得命题 B 的固定锚点？R2 的自然尾部选择使所有固定向量的投影趋零；在同一 $E$ 中一直保留固定 $x_j$ 又有正缺陷下界。这要求真正不同的选择机制。
2. 能否构造带可控 Sylvester 逆的近不变分解，并使 $\kappa^2\|B\|\|C\|\to0$？仅有 $\|C\|\to0$ 不够，命题 E 已明确排除这一简化。
3. 若能产生非零 WOT 极限 $0<P<I$，还需证明其在 $0$ 或 $1$ 有非零特征空间，或另外提出从全支撑正收缩算子提取不变子空间的论证。例 C2 表明不能把“非标量极限”或“不是 $0,I$”直接替代该要求。

这些问题目前仍未证明。本笔记不将任何一条条件性桥梁登记为完整 ISP 的答案。
