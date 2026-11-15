# R279：同一完整 Gaussian 数据纤维内有限频率同时支付两个 even 能量

日期：2026-11-15。**完整纸面建设性证明；没有执行新的求积、符号程序、参数扫描或研究计算。**

本稿接 [R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md) 的真实低阶导数数据纤维。R277 已付全部72条 Gaussian 观测在该纤维内准确不变，并用一个有限频率的连续路径支付 $L_c=0$。本稿从同类新格点构造重新选择三个母包，使用真实 bulk 的两个 principal 向量和有限 N 的精确 IFT，同时取得

$$
L_c=M_c=0.
$$

原完整包装始终有 $L_s=M_s=0$；在真正的共振参数，已发表的一般微包身份再给 $N_c=N_s=0$。全部 Gaussian 观测仍与所选同形格点基点完全相同。因此 R277 的六条剩余 even 条目仍留欠，没有借 principal 或高频近似把它们置零。

这里不假定任意母函数 regular。母包、全部实际位置和完整副本一开始按下文重新选择；不搬移一个已求得的能量零解来冒称保持旧目标。

## 1. 原两个 bulk 与全部真实副本

保持同一右锚，并选一个已由既有真实闭 hook 安装允许的固定共振端芽

$$
h_e>0,\qquad \kappa\ne0,\qquad \varepsilon=\kappa^2/4.
$$

记原算子

$$
\mathcal G=-\Phi_{p_2}/2,\qquad
\mathcal D=\Phi_{p_1}-\Phi_{t_1}/8.
$$

对正区间中的实紧 q，置

$$
\Psi_q=x^2q''-2xq'+2q,\qquad
\Theta_q=3x^2q''-5xq'+4q.
$$

[R238 §3–4](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md) 的两个**准确 bulk**为

$$
\boxed{
S(q)=\frac1{64}\int x^6\Psi_q^2(q''')^2,\qquad
T(q)=-\frac1{64}\int x^5\Psi_q\Theta_q(q''')^2.
}
\tag{1}
$$

第二式保了整个原 $\mathcal D$。具体说，

$$
(\mathcal G(q,q)/x)''=-x\Psi_q q'''/4,
$$

$$
(\mathcal D(q,q)/x)''
=\Theta_q q'''/4-\Psi_q^2/(4x^3).
$$

最后一项在 bulk 中贡献
$\int x^2\Psi_q^3q'''/64=\int(\Psi_q^4)'/256=0$，
因为 q 的全部端 jets 为零。这是准确总导数，不是主尺度删项。

$G(q,q)$ 与 $D(q,q)$ 的原左尾一般非零；其除以 x 后为仿射尾。完整内槽的三矩零先使总体边界消失，之后才可利用不同微包的 bulk 支撑不交。由此对任意不交实微包与常实方向系数，

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
$$

有准确公式

$$
L_c=\sum_i\lambda_i S(u_i),\qquad
M_c=\sum_i\lambda_i T(u_i),\qquad
\lambda_i=a_i^2(b_i^2-a_i^2).
\tag{2}
$$

不把单包完整能量等同于(1)，也不删除其左尾。

现在保留 R277 的所有完整八/十二副本。记其实际相对平移为 $d_\nu$，共同 profile 幅度为 $\gamma_\nu$；若某副本翻 g，(2)的系数不变。令

$$
\mathcal W=\sum_\nu\gamma_\nu^4>0,\qquad
\bar d=\mathcal W^{-1}\sum_\nu\gamma_\nu^4d_\nu.
\tag{3}
$$

这些都是原完整副本的真实有限数据，不用一个理想均匀平均替代。第 i 个基本包在副本中的位置为

$$
\xi_{i,\nu}=\Xi+t_i+d_\nu.
\tag{4}
$$

$\Xi$ 是在最终求解前一次选定的大正位置。这里 $T_\xi u(x)=u(x-\xi)$ 是平移记号，与能量 $T(q)$ 区分。全部原能量为

$$
\begin{pmatrix}L_c\\M_c\end{pmatrix}
=\sum_i\lambda_i\sum_\nu\gamma_\nu^4
\begin{pmatrix}
S(T_{\xi_{i,\nu}}u_i)\\
T(T_{\xi_{i,\nu}}u_i)
\end{pmatrix}.
\tag{5}
$$

## 2. 正则母包的选择不循环依赖物理区间

仍用 R277 的 even $C^2$ Banach 域及完整多项式观测 $\mathcal F$。它包括全部 self 的实际平移系数和三个原二次矩，而非只选几条将要支付的能量。

先取一个 even 光滑参考母包 v，使 $v''(0)\ne0$。在它的一个固定小 $C^2$ 邻域中，可以固定 even cutoff $\chi$，支撑在中心附近，并使

$$
\int (u'')^2\chi^2\ge c_0>0
\tag{6}
$$

对该邻域中的所有 u 成立，同时 $u,u',u''$ 有统一上界。

$\mathcal F$ 的最大秩点在这个邻域内可以取为光滑母包。为说明这比“任意母包 regular”弱而准确，先选一个光滑最大秩点及一个非零 minor。该 minor 是母包的多项式函数；沿参考 v 到这个最大秩点的实线段，不是恒零多项式，因此在任意小的线段参数邻域都有非零值。于是可以在上面的固定邻域内选光滑最大秩 $u_0$，且 $u_0''(0)\ne0$。

下节的大 $\Xi$ 估计只用这个固定邻域的 $C^2$ 上下界、$\chi$ 和有限位置偏移，故可统一选定一个充分大的有限 $\Xi$。随后选包含所有最后副本的共同合法正 I，并固定右锚。几何 scalar 包络先定，$x+\omega>0$ 余量按 R271/R277 的同一规则支付。

之后才固定具体的光滑正则 $u_0$、真实 r 阶 minor 和纠正方向。或者先选 $u_0$ 再取该统一允许的 $\Xi$，得到同一结论。没有将一个能量已为零的实际 profile 事后平移。

## 3. 所有完整副本聚合后的 principal 比值

对第 i 个基本包，定义两个来自**实际基点**的有限积分

$$
\begin{aligned}
s_i={}&\frac1{128}\sum_\nu\gamma_\nu^4
\int x_{i,\nu}^6
\bigl(x_{i,\nu}^2u_0''-2x_{i,\nu}u_0'+2u_0\bigr)^2\chi^2\,dy,\\
t_i^\sharp={}&-\frac1{128}\sum_\nu\gamma_\nu^4
\int x_{i,\nu}^5
\bigl(x_{i,\nu}^2u_0''-2x_{i,\nu}u_0'+2u_0\bigr)\\
&\hspace{34mm}\cdot
\bigl(3x_{i,\nu}^2u_0''-5x_{i,\nu}u_0'+4u_0\bigr)
\chi^2\,dy,
\end{aligned}
\tag{7}
$$

其中 $x_{i,\nu}=\Xi+t_i+d_\nu+y$。特别 $s_i>0$。这些积分没有被当作可独立指定的坐标。

令 $r=u_0''$、$v_1=u_0'$、$K=\int r^2\chi^2>0$。由(1)原多项式直接展开：

$$
x^6\Psi^2=x^{10}r^2-4x^9rv_1+O(x^8),
$$

$$
x^5\Psi\Theta=3x^9r^2-11x^8rv_1+O(x^7).
$$

$u_0,\chi$ 为 even，故

$$
\int yr^2\chi^2=0,\qquad \int rv_1\chi^2=0.
$$

保留全部副本权与位置后，

$$
s_i=\frac{\mathcal WK}{128}
\{\Xi^{10}+10(t_i+\bar d)\Xi^9+O(\Xi^8)\},
$$

$$
t_i^\sharp=-\frac{\mathcal WK}{128}
\{3\Xi^9+27(t_i+\bar d)\Xi^8+O(\Xi^7)\}.
\tag{8}
$$

余项对所选有限位置和第2节固定 $C^2$ 邻域一致。于是准确比值

$$
\rho_i=\frac{t_i^\sharp}{s_i}
=-\frac3\Xi+\frac{3(t_i+\bar d)}{\Xi^2}
+O(\Xi^{-3}).
\tag{9}
$$

式(9)仅用于在一个充分大但有限的实际 $\Xi$ 上取得严格顺序，不把该展开本身当成完整能量等式。

R277 的格点中存在两个 high 包夹着一个 low 包。其显式17进制构造中，原位置0和33属于 high 类，位置1属于 low 类，因此可直接选

$$
t_1<t_2<t_3,\qquad
R_1=R_3=8B,\quad R_2=-B/2.
\tag{10}
$$

对应

$$
\lambda_1=\lambda_3=-72B^2<0,\qquad
\lambda_2=B^2/4>0.
$$

由(9)，固定充分大有限 $\Xi$ 后有

$$
\boxed{\rho_1<\rho_2<\rho_3.}
\tag{11}
$$

所有其他微包及副本仍在其最后位置，不因后续幅度求解而迁移。


## 4. 一个严格正 balance，及正幅度的正则极限根

定义真实有符号能量向量

$$
\mathbf v_i=\lambda_i(s_i,t_i^\sharp),\qquad i=1,2,3.
\tag{12}
$$

令 $A_i=|\lambda_i|s_i>0$。由(10)–(11)，

$$
\mathbf v_1=-A_1(1,\rho_1),\qquad
\mathbf v_2=A_2(1,\rho_2),\qquad
\mathbf v_3=-A_3(1,\rho_3).
$$

这些向量有严格正的准确平衡：

$$
\beta_1=\frac{\rho_3-\rho_2}{A_1},\qquad
\beta_2=\frac{\rho_3-\rho_1}{A_2},\qquad
\beta_3=\frac{\rho_2-\rho_1}{A_3},
$$

$$
\boxed{\beta_i>0,\qquad \sum_{i=1}^3\beta_i\mathbf v_i=0.}
\tag{13}
$$

而 $\mathbf v_1,\mathbf v_3$ 线性独立。因此三个真实向量的非负锥为整个 $\mathbb R^2$。这里不是将三个实际积分自由指定；(13)来自第3节已经选定的真实积分。

令 $\mathbf e_0$ 为全部最终位置和全部完整副本中，所有母包都取 $u_0$ 时的完整 $(L_c,M_c)$ 值。它只是一个固定有限向量。本稿无须假定它的第二坐标有任何符号。

先在实线性代数中解

$$
\mathbf e_0+\eta_1\mathbf v_1+\eta_3\mathbf v_3=0,
\qquad \eta_2=0.
$$

再将 $(\eta_1,\eta_2,\eta_3)$ 加上一个充分大的正倍数的 $\boldsymbol\beta$。由(13)，可取得三个严格正的有限数 $w_i$，满足

$$
\mathbf e_0+\sum_iw_i\mathbf v_i=0.
$$

置 $z_i^*=\sqrt{w_i}>0$。于是完整候选极限映射

$$
\mathcal E_\infty(\mathbf z)
=\mathbf e_0+\sum_{i=1}^3z_i^2\mathbf v_i
\tag{14}
$$

在严格正点 $\mathbf z^*$ 为零。上述 $\eta_i$ 只是求正系数的一步线性代数，不对应负成本或负重复次数；后面的实际 profile 只使用最终正幅度 $z_i$。

固定 $z_2=z_2^*$。以 $(z_1,z_3)$ 为两个真实参数，(14)在根处的导数为

$$
J_*=\begin{pmatrix}2z_1^*\mathbf v_1&2z_3^*\mathbf v_3\end{pmatrix},
\qquad \det J_*\ne0.
\tag{15}
$$

后续只用这个有限、真实、正则的二维根。即使 $\Xi$ 很大、向量夹角很小，(15)仍是准确非零；所需最终频率可以依赖这个已固定的逆矩阵。

## 5. 同一完整数据纤维中的真实有限频率族

采用 R277 §4 已证明的固定支撑 even $C^2$ Banach 空间。记 $\mathcal F$ 的最大秩为 r。第2节选出的光滑 $u_0$ 附近，存在 r 个实际输出坐标 $\mathcal F_*$ 及固定光滑 even 方向 $e_1,\ldots,e_r$，使

$$
D_{\mathbf a}\mathcal F_*\left(u_0+\sum_\ell a_\ell e_\ell\right)
\Big|_{\mathbf a=0}
$$

可逆。整个足够小邻域中秩恒为 r，故

$$
\ker D\mathcal F_*=\ker D\mathcal F.
\tag{16}
$$

所有方向支撑在同一个母包内部；它们不随频率或实际包位置改变。

有限 IFT 给小 $C^2$ 扰动 w 的光滑纠正系数 $\mathbf a(w)$，满足

$$
\mathbf a(0)=0,\qquad
\mathcal F_*\bigl(u_0+w+\textstyle\sum a_\ell(w)e_\ell\bigr)
=\mathcal F_*(u_0).
$$

只纠正 r 个坐标就足够保全部 $\mathcal F$，但理由不是忽略其余坐标。沿实际路径
$t\mapsto u_0+tw+\sum a_\ell(tw)e_\ell$，
所选 r 坐标的导数为零；由(16)，整个 $\mathcal F$ 的导数都为零。积分得

$$
\boxed{
\mathcal F\bigl(u_0+w+\textstyle\sum a_\ell(w)e_\ell\bigr)
=\mathcal F(u_0).
}
\tag{17}
$$

同时 $\mathbf a(w)=O(\|w\|_{C^2})$，且 $D\mathbf a$ 在这个固定小邻域中有界。

现在用比 R277 单能量无界路径更小的振荡尺度：

$$
w_N(z,y)=zN^{-3}\chi(y)\cos(Ny),
\tag{18}
$$

并定义真实光滑母包

$$
u_N(z)=u_0+w_N(z)+\sum_\ell a_\ell(w_N(z))e_\ell.
\tag{19}
$$

先固定包含 $\mathbf z^*$ 的一个有限、严格正的幅度盒。对盒中每一个 z，取足够大的同一个有限整数 N，使(18)位于 IFT 的固定小邻域。于是(17)对整个幅度盒成立。

由于 $\chi$ even、$\cos(Ny)$ even，所有 $u_N(z)$ 都是实 even 紧包。固定光滑纠正方向保证每个有限 N 的 profile 仍为 $C^\infty$。对固定幅度盒，一致有

$$
\|u_N(z)-u_0\|_{C^2}
+\|\partial_z u_N(z)\|_{C^2}=O(N^{-1}),
$$

$$
|\mathbf a(w_N(z))|
+|\partial_z\mathbf a(w_N(z))|=O(N^{-1}).
\tag{20}
$$

因此其真实三阶导数及参数导数为

$$
u_N'''(z,y)
=u_0'''(y)+z\chi(y)\sin(Ny)+\epsilon_N(z,y),
$$

$$
\partial_z u_N'''(z,y)
=\chi(y)\sin(Ny)+\partial_z\epsilon_N(z,y),
$$

$$
\sup_{z,y}\bigl(|\epsilon_N|+|\partial_z\epsilon_N|\bigr)
=O(N^{-1}).
\tag{21}
$$

(21)包括 cutoff 的全部导数项及所有纠正项。固定 $e_\ell$ 的三阶导有界，故它们的贡献确为 $O(N^{-1})$；没有假定任意 $C^2$ 小扰动的三阶导也小。

将三个基本母包分别替换为 $u_N(z_i)$，并在各自预先固定的每一个完整副本中使用同一个 $u_N(z_i)$。其他母包保持 $u_0$。每个包始终有完全相同的 $\mathcal F$ 值：

$$
\mathcal F(u_N(z_i))=\mathcal F(u_0),\qquad i=1,2,3.
\tag{22}
$$

特别，整体 inner 三矩在整个参数盒内准确为零，所以第1节完整边界已付的能量公式(5)始终适用。

## 6. 完整原能量映射的 C¹ 收敛

令 $\mathcal E_N(\mathbf z)$ 是(19)所定义的实际圆、实际完整副本和固定右锚下的完整 $(L_c,M_c)$。本节证明

$$
\boxed{
\mathcal E_N\longrightarrow\mathcal E_\infty
\quad\hbox{在上述固定幅度盒上以 }C^1\hbox{ 收敛。}
}
\tag{23}
$$

这是对原式(1)、(5)的收敛，不是只对 principal 的形式收敛。

在每一个实际位置，(1)可写成

$$
\int A(q,q',q'';x)\,(q''')^2,
$$

其中两个准确系数分别为

$$
A_S=\frac{x^6\Psi_q^2}{64},\qquad
A_T=-\frac{x^5\Psi_q\Theta_q}{64}.
\tag{24}
$$

它们只含二阶以内的原 jets，而且是这些 jets 的多项式。由(20)，将 q 取为各个真实平移后的 $u_N(z)$ 时，(24)一致趋于其 $u_0$ 值，参数导数一致为 $O(N^{-1})$。所有实际 x、平移、副本权已固定且有限；这些误差的常数可以依赖它们，不需要对一个尚未选择的布局作统一承诺。

再用(21)展开平方。准确积分包含：

1. 原基点项；
2. 与 $\sin(Ny)$ 线性的交叉项；
3. $z^2\chi^2\sin^2(Ny)$ 项；
4. 一致为 $O(N^{-1})$ 的余项及其 z 导数。

第2项的系数是固定光滑紧函数，普通分部积分使其积分为 $O(N^{-1})$。第3项中

$$
\sin^2(Ny)=\frac12-\frac12\cos(2Ny),
$$

振荡部分同样积分为 $O(N^{-1})$。同一估计逐项适用于 z 导数；系数本身的 z 导数已由(20)、(24)控制。于是每个实际副本准确有

$$
\begin{aligned}
S(T_\xi u_N(z))
={}&S(T_\xi u_0)
+\frac{z^2}{128}\int
(\xi+y)^6\Psi_{T_\xi u_0}(\xi+y)^2\chi(y)^2\,dy
+O(N^{-1}),\\
T(T_\xi u_N(z))
={}&T(T_\xi u_0)
-\frac{z^2}{128}\int
(\xi+y)^5\Psi_{T_\xi u_0}(\xi+y)
\Theta_{T_\xi u_0}(\xi+y)\chi(y)^2\,dy
+O(N^{-1}),
\end{aligned}
\tag{25}
$$

两式余项均在所选 z 区间中为 $C^1$ 的 $O(N^{-1})$。

最后把(25)按实际 $\gamma_\nu^4$ 相加，并乘实际 $\lambda_i$。有限和与(7)、(12)完全对应，给

$$
\mathcal E_N(\mathbf z)
=\mathbf e_0+\sum_i z_i^2\mathbf v_i+O_{C^1}(N^{-1}),
\tag{26}
$$

即(23)。特别，所有局部低阶项、真实副本位置差和原 $\mathcal D$ 中的项都已进入基点或准确系数；它们没有因高频而被从方程中删除。

## 7. 一个有限整数 N 的准确双零

现在固定 $z_2=z_2^*$。在 $(z_1^*,z_3^*)$ 的一个足够小闭球内，两个坐标仍严格正，并可使

$$
\|I-J_*^{-1}D\mathcal E_\infty\|\le\frac14.
$$

由(23)，所有充分大的有限 N 都满足

$$
\|I-J_*^{-1}D\mathcal E_N\|\le\frac12
$$

于同一个球；同时
$J_*^{-1}\mathcal E_N(\mathbf z^*)\to0$。
因此可再选一个有限整数 N，使

$$
(z_1,z_3)\longmapsto
(z_1,z_3)-J_*^{-1}\mathcal E_N(z_1,z_2^*,z_3)
\tag{27}
$$

将该闭球映入自身并为压缩映射。它有实际固定点
$(z_{1,N},z_{3,N})$，仍严格正，满足

$$
\boxed{
L_c=M_c=0
}
\tag{28}
$$

的完整原方程。

这个论证不要求把 $\mathcal E_N$ 对 $1/N$ 作解析延拓，也不需要无穷频率的 profile。选定一个满足上述条件的有限整数 N 后，(19)给有限个真实 $C^\infty$ 函数，(27)给其有限参数中的准确根。中间的极限只用于证明该有限选择和局部根存在。


## 8. 所有已付 Gaussian 数据、完整第三及六能量

### 8.1 每个实际包的完整数据都不变

式(22)保留全部 self 的实际平移系数及三个原二次矩。因此任意一个实际副本位置的 self 值都不变；任意一对包的原跨核
$\Gamma(\mathbf m_i,\mathbf m_j)$
也不变。实际左右次序和全部平移固定，所以原有序前缀不变。

由 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的原 self/cross 公式，全部72条 Gaussian 观测在整个参数盒以及最后根处都与同形基点完全相同。这个结论使用准确(22)，与(23)的近似无关。

特别，R277 的全部36个 odd 和30个 even 零保留。剩余六条原 even 条目仍是

| Gaussian pair | 未付的 $E_{22}$ 所在外矩 |
|---|---|
| $(1,-2)$ | $I_0,\ I_1$ |
| $(1,-3)$ | $I_0,\ I_2$ |
| $(-1,-2)$ | $I_1,\ I_2$ |

它们的值也保留，但本稿没有证明其为零。这个列表不等同于六个独立约束。

每个母包的 $I_0$ 保持同一个严格正值，方向系数 $(a_i,b_i)$ 没有变化。因此共同三矩、圆的非退化以及原来至少三条不同的射影方向都保持。不存在某个被替换包因纠正而整体变零的问题；也没有把圆变成可经固定 $GL_2$ 分离的两个支撑。

### 8.2 真实几何与第三数据的范围

完整几何采用 R277 中已经安装的真实闭 hook：其 $M=0$，完整第三算子为
$\kappa_{\rm hook}\mathcal H$，$\kappa_{\rm hook}\ne0$，原 frame/位移闭合及公共端口条件均保持。这里的 $\kappa_{\rm hook}$ 与本稿端芽值 $\kappa$ 区分；不是只由八个 profile 副本便宣任意几何的完整第三已付。

母包在每个活动区间上仍为 rank-one 方向，且所有原矩准确保留。[R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 与 R277 §8 已付的 hook/八完整副本原式，遂对这些实际新母包仍然适用。全部副本、几何及右锚保持不动；不需要重新编译一个第三 forcing 或假定其 incoming history 为零。

### 8.3 Odd 能量与共振第三层

首能量 $L_s$ 对 g 奇。其完整平移多项式次数不超过10；第二能量 $M_s$ 的对应次数不超过9，直接由(1)的原多项式可见。固定的十二完整副本使用十一阶有限差分，故对任意一组当前母包都准确给

$$
L_s=M_s=0.
\tag{29}
$$

这两个式子不依赖母包同形，也不依赖其高频近似；共同平移时仍使用每个完整基本块的实际原函数。

最后采用 [R256 §10](R256-sharp-profile-energy-contrast-and-multiwidth-joint-construction.md) 已证明的**一般 rank-one 微包**身份，而非只对旧 $\pm$ 两方向族成立的缩窄公式。对 $B=gg-ff$ 或 $B=fg$，三矩先使
$\mathcal GB,\mathcal DB,\mathcal TB$
紧，整个边界消失后才取各微包的 bulk。原局部自项 $\mathcal J_7$ 为零，以及
$U_T=-8(T+S_1)$，在真实共振
$\varepsilon=\kappa^2/4$
给

$$
\Lambda_f(B)
=6\sum_i a_i^2d_iT(u_i)
=6E(\mathcal G(f,f),\mathcal DB),
\tag{30}
$$

其中 $d_i=b_i^2-a_i^2$ 或 $d_i=a_ib_i$，并保全部完整副本。这个身份允许各 $u_i$ 不同，故适用于本稿的三个独立纤维替换。

先用(28)、(29)付完前四门后，完整已识别的第三层遂满足

$$
N_c=6M_c,\qquad N_s=6M_s.
$$

因此最终圆准确有

$$
\boxed{
L_c=L_s=M_c=M_s=N_c=N_s=0.
}
\tag{31}
$$

没有在第三层推导前省掉前四门，也没有从这些 bulk 身份把 Gaussian history 局域化。

## 9. 完整选择顺序和所得到的真实构造

为避免用尚未选定的参数补回一个已冻结的结果，选择顺序明确如下。

1. **固定几何和有限布局类型。** 选一个既有实际安装允许的非零端芽值 $\kappa$，保持真实闭 hook、$\varepsilon=\kappa^2/4$、有限桥和 scalar 包络。选 R277 的有限格点、high–low–high 三个位置、八/十二完整副本及其真实相对位移与幅度。
2. **固定母支撑和大正位置。** 取固定 even 参考母包的小 $C^2$ 邻域与 cutoff，先支付(6)。根据这一邻域的统一界，选择一个使(11)严格成立的有限 $\Xi$。随后按 [R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R114](R114-constrained-static-costs-and-real-zero-matrix-words.md) 与 [R223](R223-Morse-closed-hooks-with-exact-pure-and-eight-flux-constraints.md) 的真实顺序，固定包含全部最终包及公共 collars 的共同合法正 I。scalar 包络已经固定，所以可保 $x+\omega>0$；这不是对任意狭窄旧 I 的承诺。
3. **固定真实正则纤维。** 在该固定支撑的邻域选择光滑最大秩 $u_0$、实际非零 minor 及光滑纠正方向；定义全部实际 principal 积分。所选母包不是一个未经证明 regular 的旧冻结函数。
4. **先定有限幅度目标。** 用(13)将基线向量转成一个严格正的有限极限根，固定其小正幅度盒、可逆矩阵 $J_*$ 和固定中包幅度。
5. **最后才选有限频率并求准确根。** 在这个已定盒上证明完整能量的 $C^1$ 收敛，选择一个足够大的有限整数 N，再用(27)得到实际参数。不得在求根后另改位置、副本或物理区间。
6. **固定最后 profile 圆。** 此时所有母包与全部副本都为有限个实 $C^\infty$ 紧函数。需要共同 $I_0$ 归一时可同乘一个正实常数；原矩的等式、全部零及纤维数据的相等关系均按其真实齐次性保持。

于是得到一组新的、真正不可经固定 $GL_2$ 分离的有限三矩圆。在同一个固定几何、I 和右锚上，它具有：

- 原合法完整第三数据；
- 与 R277 所选格点基点完全相同的全部72条 Gaussian 观测；
- 其中已经证明的36个 odd 和30个 even 零；
- 全部六个已识别能量条件(31)的准确零。

设计过程中改变母包通常改变由 seed 指定的目标度量。本稿不把这条设计过程称为保持某个旧目标 g 的等距变形。最后固定的圆与几何才是同一目标下的候选。

剩余六条 Gaussian even、整个完整 fourth ruling 的其余函数系数、完整 period 与同一个合法 joint gauge 的可解性均未由本稿支付。高频方案也不承诺一个预先固定的三阶导上界。它所证明的建设性事实是：**完整低阶导数观测的同一真实纤维，确可用三个有限频率母包控制，在保留全部真实副本和历史数据的同时，把两个 even 能量一起准确置零。**

