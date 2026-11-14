# R285：两个跨出生零模块与普通相邻边不足以推出首边 SOS 充分式

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：已证明的形式约束反例。** 下列全部变量是明确的一维正标量数据。它们满足所列两个联合零模 Gram 正性、上下出生的相关普通相邻边、低出生第二边，以及相关玻色仿射下界，但同时违反一位首边的 (S1)、(S2)。因此只把这些后果作为有限半正定约束，不能推出两条候选。

**这不是实际 Boolean 权行，不是否定原相邻常数一，不是 Hilbert ISP 反例。** 本稿没有宣称这些标量能同时实现为一个共同的完整硬核空间、全高度 Serre 系统或真实最小逆族。其作用是准确定位：不能用下述两个联合 Gram 块的形式正性替代尚缺的共同物理运输。

## 1. 所检验的准确形式条件

统一取 $S=1$。使用 [一位首边三块附录](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 的记号：上出生前两阶 Gram 为 $G_1,G_2>0$，下出生前三阶为 $L_1,L_2,L_3>0$，$G_0=L_0=1$。桥 $B$ 从上出生到下出生，$B_s$ 是再高一个出生进入上出生的桥。

令
$$
C_1=G_1^{-1},\quad C_2=G_2^{-1},\quad F=C_1^2-C_2,
$$
$$
Q=B^*L_2,\qquad \Theta=C_1B^*L_3,\qquad
\Delta=(\Theta-Q)/2,
$$
$$
A=\frac12(C_1Q+QL_3^{-1}L_2).
\tag{1.1}
$$
[跨出生零模稿](R284-cross-birth-zero-occupation-grams-and-exact-schur-lower-bound.md) 已证明实际 Boolean 数据必有以下两个联合 Gram 正块：
$$
\mathcal Z_2=
\begin{pmatrix}
G_1-I&Q\\
Q^*&L_2-4L_1+2I-Q^*Q
\end{pmatrix}\succeq0,
\tag{1.2}
$$
以及
$$
\mathcal Z_3=
\begin{pmatrix}X_2&R\\R^*&Y_3\end{pmatrix}\succeq0,
\tag{1.3}
$$
其中
$$
X_2=G_2-4G_1+2I-G_2B_sB_s^*G_2,
$$
$$
R=(2I-C_1)B^*L_3-3Q,
$$
$$
Y_3=L_3-9L_2+18L_1-6I
+\frac92Q^*Q+\frac32(Q^*\Theta+\Theta^*Q)
-\Theta^*(G_1-I/2)\Theta.
\tag{1.4}
$$
不等式 (1.2)、(1.3) 是真正模型的必要后果。本文仅检验它们连同相关普通相邻条件是否已经蕴含
$$
\Delta L_3^{-1}\Delta^*\preceq F\quad\text{(S1)}
$$
或
$$
A^*G_1A+L_1L_2^{-1}L_1\preceq I\quad\text{(S2)}.
$$
答案是否定的。

## 2. 明确的严格正数据

取实标量
$$
\boxed{
G_1=100,\quad G_2=20000,\quad
L_1=10,\quad L_2=200,\quad L_3=8000,\quad
B=\frac1{20},\quad B_s=0.
}
\tag{2.1}
$$
由定义逐项得到
$$
C_1=\frac1{100},\quad C_2=\frac1{20000},\quad
F=\frac1{20000},
$$
$$
Q=10,\qquad \Theta=4,\qquad \Delta=-3,\qquad A=\frac7{40}.
\tag{2.2}
$$

### 2.1 旧普通相邻边全部严格满足

本稿涉及的上首边、下首边和下第二边之比分别为
$$
\frac{G_1^2}{G_2}=\frac12,\qquad
\frac{L_1^2}{L_2}=\frac12,\qquad
\frac{L_2^2}{L_1L_3}=\frac12.
\tag{2.3}
$$
所以它们都严格满足常数一。相应的下出生块
$$
Z_0=\begin{pmatrix}1&10\\10&200\end{pmatrix},\qquad
Z_1=\begin{pmatrix}10&200\\200&8000\end{pmatrix}
$$
也严格正定：行列式分别为 $100$ 和 $40000$。

这些数据还满足当前使用到的玻色仿射后果
$$
G_1\ge1,\quad G_2\ge4G_1-2,
$$
$$
L_1\ge1,\quad L_2\ge4L_1-2,\quad
L_3\ge\frac92L_2-3,\quad L_3\ge18L_1-12.
\tag{2.4}
$$
相应右侧依次是 $1,398,1,38,897,168$。因此失败不来自忘记其中一个仿射下界。

### 2.2 第一个联合零模块严格正

(1.2) 准确成为
$$
\boxed{\mathcal Z_2=
\begin{pmatrix}99&10\\10&62\end{pmatrix},\qquad
\det\mathcal Z_2=6038>0.}
\tag{2.5}
$$
两对角均正，故该块严格正定。

### 2.3 第二个联合零模块严格正

直接用 (1.4) 得
$$
X_2=19602,\qquad R=766,
$$
$$
Y_3=8000-1800+180-6+450+120-1592=5352.
$$
因而
$$
\boxed{\mathcal Z_3=
\begin{pmatrix}19602&766\\766&5352\end{pmatrix},\qquad
\det\mathcal Z_3=104323148>0.}
\tag{2.6}
$$
它同样严格正定。每个块当然可以单独实现为一个真正的二向量 Gram，例如作普通 Cholesky 分解即可；缺少的是这些实现来自同一个完整 Boolean 硬核系统的额外关系。

## 3. 两条首边充分式均严格失败

(S1) 左侧为
$$
\Delta L_3^{-1}\Delta^*=\frac9{8000},
$$
故其差为
$$
\boxed{F-\Delta L_3^{-1}\Delta^*
=\frac1{20000}-\frac9{8000}
=-\frac{43}{40000}<0.}
\tag{3.1}
$$

(S2) 左侧则准确是
$$
\boxed{
A^*G_1A+L_1L_2^{-1}L_1
=\frac{49}{16}+\frac12
=\frac{57}{16}>1.
}
\tag{3.2}
$$
全部比较是精确有理数，不使用浮点抽样。

## 4. 对实际证明路线的限制

本稿仅排除如下推理：把 (1.2)、(1.3)、普通相邻边及 (2.4) 当成全部输入，再以一般矩阵正性、Schur 补或 Cauchy–Schwarz 自动推出 (S1) 或 (S2)。这一纯形式命题已经被标量正定数据否定，因此矩阵非交换并不是这个有限推理缺口的唯一原因。

实际模型仍有每个物理坐标的硬核平方零方程、完整有限顶端、全部出生之间的 Serre 耦合、共同原像与占据投影等约束。本稿没有满足或反驳那个完整系统。若后续用到其中新的实际关系，仍可证明两条候选；若实际两候选有一个失败，原三块首边等价也仍保留，不能把更强充分式的失败当成原目标失败。
