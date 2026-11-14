# R194：空谱逆的 UHF 边界、单侧解析独立与全纯分式场的精确交集

日期：2026-11-12（UTC）。作者：literature。根代理预留 R194。

状态：完整实际证明。
使用真实高位 Walsh 乘法酉算子，构造固定 UHF 代数而消去空谱逆的 $C^*$ 反缩。
由此确定 R192 全纯代数和分式场与 UHF、$\mathcal A$ 的精确交集。
没有把该边界移植到未知不变空间上的多位移动向量，也不据此排除一般慢核。

## 1. 设置与主结论

记物理张量表示中的 UHF 代数为
$$
\mathfrak U
=\overline{\bigcup_{m\ge0}
B\bigl((\mathbb C^2)^{\otimes m}\bigr)\otimes I}^{\|\cdot\|}
\subset B(H).
$$
真实 odometer 的 $A$ 属于 $\mathfrak U$：
截去跨第 $m$ 位的进位得到有限头矩阵，
其误差范数不超过
$$
\omega_m=\operatorname*{ess\,sup}_{y\equiv0\!\!\!\pmod{2^m}}w(y)\to0.
$$
所以
$$
\mathcal G\subseteq\mathcal A\subseteq\mathfrak U.
\tag{1.1}
$$

固定 [R189](../results/R189-empty-phase-inverse-mixed-type-and-universal-fast-fraction-field.md)
的空谱相位类。
旋转相位后，写
$$
Z=e^{-i\theta}(X_u+H_0),\qquad L=Z^{-1},
\quad H_0\in\{A\}'\text{ 有界},
$$
其中 $a\in\ell^2\setminus\ell^1$，
且
$$
\sum_j\bigl(|a_j|-\operatorname{Re}(e^{-i\theta}a_j)\bigr)<\infty.
\tag{1.2}
$$
$L$ 有界、单射、稠密像、拟幂零。

令 $\mathcal H_L$ 为
[R192](../results/R192-single-empty-inverse-holomorphic-fast-calculus-and-universal-fractions.md)
定义的有限全纯代数：
$$
\mathcal H_L
=\{F(g_1,\ldots,g_d,L):g_i\in\mathcal G,\ F\text{ 在联合字符点附近全纯}\}.
$$
变量先减字符后的定义与 R192 完全相同。

**主定理。**

1. 存在满的、含单位的 $*$ 同态
   $$
   \boxed{\Pi_L:C^*(\mathfrak U,L)\longrightarrow\mathfrak U}
   \tag{1.3}
   $$
   满足 $\Pi_L|_{\mathfrak U}=\mathrm{id}$、$\Pi_L(L)=0$。
   它由同一列真实高位 Walsh 酉共轭的强 $*$ 极限实现。
2. 有精确交集
   $$
   \boxed{\mathcal H_L\cap\mathfrak U=\mathcal G,}
   \qquad
   \boxed{\mathcal H_L\cap\mathcal A=\mathcal G.}
   \tag{1.4}
   $$
3. 将闭分式场只与全域有界算子相交，则
   $$
   \boxed{
   \operatorname{Frac}(\mathcal H_L)\cap\mathfrak U
   =\operatorname{Frac}(\mathcal G)\cap\mathfrak U.
   }
   \tag{1.5}
   $$
   两侧均使用各自最大闭实现；等式中的成员因属于 $\mathfrak U$ 而全域有界。
   再与 $\mathcal A$ 相交，得到同样的 $\mathcal A$ 版本。
4. 若 $B_0,\ldots,B_p\in\mathfrak U$，则
   $$
   \sum_{i=0}^p B_iL^i=0\quad\Longrightarrow\quad B_i=0\ \forall i.
   \tag{1.6}
   $$
   不要求这些左系数与 $L$ 交换。
   右系数版本及正收敛半径的单侧算子值解析级数版本亦成立。

第4项是准确的单侧关系排除，不把非交换系数称为通常的交换代数域。

## 2. 高尾 Walsh 乘法与纯局部算子的精确公式

令 $V_j^0=I-2E_j$，
其中 $E_j=e_{10}$ 作用于第 $j$ 个物理位。
乘法算子 $\chi_j$ 在该位为
$$
\chi_j=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
所以
$$
\chi_jV_j^0\chi_j=2I-V_j^0,\qquad
\chi_j(V_j^0)^*\chi_j=2I-(V_j^0)^*.
\tag{2.1}
$$

记 $c_j=e^{-i\theta}a_j$。
真实第一阶与纯模型之差有界，
因此在有限柱公共核心上可写
$$
Z=c_{\mathrm{const}}I+\sum_jc_jV_j^0+B,
\tag{2.2}
$$
其中 $B$ 有界。
这里 $B$ 包括实际 carry 差和给定扰动；
不要求 $B$ 与每个物理局部算子交换。
这里 $c_{\mathrm{const}}$ 为旋转后的标量常数。

取有限集合 $J$，令
$$
U_J=M_{\chi_J}=\prod_{j\in J}\chi_j,\qquad
\lambda_J=2\sum_{j\in J}c_j.
$$
$U_J$ 为自伴酉算子。
若有限柱向量 $v$ 只依赖前 $m$ 位，而 $J\subseteq[m,\infty)$，
则
$$
V_j^0v=\chi_jv,\qquad
(V_j^0)^*v=-\chi_jv\qquad(j\in J).
\tag{2.3}
$$
不同 $\chi_jv$ 两两正交，故
$$
\left\|\sum_{j\in J}c_j\chi_jv\right\|
=\left(\sum_{j\in J}|c_j|^2\right)^{1/2}\|v\|.
\tag{2.4}
$$

由 (2.1)—(2.3)，得到真实有限柱恒等式
$$
(Z-\lambda_J)U_Jv
=
U_JZv
-2U_J\sum_{j\in J}c_j\chi_jv
+[B,U_J]v.
\tag{2.5}
$$
于是
$$
\boxed{
\|(Z-\lambda_J)U_Jv\|
\le\|Zv\|+(2\|a\|_2+2\|B\|)\|v\|.
}
\tag{2.6}
$$
右侧与 $J$ 的长度和位置无关，只要求 $J$ 位于 $v$ 的头之外。

同样对通常伴随，有限柱属于其核心，且
$$
\boxed{
\|(Z^*-\overline{\lambda_J})U_Jv\|
\le\|Z^*v\|+(2\|a\|_2+2\|B\|)\|v\|.
}
\tag{2.7}
$$
该式只是在 (2.3) 的伴随方向改变了正交和的符号，
范数估计相同。
无界算子的公式只在这个明确公共域上使用。

## 3. 一列同时使逆及其伴随消失的高位酉算子

由 (1.2) 与 $a\notin\ell^1$，
$$
\sum_{j\ge m}\operatorname{Re}c_j=+\infty
$$
对每个固定 $m$ 成立：
其部分和等于对应的 $\sum|a_j|$，
减去一个有界的相位缺陷部分和。

取 $m_n\to\infty$。
可选有限区间
$$
J_n=[m_n,M_n)\cap\mathbb N
$$
使
$$
\operatorname{Re}\lambda_{J_n}\ge n.
\tag{3.1}
$$
令 $U_n=U_{J_n}$、$\lambda_n=\lambda_{J_n}$。
这列选择只依赖第一阶系数及相位，不依赖 $H_0$。

对每个固定有限柱 $v$，(2.6) 的误差一致有界。
记 $r_n=(Z-\lambda_n)U_nv$。
因 $U_nv\in\operatorname{Dom}Z$，
$$
U_nv-\lambda_nLU_nv=Lr_n.
$$
从而
$$
\|LU_nv\|
\le
|\lambda_n|^{-1}(\|v\|+\|L\|\|r_n\|)
\longrightarrow0.
\tag{3.2}
$$

$Z$ 有有界全域逆，所以 $(Z^*)^{-1}=L^*$。
同理由 (2.7)，
$$
\|L^*U_nv\|\to0.
\tag{3.3}
$$
$LU_n,L^*U_n$ 的算子范数分别不超过 $\|L\|$；
有限柱在 $H$ 中稠密，故 (3.2)—(3.3) 延至所有固定向量：
$$
\boxed{LU_n\to0,\qquad L^*U_n\to0\quad\text{强}.}
\tag{3.4}
$$
因此
$$
\boxed{U_n^*LU_n\to0\quad\text{强 }*.}
\tag{3.5}
$$

这不是把强误差作用到任意移动向量：
(2.6)—(2.7) 先在固定柱向量上给与 $J_n$ 无关的显式界，
再用统一算子范数扩展。

## 4. 同一酉共轭在整个 UHF 代数上趋于恒等

若 $C$ 是前 $m$ 位的局部矩阵，
则所有 $J_n\subseteq[m,\infty)$ 都使
$$
U_nC=CU_n.
$$
给任意 $C\in\mathfrak U$，
以低位局部矩阵作范数逼近，
得到
$$
\boxed{\|U_n^*CU_n-C\|\to0.}
\tag{4.1}
$$
这里不只得到强收敛，而是范数收敛。

作为与实际 odometer 的一致性检查，
$$
[A,U_J]f(y)
=w(y)\bigl(\chi_J(y-1)-\chi_J(y)\bigr)f(y-1).
$$
若 $J\subseteq[m,\infty)$，
括号只可能在 $y\equiv0\pmod{2^m}$ 时非零。
所以
$$
\|[A,U_J]\|\le2\omega_m\to0.
\tag{4.2}
$$
这也直接核验了实际进位没有破坏 (4.1) 对 $\mathcal A$ 的适用。

## 5. 构造实际 $C^*$ 反缩

在由 $\mathfrak U,L,L^*$ 生成的有限 $*$ 多项式代数上，
(3.5)、(4.1) 及一致范数界给
$$
U_n^*P(C_1,\ldots,C_s,L,L^*)U_n
\longrightarrow P(C_1,\ldots,C_s,0,0)
\quad\text{强 }*.
\tag{5.1}
$$
乘法的强收敛在这里合法，因为每个固定有限词中的因子一致有界。

由强极限的范数下半连续性，
$$
\|P(C_1,\ldots,C_s,0,0)\|
\le\|P(C_1,\ldots,C_s,L,L^*)\|.
\tag{5.2}
$$
特别，若一个实际 $*$ 多项式为零，其置零后的值也为零。
故置 $L,L^*$ 为零定义一个无歧义的收缩 $*$ 同态。
它按范数连续性延至
$$
\Pi_L:C^*(\mathfrak U,L)\to\mathfrak U.
$$
它固定 $\mathfrak U$，所以满且为反缩。

对任意 $T\in C^*(\mathfrak U,L)$，
先以有限 $*$ 多项式范数逼近，
再用酉共轭的等距性，
得到整代数上的实现
$$
\boxed{U_n^*TU_n\to\Pi_L(T)\quad\text{强 }*.}
\tag{5.3}
$$
没有假设此映射在整个 $B(H)$ 上正常，
也没有把强极限换成范数极限。

## 6. 全纯代数与 UHF 的交集恰为 $\mathcal G$

对
$$
T=F(g_1,\ldots,g_d,L)\in\mathcal H_L
$$
使用 R192 已证明的范数收敛多变量演算，
连续同态给
$$
\boxed{\Pi_L(T)=F(g_1,\ldots,g_d,0)\in\mathcal G.}
\tag{6.1}
$$
最后归属可直接由 $\mathcal G$ 的定义验证，而非从
$\mathcal H_L$ 的全纯闭性反推。
对有限个 $g_i$ 取真正解析快逼近 $f_{i,n}(A)\to g_i$。
先减字符，再使用 R192 §2 的共同等价范数，
使固定的有限组 $g_i$ 落在 $F(\,\cdot\,,0)$ 的收敛多圆盘内部；
算子范数逼近保证 $f_{i,n}(A)$ 最终也在同一内部多圆盘。
真实差商给
$$
F(g_1,\ldots,g_d,0)-F(f_{1,n}(A),\ldots,f_{d,n}(A),0)
=\sum_i(g_i-f_{i,n}(A))C_{i,n}.
$$
故差的范数趋于0，且由有限交换和的谐和估计，其四次型趋于无穷。
有限头 $F(f_{1,n}(z),\ldots,f_{d,n}(z),0)$ 是真正解析芽。
这正是 $F(g_1,\ldots,g_d,0)\in\mathcal G$ 的定义条件。

若 $T\in\mathfrak U$，则 $\Pi_L(T)=T$，故 $T\in\mathcal G$。
反包含来自 $\mathcal G\subseteq\mathcal H_L\cap\mathfrak U$。
于是
$$
\mathcal H_L\cap\mathfrak U=\mathcal G.
$$
再由 $\mathcal G\subseteq\mathcal A\subseteq\mathfrak U$，
也有 $\mathcal H_L\cap\mathcal A=\mathcal G$。
特别 $L\notin\mathfrak U$，否则 $\Pi_L(L)=L=0$，
与 $L$ 单射且非零矛盾。

## 7. 非零全纯元素的最低 $L$ 次数可真实提出

取 $0\ne P\in\mathcal H_L$，
用 R192 的忠实形式映射记 $\widehat P(z,w)$。
令
$$
p=\operatorname{ord}_w\widehat P<\infty.
$$
对一个表达式 $P=F(g,L)$ 作 $w$ 的有限 Taylor 分解：
$$
F(s,w)=\sum_{i=0}^{p-1}F_i(s)w^i+w^pF^{[p]}(s,w).
$$
因 $\widehat P$ 的前 $p$ 个 $w$ 系数为零，
$$
\iota(F_i(g))=0\qquad(i<p).
$$
这些系数在 $\mathcal G\subset\mathcal A$ 中，
所以由忠实性，$F_i(g)=0$。
故得到真实有界因子化
$$
\boxed{
P=L^pP_1,\qquad P_1=F^{[p]}(g,L)\in\mathcal H_L,
\qquad \Pi_L(P_1)\in\mathcal G\setminus\{0\}.
}
\tag{7.1}
$$

这里不是只在形式级数中除以 $L$：
Taylor 余项是收敛芽，实际商仍是有界 $\mathcal H_L$ 元素。

## 8. 全纯分式场与 UHF 的精确交集

取 $f=P/Q\in\operatorname{Frac}\mathcal H_L$，
假设其最大闭实现是全域有界算子
$$
T_f=B\in\mathfrak U.
$$
若 $P=0$，则 $B=0$，结论平凡。
以下设 $P,Q$ 均非零。

最大图首先给全域有界恒等式 $QB=P$。
$B$ 自动与 $A$、$L$ 及相关有界分子分母交换。
例如
$$
Q(BA-AB)=PA-AP=0,
$$
由 $Q$ 单射即可取消；
对 $L,Q$ 同样。
特别 $B\in\{A\}'$，无需把任意 UHF 元素先假设成交换子。
现在可写
$$
\boxed{P=BQ.}
\tag{8.1}
$$

分别用 (7.1) 写
$$
P=L^pP_1,\qquad Q=L^qQ_1,
$$
并置
$$
g_P=\Pi_L(P_1)\ne0,\qquad
g_Q=\Pi_L(Q_1)\ne0.
$$
它们均属于 $\mathcal G$。

若 $p<q$，在 (8.1) 中取消单射 $L^p$ 得
$$
P_1=B L^{q-p}Q_1.
$$
施 $\Pi_L$ 得 $g_P=0$，矛盾。

若 $p>q$，取消 $L^q$ 得
$$
L^{p-q}P_1=BQ_1.
$$
施 $\Pi_L$ 得 $Bg_Q=0$。
$g_Q$ 稠密像，故 $B=0$，
又与 $P=BQ\ne0$ 矛盾。

因此必有 $p=q$。
此时取消共同幂再施 $\Pi_L$，得到
$$
\boxed{Bg_Q=g_P.}
\tag{8.2}
$$
因为 $B$ 全域有界，
$g_P/g_Q$ 的最大闭图恰为 $B$ 的全域图：
$g_Qy=g_Px=g_QBx$ 与 $g_Q$ 单射给 $y=Bx$。
所以 $B$ 是 $K=\operatorname{Frac}\mathcal G$ 的有界实现。

反包含因 $\mathcal G\subset\mathcal H_L$ 立即成立。
这证明 (1.5)。
再与 $\mathcal A$ 相交，得到
$$
\operatorname{Frac}(\mathcal H_L)\cap\mathcal A
=\operatorname{Frac}(\mathcal G)\cap\mathcal A,
\tag{8.3}
$$
仍只指全域有界实际成员。

## 9. UHF 系数的单侧多项式和解析关系

设
$$
\sum_{i=0}^pB_iL^i=0,\qquad B_i\in\mathfrak U.
$$
若有非零系数，取最小的 $k$，使 $B_k\ne0$。
在右侧提出 $L^k$：
$$
\left(\sum_{j=0}^{p-k}B_{j+k}L^j\right)L^k=0.
$$
$L^k$ 值域稠密，括号有界，所以括号为零。
对其施 $\Pi_L$，得到 $B_k=0$，矛盾。
这证明 (1.6)。

对右系数关系
$$
\sum_iL^iB_i=0,
$$
在左侧提出最低 $L^k$，使用 $L^k$ 单射取消，
再施 $\Pi_L$，得到同一结论。

更一般，若 $B_i\in\mathfrak U$ 且
$$
\limsup_{i\to\infty}\|B_i\|^{1/i}<\infty,
\tag{9.1}
$$
则由 $L$ 拟幂零，
$\sum B_iL^i$ 和 $\sum L^iB_i$ 都范数绝对收敛，
任意有限次数移位后的级数也如此。
同一最低次数提取证明：
$$
\sum_{i\ge0}B_iL^i=0
\quad\text{或}\quad
\sum_{i\ge0}L^iB_i=0
\quad\Longrightarrow\quad B_i=0\ \forall i.
\tag{9.2}
$$

这些是单侧系数结论；
没有宣称包含交错词 $B_0LB_1L\cdots$ 的非交换自由代数忠实，
也没有把 UHF 本身当作交换系数域。

## 10. 同一第一阶的多个有界扰动仍有共同 $C^*$ 边界

固定第一阶及旋转相位，允许任意一族有界
$$
H_\alpha\in\{A\}',\qquad
L_\alpha=\bigl(e^{-i\theta}(X_u+H_\alpha)\bigr)^{-1}.
$$
§3 的 $U_n$ 只由第一阶系数选择。
对每个固定 $\alpha$，(2.6)—(2.7) 的常数虽可依赖 $\|H_\alpha\|$，
但仍给
$$
L_\alpha U_n\to0,\qquad L_\alpha^*U_n\to0
\quad\text{强}.
$$
每个有限 $*$ 多项式只涉及有限多个 $\alpha$，
因此 §5 的证明给
$$
\Pi:C^*(\mathfrak U,\{L_\alpha\}_\alpha)\to\mathfrak U,
\qquad
\Pi|_{\mathfrak U}=\mathrm{id},\quad \Pi(L_\alpha)=0.
\tag{10.1}
$$

这与两预解式差恢复任意有界交换子的边界一致，
并不证明混合多项式的普遍单射稠密性。
例如两个逆的差仍精确编码原来的未知核。
$C^*$ 边界可同时存在，而这些混合核仍未排除。

## 11. 一个直接的有限总像障碍

令 $0\ne F\in\mathfrak U$。
对 §10 中任意有限个逆 $L_1,\ldots,L_m$，
有
$$
\boxed{
\operatorname{Ran}F
\not\subseteq
\operatorname{Ran}L_1+\cdots+\operatorname{Ran}L_m.
}
\tag{11.1}
$$
证明如下。
令行算子 $R:H^m\to H$ 为
$$
R(x_1,\ldots,x_m)=\sum_iL_ix_i.
$$
若范围包含成立，对每个 $x$ 可取 $Fx$ 的唯一最小范数原像，
即位于 $(\ker R)^\perp$ 的原像，记作 $Bx$。
该映射全域线性且图闭：
若 $x_n\to x$、$Bx_n\to y$，
则 $Ry=Fx$ 且 $y\in(\ker R)^\perp$，
所以 $y=Bx$。
闭图定理给 $B$ 有界，且 $F=RB$。
因此
$$
FF^*\le\|B\|^2RR^*
=\|B\|^2\sum_iL_iL_i^*.
$$
两侧属于 (10.1) 的 $C^*$ 代数。
施正的 $*$ 同态 $\Pi$，得到 $FF^*\le0$，
与 $F\ne0$ 矛盾。

这个范围障碍不依赖某个未知不变空间的选择，
也没有把强收敛的多位酉算子作用到未知空间的移动向量上。

## 12. 对当前单核问题的准确含义

R192 的全纯分式演算虽严格扩大 $K(L)$，
但它与原 UHF 代数的交集恰被 (1.5) 控制。
因此若另有实际有界 $S\in\mathfrak U$ 已被证明不属于
$\operatorname{Frac}\mathcal G$ 的有界实现，
那么 $S$ 不会落入任何本稿单一 empty anchor 的全纯分式场。

另一方面，$\Pi_L$ 是原空间上通过高位酉共轭建立的边界。
这些酉算子包含的高位数可增长且不保持任意未知不变空间。
本稿没有把它降到这样的空间或其压缩上，
因此不能由 (1.3) 直接证明任意混合慢符号的限制单射或稠密像。
