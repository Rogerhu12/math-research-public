# 固定差分逆像的整参数化与有限处大小发散

日期：2026-11-12。**状态：已证明。**

本笔记推进 `2026-11-12-fixed-difference-bost-inputs.md` 的复解析部分：
不只是取得一个较大的复收敛圆盘，而是构造整个 $\mathbb C$ 上的
亚纯延拓。因此 Bost–Chambert-Loir 的典范切线在无穷处的半范数为零。
结合 R28，可证明固定差分逆像的完整图像不是 A-analytic。
这没有把大小损失定位到目标 $\chi$ 分量，也没有推出本题的无穷素数结论。

## 1. 设置

固定一个复嵌入，设
$$
\exp_E:\mathbb C\longrightarrow E(\mathbb C)
$$
为与所选不变微分相配的通用覆盖。
记
$$
\varphi(z)=\Phi(\exp_E z),
\qquad q(z)=\log\varphi(z).
$$
$\varphi$ 是复平面上的亚纯函数，在 $0$ 附近有限非零，且
$\varphi(0)=1$。取 $q(0)=0$ 的局部对数。
R19 给出 $q'(0)=0$，所以可选 $r_0,C_0>0$，使
$$
|q(z)|\le C_0|z|^2\quad (|z|\le r_0).
\tag{1}
$$
这里只需要二阶消失；本题的奇对称实际上给更强的三阶消失。

对 $a=69$、$m\ge1$，令
$$
e_{m,n}=a^n\binom{m+n-1}{n}\in\mathbb Z_{>0}.
$$

## 2. 全平面亚纯乘积

**命题 1。** 乘积
$$
\mathcal F_m(z)
=\prod_{n=0}^{\infty}
\varphi\!\left(\frac{z}{a^{m+n}}\right)^{e_{m,n}}
\tag{2}
$$
定义整个复平面上的亚纯函数，且在 $0$ 附近等于
$$
\exp\left(\sum_{k\ge2}\frac{b_kz^k}{(a^k-a)^m}\right),
\qquad q(z)=\sum_{k\ge2}b_kz^k.
\tag{3}
$$

**证明。** 固定 $R>0$。对充分大的 $n$，$|z|\le R$ 蕴含
$|z/a^{m+n}|\le r_0$，故这些尾因子有限非零，且可使用同一个
局部对数 $q$。由 (1)，
$$
\left|e_{m,n}\,q\!\left(\frac{z}{a^{m+n}}\right)\right|
\le C_0R^2a^{-2m}
\binom{m+n-1}{n}a^{-n}.
\tag{4}
$$
右端关于 $n$ 可求和。因此尾对数在闭圆盘 $|z|\le R$ 上一致收敛，
其指数是非零全纯函数。被截掉的有限个因子是亚纯函数的正整数次幂。
两者的乘积在该圆盘上亚纯，不会产生分数幂的多值问题。
改变截断点或增大圆盘给相容的函数，故 (2) 在全平面亚纯。

在充分小的圆盘内可以绝对交换求和。利用
$\sum_{n\ge0}\binom{m+n-1}{n}x^n=(1-x)^{-m}$，得
$$
\begin{aligned}
\log\mathcal F_m(z)
&=\sum_{k\ge2}b_kz^k
\sum_{n\ge0}\binom{m+n-1}{n}a^{n-(m+n)k}\\
&=\sum_{k\ge2}b_kz^k\,
a^{-mk}(1-a^{1-k})^{-m}\\
&=\sum_{k\ge2}\frac{b_kz^k}{(a^k-a)^m}.
\end{aligned}
$$
这证明 (3)。$\square$

对任意代数数 $c$，令
$$
\mathcal F_{m,c}(z)=e^{cz}\mathcal F_m(z).
\tag{5}
$$
它仍在全平面亚纯，且其形式 germ 就是 R28 的 $F_{m,c}$
在坐标 $z=\log_E(t)$ 中的表示。

## 3. 典范切线半范数确实为零

取射影簇 $X=E\times\mathbb P^1$。因为亚纯函数是到
$\mathbb P^1$ 的全纯映射，式
$$
\Psi_{m,c}:\mathbb C\longrightarrow X(\mathbb C),
\qquad z\longmapsto\bigl(\exp_E z,\mathcal F_{m,c}(z)\bigr)
\tag{6}
$$
在全平面全纯。
它在 $0$ 的导数非零，因为第一分量是椭圆曲线通用覆盖。
其在 $0$ 的形式像恰为 $F_{m,c}$ 的光滑图像 $\widehat C_{m,c}$。
这里不要求 (6) 在全平面单射，也不要求第二分量是 $E$ 上的单值函数。

Bost–Chambert-Loir，
*Analytic curves in algebraic varieties over number fields*，
[arXiv:math/0702593v3](https://arxiv.org/abs/math/0702593v3)，
Proposition 5.15（印刷页 33），对任意相对紧的复圆盘
$\Omega_R=\{|z|<R\}$ 及映射 $\Psi_{m,c}|_{\Omega_R}$ 给出
$$
\left\|D\Psi_{m,c}(0)\frac{\partial}{\partial z}\right\|^{\mathrm{can}}
\le
\left\|\frac{\partial}{\partial z}\right\|^{\mathrm{cap}}_{0,\Omega_R}
=R^{-1}.
\tag{7}
$$
令 $R\to\infty$，得到
$$
\boxed{\quad
\|\cdot\|^{\mathrm{can}}_{\widehat C_{m,c},\infty}=0.
\quad}\tag{8}
$$
论证对每个复嵌入都成立。它使用全平面延拓，
比仅将局部半径放大 $a^m$ 更强。

## 4. 完整形式图像的有限处大小必发散

取定义 $E,\Phi,c$ 的数域 $K_c$。式 (3)–(5) 给出
$F_{m,c}\in K_c[[t]]^\times$。
在每个有限处它都有正解析半径：

- 局部 $q(z)$ 解析；当 $p\nmid a$ 时，
  $v_p(a^k-a)=O_p(\log k)$，故除以 $(a^k-a)^m$ 不改变
  正的 $z$ 收敛半径；
- 当 $p\mid a$ 时，$k\ge2$ 给 $v_p(a^k-a)=v_p(a)$；
- 最后在足够小的圆盘内与 $\log_E$ 及指数复合。

因此 $\widehat C_{m,c}$ 在所有处解析。
在某个好整模型 $\mathcal X/\mathcal O_{K_c}[1/N]$ 中，
记其有限处大小为 $S_v\in(0,1]$。

**命题 2。** 有
$$
\boxed{\quad\sum_{v\nmid N}-\log S_v=+\infty.\quad}
\tag{9}
$$

**证明。** 若此和有限，则 Definition 3.7 给出
$\widehat C_{m,c}$ 是 A-analytic。
此时典范切线度数在 $(-\infty,+\infty]$ 中良好定义。
由 (8)，至少一个阿基米德贡献为 $+\infty$；
A-analytic 保证负贡献可求和，故该度数为 $+\infty$。
Theorem 6.1 遂推出 $\widehat C_{m,c}$ 代数，即 $F_{m,c}$
在 $K_c(E)$ 上代数。这与 R28 矛盾。$\square$

## 5. 对主路线的实际含义

对这些固定差分逆像，复解析条件已经完成；
若某个反设能推出 A-analytic，就立即与 R28 矛盾。
但是 (9) 是对**完整图像、全部有限处**的断言。
它没有证明发散贡献必须来自普通素数的目标字符，
也没有把其大小与 $H_p$ 在中心的零阶建立等价。

前一笔记列出的 tame 共振块、额外圆分因子、线性系数规范及
惰性素数，仍可能承担这种大小损失。
因此不能把 (9) 直接改写为存在无穷多个 $p$ 使
$\operatorname{ord}_{T=p}H_p\le3$。
下一步若要继续这条具体路线，应尝试对这些非目标贡献给出可求和上界，
或构造另一个固定形式对象，使其大小损失被准确限制在目标块中。
