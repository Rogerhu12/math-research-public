# 首支撑有序的二次偏离：有限 dyadic 差、核内单位与完整 Fourier 排核

日期：2026-11-13（UTC）。作者：central_review。供主会话独立复核后登记。
状态：下述定理的证明已在本文逐步完成；一般 Hilbert 不变子空间问题仍未完成。

## 1. 结论与准确范围

沿用本课题的原 Haar 模型
$$
H=L^2(\mathbb Z_2,\mu),\qquad
\mathcal A=\overline{\mathbb C[I,A]},
$$
其中 $A$ 为原单射拟幂零加权 odometer，
$\omega>0$ 几乎处处；$A$ 的唯一谱点为 $0$。
记
$$
N_j=A^{2^j}/d_j,\qquad
d_j=\|A^{2^j}\|>0,\qquad
V(z)=\frac{1-z}{1+z}.
$$

取任意
$$
a,b\in\ell^2(\mathbb C),\qquad
a_*,b_*\in\mathbb C,\qquad
c\in\ell^1(\mathbb C),\quad c\ne0,
$$
并定义
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
w=b_*+\sum_{j\ge0}b_j\chi_j.
\tag{1.1}
$$
所有一阶级数均按实际 $\ell^2$ Haar 意义理解。
令
$$
j_a=\min\{j:a_j\ne0\},\qquad
j_c=\min\{j:c_j\ne0\},
\tag{1.2}
$$
空集的最小值记为 $+\infty$；因 $c\ne0$，$j_c$ 有限。

**定理 1。** 若
$$
\boxed{j_c\le j_a,}
\tag{1.3}
$$
则向量
$$
\boxed{
f=
\left[
u^2+\sum_{j\ge0}(2a_j^2+c_j)(\chi_j-1)
\right]e^w
}
\tag{1.4}
$$
非零且对原 $A$ 循环。

主系数与偏离系数均允许任意复相位。
没有主尾的幂率、重排、同射线或预解增长假设。
偏离只要求可和及首支撑条件 (1.3)，不要求
$|c_j|\asymp |a_j|^\kappa$。
指数权允许任意复 $\ell^2$ 系数。
特别允许 $a_*=0$，也允许主一阶级数不属于 $\ell^1$。
若所有 $a_j=0$，按 (1.2) 的约定，定理同样适用。

本稿不处理 $j_c>j_a$ 的一般情形。
最后一节说明本证明在该处缺少哪一个准确命题，
并核对旧 R270C/D 没有提供它。

## 2. 原闭算子、自然域与点态向量

设
$$
t_j=e^{-2b_j},\qquad R_j=V(t_jN_j).
\tag{2.1}
$$
这些均为真正有界的 $\mathcal A$ 元素。
R176 §10.1 给固定 $b\in\ell^2$ 下的统一范数界，
并构造实际倾斜闭 first $X=X_b$。
这里没有把非 $\ell^1$ 主系数的 first 写成算子范数收敛级数。
若全部 $a_j=0$，则直接取 $X=a_*I$，全部自然幂域均为 $H$；
本节的闭性、域交换和图核心事实在这个有界退化情形直接成立，
不依赖 R176 开头的非零主行假设。

定义
$$
Y=\sum_{j\ge0}c_j(R_j-I),\qquad
B=\sum_{j\ge0}a_j^2(R_j-I)^2.
\tag{2.2}
$$
因为 $c\in\ell^1$、$a\in\ell^2$，
两式按算子范数绝对收敛。
它们属于 $\mathcal A$，且
$$
\chi(Y)=\chi(B)=0.
\tag{2.3}
$$
本稿不要求 $Y\in\mathcal G$。

取
$$
T=X^2+Y-B,\qquad
\operatorname{Dom}T=\operatorname{Dom}X^2.
\tag{2.4}
$$
R176 的自然首一多项式定理与其复倾斜版本证明：

- $T$ 在 (2.4) 的准确自然域上闭；
- 它对原共轭
  $C h(y)=\overline{h(-1-y)}$
  完整自伴，即 $T=CT^*C$；
- 所有有界 $\mathcal A$ 系数与 $X$ 完整域交换，并保持其全部自然幂域；
- $\xi=e^w$ 循环且属于 $\bigcap_{p\ge1}\operatorname{Dom}X^p$；
- $\operatorname{span}\{A^n\xi:n\ge0\}$ 是 $T$ 的图核心。

二阶 Bell 恒等式为
$$
X^2\xi
=
u^2\xi-\sum_j a_j^2(I-R_j^2)\xi.
$$
又 $R_j\xi=\chi_j\xi$，所以
$$
\begin{aligned}
T\xi
&=
\left[
u^2+\sum_j a_j^2\{-I+R_j^2-(R_j-I)^2\}
+\sum_j c_j(R_j-I)
\right]\xi\\
&=
\left[
u^2+\sum_j(2a_j^2+c_j)(\chi_j-1)
\right]\xi=f.
\end{aligned}
\tag{2.5}
$$
上述有界尾均按范数收敛，向量恒等式来自实际自然域，
不是仅在形式符号中相等。
由真实图核心，
$$
[f]_A=\overline{\operatorname{Ran}T}.
\tag{2.6}
$$
因此只须证明 $\ker T=0$；完整 $C$ 自伴性随后给稠密像。

## 3. 未知核上的一阶限制是拟幂零有界算子

反设
$$
M=\ker T\ne0.
$$
R176 §8 的最大图与固定正则器论证给
$$
M\subset\bigcap_{p\ge1}\operatorname{Dom}X^p,\qquad
X_M:=X|_M\in\mathcal B(M).
\tag{3.1}
$$
$M$ 闭且 $A$ 不变；所有 $\mathcal A$ 元素保持 $M$。
在该真实核上，
$$
X_M^2=(B-Y)|_M.
\tag{3.2}
$$

由 (2.3)，$B-Y$ 在单字符代数 $\mathcal A$ 中拟幂零。
限制的幂范数不超过原算子的幂范数，故
$$
r\bigl((B-Y)|_M\bigr)=0.
$$
由 (3.2) 与有界谱映射，
$$
\boxed{\sigma(X_M)=\{0\}.}
\tag{3.3}
$$
没有把全空间闭 $X$ 的谱传给未知限制；
(3.3) 仅由核内有界性及真实平方关系推出。

若 $F\in\mathcal A$，则 $F_M$ 与 $X_M$ 交换，而且
$$
(F_MX_M)^n=F_M^nX_M^n.
$$
因此
$$
r(F_MX_M)
\le \|F_M\|\,r(X_M)=0,
$$
并得到
$$
\boxed{I_M+F_MX_M\text{ 在 }M\text{ 上有有界逆}.}
\tag{3.4}
$$
这是只在当前固定未知核上使用的逆，不宣称相应全空间闭算子有预解。

## 4. Dyadic gauge 的完整域恒等式

令
$$
\Gamma=\bigcup_{h\ge0}\mu_{2^h},\qquad
(U_\zeta v)(y)=\zeta^y v(y),\qquad
\gamma_\zeta(S)=U_\zeta S U_\zeta^*.
\tag{4.1}
$$
对 $\zeta^{2^h}=1$，
$$
\gamma_\zeta(A)=\zeta A,\qquad
\gamma_\zeta(N_j)=\zeta^{2^j}N_j.
\tag{4.2}
$$
当 $j\ge h$ 时最后一个相位等于 $1$。

R176 §9 与 R270C §1 已证明实际闭算子及全部自然幂域的恒等式
$$
\gamma_\zeta(X)=X+D_\zeta,\qquad
U_\zeta\operatorname{Dom}X^p=\operatorname{Dom}X^p,
\tag{4.3}
$$
其中
$$
D_\zeta
=
\sum_{j<h}a_j
\left[
V(t_j\zeta^{2^j}N_j)-V(t_jN_j)
\right].
\tag{4.4}
$$
这是有限个真正解析函数的和，属于真正标量解析演算，
并与 $X$ 完整域交换。
整个过程不涉及未定义的 $\sum_j a_j$。

类似地，
$$
\Delta_\zeta Y=\gamma_\zeta(Y)-Y,\qquad
\Delta_\zeta B=\gamma_\zeta(B)-B
\tag{4.5}
$$
均为真正解析有限头。
原因是两式的高位项在 (4.2) 下逐项完全不变，
而原级数按范数绝对收敛。

在同一个准确域 $\operatorname{Dom}X^2$ 上，
$$
\begin{aligned}
\gamma_\zeta(T)-T
&=(X+D_\zeta)^2-X^2+\Delta_\zeta Y-\Delta_\zeta B\\
&=2D_\zeta X+E_\zeta,
\end{aligned}
\tag{4.6}
$$
其中
$$
E_\zeta=D_\zeta^2+\Delta_\zeta Y-\Delta_\zeta B.
\tag{4.7}
$$
共轭后的算子仍是关于 $X$ 的首一二次自然多项式，
系数有界且完整域交换，所以仍完整 $C$ 自伴。
亦可直接使用 $CU_\zeta C=\zeta U_\zeta$ 验证，
其中出现的标量在共轭 $U_\zeta T U_\zeta^*$ 中相消。

## 5. 首支撑顺序给真解析分解

置
$$
m=2^{j_c}.
$$
固定任意
$$
\zeta\in\Gamma,\qquad \zeta^m\ne1.
\tag{5.1}
$$
下文的每个解析函数均只需在零点的一个实际邻域收敛；
其邻域和范数可以依赖当前固定 $\zeta$。

若 $A$ 的形式变量记为 $z$，则
$$
V(t_j z^{2^j}/d_j)
=
1-\frac{2t_j}{d_j}z^{2^j}
+O(z^{2^{j+1}}).
\tag{5.2}
$$
故
$$
V(t_j\zeta^{2^j}z^{2^j}/d_j)
-
V(t_jz^{2^j}/d_j)
=
-\frac{2t_j}{d_j}(\zeta^{2^j}-1)z^{2^j}
+O(z^{2^{j+1}}).
\tag{5.3}
$$

由 $j_c$ 的定义及 (5.1)，$\Delta_\zeta Y$ 的精确首阶为 $m$，
其首系数为
$$
-\frac{2c_{j_c}t_{j_c}}{d_{j_c}}(\zeta^m-1)\ne0.
\tag{5.4}
$$
没有较高物理位能贡献 $z^m$ 项。

若 $j_a<\infty$，则 (4.4) 中每个非零项的首阶至少为 $2^{j_a}$。
某些相位可能使整项为零，这只会提高首阶。
因此
$$
\operatorname{ord}D_\zeta\ge 2^{j_a}\ge m,
\tag{5.5}
$$
并且
$$
\operatorname{ord}D_\zeta^2\ge 2^{j_a+1}>m.
\tag{5.6}
$$
又每个 $(R_j-I)^2$ 的首阶至少为 $2^{j+1}$，故
$$
\operatorname{ord}\Delta_\zeta B\ge 2^{j_a+1}>m.
\tag{5.7}
$$
若全部 $a_j=0$，则 $D_\zeta=B=0$，
同样满足此处所需的消失条件。

由 (4.7)、(5.4)–(5.7)，
$$
E_\zeta=e_\zeta(A),\qquad
e_\zeta(z)=z^m e_{\zeta,0}(z),\qquad
e_{\zeta,0}(0)\ne0.
\tag{5.8}
$$
同时存在真正解析芽 $d_{\zeta,0}$ 使
$$
D_\zeta=A^m d_{\zeta,0}(A).
\tag{5.9}
$$
因此真正解析芽
$$
f_\zeta(z)=\frac{2d_{\zeta,0}(z)}{e_{\zeta,0}(z)}
\tag{5.10}
$$
在零点某个邻域有定义。
用 $A$ 的通常全纯演算定义
$$
F_\zeta=f_\zeta(A)\in\mathcal A.
$$
没有取 $E_\zeta^{-1}$，
也没有把形式除以 $A^m$ 直接当成有界除法；
(5.8)–(5.10) 是两个实际解析芽的可去因子与非零常数分母。

准确有
$$
E_\zeta F_\zeta=2D_\zeta,
$$
于是 (4.6) 成为实际域恒等式
$$
\boxed{
\gamma_\zeta(T)-T
=
E_\zeta(I+F_\zeta X)
\quad\text{于 }\operatorname{Dom}X^2.
}
\tag{5.11}
$$

当 $j_c=j_a=j_0$ 时，
$$
F_\zeta(0)=\frac{2a_{j_0}}{c_{j_0}},
$$
也可写成
$$
\gamma_\zeta(T)-T
=
2D_\zeta(X+K_\zeta),\qquad
K_\zeta(0)=\frac{c_{j_0}}{2a_{j_0}}\ne0.
\tag{5.12}
$$
当 $j_c<j_a$ 时，(5.11) 同时涵盖 $D_\zeta=0$ 的情况；
不须另选一个一定改变主 first 的字符。

## 6. 差算子在同一个未知核上的像稠密

$E_\zeta$ 是非零真解析演算，故属于 R151 的 $\mathcal G$。
该文 §3.1 的结论精确作用于每个闭 $A$ 不变空间：
$$
\overline{E_\zeta M}=M.
\tag{6.1}
$$
这里调用的是已经证明的普遍限制稠密性，
不是从 $E_\zeta H$ 稠密推断 (6.1)。
对于本稿的真解析因子，也可由
$E_\zeta=A^m e_{\zeta,0}(A)$、
$e_{\zeta,0}(A)$ 为 $\mathcal A$ 单位，
以及 $A^m$ 的同一限制稠密性质直接得到。

由 (3.4)，
$$
W_{\zeta,M}=I_M+(F_\zeta)_M X_M
$$
在 $M$ 上有有界逆。
$E_\zeta,F_\zeta$ 保持 $M$，
$X_M$ 已是全域有界限制，
所以 (5.11) 在 $M$ 上是有界算子恒等式，并给
$$
\begin{aligned}
(\gamma_\zeta T-T)M
&=(E_\zeta)_M W_{\zeta,M}M\\
&=E_\zeta M.
\end{aligned}
\tag{6.2}
$$
从而
$$
\boxed{
\overline{(\gamma_\zeta T-T)M}=M
\qquad(\zeta^m\ne1).
}
\tag{6.3}
$$
本步不需要上述逆对不同 $\zeta$ 一致有界。
整个证明逐个处理固定字符。

## 7. 正确方向的 C 配对

原双线性配对为
$$
\mathcal B(v,z)
=
\int_{\mathbb Z_2}v(y)z(-1-y)\,d\mu(y).
\tag{7.1}
$$
它满足
$$
|\mathcal B(v,z)|\le\|v\|_2\|z\|_2.
$$
不假定 $CM=M$。

由实际域等式 (4.3)，
$$
M_\zeta:=U_\zeta M
=
\ker\gamma_\zeta(T),
\qquad
M,M_\zeta\subset\operatorname{Dom}X^2.
\tag{7.2}
$$
取 $v\in M$、$z\in M_\zeta$。
完整自然域上的 $\mathcal B$ 对称性给
$$
\begin{aligned}
\mathcal B((\gamma_\zeta T-T)v,z)
&=\mathcal B(\gamma_\zeta T v,z)-\mathcal B(Tv,z)\\
&=\mathcal B(v,\gamma_\zeta T z)-0\\
&=0.
\end{aligned}
\tag{7.3}
$$
第一行所有算子作用有定义；
第二行移动的是 $\gamma_\zeta T$，
其右端确实杀掉 $z\in M_\zeta$。

现在使用 (6.3) 在左端的稠密像以及 (7.1) 的连续性：
$$
\boxed{
\mathcal B(M,U_\zeta M)=0
\qquad(\zeta\notin\mu_m).
}
\tag{7.4}
$$
没有把 $U_\zeta$ 当成保持 $M$，
也没有把原空间 $C$ 自伴性传给 $M$ 上的限制。

## 8. 有限 Fourier 支撑与逐柱维数

对任意 $v,z\in M$，置
$$
h_{v,z}(y)=v(y)z(-1-y).
$$
由 Cauchy–Schwarz，$h_{v,z}\in L^1(\mu)$。
准确计算
$$
\mathcal B(v,U_\zeta z)
=
\zeta^{-1}\int_{\mathbb Z_2}
h_{v,z}(y)\zeta^{-y}\,d\mu(y).
\tag{8.1}
$$
因此 (7.4) 说明 $h_{v,z}$ 的所有
$\Gamma\setminus\mu_m$ Fourier 系数为零。

令 $\mathbb E_n$ 为模 $2^n$ 柱代数的 Haar 条件期望。
当 $2^n\ge m$ 时，$\mathbb E_n h_{v,z}$ 的 Fourier 展开只剩
$\mu_m$ 中的有限字符，故这些条件期望等于同一个函数，
并在每个模 $m$ 柱上为常数。
又
$$
\mathbb E_n h_{v,z}\longrightarrow h_{v,z}
\quad\text{于 }L^1,
$$
所以
$$
\boxed{
v(y)z(-1-y)
\text{ 在每个模 }m\text{ 柱上几乎处处为常数}.
}
\tag{8.2}
$$

下面写全从总本质支撑到有限维的步骤。
取 $M$ 的可数稠密族 $(v_n)$，令
$$
E=\bigcup_n\{y:v_n(y)\ne0\}
$$
为其总本质支撑，按零测集等价理解。
任何 $v\in M$ 都在 $E^c$ 上为零。
因 $AM\subset M$ 且原权 $\omega>0$ 几乎处处，
各 $Av_n$ 的本质支撑是 $v_n$ 支撑的 odometer 平移，
从而
$$
E+1\subset E\quad\text{模零测集}.
$$
Haar 测度平移不变使包含成为几乎处处相等。
由 odometer 遍历性，$\mu(E)$ 只能为 $0$ 或 $1$。
$M\ne0$ 迫
$$
\mu(E)=1.
\tag{8.3}
$$
反射集合 $-1-E$ 也全测。

固定一个模 $m$ 柱 $C_r$。
由 (8.3)，可数集合
$$
\{y\in C_r:v_n(y)v_\ell(-1-y)\ne0\},
\qquad n,\ell\ge1,
$$
的并覆盖 $C_r$ 的几乎全部。
因此至少有一对 $(n_r,\ell_r)$ 的乘积在该柱正测集上非零。
但由 (8.2)，该乘积已是柱常数，故存在 $k_r\ne0$ 使
$$
v_{n_r}(y)v_{\ell_r}(-1-y)=k_r
\quad\text{几乎处处于 }C_r.
\tag{8.4}
$$
特别，两个因子均在整柱几乎处处非零。

对任意 $v\in M$，(8.2) 再给某个柱常数 $k_r(v)$：
$$
v(y)v_{\ell_r}(-1-y)=k_r(v)
\quad\text{于 }C_r.
$$
除以 (8.4) 的非零因子，得到
$$
v|_{C_r}
=
\frac{k_r(v)}{k_r}v_{n_r}|_{C_r}.
\tag{8.5}
$$
所以 $M$ 在每个柱上的限制空间维数至多为 $1$。
模 $m$ 共有 $m$ 个柱，所有柱的联合限制映射是单射，
因此
$$
\boxed{\dim M\le m.}
\tag{8.6}
$$

$A|_M$ 若作用于非零有限维空间，由原 $A$ 单射而单射；
另一方面
$$
\|(A|_M)^n\|\le\|A^n\|
$$
使它拟幂零。
非零有限维上的拟幂零算子是幂零算子，不能单射。
矛盾。
因此 $M=0$。

由 (2.4) 的完整 $C$ 自伴性，
$\overline{\operatorname{Ran}T}=H$；
再由 (2.5)–(2.6)，(1.4) 非零且循环。
定理 1 得证。

## 9. 全行高阶偏离的直接推论

若 $a\ne0$、$c\in\ell^1$，且
$$
c_j=0\iff a_j=0,
\tag{9.1}
$$
则 $j_c=j_a$，直接满足定理 1。
实际上只须首个非零主系数的位置已带非零偏离，
并且此前偏离任意；后续零位和大小均不受限制。

特别，固定实数 $\kappa>2$。
若对全部非零主系数有
$$
0<|c_j|\le C|a_j|^\kappa,
\tag{9.2}
$$
并在主零位令 $c_j=0$，
则 $\ell^2\subset\ell^\kappa$ 保证 $c\in\ell^1$，
且 (9.1) 成立。
所以 (1.4) 循环。
无需 (9.2) 的统一正下界，
也无需任何重排尾率。
当 $\kappa$ 为整数时包括
$$
c_j=\gamma a_j^\kappa,\qquad\gamma\ne0.
\tag{9.3}
$$
对于非整数实 $\kappa$，(9.2) 仅比较绝对值；
本稿不定义多值复幂 $a_j^\kappa$。

例如
$$
a_j=(-1)^j(j+1)^{-\sigma},\qquad
\frac12<\sigma<1,\qquad
c_j=\beta |a_j|^\kappa\omega_j,
\tag{9.4}
$$
其中 $\beta\ne0$、$|\omega_j|=1$、$\kappa>2$。
主 first 属于 R138 的全平面连续谱分支，
辅助为全支撑慢幂。
尽管先前全空间共同圆周预算指数
$$
\frac{2\sigma(\kappa-1)}{\kappa\sigma-1}>2,
$$
(9.4) 现在由首支撑相同的有限 dyadic 机制排核。
这里不须缩小共同圆周，也没有将高次弱零提升重称为近单位。

同样，弱 $\ell^1$、可和慢幂、长平台以及任意物理排列的全行偏离，
只要满足 (1.3)，均不再需要原尾预算。
原尾预算和稀疏支撑准则在首偏离晚于首主系数时仍可能有独立范围。

## 10. 首偏离更晚时的精确缺口

若
$$
j_c>j_a,\qquad m_a=2^{j_a},
$$
则对 $\zeta^{m_a}\ne1$，
$D_\zeta$ 的精确首阶为 $m_a$，
而 $E_\zeta$ 的首阶至少为 $2m_a$。
此时仍可作真正解析因子消去，写成
$$
\gamma_\zeta T-T
=
2D_\zeta(X+K_\zeta),\qquad
K_\zeta(0)=0.
\tag{10.1}
$$
但在未知 $M$ 上，$X_M+(K_\zeta)_M$ 只知有界拟幂零，
没有非零常数项使它成为单位。
全空间单射或稠密像不保证它在 $M$ 上像稠密。

R270C 的末节明确没有证明非快分式分支在任意未知限制上的稠密性。
R270D §7 也明确只证明全空间循环性的双向等价，
并未证明一般正则化算子 $Q$ 在每个未知限制上稠密，
也未证明任意向量的两个闭循环空间相等。
因此不能用这些旧结论补出 (10.1) 所缺的限制稠密性。

例如主首位 $a_0\ne0$、偏离 $c_0=0$ 而 $c_1\ne0$，
即使后续 $|c_j|\asymp |a_j|^\kappa$，
也不由本稿定理直接闭合。
若另有弱 $\ell^1$／实际预解预算、
首位以外的稀疏偏离支撑预算，
或固定盘核内逆条件，则仍可调用相应独立定理；
本稿不把这些已有结论推成所有首位遗漏的统一结论。

本稿完成的是 (1.3) 所定义的二次偏离类。
它没有证明所有非零向量循环，
也没有达到本课题 README 对整个 Hilbert ISP 的完成标准。

## 11. 证据链

- [R176](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)：
  自然首一多项式闭性、完整 $C$ 自伴域、循环图核心、
  核内一阶有界限制、dyadic 全自然域恒等式与复 $\ell^2$ 指数权。
- [R151](../results/R151-quartic-analytic-approximation-gauge-stability.md) §3.1：
  每个非零 $\mathcal G$ 元素在任意闭 $A$ 不变限制上的实际稠密像；
  本稿只需其中的真解析特例。
- [R270C](../results/R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md)
  §§1、7–8：有限 dyadic first 增量、自然深域、
  原 Haar 双线性配对及 Fourier／全本质支撑排核。
- [R270D](../results/R270-appendix-arbitrary-fast-leading-coefficients-maximal-closure-and-cyclicity.md)
  §7：全空间循环 iff 的准确量词及未知限制边界。
- [R138](../results/R138-first-chaos-complete-spectrum-classification.md)：
  (9.4) 的全平面连续谱分类；该分类只用来说明范围，
  不参与 §§2–8 的排核证明。
