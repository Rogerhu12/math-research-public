# R179：真实快尾子代数、全纯稳定性与相对闭理想分类

日期：2026-11-12。作者：l2_moments。根代理预留 R179。
状态：完整证明。所有头部和每个尾因子均为实际真解析芽；没有把一般 $\mathcal G$ 元素或任意范数极限纳入本子代数。

## 1. 定义

令
$$
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},\qquad
M_n=A^n/W_n,\qquad W_n=\|A^n\|,
$$
并记其连续形式嵌入为 $\iota$，唯一字符为 $\chi$。
$\mathbb C\{A\}$ 表示零点附近真正解析标量芽在实际拟幂零 $A$ 上的值。

定义 $\mathcal T$ 为所有具有以下至少一种表示的元素：
$$
\boxed{
S=H(A)+\sum_{n\ge1}c_nM_nV_n,
\quad H\in\mathbb C\{z\},\quad
V_n\in\mathbb C\{A\},\quad \|V_n\|\le1.
}
\tag{1.1}
$$
非零 $c_n$ 可以只有有限个；无限时要求其非增模长重排满足
$$
\boxed{
\frac{-\log c_\ell^*}{\ell^3}\longrightarrow+\infty.
}
\tag{1.2}
$$
未使用的指数系数置零。
同一正整数指数只列一项，指数可以任意稀疏。
有统一有限范数上界的因子可乘一个固定常数正规化到 $\|V_n\|\le1$。

(1.2) 保证 $\sum_n|c_n|^\varepsilon<\infty$ 对全部 $\varepsilon>0$ 成立，
特别 (1.1) 按算子范数绝对收敛。
定义有限头
$$
S_N=H(A)+\sum_{1\le n\le N}c_nM_nV_n,\qquad S_0=H(A).
\tag{1.3}
$$
每个 $S_N$ 本身真解析，$S_N\to S$ 按范数，且
$$
\chi(S_N)=H(0)=\chi(S).
\tag{1.4}
$$
不要求不同 $S_N$ 或 $V_n$ 具有统一解析半径。

## 2. 超三次重排的有限运算

下文需要一个不依赖原指数排列的事实。

若有限个序列 $c^{(1)},\ldots,c^{(d)}$ 均满足 (1.2)，则
$$
e_n=\sum_{\nu=1}^d|c_n^{(\nu)}|
$$
也满足 (1.2)。
确实，若 $e_n>dt$，至少有一个 $\nu$ 满足
$|c_n^{(\nu)}|>t$。
因此第 $dk$ 个最大的 $e_n$ 至多为
$$
d\max_\nu(c_k^{(\nu)})^*.
\tag{2.1}
$$
一个有限的索引偏移不影响结论。
因为各序列可支付任意大的三次指数，(2.1) 中固定的 $d^3$ 损失不影响极限为无穷。

删除或添加有限项、乘固定非零常数、取逐项较小序列也保持 (1.2)。
同样，把某个具体坐标序列乘 $C^n$ 后，如果原次序本身已满足
$|c_n|\le e^{-\Gamma n^3}$ 对任意固定 $\Gamma$ 最终成立，
结果的重排仍满足 (1.2)。
最后这一规则正是 R159 振幅枚举中吸收有限柱增长常数所用的规则，
不被误用为对任意无序序列乘 $C^n$ 都稳定。

## 3. 加法和乘法封闭

### 3.1 加法

设 $S,T$ 分别有头 $H,K$、系数 $c_n,d_n$ 和因子 $V_n,U_n$。
令 $e_n=|c_n|+|d_n|$。
若 $e_n>0$，置
$$
R_n=(c_nV_n+d_nU_n)/e_n.
$$
则 $R_n$ 真解析，范数至多1，且
$$
S+T=(H+K)(A)+\sum_ne_nM_nR_n.
$$
§2 给重排条件，所以 $S+T\in\mathcal T$。
标量乘法、负号及单位显然也在 $\mathcal T$ 中。

### 3.2 乘法

按同一整数截断形成 $S_N,T_N$。
其范数一致有界，且所有有限头都真解析。
精确的排序差为
$$
\begin{split}
S_NT_N-S_{N-1}T_{N-1}
&=(S_N-S_{N-1})T_N
+S_{N-1}(T_N-T_{N-1})\\
&=M_N\big[c_NV_NT_N+d_NU_NS_{N-1}\big].
\end{split}
\tag{3.1}
$$
这包含正确的一次交叉项，没有把两个尾增量乘积漏掉。

取
$$
C=\max\left(1,\sup_N\|S_N\|,\sup_N\|T_N\|\right).
$$
方括号范数至多 $C(|c_N|+|d_N|)$。
除以该非零正数后得到真解析、范数不超过1的新因子。
系数 $C(|c_N|+|d_N|)$ 由 §2 超三次重排。
初始头 $H(A)K(A)$ 真解析，而 $S_NT_N\to ST$ 按范数。
故
$$
\boxed{ST\in\mathcal T.}
\tag{3.2}
$$

因此 $\mathcal T$ 是含单位交换子代数，并含全部真解析函数和全部多项式。

## 4. 实际单位逆及 gauge 稳定

### 4.1 单位逆

设 $S\in\mathcal T$ 在 $\mathcal A$ 中可逆。
由于 $\mathcal A$ 的唯一字符为 $\chi$，这等价于
$\chi(S)=H(0)\ne0$。
(1.4) 表明每个 $S_N$ 也可逆，其逆是一个真解析芽在 $A$ 上的值。

$S_N\to S$ 及有界逆的范数连续性给
$$
D=\sup_N\|S_N^{-1}\|<\infty.
$$
其中有限个早期项分别取范数即可，不要求逐头的标量解析半径一致。

实际逆差恒等式为
$$
S_N^{-1}-S_{N-1}^{-1}
=-c_NM_NS_N^{-1}V_NS_{N-1}^{-1}.
\tag{4.1}
$$
后因子真解析且范数至多 $D^2$。
初始头 $H(A)^{-1}$ 真解析，新增系数 $D^2c_N$ 仍超三次，
所以
$$
\boxed{S^{-1}\in\mathcal T.}
\tag{4.2}
$$
若 $S$ 在原 $B(H)$ 中可逆，同样成立：
$\chi(S)=0$ 时 $S$ 的幂谱半径为0，不能有有界全域逆；
故实际可逆必有非零字符。
因此这里也是对原 Hilbert 有界逆的封闭性。

### 4.2 Gauge

对 dyadic $\zeta$，
$$
\gamma_\zeta M_n=\zeta^nM_n.
$$
$\gamma_\zeta$ 是实际酉共轭，保持范数；
$V_n=F_n(A)$ 变成 $F_n(\zeta A)$，仍真解析。
故
$$
\boxed{\gamma_\zeta\mathcal T=\mathcal T.}
\tag{4.3}
$$
双向由 $\zeta^{-1}$ 得到。

## 5. 有限元的全纯演算稳定

取 $S^{(1)},\ldots,S^{(d)}\in\mathcal T$，
令 $\beta_\nu=\chi(S^{(\nu)})$。
设标量函数 $F$ 在 $\beta=(\beta_1,\ldots,\beta_d)$ 的邻域全纯。
则
$$
\boxed{F(S^{(1)},\ldots,S^{(d)})\in\mathcal T.}
\tag{5.1}
$$

所有 $S^{(\nu)}-\beta_\nu I$ 拟幂零且交换，
故通常多元 Taylor 演算在实际代数中绝对收敛。
也可在包含于全纯定义域的固定小多圆盘边界上使用多元 Cauchy 积分。

令各 $S_N^{(\nu)}$ 按共同整数指数截断。
每个有限头的字符仍为 $\beta_\nu$，
所以所选多圆盘边界均位于其预解集。
对每个 $\nu$，所有
$$
(z_\nu I-S_N^{(\nu)})^{-1}
$$
在边界和 $N$ 上统一有界：
充分大的 $N$ 由范数收敛与逆连续性统一控制，剩余有限个头再取最大值。

置
$$
F_N=F(S_N^{(1)},\ldots,S_N^{(d)}).
$$
它是真解析芽在 $A$ 上的值。
具体地，若 $S_N^{(\nu)}=h_{\nu,N}(A)$，
则 $h_{\nu,N}(0)=\beta_\nu$，
所以 $z\mapsto F(h_{1,N}(z),\ldots,h_{d,N}(z))$ 在0附近真解析。
半径允许依赖 $N$。

逐坐标 telescoping，再用 Cauchy 积分中的真实逆差式，给
$$
F_N-F_{N-1}
=\sum_{\nu=1}^d
(S_N^{(\nu)}-S_{N-1}^{(\nu)})R_{\nu,N}.
\tag{5.2}
$$
每个 $R_{\nu,N}$ 由有限头的单、双预解因子及固定 Cauchy 积分构成。
刚才的统一预解界给
$$
\sup_{\nu,N}\|R_{\nu,N}\|<\infty.
\tag{5.3}
$$
它们逐项真解析：
对固定 $N$，在 $A$ 的标量参数 $z=0$ 的足够小圆盘内，
所有 $h_{\nu,N}(z)$、$h_{\nu,N-1}(z)$ 都仍位于 Cauchy 轮廓内部；
相应积分给真解析标量芽，求值于拟幂零 $A$ 即为 $R_{\nu,N}$。
这里没有以范数极限替代逐项解析证明。

将
$$
S_N^{(\nu)}-S_{N-1}^{(\nu)}
=c_N^{(\nu)}M_NV_N^{(\nu)}
$$
代入 (5.2)，每个增量含共同真实因子 $M_N$。
以
$$
C\sum_\nu|c_N^{(\nu)}|
$$
吸收 (5.3) 后，因子范数不超过1，且系数由 §2 超三次重排。
初始头 $F_0$ 真解析。
Cauchy 积分的统一预解界还给 $F_N\to F(S^{(1)},\ldots,S^{(d)})$ 按范数。
这就得到 (5.1) 的所需表示。

## 6. 每个非零元生成标准闭主理想

设 $0\ne S\in\mathcal T$，形式首阶为 $r$。
若 $r=0$，$S$ 是单位，结论为 $\overline{S\mathcal A}=\mathcal A$。

设 $r\ge1$。
在 (1.3) 选 $N\ge r$。
余尾的每项形式阶至少为其指数 $n>N$，
故有限头 $S_N$ 与 $S$ 的前 $r+1$ 个形式系数完全相同。
其真解析芽于是有分解
$$
S_N=A^rU_N(A),\qquad U_N(0)\ne0.
\tag{6.1}
$$
把这个头作为单个 $n=r$ 的归一化幂项，
将单位 $U_N(A)$ 除以其范数，
其余尾保留原表示。
首因子字符非零、所有指数均大于 $r$、系数重排三次型为无穷，
完全满足 R118 的实际假设。

因此
$$
\boxed{
\overline{S\mathcal A}^{\|\cdot\|}=I_r
=\overline{A^r\mathcal A}^{\|\cdot\|}.
}
\tag{6.2}
$$
还存在实际单位 $Z_k\in\mathcal A^\times$，使
$$
SZ_k\longrightarrow A^r.
\tag{6.3}
$$
本稿没有断言这些特定 $Z_k$ 必在 $\mathcal T$，也不需要这一点。

由于 $\mathbb C[I,A]$ 在 $\mathcal A$ 中范数稠密，
(6.2) 还给
$$
\boxed{
A^r\in\overline{S\,\mathbb C[I,A]}^{\|\cdot\|}.
}
\tag{6.4}
$$
对 (6.3) 的每个 $Z_k$ 单独用多项式范数逼近，并令乘回 $S$ 的误差趋零即可。

## 7. 相对范数闭理想完整分类

这里“相对范数闭”指在 $\mathcal T$ 的继承算子范数拓扑中闭；
不假设 $\mathcal T$ 完备。

**定理7.1。**
$\mathcal T$ 的全部非零相对范数闭理想恰为
$$
\boxed{\mathcal T\cap I_r,\qquad r=0,1,2,\ldots.}
\tag{7.1}
$$
此外还有零理想。
每个 $\mathcal T\cap I_r$ 在 $\mathcal T$ 中的余维为 $r$。

**证明。**
$\mathcal T\cap I_r$ 显然是相对闭理想。
反向，设 $J\ne0$ 是相对闭理想。
非零元的形式阶是非负整数，故可选 $S\in J$，使
$$
r=\operatorname{ord}S
=\min\{\operatorname{ord}T:0\ne T\in J\}.
$$
由 (6.4)，存在 $Sp_k(A)\to A^r$ 按范数。
每个 $p_k(A)\in\mathcal T$，故 $Sp_k(A)\in J$；
又 $A^r\in\mathcal T$，相对闭性给 $A^r\in J$。

若 $T\in\mathcal T\cap I_r$，
则有 $A^rq_k(A)\to T$ 按范数。
这些近似都在 $J$ 中，故 $T\in J$。
反向，最小阶的选择以及
$I_r=\{T\in\mathcal A:[z^n]\iota(T)=0,\ n<r\}$
给 $J\subseteq\mathcal T\cap I_r$。
所以等号成立。

前 $r$ 个系数映射在 $\mathcal T$ 上满射到 $\mathbb C^r$，
因为 $I,A,\ldots,A^{r-1}\in\mathcal T$。
其核就是 $\mathcal T\cap I_r$，余维结论随之成立。证毕。

作为纯代数补充，$\mathcal T$ 的唯一极大理想也是 $\mathcal T\cap I_1$：
任何非零字符元在 §4 已有 $\mathcal T$ 内的逆，
所以任何真理想都包含于字符核；
该核的商为 $\mathbb C$。

## 8. 仅对相交理想成立的母代数结论

若 $\mathcal A$ 的一个范数闭理想 $J$ 满足
$$
J\cap\mathcal T\ne\{0\},
$$
则 $J=I_s$ 对某个有限 $s$ 成立。

确实，取 $0\ne S\in J\cap\mathcal T$，阶为 $r$。
(6.2) 给 $I_r\subseteq J$。
令 $s$ 为 $J$ 中非零元的最小阶，选取阶为 $s$ 的 $T\in J$。
明确取 $Q(A)$ 为 $T$ 的形式 Taylor 多项式，保留 $0$ 至 $r$ 次（含第 $r$ 次）。
则 $T-Q(A)\in I_{r+1}\subseteq I_r\subseteq J$，
所以 $Q(A)\in J$；因为 $s\le r$，其首阶仍为 $s$。
于是 $Q\in J\cap\mathcal T$，再由 (6.2) 得 $I_s\subseteq J$；
最小阶给反向包含。

因此
$$
\boxed{
\mathcal A\text{ 的任何非标准范数闭理想必须与 }\mathcal T
\text{ 只有零交。}
}
\tag{8.1}
$$
虽然 $\mathcal T$ 含全部多项式且在 $\mathcal A$ 中稠密，
本稿没有据此断言每个非零闭理想都与它非零相交。
稠密子代数完全可能与一个指定闭子空间只有零交；
(8.1) 不能被省略前提地扩大成 $\mathcal A$ 的理想分类。

## 9. 与已有快类及普遍表示的接口

### 9.1. 一般整数归一化幂的准确尾型

此处使用的是 **R110 §§2–4 的全部整数幂估计，以及 R115 §2 式(3)—(4)的有界因子版本**，不限于 dyadic $N_j$。为排除范围歧义，完整写出所需形式。

设
$$
B_K=\sum_{n\ge K}c_nM_nV_n,\qquad
A_K=\frac14\left(\sum_{n\ge K}n^{-4/3}\right)^{-3}.
\tag{9.1}
$$
因为 $V_n$ 与全部 $M_\ell$ 交换且 $\|V_n\|\le1$，R110 的真实重复幂界直接给
$$
\|(M_nV_n)^s\|
\le\|M_n^s\|
\le\exp[-n^4(s-1)^4/4]\qquad(s\ge1).
\tag{9.2}
$$
这里因子 $V_n$ 只需有界交换；其真解析性留给有限头，不用于尾的幂估计。

给定任意 $\gamma>0$，由 (1.2) 可选有限 $R_0$，使
$$
-\log c_\ell^*\ge\gamma\ell^3\qquad(\ell>R_0).
$$
再选 $K$ 大于前 $R_0$ 个最大系数所在的所有原指数。
于是所有尾系数小于1，任意 $d$ 个不同尾指标的系数积至多
$$
\exp\!\left[-\gamma\sum_{\ell=1}^{d}(R_0+\ell)^3\right]
\le e^{-\gamma d^4/4}.
\tag{9.3}
$$
这一步同时付清“删有限大系数”与“按原整数指数切尾”，没有把排序名次等同于原指数。

固定 $0<\varepsilon<1$，置 $D=(1-\varepsilon)\gamma/4$。
在 $B_K^L$ 的一个有序项中，令 $s_n$ 为指标出现次数、$d$ 为不同指标数。
由加权 Hölder，
$$
\frac14\sum_n n^4(s_n-1)_+^4\ge A_K(L-d)^4.
$$
$(1-\varepsilon)$ 部分系数由 (9.3) 支付 $Dd^4$；
剩余 $\varepsilon$ 部分保留作绝对求和。二项 Hölder 给
$$
A_K(L-d)^4+Dd^4
\ge b_K L^4,\qquad
b_K=(A_K^{-1/3}+D^{-1/3})^{-3}.
$$
于是
$$
\boxed{
\|B_K^L\|
\le
\left(\sum_{n\ge K}|c_n|^\varepsilon\right)^L
e^{-b_KL^4}.
}
\tag{9.4}
$$
所有求和先对有限尾成立，再由绝对算子范数收敛取极限。
一次系数和有限，其对数只产生 $O(L)$，所以
$$
\tau_4(B_K)\ge b_K.
\tag{9.5}
$$

为了明确任意型预算，给定 $\Theta>0$，可取
$$
\varepsilon=\frac12,\qquad \gamma=64\Theta,\qquad D=8\Theta.
$$
先删上述有限大系数，再增大 $K$ 至 $A_K\ge8\Theta$。
此时
$$
b_K\ge
\bigl(2(8\Theta)^{-1/3}\bigr)^{-3}
=\Theta.
$$
这些条件对所有更大的 $K$ 保持成立，故
$$
\boxed{\tau_4(B_K)\longrightarrow+\infty\quad(K\to\infty).}
\tag{9.6}
$$
有限支持时尾最终为零，结论按 $\tau_4(0)=+\infty$ 解释。

现在 (1.1) 的有限头
$$
H(A)+\sum_{n<K}c_nM_nV_n
$$
每次都是真解析芽：只有有限个真解析因子，取其共同的足够小零点邻域即可。
它按范数趋于 $S$，误差正是 $B_K$。结合 (9.6)，得到
$$
\boxed{\mathcal T\subseteq\mathcal G.}
\tag{9.7}
$$
这证明依赖具体的 (1.1) 表示，不要求 $\mathcal G$ 范数闭，也不依赖 dyadic 指数限制。

### 9.2. 已有快类及普遍表示

R175 的所有 $P_{f,w}$ 都属于 $\mathcal T$。
其原振幅枚举的增长因子已经吸入超三次系数，
而互异指数 $2^{j_m}$ 可重新按整数次序排列；
绝对范数收敛保证值不变。
因此本稿的加乘、逆和全纯稳定性也可用于这些快符号产生的实际算子。

对任意连续含幺表示 $\pi:\mathcal A\to B(X)$，
(6.2) 的两向范数逼近给
$$
\ker\pi(S)=\ker\pi(A)^r,\qquad
\overline{\operatorname{Ran}\pi(S)}
=\overline{\operatorname{Ran}\pi(A)^r}.
\tag{9.8}
$$
这延续 R118/R175 的普遍表示接口，
不要求新表示具有原 $N_j\to I/2$ 的弱极限。

$\mathcal T$ 不是整个 $\mathcal A$：
R160 的慢 Bell 元素具有首阶1而四次型0，故不在 $\mathcal G$，
从而不在 $\mathcal T$。
因为 $\mathcal T$ 含稠密的多项式，它也不是范数闭子代数。

本稿没有解决一般慢元素的标准闭理想问题、边界无限维不变格，
也没有从有限快类外推到完整 Hilbert 不变子空间问题。
