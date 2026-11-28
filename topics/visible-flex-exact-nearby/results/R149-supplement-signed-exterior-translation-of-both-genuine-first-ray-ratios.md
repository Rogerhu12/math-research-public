# 势支持外两真实首比值的同一有向平移

取原 $n=4|j|\ge388$、$\epsilon=\mathrm{sgn}(j)$、$L=1/2000$、$s=\sqrt{-T}$，原终端基准列、根剪切矩阵及修复族。令
\[
 \lambda_j=\frac12\int_0^L\chi_V(-y)V(j^{-2},-y)y^{-1/2}\,dy .
 \tag{GXM.1}
\]
在 $-T\ge L$ 的真实区域，完整 [WUA.18](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md) 势延拓的 $\mathcal B_j(T)=\lambda_j/s$。这是 $y=h^2(-T)$ 对 $\int_0^1 V_{j,\mathrm{ext}}(h^2T)dh$ 的换元。$\lambda_j$ 为实数，保留原频率、背景和 $\delta$ 依赖；同一所选背景下它不依赖 $r,\phi$。

写 $x=X_\phi,t=\omega_\phi,M_\sigma=G(x-\sigma t)^2/2$。在 [GFW.1–2](R149-supplement-signed-free-first-wave-and-correlated-genuine-potential.md) 记号中，完整首幅在该区域有确切分解
\[
 w_1^V=\begin{pmatrix}
 i\epsilon\sum_\sigma M_\sigma(r_\sigma+\sigma\lambda_j)\\
 s^{-1}\sum_\sigma\sigma M_\sigma(r_\sigma+\sigma\lambda_j)
 \end{pmatrix}.                                                 \tag{GXM.2}
\]
确实 $\sum M_\sigma=G(x^2+t^2),\ \sum\sigma M_\sigma=-2Gxt$，所以新增向量等于 $\mathcal B_j\mathcal K w_0$ 的两个实际分量。两条带号输运方程仍为 $L_\sigma(r_\sigma+\sigma\lambda_j)=F_\sigma$，两物理角导亦保持原有方向。在每个开严格片上令 $f$ 为 GFW.2 原来对 $w_1$ 的完整两分量自由波，$g$ 为同一算子 $\mathfrak A_0$ 对 $(i\epsilon\sum\sigma M_\sigma,s^{-1}\sum M_\sigma)^t$ 的值。因为在此 $V_{j,\mathrm{ext}}$ 及其导数为零，[G.7–9](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md) 的完整局部普通残差恰为
\[
 P\{\mathsf S^{V}(f)+\mathsf S^{V}(g)\operatorname{diag}(\lambda_j)\}.
 \tag{GXM.3}
\]
两 $\mathsf S^V$ 保留真实 $F_n(T)Z_n(-L)$ 和 $n^{1/6}$。也可在每个真实输入处先把 $\lambda_j$ 与 $r_\sigma$ 有向相加，再使用 GFW.2。末端点的 $w_1^V,Dw_1^V$ 同理。原非局部项按其实际算子有序作用于该幅，物理投影并未提前；严格接缝仍用 GJS 的有向跳。支撑或跨支撑界的闭格需使用原势公式。

## 全频率有向标量的严格接收

令 $B$ 是原 $-\partial_y\chi_V(-y)$ 的概率测度所描述的随机变量，即 $\Pr(B>y)=\chi_V(-y)$。由 WUA.18 的 $p_{64}$，
$B=(L/4)(3+Y)$，$Y\in[-1,1]$ 密度正比 $(1-Y^2)^{64}$，故 $Y^2$ 的分布是 $\mathrm{Beta}(1/2,65)$。置
\[
 m_k=\tfrac12\int_0^L \chi_V(-y)(y/L)^k y^{-1/2}dy
 =\frac{\sqrt L}{2k+1}(3/4)^{k+1/2}
     \mathbb E(1+Y/3)^{k+1/2}.
 \tag{GXM.4}
\]
每个偶矩满足 $\mathbb EY^{2d}/\mathbb EY^{2d-2}=(2d-1)/(2d+129)$；所有奇矩精确为零。对 $0\le k\le13$，用二项级数保留到 62 阶，剩余偶项之绝对值比小于 $1/9$，故首遗项的 $9/8$ 倍覆盖整尾。在全真参数域，$|\lambda_j|\le276m_0\le138\sqrt{3L}<27/5$；$\mathbb E\sqrt B\le\sqrt{3L/4}$ 用了 $\mathbb E B=3L/4$。

从原完整有向根阶读出 $V(j^{-2},Rz)=\sum_{k=0}^{12}a_{j,k}z^k+\cdots$，$R=1/32768$。A.5、A.8 的同一整件复像在 $R_T=7/10000$ 上给 $|V|<276$、$|V_{TT}|<3830956$。[原势与复像](R133-supplement-actual-complete-common-radial-potential-and-root-piece-image.md)
取 $q=L/R_T=5/7$。每个自然输入带的 $\lambda_j$ 在以下两个 **有向** 区间的交内，
\[
 \sum_{k=0}^{12}a_{j,k}(-L/R)^k m_k
    \ \pm\frac{276q^{13}m_{13}}{1-q},
 \qquad
 a_{j,0}m_0-(L/R)a_{j,1}m_1
    \ \pm(3830956/2)L^2 m_2.
 \tag{GXM.5}
\]
第一余项先对每个 $y$ 的完整收敛尾用 $(y/R_T)^{13}/(1-q)$，再按正测度积分；第二余项为真实线段上二阶 Taylor 积分余项。两式皆包括过渡区的真实次数 129 截断及完整根均值。首个公开消费者接收从 $|j|=97$ 开始的全部整数和无限尾，记录同一背景族的有向范围、端点和每带精度。GXM.3 的其余几何幅与腰传播仍由各自算子接收。
