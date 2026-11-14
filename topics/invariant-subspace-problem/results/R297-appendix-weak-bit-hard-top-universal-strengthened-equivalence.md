# 弱位有限反例传输：全部加强高度等价于奇数硬端首边

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：下列范数极限、有限反例传输与同常数量词等价已证明；硬端首边的统一有限常数仍未证明。** 本文使用刚付清的任意临界旧池弱位抵消，封住唯一奇异的高度二到高度一转换。没有从参数边界连续性推出某个有限权区间或整个内部都正。

## 1. 统一定义实际首加强费用

对任意有限正权 Boolean 行 \(d=\sum_{i=1}^M b_iE_i\)，固定出生 \(r\ge0\)、合法高度 \(h=M-2r\ge1\)。记
\[
G_j=\Gamma_{j,r},\quad C_1=G_1^{-1},
\quad C_2=G_2^{-1}\ (h\ge2),
\]
而 \(h=1\) 时仅在精度端置 \(C_2=0\)。令
\[
B=\left(\sum_i b_i^3E_i\right)|_{K_r}:K_r\to K_{r-1},
\qquad L_j=\Gamma_{j,r-1},
\]
出生零时这些低出生项均为零。定义
\[
\Delta=\tfrac12(C_1B^*L_3-B^*L_2),
\qquad
\boxed{\mathscr K(d,r)=G_1(C_2+\Delta L_3^{-1}\Delta^*)G_1.}
\tag{1.1}
\]
\(\mathscr K\) 是真实物理 \(K_r\) 上的正算子。对任何 \(\kappa>0\)，首加强不等式恰为
\[
\mathscr K(d,r)\preceq\kappa I_{K_r}.
\tag{1.2}
\]
所有 \(\Gamma_j\) 都是 \(d^j/j!\) 的完整层 MP Gram，不是原 graph 返回 Gram。

## 2. 加入弱位，同时提高出生

若旧高度 \(h\ge2\)，加入一个权 \(a>0\) 的新位，取
\[
D_a=d+aE,\qquad r'=r+1,\qquad h'=h-1.
\]
新 primitive 源的固定坐标是
\[
U=K_{r+1}(d),\qquad V=K_r(d),\qquad
\mathcal E_a(x,y)=(x-aRy,y),\quad R=\mathcal J_{1,r}(d).
\tag{2.1}
\]
其物理源度量为
\[
H_0(a)=\mathcal E_a^*\mathcal E_a
=\operatorname{diag}(I_U,I_V+a^2G_1).
\tag{2.2}
\]
因此 \(\mathcal U_a=\mathcal E_aH_0(a)^{-1/2}\) 是从同一个 \(U\oplus V\) 到新物理源的等距同构。

### 定理 1：任意旧高度的弱位首费用极限

如果 \(h\ge3\)，则
\[
\boxed{
\mathcal U_a^*\mathscr K(D_a,r+1)\mathcal U_a
\xrightarrow[a\downarrow0]{\|\cdot\|}
\operatorname{diag}\bigl(\mathscr K(d,r+1),\mathscr K(d,r)\bigr).
}
\tag{2.3}
\]
左上旧源的高度为 \(h-2\ge1\)；当 \(h=3\) 时它使用真正硬端 \(C_2=0\)。

如果 \(h=2\)，则
\[
\boxed{
\mathcal U_a^*\mathscr K(D_a,r+1)\mathcal U_a
\xrightarrow[a\downarrow0]{\|\cdot\|}
\operatorname{diag}\bigl(0_U,\mathscr K(d,r)\bigr).
}
\tag{2.4}
\]
此时旧 \(U\) 只有高度零，不能写一个不存在的 \(\mathscr K(d,r+1)\)；零块是联合抵消的结论。

## 3. 非奇异高度的完整源证明

证明 (2.3)。旧 \(U\) 的高度至少一。按 [R275 完整一位公式](R275-one-bit-full-primitive-schur-recursion-and-innovation.md)，用 \(A_j\) 表示旧 \(U\) 的精度；\(A_0=I\)、\(A_1>0\)，并允许在旧高度一时 \(A_2=0\)。新上源前两阶形式 \(H_j(a)\) 的逆准确为
\[
H_j(a)^{-1}=
\begin{pmatrix}
P_j(a)^{-1}+a^2q_jV_j(a)^{-1}q_j^*&aq_jV_j(a)^{-1}\\
aV_j(a)^{-1}q_j^*&V_j(a)^{-1}
\end{pmatrix},
\tag{3.1}
\]
其中 \(q_j\) 是固定旧模型的真实剪切，
\[
P_1(a)^{-1}=A_1+a^2I,
\qquad P_2(a)^{-1}=A_2+a^2A_1,
\]
\[
V_j(a)=G_j+a^2G_{j+1}\quad(j=1,2).
\tag{3.2}
\]
当 \(h=3\) 时，\(P_2=a^{-2}A_1^{-1}\) 是准确顶硬约束；式 (3.1) 仍是合法完整逆，不能通过写一个有限的旧上源 \(G_2\) 来替代它。

由此
\[
H_1(a)\to\operatorname{diag}(A_1^{-1},G_1),
\qquad
H_2(a)^{-1}\to\operatorname{diag}(A_2,G_2^{-1}).
\tag{3.3}
\]
在同一个源中，新 \(\Gamma_1\) 的算子坐标是 \(H_0^{-1}H_1\)，新第二精度的算子坐标是 \(H_2^{-1}H_0\)。所以 (3.3) 连同 \(H_0\to I\) 保留了原源伴随次序。

新低出生的源是 \(V\oplus K_{r-1}\)，其源度量也趋于恒等。因为旧 \(V\) 的高度 \(h\ge3\)，它的第二、第三 Gram 都合法，故新低出生的这两阶完整形式分别趋于
\[
\operatorname{diag}(G_2,L_2),\qquad
\operatorname{diag}(G_3,L_3),
\tag{3.4}
\]
后者是固定严格正矩阵。实际三次桥的坐标为
\[
\begin{pmatrix}
B_U&a(a^2I-T)\\0&B_V
\end{pmatrix}
\longrightarrow\operatorname{diag}(B_U,B_V),
\tag{3.5}
\]
其中 \(B_U=C|_U\)、\(B_V=C|_V\)，\(T\) 是固定旧 MP 源给出的真实块。

(1.1) 所需的全部源矩阵、合法逆、第二精度和桥因此按正确次序收敛。第二精度左上角允许趋于零，无需取其逆。最后由 \(H_0^{-1/2}\) 作真正等距源同余，得到 (2.3)。

对于 \(h=2\)，上述步骤中 \(H_1\) 的旧上源块会发散，不能套用非奇异连续性。这正是[弱位临界池首 S1 稿](R297-weak-bit-critical-pool-cancellation-and-first-edge-transfer.md)的情形：旧位数为 \(2(r+1)\)，旧 \(U\) 临界。该稿保全部上下源度量，利用对偶升算子、跨出生硬端恒等式及共同剪切平方，证明标准化费用趋于 (2.4)。这补全定理 1 的全部高度。

## 4. 严格反例总能在有限正参数下传到硬端

固定 \(\kappa>0\)。假设某有限正权模型有单位 \(y\in K_r\) 满足
\[
\langle\mathscr K(d,r)y,y\rangle>\kappa.
\tag{4.1}
\]
如果 \(h\ge2\)，(2.3) 或 (2.4) 对同一标准源向量 \((0,y)\) 的范数收敛给出一个有限 \(a_0>0\)，使每个 \(0<a<a_0\) 都有
\[
\left\langle
\mathscr K(D_a,r+1)\mathcal U_a(0,y),
\mathcal U_a(0,y)
\right\rangle>\kappa.
\tag{4.2}
\]
\(\mathcal U_a(0,y)\) 是新原物理范数中的单位向量。参数始终严格正，没有把零权极限当作有限反例。

每次先固定已经选出的有限模型和仍严格的见证，再选择下一次足够小的正权；因此可迭代 \(h-1\) 次。最终
\[
M'=M+h-1=2M-2r-1,
\qquad r'=r+h-1=M-r-1,
\qquad M'=2r'+1,
\tag{4.3}
\]
最终高度恰为一，且同一个 \(\kappa\) 仍被严格违反。这里各阈值可以依赖旧权和严格余量；量词不要求对全部旧模型预先指定一个弱权。

## 5. 全部加强问题同常数等价于奇数硬端首边

对固定 \(\kappa>0\)，以下三种全称陈述等价。

1. 对全部有限正权及全部合法出生，首加强费用满足 \(\mathscr K(d,r)\preceq\kappa I\)。
2. 只对全部奇数位数硬端 \(M=2r+1\)、全部正权，首加强费用满足 \(\mathscr K(d,r)\preceq\kappa I\)。
3. 对全部有限正权、出生及合法高度，全部加强相邻式以同一 \(\kappa\) 成立。

第一条蕴含第二条是取子类；第二条蕴含第一条由第 4 节严格反例传输的逆否命题。这里非严格正序失败总存在严格负方向，因而没有遗漏等号情形。

第一条与第三条的同常数等价，已经由 [R293 全高度强位传输](R293-appendix-all-height-strengthened-s1-heavy-bit-equivalence.md)证明；其中一般 \(\kappa\) 的真正上源 Schur 和硬顶已经保留。将其与本稿弱位传输合并，才得到上述三条等价。

因此，为证明一个与位数、出生和权无关的有限常数，**只须处理任意正权的奇数硬端首边**。该硬端中 \(C_2=0\)，目标准确是
\[
\boxed{
\left\|L_3^{-1/2}\Delta^*C_1^{-1}\right\|^2\le\kappa,
\qquad M=2r+1.
}
\tag{5.1}
\]
反过来，若 (5.1) 的普适常数不存在，全部加强问题也没有普适常数。任何已付的有限 \(\kappa\) 会给普通相邻 Gram 序同一常数，但仍不自动支付原 graph 首物理头或 ISP 完成标准。

## 6. 这个归约没有证明什么

本稿没有证明 (5.1)，也没有利用边界连续性宣布任意中间权正性。它真正减少的是需要证明的全称模型类，同时完整保留固定物理源、所有合法逆、唯一奇异弱位转换以及有限正参数的反例见证。

下一项数学需求已可精确固定为：在 \(M=2r+1\) 的完整正权模型中，用真实对偶升降关系控制 (5.1) 的共同创新算子；上出生普通第二高度在这里不存在，不能作为额外假设。
