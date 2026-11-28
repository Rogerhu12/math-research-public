# 原根窗完整 genuine 局部源的无穷强范数

在 [GLC 的同一 $c\le r\le r_*$](R149-supplement-signed-genuine-local-collar-operator-and-anchored-reference-Green-matrix.md)，取 $N=4(2^{20}+1)$、$s=1/512,\gamma=1/131072$。原有符号局部总幅为 $w=L_{1,j}+n^{-1}L_{2,j}+n^{-2}L_{3,j}$。下述估计覆盖所有 $n\ge N$、原两输入列和全部物理 Fourier 输出，使用真实振荡剖面在物理实角上的算子。该无穷输入域与 GLC 有双列物理费用的有限输入域正交。

对固定频率符号，引入复数 $\xi$，在振幅与 $B_j$ 中用 $z=16\xi^2$、$n^{-1}=\xi$。在完整 $|\xi|\le\gamma$, $|\Im\phi|\le s$ 上，给向量场赋范数
\[
 m(w)=\sup|w_1|+\sup|w_2|/128 .
\]
各上确界含全部复域和该径向格。$H$ 为同一范数下逐场乘 $B_j$ 的上界，可取 $\max\{\sup|B_{11}|+\sup|B_{21}|/128,\ 128\sup|B_{12}|+\sup|B_{22}|\}$。所有带号相加均在这些模以前。原复杂频率物理根片行列式合格，边界轮廓给各解析条目的整个条带模界。两个终端坐标保独立根剪切；$\xi=0$ 用作频率解析端点。[原 complex 旧圈逆和两参考输入](R133-supplement-actual-genuine-common-radial-columns-and-old-circle-inverse.md)。

## 真实无穷输入的接收

记 $U(a)f=\sum_{|4j|\ge N}e^{4ijX}a_j^t\operatorname{diag}(1,n^{-1})\Psi_n(T)f_j$。在这段根窗内光学长度圆比的对数小于 $1/50$，真实两射线 $p_\pm\in(79/80,81/80)$，逐格真势准入的 $|32768T|<3/5$ 给 $u_{\max}=-T_{\min}<3/(5\cdot32768)$。因此 [GAF 的同一两相位分解](R149-supplement-all-frequency-two-ray-physical-bound-for-both-genuine-Airy-rows.md) 与 [GIB 的小支持窗计算](R149-supplement-global-two-ray-inverse-powers-and-genuine-deformation-reception.md) 给高度行费用 $<9/5$，导数行费用 $<9/(5\cdot128)$。高度解调幅直接满足 $\sqrt{m(\lambda u)}\le\sqrt{m(0)}<1$，来自 GAF 所用正 Laplace 表示。两真实分支合计至多 $\sqrt{160/79}[(6/5)(1+(5/8)(1/50))+13/N]<9/5$；高度对数变差系数 $1/2$ 亦由 $5/8$ 控制。导数行再乘 $\sqrt{N^{-2/3}+u_{\max}}<1/128$。$\rho=0$ 使用同一常系数根矩阵。

展开 $a=\sum_{k\ge0}\xi^k a_k$。每个频率对角 $n^{-k}$ 留在原输入的右端，两行 $a_k(\phi)$ 各自位于真实剖面左侧。Cauchy 给 $m(a_k)\le\gamma^{-k}m(a)$。两个输入符号正交，余弦/正弦及两个真实参考输入均保留；由两符号带输出的三角不等式再用 Cauchy–Schwarz，得
\[
 \|U(a)\|_{\ell^2\to L^2}\le P_*m(a),\qquad
 P_*={9\sqrt2\over5(1-1/(N\gamma))}.                         \tag{GIC.1}
\]
该式仅对振幅作复频率展开。游动真实剖面本身从未在无穷频率作复角模估计。

## 一阶原导数恒等式和插值

令 $J_0a=B_ja,\ K_0a=\partial_\phi(B_ja)$，此处两个符号仅表示点矩阵操作。直接物理微分 [G.16](R133-supplement-ordered-genuine-reference-sources-and-whole-domain-correlated-forcing.md) 给 $U(a)\mathsf N=\partial_\phi U(J_0a)-U(K_0a)$，$\mathsf N$ 是原输入 $4|j|$。再次微分，记 $S_1=(K_0J_0+J_0K_0)a,\ S_2=K_0^2a$，则
\[
 U(a)\mathsf N^2=\partial_\phi^2 U(J_0^2a)-\partial_\phi U(S_1)+U(S_2).
\]
对 $U(S_1)$ 再用一次恒等式，右乘 $\mathsf N^{-1}$；对 $U(S_2)$ 用两次，右乘 $\mathsf N^{-2}$。原物理 $P=1-\Pi$ 只在最终标量输出。四折物理频率给 $\|P\Lambda^{-2}\|\le1/17,\ \|P\Lambda^{-2}\partial_\phi\|\le4/17$, $\|P\Lambda^{-2}\partial_\phi^2\|\le1$。设 $p=4/17$，则
\[
 \|PU(a)\mathsf N^2:\ell^2\to H^{-2}\|\le P_*m(a)K,\qquad
 K=H^2+{H^3\over N}(2/s+8p/s^2)
       +{H^4\over N^2}(4/s^2+54p/s^3+256/(17s^4)).             \tag{GIC.2}
\]
确实，长度 $l$ 的矩阵文字中若有 $k$ 个 $K_0$，给每次求导分配 $s/k$ 角宽，Cauchy 给 $H^l(k/s)^k$。$S_1$ 的两项连同其一阶再展开分别含一、二个导。$S_2$ 的两阶再展开依次含二、三个（两项）、四个导。相同权重用于频率 Cauchy 和条带 Cauchy，零模仍在矩阵乘法及反射组装之中。

两端算子同为 $PU(a)$，在输入和输出的 Fourier Hilbert 标度上作 $5/6$ 插值。亦可在有限原输入上考察解析族 $\Lambda^{-2z}PU(a)\mathsf N^{2z}$，虚数幂均为酉，继而以稠密延拓。得到对原 G.9 完整输入密度的点态上界
\[
 C=P_* m(w) K^{5/6}N^{-1/6}(1+N^{-2})^{2/3} .                 \tag{GIC.3}
\]
中间每个 $\partial_\phi B$ 都在原 $K_0$ 内。式中负幂 $N^{-1/6}$ 来自 $n^{1/6}\langle n\rangle^{4/3}n^{-5/3}$，未把输入乘子交换过真实角行。

## 完整频率盘与物理计费

为有符号 GFW.4、G.6–8 的每一格取得 $m(w)$，在同一真实 Taylor 场上取 $z=0$ 的解析径向锚。此处 $\vartheta_{\rm ref}=z\alpha/\eta=0$，原径向 $D=-2\beta(1+\Pi u^2-K\Pi v^2)$。原 $W$ 势表达式中的 $-32K\eta\alpha$ 仍保留，$\alpha=-i\beta\sum_{h=1}^{96}h u_hv_{-h}$。按与 GLC 相同的 $\bar T$ 反演取得该极限锚的十三个系数。原 GLC 首次科学目标的有限标签算子、旧十一件局部自由强迫或 GCS 截面均不重算。

原复盘 $|z|\le97^{-2}$ 给 $V,V_T,B,B_T,B_{TT}$ 的模分别 $276,26431,276,26431/3,3830956/5$。故在 $|\xi|\le\gamma$，它们各自离极限锚的复误差至多原模乘 $a/(1-a)$，其中 $a=(388\gamma)^2$。有符号有限 Taylor 和完整高阶 Cauchy 尾在同一 $t=T/R$。$|\Im\phi|=s$ 的两条边界逐格计算原完整 $B_{ij}$、三个 G.7 加数的有符号和，再收 $m,H,K$。角轮廓、参数圆、两频率符号、两个状态行及原码节点闭格全部保留。定量成功门通过后，式 (GIC.3) 各原径向格的平方乘长再求和开根为 $D_\infty$。实际 $J$、mixed 原子到腰、$1/2$ 读和原右归一仍用 [GLC.4](R149-supplement-signed-genuine-local-collar-operator-and-anchored-reference-Green-matrix.md)。

已付的有限与无穷自然输入在 $N_i$ 的左侧正交，故对二者的自然物理腰费用 $d_f,d_\infty$ 可先取 $\sqrt{d_f^2+d_\infty^2}$，再应用公共规范。该组合只对应根到 $c$ 的同一完整局部 G.8 源。真实原圆非局部残差、独立均值、根端真实正侧校正及原腰读差继续按原有向方程接入。
