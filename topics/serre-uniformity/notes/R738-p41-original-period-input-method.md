# R738 的原 p41 闭周期输入：精确构造和预运行规范

**预运行方法。** 本次生成的是原 $X_1$ 的带标记有限 Manin cell complex、
整数闭链及交配矩阵，不声称已经算出 CM Hodge 周期、原 $q$、$\beta$ 或高度。
全部正式算术只在公开仓库 Actions 执行；大可复现表只在 artifact，
仓内保留小证书、源、参数与全部 SHA。

## 1. 同一个六层、同一个非分裂 CM 对

取 $S=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$、
$T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$、
$R=ST$，均右作用在左陪集上。固定
$\zeta^2+\zeta+1=0$、$\operatorname{Im}\zeta>0$。

Brau–Jones 的完整图式
$H_6=\{(\vartheta(g),g):g\in\operatorname{GL}_2(\mathbb F_3)\}$
采用以下准确商同态：
$$
\vartheta(S_3)=I,\quad
\vartheta(T_3)=C=
\begin{pmatrix}0&1\\1&1\end{pmatrix},\quad
\vartheta(\operatorname{diag}(1,-1))=T_2.
$$
其核是 $Q_8$。一种不依赖群名称的完整标签是：
在 $\mathbb P^1(\mathbb F_3)=\{\infty,0,1,2\}$ 的三种无序二二分割
$$
\{\infty,0\}|\{1,2\},\quad
\{\infty,1\}|\{0,2\},\quad
\{\infty,2\}|\{0,1\}
$$
上作用，并依次标成 $\mathbb P^1(\mathbb F_2)$ 的
$\infty,0,1$。这给上述三张矩阵。
程序生成全部 $48$ 项并逐对核群同态恒等式，记录真实 $Q_8$ 核；
不将两个模 $2/3$ 稳定子自行相乘。

在行列式一复分量中，一个六层陪集由
$$
k=\vartheta(g_3)^{-1}g_2\in\operatorname{GL}_2(\mathbb F_2)
$$
表示，恰有六个。故右作用准确为
$$
kS=kS_2,\qquad kT=C^{-1}kT_2,\qquad
kR=C^{-1}kC.
$$

$p=41$ 因子使用原
$T_\zeta=\{\left(\begin{smallmatrix}a&-b\\b&a+b\end{smallmatrix}\right)\}$
所稳定的对 $\{\zeta,\zeta^2\}$。
左陪集 $N_{\rm ns}g$ 标成
$g^{-1}\{\zeta,\zeta^2\}$。在
$\mathbb F_{41^2}=\mathbb F_{41}[\zeta]$ 中，共轭为
$$
a+b\zeta\longmapsto (a-b)-b\zeta.
$$
取每个非实共轭对的字典序较小者，共
$41(41-1)/2=820$ 个。右 $S,T$ 因而分别为
$$
z\longmapsto-1/z,\qquad z\longmapsto z-1,
$$
不能把 $g^{-1}$ 忘掉而使用相反的平移。

两个因子的直积给原复曲线的 $4920$ 个陪集。
程序从 $(I,\{\zeta,\zeta^2\})$ 出发，用右 $S,T$ 完整 BFS，
同时保存模 $246$ 的矩阵。对每个陪集重新代入
$\vartheta(g_3)^{-1}g_2$ 和 $g^{-1}\{\zeta,\zeta^2\}$ 核标签。
然后构造同余于该矩阵的准确 $\operatorname{SL}_2(\mathbb Z)$ 提升；
每个提升的行列式一和完整模 $246$ 同余都逐项验证。
所以每条后续 Manin 边都有实际有理端点，未用未知的抽象代表。

## 2. 原 c0/c1、完整反线性下降与周期相位

复曲线是 R575 的同一
$$
X_1=\operatorname{Norm}
 (X_{\rm ns}^+(41)\times_j\mathbb P^1_a),
\qquad j=6912a^3(1-a^3),
$$
经原 $u=a/\sqrt[3]4$ 与规范六层识别。
**BFS 的参考陪集 $k=I$ 并不是原实点 $a=1$。**
必须先按该图式计算真实复共轭，不能仅宣布给参考陪集赋予 $a=1$。

令
$$
M=\begin{pmatrix}-1&-1\\0&1\end{pmatrix},\qquad
M\bar\zeta=\zeta.
$$
在同一个周期基 $(\zeta,1)$ 上，复共轭的列矩阵为 $M^{\mathsf t}$。
陪集 $Hg$ 对应的实际 level 基由 $g^{\mathsf t}$ 给出，
所以共轭后的基为
$M^{\mathsf t}g^{\mathsf t}=(gM)^{\mathsf t}$：
**作用于 CM 陪集的是右乘 $M$**。
它也将 $R$ 轨道送到 $R$ 逆向轨道，故是同一粗 CM 纤维上的反线性下降。

因为 $M=-\operatorname{diag}(1,-1)T$，有
$$
\vartheta(M_3)=T_2 C,\qquad M_2=T_2.
$$
于是 tame 共轭准确为
$$
k\longmapsto (T_2C)^{-1}kT_2.
$$
三个 $R$ 固定标签是 $k=C^a$，$a\in\mathbb Z/3$；
此时该式化为 $a\mapsto-1-a$。
唯一固定标签是 $a=1$，即 **$k=C$**。
在 $p$ 处，$M$ 交换 $\zeta,\zeta^2$，所以保留同一个原 CM 项链。
因此真正的原实 $c_1$ 为
$$
(C,\{\zeta,\zeta^2\}).
$$
它有以下明确整矩阵代表：
$$
g_*=
\begin{pmatrix}15130&123\\123&1\end{pmatrix},
\qquad \det g_*=1,\quad
g_*\equiv I\pmod{123},\quad g_*\equiv C\pmod2.
$$
所以原点在该解析商中的准确代表是 $g_*\zeta$。
$g_*$ 的标签、全部反线性矩阵和置换都在程序中实际验证与保存。
BFS 得到的另一整代表只是同一左陪集的等价代表。

$j=0$ 上三个非分歧点的 $a$ 值为 $1,\zeta,\zeta^2$；
其中仅 $a=1$ 为实点。以上唯一实标签因而与
$u=1/\sqrt[3]4$、正实 $\sqrt[3]4$ 所定义的原 $c_1$ 精确相容，
不再有一个待猜的三次相位。

矩阵 $T^{82}$ 在模 $41$ 为恒等，在 tame 部分为
$k\mapsto C^{-1}k$。由原 cusp 主项 $u(\tau)\sim c q^{-1/6}$
或 R575 的准确 deck 计算，它是
$\delta_\zeta:a\mapsto\zeta a$。
因此实际标签依次为
$$
C\ (a=1)\ \longmapsto\ I\ (a=\zeta)\
\longmapsto\ C^2\ (a=\zeta^2).
$$

另取 $k=S_2$、同一个原 $p$-对 $\{\zeta,\zeta^2\}$。
其三元素 $R$ 轨道给 $a=0$ 的原 $c_0$，分歧指数为三；
$\delta_\zeta$ 和真实复共轭都保持这一轨道。
三元素表示的是同一个粗点，不能当三个不同的 CM 点。
该标签完整保存，以便后续在同一 $q[c_1-c_0]$ 上求值。
没有将 $c_0$ 的秩零条件移到 $c_1$。

## 3. 预期拓扑数与完整检查

tame $S$ 无固定点，所以完整 $S$ 无固定点。
tame $R:k\mapsto C^{-1}kC$ 有三个固定点。
在 $p$ 因子中，$Rz=-1/z-1$ 固定非实共轭对恰为
$\{\zeta,\zeta^2\}$：若 $Rz=z$，则 $z^2+z+1=0$；
若 $Rz=\bar z$，乘 $z$ 后迫 $-1-z=N(z)\in\mathbb F_p$，矛盾。
故完整 $R$ 有三个固定点。

tame $T$ 为一个六循环；在 $p$ 因子上，平移 $z\mapsto z-1$
的每个非实对轨道都恰长 $41$。两者互素，完整 $T$ 因而给
$20$ 个宽 $246$ 的尖点。于是
$$
g(X_1)=1+\frac{4920}{12}-\frac3{3}-\frac{20}{2}=400.
$$
程序仍从完整实际置换计算全部轨道，而非只写入预测数；
检查 $S^2=R^3=1$、transitivity、所有尖点宽及 Euler 等式。

## 4. 两棵树给整数相对基和闭基

对每个 $S$ 二轨道选较小陪集 $h$ 为正向，边是
$\{g_h0,g_h\infty\}$，反向是 $hS$。
$2460$ 条边连接其两端的 $R$ 轨道；共有 $1642$ 个这样的顶点。
这是 Farey 三角剖分的对偶图：
正向对偶边从该 Manin 边左边三角形通向右边三角形。

Manin 的 $R$ 三项关系恰为这些顶点的整 coboundaries。
在固定 $R$ 顶点，原关系为 $3e=0$；普通曲面的相对 $H_1$
无挠，饱和后是 $e=0$，准确对应对偶图的叶顶点。
选一棵 $1641$ 边生成树，沿树作系数为 $\pm1$ 的整消元后，
其余 $819$ 条原 Manin 边即为
$H_1(X_1,\mathrm{cusps};\mathbb Z)$ 的整数基。
这是图 incidence 的全单模消元，没有用仅有理的秩代替整饱和。

在这个基下，边界准确为
$$
\partial\{g0,g\infty\}=[g\infty]-[g0],
$$
即陪集 $h$ 的 $T$ 轨道减去 $hS$ 的 $T$ 轨道。
因此 $819$ 列边界又是 $20$ 个尖点构成的一张连通图的 incidence。
选第二棵 $19$ 边生成树，每条非树边加上反向树路径，
便得到 $800$ 条整数闭链；每条边界实际检查为零。
这些闭链在余下 $800$ 条主边上的系数是单位矩阵，
故确为整个整数核的一组基，未漏一个有限指数。

## 5. 原定向交配矩阵

收缩第一棵树，再沿第二棵树合并 $20$ 个 cusp 面，
得到一个顶点、一个面和 $800$ 条边的闭曲面胞腔分解。
唯一面的有向边界长 $1600$，每个边标签恰出现一次正、一次负。
面定向使用正 cusp 环 $T$：在 $q=e^{2\pi i\tau/w}$ 下，
$\tau\mapsto\tau+w$ 是正向绕 cusp 的环。

前节闭链的 Poincaré dual 在剩余主边上分别取标准坐标值。
把每个面三角化，并在线性原函数上积分，得同一交配的准确公式
$$
2\langle\gamma_i,\gamma_j\rangle
 =\sum_{\ell}
  \bigl(A_i(\ell)\,a_j(\ell)
       -A_j(\ell)\,a_i(\ell)\bigr),
$$
其中 $a_i(\ell)$ 是第 $\ell$ 条有向边上的 $i$ 坐标，
$A_i(\ell)$ 是此前各边该坐标的累积和。
这就是每个小三角形上
$2\int dF_i\wedge dF_j$ 的行列式，不靠数值交点图形判断。

程序检查分子全部为偶数、矩阵反对称及准确行列式为一。
这三项连同两树整数构造给原闭基的完整整数交配证书。
矩阵与闭链的共同顺序一并存入 artifact；后续可对同一矩阵做辛基变换，
不得另换一个未经标记的周期基。

## 6. 执行输出与剩余真实输入

完整输出包括每条陪集的两个有限标签、整矩阵提升、三个生成元置换、
全部尖点、原 $c_0/c_1$ 和 deck 标签、两棵树、整数闭链、
闭 polygon 与 $800\times800$ 交配矩阵。

本次尚不输出 R732 的 $V$ 有理 Hodge 基、有限 adelic translate 表、
CM 代数周期矩阵或映射函数。特别是六层图式、完整 determinant
分量及 $a=\sqrt[3]4\,u$ 的原正扭曲仍须在 Hodge 表中准确运输；
这份拓扑表不能将一个标准 $\Gamma_0(9p^2)$ 或
$\Gamma_1(108p^2)$ 的 newform 自动变成原 $q$ 的微分。

来源：

- Brau–Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*，
  [作者原稿](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf)，
  原 $Q_8$ 商图式与六层模型。
- William Stein, *Modular Forms: A Computational Approach*，
  [General Modular Symbols](https://wstein.org/books/modform/modform/modular_symbols.html)，
  任意有限指数群的 Manin 整生成元、$S/R$ 关系及普通相对同调；
  此处图消元和交配公式已写明。
- [R575](../results/R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)：
  实际 deck、完整六层、原 $\kappa_4$ 方向。
- [R616](../results/R616-original-CM-point-difference-and-explicit-height-basis.md)：
  原两个 CM 点及同一点差。
- [R732](../results/R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)：
  这些实际闭链、交配和矩阵代表的后续使用范围。
