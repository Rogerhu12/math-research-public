# 原 weight5 完整 toric Artin 基与三条惰性首层的共同相位

2026-11-27 / Astra-rank2-Sha-0b097461-20261127。

**已证明。** 本注使用 R1049§§13–14 的完整经典平方，
从原同一54图在固定 weight5 的实际值构造平方根。
三条原$\eta_j$的相位因此先在特征零同步，再同时约化。
结论适用于固定坏集外全部惰性$p$，不需要先限
$p\equiv2,5\bmod9$。原 Artin 基$a_{j,p}$仍原样保留。

所得是残余首层的完整三向量比较，不是全$p$精度的 canonical
等式，也不删原 type4 线性组合的外部项。

## 1. 固定 weight5 的真实54值

沿 R1049 固定
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
E=K(\zeta_{18})=\mathbf Q(\zeta_9),\qquad
\mathcal J=\{4,10,16\}.
$$
对整数$k\ge5$、$k\equiv5\bmod6$，令
$$
g_k(\tau)=\theta(\psi_{27}^{\,k-1})(\tau/3),
$$
并在原$A=E_{27}$、原 full9 基及同54个 degree34 商图上定义
$$
T_{j,k}
=\sum_{i=0}^2\sum_{t\in C_{18}}
 \omega^i\vartheta_{l_j}(t)^{-1}
 g_k(S_{b_{i,t}},\ell_{i,t},\omega_{b_{i,t}}/d_{i,t}).
\tag{1}
$$
这里$\varphi_{i,t}^{*}\omega_b=d_{i,t}\omega_A$，
所以实际权倍率为$d_{i,t}^{\,k}$。
这就是 R1049(88)的同一$\mathcal T^g$；
不作$1/54$或新的局部平均。

R1049§13.1–13.5的经典证明只使用$k\equiv5\bmod6$，
没有使用$k$为素数。
其中原$\Gamma$、右$D$值$i^k$、$Ph$分量、
2与17的实际 determinant、3处 Gauss 以及无穷平移均保持。
所以其(90)对这里全部$k$准确是
$$
T_{j,k}^{\,2}
=2\omega\,3^{k+1}34^2c_j\gamma_j\rho^{2k-1}
 \bigl((k-1)!\,d_{j,k-1}\bigr)^2,
\tag{2}
$$
其中
$$
d_{j,m}=[z^m]D_{j,1},\qquad
\gamma_j=L(\psi_{27}\eta_j,1)/\Omega,\qquad
\rho=\epsilon_0^{-1}2^{-1/3}.
$$
$\epsilon_0\in\mu_6$是原$\Omega$与原$\varpi_0$的固定单位，
不为本注改动原9级点。

现在只用**固定的$k=5$**，定义
$$
\boxed{\qquad B_j=\frac{17\delta}{9}\,T_{j,5}.\qquad}
\tag{3}
$$
$g_5$是一个固定特征零代数模形式，故$B_j$由固定实际 CM 图
的有限代数评价给出；(3)没有在一个大扩域里任取平方根。
原$[z^4]D_{j,1}=1$，而$c_j,\gamma_j\ne0$已经由
R806、R994/R1002证明。
所以(2)在$k=5$严格给$T_{j,5}\ne0$。

因为$\rho^9=\epsilon_0^{-3}/8$及$4!^2=576$，
直接相乘得到
$$
\boxed{\quad
B_j^2=-972\,\omega\,34^4
       \epsilon_0^{-3}c_j\gamma_j=\mathscr C_j .
\quad}
\tag{4}
$$
这正是 R1049(117)的固定常数，包含其符号和全部34倍率。

## 2. 平方根确在原 $\eta$ 几何线中

此处必须区分几何级点里的$\zeta_9$和外系数$\zeta_9$。
先在
$$
L_0\otimes_K E,\qquad L_0=K(E_{27}[306])
$$
中书写(1)，几何 Galois 只作用于第一个因子。
R1043(74)已经支付原 full9 的全部 determinant 和
Weil pairing 下降；(75)给严格规范图等式
$$
\gamma\varphi_{i,t}
 =\varphi_{i-r_\gamma,h_\gamma^{-1}t}.
\tag{5}
$$
它包含微分、源和靶模型，不留一个源的$\mu_6$自同构。
因此对定义于原$K$模型的任意$g_k$，
(5)同样逐项运输(1)的实际模形式值。
重新标号后准确有
$$
\gamma T_{j,k}=\eta_j(\gamma)T_{j,k},\qquad
\gamma B_j=\eta_j(\gamma)B_j .
\tag{6}
$$
权$k$没有给(6)另添一个$\epsilon(u)^k$：
该相位已经包含在(5)的严格级点和拉回微分中。
这里不是仅从一条 Hodge 标签推测 Galois 作用。

特别$T_{j,k},B_j$在几何$\operatorname{Gal}(L_0/H)$下固定，
故属于$H\otimes_K E$。
R806(12)给$H/K$在3不分歧；
$E/K$为在3全分歧的三次扩张，因而$H\cap E=K$。
所以$H\otimes_K E=HE$是一个域，且其到实际复数评价的乘法映射
在这一子域上为单射。
这一步解决了$E$本来亦包含于 full9 级点域的重合问题，
不把两个$\zeta_9$拷贝无声等同后再令几何 Galois 固定其中一个。

因$H/K$为 cyclic18且$E$包含角色值，
其$\eta_j$本征空间是一个$E$维数1的空间。
(3)、(6)说明$B_j$是其中的真实非零基。
于是
$$
\boxed{\qquad T_{j,k}/B_j\in E.\qquad}
\tag{7}
$$
同时$B_je_{\eta_j^{-1}}$是全有限 Artin 实现的一个固定 de Rham
基。原题已有的$a_{j,p}e_{\eta_j^{-1}}$仍不改变；
$B_j/a_{j,p}$只是明确记出的实际基变换。

令$\sigma$为$\operatorname{Gal}(E/K)$中
$\zeta_9\mapsto\zeta_9^4$的生成元，作用时固定几何$H$。
它把$j$按
$$
10\longmapsto4\longmapsto16\longmapsto10
\tag{8}
$$
循环：对$\zeta_{18}$的指数是13，
故$l=1,-5,7$恰按此顺序变化。
从(1)、(3)直接得到
$\sigma T_{j,k}=T_{\sigma j,k}$、$\sigma B_j=B_{\sigma j}$。
另一方面 R806(23)用原 CM13 projector 并按$z^4=1$唯一归一，
所以也严格有
$$
\sigma D_{j,1}=D_{\sigma j,1},\qquad
\sigma d_{j,m}=d_{\sigma j,m}.
\tag{9}
$$
没有给三条线分别加不同首项比例。

## 3. 在特征零先锁住共同号

定义一个完全明确的$K$中常数
$$
A_k=\frac{\delta}{34}\,
       3^{(k-5)/2}\,2^{-(k+1)/3}(k-1)! .
\tag{10}
$$
两个指数为整数。将(2)除以(4)，使用
$\rho^{2k-1}=\epsilon_0^{-3}2^{-(2k-1)/3}$，得到
$$
\frac{T_{j,k}^{\,2}}{B_j^2}
=-\frac{3^{k-4}}{34^2}
  2^{-2(k+1)/3}(k-1)!^2d_{j,k-1}^{\,2}
=A_k^2d_{j,k-1}^{\,2}.
\tag{11}
$$
因此，若某个$d_{j,k-1}\ne0$，则全部三条均非零，
并可在(7)的**特征零域$E$**中取实际比值
$$
r_{j,k}=\frac{T_{j,k}}{A_kB_jd_{j,k-1}}\in E,\qquad
r_{j,k}^2=1.
$$
所以$r_{j,k}$只能是$1$或$-1$。
由(8)–(9)，$\sigma r_{j,k}=r_{\sigma j,k}$；
而$1,-1$均被$\sigma$固定，故三个实际比值必相同。
若一条$d_{j,k-1}=0$，(9)使全部为零，(11)又使全部$T_{j,k}=0$，
此时任取一个共同号等式亦成立。
从而对每个合法$k$，存在一个共同
$\varepsilon_k\in\{1,-1\}$使
$$
\boxed{\qquad
T_{j,k}=\varepsilon_k A_k B_jd_{j,k-1}
\quad(j=4,10,16).
\qquad}
\tag{12}
$$
这不是逐$j$选择平方根。
在固定首权$k=5$，(3)、(10)给$A_5B_j=-T_{j,5}$，
所以准确有$\varepsilon_5=-1$。
本注不由此声称所有更高权的$\varepsilon_k$都相同。

由于(12)在特征零已经同步，后续即使
$E\otimes_KK_p$分裂成三个因子，也不能重新各选一个号。
因此本结论不需要$p\bmod9$的不可约性前提。

## 4. 原三条惰性端点的残余线性等式

现取 R1049 的好惰性$p$，并删去(3)这三个固定非零代数数的
有限零极支撑。原$a_{j,p}$保持为其已指定的单位基；
$[L:H]$也仍取实际值。
R1049(88)、(114)与 Newton 笔记的同源端点(116)给
$$
\begin{split}
\frac{\overline a_{j,p}\,\overline h_{j,p}}{[L:H]}
 &=-3\delta\,\overline\alpha_p\,\overline T_{j,p},\\
\overline\alpha_p&=-2^{(p+1)/3}\rho_p,\qquad
\overline d_{j,p-1}
 =34\,\overline{p c_{\sigma,p}}\,\overline K_{j,p}(0),\\
\overline{p c_{\sigma,p}}&=-\rho_p^{-1}.
\end{split}
\tag{13}
$$
把(12)代入第一行。
用$\delta^2=-3$、Wilson 的$(p-1)!\equiv-1$以及
Euler 判据$3^{(p-1)/2}\equiv(3/p)$，全部系数逐项化为
$$
\boxed{
\overline a_{j,p}\,\overline h_{j,p}
 =s_p[L:H]\,\overline B_j\,\overline K_{j,p}(0),
\qquad
s_p=-\varepsilon_p\left(\frac3p\right)\in\{1,-1\}.
}
\tag{14}
$$
同一个$s_p$同时作用于全部三个$j$。
例如在尚未用 Wilson 前，
$-3\delta\alpha_p A_p d_{j,p-1}/K_{j,p}(0)$
准确等于$3^{(p-1)/2}(p-1)!$；
这里两个负号分别来自(114)和$p c_{\sigma,p}=-\rho_p^{-1}$。
(14)平方后恰回 R1049(117)，可独立核回全部常数。

并未为使$a_{j,p}$互为系数共轭而重选原 Artin 基。
其兼容性在实际 raw 值上处理：
按定义，$a_{j,p}h_{j,p}$就是原 raw 读数；
模$p$它由(13)第一行的同一个$T_{j,p}$给出。
所以固定原基以后，(14)仍准确成立，基变换只出现在显示的
$B_j/a_{j,p}$中。

对任意一组三个原系数$r_{j,p}$，因此有
$$
\boxed{
\sum_j r_{j,p}\overline h_{j,p}
 =s_p[L:H]\sum_j
     r_{j,p}\frac{\overline B_j}{\overline a_{j,p}}\,
          \overline K_{j,p}(0).
}
\tag{15}
$$
这支付了同一完整三向量的首层线性比较；
无需假设各项非零，也不依赖系数行本身是否 Galois 不变。
原乘子$B_j/a_{j,p}$不能删去，更不能无证把右边改成
$\sum_jr_{j,p}\overline K_{j,p}(0)$。

## 5. 仍需付的原来源接口

(14)–(15)不能单独推出右侧任一完整线性组合非零。
三个端点分别为单位，也不排除一条给定系数行的抵消。
它们更没有把原 rank-two 曲线的中央假设自动转换成
三个$\overline h_{j,p}$各自为零。

本注也没有证明$\varepsilon_k$沿任一$p$进权支连续，
或把(12)的正整数权等式逐项延拓到$p$进负二点。
若要支付原 signed/Soulé 的全精度等式，仍须同一实际
theta/Heisenberg 来源的未平方生成函数比较，或另一条全源
互反律；不能从一个共同残余号跳过去。
R1049中把$h$解释成原固定循环 AJ 的全部$q_0$/整格前提仍保留。

本注没有新数学运行；固定$T_{j,5}$按(1)定义，其非零由已付完整
经典式证明，不存 CM 坐标表或另做数值近似。
依赖：[R1049](../results/R1049-original-inert-syntomic-graphs-and-crystalline-lattice.md)
§§12–14，
[R1043](../results/R1043-original-two-isogeny-level-transport-and-weighted-orbit-reduction.md)
§16，
[R806](../results/R806-original-type-four-order-eighteen-and-negative-two-katz.md)
§§1、2、4、5，
以及[原同源 Newton 笔记](2026-11-27-original-type-four-inert-negative-two-newton-and-signed-line.md)。
