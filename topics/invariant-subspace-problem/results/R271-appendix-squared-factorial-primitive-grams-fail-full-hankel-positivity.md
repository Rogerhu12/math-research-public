# R271 附录：平方阶乘 primitive Gram 不满足全 Hankel 正性

日期：2026-11-13（UTC）。作者：kernel_resume_1cf / Astra-ISP-1cf8c51d；AI 辅助：GPT-6 Astra Pro。
状态：已证明；root 与 boundary 全文独立核查。

本稿排除把真实最小逆 Gram 归一化为 $(k!)^2H_k$ 后，再对它使用全部 Hankel 正性或正算子值矩表示的路线。反例先落在实际有限正异权布尔模型，再用已付的高阶暗对双界传到原连续尾 $D_m=\sum_{j\ge m}(j+1)^{-2}E_j$。

这比相邻两个高度的比较强得多。本稿不否定尚未证明的相邻平方常数上界 $4$，不把高阶 Hankel 负块当成某个相邻 $2\times2$ 负块，也没有把构造源识别为原边界向量产生的窄 Schur 返回源。

## 1. 真实最小逆及待排除的强性质

设 $D$ 为一个正异权布尔删除算子，$\mathcal H_s$ 为第 $s$ 孔层，
$$
K_s=\ker D\cap\mathcal H_s.
$$
对一个确在 $D^k$ 像中的 $g\in K_s$，令 $J_kg$ 为方程
$$
D^kv=g,\qquad v\in\mathcal H_{s+k}
$$
的真正最小范数解，并令
$$
h_k(g)=\|J_kg\|^2,\qquad J_0g=g.
\tag{1.1}
$$
在有限层或存在有界最小逆的情形，写 $H_k=J_k^*J_k$；
在 $D^k$ 满射到目标层的有限模型中，公式是
$$
H_k=P_{K_s}\,[D^k(D^*)^k|_{\mathcal H_s}]^{-1}|_{K_s}.
\tag{1.2}
$$
若有限目标层非满射，则只在实际像上取 Moore–Penrose 逆；以下真空模型的目标是一维且满射。这里始终先取真正的最小逆，再压缩到 primitive 源；不交换这两个步骤。

平方阶乘归一为
$$
\mathcal G_k=(k!)^2H_k.
\tag{1.3}
$$
待排除的强性质要求每个合法有限 Hankel 块均半正定：
$$
\boxed{[\mathcal G_{i+j}]_{i,j=0}^{L}\ge0.}
\tag{1.4}
$$
在同一源 $g$ 上，它特别要求
$$
\sum_{i,j=0}^L c_i c_j(i+j)!^2h_{i+j}(g)\ge0
\quad\text{对所有实 }c_i.
\tag{1.5}
$$
任何正标量或正算子值测度的完整矩表示都蕴含 (1.4)。
下面直接否定 (1.5)，只用具有显式原像的同一 primitive 源。

## 2. 两个强位与有限弱池的准确真空 Gram

取两个权为 1 的位和 $N$ 个权为 $N^{-1/2}$ 的位：
$$
D^{(N)}=E_1+E_2+N^{-1/2}\sum_{j=3}^{N+2}E_j.
\tag{2.1}
$$
令 $\Omega$ 为活跃真空。它是单位 primitive 源，且目标层 $\mathcal H_0=\mathbb C\Omega$。
对 $0\le k\le N+2$，
$$
(D^{(N)*})^k\Omega
=k!\sum_{|I|=k}b_I e_I,\qquad
\|(D^{(N)*})^k\Omega\|^2=(k!)^2e_k(b^2).
$$
因此真正最小逆准确为
$$
J_k\Omega=
\frac{(D^{(N)*})^k\Omega}{(k!)^2e_k(b^2)},\qquad
h_k^{(N)}=\frac1{(k!)^2e_k(b^2)}.
\tag{2.2}
$$
这是整个第 $k$ 孔层中的最小解，因为它在实际伴随像中并解原方程。

此处
$$
e_k(b^2)
=\binom NkN^{-k}
+2\binom N{k-1}N^{-(k-1)}
+\binom N{k-2}N^{-(k-2)},
\tag{2.3}
$$
不合法二项式按零解释。对每个固定 $k$，令 $N\to\infty$，得到
$$
e_k(b^2)\longrightarrow
\frac1{k!}+\frac2{(k-1)!}+\frac1{(k-2)!}
=\frac{k^2+k+1}{k!}.
$$
所以归一矩的逐项极限是
$$
\boxed{
(k!)^2h_k^{(N)}\longrightarrow
m_k:=\frac{k!}{k^2+k+1},\qquad k\ge0.
}
\tag{2.4}
$$
这里只将有限模型的数值取极限；不把无穷多个越来越小的位当成一个已经构造好的实际算子。

## 3. 极限矩的显式有符号密度

置
$$
\beta=\frac{\sqrt3}{2}.
$$
先在 $(0,1)$ 上定义有限实有符号测度
$$
d\nu(t)=\frac1\beta\,t^{-1/2}
\sin\!\bigl(\beta\log(1/t)\bigr)\,dt.
\tag{3.1}
$$
作 $u=-\log t$，直接积分得
$$
\int_0^1t^k\,d\nu(t)
=\frac1\beta\int_0^\infty
e^{-(k+1/2)u}\sin(\beta u)\,du
=\frac1{k^2+k+1}.
\tag{3.2}
$$

将它与单位指数密度作乘法卷积，定义
$$
\boxed{
f(x)=\frac1\beta
\int_0^1 t^{-3/2}e^{-x/t}
\sin\!\bigl(\beta\log(1/t)\bigr)\,dt,\qquad x>0.
}
\tag{3.3}
$$
这是实的、在 $(0,\infty)$ 上连续的函数。
对每个 $0<c<1$，Tonelli 估计给
$$
\begin{aligned}
\int_0^\infty e^{cx}|f(x)|\,dx
&\le\frac1\beta\int_0^1t^{-3/2}
\int_0^\infty e^{-x(1/t-c)}\,dx\,dt\\
&=\frac1\beta\int_0^1\frac{t^{-1/2}}{1-ct}\,dt
\le\frac2{\beta(1-c)}<\infty.
\end{aligned}
\tag{3.4}
$$
所有后续换序因此有绝对积分依据。特别
$$
\boxed{
\int_0^\infty x^kf(x)\,dx
=k!\int_0^1t^k\,d\nu(t)=m_k.
}
\tag{3.5}
$$

这个密度确实取负值。令 $z=1/2+i\beta$，以积分定义上不完全 Gamma：
$$
\Gamma(z,x)=\int_x^\infty u^{z-1}e^{-u}\,du.
$$
在 (3.3) 作 $u=x/t$，得到准确式
$$
f(x)=\frac{x^{-1/2}}\beta
\operatorname{Im}\!\left[x^{-i\beta}\Gamma(1/2+i\beta,x)\right].
\tag{3.6}
$$
由 $\operatorname{Re}z=1/2$，
$$
\Gamma(z,x)=\Gamma(z)+O(x^{1/2}),
$$
故
$$
\boxed{
f(x)=\frac{x^{-1/2}}\beta
\operatorname{Im}\!\left[\Gamma(1/2+i\beta)e^{-i\beta\log x}\right]
+O(1)
\quad(x\downarrow0).
}
\tag{3.7}
$$

这里振荡系数非零有具体标准依据。
[NIST DLMF 5.5.3](https://dlmf.nist.gov/5.5.E3) 的 Gamma 反射公式及 Euler 积分的共轭关系给
$$
\boxed{
|\Gamma(1/2+i\beta)|^2
=\frac{\pi}{\cosh(\pi\beta)}>0.
}
\tag{3.8}
$$
所以 (3.7) 的主项随 $\log x$ 无穷次变号，幅度为固定正数乘 $x^{-1/2}$。
其 $O(1)$ 余项不能抵消充分小 $x$ 处的正、负峰。
因此存在一个闭区间 $I\subset(0,\infty)$，使 $f<0$ 在 $I$ 上成立，且
$$
\int_I f(x)\,dx<0.
\tag{3.9}
$$

## 4. 由负密度得到有限多项式负二次型

为避免把一个有符号表示直接误当成“没有其他正表示”，这里给出所需密度论证。

**引理。** 若有限正测度 $\mu$ 支撑在 $[0,\infty)$，并对某个 $a>0$ 有
$\int e^{2ax}\,d\mu(x)<\infty$，则实多项式在实 $L^2(\mu)$ 中稠密。

**证明。** 设 $h\in L^2(\mu)$ 与全部多项式正交。
Cauchy--Schwarz 给
$$
\int e^{ax}|h(x)|\,d\mu(x)<\infty.
$$
因此
$$
F(z)=\int e^{zx}h(x)\,d\mu(x)
$$
在半平面 $\operatorname{Re}z<a$ 解析。
正交性给 $F^{(k)}(0)=0$ 对全部 $k$ 成立；
解析延拓使 $F$ 在该连通半平面恒为零。
特别有限有符号测度 $h\mu$ 的傅里叶变换处处为零。
傅里叶唯一性可直接用高斯卷积验证：其与任意高斯核的卷积的傅里叶积分均为零，再令高斯形成近似单位，得 $h\mu=0$。
所以正交补为零，证明稠密。复情形同理，取实部得到实多项式逼近。$\square$

应用于
$$
d\mu(x)=|f(x)|\,dx.
$$
(3.4) 支付所需指数矩。取实多项式 $p_n\to\mathbf1_I$ 于 $L^2(\mu)$。
由于
$$
\|p_n^2-\mathbf1_I\|_{L^1(\mu)}
\le
\|p_n-\mathbf1_I\|_{L^2(\mu)}
\bigl(\|p_n\|_{L^2(\mu)}+\|\mathbf1_I\|_{L^2(\mu)}\bigr)
\longrightarrow0,
$$
(3.9) 给
$$
\int p_n(x)^2f(x)\,dx\longrightarrow\int_I f(x)\,dx<0.
$$
于是存在一个固定有限实多项式
$$
p(x)=\sum_{i=0}^L c_i x^i
$$
满足
$$
\boxed{
\sum_{i,j=0}^L c_i c_jm_{i+j}
=\int p(x)^2f(x)\,dx<0.
}
\tag{4.1}
$$
这已是一条完整的有限 Hankel 反证，不依赖浮点矩阵特征值、数值截断或某个大阶行列式的符号输出。

特别 $m_k$ 不可能是正测度的矩序列：若存在正表示，左侧会等于正测度下的 $p^2$ 积分。
更重要的是，(4.1) 给下一节可传递的固定有限测试。

## 5. 反例落到真实有限布尔模型

固定 §4 得到的同一个 $L$ 和 $c_0,\ldots,c_L$。
由 (2.4) 的有限项收敛，
$$
\sum_{i,j=0}^L c_i c_j(i+j)!^2 h_{i+j}^{(N)}
\longrightarrow
\sum_{i,j=0}^L c_i c_jm_{i+j}<0.
$$
因此可固定一个充分大的有限 $N$，同时保证
$N+2\ge2L$，使
$$
\boxed{
\sum_{i,j=0}^L c_i c_j(i+j)!^2 h_{i+j}^{(N)}<0.
}
\tag{5.1}
$$
所有所需最小逆都处于真实有限模型的合法孔层。
这否定正异权布尔删除算子的普遍全 Hankel 性质 (1.4)。

逻辑顺序是：先用解析证明取得一个有限多项式，再固定一个足够大的有限弱池。
不需要对多项式次数、池大小或最小特征值作任何不受控的数值极限。

## 6. 同一个源的全部固定阶暗对传递

以下使用并重述[全高度平方下界稿 §§4—5](R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md)的真实双界，以保证各阶不更换源。

设活跃算子 $D_{\rm a}$ 作用于一个固定有限布尔空间；
背景是相邻暗对及远尾真空，单位向量为 $\chi$，满足
$$
D_{\rm b}\chi=0.
$$
对每个背景组件的上升算子 $B_\nu$ 和基向量 $\chi_\nu$，有
$$
B_\nu\chi_\nu\perp\chi_\nu,\qquad
B_\nu^2\chi_\nu=0,\qquad d_\nu=\|B_\nu\chi_\nu\|.
$$
置 $\delta^2=\sum_\nu d_\nu^2$。不同激活组件集合的张量向量正交，准确给
$$
\boxed{
\|(D_{\rm b}^*)^\ell\chi\|^2
=(\ell!)^2e_\ell(d_\nu^2)\le\ell!\,\delta^{2\ell}.
}
\tag{6.1}
$$
原连续尾的算子级数按范数收敛，故可先证明有限组件公式，再取极限。

令
$$
\widehat D=D_{\rm a}\otimes I+I\otimes D_{\rm b},
\qquad g=\Omega_{\rm a}\otimes\chi.
$$
同一个 $g$ 用于所有阶。对每个固定 $k\le2L$，在活跃真空目标层置
$$
w_k=[D_{\rm a}^k(D_{\rm a}^*)^k]^{-1}\Omega_{\rm a},
\quad
v_k=(D_{\rm a}^*)^kw_k,\quad
a_k=\|v_k\|^2.
$$
$v_k\otimes\chi$ 是 $\widehat D^kx=g$ 的实际试探解。
全空间解集是非空闭仿射集，因而有唯一最小解；记其范数平方为
$a_k^{\rm full}$。全部解和极小化均取指定总孔层。

取真实对偶测试 $w_k\otimes\chi$。
二项式展开中不同背景上升阶对应不同活跃孔数，所以各项正交。
由 (6.1) 得
$$
\|(\widehat D^*)^k(w_k\otimes\chi)\|^2
\le a_k+
\sum_{\ell=1}^k\binom{k}{\ell}^2\ell!\,
\|(D_{\rm a}^*)^{k-\ell}w_k\|^2\delta^{2\ell}.
$$
再用 $\langle\Omega_{\rm a},w_k\rangle=a_k$ 与 Cauchy--Schwarz，
$$
\boxed{
\frac{a_k^2}{
a_k+\displaystyle\sum_{\ell=1}^k\binom{k}{\ell}^2\ell!\,
\|(D_{\rm a}^*)^{k-\ell}w_k\|^2\delta^{2\ell}}
\le a_k^{\rm full}\le a_k.
}
\tag{6.2}
$$
对固定有限活跃参数的一个紧邻域和全部有限阶 $k\le2L$，
各活跃 Gram 严格正定，故
$$
\boxed{a_k^{\rm full}=a_k+O(\delta^2)\quad(0\le k\le2L)}
\tag{6.3}
$$
有共同有限常数。
无需全空间核投影连续、全层最小逆有界或各阶换一个 primitive 源。

## 7. 嵌入原连续尾及几何归一

固定 §5 的有限 $N$、$L$ 和多项式系数。
在原尾
$$
D_m=\sum_{j\ge m}(j+1)^{-2}E_j,\qquad b_m=(m+1)^{-2}
$$
中，先归一化
$$
\widehat D_m=D_m/b_m.
$$
选两个强活跃位 $m,m+1$；再选 $N$ 个连续弱活跃位
$[\ell_m,\ell_m+N)$，其中
$$
\ell_m+1=N^{1/4}(m+1)+O(1),\qquad
\ell_m-m-2\text{ 为偶数}.
\tag{7.1}
$$
向上调整不足2个整数即可满足奇偶要求。
固定 $N>1$ 后，两簇对充分大 $m$ 分离。
实际归一活跃权趋于
$$
(1,1,\underbrace{N^{-1/2},\ldots,N^{-1/2}}_{N\text{ 位}}).
\tag{7.2}
$$

对每个整数 $s\ge4\cdot2^m$，置
$$
K=m+2s+N+2.
$$
将两个背景区间
$$
[m+2,\ell_m),\qquad [\ell_m+N,K)
$$
分别按相邻位配成暗对。
两段均有偶数个位，合计恰有 $2s$ 个背景位，因此正好形成 $s$ 个暗对。
在 $j\ge K$ 取无孔真空。
每对权 $b_j,b_{j+1}$ 的暗态是
$$
\chi_j=
\frac{b_{j+1}e_j-b_je_{j+1}}{\sqrt{b_j^2+b_{j+1}^2}},
$$
它被该对的真实删除消去。故
$$
\boxed{
g_{m,s}=\Omega_{\rm a}\otimes\chi_{m,s}
\in\ker D_m\cap\mathcal H_s,\qquad \|g_{m,s}\|=1.
}
\tag{7.3}
$$
对每个固定 $(m,s)$，(7.3) 是全部阶共用的唯一源。

一个暗对的背景上升平方费用为
$$
\frac{(b_j^2-b_{j+1}^2)^2}{b_j^2+b_{j+1}^2}.
$$
用 $b_j=(j+1)^{-2}$ 和均值估计
$|b_j^2-b_{j+1}^2|\le4(j+1)^{-5}$，
每对至多 $16(j+1)^{-6}$。
再加上 $j\ge K$ 的真空尾并除以 $b_m^2$，得到
$$
\boxed{
\delta_{m,s}^2
\le \frac{C}{m+1}+\frac{(m+1)^4}{3K^3}
\longrightarrow0
}
\tag{7.4}
$$
对所有 $s\ge4\cdot2^m$ 一致。
所需高阶背景费用用 (6.1)，不改用可能很大的背景算子范数幂。

活跃真空的各阶有限 Gram 在 (7.2) 附近为非零标量，
其最小逆和 (6.2) 中的有限量均连续。
因此，令 $\widehat h_k(m,s)$ 为
$\widehat D_m^kx=g_{m,s}$ 的真正最小解范数平方，
(6.2)—(7.4) 给
$$
\boxed{
\widehat h_k(m,s)\longrightarrow h_k^{(N)}
\quad(0\le k\le2L)
}
\tag{7.5}
$$
对全部 $s\ge4\cdot2^m$ 一致。
由 (5.1)，充分大 $m$ 时，对每个这样的 $s$，
$$
\boxed{
\sum_{i,j=0}^L c_i c_j(i+j)!^2
\widehat h_{i+j}(m,s)<0.
}
\tag{7.6}
$$

最后还原原几何尺度。对同一个 $g_{m,s}$，
$$
\widehat h_k(m,s)=b_m^{2k}h_k^{D_m}(g_{m,s}).
\tag{7.7}
$$
所以 (7.6) 就是原矩在系数
$$
\widetilde c_i=c_i b_m^{2i}
$$
上的负二次型。
等价地，归一后的 Hankel 块由原块经正对角
$\operatorname{diag}(b_m^{2i})$ 同余得到。
因此归一化不改变全 Hankel 正性的真伪。

这证明原连续尾在任意充分高的合法出生层上，也不具有 (1.4) 的普遍性质。
全部有限矩都已由显式试探原像支付；结论不依赖未证的全层逆范数。

## 8. 对后续路线的准确限制

本稿确实排除了两种较强设想：

- 正异权有限布尔 primitive Gram 的平方阶乘序列普遍满足全部 Hankel 正性；
- 原连续尾的同一序列普遍有正标量或正算子值测度的完整矩表示。

证明甚至从一个真空源的有限模型开始，随后保持同一暗对源传到真实尾；它不是“不交换的算子也许有问题”的形式反对。

但全 Hankel 正性远强于逐个相邻的 $2\times2$ 块正性。
本稿没有给出
$$
\mathcal G_{k+1}\ge\mathcal G_k\mathcal G_{k-1}^{-1}\mathcal G_k
$$
的反例，也没有推翻相邻第一下降的候选平方常数 $4$。
此前[全高度平方下界稿](R271-appendix-two-cluster-minimal-inverses-and-squared-all-height-comparison-lower-bounds.md)的必要下界仍保持原范围。

源 $g_{m,s}$ 是完整 primitive 核中的实际向量，尚未与原正常见证的特定窄 Schur 源匹配。
因此，本稿只关闭上述全矩表示证明路线，不宣称原返回费用、真实正常见证或不变子空间问题已经完成。

## 9. 出生阶乘归一同样不能给一般 primitive 全矩表示

本节把 §7 的同源负型用于一个不同的、在后续比较中出现的归一。
[R239 饱和两簇固定线](R239-appendix-saturated-two-cluster-primitive-stieltjes-moments.md) 已在其指定一维源上证明
$s!\mathcal G_k/(s+k)!$ 的正矩表示。以下证明这个性质不能普遍推广到整个 primitive 核；两结论的源范围不同。

在原第 $s$ 出生层上，定义新的序列
$$
\mathcal M_{s,k}=\frac{s!}{(s+k)!}(k!)^2H_k.
\tag{9.1}
$$
**结论。** 存在固定有限阶 $L$，使对所有充分大的 $m$ 及每个
$s\ge4\cdot2^m$，原连续尾 $D_m$ 上的同一个 §7 源 $g_{m,s}$ 满足：
$\bigl[\langle\mathcal M_{s,i+j}g_{m,s},g_{m,s}\rangle\bigr]_{i,j=0}^L$
不是半正定矩阵。因此即使加入出生阶乘因子，也没有一般 primitive 的完整正矩或 POVM 表示。

**证明。** 保留 §§4–7 的固定有限 $L$、实系数 $c_i$、有限活跃弱池 $N$。
记
$$
\gamma_k^{(N)}=(k!)^2h_k^{(N)},\qquad
\sum_{i,j=0}^L c_ic_j\gamma_{i+j}^{(N)}=-\Delta<0.
$$
这里 $\Delta>0$ 固定，不随 $m,s$ 改变。

对 $s\ge1$、固定非负整数 $k$，置
$$
a_{s,k}=s^k\frac{s!}{(s+k)!}
=\prod_{h=1}^k\left(1+\frac hs\right)^{-1}.
$$
空乘积为1。对全部 $0\le k\le2L$，
$$
0<a_{s,k}\le1,\qquad
|a_{s,k}-1|\le \frac{k(k+1)}{2s}.
\tag{9.2}
$$
后一式可用 $1-\prod_h(1+x_h)^{-1}\le\sum_hx_h$ 逐因子归纳证明。
因此 (9.2) 对 $s\ge4\cdot2^m$ 一致趋于0。

由 (7.5) 的全部固定阶、同源、一致收敛，
$$
a_{s,k}(k!)^2\widehat h_k(m,s)\longrightarrow\gamma_k^{(N)}
\quad(0\le k\le2L)
\tag{9.3}
$$
对所有这些 $s$ 一致；试探上界 (6.2) 同时给所需的有限一致有界性。
于是充分大 $m$ 时，
$$
\sum_{i,j=0}^L
c_ic_j\,a_{s,i+j}(i+j)!^2\widehat h_{i+j}(m,s)
<-\Delta/2
\tag{9.4}
$$
对全部 $s\ge4\cdot2^m$ 成立。

再用 (7.7)，左侧准确等于
$$
\sum_{i,j=0}^L
\widetilde c_i\widetilde c_j
\frac{s!}{(s+i+j)!}(i+j)!^2h_{i+j}^{D_m}(g_{m,s}),
\qquad
\widetilde c_i=c_i(s\,b_m^2)^i.
$$
这只是正对角 $\operatorname{diag}((s b_m^2)^i)$ 的同余，没有改变 Hankel 正性的真伪。
它给 (9.1) 的实际有限负二次型。证明完毕。

这项加强仍然只否定完整矩表示。
它没有证明或否定较弱的相邻算子序
$$
\mathcal G_k\mathcal G_{k+1}^{-1}\mathcal G_k
\le\frac{s+k}{s+k+1}\mathcal G_{k-1},
$$
也没有否定常数1的更弱式或实际高度2平方常数4。
指定饱和两簇的一维正矩结论完整保留，原窄 Schur 返回源的匹配仍然未得。

