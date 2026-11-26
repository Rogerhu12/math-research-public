# R597 有限角弱 BVP 的准确核心余项与可实现的自由阶

状态：严格核心接口；主课题未完成。

本条给 [R594](../results/R594-exact-nonlinear-radial-acceleration-and-galerkin-leakage.md) 的非线性弱径向方程补完整核心端值。它用于保留实际高度场的有限角边值计算，不以 $R-\varepsilon$ 冒充核心，不断言一个尚未求出的有限解存在。

## 1. 假设、符号和真正有界的核心量

令 $\delta=R-r$，$1/2<\alpha<1$。背景满足逐阶可微的一致渐近
$$
W=k\delta^{-\alpha}(1+O(\delta))+O(1),\qquad
W'=\alpha k\delta^{-\alpha-1}(1+O(\delta))+O(\delta^{-\alpha}),
\quad k>0.
$$
只写 $W\sim k\delta^{-\alpha}$ 而不控制导数不足以推出以下极限。

高度为 $Z=h+f$，$h'=-W$，$\langle f\rangle=0$，
$f(R,\theta)=0$。假设角向所用导数一致，并且
$$
P(r,\theta)=Wf_r,\qquad
P(r,\cdot)\longrightarrow P_0,\qquad
P_r(r,\cdot)\longrightarrow P_1
$$
在足够角 jets 中成立。于是 $\langle P_0\rangle=\langle P_1\rangle=0$。由积分和微分，
$$
f=-\frac{P_0}{k(1+\alpha)}\delta^{1+\alpha}
+o(\delta^{1+\alpha}),\qquad
f_r=\frac{P_0}{k}\delta^\alpha+o(\delta^\alpha),
$$
$$
f_{rr}=-\frac{\alpha P_0}{k}\delta^{\alpha-1}
+o(\delta^{\alpha-1}),\qquad
W'f_{\theta\theta}\longrightarrow
-\frac{\alpha}{1+\alpha}(P_0)_{\theta\theta}.
$$
这些条件适用于本包的真实齐次 core modes、已经定义的非齐次 $j=4$ core flow 和下述新的径向自由项；一般任意 $C^2$ 高度并不会自动满足它们。

设同一 turning 根写作 $E=W^2+e$。
在 R576/R594 的正域内，核心根 $e_R$ 由
$$
\left\langle(e_R+2P_0)^{-1/2}\right\rangle=1,
\qquad e_R+2P_0>0 \tag{1}
$$
唯一给定，且 $e\to e_R$、$M\to R$。对光滑 $P_0$，左边在
$e_R>-2\min P_0$ 严格递减；在下端，由最小点的二次上界，积分趋于无穷，
在无穷端趋于零，故确有唯一正域根。其分母在角圆上有严格正下界。
这里只用实际核心 $P_0$；不将背景 $e_R=1$ 偷换到非圆高度上。

## 2. 完整核心残差

沿用 R576 的无背景大项表达
$$
\begin{aligned}
A_t={}&-rWf_{rr}-rW'f_r-eW'f_{\theta\theta}\\
&+(W^2+e)f_{rr}f_{\theta\theta}
-WW'f_rf_{\theta\theta}
-(W^2+e)(f_{r\theta}-f_\theta/r)^2\\
&+rf_rf_{rr}+WW'f_\theta^2/r .
\end{aligned} \tag{2}
$$
把其线性部分写成
$$
-r(Wf_r)'-W'f_{\theta\theta}
=-rP_r-W'f_{\theta\theta};
$$
这是一个准确恒等式，避免分别求两个发散大项再相减。

其余各项的极限为
$$
-(e-1)W'f_{\theta\theta}
\longrightarrow \frac{\alpha}{1+\alpha}(e_R-1)(P_0)_{\theta\theta},
$$
$$
(W^2+e)f_{rr}f_{\theta\theta}
\longrightarrow\frac{\alpha}{1+\alpha}P_0(P_0)_{\theta\theta},
$$
$$
-WW'f_rf_{\theta\theta}
\longrightarrow\frac{\alpha}{1+\alpha}P_0(P_0)_{\theta\theta},
\qquad
-(W^2+e)(f_{r\theta}-f_\theta/r)^2\longrightarrow-(P_0)_\theta^2.
$$
$r f_r f_{rr}=O(\delta^{2\alpha-1})\to0$，此处用到 $\alpha>1/2$；
$WW'f_\theta^2/r=O(\delta)\to0$。因此
$$
\boxed{
(A_t)_R=-RP_1+\frac{\alpha}{1+\alpha}
(e_R+2P_0)(P_0)_{\theta\theta}-(P_0)_\theta^2 .
} \tag{3}
$$

上述一致 jets 还实际支付 $e'$ 的有限极限。置
$u_R=(e_R+2P_0)^{1/2}$。由 $q=f_\theta=O(\delta^{1+\alpha})$、
$p=-W+f_r$ 和 $t=f_{\theta\theta}$，有
$$
N_r\longrightarrow-\frac{(P_0)_{\theta\theta}}{R(1+\alpha)},
\qquad (V-W^2)_r\longrightarrow-2P_1.
$$
第一式使用 $(Wt)_r=W't+P_{\theta\theta}\to(P_0)_{\theta\theta}/(1+\alpha)$；
第二式中 $(f_r^2)_r=O(\delta^{2\alpha-1})\to0$、
$\bigl(p^2q^2/b^2\bigr)_r=O(\delta)\to0$。
对准确 turning 恒等式 $\langle N/u\rangle=1$ 隐微分，正分母的极限非零，故
$$
\boxed{
e'_R=-2\frac{\langle P_1/u_R^3\rangle+
\langle(P_0)_{\theta\theta}/u_R\rangle/[R(1+\alpha)]}
{\langle u_R^{-3}\rangle}.
} \tag{3a}
$$
因此完整 Darboux 缺陷 $D=A_t-e'M/2$ 有实际有限端值
$$
D_R=(A_t)_R-\frac R2 e'_R. \tag{3b}
$$
角向分部积分给
$\langle(P_0)_{\theta\theta}/u_R\rangle
=\langle(P_0)_\theta^2/u_R^3\rangle$；
将 (3a) 代回 (3)，也直接核得 $\langle u_R^{-3}D_R\rangle=0$。
这里没有将两个发散背景导数相减作为数值端值。
有限角弱边值行不需要事先猜 $e'_R$：对每个正角频率 $m$，
$$
\left\langle\cos(m\theta)\frac{D_R}{M_R}\right\rangle
=\frac1R\langle\cos(m\theta)(A_t)_R\rangle . \tag{4}
$$
常数 $e'_R$ 准确消去。若全部正频率为零，$A_t$ 为角常数，且原 turning 导数身份
$\langle u^{-3}D_R\rangle=0$ 再强制 $D_R=0$；
只消有限频率时，剩余核心角谱仍须报告，不能由 (4) 隐去。

## 3. 齐次、旧 forced 项和新自由项逐一支付

对真实齐次模 $f_j=C_j(r)\cos(j\theta)$，满足
$$
r(WC_j')'-j^2W'C_j=0,\qquad C_j(R)=0,
$$
且 $A_j(R)$ 有限，原定义
$A_j=W(j^2 C_j-rC_j')/(j^2-1)$ 给
$$
(P_0)_j=-\frac{j^2-1}{R}A_j(R),\qquad
(P_1)_j=\frac{\alpha}{R(1+\alpha)}(P_0)_{j,\theta\theta}. \tag{5}
$$
代 (3) 后，$-RP_1+\alpha(P_0)_{\theta\theta}/(1+\alpha)$ 的齐次线性部分准确为零。它不意味着非线性的剩余部分为零。

旧 body-forced $j=4$ 方向满足
$r(WG')'-16W'G=S$，故其准确线性贡献是
$-S(R)\cos4\theta$，要乘它在实际高度中的系数和已冻结的正归一尺度。原浮点传播误差及显式两 jets 混合不因这一形式等式而成为证书。

$\tanh$ 前高度 $v=O(\delta^{1+\alpha})$、其齐次部分满足上述端条件时，
$\tanh(v/s)s-v=O(\delta^{3+3\alpha})$，逐阶导数余项给其对 $P_0,P_1$ 均无贡献。
原 envelope bulk 为 $O(\delta^{2+2\alpha})$，其 $P=O(\delta^{1+\alpha})$、$P_r=O(\delta^\alpha)$，也不改变这两个端值。

若只继续采用该旧 bulk 阶，则端部的一般非线性源没有独立的 $P_1$ 自由度。新的自由项选为
$$
\Delta f(r,\theta)=b(r,\theta)\delta^{\alpha+2}, \tag{6}
$$
其中 $b$ 至少 $C^2$ 延伸到核心，角 jets 足够，则
$$
(\Delta P)_0=0,\qquad
(\Delta P)_1=k(\alpha+2)b(R,\theta). \tag{7}
$$
它准确保持核心主角函数 $P_0$，同时独立改变 (3) 中的 $-RP_1$。
因 $1/2<\alpha<1$，在 R576 的正则核心变量
$x=(\delta/d)^{1-\alpha}$ 中，(6) 为
$O(x^{(\alpha+2)/(1-\alpha)})$，指数大于 5；相应两 jets 在核心为零。
故在已经满足 R576 核心匹配门的候选上，它保持闭面的 $C^2$ 匹配。
这不是说任意主体高度自动满足该门。

例如当前 $\alpha=.55$，旧 bulk 阶为 $\delta^{3.1}$，
新的 source-response 自由阶为 $\delta^{2.55}$；
两者都可有 $C^2$ 核心，但只有后者能直接调整一般有限的 $P_1$ 余项。
该区别是准确渐近阶，不是对数值峰的经验拟合。

## 4. 有限角边值实现中的身份

下一输入保留完整实际高度 $f_{\rm paid}$，新增
$$
\Delta f=\sum_{m=2,4,\ldots,16}
\left(a_m C_m^{\rm adm}(r)
+\chi_{\rm in}(r)\delta^{\alpha+2}B_m(r)\right)\cos(m\theta).
$$
各 $C_m^{\rm adm}$ 的内端都是本模真实全平线，核心齐次段的
$A_m(R)$ 和显式连接修正全部保留。$\chi_{\rm in}$ 在一个明定的小内区恒零，之后光滑变成 1；这只限制新的 bulk，不把原高度或真实端核冻结为零。$B_m$ 为实际径向样条未知函数。
固定 $a_2=0$ 保持已经选择的主核心幅度，径向静态参数 $H$ 为一个未知；
其它核心模系数可以变化。这里改变 $H$ 是静态设计新度量，尚非同一个 $g$ 的弯曲。

主体求解准确的有限弱行 $\langle\cos(m\theta)D/M\rangle=0$，
核心加入 (3)--(7) 的准确有限端行。它们作为整体非线性边值系统离散，禁止按失号的 $\mathfrak a$ 点除；
实际 $\mathfrak a$、弱质量矩阵和完整原度量残差均另行报告。
有限样条/有限角求根仍只是离散近似；原非线性内尾、所有高角谱泄漏、数值传播误差和真正全局 reach 仍须继续支付。

