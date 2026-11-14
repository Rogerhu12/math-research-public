# 平方共振核：同一 gauge 的全部幂配对没有增加独立约束

日期：2026-11-12。作者：l2_moments。独立短记录，不另占结果号。

本稿续 square-resonance-bounded-restriction 笔记。它只界定一个具体消元尝试的范围，不宣称本题共振命题为假。

## 1. 已有的真实核结构

沿用该稿的 $X=X_u$、$Y=(a^2I-B_2)^{1/2}$、$\chi(Y)=a$，并设
$$
M=\ker(X-Y).
$$
此前已证明
$$
M\subseteq\bigcap_{n\ge1}\operatorname{Dom}X^n,
\qquad X^n x=Y^n x\quad(x\in M).
\tag{1.1}
$$
$Y$ 是有界交换子；全部有界交换子保持 $M$。

固定 dyadic $\zeta$，记
$$
D_\zeta=\gamma_\zeta(X)-X,
\qquad Z_\zeta=\gamma_\zeta(Y)-D_\zeta.
\tag{1.2}
$$
$D_\zeta$ 是真正解析有界增量，$Z_\zeta\in\{A\}'$ 有界。
第一阶 gauge 保持所有自然幂域。若 $y=U_\zeta x$、$x\in M$，则
$$
Xy=(\gamma_\zeta(Y)-D_\zeta)y=Z_\zeta y.
$$
有界交换子保持 $U_\zeta M$，所以
$$
U_\zeta M\subseteq\bigcap_{n\ge1}\operatorname{Dom}X^n,
\qquad X^ny=Z_\zeta^ny\quad(y\in U_\zeta M).
\tag{1.3}
$$
以上都是实际闭域上的等式。

## 2. 一次完整跨配对已经推出全部多项式版本

由 $X$ 的 $B$ 对称性及 (1.1)—(1.3)，
$$
B((Y-Z_\zeta)M,U_\zeta M)=0.
\tag{2.1}
$$
对任意 $n\ge1$，直接使用自然幂可再得
$$
B((Y^n-Z_\zeta^n)M,U_\zeta M)=0.
\tag{2.2}
$$
但 (2.2) 没有给超出 (2.1) 的独立条件。确实
$$
Y^n-Z_\zeta^n
=(Y-Z_\zeta)\sum_{k=0}^{n-1}Y^{n-1-k}Z_\zeta^k,
\tag{2.3}
$$
后面的有限和是有界交换子，保持 $M$。
将它作用于 (2.1) 的第一端，即得 (2.2)。

更一般地，对任意有界交换子系数多项式
$$
F(w)=\sum_{k=0}^n C_k w^k,\qquad C_k\in\{A\}',
$$
有真实有界 divided-difference 因式分解
$$
F(Y)-F(Z_\zeta)=(Y-Z_\zeta)H_F(Y,Z_\zeta),
$$
其中 $H_F(Y,Z_\zeta)$ 仍保持 $M$。所以所有相应的跨配对也由 (2.1) 推出。

同样，对任意有界交换子 $T_1,T_2$，
$$
B((Y-Z_\zeta)T_1M,T_2U_\zeta M)=0
$$
只是在 (2.1) 中选择了较小的两个输入集合。
特别，改变整数矩锚点、插入有限个实际归一化 dyadic 幂或任意有限高位多项式测试，不会在这个已经对整个 $M\times U_\zeta M$ 成立的等式之外自动产生新的同一 gauge 约束。

## 3. 哪一部分仍可能有新信息

(2.1) 的有界因子是
$$
Y-Z_\zeta=D_\zeta+Y-\gamma_\zeta(Y).
$$
其首 $A^h$ 字符在平方共振值处恰好抵消。
此处不能仅凭该因子全空间单射稠密，就从 (2.1) 删除它；需要的是它在未知 $M$ 上的稠密像。

不同 $\zeta$ 对应不同目标空间 $U_\zeta M$。
因此将两个 gauge 的有界因子作 Bézout 组合之前，必须先把它们的跨配对合法地放在同一对输入空间上。
本稿没有这样的对齐，也没有假设 $M$ 被任何非平凡 $U_\zeta$ 保持。

这条记录只排除“同一 gauge 的更多幂或更多交换测试自然加强一次跨配对”的推断。
非交换的物理头投影、不同 gauge 之间的核图关系、额外的限制范围定理，以及真实二阶来源仍可能提供新信息，均未被这里的代数冗余判断排除。
