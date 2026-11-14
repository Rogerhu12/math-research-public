# 任意 Schur 前向块的收敛逆源：统一大次数全列障碍

日期：2026-11-13（UTC）。作者：normal_complex / Astra-ISP-0c017065。

**状态：已证明的中间结论。** 本稿不再逐个处理单位圆周弧。
对任意逐块变化的标量 Schur 函数 $b_i$，只要 $b_i(0)\ne0$，
纯前向块 $R_i=b_i(T_{q_i})$ 的准确实际逆真空源乘积确实收敛，
便能在既有同一固定分块、同一固定正常态下构造真实有限 Walsh 列，
使 R244 全列聚合比值指数发散。

允许每块任意有限或无限零点、任意整体相位、零点自由内因子及外因子；
只要求 $b_i$ 在开单位圆盘解析且 $|b_i|\le1$。
没有要求它跨单位圆连续或解析。
证明不把来源推广为“每个收缩矩阵都存在这种标量 Schur 表示”。

核心是：完整 Schur 前向块接近真空，强制相应径向点值趋于 $1$。
这个径向预算同时控制紧内零点数、其余零点的总径向缺陷，
以及零点自由因子的正调和对数。消去紧内分母后，
剩余逆在一个固定紧圆盘的上界仅为 $\exp[o(\sqrt q)]$。
有限幂零性再给明确指数的算子界，
而约 $q/3$ 次 Walsh 列的矩增益严格超过它。

本稿没有将固定测试态变成真正湮灭者，也没有完成普通 Hilbert ISP。

## 1. 定理的准确对象和实际前提

纯块仍为
$$
T_q=\frac2{q+2}\sum_{j=1}^qE_j,\qquad
E=|1\rangle\langle0|,\qquad Q=q+2,
$$
$$
\Omega=\Omega_+^{\otimes q},\qquad
\Omega_+=2^{-1/2}(|0\rangle+|1\rangle),\qquad
D_j=I-2E_j.
\tag{1.1}
$$
$T_q^{q+1}=0$，$\|T_q\|<1$。
Walsh 基写作 $\chi_F=D_F\Omega$。
对有限块向量 $u=\sum_Fu_F\chi_F$，
$$
X_u^0=\sum_Fu_FD_F,\qquad X_u^0\Omega=u.
$$

第 $i$ 块取任意 Schur 函数
$$
b_i:\mathbb D\longrightarrow\overline{\mathbb D},
\qquad b_i(0)\ne0.
$$
定义纯前向、逆和源
$$
R_i=b_i(T_{q_i}),\qquad
U_i=R_i^{-1},\qquad
g_i=U_i\Omega,\qquad n_i=\|g_i\|\ge1.
\tag{1.2}
$$
幂零性使函数演算只使用前 $q_i+1$ 个 Taylor 系数。
$R_i$ 可逆是因为其唯一特征值为 $b_i(0)\ne0$；
Schur 性使 $R_i$ 收缩，故 $U_i$ 扩张。

为使最后一句不依赖未说明的函数演算推广，给出简短证明。
对任意严格收缩 $T$，令 $D_T=(I-T^*T)^{1/2}$，
$$
Vx=(D_TT^nx)_{n\ge0}\in\ell^2(\mathbb N_0;H).
$$
望远镜恒等式给 $\|Vx\|=\|x\|$，
且 $VT=S^*V$，其中 $S^*$ 为向后移位。
若 $b_r(z)=b(rz)$、$r<1$，则
$\|b_r(S^*)\|\le1$：
它是 Hardy 空间上系数共轭函数乘子之伴随，
乘子范数由圆周 Parseval 及 $|b_r|\le1$ 控制。
所以
$\|b_r(T)x\|=\|Vb_r(T)x\|
=\|b_r(S^*)Vx\|\le\|x\|$。
令 $r\uparrow1$，在幂零块上仅有限个系数取极限，得到
$\|b(T)\|\le1$。

实际生成元保持原来完整估计
$$
V_j1=\chi_j,\qquad
\|V_j-D_j\|\le8\eta_j,\qquad
\eta_j\le e^{-770\,16^j},\qquad
\|V_j\|,\|D_j\|<3.
\tag{1.3}
$$
对有限 $u$，实际有限列为 $X_u=\sum_Fu_FV_F$，且 $X_u1=u$。

准确实际逆块和源为
$$
\widetilde U_i=X_{g_i}/(1-\varepsilon_i),\qquad
\widetilde g_i=g_i/(1-\varepsilon_i),\qquad
0\le\varepsilon_i<1/2,
\tag{1.4}
$$
保持已经支付的预算
$$
16q_i5^{q_i}\max(1,n_i)\eta_{\min B_i}\le\varepsilon_i.
\tag{1.5}
$$
假设互不交块的准确源乘积确实在原 $H$ 中收敛：
$$
g^{(m)}=\prod_{i\le m}\widetilde g_i\longrightarrow g.
\tag{1.6}
$$
再保持实际收缩逆积构造所得 $P$、$Pg=1$
以及 R244 所需的同一组一致有界强单位等原前提。
因此使用的是同一个实际最小逆
$$
G=P^{-1}=X_g,\qquad Gu=X_ug
\tag{1.7}
$$
对每个有限 Walsh $u$ 准确成立。

固定分块和正常态为
$$
q_i=|B_i|=16^i,\qquad
f=1+\sum_{i\ge1}c_i\chi_{B_i},\qquad
c_i=2^{-i-2}=\frac1{4q_i^{1/4}},
$$
$$
\lambda=\|f\|^2=\frac{49}{48},\qquad
\phi_f(Y)=\langle Yf,f\rangle.
\tag{1.8}
$$
这个 $f$ 连续正且 $C$ 实，但已知不是所需慢主理想的湮灭者。
所有测试列使用这个同一 $f$，不另换态或分块。

**结论。** 存在块内非零有限 Walsh 列 $u_i$，$\|u_i\|\le1$，
使
$$
\boxed{
\liminf_{i\to\infty}\frac1{q_i}
 \log\frac{|\phi_f(X_{u_i})|}{\|Gu_i\|}
\ge
\gamma:=
\frac{\log2}{3}+\frac{\log3}{6}-\log\frac{11}{8}
>0.
}
\tag{1.9}
$$
因此 $\phi_f$ 不能满足这些逆源的 R244 全有限列聚合界。

## 2. 源收敛给真空接近；开圆盘 Schur 函数的准确径向化

由准确张量关系，
$$
\|g^{(i)}-g^{(i-1)}\|
=\|g^{(i-1)}\|\,
 \|g_i/(1-\varepsilon_i)-\Omega\|.
$$
由于各源块范数至少 $1$，前面的范数至少 $1$。
(1.6) 因而推出
$$
g_i/(1-\varepsilon_i)\to\Omega.
$$
又 $(1-\varepsilon_i)^{-1}\le\|g_i/(1-\varepsilon_i)\|\to1$，
所以 $\varepsilon_i\to0$、$g_i\to\Omega$。
收缩性遂给
$$
\|R_i\Omega-\Omega\|
=\|R_i(\Omega-g_i)\|
\le\|\Omega-g_i\|\longrightarrow0.
\tag{2.1}
$$

为允许 $b_i$ 只有开圆盘解析性，对每个 $i$ 选 $0<s_i<1$，
令
$$
\widehat b_i(z)=b_i(s_i z),\qquad
\widehat R_i=\widehat b_i(T_i),\qquad
\widehat U_i=\widehat R_i^{-1}.
$$
可令 $s_i$ 足够接近 $1$，同时使
$$
\boxed{
\|\widehat R_i-R_i\|\le e^{-q_i^2},\qquad
\|\widehat U_i-U_i\|\le e^{-q_i^2}.
}
\tag{2.2}
$$
理由是纯有限函数演算只用有限多个 Taylor 系数，
它们随 $s_i\uparrow1$ 连续；
常数项始终为 $b_i(0)\ne0$，所以矩阵逆也连续。
这是存在性的逐块明确近似要求，没有假设一致逆范数。

$\widehat b_i$ 在某个半径大于 $1$ 的圆盘解析，
并在闭单位圆盘上模不超过 $1$。
(2.1)--(2.2) 给
$\widehat R_i\Omega\to\Omega$。
下节先对这些准确的闭盘邻域解析函数作有限零点分解。
最终列通过 (2.2) 转回原 $U_i$，所以原来的 $P$、$g$ 和 $G$ 从未被替换。

## 3. 真空圆周密度与径向点值

令 $h_q=q^{-1/2}$。
纯真空矩准确为
$$
c_{q,n}=\langle T_q^n\Omega,\Omega\rangle
=\frac{(q)_n}{(q+2)^n}\quad(0\le n\le q).
$$
定义
$$
w_q(\theta)=1+2\sum_{n=1}^q c_{q,n}\cos(n\theta),\qquad
d\sigma_q(\theta)=\frac{w_q(\theta)}{2\pi}\,d\theta.
\tag{3.1}
$$
它是概率测度：严格收缩的 Cayley 恒等式
$$
\operatorname{Re}[(I+zT_q)(I-zT_q)^{-1}]
=(I-\overline zT_q^*)^{-1}
 (I-|z|^2T_q^*T_q)(I-zT_q)^{-1}\ge0
$$
在 $|z|=1$ 取真空元给 $w_q\ge0$，
常数 Fourier 系数给总质量 $1$。
对闭盘邻域解析的 $b$，
$$
\langle b(T_q)\Omega,\Omega\rangle
=\int b(e^{i\theta})\,d\sigma_q(\theta).
\tag{3.2}
$$

[Schur 零点稿](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)
已给完整 Riemann 和证明：
$$
h_qw_q(h_qx)\longrightarrow\sqrt{2\pi}e^{-x^2/2}
\quad\text{在每个固定紧窗一致}.
\tag{3.3}
$$
这里关键的两个直接估计是：
$n\le L\sqrt q$ 时
$\log c_{q,n}=-n^2/(2q)+O_L(q^{-1/2})$，
所有 $n$ 上 $c_{q,n}\le e^{-n^2/(3q)}$。
后者支付整个高斯外尾。
因此对每个固定 $M$，存在 $c_M>0$，
使充分大 $q$ 在 $|x|\le M$ 上满足
$h_qw_q(h_qx)\ge c_M$。

由 $\widehat R_i\Omega\to\Omega$、(3.2) 和 Schur 性，
$$
\int|1-\widehat b_i(e^{i\theta})|^2\,d\sigma_{q_i}(\theta)
\le2-2\operatorname{Re}\langle\widehat R_i\Omega,\Omega\rangle
\longrightarrow0.
$$
密度下界因而给每个固定 $M$ 上
$$
\int_{-M}^{M}
 |1-\widehat b_i(e^{ih_ix})|^2\,dx\longrightarrow0,
\qquad h_i=q_i^{-1/2}.
\tag{3.4}
$$

令 $x_i=1-h_i$。Poisson 核满足
$$
P_{x_i}(\theta)
\le\frac{\pi^2h_i}{h_i^2+\theta^2}
\qquad(q_i\ge4,\ |\theta|\le\pi).
\tag{3.5}
$$
Poisson 公式中，$|\theta|\le Mh_i$ 的积分由 (3.4) 与
Cauchy--Schwarz 趋于零；
外部用 $|1-\widehat b_i|\le2$ 和 (3.5) 至多得 $2\pi/M$。
先 $i\to\infty$，再 $M\to\infty$，遂得
$$
\boxed{\widehat b_i(x_i)\longrightarrow1.}
\tag{3.6}
$$
对充分大 $i$，这些值非零。以下略去有限初块并定义
$$
\ell_i=-\log|\widehat b_i(x_i)|\ge0,\qquad \ell_i\longrightarrow0.
\tag{3.7}
$$
不从普通弱收敛直接取点值；完整 Poisson 外尾已经支付。

## 4. 全部零点与零点自由因子的同一径向预算

固定一块，暂略下标 $i$。
$\widehat b$ 在闭盘邻域解析且不恒为零，
所以在开单位圆盘的零点数有限。
按重数列为 $\alpha_1,\dots,\alpha_m$，没有零点为 $0$。
令
$$
I(z)=\prod_{\nu=1}^m
 \frac{z-\alpha_\nu}{1-\overline{\alpha_\nu}z},
\qquad F(z)=\widehat b(z)/I(z).
\tag{4.1}
$$
$F$ 在单位圆盘解析且无零点。
圆周上 $|I|=1$，故最大值原理给 $|F|\le1$。
单位圆周上的零点不妨留在 $F$ 中；它们不破坏开盘内对数调和性。

### 4.1 任意圆周方向的径向缺陷

令 $x=1-h$，$h=q^{-1/2}$。
对任意零点 $\alpha$、$p=|\alpha|<1$，
$$
1-\left|\frac{x-\alpha}{1-\overline\alpha x}\right|^2
=\frac{(1-x^2)(1-p^2)}{|1-\overline\alpha x|^2}
\ge\frac{h(1-p)}4.
\tag{4.2}
$$
这里只用了 $1-x^2\ge h$、$1-p^2\ge1-p$、
$|1-\overline\alpha x|\le2$，没有角度限制。
由 $\log(1-y)\le-y$，
$$
\left|\frac{x-\alpha}{1-\overline\alpha x}\right|
\le e^{-h(1-p)/8}.
$$
又 $|\widehat b(x)|=|I(x)F(x)|\le|I(x)|$，故
$$
\boxed{
\sum_{\nu=1}^m(1-|\alpha_\nu|)
\le\frac{8\ell}{h}.
}
\tag{4.3}
$$

将 $|\alpha|\le3/4$ 的零点称为紧内零点，其数目为 $r$。
每个贡献至少 $1/4$，所以
$$
\boxed{r\le\frac{32\ell}{h}.}
\tag{4.4}
$$
回到逐块情形，$\ell_i\to0$ 给
$r_i=o(\sqrt{q_i})$。

### 4.2 零点自由 Schur 因子的对数

函数
$$
v(z)=-\log|F(z)|
$$
在整个开单位圆盘上非负调和。
因为 $|F(x)|\ge|\widehat b(x)|$，有 $v(x)\le\ell$。

取固定
$$
\rho_1=\frac8{11}.
$$
正调和函数的 Harnack 不等式给
$$
v(0)\le\frac{1+x}{1-x}v(x)\le\frac{2\ell}{h},
$$
$$
\sup_{|z|\le\rho_1}v(z)
\le\frac{1+\rho_1}{1-\rho_1}v(0)
\le\frac{38}{3}\frac{\ell}{h}.
\tag{4.5}
$$
这些 Harnack 常数直接来自 Poisson 核的最大最小值；
先在任意稍小同心圆上应用 Poisson 公式，再把半径趋于 $1$，
所以不要求 $v$ 在圆周有有限连续值。

### 4.3 其余全部零点的逆

若 $p=|\alpha|>3/4$ 且 $|z|\le\rho_1$，则
$$
\left|
\frac{1-\overline\alpha z}{z-\alpha}
\right|
\le\frac{1-p\rho_1}{p-\rho_1}.
\tag{4.6}
$$
证明可旋转使 $\alpha=p$；
固定 $|z|=s<p$ 时，平方比值
$(1-2ps\cos\theta+p^2s^2)/
 (p^2-2ps\cos\theta+s^2)$
随 $\cos\theta$ 递增，最大值在 $\theta=0$；
所得 $(1-ps)/(p-s)$ 随 $s$ 递增，故取 $s=\rho_1$ 即得 (4.6)。

又
$$
\frac{1-p\rho_1}{p-\rho_1}
=1+\frac{(1-p)(1+\rho_1)}{p-\rho_1}
\le1+76(1-p).
$$
所以这些逆因子的乘积在该紧圆盘满足
$$
\log\left|\prod_{|\alpha|>3/4}
 \frac{1-\overline\alpha z}{z-\alpha}\right|
\le76\sum_{|\alpha|>3/4}(1-|\alpha|)
\le608\,\frac{\ell}{h}.
\tag{4.7}
$$

令 $I_{\rm out}$ 为全部这些外圈零点的 Blaschke 积，
并定义剩余逆
$$
H(z)=\frac1{I_{\rm out}(z)F(z)}.
$$
它在 $|z|\le\rho_1$ 的邻域解析。
(4.5)、(4.7) 给
$$
\boxed{
\sup_{|z|\le8/11}|H(z)|
\le e^{A},\qquad
A=\frac{1862}{3}\frac{\ell}{h}.
}
\tag{4.8}
$$
逐块有 $A_i=o(\sqrt{q_i})$。
这个预算同时包括全部其他复圆周弧和所有零点自由因子。

## 5. 消去紧内分母后的有限块算子预算

令
$$
D_i(z)=\prod_{|\alpha|\le3/4}(z-\alpha),\qquad
N_i(z)=\prod_{|\alpha|\le3/4}(1-\overline\alpha z),
$$
$$
b_i^{\rm c}=\prod_{|\alpha|\le3/4}(1+|\alpha|).
\tag{5.1}
$$
这里 $b_i^{\rm c}$ 是正标量预算，与 Schur 函数 $b_i(z)$ 有区别。
准确函数分解为
$$
\widehat U_i=
H_i(T_i)N_i(T_i)D_i(T_i)^{-1}.
\tag{5.2}
$$

若 $H_i(z)=\sum_{n\ge0}h_{i,n}z^n$，
Cauchy 与 (4.8) 给
$|h_{i,n}|\le e^{A_i}(11/8)^n$。
因为 $T_i^{q_i+1}=0$、$\|T_i\|<1$，
$$
\boxed{
\|H_i(T_i)\|
\le\frac{11}{3}\left(\frac{11}{8}\right)^{q_i}e^{A_i}
=:M_i.
}
\tag{5.3}
$$
准确的几何和写法为
$\sum_{n=0}^{q}\rho_1^{-n}
\le\rho_1^{-q}/(1-\rho_1)$。
不需要任何无限算子 Neumann 级数。

取
$$
k_i=\lfloor q_i/3\rfloor,\qquad
v_{q,k}=\binom qk^{-1/2}\sum_{|F|=k}\chi_F,
$$
$$
u_i^0=\frac{D_i(T_i)v_{q_i,k_i}}{b_i^{\rm c}}.
\tag{5.4}
$$
$\|u_i^0\|\le1$，因为每个 $\|T_i-\alpha I\|\le1+|\alpha|$。
其 Walsh 次数至多 $k_i+r_i<q_i$ 对充分大 $i$ 成立。
紧内分母在 (5.2) 中准确消去，
而 $\|N_i(T_i)/b_i^{\rm c}\|\le1$，故
$$
\|\widehat U_i u_i^0\|\le M_i.
$$
通过 (2.2) 回到原逆，
$$
\boxed{\|U_i u_i^0\|\le M_i+e^{-q_i^2}.}
\tag{5.5}
$$

准确实际源的分块范数关系给
$$
\|X_{u_i^0}^0g\|
=\frac{\|g\|}{n_i}\|U_i u_i^0\|
\le\|g\|\,[M_i+e^{-q_i^2}].
\tag{5.6}
$$
这里使用 $n_i\ge1$，没有将纯源换成径向近似源。

全部 $2^{q_i}$ 个 Walsh 系数的 Cauchy--Schwarz 给
$\sum_F|(u_i^0)_F|\le2^{q_i/2}$。
(1.3) 的完整 telescoping 因而给
$$
\boxed{
\Delta_i:=\|X_{u_i^0}-X_{u_i^0}^0\|
\le8q_i(3\sqrt2)^{q_i}\eta_{\min B_i}
\le\frac{\varepsilon_i}{2n_i}
 \left(\frac{3\sqrt2}{5}\right)^{q_i}\longrightarrow0.
}
\tag{5.7}
$$
所以同一个实际 $G$ 满足
$$
\boxed{
\|Gu_i^0\|\le\|g\|\,[M_i+e^{-q_i^2}+\Delta_i].
}
\tag{5.8}
$$
此大次数输入没有使用不合适的
$q_i^{(\deg u_i^0)/2}$ 粗预算。

## 6. 中心在约 $-5/6$ 的准确完整块矩

固定 $q,k$ 和 $|F|=k$。
记
$$
L_{q,k}(p)=2^{-k}\langle p(T_q)D_F\chi_B,\chi_B\rangle.
$$
逐坐标使用 $D\chi=2\chi-\Omega_+$ 和
$E\chi=E\Omega_+$，得到准确生成式
$$
L_{q,k}(e^{tT_q})
=(1-t/Q)^{q-k}(1-t/(2Q))^k.
\tag{6.1}
$$
它与 $F$ 的具体位置无关。
应使用的中心是
$$
\xi_{q,k}=L_{q,k}(T_q)
=-1+\frac{2+k/2}{Q}.
\tag{6.2}
$$
特别不能在 $k\asymp q$ 时继续把 $-1$ 当作均值中心。

对中心化生成式取对数，线性项准确消失：
$$
\log L_{q,k}(e^{t(T_q-\xi_{q,k})})
=-\sum_{n\ge2}\frac{q-k+k/2^n}{nQ^n}\,t^n.
\tag{6.3}
$$
对指数 Taylor 系数逐项取绝对值，在 $0\le t\le Q/2$ 上得
$$
\boxed{
\sum_{m\ge0}
 \frac{|L_{q,k}((T_q-\xi_{q,k})^m)|}{m!}t^m
\le e^{t^2/q}.
}
\tag{6.4}
$$
因为其对数绝对主控不超过
$q\sum_{n\ge2}(t/Q)^n/n\le t^2/q$。
这个复线性泛函不被当作概率测度。

当 $q\ge80$、$k=\lfloor q/3\rfloor$ 时，
$\xi_{q,k}\le-13/16$。
因此每个紧内零点 $|\alpha|\le3/4$ 有
$$
|\xi_{q,k}-\alpha|\ge1/16,\qquad
\frac{|\xi_{q,k}-\alpha|}{1+|\alpha|}\ge1/28.
\tag{6.5}
$$
展开紧内分母
$$
\frac{D_i(T_i)}{D_i(\xi_i)}
=\prod_{|\alpha|\le3/4}
 \left[I+\frac{T_i-\xi_i}{\xi_i-\alpha}\right],
\qquad \xi_i=\xi_{q_i,k_i}.
$$
第 $m$ 次系数模至多 $(16r_i)^m/m!$。
由 $r_i=o(\sqrt{q_i})$，最终 $16r_i\le Q_i/2$，
所以 (6.4) 给
$$
\boxed{
\left|\frac{L_{q_i,k_i}(D_i(T_i))}{D_i(\xi_i)}-1\right|
\le e^{256r_i^2/q_i}-1=:E_i\longrightarrow0.
}
\tag{6.6}
$$
同时
$|D_i(\xi_i)|/b_i^{\rm c}\ge28^{-r_i}$。

纯代数中
$X_{u_i^0}^0=D_i(T_i)X_{v_{q_i,k_i}}^0/b_i^{\rm c}$。
把所有 $|F|=k_i$ 相加，得到准确矩
$$
\langle X_{u_i^0}^0\chi_{B_i},\chi_{B_i}\rangle
=
2^{k_i}\sqrt{\binom{q_i}{k_i}}\,
 \frac{D_i(\xi_i)}{b_i^{\rm c}}(1+\theta_i),
\qquad |\theta_i|\le E_i.
\tag{6.7}
$$
选单位相位 $\omega_i$ 使 $\omega_iD_i(\xi_i)>0$，
最终测试列定义为 $u_i=\omega_i u_i^0$。

因为 $\deg u_i^0<q_i$，
纯真空和完整块之间的两个交叉矩都为零。
其余真空项的模至多 $\lambda$。
结合 $c_i^2=1/(16\sqrt{q_i})$，充分大 $i$ 有
$$
\boxed{
\operatorname{Re}\phi_f(X_{u_i}^0)
\ge
\frac1{32\sqrt{q_i}}\,
 2^{k_i}\sqrt{\binom{q_i}{k_i}}\,28^{-r_i}
-\lambda.
}
\tag{6.8}
$$
实际矩误差至多 $\lambda\Delta_i\to0$。

## 7. 两个指数的严格分离

对 $1\le k\le q$，
$$
\binom qk
=\prod_{j=0}^{k-1}\frac{q-j}{k-j}
\ge(q/k)^k.
$$
当 $k_i=\lfloor q_i/3\rfloor$ 时，
$q_i/k_i\ge3$，所以
$$
2^{k_i}\sqrt{\binom{q_i}{k_i}}
\ge(2\sqrt3)^{k_i}.
\tag{7.1}
$$
又 $r_i=o(\sqrt{q_i})$，
因此 (6.8) 右侧主项的对数除以 $q_i$ 的下极限至少为
$$
\frac{\log2}{3}+\frac{\log3}{6}.
$$
减去的有界真空项和趋零的实际误差不改变这个指数。

另一方面，$A_i=o(\sqrt{q_i})$。
由 (5.3)、(5.8)，逆像范数对数除以 $q_i$ 的上极限至多为
$\log(11/8)$。
得到 (1.9)。

指数差严格为正可直接核算：
$$
(2\sqrt3)^2=12>\left(\frac{11}{8}\right)^6,
$$
即 $12\cdot8^6>11^6$。
甚至 $\gamma>1/16$：
$\log2>2/3$，
$\log3>13/12$，
且
$$
\log(11/8)
\le\frac38-\frac12\left(\frac38\right)^2
 +\frac13\left(\frac38\right)^3
=\frac{165}{512},
$$
所以
$\gamma>29/72-165/512=371/4608>1/16$。

$D_i(T_i)$ 可逆、$v_{q_i,k_i}\ne0$，
因此全部 $u_i\ne0$。
$G=P^{-1}$ 在其定义域上单射，故分母不会为零。
这完成了对原实际 $G$ 的真实有限列证明。

## 8. 有限个完整逆源的线性组合

设同一分块上有限个完整成功源 $g^{(\nu)}$，
每支纯前向均为上述任意 Schur 函数。
若
$$
g=\sum_{\nu=1}^Kz_\nu g^{(\nu)}
$$
又确为某个合格 $P$ 的 $P^{-1}1$，结论仍成立。

各支按第2节分别径向化，然后取各支紧内分母的共同乘积。
共同次数 $r_i$ 是有限个 $o(\sqrt{q_i})$ 的和，
故仍为 $o(\sqrt{q_i})$。
对第 $\nu$ 支，取消本支分母后，
其余分支额外的分母连同本支紧内分子，
在共同 $b_i^{\rm c}$ 归一后的算子范数不超过 $1$。
本支剩余逆仍满足
$$
M_{i,\nu}\le(11/3)(11/8)^{q_i}e^{o(\sqrt{q_i})}.
$$
各支的纯源分块等式及有限三角和给 (5.8) 的对应界；
共同分母的完整矩证明第6节原样成立，
所以同一个指数差 $\gamma$ 仍给比值发散。

这里组合的是完整逆源，且明确假设该组合仍是合格 $P$ 的真空原像。
没有把正则器之和的逆写成各逆之和，
也没有从一般块内有理线性组合推断 Schur 性。

## 9. 本结论关闭的路线与仍然开放的对象

**随后扩展：** 同日的[整个有限块 Gram 定理](2026-11-13-arbitrary-contractive-block-complete-gram-and-source-obstruction-normal-complex.md)已进一步覆盖任意纯有限交换块中的可逆收缩，不再要求标量 Schur 表示；下文原范围记录仅描述本稿这条显式次数列证明。

本稿统一覆盖此前需要分开处理的族：

- 任意参数、任意有限阶 Blaschke 前向块，包括全部复圆周弧；
- 任何在圆盘内解析的零点自由 Schur 前向块，包括边界奇异内因子；
- 有限及无限零点、内外因子混合的任意 Schur 前向函数；
- 同一分块上的有限个完整成功逆源线性组合，条件如第8节。

这些族仍须真的满足实际源收敛、carry、$Pg=1$ 和同组强单位等公共前提。
若没有真空原像，本文不能先替它定义一个 $g$；
若只有某个有限矩阵 $R_i$ 为收缩，而没有标量 Schur 函数表示，
本文也没有证明它属于上述范围。

[负实粗源稿](2026-11-13-signed-real-and-complex-sector-blaschke-large-column-obstruction-normal-complex.md)
中的准确 Gram 例仍有独立作用：
它表明某些合格逆源不在 $\mathcal H_{\sqrt3}$，
即使逆算子积本身范数收敛。
本稿避免把加权源正则性当作一般必要条件，
直接用原 $G$ 的大次数完整列得到统一障碍。

固定 $f$ 本来就不是湮灭者。
因而这里没有排除一般正正常见证；
真正湮灭者专属配对、不同物理分块、无真空原像前向族、
不具标量 Schur 表示的块构造以及慢符号有界分母仍未解决。
普通 Hilbert ISP 未完成。

完整依赖：

- [R244 聚合逆图和全有限列核心](../results/R244-appendix-aggregate-inverse-graph-moment-criterion-and-cyclic-factor.md)；
- [Schur 真空密度和径向点值](2026-11-13-schur-zero-count-for-convergent-inverse-vacuum-blocks-normal-next.md)；
- [负实边界准确 Gram 与大次数中心计算](2026-11-13-signed-real-and-complex-sector-blaschke-large-column-obstruction-normal-complex.md)；
- [复有理分母消去](2026-11-13-complex-rational-block-denominator-cancellation-and-growing-order-obstruction-normal-next.md)。

第3节重列了使用的完整径向论证，第6节重做了大次数中心；
没有把小次数在 $-1$ 处的误差公式挪到 $k\asymp q$。
