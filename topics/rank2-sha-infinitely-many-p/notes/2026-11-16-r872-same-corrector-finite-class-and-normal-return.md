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

无新增数学数值运行。
