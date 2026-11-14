# R236 附录：原正慢行真实消元商的四次 dyadic 指数下界

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的实际费用下界。** 本文对原 $S_N$ 的真实递推商给出直接下界，说明将其替成原始慢行尾比会漏掉主费用。该下界不构造正常湮灭者，不排除其他完整尾理想目标，也不关闭普通 ISP。

## 1. 正算子序与真实递推

本稿的 $B\succeq0$ 表示 $B$ 保持原 $L^2$ 上几乎处处非负函数的锥，
**不是**自伴半正定。若 $B\succeq C\succeq0$，则其乘积和正系数幂和保这个序。
此外 $\|B\|\ge\|C\|$：对任意复向量 $f$，
$|Cf|\le C|f|\le B|f|$，再取 $L^2$ 范数即可。

原实际 $N_k$ 满足
$$
N_k=\begin{pmatrix}0&\eta_kN_{k+1}\\I&0\end{pmatrix},
\qquad \|N_k\|=1,\qquad N_k\succeq0,
\qquad 0<\eta_k\le e^{-770\cdot16^k}.
\tag{1.1}
$$
取任意严格正实可和行 $a_k>0$，置
$$
F_m=\sum_{k\ge m}a_kN_k,
\qquad S_0=F_0.
$$
一律使用真实一次尾交递推
$$
S_j=C_j+N_jD_j,
\quad G_j=D_j^{-1}C_j,
\quad S_{j+1}=G_j^2-\eta_jN_{j+1}.
\tag{1.2}
$$
初始 $C_0=F_1$、$D_0=a_0I$，所以
$$
G_0=a_0^{-1}F_1\succeq0.
\tag{1.3}
$$
以下 $j\ge1$ 的 $G_j$ 不再是 $F_{j+1}/a_j$。

## 2. 负号与正 Neumann 级数没有取消

**命题 2.1。** 每个 $j\ge1$ 的 $G_j$ 满足 $-G_j\succeq0$。
更精确地，若把 $G_{j-1}^2$ 对第 $j$ 位作真实物理分块，则
$$
G_{j-1}^2=C_j+N_jP_j,
\qquad C_j\succeq0,\quad P_j\succeq0,
$$
$$
D_j=P_j-\eta_{j-1}I,
\qquad \chi(P_j)=0.
\tag{2.1}
$$
因此 $P_j$ 在实际范数尾代数中拟幂零，且
$$
\boxed{
-D_j^{-1}=
\sum_{l=0}^{\infty}\eta_{j-1}^{-l-1}P_j^l
\succeq\eta_{j-1}^{-1}I,
\qquad
-G_j\succeq\eta_{j-1}^{-1}C_j.
}
\tag{2.2}
$$

证明：初步 $G_0\succeq0$，其平方的物理块都保持非负锥。
若此前 $-G_{j-1}\succeq0$，其平方仍保持非负锥。
真实偶块是左上块 $C_j$，奇块系数是左下块 $P_j$，故二者都保锥。
$G_{j-1}$ 的常数字符零，故其平方对 $N_j$ 的一次形式系数为零，
准确给 $\chi(P_j)=0$。
实际单生成拟幂零范数代数只有常数字符，因此 $P_j$ 拟幂零。
于是 (2.2) 的 Neumann 级数按算子范数绝对收敛：
$\lim_l\|P_j^l\|^{1/l}=0$，不要求 $\|P_j\|<\eta_{j-1}$。
各项保锥，乘以 $C_j$ 后得 $-G_j\succeq0$ 并完成归纳。证毕。

例如第一步已经准确是
$$
G_1=
\frac{F_2^2+a_1^2\eta_1N_2}{2a_1F_2-a_0^2\eta_0I}.
\tag{2.3}
$$
分母的逆是负的保锥算子；没有可抵消其巨大费用的交替符号。

## 3. 全部高度的原正尾下界

令 $r_j=2^j$，定义
$$
c_0=a_0^{-1},\qquad
c_j=\eta_{j-1}^{-1}c_{j-1}^2
=a_0^{-2^j}\prod_{l=0}^{j-1}
\eta_l^{-2^{j-1-l}}.
\tag{3.1}
$$
则
$$
\boxed{
-G_j\succeq c_j F_{j+1}^{\,2^j}
\quad(j\ge1).
}
\tag{3.2}
$$
为统一归纳，$j=0$ 时把 $-G_0$ 换成 $G_0$，(3.2) 即为 (1.3)。
若前步成立，保锥序的乘法给
$G_{j-1}^2\succeq c_{j-1}^2F_j^{2^j}$。
又 $F_j=a_jN_j+F_{j+1}\succeq F_{j+1}$，故其左上物理块满足
$C_j\succeq c_{j-1}^2F_{j+1}^{2^j}$。
再用 (2.2)，便得 (3.2)。全部右边是原真实尾算子，未切断 carry。

在 $F_{j+1}^{r_j}$ 的展开中保留一组互异指标
$j+1,\ldots,j+r_j$，其系数为
$r_j!\prod_{k=j+1}^{j+r_j}a_k$。
对应的 $\prod N_k$ 范数准确为一：将这些位上的全零物理向量按指标递减顺序变为全一，
每一步都走真实矩阵的左下单位块，不触 carry；上界来自各因子范数一。
因此
$$
\boxed{
\|G_j\|\ge
a_0^{-2^j}\left(\prod_{l<j}\eta_l^{-2^{j-1-l}}\right)
(2^j)!\prod_{k=j+1}^{j+2^j}a_k.
}
\tag{3.3}
$$
这同时允许任意实际尾宽；没有使用有限截断的最小奇异值。

## 4. 原 $S_N$ 的明确增长率

原行 $a_k=(k+1)^{-2}$ 满足 $a_0=1$。由
$$
\sum_{l=0}^{j-1}2^{j-1-l}16^l
=\frac{16^j-2^j}{14},
$$
(1.1)、(3.3) 给
$$
\log\|G_j\|
\ge55(16^j-2^j)
 +\log((2^j)!)
 +2\log\frac{(j+1)!}{(j+2^j+1)!}.
\tag{4.1}
$$
特别，去掉非负阶乘项并粗估分母，得到完全显式的
$$
\boxed{
\log\|G_j\|
\ge55(16^j-2^j)-2\cdot2^j\log(j+2^j+1),
}
\tag{4.2}
$$
从而
$$
\boxed{\liminf_{j\to\infty}16^{-j}\log\|G_j\|\ge55.}
\tag{4.3}
$$
真实一次消元商已经至少以 $\exp[(55-o(1))16^j]$ 增长。
所以前稿“真实 $G_j$ 存在有界子列即可排正常湮灭”的充分条件在原 $S_N$ 上确实不成立。
不能把原始尾比 $\|F_{j+1}/a_j\|=O(j)$ 代入真实消元商。

## 5. 同一个实际条件锚也确实爆炸

[正交叉块与条件锚稿](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)的实际目标是
$$
\Theta_j=2(N_j+G_j)(I+N_j)^{-2},
\qquad \omega_j(\Theta_j)=1.
$$
由 $\Theta_j(I+N_j)^2=2(N_j+G_j)$、$\|N_j\|=1$ 及
$\|(I+N_j)^2\|\le3+\eta_j$，得到
$$
\boxed{
\|\Theta_j\|\ge\frac{2(\|G_j\|-1)}{3+\eta_j}.
}
\tag{5.1}
$$
因此在原 $S_N$ 上，该指定目标的实际范数归一真空锚满足
$$
\frac{|\omega_j(\Theta_j)|}{\|\Theta_j\|}
\le\exp[-(55-o(1))16^j].
\tag{5.2}
$$
这不是只说明其现有上界支付失败，而是其真实目标范数的下界。
它只关闭这一指定的条件锚族，没有给整个 $q_j^{\rm joint}$ 的上界。

## 6. 同一证明允许的正行范围

一般严格正可和行保留 (3.3) 的准确形式。
若 $a_k=e^{-\beta(k+1)^\alpha}$、$0<\alpha<3$，则
$\sum_{k=j+1}^{j+2^j}(-\log a_k)=o(16^j)$，
所以同样有 (4.3) 与 (5.2)。
在 $\alpha=3$ 时，(3.3) 仅给
$$
\liminf_j16^{-j}\log\|G_j\|\ge55-\frac\beta4;
$$
只有右边严格正时，这个下界才证明发散。

本稿不套用于 $S_Y=\sum a_kN_k(I+N_k)^{-1}$，因为其物理对角块有负号，
也不套用于一般复行或加了任意解析项的联合 $S=X+H$。
那些问题若要利用本方法，必须重新证明整个递推的锥符号。


[完整下一尾理想商距离](R236-appendix-full-tail-ideal-quotient-cost-and-normal-anchors.md)仍允许修正 $G_j$；上述原始范数下界不是商距离下界。
