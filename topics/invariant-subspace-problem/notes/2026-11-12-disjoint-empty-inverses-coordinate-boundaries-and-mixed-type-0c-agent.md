# R197：不交空谱模式的多坐标 UHF 边界与全部子商混合幂精确型

日期：2026-11-12（UTC）。作者：literature。根代理预留 R197。

状态：完整证明。
对有限个不交物理位支持的非负、非绝对可和第一阶，
构造逐坐标杀去一个逆而固定其余逆的真实 $C^*$ 边界。
另证明所有有限放大不变子商上的混合单项式精确四次型。
多变量代数独立不被等同于任意多变量多项式的普遍单射稠密。

## 1. 实际设置与结论

记 $\mathfrak U$ 为物理 UHF 代数，$\mathfrak C=\{A\}'$。
取有限个非负行
$$
b^{(i)}=(b_{ij})_{j\ge0}\in\ell^2\setminus\ell^1,
\qquad b_{ij}\ge0,\qquad 1\le i\le d,
$$
其支持
$$
S_i=\{j:b_{ij}>0\}
$$
两两不交。
取任意
$$
H_i\in\mathfrak U\cap\mathfrak C
$$
并令
$$
T_i=X_{b^{(i)}}+H_i,\qquad L_i=T_i^{-1}.
\tag{1.1}
$$
第一阶的任意标量常数可并入 $H_i$。
R189 保证每个 $T_i$ 空谱，
$L_i$ 为有界、单射、稠密像、拟幂零交换子；
而且在所有非零有限放大不变子商上仍单射稠密。
全部 $L_i$ 两两交换。

置
$$
\mathfrak D=C^*(\mathfrak U,L_1,\ldots,L_d).
$$

**定理1.1（多坐标实际边界）。**
对每个 $i$ 存在满的含单位 $*$ 同态
$$
\boxed{
\Pi_i:\mathfrak D\longrightarrow
C^*(\mathfrak U,\{L_j:j\ne i\})
}
\tag{1.2}
$$
固定目标代数，并满足 $\Pi_i(L_i)=0$。
视为 $\mathfrak D$ 的幂等端同态时，这些 $\Pi_i$ 两两交换。
所以可独立置零任意一组逆坐标。

**定理1.2（UHF 系数的单侧解析独立）。**
若 $B_\alpha\in\mathfrak U$ 满足某个正多圆盘半径的系数界
$$
\|B_\alpha\|\le C\rho_1^{-\alpha_1}\cdots\rho_d^{-\alpha_d},
$$
则范数收敛级数
$$
\sum_{\alpha\in\mathbb N^d}B_\alpha L^\alpha=0
\quad\Longrightarrow\quad
B_\alpha=0\ \text{对全部 }\alpha.
\tag{1.3}
$$
右系数版本同样成立。
特别不存在非零 UHF 左系数或右系数的多变量多项式关系。

**定理1.3（全部子商上的混合精确型）。**
对每个非零有限放大不变子商 $Q$，
以及整数 $r,k_1,\ldots,k_d\ge0$，
$$
\boxed{
\tau_4\!\left(A_Q^r\prod_{i=1}^dL_{i,Q}^{k_i}\right)
=\frac{100}{15}r^4.
}
\tag{1.4}
$$
这一条本身不需要不交支持或 $H_i\in\mathfrak U$：
只要每个 $L_i$ 分别满足 R189 的空谱相位类条件，
允许各自的任意有界交换扰动，结论仍成立。
不交支持和 UHF 扰动是定理1.1–1.2 的假设。

## 2. 真实 carry 差属于 UHF

对纯物理位算子
$$
V_j^0=I-2E_j
$$
有
$$
X_{b^{(i)}}=X_{b^{(i)}}^0+K_i,
\qquad
K_i=\sum_jb_{ij}(V_j-V_j^0).
$$
实际差的范数绝对收敛：
$$
\|K_i\|\le8\sum_jb_{ij}\eta_j
\le8\|b^{(i)}\|_2\|\eta\|_2.
\tag{2.1}
$$
$V_j\in\mathcal A\subseteq\mathfrak U$，
$V_j^0$ 为局部矩阵，
所以 $K_i\in\mathfrak U$。
因此
$$
T_i=X_{b^{(i)}}^0+B_i,\qquad B_i=K_i+H_i\in\mathfrak U.
\tag{2.2}
$$

若 $J\subseteq[m,\infty)$ 有限，记
$$
U_J=M_{\chi_J}.
$$
它与所有前 $m$ 位局部矩阵精确交换。
故对每个固定 $B\in\mathfrak U$，
$$
\sup_{J\subseteq[m,\infty),\ J\text{ 有限}}
\|[B,U_J]\|\longrightarrow0.
\tag{2.3}
$$
这是对全部有限高位集合的统一范数估计。

## 3. 翻一个支持时，自己的逆强消失

固定 $i$。
因 $\sum_{j\in S_i}b_{ij}=\infty$，
可选
$$
J_{i,n}\subseteq S_i\cap[m_n,\infty)
$$
有限，$m_n\to\infty$，
使
$$
\lambda_{i,n}=2\sum_{j\in J_{i,n}}b_{ij}\ge n.
$$
令 $U_{i,n}=M_{\chi_{J_{i,n}}}$。

R194 的真实有限柱共轭证明可原样用于这个子集。
明确地，对固定有限柱 $v$，当 $J_{i,n}$ 位于其头之外时，
$$
\|(T_i-\lambda_{i,n})U_{i,n}v\|
\le
\|T_iv\|+
(2\|b^{(i)}\|_2+2\|B_i\|)\|v\|.
\tag{3.1}
$$
通常伴随也满足同一界，将 $T_i,\lambda_{i,n}$ 换为
$T_i^*,\overline{\lambda_{i,n}}$。
这里来自
$$
\chi_jV_j^0\chi_j=2I-V_j^0
$$
及不同高位 $\chi_jv$ 的正交性；
误差不含 $|J_{i,n}|$。

用 $L_iT_i=I$ 及 $L_i^*T_i^*=I$，
再从有限柱用一致算子范数推广，得到
$$
\boxed{
L_iU_{i,n}\to0,\qquad L_i^*U_{i,n}\to0
\quad\text{强}.
}
\tag{3.2}
$$
因此
$$
U_{i,n}^*L_iU_{i,n}\to0\quad\text{强 }*.
\tag{3.3}
$$

## 4. 其他逆在算子范数中固定：完整域与逆交换子

固定 $j\ne i$。
$J_{i,n}\subseteq S_i$ 与 $S_j$ 不交，
所以 $U_{i,n}$ 与纯算子 $X_{b^{(j)}}^0$ 精确域交换。
可以直接从有限柱公共核心验证，
再对闭图取极限；
因为 $U_{i,n}$ 自伴且平方为 $I$，
得到双向域保持
$$
U_{i,n}\operatorname{Dom}X_{b^{(j)}}^0
=\operatorname{Dom}X_{b^{(j)}}^0.
$$
加上有界 $B_j$ 不改变定义域，
故在完整实际域上
$$
[T_j,U_{i,n}]=[B_j,U_{i,n}].
\tag{4.1}
$$
由 (2.3)，右侧有界且范数趋于0。

实际逆的交换子恒等式因此合法：
$$
\boxed{
[L_j,U_{i,n}]
=-L_j[B_j,U_{i,n}]L_j.
}
\tag{4.2}
$$
其推导只使用完整域保持及有界逆，不忽略无界 $T_j$ 的域。
于是
$$
\boxed{
\|[L_j,U_{i,n}]\|
\le\|L_j\|^2\|[B_j,U_{i,n}]\|\to0.
}
\tag{4.3}
$$
伴随方向同样在范数中趋于0。

所以翻第 $i$ 个支持时：

- 整个 UHF 代数范数渐近固定；
- 其他全部 $L_j,L_j^*$ 范数渐近固定；
- $L_i,L_i^*$ 强渐近置零。

任意 $H_j\in\{A\}'$ 而不在 UHF 时，
(2.3) 对 $H_j$ 不成立；
本稿不省略这个假设。

## 5. 多坐标 $C^*$ 反缩

对 $\mathfrak D$ 中的有限 $*$ 多项式，
§§3–4 给
$$
U_{i,n}^*P(\mathfrak U,L_1,\ldots,L_d,L_1^*,\ldots,L_d^*)U_{i,n}
\longrightarrow
P\big|_{L_i=L_i^*=0}
\quad\text{强 }*.
\tag{5.1}
$$
因此置零后的范数不超过原值范数。
如 R194 的实际构造，
这定义无歧义的收缩 $*$ 同态，并延至完整 $\mathfrak D$，
得到定理1.1 的 $\Pi_i$。

每个 $\Pi_i$ 固定其目标代数，因而是满的反缩。
把目标重新包含进 $\mathfrak D$ 后，
$\Pi_i\Pi_j$ 和 $\Pi_j\Pi_i$ 在全部生成元上相同，
故在完整 $C^*$ 代数上相同。
对任意 $I\subseteq\{1,\ldots,d\}$，
复合 $\Pi_I$ 恰置零 $I$ 中的坐标，固定其余坐标。

这里的复合结论来自同态恒等式。
没有把两个不同强极限直接在未经控制的移动向量上交换。

## 6. 单侧多变量关系的逐变量消去

先证明有限多项式版本，再同时说明解析级数的收敛。

对变量个数作归纳。
一个变量时正是 R194：
若
$$
\sum_{k\ge0}C_kL_i^k=0
$$
的系数都被 $\Pi_i$ 固定，
且级数及任意有限次移位的级数范数收敛，
取最小非零系数 $C_k$，
在右侧提出 $L_i^k$。
稠密像允许取消该右因子，
再施 $\Pi_i$，便给 $C_k=0$，矛盾。
这个论证不要求 $C_k$ 与 $L_i$ 交换。

对 $d$ 个变量，按 $L_1$ 次数写
$$
\sum_{\alpha}B_\alpha L^\alpha
=\sum_{k\ge0}C_kL_1^k,
\qquad
C_k=\sum_{\beta\in\mathbb N^{d-1}}B_{(k,\beta)}
L_2^{\beta_2}\cdots L_d^{\beta_d}.
\tag{6.1}
$$
全部 $L_i$ 两两交换，故该重排合法；
不需要把 $L_i$ 移过左系数。
$C_k$ 属于 $\Pi_1$ 的固定代数。
一个变量论证迫使每个 $C_k=0$。
再对其余 $d-1$ 个坐标用归纳，得到全部 $B_\alpha=0$。

若系数满足定理1.2 的正多圆盘界，
每个 $L_i$ 拟幂零，故
$$
\sum_{n\ge0}\rho_i^{-n}\|L_i^n\|<\infty.
$$
因此多变量系列绝对范数收敛，任意有限次移位同样成立。
(6.1) 的系数也具有正的一变量收敛半径：
$$
\|C_k\|
\le
C\rho_1^{-k}\prod_{i=2}^d
\left(\sum_{n\ge0}\rho_i^{-n}\|L_i^n\|\right).
$$
所有消去步骤于是同样适用于解析级数。

右系数版本在左侧提出 $L_i^k$，
使用其单射性取消，其余步骤不变。
这证明定理1.2。

在交换系数子代数 $\mathcal A$ 或 $\mathcal G$ 上，
该结论尤其给通常意义的代数独立。
对一般 UHF 系数只称单侧解析关系排除，
不称非交换自由性。

## 7. 混合型的共同预解式正则化

本节不再需要支持不交。
只假设有限个 $L_i$ 分别来自 R189，
故在每个非零子商 $Q$ 上都单射稠密。
定义准确最大逆
$$
Z_{i,Q}=L_{i,Q}^{-1},\qquad
\operatorname{Dom}Z_{i,Q}=\operatorname{Ran}L_{i,Q}.
$$
其共同域稠密，因为包含
$$
\operatorname{Ran}\left(\prod_iL_{i,Q}\right),
$$
而有限个交换的稠密像有界算子之积仍像稠密。

R189 给常数 $\kappa_i\ge0$ 及
$$
R_{i,s}=(I+sZ_i)^{-1}=L_i(L_i+sI)^{-1},
\qquad
U_{i,s}=(L_i+sI)^{-1},
$$
使小 $s>0$ 时
$$
\|R_{i,s,Q}\|\le(1-\kappa_is)^{-1},\qquad
\|U_{i,s,Q}\|\le3/s.
\tag{7.1}
$$
全部有界因子交换。

固定非零
$$
x\in\bigcap_i\operatorname{Dom}Z_{i,Q}.
$$
对所有 $k_i>0$ 令
$$
N_i=k_in,\qquad s_i=\delta/N_i,
$$
$k_i=0$ 的坐标省略。
单坐标望远镜给
$$
\|R_{i,s_i,Q}^{N_i}x-x\|
\le\delta e^{2\kappa_i\delta}\|Z_{i,Q}x\|
$$
对充分大 $n$ 成立。
再对有限乘积望远镜，得到
$$
\boxed{
\left\|\prod_iR_{i,s_i,Q}^{N_i}x-x\right\|
\le
\delta e^{2\delta\sum_i\kappa_i}
\sum_i\|Z_{i,Q}x\|.
}
\tag{7.2}
$$
这里先选 $\delta$，再令 $n$ 趋于无穷。

取输入
$$
y_n=\prod_iU_{i,s_i,Q}^{N_i}x.
$$
交换性给
$$
\left(\prod_iL_{i,Q}^{N_i}\right)y_n
=\prod_iR_{i,s_i,Q}^{N_i}x,
$$
且
$$
\boxed{
\|y_n\|
\le\|x\|\prod_{i:k_i>0}
(3k_in/\delta)^{k_in}
=\exp(O(n\log n))\|x\|.
}
\tag{7.3}
$$
常数只需对固定有限坐标、固定 $k_i,\delta$ 控制。

## 8. 固定整数块、有限 offset 与精确型

先设 $r\ge1$ 且至少一个 $k_i>0$。
固定正整数 $m$，令
$$
n=n_{j,m}=\left\lceil\frac{m2^j}{r}\right\rceil,\qquad
rn=m2^j+t_{j,m},\quad 0\le t_{j,m}<r.
$$
R140 的真实子商归一化弱极限为
$$
A_Q^{m2^j}/W_{m2^j}
\longrightarrow2^{-\operatorname{popcount}(m)}I_Q.
$$
有限个向量 $A_Q^tx$（$0\le t<r$）都非零。
故存在 $c_{m,x}>0$，对全部充分大的 $j$，
$$
\|A_Q^{rn}x\|\ge c_{m,x}W_{m2^j},
\qquad
\|A_Q^{rn}\|\le W_{m2^j}.
\tag{8.1}
$$

针对这个固定 $m$ 选 $\delta>0$，
使 (7.2) 右侧小于 $c_{m,x}/2$。
之后才令 $j\to\infty$。
由 (7.2)—(8.1)，
$$
\left\|A_Q^{rn}\prod_iL_{i,Q}^{k_in}\right\|
\ge
\frac{c_{m,x}}{2\|x\|}
W_{m2^j}
\prod_{i:k_i>0}(3k_in/\delta)^{-k_in}.
\tag{8.2}
$$
额外对数代价是 $O(n\log n)$。
固定 $m$ 先令 $j\to\infty$，得到型上界
$$
100r^4\,D_4(m)/m^4.
$$
最后沿 $m=2^q-1\to\infty$，其极限为 $100r^4/15$。

反向几何幂界给
$$
\left\|A_Q^{rn}\prod_iL_{i,Q}^{k_in}\right\|
\le W_{rn}\prod_i\|L_{i,Q}\|^{k_in},
$$
故型至少为 $100r^4/15$。
两向合并得到 (1.4)。

若 $r=0$，用 (7.2) 将误差压到 $\|x\|/2$ 以下，
(7.3) 给型上界0；有界算子幂界给下界0。
若全部 $k_i=0$，就是 R140 的精确 $A_Q^r$ 型。
恒等算子的情形同样包含在内。

## 9. 一个确实可迁移到所有子商的混合解析子类

若标量收敛芽具有真正的单项式单位分解
$$
q(w_1,\ldots,w_d)
=w_1^{k_1}\cdots w_d^{k_d}v(w),
\qquad v(0)\ne0,
\tag{9.1}
$$
则有限交换拟幂零元的演算使 $v(L_Q)$ 有界可逆。
由定理1.3，
$$
\boxed{
\tau_4(A_Q^r q(L_{1,Q},\ldots,L_{d,Q}))
=\frac{100}{15}r^4.
}
\tag{9.2}
$$

因此 R192 的最低 $z$ 层论证可推广到以下明确子类。
取有限个 $g_\ell\in\mathcal G_0$ 和一个收敛芽
$$
F(s_1,\ldots,s_e,w_1,\ldots,w_d).
$$
若形式
$$
\widehat F(z,w)
=F(\iota(g_1)(z),\ldots,\iota(g_e)(z),w)
$$
非零，且其最低 $z$ 层
$$
q(w)=[z^r]\widehat F
$$
满足 (9.1)，则
$$
T=F(g_1,\ldots,g_e,L_1,\ldots,L_d)
$$
在所有非零有限放大不变子商上单射稠密。

完整论证仍只有以下有限步骤：
同时作快解析逼近 $g_{\ell,n}=f_{\ell,n}(A)$；
真实全纯差商把误差写成有限个快尾乘有界交换因子，
故误差型趋于无穷；
精确 jet 稳定给
$$
T_Q=A_Q^rq(L_Q)+A_Q^{r+1}J_n(A_Q,L_Q)+E_{n,Q},
\qquad \tau_4(E_{n,Q})\to\infty.
$$
若 $T_Q=0$，(9.2) 与更高 $A$ 阶加快尾的谐和型下界矛盾。
再分别取后续核空间和闭像商，得到单射与稠密像。
所有全纯演算的范数收敛由有限交换拟幂零元的共同等价范数保证，
与 R192 §2 相同。

这里的条件不是空话：
它包含最低 $z$ 层常数非零的全部情形，
以及有共同坐标最低幂且剩余常数非零的混合式。

## 10. 非负第一阶组合产生的混合余因子多项式

这里还有一类通常不满足 (9.1) 的真正混合式。
取 $c_i\ge0$，并非全部为零，令
$$
T_c=\sum_i c_iT_i
$$
表示系数行 $\sum_i c_i b^{(i)}$ 与有界扰动 $\sum_i c_iH_i$
所定义的闭第一阶。
该行仍非负、平方可和而非绝对可和；
所以 $T_c$ 属于 R189，具有普遍逆
$$
L_c=T_c^{-1}.
$$
定义
$$
R=\prod_iL_i,\qquad
q_c(w)=\sum_i c_i\prod_{j\ne i}w_j.
\tag{10.1}
$$

先核真实域。
$\operatorname{Ran}R\subseteq\bigcap_i\operatorname{Dom}T_i$。
在这个共同域上，$T_c$ 确实等于自然和 $\sum_i c_iT_i$：
对 $T_c^*$ 的有限柱核心作配对，
其作用等于有限和 $\sum_i c_iT_i^*$；
因此任何共同域向量都满足定义 $T_c^{**}=T_c$ 的伴随界，
其像就是该有限和。
这只证明所需域包含，不假定自然和的原始域已经等于最大域。

于是对每个 $h\in H$，
$$
T_cRh=\sum_i c_i\prod_{j\ne i}L_jh=q_c(L)h.
$$
乘有界逆并利用全部有界交换子交换，得到
$$
\boxed{q_c(L)L_c=R.}
\tag{10.2}
$$
这是真实有界算子恒等式，因此下降所有子商。

$R_Q$ 单射且像稠密。
由 (10.2)，$q_c(L)_Q$ 的核包含于 $R_Q$ 的核，
其像包含 $R_QQ$；
所以
$$
\boxed{
q_c(L)_Q\text{ 在每个非零 }Q\text{ 上单射稠密}.
}
\tag{10.3}
$$

而且对任意 $r\ge0$，
$$
\boxed{\tau_4(A_Q^r q_c(L)_Q)=\frac{100}{15}r^4.}
\tag{10.4}
$$
一向由
$\|(A_Q^rq_c(L)_Q)^n\|\le W_{rn}\|q_c(L)_Q\|^n$。
另一向由 (10.2)：
$$
\|A_Q^{rn}R_Q^n\|
\le
\|(A_Q^rq_c(L)_Q)^n\|\,\|L_{c,Q}\|^n.
$$
左侧具有 §8 已证的混合单项式精确型，
右侧额外几何因子不改变四次型，得到反向界。

对任意非空坐标子集，完全相同的论证成立。
此外，单项式、任意有限个这种 $q_c$ 的乘积，
再乘一个常数项非零的标量解析单位，仍具有 (10.4)：
把对应的有限个 $L_c$ 乘到左边，
可化为一个混合单项式乘单位，
然后使用同一幂范数比较。
所有这些因子也都普遍单射稠密。

因此 §9 的最低层条件还可放宽为上述有限乘积类。
特别两个坐标的任意正系数和
$c_2L_1+c_1L_2$ 已在本稿中获得普遍单射稠密和精确混合型；
它不是需要保留为未知的例子。

## 11. 独立性与单核之间仍有明确缺口

一般非零多变量标量多项式 $q(w)$ 不必满足 (9.1)。
例如 $w_1-w_2$ 不能在收敛芽环中写为一个单项式乘单位，
也不属于 §10 已证明的非负余因子乘积类。
定理1.2 证明它在原 $H$ 上不为零，
但并不因此证明它在所有不变子商上单射或有稠密像。
本稿也没有证明这种一般 $q(L_Q)$ 的精确零型。

不交支持在多坐标边界中是实质条件。
若同一第一阶作两个不同有界扰动，
则两逆满足
$$
L_0-L_H=L_0HL_H.
$$
当 $H\in\mathfrak U$ 时，
一个固定 UHF、杀 $L_0$ 而固定 $L_H$ 的 $*$ 同态，
会把该式变成 $-L_H=0$，不可能。
所以不能把 §5 的逐坐标边界推广成任意多个 empty anchor。

本稿完成的真实扩大是多坐标边界、UHF 单侧解析独立、
普遍混合单项式精确型，以及 §§9—10 明确的最低层和非负余因子子类。
一般双慢多项式单核和完整 Hilbert 不变子空间问题仍未解决。
