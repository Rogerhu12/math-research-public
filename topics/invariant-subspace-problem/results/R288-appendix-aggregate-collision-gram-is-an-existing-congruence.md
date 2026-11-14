# R288 附录：聚合碰撞 Gram 已包含在现有跨出生零模块中

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明的依赖说明，不登记新的独立正性输入。** 下面的占据加强确实对实际 Boolean 模型成立，但它恰是已有第一个联合零模块的一次合同，不能用来绕过 R285 的形式反模型。

## 1. 实际碰撞部分

取有限正权 $\sum_i b_i^2=1$，在标准玻色空间记物理坐标湮灭/产生为 $a_i,a_i^*$，第零模式为 $a_0=\sum_i b_i a_i$。实际平方自由空间记为 $\mathcal H$，其投影为 $P_{\rm hc}$；在 $\mathcal H$ 上 $d=a_0|_{\mathcal H}$、$d^*=P_{\rm hc}a_0^*|_{\mathcal H}$。

固定合法上出生 $K_s$（$s\ge1$，至少上高度一合法）。令 $W=\sum_i b_i^2n_i$。对 $f\in K_s$ 定义碰撞产生向量
$$
\mathcal A_{\rm col}f=\sum_i b_i(a_i^*)^2a_i f.
$$
因为 $f$ 的每个物理坐标只能占据零或一，逐基作用准确给
$$
\boxed{\mathcal A_{\rm col}f=(I-P_{\rm hc})a_0^*f=a_0^*f-d^*f.}
\tag{1.1}
$$
不同 $i$ 项具有不同的重复占据坐标，彼此正交。因此
$$
\|\mathcal A_{\rm col}f\|^2=2\langle Wf,f\rangle.
$$
用 $a_0f=0$ 及标准玻色交换关系还得到
$$
a_0\mathcal A_{\rm col}f=2Wf,\qquad
 a_0^2\mathcal A_{\rm col}f=2Cf,\qquad
 a_0^3\mathcal A_{\rm col}f=0,
$$
其中 $C=\sum_i b_i^3E_i$ 在实际 primitive 源上的作用即三次桥。

若 $P_0$ 是第零玻色模式占据为零的正交投影，则按占据零、一、二分解，
$$
\boxed{\|P_0\mathcal A_{\rm col}f\|^2
=2\langle Wf,f\rangle-4\|Wf\|^2+2\|Cf\|^2.}
\tag{1.2}
$$
这给一个正确的加权占据正 Gram。

## 2. 为什么它不是额外约束

沿用 R275 的真 MP 记号，令上出生首阶 Gram 为 $G_1$、$C_1=G_1^{-1}$，下出生前两阶为 $L_1,L_2$，$B=C|_{K_s}$，$Q=B^*L_2$。真实两带身份给
$$
d^*|_{K_s}=\mathcal J_{1,s}C_1-\mathcal J_{2,s-1}B.
$$
置
$$
E=P_0\mathcal J_{1,s},\qquad F=P_0\mathcal J_{2,s-1}.
$$
由于 $a_0^*f$ 的第零模式占据为一，(1.1) 准确成为
$$
\boxed{P_0\mathcal A_{\rm col}=-EC_1+FB.}
\tag{2.1}
$$
[已证跨出生零模稿](R284-cross-birth-zero-occupation-grams-and-exact-schur-lower-bound.md) 给
$$
\begin{pmatrix}E^*E&E^*F\\F^*E&F^*F\end{pmatrix}
=
\begin{pmatrix}
G_1-I&Q\\Q^*&L_2-4L_1+2I-Q^*Q
\end{pmatrix}\succeq0.
\tag{2.2}
$$
所以新看见的范数平方其实就是 (2.2) 对列 $(-C_1,B)^\mathsf T$ 的合同。

令 $H_0=C_1+B^*L_2B=P_{K_s}[d,d^*]|_{K_s}$。直接展开，利用 $C_1G_1C_1=C_1$ 及 $QB=B^*L_2B$，得到
$$
\boxed{
(P_0\mathcal A_{\rm col})^*(P_0\mathcal A_{\rm col})
=H_0-H_0^2-B^*(4L_1-2I)B\succeq0.
}
\tag{2.3}
$$
因此 $B^*(4L_1-2I)B\preceq H_0-H_0^2$ 虽比单独使用 $0\preceq W\preceq I$ 的某些粗界精确，但没有增加 (2.2) 之外的条件。

这也解释了把 $E,F,P_0\mathcal A_{\rm col}$ 三个向量再并成 $3\times3$ 联合 Gram 没有提供新自由度：第三列已经由 (2.1) 线性决定。

## 3. 对后续工作的限制

不能把 (1.2) 的“逐坐标硬核”来源误当成一个尚未使用的独立正性条件；完整展开后，它已经落回现有零模块。R285 的标量形式族仍可满足 (2.3)，这不构成该族的实际 Boolean 实现。

真正可补缺口的关系仍须超出这一次合同，例如额外共享坐标方程、全高度与全出生的实际耦合，或者一个已经证明为收缩的共同物理映射。本文只保存这一依赖，防止把已有正性换一种写法重复计为推进。
