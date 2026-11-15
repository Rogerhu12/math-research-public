# R250：完整圆的 Gaussian 面积系数、十个标量条件与非均匀微包零例

日期：2026-11-15。**完整纸面证明；没有执行新的 profile 积分、符号目标、函数秩、求根或几何研究计算。**

本稿从 R73 的完整三槽恢复提取 $A_{-2,-3}$ 在整个 $\theta$ 圆中的系数，覆盖零次、二次及四次谐波。结论比 R249 的 pure 第四谐波条件更强，但并不普遍排除所有合法三阶圆：本文给出一个准确消去此面积的非均匀微包构造，并按已有 R183 构造支付完整三阶。**这个构造同时严格违反 R231 的 $L_c=0$，因此不是完整第四 ruling 的候选。** 单面积可解与其他已知必要门失败在本文中分开证明。

来源：[R56 完整分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 点态八矩及完整第三桥](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183 导数分包与完整三阶圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R224 真前缀与偶部商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R231 完整 mixed 领先门](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、[R238 真实尾与局部 bulk](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md)、[R241 共振芽及联合安装](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)、[R245 全部 Gaussian history](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R248 完整第四谐波规范](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)和 [R249 真实词独立及 pure 障碍](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)。

## 1. 同一真实端芽、圆与右锚

取 R241/R249 的共振例外芽

$$
\kappa\ne0,\qquad h_e>0,\qquad
\varepsilon=\kappa^2/4,\qquad H=e^{\varepsilon\sigma^2},
$$

$$
h=h_eH,\qquad
k=\kappa(1-2\varepsilon\sigma^2),\qquad
\omega=\kappa/h,\qquad
j=2\varepsilon\kappa\sigma^2.
\tag{1}
$$

保持原共同合法区间 $I=[\ell,r]$、真实物理支及双零 collar。需要正 bulk 时取已有构造允许的 $\ell>0$。本稿不把实际闭几何延长到整个实轴；(1) 的解析模型只用于同一 germ 的函数身份。

所有 profile 原函数均为

$$
J(a)(x)=\int_x^r a(\xi)\,d\xi,\qquad J(a)'=-a.
$$

令实 $f,g\in C_c^\infty(I^\circ)$ 满足三矩圆条件

$$
\mathbf m(f,f)=\mathbf m(g,g),\qquad
\mathbf m(f,g)=0,
\tag{2}
$$

其中

$$
\mathbf m(u,v)=
\left(
\int_Iu''v'',\
\int_Ixu''v'',\
\int_I(x^2u''v''+2u'v')
\right).
$$

置

$$
\phi_\theta=c_\theta f+s_\theta g,\qquad
c_\theta=\cos\theta,\quad s_\theta=\sin\theta,
$$

$$
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{3}
$$

$\odot$ 表示对称双线性算子槽，不是先取点态平方再求四次导数。以后特别写

$$
D_\theta^{[2,2]}=(f'')^2-(\phi_\theta'')^2.
\tag{4}
$$

完整二、三阶场按 R248 的同一 canonical 起点恢复：

$$
Z_\theta=Z(D_\theta),\qquad
W_\theta=-2C(\phi_\theta;D_\theta).
$$

因此整个第四 ruling 原式为

$$
\mathscr K_\theta
=-\mathfrak b_\sigma(Z(D_\theta),Z(D_\theta))
+4\mathfrak b_\sigma(Y_{\phi_\theta},C(\phi_\theta;D_\theta)).
\tag{5}
$$

这里 $\mathfrak b_\sigma$ 是 R56/R248 的真实分子配对。带左尾的分解项仍保留原尾；不把这些分解项各自宣称为合法完整场。

## 2. 从完整三槽历史取得唯一面积来源

采用

$$
\mathcal P(u,v)=J(u''v''),\qquad
\mathcal R(u,v)=u'v'+xJ(u''v''),\qquad
\mathcal S(u,v)=J(\xi u''v''),
$$

$$
[\mathcal A,\mathcal B](a;b,c)
=\mathcal A(a,\mathcal B(b,c))
-\mathcal B(a,\mathcal A(b,c)),
$$

$$
\mathfrak H=[\mathcal P,\mathcal S]-3[\mathcal P,\mathcal R].
\tag{6}
$$

R249 已从 R73 的原 raw 矩阵（含全部 $h_s,k_s$ 项）给出

$$
B_{-2}=a_*\mathcal R+b_*\mathcal S,\qquad
B_{-3}=c_*\mathcal P,
\tag{7}
$$

$$
a_*=-\frac{51\kappa^4+2\kappa^2+8}{64h_e^2},\qquad
b_*=-\frac{17\kappa^4+4\kappa^2}{32h_e^2},\qquad
c_*=-\frac{\kappa(41\kappa^4+27)}{216h_e^3}.
$$

特别

$$
a_*+3b_*=-\frac{153\kappa^4+26\kappa^2+8}{64h_e^2},
\qquad c_*(a_*+3b_*)\ne0.
\tag{8}
$$

仍取真实共同中心原函数

$$
E_r(\sigma)=\int_0^\sigma H(t)^r\,dt,\qquad
K_{r,s}(\sigma)=\int_0^\sigma H(t)^rE_s(t)\,dt,
$$

$$
A_{r,s}=K_{r,s}-K_{s,r},\qquad
K_{r,s}=\frac{E_rE_s+A_{r,s}}2.
\tag{9}
$$

本稿指定 $A_{-2,-3}=K_{-2,-3}-K_{-3,-2}$ 的方向。

R73 的全三槽方程为

$$
(W_C)'=
\ell_\sigma(a;D)
-\Phi_{\mathsf M(\sigma)}(a,\Phi_{\mathsf m(\sigma)}D)
-\Psi_\sigma(a,\Phi_{\mathsf M(\sigma)}D).
\tag{10}
$$

R245/R249 的 history 分类在 (10) 中逐槽成立，未使用 $a=b=c$：

- 第二局部场与 $Y_{\Phi_{\mathsf m}D}$ 的平方只产生 $E_rE_s$ 等对称积；
- 第三局部恢复至多含单个累计第二 history；
- $\ell-\Psi$ 无累计 $\mathsf m$，其积分为已证明的初等或单 history 项；
- 涉及奇 Laurent 部分 $Q_\sigma$ 的项，经同锚分部积分只给初等项和单个 $E_r$，真实积分常数保留。

于是全部二重词项恰为

$$
(W_C)_{\mathrm{two}}
=-\sum_{r,s}K_{r,s}B_r(a,B_s(D)).
\tag{11}
$$

$A_{r,s}$ 在 $W_C$ 中的系数是
$-[B_r,B_s](a;D)/2$。因 (5) 中 $C=K_C-Y_{W_C}$，完整圆的面积系数为

$$
\boxed{
\mathscr A_\theta
=2\mathcal E_\sigma\!
\left(\phi_\theta,[B_{-2},B_{-3}](\phi_\theta;D_\theta)\right),
}
\qquad
\mathcal E_\sigma(u,v)=\mathfrak b_\sigma(Y_u,Y_v).
\tag{12}
$$

这是 (5) 的完整系数，符号为正 $2$。R249 pure 齐次四次算子的相应符号为负 $2$；二者的差别正来自 $D_\theta=f\odot f-\phi_\theta\odot\phi_\theta$，不能混用。

R249 已证明 $1,E_r,E_rE_s,A_{r,s}$ 是
$\mathbb R(\sigma,H)$ 上的真实独立基，而不是冗余形式生成元。原偶部三矩空间

$$
\mathcal W_e=
\operatorname{span}_{\mathbb R}
\{h,\sigma^2,(1+4\varepsilon^2\kappa^2\sigma^4)/h\}
\subset\mathbb R(\sigma,H)
$$

没有面积词。因此完整第四 ruling 存在时，(12) 必须对整个 $\sigma$ germ 和全部 $\theta$ 为零。R224/R231 的真实前缀比较、允许的二阶 homogeneous gauge 和第三 homogeneous gauge，只改变同一个 $\mathcal W_e$ 内的偶函数；不改变这个必要面积条件。所有负 Gaussian 的原常数尾仍在 (9) 中。

## 3. 不能用纯对角代替的全槽交换子

直接对内层求导：

$$
\mathcal S(b,c)''
=-b''c''-x(b'''c''+b''c'''),\qquad
\mathcal P(b,c)''
=-(b'''c''+b''c''').
$$

故同一右锚下准确有

$$
\boxed{
[\mathcal P,\mathcal S](a;b,c)
=-J(a''b''c'').
}
\tag{13}
$$

右边全对称；左尾不被删除。由 (6)，

$$
[\mathcal P,\mathcal R]
=-\frac13\{J(a''b''c'' )+\mathfrak H(a;b,c)\}.
$$

代入 (7) 得完整三槽身份

$$
\boxed{
[B_{-2},B_{-3}](a;b,c)
=\frac{c_*}{3}
\left[
(a_*+3b_*)J(a''b''c'')
+a_*\mathfrak H(a;b,c)
\right].
}
\tag{14}
$$

所以在尚未使用第三阶周期条件前，(12) 是

$$
\boxed{
\mathscr A_\theta
=\frac{2c_*}{3}
\left[
(a_*+3b_*)\mathcal E_\sigma
\left(\phi_\theta,J(\phi_\theta''D_\theta^{[2,2]})\right)
+a_*\mathcal E_\sigma
\left(\phi_\theta,\mathfrak H(\phi_\theta;D_\theta)\right)
\right].
}
\tag{15}
$$

这一步明确保留了纯对角 $\mathfrak H(q;q,q)=0$ 无法判定的外槽。

现在限定本课题已经实现的几何类

$$
M=0,\qquad T=\kappa_H\mathfrak H,\qquad \kappa_H\ne0,
\tag{16}
$$

其中 $\kappa_H$ 是整路径第三算子的系数，与 (1) 的 $\kappa$ 不混同。对固定种子 f 的合法第三阶圆，第三 period 必须给

$$
\mathfrak H(\phi_\theta;D_\theta)=0.
\tag{17}
$$

独立二阶 homogeneous gauge 对这一第三 period 的变化是 $M$ 项；在 (16) 中为零，所以不能取消 (17)。

由对角 hook 恒等式，

$$
\mathfrak H(\phi_\theta;D_\theta)
=\mathfrak H(\phi_\theta;f,f)
=s_\theta\,\mathfrak H(g;f,f).
\tag{18}
$$

因此一般固定种子圆只需要这里的
$\mathfrak H(g;f,f)=0$；不能据此再断言
$\mathfrak H(f;g,g)=0$ 或全部三槽均零。R183 的导数分包类另行满足全部三槽零，属于更强的特例。

在准确范围 (16)—(17) 中，完整面积条件缩为

$$
\boxed{
\mathscr A_\theta
=\frac{2c_*(a_*+3b_*)}{3}\,
\mathcal E_\sigma(\phi_\theta,t_\theta),
\qquad
t_\theta=J\!\left[\phi_\theta''
\big((f'')^2-(\phi_\theta'')^2\big)\right].
}
\tag{19}
$$

## 4. 三个真实矩：完整左尾仍在

写

$$
F=f'',\quad G=g'',\quad
R_\theta=c_\theta F+s_\theta G,\quad
P_\theta=c_\theta f'+s_\theta g'.
$$

则

$$
t_\theta'=-R_\theta F^2+R_\theta^3,\qquad
t_\theta''=-R_\theta'F^2-2R_\theta FF'
+3R_\theta^2R_\theta'.
\tag{20}
$$

$t_\theta$ 一般有非零左常尾。本节只利用外槽 $\phi_\theta$ 及其导数在两 collar 为零。

定义真正的全区间矩

$$
m_0(\theta)=\int_I R_\theta t_\theta'',\quad
m_1(\theta)=\int_I xR_\theta t_\theta'',\quad
m_2^*(\theta)=\int_I(x^2R_\theta t_\theta''+2P_\theta t_\theta').
$$

一次分部积分逐项给

$$
\boxed{m_0=-\int_I R_\theta^2FF',}
\tag{21}
$$

$$
\boxed{
m_1=\frac12\int_I R_\theta^2F^2
-\frac34\int_I R_\theta^4
-\int_I xR_\theta^2FF',
}
\tag{22}
$$

$$
\boxed{\begin{aligned}
m_2^*={}&\int_I xR_\theta^2F^2
-\frac32\int_I xR_\theta^4
-\int_I x^2R_\theta^2FF'\\
&-2\int_I P_\theta R_\theta F^2
+2\int_I P_\theta R_\theta^3.
\end{aligned}}
\tag{23}
$$

例如 (21) 用
$\int RR'F^2=-\int R^2FF'$ 及
$\int R^3R'=0$；边界均由外槽导数的紧性支付。没有为 $t_\theta$ 强加左零值。

R56 的分子配对对一个紧外槽仍给

$$
\mathcal E_\sigma(\phi_\theta,t_\theta)
=\frac{1+j^2}{4h}m_0(\theta)
+\frac j2m_1(\theta)
+\frac h4m_2^*(\theta).
\tag{24}
$$

乘 $4h$ 后是

$$
(1+j^2)m_0+2jh_eH\,m_1+h_e^2H^2m_2^*.
$$

$H$ 对 $\mathbb R(\sigma)$ 超越，且 $j$ 非零，所以对固定 $\theta$，
(24) 恒零当且仅当三个真实矩全零。结合 (8)、(19)，得到

$$
\boxed{
\mathscr A_\theta\equiv0\quad\text{对全部 }\sigma,\theta
\quad\Longleftrightarrow\quad
m_0(\theta)=m_1(\theta)=m_2^*(\theta)=0
\quad\text{对全部 }\theta.
}
\tag{25}
$$

这是整个指定面积的充要条件，不是完整第四 ruling 的充要条件。式 (21)—(23) 只有零、二、四次角谐波；它们在 $\theta=0,\pi$ 自动为零。

## 5. 全角条件等价于十个明确标量等式

以下给出一个无需 theta 采样的有限重述；不声称这十个函数约束在任意 profile 点的微分秩为十。

先记

$$
A_4=\int F^4,\quad B_4=\int F^3G,\quad
C_4=\int F^2G^2,\quad D_4=\int FG^3,\quad E_4=\int G^4,
$$

$$
U=\int xF^2GF',\qquad V=\int xFG^2F'.
$$

由 (21)，$m_0$ 全角零准确等价于

$$
\boxed{\int F^2GF'=0,\qquad \int FG^2F'=0.}
\tag{26}
$$

将 (22) 用 $c^2+s^2=1$ 齐次化为四次式。$c^4$ 系数自动为零，其余四个系数依次为

$$
-2(B_4+U),\quad
\frac34A_4-4C_4-V,\quad
B_4-2U-3D_4,\quad
\frac12C_4-V-\frac34E_4.
$$

因此

$$
\boxed{
U=-B_4,\qquad D_4=B_4,\qquad
A_4+E_4=6C_4,\qquad
V=\frac{2C_4-3E_4}{4}.
}
\tag{27}
$$

为写 (23)，置 $p=f',q=g'$，定义

$$
L_0=\frac32\int xF^4-2\int pF^3,
$$

$$
L_1=2\int xF^3G-2\int x^2F^2GF'
-2\int(pG+qF)F^2,
$$

$$
L_2=\int xF^2G^2-\int x^2FG^2F'
-2\int qGF^2.
$$

以真实四次多项式定义 $Q_0,\ldots,Q_4$：

$$
\frac32\int x(cF+sG)^4
-2\int(cp+sq)(cF+sG)^3
=\sum_{\nu=0}^4Q_\nu c^{4-\nu}s^\nu.
\tag{28}
$$

其中 $Q_0=L_0$。式 (23) 恰是
$L_0c^2+L_1cs+L_2s^2-\sum Q_\nu c^{4-\nu}s^\nu$，
所以余下四个条件为

$$
\boxed{
L_1=Q_1,\qquad L_0+L_2=Q_2,\qquad
L_1=Q_3,\qquad L_2=Q_4.
}
\tag{29}
$$

(26)、(27)、(29) 正是所称十个标量等式。

相较之下，pure 条件
$\int(F+iG)^4=0$ 只给
$A_4+E_4=6C_4$ 和 $B_4=D_4$。
全圆条件还保留 U、V 以及 (26)、(29)；不能由已消 pure 面积便宣告零次与二次谐波也消失。

## 6. 导数分包时的严格简化

取互不交的实紧微包 $u_i$，写

$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
A_i(\theta)=a_i c_\theta+b_i s_\theta.
\tag{30}
$$

R183 已证明此类满足全部 hook 槽零。定义

$$
C_i=\int(u_i'')^4>0,\qquad
M_i=\int x(u_i'')^4,\qquad
N_i=\int u_i'(u_i'')^3.
$$

代 (21)—(23)，逐包的实一维分部积分给

$$
\boxed{
m_0=0,\qquad
m_1=\frac34\sum_i C_iA_i^2(a_i^2-A_i^2),
}
\tag{31}
$$

$$
\boxed{
m_2^*=\sum_i\left(\frac32M_i-2N_i\right)
A_i^2(a_i^2-A_i^2).
}
\tag{32}
$$

这里的局域性来自已经准确化简的 $t_\theta',t_\theta''$ 与紧外槽；没有断言完整二、三阶恢复在每个微包外为零。

在此类中 $U=-B_4/4,V=-C_4/4$，因而 (27) 进一步等价于

$$
\boxed{
A_4=5C_4,\qquad E_4=C_4,\qquad B_4=D_4=0.
}
\tag{33}
$$

这些条件仍须与真实二次三矩 (2) 同时支付。仅按四次角权配平，不自动形成合法圆。

## 7. 四十个同形偶微包同时支付二次三矩与全角面积

本节给一个完全准确的零例。它只用于证明指定面积并非普遍障碍；第 9 节将证明其另一个已知必要门严格失败。

选一个非零实偶 $u\in C_c^\infty(-\delta,\delta)$。全部微包为同形平移
$u_i(x)=u(x-\xi_i)$，$\xi_i=c_0+\ell_0\rho_i$。以下所有中心互异：

| 类别 | $\rho_i$ | $(a_i,b_i)$ | 数量 |
|---|---|---|---:|
| 强正方向 | $\pm1,\ \pm4$ | $(\sqrt5,1)$ | 4 |
| 强负方向 | $\pm2,\ \pm\sqrt{13}$ | $(-\sqrt5,1)$ | 4 |
| 弱方向 | $\displaystyle\pm\sqrt{\frac{17}{2}\pm\frac{j}{100}},\ j=1,\ldots,8$ | $(0,1)$ | 32 |

最后一行两个正负号独立。选择 $\ell_0>0$、$c_0$ 使全部中心位于同一合法 I 的内部，再取足够小的 $\delta$，即可保证所有支撑两两不交并留双 collar。也可先取 $c_0>4\ell_0$ 再将整个有限构造放入允许的正区间；不需要计算某个实际宽度。

令 $z_i=a_i+ib_i$。同形偶性使三个二次矩准确为

$$
\int(q'')^2=I_0\sum_i z_i^2,\qquad
\int x(q'')^2=I_0\sum_i\xi_i z_i^2,
$$

$$
\int\{x^2(q'')^2+2(q')^2\}
=I_0\sum_i\xi_i^2z_i^2+I_2\sum_i z_i^2,
\tag{34}
$$

其中这里 $q=f+ig$，
$I_0=\int(u'')^2>0$、
$I_2=\int\{x^2(u'')^2+2(u')^2\}$。

先有

$$
\sum_i(a_i^2-b_i^2)=8\cdot4-32=0,\qquad
\sum_i a_i b_i=0.
$$

同方向的镜像中心对使 $\sum_i\rho_i z_i^2=0$。二次中心和准确为

$$
\sum_{\mathrm{strong}}\rho_i^2=2(1+16+4+13)=68,
$$

$$
\sum_{\mathrm{weak}}\rho_i^2
=2\sum_{j=1}^8
\left(\frac{17}{2}+\frac j{100}+\frac{17}{2}-\frac j{100}\right)
=272,
$$

$$
\sum_{\mathrm{strong}}\rho_i^2a_ib_i
=2\sqrt5(1+16-4-13)=0.
$$

因此
$\sum_i\rho_i^2z_i^2=4\cdot68-272=0$，
(34) 的三复矩全部为零。同时

$$
\int(f'')^2=\int(g'')^2=40I_0>0,\qquad
\int f''g''=0.
\tag{35}
$$

这已是非退化三矩圆；共同正归一化不破坏任何零条件。

令 $C=\int(u'')^4>0$。四次矩恰为

$$
(A_4,B_4,C_4,D_4,E_4)=C(200,0,40,0,40).
\tag{36}
$$

由 (33)，$m_1(\theta)=0$ 对全部角度成立。实偶性还给
$N_i=0$、$M_i=\xi_i C$。每个方向的中心均成
$c_0\pm\ell_0\rho$ 对，且 (31)、(32) 中的角因子相同，故

$$
\boxed{m_2^*(\theta)=2c_0m_1(\theta)=0.}
\tag{37}
$$

这里比例是 $2c_0$，不是 $c_0$。连同 $m_0=0$，(25) 全部成立。

三条实射影方向
$(\sqrt5,1),(-\sqrt5,1),(0,1)$ 互异。若某个常数可逆实二阶矩阵把 $(f,g)$ 变为支撑不交的一对，所有非零值向量必须原已落在两条固定直线的并中，与这三条方向矛盾。因此该 profile 平面不能由常数 GL(2) 换基化成不交类。

顺带，由 (36)、中心配对与偶性，

$$
\int(q'')^4=0,\qquad
\int x(q'')^4=0,\qquad
\int q'(q'')^3=0.
\tag{38}
$$

所以它也清掉 R249 的两个 pure 矩。这个事实来自本构造的新角方向，并不与 R249 对未旋转 $\pm$ 微包及 R239 特定互补双 block 的严格排除矛盾。

### 全角条件确实严格强于 pure 条件

再将这同一 pair 换为 $(\widetilde f,\widetilde g)=(g,-f)$。此时
$\widetilde q=-iq$、$\tau_{\widetilde q}=i\tau_q$，所以 R249 的两个 pure 矩仍为零；三矩、全 hook 以及下一节的完整第三阶构造也保留。但其四次矩变成
$C(40,0,40,0,200)$，故

$
\widetilde m_1(\pi/2)
=\frac34(\widetilde C_4-\widetilde E_4)
=-120C\ne0.
\tag{38a}
$

于是 pure 的两条第四谐波条件不能替代整个圆的面积条件。这是更换第一 profile 为 g 后的准确反例，目标度量随之改变；不是在旧固定目标上任意旋转。

## 8. 既有八复制如何使这个零例完整合法到三阶

把第 7 节 pair 视为一个完整基本包 $(f_*,g_*)$。按 R183，取八个等距平移、互不交的完整包络，并置

$$
\alpha_j=(-1)^j\binom7j^{1/3},\qquad
f=\sum_{j=0}^7\alpha_j f_*(x-t_*-jL),\qquad
g=\sum_{j=0}^7\alpha_j g_*(x-t_*-jL).
\tag{39}
$$

宽度和位置可预先选得足够小以容于同一个合法 I；最后只作共同正归一化。

每个基本包已付三复矩，所以对角差和交叉两种二阶 forcing 的真实恢复在整包络外为零。这里使用的是这些完整 forcing，**不是**宣称各自 $Z(f_*,f_*)$ 或单个微包第二场局域。

R46/R52/R183 的完整原式已证明：四个第三 forcing 的 ruling 在平移参数中次数至多六；其真实 second histories 与混合分量保留。因
$\alpha_j^3=(-1)^j\binom7j$，
第七有限差分准确消掉四个第三 ruling。导数分包保持全 hook 零，故在 (16) 的真实闭路径上，四个第三 period 也全部为零。这是已有三阶构造的直接应用，没有重算旧 forcing。

本稿所选面积的三个矩只含 (21)—(23) 的同点四次导数乘积，因此各完整复制按 $\alpha_j^4$ 相加。平移时

$$
(m_0,m_1,m_2^*)\longmapsto
(m_0,\ m_1+t\,m_0,\ m_2^*+2t\,m_1+t^2m_0).
$$

每个基本包的三项全为零，故 (39) 仍使完整 $A_{-2,-3}$ 系数全角恒零。三条射影方向保留，不能常换基分离。

由 R241 的联合安装范围，可以在同一 $M=0,T=\kappa_H\mathfrak H\ne0$ 类上使用 (1) 的小非零共振芽；这里不从“逐固定 $\kappa$ 可选小 $\varepsilon$”推断未经支付的抛物曲线。于是存在已支付完整三阶、且消去本稿整个指定面积的真实圆。改变首 profile 后目标度量也按新 f 定义；不称这是原 R239 固定目标上的变形。

## 9. 同一四十包严格违反另一个已知必要门

以上零例**不能**进入完整第四 ruling：R231 的 $L_c$ 对它严格为负。这一失败可以直接纸证，无需评价任何新积分。

取 R231 的 $\mathcal G=\mathcal G_0$，记
$G_i=\mathcal G(u_i,u_i)$。每个 $G_i$ 的真实左尾为 $c_i x^2$，并非紧槽。定义局部正 bulk

$$
S_i=\frac14\int_I x^4\big((G_i/x)''\big)^2
=\frac1{64}\int_I
x^6(x^2u_i''-2xu_i'+2u_i)^2(u_i''')^2>0.
\tag{40}
$$

其严格正性也可直接见于
$W=x^2u_i''-2xu_i'+2u_i$、
$W'=x^2u_i'''$：
若 (40) 为零，则 $(W^2)'=2WW'=0$，紧性迫 W=0，再由
$(u_i/x)''=W/x^3$ 得 $u_i=0$，矛盾。

置

$$
A_f=\mathcal G(f,f)=\sum_i a_i^2G_i,\qquad
A_g-A_f=\sum_i(b_i^2-a_i^2)G_i.
$$

第二槽因三矩而真正紧支撑。R238 的准确能量边界式先使**总体**边界为零，然后 $(G_i/x)''$ 的互不交支撑才给

$$
\boxed{
L_c=E(A_f,A_g-A_f)
=\sum_i a_i^2(b_i^2-a_i^2)S_i
=-20\sum_{\mathrm{strong}}S_i<0.
}
\tag{41}
$$

不能将这一步改写成
$E(G_i,G_i)=S_i$：单个 $G_i$ 的左二次尾有真实边界贡献。

式 (41) 对每个平移或正伸缩的基本包仍成立；八复制只增添正的 $\alpha_j^4$ 权重。故第 8 节的合法三阶圆也严格违反 $L_c=0$。本稿没有声称它支付 R231/R237/R241 的六能量，也没有把那些门仅标成“尚未检查”。

## 10. 新结论与下一构造的准确余地

本稿付清的是三个层次：

1. 从完整 R73 外槽而非 pure 对角，得到 (15) 的真实 Gaussian 面积系数，并在实际第三周期范围内准确化为 (19)。
2. 在该范围内，整个指定面积全角为零等价于十个明确标量条件 (26)、(27)、(29)；只消 pure 第四谐波不够。
3. 存在非均匀、不可常换基分离的合法三阶圆，确实满足全部这些条件；但本文的具体四十包被独立已知门 (41) 严格排除。

因此不能把 R249 的面积论证推广为“所有合法圆都失败”，也不能把本文的面积零例升级为完整第四阶构造。

对微包类，下一建设性问题至少要同时保三矩、(33)、(32) 与 $L_c=0,L_s=0$。式 (41) 说明仅加入 $a=0$ 包无法给 $L_c$ 正贡献；要在这种加法结构内抵消现有负项，须有某些 $0<a_i^2<b_i^2$ 的非零方向，或改变结构使正贡献实际出现。面积的权重 $C_i=\int(u_i'')^4$ 与能量的权重 $S_i$ 也不同，不能在二者之间共用一个未经证明的比例。

例如正坐标伸缩 $u_\lambda(\lambda x)=u(x)$ 给
$C(u_\lambda)=\lambda^{-7}C(u)$，
而 R238 给 $S(u_\lambda)=\lambda S(u)$。
这是真实的不同权重自由度，不是已经支付全条件的存在性证明。变形还必须保共同合法区间、完整第三阶及所有其他面积和完整 ruling/period；本稿未证明这些同时可解。

全部结论为准确纸面身份。没有新科学运行，没有把有限样本或小残差当连续结论，也没有获得有限等距族、闭嵌入、reach 或宏观幅度目标。
