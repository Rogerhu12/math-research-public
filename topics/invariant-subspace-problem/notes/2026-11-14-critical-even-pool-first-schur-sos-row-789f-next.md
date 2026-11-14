# 旧偶临界池首 Schur 行的完整半线平方分解准则

日期：2026-11-14（UTC）。代理：literature_audit / 789f。

**状态：本文的矩阵恒等式与条件蕴含均已证明；两个一般 Boolean 正性条件仍未证明。** 本文给出一个没有自由待选行的实际半线平方分解候选。它没有证明统一有限常数，也没有把有限参数的正性改成原一次系数正性。后者已被实际四权族排除。

## 1. 物理源、已有完整铅笔及依赖

旧池有 $2s$ 个任意正权。令
$$
d=\sum_i b_iE_i,\qquad e=\sum_i b_i^{-1}E_i^*,
$$
并使用物理正交 primitive 源
$$
U=\ker d\cap H_s,\qquad
V=\ker d\cap H_{s-1},\qquad
W=\ker d\cap H_{s-2}.
$$
空源 $W$ 的全部行列一并省略。记
$$
G=\Gamma_{1,s-1},\quad L=\Gamma_{2,s-1},\quad
Z_j=\Gamma_{j,s-2}\quad(1\le j\le4),
$$
$$
A_0=e^*|_U:U\to V,\qquad A=e^*|_V:V\to W,
\qquad R=A_0A_0^*.
$$
所有 $\Gamma$ 仍是完整原层的 $d^j/j!$ 最小范数逆之后，再压到所列 primitive 源的真实 Gram。本文没有交换完整逆与 primitive 压缩的次序。

令 $F=(\sum_i b_i^3E_i)|_V:V\to W$，并记
$$
Q=F^*Z_2,
\quad
\delta_2=\tfrac12(G^{-1}F^*Z_3-F^*Z_2),
$$
$$
\delta_3=\tfrac13(L^{-1}F^*Z_4-G^{-1}F^*Z_3),
\quad D=\delta_2+\delta_3,
\quad H_0=2G+QA.
\tag{1.1}
$$

下述实际身份与完整有限参数铅笔，已由
[有限单弱位的共同缺陷稿](2026-11-14-finite-weak-bit-common-defect-pencil-and-coefficient-obstruction-789f-next.md)
证明：
$$
H_0=G^{-1}L-2G-R,
\qquad
Z_1A=-(2\delta_2^*+\delta_3^*)G,
\qquad
Z_2A=-\delta_3^*L.
\tag{1.2}
$$

固定 $\kappa>0$。新增位权 $a>0$，令 $t=a^2$。新增奇数硬端的实际费用不超过 $\kappa I$，当且仅当
$$
\mathscr P_\kappa(t)\succeq0,
\tag{1.3}
$$
其中在 $V\oplus V\oplus W$ 上
$$
\mathscr P_\kappa(t)=P_0+tP_1+t^2P_2,
$$
$$
P_0=
\begin{pmatrix}
\kappa I&I&A^*Z_1\\
I&G^{-1}LG^{-1}&-G^{-1}LD\\
Z_1A&-D^*LG^{-1}&Z_3+D^*LD
\end{pmatrix},
\tag{1.4}
$$
$$
P_1=
\begin{pmatrix}
\kappa G&-H_0^*&A^*Z_2\\
-H_0&G^{-1}L+LG^{-1}-R/\kappa&-LD\\
Z_2A&-D^*L&Z_4
\end{pmatrix},
\qquad
P_2=\operatorname{diag}(0,L,0).
\tag{1.5}
$$
全部伴随按各 primitive 源的物理 Hilbert 内积取。$G,L,Z_3,Z_4$ 在非空源上均正定。

本文只从 (1.1)–(1.5) 做精确有限维代数，不重新主张这些已有身份的编号。

## 2. 常数项的两个实际 Schur 因子

由消去 (1.4) 的第二块，有
$$
P_0\succeq0
\iff
G\bigl(L^{-1}+\delta_2Z_3^{-1}\delta_2^*\bigr)G
\preceq\kappa I.
\tag{2.1}
$$
这是固定旧池的首加强费用条件。

为看清已有自然平方，定义从 $V\oplus V\oplus W$ 到 $V$ 的行
$$
X_0=
\bigl[L^{-1/2}G,\ L^{1/2}G^{-1},\ -L^{1/2}D\bigr].
$$
直接相乘并用 $A^*Z_1+GD=-G\delta_2$，得到
$$
P_0-X_0^*X_0=
\begin{pmatrix}
\kappa I-GL^{-1}G&0&-G\delta_2\\
0&0&0\\
-\delta_2^*G&0&Z_3
\end{pmatrix}.
\tag{2.2}
$$
这个身份保留了真正旧首缺陷。

本稿采用另一个因子：对 (1.4) 的第一块 $\kappa I$ 作 Schur 分解，置
$$
\mathcal R_\kappa=
\bigl[\sqrt\kappa I,\ \kappa^{-1/2}I,
\ \kappa^{-1/2}A^*Z_1\bigr].
\tag{2.3}
$$
则只要 $P_0\succeq0$，就有
$$
\mathcal R_\kappa^*\mathcal R_\kappa\preceq P_0.
\tag{2.4}
$$
确实，$P_0-\mathcal R_\kappa^*\mathcal R_\kappa$ 的第一行列为零，剩下的两块恰是第一块 Schur 补。因此 (2.4) 没有增加独立的正性假设。

## 3. 唯一指定的相位行

考虑下述实际源上的条件：
$$
\boxed{H_0^*L^{-1}H_0\preceq\kappa I.}
\tag{3.1}
$$
它在这里尚未对任意正权、任意出生证明。尤其不能以另一顺序的 $H_0L^{-1}H_0^*$ 代替它。

定义
$$
U_\kappa=-\kappa^{-1/2}L^{-1/2}H_0:V\to V.
$$
条件 (3.1) 正是 $U_\kappa^*U_\kappa\preceq I$。因此由 (2.4)，若旧首费用 (2.1) 与 (3.1) 同时成立，则下列指定行自动满足常数预算：
$$
\boxed{
X=U_\kappa\mathcal R_\kappa
=-L^{-1/2}H_0
\bigl[I,\ \kappa^{-1}I,\ \kappa^{-1}A^*Z_1\bigr],
\qquad X^*X\preceq P_0.
}
\tag{3.2}
$$

取同一个输出空间 $V$ 上的行
$$
Y=\bigl[0,L^{1/2},0\bigr].
\tag{3.3}
$$
它满足 $Y^*Y=P_2$。选择 (3.2) 的好处是，一次交叉项的第 $1,2$ 块准确为
$$
(X^*Y)_{12}=-H_0^*,
$$
所以这个混合块被精确抵消；没有对 $H_0$ 的两个大项分别估计。

## 4. 剩余一次块与完整平方恒等式

定义
$$
B_\kappa=
G^{-1}L+LG^{-1}+\kappa^{-1}(H_0+H_0^*-R),
$$
$$
J_\kappa=-LD+\kappa^{-1}H_0A^*Z_1,
$$
以及
$$
\boxed{
S_\kappa=
\begin{pmatrix}
\kappa G&0&A^*Z_2\\
0&B_\kappa&J_\kappa\\
Z_2A&J_\kappa^*&Z_4
\end{pmatrix}.
}
\tag{4.1}
$$

**命题 4.1。** 对每个 $t\in\mathbb R$，有完整恒等式
$$
\boxed{
\mathscr P_\kappa(t)
=(P_0-X^*X)+(X+tY)^*(X+tY)+tS_\kappa.
}
\tag{4.2}
$$

**证明。** 常数项与二次项由 (3.2)–(3.3) 自动匹配。直接乘出一次项：
$$
(X^*Y+Y^*X)_{12}=-H_0^*,
$$
$$
(X^*Y+Y^*X)_{22}=-\kappa^{-1}(H_0+H_0^*),
$$
$$
(X^*Y+Y^*X)_{23}=-\kappa^{-1}H_0A^*Z_1,
$$
及其伴随；其余块均为零。与 (1.5) 相减，恰得 (4.1)。$\square$

**条件定理 4.2。** 对固定旧偶池和固定 $\kappa>0$，若下列三项全部成立：

1. 旧首加强费用 (2.1)；
2. 实际相位条件 (3.1)；
3. 完整联合块 $S_\kappa\succeq0$；

则每个有限正 $a$ 所得新增奇硬端都满足同一 $\kappa$ 上界。

**证明。** 由前两项及 (3.2)，$P_0-X^*X\succeq0$。在 $t=a^2\ge0$ 上，(4.2) 的三项均正半定，所以 $\mathscr P_\kappa(t)\succeq0$。用 (1.3) 即得结论。$\square$

这是一条没有自由 $X$ 变量的具体充分准则。它并不要求原 $P_1\succeq0$，因此不落入已有四权反例所排除的逐系数路线。

## 5. 完整保留最高边剩余预算；允许奇异缺陷

消去 (4.1) 中真正正定的第一块 $\kappa G$，定义
$$
E_\kappa=Z_4-\kappa^{-1}Z_2AG^{-1}A^*Z_2.
\tag{5.1}
$$
则准确等价为
$$
\boxed{
S_\kappa\succeq0
\iff
\begin{pmatrix}
B_\kappa&J_\kappa\\
J_\kappa^*&E_\kappa
\end{pmatrix}\succeq0.
}
\tag{5.2}
$$
其中 $E_\kappa\succeq0$ 等价于旧最高加强边
$$
A^*Z_2Z_4^{-1}Z_2A\preceq\kappa G.
$$
因此 (5.2) 不能只靠旧首费用非严格界免费取得。它还要求 $J_\kappa$ 由同一个真实最高边缺陷支付。

式 (5.2) 始终以完整块书写。$E_\kappa$ 可能奇异；不要求它严格正，也不把它任意替换为普通逆。若以后用广义 Schur 形式，必须同时保留交叉块的范围条件。

## 6. 用实际对偶关系消去 $D$，但不拆共同量

由 (1.2) 先得
$$
\delta_3^*=-Z_2AL^{-1},
\qquad
\delta_2^*=\tfrac12(Z_2AL^{-1}-Z_1AG^{-1}).
$$
故
$$
\boxed{
D=-\tfrac12\bigl(L^{-1}A^*Z_2+G^{-1}A^*Z_1\bigr).
}
\tag{6.1}
$$
于是联合交叉量可写成
$$
\boxed{
J_\kappa
=\tfrac12A^*Z_2
 +\bigl(\tfrac12LG^{-1}+\kappa^{-1}H_0\bigr)A^*Z_1.
}
\tag{6.2}
$$
同时
$$
B_\kappa
=(1+\kappa^{-1})(G^{-1}L+LG^{-1})
 -4\kappa^{-1}G-3\kappa^{-1}R.
\tag{6.3}
$$
这些是等式。它们没有给予各项独立的范数预算；尤其不能把 (6.2) 的两列分别放大后声称 (5.2) 已成立。一般正矩阵的 Jordan 乘积也不自动为正，故不能仅凭 $G,L>0$ 判定 (6.3)。

## 7. 等权归一化核对

当旧权全为 $b>0$ 时，在源 $V$ 上
$$
G=(2b^2)^{-1}I,
\qquad L=b^{-4}I,
\qquad A=A_0=F=0,
\qquad H_0=b^{-2}I.
$$
因此相位费用恰为 $I$，而
$$
S_\kappa=
\operatorname{diag}\!\left(
\frac{\kappa}{2b^2}I,
\frac{4+2/\kappa}{b^2}I,
Z_4\right).
$$
所以在 $\kappa\ge1$ 时该候选兼容实际等权端点，并没有在相位条件里误要求一个小于 $1$ 的普适常数。这只是准确归一化的代数核对，不是一般正权证明。

## 8. 尚未支付的部分及量词边界

本文没有证明 (3.1) 或 (5.2) 对全部实际 Boolean 正权成立，既没有证明 $\kappa=1$，也没有证明某个统一有限 $\kappa$。有限定向浮点校准不参加命题或定理的证明。

条件定理 4.2 的量词是“固定旧偶池，先有它的首加强预算，再有另外两项实际预算”。不能仅凭 R297 的全部高度与奇数硬端之普适等价，就把它称为已经闭合的按位数归纳：那些传输可以增加位数；旧偶池高度二首边经弱位传输，可能回到待控制的同一新增奇数尺寸。若要据此证明一般统一常数，仍须给出不循环的完整递推或其它全局论证。

当前明确剩下的实际问题是：在完整物理源上，支付相位压缩 (3.1)，并用同一最高边缺陷 $E_\kappa$ 支付 (6.2) 的联合交叉列。本文没有把共同谱正性、一般 Hodge 理论、普通相邻序或未投影完整提升的粗范数当作这些预算。
