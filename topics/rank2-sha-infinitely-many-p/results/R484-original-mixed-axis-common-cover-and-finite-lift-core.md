# R484 — 旧混合 W 轴在新增伴随 lift 上的真实固定覆盖与有限核心轨道

日期：2026-11-14。**状态：已证明。** R476、R480 的新增
degree612 伴随 lift 可以与旧混合 $W_t$ 轴的实际 ordinary core
放进同一个固定全 theta 空间。本篇给出最小整行放大 $510$、
全部极化与半特征、一条仍无限的固定 ray 细分、含中心比值
及绝对核心的 $4080$ 次返回。新增 $V$ 保持不动，两个有标签的
companion-only 投影分别与这个核心交换。

这里得到的是新 lift 的真实有限轨道。它不自动等于 R465
未投影六输入的原两态轨道，也不把旧混管投影后直接当作新的
完整中央零。主目标未完成。

## 1. 固定原坐标及需要兼容的真实 lift

沿用 R465 的
$$
A=t_1+t_2+t_3+t_4,\qquad
Y_s=A+c+2d,
$$
$$
W_t=A+3\delta c+4d,\qquad
Q_t=3\delta A+29c,\qquad
U_t=A+3\delta c-14d.
\tag{1}
$$
旧固定覆盖的前三个物理输出是
$$
Y=2(A+c+2d),\qquad Z=2(A-29c),\qquad U=2(A+c-15d).
\tag{2}
$$
其余三个 $R_1,R_2,R_3$ 保 R465 定义。

R476 给同一原第二态的实际整投影
$$
D_-\Pi_0\,\widehat\rho_1
=H_{\rm ref}(Y)\Lambda_{\rm ref}(\mathbf Z)
 +\sum_{j=0}^6N_7^jW_*(Y)\Lambda_j(\mathbf Z),
\tag{3}
$$
其中 $\mathbf Z=(Z,U,R_1,R_2,R_3)$，每条 $\Lambda_j$ 都是
自己的完整五变量来源。R480(35) 用两个有标签的实际态
$\Phi_i(Y,V)$，将第 $j$ 项换成
$$
-\frac{111}{280}\sum_{i=1}^2
 \chi_i^jN_{\bar\gamma_7,V}^{\,j}\Phi_i^0(Y,V)\,
 \Lambda_j(\mathbf Z).
\tag{4}
$$
参考项乘 R477 的质量一
$\overline\Lambda_{612}(V)$。记所得整个 lift 为 $\Sigma$。
忘掉 $V$，逐项返回 (3)。

因此 $\Sigma$ 是同一个标准整张量中的实际来源：
$$
\boxed{
\mathfrak H_L=
\mathcal S_{136}\otimes\mathcal S_{3480}\otimes
\mathcal S_{1020}\otimes\mathcal S_{60}\otimes
\mathcal S_{2310}\otimes\mathcal S_{4466}\otimes
\mathcal S_{612}.
}
\tag{5}
$$
次序为 $(Y,Z,U,R_1,R_2,R_3,V)$。
R476 的基逆分母素因子均不超过 $61$，当前 ray 的 $p\ge71$；
R480 的全部有限 CM 迹同样为原整算子，所以 (5) 保全来源整性。
这一陈述没有将 $\Sigma$ 与原未投影的 $\rho_1$ 混同。

## 2. 旧混合轴的完整整覆盖

在 $(A,c,d)$ 上，(2) 和 (1) 的矩阵分别为
$$
L_3=\begin{pmatrix}2&2&4\\2&-58&0\\2&2&-30\end{pmatrix},\qquad
M_3=\begin{pmatrix}1&3\delta&4\\3\delta&29&0\\1&3\delta&-14\end{pmatrix}.
$$
从 $(Y,Z,U)$ 到 $(W_t,Q_t,U_t)$ 的准确矩阵为
$$
\boxed{
C=M_3L_3^{-1}
=\begin{pmatrix}
(37+3\delta)/68&(1-3\delta)/60&(-31+3\delta)/510\\
(29+87\delta)/68&(-29+3\delta)/60&(29+87\delta)/510\\
(1+3\delta)/68&(1-3\delta)/60&(239+3\delta)/510
\end{pmatrix}.
}
\tag{6}
$$
令 $\mathcal O_K=\mathbf Z[\omega]$、$\delta=1+2\omega$。
每一行的最小正整数清分母都为 $510$。所以取
$$
B=510C\in M_3(\mathcal O_K),\qquad
\det B=-32772600.
\tag{7}
$$
这只放大前三个新输出；三个 $R$ 和新增 $V$ 不变。
其固定素因子在 $2,3,5,7,17$ 中，因此当前普通处 $B$ 是
$\mathbf Z_p^3$ 的整自同构。

完整 Hermitian 极化为
$$
C\,\operatorname{diag}(136,3480,1020)\,\bar C^{\,t}
=\operatorname{diag}(72,1624,252).
\tag{8}
$$
定义
$$
\widehat W=510W_t,\qquad
\widehat Q=510Q_t,\qquad
\widehat U=510U_t.
$$
在生成变量中沿 (7) 的转置拉回，整个 lift 因而属于固定空间
$$
\boxed{
\mathfrak H_{\widehat M}=
\mathcal S_{18727200}\otimes\mathcal S_{422402400}\otimes
\mathcal S_{65545200}\otimes\mathcal S_{60}\otimes
\mathcal S_{2310}\otimes\mathcal S_{4466}\otimes
\mathcal S_{612}.
}
\tag{9}
$$
显示的大次数分别是 $72\cdot510^2$、
$1624\cdot510^2$、$252\cdot510^2$。
全部交叉项为零，特别新增 $V$ 与旧三轴及三个 $R$ 都正交。

(5) 的各次数均偶；(7) 的系数为真正 CM 整数。原对称
sigma 半特征经整数 CM 拉回后，各偶次因子仍为标准半特征，
(8) 又消掉所有 Gaussian 交叉项。因此 (9) 是原标准张量，
不是只按次数推测出的未注明 twist。

在此处放大是必要的说明：一般的 (5) 来源不必沿有理矩阵
$C$ 直接下降到原 $(72,1624,252)$ 格。
(9) 支付了整个新 lift，而不是把原六 sigma 那个特例的下降
免费套到任意 $N_7^jW_*$ 或其伴随上。

## 3. 保旧条件的一条固定无限 ray 细分

R454 的旧实际 Frobenius 类为
$$
\pi_0\equiv a_0+b_0\omega\pmod{m_0},\qquad
(a_0,b_0)=(1428552127,2161889730),\quad m_0=2793510720.
$$
仅提高已有 $3,5,17$ 因子的幂次，取
$$
\boxed{
\pi_0\equiv1428552127+2161889730\omega
       \pmod{712345233600}.
}
\tag{10}
$$
新模数是 $255m_0$，包含
$$
2N=37454400=2^6\,3^4\,5^2\,17^2,\qquad N=18727200.
$$
代表元的范数与新模数互素，证书直接核定。
新类约化正是旧类，保留原 CM conductor 规范、
$p\equiv7\bmod64$、三条曲线的 Euler 条件及所有已有核心。
与 R454 相同的 CM ray-class 素理想定理给这个固定单位类
无穷多个 degree-one 素理想；每个有理素数只产生有限个，
故 (10) 仍含无穷多个不同普通 $p$。

在含中心模数 $2N$ 上直接计算得到
$$
\boxed{
g=\pi_0/\bar\pi_0
\equiv37353691+29063880\omega\pmod{37454400}.
}
\tag{11}
$$
各局部精确阶为

| 模数 | $g$ 的两坐标 | 阶 |
|---|---:|---:|
| $64$ | $(27,8)$ | $16$ |
| $81$ | $(55,27)$ | $3$ |
| $25$ | $(16,5)$ | $5$ |
| $289$ | $(152,17)$ | $34$ |

所以 $g$ 在完整模数中的阶为 $4080$。
本篇只需据此得到核心的 $4080$ 次返回，不宣称这是每个
来源实际轨道的最小周期。

## 4. 整个大次数核心的固定绝对定标

R413 对任意当前 prime-to-$p$ 偶 degree 的完整 division trace
给
$$
\nu_G|_{p\mathbf Z_p}
=\lambda[\kappa]_*\nu_{K_{N,p}G},\qquad
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2.
\tag{12}
$$
此处使用整个 $\mathcal S_N$，包括全部奇偶部分。
其完整含中心 Heisenberg 交织由 (11) 决定。

为使固定算子完全具体，可在原 Schrödinger 基中写
$$
Xe_j=\zeta_N^je_j,\qquad Ze_j=e_{j+1},\qquad
Q_s e_j=\zeta_{2N}^{sj^2}e_j.
$$
把 (11) 的整数代表记为 $a+b\omega$。$a$ 在模 $2N$ 中
可逆，令 $c=ba^{-1}$。其 symplectic 矩阵的完整分解为
$$
\begin{pmatrix}a&-b\\b&a-b\end{pmatrix}
=
\begin{pmatrix}1&0\\c&1\end{pmatrix}
\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}
\begin{pmatrix}1&-c\\0&1\end{pmatrix}\pmod{2N}.
\tag{13}
$$
令 $\mathcal Fe_j=N^{-1/2}\sum_k\zeta_N^{jk}e_k$，
$D_a e_j=e_{a^{-1}j}$。于是
$$
\Gamma_g=\mathcal FQ_{-c}\mathcal F^{-1}D_aQ_{-c}
\tag{14}
$$
实现 (11) 的整个对称 Heisenberg 自同构，包括中心。
(13) 和各有限生成元的共轭直接验证 (14)，不必生成一个
一千八百余万维的稠密矩阵。

绝对标量使用原真实锚
$$
A_*(z)=\Theta(3060z)\in\mathcal S_N,\qquad
N=2\cdot3060^2,\qquad A_*(0)=1.
\tag{15}
$$
尺度 $3060$ 在当前普通处为单位；R316 的原 Theta core 是
$\beta=-\lambda$。因此实际 $K_{N,p}A_*=-A_*$。
由完整 Heisenberg 不可约性，(14) 与 $K_{N,p}$ 相差标量，
$\Gamma_gA_*=\rho_gA_*$，其中固定非零数
$\rho_g=(\Gamma_gA_*)(0)$ 的规范由 (14)、(15) 完全指定。
故
$$
\boxed{K_N=-\rho_g^{-1}\Gamma_g,\qquad K_NA_*=-A_*}
\tag{16}
$$
就是同一 ray 上每一个 $K_{N,p}$。这里没有一个待猜的正负号：
整个有限 Gauss 算子及质量一锚固定了绝对比例。

因为 $g^{4080}\equiv1\bmod2N$，$K_N^{4080}$ 与全部
Heisenberg 生成元交换，必为标量；(15) 给该标量为
$(-1)^{4080}=1$。所以
$$
\boxed{K_N^{4080}=I\quad\text{在整个 }\mathcal S_N\text{ 上成立}.}
\tag{17}
$$
整性来自原完整 division trace (12) 和 R413 的整 theta 格；
(17) 还给整逆算子。没有引用某条尚未知中央导数来定标。

## 5. 新 lift 的实际有限轨道，而非预设原两态返回

记 $\mathcal B=\operatorname{diag}(B,I_4)$ 为从 (5) 的物理
七输出到 (9) 的整坐标变换。令
$\widehat\Sigma=\mathcal B_*\Sigma$，并在 (9) 中定义
$$
\widehat\Sigma_r=(K_N^r\otimes I^{\otimes6})\widehat\Sigma,
\qquad
\Sigma_r=\mathcal B^{-1}_*\nu_{\widehat\Sigma_r},
\qquad r\in\mathbf Z/4080\mathbf Z.
\tag{18}
$$
$K_N$ 不必保持 (5) 拉回到 (9) 的那个较小像。
所以一般 $\Sigma_r$ 可能只在本篇支付的固定覆盖上是 theta
来源，不能先声称它仍在原 $L$ 周期格中。
它们却都是同一原物理 $\mathbf Z_p^7$ 上的整有界测度，
同一个有限固定覆盖及 (17) 使全部状态闭合。

旧混合轴在 $(Y,Z,U)$ 上的行记为
$$
c_W=\left(\frac{37+3\delta}{68},
          \frac{1-3\delta}{60},
          \frac{-31+3\delta}{510}\right).
$$
对应的正交列准确为
$$
r_W=\frac1{36}
  \begin{pmatrix}37-3\delta\\29(1+3\delta)\\-31-3\delta\end{pmatrix},
\qquad c_Wr_W=1.
\tag{19}
$$
在前三坐标定义
$$
A_W=I+(\kappa-1)r_Wc_W,
\tag{20}
$$
并在三个 $R$ 与新增 $V$ 上取恒等。
它将旧 $W_t$ 乘 $\kappa$，逐个固定
$Q_t,U_t,R_1,R_2,R_3,V$。因此 (12) 给真正的全测度式
$$
\boxed{
\Sigma_r|_{W_t\in p^n\mathbf Z_p}
=\lambda^n(A_W^n)_*\Sigma_{r+n}
\qquad(n\ge0).
}
\tag{21}
$$
下标按 $4080$ 约化。特别 $n=4080m$ 时，右侧回到同一
$\Sigma_r$；这是本篇实际支付的同来源深度递归。

因为 $510$ 是单位，(21) 对旧 $W_t$ 与放大后的
$\widehat W$ 的深域完全相同。
若另用 $\widehat W$ 的 principal Mellin 作数值观察，
仍须乘 $\langle510\rangle^{du}$；其中央导数有
$d\log\langle510\rangle$ 乘对应的真实质量。
(21) 已拉回旧物理坐标，不需另添加该换坐标因子。

## 6. 两个有标签的伴随投影与旧 W 核严格交换

R480 的 $\mathcal D_1,\mathcal D_2$ 只作用于新增固定
$\mathcal S_{612}$ 因子，分别对应两个原输入态。
(9) 的旧 $W$ 核只作用于第一因子。因此在整个扩大空间中，
$$
\boxed{
[\mathcal D_{i,V},K_N\otimes I^{\otimes6}]=0,\qquad i=1,2.
}
\tag{22}
$$
物理坐标 (20) 也固定 $V$。所以 (21) 对各个
$\mathcal D_{i,V}\Sigma_r$ 原样成立，且 (22) 对所有原五伴随
测试都合法。R480 的统一两条算术线算子
$\mathcal D_1+\mathcal D_2+\mathcal D_3$ 也同样交换。

这不把两个 $\mathcal D_i$ 合成同一个新曲线投影。
R480 的实际交叉表仍保留
$\mathcal D_2\Phi_1=P_{{\rm ref},Y}\Phi_1$；
不带输入态标签地合并会增加那个真实参考来源。

在初态，R480 已付
$$
P_{{\rm new},Y}\Sigma_0
=S_{\rm new}(Y)\overline\Lambda_{612}(V)
 \Lambda_{\rm old}(\mathbf Z).
\tag{23}
$$
其第三曲线中央零可保全部六伴随。
但 (22) 只给各个 $\mathcal D_{i,V}\Sigma_0$ 自己的旧
$W_t$ 核心轨道，须保留前述输入标签和交叉参考。即便从
(23) 本身出发，旧核也混合 $Y,Z,U$，不保证第一因子继续
独立为 $S_{\rm new}$。本篇没有替这些新状态再赋中央零。

## 7. 所有实际管及其补域的正确运输

对于任意紧开条件域 $D$ 与连续测试 $f$，(21) 的完整形式为
$$
\boxed{
\int_{D\cap\{W_t\in p^n\mathbf Z_p\}}f\,d\Sigma_r
=\lambda^n
 \int_{(A_W^n)^{-1}D}f(A_W^nx)\,d\Sigma_{r+n}.
}
\tag{24}
$$
原第一输出的真实改变为
$$
Y\longmapsto
Y+\frac{\kappa^n-1}{36}(37-3\delta)W_t,
\tag{25}
$$
其他两个旧伴随依 (19) 同时改变，新 $V$ 则保持不动。
所以附加 $Y$ 单位条件时，右边必须使用 (25) 的单位指示函数
与对数。不能因为左边 $W_t$ 深，就把右边的移动量先认作
高阶小量；右侧源状态的未归一 $W_t$ 可以是单位。

R480 每个固定 companion CM 支只缩放、平移新 $V$ 的来源；
它不改变旧 $Y,Z,U$。因此不含 $V$ 的旧混合管
$$
W_t=c_W(Y,Z,U)\in p^n\mathbf Z_p
\tag{26}
$$
与这些实际新伴随算子逐项交换。
若测试改为
$V-\ell(Z,U,R_1,R_2,R_3)\in p^m\mathbf Z_p$，
则 (24) 必须先将 $\ell$ 按 (19)、(25) 运输；再使用一个
norm-$a$ 伴随 CM 支时，还须依 R480(14) 将 $V$ 测试改为
$V/a$，保该支的完整平移来源。

全部补域也由同一恒等式相减，不能删除。例如若 $D$ 是某个
已选原隐藏输入区域，(24) 同时支付
$D\cap\{W_t\in p^n\}$ 及
$D^c\cap\{W_t\in p^n\}$，其和才是完整旧 $W_t$ 深行。

最后，忘掉新 $V$ 与本篇真实旧 $W$ 核交换，因为它是不同
theta 因子的质量映射。忘掉后的来源是
$$
K_{W_t}^{\,r}\bigl(D_-\Pi_0\,\widehat\rho_1\bigr)
$$
在相同固定覆盖中的实际状态。
它不能改写成 $D_-\Pi_0 K_{W_t}^{\,r}\widehat\rho_1$：
原第一轴投影与混合旧 $W_t$ 核一般不交换，R465 的
$P_{\rm new}\widehat\rho_0=0$、
$P_{\rm new}\widehat\rho_1\ne0$ 已明确显示这个差别。
所以这里的 $4080$ 次返回不是把原两个状态免费延长成
新增 lift 的两态返回。

## 8. 证书与后续可用的精确接口

本篇提供一个有限固定空间，在其中旧混合核心、新伴随 CM
投影、所有原五伴随和全部域运输同时有定义。新增 $V$ 的
投影可逐项穿过旧 $W_t$ 管；改变 $Y$ 的 (25) 和原
$D_-\Pi_0$ 与旧核之间的次序仍保留。

- [固定共同覆盖及全中心比值复核脚本](../scripts/check-r484-old-mixed-axis-common-cover.py)。
- [完整矩阵、极化、ray 与精确局部阶数据](../scripts/check-r484-old-mixed-axis-common-cover.json)。
- [R465：原六输入和改变 Y 的旧 W 核](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R476：完整八维第一轴及五伴随分解](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R480：两个有标签的 companion-only CM 投影](R480-original-simultaneous-cm-companion-transfer-and-two-arithmetic-rows.md)。
- [R413：任意偶 degree 的原整核心与全部半特征](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R454：本篇所细分的原固定无限 ray](R454-original-odd33-core-and-exact-residual-slope-transport.md)。

