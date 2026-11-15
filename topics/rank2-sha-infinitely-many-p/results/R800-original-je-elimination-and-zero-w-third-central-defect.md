# R800 — 原 J/E 四格的同观察消元、零 W 缺陷与第三中央

日期：2026-11-15。**状态：以下完整来源、实际四格、原非零首矩及第三中央恒等式已证明。**

本文使用 R734 的同一个最终测试 $q=q_N^*$。R794 的 $E_{\mathcal V}$ 偶核固定整个
$(Y,W,J)$，因而 R793(37)—(38) 的交域项可直接消去。对原 W Mellin，四格不是四条
独立行，而是一个明确的外积；所有深度、局部质量和第四块的真实位置均保留。

进一步，在同一原来源上定义
$(1_{E\in p^N}-\lambda^N)qB_i$。两个态的 W 边际整条为零，
第一态的 Y 边际也整条为零，但其完整 $Z/Y$ 首矩是已证明非零的原 $D_\omega$ 点值。
第二态的完整 U 投影则准确为 $-49\lambda^{2N}[1/2]U/(3c_B)$。
这把额外的原第三中央定位在一个实际零 W 边际的来源中，而没有从零边际制造新的中央零。

## 1. 同一原源及真正固定的观察

保持原普通射线、全部固定坏集、R734 的相对密度一子族和 $p>163$。
令
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad
a=1+3\omega,\quad \alpha=17-3\omega,\quad
b_Y=\frac{20+3\omega}{17},
$$
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad
N\in4\mathbf Z_{>0},\quad u=\kappa^N,\quad
s_N=\lambda^N=\beta^N,\quad c_B=1-\omega^2.
\tag{1}
$$
这里 $s_N$ 是原实际代数数。以下不假定 $1-s_N$ 为 p-adic 单位，也不除以它。

沿 R777/R780，
$$
B_0=\frac{e_0-\omega h_W}{c_B},\qquad B_1=K_WB_0,
\qquad K_WB_1=B_0,\qquad \rho_i=qB_i .
\tag{2}
$$
原 C 六角平均、全部 quarter 标签及普通周期 $\Omega$ 统一保持。
原三维观察与隐藏行是
$$
P=b_YY+Z_0,\qquad W=P-at=b_YY+Z,\qquad Z=Z_0-at,
$$
$$
E=E_{\mathcal V}+e_JJ,\qquad
e_J=-1841/72,\qquad
E_{\mathcal V}=\frac{h_0}{144a}(119Z_0+144at),
\quad h_0=17+3\omega.
\tag{3}
$$
q 仅依真实的 $C,H_1,J$，它们全垂直于 $\mathcal V=\operatorname{span}(Y,P,t)$。
特别
$$
E_{\mathcal V}\perp Y,W,J,\qquad E\perp Y,W,
\tag{4}
$$
但 E 不是 $E_{\mathcal V}$。

记 $\mathcal J=\{J\in p^N\}$、$\mathcal E=\{E\in p^N\}$，补集均指整个浅补域。
R794(8)—(11) 给原完整三态的真实身份
$$
\rho_i|_{E_{\mathcal V}\in p^N}
=s_N(P_{E_{\mathcal V},u})_*\rho_i,
$$
$$
\boxed{
\int_{\mathcal J\cap\mathcal E}F(Y,W,J)\,d\rho_i
=s_N\int_{\mathcal J}F(Y,W,J)\,d\rho_i .}
\tag{5}
$$
其证明使用 $\mathcal J$ 内 $E$ 深等价于 $E_{\mathcal V}$ 深，
以及(4)逐点固定整个测试。它是联合来源身份，不由两个边际相同推得。
若 F 另依 P、t、U 失败或其它未固定的行，必须使用 R794(9)、(12)的全矩阵，
不能直接使用(5)。

## 2. R793 的真实四格与交域项消元

沿 R793 置
$$
z^\circ=Z_0-\frac4{17}W,\qquad
c=\frac{\alpha}{36},\qquad c_z=-\frac{17\alpha}{468},
$$
$$
R_z=Y-cW-c_z z^\circ .
\tag{6}
$$
$W,z^\circ,R_z$ 是原 $\mathcal V$ 的正交框架。
R793 已支付真实 degree2808 轴的全部 quarter 偶核及 $R_z$ 偶核。
对偶数 $L,r\ge N$，
$$
M=M_{L,r}=P_{z^\circ,\kappa^L}P_{R_z,\kappa^r},\qquad
\mathcal R_{L,r}=\{z^\circ\in p^L,\ R_z\in p^r\},
$$
$$
\rho_i|_{\mathcal R_{L,r}}=\lambda^{L+r}M_*\rho_i .
\tag{7}
$$
W、J、q 固定；物理 E 在这个返回中为
$$
E\circ M=e_R\kappa^rR_z+e_z\kappa^Lz^\circ+e_JJ,
$$
$$
e_R=h_0b_Y/a,\qquad e_z=-289(25+48\omega)/1872.
\tag{8}
$$
所以物理 E 深/浅返回成 J 深/浅。另一门为
$$
E^{[-]}=E\circ M^{-1}
=e_R\kappa^{-r}R_z+e_z\kappa^{-L}z^\circ+e_JJ .
\tag{9}
$$
它只在(7)的整像上使用，不能与物理 E 相认。

令
$$
\mathcal A_{\epsilon,\eta}
=\mathcal R_{L,r}\cap \mathcal E^\epsilon
                  \cap\{E^{[-]}\in p^N\}^{\eta},
\qquad \epsilon,\eta\in\{+,-\}.
\tag{10}
$$
原 inverse-Y 为
$$
Y^{[-]}=Y\circ M^{-1}
=\kappa^{-r}R_z+c_z\kappa^{-L}z^\circ+cW.
\tag{11}
$$
对任意相同的两变量有界测试 F，(7)给
$$
\int_{\mathcal A_{\epsilon,\eta}}F(Y^{[-]},W)\,d\rho_i
=\lambda^{L+r}\int_{\mathcal J^\epsilon,\mathcal E^\eta}
                         F(Y,W)\,d\rho_i .
\tag{12}
$$

记
$$
\mathsf A_i(F)=\int F(Y,W)\,d\rho_i,\quad
\mathsf J_i(F)=\int_{\mathcal J}F(Y,W)\,d\rho_i,\quad
\mathsf E_i(F)=\int_{\mathcal E}F(Y,W)\,d\rho_i .
$$
由(5)，(12)的完整归一四格为
$$
\boxed{
\begin{pmatrix}
s_N\mathsf J_i&(1-s_N)\mathsf J_i\\
\mathsf E_i-s_N\mathsf J_i&
\mathsf A_i-\mathsf E_i-(1-s_N)\mathsf J_i
\end{pmatrix}.}
\tag{13}
$$
这已经消去 R793 唯一的交域项。尤其取
$f_w(x)=1_{x\ {\rm unit}}\langle x\rangle^{d_pw}$、$d_p=p-1$，
并定义
$$
F_i^+(w)=\mathsf J_i(f_w(W)),\qquad
T_B(w)=\frac{6\delta}{c_B}J_T(w),
$$
原完整 W 来源给
$$
\mathsf A_i(f_w(W))=s_NT_B(w),\qquad
\mathsf E_i(f_w(W))=s_N^2T_B(w).
$$
所以实际 W 四格准确为
$$
\boxed{
\bigl(A_{\epsilon,\eta}^{\,i}(w)\bigr)
=\lambda^{L+r}
\begin{pmatrix}
F_i^+(w)\\ s_NT_B(w)-F_i^+(w)
\end{pmatrix}
\begin{pmatrix}s_N&1-s_N\end{pmatrix}.}
\tag{14}
$$
这是整个 Mellin 函数的外积分解，包括 $w=0$ 的全部局部质量。
不需要 $J_T'(0)=0$。若施加该原中央零，导数表仅将第二行改成第一行的负数；
不会得到两个独立的交域零。

特别 R793 的 $X_i(w)$ 已准确确定为
$$
\boxed{X_i(w)=s_NF_i^+(w).}
\tag{15}
$$
其原有限 $\widetilde\Phi_N(u)$ 呈示仍合法，但不再是未消掉的交域未知量。

## 3. 整个深矩形避开原帽，第三和第四块的真实位置

原帽为
$$
\mathcal H_{N,n}
=\{Y\ {\rm unit},\ J,Z_0\in p^N,\
                        U=u_JJ+u_ZZ_0\notin p^n\}.
\tag{16}
$$
在 $\mathcal R_{L,r}$ 上，
$$
Y=R_z+c_z z^\circ+cW,\qquad Z_0=z^\circ+4W/17.
$$
若 W 为单位，则 Y、Z0 都为单位；若 W 非单位，则 Y 非单位。
因此有比 R793(35)更完整的集合结论
$$
\boxed{\mathcal R_{L,r}\cap\mathcal H_{N,n}=\varnothing .}
\tag{17}
$$
这里未删除 U 失败门；(17)在到达该门之前已由原 Y/Z0 条件强制。

因此对任意整数 $j\ge1$，
$$
\mathcal R_{L,r}\cap\mathcal E^c\cap\{W\notin p^j\}
$$
真正位于 R789 的第四块，而
$$
\mathcal R_{L,r}\cap\mathcal E^c\cap\{W\in p^j\}
$$
位于其同来源的 W 深补块。不能把后者因物理 Y 深而删掉：
本文使用(11)的 inverse-Y，它在该域上仍可能为单位。
(17)不声称这两个子域覆盖原整个第三、第四块。

## 4. 同一个原来源上的零 W 缺陷

定义实际有界有限门来源
$$
\boxed{\Psi_i=(1_{\mathcal E}-s_N)\rho_i,\qquad i=0,1.}
\tag{18}
$$
它不是由指定边际重新选出的测度。其权完整保原 E 深 N、同一个 q、
所有真实参数和全部六输入。

原 E 表及总 W 表立即给
$$
\boxed{W_*\Psi_0=W_*\Psi_1=0.}
\tag{19}
$$
原 B0 的总 Y 来源和 E 深 Y 来源都整条为零，所以
$$
\boxed{Y_*\Psi_0=0.}
\tag{20}
$$
对任意同一 F(Y,W)，将(13)改写成
$$
\boxed{
\begin{pmatrix}\mathsf J_i\\\mathsf A_i-\mathsf J_i\end{pmatrix}
\begin{pmatrix}s_N&1-s_N\end{pmatrix}
+
\begin{pmatrix}0&0\\\Psi_i(F)&-\Psi_i(F)\end{pmatrix}.}
\tag{21}
$$
这里 $\Psi_i(F)=\int F(Y,W)\,d\Psi_i$。
因(5)，这个联合缺陷在 J 深行上为零；它准确在 J 浅行出现。
对 F 仅依 W，(19)使第二个矩阵完全消失，回到(14)。
对一般 F(Y,W)，不能从零 W 边际删除它。

同样，令 $\mathcal R^-=\mathcal R_{L,r}\cap\mathcal E^c$。
(12)、(5)给完整同域公式
$$
\boxed{
\int_{\mathcal R^-}
 F(Y^{[-]},W)(1_{E^{[-]}\in p^N}-s_N)\,d\rho_i
=\lambda^{L+r}\int F(Y,W)\,d\Psi_i .}
\tag{22}
$$
物理 E 深行的相应积分为零。这个“零”只对所示整个
$(Y^{[-]},W)$ 观察成立，不是将物理 E 深来源本身置零。

## 5. 第二态的原全 Y 来源和完整 U 投影

沿 R780，$\Xi$ 是未适配第二态的整个第一 $2Y$ 来源，保原参考和外谱。
原两个全式为
$$
Y_*\rho_1
=\frac{s_N}{c_B}\bigl([1/2]_*\nu_\Xi+\nu_S\bigr),
$$
$$
Y_*(1_{\mathcal E}\rho_1)
=\frac{s_N^2}{c_B}
 \left([1/2]_*\nu_U+\frac{\delta\omega^2}{2}\nu_S\right).
$$
因此
$$
\boxed{
Y_*\Psi_1
=\frac{s_N^2}{c_B}
 \left([1/2]_*(\nu_U-\nu_\Xi)+\frac{\omega^2}{2}\nu_S\right).
}
\tag{23}
$$
用了 $\delta\omega^2/2-1=\omega^2/2$；没有删除 $\Xi$ 的质量或其它谱。

特别，记 $\mathcal Z_i(w)=\int f_w(Y)\,d\Psi_i$，则
$$
\mathcal Z_0(w)=0,
$$
$$
\boxed{
\mathcal Z_1(w)=\frac{s_N^2}{c_B}
 \left[
 \langle2\rangle^{-d_pw}(J_U(w)-J_\Xi(w))
                    +\frac{\omega^2}{2}J_S(w)\right].
}
\tag{24}
$$
其导数必须保
$-d_p\log\langle2\rangle(J_U(0)-J_\Xi(0))$。
只有原 $J_U(0)=0$ 已付，不能由三原中央零删去 $J_\Xi(0)$。

现在使用 R483/R493/R695 的原完整第一 $2Y$ 投影 $\mathcal P_U$。
该投影的全六变量身份是
$$
\mathcal P_Ue_0=0,\qquad \mathcal P_Uh_W=0,\qquad
\mathcal P_UB_0=0 .
\tag{25}
$$
第一式来自 R483(25) 的完整 $N_7^9=-1$ 块；
第二式由 R493(17)、(25)、(27)—(28) 的
$h_W=\omega^2\mathcal T_*e_0$、
$Y\mathcal T=Y$、完整五伙伴输运及 canonical 中心交换得到。
这些不是只有 Y 边际的零。

q 和 E 都在 $Y^\perp$，故整个(18)权与 $\mathcal P_U$ 交换。
再用 R784(5)的两个实际投影来源，
$$
Y_*\mathcal P_U(1_{\mathcal E}\rho_1)
=\frac{s_N^2}{c_B}[1/2]_*\nu_U,\qquad
Y_*\mathcal P_U\rho_1
=\frac{52s_N}{3c_B}[1/2]_*\nu_U .
$$
因此
$$
\boxed{
\mathcal P_U\Psi_0=0\quad\hbox{作为全来源},\qquad
Y_*\mathcal P_U\Psi_1
=-\frac{49s_N^2}{3c_B}[1/2]_*\nu_U .
}
\tag{26}
$$
第二式明确是“完整投影之后”的 Y 推前，并没有把它提升成
U 与五伙伴的一个未经证明的简单张量。

完整 Mellin 行为
$$
\boxed{
\int f_w(Y)\,d\mathcal P_U\Psi_1
=-\frac{49s_N^2}{3c_B}
             \langle2\rangle^{-d_pw}J_U(w).
}
\tag{27}
$$
$49s_N^2/(3c_B)$ 在原好 p 上为单位。因为 $J_U(0)=0$，
(27)的中央导数零准确等价于原 $J_U'(0)=0$。
这是已有第三中央在来源(18)中的新精确定位，不新增一个零条件。

## 6. 零 Y/W 边际不消掉原非零混合首矩

R767(22)—(28)给同 q、同 B0 的完整第一来源
$$
\Omega^{-1}Y_*(t\rho_0)
=-\frac{22s_N}{21}\nu_{D_\omega}.
\tag{28}
$$
原 $\mathcal T$ 固定 Y、Z0、q，并有 $\mathcal T_*B_0=\omega^2B_0$。
因此
$$
Y_*(Z_0\rho_0)=0,\qquad
\Omega^{-1}Y_*(Z\rho_0)
=\frac{22a s_N}{21}\nu_{D_\omega}.
$$
R796(14)已付同一**物理 E 深门**的整个首源
$Y_*(Z1_{\mathcal E}\rho_0)=0$。
代入(18)准确得到
$$
\boxed{
\Omega^{-1}Y_*(Z\Psi_0)
=-\frac{22a s_N^2}{21}\nu_{D_\omega}.}
\tag{29}
$$
所以在原已识别的有限点空间中，
$$
\boxed{
\int_{Y\ {\rm unit}}\frac ZY\,d\Psi_0
=-\frac{22a s_N^2\Omega}{21}I_\omega\ne0 ,
}
\tag{30}
$$
其中 $I_\omega=\int_{Y\ {\rm unit}}Y^{-1}\,d\nu_{D_\omega}$，
其非零使用 R735 的原角色、周期与 rank-one 点。
没有投影一个无限对数级数，也没有以 R791 的另一对 J 深浅独立性替代本式。

这给一个完全位于原六变量池中的具体事实：
(19)、(20)的两个整条零边际，并不能决定同来源的(30)。
它不与这两个零边际冲突。

更精确地，对 $z\in p\mathcal O$ 定义
$$
\mathcal G_N(z,w)=\int f_w(b_YY+zZ)\,d\Psi_0 .
$$
unit cut 准确是 Y-unit；由(20)，
$\mathcal G_N(0,w)=0$、$\mathcal G_N(z,0)=0$。
完整中央展开为
$$
\begin{aligned}
\partial_w\mathcal G_N(z,0)
={}&-\frac{22d_pa s_N^2\Omega}{21b_Y}I_\omega z\\
&+d_p\sum_{k\ge2}\frac{(-1)^{k+1}z^k}{k b_Y^k}
       \int_{Y\ {\rm unit}}Z^kY^{-k}\,d\Psi_0 .
\end{aligned}
\tag{31}
$$
q 在原好子族上整有界，(18)亦整有界。
若 $z=\kappa^j$、$j\ge1$，尾部属于 $p^{2j}\mathcal O$；
这里使用 $kj-v_p(k)\ge2j$，$k\ge2$，而非删除 log 分母。
因此当 $j>v_p(I_\omega)$ 时，
$$
v_p(\partial_w\mathcal G_N(\kappa^j,0))
=j+v_p(I_\omega).
\tag{32}
$$

Z 偶核固定 E、q 和两个态，所以对偶 $j$，
$$
\Psi_i|_{Z\in p^j}
=\lambda^j(P_{Z,\kappa^j})_*\Psi_i.
$$
由(19)有同一原 W 观察的完整无条件补偿
$$
\boxed{
\int_{Z\in p^j}f_w(W)\,d\Psi_0
=\lambda^j\mathcal G_N(\kappa^j,w),\qquad
\int_{Z\notin p^j}f_w(W)\,d\Psi_0
=-\lambda^j\mathcal G_N(\kappa^j,w).
}
\tag{33}
$$
这个补偿不需要假定 $J'_T=0$。
它说明(30)可以给受限 W 行非零，却仍不能将(19)变成矛盾。

## 7. 逆 Y 行的 W 深补项完整返回

E、q、J 均被原 W 缩放固定，故(18)保原真实两态核：
$$
\boxed{
\Psi_i|_{W\in p^j}
=\lambda^j(P_{W,\kappa^j})_*\Psi_{i+j\bmod2},
\qquad j\ge0.
}
\tag{34}
$$
定义完整移动观察
$$
Y_j=Y\circ P_{W,\kappa^j}
=Y+\frac{\alpha}{36}(\kappa^j-1)W
=y^\circ+\frac{\alpha\kappa^j}{36}W,
\qquad y^\circ=Y-\alpha W/36,
$$
$$
\mathcal K_{i,j}(w)
=\int f_w(Y_j)\,d\Psi_{i+j\bmod2}.
\tag{35}
$$
对 $j\ge1$，Yj-unit 的确等价于 $y^\circ$-unit，
但完整权仍为
$$
\boxed{
f_w(Y_j)=1_{y^\circ\ {\rm unit}}
 \langle y^\circ\rangle^{d_pw}
 \left\langle1+\frac{\alpha\kappa^jW}{36y^\circ}\right\rangle^{d_pw}.
}
\tag{36}
$$
第二因子的全部 log 与局部质量不能省略。
(35)使用原有限 W 核，不将这个变化认作一个未证明的 fixed-Lp 恒等式。

现在对 R793 的真实矩形定义
$$
\begin{aligned}
\mathcal C_{i,j}^{\,\mathrm{out}}(w)
={}&\int_{\substack{\mathcal R_{L,r},\,E\notin p^N\\W\notin p^j}}
 f_w(Y^{[-]})(1_{E^{[-]}\in p^N}-s_N)\,d\rho_i,\\
\mathcal C_{i,j}^{\,\mathrm{deep}}(w)
={}&\int_{\substack{\mathcal R_{L,r},\,E\notin p^N\\W\in p^j}}
 f_w(Y^{[-]})(1_{E^{[-]}\in p^N}-s_N)\,d\rho_i .
\end{aligned}
\tag{37}
$$
按(17)，前者确属原第四块、后者是其同矩形 W 深补域。
(22)、(34)逐项给
$$
\boxed{
\begin{aligned}
\mathcal C_{i,j}^{\,\mathrm{deep}}(w)
 &=\lambda^{L+r+j}\mathcal K_{i,j}(w),\\
\mathcal C_{i,j}^{\,\mathrm{out}}(w)
 &=\lambda^{L+r}
        \bigl(\mathcal Z_i(w)-\lambda^j\mathcal K_{i,j}(w)\bigr).
\end{aligned}}
\tag{38}
$$
这把 R793(41)的补域继续还原为同一个有限来源和(36)的实际观察。
没有留下一个可以任意选值的“补项”。

对 $i=0$，$\mathcal Z_0=0$，两部分整条相反，完全不需三个原中央假设。
对 $i=1$，两部分之和是(24)的完整 $U-\Xi$ 行。
若将 U 投影用于该式，必须同步投影来源并运输(35)的 W cut；
不能让 $\mathcal P_U$ 穿过未改变的 W 深门，亦不能逐项删去 $\Xi$。
下一节使用已经支付的完整 CM 共轭词来做到这一点。

## 8. 零 W 来源的原第三中央及全部 CM 帽补域

采用 R784 的完整216分支，记分支参数为 $\xi$，与(1)的 $s_N$ 区分：
$$
\alpha_{j,k}=(4+\omega)^j(5+2\omega)^k,\qquad
\xi=\zeta\bar\alpha_{j,k}/\alpha_{j,k},
$$
$$
0\le j\le17,\quad k=0,1,\quad\zeta\in\mu_6,\qquad
a_\xi=\omega^{2j}(-\omega)^k/216 .
$$
保原 first-$2Y$ degree136 canonical 算子
$$
\sigma_{\xi,i}=\alpha^{-1}(D_\xi)_*
                  \nu_{\mathcal Q_\alpha B_i},
\qquad
\mathcal Q_\alpha=\sum_{\tau\in E[\alpha]}
                  \mathsf T^{136}_{\bar\alpha\tau,\,2Y}.
\tag{39}
$$
所有原 flat、中心及 $1/\alpha$ 不变。置
$$
\Psi_{\xi,i}=(1_{\mathcal E}-s_N)q\,\sigma_{\xi,i},\qquad
W_\xi=W\circ D_\xi^{-1},
$$
$$
M_{\xi,m}=D_\xi P_{W,\kappa^m}D_\xi^{-1},\qquad
Y_\xi^{[-m]}=Y\circ M_{\xi,m}^{-1}.
$$
R487/R695 的原13/19高射线已支付这里的全来源 W 相容性；
E、q 被 $D_\xi$ 和 $M_{\xi,m}$ 固定。
所以
$$
\boxed{
\sum_\xi a_\xi
 \int_{W_\xi\in p^m}f_w(Y_\xi^{[-m]})\,d\Psi_{\xi,0}
=
\begin{cases}
0,&m\ {\rm even},\\[1mm]
-\dfrac{49\lambda^{m+2N}}{3c_B}
        \langle2\rangle^{-d_pw}J_U(w),&m\ {\rm odd}.
\end{cases}}
\tag{40}
$$
(40)先作完整的实际域返回，再用(25)—(27)；没有从某个边际零
推断每条 canonical 平移来源为零。
原 $J_U(0)=0$ 只消整个右边的尺度质量项。

在 R784 的原帽 $\mathcal H_{N,n}\cap\{W_\xi\in p^m\}$ 上，
$m\ge1$ 时 E 为单位，因此
$$
\Psi_{\xi,0}|_{\mathcal H_{N,n},\,W_\xi\in p^m}
=-s_Nq\,\sigma_{\xi,0}|_{\mathcal H_{N,n},\,W_\xi\in p^m}.
\tag{41}
$$
若 $A_{\xi,m}(w)$ 是 R784(20)的完整帽行，定义
$$
\mathcal O_{\xi,m}^{\Psi}(w)
=\int_{\{W_\xi\in p^m\}\setminus\mathcal H_{N,n}}
          f_w(Y_\xi^{[-m]})\,d\Psi_{\xi,0}.
$$
则对奇 m，
$$
\boxed{
-s_N\sum_\xi a_\xi A_{\xi,m}(w)
+\sum_\xi a_\xi\mathcal O_{\xi,m}^{\Psi}(w)
=-\frac{49\lambda^{m+2N}}{3c_B}
            \langle2\rangle^{-d_pw}J_U(w).
}
\tag{42}
$$
$\xi=1$ 的帽行仍是原 W 近相消帽；其余215项仍在 R784 的真实四-unit位置，
且来源为各自 $\sigma_{\xi,0}$，并非都为裸 B0。
(42)的补域包含原 E 深及 E 浅部分，权在两部分分别为
$1-s_N$、$-s_N$；任何一部分都没有删除。

若原 $J_U'(0)=0$，(42)只给
$$
\sum_\xi a_\xi(\mathcal O_{\xi,m}^{\Psi})'(0)
=s_N\sum_\xi a_\xi A_{\xi,m}'(0).
\tag{43}
$$
它不是把非零帽行或第四块各自赋零。
拉回 $D_\xi$ 时每条仍有
$\alpha^{-1}\langle\xi\rangle^{d_pw}$，
所以每个实际局部质量仍乘
$d_p\log\langle\xi\rangle$；只在整个投影求和后才能使用右边的零质量。

本节没有宣称 R793 的新 $z^\circ$ 核与全部第一 Y 的 CM 分支交换。
它使用的是已付的 W 共轭词(39)—(40)，不偷换两套实际词域。

## 9. 本篇确定的实际未知量与独立性范围

R793 的交域项已由(15)完全消掉；同 W 四格的完整外积分解为(14)。
第三、第四块在原深矩形上的逆 Y 关系则准确是(38)。
原第三中央位于(26)—(27)的零 W 来源第二态，并由(40)—(42)
在原全部 CM 管中实现。

这些结论同时保留一个严格非零的实际混合值(30)。
它没有与原 $J_S'=J_T'=J_U'=0$ 冲突：
完整 W 边际为零的来源本身就能具有(30)，并由(33)无条件产生相反补偿。
因此同 W 四格的消元不能被重复计作一个新的点因子约束。

仍需支付的具体连接是：
(36)的移动 inverse-Y 行与原其它已识别中央之间的全来源关系，
或(42)完整外部的另一个同域算术控制。
(24)保原 $\Xi$，(38)保 W 深补域，(42)保216来源及全部质量；
本文没有将任何一项当作一个新假定零。

## 依赖及执行范围

- [R483](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)、
  [R493](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)、
  [R695](R695-original-cm-word-domains-and-a-z-carries.md)：完整 U 投影、保 Y 的 T 输运及实际 CM 共轭词。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：本文未改的最终 q。
- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)、
  [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：原 $D_\omega$ 非零值及同 q 的完整 t 首来源。
- [R780](R780-original-third-central-b-state-and-true-w-deep-return.md)、
  [R784](R784-third-central-shallow-hats-and-four-unit-cm-tubes.md)：原 S/T/U 规范、$\Xi$ 全谱、E 深浅与全部 CM 帽补域。
- [R786](R786-original-j-depth-three-output-and-native-e-exteriors.md)、
  [R789](R789-fixed-cm-hat-germs-and-nonzero-native-exterior-differences.md)：实际 J 来源、固定观察及四格。
- [R793](R793-original-w-orthogonal-hat-axis-and-fourth-cell-j-e-return.md)、
  [R794](R794-original-e-j-intersection-and-native-w-annuli.md)、
  [R796](R796-whole-halfperiod-and-physical-e-first-moment-cancellation.md)：两个真实 E 门、整个 J/E/Y/W 返回及 E 深 Z 首矩零。

本文只作已付全来源与显示域的代数推导，没有新增数值计算、辅助模数、
射线或可重算数据。主目标仍未完成。
