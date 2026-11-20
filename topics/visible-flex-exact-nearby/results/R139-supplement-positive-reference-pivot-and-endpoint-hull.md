# W2C reference：同一指数的凸组合 pivot 与真实 endpoint hull

2026-11-20，`visible-exact-astra-ac637-20261120`。纯解析包含证明；本地科学计算为0。

## 原失败与修改边界

公共 continuation `44719196440/1` 仍在完整153 parent / 155 panel 准备后、首条新标量之前失败。失败位置为 `profiles.at -> _segment(elapsed,p)` 的严格正 `complete scaled impedance pivot` 检查。原零端点表示问题已经通过；这次是同一指数在分式公式中反复出现的依赖损失。原失败与0条新标量记录均保留。

本补丁保留前版的真实几何非负长度修复，也保留所有严格正 panel、speed、impedance、frequency 和 pivot 检查。它用已证明的同函数范围与原有向球相交；不把负球端点改称为正数。

## 一、正 pivot 是同一指数的凸组合

固定任一真实参考系数和任一合法长度，写

\[
\omega=\sqrt{a^2+c^2q^2}>0,\quad
z=e^{-\omega h},\quad e=z^2\in[0,1],
\quad A=(1+e)/2,\quad B=(1-e)/(2\omega).
\]

原 pivot 是

\[
D=A+B(a+cp)
=e+(1-e)d,\qquad
d=\frac{\omega+a+cp}{2\omega}.
\tag{P1}
\]

由于 `c>0`、`p>0`、`q>0`，有 `omega>=|a|`，从而

\[
d\ge\frac{cp}{2\omega}
\ge\frac{c_{\rm lo}p_{\rm lo}}{2\omega_{\rm hi}}>0.
\tag{P2}
\]

这里每个 lo/hi 都是已经有向包围同一真实量的端点。即使 `p` 与长度相关，也逐个真实取值成立，无须把两者宣布独立。

令 `[d_lo,d_hi]` 包含 `d`，其中 `d_lo` 取原 `d` 球下端与(P2)有向下端的最大值；令 `[e_lo,e_hi]` 为原指数球与 `[0,1]` 的交集端点。函数 `e+(1-e)d` 对 `d` 非减，固定 `d` 后对 `e` 仿射。因此其完整矩形界为

\[
\begin{aligned}
D_{\rm lo}&=e_-+(1-e_-)d_{\rm lo},&
e_-&=\begin{cases}e_{\rm lo},&d_{\rm lo}\le1,\\e_{\rm hi},&d_{\rm lo}>1,\end{cases}\\
D_{\rm hi}&=e_++(1-e_+)d_{\rm hi},&
e_+&=\begin{cases}e_{\rm lo},&d_{\rm hi}\ge1,\\e_{\rm hi},&d_{\rm hi}<1.\end{cases}
\end{aligned}
\tag{P3}
\]

有向计算分别取(P3)下、上端，核验 `0<D_lo<=D_hi`。把原 `A+B*(a+c*p)` 球与此区间相交，仍包含全部真实 pivot。随后**原来的正 pivot 下端检查仍必须通过**才允许除法。这个界至少保留凸组合的严格正性；当指数已有更窄范围时，还利用其实际端点。

## 二、B 的零端点

由同样的正频率与指数范围，

\[
\frac{1-e_{\rm hi}}{2\omega_{\rm hi}}
\le B\le
\frac{1-e_{\rm lo}}{2\omega_{\rm lo}}.
\tag{P4}
\]

两端非负，且覆盖全部相关的真实指数/频率取值。代码先向外计算(P4)，再沿前版已经证明的对称球平移法表示其非负 hull。没有把一个真正负的 B 取绝对值。

## 三、p 的同 panel endpoint hull

在一个常系数 reference cell 中，真实阻抗满足自治标量 Riccati 方程

\[
p'=2ap+cp^2-cq^2.
\tag{P5}
\]

右端为局部 Lipschitz 多项式。一个非常数解若在内部达到平衡值，常数解与其在该点有同一初值，由唯一性两者必须相同，矛盾。因此非常数解的导数不变号，整个 cell 上单调；平衡解则恒定。零速 collar 的 `a=c=0` 情况也是恒定。

对每个固定真实参考参数，任一内部点的 `p` 都在同 cell 两个真实端点值之间。先作这一逐参数论证，再取已经保存的两端完整有向包络的凸包，得到整个参数/真实根域统一有效的内部界。`at` 把原内部 `p` 球与此 hull 相交后再送入第二次 `elapsed,p` 计算。它不以区间中点或两个上界代替真函数，也没有另算旧 norm 目标。

## 保持的对象

固定 WVC reference/diagonal chain、同一根、同一参数域、真实 eta、S、193 mean 与全部 atoms、原 cutoff、primitive 和所有独立 ports 均不变。只收紧新私有函数球中的依赖外包，不改变任何已成科学记录。完整 L 的三条记录仍须在公共 Actions 首次完成；本证明不预判 R139、有限逆或几何完成条件。
