# R582 — 原 Norm2 两个完整深补项、真实二态与五线算术余域

日期：2026-11-14。**状态：已证明。**

本篇接 R576 的同一个三线单位余域。其内
$U$ 深、$V$ 单位与 $V$ 深、$U$ 单位这两个区域的并集
由原 $c$ 反射保持，故整个反对称行准确返回原 $\rho_0$。
不需要给任何新状态增添算术中央零假设。

为计算这两个实际补项，本文支付 entire degree $12/84$ 的
单层绝对核心和 degree $168$ 的完整平方核心，
并在同一个原六输入上建立两套真正二态。
全部 $q_n$、$\kappa^{-n}$、$E/G/Y/W$ 和各自单位条件随框架完整运输。
第4节保新状态的整个 $S_2$ 条件质量和六次矩；
第5节将全部新补项重新放入原 $S/T$ 总行，留下五条明确单位线。

## 1. 原测试、Norm2 坐标及整个并域

沿用
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R539](R539-original-degree8-mixed-st-core-and-amplified-central-domain.md)、
[R553](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)、
[R571](R571-original-common-deep-complement-and-two-sigma-tail.md)、
[R576](R576-original-single-sigma-complements-and-three-line-domain.md)
的全部射线、固定坏集和周期，不另加同余。
记
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
\tag{1}
$$
原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d)$，
$$
\rho_0=-\nu_\sigma^{\otimes6}/84,\quad
\mu_0=\mathcal P_C\rho_0,\quad
\nu_4=-\mathcal P_C\nu_\sigma^{\otimes4}/84 .
$$
原 $D_4,C,H_1,A,E,G,Y,W$ 及 $q_n,\ell,a_n=q_n\ell$
完全按 R576 (3)–(5)，特别
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
a=2+3\omega,\quad g=3-2\omega,\quad
D=D_4+c+ad=F-C .
\tag{2}
$$
$q_n$ 是原三 carry 的平均，
$$
q_n=\frac1{3b\Omega^6}\sum_{j=0}^2
1_{\Gamma_{n,j}}\widehat P_p(D_j/\kappa^n,E_j,G),\qquad
\widehat P_p=\mathcal R_pP_p,
\tag{3}
$$
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
 -1_{W\ {\rm unit}}\log\langle W\rangle\}.
\tag{4}
$$
以下所有参数变化都不改变 $\widehat P_p$ 的原 $\lambda,\kappa$
系数和整右逆。

取原真实 Norm2 坐标
$$
U=c+\omega d,\quad V=c-\omega d,\quad
c=(U+V)/2,\quad d=\omega^2(U-V)/2 .
\tag{5}
$$
令 $\alpha=1-\omega$，则
$$
D=D_4+\alpha U+\omega V,\quad
u=-(U+\omega^2V)/2 .
\tag{6}
$$
R576 的原余域为
$$
\mathscr V_3=\{U+V,U-V,U+\omega^2V\ {\rm unit}\},
$$
$$
U_n^{\times,\times}
=\int_{\mathscr V_3}(a_n-a_n\circ R_c)\,d\Delta,\qquad
\Delta=\rho_0-\eta .
\tag{7}
$$
原 $R_c$ 在此准确为 $(U,V)\mapsto(-V,-U)$，
并满足 $\Delta-R_{c,*}\Delta=3\rho_0$。

现在定义两个整个原深补项
$$
\boxed{
C_{U;n,m}=\int_{\{U\in p^m\}}a_n\,d\rho_0,\qquad
C_{V;n,m}=\int_{\{V\in p^m\}}a_n\,d\rho_0,\qquad n,m\ge1 .
}
\tag{8}
$$
它们不预先要求另一个 Norm2 坐标为单位。
由于 (5) 整可逆，$U,V$ 同时深一层恰为 $c,d$ 同时深一层。
记 R571 的整个交项仍为
$$
I_{n,1}=\int_{\{c,d\in p\}}a_n\,d\rho_0 .
\tag{9}
$$

## 2. 两个完整框架与实际二态

### 2.1 全部四伴随和整格

以下 $\epsilon$ 取 $U$ 或 $V$，以 $Z_\epsilon$ 表示该真实轴。
定义表如下：

|$\epsilon$|$Z_\epsilon$|$\alpha_\epsilon$|$T_\epsilon$|$r_\epsilon$|$R_\epsilon$|
|---|---|---|---|---|---|
|$U$|$U$|$1-\omega$|$D_4+\omega V$|$3/4$|$3T_U-4\alpha U$|
|$V$|$V$|$\omega$|$D_4+(1-\omega)U$|$1/6$|$T_V-6\omega V$|

置
$$
q_\epsilon=\alpha_\epsilon Z_\epsilon,\qquad
e_\epsilon=q_\epsilon-r_\epsilon T_\epsilon,\qquad
D=T_\epsilon+q_\epsilon .
\tag{10}
$$
两套正交度数准确为
$$
\begin{array}{c|cc|cc}
&N(T_\epsilon)&N(Z_\epsilon)&N(D)&N(R_\epsilon)\\ \hline
U&8&2&14&168\\
V&12&2&14&84 .
\end{array}
\tag{11}
$$
$T_\epsilon\perp Z_\epsilon$、$D\perp R_\epsilon$，
且
$$
e_U=-R_U/4,\qquad e_V=-R_V/6 .
$$
两套二维 span 完全相同；从 $(T_U,U)$ 到 $(D,R_U)$ 的行列式
为 $-7(1-\omega)$，从 $(T_V,V)$ 到 $(D,R_V)$ 为 $-7\omega$。
这些都是当前处单位。

设
$$
(c_{Y,U},c_{W,U})=(-\omega/2,\,(-4+\omega)/6),\qquad
(c_{Y,V},c_{W,V})=(-(1+3\omega)/2,\,(3-7\omega)/2).
$$
四个共同伴随定义为
$$
\boxed{
E_\epsilon=E-e_\epsilon,\quad
G_\epsilon=G-ge_\epsilon,\quad
Y_\epsilon=Y-c_{Y,\epsilon}e_\epsilon,\quad
W_\epsilon=W-c_{W,\epsilon}e_\epsilon .
}
\tag{12}
$$
每个伴随都与 $T_\epsilon,Z_\epsilon,D,R_\epsilon$ 正交。
所以 (12) 同时给整个原观察的准确逆表达，不只给某条边际。

完整六行框架
$(T_\epsilon,Z_\epsilon,E_\epsilon,G_\epsilon,Y_\epsilon,W_\epsilon)$
的行列式与范数为
$$
\begin{array}{c|c|c}
U&22568+14560\omega&2^6\,3\,7^2\,13^3\,19\\
V&-10192-12376\omega&2^6\,7^2\,13^3\,19 .
\end{array}
\tag{13}
$$
把四个伴随乘 $24$ 后，三个纯 $C$ 共轭的全框架均为整数；
再乘原 $\eta$ 的 $H$ 矩阵也仍整。
$(T,Z,D,R)$ 的原三支非零 mod $2$ 系数数目为
$(4,2,4,4),(6,2,6,6),(6,2,6,6)$；
乘 $H$ 后分别为
$(4,2,2,4),(6,2,4,6),(6,2,4,6)$。
所以所有需要的轴都是 standard even，保整个余伴随格。
后文二态只以 $\mu_0$ 为起始来源，不把这些计数当成新的算术识别。

### 2.2 whole degree12、84 与168的绝对规范

令 $K_N$ 表示提出外部 $\lambda$ 后的原完整普通核心。
R539 已证明 entire $\mathcal S_8$ 上
$$
K_8=\frac14\sum_{t\in E[4]}\mathsf T_t^8
 -\frac12\sum_{t\in E[2]}\mathsf T_t^8,\qquad K_8^2=I.
\tag{14}
$$
所有 quarter lift 和两个负中心号均使用该已付规范。

对 $N=12$ 或 $84$，令 $m=N/4$（为奇数）。
canonical 二挠 lift 为
$$
\mathsf T^{(N)}_{(s+r\omega)/2}e_j
=(-1)^{s(j+mr)}e_{j+Nr/2},\qquad s,r=0,1 .
$$
完整四项和准确给
$$
\boxed{
A_N:=\frac12\sum_{t\in E[2]}\mathsf T_t^{(N)},
\qquad A_Ne_j=e_{(1+N/2)j},\qquad A_N^2=I .
}
\tag{15}
$$
第三个非零点的负 cocycle 已在 $mr$ 中，不能删掉。

当前 ray 的全模数为
$$
g_\pi\equiv19\pmod{24},\qquad g_\pi\equiv43\pmod{168}.
$$
第一项是 $19\equiv13\cdot7\bmod24$；
中心因子 $13=1+12$ 的完整 cocycle 商为 $14$，故它不改变 lift。
因此 $K_{12}$ 与 $A_{12}$、$K_{84}$ 与 $A_{84}$ 分别只差标量。

真实非零 sigma 锚
$$
\sigma(2\delta z)\in\mathcal S_{12},\qquad
\sigma(2\delta\gamma_7z)\in\mathcal S_{84}
$$
在三个非零 canonical 二挠下均取特征 $-1$，
所以 $A_N$ 对两锚都取 $-1$。
原 sigma 的实际核心为 $\beta=-\lambda$，
固定 CM 拉回与普通核心严格交换，遂准确得到
$$
\boxed{K_{12}=A_{12},\qquad K_{84}=A_{84}.}
\tag{16}
$$
这是原普通 trace 的归一；不与其他 Cartier 规范的绝对符号互换。

对 $N=168$，当前 ray 给
$$
g_\pi\equiv43+168\omega\pmod{336},\qquad
g_\pi^2\equiv169=1+168\pmod{336}.
\tag{17}
$$
平方的完整中心商为 $(169^2-1)/168=170$，为偶数。
因此 $K_{168}^2$ 在 entire $\mathcal S_{168}$ 上为标量。
用真实非零锚
$$
\Theta(2\delta\gamma_7z)\in\mathcal S_{168},
\quad N(2\delta\gamma_7)=84
$$
定标：其实际核心为 $\beta$，故归一特征平方为一。
于是
$$
\boxed{K_{168}^2=I\quad\text{于整个 }\mathcal S_{168}.}
\tag{18}
$$
(18) 不凭 projective 交织猜单层符号；实际二态中的单层符号由
下面同一个完整来源的两套矩形比较决定。

### 2.3 两套真正二态

为了将所有外部标量统一成 $\beta$，置
$$
J_\epsilon=-K_{T_\epsilon},\qquad
\mu_{\epsilon,0}=\mu_0,\qquad
\mu_{\epsilon,1}=J_\epsilon\mu_0 .
\tag{19}
$$
这是完整六变量定义，具体有限来源为
$$
\boxed{
J_U=\frac12\sum_{E[2]}\mathsf T_{T_U,t}^{8}
 -\frac14\sum_{E[4]}\mathsf T_{T_U,t}^{8},\qquad
J_V=-\frac12\sum_{E[2]}\mathsf T_{T_V,t}^{12}.
}
\tag{20}
$$
所以没有未说明的辅助来源或未定 scalar。
原四个伴随在每一项中完整保持。

原 $D$ whole 核和 $Z_\epsilon$ whole $S_2$ 核都为 $\beta$。
两套框架的同时一层深域相同，物理缩放也都是该完整二维平面
乘 $\kappa$、其正交补保持不动。因此比较其真正限制测度，得
$$
(-K_{R_\epsilon})\mu_0
=(-K_{T_\epsilon})\mu_0=\mu_{\epsilon,1}.
\tag{21}
$$
这里先用了 $\mu_0$ 的两个已付 scalar 核，再比较同一个
全平面深域；不是由不同边际推交织。

$K_{T_\epsilon}^2=K_{R_\epsilon}^2=I$ 给两态的返回。
又 $Z_\epsilon\perp T_\epsilon$、$D\perp R_\epsilon$，
所以第一个表达保 whole $Z_\epsilon$，第二个表达保 whole $D$。
故在同一完整二态上，
$$
\boxed{
\begin{array}{c|c}
\text{实际轴核心}&\text{在 }(\mu_{\epsilon,0},\mu_{\epsilon,1})\text{ 上}\\ \hline
D,\ Z_\epsilon&\beta I\\
T_\epsilon,\ R_\epsilon&\beta X,\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\end{array}}
\tag{22}
$$
只在各自正交的两轴内交换核心，不宣称 $D$ 与 $Z_\epsilon$
的物理缩放相互交换。
特别对 $i=0,1$ 和任意非负 $n,m$，
$$
\boxed{
\begin{aligned}
\mu_{\epsilon,i}|_{\{D\in p^n,R_\epsilon\in p^m\}}
 &=\beta^{n+m}
 (P_{D,\kappa^n}P_{R_\epsilon,\kappa^m})_*
 \mu_{\epsilon,i+m\ ({\rm mod}\ 2)},\\
\mu_{\epsilon,i}|_{\{T_\epsilon\in p^n,Z_\epsilon\in p^m\}}
 &=\beta^{n+m}
 (P_{T_\epsilon,\kappa^n}P_{Z_\epsilon,\kappa^m})_*
 \mu_{\epsilon,i+n\ ({\rm mod}\ 2)} .
\end{aligned}}
\tag{23}
$$

## 3. 两个整个补项的完整双参数式

对 $s\in p\mathcal O,t\in\mathcal O$，定义
$$
\begin{aligned}
\mathscr C_{\epsilon,i}(s,t)
=\int_{\{E_\epsilon\ {\rm unit}\}}
&\widehat P_p\bigl(T_\epsilon+tq_\epsilon,\
 E_\epsilon+s(tq_\epsilon-r_\epsilon T_\epsilon),\\
&\hspace{40mm}
 G_\epsilon+gs(tq_\epsilon-r_\epsilon T_\epsilon)\bigr)\\
{}\cdot d_p\{&
1_{Y_\epsilon\ {\rm unit}}
 \log\langle Y_\epsilon+c_{Y,\epsilon}
                 s(tq_\epsilon-r_\epsilon T_\epsilon)\rangle\\
&-1_{W_\epsilon\ {\rm unit}}
 \log\langle W_\epsilon+c_{W,\epsilon}
                 s(tq_\epsilon-r_\epsilon T_\epsilon)\rangle\}\,
d\mu_{\epsilon,i}.
\end{aligned}
\tag{24}
$$
两个单位条件分别保留。由于 $s\in p\mathcal O$，
它们与移动后的真实条件准确等价，没有省略固定尺度 log。

**定理1（所有深度及正确状态）。** 令
$$
s_{n,m}=\kappa^{\min(n,m)},\quad
t_{n,m}=\kappa^{(m-n)_+},\quad
i_{n,m}=\min(n,m)\pmod2 .
$$
则对全部 $n,m\ge1$，
$$
\boxed{
C_{\epsilon;n,m}
=\frac{\beta^{n+m}}{b\Omega^6}
 \mathscr C_{\epsilon,i_{n,m}}(s_{n,m},t_{n,m}) .
}
\tag{25}
$$

**证明。** (8) 中的 pure $C$ 三分支先在原 $\mu_0$ 上准确归为
$$
\frac1{b\Omega^6}\int_{\{D\in p^n,E\ {\rm unit},
 Z_\epsilon\in p^m\}}
\widehat P_p(D/\kappa^n,E,G)\ell\,d\mu_0 .
\tag{26}
$$
这里只使用 $\mu_0$ 的 pure $C$ 不变性。
新状态未必仍有该不变性；在 (26) 后不对它免费重作三支平均。

若 $m\le n$，在 $D\in p^n$ 内，
$Z_\epsilon\in p^m$ 当且仅当 $R_\epsilon\in p^m$：
$$
R_U=3D-7q_U,\qquad R_V=D-7q_V .
$$
应用 (23) 第一式，状态为 $m\bmod2$，
$D/\kappa^n$ 回到 $T_\epsilon+q_\epsilon$，
$e_\epsilon$ 乘 $\kappa^m$，四伴随保持。
这给 (24) 的 $(s,t)=(\kappa^m,1)$。

若 $m\ge n$，在 $Z_\epsilon\in p^m$ 内，
$D\in p^n$ 当且仅当 $T_\epsilon\in p^n$。
应用 (23) 第二式，状态为 $n\bmod2$，
$D/\kappa^n$ 变为 $T_\epsilon+\kappa^{m-n}q_\epsilon$，
$e_\epsilon$ 变为
$\kappa^n(\kappa^{m-n}q_\epsilon-r_\epsilon T_\epsilon)$。
四伴随仍不动。两种范围在 $m=n$ 完全相同，证明 (25)。证毕。

特别所有 $n\ge1$ 的一层实际补项都使用第一个新状态：
$$
\boxed{
C_{\epsilon;n,1}
=\frac{\beta^{n+1}}{b\Omega^6}\mathscr C_{\epsilon,1}(\kappa,1).
}
\tag{27}
$$
$\beta^{-n}$ 倍准确与 $n$ 无关，但不能将状态 $1$ 改回状态 $0$。

## 4. 全 S2 条件质量与准确六次首层

### 4.1 两个完整五变量系数

(19) 保 whole $Z_\epsilon$ 的 $\mathcal S_2$，
所以实际来源准确分离为
$$
\boxed{
\mu_{\epsilon,i}
=\nu_\Theta(Z_\epsilon)\otimes\Lambda_{\epsilon,i,0}
 +\nu_\Sigma(Z_\epsilon)\otimes\Lambda_{\epsilon,i,2},
\qquad \Sigma=\sigma^2,\quad\Theta=x_\wp\sigma^2 .
}
\tag{28}
$$
两条 $\Lambda$ 保其余真实五变量
$(T_\epsilon,E_\epsilon,G_\epsilon,Y_\epsilon,W_\epsilon)$。

这些系数有明确原来源，不是抽象未知：
令 $\Phi_U$ 是将 $(\xi_1,\xi_2,\xi_3,x,V)$ 送到上述五输出的
完整映射；因五输出不含 $U$，可用 $U=0$ 写它。
$\Phi_V$ 同理用 $(\xi_1,\xi_2,\xi_3,x,U)$。
其完整矩阵在证书中，行列式分别为
$-4004-11284\omega$、$1092-5096\omega$，当前处均为单位。
R553 的原双张量给
$$
\boxed{
\begin{aligned}
\Lambda_{U,0,0}&=-\omega\,(\Phi_U)_*(\nu_4\otimes\nu_\Sigma(V)),&
\Lambda_{U,0,2}&=\omega\,(\Phi_U)_*(\nu_4\otimes\nu_\Theta(V)),\\
\Lambda_{V,0,0}&=\omega\,(\Phi_V)_*(\nu_4\otimes\nu_\Sigma(U)),&
\Lambda_{V,0,2}&=-\omega\,(\Phi_V)_*(\nu_4\otimes\nu_\Theta(U)),\\
\Lambda_{\epsilon,1,j}&=J_\epsilon\Lambda_{\epsilon,0,j}
\quad(j=0,2).
\end{aligned}}
\tag{29}
$$
最后一行只在第一 $T_\epsilon$ 输出作 (20) 的真实有限平移和，
逐个保持四个伴随，包含全部中心系数。

### 4.2 六次矩的正确绝对常数

原实际展开为
$$
\sigma(z)=z+bz^7/210+\cdots,\qquad
x_\wp(z)=z^{-2}-bz^4/7+\cdots .
$$
因此
$$
\Sigma(z)=z^2+bz^8/105+\cdots,\qquad
\Theta(z)=1-\frac{2b}{15}z^6+\cdots .
$$
在次数至七内，两轴的全部非零矩恰为
$$
\boxed{
m_\Theta(0)=1,\qquad m_\Theta(6)=-96b\Omega^6,\qquad
m_\Sigma(2)=2\Omega^2 .
}
\tag{30}
$$
这里 $-96$ 是 $\Theta$ 的常数；
odd3 的 $B_3=\sigma(2z)/(2\sigma(z))$ 的六次矩 $216b\Omega^6$
属于另一来源，不能混用。

置 $\vartheta=-96b\Omega^6$。
对任意次数至六的多项式 $P(X)$，所有导数在 $X=T_\epsilon$ 取值，
定义
$$
\begin{aligned}
\mathcal B_0P&=P+\vartheta\alpha_\epsilon^6t^6P^{(6)}/6!,&
\mathcal B_2P&=\Omega^2\alpha_\epsilon^2t^2P'',\\
\mathcal E_0P&=-r_\epsilon T_\epsilon P
 +\vartheta\alpha_\epsilon^6t^6
 \{P^{(5)}/5!-r_\epsilon T_\epsilon P^{(6)}/6!\},\\
\mathcal E_2P&=\Omega^2\alpha_\epsilon^2t^2
 \{2P'-r_\epsilon T_\epsilon P''\}.
\end{aligned}
\tag{31}
$$
直接逐单项式应用 (30)，$\mathcal B_jP$ 正是
$P(T_\epsilon+tq_\epsilon)$ 对相应 $S_2$ 因子的积分；
$\mathcal E_jP$ 正是
$(tq_\epsilon-r_\epsilon T_\epsilon)P(T_\epsilon+tq_\epsilon)$
的积分。后一测试最高次数七，所以 (30) 已给全部矩。
该身份保整个条件系数，不是单个边际的矩比较。

记
$$
P(X)=\widehat P_p(X,E_\epsilon,G_\epsilon),\qquad
Q(X)=(\partial_2+g\partial_3)\widehat P_p(X,E_\epsilon,G_\epsilon),
$$
$$
\ell_{\epsilon,0}=d_p\{1_{Y_\epsilon\ {\rm unit}}\log\langle Y_\epsilon\rangle
 -1_{W_\epsilon\ {\rm unit}}\log\langle W_\epsilon\rangle\},
$$
$$
\ell_{\epsilon,1}=d_p\{c_{Y,\epsilon}1_{Y_\epsilon\ {\rm unit}}/Y_\epsilon
 -c_{W,\epsilon}1_{W_\epsilon\ {\rm unit}}/W_\epsilon\}.
$$
以下五变量积分全部保 $\{E_\epsilon\ {\rm unit}\}$。定义
$$
\mathcal F_{\epsilon,i}(t)
=\sum_{j=0,2}\int(\mathcal B_jP)\ell_{\epsilon,0}
 \,d\Lambda_{\epsilon,i,j}\in p\mathcal O,
$$
$$
\mathcal G_{\epsilon,i}(t)
=\sum_{j=0,2}\int
 \{(\mathcal E_jQ)\ell_{\epsilon,0}
   +(\mathcal E_jP)\ell_{\epsilon,1}\}
 \,d\Lambda_{\epsilon,i,j}\in\mathcal O .
\tag{32}
$$
两者只有 $t^0,t^2,t^6$ 三种幂，且 $\widehat P_p$ 的全部
$p$ 依赖原样保留。

**定理2（完整首层）。** 对所有实际 $s\in p\mathcal O,t\in\mathcal O$，
$$
\boxed{
\mathscr C_{\epsilon,i}(s,t)
=\mathcal F_{\epsilon,i}(t)
 +s\mathcal G_{\epsilon,i}(t)+s^2\mathcal O .
}
\tag{33}
$$
尾对 $t$ 有界。证明是先在 $s=0$ 精确积分 (28)，再对多项式
与两个独立 log 各作一次位移，得到 (31)–(32)。
高项的唯一 log 分母为其次数 $r$；
$s^{r-2}/r$ 在当前 $p\ge71$ 下整，原来源有界，故给统一整尾。

与原 sigma 的零质量不同，$\Theta$ 的质量为一。
所以这里一般有 $t^0$ 边界，不能从 (33) 删掉
$\mathcal F_{\epsilon,i}(0)$，也不免费断言整个深尾趋零。
任何单位逆必须保 R553 的常数项或整个对应边界。

结合 (27)，准确有
$$
\boxed{
C_{\epsilon;n,1}
=\frac{\beta^{n+1}}{b\Omega^6}
\{\mathcal F_{\epsilon,1}(1)
 +\kappa\mathcal G_{\epsilon,1}(1)+p^2\mathcal O\}.
}
\tag{34}
$$
这是同一个原 $q_n\ell$ 的补项，未给新状态中央赋零。

## 5. 两个真实深区合并及全部算术总行

令
$$
\mathscr S=\{U\in p,V\ {\rm unit}\}\ \sqcup\
             \{V\in p,U\ {\rm unit}\}.
$$
该并域完整包含于 $\mathscr V_3$，且由 $R_c$ 保持。
因此对同一个完整 $a_n$，
$$
\int_{\mathscr S}(a_n-a_n\circ R_c)\,d\Delta
=3\int_{\mathscr S}a_n\,d\rho_0
=3\{C_{U;n,1}+C_{V;n,1}-2I_{n,1}\}.
\tag{35}
$$
这一步只对完整并域换元，不把两单支分别认成反射不变。

剩余域恰为
$$
\boxed{
\mathscr V_5=\{U,V,U+V,U-V,U+\omega^2V\ {\rm unit}\},
\qquad
U_n^{(5)}=\int_{\mathscr V_5}(a_n-a_n\circ R_c)\,d\Delta .
}
\tag{36}
$$
没有额外的 $L=\omega U+\delta V$ 单位条件。
由 (7)、(35) 和 R576 的完整总行，得到

**定理3（原算术比较的完整五线形式）。**
$$
\boxed{
\begin{aligned}
3\beta^n(J'_S-6\delta J'_T)
={}&\mathcal N_n+U_n^{(5)}\\
&+3\{C_{c;n,1}+C_{d;n,1}
      +C_{U;n,1}+C_{V;n,1}-3I_{n,1}\}.
\end{aligned}}
\tag{37}
$$
四个整个单深项的两两交域都是同一个 $c,d$ 共同深域；
(37) 的系数 $-3$ 与完整包含排除一致。
本式保 native 残差 $\mathcal N_n$、两个原 sigma 深项、
两个新 Norm2 深项和整个剩余五线域。

更具体地，令 R576 的 $L_0,L_1$ 保持原定义，置
$$
F_0=\mathcal F_{U,1}(1)+\mathcal F_{V,1}(1)\in p\mathcal O,\qquad
F_1=\mathcal G_{U,1}(1)+\mathcal G_{V,1}(1)\in\mathcal O .
$$
R567 的 $C_0,C_1$ 与 R571 的真实 $K_1$ 亦保持原定义。
由 (34)、(37) 得全首层
$$
\boxed{
\begin{aligned}
\frac{3b\Omega^6}{p}(J'_S-6\delta J'_T)
\equiv{}&
\beta(C_0/p+\lambda^2C_1)\\
&+3\beta\{(L_0+F_0)/p+\lambda^2(L_1+F_1)\}
-9\lambda^4K_1\\
&+\frac{b\Omega^6}{p\beta^n}U_n^{(5)}
\pmod p .
\end{aligned}}
\tag{38}
$$
所有原 log 质量及正确状态已在显示项中；没有省略
$F_0/p$，也没有将 fixed $S_2$ 六次矩当作某个未知负矩的值。

(27)、R576 和 R571 的准确全深身份还给：
$\beta^{-n}U_n^{(5)}$ 对全部 $n\ge1$ 准确相同。
因此增加原 carry 深度只重现同一个全算术式；
不能凭局部首项非零或深度变化删除 (36)。

## 6. 所有剩余测试仍是原混合权

R576 已付原五线域上的整个来源为
$$
(\nu_B(v)\otimes\Theta_B+\nu_{\sigma^3}(v)\otimes\Theta_P)
\otimes
[-\delta(\nu_\Theta(U)\otimes\nu_\Sigma(V)
 +\omega^2\nu_\Sigma(U)\otimes\nu_\Theta(V))],
\tag{39}
$$
其中 $\Theta_B,\Theta_P$ 是它的完整三维实际伴随，
并非仅它们的质量。原 $C=v/\delta$；在其余原
$(Z,Q,r)$ 上置
$$
A_0=(-2+\omega)Z/2+(4+3\omega)Q/2+2\delta r,\qquad
J_0=\delta Z/6+(1-2\omega)Q/2+\omega^2r .
$$
全部原观察仍为
$$
F=J_0+(1-\omega)U+\omega V,\quad
Y=A_0-\delta U/2+(3+2\omega)V/2,
$$
$$
W=A_0+(-1+2\omega)U/2+(7+10\omega)V/2,\quad
G=13H_1+gF .
\tag{40}
$$
所以 (36) 中的 $D_j/\kappa^n,E_j$、两个 Mellin cut 和所有
$R_c$ 转置都仍按原线性式计算。
特别不能把 $U$ 或 $V$ 单位逆中移动后的 $F,Y,W$ 改回未移动的行。

本篇的新核心用于实际 (8)、(35)–(38)，没有另开无算术比较的
单位见证。未支付的仍是五线全混合行与已明确各补项之间的最终
消去或非消失。没有由新状态、边际质量或单个非零区域关闭主目标。

## 精确证书

- [check-r582-original-normtwo-deep-complements-and-five-line-domain.js](../scripts/check-r582-original-normtwo-deep-complements-and-five-line-domain.js)
- [check-r582-original-normtwo-deep-complements-and-five-line-domain.json](../scripts/check-r582-original-normtwo-deep-complements-and-five-line-domain.json)

脚本使用 BigInt 的 $\mathbf Q(\omega)$ 算术，保存全部六行和
五行框架、三个 $C$ 共轭与原 $H$ 后的整数半特征、
物理正交投影、行列式、完整二挠排列和中心平方。
对 (31) 的全部 $0,\ldots,6$ 次单项式逐项核定两个真实 $S_2$
矩公式，并从原 sigma/Weierstrass 展开核定 $\Theta$ 的 $-96$。
全深度的状态、域等价、整尾和总算术分区由正文直接证明；
未用有限素数样本或边际非零替代。
