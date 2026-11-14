# R229附录：幂零回文加权移位的最小正秩二泛函

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：完整有限维反例。加强 [R229](R229-cyclic-complex-symmetric-positive-rank-two-counterexample.md) 对一般“循环且共同 $C$ 对称就能把正泛函纯化”的否定：现在同时可取实矩阵、幂零、单个 Jordan 块的相似类、严格正回文权。仍不是目标慢主理想的湮灭见证，亦不构成无限维 ISP 的答案。

## 1. 明确的九维算子

在 $\mathbb C^9$ 标准正交基 $e_1,\ldots,e_9$ 上，取
$$
Ae_j=w_je_{j+1}\quad(1\le j\le8),\qquad Ae_9=0,
$$
$$
(w_1,\ldots,w_8)
=\left(\frac75,5,1,1,1,1,5,\frac75\right).
\tag{1.1}
$$
所有权均为正，且 $w_j=w_{9-j}$。
令
$$
C\left(\sum_{j=1}^9z_je_j\right)
=\sum_{j=1}^9\overline{z_j}e_{10-j}.
$$
逐基计算给 $CAC=A^*$。因此 $A$ 及每个多项式 $p(A)$ 都为同一 $C$ 对称。

$A^9=0$ 而 $A^8\ne0$。$e_1$ 循环，事实上 Krylov 矩阵的行列式为
$$
\det[e_1,Ae_1,\ldots,A^8e_1]
=\prod_{j=1}^8w_j^{9-j}=7^9\ne0.
\tag{1.2}
$$
单个满长幂零 Jordan 块的交换子正是多项式代数；
也可直接由交换子在循环向量 $e_1$ 上的像唯一确定：
$$
\{A\}'=\mathbb C[A].
\tag{1.3}
$$

## 2. 一个三维最高特征空间

置
$$H=\operatorname{Re}A^3=\frac{A^3+(A^*)^3}{2}.$$
按三个模3链
$(e_1,e_4,e_7)$、$(e_2,e_5,e_8)$、$(e_3,e_6,e_9)$
重排后，$H$ 为三个实对称矩阵
$$
\frac12
\begin{pmatrix}
0&p&0\\
p&0&q\\
0&q&0
\end{pmatrix}
$$
的直和，其中 $(p,q)$ 分别为 $(7,1)$、$(5,5)$、$(1,7)$。
每个矩阵的特征值为
$$
-\frac{5\sqrt2}{2},\quad0,\quad\frac{5\sqrt2}{2}.
$$
故 $H$ 的最大特征值
$\lambda=5\sqrt2/2$ 重数恰为3。
其正交单位基可取
$$
u_1=\frac7{10}e_1+\frac1{\sqrt2}e_4+\frac1{10}e_7,
$$
$$
u_2=\frac12e_2+\frac1{\sqrt2}e_5+\frac12e_8,
$$
$$
u_3=\frac1{10}e_3+\frac1{\sqrt2}e_6+\frac7{10}e_9.
\tag{2.1}
$$
记 $E=\operatorname{span}\{u_1,u_2,u_3\}$，$P_E$ 为正交投影。
有 $Cu_1=u_3$、$Cu_2=u_2$。因此
$$
v_1=\frac{u_1+u_3}{\sqrt2},\qquad
v_2=u_2,\qquad
v_3=\frac{i(u_1-u_3)}{\sqrt2}
\tag{2.2}
$$
是 $E$ 的 $C$ 实正交基：$Cv_j=v_j$。

取正迹一密度
$$
\rho=\frac13P_E,\qquad
\phi(F)=\operatorname{Tr}(\rho F).
\tag{2.3}
$$

## 3. 顶层压缩的六个 Hermitian 矩张成全部实对称矩阵

在基 $(v_1,v_2,v_3)$ 中，令
$$
R_k=P_E\operatorname{Re}(A^k)|_E,\qquad
I_k=P_E\operatorname{Im}(A^k)|_E.
$$
直接将 (1.1)、(2.1)--(2.2) 代入得到
$$
R_1=\sqrt2
\begin{pmatrix}
1/20&31/50&0\\
31/50&0&0\\
0&0&-1/20
\end{pmatrix},\qquad
I_1=\sqrt2
\begin{pmatrix}
0&0&-1/20\\
0&0&31/50\\
-1/20&31/50&0
\end{pmatrix},
\tag{3.1}
$$
$$
R_2=
\begin{pmatrix}
37/50&13/10&0\\
13/10&0&0\\
0&0&-37/50
\end{pmatrix},\qquad
I_2=
\begin{pmatrix}
0&0&37/50\\
0&0&-13/10\\
37/50&-13/10&0
\end{pmatrix},
\tag{3.2}
$$
以及
$$
R_6=
\begin{pmatrix}
49/100&0&0\\
0&25/4&0\\
0&0&49/100
\end{pmatrix}.
\tag{3.3}
$$
这些数值来自精确的有限矩阵乘法，不是近似数据。例如 $A^6$ 在三个模3链中分别有唯一长跳权 $7,25,7$，与 (2.1) 的首末系数相乘即给 $49/100,25/4,49/100$。

为明确验证独立性，置
$D=\operatorname{diag}(1,0,-1)$，
$S_{ij}=e_ie_j^T+e_je_i^T$。
$R_1,R_2$ 在 $(D,S_{12})$ 中的系数行列式为
$$
\frac{\sqrt2}{20}\frac{13}{10}
-\frac{31\sqrt2}{50}\frac{37}{50}
=-\frac{1969\sqrt2}{5000}\ne0.
$$
$I_1,I_2$ 在 $(S_{13},S_{23})$ 中的系数行列式也是同一非零数。
$I_E,R_6$ 则张成
$\operatorname{diag}(a,b,a)$ 的两维空间，因为 $49/100\ne25/4$。
再加 $D$，所有三个对角方向均得到。于是
$$
\boxed{
\operatorname{span}_{\mathbb R}
\{I_E,R_1,I_1,R_2,I_2,R_6\}
=\operatorname{Sym}_3(\mathbb R).
}
\tag{3.4}
$$

## 4. 不存在正秩一实现

假设存在 $h\in\mathbb C^9$，使
$$
\langle p(A)h,h\rangle
=\phi(p(A))\qquad(p\in\mathbb C[z]).
\tag{4.1}
$$
取 $p=1$，得 $\|h\|=1$。
取 $p(z)=z^3$ 并取实部，得
$$
\langle Hh,h\rangle
=\operatorname{Tr}(\rho H)=\lambda.
$$
因为 $\lambda I-H\ge0$ 且其核恰为 $E$，必有 $h\in E$。

把 $h$ 在 $C$ 实基 (2.2) 中写成坐标向量 $z=a+ib$，
其中 $a,b\in\mathbb R^3$。
对 (3.4) 中任一实对称矩阵 $M$，(4.1) 及 Hermitian 取实、虚部给
$$
z^*Mz=\frac13\operatorname{Tr}M.
$$
实对称性使左侧等于
$\operatorname{Tr}(M(aa^T+bb^T))$。
由 (3.4) 得
$$
aa^T+bb^T=\frac13I_3.
\tag{4.2}
$$
左侧秩至多2，右侧秩为3，矛盾。
所以 $\phi$ 在 $\mathbb C[A]$ 上没有任何正秩一实现。

## 5. 最小正秩恰为二

每个 $p(A)$ 共同 $C$ 对称，故其在 $C$ 实基 $(v_1,v_2,v_3)$ 上的压缩矩阵为复对称矩阵。
置
$$
h_1=\frac{v_1+i v_2}{\sqrt3},\qquad
h_2=\frac{v_3}{\sqrt3}.
$$
复对称性使 $h_1$ 的两个交叉项抵消，因此对所有 $F\in\mathbb C[A]$，
$$
\langle Fh_1,h_1\rangle+\langle Fh_2,h_2\rangle
=\frac13\sum_{j=1}^3\langle Fv_j,v_j\rangle
=\phi(F).
\tag{5.1}
$$
$h_1,h_2$ 线性无关，所以相应密度正秩为2。
第4节排除秩一，故
$$
\boxed{\text{$\phi|_{\mathbb C[A]}$ 的最小正表示秩恰为2。}}
\tag{5.2}
$$

这没有与通常“循环有限维代数的每个线性泛函都有某个双向量表示”冲突。
这里排除的是同一个向量置于内积两端的正秩一表示；
两端可变的表示不是本稿对象。

## 6. 对主路线的准确意义

R229 的一般复杂对称例子原本没有幂零假设。
本稿进一步说明：实性、幂零性、严格正回文加权移位、循环性和共同 $C$ 对称性，合在一起仍不足以把任意正有限秩泛函降成正秩一。

这不证明原实际 $A$ 的正泛函具有相同障碍，也没有给某个全空间单射慢 $S$ 的 $\phi(S\mathcal A)=0$ 见证。
本例中的 $\phi$ 特意在 $\operatorname{Re}A^3$ 的非零最高特征值上取等；
它不是把全部正幂湮灭的原点态。
因此它只排除所列有限维结构条件提供的普遍纯化推理。
真实最小正常见证仍须使用其完整慢理想湮灭方程与无限维闭域结构。

