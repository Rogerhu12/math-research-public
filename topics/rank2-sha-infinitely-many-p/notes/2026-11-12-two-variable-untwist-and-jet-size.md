# 双变量的中心一共同逆像、准确 jet 大小及高维代数化检验

**可信度：本文命题均已证明；没有推出初级有限的无穷性。**
日期：2026-11-12。

接续 [CM sigma 除法笔记](2026-11-12-cm-sigma-division-and-common-resonance.md)。
这里确实构造一个中心为 $1$、两个差分右端均有理的正规双变量共同逆像，
然后计算这个形式曲面本身的算术大小。增加变量没有消除共同共振：
正确的单项特征含两个指数，惰性处恒有权 $(p,1)$。
这也给出对高维 Bost 定理的直接检验，而不是先限制回一条曲线。

固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
\omega=\frac{dx}{2y},\quad t=-x/y,\quad
z=\log_E(t),\quad D=d/\omega.
$$
令 $\sigma(z)=\Sigma(t(z))$ 为前述固定 sigma，$\zeta=\sigma'/\sigma$。

## 1. 一个正规但超越的加法原函数

写
$$
w_n=(-1)^n\binom{2n}{n}17^n,\qquad
V(t)=\zeta(z(t))-\frac1t
=-\frac12\sum_{n\ge1}\frac{w_n}{4n-1}t^{4n-1}.
\tag{1.1}
$$
于是 $V\in t^3\mathbb Q[[t]]$，首项为 $17t^3/3$。
因为 $1/t=-y/x$，
$$
V=\zeta+y/x,\qquad
D(y/x)=x+17/x,\qquad
\boxed{DV=17/x.}
\tag{1.2}
$$
右端在 $O$ 正规，且首项为 $17t^2$。

这个原函数还有准确的复解释。取半周期 $\tau$ 对应
$T=(0,0)$。Weierstrass 加法公式给
$$
\boxed{V(t(z))=\zeta(z+\tau)-\zeta(\tau).}
\tag{1.3}
$$
所以 $V$ 只有 $-\tau+\mathcal L$ 处的简单极点，而
$$
V(t(z+\lambda))=V(t(z))+\eta(\lambda)
\quad(\lambda\in\mathcal L).
\tag{1.4}
$$
至少一个 $\eta(\lambda)$ 非零：否则 $\zeta$ 会下降为椭圆曲线上的
亚纯函数，只有一个留数为 $1$ 的极点，违反留数和为零。

**命题 1。** $V$ 超越于 $\mathbb C(E)$。

**证明。** 若 $V$ 满足系数属于 $\mathbb C(E)$ 的非零多项式，
固定满足 $\eta(\lambda)\ne0$ 的周期，在一个避开极点、首项不消失的
一般 $z$ 处，所有
$V(t(z))+n\eta(\lambda)$ 都是同一个有限次多项式的根。
这些值两两不同，矛盾。证毕。

## 2. 两个有理右端和真正的中心一共同逆像

设 $\beta\in\mathbb Z[i]$ 非零，$d=N\beta$。
由已证 sigma 除法关系，
$$
Z_\beta(P):=\zeta(\beta z)-\bar\beta\zeta(z)
=\frac1\beta D\log R_\beta\in K(E),
\quad
R_\beta=\frac{\sigma(\beta z)}{\sigma(z)^d}.
\tag{2.1}
$$
若 $R_\beta$ 仅在二重覆盖上有理，则右边读为
$(2\beta)^{-1}D\log R_\beta^2$；本节的两个乘子均为奇范数，
直接使用已有的多项式 $\Psi_{2+i}$、$\Psi_{3+2i}$ 即可。

置
$$
B_\beta(P)=Z_\beta(P)
-\frac1{t([\beta]P)}+\frac{\bar\beta}{t(P)}\in K(E).
\tag{2.2}
$$
准确的形式恒等式是
$$
\boxed{V([\beta]t)-\bar\beta V(t)=B_\beta(P).}
\tag{2.3}
$$
因此 (2.2) 在 $O$ 的表面极点全部可去，且 $B_\beta\in t^3K[[t]]$。
两个乘子满足
$$
B_\alpha([\beta]P)-\bar\beta B_\alpha(P)
=B_\beta([\alpha]P)-\bar\alpha B_\beta(P).
\tag{2.4}
$$
这是逐项相消所得的准确等式，没有未定常数。

现在在 $E\times\mathbb G_a$ 上定义代数自映射
$$
\varphi_\beta(P,u)=([\beta]P,u/\bar\beta),
\qquad
\mathcal F(t,u)=uV(t)\in(t,u)^4\mathbb Q[[t,u]].
\tag{2.5}
$$
则
$$
\boxed{
(\varphi_\beta^*-1)\mathcal F
=\frac{u}{\bar\beta}B_\beta(P)\in K(E)(u).
}
\tag{2.6}
$$
右端在 $(O,0)$ 正规。特别地，取
$\beta_1=2+i,\ \beta_2=3+2i$，
两条中心为 $1$ 的有理差分方程有同一个正规解；
由 (2.4) 可直接核对兼容性。

该解也确实唯一，条件是常数项为零。
在线性坐标 $(z,u)$ 中，单项 $z^ku^\ell$ 的特征为
$$
\boxed{\beta^k\bar\beta^{-\ell}.}
\tag{2.7}
$$
若对 $\beta=2+i$ 这个特征为 $1$，取复绝对值得 $k=\ell$；
随后 $(\beta/\bar\beta)^k=1$。
由于 $(2+i)$ 与 $(2-i)$ 是不同的高斯素理想，
$\beta/\bar\beta$ 不是根单位，故 $k=\ell=0$。
所以 $\varphi_{\beta_1}^*-1$ 在零常数的形式级数空间上已经无核。

图像 $Y=\mathcal F(t,u)$ 还在以下有理映射下不变：
$$
\widetilde\varphi_\beta(P,u,Y)
=\left([\beta]P,\frac{u}{\bar\beta},
Y+\frac{u}{\bar\beta}B_\beta(P)\right).
\tag{2.8}
$$
这些映射在其共同定义域上交换；(2.4) 正好给出最后坐标的相容性。

## 3. 不能把这个构造限制到非平凡的稳定曲线

**命题 2。** 对任意 $N\beta>1$，
通过 $(O,0)$、被 $\varphi_\beta$ 稳定的形式曲线的每条分支
只能是两条坐标轴之一。因此 $\mathcal F$ 在它们上均为零。

**证明。** 若一条不可约分支既不在 $z=0$ 也不在 $u=0$，
在其正规化上取参数 $s$，写
$$
z=a s^m+\cdots,\qquad u=b s^n+\cdots,\quad
ab\ne0,\ m,n>0.
$$
诱导的参数自同构首项为 $cs$，于是
$c^m=\beta$、$c^n=\bar\beta^{-1}$。
消去 $c$ 后，
$$
\beta^n=\bar\beta^{-m},
$$
但复绝对值给 $|\beta|^n=|\beta|^{-m}$，矛盾。
若若干分支被置换，对一个正次幂使用同一论证。证毕。

所以这里没有遗漏一条既正规、稳定、又保留非零原函数的一维通道。
这与 [R41](../results/R41-two-multiplier-common-depth-summability.md)
所处理的一维未扭曲算子不能混同。

## 4. 两变量的真实共同剩余核

设 $p\equiv3\pmod4$ 为好素数，并排除两个乘子的范数素因子。
在 $\mathbb F_{p^2}$ 中
$\bar\beta=\beta^p$，故 (2.7) 的剩余特征为
$$
\beta^{\,k-p\ell}.
\tag{4.1}
$$
若
$d_p=|\langle\beta_1,\beta_2\rangle\subset\mathbb F_{p^2}^{\times}|$，
则同时的剩余特征为 $1$ 当且仅当
$$
d_p\mid k-p\ell.
\tag{4.2}
$$
尤其 $(k,\ell)=(p,1)$ 对**每个**这样的 $p$ 都是共同共振，
无论 $d_p$ 有多大。

实际级数 $\mathcal F$ 对 $u$ 为一次，所以它所见的分母是
$\beta^k/\bar\beta-1$，并非 R41 中的 $\beta^k-1$。
增加一个变量使方程表面的中心变成 $1$，没有把两个指数的剩余核
改成 R41 的单指数核。下面的准确系数证明这不是仅形式上的区别。

## 5. 任意维图像的 size 公式

这里使用 $|p|_p=p^{-1}$。先证明一个直接适用于形式曲面的引理。

**引理。** 设 $f(X_1,\ldots,X_m)=\sum_I a_I X^I$ 有正收敛半径，
$f(0)=0$、$Df(0)=0$。在整仿射模型中，其形式图像的 Bost size 为
$$
\boxed{
S(\operatorname{graph}f)
=\min\left(1,\inf_{\substack{|I|\ge2\\a_I\ne0}}
|a_I|^{-1/(|I|-1)}\right).
}
\tag{5.1}
$$

**证明。** Bost–Chambert-Loir Theorem 3.1(c) 的定义适用于任意维数：
size 是可由 $G_{\rm an,r}$ 中的解析坐标自同构拉直图像的最大 $r\le1$，
其中每个坐标的 $r$-Gauss 范数至多 $r$，切映射属于整一般线性群。

若 $\|f\|_r\le r$，三角自同构
$(X,Y)\mapsto(X,Y+f(X))$ 及其逆都满足此条件，故得到一个方向。
反之，设 $g\in G_{\rm an,r}$ 把标准 $m$ 维平面送到图像。
因图像的切平面是 $Y=0$，$Dg(0)$ 分块上三角；
其切向块和法向块均为整可逆矩阵。
因此 $g(X,0)$ 的前 $m$ 个坐标组成
$g_0\in G_{\rm an,r}$，其逆也属于该群。
将最后坐标与 $g_0^{-1}$ 复合即得 $f$，
故 $\|f\|_r\le r$。
这个不等式恰等价于对全部 $I$ 有
$|a_I|r^{|I|-1}\le1$，得 (5.1)。证毕。

在 $E$ 的整 Weierstrass 模型的 $O$ 邻域，
$t$ 是整 étale 参数；由同一 Theorem 3.1(b)，该引理计算的正是
$E\times\mathbb A^2$ 中图像的 size。
仅用好素数也已足够以下 adelic 结论。

## 6. 原点处的准确双变量 jet 大小

记
$$
a_n=-\frac{w_n}{2(4n-1)},\qquad
\mathcal F(t,u)=\sum_{n\ge1}a_n t^{4n-1}u.
\tag{6.1}
$$
系数分母的赋值至多随 $\log n$ 增长，所以每个有限素数处都有正收敛半径。

**命题 3。** 对每个惰性素数 $p\equiv3\pmod4$，
$$
\boxed{S_{p,(O,0,0)}(\operatorname{graph}\mathcal F)=p^{-1/p}.}
\tag{6.2}
$$
对 $p=2$ 或 $p\equiv1\pmod4$，上述整参数中的图像 size 为 $1$。

**证明。** 令 $m=4n-1$。在惰性处，
$v_p(a_n)\ge-v_p(m)$。
若 $v_p(m)=a\ge1$，则
$$
\frac{-v_p(a_n)}{m}\le\frac{a}{m}
\le\frac{a}{p^a}\le\frac1p.
\tag{6.3}
$$
取 $n=r=(p+1)/4$，则 $m=p$；
因 $2r=(p+1)/2<p$ 且 $p\nmid17$，$w_r$ 是 $p$ 单位。
所以 $v_p(a_r)=-1$，(6.3) 达到等号。
单项 $t^m u$ 的总次数为 $m+1$，在 (5.1) 的分母正是 $m$；
故得到 (6.2)。

若 $p\equiv1\pmod4$ 且 $p^a\mid4n-1$，
对每个 $1\le j\le a$ 有
$$
n\bmod p^j=\frac{3p^j+1}{4}>\frac{p^j}{2}.
$$
所以
$\lfloor2n/p^j\rfloor-2\lfloor n/p^j\rfloor=1$；
阶乘赋值公式给
$v_p\binom{2n}{n}\ge a$，恰消去所有可能的分母。
在 $p=2$，$\binom{2n}{n}$ 为偶数而 $4n-1$ 为奇数，
同样得到 $a_n\in\mathbb Z_2$。证毕。

定义总次数不超过 $k$ 的局部最大斜率
$$
b_{p,0}(k)=
\max\left(0,\max_{4n\le k}
\frac{-v_p(a_n)}{4n-1}\right).
\tag{6.4}
$$
上述证明还给出准确的截断结论：
$b_{p,0}(k)=1/p$ 当 $p\equiv3\pmod4$ 且 $p+1\le k$；
否则为零。因此
$$
\boxed{
\mathcal B_0(k):=\sum_p b_{p,0}(k)\log p
=\sum_{\substack{p\equiv3\ (4)\\p\le k-1}}\frac{\log p}{p}
=\frac12\log k+O(1).
}
\tag{6.5}
$$
最后一步是固定算术级数的 Mertens 渐近；
若只计好模型素数，删去的有限项只改变 $O(1)$。

## 7. 非零 u 处的曲面结构及另一准确大小

在 $u\ne0$ 上，代数坐标变换 $W=Y/u$ 将图像变为
$$
W=V(t),\qquad u\ \text{自由}.
\tag{7.1}
$$
因此该曲面是超越曲线的乘积；由命题 1，其 Zariski 闭包维数为 $3$，
而形式曲面的维数为 $2$。特别地，它不是代数曲面的分支。
这直接证明增加变量没有使当前对象代数化。

在 $(O,1,0)$ 处写 $v=u-1$，图像为
$$
Y=(1+v)V(t).
$$
纯单项 $a_n t^{4n-1}$ 的 size 斜率大于相应的混合单项。
若 $m=4n-1$、$a=v_p(m)$，则
$$
\frac{-v_p(a_n)}{m-1}\le
\frac{a}{p^a-1}\le\frac1{p-1};
$$
在 $m=p$ 达到等号。因此
$$
\boxed{S_{p,(O,1,0)}=p^{-1/(p-1)}
\quad(p\equiv3\pmod4),}
\tag{7.2}
$$
其余素数的整参数 size 为 $1$。
相应的总次数 $k$ jet 预算是
$$
\boxed{
\mathcal B_1(k)=
\sum_{\substack{p\equiv3\ (4)\\p\le k}}\frac{\log p}{p-1}
=\frac12\log k+O(1).
}
\tag{7.3}
$$
这两个基点的准确公式不同，但对数发散的主项一致。

## 8. 直接核对高维 Bost 定理的三个输入

Bost，*Algebraic leaves of algebraic foliations over number fields*，
Theorem 3.4 适用于**任意维数**的光滑形式 germ。
它要求：每个有限处有正 size 且
$\sum_{\mathfrak p}\log S_{\mathfrak p}^{-1}<\infty$；
各复嵌入处解析；至少一个复嵌入存在 Liouville 复流形的局部一致化。
没有把最后一项换成不受条件限制的“维数奖励”。

本曲面各有限处正收敛及复解析均已成立。
复一致化可取
$$
M=(\mathbb C\setminus(-\tau+\mathcal L))\times\mathbb C,
\qquad
(z,u)\longmapsto(P(z),u,uV(t(z))).
\tag{8.1}
$$
它在两个所讨论基点附近都是局部嵌入。
$M$ 是 $\mathbb C^2$ 删去一个闭解析集合，具有 Liouville 性质：
有界上半连续多重次调和函数可跨该集合延拓，再用 $\mathbb C^2$ 的
Liouville 性质。
然而由 (6.2) 或 (7.2)，
$$
\sum_p\log S_p^{-1}=\infty.
\tag{8.2}
$$
故该高维定理的算术输入明确失败。
本曲面和系数都在 $\mathbb Q$ 上定义，可直接在 $\mathbb Q$ 上作此检验；
扩域至 $K$ 并使用标准局部度数权重不会改变收敛与否。

以上没有借用只对形式曲线陈述的 Herblot 数值门槛。
任何更宽的高维算术代数化准则若要用于这个对象，必须与
(6.5)、(7.3) 及已证的非代数性相容；
单有两个可交换有理差分关系，不提供所缺的 size 收敛。

## 9. 同一失败也表现为每个惰性处的非零 p-曲率

在 $u\ne0$、坐标 $(P,u,W)$ 中，图像是如下正规秩二叶层的叶：
$$
X=D+h(P)\partial_W,\qquad \partial_u,\qquad h(P)=17/x(P).
\tag{9.1}
$$
两个向量场交换，且在 $(O,1,0)$ 线性无关。
相反，在原坐标的 $u=0$ 处，形式上自然的第二个生成元
$u\partial_u+Y\partial_Y$ 消失，不能在那里直接援用正规叶层定理。

现在设 $p\equiv3\pmod4$。在特征 $p$ 的椭圆曲线上，
$D^p$ 是平移不变导子，故 $D^p=A D$。
由 $[i]^*\omega=i\omega$，
$D^p[i]^*=i^p[i]^*D^p$，而 $i^p=-i$。
与 $D^p=A D$ 比较得 $A=0$，即
$$
D^p=0.
\tag{9.2}
$$
由于 $X^p$ 在基底函数上为 $D^p$，在 $W$ 上为 $D^{p-1}h$，
而 $p$ 次幂仍是导子，所以
$$
X^p=(D^{p-1}h)\partial_W.
\tag{9.3}
$$

令 $r=(p+1)/4$。形式对数
$z(t)=\sum_{n\ge0}w_n t^{4n+1}/(4n+1)$
在次数不超过 $p$ 的部分是 $p$ 整的，其逆亦然：
这里不可能出现 $4n+1=p$。
因此若 $q_p=[z^p]V(t(z))$，(1.1) 给
$$
p q_p\equiv-w_r/2\pmod p.
$$
利用 $DV=h$ 和 Wilson 公式，
$$
\boxed{
D^{p-1}h(O)=p!q_p\equiv w_r/2\ne0\pmod p.
}
\tag{9.4}
$$
所以 $X^p$ 在该点有非零竖直分量，不能属于
$\langle X,\partial_u\rangle$。
叶层在**每个惰性好素数**处都不被 $p$ 次幂稳定。
Bost Theorem 2.1 的几乎处处 $p$-闭合条件因此也明确不成立；
这不是尚未计算的异常集合。

## 10. 已获得的精确结论

当前构造提供了正规的、兼容的双变量中心一共同逆像，
并证明不存在保留它的非零稳定一维切片。
同时，真实双变量剩余核和 jet 计算显示：
惰性共同共振位于 $(p,1)$，仍给 $\tfrac12\log k+O(1)$ 的损失。
从 $Y=uV$ 这一曲面出发，经典任意维 Bost 定理和叶层版本均不适用。
这是对一个具体高维候选的完整检验；并未排除不同算术对象或更强新输入。

## 来源

- 前置系数及规范：[固定 sigma 笔记](2026-11-12-fixed-sigma-height-and-inert-denominator.md)，
  [非实 CM 除法笔记](2026-11-12-cm-sigma-division-and-common-resonance.md)。
- NIST DLMF，§23.2、§23.10，特别是 23.10.2 的 zeta 加法公式，
  [原文](https://dlmf.nist.gov/23.10)。
- J.-B. Bost、A. Chambert-Loir，
  *Analytic curves in algebraic varieties over number fields*，
  Theorem 3.1 及其之前的 $G_{\rm an,r}$ 定义、Proposition 3.4，
  [作者全文](https://arxiv.org/pdf/math/0702593)。
  本文 (5.1) 的任意维图像公式从这些定义直接证明，
  没有把该文一维 Proposition 3.5 改称为已发表的高维命题。
- J.-B. Bost，*Algebraic leaves of algebraic foliations over number fields*，
  Publ. Math. IHÉS **93** (2001)，161–221，
  Theorem 2.1、Theorem 3.4、§2.1.2、§3.4，
  [已出版全文](https://www.numdam.org/article/PMIHES_2001__93__161_0.pdf)。
- 固定算术级数的同一 jet 求和方法亦见
  [R38](../results/R38-exact-inert-sigma-size-and-jet-budget.md)；
  两个未扭曲乘子的可求和定理是
  [R41](../results/R41-two-multiplier-common-depth-summability.md)，
  它的单指数假设与本文 (4.2) 不同。
