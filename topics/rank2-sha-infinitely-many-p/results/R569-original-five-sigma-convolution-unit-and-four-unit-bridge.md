# R569 — 原五 sigma 的真实六度边际、完整卷积单位与四单位负矩桥

日期：2026-11-14。**状态：已证明。**

本篇在 R567 使用的同一个五 sigma 来源中，准确计算纯 $C$ 平均后的
$(D_4,d_0)$ 全边际。它恰是原 $f_4=x_\wp\sigma^6$ 与原 sigma 的独立
乘积，常数为 $\omega^2/84$，无需另加角投影。
一个明确的五次权使**整个五维**有界测度成为整卷积单位。
进一步，把 R562 的完整四单位积分连同其两个补集，转置成这同一个
原来源上的一个实际单位积分；所有平移后的单位条件均保留。

最后将这个单位测试和原 $S/T$ 中央测试分别运输到 R568 的同一个
完整混合词域。两行的来源及域相同，测试不同；本篇没有把前者认成
后者，也没有把 R556 的 native 条带残差认成完整算术总行。

## 1. 同一个原来源与规范

沿用
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R562](R562-original-four-unit-domain-and-negative-two-unit-relation.md)、
[R567](R567-native-both-strips-and-exact-five-sigma-normal-jets.md)、
[R568](R568-original-positive-strip-full-cores-and-native-transport.md)
的原普通射线、全部有限坏集及周期。这里没有新增射线或坏素数。

记
$$
b=17,\quad \omega^2+\omega+1=0,\quad\delta=1+2\omega,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad\Omega=\Omega_p\in\mathcal O^\times.
\tag{1}
$$
特别，原 sigma 与整个六度空间的实际核心为 $\beta$。
物理输入、单位和 $p$ 倍子群均在原紧致输入格上理解。
测度 $\nu_F$ 的矩规范仍为
$$
\int z^j\,d\nu_F(z)=\Omega^jF^{(j)}(0).
\tag{2}
$$

原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。令
$$
C=\frac{\xi_1-\xi_3+x}{\delta},\qquad
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3 .
$$
其 Hermitian 数据准确是
$$
N(C)=1,\qquad N(D_4)=6,\qquad\langle D_4,C\rangle=-1.
\tag{3}
$$
纯 $C$ 旋转及其平均为
$$
S_C=I+(\omega-1)\bar C^{\,t}C,\qquad
\mathcal P_C=\frac{I+(S_C)_*+(S_C^2)_*}{3}.
\tag{4}
$$
它只操作前四输入，固定 $c,d_0$，并保原 $Y,W,W',F,G$。
完整五输入来源是 R567 的
$$
\boxed{
\nu_5=-\frac1{84}\mathcal P_C
\bigl(\nu_\sigma(\xi_1)\otimes\nu_\sigma(\xi_2)
      \otimes\nu_\sigma(\xi_3)\otimes\nu_\sigma(x)
      \otimes\nu_\sigma(d_0)\bigr).
}
\tag{5}
$$
原六输入 $\mu_0=\mathcal P_C\rho_0$ 精确为
$\nu_5\otimes\nu_\sigma(c)$，按原坐标次序理解。
以下没有换掉 (5) 的隐藏输入。

## 2. 三个完整共轭给出的准确六度边际

由 (3)，对 $\zeta=1,\omega,\omega^2$ 有
$$
D_4S_C^\zeta=D_4+(1-\zeta)C,
\tag{6}
$$
这里 $S_C^\zeta$ 表示把 (4) 中的 $\omega$ 换成 $\zeta$。
在前四个原输入上的三行及其全 sigma 乘积是
$$
\begin{array}{c|c|c}
\zeta&\text{实际四系数}&
 \prod_{\ell=1}^{4}\sigma(a_{\zeta,\ell}z)\\ \hline
1&(1,\omega^2,-2\omega,0)&0\\
\omega&(-\omega,\omega^2,1-\omega,\omega^2)&
 (2+\omega)f_4(z)\\
\omega^2&(1-\omega,\omega^2,-\omega,-\omega)&
 \delta f_4(z)
\end{array},
\qquad f_4=x_\wp\sigma^6.
\tag{7}
$$
这些是全函数恒等式。第一行因为一个真实独立 sigma 输入取零而
全消；后两行只用
$$
\sigma(\epsilon z)=\epsilon\sigma(z)\quad(\epsilon\in\mu_6),\qquad
1-\omega=\omega^2\delta,\qquad
\sigma(\delta z)=\delta x_\wp(z)\sigma(z)^3 .
$$
例如第二行的完整单位乘子为
$(-\omega)\omega^2\omega^2\omega^2\delta=-\omega\delta=2+\omega$。
没有漏掉半特征或重新选择四挠代表。

因此平均的系数为
$$
\frac{(2+\omega)+\delta}{3}=1+\omega=-\omega^2.
$$
连同 (5) 的原 $-1/84$，得到完整测度恒等式
$$
\boxed{
(D_4,d_0)_*\nu_5=\frac{\omega^2}{84}\,
                    \nu_{f_4}\otimes\nu_\sigma .
}
\tag{8}
$$
全函数恒等式通过 (2) 给全部矩，再由原紧致输入格上多项式的稠密性
给 (8)。这里只忘去三个真实伴随；没有把它们在含旧 $Y/W$ 测试时
擅自积分掉，也没有再对第一轴作 $\mu_6$ 投影。

这也直接连接 R567 的两个法向：
$$
T_7=D_4-\omega d_0,\qquad T_{10}=D_4-2\omega d_0,
$$
$$
\operatorname{Gram}(T_7,T_{10})=
\begin{pmatrix}7&8\\8&10\end{pmatrix},\qquad
\boxed{D_4=2T_7-T_{10},\quad
       d_0=\omega^2(T_7-T_{10}).}
\tag{9}
$$
变换行列式是 $-\omega$，为单位；Gram 行列式是 $6$。
两法向不正交，(9) 不允许把它们的两个深度事件当成独立矩形。
它们只是同一个 (5) 的实际坐标。

## 3. 完整五维和六维的整卷积单位

原六度核心及 sigma 核给
$$
\nu_{f_4}|_{p\mathcal O}=\beta[\kappa]_*\nu_{f_4},\qquad
\nu_\sigma|_{p\mathcal O}=\beta[\kappa]_*\nu_\sigma.
$$
因为 $f_4(z)=z^4+O(z^{10})$、$\sigma(z)=z+O(z^7)$，
定义
$$
m_4^\times=24\Omega^4(1-\beta\kappa^4),\qquad
m_1^\times=\Omega(1-\beta\kappa).
\tag{10}
$$
二者均为单位。这里 $m_4^\times$ 是明确的**正四矩**；
下一节的 $I_4$ 始终是原**负二矩**，绝不把它们相认。

在完整五维格上置
$$
w_5(\xi)=1_{\{D_4,d_0\ {\rm unit}\}}D_4^4d_0,\qquad
d\tau_5=w_5\,d\nu_5 .
$$
(8) 准确给
$$
\boxed{
\tau_5(\mathcal L_5)
=\frac{\omega^2}{84}m_4^\times m_1^\times
=\frac{2\omega^2}{7}\Omega^5
 (1-\beta\kappa^4)(1-\beta\kappa)\in\mathcal O^\times.
}
\tag{11}
$$
其中 $\mathcal L_5$ 是原五输入格。可以取
$(D_4,\xi_2,\xi_3,x,d_0)$ 为其坐标；这一变换行列式为一。
故这里确实是完整五维测度的质量，而非一个一维形式商。

原有界整测度代数的 Amice 同构把 $\tau_5$ 送到完整多变量
$\mathcal O[[T_1,\ldots,T_5]]$。其常数项 (11) 为单位，
所以存在唯一有界整测度
$$
\boxed{\ \mathcal U_5=\tau_5^{*-1},\qquad
               \tau_5*\mathcal U_5=\delta_0.\ }
\tag{12}
$$
若系数格需要更多 $\mathbf Z_p$ 坐标，就取相应的全部 Amice 变量；
同一个常数项证明逐字成立。
构造上，写 $\mathcal A_{\tau_5}=M+G$、$G(0)=0$，则
$$
\mathcal A_{\mathcal U_5}
=M^{-1}\sum_{r\ge0}(-M^{-1}G)^r .
$$
这是多变量幂级数拓扑中的系数逐项收敛式，所有系数整；
不需要未经支付的 theta 反卷积或新的解析收敛假设。

更强地，在原完整六输入来源上取
$$
w_6=1_{\{c,D_4,d_0\ {\rm unit}\}}\,cD_4^4d_0,\qquad
d\tau_6=w_6\,d\mu_0 .
$$
则
$$
\boxed{
\tau_6(\mathcal L_6)
=\frac{2\omega^2}{7}\Omega^6
 (1-\beta\kappa^4)(1-\beta\kappa)^2\in\mathcal O^\times.
}
\tag{13}
$$
所以完整六维的 $\tau_6$ 也有有界整卷积逆。

### 3.1 全部混合条件的准确转置

对任一原五维有界整测度 $\zeta$，定义
$$
\mathcal V_\zeta=\zeta*\mathcal U_5,\qquad
(\mathcal T_\zeta f)(\xi)=\int f(\xi+t)\,d\mathcal V_\zeta(t).
$$
由有界测度的 Fubini 和 (12)，对任意连续有界 $f$ 有
$$
\boxed{
\int f\,d\zeta=\int w_5(\xi)\,
                       (\mathcal T_\zeta f)(\xi)\,d\nu_5(\xi).
}
\tag{14}
$$
这是完整五维转置。若 $f$ 含实际线性观察 $r$，每一项都变成
$r(\xi+t)=r(\xi)+r(t)$；例如
$$
1_{\{Y\ {\rm unit},\,E\in p^m\}}\log\langle Y\rangle
\longmapsto
1_{\{Y(\xi)+Y(t)\ {\rm unit},\,
       E(\xi)+E(t)\in p^m\}}
\log\langle Y(\xi)+Y(t)\rangle .
\tag{15}
$$
全部 $W$、另外三个伴随和混合切集同样转置。
六维版本用 (13) 完全相同。此证明没有声称这些平移与原深度核或
算术 projector 交换。原某一中央值为零，不会自动给出其全部平移为零。

## 4. R562 四单位域在同一个原来源上的显式返回

沿用 R562 的原质量一奇三度源
$$
B=-y_\wp\sigma^3,\qquad
I_4=\int_{z\ {\rm unit}}z^{-2}\,d\nu_{f_4}(z).
\tag{16}
$$
这里 $\nu_B$ 与 (8) 的 $\nu_{f_4}$ 都采用 (1)–(2) 的实际周期。

先在一维定义
$$
d\tau_4(z)=1_{\{z\ {\rm unit}\}}z^4\,d\nu_{f_4}(z),\qquad
\mathcal U_B=\nu_B*\tau_4^{*-1}.
\tag{17}
$$
$\tau_4$ 的质量恰为 (10) 的 $m_4^\times$，所以逆是有界整测度；
整个式子没有使用 $I_4^{-1}$，也不要求 $I_4$ 非零。
质量 $\mathcal U_B(\mathcal O)=(m_4^\times)^{-1}$ 也是单位。

把 R562 原独立 sigma 输入改名为 $d$，定义一个全域有界连续测试
$$
\begin{aligned}
j(v,d)={}&
1_{\{d,v,\delta d-v,\delta d+v\ {\rm unit}\}}\\
&\cdot\frac{d^3}{2}
 \left\{(\delta d-v)^{-2}+(\delta d+v)^{-2}\right\}.
\end{aligned}
\tag{18}
$$
分母只在显示的单位域使用，域外为零。其原完整积分为
$J_{\mathscr B}$。定义准确转置
$$
j^\sharp(z,d)=\int j(z+t,d)\,d\mathcal U_B(t).
\tag{19}
$$
由 $\tau_4*\mathcal U_B=\nu_B$，严格有
$$
\boxed{
J_{\mathscr B}
=\int_{z,d\ {\rm unit}}z^4j^\sharp(z,d)\,
                  d\nu_{f_4}(z)d\nu_\sigma(d).
}
\tag{20}
$$
这里每个平移分支都保留四条原条件
$$
d,\quad z+t,\quad\delta d-z-t,\quad\delta d+z+t
\quad\text{均为单位}.
\tag{21}
$$
额外的 $z$ 单位是原加权测度 $\tau_4$ 的真实支撑，不被删去。

利用独立 sigma 的准确正一矩，还同时有
$$
\boxed{
I_4=\int_{z,d\ {\rm unit}}
       \frac{z^{-2}d}{m_1^\times}\,
                   d\nu_{f_4}(z)d\nu_\sigma(d).
}
\tag{22}
$$
因此置
$$
c_I=\frac{9b\Omega^3(1-\beta\kappa^3)}{2\delta^2},\qquad
G(z,d)=1_{\{z,d\ {\rm unit}\}}
       \left\{z^4j^\sharp(z,d)+
              c_I\frac{z^{-2}d}{m_1^\times}\right\}.
\tag{23}
$$
由 (8)、(20)–(22)，在**同一个原五 sigma 来源**上得到
$$
\boxed{
\int G(D_4,d_0)\,d\nu_5
=\frac{\omega^2}{84}\left(J_{\mathscr B}+c_I I_4\right).
}
\tag{24}
$$
这个式子的左边不是一个新选的辅助 theta 来源。

R562 对两个真实深补集已给完整级数 $C_\sigma\in\kappa^7\mathcal O$、
$T_B\in\kappa^6\mathcal O$，故 (24) 的准确值是
$$
\boxed{
\begin{aligned}
\int G(D_4,d_0)\,d\nu_5
={}&-\frac{\omega^2}{504}\,
     \Omega(1-\beta\kappa)(1-3\beta)\\
&-\frac{\omega^2}{84}(C_\sigma+T_B)
\ \in\ \mathcal O^\times .
\end{aligned}}
\tag{25}
$$
$1-3\beta$ 为单位的偶迹/Hasse 证明正是 R562 §4，
其余因子在当前射线上为单位。特别，没有省去三度输入深补集的
真实一阶质量 $\beta\Omega(1-\beta\kappa)/\delta^2$。

### 4.1 两个原法向上的全部混合单位条件

用 (9)，(19) 中每个实际平移分支可全部写成
$$
z=2T_7-T_{10},\qquad d=\omega^2(T_7-T_{10}),\qquad
v=2T_7-T_{10}+t,
$$
$$
\boxed{
\begin{aligned}
H_{\rm raw}&=\omega^2T_7+\omega T_{10}-t,\\
K_{\rm raw}&=(3-\omega)T_7+(-2+\omega)T_{10}+t.
\end{aligned}}
\tag{26}
$$
原 $d^3=(T_7-T_{10})^3$，因为 $\omega^6=1$。
所以四条原单位条件正是
$$
T_7-T_{10},\quad 2T_7-T_{10}+t,\quad
\omega^2T_7+\omega T_{10}-t,\quad
(3-\omega)T_7+(-2+\omega)T_{10}+t
\quad\text{均为单位},
\tag{27}
$$
并另保 $2T_7-T_{10}$ 单位。
(26)–(27) 是 R567 同源两法向中的实际测试式，
不把不同法向当成独立输入，也不把平移 $t$ 取零。

## 5. 与完整原 $S/T$ 行放在同一个真实词域

先把 (25) 提回原六输入：
$$
\widetilde G(\xi)=
1_{\{c\ {\rm unit}\}}\frac{c}{m_1^\times}G(D_4,d_0).
$$
由 $\mu_0=\nu_5\otimes\nu_\sigma(c)$，有
$$
\boxed{\ \mu_0(\widetilde G)=\nu_5(G)\in\mathcal O^\times.\ }
\tag{28}
$$

取 R568 的同一实际轴
$$
D=D_4+c+(2+3\omega)d_0,\quad
u=\frac{\omega c+(1-\omega)d_0}{2},\quad
P=u-\omega^2D/7,
$$
并记
$$
P_{a,t}=I+(t-1)\frac{\bar a^{\,t}a}{N(a)},\qquad
\mathsf A=P_{u,\kappa}P_{P,\kappa}.
\tag{29}
$$
R568 已付整个两态的完整来源返回，特别
$$
\boxed{
\mu_0|_{\mathsf A\mathcal L_6}
=-\chi_{65}\lambda^2\,\mathsf A_*\mu_0.
}
\tag{30}
$$
这是原矩阵像格，不是两个非正交轴的虚构共同深矩形。

令 $q_n$ 是 R536 的完整三个 carry 分支平均测试，
包含原 $\widehat P_p$、全部 $E$ 单位逆及 $D_j/\kappa^n$，
域外为零。令
$$
\ell=(p-1)\left\{
1_{\{Y\ {\rm unit}\}}\log\langle Y\rangle
-1_{\{W\ {\rm unit}\}}\log\langle W\rangle
\right\}.
$$
纯 $C$ 旋转保该平均及 $Y,W$，因此 R536 的完整 $\pi_4$ 身份给
$$
\boxed{
\mu_0(q_n\ell)=
\beta^n\bigl(J'_S-6\delta J'_T\bigr).
}
\tag{31}
$$
这里是**完整原算术行**；没有在 $\mathcal B$、两条 native strip
或其任一补域上单独赋零。

把 (28)、(31) 同时通过同一个 (30) 运输：
$$
\boxed{
\int_{\mathsf A\mathcal L_6}
       \widetilde G(\mathsf A^{-1}\xi)\,d\mu_0
=-\chi_{65}\lambda^2\,\nu_5(G)\in\mathcal O^\times,
}
\tag{32}
$$
$$
\boxed{
\int_{\mathsf A\mathcal L_6}
 q_n(\mathsf A^{-1}\xi)\ell(\mathsf A^{-1}\xi)\,d\mu_0
=-\chi_{65}\lambda^2\beta^n
       \bigl(J'_S-6\delta J'_T\bigr).
}
\tag{33}
$$
(32) 中 (21)、(27) 的全部单位条件仍按 $\mathsf A^{-1}$ 转置；
(33) 中原 $q_n,Y,W$ 的全部观察与指示也这样转置。
所有显示的逆仅在实际像格上使用，其值仍在原输入格内。

两式提供相同原来源、相同完整词域上的一个单位行与一个原算术行。
它们的测试尚未被证明等价。要由此排除原两个中央同时为零，
仍须支付这两个真实测试之间的关系或整个余域补偿。
特别，不能把 (25) 或 (32) 的单位性直接代入 R567 的
$C_0/p+\lambda^2C_1$，也不能把 native 条带积分非零当成 (33) 非零。
全文没有完成课题的无穷素数目标。

## 精确证书

- [check-r569-original-five-sigma-convolution-unit-and-four-unit-bridge.js](../scripts/check-r569-original-five-sigma-convolution-unit-and-four-unit-bridge.js)
- [check-r569-original-five-sigma-convolution-unit-and-four-unit-bridge.json](../scripts/check-r569-original-five-sigma-convolution-unit-and-four-unit-bridge.json)

脚本在 $\mathbf Q(\omega)$ 中用 BigInt 有理运算核定完整 $C$ 旋转、
三支的真实四系数与绝对 sigma 相位、(8) 的原归一、(9)、(26)
的全部物理变换以及 (11)、(13)、(25) 的常数。
多变量整逆、完整条件转置和词域的测度恒等式由正文支付；
证书不以有限素数采样或数值非零代替这些证明。
