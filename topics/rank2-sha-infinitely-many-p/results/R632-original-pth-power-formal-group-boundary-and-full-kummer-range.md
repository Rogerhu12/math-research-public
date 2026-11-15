# R632 — 原 p 次幂的精确形式群边界与整个首野分支域

日期：2026-11-15。**状态：已证明。**

本篇将 R625/R627 的有限整窗推进到原未去 Gaussian 来源的全部级数。
原 $f_4,f_1,S,T$ 及质量一参考 $H_{38}$ 的归一函数 $B$ 满足：
$$
\operatorname{rad}(B^p)=R_E:=p^{-1/(p^2-1)},
\qquad B^p\text{ 在闭 }R_E\text{ 非 Tate}.
$$
证明在原 $u=x^{-1/2}$ 参数中隔离唯一临界指数，
再用同一个形式对数在闭边界的完整范数运输回来。

由此，对整个 $S\le R<R_E$，原 sigma 自身给准确 degree-$p$
Kummer 域，七个原正幂积分在这个实际域上仍代数独立。
这里 $S=p^{-p/(p^2-1)}$ 是原第一 Gaussian 半径。
不再只把结论限制在 R618 第二盘之后的一小段。
所有 $p$ 次幂仍支付其真实来源次数；原中央值没有获得新的零。

## 1. 原参数、同一 theta 与结论范围

固定
$$
p=6s-1>71,\qquad b=17,\qquad
L=(p^2-1)/6,\qquad d_0=p+1.
\tag{1}
$$
沿原 $y^2=x^3+b$、$dz=dx/(2y)$、
$\sigma=z+O(z^7)$ 与 $(\log\sigma)''=-x$ 的规范，
令
$$
u=x^{-1/2},\quad \tau=bu^6,\quad
z=uH(\tau),\quad C(\tau)=(1+\tau)^{-1/2},
$$
$$
H_n=\frac{C_n}{6n+1},\qquad
C_n=(-1)^n4^{-n}\binom{2n}{n}.
\tag{2}
$$
保持首项 $u=z+\cdots$。定义同一个原函数
$$
K(\tau)=\left(\frac{\sigma(z(u))}{u}\right)^6,\qquad
\mathscr L(\tau)=\log K(\tau).
\tag{3}
$$

对
$$
\mathcal F=\sigma^m x^\alpha(-y)^\beta Q(\tau),\qquad
d=m-2\alpha-3\beta\ge0,\qquad
B(z)=z^{-d}\mathcal F(z),
\tag{4}
$$
本篇假设 $m\in\mathbf Z_p^\times$、$Q\in1+\tau\mathbf Z_p[[\tau]]$，
且保原固定整数 $m,\alpha,\beta$。
全部实际应用如下：
$$
\begin{array}{c|rrrr}
\mathcal F&m&\alpha&\beta&d\\ \hline
f_4&6&1&0&4\\
f_1&6&1&1&1\\
S&34&14&0&6\\
T&72&33&0&6\\
H_{38}&38&19&0&0
\end{array}
\tag{5}
$$
$Q$ 分别是既有的完整原多项式；没有省去 $S,T,H_{38}$ 的任何因子。
所有这些 $m$ 在当前素数处确为单位。

**定理1。** 对 (4)，
$$
\boxed{
\operatorname{rad}_z(B^p)=R_E,\qquad
B^p\notin\mathbf C_p\langle z/R_E\rangle.
}
\tag{6}
$$
并且对每个闭 $R<R_E$，$B^p$ 及其逆都是范数一的 Tate 单位。
同样结论适用于原 $\mathcal F^p$ 的精确半径及闭边界非 Tate，
但 $\mathcal F^p$ 还保有原点零阶 $dp$。

## 2. 原 u 参数对数的准确系数

设
$$
J(\tau)=\sum_{n\ge0}\frac{C_n}{1-6n}\tau^n.
$$
由 $\zeta'=-x$ 及原首项可直接积分，得到
$$
\zeta(z(u))=u^{-1}J(\tau),\qquad
6\tau J'-J=-C.
\tag{7}
$$
令 $A=CJ$。用 $C'/C=-1/(2(1+\tau))$，有
$$
6\tau(1+\tau)A'=(1-2\tau)A-1,\qquad A(0)=1.
$$
故其全部系数满足
$$
A_n=-\frac{6n-4}{6n-1}A_{n-1}.
$$
另一方面，(3) 的原对数导数给
$\tau\mathscr L'=CJ-1$。因此
$$
\boxed{
\mathscr L_n=
\frac{(-1)^n}{n}\prod_{j=1}^n\frac{6j-4}{6j-1}
\quad(n\ge1).
}
\tag{8}
$$
这是原 $K=\Theta_{\rm old}(-\tau)^3$ 的同一规范，
不是将旧角参数错认成 $-bz^6$。
推导也固定了每个符号及分母。

## 3. 全部对数分母及唯一临界低项

对任一 $p^h=M$，分子 $6j-4$ 与分母 $6j-1$ 的零剩余类分别是
$$
\begin{array}{c|cc}
h& r_{\rm num}&r_{\rm den}\\ \hline
\text{奇数}&(2M+2)/3&(M+1)/6\\
\text{偶数}&(M+2)/3&(5M+1)/6.
\end{array}
\tag{9}
$$
它们都在 $1,\ldots,M-1$ 中。
每个完整长度 $M$ 的区间对两者贡献相同。
所以在任意前缀 $1\le j\le n$ 上，第 $h$ 层的估值差属于

- $h$ 奇数时的 $\{-1,0\}$；
- $h$ 偶数时的 $\{0,1\}$。

若 $h\le v_p(n)$，该层恰由完整区间组成，差为零。

设 $k=\lfloor\log_p(6n)\rfloor$、$a=v_p(n)$。
所有因子小于 $6n$，高于 $k$ 的层没有贡献；
前 $a$ 层差为零，其余每层损失至多一。
将 (8) 的 $n$ 分母也保留，得到全指标界
$$
\boxed{
v_p(\mathscr L_n)\ge-k
=-\lfloor\log_p(6n)\rfloor.
}
\tag{10}
$$
因此原 $\mathscr L$ 在每个严格单位内盘收敛。

在 $n<p^2$ 的较长实际窗口，(9) 给更强结论。
因为 $6n<6p^2<p^3$，只有 $h=1,2$ 可能出现；
第二层贡献非负。
若 $p\nmid n$，至多由第一层损失一；
若 $p\mid n$，第一层差为零，而 $n$ 本身只含一个 $p$。
于是
$$
\boxed{
p\mathscr L_n\in\mathbf Z_p\quad(1\le n<p^2).
}
\tag{11}
$$
对 $n<s$，尚未碰到第一分母类 $r_{\rm den}=s$，
且 $n<p$，所以 $\mathscr L_n$ 已整。
在 $n=s$，恰有一个分母 $p$，没有分子抵消：
$$
\boxed{
v_p(\mathscr L_s)=-1,\qquad
p\mathscr L_s\in\mathbf Z_p^\times.
}
\tag{12}
$$
这是真正的唯一最早临界项，不是仅凭某个有限素数观察。

## 4. K 的 p 次幂在原 u 盘上的准确边界

在 $u$ 半径 $R_E$ 上，$\tau^n=b^nu^{6n}$ 的权估值是
$$
6n/(p^2-1)=n/L .
$$
对 $p\mathscr L_s\tau^s$，由 (12) 得恰为
$$
s/L=1/(p-1).
\tag{13}
$$
这是 $p$ 进指数的临界值。

其余每个对数项都严格高于此值。
当 $n<s$，(11) 的更强低阶结论给至少
$1+n/L>1/(p-1)$。
当 $s<n<p^2$，(11) 给至少
$n/L>s/L$。
当 $n\ge p^2$，(10) 给
$$
v_p(p\mathscr L_nb^n)+n/L
\ge1+n/L-\log_p(6n).
\tag{14}
$$
右边在 $n\ge p^2$ 严格递增，因为
$1/L>1/(p^2\log p)$。
在 $n=p^2$ 已有
$$
1+\frac{p^2}{L}-\log_p(6p^2)
>5-\log_p6>4.
$$
所以 (14) 也严格超过临界值，且趋于无穷。

因此在闭 $R_E$ 上，完整余对数
$$
p\mathscr L(\tau)-p\mathscr L_s\tau^s
$$
具有严格小于指数收敛阈值的 Gauss 范数。
上述有限低阶间隔与趋于无穷的线性尾还保证：
存在某个 $R_+>R_E$、$R_+<1$，
同一严格不等式在闭 $R_+$ 上仍成立。
于是对任何 $m\in\mathbf Z_p^\times$，有原恒等式
$$
\boxed{
K(bu^6)^{mp/6}
=V_m(u)\exp(\alpha_m u^{d_0}),\qquad
\alpha_m=\frac{mp\mathscr L_s b^s}{6}\in\mathbf Z_p^\times,
}
\tag{15}
$$
其中 $V_m,V_m^{-1}$ 都是闭 $R_+$ 上范数一的 Tate 单位。

剩余指数的准确半径是
$$
p^{-1/(d_0(p-1))}=R_E.
$$
在边界，指数第 $k$ 项的权估值为
$$
\frac{k}{p-1}-v_p(k!)=\frac{s_p(k)}{p-1}.
$$
取 $k=p^j$，这个值恒为 $1/(p-1)$，
故系数不趋零；指数在闭 $R_E$ 非 Tate。
乘 (15) 的更大盘 Tate 单位及其逆不改变这一事实。
从而
$$
\boxed{
K(bu^6)^{mp/6}\text{ 的准确 }u\text{ 半径为 }R_E，
\text{闭边界非 Tate}.
}
\tag{16}
$$
对每个严格内盘，它及其逆的范数均为一。
没有把临界两项的近似相消误当作边界整性。

## 5. 原形式对数在闭边界的完整范数

为从 $u$ 返回原 $z$，必须支付边界上的实际代换，
不能只引用两级数形式可逆。

若 $a=v_p(6n+1)$，其最低 $a$ 个 $p$ 进位由
$6n\equiv-1\pmod{p^a}$ 唯一确定。
由 $p=6s-1$，这些位从低到高交替为
$$
5s-1,\ s-1,\ 5s-1,\ s-1,\ldots .
$$
将 $n+n$ 相加，每个 $5s-1$ 位必产生一次进位，
紧随的 $s-1$ 位即使加上前一进位也不再进位。
因此至少有 $\lceil a/2\rceil$ 次进位。
阶乘估值给
$$
\boxed{
v_p(H_n)\ge-\lfloor a/2\rfloor.
}
\tag{17}
$$
$a=0$ 时同样成立。

若 $k=\lfloor a/2\rfloor\ge1$，
则 $6n+1\ge p^{2k}$，故
$$
n\ge(p^{2k}-1)/6\ge kL.
$$
结合 (17)，得到
$$
\boxed{v_p(H_n)+n/L\ge0.}
\tag{18}
$$
而 (17) 的对数增长还说明左边随 $n$ 趋于无穷。
因此
$$
H(bu^6)\in\mathbf C_p\langle u/R_E\rangle,\qquad
\|H\|_{R_E}=1,\qquad
\|uH(bu^6)\|_{R_E}\le R_E.
\tag{19}
$$
在任意闭 $R<R_E$，(18) 严格化为
$$
\|H(bu^6)-1\|_R<1.
\tag{20}
$$
故 $z(u)=uH(bu^6)$ 在该闭盘是带严格小扰动的恒等映射。
标准逐次代入可在 Tate 代数中自含地构造其逆：
对给定 $z$ 迭代 $u=z-u(H(bu^6)-1)$；
差商的范数也小于一，因为整数导数不增大系数范数。
这是严格收缩，故存在唯一 Tate 逆 $u(z)$，
$$
|u|=|z|,\qquad u/z,\ z/u
\text{ 在闭 }R\text{ 均为范数一单位}.
\tag{21}
$$
闭 $R_E$ 本身不使用逆；
后面只用已证的正向 Tate 代换 (19)。

## 6. 原 B 的 p 次幂：开盘与闭边界同时支付

由 (2)–(4) 直接得到原身份
$$
\boxed{
B(z(u))
=H(\tau)^{-d}K(\tau)^{m/6}
 (1+\tau)^{\beta/2}Q(\tau).
}
\tag{22}
$$
对 $R<R_E$，(20)–(21) 及 (15) 说明 (22) 的 $p$ 次幂
可与 $u(z)$ 合成，且所有因子及其逆都是闭 $R$ 的范数一 Tate 单位。
这支付 (6) 的半径下界，保全部原固定多项式。

反设 $B(z)^p$ 是闭 $R_E$ 的 Tate 元。
由 (19)，$B(z(u))^p$ 也是闭 $u$-$R_E$ 的 Tate 元。
因为 $d\ge0$，可乘已证 Tate 的 $H^{dp}$；
再除以
$$
(1+\tau)^{\beta p/2}Q(\tau)^p,
$$
其与逆在某个严格大于 $R_E$ 的闭盘都为 Tate 单位。
(22) 遂迫使 $K(\tau)^{mp/6}$ 在闭 $R_E$ Tate，
与 (16) 矛盾。这证明 (6)。

若 $B^p$ 有严格更大的收敛半径，它在闭 $R_E$ 必为 Tate，
故半径上界也随即成立。
乘回原单项式 $z^{dp}$ 不改变半径或闭边界非 Tate，
但必须保这个真实首阶。
定理1证毕。

对 $H_{38}$，$d=0$，此证明同样适用；
R627 的首坏位置比 $S,T$ 晚一项，
并没有改变其全级数的准确 $p$ 次幂半径。

## 7. 原 sigma 在整个 S≤R<R_E 的准确 p 域

以下取 $\mathbf C_p$ 上的闭半径 $R$，必要时在其值群内取，
并置
$$
\mathcal T_R=\mathbf C_p\langle z/R\rangle,\qquad
F_R=\operatorname{Frac}(\mathcal T_R),\qquad
h(z)=\sigma(z)/z.
$$
令
$$
S=p^{-p/(p^2-1)}.
$$
R301/R588 的同一第一 Gaussian 证明
$h$ 准确半径为 $S$、闭 $S$ 非 Tate。
定理1以 $m=1,\alpha=\beta=0,d=1,Q=1$ 应用，给
$$
h^p\in\mathcal T_R^\times\quad(R<R_E).
\tag{23}
$$
其对数导数
$$
q_\sigma=h'/h=\frac{(h^p)'}{p h^p}\in\mathcal T_R
\tag{24}
$$
也是真正解析系数。

若在 $R\ge S$ 时有 $h\in F_R$，
由 $h'=q_\sigma h$ 可见 $h$ 在闭盘没有极点：
一个阶 $a>0$ 的极点在导数中变成 $a+1$ 阶，
而解析系数乘 $h$ 至多仍是 $a$ 阶，首项不可能相消。
在 Tate 分式域中无极点的元素属于 Tate 代数，
故 $h\in\mathcal T_R$，与闭 $S$ 非 Tate 矛盾。
所以
$$
h\notin F_R\quad(S\le R<R_E).
$$
$\mathbf C_p$ 含全部 $p$ 次单位根，
而 (23) 给一个实际非平凡的 $p$ 次根，得到
$$
\boxed{
K_R^\sigma:=F_R(\sigma)=F_R(h),\qquad
[K_R^\sigma:F_R]=p,\qquad
\operatorname{Gal}(K_R^\sigma/F_R)=\mu_p
\quad(S\le R<R_E).
}
\tag{25}
$$
原 $W=z^2x$、$Y=-z^3y$ 由 (21) 属于 $\mathcal T_R$，
故 $x,y$ 属于 $F_R$，全部原 theta 有理来源都在 (25) 中。

(25) 推广 R623 实际对角子域的半径范围。
它没有宣称 R623 两个独立 Gaussian 根生成的整个 $p^2$ 域
在任意新半径仍有相同呈示；
本篇使用的是已经确定的原 sigma 本身。
也不宣称在闭 $R_E$ 或更外面的分式域已得到次数分类：
(6) 的端点结论是准确的 Tate 非成员，而非未证的外盘域论断言。

## 8. 七个原积分在整个实际 p 域仍独立

保持同一个零初值积分
$$
J_{4,j}=\int_0^z t^j f_4(t)\,dt\quad(j=0,1),\qquad
J_{1,j}=\int_0^z t^j f_1(t)\,dt\quad(j=0,\ldots,4).
\tag{26}
$$
其任意常数组合 $\mathcal J$ 的导数可写成
$$
D\mathcal J=h^6G,\qquad G\in\mathcal T_R.
\tag{27}
$$
这里 $f_4=z^4Wh^6$、$f_1=zWYh^6$，
所以 $G$ 在原点也正则，未给 $x,y$ 的 Laurent 极点漏账。

反设非零组合在 $K_R^\sigma$ 有原函数。
取 (25) 的真正特征六投影，导数与 Galois 作用交换，
得到形如 $h^6v$ 的原函数，$v\in F_R$，
且
$$
v'+6q_\sigma v=G.
\tag{28}
$$
$p>71$ 保特征六非零。
(24)、(27) 在整个闭盘正则；
同一极点阶数比较迫 $v\in\mathcal T_R$，包括原点。
所以实际 Laurent 域中
$$
\mathcal J-h^6v=C
$$
为常数。原第一 Gaussian 记为 $E_1=\exp(cz^{p+1})$。
由 R618，$E_1^{-1}h$ 在某个大于 $S$ 的盘内是 Tate 单位；
因此
$$
E_1^{-6}(\mathcal J-C)
=(E_1^{-1}h)^6v\in\mathcal T_S.
\tag{29}
$$
但 R588 对同一七个原积分的两个完整非中央 Stokes 行
已有单位矩阵，正好排除任意非零常数组合及任意 $C$ 的 (29)。
矛盾。

若某个有限代数扩张存在原函数，取域迹再除以次数，
将给 $K_R^\sigma$ 中的原函数，仍矛盾。
全部实际函数均处于 $\mathbf C_p((z))$，常数域没有增加。
应用 R575/R588 已证明的加性积分引理，得到
$$
\boxed{
J_{4,0},J_{4,1},J_{1,0},\ldots,J_{1,4}
\text{ 在 }K_R^\sigma\text{ 上代数独立}
\quad(S\le R<R_E).
}
\tag{30}
$$
同一固定三角换元将 (30) 传给原七个正幂规整塔。

这里的特征投影使用 $1/p$，只作域论证明；
没有将其当作原整来源格中的无成本运算。

## 9. 原中央与真实全局预算

(6) 是原实际 $p$ 次幂的全级数结论，
与 R625/R627 的有限首坏带完全兼容：
一次分母出现很晚，不意味着闭 $R_E$ 的全部系数趋零。
其来源幂次数仍为 $p$，不能当作原固定 $D$ 中的一条免费解析列。

(25)、(30) 也不赋任何新增中央零。
R623 在已付较小外盘证明的两个中央投影属于原 sigma 对角域，
无论原 $j$ 是否为零；那个精确身份继续保持。
本篇没有将 R622 的特定中央解无证明地延到全部 $R<R_E$。
若要扩大该中央连接范围，必须重新支付同一投影、连接和全部 Newton 尾。

原全九格的普通成本、惰性成本 $(0,3)$、
每个 $D/k$ 的真饱和层及严格全局门仍按 R583/584。
本篇只扩大实际解析域并分类原 $p$ 次幂边界，
不从解析域次数或七塔独立性重复计入来源维数。

## 依赖

- [R625](R625-original-theta-powers-integral-window-and-first-bad-coefficient.md)、
  [R627](R627-original-theta-power-first-bad-band-and-unit-two-source-prefix.md)：
  原完整来源、固定多项式、真实 $p$ 幂及有限整窗。
- [R618](R618-original-second-gaussian-exact-radius-and-newton-tail.md)：
  原第一 Gaussian 后余项的大于 $S$ 的实际盘。
- [R623](R623-original-two-gaussian-wild-field-and-diagonal-source.md)：
  较小外盘的实际对角域及七积分论证；本篇从原 sigma 扩大半径。
- [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)：
  原全非中央 Stokes 单位矩阵、闭 $S$ 非 Tate 及加性积分接口。
- 原形式对数的整性、反演范数及 $K$ 的全部分母
  已在 §§2–6 自含证明，不借 ordinary sigma 的整性定理。

本篇无新增素数扫描；全部边界、指数和真实代换均为全参数证明。
