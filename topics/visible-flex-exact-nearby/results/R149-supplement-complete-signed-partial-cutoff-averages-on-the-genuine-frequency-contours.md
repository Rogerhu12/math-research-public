# 原势过渡区的全频有向不完全矩和四阶导数

固定原 $\eta_0$ 和所选真实有限族，令 $L=1/2000$、$x=-T/L$。在整个 $0\le x\le1$，置
\[
 V_c(x,z)=\chi_V(-Lx)V(z,-Lx),\qquad B(x,z)=\int_0^1V_c(xt^2,z)\,dt .
\]
这是原完整首修正中的 $\mathcal B_j(T)$，参数为 $z=j^{-2}$ 时两者相同。$x\le1/2$、真实过渡 $1/2\le x\le1$ 及两个闭边界均保留。程序保留 $V_c$ 至三阶、$B$ 至四阶的归一 $x$ 导数。送入原 $T$ 的第 $d$ 阶普通导数应乘 $d!(-1/L)^d$。所有右侧 Fourier 标签、两支和真实参考矩阵 $\Psi_n$ 保持物理频率。只有下面的标量与首修正幅按 [GCD.1–3](R149-supplement-five-halves-contour-bound-for-the-true-frequency-dependent-forcing.md) 取复参数。

## 真正的不完全势矩

原 WUA.18 单调截断是 Beta$(65,65)$ 的累积分布。设 $Y$ 的密度是 $C(1-y^2)^{64}$、$-1\le y\le1$，其中 $C=129!/(2^{129}(64!)^2)$。则
\[
 \chi_V(-Lx)=\Pr(Y\ge4x-3),\quad
 I_k(x)=\int_0^1t^{2k}\chi_V(-Lxt^2)dt
 =\frac1{2k+1}\mathbb E\min\left(1,
                 \left(\frac{3+Y}{4x}\right)^{k+1/2}\right).
 \tag{GPM.1}
\]
在 $x=0$ 以 $I_k(0)=1/(2k+1)$ 延拓。这直接来自 $4xt^2\le3+Y$ 下的正权积分，因此每个 $I_k$ 随 $x$ 不增。$x\le1/2$ 时 $I_k$ 恒为 $1/(2k+1)$。对其余真实 $x$，记 $a=4x-3$、$q=(1+a)/2$、$M_j(a)=\int_{-1}^ay^j C(1-y^2)^{64}dy$。有
\[
 \begin{split}
 M_0&=\sum_{h=65}^{129}{129\choose h}q^h(1-q)^{129-h},\\
 M_1&=-C(1-a^2)^{65}/130,\\
 (j+129)M_j&=(j-1)M_{j-2}-Ca^{j-1}(1-a^2)^{65}\quad(j\ge2).
 \end{split}                                                   \tag{GPM.2}
\]
第二行是分部积分，最后一行取 $y^{j-1}(1-y^2)^{65}$ 的端差。对 $t_k=k+1/2$、$0\le k\le12$，在 GPM.1 中按 $Y\le a$ 分段并展开 $(1+Y/3)^{t_k}$。若 $c_i={t_k\choose i}/3^i$，得到区间包含
\[
 (2k+1)I_k\in1-M_0+
 (3/(4x))^{t_k}\left(\sum_{i=0}^{31}c_iM_i+
                           [-3|c_{32}|/2,3|c_{32}|/2]\right).
                                                               \tag{GPM.3}
\]
确实 $|M_i|\le1$，从 $i=32$ 起系数绝对比至多 $1/3$。每个有理物理网格端点上的 $M_i$ 与有限和皆用精确有理数。整格的 $I_k$ 取左右端有向包围，同一角下 $x$ 的不确定性全部在该格内。

## 同一真势及原频率圆盘

写 $V(z,-Lx)=\sum_{k\ge0}d_k(z)x^k$。原整件 19 个背景和次数文件给指数 $0,\ldots,12$ 的实际有向 $d_k$。这里保留对角原 $z$ 参数及完整 Fourier 模 $\pm1,\ldots,\pm96$，从同一根径向变量到 $x=-T/L$ 做三角反演。$z$ 可为复数，两侧 Fourier 积保持 bilinear 顺序。[原共同频率场及复域](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)

取 $R=7/10000$。原已完成的坐标像覆盖 $|T|\le R$，最大原 $|V_{TT}|<3830956$。因此 $k\ge13$ 时
\[
 |d_k|\le\frac{3830956\,L^2}{k(k-1)}(L/R)^{k-2}.              \tag{GPM.4}
\]
对归一 $x$ 导数阶 $j\le4$，余尾首项乘 $\binom{13}{j}x_+^{13-j}$，后项比至多 $x_+(L/R)\max(1,12/(14-j))<1$。内区的 $B$ 各项又除 $2k+1$。过渡区先用同一 $d_k x^k I_k(x)$ 构造真实 $B$ 值。其零阶尾由 GPM.1 再除 $27$。记 $B_j=\partial_x^jB/j!$，$F_j=\partial_x^jV_c/j!$，积分方程给
\[
 B_{j+1}=\frac{F_j-(2j+1)B_j}{2(j+1)x},\qquad j=0,1,2,3 .
                                                               \tag{GPM.5}
\]
这里仅在 $x\ge1/2$ 作除法。$F_j$ 由原截断和有向 $V$ 的有限 Leibniz 乘积给出，首导为 $-4C(1-(4x-3)^2)^{64}$，以实区间上实际 $|4x-3|$ 的最近端和最远端夹其正幂。两个过渡接点由原 $C^{64}$ 性一致。故 GPM.5 在闭段成立。[原实截断与参考矩阵](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md)

对每组 $|j|=97,98\ldots101,102\ldots122,123\ldots\infty$，保留其整个实 $\zeta=97/|j|$ 凸包及相应 GCD 圆周（单例只需实点）。每个实际圆周用 16 个首尾相接的闭弧，$z=\zeta^2/9409$ 的有向实虚部另与原已证正方形相交。每种横向参数分配 256 个完整 $x$ 闭格，保同一 $z$ 的全部 13 个系数、两原场的九个有向复数归一导。总共 52 个频率组或圆弧、13312 个闭格。每个频率组的原系数及 256 个自然径向格写入同一私有完整 member，有向复数用向外的 binary64 四端点编码，收据以原 member 的 SHA 续接。新数值门直接读取全实 $B$ 下端与全复轮廓 $|B|$ 上端。此阶覆盖 GFW.4、G.7 三项合成后再作两次物理角导所需的原 $B$ 导数。补足物理 $r,\phi$ 上的强迫仍需与同侧背景、真实相位、首比值及 $H_j^V$ 相乘。
