# R51：核向量的定量高位粗糙性与有界交织的平滑障碍

日期：2026-11-12（UTC+8）。会话：Astra-ISP-0c017065。分工：`critical_kernel`；固定高位乘子简化由 `l2_moments` 提出，闭不变子空间上的交织推广由根代理提出。

**状态：已证明的中间结论。** 第一部分把 R50 的有限尾 Walsh 阶估计用于一般潜在核向量，得到显式的高位质量下界与发散矩。第二部分证明任意闭 $A$-不变子空间上的非零有界交织都不能把其整个定义空间送进任何固定的、无穷增长的 Walsh 次数权域，或固定阶高位位置权域。未证明一般核向量不存在，也未排除针对单个核向量、利用实际核方程的额外正则化。

## 1. 记号与 R50 的定量输入

沿用原 odometer $A$、原临界对数 $L$ 与 $D=I-e^{-L}$；特别地 $\ker L=\ker D$。令

$$
\chi_j(y)=(-1)^{b_j(y)},\qquad
\chi_S=\prod_{j\in S}\chi_j
$$

（$S\subset\mathbb N_0$ 有限）。$\{\chi_S\}$ 是 $H=L^2(\mathbb Z_2)$ 的标准正交基，写

$$v=\sum_S\widehat v(S)\chi_S.$$

对 $m\ge1,d\ge0$，令 $P_{m,d}$ 保留恰好满足

$$|S\cap\{m,m+1,\ldots\}|\le d$$

的 Walsh 分量；低于 $m$ 的位不作限制。特别地 $P_{m,0}=\mathbb E_m$ 是到低 $m$ 位柱函数的条件期望。

R50 已给出一个有界模型 $T_m$，满足

$$
\|L-T_m\|\le22\eta_{m-1},\qquad \|T_m\|<8,
\tag{1.1}
$$

且当 $m+2\ge48d$ 时，对 $u=P_{m,d}u$ 有

$$
\|u\|\le K_d(m)\|T_mu\|,
\tag{1.2}
$$

其中可以取

$$
K_d(m)=\sqrt{d+1}\,(34\sqrt6)^{d+1}
                   (m+2)^{3(d+1)/2}.
\tag{1.3}
$$

这里 $\eta_j=a_{j+1}/a_j$；其超快衰减使 $K_d(m)\eta_{m-1}\to0$ 对每个固定 $d$ 成立。本条使用 (1.1)–(1.3)，不在一般向量上擅自应用有限阶左逆。

## 2. 每个潜在核向量都具有高尾阶质量

**定理 2.1。** 设 $v\in\ker L$、$m+2\ge48d$。则

$$
\boxed{
\|(I-P_{m,d})v\|
\ge
\frac{1-22K_d(m)\eta_{m-1}}{1+8K_d(m)}\,\|v\|.
}
\tag{2.1}
$$

分子为负时此式当然仍成立；对每个固定 $d$，分子最终趋于一。

**证明。** 写 $u=P_{m,d}v$、$z=(I-P_{m,d})v$。因为 $Lv=0$，

$$
T_mu=T_mv-T_mz=(T_m-L)v-T_mz.
$$

由 (1.1)–(1.2)，

$$
\|u\|\le K_d(m)\bigl(22\eta_{m-1}\|v\|+8\|z\|\bigr).
$$

再使用 $\|v\|\le\|u\|+\|z\|$ 并移项，即得 (2.1)。这里没有把 $z$ 当作有限阶向量。证毕。

若 $22K_d(m)\eta_{m-1}\le1/2$，由于 $K_d(m)\ge1$，可简化成

$$
\boxed{
\|(I-P_{m,d})v\|
\ge\frac{\|v\|}{18K_d(m)}.
}
\tag{2.2}
$$

特别地，非零核向量的柱逼近不能任意快：

$$
\|v-\mathbb E_m v\|
\ge c\,(m+2)^{-3/2}\|v\|
\quad\text{对充分大的 }m,
\qquad c=(18\cdot34\sqrt6)^{-1}.
\tag{2.3}
$$

这是潜在核的必要条件，不是对全部 $H$ 中向量的断言，也没有据此排除任意慢柱逼近。

## 3. 所有固定阶位置矩都必须发散

对有限集 $S$，令 $\ell_r(S)$ 是 $\{j+1:j\in S\}$ 中第 $r$ 大的数；当 $|S|<r$ 时令 $\ell_r(S)=0$。于是

$$
\ell_r(S)\ge m+1
\quad\Longleftrightarrow\quad
|S\cap\{m,m+1,\ldots\}|\ge r.
\tag{3.1}
$$

**推论 3.1。** 对每个非零 $v\in\ker L$ 及每个整数 $r\ge1$，

$$
\boxed{
\sum_S(1+\ell_r(S))^{3r}|\widehat v(S)|^2=\infty.
}
\tag{3.2}
$$

**证明。** 在 (2.2) 中取 $d=r-1$。对充分大 $m$ 得

$$
\sum_{\ell_r(S)\ge m+1}|\widehat v(S)|^2
\ge c_r^2(m+2)^{-3r}\|v\|^2,
\tag{3.3}
$$

其中 $c_r=[18\sqrt r(34\sqrt6)^r]^{-1}>0$。若 (3.2) 左侧有限，则由可和级数的尾趋零，

$$
(m+2)^{3r}
\sum_{\ell_r(S)\ge m+1}|\widehat v(S)|^2
\le
\sum_{\ell_r(S)\ge m+1}(1+\ell_r(S))^{3r}|\widehat v(S)|^2
\longrightarrow0,
$$

与 (3.3) 矛盾。证毕。

$r=1$ 时，这排除了一个具有明确对角范数的稠密域，其中可以包含非连续且具有无限 Walsh 阶的向量。$r>1$ 给出全部固定阶的更细位置约束。它们都没有覆盖全部 $L^2$ 向量。

## 4. 固定个数的高位多项式近似 Walsh 调制

令

$$
N_j=\frac{A^{2^j}}{\|A^{2^j}\|},\qquad
E_j=e_{10}\text{ 作用在第 }j\text{ 位},
$$

则 R12 给

$$\|N_j\|=\|E_j\|=1,\qquad\|N_j-E_j\|=\eta_j\to0.$$

对有限集 $S$ 定义有界多项式

$$
Q_S=\prod_{j\in S}(I-2N_j),\qquad
R_S=\prod_{j\in S}(I-2E_j).
\tag{4.1}
$$

各 $N_j$ 交换，$Q_S$ 是 $A$ 的多项式。若 $|S|=r$，则

$$
\|Q_S\|,\|R_S\|\le3^r,
\qquad
\|Q_S-R_S\|\le2\,3^{r-1}\sum_{j\in S}\eta_j.
\tag{4.2}
$$

**引理 4.1。** 固定整数 $r\ge1$ 及向量 $h\in H$。当 $|S|=r$、$\min S\to\infty$ 时，

$$
\boxed{\|Q_Sh-\chi_Sh\|\longrightarrow0,\qquad
        \|Q_Sh\|\longrightarrow\|h\|.}
\tag{4.3}
$$

**证明。** 先设 $h$ 仅依赖有限低位，且这些位与 $S$ 不交。第 $j$ 位的常函数满足 $(I-2E_j)1=\chi_j$，所以 $R_Sh=\chi_Sh$。由 (4.2)，$Q_Sh-\chi_Sh\to0$。

一般 $h$ 用有限柱函数 $h_0$ 在 $L^2$ 中逼近。固定 $r$ 后，

$$
\|Q_Sh-\chi_Sh\|
\le(3^r+1)\|h-h_0\|
  +\|Q_Sh_0-\chi_Sh_0\|.
$$

先让 $\min S\to\infty$，再让 $h_0\to h$，得到第一式。$\chi_S$ 是单位模乘法，第二式随之成立。证毕。

本引理的极限顺序是**先固定 $r$，再把所选位整体送往高位**。没有声称 $Q_S$ 在所有 $r,S$ 上一致有界。

还将使用两个直接后果：

1. 固定 $r$ 时，$\chi_Sh$ 的全局 Walsh 次数小于 $r$ 的部分范数趋零。对有限柱函数，新增的 $r$ 个高位全部出现；一般向量由密度得到。
2. 固定 $r$、取 $S\subseteq\{J,J+1,\ldots\}$ 且 $|S|=r$。则 $\chi_Sh$ 中满足 $\ell_r(S')<J+1$ 的 Walsh 分量总范数趋零（$J\to\infty$）。同样先用有限柱函数验证，再作 $L^2$ 逼近。

结合 (4.3)，这两个结论也适用于 $Q_Sh$；相应高次数或高位置部分的范数都趋于 $\|h\|$。

## 5. 闭不变子空间上的有界交织不能统一增加全局次数正则性

令 $\mathsf N$ 为 Walsh 次数算子，$\mathsf N\chi_S=|S|\chi_S$。取任意函数

$$
\omega:\mathbb N_0\to[1,\infty),\qquad
\omega(k)\longrightarrow\infty.
$$

不要求 $\omega$ 单调。相应的闭对角算子为

$$
W_\omega\chi_S=\omega(|S|)\chi_S,
\quad
\mathcal D(W_\omega)=
\left\{h:\sum_S\omega(|S|)^2|\widehat h(S)|^2<\infty\right\}.
\tag{5.1}
$$

**定理 5.1。** 设 $M\subset H$ 是闭 $A$-不变子空间，$Y:M\to H$ 是有界线性算子，满足

$$YA|_M=AY.$$

若 $YM\subseteq\mathcal D(W_\omega)$，则 $Y=0$。

**证明。** 因为 $W_\omega$ 闭、$Y$ 有界且复合 $W_\omega Y$ 在整个 Banach 空间 $M$ 上有定义，闭图定理给

$$\|W_\omega Yf\|\le C\|f\|\qquad(f\in M).\tag{5.2}$$

固定 $f\in M$，写 $h=Yf$。由于 $Q_S$ 是 $A$ 的多项式，$Q_Sf\in M$，且交织关系给

$$YQ_Sf=Q_Sh.$$

固定 $r$，令 $S$ 的 $r$ 个指标整体趋于无穷。记 $\Pi_{\ge r}$ 为全局 Walsh 次数至少 $r$ 的正交投影，$\underline\omega(r)=\inf_{k\ge r}\omega(k)$。由 (5.2)，

$$
C\|Q_Sf\|\ge\|W_\omega Q_Sh\|
\ge\underline\omega(r)\|\Pi_{\ge r}Q_Sh\|.
$$

引理 4.1 及其第一个后果使两边的极限满足

$$C\|f\|\ge\underline\omega(r)\|h\|.$$

这对每个固定 $r$ 都成立。最后让 $r\to\infty$；由于 $\underline\omega(r)\to\infty$，得到 $h=0$。$f$ 任意，所以 $Y=0$。证毕。

特别地，不存在非零有界 $A$ 交换子把整个 $H$ 映入任何正次数 Sobolev 域、任意固定指数次数域或更强的固定快速次数衰减域。即使权 $\omega$ 任意慢地趋于无穷，结论也成立。

## 6. 固定阶高位位置权的对应结论

固定 $r\ge1$，用 §3 的 $\ell_r$ 定义闭对角算子

$$
V_{r,\omega}\chi_S=\omega(\ell_r(S))\chi_S,
\quad
\mathcal D(V_{r,\omega})=
\left\{h:\sum_S\omega(\ell_r(S))^2|\widehat h(S)|^2<\infty\right\}.
\tag{6.1}
$$

**定理 6.1。** 在定理 5.1 的同一交织设定下，若 $YM\subseteq\mathcal D(V_{r,\omega})$，则 $Y=0$。

**证明。** 闭图定理给 $\|V_{r,\omega}Yf\|\le C\|f\|$。固定 $f\in M$、$h=Yf$，这次固定所选位数为 $r$，并取 $S_J\subseteq\{J,J+1,\ldots\}$、$|S_J|=r$、$\min S_J\to\infty$。令 $\Theta_{J,r}$ 为 $\ell_r(S')\ge J+1$ 的 Walsh 分量投影。则

$$
C\|Q_{S_J}f\|
\ge\underline\omega(J+1)
       \|\Theta_{J,r}Q_{S_J}h\|.
$$

由 §4 第二个后果，右侧第二因子趋于 $\|h\|$，而左侧趋于 $C\|f\|$。第一因子趋于无穷，故 $h=0$。证毕。

当 $r\ge2$ 时，$\mathcal D(V_{r,\omega})$ 仍包含全部全局次数小于 $r$ 的无限维空间，其嵌入并不紧。因此定理 6.1 不只是紧交换子排除的改写；证明真正使用了任意多个高位的多项式调制。

## 7. 对原临界核及半群正则化的准确含义

取恒等交织 $Y:M\hookrightarrow H$，两条定理说明：非零闭 $A$-不变子空间不可能整个包含在上述任一固定正则域中。

潜在核 $K=\ker D$ 是闭 $A$-不变子空间。因此：

- §2–3 给其每一个非零向量明确的高位质量下界和位置矩发散；
- 若 $K\ne0$，任何非零有界交织 $K\to H$ 都不能把整个 $K$ 映入某一固定的上述正则域；
- R20/R39 的每个 $S(s)$ 都单射、与 $A$ 及 $D$ 交换。所以若 $K\ne0$，$S(s)|_K$ 是非零有界交织，不能把整个 $K$ 统一送进这些域。同理适用于其他已经验证为非零的有界交织。

这里不排除针对一个特定向量的正则化，也不排除利用实际方程 $Dv=0$ 推出与一般不变子空间不同的额外控制。若真能从该方程证明一个非零有界交织把整个核送入上述域，定理 5.1 或 6.1 反而会完成反证并推出 $K=0$；目前没有证明这种核特有的平滑性。

也不能把“有限阶类稠密”与这些结论拼接成无核证明。§2 的下界虽严格为正，却随 $m$ 或允许阶数增大而趋零，一般 $L^2$ 向量可以满足这样的粗糙性必要条件。
