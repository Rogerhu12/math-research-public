# R903 — 原正水平端点的全核值单射与同源二步限制

日期：2026-11-16。**状态：下述原完整四块核的正水平值单射、准确最高 charge 帽及其强窗范围已证明。指定 forcing 和真实二步像仍未判定，主目标未完成。**

[R902](R902-original-four-block-kernel-and-first-normal-injectivity.md)
给第一法向值 $V_1$ 的单射。本篇处理不同的真实组合
$V_1-3bV_0$，其在原严格正水平上消失。
证明保同一个 $G$，并实际支付最高 charge 截面的全部次数成本。
两个单射并不作为独立秩相加。

## 1. 同一原四块与两种水平

沿用 R836/R840/R902 的原十九角曲面、几何整曲线及截面格
$$
C=(F=0),\quad P=(0,1),\quad
N=\mathcal O_C(C),\quad
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
\kappa=C^2,
$$
$$
\mathcal E=Y\partial_Y,\qquad e=\mathcal EF,\qquad e(P)\ne0,
\qquad b=\deg_YF,\quad 3b<p,\quad F(t,0)\ne0.
\tag{1}
$$
本篇 $e$ 仍为 Euler 截面，另用
$$
e_+=C.H_+,\qquad Z_+=C\cap H_+
\tag{2}
$$
记原严格正水平的交数与完整交概形。
$C$ 经过有限单位点 $P$，故不等于 $H_+$，
$Z_+$ 是 $C$ 上的有效 Cartier 除子，长度 $e_+\ge0$。
负水平及其交数仍记 $H_-$、$Z_-$、$z_-$。

只在原已付返回
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D},
\qquad q_{\rm src}(P)\ne0
\tag{3}
$$
内使用下述结论。
原 $q_{\rm src}$、总 charge 四十、$P_{134}/U_0$ 的全部 Euler 项
由 R836 的完整单位下三角逆运输，不单独删除。

写 $g=\psi e^\eta$、$\operatorname{ord}\eta=h$，保持
$$
h<T\le2h,\qquad T-h>\kappa,
$$
$$
T=s-r-13,\quad
\ell_{\rm eff}=\max(\ell-r,0)<T,\quad
H_*=\min(T,h+\ell_{\rm eff}),
\tag{4}
$$
并要求
$$
\boxed{H_*>2\kappa.}
\tag{5}
$$
相对 $J$ 单独使用时按其自己的长度另取 $T$，不换掉 (4) 的物理十三行。

令 $K_{4,T,\ell_{\rm eff}}$ 为 R902 的真实四块核：
前三个 Euler 值在 $g$ 上消到 $T$，第四个消到 $\ell_{\rm eff}$。
对同一个 $G$ 记
$$
V_i=(\mathcal E^iG)|_C.
$$
有限逆 Taylor 已付
$$
V_0,V_1\in H^0(C,N^3(-TP)),\qquad
V_2\in H^0(C,N^3(-H_*P)).
\tag{6}
$$
这里没有增加第四长行。

## 2. 真实最高 charge 的原点帽

采用 R495 的原多项式框
$$
F(t,Y)=\sum_{i=0}^b f_i(t)Y^i,\qquad
u=\max_i(\deg f_i-4i)\ge0.
$$
原类为
$$
C=bS_0+(u+4b)f-\sum_{i,j}\mu_{i,j}E_{i,j}^{*}.
\tag{7}
$$
令 $\mathcal N$ 为四条负 $Y$ 权链的底点：
$t=0$、$h_7$ 的两个几何根、$t=1$。
其首重数分别为 $\mu_{i,1}$；特别记零纤维的首重数为 $\mu_{0,1}$。
R815 的严格正水平类给准确式
$$
\boxed{e_+=u+4b-\sum_{i\in\mathcal N}\mu_{i,1}.}
\tag{8}
$$
不分裂的 $h_7$ 点在此按两个几何点计数；
等价地在原域保相应闭点次数。

**引理 1。** 若原 $G\in\mathcal H_3$ 只含最高 charge，
$$
G(t,Y)=a(t)Y^{3b}\ne0,
$$
则
$$
\boxed{\operatorname{ord}_{t=0}a(t)\le3(e_++\mu_{0,1}).}
\tag{9}
$$

**证明。** R495 §4 的真正截面帽给
$$
\deg_t a\le3u+12b.
$$
在每个 $i\in\mathcal N$ 的第一吹起中心，
正水平图中的方程是 $x^{3b}G$，$x=Y^{-1}$。
对纯最高 charge，它就是 $a(t)$。
原截面须在这个中心有至少 $3\mu_{i,1}$ 重零，故
$$
\operatorname{ord}_{t=t_i}a\ge3\mu_{i,1}.
$$
把除 $t=0$ 外的三个几何底点的这些零全部扣除，得到
$$
\operatorname{ord}_{0}a
\le3u+12b-3\sum_{i\in\mathcal N,\ i\ne0}\mu_{i,1}
=3(e_++\mu_{0,1}).
$$
中间吹起、两条正权链与底无穷远的其它条件仍保持；
本引理只使用其中必要的一组条件作上界，不放宽来源格。
证毕。

特别，引理 1 不把 $\deg_t a$ 错读成 $3u$；
原 $4i$ 底次数与三处非零有限角的强制零均已支付。

## 3. 正水平组合在整个四块核上单射

**定理 2。** 在 (1)–(5) 下，另若
$$
\boxed{T>3(e_++\mu_{0,1}),}
\tag{10}
$$
则真实映射
$$
\boxed{
G\longmapsto V_1-3bV_0
}
\tag{11}
$$
在 $K_{4,T,\ell_{\rm eff}}$ 上单射。

**证明。** 设 (11) 作为整个 $C$ 上的限制截面为零。
置 $\mathcal L=\mathcal E-3b$。
$\mathcal L$ 保原 $\mathcal H_j$，并在同一 $G$ 上给
$$
\mathcal LG=FA,\qquad A\in\mathcal H_2.
\tag{12}
$$
这是原限制序列的全局除 $F$，不只在函数域作形式除法。

再作用一次 $\mathcal L$，在 $C$ 上有
$$
(\mathcal L^2G)|_C=e|_C\,A|_C
=V_2-6bV_1+9b^2V_0.
\tag{13}
$$
由 (6)，右边在 $P$ 的阶至少 $H_*$；
$e(P)$ 是单位，故 $A|_C$ 也消到 $H_*>2\kappa=\deg N^2$。
因此 $A|_C=0$，原限制序列准确给
$$
A=FL,\qquad L\in\mathcal H_1.
$$
所以
$$
\mathcal LG=F^2L,\qquad
\mathcal L^2G=2FeL+F^2\mathcal LL.
\tag{14}
$$
$\mathcal L^2G=\mathcal E^2G-6b\mathcal EG+9b^2G$
仍是原前三长行的同源线性组合，故在 $g$ 上消到 $T$。
把 (14) 在 $g=\psi e^\eta$ 上准确展开，得到
$$
\mathcal L^2G(t,g)
=2e(t,\psi)^2\eta\,L|_C\pmod{t^T}.
\tag{15}
$$
其它项含 $\eta^2$；移位常数 $3b$ 只出现于这些较高项。
于是
$$
\operatorname{ord}_P(L|_C)\ge T-h>\kappa.
$$
所以 $L|_C=0$，继而 $L=cF$、$c\in k$。现在 (12) 变成
$$
(\mathcal E-3b)G=cF^3.
\tag{16}
$$
比较原多项式框的最高 $Y^{3b}$ 系数。
左侧该系数准确为零，右侧为 $c f_b(t)^3$。
因 $f_b\ne0$，有 $c=0$。

剩下 $(\mathcal E-3b)G=0$。
原 charge 全在 $0,\ldots,3b$，并且 $3b<p$，
所以它的核恰为纯最高 charge：
$$
G=a(t)Y^{3b}.
$$
$g(0)=1$ 是单位，第一长行迫 $\operatorname{ord}_0a\ge T$。
引理 1 和 (10) 迫 $a=0$，从而 $G=0$。证毕。

这个证明没有对任意移位 $c$ 声称相同结论。
真正端点 $3b$ 使 (16) 的最高系数先迫 $c=0$；
一般移位的同次齐次项和实际临界值不能按此删去。

## 4. 正水平的全交概形与直接接触门

在严格正水平的真实单位框中，
$$
\widehat G=x^{3b}G,\qquad
x^{3b}(\mathcal E-3b)G=-x\partial_x\widehat G.
\tag{17}
$$
故 $(\mathcal E-3b)G$ 沿整个 $H_+$ 消失。
这在与例外曲线相交的端点仍成立：
严格正水平的框只另含原底坐标因子，Euler 不微分这些因子。
(17) 也与已付十九角线性化相容。

因此 (11) 实际落在
$$
\boxed{
H^0(C,N^3(-TP-Z_+)).
}
\tag{18}
$$
$Z_+$ 使用完整 Cartier 交概形，包括非约化交、固定角端点、
原曲线奇点和剩余域；不是只扣不同的正水平点。

由定理 2 得
$$
\dim K_{4,T,\ell_{\rm eff}}
\le h^0(C,N^3(-TP-Z_+)).
\tag{19}
$$
特别，若这个原四块核非零，则必要有
$$
\boxed{T+e_+\le3\kappa.}
\tag{20}
$$
反门 $T+e_+>3\kappa$ 在 (1)–(5)、(10) 的范围确实排除本篇的整个子格核。
等号只给零次数线束，不能直接认其没有截面。
(19) 不称右侧每个截面可由原来源实现。

## 5. 原 r=2 强窗自动支付最高 charge 帽

现在明确限于原 $r=2$ profile、$C.f_0=3$、$b\ge5$。
这里 $f_0$ 是原严格零纤维，所有中间吹起仍保留。
R815 的 nef 链给
$$
\mu_{0,1}\le\sum_j\mu_{0,j}=b-3.
$$
R819 的完整原 nef 余量界给
$$
\kappa\ge(b-3)e_++3b.
\tag{21}
$$
于是
$$
\begin{aligned}
2\kappa-3(e_++\mu_{0,1})
&\ge2(b-3)e_++6b-3e_+-3(b-3)\\
&=(2b-9)e_++3b+9>0,
\end{aligned}
\tag{22}
$$
因为 $e_+\ge0$、$b\ge5$。
由 (4) 的 $T>2\kappa$，(10) 自动成立。

因此在这些实际 profile 内，只须保原短窗门
$H_*>2\kappa$，就可直接使用 (11)、(18)–(20)。
特别，已经成立的强窗 $h\ge\kappa+14$、
$T=2h-13$ 配上 $\ell_{\rm eff}\ge T-h$ 即满足全部要求。
本篇不新造一个具有该接触的 $F$，
也不把其它 $r$ 或未付 $C.f_0=3$ 的来源套入 (21)。

## 6. 正负水平必须来自同一个二步链

若再保持 R902 的 $T>3z_-$ 及
$$
\ell_{\rm eff}\ge T-h,
$$
则 $H_*=T$，同一 $V_0,V_1,V_2$ 都在
$V_T=H^0(C,N^3(-TP))$，且
$$
D_3(V_0)=V_1|_Z,\qquad D_3(V_1)=V_2|_Z.
\tag{23}
$$
定义两个真实端点坐标
$$
U_-=V_1,\qquad U_+=V_1-3bV_0.
\tag{24}
$$
R902 与本篇分别给两个单射，且
$$
U_-\in H^0(C,N^3(-TP-Z_-)),\qquad
U_+\in H^0(C,N^3(-TP-Z_+)).
$$
二者都属于 R836 的实际 $W_T$：
对 $U_-$ 的后继值是 $V_2$，对 $U_+$ 的后继值是
$V_2-3bV_1$。准确的共同关系为
$$
\boxed{
V_0=(U_--U_+)/(3b),\qquad
D_3(U_--U_+)=3b\,U_-|_Z.
}
\tag{25}
$$
所有式子使用同一个原 $G$。两端的值空间不独立，
因此不把两个单射的秩或消失除子相加；
尤其不能从 (24) 断言 $V_0$ 同时消在 $Z_-$ 与 $Z_+$。

式 (25) 是实际必要关系，不是两个端点空间的满像定理。
原 $2Z$ 的第二层、真实 $3\eta$ 镜轴、同一个最后 $cF^3$
和剩余第四短尾继续由 R840 联立。
它们尚未被这些端点关系消除。

对一个指定完整物理目标，若两个原解的整个
$(\mathcal EG-3bG)|_C$ 相同，其差由定理 2 为零。
因此这一正水平坐标也至多对应一个实际解；
不保证该坐标可实现，更不决定指定 $[b_0]$ 的取值。
原 $q_{\rm src}$ 的所有 Euler 项、同 $K_{\rm corr}/H_{\rm corr}$、
全部十九边界、三个十三行带及同 $R/S$ 更高位保持。
本篇没有把该显示子格换成整个 $\mathcal W_D$。

依赖：[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)
§§2、4 的原框与全截面帽；
[R815](R815-complete-original-mori-nef-cones-and-s-fibration.md)
的正水平类与原 nef 链；
[R819](R819-original-nef-surplus-and-s-projection-degree.md)
的余量界；
[R836](R836-original-restricted-euler-values-and-three-long-kernel-presentation.md)、
[R840](R840-original-double-ramification-euler-image-and-unique-normal-tail.md)、
[R902](R902-original-four-block-kernel-and-first-normal-injectivity.md)。

本篇只有精确来源、系数比较及交数证明，没有新增数学执行或数值样本。
