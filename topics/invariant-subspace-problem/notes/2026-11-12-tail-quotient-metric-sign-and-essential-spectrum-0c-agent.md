# 尾商交织度量的符号与本质谱：一个准确边界

日期：2026-11-12。状态：完整引理；不另占结果号。本稿不排除 R208 的实际慢平方核。

## 1. 适用对象

R208 的实系数头图附录给出尾 Hilbert 空间上的闭不变空间

$$
N\subset L,\qquad Q=L/N,
$$

以及尾反射 $R=R_{\rm tail}$。将 $Q$ 实现为 $L\ominus N$，记其正交投影为 $P$。在该附录的情形，

$$
G_L=P_LR|_L,\qquad N\subset\ker G_L,
\qquad G_Q=PR|_Q.
\tag{1.1}
$$

$G_Q$ 是有界自伴算子，可能为零，也可能有核。它满足

$$
G_QA_Q=A_Q^*G_Q.
\tag{1.2}
$$

这里 $A_Q$ 是实际尾移位在该 Haar 子商上的算子。它拟幂零且值域稠密；这些性质在 R23、R140 的子商机制中已经证明。以下第一引理只使用这两个性质，因此也适用于任意有限放大的 Haar 子商。

第二引理使用实际高位反射 $J_j=M_{\chi_j}$。这里的投影强交换不能用于任意投影，其具体依据如下。实际归一化幂满足

$$
\rho_j=N_j+N_j^*-I\longrightarrow0\quad\hbox{强},
\qquad J_j-(N_j^*-N_j)\longrightarrow0\quad\hbox{强}.
\tag{1.3a}
$$

这些是 R164 的实际极限：先在固定有限柱上计算纯单比特矩阵，再用 $\|N_j-E_j\|\le\eta_j\to0$ 和统一范数界延拓到全空间。

若 $P_0$ 是实际 $A$ 不变投影，则 $(I-P_0)N_jP_0=0$，同时 $P_0N_j^*(I-P_0)=0$。所以

$$
[P_0,N_j]=P_0N_j(I-P_0)=P_0\rho_j(I-P_0)\longrightarrow0\quad\hbox{强},
$$

而其伴随为 $(I-P_0)\rho_jP_0\to0$ 强。因此 $[P_0,N_j]\to0$ 强星，并由 (1.3a) 得到 $[P_0,J_j]\to0$ 强星。分别对不变旗的 $P_L,P_N$ 使用这个证明，再相减，才得到商投影 $P=P_L-P_N$ 的结论：

$$
[P,J_j]\longrightarrow0\quad\hbox{强算子拓扑},
\qquad J_j\longrightarrow0\quad\hbox{弱算子拓扑},
\qquad RJ_j=-J_jR.
\tag{1.3}
$$

没有要求 $Q$ 本身是原空间中的不变子空间。固定有限放大只需将 (1.3a) 张量恒等矩阵，上述推导不变。

## 2. 正交织度量必为零

**引理 2.1。** 设 $T$ 是 Hilbert 空间上的有界拟幂零算子，且 $\overline{\operatorname{Ran}T}=H$。若有界算子 $H_0\ge0$ 满足

$$
H_0T=T^*H_0,
\tag{2.1}
$$

则 $H_0=0$。

**证明。** 固定 $x$，令

$$
b_n=\|H_0^{1/2}T^nx\|^2\ge0.
$$

由 (2.1) 和半正内积的 Cauchy--Schwarz 不等式，对 $n\ge1$ 有

$$
b_n^2\le b_{n-1}b_{n+1}.
\tag{2.2}
$$

具体地，$b_n=\langle H_0T^{n-1}x,T^{n+1}x\rangle$，所以这个计算不需要 $H_0$ 可逆。

若 $b_1>0$，则 (2.2) 先迫 $b_0>0$，再递推得到各 $b_n>0$ 且 $b_{n+1}/b_n\ge b_n/b_{n-1}$。因此

$$
b_n\ge b_0\left(\frac{b_1}{b_0}\right)^n.
\tag{2.3}
$$

另一方面，

$$
b_n\le\|H_0\|\,\|T^n\|^2\|x\|^2.
$$

取 $n$ 次方根，拟幂零性与 (2.3) 矛盾。故对每个 $x$ 都有 $b_1=0$，即 $H_0^{1/2}T=0$。值域稠密性给出 $H_0^{1/2}=0$。证毕。

**推论 2.2。** 任意非零 Haar 子商上，满足 $H_0A_Q=A_Q^*H_0$ 的有界半正算子只能为零。半负算子同样只能为零。

因此，若 (1.1) 的 $G_Q\ne0$，不能给它补上半正性假设。对 $G_Q$ 取正部也不合法：从 (1.2) 不推出 $G_Q^+A_Q=A_Q^*G_Q^+$。

## 3. 反射压缩的渐近反交换

在 $Q$ 上定义

$$
F_j=PJ_j|_Q.
\tag{3.1}
$$

它们是自伴收缩，一般不是酉算子。由 (1.3)，

$$
F_j\longrightarrow0\quad\hbox{弱},\qquad
F_j^2\longrightarrow I_Q\quad\hbox{强}.
\tag{3.2}
$$

后一个结论可以直接计算：对 $x\in Q$，

$$
\|F_j^2x-x\|
=\|PJ_j(P-I)J_jx\|
\le\|(P-I)J_jx\|
=\|[P,J_j]x\|\longrightarrow0.
$$

同时，写 $G=PRP$ 为全空间上的零延拓，有精确恒等式

$$
GJ_j+J_jG
=PR[P,J_j]-[P,J_j]RP.
\tag{3.3}
$$

压缩 (3.3)，或者直接将 $P$ 插入每个乘积，得到

$$
G_QF_j+F_jG_Q\longrightarrow0\quad\hbox{强}.
\tag{3.4}
$$

这些结论没有使用 $G_Q$ 非退化，也没有使用未知核空间上的任何范数交换率。

## 4. 整个谱关于零对称，而且都是本质谱

**引理 4.1。** 在可分 Hilbert 空间上，若有界自伴 $G$ 上存在自伴收缩 $F_j$，满足

$$
F_j\to0\ \hbox{弱},\qquad F_j^2\to I\ \hbox{强},
\qquad GF_j+F_jG\to0\ \hbox{强},
\tag{4.1}
$$

则

$$
\sigma(G)=-\sigma(G)=\sigma_{\rm ess}(G).
\tag{4.2}
$$

这里 $\sigma_{\rm ess}$ 是通常 Fredholm 本质谱。

**证明。** 固定 $\lambda\in\sigma(G)$。从 $n=2$ 开始，自伴性给出单位向量 $x_n$，使

$$
\|(G-\lambda)x_n\|\le n^{-1}.
$$

对每个固定 $n$，由 (4.1)，$\|F_jx_n\|\to1$，且

$$
\|(GF_j+F_jG)x_n\|\to0.
$$

取一个固定稠密测试序列，逐个选择严格递增的 $j_n$，同时使上述误差小于 $n^{-1}$、$\|F_{j_n}x_n\|\ge1-n^{-1}$，并使 $F_{j_n}x_n$ 与前 $n$ 个测试向量的内积绝对值小于 $n^{-1}$。定义归一化向量

$$
y_n=F_{j_n}x_n/\|F_{j_n}x_n\|.
$$

则 $y_n\rightharpoonup0$，且

$$
\|(G+\lambda)y_n\|
\le\frac{\|(GF_{j_n}+F_{j_n}G)x_n\|
+\|F_{j_n}(G-\lambda)x_n\|}{\|F_{j_n}x_n\|}
\longrightarrow0.
$$

所以 $-\lambda\in\sigma_{\rm ess}(G)$。于是

$$
-\sigma(G)\subset\sigma_{\rm ess}(G)\subset\sigma(G).
$$

第一包含又迫 $\sigma(G)$ 关于零对称，遂两包含都是等号。证毕。

对 (1.1) 应用该引理即得

$$
\boxed{\ \sigma(G_Q)=-\sigma(G_Q)=\sigma_{\rm ess}(G_Q).\ }
\tag{4.3}
$$

特别地，若 $G_Q\ne0$，则正谱空间和负谱空间都是无限维；$G_Q$ 不能是有限正指标或有限负指标的非零度量，也不能是非零紧算子。

## 5. 对共同零纤维的准确含义

R208 头图附录留下的实际对象是

$$
W_Q=0,\qquad Z_Q=0,
\qquad Z=4\sum_j a_j^2N_j(I+N_j)^{-2}
$$

的共同尾商。实系数情形可从 $Z_Q=0$ 写出关于 $G_Q$ 的有界完全正映射不动点恒等式；但这里的不动点 $G_Q$ 一般不定，甚至可能为零。

本稿证明，不能通过给该交织度量附加半正性或有限负指标来补上正常态论证：若度量非零，它实际上具有对称的无限维正负本质谱。这不是共同零纤维不存在的证明，也不是其存在性构造。

还需保留两个区别：$N\subset\ker G_L$ 不等于 $N=\ker G_L$；全空间上 $W$、$Z$ 分别单射稠密，也不推出上述子商为零。

## 6. 依赖

- R23、R140：实际 Haar 不变子商的拟幂零性与稠密值域。
- R164：实际不变投影与高位 $J_j$ 的强交换。
- R208 头图附录：$N\subset L\cap(RL)^\perp$、共同像闭包，以及 $W_Q=Z_Q=0$ 的准确域含义。

第 2、4 节的抽象引理已在本稿自含证明；没有调用关于不定度量或收缩算子的外部谱定理来排核。
