# R284：跨出生的真实零占据 Gram 与二阶联合费用的精确 Schur 接续

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core；前三阶交叉身份与 literature_audit 独立推导一致。

**状态。** 本文证明两个实际跨出生零占据 Gram 正块，并从第二块得到保留高出生三次桥的二阶费用下界。它们把 [R275 的首边三块接口](R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md) 中的 $Q,\Delta$ 接到 [真正硬核联合最小化](../notes/2026-11-14-bosonic-hardcore-first-edge-789f-next.md) 的零占据费用。一般 (S1)、(S2) 仍未证明，本文不据此断言一般首边或普通 ISP 完成。

## 1. 完整层、单位归一与合法高度

取 $M$ 个正权，先统一归一到
$$
D=\sum_{i=1}^M b_iE_i,\qquad b_i>0,\qquad \sum_i b_i^2=1.
$$
所有空间和范数都是标准 Boolean 平方自由物理层及其原 Hilbert 范数。固定 $s\ge1$，记
$$
K=K_s=\ker D\cap\mathcal H_s,\qquad
L=K_{s-1},\qquad \ell=M-2s.
$$
第一块只需 $\ell\ge1$；第二块要求 $\ell\ge2$。定义完整归一最小逆
$$
\mathcal J_{j,r}=(D^j/j!)^\dagger\big|_{K_r},\qquad
G_j=\mathcal J_{j,s}^*\mathcal J_{j,s},\qquad
L_j=\mathcal J_{j,s-1}^*\mathcal J_{j,s-1}.
$$
这里始终先在完整实际目标层上取 Moore–Penrose 逆，再限制源到 $K_r$。在所列合法高度，有限正权 Boolean 完整幂均满射，所以这些 Gram 为正定。$G_0=I_K$、$L_0=I_L$。

置
$$
C_1=G_1^{-1},\qquad
B=\left(\sum_i b_i^3E_i\right)\big|_{K}:K\longrightarrow L,
$$
$$
Q=B^*L_2,\qquad
\Theta=C_1B^*L_3,\qquad
\Delta=\frac{\Theta-Q}{2},\qquad H=G_1-I.
\tag{1.1}
$$
这些正是 R275 同源首剪切和相邻创新；没有重新选 primitive 源基。$B$ 的取值域合法，因为 $\sum b_i^3E_i$ 与 $D$ 交换。

把 Boolean 空间等距嵌入 $M$ 模式 bosonic Fock 空间的硬核部分。令
$$
a_0=\sum_i b_i a_i,
$$
则 $a_0$ 是单位 bosonic 模式，且 $a_0|_{\mathcal H}=D$。以该模式的 occupation 分解完整 Fock 空间。记 $P_0$ 为 occupation 为零的正交投影，并定义
$$
U_r=P_0\mathcal J_{1,r},\qquad
Z_{j,r}=P_0\mathcal J_{j,r}\quad(j\ge2).
\tag{1.2}
$$
这些是实际最小逆的零占据分量，通常不再是 Boolean 向量。所有交叉内积都在同一个完整 transverse Fock 层内计算。

在固定实际物理层 $\mathcal H_p$ 上，这个共同 Gram 无需显式构造旋转后的 Fock 基。准确的真空投影压缩为
$$
\boxed{\mathsf E_p:=P_{\mathcal H_p}P_0|_{\mathcal H_p}
=\sum_{m=0}^p\frac{(-1)^m}{m!}(D^*)^mD^m,\qquad
0\preceq\mathsf E_p\preceq I.}
\tag{1.3}
$$
这里每个 $(D^*)^m$ 是从实际低层返回 $\mathcal H_p$ 的完整物理伴随幂。在整个 occupation $n$ 空间上，右边对应的未压缩算子作用为
$\sum_{m=0}^n(-1)^m\binom nm=1_{\{n=0\}}$；又 $a_0^m$ 保持硬核部分，所以压缩后准确得到 (1.3)。因此对处于同一个物理层的任意两个最小逆映射 $J,J'$，
$$
(P_0J)^*(P_0J')
=J^*\mathsf E_pJ'
=\sum_{m=0}^p\frac{(-1)^m}{m!}(D^mJ)^*(D^mJ').
\tag{1.4}
$$
后文的正块是这个实际同层投影的 Gram；交替符号和不能逐项按正性拆开。

## 2. 所需两下降身份的自足证明

Boolean 平方零关系直接给
$$
[D,[D,D^*]]=-2\mathcal C,\qquad
\mathcal C=\sum_i b_i^3E_i,\qquad
[D,\mathcal C]=0.
\tag{2.1}
$$
特别 $\operatorname{ad}_D^3(D^*)=0$。

### 2.1 二阶下降

对任意合法出生 $r$，令 $B_r=\mathcal C|_{K_{r+1}}:K_{r+1}\to K_r$，并令 $\Gamma_{2,r}=\mathcal J_{2,r}^*\mathcal J_{2,r}$。则
$$
\boxed{D\mathcal J_{2,r}=2\mathcal J_{1,r}-B_r^*\Gamma_{2,r}.}
\tag{2.2}
$$
证明：左边减去 $2\mathcal J_{1,r}$ 后落在 $K_{r+1}$。若 $x\in K_{r+1}$，则 (2.1) 给
$$
\frac{D^2}{2}D^*x=-\mathcal Cx=-B_rx.
$$
因此 $D^*x$ 投到完整 $\operatorname{Ran}(D^*)^2$ 的正交投影准确是 $-\mathcal J_{2,r}B_rx$。与 $\mathcal J_{2,r}y$ 配对，即得到剩余 $K_{r+1}$ 分量为 $-B_r^*\Gamma_{2,r}y$。这里投影使用的是完整幂的最小逆。

### 2.2 下出生三阶下降

在本文记号下，
$$
\boxed{D\mathcal J_{3,s-1}=3\mathcal J_{2,s-1}-\mathcal J_{1,s}\Theta.}
\tag{2.3}
$$
先由 $D^3\mathcal J_{3,s-1}=6I$，知差向量属于 $\ker D^2\cap\mathcal H_{s+1}$。它还正交于 $K_{s+1}$：对 $z\in K_{s+1}$，(2.1) 给 $D^3D^*z=0$，故 $D^*z\perp\operatorname{Ran}(D^*)^3$。因此该差属于 $\operatorname{Ran}\mathcal J_{1,s}$。

对 $x\in K$，由 $D\mathcal J_{1,s}x=x$、$D^2\mathcal J_{1,s}x=0$ 和 (2.1)，
$$
\frac{D^3}{6}D^*\mathcal J_{1,s}x=-Bx.
$$
故 $D^*\mathcal J_{1,s}x$ 在完整 $\operatorname{Ran}(D^*)^3$ 上的投影为 $-\mathcal J_{3,s-1}Bx$。又 $\mathcal J_{1,s}\perp\mathcal J_{2,s-1}$，配对后余项系数 $v$ 满足
$$
G_1v=-B^*L_3y,
$$
即 $v=-\Theta y$，证明 (2.3)。这里使用的正交性是完整塔的实际正交：$\mathcal J_{1,s}$ 的像属于 $\ker D^2$，而 $\mathcal J_{2,s-1}$ 的像正交于 $\ker D^2$。

## 3. 第一/第二层共同零占据块

由 $D\mathcal J_{1,r}=I$ 及 primitive 源的 occupation 为零，
$$
\mathcal J_{1,r}=|1\rangle I+|0\rangle U_r,\qquad
U_r^*U_r=\Gamma_{1,r}-I.
\tag{3.1}
$$
而 (2.2) 在下出生给
$$
\mathcal J_{2,s-1}
=\sqrt2\,|2\rangle I
+|1\rangle(2U_{s-1}-Q)+|0\rangle Z_{2,s-1}.
\tag{3.2}
$$
有 $U_{s-1}\perp K$：因为 $\mathcal J_{1,s-1}$ 正交于其完整目标层的 $\ker D=K$，且 $K$ 完全位于 occupation 为零部分。因此 $U_{s-1}^*Q=0$。

不同出生的 $\mathcal J_{1,s}$ 与 $\mathcal J_{2,s-1}$ 位于同一物理层并正交。将 (3.1)、(3.2) 按 occupation 配对，得到第一条真实交叉身份
$$
\boxed{U_s^*Z_{2,s-1}=Q=B^*L_2.}
\tag{3.3}
$$
对 (3.2) 取 Gram 又得
$$
\boxed{Y_2:=Z_{2,s-1}^*Z_{2,s-1}=L_2-4L_1+2I-Q^*Q.}
\tag{3.4}
$$
所以在同一 transverse degree $s+1$ 中，实际联合零占据 Gram 正块为
$$
\boxed{
\begin{pmatrix}
G_1-I&Q\\
Q^*&L_2-4L_1+2I-Q^*Q
\end{pmatrix}
=\begin{pmatrix}U_s^*\\Z_{2,s-1}^*\end{pmatrix}
\begin{pmatrix}U_s&Z_{2,s-1}\end{pmatrix}
\succeq0.
}
\tag{3.5}
$$
它保留三次桥与两边零占据费用的共同度量。

令 $H=G_1-I\succeq0$。有限维 Gram 的真实范围关系给
$\operatorname{Ran}Q\subseteq\operatorname{Ran}H$，故 (3.5) 等价于
$$
Y_2\succeq Q^*H^\dagger Q,
$$
连同该范围条件。于是
$$
\boxed{L_2-4L_1+2I\succeq Q^*(I+H^\dagger)Q.}
\tag{3.6}
$$
当 $H>0$ 时，右边也可写作 $Q^*(I-C_1)^{-1}Q$，因为
$$
I+H^{-1}=G_1(G_1-I)^{-1}=(I-C_1)^{-1}.
$$
若 $H$ 奇异，保留 (3.5) 或带范围条件的 (3.6)，不把普通逆强行延拓。

## 4. 第二/第三层共同零占据块

此节要求 $\ell\ge2$，从而上出生的 $\mathcal J_{2,s}$ 是合法完整最小逆。令
$$
B_s=\mathcal C|_{K_{s+1}}:K_{s+1}\longrightarrow K,\qquad
V_s=-B_s^*G_2.
$$
由 (2.2)，
$$
\mathcal J_{2,s}
=\sqrt2\,|2\rangle I+|1\rangle(2U_s+V_s)+|0\rangle Z_{2,s}.
\tag{4.1}
$$
$U_s\perp K_{s+1}$，而 $V_s$ 的像在 $K_{s+1}$，故
$$
\boxed{X_2:=Z_{2,s}^*Z_{2,s}
=G_2-4G_1+2I-G_2B_sB_s^*G_2.}
\tag{4.2}
$$
这正是二阶硬核联合最小化在扣除高出生分量后的实际零占据费用。

由 (2.2)、(2.3) 再下降一次，
$$
D^2\mathcal J_{3,s-1}=6\mathcal J_{1,s-1}-3Q-\Theta.
$$
所以三阶最小逆的完整 occupation 展开为
$$
\begin{aligned}
\mathcal J_{3,s-1}={}&\sqrt6\,|3\rangle I\\
&+\frac1{\sqrt2}|2\rangle(6U_{s-1}-3Q-\Theta)\\
&+|1\rangle(3Z_{2,s-1}-U_s\Theta)
+|0\rangle Z_{3,s-1}.
\end{aligned}
\tag{4.3}
$$
此外 $Z_{2,s-1}\perp K_{s+1}$：$\mathcal J_{2,s-1}$ 的像正交于完整 $\ker D^2$，其中包括 $K_{s+1}$，而后者 occupation 为零。因此 (4.1) 中 $V_s$ 与 (4.3) 的整个 occupation 一系数正交。

现在 $\mathcal J_{2,s}\perp\mathcal J_{3,s-1}$，因为前者的像在 $\ker D^3$ 中，后者的像正交于完整 $\ker D^3$。按 occupation 配对，并使用 (3.3)，得到
$$
\begin{aligned}
0={}&-3Q-\Theta
+6Q-2H\Theta+Z_{2,s}^*Z_{3,s-1}.
\end{aligned}
$$
故第二条交叉身份为
$$
\boxed{
R:=Z_{2,s}^*Z_{3,s-1}
=(I+2H)\Theta-3Q
=(2I-C_1)B^*L_3-3Q.
}
\tag{4.4}
$$
同样对 (4.3) 取 Gram，利用 $U_{s-1}\perp K$ 和 $U_s^*Z_{2,s-1}=Q$，得到仅含真实旧 Gram 与桥的表达式
$$
\boxed{
\begin{aligned}
Y_3:=Z_{3,s-1}^*Z_{3,s-1}
={}&L_3-9L_2+18L_1-6I\\
&+\frac92Q^*Q+\frac32(Q^*\Theta+\Theta^*Q)
-\Theta^*(G_1-\tfrac12I)\Theta.
\end{aligned}
}
\tag{4.5}
$$
因此在同一 transverse degree $s+2$ 上，
$$
\boxed{
\begin{pmatrix}X_2&R\\R^*&Y_3\end{pmatrix}
=\begin{pmatrix}Z_{2,s}^*\\Z_{3,s-1}^*\end{pmatrix}
\begin{pmatrix}Z_{2,s}&Z_{3,s-1}\end{pmatrix}
\succeq0.
}
\tag{4.6}
$$
特别 $Y_3\succeq0$；(4.5) 中单项没有各自正性的要求，不能拆开估计后再声称保持这个共同 Gram。

## 5. 对硬核联合二阶费用的真实下界

有限维 (4.6) 自动给 $\operatorname{Ran}R^*\subseteq\operatorname{Ran}Y_3$。因此其合法 Schur 补是
$$
X_2\succeq RY_3^\dagger R^*.
$$
代入 (4.2)，得到
$$
\boxed{
G_2\succeq4G_1-2I
+G_2B_sB_s^*G_2
+RY_3^\dagger R^*.
}
\tag{5.1}
$$
所有逆均已标明：$Y_3^\dagger$ 是实际零占据 Gram 上的 Moore–Penrose 逆，其范围条件由共同 Gram 支付。此式没有假设 $Y_3$ 可逆，也没有固定或删除较高出生返回。

在硬核联合最小化的记号中，令 $\mathcal M_s$ 为零占据分量和高出生 occupation 一修正的联合最小解，则
$$
\mathcal M_s^*\mathcal M_s
=G_2B_sB_s^*G_2+X_2.
$$
故 (5.1) 等价于真实新增的下界
$$
\boxed{\mathcal M_s^*\mathcal M_s
\succeq G_2B_sB_s^*G_2+RY_3^\dagger R^*.}
\tag{5.2}
$$
一般首边所需的目标仍为
$$
\mathcal M_s^*\mathcal M_s\succeq H^2-2H-I.
\tag{5.3}
$$
本文没有证明 (5.2) 的右边对全部正权支配 (5.3) 的右边。

## 6. 与 R275 创新式的准确距离

由 $\Theta=Q+2\Delta$，(4.4) 也写成
$$
\boxed{R=2(2G_1-I)\Delta+2(G_1-2I)Q.}
\tag{6.1}
$$
它显示真实零占据交叉费用含有 $Q$ 与 $\Delta$ 的联合项；不能把 (5.1) 的 $R$ 换成单独的 $\Delta$，也不能把两个矩阵当成可交换标量。

R275 的候选 (S1) 为
$$
G_2^{-1}+\Delta L_3^{-1}\Delta^*\preceq C_1^2
\qquad(\ell\ge2).
$$
共同零占据正块 (3.5)、(4.6) 是从实际模型得到的额外约束，但目前没有从它们推导出这条候选。旧顶 $\ell=1$ 的 R275 (S1) 使用零精度 $C_2=0$；本文第二块不覆盖该端点，因为那里不存在上出生 $G_2$。第一块 (3.5) 仍合法。

最后，若原权未归一，令 $S=\sum b_i^2$ 后使用 $b_i/\sqrt S$ 即可。直接保留原最小逆和原桥时，(3.3)、(4.4) 分别变为
$$
U_s^*Z_{2,s-1}=\frac{Q}{S},\qquad
Z_{2,s}^*Z_{3,s-1}
=\frac{(2S I-C_1)B^*L_3-3Q}{S^2}.
$$
这是尺度恢复，不是对原 graph $\Gamma=T^*T$ 的估计；整篇始终在真正 primitive Gram 上。
