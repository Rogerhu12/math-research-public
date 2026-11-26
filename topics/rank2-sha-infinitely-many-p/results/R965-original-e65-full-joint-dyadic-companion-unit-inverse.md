# R965 — 原 E65 框架的完整二挠伴随算子与两态单位逆

日期：2026-11-26。**状态：已证明。**

本篇始终使用 R963 的原六 sigma 联合及同一个 $L_h$ 框架。
给出三个明确的有限 theta 群操作，只作用于五个伴随变量，满足
$$
\boxed{\Phi_h=\mathscr D\Phi_\rho,\qquad
       \Phi_\rho=-\frac43\mathscr D\Phi_h.}
\tag{1}
$$
它们可以全部取在五伴随的 $E[16]$ 上，全部中心相位由原 lift
的指定奇次幂保留；系数分母只有 $2,3$。
式(1)是整个六变量来源的身份，不是第一边际或质量身份。

算子平方最初只在下文的四维共同来源空间成立。
向原 E65 秩一投影运输时，使用它确切只动伴随这一事实；
不假设第一 CM 投影保持该四维空间。
对于一般混合 cut，本篇保持三条真实 torsion 中心的整测度积分，
不将 prime-to-$p$ torsion 写成 $\mathbf Z_p$ 上的连续字符或物理平移。

## 1. 原框架、两个完整来源及共同格

保持 R961/R963 的
$$
\delta=1+2\omega,\quad
a=7+3\omega,\quad g=3+\omega,\quad \bar g=2-\omega,
$$
以及原第一行
$$
r_h=(\delta,2\delta,a,18,g,\omega^2\bar g).
\tag{2}
$$
原整框架 $L_h$ 的完整 Gram 为
$$
L_h\bar L_h^{\,t}
=\operatorname{diag}
(390,102960,14256,11016,8976,6512)=D_L.
\tag{3}
$$
它和 $L_hH$ 都是原整矩阵，全部半特征和零 Gaussian 交叉项已经由
R963 的完整返回支付。$H$ 固定前四个输入，末二块是
$$
H=\frac12
\begin{pmatrix}\omega^2&-\delta\\2+\omega&\omega^2\end{pmatrix}.
\tag{4}
$$
记 $\rho_{\rm raw}=-\nu_\sigma^{\otimes6}/84$，
$\eta_{\rm raw}=\omega^2H_*\rho_{\rm raw}$，
$h_{\rm raw}=\eta_{\rm raw}+\rho_{\rm raw}/2$，并使用同一规范
$$
\Phi_\rho=\frac1{9a}(L_h)_*\rho_{\rm raw},\quad
\Phi_\eta=\frac1{9a}(L_h)_*\eta_{\rm raw},\quad
\Phi_h=\Phi_\eta+\frac12\Phi_\rho.
\tag{5}
$$
下文把测度及其完整生成截面用同一符号表示。

为核定原 theta 群中心，先在 $b=1$ 的复 CM 格
$\mathcal O_K=\mathbf Z[\omega]$ 上证明完整截面身份；
最后沿 R963 同一个 $b=17$ 同形变换和普通整周期返回。
记原生成变量为 $w=L_h^t z$。令
$$
J=\mathcal O_K^4\times J_2,\qquad
J_2=\{(u,v)\in\mathcal O_K^2:u\equiv\omega^2v\pmod2\}.
\tag{6}
$$
由于 $L_h,L_hH$ 都整，
$L_h^t\mathcal O_K^6\subset J$。
而 $[\mathcal O_K^6:J]=4$。

这不只是一条无相位的格关系。
原 sigma 半特征为
$$
\chi(r)=(-1)^{m+n+mn}\quad(r=m+n\omega);
\qquad \chi(0)=1,\quad
\chi(r)=-1\quad(0\ne r\bmod2).
\tag{7}
$$
如果 $(u,v)=(\omega^2v+2q,v)\in J_2$，准确有
$$
H^t(u,v)=\bigl(\omega^2(q-v),-v-\delta q\bigr).
\tag{8}
$$
原两乘积的末二半特征分别为
$\chi(\omega^2v)\chi(v)=1$ 和
$\chi(q+v)^2=1$。
因此两态在整个 $J$ 上的完整中心字符相同，都是前四个
$\chi(w_i)$ 的乘积。没有只核 torsion 点而省去 lift。

用主极化的交替型 $E$，规范 $E(1,\omega)=1$。
$J$ 的对偶格是
$$
J^\vee=\mathcal O_K^4\times
\left(\mathcal O_K^2+
\mathcal O_K\frac{(1,-\omega)}2\right).
\tag{9}
$$
它与 $J$ 的商有16元。共同字符的完整截面空间记为 $\mathcal C$。
它在原多 theta 格中的像准确为四维：
从 $J\subset\mathcal O_K^6$ 的四重覆盖作完整有限字符分解，
四项各是主极化线束的一个平移，各有一个截面。
这同时保留前四个原 sigma；$\Phi_\rho,\Phi_\eta\in\mathcal C$。
以下显式构造的四个独立向量也直接给出其完整基。

## 2. 两个真正只动伴随的有限 theta 群

令 $\mathbb F_4=\mathcal O_K/(2)$，始终用
$\{0,1,\omega,\omega^2\}$ 作标签。对标签 $r,s$ 定义原 $w$ 格中的
实际向量
$$
\begin{aligned}
u_r={}&\left(
 -3\omega^2(3+4\omega)r,\ 0,\ -(3+4\omega)r,\ 0,\
 \frac{\delta r}{2},-\frac{\omega r}{2}\right),\\
v_s={}&\left(
 -3\omega^2\bar g s,\ 0,\ -\bar g s,\ 0,\ s,\ 0\right).
\end{aligned}
\tag{10}
$$
二者都属于 $J^\vee$。其原输出平移点为
$$
t^u_r=L_h^{-t}u_r,\qquad t^v_s=L_h^{-t}v_s.
\tag{11}
$$

这些点的第一坐标准确为零。因为
$$
L_h^{-t}=D_L^{-1}\bar L_h,\qquad
\bar a-3\omega^2\delta=1,\qquad
\frac{\bar g\delta-\omega^2g}{2}=3+4\omega,
\tag{12}
$$
将(10)代入 $(\bar r_h\cdot w)/390$ 后，两式都为零。
这是整数 Bezout 修正，未只在模二意义下消去第一坐标。

记 $\mathsf T_t$ 为原 canonical theta 群 lift，保其完整中心。
在 $\mathcal C$ 上定义
$$
U_r=\chi(r)\mathsf T_{t^u_r},\qquad
V_s=\chi(s)\mathsf T_{t^v_s}.
\tag{13}
$$
$U_0=V_0=I$。以下公式都使用原 Weyl lift；
在整数交替配对时，其乘法中心为 $(-1)^{E}$，
与 R548(11) 的完整 degree4 lift 相同。

两个族在 $\mathcal C$ 上满足准确的有限群关系
$$
\begin{gathered}
U_rU_s=U_{r+s},\qquad V_rV_s=V_{r+s},\\
V_sU_r=(-1)^{b(r,s)}U_rV_s,\qquad
b(r,s)=\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}(r\bar s).
\end{gathered}
\tag{14}
$$
特别 $U_r^2=V_s^2=I$。

核(14)的所有中心如下。向量(10)的两个 Hermitian 平方分别是
$131\,r\bar r$ 和 $71\,s\bar s$，两个系数都是奇数；
其同族交替配对因而模二分别为 $b(r,s)$。
半特征满足
$\chi(r)\chi(s)=(-1)^{b(r,s)}\chi(r+s)$，恰好消去这两个同族
乘法中心。跨族配对的整数部分不影响交换子，
其半整数部分来自 $\delta r/2$ 与 $s$，
故交换子正是 $(-1)^{b(r,s)}$。
标签改变一个偶格代表时，$2u_r,2v_s$ 的共同字符都是一，
所以这些确是 $\mathbb F_4$ 的操作，没有残留代表选择。
这也证明了所有平方身份，未仅从 torsion 点的阶数推断 lift 的阶数。

在原 $\Phi_\rho$ 上，$v_s$ 的三个非零整数周期因子的半特征
准确相乘为 $\chi(s)$，故
$$
V_s\Phi_\rho=\Phi_\rho.
\tag{15}
$$
于是
$$
e_r=U_r\Phi_\rho\quad(r\in\mathbb F_4)
\tag{16}
$$
是四个非零、不同 $V$ 字符的完整来源，构成 $\mathcal C$ 的基：
$$
V_se_r=(-1)^{b(r,s)}e_r.
\tag{17}
$$

## 3. 原 H 的绝对四余码矩阵

在 $\mathcal C$ 内，原物理操作是
$\mathcal Hf(w)=\omega^2 f(H^tw)$，保持前四变量。
$H^tJ=J$，所以它在这个完整四维空间上定义；
不把它误称为整个原多 theta 格的处处几何自同构。

在 $J^\vee/J$ 上，直接代入 $\bar H=H^{-t}$ 得
$$
u_r\longmapsto v_{\omega r},\qquad
v_s\longmapsto u_{\omega s}+v_{\omega s}.
\tag{18}
$$
(10) 中的整修正只改变 $J$ 的代表，所有中心仍须核。
为此用同时 CM 乘 $\omega$：它保持原字符、交换所有非零标签，
且与 $\mathcal H$ 交换。
所以同一族三个非零标签的中心标量相同。
同一 $J^\vee/J$ 类的 lift 在 $\mathcal C$ 上只差已经核定的共同字符标量；
(16)–(17)也直接证明这一有限 Heisenberg 表示不可约。
各操作平方为一，标量只能是 $\pm1$。
把(14)的完整加法律共轭过去，第一族的共同标量必须为 $+1$；
第二族因为
$(U_rV_r)(U_sV_s)=-U_{r+s}V_{r+s}$（不同非零 $r,s$），
共同标量必须为 $-1$。
因此完整 lift 的准确交织为
$$
\boxed{
\mathcal H U_r\mathcal H^{-1}=V_{\omega r},\qquad
\mathcal H V_s\mathcal H^{-1}
=\chi(s)U_{\omega s}V_{\omega s}.}
\tag{19}
$$

还须固定 $\mathcal H$ 本身的绝对标量。
原反射 $R_c$ 保持共同格，并且
$$
R_c\Phi_\rho=-\Phi_\rho,\qquad
R_c\Phi_\eta=\Phi_\eta+\Phi_\rho
\tag{20}
$$
是 R548 的原两态身份。
在(16)的基上它准确为
$$
R_ce_r=-\chi(r)e_r.
\tag{21}
$$
确切核法是 $R_cu_r-u_r$ 只有第五坐标 $-\delta r$；
它在 $\Phi_\rho$ 上给 $\chi(\delta r)=\chi(r)$，
而这个差与 $u_r$ 的交替配对为零。
再保 $\Phi_\rho$ 自身的负号，即得(21)。

由(20)–(21)，$\Phi_\eta$ 的 $e_0$ 系数恰为 $-1/2$。
由(15)、(19)，它对每个非零 $t$ 满足
$(-U_tV_t)\Phi_\eta=\Phi_\eta$。
取这三个身份的 $e_0$ 坐标，三个其他系数都恰为 $+1/2$。
所以
$$
\boxed{
\Phi_\eta=\frac12(-e_0+e_1+e_\omega+e_{\omega^2}),\qquad
\Phi_h=\frac12(e_1+e_\omega+e_{\omega^2}).}
\tag{22}
$$
该绝对系数使用原(20)的完整来源身份，不从边际或质量定标。

在有序基 $(e_0,e_1,e_\omega,e_{\omega^2})$ 中，
(19)–(22) 给原整个四维矩阵
$$
\mathcal H=\frac12
\begin{pmatrix}
-1&-1&-1&-1\\
1&-1&-1&1\\
1&1&-1&-1\\
1&-1&1&-1
\end{pmatrix}.
\tag{23}
$$
这里完整四余码包括另外两个 CM 角方向，不把它们删去。
只在原 $\langle\Phi_\rho,\Phi_\eta\rangle$ 二态内读(20)，
也没有把所有四维方向都叫同一个原 $S_3$ 二维表示。

## 4. 三项显式算子、平方和完整来源单位逆

定义真正只动五伴随的算子
$$
\boxed{
\mathscr D=\frac12\bigl(
U_1V_\omega+U_\omega V_{\omega^2}+U_{\omega^2}V_1
\bigr).}
\tag{24}
$$
乘法次序按显示保留。
由(17)，其四维矩阵是
$$
\mathscr D=\frac12
\begin{pmatrix}
0&-1&-1&-1\\
1&0&-1&1\\
1&1&0&-1\\
1&-1&1&0
\end{pmatrix}
=\mathcal H+\frac12I .
\tag{25}
$$
三个 $A_r=U_rV_{\omega r}$ 各满足 $A_r^2=-I$，
任意两个不同 $A_r$ 反交换；这直接由(14)给出。
因此不需要任何未显示的压缩系数，
$$
\boxed{\mathscr D^2=-\frac34I\quad\hbox{于 }\mathcal C.}
\tag{26}
$$
结合(22)，得到(1)的两个整个来源身份。
系数 $-4/3$ 在当前好素数是单位。

(26)的初始定义域是明确的 $\mathcal C$。
本篇没有说 $\mathscr D^2=-3/4$ 在整个多 theta 空间成立，
也没有说第一 E65 投影保持 $\mathcal C$。

## 5. 保全部中心的 E[16] 代表及普通整性

由(3)，五伴随 degree 的二部分分别为 $16,16,8,16,16$。
取明确的奇数
$$
o=3^4\cdot5\cdot11\cdot13\cdot17\cdot37,
\tag{27}
$$
它是五个 degree 奇部分的公倍数。
因为(11)属于原极化核，且第一坐标严格为零，
$o\,t^u_r,o\,t^v_s$ 都属于 $\{0\}\times E[16]^5$。

不能只把点 $t$ 换成 $ot$ 后忽略中心。
本篇指定新的 lift 为原完整 lift 的奇次幂：
$$
\widehat U_r=(U_r)^o,\qquad \widehat V_s=(V_s)^o.
\tag{28}
$$
这是一个完全指定的 theta 群元素，而不是任意选择
$\mathsf T_{ot}$ 的标量。
其点分别是 $ot^u_r,ot^v_s$，其中心就是原 lift 逐次相乘的中心。
由(14)，这两个奇次幂在 $\mathcal C$ 上仍准确等于 $U_r,V_s$。

以后可在(24)中逐个用(28)替换，记所得真正完整有限算子为
$\widehat{\mathscr D}$。它仍满足(1)、(26)于所示来源，
所有分支只含伴随的二幂 torsion。
这是保 lift 的替换；未声称两个 theta 群元素在整个空间都相等。

当前 $p>211$，原曲线、固定 CM frame 与这些二幂 torsion 都在
原好整模型中。原 canonical theta 群在 prime-to-$p$ 有限 étale
torsion 扩张上作用于完整整截面格，中心是单位；
奇次幂仍保该整格。按 R963 同一个完整多 theta 格的普通 Amice
实现，每一条实际 torsion 中心都给整有界测度。
(24)、(28)及逆式只有单位分母 $2,3$，所以整个来源及其逆式在
原普通整格中成立。返回 $b=17$ 时，若 $\theta_b^6=b$，全部六 sigma 来源同有
$\Phi_{*,b}(z)=b^{-1}\Phi_{*,1}(\theta_b z)$；
平移点随同乘 $\theta_b^{-1}$，故(1)的系数完全不变。
原 $\Omega_p$ 与全部 CM/Schwartz 尺度保持，
并未从大阶矩除法推测整性。

## 6. 原 E65 完整投影及五伴随身份

令 $\mathcal P$ 为原第一角加 E65 CM 投影。
它只作用于第一因子；(28)只作用于其他五因子。
所以二者在整个张量空间严格交换。

R963 的原完整分离是
$$
\mathcal P\Phi_\rho=Z\otimes\Lambda_\rho,\qquad
\mathcal P\Phi_h=Z\otimes\Lambda_h,
\tag{29}
$$
其中 $Z=F_{65,1}$，$\Lambda_\rho=\omega^2[2]_*\Lambda_{65}$；
两条真实单位质量分别是 $\omega^2\alpha$ 和 $\alpha_h$。
把(1)经 $\mathcal P$ 投影，再约消同一非零第一因子，
得到新的整个五变量身份
$$
\boxed{
\Lambda_h=\widehat{\mathscr D}\Lambda_\rho,\qquad
\Lambda_\rho=-\frac43\widehat{\mathscr D}\Lambda_h.}
\tag{30}
$$
平方运输准确写成
$\widehat{\mathscr D}^{\,2}\mathcal P\Phi_\rho
=\mathcal P\widehat{\mathscr D}^{\,2}\Phi_\rho$；
不要求 $\mathcal P\Phi_\rho$ 仍属于原四维 $\mathcal C$。

这里没有让伴随的 CM 多项式 $\mathcal C_h$ 与
$\widehat{\mathscr D}$ 自由交换。
若用原六重 CM 转移来实现 $\mathcal P$，(30)从第一因子端取得；
每个伴随 CM 分支与(28)的相对次序仍按原式保留。

同样，对于 R963 的任何完整第一 CM 算子 $N_Y$，
$\widehat{\mathscr D}N_Y\Phi_\rho=N_Y\Phi_h$。
这只是异因子的真实交换，未扩大成任意伴随 CM 算子的交换结论。

## 7. 任意原 cut 上的完整积分身份

写 $A_r=\widehat U_r\widehat V_{\omega r}$。
对任意实际连续测试 $F$ 与任意紧开原域 $\mathcal E$，
(1)给
$$
\boxed{
\int_{\mathcal E}F\,d\nu_{\Phi_h}
=\frac12\sum_{r\ne0}
 \int_{\mathcal E}F\,d\nu_{A_r\Phi_\rho},}
\tag{31}
$$
$$
\boxed{
\int_{\mathcal E}F\,d\nu_{\Phi_\rho}
=-\frac23\sum_{r\ne0}
 \int_{\mathcal E}F\,d\nu_{A_r\Phi_h}.}
\tag{32}
$$
每一项都用(28)所指定的完整 torsion 中心与有序 lift。
这三条一般是不同的 tame 来源。
prime-to-$p$ torsion 不属于 $\mathbf Z_p$ 的物理输入，
所以(31)–(32)没有把它们写成 $x\mapsto\zeta_2^x$ 的连续字符、
也没有写成普通加法平移或未证明的全测试空间简单伴随算子。

对 R548 的同一个剩余项，保持其原
$$
f=1_{L_{\rm mix}\ {\rm unit}}q
\left(1_{Y_s\ {\rm unit}}d\log\langle Y_s\rangle
     -1_{W\ {\rm unit}}d\log\langle W\rangle\right)
$$
以及原 $P_1,R_c$。在新框架中仅令
$$
F_{\rm rem}
=\bigl((f-f\circ R_c)\circ P_1\bigr)\circ L_h^{-1}.
\tag{33}
$$
原所有 $\lambda,\kappa$ 参数、$q$、其他紧开条件均包括在(33)内。
因为(5)还含 $1/(9a)$，准确返回是
$$
\boxed{
h_{\rm raw}\bigl((f-f\circ R_c)\circ P_1\bigr)
=\frac{9a}{2}\sum_{r\ne0}
 (A_r\Phi_\rho)(F_{\rm rem}).}
\tag{34}
$$
没有改变 $P_1,R_c,L_h^{-1}$ 的顺序。
若再作原有限 CM 纤维展开，应在每个实际
$A_r\Phi_\rho$ 上保完整中心、原 $\bar\beta^{-5}$、
$\mathcal D_\beta=\operatorname{diag}(1,\bar\beta^{-1}I_5)$
和角分支，原测试按对应既定顺序整体读入；
不能因为(28)只动伴随，就删去(33)对第一轴的混合依赖。

在(29)的投影来源上，(31)–(32)同样保任意混合 cut。
仅当测试确实分离为原第一单位 Mellin 权与独立伴随测试时，
才使用 $J'_Z(0)$ 的原条件行。
本篇不给(33)或 R964 的乘法来源 $SZ$ 新增中央零，
也没有把真实四维单位逆当作原全 $J_6$ 的受迫核。

## 8. 已付的新输入

本篇已经付清原两态的相同完整中心字符、两个明确的纯伴随有限
theta 群、原绝对四余码矩阵、三个实际有限 torsion 分支的单位逆、
以及原 $\Lambda_h/\Lambda_\rho$ 的整个五变量身份。
所有证明只用显示的格、半特征及 R963/R548 的原全来源身份，
无需新的 CM producer 或有限素数试算。

后续可以直接使用(34)来消费原同一个混合余域。
其三条 tame 中心与全部测试仍是真实输入，不能把三项统一认成
未平移的 $\rho$，也不能从(30)的单位逆直接删掉混合 cut。

## 9. 无额外三挠来源的简代表与共同固定轴

这里把(10)进一步化为只使用原输入 $1,5,6$ 的实际代表：
$
\boxed{
\begin{aligned}
u'_r&=\bigl((3+4\omega)r,0,0,0,-3r/2,-\delta\omega r/2\bigr),\\
v'_s&=\bigl(\bar g s,0,0,0,\delta s,0\bigr).
\end{aligned}}
\tag{35}
$
它们都属于原 $J^\vee$，平方范数分别为 $16r\bar r$ 和
$10s\bar s$。因此在这些代表上定义
$
U'_r=\mathsf T_{L_h^{-t}u'_r},\qquad
V'_s=\mathsf T_{L_h^{-t}v'_s}
\tag{36}
$
时不再另乘 $\chi$；同族的完整乘法中心已经为一。
$V'_s\Phi_\rho=\Phi_\rho$，跨族交换子仍为(14)。

这不是任意改相位。对非零标签，
$
u'_r-u_r=
\bigl((6-5\omega)r,0,(3+4\omega)r,0,
      -(2+\omega)r,-\omega^2r\bigr)\in J.
\tag{37}
$
末两分量的 $J$ 同余差为 $-2r$，前四个半特征相乘为一。
$v'_s-v_s$ 也属于 $J$ 且共同字符为一。
原 Hermitian 配对准确是
$
\langle u_r,u'_r\rangle=(38+37\omega)r\bar r,\qquad
\langle v_s,v'_s\rangle=(20+19\omega)s\bar s.
\tag{38}
$
故交替配对分别为 $-37r\bar r,-19s\bar s$；
完整 Weyl 中心给
$
\boxed{
U'_r=\chi(r)\mathsf T_{t^u_r}=U_r,\qquad
V'_s=\chi(s)\mathsf T_{t^v_s}=V_s
\quad\text{于 }\mathcal C.}
\tag{39}
$
零标签显然同样成立。因而(24)可逐项改用(36)，原矩阵、绝对号、
整个 $h/\rho$ 身份及单位逆都不变。
这一步没有引入任何三挠 translated 来源。

简代表同时固定一整个明确的观察族：
$
r_B=(\delta,B_2,B_3,B_4,g,\omega^2\bar g).
\tag{40}
$
事实上
$
\bar r_B\cdot u'_r
=-\delta(3+4\omega)r
+\frac{-3\bar g-\delta\omega^2g}{2}r=0,\qquad
\bar r_B\cdot v'_s=-\delta\bar g s+\bar g\delta s=0.
\tag{41}
$
中间三个系数没有进入(41)。
因此在任何以这个实际 $r_B$（或其固定整数倍）为第一行、
且已支付完整极化和准周期的正交框架中，(36)都只动伴随。
不需要为每个 $p$ 另选整数 Bezout 向量。

以下都属于这个同一观察族：

| 原实际来源 | $(B_2,B_3,B_4)$ |
|---|---|
| 原 $S$ 六 sigma 乘积的同一次重排 | $(2\delta,1,2)$ |
| 原 $T$ 六 sigma 乘积的同一次重排 | $(2\delta,3\delta,4)$ |
| R958 的 $W_{89,+}$ 候选 | $(2\delta,1,2a)$ |
| R958 的 $W_{89,-}$ 候选 | $(2\delta,1,2\bar a)$ |
| R961 的 E65 候选 | $(2\delta,a,18)$ |

重排是原 R963 的同一个 monomial 操作
$(r_1,r_2,r_3,r_4,r_5,r_6)\mapsto
(r_1,r_2,r_5,r_6,r_3,\omega^2r_4)$；
其在原 $\rho_{\rm raw}$ 上的标量准确为 $\omega^2$。
因此表中不是自由改造的算术来源。
例如前两条边际准确为 $\omega^2S$ 和 $6\delta\omega^2T$；
$W$ 候选及 E65 仍保 R958/R961 的 $1/a$、$1/\bar a$、$1/(9a)$
和各自已经核定的完整 CM 投影，不能仅凭这张表删掉投影。

在 R965 的 E65 框架中，仍按(28)取原 lift 的奇次幂，
于是实际点全在 $E[16]^5$。对于另一个固定框架，
应使用该框架的 degree 奇部分公倍数及原完整 lift。
特别 R958 原框架将五个伴随加倍以后，Gram 的五个伴随 degree
是其原(25)的四倍，二部分分别为 $16,8,8,8,16$；
第一行换成表中 $W$ 重排后，乘 $H$ 的第一行仍整，
其余加倍行也都整。末两列模二要么皆零、要么皆非零，
所以全部偶半特征保持。原 CM7/13 的行列式互素性只增加二的因子。
故原两条 $W$ 也确有同样的 $E[16]$ 纯伴随实现，
不是只在有理向量空间声称固定该行。
原固定坏素数范围及所有 $W$ 尺度保持。

### 9.1 两个不同的 h 来源与真正四态

重排原 $S/T$ 构造以后，原补域的 $H,P_j,R_c$ 作用于输入 $3,4$。
将这个原第三来源明确记为
$
h_{34}=(\omega^2H_{34,*}+\tfrac12I)\rho_{\rm raw}.
$
原重排的准确尺度是 $U_*h_{\rm raw}=\omega^2h_{34}$，与
$U_*\rho_{\rm raw}=\omega^2\rho_{\rm raw}$ 同时保留；以下四态采用
除去这个共同根单位后的显示规范。
另一方面，(24)、(35)给的是
$
h_{56}=\mathscr D_{156}\rho_{\rm raw}
      =(\omega^2H_{56,*}+\tfrac12I)\rho_{\rm raw}.
\tag{42}
$
这两个来源不相同，不共用一个未注明下标的 $h$。

(35)只涉及输入 $1,5,6$，所以与作用输入 $3,4$ 的
$H_{34},R_{c,3},P_{j,34}$ 逐来源严格交换：
在生成函数中是不同变量块的操作，全部 Gaussian 因子也在各自块内。
因此有完整第四态
$
\boxed{
h_{34,56}:=\mathscr D_{156}h_{34}
=(\omega^2H_{34,*}+\tfrac12I)h_{56},}
\tag{43}
$
以及
$
\mathscr D_{156}^2h_{34}=-\tfrac34h_{34},\qquad
h_{34}=-\tfrac43\mathscr D_{156}h_{34,56}.
\tag{44}
$
这里(44)通过不同变量块的真实交换由(26)取得，
未扩大(26)在原整个多 theta 空间上的定义域。

任何仅限制输入 $3,4$ 的原深域和对应的真正普通核，
也按张量分解与(35)交换。因而 R548 的 $Q_{34}$ 深域身份及其
完整连续单位逆，可以逐真实来源运输到(43)。
但其在一般测试上仍须作用于整个 $q$、logarithm 和所有混合 cut；
没有让 $q$ 自身因(41)而不变。
原条件中央行只有在其实际投影与测试条件都已支付时才能调用。

(43)–(44)给出可直接使用的四态与完整反演。
仅把旧分布身份线性施加 $\mathscr D_{156}$ 尚不产生新的受迫零；
要消费新增 $W/Z$ 的算术条件，仍须把同一实际测试送入对应
原投影行。这条界限与(31)–(34)一致。

## 依赖

- [R963：原 h 与 E65 的同框架两态及完整投影](R963-original-h-e65-full-cm-projection.md)。
- [R961：原 E65 同六 sigma 与全部66维 CM 投影](R961-original-e65-common-six-sigma-cm-projection.md)。
- [R548：完整反射、二态与原唯一混合余域](R548-original-whole-third-source-cm-reflection-and-complete-positive-spectrum.md)。
- [R546：全伴随有限 CM 纤维及原测试转置](R546-original-third-sigma-full-five-companion-cm-transfer.md)。
