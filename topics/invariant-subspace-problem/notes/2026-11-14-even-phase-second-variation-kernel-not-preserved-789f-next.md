# 偶临界相位的二阶退化核不必沿权重直线保持等号

本稿只固定一个已知的真实四位模型，排除把二阶退化核直接当作永久等号模块的做法。它不是相位不等式的反例，也不把一个指定源的四阶正值当作整个退化块的 Schur 正性。

依赖的实际规范见 `2026-11-14-four-bit-all-weight-even-phase-bound-789f-next.md` 与 `2026-11-14-all-birth-even-phase-equal-weight-second-variation-789f-next.md`。本稿重列所有所需四位矩阵。

## 1. 一个真正的二阶零方向

取四位 unweighted Boolean 空间，\(d_0=\sum_iE_i\)、\(e_0=d_0^*\)。在 \(V_0=\ker d_0\cap\mathcal H_1\) 取

\[
x=(-1,0,0,1),\qquad
v=\tfrac12(e_1-e_2-e_3+e_4),\qquad \|v\|=1.
\]

写 \(X_j=\sum_i x_i n_i\) 于第 \(j\) 层，其中 \(n_i\) 是占据投影。直接有

\[
e_0v=e_{14}-e_{23},\qquad X_2e_0v=0. \tag{1.1}
\]

全出生二阶定理的正系数

\[
K_2=\tfrac14(d_x|_{V_0})^*(d_x|_{V_0})
 +\tfrac12(P_{U_0}d_x^*|_{V_0})^*(P_{U_0}d_x^*|_{V_0}),
\qquad U_0=\ker d_0\cap\mathcal H_2,
\]

满足 \(\ker K_2=\ker(X_2e_0|_{V_0})\)，故 \(K_2v=0\)。这里两个极端 \(x\)-组都是单点；它们的 spin \(1/2\) 均活动，不能化为“各等 \(x\) 组中除一个活动组外全取 singlet”的模块。

## 2. 沿真正正权直线的完整物理矩阵

取

\[
z(u)=(1-u,1,1,1+u),\qquad b_i(u)=\sqrt{z_i(u)},\qquad |u|<1.
\]

真实源为 \(V(u)=b(u)^\perp\)。固定无权源的去权映射是

\[
\mathcal E_uv=\operatorname{diag}(b_i(u)^{-1})v\in V(u).
\]

它并非酉映射，下面保留完整源度量。用三列

\[
E_i=\frac{e_i}{b_i}-\frac{e_4}{b_4},\quad i=1,2,3,
\qquad H=E^*E
=\operatorname{diag}(z_1^{-1},z_2^{-1},z_3^{-1})+z_4^{-1}{\bf1}{\bf1}^T.
\]

令 \(S=e_1(z),q=e_2(z),f=e_3(z),\pi=\prod_i z_i\)。\(C=G^{-1}\)、\(L\)、\(Q_0\) 的真实源算子坐标为

\[
\begin{aligned}
C_{ij}&=(S-2z_i)\delta_{ij}
 +\frac{z_i(S-z_i)(z_j-z_4)}q,\\
L_{ij}&=\frac{Sz_i^2\delta_{ij}-z_i(z_j^2-z_4^2)}{S\pi},\\
(Q_0)_{ij}&=
\frac{S(f-2\pi/z_i)\delta_{ij}
 +(S-2z_i)(\pi/z_j-\pi/z_4)}{S\pi}.
\end{aligned} \tag{2.1}
\]

这里 \(G=\Gamma_{1,1}\)、\(L=\Gamma_{2,1}\) 是对完整 \(d\) 和 \(d^2/2\) 作 MP 逆后所得的 primitive Gram；\(Q_0=P_Ve^*e|_V=4G+A_0A_0^*\)。式 (2.1) 的来源分别是完整第一层 Schur、真顶二步 MP 逆、完整 reciprocal Gram。没有把 nuisance 逆与 primitive 压缩交换。

实际相位为

\[
\Phi=H_0^*L^{-1}H_0,\qquad H_0=CL+2C^{-1}-Q_0.
\]

由于 (2.1) 是非正交源算子坐标，它的物理缺陷**二次型矩阵**为

\[
\mathcal D(u)=H-H_0^T H L^{-1}H_0. \tag{2.2}
\]

最后一个源向量对应三维坐标 \(a=(1,-1,-1)^T/2\)，即 \(Ea=\mathcal E_uv\)。

## 3. 精确非零四阶能量

把 \(z(u)\) 代入 (2.1)–(2.2)，直接有理化得到

\[
\boxed{
\langle\mathcal E_uv,(I-\Phi(u))\mathcal E_uv\rangle
=\frac{u^4(u^8-34u^6+240u^4-576u^2+432)}
{2(u-1)(u+1)(u^2-6)^2(u^2-3)^2(u^2-2)}.
} \tag{3.1}
\]

其源范数是

\[
\|\mathcal E_uv\|^2
=\frac{u^2-2}{2(u-1)(u+1)}.
\]

写 \(t=1-u^2>0\)，(3.1) 的分子括号严格等于

\[
63+194t+144t^2+30t^3+t^4>0.
\]

分母在 \(|u|<1\) 也为正。因此指定真实源的缺陷在 \(0<|u|<1\) 严格正，且

\[
\langle\mathcal E_uv,(I-\Phi(u))\mathcal E_uv\rangle
=\tfrac13u^4+O(u^6). \tag{3.2}
\]

作为同一次完整有理运算的附带恒等式，

\[
\det\mathcal D(u)=
\frac{12u^8(u^4-28u^2+48)}
{(u-1)(u+1)(u^2-6)^2(u^2-3)^2(u^2-2)}. \tag{3.3}
\]

例如 \(u=1/2\) 时其秩精确为 \(3\)。这足以排除该二阶零方向沿整条正权直线保持相位等号。结合已证全四权相位正性，(3.3) 还给该特定直线所有非零 \(|u|<1\) 上完整缺陷严格正；此结论不外推到更高位数。

## 4. 方法边界

式 (1.1) 只把源定位于中央零加权占据子空间。不同等值组之间的互补子集可以产生这种零方向，并不要求每个非活动组内部为 singlet。

式 (3.2) 使用固定去权源，不是对二阶核及其正交补先作高阶 Schur 消元后的系数。若要据此证明一般位数的完整局部相位界，仍须联合控制三阶交叉项和核上的四阶（或更高阶）缺陷，不能只把这个逐点正值逐块拼接。

配套 `2026-11-14-even-phase-second-variation-kernel-not-preserved-789f-next.py` 是产生 (3.1)–(3.3) 的原有符号运算。此次只保存已完成的准确运算，没有增加扫描或额外复核。
