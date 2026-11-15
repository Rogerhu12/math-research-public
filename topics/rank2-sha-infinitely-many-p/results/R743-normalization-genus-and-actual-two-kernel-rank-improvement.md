# R743 — 原奇异因子的正规化亏格与同预算两连接核的严格秩增益

日期：2026-11-15。**状态：已证明。**

在 R730 的同一固定角最高系数范围，原低于首共振的 ODE
迫正规化亏格满足
$$
6g(\widetilde C)\ge h-2\deg_tF-14\deg_YF+6.
$$
这使用所有正规分支，包括原奇点及全部六个固定纤维。

进一步，原函数域的两个低次数生成元 $t,Y$
限制了正规化上任何小次数线系能够具有的维数。
将这个限制用于 R550 的两个实际连接核，
在满主阶低 $\ell$ 窗中得到
$$
a_\eta\le\frac{13}{32}\kappa+o(\kappa),\qquad
b_\eta\le\frac{17}{48}\kappa+o(\kappa).
$$
所以同预算整个 $\mathcal H_3$ 的真实单位秩下界
由原 Clifford 界的 $59\kappa/16+o(\kappa)$
提高为 $359\kappa/96+o(\kappa)$。

这里没有假设 $C$ 光滑，也没有把算术亏格用于正规化的
Castelnuovo–Severi 不等式。
结论控制同一个实际像的秩；指定 forcing 是否落在全像中仍未判定。

## 1. 原来源、曲线、特征及两个实际长度

保持 R495、R550、R701、R730 的同一来源
$$
P^{\rm fact}=q\,t^rF^3\in\mathcal W_D,\qquad
q=d^{-C_D}Q,\qquad d=1+8t.
$$
原 $F\in k[t,Y]$ 几何不可约，$C\subset X$ 是其在原十九角曲面上的整曲线。
原点 $P=(0,1)\in C$ 光滑，$e(P)\ne0$，其中
$$
e=\mathcal EF,\qquad \mathcal E=Y\partial_Y,\qquad \delta=t\partial_t.
$$
写
$$
a=\deg_tF,\qquad b=\deg_YF,\qquad
\kappa=C^2,\qquad \chi=-K_XC,
$$
$$
N=\mathcal O_C(C),\qquad
\mathcal H_j=H^0(X,\mathcal O_X(jC)).
\tag{1}
$$
$C$ 的算术亏格与正规化亏格分别记为
$$
g_C=1+\frac{\kappa-\chi}{2},\qquad
\gamma=g(\widetilde C).
\tag{2}
$$
二者在下文始终区分。

保 R730 的真实最高系数条件：
$F$ 的最高 $Y$ 系数 $f_b(t)$ 的零点都在
$$
S_0=\{0,1,-1/8,\alpha_+,\alpha_-\},\qquad
\alpha_\pm=(-1\pm3\sqrt{-3})/8,
\quad S=S_0\cup\{\infty\}.
\tag{3}
$$
这是原固定角 $S$-unit 条件，不是对任意 $F$ 自动成立的结论。
继续要求
$$
p=6s-1>101,\qquad p>\max(a,b),\qquad 0<h<s,
\tag{4}
$$
以及沿原光滑支的准确接触
$$
\log(g/\psi)=t^hu,\qquad u(0)\ne0.
\tag{5}
$$
(5) 是模 $p$ 的原低段；完整整提升中的 $p\xi$ 不被删除。

后半篇的实际像比较使用 R550 强窗
$$
h>\kappa,\qquad T-h>\kappa,\qquad T\le2h,
\tag{6}
$$
其中必须分别取
$$
T_J=s-r,\qquad T_M=s-r-13.
\tag{7}
$$
特别 $0<h<T<p$。
$J$ 和完整 $M=c_*U_0w^{13}J$ 各自使用自己的 $T$，
不交换这两个连接。

可以先扩张到代数闭剩余域。
原曲线几何整，所有截面维数、有限矩阵的秩及非零条件均保持；
最终的秩不等式因而在原域成立。
实际函数域为 $k(t,Y)$，两个映射的次数准确为
$$
\deg(t:\widetilde C\to\mathbf P^1)=b,\qquad
\deg(Y:\widetilde C\to\mathbf P^1)=a.
\tag{8}
$$
由 (4)，两映射可分，其每个局部分歧指数均小于 $p$。
在代数闭常数域上这些分支均 tame。

## 2. 原 ODE 给正规化亏格下界

沿用 R507、R730 的实际有理函数
$$
V=\frac{t}{Y}\frac{dY}{dt},
$$
$$
\mathcal F_F
=\mathcal R-\{6(1-t)\delta-(1+2t)\}V,\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3(1+8t)^2}.
\tag{9}
$$
$V$ 是函数域中的有理导数；不假设 $\log Y$ 在全曲线上存在。

**引理 1。**
$$
\boxed{
h\le6\gamma+2a+14b-6.
}
\tag{10}
$$

**证明。** 在 $t(Q)\notin S$ 的正规分支上，
$Y$ 不可能有极点：$f_b(t(Q))$ 为单位，
若 $Y$ 有极，方程 $F(t,Y)=0$ 的最高 $Y$ 项将具有严格最小估值。

令 $e_Q$ 为 $t$ 在该正规分支的分歧指数。

若 $Y(Q)\ne0$ 且 $e_Q=1$，(9) 正则。
若 $Y(Q)\ne0$ 且 $e_Q\ge2$，取 tame 参数 $v$，
$t-t(Q)=v^{e_Q}$。
$V$ 的极阶至多 $e_Q-1$，$\delta V$ 的极阶至多 $2e_Q-1$，所以
$$
\operatorname{pole}_Q\mathcal F_F
\le2e_Q-1\le3(e_Q-1).
\tag{11}
$$
这只需正规分支，不要求其在原 $C$ 上为光滑点。

若 $m_Q=\operatorname{ord}_QY>0$，则
$m_Q\le a<p$、$e_Q\le b<p$；
$V$ 的极阶为 $e_Q$，$\delta V$ 的极阶至多 $2e_Q$。
因此
$$
\operatorname{pole}_Q\mathcal F_F
\le2e_Q
\le3(e_Q-1)+2m_Q.
\tag{12}
$$
最后一步对 $e_Q,m_Q\ge1$ 成立，因为右减左为
$e_Q+2m_Q-3\ge0$。
这里没有把奇点的导数因子估值当成光滑分歧指数。

$t$ 为 tame 度 $b$ 覆盖，Riemann–Hurwitz 给
$$
\sum_{Q\in\widetilde C}(e_Q-1)=2\gamma-2+2b.
\tag{13}
$$
$Y$ 的全零除子次数为 $a$。
于是固定六纤维以外的极阶总和至多
$$
3(2\gamma-2+2b)+2a.
\tag{14}
$$
(14) 对所有分歧使用总和，允许计入随后再次单独估计的固定纤维；
这是上界，不减去未识别的分歧。

固定六纤维逐分支保持 R730 的完整界：

| 纤维 | (9) 的极阶上界 |
|---|---:|
| $t=0$ | $0$ |
| $t=1$ | $e_Q$ |
| $t=-1/8$ | $2e_Q$ |
| 两个 $h_7$ 根，各自 | $2e_Q$ |
| $t=\infty$ | $e_Q$ |

在 $0,\infty$，$t/(dt/dv)$ 是 $v$ 乘单位，
故 $V,\delta V$ 正则；$\infty$ 处原有理系数至多再添一份 $t$ 极。
在 $1$，$1-t$ 抵消 $\delta V$ 的一份极。
其余有限非零纤维用一般 $2e_Q$ 界，
包含所有 $Y$ 的零、极与原十九角上的高重数。
每个完整纤维中 $\sum e_Q=b$，因此表中总贡献不超过 $8b$。

最后，由原 ODE 只在 $t^s$ 之前的准确身份及 (5)，
$$
\mathcal F_F
=h(6h-1)u(0)t^h+O(t^{h+1}).
\tag{15}
$$
$h<s=(p+1)/6$ 保 $h(6h-1)$ 为单位。
所以 (9) 是非零有理函数，在原 $P$ 的零阶恰为 $h$。
其全零、极次数相等，结合 (14) 与固定部分 $8b$ 即得 (10)。证毕。

置
$$
\boxed{
G_F=\max\left\{0,
\left\lceil\frac{h-2a-14b+6}{6}\right\rceil\right\}.
}
\tag{16}
$$
因此 $\gamma\ge G_F$。
(10) 对奇异曲线没有附加光滑假设；
奇点只通过正规化的实际 tame 分支参与 (11)–(14)。
它也没有延长原 ODE 到 $s$ 或下一共振。

## 3. 有限的小度线系界与 primitive 函数

先给独立的精确整数界。
对于 $E\ge r\ge2$，定义 Castelnuovo 数
$$
\pi(E,r)
=\frac{m(m-1)}2(r-1)+m\varepsilon,
$$
$$
E-1=m(r-1)+\varepsilon,\qquad0\le\varepsilon<r-1.
\tag{17}
$$
等价地，
$$
\pi(E,r)=\sum_{j\ge1}\max\{E-1-j(r-1),0\}.
\tag{18}
$$

给定非负整数 $G$、正整数 $A$ 和 $0<d<p$，定义
$$
\mathcal C(G,d,A)
=1+\max\left(
\{0,1\}\cup
\left\{
r\in\mathbf Z:2\le r\le d,\
\begin{array}{l}
\text{存在 }1\le\nu\le\lfloor d/r\rfloor,\ \text{使}\\
G\le\nu\pi(\lfloor d/\nu\rfloor,r)
       +(\nu-1)(A-1)
\end{array}
\right\}
\right).
\tag{19}
$$
另置 $\mathcal C(G,d,A)=0$ 对 $d<0$，
$\mathcal C(G,0,A)=1$。
(19) 仅是有限整数最大值，不涉及未知一般位置或期望维数。

**引理 2。**
设 $C$ 是本篇的几何整曲线，$\gamma\ge G$，
$k(C)=k(t,Y)$、$\deg t=b$、$\deg Y=a$。
若 $\mathscr L$ 是 $C$ 上次数 $d<p$ 的线束，则
$$
\boxed{
h^0(C,\mathscr L)\le\mathcal C(G,d,a+b).
}
\tag{20}
$$

**证明。** 令 $\nu_C:\widetilde C\to C$ 为正规化。
由于 $C$ 整且 $\mathscr L$ 局部自由，准确有
$$
H^0(C,\mathscr L)\hookrightarrow
H^0(\widetilde C,\nu_C^*\mathscr L),\qquad
\deg(\nu_C^*\mathscr L)=d.
\tag{21}
$$
次数相等可由正规化序列张量 $\mathscr L$ 后的有限长度商看出：
商长度与张量前相同，故用 Euler 特征定义的次数不变。
因此没有把原奇点处的下降条件漏计为额外截面。

负度情形无截面，零度情形至多一维。
设 $d>0$，正规化上截面维数为 $r+1$。
$r\le1$ 时 (19) 已覆盖；
$r\ge2$ 时，去掉完整线系的固定除子，
得到次数 $d_{\rm mov}\le d$ 的无基点线系，
定义
$$
\widetilde C\longrightarrow C'\subset\mathbf P^r.
$$
像非退化，令 $E=\deg C'$、
$\nu=[k(\widetilde C):k(C')]$，则
$$
d_{\rm mov}=\nu E,\qquad E\ge r,\qquad
1\le\nu\le\lfloor d/r\rfloor<p.
\tag{22}
$$
所以该有限函数域扩张可分；
其不可分次数若大于一必是至少 $p$ 的 $p$ 幂，与 (22) 矛盾。

记 $K=k(t,Y)$、$K'=k(C')$。
因为 $K=K'(t,Y)$ 且 $K/K'$ 可分，
存在常数 $c\in k$ 使
$$
K=K'(t+cY).
\tag{23}
$$
这里可以在代数闭无限常数域中选择 $c$。
具体地，对 $K/K'$ 的不同嵌入 $\sigma,\tau$，
使 $\sigma(t+cY)=\tau(t+cY)$ 的常数 $c$ 至多一个；
若它们对 $Y$ 相同，则对 $t$ 必不同，
因为 $t,Y$ 生成 $K$，此时没有坏 $c$。
避开有限个坏常数即可。
若需要同时使 $t+cY$ 可分，也可避开
$dt+c\,dY=0$ 的至多一个常数；
$dt\ne0$ 已由 $b<p$ 保证。
$\nu=1$ 时直接取 $t$ 亦可。

而且
$$
\deg(t+cY)\le a+b,
\tag{24}
$$
因为其极除子逐点被 $(t)_\infty+(Y)_\infty$ 控制。
没有假定 $t$ 单独或 $Y$ 单独生成 $K/K'$。

令 $\gamma'$ 为 $C'$ 的正规化亏格。
对 (23) 的两个子域 $K'$ 与 $k(t+cY)$
应用 Castelnuovo–Severi，得到
$$
\gamma\le\nu\gamma'+(\nu-1)(a+b-1).
\tag{25}
$$
$C'$ 的正规化到 $C'\subset\mathbf P^r$ 是 birational 的
simple 线系，因此正特征 Castelnuovo 界给
$$
\gamma'\le\pi(E,r)
\le\pi(\lfloor d/\nu\rfloor,r).
\tag{26}
$$
(25) 所用规范是 Poonen 的 Proposition 2.1；
(26) 的正特征 simple 线系规范及精确数值见
Abdón–Torres 原稿 §2, (2.2)，其原引文为
Hartshorne 的相关 genus bound 与 Rathmann, Corollary 2.8。
这里只用几何亏格上界，不调用特征零的任意一般点假设，
也不假设原映射 $\widetilde C\to C'$ 本身 birational；
其可能的复合次数已完整留在 (22)、(25)。

由 $G\le\gamma$、(25)、(26)，$r$ 必进入 (19) 的有限集合。
结合 (21) 即得 (20)。证毕。

(20) 允许原 $C$ 奇异，亦允许小度线系复合。
低于 $p$ 的次数是可分 primitive 步骤的明确门；
不能把结论直接用于任意高次数非可分线系。

## 4. 接到原两个连接核，而非自由局部参数

原 $C$ 是光滑曲面上的 Cartier 除子，因而是整 Gorenstein 曲线。
其对偶线束 $\omega_C$ 可直接使用 Riemann–Roch 与 Serre 对偶。
R550 的两个真实连接继续记为
$$
\alpha_\eta:H^0(C,N^2(-hP))\to\operatorname{coker}E_{T-h},
$$
$$
\beta_\eta:H^0(C,N^3(-TP))\to\operatorname{coker}E_{\rm mir},
$$
$$
a_\eta=\dim\ker\alpha_\eta,\qquad
b_\eta=\dim\ker\beta_\eta.
\tag{27}
$$
它们仍使用同一 $\eta$、同一个 normal 提升及完整原 $\mathcal H_1,\mathcal H_2$ 列。

残余线束的次数准确为
$$
d_\alpha=\deg(\omega_C N^{-2}(hP))=h-\kappa-\chi,
$$
$$
d_\beta=\deg(\omega_C N^{-3}(TP))=T-2\kappa-\chi.
\tag{28}
$$
在本篇原强窗中 $\kappa,\chi>0$ 且 $h,T<p$，
所以 (28) 的非负次数自动小于 $p$，可以应用引理2。

由 Riemann–Roch，
$$
h^0(C,N^2(-hP))
=\frac{3\kappa+\chi-2h}{2}
+h^0(C,\omega_CN^{-2}(hP)),
$$
$$
h^0(C,N^3(-TP))
=\frac{5\kappa+\chi-2T}{2}
+h^0(C,\omega_CN^{-3}(TP)).
\tag{29}
$$
这些式子使用算术亏格 (2)，与引理2中正规化亏格的用途不同。

**定理 1（有限的实际核界）。**
$$
\boxed{
\begin{aligned}
a_\eta&\le
\frac{3\kappa+\chi-2h}{2}
+\mathcal C(G_F,d_\alpha,a+b),\\
b_\eta&\le
\frac{5\kappa+\chi-2T}{2}
+\mathcal C(G_F,d_\beta,a+b).
\end{aligned}}
\tag{30}
$$
同时保 R550/R543 的原 Clifford 界；
可以取两种已证上界的较小者。
若 $2\kappa-h<0$ 或 $3\kappa-T<0$，
对应原截面空间直接为零。
在任何实际存在的数据上，(29) 保证相应右界非负。

证明只是把引理1的 $G_F$ 代入引理2，
再用 (27) 的核包含于其真实定义域。
这里没有把核等同于定义域，也没有改变 $\alpha_\eta,\beta_\eta$。

## 5. 原临界窗的严格常数

考虑原满主阶低 $\ell$ 窗中的实际因子族：
$$
\kappa\to\infty,\qquad
\frac h\kappa\to\frac98,\qquad
\frac T\kappa\to\frac94,\qquad
a+b=o(\kappa),\qquad \chi=o(\kappa).
\tag{31}
$$
例如原
$\kappa=47b^2/12+O(b)$、
$h=141b^2/32+O(b)$、
$a\le5b+O(1)$、$\chi=O(b)$
以及 $k+13=o(\kappa)$ 满足 (31)。
这仍是对实际存在、满足 (3) 的因子逐个应用，
不声称已经构造了这样的原首核。

由 (16)、(28)，
$$
G_F\ge\frac{3}{16}\kappa+o(\kappa),\qquad
d_\alpha=\frac18\kappa+o(\kappa),\qquad
d_\beta=\frac14\kappa+o(\kappa).
\tag{32}
$$

下面说明 (19) 的最大值也受准确常数控制，
包括全部复合次数 $\nu$。

若该最大值 $r=o(\kappa)$，所需结论显然。
否则沿一个子列令 $r/\kappa\to x>0$；
由 (22)，$\nu\le d/r$ 有界，
可以再取子列使其为固定整数。
由 (18)，若 $d/\kappa\to d_0$，则
$$
\frac{\nu\pi(\lfloor d/\nu\rfloor,r)}{\kappa}
\longrightarrow
\Phi(d_0,\nu x),
\qquad
\Phi(d_0,x)=\sum_{j\ge1}(d_0-jx)_+.
\tag{33}
$$
$\Phi$ 连续、随 $x>0$ 不增，
故 $\Phi(d_0,\nu x)\le\Phi(d_0,x)$。
同时 (25) 的补项
$(\nu-1)(a+b-1)=o(\kappa)$。
因此 (19)、(32) 迫
$$
\Phi(d_0,x)\ge\frac{3}{16}.
\tag{34}
$$

对 $d_0=1/8$，在 $x=1/32$ 时
$$
\Phi(1/8,1/32)=\frac{3+2+1}{32}=\frac{3}{16};
$$
$x$ 再增时严格变小。
对 $d_0=1/4$，在 $x=5/48$ 时
$$
\Phi(1/4,5/48)=\frac{7+2}{48}=\frac{3}{16},
$$
同样为严格临界。
所以
$$
\boxed{
\mathcal C(G_F,d_\alpha,a+b)\le\frac1{32}\kappa+o(\kappa),
\qquad
\mathcal C(G_F,d_\beta,a+b)\le\frac5{48}\kappa+o(\kappa).
}
\tag{35}
$$
(33) 已保 $\nu\ge2$ 的所有复合线系；
不能只检查 $\nu=1$ 后省去 primitive 步骤。

将 (35) 代入 (30) 得：

**定理 2。**
$$
\boxed{
a_\eta\le\frac{13}{32}\kappa+o(\kappa),\qquad
b_\eta\le\frac{17}{48}\kappa+o(\kappa).
}
\tag{36}
$$
第一主项分别是
$3\kappa/8+\kappa/32$ 与 $\kappa/4+5\kappa/48$。
原 Clifford 常数为 $7/16$ 与 $3/8$，
所以两处都是严格改进。

## 6. 同一原物理像的单位秩

保持 R550 的整个实际理想块
$$
\mathcal I=F\mathcal H_2+e\mathcal H_2\subset\mathcal H_3,
$$
并用原高目标
$$
\varepsilon:\mathcal H_3\to
k[[t]][\epsilon]/(t^T,\epsilon^2),
\qquad \zeta\mapsto\eta+a_\epsilon\epsilon.
$$
此处 $a_\epsilon$ 是原 Gaussian 单位，
与前文 $a=\deg_tF$ 无关。

R550 已证明同一个有限评价的准确秩为
$$
\dim\varepsilon(\mathcal I)=\frac{7\kappa+3\chi}{2}-a_\eta,
$$
$$
\dim\varepsilon(\mathcal H_3)=\frac{9\kappa+3\chi}{2}-a_\eta-b_\eta.
\tag{37}
$$
全部 $\mathcal H_3$ 已由 R495 返回同一 $\mathcal W_D$，
未扩大 $D$ 或增添免费来源。
因此 (30) 给 (37) 的有限有效下界，
而 (36) 在临界窗给
$$
\boxed{
\dim\varepsilon(\mathcal I)\ge
\frac{99}{32}\kappa+o(\kappa),
}
\tag{38}
$$
$$
\boxed{
\dim\varepsilon(\mathcal H_3)\ge
\frac{359}{96}\kappa+o(\kappa).
}
\tag{39}
$$
这对应实际整限制中至少相同数量的单位 Smith 因子；
它也给包含该来源的完整原矩阵的单位秩下界。

没有把两个可能相交的单位块相加。
(38)、(39) 都从同一个准确式 (37) 读取。
原 $59/16=354/96$ 的 $\mathcal H_3$ 下界因而增加了
$5\kappa/96+o(\kappa)$；
不是将来源维数直接当物理像维数。

## 7. 指定类、全部原列与同一个 R 的剩余问题

本篇没有将 $\ker\alpha_\eta$ 或 $\ker\beta_\eta$ 置零。
R730 的指定 $UA|_Z$ 仍需判断是否属于
$\operatorname{res}_ZK_{\rm mir}$；
R741 的指定非 cube forcing 仍需通过
整个 $\operatorname{res}_C\mathcal W_D$ 的全长值和 normal 条件。
(36) 缩小这些实际可能像的维数，
但不单凭维数排除某个指定元素。

尤其没有假定原 $P^{\rm fact}$ 是全首核中前缀最大的元素，
没有把新非 cube 核重新强制成 cube，
也没有从新增单位秩产生额外原算术中央零。

对完整 $M$ 使用 $T_M$，继续保原 $P_{134}/U_0$、
$U_1/p$、$\xi_0$、两条十三行 carry、
低行右逆高尾、第三精度 $d_2/G_2$，
以及同一个
$$
P_2=P^{\rm fact}+pR,\qquad R\in\mathcal W_D.
$$
本篇不改变这个来源或修正量词。
指定 forcing 在全像中的非零、跨素数非零及主目标仍开放。

## 文献与原结果

- B. Poonen, *Gonality of modular curves in characteristic p*,
  Proposition 2.1，任意完美常数域上的函数域合成 Castelnuovo–Severi 不等式：
  [作者原稿](https://math.mit.edu/~poonen/papers/gonality.pdf)。
- M. Abdón and F. Torres, *On a F_{q^2}-maximal curve of genus q(q-3)/6*,
  §2, (2.2)，正特征 simple 线系的准确 Castelnuovo 数：
  [大学原稿](https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2001-36.pdf)。
  该文的正式修订刊于 *Beiträge Algebra Geom.* 46 (2005), 241–260，
  §2.3, (2.5)。
  它所引的正特征原始结果为 J. Rathmann,
  *The uniform position principle for curves in characteristic p*,
  *Math. Ann.* 276 (1987), 565–579, Corollary 2.8，
  [出版信息](https://doi.org/10.1007/BF01456986)。
- [R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)，
  原十九角曲面、整 $\mathcal H_j$ 与真实返回。
- [R507](R507-original-euler-resonance-and-actual-forcing-transpose.md)，
  原低于 $s$ 的 ODE 及其共振边界。
- [R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)，
  原两连接、完整首核限制与准确物理秩。
- [R730](R730-specified-ramification-class-linear-contact-bound-and-actual-mirror-kernel.md)，
  全正规分支、固定角极帽与指定实际镜轴商。
- [R741](R741-specified-noncubic-first-forcing-and-necessary-normal-smoothing.md)，
  同一非 cube 核的指定首次修正及全来源边界。
