# R918 — 原稳定方向的十三带单位行与 native 端点值

日期：2026-11-16。**状态：以下同原来源的完整十三带读取、负 fringe 单位行和 native 端点条件已证明。未排除整个非稳定核，也未判定原仿射第二／第三页；主目标仍未完成。**

本篇接 R916 的唯一可能稳定方向，真正读取原首 Bockstein。
在 $-13\le r+2h-s<0$ 时，第一带和第三带的一个明确卷积组合
对该方向取单位，因此完整首 Bockstein 在稳定部分单射。
在边界 $r+2h=s$，同一个 native 行强制一个非零的高值系数；
更高接触时则迫该值再深一位。
全部结论使用原 $w^{13}$、完整实际轴和同一个余因子，未选择新来源或新高轴。

## 1. 原稳定来源与同一个物理矩阵

保持
[R916](R916-original-special-fiber-stable-kernel-and-unique-prefix-test.md)
的全部条件和真正稳定部分 $K_\infty$。
若该空间为零，以下结论空真。
否则令 $n\in\{1,\ldots,5\}$ 为唯一允许特征值，并取同一个原
$G\in K_\infty$。记其规范标量为 $\alpha=a(G)$，则
$$
\boxed{(\mathcal E-n)G=\alpha F^3.}
\tag{1}
$$
在 $K_\infty$ 上，$\alpha=0$ 当且仅当 $G=0$。
R916 的归一候选就是 $\alpha=1$。
这里的 $\alpha$ 不与实际 Gaussian 单位 $a$ 混用。

原来源为
$$
Y_G=t^r qG\in\overline{\mathcal W_D},\qquad
q=q_{\rm src},\qquad q(P)\ne0,
\quad \mathcal E=Y\partial_Y.
\tag{2}
$$
取 Hasse 对齐后的原完整矩阵及实际轴 $g^\flat$，简记 $g$。
令
$$
\mathcal U(w)=c_*U_0^\flat(w)\in k[[w]]^\times,\qquad
t(w)=t_1w+O(w^2),\quad t_1\ne0,
$$
$$
F(t(w),g(w))=w^hu(w),\quad u_0=u(0)\ne0,\quad
e_0=(\mathcal EF)(P)\ne0.
\tag{3}
$$
原总 charge 四十的实际读取准确为
$$
\boxed{
W_j(Y_G)=
\mathcal U(w)t(w)^r
\bigl[(\mathcal E+40)^j(qG)\bigr](t(w),g(w)).
}
\tag{4}
$$
原 $P_{134}$、全部固定载体和十九角都在 (2)–(4) 中。
不将 $\mathcal U$ 设为一，也不遗漏 $\mathcal E q$。

沿用 R907/R914 的长度
$$
T=s-r-13,\qquad T-h>\kappa,\qquad h<T\le2h,
\qquad T-h\le L\le h.
$$
置
$$
J=s-r=T+13,\qquad \delta=r+2h-s=2h-J.
\tag{5}
$$
因此
$$
\boxed{\delta\ge-13.}
\tag{6}
$$
原强窗有 $h>13$、$T>4$。
$G$ 的前三区相对 Euler 行消到 $T$；
由 (1)，其第三行实际上从至少 $h$ 开始。
所以 (4) 中 $W_0,W_1,W_2$ 从至少 $r+T=s-13$ 开始，
$W_3$ 从至少 $r+h>4$ 开始。

记原首 Bockstein 为
$$
\beta_1:K_1=\ker\overline M^{\rm orig}\longrightarrow
\operatorname{coker}\overline M^{\rm orig}.
$$
(2) 是已经在原 $K_1$ 中的同一个来源。
下文十三带行及 native $\Lambda_0$ 都杀
$\operatorname{im}\overline M^{\rm orig}$，
所以它们对 $\beta_1(Y_G)$ 的读取不依赖整 lift 的选择。
只对这些显示行给条件时，不声称已解全部 $\beta_1=0$。

## 2. 三条真实十三带只用同一值尾和一个固定 normal 项

令
$$
D_n=\mathcal E+n+40.
$$
从 (1) 逐项展开原 (4)，得
$$
\begin{aligned}
W_0&=\mathcal U t^r qG,\\
W_1&=\mathcal U t^r
       \bigl((D_nq)G+\alpha qF^3\bigr),\\
W_2&=\mathcal U t^r
       \bigl((D_n^2q)G+
       \alpha(2\mathcal E+n+80)q\,F^3+
       3\alpha qF^2e\bigr).
\end{aligned}
\tag{7}
$$
所有量先在同一个源端计算，再代入同一个实际 $t(w),g(w)$。

原三 carry 注的首带公式为
$$
[\epsilon^jw^i]\beta_1(Y_G)
=\frac{a^{j-1}}{(j-1)!}
\left([w^{s-13+i}]W_{j-1}
       +H_p[w^{i-9}]BW_j\right),
\quad 1\le j\le3,\quad0\le i\le12.
\tag{8}
$$
其中 $a\in k^\times$ 是同一个 Hasse 对齐 Gaussian 单位。
(8) 本来在实际参考上书写。
本源的 $W_1,W_2,W_3$ 在所有阶 $\le4$ 均为零，
故显示的 $H_p$ 项全部为零。
从参考改为完整实际轴时，一次差从 $w^{s-4}$ 起，
在 $\le s$ 的读取中只会乘 $W_1,W_2,W_3$ 的 $\le4$ 行；
它们同样为零。二次差从 $w^{2s-8}$ 起，已高于 $s$。
这是原完整 charge 展开的运输，包含公共载体随高轴的变化。
所以此处可准确使用 (4) 的实际 $W_j$，不是把参考 $g_0$ 冒充实际 $g$。

将三个原行向量写成
$$
\mathfrak b_j(G;w)=
\sum_{i=0}^{12}[\epsilon^jw^i]\beta_1(Y_G)\,w^i
\quad\bmod w^{13}.
$$
定义同源级数
$$
\zeta_G(w)=w^{-T}G(t(w),g(w)),
$$
$$
C_j(w)=
\mathcal U(w)\left(\frac{t(w)}w\right)^r
(D_n^jq)(t(w),g(w))\quad(j=0,1,2).
\tag{9}
$$
$C_0$ 是单位。注意 $\zeta_G$ 的十三项是实际值尾，
不能独立于 R916 的唯一 $G$ 另选。

因为
$$
r+3h=s+\delta+h>s
$$
由 $\delta\ge-13,h>13$ 保证，
(7) 中所有 $F^3$ 项都不进入这三条带。
$F^2e$ 则必须保持。
由 (7)–(9) 得完整向量恒等式
$$
\boxed{
\begin{aligned}
\mathfrak b_1&=C_0\zeta_G,\\
\mathfrak b_2&=aC_1\zeta_G,\\
\mathfrak b_3&=\frac{a^2}{2}
 \left(C_2\zeta_G+
       3\alpha w^{13+\delta}C_0u^2e\right)
\end{aligned}
\quad\bmod w^{13}.
}
\tag{10}
$$
这是同一个 $G$ 的三条原十三带，不是环境可任取的三个向量。

## 3. 负 fringe 给一个明确单位行

设
$$
-13\le\delta\le-1,\qquad i_\delta=13+\delta\in\{0,\ldots,12\}.
$$
在原首 Bockstein 目标上定义有限线性行
$$
\boxed{
\mathscr L_{n,\delta}=
[w^{i_\delta}]
\left(
\mathfrak b_3-
\frac{a^2}{2}\frac{C_2}{C_0}\mathfrak b_1
\right).
}
\tag{11}
$$
比值 $C_2/C_0=((D_n^2q)/q)(t(w),g(w))$ 只读所需的有限前缀。
它是同一个原 $q$ 和实际轴给定的系数，不是可调参数。
(11) 仅组合原已有十三带行，故仍杀原模 $p$ 像。

由 (10)，全部 $\zeta_G$ 准确相消，留下
$$
\boxed{
\mathscr L_{n,\delta}\,\beta_1(Y_G)
=\frac{3a^2}{2}\,
\mathcal U(0)t_1^rq(P)\,u_0^2e_0\,\alpha.
}
\tag{12}
$$
显示系数是单位。这一步不先假设第一带为零，
也没有漏掉余因子的 Euler 导数。

**定理 1。** 在 (6) 的负 fringe 范围，
$$
\boxed{
K_\infty\cap
\ker\bigl(\beta_1\circ(G\mapsto q t^rG)\bigr)=0.
}
\tag{13}
$$
因此原完整首 Bockstein 在这个实际稳定部分上单射。

证明是 (12) 与 $\alpha$ 在 $K_\infty$ 上单射。
(11) 不杀全非稳定来源的首 Bockstein，
所以 (13) 不能改写成整个 $K_1$ 或整个四块核已无提升。

## 4. 非负边界：三条带准确等价于值加深十三位

以下取 $\delta\ge0$。
此时 (10) 的最后 normal 项在模 $w^{13}$ 中为零。
由于 $C_0$ 为单位，准确有
$$
\boxed{
\mathfrak b_1=\mathfrak b_2=\mathfrak b_3=0
\quad\Longleftrightarrow\quad
G(t(w),g(w))\in w^Jk[[w]].
}
\tag{14}
$$
这是对三条首 carry 的充要条件，不是对完整首 Bockstein 的充要条件。
原 $J=T+13$ 是由这十三条实际行新支付的长度，
未将物理 $M$ 的旧读取窗直接替换成相对 $J$。

例如原三个指定尾
$$
\Pi_\tau(Y_G)=[w^{s+\tau-4}]W_2(Y_G),
\qquad\tau=1,2,3,
$$
在本稳定部分准确读为
$$
\boxed{
\Pi_\tau(Y_G)=[w^{\tau+9}]C_2(w)\zeta_G(w).
}
\tag{15}
$$
这里的 $\Pi$ 仍是原第二长块的三条尾，未混作第三 Euler 短行。
(15) 只读 R916 已确定候选的真实十三项。
通过 (14) 后它们为零；
这也与原一般首 carry 结论相容，不把该已知消失另当全像满射。

## 5. 同一个 native 行在边界处给真单位高值

本节增加原 R797 子类中的准确零纤维余因子
$$
\boxed{q(0,Y)=c_qY,\qquad c_q\in k^\times.}
\tag{16}
$$
它仅固定零纤维的整个多项式，未要求 $q$ 在全局只有一个 charge。
特别不能在全式中写 $\mathcal Eq=q$。

仍保 $\delta\ge0$，并假设同一个 $G$ 已通过 (14)。
定义其下一实际值
$$
v_G=[w^J]G(t(w),g(w)),\qquad
C_*=\mathcal U(0)t_1^r c_q\in k^\times.
\tag{17}
$$
原 native 行为
$$
\Lambda_0=-68880[w^{13}]
+\frac{5042}{a}[\epsilon w^{13}]
-\frac{246}{a^2}[\epsilon^2w^{13}]
+\frac6{a^3}[\epsilon^3w^{13}].
\tag{18}
$$
R865 的完整实际规范给
$$
\Lambda_0\beta_1(Y_G)
=\frac1a[w^s]\,
 \mathcal U t^r(3\mathcal E^2-6\mathcal E+2)(qG).
\tag{19}
$$
若用参考书写，本来出现的 $3H_p[w^4](BW_3)$
在本源上由 $W_3$ 的实际最低阶严格为零；
并非凭规范选择删除。

由 (1) 的同源 Leibniz 恒等式，
$$
\boxed{
\begin{aligned}
(3\mathcal E^2-6\mathcal E+2)(qG)
={}&\bigl((3(\mathcal E+n)^2-6(\mathcal E+n)+2)q\bigr)G\\
&+\alpha\bigl(6\mathcal Eq+(3n-6)q\bigr)F^3
+9\alpha qF^2e.
\end{aligned}}
\tag{20}
$$
原 $r+3h>s$ 排除第二行的 $F^3$ 项；
最后项仅在 $\delta=0$ 时进入 $w^s$。
第一项则由于 (14) 已将 $G$ 消到 $J$，
其非恒定乘子都不进入这个首未消系数。
(16) 给准确系数
$$
3(n+1)^2-6(n+1)+2=3n^2-1.
$$
因此
$$
\boxed{
\Lambda_0\beta_1(Y_G)
=\frac{C_*}{a}
\left((3n^2-1)v_G+
 9\alpha u_0^2e_0\,\mathbf1_{\delta=0}\right).
}
\tag{21}
$$
在 $n=1,\ldots,5$ 时，
$$
3n^2-1\in\{2,11,26,47,74\},
\tag{22}
$$
原 $p>211$ 下全部是单位。
不是把未知的完整中央组合或 Fermat 商赋成单位。

**定理 2。** 对原稳定方向，完整 $\beta_1(Y_G)=0$ 必须满足：

- 若 $\delta=0$，
  $$
  \boxed{
  v_G=-\frac{9\alpha u_0^2e_0}{3n^2-1}.
  }
  \tag{23}
  $$
  非零稳定方向有 $\alpha\ne0$，所以其实际值阶恰为 $J=s-r$，
  不能继续把它消到 $J+1$。
- 若 $\delta>0$，
  $$
  \boxed{G(t(w),g(w))\in w^{J+1}k[[w]].}
  \tag{24}
  $$

两式都保同一个 R916 候选。
在 $\delta=0$，若还由原任务另行付得该值消到 $J+1$，
则该稳定方向与完整首 Bockstein 的交恰为零；
但本篇不为全部来源额外添加这个前缀。

## 6. 与同一曲线值、候选测试及后页的关系

(23) 不只是改变量后的虚值。
由 $(\mathcal E-n)G=\alpha F^3$ 和
$F(t,\psi e^z)=e|_C\,z+O(z^2)$，
有限 Taylor 逐项给
$$
G(t,\psi e^\eta)
=e^{n\eta}G|_C+O(t^{4h}).
\tag{25}
$$
更直接地，(1) 给 $(\mathcal E^jG)|_C=n^jG|_C$（$0\le j\le3$），
因此只需四项有限 Euler Taylor，所有分母都整除 $3!$。
这里不在正特征使用无限形式原函数。
当 $\delta\ge0$ 时 $J\le2h<4h$，
所以在 (14) 下 $G|_C$ 也消到 $J$，
并且它的第 $J$ 系数与 $v_G$ 相同（使用同一 $w$ 参数）。
因此 (23) 给这整个原限制截面的准确首系数。
若写 $\eta=\eta_hw^h+\cdots$，则 $u_0=e_0\eta_h$，
该首系数也等于
$-9\alpha e_0^3\eta_h^2/(3n^2-1)$。

对 R916 的唯一归一 $G_n=B_n+c(t)Y^n$，
(14)、(23)、(24) 是其原唯一前缀测试之后的额外确定行。
必须使用实际 $g^\flat$ 继续到 $J$ 或 $J+1$；
此处可已进入 $s-4$ 之后，不能以旧 $g\equiv\rho\bmod t^T$
替换高轴。R916 的全部十九角空间与唯一 $c(t)$ 都不改变。

本篇在 $\delta<0$ 给的 (11)–(13) 是实际首 Bockstein 单位子块；
在 $\delta\ge0$ 给的三带与 native 条件是显示行的完整读取。
剩余 $\beta_1$ 行、其它来源列、固定边界与 conductor、
原三条十三带以外的 native 商、第二／第三页、
同一个 $P,R,S$ 和 $K_{\rm corr}/H_{\rm corr}$ 全部保留。
不能把这些显示行分别可解当作原全部页可解，
也不能把一个稳定方向被排除当作非稳定 forcing 已关闭。

依赖：R916 的真实唯一稳定方向；
R828 的完整三 carry 递推；
R865 的实际完整 native 读取；
R872 的原带行与同一修正规范。
本篇为精确手证，没有新数学运行或数据。
