# 原 X(6) 五次周期分母源的完整 Cartier 留数式

日期：2026-11-15。会话：serre-public-astra-20261115 / sigma_uniform。

**状态：下列有限有理模型、极阶、完整 Cartier 留数式及指定 CM 留数比较已证明；该指定留数的普遍非零、原 primitive / Legendre 同标签三单位仍开放。**
本篇接续 [XF 原全六层函数](2026-11-15-sigma-original-X6-weight-one-and-logarithmic-square.md)、
[PL 原 Schwarz / Lagrange 公式](2026-11-15-sigma-original-Schwarz-frame-and-critical-Lagrange-source.md) 和
[PC 原有限周期修正](2026-11-15-sigma-original-PF-cusp-Cartier-and-period-correction.md)。
所有代数步骤均为纸面推导；没有执行新的素数计算。

## 1. 只使用已证明整的首 p 多项式

保持原允许范围 $p=6N+5\ge41$，置
$$
r=(p-2)/3=2N+1,\qquad k=\mathbf F_p,\qquad D=1-8U^3.
$$
PC 的两个有限多项式写成
$$
A(U)=U\,\mathfrak a(U^3),\qquad
C(U)=\mathfrak c(U^3),
$$
$$
\mathfrak a(s)=\sum_{j=0}^{r}
 8^j\frac{(2/3)_j^2}{(4/3)_j j!}s^j,\qquad
\mathfrak c(s)=\sum_{j=0}^{r}
 8^j\frac{(1/3)_j^2}{(2/3)_j j!}s^j.
\tag{CR1}
$$
各分母和各非零系数均在 PC / PL 已证明的整范围内。
特别 $\mathfrak a(0)=\mathfrak c(0)=1$，
$\deg A=p-1,\deg C=p-2$。下文没有把完整非整周期级数
普通约化为一个全局函数；只使用这些指定的有限多项式。

在原 Fermat 模型上取
$$
X_6:\quad x^3+y^3=2,\qquad U=xy/2,
\qquad W=x^3-1=1-y^3,\qquad W^2=D.
$$
原 CM 点与标架为
$$
P_0=(0,\gamma),\qquad \gamma=2/\alpha,\qquad
\alpha^3=4,\quad\gamma^3=2,
\qquad dU|_{P_0}=\alpha^{-1}dx|_{P_0}.
\tag{CR2}
$$
因 $p\equiv2\pmod3$，$\alpha,\gamma$ 是 $k$ 中唯一的相应立方根。
这些均是 XF / PL 的原标记，没有另选一个只有相同 $j$ 的模型。

记
$$
\alpha_0=\frac{dy}{y^3-1}=-\frac{x^2}{D}\,dU,
\qquad
\beta=\left(\frac AC\right)^5\alpha_0.
\tag{CR3}
$$
这正是 PL 的五次分母源，符号保持如式。
若 $S_{p-6}$ 是 PL / KS 的原未筛平方卷积，则 PL14 给
$$
\boxed{
\left.\frac{\operatorname{Car}(\beta)}{dU}\right|_{P_0}
=4374\,S_{p-6}.
}
\tag{CR4}
$$
理由是 $\beta=-x^2A^5dU/(DC^5)$，$\beta$ 在 $P_0$ 正则，
其 $U$ 局部系数属于 $k$。Cartier 的常数项是
$[U^{p-1}](\beta/dU)$ 的 $p$ 次根，而该根在 $k$ 中不改变数值。

## 2. 所有可能极点都在首 p 极阶内

PC3 / PC16 的精确关系是
$$
\mathcal L A=0,\qquad
\mathcal L C=\kappa U^{p-1},\qquad
\mathcal L=\partial_U\circ D\partial_U-8U,
\quad \kappa\in k^\times.
\tag{CR5}
$$
因为 $C(0)=1$，其根都不在 $U=0$。
若 $C$ 在 $a$ 有重根且 $D(a)\ne0$，(CR5) 在该点给
$D(a)C''(a)=\kappa a^{p-1}\ne0$。因此根的重数恰为二；
也可直接由 $\deg C<p$ 排除高阶 Taylor 的特征 $p$ 例外。
$U:X_6\to\mathbf P^1$ 在有限 $D\ne0$ 处 etale，
所以这些点处 $\beta$ 的极阶至多十。

若 $D(d)=0$ 且 $C(d)=0$，则
$$
D'(d)C'(d)=\kappa d^{p-1}\ne0.
$$
故 $C$ 在 $U=d$ 是单根。曲线上的 $U-d$ 在该纤维有二阶零，
而 $\alpha_0$ 有简单极点，所以 $\beta$ 的极阶至多十一。
若 $C(d)\ne0$，这里只可能有 $\alpha_0$ 的简单极点。

为核实这里的 ramification，沿 $x^3+y^3=2$ 有
$$
dU=\frac{1-x^3}{y^2}\,dx.
$$
有限分歧点恰为 $x^3=y^3=1$，其中 $W$ 是局部参数，
$D=W^2$，而 $U-d$ 有二阶零。
$\alpha_0=dy/(y^3-1)$ 在这些点确有简单极点。

在三个无穷远点，$x,y$ 各有一阶极，$U$ 有二阶极。
因 $\deg A-\deg C=1$ 且两个最高系数都是单位，
$A/C$ 有二阶极。$\alpha_0$ 有一阶零，故 $\beta$ 有九阶极。
$A,C$ 的公因子只会降低有限极阶，不会破坏任何上界。
由 (CR3) 也没有其他极点。

综上，所有极阶都至多十一，严格小于 $p$。
局部 Laurent 公式因此说明
$$
\operatorname{Car}(\beta)
\text{ 只可能有简单极点，留数为 }
\operatorname{res}_Q(\beta)^{1/p}.
\tag{CR6}
$$
Cartier 在同一个几何点取留数的 $p$ 次根，不把极点位置任意换成
Frobenius 共轭点。

## 3. 原三挠平移消除全局正则余项

在 $k_2=\mathbf F_{p^2}$ 上取 $\zeta^3=1$、$\zeta\ne1$，并取原实际自同构
$$
\tau(x,y)=(\zeta x,\zeta^{-1}y).
\tag{CR7}
$$
它在射影 Fermat 曲线上没有不动点：有限点若不动则 $x=y=0$，
不满足曲线方程；无穷远点的两个非零齐次坐标之比则乘以
$\zeta^2\ne1$。一个 genus-one 曲线的无不动点有限阶自同构
是平移：选原点后若线性部分不是恒等，则 $1-\tau_{\mathrm{lin}}$
是非零同源并满射，从而平移部分可被一个点吸收，产生不动点。
因此 (CR7) 是实际非零三挠平移。

尤其可直接核其对正则微分的作用：$dx/y^2$ 是全局非零正则微分，且
$$
\tau^*(dx/y^2)=dx/y^2.
$$
另一方面 $U$ 不变，故
$$
\tau^*\beta=\zeta^2\beta,
\qquad
\tau^*\operatorname{Car}(\beta)
=\zeta\operatorname{Car}(\beta).
\tag{CR8}
$$
第二式同时使用 Cartier 与 pullback 的相容性及
$(\zeta^2)^{1/p}=\zeta$，没有省略半线性。

由 (CR6)，任意两个具有这些留数及 (CR8) character 的候选之差
是全局正则微分。但正则微分只有平移不变的一维空间，
与非平凡 $\zeta$ character 的交为零。因此：
$$
\boxed{
\operatorname{Car}(\beta)
\text{ 由其实际留数唯一确定，没有全局正则微分余项。}
}
\tag{CR9}
$$
这句话没有断言该微分在 $P_0$ 非零。

## 4. 把完整 Cartier 变成一个 P1 有理留数和

置
$$
s(y)=\frac{y^3(2-y^3)}8,
\qquad R(s)=\left(\frac{\mathfrak a(s)}{\mathfrak c(s)}\right)^5,
$$
并在 $k(y)dy$ 定义实际有理微分
$$
\nu(y)=
\frac{y^5(2-y^3)^{1-r}}{32(y^3-1)}
 R(s(y))\,dy.
\tag{CR10}
$$
因为 $p=3r+2$、$x^3=2-y^3$，逐项有
$$
x^p=x^2(2-y^3)^r,\qquad
\boxed{\beta=x^p\nu.}
\tag{CR11}
$$
这不是换掉原源，而是 (CR3) 的同一有理微分恒等式。
$X_6\to\mathbf P^1_y$ 是可分三次覆盖，所以 Cartier 与其 pullback 相容，
从而
$$
\boxed{\operatorname{Car}(\beta)
=x\,\operatorname{Car}_{\mathbf P^1_y}(\nu).}
\tag{CR12}
$$

这里 $\nu$ 的所有有限极点都能准确列出：
$y^3=2$、$y^3=1$ 和 $\mathfrak c(s(y))=0$。
在 $y^3=2$，其极阶恰为 $r-1=2N<p$；
$\mathfrak a(0)=\mathfrak c(0)=1$，所以没有隐藏的额外分母。
在 $\mathfrak c$ 的根上，(CR5) 的重数界给至多十阶；
若同时 $y^3=1$，则 $s'(y)=0$ 的二重分歧给至多十一阶。
$y=0$ 不是极点。
在 $y=\infty$，$\nu/dy$ 的阶为 $y^{7-p}$ 乘一个非零常数，
故 $\nu$ 有 $p-9\ge0$ 阶零。
所有显示极阶仍严格小于 $p$。

令 $\mathcal P$ 为上述有限实际极点集合，重合点只列一次，
$R_a=\operatorname{res}_{y=a}\nu$。
$\mathbf P^1$ 上的有理微分没有正则余项，故完整公式为
$$
\boxed{
\operatorname{Car}(\beta)
=x\sum_{a\in\mathcal P}R_a^{1/p}\frac{dy}{y-a}.
}
\tag{CR13}
$$
零留数点可保留为零项。式中 $p$ 次根在同一代数闭包取唯一根；
留数定理给 $\sum R_a=0$，也与 $\operatorname{Car}(\nu)$ 在无穷远正则一致。
这个有理式还给出 (CR9) 的一个显式实现。

## 5. 原 CM 点只取一个明确留数

令
$$
\mathcal R_p=\operatorname{res}_{y=\gamma}\nu\in k.
\tag{CR14}
$$
在 $y=\gamma$，$\operatorname{Car}(\nu)$ 的极部恰为
$\mathcal R_p\,dy/(y-\gamma)$。这里 $\gamma\in k$，
所以该留数的 $p$ 次根不改变数值。
由曲线方程
$$
y-\gamma=-\frac{x^3}{3\gamma^2}+O(x^6),
\qquad dy=-\frac{x^2}{y^2}\,dx,
$$
故
$$
\left.x\frac{dy}{y-\gamma}\right|_{P_0}=3\,dx|_{P_0}.
$$
$\operatorname{Car}(\nu)$ 的正则部分在乘以 $x$ 后是 $O(x^3)dx$，
不会影响这个值。因此 (CR2)、(CR4)、(CR12) 给
$$
\boxed{
\left.\frac{\operatorname{Car}(\beta)}{dU}\right|_{P_0}
=3\alpha\mathcal R_p,
\qquad
S_{p-6}=\frac{\alpha}{1458}\mathcal R_p.
}
\tag{CR15}
$$
可以不用局部 Cartier 展开再核常数：$U^p=x^py^p/2$，
所以 $U^{-p}\beta=2y^{-p}\nu$。从 $y$ 直线 pullback 到
$P_0$ 的 ramification 是三，且 $\nu$ 在 $\gamma$ 的极阶小于 $p$，
故其留数是 $6\gamma^{-1}\mathcal R_p=3\alpha\mathcal R_p$。

最后令 $v=y^3$、$w=2-v$。因为 $y^5dy=v\,dv/3$，
(CR10) 成为
$$
-\frac{(2-w)w^{1-r}}{96(1-w)}
 R\left(\frac{w(2-w)}8\right)dw.
$$
$v=y^3$ 在 $y=\gamma$ etale，因此其留数不乘三。
准确得到
$$
\boxed{
\mathcal R_p=-\frac1{96}\,[w^{2N-1}]
 \frac{2-w}{1-w}
 \left(
 \frac{\mathfrak a(w(2-w)/8)}
      {\mathfrak c(w(2-w)/8)}
 \right)^5.
}
\tag{CR16}
$$
所有在 $w=0$ 求逆的分母都是单位，所需次数 $2N-1$ 小于
$r=(p-2)/3$，因而只消费 (CR1) 的既有首 $p$ 整系数。
等价地，PL 的系数有新的单留数表达
$$
\boxed{
[U^{p-1}]\frac{x^2A^5}{DC^5}
=\frac{\alpha}{32}\,[w^{2N-1}]
 \frac{2-w}{1-w}
 \left(
 \frac{\mathfrak a(w(2-w)/8)}
      {\mathfrak c(w(2-w)/8)}
 \right)^5.
}
\tag{CR17}
$$
这里 $\alpha/32$ 来自原 CM 标架、Frobenius 和三次分歧；
不是可以自由删除的公共尺度。

## 6. 实际推进范围

(CR13) 确实消除了原 $C^{-5}$ 源在 genus-one 曲线上的
不明正则余项，并把指定 CM 值收紧到 (CR14) 的一个真实有理留数。
但是非零的其他留数只保证整个 Cartier 微分非零，
不会使 $\mathcal R_p$ 自动非零。
尤其 (CR16) 的 $\mathfrak c^{-5}$ 仍完整存在。

本篇比较的是原未筛 $S_{p-6}$。
R770 所需的同一个 primitive $h$、两个 Cartier 数及 Legendre 因子，
仍由 PL §6 的双变量不同单项式承载。
既不把它们设成一个变量，也不从 (CR15) 的未筛非零推筛后非零。
若要完成该原目标，还须对同一标签保留原 $Q_h$ 与
$P_{h-1}(1/\sqrt{-3})^2$ 权和实际 primitive 投影。
