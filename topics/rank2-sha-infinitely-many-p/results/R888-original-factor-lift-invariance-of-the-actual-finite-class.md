# R888. 原 quartic 因子化整提升的完整有限类不变性

日期：2026-11-16。**状态：以下规范不变性已证明；没有因此获得指定有限类为零，也没有授权任意选择因子修正。**

本注接[第二核的有限类及首来源刚性](../notes/2026-11-16-r872-second-kernel-finite-class-and-first-source-rigidity.md)，保持该文的原 $\mathcal W_D$、全部十九角、$\Gamma_4$、$L=E+40$、同一个模 $p$ 因子 $F$ 和
$$
\mathfrak o_D(R)\in
\mathcal W_D/(\mathscr V_1+\mathscr J_3).
$$
只比较 R491 已经实际返回同一原整来源的两种因子化提升。

设
$$
P^{\rm fact}=t^3\widetilde F^{\,4}\widetilde q,\qquad
P^{\prime\rm fact}=t^3\widetilde F'^{\,4}\widetilde q'
\quad\text{均属 }\mathcal W_{D,\mathcal O},
$$
且
$$
\widetilde F'=\widetilde F+pA,\qquad
\widetilde q'=\widetilde q+pB
$$
在同一原系数环中成立。
允许原已付的固定 $d$ 分母；不要求 $A,B$ 各自属于某个免费新增来源。
两者具有同一个模 $p$ 原来源 $t^3F^4q$。

原显示系数格为自由整格，且其约化基在原有理函数域中独立。
故
$$
\Delta=\frac{P^{\prime\rm fact}-P^{\rm fact}}p
\in\mathcal W_{D,\mathcal O}.
\tag{1}
$$
这里使用的是原来源系数的整除，未饱和物理 $M$ 的像。
直接展开给
$$
\boxed{
\bar\Delta=t^3\bigl(4F^3q\,\bar A+F^4\bar B\bigr)
\in\mathscr V_3\subset\mathscr V_1 .
}
\tag{2}
$$
因此
$$
\boxed{\mathfrak o_D(\bar\Delta)=0.}
\tag{3}
$$

若原同一个整向量写成
$$
X=P^{\rm fact}+pR+p^2S,
$$
则准确改写为
$$
X=P^{\prime\rm fact}+p(R-\Delta)+p^2S .
\tag{4}
$$
$\Delta$ 在 (1) 中取完整整商，所以 (4) 是实际恒等式；
没有丢掉其下一位或另选一个 $S$。
所有原 $M$ 行、三个十三行带及下一精度因此逐字相同。
由 (2)–(3)，
$$
\boxed{\mathfrak o_D(\overline{R-\Delta})
       =\mathfrak o_D(\bar R).}
\tag{5}
$$
又原 $\mathscr V_3$ 的零角下界使它的残因子含 $t^2$，
所以特别
$$
\boxed{[t](\overline{R-\Delta})=[t]\bar R.}
\tag{6}
$$
在当前显示的整展开中 (2) 本身还有 $t^3$；
(6) 仅需前述原因子格的已付 $t^2$ 门，故不依赖额外局部换框。

最后核原 normal 和 $\xi$ 的变化。
在同一 $C$ 上，(2) 给
$$
\bar\Delta|_C=(E\bar\Delta)|_C=(E^2\bar\Delta)|_C=0,
$$
$$
\boxed{
(E^3\bar\Delta)|_C=24t^3q\,e^3\,\bar A|_C,\qquad e=(EF)|_C .
}
\tag{7}
$$
所以已付的 $R|_C$、$ER|_C$、$E^2R|_C$ 段保持，
第三 normal 改为
$$
(E^3(R-\Delta))|_C
=(E^3R)|_C-24t^3q\,e^3\,\bar A|_C .
\tag{8}
$$
若原因子沿实际轴记成
$\widetilde F(t,g)=w^hu+p\xi$，
新提升的相应项为 $\xi+\bar A(t,g)$。
在原第三短窗模 $w^\ell$ 内，$\bar A(t,g)$ 与
$\bar A|_C$ 的差从 $w^h$ 起，而 $\ell<h$；
因此 (8) 正是原
$-24t^3q\,\xi e^3$ 项的同源变化。
不能一面改变因子提升，一面保持旧 $\xi$ 不动。

本结论只比较两种已经合法返回原 $\mathcal W_D$ 的提升。
它不声称任意 $\bar A,\bar B$ 可实现，不把 $\xi$ 视为自由变量，
也不改变 $\mathfrak o_D(R)$ 对其余真实 $K_2$ 修正的未知仿射像。
无数学数值执行。
