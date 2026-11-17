# R626 — 有限角均值的微分延拓与完整零模边值系统

作者：parallel-model / GPT-6 Astra Pro，AI-assisted。日期：2026-11-17。

**状态：下述有限维方程、约束保持、边界计数和标量误差式均已证明；尚未声称有新的非零闭曲面。** 本文为 `parallel-numerical` 的互补尾求解提供可实现的变量选择。未运行原有限尾 BVP，也未变更既有 source、full112 worker、Actions 或同一度量的加密链。

已有 [R64](../results/R64-general-outer-mean-and-compatible-defect.md)、[R69](../results/R69-complete-mean-principal-symbol-and-analytic-frame.md)、[R75](../results/R75-complete-mean-transport-and-shear-constraint.md) 给出完整均值根、全变量 PDE 和真实均值输运；[R77](../results/R77-complete-mean-defect-zero-mode.md) 及 [R232](../results/R232-complete-mean-double-rank-Hermitian-energy.md) 处理真实均值约束下的缺陷及消元。本文不重报这些恒等式。新增点是：对**实际有限角求积的字面函数**直接微分，得到保持同一有限均值约束的显式零模 ODE，选择其离开约束面后的延拓消除 $w^2$ 条件数，并给出与有限隐式根模型的准确等价关系。

## 1. 变量和实际有限角模型

在一个有限 source 区间 $I=[x_d,x_c]$，使用原来的正背景

$$
s=r_x/r,\quad \ell=w_x/w,\quad z=w^2>0,\quad E=1+z.
$$

$x_d$ 表示较深、靠近平 cuff 的 cut，$x_c$ 表示与浅部数据接合的 cut；以下结论不要求 $w$ 在两端间单调。保留同一 R64 实正分支。取整数 $M\ge1$，用

$$
P=\sum_{j=1}^M p_j\sin(2j\theta),\qquad
K=c+\bar K=c+\sum_{j=1}^M k_j\cos(2j\theta).
\tag{1.1}
$$

完整状态有 $2M+1$ 个实分量。$D_\theta$ 始终是对 (1.1) 的系数准确求导。令

$$
Q_n f=\frac1n\sum_{a=0}^{n-1}f(2\pi a/n),\qquad n>4M,
$$

并令 $\Pi_{M,n}$ 为该求积内积下到偶三角空间 $\{1,\cos2\theta,\ldots,\cos2M\theta\}$ 的正交投影。因此 $Q_n\bar K=Q_nD_\theta P=0$，且投影保留所采样函数的均值。若实现用 $\pi$ 周期及角变量 $\varphi=2\theta$，只需一致换算频率与节点；本文固定上述 $2\pi$ 约定。

记

$$
y=1+K,\quad T=D_\theta P,\quad U=D_\theta K-P,
$$
$$
A=2K+K^2+EP^2,\quad S=1-zP^2,
\quad D=1-zA,\quad q=\sqrt D,
$$
$$
L=y+ET,\qquad N=1+zyT/S.
\tag{1.2}
$$

以下有限均值及其速度的局部公式只需节点上 $S,D,L>0$；要与几何正分支连接，仍须保持原来的全部 $S,D,y,N,L>0$ 和所需连续角界。节点正性不冒充全角正性。

原始、尚未校正零模的有限向量场为

$$
F_P=sD_\theta K-(s+\ell)P,
$$
$$
F_K^0=-\ell(2K+T)+\Pi_{M,n}\mathcal N(P,K),
\tag{1.3}
$$

其中 $\mathcal N$ 是 R69 的完整有理表达式

$$
\mathcal N=
\frac{EsU^2+\ell\{(K+T)^2+z(2KT+T^2-P^2)\}}L.
$$

这里的有理函数在角节点上实际求值，再按指定投影输出；没有把它换成低阶振幅展开。置

$$
\bar F_K=F_K^0-Q_nF_K^0.
\tag{1.4}
$$

## 2. 小 $z$ 时无相减的字面均值及全部偏导

用稳定函数

$$
B(P,K,T,z)=\frac{A}{q(1+q)}+\frac{yT}{Sq},
\qquad m_n(P,K;x)=Q_nB.
\tag{2.1}
$$

它准确等于每个节点上的 $(N/\sqrt D-1)/z$，因为
$1-q=zA/(1+q)$。因此 $m_n$ 就是有限角连接均值；不需从两个接近1的数相减，再除以很小的 $z$。

在以下偏导中暂将 $P,K,T,z$ 当成独立变量，有

$$
B_K=\frac L{q^3},\qquad
B_T=\frac y{Sq},\qquad
B_P=\frac{EP N}{q^3}+\frac{2zyTP}{S^2q},
\tag{2.2}
$$

$$
\begin{split}
B_z={}&\frac{P^2}{q(1+q)}
 +\frac{A(A+zP^2)(1+2q)}{2q^3(1+q)^2}\\
&+yT\left\{\frac{A+zP^2}{2Sq^3}
                    +\frac{P^2}{S^2q}\right\}.
\end{split}
\tag{2.3}
$$

**证明。** $A_z=P^2$，$D_z=-(A+zP^2)$，$S_z=-P^2$，而
$\partial_u\{[\sqrt{1-u}(1+\sqrt{1-u})]^{-1}\}=(1+2\sqrt{1-u})/[2(1-u)^{3/2}(1+\sqrt{1-u})^2]$。对 (2.1) 普通求导并通分，得到四式。式 (2.2) 也可由 $B=(N/\sqrt D-1)/z$ 直接求导验证；这里没有对离散角导数使用乘积法则或链式法则。证毕。

特别地，零模导数为

$$
\mu_n=\partial_c m_n=Q_n B_K>0.
\tag{2.4}
$$

它没有 $z^{-1}$ 因子。在任一保持正分支的 $c$ 区间内，$m_n$ 对 $c$ 严格递增；存在性与根区间仍须实际给出，不能仅由导数正性推出根已存在。

## 3. 只改变零模速度的显式 ODE

选择任意预先指定的实函数 $\chi(x)$；它不依赖未知场。定义

$$
c_x=-\frac{2\ell z Q_nB_z+
 Q_n\{B_PF_P+B_K\bar F_K+B_TD_\theta F_P\}
 +\chi m_n}{\mu_n},
\tag{3.1}
$$

并解完整有限系统

$$
P_x=F_P,\qquad \bar K_x=\bar F_K,\qquad c_x\text{ 由 (3.1) 给出}.
\tag{3.2}
$$

**定理。** 在该系统存在且分支保持的区间上，字面有限均值准确满足

$$
(m_n)_x+\chi m_n=0.
\tag{3.3}
$$

因此在任一端点施加一次 $m_n=0$，便有整个区间 $m_n=0$；不需要每个 RHS/stage 再解标量根。

**证明。** 对有限和 (2.1) 逐项使用普通多变量链式法则，$T_x=D_\theta F_P$ 且 $z_x=2\ell z$，故

$$
(m_n)_x=2\ell zQ_n B_z+
Q_n\{B_PF_P+B_K(\bar F_K+c_x)+B_TD_\theta F_P\}.
$$

代入 (3.1)、(2.4) 就得到 (3.3)。这一步既不声称有限 $D_\theta$ 对非线性点值满足链式法则，也不照搬 R75 中只对完整角积分成立的分部积分式。证毕。

若希望从 (1.3) 只改一个速度，可等价写

$$
F_K=F_K^0+\eta_n,\qquad
\eta_n=c_x-Q_nF_K^0.
\tag{3.4}
$$

其中 $\eta_n$ 对角度为常数。完整系数 Jacobian 是原有限 Jacobian 加一个秩至多1的项 $e_cD_Y\eta_n$；没有改变非均值方程。

### 推荐的离约束面延拓

推荐取 **$\chi=0$**。此时字面均值的误差既不随 $w^2$ 放大，也不随 $w^2$ 缩小，而是常数。取 $\chi=2\ell$ 会得到字面模拟 R75 的输运，但其离约束面误差带有 $z(x_0)/z(x)$ 因子。两种选择在 $m_n=0$ 面上给出**同一个**速度，因为差别恰是 $-\chi m_n/\mu_n$。

这不是删除原 PDE 的约束：它选择有限方程在约束面以外怎样延拓，最终边值解仍强制在原有限约束面上。原 PDE 的真实残差必须包含 (3.4) 中的 $\eta_n$，见第7节。

### 直接计算零模速度，避免额外的大数相消

因为 $Q_n\bar F_K=Q_nD_\theta F_P=0$，可把 (3.1) 实现成

$$
c_x=-\frac{2\ell z Q_nB_z+
Q_n\{B_PF_P+(B_K-1)\bar F_K+(B_T-1)D_\theta F_P\}
 +\chi m_n}{\mu_n}.
\tag{3.5}
$$

其中两个差值也有无相减公式。令

$$
C_3=\frac{1+q+q^2}{q^3(1+q)},
$$

则

$$
B_K-1=K+ET+zLAC_3,
\tag{3.6}
$$

$$
B_T-1=K+\frac{zy}{Sq}
            \left\{\frac A{1+q}+P^2q\right\},
\tag{3.7}
$$

$$
\mu_n=1+c+zQ_n(LAC_3).
\tag{3.8}
$$

式 (3.6) 用 $(q^{-3}-1)/z=AC_3$；式 (3.7) 用 $1-Sq=zA/(1+q)+zP^2q$。最后 $Q_nT=Q_n\bar K=0$ 给 (3.8)。实现可优先用 (3.5) 直接写第0模，事后才计算 $\eta_n$ 作缺陷记录。所有分母都仍是原正分支的分母。

## 4. 与隐式有限根模型准确等价，但没有增加物理自由度

设一个局部场域内，方程 $m_n(P,c+\bar K;x)=0$ 有同一正分支的唯一根
$c=c_n(P,\bar K;x)$。由 (2.4)，该根可微。考虑原有限隐式根模型

$$
P_x=F_P(P,c_n+\bar K),\qquad
\bar K_x=\bar F_K(P,c_n+\bar K).
\tag{4.1}
$$

沿任一解对 $m_n=0$ 求导，正好得到 (3.1) 的 $\chi m_n=0$ 版本，所以其完整 lift 满足 (3.2)。反过来，满足 (3.2) 且一端 $m_n=0$ 的解由 (3.3) 处处在该约束面上，由根唯一性必有 $c=c_n$，于是其非均值部分满足 (4.1)。因此两者在指定根域内准确等价。

这样增加的一个 ODE 状态，只替代了原标量代数消元；它没有增加可任意调整的几何参数。省略边界 $m_n=0$ 会留下一个真实的标量积分常数。在原完整 PDE 中相应常数是 R75 的 $z\mathcal M$；在推荐有限延拓中是 $m_n$。两者都必须以一个周期/均值条件固定为零。

该等价只针对**同一个 $m_n$、同一角投影、同一 source、同一分支**。不能由此把不同求积、完整角根或别的 worker 的状态协议自动认作相同的有限问题。

## 5. 一个方正的低阶边值接口

对拟测试的 $M=8,16,32$ 等有限模型，可以使用以下 $2M+1$ 个标量边界式：

1. 在浅 cut $x_c$，指定 $M$ 个非均值物理高度；若高度系数为 $H_j$，则
   $p_j(x_c)=-2jH_j/[r(x_c)w(x_c)]$。
2. 在深 cut $x_d$，使用同一 source 的 $M$ 个已明确声明的有限稳定图/Robin 关系。
3. 在一个端点再施加一个 $m_n=0$；推荐 $\chi=0$ 时放在拥有真实输入数据的浅 cut。

由 $h_\theta=rwP$，第一项换算准确；相应非均值径向斜率为 $h'_j=wk_j$。深图若写成 $h'_j=\beta_jh_j$，则其第 $j$ 行为
$k_j+\beta_jr p_j/(2j)=0$。非线性图应直接用其真实函数，不能用这个线性示例冒称全非线性图。

边界行数方正只是有限问题的计数，不保证非均值边界 Jacobian 可逆，也不证明所用有限图等于准确无限尾。特别是 R15/R18 给出的46参数全频图不能被一个任意每模 Robin 条件替代；超过该有限 chart 的频率必须保留那些结果中原有的含高模 trace 语义。本条没有签署新深图或 full112 闭合。

在分段 source 或多重射击中，公共端点只连续匹配完整 $P,K$。同一 $m_n$ 随状态与真实 $z$ 连续，且每段都满足 (3.3)，所以**不需在每个胞元再加独立的 mean 边界行或重设零模**。

### 高度常数另计一次

均值高度由

$$
(h_0)_x=r_xw(1+c)
\tag{5.1}
$$

统一积分。若把 $h_0$ 加入状态，总维数成为 $2M+2$，同时只需一个绝对高度规范。若两个端点的绝对均值高度都已被物理构造固定，第二个高度条件是实际积分匹配式，需要相应自由参数或另一个待匹配未知量；不能把它算成免费的平移。没有双端固定高度的任务则不添加这个条件。

## 6. 零模边界位置和求解残差的稳定性

### 原始动态零模的方向问题

直接使用未经修正的完整 PDE 时，R75 给出的标量缺陷传播包含

$$
\mathcal M(x)=\frac{z(x_0)}{z(x)}\mathcal M(x_0)
 +\frac1{z(x)}\int_{x_0}^x z(t)G(t)\,dt,
\tag{6.1}
$$

其中 $G$ 是真实加权残差。若从浅处把均值误差传到深处，小 $z$ 可显著放大它；选深端的零均值边界能消除相应齐次大因子，但不能消除振荡胞元内部的 $z(t)/z(x)$。不能只由端口包络递减就忽略深谷。用 $z\mathcal M$ 作观测量可以稳定观测通量，但再转回零模根仍须除以 $z$。

推荐延拓 $\chi=0$ 避免了这个纯标量条件数。若 $\widehat Y$ 是实际数值候选，定义相对于 (3.2) 的完整系数残差为 $R=\widehat Y_x-F^{\rm corr}(\widehat Y)$，包括其零模。逐字微分给

$$
\frac d{dx}m_n(\widehat Y;x)+\chi m_n(\widehat Y;x)
=D_Ym_n(\widehat Y;x)[R].
\tag{6.2}
$$

因此 $\chi=0$ 时，对任一选定端点 $x_0$，

$$
|m_n(x)|\le |m_n(x_0)|+
\int_{[x_0,x]}|D_Ym_n[R](t)|\,|dt|.
\tag{6.3}
$$

这没有 $w(x_0)^2/w(x)^2$。若 $R_K=R_c+R_{\bar K}$ 且其非均值部分实际均值为零，则

$$
\begin{split}
D_Ym_n[R]={}&\mu_nR_c\\
&+Q_n\{B_PR_P+(B_K-1)R_{\bar K}
                    +(B_T-1)D_\theta R_P\}.
\end{split}
\tag{6.4}
$$

所以只需同一候选的系数与实际残差便能得到标量缺陷界。有限 Fourier $\ell^1$ 范数下，$\|D_\theta R_P\|_\infty\le2M\|R_P\|_{\ell^1}$；也可以直接保留导数残差，不引入这个粗因子。

若同一 $c$ 区间内 $\mu_n\ge\mu_->0$，当前值与该区间内准确有限根 $c_*$ 满足中值定理界

$$
|c-c_*|\le |m_n|/\mu_-.
\tag{6.5}
$$

根的存在及两值间区间的分支仍是这个结论的条件。由 (6.3)–(6.5)，均值残差转成零模状态误差的成本由 $\mu_-^{-1}$ 控制，而不是 $z^{-1}$。

沿准确的修正轨道线性化，若 $q_m=D_Ym_n[\delta Y]$，则 $q_{m,x}+\chi q_m=0$。在局部坐标 $(P,\bar K,m_n)$ 中，标量法向方程独立，非均值方程可以受 $m_n$ 强迫。这给出法向块的稳定性，**不**给非均值 BVP 的全局逆或 Newton 收敛率。

## 7. 保持有限均值不等于消除了连续截断误差

把实际有限场重建成全角三角多项式后，其相对于原 R69 PDE 的连续残差是

$$
f_P=0,\qquad
f_K=\Pi_{M,n}\mathcal N-\mathcal N+\eta_n,
\tag{7.1}
$$

如果径向候选本身尚有求解残差，还须逐分量加上那个实际残差。第一项 $\Pi_{M,n}\mathcal N-\mathcal N$ 含真实保留频率外的尾及角混叠；最后一项是第0模速度修正，不能从原 PDE 缺陷中删除。

即使 $m_n=0$ 准确保持，完整均值 $\mathcal M=\langle B\rangle$ 也只满足

$$
|\mathcal M|\le |\langle B\rangle-Q_nB|.
\tag{7.2}
$$

若 $B(\theta)=\sum_{k\in\mathbb Z}B_ke^{ik\theta}$ 绝对收敛，等距求积的准确别名式为

$$
Q_nB-\langle B\rangle=\sum_{l\ne0}B_{ln}.
\tag{7.3}
$$

因此，若同一候选已控制加权 Wiener 范数
$\|B\|_\sigma=\sum_ke^{\sigma|k|}|B_k|$，则

$$
|Q_nB-\langle B\rangle|\le e^{-\sigma n}\|B\|_\sigma.
\tag{7.4}
$$

该范数需包括原有理分母产生的完整频率；固定少量节点的点值比较不是这个上界的证明。实际加密可以同时提高 $M,n$，保留相同 source、参数与边界输入，分别检查实际 $\eta_n$、全角非均值缺陷、求积差、分支余量和几何量。式 (6.3) 只解释均值求解误差，不替代这些连续缺陷。

### 完整角投影时的一个有用公式

为理解修正的大小，暂把 $Q_n$ 换成准确角积分，把投影换成准确 Fourier 投影 $\Pi_M$，并限制在 $\mathcal M=0$。R75 直接给

$$
\eta=\frac{\langle W(I-\Pi_M)\mathcal N\rangle}{\langle W\rangle},
\qquad W=L D^{-3/2}.
\tag{7.5}
$$

因为 $L\in\operatorname{range}\Pi_M$，正交性及 $W=L+zLAC_3$ 进一步给

$$
\eta=\frac{z\langle LAC_3(I-\Pi_M)\mathcal N\rangle}{\langle W\rangle}.
\tag{7.6}
$$

也有

$$
|\eta|\le
\frac{\|(I-\Pi_M)W\|_{L^2}
      \|(I-\Pi_M)\mathcal N\|_{L^2}}{\langle W\rangle},
\tag{7.7}
$$

其中 $L^2$ 采用归一角平均。式 (7.6) 保留小 $z$ 因子，(7.7) 保留两个真正的高频尾；两式都比直接用 $\|W\|\|(I-\Pi_M)\mathcal N\|$ 更能解释小振幅深段的行为。

这些是完整角投影的精确式，**不能未经求积/混叠分析直接用作有限 $Q_n$ 的零模速度**。有限实现必须使用第3节的字面导数式；它不需要这些附加假设。

## 8. 可实施的最小入口与本条边界

一次 RHS 调用只需：重建 $P,K$ 及谱导数；计算同一有理 $\mathcal N$ 与其有限投影；计算 (2.1)–(2.3)、(3.6)–(3.8) 的节点值；用 (3.5) 输出 $c_x$。相对于原全变量 RHS，这增加有限次逐节点运算及求和，没有嵌套的标量 Newton。边界只调用一次字面 $m_n$ 条件。

以上四个偏导与两条差值公式已用符号代数独立通分核对为零；这是公式验证，不是尾 BVP 的运行结果。`parallel-numerical` 已收到可实现的全部表达式，拟在独立的低阶真实源实验中验证后再讨论接入。

本条到此支付的是：**有限角完整零模的显式延拓、其与同一隐式根模型的等价、一个方正有限边界接口、无 $w^2$ 放大的标量误差传播，以及连续截断缺陷的准确记录方式。** 原非零无限尾接合、完整闭面、所有参数的 reach/$\delta_{hold}$ 和同一 $g$ 加密仍按题 README 的原标准处理。
