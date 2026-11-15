# R258：三维补串 hook 的完整 Volterra 右逆、自伴四阶源与固定圆 period 接口

日期：2026-11-15。**完整纸面证明；没有新研究计算。** 本稿使用 R255 已证明的三个完整原算子 $\mathfrak J_0,\mathfrak J_1,\mathfrak J_2$，将其固定 seed 的 hook 写成一个局部自伴四阶算子的准确三次右积分。三个右端积分常数、左侧二次尾、全部混合历史项均保留。

新增的可消费接口包括：三条链的固定 f 正确递推、每条 K 项的准确总通量恒等式、两个完整混合目标及它们进入 R225 方程的真实源。在一个明确的逐包比例 profile 类上，三条链的 $K_f(g)$ 全部原式为零；对一般固定圆不作该假定。本文没有计算固定圆完整响应像的秩或宣布第四 joint 可解。

来源：[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md)、[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)、[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)。

## 1. 三维补串和真实右积分

记
$$
\mathcal J a(x)=\int_x^{r_*}a(\xi)\,d\xi,\qquad D=\frac{d}{dx},
\qquad D\mathcal J=-1.
\tag{1}
$$
所有 profiles 在共同右 collar 为零，左尾保留。$\mathcal J^m$ 是连续 m 次相同右积分，故
$$
\mathcal J^2 a(x)=\int_x^{r_*}(\xi-x)a(\xi)\,d\xi,\qquad
\mathcal J^3 a(x)=\frac12\int_x^{r_*}(\xi-x)^2a(\xi)\,d\xi.
\tag{2}
$$
不能把其中任何一次的积分常数独立重置。

沿 R255 的二次算子记号
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\ V=\Phi_{p_1},\ T=\Phi_{t_1},
$$
且 $C(A,B)(w;a,b)=A(w,B(a,b))-B(w,A(a,b))$。本稿的首个算子为
$$
\mathfrak J_0
=4C(L,R)-4C(L,S)-3C(P,T)+2C(R,U)+4C(S,U).
\tag{3}
$$
令
$$
Z=x^2D-2x,\qquad
\mathfrak J_1=\mathscr L_Z\mathfrak J_0,\quad
\mathfrak J_2=\mathscr L_Z^2\mathfrak J_0.
$$
R255 已给全部原 28 坐标、$\mathscr L_Z^3\mathfrak J_0=0$、三条完整真实独立及 $\Delta\mathfrak J_l=0$。

固定真实 f，定义
$$
K_f^l(w)=\mathfrak J_l(w;f,f),\qquad l=0,1,2.
\tag{4}
$$
f 在本稿的最终圆中保持固定；关于 f 的导数只用于准确的算子递推，不是另换一个物理圆的授权。

## 2. 首个 K 的完整 Volterra 式

记
$$
p=f',\qquad r=f'',\qquad t=f''',\qquad P_f=\mathcal J(r^2).
$$
由 R73 的完整二次式与 (3)，得到
$$
\boxed{
\begin{aligned}
K_f^0(w)={}&4wpr+2wP_f+2w'p^2-4w'fr\\
&+6\mathcal J(w''p^2)\\
&+\mathcal J^2\!\left[
w''(-4pr+4ft-2P_f)+6w'r^2\right]\\
&-2\mathcal J^3\!\left[w''(r^2+2pt)\right].
\end{aligned}}
\tag{5}
$$
特别是 $2wP_f$ 和第二行之后的全部尾项都在原式中。此式不要求 w 在 f 的支撑之外仿射或常数。

### 2.1 从五个完整 C 到原积分密度

先将查询点平移重标为零，并同时把右锚平移；这是 R255§2.3 已付的 $N\mathfrak J_0=0$ 坐标身份。对任意二次输出 b，原二次算子在此点给
$$
\begin{aligned}
L(w,b)(0)&=\tfrac12(wb'+w'b)(0)
+\tfrac14\mathcal J(x^2w''b''+2w'b')(0),\\
R(w,b)(0)&=w'b'(0),\\
S(w,b)(0)&=\mathcal J(xw''b'')(0),\\
P(w,b)(0)&=\mathcal J(w''b'')(0),\\
T(w,b)(0)&=0,\\
U(w,b)(0)&=\tfrac12\mathcal J(x^2w''b''+2w'b')(0).
\end{aligned}
\tag{6}
$$
将 (6) 代入 (3)，来自 $R(f,f)$ 的两组 J 密度准确互消。保留下来的局部值是
$$
4wpr+2wP_f+2w'p^2-4w'fr,
$$
原右积分密度是
$$
\begin{aligned}
&6p^2w''\\
&\quad+x\{(-4pr+4ft-2P_f)w''+6r^2w'\}\\
&\quad-x^2(r^2+2pt)w''.
\end{aligned}
\tag{7}
$$
这里使用的 $R(f,f)'',S(f,f)'',L(f,f)'',U(f,f)'',T(f,f)''$ 正是 R255(11)，没有丢去任何输入槽或累计项。

搬回任意物理查询点 x，(7) 中原积分变量的零点变成 $\xi-x$，右锚仍是实际 $r_*$。由 (2) 得 (5)。所以 (5) 对整个区间成立，原区间无需包含坐标零。

## 3. 三次导数准确消尾，得到自伴四阶算子

为了避免高阶导数排版歧义，下文明确写
$$
f^{(4)}=D^4f,\qquad f^{(5)}=D^5f.
$$
定义三个局部系数
$$
\begin{aligned}
a_f&=-4\{(f')^2+ff''\},\\
b_f&=12(f'')^2+8f'f'''-4f f^{(4)},\\
c_f&=8(f''')^2+12f''f^{(4)}+4f'f^{(5)}.
\end{aligned}
\tag{8}
$$
令
$$
\boxed{\mathscr A_f^0 w=D^2(a_fw'')+D(b_fw')+c_fw.}
\tag{9}
$$
这是实系数、形式自伴的四阶微分算子。完整身份是
$$
\boxed{D^3K_f^0(w)=\mathscr A_f^0w.}
\tag{10}
$$

### 3.1 逐项微分核对

将 (5) 写为
$$
K_f^0(w)=L_0+\mathcal JF_0+\mathcal J^2F_1-2\mathcal J^3G,
$$
其中
$$
\begin{aligned}
L_0&=(4pr+2P_f)w+(2p^2-4fr)w',\\
F_0&=6p^2w'',\\
F_1&=(-4pr+4ft-2P_f)w''+6r^2w',\\
G&=(r^2+2pt)w''.
\end{aligned}
$$
因为 $P_f'=-r^2$，三次微分准确得到
$$
D^3K_f^0=L_0'''-F_0''+F_1'+2G.
\tag{11}
$$
所有含 $P_f$ 的项相消。展开后的五个 w 系数为
$$
\begin{aligned}
\mathscr A_f^0w={}&-4(p^2+fr)w^{(4)}
-8(3pr+ft)w'''\\
&-8\{pt+f f^{(4)}\}w''\\
&+\{32rt+4p f^{(4)}-4f f^{(5)}\}w'\\
&+\{8t^2+12r f^{(4)}+4p f^{(5)}\}w.
\end{aligned}
\tag{12}
$$
(12) 的 $w'''$ 系数为 $2a_f'$，$w''$ 系数为 $a_f''+b_f$，$w'$ 系数为 $b_f'$；因此确为 (9)，而非只拥有相同最高项。

代 $w=f$，(12) 的每个三次 monomial 逐项相消：
$$
\boxed{\mathscr A_f^0f=0.}
\tag{13}
$$
这也与 R255 的 $K_f^0(f)=\Delta\mathfrak J_0(f)=0$ 相容。

### 3.2 必须支付的三个右端常数

原 (5) 在共同右 collar 恒零。因此原 K 不仅满足 (10)，还满足
$$
K_f^0(w)(r_*)=D K_f^0(w)(r_*)=D^2 K_f^0(w)(r_*)=0.
\tag{14}
$$
由三阶常系数积分的唯一性，
$$
\boxed{K_f^0=-\mathcal J^3\mathscr A_f^0.}
\tag{15}
$$
反过来，(15) 与 (10)、(14) 等价。若只记录 (10)，还可任意添加二次多项式，不能代替真实 K，更不能删除它在左平台的二次尾。

本式只是在固定 f 的 profile 算子上取完整右逆，不对几何 s 的历史重置，也不把 right collar 的三个零值扩成左端三个零值。

## 4. 三条链在固定 f 下的正确递推

对任意 seed 二次族 K，记 $D_fK[h]$ 为在 f 方向 h 的导数。完整三槽导子给
$$
\boxed{
K_f^{l+1}=ZK_f^l-K_f^l Z-D_fK_f^l[Zf].
}
\tag{16}
$$
不能省掉最后一项。它恰好来自两个内槽 f 同时受 Z 作用。

这是一个完全有限的代数接口：由于 K 关于 f 为二次，
$$
D_fK_f^l[h](w)=K_{f+h}^l(w)-K_f^l(w)-K_h^l(w).
\tag{17}
$$
(17) 只用于计算原式恒等，不宣称在最终几何/圆中改变 seed。

一个关键共轭身份是
$$
D^3Z=(x^2D+4x)D^3=-Z^*D^3,
\qquad Z^*=-x^2D-4x.
\tag{18}
$$
定义
$$
\boxed{
\mathscr A_f^{l+1}
=-Z^*\mathscr A_f^l-\mathscr A_f^l Z
-D_f\mathscr A_f^l[Zf].
}
\tag{19}
$$
从 (10)、(16)、(18) 得
$$
\boxed{
D^3K_f^l=\mathscr A_f^l,\qquad
K_f^l=-\mathcal J^3\mathscr A_f^l,\qquad l=0,1,2.
}
\tag{20}
$$
三个 K 均来自完整原算子并在同一右 collar 为零，故递推中的右三常数仍由原式支付。

(19) 中两个最高五阶 w 导数互消，所以每个 $\mathscr A_f^l$ 仍至多四阶。其系数是 x 与 f 的有限 jets 的多项式。更准确地，若
$\mathscr A=\sum_{j=0}^4 a_jD^j$，令 $a_5=0$，则
$$
\boxed{
a_j^{\rm new}
=x^2Da_j+(6-2j)xa_j-(j+1)(j-2)a_{j+1}
-D_fa_j[Zf].
}
\tag{21}
$$
由于
$$
D^m(Zf)=x^2f^{(m+1)}+(2m-2)x f^{(m)}
+m(m-3)f^{(m-1)},
$$
其中 $m=0$ 按原 $Zf$ 单独解释，(21) 中可能提高 f 最高 jet 的项互消。因此从 (8) 出发，三条链均无需超过 $f^{(5)}$。这给出无需旧 forcing/NF 的准确有限局部实现公式，而非新执行的研究计算。

若 $\mathscr A_f^l$ 自伴，则 (19) 的三个部分合起来仍自伴；取 f 导数也保持自伴。又对 $\mathscr A_f^lf=0$ 作 f 变分，
$$
(D_f\mathscr A_f^l[h])f+\mathscr A_f^lh=0.
$$
代 $h=Zf$ 并用 (19)，得到
$$
\boxed{
(\mathscr A_f^l)^*=\mathscr A_f^l,\qquad
\mathscr A_f^lf=0,\qquad l=0,1,2.
}
\tag{22}
$$
后两条递推并不是在固定 f 下只作 $[Z,K]$，也不把固定圆 period 商当作 sl2 商模。

## 5. 可直接读出的总通量与真实平台尾

### 5.1 K 项的准确总通量恒等式

对任意光滑 w，由 (20)、(22) 和三次分部积分，
$$
\boxed{
\int_I f'''K_f^l(w)
=-\int_I f\,\mathscr A_f^lw
=-\int_I w\,\mathscr A_f^lf=0,
\qquad l=0,1,2.
}
\tag{23}
$$
这里仅要求 f 在两个 collar 为零；w 可以保留真实左多项式尾，不要求 w 的左端迹为零。f 的全部相关端迹为零，故三次分部积分和自伴交换均没有边界漏项。这覆盖第 7 节的真实 $w=\Phi_E(D)$，而不把其左尾擅自删去。这里只对 K 项成立；完整第四响应的其余项在第 7 节保留。

### 5.2 三个右端常数决定全部二次尾

设一个开放区间 J 上 $\mathscr A_f^lw=0$。取该区间内一点 $c$，对 $x\in J$ 且 $x<c$，定义右侧真实矩
$$
m_j(c;f,w,l)=\int_c^{r_*}\xi^j\mathscr A_f^lw(\xi)\,d\xi,
\qquad j=0,1,2.
$$
若从 x 到 c 的源确为零，则 (20) 给
$$
\boxed{
K_f^l(w)(x)
=-\frac12m_2(c)+x\,m_1(c)-\frac{x^2}{2}m_0(c).
}
\tag{24}
$$
移动 c 而不跨过真实源不会改变三矩。每个平台必须用其自身右侧的积分；不能用一个共同的全局左尾替代所有内部平台。

特别地，在 f 恒定的开放区间，$\mathscr A_f^0=0$，所以 $K_f^0(w)$ 总是一个二次多项式，但一般并不为零，也不一定只是仿射。在 f 为零的开放区间，三个 $\mathscr A_f^l$ 的全部系数都为零，因此 (24) 对三条链都适用。对非零常值 f 平台及 $l=1,2$，应直接用 (19) 判断源；不把首条链的简化未经证明地扩给其余链。

(24) 的二次系数是一个确切的普通 profile 积分。对 f、w 的共同左零 collar，它给全部左二次尾；对每个内部平台，它保留相应真实右侧来源。与 R225 比较时，必须按完整目标自身的二阶导数判是否为零，不能只检查 K 的三阶导数。

## 6. 逐包比例类上的完整第三历史消失

本节给一个严格范围内的新简化。取有限个光滑 profiles $u_i$，其闭支撑两两不交，且在每个支撑边界全部 jets 为零。令
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,
\tag{25}
$$
其中 $a_i,b_i$ 为任意实数，允许 $a_i=0$。所有 profiles 仍位于共同合法区间，右 collar 固定。

**命题。** 对 (25)，三条链都满足完整函数身份
$$
\boxed{K_f^l(g)=0,\qquad l=0,1,2.}
\tag{26}
$$

**证明。** $\mathscr A_f^l$ 是局部算子，系数关于 f 的 jets 为二次。在 $a_i\ne0$ 的第 i 包，g 与 f 的全部 jets 满足 $g=(b_i/a_i)f$，且此比例为常数。因此由 (22)，
$\mathscr A_f^lg=(b_i/a_i)\mathscr A_f^lf=0$。
在 $a_i=0$ 的包及所有空隙，f 的全部 jets 为零，整个算子系数都为零，不论 g 是否非零。边界处光滑全平，没有分布项。所以 $\mathscr A_f^lg$ 在全 I 恒零；(20) 的同右三常数给 (26)。证毕。

这覆盖 R233/R235 那种整 profile 微包逐包成比例的构造；正交旋转 f、g 后，只改变每包的两个常系数，仍属 (25)。两个完整大 block 即使采用不同的比例轴对，组合后只要微包闭支撑不交，也仍满足本命题。

本命题不包括任意 f 常而 g 变化的重叠导数包，更不授任意固定圆的 $K_f^l(g)=0$。如果另要使用 R225 的完整解析 range 判据，还须验证所选圆满足该文的内部解析、有限退化及平台/端点前提，不能因 (26) 成立就自动继承另一圈的范围结论。

此外，(26) 不删去 $\Phi_A(f^2-\phi_\theta^2)$ 内的真实跨包尾。这些二次算子在不同微包之间仍有同右锚累计项；本节没有证明微包间第四响应可逐个相加。

## 7. 两个完整混合目标及进入 R225 的准确源

固定任意 f、g，令
$$
\phi_\theta=c f+s g,\qquad c=\cos\theta,\quad s=\sin\theta,
\qquad \zeta_l=K_f^l(g)=-\mathcal J^3(\mathscr A_f^lg).
\tag{27}
$$
对任一真实二次方向 $A\in E_8$，R255 的完整极化公式给
$$
\mathcal B_A(\mathfrak J_l)(f^2,\phi_\theta)
=s^2\mathcal D_{A,l}+cs\,\mathcal E_{A,l},
\tag{28}
$$
$$
\boxed{
\begin{aligned}
\mathcal D_{A,l}
&=2K_f^l\{\Phi_A(f^2-g^2)\}
+4\Phi_A(g,\zeta_l),\\
\mathcal E_{A,l}
&=-4K_f^l\{\Phi_A(fg)\}
+4\Phi_A(f,\zeta_l).
\end{aligned}}
\tag{29}
$$
两条历史项在一般圆中保留。新自伴表示把其全部输入降为已知局部算子与真实有限积分：
$$
\zeta_l'''=\mathscr A_f^lg,\qquad
\zeta_l(r_*)=\zeta_l'(r_*)=\zeta_l''(r_*)=0.
\tag{30}
$$
其余 K 项用同一局部源和相同右三常数计算。直接微分两次，得到 R225 所需的精确函数源：
$$
\boxed{
\begin{aligned}
\mathcal D_{A,l}''
&=-2\mathcal J\!\left[
\mathscr A_f^l\Phi_A(f^2-g^2)\right]
+4D^2\Phi_A(g,\zeta_l),\\
\mathcal E_{A,l}''
&=4\mathcal J\!\left[
\mathscr A_f^l\Phi_A(fg)\right]
+4D^2\Phi_A(f,\zeta_l).
\end{aligned}}
\tag{31}
$$
(31) 不重编 canonical 第四 forcing 或旧共享词表；全部右锚仍按原式给定。若需新实际评价，可直接消费 (8)、(19)、R73 的八个 $\Phi_A$ 和具体已合法化的 f、g。本文只给准确公式，尚未执行这些新评价。

由 (23)，完整目标的总通量分别为
$$
\boxed{
\begin{aligned}
\int_I f'''\mathcal D_{A,l}
&=4\int_I f'''\Phi_A(g,\zeta_l),\\
\int_I f'''\mathcal E_{A,l}
&=4\int_I f'''\Phi_A(f,\zeta_l).
\end{aligned}}
\tag{32}
$$
因此一般圆的通量问题没有从 K 项零通量自动消失。对第 6 节的逐包比例类，$\zeta_l=0$，才有两条完整目标的总通量均为零。即使如此，R225 的每个活动包通量、全部平台、内部 Laurent 条件和两端 germ 仍需分别支付；一个全区间总积分零不能代替它们。

## 8. 完整 period 像的必要充分比较和可构造右逆

本节采用 R225 的全部真实背景前提：同一合法固定圆、共同双 collar，$M=0$、$T=\kappa\mathfrak H$、$\kappa\ne0$，canonical pure 已零；f 活动区间属于其明确解析有限退化类。令该背景的两个完整真实 period 函数为
$$
V_\theta^0=s^2V_d+2cs\,V_e.
$$

### 8.1 三维补串的准确有限响应接口

对 24 个形式定义 $\mathcal B_{e_i}(\mathfrak J_l)$ 取实系数 $z_{i,l}$，令
$$
\begin{aligned}
\widehat V_d&=V_d+\sum_{i,l}z_{i,l}\mathcal D_{e_i,l},\\
\widehat V_e&=V_e+\frac12\sum_{i,l}z_{i,l}\mathcal E_{e_i,l}.
\end{aligned}
\tag{33}
$$
这里的 $1/2$ 来自原 $V_e$ 的 $2cs$ 规范，不能遗漏。要比较的完整 period 目标准确为
$$
G_c=-\frac{\widehat V_d}{4\kappa},\qquad
G_s=-\frac{\widehat V_e}{2\kappa}.
\tag{34}
$$
(29)–(31) 给 (33) 的全部函数源，不仅给某些点值或平台数。

24 是定义数，不是其真实秩。$z$ 是真实响应线性空间的坐标；这里不把任意符号组合自动当作同一个零基准实际控制词的成本。若要实际几何组装，仍须另用已付的有限控制及基准补偿接口。

### 8.2 对同一 z 施加完整四类条件

依 R225§7，(34) 能由同 collar 的 period gauge 支付，当且仅当同一个 z 使 $G_c,G_s$ 分别同时满足：

1. f 的每个常平台和 collar 上 $G''=0$，共同右 collar 还保原 $G=G'=0$；
2. 每个活动包 $[a_j,b_j]$ 的真实总通量
   $F_j(b_j;G)=\int_{a_j}^{b_j}f'G''=0$；
3. 对全部内部有限退化点，令
   $p=f'$、$A=6pp''-2(p')^2$，
   $q_j=F_j/(Ap^2)$。若 p 在该点为 n 阶零，则 $q_j$ 的 Laurent 系数在 $k\le-n-2$ 及 $k=-1$ 处必须为零；
4. 用同一个真实 $F_j$ 构造
   $u=p(C+\int q_j)$，两个平端都须具有真实 $C^\infty$ 延拓。不能擅自减去右端总通量，不能将这个条件换成有限若干 jets 或仅“目标全平”。

这些条件是完整原函数像判据。第 5–7 节的简化只给其中某些确切分量，不能替代剩下的条件，也不能用 24 定义数预报它们的同时可解性。

### 8.3 原右逆、六矩与 ruling 的顺序

四类条件成立后，R225 的构造逐包取
$$
u(x)=p(x)\left(C+\int
\frac{F_j(x;G)}{A(x)p(x)^2}\,dx\right),
$$
按原 Laurent 条件穿越内部点，在平端取真实光滑延拓；再在 f 常平台中连接并调整 $\int_Iu=0$，最后
$$
w(x)=\int_{r_*}^{x}u(t)\,dt.
\tag{35}
$$
真实右 collar 的两积分常数使 $L_f(w)=G$ 成为全函数身份，左侧仅保原允许的仿射尾，不另加左零目标。

本步骤的 $\mathcal X$ 与 R225 相同，只要求固定双 collar。R184(5) 的真实第三 range 定义域是逐相位的三矩几何函数核；六个交叉矩是一个足够强的子类，不应额外写成上面四类 period 像的必要条件。

在 R225 使用的同一固定合法圆前提下，再按其§7引用的 R185 固定六矩核投影修正 w：该修正留在 $L_f$ 的核内，保持已解完整 period，并令
$$
\mathbf m(f,w)=\mathbf m(g,w)=0.
\tag{36}
$$
两个解 $w_c,w_s$ 取同一固定右逆及该核投影，令
$$
w_\theta=(1-\cos2\theta)w_c+\sin2\theta\,w_s.
\tag{37}
$$
则它相位光滑、$2\pi$ 周期，$w_0=w_\pi=0$，并保持第三 range。该实际 w 对第四 ruling 的改变量仍按 R184/R221 的完整线性商公式计算；本稿没有证明同一 w 也使 ruling 商残差为零。

## 9. 与整个响应空间的关系

本稿给三维补串的完整固定 f 算子及双目标，因此把 R255 的三条新原定义变成无需旧 forcing 的可消费局部/Volterra接口。它没有代替全部
$$
\mathcal R_{\mathrm p0}
=(\mathcal R_{71}\cap\ker\pi)+\mathcal B(E,\operatorname{span}\chi_j).
$$
其中还有七维 hook 串、八个 $\chi_j$ 的完整 mixed 作用，以及不能只靠第三对角核穷尽的第四 pure 核方向。R225 的最终问题仍是整个真实 $O(U_{\mathrm p0})/O(\mathcal R_{\mathrm p0})$。

已完成的是 (5)、(9)–(24)、逐包比例类 (26)、全部双目标源 (29)–(32) 和准确像比较/右逆顺序。固定圆响应像的实际 rank、满射或严格 annihilator、真实带符号成本实现和同一个 w 的第四 ruling 联调都没有由这些公式自动推出。

作者责任：本文全部新推导为手写有限代数、真实同锚积分和常微分算子恒等式；没有在本地或公开 Actions 执行新研究目标。

## 10. 无新计算的整个 $Z_{71}$ 统一

前述局部自伴接口也完整覆盖旧七维 hook 串，而非只三条新方向。

记
$$
\mathfrak H=C(P,S)-3C(P,R),\qquad
K_f^{\mathfrak H}(w)=\mathfrak H(w;f,f)=L_f(w).
$$
R181/R225 的完整原式给
$$
L_f(w)''=\mathcal M_f(Dw),\qquad
\mathcal M_fu=D(A_HDu)-V_Hu,
$$
$$
A_H=6f'f'''-2(f'')^2,\qquad
V_H=6\{f''f'''\}',\qquad
\mathcal M_f(f')=0.
\tag{38}
$$
因此
$$
\boxed{
D^3K_f^{\mathfrak H}
=\mathscr A_f^{H,0}
=D\mathcal M_fD
=D^2(A_HD^2)-D(V_HD).
}
\tag{39}
$$
(39) 是完整局部自伴四阶算子，并且
$\mathscr A_f^{H,0}f=D\mathcal M_f(f')=0$。原 $L_f$ 在同一右 collar 恒零，三个右端常数都由原式付清，故
$$
K_f^{\mathfrak H}=-\mathcal J^3\mathscr A_f^{H,0}.
$$

对 $j=0,\ldots,5$ 递归定义
$$
\mathscr A_f^{H,j+1}
=-Z^*\mathscr A_f^{H,j}-\mathscr A_f^{H,j}Z
-D_f\mathscr A_f^{H,j}[Zf].
\tag{40}
$$
与第 4 节完全相同的证明给
$$
\boxed{
K_f^{\delta^j\mathfrak H}
=-\mathcal J^3\mathscr A_f^{H,j},\qquad
(\mathscr A_f^{H,j})^*=\mathscr A_f^{H,j},\qquad
\mathscr A_f^{H,j}f=0
\quad(0\le j\le6).
}
\tag{41}
$$
所有算子至多四阶，关于 f 的系数为二次局部多项式；(21) 的准确规则保持有限 jet 上界。这个结论没有恢复旧七条原根或运行新正规化。

由 R255 的真实分解 $Z_{71}=\mathfrak H_7\oplus\mathfrak J_3$，得到整个十维空间的统一定理：
$$
\boxed{
\forall\tau\in Z_{71},\quad
K_f^\tau=-\mathcal J^3\mathscr A_f^\tau,\qquad
(\mathscr A_f^\tau)^*=\mathscr A_f^\tau,\qquad
\mathscr A_f^\tau f=0,
}
\tag{42}
$$
其中 $\mathscr A_f^\tau$ 为明确线性组合的局部四阶算子。因而 (23) 的总通量恒等式及第 6 节的逐包比例消失对整个 $Z_{71}$ 成立：
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i
\quad\Longrightarrow\quad
K_f^\tau(g)=0\quad(\tau\in Z_{71}).
\tag{43}
$$

(43) 的前提是整 profile 支撑两两不交、每包两个输入为固定常比例，正是第 6 节、亦与 R250 的整 profile 分包类相同的范围。R225 的旧 step 型圆允许 f 变化而 g 在该处为非零常数，或 f 非零常值而 g 变化；这种包不满足 (25)，不能据旧 $\mathfrak H$ 对该圆的隐形性，推其全部 $\delta$ 链或 $\mathfrak J$ 链仍隐形。

对满足 (43) 的圆，$\mathcal B(E,Z_{71})$ 的全部响应都可在 (29) 中准确删去 $\zeta$ 项；两个完整目标的**总**通量均为零。下面进一步给出准确的逐整微包通量结论。这里覆盖的是第三对角核产生的响应，不是整个 $\mathcal R_{71}\cap\ker\pi$；八个 $\chi_j$ 的新 full K 也未由 (42) 推出。

### 10.1 逐整微包通量与 R225 活动区间

仍在 (43) 的范围内，置 $f_i=a_i u_i$。由于 $\mathscr A_f^\tau$ 的系数局部且二次依赖 f 的 jets，每个包内 $f=f_i$，其余包内 $f_i=0$，所有包界全平。因此
$$
\mathscr A_f^\tau f_i=0
\quad\hbox{在整个 I 上成立。}
\tag{44}
$$
对任意光滑 w，包括有真实左多项式尾的 $\Phi_E(D)$，有
$$
\boxed{
\int_I f_i'''K_f^\tau(w)
=-\int_I f_i\mathscr A_f^\tau w
=-\int_I w\mathscr A_f^\tau f_i=0.
}
\tag{45}
$$
这里的边界仍只由紧支全平 $f_i$ 支付。若 $I_i=(a_i^*,b_i^*)$ 是该整包的支撑内部，则 f 在 $I_i$ 等于 $f_i$，从而两次分部积分给
$$
\int_{I_i}f'(x)\{K_f^\tau(w)\}''(x)\,dx
=\int_{I_i}f_i'''(x)K_f^\tau(w)(x)\,dx=0.
\tag{46}
$$
当 $a_i=0$ 时同式平凡成立。由 (29) 在 $\zeta=0$ 下的完整表达，两个 mixed 响应目标分别都是这类 K 项，故 (46) 对它们逐整包成立。

若每个非零 $u_i$ 在支撑内部解析、没有内部开常平台，且只有有限个内部临界点，则整包就是 R225 的一个活动区间；有限临界点并不另开平台。因此这一子类中，(46) 恰支付 R225 在所有活动区间上的总通量门。它没有支付每个内部退化点的 Laurent 拼接、两个平端 germ、真实常平台上的二次尾，也没有支付同一 w 的第四 ruling。若包内部还有非零常平台，整包积分零不能替代拆开后各活动区间的通量条件。


