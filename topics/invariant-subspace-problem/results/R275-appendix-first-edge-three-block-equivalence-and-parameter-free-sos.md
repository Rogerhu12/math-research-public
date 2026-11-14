# R275 附录：一位首边的真实三块等价与两条无参数充分式

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit；与 root 共同推导。

**状态。** §§1–5 的精确身份与条件蕴含均已证明；§4 的 (S1)、(S2) 作为一般 Boolean 正性命题仍未证明。它们不是一般首边定理。本文不重新登记任意正权出生一的首边：该结论及其倒数权末边已由 [R271](R271-appendix-universal-birth-one-first-adjacent-primitive-gram-bound.md) 完成。全文的 Gram 是真正的 primitive Gram，不能替代原 graph 首物理头的 Gram。

## 1. 同源空间和完整最小逆

取旧 $M$ 位正权下降算子 $d=\sum_{i=1}^{M}b_iE_i$，新位权 $a>0$，$t=a^2$。固定新出生 $s\ge1$，要求
$$
M+1\ge2s+2,\qquad \ell=M-2s\ge1.
$$
令
$$
K=\ker d\cap\mathcal H_s,\qquad L=\ker d\cap\mathcal H_{s-1},\qquad R=d_s^\dagger|_L.
$$
一切伴随和单位算子使用实际物理 Hilbert 范数，$K_r=\ker d\cap\mathcal H_r$。在任意正交基中，定义旧归一最小逆 Gram
$$
G_j=\mathcal J_{j,s}^*\mathcal J_{j,s},\qquad
L_j=\mathcal J_{j,s-1}^*\mathcal J_{j,s-1},\qquad
\mathcal J_{j,r}=(d^j/j!)^\dagger|_{K_r}.
$$
于是 $G_0=I_K$、$L_0=I_L$、$R^*R=L_1$。旧上出生合法高度为 $0,\ldots,\ell$，旧下出生合法高度为 $0,\ldots,\ell+2$，所以 $G_1,L_1,L_2,L_3$ 始终正定。记
$$
C_1=G_1^{-1},\qquad
C_2=\begin{cases}G_2^{-1},&\ell\ge2,\\0,&\ell=1,\end{cases}
\qquad F=C_1^2-C_2.
\tag{1.1}
$$
$\ell=1$ 的零精度是旧顶硬端的准确约定，不是假设存在 $G_2$。

共同三次桥为
$$
B=\left(\sum_i b_i^3E_i\right)\big|_K:K\longrightarrow L.
$$
它确实取值于 $L$，因为该三次下降与 $d$ 交换。令
$$
Q=B^*L_2,\qquad
\Delta=\frac12(C_1B^*L_3-B^*L_2),\qquad
V_j=L_j+tL_{j+1}\quad(j=0,1,2).
\tag{1.2}
$$
这些定义直接来自 [R275](R275-one-bit-full-primitive-schur-recursion-and-innovation.md) 的完整一位递推及真实三次创新：首剪切为 $Q_1=Q$，下一剪切为 $Q_2=Q+\Delta$。

新 primitive 空间以同一个可逆源映射
$$
E(x,y)=(x-aRy,y),\qquad (x,y)\in K\oplus L
$$
表示。若新实际 primitive Gram 为 $\Gamma_j^{\rm new}$，置
$H_j=E^*\Gamma_j^{\rm new}E$。完整一位公式给
$$
H_0=\operatorname{diag}(I,V_0),
$$
$$
H_j=S_j^*\operatorname{diag}(P_j,V_j)S_j,\qquad
S_j=\begin{pmatrix}I&-aQ_j\\0&I\end{pmatrix}\quad(j=1,2),
\tag{1.3}
$$
其中
$$
P_1=(C_1+tI)^{-1},\qquad P_2=(C_2+tC_1)^{-1}.
\tag{1.4}
$$
当 $\ell=1$，第二式准确变为 $P_2=t^{-1}G_1$，仍是实际新最高层。

## 2. 首边与真实三块矩阵完全等价

同源可逆同余保持相邻不等式。因此新首边正性准确等价于
$$
H_1H_2^{-1}H_1\preceq H_0.
\tag{2.1}
$$
对三式共同作 $S_1^{-1}$ 的同余，得到
$$
\widetilde H_0=\begin{pmatrix}I&aQ\\aQ^*&V_0+tQ^*Q\end{pmatrix},\quad
\widetilde H_1=\operatorname{diag}(P_1,V_1),
$$
$$
\widetilde H_2=
\begin{pmatrix}I&0\\-a\Delta^*&I\end{pmatrix}
\begin{pmatrix}P_2&0\\0&V_2\end{pmatrix}
\begin{pmatrix}I&-a\Delta\\0&I\end{pmatrix}.
$$
于是
$$
\widetilde H_2^{-1}=
\begin{pmatrix}
P_2^{-1}+t\Delta V_2^{-1}\Delta^*&a\Delta V_2^{-1}\\
aV_2^{-1}\Delta^*&V_2^{-1}
\end{pmatrix}.
$$
再对首边差作 $\operatorname{diag}(P_1^{-1},I)$ 同余，并使用
$$
P_1^{-2}-P_2^{-1}=F+tC_1+t^2I,
$$
得下面三块矩阵关于 $V_2>0$ 的 Schur 补。因此 (2.1) 当且仅当
$$
\boxed{
M(t)=
\begin{pmatrix}
F+tC_1+t^2I&\sqrt t(C_1+tI)Q&\sqrt t\Delta\\
\sqrt tQ^*(C_1+tI)&I+tL_1+tQ^*Q&L_1+tL_2\\
\sqrt t\Delta^*&L_1+tL_2&L_2+tL_3
\end{pmatrix}\succeq0.
}
\tag{2.2}
$$
没有把交叉项分开估计，也没有要求各矩阵交换。

## 3. 去掉一个明确平方后的更强铅笔

令 $W_t:K\to K\oplus L\oplus L$ 为
$$
W_tx=(tx,\sqrt t\,Q^*x,0).
$$
准确相减得到
$$
\boxed{
P(t):=M(t)-W_tW_t^*=
\begin{pmatrix}
F+tC_1&\sqrt t\,C_1Q&\sqrt t\Delta\\
\sqrt t\,Q^*C_1&I+tL_1&L_1+tL_2\\
\sqrt t\Delta^*&L_1+tL_2&L_2+tL_3
\end{pmatrix}.
}
\tag{3.1}
$$
所以 $P(t)\succeq0$ 对真实首边是充分条件；没有声称它是必要条件。

记
$$
Z_0=\begin{pmatrix}I&L_1\\L_1&L_2\end{pmatrix},\qquad
Z_1=\begin{pmatrix}L_1&L_2\\L_2&L_3\end{pmatrix},\qquad
\mathscr R=[C_1Q,\Delta].
$$
则
$$
P(t)=\begin{pmatrix}F+tC_1&\sqrt t\,\mathscr R\\
\sqrt t\,\mathscr R^*&Z_0+tZ_1\end{pmatrix}.
\tag{3.2}
$$
**量词边界。** 若 $P(t)\succeq0$ 对全部 $t>0$ 成立，则其右下块除以 $t$ 并取 $t\to\infty$ 给 $Z_1\succeq0$。这正是旧下出生的第二处相邻边
$$
L_2L_3^{-1}L_2\preceq L_1.
\tag{3.3}
$$
因此不能仅假设旧首边，再由 (3.1) 声称完成关于位数的一般首边归纳。可以在 R275 原先的旧两出生全高度常数一假设下使用它；如要闭合全部高度，仍须给其余高度相应的完整创新控制。

## 4. 两条无参数的充分式，保留奇异情形

定义
$$
E_1=\Delta L_3^{-1}L_2,\qquad
A=C_1Q-E_1
=\frac12(C_1B^*L_2+B^*L_2L_3^{-1}L_2).
\tag{4.1}
$$
这里 $L_3>0$ 是实际低出生的合法完整 Gram；不会要求 $Z_0$ 或 $Z_1$ 可逆。

提出两条**尚未在一般 Boolean 中证明**的同源充分式：
$$
\boxed{
\begin{pmatrix}F&\Delta\\\Delta^*&L_3\end{pmatrix}\succeq0
}
\quad\Longleftrightarrow\quad
\Delta L_3^{-1}\Delta^*\preceq F,
\tag{S1}
$$
以及
$$
\boxed{
\begin{pmatrix}
C_1&A&0\\A^*&I&L_1\\0&L_1&L_2
\end{pmatrix}\succeq0
}
\quad\Longleftrightarrow\quad
A^*G_1A+L_1L_2^{-1}L_1\preceq I.
\tag{S2}
$$
后一等价只消去真正正定的 $C_1$ 和 $L_2$，没有使用 $Z_0^{-1}$。特别，(S2) 本身就蕴含 $Z_0\succeq0$。

**已证明的条件结论。** 若旧下出生有 (3.3)，且 (S1)、(S2) 成立，则 $P(t)\succeq0$ 对每个 $t\ge0$ 成立，因而对每个新正权 $a$ 的真实首边成立。

**证明。** 分拆
$$
\mathscr R=\mathscr R_0+\mathscr R_1,\qquad
\mathscr R_0=[A,0],\qquad \mathscr R_1=[E_1,\Delta].
$$
令 $S=[0,\Delta L_3^{-1}]$。则
$$
\mathscr R_1=SZ_1,\qquad SZ_1S^*=\Delta L_3^{-1}\Delta^*.
$$
所以在 $Z_1\succeq0$ 和 (S1) 下，
$$
\begin{pmatrix}F&\mathscr R_1\\\mathscr R_1^*&Z_1\end{pmatrix}
=
\begin{pmatrix}F-\Delta L_3^{-1}\Delta^*&0\\0&0\end{pmatrix}
+\begin{pmatrix}S\\I\end{pmatrix}Z_1\begin{pmatrix}S^*&I\end{pmatrix}
\succeq0.
\tag{4.2}
$$
(S2) 则恰是
$$
\begin{pmatrix}C_1&\mathscr R_0\\\mathscr R_0^*&Z_0\end{pmatrix}\succeq0.
\tag{4.3}
$$
取 $J_0(t)=\operatorname{diag}(\sqrt t I_K,I_{L\oplus L})$、
$J_1(t)=\operatorname{diag}(I_K,\sqrt t I_{L\oplus L})$，逐块相加给完整平方分解
$$
P(t)=J_0(t)
\begin{pmatrix}C_1&\mathscr R_0\\\mathscr R_0^*&Z_0\end{pmatrix}J_0(t)^*
+J_1(t)
\begin{pmatrix}F&\mathscr R_1\\\mathscr R_1^*&Z_1\end{pmatrix}J_1(t)^*.
\tag{4.4}
$$
这证明结论，包括 $Z_0,Z_1$ 奇异及 $t=0$ 的情况。$\square$

## 5. 两条候选的真实几何与占据身份

### 5.1 第二条是一个同层两分量收缩

两个完整最小逆的范围 $\operatorname{Ran}\mathcal J_{1,s}$ 与 $\operatorname{Ran}\mathcal J_{2,s-1}$ 位于同一物理层 $\mathcal H_{s+1}$，且属于不同出生的正交塔。因此对 $y\in L$，
$$
\mathcal T y=\mathcal J_{1,s}Ay+
\mathcal J_{2,s-1}L_2^{-1}L_1y
$$
满足
$$
\|\mathcal T y\|^2=
\langle (A^*G_1A+L_1L_2^{-1}L_1)y,y\rangle.
\tag{5.1}
$$
故 (S2) 恰是 $\|\mathcal T\|\le1$。这只是把缺口写成实际同层的收缩命题，尚未识别出自动保证此收缩的正交投影或正 Gram。

### 5.2 第一条须保留精确低出生 Schur 项

令
$$
H=[d,d^*],\quad H_0=P_KH|_K,\quad
H_1=\mathcal J_{1,s}^*H\mathcal J_{1,s},\quad
M_j=B^*L_jB,\quad N=B^*L_2L_3^{-1}L_2B.
$$
由 [联合占据附录](R275-appendix-joint-occupation-blocks-and-first-edge-necessary-bound.md) 的真正两带身份，
$$
H_0=C_1+M_2,\qquad H_1=4G_1C_2G_1-I+M_3.
$$
这在 $\ell=1$ 时也成立，按 $C_2=0$ 使用旧顶硬端。于是直接展开 (S1) 的差，得
$$
\boxed{
4(F-\Delta L_3^{-1}\Delta^*)
=C_1^2+C_1H_0+H_0C_1-C_1H_1C_1-N.
}
\tag{5.2}
$$
旧下出生第二边只给 $N\preceq M_1$；把右侧的 $N$ 换成较大的 $M_1$ 是更强且可能失去正确符号的命题，不能把这个替换当作支付创新。

## 6. 低出生为零时的精确边际差形式；不重计旧首边

此节仅帮助识别 (S1)、(S2) 的特殊结构，不宣称任一候选已闭。令旧上出生 $s=1$，于是 $L$ 为真空直线。记
$$
z_i=b_i^2,\quad S=e_1(z),\quad Z=e_2(z),\quad W=e_3(z),\quad
b=(b_i),\quad T=\operatorname{diag}(z_i),
$$
$$
u=(S-T)b,\qquad v=(Z-ST+T^2)b.
$$
则 $L_1=S^{-1}$、$L_2=Z^{-1}$、$L_3=W^{-1}$。在整个一孔层把 $C_1$ 以零延拓于 $\mathbb Cb$，R271 的真实条件协方差公式为
$$
C_1=SI-2T+bb^*-\frac{uu^*}{Z},\qquad
B^*=P_{b^\perp}Tb.
$$
利用 $\sum z_i^2=S^2-2Z$、$\sum z_i^3=S^3-3SZ+3W$，直接得到
$$
C_1B^*=-2v+\frac{3W}{Z}u,
$$
$$
\boxed{\Delta=-\frac vW+\frac{2u}{Z}-\frac bS,\qquad
A=-\frac vZ+\frac W{Z^2}u+\frac W{SZ}b.}
\tag{6.1}
$$
两向量都属于 $b^\perp$。第一式正是带物理去权的条件子集边际均值二阶差；(S1) 在此变为 $F-W\Delta\Delta^*\succeq0$，即旧首边余量须再支付一个明确秩一项。(S2) 则变为
$$
A^*G_1A+\frac Z{S^2}\le1.
\tag{6.2}
$$
R271 已证明任意正权 $s=1$ 的 $F\succeq0$（合法首边实际严格），但该结论本身不推出再扣秩一项的 (S1)，也不直接推出 (6.2)。即使以后证明本节候选，也不能把已有出生一首边当成新增结论。

## 7. 当前准确未解事项

本文保留了从真实首边到 (2.2) 的等价、从 (S1)、(S2)、旧低出生第二边到真实首边的完整充分证明，以及两候选的实际同源表达。尚未证明任意正乘积权、任意出生下的 (S1) 或 (S2)，也没有证明更强的 $P(t)$ 必然为正。小规模浮点探索不构成这里任何一个一般正性定理。

若这两个候选中有一个在实际 Boolean 模型中失败，应保留实际反例并返回 (2.2) 的完整平方，不能据此否定原首边；若二者均能证明，也仍须处理 (3.3) 的跨高度归纳依赖和全部其余高度，不能跳到一般常数一或普通 ISP 完成。

## 8. 有限小探的保存范围

[短探脚本](../notes/2026-11-14-one-bit-first-edge-pencil-probe-789f.py)及[原始输出](../notes/2026-11-14-one-bit-first-edge-pencil-probe-789f.jsonl)保存六个合法旧位数/出生组合、固定种子7892785下420组独立正权与每组九个t的浮点探索；P(t)跨块归一比最大约0.381225，未发现失败。其用途仅为筛选这个更强充分条件；不证明P、S1、S2或一般首边，且不是对完整参数空间的优化。
