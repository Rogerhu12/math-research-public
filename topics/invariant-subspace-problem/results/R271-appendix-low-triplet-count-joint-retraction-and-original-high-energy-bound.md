# R271 附录：低三维块数的全模式联合回缩与原高返回能量界

日期：2026-11-14（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿在同一个原配对前缀内，联合保留任意位置的至多 $R$ 个三维非原始块，并同时保留一整组真实远尾 primitive 出生。完整分析、合成及交叉 Gram 的费用不含模式数。将该回缩接到原三个真正最小费用，得到这一闭源空间上的 $\lambda\le C\alpha$ 及新 $H_2^\circ$ 高能量界；一组原合法参数给 $C<2$。

这不是全部前缀模式的估计，也没有联合不同配对划分。高层核消失只发生在明确指定的模型源次数区间。原实际固定缺陷来源仍须通过真正的两费用投影处理，不能由模型坐标置零。纯 $S_H^\dagger$ 逆费用、一般实际高返回、无权 $N=M$ 和普通 Hilbert ISP 仍为 OPEN。

依赖：[完整首个三维块几何](R239-appendix-complete-first-triplet-resolution-and-minimal-energy.md)、[完整短 canonical Fock 塔](R271-appendix-short-canonical-fock-flags-and-q-over-d-prefix-window.md)、[原强位回缩及三费用运输](R271-appendix-original-tail-strong-bit-boson-retraction-and-same-source-high-schur-bound.md)、[整段出生联合](R271-appendix-joint-primitive-birth-window-retraction-without-count-loss.md)、[实际两费用删除](R271-appendix-shifted-primitive-retractions-and-paid-actual-source-removal.md)。

## 1. 原相邻块及外部正交模式空间

固定原 $m\ge5,d=2^m$，保留真正的 $A_m$、原权
$a_j=(j+1)^{-2}$ 和原 Hilbert 范数。取前 $N\ge1$ 个相邻对
$$
I_i=\{m+2(i-1),m+2(i-1)+1\},\qquad 1\le i\le N.
$$
在第 $i$ 对写 $a=a_{m+2(i-1)},b=a_{m+2(i-1)+1}$，
$\sigma_i=\sqrt{a^2+b^2}$，并定义原单位向量
$$
h_i=\frac{b|10\rangle-a|01\rangle}{\sigma_i},\quad
g_i=\frac{a|10\rangle-b|01\rangle}{\sigma_i},\quad
t_i=\frac{b|10\rangle+a|01\rangle}{\sigma_i}.
$$
置
$$
\rho_i=\frac{2ab}{a^2+b^2},\qquad
\delta_i=\frac{a^2-b^2}{a^2+b^2}.
$$
准确有
$$
\rho_i^2+\delta_i^2=1,\quad
h_i=\rho_i g_i-\delta_i t_i,\quad
\langle h_i,t_i\rangle=-\delta_i.
\tag{1.1}
$$
斜投影 $P_i=|h_i\rangle\langle g_i|/\rho_i$ 和
$Q_i=I-P_i$ 都与该块删除交换。其像为
$$
\operatorname{Ran}P_i=\mathbb Ch_i,\qquad
\operatorname{Ran}Q_i=\operatorname{span}\{\Omega_i,t_i,|11\rangle_i\}.
\tag{1.2}
$$
后一个三维空间的所示基是原范数的正交归一基。其删除链严格为
$$
\mathsf D_i f_0=0,\quad
\mathsf D_i f_1=\rho_i\sigma_i f_0,\quad
\mathsf D_i f_2=\sigma_i f_1.
\tag{1.3}
$$
不将两个非零系数换成同一个数。

令局部外部空间
$$
\mathfrak B_i=\mathbb Cp_i\oplus^\perp
\operatorname{span}^{\perp}\{f_{i,0},f_{i,1},f_{i,2}\}.
$$
给 $p_i$ 孔数 $1$，给 $f_{i,j}$ 孔数 $j$。
局部合成 $U_i$ 把 $p_i$ 送到 $h_i$，把 $f_{i,j}$ 送到
$\Omega_i,t_i,|11\rangle_i$。这是四维有界同构，保孔数，并准确交织
$0\oplus\mathsf D_i$ 与原块删除。

在
$\mathfrak B_N=\bigotimes_{i=1}^N\mathfrak B_i$
中，用 $\mathfrak n$ 数处于三维 $Q$ 分量的块数。
所有模式在这个外部空间中正交。记
$$
\mathfrak B_{\le R}=1_{\{\mathfrak n\le R\}}\mathfrak B_N,\qquad
\Pi_R=1_{\{\mathfrak n\le R\}},\qquad 0\le R\le N.
$$
该空间保留每一种至多 $R$ 个 $Q$ 块的选择，且每个 $Q$ 块的全部三个原物理状态均保留；没有只挑其中一条向量。

## 2. 全部低块数模式的真实联合范数

记
$$
U_N=\bigotimes_{i=1}^N U_i,\qquad
\mathcal R_N=\prod_{i=1}^N\rho_i^{-1},\qquad
\mathcal S_N=\sum_{i=1}^N\delta_i^2.
$$
定义局部秩一算子
$$
e_i=|p_i\rangle\langle f_{i,1}|,\qquad K=\sum_{i=1}^N\delta_i e_i.
$$
它们在不同块上交换，且 $e_i^2=0$。$K$ 降低 $Q$ 块数。
对 $x\in\mathfrak B_{\le R}$，向量值 Cauchy--Schwarz 给
$$
\|Kx\|^2\le\mathcal S_N\sum_i\|e_ix\|^2
\le R\mathcal S_N\|x\|^2,
\tag{2.1}
$$
因为 $\sum_i e_i^*e_i\le\mathfrak n$。故在这个不变子空间上
$$
\|e^{\pm K}|_{\mathfrak B_{\le R}}\|\le e^{\sqrt{R\mathcal S_N}}.
\tag{2.2}
$$

下面分别核对分析和合成，不能从其中一个倒推另一个。

在原物理一孔正交基
$$
h_i,\qquad z_i=(t_i+\delta_i h_i)/\rho_i
$$
中，$U_i$ 的一孔矩阵是
$$
\begin{pmatrix}1&-\delta_i\\0&\rho_i\end{pmatrix}
=
\begin{pmatrix}1&0\\0&\rho_i\end{pmatrix}
e^{-\delta_i e_i}.
$$
在真空和二孔方向它为恒等。因此某个按块定义的酉识别之后，
$$
U_N=C_Ne^{-K},\qquad \|C_N\|\le1.
$$
由 (2.2)，
$$
\boxed{\|U_N|_{\mathfrak B_{\le R}}\|
\le b_R:=e^{\sqrt{R\mathcal S_N}}.}
\tag{2.3}
$$

另一方面，在原正交基 $g_i,t_i$ 中，
$$
U_i^{-1}=
\begin{pmatrix}\rho_i^{-1}&0\\
\delta_i\rho_i^{-1}&1\end{pmatrix}
=e^{\delta_i e_i^*}
\begin{pmatrix}\rho_i^{-1}&0\\0&1\end{pmatrix}.
$$
所以 $U_N^{-1}=e^{K^*}Z_N$，其中
$\|Z_N\|\le\mathcal R_N$。注意这个公式对整个物理输入成立。
利用
$$
\|\Pi_Re^{K^*}\|=\|e^K\Pi_R\|
\le e^{\sqrt{R\mathcal S_N}},
$$
得到完整分析界
$$
\boxed{\|\Pi_RU_N^{-1}\|
\le a_R:=\mathcal R_Ne^{\sqrt{R\mathcal S_N}}.}
\tag{2.4}
$$
特别
$$
(\Pi_RU_N^{-1})(U_N|_{\mathfrak B_{\le R}})=I,\qquad
a_Rb_R=\mathcal R_Ne^{2\sqrt{R\mathcal S_N}}.
\tag{2.5}
$$
这已支付所有模式之间的交叉项；没有对每个模式单独估计后求和。
完整首个三维块稿的原权估计还给，对所有 $N$ 一致，
$$
\boxed{\mathcal R_N\le e^{2/(m+1)},\qquad
\mathcal S_N\le\frac3{m+1}.}
\tag{2.6}
$$
因此允许 $R=O(m)$ 时，联合常数仍有统一上界，尽管所保留模式数可以很大。

## 3. 与同一个原远尾的整组出生接合

令
$$
q=N+s,\qquad J=m+2N,\qquad
D_J=\sum_{j\ge J}(j+1)^{-2}E_j,\qquad
S_J=\sum_{j\ge J}(j+1)^{-4}.
$$
取整数 $T\ge0$。对于每个具有恰好 $r\le R$ 个 $Q$ 块的模式，
保留全部满足
$$
\boxed{b\ge0,\qquad
\max(0,2r-1)\le t:=s+r-b\le T}
\tag{3.1}
$$
的远尾 primitive 出生 $b$，并保留整个真实
$K_b(D_J)=\ker D_J\cap\mathcal H_b^{(J)}$。
每个模式中 $N-r$ 个暗块恰占 $N-r$ 孔，所以其模型源的活动次数确实为
$q-(N-r)-b=t$。

在相应外部模式上，尾模型为
$$
\mathsf D=\sum_{i\in Q}\mathsf D_i+\sqrt{S_J}\,\mathsf b
$$
与整个 $K_b(D_J)$ 的恒等张量，其中 $\mathsf b$ 是标准标量玻色删除。
各 $\mathsf D_i$ 保留 (1.3) 的原权。不同模式、不同出生作为外部正交直和处理。

置
$$
H=T+d+1,\qquad P=s+R+d,\qquad
\theta=\frac{12HP}{J+1}<\frac12,\qquad
\kappa=\sqrt{\frac{1-\theta}{1-2\theta}}.
\tag{3.2}
$$
凡在原左层 $p\le q$ 或右链层 $q+j,\ 1\le j\le d$ 中出现的远尾列，
其远尾物理孔数至多 $P$，创建高度至多 $T+d=H-1$。
前者因为
$$
p-(N-r)-(\text{三维块孔数})\le s+r+d\le P,
$$
后者因为每个所选出生的活动次数是 $t\le T$。

使用完整短 canonical 塔的同一分析/合成：
$$
W_\ell^*x=
\left(\frac{P_{K_b}D_J^{\ell-b}x}
{\sqrt{(\ell-b)!S_J^{\ell-b}}}\right)_b,\qquad
V_{\ell,H}|_{K_b}
=\sqrt{(\ell-b)!S_J^{\ell-b}}\,
D_{\ell}^\dagger\cdots D_{b+1}^\dagger|_{K_b}.
$$
完整分析为压缩后的玻色等距列之伴随，故 $\|W_\ell^*\|\le1$；
短列的联合范数满足 $\|V_{\ell,H}\|\le\kappa$，且
$W_\ell^*V_{\ell,H}=I$。
这些是混合出生的全算子界。不同 $Q$ 模式使用相同的原 $D_J$，
因此可以在外部直和中一次应用，而无出生数或模式数损失。

把 (2.3) 的前缀合成与这些远尾短列相接，记为 $\mathcal B_p$。
分析 $\mathcal T_p$ 先用 $\Pi_RU_N^{-1}$，再用完整 $W^*$，
最后正交选取 (3.1) 的模式和出生。于是
$$
\boxed{
\mathcal T_p\mathcal B_p=I,\qquad
\|\mathcal T_p\|\le a_R,\qquad
\|\mathcal B_p\|\le b_R\kappa.}
\tag{3.3}
$$
所有 $p$ 的正交直和保留同样界。

这两个映射保原孔数，且准确交织原 $D_m$ 与 $\mathsf D$。
原因是局部 $P/Q$ 模式和远尾出生在各自模型删除下均不改变；
最后选择 (3.1) 只选择固定模式及出生，而不是随层变化地截断一条链。
它们与真实 $A_m$ 交换。因此全部联合核旗、原左右方程、首末端方程均保持。
并未声称它们与各核的正交投影交换。

## 4. 为什么所选模型的高出生域确实为零

固定一个具有 $r$ 个三维块的模式。其有限尾部分的孔数在
$0,\ldots,2r$ 之间。记源活动次数为 $t$。

对任意 $j\ge2$，考虑
$$
\mathsf D^{\,j-1}:
\mathfrak H_{t+j}\longrightarrow\mathfrak H_{t+1}.
\tag{4.1}
$$
由 (3.1)，当 $r\ge1$ 时 $t+1\ge2r$；当 $r=0$ 时只有标量玻色因子。
所以 (4.1) 的两端均包含有限部分的全部基向量，并有相同的有限维数。
按有限部分孔数排序，矩阵是三角矩阵。有限部分次数为 $a\le2r$ 的对角元为
$$
S_J^{(j-1)/2}
\sqrt{\frac{(t+j-a)!}{(t+1-a)!}}>0.
\tag{4.2}
$$
其余项来自至少一次三维块删除，因而严格降低有限部分次数。
故 (4.1) 可逆。张量任意 $K_b(D_J)$ 后仍可逆；固定窗口内共有有限种模式和出生，故直和也有有界逆。

因此
$$
\boxed{\ker\mathsf D^{\,j-1}|_{\mathfrak H_{t+j}}=0
\quad(j\ge2),\qquad
\widehat{\mathscr X}_H=0.}
\tag{4.3}
$$
这正是原高出生域的模型对应，不只是单步删除的满射性。
于是对所有可实现的模型同源
$$
\boxed{\widehat\lambda=\widehat\alpha.}
\tag{4.4}
$$
若删掉 (3.1) 的下界，(4.3) 一般不成立；本稿不扩展该次数范围。

## 5. 原同源完整费、裸费及新高能量

在原固定窗口源空间 $\mathscr R_q$ 中，定义闭源空间
$$
\mathscr E_q=\mathscr R_q\cap\operatorname{Ran}\mathcal B_q.
\tag{5.1}
$$
$\operatorname{Ran}\mathcal B_q$ 由 (3.3) 闭合；$\mathscr R_q$ 是原真实闭源空间。
若 $r=\mathcal B_q\widehat r\in\mathscr E_q$，对任一原左右可行链施加
$\mathcal T$，即得 $\widehat r$ 的模型可行链，故模型源也可实现。

原强位回缩稿的完整可行集证明逐字适用：左费和完整右费直接取可行链最小值；
裸费使用
$$
\alpha(r)=\inf_{c\in\mathcal A(r)}
\operatorname{dist}(c,\mathscr X_H),
$$
再用 $\mathcal T\mathscr X_H\subseteq\widehat{\mathscr X}_H$ 与
$\mathcal B\widehat{\mathscr X}_H\subseteq\mathscr X_H$。
所以对 $e=\lambda,\alpha,\mu$ 分别有
$$
a_R^{-1}\widehat e(\widehat r)
\le e(r)\le b_R\kappa\,\widehat e(\widehat r).
\tag{5.2}
$$
这里始终是同一 $\widehat r$ 和同一原 $r$，不交换不同最小问题的最优源。

结合 (4.4)，得到
$$
\boxed{
\lambda(r)\le C\,\alpha(r)\quad(r\in\mathscr E_q),\qquad
C=\mathcal R_N\kappa e^{2\sqrt{R\mathcal S_N}}.}
\tag{5.3}
$$
还有一个对任意原源有用的准确投影形式。令
$\mathcal P_q=\mathcal B_q\mathcal T_q$。
分析与合成保持原可实现性，故 $\mathcal P_q$ 是到 $\mathscr E_q$ 的有界幂等，
并且
$$
\boxed{\lambda(\mathcal P_qr)\le C\alpha(r)
\qquad(r\in\mathscr R_q).}
\tag{5.4}
$$
它是代数回缩，不能据此声称原 flat 费用收缩或负图保持。

原新高 Schur 能量的准确身份给，对 (5.1) 的同一个源，
$$
\begin{aligned}
E_H(r)
&=\lambda(r)^2-\alpha(r)^2\\
&=\left\langle(H_2^\circ)^{-1}
\mathcal R\mathcal G^\dagger\zeta(r),
\mathcal R\mathcal G^\dagger\zeta(r)\right\rangle .
\end{aligned}
$$
故
$$
\boxed{0\le E_H(r)\le(C^2-1)\alpha(r)^2.}
\tag{5.5}
$$
这里只用了新 $H_2^\circ$ 身份；它并不推出纯
$\|S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)\|$ 的相同界。

## 6. 一个允许线性多个非原始块的原合法参数族

取
$$
\boxed{
m\ge47,\quad d=2^m,\quad
R=\left\lfloor\frac{m+1}{48}\right\rfloor,\quad T=d,\quad
4096d^2\le q\le e^{d^3/4},}
$$
$$
\boxed{R-1\le s\le\left\lfloor\frac q{1024d}\right\rfloor,\qquad
N=q-s.}
\tag{6.1}
$$
这些区间非空，$R\le d\le N$，且 $T\ge2R-1$，所以每个
$0\le r\le R$ 都有合法出生。
此时 $H\le3d,\ P\le s+2d,\ J+1\ge q$，于是
$$
\theta\le\frac{36d(s+2d)}q
\le\frac{36}{1024}+\frac{72}{4096}
=\frac{27}{512}<\frac18.
\tag{6.2}
$$
故 $\kappa\le\sqrt{7/6}$。由 (2.6)，
$$
\log C\le\frac2{m+1}
+2\sqrt{\frac{3R}{m+1}}+\frac12\log(7/6)
\le\frac1{24}+\frac12+\frac1{12}
=\frac58<\log2.
$$
因此
$$
\boxed{C<2,\qquad E_H(r)<3\alpha(r)^2
\quad(r\in\mathscr E_q).}
\tag{6.3}
$$

所选出生对每个 $r\ge1$ 恰为
$$
\max(0,s+r-d)\le b\le s-r+1,
$$
对 $r=0$ 为 $\max(0,s-d)\le b\le s$。
整个 $K_b(D_J)$ 均保留。新增的联合覆盖包括所有任意位置的
至多 $R\asymp m$ 个三维块，不含 $\binom Nr$ 的范数损失。

## 7. 在真正两费用度量中删除，以及保整条实际源流

仍用原算子
$$
L=J_{\rm left}^{-1},\quad B=J_{\rm bare}^{-1},\quad
G=J_{\rm right},\quad
\mathfrak M=B+LGL,
$$
$$
\Xi(r)^2=\alpha(r)^2+\lambda_{\rm flat}(r)^2
=\langle\mathfrak Mr,r\rangle.
$$
(5.3) 与原正逆 Cauchy 给
$$
\mu(p)^2\le\lambda(p)\lambda_{\rm flat}(p)
\le \frac C2\Xi(p)^2\qquad(p\in\mathscr E_q).
\tag{7.1}
$$
若给定原来源已经位于某个真实闭约束 $\mathscr D_q$，令
$$
Z=\mathscr E_q\cap\mathscr D_q,\qquad
p=P_Z^{\mathfrak M}r,\qquad r_{\rm rem}=r-p.
$$
则两者保持 $\mathscr D_q$，且
$$
\Xi(r)^2=\Xi(p)^2+\Xi(r_{\rm rem})^2,\quad
\mu(p)\le\sqrt{C/2}\,\Xi(r),\quad
\lambda(p)\le C\Xi(r).
\tag{7.2}
$$
准确余条件是 $\iota_Z^*\mathfrak Mr_{\rm rem}=0$。
这支付残源的原裸/flat 总费用；不声称两个分量各自收缩，
也不将它改成所选模式的坐标为零。

如需同一个顶部的整条相容源流，则直接将
$\mathscr E_b\cap\mathscr N_b$ 代入
[不交未来窗顶部投影稿](R271-appendix-disjoint-window-top-projection-and-coherent-source-flow-removal.md)
的真实总度量 $\mathfrak H_b$。
(6.3)、(7.1) 给该稿所需的统一 $c_b<1,\ell_b<2$，
所以全部相邻源、primitive 增量和单步完整尾 MP 反馈仍由同一顶部修改支付。
这里必须保留该稿的总 $\mathfrak H_b$ 正交条件，不能改成逐窗各自正交。

每个模型分量的出生物理层为 $N-r+b=q-t\ge q-T$。
因此其模型左最小者经 $\mathcal B$ 送回后的原候选支撑于 $[q-T,q]$。
[实际缺陷角度稿](R271-appendix-actual-defect-angle-and-window-distortion-barrier-for-retraction-sources.md)
的准确零源 lift 配对因而也适用于本稿，失真取同一个 $C$。
特别，(6.1) 的有界失真源空间本身不能产生逼近固定非零 $w\in W$ 的左最小者族。
这与 (7.2) 相容：删除的是可付的小部分，实际来源保留在准确的余空间中。

本稿仍未控制超过 $R$ 个三维块的模式、不同配对划分的联合，
或余空间中的真实高返回。没有从这次联合覆盖推出无权 $N=M$。
