# R119 续篇：真实一阶尾框架及不含径向系数导数的可求和余项

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对同一完整非线性尾、已安装 connector 和固定双
bump，在新 $\ell^1_{224}$ 标签球上，完整 raw Jacobi 系统可准确写成
$$
 Y_t=\nu
 \begin{pmatrix}0&1\\-A&0\end{pmatrix}Y_\eta+
 \left[
 \begin{pmatrix}-A-1&0\\0&-2A\end{pmatrix}
 +\mathcal R\right]Y+\widehat e .
 \tag{F.1}
$$
真实角图、倍率 $\nu$、普通 scalar Darboux 源和 mean 行均保留。
所有层连同有限 connector 及双 bump 的准确余项满足
$$
 \int\|\mathcal R(t)\|_{\mathcal A_2}\,dt
 <2^{-426}X_{224},\qquad
 X_{224}=\|X^{[224]}(a)\|_{\mathcal X}<1.
 \tag{F.2}
$$
证明完全不引入 $A_t$ 或 $A_{tt}$；它适用于真实 log-quintic 型别
过渡及无限平尾极限。这里没有把 $\nu$ 换成1，也没有由 (F.2) 宣称
得到相对全频 return 逆。实际射线相位仍是后者的独立内容。

## 1. 实际域、共用角宽与物理 source 单位

采用 [权224完整延拓](R119-supplement-balanced-connector-label-domain-224.md)
的同一标签球 $\|a\|_{\ell^1_{224}}<1/4$。用从平尾累积圆向外的
$t=\log a+\text{常数}$，参考几何 $A=aw_a/w,E=1+w^2$ 固定。
内部全部高标签及实际两个 bump 参数保持不变。

在完整无限尾，已有
[真角图续篇 (A.13)](R119-supplement-actual-tail-angle-density-conjugation.md)
给每层的完整四态界
$$
 N_j\le2^{64}\delta_j^{443/256}\|X\|_{\mathcal X},
 \qquad \delta_j=(2/25)2^{-j},\qquad j>128.
 \tag{F.3}
$$
它在角宽 $\tau-1>11$ 上成立。完整 connector 加双 bump 则在
全程大于 $5.296$ 的实际角宽上有
$$
 N<2^{-447}X_{224}.
 \tag{F.4}
$$
所以全区间共同的宽4、3、2均已有支付。这里 $N$ 包含 mean $K_0$。

非mean 强状态的准确去权关系给
$$
 \|X\|_{\mathcal X}\le e^{-4\beta}X_\beta,\qquad \beta=224.
 \tag{F.5}
$$
不能对 mean 直接作这个线性去权；(F.3) 中的完整 mean 已由同一
holonomy 小根的二次估计支付，故 (F.3)、(F.5) 的组合是合法的。

相对状态仍为 $P=v_\theta/(aw),K=v_a/w,U=P_\theta,V=K_\theta$。
本篇普通源 $e$ 的单位准确定义为
$$
\begin{aligned}
 \dot P_t&=\dot K_\theta-(A+1)\dot P,\\
 \dot K_t&=F_P\dot P+F_K\dot K+F_U\dot P_\theta+
                                     F_V\dot K_\theta+e .
\end{aligned}
 \tag{F.6}
$$
它是连续的 scalar Darboux 体源，不是一个端口跳量。
本篇不声称任意 R37 三分量 metric-source 已免费转换成该单位。
同一 exact 背景的高标签微分对应 $e=0$。

## 2. 准确一阶框架，不作标量消元

令
$$
 J=1+K+EU,\quad Q=V-P,\quad
 D=1-w^2(2K+K^2+EP^2),\quad
 d=\frac{EQ}{J},\quad v=\frac{\sqrt D}{J}.
$$
这里 $v$ 是 principal 倍率，不是上节高度扰动；其角色由公式区分。
完整真商式给
$$
 \mathsf B=\begin{pmatrix}0&1\\-Av^2-d^2&2d\end{pmatrix},
 \quad
 \mathsf C=\begin{pmatrix}-A-1&0\\F_P&F_K\end{pmatrix},
 \quad
 \mathsf T=\begin{pmatrix}1&0\\d&v\end{pmatrix}.
 \tag{F.7}
$$
故 $\dot W=(\dot P,\dot K)^T$ 满足
$\dot W_t=\mathsf B\dot W_\theta+\mathsf C\dot W+(0,e)^T$。
置 $Z=\mathsf T^{-1}\dot W$，准确得到
$$
 Z_t=(dI+v\mathsf B_0)Z_\theta+\mathsf Z Z+
                      \begin{pmatrix}0\\e/v\end{pmatrix},
 \qquad
 \mathsf B_0=\begin{pmatrix}0&1\\-A&0\end{pmatrix},
 \tag{F.8}
$$
$$
 \mathsf Z=\mathsf T^{-1}
       (\mathsf B\mathsf T_\theta+\mathsf C\mathsf T-\mathsf T_t).
 \tag{F.9}
$$
所有 $A=0$ 点都合法，因为 $\mathsf T$ 的逆只除以 $v$。

为明示被保留的项，(F.9) 的完整矩阵是
$$
 \mathsf Z=
 \begin{pmatrix}
 d_\theta-A-1&v_\theta\\[2pt]
 \dfrac{d d_\theta+F_P+dF_K-d_t+d(A+1)}{v}
 &
 F_K+\dfrac{d v_\theta-v_t}{v}
 \end{pmatrix}.
 \tag{F.10}
$$
原点处 $d=0,v=1$，所以
$\mathsf Z=\mathsf C_0:=\operatorname{diag}(-A-1,-2A)$。

使用已由真实完整 PDE 证明的两个恒等式
$$
 (\partial_t-d\partial_\theta)\log v+d_\theta
       =\frac{A(1-v^2)-d^2}{E},
$$
$$
 d_t-d d_\theta-A v v_\theta
       =d\left[-1+\frac{A(w^2-v^2)-d^2}{E}\right].
 \tag{F.11}
$$
于是 (F.10) 只需要 $A$、角导和状态，没有 $A_t$。
在这里先消去一阶系统中的一个未知量，会人为制造系数径向导数；
本篇没有执行这个不必要的操作。

## 3. 对全部实际 $A$ 的零阶余项界

记 $n(t)$ 为宽4上的完整四态和，$n\le1/64$。以下系数在宽3估计。
一个单位 Cauchy 余宽给
$$
 \|d\|,\|d_\theta\|\le3n,\qquad
 \|v-1\|,\|v_\theta\|\le6n,\qquad
 \|\mathsf T-I\|\le9n,\quad
 \|\mathsf T\|,\|\mathsf T^{-1}\|<2.
 \tag{F.12}
$$
矩阵范数取 Wiener 元素的诱导行和。$A$ 是任意实参考值，不要求
尾内 $|A|\le7$；后者只对有限 connector 成立。

写 $F=-A(2K+U)+R$，其中
$$
 R=\frac{G}{J},\quad
 G=E(V-P)^2+A(K^2+2EKU+EU^2-w^2P^2).
$$
对任意 $A$，
$$
 \|G\|\le2(1+|A|)n^2,\quad
 \|G_P\|\le4(1+|A|)n,\quad
 \|G_K\|,\|G_U\|\le4|A|n,\quad
 \|G_V\|\le4n .
$$
由 $J^{-1}<2$ 和完整商法则，
$$
 \|F_P\|\le8(1+|A|)n,\qquad
 \|F_K+2A\|<9(1+|A|)n.
$$
所以可以保守取
$$
 \|\mathsf C-\mathsf C_0\|\le32(1+|A|)n,\qquad
 \|\mathsf B\|\le2(1+|A|),\qquad
 \|\mathsf T_\theta\|\le9n.
 \tag{F.13}
$$

(F.11) 给时间导数的直接完整界。使用
$\|v\|<2$、$\|v^2-1\|\le13n$、$0<w<1$，得到
$$
\begin{aligned}
 \|v_t\|&\le[6+36/64+26|A|]n
                         <27(1+|A|)n,\\
 \|d_t\|&\le[6+9/64+27|A|]n
                         <28(1+|A|)n .
\end{aligned}
$$
因此
$$
 \|\mathsf T_t\|\le64(1+|A|)n.
 \tag{F.14}
$$
从 (F.9) 减去 $\mathsf C_0$，四项依次为
$$
 \mathsf T^{-1}\mathsf B\mathsf T_\theta,\quad
 \mathsf T^{-1}(\mathsf C-\mathsf C_0)\mathsf T,\quad
 \mathsf T^{-1}[\mathsf C_0,\mathsf T],\quad
 -\mathsf T^{-1}\mathsf T_t.
$$
它们的系数分别不超过 $36,128,72,128$ 倍 $(1+|A|)n$。
故有已支付的统一结论
$$
 \boxed{\quad
 \|\mathsf Z-\mathsf C_0\|_{\mathcal A_3}
 \le512(1+|A|)n .
 \quad}                                                     \tag{F.15}
$$
这一步没有使用任何参考径向导数 norm。

## 4. 每个实际 log-quintic 层的完整可积费用

在第 $j$ 层，
$$
 A=-7+(\log p_*)_t,\qquad
 p_*:1,\ 64/\delta_j,\ \delta_j/(65/64),\ 1/\delta_j,\ 64.
$$
四个真实 log-quintic 转接是单调的，三个中间平台及两个端平台的
导数为零。因此完整变差准确为
$$
 \operatorname{Var}(\log p_*)
   =\log64+2\log(65/64)+6|\log\delta_j|
   <2\log128+6|\log\delta_j|.
 \tag{F.16}
$$
所有真实层的对数长度
$\ell_j/\sqrt{12}<2\delta_j$。
由 $\log128<5$、$|\log\delta_j|<j+3$，得到
$$
 \int_{{\rm cell}\ j}(1+|A|)\,dt
 \le8\ell_j/\sqrt{12}+\operatorname{Var}(\log p_*)
 <16\delta_j+6j+28<8(j+4).
 \tag{F.17}
$$
这包括所有上升、下降和端点段，不是只在平台估计 $A=-7$。

令 $\alpha=443/256$。$\delta_{129}<2^{-132}$ 且
$132\alpha>228$，所以 $\delta_{129}^\alpha<2^{-228}$。
同时 $2^{-\alpha}<1/2$，从而
$$
 \sum_{j=129}^{\infty}(j+4)\delta_j^\alpha
 <2^{-228}\sum_{k=0}^{\infty}(133+k)2^{-k}
 =268\,2^{-228}.
 \tag{F.18}
$$
由 (F.3)、(F.5)、(F.17) 得
$$
 \int_{\rm tail}(1+|A|)n\,dt
 <2^{-152}e^{-4\beta}X_\beta .
 \tag{F.19}
$$

完整有限段长度小于132、$|A|\le7$，故
$$
 \int_{\rm finite}(1+|A|)n\,dt
 <8\cdot132\cdot2^{-447}X_\beta
 <2^{-436}X_\beta .
 \tag{F.20}
$$
由于 $\beta=224$、$e>2$，(F.19) 的首项小于
$2^{-1048}X_\beta$。因此全区间
$$
 I:=\int(1+|A|)n\,dt<2^{-435}X_\beta .
 \tag{F.21}
$$
注意参考系数 $\int|A|dt$ 本身可以发散；本篇只对真扰动乘子
$(1+|A|)n$ 作可积结论，没有因此声称径向参考基本解在无权空间有界。

## 5. 真实角流与准确倍率的演化

另一个直接求和给
$$
 I_0:=\int n\,dt
 <2^{-294}e^{-4\beta}X_\beta+2^{-439}X_\beta
 <2^{-438}X_\beta.
 \tag{F.22}
$$
第一项使用
$\sum\delta_j^{\alpha+1}<2\,\delta_{129}^{\alpha+1}<2^{-359}$；
第二项使用有限长度小于132。

从平尾累积圆 $t_f$ 开始解真正的角流
$$
 \phi_t=-d(t,\phi),\qquad\phi(t_f,\eta)=\eta,\qquad j=\phi_\eta.
 \tag{F.23}
$$
这不是形式坐标。若 $\chi=\phi-\mathrm{id}$ 的 $\mathcal A_2$ norm
小于 $1/4$，Wiener 复合不等式
$\|f(\eta+\chi)\|_2\le\|f\|_{2+\|\chi\|_2}$
把所有系数放在已付宽3以内。
积分方程的全时间 Lipschitz 常数不超过 $3I_0<1/2$，故其
Picard 映射在此球内收缩，包括无限平尾端点。并有
$$
 \|\phi-\mathrm{id}\|_{\mathcal A_2}<3I_0<2^{-436}X_\beta,
 \qquad
 \|j-1\|_{\mathcal A_2}<6I_0<2^{-435}X_\beta .
 \tag{F.24}
$$
第二式来自 $j=\exp[-\int d_\theta(t,\phi)dt]$。
实对称标签下这是保持四重反射规范的真实圆周微分同胚。

置
$$
 Y=Z\circ\phi,\qquad
 \nu=\frac{v\circ\phi}{j},\qquad
 \mathcal R=(\mathsf Z-\mathsf C_0)\circ\phi,\qquad
 \widehat e=\begin{pmatrix}0\\(e/v)\circ\phi\end{pmatrix}.
 \tag{F.25}
$$
代入 (F.8) 后漂移准确消去，得到 (F.1)。
(F.15)、(F.21) 和真实复合界立即给
$$
 \int\|\mathcal R\|_{\mathcal A_2}dt
 <512\,2^{-435}X_\beta=2^{-426}X_\beta .
$$
同时可取宽松界 $\|\nu-1\|_{\mathcal A_2}<2^{-430}X_\beta$。

还可以在不微分 $A$ 的情况下准确计算倍率：
$$
 \boxed{\quad
 \frac{\nu_t}{\nu}
 =\left(\frac{A(1-v^2)-d^2}{E}\right)\circ\phi .
 \quad}                                                     \tag{F.26}
$$
因为 $(\log j)_t=-d_\theta\circ\phi$，它与 (F.11) 第一式的
$d_\theta$ 项相消。其完整积分 norm 小于
$14I<2^{-431}X_\beta$，特别小于 $2^{-430}X_\beta$。
该恒等式跨过所有型别零点均成立。

这里的实际 $\nu$ 仍在 principal 角导项中。即使
$\|\nu-1\|$ 任意小，高频相位仍不可由同宽的“小算子差”替代。
(F.26) 控制的是实际系数及其可积变化，不是已经完成的相位共轭。

## 6. 源、两个真实迹和 mean 的准确往返

(F.25) 对普通 scalar 源有实际宽度合同
$$
 \|\widehat e(t)\|_{\mathcal A_2}
 \le2\|e(t)\|_{\mathcal A_3}.
 \tag{F.27}
$$
完整反变换为
$$
 \dot P\circ\phi=Y_1,\qquad
 \dot K\circ\phi=(d\circ\phi)Y_1+(v\circ\phi)Y_2 .
 \tag{F.28}
$$
所以原高度相容条件及 mean 读取为
$$
 \langle jY_1\rangle=0,\qquad
 \dot K_0=\left\langle
 j\bigl[(d\circ\phi)Y_1+(v\circ\phi)Y_2\bigr]\right\rangle.
 \tag{F.29}
$$
不能直接把 $Y$ 的 Fourier 零模丢掉。全部标签及全部高输出都先经
真实微分同胚变换，低高交叉未被投影删除。

记 $\dot v$ 为原物理 raw 高度变化。完整恢复公式是
$$
 (\dot v)_\theta=aw\,\dot P,\qquad
 \partial_t(\dot v)_0=aw\,\dot K_0 .
 \tag{F.30}
$$
后一式须带一个独立的内端平均高度 $\dot\lambda$；即使规范状态在
平尾端趋零，也不能据此把 $\dot\lambda$ 置零。
原径向迹为 $(\dot v)_a=w\dot K$。
由已经支付的 raw 两迹、水平原函数和 normal/shear 公式得到同一
grounded 两迹及其物理 mean；没有将 $Y_2$ 误称为真实 conormal。
真实 conormal 及源密度的变换仍是前篇 (A.8)、(A.18)、(A.21)。
本篇的 $Y$ 是相对梯度框架，不能替代其中动量必须乘 $j$ 的密度规则。

最后把 holonomy 行明确保留。令 $\rho=D^{-3/2}$，
$$
 M=\left\langle
 \frac{1+w^2(1+K)U/(1-w^2P^2)}{\sqrt D}
 \right\rangle.
$$
完整源恒等式在 exact 背景上线性化给
$$
 (\dot M)_t=w^2\langle\rho J e\rangle
   =w^2\left\langle j\,(\rho J e)\circ\phi\right\rangle.
 \tag{F.31}
$$
若用 $m=\dot M/w^2$，则准确为
$$
 m_t=-2Am+\langle\rho J e\rangle,\qquad
 \dot M(t)=\dot M(t_0)+\int_{t_0}^{t}w^2\langle\rho J e\rangle\,ds.
 \tag{F.32}
$$
不把这个变系数 mean 行改成 $m_t=-2m$，也不对任意 $e$ 假设其
holonomy 负荷为零。对真实标签 Jacobi 列，$e=0,\dot M=0$ 始终成立。
一般 scalar 源的非零 holonomy 是需联立支付的有限行；本篇没有
据此宣称任意有源解都已可周期重建为一个固定度量的向量 Jacobi 场。

## 7. 新结论所减去的费用与剩余算子

现在实际无限尾的低阶扰动已可直接放入完整一阶 Airy/传递框架，
无需先生成含 $A_t$ 或 $A_{tt}$ 的标量 potential 再估计它。
强费用来自真实可求和的 $(1+|A|)N$，并覆盖原全部内部标签。

仍需证明的是保留真实 $\nu$ 及 (F.25) 输出角图的完整传播后，
$$
 DT_k(a)+\mathsf C_LDT_f(a)
$$
与长径向段已付 inner DN 联立的相对高频逆及对应强源估计。
乘法余项的 $L^1_t$ 小量不足以自动控制混合型 principal 的
相对 evolution；相位、边界两迹、mean 和 regular 列仍需同时进入。
特别不将已证原点 $2^{-40}$ 横截门当作整个非线性邻域的免费门。

[精确门与框架程序](../scripts/fourfold_unscalarized_tail_frame_20261113.py)
和 [报告](../notes/2026-11-13-R119-unscalarized-tail-frame-budget.json)
核验准确矩阵恒等式、所有有理余量及无限求和常数。
