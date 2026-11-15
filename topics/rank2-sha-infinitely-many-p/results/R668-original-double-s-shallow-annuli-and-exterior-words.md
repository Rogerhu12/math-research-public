# R668 — 原双 S 浅环带的完整四轴返回、七阶递推与全部外部词

日期：2026-11-15。**状态：已证明。**

本篇接 R664 的同一个双 $S$ 交域。
先把四个原 $Y_j$ 的全部交集写成真实来源上的有限物理词，
再证明共同伴随的第 $j$ 浅环带就是原 $A,Q,L,c,d,W_i$
同深第 $j$ 环带。对每个正层 $j$，原 carry 支撑还强迫 $D_*$ 深 $j$。
R665 的完整 $D_*$ 核因而允许一个准确四轴返回。

固定剩余深度以后，返回后的完整 carry 是 $\kappa^j$ 的
degree 至多六多项式。对应原 $S$ 浅层满足显示的七阶递推；
对应原 $T$ 与 $S$ 的单位 cut 完全一致，它们的差是同一个实际域上的
完整 log 级数。所有零阶质量、原 $Y$ 外部、第零浅层均保留。
这些局部行没有由原两个中央导数为零而单独获得零值。

## 1. 原四条 S 观察的完整交集

沿 R664 使用原
$$
\mu_0=\nu_4\otimes\nu_{\rm pair}(Q,L),\qquad
Y_0=A+Q,\quad Y_1=A+L,\quad Y_2=A-Q,\quad Y_3=A-L ,
$$
$$
N(A)=29,\quad N(Q)=N(L)=5,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1 .
$$
全部三个 A 伴随、原 $C$ 投影和原六输入均保留。
实际整数旋转 $\mathsf J(c,d)=(d,-c)$ 满足
$\mathsf J_*\mu_0=-\mu_0$，且
$Y_i=Y_0\mathsf J^{-i}$；所有下标按四取模。
记
$$
q_i=q_N\mathsf J^{-i},\qquad W_i=W\mathsf J^{-i},\qquad
W=A+b_QQ+b_LL,
$$
$$
b_Q=(11+6\omega)/5,\quad b_L=(2+12\omega)/5,\quad
b_Y=(20+3\omega)/17 .
\tag{1}
$$
$N\in4\mathbf Z_{\ge1}$，$\widehat P_p$ 是 R594 同一个整右逆多项式，
只依原 $p,\lambda,\kappa$，不随 carry 深度另选。

在固定深度 $n$ 定义原域
$$
E_i=\{Y_i\in p^n\},\quad
\Gamma_i=E_i\cap E_{i+1},\quad
\Omega_i=E_i\cap E_{i+2},\quad
\mathcal B_n=\{A,Q,L\in p^n\}.
$$
任意三个不同 $Y_i$ 在 $(A,Q,L)$ 上的行列式是 $\pm2$。
因此
$$
\boxed{\text{任意三个 }E_i\text{ 的交集均为 }\mathcal B_n.}
\tag{2}
$$
这同时付清任意两个 $\Gamma/\Omega$ 子域在一个 $E_i$ 内的交集；
没有用不相同的词像格替代它们。

设 $\eta_A=\chi_{29,p}\in\{\pm1\}$ 为原 odd29 的实际标量。
取
$$
R=Y_0+Y_1,\quad D_{10}=Y_0-Y_1,\quad
\mathcal E=5A-29(Q+L),
$$
并令
$$
B_{0,n}=P_{R,\kappa^n}P_{D_{10},\kappa^n},\quad
B_{i,n}=\mathsf J^i B_{0,n}\mathsf J^{-i},\quad
Q_i=Y_i-A .
$$
以下全是原同一个来源的完整测度身份：
$$
\begin{aligned}
\mu_0|_{E_i}
 &=\lambda^n(P_{Y_i,(-\kappa)^n})_*\mu_0,\\
\mu_0|_{\Gamma_i}
 &=\lambda^{2n}(B_{i,n})_*\mu_0,\\
\mu_0|_{\Omega_i}
 &=(-\eta_A)^n\lambda^{2n}
       (P_{A,\kappa^n}P_{Q_i,\kappa^n})_*\mu_0,\\
\mu_0|_{\mathcal B_n}
 &=\eta_A^n\lambda^{3n}
       (P_{A,\kappa^n}P_{Q,\kappa^n}P_{L,\kappa^n})_*\mu_0.
\end{aligned}
\tag{3}
$$
第一、第二式由 R664；后两式分别是实际正交的 A/Q 和 A/Q/L
共同深限制。所用 Q/L whole 核都是 R655 已定的 $\beta$，
不是未知二次符号。

令 $\mathcal U_i$ 为 $E_i$ 内其余三个 $Y$ 均不深的部分。
由 (2) 的真实包含排除，
$$
\boxed{
1_{\mathcal U_i}
=1_{E_i}-1_{\Gamma_i}-1_{\Gamma_{i-1}}-1_{\Omega_i}
 +2\,1_{\mathcal B_n}.}
\tag{4}
$$
所以对任意同一完整测试 $f$，只在各实际整像上使用其逆坐标，
$$
\begin{aligned}
\int_{\mathcal U_i}f\,d\mu_0
={}&\lambda^n\int fP_{Y_i,(-\kappa)^n}\,d\mu_0\\
&-\lambda^{2n}\int(fB_{i,n}+fB_{i-1,n})\,d\mu_0\\
&-(-\eta_A)^n\lambda^{2n}
   \int fP_{A,\kappa^n}P_{Q_i,\kappa^n}\,d\mu_0\\
&+2\eta_A^n\lambda^{3n}
   \int fP_{A,\kappa^n}P_{Q,\kappa^n}P_{L,\kappa^n}\,d\mu_0 .
\end{aligned}
\tag{5}
$$
这是五个原物理词的完整式；每一项都移动 $q_i$、单位 cut 和 log。
不能只对来源矩阵用 (5)，而把测试冻结。

两个邻边外部各自严格分成三个不交部分：
$$
\boxed{
\begin{aligned}
E_i\setminus\Gamma_i
&=\mathcal U_i\ \sqcup\
(\Gamma_{i-1}\setminus\mathcal B_n)\ \sqcup\
(\Omega_i\setminus\mathcal B_n),\\
E_i\setminus\Gamma_{i-1}
&=\mathcal U_i\ \sqcup\
(\Gamma_i\setminus\mathcal B_n)\ \sqcup\
(\Omega_i\setminus\mathcal B_n).
\end{aligned}}
\tag{6}
$$
R664 的固定邻边 $\Gamma_0$ 对 $i=0$ 使用第一行，
对 $i=1$ 使用第二行。
$\mathsf J$ 对这些完整域也循环运输；来源的负号与测试同时保持。
四个原总行仍是旋转后的同一 $S/T$ 行，不构成四个新增独立中央零。

## 2. 共同伴随浅层与原物理环带准确相同

以后只写 $i=0,1$ 和 $\Gamma_0$，其余邻边由 (2) 的原旋转得到。
R664 的正交框架为
$$
\operatorname{Gram}(R,D_{10},\mathcal E)
=\operatorname{diag}(126,10,9135),
\quad
A=(\mathcal E+29R)/63.
$$
在原输入上有准确线性恒等
$$
\begin{aligned}
\mathcal E-63A&=-29(Y_0+Y_1),\\
\mathcal E+63Q&=34Y_0-29Y_1,\\
\mathcal E+63L&=34Y_1-29Y_0 .
\end{aligned}
\tag{7}
$$
故在 $\Gamma_0$ 上，对 $0\le j<n$，
$$
\boxed{
v_p(\mathcal E)=j
\quad\Longleftrightarrow\quad
v_p(A)=v_p(Q)=v_p(L)=j.}
\tag{8}
$$
这里的等价是实际输入域，不是边际测度比较。

原 $c=(Q+2L)/5,\ d=(2Q-L)/5$ 还满足
$$
c\equiv-3A/5,\quad d\equiv-A/5\pmod{p^n}.
$$
同样
$$
W_0\equiv(-8-18\omega)A/5,\qquad
W_1\equiv(-4+6\omega)A/5\pmod{p^n}.
\tag{9}
$$
两个系数范数分别 $244/25,76/25$，新因子仅 $61,19$，
在当前 $p\ge71$ 的 ray 上都是单位。
因此 (8) 的同一个域还严格满足
$$
\boxed{v_p(c)=v_p(d)=v_p(W_0)=v_p(W_1)=j.}
\tag{10}
$$
特别正浅层确实落在原 $c,d$ 同时深的补域内。
但 (10) 不把旧未加双 Y cut 的 cd 补偿整条搬到这里：
原 $q_N$ 与全部额外条件依旧保持。

当 $n\ge N$，R664 的两 carry 门共同部分恰为
$\mathcal E\in p^N$；其浅补域按 $j=0,\ldots,N-1$ 分层。
由 (8)，这些正是原 A/Q/L 同浅的真实层，
同时属于原 L 浅域及原 Y/A 外部的相应部分。
这里只识别这些域；R662、R665 的不同完整测试未被互换。

## 3. 迫出的 D_* 深度和真正四轴 peel

保持 R664/R665 的
$$
D_*=D_4-aA,\quad C^\perp=C+\alpha D_*,
\quad \alpha=29/143,\quad
g=3-2\omega,\quad H_1^\perp=H_1+\alpha gD_* .
$$
准确有
$$
\boxed{
D_*\perp C^\perp,\qquad
D_*\perp H_1^\perp,\qquad
H_1^\perp-gC^\perp=H_1-gC.}
\tag{11}
$$
令
$$
G_\perp=13H_1^\perp+gC^\perp .
$$
所用 whole $D_*$ 核是 R665 在**全部六个 C 分支**的
$87D_*$、degree $37323$ 真覆盖上支付的
$$
\mu_0|_{D_*\in p^j}
=(\chi_D\lambda)^j(P_{D_*,\kappa^j})_*\mu_0,\qquad
\chi_D^2=1 .
\tag{12}
$$
不能改成未覆盖的 degree4147，也没有声称 D 核与 C 投影交换。
A/Q/L 三轴与 $D_*$ 正交。$\mathcal E$ 的原 whole 核为
$\eta_A\lambda$，已在 R664 由同一完整联合定标。

沿用 R664 的
$$
\begin{aligned}
e_0&=-(170+117\omega)/9135,&
v_0&=(-5-9\omega)(34Y_1-29Y_0)/315,\\
e_1&=-(170+291\omega)/9135,&
v_1&=(-5-3\omega)(34Y_0-29Y_1)/315 .
\end{aligned}
\tag{13}
$$
$D_*,C^\perp,H_1^\perp,\mathcal E,v_i$ 全与 $Y_i$ 正交。
在 $\Gamma_0$ 返回 $B_{0,n}$ 后，
原第 i 个 carry 条件是
$$
D_*+e_i\mathcal E+\kappa^n v_i\in p^N.
\tag{14}
$$
若 $1\le j<N\le n$ 且 $\mathcal E\in p^j\mathbf Z_p^\times$，
(14) **强迫 $D_*\in p^j$**。
只用 $e_i$ 整，不假定两个 $e_i$ 均为单位。

因此可真实同时应用 $\mathcal E,D_*$ 两核。
写
$$
\tau=\kappa^j,\quad M=N-j,\quad\ell=n-j,\qquad
V_j=P_{\mathcal E,\tau}P_{D_*,\tau}.
$$
一个完整物理词恒等为
$$
\boxed{
B_{0,n}V_j=
P_{A,\tau}P_{Q,\tau}P_{L,\tau}P_{D_*,\tau}\,B_{0,\ell}.}
\tag{15}
$$
证明只用正交投影的准确等式
$P_A^{\rm proj}+P_Q^{\rm proj}+P_L^{\rm proj}
 =P_R^{\rm proj}+P_{D_{10}}^{\rm proj}+P_{\mathcal E}^{\rm proj}$。
两边在 R/D10 上乘 $\kappa^n$，
在 $\mathcal E,D_*$ 上乘 $\kappa^j$，在其余两轴恒等。
这是同一个像格、同一个完整映射，未从标量相同猜词相等。

两种次序给相同的实际来源系数
$$
\boxed{a_{n,j}=(\eta_A\chi_D)^j\lambda^{2n+2j}.}
\tag{16}
$$
特别 $j\in4\mathbf Z$ 时未知两个符号均消去。

## 4. 同一固定单位 carry 与完整多项式权

置
$$
H_{i,\ell}=D_*+e_i\mathcal E+\kappa^\ell v_i,\qquad
K_{i,\ell}=H_{i,\ell}-14\alpha D_* .
$$
返回后的同一个实际门为
$$
\boxed{
\mathcal D_{i;M,\ell}
=\{\mathcal E\ {\rm unit},\ C^\perp\ {\rm unit},
                   H_{i,\ell}\in p^M\}.}
\tag{17}
$$
原 C 单位在 $j\ge1$ 时准确等价于 $C^\perp$ 单位，因为
$$
C V_j=C^\perp-\alpha\tau D_*.
$$
全部第一参数及其剩余深度都保留。
原 (14) 被 $\kappa^j$ 除后的参数就是 $H_{i,\ell}/\kappa^M$。

原另外两参数的准确返回是
$$
\boxed{
E_{\rm test}=14C^\perp+\tau K_{i,\ell},\qquad
G_{\rm test}=G_\perp+g\tau K_{i,\ell}.}
\tag{18}
$$
例如
$\langle H_1,D_*\rangle/N(D_*)=-\alpha g$，
故 (18) 的两个 D 系数同为原 $14\alpha=406/143$；
没有遗漏 H1 随 D 核的移动。

定义原来源上的实际权
$$
\boxed{
Q_{i;M,\ell}(\tau)=
\frac{1_{\mathcal D_{i;M,\ell}}}{b\Omega^6}
\widehat P_p\bigl(H_{i,\ell}/\kappa^M,\
            14C^\perp+\tau K_{i,\ell},\
            G_\perp+g\tau K_{i,\ell}\bigr).}
\tag{19}
$$
$\widehat P_p$ 的全部原系数、$u_j$ 和右逆均不变。
这是同一来源的真实返回，不是新增或更换 $q_N$。

对固定 $M,\ell$，(19) 的域与 $\tau$ 无关，且准确为
$$
Q_{i;M,\ell}(\tau)=\sum_{a=0}^6\tau^a Q_{i,a;M,\ell},
$$
$$
\boxed{
Q_{i,a;M,\ell}=
\frac{1_{\mathcal D_{i;M,\ell}}K_{i,\ell}^a}{a!\,b\Omega^6}
(\partial_E+g\partial_G)^a\widehat P_p
       (H_{i,\ell}/\kappa^M,14C^\perp,G_\perp).}
\tag{20}
$$
所有这些完整测试都整有界；$a!\in\mathcal O^\times$。
其门和多项式均与 $Y_i$ 的正交缩放逐点相容。
这不等于断言其条件第一来源就是 S。

## 5. 同一浅层上真正 S/T 单位 cut 及全部 log 质量

定义原有限层积分，保 R664 同一归一：
$$
\mathcal L_{i;N,n,j}^{Z}(u)=
\int_{\Gamma_0,\ \mathcal E\in p^j\mathbf Z_p^\times}
q_i\,1_{\{Z_iP_{Y_i,(-\kappa)^n}^{-1}\ {\rm unit}\}}
\langle Z_iP_{Y_i,(-\kappa)^n}^{-1}\rangle^{d_pu}\,d\mu_0 ,
$$
其中 $Z_i=Y_i$ 或 $W_i$。
逆像只在各真实整像上使用。以下 $1\le j<N\le n$。

记
$$
s=(-1)^n,\quad
w_0=(-8-18\omega)/315,\quad w_1=(-4+6\omega)/315,
$$
$$
Z_{i,\ell}=w_i\mathcal E+
 \kappa^\ell(W_i-w_i\mathcal E-b_YY_i).
\tag{21}
$$
$Z_{i,\ell}\perp Y_i$。
完整观察返回准确为
$$
Y_i\longmapsto sY_i,\qquad
W_iP_{Y_i,(-\kappa)^n}^{-1}
 \longmapsto sb_YY_i+\tau Z_{i,\ell}.
\tag{22}
$$
因为 $\tau\in p\mathcal O$、$b_Y$ 为单位，
两个单位 cut **严格相同**，都是 $Y_i$ 单位。
这只用于这个已完整返回的正浅层，不用于第零层或原未移动 W。

在 $Y_i$ 单位上令
$$
R_{i,n,\ell}=\frac{sZ_{i,\ell}}{b_YY_i}\in\mathcal O.
$$
于是全 Mellin 行为
$$
\boxed{
\mathcal L_{i;N,n,j}^{S}(u)
=a_{n,j}\int Q_{i;M,\ell}(\tau)\,
 1_{Y_i\ {\rm unit}}\langle Y_i\rangle^{d_pu}\,d\mu_0,}
$$
$$
\boxed{
\mathcal L_{i;N,n,j}^{T}(u)
=a_{n,j}\langle b_Y\rangle^{d_pu}
 \int Q_{i;M,\ell}(\tau)\,1_{Y_i\ {\rm unit}}
 \langle Y_i\rangle^{d_pu}(1+\tau R_{i,n,\ell})^{d_pu}\,d\mu_0.}
\tag{23}
$$
零阶质量因此相等，但它们一般不是零。

在 $u=0$ 微分并保该质量，得到
$$
\boxed{
\begin{aligned}
a_{n,j}^{-1}\bigg[
 \frac{(\mathcal L^T)'-(\mathcal L^S)'}{d_p}
 -\log\langle b_Y\rangle\,\mathcal L^S(0)
 \bigg]
=\int Q_{i;M,\ell}(\tau)\,1_{Y_i\ {\rm unit}}
                 \log(1+\tau R_{i,n,\ell})\,d\mu_0 .
\end{aligned}}
\tag{24}
$$
特别不能仅以 $(\mathcal L^T)'-(\mathcal L^S)'$ 替代右边。

将 (20) 代入，整个右边是
$$
\sum_{k\ge1}\tau^k \mathcal H_{i,k;M,\ell,s},
$$
$$
\boxed{
\mathcal H_{i,k;M,\ell,s}
=\sum_{0\le a\le\min(6,k-1)}
 \frac{(-1)^{k-a-1}}{k-a}
 \int Q_{i,a;M,\ell}\,1_{Y_i\ {\rm unit}}
               R_{i,n,\ell}^{\,k-a}\,d\mu_0 .}
\tag{25}
$$
这里 $s$ 保持实际奇偶性；所有负 Y 矩、固定 carry 和旧伴随都在。
整测度及整测试给
$$
v_p(\mathcal H_{i,k;M,\ell,s})\ge-\lfloor\log_p k\rfloor .
$$
因此级数统一收敛，并有真正同域的界
$$
\boxed{\text{(24) 右边}
=\kappa^j\mathcal H_{i,1;M,\ell,s}+p^{2j}\mathcal O.}
\tag{26}
$$
没有给这个固定第一负矩行猜非零或赋零。

## 6. 原 S 浅层的实际七阶递推

固定 $M\in4\mathbf Z_{\ge1}$、$\ell\ge M$、原 p。
令
$$
j=4r,\quad N=M+4r,\quad n=\ell+4r,\quad r\ge1.
$$
此时 $\widehat P_p$ 和 (17) 的门全部不随 r 变化，
$s=(-1)^\ell$ 也固定。记
$$
C_{i,a;M,\ell}(u)
=\int Q_{i,a;M,\ell}\,
       1_{Y_i\ {\rm unit}}\langle Y_i\rangle^{d_pu}\,d\mu_0 .
$$
由 (16)、(20)、(23)，原实际序列精确为
$$
\boxed{
\mathcal L_{i;M+4r,\ell+4r,4r}^{S}(u)
=\lambda^{2\ell}\sum_{a=0}^6
       C_{i,a;M,\ell}(u)
            (\lambda^{16}\kappa^{4a})^r.}
\tag{27}
$$
故对 r 的前移算子 $\mathsf T$，
$$
\boxed{
\prod_{a=0}^6(\mathsf T-\lambda^{16}\kappa^{4a})\,
 \mathcal L_{i;M+4r,\ell+4r,4r}^{S}(u)=0.}
\tag{28}
$$
这是原积分、同一个域返回和同一个固定多项式产生的真实递推，
不是从有限数值拟合而来，也没有认全中央零会逐项杀 (27)。
$T$ 行的准确差是 (25) 的完整级数，未把它截成七阶多项式。

(27) 同时适用于质量和中央导数。
不同特征根的 p 赋值为 $0,4,\ldots,24$；
这没有给逆 Vandermonde 的整性或任何免费原前缀收益。

## 7. 第零层、完整外部和原两个中央条件的位置

第零层不能代入 (19)。在那里原 C 单位与 $C^\perp$ 单位
一般不同，D_* 也没有被迫深；将 $\tau$ 形式上设为一不能弥补这个域差。
必须保原
$$
\mathcal L_{i;N,n,0}^{Z}
=\int_{\Gamma_0,\ \mathcal E\ {\rm unit}}\text{原同一个完整测试}\,d\mu_0 .
\tag{29}
$$
它位于原 A/Q/L/c/d 全单位的近相消域；
其 T 单位观察仍是 R664 的完整仿射 cut。

令 $\mathcal C_{i,n}^Z$ 为 R664 的共同 $\mathcal E$ 深 N 行，
$\mathcal O_{i,n}^Z$ 为原 $E_i\setminus\Gamma_0$ 全外部。
对 $n\ge N$，完整恒等就是
$$
\boxed{
\mathcal O_{i,n}^Z+\mathcal C_{i,n}^Z+
\mathcal L_{i;N,n,0}^Z+
\sum_{j=1}^{N-1}\mathcal L_{i;N,n,j}^Z
=(-1)^i\lambda^n\beta^N J_Z^*,
}
\tag{30}
$$
其中 $J_S^*=J_S,\ J_T^*=6\delta J_T$。
(5)、(6) 给 $\mathcal O$ 的完整物理词；
(19)–(28) 给每个正浅层的真实固定门返回；
第零层 (29) 和共同深域均保持。

若原两个中央导数同为零，只能对 (30) 的**整个**左侧赋零。
R665 的非零 $J_N I_{\Sigma,-1}$、R667 可见的自由差方向
均不得使 (29) 或 (5) 的外部自动为零。
所有式对原真实测试线性，所以同样适用于有完整 $\pi_4$ 零推前的差测试；
该总行恒零仍可以、并必须由这些真实补域补偿局部非零项。

本篇新增的是原浅补域的固定域、实际有限递推及同域 S/T log 比较；
未产生第三条算术中央零，也没有完成本课题的无穷素数结论。

## 固定证书与依赖

- [check-r668-double-s-shallow-annuli-and-exterior-words.js](../scripts/check-r668-double-s-shallow-annuli-and-exterior-words.js)
- [check-r668-double-s-shallow-annuli-and-exterior-words.json](../scripts/check-r668-double-s-shallow-annuli-and-exterior-words.json)

证书以 BigInt 有理 CM 算术支付四 Y 的全部三行行列式、
原六变量的环带同余、所有投影/四轴词系数、
D_*/C/H1 的完整移动和两种观察的全部返回系数。
所有深度和原积分递推由正文的一般证明支付，不用素数扫描。

主要来源：
[R664](R664-original-double-s-rotation-and-common-companion-gate.md) 的完整双 S 门；
[R665](R665-original-mixed-unit-deep-branch-and-negative-one-return.md) 的整个 $87D_*$ 核；
[R662](R662-original-annulus-exterior-and-exact-w-compensation.md) 的真实原 Y 外部与 T 观察；
[R594](R594-two-source-six-carry-compensation-and-unit-z-rectangle.md) 的原固定整右逆；
R653 的全五项 pair 来源。R594 的具体原多项式始终通过
R664/R665 已付的 $\widehat P_p$ 使用，未新增一套系数。
