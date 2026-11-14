# R202. 原两权的有理椭圆参数与准确非零 Cartier 提升障碍

日期：2026-11-12。**状态：已证明；给原 R197 两权的准确模 $p$ 有理留数表示，并证明同一全局有理原函数不能提升到模 $p^2$。不证明目标行列式或完整中央导数非零。**

## 1. 固定覆盖和原微分

设 $p=4r-1\ge7$ 为素数。原共同曲线是
$$
E_0:\ y^2=x^3-x,\qquad \omega_0=\frac{dx}{2y}.
$$
R57、R197 的 $u=x^{-1/2}$ 不是 $E_0$ 上的全局有理函数。
这里明确使用固定二同源覆盖
$$
\mathcal C:\ v^2=1-u^4,\qquad O=(0,1),\qquad
\varphi(u,v)=(u^{-2},-v u^{-3}).
\tag{1}
$$
取光滑射影完备化后，$\varphi:\mathcal C\to E_0$ 是次数二的同源，
且
$$
\varphi^*\omega_0=\frac{du}{v}=:\omega.
\tag{2}
$$
在 $O$ 处取 $v(0)=1$，所以这仍是原严格形式坐标
$$
z(u)=\int_0^u\frac{dt}{\sqrt{1-t^4}}
=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}u^{4n+1},
\qquad z=u+O(u^5).
\tag{3}
$$
以下全局有理函数在这个固定覆盖上定义；没有把 $\mathcal C$ 未经说明地当作 $E_0$ 的双有理模型。

置 $d=(p-1)/2=2r-1$，并定义
$$
N_p(u)=\sum_{n=0}^{d}
 \frac{(-1)^n\binom dn}{4n+1}u^{4n+1},
\qquad
Z_p=\frac{N_p(u)}{v^p},
\qquad
\alpha_p=Z_p\,d\log v.
\tag{4}
$$
所有 $4n+1$ 都在 $[1,2p-1]$ 内并与 $p$ 互素：
唯一可能的非零 $p$ 倍数是 $p$，而 $p\equiv3\pmod4$。
所以这些是 $p$ 整的有理函数和有理微分。

记
$$
\kappa_p=
 \frac{\binom{2r-2}{r-1}}{4^{r-1}}\in\mathbf F_p^\times,
\qquad
\mathfrak h_p=
 \sum_{n=0}^{d}\frac{(-1)^n\binom dn}{4n+1}
 \in\mathbf F_p.
\tag{5}
$$
$\kappa_p$ 正是 R197 中 $p[z^{p+1}]\log\theta$ 的约化。

### 1.1. 参数及误差实际降回原曲线

置 $h_p(s)=N_p(u)/u$，其中 $s=u^4$。
虽然 $u$ 不在 $\mathbf Q_p(E_0)$ 中，(4) 的组合却准确下降：
$$
Z_p=
 -\frac{x^{(3p-1)/2}h_p(x^{-2})}{y^p},
\qquad
\alpha_p=
 Z_p\left(d\log y-\frac32\,d\log x\right).
\tag{5a}
$$
两式在特征零就成立；第一式的分子是 $x$ 的多项式，
最低次幂为 $(p+1)/2$。
因此下面的微分恒等式和不可提升结论同时在原 $E_0$ 上成立。
固定覆盖只是把计算写成二项式和的工具，不是一个变动扩域。

## 2. 特征零恒等式与准确两权窗口

由 $N_p'(u)=(1-u^4)^d=v^{p-1}$，在特征零已有
$$
\boxed{\quad \omega-dZ_p=p\,\alpha_p. \quad}
\tag{6}
$$
这里微分作用在曲线变量，$p$ 是常数。
约化后因此有
$$
d\overline Z_p=\overline\omega.
\tag{7}
$$

原 $z(u)$ 的所有次数小于 $3p$ 的系数都 $p$ 整：
分母 $4n+1<3p$ 不可能是 $p$ 或 $2p$。
式 (7) 与 (3) 的导数相同，而二者只含 $u^{4n+1}$。
特征 $p$ 中导数为零的正次数单项是 $p$ 的倍数；
满足 $pk\equiv1\pmod4$ 的最小正 $k$ 是 $3$。
故
$$
\boxed{\quad
 \overline Z_p(u)\equiv \overline{z(u)}\pmod{u^{3p}}.
 \quad}
\tag{8}
$$
二者一次项均为一，形式反函数也在同一范围一致。
特别地
$$
p+1,\quad 2p+2 <3p,
\tag{9}
$$
所以 R197 原两权的**整坐标换元部分**可以由真正有理函数
$\overline Z_p$ 代替。这里先按 R197 消去唯一非整 theta 指数项；
不能在未正规化的有分母原级数上任意约化。

## 3. 两个基本 Cartier 值

在 $k(\mathcal C)$ 上使用 Cartier 算子 $\mathcal{C}ar$，
其中 $k$ 是任意包含 $\mathbf F_p$ 的完美域。
对一个 $p$ 基 $t$，
$$
\mathcal{C}ar\!\left(
 \sum_{j=0}^{p-1}a_j^p t^jdt\right)=a_{p-1}dt.
\tag{10}
$$
我们只用它的基本性质
$$
\mathcal{C}ar(df)=0,\qquad
\mathcal{C}ar(f^p\eta)=f\,\mathcal{C}ar(\eta),\qquad
\mathcal{C}ar(f^{p-1}df)=df.
\tag{11}
$$
最后一式可在 $df\ne0$ 时以 $f$ 为 $p$ 基读取；
$df=0$ 时两边均为零。对 $d\log f$ 也有
$\mathcal{C}ar(d\log f)=d\log f$。

本曲线直接给
$$
\overline\omega=v^{-p}(1-u^4)^ddu.
$$
右边多项式次数为 $2p-2$，所有指数都是 $4$ 的倍数，
其中没有 $p-1$，也没有第二个可被 Cartier 读取的指数。
同理，$u^2(1-u^4)^d$ 中唯一被读取的指数是 $p-1$，
来自 $n=r-1$。所以
$$
\boxed{\quad
\mathcal{C}ar(\overline\omega)=0,\qquad
\mathcal{C}ar(u^2\overline\omega)=\kappa_p\overline\omega.
\quad}
\tag{12}
$$
这里
$$
(-1)^{r-1}\binom{(p-1)/2}{r-1}
 =\frac{\binom{2r-2}{r-1}}{4^{r-1}}\pmod p
$$
来自 $\binom{-1/2}{n}=(-1)^n\binom{2n}{n}/4^n$。
$\kappa_p\ne0$，因为 $2r-2<p$。

## 4. 完整有理部分分式计算

在 $\overline{\mathbf F}_p$ 上令 $a$ 遍历 $a^4=1$。
从 (4) 得
$$
\overline\alpha_p
 =v^{-p}\left(\frac{-2N_p(u)u^3}{1-u^4}\right)du.
\tag{13}
$$
括号中的有理函数只在四个 $u=a$ 处有简单极点，留数是
$$
\frac{N_p(a)}2=\frac{a\mathfrak h_p}{2}.
\tag{14}
$$
其多项式部分只含 $u^{4j}$，次数至多 $2p-2$，
因此该多项式部分乘 $du$ 的 Cartier 值为零。
又因 $p\equiv-1\pmod4$，
$a^{1/p}=a^{-1}$。逐个简单极点应用 (11)，得到
$$
\begin{aligned}
\mathcal{C}ar\!\left(
 \frac{-2N_p(u)u^3}{1-u^4}du\right)
 &=\frac{\mathfrak h_p}{2}
   \sum_{a^4=1}\frac{a^{-1}\,du}{u-a}\\
 &=\frac{2\mathfrak h_p u^2}{u^4-1}\,du.
\end{aligned}
\tag{15}
$$
第二步使用精确部分分式
$$
\sum_{a^4=1}\frac{a^{-1}}{u-a}
 =\frac{4u^2}{u^4-1}.
$$
把外面的 $v^{-p}$ 拉出 Cartier，并用
$$
d(u^3/v)=2u^2v^{-3}du+u^2\overline\omega,
$$
得到所需完整恒等式
$$
\boxed{\quad
\mathcal{C}ar(\overline\alpha_p)
 =\mathfrak h_p u^2\overline\omega
    -\mathfrak h_p\,d(u^3/v).
\quad}
\tag{16}
$$
用 $u^2=1/x$、$u^3/v=-1/y$，式 (16) 在原曲线上成为
$$
\mathcal{C}ar(\overline\alpha_p)
 =\mathfrak h_p\left(\frac{\overline\omega_0}{x}
                          +d(1/y)\right).
\tag{16a}
$$
这个等式在原 $\mathbf F_p(\mathcal C)$ 上成立；
使用四次单位根只是为了写清有理部分分式。

## 5. 有限 Beta 和与 Wilson：常数准确为负一

有限二项式积分恒等式给
$$
\mathfrak h_p
 =\frac{4^d d!}{\prod_{n=0}^{d}(4n+1)}
 =\frac{(2r-1)!(r-1)!}{4(3r-1)!}\pmod p.
\tag{17}
$$
最后一步只用 $1/4\equiv r\pmod p$，且
$3r-1<p$。因此 $\mathfrak h_p\ne0$，并且
$$
\mathfrak h_p\kappa_p
 =\frac{(2r-1)!(2r-2)!}
        {4^r(r-1)!(3r-1)!}.
\tag{18}
$$
Wilson 配对分别给
$$
((2r-1)!)^2=1,\qquad
(r-1)!(3r-1)!=(-1)^r\pmod p.
$$
因为 $2r-1\equiv-1/2\pmod p$，式 (18) 的分子是 $-2$。
另一方面
$$
4^r=2^{(p+1)/2}=2(2/p)=2(-1)^r\pmod p.
$$
所以
$$
\boxed{\quad \mathfrak h_p\kappa_p=-1.\quad}
\tag{19}
$$
结合 (12)、(16)，得到无未知标量的结果
$$
\boxed{\quad
 \mathcal{C}ar^{\,2}(\overline\alpha_p)
       =-\overline\omega\ne0,\qquad
 \mathcal{C}ar^{\,3}(\overline\alpha_p)=0.
 \quad}
\tag{20}
$$

### 5.1. 参考单位准确位于首个 $p^2$ 对数层

在 $O$ 的 $u$ 坐标下，$Z_p\in\mathbf Z_p[[u]]$，
且可写 $\alpha_p=\sum_{n\ge0}a_nu^n\,du$，所有 $a_n$ 都整。
由 (20) 读常数项，
$$
a_{p^2-1}\equiv-1\pmod p.
\tag{20a}
$$
式 (6) 的局部积分准确为
$$
z(u)-Z_p(u)=
 p\sum_{n\ge1}\frac{a_{n-1}}n u^n.
\tag{20b}
$$
当 $1\le n<p^2$ 时，$p/n$ 为 $p$ 整，因此
$$
[u^n]z(u)\in\mathbf Z_p\quad(1\le n<p^2),
\qquad
\boxed{\quad p[u^{p^2}]z(u)\equiv-1\pmod p.\quad}
\tag{20c}
$$
所以首个非整椭圆对数系数准确出现在 $u^{p^2}$，
其赋值为 $-1$。严格反函数在这一首坏阶取相反系数，
故其四次坐标的相对因子首次 carry 位于
$w^{(p^2-1)/4}$，与 R199 的端点规范一致。

这里不要求 $\alpha_p$ 的所有 $u^{mp-1}du$ 系数为零；
$n<p^2$ 的整性仅用 $p/n\in\mathbf Z_p$。
参考单位 (20a) 因而确在更深的坐标层，
并不自动进入 $p+1,2p+2$ 两个原中央行。

还有一个明确的次数信息：在四个 $v=0$ 的点，
$N_p(a)=a\mathfrak h_p\ne0$，故 $\overline Z_p$ 各有准确
$p$ 阶极点；在无穷远处它是零点而不是极点。
因此 $\overline Z_p:\mathcal C\to\mathbf P^1$ 的次数为 $4p$。
该参数定义在固定覆盖上，但它本身的极点阶数随 $p$ 增长。

### 5.2. 固定二同源商上的准确次数 $p$

写 $h_p(s)=\sum_{n=0}^d c_ns^n$。模 $p$ 有
$$
c_{d-n}=c_n,\qquad s^d h_p(1/s)=h_p(s).
\tag{20d}
$$
这是因为 $d$ 为奇数且
$4(d-n)+1\equiv-(4n+1)\pmod p$。
由 (5a)，在原曲线上可改写
$$
\overline Z_p=
 -\frac{x^{(p+1)/2}h_p(x^2)}{y^p}.
\tag{20e}
$$
它准确不变于 $T_0=(0,0)$ 的平移
$$
(x,y)\longmapsto(-1/x,y/x^2).
$$
因此 $\overline Z_p$ 还下降到固定二同源商
$$
E_+:\ Y^2=X^3+4X,\qquad
X=x-1/x,\quad Y=y(1+1/x^2),
\qquad
\frac{dX}{2Y}\longmapsto\omega_0.
\tag{20f}
$$
在 $E_0$ 上，$\overline Z_p$ 仅在 $(1,0),(-1,0)$ 各有
$p$ 阶极点，所以次数为 $2p$；这两个点在商上同为
$T'=(0,0)$，下降参数仅在 $T'$ 有一个 $p$ 阶极点，
其映射次数准确为 $p$。其微分仍是商上的不变微分。

此外
$$
h_p(s)+4s h_p'(s)=(1-s)^d.
\tag{20g}
$$
结合 $h_p(0)=1$ 与 $h_p(1)=\mathfrak h_p\ne0$，
可知 $h_p$ squarefree。因为 $d$ 为奇数，(20d) 还给
$h_p(-1)=0$；其余根成互反对。
这些都是所选有理参数的确切几何性质，
不宣称其移动零纤维是一个完整挠点轨道。

### 5.3. 保原两权 jet 的最优次数 $2p$ 修复

本节全在特征 $p$ 的 $E_+$ 上进行，仍以 $\overline Z_p$
表示 (20f) 的下降参数，记 $\omega_+=dX/(2Y)$。
取固定点
$$
P_*=(2,4),\qquad T'=(0,0),\qquad 2P_*=T',
\qquad f=\frac1{Y-2X}.
\tag{20h}
$$
直线 $Y=2X$ 在 $P_*$ 相切且经过 $T'$，所以
$$
\operatorname{div}(f)=3O-2P_*-T'.
\tag{20i}
$$
特别地 $f$ 在 $O$ 从三阶起。

在 $T'$ 用 $Y$ 作局部参数。
由原曲线上 $(1,0)$ 的 $Y=2y+O(y^3)$ 及 (20e)，
$\overline Z_p$ 的首极项为 $-2\mathfrak h_pY^{-p}$。
由于 $d\overline Z_p=\omega_+$ 在此正则，
其全部负次幂只能是 $p$ 的倍数；极阶仅 $p$，
故这已经是完整极部。另一方面，$f$ 的极部为 $Y^{-1}$。
因此
$$
\boxed{\quad
 Z_p^\dagger=\overline Z_p+2\mathfrak h_p f^p
 \quad}
\tag{20j}
$$
在 $T'$ 的极部完全消掉，仅在 $P_*$ 留一个准确 $2p$ 阶极点。
它满足
$$
dZ_p^\dagger=\omega_+,\qquad
Z_p^\dagger-\overline Z_p=O(z^{3p}),\qquad
\deg(Z_p^\dagger)=2p.
\tag{20k}
$$
所以两个原权 $p+1,2p+2$ 的 jet 完全保留。

原 $x^2=-1$ 四挠点在商上的两个像是
$P_\pm=(\pm2i,0)$。它们原来满足 $\overline Z_p(P_\pm)=0$；
但 $f(P_\pm)=\pm i/4$，故
$$
Z_p^\dagger(P_\pm)
 =2\mathfrak h_p(\pm i/4)^p\ne0.
\tag{20l}
$$
这准确修复了选定参数把 $O$ 与这两个固定参考零点同时送到零的碰撞。
修复不声称保持全局 $\mu_4$ 齐次性；所需两权 jet 则由 (20k) 保留。

这个次数是非平凡修复的最小值。
事实上，设 $Z_{\rm new}$ 是任意满足
$dZ_{\rm new}=\omega_+$ 的有理函数，且
$$
Z_{\rm new}-\overline Z_p=O(z^{2p+3}).
$$
若二者不同，则 $\ker d=k(E_+)^p$ 给
$Z_{\rm new}-\overline Z_p=f_0^p$，
并有 $\operatorname{ord}_O f_0\ge3$，故 $\deg f_0\ge3$。
极点除子比较给
$$
p\,\deg f_0
 \le \deg Z_{\rm new}+\deg\overline Z_p
 =\deg Z_{\rm new}+p,
$$
从而 $\deg Z_{\rm new}\ge2p$，被 (20j) 达到。

$Z_p^\dagger$ 的零纤维仍有 $2p$ 个几何点；
这些零点都是简单的，因为其微分为处处非零的 $\omega_+$。
本构造没有从这个完整零纤维迹中隔离原 $O$ 分支，
也没有把参数修复当成 theta 线丛的全局有界平凡化。
第 6 节的模 $p^2$ 提升障碍也不因添加 $f^p$ 而消失。

## 6. 任何整有理原函数都不能提升到模 $p^2$

令 $\mathscr R_p$ 是特征零函数域中在竖直素因子 $(p)$ 处整的
有理函数环；它的剩余域是 $\mathbf F_p(\mathcal C)$。
允许再作有限未分歧系数扩张，结论不变。

**命题。** 不存在 $Z\in\mathscr R_p$ 满足
$$
dZ\equiv\omega\pmod{p^2}.
\tag{21}
$$

证明：若有，首先 $d\overline Z=\overline\omega=d\overline Z_p$。
在完美常数域上的单变量函数域中，
$\ker d=k(\mathcal C)^p$。故可写
$$
\overline Z-\overline Z_p=f^p.
$$
取 $f$ 的任一整有理提升 $\widetilde f$，有
$$
Z=Z_p+\widetilde f^{\,p}+pR,\qquad R\in\mathscr R_p.
\tag{22}
$$
由 (6)，式 (21) 将迫使
$$
\overline\alpha_p=f^{p-1}df+d\overline R.
\tag{23}
$$
右边经过两次 Cartier 为零，而左边由 (20) 等于
$-\overline\omega\ne0$，矛盾。

因此式 (20) 不仅排除选定 $Z_p+pR$ 的修正，
也排除改变任意首层有理原函数所允许的 $f^p$ 自由度。
这里所说的非零 Bockstein，就是 (6) 的真实除 $p$ 误差及其
不随 (22) 改变的二次 Cartier 值；没有额外假设抽象晶体格或
免费换基。

这是**全函数域上的微分同余**。它不禁止原局部有限 jet 的模
$p^2$ 计算，也不禁止有额外非有理参考项的比较。

## 7. 原 A2/B 两行的准确留数接口

沿用 [R197](R197-actual-two-weight-determinant-and-common-theta-gauge.md)
的原固定多项式 $P,Q$、$\theta$ 及
$$
\widehat K(w)=
 \sum_{\substack{1\le n\le2r-1\\n\ne r}}k_n w^n,
\qquad k_n\in\mathbf Z_p.
$$
为给一个确切全局有理代表，定义
$$
\mathcal E_p=
 \sum_{\ell=0}^{2r-1}\frac1{\ell!}
 \left(68
   \sum_{\substack{1\le n\le2r-1\\n\ne r}}
        \overline k_n\,\overline Z_p^{\,4n}
 \right)^\ell
 \in\mathbf F_p(\mathcal C).
\tag{24}
$$
所有阶乘均为单位。因为 $P(u^4),Q(u^4)$ 在 $O$ 都从 $u^4$
起，式 (8) 和指数截断说明，对 $j=1,2$，
$$
\boxed{\quad
\overline{\widehat R_j}=
 \left(
  \operatorname{Res}_O
   \frac{\mathcal E_pP(u^4)\,\overline\omega}
        {\overline Z_p^{\,j(p+1)+1}},
 \quad
  \operatorname{Res}_O
   \frac{\mathcal E_pQ(u^4)\,\overline\omega}
        {\overline Z_p^{\,j(p+1)+1}}
 \right).
\quad}
\tag{25}
$$
这里 $\widehat R_j=(\widehat A_{jr},\widehat B_{jr})$ 正是
R197 的两个 Taylor 行；没有改变 $A=A_2$ 或 $B$，
也没有丢去各自的曲线尺度。

式 (24) 只是在所需有限 jet 上准确的有理代表。
它不是原正次数 theta 线丛的全局平凡化，
也不把完整 theta 参考变成一个固定有理单位。
因此 (25) 与 R197 的
$$
\Delta_p/p^3\equiv
 -4\det(\widehat R_1,\widehat R_2)\pmod p
$$
可直接合用；但在双首行已被 $p$ 整除后，
真正要检测的
$\det(p^{-1}\widehat R_1,\widehat R_2)\pmod p$
仍需要更高一层实际输入。
式 (20) 精确说明，不能仅把 (25) 的模 $p$ 有理参数无成本地
提升成所需的全局模 $p^2$ 参数。

## 8. 依赖和范围

- 原整数微分系统、严格 $u,z$ 规范：
  [R57](R57-global-hurwitz-integers-and-fixed-polynomial-flow.md)。
- 原 $P,Q$、共同 theta 指数消除、$\kappa_p$ 和两权行列式规范：
  [R197](R197-actual-two-weight-determinant-and-common-theta-gauge.md)。
- 本文 (6)、(15)–(20)、(22)–(25) 都在上述实际对象上逐式证明；
  没有调用未经核实的跨 $p$ 非消失或 theta 有理性定理。

本结果保留了一个明确非零的固定椭圆参考提升障碍。
它没有把这个参考单位当成原双行行列式的单位，
也没有证明无穷多个 $p$ 的 Tate–Shafarevich 群有限。
