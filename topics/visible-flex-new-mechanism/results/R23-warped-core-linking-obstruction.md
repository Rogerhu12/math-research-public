# R23：ψ-warp 准确核心与平圆领的 linking 障碍

日期：2026-11-14。状态：以下是完整的拓扑与显式符号证明；已由 `literature` 和 `repo_sources` 两个独立工作分支核对法向架、绕数和环带同位链。没有执行新的几何扫描。

## 1. 结论及适用范围

设 R12 准确核心的中心曲线 \(c\) 是嵌入闭曲线，其水平投影 \(c_W\) 为**正则 Jordan 曲线**。取

\[
\chi=3\phi,\qquad
d_W=e^{i\psi(\phi)}(-\sin\chi+i\eta\cos\chi),
\quad d_z=-\sigma\cos\chi,\quad
\sigma=\sqrt{1-\eta^2}>0,
\]

\[
c_\phi=b\,d\times d_\phi,\qquad b>0.
\tag{1}
\]

这里 \(\psi(\phi+2\pi)=\psi(\phi)+2\pi\)，允许 R12 的两个控制或公开 controls 模块的多个高模；本结论另要求所取参数下 \(c_W\) 正则且为 Jordan。准确核心为 \(X(s,\phi)=c(\phi)+s\,d(\phi)\)。

**定理。** 只要核心在某个非零宽度上是嵌入环带，它的两条同向平行截圈具有 linking number \(+3\)，按反向约定则为 \(-3\)，尤其不是零。因此，包含这个核心的**同一个嵌入环带**不可能延伸到一个开放平面圆领。该核心也不可能包含在一个嵌入二球面中。

实际公开 Actions 已认证的 \(u=.8,v=0,b=1\) 和 \(u=1,v=0,b=1\) 两个基准，其水平投影正则且为 Jordan，宽度 \(w=.05\) 的准确核心也已由 R14 法向条带证书证明嵌入，因此满足上述假设。

这个结论：

- 不否定核心本身的精确度量、宏观投影位移或条带嵌入证书；
- 不否定允许自交的浸入拼接；
- 不否定其他 framing 为零的准确核心，或其他有限等距机制；
- 不从“高模控制很小”或“方向参数正则”推导全参数路径嵌入。若某个新控制的投影不再 Jordan，必须重新计算其参考 framing，不能无证沿用 \(+3\)。

## 2. 水平黑板法向架

记中心曲线的单位切向为

\[
T=\frac{c_\phi}{|c_\phi|},\qquad
r=\sqrt{T_x^2+T_y^2}>0.
\]

正则水平投影恰保证 \(r>0\)。定义水平黑板法向和有向的第二法向

\[
N=\frac{(T_y,-T_x,0)}r,\qquad
B=T\times N
=\left(\frac{T_zT_x}r,\frac{T_zT_y}r,-r\right).
\tag{2}
\]

\((T,N,B)\) 是正定向正交标架。由 (1)，\(d\perp T\) 且 \(|d|=1\)，所以存在唯一的单位圆值函数

\[
a(\phi)=d\cdot N,\qquad
b_f(\phi)=d\cdot B,\qquad a^2+b_f^2=1.
\]

利用 \(d_xT_x+d_yT_y=-d_zT_z\)，得到

\[
\boxed{b_f=-d_z/r=\sigma\cos(3\phi)/r.}
\tag{3}
\]

这里 \(b_f\) 只是法向分量，不是尺度参数 \(b\)。

## 3. 相对黑板标架的绕数准确等于 3

R12 的显式中心导数为

\[
(c_W)_\phi=b\sigma e^{i\psi}
\left[-\psi'\sin\chi\cos\chi+
i(3+\eta\psi'\cos^2\chi)\right].
\tag{4}
\]

在 \(b_f=0\)，也就是 \(\chi=\pi/2+k\pi\) 处，

\[
(c_W)_\phi=i\,3b\sigma e^{i\psi},
\qquad N_W=e^{i\psi},
\qquad d_W=-\sin\chi\,e^{i\psi}.
\]

于是

\[
a=-\sin\chi.
\tag{5}
\]

取单位圆上的正实轴点 \((a,b_f)=(1,0)\) 为正则值。它恰发生在

\[
\chi=3\pi/2+2k\pi.
\]

当 \(\phi\) 绕一周时有且只有三次这样的穿越。在这些点，

\[
b_f'=-3\sigma\sin\chi/r=3\sigma/r>0,
\]

而 \(a=1\)。所以每次都按正向穿过正实轴，给出

\[
\boxed{\deg(a+i b_f)=3.}
\tag{6}
\]

该计数没有使用近似图形、数值相位展开或假设 \(\psi'\) 始终为正。它只用了 \(r>0\)、(1)、(4) 以及 \(\chi=3\phi\)。

## 4. Jordan 投影的黑板参考 linking 为零

由于 \(c_W\) 是正则 Jordan 曲线，可以取足够小的 \(\epsilon>0\)，使平面曲线 \(c_W+\epsilon N_W\) 与 \(c_W\) 不相交。考虑

\[
c_t=(c_W,(1-t)c_z),\qquad
\widetilde c_t=c_t+\epsilon N,\qquad 0\le t\le1.
\]

两条曲线的水平投影始终是这两条不相交的平面曲线，所以整个同伦中它们都彼此不交，各自也是嵌入。故 linking number 不变。

到 \(t=1\) 时，两条闭曲线共处一个平面。它们的 Gauss linking 积分为零：两切向的叉积垂直于该平面，两点差向量位于该平面，逐点三重积为零。因此

\[
\boxed{\operatorname{lk}(c,c+\epsilon N)=0.}
\tag{7}
\]

这说明的是参考黑板 framing 的整数，不是把空间曲线的 writhe 数值近似为零。

## 5. 从法向绕数到核心两边界的 linking

在 \(c\) 的一个足够小的嵌入法向细管内，以 (2) 为框架写

\[
(\phi,\alpha)\longmapsto
c(\phi)+\epsilon(\cos\alpha\,N(\phi)+\sin\alpha\,B(\phi)).
\]

边界环面上的参考曲线 \(\alpha=0\) 是黑板 longitude；绕法向圆一周的 meridian 与 \(c\) 的 linking 为 \(+1\)。一个法向截面 \(\alpha=\alpha(\phi)\) 在该环面的第一同调中为

\[
[\text{longitude}]+\deg(e^{i\alpha})[\text{meridian}].
\]

linking 对此同调类是整数线性函数。因此由 (6)、(7)，

\[
\operatorname{lk}(c,c+\epsilon d)
=0+\deg(a+i b_f)=3.
\tag{8}
\]

换成 \(-d\) 只给角函数增加常数 \(\pi\)，不改变绕数。又可在嵌入准确核心内把第一条截圈从 \(s=\epsilon\) 移到 \(s=0\)，同时保持第二条圈在 \(s=-\epsilon\)；全程两圈不相交。于是

\[
\boxed{\operatorname{lk}(X(\epsilon,\cdot),X(-\epsilon,\cdot))=3.}
\tag{9}
\]

如果实际已证嵌入核心宽度是 \(w\)，可把任意一对有序不同截圈在这个环带内连续移到上面的细管截圈。故 (9) 对核心内部任意两条同向平行截圈成立，并非只对无穷小宽度成立。

## 6. 为什么开放平圆领产生矛盾

设一个假想的嵌入环带

\[
F:S^1\times[\ell_0,\ell_1]\longrightarrow\mathbb R^3
\]

包含准确核心，并在另一个非空开放径向区间内是一个平面圆领。两个有序参数 \(\ell<\ell'\) 的空间是连通的。让二者连续移动时，由环带嵌入性，两条曲线 \(F(S^1,\ell)\)、\(F(S^1,\ell')\) 始终不相交，所以它们的 linking number 是同一个整数。

在核心选取两个截圈，这个整数由 (9) 等于 3。在开放平圆领选取两个不同半径截圈，这两条曲线共平面，linking number 为零。得到矛盾。

即使只有一侧 core-to-tail 半带，这个论证也适用：在保留的开放准确核心 \(0<s<w\) 内取两个正 \(s\) 截圈即可，不需要先镜像成完整双带或先封帽。

如果假想闭面是一个嵌入二球面，任意两个不交平行圈在球面上分别界出不交的帽盘，故 linking 必为零。同样与 (9) 冲突。这是对二球面包含该核心的额外直接排除；它不排除核心作为某些更高亏格嵌入曲面的局部子环带。

## 7. 对当前设计计算的具体影响

第一轮 `warped_core_collar_design.py` 的开放核心、平圆领二 jet 和解析 Jacobian 检查仍然正确；它们并未证明整片环带嵌入。真实有限残差中出现方向塌缩和曲率集中，也不能单凭此诊断成拓扑证据。本文件的排除来自独立的准确 linking 论证。

若某条高模控制路径从已认证基准出发，**并且整个路径中的核心环带始终嵌入**，它的 linking 整数保持为 3，因而不能靠该路径解决平圆领拼接。正则性 \(d_\phi\ne0\) 只保证局部参数不奇异，并不保证上述路径条件；不能跳过自交检查就沿用这个结论。

后续构造应先通过零 framing 门，再投入连接带优化。可选的真实检查是：对两个已证互不相交的窄截圈给出 linking 积分的连续包围，并用整数性确定其值；或对规则投影给出完整交叉/高度证书。一个新核心若 linking 不为零，就不应再安排同一开放平圆领的嵌入 BVP 精化。

这里没有把换用 log stretch 残差或更多自由度当作拓扑修复。不同准确核、不同闭合拓扑与握持机制仍需继续研究。

## 8. 公开来源与独立审核范围

- [R12：ψ-warp 准确负曲率核心](../results/R12-warped-ruled-core.md)：(1)、(4) 和闭合几何。
- [实际宏观核心扫描](../notes/actions-43593187614-1-warped_core/receipt.json)：\(u=.8,1\) 的连续 Jordan 投影与位移预算。
- [R14：法向条带嵌入证书](../results/R14-normal-ribbon-embedding-certificate.md) 与 [实际 tube 运行](../notes/actions-43593758483-1-warped_tube/receipt.json)：两基准 \(w=.05\) 的核心嵌入。
- 2026-11-14，`literature` 独立核对 (2)–(9)、Jordan 压平参考和嵌入环带的平行圈不变量。
- 同日，`repo_sources` 独立以正实轴三次正向穿越核对整数 \(+3\)，并核对平圆领 linking 为零的矛盾。

本文件不依赖新的非线性求解或新增实际参数扫描。
