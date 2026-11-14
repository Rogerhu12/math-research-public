# R275 附录：真实联合占据正块与首边必要块的费用

日期：2026-11-14。会话：Astra-ISP-789f。推导：root 与 literature_audit 共同；整理：literature_audit，ChatGPT / GPT-6 Astra Pro。

**状态：§§1–3 的恒等式及 §4 的局部必要块上界已证明；完整相邻序仍未证明。** 此页保存共同推导，供根合并，不把分块必要条件计成一般正权 Boolean 相邻序。

## 1. 原算子与归一 MP

旧有限行 $d=\sum b_iE_i$，$b_i>0$，置
$$S=\sum_i b_i^2,\qquad W=\sum_i b_i^2n_i,\qquad
H=[d,d^*]=SI-2W,\qquad C=\sum_i b_i^3E_i.$$
因此
$$0\preceq W\preceq SI,\qquad -SI\preceq H\preceq SI.$$
这里 $W$ 是真实对角占据算子，不是任意改选的正算子。

固定出生 $s$。记 $K_s=\ker d\cap\mathcal H_s$，
$$\mathcal J_{k,s}=(d^k/k!)^\dagger|_{K_s},\qquad
G_k=\mathcal J_{k,s}^*\mathcal J_{k,s}.$$
相邻低出生的 Gram 记为 $L_k$，相邻高出生的 Gram 记为 $G_k^+$。实际三次桥为
$$B=C|_{K_s}:K_s\to K_{s-1},\qquad
B_s=C|_{K_{s+1}}:K_{s+1}\to K_s.$$
所有伴随按原 primitive Hilbert 内积取。

由原两下降和[三次桥创新稿](R275-appendix-exact-cubic-bridge-for-shear-innovations.md)，严格有
$$d_1\mathcal J_{k,s}=k\mathcal J_{k-1,s},$$
$$d_1^*\mathcal J_{k,s}
=(k+1)\mathcal J_{k+1,s}G_{k+1}^{-1}G_k,$$
$$d_2^*\mathcal J_{k,s}=-\mathcal J_{k+2,s-1}B,$$
$$d_2\mathcal J_{k,s}
=-\mathcal J_{k-2,s+1}(G_{k-2}^+)^{-1}B_s^*G_k.\tag{1.1}$$
不存在的 $k-1,k-2$ 项取零。最顶 $d_1^*$ 块为零，只在精度式中置相应 $G_{k+1}^{-1}=0$，不定义虚假有限逆。

## 2. 所有高度的完整 $H$ 压缩

第一、第二下降的输出处于不同真实核层，物理正交；其伴随输出也正交。因此 (1.1) 给
$$\boxed{\begin{aligned}
\mathcal H_{k,s}:=\mathcal J_{k,s}^*H\mathcal J_{k,s}
={}&(k+1)^2G_kG_{k+1}^{-1}G_k-k^2G_{k-1}\\
&+B^*L_{k+2}B
-G_kB_s(G_{k-2}^+)^{-1}B_s^*G_k.
\end{aligned}}\tag{2.1}$$
这恰是 $\|d^*\mathcal J_{k,s}u\|^2-\|d\mathcal J_{k,s}u\|^2$，没有把四项的符号或次序交换。

首阶 $k=0$ 特别给
$$\boxed{G_1^{-1}+B^*L_2B=P_{K_s}(SI-2W)|_{K_s}.}\tag{2.2}$$
根另从完整 $F_1=dd^*$ 在 $K_s\oplus\operatorname{Ran}d_s^*$ 上的真实 Schur 补直接推得同式：$d_sF_1k=-2Bk$、$d_sF_1d_s^*=4F_2^{(s-1)}$，故消掉正交补的精确费用为 $B^*L_2B$。

由 $H\preceq SI$，(2.1) 给严格保持高出生反馈的上界
$$\mathcal H_{k,s}\preceq SG_k.$$
当 $k\ge2$，最后的负桥项不能未经支付就从这个上界中删去；$k=0,1$ 才没有该项。

## 3. 同物理层相邻出生的联合占据正块

从 (1.1) 直接相减，得
$$\boxed{[d_1,d_2^*]\mathcal J_{k,s}
=-2\mathcal J_{k+1,s-1}B.}\tag{3.1}$$
两个输入空间 $\operatorname{Ran}\mathcal J_{k,s}$ 和
$\operatorname{Ran}\mathcal J_{k+1,s-1}$ 位于同一物理孔层，但处于不同真实核层，故正交。
因此 $H$ 在这两个空间间的交叉二次型为
$$\mathcal J_{k,s}^*H\mathcal J_{k+1,s-1}=-2B^*L_{k+1}.$$

令
$$\Omega_{k,s}=\frac12(SG_k-\mathcal H_{k,s}),$$
并以同样定义记低出生的 $\Omega_{k+1,s-1}$。完整压缩 $W\succeq0$ 给
$$\boxed{
\begin{pmatrix}
\Omega_{k,s}&B^*L_{k+1}\\
L_{k+1}B&\Omega_{k+1,s-1}
\end{pmatrix}\succeq0.}\tag{3.2}$$
同时 $SI-W\succeq0$ 给
$$\boxed{
\begin{pmatrix}
SG_k-\Omega_{k,s}&-B^*L_{k+1}\\
-L_{k+1}B&SL_{k+1}-\Omega_{k+1,s-1}
\end{pmatrix}\succeq0.}\tag{3.3}$$
两个对角均采用 (2.1) 的全部两侧桥。这是真实物理联合 Gram，不是把抽象 HL/HR 正性外推为目标。

## 4. 添加较大一位时，首边的上左必要块可支付

只在本节写旧精度 $C_1=G_1^{-1}$、$C_2=G_2^{-1}$。若旧上出生已到顶，则 $C_2=0$ 表示不存在的第一上升块；这时下面的 $k=1$ 恒等式仍成立。

用 (2.2) 及 (2.1) 的 $k=1$，因没有更高出生下降项，得
$$B^*L_2B\preceq SI-C_1,$$
$$\boxed{C_1B^*L_3BC_1\preceq C_1^2+SC_1-4C_2.}\tag{4.1}$$
第二式先由
$4G_1C_2G_1-I+B^*L_3B\preceq SG_1$，再作 $C_1$ 同余得到。

新位权为 $a>0$，记 $t=a^2$。真实第二创新为
$$\Delta_2=Q_2-Q_1=\tfrac12(C_1B^*L_3-B^*L_2).$$
前稿首边上左必要块等价于
$$t\Delta_2(L_2+tL_3)^{-1}\Delta_2^*
\preceq Z(t),\qquad
Z(t)=C_1^2-C_2+tC_1+t^2I.\tag{4.2}$$
这是将其两侧用同一个 $P_1^{-1}=C_1+tI$ 同余后的精确表达式。

矩阵 Young/完整最小化恒等式给
$$\begin{aligned}
4t\Delta_2(L_2+tL_3)^{-1}\Delta_2^*
&\preceq tB^*L_2B+C_1B^*L_3BC_1\\
&\preceq t(SI-C_1)+C_1^2+SC_1-4C_2.
\end{aligned}\tag{4.3}$$
第一步是对正矩阵 $M,N$ 的一般不等式
$(XM-YN)(M+tN)^{-1}(MX^*-NY^*)\preceq XMX^*+t^{-1}YNY^*$，
取 $M=L_2,N=L_3,X=B^*,Y=C_1B^*$。原实际桥始终是同一个 $B$。

所以准确得到
$$\boxed{\begin{aligned}
4\{Z(t)-t\Delta_2(L_2+tL_3)^{-1}\Delta_2^*\}
\succeq 3C_1^2+(5t-S)C_1+t(4t-S)I.
\end{aligned}}\tag{4.4}$$
若 $t\ge S/4$，右边正，故 (4.2) 成立。这个推导中 $C_2$ 准确相消，甚至不需要先假设旧 $C_1^2\succeq C_2$。

**范围严格限定：** (4.4) 支付的是一位递推中首边的上左必要块。完整创新矩阵还有下右块和交叉 Schur；本稿没有支付它们，也没有处理一般 $t<S/4$ 或所有相邻高度。不能把这条必要条件写成新行的 $C=1$ 证明。

## 5. 尚待解决的实际联合控制

公式 (3.2)–(3.3) 中的交叉恰与创新中的 $B^*L_j$ 对应；但创新把两个高度的交叉取差，且左右配有不同的真实精度。利用这些联合正块支付[一位递推稿](R275-one-bit-full-primitive-schur-recursion-and-innovation.md) (5.2) 的完整交叉项，仍是具体缺口。

不能只取 $H$ 的一侧压缩上界而遗忘高出生负桥，也不能把 $W\succeq0$ 的不同高度压缩当成同一个不变子空间。主问题、原边界与一般有限相邻序均未闭。
