# R47. 中央 Borel 变换的模形式实现及准确复增长

日期：2026-11-12。**状态：已证明；不提供额外跨素数非零性。**

## 1. 定理

设
$$
A=\Omega_E^2/\pi_{\mathbb C},\qquad
\tau_0=(Nf\,A)^{-1},\qquad
\mathscr D(Z)=\sum_{m\ge0}e_mZ^m,\qquad
\mathscr B(T)=\sum_{m\ge0}m!e_mT^m.
$$
存在一个固定非零权一模形式
$\mathcal G\in M_1(\Gamma(68))$，在所有 cusp 全纯，满足
$$
\boxed{
\mathscr B(T)=\frac{1}{f\Omega_E(1-u)}
 \mathcal G\!\left(i\frac{1+u}{1-u}\right),\qquad
u=\frac{T}{Af^2}=-i\tau_0T.
}
\tag{1}
$$
此外：

1. $\mathcal G(i)=0$，$\mathcal G'(i)\ne0$。
2. $\mathscr B$ 的准确收敛半径为 $\tau_0^{-1}$，
   且整个边界圆均不容亚纯延拓。
3. $\mathscr D$ 是阶恰为一、指数型恰为
   $\tau_0=\pi_{\mathbb C}/(Nf\,\Omega_E^2)$ 的整函数。

这使用全部权 $m\ge0$，没有把 R46 的 $4\mid m$ 范数公式扩大适用范围。

## 2. 固定挠点标签及权一形式

对固定256点导子轨道，选标签
$(r_S,s_S)\in(68^{-1}\mathbb Z)^2/\mathbb Z^2$，
使 $S=r_S\Omega_E+s_Si\Omega_E$。
所有标签非零。对变化的有向周期
$\boldsymbol\omega=(\omega_1,\omega_2)$，定义
$$
g(\boldsymbol\omega)=
 \sum_S\{\zeta_{\boldsymbol\omega}(r_S\omega_1+s_S\omega_2)
           -r_S\eta_1-s_S\eta_2\}.
\tag{2}
$$
固定有理标签使每项全纯；改变标签的整数代表不改变该式。
由
$\eta_j=s_2\omega_j+\bar\omega_j/A(\boldsymbol\omega)$，
括号正是 $e^*_{0,1}(z_S,0;\Lambda_{\boldsymbol\omega})$。
其两个非全纯修正在固定标签下恰合成准周期项。

有
$g(a\omega_1,a\omega_2)=a^{-1}g(\boldsymbol\omega)$，
且 $\Gamma(68)$ 换基保持标签。
故 $\mathcal G(\tau)=g(1,\tau)$ 为权一模形式。

cusp 条件可直接检验。取 $0\le s<1$，若 $s=0$ 则 $r\notin\mathbb Z$。
每个括号可写为
$$
\frac{\theta_1'(r+s\tau;\tau)}{\theta_1(r+s\tau;\tau)}
       +2\pi_{\mathbb C}is.
$$
theta 乘积的对数导数为
$$
\pi_{\mathbb C}\cot(\pi_{\mathbb C}z)
 +4\pi_{\mathbb C}\sum_{n\ge1}
       \frac{q^n}{1-q^n}\sin(2\pi_{\mathbb C}nz).
$$
代入 $z=r+s\tau$ 后，除常数项外只有正的 $q^{1/68}$ 幂。
任意 cusp 换基仍给非零、分母除68的标签，故所有 cusp 全纯。

## 3. 周期微分给两个准确阶乘

令
$$
W=-A(\boldsymbol\omega)^{-1}
 \left(\bar\omega_1\partial_{\omega_1}
       +\bar\omega_2\partial_{\omega_2}\right).
$$
Wirtinger 微分给 $WA=0$、$W\bar\omega_j=0$。
对 $\beta=z_S+\gamma$，有 $W\beta=-\bar\beta/A$。

在 $\Re\varepsilon>1/2$，级数及所需导数绝对一致收敛，
直接微分得到
$$
W^m\sum_\gamma\frac1{\beta|\beta|^{2\varepsilon}}
 =\frac{(1+\varepsilon)\cdots(m+\varepsilon)}{A^m}
  \sum_\gamma\frac{\bar\beta^m}
                    {\beta^{m+1}|\beta|^{2\varepsilon}}.
\tag{3}
$$
用 Eisenstein–Kronecker 的 Hecke 延拓后，
$\varepsilon=0$ 无极点，因为其第一指标是正数 $2m+1$。
参数微分可由同一 theta 积分表示在周期紧邻域下交换。
故
$$
W^mg=\frac{m!}{A^m}\sum_Se^*_{m,m+1}(z_S,0;\Lambda).
$$
原中央对角的准确规范为
$$
d_m=\frac1{m!A^m}\sum_Se^*_{m,m+1}(z_S,0;\Gamma).
$$
于是
$$
\boxed{\left.W^mg\right|_{(\Omega_E,i\Omega_E)}=(m!)^2d_m.}
\tag{4}
$$

在全纯变形
$\boldsymbol\omega(u)=\boldsymbol\omega-u\overline{\boldsymbol\omega}$
中，右边共轭周期固定为初值。
由 $WA=0$ 和 (4)，
$$
g(\boldsymbol\omega(u))=\sum_{m\ge0}A^m m!d_m u^m.
$$
又
$\omega_1(u)=\Omega_E(1-u)$、
$\omega_2(u)=i\Omega_E(1+u)$，
其比值在上半平面当且仅当 $|u|<1$。
代入 $u=T/(Af^2)$ 并除以 $f$，即得 (1)。

R45 给 $e_0=0$、$e_1=4/17^3\ne0$。
由 (1) 的零次与一次项，
$\mathcal G(i)=0$ 且 $\mathcal G'(i)\ne0$，
也保证 $\mathcal G$ 非恒零。

## 4. 整个边界圆不能亚纯延拓

先证明一般事实：非零正权一全纯模形式 $H$ 不能穿过任何有理实点
$r=a/c$ 作亚纯延拓。

取 $\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，
$h=H|_1\gamma$ 在无穷 cusp 满足
$h(iy)=a_0+O(e^{-\epsilon y})$。
若 $H(r+v)=\sum_{j=-J}^\infty b_jv^j$ 亚纯，
则因 $\gamma\tau-r=-1/[c(c\tau+d)]$，
$$
h(\tau)=\sum_{j=-J}^\infty
 b_j(-1/c)^j(c\tau+d)^{-j-1}.
$$
有界性迫使 $J\le1$。$j=-1$ 项可给 cusp 常数项；
去掉该项后，任意首个非零的 $j\ge0$ 项给幂衰减，
与 Fourier 余项的指数衰减矛盾。
所以 $H$ 必在一个邻域等于零或 $b_{-1}/(\tau-r)$。
恒等定理延至上半平面；前者违反非零，
后者违反同余子群包含的整数平移周期性。
这也同时排除了某 cusp 只有常项、没有 Fourier 尾的情形。

有理实点在 $\tau=i(1+u)/(1-u)$ 下的原像稠密于单位圆。
若 (1) 能穿过任一圆周点亚纯延拓，
邻域内必包含这些禁止的有理 cusp 原像。
因而整个圆周都是自然边界，准确半径为 $Nf\,A$。

## 5. 整函数的准确型

Cauchy–Hadamard 给
$$
\limsup_{m\to\infty}|m!e_m|^{1/m}=\tau_0.
$$
故对每个 $\epsilon>0$，
$|\mathscr D(Z)|\le C_\epsilon e^{(\tau_0+\epsilon)|Z|}$。
若其型小于 $\tau_0$，可取 $b<\tau_0$ 使
$|\mathscr D(Z)|\le Ce^{b|Z|}$。
Cauchy 估计在半径 $m/b$ 给
$|e_m|\le C(eb/m)^m$；
结合 Stirling 公式，上述 limsup 至多 $b$，矛盾。
阶小于一也会给任意 $b>0$ 的这种上界。
因此阶恰为一、型恰为 $\tau_0$。

## 6. 对算术路线的范围

Borel 变换去掉一个阶乘，确实改善普通系数的已知分母界；
但其复参数域随之成为具有自然边界的模形式圆盘。
不能同时沿用原来全平面整函数的 Herblot 一致化输入。

本结果不排除使用模曲线的代数参数、模形式线丛、
Gauss–Manin 系统或新的 p-adic 比较。
中心额外零阶如何强迫足够的整体算术改善仍未证明。

### 完整证明与来源

- [全权 Borel 模形式证明](../notes/2026-11-12-central-borel-modular-uniformization.md)，
  含全部周期规范、cusp 展开、Hecke 延拓及自然边界论证；已由根端独立复核。
- Kenichi Bannai, Shinichi Kobayashi,
  *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*,
  Duke Math. J. **153** (2010), 229–295，
  Proposition 1.3、Example 1.9、Theorem 1.17：
  [作者预印本](https://arxiv.org/abs/math/0610163)。
- R45 给非零最低系数；固定 theta 对角笔记给 (4) 所用的准确阶乘规范。
