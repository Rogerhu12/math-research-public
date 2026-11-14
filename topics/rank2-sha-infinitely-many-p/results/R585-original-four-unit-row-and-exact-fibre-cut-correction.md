# R585 — 原四单位算术行、完整 F 切集纠正与双 S2 反对称两支

日期：2026-11-14。**状态：已证明。**

本篇将 R582 的 native 条带和五线余域准确合成原四单位切集。
该合并本身只恢复原完整分区，不被当成新的中央零条件。
进一步利用同一个 $F$ whole 核和原 $q_n$ 的全部 $\pi_4$ 返回，
精确消去一个共同条件行，得到原有 carry 与未附 carry 的实际
四单位算术行之差。这个差只支撑八个明确的单位条件变化条带，
并保整个 $F$ 单位、carry 外余域。

原双 $S_2$ 来源还将同一个测试改写成两条严格不交的真实
degree14 支。两支只使用原反射和已付核心，所有 $Y/W$ 单位、
log 及 $\kappa^{-n}$ 逐项运输；最后给两个未附 carry 的原 sigma
深补项的完整简单极点级数，不另造单位见证。

## 1. 原规范与四单位集合

沿用
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R553](R553-original-norm2-two-theta-source-and-mixed-unit-domain.md)、
[R557](R557-third-source-common-carry-zero-mass-and-central-rows.md)、
[R576](R576-original-single-sigma-complements-and-three-line-domain.md)、
[R582](R582-original-normtwo-deep-complements-and-five-line-domain.md)
的原普通射线、全部固定坏集和同一个 $\Omega$。
记
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1.
\tag{1}
$$
原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d)$，
$\rho_0=-\nu_\sigma^{\otimes6}/84$、
$\mu_0=\mathcal P_C\rho_0$、
$\nu_4=-\mathcal P_C\nu_\sigma^{\otimes4}/84$。
所有 $D_4,C,H_1,A,F,E,G,Y,W$ 保 R576 (3) 的原行，特别
$$
a=2+3\omega,\quad l=1+3\omega,\quad g=3-2\omega,\quad
D=D_4+c+ad,\quad F=D+C,\quad E=D+14C,\quad G=13H_1+gF.
$$
原测试仍是
$$
q_n=\frac1{3b\Omega^6}\sum_j1_{\Gamma_{n,j}}
 \widehat P_p(D_j/\kappa^n,E_j,G),\qquad
\widehat P_p=\mathcal R_pP_p,
$$
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
 -1_{W\ {\rm unit}}\log\langle W\rangle\},\qquad a_n=q_n\ell .
\tag{2}
$$
$\widehat P_p$ 的全部原 $p,\lambda,\kappa$ 系数保持。

在原 Norm2 坐标
$$
U=c+\omega d,\quad V=c-\omega d,\qquad
u=-(U+\omega^2V)/2,\quad L=\omega U+\delta V
\tag{3}
$$
中，令
$$
\boxed{\mathscr A_4=\{c,d,U,V\ {\rm unit}\}
=\{U,V,U+V,U-V\ {\rm unit}\},\qquad A_4=1_{\mathscr A_4}.}
\tag{4}
$$
记 R582 的五线域为
$\mathscr V_5=\mathscr A_4\cap\{U+\omega^2V\ {\rm unit}\}$，
原 native 域为
$\mathscr B=\{u\in p,L\ {\rm unit}\}$。

在 $U+\omega^2V\in p$ 时，
$$
U\equiv-\omega^2V,\quad
c\equiv(2+\omega)V/2,\quad d\equiv V/2,\quad
L\equiv2\omega V\pmod p .
\tag{5}
$$
所有显示非零系数均为当前处单位，所以准确有
$$
\boxed{\mathscr B
=\mathscr A_4\cap\{U+\omega^2V\in p\},\qquad
\mathscr A_4=\mathscr B\sqcup\mathscr V_5 .}
\tag{6}
$$
这一步保原 $L$ 单位条件，不以只写 $u$ 深替代它。

原 $R_c$ 为 $(U,V)\mapsto(-V,-U)$，保持 $\mathscr A_4$。
其把 $\mathscr B$ 送到
$\mathscr A_4\cap\{U+\omega V\in p\}$，两支不交；
两者的共同补域是六条线
$U,V,U+V,U-V,U+\omega V,U+\omega^2V$ 都为单位。
这些是真实集合恒等式，未使用任何积分值。

置 $\Delta=\rho_0-\eta$，
$\Delta-R_{c,*}\Delta=3\rho_0$。
因此 R582 的两个完整部分准确合成
$$
\boxed{
\mathcal N_n+U_n^{(5)}
=\int_{\mathscr A_4}(a_n-a_n\circ R_c)\,d\Delta
=3\int_{\mathscr A_4}q_n\ell\,d\mu_0 .
}
\tag{7}
$$
最后一步也用了 pure $C$ 投影固定全部原测试和 (4)。
(7) 只是把原总行恢复到同一个四单位切集，不能单独据此宣布
原中央或该切集积分为零。

## 2. 同一个 F 核与四个实际投影单位条件

### 2.1 完整 F 方向和原四观察

原四观察为 $\pi_4=(Y,W,W',G)$，这里
$$
W'=(4+4\omega)\xi_1+(2+4\omega)\xi_2
 +(4+4\omega)\xi_3+(4+2\omega)c+4d
$$
是 R536 的原 $W'$，不是下面的 $d$ 反射输出。
有
$$
N(C)=1,\quad N(F)=13,\quad C\perp F,\qquad
C,F\perp Y,W,W',G .
\tag{8}
$$
完整框架 $(C,F,Y,W,W',G)$ 的行列式为
$$
3744-14976\omega,\qquad
N\det=294368256=2^{10}3^5\,7\,13^2.
\tag{9}
$$
$(\delta C,3F,Y,W,W',3G)$ 是完整整数框架。
$3F$ 属于 standard odd117，当前
$g_\pi\equiv1\bmod234$。
真实非零锚 $\sigma(3(4+\omega)z)$ 具有相同奇半特征，
其普通核心为 $\beta$。于是 whole $F$ 核在原联合上准确为
$$
\boxed{\mu_0|_{\{F\in p\}}=\beta(P_{F,\kappa})_*\mu_0,\qquad
P_{F,t}=I+(t-1)\bar F^{\,t}F/13.}
\tag{10}
$$
它固定全部 $\pi_4$ 和 $C$，因而固定 $\ell$。
同一 whole 身份及 R557 给原投影 $\eta,h$ 的对应式；
以下先对 $\mu_0$ 写出真实算术比较。

原 $q_n$ 的完整性质是
$$
\boxed{(\pi_4)_*(q_n\mu_0)=\beta^n(\pi_4)_*\mu_0,\qquad
\operatorname{supp}q_n\subset\{F\ {\rm unit}\}.}
\tag{11}
$$
这允许任意连续 $\pi_4$ 测试，不只单条中央。

### 2.2 真正的 F=0 投影

令 $P_{F,0}=I-\bar F^{\,t}F/13$，定义
$$
\boxed{
\begin{aligned}
c_0&=c-F/13,&d_0&=d+lF/13,\\
U_0&=U-2(2+\omega)F/13,&
V_0&=V-2\omega^2F/13 .
\end{aligned}}
\tag{12}
$$
这里 $d_0$ 只是本节 $d$ 的 $F=0$ 投影，不是旧第六输入的另一个名字。
它们分别为 $c,d,U,V$ 乘原完整 $P_{F,0}$，
均正交于 $C,F$，故都是 $\pi_4$ 的真实线性式。
全部十六个 $\mathbf Q(\omega)$ 系数在证书中；
其分母只含当前已排除的 $2,3,7,13$。

置
$$
A_0=1_{\{c_0,d_0,U_0,V_0\ {\rm unit}\}} .
\tag{13}
$$
由于 (12) 在当前处整且 $\kappa\in p\mathcal O$，
$$
\boxed{A_4\circ P_{F,\kappa}=A_0,\qquad
A_0\circ P_{F,t}=A_0\quad(t\in\mathcal O).}
\tag{14}
$$
这里是整个单位指示函数的准确身份，不是只对一个 Taylor 系数。

## 3. 完整共同项消去及八个实际条带

定义两个仍属同一原来源的完整积分
$$
Q_{A,n}=\mu_0(A_4q_n\ell),\qquad J_A=\mu_0(A_4\ell).
$$
$J_A$ 是原四单位切集上的算术行，并不被赋为 $J'_S-6\delta J'_T$。

**定理1（原 F 切集的准确纠正）。**
$$
\boxed{
Q_{A,n}-\beta^nJ_A
=\int_{\{F\ {\rm unit}\}}
(q_n-\beta^n)(A_4-A_0)\ell\,d\mu_0 .
}
\tag{15}
$$
记右边为 $\mathcal E_{F,n}$。

**证明。** 设 $B_0=\mu_0(A_0\ell)$。
由 (10)、(14) 及 $\ell$ 在 $F$ 方向不动，
$$
J_A=\mu_0(1_{F\ {\rm unit}}A_4\ell)+\beta B_0.
$$
因为 $A_0\ell$ 是完整 $\pi_4$ 测试，
$$
\mu_0(1_{F\ {\rm unit}}A_0\ell)=(1-\beta)B_0,\qquad
\mu_0(q_nA_0\ell)=\beta^nB_0.
$$
于是两条准确式分别为
$$
J_A=B_0+\mu_0(1_{F\ {\rm unit}}(A_4-A_0)\ell),
$$
$$
Q_{A,n}=\beta^nB_0+
\mu_0(1_{F\ {\rm unit}}q_n(A_4-A_0)\ell).
$$
相减完全消去 $B_0$，得到 (15)。证毕。

这不是把 $B_0$ 赋零。实际 source、所有 Mellin cut 和原 log
保持，消去是两个完整等式中同一个条件项的相减。
同一个证明适用于 R557 支付了 (10)–(11) 的原两态和其线性组合，
但各来源的中央仍保持原值，不增加任何零假设。

令四行依次为 $r_i=(c,d,U,V)$、$r_{i,0}=(c_0,d_0,U_0,V_0)$。
写
$$
r_{i,0}=r_i-\theta_iF,\qquad
(\theta_i)=\frac1{13}(1,-l,2(2+\omega),2\omega^2).
\tag{16}
$$
全部 $\theta_i$ 为当前处单位。
在 $F$ 单位域，$r_i,r_{i,0}$ 不可能同时深。
正负变化域可按第一次失败分成八个互不相交的完整条带：
$$
\begin{aligned}
\mathscr P_i={}&\{F\ {\rm unit},\ r_1,\ldots,r_4\ {\rm unit},\
r_{j,0}\ {\rm unit}\ (j<i),\ r_{i,0}\in p\},\\
\mathscr M_i={}&\{F\ {\rm unit},\ r_{1,0},\ldots,r_{4,0}\ {\rm unit},\
r_j\ {\rm unit}\ (j<i),\ r_i\in p\}.
\end{aligned}
\tag{17}
$$
于是
$$
\boxed{
\mathcal E_{F,n}
=\sum_{i=1}^4\int_{\mathscr P_i}(q_n-\beta^n)\ell\,d\mu_0
-\sum_{i=1}^4\int_{\mathscr M_i}(q_n-\beta^n)\ell\,d\mu_0 .
}
\tag{18}
$$
域中没有遗漏 $j>i$ 的条件：正域始终要求全部 $r_j$ 单位，
负域始终要求全部 $r_{j,0}$ 单位；另一套条件仅在第一次失败之前要求。

在原 carry $\Gamma_{n,j}$ 内，$F-\zeta_jC\in p^n$、$n\ge1$，
所以每个 $r_{i,0}$ 单位或深的条件准确转成
$r_i-\theta_i\zeta_jC$ 的同一条件。完整 $D_j/\kappa^n$ 不改变。
在 $\{F\ {\rm unit}\}\setminus\Gamma_n^{(3)}$ 上，
$q_n=0$，(15) 仍保非零权 $-\beta^n(A_4-A_0)\ell$。
因此不能只保八条带与 carry 的交域而删掉其余部分。

由 R582 的全部补项，(7)、(15) 给原总行的准确式
$$
\boxed{
\begin{aligned}
J'_S-6\delta J'_T
={}&J_A+\beta^{-n}\mathcal E_{F,n}\\
&+\beta^{-n}\{C_{c;n,1}+C_{d;n,1}
+C_{U;n,1}+C_{V;n,1}-3I_{n,1}\}.
\end{aligned}}
\tag{19}
$$
所有右边来源均已在原同一全空间上定义。
$q_n$ 的正矩归一、原两个单位 log、native 部分和 carry 外域
都在 (19) 内；没有把局部非零等同于左边非零。
$\beta^{-n}\mathcal E_{F,n}$ 对所有 $n\ge1$ 准确相同，
由 R582 的 $Q_{A,n}/\beta^n$ 与固定 $J_A$ 即得。

## 4. 同一个实际测试的双 S2 反对称两支

### 4.1 真正的交换与完整 carry 转置

在原 Norm2 坐标中，
$$
\mu_0=\omega\,\nu_4\otimes
(\nu_\Sigma(U)\otimes\nu_\Theta(V)
-\nu_\Theta(U)\otimes\nu_\Sigma(V)).
$$
令
$$
\Xi=\nu_4\otimes\nu_\Sigma(U)\otimes\nu_\Theta(V),
\qquad \mathsf S:(U,V)\mapsto(V,U).
$$
$\mathsf S$ 是原 $d$ 符号反射，固定前四输入和 $c$。
它保持 $\mathscr A_4$。故对同一个完整测试，
$$
\boxed{Q_{A,n}
=\omega\int_{\mathscr A_4}
\{a_n-a_n\circ\mathsf S\}\,d\Xi .}
\tag{20}
$$
这里没有把其余四输入换成质量，也没有将 $a_n$ 改成
只依赖 $U,V$ 的测试。

$\Xi$ 在 pure $C$ 下不变，$\mathsf S$ 与该旋转交换。
所以 (20) 两项可以各自准确约到同一第零 carry。
设
$$
f_n=\frac{1_{\{D\in p^n,C\ {\rm unit}\}}}{b\Omega^6}
 \widehat P_p(D/\kappa^n,E,G)\ell .
$$
则
$$
\boxed{Q_{A,n}
=\omega\int_{\mathscr A_4}\{f_n-f_n\circ\mathsf S\}\,d\Xi .}
\tag{21}
$$
三项平均变成一项，是来源和完整域的不变性；
没有把原 $1/3$ 留在一个已经平均完的单支外。

反射后的全部行是
$$
\boxed{
\begin{aligned}
D^-&=D\circ\mathsf S=D_4+c-ad,\\
F^-&=F-2ad,\quad E^-=E-2ad,\quad G^-=G-2gad,\\
Y^-&=Y-4d,\qquad W^-=W-8d,\qquad C^-=C .
\end{aligned}}
\tag{22}
$$
第二项的两个单位 Mellin 条件必须使用 $Y^-,W^-$。
特别 $D-D^-=2ad$ 在 $\mathscr A_4$ 上为单位，所以
$$
\boxed{
\mathscr A_4\cap\{D\in p^n,C\ {\rm unit}\},\quad
\mathscr A_4\cap\{D^-\in p^n,C\ {\rm unit}\}
}
\tag{23}
$$
严格不交。这是同一个 $j=0$ 的真实结论；
没有据此声称未经 pure $C$ 平均的所有异支交域也为空。

### 4.2 已有两条 degree14 核保整个纯张量

两行 $D,D^-$ 正交，范数都为 $14$。
$D^-$ 正是 R576 的 $R_{14}'$，未增加新的高 degree 轴。
R557 的 $D$ whole 核为 $\beta$ 于原 $\mu_0,\mathcal P_C\eta$。
原 $\mathsf S$ 在这两态上满足
$\rho_0\mapsto-\rho_0$、$\eta\mapsto\rho_0+\eta$，
且与 $\mathcal P_C$ 交换。
故用实际反射共轭得到 $D^-$ 的同一完整核心。

两纯张量 $\nu_4\otimes\Sigma\otimes\Theta$、
$\nu_4\otimes\Theta\otimes\Sigma$
是原两态的整线性组合，系数矩阵行列式为 $1-\omega$，
在当前处为单位。因此两轴在 $\Xi$ 和 $\mathsf S_*\Xi$ 上均有
真实 scalar $\beta$，且二轴正交、全部共同伴随保留。
这没有给 $\Xi$ 增添算术中央零。

用 R576 d 侧原共同四伴随 $(E_d,G_d,Y_d,W_d)$，
再记 $T_d=D_4+c$、$X_0=c-T_d/7$。
全部准确回代为
$$
\boxed{
\begin{aligned}
c&=X_0+(D+D^-)/14,&d&=(D-D^-)/(2a),\\
U&=X_0+(2+\omega)D/7+\omega^2D^-/7,&
V&=X_0+\omega^2D/7+(2+\omega)D^-/7,\\
E&=E_d-D^-,&G&=G_d-gD^-,\\
Y&=Y_d-2D^-/a,&W&=W_d-4D^-/a .
\end{aligned}}
\tag{24}
$$
特别
$$
X_0=\frac{a}{14}(Y_d-W_d)
$$
是四伴随的真实线性式，不是新增的独立变量。
完整框架 $(D,D^-,E_d,G_d,Y_d,W_d)$ 的行列式为
$-86632-15288\omega$，范数为 $2^6\,7^4\,13^3\,19$。

定义一个完整、与 $n$ 无关的测试
$$
\begin{aligned}
\mathscr F(X,T;\mathbf z)
={}&1_{\{T,\ X_0+T/14,\ X_0+\omega^2T/7,\
X_0+(2+\omega)T/7,\ E_d-T\ {\rm unit}\}}\\
&\cdot\widehat P_p(X,E_d-T,G_d-gT)\\
&\cdot d_p\{
1_{Y_d-2T/a\ {\rm unit}}\log\langle Y_d-2T/a\rangle
-1_{W_d-4T/a\ {\rm unit}}\log\langle W_d-4T/a\rangle\},
\end{aligned}
\tag{25}
$$
其中 $\mathbf z=(E_d,G_d,Y_d,W_d)$，$X_0$ 按 (24) 使用。
原 $D$ 深归一后，$\mathscr A_4$ 与 $C$ 单位准确变成 (25)
第一行；反射支同理交换 $D,D^-$。
实际兩核心因而给
$$
\boxed{
Q_{A,n}=\frac{\omega\beta^n}{b\Omega^6}
\int\{\mathscr F(D,D^-;\mathbf z)
-\mathscr F(D^-,D;\mathbf z)\}\,d\Xi .
}
\tag{26}
$$
这是 (21) 在同一完整框架中的真正归一，不删除另一轴的单位条件。
两个完整第一自由轴各只出现于原六次 $\widehat P_p$，
所以可按原 entire $S_{14}$ 的七个条件矩逐项收缩。
第六矩必须保
$\Omega^6(720\Lambda_6-672b\Lambda_0)$；
其余 $0,\ldots,5$ 次矩为相应 $k!\Omega^k\Lambda_k$。
所有条件系数仍带 (25) 的另一个 degree14 轴及四伴随，
不能由质量或角型单独删掉其中一条完整积分。

## 5. 未附 carry 的两个原 sigma 深项：准确简单极点级数

为将 (15) 的未加 carry 行与同一原完整算术权继续比较，定义
$$
C_c^\circ=\mu_0(1_{c\in p}\ell),\qquad
C_d^\circ=\mu_0(1_{d\in p}\ell).
$$
它们与 R576 的 $C_{c;n,1},C_{d;n,1}$ 不同；
这里没有 $q_n$ 或 $\kappa^{-n}$。

原 sigma 满足 $m_\sigma(0)=0$，非零矩只在 $1\bmod6$。
其实际 core 为 $\beta$。
在 $c$ 深支，$Y,W$ 的真实单位条件准确为
$A+2d$、$A+4d$ 各自为单位；
在 $d$ 深支则分别为 $A+c$、$A+3\delta c$。
所以所有常数 log 部分严格因原 sigma 零质量消失。

若 $k=6r+1$，设
$$
\begin{aligned}
R_{c,k}
&=\int\left\{
\frac{1_{A+2d\ {\rm unit}}}{(A+2d)^k}
-(3\delta)^k\frac{1_{A+4d\ {\rm unit}}}{(A+4d)^k}
\right\}\,d(\nu_4\otimes\nu_\sigma(d)),\\
R_{d,k}
&=\int\left\{
2^k\frac{1_{A+c\ {\rm unit}}}{(A+c)^k}
-4^k\frac{1_{A+3\delta c\ {\rm unit}}}{(A+3\delta c)^k}
\right\}\,d(\nu_4\otimes\nu_\sigma(c)).
\end{aligned}
\tag{27}
$$
这些都是原指定负幂所在的实际单位域，不将其代成正矩。
逐项完整 log 展开给
$$
\boxed{
C_\epsilon^\circ
=\beta d_p\sum_{r\ge0}
\frac{\kappa^{6r+1}m_\sigma(6r+1)}{6r+1}\,
R_{\epsilon,6r+1}
=\beta\kappa d_p\Omega R_{\epsilon,1}+p^7\mathcal O .
}
\tag{28}
$$
$k=1\bmod6$ 使 log 的交替号为正。
来源整有界，分母只有 $k$；在当前 $p\ge71$，
所有 $k\ge7$ 的项赋值至少七，故级数一致收敛且尾界成立。

因此 (28) 的固定简单极点行确实来自同一个原算术补项，
不是另选的单位测试。这里未赋 $R_{\epsilon,1}$ 非零。
若继续处理未附 carry 的 $U,V$ 深项，
必须保 R582 所强调的 $\Theta$ 质量一边界，不能套用 (28)
的 sigma 零质量论证。

## 6. 当前范围与精确证书

新增的实际关系为：
(15) 完整消去共同 $\pi_4$ 条件项；
(17)–(19) 保八个准确 cut 差、carry 外域及原全部算术总行；
(21)–(26) 在原双 $S_2$ 上支付两条不交的完整混合支，
用同一正交 degree14 框架保全部日志和单位条件；
(28) 则将两个未附 carry 的原补项准确接到固定简单极点行。

这些身份没有把 $J_A$、$\mathcal E_{F,n}$ 或 (26) 的任一支赋零，
也未把一个局部非零行认成原完整中央非零。
仍须在同一个实际权和全部余域上完成最后的消去或非消失。

- [check-r585-original-four-unit-row-and-exact-fibre-cut-correction.js](../scripts/check-r585-original-four-unit-row-and-exact-fibre-cut-correction.js)
- [check-r585-original-four-unit-row-and-exact-fibre-cut-correction.json](../scripts/check-r585-original-four-unit-row-and-exact-fibre-cut-correction.json)

精确证书保存完整 $F/\pi_4$ 框架、$F=0$ 投影的全部系数、
native 域的固定模 $p$ 代数、原反射的全部观察行及正交
$D,D^-$ 的共同四伴随框架。全部计算为 BigInt 有理 CM 算术。
全域分区、共同项相减、无穷 log 尾及算术量词由正文支付，
没有以有限素数采样替代。
