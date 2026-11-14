# R150 附录：二次矩阵的实像方向与全部五模式复二次位移

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d。
状态：已证明。本文使用已付的真实偏导全域逆接口；新增的是复二次矩阵的实像判据，以及至多五个正实对数模式中该判据与最高曲线条件的穷尽性。

## 1. 原模式、结论及范围

取不同的正实指数
$$
0<\rho_1<\cdots<\rho_q,\qquad
u_\nu=-\kappa_{\rho_\nu}
+\sum_{p\ge0}\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2}\chi_p.
\tag{1.1}
$$
保留每个原固定中心，且令 $w$ 为任意复平方可和指数权。设
$$
F(x)=x^{\mathsf T}Bx+\ell^{\mathsf T}x+c,\qquad
B=B^{\mathsf T}\in M_q(\mathbb C),\quad B\ne0,
\quad \ell\in\mathbb C^q,\ c\in\mathbb C.
\tag{1.2}
$$
这里二次系数可以全部为复数；$\mathsf T$ 表示普通转置，所有多项式导数均为复代数的双线性导数，不用 Hermitian 伴随代替。

**实像判据。** 如果
$$
\boxed{\operatorname{Ran}_{\mathbb C}B\cap\mathbb R^q\ne\{0\},}
\tag{1.3}
$$
则对全部 $\lambda\in\mathbb C$，
$$
\boxed{[F(u_1,\ldots,u_q)-\lambda]e^w
\text{ 非零且对原实际 }A\text{ 循环}.}
\tag{1.4}
$$
特别，充分条件是
$$
\operatorname{rank}_{\mathbb C}B>\frac q2.
\tag{1.5}
$$

**五模式结论。** 对任意 $q\le5$、任意 (1.1) 及任意非零复二次部分 (1.2)，结论 (1.4) 总成立，不要求指数等差，不要求任何指数间隔。

这些结论只直接断言 (1.4)。对于本稿实像分支，不自动断言所有普通点态幂或所有 $Q(F)e^w$。最高曲线非零的另一个分支仍保留其既有全复合结论。

## 2. 实像给真实的空谱一阶偏导

设 $0\ne y\in\operatorname{Ran}_{\mathbb C}B\cap\mathbb R^q$，选 $v\in\mathbb C^q$ 使
$$
Bv=y.
\tag{2.1}
$$
对 (1.2) 的普通方向导数为
$$
\partial_v F=2y^{\mathsf T}x+\ell^{\mathsf T}v.
\tag{2.2}
$$
令其原点态一阶符号为
$$
d(u)=2\sum_{\nu=1}^q y_\nu u_\nu+\ell^{\mathsf T}v.
\tag{2.3}
$$
$y\ne0$ 且指数不同，故它的真实物理行
$$
b_p=\frac1{p+2}
\sum_{\nu=1}^q2y_\nu\rho_\nu
(\log(p+2))^{\rho_\nu-1}
\tag{2.4}
$$
不是零行。若 $\nu_*$ 是最大满足 $y_{\nu_*}\ne0$ 的指标，则
$$
b_p\sim
2y_{\nu_*}\rho_{\nu_*}
\frac{(\log(p+2))^{\rho_{\nu_*}-1}}{p+2}.
\tag{2.5}
$$
因此 $b\in\ell^2\setminus\ell^1$，并且从某个位起具有固定实符号。其相位缺陷可和；有限头只增加有限和。

[R138 §§1、3](R138-first-chaos-complete-spectrum-classification.md) 给这个原一阶的空谱及全部有界交换预解。
原固定常数与任意复 $\ell^2$ 权 $w$ 的倾斜只加入有界交换扰动；准确的级数费用是原行与 $w$ 的 $\ell^2\times\ell^2$ 绝对可和估计。
[真实偏导逆稿 §3](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md) 已支付其完整同域实现
$$
\mathsf D=X_{d,w},\qquad
\boxed{\mathsf D^{-1}\in\{A\}'\cap B(H).}
\tag{2.6}
$$
这不是只知道第一阶向量循环。具体地，若 $L_0$ 是其未倾斜空谱一阶的有界拟幂零逆，$H_w$ 为真实有界交换扰动，则
$$
\mathsf D^{-1}=L_0(I+H_wL_0)^{-1}.
\tag{2.7}
$$
$H_wL_0$ 拟幂零，括号为有界单位；左右逆都在原完整域上成立。

## 3. 完整合并矩中的方向与全部 Bell 修正

以 $\mathsf P_{F-\lambda,w}$ 表示原向量
$(F(u)-\lambda)e^w$ 的完整规范 Bell 实现。
所有矩按
$$
(k,s)=\bigl(|\omega|,\rho\cdot\omega-|\omega|\bigr)
$$
准确合并。一次键
$$
g_\nu=(1,\rho_\nu-1)
$$
彼此不同，且 $Y_{e_\nu}=\rho_\nu W_{g_\nu}$。

因此取固定显示方向
$$
\boxed{
\partial_{\eta}
=\sum_{\nu=1}^q\frac{v_\nu}{\rho_\nu}
\partial_{W_{g_\nu}},
}
\tag{3.1}
$$
其普通转共振生成式的准确导数就是 (2.2) 的完整一阶实现。二次 Bell 修正对显示的一次变量为常数；等价地，完整修正为系数独立于显示矩变量的有限微分算子，和 (3.1) 交换。于是
$$
\boxed{\partial_\eta\mathsf P_{F-\lambda,w}=\mathsf D.}
\tag{3.2}
$$
(3.2) 首先在原共同深域上成立。两边的原 $e^w$ 多项式轨道图核心识别同一个完整闭一阶图；使用的是 R186 的规范图一致性，而非仅有形式多项式恒等式。
常数 $\lambda$ 不改变这个偏导，(2.6) 因而对每个所需位移提供同一个真实方向逆。

## 4. 在原核内实施偏导逆接口

这里明确说明一个固定方向组合没有引入额外假设。
令
$$
M=\ker\mathsf P_{F-\lambda,w}.
$$
原完整有限矩池已经由
[合并对数矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)
支付。每块物理矩阵记为 $\Xi_B$，把原单一目标坐标 $e_*$ 换成 (3.1) 的固定系数列 $\eta$，取
$$
b_B=\frac14\Xi_B^{-1}\eta,\qquad
Q_B=\mathsf D^{-1}
\sum_i (b_B)_i\prod_{j\ne i}t_{p_j}N_{p_j}.
\tag{4.1}
$$
完整一次反射系数满足
$$
L_{p_i}=4\sum_g m_g(p_i)\partial_gP,\qquad
\sum_i(b_B)_iL_{p_i}=\mathsf D.
$$
所以每个块的顶部通过真正的
$\mathsf D\mathsf D^{-1}=I$ 精确还原。

[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
的有界核方程和交换域结论使 $\mathsf D^{-1}$ 保持 $M$ 及全部所需自然词域。
先按已付正分量共同预解以深度 $O(r\deg F)$ 正则原核，仍强趋恒等。
$r$ 个块新增的费用仅是固定几何因子
$\|\mathsf D^{-1}\|^r$；方向 $\eta$ 也固定。
它们都在原 $O(r\log N)$ 对数输入预算中，严格低于原局部四次衰减。

全部输入先在 $M$ 中形成，反射始终在最左。
不把 $\mathsf D^{-1}$ 穿过反射，不让其伴随作用于未知 $M$。
因此
[真实偏导逆稿 §2](R150-appendix-global-derivative-inverses-real-quadratic-logarithmic-resonances-and-all-powers.md)
的完整顶部、纯池非零弱极限、两侧实际 $A$ 四次因子与全 $H$ 上的 $C$ 配对逐项适用，给 $M=0$。
原规范图判据同时给非零性和循环性。这证明 (1.4)。

## 5. 复秩的实维数充分条件

设 $r=\operatorname{rank}_{\mathbb C}B$。
把 $\mathbb C^q$ 视为 $2q$ 维实向量空间，则
$\operatorname{Ran}_{\mathbb C}B$ 的实维数为 $2r$，而 $\mathbb R^q$ 的实维数为 $q$。
有限维维数公式给
$$
\dim_{\mathbb R}
\left(\operatorname{Ran}_{\mathbb C}B\cap\mathbb R^q\right)
\ge 2r-q.
\tag{5.1}
$$
所以 $r>q/2$ 确保存在 (2.1) 所需的非零实 $y$。
这里不要求 $B$、$v$ 或 $\ell$ 为实数；实的只是选出的像向量 $y$。

## 6. 最高曲线恒零的非零二次部分至少有秩三

记既有最高曲线
$$
\mathcal H_F(t)
=F_2(\rho_1t^{\rho_1},\ldots,\rho_qt^{\rho_q}),
\qquad F_2(x)=x^{\mathsf T}Bx,\quad t>0.
\tag{6.1}
$$
若 $\mathcal H_F$ 不恒零，
[合并对数矩定理](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)
已给所有非零 $Q(F)e^w$ 循环，特别给 (1.4)。

以下设 $\mathcal H_F\equiv0$。
若 $B$ 的复秩不超过二，非零复二次型可分解成两个非零复线性型的乘积：
$$
F_2(x)=L_1(x)L_2(x).
\tag{6.2}
$$
这由复对称二次型的合同对角化直接得到：秩一为平方；秩二用
$z_1^2+z_2^2=(z_1+iz_2)(z_1-iz_2)$。
所有系数非零的缩放都可吸收到线性型内。

对于任意非零线性型 $L$，函数
$$
L(\rho_1t^{\rho_1},\ldots,\rho_qt^{\rho_q})
$$
不恒零。确实取最大非零系数的指数，除以其 $t^\rho$ 后令 $t\to\infty$，所得极限为非零常数。
这些函数在 $(0,\infty)$ 上实解析。
若 (6.2) 的两个因子之积恒零，其中一个因子在某个非空开区间非零，另一个就在那里恒零，进而由解析唯一性在整个区间恒零，矛盾。
因此
$$
\boxed{\mathcal H_F\equiv0,\ F_2\ne0
\quad\Longrightarrow\quad \operatorname{rank}_{\mathbb C}B\ge3.}
\tag{6.3}
$$

当 $q\le5$ 时，(6.3) 给 $r\ge3>q/2$，于是 §§2–5 的实像判据适用。
和最高曲线非零分支合并，得到 (1.4) 的全部五模式结论。

## 7. 准确使用边界

仿射非恒定目标已由最高曲线的线性独立性处理；本稿的新增内容是二次复系数，不重复登记仿射情形。
非零常数目标另为非零常数倍 $e^w$；恒等零多项式当然不属于非零循环结论。

本稿不能把 $\partial_vF$ 的真实有界逆直接作为任意 $Q(F)$ 的完整偏导逆。
外层复合后必须重新建立全部普通 Bell 与合并矩；一般高阶方向 $v^{\otimes h}$ 也不必和原合并键相容。
因此五模式结论只保证所有一次位移 $(F-\lambda)e^w$。
另行已付的实二次全复合、矩形首系数全复合及特定四次族全复合仍保各自范围。

一般 $q\ge6$ 的曲线恒零二次型、像中无非零实方向的矩阵、无限模式和任意 $L^2$ 向量不由本文自动解决。
普通 Hilbert 不变子空间问题仍未完成。
