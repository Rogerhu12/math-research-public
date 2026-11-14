# 中央对角的 Borel 变换：固定权一模形式、自然边界与准确复增长

日期：2026-11-12。状态：本文的模形式实现、自然边界与增长结论均已证明；没有证明任何新的跨素数 Sha 有限性。

## 1. 固定对象与结论

沿用 [中央整函数笔记](2026-11-12-central-diagonal-entire-series.md) 的规范：
$E:y^2=x^3-17x$，$\Gamma=\Omega_E\mathbb Z[i]$，$\Omega_E>0$，
$f=34(1+i)$，$Nf=2312$，以及

$$
 A=\frac{\Omega_E^2}{\pi_{\mathbb C}},\qquad
 e_m=\frac{d_m}{f^{2m+1}}\in\mathbb Q,\qquad
 \mathscr D(Z)=\sum_{m\ge0}e_mZ^m.
$$

$\mathcal S$ 是原始固定 $256$ 点导子轨道。因为 $f\mid68$，
可给每个 $S\in\mathcal S$ 固定一对
$(r_S,s_S)\in(68^{-1}\mathbb Z)^2/\mathbb Z^2$，使在原方格上

$$
 z_S=r_S\Omega_E+s_Si\Omega_E.
$$

所有这些挠点非零。本文所有权 $m\ge0$ 使用同一组坐标，
没有把 Yang 平方范数公式只覆盖的 $4\mid m$ 分支扩展到其余权。

定义一次 Borel 变换

$$
 \mathscr B(T)=\sum_{m\ge0}m!e_mT^m,\qquad
 \tau_0=\frac{\pi_{\mathbb C}}{Nf\,\Omega_E^2}=\frac1{Nf A}.
                                                               \tag{1}
$$

结论是：

1. 存在固定非零的、在所有 cusp 处全纯的权一模形式
   $\mathcal G$，所属群可取 $\Gamma(68)$，使

   $$
   \boxed{\quad
   \mathscr B(T)=
   \frac{1}{f\Omega_E(1-u)}
   \mathcal G\!\left(i\frac{1+u}{1-u}\right),
   \qquad
   u=\frac{T}{Af^2}=-i\tau_0T.
   \quad}                                                     \tag{2}
   $$

2. $\mathcal G(i)=0$，而 $\mathcal G'(i)\ne0$。
3. $\mathscr B$ 的收敛半径准确为 $\tau_0^{-1}$。
   整条圆周 $|T|=\tau_0^{-1}$ 都是自然边界；这里甚至不存在穿过任一圆周点的亚纯延拓。
4. 原来的 $\mathscr D$ 是增长阶恰为 $1$、指数型恰为 $\tau_0$ 的整函数。

因此除去一个阶乘给出一个真实的模形式参数化，
但没有保留原整函数的全平面参数域。
特别是不能沿用 $\mathbb A^1(\mathbb C)$ 上的 Herblot 增长输入，
同时只更改有限处的阶乘预算。

## 2. 固定挠点坐标给出全纯权一模形式

让 $\boldsymbol\omega=(\omega_1,\omega_2)$ 在
$\operatorname{Im}(\omega_2/\omega_1)>0$ 的周期空间变化。
记 $\Lambda_{\boldsymbol\omega}=\mathbb Z\omega_1+\mathbb Z\omega_2$，
$\zeta_{\boldsymbol\omega}$ 为 Weierstrass zeta 函数，
$\eta_j=\zeta(z+\omega_j)-\zeta(z)$ 为其准周期。
令

$$
 g(\boldsymbol\omega)=
 \sum_{S\in\mathcal S}
 \bigl[
  \zeta_{\boldsymbol\omega}(r_S\omega_1+s_S\omega_2)
  -r_S\eta_1-s_S\eta_2
 \bigr].
                                                               \tag{3}
$$

改变 $(r_S,s_S)$ 的整数代表不改变每个括号。
非零挠点在上半平面的任何周期格中都不是零点，
所以 (3) 对两个周期是全纯函数。
同一括号也等于

$$
 e^*_{0,1}(z_S,0;\Lambda_{\boldsymbol\omega})
 =
 \zeta_{\boldsymbol\omega}(z_S)-s_2(\Lambda_{\boldsymbol\omega})z_S
           -\frac{\bar z_S}{A(\boldsymbol\omega)},              \tag{4}
$$

因为
$\eta_j=s_2\omega_j+\bar\omega_j/A(\boldsymbol\omega)$，
其中

$$
 A(\boldsymbol\omega)
 =\frac{\omega_2\bar\omega_1-\omega_1\bar\omega_2}{2\pi_{\mathbb C}i}.
$$

(4) 的两项非全纯修正，在固定有理挠点坐标下恰好合并为
$r_S\eta_1+s_S\eta_2$。这一步不能对任意独立变化的 $z_S$ 忽略。

具体公式 (4) 可由 Bannai–Kobayashi (2010),
Example 1.9 及 Theorem 1.17 直接取得：
对平移 Kronecker theta 取常数项，
得到 $\theta'(z_S)/\theta(z_S)-\bar z_S/A$，
而 $\theta=e^{-s_2z^2/2}\sigma$。

(3) 在整体缩放下为一次逆齐次：

$$
 g(a\omega_1,a\omega_2)=a^{-1}g(\omega_1,\omega_2).
                                                               \tag{5}
$$

在 $\Gamma(68)$ 的换基下，固定挠点标签只相差整数周期，
故 $g$ 不变。因此

$$
 \mathcal G(\tau)=g(1,\tau)
                                                               \tag{6}
$$

满足权一变换律
$\mathcal G(\gamma\tau)=(c\tau+d)\mathcal G(\tau)$，
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\Gamma(68)$。

### 2.1 每个 cusp 的全纯性

这也可以逐项检验，避免只由周期换基断言 cusp 条件。
将一个非零标签取成 $0\le s<1$；若 $s=0$，则 $r\notin\mathbb Z$。
在格 $\mathbb Z+\mathbb Z\tau$ 上有

$$
 \zeta(r+s\tau)-r\eta_1-s\eta_2
 =
 \frac{\theta_1'(r+s\tau;\tau)}{\theta_1(r+s\tau;\tau)}
       +2\pi_{\mathbb C} i s.                               \tag{7}
$$

这里导数是对实际复坐标求导，$\theta_1$ 的第一周期取 $1$。
其乘积展开的对数导数为

$$
 \pi_{\mathbb C}\cot(\pi_{\mathbb C}z)
 +4\pi_{\mathbb C}\sum_{n\ge1}
       \frac{q^n}{1-q^n}\sin(2\pi_{\mathbb C}nz),
 \qquad q=e^{2\pi_{\mathbb C}i\tau}.                         \tag{8}
$$

代入 $z=r+s\tau$：
若 $s=0$，所有项有有界的 $q^{1/68}$ 展开；
若 $0<s<1$，正弦中的两部分有指数 $n(1+s)$ 与 $n(1-s)$，
而 cotangent 有常数项 $-i$ 及正的 $q^{s}$ 幂。
因此 (7) 在无穷 cusp 全纯。

对任一 $\gamma\in\mathrm{SL}_2(\mathbb Z)$，
$\mathcal G|_1\gamma$ 仍是有限个同样的非零挠点标签的 (7) 之和；
标签的分母仍除 $68$。同一证明给出所有 cusp 的全纯性。

## 3. 周期方向的微分精确恢复两个阶乘

在周期空间上使用 Wirtinger 导数，定义

$$
 W=-A(\boldsymbol\omega)^{-1}
     \left(\bar\omega_1\frac{\partial}{\partial\omega_1}
          +\bar\omega_2\frac{\partial}{\partial\omega_2}\right).
                                                               \tag{9}
$$

直接计算给出

$$
 W A=0,\qquad W\bar\omega_j=0.
                                                               \tag{10}
$$

对固定标签及 $\gamma=a\omega_1+b\omega_2$，置
$\beta=z_S+\gamma$。则
$W\beta=-\bar\beta/A$，$W\bar\beta=0$。
在 $\operatorname{Re}\varepsilon>1/2$ 的绝对收敛区间，

$$
 W^m\sum_{\gamma\in\Lambda}
          \frac1{\beta|\beta|^{2\varepsilon}}
 =
 \frac{(1+\varepsilon)(2+\varepsilon)\cdots(m+\varepsilon)}{A^m}
 \sum_{\gamma\in\Lambda}
       \frac{\bar\beta^m}
            {\beta^{m+1}|\beta|^{2\varepsilon}}.
                                                               \tag{11}
$$

在周期空间的紧邻域内，这些级数及所用导数一致收敛。
两边经 Eisenstein–Kronecker 的 Hecke 解析延拓，仍有 (11)。
这里涉及 $K^*_{2m+1}$；其第一指标为正，
所以 $\varepsilon=0$ 无极点，没有“零乘极点”的补项。
该延拓及参数微分可由 BK Proposition 1.3 的 theta 积分表示逐项取得。

在 $\varepsilon=0$ 代入 (11)，再对 $\mathcal S$ 求和：

$$
 W^m g=\frac{m!}{A^m}
       \sum_{S\in\mathcal S}e^*_{m,m+1}(z_S,0;\Lambda).
                                                               \tag{12}
$$

回到原方格，原 theta 对角的准确定义是

$$
 d_m=\frac1{m!A^m}
       \sum_{S\in\mathcal S}e^*_{m,m+1}(z_S,0;\Gamma).
$$

故得到全权公式

$$
 \boxed{\quad
       \left.W^m g\right|_{(\Omega_E,i\Omega_E)}
                  =(m!)^2d_m.
       \quad}                                                 \tag{13}
$$

这不是把 Maass–Shimura 导数的规范凭比例比较：
(11) 的升阶因子与 theta 对角自身的 $m!$，
分别给出 (13) 的两个阶乘。

## 4. 线性周期变形与准确 Borel 恒等式

在下面的全纯变形中，右边的共轭周期固定为原方格的常数：

$$
 \boldsymbol\omega(u)
  =\boldsymbol\omega-u\,\overline{\boldsymbol\omega},
 \qquad
 \boldsymbol\omega=(\Omega_E,i\Omega_E).
                                                               \tag{14}
$$

由于 $g$ 全纯，且 (10) 使迭代微分中不产生 $A$ 的导数，
其 Taylor 展开由 (13) 给出

$$
 g(\boldsymbol\omega(u))
   =\sum_{m\ge0} A^m m!d_m\,u^m.
                                                               \tag{15}
$$

这是在原点的全纯 Taylor 级数。
(14) 不能理解成变形以后再用新的共轭周期定义同一固定向量场。

现在

$$
 \omega_1(u)=\Omega_E(1-u),\qquad
 \omega_2(u)=i\Omega_E(1+u),
$$

所以 $\operatorname{Im}(\omega_2(u)/\omega_1(u))>0$
准确等价于 $|u|<1$。
用 (5) 改写 (15)，再令 $u=T/(Af^2)$ 并除以 $f$，
得到 (2)。因此 (2) 在 $|T|<Nf A$ 整个圆盘成立。

已证明的精确最低系数是

$$
 d_0=0,\qquad
 d_1=64(-1+i),\qquad e_1=\frac4{17^3}\ne0;
$$

见 [最低迹全局证明](2026-11-12-central-theta-d1-exact-global-trace.md)。
由 (2) 在零点的取值和一阶导数，
$\mathcal G(i)=0$ 且 $\mathcal G'(i)\ne0$。
特别是所构造的模形式非零，不需再假设中央 $L$ 值的一般非消失定理。

## 5. 权一模形式的 cusp 尾与自然边界

以下论证特意允许某个 cusp 的常数项非零。

**引理。** 若 $H$ 是某个有限指标同余子群上的非零权一全纯模形式，
则作为上半平面上的函数，它不能穿过任一有理实点作亚纯延拓。

**证明。**
取有理点 $r=a/c$，$c\ne0$，以及
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\mathrm{SL}_2(\mathbb Z)$。
$h=H|_1\gamma$ 在无穷 cusp 有收敛 Fourier 展开，
所以沿 $\tau=iy\to i\infty$ 有

$$
 h(iy)=a_0+O(e^{-\epsilon y})                                \tag{16}
$$

（若非恒 Fourier 项全部为零，余项就是零）。

若 $H$ 在 $r$ 亚纯，写
$H(r+v)=\sum_{j=-J}^{\infty}b_jv^j$。
由 $\gamma\tau-r=-1/[c(c\tau+d)]$，

$$
 h(\tau)
   =\sum_{j=-J}^{\infty}
      b_j(-1/c)^j(c\tau+d)^{-j-1}.                          \tag{17}
$$

(16) 有界迫使 $J\le1$。
(17) 中的 $j=-1$ 项最多给一个常数，
这正是 cusp 常项可来自有限极点的情形。
去掉它以后，若有第一个非零的 $b_j$、$j\ge0$，
就得到非零的 $y^{-j-1}$ 量级，违反 (16) 的指数衰减。
故全部 $b_j$、$j\ge0$ 必为零。

于是 $H$ 在该邻域要么为零，要么恰为 $b_{-1}/(\tau-r)$。
全纯恒等定理将此等式延至上半平面。
前者违反 $H\ne0$；后者违反该同余子群中某个
$\tau\mapsto\tau+N$ 的周期性。
这也证明每个 cusp 的 Fourier 尾不可能恒为零。证毕。

对本文的 $\mathcal G$ 应用引理。
Möbius 映射 $\tau=i(1+u)/(1-u)$
把单位圆（除 $u=1$）送到实轴；
有理 cusp 的原像在单位圆上稠密。
在这些点，(2) 中的初等因子 $1/(1-u)$ 不消除障碍。
若 $\mathscr B$ 能穿过任一圆周点亚纯延拓，
该延拓邻域也会包含一个上述有理 cusp 的原像，矛盾。

所以整条圆周都是自然边界，并且原点的准确收敛半径为

$$
 R_{\mathbb C}(\mathscr B)=Nf A=\tau_0^{-1}.
                                                               \tag{18}
$$

## 6. 原中央整函数的增长阶与型

由 (18) 和 Cauchy–Hadamard，

$$
 \limsup_{m\to\infty}|m!e_m|^{1/m}=\tau_0>0.                 \tag{19}
$$

对每个 $\epsilon>0$，有固定 $C_\epsilon$ 使
$|m!e_m|\le C_\epsilon(\tau_0+\epsilon)^m$，从而

$$
 |\mathscr D(Z)|\le C_\epsilon e^{(\tau_0+\epsilon)|Z|}.
                                                               \tag{20}
$$

因此 $\mathscr D$ 是阶至多一、型至多 $\tau_0$ 的整函数。

反过来，若其指数型小于 $\tau_0$，
可取 $b<\tau_0$ 使 $|\mathscr D(Z)|\le C e^{b|Z|}$。
Cauchy 估计取半径 $m/b$，得
$|e_m|\le C(eb/m)^m$。
再用 $(m!)^{1/m}\sim m/e$，
推出 (19) 左边至多 $b$，矛盾。
若阶小于一，同样可对任意 $b>0$ 得到这样的上界。
因此

$$
 \boxed{\quad
   \rho(\mathscr D)=1,\qquad
   \operatorname{type}(\mathscr D)=\tau_0.
 \quad}                                                       \tag{21}
$$

## 7. 对当前跨素数路线的实际含义

Borel 变换的确把普通处已知的
$v_p(e_m)\ge-2v_p(m!)$ 改成
$v_p(m!e_m)\ge-v_p(m!)$。
但它同时把全平面整函数改成了 (2) 的模形式圆盘参数；
(18) 证明这一改变不能忽略。

本文没有排除使用模曲线的其他代数参数、
模形式线丛或 Gauss–Manin 系统研究同一对象。
也没有把自然边界当成 Selmer 非消失的反证。
需要的新桥仍是：如何把几乎所有普通 $p$ 的假想额外中央零阶，
转成某个固定对象足够强的整体算术性质。

### 来源

- K. Bannai, S. Kobayashi, *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*,
  Duke Math. J. **153** (2010), 229–295：
  Proposition 1.3、Example 1.9、Theorem 1.17。
  [作者预印本](https://arxiv.org/abs/math/0610163)。
- 固定 $256$ 点、$d_m$ 与 $e_m$ 的规范：
  本课题 [theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)、
  [中央整函数笔记](2026-11-12-central-diagonal-entire-series.md)。
- $e_1=4/17^3$：
  [固定最低迹的全局证明](2026-11-12-central-theta-d1-exact-global-trace.md)。

周期微分、全纯 cusp 条件、自然边界以及准确增长型在本文直接证明。
