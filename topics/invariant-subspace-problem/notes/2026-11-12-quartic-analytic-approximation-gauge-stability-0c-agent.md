# 四次型解析逼近、精确有限 jet 与 gauge 稳定性

日期：2026-11-12（UTC）。独占作者：critical_kernel。根代理预留 R151。
状态：以下逼近类、子商型、有限放大稠密性及 gauge 排核均已完整证明。
本稿的类型假设不是任意算子范数逼近，也不把一般 $\mathcal A$ 元素
自动视为具有可控解析尾。

## 1. 定义与低阶系数的精确稳定

设 $\mathcal A=\overline{\mathbb C[I,A]}$。
对 $T\in\mathcal A$，记 $\operatorname{ord}T$ 为其最低非零形式阶，
零算子的阶为无穷。形式系数在 $\mathcal A$ 上连续且忠实。

定义 $\mathcal G$ 为满足下述条件的 $E\in\mathcal A$：

存在真正收敛的标量解析芽 $f_n$，使

$$
F_n=f_n(A),\qquad
\|E-F_n\|\longrightarrow0,\qquad
\tau_4(E-F_n)\longrightarrow+\infty.
\tag{1.1}
$$

这里 $\tau_4(0)=+\infty$。
每个 $f_n$ 的解析邻域可依赖 $n$；
只使用其通常全纯演算，不要求一个统一标量收敛半径。

### 1.1 类型上界迫使有限 jet 最终精确相同

R146/R148 使用的真实系数界为

$$
W_k|\gamma_k(T)|\le\|T\|,\qquad W_k=\|A^k\|.
$$

若非零 $T$ 的首阶为 $r$、首系数为 $\beta\ne0$，则

$$
\|T^m\|\ge|\beta|^mW_{rm}.
$$

因此 R109 给

$$
\boxed{
\tau_4(T)\le\frac{100}{15}(\operatorname{ord}T)^4.
}
\tag{1.2}
$$

首阶为0时同样给 $\tau_4(T)\le0$；有界算子的型至少为0，
所以非零常数特征的型就是0。

固定整数 $N\ge1$。
由 (1.1)，充分大 $n$ 有

$$
\tau_4(E-F_n)>\frac{100}{15}(N-1)^4.
$$

若该差非零，(1.2) 迫其首阶至少为 $N$；
为零时结论当然成立。故

$$
\boxed{
\gamma_k(F_n)=\gamma_k(E)
\quad(0\le k<N,\ n\text{充分大}).
}
\tag{1.3}
$$

这是**最终精确相等**，不是“这些系数趋于相同”。
因此可以重取子序列，使

$$
\operatorname{ord}(E-F_n)\ge n
\tag{1.4}
$$

同时保留 (1.1)。
保阶不是从范数逼近中擅自推得；它来自额外的尾型趋无穷
与尖锐的最低系数上界 (1.2)。

## 2. 代数与 gauge 稳定性

所有真解析演算均属于 $\mathcal G$，取恒等逼近即可。

### 2.1 有限和

若 $E,F\in\mathcal G$，分别取解析逼近 $E_n,F_n$，
尾为 $R_n,S_n$。有界交换算子的二项 Hölder 界给

$$
\tau_4(R_n+S_n)\ge
\bigl(\tau_4(R_n)^{-1/3}
+\tau_4(S_n)^{-1/3}\bigr)^{-3}
\longrightarrow+\infty.
\tag{2.1}
$$

范数尾也趋零，所以 $E+F\in\mathcal G$。
标量乘法和减法同样成立。

### 2.2 乘法

有精确分解

$$
EF-E_nF_n=(E-E_n)F+E_n(F-F_n).
\tag{2.2}
$$

固定一个有界交换因子只改变幂范数的 $O(m)$ 对数项，
故 (2.2) 中两个尾项的四次型分别至少是
$\tau_4(R_n),\tau_4(S_n)$。
再用 (2.1)，误差型趋无穷。
范数收敛保证 $E_n$ 一致有界，所以范数误差也趋零。
因此 $\mathcal G$ 是含全部解析演算的交换子代数。

### 2.3 单位的逆

若 $E\in\mathcal G$ 且 $\chi(E)\ne0$，
则 $E$ 为 $\mathcal A$ 单位。
由 (1.3)，充分大 $n$ 的 $E_n=f_n(A)$ 有相同的非零常数特征，
其逆是真解析芽 $(1/f_n)(A)$。
范数收敛给逆的一致有界性，且

$$
E^{-1}-E_n^{-1}
=-E^{-1}(E-E_n)E_n^{-1}.
\tag{2.3}
$$

右侧型至少为 $\tau_4(E-E_n)$，范数趋零。
故 $E^{-1}\in\mathcal G$。
这不涉及对零字符元素的有界除法。

### 2.4 Gauge

对每个 dyadic $\zeta$，
$\gamma_\zeta(E_n)=f_n(\zeta A)$ 仍是真解析演算，
且 gauge 等距、保乘法，所以

$$
\|\gamma_\zeta(E-E_n)\|=\|E-E_n\|,\qquad
\tau_4(\gamma_\zeta(E-E_n))=\tau_4(E-E_n).
$$

因此

$$
\boxed{\gamma_\zeta(\mathcal G)=\mathcal G.}
\tag{2.4}
$$

### 2.5 任意有限 Taylor 头可合法移出

给定 $E\in\mathcal G$ 与固定 $N$，令

$$
P_N(z)=\sum_{k=0}^{N-1}\gamma_k(E)z^k.
$$

$P_N(A)$ 是一个真正有限多项式，故

$$
E-P_N(A)\in\mathcal G.
\tag{2.5}
$$

更明确地，可以用 $f_n(A)-P_N(A)$ 逼近；
尾仍**恰好等于** $E-f_n(A)$，没有任何型损失。
由 (1.3)，充分大 $n$ 的标量解析芽 $f_n-P_N$
在零点低于 $N$ 的 Taylor 系数精确为零。
所以

$$
\operatorname{ord}(E-P_N(A))\ge N
$$

以及这些保阶解析逼近都是真实成立的。
本节没有把一次不受控的 Taylor 截断误差另当作快尾。

## 3. 全空间及每个非零子商上的精确型

**定理3.1。** 若非零 $E\in\mathcal G$ 的首阶为 $h$，则

$$
\boxed{\tau_4(E)=\frac{100}{15}h^4.}
\tag{3.1}
$$

对每个非零不变 Hilbert 子商 $Q=M/L$，还都有

$$
\boxed{
E_Q\ne0,\qquad
\tau_4(E_Q)=\frac{100}{15}h^4.
}
\tag{3.2}
$$

**全空间证明。**
$h=0$ 时 $E$ 为单位，型为0。
设 $h\ge1$。
(1.3) 保证充分大 $n$ 的解析 $F_n$ 首阶精确为 $h$，
所以 $\tau_4(F_n)=a:=100h^4/15$。
写 $E=F_n+R_n$，其中 $\tau_4(R_n)\to\infty$。
给 $F_n$ 和 $R_n$ 分别使用任意严格小于其型的指数上界，
二项 Hölder 给

$$
\tau_4(E)\ge
\bigl((a-\varepsilon)^{-1/3}
+b_n^{-1/3}\bigr)^{-3},
\qquad b_n<\tau_4(R_n).
$$

令 $b_n\to\infty$，再令 $\varepsilon\downarrow0$，
得到下界 $a$；(1.2) 给反向界。

**子商证明。**
R88 保证所有相关交换子保持 $M,L$。
压缩范数给

$$
\tau_4(E_Q)\ge\tau_4(E)=a.
$$

若 $\tau_4(E_Q)>a$（包括 $E_Q=0$），取 $b>a$
且 $b<\tau_4(E_Q)$。
同时 $(R_n)_Q$ 的型不小于 $\tau_4(R_n)\to\infty$。
由 $F_{n,Q}=E_Q-(R_n)_Q$ 及二项 Hölder，
充分大 $n$ 会得到

$$
\tau_4(F_{n,Q})>
a.
$$

但 R140 对真解析首阶给
$\tau_4(F_{n,Q})=a$，矛盾。
$h=0$ 时单位及逆都可诱导到子商，型为0，亦不可能为零。
证毕。

### 3.1 每个限制及有限放大的稠密像

设 $E\in\mathcal G$ 非零、$M$ 闭且 $A$ 不变。
若 $L=\overline{EM}$ 真小于 $M$，则非零商 $M/L$ 上 $E_Q=0$，
与 (3.2) 矛盾。因此

$$
\boxed{\overline{EM}=M.}
\tag{3.3}
$$

若 $\ker E\ne0$，取其为非零不变限制，在该子商上仍有 $E_Q=0$，
同样矛盾。因此 $E$ 全空间单射稠密。

R140 的解析子商型与高位 WOT 证明对每个有限放大成立；
尾的放大范数保持原值。
故以上证明逐字适用于

$$
E^{(d)}=E\otimes I_{\mathbb C^d}
$$

在每个闭 $A^{(d)}$ 不变空间上的限制：

$$
\boxed{
\overline{E^{(d)}\mathcal M}=\mathcal M
\quad(d<\infty).
}
\tag{3.4}
$$

特别由 R140 的有限测试向量论证，

$$
I\in\overline{E\,\mathbb C[A]}^{\mathrm{SOT}}.
\tag{3.5}
$$

这只是强算子拓扑的主理想近似。
没有据此声称范数闭主理想标准、包含某个指定 $A^r$，
或每个形式商都能作有界算子除法。

## 4. Gauge 差属于 $\mathcal G$ 时的全部核

**定理4.1。** 设 $X\in\mathcal A$ 非标量，并且

$$
\gamma_\zeta(X)-X\in\mathcal G
\qquad\text{对每个 dyadic }\zeta.
\tag{4.1}
$$

则对每个 $\lambda\in\mathbb C$，

$$
\boxed{
\ker(X-\lambda I)=0,\qquad
\overline{\operatorname{Ran}(X-\lambda I)}=H.
}
\tag{4.2}
$$

**证明。** 令 $h\ge1$ 是 $X$ 的第一个非零非常数形式阶。
对 $\zeta^h\ne1$，差 $\gamma_\zeta(X)-X$ 在 $h$ 阶的系数非零；
由 (4.1) 及 (3.3)，它在每个闭 $A$ 不变 $M$ 上值域稠密。

固定 $\lambda$，取 $M=\ker(X-\lambda I)$。
常数参数在 gauge 差中消去。
$C$ 对称性给

$$
B((\gamma_\zeta(X)-X)M,U_\zeta M)=0.
$$

限制稠密性遂给 $B(M,U_\zeta M)=0$，
对所有不满足 $\zeta^h=1$ 的 dyadic 根成立。
除外集合仅为有限子群 $\mu_{2^{v_2(h)}}$。

R122 的 Fourier/全本质支撑论证给
$\dim M\le2^{v_2(h)}$，与 $A$ 无非零有限维不变空间矛盾。
故 $M=0$；$C$ 对称性给稠密值域。证毕。

这里不要求差是真解析芽。
其在 $\mathcal G$ 中的真实有限放大/限制稠密性已经由 §3 独立证明。

## 5. 任意快解析逼近扰动的稳定性

**推论5.1。** 设 $B\in\mathcal A$ 的所有 dyadic 差都是真解析芽，
$E\in\mathcal G$。则每个非零

$$
S=B+E
\tag{5.1}
$$

都单射稠密，$S1$ 循环。
若 $S$ 非标量，则对全部 $\lambda$ 都有 $S-\lambda I$ 单射稠密。

证明直接来自

$$
\gamma_\zeta(S)-S
=(\gamma_\zeta(B)-B)+(\gamma_\zeta(E)-E)\in\mathcal G,
$$

因为真解析演算属于 $\mathcal G$，且 §2 给加法和 gauge 稳定性。
非零标量情形本来可逆。

这个结论没有前缀首阶大小、相位、系数缩放或 R148 的常数8限制。
原因不是省略了两项 harmonic 损失：
$\mathcal G$ 的稳定性使整个非零差再次具有与其**实际首阶**
相符的精确型，并可在每个未知限制上使用。
有限个低阶取消只改变最终首阶，不会破坏该类。

更一般地，若 $E_1,\ldots,E_s\in\mathcal G$，
$r_1,\ldots,r_s$ 为任意真解析芽，则

$$
B+\sum_{\nu=1}^s r_\nu(A)E_\nu
$$

只要非零便循环，因为整个有限扰动仍属于 $\mathcal G$。
不同 $E_\nu$ 不要求是同一个算子的解析函数。

本稿只对有限和使用这条代数稳定性；
任意无限和还须独立验证 (1.1)。

## 6. 实际满足定义的系列与一个严格非成员

### 6.1 超三次归一化幂级数及 Boolean 系列

以下已有真实占据估计可直接验证 (1.1)：

- R106 的第一尾
  $\sum_j c_jY_j$，其中非零模长降序后的
  $-\log c_\ell^*/\ell^3\to\infty$；
- R110 的标量归一化幂级数
  $\sum_n c_nA^n/W_n$，满足同一超三次重排条件；
- R115 的 Boolean 系列
  $\sum_J b_J\prod_{j\in J}Y_j$，
  对加权模长 $3^{|J|}|b_J|$ 满足超三次重排条件。

按普通 $A$ 形式首阶截断时，各有限头都是真正解析函数，
范数尾趋零，真实重复占据估计给尾型趋无穷；
从而均属于 $\mathcal G$。
这不要求全局 Walsh 次数有上界。

**范围限制：** R115 更一般允许任意有界因子 $V_n\in\mathcal A$。
若这些因子本身没有真解析性或已证的 $\mathcal G$ 结构，
其有限头未必是真解析演算，不能自动套本节。
本稿没有把 R115 的全部任意因子版本都划入 $\mathcal G$。

R148 构造的真实商

$$
F=\sum_{\substack{1\le i<j\\j\ge3}}
\alpha_i^2e^{-(i+j+4)^8}
\frac{y_i(A)}{y_0(A)}Y_j
$$

也属于 $\mathcal G$：
该稿已逐项给出归一化系数
$18d_0\alpha_i e^{-(i+j+4)^8}$、
有限解析因子及尾型趋无穷。
因此其与任意加性解析 cocycle 的非零和，
现可直接由推论5.1处理，不必再比较 $9^4$ 与 $8\cdot4^4$。

### 6.2 该类不是整个 $\mathcal A$

考虑保序算子（即保持非负函数的算子）

$$
B_{\rm slow}=\sum_{j\ge0}2^{-j}N_j.
\tag{6.1}
$$

它真实绝对范数收敛，属于 $\mathcal A$，
首形式阶为1。
每个 dyadic gauge 差仅改变有限多个 $j$，
因而是真正有限多项式。

但其四次型为0。
因为 $N_j$ 都保持非负函数且彼此交换，
$B_{\rm slow}^n$ 的展开中包含保序项

$$
n!\,2^{-n(n-1)/2}N_0N_1\cdots N_{n-1}.
$$

真实二进位乘积给

$$
\|N_0N_1\cdots N_{n-1}\|
=\frac{W_{2^n-1}}{\prod_{j=0}^{n-1}d_j}=1.
$$

保序算子序的范数单调性遂给

$$
\|B_{\rm slow}^n\|
\ge n!\,2^{-n(n-1)/2}.
$$

这里没有声称 $N_j$ 是 Hilbert 意义的自伴正算子。
所用范数单调性来自 $0\le S\le T$ 时
$|Sx|\le S|x|\le T|x|$。

其负对数至多为 $O(n^2)$，而有界算子的型至少为0，故

$$
\tau_4(B_{\rm slow})=0.
\tag{6.2}
$$

若它属于 $\mathcal G$，(3.1) 将给首阶1的型 $100/15$，矛盾。
所以 $\mathcal G$ 是严格的结构类；
其定义不能由“多项式在 $\mathcal A$ 中范数稠密”代替。

另一方面 $B_{\rm slow}$ 属于已有的加性解析 cocycle 类。
因此 §5 确允许一个不属于 $\mathcal G$ 的慢方向
与任意 $\mathcal G$ 扰动相加。

## 7. 对闭分式和剩余核问题的准确意义

(3.4) 使每个非零 $\mathcal G$ 元素都可作为 R143 附录中的受控分母：
对任意有界交换的分子 $P$，
最大闭商 $E^{-1}P$ 的 $\operatorname{Ran}E$ 图核心
可由有限放大稠密性证明，进而得到全空间的 $C$ 自伴性。

这仍不意味着未知不变限制继承该共轭，
也不使任意自然平方的定义域变成全空间。
一般两个独立慢临界行、任意非解析规范代数元素及完整 ISP
仍未解决。

本稿没有给 $\mathcal G$ 的范数闭包、所有有界商或所有范数闭主理想
作未证分类；其证明只使用 (1.1)、精确系数稳定、真实幂型和已建立的
gauge 跨核机制。

