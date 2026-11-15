# R768 的实际 r=2 延拓：三次有限纤维、固定最高主部与完整两输出

日期：2026-11-15。**状态：本文的实际来源序列、指定最高主部、全高尾矩阵及常数留数代表已证明；该矩阵的指定像和全球延拓仍未判定。**

原 $t^r$ 层强迫
$$
3\deg_YF(0,Y)+\deg_YQ(0,Y)\le4r+2.
\tag{1}
$$
因此先前 $r=1,\deg_YF(0,Y)\ge3$ 的条件推导不提供实际窗口；
其范围已另行更正。
本篇直接使用仍被原帽允许的
$$
\boxed{r=2,\quad\ell=1,\quad k=0,\quad
s=2h+2,\quad \deg_YF(0,Y)=3.}
\tag{2}
$$
保原 $P^{\rm fact}=qt^2F^3$、$q=d^{-C_D}Q$、
$d=1+8t$、$f_D<p$、全部十九角及 R750 的强接触门。
$F_Y(P),q(P)$ 为单位，$P=(0,1)$，
$\eta_0=t^hu$，$t^s=p\epsilon b_s$，
且 $M=c_*U_0w^{13}J$ 是整个原矩阵。

(2) 要求 $p=6s-1\equiv11\pmod{12}$。
由 (1) 有 $\deg Q(0,Y)\le1$。
原零角 $m=-v_0(F)$ 还准确为三：
$m\ge\deg F(0,Y)=3$，而
$v_0(qt^2F^3)\ge-2$、$v_0(Q)\le0$ 给 $3m\le10$。
所以 R765 的实际 $r_F\ge1$，此处 $k=0<r_F$。
这些是本窗口的真实必要条件，不是说已经找到一个满足强接触的具体 $F$。

置
$$
N_0=s-13,\quad T=N_0-2,\quad
\mathcal N=\mathcal O_C(C),\quad C=(F=0),
$$
$$
\boxed{
B=\frac{b_s(0)q_0(0)e(0)^3u(0)^2}{a}\in k^\times,
\quad e=(\mathcal EF)|_C,\quad q_0=q|_C .
}
\tag{3}
$$

## 1. 两个有限非 P 方向与实际核

令 $Z_0$ 为 $t=0$、有限 $Y$、除 $P$ 外的全部 Cartier 纤维部分。
它的长度准确为二，包括可能的非约化交。
在该开集，$E'$ 的方程是 $q_0t^2$，故
$$
Z_0\le E',\qquad
\mathcal P_{E'}\longrightarrow
\mathcal P_{E'}/\mathcal P_{E'-Z_0}
\simeq\mathcal N^3(E')|_{Z_0}.
\tag{4}
$$
在同一框中乘 $q_0t^2$ 后，(4) 读原来源的 $R\bmod t$。
$q_0$ 在其它点有零时仍使用这个线束框，不将它当函数单位。

沿用 R750/R766：
$$
0\longrightarrow H^0(C,\mathcal N^3)
\longrightarrow\mathcal U_D
\longrightarrow\mathcal V_{E'}\longrightarrow0,
$$
$$
\mathcal U_D=
\left\{\frac{R|_C}{q_0t^2}:
R\in\overline{\mathcal W}_D,\ 
\operatorname{ord}_P(R|_C)\ge2\right\}.
\tag{5}
$$
写
$$
F_0(Y)=F(0,Y)=c_0(Y-1)V_0(Y),
\qquad \deg V_0=2,\quad V_0(1)\ne0 .
$$
原 $A_n$ 保 $R(0,Y)$ 的次数至多二；(5) 保 $R(0,1)=0$。
因此最高极层的像包含在
$$
\mathcal L_2=\{A(Y-1)+C(Y-1)^2:A,C\in k\}
\longrightarrow k[Y]/V_0.
$$
这个映射为同构：
其核若非零，便是一个次数至多二却同时被
$Y-1$ 与 $V_0$ 整除的多项式，不可能。

定义准确的实际核
$$
\boxed{
\mathcal V_t^{(2)}
=\operatorname{pp}_{E'}
\left\{\frac{R|_C}{q_0t^2}:
R\in\overline{\mathcal W}_D\cap t\,k[t,Y,d^{-1}],
\ \operatorname{ord}_P(R|_C)\ge2\right\}.
}
\tag{6}
$$
这里的第二个条件不能省去；仅被 $t$ 整除不保证除 $t^2$ 后在 $P$ 正则。

**定理 1。** 完整实际来源给
$$
\boxed{
0\longrightarrow\mathcal V_t^{(2)}
\longrightarrow\mathcal V_{E'}
\xrightarrow{\pi_0}\mathcal L_2
\longrightarrow0.
}
\tag{7}
$$
核的证明与上述 monic 除法一致：
若最高极层为零，则 $V_0\mid R(0,Y)$；
结合 $R(0,1)=0$ 和次数帽，得到 $R(0,Y)=0$。
增加三倍截面可用原 $qt^2H_3$ 表示，仍在 (6)，故与代表无关。
下面给原全帽内的两个满射列，同时支付第二阶低值门。

## 2. 同一个低 r 右逆和完整实际两列

原低轴有
$$
\psi(t)=1+\gamma_1t+O(t^2),
\qquad \gamma_1=154/15 .
\tag{8}
$$
这是同一个实际 $g$ 的低轴，因 $h>2$ 与 $C$ 分支相同。
取原
$$
q_2=(t-1)/d,\qquad
\iota_2(f)=Y^2q_2\,\pi_2^t(f/(\psi^2q_2)).
$$
将 $Y-1$ 与 $1-2Y-Y^2q_2$ 用这个右逆校正，
准确得到
$$
\boxed{
L_2=Y-1+\gamma_1tY^2q_2,
}
\tag{9}
$$
$$
\boxed{
Q_2=1-2Y-(1+9t)Y^2q_2
=(Y-1)^2-\frac{9t^2Y^2}{d}.
}
\tag{10}
$$
两者的曲线值均消到 $t^2$，
而零纤维多项式仍分别为 $Y-1$ 与 $(Y-1)^2$。
$n=0,1,2$ 的原列和次数至多一的系数完全支付 (9)、(10)；
未添加新来源。

记 $v_{\rm lin},v_{\rm quad}$ 为对应真实主部。
(9)、(10) 证明 (7) 满射。
尤其其最高极层是整个长度二的环境层，
但**只有这个投影**已证明满射；
$\mathcal V_{E'}$ 的其它边界部分没有被替换为环境。

(10) 的完整归一高尾为
$$
\boxed{
u_{\rm quad}
=\frac{1}{q_0}\left(\frac{\psi-1}{t}\right)^2
-\frac{9\psi^2}{q_0d}.
}
\tag{11}
$$
其原点值准确为
$$
\boxed{
u_{\rm quad}(P)
=\frac{\gamma_1^2-9}{q_0(P)}
=\frac{109\cdot199}{225q_0(P)}\in k^\times.
}
\tag{12}
$$
$109,199\equiv1\pmod3$，所以当前惯性 $p>101$ 不会除这两个数。
这只是实际高尾的一个已知单位，不独立构成整个余核非零。

第一 normal 的完整曲线值为
$$
\boxed{
(\mathcal EQ_2)|_C
=2\psi(\psi-1)-\frac{18t^2\psi^2}{d}.
}
\tag{13}
$$
(11)、(13) 均保全部高尾；不能以它们在 $P$ 的首项替代。

## 3. 原完整 p² 条件指定最高平方主部

对 (5) 定义
$$
d_1(\operatorname{pp}u)=(\mathcal ER)(P),\qquad
d_2(\operatorname{pp}u)=(\mathcal E^2R)(P).
$$
由 (7)，对
$\pi_0(v)=A(Y-1)+C(Y-1)^2$，
$$
\boxed{d_1(v)=A,\qquad d_2(v)=A+2C.}
\tag{14}
$$
两个泛函都杀 (6) 和整个 $H^0(C,\mathcal N^3)$。

若同一个实际 $R$ 满足
$$
M(P^{\rm fact}+pR)\in p^2,
\tag{15}
$$
则 R755/R765 的完整值投影给 $R|_C=0\bmod t^{N_0}$，
而前一 normal 常数 forcing 为零，
第三块第 $13$ 行的 forcing 为 $3a^2B$。
所以
$$
d_1(v_R)=0,\qquad d_2(v_R)=-6B,
$$
从而
$$
\boxed{
R(0,Y)=-3B(Y-1)^2,\qquad
\pi_0(v_R)=-3B(Y-1)^2.
}
\tag{16}
$$
这是整个原 $M$ 的首次提升必要条件，无须删掉两条十三行改用相对 $J$。

因为 $Y-1$ 在 $Z_0$ 上为单位，(16) 还给每个正规化支的准确极阶
$$
\boxed{
\operatorname{pole}_Q(u_R)
=v_Q(q_0)+2v_Q(t)\qquad(Q\text{ 位于 }Z_0).
}
\tag{17}
$$
此处 $r=2$，所以即使 $q_0$ 在 $Z_0$ 是单位，
(16) 也只指定最高一个 $t$ 极层，不能宣称两个 $t$ 层都固定。
较低层和其它原边界仍由同一个来源联立决定。

## 4. 实际剩余核和完整两个输出

(16) 与低二阶值门准确等价于
$$
\boxed{
R=-3B Q_2+R_t,\quad
R_t\in\overline{\mathcal W}_D\cap t\,k[t,Y,d^{-1}],
\quad \operatorname{ord}_P(R_t|_C)\ge2.
}
\tag{18}
$$
因此值段加两个常数 normal 可解，准确等价于
$$
\boxed{
\mathcal O_T(v_{\rm quad})
\in\mathcal O_T(\mathcal V_t^{(2)}).
}
\tag{19}
$$
从 (19) 返回时，只减去由原 $qt^2H_3$ 给出的三倍截面，
它保持 (6)，所以始终是同一个真实 $R$。

为保剩余 first-normal 的全长，写 $R_t=tS$。
$\mathcal S_D=t^{-1}(\mathcal W_D\cap t\,\mathcal O[t,Y,d^{-1}])$
的完整整基准确为
$$
\boxed{
\begin{cases}
Y^nq_n\,\mathcal O[t]_{\le e_{n+1}-1},&n=0,1,2,\\
Y^n(q_n/t)\,\mathcal O[t]_{\le e_{n+1}},&n\ge3.
\end{cases}}
\tag{20}
$$
这是一个实际商的定义；不把整个原格免费除 $t$。

将 $\beta=M(P^{\rm fact})/p\bmod p$ 按原完整 $c_*U_0$ 和 $w^{13}$
运输到短三块，写为
$(0,\beta_1,3a^2B)$。
因为 $P^{\rm fact}\in\ker\bar J$，
它在两条十三行 carry 位置的约化为零。
代入 (18)，整个首次提升的剩余方程准确为
$$
\boxed{
\begin{aligned}
S(t,g)_{<N_0-1}
&=\left[\frac{3B\,Q_2(t,g)}t\right]_{<N_0-1},\\
(\mathcal ES)(t,g)_{<N_0-1}
&=\left[
\frac{3B(\mathcal EQ_2)(t,g)}t
-\frac{\beta_1}{a t}
\right]_{<N_0-1},
\qquad S\in\overline{\mathcal S}_D .
\end{aligned}}
\tag{21}
$$
两个右端整，第一行的常数为零，
所以同一个 $S$ 自动满足 $S(P)=0$，即 (18) 所需的二阶低值门。
$\operatorname{ord}\beta_1\ge h>2$；
其 native $\xi$、完整 regular 高尾与 carry 全留在 (21) 中。
$t(w)$ 的完整单位变换也未替成首项。

(21) 不是只判一个 scalar：
它是同来源两输出、全长度 $N_0-1$ 的指定像问题。
两个输出不能用不同的 $S$ 分别解决。
进入 $p^3$ 时，仍用 (18) 的同一个整 $R$，
恢复完整 $J$、两条十三行和同一个下一修正；
模 $p$ 行消元不冒整目标的自由共轭。

## 5. 对偶只在剩余实际核上归零

由 (7)，
$(\mathcal V_t^{(2)})^\perp=\operatorname{span}\{d_1,d_2\}$。
(19) 失败，当且仅当存在
$$
\omega\in\mathcal D_T
=H^0(C,\omega_C\mathcal N^{-3}(TP))
$$
和某个 $\lambda\in k$，满足
$$
\boxed{\mathcal O_T^*\omega=d_2+\lambda d_1.}
\tag{22}
$$
等价地，$\mathcal O_T^*\omega$ 杀 (6)，
但在固定平方主部 $v_{\rm quad}$ 上非零；
不是对整个 $\mathcal V_{E'}$ 无条件指定一个既定单行。
因为 $d_1(v_{\rm quad})=0,d_2(v_{\rm quad})=2$，
归一化成 (22) 合法。

若 (22) 实际成立，R766 同一个低二阶右逆产生真正杀全 $M$ 首像的行，
在完整 forcing 上的值为 $6B\ne0$。
本篇仍未构造这个全球 $\omega$。

## 6. 三次有限纤维的常数二阶代表

此处 monic $W_0=F_0/c_0$ 恰为三次，写
$$
W_0(Y)=Y^3+c_2Y^2+c_1Y+c_0',
\qquad W_0(1)=0.
$$
其 Lagrange 核为
$$
L(Z,Y)=Z^2+ZY+Y^2+c_2(Z+Y)+c_1.
$$
所以 R768 的两条实际 normal 核准确为
$$
K_1(Y)=Y+2+c_2,\qquad K_2(Y)=Y+4+c_2.
$$
因此
$$
\boxed{
K_2+\lambda K_1
=(1+\lambda)(Y+c_2)+4+2\lambda,
}
\tag{23}
$$
最高 $Y$ 项的唯一消去是
$$
\boxed{\lambda=-1,\qquad K_2-K_1=2.}
\tag{24}
$$
原 forcing 值不变，因为第一 normal 常数为零。
这不是新增测试，也没有把其它角变成自由单位。

经过同一个 $q_0t^2$ 框，
普通二阶泛函 $d_2-d_1$ 的确定局部代表为
$$
\boxed{
\omega_{\rm ord}=2c_0\,q\,t\,\frac{dt}{F_Y}.
}
\tag{25}
$$
与 $u_R$ 相乘后为 $2c_0R\,dt/(tF_Y)$，
正好读取 (16) 的最高 $t$ 极层。
它杀 (6)，并在 $v_{\rm quad}$ 上取值二。
$P$ 分支的局部留数仍为零，因为 (5) 的分子消到 $t^2$。

(25) 在 $P$ 的零阶准确为一：
$q(P),F_Y(P),2c_0$ 都为单位。
它在其它原边界的完整除子仍是
$$
\boxed{
\operatorname{div}_{\widetilde C}
(2c_0q\,tY^3F_Y^2dt)
+\Delta_C-3\pi^*D_e.
}
\tag{26}
$$
故它作为 $\omega_C\mathcal N^{-3}$ 的有理截面，
总极次数至少为
$$
2\kappa+\chi+1,
$$
且全部仍在原边界，不能免费移到 $P$。

相对于单独 $K_2$，每个 $v_Q(Y)<0$ 的原支准确改善
$-v_Q(Y)$ 个极阶；其它十九角和无穷远支须照 (26) 读取。
(24) 在整个允许两行铅笔内是唯一最高项消去，
不是说它已经全球延拓到 $\mathcal D_T$。

本篇给了不再被最低角不等式直接排除的参数范围，以及同一个 $R$ 的完整新接口：
最高平方主部、低二阶整右逆的全部高尾、
(21) 的原两输出矩阵，以及 (25) 的常数有限纤维核。
仍须判 (21) 的指定像或完成 (22) 的真实全球延拓；
原无穷素数主目标没有完成。

依赖：
[R768](../results/R768-finite-fiber-normal-residue-and-original-global-pole-divisor.md)；
[R750](../results/R750-whole-source-residual-divisor-and-specified-forcing-residue-rows.md)；
[R755](../results/R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R765](../results/R765-original-zero-angle-and-unavoidable-nonfactor-first-correction.md)；
[R766](../results/R766-actual-principal-part-normal-functional-and-specified-small-obstruction.md)。
