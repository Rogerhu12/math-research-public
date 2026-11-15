# R816 — 原 E−11 的秩二下界、完整 Schwartz 与唯一 degree66 来源

日期：2026-11-15。**状态：本篇所列秩下界、完整 Hecke 角色、绝对局部 Schwartz、全权平方与原 S66 截面识别已证明。** 尚未把这个新来源与原 S34/T72/U136 的全部高轴、十三个 carry 合成第四条独立的原模条件；这一后续任务不由本篇的零质量自动完成。

固定曲线是
$$
E_-:\quad y^2=x^3-11.
\tag{1}
$$
它不是旧 S34 的倍点，也不是 R812 的同来源重基。所需新坏位是11，三处实际导子提高到 $\delta^2$。其真实原 theta 来源为标准 $S_{66}$，不能只由 $|{-11}|$ 猜成 $S_{22}$。

## 1. 两个有理点与严格秩下界

取
$$
P=(3,4),\qquad Q=(15,58).
\tag{2}
$$
两式 $4^2=3^3-11$、$58^2=15^3-11$ 直接验证它们在 (1) 上。

对好奇素数 $\ell$，若 $r^3=11$ 于 $\mathbf F_\ell$，点 $(r,0)$ 是约化曲线的有理二挠点。标准二下降同态为
$$
d_r:E_-(\mathbf F_\ell)\longrightarrow
 \mathbf F_\ell^\times/\mathbf F_\ell^{\times2},\qquad
d_r(T)=x(T)-r,
\tag{3}
$$
在 $O$、$(r,0)$ 处分别取 $1$、$3r^2$。该同态杀掉 $2E_-(\mathbf F_\ell)$；也可用函数 $x-r$ 的除子 $2[(r,0)]-2[O]$ 证明。

在 $\ell=5,r=1$ 和 $\ell=17,r=12$，两个有理点的平方类为
$$
\begin{array}{c|cc}
 &P&Q\\ \hline
(5,1)&2\quad\text{非平方}&4\quad\text{平方}\\
(17,12)&8\quad\text{平方}&3\quad\text{非平方}.
\end{array}
\tag{4}
$$
其中 $12^3\equiv11\pmod {17}$。两处均好约化，因此 (4) 定义在 $E_-(\mathbf Q)/2E_-(\mathbf Q)$ 上的两列独立，给其维数至少二。
又 $E_-(\mathbf Q)[2]=0$，因为 $x^3=11$ 无有理根。由 Mordell–Weil 有限生成，有限扭群的模二商维数等于其二挠维数，故这里
$$
\dim_{\mathbf F_2}E_-(\mathbf Q)/2E_-(\mathbf Q)
=\operatorname{rank}E_-(\mathbf Q).
$$
于是严格得到
$$
\boxed{\operatorname{rank}E_-(\mathbf Q)\ge2.}
\tag{5}
$$
没有使用数据库秩、解析数值或 Sha 有限性。

短整模型的判别式为 $-432\cdot11^2$。Tate 算法的三个坏位是
$$
\begin{array}{c|c|c|c}
\ell&v_\ell(\Delta_{\min})&\text{Kodaira 型}&f_\ell\\ \hline
2&4&\mathrm{IV}&2\\
3&3&\mathrm{II}&3\\
11&2&\mathrm{II}&2.
\end{array}
\tag{6}
$$
在2处用 $y=Y+1$ 得 $Y^2+2Y=X^3-12$，IV 步的多项式为
$T^2+T+1$；在3处用 $x=X-1$ 得 $Y^2=X^3-3X^2+3X-12$，
$v_3(a_6)=1$；11处原短模型已给 II。各判别式赋值小于12，
不能再整降；Ogg 公式给表中导子指数。因此
$$
N(E_-)=2^2\,3^3\,11^2=13068.
\tag{7}
$$

## 2. 全部 Hecke 角色及三个坏位

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad\delta^2=-3,\quad\operatorname{Im}\delta>0.
$$
设 $\psi_-=\psi_{-11}$ 为 (1) 的解析 CM type 代数 Hecke 角色，
$\chi=\psi_-|\cdot|_K^{-1/2}$ 为 Yang 的 unitary 规范。
加性角色与 R290 相同：
$$
\psi_{\mathrm{add},\infty}(x)=e^{2\pi ix},\qquad
\psi_{\mathrm{add},\ell}(x)=e^{-2\pi i\{x\}_\ell},\qquad
\psi_{K,\ell}=\psi_{\mathrm{add},\ell}\circ\operatorname{Tr}.
\tag{8}
$$
特别 $\chi_\infty(z)=(z/|z|)^{-1}$。

Silverman–Stange 的实际六次剩余公式给
$$
\psi_D(\mathfrak l)
=-\left(\frac{4D}{\mathfrak l}\right)_6^{-1}\pi,\quad
\pi\equiv2\pmod3,\qquad
\frac{\psi_-}{\psi_1}(\mathfrak l)
=\left(\frac{-11}{\mathfrak l}\right)_6^{-1}.
\tag{9}
$$
这里的理想角色与 idèle 单位角色方向相反。完整本地表为
$$
\begin{array}{c|c|c|c}
v&\chi_v\text{ 在单位上}&\text{uniformizer 值}&a(\chi_v)\\ \hline
2&\operatorname{Teich}_{\mu_3}(u\bmod2)&\chi_2(2)=-1&1\\
3&\chi_3(\epsilon\omega^a)=\epsilon\omega^a
 &\chi_3(\delta)=+i&2\\
11&(u\bmod11)^{20}\in\mu_6\subset\mathbf F_{121}^{\times}
 &\chi_{11}(11)=-1&1.
\end{array}
\tag{10}
$$
三处单位在模 $\delta^2$ 后唯一写成 $\epsilon\omega^a$。

首先，$-11$ 在 $K_2$ 是六次幂：$11/3\equiv1\pmod8$ 有
$\mathbf Q_2$ 平方根，故 $-11=\delta^2(11/3)$ 在 $K_2$ 有
平方根，其剩余类为1；立方映射在相应 pro-2 单位群上是同构。
所以二处与 $E_1$ 完全相同。11处 (9) 的 tame Kummer 计算给
idèle 单位角色 $u^{(121-1)/6}=u^{20}$，并非它的逆。
CM 导子–有理导子公式与 (7) 给三处精确指数2；而
$\mu_6\to(\mathcal O_K/\delta^2)^\times$ 是同构，主单位乘积
便确定它的全部单位角色。

具体地，$\chi_{11}(\omega)=\omega^2$、$\chi_{11}(\delta)=1$、
$\chi_2(\omega)=\omega$、$\chi_2(\delta)=1$。全局 $\omega,-1,\delta$
的乘积关系分别给三处的 $\omega$、符号及 $+i$。再用有理元2、
11确定两处 uniformizer 值。这包括所有单位、uniformizer 和
无穷角色，不是由两个好素数的迹猜角色。实际 primitive 导子为
$$
\boxed{\mathfrak f=(2\delta^2\cdot11)=(66),\qquad
 \operatorname N\mathfrak f=4356.}
\tag{11}
$$
其射线类次数准确为
$$
\#\operatorname{Cl}_K(\mathfrak f)
=\frac{(4-1)(9-3)(121-1)}6=360.
\tag{12}
$$
这记录后继下降的固定成本，不提前套用旧导子下的中央身份。

## 3. 根数与实际 Hermitian 参数

Yang 的本地 dichotomy 条件为
$$
\epsilon(1/2,\chi_v,\psi_{K,v}/2)\chi_v(\delta)
=\epsilon_{K_v/\mathbf Q_v}(\alpha).
\tag{13}
$$
二处与 R290 的原 Gauss 和完全相同，左边为 $+1$。

十一处 $\vartheta(z)=z^{20}$ 在 $\mathbf F_{11}^{\times}$ 上平凡，
$\vartheta(\delta)=1$，沿实坐标分纤维的完整和为
$$
\sum_{z\ne0}\vartheta(z)^{-1}
 e^{-2\pi i\operatorname{Tr}(z)/(2\cdot11)}
=11\vartheta(\delta)=11.
\tag{14}
$$
Tate 式中 $\chi_{11}(11)=-1$，所以 epsilon 为 $-1$，
乘 $\chi_{11}(\delta)=1$ 后仍为 $-1$。

三处 $n(\psi_K/2)=-1$、$a(\chi_3)=2$，取 $c=\delta^3$。
完整六项 Gauss 和为
$$
\sum_{u\in\mu_6}u^{-1}\,
 \psi_{\mathrm{add},3}\!\left(\operatorname{Tr}
                      \frac{u}{2\delta^3}\right)=-3.
\tag{15}
$$
若 $u=a+b\omega$，迹为 $-b/6$，加性相位为 $\omega^{2b}$，
故 (15) 是直接的六项等式。因 $\chi_3(\delta)^3=-i$，
epsilon 为 $i$；乘 $\chi_3(\delta)=i$ 后是 $-1$。
无穷处 epsilon 为 $i$、$\chi_\infty(\delta)=-i$，dichotomy
为 $+1$。各处 epsilon 的乘积因而为 $+1$，而 (13) 在
$2,3,11,\infty$ 的完整表是 $(+1,-1,-1,+1)$。

$\alpha=11$ 已代表该类。乘 $N(\delta)=3$ 后选
$$
\boxed{\alpha=33.}
\tag{16}
$$
这一代表使下述全部有限向量下降到原标准 $S_{66}$。
在 Yang 极化 $X=\mathbf Q\delta$ 上，
$$
\iota_{33}(x+y\delta)=
 \begin{pmatrix}x&297y\\-y/99&x\end{pmatrix},\qquad
\kappa_\infty=|\delta^3\alpha|=99\sqrt3.
\tag{17}
$$

## 4. 二处与三处原向量

二处令
$$
e_j=\mathbf1_{j/2+2\mathbf Z_2},\quad
f_A=e_0-e_2,\quad f_B=e_1+e_3,\quad
t_+=\frac{1+\sqrt3}{\sqrt2}.
$$
取
$$
\phi_2=f_A+t_+f_B,\qquad
v_2=(1,t_+,-1,t_+),\qquad
\|\phi_2\|^2=3+\sqrt3.
\tag{18}
$$
这不是未定的 dyadic 特征选择。$33/17\equiv1\pmod {16}$，
故存在 $c\in1+8\mathbf Z_2$ 使 $c^2=33/17$。实际
Schrödinger dilation 把 R290 的 $\iota_{17}$ 共轭到 (17)，
逐个保持上述四陪集，Jacobian为1，平方单位的 Weil 相位为1。
二处 Hecke 角色已完全相同，因此 R290 的 $\omega,-1,g_*$
全生成元验证及全部支撑直接运输为 (18)。

三处先用 R776 基角色
$\chi_3^0(\epsilon\omega^a)=\epsilon,\ \chi_3^0(\delta)=-i$。
此时
$$
n((33\delta/4)\psi_K)=-4,\qquad
L=\delta^{-2}\mathcal O_{K_3},\qquad v=\delta^{-3}.
$$
原 lattice–Schrödinger 转模的 splitting 比严格为1；
在 $(f_0,f_v,f_{-v})$ 上的绝对矩阵为
$$
W_3(\omega)=\operatorname{diag}(1,\omega,\omega),\qquad
W_3(-1)(f_0,f_v,f_{-v})=(f_0,f_{-v},f_v).
\tag{19}
$$
例如 $f_v$ 的 $\omega$ 相位为 $\psi_3(11/12)=\omega$，
与 R776 的 $29/12$ 相差三进整数。$G_2=G_3$ 在全块上平凡，
所以这两个矩阵核定整个本地环面。

odd 特征 $\tau_o(\omega)=\omega,\tau_o(-1)=-1$ 的 Hilbert90
转置 $\chi_3^0(z)\tau_o(z/\bar z)^{-1}$ 正是 (10) 的三处角色。
故真正不变函数为
$$
\boxed{\phi_3=
 \mathbf1_{\frac19+\frac13\mathbf Z_3}
-\mathbf1_{-\frac19+\frac13\mathbf Z_3},\qquad
\|\phi_3\|^2=6.}
\tag{20}
$$
两个中心向量的相位都是1，没有额外 modulation。此函数为奇；
原 $E_{17}$ 的三处球不能代替它。

## 5. 十一处有限环面的完整绝对模型

令 $\zeta=e^{2\pi i/11}$，
$G_{11}=\sum_{r\in\mathbf F_{11}}\zeta^{r^2}=i\sqrt{11}$，
取 $e_a^{(11)}=\mathbf1_{a/11+\mathbf Z_{11}}$。
对 $g=x+y\delta\in T_{11}=\mathbf F_{121}^1$、$y\ne0$，原
有限 $\mu_4$ Weil 模型为
$$
\boxed{
W(g)_{ab}=
 \frac{(\frac{9/(2y)}{11})}{G_{11}}\,
 \zeta^{\frac9{2y}\{x(a^2+b^2)-2ab\}},\quad
W(1)=I,\quad W(-1)e_a=-e_{-a}.}
\tag{21}
$$
指数在 $\mathbf F_{11}$ 读取，9是 $-\Delta(\alpha/11)$。
这由 (17)、原负有限加性角色及 Yang 的实际 lattice
intertwiner 得到；尤其 $W(-1)=-R$，不能照搬剩余特征
$1\bmod4$ 的 $+R$。有限 Gauss 合成验证全部乘法；非恒等
$g$ 的迹为 $-\tau_6(g)$，$\tau_6$ 是环面的二次角色。
所以此十一维表示恰含除 $\tau_6$ 外的每个环面角色一次。

取
$$
g_0=-3-\delta,\qquad g_0^{12}=1,\quad g_0^4=\omega.
$$
Hilbert90 的 $g=z/\bar z=z^{-10}$ 将真实单位角色 $z^{20}$
写成 $\eta(g)=g^{-2}$。Yang Proposition1.2(3) 的 quadratic
splitting 使真正的 Hecke 不变向量必须落在
$$
\tau=\tau_6\eta^{-1}=\tau_8,\qquad \tau(g_0)=\omega^2.
\tag{22}
$$
它不是被删的 $\tau_6$，故完整投影
$$
\Pi_8=\frac1{12}\sum_{k=0}^{11}\omega^k W(g_0^k)
\tag{23}
$$
恰好秩一。固定
$$
f_{11}=\Pi_8e_1,\qquad
n_{11}=\sum_a|f_{11}(a)|^2
       =\langle e_1,\Pi_8e_1\rangle>0.
\tag{24}
$$
非零是 Yang Proposition1.5(2) 的实际 odd-Schwartz 结论：
该分支所有非零陪集代表的投影均非零，其证明使用
$\zeta_{11}\mapsto\zeta_{11}^{a^2}$ 的完整 Galois 运输。
也可直接从 (21)–(23) 验证。(24) 是固定有限代数和指定的
**准确范数**，没有把它设为1。

由 $\overline{W(g)}=W(g^{-1})$，投影 (23) 的坐标为实数；
又 $\tau_8(-1)=1$ 而 $W(-1)=-R$，所以
$$
f_{11}(-a)=-f_{11}(a),\qquad
\overline{f_{11}(a)}=f_{11}(a).
\tag{25}
$$
取 $\phi_{11}=\sum_a f_{11}(a)e_a^{(11)}$。
它在整个真实 $\omega_{33,\chi_{11}}$ 下固定，范数平方为
$n_{11}$。其余有限处取原球 $\mathbf1_{\mathbf Z_\ell}$。

## 6. 原有理支撑、全部半特征和非零截面

有限张量 (18)、(20)、(24) 的有理支撑准确为 $x=n/198$。
实际坐标为
$$
2x=n/99\leftrightarrow3n\bmod4,\quad
9x=n/22\leftrightarrow n\bmod3,\quad
11x=n/18\leftrightarrow8n\bmod11.
$$
写 $v_3(0)=0,v_3(1)=1,v_3(2)=-1$，则完整原系数为
$$
\boxed{a_n=v_2(n\bmod4)v_3(n\bmod3)f_{11}(8n\bmod11).}
\tag{26}
$$
这里用了 $v_2(3n)=v_2(n)$。由 CRT、$f_{11}\ne0$，这些系数不全零。
两处奇向量的符号相乘，给
$$
a_{-n}=a_n=\overline{a_n},\qquad
a_{n+132}=a_n,\qquad
(-1)^n a_{n+66}=-a_n.
\tag{27}
$$

令 $s=(1-\omega)^{-1}$、$\Lambda=\mathbf Z+s\mathbf Z$，并设
$$
F(Z)=\sum_{n\in\mathbf Z}a_n
 \exp\!\left(\pi i\frac{\delta}{3}\frac{n^2}{132}+2\pi inZ\right).
\tag{28}
$$
实际半周期等式为
$$
F(Z+1)=F(Z),\qquad
F(Z+s)=e^{-66\pi is-132\pi iZ}F(Z).
\tag{29}
$$
所以
$$
S_{\mathrm{raw}}(Z)=e^{66\sqrt3\pi Z^2}F(Z)
 \in H^0(\mathbf C/\Lambda,\mathcal O(66[0])).
\tag{30}
$$
Fourier 系数唯一性证明它非零。(27)–(29) 包括全部半特征：
本篇得到原标准 $S_{66}$，没有遗留 flat twist，也没有从矩形格
漏掉二倍下降。

设 $\sum H_m(x)T^m/m!=e^{xT-T^2/(8\pi)}$。原 Hermite 系数为
$$
b_m=\sum_{n\in\mathbf Z}a_n
 H_m\!\left(\frac{\sqrt{99\sqrt3}}{198}n\right)
 e^{-\pi\sqrt3n^2/396}\in\mathbf R.
\tag{31}
$$
置 $h=\sqrt{99\sqrt3}/(396\pi i)$，则
$$
\mathcal B(T)=\sum b_mT^m/m!=S_{\mathrm{raw}}(hT),\qquad
66\sqrt3\pi h^2=-1/(8\pi).
\tag{32}
$$
所有有限处的真实 $\omega$ 环面作用均固定原向量。全局有理单位
的 Weil 相容与 (27) 因而给
$$
\mathcal B(T)\in\mathbf R[[T^6]].
\tag{33}
$$
这包含完整二阶、四阶消失，未以低阶样本代证明。

## 7. 全权实平方与零质量

对 $m\ge0,6\mid m$，全部坏位角色在 $\chi^{2m+1}$ 下保持 (10)：
三处 $+i$ 要求 $m$ 偶，2/11 的三次部分要求 $3\mid m$。
同一有限 Schwartz 的全范数为
$$
\mathcal N_m=
 \frac{6(3+\sqrt3)n_{11}}{\sqrt{198\sqrt3}}\,
 \frac{m!}{(4\pi)^m}.
\tag{34}
$$
Yang Theorem1.11 的非分歧二次坏位集合为 $\{2,11\}$，
没有坏分裂点。因此
$$
c(0)=(1+2^{-1})^{-1}(1+11^{-1})^{-1}=11/18.
$$
$h_K=1$，原范数一商与极大紧群的体积比仍是 $|\mu_6|=6$。
由其完整范数平方公式及 $L(1,\epsilon_K)=\pi/(3\sqrt3)$，
$$
\boxed{
L(\psi_-^{\,2m+1},m+1)
=C_-\frac{(4\pi)^m}{m!}\,b_m^2,\qquad
C_-=\frac{\pi\sqrt{198\sqrt3}}
 {33\sqrt3(3+\sqrt3)n_{11}}>0.}
\tag{35}
$$
这里保留二处范数、三处 odd 范数6、十一处完整范数和全部
uniformizer，并非模代数单位的未定平方。
因为 (31) 为实数，右边是同一个来源的实平方。

CM rank-zero 定理的方向
$L(E_-,1)\ne0\Rightarrow\operatorname{rank}E_-(\mathbf Q)=0$
与 (5) 给 $L(E_-,1)=0$。用 (35) 的 $m=0$ 得
$$
b_0=0,\qquad\operatorname{ord}_0S_{\mathrm{raw}}\ge6.
\tag{36}
$$
正六次非零将在下一节由完整算子唯一识别证明，不从正权值猜测。

## 8. 两个完整代数 CM 算子与唯一质量核

在 $b=1$、$x=z^{-2}+\cdots,y=-z^{-3}+\cdots,\sigma=z+\cdots$ 下，
原 $S_{66}$ 的 type0 完整基为
$$
e_j=\sigma^{66}X^j,\qquad X=x^3,\quad0\le j\le11.
\tag{37}
$$
其原点阶为 $66-6j$。质量行是 $\ell=(0,\ldots,0,1)$；
必须保留质量列。

取 R297 的 $\gamma_7=3+\omega,\gamma_{13}=4+\omega$ 以及
原 division 多项式 $Q_\gamma=\sigma(\gamma z)/\sigma(z)^{N\gamma}$。
同一个完整来源算子为
$$
N_\gamma=\gamma^{-1}[\gamma]_*[\bar\gamma]^*.
\tag{38}
$$
设 $x(\gamma z)=A_\gamma(x)/B_\gamma(x)$。对目标横坐标 $a$，
以 $f_a=(A_\gamma-aB_\gamma)^{\rm monic}$ 表示完整同源纤维。
输入为 $\sigma^{66}P(x)$ 时，输出除以目标 $\sigma^{66}$ 为
$$
\gamma^{-1}\operatorname{Tr}_{f_a}
 \left[(Q_{\bar\gamma}/Q_\gamma)^{66}
             P(x(\bar\gamma z))\right].
\tag{39}
$$
式 (39) 保持整个 carrier 的66次方及 division leading constant，
没有补一个自由归一标量。每个算子在 $a=1,\ldots,12$ 的十二个
全纤维求值确定 (37) 上矩阵；$a=13,14$ 的两个全纤维核验全部列。
真实 pull/trace 保持 degree66、type0，且 $(a^{3j})$ 是可逆
Vandermonde，所以这严格确定完整算子。

令 $\mathcal O_{13},\mathcal O_7$ 分别由
$\ell,\ell N_\gamma,\ldots,\ell N_\gamma^{11}$ 组成。
公开有理精确计算给
$$
\dim\ker\mathcal O_{13}=6,\qquad
\dim\ker\mathcal O_7=3,\qquad
\operatorname{rank}\binom{\mathcal O_{13}}{\mathcal O_7}=11.
\tag{40}
$$
该行空间在两个算子下已经稳定，两个矩阵严格交换。
共同核恰由一个向量生成：
$$
\begin{split}
v={}&(0,\tfrac{262144}7,\tfrac{393216}7,159744,119808,
 \tfrac{212736}7,53376,-\tfrac{7248}7,-\tfrac{18156}7,
 \tfrac{1515}7,1,0)^{\mathsf t},\\
&N_7v=-v,\qquad N_{13}v=\omega v.
\end{split}
\tag{41}
$$
全部计算在 $\mathbf Q(\omega)$ 内进行，不是辅助模数上的秩。

现在连接实际来源，而不由 (41) 猜其曲线。各坏位原 Schwartz
已经在完整紧环面上固定，因此 $\gamma/\bar\gamma$ 对应的有限
Weil 算子保持其线。(39) 在完整 Heisenberg theta 结构上实现
同一自同构；由不可约性与其非零性只差一个共同非零标量。
所以由 (10)、(18)、(20)、(22) 定义的原来源同时是
$N_7,N_{13}$ 的本征向量。它非零且质量为零，必在 (40) 的
共同核中。一维性因而识别实际来源；两个算子没有被用来代替
全部坏位角色的证明。

## 9. 确切多项式、全部缩放及角式

记 (41) 前十一项的有理系数为 $c_j$，$0\le j\le10$。
归一 $[z^6]V_1=1$ 后原来源准确为
$$
\boxed{
\begin{aligned}
V_1(z)=\frac{\sigma^{66}X}{7}\big(&7X^9+1515X^8-18156X^7-7248X^6
 +373632X^5\\
 &+212736X^4+838656X^3+1118208X^2
 +393216X+262144\big).
\end{aligned}}
\tag{42}
$$
所以 $\operatorname{ord}_0V_1=6$，其原正六次系数确实非零。
对任意非零 $b$，同一个微分规范下
$$
V_b(z)=\sigma_b^{66}\sum_{j=0}^{10}c_jb^{10-j}x_b^{3j}
      =b^{-1}V_1(b^{1/6}z),\qquad V_b(z)=z^6+O(z^{12}).
\tag{43}
$$
因为只含六次幂，右边不依赖六次根选择。目标曲线来源为
$\Phi_-=V_{-11}$；旧 $b=17$ 模型上的 $V_{17}$ 必须按 (43)
同时运输实际微分和 Gaussian，不能只替换多项式系数。

令 $\Theta_b=x_b\sigma_b^2,t=-b/x_b^3$。完整角式为
$$
V_b=b^{-1}\Theta_b^{33}f_V(t),\qquad
f_V(t)=\sum_{j=0}^{10}c_j(-t)^{11-j}.
\tag{44}
$$
例如起始项是 $-t+(1515/7)t^2$，最高项为
$(262144/7)t^{10}$。这是带完整角多项式的真实 Gaussian
charge33 来源，相对原 $S_{34}$ 的 charge 比为 $33/17$。
本篇不按该比值自动扩充旧角格或减少 carry 成本。

为显示全权常数与目标周期的接口，取
$\theta_-^6=-11$、$\Omega_-=\Omega_1/\theta_-$，
目标周期格为 $\Omega_-\Lambda$，$\varpi_-=s\Omega_-$。
$\Omega_-$ 是允许为复数的 CM 尺度，不能称为正实周期。
设
$$
S_{\rm raw}(Z)=C_{\rm raw,-}\Phi_-(\Omega_-Z),\quad
\Phi_-=\sum s_mz^m,\quad
\kappa_-=\frac{C_-C_{\rm raw,-}^2}{\Omega_-}\ne0.
$$
由 (32)、(35) 的同一 Hermite 尺度严格得到
$$
\frac{(2\pi/\sqrt3)^mL(\psi_-^{2m+1},m+1)}
     {m!\Omega_-^{2m+1}}
=\kappa_-198^{-m}s_m^2,
$$
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\psi_-^{2m+1},m+1)}
     {m!\varpi_-^{2m+1}}
=\frac{\kappa_-}{s}\,66^{-m}s_m^2
\quad(6\mid m).}
\tag{45}
$$
第二式使用 $s^{2m}=3^{-m}$。$s_6=1$ 与 (35) 给该正权值非零，
CM 临界值代数性从而给
$\kappa_-=s\,66^6\mathscr E_{-,6}\in\overline{\mathbf Q}^{\times}$。
原分析标量 $C_{\rm raw,-}$ 本身没有被无证称为代数数。

## 10. 已付范围与第四中央的剩余工作

本篇完成了固定曲线秩至少二、primitive 导子与所有局部角色、
同一有限 Schwartz 的全部权、完整实平方、标准线丛及唯一有理
原截面。它与旧三个曲线的有限角色不同。

后继若要把它用作第四个原中央，仍须：

1. 对 $\mathfrak f=(66)$ 支付普通/惰性完整通常 Selmer 与同一
   theta–Katz、signed 格桥，保 (45) 的66尺度和 $\theta_-$ 微分；
2. 在原共同 $M$、13 个 carry 及 Gaussian 下写出其真实输入行，
   核第四条是否独立并支付新固定系数格成本；
3. 区分新的中央来源与“质量为零”“新角多项式存在”。后二者
   单独不蕴含新高精度 forcing，更不证明中央导数非零。

(42) 是可用于后继的完整实际来源；未提前宣称第四个 $p^4$
条件或主目标已闭合。

## 11. 公开精确运行

算法：
[check-r816-degree66-full-cm-and-rank-two-source.py](../scripts/check-r816-degree66-full-cm-and-rank-two-source.py)。

脚本不读生成数据、不写输出文件；重用 R732/R464 原完整
division/trace 算法，重新生成 (39) 的所有纤维。
同一 CM13 纤维始终附 R297 原 S34 的 leading-constant 锚。
(40)–(42) 来自整个 $\mathbf Q(\omega)$ 矩阵行化。
完整矩阵 canonical SHA256 为
520bcf78a28289b33aa59eec418b7d8aa911f4b229397055ac684cd724f948da。

- source commit：71c2de7a0ae8c41755245b8ea073b594266f406c；
- GitHub Actions run：43754381135，job：132935145766；
- 参数：--workers=4，python-flint==0.9.0；
- script SHA256：
  da2711c1db7be0ad05ba4f005d74ba3637f4a471478185e1f1ac87e523a58ea2；
- stdout：1672 bytes，SHA256：
  9135fa563bae29d8d99aad69277081ba9a53af152001652ae32d6b93be87befe。

可重算结果只保在公开运行日志，未新增结果数据文件。

## 文献和原规范依赖

- J. H. Silverman and K. E. Stange, *Amicable pairs and aliquot cycles for
  elliptic curves*, Experimental Mathematics20 (2011),329–357，
  §6、Theorem19 证明的六次剩余公式：
  <https://arxiv.org/pdf/0912.1831>。
- T. Yang, *Theta liftings and Hecke L-functions*, J. Reine Angew. Math.485
  (1997),25–53，Theorem1.11、Theorems2.6/2.15：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- T. Yang, *Eigenfunctions of the Weil representation of unitary group of
  one variable*, Trans. Amer. Math. Soc.350 (1998),2393–2407：
  <https://people.math.wisc.edu/~tonghaiyang/lattice.pdf>。
- T. Yang, *Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*, Compositio Math.117 (1999),337–359，Proposition1.2、
  Proposition1.5(2)、Appendix(A6)–(A12)：
  <https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
- K. Rubin, *Elliptic curves with complex multiplication and the conjecture
  of Birch and Swinnerton-Dyer*, Invent. Math.64 (1981),455–470，
  Corollary2.2；这里只用非零复中央值迫秩零的方向。
- [R290 原完整 Schwartz 规范](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)。
- [R297 原 CM trace 与唯一质量核方法](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R776 三处绝对 Weil 模型](R776-original-degree174-three-primary-absolute-weil-spectrum.md)。
- [R469 第三来源完整中央桥的范围](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)。
