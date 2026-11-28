# R1201：原最高 packet 的 CM 核首对数值为单位

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对 R1197 的原最高 packet 完整 CM profile 核
$T_*(b)=(b^3-1)^{2g-1}$，R1199–1200 所定义的同一
$P=(p-1)D_0$ 的完整首对数值有精确公式
$$
\boxed{\qquad
V_m(T_*)=\frac{32m\,c_m^0\,\nu}
 {\binom{m}{\,2g-1\,}^{\,2}}\in k^\times.
\qquad}
\tag{1201.1}
$$
全部 normal 交叉项、原三个 CM 支、同一个 Cartier–Weil 相位和原参考权都在此公式中保留。证明先用准确的 Jacobi quadrature 消去 supersingular 求和，再算 CM 端点 $32$，最后在特征 $p$ 中构造一个显式多项式原函数，使剩余安全积分严格为零。

这不是“全部简单极部消失”的论证；该路线已被原有限诊断排除。本文也没有把整
$E_m=\tau_m+\mathrm{PS}_{m-1}$ packet 的单位，自动投成指定非 CM 因子 $C$ 上的单位；没有宣布同一 $\beta$ 的两列楔或 whole-disc 排除已经成立。

## 1. 原有限源与准确归一

保持
$$
p=12g-1>37,\qquad
n=2g-1,\qquad m=6g-1=3n+2,\qquad p=6n+5.
$$
$n,m$ 都是奇数。另记
$$
\alpha=2n+2=4g,\qquad
r(b)=1-b^3,\qquad
A(b)=bQ(b^3),
$$
其中 $A$ 是 R1200 的 monic supersingular polynomial，故 $Q$ monic 且
$\deg Q=n$。以下用于多项式的变量写作 $B=b^3$，避免与曲线点 $P$ 混淆。

R1200 §8.1 已严格消去原
$\lambda=-6(b+1)/r$ 在完整求和中的常数部分。令
$$
\lambda_1(b)=-6b/r(b),\qquad T_*(b)=-r(b)^n,
$$
$$
\mathcal P_m^{\lambda_1}(T_*)(b)=\mathsf P(b^3),\qquad
\mathsf P\in k[B],\quad \deg\mathsf P\le3n+1.
\tag{1201.2}
$$
这只是完整有限收缩之后的已证对称消去，不把原单点的
$G(b_{\rm lift})^2$ 换成另一个单位。

原参考权仍为
$$
w_a=\frac{2(-1)^{m-a}(m-1)!}
 {(a-1)!(m-a+2)!},\qquad 1\le a\le m.
\tag{1201.3}
$$
R1200 的单位是
$$
c_m^0=(-1)^{(m-1)/2}
       \binom{m-1}{(m-1)/2},\qquad
\nu=(-3)^{(m-1)/2}(2\gamma)^{m-1}\in\mathbf F_p^\times.
$$
$\gamma$ 来自原共同 Weil 根；没有重新选节点根。已证完整值是
$$
V_m(T_*)=-m c_m^0\nu\,\Sigma,\qquad
\Sigma=\sum_{A(s)=0}
 \frac{\mathsf P(s^3)}
 {(1-s^3)^{n+2}A'(s)^2}.
\tag{1201.4}
$$

由 R1200.26 的实际微分算子形式，每项
$r^jT_*^{(j)}$ 都被 $r^n$ 整除：$j\le n$ 时逐次微分最多降低 $j$ 阶，$j>n$ 时已有 $r^j$。所以
$$
\mathsf P(B)=(1-B)^n H(B),\qquad
H\in k[B],\quad \deg H\le2n+1.
\tag{1201.5}
$$
下面所有形式积分都是对次数至多 $p-2$ 的多项式逐单项积分；从不反除 $p$。

## 2. 原 $Q$ 的准确 Jacobi quadrature

### 2.1 同一个 polynomial 的 Rodrigues 公式

将 R1200.30 中 $A=bQ(B)$ 代入，直接得到
$$
B(1-B)Q''+\frac43(1-2B)Q'-\frac{25}{36}Q=0.
\tag{1201.6}
$$
因 $p=6n+5$，这是参数 $\alpha=2n+2$ 的 shifted Jacobi 方程
$$
B(1-B)Q''+
 [\alpha+1-(2\alpha+2)B]Q'
 +n(n+2\alpha+1)Q=0.
$$
其 monic 解唯一：逐低次比较时需要反除
$(n-i)(n+i+2\alpha+1)$，$0\le i<n$；这两个因子都非零模 $p$。

置 $w(B)=B^\alpha(1-B)^\alpha$。准确的 monic Rodrigues 式为
$$
\boxed{\qquad
Q(B)=\frac1{n!\,w(B)}
 \frac{d^n}{dB^n}\bigl(B^m(1-B)^m\bigr).
\qquad}
\tag{1201.7}
$$
分子在两端至少有阶 $m-n=\alpha$，故右侧为次数 $n$ 的多项式，并直接满足 (1201.6)。其最高系数为
$(-1)^n(p-1)!/[n!(5n+4)!]=1$：
$n$ 为奇数，Wilson 给
$n!(5n+4)!=n!(p-1-n)!=1$。特别
$$
Q_0:=Q(0)=\binom mn\in k^\times,\qquad
Q(1)=(-1)^nQ_0=-Q_0.
\tag{1201.8}
$$

对 $\deg G<n$，将 (1201.7) 分部积分 $n$ 次。端点的全部边界项为零，最后 $G^{(n)}=0$，所以
$$
\int_0^1 w(B)Q(B)G(B)\,dB=0.
\tag{1201.9}
$$
这里总次数至多 $p-2$；每一步均在同一个 $p$-整多项式积分中合法。

### 2.2 Gauss 权的常数严格为 $1$

令 $q_j$ 为同一 $\alpha$ 下的 monic shifted Jacobi polynomial。
只需 $j\le n-1$。Rodrigues 分部积分和
$\int_0^1 B^a(1-B)^c\,dB=a!c!/(a+c+1)!$
给
$$
h_j:=\int_0^1 w\,q_j^2
 =\frac{j!(j+\alpha)!^2(j+2\alpha)!}
 {(2j+2\alpha+1)!(2j+2\alpha)!}.
\tag{1201.10}
$$
这里所有 factorial 下标小于 $p$。

由同一方程，或将两侧按这些 monic 正交多项式展开，得
$$
B(1-B)Q'
 =(-nB+n/2)Q+d_nq_{n-1},
$$
$$
d_n=\frac{n(n+\alpha)(n+2\alpha)}
 {2(2n+2\alpha-1)(2n+2\alpha)}.
\tag{1201.11}
$$
常数也可在 $B=0$ 由
$d_n=-nQ(0)/(2q_{n-1}(0))$ 直接确定。

先用插值定义 quadrature 权。由 (1201.9)，它对次数至多
$2n-1$ 的多项式 exact。将此 exactness 用于
$q_{n-1}(B)Q(B)/(B-s)$，得到每个 $Q(s)=0$ 的权
$$
\frac{h_{n-1}}{Q'(s)q_{n-1}(s)}
 =\frac{h_{n-1}d_n}{s(1-s)Q'(s)^2}.
$$
由 (1201.10)–(1201.11)，
$$
h_{n-1}d_n
 =\frac{n!\,m!\,(m-1)!\,(5n+4)!}
 {2(p-1)!(p-2)!}=1.
$$
最后一步用
$n!(5n+4)!=1$、$(m!)^2=1$、$m^{-1}=-2$；
这些都在原 $p=6n+5$ 中成立。因此
$$
\boxed{\quad
\sum_{Q(s)=0}\frac{F(s)}{s(1-s)Q'(s)^2}
 =\int_0^1 B^\alpha(1-B)^\alpha F(B)\,dB
 \quad(\deg F\le2n-1).
\quad}
\tag{1201.12}
$$
这不是只知道权到非零比例；原 monic $Q$ 的比例已经等于 $1$。

## 3. 两个端点的准确修正

在 $A$ 的非零根处，$A'(s)=3s^3Q'(s^3)$，每个 $Q$ 根对应三个 $s$。因此 (1201.4) 的全和为
$$
\Sigma=\frac{H(0)}{Q_0^2}
 +\frac13\sum_{Q(t)=0}
 \frac1{t(1-t)Q'(t)^2}\,
 \frac{H(t)}{t(1-t)}.
\tag{1201.13}
$$
第二个输入虽不是多项式，但只在 $0,1$ 有简单极。写
$$
\frac{H(B)}{B(1-B)}
 =F_{\rm pol}(B)+\frac{H(0)}B+\frac{H(1)}{1-B},
\qquad \deg F_{\rm pol}\le2n-1.
$$

定义
$$
\mathcal B=\int_0^1 B^{\alpha-1}(1-B)^m\,dB
 =\frac{(\alpha-1)!\,m!}{(5n+4)!}.
$$
将 (1201.7) 对 $1/B$ 分部积分 $n$ 次，准确给
$\int wQ/B=\mathcal B$。将 (1201.12) 用于多项式
$(1-Q(B)/Q_0)/B$，便得
$$
\sum_{Q(t)=0}\frac1{t(1-t)Q'(t)^2}\frac1t
 =\int_0^1\frac{w(B)}B\,dB-\frac{\mathcal B}{Q_0}.
$$
反射 $B\mapsto1-B$ 给 $1/(1-B)$ 的相同修正。又
$$
Q_0\mathcal B
 =\frac{(m!)^2}{\alpha\,n!(5n+4)!}
 =\frac1\alpha=3.
\tag{1201.14}
$$
故原 $s=0$ 项恰好消去 $0$ 端点的修正，而不是被人为删除：
$$
\boxed{\quad
\Sigma=\frac13 I-\frac{H(1)}{Q_0^2},\qquad
I=\int_0^1 B^{2n+1}(1-B)^{n+1}\mathsf P(B)\,dB.
\quad}
\tag{1201.15}
$$
被积多项式次数至多
$2n+1+n+1+3n+1=6n+3=p-2$。式 (1201.15) 保留了全部 supersingular 简单极部可能非零的情形。

## 4. 原 CM 端点严格为 $32$

取任意 $c^3=1$，写 $b=c+x$。则
$$
r=R x+O(x^2),\quad R=-3c^2,\qquad
\lambda_1=\frac{\lambda_{\rm res}}x+O(1),\quad
\lambda_{\rm res}=2/c.
$$
计算 $H(1)=\lim_{b\to c}\mathcal P_m^{\lambda_1}(T_*)/r^n$ 时，只需原 Picard–Fuchs 方程的最低 Euler 部分
$$
f''+\frac1x f'-\frac1{36x^2}f=0.
\tag{1201.16}
$$
这不是丢弃原有限函数：R1200.26 已证明输出至少有 $r^n$，
对有限递推取 $x$ 的最低齐次项，正给 (1201.16)；
方程或输入的任一更高项都会提高最终 $x$ 阶。

完整收缩的 framing 不变性允许在这一步取
$f_0=(1+t/x)^{-1/6}$。规范周期比及其逆为
$$
\xi=3x\bigl((1+t/x)^{1/3}-1\bigr),\qquad
1+t/x=(1+v/(3x))^3.
$$
因 $3\alpha=p+1$，全部所需次数小于 $p$ 的最低 jet 给
$$
D_a=\frac{3\lambda_{\rm res}(-1)^{a-1}}
 {a(3x)^a},
$$
$$
\widetilde e_N(T_*)
 =-R^\alpha x^\alpha
   \binom mN(3x)^{-N}.
\tag{1201.17}
$$
这是同一个 $\widetilde e_N=-r^\alpha f_0^3$；
$(1+v/(3x))^{p+1-3/2}$ 在当前次数范围等于
$(1+v/(3x))^{-1/2}$，且 $-1/2=m$ 于 $k$。

令 $N=m-a$。$m$ 为奇数，(1201.3) 与 (1201.17) 的两个符号相消。Vandermonde 恒等式给
$$
\sum_{a=1}^m
 \frac{w_a(-1)^{a-1}}a\binom m{m-a}
 =
 \frac{2}{m(m+1)(m+2)}
 \left(\binom{2m+2}{m}-1\right)
 =
 -\frac2{m(m+1)(m+2)}.
\tag{1201.18}
$$
这里 $2m+2=p+1$，$2\le m<p-1$，故
$\binom{p+1}m=0$ 于 $k$。

带回算子前面的 $r^{m-2g-1}$ 并除以 $r^n$，
得到
$$
H(1)
 =\frac{6\lambda_{\rm res}(R/3)^m}
 {m(m+1)(m+2)}
 =-\frac{12}{m(m+1)(m+2)}
 =32.
\tag{1201.19}
$$
使用了 $(R/3)^m=(-c^2)^m=-c$ 及
$m(m+1)(m+2)=-3/8$。没有将原模型常数规范化掉。

## 5. 特征 $p$ 的准确微分恒等式

下面严格计算 (1201.15) 的积分，使用同一个有限周期源。

对形式函数 $K,E$ 定义
$$
\operatorname{RC}_N^{2,3}(K,E)=
 \sum_{i+j=N}(-1)^j
 \binom{N+1}{j}\binom{N+2}{i}
 K^{(i)}E^{(j)}.
\tag{1201.20}
$$
这里导数都是对同一周期变量取导数。所有阶数小于 $p$；
本文直接证明所需恒等式，不借用任何未支付的比较定理。

若 $D_a=[v^a]\mathcal H(v)$、
$E_N=[v^N]E(v)$，$K=\mathcal H'$，则逐项比较 factorial 得
$$
\sum_{a=1}^m w_aD_aE_{m-a}
 =\frac{2}{m(m+1)!}
   \operatorname{RC}_{m-1}^{2,3}(K,E).
\tag{1201.21}
$$
对 (1201.20) 求导，在目标项 $K^{(i)}E^{(j)}$、
$i+j=m-1$ 的系数中，导数与
$\operatorname{RC}_{m-1}^{2,3}$ 的比为
$$
\frac{m(m-1)-(2m+1)j}{m(m+1)}
 =\frac{m-1}{m+1},
$$
因为 $2m+1=p=0$。因此
$$
\frac d{dv}\operatorname{RC}_{m-2}^{2,3}
 =\frac{m-1}{m+1}\operatorname{RC}_{m-1}^{2,3}.
$$
置
$$
\mathcal T(K,E)
 =\frac{2}{m(m-1)m!}
   \operatorname{RC}_{m-2}^{2,3}(K,E).
$$
则准确有
$$
\boxed{\qquad
\frac d{dv}\mathcal T(K,E)
 =\sum_{a=1}^m w_aD_aE_{m-a}.
\qquad}
\tag{1201.22}
$$

### 5.1 低一阶表达也具有需要的 framing 不变性

对 $f_0\mapsto f_0+cf_1$，同一归一变量满足
$$
K_{\rm new}(v)=(1-cv)^{-2}
 K\!\left(\frac v{1-cv}\right),\qquad
E_{\rm new}(v)=(1-cv)^{-3}
 E\!\left(\frac v{1-cv}\right).
$$
用 Taylor 系数写 (1201.20)，其 $K_iE_j$ 系数为
$$
(-1)^j\frac{(N+1)!(N+2)!}{(i+1)!(j+2)!}.
$$
对 $c$ 微分，
$\dot K_i=(i+1)K_{i-1}$、
$\dot E_j=(j+2)E_{j-1}$，相邻两项准确抵消。
整个表达关于 $c$ 的次数至多 $N=m-2<p$，所以在基点的
$\mathcal T$ 严格不变。

这允许以下计算采用同一局部 finite period 的归一 $f_0$。
它不重新选择原 Kummer 根或 actual node parameter，也不把一个有限 Cartan 结构提升到整塔。

## 6. 同一源的显式多项式原函数

在任意普通计算基点 $b$，仍用 R1200 的有限解 $f_0,f_1$、
$\xi=f_1/f_0$、$J=\xi^{-1}$。令
$$
\mathcal H_b'(v)=
 \lambda_1(b+J(v))J'(v),\qquad
\mathcal H_b(0)=0,
$$
$$
K_b=\mathcal H_b',\qquad
E_b(v)=-r(b+J(v))^\alpha f_0(J(v))^3,
$$
$$
\mathcal T_b=
 \mathcal T(K_b,E_b)\big|_{v=0}.
\tag{1201.23}
$$
定义一个真正有理函数
$$
\mathcal J(b)=3b^p r(b)^{m-1}\mathcal T_b.
\tag{1201.24}
$$

### 6.1 原有限 period 逐项给出 $\mathcal J'$，没有未知比较常数

为检验这个有理函数的导数，只需次数至多 $m+1<p$ 的局部形式解。取同一个 Picard–Fuchs 方程的解 $y_0,y_1$，写
$$
z=y_1/y_0,\qquad z'=\frac C{r\,y_0^2},
$$
其中 $C$ 是同一 Wronskian 常数。令
$$
E_{\rm glob}(z)=-r^\alpha y_0^3,\qquad
K_{\rm glob}(z)=d\mathcal H/dz,\qquad
d\mathcal H/db=\lambda_1.
$$
在基点 $b$，归一
$$
f_0=y_0/y_0(b),\qquad
\xi=\frac{z-z(b)}{z'(b)}
$$
给
$$
\mathcal T_b=z'(b)^{m-1}y_0(b)^{-3}
 \mathcal T(K_{\rm glob},E_{\rm glob})(z(b)).
\tag{1201.25}
$$
上一节的有限 framing 恒等式保证这与原 $f_0'(0)=0$
定义的同一值相等。全收缩同样按
$z'(b)^m y_0(b)^{-3}$ 运输。

由 $2m+1=p$，(1201.24)–(1201.25) 变成
$$
\mathcal J
 =3C^{m-1}(b/y_0)^p\,
   \mathcal T(K_{\rm glob},E_{\rm glob}).
$$
在特征 $p$ 中 $d(b/y_0)^p=0$，再用 (1201.22)，准确得到
$$
\boxed{\quad
\mathcal J'(b)
 =3b^p r(b)^{m-1}
   \sum_{a=1}^m w_aD_a(b)\widetilde e_{m-a}(T_*;b)
 =3b^p r(b)^{2g}\mathsf P(b^3).
\quad}
\tag{1201.26}
$$
这个证明只用有限 ODE jet 来检验一个有理恒等式；
没有假定特征 $p$ 的整个 Gauss–Manin 连接存在两个独立的全局水平解。

### 6.2 原函数是有界次数多项式，并在两个端点为零

R1200 的实际有限递推给
$$
D_{i+1}\in r^{-(i+1)}k[b]_{\le2i+1}.
$$
当 $T_*=-r^n$ 时，同一个导数展开进一步给
$$
[v^j]E_b
 \in r^{\alpha-j}k[b]_{\le2j}.
\tag{1201.27}
$$
理由是 $r^\ell T_*^{(\ell)}/r^n$ 是次数至多 $2\ell$
的多项式；代入 R1200.26 前的展开，剩余因子次数至多
$2(j-\ell)$。

在 $\operatorname{RC}_{m-2}$ 的每项 $i+j=m-2$ 中，
$K_b^{(i)}=(i+1)!D_{i+1}$。于是
$$
\mathcal T_b\in r^{1-n}k[b]_{\le p-4},
$$
从而
$$
\boxed{\qquad
\mathcal J(b)=b^p r(b)^\alpha R(b),
\qquad R\in k[b],\quad \deg R\le p-4,
\quad \deg\mathcal J\le3p-3.
\qquad}
\tag{1201.28}
$$
这里的 $R$ 已吸收原常数 $3$ 及 (1201.22) 的全部 factorial。

同一三次对称性给 $K_b^{(i)}$ 的权 $1-i$，
$E_b^{(j)}$ 的权 $-j$，故 $\mathcal T_b$ 的权
$3-m\equiv1\pmod3$。乘以 $b^p$ 后总权为零。因此存在
$$
J_0(B)\in k[B],\qquad
\mathcal J(b)=J_0(b^3),\qquad
\deg J_0\le p-1.
\tag{1201.29}
$$
实际上同一权还给 $R\in b\,k[b^3]$，所以
$J_0\in B^\alpha(1-B)^\alpha k[B]$；特别
$J_0(0)=J_0(1)=0$。将 (1201.26) 除以
$3b^2$，并用 $(p-2)/3=2n+1$，得到
$$
J_0'(B)=B^{2n+1}(1-B)^{n+1}\mathsf P(B).
\tag{1201.30}
$$

所以 (1201.15) 中的准确多项式积分为
$$
\boxed{\qquad I=J_0(1)-J_0(0)=0.\qquad}
\tag{1201.31}
$$
此处次数界不可删：$\deg J_0\le p-1$ 排除了非恒定
$p$ 次幂造成的模 $p$ 积分歧义。只在更大的有理函数域中说
“导数为零”并不足以得到这个端点结论；本文已经给出同一实际原函数的多项式、次数及两端点证书。

## 7. 完整首列、单位性及剩余投影边界

由 (1201.15)、(1201.19)、(1201.31)，
$$
\boxed{\qquad
\Sigma=-\frac{32}{Q_0^2}.
\qquad}
\tag{1201.32}
$$
结合原 (1201.4) 和 $Q_0=\binom mn$，得到首式 (1201.1)。

所有分子因子 $32,m,c_m^0,\nu$ 都是单位；
$\binom mn$ 的全部 factorial 下标小于 $p$，也为单位。
因此原完整首列确实非零且具有原格中的单位尺度，
不只是在有理系数中非零。

本结论精确作用于 R1197–1199 的同一个整最高 packet 及其
CM profile 一维核。它同时使用原 MW 类 $P=(p-1)D_0$，
没有改用另一个 CM 点。它排除了“完整 CM profile 核也落入该原首对数列的核”的情形。

但是 $E_m$ 仍包含 $\tau_m$ 与 $\mathrm{PS}_{m-1}$；
本文没有删除 PS 上的原点类，也没有声称任意给定
$q_C$ 自动保存该单位。R1190 的格损失、R1191 的实际型槽、
R1196 的同 $\beta$ 运输与后续两列比较仍须按各自范围消费。
whole-disc 主目标没有因此自动完成。

## 来源与验证范围

- [R1197：原最高 packet 完整 CM profile](R1197-original-highest-packet-complete-CM-coefficient-flag.md)：使用其核 $T_*=(b^3-1)^{2g-1}$。
- [R1199：全部 generic normal 与 kernel log](R1199-original-highest-packet-complete-generic-pairing-and-kernel-log.md)：原同一 $P$ 的全图配对、全部交叉项及三个 CM 支的严格消去。
- [R1200：规范 Igusa–Weil 相位及有理算子](R1200-original-canonical-Igusa-Weil-phase-and-rational-packet-pairing.md)：同一 $\nu$、参考权、有限 Picard–Fuchs 源、算子分母和次数、完整三次对称消去。
- 本文的 Rodrigues、quadrature 常数、端点和 Rankin–Cohen 微分恒等式均在正文逐式证明，不将数值探查用作证明。
- root 的原有限探查在 $p=59,71,83$ 给
$\Sigma=20,11,27$；它只作为先前失败路线的诊断，不是 (1201.32) 的依据。本文没有执行本地数学程序。

