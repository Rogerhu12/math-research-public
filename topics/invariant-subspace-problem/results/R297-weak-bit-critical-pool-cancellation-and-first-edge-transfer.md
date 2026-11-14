# 任意临界正权池加入弱位：首加强费用的真实抵消极限与低出生传输

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：下列有限维范数极限、硬端抵消及严格反例传输已证明。** 本文处理任意临界旧正权池，不限旧权分组。它支付弱位边界上的共同小精度抵消；没有声称全部正参数或一般统一 \(\kappa\) 已被证明。

## 1. 两个旧源与新源始终保留

旧行有 \(M=2s\) 个任意正权，\(s\ge1\)：
\[
d=\sum_{i=1}^{2s}b_iE_i,
\qquad C=\sum_i b_i^3E_i,
\qquad b_i>0.
\]
定义三个实际 primitive 源
\[
U=K_s,\quad V=K_{s-1},\quad W=K_{s-2},
\qquad B=C|_U:U\to V,\quad F=C|_V:V\to W.
\]
\(s=1\) 时 \(W=0\)，全部涉及它的映射都省略。旧 \(U\) 的合法高度只有零；旧 \(V\) 的最高高度是二，旧 \(W\) 的最高高度是四。

记旧真实归一 MP Gram
\[
L_j=\Gamma_{j,s-1}\quad(j=0,1,2),\qquad
Z_j=\Gamma_{j,s-2}\quad(j=0,\ldots,4),
\qquad L_0=I_V,
\]
并置 \(\Lambda_1=L_1^{-1}\)、\(\Lambda_2=L_2^{-1}\)。令
\[
R=\mathcal J_{1,s-1},\qquad R_- =\mathcal J_{1,s-2},
\qquad T=CR-R_-F=P_VCR:V\to V.
\tag{1.1}
\]
所有逆都在所列合法旧高度；没有定义旧上源 \(U\) 的 \(\Gamma_1\)。

添加一个权 \(a>0\) 的位：\(D_a=d+aE\)。新上出生 \(s\) 的高度是一，新低出生 \(s-1\) 的高度是三。使用同一实际源映射
\[
\mathcal E_a(x,y)=(x-aRy,y),\quad(x,y)\in U\oplus V,
\]
\[
\mathcal F_a(u,v)=(u-aR_-v,v),\quad(u,v)\in V\oplus W.
\tag{1.2}
\]
其物理源度量分别为
\[
H_0(a)=\operatorname{diag}(I_U,I_V+a^2L_1),\qquad
J_0(a)=\operatorname{diag}(I_V,I_W+a^2Z_1).
\tag{1.3}
\]
它们都在 \(a\to0\) 时趋于对应源的恒等，但在任何有限 \(a\) 计算中必须保留。

## 2. 旧硬端需要的三个精确恒等式

定义旧低出生的两个桥创新
\[
\delta_2=\tfrac12(\Lambda_1F^*Z_3-F^*Z_2),\qquad
\delta_3=\tfrac13(\Lambda_2F^*Z_4-\Lambda_1F^*Z_3),
\]
以及
\[
q=B^*L_2,\qquad
\sigma=\tfrac12(F^*Z_2+\Lambda_1F^*Z_3),\qquad
\tau=\sigma+\delta_3.
\tag{2.1}
\]
以下恒等式都来自实际乘积权和真正 MP 塔：
\[
\boxed{T+\sigma F=\Lambda_1-2\Lambda_2L_1,}
\tag{2.2}
\]
\[
\boxed{BB^*L_2=\Lambda_1-4\Lambda_2L_1+\delta_3F,}
\tag{2.3}
\]
\[
\boxed{(\delta_3^*-Z_2F)L_2B=0.}
\tag{2.4}
\]
第三式尤其保留了真实 \(U\to V\to W\) 的来源；不能删除右侧的 \(L_2B\)，把它变成任意低出生向量上的假恒等式。

### 2.1 第一式：同一个三次桥作用于首逆

使用真实两带式
\[
d^*R=2\mathcal J_{2,s-1}\Lambda_2L_1-\mathcal J_{3,s-2}F,
\]
以及
\[
d^2\mathcal J_{3,s-2}
=6R_- -3F^*Z_2-\Lambda_1F^*Z_3,
\]
代入 \(\operatorname{ad}_d^2(d^*)=-2C\)，对 \(R\) 的源使用 \(dR=I\)，再投到 \(V\)，得到
\[
T=\Lambda_1-2\Lambda_2L_1
-\tfrac12(F^*Z_2+\Lambda_1F^*Z_3)F.
\]
这就是 (2.2)。

### 2.2 第二式：保留临界上出生的 Serre 块

在旧硬端，实际两带式给
\[
d^*|_U=-\mathcal J_{2,s-1}B,
\qquad
d^*\mathcal J_{2,s-1}=-\mathcal J_{4,s-2}F,
\qquad
d\mathcal J_{2,s-1}=2R-B^*L_2.
\tag{2.5}
\]
在 \(\operatorname{ad}_d^3(d^*)=0\) 中代入 \(\mathcal J_{2,s-1}\)，并投到 \(V\)。三个非零项分别是
\[
\begin{aligned}
P_Vd^3d^*\mathcal J_{2,s-1}
 &= (12F^*Z_2+4\Lambda_1F^*Z_3+2\Lambda_2F^*Z_4)F,\\
P_Vd^2d^*d\mathcal J_{2,s-1}
 &=8\Lambda_2L_1+2BB^*L_2
   +(6F^*Z_2+2\Lambda_1F^*Z_3)F,\\
P_Vdd^*d^2\mathcal J_{2,s-1}
 &=2(\Lambda_1+F^*Z_2F).
\end{aligned}
\]
以系数 \(1,-3,3\) 合并后，\(F^*Z_2F\) 项相消，所得式恰为 (2.3)。

### 2.3 第三式：对偶升算子支付跨出生硬端抵消

定义真实对偶升、降算子
\[
e=\sum_i b_i^{-1}E_i^*,\qquad A=e^*=\sum_i b_i^{-1}E_i.
\]
它们满足
\[
[d,e]|_{\mathcal H_r}=(2s-2r)I,
\qquad [A,d^*]|_{\mathcal H_r}=(2s-2r)I,
\qquad [A,C]=0.
\tag{2.6}
\]
由有限 \(\mathfrak{sl}_2\) 链的实际代数端点，
\[
eU=0,\qquad eR=\mathcal J_{2,s-1},\qquad
e\mathcal J_{2,s-1}=0,\qquad
e\mathcal J_{3,s-2}=\mathcal J_{4,s-2}.
\tag{2.7}
\]
这些等式不需要把 \(e\) 当成 \(d\) 的物理伴随。为说明最后两条最小逆连接：高度二的完整顶逆是 \(e^2/2\)，\(R-e/2\) 的值在被 \(e\) 消去的 \(U\) 中；高度四的完整顶逆是 \(e^4/24\)，\(\mathcal J_3-e^3/24\) 的值在被 \(e\) 消去的 \(\mathcal J_2(V)\) 中。

记 \(A_U=A|_U:U\to V\)、\(A_V=A|_V:V\to W\)。因为 \(A\) 与 \(d\) 交换，这些范围确在所列 primitive 源。由 (2.7) 与逐塔正交分解，
\[
A\mathcal J_{2,s-1}
=R\Lambda_1L_2+\mathcal J_{2,s-2}A_V.
\tag{2.8}
\]
该式没有 \(U\) 分量，因 \(eU=0\)；最高深度由 \(d^2A\mathcal J_2=2A_V\) 决定。

在 \(U\) 上使用 \([A,d^*]=0\)，结合 (2.5)、(2.8)，比较 \(R(V)\) 分量，得到
\[
\boxed{A_U=-L_2B.}
\tag{2.9}
\]
再在 \(\mathcal J_{2,s-1}(V)\subset\mathcal H_{s+1}\) 上使用 \([A,d^*]=-2I\)，取 \(\mathcal J_{3,s-2}(W)\) 分量。由 \(e\mathcal J_3=\mathcal J_4\)，\(A\mathcal J_4\) 在该塔上的系数是 \(Z_3^{-1}Z_4\)；其余更深分量不参与这个投影。由此得到
\[
-Z_3^{-1}Z_4F+F\Lambda_1L_2-3Z_3^{-1}Z_2A_V=0,
\]
也就是
\[
\boxed{\delta_3^*L_2=-Z_2A_V.}
\tag{2.10}
\]
最后 \([A,C]=0\) 给 \(A_VB=FA_U=-FL_2B\)。将它代入 (2.10) 即得 (2.4)。这完成了不能由单独高度界替代的跨出生抵消。

## 3. 新完整形式与实际桥

新上源的首阶 Gram 形式准确为
\[
H_1(a)=
\begin{pmatrix}
a^{-2}I_U&-a^{-1}q\\
-a^{-1}q^*&L_1+a^2L_2+q^*q
\end{pmatrix}.
\tag{3.1}
\]
这是 [R275 完整一位递推](R275-one-bit-full-primitive-schur-recursion-and-innovation.md)的顶硬约束在新高度一时的同一个解。也可直接求唯一中间层原像：其已占新位分量为 \(a^{-1}x+Ry-qy\)，未占新位分量为 \(-a\mathcal J_{2,s-1}y\)。两部分平方给 (3.1)。其中 \(2UR=q\) 的斜投影关系由 \(d\mathcal J_2=2R-q\) 直接给出。

新低源的第二、第三阶 Gram 形式记为 \(J_2(a),J_3(a)\)。置
\[
P(a)=(L_2^{-1}+a^2L_1^{-1})^{-1},\qquad V(a)=Z_3+a^2Z_4.
\]
同一 R275 全层 MP 递推给
\[
J_2(a)=
\begin{pmatrix}
P(a)&-aP(a)\sigma\\
-a\sigma^*P(a)&Z_2+a^2Z_3+a^2\sigma^*P(a)\sigma
\end{pmatrix},
\tag{3.2}
\]
\[
J_3(a)=
\begin{pmatrix}
a^{-2}L_2&-a^{-1}L_2\tau\\
-a^{-1}\tau^*L_2&V(a)+\tau^*L_2\tau
\end{pmatrix}.
\tag{3.3}
\]
新三次权桥在 (1.2) 两个源中的真实坐标为
\[
\boxed{
\mathcal B_a=
\begin{pmatrix}
B&a(a^2I_V-T)\\0&F
\end{pmatrix}.
}
\tag{3.4}
\]
这是直接展开 \((C+a^3E)\mathcal E_a=\mathcal F_a\mathcal B_a\) 的结果；不是可任意选择的交叉块。

## 4. 先标准化真实首精度，再取弱位极限

记新物理上、下 Gram 为 \(G_1^{a}\)、\(L_j^{a}\)，新上首精度为 \(C_1^{a}=(G_1^{a})^{-1}\)，真实桥为 \(B_a\)。新上出生高度只有一，所以其第二精度按硬顶为零。首加强的标准化费用算子是
\[
\mathcal K_a
=G_1^{a}\Delta_a(L_3^{a})^{-1}\Delta_a^*G_1^{a},
\qquad
\Delta_a=\tfrac12(C_1^{a}B_a^*L_3^{a}-B_a^*L_2^{a}).
\tag{4.1}
\]
因此首加强常数 \(\kappa\) 准确等价于 \(\mathcal K_a\preceq\kappa I\)。

在同源 (1.2) 中，不正交伴随完整抵消后，其二次型是
\[
\boxed{
\mathcal E_a^*\mathcal K_a\mathcal E_a
=\tfrac14 K(a)^*J_3(a)^{-1}K(a),
\qquad
K(a)=J_3(a)\mathcal B_a
-J_2(a)\mathcal B_aH_0(a)^{-1}H_1(a).
}
\tag{4.2}
\]
这一步显式保留 \(H_0^{-1}\)。下源 \(J_0\) 由正确的伴随、算子 Gram 与逆顺序抵消；不能将 \(H_1,J_j\) 直接当成欧氏源上的 Gram 算子。

## 5. Laurent 块中的全部危险项相消

所有旧空间有限维，旧合法 Gram 严格正。以下 \(O(a^m)\) 均指固定旧模型下的算子范数估计。

令
\[
\mathcal A=Bq-T-\tau F.
\]
由 (2.2)、(2.3) 立即得到
\[
\boxed{\mathcal A=-2\Lambda_2L_1.}
\tag{5.1}
\]
展开 \(P(a)=L_2-a^2L_2\Lambda_1L_2+O(a^4)\)，按 (4.2) 的 \(U\oplus V\to V\oplus W\) 块得到
\[
K_{11}(a)=2L_1L_2B+O(a^2),
\qquad
K_{12}(a)=-2a^{-1}L_1+O(a),
\tag{5.2}
\]
\[
K_{21}(a)
=a^{-1}(\sigma^*-\tau^*+Z_2F)L_2B+O(a)=O(a).
\tag{5.3}
\]
最后一步恰使用 (2.4)。这消去了可能在标准化费用中造成 \(a^{-2}\) 发散的真正低块。

对剩下的 \(22\) 块，不应单独估费；与 \(J_3^{-1}\) 的剪切一起完成平方后，有
\[
a\tau^*K_{12}(a)+K_{22}(a)
=Z_3F-Z_2FL_1+O(a^2)
=2\delta_2^*L_1+O(a^2).
\tag{5.4}
\]
核验：其常数项展开为
\[
(\tau^*-\sigma^*)L_2Bq
+Z_3F-Z_2F(L_1+q^*q).
\]
由 \((\tau^*-\sigma^*)L_2B=Z_2FL_2B=Z_2Fq^*\)，第一项正好消去 \(-Z_2Fq^*q\)。因此 (5.4) 仍保同一旧 \(L_1\) 及真实桥来源。

准确逆式给出共同平方
\[
K^*J_3^{-1}K
=a^2K_{1\bullet}^*L_2^{-1}K_{1\bullet}
+(a\tau^*K_{1\bullet}+K_{2\bullet})^*
V(a)^{-1}(a\tau^*K_{1\bullet}+K_{2\bullet}).
\tag{5.5}
\]
将 (5.2)–(5.4) 代入，可见 \(U\) 列的费用是 \(O(a^2)\)，交叉是 \(O(a)\)，\(V\) 列趋于
\[
4L_1\Lambda_2L_1+4L_1\delta_2Z_3^{-1}\delta_2^*L_1.
\]

## 6. 完整范数极限与有限参数蕴含

定义旧低出生首加强的标准化费用
\[
\mathcal K_{\mathrm{old}}
=L_1\bigl(\Lambda_2+\delta_2Z_3^{-1}\delta_2^*\bigr)L_1
\quad\text{在 }V\text{ 上}.
\tag{6.1}
\]
综合以上得到
\[
\boxed{
H_0(a)^{-1/2}\mathcal E_a^*\mathcal K_a\mathcal E_aH_0(a)^{-1/2}
\xrightarrow[a\downarrow0]{\|\cdot\|}
\begin{pmatrix}0_U&0\\0&\mathcal K_{\mathrm{old}}\end{pmatrix}.
}
\tag{6.2}
\]
这里左右确在各自原物理范数的等距源中比较；由于 \(H_0(a)=I+O(a^2)\)，此前的块余项完整保留。

这给出两条准确有限参数结论。

- 若旧 \(V\) 首加强费用满足 \(\|\mathcal K_{\mathrm{old}}\|<\kappa\)，则存在依赖该旧模型和严格余量的 \(a_0>0\)，使全部 \(0<a<a_0\) 的新增硬顶首边满足常数 \(\kappa\)。非严格旧界只能给新费用的极限上界，不能据此宣称每个有限 \(a\) 同常数成立。
- 若某旧 \(y\in V\) 使 \(\langle\mathcal K_{\mathrm{old}}y,y\rangle>\kappa\|y\|^2\)，则由同源 \((0,y)\) 的连续性，所有充分小正 \(a\) 给真实新增硬顶首加强反例。旧源和新源的物理范数都按 (1.3) 支付。

最危险的新增小精度方向对应旧临界 \(U\)，而 (6.2) 中它的标准化费用极限为零。这是实际联合抵消的结论，不是对某个单独 creation 或桥项的粗范数估计。

本文仍未控制任意中间大小的新增权 \(a\)，也没有给原 graph 返回源统一费用。它与既有强位传输互补：这里是任意临界旧池的弱位边界，且剩余费用是旧低出生的**首边**，不把它混同于强位时向更高高度的运输。
