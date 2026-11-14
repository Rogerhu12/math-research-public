# R163：全部不变限制上的高可积性正则化障碍

日期：2026-11-12。作者：l2_moments。
状态：完整证明，根代理已核验核心不等式；本稿给出全部细节。
执行器失效期间直接创建完整 Git blob；不据此修改分支或共享索引。

## 1. 结论与旧结果的区别

沿用 $H=L^2(\mathbb Z_2,\mu)$ 与实际 $A$。
设 $M\subseteq H$ 为闭 $A$ 不变子空间，
$B:M\to H$ 为有界线性算子，满足
$$
BA|_M=AB.
\tag{1.1}
$$

**定理1.1。** 对任意 $2<p\le\infty$，
$$
\boxed{\operatorname{Ran}B\subseteq L^p(\mathbb Z_2)
\quad\Longrightarrow\quad B=0.}
\tag{1.2}
$$
这里只要求集合包含，没有预先假设 $B:M\to L^p$ 有界。

因此非零闭不变 $M$ 不可能整个包含于任何 $L^p$、$p>2$。
对候选核空间也一样：任何非零有界交织都不能把整个核统一送进
更高 $L^p$ 或有界函数类。

已对照旧稿：

- R44 §6 排除了全空间交换子 $YH\subset C(\mathbb Z_2)$；
  证明依赖连续代表与整数点评价。
- R51 §§5–6 排除了任意闭不变限制上的全局 Walsh 次数权域
  及固定阶位置权域平滑。
- 本稿直接处理实空间 $L^p$ 可积性，不要求连续代表、次数衰减、
  位置权或点迹。其结论也在所有闭不变限制上成立。

这些结论不互相等价。本稿没有把 $L^p$ 包含在某个固定 Walsh 正则域中，
也没有把非紧的 $L^p\hookrightarrow L^2$ 嵌入当成紧算子。

## 2. 固定长度的高位创建块与物理柱投影

记
$$
N_j=\frac{A^{2^j}}{W_{2^j}},\qquad E_j=e_{10}^{(j)}.
$$
已有
$$
\|N_j\|=\|E_j\|=1,\qquad
\|N_j-E_j\|=\eta_j,\qquad\eta_j\to0.
\tag{2.1}
$$
$N_j$ 是 $A$ 的多项式。

固定一个正整数 $r$，对 $m\ge0$ 取
$$
J_m=\{m,m+1,\ldots,m+r-1\},
\quad
F_m=\prod_{j\in J_m}N_j,
\quad
E_{J_m}=\prod_{j\in J_m}E_j.
\tag{2.2}
$$
再令 $P_m$ 为乘以物理柱指示函数的正交投影：
$$
P_mh=1_{\{b_j=1\ \forall j\in J_m\}}h,
\qquad \mu(\operatorname{supp}P_m)=2^{-r}.
\tag{2.3}
$$
$P_m$ 不要求保持 $M$。真正保持 $M$ 的是 $F_m$，
因为它是 $A$ 的有限多项式。

由排序望远镜和全部因子范数不超过1，
$$
\|F_m-E_{J_m}\|\le\sum_{j\in J_m}\eta_j\longrightarrow0
\quad(m\to\infty,\ r\text{ 固定}).
\tag{2.4}
$$

**引理2.1。** 对每个固定 $h\in H$ 与固定 $r$，
$$
\boxed{
\|F_mh-P_mh\|_2\to0,\qquad
\|P_mh\|_2\to2^{-r/2}\|h\|_2.
}
\tag{2.5}
$$
所以
$$
\boxed{
\|F_mh\|_2\to2^{-r/2}\|h\|_2,\qquad
\|P_mF_mh\|_2\to2^{-r/2}\|h\|_2.
}
\tag{2.6}
$$

**证明。** 若 $h_0$ 只依赖有限低位，且 $m$ 超过其全部位，
每个 $E_j$ 将该位的常函数 $(1,1)$ 送为 $(0,1)$，
故
$$
E_{J_m}h_0=P_mh_0.
$$
两者范数均不超过1，所以对一般 $h$，
$$
\|(E_{J_m}-P_m)h\|_2\le2\|h-h_0\|_2
$$
在足够大的 $m$ 上成立。
先取 $m\to\infty$，再使 $h_0\to h$，结合 (2.4)，得第一式。

对这样的 $h_0$，独立位直接给
$$
\|P_mh_0\|_2=2^{-r/2}\|h_0\|_2.
$$
再用 $\|P_m\|\le1$ 和有限柱的 $L^2$ 密度即得第二式。
(2.6) 的第一式由三角不等式推出；
第二式利用
$$
\|P_mF_mh-P_mh\|_2\le\|F_mh-P_mh\|_2.
$$
证毕。

极限次序是先固定 $r$，再令 $m\to\infty$。
没有要求此逼近对同时增长的 $r,m$ 一致，
没有要求 $h$ 具备任何预定的尾速率。

## 3. Banach 闭图先给出真实 $L^p$ 算子界

假设 $\operatorname{Ran}B\subseteq L^p$，$2<p\le\infty$。
将同一个线性映射视为
$$
B_p:M\longrightarrow L^p.
$$
若 $x_n\to x$ 于 $M$，且 $Bx_n\to h$ 于 $L^p$，
由于 $\mu$ 为概率测度，$L^p\hookrightarrow L^2$ 连续，
所以 $Bx_n\to h$ 于 $H$。
另一方面原来的有界 $B:M\to H$ 给 $Bx_n\to Bx$ 于 $H$，
故 $h=Bx$。
因此 $B_p$ 图闭。

$M$ 与 $L^p$ 均为 Banach 空间，包括 $p=\infty$，
闭图定理给一个有限常数 $C_p$，满足
$$
\boxed{\|Bx\|_p\le C_p\|x\|_2\qquad(x\in M).}
\tag{3.1}
$$
这一常数是由集合包含推出的，不是额外假设。

## 4. 高位压缩与 Hölder 不等式排除非零交织

固定 $x\in M$，记 $h=Bx$。
因为 $F_m$ 是 $A$ 的多项式，(1.1) 给
$$
F_mx\in M,\qquad BF_mx=F_mh.
\tag{4.1}
$$
由 (3.1)，
$$
\|F_mh\|_p\le C_p\|F_mx\|_2.
\tag{4.2}
$$

记
$$
\theta_p=\frac12-\frac1p>0,
$$
其中 $1/\infty=0$。
在测度为 $2^{-r}$ 的柱上，Hölder 不等式给
$$
\|P_mF_mh\|_2
\le2^{-r\theta_p}\|F_mh\|_p
\le2^{-r\theta_p}C_p\|F_mx\|_2.
\tag{4.3}
$$
先固定 $r$，令 $m\to\infty$。
由 (2.6)，得到
$$
2^{-r/2}\|h\|_2
\le2^{-r\theta_p}C_p2^{-r/2}\|x\|_2.
$$
消去正数 $2^{-r/2}$，
$$
\boxed{\|Bx\|_2\le C_p2^{-r\theta_p}\|x\|_2
\quad\text{对每个固定整数 }r\ge1.}
\tag{4.4}
$$
现在才令 $r\to\infty$。
因为 $\theta_p>0$，(4.4) 给 $Bx=0$。
$x$ 任意，故 $B=0$，定理1.1得证。

这里从未使用 $P_mM\subseteq M$；
$P_m$ 仅用于输出上的 Hölder 估计。
也没有把物理柱投影误认为 $A$ 的多项式。

## 5. 非零交织的通常输出同时不属于任何更高 $L^p$

还能得到一个准确的 Baire 范畴加强。

设 $B\ne0$，固定 $p>2$，令
$$
\mathcal D_p=\{x\in M:Bx\in L^p\},
\qquad
K_n=\{x\in M:\|Bx\|_p\le n\}.
$$
这里把不属于 $L^p$ 的向量之范数记为 $+\infty$。
$L^p$ 范数对 $L^2$ 收敛下半连续：
取几乎处处收敛子列并用 Fatou；$p=\infty$ 时用几乎处处的本质上界。
所以每个 $K_n$ 在 $M$ 中闭，且
$$
\mathcal D_p=\bigcup_{n\ge1}K_n.
$$

若某个 $K_n$ 含一个开球 $B_M(x_0,\varepsilon)$，
则对 $\|y\|_2<\varepsilon$，
$x_0+y,x_0$ 都在该球内，可得
$$
\|By\|_p\le\|B(x_0+y)\|_p+\|Bx_0\|_p\le2n.
$$
缩放便推出 $\operatorname{Ran}B\subseteq L^p$，
由主定理迫 $B=0$，矛盾。
因此每个 $K_n$ 都闭且无内点，$\mathcal D_p$ 为第一纲 $F_\sigma$ 集。

对可数列 $p_k=2+1/k$ 取交，
$$
\boxed{
\{x\in M:Bx\notin L^p\text{ 对全部 }p>2\}
\text{ 在 }M\text{ 中为稠密剩余集}.
}
\tag{5.1}
$$
因为若某输出属于一个 $L^p$、$p>2$，
选 $k$ 使 $p_k<p$，便属于 $L^{p_k}$。
这个加强不声称每个非零输出都粗糙；
可能有个别或稠密的特殊向量落入更高可积类。

取恒等包含交织 $M\hookrightarrow H$，
每个非零闭 $A$ 不变子空间中的通常向量都同时不在任何 $L^p$、$p>2$。
这与 $H$ 中许多具体循环向量非常规则并不冲突。

## 6. 有限放大版本

设 $M\subseteq H^{\oplus d}$ 闭且对 $A^{(d)}$ 不变，
$B:M\to H^{\oplus s}$ 有界并交织相应放大。
若
$$
BM\subseteq L^p(\mathbb Z_2;\mathbb C^s),\qquad p>2,
$$
则 $B=0$。

证明把 $F_m$、$P_m$ 分别对输入和输出逐分量放大。
引理2.1对有限多个坐标相加仍给相同的 $2^{-r/2}$ 极限。
Hölder 使用点态欧氏范数，闭图与 (4.3) 完全不变。
无需放大维数相关的常数来改变指数衰减。

## 7. 对当前研究路线的准确含义

本稿堵住的是统一正则化方案：
不能仅找一个非零有界交织，把未知闭不变空间或候选核的全部向量
送进 $L^\infty$、有界有限 chaos 或任何固定 $L^p$、$p>2$，
再借已知规则端点循环结论排核。

仍然允许：

1. 对一个特定核向量获得额外可积性；
2. 使用真正的核方程证明一种核特有的正则性，
   此时主定理反而可作为最后的反证；
3. 采用无界、但定义域已严格控制的正则化；
4. 使用不改善 $L^p$ 的结构性约束。

这些结论不判断慢共振平方是否有核，也不解决完整 ISP。
