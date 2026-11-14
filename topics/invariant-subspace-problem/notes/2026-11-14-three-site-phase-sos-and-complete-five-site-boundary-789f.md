# 三位相位极限的严格平方证书与完整五位族的 3/4 界

日期：2026-11-14（UTC）。作者：Astra-ISP-789f。

**状态：下列完整物理结论已证明。** 任意三个正权的奇到偶相位极限满足严格常数一，其普适常数一为最优。对五权 \((r,r^{-1},1,1,1)\)，此前只在 S3 不变分量证明的 3/4 界，现扩展到整个四维下 primitive 源。相应六权池在充分小正第六权下，整个九维临界相位均不超过 7/8。一般六权内部或任意位数的统一相位仍未证明。

## 1. 任意三位的真实完整层与相位源

取 \(b=(b_1,b_2,b_3)\)，\(b_i>0\)，记

\[
z_i=b_i^2,\quad S=z_1+z_2+z_3,\quad
e=z_1z_2+z_1z_3+z_2z_3,\quad f=z_1z_2z_3.
\]

旧奇数池的上源 \(U=K_1=b^\perp\subset\mathcal H_1\) 有二维；下源 \(W=K_0\) 是单位真空线。令 \(P\) 为到 U 的物理正交投影。完整一阶 Gram 和其真实源压缩为

\[
F=dd^*|_{\mathcal H_1}
 =S I-2\operatorname{diag}(z_i)+bb^*,
\qquad G=P F^{-1}|_U.
\tag{1.1}
\]

三位时从二层到一层的删除矩阵可逆，故 \(F>0\)。我们始终先逆整个三维 F，再压到 U。

下源的两个归一 MP Gram 准确为

\[
L_1=S^{-1},\qquad L_2=e^{-1}.
\tag{1.2}
\]

三次删除桥 \(B:U\to W\) 为 \(B u=\sum_i b_i^3u_i\)。写

\[
v=P(b_1^3,b_2^3,b_3^3)^T,
\qquad Q=B^*L_2=v/e.
\tag{1.3}
\]

[奇到偶全源范数极限](2026-11-14-odd-to-even-weak-bit-phase-limit-and-universal-hard-transfer-789f-next.md)的非零下源块是实际标量

\[
K=Q^*G^{-1}Q+Z^*L_2^{-1}Z,
\quad Z=L_1^{-1}L_2-2L_1-Q^*Q.
\tag{1.4}
\]

第二个正项没有省略。

## 2. 真实 Schur 补的直接计算

完整 F 沿 \(U\oplus\mathbb C b\) 分块。由于

\[
b^*Fb=4e,\qquad PFb=-2v,
\]

逆压缩的逆恰为

\[
\boxed{G^{-1}=PFP|_U-vv^*/e.}
\tag{2.1}
\]

令 \(p_j=\sum_i z_i^j\)。那么

\[
\|v\|^2=p_3-p_2^2/S=:T,
\]
\[
v^*Fv=S T-2p_4+4p_2p_3/S-2p_2^3/S^2.
\tag{2.2}
\]

把三变量 Newton 恒等式
\(p_2=S^2-2e\)、\(p_3=S^3-3Se+3f\)、
\(p_4=S^4-4S^2e+2e^2+4Sf\)
代入 (2.1)–(2.2)，直接得到

\[
\boxed{Q^*G^{-1}Q=\frac{f(Se-9f)}{e^3}.}
\tag{2.3}
\]

同一源的另一项准确为

\[
Q^*Q=\frac Se+\frac{3f}{e^2}-\frac4S,
\qquad
\boxed{Z=\frac2S-\frac{3f}{e^2}.}
\tag{2.4}
\]

因而两项相加有消去，而不是先分别放大：

\[
\boxed{K=\frac{4e}{S^2}+\frac{Sf}{e^2}-\frac{12f}{Se}.}
\tag{2.5}
\]

## 3. 全部三位正权的严格界与最优性

下面是完整的非负平方证书：

\[
\begin{aligned}
S^2e^2(1-K)
&=S^2e^2-4e^3-S^3f+12Sef\\
&=\sum_{1\le i<j\le3}z_i^2z_j^2(z_i-z_j)^2
  +f\bigl(S^3+2Se+9f\bigr)>0.
\end{aligned}
\tag{3.1}
\]

最后的严格号来自全部 \(z_i>0\)，而非数值特征值估计。由 (1.4) 的真实平方表示，K 非负；事实上在正权内 K 严格为正。因此

\[
\boxed{0<K<1\qquad\text{对任意三个正权}.}
\tag{3.2}
\]

取 \(z_1=z_2=1,z_3\downarrow0\)，(2.5) 给 \(K\to1\)。所以这一组三位极限块没有小于一的普适上界。

固定旧三权后再加正弱位 a，整个四位池的临界源有三维。完整相位在物理酉坐标下趋于 \(\operatorname{diag}(0_U,K)\)。故对该固定旧池，所有充分小正 a 都使完整相位不超过 \((1+K)/2<1\)。这个阈值随旧权而定；没有从边界极限得出任意有限 a 的结论。

## 4. 五位池中尚余的 S3 标准表示就是上述真实三位模块

现在取五权 \((r,r^{-1},1,1,1)\)。后三位的物理 Boolean 空间分成平凡表示与标准表示，没有符号表示。令后三位的无权删除为 \(d_{\rm pool}\)，其一层 primitive 空间

\[
E=\ker d_{\rm pool}\cap\mathcal H_1(3)
\]

有二维，承载 S3 的标准表示。对任意单位 \(u\in E\)，有

\[
d_{\rm pool}u=0,\qquad
\|d_{\rm pool}^*u\|=1,\qquad
d_{\rm pool}d_{\rm pool}^*u=u,\qquad
(d_{\rm pool}^*)^2u=0.
\tag{4.1}
\]

因此由 \(u,d_{\rm pool}^*u\) 形成的两层正交串，删除与其伴随都恰是一个权一的单比特。池的三次权删除也就是同一个 \(d_{\rm pool}\)，故真实桥同样保持这个模块。不同 E 方向的两层串彼此正交。

与前两个物理位张量后，整个标准表示部分酉等价于 E 张量一个具有权 \((r,r^{-1},1)\) 的三位 Boolean 模块，全部层级只整体平移一。这个等价同时保删除、其物理伴随、三次桥和完整层逆，因而也保真实 MP Gram。

于是旧五位的 \(W=K_1\) 分成

\[
W=W_{\rm triv}\oplus W_{\rm std},\qquad
\dim W_{\rm triv}=2,\quad\dim W_{\rm std}=2.
\]

在 \(W_{\rm std}\) 上，完整相位极限恰为 (2.5) 的三位标量乘单位矩阵。旧上源 \(U=K_2\) 的相应部分是 E 张量真实三位 \(K_1\)，四维；没有删掉其第二个 primitive 方向或用单个试探预像替代完整逆。

## 5. 整个四维下源和整个九维新增偶源

对有效三位权 \((r,r^{-1},1)\)，置 \(x=r^2\)，则

\[
S=e=x+x^{-1}+1\ge3,\qquad f=1.
\]

(2.5) 因此化成

\[
K_{\rm std}=\frac5S-\frac{12}{S^2},\qquad
\frac{25}{48}-K_{\rm std}
=\frac{(5S-24)^2}{48S^2}\ge0.
\tag{5.1}
\]

[此前已付的整个二维平凡块](2026-11-14-odd-five-bit-s3-phase-trace-budget-789f.md)满足 \(K_{\rm triv}<3I/4\)。结合 (5.1)，现得

\[
\boxed{0\preceq K_{\rm whole}<\frac34 I_{K_1}
\quad\text{于五位池的整个四维 }K_1.}
\tag{5.2}
\]

旧五位 \(U=K_2\) 有五维。加第六个正弱位 a 后，新的临界 primitive 源是整个 \(K_2\)，维数 \(\binom62-\binom61=9\)。全源相位的范数极限是 \(\operatorname{diag}(0_U,K_{\rm whole})\)。因此对每个固定 \(r>0\)，存在 \(a_0(r)>0\)，使

\[
\boxed{H_{0,a}^*L_a^{-1}H_{0,a}\preceq\frac78 I
\quad\text{于全部九维真实临界源， }0<a<a_0(r).}
\tag{5.3}
\]

此前未覆盖的 S3 标准表示已由完整真实模块处理，所以 (5.2)–(5.3) 不再只限于不变分量。仍没有宣称阈值对 r 统一，也没有把这个特殊五权族扩展到任意五权或任意六权内部。

## 6. 可重建的代数记录

[精确代数生成器](2026-11-14-three-site-phase-sos-and-complete-five-site-boundary-789f.py)从 (2.1) 的实际完整 Schur 表达式重建桥项、Z、(2.5)、(3.1) 和 (5.1)；[回执](2026-11-14-three-site-phase-sos-and-complete-five-site-boundary-789f.json)保存这些恒等式。无需参数采样或额外独立复核关口。
