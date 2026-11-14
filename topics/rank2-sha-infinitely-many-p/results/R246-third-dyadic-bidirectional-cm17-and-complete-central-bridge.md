# R246 — 第三种 dyadic 型的双向原运输、CM17 反号与完整中央桥梁

日期：2026-11-13。**状态：下面的实际五块双向运输、全部归一常数、两个 CM 方向的相反符号、到三条秩二曲线的完整中央行以及 R245 伴随的转置公式均已证明。尚未证明这些中央行在无穷多个素数上不同时消失。**

本篇所有平移均是 [R239](R239-third-rank2-curve-and-original-sixteen-coset-transport.md)
的原 theta 群作用。先统一作 $[2]$ 拉回，次数为 $272$，二挠线丛扭转已消去。
特别不把 degree-$68$ 的新旧两个不同线丛直接混在一起。

令 $H=A_{136}$ 取 [R243](R243-third-rank2-explicit-theta-and-common-rational-parameter.md)
首项一的原归一，$S_8=-y\vartheta\sigma^3$ 取
[原 E8 参考](../notes/2026-11-13-three-curve-central-functional-and-rankzero-connection.md)。
写
$$
\alpha_+=4+i,\qquad\alpha_-=4-i,\qquad
\rho=\frac{2^{5/8}}{\cos(\pi/16)},\qquad \kappa_4=2^{-1/4}.
$$
下文构造固定代数、在所有奇素位整的互逆块运输 $\mathcal U,\mathcal V$。
其准确作用包括
$$
\boxed{\begin{aligned}
\mathcal U A_{17}(4z)&=-22i\,H(2z),\
\mathcal U\vartheta(4\alpha_+z)&=S_8(2\alpha_+z),\
\mathcal U\vartheta(4\alpha_-z)&=-S_8(2\alpha_-z).
\end{aligned}}
\tag{1}
$$
因此新 CM17 反对称方向的反向像是旧的**对称**方向。
这一个负号不能沿用 R231 旧 dyadic 型的同号规范。

## 1. 固定实际算子及其双向性

仍用 $E_0:y^2=x^3-x$、$dz=dx/(2y)$，令 $\Omega_0$ 为正实周期。
置
$$
P=\frac{(4-i)\Omega_0}{16},\qquad Q=-iP,\qquad N=272,
$$
$$
\mathcal T_R f(z)=
\exp\!\left(\frac{N\pi\bar R}{\Omega_0^2}z
       -\frac{N\pi|R|^2}{2\Omega_0^2}\right)f(z-R).
\tag{2}
$$
R239 已准确识别 $X=\mathcal T_P,Z=\mathcal T_Q$ 与原十六格的
移位、乘相位算子。写 $\zeta=e^{2\pi i/16}$，有
$$
ZX=\zeta XZ,\quad X^{16}=Z^{16}=1,
\quad
\mathcal R=\frac{ZX+\zeta Z^{-1}X+\zeta ZX^{-1}+Z^{-1}X^{-1}}{1+\zeta}.
\tag{3}
$$
设 $t_0=\tan(\pi/16)$，原向量是
$$
v_0=(1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0),
$$
$$
v=(0,1,0,t_0,0,-t_0,0,-1,0,-1,0,-t_0,0,t_0,0,1).
$$
按未除 Haar 常数的有限内积，
$$
\langle v_0,v_0\rangle=4,\qquad
\langle v,v\rangle=4(1+t_0^2),\qquad\mathcal Rv_0=v.
\tag{4}
$$
旧块投影是明确的十六项实际算子
$$
\Pi_0=\frac1{16}\sum_{a,b=0}^3X^{4a}Z^{4b}
       =\frac{v_0v_0^*}{4}\otimes1_{17}.
$$
星号是固定代数对合 $X^*=X^{-1},Z^*=Z^{-1},\zeta^*=\zeta^{-1}$。
定义
$$
\boxed{
\mathcal U=\rho^{-1}\mathcal R\Pi_0,\qquad
\mathcal V=\rho\cos^2(\pi/16)\Pi_0\mathcal R^*.
}
\tag{5}
$$
在原有限坐标中，它们分别是
$\rho^{-1}vv_0^*/4$ 和 $\rho v_0v^*/\langle v,v\rangle$。
故准确有
$$
\mathcal V\mathcal U=\Pi_0,\qquad
\mathcal U\mathcal V=\Pi_v,
\qquad
\Pi_v=\frac{vv^*}{\langle v,v\rangle}\otimes1_{17}.
\tag{6}
$$
两者都保留整个十七处向量。
有限 Fourier 算子在 $v_0,v$ 上都取一，所以 (5) 与原全局 $i$ 作用交换。
所有分母都是固定二单位；特别 $1+\zeta$ 的范数为二，
$\cos(\pi/16)$ 和 $2^{1/8}$ 在任何奇素位都是单位。
R239 的真实 theta 群整模型于是使 (5) 在所有奇好素位保持截面格。

## 2. 精确的常数 $\rho$

在 degree-$16$ 的基础尺度令 $P_0=\Omega_0/16,Q_0=-iP_0$，
记相应算子为 $X_0,Z_0,\mathcal R_0$。
旧向量给 $\vartheta(4z)$；原新向量给 $S_8(2z)$ 的一个非零倍数。
后一个身份由原 E8 参考笔记的同一个 $I=1,G=i$ 唯一特征线确定。
所以只须准确计算其常数项。

写
$$
D_0=\sum_{n\in\mathbb Z}e^{-\pi n^2},\qquad
S_0=\sum_{n\in\mathbb Z}i^n e^{-\pi(n+1/4)^2},\qquad
\xi=e^{\pi i/16},\quad\xi^2=\zeta.
$$
则
$$
\boxed{\frac{S_0}{D_0}=2^{-3/8}\xi^{-1}.}
\tag{7}
$$
给出其确切 theta 证明。令 $T=(1-i)\Omega_0/4$。
原 theta 加法式为
$$
\vartheta(z+w)\vartheta(z-w)
=\vartheta(z)^2\vartheta(w)^2+\sigma(z)^2\sigma(w)^2.
\tag{8}
$$
它可由两边的除子、自动因子及 $w=0$ 的值直接核定。
在 $T$ 有 $x(T)=i,y(T)=1-i$。将 $(z,w)=(T,iT)$ 代入 (8)，得到
$\vartheta(\Omega_0/2)^2=2\vartheta(T)^4$。
在平方格上，Jacobi 的 $\theta_3^4=\theta_2^4+\theta_4^4$ 和
$\theta_2=\theta_4$ 给
$\vartheta(\Omega_0/2)=e^{\pi/8}2^{-1/4}$。
取从原点连续确定的正分支，即
$$
e^{-\pi|T|^2/(2\Omega_0^2)}\vartheta(T)=2^{-3/8}.
$$
把 $\vartheta$ 写成原 normalized Gaussian 级数就得到 (7)，相位是
$\xi^{-1}$，并非一个未指定的八次根。

在原有限 Gaussian 中，四项 $ZX,Z^{-1}X,ZX^{-1},Z^{-1}X^{-1}$
作用于 $v_0$ 后的常数项，除以 $D_0$，依次是
$$
2^{-3/8}(\xi,\xi^{-1},\xi^{-1},\xi).
$$
用 (3) 的两个 $\zeta$ 系数合并，得到
$$
\frac{4\cdot2^{-3/8}\xi}{1+\zeta}
=\frac{2^{5/8}}{\cos(\pi/16)}=\rho.
$$
因此
$$
\boxed{\mathcal R_0\vartheta(4z)=\rho S_8(2z).}
\tag{9}
$$
本节没有用小数拟合认定代数常数。

## 3. CM17 两个方向的相位分别为正与负

对 $O_\pm(z)=\vartheta(4\alpha_\pm z)$，(2) 在拉回后准确变成
degree-$16$ 的平移：
$$
\mathcal T_R^{272}\bigl(f(\alpha_\pm z)\bigr)
=\bigl(\mathcal T_{\alpha_\pm R}^{16}f\bigr)(\alpha_\pm z).
\tag{10}
$$
这里包括全部线性及常数指数，因为 $\alpha_\pm\bar\alpha_\pm=17$。

在正方向，$\alpha_+P=17P_0,\alpha_+Q=17Q_0$。
由于 $X_0^{16}=Z_0^{16}=1$，(3) 就成为原 $\mathcal R_0$。

在负方向，
$$
\alpha_-P=15P_0+8Q_0,\qquad
\alpha_-Q=-8P_0+15Q_0.
$$
准确的复合规则为
$\mathcal T_{aP_0+bQ_0}^{16}=\xi^{-ab}Z_0^bX_0^a$。
因此两个生成元变为
$$
\boxed{X_-=iZ_0^8X_0^{-1},\qquad
        Z_-=-iZ_0^{-1}X_0^8.}
\tag{11}
$$
第二个相位为 $-i$，因为 $120\equiv24\pmod {32}$。
在 $X_0^8v_0=Z_0^8v_0=v_0$ 上，四项逐一化为
$$
\begin{array}{c|c}
Z_-X_-&-Z_0^{-1}X_0^{-1}v_0\\
Z_-^{-1}X_-&-Z_0X_0^{-1}v_0\\
Z_-X_-^{-1}&-Z_0^{-1}X_0v_0\\
Z_-^{-1}X_-^{-1}&-Z_0X_0v_0.
\end{array}
$$
它们连同 (3) 的系数恰为 $-\mathcal R_0v_0$。
结合 (9)、(10)，便得 (1) 的两个 CM 等式。
由 (6)，反向准确是
$$
\boxed{\mathcal V S_8(2\alpha_+z)=O_+(z),\qquad
       \mathcal V S_8(2\alpha_-z)=-O_-(z).}
\tag{12}
$$

## 4. 三个 primitive 块的全部原归一

在未双倍的旧 degree-$17$ 尺度，用 R231 的实际多项式
$$
\begin{aligned}
P_1(s)&=s+3s^2/5-s^3/5+s^4/5,\\
P_2(s)&=1-18s^2+16s^3+s^4,\\
P_3(s)&=1-7s+21s^2-5s^3-2s^4.
\end{aligned}
$$
置
$$
A_0(z)=A_{17}(4z),\qquad
R_k(z)=\vartheta(4z)^{17}P_k(x(4z)^{-2})\quad(k=2,3).
$$
其中 $R_2=S_{289}(2z),R_3=S_{4913}(2z)$；两个 $S$ 均取中心一归一。

由 (5) 的实际有限向量，三个像分别属于新 dyadic 型的
$\lambda,\lambda^2,\lambda^3$ primitive 线。
它们就是 $D=8\cdot17^k$ 的三个真实四次扭曲
$y^2=x^3-Dx$，不是另外挑出的等维空间。

所有常数可在同一个四挠点支付。由 (3) 及 $ZX=\xi\mathcal T_{P+Q}$，
$$
\mathcal R=\frac1{2\cos(\pi/16)}
       \sum_{\epsilon,\delta=\pm1}\mathcal T_{\epsilon P+\delta Q}.
\tag{13}
$$
改为 $w=4z$ 后，四个平移点分别模周期等于 $\pm T,\pm iT$。
旧 degree-$17$ theta 的半特征是
$\chi(m\Omega_0+ni\Omega_0)=(-1)^{mn}$。
支付从原四点到这四个代表的完整相位后，四项都乘 $i$。
例如
$4(P+Q)=-\bar T+(1-i)\Omega_0$，相位为
$(-1)^{-1}\exp(-17\pi i/2)=i$。

取平移 $T$ 的局部展开。
由二倍点的 zeta 加法公式，
$$
(\log\vartheta)'(T)-\pi\bar T/\Omega_0^2=-(1+i)/2.
$$
于是移回原点后的单个 theta 因子、除去常数 $2^{-3/8}$ 后，
其对数至四阶为
$$
\frac{1+i}{2}w-\frac i2w^2-\frac{1-i}{3}w^3+\frac13w^4+O(w^5).
$$
同时
$$
x(w-T)=i-2(1-i)w-4w^2-4(1+i)w^3-8iw^4+O(w^5).
$$
因此对实际 $P_1$，单项平移除去 $2^{-51/8}$ 后准确为
$$
-\frac{32(1+i)}5w-\frac{32i}5w^2
+\frac{56(1-i)}5w^3-88w^4+O(w^5).
\tag{14}
$$
四个 $i$ 旋转相加只留下四的倍数权。
用 $w=4z$、$H(2z)=16z^4+\cdots$ 以及 (13)，得到
$$
\mathcal R A_0=-22i\rho H(2z).
$$
同一计算对中心一的另外两列只须使用
$P_2(-1)=-32,P_3(-1)=32$。
所得完整表为

| 旧 $v_0$ 实际来源 | $\mathcal U$ 的准确像 | $\mathcal V$ 的反向像 |
|---|---|---|
| $O_+$ | $N_+:=S_8(2\alpha_+z)$ | $\mathcal VN_+=O_+$ |
| $O_-$ | $-N_-:=-S_8(2\alpha_-z)$ | $\mathcal VN_-=-O_-$ |
| $A_0$ | $-22iH(2z)$ | $\mathcal VH(2z)=iA_0/22$ |
| $S_{289}(2z)$ | $-iS_{2312}(2z)/2$ | $\mathcal VS_{2312}(2z)=2iS_{289}(2z)$ |
| $S_{4913}(2z)$ | $iS_{39304}(2z)/2$ | $\mathcal VS_{39304}(2z)=-2iS_{4913}(2z)$ |

这里也可把表中第四、五行作为 $S_{2312},S_{39304}$ 的固定代数构造。
它们中心值准确为一，且有限向量已确定其真实曲线身份。
Yang 的原 theta 平方公式在权零的比例常数非零，所以这两条曲线
的复中心 $L$ 值非零；其解析秩为零。
此处没有从一个数据库的代数秩零倒推解析中心非零。

## 5. 第三条实际秩二曲线的同图接口

将 R231 的 $Q_{+,0}$ 同时作 $[2]$ 拉回，仍记为 $Q_{+,0}$。
它是原八项 Mumford 运输，保持整个十七处向量。
定义
$$
Q_{+,v}=Q_{+,0}\mathcal V.
$$
原准确归一为
$$
Q_{+,0}A_0=-\frac{\kappa_4}{5}S_{68}(2z),\qquad
Q_{+,0}S_{289}(2z)=-320\kappa_4 B(2z),
$$
$$
Q_{+,0}S_{4913}(2z)=-\kappa_4S_{19652}(2z),\qquad B=A_{34}.
$$
所以三条新 primitive 来源准确给
$$
\boxed{\begin{aligned}
Q_{+,v}H(2z)&=-\frac{i\kappa_4}{110}S_{68}(2z),\\
Q_{+,v}S_{2312}(2z)&=-640i\kappa_4 B(2z),\\
Q_{+,v}S_{39304}(2z)&=2i\kappa_4S_{19652}(2z).
\end{aligned}}
\tag{15}
$$
特别第二行把新型的实际 $\lambda^2$ 行送回合法 rank-two 曲线 E34。
在 $p>19$ 上，这些非零标量全是单位。
这组式子可以直接用于原有限投影；它没有断言一个来源中央为零便使
任意平移后的中央行也为零。

## 6. 同一 gauge 的完整 Mellin 行与两个参考单位

固定惰性 $p>19$，排除前篇固定分母，置
$$
d=p+1,\qquad c=272c_0,\qquad q_2=2^{p-1},\quad q_4=4^{p-1},
\qquad U_\pm=\alpha_\pm^d/17\in1+p\mathcal O_{K_p}.
$$
所有左侧用同一个 R245 完整泛函 $\mathcal J_c$。
记
$$
J_\vartheta(u)=\mathcal J_{c_0}(\vartheta;u),\quad
J_8(u)=\mathcal J_{4c_0}(S_8;u),\quad
C_p(u)=\frac{U_+^u+U_-^u}{2},\quad
D_p(u)=\frac{U_+^u-U_-^u}{2i}.
$$
两个 $J$ 的中心值均为一，但本篇不设其中央导数为零。
准确有
$$
\begin{aligned}
\mathcal J_c(O_\pm;u)&=q_4^uU_\pm^uJ_\vartheta(u),\\
\mathcal J_c(N_\pm;u)&=q_2^uU_\pm^uJ_8(u).
\end{aligned}
\tag{16}
$$
同样，$\mathcal J_c(A_0;u)=q_4^uJ_{17}(u)$，
$\mathcal J_c(H(2z);u)=q_2^uJ_{136}(u)$，
$\mathcal J_c(B(2z);u)=q_2^uJ_{34}(u)$。
三条秩二行的中心为零，故这些固定尺度单位不改变其中央导数。

令 $O_R=(O_++O_-)/2,O_I=(O_+-O_-)/(2i)$，
$N_R=(N_++N_-)/2,N_I=(N_+-N_-)/(2i)$。
(1)、(12) 准确成为
$$
\mathcal UO_R=iN_I,\quad\mathcal UO_I=-iN_R,
\qquad
\mathcal VN_R=iO_I,\quad\mathcal VN_I=-iO_R.
\tag{17}
$$
特别，写
$$
M_p(u)=2^{-(p-1)u}\frac{J_8(u)}{J_\vartheta(u)},\qquad M_p(0)=1,
$$
则在这一实际二维 CM 块上有完整中央运输矩阵
$$
\binom{\mathcal J_c(\mathcal UO_R;u)}
      {\mathcal J_c(\mathcal UO_I;u)}
=M_p(u)
\begin{pmatrix}0&i\\-i&0\end{pmatrix}
\binom{\mathcal J_c(O_R;u)}{\mathcal J_c(O_I;u)}.
\tag{18}
$$
这里的未知参考连接准确是
$$
M_p'(0)=J_8'(0)-J_\vartheta'(0)-(p-1)\log_p2.
\tag{19}
$$
所以 rank-zero 参考及尺度产生的导数均已保留。

若 $j(G)=\mathcal J_c(G)'(0)$，则
$$
\begin{aligned}
j(O_R)&=J_\vartheta'(0)+(p-1)\log_p4+\frac{p-1}{2}\log_p17,\\
j(N_R)&=J_8'(0)+(p-1)\log_p2+\frac{p-1}{2}\log_p17,\\
j(O_I)&=j(N_I)=\frac{d}{2i}\log_p\frac{4+i}{4-i}\ne0.
\end{aligned}
\tag{20}
$$
这些式子来自全部解析单位的导数，未使用一个不存在的 $u\mapsto-u$ 偶性。
(15) 也可逐项直接取完整 $\mathcal J_c$，给实际 E34 的同图中央行。

## 7. R245 伴随的真正转置行，包括全部交换差

取 R245 的固定
$$
a=-\frac{14548243}{4370281080},\qquad
F=S_8^{17},\qquad C_*,\qquad
\nabla_8^2C_*=H-aK_I.
$$
作 $[2]$ 拉回，记
$$
F_2(z)=F(2z),\quad C_2(z)=C_*(2z),\quad
\nabla_2=\partial_z-F_2'/F_2.
$$
由于两个普通导数各产生因子二，准确有
$$
\nabla_2^2C_2=4\bigl(H(2z)-aN_I(z)\bigr).
\tag{21}
$$
现在定义一个完整的实际转置行
$$
\Psi_p(u)=\frac14\mathcal J_c(\mathcal V\nabla_2^2C_2;u).
$$
(12) 及五块表给出整条解析恒等式
$$
\boxed{
\Psi_p(u)=\frac i{22}q_4^uJ_{17}(u)
           +ia\,q_4^uC_p(u)J_\vartheta(u).
}
\tag{22}
$$
因此 $\Psi_p(0)=ia$；它不是中心质量零的原 $\Phi_*$。
这已经把一个新的完整伴随行准确传回原 E17 和实际参考，
不是只给有限来源的可逆矩阵。

为明确 (22) 中没有偷移协变导数，写 (5) 的固定有限展开
$\mathcal V=\sum_s b_s\mathcal T_s$，并置
$$
a_s=\partial_z\log\frac{\mathcal T_sF_2}{F_2}.
$$
逐项普通微分给准确恒等式
$$
\mathcal V\nabla_2^2C_2
=\nabla_2^2\mathcal VC_2+\mathscr E,
$$
$$
\boxed{
\mathscr E=
\sum_s b_s\left\{-2a_s\nabla_2(\mathcal T_sC_2)
                    +(a_s^2-a_s')\mathcal T_sC_2\right\}.
}
\tag{23}
$$
所有 $a_s$ 都是固定的椭圆有理连接差。
平移后的对数取标准 $p$ 进支
$\log_p r(2(z-s))$，包括常数 $\log_p r(-2s)$。
出现的 $s$ 在 $P,Q$ 坐标中两坐标均为奇数，故 $2s$ 是真正八挠点，
没有落在 $r$ 的二挠零极点上。
对奇好素位这些值都是单位，所有平移 germ 都真实有定义。
改变对数支只改变一个 $F_2$ 的常数倍；(23) 的完整组合不变。

由 (5) 与原 $i$ 作用交换，$\mathcal VC_2$ 仍有 $i$ 特征 $-1$，
所以 $g=z^{-2}\mathcal VC_2$ 在原点正则。
令
$$
W=zF_2'/F_2,\quad W_0=W-dcz^d,\quad E=z\partial_z,
$$
$$
f(u)=\mathcal J_c(g;u),\quad
g_1(u)=\mathcal J_c(W_0g;u),\quad
h(u)=\mathcal J_c((W_0^2+EW_0-W_0)g;u).
$$
则 (23) 的全部 Mellin 形式是
$$
\boxed{\begin{aligned}
4\Psi_p(u)={}&(du+1)(du+2)f(u)
 +du(d-3-2du)f(u-1)+d^2u(u-1)f(u-2)\\
&-2(du+1)g_1(u)+2dug_1(u-1)+h(u)
 +\mathcal J_c(\mathscr E;u).
\end{aligned}}
\tag{24}
$$
这里 $f(0)$ 不必为零。求中央导数时必须保留
$$
\begin{aligned}
4\Psi_p'(0)={}&3df(0)+2f'(0)+d(d-3)f(-1)-d^2f(-2)\\
&-2g_1'(0)+2dg_1(-1)+h'(0)
 +\mathcal J_c(\mathscr E)'(0).
\end{aligned}
\tag{25}
$$
$g_1(0)=h(0)=0$ 是由 $W_0(0)=0$ 得到，而非删掉 (23)。
R245 的原半径 $R=p^{-1/(2p)}$ 仍适用，但平移后的对数要付新的成本。
它在八挠点展开一般有线性首项；若写成
$\log_p r(-2s)+\log(1+u_s(z))$，则
$u_s=\widetilde u_s(u_0(z))$，其中 $u_0=x^{-1/2}$ 是原整形式参数，
$\widetilde u_s\in u_0\mathcal O[[u_0]]$。
原 R54/R245 半径上 $\|u_0(z)\|_R=R$，所以 $\|u_s\|_R\le R$；
这里不声称全部加法坐标 $z$ 的系数都整。
因此
$$
\|\log(1+u_s)\|_R\le
\sup_{n\ge1}p^{v_p(n)}R^n=p^{1/2}.
$$
最大成本来自 $n=p$，不能继续用原点二阶对数的范数一界。
作同一共同 gauge 后，固定阶微分、原连接差的原点正则 germ 及最后除以 $z^2$
至多再损失固定次半径 $R^{-C}$。
故对应 Newton 系数的赋值仍至少为
$h(p-1)/(2p)-1/2-C/(2p)$，随 $h$ 趋于无穷。
全部尾项收敛，(24)–(25) 是包含这项真实成本的完整公式。

## 8. 两个原 rank-two 零条件迫出两个独立的固定对数

原 R245 行仍满足
$$
J_{136}'(0)-\Phi_*'(0)
=\frac{ad}{2i}\log_p\frac{4+i}{4-i}.
\tag{26}
$$
对 (22) 使用真实中心一的单位归一
$$
\widehat\Psi_p(u)=
\frac{\Psi_p(u)}{ia\,q_4^uJ_\vartheta(u)}
=C_p(u)+\frac1{22a}\frac{J_{17}(u)}{J_\vartheta(u)}.
\tag{27}
$$
所有参考导数在这个商中按普通求导法则抵消；不是把它们先设为零。
故若两条实际曲线同时满足 $J_{17}'(0)=J_{136}'(0)=0$，则
$$
\boxed{
\Phi_*'(0)=-\frac{ad}{2i}\log_p\frac{4+i}{4-i},\qquad
\widehat\Psi_p'(0)=\frac{p-1}{2}\log_p17.
}
\tag{28}
$$
这两个数不仅非零，而且在代数数系数上线性无关。
确实，若 $17^m((4+i)/(4-i))^n$ 是根单位，则比较
$\mathbb Q(i)$ 中 $(4+i)$ 与 $(4-i)$ 的赋值，给 $m+n=m-n=0$。
对 $p\ne17$ 二者均为 $p$ 进单位；对数在单位上的核是根单位，
所以两个对数先在 $\mathbb Q$ 上线性无关。
Brumer 的 $p$ 进对数定理遂给代数系数线性无关。
所用的准确形式见 Sharifi 作者讲义 Theorem 1.5.17，核读日期 2026-11-13。

式 (28) 是对两个**实际剩余中央行**的约束。
若今后由原 E34 行和同一完整图证明这两行存在一个非平凡代数系数线性关系，
则三条原 rank-two 中央导数不能同时为零。
本篇没有声称 (5) 的有限可逆性自动给这条关系：
具体尚存的项正是 (24) 的 $W$、两个移权值和 (23) 的实际交换差。

## 来源与精确证书

- 原十六格和四项 theta 群运输：R239；实际新多项式与首项：R243。
- 旧五维 primitive 来源、$Q_{+,0}$ 及全部旧归一：R231。
- 原 E8 参考、线丛半特征和完整尺度：上述 E8 参考笔记；原对数伴随：R245。
- T. Yang，*Theta liftings and Hecke L-functions*，J. reine angew. Math. 485 (1997)，25–53，
  原局部—全局 theta 平方公式及 Corollary 2.10，
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- A. Brumer，*On the units of algebraic number fields*，Mathematika 14 (1967)，121–124，
  [DOI](https://doi.org/10.1112/S0025579300003703)；准确的 $p$ 进单位对数形式见
  R. Sharifi，[Iwasawa Theory，Theorem 1.5.17](https://math.ucla.edu/~sharifi/notes/iwasawa-ch01.html)。
- [精确脚本](../scripts/check-third-dyadic-cm17-bidirectional.py) 和
  [输出](../scripts/check-third-dyadic-cm17-bidirectional.json)
  在 $\mathbb Q(\zeta_{16})$ 中验证真实两个投影、双向算子、Fourier 等变、
  CM 负方向的两个相位，以及 (14) 的完整四阶展开和三个 primitive 常数。
  只有有理运算，不使用数值识别或目标素数扫描。
