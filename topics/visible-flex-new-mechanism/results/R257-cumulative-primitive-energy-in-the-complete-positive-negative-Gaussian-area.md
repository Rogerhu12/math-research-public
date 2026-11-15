# R257：完整正负 Gaussian 面积中的累计二次 primitive 能量

日期：2026-11-15。**已证明，纯纸面结论。** 没有执行新的 profile 求积、规范化、参数扫描或几何研究计算。

本稿从原 $\Phi_{p_2}$ 算子取得完整 $A_{1,-3}$ 面积的一条新必要矩。它包含
$\int_I(J((q'')^2))^2$，保留各微包的真实累计顺序，不能由局部四次角权或 $S_i/C_i$ 比值替代。

对 R250 的四十同形偶包，这个量的虚部严格为正，因此该包不仅有 R250 已知的 $L_c<0$，还违反另一个完整 Gaussian 面积。更有用的是，本稿把新矩写成适用于多宽度微包的准确有限有序公式，供后继联合构造使用；没有把该有限方程宣称为整个 ruling 的充分条件。

来源：[R73 原八矩及真实 history](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R245 完整 Gaussian 归约](R245-complete-block-additivity-and-four-Gaussian-history-reduction.md)、[R248 完整第四谐波](R248-complete-fourth-harmonics-and-complementary-block-reduction.md)、[R249 真实词独立性](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R250 完整圆面积与四十包](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R251 参数系数](R251-nonresonant-Gaussian-area-obstruction-and-two-exceptional-curves.md)和 [R252 原交叉矩方法](R252-two-further-Gaussian-areas-exclude-the-even-packet-exceptional-family.md)。

## 1. 新必要条件及完整面积来源

仍取同一例外端芽

$$
H=e^{\varepsilon\sigma^2},\quad
h=h_eH,\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,
\qquad h_e>0,\quad\varepsilon>0,\quad\kappa\ne0.
\tag{1}
$$

实际区间、物理支、左右 collar、右锚及全部真实入 history 保持。令 $q=f+ig$ 为合法三矩圆的复 profile，即

$$
\int_I(q'')^2
=\int_Ix(q'')^2
=\int_I\{x^2(q'')^2+2(q')^2\}=0.
\tag{2}
$$

定义普通复乘积

$$
v=q',\qquad \rho=q'',\qquad \tau=q''',\qquad
\mathcal A=J(\rho^2),\qquad J(F)(x)=\int_x^rF(t)\,dt.
$$

本稿的新 quartic 泛函是

$$
\boxed{
\begin{aligned}
\mathscr Q(q)={}&\frac12\int_I\mathcal A^2
+\int_Ix^2\rho^4-\frac83\int_Ixv\rho^3\\
&+\frac43\int_Iq\rho^3+\int_Iv^2\rho^2.
\end{aligned}}
\tag{3}
$$

没有使用共轭或绝对值平方。

记 $P=\Phi_{r_0}$、$Y=\Phi_{p_2}$。R73 的 $p_2$ raw 系数为

$$
M_{p_2}=-\frac{kh}{2}
=\frac{h_e}{2}(j-\kappa)H,\qquad
j=2\varepsilon\kappa\sigma^2.
$$

在 $\int_0^\sigma jH$ 中，$E_1=\int_0^\sigma H$ 的余系数准确为 $-\kappa$。故

$$
\boxed{B_1=-\kappa h_eY.}
\tag{4}
$$

同 R251，

$$
B_{-3}=cP,\qquad
c=\frac{\kappa\{\varepsilon(36-84\kappa^2)-20\kappa^4-9\kappa^2-27\}}
{216h_e^3}.
\tag{5}
$$

在 R250 的共振 $\varepsilon=\kappa^2/4$ 上，$c\ne0$。

R249/R252 已逐槽证明：完整 pure 四次 ruling 的 $A_{s,t}$ 系数准确为
$-2\mathcal E_\sigma(q,[B_s,B_t]_\Delta(q))$。这里

$$
[B_1,B_{-3}]_\Delta
=\kappa h_ec[P,Y]_\Delta.
\tag{6}
$$

下文证明原式身份

$$
\boxed{
m_0(q,[P,Y]_\Delta(q))
:=\int_Iq''([P,Y]_\Delta(q))''
=-\frac12\mathscr Q(q).
}
\tag{7}
$$

外槽的完整能量仍为

$$
\mathcal E_\sigma(q,\psi)
=\frac{1+j^2}{4h}m_0(q,\psi)
+\frac j2m_1(q,\psi)+\frac h4m_2^*(q,\psi).
\tag{8}
$$

$H$ 对 $\mathbb R(\sigma)$ 超越，因此 (8) 恒零必须使 $m_0=0$。真实 Gaussian 面积独立性随即给：

$$
\boxed{
c\ne0,\quad\text{完整第四 ruling 可解}
\quad\Longrightarrow\quad \mathscr Q(q)=0.
}
\tag{9}
$$

未知的 $m_1,m_2^*$ 没有被置零，也不能取消非零的 $H^{-1}$ 系数。式 (9) 只是一条新必要矩，不是该面积或全部 ruling 的充分条件。

## 2. 原 $p_2$ 二次算子及 cubic 能量

R73 的完整原式给

$$
Y(q,q)
=-xq^2+x^2qv-\frac{x^3}{2}v^2
-\frac{x^2}{4}\mathcal C,
\qquad
\mathcal C=J(x^2\rho^2+2v^2).
\tag{10}
$$

没有丢弃 $\mathcal C$ 的左尾。直接求二阶导数得

$$
\begin{aligned}
(Y(q,q))''={}&-2qv+2xq\rho-2x^2v\rho
+x^2(q-xv)\tau\\
&+\frac{x^3}{2}\rho^2+xv^2-\frac{\mathcal C}{2}
+\frac{x^4}{2}\rho\tau.
\end{aligned}
\tag{11}
$$

定义 $\mathcal F_Y(q)=\int_I\rho(Y(q,q))''$。逐项分部积分给

$$
\boxed{
\mathcal F_Y(q)=
\int_I\left\{
xq\rho^2-\frac32x^2v\rho^2
+\frac13x^3\rho^3-\frac13v^3
\right\}.
}
\tag{12}
$$

为列明原系数与端项，(11) 使用的恒等式包括

$$
\int_Iqv\rho=-\frac12\int_Iv^3,\qquad
\int_Ixv^2\rho=-\frac13\int_Iv^3,
$$

$$
\int_Ix^2q\rho\tau
=-\int_Ixq\rho^2-\frac12\int_Ix^2v\rho^2,
$$

$$
\int_Ix^3v\rho\tau
=-\frac32\int_Ix^2v\rho^2-\frac12\int_Ix^3\rho^3,
$$

$$
\int_Ix^4\rho^2\tau=-\frac43\int_Ix^3\rho^3,
$$

$$
\int_I\rho\mathcal C
=\int_Ix^2v\rho^2+2\int_Iv^3.
\tag{13}
$$

最后一式来自 $\rho=v'$ 和
$\mathcal C'=-(x^2\rho^2+2v^2)$；端项 $[v\mathcal C]$ 因 $v$ 的双零 collar 消失。证明 (12) 本身不需要先把 $\mathcal C$ 左尾假设为零。

## 3. 合法方向上的真实变分与新 primitive 项

对 $P(q,q)=\mathcal A$，原式立即给

$$
\mathcal F_P(q)=\int_I\rho(P(q,q))''=0.
$$

三矩 (2) 使 $\mathcal A$ 和 $Y(q,q)$ 都为紧 profile。具体地，$\mathcal A$ 的左常尾由第一个矩支付；(10) 的左二次尾由第三个矩支付。因而沿这两个方向对紧输入恒等式求变分合法，不是假定单个微包也有同样的紧性。

由对称配对 $m_0$，

$$
2m_0(q,[P,Y]_\Delta(q))
=D\mathcal F_P(q)[Y(q,q)]
-D\mathcal F_Y(q)[P(q,q)]
=-D\mathcal F_Y(q)[\mathcal A].
\tag{14}
$$

沿 $\delta q=\mathcal A$，

$$
\delta v=-\rho^2,\qquad
\delta\rho=-2\rho\tau.
$$

将其直接代入 (12)，未分部积分的完整变分是

$$
\begin{aligned}
D\mathcal F_Y(q)[\mathcal A]
=\int_I\bigl\{&
x\mathcal A\rho^2-4xq\rho^2\tau
+\tfrac32x^2\rho^4\\
&+6x^2v\rho^2\tau
-2x^3\rho^3\tau+v^2\rho^2
\bigr\}.
\end{aligned}
\tag{15}
$$

其中

$$
\int_Ixq\rho^2\tau
=-\frac13\int_I(q+xv)\rho^3,
$$

$$
\int_Ix^2v\rho^2\tau
=-\frac13\int_I(2xv\rho^3+x^2\rho^4),
$$

$$
\int_Ix^3\rho^3\tau=-\frac34\int_Ix^2\rho^4.
\tag{16}
$$

新的累计项必须保留：

$$
\begin{aligned}
\int_Ix\mathcal A\rho^2
&=-\frac12\int_Ix(\mathcal A^2)'\\
&=-\frac12[x\mathcal A^2]_\ell^r+\frac12\int_I\mathcal A^2
=\frac12\int_I\mathcal A^2.
\end{aligned}
\tag{17}
$$

这里先由 (2) 知 $\mathcal A$ 在两 collar 为零，才消掉端项。其余 (13)、(16) 的边项均含紧输入的导数。合并 (15)—(17) 即得
$D\mathcal F_Y[\mathcal A]=\mathscr Q$，从而证明 (7)。

最后的三次交换子仍可能有左尾；本稿不据上述两条二次方向的紧性将其删掉。外槽一直使用完整 (8)。

## 4. 任意 disjoint 微包的有序 primitive 公式

式 (3) 的非局部项可准确有限化。设
$\varrho=q''^2$，其全积分为零。取

$$
K(x)=\int_I|x-y|\varrho(y)\,dy.
$$

则 $K''=2\varrho$，且

$$
K'(x)=-2\mathcal A(x).
$$

$K$ 本身可以在 collar 取非零常值，但 $K'$ 在两端为零。于是

$$
\boxed{
\int_I\mathcal A^2
=-\frac12\int_I\int_I|x-y|
\,\varrho(x)\varrho(y)\,dx\,dy.
}
\tag{18}
$$

这是普通复双线性身份，不是非负范数。端项 $[KK']$ 已由真实零总矩支付。

进一步写

$$
q=\sum_i z_i u_i,
$$

其中实 $u_i$ 的支撑互不交，按从左到右排序。置

$$
m_i=\int_I(u_i'')^2>0,\qquad
\mu_i=\frac1{m_i}\int_Ix(u_i'')^2,
$$

$$
\Delta_i=\int_I\int_I|x-y|
(u_i''(x))^2(u_i''(y))^2\,dx\,dy>0.
$$

在不同包 $i<j$ 上，$|x-y|=y-x$。式 (18) 准确成为

$$
\boxed{
\int_I\mathcal A^2
=-\frac12\sum_i z_i^4\Delta_i
-\sum_{i<j}z_i^2z_j^2m_im_j(\mu_j-\mu_i).
}
\tag{19}
$$

这正是必须保留的真实左右次序与跨包尾项。单个 $J((u_i'')^2)$ 有非零左常尾，不能把 (19) 改成仅第一项或仅各包局部积分。

## 5. R250 四十包的全部局部项准确消失

沿用 R250 未归一的基本 pair。所有微包是同一实偶 $u$ 的平移，中心为
$\xi_i=c_0+\ell_0\rho_i$。其正半边的从左到右次序和系数为：

| 正中心参数 | $z_i=a_i+ib_i$ | $z_i^2$ |
|---|---|---|
| $1$ | $\sqrt5+i$ | $4+2i\sqrt5$ |
| $2$ | $-\sqrt5+i$ | $4-2i\sqrt5$ |
| $\sqrt{17/2\pm j/100}$，$j=1,\ldots,8$ | $i$ | $-1$ |
| $\sqrt{13}$ | $-\sqrt5+i$ | $4-2i\sqrt5$ |
| $4$ | $\sqrt5+i$ | $4+2i\sqrt5$ |

每个中心还有同系数的负镜像，共四十包。宽度取 R250 已允许的严格不交范围。其三复矩证明已给

$$
\sum_i z_i^2=\sum_i\xi_i z_i^2
=\sum_i\xi_i^2z_i^2=0.
\tag{20}
$$

对于这三种角方向，逐项有

$$
z_i^4=-\operatorname{Re}(z_i^2)
+8i\,\operatorname{Im}(z_i^2).
$$

因此同一三个实权也给

$$
\sum_i z_i^4=\sum_i\xi_i z_i^4
=\sum_i\xi_i^2z_i^4=0.
\tag{21}
$$

式 (3) 的其余四项是同形包的局部四次积分；在平移参数中次数分别至多 $2,1,0,0$。由 (21)，它们全部准确为零。因此在这个基本包上，

$$
\boxed{
\mathscr Q(q)=\frac12\int_I\mathcal A^2,\qquad
m_0(q,[P,Y]_\Delta(q))=-\frac14\int_I\mathcal A^2.
}
\tag{22}
$$

(21) 只消局部项，不消 (19) 的真实有序交叉项。

## 6. 整个累计 primitive 的严格虚部符号

令 $m=\int(u'')^2>0$，并记 $P_*=4+2i\sqrt5$。从最右侧向中心移动，包间的准确累计值依次为

$$
\frac{\mathcal A}{m}:
\quad 0\longrightarrow P_*\longrightarrow8
\longrightarrow-8\longrightarrow-P_*\longrightarrow0.
\tag{23}
$$

中间 $8\to-8$ 恰是正半边十六个弱包各减一。它们确在 $2$ 与 $\sqrt{13}$ 之间，因为

$$
4<\frac{17}{2}-\frac8{100}
<\frac{17}{2}+\frac8{100}<13.
$$

在一个强包内部，令 $t\in[0,1]$ 表示该包已经纳入右积分的 $(u'')^2$ 质量比例。四个强包按从右到左的顺序，其准确虚部为

| 强包中心参数 | $\operatorname{Im}(\mathcal A/m)^2$ |
|---|---|
| $4$ | $16\sqrt5\,t^2$ |
| $\sqrt{13}$ | $16\sqrt5(1-t^2)$ |
| $2$ | $16\sqrt5\,t(2-t)$ |
| $1$ | $16\sqrt5(1-t)^2$ |

全部非负。弱包内 $\mathcal A$ 始终实，所以虚部为零。在
$4$ 与 $\sqrt{13}$ 的两个强包之间，以及 $2$ 与 $1$ 之间，存在正长度的平台且

$$
\operatorname{Im}(\mathcal A/m)^2=16\sqrt5>0.
$$

密度 $q''^2$ 关于 $c_0$ 为偶，而其总积分为零，因此整个真实 primitive 满足

$$
\mathcal A(c_0+t)=-\mathcal A(c_0-t).
$$

其平方在两半边相同；collar 外的零延拓不要求原 I 关于 $c_0$ 对称。于是

$$
\boxed{\operatorname{Im}\int_I\mathcal A^2>0.}
\tag{24}
$$

这不是小宽度渐近或只取包间常值：表中已经包含每个强包内部的完整过渡，弱包也逐项保留。

由 (22)、(24)，共振端芽上完整 $A_{1,-3}$ 的一个真实外矩非零。R249 的真实 Gaussian 独立性及允许 gauge 的偶部范围说明，此面积不能由其他局部项、别的面积、真实中心 history 或二、三阶 homogeneous gauge 消去。

## 7. 完整第三阶复制与归一化不消掉这个新缺陷

R250 的八复制使用互不交的完整基本包及实幅度 $\alpha_j$。每个基本包已经有第一个复矩零，所以各自的 $\mathcal A_j$ 真正紧支撑；这时才有

$$
\mathcal A_{\rm total}
=\sum_j\alpha_j^2\mathcal A_j,\qquad
\int_I\mathcal A_{\rm total}^2
=\sum_j\alpha_j^4\int_I\mathcal A_j^2.
\tag{25}
$$

平移不改变右边各项，故虚部严格为正。每个包的 (21) 在平移后仍成立，局部项仍全为零。于是已经完成三阶的八复制圆也违反 (9)。

若其后作共同实归一化，$\mathscr Q$ 只乘正四次因子。对共同正坐标伸缩 $x=ay+d$，令 $q_{\rm new}(x)=q((x-d)/a)$ 并同时搬移右锚，原式给

$$
\mathscr Q(q_{\rm new})
=a^{-5}\left\{
\mathscr Q(q)+2\frac daM_1(q)
+\left(\frac da\right)^2M_4(q)
-\frac83\frac daN_1(q)
\right\},
\tag{26}
$$

其中 $M_4=\int(q'')^4$、$M_1=\int x(q'')^4$、
$N_1=\int q'(q'')^3$。R250 基本包和八复制都已准确满足这三个量为零，所以 (26) 保留非零性。没有假定任意固定查询在仿射变化下只乘常数。

## 8. 给多宽度新构造的准确有限方程

以下接口保留新的真自由度，也保留全部累计交叉项。取一个实偶紧 $u$，令

$$
\eta_w(x-\xi)=w^{3/2}u((x-\xi)/w),\qquad w>0.
$$

这是 $I_0$ 归一化的宽度族。写互不交且从左到右排列的

$$
q(x)=\sum_i z_i\eta_{w_i}(x-\xi_i).
$$

定义固定形状常数

$$
m=\int(u'')^2,\qquad C=\int(u'')^4,\qquad
I_2^*=\int\{x^2(u'')^2+2(u')^2\},
$$

$$
\Delta=\iint|x-y|(u''(x))^2(u''(y))^2\,dx\,dy,
$$

$$
L=\int\left\{
x^2(u'')^4-\frac83xu'(u'')^3
+\frac43u(u'')^3+(u')^2(u'')^2
\right\}.
$$

真实三复矩恰为

$$
\sum_i z_i^2=0,\qquad
\sum_i\xi_i z_i^2=0,\qquad
m\sum_i\xi_i^2z_i^2+I_2^*\sum_iw_i^2z_i^2=0.
\tag{27}
$$

此时 (19) 给

$$
\int_I\mathcal A^2
=-m^2\sum_{i<j}z_i^2z_j^2(\xi_j-\xi_i)
-\frac{\Delta}{2}\sum_i z_i^4w_i.
$$

而 (3) 的局部项准确为
$\sum_i z_i^4(C\xi_i^2/w_i+w_iL)$，偶性已经支付所有一阶中心项。因此

$$
\boxed{
\mathscr Q(q)=
-\frac{m^2}{2}\sum_{i<j}z_i^2z_j^2(\xi_j-\xi_i)
+\sum_i z_i^4
\left\{\frac{C\xi_i^2}{w_i}
+w_i\left(L-\frac{\Delta}{4}\right)\right\}.
}
\tag{28}
$$

这是可以与局部角权、$S_i/C_i$、三矩及其他面积共同处理的准确有限方程。系数是真实固定 shape 积分；本稿没有数值评价它们，也没有把它们假定为可独立调节。

式 (28) 明确表明：即使局部四次张量及两领先能量被配平，累计顺序项仍须另付。反之，$\mathscr Q=0$ 只清本稿指定面积的 $m_0$，尚须同面积的 $m_1,m_2^*$、其他面积、其余局部函数及整个 period/joint。

本稿因此提供的是一个新的完整函数必要门、一个已知试验包的准确失败机制，以及后继联合构造可直接使用的真实有限表达，不是对所有圆的否定，也不是主课题完成。

