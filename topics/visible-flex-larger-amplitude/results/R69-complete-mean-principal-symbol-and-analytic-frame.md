# R69 — 完整均值主符号、真实剪切与解析权的条件传播界

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

**状态：完整条件工具。** 本文证明实际 Darboux 一阶系统的主符号恒等式，列出剪切及 frame 的全部导数项，并给一个明确支付 Fourier 权交换的线性先验界。本文没有计算 outer $0,\ldots,11$ 的这些系数积分，也没有支付该非线性边值问题的 Green/Schur 门。点态相似性不被当作完整传播证明。

使用 [R41](R41-exact-angular-connection-inverse.md)、[R44](R44-compatible-outer-height-and-continuous-defect.md)、[R64](R64-general-outer-mean-and-compatible-defect.md) 的完整根和真实高度约定。R68 的背景最优 frame 结果是下述主符号在轴对称背景处的一个特例；其已付数值不自动支付本文的非轴对称系数。

## 1. 变量、完整均值与正支

在一个真实 source 坐标区间取 $r=r(x)>0$、$r_x>0$、$w=w(x)>0$，并记

$$
s=\frac{r_x}{r},\qquad
\ell=\frac{w_x}{w},\qquad
z=w^2,\qquad E=1+z.
\tag{69.1}
$$

度量是 $g=E\,dr^2+r^2d\theta^2$。对一个真实高度 $h$ 定义

$$
P=\frac{h_\theta}{rw},\qquad
K=\frac{h_r}{w}-1=c(x)+\bar K(x,\theta),\qquad
\langle\bar K\rangle=0.
\tag{69.2}
$$

这里 $c$ 是完整均值方程的既有唯一小分支，**不是截断均值，也不是任意置零**。可以使用 R64 已证的端点符号和严格单调门；其中

$$
M_c=\left\langle L D^{-3/2}\right\rangle>0.
\tag{69.3}
$$

保留该根的全部正支条件，包括 R64 的 $S,D,y,N,L$ 正性。下述符号恒等式本身只需 $D>0,L>0$，但由它们反推几何根时仍须满足原完整分支条件。

再记

$$
T=P_\theta,\qquad V=K_\theta,\qquad U=V-P,
\qquad L=1+K+ET,
$$

$$
D=1-z(2K+K^2+EP^2).
\tag{69.4}
$$

定义完整有理源

$$
\begin{aligned}
\mathcal A
&=EsU^2+\ell\bigl((K+T)^2+z(2KT+T^2-P^2)\bigr),\\
\mathcal N(P,K,T,V;x)&=\mathcal A/L.
\end{aligned}
\tag{69.5}
$$

均值 $c$ 已经包含在每个 $K$ 和 $L$ 中。不能只把 $\bar K$ 代入 (69.5)。也没有删去 $w^2$ 项或将 $L^{-1}$ 换成有限阶近似。

假设本文涉及的中心场足够光滑，使所有列出的 $x,\theta$ 导数存在；在解析传播部分还明确要求相应 Fourier 系数范数有限且可积。R48/R66 的实际有限候选及其完整均值可以作为计算这些条件的输入，但已付缺陷上界本身不替代这些系数条件。

## 2. 真实系统及线性化的偏导约定

高度兼容恒等式给出

$$
P_x=sK_\theta-(s+\ell)P.
\tag{69.6}
$$

在 R44 的同一正支上，真实 Darboux 方程等价于

$$
K_x=-\ell(2K+T)+\mathcal N.
\tag{69.7}
$$

对一个兼容但未必精确的候选，(69.6) 仍恒等成立；(69.7) 的差就是需要支付的真实第二源分量。本文不以 (69.7) 重定义候选导数。

以下偏导 $\mathcal N_P,\mathcal N_K,\mathcal N_T,\mathcal N_V$ 均是在固定真实 $x$ 下，把 $P,K,T,V$ 当作四个独立实变量的偏导。特别是 $\mathcal N_K$ 中的 $K$ 包括完整零模。若之后用隐式根消去零模，其导数须另外保留；本文的全变量线性化没有省略它。

直接求导得

$$
\begin{aligned}
\mathcal N_V&=\frac{2EsU}{L},\\
\mathcal N_T&=\frac{2\ell E(K+T)L-E\mathcal A}{L^2},\\
\mathcal N_K&=\frac{\ell(2K+2ET)L-\mathcal A}{L^2},\\
\mathcal N_P&=\frac{-2EsU-2\ell zP}{L}.
\end{aligned}
\tag{69.8}
$$

在给定中心场线性化，令 $X=(p,k)^t$ 为完整变化量。其线性部分是

$$
X_x=A X_\theta+C X+f,
\tag{69.9}
$$

$$
A=\begin{pmatrix}0&s\\ \mathcal N_T-\ell&\mathcal N_V\end{pmatrix},
\qquad
C=\begin{pmatrix}-(s+\ell)&0\\ \mathcal N_P&-2\ell+\mathcal N_K\end{pmatrix}.
\tag{69.10}
$$

这里 $f$ 可以包含候选残差和另行核销的高阶项。对同一高度候选的原兼容残差，第一源分量精确为零，$f=(0,f_K)^t$。这项零结构不把非线性余项或完整均值源删去。

**证明。** (69.6) 由 $h_{r\theta}=wK_\theta$ 及 $h_\theta=rwP$ 逐项求导。将 (69.7) 乘以 $L$，使用

$$
(2K+T)L-\bigl((K+T)^2+z(2KT+T^2-P^2)\bigr)
=2K+K^2+zP^2+(1+K)T,
$$

即得到 R44/R64 的完整有限 $J$ 公式。再对四个变量逐项求导得 (69.8)，并将 $p_\theta,k_\theta$ 项与零阶项分开，得到 (69.9)–(69.10)。全过程未使用 $K$ 的小幅假设。证毕。

## 3. 精确主符号恒等式

**定理 69.1。** 在上述正支上，令

$$
a=\frac{EU}{L},\qquad \alpha=sa=\frac{EsU}{L},\qquad d=\frac{D}{L^2}>0.
\tag{69.11}
$$

则

$$
\operatorname{tr}A=2\alpha,
\qquad
(\operatorname{tr}A)^2-4\det A=-4s\ell d,
\tag{69.12}
$$

且真实三角剪切

$$
S=\begin{pmatrix}1&0\\-a&1\end{pmatrix}
\tag{69.13}
$$

满足

$$
SAS^{-1}=\widetilde A
=\alpha I+\begin{pmatrix}0&s\\-\ell d&0\end{pmatrix}.
\tag{69.14}
$$

因此在 $D,L>0,s>0$ 下，点态主符号的实/复特征型仅由 $\ell$ 的符号决定。$\ell<0$ 时两条特征值为实数；$\ell>0$ 时为一对共轭非实数；$\ell=0$ 时退化。这里只是点态代数结论。

**证明。** 因 $\mathcal N_V=2\alpha$，只需验证

$$
\alpha^2+s(\mathcal N_T-\ell)=-s\ell D/L^2.
\tag{69.15}
$$

乘以 $L^2/s$，左端化为

$$
E^2sU^2+2\ell E(K+T)L-E\mathcal A-\ell L^2.
$$

用 (69.5) 消去 $E^2sU^2$，余项是 $\ell$ 乘以

$$
2E(K+T)L-E\bigl(K^2+2EKT+ET^2-zP^2\bigr)-L^2.
$$

展开 $L=1+K+ET$ 后，所有 $KT,T^2,T$ 项相消，剩下

$$
-1+z(2K+K^2+EP^2)=-D.
$$

这证明 (69.15)。将 $a=\alpha/s$ 代入三角矩阵乘法，左下项为 $\mathcal N_T-\ell+\alpha^2/s=-\ell d$，两条对角线均为 $\alpha$，得到 (69.14)。特征值为 $\alpha\pm\sqrt{-s\ell d}$，故型的结论成立。证毕。

## 4. 剪切导数与完整变换后方程

不能将 $SAS^{-1}$ 直接代替原系统而丢弃 $S$ 的变化。令 $Y=SX$，逐项求导得到

$$
Y_x=\widetilde A Y_\theta+\widetilde C Y+Sf,
\tag{69.16}
$$

$$
\widetilde C
=SCS^{-1}+S_xS^{-1}+SA(S^{-1})_\theta
=SCS^{-1}+
\begin{pmatrix}s a_\theta&0\\-a_x+\alpha a_\theta&0\end{pmatrix}.
\tag{69.17}
$$

这是精确等式，不是一个省略低阶项的符号等价。

所需导数可以直接由真实候选计算：

$$
\begin{aligned}
E_x&=2z\ell,\\
U_x&=(K_x)_\theta-P_x,\\
L_x&=K_x+E_xT+E(P_x)_\theta,\\
a_x&=\frac{E_xU+EU_x}{L}-\frac{EU L_x}{L^2},\\
a_\theta&=\frac{E(K_{\theta\theta}-T)}{L}
-\frac{EU(K_\theta+E P_{\theta\theta})}{L^2}.
\end{aligned}
\tag{69.18}
$$

这里 $K_x$ 必须取候选实际导数，包括完整 $c_x$；对非精确候选不能用 (69.7) 无条件代入。$P_x$ 可使用恒等的 (69.6)。R48 已保存的实际高度/归一斜率多项式和 R64 的完整均值导数提供一个具体输入接口。

如果 $f=(0,f_K)^t$，则 $Sf=f$。第一源列为零的结构在这次真实剪切下保持。

## 5. 正 frame、$b<1$ 与接口跳变

令 $b=b(x)>0$ 与 $\theta$ 无关，允许在有限个真实面板边界跳变。面板内部取 $W=B Y$、$B=\operatorname{diag}(b,1)$。则

$$
W_x=\widehat A W_\theta+\widehat C W+B S f,
\tag{69.19}
$$

$$
\widehat A=\alpha I+
\begin{pmatrix}0&sb\\-\ell d/b&0\end{pmatrix},\qquad
\widehat C=B\widetilde C B^{-1}+
\begin{pmatrix}b_x/b&0\\0&0\end{pmatrix}.
\tag{69.20}
$$

一个面板内选精确正 dyadic 常数 $b$ 时，最后的 $b_x/b$ 项为零，但边界跳变仍必须付。若同一 $a$ 在边界连续，则

$$
W^+=\operatorname{diag}(b^+/b^-,1)W^-.
\tag{69.21}
$$

正向和反向的精确范数成本分别是 $\max(1,b^+/b^-)$、$\max(1,b^-/b^+)$。一般有 $a$ 跳变时，必须使用完整的 $B^+S^+(B^-S^-)^{-1}$。对共享相同物理两 jet 的 R48 候选，$P,K,U,L$ 及 $a$ 在真实几何接口相同；source 坐标的不同速度不会改变 $a=EU/L$。

在任一端口，转回原未知量的成本可由

$$
\|BS\|\le\max(b,1)(1+\|a\|_{A_\tau}),\qquad
\|(BS)^{-1}\|\le\max(1,b^{-1})(1+\|a\|_{A_\tau})
\tag{69.22}
$$

控制。这里范数指下一节的加权 Fourier $\ell^2$ 上的乘法算子。故 $b<1$ 不能免付 $b^{-1}$ 的逆端口因子。若第一源分量为零，则 $BSf=f$，但这不消除解的端口或中途跳变成本。

## 6. 一个明确支付解析交换的 Fourier 能量界

本节给出条件先验估计。它适用于满足条件的光滑解析解，也逐项适用于变换后方程 (69.19) 的任意有限 Fourier Galerkin 系统；不声称对原方程先截断再作非恒定剪切与此投影完全相同。本节不另外声称一个尚未核销的非线性存在定理。

写

$$
\widehat A(x,\theta)=\sum_{j\in\mathbb Z}A_j(x)e^{ij\theta},\quad
\widehat C(x,\theta)=\sum_j C_j(x)e^{ij\theta}.
$$

所有矩阵系数范数取欧氏算子范数。定义

$$
\begin{aligned}
\gamma_0&=\frac12\|A_0-A_0^t\|
=\frac12\left|sb+\frac{\ell}{b}\langle d\rangle\right|,\\
\gamma_1(\tau)&=\sum_{j\ne0}e^{\tau|j|}\|A_j\|,\\
\chi_1(\tau)&=\sum_{j\ne0}|j|e^{\tau|j|}\|A_j\|,\\
C_*(\tau)&=\sum_j e^{\tau|j|}\|C_j\|.
\end{aligned}
\tag{69.23}
$$

中心为真实实场时 $A_0$ 为实矩阵，且 (69.20) 给出上式的 $\gamma_0$。在无需精确逐矩阵范数的实现中，可用

$$
\begin{aligned}
\gamma_1(\tau)&\le
\|\alpha-\langle\alpha\rangle\|_{A_\tau}
+\frac{|\ell|}{b}\|d-\langle d\rangle\|_{A_\tau},\\
\chi_1(\tau)&\le
\|\alpha_\theta\|_{A_\tau}
+\frac{|\ell|}{b}\|d_\theta\|_{A_\tau}.
\end{aligned}
\tag{69.24}
$$

这些非零 Fourier 成本是实际条件，不能由点态特征值直接删去。

对绝对连续角宽 $\tau(x)>0$，设

$$
\mathcal E(x)=\sum_m e^{2\tau(x)|m|}\|W_m(x)\|^2,
\qquad
\mathcal Q(x)=\sum_m |m|e^{2\tau(x)|m|}\|W_m(x)\|^2.
$$

**定理 69.2。** 假设 (69.23) 的量及源范数在所考察面板可积，且

$$
\tau'(x)+\gamma_0(x)+\gamma_1(\tau(x))\le0
\quad\text{a.e.}
\tag{69.25}
$$

则对于 (69.19) 的上述解，令 $F=BSf$，有

$$
\frac{d}{dx}\sqrt{\mathcal E}
\le\bigl(\chi_1(\tau)+C_*(\tau)\bigr)\sqrt{\mathcal E}
+\|F\|_{\ell^2_\tau}
\tag{69.26}
$$

的积分形式。具体地，$\Lambda=\chi_1+C_*$ 时

$$
\|W(x)\|_{\ell^2_{\tau(x)}}
\le e^{\int_a^x\Lambda}\|W(a)\|_{\ell^2_{\tau(a)}}
+\int_a^x e^{\int_t^x\Lambda}\|F(t)\|_{\ell^2_{\tau(t)}}\,dt.
\tag{69.27}
$$

跨面板时还须乘 (69.21) 的实际跳变因子，并付 (69.22) 的端口换元。反向传播用反向坐标重写方程，角宽按传播方向递减；相同的 $\gamma_0,\gamma_1,\chi_1,C_*$ 上界及反向跳变成本仍有效。

**证明。** 令 $Z_m=e^{\tau|m|}W_m$。角宽求导给出 $\tau'\mathcal Q$。常数矩阵项满足

$$
\operatorname{Re}\langle Z_m,imA_0Z_m\rangle
\le |m|\gamma_0\|Z_m\|^2.
$$

非零系数 $j=m-n$ 的加权因子至多为 $e^{\tau|j|}$，因为 $|m|-|n|\le|j|$。另有精确不等式

$$
|n|\le\sqrt{|m||n|}+|m-n|.
\tag{69.28}
$$

当 $|n|\ge|m|$ 时，将 $|n|-\sqrt{|m||n|}$ 有理化便得到它不大于 $|n|-|m|\le|m-n|$；另一情形显然成立。对每个固定 $j$，Cauchy–Schwarz 给出

$$
\sum_m\sqrt{|m||m-j|}\|Z_m\|\|Z_{m-j}\|\le\mathcal Q,
\quad
\sum_m\|Z_m\|\|Z_{m-j}\|\le\mathcal E.
$$

因此全部非零主系数贡献不超过 $\gamma_1\mathcal Q+\chi_1\mathcal E$。这一步明确保留了 Fourier 权的交换损失。零阶卷积由 Young 不等式不超过 $C_*\mathcal E$，源项不超过 $\sqrt{\mathcal E}\|F\|_{\ell^2_\tau}$。相加得到

$$
\tfrac12\mathcal E'
\le(\tau'+\gamma_0+\gamma_1)\mathcal Q
+(\chi_1+C_*)\mathcal E
+\sqrt{\mathcal E}\|F\|_{\ell^2_\tau}.
$$

利用 (69.25)，对 $\sqrt{\mathcal E+\varepsilon}$ 积分再令 $\varepsilon\downarrow0$，得 (69.26)–(69.27)。对有限 Galerkin 系统，投影在能量内积中因 $Z$ 已在该空间而消去，故同一估计逐项成立；对上述解析解以绝对收敛或有限截断极限证明相同等式。界面与反向成本由精确换元直接得到。证毕。

## 7. 范数转换、完整均值和未付项

本节的 $\ell^2_\tau$ 不是免费等同于外头使用的 Wiener 一阶范数。若 $0\le\sigma<\tau$、$\delta=\tau-\sigma$，则

$$
\sum_m(1+|m|)e^{\sigma|m|}\|X_m\|_2
\le C_\delta\|X\|_{\ell^2_\tau},
\qquad
C_\delta^2=\frac{2(1+e^{-2\delta})}{(1-e^{-2\delta})^3}-1.
\tag{69.29}
$$

这是 Cauchy–Schwarz 和全整数频率几何级数的直接结果；若要分别相加两个分量的 Wiener 范数，另付 $\sqrt2$。本课题的偶频率子空间可以使用这个保守的全整数界。$\delta=0$ 时不能使用它。

完整零模包含在上述能量里。$\langle P\rangle=0$ 由高度定义和 (69.6) 保持；$K$ 的零模则由原完整根及其导数决定。若采用消去均值的变量，必须明确支付这个隐式函数的导数以及 $M_c^{-1}$。本文直接在包含该零模的较大线性空间估计，故没有靠丢掉它缩小算子。

要将本文用于实际全 outer 误差闭合，至少还须核销下列互不等价的量：

1. 同一真实 $g$、同一兼容候选上的完整 root/分支域与邻域；不能仅引用有限 endpoint 正性。
2. $a,a_x,a_\theta,d,d_\theta,\mathcal N_P,\mathcal N_K$ 的连续 Fourier 界，包括候选的真实 $K_x$ 和完整 $c_x$。
3. 所选 $b$ 的全部跳变、端口因子与 (69.23)–(69.25) 的实际角宽账本；不能仅支付 $\int\sqrt{s\ell d}$。
4. 有源项在真实位置、正确 source 测度上的 (69.27) 积分，以及接到既定 Wiener 范数时的严格宽度损失。
5. 参数化真内头迹、完整外侧边界条件、有限 Schur 逆和非线性 Taylor 余项。线性估计不自动给这一固定点。

特别地，轴对称背景处 $P=K=T=V=0$，故 $a=\alpha=0,d=1$，而 $\gamma_1=\chi_1=0$，主符号成本回到 $\tfrac12|sb+\ell/b|$。这解释了 R68 在 $\ell<0$ 时能够通过正 frame 支付的抵消；一般非轴对称中心的 $\gamma_1,\chi_1,\widetilde C$ 仍是真正新增的项目。
