# R488：真实正割高度族的完整三函数 ruling 与同一个十三行规范

日期：2026-11-16。**完整纸面原式证明；没有执行符号程序、原根恢复、profile 求积、数值秩、人工检查或新的科学计算。**

本文接 [R486](R486-full-ruling-principal-square-and-obstruction-to-an-open-state-family.md) 的完整平方门，给出一个真正低维的实际状态族：
$$
k=0,\qquad \omega=\omega_0,\qquad
h=H\sec(s-s_*),\quad H>0.
$$
它不是把任意八维历史当作自由状态，也不使用三乘三矩阵的平方零替代原二次算子的复合。

新增结论分为四层。

1. 若 R486 的整个局部 principal 因子对所有二阶 profile jets 恒零，并同时要求原实际历史方程，那么上述正割族是全部局部解；其实际历史也被唯一确定。这个假设比某一母函数、某一相位或若干 signed 积分为零严格更强。
2. 在这条实际几何上，无论真实入历史是否满足上述 principal 归一，完整二阶、三阶场都对 $v=\tan(s-s_*)$ 仿射。因而完整第四 ruling 恰为
$$
\mathscr K_\theta(s)=
\frac{\mathfrak a_\theta+\mathfrak b_\theta v+
\mathfrak c_\theta v^2}{h}.
$$
这里保留全部原右锚、左尾、二三阶入值和规范平方；并非只列最高导数项。
3. 一条真实中心清理条件使 $\mathfrak b_\theta=0$。在单个 patch 上，其余两个完整目标可以由 R47 的原第三规范 Gram 右逆同时支付。若另一个保护芽已锁定同一个第三规范，则这两目标不再自由；本文将它们准确放回 R469 的同一十三行核，得到每个正割 patch 的三条显示线性兼容行。
4. 这条几何的一个原矩阵坐标严格单调，故任何正长度段都不能是 $M=0$ 返回块。它也不能在保持该状态方程时平滑接常 scalar collar。因此局部结论没有支付完整闭词的桥或全部其它段。

直接使用 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R47](R47-fourth-order-range-and-third-gauge.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md) 和 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 的同一原规范。

## 1. 一套坐标、实际历史及本稿的条件范围

物理区间仍是同一个 $x\in I=[\ell,r]$，右原函数始终从原 $r$ 起。令
$$
\gamma=h_s,\quad \upsilon=k_s,\quad
\omega_s=\frac{\upsilon}{2h},\quad
e=h(x+\omega)-k,\quad Q=1+e^2 .
\tag{1}
$$
原高度满足 $h>0$，活动窗口满足 $x+\omega>0$。实际八矩历史及算子为
$$
\mathsf m_s=M_{\rm raw},\qquad
\mathsf A_s=\Phi_{\mathsf m(s)}.
\tag{2}
$$
没有在子段入口重新置零 $\mathsf m$ 或第三历史。

固定原 profile 圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
\tag{3}
$$
原三个二阶矩条件、二三阶真实 range、同 collar、相位光滑和两个 seed 条件在使用它们时明确保留。几何上的仿射结论本身不要求不交包、相同母形或 R480 的额外观察；把它接入当前 R467/R469 的实际库时仍须保那些原条件。

把二、三阶完整物理场写为 $Z_\theta,W_\theta$，第一阶是 $Y_{\phi_\theta}$。完整第四 forcing 为
$$
H_{4,\theta}
=-\{(dZ_\theta)^2+\mathcal S(Y_{\phi_\theta},W_\theta)\},
\qquad
\mathcal S(Y,W)_{ab}=Y_a\cdot W_b+W_a\cdot Y_b .
\tag{4}
$$
本文研究的 ruling 是原物理横坐标 $u_{\rm ph}$ 上的完整
$\mathscr K_\theta=\int H_{4,\theta;u_{\rm ph}u_{\rm ph}}\,du_{\rm ph}$。

## 2. 实际 principal-null 分支的完整分类

沿 R486，若 $q$ 是一个局部 profile，记 $p=q'$、$r_q=q''$，原局部 principal 因子为
$$
\mathscr L_s[q]
=\frac12\alpha_{\mathsf m}[q]
+\frac{Q}{8h^3}\{\gamma p-e_s r_q\},
\qquad
\alpha_{\mathsf m}[q]
=A_{1,\mathsf m}q+2A_{2,\mathsf m}p-2C_{\mathsf m}r_q .
\tag{5}
$$

**定理 1。** 在一个非空实际开区间中，同时满足(2)及
$$
\mathscr L_s[q]\equiv0
\quad\text{作为任意 }(q,q',q'')\text{ 的恒等式},
\tag{6}
$$
当且仅当，作一次固定的 $y=x+\omega_0$ 记号替换后，
$$
\begin{gathered}
k=0,\qquad\omega=\omega_0,\qquad
v=\frac{h_s}{h},\qquad v_s=1+v^2,\qquad h_s=hv,\\
h=H\sec\sigma,\qquad v=\tan\sigma,\qquad
\sigma=s-s_*,\quad H>0,\quad |\sigma|<\pi/2,
\tag{7}\\
\boxed{\mathsf A_s
=-\frac{v}{8h^2}R_y-\frac v8T_y.}
\tag{8}
\end{gathered}
$$
这里原两算子及其同锚原函数是
$$
R_y(q,q)=p^2+yJ(r_q^2),\qquad
T_y(q,q)=y^2p^2+yJ(y^2r_q^2+2p^2),\qquad
Jb(y)=\int_y^{r+\omega_0}b(t)\,dt .
\tag{9}
$$

**证明。** (6)中 $q$ 的系数给
$A_{1,\mathsf m}=0$，即原 $p_0,p_1,p_2$ 三个历史坐标均零。原 R73 密度的最高坐标为
$$
(M_{\rm raw})_{p_2}=-kh/2.
$$
由(2)与 $h>0$ 得 $k=0$，再由(1)得 $\upsilon=0$、$\omega=\omega_0$。这是沿一个实际区间的结论，不能只从一个时刻的零值推出。

在固定 $y$ 坐标中，$Q=1+h^2y^2$、$e_s=hvy$。当三项 $p_j$ 为零时，原 E8 系数为
$$
A_2=r_1+s_1y+t_1y^2,
$$
$$
C=r_0+(r_1+s_0)y+\frac32s_1y^2+t_1y^3.
$$
比较(6)的 $p,r_q$ 系数，准确得到
$$
A_2=-\frac{vQ}{8h^2},\qquad
C=-\frac{vyQ}{8h^2}.
$$
所以 $r_0=s_0=s_1=0$，
$r_1=-v/(8h^2)$、$t_1=-v/8$，即(8)。

另一方面，直接将 $k=0$、$\gamma=hv$、$e_s=hvy$ 代回原 R73 完整密度，得到
$$
\boxed{\Phi_{M_{\rm raw}}
=\frac{v^2-1}{8h^2}R_y-\frac{1+v^2}{8}T_y.}
\tag{10}
$$
对(8)的两系数分别求原 $s$ 导数，两式都准确等价于
$v_s=1+v^2$；并非另加一个独立一致性条件。联立 $h_s=hv$ 积分即得(7)。反代(5)(10)也逐项成立。证毕。

(6)仅是一条可明确分类的强分支。R486 的 signed 多包 principal 积分为零，不必迫(6)；一个固定母上的因子为零，也不必迫全部 jets 的(6)。还须保 R486(13)的真实第三入值：从中间切点写主项时，原常量
$
\partial_{r_q}^{\rm loc}T_{s_0}
-\beta_{s_0}^2+\alpha_{\mathsf A_{s_0}}^2/4
$
不能因(6)而删除。只有它由原全词起点条件确实为零时，(6)才消去该稿的整个显示主平方；任意其它入值仍留在本稿的完整场及(21)中。以下完整 ruling 结论不靠把这些不同范围混为一谈。

## 3. 该族确是实际几何，并有不可删除的返回障碍

原移动框架在 $k=0$ 时可取
$$
T=e_1,\quad
N=e_2\cos\sigma-e_3\sin\sigma,\quad
B=e_2\sin\sigma+e_3\cos\sigma.
\tag{11}
$$
它准确满足原框架方程；中心线有 $\alpha_s=h^2T$。固定一个欧氏平移后，
$$
\alpha=H^2\tan\sigma\,e_1.
$$
利用原物理坐标 $u_{\rm ph}=h/y$，完整浸入在 $(v,y)$ 上为
$$
\boxed{X(v,y)=(H^2v,\ H/y,\ -Hv/y).}
\tag{12}
$$
它落在真实二次曲面
$H^2X_3+X_1X_2=0$ 上。$H>0$、$y>0$ 时，$X_v,X_y$ 线性无关；且 $X_1,X_2$ 分别确定 $v,y$，所以每个有限坐标矩形本身是一个嵌入 patch。没有取小 $\sigma$ 极限或近似原度量。

式(7)可在任何紧子区间内实际使用。但(10)的 $t_1$ 坐标严格为
$$
(M_{\rm raw})_{t_1}=-\frac{1+v^2}{8}<0.
\tag{13}
$$
故任何正长度段都有非零总矩阵；它不能是原 $A_B=0$ 的第三 prototype，更不能单独成为 $M=T=0$ 控制块。

若要求整条相接路径都保持(6)，那么 $k=0$、同一 $\omega_0$ 和 ODE 唯一性使各段只是同一条(7)的延续；不能靠重标中心或拼两份正割段使(13)消失。即使在 $v=0$，
$$
h_s=0,\qquad h_{ss}=h(1+2v^2)=H\ne0,
\tag{14}
$$
也不能在保持此方程时接入一个 $C^\infty$ 常 scalar collar。

因此后置真实复位桥是可能继续研究的对象，但它必然离开这个特殊族。桥的全部 $A,T,V$、真实入值和内部 ruling 均仍须支付。

## 4. 任意两仿射场的 forcing 有一个严格闭合形态

本节只使用实际浸入(12)，不再要求历史满足(8)。因而它适用于该 patch 的任意真实二、三阶入值。

以撇号表示 $y$ 导数。给定两个或有限多个物理场
$$
Z_i(v,y)=a_i(y)+v b_i(y)
$$
和与 $(v,y)$ 无关的对称系数矩阵 $C$，令
$$
F_{ab}=\sum_{i,j}C_{ij}(Z_i)_a\cdot(Z_j)_b,\qquad a,b\in\{v,y\}.
$$
直接展开必有
$$
\boxed{
F_{vv}=f(y),\quad
F_{vy}=g(y)+\frac v2f'(y),\quad
F_{yy}=q_0(y)+vq_1(y)+v^2q_2(y).
}
\tag{15}
$$
特别，$F_{vy}$ 的一次系数不是独立输入：对称性给
$\sum C_{ij}b_i\cdot b_j'=f'/2$。这正覆盖原二阶 forcing
$(dY_f)^2-(dY_\phi)^2$、第三 forcing $-\mathcal S(Y_\phi,Z)$ 及第四 forcing(4)。

反过来，任意具有(15)形态且在同一右 collar 为零的 forcing，均有一个同右 collar 为零的仿射场解。明确取
$$
Z(v,y)=A(y)+vB(y),\qquad b(y)=B_2(y)
$$
为一个任意右 collar 平零函数。原线性度量算子使用
$$
(\mathcal L_XZ)_{vv}=2X_v\cdot Z_v,\quad
(\mathcal L_XZ)_{vy}=X_v\cdot Z_y+X_y\cdot Z_v,\quad
(\mathcal L_XZ)_{yy}=2X_y\cdot Z_y.
$$
由
$$
X_v=(H^2,0,-H/y),\qquad
X_y=(0,-H/y^2,Hv/y^2)
$$
逐项求解，准确得到五式
$$
\boxed{
\begin{aligned}
A_2'&=-\frac{y^2}{2H}q_0,\\
B_3'&=\frac{y^2}{2H}q_2,\\
A_3'&=b'+\frac{y^2}{2H}q_1,\\
B_1&=\frac{f+2HB_3/y}{2H^2},\\
A_1'&=\frac{g+HA_3'/y+Hb/y^2}{H^2}.
\end{aligned}}
\tag{16}
$$
$A_2,B_3,A_3,A_1$ 全部从同一个原右端积分，右常数为零；$B_1$ 用显示的代数式，$B_2=b$。所有真实左值完整保留。五式核对同时也给(15)剩下的 $vy$ 一次项，未再附加一条 forcing 条件。

若改变自由函数 $b$，差场恰为原齐次场 $Y_\psi$。准确地，
$$
\psi(y)=\frac{2y^2}{H}J\!\left(\frac b{y^2}\right),\qquad
A_1=\frac b{Hy}-\frac2H J\!\left(\frac b{y^2}\right),\quad
A_3=b,\quad B_2=b,
\tag{17}
$$
其余分量零，而
$$
Y_\psi(v,y)=
\left(-\frac{\psi'}{2y},\
Hv\left(\frac\psi y-\frac{\psi'}2\right),\
H\left(\frac\psi y-\frac{\psi'}2\right)\right).
\tag{18}
$$
式(17)仍是原右锚；一般右平零输入可留下真实左尾，不能直接称 $\psi$ 双 collar 紧。

## 5. 仿射 particular 确实描述原恢复，而非另换一个方便解

还须把(16)与原 R56 恢复接上，不能仅因存在一个 particular 就替换已固定的二、三阶场。

若两个右 collar 为零的场解同一个原 forcing，其差满足齐次方程。R56 对零 forcing 的原分子式准确给
$$
P=B=\eta_0=0,\qquad W_s=0.
$$
恢复场于是为 $-Y_W$，其中 $W$ 是一个与原 $s$ 无关的 profile。它在本几何上正具有(18)的仿射形态。原 rigid-motion 自由度若在一个右 collar 开集为零也只能为零。

所以：

**定理 2。** 在实际 patch(12)上，任何同右 collar 的原二阶恢复场，都对 $v$ 仿射；对其真实第三 forcing，任何同右 collar 的原第三恢复场也对 $v$ 仿射。结论保留任意真实段首第二、第三 profile 历史，不将它们重新置零。

**证明。** 原第一阶场即(18)。二阶 forcing 因(15)有仿射 particular；任一原解与它的差是(18)，故仍仿射。第三阶对已确定的完整二阶场重复此论证。证毕。

同样归纳适用于每个固定有限 Taylor 阶，只要此前实际场和 range 已有意义；这只是一个有限阶表示闭合，不是等距级数收敛或非线性族存在性。

定理 2 没有取消两侧 collar 或周期门。原 R56 的左 normal 尾、整个 characteristic period 仍由该原恢复支付。如果 lower-order ruling/period 不成立，不能把右 particular 当作合法双 collar 周期场。即使这些条件成立，(16)(17)中的累计量也须先保留再相消，不能逐包重设积分常数。

## 6. 完整第四 ruling 恰有三个真实系数

把任一固定原第二规范和原第三入值下的完整场写成
$$
Y_\phi=y_0+vy_1,\qquad
Z_\theta=z_0+vz_1,\qquad
W_\theta^0=w_0+vw_1.
\tag{19}
$$
这里 $w_0,w_1$ 是物理向量函数，不是第二 profile 规范 $w_\theta$；上标0只表示尚未加本节另行显示的第三齐次 $Y_{\chi_\theta}$。所有真实第三历史均已包含在 $W_\theta^0$ 中。

固定 $s$ 时，
$$
\frac{\partial}{\partial u_{\rm ph}}
=-\frac{y^2}{h}\frac{\partial}{\partial y},
\qquad du_{\rm ph}=-\frac h{y^2}dy .
$$
原物理积分由右 $y$ 端到左 $y$ 端，换回递增 $y$ 后，(4)准确给
$$
\mathscr K_\theta^0(s)
=-\frac1h\int_{\ell+\omega_0}^{r+\omega_0}
y^2\bigl(|(Z_\theta)_y|^2+
2(Y_\phi)_y\cdot(W_\theta^0)_y\bigr)\,dy .
\tag{20}
$$
这里没有分部积分，没有删左尾或任何已知平方。

定义三个完整数值泛函
$$
\begin{aligned}
\mathfrak a_\theta
&=-\int y^2\bigl(|z_0'|^2+2y_0'\cdot w_0'\bigr),\\
\mathfrak b_\theta
&=-2\int y^2\bigl(z_0'\cdot z_1'
+y_0'\cdot w_1'+y_1'\cdot w_0'\bigr),\\
\mathfrak c_\theta
&=-\int y^2\bigl(|z_1'|^2+2y_1'\cdot w_1'\bigr).
\end{aligned}
\tag{21}
$$
“数值”只指它们对冻结对象是实数，本稿没有评价这些积分。由(19)(20)，
$$
\boxed{\mathscr K_\theta^0(s)=
\frac{\mathfrak a_\theta+\mathfrak b_\theta v+
\mathfrak c_\theta v^2}{h}.}
\tag{22}
$$

(21)包含原完整 second square、全部 $Y$–third 交叉、二三阶入值及任何先前已选第二规范。它与 R486 仅取 principal 的(6)是不同层次的结论。三个泛函可能包含高导、非局部尾和实际入历史；本文没有把它们一律称为可免费加入旧 $F^\star$ 的 $C^2$ 观察。

在任何非空真实开子区间，$1/h,v/h,v^2/h$ 线性无关，因为乘以正 $h$ 后是三个普通多项式。因此 (22)恒零恰要求三个系数全零；三个不是预授控制秩。

## 7. 一个真正中心清理条件与两个 even 目标的原 range

取 patch 包含 $\sigma=0$，令其真实中心历史为
$\mathsf A_*=\Phi_{\mathsf m(s_*)}$。沿 R482，完整第二场写为
$$
Z_\theta=K_{D_\theta}-Y_{q_\theta},\qquad
q_\theta(s)=\mathsf A_sD_\theta+w_\theta .
\tag{23}
$$
这里 $K_D$ 含原 $P_D,B_D,\eta_D$，不是仅剩局部项。

若同一个第二规范满足真实中心清理
$$
\boxed{\mathsf A_*D_\theta+w_\theta=0
\quad\text{作为整个 profile 函数},}
\tag{24}
$$
则在中心 $\gamma=k_s=0$，R482 的完整 $\eta_D=\gamma a_h+k_sa_k$ 为零。由(23)，$Z_\theta(0,y)$ 只在固定 $e_2$ 方向，所有 $P_D,B_D$ 原尾仍保留在这个分量中。

令 $\mathcal R=\operatorname{diag}(-1,1,-1)$。原第一场满足
$$
Y_q(-v,y)=-\mathcal RY_q(v,y):
\quad y_0\in\operatorname{span}(e_1,e_3),\
y_1\in\operatorname{span}(e_2).
$$
二阶 forcing(15)的 $g,q_1$ 为零。(16)和中心 $Z(0)$ 的上述真实归一给
$$
z_0\in\operatorname{span}(e_2),\qquad
z_1\in\operatorname{span}(e_1,e_3).
\tag{25}
$$
具体地，五式中 $A_3'=b'$，同右锚给 $A_3=b$；中心 $A_3=0$ 迫 $b=0$，从而 $A_1=0$。这不是仅凭一种形式反射猜测原恢复的奇偶。

随后第三 forcing $-\mathcal S(Y_\phi,Z_\theta)$ 的
$f,q_0,q_2$ 全零。(16)遂给
$$
w_0\in\operatorname{span}(e_1,e_3),\qquad
w_1\in\operatorname{span}(e_2).
\tag{26}
$$
任意真实第三入值差只增加原 $Y_\psi$，仍是同一型，因此不要求把第三入历史置零。(25)(26)逐点代入(21)，准确得到
$$
\boxed{\mathfrak b_\theta=0.}
\tag{27}
$$
此结论涵盖完整场，而不只是(5)的 principal。

条件(24)也是一条真实规范条件，不是新的自由瞬时状态。原 $D_\theta$ 三矩全零使 $\mathsf A_*D_\theta$ 同 collar 真紧；在当前八副本库上，R326 的原 cubic 恒等式还给
$\mathbf I(\phi_\theta,\mathsf A_*D_\theta)=0$，所以这项中心清理保第三合法性。但它不自动支付第四 period、原十三行或其它段，不能与已经选定的全局 $w_\theta$ 冲突后再单独实施。

现在加入一个与 $s$ 无关的同 collar 第三 profile $\chi_\theta$。R47 的原式为
$$
\delta\mathscr K_\theta=-2\mathcal E_s(\phi_\theta,\chi_\theta).
$$
在本 patch 的固定 $y$ 坐标，
$$
\mathcal E_s(a,b)
=\frac1{4h}I_0^y(a,b)+\frac h4I_2^y(a,b),
\tag{28}
$$
其中
$$
I_0^y(a,b)=\int a''b'',\quad
I_1^y(a,b)=\int y a''b'',\quad
I_2^y(a,b)=\int(y^2a''b''+2a'b').
$$
原 $2a'b'$ 项全程保留。因为 $h^2=H^2(1+v^2)$，由(22)(28)得到以下完整等价：

**定理 3：单 patch 第三矩条件。** 对任意真实入值和给定的同 $s$ 第三规范，该 patch 的完整 ruling 全零，当且仅当
$$
\boxed{
\mathfrak b_\theta=0,\qquad
I_0^y(\phi_\theta,\chi_\theta)
=2(\mathfrak a_\theta-\mathfrak c_\theta),\qquad
I_2^y(\phi_\theta,\chi_\theta)
=\frac{2\mathfrak c_\theta}{H^2}.}
\tag{29}
$$
在中心清理(24)下，第一条件已由原场结构严格支付。若第三规范尚未被其它段锁定，且 $\phi_\theta\ne0$，则存在同 collar 紧规范的唯一兼容要求就是 $\mathfrak b_\theta=0$；两个 even 目标由下面的真实右逆同时支付。

两个剩余矩有真实、显式的共同右逆。对任意非零紧 $\phi$，R47 的三个密度
$$
L_0\phi=\phi'''',\quad
L_1^y\phi=y\phi''''+2\phi''',\quad
L_2^y\phi=y^2\phi''''+4y\phi'''
$$
线性无关。其 Gram $G_{ij}^\phi=\int(L_i^y\phi)(L_j^y\phi)$ 正定；对
$$
t_\theta=
\left(2(\mathfrak a_\theta-\mathfrak c_\theta),\
0,\ 2\mathfrak c_\theta/H^2\right)
$$
准确取
$$
\boxed{\chi_\theta
=\sum_{j=0}^2[(G^{\phi_\theta})^{-1}t_\theta]_j
L_j^y\phi_\theta .}
\tag{30}
$$
这是一条 profile 对整个 patch 同时使用，不是逐 $s$ 另选修正。$I_1^y=0$ 只是单 patch 允许选取的剩余一维矩；若别处要求另一值，可在(30)中如实换成该值。

若 $f,g$ 线性无关，则 $\phi_\theta\ne0$ 对全相位成立。紧相位圆上 Gram 逆光滑，故(30)保原光滑、周期；当原二三阶场及目标保 seed 时，$\mathfrak a,\mathfrak c$ 在 $0,\pi$ 为零，(30)也保这两个 seed。

这里实际支付的是完整 patch ruling。它不证明该 patch 单独的第四 period 为零。只有放入原总 $M=0$ 的同一个闭词时，R47 才保证这种全局第三齐次改动不改变整个第四 period。单 patch 的(13)反而说明不能直接套这个总矩阵零结论。

## 8. 已付保护芽会锁住这两个目标，不能再选择一次 χ

现在回到 R467/R469 的同一个最终词。其保护有理芽已用同一个
$(\bar w_\theta,\bar\chi_\theta)$ 支付，原十三门和全 period 已成立。保护芽的三个几何权独立，故在固定 $\bar w$ 后，第三规范的原三矩
$$
z_\theta=\mathbf I_x(\phi_\theta,\bar\chi_\theta)
=(z_0,z_1,z_2)
$$
已被唯一锁定。

本 patch 只作一次固定坐标记号 $y=x+\omega_0$，并不平移实际 profile。真实矩变换为
$$
I_0^y=I_0^x,\quad
I_1^y=I_1^x+\omega_0I_0^x,\quad
I_2^y=I_2^x+2\omega_0I_1^x+\omega_0^2I_0^x.
\tag{31}
$$
因此，对尚未加入 $\bar\chi$ 的同一完整(21)，本 patch 与旧规范兼容的准确条件是
$$
\boxed{
\mathfrak b_\theta=0,\qquad
z_0=2(\mathfrak a_\theta-\mathfrak c_\theta),\qquad
z_2+2\omega_0z_1+\omega_0^2z_0
=2\mathfrak c_\theta/H^2.}
\tag{32}
$$
不能因单 patch 的 Gram 满射就把已锁的 $z$ 再改成(30)。第三矩之外的任意零矩 profile 对整条路径 ruling 都无作用。

若还允许改变第二规范，原 R469 的全部平方与交叉须同步保留。记其固定抽取为 $\nu_*$、投影为
$$
\mathcal P_*F=F-\mathbf w(s)\cdot\nu_*(F),\qquad
\mathbf w=\left(\frac{1+(h\omega-k)^2}{4h},\
\frac{h\omega-k}{2},\frac h4\right).
$$
后继允许的 $\eta_\theta$ 必须同时属于原 period 核和原十三行核：
$$
L_f\eta_\theta=0,\qquad \mathcal A_\theta(\eta_\theta)=0.
\tag{33}
$$
R469 的同一个第三修正被准确迫为
$$
\mathbf I_x(\phi_\theta,\zeta_\theta)
=\frac12\nu_*(\mathcal B_\theta(\eta_\theta))
-\mathbf I_x(\bar w_\theta,\eta_\theta)
-\frac12\mathbf I_x(\eta_\theta,\eta_\theta).
\tag{34}
$$
代入后，整个路径的增量是
$$
\delta\mathscr K_\theta=\mathcal P_*\mathcal B_\theta(\eta_\theta).
\tag{35}
$$
平方并未省略；它准确出现在(34)，由同一个全局 $\zeta$ 支付。

## 9. 正割 patch 对原十三行核只增加三个明确线性行

可以进一步把(35)在本 patch 上写成原 E8 与 local pairing 的显示式，而不只留下一个一般函数条件。

真实历史沿(7)必有
$$
\mathsf A_s=\mathsf A_*-\frac{v}{8h^2}R_y-\frac v8T_y .
\tag{36}
$$
这里 $\mathsf A_*$ 是该解析正割段延到 $\sigma=0$ 时的真实常数部分；当中心实际位于 patch 内，它就是原中心入历史。没有为推导(36)要求 $\mathsf A_*=0$。

对任意 profile $\eta$ 定义
$$
\mathbf H_{\mathsf A_*,\theta}(\eta)
=-\mathbf I_x(\mathsf A_*D_\theta,\eta)
+2\mathbf I_x\{\phi_\theta,\mathsf A_*(\phi_\theta,\eta)\}.
\tag{37}
$$
原 R221 完整线性响应为
$$
\begin{aligned}
\mathcal B_\theta(\eta)
={}&2\mathcal T_s(\eta;D_\theta)
-4\mathcal T_s(\phi_\theta;\phi_\theta,\eta)\\
&-2\mathcal E_s(\mathsf A_sD_\theta,\eta)
+4\mathcal E_s\{\phi_\theta,\mathsf A_s(\phi_\theta,\eta)\}.
\end{aligned}
\tag{38}
$$
先减去 $2\mathbf w\cdot\mathbf H_{\mathsf A_*,\theta}(\eta)$。余项中 $\gamma=hv$、$e_s=hvy$ 及(36)的非常数部分均奇，$h,e,Q$ 均偶，所以余项对 $v$ 是奇函数。由完整场仿射性，它又属于
$\operatorname{span}\{1/h,v/h,v^2/h\}$：两种第二规范的完整 ruling 差仍在该空间，原规范平方和第三矩也在其中。因此余项恰只有一个系数：
$$
\boxed{\mathcal B_\theta(\eta)|_{\rm sec}
=\beta_\theta(\eta)\frac v h
+2\mathbf w\cdot\mathbf H_{\mathsf A_*,\theta}(\eta).}
\tag{39}
$$

这个线性行可以从原式直接定义，不需运行新的 forcing 或矩阵观察。置
$$
\mathsf R_H=-R_y/(8H^2)-T_y/8,\quad Q_H=1+H^2y^2,\quad
F_c=Q_Hc''-2H^2yc'+2H^2c,
$$
$$
\begin{aligned}
\dot{\mathcal T}_H(c;a,b)
=\frac1{32H^3}\int\big[&
Q_H^2c'''(a'b''+a''b'-ya''b'')\\
&-2H^2yQ_Hc'''a'b'\\
&+F_c\{(1-H^2y^2)a''b''-2H^2a'b'\}\big].
\end{aligned}
\tag{40}
$$
这是 $\partial_v\mathcal T_s|_{v=0}$，所有原尾转置和 local pairing 的条件同 R221。对 $D_\theta$ 按双线性展开(40)，准确有
$$
\begin{aligned}
\beta_\theta(\eta)=H\big[&
2\dot{\mathcal T}_H(\eta;D_\theta)
-4\dot{\mathcal T}_H(\phi_\theta;\phi_\theta,\eta)\\
&-2\mathcal E_H(\mathsf R_HD_\theta,\eta)
+4\mathcal E_H\{\phi_\theta,\mathsf R_H(\phi_\theta,\eta)\}\big].
\end{aligned}
\tag{41}
$$
原 $\mathcal E_H=I_0^y/(4H)+HI_2^y/4$。这给(39)的完整系数，而非 principal。

令
$$
t_\theta(\eta)
=2\mathbf H_{\mathsf A_*,\theta}(\eta)
-\nu_*(\mathcal B_\theta(\eta)),\qquad
t_y=t_2+2\omega_0t_1+\omega_0^2t_0 .
\tag{42}
$$
由(35)(39)及 $h^2=H^2(1+v^2)$，
$$
\boxed{
\delta\mathscr K_\theta|_{\rm sec}
=\frac{\beta_\theta(\eta)v+
\{t_0+H^2(1+v^2)t_y\}/4}{h}.}
\tag{43}
$$

把当前已经使用 $(\bar w,\bar\chi)$ 后的实际 residual 写成
$$
\mathscr R_\theta|_{\rm sec}
=(a_\theta+b_\theta v+c_\theta v^2)/h.
$$
则同一个后继 $\eta_\theta$ 支付本 patch 的全部 $s$，准确等价于三行
$$
\boxed{
b_\theta+\beta_\theta(\eta_\theta)=0,\qquad
a_\theta-c_\theta+t_0(\eta_\theta)/4=0,\qquad
c_\theta+H^2t_y(\eta_\theta)/4=0,
}
\tag{44}
$$
同时仍必须满足原(33)。

对当前 rank-one 库，R469 已证明
$\eta=\sum_i\lambda_i u_i+\sum_i\mu_i\chi_i+\eta_{\rm gap}$，
其中 gap 对全路径 $\mathcal B$ 与十三门均零。因此(44)只需在原同一 $2n$ 个母/平台列上加入三条明确线性行；平台的真实二次尾仍通过(37)(38)保留。有限多个正割 patch 给相应的有限多组三行，全部使用同一组 $\lambda_i,\mu_i$ 和同一个(34)，而非逐段另选 $\chi$。

本文没有宣称新增三行在原十三行核上满射，也没有以三个系数代替三阶或第四 period。相位光滑、周期、seed 及原核的有限降秩兼容仍按 R327/R394 保留。特别，逐相位可解不自动给一个允许的全圆规范。

## 10. 这一真实状态族已完成什么，以及全词仍须支付什么

这里得到的是一条可直接进入全路径研究的新机制。

- 几何本身是准确的实际 patch(12)，不是任意状态矩阵的形式赋值。
- 匹配历史(8)准确消去 R486 的 universal 局部 principal 因子；整个第四 ruling 另外由(20)—(22)完整处理。
- 任意真实入值的全 $s$ 问题缩为三个完整系数。中心清理(24)严格支付 odd 系数，单 patch 的两个 even 目标有(30)的真实右逆。
- 与已有保护芽接合时，三个第三矩已经锁定。不能重复消费(30)；必须使用同一十三行核中的(44)，或直接检查(32)。
- 第二规范平方、第三入历史、右原函数、真实左尾和 seed 都未删；(34)说明平方如何在同一规范内准确处理。

同时，(13)(14)是实际拼接的限制。正割分支本身没有正长度 $M=0$ 返回块，不能保持分支而接平常 collar。R472 的矩阵/第三桥若用于复位，必须把其全部第四基准统一交原成本控制；桥内的 ruling 仍须代入同一个 $(w,\chi)$。本稿没有给该桥自动继承(22)，也没有从一个 patch 的 Gram 满射推出整闭词 full range。

这也不排除 R486 中真正的常 scalar 关联族或其它受约束状态路径；本稿没有把开放状态族的否定扩大成这些低维路径的否定。下一实际门是明确的：对同一最终词选择允许的正割段及真实连接，保所有入历史，然后判断原(33)与新增(44)及连接段原 ruling 的共同像。不能只重复旧全成本 rank、只延长一个 prototype，或把 $M_c^2=0$ 当作 $\Phi_{M_c}\circ\Phi_{M_c}=0$。

本稿所有结论来自原场和同锚代数。唯一局部交叉核为(15)(16)及(25)(26)的分量代数；它不替代本文明确保留的全 period、左 collar 和最终同规范条件。
