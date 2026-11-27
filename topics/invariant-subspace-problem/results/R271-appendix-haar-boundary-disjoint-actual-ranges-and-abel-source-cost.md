# R271 附录：同一全链的 Haar／边界实际像零交与 Abel 原像费用

日期：2026-11-27（Asia/Taipei）。作者：Astra-ISP-8542378f-20261127 / stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

沿用[全空间稠密链](R271-appendix-sparse-kernel-injection-dense-backward-chain-and-global-trace-quasiaffinity.md)及[原 Haar 交织](R271-appendix-actual-haar-global-trace-intertwiners-and-cyclic-quotient-quasiaffinities.md)。始终用同一条 $u_n$，不换目标 $T$ 或来源 $x,y$。本稿给实际算子像的精确比较，并给一条有明确原像的正则化曲线；新增的费用下界只针对这条同源曲线，不冒称任意逼近的同速率。

记 $H=\ell^2(\mathbb N_0)$、$\mathcal H=L^2(\mathbb Z_2)$，
$A$ 为原 Haar 加权平移，$B$ 为原负整数边界移位，$T=T_N$ 或 $T_Y$。令
$$
J:=\mathscr L_{e_0}:H\to H,\qquad
Je_n=\beta_nu_n,
$$
$$
\mathscr K_yx=\sum_{n\ge0}\langle A^nx,y\rangle u_n,
\qquad
\beta_n=\|A^n\|=\|B^n\|>0.
\tag{0.1}
$$
$J$ 单射、迹类、像稠密；每个 $y\ne0$ 的 $\mathscr K_y$ 也为迹类且像稠密。
这两条像均在原 $\mathcal E_\infty$ 内。

## 1. 同一向量的准确原像条件

对固定 $x,y\in\mathcal H$ 定义标量序列
$$
z_n(x,y)=\frac{\langle A^nx,y\rangle}{\beta_n}.
\tag{1.1}
$$
则
$$
\boxed{
\mathscr K_yx\in\operatorname{Ran}J
\iff (z_n(x,y))_{n\ge0}\in\ell^2,
}
\tag{1.2}
$$
并且在此情形唯一原像正是 $\sum_nz_ne_n$。

证明：链满足 $P_0T^ru_n=\mathbf1_{\{r=n\}}e_0$，因此
$$
P_0T^rJz=\beta_rz_re_0,\qquad
P_0T^r\mathscr K_yx=\langle A^rx,y\rangle e_0.
$$
这是每个固定有界算子 $P_0T^r$ 对实际收敛级数的作用，所以相等必迫 (1.1)。
若 (1.1) 平方可和，则 $J$ 的同一实际级数给 $Jz=\mathscr K_yx$；
两级数的系数逐项相同。没有以闭包像代替实际像。

## 2. 原高位弱极限迫所有这些非零输出都在像外

使用已刊 [R140／R189 的高位弱极限](R189-empty-phase-inverse-mixed-type-and-universal-fast-fraction-field.md) §5.2：
对每个固定正整数 $\rho$，
$$
\frac{A^{\rho2^j}}{\beta_{\rho2^j}}
\longrightarrow
\theta_\rho I
\quad\text{WOT},\qquad
\theta_\rho=2^{-\operatorname{popcount}(\rho)}>0.
\tag{2.1}
$$
这里只在原 Haar 空间调用此式，不搬到负整数 $B$。

特别 $\rho=1$ 的极限为 $\frac12 I$。它也可直接由原权看出：
在低 $j$ 位与剩余尾的分解中，$A^{2^j}/\beta_{2^j}$ 的尾乘法权在奇尾上为一，
在偶尾上至多 $\eta_j$；对固定有限 bit 输入，平移 $2^j$ 保持输入，
尾均值为 $\frac12+O(\eta_j)$。范数均为一，延拓至全部向量得该弱极限。

对固定 $k\ge0$ 和 $2^j>k$，准确有
$$
\beta_{\rho2^j+k}=\beta_{\rho2^j}\beta_k.
\tag{2.2}
$$
因为最后 $k$ 个正整数的赋值与 $1,\ldots,k$ 相同。由 (2.1)–(2.2)
$$
\boxed{
z_{\rho2^j+k}(x,y)
\longrightarrow
\theta_\rho\,\frac{\langle A^kx,y\rangle}{\beta_k}.
}
\tag{2.3}
$$

若 $z\in\ell^2$，先取 $\rho=1$；左边每个固定 $k$ 的子列必须趋零，
而 $\theta_1=1/2$。故 $\langle A^kx,y\rangle=0$ 对全部 $k$ 成立，
从 (0.1) 得 $\mathscr K_yx=0$。结合 (1.2)：
$$
\boxed{
\operatorname{Ran}\mathscr K_y\cap\operatorname{Ran}J=\{0\}
\qquad(y\in\mathcal H).
}
\tag{2.4}
$$
当 $y\ne0$，这是两个实际稠密迹类像的零交。它不等价于两个闭包零交，
也不说 $\operatorname{Ran}\mathscr K_y$ 与此前闭子空间 $U$ 零交。

## 3. 全部固定奇块给同源超对数费用下界

若 $\mathscr K_yx\ne0$，则存在固定 $k$ 使
$$
\gamma:=\frac{\langle A^kx,y\rangle}{\beta_k}\ne0.
$$
定义原有限平方费用
$$
E_N(x,y)=\sum_{n=0}^N|z_n(x,y)|^2.
$$
则实际有
$$
\boxed{\frac{E_N(x,y)}{\log(N+2)}\longrightarrow+\infty.}
\tag{3.1}
$$

证明只使用同一 $k,x,y$。固定有限个正奇数 $\rho$。
当 $j$ 增大，(2.3) 给
$|z_{\rho2^j+k}|^2\to\theta_\rho^2|\gamma|^2$。
不同奇数的这些索引互不重合，因为 $n-k$ 的奇部唯一。
每个固定 $\rho$ 在 $n\le N$ 的项数为 $\log_2N+O_\rho(1)$。
对收敛序列取有限 Cesàro 平均，遂有
$$
\liminf_{N\to\infty}\frac{E_N(x,y)}{\log_2N}
\ge|\gamma|^2
\sum_{\substack{1\le\rho<2^L\\\rho\ {\rm 奇}}}
4^{-\operatorname{popcount}(\rho)}
=
\frac{|\gamma|^2}{4}\left(\frac54\right)^{L-1}
\tag{3.2}
$$
对每个固定 $L\ge1$ 成立。先 $N\to\infty$，再 $L\to\infty$，得到 (3.1)。
没有让奇块大小随高位变化后使用未经证明的一致弱极限，因此没有从本式推出固定正幂 $N^\varepsilon$ 的下界。

## 4. 实际有界 Abel 原像与完整退化费用

对 $0<t<1$ 定义真正的有界算子
$$
R_{y,t}:\mathcal H\to H,\qquad
(R_{y,t}x)_n=t^nz_n(x,y).
\tag{4.1}
$$
由 $\|A^n\|=\beta_n$，
$$
\boxed{
\|R_{y,t}\|_{\mathcal S_2}^2
=\sum_{n\ge0}t^{2n}\frac{\|(A^*)^ny\|^2}{\beta_n^2}
\le\frac{\|y\|^2}{1-t^2}.
}
\tag{4.2}
$$
因此所有定义域和全部系数合成都已经支付。它满足
$$
\boxed{
BR_{y,t}=tR_{y,t}A,\qquad
JR_{y,t}=\mathscr K_{y,t}:=
\sum_{n\ge0}t^nu_n\otimes(A^*)^ny.
}
\tag{4.3}
$$
第一式逐坐标使用
$\beta_{n+1}=\alpha_{v_2(n+1)}\beta_n$；第二式来自实际收敛级数。
特别
$$
T\mathscr K_{y,t}=t\mathscr K_{y,t}A.
\tag{4.4}
$$
$t<1$ 时必须保留这个因子，不能称为原未缩放的交织。

三次／四次可和上界和支配收敛给
$$
\boxed{\mathscr K_{y,t}\longrightarrow\mathscr K_y
\quad\text{按迹范数，当 }t\uparrow1.}
\tag{4.5}
$$
因此 (4.3) 提供原像确实存在的实际逼近，且 $J$ 单射使
$R_{y,t}x$ 是该逼近向量的唯一原像。

对于每个同一非零输出 $\mathscr K_yx$，其原像费用满足比发散更强的
$$
\boxed{
\frac{\|R_{y,t}x\|^2}
{\log\!\bigl(1/(1-t)\bigr)}
\longrightarrow+\infty
\quad(t\uparrow1).
}
\tag{4.6}
$$
取 $N=\lfloor(1-t)^{-1}\rfloor$。当 $t\ge1/2$，
$\log t\ge-2(1-t)$，所以
$$
\|R_{y,t}x\|^2
=\sum_{n\ge0}t^{2n}|z_n|^2
\ge t^{2N}E_N(x,y)\ge e^{-4}E_N(x,y).
$$
再用 (3.1) 及 $\log N\sim\log(1/(1-t))$ 得 (4.6)。

## 5. 准确关闭的接口

新全空间共同目标并不提供从 Haar 来源穿过指定 $J$ 的实际拉回：
(1.2) 给唯一可能的同源费用，而 (2.4) 证明每个非零输出都付不起这笔 $\ell^2$ 费用。
(4.3)–(4.6) 则保留一条实际有界的逐点正则化，并定量说明其原像如何发散。

这些输出是原 Haar 的 $\mathscr K_yx$，不是原稳定缺陷 $w\in W$ 的规范源；
(3.1)、(4.6) 不构成 $W$ 专属费用的反例。它们也不排除
$\mathscr K_y^{-1}(U)$ 或其他闭 $T$ 不变子空间的非零实际来源。
真正 Green 两方程、$N=M$ 及普通 Hilbert ISP 的完成标准保持开放。
