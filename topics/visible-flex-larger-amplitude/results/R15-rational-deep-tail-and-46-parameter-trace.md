# R15：固定有理深尾、46 参数真实 trace 与可执行线性 Green 账本

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**状态：下述深尾推广和线性账本有完整证明；浅部大幅前缀与该真实 trace 的非线性匹配仍未完成。** 本文不是完整闭曲面、幅度或 reach 的完成证明。它使用仓库已采用的 R20 全解析局部胞元引理；不另设独立审查门槛。

本文解决一个具体的定义欠账：有限程序的 `calibrationSteps=512` 不能定义或认证全部无限层的精确校准根。这里为以后的一条新固定度量选用**不作校准的有理深源**，并用实际倾斜中心束代替精确的水平中心轴。原来保存的 `g_stored`、它的全部数值结论和固定度量加密链均保持原意义。

## 1. 新度量如何固定，哪些东西确实保持

取

$$
R=64,\quad a=11/4,\quad \delta_n=d_0 2^{-n},\quad
c_n=c_0 2^{-n/2},\quad \eta_n=c_n\delta_n,
\quad \alpha_n=65/64.
\tag{1.1}
$$

其中 $d_0,c_0$ 只固定一次，满足

$$3/500\le d_0<1/128,\qquad 3/5\le c_\eta:=c_0/\sqrt{d_0}\le2/3,
\qquad 0<c_0\le1/16.$$

参考选择是 $d_0=3/500,c_0=1/20$。要逐字保留现有计算的源长度，可以取原 IEEE-754 存数的**精确有理值**

$$d_0=3458764513820541/576460752303423488,\quad
c_0=3602879701896397/72057594037927936.$$

它们满足上述同一组不等式。本文的线性常数同时覆盖这两种固定选择；adapter 采用后一种，绝不把存数默认为不同的十进制有理数。下文所有指数/对数函数定义为相应固定实参数的数学函数，浮点函数求值是其数值近似。

每个深胞元使用现有的九段 quintic-log 配方，依次连接相对值

$$1,\quad 64/\delta_n,\quad \delta_n/(65/64),\quad1/\delta_n,\quad2^{11/4}.$$

三个中平台各长 $\delta_n$；四转接和两个端口各长 $\eta_n$。转接函数严格取

$$S(t)=10t^3-15t^4+6t^5.$$

于是整个深源由有限个有理常数和明确函数定义；**没有“把某次浮点根当作精确根”的步骤**。端口长度、半径、相对端值和两阶端口 jets 不依赖中间谷值参数 $\alpha_n$。因为 $S'(0)=S'(1)=S''(0)=S''(1)=0$，改变一个胞元内部的 $\alpha_n$ 不改它与相邻胞元的端口两 jet。

对现有配置，可以只从未改造区 $n\ge J=\texttt{protectCell}=160$ 开始采用 (1.1)，逐字保留 $0\le n<160$ 的源 profile、浅部 cap/valley/warp、全宽归一系数及前缀。原 `assemble` 的全宽系数不得因为这一步重新计算后再声称浅部不变；本定义直接保留它。$n\ge160$ 的源长度和端口位置不随 $\alpha$ 改变，所以不用重新归一浅部。该操作仍然定义了**新度量**，不能接在旧 `g_stored` 加密链后冒充同一 $g$。

在本证明的深域用 $\rho=r/r_c$ 归一到 $1\le\rho\le2$。将常数吸收到一次固定的 $\epsilon>0$，写

$$P=\epsilon\delta_n^{11/4}p_{*,n},\qquad w=P/\rho^7,
\qquad g=(1+w^2)d\rho^2+\rho^2d\theta^2.$$

最后乘回 $r_c^2$ 即得物理度量。深起点 $N\ge J$ 只选一次，之后不随解参数、Fourier 阶数或数值容差变化。

## 2. 采用的局部输入与为何不需要精确校准

固定来源为提交 `869436630c99aa5a68afb55bd8877c826034d117` 中：

- [R20 §§2、7](../../large-amplitude-twist-flex/results/R20-mild-r64-c2-single-tail.md)：完整非线性/mean、全频局部 Cauchy map、整胞元两 jet 与单值发展。
- [局部胞元估计 L](../../large-amplitude-twist-flex/notes/general-geometry-mild-tail-huge-r-cell-estimates.md) §§0–4：其 profile 假设是 $1/2\le\alpha\le2$；§4.1 的实际传递趋近在该整区间一致成立。
- [全解析胞元 map A](../../large-amplitude-twist-flex/notes/general-exact-mild-tail-full-analytic-map.md) §§2–10：任意固定角宽差 $h>0$ 的 Galerkin/全频校正。
- [二次材料 Q](../../large-amplitude-twist-flex/notes/general-exact-mild-tail-quadratic-material.md) §§1–7：常数允许依赖固定 $\delta_0,c_\eta$，假设只有统一 $\alpha$、半径及正 slope 界。

参考选择有 $c_\eta=\sqrt{5/12}$，adapter 的 dyadic 选择仍在 $[3/5,2/3]$ 内。把原 $\delta_0=.08$ 改为这里固定的 $d_0$ 后，各证明中唯一涉及这两个常数的输入是：

1. $\eta=c_\eta\delta^{3/2}$，且在 $n\ge1$ 上 $\eta/\delta=c_n\le1/(16\sqrt2)<.05$；
2. $1/2\le\alpha\le2$；
3. 有界固定半径比和 $w\le1$；
4. 四个 log 跳幅和不超过 $2\log(128)+6|\log\delta|$。

这些逐项成立。材料积分仍是 $C\delta^{-2}$，转接增益仍是固定幂 $\delta^{-2890}$，低模内传播仍是 $C(1+M)^{12}$，原点物理小球及完整 mean 小根不使用 $(T_2)_{21}=0$。精确校准只在 R20 §3 的特殊水平中心列/乘积公式中被使用；本文不使用那个公式。

具体地，取任意固定 $h>0$，令

$$
\gamma=h/32,\quad
M_n=2\left\lceil\frac{10016}{2\gamma}(1+|\log\delta_n|)\right\rceil.
$$

在一次充分深的共同起点以后，存在固定 $c_*,C_*>0$，使完整实际胞元 map 满足

$$
\Phi_n:B_{\mathscr A_{\tau+h}}(\rho_n)\to\mathscr A_\tau,
\qquad
\rho_n=c_*\epsilon\delta_n^{19/4}(1+M_n)^{-60},
\tag{2.1}
$$

$$
\Phi_n(U)=T_nU+\mathscr R_n(U),\quad
\|\mathscr R_n(U)\|\le
\frac{C_*(1+M_n)^{72}}{\epsilon\delta_n^{19/4}}\|U\|^2,
\tag{2.2}
$$

以及同系数的二次 Lipschitz 界。全胞元的实际 nonmean 零阶和全部二阶以内 jets、mean 一二阶满足

$$
\|\mathcal J_n(U)\|_{C^2,\tau}
\le C_*(1+M_n)^{15}\delta_n^{-7/2}\|U\|_{\mathscr A_{\tau+h}}.
\tag{2.3}
$$

完整 mean 保留。常数与绝对角宽无关，允许依赖这里已经固定的 $h,c_\eta,\delta_0$ 和半径归一。$M_n$ 仅为局部证明 cutoff；最终场没有截断。

这几个界的取得仍是 A 中同一个具体流程：以压缩 Galerkin 逆在 (2.1) 上继续低模近解；使用全密度残差；通过一次固定角差的 forced Volterra 校正加入所有高模；在共同复球上以 Cauchy 估计取得 (2.2)。在该流程中 $\alpha=65/64$ 完全符合 L/Q 的整区间假设，故无需另假定未证明的数值校准误差界。

## 3. 实际线性块、完整谱和46个自由参数

写 $m=2j$，

$$
\nu_j=j^2(4j^2-1)/3,\quad d=2^{-11/4},\quad \alpha=65/64.
$$

真实 raw 块仍由 canonical 系统积分后乘 $\operatorname{diag}(1,d)$ 得到。三个平台的实际极限为

$$
T_{2j,\infty}=
\begin{pmatrix}
1-65\nu_j&65/64\\
65d\nu_j(\nu_j-1)&d(1-(65/64)\nu_j)
\end{pmatrix}.
\tag{3.1}
$$

其两个特征值是 $-L_j,-S_j$，$L_jS_j=d$，且

$$
64\nu_j<L_j<65(1+d/64)\nu_j\quad(j\ge2).
\tag{3.2}
$$

$j=1$ 时恰为 $-64,-d/64$。

现在改选

$$
h=\frac{\log2}{4},\quad b=\frac{11}{2},\quad
\tau_n=\tau_0+(n-N)h,\quad \zeta_n=\epsilon\delta_n^b,
\tag{3.3}
$$

其中 $\tau_0>0$ 先固定。定义

$$
X_{j,n}=\zeta_n^{-1}e^{2j\tau_n}(-1)^{jn}U_{j,n}.
$$

实际关系为

$$
X_{n-1}=\mathcal A_nX_n+\mathscr R_n^\sharp(X_n),\qquad
(\mathcal A_n)_j=(-1)^j2^{-11/2-j/2}T_{2j,n}.
\tag{3.4}
$$

理想块 $A_j=(-1)^j2^{-11/2-j/2}T_{2j,\infty}$ 的第一模大特征值仍恰为1，因为 $b+1/2=6$。对 $j\ge2$，大特征值模长介于

$$
\nu_j2^{-(j-1)/2}\quad\hbox{和}\quad
(65/64)^2\nu_j2^{-(j-1)/2}.
\tag{3.5}
$$

逐个整数比较给

$$
\nu_j^2>2^{j-1}\ (2\le j\le46),\qquad
(65/64)^4\nu_{47}^2<2^{46}.
$$

从 $j=12$ 起，$\nu_{j+1}/\nu_j<\sqrt2$，且该比值递减：由

$$
\frac{\nu_{j+1}}{\nu_j}
=\left(\frac{j+1}{j}\right)^2\frac{2j+3}{2j-1}
$$

两因子分别递减即可。因此恰有 $j=2,\ldots,46$ 共45个不稳定方向；$j\ge47$ 的两个方向都稳定。连同第一模中心标签，得到46个自由实参数，物理频率为 $2,4,\ldots,92$。

这些是所选权空间中的自由度；不是所有 $C^2$ 尾的分类或维数上界。

## 4. 不用巨大指数常数的实际矩阵漂移界

以下为新推导；它直接比较实际九段乘积，保留真实转接。

令 $m=2j$、$k=(m^2-4)/\sqrt{12}$、$\omega^2=(7m^2-16)/12$。三个中平台的 canonical 生成元为

$$
B_p=\begin{pmatrix}k\delta&\delta^2/p\\-\nu_jp&-k\delta\end{pmatrix},
\quad p=64,\delta^2/\alpha,1,
\quad B_p^2=-\omega^2\delta^2I.
$$

所以实际平台指数是

$$e^{B_p}=\cos(\omega\delta)I+\operatorname{sinc}(\omega\delta)B_p.$$

理想三个 shear 的范数分别为

$$s_1=1+64\nu_j,\quad s_2=1+\alpha,\quad s_3=1+\nu_j.$$

设相应非零 shear 元素的模为 $n_i=(64\nu_j,\alpha,\nu_j)$，并设 $c_i=(1/64,\nu_j/\alpha,1)$。由 $|\cos x-1|\le x^2/2$、$|\operatorname{sinc}x-1|\le x^2/6$、$|\operatorname{sinc}x|\le1$，每个平台误差不超过

$$
e_i\le |k|\delta+
\delta^2\{\omega^2(1/2+n_i/6)+c_i\}
\le E_i\delta.
\tag{4.1}
$$

六个短段每个的生成元积分范数不超过

$$
L=c_n(|k|\delta+64\nu_j)
\le c_\eta(|k|+64\nu_j)\sqrt\delta.
\tag{4.2}
$$

因而其传播范数至多 $e^L$、与单位矩阵的差至多 $e^L-1$。逐因子展开实际乘积与理想乘积之差，得到

$$
\|T_{m,n}-T_{m,\infty}\|_1
\le e^{6L}\prod_i(s_i+e_i)-\prod_i s_i.
\tag{4.3}
$$

这只是矩阵三角不等式；没有交换矩阵次序。

当 $6L\le1$ 且 $e_i/s_i\le1$ 时，$e<3$ 给

$$
\|T_{m,n}-T_{m,\infty}\|_1
\le3\prod_i s_i\left(6L+4\sum_i e_i/s_i\right).
\tag{4.4}
$$

对全部 $j\ge1$，$|k|\le\nu_j$、$\omega^2\le\nu_j$、$c_\eta<2/3$，并且

$$
\prod_i s_i\le390\nu_j^2,\qquad E_i/s_i\le(5/2)\nu_j.
$$

故

$$
\boxed{\|T_{2j,n}-T_{2j,\infty}\|_1
\le339300\nu_j^3\sqrt{\delta_n}
<2^{20}j^{12}\sqrt{\delta_n}.}
\tag{4.5}
$$

取 $J_0=16384$。对 $j<J_0$ 有 $m<2^{15}$。在 $n\ge128$ 时，(4.2) 给 $6L<2^{65}\sqrt\delta<1$，而 (4.1) 给 $e_i/s_i\le(5/2)\nu_j\delta<1$；所以 (4.5) 对这个**完整有限块**一致成立。

由

$$
\max_{x>0}x^{12}2^{-x/2}
=\left(\frac{24}{e\log2}\right)^{12}
< (27/2)^{12}<2^{46},
$$

归一化后的有限块误差常数可取

$$\boxed{C_E=2^{61}.}\tag{4.6}$$

这里只使用 $e>8/3$、$\log2>2/3$；这些常数可由普通级数直接界定。

## 5. 真实高模、理想高模与 Green 常数

L §3 的实际全模估计不需要校准根：

$$
\|T_{m,n}\|_1\le C_L(1+m)^{308}e^{m\beta(\delta_n)},
$$

$$
\beta(\delta)=3\delta+6c_\eta\delta^{3/2}
+\sqrt{(15/2)c_\eta\delta^{3/2}{2\log128+6|\log\delta|\}}.
$$

这里 $C_M<23$、$2^a<7$、$e<3$ 给

$$
C_L\le7\{3^6 68^3+8\cdot64^3\cdot23^4\cdot8\}<2^{46}.
$$

对所有 $n\ge128$，$\delta_n<2^{-n-7}$、$|\log\delta_n|<n+6$，从上述式子立即有 $256\beta(\delta_n)<h/4$。特别地 $\beta\le h/4$，故

$$
\|(\mathcal A_n)_j\|_1
\le2^{-11/2}C_L(1+2j)^{308}2^{-3j/8}.
$$

在 $j=J_0=16384$，用 $1+2J_0<2^{16}$ 得上界小于 $2^{-1175}<1/4$。该 majorant 此后递减，因此全部 $j\ge J_0$ 的实际块都小于 $1/4$。

令 $B_n$ 在 $j<J_0$ 上取理想块 $A_j$，在 $j\ge J_0$ 上取真实 $(\mathcal A_n)_j$。于是

$$\mathcal A_n=B_n+\mathcal E_n,\qquad
\|\mathcal E_n\|\le2^{61}\sqrt{\delta_n}.\tag{5.1}$$

理想块还可从 $j=110$ 起整体处理：

$$
\|A_j\|_1\le2^{-11/2-j/2}
\{(260/3)j^4+(52/3)j^8\}<1/4\quad(j\ge110).
\tag{5.2}
$$

在110的有理上界为 $.230195$，之后两个单项分别递减。因此不必对110至16383的几乎平行特征投影分别取范数。

取

$$
\mathcal X=\ell^\infty_{n\ge N}\ell^1_{j\ge1}(\mathbb C^2),\qquad
\|F\|_{\mathcal Y}=\sup_{n>N}\delta_n^{-3/8}\sum_j|F_{j,n}|_1.
\tag{5.3}
$$

参考 Green 解 $X_{n-1}=B_nX_n+F_n$ 时，对中心校正规定无穷端极限0，对45个不稳定方向规定 cut 值0。稳定/中心和不稳定标量公式分别是

$$x_n=\sum_{k\ge1}\lambda^{k-1}f_{n+k},\qquad
x_n=-\sum_{s=N+1}^n\lambda^{-(n-s+1)}f_s.$$

高模用对应有序矩阵乘积。有限理想块先作真实谱投影。

对 $47\le j<110$，两个特征值有相同符号，模为 $r_j,s_j<1$。Cayley–Hamilton 恒等式给

$$
\sum_{k\ge0}\|A_j^k\|_1
\le1+\frac{\|A_j\|_1+r_js_j}{(1-r_j)(1-s_j)}.
\tag{5.4}
$$

这是把整块相加，保留两个投影间的抵消。不是用谱半径代替矩阵范数。对 $j=1,\ldots,46$，按真实投影范数和谱隙逐项相加；对全部 $j\ge110$，用 $1/4$ 整块上界。所得明确常数满足

$$
\boxed{\|\mathcal G_0F\|_{\mathcal X}
\le C_G\delta_N^{3/8}\|F\|_{\mathcal Y},\qquad C_G<2^{27}.}
\tag{5.5}
$$

附属脚本 [closure_rational_tail_linear.py](../computations/closure_rational_tail_linear.py) 用有理区间和整数开根证明全部有限比较。实际相加的有理上界约为 $5.913151568\times10^7$，小于 $2^{27}$；所有 PASS 使用精确分数而非该小数。结果为 [线性账本 JSON](../notes/2026-11-12-closure-rational-linear.json)。

特别地

$$
\|\mathcal G_0\mathcal E\|\le C_G C_E\sqrt{\delta_N}
<2^{85-N/2}.
\tag{5.6}
$$

$N\ge192$ 已使这一线性扰动范数至多 $2^{-11}$。**这不是全部非线性起点的认证。**

## 6. 实际中心束、真实 Green 和全部非线性门

令理想中心向量为 $e_c=(1,0)$，45个不稳定向量 $e_j^u$ 按 $\ell^1$ 范数归一。参数

$$\mathbf b=(q,b_2,\ldots,b_{46}),\qquad |\mathbf b|_1<1/4.$$

参考齐次列为中心常数 $qe_c$ 和不稳定列

$$H_{j,n}=\lambda_j^{-(n-N)}b_je_j^u,$$

其余为0。实际线性列为

$$
X^{\rm lin}=(I-\mathcal G_0\mathcal E)^{-1}H,
\qquad
\|X^{\rm lin}-H\|\le\frac{\eta_N}{1-\eta_N}|\mathbf b|_1,
\quad \eta_N=C_GC_E\sqrt{\delta_N}.
\tag{6.1}
$$

Neumann 级数在 (5.6) 下真实收敛。这就是实际的倾斜中心/不稳定束；不存在把 $\xi=0$ 轴仍然宣布为精确中心列的步骤。第一模只有中心参数时，在更深端口重复相同未来 Green 估计给

$$X_{1,n}^{\rm lin}=q(e_c+O(\sqrt{\delta_n})).$$

其第二分量一般不为0。实际线性 Green 为

$$\mathcal G=(I-\mathcal G_0\mathcal E)^{-1}\mathcal G_0,$$

范数至多 $(1-\eta_N)^{-1}C_G\delta_N^{3/8}$，并保持相同中心无穷端和不稳定 cut 规范。

由 (2.2)、(3.3) 得

$$
\|\mathscr R_n^\sharp(X)\|
\le C_1(1+M_n)^{72}\delta_n^{3/4}\|X\|^2,
\qquad C_1=2^{-11/2}C_*.
\tag{6.2}
$$

定义

$$
A_N=\sup_{n\ge N}(1+M_n)^{60}\delta_n^{3/4},\qquad
B_N=\sup_{n>N}(1+M_n)^{72}\delta_n^{3/8}.
\tag{6.3}
$$

$M_n\le C(1+n)$，所以两者有限并趋零。选择一个共同有限 $N$，除了 (2.1) 的局部起点、半径/角宽等门外，明确要求

$$
c_*^{-1}A_N\le1/4,\quad
C_GC_E\sqrt{\delta_N}\le1/4,\quad
2C_GC_1\delta_N^{3/8}B_N\le1/4.
\tag{6.4}
$$

全部常数先固定，故这样的 $N$ 存在。[R17](R17-explicit-rational-tail-nonlinear-depth.md) 进一步逐项给出保守数值
$c_*=2^{-256},C_*=2^{320}$ 和当前配置可用的 $N=4096$；这不来自有限曲面样本。浅头的大幅数据是否落在这一精确图的可延拓范围，仍是另一项未完成的匹配问题。

在同一个单位 $\mathcal X$ 球解

$$
\boxed{X=H(\mathbf b)+\mathcal G_0
\{\mathcal E X+\mathscr R^\sharp(X)\}.}
\tag{6.5}
$$

右侧 Lipschitz 常数至多 $1/2$，把单位球映入自身。共同复球上的 Banach 收缩给完整全频解和参数全纯性。自由参数的真实意义保持为

$$
\lim_{n\to\infty}P_cX_{1,n}=qe_c,\qquad
P_{j,u}X_{j,N}=b_je_j^u\quad(2\le j\le46).
$$

这与45个任意 cut 高度不是同一说法；下一节才支付其坐标转换。

## 7. 完整 mean、整胞元 C²、单值嵌入

(6.5) 精确匹配相邻真实 Cauchy map 的 raw 值。raw 非mean值/径向导数一致；完整通量1的小根唯一性使 mean 梯度也匹配。只保留一次 mean 高度常数，并沿整个尾积分，不在各圈重置。

(2.3) 和 $\|U_n\|\le\epsilon\delta_n^{11/2}$ 给整个胞元上的界

$$
\|\operatorname{jets}_{\le2,\perp}v\|_{
\mathrm{cell}\ n}
+\|\operatorname{jets}_{1,2}\overline v\|_{
\mathrm{cell}\ n}
\le C_*\epsilon(1+M_n)^{15}\delta_n^2\longrightarrow0.
\tag{7.1}
$$

背景由固定有理深源直接有 $w=O(\delta_n^{7/4})$、$w_r=O(\delta_n^{1/4}(1+|\log\delta_n|))$。因此完整高度在 cuff 真实 $C^2$ 接到平面；(7.1) 控制全部胞元，不只是端口。

R20 §7 的投影 coframe 由完整 Darboux 方程得到 curl0；完整通量根给角周期 $2\pi$；平端点使平移 period 为0。固定一次平面刚体规范后恢复单值 $C^2$ 等距映射。物理小球给正角连接和正法向支持函数径向导数，故投影圆严格凸且嵌套，深尾为嵌入。这个论证只作用于所建深尾域，不给浅头或整闭面的 reach。

同一复参数球内的整胞元两 jet 界及 (7.1) 也给 $C^2$ 值的参数全纯性。全部参数共用这一次固定的 $g$ 和同一 $N$。

## 8. 可实际求解的低频 Dirichlet chart

在深端 $N$ 选出 $X_{j,N}$ 的第一分量，$1\le j\le46$，组成 $D(\mathbf b)$。理想不稳定向量可写成 $(1,s_j)$；由 (3.1) 的两特征值公式，

$$-d\nu_j<s_j\le0.$$

所以按 $\ell^1$ 归一后，它的第一分量至少

$$
\kappa=\min_{j\le46}(1+|s_j|)^{-1}
>\frac{6}{5969242}>10^{-6}.
\tag{8.1}
$$

第一模中心的第一分量为1。由 (6.1)，$D'(0)$ 与此可逆对角矩阵的差不超过 $\eta_N/(1-\eta_N)$。若把深起点进一步选到 $N\ge224$，则线性账本给 $\eta_N<2^{-27}$，因此 $D'(0)$ 可逆，且可取

$$\|D'(0)^{-1}\|_{\ell^1\to\ell^1}\le2\times10^6=:A.\tag{8.2}$$

同时保留所有非线性门。令

$$r=C_GC_1\delta_N^{3/8}B_N\le1/8.$$

收缩估计给 $\|X(\mathbf b)\|\le2|\mathbf b|_1$，以及

$$
\|X(\mathbf b)-X^{\rm lin}(\mathbf b)\|
\le8r|\mathbf b|_1^2,
$$

$$
\|R(\mathbf b)-R(\mathbf c)\|
\le8r(|\mathbf b|_1+|\mathbf c|_1)|\mathbf b-\mathbf c|_1.
\tag{8.3}
$$

于是令

$$r_b=\min(1/4,(32Ar)^{-1}),\qquad r_z=r_b/(2A).$$

对 $|z|_1<r_z$，方程

$$\mathbf b=D'(0)^{-1}z-D'(0)^{-1}\{D(\mathbf b)-D'(0)\mathbf b\}$$

在 $|\mathbf b|_1\le r_b$ 上收缩，给低46高度坐标的解析反函数。

物理数据换算明确为

$$
C_{2j}(r_N)=r_N^4\zeta_Ne^{-2j\tau_0}(-1)^{jN}z_j,
$$

$$C_{2j}'=r_N^3\{(2j)^2Q_{2j}+\sqrt{12}\xi_{2j}\}.$$

因此这是真正的有限维 **low-height-to-full-trace** 图：给定前46高度，输出它们的全部斜率，以及47起的完整两分量、完整 mean 梯度。由于线性 map 不耦合角频，高于46的 trace 一阶为0，实际从二阶开始。

**不能把高于46的高度强行置0而仍称作同一精确图。** 当前有限求解器若只给每个保留模一个 Robin 条件，还需比较其未表示高模和这里的真实 trace 图；本文没有替它们签署一致性证明。

## 9. 从深 trace 到浅 cut 的接口

固定任意有限个正 slope 胞元/有限改造头，先固定足够的输入角宽 $\tau_0$。完整 Cauchy 方程在零解附近给有限头的解析传播 $\mathcal P_{N\to c}$，其余量和允许球须按该头的实际参数计算。于是

$$\Gamma_c(z)=\mathcal P_{N\to c}\Gamma_N(z)\tag{9.1}$$

是精确浅 cut trace。在线性级，每个模独立，且完整 $2\times2$ 传递矩阵可逆；因此来自一个非零深端方向的浅端二维列不可能同时为零。

可执行选择是：每个自由模取浅端高度或 canonical momentum 中较不退化的一个作为输入坐标；这46个混合坐标的 Jacobian 在零处为可逆对角矩阵。小球上的反函数定理给真实混合端口图。若要全部使用高度坐标，就必须另验证每个线性高度传递因子非零，而不能只查看有限值的 quotient。

实际前缀应该解完整方程

$$U_c^{\rm prefix}(p)-\Gamma_c(z)=0,$$

包含所有保留模的两分量、受控未表示高模，以及完整 mean 导数。常数高度只调一次平移。若两片确实同 $g$ 且完整高度两 jet 相容，本题 R10 才把它提升为 Cartesian 两 jet 接缝。

这里把未知边界收束为可计算的46参数图，并给了精确的深部模型、线性误差门及 R17 的具体非线性深起点；**尚未算出当前强前缀所需的非线性图值，也未证明目标幅度位于其允许球内。** 这两项应继续由真实延拓、固定新 $g$ 的加密和全空间几何计算支付。

## 10. 重现与保留的边界

从仓库根运行：

```bash
python topics/visible-flex-larger-amplitude/computations/closure_rational_tail_linear.py \
  --out topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-rational-linear.json
```

程序只核算本稿有限谱、Green 常数及线性深度，不联网、不重算任何数值曲面、不修改旧 metric。以下事项仍未支付：

1. 从可算的 far192/256 到 R17 的具体精确深尾起点 $N=4096$ 的尺度化传播/余项账本；
2. 真实有限头的全频传播预算与强幅 cut 的非线性 trace 匹配；
3. 完整大幅闭图的固定新 $g$ 加密、全时嵌入、连续空间 reach 和 $\delta_{\rm hold}\ge.2D$。

它们不是新的审批门；后续继续实际计算。旧小幅有限闭网格和外倍数容量实验没有因此升级为完成解。
