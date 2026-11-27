# R1103. 原 full47 的粗 CM 切向、有限域第三类首项与整二次 QC 判据

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126；global_route。

**状态：以下读取公式、有限域归一化和条件式排盘判据已证明，纯纸面；本篇没有新的数学执行。**
固定
$$
X=X_{\rm ns}^{+}(47),\quad g=73,\quad q=4513,\quad
\mathcal X/\mathbb Z_q\text{ 为原好模型}.
$$
本篇保持 R1090 的原95个 weight-one Reynolds 来源、全23个 cusp 留数以及真正73维 Hodge 核。
不使用另一个模曲线的整微分格。

R1074、R1086 将原有理点限制到八个已知有理 CM 点的同一坏47管域及同一好4513剩余盘。
本篇为这些原盘给出可直接继续计算的切向量和第三类微分首项，并证明一个仅需模4513的二次 QC 判据。
它不声称所需有限矩阵已经计算，也不从全局高度单位直接推出盘内唯一性。
对一般 trace-zero 角组合，非4513局部项的消失在第6节列为明确前提；不从 principal 对应的 degree-zero 性质移植。

## 1. 原整格、行作用和全部尺度

令
$$
\mathbb T=\mathbb T_q,\qquad
u_4=23y_4-C_\infty,\qquad
B=q+1-T_q,\qquad D_4=B u_4.
\tag{1103.1}
$$
R1093 已证明
$$
M=J(\mathbb Q)\otimes\mathbb Z_q=\mathbb T[D_4],
\qquad \log M=q\,\operatorname{Lie}J(\mathbb Z_q).
\tag{1103.2}
$$
这里也可用 $u_4$ 作生成元，因为 R1089 的 $B$ 是整单位；本文始终使用 (1103.1)，不删除其准确算子。

取 R1090 原整全纯基的约化 $(\omega_i)_{1\le i\le73}$。
令 $H=T_3+T_5$ 在此基上的矩阵使用原 row-action 约定：
$$
H\omega_i=\sum_j H_{ij}\omega_j.
$$
记原已认证完整列
$$
\lambda_4=\left(q^{-1}\log D_4(\omega_i)\right)_i.
$$
则
$$
\mathcal L=
 [\,\lambda_4,\ H\lambda_4,\ \ldots,\ H^{72}\lambda_4\,]
\tag{1103.3}
$$
是从 $\mathbb T/q$ 的 $1,H,\ldots,H^{72}$ 坐标到原 Lie 读数的可逆矩阵。
它的可逆性来自 (1103.2) 和 R1096 的整生成元 $H$，不是待猜测的新秩。
不同整全纯 lift 不改变本篇模 $q$ 的列。

令
$$
a=(T_2-1)/2\in\mathbb T^\times.
$$
R1096 定义 $\Gamma(T)=q^{-1}h(D_4,T D_{16})$，其中 $D_{16}=aD_4$。
若 $\kappa\in\mathbb T/q$ 是这个泛函的原迹坐标，则本篇使用
$$
K=a^{-1}\kappa,\qquad
q^{-1}h(SD_4,TD_4)\equiv
 \operatorname{Tr}_{\mathbb T/q\,/\,\mathbb F_q}(KST)\pmod q.
\tag{1103.4}
$$
这保留了移动算子 $a$；不将 $\kappa$ 本身误当原 $D_4$ 的高度系数。
也不要求 $K$ 在每个残余因子上为单位。

固定 R1094 所构造的原整、各向同性、Hecke 稳定 Hodge 补空间 $W$。
以下全局与局部高度均采用同一个 $W$ 及原圆分高度字符。

## 2. 八个原 CM 点的真正粗切向

令 $y$ 为其中一个实际 CM 点，$J=j(y)$。
原规范47-Cartan 被该椭圆曲线的全部 CM 单位保持。
在 $q>3$ 的好模型上，泛 $j$ 点的有效自同构平凡；在 $j=1728,0$ 处，规范 Cartan 的稳定子正是底椭圆曲线的完整有效稳定子。
因此原粗模映射 $j$ 在这八个指定点上 étale。

所以
$$
z=j-J,\qquad z(y)=0
\tag{1103.5}
$$
是真正的原粗整参数，且 $U_y(\mathbb Q_q)$ 由 $z=qt$、$t\in\mathbb Z_q$ 参数化。
这里不把一个任意47-necklace 的 elliptic branch 换成规范 CM branch。

在物理短模型及微分
$$
E:\ y_E^2=x_E^3+A x_E+B,\qquad
\omega_E=\frac{dx_E}{2y_E},\qquad
\Delta_0=4A^3+27B^2
$$
下，原 Kodaira--Spencer 规范是
$$
\operatorname{KS}(\omega_E^2)
 =\frac{9B\,dA-6A\,dB}{2\Delta_0},
\qquad
j=\frac{6912A^3}{\Delta_0}.
\tag{1103.6}
$$
$A$ 固定时，第一式为 R1091 的 $-3A\,dB/\Delta_0$；
另一项也由权四/六的缩放方向被 KS 杀掉唯一确定。
直接微分给
$$
dj=\frac{124416A^2B}{\Delta_0}
       \operatorname{KS}(\omega_E^2).
\tag{1103.7}
$$

每个原 Hodge 形式写为
$$
\omega_i=F_i(E,\omega_E)\operatorname{KS}(\omega_E^2).
$$
$F_i$ 是 R1090 原95个 $F_{a,\rho}$ 的同一个73维 kernel 组合。
所有47挠点、两个不同的 Weil 相位以及 $\rho$ 的实际共轭方向继续保留。

### 2.1 普通粗 $j$ 值：只需有限点值

若 $\bar J\ne0,1728$，由 (1103.7)，
$$
\boxed{\quad
e_{y,i}:=\frac{\omega_i}{dz}(y)
 =\frac{\Delta_0}{124416A^2B}\,F_i(E_y,\omega_E).
\quad}
\tag{1103.8}
$$
这里“普通粗 $j$ 值”只表示非 elliptic $j$ 值，不表示该椭圆曲线在4513普通。
原两个 $-7,-28$ CM 点在4513超奇异，仍可使用 (1103.8)；
必须使用 R1086 已识别的实际 CM necklace，不能任取一个 Frobenius-stable Cartan。

### 2.2 高斯点：完整 fine 一阶，粗参数不再除二

在 $j=1728$，固定 $A\in\mathbb Z_q^\times$，以 $B$ 为 fine 参数。
规范 $\mu_4$ 的作用及原微分的下降给
$$
F_i(A,B)=f_{i,1}B+O(B^3).
$$
又
$$
j-1728=-\frac{11664}{A^3}B^2+O(B^4),\qquad
\operatorname{KS}(\omega_E^2)
 =-\frac{3}{4A^2}dB+O(B^2)dB.
$$
于是
$$
\boxed{\quad e_{y_4,i}=\frac{A}{31104}\,f_{i,1}.\quad}
\tag{1103.9}
$$
原已用模型 $A=343$ 及其真实47基可以直接消费。
粗模二次参数的 Jacobian 已在 (1103.9) 中；没有另一个 stabilizer 因子。

### 2.3 三次点：完整 fine 二阶，粗参数不再除三

在 $j=0$，固定 $B\in\mathbb Z_q^\times$，以 $A$ 为 fine 参数。
规范 $\mu_6$ 给
$$
F_i(A,B)=f_{i,2}A^2+O(A^5).
$$
由
$$
j=\frac{256}{B^2}A^3+O(A^6),\qquad
\operatorname{KS}(\omega_E^2)=\frac{dA}{6B}+O(A^3)dA
$$
得到
$$
\boxed{\quad e_{y_3,i}=\frac{B}{4608}\,f_{i,2}.\quad}
\tag{1103.10}
$$
所有分母只含2、3的幂，都是4513单位。

### 2.4 两个短 jet 的有限代数读取

可以直接在原47挠点上作一阶、二阶 Hensel 提升。
等价的短算法使用同一个代数 heat derivation
$$
\partial A=6B,\qquad \partial B=-4A^2/3,
\tag{1103.11}
$$
以及每个原47挠点的
$$
\begin{aligned}
\partial e_P&=-e_Px_P-y_P,\\
\partial x_P&=2x_P^2+2e_Py_P+4A/3,\\
\partial y_P&=3x_Py_P+e_P(3x_P^2+A).
\end{aligned}
\tag{1103.12}
$$
这些是 R1090 的原 theta/Weierstrass 热恒等式在同一短模型 frame 下的代数部分。
它们也由完整 Ramanujan/weight 系统逐项相减得到。
本节只读取实际 fine 参数的有限导数，不把这个 $\partial$ 误称为所有阶的 unit-root 导数。

高斯点有
$$
f_{i,1}=-\frac{3}{4A^2}(\partial F_i)(A,0),
$$
三次点有
$$
f_{i,2}=\frac{(\partial^2F_i)(0,B)}{72B^2}.
\tag{1103.13}
$$
后一式在完整流中微分以后才取 $A=0$；
不能在第一次微分前删除系数中含 $A$ 的项。
例如 $\partial^2$ 的系数导数在 $A=0$ 才消失，留下
$36B^2\partial_A^2F_i=72B^2f_{i,2}$。

最终原切向的 $\mathbb T/q$ 坐标是
$$
\boxed{\quad b_y=\mathcal L^{-1}(e_{y,i})_i.\quad}
\tag{1103.14}
$$
这是 column 方向的公式，与原 Hodge row-action 相容。
没有新增 period，也没有删掉 $B$ 或乘入另一个 $q$。

## 3. 第三类微分首项由有限域唯一确定

本节对任意 $\mathbb Q_q$ 上的 degree-zero 除子 $D$ 成立，只要求其全部几何支撑避开 $U_y$。
令 $\omega_D^W$ 为原 $W$ 规范的第三类微分，并令
$$
\bar D=\operatorname{sp}D,\qquad
N=\#J(\mathbb F_q).
$$
R1089 给 $q\nmid N$。

### 3.1 从原高度规范到有限域 dlog：不假设 Cartier-fixed 就是 $W$

因 $N$ 杀 $J(\mathbb F_q)$，存在
$\bar f\in\mathbb F_q(X)^\times$，满足
$$
\operatorname{div}\bar f=N\bar D.
\tag{1103.15}
$$
这包括所有几何点和重数。有限域的 rational principal divisor 可取基域函数：
可由 Riemann--Roch 核的一维下降，或 Hilbert90 直接证明。

取避开 $\bar y$ 的足够大的辅助 RR 极除子，将 $\bar f$ 提升为
$f\in\mathbb Q_q(X)^\times$，并取垂直赋值为零。
相对 RR 的 $H^1=0$ 给提升；因为 $\bar f$ 在 $\bar y$ 为单位，
$f$ 在整个 $U_y$ 的形式环中为单位。
因此
$$
E=ND-\operatorname{div}f
$$
在每个几何剩余盘上的 specialization 都为零，而且其支撑仍避开 $U_y$。

R1094 的整双极核与完整 Galois 多重集估值给
$$
\omega_E^W|_{U_y}\in q\,\mathbb Z_q[[z]]\,dz.
$$
规范第三类微分对 principal divisor 准确为 $d\log f$，故
$$
N\omega_D^W-d\log f=\omega_E^W.
$$
于是 $\omega_D^W$ 在 $U_y$ 整，并得到
$$
\boxed{\quad
\overline{\omega_D^W}|_{U_y}
 =N^{-1}d\log\bar f|_{U_y}.
\quad}
\tag{1103.16}
$$
右边独立于 $\bar f$ 乘常数的选择，亦独立于任何整各向同性 $W$。
这个独立性来自实际整核估值；没有把一个抽象 Cartier 特征条件直接当成特征零的 $W$ 规范。

特别
$$
\alpha_{D,y}:=
 \left(\frac{\omega_D^W}{dz}(y)\bmod q\right)
 =\left(\frac{N^{-1}d\log\bar f}{dz}\right)(\bar y).
\tag{1103.17}
$$

### 3.2 不必构造巨大 $N$ 函数的等价有限算法

令 $S$ 为 $\bar D$ 的 reduced support。
由总留数序列，先取任意
$$
\eta\in H^0(X_{\mathbb F_q},\Omega^1(S))
$$
使每个几何点的 residue 为 $\bar D$ 的对应整数系数模 $q$。
全部 conjugates 同时保留。存在性来自总留数为零；这是基域上的线性 RR 问题。

Cartier 算子 $C$ 固定这些 $\mathbb F_q$ 整数 residues，所以
$$
C\eta-\eta\in H^0(X_{\mathbb F_q},\Omega^1).
$$
原 Hodge 空间上有准确等式
$$
C=\overline{T_q}.
\tag{1103.18}
$$
证明是在 R1090 的原 cusp 参数 $t=q_\tau^{1/47}$ 上：
$\omega=47\sum c_nt^{n-1}dt$ 的 Cartier 读数是
$47\sum c_{qn}t^{n-1}dt$；
原 Hecke 公式中另一项含 $q$，而 $q\equiv1\pmod {47}$ 使两个 Weil-root 重标都为恒等。
全局相等由原 q-expansion 原理得出。

所以
$$
1-C=\overline{q+1-T_q}=\bar B
$$
是可逆的实际73维矩阵。唯一 prescribed-residue Cartier-fixed 形式为
$$
\boxed{\quad
\eta_{\rm fix}
=\eta-(C-1)^{-1}(C\eta-\eta),\qquad
\alpha_{D,y}=(\eta_{\rm fix}/dz)(\bar y).
\quad}
\tag{1103.19}
$$
它就是 (1103.16) 的 $N^{-1}d\log\bar f$：
后者具有相同 residues 且 Cartier-fixed，二者之差全纯，$C-1$ 可逆。

本式可以用原 Hodge 矩阵和 normalized-newform/CRT 的 $T_q$ 读取，
不用把 cusp 展开推进到 $4513\cdot167$。
但仍必须实际构造 $\eta$ 并读取其 Cartier 差。
只知道73维 Hodge 基，并不自动给出这个亚纯 RR 输入。
另一合法实现是完整 finite-field Miller/RR 计算 (1103.15) 的 $d\log$；本篇未执行任一实现。

## 4. 原角除子的支撑与可计算数据

令 $Z$ 是原非恒等 Cartan 角的对称整数线性组合，且
$$
\operatorname{Tr}(Z|H^0\Omega)=0.
$$
允许 $\deg Z\ne0$。
Lefschetz 公式给 $\deg\operatorname{Fix}Z=2\deg Z$，所以
$$
D_{Z,y}=\operatorname{Fix}Z-2Z(y)
\tag{1103.20}
$$
是 degree-zero 除子。其原 MW 坐标记为 $d_{Z,y}\in\mathbb T/q$。

在4513的实际规范 CM 点 $\bar y$，所有非恒等角支都把该 necklace 送到不同 coarse 点。
一般 $j$ 的有效自同构平凡；两个 elliptic $j$ 的全部单位则保持 canonical Cartan。
$q$ 不整除有限47-level 群阶，原有限商和各支的 pull--push 保持这些特殊纤维重数。
因此 $Z(y)$、$\operatorname{Fix}Z$ 的全部几何支撑避开 $\bar y$，
整个 $U_y$ 与 $Z(U_y)$ 也不相交。
没有删除 signed combination 中相消前的 raw 支撑。

R1078 的准确 cycle 公式仍是
$$
\operatorname{Fix}Z=
 \tfrac12(\mathcal F_4^*Z)y_4+
 \tfrac23(\mathcal F_3^*Z)y_3+n_ZC_\infty.
\tag{1103.21}
$$
由 degree 和 trace 的等式，全部 cusp 系数相消后给
$$
23[D_{Z,y}]
=\tfrac12(\mathcal F_4^*Z)u_4+
 \tfrac23(\mathcal F_3^*Z)u_3-2Zu_y.
\tag{1103.22}
$$
这条 Picard 恒等式只需要 trace zero，不需要 degree zero。
证明时使用 $ZC_\infty=(\deg Z)C_\infty$；
其余 cusp 系数是
$\tfrac12\deg\mathcal F_4^*Z+\tfrac23\deg\mathcal F_3^*Z+
23n_Z-2\deg Z=0$。
所以不能在中途把 $ZC_\infty$ 当成零。

式 (1103.22) 给有限读取 $d_{Z,y}$ 的准确目标，
仍保留每个原 CM 类及其真实角作用；它不是已经计算出的 coordinate vector。

## 5. 只有二次首项的整解析 QC 差

令 $x=x(t)\in U_y(\mathbb Q_q)$，$z(x)=qt$，并置 $P=x-y$。
用 (1103.2) 将其 Abel 对数准确写为
$$
\log P=A_y(t)\log D_4,\qquad A_y(t)\in\mathbb T\langle t\rangle.
\tag{1103.23}
$$
这里定义的是实际对数空间的解析坐标，不声称所有 $x(t)$ 都是有理点或 MW 点。

任一整 Hodge 微分 $\sum_{n\ge0}c_nz^n dz$ 的 Abel primitive 除以 $q$ 是
$$
\sum_{n\ge0}\frac{c_nq^n}{n+1}t^{n+1}.
$$
当 $n\ge1$，$n-v_q(n+1)\ge1$，且趋于无穷。
结合 (1103.3)，
$$
A_y(t)\equiv t b_y\pmod q.
\tag{1103.24}
$$

原 bilinear 高度从 MW 对数空间延拓，定义
$$
f_{Z,y}(t)=q^{-1}\left\{
 h(P,D_{Z,y}-ZP)-h_q^W(P,D_{Z,y}-ZP)
\right\}.
\tag{1103.25}
$$
全局项的第一槽使用 (1103.23)，第二槽使用 $d_{Z,y}-Z A_y(t)$；
这给一个定义在整个原盘的解析函数，不以 $x$ 有理作为定义前提。

由第3节，$\omega_{D_{Z,y}}^W$ 在 $U_y$ 整，故
$$
q^{-1}h_q^W(P,D_{Z,y})
 \equiv \alpha_{Z,y}\,t\pmod q,
\quad \alpha_{Z,y}:=\alpha_{D_{Z,y},y}.
\tag{1103.26}
$$

另一方面，
$$
h_q^W(P,ZP)\in q^2\mathbb Z_q\langle t\rangle.
\tag{1103.27}
$$
具体地，在 $U_y\times Z(U_y)$ 上使用 R1094 的实际整双极核，
沿原 finite tame Cartan correspondence 作 pull--trace，得到
$U_y\times U_y$ 上的整双微分。
源和目标不交，故没有 diagonal 主部。
两次从零积分的系数为
$$
c_{rs}\frac{q^{r+s+2}}{(r+1)(s+1)}.
$$
除以 $q^2$ 后仍整并趋于零。
原粗模 ramification 的所有分支及 pullback Jacobian 都在 trace 中；
等价地可用 R1094 的整个 Galois signed-multiset / norm polynomial 证明。
不能把 ramified 端点逐个冒称为 $q$-深点。

因而 (1103.25) 是整 restricted analytic 函数，$f_{Z,y}(0)=0$，且
$$
\boxed{\quad
\bar f_{Z,y}(t)
=t(B_{Z,y}+A_{Z,y}t),
\quad
A_{Z,y}=-\operatorname{Tr}(K\,z_Z b_y^2),
\quad
B_{Z,y}=\operatorname{Tr}(K\,b_y d_{Z,y})-\alpha_{Z,y}.
\quad}
\tag{1103.28}
$$
$z_Z\in\mathbb T/q$ 是原 $Z$ 的整作用。
$K$、$d_{Z,y}$、$\alpha_{Z,y}$ 三项都保留；全局高度单位不允许省去后两项。

上述所有高阶估值对整个 $t\in\mathbb Z_q$ 成立，
不只是 $t$ 在一个更小的邻域。
因此这里已经给出所需尾项控制，不需要凭有限截断猜整个盘的零点数。

## 6. 一个准确的、可执行的盘内唯一性判据

选若干原 $Z_\nu$ 如第4节。
另外须对正在研究的有理点集合验证真正的全局前提：
$$
h_\ell\!\left(x-y,\operatorname{Fix}Z_\nu-Z_\nu x-Z_\nu y\right)=0
\quad\text{对所有 }\ell\ne q.
\tag{1103.29}
$$
如果采用 R43/R148 的原 Poincare 规范截面，
应从其好整模型和实际 vertical correction 证明 (1103.29)；
不能仅因某个 $\deg Z_\nu=0$，或从另一个 principal 组合的 cusp 消去，直接推给所有新 $Z_\nu$。
R1074§9 已支付八个原坏47管域的相应项。
本篇不将其余未核条件隐藏在“QC”一词中。

在 (1103.29) 成立的有理点上，全球高度的局部和给
$f_{Z_\nu,y}(t)=0$。
如果原有限矩阵
$$
\begin{pmatrix}
 A_{Z_1,y}&B_{Z_1,y}\\
 A_{Z_2,y}&B_{Z_2,y}\\
 \vdots&\vdots
\end{pmatrix}
\tag{1103.30}
$$
在 $\mathbb F_q$ 上秩二，则这些函数的共同约化零点只有 $t=0$。
确实，非零 $t$ 会使向量 $(t,1)$ 同时被所有行杀掉。
秩二又保证线性系数这一列非零，即某个 $B_{Z_\nu,y}\ne0$；
对这个整 analytic 函数，零点 $t=0$ 是 simple，并且它对应已知的准确 CM 点 $y$。
Hensel 唯一性在整个 $t\equiv0\pmod q$ 类给唯一提升；
其它 residue classes 已被共同约化排除。
于是正在研究的有理点集合在整个 $U_y$ 中只有 $y$。

另一足够情形是所有 $A_{Z_\nu,y}=0$、但某个 $B_{Z_\nu,y}\ne0$。
其余秩一或全零情形均不自动排盘：
可能有额外残余根或多重根，必须继续原精度，而不是将 $K$ 的单位性代入结论。

## 7. 当前新输入的边界

| 数据 | 实际读取 | 本篇结论 |
|---|---|---|
| $b_y$ | 原95来源、73核、真实47标记，点值及最多二阶 fine jet；再用 (1103.14) | 完整有限算法，尚不报告数值 |
| $K$ | 原完整全局高度泛函的 $\kappa$，再除 $a$ | 精确尺度 (1103.4)，不预设非零块 |
| $z_Z,d_{Z,y}$ | 原角算子和完整 fixed-cycle / 三类 CM 关系 (1103.22) | 全 cusp 和 degree 项已保，坐标尚需读取 |
| $\alpha_{Z,y}$ | 规定 residues 的原亚纯 RR 源，加 (1103.19)；或 finite-field Miller | 规范与 $W$ 的关系已证明，实际函数尚需构造 |
| 整尾 | 单/双积分的完整 $q$ 赋值 | 已证明，覆盖整个 $U_y(\mathbb Q_q)$ |
| 非 $q$ 项 | 原好模型的 Poincare 规范及坏47 vertical 项 | 判据明确要求 (1103.29)，不假定所有新组合已通过 |

原点限制、整 MW 格和全局高度计算是这个判据的输入。
本篇没有声称已完成八个原盘的数值验证，更不把固定47的结论当成 Serre 一致性完成。

## 8. 来源与独立纸核

- [R1090](R1090-original-weight-one-integral-Hodge-source.md)：原两相位 Reynolds 族、整95格、全部23 residues、实际 Hodge73及热恒等式。
- [R1091](R1091-original-Gaussian-CM-logarithm-as-one-algebraic-coefficient.md)：相同物理短模型的 KS、原 $B_q$ 与 Gaussian 首对数尺度。
- [R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)、
  [R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)：整 MW 对数同构、原 $H$、$a$ 和全局迹高度规范。
- [R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md) §§1–4：整各向同性补空间、两变量整核和 ramified Galois 多重集估值；其已核 Coleman--Gross / Coleman reciprocity 来源继续适用。
- R43、R148、R707、R1074§9、R1086：实际高度方程、基点规范及已付原残余盘范围；本篇不重跑旧41结论。
- Cartier 的 logarithmic identity、simple-pole residues 规则也可直接在一个分离参数中由
  $C(\sum a_nt^n dt)=\sum a_{qn+q-1}^{1/q}t^n dt$ 核准。
  全局 $C=\bar T_q$ 已在 (1103.18) 从本曲线的实际 Tate 公式证明，不从另一个曲线的 Hasse--Witt 矩阵搬来。

o1 已独立纸核三种 coarse 切向和全部常数；
o2 已独立纸核第3节有限域归一化，特别辅助 RR lift、whole Galois cycle 和 $W$ 边界。
o2 亦已独立纸核第5–6节的原 $K=\kappa/a$ 缩放、完整 pull--trace 双积分与 simple-root 判据；线性系数在本篇记为 $B_{Z,y}$。非 $q$ 前提仍严格按 (1103.29) 保留。

root另逐节核原KS/heat系数、同一a/B/q尺度、RR提升的whole-tube单位、Cartier差的唯一性及完整双积分尾；非q条件仍按(1103.29)保留。
