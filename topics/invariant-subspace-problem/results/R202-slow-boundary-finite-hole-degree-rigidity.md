# R202：慢边界符号的有限孔次数刚性与唯一长进位

日期：2026-11-12（UTC）。作者：l2_moments。状态：已证明。

本文在负整数边界表示中工作，证明有限孔次数的向量不可能藏在已构造的慢符号非真空核中。所用系数提取是实际矩阵元，不是纯模型极限，也不把一个很小的绝对进位误差除以更小的提取系数。

## 1. 两种“次数”必须区分

沿用 R174、R185 的边界空间
$$
\mathcal H_-=\ell^2(\mathbb N_0),\qquad
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}.
$$
对有限集合 $S\subseteq\mathbb N_0$，记
$$
n(S)=\sum_{j\in S}2^j,\qquad e_S=e_{n(S)}.
$$
这里 $S$ 表示边界真空上有限多个被占据的物理位，也称有限孔集合。
定义
$$
\mathcal H^-_{\le p}
=\overline{\operatorname{span}}\{e_S:|S|\le p\}.
\tag{1.1}
$$
这是在边界正交基 $e_S$ 中的次数完成空间。
它不是把原 Haar 表示中的 Walsh 次数结论直接搬过来；
两个表示的实际算子作用并不相同。

另定义物理有限头
$$
\mathcal F_m=\operatorname{span}\{e_n:0\le n<2^m\}
=\operatorname{span}\{e_S:S\subseteq\{0,\ldots,m-1\}\},
\qquad m\ge0.
\tag{1.2}
$$
特别 $\mathcal F_0=\mathbb Ce_0$。
“有限孔次数”允许孔位无限远；“有限头”则只允许有限多个物理位。

记
$$
W_0=1,\qquad W_n=\prod_{\nu=1}^n\alpha_{v_2(\nu)},
\qquad d_j=W_{2^j},\qquad
\mathsf N_j=B^{2^j}/d_j.
$$
本文的慢符号为
$$
T_N=\sum_{j\ge0}a_j\mathsf N_j,\qquad a_j=(j+1)^{-2}.
\tag{1.3}
$$
该和按算子范数收敛，且所有 $a_j>0$。

**定理1.1（带明确支撑界的有限头反向刚性）。**
设 $p,m\ge0$ 为整数。如果
$$
x\in\mathcal H^-_{\le p},\qquad T_Nx\in\mathcal F_m,
$$
则
$$
\boxed{
x\in\mathcal F_{m+C_p},
\qquad C_p=\frac{p(p+1)(p+2)}3.
}
\tag{1.4}
$$

因此，对 R185 的真实慢边界核 $M_N=\ker T_N$，
$$
\boxed{
M_N\cap\mathcal H^-_{\le p}=\mathbb Ce_0
\quad\text{对每个有限 }p.
}
\tag{1.5}
$$
特别，R185 构造的非真空核向量必有任意高的孔次数。

本文还证明更一般的返回刚性：

**定理1.2（有限次数返回只能来自有限头）。**
若 $x$ 与 $T_Nx$ 都具有某个有限孔次数，则 $x$ 属于一个有限头。
反向显然成立，因为 $T_N$ 保持每个 $\mathcal F_m$。

## 2. 真实矩阵行与进位系数

对任意 $n\ge0$，
$$
(T_Nx)_n
=\sum_{k\ge0}a_k\gamma_{n,k}\,x_{n+2^k},
\qquad
\gamma_{n,k}
=\frac{W_{n+2^k}}{W_nd_k}\in(0,1].
\tag{2.1}
$$
由 $\|\mathsf N_k\|=1$ 及 $a\in\ell^1$，
算子级数与该坐标级数均真实收敛。

若 $n$ 的第 $k$ 位为 0，则
$$
\gamma_{n,k}=1.
$$
若从第 $k$ 位起恰有 $\ell\ge1$ 个连续 1，随后为 0，
则
$$
\boxed{\gamma_{n,k}=\alpha_{k+\ell}/\alpha_k.}
\tag{2.2}
$$
这是 R200 的实际 carry 恒等式；也可从
$\mathsf N_k=E_k+\eta_kE_k^*\mathsf N_{k+1}$
递推得到。本文会使用该系数严格非零，
而不会声称它有一个与孔位无关的正下界。

记 $\nu(n)$ 为 $n$ 的二进位 1 的个数。
若第 $k$ 位为 0，则
$$
\nu(n+2^k)=\nu(n)+1.
\tag{2.3}
$$
若它为 1，且由该位开始的连续 1 串长度为 $\ell_k$，则
$$
\nu(n+2^k)=\nu(n)-\ell_k+1.
\tag{2.4}
$$

## 3. 唯一长进位引理

**引理3.1。**
设 $p\ge1$，$S$ 恰有 $p$ 个孔。
设 $j\in S$，$0\le i<j$，并满足：

- $S\cap\{i,\ldots,j-1\}=\varnothing$；
- 若 $i>0$，则 $i-1\notin S$；
- $L:=j-i\ge p$。

令
$$
n=n(S)-2^i.
\tag{3.1}
$$
则 $n$ 的孔集合恰为
$$
(S\setminus\{j\})\cup\{i,\ldots,j-1\}.
\tag{3.2}
$$
它有一段两端隔开的长 1 串 $[i,j)$，
其余全部 1 合计只有 $p-1$ 个。
对任意 $x\in\mathcal H^-_{\le p}$，
$$
\boxed{
(T_Nx)_n
=a_i\frac{\alpha_j}{\alpha_i}\,x_{n(S)}.
}
\tag{3.3}
$$

**证明。**
$n$ 的第 $j$ 位为 0；
若 $i>0$，第 $i-1$ 位也为 0，
所以长串确不会与外部连续段合并。
其总次数为
$$
\nu(n)=p-1+L.
$$
逐个检查 (2.1) 中所有加法位置。

1. 若第 $k$ 位为 0，包括 $k=j$ 及任何更高的空位，
   则由 (2.3)
   $$
   \nu(n+2^k)=p+L>p,
   $$
   对应输入系数为零。

2. 若 $k=i$，整段 $L$ 个 1 恰被进位清除，恢复原集合 $S$：
   $$
   n+2^i=n(S),\qquad \nu(n+2^i)=p.
   $$
   (2.2) 给它的实际系数 $\alpha_j/\alpha_i>0$。

3. 若 $i<k<j$，由第 $k$ 位开始的连续串长度为 $j-k=L-(k-i)$，
   所以
   $$
   \nu(n+2^k)=p+k-i>p.
   $$

4. 若 $k<i$ 且第 $k$ 位为 1，
   它的连续串不能跨过第 $i-1$ 位的隔离零；
   若 $k>j$ 且第 $k$ 位为 1，
   它的连续串也完全位于长串之外。
   无论这些低位或顶部连续段如何排列，
   它们总共只含 $p-1$ 个 1。
   因此 $\ell_k\le p-1<L$，由 (2.4)
   $$
   \nu(n+2^k)=p+L-\ell_k>p.
   $$

以上覆盖所有 $k\ge0$。
仅 $k=i$ 保留次数不超过 $p$ 的输入，得到 (3.3)。
全部等式都在真实矩阵行上成立，没有遗漏高位或顶部的连续进位。证毕。

隔离零不可省去：若长串与其下方原有的孔相连，
较低的加法位置可能产生更低次数的输入，就不再是唯一项。
下面每次选择 $i$ 都明确保留这个隔离零。

## 4. 顶次数只能占据一个明确有限头

**引理4.1。**
若 $p\ge1$，
$$
x\in\mathcal H^-_{\le p},\qquad T_Nx\in\mathcal F_m,
$$
则 $x$ 的第 $p$ 齐次部分 $x^{[p]}$ 满足
$$
\boxed{
x^{[p]}\in\mathcal F_{m+p(p+1)}.
}
\tag{4.1}
$$

**证明。**
假设 $|S|=p$ 且
$$
\max S\ge m+p(p+1).
\tag{4.2}
$$
把 $S$ 中不小于 $m$ 的孔递增写成
$$
j_1<\cdots<j_s,\qquad s\le p,
$$
并添加一个仅用于计数的起点 $j_0=m-1$。
如果每个间距 $j_\ell-j_{\ell-1}\le p+1$，则
$$
j_s\le m-1+s(p+1)\le m-1+p(p+1),
$$
与 (4.2) 矛盾。
故存在 $\ell$ 使
$$
j_\ell-j_{\ell-1}\ge p+2.
$$
取
$$
j=j_\ell,\qquad i=j_{\ell-1}+2.
\tag{4.3}
$$
于是 $j-i\ge p$。

若 $\ell>1$，$j_{\ell-1}$ 是实际前一个孔，
所以 $i-1=j_{\ell-1}+1$ 是空位，
且 $[i,j)$ 全空。
若 $\ell=1$，间距条件给 $j_1\ge m+p+1$，
所以从第 $m$ 位起至 $j_1-1$ 都为空；
此时 $i=m+1$，同样有隔离零和空段。
这也覆盖 $m=0$ 的情况。

由 (4.3) 有 $i\ge m+1$。
输出 $n=n(S)-2^i$ 含第 $i$ 位，
故
$$
n\ge2^i\ge2^{m+1}>2^m-1.
$$
因此 $(T_Nx)_n=0$。
应用引理3.1，
$$
0=a_i(\alpha_j/\alpha_i)x_{n(S)}.
$$
所有因子严格非零，故 $x_{n(S)}=0$。
所以所有第 $p$ 阶非零系数的孔位都小于 $m+p(p+1)$，证明 (4.1)。

注意：没有对极小系数 $\alpha_j/\alpha_i$ 做任何误差除法。
这里右侧恰有唯一一项，而且左侧恰为零。证毕。

## 5. 逐层有限支撑界

每个 $\mathsf N_j$ 都降低整数索引，
因此保持 $\mathcal F_m$；
范数和 $T_N$ 也保持它。

现在对 $p$ 归纳证明定理1.1。
$p=0$ 时 $x$ 是真空的标量倍，属于 $\mathcal F_0\subseteq\mathcal F_m$。

设 $p\ge1$。由引理4.1，
$$
h=x^{[p]}\in\mathcal F_{m+p(p+1)}.
$$
令 $y=x-h$，则
$$
y\in\mathcal H^-_{\le p-1},\qquad
T_Ny=T_Nx-T_Nh\in\mathcal F_{m+p(p+1)}.
$$
用归纳假设，
$$
y\in\mathcal F_{m+p(p+1)+C_{p-1}}.
$$
该头也包含 $h$，故
$$
x\in\mathcal F_{m+C_p},
\qquad C_p=p(p+1)+C_{p-1}.
$$
求和得
$$
C_p=\sum_{k=1}^p k(k+1)
=\frac{p(p+1)(p+2)}3.
$$
这就是 (1.4)，其中 $m$ 自始至终表示物理头的位数。

若 $T_Nx=0$，可取 $m=0$，从而 $x$ 属于有限头 $\mathcal F_{C_p}$。
而 $T_N$ 的形式首阶为 1，首系数为 $a_0/d_0\ne0$。
在任何有限头上，它是
$$
B\bigl((a_0/d_0)I+\text{幂零多项式}\bigr),
$$
括号可逆，所以其核只有 $\mathbb Ce_0$。
这证明 (1.5)。

## 6. 有限孔次数的返回刚性

为完整证明定理1.2，
设
$$
x\in\mathcal H^-_{\le p},\qquad
T_Nx\in\mathcal H^-_{\le q},
$$
其中 $p,q$ 都有限。

若 $p=0$，结论成立。
设 $p\ge1$，令
$$
L_0=\max\{p,q-p+2\},\qquad M_0=p(L_0+1).
\tag{6.1}
$$
假设一个第 $p$ 阶集合 $S$ 满足 $\max S\ge M_0$。
把全部 $p$ 个孔排成 $j_1<\cdots<j_p$，设人工起点 $j_0=-1$。
同样的间距计数给某个相邻差至少为 $L_0+2$。
取 $i=j_{\ell-1}+2$、$j=j_\ell$，
便有隔离零、$L=j-i\ge L_0\ge p$。

引理3.1 的输出次数为
$$
\nu(n)=p-1+L\ge q+1.
$$
所以 $(T_Nx)_n=0$，再次迫使这个 $x_S=0$。
因此
$$
x^{[p]}\in\mathcal F_{M_0}.
\tag{6.2}
$$

删去这个有限头顶层后，
$$
y=x-x^{[p]}\in\mathcal H^-_{\le p-1},\qquad
T_Ny\in\mathcal H^-_{\le q'},
\qquad q'=\max\{q,M_0\}.
$$
因为 $T_Nx^{[p]}\in\mathcal F_{M_0}\subseteq\mathcal H^-_{\le M_0}$。
对 $p$ 归纳，$y$ 属于有限头，故 $x$ 也属于有限头。

若需要一个完全确定的界，可以递归定义
$$
R(0,q)=0,
$$
$$
\begin{aligned}
L(p,q)&=\max\{p,q-p+2\},\\
M(p,q)&=p\bigl(L(p,q)+1\bigr),\\
R(p,q)&=\max\left\{M(p,q),
R\bigl(p-1,\max\{q,M(p,q)\}\bigr)\right\}.
\end{aligned}
$$
上述证明给 $x\in\mathcal F_{R(p,q)}$。
这里只主张一个安全的有限界，不追求最优值。

## 7. 任意无限支撑系数：不需要有界空隙

上述唯一行并不依赖 $a_i$ 的大小或相位，
只要求被选中的那个 $a_i\ne0$。
这允许一个不假设支撑空隙有界的推广。

令
$$
T_a=\sum_{j\ge0}a_j\mathsf N_j,\qquad
a\in\ell^1,
$$
且 $\{j:a_j\ne0\}$ 无限。所有系数可以是复数。

### 7.1 有限候选集合一定避开全部坏位置

固定 $p\ge1$，从非零支撑中取前 $p(p+1)+1$ 个指标，
记这个有限集合为 $\mathcal C_p$，其最大值为 $K_p$。

对任意 $p$ 孔集合 $S$，把下列指标称为坏位置：
$$
\mathcal B_p(S)
=
\{i\ge1:i-1\in S\}
\cup
\{i\ge0:[i,i+p-1]\cap S\ne\varnothing\}.
\tag{7.1}
$$
第一部分至多 $p$ 个；
每个孔在第二部分中至多造成 $p$ 个指标，
所以
$$
|\mathcal B_p(S)|\le p(p+1).
\tag{7.2}
$$
因此 $\mathcal C_p$ 中至少有一个非坏指标 $i$。
它满足 $a_i\ne0$、$[i,i+p-1]$ 无孔，
而且 $i>0$ 时前一位 $i-1$ 也无孔。
$i=0$ 不需要任何虚构的负位条件。

### 7.2 顶层支撑界及完整归纳

设 $x\in\mathcal H^-_{\le p}$、$T_ax\in\mathcal F_m$，
并设一个顶层集合 $S$ 满足
$$
\max S>\max\{m,K_p+p\}.
\tag{7.3}
$$
选上节的非坏 $i\in\mathcal C_p$。
由于 $i\le K_p$，$S$ 中在 $i$ 之后确有孔。
记其后的第一个孔为 $j$。于是
$$
j-i\ge p,
$$
且长串的隔离条件全部成立。
引理3.1 逐字适用于 $T_a$，只把 $a_i$ 改为这个非零复系数。

输出 $n=n(S)-2^i$ 必在 $\mathcal F_m$ 之外。
若被借用的孔 $j$ 不是最高孔，最高孔仍保留，故 $n\ge2^{\max S}>2^m$。
若 $j=\max S$，则长串包含第 $j-1$ 位；
由 $j>m$ 得 $j-1\ge m$，故 $n\ge2^m$。
因此 $(T_ax)_n=0$，唯一项迫 $x_S=0$。

所以
$$
\boxed{
x^{[p]}\in
\mathcal F_{\max\{m+1,K_p+p+1\}}.
}
\tag{7.4}
$$
这里的 $m+1$ 不能误删：若 $x=e_{2^m}$，其任何严格降索引的 $T_a$ 像已在
$\mathcal F_m$，但 $x$ 本身未必在 $\mathcal F_m$。

逐层剥去顶次数，重复 (7.4)，给一个明确的安全界
$$
\boxed{
x\in\mathcal F_{\max\{m+p,K_p+2p\}}
\qquad(p\ge1).
}
\tag{7.5}
$$
确实，往下处理次数 $q\le p$ 时，
$K_q\le K_p$，
每步把当前头参数 $m'$ 换成
$\max\{m'+1,K_q+q+1\}$；
至多 $p$ 步后不超过 (7.5)。
$p=0$ 仍为真空情形。

这个证明仅取一个固定的有限非零支撑集合。
即使后续非零系数之间有任意长的空隙，结论仍成立。

### 7.3 无限支撑下的有限次数返回

若只知道 $T_ax\in\mathcal H^-_{\le q}$，
令
$$
L=\max\{p,q-p+2\}.
$$
改取前 $p(L+1)+1$ 个非零指标，最大值记为 $K_{p,L}$；
坏位置改为
$$
\{i:i-1\in S\}\cup\{i:[i,i+L-1]\cap S\ne\varnothing\}.
$$
它至多有 $p(L+1)$ 个元素。
如果 $\max S>K_{p,L}+L$，可选非坏 $i$，
其后第一孔距离至少 $L$。
唯一行的输出次数至少为
$p-1+L\ge q+1$，所以该系数为零。

于是
$$
x^{[p]}\in\mathcal F_{K_{p,L}+L+1}.
$$
剥去顶层，把 $q$ 更新为它与这个有限头位数的最大值，
再对 $p$ 归纳。
得到对任意无限支撑复 $\ell^1$ 列：
$$
\boxed{
x,\ T_ax\text{ 均为有限孔次数}
\ \Longrightarrow\ x\text{ 属于有限头}.
}
\tag{7.6}
$$

无限支撑条件对 (7.6) 不能直接删去。
例如仅取 $T_a=\mathsf N_0$，
并令
$$
x=\sum_{j\ge1}c_je_{\{0,j\}},
\qquad c\in\ell^2\text{ 且支撑无限}.
$$
由于第 0 位已有孔，
$$
\mathsf N_0x=\sum_{j\ge1}c_je_{\{j\}}.
$$
两端次数分别不超过 2 与 1，但 $x$ 不是有限头。

### 7.4 任意非零可和列的有限次数核

令 $a\in\ell^1$ 任意非零，
$j_0=\min\{j:a_j\ne0\}$，$h=2^{j_0}$。
则
$$
\boxed{
\ker T_a\cap\mathcal H^-_{\le p}
=
\mathcal F_{j_0}\cap\mathcal H^-_{\le p}
\quad(p<\infty).
}
\tag{7.7}
$$

若支撑无限，先由 (7.5) 把核向量降到有限头。
在任何有限旗上，
$T_a=B^h((a_{j_0}/d_{j_0})I+\text{幂零多项式})$，
所以核恰为 $\ker B^h=\mathcal F_{j_0}$ 与该有限旗之交。

若支撑有限，则这个因子化本身就是全空间的有限多项式因子化，
括号因 $B$ 拟幂零而为有界单位；
于是全空间核已经恰为 $\mathcal F_{j_0}$。

反向包含直接由所有幂的阶数至少为 $h$。
这证明 (7.7)，也说明具体慢列的真空结论不是正系数巧合。

## 8. 保留的范围

本文没有把边界的孔次数与原 Haar 表示的 Walsh 次数混为一谈。
它也没有把有限次数的稠密并集当作核为零的依据：
实际慢边界核已知包含非真空无限次数向量。

结论不自动推广到
$$
T_Y=\sum_j a_j\mathsf N_j(I+\mathsf N_j)^{-1}.
$$
后者包含全部整数阶项，唯一 dyadic 输入的论证不能直接照搬。
尤其不能仅由 $T_Y-T_N$ 的很小算子范数，
就忽略 (3.3) 中可能更小得多的 $\alpha_j/\alpha_i$；
若要比较，必须另证真实路径的相对估计。

对 R200 的饱和问题，
现在确定了 $M_N$ 中所有非真空向量都具有无限孔次数。
但这没有证明
$$
\overline{BM_N}=M_N,
$$
也没有证明其反面。
边界表示与原 Haar 表示之间的有界交织缺口仍然保留。
