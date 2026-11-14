# R180：无界一阶的独立形式类与任意平方可和点态多项式的有限 gauge 联合循环

日期：2026-11-12（UTC）。作者：literature。

状态：完整证明。新增的核心是：无界第一阶乘子的 gauge 形式原函数，不能与任何有限组有界加性慢模式形成非平凡常系数线性关系模 $K$。证明通过纯 $K$ 最大闭分式、共同域的闭差、字符 MASA 和真实 UHF 左乘障碍完成。随后把既有有限轨道消元合法搬到全部自然幂域，覆盖任意复杂 $\ell^2$ 第一阶点态多项式及指数权。有限联合循环没有被改写成一般单核结论。

## 1. 设置与主要结论

记
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
\mathcal G\subseteq\mathcal A,\qquad
K=\operatorname{Frac}\iota(\mathcal G)\subseteq L=\mathbb C((z)).
\tag{1.1}
$$
其中 $\iota:\mathcal A\to\mathbb C[[z]]$ 是 R32 的忠实形式嵌入，
$\mathcal G$ 是 R151 的快速解析逼近代数。
令
$$
\Gamma=\mu_{2^\infty},\qquad
\gamma_\zeta(T)=U_\zeta T U_\zeta^*,\qquad
\alpha_\zeta f(z)=f(\zeta z).
$$

取
$$
u=a_*+\sum_{j\ge0}a_j\chi_j,\qquad
a\in\ell^2\setminus\ell^1,
\tag{1.2}
$$
并令 $X=X_u$ 为 R125 的实际闭第一阶乘子。
本稿先处理这个真正无界分支；$\ell^1$ 分支在末尾与 R173 合并。

定义只用于跟踪 gauge 增量的形式级数
$$
\boxed{
\beta_a(z)=\sum_{j\ge0}a_j\bigl(v_j(z)-1\bigr),\qquad
v_j(z)=\frac{d_j-z^{2^j}}{d_j+z^{2^j}}.
}
\tag{1.3}
$$
每个固定系数只涉及有限多个 $j$。
没有把 $\beta_a(A)$ 当作有界或闭算子，也没有给无界 $X$ 默认建立 $\iota(X)$。
常数 $a_*$ 不影响任何 gauge 增量，所以未放入 (1.3)。

称 $S\in\mathcal A$ 为本稿的有界加性模式，若
$$
\gamma_\zeta S-S\in\mathcal G
\qquad(\zeta\in\Gamma).
\tag{1.4}
$$

**定理1.1（新独立类）。** 对每个满足 (1.4) 的 $S$，
$$
\boxed{\beta_a-\iota(S)\notin K.}
\tag{1.5}
$$
因此 $\beta_a$ 在 $L/K$ 中的类不属于任意有限组有界加性模式的类所张成的
$\mathbb C$ 线性空间。

更一般，令 $H\in\mathcal A$ 满足 (1.4)，
$$
Y=X+H,\qquad
\operatorname{Dom}Y=\operatorname{Dom}X,\qquad
\beta_Y=\beta_a+\iota(H).
\tag{1.6}
$$
若 $\sigma_1,\ldots,\sigma_r$ 是有界加性模式的形式级数，且其在 $L/K$ 中的类对 $\mathbb C$ 线性无关，
则
$$
\boxed{\beta_Y,\sigma_1,\ldots,\sigma_r
\text{ 在 }K\text{ 上代数无关}.}
\tag{1.7}
$$
特别，对任意有限组有界加性模式 $S_1,\ldots,S_d$，
$\beta_Y$ 超越于 $K(\iota(S_1),\ldots,\iota(S_d))$。

**定理1.2（闭 monic 多项式的轨道分离）。**
取有限组有界加性模式 $S_1,\ldots,S_d$，并设
$$
T=P(Y,S_1,\ldots,S_d),\qquad
P(t,s)\in\mathcal G[s_1,\ldots,s_d][t]
\tag{1.8}
$$
关于 $t$ 为正次数 $p$ 的首一多项式。
实际自然域为 $\operatorname{Dom}X^p$。
令有界模式的类秩为
$$
r=\dim_{\mathbb C}\operatorname{span}_{\mathbb C}
\{[\iota(S_i)]\}\subseteq L/K.
\tag{1.9}
$$
则：

1. 若 $r=0$，$T$ 单射且值域稠密。
2. 若 $r=1$，存在有限 dyadic 子群 $H_0$，使对所有 $\zeta\notin H_0$，
$$
\boxed{
\ker T\cap\ker\gamma_\zeta T=0,\qquad
\overline{\operatorname{Ran}T+\operatorname{Ran}\gamma_\zeta T}=H.
}
\tag{1.10}
$$
3. 若 $r\ge1$，可选含 $1$ 的至多 $r+1$ 个 gauge，使相应闭算子的共同核为零、总值域稠密。选择可逐步避开有限坏集合；不声称整个参数笛卡尔积只有有限坏点。
4. 若 $\xi\in\operatorname{Dom}X^p$ 对 $A$ 循环，则相应的 $T\xi$ 及其所选 gauge 像联合循环。

**推论1.3（任意 $\ell^2$ 点态多项式）。**
设
$$
u=a_*+\sum_ja_j\chi_j,\qquad
w=c_*+\sum_jb_j\chi_j,\qquad a,b\in\ell^2,
$$
并取次数 $p\ge1$ 的非零标量多项式 $q$。
只要 $q(u)e^w\ne0$，该向量与至多 $p-1$ 个附加 gauge 像联合循环。
当 $p=2$ 时，存在有限 dyadic 子群 $H_0$，使
$$
\boxed{
q(u)e^w\text{ 与 }U_\zeta(q(u)e^w)
\text{ 联合循环}\quad(\zeta\notin H_0).
}
\tag{1.11}
$$
$p=1$ 时向量单独循环。
若 $a\notin\ell^1$，非零 $q$ 的向量 $q(u)e^w$ 自动非零，见 §12。

下面证明共同域、闭差标量化、形式独立性、实际消元与所有域传递。

## 2. 使用的真实闭算子输入

本稿使用以下已证明的准确结论。

### 2.1. 第一阶闭实现与正则器

R125、R128 给
$$
X^*=CXC,\qquad
(Cf)(y)=\overline{f(-1-y)}.
\tag{2.1}
$$
有限柱空间 $\mathcal D_c$ 是 $X$ 和 $X^*$ 的图核心。
每个 $B\in\{A\}'$ 保持 $\operatorname{Dom}X$ 并与 $X$ 域交换。

存在有界单射、稠密像的正则器 $R(t)\in\{A\}'$，满足
$$
R(t)\to I\text{ 强},\qquad
R(t)H\subseteq\operatorname{Dom}X,\qquad
XR(t)\in B(H).
\tag{2.2}
$$
对 $x\in\operatorname{Dom}X$，
$$
R(t)x\to x,\qquad
XR(t)x=R(t)Xx\to Xx.
\tag{2.3}
$$

### 2.2. 纯 $K$ 最大闭分式

若 $a,b\in\mathcal G$、$b\ne0$，则 R153 给
$$
T_{a/b}:\quad
\operatorname{Dom}T_{a/b}
=\{x:ax\in\operatorname{Ran}b\},\qquad
bT_{a/b}x=ax.
\tag{2.4}
$$
它闭、稠密定义、$C$ 自伴，域包含 $bH$，且
$$
T_{a/b}(bh)=ah.
\tag{2.5}
$$
同一分式的不同有限清分母表达得到同一最大图。

闭分式演算保和、积的闭包。
特别，若 $d\in\mathcal G$，则
$$
T_{r+d}=T_r+d
\tag{2.6}
$$
是同域算子等式：
右边本来已是闭算子的有界扰动，故无需再扩大其闭包域。

所有实际分母都单射。
这里没有把一般 $K$ 元素视作有界算子。

### 2.3. 无非零 UHF 左正则子

R171 的 $p=1$ 特例说：若 $0\ne b\in\mathfrak U$，
其中 $\mathfrak U$ 是实际 UHF 代数，则
$$
bX\text{ 在 }\mathcal D_c\text{ 上不能有界}.
\tag{2.7}
$$
$\mathcal A\subseteq\mathfrak U$，所以此结论特别适用于非零 $b\in\mathcal G$。

R171 更一般给：若最高系数是任意非零 UHF 元素，
其余系数有界，则正次数的
$\sum E_kX^k$ 在有限柱上无界。
本稿在证明 (1.5) 时只需要 (2.7)。

### 2.4. 自然多项式的域

R176 给：对 $Y=X+H$，$H\in\mathcal A$ 有界，
$$
\operatorname{Dom}Y^p=\operatorname{Dom}X^p.
\tag{2.8}
$$
最高系数为有界交换单位的自然多项式在此域上闭、$C$ 自伴。
每个有界交换子保持全部自然幂域。

如果 $T$ 是这种多项式，则
$$
M=\ker T
$$
是闭 $A$ 不变空间，并且
$$
\boxed{
M\subseteq\bigcap_{k\ge1}\operatorname{Dom}Y^k,\qquad
Y(M)\subseteq M,\qquad Y|_M\in B(M).
}
\tag{2.9}
$$
这不是由一阶域稠密性推出的。
它来自 R176 的最大正则化图及闭图定理。

如果 $\xi$ 循环且属于 $T$ 的自然域，R176 还给
$$
\mathbb C[A]\xi\text{ 是 }T\text{ 的图核心},\qquad
[T\xi]_A=\overline{\operatorname{Ran}T}.
\tag{2.10}
$$

## 3. 形式原函数与实际 gauge 增量

由于
$$
v_j(z)-1=-\frac{2z^{2^j}}{d_j+z^{2^j}}
$$
的形式阶为 $2^j$，(1.3) 的每个系数都是有限和。
因此 $\beta_a\in z\mathbb C[[z]]$ 是合法形式级数，无需 $\sum_j a_j$ 收敛。

固定 $\zeta\in\mu_{2^m}$ 后，所有 $j\ge m$ 满足
$$
v_j(\zeta z)=v_j(z).
$$
所以
$$
\alpha_\zeta\beta_a-\beta_a
=\sum_{j<m}a_j(v_j(\zeta z)-v_j(z)).
\tag{3.1}
$$
右侧是真正收敛解析芽，其实际求值恰为 R125 的有限 gauge 差：
$$
\boxed{
U_\zeta XU_\zeta^*=X+D_\zeta,\qquad
D_\zeta\in\mathcal G,\qquad
\iota(D_\zeta)=\alpha_\zeta\beta_a-\beta_a.
}
\tag{3.2}
$$
这是同域闭算子等式。

若 $Y=X+H$ 如 (1.6)，则
$$
U_\zeta YU_\zeta^*=Y+D_\zeta^Y,\qquad
D_\zeta^Y=D_\zeta+\gamma_\zeta H-H\in\mathcal G,
\tag{3.3}
$$
且
$$
\iota(D_\zeta^Y)=\alpha_\zeta\beta_Y-\beta_Y.
$$

(3.1)—(3.3) 只建立增量的一致性。
后续实际多项式都将在共同自然幂域上有限求值；
不会用 $\beta_a(A)$ 代替 $X$。

## 4. 闭 gauge 不变且与 $A$ 域交换的算子必为标量

本节给 (1.5) 所需的完整闭图引理。

**引理4.1。**
设 $J$ 是 $H$ 上闭、稠密定义的单值算子，并满足：

- 对每个 $\zeta\in\Gamma$，
$$
U_\zeta\operatorname{Dom}J=\operatorname{Dom}J,\qquad
JU_\zeta x=U_\zeta Jx;
\tag{4.1}
$$
- $A\operatorname{Dom}J\subseteq\operatorname{Dom}J$，且
$$
JAx=AJx\qquad(x\in\operatorname{Dom}J).
\tag{4.2}
$$

则存在 $c\in\mathbb C$，使
$$
\boxed{J=cI,\qquad \operatorname{Dom}J=H.}
\tag{4.3}
$$

### 4.1. 闭图投影属于字符 MASA 的矩阵代数

令 $\mathcal L=\operatorname{Graph}J\subset H\oplus H$，
$Q$ 为到 $\mathcal L$ 的正交投影。
(4.1) 及其逆说明 $\mathcal L$ 被全部
$U_\zeta\oplus U_\zeta$ 约化。
所以 $Q$ 与这些对角酉算子交换。

Dyadic 字符张成全部有限柱函数；
它们生成的 von Neumann 代数是全部乘法代数
$$
\mathcal M=L^\infty(\mathbb Z_2,\mu).
$$
该表示是 MASA。
例如，一个与全部乘法投影交换的有界算子 $B$，
令 $h=B1$，便有 $B\mathbf1_E=\mathbf1_Eh$。
由 $\|\mathbf1_Eh\|_2\le\|B\|\mu(E)^{1/2}$ 对全部可测 $E$ 成立，
得到 $h\in L^\infty$、$\|h\|_\infty\le\|B\|$。
再以简单函数稠密性得 $B=M_h$。
因此把 $Q$ 写成 $2\times2$ 算子矩阵后，
每个矩阵元都是某个 $L^\infty$ 函数的乘法。

所以存在可测投影矩阵 $q(y)\in M_2(\mathbb C)$，
使 $Q$ 是逐点乘以 $q(y)$。

### 4.2. 单值性与稠密域排除竖直纤维

在正测集合上若 $q(y)$ 的秩为2，
则该集合上的任意竖直向量 $(0,h)$ 都属于 $\mathcal L$，
与 $J$ 单值矛盾。
同样，不能在正测集合上出现一维竖直纤维。

若某个正测集合上的纤维为零，
则 $\operatorname{Dom}J$ 的所有向量都在该集合上为零，
与定义域稠密矛盾。

更具体地，投影矩阵的左上元 $q_{11}$ 非负；
若 $q_{11}=0$，投影正性给 $q_{12}=q_{21}=0$。
其纤维只能为零或竖直，均已排除。
所以几乎处处
$$
\operatorname{rank}q(y)=1,\qquad q_{11}(y)>0.
$$

定义有限的可测函数
$$
m(y)=q_{21}(y)/q_{11}(y).
$$
纤维像恰为 $\mathbb C(1,m(y))$。
又 $\mathcal L=\operatorname{Ran}Q$，所以
$$
\boxed{
J=M_m,\qquad
\operatorname{Dom}J=\{f\in L^2:mf\in L^2\}.
}
\tag{4.4}
$$
这是最大可测乘法域：
任意两个坐标均在 $L^2$ 的 $(f,mf)$ 逐点被 $q(y)$ 固定，
因而确实属于 $\operatorname{Ran}Q$。

### 4.3. 实际权与 odometer 遍历性迫使乘法为常数

写实际算子
$$
(Af)(y)=\omega(y)f(y-1),
$$
其中 $\omega(y)\ne0$ 几乎处处。
由 (4.2)、(4.4)，对全部 $f\in\operatorname{Dom}M_m$，
$$
m(y)\omega(y)f(y-1)
=\omega(y)m(y-1)f(y-1)
\quad\text{几乎处处}.
\tag{4.5}
$$

取
$$
f_N=\mathbf1_{\{|m|\le N\}}\in\operatorname{Dom}M_m.
$$
因为 $m$ 有限几乎处处，
这些集合移位后的并为全测。
在 (4.5) 中取消非零权，再对 $N$ 取可数并，得到
$$
m(y)=m(y-1)\quad\text{几乎处处}.
$$

Haar odometer 遍历。
也可把 $m$ 换成有界单射变换
$m/(1+|m|)$：
其 Fourier 系数在非平凡字符上因平移不变而为零，
所以该变换为常数，$m$ 本身也为常数。
于是 (4.3) 成立，证明引理。

此引理不需要 $J$ 正规或 $C$ 自伴；
需要的是闭、稠密、单值，以及 (4.1)—(4.2) 的完整域等式。

## 5. 证明无界第一阶的新独立类

假设与 (1.5) 相反：
存在有界加性模式 $S$，使
$$
\beta_a-\sigma_S=a_0/b_0\in K,\qquad
a_0,b_0\in\mathcal G,\quad b_0\ne0.
\tag{5.1}
$$
这里以 $a_0,b_0$ 表示分式分子分母，与第一阶系数序列 $a_j$ 无关。

令 $T=T_{a_0/b_0}$ 为 (2.4) 的最大闭分式。

### 5.1. 闭分式的 gauge 共轭确实同域

由 (3.1)、(5.1) 及形式忠实性，
$$
\alpha_\zeta(a_0/b_0)-a_0/b_0
=\iota(D_\zeta-\gamma_\zeta S+S)\in\iota(\mathcal G).
\tag{5.2}
$$
直接共轭最大图 (2.4) 得到
$$
U_\zeta T_rU_\zeta^*=T_{\alpha_\zeta r}.
$$
再用 (2.6)，
$$
\boxed{
U_\zeta TU_\zeta^*
=T+D_\zeta-\gamma_\zeta S+S
}
\tag{5.3}
$$
为同域闭算子等式。

这里使用的是“分式加一个有界元素”的闭场规则。
没有仅从两个无界算子的差之闭包有界，就反推它们原域相等。

### 5.2. 共同稠密域上的差可闭

置
$$
\mathcal D=\operatorname{Dom}X\cap\operatorname{Dom}T,\qquad
J_0=X-S-T\quad\text{在 }\mathcal D\text{ 上}.
\tag{5.4}
$$
对任意固定 $t>0$，
$$
b_0R(t)H\subseteq\mathcal D.
\tag{5.5}
$$
理由是 $b_0$ 保持 $\operatorname{Dom}X$，
而 $\operatorname{Ran}b_0\subseteq\operatorname{Dom}T$。
$b_0$ 与 $R(t)$ 都有稠密像，故其有界乘积也有稠密像。
因此 $\mathcal D$ 稠密。

$X,S,T$ 都对
$$
B(f,g)=\langle f,Cg\rangle
$$
对称，所以 $J_0$ 在 $\mathcal D$ 上 $C$ 对称。
这足以保证可闭：
$C\mathcal D\subseteq\operatorname{Dom}J_0^*$ 是稠密集。

令
$$
J=\overline{J_0}.
\tag{5.6}
$$
由 (3.2)、(5.3)，$\mathcal D$ 被全部 $U_\zeta$ 双向保持，
且 $J_0U_\zeta=U_\zeta J_0$。
对图收敛序列施加有界酉算子，便得
$$
U_\zeta\operatorname{Dom}J=\operatorname{Dom}J,\qquad
JU_\zeta=U_\zeta J.
\tag{5.7}
$$

$X$、$T$ 都与 $A$ 域交换，$S$ 与 $A$ 交换，
所以 $\mathcal D$ 被 $A$ 保持，$J_0A=AJ_0$。
同样对图收敛序列施加 $A\oplus A$，
得到 $A\operatorname{Dom}J\subseteq\operatorname{Dom}J$、$JA=AJ$。

引理4.1 遂给
$$
J=cI
$$
对某个 $c\in\mathbb C$ 成立。
尤其在原共同域上
$$
Xx-Sx-Tx=cx.
\tag{5.8}
$$

### 5.3. 在真实图核心上清分母导致矛盾

将 $x=b_0R(t)h$ 代入 (5.8)。
域交换与 (2.5) 给
$$
b_0XR(t)h
=(a_0+b_0S+cb_0)R(t)h.
\tag{5.9}
$$
对任意 $f\in\operatorname{Dom}X$，取 $h=f$ 并让 $t\downarrow0$，
用 (2.3) 得
$$
\boxed{
b_0Xf=(a_0+b_0S+cb_0)f
\qquad(f\in\operatorname{Dom}X).
}
\tag{5.10}
$$
右侧是全域有界算子。
而 $0\ne b_0\in\mathcal G\subseteq\mathfrak U$，
(5.10) 在全部有限柱上与 R171 的 (2.7) 矛盾。

因此 (5.1) 不可能，定理1.1 得证。

整个矛盾只使用纯 $K$ 的闭分式；
没有预先构造多个慢变量的闭分式场。

## 6. 联合形式代数独立与半线性环

### 6.1. 无界方向独立于任何有限组有界方向

若对常数 $c,c_i$ 有
$$
c\beta_a+\sum_i c_i\sigma_i\in K,\qquad c\ne0,
$$
则令 $S=-\sum_i(c_i/c)S_i$，
就有 $\beta_a-\iota(S)\in K$，违背定理1.1。

加上任意有界加性 $H$ 不改变这个结论：
若 $\beta_Y-\iota(S)\in K$，
则 $\beta_a-\iota(S-H)\in K$。
所以 $\beta_Y$ 的类也独立于全部有限有界加性类。

从有界模式中选 $r$ 个独立类。
于是
$$
[\beta_Y],[\sigma_1],\ldots,[\sigma_r]
$$
对 $\mathbb C$ 线性无关。

### 6.2. R166 的纯形式引理在此完全适用

R166 的代数独立证明只用以下纯场事实：

- 所有形式元素属于 $L=\mathbb C((z))$；
- 所有增量属于 $K$；
- $L^\Gamma=\mathbb C$；
- 所考虑的类在 $L/K$ 中常系数线性无关。

它没有使用这些形式元素本身来自有界算子。
本稿的 $\beta_Y$ 满足全部条件。
因此 (1.7) 成立。

为明确逻辑，关系理想中取 graded 单项式序最小首项的首一多项式；
半线性作用与它相减使首项消失，因此它必须精确固定。
最高齐次层系数遂为常数。
次高层产生
$$
c+\lambda_0\beta_Y+\sum_i\lambda_i\sigma_i\in\mathbb C,
\qquad c\in K,\quad(\lambda_0,\ldots,\lambda_r)\ne0,
$$
与类独立矛盾。
同一论证还给多项式环没有非零真稳定理想。

具体地，令
$$
\mathscr R=K[t,s_1,\ldots,s_r],\qquad
h_{\zeta,0}=\iota(D_\zeta^Y),\qquad
h_{\zeta,i}=\alpha_\zeta\sigma_i-\sigma_i.
$$
则
$$
\boxed{
\Lambda_\zeta P
=(\alpha_\zeta P)
(t+h_{\zeta,0},s_1+h_{\zeta,1},\ldots,s_r+h_{\zeta,r})
}
\tag{6.1}
$$
是群作用，$\mathscr R$ 为 $\Gamma$ 单环：
$$
\mathscr I\ne0,\quad \Lambda_\zeta\mathscr I=\mathscr I
\ \forall\zeta
\quad\Longrightarrow\quad\mathscr I=\mathscr R.
\tag{6.2}
$$

每个常系数依赖的有界方向可用 R166 的有限 $K$ 仿射归约消去。
所以 $\beta_Y$ 超越于全部 $K(\sigma_1,\ldots,\sigma_d)$，
也特别不属于该有理函数域。

### 6.3. 不把形式原函数误作无限算子求值

以下所有实际求值仅在
$$
\mathcal E_\infty=\bigcap_{k\ge1}\operatorname{Dom}Y^k
$$
上进行有限多项式运算。
该空间包含有限柱，稠密；
被 $Y$ 和全部有界交换子保持。

对 $E\in\mathcal A$ 与 $f\in\mathcal E_\infty$，
$EY^kf=Y^kEf$。
所以有限多项式恒等式可在 $\mathcal E_\infty$ 上逐项求值。
不会求值一个一般形式 Laurent 级数，也不会把 $K$ 分母直接当作有界逆。

## 7. 原自然多项式及其所有 gauge 核的完整幂域

对 (1.8) 的 monic $T$，R176 给
$$
\operatorname{Dom}T=\operatorname{Dom}X^p,\qquad
T^*=CTC.
\tag{7.1}
$$
对于每个 $\zeta$，(3.3) 和有界交换扰动的二项式域公式给
$$
U_\zeta\operatorname{Dom}X^p=\operatorname{Dom}X^p.
\tag{7.2}
$$
因此
$$
T_\zeta:=U_\zeta TU_\zeta^*
$$
也是 $Y$ 的首一自然多项式，系数仍在有界交换代数中，
准确域仍为 $\operatorname{Dom}X^p$。

置
$$
M_\zeta=\ker T_\zeta.
$$
R176 §8 给
$$
\boxed{
M_\zeta\subseteq\mathcal E_\infty,\qquad
Y(M_\zeta)\subseteq M_\zeta,\qquad
Y|_{M_\zeta}\in B(M_\zeta).
}
\tag{7.3}
$$
每个有界交换子也保持 $M_\zeta$。
这些结论对任何有限交 $\bigcap_{\zeta\in Z}M_\zeta$ 同样成立。

这保证后面的消元乘子即使含高于 $p$ 的 $Y$ 次幂，
在所有被测试的核向量上仍真正有定义。
没有仅在 $\operatorname{Dom}X^p$ 上非法相乘高次多项式。

此外，有限多项式 $F(Y,S)$ 在 $\mathcal E_\infty$ 上对 $B$ 对称：
每次把一个 $Y$ 或有界系数移过 $B$，两端仍有足够幂域。
因此对 $f,g\in\mathcal E_\infty$，
$$
B(F(Y,S)f,g)=B(f,F(Y,S)g).
\tag{7.4}
$$
本稿不要求这些辅助高次多项式预先选有某个最大闭实现。

## 8. 有界依赖方向的真实清分母

为避免把 $K$ 系数直接求值，说明任意有限有界模式的归约。

以常数线性变换选出 $S_1,\ldots,S_r$ 的独立类。
其余模式满足
$$
\sigma_j=\sum_{i\le r}c_{ji}\sigma_i+k_j,\qquad k_j\in K.
\tag{8.1}
$$
对每个关系取有限非零 $\mathcal G$ 分母。
形式忠实性将清分母后的 (8.1) 变成实际有界恒等式。

对有限多项式 $P$ 代入这些关系，再统一清有限个分母，
得到
$$
g\in\mathcal G\setminus\{0\},\qquad
\widetilde P\in\mathcal G[t,s_1,\ldots,s_r],
$$
使在 $\mathcal E_\infty$ 上
$$
\boxed{
gT=\widetilde P(Y,S_1,\ldots,S_r).
}
\tag{8.2}
$$
因为原 $P$ 关于 $t$ 首一，$\widetilde P$ 的最高 $t$ 系数为 $g$，
故 $\widetilde P$ 在 $K[t,s]$ 中非零。

对 gauge 共轭，有同样准确的有限恒等式
$$
\boxed{
(\gamma_\zeta g)T_\zeta
=(\Lambda_\zeta\widetilde P)(Y,S_1,\ldots,S_r)
\quad\text{在 }\mathcal E_\infty.
}
\tag{8.3}
$$
其依据是 (3.3)、有界模式的实际增量式和全部自然幂域的 gauge 保持。

原核 $M_\zeta$ 仍由原 monic 闭算子定义。
清分母没有把 $\widetilde P(Y,S)$ 自动当成同域闭算子；
$\gamma_\zeta g$ 的单射性只保证其在原域上的零集仍是 $M_\zeta$。
所有幂域和核的闭性都保留自原 $T_\zeta$。

## 9. 秩零：一个无界方向的快系数多项式单独排核

假设 $r=0$。
(8.2) 给非零 $\widetilde P\in\mathcal G[t]$。
$\beta_Y$ 超越于 $K$，所以一变量环 $K[t]$ 的作用
$$
\Lambda_\zeta Q=(\alpha_\zeta Q)(t+h_{\zeta,0})
$$
没有非零真稳定理想。

将 $\widetilde P$ 在 $K[t]$ 中分解成有限个首一不可约因子。
每个因子的全群稳定子不可能是 $\Gamma$：
否则其真主理想违反稳定理想结论。
Prüfer 群的真子群有限。
两个给定因子发生轨道相遇的参数若非空，则是某个有限稳定子的陪集。

所以存在有限 dyadic 子群 $H_0$，使
$$
\gcd_{K[t]}(\widetilde P,\Lambda_\zeta\widetilde P)=1
\qquad(\zeta\notin H_0).
$$
Euclidean 算法再清有限个 $\mathcal G$ 分母，给
$$
\boxed{
D=U\widetilde P+V\Lambda_\zeta\widetilde P,\qquad
0\ne D\in\mathcal G,\quad U,V\in\mathcal G[t].
}
\tag{9.1}
$$

令 $M=\ker T$、$M_\zeta=U_\zeta M$。
对 $f\in M$、$k\in M_\zeta$，
(7.3) 给两者属于 $\mathcal E_\infty$。
在 (9.1) 中实际求值：
第一项因 $\widetilde P(Y)f=gTf=0$ 消失。
第二项利用 (7.4) 移到 $k$；
它等于
$$
B(f,(\Lambda_\zeta\widetilde P)(Y)V(Y)k).
$$
$V(Y)$ 保持 $M_\zeta$，而 (8.3) 在该空间上为零。
所以
$$
B(Df,k)=0.
\tag{9.2}
$$

R151 保证 $\overline{DM}=M$，于是
$$
B(M,U_\zeta M)=0\qquad(\zeta\notin H_0).
\tag{9.3}
$$

为明确最后一步，任意 $f,k\in M$ 的 $L^1$ 乘积
$f(y)k(-1-y)$ 的 Fourier 系数只可能位于有限子群 $H_0$，
故该乘积是有限头柱函数。
若 $M\ne0$，其总本质支撑由实际权非零几乎处处及 odometer 遍历性为全测。
在每个有限头柱内选一对乘积非零的 $f_0,k_0$；
它在该柱为非零常数。
所有 $f\in M$ 的 $f(y)k_0(-1-y)$ 也为该柱常数，
所以该柱上 $M$ 的限制维数至多一。
有限柱数迫使 $M$ 有限维。
实际 $A$ 单射拟幂零，没有非零有限维不变空间，故 $M=0$。

$T$ 的完整 $C$ 自伴性再给伴随核为零，值域稠密。
这证明定理1.2 的秩零分支。

本节包括所有首一 $\mathcal G$ 系数的 $Y$ 多项式。
它没有把一般 Bell 系数预先列入 $\mathcal G$。

## 10. 一个有界独立方向：泛型两轨道分离

现在 $r=1$。
写独立有界模式为 $S$、形式为 $\sigma$。
$\beta_Y,\sigma$ 在 $K$ 上代数无关，且
$K[t,s]$ 的半线性作用为 $\Gamma$ 单环。

对 $\widetilde P$ 在 $K[t,s]$ 的有限不可约分解，
与 §9 相同的稳定子及陪集论证给有限 dyadic 子群 $H_0$，使
$$
\gcd_{K[t,s]}(\widetilde P,\Lambda_\zeta\widetilde P)=1
\qquad(\zeta\notin H_0).
\tag{10.1}
$$
多变量因子可以按固定 graded 序把首系数归一为1；
主理想稳定时单位倍数因此恰为1，故稳定子论证仍准确。

在 $K(s)[t]$ 中对两个多项式作 Euclidean 算法。
由 Gauss 引理，(10.1) 保证其 gcd 为1；
只依赖 $s$ 的非零因子在这个局部化环中本来就是单位。
清掉有限个 $s$ 多项式分母后，得到
$$
0\ne R(s)=U(t,s)\widetilde P
+V(t,s)\Lambda_\zeta\widetilde P,
\qquad U,V\in K[t,s].
$$
再清全部有限 $\mathcal G$ 分母，可以取
$$
\boxed{
R\in\mathcal G[s]\setminus\{0\},\quad
U,V\in\mathcal G[t,s].
}
\tag{10.2}
$$
这里没有得到单位理想；所得是非零单变量消元多项式。

因为 $\sigma$ 超越于 $K$，
$$
R(\sigma)\ne0.
$$
实际有界 $R(S)$ 的形式级数就是该值，
故 $R(S)\ne0$；R152 给 $R(S)$ 单射且值域稠密。

若 $f\in M\cap M_\zeta$，则 $f\in\mathcal E_\infty$。
(10.2) 可合法求值，并由 (8.2)—(8.3) 给
$$
R(S)f=0.
$$
单射性迫使 $f=0$。
所以
$$
M\cap M_\zeta=0.
$$
又 $T,T_\zeta$ 都完整 $C$ 自伴，因而
$$
\left(\operatorname{Ran}T+\operatorname{Ran}T_\zeta\right)^\perp
=\ker T^*\cap\ker T_\zeta^*
=C(M\cap M_\zeta)=0.
$$
这证明 (1.10)。

$R(S)$ 只在全 $H$ 上使用。
没有把其全空间密度换成未知核或不变子商上的密度，
也没有把 $M$ 与 $M_\zeta$ 先合并成同一个核。

## 11. 多个有界方向：至多 $r+1$ 个轨道

设 $r\ge1$。
总形式方向是
$$
\beta_Y,\sigma_1,\ldots,\sigma_r,
$$
共有 $r+1$ 个独立类。
R173 的 §§2–6 是纯有限 Laurent 系数和多项式环论证，
可逐条用于这些方向。

### 11.1. 固定系数的有限例外仍成立

每个形式元素都在 $\mathbb C[[z]]$；
其 gauge 增量常数项为零。
每个 $K$ 系数的 Laurent 阶有固定有限下界。
对一个固定有限次数多项式及一个固定 $z$ 次数，
半线性轨道系数只包含有限卷积，
从而是关于 $\zeta$ 的有限 Laurent 多项式。

所以在有限维次数空间中，
如果某个 $K$ 线性子空间不包含整个轨道，
只有有限多个 $\zeta$ 的轨道成员落入它。
这个论证没有用 $\beta_Y$ 的有界算子求值。

### 11.2. 从原多项式起步的降维计数

令
$$
I_Z=(\Lambda_\zeta\widetilde P:\zeta\in Z)
\subseteq K[t,s_1,\ldots,s_r].
$$
从 $Z=\{1\}$ 起步。
每次选择下一个轨道多项式，避开当前有限多个最小素理想；
有限例外引理及稳定理想为全环保证可以做到。

每加入一个这样的成员，若尚未成为单位理想，
商的最大不可约分支超越次数至少下降1。
原环有 $r+1$ 个变量；
第一个非零多项式已使该数至多 $r$。
因此可在
$$
|Z|\le r+1,\qquad 1\in Z
\tag{11.1}
$$
时，使 $I_Z$ 成为单位理想或其商为零维。

R173 已证明这里不需要 $K$ 代数闭：
零维有限型 $K$ 代数的各最小素商是有限代数域扩张，
有限生成的 nilradical 幂零，
相应有限模滤过给整个商有限维。

### 11.3. 向一个有界方向消元

若已经是单位理想，直接得到非零常数消元式。
否则在有限维商中，乘以 $s_1$ 的线性映射有非零特征多项式，
故存在
$$
0\ne R(s_1)\in I_Z\cap K[s_1].
$$
把其理想表达以及 $R$ 的有限系数统一清 $\mathcal G$ 分母，得
$$
\boxed{
R(S_1)=
\sum_{\zeta\in Z}
U_\zeta(Y,S_1,\ldots,S_r)
(\gamma_\zeta g)T_\zeta
}
\tag{11.2}
$$
在 $\mathcal E_\infty$ 上成立，
其中 $R\in\mathcal G[s_1]\setminus\{0\}$、
$U_\zeta\in\mathcal G[t,s]$。

$\sigma_1$ 超越于 $K$，所以 $R(S_1)$ 是非零实际有界算子，
R152 保证其单射。
对
$$
f\in\bigcap_{\zeta\in Z}\ker T_\zeta
$$
使用 (7.3)，(11.2) 的所有项都真正有定义并为零。
因此 $f=0$。

完整 $C$ 自伴性给总值域稠密，与 §10 相同。
这证明定理1.2 的数量界。

这里是逐步选择后各自有限的坏集合。
没有声称任意 $r+1$ 个不同 gauge 都满足结论。

## 12. 循环向量与任意 $\ell^2$ 点态多项式

### 12.1. 从闭算子范围到向量

令 $\xi\in\operatorname{Dom}X^p$ 对 $A$ 循环。
R176 的图核心结论给
$$
[T\xi]_A=\overline{\operatorname{Ran}T}.
$$
对任意 $\zeta$，
$U_\zeta\xi$ 仍循环，并由 (7.2) 属于 $T_\zeta$ 的域。
所以
$$
[U_\zeta T\xi]_A
=[T_\zeta U_\zeta\xi]_A
=\overline{\operatorname{Ran}T_\zeta}.
\tag{12.1}
$$
定理1.2 的总值域稠密因此准确变为有限向量族联合循环。

### 12.2. 任意复杂指数权的有界倾斜修正

取 $b\in\ell^2$、$w=c_*+\sum b_j\chi_j$，
记 $\xi=e^w$。
R147/R176 给 $\xi$ 循环。

定义真实倾斜位算子
$$
R_j(b)=
(I-e^{-2b_j}N_j)(I+e^{-2b_j}N_j)^{-1}.
\tag{12.2}
$$
固定 $b$ 后 $\sup_j\|R_j(b)\|<\infty$，
且
$$
R_j(b)-V_j=b_jL_j,\qquad
\sup_j\|L_j\|<\infty.
$$
因此
$$
H_{a,b}=\sum_j a_j(R_j(b)-V_j)\in\mathcal A
\tag{12.3}
$$
按范数绝对收敛。
固定 dyadic gauge 后，充分高位 $N_j$ 不变，
故 $\gamma_\zeta H_{a,b}-H_{a,b}$ 只剩有限个真正解析项，
属于 $\mathcal G$。

置
$$
Y=X+H_{a,b}.
\tag{12.4}
$$
它符合 (1.6)，并且 R176 §10 已严格证明
$$
\xi\in\bigcap_{k\ge1}\operatorname{Dom}Y^k
=\bigcap_{k\ge1}\operatorname{Dom}X^k.
\tag{12.5}
$$

### 12.3. 只有 $p-1$ 个有界累积量

定义有限标量多项式
$$
L_n(v)=
\left.\frac{d^n}{dt^n}
\log(\cosh t+v\sinh t)\right|_{t=0}.
$$
对 $2\le n\le p$，令
$$
K_n(b)=\sum_j a_j^n L_n(R_j(b)).
\tag{12.6}
$$
因为 $a\in\ell^2$、$R_j(b)$ 一致有界，
这些级数按算子范数绝对收敛，给 $\mathcal A$ 元素。
每个固定 gauge 的差仍只是有限低位真正解析项，
所以
$$
\gamma_\zeta K_n(b)-K_n(b)\in\mathcal G.
\tag{12.7}
$$

R176 的真实规范整乘积
$$
\mathcal B_b(t)=
\prod_j e^{-ta_jR_j(b)}
\bigl(\cosh(ta_j)I+R_j(b)\sinh(ta_j)\bigr)
$$
在零附近满足
$$
\log\mathcal B_b(t)
=\sum_{n\ge2}\frac{t^n}{n!}K_n(b).
\tag{12.8}
$$
每个固定 $p$ 阶只涉及有限个 $K_2,\ldots,K_p$。
其真实幂域恒等式给
$$
\boxed{
q(u)e^w=P_{q,b}\bigl(Y,K_2(b),\ldots,K_p(b)\bigr)\xi,
}
\tag{12.9}
$$
其中 $P_{q,b}$ 是有限常系数多项式，
关于 $Y$ 的次数为 $p$、最高系数为 $q_pI$。
除以非零 $q_p$ 即为 monic 情形。

因此有界模式的类秩满足
$$
r\le p-1.
$$
§§9–11 给至多 $r+1\le p$ 个 gauge 联合分离，
§12.1 给相应向量联合循环。

若 $a\notin\ell^1$，(12.9) 的自然算子在有限柱上不能为零：
展开为 $X$ 的多项式后，
最高系数仍为非零标量 $q_pI$，R171 适用。
若 $q(u)e^w=0$，则循环 $\xi$ 的图核心会迫使该自然算子为零，矛盾。
所以这个分支中非零 $q$ 自动给非零向量。

### 12.4. 二次式的明确两方向形式

当
$$
q(t)=q_2t^2+q_1t+q_0,\qquad q_2\ne0,
$$
只需一个有界模式
$$
S=K_2(b)=\sum_j a_j^2(I-R_j(b)^2).
$$
准确恒等式是
$$
\boxed{
q(u)e^w=
\bigl(q_2Y^2+q_1Y+q_0I+q_2S\bigr)e^w.
}
\tag{12.10}
$$
这里保留了同位 Bell 修正。
$S$ 不必属于 $\mathcal G$；只需要 (12.7)。

若 $[\iota(S)]=0$ 于 $L/K$，§9 给该向量单独循环。
若该类非零，§10 给除有限 gauge 外的两向量联合循环。
这证明 (1.11)，并覆盖全部复杂 $\ell^2$ 慢平方共振的联合循环结论。

它仍没有排除第二种情形下单个算子的核。

### 12.5. 与可和分支合并

若 $a\in\ell^1$，则 $u$ 有界。
R173 已用 $p$ 个有界对数累积量证明同样的至多 $p$ 个轨道结论；
$p=2$ 的有限例外两轨道版本由 R169 给出。
当实际向量为零时当然不能谈循环，所以统一陈述保留
$q(u)e^w\ne0$。

若 $a=0$ 或 $q$ 为非零常数，
实际非零向量只是 $e^w$ 的非零常数倍，本来单独循环。
因此推论1.3 对任意复杂 $\ell^2$ 第一阶完整成立。

## 13. 范围与没有被推出的结论

1. $\beta_a$ 是精确增量的形式原函数，不是未经证明的无界算子形式嵌入，也没有被直接求值于 $A$。
2. 定理1.1 用纯 $K$ 分式及实际 UHF 左乘障碍完成，未预设多个慢变量的最大闭分式场。
3. 类独立性没有被直接当作 Hilbert 空间单射性；排核或共同排核都另有实际闭域和消元证明。
4. 当有界模式类秩为零时，非零快分母在未知核上的稠密性确来自 R151。
5. 当类秩至少一时，消元算子只在全 $H$ 使用其 R152 单射性；没有外推未知限制上的稠密性。
6. (11.2) 的辅助多项式可能无界。它们只在已证明属于全部自然幂域的共同核上求值。
7. 至多 $p$ 个 gauge 联合循环不意味着每个成员单独循环。一般慢平方和高次单核缺口仍保留。
8. 本稿未覆盖任意有限 chaos 的一般点态多项式，也未给多变量未知闭核的全部格结构。
9. 完整 Hilbert 不变子空间问题仍未解决。

## 14. 依赖与新增内容

- [R125：全部 $\ell^2$ 第一阶的实际闭实现](../results/R125-all-l2-first-chaos-closed-multiplier-cyclicity.md)。
- [R128：不变限制与有界正则器](../results/R128-first-chaos-invariant-parts-and-resolvent-regularization.md)。
- [R151：快系数的强主理想单位](../results/R151-quartic-analytic-approximation-gauge-stability.md)。
- [R152：单个有界加性方向的非零多项式单射稠密](../results/R152-fast-gauge-increments-analytic-germs-and-closed-quotients.md)。
- [R153：纯 $K$ 的最大闭分式场](../results/R153-fast-fraction-field-on-all-invariant-subquotients.md)。
- [R166：独立类与半线性稳定理想](../results/R166-additive-modes-linear-classes-and-polynomial-relations.md)。
- [R169：双方向消元及可和二次式](../results/R169-finite-gauge-koszul-cores-and-two-slow-mode-separation.md)。
- [R171：UHF 最高系数的实际无界障碍](../results/R171-uhf-leading-polynomials-of-unbounded-first-multipliers.md)。
- [R173：纯形式降维与轨道数量界](../results/R173-rank-bounded-gauge-orbits-and-slow-polynomial-joint-cyclicity.md)。
- [R176：自然多项式最大图、全部核幂域与指数权图核心](../results/R176-natural-polynomial-maximal-graphs-and-bell-domains.md)。

本稿新增：闭 gauge 不变差的 MASA 标量化引理；
无界第一阶类独立于所有有限有界加性类；
monic 快系数自然多项式的秩零排核；
一个有界慢方向的泛型两轨道共同核零；
以及任意复杂 $\ell^2$ 第一阶点态多项式带任意 $\ell^2$ 指数权的次数控制联合循环。


## 15. 补充：全部 $\ell^2$ 二次核的高阶 gauge 角度退化

本节把 R178 的几何必要条件扩到本稿新覆盖的无界第一阶分支。
设 $q$ 的次数为2，$q(u)e^w\ne0$，并令
$$
T=q_2^{-1}P_{q,b}(Y),\qquad
M=\ker T.
\tag{15.1}
$$
这里乘以非零标量只为使 $T$ 关于 $Y$ 首一，不改变核。
若 $a\notin\ell^1$，$T$ 使用 R176 的准确自然闭域
$\operatorname{Dom}X^2$；
若 $a\in\ell^1$，它就是 R169 的实际有界 Bell 乘子。

假设尚未排除的 $M\ne0$。
由本稿 §10 或可和分支的 R169，
存在有限 dyadic 子群 $H_0$，使
$$
M\cap U_\zeta M=0\qquad(\zeta\notin H_0).
\tag{15.2}
$$
$M$ 是闭 $A$ 不变空间。
R178 的高阶 gauge 渐近交换适用于全部这类不变空间，
并不要求它来自有界算子的核。
所以对 $\zeta_n=e^{2\pi i/2^n}$，
$$
P_n:=P_{U_{\zeta_n}M}\to P_M\quad\text{强}.
\tag{15.3}
$$

对任何固定单位 $f\in M$，
充分大 $n$ 时两核交零，而
$$
\frac{\|f-P_nf\|}{\sqrt{1+\|P_nf\|^2}}\to0.
$$
因此加法映射
$$
\mathcal J_n:M\oplus U_{\zeta_n}M\to H,\qquad
\mathcal J_n(x,y)=x+y
$$
的最小模趋零，范数趋于 $\sqrt2$。
若和在某个无穷子序列上闭，
其有界规范投影 $E_n(x+y)=x$ 必满足
$$
\|E_n\|\ge\frac1{\|f-P_nf\|}\to\infty.
\tag{15.4}
$$
对非闭和，R178 的稠密闭无界规范幂等及其空预解集结论仍适用。

### 15.1 无界分支的有限核和闭包仍是 proper

不能在此直接说原无界 $T$ 属于 $\mathcal A$ 再用无零因子。
下面给实际有界正则化证明。

任取有限个 gauge $\zeta_1,\ldots,\zeta_m$，写
$$
T_i=U_{\zeta_i}TU_{\zeta_i}^*,\qquad M_i=\ker T_i.
$$
(3.3) 及自然幂域保持说明，
每个 $T_i$ 都是同一 $Y$ 的首一二次多项式，
其系数属于 $\mathcal A$；
它在 $\operatorname{Dom}Y^2$ 上闭。
固定基础第一阶的共同正则器 $R=R(t)$，置
$$
B_i=T_iR^2\in\{A\}'.
\tag{15.5}
$$

这些有界因子满足
$$
\boxed{\ker B_i=M_i.}
\tag{15.6}
$$
反向包含由 $B_i x=R^2T_i x$ 在自然域上立即得到。
正向若 $B_i x=0$，令 $x_s=R(s)^2x$。
则
$$
R^2T_i x_s=B_iR(s)^2x=0.
$$
$R^2$ 单射给 $T_i x_s=0$。
又 $x_s\to x$，$T_i$ 闭，所以 $x\in\ker T_i$。
这证明 (15.6)，没有预设 $x$ 一开始就在自然域中。

在 $\operatorname{Dom}Y^{2m}$ 上，各个有限多项式的逐次作用合法：
每个有界系数保持所有幂域，二次因子至多消耗两次幂。
令
$$
Q(Y)=\prod_{i=1}^mT_i(Y).
$$
它的有限多项式展开关于 $Y$ 首一，次数为 $2m$。
由实际有界正则化恒等式，
$$
\boxed{
\prod_{i=1}^mB_i=Q(Y)R^{2m}.
}
\tag{15.7}
$$
右侧是由 $YR$ 与 $R$ 构成的有界多项式。

若 (15.7) 为零，则对任意
$x\in\operatorname{Dom}Y^{2m}$，
$$
R^{2m}Q(Y)x=\left(\prod_iB_i\right)x=0.
$$
单射的 $R^{2m}$ 给 $Q(Y)x=0$。
特别这个等式在全部有限柱上成立。
把 $Y=X+H_{a,b}$ 展开，
最高 $X^{2m}$ 系数为 $I$，其余系数有界，
与 R171 矛盾。
因此
$$
\prod_iB_i\ne0.
\tag{15.8}
$$

全部 $B_i$ 在有界交换子代数中交换。
由 (15.6)，它们的乘积杀掉每个 $M_i$，
从而
$$
\boxed{
\overline{\sum_{i=1}^mM_i}
\subseteq\ker\!\left(\prod_iB_i\right)\ne H.
}
\tag{15.9}
$$
可和分支则直接由各非零 $T_i\in\mathcal A$ 的无零因子性质得到同一结论。

因此全部复杂 $\ell^2$ 二次加权未知核，
都满足高阶轨道的角度退化与有限核和真闭包约束。
这没有排除某个固定闭和，
也没有从规范投影范数发散推出 $M=0$。
