# R540 — 原 degree 6 两条来源的完整 Schwartz、全权平方与负二次 Katz 点

日期：2026-11-14。**状态：本篇完整支付 R532／R533 中 $f_4=x_\wp\sigma^6$ 与 $f_1=-x_\wp y_\wp\sigma^6$ 的实际有限 Hecke 角色、二处及三处全部 splitting、固定 Schwartz 函数、Hermitian 代表、Hermite 与周期常数、两条完整普通核心，以及 $f_4$ 固定负二次矩所读的原 primitive Katz 点。反射的复中心根数恰为 $-1$。没有据此证明负二次矩非零，也没有从已有有限素数计算推出无穷非消失。**

本篇先在基曲线 $E_0:y^2=x^3+1$ 上固定算术角色，再以实际微分同构返回原 $b=17$ frame。这里的 $\psi_0$ 始终是基曲线角色，不能与原 $E_{17}$ 或 $E_{2312}$ 的角色互换。

## 1. 实际来源与结论

设
$$
K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
\omega=(-1+\delta)/2,\quad
s=(1-\omega)^{-1}=(3+\delta)/6,\quad a=2+\omega=-\omega\delta.
\tag{1}
$$
取 $x_\wp=z^{-2}+\cdots$、$y_\wp=-z^{-3}+\cdots$、$\sigma=z+\cdots$。
在 $E_0$ 上定义
$$
f_{4,0}=x_\wp\sigma^6=\sum_{m\ge0}a_{4,m}z^m,\qquad
f_{1,0}=-x_\wp y_\wp\sigma^6=\sum_{m\ge0}a_{1,m}z^m.
\tag{2}
$$
它们分别只有 $m\equiv4,1\pmod6$ 的项，且 $a_{4,4}=a_{1,1}=1$。
这正是 [R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)
中完整双变量外积的两个因子，不是另外选择的同型 theta 线。

令 $\psi_0$ 为 [R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)
完整规定的 $E_0$ Hecke 角色。若 $c\equiv1\bmod2\delta$，则
$\psi_0((c))=c$。对素于六的 $c$，令
$$
t_2(c)=\operatorname{Teich}_{\mu_3}(c\bmod2),\qquad
k_3(c)\in\mu_6,\quad k_3(c)\equiv c\bmod\delta^2.
$$
后一个根唯一，因为 $\mu_6\longrightarrow(\mathcal O_K/3)^\times$ 是同构。
定义原有限角色
$$
\boxed{\xi((c))=t_2(c)^{-1}k_3(c)^4.}
\tag{3}
$$
其导子准确为 $(6)=2\delta^2$，阶为三，且 $\xi^c=\xi^{-1}$。
以下不用三个好素数的特征值来决定 (3)。

对 $j=4,1$、$m\ge0$、$m\equiv j\bmod6$，本篇证明存在明确固定的非零代数常数 $c_4,c_1$，使
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\xi\psi_0^{\,2m+1},m+1)}
     {m!(s\Omega_0)^{2m+1}}
 =c_j\,6^{-m}a_{j,m}^{\,2}.}
\tag{4}
$$
这里 $\Omega_0>0$ 是 $E_0$ 的 primitive 实周期，微分为 $dx/(2y)$。
常数由第 6 节的同一 Schwartz、范数及首项准确确定；没有逐权另取比例。

普通素数 $p>7$、$p\equiv1\bmod3$ 处，令
$$
\pi_0=\psi_0(\mathfrak p),\quad
\bar\pi_0=\psi_0(\bar{\mathfrak p}),\quad
\pi_0\bar\pi_0=p,\quad v_p(\pi_0)=1,\quad
\Omega_{p,0}\in\mathcal O_{\mathbf C_p}^{\times}.
\tag{5}
$$
取与该微分和同一 CM type 相容的原形式群周期。令 $\nu_{j,0}$ 为 Amice 变换
$f_{j,0}(\Omega_{p,0}\log(1+Z))$ 的整测度。则固定负点
$$
\nu_-=\xi\psi_0^{-1}\bar\psi_0^2
$$
满足
$$
\boxed{
\nu_-(\mathcal L_{(6)}^{\rm prim})
 =36c_4\Omega_{p,0}
   \left(\int_{\mathbf Z_p^\times}x^{-2}\,d\nu_{4,0}(x)\right)^2.}
\tag{6}
$$
$\mathcal L_{(6)}^{\rm prim}$ 采用 R295／R332 已固定的 Katz 晶格周期及 Artin 规范。
二、三处均真正分歧；(6) 没有 sigma 支的额外 $3/2$ 因子。

正确的复反射是
$$
\boxed{W(\xi^{-1}\psi_0^3)=-1,\qquad
L(\xi^{-1}\psi_0^3,2)=0,}
\tag{7}
$$
而同一 $f_1$ 的正一次值是
$$
\boxed{L(\xi\psi_0^3,2)>0.}
\tag{8}
$$
(7) 与 (8) 的有限角色互为逆，不能替换。负二次 $p$ 进值的非零尚未由这些等式支付。

## 2. 全部有限角色与 Hermitian 代表

### 2.1 角色定义确实下降到理想

对 $u\in\mu_6$，有 $t_2(u)=u^4$、$k_3(u)=u$，故 (3) 在更换理想生成元时不变。
有限环 $(\mathcal O_K/6)^\times$ 的十八个元素上，(3) 是非平凡三次角色。
在二处的剩余 $\mathbf F_4^\times$ 上非平凡；在三处的
$(1+\delta\mathcal O_{K,3})/(1+\delta^2\mathcal O_{K,3})$ 上也非平凡。
因此其导子既不能去掉二处，也不能将三处降为 $\delta$。
共轭分别把两个根取逆，所以 $\xi^c=\xi^{-1}$。有理主理想上的值为一，特别 $\xi((5))=1$。

固定正 Artin 约定，(3) 的完整 idèle 分量是
$$
\xi_2(u)=t_2(u),\quad \xi_2(2)=1;\qquad
\xi_3(u)=k_3(u)^{-4},\quad \xi_3(\delta)=1.
\tag{9}
$$
其余有限处未分歧，无穷处分量平凡。这里单位上的 idèle 值与 (3) 的理想值互逆。
$\xi_2(2)=\xi_3(\delta)=1$ 也由主 idèle $2,\delta$ 的乘积公式直接得到。
若使用三次剩余符号，(3) 是 $(2/\cdot)_3^{-1}$；本篇的定义和证明只需要显示的有限公式。

置
$$
\Phi_m=\xi\psi_0^{2m+1},\qquad
\chi_m=\Phi_m\mathrm N^{-m-1/2}.
\tag{10}
$$
R302 的基角色 $\chi_0^{\rm bas}=\psi_0\mathrm N^{-1/2}$ 在二处的单位角色为 $t_2$，
uniformizer 值为 $-1$；三处单位角色是 $k_3^3$，在 $\delta$ 的值是 $i$。
结合 (9)，完整坏局部数据如下。

| 权族 | 二处单位 | 二处 $2$ | 三处单位 | 三处 $\delta$ | 原导子 |
|---|---|---:|---|---:|---|
| $m\equiv4\bmod6$ | $t_2$ | $-1$ | $k_3^{-1}$ | $i$ | $(6)$ |
| $m\equiv1\bmod6$ | $t_2$ | $-1$ | $k_3^{-1}$ | $-i$ | $(6)$ |

无穷处为 $(z/|z|)^{-(2m+1)}$。表中三处 uniformizer 的符号是两族的实质差异。

### 2.2 原 epsilon 条件与三处加性相位

加性角色为
$\psi_\infty(x)=e^{2\pi ix}$、$\psi_\ell(x)=e^{-2\pi i\{x\}_\ell}$，
$\psi_{K,v}=\psi_v\circ\operatorname{Tr}_{K_v/\mathbf Q_v}$。
Yang 的局部条件采用
$$
\epsilon(1/2,\chi_{m,v},\psi_{K,v}/2)\chi_{m,v}(\delta)
 =\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{11}
$$
二处与 R302 的完整分歧三次角色相同，原 $\mathbf F_4$ Gauss 和为二，左边为 $+1$。

三处导子为二。写 $u=A+B\omega\in\mu_6$，Tate 求和可取 $c=\delta^3$。
必须在 $\mathbf Q_3/\mathbf Z_3$ 中计算：
$$
\operatorname{Tr}\frac{u}{2\delta^3}=-\frac B6
 \equiv\frac B3\pmod{\mathbf Z_3},\qquad
\psi_{K,3}\!\left(\frac{u}{2\delta^3}\right)=\omega^{-B}.
\tag{12}
$$
因此两个准确的有限和是
$$
\sum_{u\in\mu_6}u\,\omega^{-B}=3,\qquad
\sum_{u\in\mu_6}u^{-1}\omega^{-B}=-3.
\tag{13}
$$
不能把 $-B/6$ 直接当作实分数的 fractional part；那会把这里的符号写反。
本篇单位角色是 $k_3^{-1}$，所以用第一和。三处 epsilon 分别为 $-i,i$，
再乘表中的 $i,-i$ 后都为 $+1$。其余有限点同为 $+1$；正无穷 Hermite 型要求正类。

由此可选准确的全局 Hermitian 代表
$$
\boxed{\alpha=3=\mathrm N_{K/\mathbf Q}(\delta).}
\tag{14}
$$
它与一属于同一个 Hermitian 类，但实际 Schrödinger 尺度不同。
本篇始终使用
$$
\iota_3(x+y\delta)=
\begin{pmatrix}x&27y\\-y/9&x\end{pmatrix},\qquad
\kappa_\infty=|\delta^3\alpha|=9\sqrt3.
\tag{15}
$$
以下二处向量、三处支撑和 Gaussian 都针对 (15)。

## 3. 二处的完整四陪集 Schwartz，不只核 $\mu_3$

设
$$
e_b=\mathbf1_{b/2+2\mathbf Z_2},\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,\quad
t=\frac{\sqrt3-1}{\sqrt2}.
$$
两族的实际二处向量相同：
$$
\boxed{\phi_2=f_A+t f_B,\qquad v_2=(1,t,-1,t),\qquad
\|\phi_2\|^2=3-\sqrt3.}
\tag{16}
$$
令 $\zeta_8=e^{\pi i/4}$，
$g_*=(-11+4\delta)/13=(1+2\delta)/(1-2\delta)$。
将 (10)、(15) 代入 Yang Appendix (A1)–(A3)，保留 Hilbert 因子和二次 Weil 指数，得
$$
\mu(\omega)=-\omega^2\zeta_8^{-1},\qquad
\mu(g_*)=\mu(-g_*)=\zeta_8^{-1}.
\tag{17}
$$

在 $\omega$ 处，完整 Rao 核为
$$
\frac{\mu(\omega)}{\sqrt2}
 \int_{\mathbf Q_2}
 \psi_2\!\left(\frac92(u^2+4uv+v^2)\right)\phi(v)\,dv.
\tag{18}
$$
输出先在四分之一格。于 $u=k/4$ 的值是
$$
\frac{\mu(\omega)}{2\sqrt2}
\sum_{b=0}^3v_{2,b}
 \zeta_{32}^{-9(k^2+8kb+4b^2)}.
\tag{19}
$$
$k$ 奇数时，$b=0,2$ 相位相同而系数相反，$b=1,3$ 相位相反而系数相同，故完整消失。
在 $u=a/2$，原四维矩阵准确为
$$
M_{\omega,ab}
 =\frac{-\omega^2\zeta_8^{-1}}{2\sqrt2}
  \zeta_8^{-9(a^2+b^2+4ab)},\qquad
M_\omega v_2=v_2.
\tag{20}
$$
这是四维完整值，不是只检验两个 Taylor 系数。

$\phi_2$ 偶，故在 $g_*$ 处可明确作 $v\mapsto-v$。核成为
$$
2\mu(g_*)\int
 \psi_2\!\left(\frac98(11u^2-26uv+11v^2)\right)\phi(v)\,dv.
$$
驻相条件是 $a\equiv3b+2\bmod4$；四个非零相位为 $-1,1,-1,1$。
于是完整矩阵为
$$
M_{g_*}=
\begin{pmatrix}
0&0&-1&0\\
0&1&0&0\\
-1&0&0&0\\
0&0&0&1
\end{pmatrix}.
\tag{21}
$$
它同时固定 $f_A,f_B$。负生成元的相位由 (17) 保留，亦固定该偶向量。
$\mu_3,-1,g_*$ 拓扑生成 $K_2^1$：主单位的对数为 $4\delta\mathbf Z_2$，
$\log g_* /(4\delta)$ 是单位。因此 (16) 是整个实际二进环面的向量。
每个 $e_b$ 的体积为 $1/2$，直接给出 (16) 的范数。

## 4. 三处的完整两个陪集及 pro-$3$ 生成元

置
$$
e_j=\mathbf1_{j/9+(1/3)\mathbf Z_3},\quad j=0,\pm1.
$$
实际向量为
$$
\boxed{\phi_{3,+}=e_1+e_{-1},\qquad
       \phi_{3,-}=e_1-e_{-1},\qquad
       \|\phi_{3,+}\|^2=\|\phi_{3,-}\|^2=6.}
\tag{22}
$$
$+$ 用于 $m\equiv4\bmod6$，$-$ 用于 $m\equiv1\bmod6$。

先使用同一 $\alpha=3$ 的基角色 $\chi_0^{\rm bas}$ splitting。
原 $\omega$ 核是
$$
\frac13\int\psi_3\!\left(\frac92(u^2+4uv+v^2)\right)\phi(v)\,dv,
$$
其 splitting 为一。特别 $\delta(\omega-1)=3\omega^2$，而
$\chi_{0,3}^{\rm bas}(3)=1$；这里须保 $3=-\delta^2$ 的单位负号。
在 $v=j/9+t/3$ 上积分，输出只可能是 $u=k/9$、$k\equiv j\bmod3$。
写 $k=j+3l$，常数项为
$$
j^2/3+jl+l^2/2,
$$
所以
$$
W_\omega^{\rm bas}e_j=\omega^{-j^2}e_j.
\tag{23}
$$
本篇两族的实际 splitting 相对基角色在 $\omega$ 处乘 $\omega$。
故 $e_{\pm1}$ 都被新的 $W_\omega$ 固定。

再取完整主生成元
$$
g_3=\frac{1+3\delta}{1-3\delta}
   =\frac{-13+3\delta}{14}.
$$
两族的 splitting 都准确为 $\mu(g_3)=-i$，核为
$$
\frac{-i}{\sqrt3}
\int\psi_3\!\left(\frac32(13u^2+28uv+13v^2)\right)\phi(v)\,dv.
\tag{24}
$$
此处保原交叉正号；不能对奇向量 $\phi_{3,-}$ 擅作无符号的反射。
驻相仍给 $u=k/9$、$k=j+3l$。代入 $v=j/9+t/3$，常数、线性和二次项为
$$
j^2+3jl+\frac{13l^2}{6},\qquad
\left(3j+\frac{14l}{3}\right)t,\qquad
\frac{13t^2}{6}.
$$
于是所需完整 Gauss 积分为
$$
\frac13\sum_{t\bmod3}\omega^{-2(t^2+lt)}
 =\frac{\delta}{3}\omega^{2l^2},\qquad
\psi_3(13l^2/6)=\omega^{-2l^2}.
\tag{25}
$$
两相位相消；陪集体积三和 (24) 的模因子给 $\sqrt3$，剩余标量
$(-i)\sqrt3\,\delta/3=1$。因此 $g_3$ 固定每个 $e_j$。

在 $-1$ 处，Yang Proposition 1.2 的完整作用分别为 $+R$、$-R$，
其中 $R\phi(u)=\phi(-u)$：因子是
$\chi_{m,3}(\delta)(-i)$，故 (22) 的偶／奇号恰好匹配。
$\mu_6,g_3$ 生成整个 $K_3^1$，因为
$\log g_3/(6\delta)\in\mathbf Z_3^\times$。
这支付了整个三进环面，而不只支付剩余群 $\mu_6$。

其余有限处取 Yang 的标准未分歧 Schwartz 向量；在此原模型为
$\mathbf1_{\mathbf Z_\ell}$，分裂处按其 Corollary 2.14 的极化比较。
所以完整 finite norm 是
$$
\boxed{6(3-\sqrt3).}
\tag{26}
$$

## 5. 原 Hermite 系数、全部周期和 degree 6 的唯一识别

定义 Hermite 多项式
$$
\sum_{m\ge0}H_m(X)\frac{T^m}{m!}
 =e^{XT-T^2/(8\pi)}.
$$
(16)、(22) 的有理共同支撑准确为 $x=n/18$、$3\nmid n$。
此时二处 $2x=n/9\equiv n\bmod4$，三处 $9x=n/2\equiv-n\bmod3$。
令
$$
a_{+,n}=v_2(n\bmod4)\mathbf1_{3\nmid n},\qquad
a_{-,n}=v_2(n\bmod4)\left(\frac{n/2}{3}\right),
\tag{27}
$$
其中 Legendre 值在三的倍数取零。原 Hermite 系数为
$$
b_{\pm,m}=
\sum_{n\in\mathbf Z}a_{\pm,n}
H_m\!\left(\frac{\sqrt{9\sqrt3}}{18}n\right)
e^{-\pi\sqrt3 n^2/36}.
\tag{28}
$$
所有系数都是实数。不要把第二行的 $(n/2\,/\,3)$ 改成 $(n/3)$ 而丢掉总负号。

令
$$
h=\frac{\sqrt{9\sqrt3}}{36\pi i},\qquad
F_\pm(Z)=\sum_na_{\pm,n}
e^{\pi i(\delta/3)n^2/12+2\pi inZ}.
$$
则 $\mathcal B_\pm(T):=\sum b_{\pm,m}T^m/m!
=e^{-T^2/(8\pi)}F_\pm(hT)$。
原有限系数准确满足
$$
a_{\pm,n+12}=a_{\pm,n},\qquad
a_{\pm,n+6}=-(-1)^na_{\pm,n}.
$$
逐项换元因此给
$$
F_\pm(Z+1)=F_\pm(Z),\qquad
F_\pm(Z+s)=e^{-6\pi is-12\pi iZ}F_\pm(Z).
\tag{29}
$$
原 reduced theta frame 是
$$
\mathscr F_\pm(Z)=e^{6\sqrt3\pi Z^2}F_\pm(Z)\in\mathcal S_6,\qquad
6\sqrt3\pi h^2=-1/(8\pi).
\tag{30}
$$
所以 Hermite 的二次指数完全抵消，没有余下 Gaussian 或未付的平坦 twist。

为了核定全部型，使用同一个基角色 Weil 表示：二处 (16) 固定，
三处 (23) 的 $e_{\pm1}$ 特征为 $\omega^2$。
无穷第 $m$ Hermite 向量的特征为 $\omega^m$（Yang Lemma 1.1）。
全球 rational $\omega$ 的 theta 不变性给 $m\equiv1\bmod3$。
再用 (27) 的偶／奇性，分别得到 $m\equiv4,1\bmod6$。

完整 $\mathcal S_6=\sigma^6 L(6O)$ 的基可取
$$
\sigma^6,\quad x_\wp\sigma^6,\quad y_\wp\sigma^6,\quad
x_\wp^2\sigma^6,\quad x_\wp y_\wp\sigma^6,\quad x_\wp^3\sigma^6.
$$
型 $4$ 和型 $1$ 各恰一维。又 $a_{\pm,1}\ne0$，所以 Fourier 级数不恒零。
由完整线丛与型，得到固定非零常数
$$
\boxed{
\mathcal B_+(T)=C_4 f_{4,0}(\Omega_0hT),\qquad
\mathcal B_-(T)=C_1 f_{1,0}(\Omega_0hT).}
\tag{31}
$$
这里 $C_4\in\mathbf R^\times$、$C_1\in i\mathbf R^\times$，并且
$$
C_4=\frac{b_{+,4}}{4!(\Omega_0h)^4},\qquad
C_1=\frac{b_{-,1}}{\Omega_0h}.
\tag{32}
$$
完整空间的一维性与 Fourier 非零已经证明这两个首系数非零；
没有用有限 Taylor 拟合，也没有用浮点 L 值判断来源。

## 6. 完整 Yang 常数与两个周期规范

两族分别沿 $m\equiv4,1\bmod6$ 保持第 2–4 节的所有有限数据。
无穷范数为 $m!/(4\pi)^m/\sqrt{18\sqrt3}$，因此原向量范数平方是
$$
\mathcal N_m=
\frac{6(3-\sqrt3)}{\sqrt{18\sqrt3}}\frac{m!}{(4\pi)^m}.
\tag{33}
$$
Yang 1997 Theorem 1.11 的 $S_1$ 只有惰性二处，$S_2$ 为空，故
$c(0)=(1+2^{-1})^{-1}=2/3$。
三处虽然角色导子为二，它是分歧地点，并不在该定理的 $S_1,S_2$ 中；
不能再添一个三处 $c(0)$。
$h_K=1$、单位群 $\mu_6$ 以及 R302 的同一全局 Haar 规范给
$$
\begin{aligned}
L(\Phi_m,m+1)
 &=\frac{2}{6c(0)}\frac{\pi}{3\sqrt3}
   \frac{b_{\pm,m}^2}{\mathcal N_m}\\
 &=C_{\rm Y}\frac{(4\pi)^m}{m!}b_{\pm,m}^2,\qquad
\boxed{C_{\rm Y}=
\frac{\pi\sqrt{18\sqrt3}}{36\sqrt3(3-\sqrt3)}>0.}
\end{aligned}
\tag{34}
$$
这保留 finite norm、Hermite norm、两处原测度、单位群和所有坏位因子。

置
$$
\kappa_4=\frac{C_{\rm Y}C_4^2}{\Omega_0}>0,\qquad
\kappa_1=-\frac{C_{\rm Y}C_1^2}{\Omega_0}>0.
$$
因为 $(2\pi/\sqrt3)\,4\pi h^2=-1/18$，(31)–(34) 给
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\Phi_m,m+1)}{m!\Omega_0^{2m+1}}
 =\kappa_j18^{-m}a_{j,m}^2.}
\tag{35}
$$
$f_4$ 的合法权为偶，$f_1$ 的合法权为奇；后者的负号由 $C_1^2<0$ 准确抵消。

换成真实 CM 生成周期 $\varpi_0=s\Omega_0$。
由 $s^2=-\omega^2/3$，
$$
s^{-2m}=
\begin{cases}
3^m\omega,&m\equiv4\bmod6,\\
-3^m\omega,&m\equiv1\bmod6.
\end{cases}
$$
所以 (4) 中准确的常数是
$$
\boxed{c_4=\omega\kappa_4/s,\qquad c_1=-\omega\kappa_1/s.}
\tag{36}
$$
若记 (4) 左边为 $\mathscr E_{j,m}$，它们也可无任意归一地写成
$$
\boxed{c_4=6^4\mathscr E_{4,4},\qquad c_1=6\mathscr E_{1,1}.}
\tag{37}
$$
经典 CM 临界值代数性给 $c_4,c_1\in\overline{\mathbf Q}^{\times}$。
(32)–(37) 已完全确定这两个数；本篇不需要以数值认出它们是哪个代数数。
若以后需要它们在所有研究素数都为单位，须明确删除其固定有限支撑；
不能从“固定非零代数数”直接认成每个 $p$ 的单位。

首权 $m=4,1$ 在 (34) 中都严格正，特别得到 (8)。

## 7. 同一普通测度、单 Euler 核与全 tame 插值

### 7.1 整测度与真实完整核心

原普通 sigma 整性沿用 R295／R300 的实际微分与 CM 形式群规范。
$f_{4,0}=\Theta_0\sigma_0^4$；另
$f_{1,0}=\Theta_0\sigma_0 B_3$，其中
$B_3=-y_\wp\sigma_0^3=\sigma_0(2z)/(2\sigma_0(z))$。
这些原 Amice 级数均整，所以 $\nu_{j,0}$ 有界，且
$$
M_{j,m}:=\int_{\mathbf Z_p}x^m\,d\nu_{j,0}(x)
 =\Omega_{p,0}^m m!a_{j,m}.
\tag{38}
$$
三次 CM 排除了二次 Gaussian 修正，不能另换一个 $p$ 进 sigma frame。

置 $r_c(z)=\sigma_0(cz)/\sigma_0(z)^{\mathrm N c}$。
R300 的真实逐支迹在整个 degree 6 空间给
$$
\mathscr T_{p,0}(\sigma_0^6f)=
 \frac{\bar\pi_0}{p}\sigma_0^6
 \operatorname{Tr}_{[\pi_0]}
 \left[(r_{\bar\pi_0}/r_{\pi_0})^6 f\circ[\bar\pi_0]\right].
\tag{39}
$$
它保持完整空间并与 $\mu_6$ 作用交换，故在 (2) 两线上各为标量。
原测度的整性及两个首矩 $4!\Omega_{p,0}^4,\Omega_{p,0}$ 为单位，保证标量是整的。

其准确值是
$$
\boxed{\mathscr T_{p,0}\nu_{4,0}=\xi(\mathfrak p)\nu_{4,0},
\qquad\mathscr T_{p,0}\nu_{1,0}=\xi(\mathfrak p)\nu_{1,0}.}
\tag{40}
$$
为避免循环，第 7.2 节先只用已证明的 (4)、Katz 正权插值和有界测度的密集正权极限。
这独立给单位 Mellin 的整条平方。然后设 (39) 的整标量为 $c$，
在非零首权 $m=4$ 或 $1$ 比较，置 $e_m=\pi_0^m/\bar\pi_0^{m+1}$，得到
$$
(1-ce_m)^2=(1-\xi(\mathfrak p)e_m)^2.
$$
于是 $(c-\xi(\mathfrak p))e_m(2-(c+\xi(\mathfrak p))e_m)=0$。
最后一因子因 $v_p(e_m)>0$ 为单位，所以 $c=\xi(\mathfrak p)$。
这里符号由完整 Euler 比较支付，不是由好素数样本认定。

令 $\varkappa_0=p/\bar\pi_0^2$。完整测度与单位矩因此为
$$
\boxed{
\nu_{j,0}|_{p\mathbf Z_p}
 =\frac{\xi(\mathfrak p)}{\bar\pi_0}
   [\varkappa_0]_*\nu_{j,0},\qquad j=4,1,}
\tag{41}
$$
$$
\boxed{
\int_{\mathbf Z_p^\times}x^m\,d\nu_{j,0}
 =\left(1-\xi(\mathfrak p)\frac{\pi_0^m}{\bar\pi_0^{m+1}}\right)
  \Omega_{p,0}^m m!a_{j,m},\qquad m\ge0.}
\tag{42}
$$
特别 $I_1(f_{1,0})=\Omega_{p,0}(1-\xi(\mathfrak p)\pi_0/\bar\pi_0^2)$ 是单位。
这是真正正一次矩，不能直接替代 $I_{-2}(f_{4,0})$。

### 7.2 全部 Euler、Katz 规范与无循环的极限

对合法非负权，取 norm-weight-one 角色
$$
\nu_m=\xi\psi_0^{m+1}\bar\psi_0^{-m}.
\tag{43}
$$
其导子准确等于 $(6)$，且 $\nu_m\nu_m^c=\mathrm N$。
原 Katz 晶格周期插值为
$$
\nu_m(\mathcal L_{(6)}^{\rm prim})
 =\Omega_{p,0}^{2m+1}m!
 \frac{(2\pi/\sqrt3)^m}{\varpi_0^{2m+1}}
 \left(1-\xi(\mathfrak p)\frac{\pi_0^m}{\bar\pi_0^{m+1}}\right)^2
 L(\Phi_m,m+1).
\tag{44}
$$
这就是 R295 所引一般有限导子 Katz 公式的当前特化。两个因子分别为
$1-\nu_m(\mathfrak p)/p$、$1-\nu_m^{-1}(\bar{\mathfrak p})$，因
$\xi(\bar{\mathfrak p})=\xi(\mathfrak p)^{-1}$ 而相同。
二、三处均分歧，没有额外 imprimitive 删除；普通处角色未分歧，其 Gauss 因子为一。
若 Coleman 定义用辅助理想 $(5)$，则
$$
\mathrm N(5)-\nu_m((5))=25-(-5)=30,
\tag{45}
$$
沿整条族固定，对本篇 $p$ 为单位。使用逆平滑约定时须同步反转原椭圆单位；
本篇取 R332 的正约定。

将 (4)、(38) 代入 (44)：
$$
\nu_m(\mathcal L_{(6)}^{\rm prim})
 =c_j\Omega_{p,0}6^{-m}
   (1-\xi(\mathfrak p)e_m)^2 M_{j,m}^2.
\tag{46}
$$
两个阶乘分别来自 Yang 与 Katz，恰好成为 $M_{j,m}^2$。
对固定合法 $m_0$，取 $m_r=m_0+(p-1)p^r$。
它实趋于正无穷、$p$ 进趋于 $m_0$，保持模六与 tame 型。
非单位部分的 $m_r$ 矩赋值至少 $m_r$，Euler 与一之差也至少为 $m_r$。
因此 (46) 的极限直接给单位 Mellin 平方。
所有变化的 $\Omega_{p,0}^{2m_r}$ 已包含于原矩内并准确约去，
不需给任意 $\mathbf C_p$ 单位定义不合法的变指数幂。
这证明第 7.1 节比较所需的整条等式，而没有先假设 (40)。

### 7.3 固定负二次支及返回 $b=17$

设 $d=p-1$、$\langle x\rangle=x/\operatorname{Teich}(x)$，定义
$$
J_{4,-2}(u)=\int_{\mathbf Z_p^\times}
 x^{-2}\langle x\rangle^{du}\,d\nu_{4,0}(x).
$$
令 $\mathcal K_{4,p}(u)$ 为 (43) 在 $m=-2+du$ 的同一实际 $p$ 进分支，
tame 指数始终是 $-2$。由 (46) 的密集正权极限及解析恒等定理，
$$
\boxed{\mathcal K_{4,p}(u)
 =36c_4\Omega_{p,0}
   \langle6\rangle^{-du}J_{4,-2}(u)^2.}
\tag{47}
$$
$u=0$ 即 (6)。这里 $6^{-(-2)}=36$，不能吸进“一个单位”后丢弃。

现在取固定正实 $\theta=17^{1/6}$，并固定其原普通嵌入。
$E_0\to E_{17}$ 的同构为 $(X,Y)\mapsto(\theta^2X,\theta^3Y)$；
微分乘 $\theta^{-1}$。实际形式群同构给
$$
\Omega_{p,0}=\theta\Omega_p,\qquad
f_{4,17}(z)=\theta^{-4}f_{4,0}(\theta z),\qquad
f_{1,17}(z)=\theta^{-1}f_{1,0}(\theta z).
\tag{48}
$$
故这是同一 $\mathbf Z_p$ 变量上的测度等式
$\nu_{4,0}=\theta^4\nu_{4,17}$、$\nu_{1,0}=\theta\nu_{1,17}$，
不是任意代数数对测度变量的乘法。令原 R533 的
$I_{-2}(f_4)=\int x^{-2}d\nu_{4,17}$，准确返回为
$$
\boxed{\nu_-(\mathcal L_{(6)}^{\rm prim})
 =36c_4\,\theta^9\Omega_p\,I_{-2}(f_4)^2,\qquad
\theta^9=17^{3/2}.}
\tag{49}
$$
这完整支付原物理来源的算术读数；仍未断言左端或右端非零。

## 8. 正确反射的根数与不能省略的普通局部比较

由 (43)，固定负点是 $\nu_-=\xi\psi_0^{-1}\bar\psi_0^2$。
裸复共轭为
$$
\nu_-^c=\xi^{-1}\psi_0^2\bar\psi_0^{-1}
 =\xi^{-1}\psi_0^3\mathrm N^{-1}.
\tag{50}
$$
所以其反射复中心是 $L(\xi^{-1}\psi_0^3,2)$，不是 (8) 的值。

令 $\vartheta=\psi_0\mathrm N^{-1/2}$。
比较 $\xi\vartheta^{-3}$ 与 $\xi\vartheta^9$：
二、三处的**完整**局部角色相同，因为幂指数相差十二，
包括两处 uniformizer，而不只包括单位角色。
所有其他有限处未分歧且标准加性角色未分歧，所以局部 epsilon 均为一。
无穷处绝对角权分别为三与九，Fourier–Gaussian 的 epsilon 比是
$$
i^{9-3}=i^6=-1;
\tag{51}
$$
若统一采用共轭 Fourier 约定，仍是同一负号。
$\xi\vartheta^9$ 的中心由 (31)–(34) 的首权 $m=4$ 严格非零，因此根数为 $+1$。
故 $\xi\vartheta^{-3}$ 的根数为 $-1$。同时
$\xi^c=\xi^{-1}$、$\vartheta^c=\vartheta^{-1}$，所以其复共轭角色是
$\xi^{-1}\vartheta^3$；按理想共轭换元，二者整个全球 $L$ 函数相同。
这证明 (7)。

另一方面，$f_1$ 的首权 $m=1$ 读的是 $\xi\vartheta^3$，
完整三处 uniformizer 为 $-i$，其首值由 (34) 非零。
因此“把负二次反射到正一次”时若省掉 $\xi^{-1}$ 与 $\xi$ 的区别，
会把真实负根数错误换成正根数。

还必须区分两个不同操作。R332 已付同一 CM type 的 Katz 对偶 involution 为
$$
\nu\longmapsto\mathrm N(\nu^c)^{-1}.
$$
由于 $\nu_-\nu_-^c=\mathrm N$，该 involution 逐点固定 $\nu_-$，
并不把它送到 $m=1$。裸复共轭虽然给 (50)，却交换 $\mathfrak p$ 与 $\bar{\mathfrak p}$
的普通数据。若要用局部 Fourier／Fricke 再比较两个普通位置，
仍须提供真实全来源、Euler、周期及局部化比较；(7)、(8) 本身不提供它。

因此本篇给出的严格等价是
$$
I_{-2}(f_4)\ne0
\quad\Longleftrightarrow\quad
\nu_-(\mathcal L_{(6)}^{\rm prim})\ne0,
\tag{52}
$$
连同 (49) 的准确常数。它不是目标曲线的 Mordell–Weil 中心；
$E_0$ 的秩零定理也不能替代该固定负权的普通局部非消失。
已有有限模 $p$ 样本可用于寻找新输入，不能提升为所有或无穷多个素数的结论。

## 9. 证书、依赖与可复核范围

[精确脚本](../scripts/check-r540-degree-six-schwartz-and-negative-two.mjs) 和
[原数据](../scripts/check-r540-degree-six-schwartz-and-negative-two.json)
只用 BigInt 有理数与 $\mathbf Q(\zeta_{24})$／$\mathbf Q(\delta)$ 算术。
它们完整核十八元有限角色的乘法、导子及共轭，二处四维矩阵和额外支撑消失，
三处准确 Gauss 符号及 pro-$3$ 全剩余类，Fourier 两个周期、奇偶性和 CM 周期换算。
所有 457 项精确检查通过。支撑的无限陪集积分、整个环面的生成、
全权 theta 识别及 Katz 连续延拓由正文证明，有限证书不代替这些步骤。
脚本没有数值 L 值、浮点认数或有限素数非消失推断。

已出版输入采用以下原文；本篇对固定来源的局部计算已逐项写出：

1. T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math. **485**
   (1997), 25–53，Theorem 1.11、Theorems 2.6、2.15、Corollary 2.14；
   [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
2. T. Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic
   curves*, Compositio Math. **117** (1999), 337–359，Lemma 1.1、
   Proposition 1.2 及 Appendix (A1)–(A3)；
   [作者全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
3. A. Agboola–B. Howard, *Anticyclotomic Iwasawa theory of CM elliptic curves*,
   Ann. Inst. Fourier **56** (2006), 1001–1048，Theorem 2.1.1；
   [出版全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
   本篇只用一般有限导子的 Katz 插值，不把其 Selmer 主猜想结论套到未识别的负权动机。
4. F. Castella–X. Wan, *Perrin-Riou's main conjecture for elliptic curves at
   supersingular primes*, Math. Ann. **389** (2024), 2595–2636，
   Remark 2.2、Theorem 2.4 的 CM 周期与 Katz 插值规范；
   [作者出版稿](https://web.math.ucsb.edu/~castella/Perrin-Riou-print.pdf)。
5. [R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、
   [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
   [R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
   [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)、
   [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)
   固定原 sigma 整性、全部 trace 半特征、基曲线角色、Haar／周期规范和正确的同 CM-type involution。
