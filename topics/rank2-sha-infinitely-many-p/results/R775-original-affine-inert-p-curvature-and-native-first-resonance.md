# R775 — 原仿射三格的完整惰性 p-曲率与实际首次共振

日期：2026-11-15。**状态：以下完整有理算子、原有限来源上的核及原单项式首次共振已证明。**
本篇保 R763、R769、R770 的同一个三坐标来源。所得算子的像有显示的增长次数和分母；它尚未给原有序饱和旗标的改进估值，也未把原中央零传播到新来源。

## 1. 同一个抽象连接

取好惰性素数
\[
p=6s-1>3,\qquad m=3s-1,
\]
剩余域 k 含三次单位根 \(\omega\)，且 \(b\in k^\times\)。
在 \(E_b:y^2=x^3+b\) 上记不变导子
\[
\partial x=2y,\qquad \partial y=3x^2.
\]
在同一个代数微分域 \(k(E_b)(Z,\Sigma)\) 中延拓
\[
\partial Z=-x,\qquad \partial\Sigma=Z\Sigma .
\]
这里 Z、Σ 是原 ζ、σ 的抽象代数坐标；没有将带 p 分母的整个特征零 ζ、σ 级数直接约化。

令
\[
h=x/y,\quad t=-b/x^3,\quad \Theta=x\Sigma^2,\quad Q=1+hZ,\quad
\mathcal E=\Theta\partial_\Theta .
\]
则 \(\mathscr A=h\partial\) 在 \(k(t,\Theta,Q)\) 上准确为
\[
\boxed{\mathscr A=-6t\partial_t+2Q\mathcal E+
 \left(\frac{2t}{1-t}-\frac{1+2t}{1-t}Q\right)\partial_Q.}
\tag{1}
\]
这就是 R770(22) 使用的原未去 Gaussian 抽象连接。

定义完全显示的多项式和有理函数
\[
B_{p,<s}(t)=\sum_{j=0}^{s-1}(-1)^j\binom{m}{j}t^j,\qquad
H_p(t)=1-\frac{B_{p,<s}(t)}{(1-t)^m},
\]
\[
c_p=2(-1)^s\binom{m}{s-1}\in k^\times,\qquad
R_p(t)=c_p\frac{t^s}{(1-t)^{3s}} .
\tag{2}
\]
本篇的 \(H_p(t)\) 是显示的有理势函数，**不是**椭圆曲线的 Hasse 不变量。

**定理 1。** 原连接的完整 restricted p-曲率为
\[
\boxed{\mathscr V_p:=\mathscr A^p-\mathscr A
 =2\bigl(Q^p-H_p(t)\bigr)\mathcal E+R_p(t)\partial_Q.}
\tag{3}
\]
其中 p 次幂是导子的 p 重复合。特别
\[
\mathscr V_p t=0,\quad
\mathscr V_p Q=R_p(t),\quad
\mathscr V_p\Theta=2(Q^p-H_p(t))\Theta .
\]
全部系数已固定，没有一个待选的 p-adic 标量。

## 2. 椭圆基底与两个真实垂直分量

首先 \(\partial^p=0\) 在 \(k(E_b)\) 上。
因为 \(\partial^p\) 仍是平移不变的正则导子，故为 \(a\partial\)，\(a\in k\)。
原 CM 自同构 \((x,y)\mapsto(\omega x,y)\) 给
\(\partial\tau^*=\omega\tau^*\partial\)；
比较 p 次幂便有 \(a\omega=a\omega^p\)。
惰性时 \(\omega^p=\omega^2\ne\omega\)，所以 \(a=0\)。

置
\[
\gamma_p=\partial^{p-1}x.
\]
偶数次导数使它属于 \(k[x]\)，次数不超过
\((p+1)/2=3s<p\)。
它被 \(\partial\) 杀掉，因而作为 x 多项式的导数为零，只能是常数。
加权齐次性给 \(\gamma_p\) 为常数倍的 \(b^s\)。

Bell 多项式的整系数公式给
\[
\partial^p\Sigma/\Sigma=Z^p+\partial^{p-1}Z
 =Z^p-\partial^{p-2}x.
\tag{4}
\]
该恒等式可直接模 p 证明：第 p 个完整 Bell 多项式中，除
\(Z^p\) 与 \(Z^{(p-1)}\) 外的每个分拆项，系数的分子 p! 含 p，
分母的所有阶乘均小于 p，故中间项全消。
同时
\[
\partial^p Z=-\gamma_p .
\tag{5}
\]
因此没有把 ζ 方向或 σ 方向中的任何一个丢掉。

特征 p 的导子重标恒等式为
\[
(h\partial)^p=h^p\partial^p+(h\partial)^{p-1}(h)\partial.
\]
它也可由 Leibniz 展开核定：中间高阶导子系数模 p 消去，余下一阶项为所示系数。
在基底 t 上 \((h\partial)^p t=(h\partial)t\)，而 \(\partial^p t=0\)、
\(\partial t\ne0\)。所以同一个系数必为 h，得
\[
\boxed{\mathscr A^p-\mathscr A=h^p\partial^p}
\tag{6}
\]
在完整扩张上成立。由 (4)–(6)，
\[
\mathscr V_pQ=-\gamma_p h^{p+1},\qquad
\frac{\mathscr V_p\Theta}{\Theta}
 =2\{Q^p-1-h^p\partial^{p-2}x\}.
\tag{7}
\]

## 3. 完整有理势与单位常数

奇数次导数有实际形状
\[
\partial^{p-2}x
 =y\sum_{j=0}^{s-1}a_j b^j x^{3s-2-3j}.
\]
故
\[
h^p\partial^{p-2}x=\frac{B(t)}{(1-t)^{3s-1}},
\qquad \deg B\le s-1.
\tag{8}
\]
原点处 \(x\sim z^{-2}\)、\(y\sim-z^{-3}\)。
\(\partial^{p-2}x\) 的最高 Laurent 系数为
\((-1)^{p-2}(p-1)!=1\) 模 p，且 \(h^p\sim-z^p\)，
所以 \(B(0)=-1\)。

令暂时的势函数 \(H=1+h^p\partial^{p-2}x\)。
因 \(\mathscr A\) 与 \(\mathscr A^p-\mathscr A\) 交换，
在 Θ 上代入 (7) 得
\[
-6tH'(t)=\gamma_p h^{p+1},\qquad
h^{p+1}=\frac{(-1)^s t^s}{b^s(1-t)^{3s}} .
\tag{9}
\]
右边从 \(t^s\) 开始。\(1,\ldots,s-1\) 在 k 中可逆，
故 H 的 \(t,\ldots,t^{s-1}\) 系数为零。
结合 (8)、\(B(0)=-1\)，唯一可能是
\[
B(t)=-B_{p,<s}(t),\qquad H=H_p.
\tag{10}
\]

其首项为
\[
[t^s]H_p=(-1)^s\binom{3s-1}{s}
 =2(-1)^s\binom{3s-1}{s-1}=c_p.
\]
用 \(6s=1\) 模 p 比较 (9) 首项，得到完整常数
\[
\boxed{\gamma_p=-2b^s\binom{3s-1}{s-1}\in k^\times.}
\tag{11}
\]
所有阶乘的指标都小于 p，故单位性没有例外坏集。
将 (11) 代回 (7) 便得 (3)。
直接微分截断二项式也给整条身份
\[
\boxed{-6tH_p'(t)=-R_p(t).}
\tag{12}
\]
以上证明支付全部有理系数，不只其首个 t 系数。

与 R770 的实际 Gaussian 常数相比较，
令 \(c=[z^{p+1}]\log(\sigma/z)\)、\(\gamma=pc\)。
原 \(x=-(\log\sigma)''\) 给
\[
[z^{p-1}]x=-p(p+1)c.
\]
在 R614 已付的整窗口内应用 \(\partial^{p-1}\)，取常数项并用 Wilson 定理，得到
\[
\boxed{\bar\gamma=\gamma_p.}
\tag{13}
\]
所以 (11) 精确匹配原 Gaussian，不是另选一个单位规范。

## 4. 作用于每条原列以及全部来源之和

对任何实际多项式 \(F(t,Q)\) 和整数 \(n\)，由 (3)
\[
\boxed{\mathscr V_p(\Theta^nF)
 =\Theta^n\{2n(Q^p-H_p)F+R_p\partial_QF\}.}
\tag{14}
\]
保持 R769 的原三格，以下取其 \(b=1\) 框。
每个原单项式的完整返回是
\[
S^aT^bU^\nu=\Theta^nF_{a,b,\nu}(t,Q),\qquad
n=17a+36b+102\nu,
\]
\[
K=a+b+5\nu,\quad J=6\nu,\quad L=5a+11b+32\nu,
\qquad \deg_QF\le J,\ \deg_tF\le L.
\tag{15}
\]
此处 b 是第二个单项式指数，曲线常数已固定为1。
原 \(P_4,V_0,B(t,Q)\) 的全部零点及系数均在 \(F_{a,b,\nu}\) 内；
(14) 不将其各 Q 次数拆成可以另选的列。

令
\[
N_p(t)=(1-t)^{3s-1}-B_{p,<s}(t).
\]
清去显示的唯一共同分母后，整个原列准确变成
\[
\boxed{
(1-t)^{3s}\mathscr V_p(\Theta^nF)
=\Theta^n\!\left(
2n\{(1-t)^{3s}Q^p-(1-t)N_p(t)\}F
+c_p t^s\partial_QF\right).
}
\tag{16}
\]
因此实际像的 t 次数至多 \(L+3s\)，Q 次数至多 \(J+p\)，Theta charge 仍为 n。
这个增长成本是公式的一部分，不得将 (16) 当成原格内的免费列变换。

**定理 2。** 若 \(D\ge1,\ p>204D\)，则 (3) 在
原 \(\overline E_D^\partial\) 上的核恰为常数。

先核原来源在这个特征下仍单射。S、T 的比
\(S^{36}/T^{17}=f(t)^{19}/V_0(t)^{17}\) 在 \(t=0\) 有正的19阶零，
所以是非恒定有理函数，S、T代数独立。
而 U 对 Q 是六次非恒定多项式，其最高系数在本 p 范围非零，
所以 S、T、U 仍代数独立。

将任一原来源按真实 Theta charge 写成
\(\sum_n\Theta^nF_n(t,Q)\)。
所有非零 n 满足 \(0<n\le102D<p\)。
若 \(F_n\ne0\)，(14) 的最高 Q 次数是
\(p+\deg_QF_n\)，其系数为原最高系数的 \(2n\) 倍；
另两个项的 Q 次数分别至多 \(\deg_QF_n\) 和 \(\deg_QF_n-1\)，不能抵消它。
不同 n 的项也不能抵消。
所以每个正 charge 块均非零，核只余原常数列。
这是整个原来源的算子结论，没有借一个人为补足的环境列。

## 5. 原单项式的首次共振与算子的匹配

设 \((a,b,\nu)\ne(0,0,0)\)，继续 \(p>204D\)。
原全多项式在 \(t=Q=0\) 的首层满足
\[
F_{a,b,\nu}
=t^K\{f_0+O(t,Q)\},\quad
f_0=(-1)^{a+b+\nu}6^{6\nu},
\]
\[
[t^K]\partial_QF(t,0)=-34\nu f_0 .
\tag{17}
\]
第二式来自原 \(B(t,Q)=34QP_4-6P_4-6tP_4'\)，没有删除 \(P_4\)。
对任一 \(Q_0(t)\in t k[[t]]\)、\(\Theta_0(0)=1\)，
\(Q_0^p\) 从 \(t^p\) 开始，故 (14) 给
\[
[t^{K+s}]\mathscr V_p(\Theta^nF)
 \big|_{\Theta_0,Q_0}
=-2c_p(n+17\nu)f_0.
\tag{18}
\]
这里 \(0<n+17\nu=17a+36b+119\nu\le119D<p\)，所以该首项为单位。
该式针对单条原列；不同列的指定线性组合仍可能相消。

这与实际特征零首次 p 分母完全一致。
按 R770 保原 \(\Theta^\circ,Q^\circ,\chi\) 与 \(\epsilon=w^s/p\)，
整窗口中同一列为
\[
e^{2n\gamma\epsilon}(\Theta^\circ)^n
 F(t,Q^\circ+(p+1)\gamma\chi\epsilon).
\]
在原 \(w^K\) 首项上 \(\chi(0)=-1\)，
一阶 \(\epsilon\) 的两个贡献合为
\(2n\gamma+34\nu\gamma=2\gamma(n+17\nu)\) 模 p。
所以
\[
\boxed{
p[w^{K+s}](S^aT^bU^\nu)
 \equiv2\bar\gamma(n+17\nu)6^{6\nu}\not\equiv0\pmod p.
}
\tag{19}
\]
低于 \(K+s\) 的系数整；(19) 是原未更换单项式的首次简单 p 分母。
完整 \(Q^\circ\) 平移和两位 Gaussian 仍按 R770 保留，
本式没有把下一位误差删除。

## 6. 与真正全旗标门的关系

(3)、(14)、(16) 支付原完整 p-曲率，(19) 核定其与实际 Gaussian 的首次共振。
它们没有给下列未经证明的推论：

- 抽象有理来源上的算子单射，等于每个有序饱和前缀的评价单射；
- 清分母后的像仍在原 \(E_D^\partial\) 内，或其 \(O(p)\) 次数增长免费；
- 可以将特征 p 恒等式先除 p，再忽略 R770 的整个首提升修正；
- 原两个中央零自动使新三格的曲率或首次分母为零。

下一步必须在 (16) 的真实像及同一个共同前缀上支付次数、饱和格和原算术传播。
R760 的严格门仍为同一新格上的 \(a_I+3b_I<6\)，尚未达到。
本篇无数值执行或输出文件；所有式子为原导子的符号推导。

依赖：[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R760](R760-positive-derivative-three-coordinate-grid-and-full-slope-threshold.md)；
[R763](R763-positive-derivative-affine-zeta-model-and-full-gaussian-transport.md)；
[R769](R769-original-confluent-theta-return-for-positive-derivative-grid.md)；
[R770](R770-actual-gaussian-connection-and-complete-first-lift-correction.md)。
