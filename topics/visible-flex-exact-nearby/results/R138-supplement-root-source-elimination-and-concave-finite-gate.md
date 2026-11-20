# R138 补篇：根型的完整源项消元与轴坐标凹性

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇给出两个可直接接到真实根型消费者的解析步骤。第一，完整
\(\mathsf H\) 与独立均值项在分部积分后有一个准确抵消，使齐次根型的
定量正性足以给出非齐次常数 \(C_{\rm mov}\)。第二，根位置的两个已付
坐标不必被压成一个粗矩阵扰动：有限 Schur 型对这两个坐标是矩阵凹的，
所以可以核完整坐标矩形的四个顶点。这里没有宣告尚未计算的有限正性门通过。

所有积分使用完整 \(2\pi\) 圈的归一平均，所有范数也使用归一 \(L^2\)。
这只是把 [根型补篇](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)
(U.14)--(U.15) 的型与范数同时除以 \(2\pi\)，不改变常数。角变量仍是
moving \(\phi\)，原 low \(1\le j\le96\) 与 high \(j\ge97\) 不变。

## 1. 完整非齐次项的抵消

令 \(h=\mathsf H\)，并沿用 (U.12) 的同一真实 mean 列 \(g_m\)、
\(\ell=X(r_*,0)\) 和已付 \(\mathcal D>17/20\)。写
\[
 \omega_0=I\mathcal Rf,\qquad
 \ell_h=\mathcal D^{-1}\langle h\rangle\cdot\ell,\qquad
 V=I(h-g_m\ell_h),\qquad \omega=\omega_0+V.
 \tag{F.1}
\]
\(I\) 是完整环境向量圈的零均值 primitive，不能改用 scalar 四重
primitive 的 \(1/4\) 常数。原周期相容式与对称性给
\(\langle h-g_m\ell_h\rangle=0\)，故 \(V'=h-g_m\ell_h\)。
同样 \(\omega_0'=\mathcal Rf\)。

由 (U.14) 准确展开，再对唯一的 \(V\times\omega_0'\) 项分部积分，得到
\[
\boxed{\begin{split}
 \widetilde{\mathcal B}_L/(2\pi)
 ={}&\mathfrak b_*(f)/(2\pi)
 -\langle G'\cdot(V\times\omega_0)\rangle
 -2\ell_h\langle G\cdot(\omega_0\times g_m)\rangle\\
 &-\langle G\cdot(V\times h)\rangle
 -\ell_h\langle G\cdot(V\times g_m)\rangle .
\end{split}}
\tag{F.2}
\]
具体地，交叉项中的
\(\langle G\cdot[V\times\omega_0']\rangle\) 等于
\(-\langle G'\cdot(V\times\omega_0)\rangle
 +\langle G\cdot[\omega_0\times(h-g_m\ell_h)]\rangle\)。
它与另一个交叉项
\(\langle G\cdot[\omega_0\times(-h-g_m\ell_h)]\rangle\)
相加，恰好消掉直接的 \(h\) 项，而保留两份 mean 项。

这一恒等式先对光滑同域方向证明。对实际弱核，
[V 补篇](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)
已识别同对象的完整 base-order 解并支付能量与根迹；下面的有界配对使
(F.2) 由该同域稠密逼近延拓。没有把 \(h\) 设为零，也没有把 WVC hybrid
当作真正 \(DF(Q^{\rm repair})\)。

## 2. 可直接计算的 \(C_{\rm mov}\)

在非零环境频率 \(|k|\ge1\) 上，采用
\(\langle k\rangle=(1+k^2)^{1/2}\)。准确 primitive 范数为
\[
 \|I\|_{H^{-1/3}\to L^2}=2^{1/6},\qquad
 \|I\|_{H^{-1/3}\to H^{1/3}}=2^{1/3},\qquad
 \|I\|_{L^2\to H^{1/3}}=2^{1/6}.
 \tag{F.3}
\]
令 \(d=20/17\)，取同一真实全圈的界
\[
 G_0\ge\|G\|_\infty,\quad G_1\ge\|G'\|_\infty,
 \quad g_0\ge\|g_m\|_\infty.
\]
则 \(|\ell_h|\le d\|h\|_{H^{-1/3}}\)，且
\[
 C_{V,0}=2^{1/6}+d g_0,\qquad
 C_{V,1/3}=2^{1/3}+d\,2^{1/6}g_0
 \tag{F.4}
\]
分别控制 \(V\) 的 \(L^2\)、\(H^{1/3}\) 范数。这里
\(\|Ig_m\|_{L^2}\le\|g_m\|_{L^2}\le g_0\)，无需假定
\(g_m\) 自身零均值。

对 \(S=P_LN+P_HN^{1/3}\)，假设真实齐次型已定量支付
\[
 \mathfrak b_*(Sz)/(2\pi)\ge\lambda\|z\|_2^2,
 \qquad\lambda>0,
 \qquad\|I\mathcal R S z\|_2\le C_\omega\|z\|_2 .
 \tag{F.5}
\]
后一个量可直接用完整根型的无导数展开：若
\(\omega_0=y+Iv_z\)，则 \(C_\omega=Y_*+V_*\) 是充分界，
其中必须保留真正的 \(g_m\mathcal D^{-1}\) mean rank。

对 \(G\) 的叉乘矩阵，\(H^0\) 与 \(H^1\) 乘子范数分别至多
\(G_0\)、\(G_0+G_1\)。Hilbert 插值给
\[
 M_{G,1/3}=G_0^{2/3}(G_0+G_1)^{1/3}.
 \tag{F.6}
\]
因此 (F.2) 的两个交叉项与两个纯源项分别由
\[
\begin{split}
 C_\times&=(G_1 C_{V,0}+2dG_0g_0)C_\omega,\\
 C_{\rm quad}&=M_{G,1/3}C_{V,1/3}+dG_0g_0 C_{V,0}
\end{split}
\tag{F.7}
\]
控制。第一项只用 \(L^2\times L^2\) 配对；第二行中的第一项是
完整 \(H^{1/3}\)--\(H^{-1/3}\) 对偶，不能用未支付的点态 \(h\) 范数。
对 \(\|z\|_2\) 完成平方得到
\[
\boxed{\quad
 \widetilde{\mathcal B}_L/(2\pi)
 \ge -C_{\rm mov}\|\mathsf H\|_{H^{-1/3}_\phi}^2,
 \qquad C_{\rm mov}=C_{\rm quad}+\frac{C_\times^2}{4\lambda}.
 \quad}
 \tag{F.8}
\]
同一真实密度拉回满足
\(\|\mathsf H\|_{H^{-1/3}_\phi}\le\sqrt{A_\Theta}
 \|H\|_{H^{-1/3}_\theta}\)。因而接到 V 的根费用是
\(C_*=A_\Theta C_{\rm mov}\)。这里 \(A_\Theta\) 读取已完成的 X
完整保存球，不重算旧角图目标；\(C_*\) 随后进入 V 的三个完整吸收门，
并非仅检验 \(C_*=0\) 的 body-only 诊断。

## 3. 轴坐标的完整包络与有限凹性

固定实际 frame、背景与 mean 列。在 (U.21) 的同一个环境坐标中，
\[
 G(\phi;q,s)=G_{\rm inc}(\phi)+q e_z+s e_x,
 \qquad G_{\rm inc}(0)=0.
 \tag{F.9}
\]
所以齐次有限矩阵 \(K_F\) 与未投影主系数
\(a_0=2\rho^2(G\cdot n)/(-v)\) 都对 \((q,s)\) 仿射。
frame、\(g_m\)、\(\mathcal D\) 和原 96/high-97 域不随这两个坐标变化。

需要保留一个对称性细节：任意矩形顶点改变的是环境常向量，未必沿真实
旋转轴，因此该顶点的 \(G\) 本身未必四重等变。定义
\[
 a(\phi;q,s)=\frac18\sum_{j=0}^{3}
 \{a_0(\phi+j\pi/2;q,s)+a_0(-\phi+j\pi/2;q,s)\}.
 \tag{F.9a}
\]
原 odd-fourfold scalar 空间中，\(\langle a_0fq\rangle=
\langle afq\rangle\)，因为 \(fq\) 是 even-fourfold；所以完整 principal
块准确使用 \(a\)。在真实坐标处 \(a=a_0\)，各顶点则必须作 (F.9a)，
不能免费声称平移后的 \(G\) 仍等变。该投影保留仿射性，不增加任何
\(C^k\) 上界，且 \(a_0>0\) 是 \(a>0\) 的充分条件。
下文的 \(R_F=K_F-PM_aP\) 仍然仿射。

令 \(P\) 为某个原 Fourier 有限空间，\(Q=1-P\)。只在整个所用参数域
已证明 \(a>0\) 后，定义
\[
 A(q,s)=P M_{1/a(q,s)}P,\qquad
 C(q,s)=A(q,s)^{-1}+R_F(q,s).
 \tag{F.10}
\]
逆乘子先于压缩；不得把 \(A\) 改成 \((PM_aP)^{-1}\)。
以下 Hilbert 空间就是原 odd-fourfold scalar 空间，\(Q\) 是其中的余空间。
对每个 \(x\in\operatorname{ran}P\)，有准确变分公式
\[
 \langle A^{-1}x,x\rangle
   =\inf_{y\in\operatorname{ran}Q}
      \langle M_a(x+y),x+y\rangle .
 \tag{F.11}
\]
证明：严格正乘子保证该凸二次泛函有唯一极小点，Euler 方程为
\(QM_a(x+y)=0\)。其完整 block 消元给
\(PM_aP-PM_aQ(QM_aQ)^{-1}QM_aP=A^{-1}\)。
因此 (F.11) 是仿射函数族的下确界，给矩阵凹性
\[
 C(\tau\xi+(1-\tau)\zeta)
 \succeq\tau C(\xi)+(1-\tau)C(\zeta),\quad0\le\tau\le1.
 \tag{F.12}
\]
若一个完整凸多边形的每个顶点都已由同一真实矩阵的 directed enclosure
证明 \(C\succeq\kappa I\)，则整个多边形都有该下界。

一个无需新轴目标的首选域是四顶点矩形。读取已完成 axis 结论中的
完整 `nominal_q`、`nominal_s` 与 `complete_axis_error` 保存球，令
\[
\begin{split}
 q_-&=\operatorname{lower}(q_{\rm nom})-\operatorname{upper}(E_{\rm axis}),
 &q_+&=\operatorname{upper}(q_{\rm nom})+\operatorname{upper}(E_{\rm axis}),\\
 s_-&=\operatorname{lower}(s_{\rm nom})-\operatorname{upper}(E_{\rm axis}),
 &s_+&=\operatorname{upper}(s_{\rm nom})+\operatorname{upper}(E_{\rm axis}).
\end{split}
\tag{F.13}
\]
所有端点向外取有理数。原完整欧氏误差球的每个分量误差均不超过
\(\operatorname{upper}(E_{\rm axis})\)，所以真实坐标必在
\([q_-,q_+]\times[s_-,s_+]\)。四个顶点全部保留；不截去未核点，
也不以原 JSON 中较粗的 `true_root_support_coordinates` 显示球代替
这三个完整保存球。若改用更细多边形，其每个面仍须证明包含原完整球；
负 \(q_+\) 只能是包含之后的结论，不能成为删减包络的条件。

最后，有限正性仍须与同一真实全圈的 compact 一侧尾误差结合，产生
(F.5) 的完整 \(\lambda>0\)。四顶点检查自身不删除任何无限 high mode，
也不替代完整 tail gate 或 (F.8) 的 \(\mathsf H\) 费用。
