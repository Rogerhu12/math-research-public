# R271 补录：奇高度下真实最高 carry 的完整 MP 逆至多一个简单极点

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost，根复核；AI-assisted GPT-6 Astra Pro。

## 0. 结论范围

本条适用于原 N 与 Y 两个有限真实头，保留所有旧 carry、全部强 Boolean 位以及完整物理内积。
它证明完整 $r$ 次幂的 Moore–Penrose 逆随新最高 carry 参数至多损失一次 $t^{-1}$。
这不意味着原 Galerkin 源已经消去该极点；源条件另须证明。
普通 Hilbert ISP、原 $\overline{BM}=M$ 与联合预算中的实际费用均不由本条闭合。

## 1. 真实最高权的一参数族

固定 $m\ge2$，令 $n=2^{m-1}$。
旧权 $d_0,\ldots,d_{m-2}>0$ 保持原值，选定参考最高权
$$
\rho=d_{m-2}^2,\qquad d_{m-1}(t)=t\rho,\qquad 0<t\le1.
$$
在 $2n$ 维原物理基中，
$$
W_j(t)=\prod_{i\in\operatorname{bits}(j)}d_i(t),\qquad
B_m(t)e_j=\frac{W_j(t)}{W_{j-1}(t)}e_{j-1}.
$$
用这些权代入原 N 或 Y 有限符号，得到 $A_m(t)$。
记旧头 $A=A_{m-1}$、$b=b_{m-1}=m^{-2}$；
把新最高位分为两个块，最高位为 $0$ 的块放在前面。

有
$$
B_m(t)^n=t\rho E,\qquad
E=\begin{pmatrix}0&I_n\\0&0\end{pmatrix},\qquad E^2=0.
\tag{1.1}
$$
所以最高 N 项为 $bE$；最高 Y 项也为
$bE(I+E)^{-1}=bE$。
其余项统一是固定旧函数 $F_{m-1}(B_m(t))$；
Y 情形的有理芽在幂零矩阵上按有限 Taylor 代入。

因此存在固定完整物理块 $V$，使
$$
A_m(t)=
\begin{pmatrix}A&bI_n+tV\\0&A\end{pmatrix}.
\tag{1.2}
$$
这里 $V$ 包含原所有旧 carry，不作截去。
删除最高 Boolean 项后记
$$
\widehat A(t)=A_m(t)-bE=F_{m-1}(B_m(t)).
$$
因为
$$
B_m(t)=G_tB_m(1)G_t^{-1},\qquad
G_t=\operatorname{diag}(tI_n,I_n),
$$
函数演算给出
$$
\widehat A(t)=G_t\widehat A(1)G_t^{-1}.
\tag{1.3}
$$

加入任意固定偶数 $R\ge0$ 个强位，取其完整 Boolean 空间，
其正权重记为 $c_1,\ldots,c_R$，
$$
D_R=\sum_{i=1}^R c_iE_i,\qquad
D=A\otimes I+I\otimes D_R.
$$
在新最高位的二块分解下，
$$
C_t=A_m(t)+D_R=
\begin{pmatrix}D&bI+tV_R\\0&D\end{pmatrix},
\tag{1.4}
$$
其中 $V_R=V\otimes I$。
对整数 $r\ge1$，直接乘方得
$$
X_t=C_t^r=
\begin{pmatrix}
D^r&rbD^{r-1}+tT_r\\
0&D^r
\end{pmatrix},\qquad
T_r=\sum_{j=0}^{r-1}D^jV_RD^{r-1-j}.
\tag{1.5}
$$
这是对所有 $t$ 的精确恒等式，不只是零点的一阶展开。

## 2. 偶链与奇高度的完整代数消去

旧头 $A=F_{m-1}(B_{m-1})$ 是单个 $n$ 阶 Jordan 块：
$F_{m-1}'(0)=d_0^{-1}\ne0$，且 $B_{m-1}$ 是循环幂零。
这里 $n$ 为偶数。

对强权作有限可逆对角相似后，完整 $R$ 位 Boolean 删除和的
Lefschetz 链长为 $R-2j+1$。由于 $R$ 偶，它们全部为奇数。
单个 $n$ 阶链与一条 $l$ 阶链的张量和的链长为
$$
n+l-1,\ n+l-3,\ \ldots,\ |n-l|+1.
$$
因此 $D$ 的每一条 Jordan 链均为偶长。
这里只用相似认证链长；随后 MP 范数仍在原物理内积中计算。

### 引理 2.1

若有限幂零 $D$ 没有长度恰为 $r$ 的 Jordan 链，则存在完整物理算子
$P,Q$ 使
$$
D^{r-1}=D^rP+QD^r.
\tag{2.1}
$$
等价的内在条件为
$$
D^{r-1}\ker D^r\subset\operatorname{Ran}D^r.
\tag{2.2}
$$

**证明。** 在单位后移链 $J_Le_j=e_{j-1}$ 上：
若 $L<r$，则 $J_L^{r-1}=0$；
若 $L>r$，令 $S=J_L^*$、
$$
Q_0=|e_{L-r}\rangle\langle e_{L-r-1}|,
$$
则逐基向量核对可得
$$
J_L^{r-1}=J_L^rS+Q_0J_L^r.
$$
第一项只遗漏输入 $e_{L-1}$ 的那一列，第二项恰补上。
所有链合回并还原物理相似，得 (2.1)；
它蕴含 (2.2)。反过来，令 $Z=D^r,\Pi=ZZ^\dagger$，则
$$
P=Z^\dagger D^{r-1},\qquad
Q=(I-\Pi)D^{r-1}Z^\dagger
\tag{2.3}
$$
满足
$$
ZP=\Pi D^{r-1},\qquad
QZ=(I-\Pi)D^{r-1}P_{(\ker Z)^\perp}.
$$
由 (2.2)，最后的核补项为零，故两项相加等于 $D^{r-1}$。
同时在完整物理范数中
$$
\|P\|,\|Q\|
\le M_r:=\|D^{r-1}\|\,\|(D^r)^\dagger\|.
\tag{2.4}
$$
证毕。

以下取 $r$ 为奇数。因 $D$ 的全部链长为偶，引理适用。
用 (2.3) 的物理 $P,Q$ 定义固定剪切
$$
L=\begin{pmatrix}I&-rbQ\\0&I\end{pmatrix},\qquad
J=\begin{pmatrix}I&-rbP\\0&I\end{pmatrix}.
\tag{2.5}
$$
由 (1.5)、(2.1) 精确消去最高 Boolean 项：
$$
LX_tJ=
\begin{pmatrix}D^r&tT_r\\0&D^r\end{pmatrix}
=\widehat X_t.
\tag{2.6}
$$
另一方面 (1.3) 给出
$$
\widehat X_t
=(G_t\otimes I)\,
(\widehat A(1)+D_R)^r\,
(G_t^{-1}\otimes I).
\tag{2.7}
$$

## 3. 完整 Moore–Penrose 费用

### 定理 3.1

在以上原头、偶 $R$、奇 $r$ 条件下，所有 $0<t\le1$ 满足
$$
\boxed{
\|(C_t^r)^\dagger\|
\le
\frac{(1+rbM_r)^2}{t}\,
\|((\widehat A(1)+D_R)^r)^\dagger\|.
}
\tag{3.1}
$$
同一界也适用于 $((C_t^*)^r)^\dagger$。

**证明。** 先由 (2.7) 构造完整真解。
若 $y\in\operatorname{Ran}\widehat X_t$，
$$
z=(G_t\otimes I)
((\widehat A(1)+D_R)^r)^\dagger
(G_t^{-1}\otimes I)y
$$
满足 $\widehat X_tz=y$。最小范数性和
$\|G_t\|\|G_t^{-1}\|=t^{-1}$ 给出相应的 MP 范数界。

再令 $y\in\operatorname{Ran}X_t$。
由 (2.6)，$Ly\in\operatorname{Ran}\widehat X_t$，且
$x=J\widehat X_t^\dagger Ly$ 满足完整方程 $X_tx=y$。
因此
$$
\|X_t^\dagger\|
\le\|J\|\|\widehat X_t^\dagger\|\|L\|.
$$
(2.4)–(2.5) 给出
$\|J\|,\|L\|\le1+rbM_r$，即得 (3.1)。
伴随的非零奇值相同，所以逆范数相同。证毕。

这个证明没有把任何非正交相似当成单位算子；
剪切、两块缩放与参考 MP 的成本均在 (3.1) 明列。
所有构造解都解完整方程，故没有把低列逆或可达压缩逆冒充完整 MP。

## 4. 一阶 Schur 开齐全部新增秩

写 $X_t=X_0+tX_1$，并令
$$
K=\ker X_0,\quad Z=\ker X_0^*,\quad
\mathcal E_1=P_ZX_1|_K,\quad E=\operatorname{Ran}\mathcal E_1.
\tag{4.1}
$$
固定可逆零阶块做 Schur 消元后，新增块为
$t\mathcal E_1+O(t^2)$。
若有非零奇值直到 $t^2$ 或更高阶才打开，则 MP 范数至少以
$t^{-2}$ 发散，与对全部 $0<t\le1$ 的 (3.1) 矛盾。
因此
$$
\operatorname{rank}\mathcal E_1
=\operatorname{rank}X_t-\operatorname{rank}X_0\qquad(t>0).
\tag{4.2}
$$
这里 $\operatorname{rank}X_t$ 对 $t>0$ 恒定，也直接来自 (2.6)–(2.7)。

由完整一阶开秩，
$$
\lim_{t\to0}\ker X_t=\ker(\mathcal E_1|_K),\qquad
\lim_{t\to0}\operatorname{Ran}X_t
=\operatorname{Ran}X_0\oplus^\perp E.
\tag{4.3}
$$
例如第一式：任何极限核向量先在 $K$，其一阶兼容性要求
$\mathcal E_1u=0$；由 (4.2) 两侧维数相同，所以包含即为等号。
第二式由消去零阶范围块后的全部一阶新方向得到。

还有直接的解析框架：由 (2.6)–(2.7)，
$$
\ker X_t=J(G_t\otimes I)\ker\widehat X_1.
$$
在固定子空间 $\ker\widehat X_1$ 中，先选第二块投影独立的向量，
再选只在第一块的核向量；后一组在缩放后除以 $t$。
得到在零点仍满列秩的线性多项式框架。
范围同理。因此这些极限是真核、真范围的解析极限。

## 5. 偶高度不能直接调用

当 $r$ 偶时，$D$ 可以有长度正好为 $r$ 的链，
(2.2) 便可能失败。最小例取旧 $n=2$ 链、$R=0,r=2$：
$$
C_t=
\begin{pmatrix}
0&1&b&0\\
0&0&t&b\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
$$
$C_t^2$ 的非零部分在行 $(0,1)$、列 $(2,3)$ 上为
$$
\begin{pmatrix}t&2b\\0&t\end{pmatrix}.
$$
当 $b\ne0$ 时其逆包含 $-2b/t^2$，完整 MP 具有二阶损失。
故奇 $r$ 是本条精确消去所用的实质条件。

## 6. 尚须支付的源条件

对原纯高度代表，费用由
$q_t=((C_t^*)^r)^\dagger\xi_t$ 决定。
(3.1) 只给出上界中的 $t^{-1}$。
除非另证真实完整 Galerkin 残差在相应新增方向上消失，
不能把最高 carry 越小直接解释成费用越小。
后续必须估计完整真核极限中的源损失，或在增长 $R,r$ 下量化其残余阶数。
