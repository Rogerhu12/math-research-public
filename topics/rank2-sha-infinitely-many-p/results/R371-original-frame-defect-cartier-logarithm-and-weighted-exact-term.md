# R371：原 theta frame 差的显式 Cartier 对数与完整加权补项

日期：2026-11-13。**状态：已证明。** R369 的实际 frame 差有一个简单的完整有理表达。其 Cartier 像是一条显式对数微分，剩余部分有明确有理原函数；所有原点、非原点测试极和二挠点的极部均被保留。对任意原权，恰当微分所产生的加权补项也准确列出。该项不因未加权留数为零而消失，主目标未完成。

## 1. 同一原曲线、导子及有限 primitive

固定
$$
E_b:y^2=x^3+b,\qquad b=17,\qquad
p=6s-1>7,\quad p\nmid b,
$$
在完美的模 $p$ 剩余域 $k$ 上工作。
原不变导子和微分为
$$
Dx=2y,\qquad Dy=3x^2,\qquad dz=\frac{dx}{2y}.
\tag{1}
$$
R342/R346 的原有理函数记为 $Z=Z_p$，满足
$$
DZ=1,\qquad Z(O)=0,\qquad \operatorname{ord}_OZ=1.
\tag{2}
$$
它只在三个非零二挠点有极，每处极阶为 $p$。
这些都是同一个原 $Z_p$ 的性质；没有更换局部参数的全局延拓。

R356 的有限原函数为
$$
G_\sigma=
\sum_{i=0}^{p-2}\frac{(-1)^iZ^{i+1}}{(i+1)!}D^i(-x),
\qquad
DG_\sigma=-x+c_pZ^{p-1},
\tag{3}
$$
其中 $c_p\in k^\times$ 是该文的原常数。
另一合法 Gaussian 规范为
$G_\kappa=G_\sigma-\bar\delta_\kappa Z^p$。
因此
$$
D^{p-1}G_\kappa=D^{p-1}G_\sigma .
\tag{4}
$$
本篇的 frame 差正是 R369 的
$$
\chi=\frac1Z+Z^{p-1}D^{p-1}G_\sigma .
\tag{5}
$$
它不是为了改变测试点而任意添加的微分。

为避免与原 double-Euler 的变量 $r$ 混淆，以下把简单函数记为
$$
a=\frac{x^2}{y},\qquad F=1+Za.
\tag{6}
$$

## 2. 一个准确的 p 次根恒等式

**定理1。** 在同一个函数域 $k(E_b)$ 中，
$$
\boxed{D^{p-1}G_\sigma=\left(\frac{x^2}{y}\right)^p=a^p.}
\tag{7}
$$
因此
$$
\boxed{\chi=\frac{(1+Zx^2/y)^p}{Z}=\frac{F^p}{Z}.}
\tag{8}
$$

**证明。** 先支付 $D^p=0$。
$D$ 是椭圆曲线上的全局不变向量场，特征 $p$ 下 $D^p$ 仍是
全局向量场，所以 $D^p=cD$，$c\in k$。
在完美扩域中取 primitive 六次单位 $\zeta$，
原 CM 自同构满足 $I_\zeta D=\zeta^{-1}DI_\zeta$。
因此 $D^p$ 与 $D$ 的字符分别是 $\zeta^{-p}$、$\zeta^{-1}$。
$p\equiv-1\bmod6$ 且 $p>3$，两字符不同，故 $c=0$。
恒等式可下降到原剩余域。

于是 $D^{p-1}G_\sigma\in\ker D=k(E_b)^p$。
最后一个等式也可直接由 (2) 看出：$Z$ 是 separating parameter，
$[k(E_b):k(E_b)^p]=p$，非零导子的核必须恰是这个 $p$ 次幂子域。

从 (3) 再微分 $p-2$ 次，并用 $(p-1)!=-1$，得到
$$
D^{p-1}G_\sigma=-D^{p-2}x-c_pZ.
\tag{9}
$$
$D^{p-2}x$ 只在 $O$ 有至多 $p$ 阶极；
$Z$ 只在三个非零二挠点有 $p$ 阶极。
所以 (9) 的唯一 $p$ 次根 $q$ 至多在整个 $E_b[2]$ 的四点有简单极。

原 $Z$ 的 $\mu_6$ 型为一，$G_\sigma$ 的型为负一，
所以 $D^{p-1}G_\sigma$ 型为 $-p\equiv1\bmod6$，
其 $p$ 次根 $q$ 型为负一。
四维空间
$$
L\!\left(\sum_{T\in E_b[2]}T\right)
=\operatorname{span}_k\{1,\ 1/y,\ x/y,\ x^2/y\}
\tag{10}
$$
可由所列四个不同极部和 genus-one Riemann--Roch 直接验证。
其型分别为 $0,3,1,-1$，故 $q$ 必为 $a=x^2/y$ 的标量倍数。

在原点，$G_\sigma$ 的极部是 $z^{-1}$，故
$D^{p-1}G_\sigma$ 的极部为 $-z^{-p}$。
另一方面 $a=-z^{-1}+\cdots$，所以 $a^p$ 的极部也是 $-z^{-p}$。
标量因而为一，证明 (7)。将其代入 (5)，用 Frobenius
$(1+Za)^p=1+Z^pa^p$，即得 (8)。$\square$

此证明也给 (9) 的完整有理恒等式
$$
D^{p-2}x+c_pZ+(x^2/y)^p=0.
\tag{11}
$$
它保留了三个二挠点的全部极，而不仅是原点的有限 Taylor 比较。

## 3. 真正的对数 Cartier 像

记 $\mathcal C$ 为 Cartier 算子。因为 $dZ=dz$，
且 $\mathcal C(f^p\,d\log Z)=f\,d\log Z$，(8) 给
$$
\boxed{
\mathcal C(\chi\,dz)
=F\,d\log Z
=d\log Z+\frac{x^2}{y}\,dz.
}
\tag{12}
$$
(1) 又给准确恒等式
$$
\frac{x^2}{y}\,dz=\frac{x^2dx}{2y^2}
=\frac13\,d\log y.
$$
所以
$$
\boxed{
\mathcal C(\chi\,dz)
=\Lambda:=\frac13\,d\log(Z^3y),\qquad
\mathcal C^2(\chi\,dz)=\Lambda.
}
\tag{13}
$$
系数 $1/3$ 在 $\mathbf F_p$ 中，Cartier 的半线性没有额外常数。
(13) 使用完整原 $Z$；没有把它换成只有同一首项的形式变量。

还可直接给差的原函数，不需要只凭 Cartier 的核存在性。
对任意有理 $f$ 定义
$$
\mathcal I_Z(f)=
\sum_{i=0}^{p-2}\frac{(-1)^i Z^{i+1}}{(i+1)!}D^if.
\tag{14}
$$
逐项微分相消给
$$
D\mathcal I_Z(f)=f+Z^{p-1}D^{p-1}f.
\tag{15}
$$
在 separating parameter $Z$ 中，Cartier 的标准系数式
$$
\mathcal C(f\,dZ)=(-D^{p-1}f)^{1/p}dZ
$$
可由 $k(E_b)=\bigoplus_{j=0}^{p-1}k(E_b)^pZ^j$ 逐项验证。
因 $a\,dz=\frac13d\log y$ 被 Cartier 固定，所以
$$
D^{p-1}a=-a^p.
\tag{16}
$$
令
$$
\boxed{
K_p=\mathcal I_Z(a).
}
\tag{17}
$$
(15)、(16) 给
$$
DK_p=a-Z^{p-1}a^p=\frac{F-F^p}{Z}.
\tag{18}
$$
最终得到整个函数域中的完整式
$$
\boxed{
\chi\,dz=\frac13d\log(Z^3y)-dK_p.
}
\tag{19}
$$
这是实际 frame 差的分解，包含所有极部和全部 exact 项。

## 4. 原点、测试极、二挠点逐一保留

在 $O$ 取 (2) 的同一个参数 $Z$。原低阶展开为
$$
x=Z^{-2}-\frac b7 Z^4+\cdots,\qquad
y=-Z^{-3}-\frac{2b}7Z^3+\cdots,
$$
故
$$
a=-Z^{-1}+\frac{4b}7Z^5+\cdots,\qquad
F=\frac{4b}7 Z^6+\cdots.
\tag{20}
$$
因此
$$
\boxed{
\chi=\left(\frac{4b}7\right)^pZ^{6p-1}+\cdots.
}
\tag{21}
$$
显示系数为单位。它精确解释为何这个全局差在原短窗口中不可见，
却不是零函数。

$K_p$ 在 $O$ 正规。事实上 (14) 中每项至多有常数首项，
其总常数为
$$
-\sum_{j=1}^{p-1}j^{-1}=0.
$$
由 (18)、(20)，
$$
\boxed{K_p=\frac{2b}{21}Z^6+\cdots\quad\hbox{于 }O.}
\tag{22}
$$
所以 $K_p$ 是一个明确非恒定的有理函数；没有留下未定积分常数。

设 $P\ne O$ 且 $Z(P)=0$。
由 $DZ=1$，这个零简单；$y(P)\ne0$，故 $a$ 在此正规。
于是
$$
\boxed{
\operatorname{Res}_P(\chi\,dz)=1,\qquad
K_p(P)=0,\qquad
DK_p(P)=a(P).
}
\tag{23}
$$
这包括原全部 $B_p$ 测试点及固定 $x=0$ 的两个零点。
若回到 genus-two 覆盖，须按实际分歧指数拉回；
在原 $v,y$ 均为单位的测试点处是已付的 étale 拉回。

在三个非零二挠点，$a$ 有简单极，$Z$ 有 $p$ 阶极。
所以 (8) 给 $\chi\,dz$ 的极阶准确为 $p^2$。
(14) 的最高项 $i=p-2$ 给 $K_p$ 极阶准确为 $p^2-1$；
低项极阶更小，不可能取消它。
由 (19) 保留 exact 项后仍可准确读留数：
$d\log Z$ 的留数为 $-p=0$，$d\log y$ 的留数为一，故
$$
\boxed{\operatorname{Res}_T(\chi\,dz)=1/3
       \quad(T\in E_b[2]\setminus\{O\}).}
\tag{24}
$$
原点留数为零，没有其他极点。
在整个 $E_b$ 上，$Z$ 的非原点零共 $3p-1$ 个，
其留数和是 $-1$；(24) 的三点之和是一，准确满足全局留数定理。
没有将二挠点补偿隐藏在“无穷远余项”中。

## 5. 所有权的准确留数公式

对任意有理权 $f$，或在所用点的任意有限 Laurent 权，
由 $\operatorname{Res}d(fK_p)=0$，(19) 给
$$
\boxed{
\operatorname{Res}_P(f\chi\,dz)
=\frac13\operatorname{Res}_P\!\bigl(f\,d\log(Z^3y)\bigr)
 +\operatorname{Res}_P(K_p\,df).
}
\tag{25}
$$
式中第二项对一般 $f$ 并不为零。
因此不能把未加权的 exact 消去，直接用于原
$\boldsymbol q(\lambda,P)$ 或 canonical 列的加权观察。
(25) 正是可以代回原 Serre 伴随的完整补项。

对真正 $p$ 次幂权 $f=h^p$，$df=0$，第二项才准确消失。
这给一个实际的允许情形，并不把原一般权偷换成 Frobenius 常数。
所有两接触尾、原 $U_0/P_{134}$ 与十三行仍须在自己的 $f$ 中保留。

## 6. 这个 exact 项不是可免费的有理乘法规一

对 $m\in\mathbf F_p^\times$，考虑同一个函数域上的秩一连接
$$
\nabla_m=D+m\chi.
$$
其 $p$ 曲率准确为
$$
\boxed{
\Psi(\nabla_m)=
\frac{m(F^{p^2}-F^p)}{Z^p}
=-m(DK_p)^p\ne0.
}
\tag{26}
$$
证明只需特征 $p$ 的标量算子式
$(D+a_0)^p=D^p+D^{p-1}a_0+a_0^p$。
为直接核该式，左侧与乘函数的交换子是 $D^p=0$，
所以差为乘法算子；对常数一求值后的 complete Bell 展开中，
除 $a_0^p$ 和 $D^{p-1}a_0$ 外，所有系数都被 $p$ 整除：
其分母只含小于 $p$ 的阶乘，而分子含 $p!$。
这给所列算子恒等式。

在本篇 $D(F^p)=0$，故
$D^{p-1}\chi=-F^p/Z^p$。
与 $\chi^p=F^{p^2}/Z^p$ 合并，即得 (26)。
(22) 使 $DK_p\ne0$，从而非零性确实成立。

因此不存在非零全局有理函数 $u$ 满足
$D\log u=m\chi$；任何这样的乘法规一都会使 $p$ 曲率为零。
同样可由 (13) 看出：有理对数微分被 Cartier 固定，
而 $\chi\,dz\ne\Lambda$。
原有限指数多项式中用来抵消这项的截尾部分不能无证删除。

这仍允许在低于 $p$ 的局部窗口取正规指数；
R366 的局部单位权和 R369 的实际 $Z^{68}$ 移位没有矛盾。
本结果确定了二者之间的完整有理差，并明确说明
把它用于全局原配对所需保留的项。

## 7. 对当前主接口的意义

R369 已将原 $Q_0,Q_1$ 的有限 theta 模型留数作准确移位，
得到 $q_1,\ldots,q_{11}$ 的真实零列和其余共同尾的原始整单射。
本篇把其 global frame 差进一步写成 (19)、(25) 的固定公式。
要从原 $C_2$ 配对迫出那些尾的零，仍须控制
$\operatorname{Res}(K_p\,df)$ 和原全部二挠点／公共导子项；
不能只用 (23) 或 R363 的测试点值为零。
这里没有把整块矩阵在形式窗口外任意替换，也没有新增中央零。

## 引用

- [R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)、[R346](R346-original-off-origin-residue-injection-and-full-cartier-polar-part.md)：同一个原 $Z_p$、测试极及覆盖。
- [R356](R356-original-gaussian-zeta-primitive-and-all-test-pole-normalization.md)：$G_\sigma,G_\kappa$ 及原短规范。
- [R366](R366-original-two-degree-two-multipliers-and-joint-local-residue-primitivity.md)：两个真乘子、完整提升核运输及固定 Bézout。
- [R369](R369-original-finite-theta-frame-and-shifted-joint-residue-primitivity.md)：原有限 theta、$\chi$、真实 $Z^{68}$ 及移位留数。
