# R623 — 第二临界盘外的真实野域、对角原来源与中央原函数

日期：2026-11-14。**状态：已证明。**

R618 的第二 Gaussian 不能在跨过其临界半径后继续当作 Tate 单位。
本篇在这个新半径范围明确区分三个实际域：

- 两个 Gaussian 一起生成的辅助扩张，次数为 $p^2$；
- 完整原 sigma 所在的对角扩张，次数仍为 $p$；
- 只添第一个 Gaussian 的旧子域；它在此范围已不包含原 sigma。

七个原积分在新的整个 $p^2$ 域上仍代数独立。
但 R622 的两个中央投影原函数，无论原 $j$ 是否为零，
都已经属于实际对角域。因而新解析分解既不增加两条算术零，
也不能将两个中央投影算成这里新增的积分超越坐标。

## 1. 同一原 sigma 和真正可用的外盘

保持 R618 的
$$
p=6s-1>71,\quad d=p+1,\quad
S=p^{-p/(p^2-1)},\quad
R_2=p^{-(2p-1)/(p(p^2-1))},\quad
R_E=p^{-1/(p^2-1)}.
$$
取原
$$
c=[z^d]\log(\sigma/z),\qquad
a_2=[w^{ps}]\{\log(\sigma/z)-cw^s-\log U_0\},
\qquad w=z^6,
$$
其中 $U_0$ 是 R618 的实际整 Taylor 多项式。
已付
$$
v_p(c)=-1,\qquad v_p(a_2)=-2,\qquad
p^2a_2\equiv b^Lpc\pmod p.
\tag{1}
$$

原完整因子分解为
$$
\mathscr E_1=\exp(cz^d),\qquad
\mathscr E_2=\exp(a_2z^{pd}),\qquad
\sigma=zV\mathscr E_1\mathscr E_2.
\tag{2}
$$
R618 给某个 $R_+>R_2$，可共同缩小到 $R_+<R_E$，使
$$
V,V^{-1},\quad W=z^2x,\quad Y=-z^3y
\in\mathcal T_{R_+},
$$
且所用单位的 Gauss 范数为一。
这里
$$
\mathcal T_R=\mathbf C_p\langle z/R\rangle,\qquad
F_R=\operatorname{Frac}(\mathcal T_R),
\qquad R_2\le R\le R_+.
\tag{3}
$$
半径取在 $\mathbf C_p$ 的值群中。
所有域均通过实际原点 Laurent 展开嵌入
$\mathbf C_p((z))$，常数域为 $\mathbf C_p$。

以下只使用 (3) 的闭盘；不将 $V$ 免费延到 $R_E$。

## 2. 两个 p 次幂同在外盘，但两个原根都不在

一般地，若 $v_p(q)=-e$，则
$\exp(qz^N)$ 的精确半径为
$p^{-(e+1/(p-1))/N}$。
其临界加权系数沿 $k=p^j$ 的估值为 $1/(p-1)$，
故临界闭盘非 Tate。
R618 已对前两行支付这一计算；对后两行同用 Legendre 公式得到：

| 实际函数 | log 系数赋值 | 指数次数 | 精确半径 |
|---|---:|---:|---|
| $\mathscr E_1$ | $-1$ | $d$ | $S$ |
| $\mathscr E_2$ | $-2$ | $pd$ | $R_2$ |
| $\mathscr E_1^p$ | $0$ | $d$ | $R_E$ |
| $\mathscr E_2^p$ | $-1$ | $pd$ | $R_E$ |

每行在各自临界闭盘均非 Tate。
因为本篇 $R<R_E$，准确有
$$
\mathscr E_1^p,\mathscr E_2^p
\in\mathcal T_R^\times.
\tag{4}
$$
此表逐个陈述函数，不排除两个 $p$ 次幂的特殊乘积在 $R_E$
出现额外相消。

对 $0\le i,j<p$、$(i,j)\ne(0,0)$，置
$$
Z_{i,j}=\mathscr E_1^i\mathscr E_2^j.
$$
若 $i\ne0$，则第一指数仍有精确半径 $S$；
第二指数及其逆在闭 $S$ 上为 Tate 单位，
所以 $Z_{i,j}$ 精确半径仍为 $S$、闭 $S$ 非 Tate。
若 $i=0$，则 $j\ne0$，其精确半径为 $R_2$、闭 $R_2$ 非 Tate。

还须排除它们是 $F_R$ 中的有极点元素。
实际有
$$
DZ_{i,j}
=\{icd\,z^{d-1}+ja_2pd\,z^{pd-1}\}Z_{i,j}.
\tag{5}
$$
R588 的闭盘无极点引理在 (3) 同样适用：
若 $u\in F_R$ 且 $Du+qu=h$，$q,h\in\mathcal T_R$，
一个有限极点的导数产生不可相消的更高一阶极；
一元 Weierstrass 分解遂迫 $u\in\mathcal T_R$，
边界点也包括在内。

若 $Z_{i,j}\in F_R$，将该引理用于 (5)，便迫它属于
$\mathcal T_R$。这与上述 $S$ 或 $R_2$ 的闭边界失败矛盾。
因此
$$
\boxed{
\mathscr E_1^i\mathscr E_2^j\notin F_R
\quad(0\le i,j<p,\ (i,j)\ne(0,0)).
}
\tag{6}
$$

## 3. 完整两根扩张的次数准确为 p²

定义实际辅助域
$$
\mathcal K_R=F_R(\mathscr E_1,\mathscr E_2).
\tag{7}
$$
由 (4)，它是可分正规扩张；
系数域包含全部 $\mu_p$，Galois 群是
$\mu_p\times\mu_p$ 的子群，作用为
$$
(\zeta_1,\zeta_2):
(\mathscr E_1,\mathscr E_2)\longmapsto
(\zeta_1\mathscr E_1,\zeta_2\mathscr E_2).
$$
若该子群严格小于整个二维 $\mathbf F_p$ 向量空间，
则有非零特征 $(i,j)$ 在该子群上平凡。
相应的实际单项式
$\mathscr E_1^i\mathscr E_2^j$
就被整个 Galois 群固定，从而属于 $F_R$，
违反 (6)。
所以
$$
\boxed{
[\mathcal K_R:F_R]=p^2,\qquad
\operatorname{Gal}(\mathcal K_R/F_R)=\mu_p^2.
}
\tag{8}
$$
同时，$\mathscr E_1^i\mathscr E_2^j$、
$0\le i,j<p$ 是一个实际特征基。
这证明整个扩张，没有把两个单独的 degree-$p$ 断言相乘了事。

## 4. 原 sigma 只占对角 degree-p 子域

记
$$
\mathscr E_\Delta=\mathscr E_1\mathscr E_2,\qquad
K_R^\sigma=F_R(\mathscr E_\Delta).
\tag{9}
$$
(6) 与 $\mathscr E_\Delta^p\in F_R$ 给
$$
\boxed{[K_R^\sigma:F_R]=p.}
\tag{10}
$$
其固定群正是 $\{(\zeta,\zeta^{-1})\}$。
由 (2)，
$$
F_R(\sigma)=K_R^\sigma.
\tag{11}
$$
而且
$$
x,y,z\in F_R,\qquad
\zeta_\sigma=\frac{\sigma'}{\sigma}
=\frac1z+\frac{V'}V+cd\,z^{d-1}+a_2pd\,z^{pd-1}
\in F_R.
\tag{12}
$$
因此所有完整原 theta 多项式，包括
$S_{34},T_{72},S_{136}$，都在 $K_R^\sigma$ 中。
它们没有占用两条独立 Gaussian 特征。

在同一外盘，$\mathscr E_2\notin F_R(\mathscr E_1)$，
否则 (8) 的次数至多为 $p$。
于是
$$
\boxed{\sigma\notin F_R(\mathscr E_1).}
\tag{13}
$$
这说明旧 R588 的第一根域在跨过 $R_2$ 后不能原样充作
“包含完整 sigma 的域”。
正确的原来源域是 (9)，或把两个根都保留的 (7)。

这些都是实际解析域身份，不是新的整数来源格或免费的新坐标。

## 5. 七个原被积微分在完整 p² 域仍不精确

保持原零初值积分
$$
J_{4,j}=\int_0^z t^j f_4(t)\,dt\quad(j=0,1),
$$
$$
J_{1,j}=\int_0^z t^j f_1(t)\,dt\quad(j=0,\ldots,4),
$$
其中 $f_4=x\sigma^6$、$f_1=-xy\sigma^6$。
R588 已在同一个原模型证明：对任意非零常数组合
$\mathcal J$ 及任意 $C\in\mathbf C_p$，
$$
\mathscr E_1^{-6}(\mathcal J-C)\notin\mathcal T_S.
\tag{14}
$$
它使用原两个完整非中央 Stokes 行的单位矩阵；
没有假定任何指定中央值非零。

**定理 1。** 这七个被积函数的任意非零常数组合，
在 $\mathcal K_R$ 中以及其任何有限代数扩张中都没有原函数。

证明。由 (2)，
$$
D\mathcal J=\mathscr E_\Delta^6h,\qquad h\in\mathcal T_R.
\tag{15}
$$
两类 $h$ 分别由
$z^{4+j}WV^6$ 和 $z^{1+j}WYV^6$ 组成；
原点正则及全部固定因子都保留。

若 $v\in\mathcal K_R$ 是 (15) 的原函数，
取 (8) 中真正的特征 $(6,6)$ 投影。
导数与 Galois 作用交换，投影得到
$$
v_{6,6}=\mathscr E_\Delta^6u,\qquad u\in F_R,
$$
$$
Du+6\{cd\,z^{d-1}+a_2pd\,z^{pd-1}\}u=h.
\tag{16}
$$
$p>71$ 保该特征非零；它的 eigenspace 准确为显示的一维
$F_R$ 空间。
无极点引理给 $u\in\mathcal T_R$。

实际 Laurent 域的常数域没有增加，所以
$\mathcal J-\mathscr E_\Delta^6u=C$。
因此
$$
\mathscr E_1^{-6}(\mathcal J-C)=\mathscr E_2^6u.
$$
右边在闭 $S$ 是 Tate 元：$u$ 可限制到该盘，
而 $\mathscr E_2$ 在更大的 $R_2$ 开盘内解析。
这与 (14) 矛盾。
若有限代数扩张有原函数，取迹除以次数会给
$\mathcal K_R$ 中的原函数，仍矛盾。证毕。

这里的投影含 $1/p^2$；它仅用于域论证明，
没有被放入原整来源格。

## 6. 七塔独立性继续越过第二临界盘

实际积分扩张仍在 $\mathbf C_p((z))$ 中，
所以没有新常数。
应用 R575/R588 已完整证明的加性积分引理，
定理 1 给
$$
\boxed{
J_{4,0},J_{4,1},J_{1,0},\ldots,J_{1,4}
\text{ 在 }\mathcal K_R\text{ 上代数独立。}
}
\tag{17}
$$
原七个正幂规整塔 $V_{\ell,r}$ 与这些 $J$ 由
$F_R$ 上可逆的固定三角变换相连，
故 (17) 对 R583 的同一七个实际坐标成立。
尤其它们在实际对角子域 $K_R^\sigma$ 上仍独立。
这是把 R588 的解析基域真实推进到了第二临界盘外，
未把缺少第二根的旧域当作完整来源域。

对任何真正含塔的原多项式
$\Phi=P(S,T,V_{4,1},V_{4,2},V_{1,1},\ldots,V_{1,5})$，
原 R588 的闭 $S$ 非 Tate 结论仍保持。
更明确地，对任意整数 $a,b$，
$$
\boxed{
\operatorname{rad}(\mathscr E_1^a\mathscr E_2^b\Phi)=S,\qquad
\mathscr E_1^a\mathscr E_2^b\Phi\notin\mathcal T_S.
}
\tag{18}
$$
因为 $\mathscr E_2^b$ 及其逆在闭 $S$ 为 Tate 单位，
(18) 的闭边界正由 R588 的
$\mathscr E_1^a\Phi$ 结论运输；
所有因子在每个严格内盘解析，支付半径下界。
允许任意次数及依赖 $p$ 的常数系数，前提是正塔次数的实际系数
收集后至少一个非零。

(18) 只排除以这两个 Gaussian 因子扩大含塔原函数的半径；
它不把单函数远处的分母当成非空真前缀的首行。

## 7. 两个中央投影原函数却无条件已经在对角域

保持 R622 的完整原对象：
$$
\mathscr U_m(z)=\int_0^z A_m(t)\frac{dt}{t},
\quad m=34,72,\qquad
\Pi_0f=\frac1d\sum_{\xi^d=1}f(\xi z).
$$
R622 对某个共同外盘给实际 Tate 解
$\mathcal R_{m,2}(X)$，$X=z^d$，并证明完整恒等式
$$
d\,\Pi_0\mathscr U_m
=\exp(mcX+ma_2X^p)\mathcal R_{m,2}(X)-j_m.
\tag{19}
$$
必要时将 $R_+$ 同时缩小到两条来源的已付外盘，
仍保 $R_+>R_2$。
于是 (19) 直接给
$$
\boxed{
\Pi_0\mathscr U_{34},\ \Pi_0\mathscr U_{72}
\in K_R^\sigma
\quad\text{不论 }j_{34},j_{72}\text{ 是否为零。}
}
\tag{20}
$$
因为 (19) 右侧的指数正是 $\mathscr E_\Delta^m$，
其余为实际 Tate 系数和一个常数。

因此，仅证明这两个中央投影在这个外盘的原 sigma 域内，
不能检测原算术零。
准确零条件仍是
$\mathcal R_{m,2}(0)=j_m=0$；
R622 的零初值及完整 Newton 权都不可删除。
(20) 也不能与 (17) 混淆：七个旧积分的非中央行仍在，
而 $\Pi_0$ 正杀掉了用于 (14) 的那些行。

## 8. 对原全格成本的确切含义

R618 的去 Gaussian 普通部分有
$$
v_p(g_n)\ge-\lfloor6n\tau_2\rfloor,\qquad
\tau_2=\frac{2p-1}{p(p^2-1)}=O(p^{-2}).
$$
所以其逐系数代价在全部惰性好素位求和满足
$$
\sum_p6n\tau_2\log p=O(n),
\tag{21}
$$
因为 $\sum_p\log p/p^2$ 收敛。
这准确支付普通部分的线性成本。

但完整原来源同时含第一 Gaussian，
而真正含七塔的任何原多项式还满足 (18)。
因此不能把 (21) 直接替换成 R583 对原九格的全部惰性预算，
也不能从辅助域次数 $p^2$ 增加原全局来源维数。
两个中央投影的 (20) 同样不提供新的局部积分超越坐标。

当前已付的同格上界仍是 R583 的 $(a_I,b_I)=(0,3)$。
本篇不由半径断言该真实旗标成本最优；
若要改善，仍须支付同一个整数格、全部角、全部连续前行及
非空饱和层，而不能只对分解后的因子计价。

## 依赖

- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  实际 $a_2$、完整 $V$ 和略大于第二半径的闭盘。
- [R622](R622-original-two-gaussian-central-connection-and-identical-newton-defect.md)：
  同一个原中央解及 (19) 的完整归一。
- [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)：
  闭盘无极点引理、原非中央 Stokes 排除、加性积分独立和真实七塔。
- [R583](R583-nine-coordinate-inert-resonance-absorption-and-sharp-envelope.md)：
  同一九格、全部真前缀与目前的完整惰性成本。

全篇为实际函数域和闭盘证明，没有新增素数扫描。
