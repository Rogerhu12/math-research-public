# R114：受约束常态第四成本、八矩正锥与真实有限圈字

日期：2026-11-14。**已证明。** 本稿为纸面推导，没有新的研究计算。依据 [R62](R62-reciprocal-constant-states-and-fourth-local-drift.md)、[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md) 与 [R112](R112-local-fourth-geometric-derivative-weights.md)。

本稿给静态局部 consumer 的实际约束接口。单个几何系数不属于 $\mathcal R_8$，本身不意味着有可独立调节的真实成本。正确的静态门先要求**正时长的常态矩阵配平**，并保留所有真实连接、完整框架周期及有限圈数校正。下文还把“所有配平静态成本为零”化成一个只有八个几何函数的准确商条件。

## 1. 固定对象与常态八坐标

继续使用 R109 的完整相位目标、同一右 collar、同一 profile 原函数及 canonical 恢复。记

$$
m=m^{[0]}+m^{[2]},\qquad
\mathscr L_4=v-\mathcal B_mN
=\mathscr L_4^{[0]}+\mathscr L_4^{[2]}+\mathscr L_4^{[4]}.
$$

这里上标是几何导数权。取一个真实常态

$$
S=(h,k,\omega),\quad h>0,\qquad d=h\omega-k,\quad Q=1+d^2.
$$

令 $m_0(S)=m^{[0]}(S)$，$\ell_0(S)=\mathscr L_4^{[0]}(S)$。二者不含累计历史。按照 R73 的八坐标顺序，准确有

$$
\begin{aligned}
p_0&=-\frac{kQ}{2h},&
p_1&=-kd,&
p_2&=-\frac{kh}{2},\\
r_0&=\frac{Q(d+k)(kd-1)}{8h^3},&
r_1&=\frac{Q(k^2+2kd-1)}{8h^2},\\
s_0&=\frac{d(d+k)(kd-1)}{4h^2},&
s_1&=\frac{d(k^2+2kd-1)}{4h},&
t_1&=\frac{k^2+2kd-1}{8}.
\end{aligned}\tag{1}
$$

第九系数是 $t_0=p_0/4+s_1/2$。与二次 profile 基 $1,\xi,\xi^2$ 对应的矩阵为

$$
M_0(S)=
\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix}
\in\mathfrak{sl}_3(\mathbb R).
\tag{2}
$$

式 (1) 直接由 R73 点态公式在 $h_s=k_s=0$ 时得到；特别 $\omega=(d+k)/h$，没有在不同状态间把 $\omega$ 重置成一个共同数。

矩阵与完整二次算子一一对应，下文不再区分 $m_0$ 与 $M_0$。一个常态的完整框架周期为

$$
\tau(k)=\frac{2\pi}{\sqrt{1+k^2}}.
$$

它给真正的整圈矩阵及局部商成本

$$
D(S)=\tau(k)m_0(S),\qquad
c(S)=\tau(k)[\ell_0(S)].
\tag{3}
$$

方括号表示模 $\mathcal R_8=\operatorname{span}\mathcal B_{E_8}(W)$。先在 R105 的有限模板空间中工作，必要时加入 R109 局部势产生的有限模板；这是有限维真实函数空间，不把正规化代表独立当成真实函数独立。

## 2. 第八方向及完整正锥

取

$$
\mathbf w(h,d)=
\begin{pmatrix}
Q/(4h^2)\\ d/(2h)\\1/4
\end{pmatrix},\quad
\mathbf a(h,d)=
\begin{pmatrix}0\\1\\-2d/h\end{pmatrix},\quad
\mathbf b(h,d)=
\begin{pmatrix}-2h\\2d\\-2(d^2-1)/h\end{pmatrix}.
$$

逐列核对 (1)–(2) 得

$$
M_0(h,d,k)=
\mathbf w\bigl((k^2-1)\mathbf a+k\mathbf b\bigr)^T.
\tag{4}
$$

$\mathbf a,\mathbf b$ 独立，且都垂直于 $\mathbf w$。

这里可以把四个正则状态全部取为

$$
(h_i,d_i)=(1,0),(1,1),(1,-1),(1,2).
\tag{5}
$$

相应 $\mathbf w_i$ 的射影代表是

$$
v_1=(1,0,1)^T,\quad v_2=(2,2,1)^T,\quad
v_3=(2,-2,1)^T,\quad v_4=(5,4,1)^T.
$$

前三者行列式为 $-4$，且

$$
v_4=-3v_1+3v_2+v_3.
\tag{6}
$$

令 $A_i=\mathbf w_i\mathbf a_i^T$、$B_i=\mathbf w_i\mathbf b_i^T$。如果一个矩阵 $Y$ 对全部八个 $A_i,B_i$ 的 trace 配对为零，那么 $Y^T\mathbf w_i$ 同时垂直于 $\mathbf a_i,\mathbf b_i$，故与 $\mathbf w_i$ 平行。前三条线是本征基；(6) 的三个系数都非零，迫使三个本征值相等。因此 $Y$ 是标量矩阵。于是

$$
\operatorname{span}\{A_i,B_i:1\le i\le4\}
=\mathfrak{sl}_3,\qquad\dim=8.
\tag{7}
$$

在每个固定 $(h_i,d_i)$ 上，

$$
M_0(0)=-A_i,\qquad M_0(1)=B_i,\qquad
M_0(-1)=-B_i,\qquad M_0(2)+M_0(-2)=6A_i.
\tag{8}
$$

所有 $\tau(k)>0$，所以取 $k=0,\pm1,\pm2$ 的二十个真实整圈，已经使其矩阵的有限正锥等于全部 $E_8$：

$$
\boxed{\operatorname{cone}\{D(S):S\text{ 为真实常态}\}=E_8.}
\tag{9}
$$

这里正锥系数是后文先研究的静态占用量；还未把任意实系数授予为整圈数。

式 (1) 另给很直接的第八方向证据：

$$
p_1+4t_1=\frac{k^2-1}{2}.
\tag{10}
$$

因此 $k=\pm1$ 的 R89 物理族仍只有七维；本稿并没有推翻这个结论。$k=0$ 给 (10) 的负方向，$k=\pm2$ 给正方向，才补齐八维。

虽然 (5) 的常态都满足 $h=1$，它们之间的真实桥一般必须改变 $h$，以满足 $\omega_s=k_s/(2h)$ 及指定的 $\omega$ 端口。本稿从不声称完整路径恒 $h$，与 R97 完全相容。

## 3. 正配平静态占用量

定义有限正配平成本集合

$$
\mathcal C_{\rm stat}=
\left\{
\sum_{j=1}^Jt_jc(S_j):
t_j>0,\quad
\sum_{j=1}^Jt_jD(S_j)=0,\quad J<\infty
\right\}\cup\{0\}.
\tag{11}
$$

系数 $t_j$ 是相对圈数的连续记账量，而非已经实现的非整数框架圈。其真实实现将在第 5 节给出。

为了不循环选择物理区间，先选有限状态、参数邻域和连接族，再从其紧 scalar 包络外选共同 $\xi$ 区间，使 $\xi+\omega$ 有统一正下界。所有后续重复只增加圈数，不扩大这个 scalar 包络。没有保证任意预先指定的窄区间、总长或 $h,k$ 控制盒。

### 准确静态商判据

以下两条等价：

1. $\mathcal C_{\rm stat}=\{0\}$；
2. 存在一个固定线性映射 $G:E_8\to E_4/\mathcal R_8$，使对全部真实常态

$$
\boxed{[\ell_0(S)]=G(m_0(S)).}
\tag{12}
$$

**证明。** (12) 对每个 (11) 显然给零。反向，先考虑任意有限带符号关系

$$
\sum_ja_jD(S_j)=0.
$$

把正、负部分的公共矩阵和记为 $M$。由 (9)，存在有限正组合 $\nu$，其矩阵和为 $-M$。正部分加 $\nu$、负部分加同一个 $\nu$ 都是正配平组合，所以两者成本均零；相减得 $\sum_ja_jc(S_j)=0$。因此赋值 $D(S)\mapsto c(S)$ 尊重全部线性关系，且这些 $D$ 张成 $E_8$，从而定义唯一线性 $G$。再消去正因子 $\tau(k)$ 即得 (12)。这只是函数线性空间中的证明，没有把实际路径成本允许相减。证毕。

同样，对任意线性泛函 $\Lambda$，

$$
\Lambda(\mathcal C_{\rm stat})=\{0\}
\iff
\exists\mu\in E_8^*,\ 
\Lambda([\ell_0(S)])=\mu(m_0(S))\quad\forall S.
\tag{13}
$$

这个判据明确说明：逐个静态几何系数属于 $\mathcal R_8$ 是充分条件，但一般不是正确的必要条件。必须允许八个二阶矩函数的固定线性组合。

## 4. 八个有理基准状态给直接可消费的归一化

取 (5) 每组的 $k=0,1$，共八个状态 $S_i^*$。由 (7)–(8)，$m_0(S_i^*)$ 是 $E_8$ 的一组基，且其坐标全为有理数。它们全部满足 $h=1$，所以若局部势含 $\log h$，在这些基准点上也不会新增 $\log2$ 等系数。

对任意 $S$，唯一写成

$$
m_0(S)=\sum_{i=1}^8a_i(S)m_0(S_i^*).
$$

则 (12) 准确等价于

$$
\boxed{
\ell_0(S)-\sum_{i=1}^8a_i(S)\ell_0(S_i^*)
\in\mathcal R_8\quad\forall S.
}
\tag{14}
$$

$a_i(S)$ 只需对 (1) 的八个有理坐标做一次固定 $8\times8$ 线性变换。局部密度已经导出时，(14) 只消费现有原式，不需要重编 forcing、第三模板或几何积分。它可以按相同 profile 仿射权分块，但必须保完整两个相位和同一实响应系数。

有限 Laurent/log 几何单项的系数匹配可作为这个原式身份的准确有限实现；非零改写余项本身仍不是函数非成员证书。

此外，若把 R109 的局部势加一个与状态无关的第三算子 $C$，则静态密度改变为 $-\mathcal B_{m_0(S)}(C)$。这正是 (12) 允许的固定线性矩函数；故正配平门不会受这种未付常势参考值影响。

## 5. 正规八圈与真实整数化

固定一个 (11) 中的有限正配平表。为保证整数化和连接成本可由准确 IFT 支付，附加任意小正权 $\varepsilon>0$ 的正规八圈：四组 (5)，每组取

$$
k_{i,+}=1+\alpha_i+\beta_i,\qquad
k_{i,-}=-1-\alpha_i+\beta_i,
$$

并固定各组 $h_i,d_i$，所以每个 $\omega$ 端口按 $(d_i+k)/h_i$ 真正变化。每段走其自身完整周期。零参数时，每组的矩阵和为零。对 $\tau_1=\sqrt2\pi$，直接微分 (4) 及真实 $\tau(k)$ 得

$$
\partial_{\alpha_i}(D_{i,+}+D_{i,-})=4\tau_1A_i,\qquad
\partial_{\beta_i}(D_{i,+}+D_{i,-})=\tau_1B_i.
\tag{15}
$$

(7) 使这八列可逆。乘 $\varepsilon>0$ 不改变可逆性。记这个正规八圈的静态成本为 $q_{\rm reg}$，原表成本为 $q$；附加表的成本是 $q+\varepsilon q_{\rm reg}$。

给全部常态段按固定顺序加入真实平滑连接，首末为同一常 scalar germ、frame 从 $I$ 回 $I$。R70 的局部参数 IFT 给一组随八参数光滑变化的有限连接；其辅助圈数一开始选定，**独立于外层圈数 $N$**。每个真实常段完整周期的 frame 恒为 $I$，所以连接的总矩阵 $C(p)$ 及其参数导数不随外层圈数增长。所有端口 $\omega$ 由真实微分方程连续传递，不重置。

对附加表的每个正权 $t_j$，取真实整数圈数

$$
n_j(N)=\lfloor Nt_j\rfloor
$$

（充分大 $N$ 时均为正）。令 $D_j(p)$ 为该常态一整圈的矩阵。完整矩阵方程为

$$
\sum_jn_j(N)D_j(p)+C(p)=0.
\tag{16}
$$

除以 $N$ 后，参数为 $n_j(N)/N=t_j+O(N^{-1})$ 及 $N^{-1}$。在 $p=0$、极限权 $t_j$、$N^{-1}=0$ 处，左侧为零，八参数导数由 (15) 可逆。因此普通有限维 IFT 给每个充分大有限整数 $N$ 的真实解

$$
p_N=O(N^{-1}).
\tag{17}
$$

这里固定 $\varepsilon$ 后使用 (17)；其常数可以依赖 $\varepsilon$。若以后令 $\varepsilon\to0$，可以先相应增大 $N$，使所有 $p_N$ 仍位于同一个预先固定的小参数邻域。没有把非整数圈补成一个不闭 frame 的短段，也没有把数值近零当成准确矩阵零。

## 6. 局部商成本的极限与有限 N 结论

沿第 5 节的真实路径 $B_N$，全部常态 jets 为零；连接在固定参数邻域中长度及 jets 有界。R109 给

$$
[V_{B_N}]
=
\left[\int_{B_N}\mathscr L_4\,ds\right]
=
\sum_jn_j(N)c_j(p_N)+C_4(p_N),
\tag{18}
$$

其中 $C_4$ 是所有真实连接的完整局部成本，保留几何导数权 $0,2,4$，并未设为零。由于它不接收累计历史，$C_4$ 在此紧参数族中为 $O(1)$。原始第四历史可以有高次 $N$ 项；(18) 仅在 R109 已证的真实函数商中把这些项消到 $\mathcal R_8$，不是在原第四成本里删掉桥效应。

由 (17) 及局部系数光滑性，

$$
[V_{B_N}]
=N(q+\varepsilon q_{\rm reg})+O(1).
\tag{19}
$$

$B_N$ 已有准确 $M=0$，但通常 $T\ne0$。同端口真倒行满足 $T_{B_N^R}=-T_{B_N}$、$V_{B_N^R}=V_{B_N}$，所以

$$
B_NB_N^R:\quad M=T=0,\qquad
V_{B_NB_N^R}=2V_{B_N}.
\tag{20}
$$

frame 也从 $I$ 回 $I$。空间位移没有被指定为零；这符合 R105 中真实成本路径的范围。

有限维空间 $\mathcal U_4/\mathcal R_8$ 对极限封闭。由 (19)–(20) 先令 $N\to\infty$，得 $q+\varepsilon q_{\rm reg}$ 属于该空间；再令 $\varepsilon\to0$，得

$$
\boxed{
\operatorname{span}\mathcal C_{\rm stat}
\subseteq \mathcal U_4/\mathcal R_8.
}
\tag{21}
$$

这是**成本线性跨度的包含**。没有把极限向量本身冒称一个有限实际路径的准确成本，也没有把有限路径的加法半群变成实向量空间。

如果某个 $q\in\mathcal C_{\rm stat}$ 真非零，则先取足够小 $\varepsilon>0$ 使 $q+\varepsilon q_{\rm reg}\ne0$，再取充分大有限 $N$。由 (19)，已经得到一个真实有限 $M=T=0$ 路径，其成本商非零。故这种非零性不只存在于无限圈极限。

若还要求该原料的中心线准确闭合，可在 $B_N$ 后接一个固定同 scalar 的 $M=T=0$、frame $I\to D$ 桥，再用 R45 的 $P,P,P^R,P^R$。它保留固定桥成本、给中心位移和 frame 的准确闭合，完整成本为单 $P$ 的四倍；因此非零 leading 商在充分大有限 $N$ 仍保持。这只给周期正则浸入环带，不给嵌入、reach 或无边界闭面。

## 7. 对当前未决静态系数的实际含义

若未来从原式证 (14) 全部成立，则所有正配平常态 leading 成本在 $\mathcal R_8$ 中；这仍不清除连接的导数权 $2,4$ 或有限 $O(1)$ 基准。

若从原式证 (14) 真失败，则第 3 节给某个有限正配平 $q\ne0$，第 6 节把它变成真实有限非零商成本。失败必须是实际函数身份的失败，例如准确分离泛函；不完备正规化留下非零代表还不够。

这个新门不声称任意完整成本可正负调节，不支付完整第四 ruling、半群剩余商、更高阶收敛、宏观幅度或厚度。它准确补上了“静态系数”与“真实受约束路径”之间的缺环。
