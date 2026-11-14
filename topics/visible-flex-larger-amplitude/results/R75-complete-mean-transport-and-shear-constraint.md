# R75：完整均值输运、剪切约束与非精确中心的额外项

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

**已证明的条件工具。** 本文证明完整连接均值的真实微分恰是 R69 剪切后第二分量的正权平均，并给出任意有源全变量系统中的精确输运公式。这说明从真实内头接入的完整 mean 可由全变量方程保持；没有新增的独立外端 mean slope 条件。对非精确兼容候选线性化时，一个含实际候选残差的零阶项必须保留。

本文不提供外 $0,\ldots,11$ 的 Green/Schur 逆、解析传播积分或非线性收缩数值。其对象始终是同一个真实背景，不能把某个已付内头的 trace 换成另一个参数或有限保存场的 trace。

## 1. 正则性、完整变量和分支

取有限真实 source 区间 $I=[a,b]$，$r,w\in C^1(I)$，$r,w>0$，$r_x>0$，并定义

$$
s=\frac{r_x}{r},\qquad \ell=\frac{w_x}{w},\qquad
z=w^2,\quad E=1+z.
\tag{75.1}
$$

场 $P,K$ 为实、$2\pi$ 周期函数；$K$ 包含其完整零模。假设 $x$ 导数、下述混合导数和角导数存在且连续，足以逐项使用链式法则及周期分部积分。例如在一个固定正角宽上对角变量解析、对 $x$ 为 $C^1$，且所需解析范数局部一致有界，已经足够。第 4 节调用经典 Darboux/曲率表达式时，另取与 R44 相同的物理半径背景 $w(r)\in C^2$ 及相应 $C^2$ 高度正则性。分段 source 图可以逐段应用，物理 trace 在公共端点一致时按真实坐标拼接。

记

$$
y=1+K,\quad T=P_\theta,\quad U=K_\theta-P,\quad
S=1-zP^2,\quad D=ES-zy^2,
$$

$$
L=y+ET,\qquad
N=1+\frac{zyT}{S},\qquad
\Omega=\frac{N}{\sqrt D}.
\tag{75.2}
$$

保持 [R44](R44-compatible-outer-height-and-continuous-defect.md)、[R64](R64-general-outer-mean-and-compatible-defect.md) 的同一实正支：$S,D,y,N,L>0$。解析算子估计仍须另付其条带分母门，实角正性不是该门的替代。

完整连接均值定义为

$$
\mathcal M(Y;x)=\frac{\langle\Omega\rangle-1}{z},
\qquad Y=(P,K),
\tag{75.3}
$$

角平均为 $(2\pi)^{-1}\int_0^{2\pi}$。实际小 $w$ 算术可使用 R44.12 的无相减级数；式 (75.3) 用于精确恒等式。这里 $z>0$，未通过除以浮点极小数定义另一个方程。

## 2. 完整 mean 的微分就是剪切后的正权平均

置

$$
W=\frac{L}{D^{3/2}},\qquad
\alpha=\frac{EU}{L},\qquad
\mathscr S=\begin{pmatrix}1&0\\-\alpha&1\end{pmatrix}.
\tag{75.4}
$$

这里 $\alpha$ 是 R69 中记作 $a$ 的剪切系数；没有把 source 系数 $s\alpha$ 与它混用。

**定理 75.1。** 固定真实 $x$，对任意周期变化量 $X=(p,k)^t$，完整 Fréchet 微分为

$$
\boxed{
D_Y\mathcal M[X]
=\left\langle\frac{Lk-EU p}{D^{3/2}}\right\rangle
=\langle W(\mathscr S X)_2\rangle .}
\tag{75.5}
$$

**证明。** 将 $P,K,T$ 暂作为三个独立变量，R44 的逐项求导给

$$
\Omega_K=\frac{zL}{D^{3/2}},\quad
\Omega_T=\frac{zy}{S\sqrt D},\quad
\frac{\Omega_P}{z}=\frac{EP N}{D^{3/2}}
+\frac{2zyTP}{S^2\sqrt D}.
\tag{75.6}
$$

真实变化满足 $\delta T=p_\theta$。周期分部积分后

$$
D_Y\mathcal M[X]
=\left\langle Wk+
\left(\frac{\Omega_P}{z}
-\partial_\theta\frac{y}{S\sqrt D}\right)p\right\rangle.
\tag{75.7}
$$

直接求导，使用 $S_\theta=-2zPT$、$D_\theta=-2z(yK_\theta+EPT)$，得

$$
\partial_\theta\frac{y}{S\sqrt D}
=\frac{K_\theta}{S\sqrt D}
+\frac{2zyPT}{S^2\sqrt D}
+\frac{zy(yK_\theta+EPT)}{S D^{3/2}}.
$$

与 (75.6) 相减后，中间两项消去，其余通分的分子为

$$
EP(S+zyT)-K_\theta D-zy^2K_\theta-zyEPT
=ES(P-K_\theta).
$$

这里用了 $D+zy^2=ES$。因此括号恰为 $-EU/D^{3/2}$，得到 (75.5)。所有分部积分均是完整周期积分，不是有限角采样。证毕。

特别地，若 $K=c+\bar K$ 且 $\langle\bar K\rangle=0$，给定变化 $(p,\bar k)$ 后同一完整根的零模变化唯一为

$$
\delta c=-\frac{\langle W\bar k-EU D^{-3/2}p\rangle}
{\langle W\rangle}.
\tag{75.8}
$$

分母是原来的 $M_c>0$。这没有删掉均值导数；它把该导数写成与 R69 剪切完全一致的形式。式中没有隐藏的 $1/w$ 因子。

## 3. 任意完整有源系统中的精确输运

采用 R69 的完整有理源

$$
\mathcal N(Y)=
\frac{EsU^2+\ell\bigl((K+T)^2+z(2KT+T^2-P^2)\bigr)}{L}.
\tag{75.9}
$$

令实际两行残差为

$$
f_P=P_x-sK_\theta+(s+\ell)P,
\qquad
f_K=K_x+\ell(2K+T)-\mathcal N(Y).
\tag{75.10}
$$

对已知候选，所有左侧径向导数都取其实际导数。不得用右端重新定义它们而把缺陷置零。

**定理 75.2。** 在第 1 节假设下，

$$
\boxed{
\mathcal M_x+2\ell\mathcal M
=\langle W(f_K-\alpha f_P)\rangle
=\langle W(\mathscr S f)_2\rangle .}
\tag{75.11}
$$

等价地，

$$
\partial_x(z\mathcal M)=z\langle W(\mathscr S f)_2\rangle.
\tag{75.12}
$$

**证明。** R44.34 的完整连接 curl 恒等式是

$$
\Omega_x-\partial_\theta\mathcal A_x
=zW f_K+\Omega_T\partial_\theta f_P+\Omega_P f_P,
$$

其中 $\mathcal A_x=szyU/(S\sqrt D)$。对完整角度取平均，周期导数项消去。再对 $f_P$ 项周期分部积分，(75.7) 中已经逐项证明的恒等式给

$$
\partial_x\langle\Omega\rangle
=z\langle W f_K-EU D^{-3/2}f_P\rangle.
$$

用 $\langle\Omega\rangle=1+z\mathcal M$ 和 $z_x=2\ell z$，即为结论。证毕。

因而在任意 $a\le x\le b$，有准确有源式

$$
\mathcal M(x)=\frac{z(a)}{z(x)}\mathcal M(a)
+\frac1{z(x)}\int_a^x z(t)
\langle W(t)(\mathscr S(t)f(t))_2\rangle\,dt.
\tag{75.13}
$$

这只是恒等式。若将它用于误差范数，须保留真实 $z(t)/z(x)$；没有从零源保持结论免费推出某个有源算子范数。

## 4. 从一个真实内端保持完整 mean 及高度

**推论 75.3。** 假设一个完整全频解满足 $f_P=f_K=0$，其真实内端 trace 有 $\langle P(a)\rangle=0$、$\mathcal M(Y(a);a)=0$。则整个区间上

$$
\langle P(x)\rangle=0,\qquad \mathcal M(Y(x);x)=0.
\tag{75.14}
$$

若同时保持 R64 指定的可容许分支区间，则其 $K$ 零模就是同一个完整 mean 根，不是另加的自由量。

**证明。** 第一行取平均给
$\partial_x\langle P\rangle=-(s+\ell)\langle P\rangle$，其零初值解唯一为零。式 (75.12) 给 $z\mathcal M$ 为常数，零初值遂恒为零。R64 的严格单调性给指定分支内的根唯一性。证毕。

令 $\partial_\theta^{-1}$ 是零均值周期函数上的逆角导数。定义

$$
h_\perp=rw\,\partial_\theta^{-1}P,
\qquad
(h_0)_x=r_xw(1+\langle K\rangle).
\tag{75.15}
$$

第一行方程准确给

$$
(h_\perp)_x=r_xw(K-\langle K\rangle),
\qquad h_\theta=rwP,\qquad h_r=w(1+K).
$$

因此 $h=h_0+h_\perp$ 是同一兼容高度，$f_K=0$ 经 R44 的真实 Darboux 恒等式给完整 Darboux 方程。$h_0$ 只有一个全区间积分常数。若原问题没有固定 cuff 的绝对竖直位置，可按 R61 的单一平移约定匹配该常数；不能逐胞元另选常数，也不能在已经指定双端均值高度的构造里省去其积分条件。

本推论只适用于全部真实频率。有限 Galerkin 投影一般不保持 (75.11)，除非其遗漏量已经明确纳入 $f$；有限存储的 mean 或数值 turn 不被当成 (75.14) 的精确输入。

## 5. 非精确中心的线性化：不能遗漏残差项

记完整向量场为 $Y_x=\mathcal F(Y)$。让 $\widehat Y$ 是一个兼容的完整 mean 候选，满足

$$
\widehat Y_x-\mathcal F(\widehat Y)
=(0,\widehat R_K),\qquad \mathcal M(\widehat Y;x)=0.
\tag{75.16}
$$

一般 $\widehat R_K\ne0$，即使它的正权平均为零。对完整变化量 $X=(p,k)$，设

$$
X_x=D\mathcal F(\widehat Y)X+g,
\qquad q=D\mathcal M(\widehat Y)[X].
$$

**定理 75.4。** 线性化后的准确 mean 输运为

$$
\boxed{
q_x+2\ell q
=\langle\widehat W(g_K-\widehat\alpha g_P)\rangle
+\langle D W(\widehat Y)[X],\widehat R_K\rangle .}
\tag{75.17}
$$

其中

$$
DW[X]=\frac{k+Ep_\theta}{D^{3/2}}
+\frac{3zL\bigl((1+K)k+EPp\bigr)}{D^{5/2}}
\tag{75.18}
$$

在 $\widehat Y$ 处求值。

**证明。** 将 (75.11) 应用于 $Y_\varepsilon=\widehat Y+\varepsilon X$。其残差为
$(0,\widehat R_K)+\varepsilon g+O(\varepsilon^2)$。对 $\varepsilon$ 在零点求导，第一残差的中心值为零，所以只留下权 $W$ 对第二中心残差的变化项，即 (75.17)。由 $\delta L=k+Ep_\theta$、$\delta D=-2z((1+K)k+EPp)$ 直接求导 $W=LD^{-3/2}$ 得 (75.18)。证毕。

若中心不兼容，还须另加
$\langle D(-\alpha W)[X],\widehat R_P\rangle$，不能使用 (75.17) 省去它。

在精确中心 $\widehat R_K=0$ 时，齐次线性方程确实保持零 mean 切约束 $q(a)=0$。在非精确中心，即使 $g=0$，最后一项仍可能非零。因此不能将逐点的 mean 切空间直接当成该候选线性流保持的子空间。R69 在包含完整零模的空间上估计是合法的，但若将它缩到消去均值的变量，必须支付 (75.17) 或等价的隐式根导数项。

## 6. 外侧接合时的作用与仍需支付的量

真实内头的完整 trace 给出的 mean 条件已经是 (75.14) 的初值；全变量外方程的精确解将保持它。这样可以在较大、包含零模的解析空间构造外侧解，而不人为增加一个独立的外端 mean slope Dirichlet 条件。最终固定点必须满足原全频方程与真内端 trace；中间线性迭代不要求误认为已经满足完整 mean 根。

外侧的实际 Green/Schur 逆、R69 的完整系数积分、非线性邻域、全部有限/无限频率边界匹配、分支保持和 mean 高度积分仍须核算。特别是 R72 的已付内头参数域不能代替这些外侧量。本文将 mean 的逻辑接线及其额外线性化项写清，没有把任何未支付的算子界记为通过。
