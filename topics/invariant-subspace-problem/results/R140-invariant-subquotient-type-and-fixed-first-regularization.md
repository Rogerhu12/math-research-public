# R140：不变子商四次型与第一阶固定正则化

日期：2026-11-12。作者：l2_moments，独占稿；完整结果 R140。
状态：本稿各定理完整证明。它给出一般第一阶限制问题的精确有界化，以及 R109/R110 快速尾类的严格正结论；没有证明所有复 $\ell^2$ 第一阶限制均有稠密值域。

依赖：R23 的高阶收缩多项式强近似单位；R88 的交换子强多项式闭包；R109 的实际权公式及有限高位积；R110 的归一化幂重复占据估计；R125/R128 的第一阶闭乘子及正分量预解式。新的部分在于把真实高位信息传到所有不变子商、有限放大和固定正则化图核心。

## 1. 不变子商的实际表示

设 $N\subseteq M\subseteq H$ 是两个闭 $A$ 不变子空间。用
$$
K=M\ominus N
$$
等距表示 Hilbert 商 $M/N$。若 $T$ 保持 $M,N$，其诱导算子记为
$$
T_Q=P_KT|_K.
$$
对任何多项式 $p$，
$$
p(A_Q)=P_Kp(A)|_K,\qquad
\|p(A_Q)\|\le\|p(A)\|.
\tag{1.1}
$$
等式来自诱导映射的乘法性；并非把任意正交压缩都当作乘法同态。

R88 说明每个 $T\in\{A\}'$ 都是 $A$ 的多项式的强算子极限。因此它保持每个闭 $A$ 不变空间，特别保持 $M,N$，故 $T_Q$ 总有定义；诱导算子之间保留原有的交换和代数恒等式。

### 1.1 $A_Q$ 单射且值域稠密

R23 给多项式 $E_n=e_n(A)$，满足
$$
\|E_n\|\le1,\qquad E_n\to I\text{ 强收敛},\qquad
\operatorname{ord}e_n\to\infty.
\tag{1.2}
$$
固定 $r\ge1$ 后，充分大 $n$ 可写
$$
E_n=A^rR_{n,r}(A),
$$
其中每个 $R_{n,r}(A)$ 有界；无需一致范数界。

若 $A_Q(x+N)=0$，即 $x\in M$ 且 $Ax\in N$，则
$$
E_nx=R_{n,1}(A)Ax\in N.
$$
$N$ 闭且 $E_nx\to x$，故 $x\in N$。所以 $A_Q$ 单射。

又对每个 $x\in M$，$E_nx$ 属于 $A^rM$，并趋于 $x$。取商得
$$
\overline{\operatorname{Ran}A_Q^r}=Q
\quad(r\ge1).
\tag{1.3}
$$
这同时给 $A_Q$ 的稠密值域。由 (1.1)，
$\|A_Q^n\|\le W_n$，故 $A_Q$ 拟幂零。

因此在非零不变子商中，不能因为取了商就让 $A$ 出现零特征向量。这里真正使用的是 R23，而非只用原 $A$ 单射。

## 2. 固定高位积的弱极限传到子商

沿用
$$
N_j=\frac{A^{2^j}}{d_j},\qquad d_j=W_{2^j},
\qquad \|N_j-E_j\|\le\eta_j.
$$
对固定正整数 $m$，令 $J_m$ 为其二进位支撑，$q=|J_m|$。实际恒等式为
$$
T_{j,m}:=\frac{A^{m2^j}}{W_{m2^j}}
=\prod_{\ell\in J_m}N_{j+\ell}.
\tag{2.1}
$$
它与 $\prod_{\ell\in J_m}E_{j+\ell}$ 的算子范数差趋零，且各自范数不超过一个统一常数。

若两个测试向量都为有限柱，并且这些高位超过其全部坐标，则逐位参考常数的
$\langle E_\ell1,1\rangle=1/2$ 给矩阵元恰为原矩阵元的 $2^{-q}$ 倍。用有限柱稠密性和一致有界性扩展，得到
$$
\boxed{T_{j,m}\ \xrightarrow{\mathrm{WOT}}\ 2^{-q}I.}
\tag{2.2}
$$
这里用的是弱算子极限，不是原空间中的固定向量范数极限。

压到 $K=M\ominus N$ 后，(1.1) 给
$$
(T_{j,m})_Q
=\frac{A_Q^{m2^j}}{W_{m2^j}}
=P_KT_{j,m}|_K
\ \xrightarrow{\mathrm{WOT}}\ 2^{-q}I_Q.
\tag{2.3}
$$
所以对任意固定非零 $x\in Q$，
$$
\liminf_j
\left\|\frac{A_Q^{m2^j}}{W_{m2^j}}x\right\|
\ge2^{-q}\|x\|.
\tag{2.4}
$$
这个常数比 R109 原限制的 $2^{-q/2}$ 弱，但仍严格为正，足以决定四次对数型。

## 3. 任意非零子商上解析首阶的精确四次型

对有界算子 $B$ 记
$$
\tau_4(B)=\liminf_{n\to\infty}\frac{-\log\|B^n\|}{n^4}.
$$
设
$$
F(z)=z^ru(z),\qquad r\ge1,\quad u(0)\ne0
$$
为收敛解析芽。由于 $A_Q$ 拟幂零，$u(A_Q)$ 有界可逆。

**定理 3.1。** 对每个非零不变子商 $Q=M/N$，
$$
\boxed{\tau_4(F(A_Q))=\frac{100}{15}r^4.}
\tag{3.1}
$$

**证明。** 实际权满足
$$
-\log W_n
=100D_4(n)-105D_3(n)
+\sum_{\ell:b_\ell(n)=1}(150\ell+25)2^\ell,
$$
其中 $D_s(n)=\sum_{\ell:b_\ell(n)=1}2^{s\ell}$。由
$D_4(n)\ge n^4/15$、$D_3(n)\le n^3$，
$$
-\log W_n\ge\frac{100}{15}n^4-105n^3.
\tag{3.2}
$$
又 $\|F(A_Q)^n\|\le W_{rn}\|u(A_Q)\|^n$，故 (3.2) 给
$\tau_4(F(A_Q))\ge100r^4/15$。

反向固定正整数 $m$，令
$$
n_{j,m}=\left\lceil\frac{m2^j}{r}\right\rceil,
\qquad rn_{j,m}=m2^j+t_{j,m},\quad0\le t_{j,m}<r.
$$
取固定非零 $x\in Q$。$A_Q$ 单射，故有限组 $A_Q^tx$（$0\le t<r$）均非零；对它们同时使用 (2.4)，得到某个 $c_{x,m}>0$，使充分大 $j$ 时
$$
\|A_Q^{rn_{j,m}}\|
\ge c_{x,m}W_{m2^j}.
\tag{3.3}
$$
上界由 $\|A_Q\|\le\|A\|<1$ 给
$$
\|A_Q^{rn_{j,m}}\|\le W_{m2^j}.
$$
$u(A_Q)$ 及其逆的固定范数只带来 $O(n_{j,m})$ 的对数误差，所以
$$
-\log\|F(A_Q)^{n_{j,m}}\|
=-\log W_{m2^j}+O(n_{j,m}+1).
$$
固定 $m$ 时，实际权公式给
$$
\lim_{j\to\infty}
\frac{-\log\|F(A_Q)^{n_{j,m}}\|}{n_{j,m}^4}
=100r^4\frac{D_4(m)}{m^4}.
\tag{3.4}
$$
取 $m=2^q-1$，每次先固定 $q$ 再令 $j\to\infty$，最后令 $q\to\infty$；
因 $D_4(2^q-1)/(2^q-1)^4\to1/15$，得到反向界。证毕。

这一证明没有假定压缩保持原范数，也没有将未知商空间视为同一个具体 $L^2$ 模型。弱矩阵元极限已经提供全部所需下界。

## 4. 尾型排除变为每个不变限制上的稠密值域

**定理 4.1。** 设
$$
S=F(A)+B,\qquad B\in\{A\}',
$$
其中 $F(z)=z^ru(z)$、$r\ge1$、$u(0)\ne0$，且
$$
\tau_4(B)>\frac{100}{15}r^4.
\tag{4.1}
$$
则对每个闭 $A$ 不变 $M$，
$$
\boxed{\overline{SM}=M.}
\tag{4.2}
$$
全空间的单射性仍由 R109 的对应限制论证给出。

**证明。** 令 $N=\overline{SM}\subseteq M$。$S$ 与 $A$ 交换，故 $N$ 是闭 $A$ 不变空间，所有相关有界交换子都保持 $M,N$。若 $N\ne M$，则非零商 $Q=M/N$ 上
$$
S_Q=0,\qquad F(A_Q)=-B_Q.
$$
又 $\|B_Q^n\|\le\|B^n\|$，所以
$$
\tau_4(F(A_Q))=\tau_4(B_Q)\ge\tau_4(B)
>\frac{100}{15}r^4,
$$
与定理 3.1 矛盾。故 $N=M$。证毕。

这是对具体算子分解的充分条件，不是从全空间稠密值域直接推得不变限制稠密。

## 5. $80/3$ 归一化幂级数类的完整加强

设
$$
S=\sum_{n\ge1}c_n\frac{A^n}{W_n},\qquad
r=\min\{n:c_n\ne0\},
$$
其中非零系数模长的非增重排为 $c_\ell^*$，满足
$$
\Gamma(c):=\liminf_{\ell\to\infty}
\frac{-\log c_\ell^*}{\ell^3}
>\frac{80}{3}r^4.
\tag{5.1}
$$
有限支持也包括在结论中。

**推论 5.1。** 这类 $S$ 不仅单射稠密且 $S1$ 循环，而且
$$
\boxed{\overline{SM}=M
\quad\text{对每个闭 }A\text{ 不变 }M.}
\tag{5.2}
$$

为明确阈值没有被提升为较强的 Banach 主理想条件，重述 R110 的相关范数估计。取
$$
\frac{80}{3}r^4<\gamma<\Gamma(c),\qquad
0<\varepsilon<1,\qquad
D=\frac{(1-\varepsilon)\gamma}{4}>\frac{100}{15}r^4.
$$
令
$$
B_K=\sum_{n\ge K}c_n\frac{A^n}{W_n},\qquad
A_K=\frac14\left(\sum_{n\ge K}n^{-4/3}\right)^{-3},
\qquad
b_K=(A_K^{-1/3}+D^{-1/3})^{-3}.
$$
则 $A_K\to\infty$、$b_K\to D$。

R110 的真实重复占据界是
$$
\left\|\left(\frac{A^n}{W_n}\right)^s\right\|
\le\exp\left[-\frac14n^4(s-1)^4\right].
$$
对 $B_K^N$ 的一个有序项，若出现 $d$ 个不同指标，加权 Hölder 给重复部分代价至少
$A_K(N-d)^4$。删除有限多个最大系数并取足够大 $K$ 后，重排假设使这 $d$ 个不同系数的 $(1-\varepsilon)$ 次模长部分至少支付 $Dd^4$。四次 Hölder 于是给统一代价 $b_KN^4$；保留的 $\varepsilon$ 次系数按全部有序项求和，得到真实范数不等式
$$
\|B_K^N\|
\le
\left(\sum_{n\ge K}|c_n|^\varepsilon\right)^N e^{-b_KN^4}.
\tag{5.3}
$$
(5.1) 保证该一次尾和有限。固定次幂可先对有限和证明，再用范数收敛取极限。

取 $K>r$ 足够大，则
$$
\tau_4(B_K)\ge b_K>\frac{100}{15}r^4.
$$
剩余有限头
$$
F_K(z)=\sum_{1\le n<K}\frac{c_n}{W_n}z^n
$$
首阶为 $r$。定理 4.1 给 (5.2)。有限支持时直接用
$S=A^ru(A)$、$u(A)$ 及其逆保持 $M$，并用 R23 的 $\overline{A^rM}=M$。

## 6. 有限放大与强算子主理想

上述结论还对每个有限放大
$$
A^{(d)}=A\otimes I_{\mathbb C^d},\qquad
S^{(d)}=S\otimes I_{\mathbb C^d}
$$
成立。理由如下：

1. R23 的 $E_n^{(d)}$ 仍收缩并强趋恒等，且任意固定高位积仍
   WOT 收敛到 $2^{-q}I$。
2. 若 $B\in\{A\}'$，R88 的多项式强逼近在有限放大仍强收敛到
   $B^{(d)}$：每个测试向量只有有限个 $H$ 分量。因此任何闭
   $A^{(d)}$ 不变空间被 $B^{(d)}$ 保持。
3. 对这些不变空间及其商，§§1–4 的每一个压缩、单射、稠密像与型估计都保持；并有
   $\|(B^{(d)})^n\|=\|B^n\|$。

因此对定理 4.1 及推论 5.1 的 $S$，
$$
\overline{S^{(d)}M}=M
$$
对所有有限 $d$ 和所有闭 $A^{(d)}$ 不变 $M$ 成立。

取任意有限组 $x_1,\ldots,x_d\in H$，令
$$
M=\overline{\{(p(A)x_1,\ldots,p(A)x_d):p\in\mathbb C[z]\}}.
$$
有限放大结论使 $(x_1,\ldots,x_d)$ 可由同一个多项式的向量
$(p(A)Sx_1,\ldots,p(A)Sx_d)$ 逼近。于是
$$
\boxed{I\in\overline{\{S\,p(A):p\in\mathbb C[z]\}}^{\mathrm{SOT}}.}
\tag{6.1}
$$

(6.1) 是有限测试向量意义下的强拓扑闭包结论。证明没有给逼近算子的统一范数界，也没有据此声称存在一列在全空间强收敛且具有所需范数界的具体多项式。

尤其，(4.2)、(5.2) 或 (6.1) **不自动推出**
$\overline{S\mathcal A}^{\|\cdot\|}$ 是某个标准主理想，或包含某个指定
$A^r$。前者研究这个具体 Hilbert 表示中的不变子空间和强算子拓扑；后者要求算子范数中的统一逼近。本文没有构造范数 Bézout 证书，也没有将 R118 的较强主理想阈值降到 $80/3$。

## 7. 任意复第一阶限制的固定有界正则化

现在回到一般
$$
u=a_*+\sum_ja_j\chi_j\ne0,\qquad a\in\ell^2,\qquad X=X_u.
$$
不加任何快速尾或相位缺陷条件。把
$$
a=b_1-b_2+i b_3-i b_4,\qquad b_\nu\ge0,\quad b_\nu\in\ell^2,
$$
取为实部、虚部的正负部分；记 $\lambda=(1,-1,i,-i)$。R128 给收缩预解式
$$
R_\nu(t)=(I+tX_{b_\nu})^{-1}\in\{A\}',\qquad t>0,
$$
零分量取 $R_\nu(t)=I$。置
$$
R(t)=\prod_{\nu=1}^4R_\nu(t),\qquad S(t)=XR(t).
\tag{7.1}
$$
R128 的含定义域恒等式为
$$
S(t)
=a_*R(t)+\frac1t\sum_{\nu=1}^4
\lambda_\nu(I-R_\nu(t))
\prod_{\mu\ne\nu}R_\mu(t),
\tag{7.2}
$$
所以 $S(t)$ 是有界交换子，且
$\operatorname{Ran}R(t)\subseteq\operatorname{Dom}X$。
$R(t)\to I$ 强收敛；对每个 $x\in\operatorname{Dom}X$，
$$
R(t)x\to x,\qquad XR(t)x=R(t)Xx\to Xx.
\tag{7.3}
$$
R128 还给每个闭 $A$ 不变 $M$ 上的
$$
X(\operatorname{Dom}X\cap M)\subseteq M.
\tag{7.4}
$$

### 7.1 不同正则化参数只相差有界交换单位

对 $s,t>0$，单个预解式的恒等式为
$$
R_\nu(s)=R_\nu(t)U_\nu(s,t),\qquad
U_\nu(s,t)=\frac tsI+\left(1-\frac ts\right)R_\nu(s).
\tag{7.5}
$$
它可直接由
$(I+tX_{b_\nu})R_\nu(s)=\frac tsI+(1-\frac ts)R_\nu(s)$
验证。交换 $s,t$ 后再相乘，利用 $R_\nu(t)$ 单射，得
$$
U_\nu(s,t)U_\nu(t,s)=I.
$$
故每个 $U_\nu(s,t)$ 是有界交换单位；所有因子交换。设
$$
U(s,t)=\prod_{\nu=1}^4U_\nu(s,t).
$$
则
$$
\boxed{R(s)=R(t)U(s,t),\qquad S(s)=S(t)U(s,t).}
\tag{7.6}
$$
每个 $U(s,t)$ 及其逆保持所有闭 $A$ 不变空间。因此对任意固定 $M$，
$$
R(s)M=R(t)M,\qquad S(s)M=S(t)M.
\tag{7.7}
$$
这是真正的像集合相等，不仅是闭包相等。

### 7.2 固定参数的图核心及准确等价

对任意固定 $t>0$，
$$
\boxed{R(t)M\text{ 是 }X_M
\text{ 的图核心},\quad
X_M=X|_{\operatorname{Dom}X\cap M}.}
\tag{7.8}
$$
因为对 $x\in\operatorname{Dom}X\cap M$，(7.3) 的 $R(s)x$ 给图逼近，而由 (7.7)，每个 $R(s)x$ 都属于同一个固定集合 $R(t)M$。该集合也确包含于 $X_M$ 的域。

取图核心的像并闭包，得到
$$
\boxed{
\overline{X(\operatorname{Dom}X\cap M)}
=\overline{S(t)M}
\quad\text{对每个固定 }t>0.
}
\tag{7.9}
$$

R125 保证非零第一阶 $X$ 单射。每个 $R_\nu(t)$ 单射，所以 $R(t)$、
$S(t)$ 都单射。$S(t)\in\{A\}'$ 的 $C$ 对称性又给其全空间值域稠密。
然而这两个全空间性质不能代替 (7.9) 右侧在每个未知 $M$ 上的稠密性。一般复第一阶限制问题被准确化为：

> 对这里特定的有界交换子 $S(t)$，是否对每个闭 $A$ 不变 $M$ 都有
> $\overline{S(t)M}=M$？

相位缺陷有限且不可和的类由 R134 已在每个限制上满射；增生或经旋转增生的类有 R128 的稠密像结论；上述尾型准则若适用于某个有界正则化 $S(t)$，则也立即给肯定答案。本文不预设它对所有一般 $S(t)$ 自动成立。

## 8. 一个严格的使用界线

R138 的全平面连续谱类仍满足全空间 $\ker X=0$、稠密值域，并且具有有限柱的弱零近似特征向量。那些近似向量没有被证明位于任意指定的未知不变子空间 $M$，因此不能把全空间谱分类直接当作每个限制的谱分类。

同样，R132 证明 $X$ 将其定义域内的全空间循环向量送为循环向量；这不能直接用于一个真不变空间内部，因为其向量对原 $A$ 本来就不循环。式 (7.9) 给出需要补齐的准确有界范围命题，而不是由稠密性省略该命题。

另一方面，§§1–6 已给可直接使用的新正结论：真实四次尾型排除对所有非零子商有效，从而相应算子在全部不变限制及全部有限放大中具有稠密像，并有强主理想近似。其证明完全保留实际归一化高位幂和商空间范数，没有借用未知不变空间的函数点值或有限 chaos 向量。
