# R287：两种偶振荡形状在同数据纤维内支付完整负三—负二乘积

日期：2026-11-15。**真实有限参数的纸面存在证明；没有执行新的求积、符号程序、profile 采样、人工检查或研究运行。**

[R286](R286-complete-mixed-minus-three-minus-two-Gaussian-moments.md) 将当前 $E_{-3}E_{-2}$ 的 whole-circle 系数准确化为一个随 $H_1=0$ 自动消失的矩和两个新的余门。它还展示了同一个 even 振荡因子下的真实 principal 共线性：仅增加位置不能把第一余门与 $H_0$ 分开。

本稿从一开始选两个不同的真实 even 振荡因子，仍在同一个 [R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md) 数据纤维内，使用现有布局的两组各七个交替 high/low 微包。每组的主向量正锥恰为一个六维超平面；两个不同超平面合为完整七维空间。随后用真实一致 $C^1$ 极限和有限频率隐函数定理，联立支付
$H_0,H_1,H_2,L_c,M_c$ 与 R286 两个余门。

得到的同一个有限圆保持全部72面积、六识别能量及整个 $E_{-3}^2$，并新增整个 $E_{-3}E_{-2}$ 为零。其余八个对称乘积、零/一层 history、canonical period 与完整第四存在性仍未支付。

来源：[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md)、[R281](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md)、[R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md)、[R284](R284-six-alternating-packets-pay-the-square-history-and-even-energies.md)、[R285](R285-principal-splitting-of-symmetric-Gaussian-products.md)、R286。

## 1. 七个完整量是原32观测的准确子系统

保持 R286 的实际共振常数

$$
a=-\frac{51\kappa^4+2\kappa^2+8}{64h_e^2},\quad
b=-\frac{17\kappa^4+4\kappa^2}{32h_e^2},\quad
c=-\frac{\kappa(41\kappa^4+27)}{216h_e^3},
\tag{1}
$$

其中 $\kappa\ne0$，所以 $a,b,a+b,c$ 均非零。包方向仍为
$b_i^2=B_0$、$R_i=a_i^2-B_0\in\{-B_0/2,8B_0\}$，记
$\lambda_i=-a_i^2R_i$。

沿用 R286 的完整实际加权量
$\mathsf K_j,\mathsf J_j,\mathsf C_j$；特别

$$
H_0=\mathsf K_0,\quad H_1=\mathsf K_1,\quad
H_2=\mathsf K_2+2\mathsf C_0.
$$

定义

$$
U=4a\mathsf J_1+(2a+5b/2)\mathsf C_0,
$$

$$
V=-(a+b)\mathsf K_3+4a\mathsf J_2-(2a+b)\mathsf C_1
\tag{2}
$$

及七个真实量

$$
\mathcal W=(-H_0,-H_1,-H_2,L_c,M_c,U,V).
\tag{3}
$$

所有低阶项都留在(2)—(3)。这里没有把 $U,V$ 的 principal 单独作为目标。

为与 R285 的32维必要观测对应，令
$\widetilde Q_{-3,-2,j}$ 是不同字母乘积系数除以2后的第 j 外矩，平方 $Q_{-3,-3,j}$ 不除以2。R282/R286 的准确式给

$$
-H_j=\frac{Q_{-3,-3,j}}{c^2},\qquad j=0,1,2,
$$

$$
U=\frac{\widetilde Q_{-3,-2,1}}c
-\frac{a+b}{c^2}Q_{-3,-3,2},\qquad
V=\frac{\widetilde Q_{-3,-2,2}}c.
\tag{4}
$$

这些等式在当前 even 同纤维、完整复制后按 $\theta=\pi/2$ 取值；R286 已证明其 whole-circle 表为同一个 $\sin^2\theta$ 倍。因此 $\mathcal W=0$ 确实支付整个两个乘积，而不是只在一个相位做采样。

(4)是原32观测的固定线性子系统，加上本来就在其中的 $L_c,M_c$。本稿没有把32个量都变成七个，也不声称其余主项或 $C^2$ 余项自动相容。

## 2. 同一个有限数据纤维和两种真实 even 因子

按 R281，从一开始取

$$
u_0=\psi P_0,\qquad e_\ell=\psi P_\ell,
$$

其中 $u_0$ 是原 $\mathcal F$ 的真实最大秩基点，$P_0$ 在闭母支撑上严格正，且 $u_0''(0)\ne0$。这不是对任意已经冻结的旧母包作正则性假设。

简记 $v_0=u_0'$、$r_0=u_0''$。在中心小邻域 $r_0\ne0$，even 性给

$$
v_0(y)=r_0(0)y+O(y^3),\qquad
\frac{y v_0(y)}{r_0(y)}=y^2+O(y^4).
\tag{5}
$$

该函数在足够小的正 y 区间严格递增。因此可以先取两个非零 even 光滑 cutoff，分别集中在两个互不相同的小 $|y|$ 邻域，使

$$
K_t=\int r_0^2\chi_t^2>0,\qquad
\rho_t=\frac14
\frac{\int yv_0r_0\chi_t^2}{\int r_0^2\chi_t^2},
\qquad \rho_1\ne\rho_2.
\tag{6}
$$

具体地，让两个 cutoff 支撑上(5)的值域严格分离，正权平均就严格不同。这个论证不需要假定某个未计算积分的符号。

若保解析端芽类别，按 R281 的同一密度引理，将两个 cutoff 分别用
$\chi_t=\psi Q_t$ 的 even 多项式倍数作足够小的 $C^2$ 逼近。分母的正下界及两个比值的严格间隙都是开条件，因此(6)仍成立。解析因子不必在母包内部某个开区间上准确为零。

对 t=1,2 使用同一组固定纠正方向：

$$
u_{t,N}(z,y)
=u_0(y)+zN^{-3}\chi_t(y)\cos Ny
+\sum_\ell a_{t,\ell,N}(z)e_\ell(y).
\tag{7}
$$

同一个原 minor 在两族上都可用；有限 IFT 给

$$
\mathcal F(u_{t,N}(z))=\mathcal F(u_0)
\tag{8}
$$

以及每个预先固定有限幅盒上的一致估计

$$
u_{t,N}-u_0,\ \partial_z u_{t,N}=O_{C^2}(N^{-1}),
$$

$$
u_{t,N}'''=u_0'''+z\chi_t\sin Ny+O_{C^0}(N^{-1}),\quad
\partial_z u_{t,N}'''=\chi_t\sin Ny+O_{C^0}(N^{-1}).
\tag{9}
$$

只需有限两个 t；所有估计可统一。没有把两个数据纤维混合，也没有增添或删去原 $\mathcal F$ 观测。

## 3. 两组七个真实交替微包

R280 的基本17进制编码把数位和0类取为 high。七个真实索引

$$
0,\ 1,\ 33,\ 34,\ 49,\ 50,\ 65
\tag{10}
$$

依次为 high、low、high、low、high、low、high；最后一个
$65=3\cdot17+14$ 的数位和为17。

使用原第二编码层的 k=0 和 k=1 两份：

- 在正布局 $i=kL+j$ 中，两组分别取 k=0、1；
- 在负布局 $i=jK+k$ 中，仍分别取 k=0、1。

两组的14个实际索引互异。每组都有严格递增的七个位置
$t_{t,1}<\cdots<t_{t,7}$，并且

$$
\operatorname{sgn}\lambda_{t,i}=(-1)^i,\qquad i=1,\ldots,7.
\tag{11}
$$

第 t 组使用 $\chi_t$。k=1 对原 $T_i=a_ib_i$ 造成的既有符号变化并不改变 $\lambda_i$ 或(11)，也不改变整个原有限编码。我们没有重排一个已经固定的旧圆；这些是新存在构造从一开始作出的有限选择。

每个选中基本包在其全部八/十二完整副本中使用同一个 $u_{t,N}(z_{t,i})$。其实际正四次复制权全部保留。由于(8)以及原 rank-one/完整复制证明，72面积、三矩和完整第三条件在整个14参数盒内准确保持。

## 4. 保全部副本的七维 principal 列

固定一个完整 block 的真实副本偏移 $d_\nu$ 与正四次权
$\omega_\nu$，令 $W=\sum_\nu\omega_\nu>0$。对每个 t 定义

$$
P_{t,j}(X)=
2\sum_\nu\omega_\nu
\int(X+d_\nu+y)^j r_0(y)^2\chi_t(y)^2\,dy,
\quad j=0,1,2,3,
$$

$$
Q_{t,j}(X)=
\frac12\sum_\nu\omega_\nu
\int(X+d_\nu+y)^j v_0(y)r_0(y)\chi_t(y)^2\,dy.
\tag{12}
$$

设

$$
k_t=2WK_t>0,\qquad
\bar d=W^{-1}\sum_\nu\omega_\nu d_\nu.
$$

$P_{t,j}$ 是首系数 $k_t$ 的真实 j 次多项式。even 性准确给

$$
Q_{t,0}=0,\qquad Q_{t,1}=\rho_t P_{t,0},\qquad
Q_{t,2}=2\rho_t P_{t,1}.
\tag{13}
$$

例如 $P_{t,1}=k_t(X+\bar d)$；$Q_{t,2}$ 的 $y^0,y^2$ 项都因
$v_0r_0\chi_t^2$ 为 odd 消失，余下是
$(X+\bar d)\sum_\nu\omega_\nu\int yv_0r_0\chi_t^2$。
这说明(13)保留了全部实际偏移，未把副本中心理想化。

记 $\mathcal S_t,\mathcal T_t$ 为 R284 原能量 principal，即

$$
\mathcal S_t(X)=\frac1{128}\sum_\nu\omega_\nu
\int x^6\Psi(x,y)^2\chi_t^2,\qquad
\mathcal T_t(X)=-\frac1{128}\sum_\nu\omega_\nu
\int x^5\Psi(x,y)\Theta(x,y)\chi_t^2,
\quad x=X+d_\nu+y.
$$

其中 $\Psi(x,y)=x^2r_0(y)-2xv_0(y)+2u_0(y)$、
$\Theta(x,y)=3x^2r_0(y)-5xv_0(y)+4u_0(y)$；物理 x 与母坐标 y 不混用。准确有

$$
\mathcal S_t=s_tX^{10}+O_{\rm poly}(X^9),\qquad
\mathcal T_t=-3s_tX^9+O_{\rm poly}(X^8),\qquad
s_t=WK_t/128>0.
\tag{14}
$$

这里 $O_{\rm poly}$ 只是次数较低的固定真实多项式，不是省略一个有限 N 上的误差。

因为 $\lambda_i=-a_i^2R_i$，第 t 组原七量(3)的 principal 列为

$$
\boxed{
v_t(X)=
\begin{pmatrix}
P_{t,0}\\ P_{t,1}\\ P_{t,2}\\
\mathcal S_t\\ \mathcal T_t\\
-4a\rho_tP_{t,0}\\
(a+b)P_{t,3}-8a\rho_tP_{t,1}
\end{pmatrix}.
}
\tag{15}
$$

真实增量是 $z_{t,i}^2\lambda_{t,i}v_t(X+t_{t,i})$。
第六行的负号来自 $\mathsf J_j$ 的权是 $a_i^2R_i=-\lambda_i$；
第七行同时保了 $\mathsf K_3$ 与 $\mathsf J_2$，没有只用三次领先项替代完整列。

## 5. 每组恰有一个已知超平面关系，并有真实正核

由(15)，每一列都在六维超平面

$$
\mathscr H_t=
\{x\in\mathbb R^7:x_6=-4a\rho_t x_1\}.
\tag{16}
$$

删除第六个从属坐标后，对剩余六行作固定可逆变换：前四个 $P_{t,j}$ 三角归一为 $1,X,X^2,X^3$，再将能量两行交换、缩放为 monic 九、十次多项式。第七原行中可以减去已存在的一次行，并除以非零 $a+b$，所以这个变换确可逆。

于是六行化为

$$
1,\ X,\ X^2,\ X^3,\ q_{t,9}(X),\ q_{t,10}(X).
\tag{17}
$$

取任意六个固定递增 $\tau_1<\cdots<\tau_6$。消去高两行 Taylor 的0—3次部分后，4、5次项的准确首系数为

$$
\binom94\binom{10}5-\binom95\binom{10}4
=126\cdot252-126\cdot210=5292.
$$

因此

$$
\boxed{
\det(17)\big|_{X+\tau_1,\ldots,X+\tau_6}
=
5292X^{10}\prod_{i<j}(\tau_j-\tau_i)+O(X^9).
}
\tag{18}
$$

任何原低次系数或更高 Taylor 幂只进入 $O(X^9)$。这是一条有限多项式身份的首项论证，不涉及数值秩或采样。

每组只有七个删列子式；两个 t 及最后五个 block 也都有限。所以一次选择足够大的**有限**共同正 X，就使每组全部六阶子式同号、非零。

按(11)和 cofactor 身份，每组七条带符号的列
$\lambda_{t,i}v_t(X+t_{t,i})$ 有一个所有坐标严格正的核向量，并且张成整个 $\mathscr H_t$。更具体地，若归一六行矩阵删去第 i 列所得正子式为 $D_{t,i}$，则

$$
w_{t,i}=D_{t,i}/|\lambda_{t,i}|>0,\qquad
\sum_iw_{t,i}\lambda_{t,i}v_t(X+t_{t,i})=0.
\tag{19}
$$

固定行变换不影响此原向量恒等。因此这七列的非负锥恰为整个六维线性空间 $\mathscr H_t$：任意实系数表示加一个足够大的正倍数(19)，就得到全部严格正的系数表示。

## 6. 两个真实超平面共同支付任意完整七维基线

由 $a\ne0$、$\rho_1\ne\rho_2$，(16)的两个超平面不同，准确有

$$
\mathscr H_1+\mathscr H_2=\mathbb R^7.
\tag{20}
$$

这不是只数参数。给任意目标的第一、第六坐标 $(x_1,x_6)$，方程

$$
r_1+r_2=x_1,\qquad
-4a(\rho_1r_1+\rho_2r_2)=x_6
$$

有唯一实解；其余五个坐标可以自由分给两超平面。然后分别应用第5节的原正锥。

令 b 是所有基本包为 $u_0$ 时的**完整**七量(3)。它含
$2\mathsf C_0$、$(2a+5b/2)\mathsf C_0$、$-(2a+b)\mathsf C_1$，
也含所有未选包的原值。此处向量 b 与 Gaussian 常数 b 可由上下文区分；没有把这些已知基线抛掉。

由(20)，先取两个超平面中的实表示，再分别加上(19)的正核。得到有限严格正权 $w_{t,i}^*$，使

$$
b+\sum_{t=1}^2\sum_{i=1}^7
w_{t,i}^*\lambda_{t,i}v_t(X+t_{t,i})=0.
\tag{21}
$$

真正进入 profile 的幅度为 $z_{t,i}^*=\sqrt{w_{t,i}^*}>0$；
中间的实线性表示不是负包、负复制或非整数拼接。

联合14列的秩恰为7。可直接选择第1组任意六列和第2组任意一列：
前六列张成 $\mathscr H_1$；后列的第一坐标非零，且
$\rho_2\ne\rho_1$，所以它不在 $\mathscr H_1$。这给下一真实 IFT 所需的具体七列非退化，而不只给正锥满的抽象结论。

## 7. 有限 N 的真实七变量根

固定(21)的有限正幅度盒。将14个所选实际包分别换成(7)，其余包保 $u_0$；所有完整副本复制同一族参数。记实际完整映射为
$\mathcal W_N(\mathbf z)$。

原 $\mathcal F$ 准确保持各 $C_{0,i}$，even 性和已固定位置也准确保持 $C_{1,i}$。其余原三阶部分均是 $C^2$ 系数乘 $(u''')^2$。由(9)和原 R279 的振荡平均与参数导数论证，准确有

$$
\boxed{
\mathcal W_N(\mathbf z)\longrightarrow
b+\sum_{t,i}z_{t,i}^2\lambda_{t,i}v_t(X+t_{t,i})
\quad\text{在固定盒上一致 }C^1.
}
\tag{22}
$$

所有有限 N 余项仍在左边。它们没有被称零，也没有假定原 F 固定任意二阶泛函；这里只用了 R286 已准确提取的完整局部式及原 F 确实固定的 $C_{0,i}$。

在 $\mathbf z^*$ 处，选第6节那七个幅度变量，其 Jacobian 的列是

$$
2z_{t,i}^*\lambda_{t,i}v_t(X+t_{t,i}),
$$

故可逆。把其余七个幅度固定在各自严格正值，真实有限维 $C^1$ 隐函数定理或其收缩形式给：存在一个充分大的**有限整数** N 和附近真实正幅度 $\mathbf z_N$，使

$$
\boxed{\mathcal W_N(\mathbf z_N)=0.}
\tag{23}
$$

这里不是把 $1/N$ 当作连续光滑参数；是可逆极限零点对一致 $C^1$ 小扰动的稳定性。所有常数允许依赖已经固定的巨大但有限布局、幅盒、共同位置与逆矩阵。

由 R282/R286 的准确 iff，(23)同时支付两个完整乘积的全角系数。

## 8. 接入同一最终圆，并保解析端点类别

先按 R280 固定两个布局、全部完整副本、最后五块位置的相对关系与正四次混合权。再选共同正则母包、据它选择两个真实 $\chi_t$，随后取足够大的最终正位置；所有选择都在真实根以前完成。

每个最后 block 上应用第7节，分别得到(23)。同 F 保住全部 self、真实三矩和有序面积，故五块的原正幅混合仍准确消全部72面积。完整第三由原八复制保持，十二复制给 odd 能量零，共振身份给其余两个已识别能量。整个同一圆遂满足

$$
\boxed{
\begin{gathered}
\text{全部72 Gaussian 面积}=0,\qquad
L_c=L_s=M_c=M_s=N_c=N_s=0,\\
[E_{-3}^2]\mathscr K_\theta=0,\qquad
[E_{-3}E_{-2}]\mathscr K_\theta=0
\quad\text{对全部 }\theta.
\end{gathered}}
\tag{24}
$$

正幅混合没有新原尾交叉：R286 的 local 式在完整合法 D 下成立，而各完整 block 的三矩本身都为零。它不要求单微包 primitive 紧支撑。

采用第2节的解析选择时，每个实际 prefactor 为

$$
P_0+\sum_\ell a_{t,\ell,N}(z)P_\ell
+zN^{-3}Q_t\cos Ny.
$$

预先固定的有限幅度盒中，有限纠正为 $O(N^{-1})$。所以同一个有限 N 可以同时满足第7节的真实根条件和全部实际 prefactor 的严格正性。R281 的解析端芽与有限端点 iff 因而适用于(24)的圆；该判据仍不是其尚未支付的 period/一次层方程自动为零。

## 9. 与 R285 上界的关系及未付范围

对于每一个固定 t，本稿只使用 R285 三十二维必要向量的一个七维投影。它的实际位置空间恰为六维，低于原至多十一维上界；第六坐标的完整依赖已由(16)明确写出。

两个不同 $\chi_t$ 改变的是真实主向量系数。原“固定母包、固定单一 $\chi$”的空间上界并不把两族绑成同一个超平面；本稿通过严格不同的(6)、全部真实六阶子式和正核，证明二族在这个特定子系统上合为七维。没有从维数上界反推任意基线可支付。

其余八个对称 Gaussian 乘积仍须保完整全角和 $C^2$ 余项逐个处理。零/一层 history、canonical period、同一个 gauge 的全路径联立、非线性收敛、闭嵌入、reach 与宏观幅度均不由(24)推出。本稿的新增结论是一个具体原完整乘积的真实支付，以及与单一 cutoff 共线性相容的明确双形状机制。

