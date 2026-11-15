# 原四首对角的有理分部边界：完整 sigma/zeta 证书

日期：2026-11-15。**状态：本文的有理证书不存在结论已证明。**

本篇给出上一份完整低核反射 note 的准确处理边界。原四首行保留
$\Theta^{17},\Theta^{36},\Theta^{68},\Theta^{33}$ 后，不能在下面指定的
特征零有理微分域内，用一个保持原 charge 的有理 primitive，
将其完整无 $\zeta$ 被积函数消成端点项。证明允许证书对 $\zeta$
有任意有理分母，不只排除多项式试探。

这不是四个首系数共同非零的证明，也不排除依赖 $p$ 的特征 $p$
Frobenius 恒等式。它解释为什么已经闭合的 charge 零卷积
$[t^{s-1}](R_NH)$，不能直接替换原四条带 $\Theta$ 的完整卷积。

## 1. 原自变量、原来源和证书域

先用原共同 $b=1$ 模型
$$
E:\ y^2=x^3+1,\qquad
x(z)\sim z^{-2},\quad y(z)\sim-z^{-3},
$$
$$
D=\frac d{dz},\qquad Dx=2y,\quad Dy=3x^2,\quad
\frac{\sigma'}{\sigma}=\zeta,\quad D\zeta=-x.
\tag{1}
$$
原角及原 theta 变量为
$$
t=-x^{-3},\qquad \Theta=x\sigma^2,\qquad
\frac{D\Theta}{\Theta}=2\zeta+\frac{2y}{x}.
\tag{2}
$$
四个完整来源一律是
$$
A_\nu=\Theta^{n_\nu}tP_\nu(t),\qquad
(n_S,n_T,n_U,n_V)=(17,36,68,33).
\tag{3}
$$
这里 $tP_\nu=f_\nu$ 是 R821 的实际多项式，未截去任何原因子。
例如
$$
tP_S=\frac17t(t-1)(7+4t+16t^2)(1+8t),
$$
$$
tP_V=\frac17t(t-1)(7+4t+16t^2)(1+8t)^2
(4t-1)(-1+228t-48t^2+64t^3).
\tag{4}
$$
$P_T,P_U$ 也保持 R821 式 (2) 的完整分子。四个 $P_\nu$
均非零；本篇不改变其常数归一。

取抽象有理函数域
$$
F=\mathbf C(E)(Z),\qquad DZ=1,
\tag{5}
$$
并用 $Z=z$ 作实际均匀化嵌入。这个嵌入是单射：若一个关于
$Z$ 的非零多项式在 $(x(z),y(z),z)$ 上恒为零，
固定一个避开系数极点的普通点，再令 $z$ 加任意整数倍的非零周期，
便得到该多项式的无穷多个不同根。其各系数遂在普通点恒为零，
矛盾。

以后仍将 (5) 的变量写为 $Z$，以免把形式有理变量与取值混淆。
证书域是
$$
F(\zeta)=\mathbf C(E)(Z,\zeta),\qquad D\zeta=-x.
\tag{6}
$$
下节将同时证明 $\zeta$ 对 $F$ 超越；故这里确实可以按
$\zeta$ 的不可约分母逐项论证。

对于 $p=6s-1$，实际首对角是
$$
\alpha_\nu=[z^{p+1}]A_\nu
=\operatorname{res}_{z=0}
 \Theta^{n_\nu}tP_\nu(t)z^{-p-2}\,dz.
\tag{7}
$$
因此保持原 charge 的有理分部证书准确指
$$
D(\Theta^{n_\nu}V)=
\Theta^{n_\nu}tP_\nu(t)Z^{-p-2},
\qquad V\in F(\zeta).
\tag{8}
$$
右端是原完整被积函数；没有把它换成某个裸 $R$ 或 $H$ 的卷积。

## 2. $-x$ 在 $F$ 及其有限代数扩张中没有 primitive

**引理 1。** 不存在 $B\in F$ 满足 $DB=-x$。

**证明。** 若存在，将 $B$ 代入均匀化，所得亚纯函数与
$\zeta(z)$ 的导数相同，故两者之差为常数。

取定向周期基 $\Omega_1,\Omega_2$，记
$$
\zeta(z+\Omega_i)-\zeta(z)=\eta_i.
$$
由上一节的单射，实际解析恒等式准确给出 $F$ 中的有理函数恒等式
$$
B(Z+\Omega_i)-B(Z)=\eta_i,\qquad i=1,2.
\tag{9}
$$
先只看一个非零周期 $\Omega_1$。若 $B$ 关于 $Z$ 有有限极点，
其有限极点集在 $\overline{\mathbf C(E)}$ 中必须由
$Z\mapsto Z+\Omega_1$ 保持：否则 (9) 左端会有极点，而右端为常数。
特征零下非零平移的每个轨道都是无穷集，所以有限非空极点集
不可能保持。于是 $B$ 是关于 $Z$ 的多项式。

若其次数至少为二，则 $B(Z+\Omega_1)-B(Z)$ 的最高项
是 $d\Omega_1b_dZ^{d-1}\ne0$，仍不可能为常数。故
$$
B=aZ+b,\qquad a,b\in\mathbf C(E).
$$
两个周期同时代入 (9)，给
$$
a\Omega_1=\eta_1,\qquad a\Omega_2=\eta_2.
\tag{10}
$$
但沿一个基本平行四边形积分 $\zeta\,dz$，
边积分的准周期差与原点处留数一给出 Legendre 关系
$$
\eta_1\Omega_2-\eta_2\Omega_1=2\pi i\ne0
\tag{11}
$$
（反定向只同时改变符号）。(10) 与 (11) 矛盾。$\square$

**引理 2。** 若 $L/F$ 是任意有限代数扩张，也不存在
$A\in L$ 满足 $DA=-x$。特别，实际 $\zeta$ 不代数于 $F$。

**证明。** 特征零下微分在有限代数扩张中唯一延拓，并与域迹交换。
若 $DA=-x$，则
$$
B=\frac{\operatorname{Tr}_{L/F}A}{[L:F]}\in F,\qquad DB=-x,
$$
与引理 1 矛盾。$\square$

这一步使用完整的两周期关系；只知道 $\zeta$ 不是椭圆函数，
不足以排除它在 $\mathbf C(E)(Z)$ 中的有理表达。

## 3. 完整 Darboux 分母排除

在 $F[T]$ 中定义
$$
\delta|_F=D,\qquad \delta T=-x.
\tag{12}
$$
由引理 2，可将 $T$ 与实际 $\zeta$ 认同，而不产生代数关系。

**引理 3。** 任一正次数不可约 $q(T)\in F[T]$ 都不满足
$q\mid\delta q$。

**证明。** 将 $q$ 取为首一，令 $a$ 为它在 $F$ 的有限代数扩张中的根。
若 $q\mid\delta q$，则 $\delta q(a)=0$。另一方面，对 $q(a)=0$
用唯一延拓的微分求导，得到
$$
0=(D_{\rm coeff}q)(a)+q'(a)Da
  =\delta q(a)+q'(a)(Da+x).
$$
特征零使不可约 $q$ 可分，故 $q'(a)\ne0$，从而 $Da=-x$，
违反引理 2。$\square$

因此证书在任何有限 $\zeta$ 位置的极点，都不能靠一个
未列出的 Darboux 因子藏掉。这个结论覆盖任意次数的不可约分母，
不只 $\zeta$ 本身或线性猜测。

## 4. 有理证书定理

**定理。** 对任意
$$
m\in\mathbf C^\times,\qquad r,f\in F,\qquad f\ne0,
$$
方程
$$
\delta V+(mT+r)V=f
\tag{13}
$$
在 $F(T)$ 中无解。

**证明。** 假设 $V$ 在正次数不可约 $q$ 处有 $k>0$ 阶极点。
写 $V=q^{-k}v$，其中 $v$ 在 $q$ 处为单位。由于
$F[T]_{(q)}$ 中的正则有理函数经 $\delta$ 微分仍正则，
$$
\delta V=q^{-k}\delta v-kq^{-k-1}v\,\delta q.
$$
由引理 3，第二项在 $q$ 处恰有 $k+1$ 阶极点，第一项至多有
$k$ 阶极点。$(mT+r)V$ 也至多有 $k$ 阶极点；$f\in F$ 在这个
$T$ 的有限位置正则。因此最高极点无法抵消，矛盾。

于是 $V$ 没有有限 $T$ 极点，只能属于 $F[T]$。若其次数为
$h\ge0$、最高系数 $v_h\ne0$，则 $\delta V$ 与 $rV$
的次数至多为 $h$，而 $mTV$ 的最高项为
$m v_hT^{h+1}\ne0$。它不能等于次数零的 $f$。
$V=0$ 也不能满足 $f\ne0$。$\square$

此论证不要求 $m$ 为整数，也不要求 $f$ 为多项式。
$Z$、$x$、$y$ 的全部有理分母都已经包含在 $F$ 中。

## 5. 回到四个原首对角和原角换元

由 (2)，(8) 等价于
$$
DV+\left(2n_\nu\zeta+\frac{2n_\nu y}{x}\right)V
=tP_\nu(t)Z^{-p-2}.
\tag{14}
$$
这里 $m=2n_\nu\ne0$，$r=2n_\nu y/x\in F$，
右端也是 $F$ 中的非零元素。所以定理逐个排除四个原 (8)。
它排除的是保持全部原因子后的完整证书，不是某个低次 ansatz
失败的数值记录。

这也准确对应前一 note 的 $(t,C,H,R)$ 记号。必要时取有限代数扩张
$u=x^{-1/2}$，选择 $u\sim z$ 的原分支，则
$$
t=-u^6,\qquad
C=(1-t)^{-1/2}=-\frac1{u^3y},\qquad
H=\frac Zu,\qquad
R=uC\zeta=-\frac{x\zeta}{y},
\tag{15}
$$
$$
\Theta=(\sigma/u)^2,\qquad
Dt=-\frac{6ty}{x}.
\tag{16}
$$
引理 2 对这个有限扩张仍成立，故第 3–4 节的证明原样适用。
有理的 $t$-分部证书，乘以非零 $Dt$ 后就是 (14) 的
$z$-微分证书，不会因换变量而绕开结论。

前一 note 的完整首行仍是
$$
\alpha_\nu\equiv(-1)^s[t^{s-1}]
  \Theta^{n_\nu}P_\nu\,\frac C{H^2}\pmod p.
\tag{17}
$$
它来自 (7) 的准确换元和有限窗口内的
$H^p\equiv1$；后一步是模 $p$ 事实，不是特征零的全函数等式。
在其真实伴随式中，两项
$$
2n_\nu r_{s-1}\,\mathfrak B_{s-1}
 \!\left(\frac{\Theta^{n_\nu}P_\nu}{H}\right),
\qquad
[t^{s-1}]\frac{\Theta^{n_\nu}}H
 \big((6-2n_\nu)P_\nu+6tP_\nu'\big)
\tag{18}
$$
都继续保留。不能以有理分部为由省去后者或整个
$\Theta^{n_\nu}$ 指数。反之，已付的 $R_NH$ 闭式没有这些非零
charge，故不与本定理冲突。

## 6. 准确的未付范围

本文只排除特征零中保持原 charge 的
$\Theta^{n_\nu}F(\zeta)$ 有理 primitive：

- 它不排除在更大的函数域中引入新的积分或特殊函数；
- 它不排除特征 $p$ 特有的 Frobenius、Cartier 或
  依赖 $p$ 的有限除法恒等式；
- 它不把一个被积函数没有上述 primitive，变成其原点单个留数非零；
- 它不证明四个原 $\alpha_\nu$ 独立或不能同时为零，
  更不从分级 charge 的区别添加一个中央零条件。

尤其在特征 $p$ 中，迹除以扩张次数和最高项系数的非零性
都不能不加条件照搬。原 R647 的完整 rational/Cartier 读取、
R828 的 $b_\Theta+a_pB_4v$、同一个 $K_1/C_1$ 及全部 native
Schur 项仍是下一实际对象。本文没有用这个方法边界替代它们的判定。

## 依赖

- [R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)：
  四个实际来源、原 $\Theta/t$ 和全部中央归一。
- [完整低核反射与 RH 卷积](2026-11-15-original-first-diagonal-full-reversal-and-rh-convolution.md)：
  (15)、(17)、(18) 的同一负角与全部伴随项。
- [R828](../results/R828-original-four-high-axis-reflection-and-native-central-compatibility.md)：
  原四个高轴与实际 Schur 相容式。
- [R647](../results/R647-original-three-source-rational-model-and-five-cartier-conditions.md)：
  本文没有替换的原特征 $p$ rational/Cartier 层。

所有显示结论由上述微分、域迹、有限极点及周期论证证明。
本篇不需要数学数值执行，也没有生成可重算输出。
