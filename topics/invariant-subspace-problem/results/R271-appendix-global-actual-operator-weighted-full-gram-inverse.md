# R271 附录：原全算子的完整 Gram inverse、闭孔权域及同源物理比较

日期：2026-11-26（UTC）。

作者：Astra-ISP-347c-20261126 / r271_source；AI-assisted，GPT-6 Astra Pro。

**状态：以下原 $T_N/T_Y$ 的完整未加权 inverse 孔权界及同源比较已证明。**
该结论直接作用于原无限物理算子 $T$，保全部 carry。
方差仍为 $s\ge2^{24}/(m+2^m)$；没有把完整空间换成最高真核 $F_0$，
也没有把 Gram 正则化列称为真核列。

使用：

- [原 c26 联合 carry 预算](../notes/2026-11-14-joint-positive-carry-budget-and-twenty-six-window-actual-sources-789f-next.md)，特别 (0.1)–(0.3)；
- [真实强头的完整 Gram](R271-appendix-actual-strong-head-gram-comparison-and-true-far-variance-source-limit.md)，§§1–2；
- [真空源矩、全新增位物理运输与完整加权 inverse](R271-appendix-vacuum-source-moments-all-strong-physical-transport-and-weighted-inverse.md)，§§4–6。

## 1. 原全局 carry 在两向闭孔权中的费用

取原 $T=T_N$ 或 $T_Y$，$m\ge10$、$d=2^m$，置
$$
L_m=A_m+D_{\ge m},\qquad y=m+d,\qquad
\Gamma_y=32^{N_{\ge y}},\qquad
\mathcal R_m=e^{(417/8)d^3}.
$$
$\Gamma_y$ 是正自伴闭算子，其逆处处有界；使用真实物理孔数。
原完整相邻 carry 满足
$$
T-L_m=\sum_{p=m}^{\infty}K_p,
$$
每个 $K_p$ 只作用前 $p+1$ 位。
在 c26 的 (0.2) 中取 $j=k=0$、$R=\mathcal R_m\le\mathcal R_p$，得到
$$
\mathcal R_m\|K_p\|\le e^{-2\cdot16^p},\qquad p\ge m.
\tag{1.1}
$$
有限支持同时给
$$
\|\Gamma_yK_p\Gamma_y^{-1}\|,
\quad\|\Gamma_y^{-1}K_p\Gamma_y\|
\le32^{\max(0,p-y+1)}\|K_p\|
\le32^{p+1}\|K_p\|.
\tag{1.2}
$$
两个共轭最初在有限位置/有限孔核心上定义，右端给有界延拓。

相邻求和项的比至多
$32e^{-30\cdot16^p}<1/2$，故 (1.1)–(1.2) 的完整无穷和满足
$$
\begin{aligned}
\varepsilon_m
&:=\max\left\{
\|\Gamma_y(T-L_m)\Gamma_y^{-1}\|,
\|\Gamma_y^{-1}(T-L_m)\Gamma_y\|
\right\}\\
&\le2\,32^{m+1}\mathcal R_m^{-1}e^{-2d^4}
\le e^{-7d^4/4}.
\end{aligned}
\tag{1.3}
$$
最后一步对 $d\ge1024$ 有充分余量，
例如 $\log2+(m+1)\log32\le d^4/4$，并可直接丢掉负的 $-\log\mathcal R_m$。
这没有只保一个有限头的 carry 压缩。

加权级数与原算子范数级数都绝对收敛，在共同核心上相同。
由 $\Gamma_y$ 闭性，(1.3) 的正向共轭保证 $T-L_m$ 保持
$\operatorname{Dom}\Gamma_y$；逆向共轭取伴随又保证 $(T-L_m)^*$ 保持该域。
此后所有乘积都先在此闭域上作，再使用明确的有界延拓。

## 2. 两向有界头和全部级数 Gram

把原 $L_m$ 准确写成
$$
L_m=C_y+D_{\ge y},\qquad C_y=A_m+D_{[m,y)},\qquad C_y^{2d}=0.
$$
$C_y$ 作用前 $y$ 位，所以与 $\Gamma_y$ 交换。
原 $\|C_y\|\le7$、$\|D_{\ge y}\|\le1/y$，且
$$
\Gamma_yD_{\ge y}\Gamma_y^{-1}=D_{\ge y}/32,
\qquad
\Gamma_y^{-1}D_{\ge y}\Gamma_y=32D_{\ge y}.
$$
因此两向 $L_m$ 共轭范数至多 $8$，再由 (1.3)，两向 $T$ 共轭范数至多 $9$。
其伴随的正向共轭恰为相应算子逆向共轭的伴随，亦至多 $9$。

对 $X=T,L_m$ 和任意 $J\in\{0,1,2,\ldots,\infty\}$，定义原完整 Gram
$$
H_{X,J}(s)=\sum_{j=0}^{J}\frac{(X^*)^jX^j}{j!s^j},\qquad s>0.
\tag{2.1}
$$
当 $J=\infty$，这是算子范数收敛的完整级数，因为 $X$ 有界。
每个 $H_{X,J}(s)\succeq I$，所以原未加权 inverse 处处有界且范数至多 $1$。

正向加权 Gram 的准确表达式为
$$
\Gamma_yH_{X,J}(s)\Gamma_y^{-1}
=\sum_{j=0}^{J}\frac{
\bigl[(\Gamma_y^{-1}X\Gamma_y)^*\bigr]^j
\bigl[\Gamma_yX\Gamma_y^{-1}\bigr]^j}{j!s^j}.
\tag{2.2}
$$
这不是正定的另一个加权 Gram；它是原 Gram 的真实共轭。
右端在 $J=\infty$ 时也于算子范数收敛，范数至多 $e^{81/s}$。
有限级数在原闭域上的恒等式和闭性说明它确实实现左端。

两向因子的幂差望远镜给第 $j\ge1$ 项的范数差至多
$2j\varepsilon_m9^{2j-1}$。完整求和，得到所有 $J$ 同时成立的界
$$
\boxed{
\|\Gamma_y[H_{T,J}(s)-H_{L_m,J}(s)]\Gamma_y^{-1}\|
\le\frac{18\varepsilon_m}{s}e^{81/s}.}
\tag{2.3}
$$
没有把每层误差分别截成不同的输入，也没有在 $J=\infty$ 时使用有限 creation 的范数。

## 3. 大辅助方差下原全 $T$ inverse 的统一孔权界

现在取
$$
s\ge K/y,\qquad K\ge2^{24}.
\tag{3.1}
$$
由 $y\le2d$，
$$
\log(18/s)+81/s
\le\log(36d)+162d\le d^4/4\qquad(d\ge1024).
$$
因此 (1.3)、(2.3) 给
$$
\delta_m:=\|\Gamma_y[H_{T,J}(s)-H_{L_m,J}(s)]\Gamma_y^{-1}\|
\le e^{-3d^4/2}.
\tag{3.2}
$$
引用全新增位原 inverse 定理，而不是改变最小化度量，已得
$$
\|\Gamma_yH_{L_m,J}(s)^{-1}\Gamma_y^{-1}\|\le31/30
\quad\text{对全部 }J\le\infty.
\tag{3.3}
$$
在图范数空间 $\operatorname{Dom}\Gamma_y$ 上，置
$E_J=H_{T,J}(s)-H_{L_m,J}(s)$。
由 (3.2)–(3.3)，
$H_{L_m,J}^{-1}E_J$ 的加权范数至多 $(31/30)\delta_m<1$。
Neumann 级数给加权空间中的 inverse；因原 $H_{T,J}\succeq I$ 的 Hilbert 解唯一，
该 inverse 就是原 $H_{T,J}^{-1}$ 在该域上的限制。
故
$$
\boxed{
H_{T,J}(s)^{-1}\operatorname{Dom}\Gamma_y
\subseteq\operatorname{Dom}\Gamma_y,
\qquad
\|\Gamma_yH_{T,J}(s)^{-1}v\|
\le\frac{16}{15}\|\Gamma_yv\|.}
\tag{3.4}
$$
准确的 inverse 差同时满足
$$
\begin{aligned}
\|\Gamma_y[H_{T,J}^{-1}-H_{L_m,J}^{-1}]\Gamma_y^{-1}\|
&\le\frac{(31/30)^2\delta_m}{1-(31/30)\delta_m}\\
&\le2e^{-3d^4/2}\le e^{-d^4}.
\end{aligned}
\tag{3.5}
$$
式 (3.4) 也可由 $31/30+e^{-d^4}\le16/15$ 直接读出。
所有式子都包括 $J=0$ 和完整无穷级数；不存在随截断高度增长的常数。

## 4. 原实际 forcing 与旧同源物理列

令 $g$ 支撑前 $y$ 位，以原以后真空嵌入记为 $i_0g$。
设 $f_{y,s,J}^{\rm phys}$ 为原旧头 $C_y$ 的完整最小者产生的物理阻尼列，
$\mu_1$ 是该同一旧最小者的第一高度能量。
全新增位运输定理与 (3.5) 给
$$
\boxed{
\|\Gamma_y[H_{T,J}(s)^{-1}i_0g-f_{y,s,J}^{\rm phys}]\|
\le e^{-d^4}\|g\|
+\frac{96}{\sqrt{3K}\,y}\sqrt{\mu_1}.}
\tag{4.1}
$$
对 $J\ge2d-1$，旧列和 $\mu_1$ 已稳定，故可直接令 $J\to\infty$；
左端成为原全算子的完整级数正则化源。

若先照全新增位运输定理在 $[K/y,2K/y]$ 内选择一次 $s_*$，
则对所有后续合法原 $Q$ 可使用
$$
\sqrt{\mu_1(s_*)}\le\Delta_{g,Q}/\sqrt{\log2}.
$$
原旧物理列保持 $V_Q/K_Q$ 及同一个 $u_{g,Q}$，前提仍为
$Q\ge(y-m)+J$（完整旧列时可用稳定后的 $J=2d-1$）。
因此 (4.1) 以原物理范数量化它与实际 $T$ 正则化源的差；
不能把该小差改成投影完全相等。

另对任意 $w\in M=\ker T$，有 $H_{T,J}(s)w=w$，从而准确
$$
\langle w,H_{T,J}(s)^{-1}i_0g\rangle
=\langle w,i_0g\rangle .
\tag{4.2}
$$
这是同一个原 $w$ 的配对，不依赖近似 forcing 或另选 kernel-input。

## 5. 未由正则化删除的真核返回

对固定 $T$，完整级数 $H_{T,\infty}(s)^{-1}$ 随 $s\downarrow0$ 强趋 $P_M$。
确实它在 $M$ 上恒等，且
$$
0\preceq H_{T,\infty}(s)^{-1}-P_M
\preceq(I+T^*T/s)^{-1}-P_M,
$$
右端由谱定理强趋零。
这个事实本身不提供移动参数的收敛速率，也不提供 $P_M$ 的相同孔权界。
因为 (3.1) 要求 $y\ge K/s$，这里的孔权起点随 $s\downarrow0$ 移动。

特别，$H_{T,J}(s)^{-1}i_0g$ 通常不在 $M$，
尽管它在闭指数孔权域中且满足准确配对 (4.2)。
仍须支付原真物理核/完整 MP 返回，或控制真实 $F_0$ 约束 Schur 的混级费用。
(3.4) 的完整空间 inverse 界不蕴含未知 $P_{F_0}$ 与 $\Gamma_y$ 交换，
也不证明原 $\mathcal Z_{1/32}(S_x)$ 或 $N=M$。
