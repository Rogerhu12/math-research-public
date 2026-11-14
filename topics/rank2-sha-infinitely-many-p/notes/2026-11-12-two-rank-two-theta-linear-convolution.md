# 两条实际秩二 theta 行：固定有理乘子与完整 Mellin 卷积

日期：2026-11-12。**状态：以下恒等式与测度比较已证明。**
本篇保留原始的两条 theta 行，不由有理乘子的非挠零点推断中央导数非零。

## 1. 共同曲线尺度中的准确恒等式

全部函数先放在 $E_0:y^2=x^3-x$ 上，使用 $\omega=dx/(2y)$、
$x(z)=\wp_0(z)$、$y(z)=\wp_0'(z)/2$、$\sigma=\sigma_0$。
记 $\vartheta^2=x\sigma^2$、$\vartheta(0)=1$，以及
$$
 X=x^2,\qquad f(X)=5X^2-2X+1.
$$
R51 与 R115 的两份首项为 $z^4$ 的**实际**截面是
$$
 A(z)=\frac15\vartheta(z)\sigma(z)^{16}(X+1)f(X),
$$
$$
 B(z)=\frac15\sigma(z)^{68}X(X-1)(X+1)^2
                (X^2-2X+5)f(X)Q_8(X),                         \tag{1}
$$
其中
$$
 Q_8=X^8+364X^6-1088X^5+1190X^4-1088X^3+364X^2+1.
$$
$A$ 是 $E_{17}$ 的既有实际行经固定尺度改变后的截面；$B$ 是 R115
已用完整十七个系数严格认证的 $E_{34}$ 行。

设
$$
\begin{aligned}
 H_1(X)&=X^4+4X^3+70X^2+4X+1,\\
 H_2(X)&=X^4+20X^3-26X^2+20X+1,\\
 R(X)&=\frac{(X+1)Q_8(X)}{(X-1)H_1(X)H_2(X)}.
\end{aligned}                                                    \tag{2}
$$
则有完整恒等式
$$
                 \boxed{\quad 16B(z)=R(x(z)^2)A(2z).\quad}       \tag{3}
$$
这将次数六十八的 $B$ 与次数同为六十八的 $[2]^*A$ 比较；
不需要把 $B$ 先改写成 $A^4$。

**证明。** 在当前首项规范下，二倍公式是
$$
 \sigma(2z)=-2y(z)\sigma(z)^4,\qquad
 \vartheta(2z)=(X+1)\sigma(z)^4,
$$
$$
 x(2z)=\frac{(X+1)^2}{4x(X-1)}.
$$
前两式可由除子和原点首项 $2z$、$1$ 核定，第三式是椭圆曲线的二倍公式。
令 $D=16X(X-1)^2$。代入 $A(2z)$ 得
$$
 A(2z)=\frac{16}{5}\sigma(z)^{68}X(X-1)^2(X+1)G(X),
$$
$$
 G=5(X+1)^{12}+3(X+1)^8D-(X+1)^4D^2+D^3.
$$
准确的整系数因式分解为
$$
                   G=(X^2-2X+5)f(X)H_1(X)H_2(X).                \tag{4}
$$
与 (1) 相除即为 (3)。这些都是全局函数恒等式，原点处的可去因子已消去。

## 2. 固定乘子的局部规范和二挠平移

置 $v=1/X$。三个次数为偶数的多项式 $Q_8,H_1,H_2$ 都互反，故
$$
 R=\frac{(1+v)Q_8(v)}{(1-v)H_1(v)H_2(v)}\in1+v\mathbb Z[[v]],
$$
$$
                    R=1-22v+770v^2-17430v^3+\cdots.             \tag{5}
$$
因此 $R$ 在原点正则，$R(O)=1$；不存在 (3) 中被忽略的原点极点或常数。
又有
$$
                            R(1/X)=-R(X).                       \tag{6}
$$
对 $T_0=(0,0)$，加法公式给 $x(P+T_0)=-1/x(P)$，所以
$$
                 R(x(P+T_0)^2)=-R(x(P)^2).                     \tag{7}
$$
这是同一实际乘子的二挠平移性质。它不把 $T_0$ 当作普通形式圆盘内的平移。

由 (3)，$R$ 的极点都来自 $[2]^*A$ 的挠点零除子。
在 $X=1$ 的两个二挠点，其极点阶为二；其余可能极点由 $H_1H_2$ 给出。
R117 所证的三十二个非挠零点仍在分子 $Q_8$ 中。
这里没有把 $R\omega$ 与 $d\log R$ 混同：前者的极点是上述挠点，
后者还在这些非挠零点有留数。

为核定最低项，令 $u=1/\sqrt{x}$。由 $u''=-2u^3$、$u(0)=0$、$u'(0)=1$，
$$
 v=u^4=z^4-\frac25z^8+O(z^{12}),\qquad
 R(x(z)^2)=1-22z^4+\frac{3894}{5}z^8+O(z^{12}).                 \tag{8}
$$
R51 的共同尺度系数 $[z^8]A=97/60$ 因而给
$$
 [z^8]B=16\frac{97}{60}-22=\frac{58}{15},
$$
与 R115 的独立证书一致。

## 3. 原普通测度之间的完整线性卷积

设 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$。固定一个包含所需未分歧
系数的完备整数环 $\mathcal O$，以及 $E_0$ 的同一个普通周期 $\Omega_p$。
选择整正式群同构
$$
 t(Z)=\exp_{E_0}\bigl(\Omega_p\log(1+Z)\bigr)\in Z\mathcal O[[Z]],
 \qquad t'(0)=\Omega_p\in\mathcal O^\times.
$$
R38 的普通整 sigma 和 (1) 给整 Amice 级数
$$
 \mathcal A_p(Z)=A\bigl(\Omega_p\log(1+Z)\bigr),\qquad
 \mathcal B_p(Z)=B\bigl(\Omega_p\log(1+Z)\bigr).
$$
记对应的有界整测度为 $\nu_{A,p},\nu_{B,p}$。
另外，$v(t)=x(t)^{-2}\in t^4\mathbb Z_p[[t]]$，所以 (5) 给
$$
 \mathcal R_p(Z)=R(x(t(Z))^2)\in1+Z^4\mathcal O[[Z]].           \tag{9}
$$
它对应唯一有界整测度 $\sigma_p$，其总质量为一。
这不声称 $\sigma_p$ 为正测度，也不声称它只支撑于单位或 $p\mathbb Z_p$。

Amice 乘积对应**加法卷积**，$z\mapsto2z$ 对应测度的 $[2]$ 推前。
(3) 遂给
$$
              \boxed{\quad 16\nu_{B,p}
                       =\sigma_p*[2]_*\nu_{A,p}.\quad}          \tag{10}
$$
这使用了整个 $\mathbb Z_p$ 上的测度，不在卷积前删去非单位。

这些确实是原两条曲线的测度，而非另造的形式测度。
若原曲线的微分周期分别记为 $\Omega_{17,p},\Omega_{34,p}$，
可通过固定整 CM 同构相容选取
$$
 \Omega_p=17^{1/4}\Omega_{17,p}=\sqrt{34}\,\Omega_{34,p}.
$$
准确的复及形式尺度关系为
$$
 A_{17,\mathrm{orig}}(z)=17^{-1}A(17^{1/4}z),\qquad
 A_{34,\mathrm{orig}}(z)=34^{-2}B(\sqrt{34}\,z).
$$
故 $\nu_{A,p}=17\nu_{17,p}$、$\nu_{B,p}=34^2\nu_{34,p}$。
两个标量都是所列 $p$ 的单位；它们不会改变实际中央导数的消失与否。

## 4. 不省略单位边界的原 Mellin 导数公式

对 $x\in\mathbb Z_p^\times$ 置
$$
 \ell_p(x)=\frac{\log\langle x\rangle}{\log(1+p)},\qquad
 f_p(x)=\ell_p(x),
$$
并在 $p\mathbb Z_p$ 定义 $f_p(x)=0$。
这是整个 $\mathbb Z_p$ 上的连续 $\mathbb Z_p$ 值函数。
原 principal Mellin 系列为
$$
 J_A(T)=\int_{\mathbb Z_p^\times}(1+T)^{\ell_p(x)}\,d\nu_{A,p}(x),
 \qquad
 J_B(T)=\int_{\mathbb Z_p^\times}(1+T)^{\ell_p(x)}\,d\nu_{B,p}(x).
$$
于是 (10) 严格给
$$
 \boxed{\quad
 16J_B'(0)=\int_{\mathbb Z_p^2}f_p(u+2x)\,
                              d\sigma_p(u)\,d\nu_{A,p}(x).
 \quad}                                                        \tag{11}
$$
特别地，它不是两个 Mellin 系列的乘积。

利用 $\sigma_p(\mathbb Z_p)=1$ 以及已证的实际 $J_A(0)=0$，
$$
 \int f_p(2x)\,d\nu_{A,p}(x)
     =J_A'(0)+\ell_p(2)J_A(0)=J_A'(0).
$$
因此可写成一条准确的两行斜率关系
$$
 \boxed{\quad
 16J_B'(0)-J_A'(0)
  =\int_{\mathbb Z_p^2}\bigl(f_p(u+2x)-f_p(2x)\bigr)\,
                           d\sigma_p(u)\,d\nu_{A,p}(x).
 \quad}                                                        \tag{12}
$$
右侧保留了 $u+2x$ 变成非单位、或者 $x$ 原为非单位的全部贡献。
没有未经支撑控制就将核换成 $\log(1+u/(2x))$。
(12) 不需要在本篇额外假定 $J_B(0)=0$，也不新增未经证明的
$E_{34}$ Selmer 零阶比较。

在原曲线规范下，等价的左边为
$$
                 16\cdot34^2J_{34}'(0)-17J_{17}'(0).           \tag{13}
$$
右边仍使用 (10) 中已明确归一的两份测度。

## 5. 系数行及目前尚需的真实输入

写 $A=\sum a_{4n}z^{4n}$、$B=\sum b_{4n}z^{4n}$、
$R(x(z)^2)=\sum r_{4j}z^{4j}$，其中 $r_0=1$。
同一恒等式给全部权的三角关系
$$
        16b_{4n}=\sum_{j=0}^{n-1}r_{4j}\,2^{4(n-j)}a_{4(n-j)}.
                                                                  \tag{14}
$$
它直接适用于原普通权 $p-1$ 和惰性权 $p+1$，但没有丢弃任何较低权项。
普通处的完整关系则为 (10)–(12)，不限于首层。

因此，如果能证明 (12) 的**这个实际右端**对无穷多个普通 $p$ 非零，
便能证明这两条实际 Mellin 斜率不同时消失。
本篇尚未证明该非零性。固定有理乘子在原点是单位、两个 theta 行独立、
以及 $R$ 的零除子含非挠点，都不是该右端非零的替代条件。

## 已用来源

- [R51](../results/R51-explicit-theta-section-and-central-square-constant.md)
  的实际 $E_{17}$ 截面。
- [R115](../results/R115-e34-explicit-degree68-theta-section.md)：实际 $E_{34}$ 截面、
  两种微分尺度和完整十七项严格证书。
- [R38](../results/R38-exact-inert-sigma-size-and-jet-budget.md) 开头的普通整 sigma；
  [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md) §4 的
  同一正式群周期、Amice 测度和整个权分支规范；
  [R63](../results/R63-full-euler-cartier-and-fixed-primitive-connection.md)
  的实际 $J_A(0)=0$。
- [R117](../results/R117-e34-nontorsion-theta-divisor.md)：$Q_8$ 的非挠零点。
  本篇的 (3)–(8) 由明确代数公式直接证明。
