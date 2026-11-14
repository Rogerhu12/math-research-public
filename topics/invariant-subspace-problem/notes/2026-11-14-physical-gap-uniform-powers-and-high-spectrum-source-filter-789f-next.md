# 正 gap 滤波的统一幂预算与精确高谱截断

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 本稿接[全源正 gap 滤波](2026-11-14-physical-gap-all-source-positive-filter-and-paid-negative-range-789f-next.md)，补齐其反复应用的真实费用。结论来自一个保非交换次序的二次型不等式，不把单步的 \(\sqrt2\) 常数反复相乘。固定参数下滤波幂趋零的速率仍依赖该参数，不能与原移动头／孔窗极限交换。

## 1. 同一 \(L\) 单位坐标中的耗散不等式

使用前稿的
\[
\mathcal E=(L+B)^{-1}L-(L+G^{-1})^{-1}L,\qquad
B\preceq G^{-1},
\]
并在本节写
\[
E=L^{1/2}\mathcal EL^{-1/2},\quad
X=L^{-1/2}BL^{-1/2},\quad
Y=L^{1/2}GL^{1/2},\quad M=X+Y.
\]
故 \(\mu(r)=\|L^{1/2}r\|\)、\(\Xi(r)^2=
\langle M L^{1/2}r,L^{1/2}r\rangle\)，且
\(0\preceq E\preceq I\)、\(I-E\preceq M\)。

令
\[
F=(I+X)^{-1},\qquad Z=(I+Y^{-1})^{-1}.
\]
由 \(X\preceq Y^{-1}\)，\(0\prec Z\preceq F\prec I\)，而
\[
E=F-Z,\qquad 0\preceq E\preceq F,\quad
0\preceq E\preceq I-Z.
\]
完整非交换恒等式为
\[
EME+2E^2=E\{F^{-1}+(I-Z)^{-1}\}E.
\]
对任意 \(0\preceq E\preceq H\) 且 \(H\) 严格正，
\(EH^{-1}E\preceq E\)，这是将
\(H^{-1/2}EH^{-1/2}\preceq I\) 平方后合同的结果。
分别取 \(H=F\) 和 \(I-Z\)，得到
\[
\boxed{EME\preceq2E(I-E).}
\tag{1.1}
\]
右边的乘积是 \(E\) 自身的谱函数，无任何不允许的 \(M,E\) 交换。

同一个式子也由前稿的原物理未来差 \(h\) 得到：
\[
\Xi(\mathcal Er)^2\le2\|h\|^2,\qquad
\|h\|^2=\langle E(I-E)L^{1/2}r,L^{1/2}r\rangle.
\]
因而矩阵证明与原物理投影完全同源。

## 2. 任意次幂的统一两费用与左误差

对每个整数 \(n\ge1\)，将 (1.1) 以 \(E^{n-1}\) 合同：
\[
\boxed{
E^nME^n
\preceq2E^{2n-1}(I-E)
\preceq2(I-E)\preceq2M.}
\tag{2.1}
\]
因此
\[
\boxed{\Xi(\mathcal E^n r)\le\sqrt2\,\Xi(r)
\qquad(n\ge1).}
\tag{2.2}
\]
右端不随 \(n\) 增长。

标量 \(0\le t\le1\) 上有
\[
(1-t^n)^2\le1-t^n\le n(1-t).
\]
所以
\[
\boxed{
\mu(r-\mathcal E^n r)^2
\le n\langle L(I-\mathcal E)r,r\rangle
\le n\,\Xi(r)^2.}
\tag{2.3}
\]
所有 \(n\ge1\) 的像仍属于前稿的全部共同费用负图，因
\(\operatorname{Ran}\mathcal E^n\subset\operatorname{Ran}\mathcal E\)。

此外，将
\[
EME+(I-E)^2\preceq I-E^2
\]
依次以 \(E^{n-1}\) 合同并望远镜，得到真正总耗散预算
\[
\boxed{
\sum_{n\ge1}\left\{
\Xi(\mathcal E^n r)^2+
\mu(\mathcal E^{n-1}r-\mathcal E^n r)^2
\right\}
\le\mu(r)^2.}
\tag{2.4}
\]
只保留两费用还可写成算子序
\[
\sum_{n\ge1}E^nME^n
\preceq 2E(I+E)^{-1}\preceq I.
\tag{2.5}
\]

## 3. 固定参数的收敛与不能交换的量词

固定原 \(m,q\) 时 \(L,B,G\) 有界严格正。特别 \(X\succeq aI\) 对某个 \(a>0\)，故
\[
I-E\succeq X(I+X)^{-1}
\succeq\frac{a}{1+a}I.
\]
因此
\[
\boxed{\ker(I-E)=0,\qquad
\|E^n\|\le(1+a)^{-n}\longrightarrow0.}
\tag{3.1}
\]
这是固定参数的算子范数收敛；\(a\) 的温和原窗下界未付。

(2.2) 的统一两费用不意味着 \(\mathcal E^n r\) 的左范数能在 \(n\to\infty\) 时仍保持。它最终按 (3.1) 趋零；同时 (2.3) 的 \(\sqrt n\) 误差增长。只有在真正的移动来源上另外保有
\(n\,\Xi(r)^2\to0\)，才能将 (2.3) 用作左近似。本文不从固定参数收敛推出原 \(N=M\)。

## 4. 高 \(E\) 谱带的准确源保持过滤

这也是 (1.1) 的一个直接、可单独使用的后果。
对 \(0<\varepsilon<1\)，令
\[
P_\varepsilon=1_{[1-\varepsilon,1]}(E),\qquad
r_\varepsilon=L^{-1/2}P_\varepsilon L^{1/2}r.
\]
\(E^{-1}P_\varepsilon\) 有界；由 (1.1) 作此共同合同，
\[
P_\varepsilon M P_\varepsilon
\preceq2P_\varepsilon E^{-1}(I-E)P_\varepsilon.
\]
因此
\[
\boxed{
\Xi(r_\varepsilon)^2
\le\frac{2}{1-\varepsilon}\,\Xi(r)^2,\qquad
\mu(r-r_\varepsilon)^2
\le\frac1\varepsilon\,\Xi(r)^2.}
\tag{4.1}
\]
同时在整个过滤像上，
\[
\boxed{\Xi(r_\varepsilon)^2
\le\frac{2\varepsilon}{1-\varepsilon}\,
\mu(r_\varepsilon)^2.}
\tag{4.2}
\]
由于 \(P_\varepsilon=E(E^{-1}P_\varepsilon)\)，这个像确实位于
\(\operatorname{Ran}\mathcal E\)，保留全部共同费用负图，不只保其闭包。

(4.2) 是该高谱空间上“两费用相对左费很小”的准确方向，不能反向使用为原所需的左费用上界。它定位可能的长寿命 gap 方向，没有排除它们。若再施加已付联合旗投影，须继续使用前稿的真实改变量界；不假定该投影与 \(P_\varepsilon\) 或 \(\mathcal E\) 交换。
