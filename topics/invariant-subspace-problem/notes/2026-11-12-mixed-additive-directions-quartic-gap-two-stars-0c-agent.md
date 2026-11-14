# 两个独立加性方向的四次型缺口与无限临界双星

日期：2026-11-12（UTC）。独占作者：critical_kernel。根代理预留 R146。
状态：以下定理与有限多方向扩充已完整证明。
慢方向没有快尾假设；不同方向不要求属于同一个加性乘子的解析函数域。

## 1. 两方向定理

记 $\mathcal A=\overline{\mathbb C[I,A]}$，$\chi$ 为唯一常数特征，
$\gamma_\zeta(T)=U_\zeta T U_\zeta^*$ 为实际 dyadic gauge。
对有界算子 $T$ 记

$$
\tau_4(T)=\liminf_{n\to\infty}
\frac{-\log\|T^n\|}{n^4}.
\tag{1.1}
$$

设 $B_0,B_1\in\mathcal A$，且：

1. $\chi(B_i)=0$；其首个非零形式阶分别为 $h_i\ge1$；
2. 对每个 dyadic $\zeta$，$\gamma_\zeta(B_i)-B_i$ 是某个真正
   收敛标量解析芽在 $A$ 上的通常全纯演算；
3. $r(z)$ 为真正解析芽，首阶为 $q\ge1$，并且

$$
q<h_0<q+h_1;
\tag{1.2}
$$

4. 快方向满足严格型差

$$
\boxed{
\tau_4(B_1)>
\frac{100}{15}(h_0-q)^4.
}
\tag{1.3}
$$

**定理1.1。** 实际有界算子

$$
S=B_0+r(A)B_1
\tag{1.4}
$$

单射且值域稠密，$S1$ 对 $A$ 循环。
它的首形式阶为 $h_0$，因此它非零。
所有非零谱参数处本来可逆，因为 $\chi(S)=0$。

这里 $h_0,h_1$ 不必是二的幂。
加性差必须是真解析芽；没有把任意范数代数元素的 gauge 差作这种解释。

## 2. 两条真实接口

### 2.1 子商中的解析首阶型

R140 证明：若 $L\subsetneq M$ 是闭 $A$ 不变空间，
则非零 Hilbert 子商 $Q=M/L$ 上的 $A_Q$ 单射、值域稠密且拟幂零。
若 $F(z)=z^\ell u(z)$ 为非零解析芽、$\ell\ge1,u(0)\ne0$，则

$$
\boxed{
\tau_4(F(A_Q))=\frac{100}{15}\ell^4.
}
\tag{2.1}
$$

它使用真实高位积的 WOT 极限，并非把子商当成原 Haar 模型。

直接推论是：若 $E\in\{A\}'$ 且

$$
\tau_4(E)>\frac{100}{15}\ell^4,
\tag{2.2}
$$

则对每个闭 $A$ 不变 $M$，

$$
\boxed{\overline{(F(A)+E)M}=M.}
\tag{2.3}
$$

证明可简述如下。令 $L=\overline{(F(A)+E)M}$。
若 $L\ne M$，则在非零商 $Q=M/L$ 上
$F(A_Q)=-E_Q$。压缩范数给
$\tau_4(E_Q)\ge\tau_4(E)$，与 (2.1)—(2.2) 矛盾。

式 (2.3) 是每个未知限制上的真实稠密像；不是由全空间的稠密性推得。

### 2.2 解析因子在每个不变限制上的稠密像

若 $d(z)=z^qv(z)$ 非零解析、$v(0)\ne0$，则

$$
\overline{d(A)M}=M
\tag{2.4}
$$

对每个闭 $A$ 不变 $M$ 成立。
真实单位 $v(A)$ 及其逆保持 $M$；R23 给
$\overline{A^qM}=M$。

若两个有界交换子 $D,T$ 分别在 $M$ 上有稠密像，则

$$
\overline{DTM}=M.
\tag{2.5}
$$

确实，$T M$ 在 $M$ 稠密，故 $DTM$ 在 $DM$ 稠密，再用 $DM$ 稠密。
这一步不要求任何有界逆。

## 3. 一个 gauge 差中的低阶解析头

记真实解析增量为

$$
b_{i,\zeta}(A)=\gamma_\zeta(B_i)-B_i.
$$

定义解析芽

$$
d_\zeta(z)=r(\zeta z)-r(z),\qquad
e_\zeta(z)=b_{0,\zeta}(z)+r(\zeta z)b_{1,\zeta}(z).
\tag{3.1}
$$

直接展开实际有界算子得到

$$
\boxed{
\gamma_\zeta(S)-S
=d_\zeta(A)B_1+e_\zeta(A).
}
\tag{3.2}
$$

令 $c_0\ne0$ 为 $B_0$ 的 $h_0$ 阶形式系数，
$c_r\ne0$ 为 $r$ 的 $q$ 阶系数。
当 $\zeta^{h_0}\ne1$ 时，

$$
\operatorname{ord}b_{0,\zeta}=h_0,\qquad
[z^{h_0}]b_{0,\zeta}=c_0(\zeta^{h_0}-1).
$$

总有 $\operatorname{ord}b_{1,\zeta}\ge h_1$，增量为零时阶记为无穷。
由 $h_0<q+h_1$，第二项不能取消 $e_\zeta$ 的首项，所以

$$
\operatorname{ord}e_\zeta=h_0
\qquad(\zeta^{h_0}\ne1).
\tag{3.3}
$$

当同时 $\zeta^q\ne1$ 时，$d_\zeta$ 的首阶为 $q$，
故真正解析商

$$
H_\zeta(z)=\frac{e_\zeta(z)}{d_\zeta(z)}
\tag{3.4}
$$

在零点附近收敛，并且

$$
\operatorname{ord}H_\zeta=h_0-q\ge1.
\tag{3.5}
$$

这里被除的是两个标量收敛解析芽，且已核对首阶；
没有除未知 $\mathcal A$ 元素，也没有除可能无界的闭乘子。

除外根满足 $\zeta^{h_0}=1$ 或 $\zeta^q=1$。
在 dyadic 根群中它们包含于有限群

$$
\mu_{2^d},\qquad d=\max\{v_2(h_0),v_2(q)\}.
\tag{3.6}
$$

若某个除外根仍有更高非零 $d_\zeta$，无需另作判断；
有限群已经足够后续 Fourier 论证。

## 4. 实际核与 Fourier 排除

令 $M=\ker S$，暂设它非零。$M$ 闭且 $A$ 不变。
对不在 (3.6) 中的 $\zeta$，由 (3.2)—(3.4)，

$$
\gamma_\zeta(S)-S
=d_\zeta(A)\bigl(B_1+H_\zeta(A)\bigr).
\tag{4.1}
$$

由 (1.3)、(3.5) 和 (2.3)，

$$
\overline{(B_1+H_\zeta(A))M}=M.
$$

再用 (2.4)—(2.5)，得到

$$
\boxed{
\overline{(\gamma_\zeta(S)-S)M}=M.
}
\tag{4.2}
$$

这个限制稠密性来自 R140 的实际子商型比较，
并非只由 $B_1+H_\zeta(A)$ 在整个 $H$ 上单射稠密。

记 $M_\zeta=U_\zeta M=\ker\gamma_\zeta(S)$。
全交换子的 $B$ 对称性给

$$
B((\gamma_\zeta(S)-S)M,M_\zeta)=0.
$$

由 (4.2)，

$$
B(M,U_\zeta M)=0
\qquad(\zeta\notin\mu_{2^d}).
\tag{4.3}
$$

R122 的后半段遂完整适用：对 $v,w\in M$，
$v(y)w(-1-y)\in L^1$ 只有有限子群中的 Fourier 系数可能非零，
故它在前 $d$ 位的每个物理柱上为常数。
非零闭 $A$ 不变空间的总本质支撑全测；
逐柱从可数稠密族选一个非零乘积，使该柱上的限制秩至多1。
故 $\dim M\le2^d$，与 $A$ 单射拟幂零不允许非零有限维不变空间矛盾。

因此 $\ker S=0$。$C$ 对称性给闭值域为 $H$。
$S$ 与 $A$ 交换且 $1$ 循环，故 $S1$ 循环。定理1.1证毕。

## 5. 快方向的四次型：保留真实占据估计

本节给 (1.3) 一个直接可检查的充分条件。

**引理5.1。** 设 $B\in\mathcal A$ 首形式阶为 $h\ge1$、首系数为
$\beta\ne0$。假设有实际分解

$$
B=F_K+E_K,\qquad F_K=A^hU_K,\quad U_K\in\mathcal A^\times,
\tag{5.1}
$$

并有

$$
\tau_4(E_K)\longrightarrow+\infty.
\tag{5.2}
$$

则

$$
\boxed{\tau_4(B)=\frac{100}{15}h^4.}
\tag{5.3}
$$

**证明：下界。** 记 $a_0=100h^4/15$。
R109 及实际单位因子的 $O(n)$ 对数误差给
$\tau_4(F_K)=a_0$。固定 $0<a<a_0$，以及
$0<b<\tau_4(E_K)$。存在有限常数 $C_K,D_K$，使所有整数 $n\ge0$ 有

$$
\|F_K^n\|\le C_K^n e^{-an^4},\qquad
\|E_K^n\|\le D_K^n e^{-bn^4}.
$$

有限个小 $n$ 可吸收进常数。交换性及二项展开给

$$
\begin{aligned}
\|B^n\|
&\le\sum_{j=0}^n\binom nj
C_K^jD_K^{n-j}e^{-aj^4-b(n-j)^4}\\
&\le(C_K+D_K)^n
\exp\!\left[-(a^{-1/3}+b^{-1/3})^{-3}n^4\right].
\end{aligned}
\tag{5.4}
$$

最后一步是四次 Hölder。
先固定 $K,b$ 取 $\liminf$，再令 $K$ 与可取的 $b$ 趋无穷，
最后令 $a\uparrow a_0$，得 $\tau_4(B)\ge a_0$。

**证明：上界。** 对任何 $T\in\mathcal A$，其固定形式系数满足

$$
W_n|\gamma_n(T)|\le\|T\|,\qquad W_n=\|A^n\|.
\tag{5.5}
$$

对多项式，此界由选取比其次数更长的物理头、压缩头0到头$n$
得到；范数逼近与固定系数连续性把它传给 $\mathcal A$。
$B^n$ 的首系数为 $\beta^n$，位于次数 $hn$，所以

$$
\|B^n\|\ge|\beta|^nW_{hn}.
$$

R109 的 $\tau_4(A^h)=100h^4/15$ 遂给反向不等式。
证毕。

### 5.1 超三次第一尾的明确应用

设

$$
B=\sum_{j\ge k}c_jY_j,\qquad
Y_j=N_j(I+N_j)^{-1},\qquad c_k\ne0,
\tag{5.6}
$$

且非零系数模长的非增重排 $c_\ell^*$ 满足

$$
\frac{-\log c_\ell^*}{\ell^3}\longrightarrow+\infty.
\tag{5.7}
$$

有限支持亦允许。此条件给 $\sum_j\sqrt{|c_j|}<\infty$，
所以 (5.6) 真实绝对范数收敛。

R106 的实际重复占据与不同指标分裂估计给，对尾

$$
E_K=\sum_{j\ge K}c_jY_j,
$$

存在 $\sigma_K<\infty$、$b_K\to\infty$，使

$$
\boxed{
\|E_K^n\|\le\sigma_K^n e^{-b_Kn^4}\qquad(n\ge1).
}
\tag{5.8}
$$

该估计保留 $N_j^2=\eta_jN_{j+1}$ 的真实进位，不是纯张量替代。
有限头为真正解析函数，其首阶为 $h=2^k$，首系数为 $c_k/d_k$；
它实际等于 $A^h$ 乘一个 $\mathcal A$ 单位。
引理5.1因而给

$$
\boxed{
\tau_4\!\left(\sum_{j\ge k}c_jY_j\right)
=\frac{100}{15}2^{4k}.
}
\tag{5.9}
$$

标量缩放不改变 $\tau_4$。
任意有限前缀、复相位和满足 (5.7) 的稀疏排列均允许。
没有从该算子的单射性反推 (5.9)。

## 6. 两个无限临界星：一个任意慢行和一个快行

取整数 $i<\ell<k$，并设

$$
B_0=\sum_{j\ge k}a_jY_j,\qquad
B_1=\sum_{j\ge k}c_jY_j,
\tag{6.1}
$$

其中 $a,c\in\ell^1$、$a_k\ne0$，
$c$ 的最低非零指标为 $k_1\ge k$。
对 $a$ 没有其他衰减或相位限制；
对 $c$ 假设 (5.7)，也可直接假设下文所需的型不等式。

考虑真正 Boolean 二次算子

$$
T=Y_iB_0+Y_\ell B_1.
\tag{6.2}
$$

有限解析比值

$$
r(z)=\frac{y_\ell(z)}{y_i(z)},\qquad
y_j(z)=\frac{z^{2^j}/d_j}{1+z^{2^j}/d_j},
\tag{6.3}
$$

在零点解析，其首阶为

$$
q=2^\ell-2^i,\qquad 0<q<2^k.
$$

这是先把两个有限解析函数的共同 $z^{2^i}$ 因子明确消去，
不使用无界 $Y_i^{-1}$。实际恒等式为

$$
T=Y_i\bigl(B_0+r(A)B_1\bigr).
\tag{6.4}
$$

这里 $h_0=2^k,h_1=2^{k_1}$，
$q<h_0<q+h_1$。
(5.9) 给

$$
\tau_4(B_1)=\frac{100}{15}h_1^4
>
\frac{100}{15}(h_0-q)^4.
$$

定理1.1证明括号中算子单射稠密。
$Y_i$ 本身是真解析 $A^{2^i}$ 乘单位，故也单射稠密。
因此

$$
\boxed{
T\text{ 单射稠密，}\quad T1\text{ 循环}.
}
\tag{6.5}
$$

本结论特别允许两个最低物理行都为无限支撑：
它不要求像 R139 那样把这些行全部收入一个有限解析头。

具体可取

$$
i=0,\quad \ell=1,\quad k=2,\qquad
a_j=(j+1)^{-2},\quad c_j=e^{-(j+1)^4}\quad(j\ge2).
\tag{6.6}
$$

其实际向量为

$$
T1=b_0^{\mathrm{phys}}
\sum_{j\ge2}(j+1)^{-2}b_j^{\mathrm{phys}}
+
b_1^{\mathrm{phys}}
\sum_{j\ge2}e^{-(j+1)^4}b_j^{\mathrm{phys}}.
\tag{6.7}
$$

它连续有界、非零，且两个低行都无限。
按 Boolean 单项式写法没有一次项；换成 Walsh 写法时，
每个行都精确满足 $\tau_i=a_i+\sum_{j\ne i}b_{ij}=0$。
这指一次 Boolean 项的消失，不声称所有 $A^{2^i}$ 的普通形式系数都消失：
较低位的高次进位仍可能贡献那些系数。
慢行不满足超三次快尾要求，但主证明完全不要求它满足。
本稿不据此声称已计算整个混合算子的精确 $\tau_4$。

## 7. 有限多个独立方向的扩充

设 $B_0,B_1,\ldots,B_s\in\mathcal A$ 均为非零临界加性解析
cocycle，首形式阶为 $h_0,h_1,\ldots,h_s$。
令 $r_\nu(z)$ 为非零解析芽，首阶 $q_\nu\ge1$，置

$$
S=B_0+\sum_{\nu=1}^s r_\nu(A)B_\nu,\qquad
q=\min_{\nu\ge1}q_\nu.
$$

假设

$$
q<h_0,\qquad
h_0<q_\nu+h_\nu\quad(1\le\nu\le s),
\tag{7.1}
$$

各 $\tau_\nu:=\tau_4(B_\nu)>0$，且

$$
\boxed{
\left(\sum_{\nu=1}^s\tau_\nu^{-1/3}\right)^{-3}
>
\frac{100}{15}(h_0-q)^4.
}
\tag{7.2}
$$

无穷型的逆三次根按0计。

**定理7.1。** 此时 $S$ 单射稠密，$S1$ 循环。

**证明。** 对任意 dyadic $\zeta$，所有
$r_\nu(\zeta z)-r_\nu(z)$ 都可被 $z^q$ 真解析整除。故

$$
\gamma_\zeta(S)-S
=A^q\left[F_\zeta(A)+
\sum_{\nu=1}^sC_{\nu,\zeta}(A)B_\nu\right],
\tag{7.3}
$$

其中

$$
\begin{aligned}
C_{\nu,\zeta}(z)
&=\frac{r_\nu(\zeta z)-r_\nu(z)}{z^q},\\
F_\zeta(z)
&=\frac{b_{0,\zeta}(z)+
\sum_{\nu=1}^s r_\nu(\zeta z)b_{\nu,\zeta}(z)}{z^q}.
\end{aligned}
$$

只要 $\zeta^{h_0}\ne1$，(7.1) 保证
$\operatorname{ord}F_\zeta=h_0-q$。

固定 $\zeta$。
乘一个有界交换因子至多增加 $O(n)$ 对数项，所以

$$
\tau_4(C_{\nu,\zeta}(A)B_\nu)\ge\tau_\nu.
$$

交换的有限和使用多项展开及四次 Hölder，与 (5.4) 相同地得到

$$
\tau_4\!\left(\sum_{\nu=1}^s
C_{\nu,\zeta}(A)B_\nu\right)
\ge
\left(\sum_{\nu=1}^s\tau_\nu^{-1/3}\right)^{-3}.
\tag{7.4}
$$

可先把每个 $\tau_\nu$ 换成严格较小的正数，吸收有限小次幂常数，
再取极限；各常数允许依赖这个固定 $\zeta$。
为零的 $C_{\nu,\zeta}$ 只会改善界。

(7.2)、R140 与 (7.3) 给每个闭不变 $M$ 上
$\gamma_\zeta(S)-S$ 的稠密像。
除外根 $\zeta^{h_0}=1$ 只构成有限 dyadic 子群。
其余 Fourier 证明与 §4 完全相同。证毕。

若 $q\ge h_0$，则还有一个不需要型假设的简单支路：
直接把 (7.3) 改按 $A^{h_0}$ 提取，
$\delta B_0/A^{h_0}$ 的字符非零，而其余各项的字符为零；
因而 gauge 差是 $A^{h_0}$ 乘实际单位。
本稿新增的型比较用于真正较低调制阶 $q<h_0$ 的情形。

## 8. 范围与剩余问题

本稿把 R140 的子商型约束用于两个或有限多个独立加性方向，
得到一个任意慢方向加若干快方向的混合循环类。
实际差的限制稠密性已经证明，因此没有把全空间 quasiaffinity
未经论证传给未知不变空间。

仍未覆盖两个都无四次型控制的独立慢临界行，
也未证明任意 $B_0+r(A)B_1$ 都单射。
没有把 $B_1$ 假设成 $B_0$ 的一个解析函数，没有使用一般
$\mathcal A$ 非零元素自动无核的未证命题。

