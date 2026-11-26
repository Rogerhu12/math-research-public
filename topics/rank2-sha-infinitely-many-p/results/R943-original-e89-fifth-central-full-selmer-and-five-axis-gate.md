# R943 — 原 E89 的第五中央、完整通常 Selmer 桥与五高轴门

日期：2026-11-26。**状态：本篇各定理已证明。** 固定新曲线为
$$
E_{89}:y^2=x^3+89.
$$
本篇支付它的秩至少二、全部有限局部角色及原 Schwartz、标准 degree178 截面、非零六次首项、全权平方、普通与惰性处的完整通常 Selmer 比较。它给第五条合法原中央条件，与原 $S_{34},T_{72},U_{136},V_{66}$ 共用同一实际角函数后，五个确定的高轴有唯一模 $p^5$ 必要值。

新来源不属于旧归一化的 $B_{89}$；第五中央不自动产生 $\epsilon^5$ 深核。本篇另把它所约束的五个高轴实际运输到旧完整来源格，保留四条十三行带，以及三、四、五次指数项先按真实 $w$ 次数折回产生的低层 carry。尚未证明五条原中央在无穷多个素数不能同时零。

## 1. 两个实际点与严格秩下界

取
$$
P=(-4,5),\qquad Q=(10,33).
$$
它们满足原方程。模 $5$、模 $17$ 的约化都好，且 $x^3+89$ 分别有唯一根 $r=1,4$。在只有一个非零有理二挠点 $T=(r,0)$ 的有限域曲线上，标准二下降同态为
$$
d_\ell(R)=x(R)-r\in\mathbf F_\ell^\times/
\mathbf F_\ell^{\times2},\quad
d_\ell(T)=3r^2,\quad d_\ell(O)=1.
\tag{1}
$$
它杀掉 $2E(\mathbf F_\ell)$。模5时 $P$ 正好约化为 $T$，因此必须使用导数特值，而非把零当平方类。两行的 Legendre 符号准确为
$$
\begin{array}{c|cc}
\ell&d_\ell(P)&d_\ell(Q)\\ \hline
5&-1&+1\\
17&+1&-1
\end{array}.
\tag{2}
$$
具体地，第一行用 $3$ 和 $4$，第二行用 $9$ 和 $6$。两个约化下降给 $E_{89}(\mathbf Q)/2E_{89}(\mathbf Q)$ 中两个独立元素。又 $-89$ 不是有理立方，故 $E_{89}(\mathbf Q)[2]=0$，于是
$$
\operatorname{rank}E_{89}(\mathbf Q)\ge2.
\tag{3}
$$
这里没有预设秩恰为二。

## 2. 原 Hecke 角色、所有坏位与 Hermitian 参数

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad\delta^2=-3,\quad\operatorname{Im}\delta>0,
$$
$$
s_0=(1-\omega)^{-1},\qquad\Lambda=\mathbf Z+s_0\mathbf Z.
$$
$\psi_{89}$ 始终是 $E_{89}$ 自身的 CM Hecke 角色，
$\chi=\psi_{89}|\cdot|^{-1/2}$，且
$\chi_\infty(z)=(z/|z|)^{-1}$。
Silverman–Stange §6、Theorem19 的证明给所有好素理想上的六次扭转公式
$$
\psi_{89}(\mathfrak p)/\psi_1(\mathfrak p)
=(89/\mathfrak p)_6^{-1}.
\tag{4}
$$
从该原角色得到完整局部表：
$$
\begin{array}{c|c|c|c}
v&\chi_v\text{ 在单位上}&\text{uniformizer 值}&a(\chi_v)\\ \hline
2&u\bmod2\in\mu_3&\chi_2(2)=-1&1\\
\delta&u\bmod\delta\in\{\pm1\}&\chi_3(\delta)=-i&1\\
89&u^{1320}\bmod89\in\mu_6&\chi_{89}(89)=-1&1
\end{array}.
\tag{5}
$$
单位值均取指定复嵌入的 Teichmüller 提升；89处的指数是局部 idèle 单位分量的正指数，不能把 (4) 的 Frobenius 逆号再抄到此栏。

完整核定如下。在2处，$89/17\equiv1\bmod8$ 是 $\mathbf Q_2$ 中六次幂；在3处，$89/17\equiv1\bmod9$ 是 $\mathbf Q_3$ 中六次幂。因此这两处的单位和 uniformizer 角色均等于 R290 的原 $E_{17}$ 角色。在89处，$K_{89}/\mathbf Q_{89}$ 非分歧二次，六次扭转的 tame 单位角色为 $u^{(89^2-1)/6}$，导子一次；其 uniformizer 扭转值为一，因为 $-1$ 是残域中的六次幂。参考未分歧角色在惰性 uniformizer 上为 $-1$，给 (5)。这也逐个满足主 idèle $2,\delta,89$ 的乘积关系。

所以原 primitive 导子与射线次数是
$$
\mathfrak f_{89}=(2\delta\cdot89),\qquad
N_{E_{89}}=3N\mathfrak f_{89}=285156,
$$
$$
[K(\mathfrak f_{89}):K]
=\frac{(4-1)(3-1)(89^2-1)}6
=7920=2^4\,3^2\,5\,11.
\tag{6}
$$
$K$ 类数为一，只有恒等根单位模 $\mathfrak f_{89}$ 为一，故没有省略根单位商。

原 dichotomy 的四个符号，在 $2,3,89,\infty$ 依次为
$(+,-,-,+)$。2、3处由刚才的完整局部同构及 R290 的 Gauss 和得到。89处令 $\theta(u)=u^{1320}$。它在 $\mathbf F_{89}^\times$ 上平凡，且
$\theta(\delta)=(-1)^{15}=-1$。将 $u=x+y\delta$ 按 $x$ 分纤维，$x=0$ 时单位角色之和为 $-88$，$x\ne0$ 时为 $1$，故原负有限加性角色的 Gauss 和为 $-89$。结合 $\chi_{89}(89)=-1$ 得局部 epsilon 为 $+1$，再乘 $\chi_{89}(\delta)=-1$ 得 dichotomy 负号。无穷处取正参数。于是可以且固定取
$$
\alpha=89,\qquad W(E_{89})=+1,\qquad
\iota_\alpha(x+y\delta)=
\begin{pmatrix}x&9\alpha y\\-y/(3\alpha)&x\end{pmatrix}.
\tag{7}
$$
89在2处为单位范数、在3处为非范数单位、在89处为奇赋值、在无穷处为正，逐个核对上述符号。

## 3. 全部有限 Schwartz 与真实非零向量

### 3.1 二处和三处

令
$$
e_j=\mathbf1_{j/2+2\mathbf Z_2},\qquad
t_+=(1+\sqrt3)/\sqrt2,\qquad
\phi_2=e_0-e_2+t_+(e_1+e_3).
\tag{8}
$$
其四坐标为 $v_2=(1,t_+,-1,t_+)$，范数平方 $3+\sqrt3$。
存在 $c\in\mathbf Z_2^\times$ 满足 $c^2=89/17$，可选 $c\equiv3\bmod8$；原 Schrödinger kernel 的变量代换给 $\iota_{17}$ 到 $\iota_{89}$ 的实际共轭。Jacobian为一，平方改变不改 Weil 指数，而 $v_2(3j)=v_2(j)$，所以这个 dilation 固定整个向量。由 (5) 的完整同角色，R290 的全部生成元验证直接运输；没有自由重置一个 dyadic 相位。

三处取
$$
\phi_3=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\|\phi_3\|^2=3.
\tag{9}
$$
$89/17$ 是三进单位平方，原 dilation 保持该球；同一个 $\chi_3$ 和完整 Weil kernel 因而给全环面不变性。

### 3.2 八十九处

置 $q=89$、$\zeta=e^{2\pi i/q}$，
$T_q=\{x+y\delta:x^2+3y^2=1\}\subset\mathbf F_{q^2}^\times$，
以 $e_a=\mathbf1_{a/q+\mathbf Z_q}$ 为基。
原有限 $\mu_4$ Weil 模型准确为
$$
W(g)_{ab}=-\frac{(\frac yq)}{\sqrt q}\,
 \zeta^{\frac3{2y}\{x(a^2+b^2)-2ab\}}
 \quad(g=x+y\delta,\ y\ne0),
\qquad W(1)=I,\quad W(-1)e_a=e_{-a}.
\tag{10}
$$
这是 (7)、负有限加性角色和原 lattice–Schrödinger intertwiner 的公式；
$(6/89)=-1$、$G_{89}=\sqrt{89}$ 给显示前因子。全部乘法由有限 Gauss 合成验证，不能从十一处的 $-R$ 模型搬用反射号。

Hilbert90 的 $g=z/\bar z=z^{-88}$ 把 (5) 写成
$\eta(g)=g^{-15}$。Yang 1999 Proposition1.2(3) 的 quadratic splitting 是
$\eta_0(g)=g^{45}$，所以原 Hecke 不变线在 $\mu_4$ 模型中要求
$$
\tau=\eta_0\eta^{-1},\qquad\tau(g)=g^{60}.
\tag{11}
$$
它是偶的三次角色，异于唯一缺失的二次角色。由 Yang 1998 的完整有限环面分解，
$$
\Pi_\tau=\frac1{90}\sum_{g\in T_q}\tau(g)^{-1}W(g)
$$
是秩一正交投影。固定原向量
$$
f_{89}=45\sqrt{89}\,\Pi_\tau e_0.
\tag{12}
$$
它的坐标和精确范数为
$$
f_{89}(a)=\sqrt{89}\,\mathbf1_{a=0}
-\frac12\sum_{\substack{g=x+y\delta\in T_q\\g\ne\pm1}}
\tau(g)^{-1}\Big(\frac y{89}\Big)
\zeta^{3xa^2/(2y)},
$$
$$
c_{\rm loc}=\frac12\sum_{g\ne\pm1}\tau(g)^{-1}
 \Big(\frac y{89}\Big)=5,\qquad
f_{89}(0)=\sqrt{89}-5,\qquad
n_{89}:=\sum_a|f_{89}(a)|^2=45(89-5\sqrt{89})>0.
\tag{13}
$$
这里的 $5$ 由第12节公开精确有限域运算得到，并非选定一个范数归一。即使不先求这个整数，(12) 的非零也已严格成立：$g,-g$ 配对说明 $c_{\rm loc}\in\mathbf Z[\omega]$，$g,g^{-1}$ 配对说明它实，故 $c_{\rm loc}\in\mathbf Z$；它不能等于 $\sqrt{89}$。这是 Yang 1999 Proposition1.5(1) 的非零机制。

由 $\overline{W(g)}=W(g^{-1})$、$\tau(-1)=1$，
$f_{89}$ 为实偶函数。取 $\phi_{89}=\sum_a f_{89}(a)e_a$，则它在整个原 $\omega_{\alpha,\chi_{89}}$ 下固定，范数平方是 (13)。其余有限处均取 $\mathbf1_{\mathbf Z_\ell}$。

## 4. 原半特征、标准 degree178 截面与全权平方

(8)、(9)、(12) 的有理支撑是 $x=n/534$。相应局部坐标为
$2x=n/267\leftrightarrow3n\bmod4$、
$89x=n/6\leftrightarrow15n\bmod89$。
因 $v_2(3n)=v_2(n)$，原 Fourier 系数准确为
$$
a_n=v_2(n\bmod4)f_{89}(15n\bmod89).
\tag{14}
$$
CRT 与 (13) 给它们不全零。所有半特征是
$$
a_{-n}=a_n=\overline{a_n},\quad
a_{n+356}=a_n,\quad (-1)^na_{n+178}=-a_n.
\tag{15}
$$
定义
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\left(\pi i\frac{\delta}{3}\frac{n^2}{356}+2\pi inZ\right),
\qquad S_{\rm raw}(Z)=e^{178\sqrt3\pi Z^2}F(Z).
\tag{16}
$$
换指标并用 (15) 得
$$
F(Z+1)=F(Z),\qquad
F(Z+s_0)=e^{-178\pi i s_0-356\pi iZ}F(Z).
\tag{17}
$$
所以 $S_{\rm raw}\in H^0(\mathbf C/\Lambda,\mathcal O(178[0]))$，没有 flat twist；Fourier 唯一性证明它非零。

令 Hermite 多项式由
$\sum H_m(x)T^m/m!=e^{xT-T^2/(8\pi)}$ 定义，置
$$
b_m=\sum_n a_n H_m\left(\frac{\sqrt{267\sqrt3}}{534}n\right)
 e^{-\pi\sqrt3 n^2/1068},
\quad h=\frac{\sqrt{267\sqrt3}}{1068\pi i}.
$$
于是
$$
\sum_m b_mT^m/m!=S_{\rm raw}(hT),\qquad
178\sqrt3\pi h^2=-1/(8\pi).
\tag{18}
$$
全部有限处的原 $\omega$ 作用已固定，结合全局有理单位的 Weil 相容及 (15)，右边属于 $\mathbf R[[T^6]]$。

对 $6\mid m$，(5) 的所有坏位角色在 $\chi^{2m+1}$ 下不变：单位的三次部分要求 $3\mid m$，三处 $-i$ 要求 $m$ 偶。这正是同一原有限 Schwartz 的全权系列。全范数为
$$
\mathcal N_m=
 \frac{3(3+\sqrt3)n_{89}}{\sqrt{534\sqrt3}}\,
 \frac{m!}{(4\pi)^m}.
\tag{19}
$$
Yang 1997 Theorem1.11 的非分歧二次坏位集合为 $\{2,89\}$，故
$c(0)=(1+1/2)^{-1}(1+1/89)^{-1}=89/135$。
$h_K=1$，范数一商与极大紧群的原体积比为6；
代入 $L(1,\epsilon_K)=\pi/(3\sqrt3)$ 及 (19) 给
$$
L(\psi_{89}^{2m+1},m+1)=
C_{89}\frac{(4\pi)^m}{m!}b_m^2,\qquad
C_{89}=\frac{5\pi\sqrt{534\sqrt3}}
 {89\sqrt3(3+\sqrt3)n_{89}}>0.
\tag{20}
$$
这是完整实平方，保二、三、89处的范数及所有原 uniformizer。

Rubin 的 CM rank-zero 定理给
$L(E_{89},1)\ne0\Rightarrow\operatorname{rank}E_{89}(\mathbf Q)=0$。
由 (3)、(20) 得
$$
b_0=0,\qquad\operatorname{ord}_0S_{\rm raw}\ge6.
\tag{21}
$$
正六次非零由下面的完整算子识别证明，不从正权值猜测。

## 5. 完整30维 CM 识别、非零首项与实际来源定义

在共同模型 $E_1:y^2=x^3+1$，固定
$dz=dx/(2y)$、$x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、
$\sigma=z+\cdots$。标准 degree178 的完整 type0 基为
$$
e_j=\sigma^{178}x^2X^j,\qquad X=x^3,\quad0\le j\le29.
\tag{22}
$$
原点阶是 $174-6j$，质量行是 $\ell=(0,\ldots,0,1)$。

取原 $\gamma_7=3+\omega,\gamma_{13}=4+\omega$ 和
$$
N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^*.
\tag{23}
$$
若 $x(\gamma z)=A_\gamma(x)/B_\gamma(x)$，
$f_a=(A_\gamma-aB_\gamma)^{\rm monic}$，则完整 fiber 的输出除以目标 $\sigma^{178}a^2$ 是
$$
\frac1{\gamma a^2}\operatorname{Tr}_{f_a}
\left[
 (Q_{\bar\gamma}/Q_\gamma)^{178}
 x(\bar\gamma z)^2P(x(\bar\gamma z)^3)
\right],
\quad
Q_\gamma=\frac{\sigma(\gamma z)}{\sigma(z)^{N\gamma}}.
\tag{24}
$$
原178次 carrier、division leading constant、$a^{-2}$ 均保留。
$a=1,\ldots,30$ 的全纤维与 $(a^{3j})$ 的 Vandermonde 给完整矩阵，
$a=31,32$ 再核全部列。每个 norm13 fiber 另用原 $S_{34}$ 绝对锚核相位；
norm7 使用 R464 原全 fiber。算子保持完整 theta 空间的事实由原 pull/trace 给出，额外两个 fiber 不是以抽样代次数证明。

第12节的 $\mathbf Q(\omega)$ 精确运行证明两个矩阵交换。
质量观察行 $\ell,\ell N,\ldots,\ell N^{29}$ 的核维数在 norm13、norm7 下分别为24、1；两个算子共同稳定观察行空间的秩为29。
唯一共同核有归一向量
$$
(c_0,\ldots,c_{28},c_{29}),\qquad
c_{28}=1,\quad c_{29}=0,\quad c_j\in\mathbf Z[1/91],
\tag{25}
$$
且 $N_7$、$N_{13}$ 在该线上分别作用为 $1+\omega,\omega$。
本篇用 (22)–(25) 的唯一性定义全部系数；不把可重算的29项输出表存成新数据或源码输入。

现在识别实际来源。第2–4节已独立支付完整 Hecke 角色与各坏位 Schwartz。
R297 的原有限 Heisenberg push/pull 比较，在7、13处完成未分歧 trace 后，把 (23) 与各坏位的同一 $\gamma/\bar\gamma$ Weil 作用相比；两个作用实现同一 Heisenberg 自同构，故只差共同非零标量。各原局部线均固定，所以 $S_{\rm raw}$ 是两个完整算子的本征向量。
它非零而质量为零，由一维共同核必等于 (25) 的线。这一步没有以两个 Frobenius 特征值代替全部局部角色。

令
$$
P_{28}(X)=\sum_{j=0}^{28}c_jX^j,\qquad
W_1(z)=\sigma^{178}x^2P_{28}(x^3)=\sum_m\alpha_mz^m.
\tag{26}
$$
则 $\alpha_6=1$，所以 $b_6\ne0$。
对任意 $b\ne0$，真正齐次来源为
$$
W_b(z)=\sigma_b^{178}\sum_{j=0}^{28}
 c_jb^{28-j}x_b^{2+3j}
=b^{-1}W_1(b^{1/6}z).
\tag{27}
$$
取 $\theta^6=89$，$\Phi_{89}=W_{89}=89^{-1}W_1(\theta z)
=\sum s_mz^m$。于是
$s_m=89^{m/6-1}\alpha_m$、$s_6=1$；
来源不依赖所选六次根，周期和微分始终取相容根。

置 $\Omega_{89}=\Omega_1/\theta$、$\varpi_{89}=s_0\Omega_{89}$，
定义非零常数 $C_{\rm raw}$ 使
$S_{\rm raw}(Z)=C_{\rm raw}\Phi_{89}(\Omega_{89}Z)$。
由 (18)、(20)，先得到实尺度 $534^{-m}$，再用
$s_0^{2m}=3^{-m}$，准确得到
$$
\mathscr E_{89,m}:=
\frac{(2\pi/\sqrt3)^mL(\psi_{89}^{2m+1},m+1)}
 {m!\varpi_{89}^{2m+1}}
=\frac{\kappa_{89}}{s_0}\,178^{-m}s_m^2,
\quad
\kappa_{89}=\frac{C_{89}C_{\rm raw}^2}{\Omega_{89}}\ne0.
\tag{28}
$$
CM 临界值代数性和 $s_6=1$ 给
$\kappa_{89}=s_0\,178^6\mathscr E_{89,6}\in\overline{\mathbf Q}^{\times}$。
不把 $C_{\rm raw}$ 本身称为代数数，也不把固定 $\kappa_{89}$ 在各 $p$ 的赋值设为零。

## 6. 普通完整测度、Katz 平方与通常 Selmer

以下统一 $p>211$，因而 (6)、(25) 的全部固定小素数均为单位。
记
$$
r=\operatorname{rank}E_{89}(\mathbf Q)\ge2,\qquad
r_p=\operatorname{corank}_{\mathbf Z_p}\Sha(E_{89}/\mathbf Q)[p^\infty].
$$
先设 $p\equiv1\bmod3$。Mazur–Tate 普通 sigma 唯一性与 CM 自同构 $[\omega]$ 给原二阶对数方程的常数 $c_p=\omega^2c_p$，故 $c_p=0$。因此
$\sigma_{89}(\log_{E_{89}}t)\in t\mathbf Z_p[[t]]$。
(27) 每项的实际参数阶 $174-6j\ge6$，固定分母91在 $p$ 为单位，所以 $\Phi_{89}(\log_{E_{89}}t)$ 整。

取与 $\varpi_{89}$ 相容的单位普通周期 $\Omega_{p,89}$。Amice 对应给同一个有界整测度
$$
\Phi_{89}(\Omega_{p,89}\log(1+Z))
=\int_{\mathbf Z_p}(1+Z)^x\,d\nu_{89,p}(x),
\qquad
M_m=\Omega_{p,89}^{m}m!s_m.
\tag{29}
$$
定义其单位 principal Mellin 函数
$$
G_{89,p}(T)=\int_{\mathbf Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}
 \,d\nu_{89,p}(x).
\tag{30}
$$
原全质量零并不单独给 (30) 的中心零。

令 $\pi=\psi_{89}(\mathfrak p)$、$\bar\pi=\psi_{89}(\bar{\mathfrak p})$，
$v_p(\pi)=1$、$v_p(\bar\pi)=0$。
对正的 $p-1\mid m$，原角色
$\epsilon_m=\psi_{89}^{m+1}\bar\psi_{89}^{-m}$
的有限导子仍为 $\mathfrak f_{89}$；这使用 (5) 的完整单位和 uniformizer 表。两个 Katz Euler 因子恰同为
$$
1-\frac{\epsilon_m(\mathfrak p)}p
=1-\epsilon_m^{-1}(\bar{\mathfrak p})
=1-\frac{\pi^m}{\bar\pi^{m+1}},
\tag{31}
$$
$p$ Gauss 因子为一，其余坏位保 primitive 乘积。
按 R397 的原 Katz/de Shalit 规范，(28) 给
$$
\mathcal K_{89,p}((1+p)^m-1)
=\frac{\kappa_{89}}{s_0}\Omega_{p,89}\,178^{-m}
 \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2M_m^2.
\tag{32}
$$
两个实际阶乘合成 $(m!s_m)^2$，没有丢掉一个。

沿 $m_j=m_0+(p-1)p^j$ 取实无穷、$p$-adic 有限极限，非单位矩的赋值至少 $m_j$，(31) 与一之差的赋值也至少 $m_j$。
再用互异权趋零的解析恒等定理，得到整条同源身份
$$
\mathcal K_{89,p}(T)=
\frac{\kappa_{89}}{s_0}\Omega_{p,89}
 (1+T)^{-a_{178,p}}G_{89,p}(T)^2,\qquad
a_{178,p}=\frac{\log_p\langle178\rangle}{\log_p(1+p)}.
\tag{33}
$$

Agboola–Howard Theorem2.4.17(1)(b),(c) 的假设全部满足：
类数一、最大整环 CM、有理曲线、好普通、正根数，且
$p\nmid[K(\mathfrak f_{89}):K]=7920$。
它给反圆 $\mathbf Z_p$ 塔上的通常单 CM Selmer 对偶 torsion，特征理想为 (33) 的相容 Katz 分支；该分支非零。若用辅助理想，可取 $(5)$：实际 $\psi_{89}((5))=-5$、范数25，中心辅助值 $-30$ 为单位。

基层通常 Selmer 向塔上不变量的限制为单射：连通 $\pi$ 挠点的一阶 tame inertia 像有阶 $p-1$，pro-$p$ 塔不能使其平凡，所以塔上没有非零 $\pi$-初级挠点；inflation–restriction 的核为零，通常 Kummer 条件在限制下保持。因此
$$
\operatorname{corank}_{\mathbf Z_p}
 \operatorname{Sel}_{\pi^\infty}(E_{89}/K)
\le\operatorname{ord}_0\mathcal K_{89,p}.
\tag{34}
$$
$E_{89}$ 的 $-3$ 二次扭转 $y^2=x^3-2403$ 与它有理三同源；
一般 $D$ 的显示同源为
$$
(x,y)\longmapsto
\left(\frac{x^3+4D}{x^2},
 \frac{y(x^3-8D)}{x^3}\right):
E_D\longrightarrow E_{-27D}.
$$
其对偶复合为 $[3]$。$p\ne2,3$ 时，二次限制/核心限制、特征投影、三同源均保持整个通常 Selmer 余秩，复共轭交换两个 CM 分量，故 (34) 左边准确为 $r+r_p$。从 (33) 得
$$
G_{89,p}\ne0,\quad G_{89,p}(0)=0,\qquad
r+r_p\le2\operatorname{ord}_0G_{89,p},
$$
$$
G'_{89,p}(0)\ne0\quad\Longrightarrow\quad
r=2,\qquad\Sha(E_{89}/\mathbf Q)[p^\infty]\text{ 有限}.
\tag{35}
$$
这里包含全部潜在 Sha 自由方向，未用严格局部 Selmer 替代通常 Selmer。

## 7. 惰性完整 Newton 因子与 signed 通常 Selmer

现在设 $p=6s-1>211$、$d=p+1$、$\mathcal O=\mathbf Z_{p^2}$。
在共同 $E_1$ 上令
$$
f=\log(\sigma/z),\quad c=[z^d]f,\quad B=x\sigma^2=\sum_m\beta_mz^m,
$$
$$
G_{178}=W_1e^{-178cz^d},\qquad
J_{178,p}(v)=\sum_{h\ge0}(178c)^{-h}
 [z^{dh}]G_{178}\,(v)_h,
$$
$$
J_{0,p}(v)=\sum_{h\ge0}(2c)^{-h}
 [z^{dh}](Be^{-2cz^d})(v)_h.
\tag{36}
$$
$(v)_h=v(v-1)\cdots(v-h+1)$。
R301 的准确首分母给 $v_p(c)=-1$；不另选 Gaussian。
置 $\mathcal W=z^2x$、$R=p^{-1/(2p)}$。完整余项逐项为
$$
G_{178}=\sum_{j=0}^{28}c_jz^{174-6j}
 \mathcal W^{2+3j}\exp\{178(f-cz^d)\}.
\tag{37}
$$
在 R301 的严格圆盘上 $\|\mathcal W\|_R=1$，修正指数范数至多一；
每个实际幂 $174-6j\ge6$，故 $\|G_{178}\|_R\le R^6$。
因此其 Newton 系数 $a_h$ 满足
$$
v_p(a_h)\ge\left\lceil\frac{h(p-1)+6}{2p}\right\rceil,\quad
J_{178,p}\in pv\,\mathbf Z_p\langle v\rangle,\quad
J_{0,p}\in1+p\mathbf Z_p\langle v\rangle.
\tag{38}
$$
两者在 $|v|_p<p^{(p-1)/(2p)}$ 解析。
有限 Gaussian 卷积准确给所有整数 $k\ge0$
$$
J_{178,p}(k)=k!(178c)^{-k}\alpha_{dk},\qquad
J_{0,p}(k)=k!(2c)^{-k}\beta_{dk}.
\tag{39}
$$
所以每个 $\beta_{dk}$ 非零。物理曲线的 Gaussian 为
$c_{89,p}=\theta^dc$；把 (27) 与 Gaussian 同时运输后，
$$
J_{\Phi_{89},p}=89^{-1}J_{178,p}.
\tag{40}
$$
所有 $\theta^{dh}$ 准确相消，不能只运输 Taylor 系数。

因为 $6\mid p+1$，存在相容单位 $\theta\in\mathcal O^\times$、
$\theta^6=89$，并有整模型、形式群、完整 CM Tate 格同构
$$
F_\theta:E_1\longrightarrow E_{89},\quad
(X,Y)\mapsto(\theta^2X,\theta^3Y),\qquad
F_\theta^*\omega_{89}=\theta^{-1}\omega_1.
\tag{41}
$$
$\psi_{89}/\psi_1$ 是有限六次角色。
当 $d\mid m$ 时，其有限部分与 $p$ 处 tame 部分都消掉，两个高权特化使用同一反圆分角色。固定原始参数 $q_{\rm ac}\in1+p\mathcal O$、
$v_p(q_{\rm ac}-1)=1$，则
$$
x_m=q_{\rm ac}^m-1,\qquad v_p(x_{dk})=1+v_p(k).
\tag{42}
$$

BKO21 的局部 Rubin 定理与 BKO24 §2.2.1 给完整整分解
$M_j=M_j^+\oplus M_j^-$、$M_j^\pm\simeq\mathcal O[[T]]$，
$j=1,89$；(41) 与限制、corestriction、dual exponential 相容。
两原曲线根数均正，标准椭圆单位类均在正号格。参考原值
$L(E_1,1)/\varpi_1=(1-\omega)/6$ 为当前单位。
由 BKO24 Corollary4.11(i) 的证明，参考类 $\xi_1$ 是该格的整基，
所以唯一存在
$$
F_\theta^*\xi_{89}=\mathcal A_{89,p}(T)\xi_1,\qquad
\mathcal A_{89,p}\in\mathcal O[[T]],\quad
\mathcal A_{89,p}\ne0.
\tag{43}
$$
非零与特征理想由 BKO21 给出；新射线下降次数7920和扭转次数6均与 $p$ 互素。这里使用完整格，不是删有限模后的伪同构。

混合权比较与 R303、R820 相同，但新输入逐项支付如下。两条路径都从同一 primitive 射线椭圆单位给
$T_j^{-(2m+1)}(1+m)$ 和
$\psi_j^{-(2m+1)}\chi_{\rm cyc}^{1+m}$。
在原 CM 基、Tate 基下，它们都是
$\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}$；
norm、twist、特化与局部化交换。Kato 的两张 §15.11 定义性 period 图和 (15.16.1) 比较的是这个实际秩一张量，不需一般高权 motivic 相容性。

- Primitive 导子分别为 $(2\delta89)$、$(2\delta)$；(5) 的所有坏位值与下降次数7920完整保留。
- 可取惰性辅助素数 $\ell\equiv1\bmod p$、$\ell\nmid178p$；两曲线在 $(\ell)$ 的 Hecke 值均为 $-\ell$，辅助除数 $\ell^2+\ell^{-1}\equiv2\bmod p$ 为单位。
- 真微分张量 (41) 贡献 $\theta^{-(2m+1)}$；全部 CM 张量在秩一格上作，没有对称幂阶乘分母。
- 共同临界 Tate/Gamma 规范为 $(i\sqrt3)^m m!$。可能非单位的 $m!$ 只在两曲线的比中消去。
- 两个惰性好位 Euler 因子均为 $1+1/p$，赋值为 $-1$，也只在比中消去。参考曲线在89处的好 Euler 因子是 $90/89$，在当前为单位；没有为共用射线模数人为删掉它。

因此原相对 period 比较严格给
$$
v_p\mathcal A_{89,p}(x_m)
=v_p\mathscr E_{89,m}-v_p\mathscr E_{1,m},
\qquad m>0,\ d\mid m.
\tag{44}
$$
只用每权准确赋值，不假设剩余单位随权解析。
参考平方 $\mathscr E_{1,m}=(6s_0)^{-1}2^{-m}\beta_m^2$ 与 (28) 给
$$
\frac{\mathscr E_{89,m}}{\mathscr E_{1,m}}
=6\kappa_{89}\,89^{-2}\theta^{2m}89^{-m}
 \left(\frac{\alpha_m}{\beta_m}\right)^2.
\tag{45}
$$
在 $m=dk$ 时，(39) 给
$\alpha_{dk}/\beta_{dk}=89^kJ_{178,p}(k)/J_{0,p}(k)$，
故
$$
v_p\mathcal A_{89,p}(x_{dk})
=v_p(\kappa_{89})+2v_pJ_{178,p}(k).
\tag{46}
$$
若 $J_{178,p}$ 恒零，非零 $\mathcal A_{89,p}$ 在
$x_{dp^n}\to0$ 无穷点上零，矛盾。
令 $e=\operatorname{ord}_0J_{178,p}$、
$j_e=[v^e]J_{178,p}$。沿 $k=p^n$ 比较首项赋值中 $n$ 的系数和常数，准确得到
$$
\operatorname{ord}_0\mathcal A_{89,p}=2e,\qquad
v_p([T^{2e}]\mathcal A_{89,p})
=v_p(\kappa_{89})+2v_p(j_e)-2e.
\tag{47}
$$
固定 $\kappa_{89}$ 的实际赋值全保。

BKO21 Theorems6.1–6.2 在正根数 CM 曲线上给基层完整通常 Selmer 界
$$
\operatorname{corank}_{\mathcal O}
\operatorname{Sel}_{p^\infty}(E_{89}/K)
\le\operatorname{ord}_0\mathcal A_{89,p}.
$$
平凡角色属于正号分支，没有相反符号的一维附加项。
用第6节同一二次特征分解、三同源，把左边准确识别为 $r+r_p$。
故
$$
J_{178,p}\ne0,\qquad r+r_p\le2\operatorname{ord}_0J_{178,p},
$$
$$
J'_{178,p}(0)\ne0\quad\Longrightarrow\quad
r=2,\qquad\Sha(E_{89}/\mathbf Q)[p^\infty]\text{ 有限}.
\tag{48}
$$
这不假设 $p$-adic 高度非退化，不删除严格局部核。
余秩零推出有限使用通常 Selmer 及其 Sha 商的有限余生成性。

## 8. 同一实际角函数、真归一化成本与第五原中央

沿 R821 置
$$
w=z^6,\quad t=-x^{-3},\quad\Theta=x\sigma^2,\quad
d=1+8t,\quad \mathfrak a=t(t-1)(7+4t+16t^2).
$$
新来源的完整角式为
$$
W_1=\Theta^{89}f_W(t),\qquad
f_W(t)=\sum_{j=0}^{28}c_j(-t)^{29-j}.
\tag{49}
$$
第12节从原 CM 算子重生系数后作精确除法，得到
$$
\mathfrak a\mid f_W,\quad
\operatorname{ord}_{t=0}f_W=1,\quad
\deg f_W=29,\quad\deg(f_W/\mathfrak a)=25.
\tag{50}
$$
它还给 $P_{28}$ 被原 $S_{34}$ 的 $X$ 多项式整除，商次数24；
故 $W_1=S_{34}H_{144}$，其中 $H_{144}$ 为质量一的完整全纯截面。
中央不是乘法泛函，这个等式不把 $J'_S=0$ 传播为 $J'_W=0$。
第五中央的授权是第1–7节。

旧 R473 归一化的准确分次是
$$
B_m=\vartheta^m\mathfrak a^{\lceil m/68\rceil}
 R[t]_{\le\lfloor11m/34\rfloor-4\lceil m/68\rceil}.
\tag{51}
$$
在同一形式角坐标中，(49) **不属于 $B_{89}$**：
(51) 要求 $\mathfrak a^2$，而其 $t=0$ 重数仅一；
且允许最大角次数28，小于实际29。
然而 $S_{34}W_1\in B_{106}$：乘积含 $\mathfrak a^2$，角次数34，
正好满足 $\lfloor11\cdot106/34\rfloor=34$。
所以 R473 的旧权10980导子给
$$
c_{\rm old}S_{34}W_1\in A_{11086}.
\tag{52}
$$
这是支付额外 $S_{34}$ 后的整来源返回；没有给这个乘积新的中央零。
若要扩大原来源环，其新归一化和导子必须另证。
以下五轴必要系统只用原 Hurwitz 来源，不要求把 $W$ 免费放入 (51)。

固定同一个
$$
\kappa=34[z^{p+1}]\log(\sigma/z)+\Delta,\quad
\Delta\in\mathcal O,\quad a_p=p\kappa\in\mathcal O^\times,\quad
g=d\Theta^{17}e^{-\kappa w^s}.
\tag{53}
$$
五个相对 charge 是
$$
(q_S,q_T,q_U,q_V,q_W)=(1,36/17,4,33/17,89/17).
$$
置 $\widehat\nu=(g/d)^{q_\nu}f_\nu(t)$，并用
$(q_\nu\kappa)^{-h}[w^{hs}]\widehat\nu$ 定义完整 Newton 函数 $J_\nu$。
对新源，$q_W\kappa=178c+q_W\Delta$。
R342 的整 Gaussian 重标使整个 Newton 函数只乘一个
$(1+p\mathcal O)^v$ 单位指数；因原质量零，中心导数准确不变。
结合 (40)、(48)，$J'_W(0)\ne0$ 确实控制固定 $E_{89}$ 的全部 Sha 初级商。

## 9. 五实际高轴、完整尾与模 $p^5$ 唯一必要值

R434 给原角系数
$$
\log\Theta^{17}=\sum_{n\ge1}\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n}.
$$
对 $r=1,\ldots,5$，固定真实值
$$
A_r^*=\ell_{s-r}
 +(-1)^{s-r+1}\frac{8^{s-r}}{s-r}\in\mathcal O.
\tag{54}
$$
这些是原 $\log g$ 的实际 $t^{s-r}$ 系数；Gaussian 从 $t^s$ 才开始。
显示分母为单位。保留 $8^{s-r}$ 的全精度，不把实际 Fermat 商进位换成剩余类。

从原 $\log g$ 准确删去这五项得唯一 $g_\circ$。
对计算参数 $A=(A_5,\ldots,A_1)$ 令
$$
h_A(t)=\sum_{r=1}^5 A_rt^{s-r},\quad g_A=g_\circ e^{h_A},\quad
h_A(w)=w^{s-5}(P_4(w)+w^5H_A(w)),
$$
$$
P_4=u_0+u_1w+\cdots+u_4w^4.
\tag{55}
$$
$H_A$ 是确定的完整高尾。若 $\mathcal T(w)=-t/w$，则
$$
u_j=\sum_{\substack{1\le r\le5\\5-r\le j}}
 A_r(-1)^{s-r}[w^{j-5+r}]\mathcal T(w)^{s-r}.
\tag{56}
$$
这是整三角可逆换基，对角为 $(-1)^{s-5},\ldots,(-1)^{s-1}$，
行列式为 $\pm1$。只有 $A=A^*$ 恢复原算术对象，五个参数不是五条新曲线。

令 $\widehat\nu_\circ=(g_\circ/d)^{q_\nu}f_\nu(t)$。对 $1\le h\le6$ 定义真正系数多项式
$$
C_{\nu,h}(u)=[w^{hs}]\widehat\nu_\circ
 \sum_{m=0}^{h}\frac{q_\nu^m}{m!}h_A(w)^m.
\tag{57}
$$
因为 $1+(h+1)(s-5)>hs$（$s>35,h\le6$），更高指数项不进入该权；
(57) 保整个 $H_A$，次数至多 $h$。

这里需要比“多留一权”更强的尾证明。R602 的 Hurwitz 代数封闭于乘法、单位逆和零常数指数。新来源逐项满足
$$
\frac{W_1e^{-178cw^s}}w
=\sum_{j=0}^{28}c_jw^{28-j}\mathcal W^{2+3j}
 e^{178(\log(\sigma/z)-cw^s)}\in\mathscr H_{\mathcal O}.
\tag{58}
$$
所有 $w$ 幂非负；其余四源已由 R821 支付。
$t=-w\mathcal W^{-3}$ 与所有整参数扰动也属于同一 Hurwitz 代数。
严格圆盘上，扰动范数的赋值至少
$(p-29)/(2p)>1/(p-1)$，故指数及逆真实收敛、范数一，仍有来源范数至多 $R^6$。
于是 R602 的统一尾界对整个参数 family 成立：
$$
v_p(J'_\nu-L_{\nu,H})\ge
\left\lceil\frac{(H+1)(5p-7)+6}{6(p-1)}\right\rceil+v_p(H!).
\tag{59}
$$
取 $H=6$，右边为6。直接取 $H=5$ 只得5，尚不足归一后的模 $p^5$。

再付第六权本身。R614 的原 addition 整窗给
$\mathcal W$ 及 $(\sigma/z)e^{-cw^s}$ 在 $w$ 次数
$<(p^2-1)/6$ 全整。由 (58)，原 regularized 来源除以 $w$ 后直到 $w^p$ 全整。
扰动从 $w^{s-5}$ 开始，而 $7(s-5)>p$；故到 $w^p$ 的指数只用 $0!,\ldots,6!$，全为单位。
所以所有 (57) 在 $h\le6$ 都是整系数多项式，特别
$C_{\nu,6}\in\mathcal O[u]$。
其原 Newton 导数项有因子 $p^6$，与 (59) 合并后，全部 $h\ge6$ 在 $J'_\nu$ 中属于 $p^6\mathcal O$。
这才得到准确五权式
$$
F_\nu(u):=\sum_{h=1}^{5}
 \frac{(-1)^{h-1}(h-1)!\,p^{h-1}}
 {q_\nu^h a_p^{h-1}}C_{\nu,h}(u)
\equiv\frac{a_p}{p}J'_\nu(0)\pmod{p^5}.
\tag{60}
$$
并有
$$
F_\nu\in\mathcal O[u_0,\ldots,u_4],\qquad
F_\nu-C_{\nu,1}/q_\nu\in p\mathcal O[u_0,\ldots,u_4].
\tag{61}
$$
这使用真实整窗和完整无限尾，未把第六权当成普遍可删的形式项。

设 $\lambda_{\nu,j}=[w^j]\nu$，$1\le j\le5$。
参考的低五项未改变，(57) 的第一权线性部分是
$q_\nu\sum_{j=0}^4u_j\lambda_{\nu,5-j}$；质量零使 $w^sH_A$ 不进入。
故整个 Jacobian 模 $p$ 恒为固定矩阵
$$
B_5=(\lambda_{\nu,5},\lambda_{\nu,4},\lambda_{\nu,3},
 \lambda_{\nu,2},\lambda_{\nu,1})_{\nu=S,T,U,V,W}.
$$
第12节从原 $x''=6x^2$、sigma 对数和五个完整来源重建低项，得到
$$
\det B_5=
-\frac{104568614585465172496900768457847209984}
 {46188380197265625}\ne0.
\tag{62}
$$
所有低项的固定分母仅含当前已删小素数。定义明确有限坏集
$$
\mathcal B_5=\{p:p\le211\}\cup
 \{p:p\mid104568614585465172496900768457847209984\}.
\tag{63}
$$

**定理1。** 对 $p=6s-1\notin\mathcal B_5$，固定原 $g_\circ,t,a_p$，
五个 (60) 有唯一模 $p^5$ 的零点 $u^\dagger$。
若五个完整原中央导数同时零，则实际 (54)、(56) 满足
$$
u^*\equiv u^\dagger\pmod{p^5}.
\tag{64}
$$
证明先解模 $p$ 的仿射系统，再逐次以 $B_5^{-1}$ 唯一提升；(61) 保每步整性，(62) 保单位 Jacobian。形式 Hensel 解不产生新算术对象，也不使 (64) 成为完整中央零的充分条件。

若 $B_{\nu,k}=[w^{ks}]\nu$ 是未删 Gaussian 的裸系数，则同一有限卷积把实际必要条件写成
$$
\frac5{q_\nu}B_{\nu,1}
-\frac{10p}{q_\nu^2a_p}B_{\nu,2}
+\frac{20p^2}{q_\nu^3a_p^2}B_{\nu,3}
-\frac{30p^3}{q_\nu^4a_p^3}B_{\nu,4}
+\frac{24p^4}{q_\nu^5a_p^4}B_{\nu,5}
\in p^5\mathcal O.
\tag{65}
$$
系数由 $\sum_{h=k}^{5}(h-1)!/(h-k)!=(k-1)!\binom5k$ 得到。
整体整，不能先对五个裸系数分别赋零。

第五来源在89处有原始分歧六次角色，旧四源没有。
它也不是旧源的 CM 标量 pullback：相应 theta 度比在惰性素数89处为奇赋值，不可能为 $K$ 元素的范数。
这些事实排除重复倍点机制；(62) 仍不宣称五个中央的算术独立或无穷联合非零。

## 10. 旧完整来源的五块评价与真实三、四、五次折回

本节始终使用原 $W_D$、原 $P_{134}$、原公共单位和全部相对列；不把 (49) 免费加入旧列格。五块目标及其真实评价可以直接定义，存在性不由中央条数推出。

取 $1\le\ell<s-13$，$L_5=4s+\ell$，定义
$$
\Gamma_{L_5}^{(5)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^5,
 w^\ell\epsilon^4),
$$
$$
\Gamma_{L_5+13}^{(5)}
=\mathcal O[w,\epsilon]/(w^s-p\epsilon,\epsilon^5,
 w^{\ell+13}\epsilon^4).
\tag{66}
$$
物理窗口 $L_5+13<5s<p$ 在原 R324 的整窗内。
对原相对来源 $P$，记
$P_i=(\mathcal E_{\rm rel}^iP)(t(w),\vartheta_\circ(w))$，
$\vartheta_\circ=(g_\circ/d)^{1/17}$，
$\mathscr S$ 为准确的 $s$ 阶系数移位。
完整五块评价的第 $r$ 块为
$$
J_{5,\circ}(P)_r=
\left[\sum_{i=0}^r
 \frac{a_p^i}{i!}p^{r-i}\mathscr S^{r-i}P_i\right]_{<m_r},
\quad
m_0=m_1=m_2=m_3=s,\quad m_4=\ell.
\tag{67}
$$
这保留所有真实第四次 Euler 行，未增加自由目标参数。

原物理评价是
$$
M_\circ^{\rm orig}=c_*U_{0,\circ}\,m_{13}J_{5,\circ}.
\tag{68}
$$
乘 $w^{13}$ 的四条跨界带，源下标分别为
$js-13,\ldots,js-1$，$j=1,2,3,4$；
每个坐标乘一个 $p$。最后部分块不跨界。
因此固定 Smith 成本为52，最前十三个自由目标方向仍保留；
同一来源格在任意精度的核长度差介于0和52。
不能沿用四块成本39。

令 $K_A=P_4+w^5H_A$，原每列总 charge 为
$\mathcal E_{\rm tot}=\mathcal E_{\rm rel}+40$。
完整参数运输在 (66) 中准确为
$$
\begin{aligned}
M_A^{\rm orig}=c_*U_{0,\circ}\bigg\{&
 w^{13}J_{5,\circ}
 +p\epsilon w^8K_AJ_{5,\circ}\mathcal E_{\rm tot}\\
&+\frac{p^2\epsilon^2}{2}w^3K_A^2
 J_{5,\circ}\mathcal E_{\rm tot}^2\\
&+\frac{p^2\epsilon^2}{6}w^{s-2}K_A^3
 J_{5,\circ}\mathcal E_{\rm tot}^3\\
&+\frac{p^3\epsilon^3}{24}w^{s-7}K_A^4
 J_{5,\circ}\mathcal E_{\rm tot}^4\\
&+\frac{p^4\epsilon^4}{120}w^{s-12}K_A^5
 J_{5,\circ}\mathcal E_{\rm tot}^5
\bigg\}\pmod{p^5}.
\end{aligned}
\tag{69}
$$
所有乘积都在同一完整目标中继续按 $w^s=p\epsilon$ 折回，
各 $J$ 保所需全部前缀，$U_{0,\circ}$ 保整个原单位。

证明逐列展开 $w^{13}e^{Qh_A}$。
指数第 $j$ 项的首 $w$ 次数是 $13+j(s-5)$。
$j=0,1,2$ 给前缀 $w^{13},p\epsilon w^8,p^2\epsilon^2w^3$。
但后三个准确是
$$
w^{3s-2}=p^2\epsilon^2w^{s-2},\quad
w^{4s-7}=p^3\epsilon^3w^{s-7},\quad
w^{5s-12}=p^4\epsilon^4w^{s-12}.
\tag{70}
$$
不能先写成带负 $w$ 幂的 $\epsilon^3,\epsilon^4,\epsilon^5$ 项再截断。
$j\ge6$ 的首阶至少 $6s-17>5s$，才真正消失。
因为 $H_A$ 从 $K_A$ 的 $w^5$ 部分开始，(69) 的后三项都可能读取它；
尤其末项的最大允许剩余次数可达10，仍可能含两个高尾因子。
这证明 (69) 包括完整边界情形。

立即有 $\bar M_A=\bar M_\circ$，且
$M_A\bmod p^5$ 至多依赖 $u\bmod p^4$：
最低非恒定项已有一个 $p$。
定理1的第五位必要值不能仅因未进入这个矩阵就算成第五深核。

为显示首提升真正落在哪些行，将同一完整参考列写成
$w^{13}A_\Phi(w)e_4(Q_\Phi a_p\epsilon)$，
其中 $e_4$ 是四次截断指数，$A_\Phi$ 含原公共单位和 $P_{134}$。
对真实首核向量 $P$ 置
$$
W_j(P)=\sum_\Phi P_\Phi Q_\Phi^jA_\Phi(w).
$$
整个原 $M$ 的首核条件给
$$
W_0,W_1,W_2,W_3\in w^{s-13}k[[w]],\qquad
W_4\in w^\ell k[[w]].
\tag{71}
$$
定义 $d_{j,i}=[w^{s-13+i}]W_j$（$j=1,2,3$）、
$d_{4,i}=[w^{\ell+i}]W_4$，$0\le i\le4$，负下标置零。
在同一完整首余核中，Bockstein 变化准确为
$$
\begin{aligned}
(\beta_1^A-\beta_1^\circ)(P)=\bigg[
\sum_{i,k=0}^4 u_k\big(&d_{1,i-k}\epsilon w^{s-5+i}
+a_pd_{2,i-k}\epsilon^2w^{s-5+i}\\
&+\frac{a_p^2}{2}d_{3,i-k}\epsilon^3w^{s-5+i}
+\frac{a_p^3}{6}d_{4,i-k}\epsilon^4w^{\ell+8+i}
\big)\bigg].
\end{aligned}
\tag{72}
$$
方括号商去同一个 $\operatorname{im}\bar M$。
这是 (69) 除 $p$ 再模 $p$ 的一次项；$H_A$ 部分只有在使用 (71) 后才消失。
二十个实际尾位置是
$$
\begin{split}
&2s-5,\ldots,2s-1;\quad
3s-5,\ldots,3s-1;\quad
4s-5,\ldots,4s-1;\\
&L_5+8,\ldots,L_5+12.
\end{split}
\tag{73}
$$
这些由同一个 $P$ 决定，不是二十个自由源或已知非零余核类。
后续提升必须继续用整个 (69)。

## 11. 新输入真正改变的门及保留的全核问题

**定理2。** 原四条中央之外，第五条真实 $E_{89}$ 中央为同一实际角函数增加 (60) 的第五行，固定低 jet 矩阵从 $B_4$ 扩为单位 $B_5$；
若五条原中央都零，五个确定实际高系数必须满足 (64)。
这些条件对旧 $W_D$ 的具体作用是 (69)、(72)，包括全部52跨界成本。

这使原零估计可以使用五个实际高轴和四条满长块，但没有证明同预算来源中存在一个可提升的五次幂首核。若同一原格另有
$$
\bar P=t^rF^5Q,\qquad F(0,1)=0,\quad
(\mathcal E_{\rm rel}F)(0,1)Q(0,1)\ne0,\quad
h=\operatorname{ord}_wF(t(w),\bar\vartheta(w))>0,
$$
则其 Euler 阶准确是 $r+(5-i)h$，$0\le i\le4$，故相对评价 (67) 给
$$
\bar P\in\ker\bar J_5
\quad\Longleftrightarrow\quad
r+2h\ge s,\qquad r+h\ge\ell.
\tag{74}
$$
证明只用显示非零首项 $5,20,60,120$，它们在当前均为单位；
含 $\mathcal E Q$ 的项有更高 $F$ 次数。
(74) 只判一个真实已存在的来源，不证明全部首核都被 $F^5$ 整除，
更不提供同格 $p^2,\ldots,p^5$ 修正。
实际物理 $w^{13}$ 与各页余像仍须用 (68)–(73) 保留。

旧 [一般块数的纯幂预算](../notes/2026-11-15-general-central-blocks-and-pure-power-multiplicity-budget.md) 已排除单靠增加固定纯幂重数越过严格全次数门的做法；
本篇不重算该已登记结论。
新来源可用于旧列的指定后页障碍，也可在支付 (51) 外的新归一化后用于扩大来源环。
本篇已付的是第五合法算术输入、五轴唯一必要系统及其完整旧列运输；五条原中央的跨素数联合非零、或由这些实际值排除全部相容修正，仍须继续证明。

## 12. 公开精确运行与可重现来源

全部数学执行都在公开 GitHub Actions 中进行。没有保存 CM 矩阵、系数表、低 jet 表或日志数据；以下仅保存脚本、参数、run 和 hash。

### 12.1 完整30维 CM 源

脚本：[check-r943-degree178-full-cm-source.py](../scripts/check-r943-degree178-full-cm-source.py)，参数为 --workers=4，Python3、python-flint0.9.0。原依赖为 R732 norm13 与 R464 norm7 全 fiber producer。实际结果是第5节的共同核一维、首阶六、固定分母91及全部原相位核验通过。

- Source commit：ab5d8cefd5ccfc294ebf85408e539a4565b3362f。
- Run：45764784007；job：139722963336；成功完成时间2026-11-26 05:56:37 UTC。
- Script SHA256：b5c2e3f6781e1a788e2d3fd749f10e2ecab9e6c58e2950aecc9acf727f237e67。
- Stdout：2915 bytes；SHA256：bf8fb4b3536157c8ec802ee81050c9f40bbc81edbe483fda972836e44fa5b2e0。
- 完整job日志，按工具返回UTF-8保BOM口径：16132 bytes；SHA256：77459e236b632c74b6f3c6f821052692c259b0dad4bcc18a5a84089b6f5fa06e。
- 两个完整矩阵的 canonical JSON SHA256：6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665。
- R732 依赖 SHA256：d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469。
- R464 依赖 SHA256：b3e11a9da1b28a7623d86acf944262ab23c2d1969b1f0183030a4d1c96b5f1ff。

### 12.2 真第五低 jet、有限89范数与角帽

脚本：[check-r943-original-degree178-fifth-axis.py](../scripts/check-r943-original-degree178-fifth-axis.py)，无参数，Python3、python-flint0.9.0。该 reader 在同一 run 的内存中以 --workers=4 重生12.1的完整算子，核同一矩阵 SHA 后读取唯一归一线；不把此前输出29项作为硬编码输入，不落中间数据文件。

它由实际 differential recurrence 重建五来源低 jet，核原 $B_4$ 锚并得到 (62)，在 $\mathbf F_{89^2}$ 精确得到 (13) 的 $c_{\rm loc}=5$，并核 (50)–(52) 的真角帽。重复原 CM producer 只为生成本次新检验输入，不登记成新结论。

- Source commit：2063772449e2208962076fd740b714a7b2ad2bb8。
- Run：45766655437；job：139729057126；成功完成时间2026-11-26 06:13:33 UTC。
- Script SHA256：c4226727954c4f5fc8477bb17987a49242ef73103049ff7de8e004d442698ec6。
- Stdout：1996 bytes；SHA256：48a39280ed06fd2e8579da8df6815287c68cfdd59b294d6e396ce83474f0e949。
- 完整 job log，按工具返回的 UTF-8、保 BOM 口径：15034 bytes；SHA256：22cb81d7e811e3cc1d71dcdec8af241ac96de4b5fef7639511855675ae6b5137。

第6–11节的通常 Selmer、无限尾、参数整性和真实 carry 是本文统一证明，不能由有限矩阵运行或低项表代替。

## 文献与已证规范依赖

1. J. H. Silverman、K. E. Stange，*Amicable pairs and aliquot cycles for elliptic curves*，Experimental Mathematics20 (2011)，329–357，§6、Theorem19 的六次剩余公式；[全文](https://arxiv.org/pdf/0912.1831)。
2. T. Yang，*Theta liftings and Hecke L-functions*，J. Reine Angew. Math.485 (1997)，25–53，Theorem1.11、Theorems2.6/2.15；[全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
3. T. Yang，*Eigenfunctions of the Weil representation of unitary group of one variable*，Trans. Amer. Math. Soc.350 (1998)，2393–2407，完整有限环面分解；[全文](https://people.math.wisc.edu/~tonghaiyang/lattice.pdf)。
4. T. Yang，*Nonvanishing of central Hecke L-values and rank of certain elliptic curves*，Compositio Math.117 (1999)，337–359，Propositions1.2、1.5(1)；[全文](https://people.math.wisc.edu/~tonghaiyang/rank.pdf)。
5. K. Rubin，*Elliptic curves with complex multiplication and the conjecture of Birch and Swinnerton-Dyer*，Invent. Math.64 (1981)，455–470，Corollary2.2；只用非零复中央值推出秩零。
6. A. Agboola、B. Howard，*Anticyclotomic Iwasawa theory of CM elliptic curves*，Ann. Inst. Fourier56 (2006)，1001–1048，Theorem2.4.17(1)(b),(c)；[全文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
7. A. Burungale、S. Kobayashi、K. Ota，*Rubin's conjecture on local units in the anticyclotomic tower at inert primes*，Annals194 (2021)，943–966，Theorems2.1、6.1、6.2；[出版页](https://annals.math.princeton.edu/2021/194-3/p08)。
8. 同三位作者，*p-adic L-functions and rational points on CM elliptic curves at inert primes*，JIMJ23 (2024)，1417–1460，§2.2.1、Proposition3.1、Corollary4.11(i) 的证明；[全文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
9. K. Kato，*p-adic Hodge theory and values of zeta functions of modular forms*，Astérisque295 (2004)，117–290，Theorem12.5(1)、§15.8、§15.11 两张定义性 period 图、(15.16.1)；本篇只用 R303 已完整证明的同类特化路径；[全文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。

仓库内实际规范：

- [R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)：原局部 Schwartz、绝对 CM fiber、完整 Heisenberg 比较。
- [R816](R816-original-minus-eleven-rank-two-schwartz-and-degree66-source.md)、[R820](R820-original-minus-eleven-full-central-and-selmer-bridges.md)：原不同 primitive 导子的完整角色、Hermite尺度、通常 Selmer 比较范式；本篇已逐项支付89处新输入。
- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、[R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、[R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)：实际首分母、严格解析、同椭圆单位混合权及整 Gaussian 重标。
- [R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)、[R469](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)：原 Katz 平方、两种约化的完整通常 Selmer。
- [R473](R473-three-source-function-field-normalization-and-integral-conductor.md)、[R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)、[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：真角帽和导子、Hurwitz 全尾及原 addition 整窗。
- [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)：四原来源、共同参数、旧完整公共单位、真实 charge 和首余核；本篇增加第五源及五轴/五块具体证明，没有重登记旧四轴结论。
