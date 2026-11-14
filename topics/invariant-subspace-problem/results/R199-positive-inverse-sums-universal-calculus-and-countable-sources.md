# R199：正逆和的普遍增生闭包、单锚全纯场与真正可数来源

日期：2026-11-12（UTC）。作者：literature。根代理预留 R199。

状态：完整证明。
严格增生的空谱逆在正系数求和下形成一个可重复使用的实际类；
可数求和须满足明确预算。
每个新和各自具有 R189/R192 的普遍快系数演算。
对真实第一阶来源构造共同高位 Walsh 边界，并证明精确 UHF 交集。
不把多个新和的全纯场任意合并。

## 1. 抽象正逆类与主结论

记 $\mathfrak C=\{A\}'$。
使用 R88：该代数交换，且其每个元素是 $A$ 的多项式的强极限，
从而保持全部有限放大中的闭 $A^{(d)}$ 不变空间。

称有界算子 $L\in\mathfrak C$ 属于正逆类 $\mathscr E$，若：

1. $L$ 单射、稠密像、拟幂零；
2. 存在 $\varepsilon>0$，使
   $$
   \boxed{\operatorname{Re}L\ge\varepsilon L^*L.}
   \tag{1.1}
   $$

该不等式等价于准确最大逆 $Z=L^{-1}$ 在
$\operatorname{Dom}Z=\operatorname{Ran}L$ 上满足
$$
\operatorname{Re}\langle Zy,y\rangle\ge\varepsilon\|y\|^2.
\tag{1.2}
$$
因 $L$ 拟幂零，这个闭逆为空谱。
后面会证明 $L$ 在所有非零有限放大不变子商上都单射稠密，
故定义不必把该性质重复列作额外假设。

取有限或可数多个 $L_i\in\mathscr E$，
并选常数 $\varepsilon_i>0$ 满足 (1.1)。
取正权 $c_i>0$，假设
$$
\boxed{
C:=\sum_i\frac{c_i}{\varepsilon_i}<\infty.
}
\tag{1.3}
$$
定义
$$
S=\sum_i c_iL_i.
\tag{1.4}
$$
事实上 (1.3) 自动保证该和在范数中绝对收敛。

**定理1.1（正逆和）。**
$S\in\mathscr E$，并满足
$$
\boxed{\operatorname{Re}S\ge C^{-1}S^*S.}
\tag{1.5}
$$
在每个非零有限放大不变子商 $Q$ 上，
$S_Q$ 单射、稠密像且拟幂零；
其准确闭逆 $Z_Q=S_Q^{-1}$ 空谱，且
$$
\operatorname{Re}\langle Z_Qy,y\rangle
\ge C^{-1}\|y\|^2.
\tag{1.6}
$$

**定理1.2（每个新单锚的快演算）。**
对任意这样的 $S$，
$$
\tau_4(A_Q^rS_Q^k)=\frac{100}{15}r^4
\qquad(r,k\ge0)
\tag{1.7}
$$
在全部非零 $Q$ 上精确成立。
单锚有限全纯代数
$$
\mathcal H_S
=\{F(g_1,\ldots,g_d,S):
g_i\in\mathcal G,\ F\text{ 在联合字符点附近全纯}\}
$$
具有忠实二变量形式演算；
每个非零成员在全部这些 $Q$ 上单射稠密。
整个 $\operatorname{Frac}\mathcal H_S$ 有忠实最大闭分式场、
原分母图核心、闭包和积、域内精确循环子空间保持。

**定理1.3（真实来源的边界与严格可数范围）。**
若各 $L_i$ 来自 §7 的真实相位缺陷第一阶，
则存在共同高位 Walsh 酉共轭边界，固定 UHF 而杀去所有 $L_i$ 及 $S$。
因而
$$
\mathcal H_S\cap\mathfrak U=\mathcal G,\qquad
\operatorname{Frac}\mathcal H_S\cap\mathfrak U
=\operatorname{Frac}\mathcal G\cap\mathfrak U,
\tag{1.8}
$$
第二个等式只取全域有界实际成员。
§10 构造满足 (1.3) 的真正可数实例；
它甚至不能被任何有限来源 $C^*$ 代数中的非零有界分母表示。

## 2. 正性在所有不变子商上的严格含义

由 (1.1) 及 Cauchy–Schwarz，
$$
\varepsilon\|Lx\|^2
\le\operatorname{Re}\langle Lx,x\rangle
\le\|Lx\|\|x\|.
$$
所以
$$
\boxed{\|L\|\le\varepsilon^{-1}.}
\tag{2.1}
$$
特别 (1.3) 蕴含 $\sum_i c_i\|L_i\|<\infty$。

设 $Q=M/N$ 为有限放大中的闭不变子商。
用 $M\ominus N$ 的向量表示商。
对其非零代表 $x$，
$$
\operatorname{Re}\langle L_Qx,x\rangle
=\operatorname{Re}\langle L^{(d)}x,x\rangle
\ge\varepsilon\|L^{(d)}x\|^2>0,
\tag{2.2}
$$
最后使用原 $L^{(d)}$ 单射。
这一步比只保留商范数的下界更强。
尤其也有
$$
\operatorname{Re}L_Q\ge\varepsilon L_Q^*L_Q.
\tag{2.3}
$$

由 (2.2)，$L_Q$ 无核。
又
$$
\operatorname{Re}\langle L_Q^*x,x\rangle
=\operatorname{Re}\langle L_Qx,x\rangle>0
$$
对所有非零 $x$ 成立，
所以 $L_Q^*$ 也无核，故 $L_Q$ 值域稠密。
不需要假设这个子商继承原共轭。

幂的子商范数不增加，故 $L_Q$ 仍拟幂零。
这样，每个 $\mathscr E$ 元素本身已经是普遍分母。

## 3. 可数正和的正性、拟幂零与普遍单射稠密

### 3.1 加权不等式

对有限部分和 $S_N=\sum_{i\le N}c_iL_i$，
Hilbert 空间 Cauchy–Schwarz 给
$$
\|S_Nx\|^2
\le
\left(\sum_{i\le N}\frac{c_i}{\varepsilon_i}\right)
\left(\sum_{i\le N}c_i\varepsilon_i\|L_ix\|^2\right).
\tag{3.1}
$$
每个求和项非负，而且
$$
\sum_i c_i\varepsilon_i\|L_ix\|^2
\le
\sum_i c_i\operatorname{Re}\langle L_ix,x\rangle
=
\operatorname{Re}\langle Sx,x\rangle.
$$
范数绝对收敛和 (1.3) 允许令 $N\to\infty$，得到 (1.5)。

同样在任意 $Q$ 上，
$$
\operatorname{Re}\langle S_Qx,x\rangle
\ge\sum_i c_i\varepsilon_i\|L_{i,Q}x\|^2.
\tag{3.2}
$$
对非零 $x$，任选一个固定的 $i$；
其 $L_{i,Q}$ 单射，且 $c_i\varepsilon_i>0$，
所以右侧严格正。
对 $S_Q$ 和 $S_Q^*$ 同时使用这个实部，得到
$$
\ker S_Q=0,\qquad\ker S_Q^*=0.
\tag{3.3}
$$
于是 $S_Q$ 单射且值域稠密。

### 3.2 范数和的拟幂零性只使用交换结构

有限个交换拟幂零元的和仍拟幂零：
给任意 $\delta>0$，各因子幂满足
$\|L_i^n\|\le C_i\delta^n$，
有限多项式展开给相应和的谱半径为零。

对可数和，$S_N$ 与 $S-S_N$ 交换。
交换元的谱半径满足
$$
r(U+V)\le r(U)+r(V),
$$
这可由交换二项式展开及各自幂的几何上界直接得到。
因此
$$
r(S)\le r(S_N)+\|S-S_N\|=\|S-S_N\|\to0.
\tag{3.4}
$$
这里没有调用一般谱半径对范数极限的连续性；
交换性是明确使用的输入。
所以 $S$ 及各子商 $S_Q$ 拟幂零。

结合 (3.3)，$S\in\mathscr E$，且参数可取 $\varepsilon=C^{-1}$。

## 4. 准确闭逆、预解式与可重复的闭包操作

设 $L\in\mathscr E$，取 $Z=L^{-1}$。
它闭且稠密定义。
因为 $L$ 拟幂零，
$$
(Z-\lambda)^{-1}=L(I-\lambda L)^{-1}
\qquad(\lambda\in\mathbb C),
\tag{4.1}
$$
所以 $\sigma(Z)=\varnothing$。

对 $y=Lx$，
$$
\operatorname{Re}\langle Zy,y\rangle
=\operatorname{Re}\langle x,Lx\rangle
\ge\varepsilon\|Lx\|^2=\varepsilon\|y\|^2.
$$
这证明 (1.2)，对子商也完全相同。

小参数预解式具有准确有界公式
$$
R_s=(I+sZ)^{-1}=L(L+sI)^{-1},\qquad
U_s=(L+sI)^{-1},
$$
且对所有 $s>0$，
$$
\boxed{
\|R_s\|\le(1+\varepsilon s)^{-1}\le1,\qquad
\|U_s\|\le2/s,\qquad R_s\to I\text{ 强}.
}
\tag{4.2}
$$
强极限先在 $\operatorname{Dom}Z$ 上用
$R_sx-x=-sR_sZx$，再由一致范数界扩展。
相同估计下降全部子商。

该类还允许真实逆的标量平移。
若 $h\in\mathbb C$ 且 $\varepsilon+\operatorname{Re}h>0$，则
$$
\widetilde L=(Z+hI)^{-1}=L(I+hL)^{-1}\in\mathscr E,
\tag{4.3}
$$
其参数可取 $\varepsilon+\operatorname{Re}h$。
有界因子 $I+hL$ 是交换单位；
精确逆公式保证全部域与子商性质。
正标量倍也保留该类，相应调整 $\varepsilon$。

因此可以反复进行：

- 满足 (1.3) 的有限或可数正逆和；
- 保持严格实部下界的逆标量平移；
- 正标量倍。

每次得到的新有界逆仍属于 $\mathscr E$。
这是一组带明确预算的闭包操作，
不是任意算子范数闭包，也不包括任意负或复系数和。

## 5. 抽象正逆的精确混合型

这一证明只使用 $\mathscr E$ 的预解式及原 $A$ 的 R140 高位弱极限，
不需要新逆仍可写成一个第一阶的逆。

固定非零子商 $Q$ 和非零
$x\in\operatorname{Dom}Z_Q$。
对任意 $N\ge1$，由 (4.2) 的收缩估计，
$$
\|R_{s,Q}^Nx-x\|\le Ns\|Z_Qx\|.
$$
取 $s=\delta/N$，令 $y_N=U_{s,Q}^Nx$，则
$$
L_Q^Ny_N=R_{s,Q}^Nx,\qquad
\|L_Q^Ny_N-x\|\le\delta\|Z_Qx\|,
$$
并且
$$
\boxed{\|y_N\|\le(2N/\delta)^N\|x\|.}
\tag{5.1}
$$

设 $r,k\ge1$。
先固定正整数 $m$，
再令
$$
n=n_{j,m}=\left\lceil\frac{m2^j}{r}\right\rceil,\qquad
rn=m2^j+t_{j,m},\quad 0\le t_{j,m}<r.
$$
R140 的
$$
A_Q^{m2^j}/W_{m2^j}
\longrightarrow2^{-\operatorname{popcount}(m)}I_Q
$$
同时作用于有限个非零 $A_Q^tx$，
给某个 $c_{m,x}>0$，
$$
\|A_Q^{rn}x\|\ge c_{m,x}W_{m2^j},
\qquad
\|A_Q^{rn}\|\le W_{m2^j}
\tag{5.2}
$$
对全部充分大的 $j$ 成立。

针对这个固定 $m$ 先选 $\delta$，
使 $\delta\|Z_Qx\|<c_{m,x}/2$。
令 $N=kn$，由 (5.1)—(5.2)，
$$
\|A_Q^{rn}L_Q^{kn}\|
\ge
\frac{c_{m,x}}{2\|x\|}
W_{m2^j}(2kn/\delta)^{-kn}.
\tag{5.3}
$$
额外对数项仅为 $O(n\log n)$。
因此先固定 $m$ 令 $j\to\infty$，
再沿 $m=2^q-1\to\infty$，
得到型上界 $100r^4/15$。
相反，
$$
\|A_Q^{rn}L_Q^{kn}\|\le W_{rn}\|L_Q\|^{kn}
$$
给同一型下界。

$r=0,k>0$ 时，用 (5.1) 选误差小于 $\|x\|/2$，得到精确零型；
$k=0$ 就是 R140；二者皆零为恒等算子。
所以对每个 $L\in\mathscr E$，
$$
\boxed{\tau_4(A_Q^rL_Q^k)=100r^4/15.}
\tag{5.4}
$$
特别适用于正和 $S$。

## 6. 每个新单锚的全纯快演算与闭分式场

取一个固定 $L\in\mathscr E$。
给有限个 $g_i\in\mathcal G_0$ 和收敛芽
$F(s_1,\ldots,s_d,w)$，
设
$$
T=F(g_1,\ldots,g_d,L),\qquad
\widehat T(z,w)=F(\iota(g_1)(z),\ldots,\iota(g_d)(z),w).
$$
所有有限交换拟幂零元的演算范数绝对收敛；
R192 的共同等价范数证明保证复合和逐变量差商均真实合法。

若 $\widehat T=0$，
按 $w$ 展开，所有系数都是 $\mathcal A$ 中形式为零的算子，
由 R32 忠实性逐项为零，故 $T=0$。

若形式非零，取最低 $z$ 阶 $r$：
$$
q(w)=[z^r]\widehat T(z,w)\ne0.
$$
$q$ 是收敛芽，可写 $q(w)=w^kv(w)$、$v(0)\ne0$。
由 (5.4) 和有界单位 $v(L_Q)$，
$$
\tau_4(A_Q^rq(L_Q))=100r^4/15.
\tag{6.1}
$$

对各 $g_i$ 同步取真解析快逼近。
精确有限 jet 与真实差商给
$$
T_Q=A_Q^rq(L_Q)+A_Q^{r+1}J_n(A_Q,L_Q)+E_{n,Q},
\qquad\tau_4(E_{n,Q})\to\infty.
\tag{6.2}
$$
每次固定 $n$ 的 $J_n(A_Q,L_Q)$ 有界。
若 $T_Q=0$，
右侧后两项的交换和谐和型下界趋于
$100(r+1)^4/15$，
与 (6.1) 矛盾。
所以非零形式在每个非零子商上不消失。

分别取其后续核空间和闭像商，得到
$$
\ker T_Q=0,\qquad\overline{T_QQ}=Q.
\tag{6.3}
$$
这也证明实际与形式的忠实对应、有限全纯代数封闭，
以及有限测试向量意义的强主理想单位。

对非零分母 $D$ 与分子 $B$ 属于该全纯代数，
定义准确最大图
$$
\operatorname{Graph}T_{B/D,Q}
=\{(x,y):B_Qx=D_Qy\}.
$$
它闭、稠密定义。
在该有限放大不变图上，$D_Q\oplus D_Q$ 的像稠密，
且
$$
(D_Qx,D_Qy)=(D_Qx,B_Qx)
$$
是原参数图。
因此
$$
\boxed{
\operatorname{Graph}T_{B/D,Q}
=\overline{\{(D_Qh,B_Qh):h\in Q\}}.
}
\tag{6.4}
$$
非零分式单射稠密。
有界参数恒等式给自然和、积的闭包和分式逆；
不把原始自然乘积域当作已经闭。

若 $M\subseteq Q$ 闭不变，
$D_Qy=B_Qx\in M$ 与 $D_{Q/M}$ 单射迫使 $y\in M$。
于是分式在域内保持每个不变空间，
其限制具有同一原分母图核心、稠密定义域和稠密像。
对分式及其逆两次应用，得到精确等式
$$
[T_fx]_{A_Q}=[x]_{A_Q}\qquad(f\ne0).
\tag{6.5}
$$
原空间上还有通常的 $C$ 自伴；
对子商不额外假设共轭。

这些结论每次只针对一个固定的新 $L$ 或 $S$。
没有将多个新锚的全纯字段自动合并。

## 7. 真实相位缺陷来源与共同高位选择

考虑有限或可数个实际第一阶行
$$
a^{(i)}\in\ell^2\setminus\ell^1,
$$
各自有相位 $\theta_i$，使
$$
D_i=\sum_j
\left(|a_{ij}|-\operatorname{Re}(e^{-i\theta_i}a_{ij})\right)<\infty.
\tag{7.1}
$$
允许各自任意有界 $H_i\in\mathfrak C$。
先旋转，再加足够大的实常数，使
$$
Z_i=e^{-i\theta_i}(X_{a^{(i)}}+H_i)+\gamma_iI
$$
满足 $\operatorname{Re}Z_i\ge\varepsilon_iI$。
R189 保证它仍为空谱；
其逆 $L_i=Z_i^{-1}$ 属于 $\mathscr E$。
不要求各行的支持不交，也不要求 $H_i\in\mathfrak U$。

记 $c_{ij}=e^{-i\theta_i}a_{ij}$。
负实部的全部预算有限：
$$
N_i:=\sum_j(-\operatorname{Re}c_{ij})_+
\le D_i/2<\infty.
\tag{7.2}
$$
而每个高尾的 $\sum_j\operatorname{Re}c_{ij}$ 仍发散到 $+\infty$。

第 $n$ 步，令 $m_n\ge n$。
对前 $n$ 行分别选有限集
$$
J_{i,n}\subseteq[m_n,\infty),\qquad
\operatorname{Re}\sum_{j\in J_{i,n}}c_{ij}\ge n+N_i.
$$
取有限并集
$$
J_n=\bigcup_{i\le n}J_{i,n},\qquad U_n=M_{\chi_{J_n}}.
$$
加入其他行的位最多损失该行的全部负实部预算 $N_i$，
因此对每个 $i\le n$，
$$
\boxed{
\operatorname{Re}\sum_{j\in J_n}c_{ij}\ge n.
}
\tag{7.3}
$$
这正是相位缺陷行的并集步骤所需的补偿；
非负行时 $N_i=0$。

对每个固定 $i$、固定有限柱 $v$，
真实纯局部共轭及有界 carry/扰动给
$$
\|(Z_i-\lambda_{i,n})U_nv\|
\le
\|Z_iv\|+
(2\|a^{(i)}\|_2+2\|B_i\|)\|v\|,
$$
其中 $\lambda_{i,n}=2\sum_{j\in J_n}c_{ij}$，
$B_i$ 是固定的有界纯模型差，
$\operatorname{Re}\lambda_{i,n}\ge2n$。
通常伴随同样成立。

由有界逆及有限柱密度，得到对每个固定 $i$，
$$
\boxed{
L_iU_n\to0,\qquad L_i^*U_n\to0\quad\text{强}.
}
\tag{7.4}
$$
没有对 $i$ 作未经证明的一致估计；
所有可数推广都先截断来源数。

## 8. 正和的共同 UHF 边界与精确交集

$\sum_i c_i\|L_i\|<\infty$，
所以先截断有限个来源，再用 (7.4)，得到
$$
SU_n\to0,\qquad S^*U_n\to0\quad\text{强}.
\tag{8.1}
$$
另一方面，$J_n$ 的最小位趋于无穷，
所以对任意 $B\in\mathfrak U$，
$$
\|U_n^*BU_n-B\|\to0.
$$
有限 $*$ 多项式的强 $*$ 极限、范数下半连续性与范数完备化，
构造满的反缩
$$
\boxed{
\Pi:C^*(\mathfrak U,\{L_i\}_i)\to\mathfrak U,
\quad
\Pi|_{\mathfrak U}=\mathrm{id},\
\Pi(L_i)=0,\ \Pi(S)=0.
}
\tag{8.2}
$$
可数生成元不造成问题：每个有限词只含有限多个来源，
再取范数闭包。

对 $F(g,S)\in\mathcal H_S$，
$$
\Pi(F(g,S))=F(g,0)\in\mathcal G.
$$
最后归属由 $\mathcal G$ 的真解析快逼近、有限全纯差商证明：
差为有限个快尾乘有界交换因子，
范数趋零且四次型趋无穷。
于是
$$
\mathcal H_S\cap\mathfrak U=\mathcal G.
\tag{8.3}
$$

若一个非零最大分式 $P/Q$ 的实际值是有界 $B\in\mathfrak U$，
按忠实形式中 $w$ 的最低次数真实提出
$$
P=S^pP_1,\qquad Q=S^qQ_1,
\qquad
\Pi(P_1)=g_P\ne0,\quad\Pi(Q_1)=g_Q\ne0,
$$
其中 $g_P,g_Q\in\mathcal G$。
这里的提出是实际有界因子化：
对一个全纯表达式作有限 $w$-Taylor 分解，
最低次数以前的系数在 $\mathcal G$ 中形式为零，
由忠实性实际为零；剩余 Taylor 余项仍为收敛芽。
因最大图给 $QB=P$，
由分母单射可先证明 $B$ 与 $S,Q$ 交换，
再在 $P=BQ$ 中取消共同 $S$ 幂。

若 $p<q$，施 $\Pi$ 迫使 $g_P=0$；
若 $p>q$，施 $\Pi$ 得 $Bg_Q=0$，
稠密像迫使 $B=0$；
所以只能 $p=q$，并有
$$
Bg_Q=g_P.
$$
这说明 $B$ 恰为 $K=\operatorname{Frac}\mathcal G$ 的有界实现。
反包含直接成立，得到 (1.8)。
再与 $\mathcal A$ 相交，也得相同精确等式。

同一个来源代数中的后续允许操作仍保留此边界。
若 $\Pi(L)=0$，则
$$
\Pi\bigl(L(I+hL)^{-1}\bigr)=0,
$$
因为 $I+hL$ 是 $C^*$ 代数中的有界单位，其逆也在该代数中。
满足预算的可数正和亦在范数中保留 $\Pi(L)=0$。
所以从同一来源经 §4 操作逐次产生的新单锚，
仍具有这里的精确 UHF 交集公式。

本节的边界针对实际来源给出。
对没有 §7 高位实现的任意抽象 $\mathscr E$ 元素，
只保留 §§2—6 的正性、型与闭场结论，
不自动附加 UHF 交集公式。

## 9. 为什么这是带预算的可重复扩大

如果一个原空谱逆仅满足其逆的实部下界为 $-\kappa$，
先作 $Z\mapsto Z+(\kappa+1)I$，
便得到 $\varepsilon=1$ 的 $\mathscr E$ 元素。
这个归一化只乘上有界交换单位，不损失原来的普遍子商性质。

随后取正逆和、再作允许的逆平移，
可继续使用 §4 的操作。
新锚的完整单锚演算始终由 §§5—6 重新证明，
不需要它仍是第一阶或仍有固定有限模式表达。

这里并没有宣称新场包含每个旧场，
也没有把字段之间任意加法或联合全纯代数都当成普遍分母。
准确的增量是：每次构造新的普遍分母和它自己的完整单锚场。
下一节给出这些新分母确实不能简化为有限来源的实际实例。

## 10. 一个严格超出任意有限来源的可数实例

### 10.1 可数不交的真实正行

将所有物理位分成
$$
S_i=\{2^{i-1}(2k+1)-1:k\ge0\},\qquad i\ge1.
$$
这些集合两两不交并覆盖 $\mathbb N$。
在第 $i$ 行设
$$
b_{i,\,2^{i-1}(2k+1)-1}=(k+1)^{-1},
$$
其余系数为零。
每一行都非负、属于 $\ell^2\setminus\ell^1$，
且 $\ell^2$ 范数同为 $\pi/\sqrt6$。

实际 carry 差 $K_i$ 具有共同有限上界
$$
\|K_i\|\le8(\pi/\sqrt6)\|\eta\|_2=:K_*.
$$
纯第一阶的实部非负。
取
$$
Z_i=X_{b^{(i)}}+(K_*+1)I,\qquad L_i=Z_i^{-1}.
$$
则 $\operatorname{Re}Z_i\ge I$，所以 $\varepsilon_i=1$、$\|L_i\|\le1$。
令
$$
\boxed{S=\sum_{i\ge1}2^{-i}L_i.}
\tag{10.1}
$$
此时 (1.3) 的 $C=1$，全部前述结论成立。

### 10.2 可数坐标边界仍存在

固定 $i$，只在 $S_i$ 中选高位 Walsh 集，
使对应第 $i$ 行的和趋于无穷。
它使 $L_i$ 及其伴随强消失。
对每个固定 $j\ne i$，
纯部分严格域交换，而 $K_j+(K_*+1)I\in\mathfrak U$，
所以 R197 的有界逆交换子公式给
$L_j$ 的范数渐近固定。

因此有限词的边界延至可数生成代数，
得到
$$
\Pi_i:C^*(\mathfrak U,\{L_j\}_{j\ge1})
\to C^*(\mathfrak U,\{L_j:j\ne i\}),
$$
固定目标并杀 $L_i$。
由 (10.1) 的范数收敛，
$$
\boxed{\Pi_i(S)=S-2^{-i}L_i.}
\tag{10.2}
$$

### 10.3 非零有限来源分母不可能表示 $S$

给任意有限 $F\subset\mathbb N$，令
$$
\mathfrak D_F=C^*(\mathfrak U,\{L_j:j\in F\}).
$$
若存在 $P,Q\in\mathfrak D_F$ 满足
$$
SQ=P,
$$
选 $i\notin F$，施 $\Pi_i$，得到
$$
(S-2^{-i}L_i)Q=P.
$$
两式相减给 $L_iQ=0$；
$L_i$ 单射，故 $Q=0$。

同样，如果 $QS=P$，两式相减得 $QL_i=0$，
$L_i$ 稠密像仍迫使 $Q=0$。
所以
$$
\boxed{
SQ=P\ \text{或}\ QS=P,\quad P,Q\in\mathfrak D_F
\quad\Longrightarrow\quad Q=0.
}
\tag{10.3}
$$

特别 $S\notin\mathfrak D_F$。
它也不属于任何由有限来源构成、以非零有界分母表示的候选闭分式演算；
尤其不属于任意单一旧来源的 R192 全纯闭分式场。
该排除只用全域有界等式 (10.3)，
不预设某个未经建立的多来源一般闭场已经存在。

这证明可数预算带来真正的新范围，
不是任意范数极限的无条件封闭声明，
也不是把有限来源换一种写法。

## 11. 保留的边界

本稿依赖正权与严格实部不等式。
任意负系数或复系数混合不满足这个论证；
两个独立正方向的差仍允许一般结构上的抵消，
R196 的反模型已明确展示这一点。

单个新锚的快全纯演算和全部子商闭场已经完成，
但多个新锚的任意混合多项式仍不能只凭各自的普遍性质排核。
共同 $C^*$ 边界也不因存在而变成忠实映射，
不能直接用于未知核投影的取消。

一般慢二次单核与完整 Hilbert 不变子空间问题仍未解决。
