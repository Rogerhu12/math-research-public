# R288：逐物理位的占据、碰撞与 creation 共同 Gram

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下有限模型身份与条件蕴含已证明；S2 收缩仍未证明。** 本稿保留每个真实物理坐标，供后续使用完整硬核关系；不把已经塌回 R284 的碰撞总和重复登记为新约束。这里没有把 R285 的抽象数据解释成满足全部逐位身份的实际模型。

## 1. 实际 primitive 删除行与每个占据投影

取有限正权 $d=\sum_{i=1}^M b_iE_i$，归一 $\sum b_i^2=1$。固定 $s\ge1$，要求 $M\ge2s+1$。记
$$
K=\ker d\cap\mathcal H_s,\qquad L=\ker d\cap\mathcal H_{s-1}.
$$
令 $G_1$ 是上出生首阶归一真 MP Gram，$L_1,L_2$ 是下出生前两阶；$\mathcal J_{j,r}=(d^j/j!)^\dagger|_{K_r}$。定义逐位实际删除
$$
R_i=E_i|_K:K\to L,\qquad N_i=R_i^*R_i=P_Kn_i|_K.
\tag{1.1}
$$
$R_i$ 的值确在 $L$，因为 $E_i$ 与 $d$ 交换。于是
$$
\sum_i b_iR_i=0,\qquad \sum_iN_i=sI_K,\qquad0\preceq N_i\preceq I_K.
\tag{1.2}
$$
不同出生上的这些真实 $R_i$ 还继承逐位平方零及相互交换：在合法源中
$R_i^{(s-1)}R_i^{(s)}=0$、$R_i^{(s-1)}R_j^{(s)}=R_j^{(s-1)}R_i^{(s)}$。

对 $f\in K$，$d n_i f=b_iR_i f$，且再删一次为零。因而 $n_if$ 在整个实际 $\ker d^2|_{\mathcal H_s}$ 中的正交分解为
$$
\boxed{n_i f=N_i f+b_i\mathcal J_{1,s-1}R_i f.}
\tag{1.3}
$$
两项分别在 $K$ 和 $\ker d^2\ominus\ker d$ 中。对两份源配对给
$$
\boxed{P_Kn_in_j|_K=N_iN_j+b_ib_jR_i^*L_1R_j.}
\tag{1.4}
$$
特别，每个物理投影 $n_i^2=n_i$ 都保留为
$$
\boxed{N_i-N_i^2=b_i^2R_i^*L_1R_i.}
\tag{1.5}
$$
物理 $n_i,n_j$ 的交换进一步给准确的压缩交换缺陷
$$
[N_i,N_j]=-b_ib_j(R_i^*L_1R_j-R_j^*L_1R_i).
\tag{1.6}
$$
所以不能在使用 (1.4) 时把不同 $N_i$ 默认为交换。

## 2. 保留全部单坐标碰撞零模

在实际玻色嵌入中记物理产生/湮灭为 $a_i^*,a_i$，第零模式为 $a_0=\sum b_i a_i$，其真空投影为 $P_0$。定义
$$
\mathcal A_i=b_i(a_i^*)^2a_i|_K,\qquad V_i=P_0\mathcal A_i.
$$
不同 $i$ 的未投影碰撞向量具有不同的重复占据坐标，故
$$
\mathcal A_i^*\mathcal A_j=2\delta_{ij}b_i^2N_i.
$$
逐基或用交换关系得到
$$
a_0\mathcal A_i=2b_i^2n_i|_K,\qquad
 a_0^2\mathcal A_i=2b_i^3R_i,\qquad a_0^3\mathcal A_i=0.
$$
在这个最高占据二的空间上，真空投影的配对公式为
$$
\langle P_0u,P_0v\rangle
=\langle u,v\rangle-\langle a_0u,a_0v\rangle
+\tfrac12\langle a_0^2u,a_0^2v\rangle.
$$
于是得到保留所有物理位交叉的精确 Gram：
$$
\boxed{
V_i^*V_j
=2\delta_{ij}b_i^2N_i
-4b_i^2b_j^2P_Kn_in_j|_K
+2b_i^3b_j^3R_i^*R_j.
}
\tag{2.1}
$$
矩阵 $[V_i^*V_j]_{i,j}$ 是 $K^{\oplus M}$ 上的正算子。它允许每个位使用不同源向量；只对全部 $i$ 求和，会丢掉这份逐源共同数据。

## 3. 与已有两个零模的完整交叉

令
$$
B=\sum_i b_i^3R_i,\qquad Q=B^*L_2,\qquad
E=P_0\mathcal J_{1,s},\qquad F=P_0\mathcal J_{2,s-1}.
$$
[R284 的已证零模公式](R284-cross-birth-zero-occupation-grams-and-exact-schur-lower-bound.md)为
$$
E^*E=G_1-I,\quad E^*F=Q,\quad
F^*F=L_2-4L_1+2I-Q^*Q.
$$
物理硬核向量 $\mathcal J_{1,s}f$、$\mathcal J_{2,s-1}y$ 均与每个 $\mathcal A_i g$ 正交。用上节真空配对式，得到
$$
\boxed{E^*V_i=-2b_i^2N_i.}
\tag{3.1}
$$
另一方面，真实两带式 $d\mathcal J_{2,s-1}=2\mathcal J_{1,s-1}-Q$ 及 (1.3) 给
$$
\boxed{F^*V_i=-2b_i^3(2L_1-I)R_i+2b_i^2Q^*N_i.}
\tag{3.2}
$$
因此 $E,F,V_1,\ldots,V_M$ 构成一个全部条目如上明确的共同正 Gram。该陈述使用一个共同的实际零模空间，不是把各坐标的独立二次型界相加。

对全部 $i$ 求和时，$\sum_iV_i=-EC_1+FB$，$C_1=G_1^{-1}$。故聚合碰撞的正性已经是已有 $(E,F)$ 块的一次合同，见[依赖说明](R288-appendix-aggregate-collision-gram-is-an-existing-congruence.md)。本稿保留的是未先求和的行及其实际坐标约束；没有声称它们自动支付 S2。

## 4. 每个实际 creation 的完整三带分解

令
$$
T_i=P_{K_{s+1}}E_i^*|_K,
\qquad A_i=b_i(I-2N_i)-b_i^2QR_i.
\tag{4.1}
$$
这里 $K_{s+1}=\ker d\cap\mathcal H_{s+1}$，允许它是零空间。因为
$$
dE_i^*f=b_i(I-2n_i)f,\qquad
 d^2E_i^*f=-2b_i^2R_if,\qquad d^3E_i^*f=0,
$$
按同一物理层的三个正交核差空间分解，得到
$$
\boxed{E_i^*|_K=T_i+\mathcal J_{1,s}A_i-b_i^2\mathcal J_{2,s-1}R_i.}
\tag{4.2}
$$
证明可直接逐次删孔核验：右端二阶删除为 $-2b_i^2R_i$，一阶删除为 $b_i(I-2N_i)-2b_i^2\mathcal J_{1,s-1}R_i=b_i(I-2n_i)|_K$，余差落入 $K_{s+1}$。三个分量分别属于深度零、一、二，故互相正交。

实际单坐标 creation 的整个行 Gram 是
$$
P_KE_iE_j^*|_K=R_j^*R_i+\delta_{ij}(I-2N_i).
$$
因此 (4.2) 给新的完整行表示
$$
\boxed{
T_i^*T_j=
R_j^*R_i+\delta_{ij}(I-2N_i)
-A_i^*G_1A_j-b_i^2b_j^2R_i^*L_2R_j.
}
\tag{4.3}
$$
其 $i,j$ 块矩阵半正定性保留了所有 creation 交叉；不能把 $R_j^*R_i$ 错换为 $R_i^*R_j$。

为保留与原加权行的接合，另有
$$
\boxed{\sum_i b_iT_i=0,\qquad
\sum_i b_iA_i=C_1,\qquad
\sum_i b_i^3R_i=B.}
\tag{4.4}
$$
第一式来自 $d^*K\perp K_{s+1}$；第二式来自
$\mathcal J_{1,s}^*d^*|_K=(d\mathcal J_{1,s})^*=I_K$，
再以同一个 $G_1$ 求正交投影系数。因而 (4.2) 的加权和准确回到
$d^*|_K=\mathcal J_{1,s}C_1-\mathcal J_{2,s-1}B$。
尤其 $C_1=I-2\sum_i b_i^2N_i-B^*L_2B$；这里没有另换源度量。

## 5. 一个可直接支付 S2 的共同物理提升准则

再假定下出生第三高度合法，置
$$
A=\frac12(C_1Q+QL_3^{-1}L_2),\qquad
\mathcal T=\mathcal J_{1,s}A+\mathcal J_{2,s-1}L_2^{-1}L_1.
$$
[R275 的 S2](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 正是 $\|\mathcal T\|\le1$。以下给一个实际局部提升的充分条件，尚未构造一般满足条件的提升。

若能在同一个模型中找到 $Y_i:L\to K$，使
$$
\sum_iA_iY_i=A,\qquad
-\sum_i b_i^2R_iY_i=L_2^{-1}L_1,
\tag{5.1}
$$
并证明共同物理映射
$$
\mathcal Z=\sum_iE_i^*Y_i:L\to\mathcal H_{s+1}
$$
为收缩，则 (4.2) 的两塔正交投影恰是 $\mathcal T$。所以立即得到 S2。

所需收缩可准确写成保留全部交叉的一个块式
$$
\boxed{
\sum_{i,j}Y_i^*
\{R_j^*R_i+\delta_{ij}(I-2N_i)\}Y_j\preceq I_L.
}
\tag{5.2}
$$
它不是对每个 $Y_i$ 单独估费，也没有使用已经失效的逆源度量粗求和。

本稿没有证明 (5.1)、(5.2) 在一般正权模型中可同时满足，亦没有证明这个具体提升准则对 S2 必要。它明确保留可继续尝试的实际共享算子及约束，而不把“某个抽象行是收缩”当成已完成的数学步骤。
