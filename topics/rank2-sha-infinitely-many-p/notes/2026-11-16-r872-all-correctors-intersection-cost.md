# R872 短推论：全部同一首修正的严格零纤维交数成本

日期：2026-11-16。**状态：已证明；只给全 $R$ 的必要交数门，不判原尾泛函或完整第二、第三页。**

保持[同一第二页修正的末行和剩余分支](2026-11-16-r872-factored-corrector-last-row-and-residual-branches.md)(1)–(6)的全部实际来源、因子化提升和精度：$r=3,\tau=1,s=2h+2$，同一个
$P^{\rm fact}+pR+p^2S$ 通过原全 $M/p^3$。特别所有十九角、三个十三行带及第四短块保持。

令 $C$ 是 $F$ 在原 $X$ 上的几何整严格变换，
$\kappa=C^2\ge1$，$\mathcal B_D$ 是同一个 $\mathcal W_D$ 的原来源类。
则任何这样的首修正都必须满足
$$
\boxed{\mathcal B_D\cdot C\ge s+2=2h+4.}
\tag{1}
$$

**证明。** 引用上述证明的(9)–(10)，
$$
t\mid R,\quad t^2\nmid R,\quad
\operatorname{ord}_P(R|_C)\ge s,\quad
ER|_C=-\frac{11C_0u_0^4}{a}w^{s-1}+O(w^s).
\tag{2}
$$
原零角 Gauss 值为 $v_0(F)=-3$。
[R815](../results/R815-complete-original-mori-nef-cones-and-s-fibration.md)(5)、(36)给严格零纤维
$$
f_0=f-\sum_{j=1}^4E_{0,j},\qquad C\cdot f_0=3.
\tag{3}
$$
$R$ 的实际截面零除子 $D_R\sim\mathcal B_D$ 含一次 $f_0$。
在 $P$ 处，它的剩余截面在单位框下是 $R/t$；
这并非断言 raw 除 $t$ 已删除整个总纤维或所有例外分量。

若 $F\nmid R$，则 $D_R-f_0$ 不含 $C$。
其与 $C$ 的原点交数由 (2) 至少为 $s-1$，
因为 $t$ 是 $C$ 在 $P$ 的参数。
其余局部交数非负，因此
$$
\mathcal B_D\cdot C-3=(D_R-f_0)\cdot C\ge s-1.
\tag{4}
$$
这就是(1)。

若 $F\mid R$，前述平方排除保证 $C$ 的重数恰为一。
同一修正写为 $R=tFH$，已证明
$$
\operatorname{ord}_P(H|_C)=2h.
$$
因此剩余有效除子 $D_R-f_0-C$ 在 $P$ 与 $C$ 的交数至少为 $2h$，且不含 $C$。于是
$$
\mathcal B_D\cdot C\ge\kappa+3+2h
\ge 2h+4=s+2,
\tag{5}
$$
再次得到(1)。证毕。

在当前几何整、非边界因子范围，$\kappa\ge1$ 也无需额外猜测：
$C$ 为 R815 的 nef 曲线，$C\cdot f_0=3$，
而 $b=C\cdot f=\deg_YF\ge3$。
该文(33a)给
$\kappa\ge6b-9\ge9$。
若只在局部因子或未付几何整的其它范围工作，则仍须显式保留本推论的全局前提。

式(1)统一覆盖含与不含 $F$ 的全部真实 $R$。
它比只在原点读取 $R|_C$ 多保了严格零纤维与 $C$ 的另外两个交点成本，
但没有把 $\mathcal B_D\cdot C$ 的主阶从约 $4\kappa$ 降到
足以排除 $h/\kappa\approx4/3$。
原 $\pi_\tau(K_1)$、同 $R,S$ 的其它 normal 和 carry 仍未由此解决。
无数学程序运行。
