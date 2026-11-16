# 同一原修正的有限纤维零类与完整低 normal 段返回

日期：2026-11-16。**状态：以下同预算分解的真实 normal 运输、指定修正有限类的条件非零及同一第二页的限制已证明。没有由此排除原全部 $p^3$ 提升，也没有判定 $K_1$ 的完整有限纤维像。**

本注接[同一第二页修正的末行和剩余分支](2026-11-16-r872-factored-corrector-last-row-and-residual-branches.md)、[真实有限纤维商](2026-11-16-r872-native-finite-fiber-quotient-and-cubic-ramification.md)及[两 charge 连接核](2026-11-16-r872-quartic-two-charge-global-connecting-kernel.md)。

## 1. 原精度与完整零类

严格保前述同修正注的假设：
$$
p=6s-1>211,\quad r=3,\quad \tau=1,\quad
s=2h+2,\quad 1<\ell\le h-1,\quad h<s-4.
$$
同一 R491 因子化整来源为
$$
P^{\rm fact}=t^3\widetilde F^{\,4}\widetilde q
\in\mathcal W_D ,
$$
并且同一个原 $R,S$ 满足
$$
\boxed{
M^{\rm orig}(P^{\rm fact}+pR+p^2S)\in p^3\Gamma_4.
}
\tag{1}
$$
全部 $P_{134}$、$c_*U_0$、charge 四十、十九角及三条十三行带保持。
以下的 $R$ 取其模 $p$ 约化。
另保实际 $D\ge4b$、$p>D+40$ 与原因子曲线 $C$ 几何整。

置
$$
L=E+40,\quad
\mathscr V_1=\mathcal W_D\cap Fk(t)[Y],\quad
\mathscr J_3=L^{-1}(\mathcal W_D\cap F^3k(t)[Y]).
$$
定义真正的全球来源类
$$
\mathfrak o_D(W)=[W]\in
\mathcal W_D/(\mathscr V_1+\mathscr J_3).
\tag{2}
$$
前述有限纤维证明将 (2) 分成实际有限层与
$\ker[H^1\mathscr V_4\to H^1\mathscr V_1\oplus H^1\mathscr V_3]$。
本注中“零类”始终指**两部分都为零**，不只是物理 $t=0$ 的二／三行商。

若
$$
\mathfrak o_D(R)=0,
\tag{3}
$$
则按定义有真正同预算分解
$$
\boxed{R=R_F+J,\qquad R_F=FH\in\mathscr V_1,\qquad
J\in\mathscr J_3.}
\tag{4}
$$
$H$ 不被认成另一个可任意选择的来源；只用原 $R_F$ 的真实因子商。

## 2. 四个限制值的准确运输

由 (1) 的完整原精度，前述同修正注已付
$$
R|_C\in w^s,\qquad
ER|_C=-\frac{11C_0u_0^4}{a}w^{s-1}+O(w^s),
\tag{5}
$$
$$
E^2R|_C\equiv
\frac{28}{a}w^{h+1}C(w)u(w)^3e(w)\pmod{w^{h+\ell}},
\tag{6}
$$
$$
E^3R|_C\equiv
-24w^3C(w)\xi(w)e(w)^3
-\frac{36}{a}wC(w)u(w)^2e(w)^2
\pmod{w^\ell}.
\tag{7}
$$
这里 $C,u,e,\xi$ 全部是同一个因子提升及完整实际轴的数据；
特别 $C_0=t_1^3q(0,1)$，不再包含已经准确运输的 $c_*U_0$。
式 (7) 的 $\xi$ 仍保留。

由 (4)，$J|_C=R|_C\in w^s$。
原 $\mathscr J_3$ 的 Euler Taylor 因而给
$W_0(J)\in w^s$，所以 $J\in K_1$，且其三条首 carry 带均通过。

还需要计算全 normal，不能只用 $\Pi(J)=0$。
写 $LJ=F^3A$。逐项 Leibniz 给
$$
LJ\in(F^3),\qquad L^2J\in(F^2),\qquad L^3J\in(F).
$$
限制后依次解三个三角等式，准确得到
$$
\boxed{(E^iJ)|_C=(-40)^iJ|_C,\qquad 0\le i\le3.}
\tag{8}
$$
这里是原多项式先作 $E^i$ 再限制；**没有**把横向 $E$ 当成
$k(C)$ 上可直接求导的算子。

由 $J|_C\in w^s$，同一个 $R_F$ 满足
$$
\boxed{
R_F|_C=0,\qquad
ER_F|_C\equiv ER|_C\pmod{w^s},
}
\tag{9}
$$
以及 (6)、(7) 原样成立于 $R_F$。
理由是 $h+\ell\le2h-1<s$ 且 $\ell<s$，
故 (8) 的全部补项严格在所读段之外。
这保了整个已付短 normal 段，不仅是其首系数。

原 $J\in t^2$，而同修正注给 $t\mid R$、$t^2\nmid R$。
所以 $t\mid R_F$、$t^2\nmid R_F$，并且两者的
$t^1$ 来源多项式完全相同。
又 $F(0,Y)\ne0$，原 $t$-Gauss 除法使 (4) 进一步写成
$$
\boxed{R_F=tF\,H_*}
\tag{10}
$$
的真实整局部因子商，且原全部十九角成员性仍由 $R_F\in\mathcal W_D$ 支付。

将 (9)、(6)、(7) 代入 (10)，前述同修正注(12)–(17)的证明逐字适用。
特别
$$
H_*|_C
=-\frac{11C_0u_0^4}{a t_1e_0}w^{2h}+O(w^{2h+1}),
\tag{11}
$$
且 $H_*$ 的两条近支在至多二次常数域扩张后仍具有相同的
$(7\pm\sqrt{-17})/6$ 领先系数。
这些支属于**同一个原 $R_F$**，不是重新选的近似来源。

## 3. 指定有限类的条件非零

记 $d_D=B_D\cdot C$、$\kappa=C^2$。
原严格零纤维
$$
f_0=f-\sum_{j=1}^4E_{0,j}
$$
满足 $C\cdot f_0=3$。

$R_F$ 的实际截面除子含一次 $C$ 和至少一次 $f_0$。
由 (9) 的单位首项，$R_F$ 不含 $F^2$，所以除去这两部分后
不含 $C$；在原点与 $C$ 的接触由 (11) 恰为 $2h$。
全部其它有效分量与 nef 的原 $C$ 交数非负。因此
$$
\boxed{
\mathfrak o_D(R)=0
\quad\Longrightarrow\quad
d_D\ge\kappa+3+2h=\kappa+s+1.
}
\tag{12}
$$
扣除的是严格 $f_0$ 的三，不是整个总纤维的 $b$。

于是得到一个真正针对 (1) 指定修正的结论：
$$
\boxed{
d_D<\kappa+s+1
\quad\Longrightarrow\quad
\mathfrak o_D(R)\ne0
\quad\text{对每个满足 (1) 的同源 }R.
}
\tag{13}
$$
这没有说 (1) 不可能；它只排除了对该 $R$ 作
$\mathscr V_1+\mathscr J_3$ 的全球零类归一化。

若原 quartic 余乘子的零 charge 不恒为零，
两 charge 连接核证明已付全部 $D$ 的全球连接核消失。
在这个准确范围，(13) 还迫
$$
\operatorname{im}(R\to H^0\mathscr T_D)\ne0
$$
于至少一个真实底纤维。
不能进一步指定它必在 $t=0$，也不能把整个有限层换成那个二／三行商。

## 4. 同一第二页不能借改变 R 绕过

固定 (1) 的 $P^{\rm fact},R,S$。
若以同一原来源向量 $Y$ 改变 $R$，并仍要求存在同源 $Z$ 使
$$
M^{\rm orig}(P^{\rm fact}+p(R+Y)+p^2(S+Z))\in p^3,
$$
则差式必给
$$
\bar Y\in K_1,\qquad
\boxed{\beta_1(\bar Y)=0\text{ 于 }\operatorname{coker}\bar M.}
\tag{14}
$$
第一项只保原 $p^2$；第二项才是同一个第二页还能补偿的完整条件。
不可仅检查 $\Pi(Y)$ 或一条 $\Lambda_0$。

设 $\mathcal K_2=\ker(\beta_1:K_1\to\operatorname{coker}\bar M)$。
在 (13) 的数值范围，准确有
$$
\boxed{
0\notin \mathfrak o_D(R)+\mathfrak o_D(\mathcal K_2).
}
\tag{15}
$$
否则某个真实 $Y\in\mathcal K_2$ 可由同一 $Z$ 支付 (14)，
得到另一个通过 (1) 且满足零类 (3) 的修正，违背 (12)。

因此若某个 $Y\in K_1$ 仅在原第一层把
$R+Y$ 送进 $\mathscr V_1+\mathscr J_3$，
则在 (13) 范围中它必须具有非零的完整首 Bockstein 类；
不能以其有限纤维作用已经合适而省掉第二页。

式 (15) 仍没有算出 $\mathcal K_2$ 或 $K_1$ 的有限像，
没有证明这个仿射类与原全部来源矛盾，
也没有把 (12) 当成当前所有临界参数都违反的门。
原完整 $R,S$、实际四中央以及剩余 normal/carry 继续保留。

## 5. 同一个 quartic 截面的全预算与数值可读门

本节仍保正文全部条件。令 $j$ 为原残截面
$P^{\rm fact}/F^4$ 沿严格负水平 $H_-$ 的准确零阶。
[原负水平全范围](2026-11-16-r872-quartic-negative-horizontal-range-and-double-vanishing.md)
已经证明 $j\in\{0,1,2\}$。记 $z_-=C H_-$。
原截面的有效零除子准确包含
$
4C+3f_0+jH_-.
\tag{16}
$
这里仍只扣严格 $f_0$；原十九角不允许将它换成总纤维。
三种分量互不相同；在未吹起的零纤维一般点，
原 $t^3$ 给三，而 $F(0,Y)\ne0$、$q(0,1)\ne0$ 保该判断。

[R680](../results/R680-original-nineteen-angle-root-energy-and-mixed-charge-restriction.md)
的原 $B_D$ 为 nef，且其完整十九重数表给
$B_D f_0=2$、$B_D H_-=4$。
[R815](../results/R815-complete-original-mori-nef-cones-and-s-fibration.md)
给原几何整非边界 $C$ 为 nef。因此将 (16) 分别与两者相交，得到
$
\boxed{
4d_D+6+4j\le B_D^2,\qquad
4\kappa+9+jz_-\le d_D.
}
\tag{17}
$
特别还有准确的联合预算
$
\boxed{16\kappa+42+4j(1+z_-)\le B_D^2.}
\tag{18}
$
未计入的其它有效分量均保在余除子中，由 nef 性支付它们的非负交数。

若同一个 $R$ 满足完整零类条件，则正文 (12) 与 (17) 给
$
\boxed{
\mathfrak o_D(R)=0
\quad\Longrightarrow\quad
B_D^2\ge4\kappa+4s+10+4j.
}
\tag{19}
$
零链亏量三使 $b\ge3$，且 R815(33a) 给 $\kappa\ge6b-9$。
故还有完全整数的必要门
$
\boxed{B_D^2\ge4s+24b+4j-26.}
\tag{20}
$
特别 $B_D^2<4s+46$ 时，任何通过原完整 $p^3$ 的同修正
都满足 $\mathfrak o_D(R)\ne0$。

这些式子使用 R680(7) 的实际整数自交
$
B_D^2=4D^2+2D\bigl(2\lfloor D/2\rfloor+4\bigr)
-\sum_{i,a}\nu_{i,a}(D)^2,
\tag{21}
$
其中 $\nu_{i,a}(D)$ 是该文的全部十九重数。
有限参数不可将 (21) 替成仅主项的近似。

## 6. 原 ODE 使零类反门覆盖整个原临界区间

当前实际轴与原低轴 $\rho=d\Theta^{17}$ 的首差从 $w^{s-4}$ 起。
本窗严格有 $h<s-4$，且 $t(w)/w$ 为单位。
所以同一个 $F$ 在 (1) 的接触 $h$ 也是
$F(t,\rho)$ 的准确接触；没有把实际高轴替到其未获许可的高阶。

R680(15)–(20) 的原 Euler forcing 在 $C$ 上非零，
其全极帽为 $3C+L$，且 $LC\le8b$。
原点处 $EF$ 为单位，故物理支无判别式损失；该 forcing
在此有至少 $h$ 阶零。于是
$
\boxed{h\le3\kappa+LC\le3\kappa+8b.}
\tag{22}
$
只读取原共振前长度；其它支的交数、判别式及全部固定角
并未删掉，只在必要下界中不再计入。

将 (22) 与 (19) 联立，并用 $s=2h+2$，逐步有
$
3B_D^2\ge12\kappa+12s+30+12j
\ge4h-32b+12s+30+12j
=14s+26+12j-32b.
$
由于 $4b\le D$，得到不再依赖未知因子自交的必要门：
$
\boxed{
\mathfrak o_D(R)=0
\quad\Longrightarrow\quad
14s\le3B_D^2+32b-26-12j
\le3B_D^2+8D-26-12j.
}
\tag{23}
$
因此
$
\boxed{
14s>3B_D^2+8D-26
\quad\Longrightarrow\quad
\mathfrak o_D(R)\ne0
}
\tag{24}
$
对当前窗口内每一个原 $F$ 及每一个通过完整 (1) 的同 $R,S$ 都成立。

主项的含义可以严格单独表述：若一列当前原输入有 $D\to\infty$，
且 $\liminf p/D^2>141/28$，则 R680 的
$B_D^2=(47/12)D^2+O(D)$ 使 (24) 从某项起成立。
特别原 $p/D^2\to47/8$ 的临界列满足这个严格反门。
这是对全因子范围的渐近结论，不是目标素数扫描。

在 (24) 内，正文 (15) 的同第二页仿射类准确不含零；
当 $j=0$ 时，已付的全球连接核消失还迫至少一个真实有限纤维读数非零。
仍不能指定它在物理 $t=0$，不能从这里推出完整 $p^3$ 不存在，
更不能把这一步称为主课题的中央非零。
下一步仍是原 $K_1$ 的所有高前缀与
$\mathfrak o_D(\ker\beta_1)$ 的实际联合像。

无新增数学数值运行。
