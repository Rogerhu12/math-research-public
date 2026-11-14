# R28：保作用量径向均值的精确 Liouville 归一与全高频逆

2026-11-12，visible-flex-exact-nearby / independent-audit。

**状态：已证明的中间结论。** 对 R25 的新背景，本文处理偶对称、仅在
正势区内部改变、且精确保正势作用量的真实径向均值。一个在全部外尾
恒等的 Liouville 坐标把 $n^2$ 级主势改变准确变成与 $n$ 无关的有界
零阶势。因此所有充分高的四重频率都有已付常数的真实逆，只剩有限个
低角频的实际一维边值问题及有限秩兼容需要另外处理。本文也给两个
具体合法均值方向；其作用量和第四模投影有非退化的真实 Jacobian。

本结果尚未归一化角依赖的非径向主符号；未把任意有限幅候选或其
非线性边界图纳入本定理。它解决的是自由均值造成的全高频漂移问题。

## 1. 同一个新背景与允许的实际径向改变

固定 R25 的
$$
\mu=\frac{484}{89},\qquad
\nu=\frac{495}{89},\qquad
V(x)=\nu^2\operatorname{sech}^2x-\mu^2.
$$
令 $x_0>0$ 为正零点，则
$$
\tanh^2x_0=\frac1{4\mu+1},\qquad
\int_{-x_0}^{x_0}\sqrt{V}\,dx=\frac{11\pi}{89}.
\tag{1.1}
$$

设 $\widetilde V$ 为真实偶 $C^\infty$ 函数，满足：

1. $\widetilde V-V$ 的支撑为 $(-x_0,x_0)$ 内的紧集；
2. $\widetilde V>0$ 于 $(-x_0,x_0)$；
3. 精确作用量相等：
$$
\int_{-x_0}^{x_0}\sqrt{\widetilde V(x)}\,dx
=\int_{-x_0}^{x_0}\sqrt{V(x)}\,dx.
\tag{1.2}
$$

这些条件包括转折点及完整外尾保持不变，不是把近似相等的积分当成
(1.2)。后面的两个指数均值给实际满足这些条件的局部参数曲线。
一般定理也允许较大的改变，只要上述条件和下列导数界确实得到验证。

## 2. 准确的紧支坐标改变

在 $|x|<x_0$ 定义
$$
I(x)=\int_0^x\sqrt{V(t)}\,dt,\qquad
\widetilde I(x)=\int_0^x\sqrt{\widetilde V(t)}\,dt,
$$
$$
\varphi(x)=I^{-1}\bigl(\widetilde I(x)\bigr).
\tag{2.1}
$$
两势均正，故 $I,\widetilde I$ 在内部严格递增。偶性和 (1.2) 使它们
具有完全相同的两个端值，所以 (2.1) 在整个内部有唯一解。
它为奇函数，且
$$
\rho(x):=\varphi'(x)>0,\qquad
\widetilde V(x)=\rho(x)^2V(\varphi(x)).
\tag{2.2}
$$

这个坐标在转折点处没有隐藏奇性。事实上，由支撑条件，存在
$\delta>0$ 使两势在 $[x_0-\delta,x_0]$ 相同；再用半作用量相等，
对于这段内的 $x$，
$$
\widetilde I(x)
=\widetilde I(x_0)-\int_x^{x_0}\sqrt{\widetilde V}
=I(x_0)-\int_x^{x_0}\sqrt V=I(x).
$$
故 $\varphi(x)=x$ 于该整段。负端相同。在 $|x|\ge x_0$ 直接定义
$\varphi(x)=x$，得到全实线上的奇 $C^\infty$ 保向微分同胚，且
$\varphi-\operatorname{id}$ 紧支于原正势区内部。
因此包括实际长帽切口、Robin 两迹和全部外尾在内的外部坐标保持原样。

记逆映射为 $\psi=\varphi^{-1}$。给定任意已验证的界
$$
0<m\le\rho(x)\le M<\infty,\qquad
A_1\ge\left\|\frac{\rho'}{\rho^2}\right\|_\infty,
\tag{2.3}
$$
以及下面定义的 $Q_*\ge\|Q\|_\infty$。这些都是紧集上的有限导数
上确界，外部 $\rho=1$、$\rho'=\rho''=Q=0$。

## 3. Liouville 恒等式与 Schwarzian 的符号

令
$$
u(x)=\rho(x)^{-1/2}v(\varphi(x)).
\tag{3.1}
$$
因为 $2(\rho^{-1/2})'\rho+\rho^{-1/2}\rho'=0$，
$$
u''=\rho^{3/2}v''\circ\varphi
+\left(\frac34\rho^{-5/2}(\rho')^2
-\frac12\rho^{-3/2}\rho''\right)v\circ\varphi.
$$
所以对于每个整数 $n$ 有准确恒等式
$$
\boxed{\quad
(-\partial_x^2-n^2\widetilde V)u
=\rho^{3/2}\bigl(L_nv+Qv\bigr)\circ\varphi ,
\quad}
\tag{3.2}
$$
其中 $L_n=-\partial_\xi^2-n^2V(\xi)$，而 $Q$ 的自变量是 $\xi$：
$$
\boxed{\quad
Q(\xi)=
\left(\frac{\rho''}{2\rho^3}
-\frac{3(\rho')^2}{4\rho^4}\right)\!(\psi(\xi))
=\frac12\left(\frac{S\varphi}{(\varphi')^2}\right)\!(\psi(\xi))
=-\frac12 S\psi(\xi).
\quad}
\tag{3.3}
$$
$Sf=f'''/f'-\tfrac32(f''/f')^2$。最后的符号来自
$S(\varphi\circ\psi)=0$，不能省略逆映射或把两个 Schwarzian 的符号混用。

例如，若直接认证了
$$
\|\varphi'-1\|_\infty\le b<1,\qquad
\|\varphi''\|_\infty\le c,\qquad
\|\varphi'''\|_\infty\le d,
$$
则可明确取
$$
m=1-b,\quad M=1+b,\quad
A_1=\frac{c}{(1-b)^2},\qquad
\boxed{\quad
Q_*=\frac{d}{2(1-b)^3}
+\frac{3c^2}{4(1-b)^4}.
\quad}
\tag{3.4}
$$
也可直接用 (3.3) 做更紧的区间认证。这里没有频率依赖的未知常数。

## 4. 正确的 $L^2$ 范数转移与全部高角频

令
$$
\widetilde L_n=-\partial_x^2-n^2\widetilde V(x),\qquad
\widehat f(\xi)=\bigl(\rho^{-3/2}f\bigr)(\psi(\xi)).
$$
由于 $d\xi=\rho\,dx$，精确换元给
$$
\|\widehat f\|_2^2
=\int\rho^{-2}|f|^2dx\le m^{-2}\|f\|_2^2,
$$
$$
\|u\|_2^2
=\int\rho(\psi(\xi))^{-2}|v(\xi)|^2d\xi
\le m^{-2}\|v\|_2^2.
\tag{4.1}
$$
不能将 (3.1) 当成酉变换；两个 $m^{-1}$ 因子都必须支付。

取 $n\in4\mathbb N$、$n\ge8$。R25 给 $\|L_n^{-1}\|\le66/n$。
若
$$
\eta_n:=\frac{66Q_*}{n}<1,
\tag{4.2}
$$
则在同一 $L^2_\xi$ 空间中
$$
(L_n+Q)^{-1}
=(I+L_n^{-1}Q)^{-1}L_n^{-1}
$$
由真正 Neumann 级数定义，没有消耗角解析宽度。
所以 $\widetilde L_n:H^2(\mathbb R)\to L^2(\mathbb R)$ 实际可逆，且
$$
\boxed{\quad
\|\widetilde L_n^{-1}f\|_2
\le\frac{66}{m^2n(1-\eta_n)}\|f\|_2.
\quad}
\tag{4.3}
$$
其定义域合法性由 $v\in H^2$ 和光滑、有界且外部恒等的 $\varphi$
直接得到；(3.2) 同时证明唯一性。

由
$$
u'=\rho^{1/2}v'\circ\varphi
-\frac12\rho^{-3/2}\rho'v\circ\varphi
$$
和 R25 的一阶界，得到
$$
\boxed{\quad
\|u'\|_2\le
\frac{78+33A_1/n}{m(1-\eta_n)}\|f\|_2.
\quad}
\tag{4.4}
$$
这里第一项换元后恰为 $\|v'\|_2$，没有额外 $M$ 因子。
二阶可直接从实际方程付费：
$$
\|u''\|_2
\le\left(1+\frac{66n\|\widetilde V\|_\infty}
{m^2(1-\eta_n)}\right)\|f\|_2.
\tag{4.5}
$$

一个明确全高频截止是
$$
\boxed{\quad N=4\left\lceil\max\{2,33Q_*\}\right\rceil .\quad}
\tag{4.6}
$$
对所有 $n\in4\mathbb N$、$n\ge N$，有 $\eta_n\le1/2$。
因此 (4.3)--(4.5) 的 $1/(1-\eta_n)$ 可统一换成 $2$。
只剩 $4\le n<N$ 的有限个角频；每个仍是需要真正认证的连续
一维 Sturm 问题，不把一张有限差分矩阵当成该连续算子本身。

## 5. 普通两分量源也不损角阶

考虑同一改变后背景的系统
$$
X'=-in\widetilde VY+g_1,\qquad
Y'=-inX+g_2.
\tag{5.1}
$$
以下只讨论满足 (4.2) 的 $n\ge8$，所以没有核兼容遗漏。
作明确的三角变换
$$
Y(x)=\rho(x)^{-1/2}b(\varphi(x)),\qquad
X(x)=\rho(x)^{1/2}a(\varphi(x))+
\frac{\rho'(x)}{2in\rho(x)^{3/2}}\,b(\varphi(x)).
\tag{5.2}
$$
直接求导，两个 $a$ 的零阶交叉项相消，得到
$$
a_\xi=-inVb+\frac{iQ}{n}b+\widehat g_1,\qquad
b_\xi=-ina+\widehat g_2,
\tag{5.3}
$$
其中
$$
\widehat g_1
=\left(\rho^{-3/2}g_1-
\frac{\rho'}{2in\rho^{5/2}}g_2\right)\circ\psi,\qquad
\widehat g_2=(\rho^{-1/2}g_2)\circ\psi.
\tag{5.4}
$$
消元为 $(L_n+Q)b=in\widehat g_1-\widehat g_2'$，与 (3.2) 一致。

令 $(a_0,b_0)$ 为未加 $Q$ 的真实 R25 普通源解。由 R25 (4.6)，
$$
\|(a_0,b_0)\|_2\le159\|\widehat g\|_2,\qquad
\|b_0\|_2\le\sqrt{10440}\|\widehat g\|_2.
$$
并且
$$
b=b_0-L_n^{-1}(Qb),\qquad
a=a_0-\frac{i}{n}\partial_\xi L_n^{-1}(Qb).
$$
因此
$$
\|b\|_2\le\frac{\sqrt{10440}}{1-\eta_n}\|\widehat g\|_2,
$$
$$
\|(a,b)\|_2
\le\left(159+
\frac{10440Q_*}{n(1-\eta_n)}\right)\|\widehat g\|_2
\le\frac{159}{1-\eta_n}\|\widehat g\|_2.
\tag{5.5}
$$
最后一步恰用 $10440<159\cdot66$，无需把门放宽成
$159Q_*/n<1$。

置
$$
C_n=\max(1,m^{-1})+\frac{A_1}{2n}.
$$
换元后，(5.2) 的 $L^2$ 传递矩阵为
$$
\begin{pmatrix}
1&\rho'/(2in\rho^2)\\
0&\rho^{-1}
\end{pmatrix};
$$
(5.4) 的源传递矩阵为
$$
\begin{pmatrix}
\rho^{-1}&-\rho'/(2in\rho^2)\\
0&1
\end{pmatrix}.
$$
二者的范数都至多 $C_n$，所以
$$
\boxed{\quad
\|(X,Y)\|_{L^2_x}
\le\frac{159C_n^2}{1-\eta_n}
\|(g_1,g_2)\|_{L^2_x}.
\quad}
\tag{5.6}
$$
对于 (4.6) 的全高频，可统一用 $318C_N^2$。
整个推导只需普通 $L^2$ 源，无端点迹或额外径向导数；
通过光滑源逼近得到实际 $H^1$ 解。常数对全部高角频统一，故可在
同一任意固定 Fourier 权中求和。

## 6. 两个具体的真实指数均值

令 $h>0$ 为 R25 的真实背景解，$w=h'/h$，并定义
$$
\phi_i(x)=
\begin{cases}
\displaystyle\exp\!\left(1-\frac1{1-1024x^2}\right),&|x|<1/32,\\
0,&\text{其它},
\end{cases}
$$
$$
v_0(x)=(4\mu+1)\tanh^2x,\qquad
\phi_o(x)=\Psi(8v_0(x)-6),
$$
$$
\Psi(s)=
\begin{cases}
\displaystyle\exp\!\left(4-\frac1{s(1-s)}\right),&0<s<1,\\
0,&\text{其它}.
\end{cases}
\tag{6.1}
$$
二者都是非零非负偶 $C^\infty$ 函数；外方向支持在
$3/4<v_0<7/8$，内方向支持在 $v_0<1/8$。两支持不交并均严格位于
正势区内部。设
$$
\zeta=\alpha\phi_i+\beta\phi_o,\qquad
h_{\alpha,\beta}=he^\zeta,
$$
$$
V_{\alpha,\beta}
=-\frac{h_{\alpha,\beta}''}{h_{\alpha,\beta}}
=V-\zeta''-2w\zeta'-(\zeta')^2.
\tag{6.2}
$$
实际旋转面用 $a_{\alpha,\beta}=h_{\alpha,\beta}^{-1}$、
$(z_{\alpha,\beta})_x=h_{\alpha,\beta}^{-2}$ 定义。
这不是给旧线性均值组合重新贴上“保作用量”标签。其外部 $h$ 及势
完全不变，只有两端的高度常数可以各自平移。

在原点附近，$V_{\alpha,\beta}$ 在固定支持上仍正。记
$$
J(\alpha,\beta)=\int_{-x_0}^{x_0}\sqrt{V_{\alpha,\beta}}\,dx.
$$
对任意非零非负、紧支于正势区的方向 $\phi$，
$$
\dot V=-\phi''-2w\phi',\qquad
\dot J=\int\phi\left[-\frac12(V^{-1/2})''
+(wV^{-1/2})'\right]dx<0.
\tag{6.3}
$$
严格符号可直接核验：正半区 $w<0,w'<0,V'<0,V''<0$，
因而 $(V^{-1/2})'>0$、$(V^{-1/2})''>0$，
$(wV^{-1/2})'<0$；负半区由偶性相同。$V''<0$ 来自
$\tanh^2x<(4\mu+1)^{-1}<1/3$，不是对任意势的假设。

所以 $J_\alpha<0,J_\beta<0$，实解析隐函数定理给唯一局部曲线
$$
\beta=\beta(\alpha),\quad \beta(0)=0,\qquad
J(\alpha,\beta(\alpha))=J(0,0),\quad
\beta'(0)=-J_\alpha/J_\beta<0.
\tag{6.4}
$$
沿这条真实曲线，(1.2) 准确成立。每个实际参数的
$\varphi,\rho,Q$ 由 (2.1)--(3.3) 明确给出，故 (4.6) 真正覆盖其
全部高频；不再需要对每个无穷角模另作数值扫描。

## 7. 同一作用量曲线上的第四模横截

令 $y=\operatorname{sech}^{4\mu}x$，
$q_0=h''/h=-V$。对一方向 $\phi$ 定义
$$
\kappa(\phi)=-32\int\phi D\,dx,\qquad
D=(y'-wy)^2+15q_0y^2.
\tag{7.1}
$$
两次分部积分给
$$
\kappa(\phi)=-16\int(\phi''+2w\phi')y^2\,dx,
$$
所以原简单第四模特征值的导数为
$$
E_4'(\phi)=-\frac{\kappa(\phi)}{\|y\|_2^2}.
\tag{7.2}
$$

内方向有具体下界
$$
\boxed{\quad \kappa_i:=\kappa(\phi_i)>\frac{297}{25}>11.\quad}
\tag{7.3}
$$
证明如下。$27/5<\mu<11/2$、$\nu^2<31$，所以 $|x|\le1/32$ 时
$$
-\frac{11}{8}<q_0
=-\frac\mu4+\nu^2\tanh^2x
<-\frac{27}{20}+\frac{31}{1024}<-\frac54.
$$
这里 $h\le1$，且
$$
h\ge1-\frac{11}{16}x^2>\frac{31}{32},\qquad
|h'|\le\frac{11}{8}|x|\le\frac{11}{256},\qquad
|w|\le\frac{11}{248}.
$$
又 $|y'/y|\le4\mu|x|<11/16$，从而
$$
|y'/y-w|<3/4,\qquad D/y^2<9/16-75/4<-18.
$$
在 $|x|\le1/64$，有
$\phi_i\ge e^{-1/3}>2/3$，
$y^2\ge e^{-4\mu x^2}>1-22/4096>99/100$。
代入 (7.1)，得到
$32\cdot18\cdot(1/32)\cdot(2/3)\cdot(99/100)=297/25$ 的严格下界。

外方向满足 $\kappa_o<0$。这里重述 R24 的真实符号估计以说明新参数合法。
设 $t=\tanh x$。由 $\mu>7/5$ 得 $x_0<1/2$，
在 $[0,x_0]$ 上有 $\tanh x\ge(11/12)x$、
$h>24/25$、$|w|\le(25/88)\mu t$。
因此 $|y'/y-w|>(11/3)\mu t$。
在外支持上，
$t^2>3/[4(4\mu+1)]$、$V<\mu/16$、$4\mu+1<5\mu$，故
$$
D/y^2>\frac{121\mu}{60}-\frac{15\mu}{16}
=\frac{259\mu}{240}>\mu.
$$
所有不等式只用已显示的有理界；负半轴相同。于是
$$
\kappa_o<-32\mu\int\phi_oy^2<0.
\tag{7.4}
$$

沿 (6.4) 的准确作用量曲线，
$$
\frac{dE_4}{d\alpha}(0)
=-\frac{\kappa_i+\beta'(0)\kappa_o}{\|y\|_2^2}
<-\frac{11}{2}.
\tag{7.5}
$$
最后用 $\beta'(0)<0,\kappa_o<0$ 和
$\|y\|_2^2<\int\operatorname{sech}^2x\,dx=2$。
原第四模为简单孤立本征值，紧支有界解析乘法扰动的 resolvent
Neumann 级数给所用的可微特征分支，因此 (7.5) 不依赖形式级数。

## 8. 有限低模增广的正确接口

映射 $(\alpha,\beta)\mapsto(J,E_4)$ 在原点的 Jacobian 非退化。
事实上沿 $J$ 等值线的 $E_4$ 导数已由 (7.5) 严格非零，而
$J_\beta\ne0$。这说明可用一个真实均值自由度保持作用量，并留一个
真实自由度处理最低模投影。**不要求均值背景自身的 $L_4$ 始终恰有核**：
有限幅求解中应保留实际第四模振幅/相位规范和实际均值列，解完整
低模增广系统。

本节只支付该径向参数接口的非退化性。对于给定有限幅非径向候选，
它的完整低模 Jacobian、非齐次尾 DN、重建 $J$ 边界项和实际均值列
仍须一起验证。不能用 (7.5) 代替候选上的有限幅 Schur 分母。

最后，高频逆并非有理谱公式的未经证明的连续性转授：
实际机制是 (2.1) 的精确坐标、(3.2) 的准确算子恒等式、
(3.3) 的有界无频率势，以及 (4.2) 的同宽收敛门。
真正角依赖的主系数还会产生混合导数；本文未把它们误当成零阶项。


## 9. 更宽的内方向：半径 $1/8$ 仍有明确横截

有限幅均值探索可以用较宽的实际指数方向
$$
\phi_{i,\mathrm{wide}}(x)=
\begin{cases}
\displaystyle\exp\!\left(1-\frac1{1-64x^2}\right),&|x|<1/8,\\
0,&\text{其它},
\end{cases}
\tag{9.1}
$$
替代 (6.1) 的内方向，外方向保持不变。这个替代仍符合全部同尾和
正势支撑条件，并有更强的显式下界
$$
\boxed{\quad
\kappa_{i,\mathrm{wide}}>
\frac{288\mu}{125}=\frac{139392}{11125}>12.
\quad}
\tag{9.2}
$$

证明不沿用窄支持上的 $q_0<-5/4$。在 $0\le x<x_0$，第 7 节已付
$w<0$ 及 $|w|\le(25/88)\mu\tanh x<4\mu\tanh x$。
置 $t=\tanh x$、$v_0=(4\mu+1)t^2$，则
$$
\frac{D}{y^2}
=( -4\mu t-w)^2-15V
\le16\mu^2t^2-\frac{15\mu}{4}(1-v_0)
<\mu\left(\frac{31}{4}v_0-\frac{15}{4}\right).
\tag{9.3}
$$
在 $|x|\le1/8$，
$$
v_0\le\frac{4\mu+1}{64}=\frac{2025}{5696}<\frac9{25}.
$$
所以 (9.3) 严格小于 $-24\mu/25$。这也说明支撑完全位于正势区内，
并与外方向的 $3/4<v_0<7/8$ 支撑不交。
在 $|x|\le1/16$，
$$
\phi_{i,\mathrm{wide}}\ge e^{-1/3}>2/3,\qquad
y^2\ge e^{-4\mu x^2}>1-\frac{22}{256}>\frac9{10}.
$$
因此
$$
\kappa_{i,\mathrm{wide}}>
\frac{768\mu}{25}\cdot\frac18\cdot\frac23\cdot\frac9{10}
=\frac{288\mu}{125},
$$
即得 (9.2)。第 6 节的 $J_\alpha<0$、$J_\beta<0$ 和第 7 节外方向
$\kappa_o<0$ 仍成立，故存在对应的真实 action 保持曲线，其
$$
\frac{dE_4}{d\alpha}(0)<-6.
\tag{9.4}
$$

这个版本降低固定参数下窄 bump 的高阶导数费用，适合作为数值求解
的另一个实际均值对象。它没有声称某个有限振幅的参数值已经保持
正势、达到 reach 预算或解出非径向方程；那些条件仍需对指数改变
后的同一完整对象验证。


## 10. 使用 R25 强化常数后的更小截止

R25 §8 对同一个 $p=11$ 背景把径向标量逆及其一阶导数常数改进为
$17/n$、$20$，普通两分量源常数改进为 $42$。
因此本结果也可直接使用
$$
\eta_n^{\rm sharp}=\frac{17Q_*}{n}<1,\qquad
N_{\rm sharp}=4\left\lceil\max\{2,17Q_*/2\}\right\rceil .
\tag{10.1}
$$
在该门下，(4.3)--(4.4) 分别改进为
$$
\|\widetilde L_n^{-1}f\|_2
\le\frac{17}{m^2n(1-\eta_n^{\rm sharp})}\|f\|_2,
$$
$$
\|u'\|_2
\le\frac{20+(17/2)A_1/n}{m(1-\eta_n^{\rm sharp})}\|f\|_2.
\tag{10.2}
$$
普通源 (5.6) 改为
$$
\boxed{\quad
\|(X,Y)\|_2\le
\frac{42C_n^2}{1-\eta_n^{\rm sharp}}\|(g_1,g_2)\|_2,
\qquad C_n=\max(1,m^{-1})+\frac{A_1}{2n}.
\quad}
\tag{10.3}
$$
证明逐字沿用第 5 节，仅将
$17^2+20^2=689<42\cdot17$ 代替 $10440<159\cdot66$。
对全部 $n\ge N_{\rm sharp}$，$\eta_n^{\rm sharp}\le1/2$，
所以普通源统一常数可取 $84C_{N_{\rm sharp}}^2$。
更小截止减少需要另行认证的低角频数量；它没有移除第四模兼容、
非径向主符号或真实外尾源的问题。

