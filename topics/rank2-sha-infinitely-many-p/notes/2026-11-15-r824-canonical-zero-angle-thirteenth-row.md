# R824 增补：原二次零角帽在第十三行的真实单位左配对

日期：2026-11-15。**状态：以下原完整四块的首 Bockstein 排除已证明。**

本说明加强 R824 的十三行 fringe：在整个相对来源的真实零角像仍为
$\langle1,Y,Y^2\rangle$ 的范围，第十三行本身也产生单位左配对。
这里 $Y=\rho$、$\mathcal EY=Y$；若改用 $\Theta$，三项是
$1,\Theta^{17},\Theta^{34}$，不是 $\Theta$ 的二次多项式。

结论严格限于上述实际零角帽。仅仅知道所有列有共同 $G_0$，
不足以对 R824 的任意扩充 $\mathscr W_{\rm act}$ 使用本增补。

## 1. 完整来源与真实仿射修正

保持 R824 的全部规范：
$$
p=6s-1>211,\qquad \ell_0=\ell+13,\qquad
1\le\ell<s-13,\qquad a\in\mathcal O^\times,
$$
$$
\mathcal EG_0=40G_0,\qquad
G_0(t(w),\vartheta(w))=w^{13}g_0(w),\qquad g_0(0)\in\mathcal O^\times.
$$
不删除原 $P_{134}$、普通单位、四十 charge 或任何一条十三行带。

设实际相对整格 $\mathscr W$ 满足
$$
\boxed{P(0,Y)\in\mathcal O[Y]_{\le2}\quad(P\in\mathscr W).}
\tag{1}
$$
原完整 canonical $\mathcal W_D$ 逐列满足 (1)：其 $n\ge3$ 列都含
$t^{\lfloor(n+1)/4\rfloor}$，而 $n=0,1,2$ 的零角像分别为
$1,Y,Y^2$ 的倍数。
若加入混合列，必须逐列重新核 (1)，不能只凭共同导子推断。

取一份真实首核
$$
\bar P=t^rF^4Q,\qquad
F(0,1)=0,\quad (\mathcal EF)(0,1)Q(0,1)\ne0,
$$
并令 $h=\operatorname{ord}_wF(t(w),\bar\vartheta(w))$。
首先，(1) 已迫
$$
\boxed{r\ge1.}
\tag{2}
$$
否则 $\bar P(0,Y)$ 在 $Y=1$ 有准确至少四阶零，
而且不是零级数；非零二次多项式不可能满足这个条件。

取任意实际系数提升 $P_b\in\mathscr W$，
并取 R824 的整因子提升，写
$$
G_0P_b=G_0t^r\widetilde F^4\widetilde Q+pG_0R_b.
$$
并不假设因子乘积本身属于 $\mathscr W$。
因为 $r\ge1$，它的零角值在特征零中也是零；
因此
$$
\boxed{
R_b(0,Y)=P_b(0,Y)/p\in\mathcal O[Y]_{\le2}.
}
\tag{3}
$$
此处 $\bar P_b(0,Y)=0$ 保证系数可整除以 $p$。
所有允许的其它首次修正是 $R_b+\mathscr W$，
所以整个真实仿射修正的零角仍满足 (1)。
这一步避免把因子整提升是否保持全部角帽当作隐含假设。

## 2. 第十三行的全首像左泛函

对 R824(9) 的四个完整物理块，令
$$
\pi_j=[w^{13}]\text{第 }j\text{ 块},\qquad0\le j\le3 .
$$
这些行全部存在：$s>35$，且 $\ell_0\ge14$。
模 $p$ 时，任意完整列 $G_0P$ 给
$$
\pi_j\overline{\mathfrak M}_4(G_0P)
=g_0(0)\frac{a^j}{j!}
\bigl((\mathcal E+40)^jP(0,Y)\bigr)_{Y=1}.
\tag{4}
$$
全部 $p\mathscr S$ 进位在首像约化中为零；
它们在下一节首商中仍完整保留。

由于 (1) 的三个 $\mathcal E$ 特征是 $0,1,2$，
准确多项式
$$
(T-40)(T-41)(T-42)
=T^3-123T^2+5042T-68880
$$
杀掉全部零角列。故
$$
\boxed{
\lambda=
6a^{-3}\pi_3-246a^{-2}\pi_2
+5042a^{-1}\pi_1-68880\pi_0
}
\tag{5}
$$
在整个原 $\overline{\mathfrak M}_4$ 像上为零。
由 (3)，它也杀掉实际因子提升产生的仿射基项。
这不是只对 $F$ 倍或 $F^2$ 倍修正成立的左行。

## 3. 贴边四次幂给准确单位值

现在取实际贴边
$$
\boxed{r+2h=s.}
\tag{6}
$$
在 R824 的完整物理指数中，这正是
$k=r+13+2h-s=13$。
写原实际轴上的
$$
f=\widetilde F(t(w),\vartheta(w))=w^hu+p\xi,\qquad
e=(\mathcal E\widetilde F)(t(w),\vartheta(w)),
$$
$$
G_0t^r\widetilde Q=w^{r+13}C(w),
\qquad C(0)u(0)e(0)\ne0.
$$
这些都是原真实单位；$\xi$ 没有改选或删除。

直接在完整四块取首次整商。
本原项的第 $i$ 个 Euler 导数，其最低 $p\xi$ 项从
$w^{r+13+(3-i)h}$ 起。
因此对 $i\le2$ 不进入第十三行；对 $i=3$ 亦从
$r+13>13$ 起。
其它 cofactor、$\mathcal E^jF$ 的高项只会提高这些阶。

前三块的首次 carry 分别读取未除 $p$ 的
$\Phi_0$、$\Phi_1$ 在 $s+13$ 的系数。
它们的起阶分别是
$s+13+2h$、$s+13+h$，故这些读数为零。
末块的 carry 则读取
$$
[w^{s+13}]\bar\Phi_2
=12C(0)u(0)^2e(0)^2.
$$
其系数是 $pa^2/2$。以 $\beta_{\rm fact}$ 记因子整基项的首次商，准确有
$$
\boxed{
\pi_0\beta_{\rm fact}=\pi_1\beta_{\rm fact}=\pi_2\beta_{\rm fact}=0,\qquad
\pi_3\beta_{\rm fact}=6a^2C(0)u(0)^2e(0)^2.
}
\tag{7}
$$
真实系数提升的首次商为
$\beta_b=\beta_{\rm fact}+\overline{\mathfrak M}_4(G_0\bar R_b)$。
其四个单独坐标未必仍满足 (7)，但 (3)、(5) 保证
$\lambda(\beta_b)=\lambda(\beta_{\rm fact})$。
所有更高 $p^2$、$p^3$ carry 在首次商模 $p$ 中确实消失，
没有提前删除原目标行。

合并 (5)、(7) 得
$$
\boxed{
\lambda(\beta_b)=\lambda(\beta_{\rm fact})
=36a^{-1}C(0)u(0)^2e(0)^2\in k^\times .
}
\tag{8}
$$
所以 (6) 的这份原首核，在同一完整来源格中不能提升到模 $p^2$。
这是原首余核中的实际非零类，不只是沿某一形式分支的非零值。

## 4. 准确加强及界限

R824 已排 $0\le k<13$；本增补在 (1) 的来源范围再排 $k=13$。
所以该范围内任何可提升的四次幂候选必须满足
$$
\boxed{r+2h\ge s+1.}
\tag{9}
$$
(9) 不是充分条件；其它分支值、全部高尾和同一后续修正仍然保留。
本增补也没有证明四条完整中央零会产生这种首核，
没有把第三中央精度改成四块精度，
更没有把四次幂族的排除当作整个原核的排除。

依赖：
[R824](../results/R824-original-quartic-first-correctors-and-native-central-schur.md)；
[R335](../results/R335-full-integral-canonical-conductor-and-exact-relative-source.md)的完整 canonical 列；
[R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)的原四块规范。

全文为原完整行的符号计算，无新增数学执行或生成数据。
