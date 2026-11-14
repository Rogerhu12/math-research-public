# R25：奇分母有理作用量的四重背景、线性谱隙与同宽普通源逆

2026-11-12，visible-exact-nearby / independent-audit。

**状态：已证明的中间结论。** 本文另选真实旋转背景，保留唯一第四模核，
把 R20 的四重全频标量逆损失 $O(n^2)$ 改为 $O(n^{-1})$。对应的一阶
Sturm 系统对普通 $L^2$ 两分量源有不损角阶的逆。本文还支付任意角模
耦合的一阶扰动的同宽 Neumann 门；它不覆盖实际非径向线性化的二阶
主系数扰动，不将本背景的谱转授给已有的 $\mu=4\sqrt2$ 候选。
实际固定平尾、有限幅精确解和可见性均仍需另付。

## 1. 明确参数和结论

取整数 $p\ge3$，置
$$
q=8p+1,\qquad
\mu=\frac{4p^2}{q}=\frac{(q-1)^2}{16q},\qquad
\nu=\frac{p(4p+1)}q=\frac{q^2-1}{16q}.
\tag{1.1}
$$
于是
$$
\nu-\mu=\frac pq,\qquad
\nu^2=\mu^2+\frac\mu4,\qquad
\mu>1,\quad q\ge25.
\tag{1.2}
$$
定义
$$
V(x)=\nu^2\operatorname{sech}^2x-\mu^2,\qquad
L_n=-\partial_x^2-n^2V,\qquad
D(L_n)=H^2(\mathbb R).
\tag{1.3}
$$
$L_n$ 是 $L^2(\mathbb R)$ 上的自伴算子。全部正整数频率中唯一的核为
$$
\ker L_4=\mathbb C y,\qquad y(x)=\operatorname{sech}^{4\mu}x.
\tag{1.4}
$$
对全部四重频率 $n\in4\mathbb N$，剔除该核后的每个谱点满足
$$
\boxed{\quad
|\lambda|>\mu n\Delta_q,\qquad
\Delta_q=\frac{q^2-1}{4q^3}.
\quad}
\tag{1.5}
$$
所以，第四模在 $y^\perp$ 上取逆，其余模取完整逆，有
$$
\|L_n^{-1}f\|_2\le\frac{C_q}{n}\|f\|_2,\qquad
C_q=\frac{4q^3}{\mu(q^2-1)}.
\tag{1.6}
$$

特别，本文的具体新背景取
$$
\boxed{\quad
p=11,\quad q=89,\quad
\mu=\frac{484}{89},\quad \nu=\frac{495}{89}.
\quad}
\tag{1.7}
$$
对应的完全有理常数为
$$
C_q=\frac{62742241}{958320}<66.
$$
对所有 $n\in4\mathbb N$，上述真实逆满足
$$
\boxed{\begin{aligned}
\|u\|_2&\le \frac{66}{n}\|f\|_2,\\
\|u'\|_2&\le78\|f\|_2,\\
\|u''\|_2&\le1953n\|f\|_2.
\end{aligned}}
\tag{1.8}
$$
这些是全实线算子估计，未用有限频率扫描或有限区间 Robin 代换。

## 2. 完整谱及唯一核

令 $\ell_n>0$ 由 $\ell_n(\ell_n+1)=\nu^2n^2$ 定义，则
$$
\ell_n=\sqrt{\nu^2n^2+\frac14}-\frac12.
\tag{2.1}
$$
Pöschl--Teller 的实参数因式分解给
$$
\operatorname{spec}_{\rm ess}(L_n)=[\mu^2n^2,\infty),
\qquad
E_{n,j}=\mu^2n^2-(\ell_n-j)^2,\quad
j\in\mathbb Z,\ 0\le j<\ell_n.
\tag{2.2}
$$
这里也可直接证明所用的谱公式。记
$H_\ell=-\partial_x^2-\ell(\ell+1)\operatorname{sech}^2x$，
$B_\ell=\partial_x+\ell\tanh x$，则
$$
B_\ell^*B_\ell=H_\ell+\ell^2,\qquad
B_\ell B_\ell^*=H_{\ell-1}+\ell^2.
$$
$\operatorname{sech}^{\ell}x$ 是能量 $-\ell^2$ 的基态。逐次使用上述
互换恒等式，得到所有 $-(\ell-j)^2$，$0\le j<\ell$。反过来，任何
负能量特征函数逐次下降，或被某个 $B_{\ell-j}$ 消去，或最终落到
参数在 $[-1,0]$ 的非负势算子，后者无负谱。因此没有漏掉负谱。
衰减有界势是自由 resolvent 的相对紧扰动，给出本质谱；一维
Wronskian 或 Sturm 唯一性给离散特征值单重。平移能量 $\mu^2n^2$
即得 (2.2)。

置
$$
c(n)=\sqrt{\nu^2n^2+\frac14}-\nu n
=\frac1{4\bigl(\sqrt{\nu^2n^2+1/4}+\nu n\bigr)}.
\tag{2.3}
$$
它为正且随 $n$ 严格下降。由 (1.1) 准确得到
$$
c(4)=\frac1{2q},\qquad \ell_4=4\mu.
\tag{2.4}
$$
对任意整数 $n,j$，
$$
\ell_n-\mu n-j
=\left(\frac{pn}{q}-j-\frac12\right)+c(n).
\tag{2.5}
$$
由于 $q$ 为奇数，括号中的数的分子
$2pn-q(2j+1)$ 为奇整数，故
$$
\left|\frac{pn}{q}-j-\frac12\right|\ge\frac1{2q}.
\tag{2.6}
$$
当 $n>4$ 时，$0<c(n)<1/(2q)$，所以 (2.5) 不为零。$n=4$ 时，
只有 $j=0$ 可为零。若 $1\le n<4$，由
$$
\ell_n(\ell_n+1)=\mu^2n^2+\frac{\mu n^2}{4}
<\mu n(\mu n+1)
$$
得 $\ell_n<\mu n$，故此时整个 $L_n$ 严格正。于是唯一核确为 (1.4)；
直接代入或基态公式均给出 $y$。

这一步使用有理主相位的奇分母和明确的次阶项；没有诉诸不可量化的
Diophantine 常数。

## 3. 四重线性谱隙

对 $n\ge8$，(2.5)--(2.6) 及 $c$ 单调给
$$
|\ell_n-\mu n-j|\ge c(4)-c(8).
$$
用 (1.1) 可将右边准确化为
$$
c(4)-c(8)
=\frac{q^2-\sqrt{q^4-q^2+1}}{2q}
=\frac{q^2-1}{2q\bigl(q^2+\sqrt{q^4-q^2+1}\bigr)}
>\frac{q^2-1}{4q^3}=\Delta_q.
\tag{3.1}
$$
由于离散谱中 $\ell_n-j>0$，
$$
|E_{n,j}|
=|\ell_n-\mu n-j|\,(\ell_n-j+\mu n)
>\Delta_q\mu n.
$$
本质谱下端 $\mu^2n^2$ 也满足该界。
第四模的非零离散谱是
$j(8\mu-j)$，$1\le j<4\mu$，其最小值至少 $8\mu-1$；
这大于 $4\mu\Delta_q$，本质谱同样满足。因此 (1.5) 对全部
$4\mathbb N$ 非核谱成立，谱定理给 (1.6)。

若需要全部整数频率而非四重空间，仍有一个较松但线性的界
$$
|\lambda|>\frac{\mu n}{11q}
\tag{3.2}
$$
（第四模剔核）。事实上，$n\ge5$ 时
$$
c(4)-c(n)\ge \frac1{2q}-\frac1{40\nu}
=\frac{q^2-5}{10q(q^2-1)}>\frac1{11q},
$$
最后用 $q^2>45$。对 $n=1,2,3$，最低谱点满足
$$
\mu^2n^2-\ell_n^2
=\mu n(1-n/4)\frac{\mu n+\ell_n}{\mu n+\ell_n+1}
>\frac{\mu n}{8};
$$
这里 $\mu n>1$。第四模非核谱如前处理即可。

## 4. 导数、弱源与普通两分量源

以下固定 (1.7)。因为 $V\le\mu/4$，对 $L_nu=f$ 分部积分得
$$
\|u'\|_2^2
=\operatorname{Re}\langle f,u\rangle+n^2\int V|u|^2
\le \|f\|_2\|u\|_2+\frac{\mu n^2}{4}\|u\|_2^2.
$$
代入 $\|u\|_2\le66\|f\|_2/n$ 和 $n\ge4$，
$$
\|u'\|_2^2
\le\left(\frac{66}{4}+\frac{66^2\mu}{4}\right)\|f\|_2^2
<78^2\|f\|_2^2.
$$
又 $|V|\le\mu^2$，所以
$$
\|u''\|_2
\le\|f\|_2+n^2\mu^2\|u\|_2
\le \left(\frac14+66\mu^2\right)n\|f\|_2
<1953n\|f\|_2.
$$
这证明 (1.8)。第四模取核外逆时分部积分不变。

写 $R_n$ 为上述逆，第四模在源端也先作核外正交投影。
自伴性和 $\|\partial_xR_n\|\le78$ 给
$$
\|R_n\partial_x g\|_2\le78\|g\|_2.
\tag{4.1}
$$
这定义了普通 $L^2$ 源的弱导数输入，无需源有端点迹。还可付清
$$
\|\partial_xR_n\partial_x g\|_2\le92n\|g\|_2.
\tag{4.2}
$$
证明先取 $g$ 光滑紧支，令 $u=R_n\partial_xg$，$a=\|u'\|_2$，
$b=\|g\|_2$。核外投影不影响与 $u$ 的配对，因此能量恒等式和 (4.1)
给
$$
a^2\le ba+\frac{\mu n^2}{4}\,78^2b^2,
\qquad
a\le b+78n\sqrt{\mu/4}\,b<92nb.
$$
最后使用 $n\ge4$、$\mu/4=121/89<11/8$；稠密性推广至全部 $L^2$。

现在考虑真实一阶系统
$$
x'=-inVy+g_1,\qquad y'=-inx+g_2.
\tag{4.3}
$$
消元恰为
$$
L_ny=in g_1-g_2',\qquad
y=R_n(in g_1-g_2'),\qquad x=\frac{i}{n}(y'-g_2).
\tag{4.4}
$$
对 $n=4$，完整兼容条件为
$$
in\int_{\mathbb R}\overline y_4\,g_1
+\int_{\mathbb R}\overline {y_4'}\,g_2=0,
\qquad y_4=\operatorname{sech}^{4\mu}x,
\tag{4.5}
$$
并以 $y\perp y_4$ 固定核；对其余四重模无需兼容条件。
由 (1.8)、(4.1)--(4.2)，
$$
\|y\|_2\le66\|g_1\|_2+78\|g_2\|_2,\qquad
\|x\|_2\le78\|g_1\|_2+93\|g_2\|_2.
$$
系数矩阵的 Frobenius 范数平方为 $25173<159^2$，故
$$
\boxed{\quad
\|(x,y)\|_{L^2_x}\le159\|(g_1,g_2)\|_{L^2_x}.
\quad}
\tag{4.6}
$$
先对光滑源代回 (4.3)，再由 (4.6) 和方程通过普通 $L^2$ 极限；
各模解属于 $H^1$，因此这是实际一阶系统的解。逐模唯一性来自标量
核分类。所有 Fourier 模的同一常数可直接平方求和，也可乘任意固定
角频权后求和。因此 (4.6) 是径向背景的同宽 ordinary-source 逆，
没有对第二分量源索取一阶径向导数。

## 5. 一个真实的角模耦合一阶扰动门

令 $\mathcal H$ 为 $L^2(\mathbb R\times S^1)$ 中只含非零
$4\mathbb Z$ 模的闭子空间，角变量使用通常归一的 Fourier 基。
定义自伴直和算子
$$
\mathcal L=-\partial_x^2+V(x)\partial_\theta^2,\qquad
K=\ker\mathcal L
=\operatorname{span}\{y(x)e^{4i\theta},y(x)e^{-4i\theta}\}.
$$
以 $\Pi$ 表示到 $K$ 的正交投影。自然定义域是直和图范数定义域，
不预设其为全空间 $H^2$。令
$$
\mathcal R=(\mathcal L+\Pi)^{-1}.
$$
核外部分由 (1.8) 控制；核上的逆为恒等，而
$\|y'\|_2\le4\mu\|y\|_2<78\|y\|_2$。故
$$
\|\mathcal R\|\le\frac{33}{2},\qquad
\|\partial_x\mathcal R\|\le78,\qquad
\|\partial_\theta\mathcal R\|\le66.
\tag{5.1}
$$
这些整模界也可从 $L_4+\Pi_4$ 的能量恒等式直接获得：
其谱逆仍满足 $66/n$，而能量中的 $-\|\Pi_4u\|_2^2$ 只改善一阶估计。
第三式在核上仅需常数 $4$。二阶估计仍可取 (1.8) 的 $1953n$，
因为添加的投影至多再增加一个 $\|f\|_2$，而
$1/2+66\mu^2<1953$。

设 $b_0,b_x,b_\theta$ 为有界、$\pi/2$ 周期的系数，允许依赖
$(x,\theta)$，并定义
$$
\mathcal B u=P_{\ne0}
\bigl(b_0u+b_x\partial_xu+b_\theta\partial_\theta u\bigr).
$$
则即使它耦合无限多个角模，仍有
$$
\|\mathcal B\mathcal R\|\le
\kappa:=
\frac{33}{2}\|b_0\|_\infty+
78\|b_x\|_\infty+
66\|b_\theta\|_\infty.
\tag{5.2}
$$
当 $\kappa<1$ 时，
$$
(\mathcal L+\Pi+\mathcal B)^{-1}
=\mathcal R(I+\mathcal B\mathcal R)^{-1}
\tag{5.3}
$$
由同一 $L^2$ 空间中的 Neumann 级数严格定义，其 $L^2$、一阶径向、
一阶角向范数依次至多
$$
\frac{33/2}{1-\kappa},\qquad
\frac{78}{1-\kappa},\qquad
\frac{66}{1-\kappa}.
$$
这里添加 $\Pi$ 是一个明确的有限秩增广算子，不是把真实核删掉后
声称物理方程自动可解。实际均值列及第四模兼容仍需识别。
等价地，可在核外求解并以 $K$ 值未知量补充源，再另付该未知量由
实际均值方向实现的条件。

**边界。** (5.2) 不适用于二阶项
$b_{xx}u_{xx}+2b_{x\theta}u_{x\theta}+b_{\theta\theta}u_{\theta\theta}$。
即使本径向逆增益一阶，$\partial_\theta^2\mathcal R$ 仍无界。
具体取 $n=4(1+q\ell)$、$j=4p\ell$，$\ell=1,2,\ldots$。由 (2.5)，
$\ell_n-\mu n-j=-1/(2q)+c(n)$，所以对应真特征值
$$
E_{n,j}=\frac{\mu}{q}n+O(1).
$$
在其归一特征向量上，
$\|\partial_\theta^2\mathcal R\|$ 的相应比值为
$n^2/|E_{n,j}|\to\infty$。因此不能仅凭二阶主系数的 $L^\infty$
小量直接套 (5.2)。后续若能对实际算子作合法主符号归一化，使余项
只是一阶，则本节提供完全支付的同宽逆接口；本文尚未构造该归一化。

## 6. 同一个势的闭 $C^2$ 旋转背景和非刚体场

取正偶初值问题
$$
h''+Vh=0,\qquad h(0)=1,\quad h'(0)=0.
\tag{6.1}
$$
其解在全实线正。事实上 $L_1$ 的谱下端
$\mu^2-\ell_1^2>0$；若 $h$ 有首正零点，偶性在两首零点之间给
非零的零 Dirichlet 解，零延拓后的 $H^1$ 函数使 $L_1$ 二次型为零，
与严格正性矛盾。

当 $x$ 足够大时，$h''/h=\mu^2-\nu^2\operatorname{sech}^2x>\mu^2/2$。
此后 $h'$ 必最终变正：否则正凸解下降到零，比较原理给指数衰减，
偶延拓将成为 $L_1$ 的非零 $L^2$ 零解，仍矛盾。
对最终正的 $w=h'/h$，Riccati 方程
$w'=\mu^2-\nu^2\operatorname{sech}^2x-w^2$
与任意两个常数势 logistic 方程比较，得
$$
\frac{h'}h\longrightarrow\mu,\qquad
\frac{h''}h\longrightarrow\mu^2.
\tag{6.2}
$$
特别 $h$ 至少指数增长。

定义
$$
a=h^{-1},\qquad z(x)=\int_0^x h^{-2},\qquad
X(x,\theta)=a(x)e_r(\theta)+z(x)e_z.
\tag{6.3}
$$
内部 $z_x=h^{-2}>0$，故没有自交；两端高度和弧长有限。
在上极点以 $a$ 为径向图坐标，
$$
z_a=-\frac1{h'},\qquad
\frac{z_a}{a}=-\frac h{h'}\longrightarrow-\frac1\mu,\qquad
z_{aa}=-\frac{h''h^2}{(h')^3}\longrightarrow-\frac1\mu.
\tag{6.4}
$$
这正是两个 Cartesian Hessian 特征值趋于同一有限值的条件，
所以补两极后得到真正闭 $C^2$ 嵌入球面。其真实 Sturm 势就是
$-h''/h=V$，没有把独立算子强加给不相关的几何。

令
$$
U=\frac yh,\qquad T=-\frac U4,\qquad
W=\frac{h'}h\,y-\frac{y'}{16},
$$
$$
Z=U\cos4\theta\,e_r+T\sin4\theta\,e_\theta
+W\cos4\theta\,e_z.
\tag{6.5}
$$
把 (6.5) 代入 R16 (5) 的三条线性度量方程，前两条恒等为零，
第三条恰为 $L_4y/(8h^2)=0$。因此 $Z$ 是实际全局无穷小等距场。
$y$ 及固定阶 $x$ 导数以 $e^{-4\mu|x|}$ 衰减；
(6.2) 及其方程给 $h$ 和相应系数任意微小指数余量的界。
每次极点 Cartesian 求导至多增加一个 $O(h)$ 因子，故 $Z$ 的
前两阶 Cartesian 导数都趋零。补零给合法 $C^2$ 场及零二 jet。
腰圈法向分量为 $\cos4\theta$，所以它不是刚体速度场。
这里只固定两极，未把它们当成固定开握持区。

## 7. 作用量的准确值及后续范围

设 $x_0>0$ 是 $V$ 的唯一正零点。用 $t=\tanh x$，再用
$t=\sqrt{1-\mu^2/\nu^2}\sin\phi$，直接积分得到
$$
\boxed{\quad
\int_{-x_0}^{x_0}\sqrt{V(x)}\,dx
=\pi(\nu-\mu)=\frac{\pi p}{q}.
\quad}
\tag{7.1}
$$
具体地，中间积分为
$$
\nu\int_{-\pi/2}^{\pi/2}
\left(1-\frac{1-a^2}{1-a^2\sin^2\phi}\right)d\phi,
\qquad a^2=1-\mu^2/\nu^2.
$$
用 $\tan\phi$ 代换可得
$\int_{-\pi/2}^{\pi/2}(1-a^2\sin^2\phi)^{-1}d\phi
=\pi/\sqrt{1-a^2}$，于是得到 (7.1)。
奇分母使半整数 Maslov 主相位避开全部整数角模；(2.3) 的准确余项
使第四模仍可共振而其余四重模具有线性谱隙。

R24 的“精确保作用量”思路可在这个新背景上另行使用，但仅保持
(7.1) 仍不自动证明被扰动算子的所有高频余项或非径向耦合受控。
本文新增的可直接使用模块是 (1.8)、普通源 (4.6) 及有限秩增广后的
一阶耦合门 (5.2)，不是有限幅非线性存在证明。


## 8. 对具体 $p=11$ 的强化：$17/n$、$20$、$504n$

对 (1.7) 的具体背景，可以使用四重频率的准确整除关系进一步改进
(1.8)，不是再估算同一个连续最坏分母。结论为
$$
\boxed{\quad
|\lambda|>\frac n{17},\qquad
\|R_nf\|_2\le\frac{17}{n}\|f\|_2,\quad
\|\partial_xR_nf\|_2\le20\|f\|_2,\quad
\|\partial_x^2R_nf\|_2\le504n\|f\|_2 .
\quad}
\tag{8.1}
$$
第四模仍在 $y^\perp$ 上取逆。

### 8.1 准确的最危险频率

写 $n=4r$。对于离散谱指数 $j$，置
$$
M=8pr-q(2j+1)\in2\mathbb Z+1,\qquad
\delta=\ell_n-\mu n-j=\frac M{2q}+c(n).
\tag{8.2}
$$
若 $M\ge1$，则 $\delta>1/(2q)$，故
$$
|E_{n,j}|=\delta(2\mu n+\delta)>\frac{\mu n}{q}.
$$
若 $M\le-3$，由 $c(n)\le c(4)=1/(2q)$ 得
$d:=-\delta\ge1/q$。离散谱的 $\ell_n-j>0$ 又给 $d<\mu n$。
函数 $d(2\mu n-d)$ 在 $0<d<\mu n$ 上严格增加，故
$$
|E_{n,j}|\ge\frac1q\left(2\mu n-\frac1q\right)
>\frac{\mu n}{q}.
$$
这里 $\mu n>1/q$。而 $\mu/q=484/7921>1/17$。

只剩 $M=-1$。由 $q=8p+1$，此时
$$
q(r-2j-1)=r-1.
$$
因此 $r=1+q\ell$、$j=4p\ell$。$\ell=0$ 恰为第四模核；
其余情形 $\ell\ge1$，所以
$$
n\ge4(q+1)=360.
$$
由 (2.3)，
$$
c(n)<\frac1{8\nu n}
\le\frac1{32\nu(q+1)}
<\frac1{2q(q-1)}.
$$
所以
$$
d=\frac1{2q}-c(n)>
d_0:=\frac{q-2}{2q(q-1)}.
$$
再用 $d(2\mu n-d)$ 的单调性，
$$
\frac{|E_{n,j}|}{n}>
2\mu d_0-\frac{d_0^2}{4(q+1)}
=\frac{592879799}{9814435840}
>\frac1{17}.
\tag{8.3}
$$
最后的不等式只需整数比较
$17\cdot592879799-9814435840=264520743>0$。
第四模非零谱及所有本质谱均显然满足同一界，于是完成 (8.1) 的谱部分。

### 8.2 导数、普通源与一阶耦合

把第 4 节能量证明中的 $66$ 换成 $17$：
$$
\|u'\|_2^2
\le\left(\frac{17}{4}+\frac{17^2\mu}{4}\right)\|f\|_2^2
<20^2\|f\|_2^2,\qquad
\frac14+17\mu^2<504.
$$
因此导数常数如 (8.1)。
弱源估计相应变为
$$
\|R_n\partial_xg\|_2\le20\|g\|_2,\qquad
\|\partial_xR_n\partial_xg\|_2\le24n\|g\|_2.
\tag{8.4}
$$
第二式由
$a\le b+20n\sqrt{\mu/4}\,b<24nb$
直接得到。

第 4 节的 ordinary-source 系统于是满足
$$
\|y\|_2\le17\|g_1\|_2+20\|g_2\|_2,\qquad
\|x\|_2\le20\|g_1\|_2+25\|g_2\|_2.
$$
由于 $17^2+20^2+20^2+25^2=1714<42^2$，
$$
\boxed{\quad \|(x,y)\|_2\le42\|(g_1,g_2)\|_2.\quad}
\tag{8.5}
$$
第四模的完整兼容和规范仍是 (4.5)，没有改变。

同样，添加核投影后的
$\mathcal R=(\mathcal L+\Pi)^{-1}$ 保留上述模态和能量界。
因此第 5 节可以采用更强的门
$$
\boxed{\quad
\kappa_{\rm sharp}
=\frac{17}{4}\|b_0\|_\infty+
20\|b_x\|_\infty+
17\|b_\theta\|_\infty<1.
\quad}
\tag{8.6}
$$
该改进仍只覆盖一阶耦合，未改变二阶主符号限制。
此前使用 $66,78,1953,159$ 的结果继续成立，可在需要时独立替换为
本节更小的常数。
