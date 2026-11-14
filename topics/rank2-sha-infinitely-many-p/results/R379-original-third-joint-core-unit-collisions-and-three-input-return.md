# R379：原输出的第三联合 core、单位碰撞管及同一 S 的三输入正交返回

日期：2026-11-14。**状态：已证明。** 在一个明确固定的无穷普通素数族上，
R375 的同一个联合测度除了 $X,Z$ 两个 core，还具有保持正交辅助坐标的
完整原输出 $Y$-core。它准确计算两个原坐标都是单位而总输出深陷 $p^n$
的碰撞管；其全部 tame 行均返回原 $S$。另外，同一个 $S$ 可写成
$-A^2C_{18}/12$ 的三个真实有界输入，其三个正交坐标也有完整独立 core。
这些是实际联合测度式，包含原周期、全部半特征、质量和相加 carry。
原独立叶格仍有两个随输出移动的单位中心，本文没有把它们改成原点球。

## 1. 固定原模型、同一来源和无穷素数族

沿用
$$
E_{17}:y^2=x^3+b,\quad b=17,\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\gamma_{13}=4+\omega,
$$
$$
x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,\quad \sigma=z+\cdots,
\qquad dz=dx/(2y),\qquad \Theta=x\sigma^2.
$$
本文用 $X_{\rm ell}=x^3$ 表示椭圆函数的立方，避免与联合测度坐标混淆。
原目标和 R367 的两部分为
$$
A=\sigma(z)\sigma(2z)\sigma(\delta z),\qquad
B=\sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z),\qquad
S=-AB/84.
\tag{1}
$$
它们的真实 degree 为 $8,26,34$，型分别为 $3,3,0$，
$A=2\delta z^3+\cdots$、$B=14\delta z^3+\cdots$、$S=z^6+\cdots$。
$\mathcal E=\mathcal E_{56}$ 保持 R367 的原规范，质量一。

设原普通参数与周期为
$$
\pi=\psi_{17}(\mathfrak p),\quad \pi\bar\pi=p,\quad
\kappa=p/\bar\pi^2,\quad
\int e^{zt/\Omega}\,d\nu_G(t)=G(z).
\tag{2}
$$
$\Omega$ 是 R300、R316 的同一个普通单位周期，不另换曲线或微分。

为同时支付下文所有整个 theta 空间的中心，固定
$$
M=\operatorname{lcm}(24192,68,52)
 =2^7\cdot3^3\cdot7\cdot13\cdot17=5346432
$$
及集合
$$
\boxed{\mathcal P_*=\{p:\ p>17,\ p\equiv1\pmod3,\
              \psi_{17}(\mathfrak p)\equiv1\pmod{M\mathcal O_K}\}.}
\tag{3}
$$
取好素数即可。它包含 $K(E_{17}[M])$ 的全部好全分裂有理素数；
因此 Chebotarev 给一个固定无穷集合。这里用的是实际 Frobenius，
不是事后更换范数 $p$ 的生成元。

R290 的原规范使 $\pi_0=\varepsilon\pi$ 是 $E_1$ 的
$2\delta$-primary 生成元，其中 $\varepsilon\in\mu_6$。
(3) 蕴含 $\pi\equiv1\bmod2\delta$。$\mu_6$ 到
$(\mathcal O_K/2\delta)^\times$ 的映射是同构，故在本族上
$$
\boxed{\varepsilon=1,\qquad
\lambda_\sigma=\lambda_\Theta=\lambda_S=\lambda=1/\bar\pi.}
\tag{4}
$$
$\lambda$ 是单位，$v_p(\kappa)=1$。以下并不把 $\lambda^n$ 当作趋零项。

## 2. 整个来源空间的原绝对 core

记 $\mathcal S_N=\sigma^N L(NO)$。使用 R300 的真实 pull/trace 和
完整对称 Heisenberg lift：当 $\pi/\bar\pi\equiv1\bmod2N$ 时，
对应算子与整个 Heisenberg 群（包括中心）交换。
primitive 交换子给该 $N$ 维表示不可约，所以算子在整个
$\mathcal S_N$ 上为标量。标量仍须由同 degree 的真实来源锚定。

本篇所需锚如下；所有尺度均在当前 $p$ 处为单位。

| $N$ | 同 degree 的真实锚 | 已付原 core |
|---|---|---|
| $8$ | $\Theta(2z)$ | $\lambda$ |
| $16$ | $\sigma(4z)$ | $\lambda$ |
| $18$ | $\Theta(3z)$ | $\lambda$ |
| $26$ | $\Theta(\gamma_{13}z)$ | $\lambda$ |
| $34$ | 原 $S$ | $\lambda$ |
| $56$ | $\Theta(2\gamma z)$ | $\lambda$ |
| $64$ | $\sigma(8z)$ | $\lambda$ |
| $448$ | $\sigma(8\gamma z)$ | $\lambda$ |
| $1728$ | $\sigma(24\delta z)$ | $\lambda$ |

例如 $26=2N(\gamma_{13})$、$56=2N(2\gamma)$。
$\Theta$ 的缩放 core 来自 R316 的同一有界测度；没有把它的加法卷积
当成乘法 Mellin。$S$ 的锚来自 R300 的原完整 $p$-core，
虽然其质量零，但它是非零截面，足以确定整个空间的标量。
$2N$ 对本表全部 $N$ 都整除 $M$。所以
$$
\boxed{\nu_G|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_G
       \quad(G\in\mathcal S_N,\ N\text{ 在上表中}).}
\tag{5}
$$
这里对任意实际有界 $G$ 及全部 tame 成立，不只是型零线或一个首矩。

积分格也没有被略过。原
$\sigma^N,\sigma^Nx^i,\sigma^Nyx^j$ 的允许基有互异首阶和单位首系数；
以原整 Amice 展开按首阶消元，得到同一个整 theta 格。
后文的联合系数可先用未除以阶乘的辅助矩
$\int v^m\,d\nu$，它们是整有界测试。每个这样的输出截面都属于
上述原整格，再用 (5)，最后由全部多变量矩的唯一性得到联合测度式。
因此没有将“任意平移截面在复数上有相同 degree”冒充整性。

## 3. R375 同一个联合的第三方向

保持 R375 的实际输入 $y,r,s$：
$$
d\mu=-\frac1{84}d\nu_A(y)d\nu_{\mathcal E}(r)d\nu_B(s),\qquad Y=y+s.
$$
令
$$
W=\frac{7y+r}{8},\qquad Z=s+\frac{y-r}{8},\qquad Y=Z+W.
\tag{6}
$$
$\rho=(Z,W)_*\mu$；这里 $W=X/8$，只是将 R375 的 $X$ 除以单位八。
其整个变换是
$$
-\frac1{84}A(z/8+7w/8)\mathcal E(w/8-z/8)B(z).
$$
R375 已完整支付两个 core：
$$
\rho|_{Z\in p}=\lambda[\kappa,\mathrm{id}]_*\rho,\qquad
\rho|_{W\in p}=\lambda[\mathrm{id},\kappa]_*\rho.
\tag{7}
$$

新的正交坐标为
$$
\boxed{Y=Z+W,\qquad V=7Z-27W.}
\tag{8}
$$
行列式 $-34$ 是当前单位，且
$$
Z=(27Y+V)/34,\qquad W=(7Y-V)/34.
\tag{9}
$$
写 $\widetilde\rho=(Y,V)_*\rho$。它的原整个变换准确为
$$
\boxed{
-\frac1{84}A(z-91w/4)\mathcal E(-17w/4)B(z+7w).
}
\tag{10}
$$
这是保持原周期的代数换坐标，没有另添 Gaussian。

对原周期 $\lambda_0$，(10) 的 $z$ 平移自动因子中，
$A$ 和 $B$ 的交叉项分别是
$8(-91/4)\eta_{\lambda_0}w=-182\eta_{\lambda_0}w$、
$26\cdot7\eta_{\lambda_0}w=182\eta_{\lambda_0}w$，准确抵消。
剩余为原 degree 三十四的
$34\eta_{\lambda_0}(z+\lambda_0/2)$。
$A=-2\delta\sigma^8xy$、$B\in\sigma^{26}L(26O)$，
而 $\mathcal E$ 与 $z$ 无关，因而半特征也是原偶 degree 的特征。
每个辅助矩截面遂在**同一个整个** $\mathcal S_{34}$ 中。
第2节的整格和中心已付；逐矩用 (5)，得到
$$
\boxed{\widetilde\rho|_{Y\in p}
       =\lambda[\kappa,\mathrm{id}]_*\widetilde\rho.}
\tag{11}
$$
它保持 $V$，不只是 $Y$ 边际的原 $S$-core。

还有一个不用猜测新 degree 标量的互补方向。
(7) 给全原点格
$\rho|_{p^2}=\lambda^2[\kappa,\kappa]_*\rho$；
(8) 是整可逆变换，故同式适用于 $(Y,V)$。
将 (11) 再限制 $V\in p$，并取消注入推前
$[\kappa,\mathrm{id}]_*$，得到
$$
\boxed{\widetilde\rho|_{V\in p}
       =\lambda[\mathrm{id},\kappa]_*\widetilde\rho.}
\tag{12}
$$
这证明了两个全联合方向，未给 $V$ 方向另造一个未锚定的 theta 常数。
特别对任意 $m,n\ge0$，
$$
\boxed{\widetilde\rho|_{\{Y\in p^m,V\in p^n\}}
       =\lambda^{m+n}[\kappa^m,\kappa^n]_*\widetilde\rho.}
\tag{13}
$$

## 4. 两个单位坐标的真实输出碰撞管

对 $n\ge1$，定义同一联合中的
$$
\mathcal C_n=\{Z,W\in\mathbf Z_p^\times,\ Y=Z+W\in p^n\}.
$$
由 (9)，当 $Y\in p$ 时，$Z,W$ 为单位当且仅当 $V$ 为单位；
$27,7,34$ 均为当前单位。由 (11)–(12)，
$$
\boxed{
Y_*(1_{\mathcal C_n}\rho)
=\lambda^n(1-\lambda)[\kappa^n]_*\nu_S.
}
\tag{14}
$$
这是一条完整推前式，包含进一步深陷的所有输出。
若改取精确环带 $v_p(Y)=n$，右边准确改为
$\lambda^n(1-\lambda)[\kappa^n]_*\nu_S^\times$。

更一般地，在同一交域中另限制 $v_p(V)=m$，可直接由 (13)
得到完整深度与环带公式；没有用点数替代测度。
本篇最有用的是 (14) 所控制的**两者皆单位**相加碰撞，
而不是再把一个全空间 core 改名。

### 4.1 原六 sigma 的相位接口

(6) 的 $\mu$ 来自 R367 的原 $R$ 投影，而非未经投影的六输入。
在原六输入中写
$$
y=X_1+2X_2+\delta X_3,\quad
r=2X_2+\delta X_3-7X_1,\quad
s=2\delta X_4+\gamma X_5+\bar\gamma X_6,\quad Y=y+s,
$$
$$
d\eta_6=-d\nu_\sigma^{\otimes6}/84.
$$
对 $\xi\in\mu_6$ 置
$$
W_\xi=(7y+\xi r)/8,\quad Z_\xi=Y-W_\xi,\quad
V_\xi=7s-91y/4-17\xi r/4.
\tag{15}
$$
则 (14) 在原输入上准确表示为
$$
\boxed{
\frac16\sum_{\xi\in\mu_6}
Y_*\!\left(
 1_{\{Y\in p^n,\ 7y+\xi r\ {\rm unit}\}}\eta_6
\right)
=\lambda^n(1-\lambda)[\kappa^n]_*\nu_S.
}
\tag{16}
$$
相位 $\xi=1$ 时
$$
V_1=7X_1-54X_2-27\delta X_3
       +14\delta X_4+7\gamma X_5+7\bar\gamma X_6.
$$
全部六支的权和必须保留；(16) 是平均，不声称这些域互不相交，
也不把其中单支赋予一个未经证明的中央零。

### 4.2 全 tame、尺度质量与单位因子

记 $d=p-1$，
$$
J_{S,\ell}(u)=\int_{\mathbf Z_p^\times}
 \omega_p(t)^\ell\langle t\rangle^{du}\,d\nu_S(t),\qquad
U_{n,\ell}(u)=
 \omega_p(\bar\pi)^{-2n\ell}
 \langle\bar\pi\rangle^{-2ndu}.
$$
将 (14) 的第 $n$ 环带输出除以 $p^n$，得到准确整条式
$$
\boxed{J_{\mathcal C_n,\ell}^{[n]}(u)
       =\lambda^n(1-\lambda)U_{n,\ell}(u)J_{S,\ell}(u).}
\tag{17}
$$
导数右边保留
$$
\lambda^n(1-\lambda)U_{n,\ell}(0)
 [J'_{S,\ell}(0)-2nd\log_p(\bar\pi)J_{S,\ell}(0)].
\tag{18}
$$
principal 分支 $J_{S,0}(0)=0$ 已由原 core 支付；
因此原 $J'_S(0)=0$ 确实传播到 (16) 的全部这些规范化碰撞管。
这不是一条只在裸 source 或第一个矩上的零传播。

本族上 $1-\lambda$ 和 $1+\lambda$ 都是单位。
若其中一个非单位，则 $\mathfrak p$ 整除 $\bar\pi\mp1$；
正整数范数 $p+1\mp a_p$ 在 $p>7$ 时严格位于 $0$ 和 $2p$ 之间，
故被 $p$ 整除只能给 $a_p=\pm1$。
但 (3) 使 $E_{17}[2]$ 全部在 $\mathbf F_p$ 上有理，所以 $a_p$ 偶，
矛盾。这同时证明 $1-\lambda^2$ 为单位。
故 (17) 在 principal 中央的比例没有损失额外的 $p$ 深度。

## 5. 同一来源族的完整 Möbius 返回及余域

R375 的原族是
$$
\nu_{T_\xi}=(Z+\xi W)_*\rho,\qquad T_1=S.
$$
在 $(Z,W)$ 中，(11) 的实际线性映射为
$$
\boxed{
M_Y=\frac1{34}
\begin{pmatrix}
27\kappa+7&27(\kappa-1)\\
7(\kappa-1)&7\kappa+27
\end{pmatrix},\qquad \det M_Y=\kappa.
}
\tag{19}
$$
它保持 $V$、将 $Y$ 乘 $\kappa$，其像恰是 $Y\in p$。
因此对任意当前有界系数 $\xi$，
$$
\boxed{
(Z+\xi W)_*(1_{Y\in p}\rho)
=\lambda\{a_\xi Z+b_\xi W\}_*\rho,
}
\tag{20}
$$
$$
a_\xi=\frac{27\kappa+7+7(\kappa-1)\xi}{34},\qquad
b_\xi=\frac{27(\kappa-1)+(7\kappa+27)\xi}{34}.
$$
若 $a_\xi\ne0$，其形式斜率为
$$
f(\xi)=\frac{27(\kappa-1)+(7\kappa+27)\xi}
 {27\kappa+7+7(\kappa-1)\xi}.
\tag{21}
$$
本文始终以 (20) 为完整式；不能在 $a_\xi$ 非单位时直接删掉尺度、
跨出有界图表或改写单位输出条件。

例如 $\xi=1+\kappa u$ 时，原 $Z+\xi W$ 为单位当且仅当 $Y$ 为单位。
此时
$$
a_\xi=\kappa\left[1+\frac7{34}(\kappa-1)u\right],\qquad
b_\xi=\kappa\left[1+\frac{7\kappa+27}{34}u\right].
\tag{22}
$$
括号之差是 $u$，不可能同时非单位。
若第一个非单位，须用 $W+\eta Z$ 的另一张图表；
不是将其误当作一个无额外 carry 的 $T_{f(\xi)}$。
$\xi=1$ 确实固定，给原 $S$-core。

此外，对原 $Y$-unit 域，(7) 精确给
$$
\begin{aligned}
\int_{Y\ {\rm unit}}\varphi(Y)\,d\rho
={}&\lambda\int_{Z\ {\rm unit}}\varphi(Z+\kappa W)\,d\rho\\
&+\lambda\int_{W\ {\rm unit}}\varphi(\kappa Z+W)\,d\rho\\
&+\int_{\{Z,W,Y\ {\rm unit}\}}\varphi(Y)\,d\rho .
\end{aligned}
\tag{23}
$$
两个深坐标域不交；第三项是完整共同单位余域。
(14) 支付的是其旁边 $Y$ 深的真实碰撞管，未自动支付 (23) 的第三项。
所以第三 core 使一类实际 unit 碰撞零可传播，却没有把
$\xi=1$ 的中央零免费带到 R375 的整个深参数盘。
所有原 unit-domain 边界仍清楚可见。

## 6. 一个固定、原本就等于 S 的三输入模型

原 division 身份给
$$
A=-2\delta\sigma^8xy,
$$
$$
B=-14\delta\sigma^{26}xy
 (X_{\rm ell}-8b)
 (X_{\rm ell}^2-4bX_{\rm ell}/7+16b^2/7).
$$
因此定义
$$
\boxed{
C_{18}=\sigma^{18}
 (X_{\rm ell}-8b)
 (X_{\rm ell}^2-4bX_{\rm ell}/7+16b^2/7)
}
\tag{24}
$$
后，准确有
$$
\boxed{B=7AC_{18},\qquad S=-A^2C_{18}/12,\qquad C_{18}(0)=1.}
\tag{25}
$$
这里没有把比值留下为一个未知 Mellin 商。
$C_{18}$ 的真实有界原测度可直接由正幂多项式给出：
$$
C_{18}=\Theta^9-\frac{60b}{7}\sigma^6\Theta^6
 +\frac{48b^2}{7}\sigma^{12}\Theta^3
 -\frac{128b^3}{7}\sigma^{18}.
\tag{26}
$$
所以其整性、同一周期和加法卷积全部明确。
第2节的 $\Theta(3z)$ 锚付清
$\nu_{C_{18}}|_p=\lambda[\kappa]_*\nu_{C_{18}}$。
这是本固定无穷素数族上的整个空间身份；
不声称 $C_{18}$ 单独是一条全球 CM Hecke 特征线。

$C_{18}=B/(7A)$ 是全纯截面，故其零除子为
$\operatorname{div}_0(B)-\operatorname{div}_0(A)$，全部支撑仍在固定
二、三、七挠点。R376 的原整小球公式遂适用：
$$
\boxed{
\nu_{C_{18}}(c+p^n)\text{ 对所有 }c,n\text{ 都是单位；}
}
\tag{27}
$$
$A,B$ 的全部非原点小球也都是单位，而原点小球质量零。
这个结论使用实际 core、全纯除子和原 division 常数，未仅由复零点作推断。

现在令
$$
d\eta_3=-\frac1{12}d\nu_A(a)d\nu_A(b_1)d\nu_{C_{18}}(c_1),
\qquad Y=a+b_1+c_1.
\tag{28}
$$
它是同一个 $\nu_S$ 的准确三输入表示。
全输入 $p$ 部分的系数是 $\lambda^3$，整体输出的 core 仍是 $\lambda$。
设 $\mathcal P$ 表示至少一个输入为单位；对 $n\ge1$，
$$
\boxed{
Y_*(1_{\mathcal P,\ Y\in p^n}\eta_3)
 =\lambda^n(1-\lambda^2)[\kappa^n]_*\nu_S.
}
\tag{29}
$$
证明是从完整输出深管减去全输入 $p$：
后者准确为 $\lambda^3\lambda^{n-1}[\kappa^n]_*\nu_S$。
这保留了所有 unit 输入组合，不将“至少一输入单位”
误拆成恰一输入单位。
(29) 的全 tame 与质量导数与 (17)–(18) 相同，
只将 $1-\lambda$ 换成已证单位 $1-\lambda^2$。

## 7. 三输入模型的三个真实正交 core

在 (28) 中引入
$$
\boxed{
Y=a+b_1+c_1,\qquad Q=a-b_1,\qquad R=9(a+b_1)-8c_1.
}
\tag{30}
$$
变换行列式为 $34$，相应 theta Gram 为
$$
\boxed{\operatorname{diag}(34,16,2448).}
\tag{31}
$$
完整整个变换为
$$
-\frac1{12}A(z+u+9v)A(z-u+9v)C_{18}(z-8v).
\tag{32}
$$
交叉项分别是 $8-8=0$、$72+72-144=0$、$72-72=0$。
所以原 $Y$ 方向处于整个 $\mathcal S_{34}$，$Q$ 方向处于整个
$\mathcal S_{16}$，中心和整格均由第2节付清。
若 $\eta=(Y,Q,R)_*\eta_3$，得到两个全联合 core
$$
\eta|_{Y\in p}=\lambda[\kappa,1,1]_*\eta,\qquad
\eta|_{Q\in p}=\lambda[1,\kappa,1]_*\eta .
$$
全部三个原输入都有 core $\lambda$，而 (30) 整可逆，
故全原点格的 core 是 $\lambda^3[\kappa,\kappa,\kappa]_*$。
再限制前两坐标并取消注入推前，准确推出第三条
$$
\boxed{\eta|_{R\in p}=\lambda[1,1,\kappa]_*\eta.}
\tag{33}
$$
这没有给 degree $2448$ 猜一个单变量锚。

于是对任意独立 $m,n\ge0$，
$$
\boxed{
Y_*(1_{\{Q\in p^m,R\in p^n\}}\eta)
 =\lambda^{m+n}\nu_S.
}
\tag{34}
$$
任一辅助深球改成精确环带，就另乘 $1-\lambda$。
所以当原 $J'_S(0)=0$ 时，(34) 的整个二维辅助深度网格、
及其任意深球/环带组合，确有同一原中央零。
这里保持原 $Y$，没有为了归一辅助深度而缩放原总输出。

原三个输入的单一单位叶则不同。由 (30)
$$
a=\frac{8Y+R+17Q}{34},\quad
b_1=\frac{8Y+R-17Q}{34},\quad
c_1=\frac{9Y-R}{17}.
\tag{35}
$$
因此公共深度 $N\ge1$ 下
$$
\boxed{
\{a\ {\rm unit},\,b_1,c_1\in p^N\}
=
\{Y\ {\rm unit},\,Q-Y\in p^N,\,R-9Y\in p^N\}.
}
\tag{36}
$$
右边是两个随输出移动的**单位中心**。
它不是 (34) 的原点辅助网格。两个深度不同时，准确条件仍是
$8Y+R-17Q\in34p^m$、$9Y-R\in17p^n$，必须一同保留。
本篇没有把 (34) 的零性搬到 (36)。

## 8. 同一三输入叶的完整中央尾

为使最后的差别可直接计算，保留 (28) 并取
$a$ unit、$b_1\in p^m$、$c_1\in p^n$，$m,n\ge1$。
其输出自动为单位。
写
$$
M_r(A)=\int x^r\,d\nu_A,\quad
M_s(C_{18})=\int x^s\,d\nu_{C_{18}},\quad
I_{-k}(A)=\int_{\mathbf Z_p^\times}x^{-k}\,d\nu_A .
$$
$\mu_6$ 型给 $M_r(A)=0$ 除非 $r\equiv3\bmod6$，
$M_s(C_{18})=0$ 除非 $s\equiv0\bmod6$，且
$$M_3(A)=12\delta\Omega^3,\qquad M_0(C_{18})=1.$$
直接展开原 $\log(a+\kappa^mb_1+\kappa^nc_1)$，得到
$$
\boxed{
J'_{\mathrm{leaf},m,n}(0)
=-\frac{d\,\lambda^{m+n}}{12}
 \sum_{\substack{r\ge3,\ r\equiv3(6)\\s\ge0,\ s\equiv0(6)}}
 \frac1{r+s}\binom{r+s}{r}
 \kappa^{mr+ns}M_r(A)M_s(C_{18})I_{-(r+s)}(A).
}
\tag{37}
$$
原 log 常数项被深 $A$ 的零质量杀掉；保留的指数 $r+s$ 为奇数，
所以此式的 log 展开符号准确为正，外面仍有原 $-1/12$。
第 $(r,s)$ 项赋值至少 $mr+ns-v_p(r+s)$，
故所有尾都收敛，没有交换一个未经控制的 Mellin 乘积。
首项是
$$
-\frac{d\delta\Omega^3}{3}\lambda^{m+n}\kappa^{3m}I_{-3}(A).
\tag{38}
$$
这里并未预设固定 $I_{-3}(A)$ 非零。

全 tame 式同样直接保留：将 (37) 的
$d(r+s)^{-1}\binom{r+s}{r}I_{-(r+s)}(A)$
换成
$$
\binom{du}{r+s}\binom{r+s}{r}
 \int_{\mathbf Z_p^\times}
 \omega_p(a)^\ell\langle a\rangle^{du}a^{-(r+s)}\,d\nu_A(a).
$$
整体仍乘 $-\lambda^{m+n}/12$ 和对应矩与尺度。
这给整个叶 Mellin；在 $u=0$ 全部 tame 质量均为零，
因为所有保留项 $r+s>0$。
所以 (37) 的原中央导数并非遗漏尺度质量后的形式值。

## 9. 本篇取得的实际控制

(11)–(18) 给 R375 同一联合上的新第三方向、互补方向及完整 unit 碰撞管，
并将它们以正确的六相位平均接回原六 sigma 输入。
(24)–(34) 进一步在同一个固定来源上提供一个较小的三输入模型，
其两个独立辅助深度可真实传播原中央零。
两套结果都包含所有输出 carry、tame 和原点质量，系数在所选固定无穷族上为单位。

仍需支付的是 (23) 的共同单位余域，或 (36) 的两个移动单位中心；
(37) 已把后一行保留为同一实际来源的完整收敛负矩表达。
不能只由原点辅助网格、逐球单位或 Möbius 的形式斜率删除这些条件。
固定曲线的无穷素数主目标没有在本篇被提前宣告完成。

## 依赖与同步

- [R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)：原完整 trace、整格和 $S$ 的 core。
- [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)：原 sigma、Theta、周期和尺度 core。
- [R367](R367-original-degree-seven-fifty-six-joint-and-translated-leaf-balls.md)：原 $A,\mathcal E,B$ 联合、相位和原输入接口。
- [R375](R375-original-tilted-jacobi-double-core-and-central-return.md)：同一 $X,Z$ 联合及完整倾斜来源族。
- [R376](R376-original-additive-ball-theta-group-formula-and-integral-torsion-values.md)：原整 theta 群小球公式及固定挠除子单位判据。

终端失联期间，通过仓库规则许可的小文本 GitHub 接口提交本证明；
API 同步不冒称为一次 git pull。根代理负责 core、HANDOFF 与结果登记。
