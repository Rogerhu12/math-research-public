# R249 — 三原来源的固定导子与完整角向块

日期：2026-11-13。**状态：在真实三源代数中，以固定次数二十二的导子支付，可以整地实现归一化的全部角向块。固定坏集、原次数、原点阶、Euler 质量及原第一带矩阵均保留。尚未由此完成加权像的净 Smith 估计或中央非零。**

这一步使用 R244 已证明的实际三源曲线，而不是把某个有限扩张免费当作原来源。其效果是在原有限次数源中构造一个明确的、只损失线性维数的完整子格。

## 1. 真实源环及其归一化

R243/R244 已给
$$
(A,B,H)=\rho\,(a(t),b(t),h(t)),
\qquad \rho=5w+O(w^2),\quad t=1-\tfrac12w+O(w^2),
\tag{1}
$$
其中 $a,b$ 次数二十三，$h$ 次数二十四；三者同时齐次化为二十四次二元形式后无共同基点。射影像
$$
C:\Phi(A,B,H)=0\subset\mathbf P^2
$$
是次数二十四的几何整有理曲线，且 $\mathbf P^1\to C$ 是归一化。
原点对应 $t=1$、$O=[1:1:1]$，该点光滑。

令实际齐次源代数
$$
\mathcal A=\mathbf Q[A,B,H]/(\Phi),\qquad \deg A=\deg B=\deg H=1.
$$
把 $t=T/V$，并用 (1) 的同一二十四次齐次参数化，便得到
$$
\boxed{
\mathcal A\subset
\mathcal B:=\bigoplus_{m\ge0}H^0(\mathbf P^1,\mathcal O(24m))
=\mathbf Q[T,V]^{(24)}.}
\tag{2}
$$
这里 $\mathcal B_m$ 维数为 $24m+1$，其在原函数域中的元素是
$\rho^m q(t)$、$\deg q\le24m$。

$\mathcal B$ 确实是 $\mathcal A$ 的整闭包。两者的分式域相同，
因为 R244 的射影参数化双有理且两个环的次数群都是 $\mathbf Z$。
$\mathcal B$ 是正常的 Veronese 环；无共同基点使其在 $\mathcal A$
上有限。例如，三个二十四次形式生成的理想在 $\mathbf Q[T,V]$
中的零集只有原点，故该二元多项式环、以及其 Veronese 子环，都有限于
由这三个形式生成的子环。这给 (2) 的有限整性，而非仅给函数域有限扩张。

另一个在这里有用的精确事实是
$$
\mathcal A_m=H^0(C,\mathcal O_C(m))\qquad(m\ge0).
\tag{3}
$$
由
$0\to\mathcal O_{\mathbf P^2}(m-24)\to
\mathcal O_{\mathbf P^2}(m)\to\mathcal O_C(m)\to0$
及 $\mathbf P^2$ 上 $H^1(\mathcal O(n))=0$，即可证明 (3)。
所以后面得到的全局截面确实能由原次数为 $m$ 的三元多项式代表。

## 2. 固定次数二十二足够支付导子

记 $\nu:\mathbf P^1\to C$，导子理想为
$$
\mathfrak c=\operatorname{Ann}_{\mathcal O_C}
                 (\nu_*\mathcal O_{\mathbf P^1}/\mathcal O_C).
$$
由于平面曲线为 Gorenstein，导子在归一化上是
$\mathcal O_{\mathbf P^1}(-\mathfrak D)$，其中
$$
\deg\mathfrak D=2(p_a(C)-g(C))
=2\cdot\frac{23\cdot22}{2}=506.
\tag{4}
$$
这里使用的标准导子/伴随定理及其“所有次数的完整线性系”形式，可见
Böhm–Decker–Laplagne–Pfister,
[Local to Global Algorithms for the Gorenstein Adjoint Ideal of a Curve](https://arxiv.org/abs/1505.05040)，
2015 年预印本（2017 年发表于 Springer 编集 *Algorithmic and Experimental Methods in Algebra, Geometry, and Number Theory*），§3，Remark 3.10、Theorem 3.11。其输入恰为本篇已认定的平面整曲线和归一化，不需要猜测奇点类型。

因为 $\nu^*\mathcal O_C(1)=\mathcal O_{\mathbf P^1}(24)$，
$$
H^0(C,\mathfrak c(22))
=H^0(\mathbf P^1,\mathcal O(528)(-\mathfrak D))
\simeq H^0(\mathbf P^1,\mathcal O(22)).
\tag{5}
$$
这是维数二十三的有理向量空间。$O$ 光滑，故 $t=1$ 不在
$\mathfrak D$ 的支撑里；右侧残余线性系无基点。因此可以固定选取
$$
c\in\mathcal A_{22}\cap\mathfrak c,\qquad
c(\rho,t)=\rho^{22}c_0(t),\qquad c_0(1)\ne0.
\tag{6}
$$
选择可以在 $\mathbf Q$ 上完成：评价到这个有理光滑点是非零的
$\mathbf Q$ 线性映射，取其非零有理原像即可。

导子的定义与 (3) 随即给出整个 graded 包含
$$
\boxed{c\,\mathcal B_m\subset\mathcal A_{m+22}
       \quad\text{对全部 }m\ge0.}
\tag{7}
$$
这不是“对足够大 $m$”才成立的未量化陈述；次数二十二已经支付
了固定导子，(7) 对每个非负整数 $m$ 成立。

若只需要一个更直接、次数二十三的选择，也可用在 $O$ 不为零的
Jacobian 偏导。原参数的一阶法向量准确为
$(207,-691,484)$，所以 $\Phi_H(O)\ne0$；平面 Jacobian 理想包含在导子中。
本篇采用更小的 (6)，并不需要展开次数二十四的巨大隐式方程。

该 Jacobian 包含也可直接从同一伴随公式看出：在每条归一化分支的
参数 $\tau$ 上，若导子指数为 $c_\tau$，则平面 dualizing 微分
$dx/f_y$ 的阶为 $-c_\tau$。因此
$v_\tau(f_y)=c_\tau+v_\tau(dx/d\tau)\ge c_\tau$；交换坐标处理
$f_x$，再逐支应用导子判据即可。特征零允许选择非恒定的投影坐标。

这个非零值是去公共因子后的**角向**值。实际函数仍是
$$
\Phi_H(A(w),B(w),H(w))
=\rho(w)^{23}\Phi_H(a(t(w)),b(t(w)),h(t(w))).
$$
它在原点恰二十三阶，中心质量为零；不能因射影值非零便称这个实际
函数为 Mellin 单位。(6) 的实际函数同理恰二十二阶。两种选择都
保留原 $\rho=\Theta\,g/(2-t^2)^{17}$，没有把原 $F/\Theta$ 或其二次
角因子从来源中除去。

## 3. 一个固定坏集同时支付所有次数的整数性

以上并不自动给原整数源；这一节补出统一的整数化。

所有参数化系数、$c$、有限整性方程都在 $\mathbf Q$ 上。
可取一个固定正整数 $M$，并置
$$
\mathcal R=\mathbf Z[1/M],
$$
使得：

1. $\mathcal A_{\mathcal R}$、$\mathcal B_{\mathcal R}
=\mathcal R[T,V]^{(24)}$ 具有 (2) 的同一有限 graded 包含；
2. $c\mathcal B_{\mathcal R}\subset\mathcal A_{\mathcal R}$；
3. $c_0(1)$、$2$、$5$ 为 $\mathcal R$ 单位；
4. $\mathcal A_{\mathcal R}/c\mathcal B_{\mathcal R}$ 在 $\mathcal R$ 上无扭。

这些要求只删去固定有限多个素数，完全不依赖 $m$ 或目标前缀。
证明如下。先给 $\mathcal B$ 的有限多个环生成元选择整性方程，
清除其有限系数分母，即得一个有限 $\mathcal A_{\mathcal R}$ 模。
再选有限 graded 模生成元 $b_i$，并为有限多个 $cb_i$ 选择原多项式
代表，清除这些分母，便得到第二条。最后上述商是 Noetherian
$\mathcal A_{\mathcal R}$ 模；其 $\mathbf Z$ 扭子模有限生成，每个生成元
被一个非零整数消去。再倒入它们的乘积即可得到第四条。

因此，对每个 $p\nmid M$，(7) 在同一个原 $O=\mathbf Z_p$ 源中成立，
且每个有限 graded 截断的子格
$c\mathcal B_{\le d-22}\subset\mathcal A_{\le d}$
是 primitive 的。这里没有把每个 $m$ 分别出现的新分母省略掉。

还有一个可用于高度预算的统一形式。可为下节各列选择原齐次多项式
代表，使其分母至多为 $M^{C(m+1)}$、系数 $\ell^1$ 范数至多为
$C^{m+1}$，其中 $C$ 是与 $m,p$ 无关的固定常数。
确实，乘以 $\mathcal B_1$ 的二十五个固定二元单项式，在上述有限
graded $\mathcal A$ 模上由有限个固定多项式矩阵实现；对其范数取共同
上界，迭代 $m$ 次，再乘固定 $cb_i$ 的代表即可。
因而这一步的来源高度是线性于次数的成本，不是未支付的任意有理函数高度。

## 4. 原有限次数源中的完整角向列

把固定有理数归一，令
$$
R=\rho/5=w+O(w^2),\qquad q=-2(t-1)=w+O(w^2),
$$
$$
C_0=R^{22}\frac{c_0(t)}{c_0(1)}
      =w^{22}+O(w^{23}).
\tag{8}
$$
在扩大一次固定 $M$ 后，以下全部函数属于原整源：
$$
\boxed{
\Omega_{m,j}:=C_0R^m q^j
\in\mathcal A_{m+22}\otimes O,\qquad
0\le j\le24m,\quad m\ge0.}
\tag{9}
$$
因为 $R^mq^j$ 对应 $\mathcal B_m$ 中的二十四次 Veronese 单项式，
(9) 正是 (7)，不是独立添加了一个归一化变量。

每列有准确首部
$$
\Omega_{m,j}=w^{m+22+j}+\cdots .
\tag{10}
$$
所以它在原 $p$ 整源中 primitive，且固定 $m$ 下的
$24m+1$ 列具有完整连续的首角权
$$
m+22,\ m+23,\ldots,\ 25m+22.
\tag{11}
$$
同一 $m$ 下从这些列到对应角向 jet 的矩阵为单位下三角，
没有一个依赖 $m$ 的未知 minor 因子。不同 $m$ 的列由 graded 源
本身分开，其全部线性独立性也来自 (2)、(7)，不以角向首项互异为理由。

对原总次数界 $D\ge22$，这个真实子格的秩为
$$
\boxed{
\sum_{m=0}^{D-22}(24m+1)
=12(D-22)^2+13(D-22)+1
=12D^2-515D+5523.}
\tag{12}
$$
R244 的完整原源秩为 $12D^2-240D+1772$（$D\ge24$），
所以 (9) 仅损失 $275D-3751$ 个维数。其二次主项是完整原源的同一个
$12D^2$，这是实际子格的维数，不是从函数域扩张次数直接猜出的预算。

## 5. 原 J 和 Euler 质量没有更换

对 (9)，原三源 Euler 算子
$$
\mathcal E=A\partial_A+B\partial_B+H\partial_H
$$
准确满足
$$
\boxed{\mathcal E\Omega_{m,j}=(m+22)\Omega_{m,j}.}
\tag{13}
$$
因此原底层 charge 是 $17(m+22)$，不是 $17m$。
式 (8) 的 $C_0$ 在原点恰二十二阶，不能把它当 Mellin 单位删掉。

在 R199 的真实第一带中，令 $b=17u_0$、$a=pb$，
$R_p=r(p-1)$。原共同整轴上的 (9) 记为
$g_{m,j}(w)$；它仍以 $w^{m+22+j}$ 为首项一。
沿同一个实际曲线，准确有
$$
\Omega_{m,j}(w)
=e^{b(m+22)w^r}g_{m,j}(w)\pmod{w^{R_p+1}}.
$$
故对 $rh+l\le R_p$、$0\le l<r$，
$$
\boxed{
J_{rh+l}(\Omega_{m,j})
=\sum_{i=0}^h
 p^{h-i}\frac{a^i}{i!}(m+22)^i
 [w^{l+r(h-i)}]g_{m,j}(w).}
\tag{14}
$$
这就是同一原有限目标上的完整列，包括所有尾系数。

这里整轴的 $R,q,C_0$ 也确实整：可由 $A/a(t)$ 取得 $\rho$；
在 $t=1$，$a(1)=1/5$ 是单位。R244 的 $B/A$ 在该点的参数导数为
$44$，故排除固定素数 $11$ 后，原整比值轴通过整逆函数恢复同一个
$t$，再得到 (8)。这些操作只证明固定原函数的轴系数整，
没有在有限次数来源中免费加入比值。

式 (14) 可用于重新计算完整连续像、同一 Schur 核或 Smith 长度。
仅凭 (12) 并不能跳过这个计算：不同质量列仍可能在同一目标行相消，
原 $J$ 的饱和损失仍须支付。本文已经支付的是源代数到完整角向块的
固定导子成本；尚未支付的是把中央全零强迫转成这些原像列上的新深度。

## 6. 固定 overhead 没有自行改掉“惰性四、复侧二”的主系数

这一节比较同一个已支付来源的真实 jump，不能把维数增加直接计成
Smith 收益。用 (9) 中 $m\le D-22$ 的全部列构成自由源
$\mathcal F_D$，其秩记为 $n_D$，真正增加有理秩的阶数记为
$$
0\le k_1<\cdots<k_{n_D}=K_D,\qquad S_D=\sum_i k_i.
$$
它们不必以零开始，因为所有导子列的原点阶至少二十二。

首先有
$$
n_D=12D^2+O(D),\qquad K_D=O(D^2),\qquad S_D=\Theta(D^4).
\tag{15}
$$
第一式是 (12)。下界用 $k_i\ge i-1$。上界可直接支付 R244 的
原 resultant 出口：任意非零 $P\in\mathcal A_{\le D}$ 给一个非零
旧两源多项式 $Q=\operatorname{Res}_H(\Phi,P)$，次数至多 $24D$。
整 Bezout 式在原曲线上是 $Q=W P$，其中 $W$ 是原多项式函数，
所以 $\operatorname{ord}_wQ\ge\operatorname{ord}_wP$。
R191/R217 的旧源接触界遂给
$K_D\le(576+o(1))D^2$。这里常数不是优化目标；它足以严格给出
$$
\sum_i k_i\log k_i=2(\log D)S_D+O(D^4).
\tag{16}
$$
同样结论也适用于 R244 的完整原三源，而非只适用于 $\mathcal F_D$。

**复侧。** 三条实际来源都是同一 $w=z^4$ 参数下有限型增长阶
$1/2$ 的整函数。第 3 节的来源代表具有 $O(D)$ 对数高度，所以
R159 的同一 Cauchy 计算给
$$
\log\|\varphi_D^{k_i}\|_\infty
\le-2k_i\log(k_i/D)+O(k_i+D).
$$
累计并用 (16)，得到
$$
\boxed{
\sum_i\log\|\varphi_D^{k_i}\|_\infty
\le-2S_D\log D+O(D^4).}
\tag{17}
$$
此处所有函数仍是原次数至多 $D$ 的全局整 theta 多项式，不能把
独立的 $R$ 或 $q$ 当作全局整函数来应用 Cauchy。来源系数范数的
固定指数成本累计为 $O(Dn_D)=O(D^3)$，不改变 (17) 的主项。

**惰性侧。** R173/R215 的同一全深权
$$
e_{p,k}=
\begin{cases}
0,&\lfloor k/r\rfloor=0,\\
\lfloor k/r\rfloor+
 \left\lfloor\dfrac{\lfloor k/r\rfloor-1}{p-1}\right\rfloor,
 &\lfloor k/r\rfloor\ge1
\end{cases}
$$
也支付实际第三来源。确实在原平面中
$H=a^{17}s\sqrt{1-s}Q_{15}(s)$、$s=b/a$，$a(0)=1$。
该加权整级数环对逆和乘法封闭；$\sqrt{1-s}$ 由首项一及
$2\in O^\times$ 的 Hensel 递推取得同样权界。因而原 $H$，以及
全部实际原多项式列，仍有相同 $e$ 包络。R215 的原 $w$ 运输也不变。

除去第 3 节的固定坏集，原饱和 jump 遂满足
$\|\varphi_D^{k_i}\|_p\le p^{e_{p,k_i}}$。
R173/R217 的模四素数和是
$$
\sum_{p\equiv3\ (4)}e_{p,k}\log p
=2k\log k+O(k).
$$
因此未经任何新增真实 Smith 改善的包络累计仍是
$$
\boxed{
\sum_i\sum_{p\equiv3\ (4)}e_{p,k_i}\log p
=4S_D\log D+O(D^4).}
\tag{18}
$$
普通位的原整图形可同样加入首项一的平方根，所以真正 jet 成本仍
非正；固定坏集以及固定导子的分母只增加 $O(S_D+Dn_D)=O(D^4)$。

于是固定次数二十二（或二十三）的 overhead 不改变本预算的主系数：
$$
\boxed{\text{原无条件惰性包络为 }4S_D\log D,\quad
\text{复侧负项为 }-2S_D\log D.}
\tag{19}
$$
$12D^2$ 的源维数主项会改变 $S_D$ 的常数，却同时乘到这两侧，
不会单独把四变成小于二。$D$ 换成 $D+22$ 只改变低阶项。
因此仍须在同一个真实 jump 矩阵中证明超过
$(2+\varepsilon)S_D\log D$ 的真实累计 Smith 改善，或直接取得某个
固定精度的无穷素数非零证书。本文没有将完整角带的存在当作该改善。

作为同一结论的有限精度核对，在有正分母成本的支持
$p\le4K_D-1$ 上，每个模 $p^N$ 可见的真实 jump 缺损至多 $Nn_D$，
故其加权总量至多 $O(ND^4)$。固定三权或四权不会因为 (12) 的
维数系数变大而自动取得 $D^4\log D$ 主项；这与 R217 完全相容。

依赖：R243 的实际三截面与共同参数；R244 的次数二十四有理曲线、
光滑原点、真实源代数及 Hilbert 函数；R199 的同一原第一带矩阵。
标准平面导子定理的原始技术接口见第 2 节所引论文 §3。
本篇没有扫描目标素数，也没有去掉原 carrier 后把结果当作 Mellin 商。

