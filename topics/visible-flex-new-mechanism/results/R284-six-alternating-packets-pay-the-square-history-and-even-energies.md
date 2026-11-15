# R284：六个真实交替微包在同数据纤维中支付平方 history 与两个 even 能量

日期：2026-11-15。**有限参数的完整纸面建设性证明；没有执行新的求积、符号消元、profile 采样、人工检查或研究运行。**

[R282](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md) 提取了此前未付的完整 $E_{-3}^2$ 系数，并证明六能量与72面积不蕴含它。本稿在 [R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 的同一布局和有限数据纤维结构中，从一开始重新选择六个真实微包，联立支付

$$
H_0=H_1=H_2=L_c=M_c=0.
$$

全部72面积、真实三矩与完整第三条件保持；原 odd 包装和共振身份再给其余四个能量。因此存在一个实际有限光滑圆，同时支付此前全部条件与整个 $E_{-3}^2$ 系数。其余九个对称 Gaussian 乘积、零/一层 history、canonical period 和完整第四存在性仍没有由此证明。

来源：[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R279](R279-finite-frequency-fiber-control-pays-both-even-profile-energies.md)、R280 与 R282。

## 1. 本次联立的是五个真实量

使用 R277 的等平方背景方向

$$
b_i^2=B_0>0,\qquad
R_i=a_i^2-B_0\in\{-B_0/2,8B_0\},\qquad
\lambda_i=-a_i^2R_i.
$$

于是 high 包有 $\lambda_i=-72B_0^2<0$，low 包有
$\lambda_i=B_0^2/4>0$。各实际完整副本的共同 profile 幅度由其正四次权另行保留。

设 $u_i$ 为实际包，$r_i=u_i''$。本稿五个量采用

$$
\mathcal V=(-H_0,-H_1,-H_2,L_c,M_c).
\tag{1}
$$

其中 R282 的准确式为

$$
H_j=\sum_i a_i^2R_i\int x^j\{(r_i^2)'\}^2
\quad(j=0,1),
$$

$$
H_2=\sum_i a_i^2R_i\int x^2\{(r_i^2)'\}^2
+2\sum_iR_i^2\int r_i^4.
\tag{2}
$$

最后一项是保留全部原 $I_2$ 后的真实低阶基线，本稿不会删掉它。其余两量保持原 bulk：

$$
L_c=\sum_i\lambda_iS(u_i),\qquad
M_c=\sum_i\lambda_iT(u_i),
$$

$$
S(u)=\frac1{64}\int x^6\Psi_u^2(u''')^2,\qquad
T(u)=-\frac1{64}\int x^5\Psi_u\Theta_u(u''')^2,
$$

$$
\Psi_u=x^2u''-2xu'+2u,\qquad
\Theta_u=3x^2u''-5xu'+4u.
\tag{3}
$$

这些是原完整内槽三矩先消除总体边界后的准确式，不是用单包假紧的能量代替。若最后对多个完整 block 正幅相加，每项按实际四次权相加。

## 2. 不改变此前 Gaussian 数据的真实参数族

按 R277，$\mathcal F$ 是三个原二次矩和全部六 Gaussian pair、三外矩 self 的所有真实平移系数。它是 even $C^2$ Banach 空间上的有限多项式映射。选定光滑最大秩基点 $u_0$、固定有限纠正方向 $e_\ell$ 及一个非零 minor。

这里 $\mathcal F$ 确实保持

$$
C(u)=\int(u'')^4.
$$

准确来源不是额外增添一个观测：R267 的真实单包 Green 表给
$S_{\mathcal P,\Phi_{p_0},0}=C/6$、
$S_{\mathcal P,\Phi_{s_1},0}=7C/6$，
故原 $S_{B_{-1},B_{-3},0}=-c(d_-+7e_-)C/6$。
在当前非零共振 $\kappa$ 上，
$c\ne0$、$d_-+7e_-=-\kappa(81\kappa^2+7)/(4h_e)\ne0$。
所以(2)的低阶项在本次纤维中准确固定。

选共同 even cutoff $\chi$，使

$$
K_\chi=\int(u_0'')^2\chi^2>0.
\tag{4}
$$

R279 已给真实有限 IFT 族

$$
u_N(z,y)=u_0(y)+zN^{-3}\chi(y)\cos(Ny)
+\sum_\ell a_\ell(z,N)e_\ell(y),
\tag{5}
$$

满足

$$
\mathcal F(u_N(z))=\mathcal F(u_0)
\tag{6}
$$

及在每个先固定的有限正幅盒上一致的

$$
\|u_N-u_0\|_{C^2}+\|\partial_z u_N\|_{C^2}=O(N^{-1}),
$$

$$
u_N'''=u_0'''+z\chi\sin Ny+O(N^{-1}),\qquad
\partial_z u_N'''=\chi\sin Ny+O(N^{-1}).
\tag{7}
$$

(7)的最后余项在 $C^0$ 中对参数及其一阶导数一致成立。所有 $e_\ell$ 是固定光滑函数，故有限纠正的三阶导确实为 $O(N^{-1})$；没有把一般 $C^2$ 小扰动错误地当作 $C^3$ 小扰动。

每个被选基本包使用自己的 z；在该包的全部八/十二完整副本中复制同一个 $u_N(z)$。所以全部72 Gaussian self、真实有序跨包矩及完整第三构造，在整个参数盒内准确保持，而不只在最终根保持。

## 3. 六个需要的真实交替位置已经存在

R280 的两个布局均可从一开始将17进制数位和的0类选为 high。在基本17进制层中，索引

$$
0,\ 1,\ 33,\ 34,\ 49,\ 50
\tag{8}
$$

依次为 high、low、high、low、high、low：
$33=1\cdot17+16$、$49=2\cdot17+15$ 的数位和均为17，其后两个 low 的数位和分别为2、18。

在正布局 $i=kL+j$ 中取 $k=0$；在负布局 $i=jK+k$ 中取 $k=0$。两者都给六个严格递增的真实位置

$$
t_1<\cdots<t_6
$$

及交替系数

$$
\lambda_1<0,\ \lambda_2>0,\ \lambda_3<0,\
\lambda_4>0,\ \lambda_5<0,\ \lambda_6>0.
\tag{9}
$$

没有将形式次序翻转当成物理反射，也没有新增一类不可实现的方向。格距和全部包宽按 R280 原规则一次选到支持严格不交。正负面积模板的其他基本包仍保留 $u_0$。

这些只是允许的构造参数选择；本稿不是把一个已经固定的旧数值圆的 high 类和位置重新移动。

## 4. 保全部副本后的五个 principal 多项式

记一个完整 block 的全部真实副本偏移和正四次权为

$$
d_\nu,\quad \omega_\nu=\gamma_\nu^4,\qquad
W=\sum_\nu\omega_\nu>0.
$$

第 i 个基本包及其副本位于 $X+t_i+d_\nu$。令 $r_0=u_0''$。定义原五量的高频 principal 函数：

$$
P_j(X)=2\sum_\nu\omega_\nu
\int(X+d_\nu+y)^j r_0(y)^2\chi(y)^2\,dy,
\qquad j=0,1,2,
\tag{10}
$$

$$
\mathcal S(X)=\frac1{128}\sum_\nu\omega_\nu
\int (X+d_\nu+y)^6
\Psi_{X+d_\nu,u_0}(y)^2\chi(y)^2\,dy,
$$

$$
\mathcal T(X)=-\frac1{128}\sum_\nu\omega_\nu
\int (X+d_\nu+y)^5
\Psi_{X+d_\nu,u_0}(y)\Theta_{X+d_\nu,u_0}(y)
\chi(y)^2\,dy.
\tag{11}
$$

$\Psi_{\xi,u_0}$ 表示在原(3)中取 $x=\xi+y$，profile 值仍为 $u_0(y)$；$\Theta$ 同理。系数 $1/128$ 是原 $1/64$ 乘 $\sin^2 Ny$ 的准确弱平均 $1/2$，不把它再乘一次。

设

$$
k_0=2WK_\chi>0,\qquad s_0=\frac{WK_\chi}{128}>0,
$$

$$
\mu_\ell=\frac1{WK_\chi}
\sum_\nu\omega_\nu\int(d_\nu+y)^\ell r_0^2\chi^2.
$$

则(10)是准确三角多项式

$$
P_0=k_0,\quad P_1=k_0(X+\mu_1),\quad
P_2=k_0(X^2+2\mu_1X+\mu_2).
\tag{12}
$$

同时

$$
\mathcal S(X)=s_0X^{10}+\text{次数至多9的真实多项式},
$$

$$
\mathcal T(X)=-3s_0X^9+\text{次数至多8的真实多项式}.
\tag{13}
$$

全部偏移、形状和副本权都在这些多项式里。没有把各副本移到共同理想点，也没有假设其高阶位置矩为零。

令

$$
v(X)=(P_0(X),P_1(X),P_2(X),\mathcal S(X),\mathcal T(X))^T.
\tag{14}
$$

真实五量的有限频率映射将在下一节写为
$b+\sum_i z_i^2\lambda_i v(X+t_i)$ 的 $C^1$ 逼近。这里前三个正 principal 与(1)采用负 H 的符号完全一致，因为 $\lambda_i=-a_i^2R_i$。

## 5. 所有五列子式的共同严格符号

对(14)作固定可逆行变换，前三行由(12)化成
$1,X,X^2$；将第四、第五行交换并缩放后化成

$$
q_9(X)=-\mathcal T(X)/(3s_0),\qquad
q_{10}(X)=\mathcal S(X)/s_0.
$$

所以只需研究五行

$$
1,\ X,\ X^2,\ q_9(X),\ q_{10}(X),
\tag{15}
$$

其中 $q_9,q_{10}$ 是来自原几何的真正 monic 九、十次多项式，低次系数固定，不能独立指定。

取任意五个固定递增位置 $\tau_1<\cdots<\tau_5$。在共同正位置 X 展开，先将高两行的零、一、二次 Taylor 项用前三行消去。三、四次项的行列式首系数是

$$
\binom93\binom{10}4-\binom94\binom{10}3
=84\cdot210-126\cdot120=2520.
$$

因此

$$
\boxed{
\det\begin{pmatrix}
1&\cdots&1\\
X+\tau_1&\cdots&X+\tau_5\\
(X+\tau_1)^2&\cdots&(X+\tau_5)^2\\
q_9(X+\tau_1)&\cdots&q_9(X+\tau_5)\\
q_{10}(X+\tau_1)&\cdots&q_{10}(X+\tau_5)
\end{pmatrix}
=
2520X^{12}\prod_{i<j}(\tau_j-\tau_i)+O(X^{11}).
}
\tag{16}
$$

高两行中任何低次系数或更高 Taylor 幂，都只进入 $O(X^{11})$。这是有限多项式的首项论证，不是浮点主项支配猜测。

六个实际位置 $t_i$ 只有六个删列子式。故一次选择足够大的**有限** X，可使(15)在这六列上的全部五列子式严格为正。原(14)的相应子式只共同乘一个固定非零行变换因子，因此同号、全非零。

本稿只用这个有限位置结论，不需要宣称在任意先冻结的窄区间中都有相同的 Chebyshev 性质。若需要更大的 X，必须在最终求解和安装前选择；不搬动已经得到的旧能量零解。

## 6. 六条带真实符号的 principal 向量正锥为全空间

记归一后的五乘六矩阵为
$V=(v_1,\ldots,v_6)$，其中 $v_i$ 是(15)在 $X+t_i$ 的列。
令 $D_i>0$ 为删去第 i 列的五阶行列式。
cofactor 身份给

$$
\sum_{i=1}^6(-1)^{i+1}D_i v_i=0.
\tag{17}
$$

由于(9)的 $\lambda_i$ 符号恰为 $(-1)^i$，

$$
w_i=\frac{D_i}{|\lambda_i|}>0
\quad\Longrightarrow\quad
\sum_iw_i\lambda_i v_i=0.
\tag{18}
$$

固定可逆行变换不会改变这个正核。故对原五量使用的六条向量
$\lambda_i v(X+t_i)$，也有同一个严格正 balance，且任意五列线性独立。

于是它们的非负锥等于 $\mathbb R^5$。证明不是将成本任意指定：对任意给定的有限基线 b，先由秩5取一个实向量 $\eta$ 解

$$
b+\sum_i\eta_i\lambda_i v(X+t_i)=0.
$$

再加一个充分大的有限正倍数的(18)，得到全部严格正的 $w_i^*$，保持同一等式。置

$$
z_i^*=\sqrt{w_i^*}>0.
\tag{19}
$$

这里曾出现的实线性解 $\eta$ 不是实际负包或负能量；真正进入 profile 的仅是最后的严格正有限幅度(19)。

## 7. 五个完整量的 $C^1$ 收敛与有限频率根

固定最终布局、X、全部副本，以及包含 $\mathbf z^*$ 的一个有限严格正幅度盒。令 b 是所有基本包均为 $u_0$ 时的完整五量(1)，**包含** $H_2$ 的 $2\sum R_i^2C_i$ 及所有未选微包的原值。

分别将六个已选包替换为(5)，其余包不变。记由真实 profile、原同锚公式得到的完整映射为 $\mathcal V_N(\mathbf z)$。

由(6)，$C_i$ 与全部低阶 Gaussian 数据逐参数准确不变。由(7)，三个 H 的高阶部分是固定 $C^2$ 系数乘 $(u_N''')^2$；(3)亦然。逐项展开、消去 $\sin Ny$ 与 $\cos2Ny$ 的振荡积分，得到

$$
\boxed{
\mathcal V_N(\mathbf z)
\longrightarrow
\mathcal V_\infty(\mathbf z)
=b+\sum_{i=1}^6z_i^2\lambda_i v(X+t_i)
\quad\text{在该固定幅度盒上一致 }C^1.
}
\tag{20}
$$

这里可逐项沿用 R279 的原证明：

- 真实 profile 的 $C^2$ 系数与其参数导数相对基点为 $O(N^{-1})$；
- 三阶导的固定光滑纠正与其参数导数亦为 $O(N^{-1})$；
- 主振荡平方给(10)—(11)，线性交叉振荡积分一致趋零；
- 对 z 微分后仍是同样的固定可积系数与有限振荡和，故导数也一致收敛。

不需要对 $\mathcal F$ 提出新的高阶观测，不需要令一个实际 profile 的 N 无穷大。所有常数允许依赖已经固定的有限 X、原副本数、幅度盒及其有限逆矩阵。

由(19)，$\mathcal V_\infty(\mathbf z^*)=0$。固定 $z_6=z_6^*$，其余五变量的 Jacobian 是

$$
J_*=
\bigl(2z_1^*\lambda_1v(X+t_1),\ldots,
2z_5^*\lambda_5v(X+t_5)\bigr).
\tag{21}
$$

(16)及严格正 $z_i^*$ 使其可逆。有限维 $C^1$ 稳定性或收缩形式的隐函数定理遂给：对一个充分大的**有限整数** N，存在附近的真实正幅度 $\mathbf z_N$，准确满足

$$
\boxed{
H_0=H_1=H_2=L_c=M_c=0.
}
\tag{22}
$$

该步骤使用的是真实完整 $\mathcal V_N$，不是只将(20)的 principal 代回旧函数。它没有删掉 $H_2$ 的低阶项，也不以实际数值残差近零代替(22)。

## 8. 接入五个最后完整 block 的同一真实圆

在 R280 中先固定两个格点模板、全部八/十二副本、五个最后相对中心及正幅权。这些幅权由三个有序面积的准确正平衡确定。

随后一次增大共同正 X，使第5节的六个子式对五个最后 block 全部成立。每个 block 只有有限的相对位置和副本数据，所以这样的共同有限 X 存在。原五块面积零在这个共同平移下仍准确保持；这是原三个矩面积的三角变换，不是对旧能量解事后搬动。

在五个已经固定的最终位置上，分别应用第7节的有限频率根。每个真实微包都保原 $\mathcal F$，因此：

- 全部72 Gaussian 面积及最后五块正权准确保持；
- 每个基本 pair 的真实三矩不变，完整八复制的四槽第三 ruling 与原 hook 周期条件不变；
- 每个最后 block 都有(22)，故它们的正四次幅混合保持全部三个 H 与 $L_c,M_c$；
- 原十二完整副本给 $L_s=M_s=0$，共振身份 $N_c=6M_c$、$N_s=6M_s$ 给其余两个能量；
- 原 $I_0$ 值固定，可以作共同正归一化；所有齐次零保持，圆非退化。

按 R282 的准确 iff，最后同一个实际圆满足

$$
\boxed{
\text{全部72 Gaussian 面积}=0,\quad
L_c=L_s=M_c=M_s=N_c=N_s=0,\quad
[E_{-3}^2]\mathscr K_\theta=0\quad\text{全部 }\theta.
}
\tag{23}
$$

(23)没有消费任何预先存在的几何数值状态。它是新 seed/目标按原 profile 构造共同选择的有限光滑存在定理。

## 9. 选择次序与未付范围

准确顺序是：先选有限数据纤维的真实母包与控制方向、两个有限编码和全部相对布局；再选足够大的共同正位置及合法有限 I；再解有限 principal 正平衡，固定有限幅度盒；最后选足够大的有限 N，解真实五变量系统。每一步只依赖先前已经固定的有限数据，不交换“固定后再任意放大”的次序。

本稿不要求已经冻结的任意母包具有所需最大秩。可从一开始采用 [R281](R281-analytic-packet-fibers-and-finite-canonical-end-germ-conditions.md) 的同一解析选择：$u_0=\psi P_0$、$e_\ell=\psi P_\ell$、$\chi=\psi Q$，其中 $P_0$ 在闭母支撑上严格为正。对第7节已经固定的有限正幅度盒，实际扰动的 prefactor 为

$$
P_0+\sum_\ell a_\ell(z,N)P_\ell+zN^{-3}Q\cos(Ny).
$$

有限纠正及其参数导数为 $O(N^{-1})$，故把同一个有限 N 再取足够大，就同时保持五变量真实根所需的 $C^1$ 逼近与该 prefactor 在全闭支撑上的严格正性。有限个 block 可以一并满足这些有限下界，无需增加方程。因此 R281 的实际解析端芽及 canonical 零端有限 iff 同样适用于本稿存在的圆；这只是明确端点判据的适用类别，并没有宣称其尚待支付的 period/一次层条件已经为零。不能将此结论改写成任意旧 $C^\infty$ 根自动具有解析结构。

其余九个对称乘积的完整外矩尚须据 R282(7)—(8)分别处理。零/一层 history、canonical 第四 period、全路径 gauge 联立、后续非线性收敛、闭嵌入与 reach/宏观幅度也未由(23)推出。本稿的新支付仅是一个原来确实独立的完整平方 history；它不把五维 principal 正锥当成所有第四条件的自由控制器。

