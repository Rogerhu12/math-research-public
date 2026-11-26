# R967 — 原 E65 三个二挠译像的准确主分量与完整 mixed 读数

日期：2026-11-26。**状态：已证明。**

在 R959/R966 的同一个原格和完整 Fourier 来源上，三个非零二挠点
的原 Weyl lift 满足
$$
\boxed{\Pi_0\mathcal U_T^{(390)}Z=\frac1{\sqrt3}Z.}
\tag{1}
$$
这里 $\sqrt3$ 是固定的正实代数根；原 lift 确实在含 $\sqrt3$ 的域上，
不是一个被额外缩放的 $K=\mathbf Q(\omega)$ 有理矩阵。
第2节给其准确代数式：若用有理 lift $B_T$，同一结论是
$\Pi_0B_TZ=3^{97}Z$。

(1) 给原坏中央强迫的三个真实 translated 来源。
对于已经分离的原 E65 联合，它还在整个全局 $\mu_6$ 不变
mixed 测试上准确压缩；不要求测试分离成两个因子。
这个结论不把原 mixed 值赋零，也不把未成轨道的单个 CM
torsion 分支认成全局不变。

## 1. 完全指定的格、正实半点和原 Weyl lift

保持 R966 的
$$
\delta=1+2\omega,\quad
\tau=(1-\omega)^{-1},\quad
\Lambda=\mathbf Z+\tau\mathbf Z,
$$
以及标准 Weierstrass sigma $\Sigma(u)=u+\cdots$。
其准周期为
$\eta_v=2\sqrt3\pi\bar v$，线性延伸到下面的实际分点。
令
$$
T_*=\frac12,\qquad
T_r=\frac r2\quad(r=1,\omega,\omega^2).
\tag{2}
$$
保这些代表的完整中心；三者恰为三个非零二挠点。
原 degree390 Weyl lift 是
$$
\mathcal U_T^{(390)}A(u)
=e^{-390\eta_T(u+T/2)}A(u+T).
\tag{3}
$$
它不是仅给出点 $T$ 后任取一个 scalar 的平移。

R959 的同一来源是一个固定非零 scalar 倍的
$$
A(u)=e^{390\sqrt3\pi u^2}
\sum_{n\in\mathbf Z}a_n
 \exp\!\left(\frac{\pi i\delta n^2}{2340}+2\pi inu\right).
\tag{4}
$$
在 $T_*=1/2$，$\eta_{T_*}=\sqrt3\pi$，所以(3)的 Gaussian
准确消去(4)平移产生的全部 Gaussian：
$$
\boxed{
\mathcal U_{1/2}^{(390)}A(u)
=e^{390\sqrt3\pi u^2}
\sum_n(-1)^n a_n
 \exp\!\left(\frac{\pi i\delta n^2}{2340}+2\pi inu\right).}
\tag{5}
$$
这里没有遗留根单位或三、五、十三处的额外改动。
原 degree 为偶，完整周期字符使
$(\mathcal U_T^{(390)})^2=I$，而 $Z$ 偶使三个译像也都偶。

## 2. 二挠点的代数身份与不可省的 sqrt3

用正实周期将(2)认回同一个
$E_1:y^2=x^3+1,\ dz=dx/(2y)$。
实半点是唯一的非零实二挠点，故
$$
T_*\longleftrightarrow(-1,0).
\tag{6}
$$
这个实规范没有任意再旋转一个 CM 单位。
也可从 $\Lambda=(1-\omega)^{-1}\mathcal O_K$、
$\wp(\omega u)=\omega\wp(u)$ 核定相同的实根。

先在 degree2 核定常数。
令 $c_T=e^{-\eta_TT}\sigma(T)^2$；沿实区间 sigma 从正的首项
连续到实半点，故 $c_T>0$。
实际半点加法给
$$
\mathcal U_T^{(2)}(\sigma^2)
=c_T(x+1)\sigma^2,\qquad
\mathcal U_T^{(2)}(x\sigma^2)
=c_T(2-x)\sigma^2 .
\tag{7}
$$
原 lift 的平方为一，(7)的两个完整矩阵相乘给
$3c_T^2=1$。因此绝对正号是
$$
\boxed{c_T=\frac1{\sqrt3}.}
\tag{8}
$$
这与(5)是同一个原 lift，不是为取得想要的主分量另选归一。

在 degree390，定义完整有理算子
$$
B_T[\sigma^{390}R(x,y)]
=\sigma^{390}(x+1)^{195}
R\!\left(\frac{2-x}{x+1},
         \frac{-3y}{(x+1)^2}\right).
\tag{9}
$$
整个分式按原 whole 截面延拓。
准确有
$$
\boxed{
B_T^2=3^{195}I,\qquad
\mathcal U_T^{(390)}=3^{-195/2}B_T.}
\tag{10}
$$
所以 $B_T$ 是 $\mathbf Q$ 上的有理 lift，却不是 involution；
原 involution $\mathcal U_T$ 确实需要
$\mathbf Q(\omega,\sqrt3)$。$\Pi_0$ 有理与(1)之间不存在域矛盾。

对原 $Z=\sigma^{390}P_Z(x^3)$，(1)等价于整个有理多项式身份
$$
\boxed{
\Pi_{x^3}
\left[(x+1)^{195}
 P_Z\!\left(\left(\frac{2-x}{x+1}\right)^3\right)\right]
=3^{97}P_Z(x^3),}
\tag{11}
$$
其中 $\Pi_{x^3}$ 仅保 $x$ 的三倍次幂。
本篇的证明在第3节给出，不以有限 jet 或样点判断(11)。

## 3. 原 2 处矩阵如何准确变成几何主分量

R959 的完整 Fourier 系数是
$$
a_n=v_2(n\bmod4)v_3(n\bmod3)
 f_5(2n\bmod5)f_{13}(-n\bmod13),
$$
$$
v_2=(1,t,-1,t),\quad
t=\frac{\sqrt3-1}{\sqrt2},\quad v_3=(0,1,1).
\tag{12}
$$
五、十三处的实际来源全部保持。
在原二处 Haar 格中
$$
f_A=e_0-e_2,\qquad f_B=e_1+e_3,\qquad
\phi_2=f_A+t f_B;
$$
$f_A,f_B$ 正交且平方范数都为一。
R959(21)的整个实际算子为
$$
M_\omega
=-\frac{\omega^2\zeta_8^{-1}}{\sqrt2}
 \begin{pmatrix}1&\zeta_8^{-1}\\\zeta_8^{-1}&i\end{pmatrix},
\quad
M_\omega\phi_2=\phi_2,\quad
\operatorname{char}(M_\omega)=(X-1)(X-\omega).
\tag{13}
$$
它在这个完整块上酉，不是只在一条给定向量上猜到的标量。

由(5)，二处准确换为
$\phi'_2=f_A-t f_B$，所有其他局部向量不变。
于是原特征一投影
$P_2=(I+M_\omega+M_\omega^2)/3$ 给
$$
P_2\phi'_2
=\frac{\langle\phi'_2,\phi_2\rangle}
       {\langle\phi_2,\phi_2\rangle}\phi_2
=\frac{1-t^2}{1+t^2}\phi_2
=\frac1{\sqrt3}\phi_2.
\tag{14}
$$

必须说明(14)为什么是原几何主分量，而不仅是一个有限酉投影。
原 R290 §6、R959 §9 使用的是同一个全局有理 $\omega$ 的
Weil 互反：theta 求和泛函被全局 $\omega$ 保持，无穷处第 $m$
Hermite 向量的特征是 $\omega^{\pm m}$。
保持其他有限处原向量时，对二处向量作任意线性替换，这条
互反身份仍逐向量成立。
因此在 $3\mid m$ 的各个真实 Hermite 系数中，只读二处的
$M_\omega=1$ 分量；另一条特征 $\omega$ 的整条来源没有任何这些
系数。这个推论使用原全部有限向量和实际无限族 Hermite 系数，
没有改换 Schwartz 或只核低阶。

原(12)及其带 $(-1)^n$ 的替换都为偶来源，故 $\mu_6$ 主分量
恰由上述 $3\mid m$ 的偶系数构成。
再用 R959 的原 Hermite 生成恒等式认回完整 entire 截面，
(14)遂给
$$
\Pi_0\mathcal U_{1/2}^{(390)}Z=\frac1{\sqrt3}Z .
$$
原将(4)归一为 $Z$ 的同一非零 scalar 在两边相消。
这付了整个 Weil 到几何的字典，而不是将质量内积冒作来源身份。

最后，CM 乘 $\omega$ 保持标准 Hermitian 型和 Weyl 中心，
循环(2)的三个指定 lift；$Z$ 本身属于主型。
故(1)对三个 $T_r$ 全部成立，原正号和同一个 $\sqrt3$ 不变。

## 4. 普通、惰性与同一坏中央的三个真译像

每个 $\mathcal U_TZ$ 是同一个 degree390 whole 截面。
由(1)的常数项，它的中心值准确为零；也可由
$P_Z$ 的原 $(X+1)$ 因子直接核实实半点。
在原好位 $p>211$，(9)–(10)的系数整、所有显示分母及 $\sqrt3$ 都是单位；
在固定的有限 étale 系数扩张上使用同一个 lift，未逐 $p$ 换相位。

普通处原 principal 单位 Mellin 读者满足
$\mathcal L_p(A)=\mathcal L_p(\Pi_0 A)$：
单位域及 $\log\langle x\rangle$ 都在 $\mu_6$ 下不变。
所以准确有
$$
\boxed{
\mathcal L_p(\mathcal U_T Z)
=\frac1{\sqrt3}\mathcal L_p(Z).}
\tag{15}
$$
同样的身份对完整 principal 单位 Mellin 函数成立，不只在导数。

惰性处 $p+1$ 是六的倍数，原 Gaussian 也只含六倍次幂。
因此 R959/R966 的整个 Newton 读者只读取 $\Pi_0 A$。
先用(1)进入原至少六阶的整格，再用同一个严格圆盘估计，
得到整个收敛函数身份
$$
\boxed{
\mathcal J_{\mathcal U_TZ,p}
=\frac1{\sqrt3}\mathcal J_{Z,p}.}
\tag{16}
$$
没有将普通测度搬到惰性处，也没有遗漏 $p\kappa$ 的单位规范。

因此原 E65 坏中央确实强迫三个完整二挠译像的中央全零。
这项授权只属于这些已指定来源；不授予一般乘积或任意
first-sigma 平移一个中央零。

返回 $b=17$ 时，$Z_b(z)=b^{-1}Z_1(\theta_b z)$、
$\theta_b^6=b$，点同取 $T_{r,b}=\theta_b^{-1}T_{r,1}$。
完整 lift 随同共轭，(1)、(15)–(16)的系数仍是 $1/\sqrt3$。
R959 的实际物理比例 $17/65$ 与原 period/Schwartz 全部保持。

## 5. 与真实 δ 两中心的完整合并

令 $\mathcal T_j$ 是 R966 的原三点 lift，$j=0,1,2$。
其相同 Gaussian 比较表明，它就是这三个点上的同一 Weyl lift。
保持实际有序操作
$$
\mathcal U_{T_r}\mathcal T_j Z .
\tag{17}
$$
不把它按 torsion 点相加后丢去中心。
两组的 theta 群交换子是一：$390E(T_r,j/3)$ 总为整数。
其单次 Weyl 乘法中心仍可能为负，已由(17)的次序保留。

对实半点，用(5)和 R966(6)，完整 Fourier 系数同时乘
$(-1)^n e^{2\pi i nj/3}$。
二处仍按(14)分解；三处准确是
$$
(0,\omega^j,\omega^{2j})
=-\frac12(0,1,1)\ \pm\frac\delta2(0,1,-1)
\quad(j=1,2).
\tag{18}
$$
后一项是原三处的奇方向，它的三次单位特征与原偶方向相同，
但反射特征相反，故产生的整个来源只含模六为三的角型。
二处另一特征只产生非主的偶角型；两者合用仍不可能产生主型。
由同一个全局 Weil/Hermite 字典，
$$
\boxed{
\Pi_0\mathcal U_T\mathcal T_j Z
=-\frac1{2\sqrt3}Z\quad
(T\ne0,\ j=1,2).}
\tag{19}
$$
CM 循环时保原三点 lift；其与三次单位的周期中心在 degree390
为一，故其他两半点同样成立。

于是整个 $E[2]\oplus E[\delta]$ 的十二个指定有序 lift 的主分量
系数全部明确：
$$
c_{0,0}=1,\qquad c_{0,1}=c_{0,2}=-\frac12,\qquad
c_{T,0}=\frac1{\sqrt3},\qquad
c_{T,1}=c_{T,2}=-\frac1{2\sqrt3}.
\tag{20}
$$
它们的普通 principal/惰性完整读者都是同一个原读者乘(20)。
这是同一来源的有限真受迫族；没有增加新的算术曲线假设。

## 6. 原 full joint 与完整 mixed cut 的实际压缩

本节 mixed 积分仍在原普通情形；不向惰性处增添普通测度。
使用 R963/R965 的原分离
$$
\mathcal P_{65}\Phi=Z\otimes\Lambda,\qquad
\Phi=\Phi_\rho\ \text{或}\ \Phi_h.
\tag{21}
$$
这两整个来源在六变量同时乘 $\zeta\in\mu_6$ 下不变；
$\mathcal P_{65}$ 与该作用交换，$Z$ 为主型，
所以整个五伴随 $\Lambda$ 也在同时乘 $\zeta$ 下不变。

故对任何完整测试
$$
F(\zeta Y,\zeta\mathbf Z)=F(Y,\mathbf Z)
\quad(\zeta\in\mu_6)
\tag{22}
$$
及其原全部 mixed 单位/deep 条件，准确有
$$
\boxed{
((\mathcal U_{T,Y}\mathcal P_{65})\Phi)(F)
=\frac1{\sqrt3}(\mathcal P_{65}\Phi)(F),}
\tag{23}
$$
以及
$$
\boxed{
((\mathcal U_{T,Y}\mathcal T_{j,Y}\mathcal P_{65})\Phi)(F)
=c_{T,j}(\mathcal P_{65}\Phi)(F).}
\tag{24}
$$
证明是对整个来源作对角 $\mu_6$ 平均；因 $\Lambda$ 不变，
它准确只保第一因子的 $\Pi_0$。然后应用(1)、(19)。
这不要求 $F$ 分离为第一轴权与独立伴随测试，
也不需要假设原中央为零。
但(23)–(24)本身没有令右端原 mixed 值为零。

原 R536 的 $q$ 是全齐次六的原整模型组合，原 R544/R548 的
所有单位/deep 域以及 principal logarithm 都在同时乘
$\mu_6$ 下保持。线性 $P_1,R_c,L_h^{-1}$ 与全局标量交换。
因此原
$$
F_{\rm rem}=((f-f\circ R_c)\circ P_1)\circ L_h^{-1}
\tag{25}
$$
满足(22)，整个原 $q$、$\lambda,\kappa$ 参数和所有域不需修改。
(23)–(24)可直接用于这个同一个实际测试。

R965 §9 的完整四态
$\rho,h_{34},h_{56},h_{34,56}$
也都是全局 $\mu_6$ 型零；这只支付相应全局平均。
其中 $h_{34}$、$h_{34,56}$ 若需更大整覆盖，仍须支付它们自己的
真实第一投影与 lift，不能直接冒作 R963 的 degree390 框架。
只有已经取得准确(21)的来源，才直接使用本节的系数；
全局角型本身不替代这条来源门。
相反，单个码 $e_r$ 或未成轨道的 $A_r\rho$ 一般在 $\omega$ 下
相互置换，虽然它们都偶，却不能各自套(23)。
原未配对的单个 CM torsion 中心同样不能各自作全局平均；
必须保持完整真实 CM 和式或实际轨道以后再使用(22)。

本篇所有第一平移都放在原 $\mathcal P_{65}$ 之后。
它们与 R965 的纯伴随算子严格交换，却没有与
$\mathcal P_{65}$ 自由交换，也没有与 R964 的 $S=d/h_7$ 乘法交换。
原 R548 的未投影 mixed 余项及 R966 的交叉乘积 $C_1J_Z$
仍不能因此被赋零。


## 7. 十二个受迫译像的准确范围与实际交叉项

由(20)，这十二个指定有序来源在原 $\Pi_0$ 后的张成恰为
$K(\sqrt3)\,Z$；包含恒等来源，所以不是只得到一个上界。
不能将这条有限轨道误作 entire degree390 主空间。

R966 的同一个 $C=C_{24}$、$J=J_Z$ 满足
$C_1+C_2=9SC-C$，其中 $S=X(X-8)/Q_2$ 是该文的有理乘子。
两者都奇，真实反射把 $C_1J$ 换成 $C_2J$；
各乘积在 $[\omega]$ 下不变，因为 $C_j$、$J$ 的三次型分别为二、一。
故其完整主投影准确为
$
\boxed{\Pi_0(C_1J)=\frac{C_1J+C_2J}{2}
             =\frac{9SZ-Z}{2}.}
\tag{26}
$
这个等式保原全部乘积和 canonical 中心，不把任意因子单独投影。
因此
$
\frac{\Pi_0(C_1J)}Z=\frac{9S-1}{2}
$
是非常数；$SZ/Z=S$ 也非常数。
两者均不在上述十二个受迫来源的主投影张成中。
这用的是实际函数恒等式，不是维数或质量猜测。
在原好剩余特征同样成立：$Q_2=7X^2-4X+16$ 的非零常数项
排除它与 $X(X-8)$ 成比例。

所以新真中央族尚不能使交叉项 $C_1J$ 或 $SZ$ 的中央为零。
要从其他不同 degree 的已知算术曲线获得它，仍须另给真正的同来源桥；
乘固定载体不会自动运输中央零。后续继续使用实际共同伴随和完整 mixed 域，
不原样扩充这条已经计算清楚的有限轨道。

## 依赖

- [R959：原 E65 全部局部 Schwartz 与全权来源](R959-original-e65-two-independent-points.md)。
- [R290：原全局 Weil 求和与全部 Hermite 权的角型](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)。
- [R966：原准确 δ-new 及两个非零三中心](R966-original-e65-delta-new-and-c24-two-center-defect.md)。
- [R965：原完整二挠伴随单位逆与四态](R965-original-e65-full-joint-dyadic-companion-unit-inverse.md)。
- [R964：原实际乘法来源的单位交换子](R964-original-e65-rational-off-target-unit-commutator.md)。
