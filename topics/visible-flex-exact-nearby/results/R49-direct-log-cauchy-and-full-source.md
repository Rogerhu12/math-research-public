# R49：真实严格区的同 log 宽 Cauchy、完整源与反向估计

2026-11-12，independent-audit。

**状态：已证明的实际算子估计。** 对一个真实有限径向区间上的
对称双曲系统，本篇在同一直接 log 角权上证明任意小正 Sobolev
损失的 Cauchy 与完整普通源估计。常数只由实际系数的明确 Fourier
和能量范数给出，不要求系数接近径向或主角图接近恒等。

证明保留实际变系数 symmetrizer。它不把权共轭后的 symmetrizer
当成自伴，而是在共轭方程中精确计入主、低阶交换子和变化的
Sobolev 阶。均值保留；反向传播及反号权通量对偶也一起给出。
这支付 R46 严格区加权 Cauchy/source 的一个真实输入，仍不代付
转折、正帽、全反馈低块或非线性闭族。

## 1. 系统、直接 log 权与实际输入

在 $x\in[0,L]$、$\theta\in\mathbb R/(2\pi\mathbb Z)$ 上，考虑
$$
\partial_xZ=\mathsf A(x,\theta)\partial_\theta Z
                       +\mathsf B(x,\theta)Z+F.
\tag{1.1}
$$
向量维数有限，矩阵可以复数；假设实际 Hermitian 矩阵
$\mathsf H$ 满足
$$
h_*I\le\mathsf H\le h^*I,\qquad
\mathsf H\mathsf A=(\mathsf H\mathsf A)^*,\qquad 0<h_*\le h^*<\infty.
\tag{1.2}
$$
所需径向导数可按弱导数理解；例如 $\mathsf H$ 关于 $x$ Lipschitz、
各系数连续或分段连续已足够。首先对角光滑对象证明，再按下面的
实际有限范数及有界延拓完成空间。

设
$$
\omega(t)=(\log(e+t))^{3/2}-1,\qquad
W_\rho(j)=e^{\rho\omega(|j|)},\qquad \rho\in\mathbb R,
$$
$$
\|z\|_{r,\rho}^2
=\sum_{j\in\mathbb Z}\langle j\rangle^{2r}W_\rho(j)^2|z_j|^2.
\tag{1.3}
$$
$\omega(0)=0$，它递增、凹，因
$$
\omega''(t)=\frac{3(1-2\log(e+t))}
 {4(e+t)^2\sqrt{\log(e+t)}}<0.
$$
故它次可加，特别
$|\omega(|k|)-\omega(|j|)|\le\omega(|k-j|)$。
这里的 $H^r_\rho$ 是完整 Fourier Hilbert 空间。$\rho<0$ 时它可能
含非分布元素；对此只声明从实际光滑数据得到的有界 Fourier
延拓，不把所有完成元素称为经典 PDE 解。

固定所用 Sobolev 窗口 $|r|\le S$，$S\ge0$。令
$$
w_l=2^{S/2}\langle l\rangle^S e^{|\rho|\omega(|l|)},
\quad
\mathfrak A(x)=\sum_{l\ne0}|l|w_l\|\mathsf A_l(x)\|,
\quad
\mathfrak B(x)=\sum_{l\ne0}w_l\|\mathsf B_l(x)\|.
\tag{1.4}
$$
矩阵 norm 是实际有限维算子 norm。另置
$$
C_H(x)=\frac12\sum_{l\ne0}
\log(\sqrt2\langle l\rangle)\|\mathsf H_l(x)\|,
\tag{1.5}
$$
$$
\Gamma(x)=\frac12\sup_\theta
\left\|\mathsf H^{-1/2}
\{\mathsf H_x-(\mathsf H\mathsf A)_\theta
            +\mathsf H\mathsf B+\mathsf B^*\mathsf H\}
\mathsf H^{-1/2}\right\|.
\tag{1.6}
$$
这些都必须针对同一个实际系统支付；其中 $\mathsf B$ 包括全部
低阶项。足够条件是所需系数在一个真实正复角 strip 上有一致界；
§7 给由 strip 界到 (1.4)–(1.5) 的显式有限和上界。

下面使用
$$
C_1(x)=3|\rho|\,\mathfrak A(x),\qquad
C_0(x)=(4+2S+6|\rho|)\mathfrak A(x)+2\mathfrak B(x).
\tag{1.7}
$$

## 2. 真实权交换子的完整矩阵估计

记 $\mathcal L e_j=\log\langle j\rangle\,e_j$，均值上为零。
令 $M_r e_j=\langle j\rangle^rW_\rho(j)e_j$。
对 $|r|\le S$，准确共轭差为
$$
\mathcal R_r
=[M_r,\mathsf A]\partial_\theta M_r^{-1}
                         +[M_r,\mathsf B]M_r^{-1}.
\tag{2.1}
$$

**引理 2.1。** 在完整角频空间上有
$$
\boxed{\quad
\|\mathcal R_rY\|_2
\le C_1(x)\|\mathcal L^{1/2}Y\|_2+C_0(x)\|Y\|_2.
\quad}
\tag{2.2}
$$
相同常数也适用于截断 log 权
$W_{\rho,R}(j)=\exp[\rho\omega(\min(|j|,R))]$，$R>0$。

**证明。** 记 $m_j=\langle j\rangle^rW_\rho(j)$。Peetre 与次可加性给
$$
\max(m_{j+l}/m_j,m_j/m_{j+l})\le w_l.
\tag{2.3}
$$
对 $l\ne0$，若 $|j|<2|l|$，则
$$
|j||m_{j+l}/m_j-1|\le4|l|w_l.
\tag{2.4}
$$
若 $|j|\ge2|l|$，从 $j$ 到 $j+l$ 的实线段不经过零，且
其绝对值在 $[|j|/2,3|j|/2]$ 内。对
$r\log\langle t\rangle+\rho\omega(|t|)$ 作实积分微分，使用
$$
|\partial_t\log\langle t\rangle|\le2/|j|,
$$
$$
|\partial_t\omega(|t|)|
\le\frac3{|j|}\left(\sqrt{\log\langle j\rangle}+2\right)
\tag{2.5}
$$
得到
$$
\left|\log\frac{m_{j+l}}{m_j}\right|
\le\frac{|l|}{|j|}
\left[2S+6|\rho|+3|\rho|\sqrt{\log\langle j\rangle}\right].
\tag{2.6}
$$
例如 (2.5) 由
$e+|t|\le(3/2)(e+|j|)$ 及
$\sqrt{\log(e+1)}+\sqrt{\log(3/2)}<2$ 直接推出。
再用 $|e^u-1|\le\max(1,e^u)|u|$ 和 (2.3)，合并两种情形给
$$
\boxed{\quad
|j||m_{j+l}/m_j-1|
\le |l|w_l
\left[(4+2S+6|\rho|)+3|\rho|\sqrt{\log\langle j\rangle}\right].
\quad}
\tag{2.7}
$$
$j=0$ 时左边为零，所以没有漏掉均值列。
低阶交换子的矩阵则用
$|m_{j+l}/m_j-1|\le2w_l$。

真实主矩阵条目为
$ij(\mathsf A_l)(m_{j+l}/m_j-1)$，低阶条目同理。
分别对输入序列 $|Y_j|$ 与
$\sqrt{\log\langle j\rangle}|Y_j|$ 作卷积 Young 不等式，给 (2.2)。
这是整个 Fourier 矩阵估计，不是只在某一频率锥上计算符号。

截断函数 $\omega_R(t)=\omega(\min(t,R))$ 仍递增、凹、次可加，
其几乎处处导数不超过 $\omega'(t)$；因此 (2.3)–(2.7) 及最终
常数完全不依赖 $R$。这是一个连续、绝对连续的权截断，不是
频率投影，也没有在 $|j|=R$ 把权跳回 $1$；导数的折角仍可用
同一个实线段积分，所以不存在另漏的频率边缘大项。$\square$

## 3. 真实 symmetrizer 与变化的 Sobolev 阶

不能在带权系统中假设 $M_r\mathsf H M_r^{-1}$ 自伴。
本篇对共轭未知量 $Y$ 继续使用实际点乘 $\mathsf H$ 作能量，
所以主共轭的全部误差恰为 (2.1)。变化的 Sobolev 阶另产生
$\mathcal L$，它与 $\mathsf H$ 的不交换费用如下。

**引理 3.1。** 对任意光滑 $Y$，
$$
\boxed{\quad
\operatorname{Re}\langle Y,\mathsf H\mathcal LY\rangle
\ge h_*\|\mathcal L^{1/2}Y\|_2^2-C_H(x)\|Y\|_2^2.
\quad}
\tag{3.1}
$$

**证明。** Hermitian 部分与
$\mathcal L^{1/2}\mathsf H\mathcal L^{1/2}$ 的矩阵差为
$$
\frac12(\mathsf H_{k-j})
\left(\sqrt{\log\langle k\rangle}
                  -\sqrt{\log\langle j\rangle}\right)^2.
\tag{3.2}
$$
因 $|\sqrt a-\sqrt b|^2\le|a-b|$ 以及
$$
|\log\langle k\rangle-\log\langle j\rangle|
\le\log(\sqrt2\langle k-j\rangle),
$$
卷积 Young 给差算子的 $L^2$ norm 至多 (1.5)。
$\mathsf H\ge h_*I$ 给 (3.1)。均值也包含在同一个矩阵式里。
$\square$

现固定 $\varepsilon>0$ 和输出阶 $r_1$，令
$$
r(x)=r_1+\varepsilon(1-x/L),\qquad
\kappa=\varepsilon/L,\qquad
S=\max(|r_1|,|r_1+\varepsilon|).
\tag{3.3}
$$
取 $Y=M_{r(x)}Z$。因为 $(M_{r(x)})_xM_{r(x)}^{-1}=-\kappa\mathcal L$，
准确共轭方程为
$$
Y_x=\mathsf A Y_\theta+\mathsf B Y+\mathcal R_{r(x)}Y
                                      -\kappa\mathcal LY+M_{r(x)}F.
\tag{3.4}
$$
设 $E(x)=\langle Y,\mathsf H Y\rangle$。由 (1.6)、(2.2)、(3.1)，
$$
\begin{aligned}
\tfrac12 E'
\le{}&\Gamma E+h^*C_0\|Y\|_2^2
 +h^*C_1\|Y\|_2\|\mathcal L^{1/2}Y\|_2\\
&-\kappa h_*\|\mathcal L^{1/2}Y\|_2^2
 +\kappa C_H\|Y\|_2^2
 +\sqrt E\,\sqrt{h^*}\|M_{r(x)}F\|_2 .
\end{aligned}
\tag{3.5}
$$
Young 不等式将第三项的一半负能量吸收后，得到
$$
(\sqrt E)'
\le G_\varepsilon(x)\sqrt E+\sqrt{h^*}\|F(x)\|_{r(x),\rho},
\tag{3.6}
$$
其中完全明确地取
$$
\boxed{\quad
G_\varepsilon
=\Gamma+\frac{h^*C_0+\kappa C_H}{h_*}
             +\frac{(h^*)^2C_1^2}{2\kappa h_*^2}.
\quad}
\tag{3.7}
$$
因此即使 $|\rho|$ 或系数偏离径向的幅度不小，只要这些实际范数
有限，就获得有限常数；小 $\varepsilon$ 的费用显式包含
$\varepsilon^{-1}$，没有将它隐藏在“tame”一词内。

## 4. 同一角权上的完整 Cauchy 与源定理

记
$$
\mathfrak C_{\varepsilon,\rho,r_1}
=\sqrt{h^*/h_*}
\exp\!\left(\int_0^L G_\varepsilon(x)dx\right).
\tag{4.1}
$$
若用一致系数界，也可直接使用
$$
\begin{aligned}
\log\mathfrak C_{\varepsilon,\rho,r_1}
\le{}&\tfrac12\log(h^*/h_*)+L\|\Gamma\|_\infty
 +L(h^*/h_*)\|C_0\|_\infty\\
&+\varepsilon\|C_H\|_\infty/h_*
 +\frac{(h^*)^2L^2}{2\varepsilon h_*^2}\|C_1\|_\infty^2.
\end{aligned}
\tag{4.2}
$$

**定理 4.1。** 同一个实际系统 (1.1) 的解满足
$$
\boxed{\quad
\|Z(L)\|_{r_1,\rho}
\le\mathfrak C_{\varepsilon,\rho,r_1}
\left[\|Z(0)\|_{r_1+\varepsilon,\rho}
       +\int_0^L\|F(x)\|_{r(x),\rho}dx\right].
\quad}
\tag{4.3}
$$
中间任意端点 $x$ 也有同一式，左端阶为 $r(x)$、积分截到 $x$，
常数可用 (4.1)，或者用仅积分到 $x$ 的指数。特别有较易使用的
一致源尺度
$$
\|Z(L)\|_{r_1,\rho}
\le\mathfrak C_{\varepsilon,\rho,r_1}
\left[\|Z(0)\|_{r_1+\varepsilon,\rho}
       +\|F\|_{L^1_xH^{r_1+\varepsilon}_\rho}\right].
\tag{4.4}
$$
同一式对反向传播成立，其损失仍从输入端到输出端为
$\varepsilon$。普通 $L^2_x$ 源可再付 $L^{1/2}$ 代替上述 $L^1_x$ norm。

**证明。** 对 (3.6) 用 Gronwall，并以
$h_*\|Y\|_2^2\le E\le h^*\|Y\|_2^2$ 比较端点，立即得到 (4.3)。
更准确的非齐次式中，每个源时刻 $x$ 的乘子是
$\sqrt{h^*/h_*}\exp\int_x^L G_\varepsilon$，故没有将源与初值
错误放在不同的径向角尺度上。

为避免预先假定解有正 log 正则，先用实际光滑数据的真实无权
Cauchy 解，换成引理 2.1 的截断 log 权。本题这一无权解已经由
R46 §2 的约束保持能量构造；一般系统也可由 (1.2)、(1.6) 的
无权对称双曲能量和 Friedrichs 逼近构造。这不是新增一个待付的
带权存在性假设。截断后的 log 因子是一个有界指数权，
所以所有计算可以先在足够高的普通 Sobolev 层完成。引理 2.1
给不依赖截断 $R$ 的 (3.6) 与 (4.3)。对 $\rho>0$ 以 Fatou/
单调极限、对 $\rho<0$ 以同一有界权极限，得到实际光滑数据的
(4.3)。再按初值及源 norm 完成有界延拓。
角系数若只给上述实际 Fourier 范数，也可先平滑角系数，在同一
有界窗口取极限；正下界和 (1.6) 仍须由实际输入一致支付。

反向令 $\widetilde x=L-x$。系统矩阵变成 $-\mathsf A,-\mathsf B$，
$\mathsf H_x$ 同时变号，(1.6) 中整个 Hermitian 矩阵反号而其
norm 不变；(1.4)–(1.5) 也不变。因此相同证明和常数适用。
唯一性保证这始终是原实际 Cauchy 演化的反向，而非另造的算子。
$\square$

本定理不声称无损 $H^r_\rho\to H^r_\rho$。它准确给任意
$\varepsilon>0$ 的有限损失，并且角权 $\rho$ 的数值完全不变。
若分成有限多个实际区间，分别分配正的 $\varepsilon_i$，
损失相加、常数相乘；中间真实源仍按每段自己的阶函数携带。

## 5. 真实 Darboux Cauchy 及完整普通源

将本定理用于 R46 的实际严格区密度算子
$$
Pu=\partial_x(au_x+bu_\theta)+\partial_\theta(bu_x+cu_\theta)+du=f,
\quad p=au_x+bu_\theta,\quad a>0,\quad b^2-ac>0.
\tag{5.1}
$$
记 $\alpha=1/a,q=b/a,\gamma=(b^2-ac)/a$，则
$Z=(u,u_\theta,p)^t$ 的准确矩阵为
$$
\mathsf A=\begin{pmatrix}0&0&0\\0&-q&\alpha\\0&\gamma&-q\end{pmatrix},
\quad
\mathsf B=\begin{pmatrix}0&-q&\alpha\\0&-q_\theta&\alpha_\theta\\
-d&\gamma_\theta&-q_\theta\end{pmatrix},
\quad
\mathsf H=\operatorname{diag}(1,\gamma,\alpha),\quad F=(0,0,f)^t.
\tag{5.2}
$$
两个前行保证 $Z_2=u_\theta$ 约束准确保持。
单就本篇 Cauchy 估计，$a,b,c$ 关于真实 $x$ 为
$W^{1,\infty}$、$d$ 为 $L^\infty$，连同 (1.2)、(1.4)–(1.6)
的实际角界已经足够：$\alpha,\gamma$ 的弱一阶径向导数正是
$\mathsf H_x$ 所需量。这里不要求时间解析或更高径向导数。
R46 的有限 WKB residual 另需它已列出的
$C^2\cap W^{3,\infty}$ 等实际导数；不能把较弱的 Cauchy 输入
当成已经支付了那个 residual。
令
$$
\mathcal P_{s,\rho}=H^{s+1/2}_\rho\oplus H^{s-1/2}_\rho .
$$
逐频率恒等式为
$$
\|(u,u_\theta,p)\|_{s-1/2,\rho}^2
=\|u\|_{s+1/2,\rho}^2+\|p\|_{s-1/2,\rho}^2.
\tag{5.3}
$$
所以对输出阶 $s$，在 (3.3) 取 $r_1=s-1/2$，便得
$$
\boxed{\quad
\|(u,p)(L)\|_{\mathcal P_{s,\rho}}
\le\mathfrak C_{\varepsilon,\rho,s-1/2}
\left[\|(u,p)(0)\|_{\mathcal P_{s+\varepsilon,\rho}}
 +\int_0^L\|f(x)\|_{s-1/2+\varepsilon(1-x/L),\rho}dx\right].
\quad}
\tag{5.4}
$$
这是原 $p$ 的完整源响应；没有把 $p$ 改成 $a u_x$，也没有投影掉
均值。若 $f$ 已在 $L^1H^{s+\varepsilon-1/2}_\rho$，直接使用该
一致 norm 即可。

R46 的完整 frame $\mathscr F$ 同样可使用。只需将 R46 (3.4)–(3.5)
中的乘法量换成真实带权量
$$
M_{v,\rho}(a_0)=2^{|v|/2}
\sum_l\langle l\rangle^{|v|}e^{|\rho|\omega(|l|)}|(a_0)_l|.
\tag{5.5}
$$
设得到的实际常数为 $F_{v,\rho},I_{v,\rho}$。则准确幅度传播
$\mathcal C(L,0)$ 有
$$
\|\mathcal C(L,0):E_{s+\varepsilon,\rho}\to E_{s,\rho}\|
\le I_{s,\rho}(L)\,
\mathfrak C_{\varepsilon,\rho,s-1/2}\,
F_{s+\varepsilon,\rho}(0).
\tag{5.6}
$$
其普通源为同一个
$$
\mathscr F(L)^{-1}\int_0^L\mathcal T(L,x)(0,f(x))^t dx,
\tag{5.7}
$$
范数由 (5.4) 再乘 $I_{s,\rho}(L)$ 控制。源若来自一个实际
divergence 或 contact 表达，应先保持该表达和正确的状态初值，
再使用相应的一阶源；本篇不因“源”这个名称自动少算导数。

## 6. 反号权的准确通量对偶

对 (5.1) 的同一真实齐次问题，Green 恒等式保存通量
$$
\Omega((u,p),(v,q))
=\frac1i\int(\overline u\,q-\overline p\,v)\,\frac{d\theta}{2\pi}.
\tag{6.1}
$$
在 $\mathcal P_{s,\rho}$ 与 $\mathcal P_{-s,-\rho}$ 之间，这个配对的
对偶 norm 恰为 $1$，因为两个 Sobolev 因子及两个 Fourier 权
逐模抵消。因此准确通量伴随给
$$
\boxed{\quad
\|\mathcal T(x,y):
 \mathcal P_{s+\varepsilon,\rho}\to\mathcal P_{s,\rho}\|
=
\|\mathcal T(y,x):
 \mathcal P_{-s,-\rho}\to\mathcal P_{-s-\varepsilon,-\rho}\|.
\quad}
\tag{6.2}
$$
这也给反号权的负阶窗口，绝不能把固定正权共轭后的非自伴系统
当作原系统来作同号权对偶。

等式先对光滑数据由真实可逆演化成立，再以有限 Fourier 序列的
稠密性延伸到上述 Hilbert 完成。负权完成可能不是分布空间这一点
不改变该准确 Hilbert 对偶，也不允许删除均值。与源项的对偶关系
同样来自完整 Duhamel 式 (5.7) 和 (6.2)，而不是省略源接触项后
另写一个形式伴随。

在完整 frame 中，R46 的普通 $L^2$ onto $J$-unitarity 仍是同一个
真实传播事实。正 log 权上的估计是 (5.6)，不宣称其在该带权
内积中也为 $J$-unitary。

## 7. 由真实解析 strip 明确支付 Fourier 系数输入

本节是一个充分条件，不需要用于已有直接 Fourier 包络的对象。
若矩阵 $A_0(\theta)$ 在 $|\operatorname{Im}\theta|<b$ 全纯，且
$\|A_0\|\le M_b$，则实际 contour 移动给
$\|(A_0)_l\|\le M_be^{-b|l|}$（可先取略小闭 strip）。
令
$$
N=\lceil S\rceil,\qquad
a_\rho=|\rho|(3/e)^{3/2},\qquad c=b/2,\qquad
E_{\rho,b}=\exp\left(a_\rho\sqrt e+\frac{a_\rho^2}{2b}+c\right).
\tag{7.1}
$$
用
$\omega(t)\le(3/e)^{3/2}\sqrt{e+t}$、
$a_\rho\sqrt t\le (b/2)t+a_\rho^2/(2b)$，以及
$$
\sum_{n\ge1}n^p e^{-cn}\le e^c\Gamma(p+1)c^{-p-1}
\quad(p\ge0),
$$
得到
$$
\sum_{l\ne0}|l|w_l\|(A_0)_l\|
\le 2^{S/2+N+1}M_b E_{\rho,b}
                         \Gamma(N+2)c^{-N-2},
\tag{7.2}
$$
$$
\sum_{l\ne0}w_l\|(A_0)_l\|
\le 2^{S/2+N+1}M_b E_{\rho,b}
                         \Gamma(N+1)c^{-N-1}.
\tag{7.3}
$$
分别用在 $\mathsf A,\mathsf B$。若 $\mathsf H$ 有同一 strip 界
$H_b$，还可取
$$
C_H\le H_b\,\frac{e^{-b}}{(1-e^{-b})^2},
\tag{7.4}
$$
因为 $\log(\sqrt2\langle n\rangle)\le n$，$n\ge1$。
这些常数粗但完全有限，且没有要求 $|\rho|$ 小于 $b$：直接 log
比指数权增长慢。实际数值证书可以直接使用更紧的有限 Fourier
和加指数尾包络。

对本题分段径向样条，有限 Fourier 的真实几何系数可以在每个
真实 $r$ 上取同一小复角 strip，前提是所有实际分母和选定平方根
分支在该 strip 内有严格界。径向 knot 不需在复数中延拓；
(1.1) 始终以真实 $r$ 为时间，(1.4)–(1.6) 对该时间取一致实界。
这不能免去 root collar 的独立真实坐标输入，但不会重新引入
一个不存在的全局复径向样条。

## 8. 有限参数差量及强余项使用方式

若实际矩阵族对参数 $\lambda$ 二次可微，且上述能量/Fourier 门
在一个真实参数区间内一致，令
$\mathcal L_\lambda=\mathsf A_\lambda\partial_\theta+\mathsf B_\lambda$。
其实际变分方程给
$$
\partial_\lambda T_\lambda(L,0)
=\int_0^L T_\lambda(L,x)
       (\partial_\lambda\mathcal L_\lambda)(x)T_\lambda(x,0)dx,
\tag{8.1}
$$
二阶导数则是一次 $\partial_\lambda^2\mathcal L_\lambda$ 插入，加上
两次 $\partial_\lambda\mathcal L_\lambda$ 的有序积分，系数为 $2$。
这里 $T$ 是 (1.1) 的真实向量演化。

例如，每条传播腿分配 $\eta>0$ 的损失，在所用有限窗口令其常数
共同不超过 $C$，并令真实乘子界给
$$
\|\partial_\lambda^j\mathcal L_\lambda:
(H^{r+1}_\rho)^m\to(H^r_\rho)^m\|\le P_j,\qquad j=1,2.
\tag{8.2}
$$
则准确有
$$
\|\partial_\lambda T_\lambda:
 H^{r+1+2\eta}_\rho\to H^r_\rho\|\le LC^2P_1,
\tag{8.3}
$$
$$
\|\partial_\lambda^2 T_\lambda:
 H^{r+2+3\eta}_\rho\to H^r_\rho\|
\le LC^2P_2+L^2C^3P_1^2.
\tag{8.4}
$$
所有向量分量取相同阶；用于 $(u,p)$ 或 $\mathscr F$ 时必须同时
微分其实际状态/端口 frame，不能把变化的 conormal 当成固定坐标。
这些式子由真实 Duhamel 的有序单纯形体积给出，不含形式参数
可微性的附加假设。普通源的参数导数按同一式加上其实际源导数。

最后，对 R46 的加权二阶强余项，可以明确分配损失预算：
真实 Cauchy/source 腿花 $\eta_C>0$，实际角流复合由 R41 花
$\eta_H>0$。式 R46(5.9) 的真实 residual 在 input 预付
$\eta_C+\eta_H$ 后满足本篇 (5.4) 的完整源尺度；R46 的初始
momentum 差、mean 列及 ordering/跨号修正按相同窗口逐项支付。
因此可得
$$
R_2:E_{s+\eta_C+\eta_H,\rho}\longrightarrow E_{s+2,\rho},
\tag{8.5}
$$
其常数就是 R46(6.8) 中实际 Cauchy 常数换成本篇 (4.1)，角图
常数换成 R41 对应有损强界、并把每个中间阶按上述预算平移后，
按同一算子顺序相乘求和。特别 Cauchy 输出阶取 $s+2$，它要求的
一致源阶准确是 $s+3/2+\eta_C$；实际 WKB source 中
$\Lambda^{-3/2}$ 将输入提升到 $s+3/2+\eta_C+\eta_H$，
真实角复合再花 $\eta_H$，正好落在这个源阶。初始 momentum
差、mean 列的 Cauchy 输入阶则取 $s+2+\eta_C$。
均值列的输出带权 norm也需真实支付；若实际系数/流的正 strip
和所有零阶乘子界已给，§7 与 R41 正好给这些量。

这关闭了严格区“需要另假设带权 Cauchy/source”的抽象空项。
实际候选仍须将其系数上下界、复角 strip、参数窗口和数值常数
填入，且 R43/R45/R47 的转折与正组件输入、全相位小除数、低块
和原 R37 residual 因子都必须在同一个对象上继续接合。
