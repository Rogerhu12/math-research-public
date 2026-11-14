# R567 — 原正负全域的共同首两行与同一五 sigma 来源的精确消元

日期：2026-11-14。**状态：已证明。**

本篇把 R564 的整个负条带与 R568 的整个正条带接成原同一个
native 残差，准确保留常数 log 项、一阶项及全部单位切集。
两项非原始来源各有一个原 sigma 输入可以精确积分掉；剩余的
五 sigma 测度是同一个实际来源，但两套投影、单位域和观察权仍不同。
第七 sigma 矩及七／十度 theta 的第六矩质量校正全部显示。

结果给出该完整残差的明确首层判据；没有证明该判据非零，
也没有从辅助来源的一条单位系数推出原中央非零。

## 1. 同一个原行及两套实际伴随

全部射线、有限坏集、周期及 R536 的原七行右逆沿用
[R560](R560-native-single-branch-and-seven-conditional-moments.md)、
[R564](R564-original-negative-strip-orthogonal-cores-and-complete-return.md)、
[R568](R568-original-positive-strip-full-cores-and-native-transport.md)。
记
$$
b=17,\quad \omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\quad\chi=\chi_{65}.
\tag{1}
$$
原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。保
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\quad
D=D_4+c+(2+3\omega)d_0,\quad N(D)=14,
$$
$$
u=\frac{\omega c+(1-\omega)d_0}{2},\quad
P=u-\omega^2D/7,\quad
Z_*=d_0+(1+3\omega)D/14-(8+3\omega)P/10,
$$
$$
V=(-\omega^2,-\omega,2,0,-2\omega,-2\omega),\quad
K_{42}=(-\omega^2,-\omega,2,0,-3+3\omega,3).
\tag{2}
$$
$N(P)=5/7$，$N(V)=14$；两套正交三轴分别为
$(D,P,Z_*)$ 与 $(D,V,K_{42})$。

置
$$
\mu_0=\mathcal P_C\rho_0,\quad
\eta_C=\mathcal P_C\eta,\quad
\mu_h=\eta_C+\mu_0/2,\quad
\mu_R=R_{1*}\mu_0=\mu_0+\eta_C .
\tag{3}
$$
最后一式是 R544/R568 的完整来源身份。
$R_1=I-2\bar u^{\,t}u$ 是原真实 $u$ 反射；它与纯 $C$ 旋转交换。
$\mathsf H$ 只操作末两输入，且
$\eta_C=\omega^2\mathsf H_*\mu_0$。

对任一原观察 $r$，令
$$
r^\pm=r-a_r^\pm A_\pm,\qquad A_+=P,\quad A_-=V,\qquad
a_r^\pm=\frac{\langle r,A_\pm\rangle}{N(A_\pm)}.
\tag{4}
$$
本篇 $A_\pm$ 只是法向轴记号，不是 R565 的 Cartier 系数。
原 $E,G,Y,W,W'$ 均与 $D$ 正交，故 $r^\pm$ 与相应的两个法向轴都正交。
需要的一阶系数为
$$
\begin{array}{c|cc}
r&a_r^+&a_r^-\\ \hline
E&14\omega/5&\omega\\
G&(28+70\omega)/5&2+5\omega\\
Y&7(3+\omega)/10&(12+11\omega)/14\\
W&7(11+\omega)/10&(8+19\omega)/14
\end{array}.
\tag{5}
$$

令 $\mathcal V_\pm=\{D,A_\pm\}^{\perp}$。
可以取任意同一整格的完整四维坐标表示它；以下全部原观察
$r^\pm$ 都是这同一个四维空间的真实线性式。
原固定域为
$$
\mathcal U_+=\{Z_*\text{ unit},E^+\text{ unit}\},\qquad
\mathcal U_-=\{K_{42}\text{ unit},E^-\text{ unit}\}.
\tag{6}
$$
若另外保 R566 的两个补域，则附加
$\bar H^\pm$ 单位或为深；它同样是 $\mathcal V_\pm$ 的实际事件。
不把这些不同域或不同观察互换。

## 2. 整个正负贡献的共同展开

记原六次多项式为 $\widehat P_p(T,E,G)$，其所有
$p,\lambda,\kappa$ 系数均保留。置
$$
\ell_\pm(t)=d\left\{
1_{Y^\pm\text{ unit}}\log\langle Y^\pm+t a_Y^\pm A_\pm\rangle
-1_{W^\pm\text{ unit}}\log\langle W^\pm+t a_W^\pm A_\pm\rangle
\right\}.
\tag{7}
$$
在 $t\in p\mathcal O$ 上，所有单位事件等于 $t=0$ 的事件，
包括 $E^\pm+t a_E^\pm A_\pm$；因此 (6) 是整个该盘上的准确域，
没有边界微分被省略。

定义完整解析函数
$$
F_+(t)=\int_{\mathcal U_+}
\widehat P_p(D,E^++t a_E^+P,G^++t a_G^+P)\,
\ell_+(t)\,d(\mu_0+2\eta_C),
$$
$$
F_-(t)=\int_{\mathcal U_-}
\widehat P_p(D,E^-+t a_E^-V,G^-+t a_G^-V)\,
\ell_-(t)\,d(\mu_0+\mu_R).
\tag{8}
$$
R568 的 $-2\chi\lambda\mu_h$ 与 R564 的
$\beta(2\mu_0+\eta_C)$ 给整个原行
$$
\boxed{
\mathcal N_n=\frac{\beta^{n+1}}{b\Omega^6}
\{\chi F_+(\kappa)+F_-(\kappa)\},\qquad n\ge1.
}
\tag{9}
$$
这含两条原条带的全部贡献；不是在另一个深子域上的恒等式。

把指示函数 (6) 纳入系数，定义两个关于 $T$ 的多项式
$$
\mathsf A_\pm(T)=
1_{\mathcal U_\pm}\widehat P_p(T,E^\pm,G^\pm)\ell_\pm(0),
\tag{10}
$$
$$
\begin{aligned}
\mathsf B_\pm(T)=1_{\mathcal U_\pm}\bigg[
&(a_E^\pm\partial_E\widehat P_p+
  a_G^\pm\partial_G\widehat P_p)(T,E^\pm,G^\pm)\ell_\pm(0)\\
&+d\,\widehat P_p(T,E^\pm,G^\pm)
\left\{\frac{1_{Y^\pm\text{ unit}}a_Y^\pm}{Y^\pm}
-\frac{1_{W^\pm\text{ unit}}a_W^\pm}{W^\pm}\right\}\bigg].
\end{aligned}
\tag{11}
$$
分母只在对应单位域使用，域外该项为零。
这两个多项式的 $T$ 次数至多六；所有系数都是相应
$\mathcal V_\pm$ 上的有界连续函数。
$\mathsf A_\pm$ 的系数在 $p\mathcal O$ 中，
$\mathsf B_\pm$ 的系数在 $\mathcal O$ 中。

准确的首两行是
$$
F_{+,0}=\int\mathsf A_+(D)\,d(\mu_0+2\eta_C),\qquad
F_{+,1}=\int P\mathsf B_+(D)\,d(\mu_0+2\eta_C),
$$
$$
F_{-,0}=\int\mathsf A_-(D)\,d(\mu_0+\mu_R),\qquad
F_{-,1}=\int V\mathsf B_-(D)\,d(\mu_0+\mu_R).
\tag{12}
$$
所有高项的系数满足 $v_p([t^j]F_\pm)\ge-\lfloor\log_pj\rfloor$。
由 $p\ge71$、$v_p(\kappa)=1$，得到
$$
F_\pm(\kappa)=F_{\pm,0}+\kappa F_{\pm,1}+p^2\mathcal O .
\tag{13}
$$
常数 log 项与一阶项同在可能的第一 $p$ 阶，尚未消去任何一项。

## 3. 一个原 sigma 输入的完整消元几何

令
$$
d\nu_5=-\frac1{84}\,d\bigl(\mathcal P_C
(\nu_\sigma^{\otimes4})\otimes\nu_\sigma\bigr)
\tag{14}
$$
于原五输入 $(\xi_1,\xi_2,\xi_3,x,d_0)$。
这里 $\mathcal P_C$ 仍只操作前四输入；没有新选一个辅助 theta 来源。
原 $\mu_0$ 准确是 $\nu_5\otimes\nu_\sigma(c)$，按实际坐标次序理解。
因此两个消元使用同一个 (14)。

### 3.1 正域：通过原 H 消去 c

对任一 $r\in\mathcal V_+$，有
$$
(r\mathsf H)_c=0.
\tag{15}
$$
原因是 $u=P+\omega^2D/7$，故 $r\perp u$，
而 $u\mathsf H=c$。定义
$$
T_{10}=D_4-2\omega d_0,\qquad N(T_{10})=10 .
$$
完整法向行准确为
$$
\boxed{
D\mathsf H=T_{10}+2\omega c,\qquad
P\mathsf H=-\frac{\omega^2}{7}T_{10}+\frac57c .
}
\tag{16}
$$
对相应伴随函数作原 $\mathsf H$ 的真实转置后，
它们全部不依赖 $c$。所有单位、对数及额外补域也如此。

### 3.2 负域：通过原 R1 消去 c

对任一 $r\in\mathcal V_-$，从 $r\perp D,V$ 得
$$
r_c=(\omega-1)r_{d_0},\qquad
(rR_1)_c=0,\qquad(rR_1)_{d_0}=-2r_{d_0}.
\tag{17}
$$
前四个系数不变。这里必须按完整 Hermitian 内积计算，
不能把共轭号省略。

置
$$
T_7=D_4-\omega d_0,\qquad N(T_7)=7,\qquad
a=3+2\omega,\qquad e=-1-3\omega=\omega^2a .
$$
准确有
$$
\boxed{
DR_1=T_7+ac,\qquad
VR_1=-\omega^2T_7+ec .
}
\tag{18}
$$
因为 $R_1$ 与 $\mathcal P_C$ 交换，(17)–(18) 对原完整投影来源成立，
不是只对未平均的一支成立。

(15)、(17) 还给两条真实未加权边际零：
$$
(\mathcal V_+)_*\eta_C=0,\qquad
(\mathcal V_-)_*\mu_R=0 .
\tag{19}
$$
有 $D$ 的多项式权时必须使用下一节；(19) 不允许删除 (12) 的常数 log 行。

## 4. 六次多项式和第七矩的准确公式

原 sigma 的低矩完整为
$$
m_\sigma(0)=0,\quad m_\sigma(1)=\Omega,\quad
m_\sigma(j)=0\ (2\le j\le6),\quad
\boxed{m_\sigma(7)=24b\Omega^7}.
\tag{20}
$$
这由 $\sigma(z)=z+bz^7/210+O(z^{13})$ 给出。

对任一上节类型的
$\mathsf A(T)=\sum_{k=0}^6\mathsf A_kT^k$，
用 $\widetilde{\mathsf A}_+$ 表示所有伴随系数经真实 $\mathsf H$
转置、删去已不存在的 $c$；用 $\widetilde{\mathsf A}_-$ 表示经真实
$R_1$ 的相同操作。两者的域和系数通常不同。
以下积分全在同一个 (14) 上；$T$ 分别取 $T_{10}$、$T_7$。

**正域精确公式：**
$$
\boxed{
\mathscr E_{+,0}[\mathsf A]:=\int\mathsf A(D)\,d\eta_C
=2\Omega\int\partial_T\widetilde{\mathsf A}_+(T_{10})\,d\nu_5 ,
}
\tag{21}
$$
$$
\boxed{
\begin{aligned}
\mathscr E_{+,1}[\mathsf A]
&:=\int P\mathsf A(D)\,d\eta_C\\
&=\frac{\omega^2\Omega}{7}
 \int\{5\widetilde{\mathsf A}_+
       -2T_{10}\partial_T\widetilde{\mathsf A}_+\}\,d\nu_5
+\frac{7680\omega^2b\Omega^7}{7}
 \int\widetilde{\mathsf A}_{+,6}\,d\nu_5 .
\end{aligned}}
\tag{22}
$$

**负域精确公式：**
$$
\boxed{
\mathscr E_{-,0}[\mathsf A]:=\int\mathsf A(D)\,d\mu_R
=a\Omega\int\partial_T\widetilde{\mathsf A}_-(T_7)\,d\nu_5 ,
}
\tag{23}
$$
$$
\boxed{
\begin{aligned}
\mathscr E_{-,1}[\mathsf A]
&:=\int V\mathsf A(D)\,d\mu_R\\
&=e\Omega\int\{\widetilde{\mathsf A}_-
       -T_7\partial_T\widetilde{\mathsf A}_-\}\,d\nu_5
+24be a^6\Omega^7\int\widetilde{\mathsf A}_{-,6}\,d\nu_5 .
\end{aligned}}
\tag{24}
$$

证明只需有限多项式展开，因此可与所有有界连续伴随测试交换。
例如在负域用 (18) 展开
$$
(-\omega^2T_7+ec)\,\widetilde{\mathsf A}_-(T_7+ac).
$$
一次 $c$ 项给 $e\Omega(\mathsf A-T_7\mathsf A')$；
唯一可能的七次项是 $e a^6\mathsf A_6c^7$，
恰给 (24) 的第二项。其他零至七次矩由 (20) 全部处理。
正域代入 (16)，并保来源系数 $\omega^2$，
得到 (21)–(22)，其中 $(2\omega)^6=64$。
这也证明两个显示的第七矩项不能遗漏。

## 5. 整个七／十度来源及实际质量校正

在 (14) 的完整五输入中，$T_7$、$T_{10}$ 各与相应转置后的
四个伴随正交。三个纯 $C$ 共轭的整数行中，
$T_7$ 的奇系数个数是 $3,5,5$，
$T_{10}$ 是 $2,4,4$。
所以它们分别属于整个 standard odd $\mathcal S_7$ 和
standard even $\mathcal S_{10}$，保全部四伴随。

可取完整基，按初始次数标号：
$$
\begin{array}{c|l}
\mathcal S_7&
F_0=-x_\wp^2y_\wp\sigma^7,\ 
F_1=x_\wp^3\sigma^7,\ 
F_2=-x_\wp y_\wp\sigma^7,\ 
F_3=x_\wp^2\sigma^7,\ 
F_4=-y_\wp\sigma^7,\ 
F_5=x_\wp\sigma^7,\ 
F_7=\sigma^7\\[2pt]
\mathcal S_{10}&
G_0=x_\wp^5\sigma^{10},\
G_1=-x_\wp^3y_\wp\sigma^{10},\
G_2=x_\wp^4\sigma^{10},\
G_3=-x_\wp^2y_\wp\sigma^{10},\
G_4=x_\wp^3\sigma^{10},\
G_5=-x_\wp y_\wp\sigma^{10},\
G_6=x_\wp^2\sigma^{10},\
G_7=-y_\wp\sigma^{10},\
G_8=x_\wp\sigma^{10},\
G_{10}=\sigma^{10}.
\end{array}
\tag{25}
$$
这里 $x_\wp,y_\wp$ 是椭圆函数，不是原自由输入 $x$。
所有基首系数为一；所需 Taylor 阶乘不超过 $10!$，在当前 $p\ge71$ 为单位。
于是各自整个联合具有有界整条件测度
$\Lambda^-_j$（$j=0,\ldots,5,7$）和
$\Lambda^+_j$（$j=0,\ldots,8,10$）。
它们是同一 $\nu_5$ 的两套实际不同投影，不是假设独立的系数。

$x_\wp=z^{-2}-bz^4/7+\cdots$、
$y_\wp=-z^{-3}-2bz^3/7+\cdots$ 给
$$
F_0=1+\frac b{30}z^6+\cdots,\qquad
G_0=1-\frac{2b}{3}z^6+\cdots .
$$
因此其条件矩准确为
$$
m^\pm_j=j!\Omega^j\Lambda^\pm_j\quad(0\le j\le5),
$$
$$
\boxed{
m^-_6=24b\Omega^6\Lambda^-_0,\qquad
m^+_6=\Omega^6(720\Lambda^+_6-480b\Lambda^+_0).
}
\tag{26}
$$
整个空间仍保留 (25) 的其他系数；只是在下列次数范围内不读它们。

例如 (24) 对应的完整条件行可写成
$$
\begin{aligned}
\mathscr E_{-,1}[\mathsf A]
={}&e\Omega\langle\widetilde{\mathsf A}_{-,0},\Lambda^-_0\rangle\\
&+e\sum_{k=2}^5(1-k)k!\Omega^{k+1}
 \langle\widetilde{\mathsf A}_{-,k},\Lambda^-_k\rangle\\
&+\boxed{24be(a^6-5)\Omega^7
 \langle\widetilde{\mathsf A}_{-,6},\Lambda^-_0\rangle}.
\end{aligned}
\tag{27}
$$
一次系数准确消失；第六系数的质量是第七 sigma 矩和
$T_7$ 第六矩两项合并的结果。

同样，正域是
$$
\begin{aligned}
\mathscr E_{+,1}[\mathsf A]
={}&\frac{\omega^2}{7}\sum_{k=0}^5(5-2k)k!\Omega^{k+1}
 \langle\widetilde{\mathsf A}_{+,k},\Lambda^+_k\rangle\\
&+\omega^2\Omega^7\left\{
-720\langle\widetilde{\mathsf A}_{+,6},\Lambda^+_6\rangle
+\frac{11040b}{7}
 \langle\widetilde{\mathsf A}_{+,6},\Lambda^+_0\rangle
\right\}.
\end{aligned}
\tag{28}
$$
常数行 (21)、(23) 分别读
$2\sum_{k=1}^6k!\Omega^k\Lambda^+_{k-1}$
和
$a\sum_{k=1}^6k!\Omega^k\Lambda^-_{k-1}$，
并逐项乘原真实系数。

这些质量系数并非被 $p$ 自动杀掉：
$$
a^6=-143-180\delta,\quad
N(a^6-5)=119104=2^6\cdot1861,\quad1861\equiv5\pmod{64}.
\tag{29}
$$
$1861$ 为素数，故原 $p\equiv7\bmod64$ 排除它；
(27) 的固定系数与 (28) 的 $11040b/7$ 在当前处均为单位。
这只说明这些条件行必须保留，不能据系数单位赋其积分单位。

## 6. 原 native 残差的准确首层判据

把全部辅助来源用上面已付公式代回 (12)，得到
$$
\begin{aligned}
F_{+,0}&=\int\mathsf A_+(D)\,d\mu_0
       +2\mathscr E_{+,0}[\mathsf A_+],\\
F_{+,1}&=\int P\mathsf B_+(D)\,d\mu_0
       +2\mathscr E_{+,1}[\mathsf B_+],\\
F_{-,0}&=\int\mathsf A_-(D)\,d\mu_0
       +\mathscr E_{-,0}[\mathsf A_-],\\
F_{-,1}&=\int V\mathsf B_-(D)\,d\mu_0
       +\mathscr E_{-,1}[\mathsf B_-].
\end{aligned}
\tag{30}
$$
右边只有原 $\mu_0$ 和同一个五 sigma 来源 (14)，所有投影已明确。
定义
$$
C_0=\chi F_{+,0}+F_{-,0}\in p\mathcal O,\qquad
C_1=\chi F_{+,1}+F_{-,1}\in\mathcal O .
$$
于是整个 native 残差准确满足
$$
\boxed{
\mathcal N_n=
\frac{\beta^{n+1}}{b\Omega^6}
(C_0+\kappa C_1)+p^2\mathcal O,\qquad
\frac{b\Omega^6}{p\beta^{n+1}}\mathcal N_n
\equiv\frac{C_0}{p}+\lambda^2C_1\pmod p .
}
\tag{31}
$$
外部所有因子都是单位。若 (31) 的右边非零，则该
$\mathcal N_n$ 对每个 $n\ge1$ 恰有赋值一。
**这仍只是 R556 (15) 的局部 native 残差，不能据此排除两条原中央同时失败。**
整个原算术总行还有下一节的两个完整补域。

**未付的正是该完整右端的非零。**
$C_0/p$ 含原单位域上的真实 log 信息，不能因 (19) 的未加权边际零
删去；(27)–(29) 的单位系数不能消除其补偿。
两个五变量投影虽来自同一个 (14)，也不能把原
$E/Y/W$ 混合条件或 R566 两超平面认成独立伴随。
本文没有把 R562 的四单位域 $J$ 或 R565 的 Cartier 双线性行
直接代入 (31)。主目标仍需在这些实际同源行之间完成进一步比较。

## 7. 必须保留的整个原算术总行

为固定范围，仍用 R556 的同一
$q=\mathfrak q_{n,p}$、$\ell$、$a=q\ell$、
$\Delta=\rho_0-\eta$ 及
$\mathcal B=\{u\in p,L\text{ unit}\}$。
本篇 (9)、(31) 计算的是
$$
\mathcal N_n=\int_{\mathcal B}(a-a\circ R_c)\,d\Delta
=2\lambda h(\Phi_1-\Phi_2).
\tag{32}
$$
真正已返回两条原中央的整个总行则是
$$
\mathcal T_n=\Delta(a-a\circ R_c)
=3\beta^n\{J'_S(0)-6\delta J'_T(0)\}.
\tag{33}
$$
因为 $\{u\in p,L\in p\}=\{c,d_0\in p\}$，
且该域在 $R_c$ 下稳定，R556 (9) 精确给
$$
\boxed{
\mathcal T_n=\mathcal N_n+\mathcal C_n,\qquad
\mathcal C_n=
\int_{\{u\text{ unit}\}}(a-a\circ R_c)\,d\Delta
+3\int_{\{c,d_0\in p\}}a\,d\rho_0 .
}
\tag{34}
$$
第二项仍按 R556 (17) 保完整 $q\circ S_\kappa$、所有 carry 和
$A$ 单位域的对数比；它没有因 sigma 总质量为零而消失。
原反证输入 $J'_S=J'_T=0$ 只给
$\mathcal C_n=-\mathcal N_n$，不会给两项分别为零。
因此 (31) 即使非零，也只迫补域以同阶非零值补偿；
终局仍须在同一个实际测试上控制 (34) 的完整右边。

本节修正本篇首发版本末节的一句过强推论：
那里曾把残差的非零当成整个算术总行非零的充分条件。
(7)–(31) 的解析、几何、来源和矩公式均未使用该推论，保持原样。
后续只按 (32)–(34) 的准确范围使用它们。

## 精确证书

- [check-r567-native-both-strips-normal-jets.js](../scripts/check-r567-native-both-strips-normal-jets.js)
- [check-r567-native-both-strips-normal-jets.json](../scripts/check-r567-native-both-strips-normal-jets.json)

脚本以 BigInt 的有理 CM 运算核定两套全部伴随的真实转置、
(16)–(18)、三个纯 C 共轭的完整半特征、七／十度的第六矩质量系数
及固定 (29)。连续测试、整个条带的返回及全尾界由 (7)–(24) 给出。
没有使用有限素数扫描、数值非零或独立审查作为发表门槛。
