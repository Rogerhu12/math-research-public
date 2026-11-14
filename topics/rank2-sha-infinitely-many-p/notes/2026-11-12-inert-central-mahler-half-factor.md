# 惰性中央权的解析半因子：显式收敛、中央阶数与导数精度

日期：2026-11-12。**状态：本篇的解析构造、阶数比较和有限精度公式已证明；
没有证明导数对无穷多个素数非零。**

本文使用 R38 的 sigma 系数估计、R50 的实际 signed 整比较、R51 的准确
中央平方式。所得半因子是一个从固定截面系数直接构造的过收敛函数。
对惰性素数，现有控制只给 Selmer 余秩的上界，所以本文只证明
半因子的一次导数非零**足以**初级有限，不引用普通情形 R40 的反向等价。

## 1. 固定的两个截面与结论

为避免无关的四次缩放，全部局部系数先在

$$
 E_1:y^2=x^3-x,\qquad \omega=\frac{dx}{2y},\qquad z=\log_E(t),\quad t=-x/y
$$

上计算。令 $\sigma$ 为固定的方格 sigma，$\vartheta^2=x\sigma^2$、
$\vartheta(0)=1$，并置

$$
 \begin{aligned}
 A(z)&=\frac15\vartheta(z)\sigma(z)^{16}
                 (x(z)^2+1)(5x(z)^4-2x(z)^2+1)
            =\sum_{m\ge0}\beta_m z^m,\\
 S(z)&=(x(z)^2+1)\sigma(z)^4
            =\sum_{m\ge0}s_m z^m .
 \end{aligned}                                                    \tag{1.1}
$$

这里 $A\in z^4\mathbb Q[[z^4]]$、$\beta_4=1$，而 $S(0)=1$。
$A$ 是 E17 实际次数十七截面的单位缩放，**不是** E1 自身的秩零
theta 因子；后者恰为 $S$。

固定惰性素数 $p\ge7$，记

$$
 d=p+1,\qquad r=d/4,\qquad R=p^{-1/(p+3)}.
$$

设

$$
 \log\frac{\Sigma(t)}t=\sum_{n\ge1}c_nt^{4n},\qquad
 c=c_r,\qquad \Sigma(t)=\sigma(\log_Et).
                                                               \tag{1.2}
$$

R38 的准确首坏项给 $v_p(c)=-1$。本篇证明存在在半径 $R$ 的闭圆盘
上解析的 $G,G_0$，满足

$$
 A(z)=e^{17cz^d}G(z),\qquad S(z)=e^{4cz^d}G_0(z),
 \qquad \|G\|_R\le R^4,\quad \|G_0\|_R\le1 .                \tag{1.3}
$$

两等式作为形式级数成立；不要求右边的单独指数在整个 $R$ 圆盘上收敛。
写 $G=\sum g_nz^n$、$G_0=\sum g_n^0z^n$，定义下降阶乘
$ (u)_h=u(u-1)\cdots(u-h+1)$、$(u)_0=1$，以及

$$
 \begin{aligned}
 J_p(u)&=\sum_{h\ge0}a_h(u)_h,
       &a_h&=g_{dh}(17c)^{-h},\\
 J_{0,p}(u)&=\sum_{h\ge0}a_h^0(u)_h,
       &a_h^0&=g_{dh}^0(4c)^{-h}.
 \end{aligned}                                                    \tag{1.4}
$$

这两个函数至少在 $|u|_p<p^{2/(p+3)}$ 上解析，并有

$$
 \boxed{J_p\in p u\mathbb Z_p\langle u\rangle,
        \qquad J_{0,p}\in1+p\mathbb Z_p\langle u\rangle.}     \tag{1.5}
$$

对每个整数 $k\ge0$，它们准确插值

$$
 \boxed{
 J_p(k)=k!(17c)^{-k}\beta_{dk},\qquad
 J_{0,p}(k)=k!(4c)^{-k}s_{dk}.
 }                                                             \tag{1.6}
$$

令 $\mathcal A_p(T)\in\mathcal O[[T]]$ 是 R50 的实际 Rubin 整系数，
$\mathcal O=\mathbb Z_{p^2}$；记 $x_m=q^m-1$，其中
$v_p(q-1)=1$。则所有正整数 $k$ 满足

$$
 \boxed{v_p\mathcal A_p(x_{dk})=2v_pJ_p(k).}                  \tag{1.7}
$$

本式允许两边同时为 $+\infty$。特别地，$J_p$ 不恒为零。若

$$
 e=\operatorname{ord}_{u=0}J_p\ge1,
 \qquad j_e=[u^e]J_p\ne0,
$$

则

$$
 \boxed{
 \operatorname{ord}_{T=0}\mathcal A_p=2e,\qquad
 v_p([T^{2e}]\mathcal A_p)=2v_p(j_e)-2e.
 }                                                             \tag{1.8}
$$

因此 $v_p(j_e)\ge e$，Rubin 中央首项的赋值是偶数。由 R50 的
signed 控制立即得到

$$
 J_p'(0)\ne0\quad\Longrightarrow\quad
 \Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}.                 \tag{1.9}
$$

更窄的首中央单位条件准确为

$$
 \boxed{
 b_{p+1}^{(17)}\in\mathbb Z_p^\times
 \quad\Longleftrightarrow\quad
 J_p'(0)/p\in\mathbb Z_p^\times .
 }                                                             \tag{1.10}
$$

式 (1.10) 的证明用全部权的整比较；它不删除 (1.4) 中的小 $h\ge2$ 项。

## 2. 余项可以延到明确的较大半径

R38 的递推在参数 $D=1$ 时给

$$
 w_n=(-1)^n\binom{2n}{n},\qquad
 c_n=\frac1{4n}\left(w_n-\frac12\sum_{j=1}^n
                  \frac{w_{n-j}w_j}{4j-1}\right),
                                                               \tag{2.1}
$$

以及

$$
 v_p(c_n)\ge-v_p(n)-\max_{1\le j\le n}v_p(4j-1),\qquad
 c_n\in\mathbb Z_p\ (n<r),\qquad v_p(c_r)=-1.                 \tag{2.2}
$$

令 $g=p^{-1/(p-1)}$ 为指数的临界范数，
$F_*(t)=\sum_{n\ne r}c_nt^{4n}$。我们逐项证明

$$
             v_p(c_n)+\frac{4n}{p+3}>\frac1{p-1}
                      \qquad(n\ne r).                       \tag{2.3}
$$

* $n<r$：左边至少 $4/(p+3)>1/(p-1)$。
* $r<n<p$：由 (2.2)，左边至少
  $-1+(p+5)/(p+3)=2/(p+3)>1/(p-1)$。
* $p\le n<p^2/4$：$v_p(n)\le1$ 且 $4j-1<p^2$，故
  左边至少 $-2+4p/(p+3)>1/(p-1)$。
* $p^2/4\le n<p^2$：$v_p(n)\le1$、$4j-1<p^3$，故
  左边至少 $-3+p^2/(p+3)>1/(p-1)$。
* $n\ge p^2$：令 $a=\lfloor\log_p n\rfloor\ge2$。
  左边至少 $-(2a+1)+4p^a/(p+3)$。在 $a=2,p\ge7$ 时已严格
  大于 $1/(p-1)$；之后正项至少乘七，负项只增加二。

式 (2.2) 的负项只有 $O(\log n)$，所以加权系数趋于零，
严格不等式的上确界由有限多个项达到。因此

$$
                         \|F_*\|_R<g.                       \tag{2.4}
$$

接着核对从 $t$ 到加法坐标 $z$ 的实际换元。形式对数是

$$
 L(t)=t+\sum_{n\ge1}\frac{w_n}{4n+1}t^{4n+1}.
                                                               \tag{2.5}
$$

对 $q=4n+1>1$，相对于首项的加权赋值至少为
$(q-1)/(p+3)-v_p(q)$。若 $p\nmid q$，此值至少 $4/(p+3)$。
若 $v_p(q)=1$，因 $p\equiv3\bmod4$ 而 $q\equiv1\bmod4$，
有 $q\ge3p$，同样至少 $4/(p+3)$。若 $v_p(q)=a\ge2$，则

$$
 \frac{q-1}{p+3}-a
 \ge\frac{p^a-1}{p+3}-a\ge\frac4{p+3}.
$$

最后一个不等式在 $a=2,p=7$ 已成立，之后随 $a,p$ 增大保持成立。
故 $L$ 在该圆盘是等距解析坐标，且其解析逆 $t=t(z)$ 满足

$$
 \left\|\frac{L(t)}t-1\right\|_R\le R^4<1,
 \qquad
 \left\|\frac{t(z)}z-1\right\|_R\le R^4.                   \tag{2.6}
$$

逆的估计也可直接由 $t=z/(1+(L(t)/t-1))$ 的严格收缩迭代得到。
所有级数的尾在该半径趋于零，故此处是实际解析逆，不只形式逆。

由于 $d=p+1$ 是 $p$-单位，由 (2.6) 得

$$
 \|c(t(z)^d-z^d)\|_R
 \le pR^{d+4}=p^{-2/(p+3)}<g.                               \tag{2.7}
$$

因此

$$
 U(z)=F_*(t(z))+c(t(z)^d-z^d)
$$

满足 $\|U\|_R<g$，所以 $e^{4U}$、$e^{17U}$ 及其逆在该圆盘上
解析，范数都是一。

最后，$X(t)=t^2x(t)\in1+t^4\mathbb Z_p[[t^4]]$；在 $p\ge7$ 时
下列两个前因子均整：

$$
 \begin{aligned}
 H(t)&=\frac15\sqrt{x(t)}(x(t)^2+1)
                  (5x(t)^4-2x(t)^2+1)t^{17}
                       \in t^4(1+t^4\mathbb Z_p[[t^4]]),\\
 H_0(t)&=(x(t)^2+1)t^4\in1+t^4\mathbb Z_p[[t^4]].
 \end{aligned}                                                    \tag{2.8}
$$

这里 $t\sqrt{x(t)}$ 取常数项一的平方根；$2,5$ 都是单位。
取

$$
 G(z)=H(t(z))e^{17U(z)},\qquad
 G_0(z)=H_0(t(z))e^{4U(z)},                                  \tag{2.9}
$$

立即得到 (1.3) 及其全部 Gauss 范数界。

## 3. 过收敛插值及准确参考赋值

式 (1.3) 给明确系数估计

$$
 \boxed{
 v_p(a_h)\ge\left\lceil\frac{2h+4}{p+3}\right\rceil,
 \qquad
 v_p(a_h^0)\ge\left\lceil\frac{2h}{p+3}\right\rceil
                   \quad(h\ge1).
 }                                                             \tag{3.1}
$$

$a_0=0$、$a_0^0=1$。由于 $(u)_h\in\mathbb Z[u]$，(3.1) 使
(1.4) 在 Tate 代数中收敛；在任意 $|u|_p\le p^\epsilon$、
$\epsilon<2/(p+3)$ 上仍一致收敛，证明过收敛性及 (1.5)。

整数 $k\ge0$ 处，$h>k$ 的下降阶乘为零，而

$$
 [z^{dk}]e^{17cz^d}G(z)
       =\sum_{h=0}^k g_{dh}\frac{(17c)^{k-h}}{(k-h)!}.
$$

这就是 (1.6)；参考式同理。特别地，参考函数在整个
$\mathbb Z_p$ 上是单位，所以所有同支正权都有准确赋值

$$
 \boxed{v_p s_{dk}=-k-v_p(k!),\qquad
 v_p d_{dk}^{(0)}=-2k-2v_p(k!)\quad(k\ge0).}                 \tag{3.2}
$$

第二式使用已证明的参考全权平方

$$
 d_m^{(0)}/f_0^{2m+1}=\frac14\,32^{-m}s_m^2
                         \quad(4\mid m),                    \tag{3.3}
$$

见 [dyadic 向量与参考 theta](2026-11-12-dyadic-vector-and-reference-theta.md)
§§6–7。该证明使用实际参考向量，不以任意 theta 替换它。

## 4. 与同一个 signed Rubin 函数的中央阶数比较

R51 的单位四次缩放给

$$
 b_{4n}^{(17)}=17^{n-1}\beta_{4n}.
                                                               \tag{4.1}
$$

故在 $m=dk$ 上，$v_p b_m^{(17)}=v_p\beta_m$。
R51 的准确中央平方式和 (3.3) 中所有额外常数都是当前 $p$ 的单位，
于是

$$
 v_pd_{dk}^{(17)}=2v_p\beta_{dk},\qquad
 v_pd_{dk}^{(0)}=2v_ps_{dk}.                                  \tag{4.2}
$$

参考值由 (3.2) 永远非零，所以 R50 的全权相对比较可用于每个正整数
$k$。两个指数常数 $17c,4c$ 的赋值都为 $-1$，两个 $k!$ 完全相同，
而 $J_{0,p}(k)$ 是单位。因此

$$
 \begin{aligned}
 v_p\mathcal A_p(x_{dk})
 &=v_pd_{dk}^{(17)}-v_pd_{dk}^{(0)}\\
 &=2\bigl(v_pJ_p(k)-v_pJ_{0,p}(k)\bigr)
   =2v_pJ_p(k),
 \end{aligned}                                                    \tag{4.3}
$$

证明 (1.7)。由连续性，赋值恒等式也延拓到所有 $k\in\mathbb Z_p$；
本文的阶数证明只用正整数 $k=p^a$。

Burungale–Kobayashi–Ota 2021 Theorem 6.1 的特征理想与同节的
torsion 结论给 $\mathcal A_p\ne0$。若 $J_p$ 恒零，则 (4.3) 使
$\mathcal A_p$ 在无限多个 $x_{dp^a}\to0$ 上为零，矛盾。
故两者都有有限中央阶数。写

$$
 \mathcal A_p(T)=\alpha T^q+\cdots,\qquad
 J_p(u)=j_eu^e+\cdots .
$$

对充分大的 $a$，由于 $v_p(x_{dp^a})=a+1$，(4.3) 成为

$$
                  q(a+1)+v_p\alpha=2ea+2v_pj_e.
$$

比较关于 $a$ 的斜率和常数，得到 $q=2e$ 及 (1.8)。这一步仅使用
R50 已证明的相对赋值式；没有宣称两套高权周期之间的未知单位随权
形成一个全局解析单位。

R50 的已发表 signed 控制给

$$
 2\le s_p\le\operatorname{ord}_0\mathcal A_p=2e,
$$

所以 $J_p'(0)\ne0$ 时 $e=1$、$s_p=2$，证明 (1.9)。
此处没有反向证明 $s_p=2\Rightarrow e=1$。

最后证明 (1.10)。由 $\beta_0=0$，(1.6) 在 $k=1$ 时给

$$
                         J_p(1)=\beta_d/(17c).
$$

因此 $\beta_d$ 为单位恰为 $v_pJ_p(1)=1$，也恰为
$v_p\mathcal A_p(x_d)=2$。又 $\mathcal A_p\in T^2\mathcal O[[T]]$、
$v_p x_d=1$，所以后者恰为 $[T^2]\mathcal A_p$ 是单位。
由 (1.8)，这准确等价 $e=1$ 且 $v_pJ_p'(0)=1$。
再用 (4.1)，得到 (1.10)。

**小 $h$ 项并没有被略去。** 这个单位等价来自所有权的相对公式
以及同一个整幂级数 $\mathcal A_p$，而不是从 (3.1) 猜测 $h=1$
独占导数的最低层。

## 5. 导数的有限精度证书

过收敛性允许逐项求导。由
$\left.\frac d{du}(u)_h\right|_{u=0}=(-1)^{h-1}(h-1)!$ 得

$$
 \boxed{J_p'(0)=
       \sum_{h\ge1}(-1)^{h-1}(h-1)!
                  \frac{g_{dh}}{(17c)^h}.}                  \tag{5.1}
$$

令 $L_{p,H}$ 为前 $H$ 项之和。式 (3.1) 与阶乘赋值的单调性给

$$
 \boxed{
 v_p\bigl(J_p'(0)-L_{p,H}\bigr)
 \ge M_{p,H}:=
       \left\lceil\frac{2H+6}{p+3}\right\rceil+v_p(H!).
 }                                                             \tag{5.2}
$$

若某个有限 $H$ 满足 $v_pL_{p,H}<M_{p,H}$，就严格证明
$J_p'(0)\ne0$，从而给该 $p$ 的初级有限证书。反过来，若导数非零，
$M_{p,H}\to\infty$ 保证某个有限 $H$ 会检测到它。

单位层只需保留 $H=(p-1)/2$：此时 $M_{p,H}=2$，故

$$
 \frac{J_p'(0)}p\equiv
 \sum_{h=1}^{(p-1)/2}(-1)^{h-1}(h-1)!
                  \frac{g_{dh}}{p(17c)^h}\pmod p .           \tag{5.3}
$$

各项在取模前都是整的。与 (1.10) 合并，右边非零与原首中央单位
完全等价。式 (5.3) 使用到 $G$ 的次数 $(p^2-1)/2$，比原来直接求
$\beta_{p+1}$ 的 jet 更长；它的用途是落实真正中央导数及更高精度，
不是宣称计算首权更快，也没有据此得到无穷非零。

### 5.1 首中央非单位迫使整个首层下降阶乘多项式消失

这一步比只考察 (5.3) 的一个线性组合更强。由 (3.1)，

$$
 Q_p(u):=J_p(u)/p\bmod p
    =\sum_{h=1}^{(p-1)/2}(a_h/p)(u)_h
                  \in\mathbb F_p[u],\qquad
 \deg Q_p\le(p-1)/2.                                      \tag{5.4}
$$

若 $b_d^{(17)}$ 不是单位，(1.10) 的证明给
$[T^2]\mathcal A_p\in p\mathcal O$。于是对每个整数
$k\in\mathbb Z_p^\times$，

$$
 v_p\mathcal A_p(x_{dk})\ge3.
$$

式 (4.3) 的右边为偶整数，所以实际上 $v_pJ_p(k)\ge2$。
因此 $Q_p$ 在全部 $\mathbb F_p^\times$ 上为零，而 $Q_p(0)=0$。
次数小于 $p$ 迫使 $Q_p=0$。下降阶乘多项式是首一三角基，故

$$
 \boxed{
 b_d^{(17)}\in p\mathbb Z_p
 \quad\Longleftrightarrow\quad
 a_h\in p^2\mathbb Z_p\quad\text{对每个 }h\ge1
 \quad\Longleftrightarrow\quad
 J_p\in p^2u\mathbb Z_p\langle u\rangle.
 }                                                             \tag{5.5}
$$

其中 $h>(p-1)/2$ 的整除性原已由 (3.1) 给出；反向只用
$a_1=J_p(1)=\beta_d/(17c)$。最后一个等价亦可由有限截断的三角基
及尾的 $p^2$ 整除直接得到，并未对无限 Hom 作未经核对的基变换。

所以原首权非单位会强迫一个长度约 $p/2$ 的完整截断同时消失。
若能够用实际固定截面或下一节的参考消期覆盖证明这些系数不能全部
消失，就会证明首权单位。本篇尚未得到这样的算术非消失定理。

## 6. 参考消期后的真正固定代数覆盖

两个指数满足 $4(17c)=17(4c)$，因此在同一个加法坐标中有

$$
 \boxed{
 \frac{G(z)^4}{G_0(z)^{17}}
 =\frac{A(z)^4}{S(z)^{17}}
 =\frac{x(z)^2(5x(z)^4-2x(z)^2+1)^4}
         {5^4(x(z)^2+1)^{13}}.
 }                                                             \tag{6.1}
$$

这是一个实际恒等式。它把消去共同 sigma 周期后的代数对象明确为

$$
 \widetilde C:\quad y^2=x^3-x,\qquad
                       v^4=\frac{x^2}{x^2+1},               \tag{6.2}
$$

以及其上的函数

$$
 B=\frac{5x^4-2x^2+1}{5(x^2+1)^3}\,v.
                                                               \tag{6.3}
$$

在 $O$ 上方选 $v\to1$ 的支，则 $B(z)=z^4+\cdots$，并有
$A/S^{17/4}=B$。右边 $17/4$ 次幂取常数项一的支。
同样 $G/G_0^{17/4}=B$；由于 $G_0-1$ 在上述圆盘范数小于一，
这个 $p$-进二项式幂也实际收敛。

式 (6.2) 的连通光滑射影正规化是亏格七曲线。事实上

$$
 \operatorname{div}\frac{x^2}{x^2+1}
       =4(T)-\sum_{[2]Q=T}(Q),\qquad T=(0,0).
$$

四个 $[2]Q=T$ 点的赋值为 $-1$，故扩张次数准确为四且各点完全
分歧；其他点均不分歧。Riemann–Hurwitz 给
$2g-2=4(2\cdot1-2)+4(4-1)=12$，所以 $g=7$。
这与前一篇 double-cover Cartier 审计中的曲线不同。

**尚未得到的映射。** (6.1) 消掉的是原函数的共同 sigma 因子。
下降阶乘变换 (1.4) 不是乘法同态，因此不能把 $G/G_0^{17/4}$
直接换成 $J_p/J_{0,p}^{17/4}$，也不能把本曲线的任意 Cartier entry
直接称为 $J_p'(0)$。若要使用固定覆盖的 Frobenius 理论，还须构造
这个变换及参考解析因子与实际 cohomology 的比较。

## 依赖和来源

- [R38：准确惰性 sigma 大小](../results/R38-exact-inert-sigma-size-and-jet-budget.md)，
  尤其式 (5)–(7)、(16)。本篇重新给出较大余项半径的完整估计。
- [R50：惰性中央整比较](../results/R50-inert-central-integral-comparison.md)，
  尤其全权式 (8) 及 signed 控制。本文没有更改其中 period 规范。
- [R51：实际次数十七截面与平方常数](../results/R51-explicit-theta-section-and-central-square-constant.md)，
  式 (1)–(3)、(11)。
- [参考 theta 的实际有限向量与全权平方](2026-11-12-dyadic-vector-and-reference-theta.md)，
  §§6–7，式 (15)、(17)。
- A. Burungale, S. Kobayashi, K. Ota,
  *Rubin's conjecture on local units in the anticyclotomic tower at inert primes*,
  Annals of Mathematics **194** (2021), 943–966，Theorems 6.1–6.2 及
  §6.0.2 的 torsion 性；[原文](https://par.nsf.gov/servlets/purl/10336626)。
  这里只用已证明的 Rubin 函数非零和基层 Selmer 上界。
