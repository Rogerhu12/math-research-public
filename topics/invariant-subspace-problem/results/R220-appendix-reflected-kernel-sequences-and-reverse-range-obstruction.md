# R220 附录：有限头反射的真实奇异序列与反向值域障碍

日期：2026-11-13（Asia/Taipei）。作者：boundary。状态：已证明。

本稿补齐 R220 的反向比较。原 R220 已证明实际慢符号不能有界地右除以纯消灭和，并且实际像不包含在纯像中。本稿构造实际 $g\in N=\overline{B\ker T}$，使纯算子 $Dg\ne0$；有限头反射再给相反的像不包含及模紧算子的定量距离。此结论排除用全局 $\|D^*u\|\le C\|T^*u\|$ 来统一形式伴随原像的多孔估计，并未排除 $W=M\ominus N$。

## 1. 记号

在实际负整数边界 $H_-=\ell^2(\mathbb N_0)$ 上，记
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1},\qquad
N_j=B^{2^j}/d_j,\qquad Y_j=N_j(I+N_j)^{-1}.
$$
取 $a_j=(j+1)^{-2}$，并令
$$
D=\sum_{j\ge0}a_jE_j,\qquad
T=T_N=\sum_ja_jN_j
\quad\text{或}\quad T=T_Y=\sum_ja_jY_j.
\tag{1.1}
$$
$E_j$ 是纯孔消灭。两种实际模型都沿用
$$
\eta_j=\alpha_{j+1}/\alpha_j\le e^{-770\,16^j},\quad
N_j=E_j+\eta_jE_j^*N_{j+1},\quad
\|T\|\le6,\quad\|D\|<2.
$$
置
$$
M=\ker T,\quad N=\overline{BM},\quad
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\},
$$
并记 $P_m$ 为对应正交投影。

## 2. UHF 的全位翻转与有限头反射

记边界 UHF 代数为 $\mathfrak U$。对每个有限位矩阵代数，同时交换所有相关位的真空与占据态，定义相容的等距 $*$ 自同构 $\rho$。它唯一延拓到 $\mathfrak U$，且
$$
\rho(E_j)=E_j^*,\qquad\rho(E_j^*)=E_j.
$$
令
$$
\sigma(E)=\rho(E^*)\quad(E\in\mathfrak U).
\tag{2.1}
$$
这是保范数的共轭线性反同构；本稿只用它对固定算子的作用，不声称其在边界 Hilbert 空间由一个全局有界反射实现。

真实递推在范数中给
$$
N_j=\sum_{r\ge j}\frac{\alpha_r}{\alpha_j}
E_j^*\cdots E_{r-1}^*E_r.
\tag{2.2}
$$
截断后的余项范数至多 $\alpha_{R+1}/\alpha_j\to0$。取伴随后全位翻转，不同位因子交换，故
$$
\sigma(N_j)=N_j,\qquad\sigma(Y_j)=Y_j.
$$
由于 (1.1) 的系数为实数，
$$
\boxed{\sigma(T)=T,\qquad\sigma(D)=D.}
\tag{2.3}
$$

令 $J_m$ 在 $\mathcal F_m$ 上按
$$
J_me_n=e_{2^m-1-n}
$$
作用，在 $\mathcal F_m^\perp$ 上取零。于是 $J_m$ 为范数 1 的自伴部分等距，$J_m^2=P_m$。

**引理 2.1。** 对任意固定 $E\in\mathfrak U$ 和 $g\in H_-$，
$$
\boxed{\|E^*J_mP_mg-J_mP_m\sigma(E)g\|\longrightarrow0.}
\tag{2.4}
$$

证明：若 $E$ 只作用前 $r$ 位，则当 $m\ge r$ 时，$P_m$ 与 $E,\sigma(E)$ 交换，并且有限张量反射精确给
$$
E^*J_mP_m=J_mP_m\sigma(E).
$$
对一般 $E$，取有限位 $E_0$ 使 $\|E-E_0\|<\varepsilon$；两边误差合计不超过 $2\varepsilon\|g\|$，因为 $\sigma$ 等距。先令 $m\to\infty$，再令 $\varepsilon\to0$。证毕。

对任意固定 $g$，向量 $x_m=J_mP_mg$ 还满足
$$
x_m\rightharpoonup0,\qquad\|x_m\|\longrightarrow\|g\|.
\tag{2.5}
$$
确实，对每个固定坐标 $n$，最终 $(x_m)_n=g_{2^m-1-n}\to0$；范数一致有界，有限坐标向量稠密，故弱收敛成立。

## 3. 任意 UHF 符号的右理想本质范数下界

**定理 3.1。** 对任意 $E,S\in\mathfrak U$、任意有界 $U\in B(H_-)$，
$$
\boxed{\|E-SU\|_{\mathrm{ess}}
\ge\|\sigma(E)|_{\ker\sigma(S)}\|.}
\tag{3.1}
$$
空核时右侧按零解释。这里 $U$ 不必属于 UHF，也不必与 $S$ 交换。

证明：取任意非零 $g\in\ker\sigma(S)$，令 $x_m=J_mP_mg$。由 (2.4)，
$$
S^*x_m\longrightarrow0,\qquad
\|E^*x_m\|\longrightarrow\|\sigma(E)g\|.
$$
任意紧 $K$ 满足 $K^*x_m\to0$。因此
$$
\liminf_m\|(E-SU-K)^*x_m\|
\ge\|\sigma(E)g\|.
$$
除以 $\|x_m\|\to\|g\|$，再对 $K$ 取下确界、对单位 $g$ 取上确界，即得 (3.1)。

对于 (1.1) 的真实慢和与纯和，(2.3) 给
$$
\boxed{\|D-TU\|_{\mathrm{ess}}\ge\|D|_M\|.}
\tag{3.2}
$$
对换两者也有
$$
\|T-DU\|_{\mathrm{ess}}\ge\|T|_{\ker D}\|,
\tag{3.3}
$$
与 R220 的明确下界一致，并给出了其反射解释。

## 4. 实际构造一个 $g\in N$，使 $Dg\ne0$

这一节不能由纯模型猜测代替，因为 (3.2) 要有真正正的右端。

固定低头 $m=2$ 和 $v=e_2\in\mathcal F_2$。对两种实际模型，
$$
(Tv)_1=\eta_0>0,\qquad (Dv)_1=0,\qquad T_2^3v=0.
\tag{4.1}
$$
逐项核对如下：$N_0e_2=\eta_0e_1$、$N_1e_2=e_0$，其余 $N_j$ 杀掉输入；而
$$
Y_0e_2=\eta_0e_1-\eta_0e_0,\qquad Y_1e_2=e_0.
$$
所以两种 $T$ 的第 1 坐标均恰为 $a_0\eta_0=\eta_0$。

取任意充分大整数 $L\ge256$，在块 $[L,2L)$ 用真实纠错所用的纯右逆，取
$$
h_0=\Omega,\qquad D_{[L,2L)}h_1=h_0,\qquad
D_{[L,2L)}h_2=h_1,
$$
其中 $h_k$ 恰有 $k$ 孔，且
$$
\|h_k\|\le(\sqrt{32}L^{3/2})^k\quad(k=1,2).
$$
低头以外、该块以下全部位真空。令
$$
V_L=v\otimes h_0-T_2v\otimes h_1+T_2^2v\otimes h_2.
\tag{4.2}
$$
式 (4.1) 使有限模型准确抵消。沿用 R185/R188 已付清且 R214 允许任意后移块的真实误差，
$$
\|TV_L\|\le26\eta_{L-1}\|V_L\|.
\tag{4.3}
$$
并且
$$
\|V_L\|\le H_L:=
1+6\sqrt{32}L^{3/2}+1152L^3=O(L^3).
\tag{4.4}
$$

现在准确计算纯 $D$ 的低头输出。$D$ 作用于 $k\ge2$ 的块孔数只能降到 $k-1\ge1$，仍不进入低头；作用于 $k=1$ 项的块部分恰给 $-T_2v$。因此
$$
P_2DV_L=D_2v-T_2v,\qquad(DV_L)_1=-\eta_0.
\tag{4.5}
$$

使用已证残差比例延拓
$$
E_p:\mathcal F_p\longrightarrow N,\qquad
\|E_pu-u\|\le2A_p\|Tu\|,\quad A_p=e^{8p2^p},
$$
取 $p=2L$，定义真正核向量
$$
g_L=E_{2L}V_L\in N.
$$
由 (4.3)，
$$
\|g_L-V_L\|\le52A_{2L}\eta_{L-1}H_L\longrightarrow0.
\tag{4.6}
$$
这里的趋零有直接预算：$\log A_{2L}=16L4^L$，而
$\log\eta_{L-1}\le-(770/16)16^L$，后者压倒前者和 $\log H_L$。

选取一个固定的大 $L$，使 (4.6) 不超过 $\eta_0/4$，记 $g=g_L$。由于 $\|D\|<2$，由 (4.5) 得
$$
\boxed{g\in N\subset M,\qquad |(Dg)_1|\ge\eta_0/2>0.}
\tag{4.7}
$$
这就是所需的实际见证。它保留 $e_2$ 处系数 1，因此也是非真空、无限支持的核向量。

## 5. 反向像不包含及单侧比较的含义

由 (3.2)、(4.7)，存在正数
$$
c_g=\frac{\|Dg\|}{\|g\|}>0
$$
使每个有界 $U$ 都满足
$$
\boxed{\|D-TU\|_{\mathrm{ess}}\ge\|D|_M\|\ge c_g>0.}
\tag{5.1}
$$
所以不存在 $D=TU$，即使允许再加紧误差也不可能。

这还给真正的像不包含：
$$
\boxed{\operatorname{Ran}D\not\subseteq\operatorname{Ran}T.}
\tag{5.2}
$$
为避免偷用未说明的像因子定理，可直接证明：若有包含，对每个 $x$ 考虑 $Tu=Dx$，并令 $Ux$ 是这个方程在 $(\ker T)^\perp$ 中的唯一最小范数解。它是处处定义的线性映射；若 $x_n\to x$、$Ux_n\to y$，连续性给 $Ty=Dx$，且 $y\perp\ker T$，故 $y=Ux$。闭图定理使 $U$ 有界，从而 $D=TU$，与 (5.1) 矛盾。

另一方面，(4.7) 直接排除 $D=UT$：作用于 $g\in\ker T$ 即矛盾。其模紧版本也成立。所取固定 $L$ 的初值 $V_L$ 满足 $\|TV_L\|\le26\eta_{L-1}H_L$；在归一化后，其头 $2L$ 已进入标准真实修复预算。故 $g$ 属于已证弱复制的标准有限块纠错类，存在精确核弱副本 $g_n\in M$，满足
$$
g_n\rightharpoonup0,\qquad
\|g_n\|\to\|g\|,\qquad
\|Dg_n\|\to\|Dg\|.
$$
由于 $Tg_n=0$，同样
$$
\boxed{\|D-UT\|_{\mathrm{ess}}\ge c_g\quad(U\in B(H_-)).}
\tag{5.3}
$$
这里只对这个已构造 $g$ 使用弱复制，不把它推广到整个未知 $M$。

结合 R220，实际慢和与纯慢和的像互不包含，两种方向、两种单侧有界因子都不能成立。本稿的 (5.1) 和 (5.3) 还排除了反向因子的任意紧误差。

## 6. 对形式伴随原像路线的准确限制

若能对全空间给 $\|D^*u\|\le C\|T^*u\|$，便与本稿的真实反射序列直接矛盾：该序列满足
$$
x_m\rightharpoonup0,\qquad
\|T^*x_m\|\to0,\qquad
\|D^*x_m\|\to\|Dg\|>0.
$$
因此此类全局控制严格不可能。

这不排除对假设缺陷 $w\in W$ 的那一个形式原像 $h$ 建立特殊的两孔或多孔估计，也不排除任何需同时使用 $Tw=0$ 与 $w\perp BM$ 的更细递推。这里没有得到对所有孔阶一致可求和的预算，$N=M$ 仍未决定。

依赖：R185/R188 的实际有限块模型误差；R214 的任意后移块；旧残差比例延拓笔记中的 $E_p:\mathcal F_p\to N$；R187 的有限头核；实际弱复制笔记。所有新反射与像比较证明均已在本文写全。
