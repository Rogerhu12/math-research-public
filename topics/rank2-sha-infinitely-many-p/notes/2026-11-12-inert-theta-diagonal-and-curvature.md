# 惰性目标系数的固定级数归约，以及不能删去的 sigma 连接

日期：2026-11-12。状态：以下 Lagrange 系数公式、全级数非 D-finite
及自然连接的算子关系已证明。尚未把目标 prime diagonal 识别为
另一个固定曲线的 Hasse–Witt 非零量。

使用已证的次数 $17$ 下降截面
（[完整下降证明](2026-11-12-theta-seventeen-isogeny-descent.md)），写成

$$
 A(z)=\theta_T(z)^{17}Q(x(z)^{-2})
       =\sum_{m\ge0}b_mz^m,\qquad
 Q(X)=\sum_{j=1}^4c_jX^j\ne0,
                                                               \tag{1}
$$

其中 $E:y^2=x^3-17x$，
$\theta_T(z)^2=x(z)\sigma_E(z)^2$、$\theta_T(0)=1$，
且 $Q(0)=0$。本篇不需要四个系数的数值候选，也不把未认证的
候选多项式用作原截面。

以下排除固定系数 $c_j$ 的有限个分母素数；这对寻找无穷多个素数无影响。
固定惰性素数 $p\ge7$，写 $p=4r-1$。
需要研究的是 $b_{p+1}\pmod p$，而非首个已知非整的后续系数。

## 1. 固定二重覆盖上的两个真实原函数

在固定椭圆二重覆盖上取

$$
 u=x^{-1/2},\qquad s=-yu^3,\qquad
 s^2=1-Du^4,\qquad D=17.
$$

在 $O$ 上方选 $u=z+\cdots,s=1+\cdots$ 的分支。于是

$$
 \frac{du}{dz}=s,\qquad
 z=\int_0^u\frac{dt}{\sqrt{1-Dt^4}}=uF(v),\qquad v=Du^4,
                                                               \tag{2}
$$

其中固定有理级数为

$$
 F(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+1)}v^n,\qquad
 H(v)=\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(4n+3)}v^n.
                                                               \tag{3}
$$

令 $\Theta(v)=\theta_T(z(u))$。
由于 $\theta_T=\sigma_E/u$，

$$
 \frac d{dz}\log\theta_T=\zeta(z)-\frac{s}{u},\qquad
 \frac {d^2}{dz^2}\log\theta_T=Du^2 .
                                                               \tag{4}
$$

第一式中的常数由 $z=0$ 的展开固定为零。
积分第二式，并用 (2)，得

$$
 \frac d{dz}\log\theta_T
       =Du^3H(v),\qquad
 \boxed{\quad
 \frac{\Theta'(v)}{\Theta(v)}
       =\frac{H(v)}{4\sqrt{1-v}},\qquad\Theta(0)=1 .
 \quad}                                                       \tag{5}
$$

$F,H$ 是代数微分的原函数；$\Theta$ 还包含一次指数积分。
不能把 (5) 的右边换成一个任意的代数函数近似。

置

$$
 \widetilde Q(v)=Q(v/D),\qquad
 \Xi_Q(v)=\frac{(\Theta(v)^{17}\widetilde Q(v))'}{F(v)}.
                                                               \tag{6}
$$

这是一个与 $p$ 无关的固定特征零级数。

## 2. $b_{p+1}$ 的准确模 $p$ 公式

**命题。** 对上述惰性 $p$，

$$
 \boxed{\quad
 b_{p+1}\equiv
        4D^r[v^{r-1}]\Xi_Q(v)\pmod p,\qquad r=(p+1)/4 .
 \quad}                                                       \tag{7}
$$

两边在取模之前均为整。

**证明。** 先核对所有分母。
在次数至多 $r-1$ 内，$F$ 的分母 $4n+1$ 至多为 $p-2$，
没有 $p$ 因子。
$H$ 的第一个含 $p$ 分母的项恰在次数 $r-1$，
因为 $4(r-1)+3=p$。
由 (5)，$\Theta$ 的第一个可能含 $p$ 分母的项因此在次数 $r$；
其次数至多 $r-1$ 的系数均整。这里积分的分母以及指数展开的
阶乘都小于 $p$，没有遗漏额外 $p$ 因子。

由于 $\widetilde Q(0)=0$，$\Theta^{17}\widetilde Q$
的次数至多 $r$ 的系数仍整。因此其导数到次数 $r-1$，
以及 $\Xi_Q$ 到该次数，都整。
等价地，把 (6) 展开为

$$
 \Xi_Q=\frac{\Theta^{17}}F
     \left(\widetilde Q'
        +\frac{17\widetilde Q\,H}{4\sqrt{1-v}}\right),
                                                               \tag{8}
$$

可见含 $H$ 的项有 $\widetilde Q$ 的一次零点，
所以 $H$ 的那个首个 $p^{-1}$ 系数恰好不进入目标次数。

Lagrange 反演对 $N=p+1=4r$ 给

$$
 \begin{aligned}
 b_N
  &=\frac1N[u^{N-1}]
       \frac d{du}\bigl(\Theta(Du^4)^{17}
                              \widetilde Q(Du^4)\bigr)
                          F(Du^4)^{-N}\\
  &=\frac{4D^r}{p+1}[v^{r-1}]
       (\Theta^{17}\widetilde Q)'F(v)^{-p-1}.
 \end{aligned}                                                \tag{9}
$$

已核对的整性允许在这一有限截断内取模 $p$。
$F(0)=1$，所以
$F(v)^p\equiv F(v^p)\equiv1\pmod{(p,v^r)}$。
又 $(p+1)^{-1}\equiv1\pmod p$，(9) 即化为 (7)。$\square$

(7) 去掉了一个随 $p$ 变化的高次幂。
剩下的并非任意有限 jet，而是固定的真实级数 $\Xi_Q$；
它仍含完整的 $\Theta$ 连接。

## 3. 固定级数 $\Xi_Q$ 不是 D-finite

这里的 D-finite 指满足一个非零、有限阶、
系数属于 $\mathbb C(v)$ 的线性微分方程。
下面的结论尤其排除把**整条** $\Xi_Q$ 误记为某个固定代数
period 系列的线性微分方程解。
它不排除仅在 (7) 所选 prime diagonal 上另有特殊恒等式。

**命题。** 对任意非零且 $Q(0)=0$ 的多项式 $Q$，
$\Xi_Q$ 不是 D-finite，因而不是代数函数。

**证明。** 令 $\Gamma_u$ 是覆盖曲线上 $u(z),s(z)$ 的共同周期格，
并选非零实周期 $\ell\in\Gamma_u$；例如可取原曲线实周期的两倍。
沿一个返回相同 $(u,s)$ 的周期环，Abel 积分 $z$ 变为 $z+n\ell$。
因此 $\Xi_Q$ 的继续分支可写成

$$
 \Xi_{Q,n}(v(z))=
 \frac{
   \dfrac d{dv}
      \bigl(\theta_T(z+n\ell)^{17}\widetilde Q(v(z))\bigr)}
      {(z+n\ell)/u(z)},\qquad n\in\mathbb Z .
                                                               \tag{10}
$$

这保留了分母 $F=z/u$ 的继续，不能只继续 theta 因子。

设 $\widetilde Q(v)=q_jv^j+\cdots$，$q_j\ne0,j\ge1$。
取任意有限整数集 $I$，假定
$\sum_{n\in I}a_n\Xi_{Q,n}=0$。
把这条恒等式拉回 $z$ 平面。
各项由亚纯椭圆函数、整 theta 函数和线性分母组成，
故是全平面的亚纯函数。

固定 $n_0\in I$，在 $z=-n_0\ell$ 处写 $w=z+n_0\ell$。
有 $u(z)=u(w)=w+\cdots$，$v(z)=Dw^4+\cdots$。
对 $n=n_0$，(10) 的分母为 $w/u(w)=1+\cdots$，
其分子首项为 $j q_jv^{j-1}$；所以

$$
 \operatorname{ord}_{w=0}\Xi_{Q,n_0}=4j-4,
$$

且首项非零。
对 $n\ne n_0$，theta 的准周期给
$\theta_T(w+(n-n_0)\ell)=C_n e^{\eta_nw}\theta_T(w)$，
$C_n\ne0$。它仍在 $w=0$ 非零，分子仍从次数 $4j-4$ 开始；
但分母
$(w+(n-n_0)\ell)/u(w)$ 有一阶极点。因此

$$
 \operatorname{ord}_{w=0}\Xi_{Q,n}\ge4j-3
                       \qquad(n\ne n_0).
$$

比较唯一的最低次项，得 $a_{n_0}=0$。
对所有 $n_0\in I$ 重复，证明任意有限个这些继续分支线性无关。

有限阶线性微分方程在避开其有限个奇点后，
所有继续分支都属于同一个有限维复解空间。
周期路径可以避开那些奇点在 $z$ 平面的离散逆像；
上面的亚纯恒等式延拓及局部最低阶比较也不要求穿过
某个 ODE 奇点来定义继续。因此无限线性无关与 D-finite 矛盾。
$\square$

## 4. 惰性处真实连接的 $p$ 次算子

本节给出试图用一个固定有限矩阵替代 sigma 连接时的另一个
具体检查。它针对以下自然算子，不声称否定所有可能的
prime-diagonal Frobenius 表达。

使用[惰性 Cartier 计算](2026-11-12-central-diagonal-inert-shift.md)
中已经证明的算子恒等式：在特征 $p$ 的曲线函数域上，
$\delta^p=0$，并且

$$
 \kappa=\delta^{p-1}X
 =-\frac12(-1)^r\binom{2r}{r}D^r\ne0.
$$

引入真实 zeta 原函数的形式变量 $U$，
令 $\mathcal DU=-X$，在曲线函数上 $\mathcal D=\delta$。
则

$$
 \mathcal D^p=-\kappa\partial_U,\qquad
 B=U^p-\delta^{p-2}X,\qquad
 \mathcal DB=-\kappa.
                                                               \tag{11}
$$

在 (1) 的另一写法
$A=\sigma_E^{17}\sqrt X\,R(X^2)$ 中，
$R(X^2)=c_1X^6+c_2X^4+c_3X^2+c_4$。
在避开该固定有理函数零极点的开集、并加入 $\sqrt X$ 的
固定可分覆盖后，真实连接算子是

$$
 \mathcal L_A=\mathcal D+17U+
                  \delta\log\bigl(\sqrt X\,R(X^2)\bigr).
                                                               \tag{12}
$$

有理 gauge 不依赖 $U$。
由 Bell/Jacobson 公式，
$(\mathcal D+17U)^p=\mathcal D^p+17B$。
再对 (12) 作该有理 gauge 的共轭，得到

$$
 \boxed{\quad
 \mathcal L_A^p=-\kappa\partial_U+17B,\qquad
 [\partial_U,\mathcal L_A]=17 .
 \quad}                                                       \tag{13}
$$

共轭没有额外项，因为 $\delta^p$ 在曲线函数域及其可分代数扩张上
仍为零，且 $\partial_U$ 杀掉 gauge。
也可检查
$[-\kappa\partial_U+17B,\mathcal L_A]=0$：
两个常数交换子恰好相消，与 $p$ 次幂必须交换一致。

### 两个准确的限制

首先，不存在某个可分代数覆盖上的代数函数 $U_0$ 满足
$\delta U_0=-X$。否则 $\delta^p$ 在该覆盖上仍为零，
却应有 $\delta^pU_0=-\kappa\ne0$。
因此不能把 (12) 中的 zeta 项直接替成固定代数函数而保持连接。

其次，若试图把 $\partial_U,\mathcal L_A$ 同时变成一个有限维
常数域向量空间上的线性自同态并保留 (13)，取迹给

$$
                  0=17\,\dim W\quad\text{于特征 }p .
$$

所以 $p\mid\dim W$。当 $p$ 变化时，
这对算子的忠实常数矩阵模型不可能有一个固定的正维数。
这里没有对半线性 Frobenius 或任意不同的 cohomology 对象
作未经证明的推论。

## 5. 当前真正剩下的非零问题

公式 (7) 把目标准确归约为

$$
 [v^{(p-3)/4}]\Xi_Q(v)\ne0\pmod p
                  \quad\text{在无穷多个惰性 }p\text{ 上}.
$$

第 3、4 节说明两条直接捷径为何缺少必要输入：
整条级数不是固定有限阶 Picard–Fuchs 解，
自然 sigma 连接也不能被删成一个固定代数函数。
它们没有证明上述选定 prime diagonal 不可能另有
Cartier、Hasse–Witt 或 Frobenius 描述。
如果找到这样的描述，仍须独立证明它与 (7) 的实际系数相等，
然后才可调用该固定对象的非零定理。
